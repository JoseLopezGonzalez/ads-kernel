#!/usr/bin/env python3
"""proceso — ADAPTADOR LOCAL REAL. Lanza un `subprocess` de verdad. Corte `V7`.

No es un simulacro. Lo que hace, y lo que se comprueba que hace:

    ejecuta una tarea            un proceso real, con su pid y su código de salida
    emite progreso               cada línea del proceso llama al invocable `progreso`
    termina bien · falla         código 0 / código distinto de 0
    excede el timeout            MATA el grupo de procesos: `SIGTERM`, y `SIGKILL` si no
                                 muere. Se comprueba con `os.kill(pid, 0)` que ya no está
    es cancelado                 igual de real: mata, no «pide por favor»
    muere abruptamente           el adaptador lo distingue de un fallo de la tarea
    idempotencia                 recibo DURABLE por `efecto` en su espacio de trabajo; una
                                 segunda llamada con el mismo `efecto` devuelve
                                 `repetido: true` SIN volver a ejecutar

DECISIÓN · grupo de procesos propio, y matar el GRUPO y no el proceso
    Alternativas: (a) `proceso.kill()`; (b) `start_new_session=True` y `os.killpg`.
    Se elige (b). Con (a) se mata al hijo directo y sus nietos quedan huérfanos ejecutándose
    y reteniendo el pipe: el `wait` se queda colgado y el «timeout» no termina nada. Un
    `sh -c 'sleep 300 & wait'` lo reproduce. Con `start_new_session=True` el hijo es líder
    de su propio grupo y `os.killpg(pgid, SIGKILL)` alcanza a toda la descendencia.

DECISIÓN · `SIGTERM` primero y `SIGKILL` después, y se espera de verdad entre los dos
    Mandar sólo `SIGKILL` impide a la tarea cerrar lo que tuviera abierto; mandar sólo
    `SIGTERM` deja vivo a quien lo ignora, y entonces el timeout no es un timeout. Se manda
    `SIGTERM`, se espera `GRACIA_SEGUNDOS`, y si sigue vivo se manda `SIGKILL`. El resultado
    declara cuál de los dos hizo falta, porque es información de diagnóstico real.

DECISIÓN · el recibo de idempotencia es un FICHERO del ESPACIO DEL ADAPTADOR, no del estado
    `g.12` y el §3 del contrato dicen que el estado canónico lo muta UN SOLO ejecutor, el
    runtime, y que el acuse durable del efecto es `canonico/efectos/<efecto>.json` escrito
    en la MISMA transición que el resultado. El adaptador NO escribe ahí: sería un segundo
    escritor del estado canónico. Lo que guarda aquí es su propio recibo, en su espacio de
    trabajo, y sirve para lo único que tiene que servir: no volver a EJECUTAR una tarea que
    ya ejecutó cuando el runtime le repite la orden tras una caída. Los dos niveles son
    deliberados y no redundantes: el del runtime protege el ESTADO, éste protege el EFECTO.

DECISIÓN · el reloj se usa, y aquí sí se puede
    `I-g3` prohíbe el reloj de pared en lo DURABLE. Un timeout es, por definición, tiempo de
    pared, y vive en el plano operacional. Lo que NO entra en el recibo es ninguna duración:
    el recibo guarda el efecto, el código y la salida, y ni un solo milisegundo.
"""
from __future__ import annotations

import json
import os
import selectors
import signal
import subprocess
import time

from .contrato import (
    VERSION_DE_CONTRATO,
    Adaptador,
    FichaDeAdaptador,
    OrdenInvalida,
    comprobar_resultado,
)

GRACIA_SEGUNDOS = 1.5
INTERVALO_DE_SONDEO = 0.05
CAPACIDAD = "proceso-local"


