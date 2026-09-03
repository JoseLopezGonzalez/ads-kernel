#!/usr/bin/env python3
"""backends — los CONTENEDORES DE RECURSOS del anfitrión, uno por mecanismo. `FD-5`.

`adaptadores/proceso.py` declara su techo con todas las letras: «un descendiente que hace
`setsid` ESCAPA, y esto está MEDIDO». Este paquete NO oculta esa limitación: la conserva como
un NIVEL de aislamiento explícitamente inferior —`grupo-de-procesos`— y añade backends que
alcanzan el nivel superior —`arbol-de-procesos`—, en los que matar la contención se lleva por
delante a toda la descendencia, haya hecho `setsid` o no.

    grupo-de-procesos   `killpg`. Muere todo el que siga en el GRUPO. Quien se sale del
                        grupo, sobrevive. Es lo que hay hoy, y se declara
    arbol-de-procesos   el contenedor de recursos se lleva TODO lo que hay dentro. `setsid`
                        no saca a nadie de un espacio de nombres de PID, de un cgroup ni de
                        un contenedor

DECISIÓN · el ORDEN DE PREFERENCIA es un dato publicado, no un `if/elif`
    `deteccion.ORDEN_DE_PREFERENCIA` lo declara y `politica.py` lo recorre. Un orden escrito
    dentro de una cadena de condicionales no se puede publicar en la evidencia, y entonces
    «se eligió el mejor disponible» es una afirmación que nadie puede contrastar.

DECISIÓN · `cgroup v2` va PRIMERO cuando está disponible, y lleva su propia guarda
    Es el mecanismo más preciso: `cgroup.kill` es una operación atómica del núcleo sobre el
    subárbol entero, no una señal que haya que dirigir. Su riesgo es simétrico: escribir en
    el `cgroup.kill` equivocado mata a quien lo escribe. Por eso, ANTES de matar, el backend
    comprueba que su propio PID no está en el grupo. Una guarda que se comprueba es barata;
    una que se recuerda, no existe.

DECISIÓN · el espacio de nombres de PID mata al PID 1 y deja que el núcleo remate
    Alternativas: (a) recorrer los procesos del espacio y señalarlos uno a uno; (b) matar al
    PID 1 del espacio.
    Se elige (b). Cuando el PID 1 de un espacio de nombres muere, el núcleo envía `SIGKILL` a
    todos los demás procesos del espacio: es la semántica del propio mecanismo, no una
    convención de este código, y no tiene carrera. Con (a) siempre hay una ventana en la que
    un proceso nuevo aparece después de haberlo enumerado.

DECISIÓN · el ámbito de `systemd` se para por su UNIDAD, no por su PID
    `systemctl --user stop <unidad>.scope` actúa sobre el cgroup del ámbito, que es el
    contenedor real. Mandar una señal al `systemd-run` deja vivo el ámbito.

DECISIÓN · el backend de contenedor NO descarga imágenes y corre SIN RED
    Una prueba cuya contención dependiera de la red no mediría la contención. La imagen la
    elige la detección entre las que YA están en local, y el contenedor se lanza con
    `--network none`.

DECISIÓN · NINGÚN backend hereda el entorno del proceso que lo lanza
    Mismo criterio que `gobierno/git.py`: el entorno se construye entero. Se pasan sólo las
    variables que un mecanismo concreto NECESITA —`XDG_RUNTIME_DIR` y el bus de sesión para
    `systemd`—, y se pasan sin leerlas.
"""
from __future__ import annotations

import os
import shutil
import signal
import subprocess
import time

from . import deteccion
from .errores import BackendNoDisponible, GrupoNoCancelado

GRACIA_SEGUNDOS = 1.5
INTERVALO_DE_SONDEO = 0.05


def entorno_base(espacio):
    """El entorno del proceso contenido. Construido entero, no heredado."""
    return {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
        "HOME": espacio,
    }


