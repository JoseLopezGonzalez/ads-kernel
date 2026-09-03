#!/usr/bin/env python3
"""ejecutor — lanza una tarea DENTRO de la contención elegida, con timeout y cancelación.

Es el bucle de `adaptadores/proceso.py` —progreso por línea, sondeo de cancelación, límite de
tiempo— con UNA diferencia, que es toda la diferencia de `FD-5`: quien mata no es `killpg`,
sino el BACKEND, y el backend sabe cuál es el alcance de lo que mata y lo declara.

DECISIÓN · la tarea lleva una MARCA única en sus argumentos, y no es decorativa
    Dentro de un espacio de nombres de PID los procesos se ven a sí mismos como 1, 2, 3 y no
    pueden publicar su PID del anfitrión. Sin una marca no hay forma de comprobar DESDE FUERA
    que la descendencia murió, y «murió» acabaría siendo una creencia. Con la marca, el
    anfitrión localiza a cada generación por su línea de órdenes y después comprueba una a
    una con `os.kill(pid, 0)`.

DECISIÓN · la marca la pone QUIEN LLAMA, y el ejecutor sólo la conserva
    Alternativas: (a) generarla aquí; (b) recibirla.
    Se elige (b). Una marca generada aquí obligaría a devolverla y a que el llamante confiara
    en que es la que se usó; recibiéndola, el llamante puede haberla puesto en la propia
    tarea —que es lo que hace la prueba de hijo, nieto y bisnieto— y no hay dos verdades.

DECISIÓN · `I-g3`: el resultado PUBLICABLE no lleva pid, ni duración, ni número de ejecución
    El resultado de trabajo sí lleva el pid, porque el llamante lo necesita para comprobar la
    muerte del proceso; `a_dict()` es la forma publicable y no lo incluye. Es el mismo reparto
    que `adaptadores/proceso.py` hace entre su resultado y su recibo.
"""
from __future__ import annotations

import os
import selectors
import subprocess
import time

from . import deteccion, politica as modulo_de_politica
from .backends import GRACIA_SEGUNDOS, INTERVALO_DE_SONDEO, sigue_vivo
from .errores import TareaInvalida

ESTADOS = ("completado", "fallido", "cancelado", "timeout")


class Resultado:
    """El desenlace de una ejecución contenida. `a_dict()` es la forma PUBLICABLE."""

    def __init__(self, **campos):
        self.estado = campos["estado"]
        self.codigo = campos["codigo"]
        self.salida = campos["salida"]
        self.detalle = campos["detalle"]
        self.backend = campos["backend"]
        self.nivel_de_aislamiento = campos["nivel_de_aislamiento"]
        self.senal = campos.get("senal")
        self.pid = campos.get("pid")
        self.ficha_del_backend = campos.get("ficha_del_backend") or {}

    @property
    def ok(self):
        return self.estado == "completado"

    def a_dict(self):
        """Sin pid, sin duración y sin número de ejecución. `I-g3`."""
        return {
            "estado": self.estado,
            "codigo": self.codigo,
            "salida": self.salida,
            "detalle": self.detalle,
            "backend": self.backend,
            "nivel_de_aislamiento": self.nivel_de_aislamiento,
            "senal": self.senal,
            "ficha_del_backend": self.ficha_del_backend,
        }

    def __repr__(self):
        return ("Resultado(" + self.estado + ", " + self.backend + ", "
                + self.nivel_de_aislamiento + ")")