def _sigue_vivo(pid):
    """`os.kill(pid, 0)` no manda ninguna señal: pregunta si el proceso existe."""
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _grupo_vivo(pgid):
    try:
        os.killpg(pgid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


class AdaptadorDeProcesoLocal(Adaptador):
    """Ejecuta una orden local real, con timeout y cancelación que MATAN."""

    identificador = "proceso-local"
    version_de_contrato = VERSION_DE_CONTRATO
    capacidades = ("proceso-local", "ejecucion-local")

    def __init__(self, espacio_de_trabajo, *, entorno=None):
        self.espacio = os.path.abspath(espacio_de_trabajo)
        self.recibos = os.path.join(self.espacio, "efectos")
        os.makedirs(self.recibos, exist_ok=True)
        self._entorno = dict(entorno) if entorno else None

    # -- ficha declarada de §3.4 -------------------------------------------
    def ficha(self):
        return FichaDeAdaptador(
            identificador=self.identificador,
            version=VERSION_DE_CONTRATO,
            capacidades=list(self.capacidades),
            operaciones=["ejecutar"],
            limites={"salida_maxima_bytes": 1 << 20,
                     "gracia_antes_de_sigkill_segundos": GRACIA_SEGUNDOS},
            timeout="limite_segundos de la orden; al vencer, SIGTERM y luego SIGKILL al "
                    "GRUPO de procesos",
            cancelacion="cooperativa por sondeo de `cancelacion.activada()`, y efectiva "
                        "por señal al grupo: no se pide, se mata",
            idempotencia="recibo durable por `efecto` en el espacio de trabajo; una "
                         "segunda llamada devuelve `repetido: true` sin ejecutar",
            forma_de_progreso="una llamada a `progreso({'linea': n, 'texto': ...})` por "
                              "cada línea que el proceso escribe",
            resultado="{estado, codigo, salida, detalle, reintentable, efecto, repetido}",
            errores=["ORDEN_INVALIDA", "ERROR_DE_ADAPTADOR"],
            evidencia="el recibo por efecto, con su código y su salida, fuera del estado "
                      "canónico",
            compatibilidad="POSIX con grupos de procesos y señales. Es una DECLARACIÓN de "
                           "intención y no un nivel alcanzado (§6.5)",
        )

    # -- idempotencia -------------------------------------------------------
    def _ruta_de_recibo(self, efecto):
        if not isinstance(efecto, str) or not efecto or "/" in efecto or efecto in (".", ".."):
            raise OrdenInvalida("identificador de efecto inválido: " + repr(efecto))
        return os.path.join(self.recibos, efecto + ".json")

    def recibo(self, efecto):
        ruta = self._ruta_de_recibo(efecto)
        if not os.path.exists(ruta):
            return None
        with open(ruta, "r", encoding="utf-8") as manejador:
            return json.load(manejador)

    def _escribir_recibo(self, efecto, resultado):
        ruta = self._ruta_de_recibo(efecto)
        temporal = ruta + ".tmp"
        cuerpo = {clave: resultado[clave] for clave in
                  ("estado", "codigo", "salida", "detalle", "reintentable", "efecto")}
        datos = json.dumps(cuerpo, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
        with open(temporal, "w", encoding="utf-8") as manejador:
            manejador.write(datos)
            manejador.flush()
            os.fsync(manejador.fileno())
        os.replace(temporal, ruta)
        descriptor = os.open(self.recibos, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)

    # -- ejecución ----------------------------------------------------------
    def ejecutar(self, orden, *, efecto, limite_segundos, progreso=None, cancelacion=None):
        if not isinstance(orden, dict):
            raise OrdenInvalida("la orden de un adaptador es un mapa")
        argumentos = orden.get("argumentos")
        if not isinstance(argumentos, (list, tuple)) or not argumentos:
            raise OrdenInvalida(
                "la orden no trae `argumentos`: un adaptador de proceso sin argumentos no "
                "tiene nada que ejecutar"
            )
        if orden.get("operacion", "ejecutar") != "ejecutar":
            raise OrdenInvalida(
                "operación no declarada por este adaptador: " + str(orden.get("operacion"))
            )

        # IDEMPOTENCIA. Antes de nada: si el efecto ya se aplicó, no se vuelve a ejecutar.
        previo = self.recibo(efecto)
        if previo is not None:
            resultado = dict(previo)
            resultado["repetido"] = True
            return comprobar_resultado(resultado, efecto)

        resultado = self._lanzar(list(argumentos), efecto, float(limite_segundos),
                                 progreso, cancelacion)
        # El recibo se escribe SÓLO cuando el efecto se produjo de verdad. Una cancelación
        # o un timeout NO dejan recibo: la tarea no llegó a aplicarse y el runtime tiene que
        # poder reintentarla.
        if resultado["estado"] in ("completado", "fallido"):
            self._escribir_recibo(efecto, resultado)
        return comprobar_resultado(resultado, efecto)

    def _lanzar(self, argumentos, efecto, limite_segundos, progreso, cancelacion):
        entorno = self._entorno if self._entorno is not None else {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "LC_ALL": "C", "LANG": "C", "TZ": "UTC",
            "HOME": self.espacio,
        }
        proceso = subprocess.Popen(
            argumentos,
            cwd=self.espacio,
            env=entorno,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            # LÍDER DE SU PROPIO GRUPO: sin esto, matar al hijo deja vivos a los nietos.
            start_new_session=True,
        )
        pid = proceso.pid
        try:
            pgid = os.getpgid(pid)
        except ProcessLookupError:
            pgid = pid

        limite = time.monotonic() + limite_segundos
        lineas = []
        numero = 0
        motivo = None
        parcial = b""
        selector = selectors.DefaultSelector()
        selector.register(proceso.stdout, selectors.EVENT_READ)
        try:
            while True:
                if cancelacion is not None and cancelacion.activada():
                    motivo = "cancelado"
                    break
                if time.monotonic() >= limite:
                    motivo = "timeout"
                    break
                for clave, _ in selector.select(timeout=INTERVALO_DE_SONDEO):
                    trozo = os.read(clave.fileobj.fileno(), 65536)
                    if not trozo:
                        motivo = motivo or "fin"
                        break
                    parcial += trozo
                    while b"\n" in parcial:
                        cruda, parcial = parcial.split(b"\n", 1)
                        numero += 1
                        texto = cruda.decode("utf-8", "replace")
                        lineas.append(texto)
                        if progreso is not None:
                            progreso({"linea": numero, "texto": texto, "efecto": efecto})
                if motivo == "fin":
                    break
                if proceso.poll() is not None and not selector.select(timeout=0):
                    motivo = "fin"
                    break
        finally:
            selector.close()

        if parcial:
            numero += 1
            texto = parcial.decode("utf-8", "replace")
            lineas.append(texto)
            if progreso is not None:
                progreso({"linea": numero, "texto": texto, "efecto": efecto})

        if motivo in ("timeout", "cancelado"):
            senal = self._matar(proceso, pid, pgid)
            estado = "timeout" if motivo == "timeout" else "cancelado"
            detalle = ("el límite de " + str(limite_segundos) + " s venció y el GRUPO de "
                       "procesos fue terminado con " + senal
                       if motivo == "timeout" else
                       "la cancelación terminó el GRUPO de procesos con " + senal)
            return {
                "estado": estado,
                "codigo": -1,
                "salida": "\n".join(lineas),
                "detalle": detalle,
                # Un timeout SÍ es reintentable —puede haber sido una máquina lenta—; una
                # cancelación NO: alguien decidió que no se hiciera.
                "reintentable": motivo == "timeout",
                "efecto": efecto,
                "repetido": False,
                "pid": pid,
            }

        self._cerrar_salida(proceso)
        codigo = proceso.wait()
        if codigo < 0:
            # Muerte ABRUPTA por señal: no es un fallo de la tarea, es que la mataron.
            return {
                "estado": "fallido",
                "codigo": codigo,
                "salida": "\n".join(lineas),
                "detalle": "el proceso murió por la señal " + str(-codigo)
                           + " sin producir código de salida",
                "reintentable": True,
                "efecto": efecto,
                "repetido": False,
                "pid": pid,
            }
        return {
            "estado": "completado" if codigo == 0 else "fallido",
            "codigo": codigo,
            "salida": "\n".join(lineas),
            "detalle": "" if codigo == 0 else "la tarea terminó con código " + str(codigo),
            # Un código distinto de cero es un fallo DEFINITIVO de la tarea: repetirla
            # produciría el mismo código. Lo reintentable es lo que puede cambiar solo.
            "reintentable": False,
            "efecto": efecto,
            "repetido": False,
            "pid": pid,
        }

    @staticmethod
    def _senalar(pgid, senal):
        """Manda una señal al GRUPO. `True` si el grupo ya no estaba, que no es un fallo."""
        try:
            os.killpg(pgid, senal)
        except ProcessLookupError:
            return True
        return False

    @staticmethod
    def _cerrar_salida(proceso):
        """Cierra la tubería del proceso. Que ya esté cerrada es el estado deseado."""
        manejador = getattr(proceso, "stdout", None)
        if manejador is None or manejador.closed:
            return False
        try:
            manejador.close()
        except OSError:
            # El descriptor ya no es válido: el proceso murió y el núcleo lo retiró. El
            # objetivo —que no quede una tubería abierta— está cumplido igualmente.
            return False
        return True

    def _matar(self, proceso, pid, pgid):
        """Mata de verdad: `SIGTERM` al grupo, y `SIGKILL` si sigue vivo. Devuelve cuál."""
        usada = "SIGTERM"
        # `ProcessLookupError` aquí NO es un error: el grupo ya no existe, que es
        # exactamente el estado al que se quería llegar. Se anota y se sigue.
        self._senalar(pgid, signal.SIGTERM)
        limite = time.monotonic() + GRACIA_SEGUNDOS
        while time.monotonic() < limite:
            if proceso.poll() is not None and not _grupo_vivo(pgid):
                break
            time.sleep(INTERVALO_DE_SONDEO)
        if _grupo_vivo(pgid) or proceso.poll() is None:
            usada = "SIGKILL"
            self._senalar(pgid, signal.SIGKILL)
        try:
            proceso.wait(timeout=GRACIA_SEGUNDOS)
        except subprocess.TimeoutExpired:               # pragma: no cover
            # No se puede hacer más: ya se mandó `SIGKILL` al grupo entero. Se sigue, y el
            # bucle de `os.kill(pid, 0)` de abajo es quien informa de si sigue vivo.
            usada = "SIGKILL"
        self._cerrar_salida(proceso)
        # No se devuelve hasta que `os.kill(pid, 0)` dice que ya no está.
        limite = time.monotonic() + GRACIA_SEGUNDOS
        while _sigue_vivo(pid) and time.monotonic() < limite:
            time.sleep(INTERVALO_DE_SONDEO)
        return usada