def sigue_vivo(pid):
    """`os.kill(pid, 0)` no manda ninguna señal: pregunta si el proceso existe."""
    try:
        os.kill(int(pid), 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        # Existe y es de otro usuario. Para «sigue vivo» eso es un SÍ.
        return True
    except (ValueError, OverflowError):
        return False
    return True


def pids_con_marca(marca):
    """Los PID del anfitrión cuya línea de órdenes contiene la MARCA dada.

    Es la forma de localizar, DESDE FUERA, a los descendientes que viven dentro de un espacio
    de nombres de PID: allí dentro se ven como 1, 2, 3 y no pueden publicar su PID del
    anfitrión. La marca es una cadena única que la tarea lleva en sus argumentos.
    """
    encontrados = []
    for nombre in os.listdir("/proc"):
        if not nombre.isdigit():
            continue
        try:
            with open("/proc/" + nombre + "/cmdline", "rb") as manejador:
                crudo = manejador.read()
        except OSError:
            # El proceso desapareció entre el listado y la lectura, o no es legible. En los
            # dos casos no aporta: lo que este barrido busca son los que SÍ están.
            continue
        if marca.encode("utf-8") in crudo:
            encontrados.append(int(nombre))
    return sorted(encontrados)


class Backend:
    """Interfaz común. Cada backend envuelve la orden y sabe cómo matar lo que envolvió."""

    identificador = ""
    nivel = ""

    def __init__(self, *, espacio, evidencia=None):
        self.espacio = espacio
        self.evidencia = dict(evidencia or {})
        self.detalle = {}

    # -- construcción de la orden ------------------------------------------
    def envolver(self, argumentos):
        return list(argumentos)

    def entorno(self):
        return entorno_base(self.espacio)

    def antes_de_lanzar(self):
        return None

    def tras_lanzar(self, proceso):
        return None

    # -- terminación --------------------------------------------------------
    def terminar(self, proceso, pid, pgid):
        raise NotImplementedError

    def limpiar(self):
        return None

    def a_dict(self):
        return {
            "backend": self.identificador,
            "nivel_de_aislamiento": self.nivel,
            "evidencia": {clave: self.evidencia[clave]
                          for clave in sorted(self.evidencia)},
            "detalle": {clave: self.detalle[clave] for clave in sorted(self.detalle)},
        }


def _senalar_grupo(pgid, senal):
    try:
        os.killpg(pgid, senal)
    except (ProcessLookupError, PermissionError):
        # El grupo ya no existe, o no es nuestro. En los dos casos no hay nada que mandar.
        return False
    return True


def _matar_grupo(proceso, pgid):
    """`SIGTERM` al grupo, espera de gracia, y `SIGKILL` si sigue. Devuelve cuál hizo falta."""
    usada = "SIGTERM"
    _senalar_grupo(pgid, signal.SIGTERM)
    limite = time.monotonic() + GRACIA_SEGUNDOS
    while time.monotonic() < limite:
        if proceso.poll() is not None:
            break
        time.sleep(INTERVALO_DE_SONDEO)
    if proceso.poll() is None:
        usada = "SIGKILL"
        _senalar_grupo(pgid, signal.SIGKILL)
    return usada


# ===========================================================================
#  SIMPLE · nivel `grupo-de-procesos`, explícitamente INFERIOR
# ===========================================================================
class Simple(Backend):
    """`killpg` sobre un grupo propio. Es lo que hoy hace `adaptadores/proceso.py`.

    SE CONSERVA, y su nivel se DECLARA. Lo que no se hace es presentarlo como contención:
    `FD-5` prohíbe degradar en silencio, y aquí el nivel viaja en el resultado, en la ficha
    del backend y en el error que se levanta cuando la política pide más.
    """

    identificador = "simple"
    nivel = deteccion.GRUPO_DE_PROCESOS

    def terminar(self, proceso, pid, pgid):
        usada = _matar_grupo(proceso, pgid)
        self.detalle["senal"] = usada
        self.detalle["alcance"] = ("el GRUPO de procesos. Un descendiente que ejecutó "
                                   "`setsid` NO está en el grupo y sobrevive")
        return usada


# ===========================================================================
#  ESPACIO DE NOMBRES DE PID · nivel `arbol-de-procesos`
# ===========================================================================
class EspacioDePid(Backend):
    """`unshare -Urpf --kill-child`. Matar al PID 1 del espacio se lleva todo el espacio."""

    identificador = "espacio-de-nombres-de-pid"
    nivel = deteccion.ARBOL_DE_PROCESOS

    def envolver(self, argumentos):
        return ["unshare", "--user", "--map-root-user", "--pid", "--fork",
                "--kill-child", "--mount-proc"] + list(argumentos)

    def terminar(self, proceso, pid, pgid):
        # Al morir `unshare`, `--kill-child` lleva `SIGKILL` al PID 1 del espacio, y el
        # núcleo remata a todos los demás procesos del espacio. No hay que enumerarlos.
        try:
            os.kill(pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        # Cinturón: si `unshare` ya había muerto y quedó algo en el grupo, se señala también.
        _senalar_grupo(pgid, signal.SIGKILL)
        limite = time.monotonic() + GRACIA_SEGUNDOS
        while proceso.poll() is None and time.monotonic() < limite:
            time.sleep(INTERVALO_DE_SONDEO)
        self.detalle["senal"] = "SIGKILL"
        self.detalle["alcance"] = ("el ESPACIO DE NOMBRES de PID entero: al morir su PID 1 "
                                   "el núcleo mata a todos los demás, `setsid` incluido")
        return "SIGKILL"


# ===========================================================================
#  ÁMBITO DE SYSTEMD · nivel `arbol-de-procesos`
# ===========================================================================
class AmbitoDeSystemd(Backend):
    """`systemd-run --user --scope`. Parar la unidad actúa sobre su cgroup entero."""

    identificador = "systemd-scope"
    nivel = deteccion.ARBOL_DE_PROCESOS

    def __init__(self, *, espacio, evidencia=None, unidad=None):
        super().__init__(espacio=espacio, evidencia=evidencia)
        # El nombre de la unidad es OPERACIONAL y no entra en nada durable: `I-g3` prohíbe
        # el pid en lo derivado, y por eso no viaja al resultado publicado.
        self.unidad = unidad or ("ads-contencion-" + os.urandom(6).hex())

    def envolver(self, argumentos):
        return ["systemd-run", "--user", "--scope", "--quiet",
                "--unit=" + self.unidad, "--"] + list(argumentos)

    def entorno(self):
        entorno = entorno_base(self.espacio)
        for nombre in ("XDG_RUNTIME_DIR", "DBUS_SESSION_BUS_ADDRESS"):
            if nombre in os.environ:
                entorno[nombre] = os.environ[nombre]
        return entorno

    def terminar(self, proceso, pid, pgid):
        subprocess.run(
            ["systemctl", "--user", "stop", self.unidad + ".scope"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            env=self.entorno(), check=False, timeout=GRACIA_SEGUNDOS * 8,
        )
        limite = time.monotonic() + GRACIA_SEGUNDOS
        while proceso.poll() is None and time.monotonic() < limite:
            time.sleep(INTERVALO_DE_SONDEO)
        if proceso.poll() is None:
            _senalar_grupo(pgid, signal.SIGKILL)
        self.detalle["senal"] = "systemctl stop"
        self.detalle["alcance"] = ("el CGROUP del ámbito: `systemd` mata a todos sus "
                                   "procesos, y `setsid` no saca a nadie de un cgroup")
        return "systemctl-stop"


# ===========================================================================
#  CGROUP V2 · nivel `arbol-de-procesos`
# ===========================================================================
class CgroupV2(Backend):
    """Un subgrupo delegado, con `cgroup.kill`. La tarea se mete ella misma antes de `exec`."""

    identificador = "cgroup-v2"
    nivel = deteccion.ARBOL_DE_PROCESOS

    def __init__(self, *, espacio, evidencia=None, nombre=None):
        super().__init__(espacio=espacio, evidencia=evidencia)
        raiz = deteccion.raiz_delegada()
        if raiz is None:
            raise BackendNoDisponible(
                "no hay ningún subárbol de `cgroup2` delegado y escribible para este usuario"
            )
        self.nombre = nombre or ("ads-contencion-" + os.urandom(6).hex() + ".scope")
        self.grupo = os.path.join(raiz, self.nombre)

    def antes_de_lanzar(self):
        os.makedirs(self.grupo, exist_ok=True)
        return None

    def envolver(self, argumentos):
        # La tarea se MUEVE ELLA MISMA al subgrupo y después hace `exec`. Es la única forma
        # sin carrera: mover desde fuera deja una ventana entre `fork` y la escritura en la
        # que el hijo ya puede haber lanzado descendencia fuera del grupo.
        return ["sh", "-c", deteccion.GUION_DE_MIGRACION, "ads-contencion",
                self.grupo] + list(argumentos)

    def _procesos(self):
        try:
            with open(os.path.join(self.grupo, "cgroup.procs"), encoding="ascii") as m:
                return [int(linea) for linea in m.read().split() if linea.isdigit()]
        except OSError:
            return []

    def terminar(self, proceso, pid, pgid):
        # GUARDA · nunca se mata un grupo que contenga a quien lo mata.
        dentro = self._procesos()
        if os.getpid() in dentro:
            raise GrupoNoCancelado(
                "el proceso que cancela está DENTRO del subgrupo que iba a matar: se aborta "
                "en vez de suicidarse",
            )
        matadero = os.path.join(self.grupo, "cgroup.kill")
        usada = "cgroup.kill"
        try:
            with open(matadero, "w", encoding="ascii") as manejador:
                manejador.write("1")
        except OSError as exc:
            # Si el núcleo no acepta `cgroup.kill` se dice, y se remata por señal al grupo.
            self.detalle["cgroup_kill_fallo"] = str(exc.strerror)
            usada = _matar_grupo(proceso, pgid)
        limite = time.monotonic() + GRACIA_SEGUNDOS
        while proceso.poll() is None and time.monotonic() < limite:
            time.sleep(INTERVALO_DE_SONDEO)
        self.detalle["senal"] = usada
        self.detalle["alcance"] = ("el SUBGRUPO entero, por operación del núcleo. `setsid` "
                                   "no saca a un proceso de su cgroup")
        return usada

    def limpiar(self):
        try:
            os.rmdir(self.grupo)
        except OSError:
            # El subgrupo tarda un instante en vaciarse tras `cgroup.kill`; que quede es un
            # residuo del anfitrión y no cambia el veredicto de la contención.
            return None
        return None


# ===========================================================================
#  CONTENEDOR · nivel `arbol-de-procesos`
# ===========================================================================
class Contenedor(Backend):
    """Un contenedor sin red, con identidad distinta. `docker kill` se lleva todo lo de dentro."""

    identificador = "contenedor"
    nivel = deteccion.ARBOL_DE_PROCESOS

    def __init__(self, *, espacio, evidencia=None, imagen=None, usuario=None,
                 nombre=None):
        super().__init__(espacio=espacio, evidencia=evidencia)
        self.imagen = imagen or self.evidencia.get("imagen") or "alpine:3.20"
        self.usuario = usuario or "65534:65534"
        self.nombre = nombre or ("ads-contencion-" + os.urandom(6).hex())

    def envolver(self, argumentos):
        return ["docker", "run", "--rm", "--network", "none",
                "--name", self.nombre, "--user", self.usuario,
                self.imagen] + list(argumentos)

    def terminar(self, proceso, pid, pgid):
        subprocess.run(["docker", "kill", self.nombre],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       env=self.entorno(), check=False, timeout=GRACIA_SEGUNDOS * 20)
        limite = time.monotonic() + GRACIA_SEGUNDOS * 4
        while proceso.poll() is None and time.monotonic() < limite:
            time.sleep(INTERVALO_DE_SONDEO)
        if proceso.poll() is None:
            _senalar_grupo(pgid, signal.SIGKILL)
        self.detalle["senal"] = "docker kill"
        self.detalle["alcance"] = ("el CONTENEDOR entero: su espacio de nombres de PID se "
                                   "destruye con él")
        return "docker-kill"

    def limpiar(self):
        if shutil.which("docker") is None:
            return None
        subprocess.run(["docker", "rm", "-f", self.nombre],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       env=self.entorno(), check=False, timeout=GRACIA_SEGUNDOS * 20)
        return None


CLASES = {
    "simple": Simple,
    "espacio-de-nombres-de-pid": EspacioDePid,
    "systemd-scope": AmbitoDeSystemd,
    "cgroup-v2": CgroupV2,
    "contenedor": Contenedor,
}


def crear(identificador, *, espacio, evidencia=None):
    """Instancia el backend pedido. `BackendNoDisponible` si no existe esa clase."""
    clase = CLASES.get(identificador)
    if clase is None:
        raise BackendNoDisponible(
            "no hay backend de contención con el identificador `" + str(identificador)
            + "`. Declarados: " + ", ".join(sorted(CLASES))
        )
    return clase(espacio=espacio, evidencia=evidencia)