def ejecutar(argumentos, *, espacio, limite_segundos, politica=None, marca=None,
             progreso=None, cancelacion=None, capacidades=None):
    """Ejecuta `argumentos` DENTRO de la contención que la política exija.

    `espacio` es el directorio de trabajo. `marca` es la cadena única que la tarea lleva en
    sus argumentos y que permite localizar su descendencia desde el anfitrión.
    """
    if not isinstance(argumentos, (list, tuple)) or not argumentos:
        raise TareaInvalida("no hay nada que ejecutar: la orden viene vacía")
    politica = politica or modulo_de_politica.Politica()
    backend = modulo_de_politica.instanciar(politica, espacio=espacio,
                                            capacidades=capacidades)
    backend.antes_de_lanzar()
    orden = backend.envolver(list(argumentos))
    entorno = backend.entorno()

    proceso = subprocess.Popen(
        orden,
        cwd=espacio,
        env=entorno,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        # Líder de su propio grupo: sin esto, el respaldo por señal del backend alcanzaría
        # también al proceso que llama.
        start_new_session=True,
    )
    pid = proceso.pid
    try:
        pgid = os.getpgid(pid)
    except ProcessLookupError:
        pgid = pid
    backend.tras_lanzar(proceso)

    limite = time.monotonic() + float(limite_segundos)
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
                        progreso({"linea": numero, "texto": texto, "marca": marca})
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
            progreso({"linea": numero, "texto": texto, "marca": marca})

    if motivo in ("timeout", "cancelado"):
        # La tubería se cierra TAMBIÉN aquí. Antes sólo se cerraba en la ruta normal, y
        # como las pruebas de contención ejercen precisamente el timeout y la cancelación,
        # cada corrida dejaba un `ResourceWarning: unclosed file` que Python cita con la
        # RUTA ABSOLUTA del fichero — y esa ruta acababa PUBLICADA en la evidencia, que se
        # versiona. Una auditoría independiente lo encontró por ahí: la evidencia no era
        # reproducible en otro checkout. El descriptor abierto era el defecto; la ruta en
        # la evidencia, sólo su síntoma.
        _cerrar_salida(proceso)
        senal = backend.terminar(proceso, pid, pgid)
        backend.limpiar()
        detalle = (("el límite venció y la CONTENCIÓN `" + backend.identificador
                    + "` terminó ") if motivo == "timeout"
                   else ("la cancelación terminó, por la CONTENCIÓN `"
                         + backend.identificador + "`, ")) + backend.detalle.get(
            "alcance", "lo que contenía")
        return Resultado(
            estado="timeout" if motivo == "timeout" else "cancelado",
            codigo=-1, salida="\n".join(lineas), detalle=detalle,
            backend=backend.identificador, nivel_de_aislamiento=backend.nivel,
            senal=senal, pid=pid, ficha_del_backend=backend.a_dict(),
        )

    _cerrar_salida(proceso)
    codigo = proceso.wait()
    backend.limpiar()
    if codigo < 0:
        return Resultado(
            estado="fallido", codigo=codigo, salida="\n".join(lineas),
            detalle="el proceso murió por la señal " + str(-codigo)
                    + " sin producir código de salida",
            backend=backend.identificador, nivel_de_aislamiento=backend.nivel,
            senal=None, pid=pid, ficha_del_backend=backend.a_dict(),
        )
    return Resultado(
        estado="completado" if codigo == 0 else "fallido",
        codigo=codigo, salida="\n".join(lineas),
        detalle="" if codigo == 0 else "la tarea terminó con código " + str(codigo),
        backend=backend.identificador, nivel_de_aislamiento=backend.nivel,
        senal=None, pid=pid, ficha_del_backend=backend.a_dict(),
    )


def _cerrar_salida(proceso):
    manejador = getattr(proceso, "stdout", None)
    if manejador is None or manejador.closed:
        return False
    try:
        manejador.close()
    except OSError:
        # El descriptor ya no vale: el proceso murió y el núcleo lo retiró. El objetivo
        # —que no quede una tubería abierta— está cumplido igual.
        return False
    return True


def esperar_a_que_mueran(pids, *, gracia=GRACIA_SEGUNDOS * 4):
    """Espera a que una lista de PID del anfitrión desaparezca. Devuelve los que quedan.

    No es cortesía: entre `SIGKILL` y la desaparición de la entrada de `/proc` hay un
    instante, y comprobar de inmediato produciría falsos supervivientes.
    """
    limite = time.monotonic() + gracia
    vivos = [pid for pid in pids if sigue_vivo(pid)]
    while vivos and time.monotonic() < limite:
        time.sleep(INTERVALO_DE_SONDEO)
        vivos = [pid for pid in vivos if sigue_vivo(pid)]
    return sorted(vivos)


def nivel_de(identificador):
    return deteccion.NIVEL_POR_BACKEND.get(identificador)
