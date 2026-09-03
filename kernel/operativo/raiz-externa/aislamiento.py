#!/usr/bin/env python3
"""aislamiento — la DEMOSTRACIÓN de que la raíz externa NO PUEDE ESCRIBIR en el árbol.

`g.15` exige «una IDENTIDAD SIN PERMISO DE ESCRITURA sobre ese repositorio, y distinta de la
identidad de escritura del runtime», y §11.8 lo repite: «sus credenciales son separadas, con
alcance mínimo y sin permiso de escritura sobre lo que verifica».

**Poner el verificador en otro directorio no demuestra nada.** Lo que hay que demostrar es que
la identidad que verifica NO PUEDE escribir, y eso se demuestra INTENTÁNDOLO. Este módulo
intenta, una a una, las escrituras que un verificador comprometido querría hacer, y publica el
mensaje real del sistema en cada intento.

ORDEN DE PREFERENCIA, y por qué el primero NO se usa aquí:

    1 · USUARIO DEL SISTEMA    lo mejor, y en este anfitrión NO ES POSIBLE: no hay `sudo` sin
        DISTINTO               contraseña y no se puede crear un usuario. La sonda lo
                               comprueba —no lo supone— y lo deja registrado como tal
    2 · CONTENEDOR CON         SÍ es posible: `docker run --user <uid distinto> --network none
        IDENTIDAD DISTINTA Y   -v <repo>:/repo:ro`. La identidad del proceso verificador es
        MONTAJE DE SÓLO        otra —`65534`, y no la del runtime— y el árbol está montado de
        LECTURA                SÓLO LECTURA
    3 · ESPACIO DE NOMBRES     `unshare -Urm` con `mount --bind` y `mount -o remount,ro,bind`.
        CON MONTAJE `ro`       Da el montaje de sólo lectura, y su LÍMITE se declara: el
                               usuario dentro del espacio se mapea al MISMO usuario del
                               anfitrión, luego demuestra la falta de permiso de ESCRITURA
                               pero NO una identidad distinta. Se conserva como RESPALDO

DECISIÓN · cada intento publica su MENSAJE REAL, y no un «falló» genérico
    Un «no se pudo escribir» puede ser un permiso, un fichero que no existe, un directorio
    ausente o un intérprete roto. Sólo el mensaje del sistema distingue «Read-only file
    system» de «No such file or directory», y sin esa distinción la prueba podría estar
    pasando porque el objetivo no existía.

DECISIÓN · hay un CONTROL POSITIVO dentro del mismo aislamiento
    Si TODOS los intentos fallan, la explicación más probable no es el aislamiento: es que el
    intérprete no arrancó. Por eso se hace una escritura que TIENE que funcionar —en el
    espacio propio del contenedor— y el informe la exige en verde. Sin ella, la demostración
    no distingue el control del mutante.

DECISIÓN · los ficheros de FUERA del árbol también se montan de sólo lectura
    La clave pública aceptada y la atestación ya firmada viven fuera del repositorio, y son
    dos de los ocho objetivos. Montarlos de sólo lectura es lo que hace comprobable que la
    identidad verificadora tampoco puede reescribir su propia evidencia después de emitirla.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile

from errores import AislamientoNoDisponible, EscrituraNoImpedida

USUARIO_DEL_CONTENEDOR = "65534:65534"
IMAGENES_ACEPTADAS = ("alpine:3.20", "python:3.11-slim", "ads-py311:local")
LIMITE = 120.0

MONTAJE_DEL_ARBOL = "/repo"
MONTAJE_EXTERNO = "/externo"

# Los OCHO intentos que el encargo de `V6-16` enumera, más el control positivo. Cada uno es
# una orden de intérprete, y el guion los ejecuta uno a uno capturando su mensaje.
INTENTOS = (
    {"id": "modificar-un-fichero",
     "guion": 'printf x >> "$REPO"/README.md'},
    {"id": "crear-un-fichero",
     "guion": 'printf x > "$REPO"/ADS-INTRUSO.md'},
    {"id": "borrar-un-fichero",
     # SIN `-f`: con `-f`, un fichero que no existiera daría código 0 y se leería como
     # «escritura permitida». El control de LECTURA garantiza que el fichero SÍ está.
     "guion": 'rm "$REPO"/README.md'},
    {"id": "cambiar-una-ref",
     "guion": ('printf 0000000000000000000000000000000000000000 > '
               '"$REPO"/.git/refs/heads/canonica')},
    {"id": "alterar-la-configuracion-de-git",
     "guion": 'printf "[core]" >> "$REPO"/.git/config'},
    {"id": "sustituir-la-clave-publica-aceptada",
     "guion": 'printf x > "$EXTERNO"/allowed_signers'},
    {"id": "cambiar-la-politica",
     "guion": ('printf x >> '
               '"$REPO"/kernel/operativo/runtime/gobierno/POLITICA-CONTROL-REPO.yml')},
    {"id": "modificar-la-atestacion-ya-firmada",
     "guion": 'printf x >> "$EXTERNO"/atestacion.json'},
)

# Los DOS controles del control. Sin ellos, «todo falló» tendría una explicación mucho más
# probable que el aislamiento: que el intérprete no arrancó, o que el árbol ni siquiera está
# montado y los objetivos no existen.
CONTROL_POSITIVO = {
    "id": "control-positivo-escribir-en-lo-propio",
    "guion": 'printf x > "$PROPIO"/ads-control-positivo',
}

CONTROL_DE_LECTURA = {
    "id": "control-de-lectura-del-arbol-montado",
    "guion": 'cat "$REPO"/README.md > /dev/null && cat "$EXTERNO"/allowed_signers > /dev/null',
}


def _guion(repo, externo, propio):
    """El guion de intérprete que ejecuta los intentos DENTRO del aislamiento.

    Las tres rutas se INCRUSTAN entrecomilladas en vez de pasarse como argumentos
    posicionales: el envoltorio del espacio de nombres necesita sus propios argumentos para
    montar, y dos convenios de argumentos sobre el mismo guion es una fuente de fallo que no
    compensa. Las tres rutas las elige este módulo; no vienen de fuera.
    """
    lineas = [
        'REPO=' + _entrecomillar(repo),
        'EXTERNO=' + _entrecomillar(externo),
        'PROPIO=' + _entrecomillar(propio),
        # EXPORTADAS: `probar` lanza un intérprete NUEVO por intento, y un intérprete nuevo
        # no hereda variables que no se exporten. Sin esto, `"$REPO"` se expandía a vacío y
        # los intentos atacaban `/README.md` en vez del árbol montado.
        'export REPO EXTERNO PROPIO',
        'printf "identidad\\t%s\\t%s\\n" "$(id -u)" "$(id -g)"',
        'probar() {',
        '  salida=$(sh -c "$2" 2>&1); rc=$?',
        '  printf "%s\\t%s\\t%s\\n" "$1" "$rc" "$(printf %s "$salida" | tr "\\n" " ")"',
        '}',
    ]
    for intento in INTENTOS + (CONTROL_POSITIVO, CONTROL_DE_LECTURA):
        lineas.append("probar " + intento["id"] + " " + _entrecomillar(intento["guion"]))
    return "\n".join(lineas) + "\n"


def _entrecomillar(texto):
    return "'" + texto.replace("'", "'\"'\"'") + "'"


def _correr(orden, limite=LIMITE):
    try:
        proceso = subprocess.run(
            orden, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                 "LC_ALL": "C", "LANG": "C", "HOME": "/tmp"},
            timeout=limite, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, "", type(exc).__name__
    return (proceso.returncode,
            proceso.stdout.decode("utf-8", "replace"),
            proceso.stderr.decode("utf-8", "replace"))


# ---------------------------------------------------------------------------
#  detección de los tres mecanismos
# ---------------------------------------------------------------------------
def sondar_usuario_del_sistema():
    """La opción 1. Se COMPRUEBA que no es posible en vez de suponerlo."""
    if shutil.which("sudo") is None:
        return {"disponible": False, "identidad_distinta": False,
                "motivo": "no hay `sudo` en el anfitrión"}
    codigo, _, error = _correr(["sudo", "-n", "true"], limite=20.0)
    if codigo == 0:
        return {"disponible": True, "identidad_distinta": True,
                "motivo": "`sudo` sin contraseña disponible"}
    return {
        "disponible": False,
        "identidad_distinta": False,
        "motivo": ("`sudo` exige contraseña (" + error.strip().splitlines()[-1]
                   if error.strip() else "`sudo` exige contraseña")
        + "): no se puede crear ni asumir un usuario del sistema distinto",
    }


def sondar_contenedor():
    """La opción 2. Demonio accesible e imagen YA en local; no se descarga nada."""
    if shutil.which("docker") is None:
        return {"disponible": False, "identidad_distinta": False,
                "motivo": "no hay cliente `docker` en el anfitrión"}
    codigo, _, error = _correr(["docker", "info", "--format", "{{.ServerVersion}}"])
    if codigo != 0:
        return {"disponible": False, "identidad_distinta": False,
                "motivo": "el demonio de contenedores no responde: " + error.strip()[:160]}
    for imagen in IMAGENES_ACEPTADAS:
        presente, _, _ = _correr(["docker", "image", "inspect", imagen])
        if presente == 0:
            return {"disponible": True, "identidad_distinta": True, "imagen": imagen,
                    "usuario": USUARIO_DEL_CONTENEDOR,
                    "motivo": "contenedor con identidad distinta y montaje de sólo lectura"}
    return {"disponible": False, "identidad_distinta": False,
            "motivo": "ninguna imagen declarada está en local y no se descarga"}


def sondar_espacio_de_nombres():
    """La opción 3, de RESPALDO. Da el montaje `ro`; NO da una identidad distinta."""
    if shutil.which("unshare") is None:
        return {"disponible": False, "identidad_distinta": False,
                "motivo": "no hay `unshare` en el anfitrión"}
    codigo, salida, error = _correr(
        ["unshare", "--user", "--map-root-user", "--mount", "sh", "-c", "id -u"],
        limite=30.0)
    if codigo == 0 and salida.strip() == "0":
        return {
            "disponible": True,
            "identidad_distinta": False,
            "motivo": ("espacio de nombres de usuario y de montaje disponible. LÍMITE "
                       "DECLARADO: el `root` de dentro se mapea al MISMO usuario del "
                       "anfitrión, luego demuestra la falta de permiso de ESCRITURA y NO "
                       "una identidad distinta"),
        }
    return {"disponible": False, "identidad_distinta": False,
            "motivo": "`unshare -Urm` no produjo un espacio usable: "
                      + (error.strip()[:160] or salida.strip()[:160])}


MECANISMOS = (
    ("usuario-del-sistema", sondar_usuario_del_sistema),
    ("contenedor", sondar_contenedor),
    ("espacio-de-nombres", sondar_espacio_de_nombres),
)


def capacidades():
    """Las tres opciones, en su orden de preferencia, cada una con su motivo real."""
    filas = []
    for identificador, sonda in MECANISMOS:
        informe = sonda()
        informe["mecanismo"] = identificador
        filas.append(informe)
    elegido = next((fila["mecanismo"] for fila in filas if fila["disponible"]), None)
    return {
        "orden_de_preferencia": [identificador for identificador, _ in MECANISMOS],
        "mecanismos": filas,
        "elegido": elegido,
        "hay_identidad_distinta": any(fila["disponible"] and fila["identidad_distinta"]
                                      for fila in filas),
    }


# ---------------------------------------------------------------------------
#  la ejecución de los intentos
# ---------------------------------------------------------------------------
def _interpretar(salida):
    identidad = {}
    intentos = {}
    for linea in salida.splitlines():
        campos = linea.split("\t")
        if len(campos) < 3:
            continue
        if campos[0] == "identidad":
            identidad = {"uid": campos[1], "gid": campos[2]}
            continue
        intentos[campos[0]] = {"codigo": int(campos[1]) if campos[1].isdigit() else -1,
                               "mensaje": campos[2].strip()}
    return identidad, intentos


def _en_contenedor(repo, externo, imagen):
    orden = [
        "docker", "run", "--rm", "--network", "none",
        "--user", USUARIO_DEL_CONTENEDOR,
        "-v", os.path.abspath(repo) + ":" + MONTAJE_DEL_ARBOL + ":ro",
        "-v", os.path.abspath(externo) + ":" + MONTAJE_EXTERNO + ":ro",
        imagen, "sh", "-c",
        _guion(MONTAJE_DEL_ARBOL, MONTAJE_EXTERNO, "/tmp"),
    ]
    return _correr(orden)


def _en_espacio_de_nombres(repo, externo, taller):
    """`unshare -Urm` con `mount --bind` y `remount,ro,bind`. RESPALDO, sin identidad distinta."""
    montaje_repo = os.path.join(taller, "repo")
    montaje_externo = os.path.join(taller, "externo")
    montaje_propio = os.path.join(taller, "propio")
    interior = "\n".join([
        "set -e",
        "mkdir -p " + _entrecomillar(montaje_repo) + " "
        + _entrecomillar(montaje_externo) + " " + _entrecomillar(montaje_propio),
        "mount --bind " + _entrecomillar(os.path.abspath(repo)) + " "
        + _entrecomillar(montaje_repo),
        "mount -o remount,ro,bind " + _entrecomillar(montaje_repo),
        "mount --bind " + _entrecomillar(os.path.abspath(externo)) + " "
        + _entrecomillar(montaje_externo),
        "mount -o remount,ro,bind " + _entrecomillar(montaje_externo),
        "set +e",
        _guion(montaje_repo, montaje_externo, montaje_propio),
    ])
    orden = ["unshare", "--user", "--map-root-user", "--mount",
             "sh", "-c", interior]
    return _correr(orden)


def ejecutar(repo, externo, *, mecanismo=None, propio=None, informe_de_capacidades=None):
    """Ejecuta los intentos DENTRO del aislamiento y devuelve el informe, intento a intento."""
    informe = informe_de_capacidades or capacidades()
    por_mecanismo = {fila["mecanismo"]: fila for fila in informe["mecanismos"]}
    elegido = mecanismo or informe["elegido"]
    if elegido is None:
        raise AislamientoNoDisponible(
            "este anfitrión no ofrece ninguna forma de ejercer una identidad sin permiso "
            "de escritura: ni usuario del sistema distinto, ni contenedor, ni espacio de "
            "nombres. El contrato queda implementado y `V6-16` NO se declara completo",
            sondas=[fila["mecanismo"] + ": " + fila["motivo"]
                    for fila in informe["mecanismos"]],
        )
    fila = por_mecanismo.get(elegido)
    if fila is None or not fila["disponible"]:
        raise AislamientoNoDisponible(
            "el mecanismo de aislamiento `" + str(elegido) + "` no está disponible: "
            + (fila["motivo"] if fila else "no existe"))

    if elegido == "contenedor":
        codigo, salida, error = _en_contenedor(repo, externo, fila["imagen"])
    elif elegido == "espacio-de-nombres":
        taller = propio
        propio_temporal = None
        if taller is None:
            propio_temporal = tempfile.mkdtemp(prefix="ads-aislamiento-")
            taller = propio_temporal
        try:
            codigo, salida, error = _en_espacio_de_nombres(repo, externo, taller)
        finally:
            if propio_temporal is not None:
                shutil.rmtree(propio_temporal, ignore_errors=True)
    else:
        raise AislamientoNoDisponible(
            "el mecanismo `" + str(elegido) + "` no tiene ejecución implementada aquí: "
            "la opción de usuario del sistema exige aprovisionamiento del anfitrión")

    if codigo is None:
        raise AislamientoNoDisponible(
            "no se pudo ejecutar el aislamiento `" + elegido + "`: " + error)

    identidad, intentos = _interpretar(salida)
    faltan = [entrada["id"] for entrada in INTENTOS if entrada["id"] not in intentos]
    filas = []
    for entrada in INTENTOS:
        resultado = intentos.get(entrada["id"], {"codigo": -1, "mensaje": "no ejecutado"})
        filas.append({
            "intento": entrada["id"],
            "impedido": resultado["codigo"] != 0,
            "codigo": resultado["codigo"],
            "mensaje": resultado["mensaje"],
        })
    control = intentos.get(CONTROL_POSITIVO["id"], {"codigo": -1,
                                                    "mensaje": "no ejecutado"})
    lectura = intentos.get(CONTROL_DE_LECTURA["id"], {"codigo": -1,
                                                      "mensaje": "no ejecutado"})
    return {
        "mecanismo": elegido,
        "identidad_distinta": bool(fila["identidad_distinta"]),
        "identidad_del_verificador": identidad,
        "identidad_del_runtime": {"uid": str(os.getuid()), "gid": str(os.getgid())},
        "intentos": filas,
        "control_positivo": {
            "intento": CONTROL_POSITIVO["id"],
            "escribio": control["codigo"] == 0,
            "codigo": control["codigo"],
            "mensaje": control["mensaje"],
        },
        "control_de_lectura": {
            "intento": CONTROL_DE_LECTURA["id"],
            "leyo": lectura["codigo"] == 0,
            "codigo": lectura["codigo"],
            "mensaje": lectura["mensaje"],
        },
        "no_ejecutados": faltan,
        "salida_de_error": error.strip()[:400],
        "ok": (not faltan and all(entrada["impedido"] for entrada in filas)
               and control["codigo"] == 0 and lectura["codigo"] == 0),
    }


def exigir_sin_escritura(informe):
    """Fallo CERRADO: un solo intento que NO fue impedido invalida la demostración."""
    if informe["control_de_lectura"]["codigo"] != 0:
        raise EscrituraNoImpedida(
            "el CONTROL DE LECTURA falló: el árbol verificado y la evidencia externa no "
            "están montados dentro del aislamiento, luego los intentos no fallaron por "
            "falta de permiso sino porque los objetivos no existían"
        )
    if informe["control_positivo"]["codigo"] != 0:
        raise EscrituraNoImpedida(
            "el CONTROL POSITIVO no pudo escribir en su propio espacio: los intentos no "
            "fallaron por el aislamiento sino porque el intérprete no llegó a ejecutar "
            "nada, y la demostración no distingue el control del mutante"
        )
    permitidos = [entrada for entrada in informe["intentos"] if not entrada["impedido"]]
    if permitidos:
        raise EscrituraNoImpedida(
            "la identidad de la raíz externa SÍ pudo hacer "
            + str(len(permitidos)) + " de los intentos de escritura: "
            + ", ".join(entrada["intento"] for entrada in permitidos),
        )
    if informe["no_ejecutados"]:
        raise EscrituraNoImpedida(
            "hay intentos que no llegaron a ejecutarse: "
            + ", ".join(informe["no_ejecutados"])
        )
    return True


def serializar(informe):
    return json.dumps(informe, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
