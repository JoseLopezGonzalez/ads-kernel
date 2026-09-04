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
    de su propio grupo y `os.killpg(pgid, SIGKILL)` alcanza a toda la descendencia
    **QUE NO SE SAQUE DEL GRUPO**.

LÍMITE DECLARADO · un descendiente que hace `setsid` ESCAPA, y esto está MEDIDO
    Una promesa que la primera embestida desmonta es peor que una limitación declarada, así
    que se dice con todas las letras: `os.killpg` alcanza a un grupo de procesos, y un
    descendiente que llama a `setsid()` deja de pertenecer a ese grupo. Medido: un nieto
    lanzado con `setsid` SOBREVIVE al timeout y a la cancelación. NO es un fallo de esta
    implementación: es el techo de lo que las señales de grupo pueden hacer.
    Contenerlo exige envolver la tarea en un contenedor de recursos del sistema —un cgroup
    v2 con `cgroup.kill`, o un espacio de nombres de PID donde matar al PID 1 se lleve todo
    por delante—, y eso es materia de OTRO CORTE: exige privilegios, montar `cgroup2` y
    decidir la política de recursos, nada de lo cual está en el alcance de `V7`.
    Lo que SÍ se garantiza aquí, y se prueba: toda la descendencia que permanece en el grupo
    muere, incluido el nieto ordinario, y se comprueba con `os.kill(pid, 0)`.

DECISIÓN · `SIGTERM` primero y `SIGKILL` después, y se espera de verdad entre los dos
    Mandar sólo `SIGKILL` impide a la tarea cerrar lo que tuviera abierto; mandar sólo
    `SIGTERM` deja vivo a quien lo ignora, y entonces el timeout no es un timeout. Se manda
    `SIGTERM`, se espera `GRACIA_SEGUNDOS`, y si sigue vivo se manda `SIGKILL`. El resultado
    declara cuál de los dos hizo falta, porque es información de diagnóstico real.

DECISIÓN · el recibo se ABRE antes de ejecutar y se CIERRA después, y por eso la duplicación
           es DETECTABLE
    EL DEFECTO, medido: el recibo se escribía SÓLO al terminar. Si el proceso moría entre
    ejecutar la tarea y escribir el recibo, al reiniciar no había rastro, el adaptador
    volvía a ejecutar y el efecto se aplicaba DOS VECES en silencio —dos marcas en disco,
    `"repetido": false` en las dos pasadas—.
    Alternativas: (a) cerrar la ventana; (b) hacerla DETECTABLE.
    Se elige (b), porque (a) es imposible: con un proceso externo cualquiera no existe
    «exactamente una vez», y prometerlo sería mentir. Lo que sí existe es no duplicar en
    silencio. El recibo se abre ANTES de lanzar, con estado `iniciado`, y se cierra después
    con el resultado; los dos con `fsync`. Una segunda llamada que encuentre un recibo
    `iniciado` y SIN CERRAR no ejecuta y devuelve `ambiguo`: nadie puede saber si la tarea
    llegó a aplicarse, y decirlo es más honesto que adivinar en cualquiera de los dos
    sentidos.

DECISIÓN · un `timeout` o una `cancelacion` RETIRAN el recibo; una caída lo deja abierto
    Y la diferencia no es un capricho: es si SOBREVIVIÓ UN TESTIGO. Cuando el propio
    adaptador mata la tarea, ese proceso presenció la terminación y puede declarar el
    desenlace, así que retira el recibo y el runtime puede reintentar —que es lo que el
    contrato ya declara para `timeout`—. Cuando el que muere es el adaptador, no queda
    nadie que sepa qué pasó, y ahí es donde `ambiguo` es la única respuesta honesta.
    Queda declarado el residuo: un `timeout` retirado y reintentado PUEDE duplicar si la
    tarea alcanzó a aplicarse antes de morir. Se conserva porque cambiarlo alteraría la
    semántica de reintento contra la que el runtime ya programa, y se dice aquí en vez de
    esconderse.

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
    AMBIGUO,
    VERSION_DE_CONTRATO,
    Adaptador,
    FichaDeAdaptador,
    OrdenInvalida,
    comprobar_resultado,
)
from . import puntero

GRACIA_SEGUNDOS = 1.5
INTERVALO_DE_SONDEO = 0.05
CAPACIDAD = "proceso-local"

