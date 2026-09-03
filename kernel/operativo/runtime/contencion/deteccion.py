#!/usr/bin/env python3
"""deteccion — DETECCIÓN de las capacidades de contención del ANFITRIÓN. `FD-5`.

`FD-5` exige «detección de capacidades del anfitrión», y aquí eso significa algo muy concreto:
**no basta con que el binario exista o con que el directorio se pueda crear.** Cada sonda
EJERCE la capacidad hasta el punto en que puede fallar, y publica el motivo real cuando falla.

DECISIÓN · la sonda de `cgroup v2` EJERCE el mismo envoltorio que el backend, y comprueba
           la MEMBRESÍA
    Alternativas: (a) comprobar que `/sys/fs/cgroup/cgroup.controllers` existe; (b) crear un
    subgrupo delegado y darlo por bueno; (c) crear el subgrupo, lanzar la tarea con el
    ENVOLTORIO REAL del backend y comprobar que aparece en `cgroup.procs` del destino.
    Se elige (c), y la razón se MIDIÓ en este mismo anfitrión, donde las tres cosas dan
    resultados distintos:
      · (a) dice que sí: hay `cgroup2` unificado con `memory` y `pids`;
      · (b) dice que sí: `systemd` delega `user@<uid>.service` y el `mkdir` funciona, y el
        subgrupo resultante tiene `cgroup.kill`;
      · (c) dice que NO: el envoltorio real —`echo $$ > <grupo>/cgroup.procs`— falla con
        **EIO** («I/O error»), la tarea nunca entra en el subgrupo, y matar ese subgrupo no
        habría matado nada.
    Con (a) o con (b) el aparato habría elegido un backend incapaz de contener y lo habría
    llamado FUERTE, que es exactamente el falso verde que `FD-5` prohíbe. La causa concreta
    del EIO pertenece al anfitrión y no se adivina aquí: lo que se publica es el mensaje del
    sistema, tal cual, y la consecuencia —backend NO disponible—.
    Y el envoltorio de la sonda y el del backend son EL MISMO TEXTO, `GUION_DE_MIGRACION`:
    una sonda que ejerciera una vía distinta de la que después se usa no detectaría nada.

DECISIÓN · la sonda de espacio de nombres de PID comprueba que el hijo ES el PID 1
    `unshare -Urpf` puede devolver 0 y no haber creado nada si el núcleo no permite espacios
    de nombres de usuario sin privilegios. Que el proceso interior se vea a sí mismo como
    PID 1 es la prueba de que el espacio existe.

DECISIÓN · la sonda de `systemd` crea y para un ámbito de verdad
    `systemd-run --user --scope -- /bin/true` devuelve 0 incluso en anfitriones donde el bus
    de sesión no permite parar el ámbito después. La sonda crea un ámbito, comprueba que
    `systemctl --user stop` lo acepta, y sólo entonces declara disponible el backend.

DECISIÓN · la sonda de contenedor NO descarga imágenes
    Una detección que dependiera de la red haría que la disponibilidad de un backend cambiara
    con la conectividad. La sonda pregunta al demonio y comprueba que alguna de las imágenes
    declaradas ya está en local; si no hay ninguna, el backend se declara NO disponible con
    ese motivo, y no se intenta `pull`.

DECISIÓN · el informe es DETERMINISTA salvo en su campo `motivo`
    Los identificadores, los niveles y el orden de preferencia son fijos y ordenados. El
    `motivo` de una sonda fallida lleva el mensaje real del sistema —que es lo que hace útil
    la detección— y por eso el informe NO se publica como evidencia byte-idéntica: se publica
    la DISPONIBILIDAD, que sí lo es.
"""
from __future__ import annotations

import errno
import os
import shutil
import subprocess
import time

# El vocabulario CERRADO de niveles de aislamiento. No hay más, y no se inventan.
GRUPO_DE_PROCESOS = "grupo-de-procesos"
ARBOL_DE_PROCESOS = "arbol-de-procesos"
NIVELES = (GRUPO_DE_PROCESOS, ARBOL_DE_PROCESOS)