# ===========================================================================
#  Puntos de fallo controlados del adaptador
# ===========================================================================
#  Mismo criterio que `estado/fallos.py`: una ventana que sólo se ha visto NO fallar no está
#  verificada, y un corte no se argumenta, se provoca. `os._exit(70)` mata sin ejecutar
#  `finally`, sin `atexit` y sin vaciar búferes: lo más parecido a un corte de corriente.
#  Sin la variable puesta, este código no hace absolutamente nada.
VARIABLE_DE_FALLO = "ADS_ADAPTADOR_FALLO"
CODIGO_DE_SALIDA = 70

PUNTOS_DE_FALLO = (
    "antes-de-abrir-el-recibo",
    "despues-de-abrir-el-recibo-antes-de-ejecutar",
    # ÉSTE es el que faltaba, y el que dejaba duplicar un efecto en silencio.
    "despues-de-ejecutar-antes-de-cerrar-el-recibo",
)


def puntos_de_fallo():
    """Los puntos declarados. Una prueba comprueba que ninguno queda sin llamar."""
    return list(PUNTOS_DE_FALLO)


def _punto(nombre):
    """Corta el proceso si el entorno pide ESTE punto. Una errata es un FALLO, no un silencio."""
    if nombre not in PUNTOS_DE_FALLO:
        raise OrdenInvalida("punto de fallo no declarado: " + str(nombre))
    pedido = os.environ.get(VARIABLE_DE_FALLO)
    if not pedido:
        return
    if pedido not in PUNTOS_DE_FALLO:
        # Con el nombre mal escrito, una prueba pasaría en verde sin haber inyectado nada y
        # publicaríamos como evidencia una ejecución en la que nunca hubo corte.
        raise OrdenInvalida(
            "punto de fallo desconocido en " + VARIABLE_DE_FALLO + ": " + str(pedido)
            + ". Declarados: " + ", ".join(PUNTOS_DE_FALLO)
        )
    if pedido == nombre:
        os._exit(CODIGO_DE_SALIDA)


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

    def __init__(self, espacio_de_trabajo, *, entorno=None, politica_de_contencion=None):
        self.espacio = os.path.abspath(espacio_de_trabajo)
        self.recibos = os.path.join(self.espacio, "efectos")
        os.makedirs(self.recibos, exist_ok=True)
        self._entorno = dict(entorno) if entorno else None
        # `FD-5`. Sin política, el comportamiento es EXACTAMENTE el de antes —`killpg`, con
        # su límite declarado y medido—. Con política, la tarea corre dentro de un contenedor
        # de recursos del anfitrión y la ausencia de contención fuerte es FALLO CERRADO, no
        # degradación silenciosa: el que decide no es el adaptador, es la política.
        self._politica_de_contencion = politica_de_contencion
        self._capacidades_de_contencion = None
        self._backend_de_contencion = None
        self._evidencia_de_contencion = None
        if politica_de_contencion is not None:
            self._elegir_contencion_ahora()

    def _elegir_contencion_ahora(self):
        """`E-16` · el FALLO CERRADO ocurre al CONSTRUIR, no al ejecutar la primera tarea.

        HECHO REPRODUCIDO ANTES DE CORREGIR: la política de contención estaba CONSTRUIDA y
        ningún punto ejecutable podía activarla —la cadena `contencion` no aparecía en
        ninguno de los cinco `ads_*.py`—, así que el fallo cerrado que este paquete promete
        no era alcanzable desde el camino productivo. Al cablearla hace falta decidir CUÁNDO
        falla.

        DECISIÓN · se elige el backend al construir el adaptador
            Alternativas: (a) elegirlo en la primera tarea; (b) elegirlo al construir.
            Se elige (b). Con (a), un anfitrión sin contención fuerte deja adquirir el lease,
            abrir el recibo del efecto y empezar el despacho antes de descubrir que no puede
            ejecutar: eso es EJECUCIÓN PARCIAL, y `FD-5` exige CERO ejecución. Con (b) el
            proceso se detiene antes de tocar nada, y el sondeo —que llama a `docker`, a
            `systemd` y al núcleo— se paga UNA vez y se reutiliza en cada tarea, en vez de
            repetirse por tarea.
        """
        from contencion import deteccion as _deteccion                # noqa: PLC0415
        from contencion import politica as _politica                  # noqa: PLC0415

        self._capacidades_de_contencion = _deteccion.capacidades()
        # `elegir` levanta `ContencionFuerteNoDisponible` o `BackendNoDisponible`. No se
        # captura: sin contención no se ejecuta, y el que decide es la política.
        self._backend_de_contencion, self._evidencia_de_contencion = _politica.elegir(
            self._politica_de_contencion, self._capacidades_de_contencion)

    # -- ficha declarada de §3.4 -------------------------------------------
    def ficha(self):
        return FichaDeAdaptador(
            identificador=self.identificador,
            version=VERSION_DE_CONTRATO,
            capacidades=list(self.capacidades),
            operaciones=["ejecutar"],
            limites={"salida_maxima_bytes": 1 << 20,
                     "gracia_antes_de_sigkill_segundos": GRACIA_SEGUNDOS},
            timeout="limite_segundos de la orden; al vencer, SIGTERM y luego SIGKILL a "
                    "TODO el contenedor de recursos, o al GRUPO si no hay política",
            cancelacion=self._cancelacion_declarada(),
            idempotencia="recibo durable por `efecto`, ABIERTO antes de ejecutar y CERRADO "
                         "después. Recibo cerrado → `repetido: true` con su resultado, sin "
                         "ejecutar. Recibo abierto → `ambiguo`, porque nadie sobrevivió "
                         "para saber si la tarea se aplicó. NO se promete «exactamente una "
                         "vez»: se promete no duplicar en silencio",
            forma_de_progreso="una llamada a `progreso({'linea': n, 'texto': ...})` por "
                              "cada línea que el proceso escribe",
            resultado="{estado, codigo, salida, detalle, reintentable, efecto, repetido}; "
                      "`estado` en completado · fallido · cancelado · timeout · ambiguo",
            errores=["ORDEN_INVALIDA", "ERROR_DE_ADAPTADOR"],
            evidencia="el recibo por efecto, con su código y su salida, fuera del estado "
                      "canónico",
            compatibilidad="POSIX con grupos de procesos y señales. Es una DECLARACIÓN de "
                           "intención y no un nivel alcanzado (§6.5)",
            resolucion_del_control_repo=puntero.DESENLACES_DECLARADOS,
        )

    def _cancelacion_declarada(self):
        """El nivel de aislamiento que la ficha declara es el REAL, no el aspiracional.

        `FD-5` se cerró mintiendo una vez y no se cierra dos: sin política de contención el
        límite del `setsid` SIGUE ESTANDO y se dice con todas las letras; con política, el
        nivel lo declara el propio paquete de contención, que es quien lo ha medido.
        """
        if self._politica_de_contencion is None:
            return ("cooperativa por sondeo de `cancelacion.activada()`, y efectiva por "
                    "señal al GRUPO: no se pide, se mata. NIVEL `grupo-de-procesos`. "
                    "LÍMITE MEDIDO: un descendiente que hace `setsid` sale del grupo y "
                    "ESCAPA. Para contenerlo se construye el adaptador con "
                    "`politica_de_contencion`, y entonces el nivel sube a "
                    "`arbol-de-procesos`")
        return ("cooperativa por sondeo de `cancelacion.activada()`, y efectiva por "
                "destrucción del CONTENEDOR DE RECURSOS del anfitrión que exige la política "
                "`" + str(self._politica_de_contencion.nivel_exigido) + "`, servida por el "
                "backend `" + str(self._backend_de_contencion) + "` ELEGIDO Y COMPROBADO al "
                "construir el adaptador. Un descendiente que hace `setsid` NO escapa, y "
                "está medido con hijo, nieto y bisnieto. Si el anfitrión no ofrece "
                "contención fuerte, el adaptador FALLA CERRADO y no ejecuta")

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

    def _publicar_recibo(self, efecto, cuerpo):
        """Publica el recibo con `fsync` del fichero y del directorio. Atómico por `replace`."""
        ruta = self._ruta_de_recibo(efecto)
        temporal = ruta + ".tmp"
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
        return ruta

    def _abrir_recibo(self, efecto):
        """ANTES de lanzar. Deja constancia durable de que este efecto SE INTENTÓ."""
        return self._publicar_recibo(efecto, {"efecto": efecto, "estado": "iniciado",
                                              "cerrado": False})

    def _cerrar_recibo(self, efecto, resultado):
        """DESPUÉS de terminar. El recibo pasa a llevar el desenlace y queda CERRADO."""
        cuerpo = {clave: resultado[clave] for clave in
                  ("estado", "codigo", "salida", "detalle", "reintentable", "efecto")}
        cuerpo["cerrado"] = True
        return self._publicar_recibo(efecto, cuerpo)

    def _retirar_recibo(self, efecto):
        """Sólo cuando ESTE proceso presenció la terminación: el efecto no se aplicó."""
        ruta = self._ruta_de_recibo(efecto)
        if os.path.exists(ruta):
            os.remove(ruta)
            descriptor = os.open(self.recibos, os.O_RDONLY)
            try:
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
            return True
        return False

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

        # IDEMPOTENCIA, en sus DOS casos.
        previo = self.recibo(efecto)
        if previo is not None:
            if previo.get("cerrado"):
                # Recibo CERRADO: se sabe qué pasó. No se vuelve a ejecutar y se reutiliza.
                resultado = {clave: previo[clave] for clave in
                             ("estado", "codigo", "salida", "detalle", "reintentable",
                              "efecto")}
                resultado["repetido"] = True
                return comprobar_resultado(resultado, efecto)
            # Recibo ABIERTO: alguien lanzó este efecto y no vivió para contarlo. NO se
            # ejecuta —duplicaría— y NO se declara completado —sería inventarlo—.
            return comprobar_resultado({
                "estado": AMBIGUO,
                "codigo": -1,
                "salida": "",
                "detalle": "hay un recibo ABIERTO para este efecto: se lanzó y no se cerró, "
                           "luego no se puede saber si la tarea llegó a aplicarse. No se "
                           "vuelve a ejecutar, porque hacerlo podría duplicar el efecto",
                "reintentable": False,
                "efecto": efecto,
                "repetido": True,
            }, efecto)

        _punto("antes-de-abrir-el-recibo")
        self._abrir_recibo(efecto)
        _punto("despues-de-abrir-el-recibo-antes-de-ejecutar")

        resultado = self._lanzar(list(argumentos), efecto, float(limite_segundos),
                                 progreso, cancelacion)

        _punto("despues-de-ejecutar-antes-de-cerrar-el-recibo")

        if resultado["estado"] in ("completado", "fallido"):
            self._cerrar_recibo(efecto, resultado)
        else:
            # `timeout` y `cancelado`: ESTE proceso presenció la terminación, así que puede
            # declarar que el efecto no quedó aplicado y retirar el recibo. Un adaptador que
            # muere no llega aquí, y por eso su recibo se queda abierto.
            self._retirar_recibo(efecto)
        return comprobar_resultado(resultado, efecto)

    def _lanzar(self, argumentos, efecto, limite_segundos, progreso, cancelacion):
        if self._politica_de_contencion is not None:
            return self._lanzar_contenido(argumentos, efecto, limite_segundos,
                                          progreso, cancelacion)
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

    def _lanzar_contenido(self, argumentos, efecto, limite_segundos, progreso, cancelacion):
        """`FD-5`: la tarea corre DENTRO de un contenedor de recursos del anfitrión.

        El adaptador no elige el mecanismo y no sabe cuál es: lo elige `contencion.politica`
        a partir de las capacidades REALES del anfitrión, y si la política exige
        `arbol-de-procesos` y ninguna está disponible, `instanciar` levanta
        `ContencionFuerteNoDisponible` y aquí NO se ejecuta nada. Ésa es la diferencia entre
        fallar cerrado y degradar en silencio, y es toda la razón de que este camino exista.

        El resultado se traduce a la forma del §3.4 —la que `comprobar_resultado` valida—
        añadiendo `nivel_de_aislamiento` y `backend`, que es lo que permite que la ficha
        declare un nivel MEDIDO en vez de uno prometido.
        """
        from contencion import ejecutar as ejecutar_contenido

        resultado = ejecutar_contenido(
            argumentos, espacio=self.espacio, limite_segundos=limite_segundos,
            politica=self._politica_de_contencion, marca=efecto,
            progreso=progreso, cancelacion=cancelacion,
            # Las capacidades se sondearon al CONSTRUIR y no se vuelven a sondear: el
            # anfitrión que se midió al arrancar es el que se declara en la ficha, y
            # remedirlo por tarea abriría la puerta a que la ficha dijera una cosa y la
            # ejecución hiciera otra.
            capacidades=self._capacidades_de_contencion,
        )
        salida = resultado.a_dict()
        # `senal` y `ficha_del_backend` son diagnóstico del contenedor, no resultado de la
        # orden: el §3.4 cierra la forma del resultado y añadirle campos sueltos la abriría.
        salida.pop("senal", None)
        salida.pop("ficha_del_backend", None)
        salida.update({
            "efecto": efecto,
            "repetido": False,
            "reintentable": resultado.estado == "timeout",
        })
        return salida

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