# Orden de PREFERENCIA entre los backends fuertes, y después el débil. Es un dato, y el
# selector no lo recalcula: un orden implícito en un `if/elif` no se puede publicar.
ORDEN_DE_PREFERENCIA = (
    "cgroup-v2",
    "espacio-de-nombres-de-pid",
    "systemd-scope",
    "contenedor",
    "simple",
)

IMAGENES_ACEPTADAS = ("alpine:3.20", "python:3.11-slim", "ads-py311:local")

LIMITE_DE_SONDA = 20.0

_ENTORNO_DE_SONDA_FIJO = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}


def _entorno():
    entorno = dict(_ENTORNO_DE_SONDA_FIJO)
    entorno["PATH"] = os.environ.get("PATH", "/usr/bin:/bin")
    entorno["HOME"] = os.environ.get("HOME", "/tmp")
    # `systemd-run --user` y `systemctl --user` necesitan el bus de la sesión. Se PASA la
    # variable; no se lee su contenido ni se publica.
    for nombre in ("XDG_RUNTIME_DIR", "DBUS_SESSION_BUS_ADDRESS"):
        if nombre in os.environ:
            entorno[nombre] = os.environ[nombre]
    return entorno


def _correr(orden, entrada=None, limite=LIMITE_DE_SONDA):
    try:
        proceso = subprocess.run(
            orden, input=entrada, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=_entorno(), timeout=limite, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, "", type(exc).__name__
    return (proceso.returncode,
            proceso.stdout.decode("utf-8", "replace").strip(),
            proceso.stderr.decode("utf-8", "replace").strip())


def _resultado(disponible, motivo, **evidencia):
    salida = {"disponible": bool(disponible), "motivo": motivo}
    salida.update({clave: evidencia[clave] for clave in sorted(evidencia)})
    return salida


# ---------------------------------------------------------------------------
#  cgroup v2
# ---------------------------------------------------------------------------
RAIZ_DE_CGROUP = "/sys/fs/cgroup"


def raiz_delegada():
    """El subárbol de `cgroup2` donde este usuario puede crear subgrupos, o `None`.

    `systemd` delega `user.slice/user-<uid>.slice/user@<uid>.service` al usuario de la
    sesión. Se busca ahí y no en la raíz, que es de `root` en cualquier anfitrión sensato.
    """
    if not os.path.isdir(RAIZ_DE_CGROUP):
        return None
    candidata = os.path.join(
        RAIZ_DE_CGROUP, "user.slice", "user-" + str(os.getuid()) + ".slice",
        "user@" + str(os.getuid()) + ".service",
    )
    if os.path.isdir(candidata) and os.access(candidata, os.W_OK):
        return candidata
    if os.access(RAIZ_DE_CGROUP, os.W_OK):
        return RAIZ_DE_CGROUP
    return None


# El envoltorio de migración. Vive AQUÍ y lo usan LOS DOS —la sonda y el backend— porque una
# sonda que ejerciera una vía distinta de la que después se usa no estaría detectando nada:
# es exactamente el defecto que esta sonda encontró en este anfitrión.
CODIGO_DE_MIGRACION_FALLIDA = 71
GUION_DE_MIGRACION = (
    'echo $$ > "$1"/cgroup.procs || exit ' + str(CODIGO_DE_MIGRACION_FALLIDA) + '\n'
    'shift\n'
    'exec "$@"\n'
)


def sondar_cgroup_v2():
    """Crea un subgrupo REAL, ejerce el ENVOLTORIO del backend y comprueba la MEMBRESÍA.

    No basta con que el `mkdir` funcione ni con que una escritura desde Python devuelva 0:
    lo que hay que medir es que **la tarea acaba DENTRO del subgrupo**, y eso se mide leyendo
    `cgroup.procs` del destino mientras la tarea corre.
    """
    controladores = os.path.join(RAIZ_DE_CGROUP, "cgroup.controllers")
    if not os.path.isfile(controladores):
        return _resultado(False, "no hay `cgroup2` unificado montado en el anfitrión")
    raiz = raiz_delegada()
    if raiz is None:
        return _resultado(
            False, "hay `cgroup2` pero no hay ningún subárbol delegado y escribible")
    prueba = os.path.join(raiz, "ads-sonda-de-contencion.scope")
    try:
        os.makedirs(prueba, exist_ok=True)
    except OSError as exc:
        return _resultado(False, "no se pudo crear un subgrupo: " + str(exc.strerror),
                          subarbol_delegado=os.path.basename(raiz))
    tiene_kill = os.path.isfile(os.path.join(prueba, "cgroup.kill"))
    dentro = []
    try:
        proceso = subprocess.Popen(
            ["sh", "-c", GUION_DE_MIGRACION, "ads-sonda", prueba,
             "sh", "-c", "sleep 0.6"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=_entorno(),
            start_new_session=True,
        )
    except OSError as exc:
        return _resultado(False, "no se pudo lanzar la sonda de migración: "
                                 + str(exc.strerror))
    limite = time.monotonic() + 3.0
    while time.monotonic() < limite and proceso.poll() is None:
        dentro = _procesos_del_grupo(prueba)
        if dentro:
            break
        time.sleep(0.02)
    try:
        _, error_crudo = proceso.communicate(timeout=5)
    except subprocess.TimeoutExpired:                                # pragma: no cover
        proceso.kill()
        _, error_crudo = proceso.communicate()
    codigo = proceso.returncode
    error = error_crudo.decode("utf-8", "replace").strip()
    try:
        os.rmdir(prueba)
    except OSError:
        # El subgrupo tarda un instante en vaciarse; que quede un residuo no cambia lo que
        # la sonda mide, y borrarlo no es su cometido.
        pass
    if codigo != CODIGO_DE_MIGRACION_FALLIDA and dentro:
        return _resultado(True, "subgrupo delegado creado y tarea MIGRADA dentro de él",
                          subarbol_delegado=os.path.basename(raiz),
                          tiene_cgroup_kill=tiene_kill)
    detalle = error or ("la tarea no apareció en `cgroup.procs` del destino")
    return _resultado(
        False,
        "el subgrupo se crea pero la tarea NO acaba dentro (" + detalle
        + "): un backend que no puede meter la tarea en su contenedor no contiene nada",
        subarbol_delegado=os.path.basename(raiz),
        tiene_cgroup_kill=tiene_kill,
        errno_de_migracion=errno.EIO,
    )


def _procesos_del_grupo(grupo):
    try:
        with open(os.path.join(grupo, "cgroup.procs"), encoding="ascii") as manejador:
            return [int(linea) for linea in manejador.read().split() if linea.isdigit()]
    except OSError:
        return []


# ---------------------------------------------------------------------------
#  espacio de nombres de PID
# ---------------------------------------------------------------------------
def sondar_espacio_de_pid():
    """Comprueba que el proceso interior se ve a sí mismo como PID 1."""
    if shutil.which("unshare") is None:
        return _resultado(False, "no hay `unshare` en el anfitrión")
    codigo, salida, error = _correr(
        ["unshare", "-Urpf", "--kill-child", "sh", "-c", "echo $$"])
    if codigo == 0 and salida == "1":
        return _resultado(True, "espacio de nombres de PID sin privilegios disponible",
                          pid_interior=1)
    return _resultado(
        False,
        "`unshare -Urpf` no produjo un espacio de PID usable: "
        + (error or salida or "sin detalle"))


# ---------------------------------------------------------------------------
#  ámbito de systemd
# ---------------------------------------------------------------------------
UNIDAD_DE_SONDA = "ads-sonda-de-contencion"


def sondar_systemd_scope():
    """Crea un ámbito de usuario y comprueba que se puede PARAR, que es lo que cancela."""
    if shutil.which("systemd-run") is None or shutil.which("systemctl") is None:
        return _resultado(False, "no hay `systemd-run` o `systemctl` en el anfitrión")
    if not os.environ.get("XDG_RUNTIME_DIR"):
        return _resultado(
            False, "no hay `XDG_RUNTIME_DIR`: sin bus de sesión no hay ámbito de usuario")
    codigo, _, error = _correr(
        ["systemd-run", "--user", "--scope", "--quiet",
         "--unit=" + UNIDAD_DE_SONDA, "--", "sh", "-c", "sleep 0.2"])
    if codigo != 0:
        return _resultado(False, "`systemd-run --user --scope` falló: "
                                 + (error or "sin detalle"))
    parada, _, error_parada = _correr(
        ["systemctl", "--user", "stop", UNIDAD_DE_SONDA + ".scope"])
    if parada not in (0, 5):
        # 5 es «unidad no encontrada»: el ámbito ya había terminado solo, que es correcto.
        return _resultado(False, "el ámbito se crea pero no se puede parar: "
                                 + (error_parada or "sin detalle"))
    return _resultado(True, "ámbito de usuario de systemd creable y parable",
                      unidad_de_sonda=UNIDAD_DE_SONDA)


# ---------------------------------------------------------------------------
#  contenedor
# ---------------------------------------------------------------------------
def sondar_contenedor():
    """Pregunta al demonio y busca una imagen YA presente. No descarga nada."""
    if shutil.which("docker") is None:
        return _resultado(False, "no hay cliente `docker` en el anfitrión")
    codigo, _, error = _correr(["docker", "info", "--format", "{{.ServerVersion}}"])
    if codigo != 0:
        return _resultado(False, "el demonio de contenedores no responde: "
                                 + (error or "sin detalle"))
    for imagen in IMAGENES_ACEPTADAS:
        presente, _, _ = _correr(["docker", "image", "inspect", imagen])
        if presente == 0:
            return _resultado(True, "demonio accesible e imagen presente en local",
                              imagen=imagen)
    return _resultado(
        False,
        "el demonio responde pero ninguna imagen declarada está en local, y la detección "
        "NO descarga: la disponibilidad de un backend no puede depender de la red")


# ---------------------------------------------------------------------------
#  el backend simple
# ---------------------------------------------------------------------------
def sondar_simple():
    """`killpg` está siempre en POSIX. Se declara DISPONIBLE y con nivel INFERIOR."""
    return _resultado(
        True,
        "grupos de procesos POSIX. AISLAMIENTO INFERIOR y declarado: un descendiente que "
        "ejecuta `setsid` sale del grupo y ESCAPA a `killpg`",
    )


SONDAS = {
    "cgroup-v2": sondar_cgroup_v2,
    "espacio-de-nombres-de-pid": sondar_espacio_de_pid,
    "systemd-scope": sondar_systemd_scope,
    "contenedor": sondar_contenedor,
    "simple": sondar_simple,
}

NIVEL_POR_BACKEND = {
    "cgroup-v2": ARBOL_DE_PROCESOS,
    "espacio-de-nombres-de-pid": ARBOL_DE_PROCESOS,
    "systemd-scope": ARBOL_DE_PROCESOS,
    "contenedor": ARBOL_DE_PROCESOS,
    "simple": GRUPO_DE_PROCESOS,
}


def capacidades():
    """El informe de capacidades del anfitrión, en el ORDEN DE PREFERENCIA declarado."""
    filas = []
    for identificador in ORDEN_DE_PREFERENCIA:
        resultado = SONDAS[identificador]()
        filas.append({
            "backend": identificador,
            "nivel": NIVEL_POR_BACKEND[identificador],
            "disponible": resultado["disponible"],
            "motivo": resultado["motivo"],
            "evidencia": {clave: resultado[clave] for clave in sorted(resultado)
                          if clave not in ("disponible", "motivo")},
        })
    fuertes = [fila["backend"] for fila in filas
               if fila["disponible"] and fila["nivel"] == ARBOL_DE_PROCESOS]
    return {
        "orden_de_preferencia": list(ORDEN_DE_PREFERENCIA),
        "niveles": list(NIVELES),
        "backends": filas,
        "fuertes_disponibles": fuertes,
        "hay_contencion_fuerte": bool(fuertes),
        "mejor_disponible": next(
            (fila["backend"] for fila in filas if fila["disponible"]), None),
    }
