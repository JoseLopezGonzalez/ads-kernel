#!/usr/bin/env python3
"""workspace — materializa y comprueba el workspace multi-fuente de un ADS Project.

Un ADS Project gobierna un PRODUCTO, no un repositorio. El producto puede estar repartido
entre varios repositorios Git independientes, declarados en `SOURCES.toml` en la raíz del
repositorio ADS de control. Contrato:
`kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md`.

    <workspace>/          NO es un repositorio Git. Es el contenedor del producto.
    ├── ads/              este repositorio: el CONTROL REPO
    ├── frontend/  .git/  fuentes, en la ruta que declara el manifiesto
    └── backend/   .git/

Órdenes:
    python3 tooling/workspace.py check   [--json]
    python3 tooling/workspace.py init    [ids...]  [--json]
    python3 tooling/workspace.py status  [--json]

Sin ids, `init` materializa todas las fuentes declaradas.

Sólo biblioteca estándar y Git por línea de órdenes. `SOURCES.toml` se lee con `tomllib`,
que es estándar desde Python 3.11: leer el manifiesto NO introduce ninguna dependencia.

TRES REGLAS QUE NO SON ESTILO, SINO SEGURIDAD:

  1. NINGÚN destino se acepta por su aspecto textual. `..` no es la única forma de salir de
     un directorio: un enlace simbólico en cualquier antecesor lo hace sin escribir un solo
     punto. Todo destino se resuelve de verdad —sin crearlo— antes de aceptarlo.
  2. `init` es TODO O NADA frente a los errores estáticos del manifiesto. Un manifiesto con
     cualquier error no clona, no crea directorios y no toca el disco.
  3. NINGUNA salida —texto, JSON o error— reproduce una credencial. El manifiesto declara
     identidad y nunca secretos, y aun así un secreto puesto por error no se propaga a un
     log, a una captura de pantalla ni a un issue.

Códigos de salida:  0 sin errores · 1 hay errores · 2 no se pudo empezar
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-04, en la zona hermana: con un
#  `hashlib.py` homónimo en `PYTHONPATH`, `validadores/huella.py` publicaba la huella
#  ESPERADA sobre un árbol MUTADO y `T150` salía SUPERADA con `EXIT=0`. Este punto
#  ejecutable no se libraba por vivir en `tooling/`: MATERIALIZA REPOSITORIOS —clona,
#  adopta y comprueba remotos—, entra en la huella de integridad por esa razón escrita en
#  `huella.py`, y un `subprocess.py`, un `tomllib` o un `json` homónimos le harían clonar,
#  o decir que clonó, lo que el lanzador quisiera. La zona `tooling/` estaba entera fuera
#  del inventario de `T306` por el mismo motivo que `validadores/`: el inventario era
#  mecánico DENTRO de dos zonas escritas a mano.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      Alternativas: (a) importar la purga de un módulo común; (b) copiar el prólogo entero
#      —recital incluido— desde `ads_runtime.py`; (c) copiar el MECANISMO byte a byte y
#      escribir el recital de esta sede.
#      Se elige (c). Con (a) la guardia dependería de un `import`, que es exactamente lo que
#      está protegiendo: una guardia que necesita importar ya ha perdido. Con (b) el recital
#      mentiría, porque el hecho reproducido allí no es el de aquí. Con (c) `T330` exige
#      —y comprueba— que el MECANISMO sea IDÉNTICO byte a byte en todos los puntos
#      ejecutables del árbol (digest `aa219465a6dd6a04`, 1 869 bytes), mientras cada sede
#      dice qué se midió en ella. Lo que protege es el mecanismo; lo que se lee, el recital.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación
#      distinta y convertiría un fallo de entorno en un fallo del aparato. Lo que `E-10`
#      nombra es concreto: `PYTHONPATH` y el `cwd`. Se retiran ésos, se cuenta cuántos, y el
#      recuento queda en `RETIRADAS_DE_LA_RUTA`.
import sys as _sys
import os as _os

_RAIZ_DEL_APARATO = _os.path.dirname(_os.path.abspath(__file__))


def _entradas_del_lanzador():
    """Lo que el LANZADOR puede meter en la ruta de importación: `PYTHONPATH` y el `cwd`."""
    sospechosas = set()
    for entrada in (_os.environ.get("PYTHONPATH") or "").split(_os.pathsep):
        if entrada:
            sospechosas.add(_os.path.realpath(entrada))
    try:
        sospechosas.add(_os.path.realpath(_os.getcwd()))
    except OSError:
        # Un `cwd` borrado bajo los pies no es motivo para no purgar el resto.
        pass
    return sospechosas


def _purgar_la_ruta_de_importacion():
    """Retira de `sys.path` lo que venga del lanzador. Devuelve cuántas entradas retiró."""
    del_lanzador = _entradas_del_lanzador()
    propia = _os.path.realpath(_RAIZ_DEL_APARATO)
    conservadas, retiradas = [], []
    for entrada in _sys.path:
        try:
            real = _os.path.realpath(entrada or _os.getcwd())
        except OSError:
            conservadas.append(entrada)
            continue
        if real != propia and real in del_lanzador:
            retiradas.append(real)
        else:
            conservadas.append(entrada)
    _sys.path[:] = conservadas
    return retiradas


RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()

# CONTROL DEL CONTROL de la purga: `os` se usa para poder purgar, así que si `os` mismo
# viniera del lanzador la purga no probaría nada. No hay forma honesta de seguir: se dice y
# se sale con el código de PROCEDENCIA.
if _os.path.realpath(_os.path.dirname(_os.__file__ or ".")) in _entradas_del_lanzador():
    _sys.stderr.write(
        "[PROCEDENCIA_NO_FIABLE] el módulo `os` procede de la ruta de importación del "
        "lanzador: este punto ejecutable no puede garantizar de dónde salen sus módulos y "
        "NO ejecuta\n")
    raise SystemExit(5)


import argparse
import json
import os
import re
import subprocess
import sys

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11
    tomllib = None

# LA GUARDA DE ENTORNO SE DECLARA UNA VEZ Y SE COMPRUEBA ANTES DE CORRER (A14). Vive en el
# kernel porque el kernel es la capa de abajo: que el tooling dependa del kernel es el
# sentido correcto de la flecha, y repetir aquí el número de versión sería el hallazgo A-12
# otra vez. Si el módulo no estuviera —una copia mutilada—, se dice y NO se calla.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "kernel", "operativo", "validadores"))
try:
    import entorno as _entorno
except ModuleNotFoundError:  # pragma: no cover - copia sin el kernel
    _entorno = None

MANIFIESTO = "SOURCES.toml"
SCHEMAS_SOPORTADOS = {1}
LAYOUTS_SOPORTADOS = {"siblings"}
RUTA_RESERVADA = "ads"

# Un `id` es un identificador ESTABLE dentro de ADS, y aparece en rutas de mensaje, en
# claves de JSON y en la salida que lee una persona. Se acota a lo que no puede
# confundirse con otra cosa: sin espacios, sin saltos de línea que inventen una línea de
# error falsa, y sin `.` ni `..` que parezcan una ruta.
ID_VALIDO = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")

ERROR, WARN, INFO = "ERROR", "WARN", "INFO"

# Esquemas cuya parte de usuario es un LOGIN de transporte, no un secreto:
# `ssh://git@github.com/org/repo.git` es una URL admitida y corriente.
ESQUEMAS_SSH = {"ssh", "git+ssh"}
# Los que esta herramienta sabe interpretar. Cualquier otro se trata como opaco.
ESQUEMAS_CONOCIDOS = ESQUEMAS_SSH | {"https", "http", "git", "file"}

_USERINFO = re.compile(r"(?P<esquema>[a-zA-Z][a-zA-Z0-9+.-]*)://(?P<userinfo>[^/@\s]*)@")


class Hallazgo:
    def __init__(self, nivel, ambito, mensaje):
        self.nivel, self.ambito, self.mensaje = nivel, ambito, mensaje

    def __str__(self):
        return f"{self.nivel:5}  {self.ambito:<24} {self.mensaje}"

    def a_dict(self):
        return {"nivel": self.nivel, "ambito": self.ambito, "mensaje": self.mensaje}


# --------------------------------------------------------------------- secretos
def redactar(texto):
    """Devuelve el texto con toda credencial embebida sustituida por `***`.

    Se aplica a TODO lo que sale de aquí: mensajes, JSON, errores de identidad y stderr de
    Git. El manifiesto no debe llevar credenciales —y si las lleva es ERROR—, pero un
    secreto puesto por error no puede además acabar en un log, en una captura o en un
    issue. La redacción es la última línea, no la primera.

    Un usuario SSH normal NO se redacta: `ssh://git@host/...` no contiene ningún secreto,
    y ocultarlo sólo haría el mensaje ilegible.
    """
    if not texto:
        return texto

    def _sub(m):
        esquema, userinfo = m.group("esquema"), m.group("userinfo")
        if esquema.lower() in ESQUEMAS_SSH and ":" not in userinfo:
            return m.group(0)
        if ":" in userinfo:
            return f"{esquema}://{userinfo.split(':', 1)[0]}:***@"
        return f"{esquema}://***@"

    return _USERINFO.sub(_sub, str(texto))


def credencial_embebida(url):
    """¿La URL lleva usuario y secreto, o sólo un usuario de transporte?

    §39 admite `ssh://git@github.com/org/repo.git`. Rechazarla por llevar `@` confundiría
    la forma canónica de SSH con un token, que es exactamente lo contrario de lo que este
    control existe para impedir.
    """
    m = _USERINFO.match(url or "")
    if not m:
        return False                       # scp-like `git@host:org/repo.git` incluido
    esquema, userinfo = m.group("esquema").lower(), m.group("userinfo")
    if ":" in userinfo:
        return True                        # usuario:secreto — siempre credencial
    if esquema in ESQUEMAS_SSH:
        return False                       # usuario SSH normal
    return bool(userinfo)                  # https://<token>@host/... también lo es


# --------------------------------------------------------------------------- Git
def git(args, cwd=None):
    """Ejecuta git y devuelve (codigo, stdout, stderr). Nunca lanza."""
    try:
        p = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except FileNotFoundError:
        return 127, "", "git no está instalado o no está en PATH"


def es_repo_git(ruta):
    if not os.path.isdir(os.path.join(ruta, ".git")):
        # un worktree tiene .git como FICHERO, no como directorio
        if not os.path.isfile(os.path.join(ruta, ".git")):
            return False
    cod, salida, _ = git(["rev-parse", "--is-inside-work-tree"], cwd=ruta)
    return cod == 0 and salida == "true"


# ------------------------------------------------------- identidad de un remoto
def _opaco(u):
    """No se sabe interpretar: sólo es igual a sí misma, carácter a carácter.

    Es la respuesta SEGURA. Inventar una identidad para lo que no se entiende es lo que
    hace que dos repositorios distintos pasen por el mismo.
    """
    return "opaco:" + u


def _local(p):
    """Ruta del sistema de ficheros.

    NO se pliegan mayúsculas ni se recorta `.git`: en un sistema sensible a mayúsculas
    `/srv/git/Foo.git` y `/srv/git/foo.git` son dos directorios distintos, y `foo.git` y
    `foo` también.
    """
    return "local:" + os.path.normpath(p).rstrip("/")


def _host_y_puerto(autoridad):
    """Separa host y puerto. Devuelve (None, None) si no es interpretable sin ambigüedad."""
    if autoridad.startswith("["):                       # literal IPv6
        cierre = autoridad.find("]")
        if cierre < 0:
            return None, None
        host, resto = autoridad[:cierre + 1], autoridad[cierre + 1:]
    else:
        host, sep, puerto = autoridad.partition(":")
        resto = (sep + puerto) if sep else ""
    if not host:
        return None, None
    if resto:
        if not re.match(r"^:\d+$", resto):
            return None, None
        return host.lower(), resto[1:]
    return host.lower(), None


def _identidad(host, puerto, ruta):
    """El host se pliega —DNS no distingue mayúsculas—; la RUTA no.

    Un servidor Git puede distinguir `Org/Repo` de `org/repo`, y plegarlo aquí igualaría
    dos repositorios que no lo son.
    """
    ruta = ruta.strip("/")
    if ruta.endswith(".git"):
        ruta = ruta[:-4]
    if not ruta:
        return _opaco(host if puerto is None else f"{host}:{puerto}")
    autoridad = host if puerto is None else f"{host}:{puerto}"
    return f"git:{autoridad}/{ruta}"


def normalizar_remoto(url):
    """Identidad comparable de un remoto Git, con criterio CONSERVADOR.

    Reconoce como el MISMO repositorio las tres formas documentadas en §39:

        https://github.com/org/repo.git
        git@github.com:org/repo.git
        ssh://git@github.com/org/repo.git

    La comparación textual ingenua diría que son tres repositorios distintos, y el
    resultado sería que `check` rechaza un workspace correcto por haberlo clonado con SSH
    en vez de HTTPS.

    Lo que NO iguala, porque igualarlo sería peor que avisar de más:

        · el mismo host con puertos distintos            — son dos servidores
        · rutas que sólo difieren en su capitalización   — puede ser significativa
        · esquemas desconocidos y URLs ambiguas          — se devuelven opacas

    Ante lo que no sabe interpretar la comparación falla de forma SEGURA: prefiere avisar
    de más a aceptar de menos.
    """
    if not isinstance(url, str) or not url.strip():
        return ""
    u = url.strip()

    m = re.match(r"^(?P<esquema>[a-zA-Z][a-zA-Z0-9+.-]*)://(?P<resto>.*)$", u, re.S)
    if m:
        esquema, resto = m.group("esquema").lower(), m.group("resto")
        if esquema not in ESQUEMAS_CONOCIDOS:
            return _opaco(u)
        if esquema == "file":
            return _local(resto[resto.index("/"):] if "/" in resto else resto)
        autoridad, sep, ruta = resto.partition("/")
        if not sep or not ruta:
            return _opaco(u)
        _, _, hostport = autoridad.rpartition("@")
        host, puerto = _host_y_puerto(hostport)
        if host is None:
            return _opaco(u)
        return _identidad(host, puerto, ruta)

    # scp-like `[usuario@]host:ruta`, y SÓLO cuando es inequívoco: o lleva usuario
    # explícito, o el host tiene un punto. Sin esa condición `C:\repos\x` se leería como
    # el host «C».
    m = re.match(r"^(?:(?P<usuario>[^@/\s]+)@)?(?P<host>[A-Za-z0-9._-]+):(?P<ruta>[^\\/].*)$", u)
    if m and (m.group("usuario") or "." in m.group("host")):
        return _identidad(m.group("host").lower(), None, m.group("ruta"))

    if u.startswith(("/", "./", "../", "~")) or re.match(r"^[a-zA-Z]:[\\/]", u):
        return _local(u)
    return _opaco(u)


# --------------------------------------------------------------------------- raíces
def localizar_control_repo(desde=None):
    """Sube desde `desde` hasta encontrar el SOURCES.toml del repositorio de control.

    Permite ejecutar la orden desde cualquier subdirectorio del control repo, que es lo
    que hace un agente que está trabajando dentro de `docs/` o de `kernel/`.
    """
    actual = os.path.abspath(desde or os.getcwd())
    while True:
        if os.path.isfile(os.path.join(actual, MANIFIESTO)):
            return actual
        padre = os.path.dirname(actual)
        if padre == actual:
            return None
        actual = padre


def raices(desde=None):
    ads_root = localizar_control_repo(desde)
    if ads_root is None:
        return None, None
    return ads_root, os.path.dirname(ads_root)


# --------------------------------------------------------------------- manifiesto
class Manifiesto:
    def __init__(self):
        self.schema = None
        self.layout = None
        self.sources = []
        self.components = []


def _real_sin_crear(ruta):
    """`realpath` de una ruta que puede no existir todavía, sin crear nada.

    `os.path.normpath` es TEXTUAL y no ve los enlaces simbólicos: si un antecesor dentro
    del workspace apunta a otro sitio, una ruta sin un solo `..` escribe fuera. Se resuelve
    el antecesor que SÍ existe y se le añade el resto.
    """
    pendientes = []
    actual = os.path.abspath(ruta)
    while True:
        if os.path.lexists(actual):
            real = os.path.realpath(actual)
            return os.path.join(real, *reversed(pendientes)) if pendientes else real
        padre = os.path.dirname(actual)
        if padre == actual:
            return os.path.normpath(actual)
        pendientes.append(os.path.basename(actual))
        actual = padre


def _dentro(hijo, padre):
    """¿`hijo` es `padre` o está debajo de él? Comparación por segmentos, no por prefijo."""
    h, p = os.path.normcase(os.path.normpath(hijo)), os.path.normcase(os.path.normpath(padre))
    return h == p or h.startswith(p.rstrip(os.sep) + os.sep)


def _ruta_segura(valor, base, campo, ambito, hallazgos, permitir_base=False):
    """Comprueba que `valor` es una ruta relativa cuyo destino REAL no escapa de `base`.

    Un manifiesto es contenido versionado que un agente puede modificar. Una ruta
    `../../otro-proyecto` convertiría `init` en una herramienta para escribir fuera del
    workspace, y eso no puede depender de que nadie la escriba. Un enlace simbólico hace
    lo mismo sin escribir un solo punto, y por eso no basta con mirar el texto.
    """
    if not isinstance(valor, str) or not valor.strip():
        hallazgos.append(Hallazgo(ERROR, ambito, f"{campo} vacío o no es texto"))
        return None
    if os.path.isabs(valor) or re.match(r"^[a-zA-Z]:[\\/]", valor):
        hallazgos.append(Hallazgo(ERROR, ambito, f"{campo} '{valor}' es una ruta absoluta"))
        return None

    base_n = os.path.normpath(os.path.abspath(base))
    textual = os.path.normpath(os.path.join(base_n, valor))
    if not _dentro(textual, base_n):
        hallazgos.append(Hallazgo(ERROR, ambito, f"{campo} '{valor}' escapa de {base_n}"))
        return None

    real_base = _real_sin_crear(base_n)
    real = _real_sin_crear(textual)
    if not _dentro(real, real_base):
        # el texto parecía relativo; el destino no lo es
        hallazgos.append(Hallazgo(
            ERROR, ambito,
            f"{campo} '{valor}' escapa de {base_n} al resolver los enlaces simbólicos: "
            f"apunta a '{real}'"))
        return None
    if not permitir_base and _dentro(real_base, real):
        hallazgos.append(Hallazgo(
            ERROR, ambito,
            f"{campo} '{valor}' resuelve a la propia raíz '{base_n}'. El workspace es el "
            f"contenedor del producto y NO es un repositorio Git (C6, topología)"))
        return None
    return real


# ---------------------------------------------------------- lectura tipada del TOML
def _tabla(datos, clave, ambito, hallazgos, obligatoria=False):
    """Devuelve `datos[clave]` sólo si es una TABLA. Nunca deja pasar otra cosa a `.get()`."""
    if clave not in datos:
        if obligatoria:
            hallazgos.append(Hallazgo(ERROR, ambito, f"falta la tabla `[{clave}]`"))
        return {}
    valor = datos[clave]
    if not isinstance(valor, dict):
        hallazgos.append(Hallazgo(
            ERROR, ambito,
            f"`{clave}` es {type(valor).__name__}, y tiene que ser una tabla `[{clave}]`"))
        return {}
    return valor


def _lista_de_tablas(datos, clave, hallazgos):
    """Devuelve `datos[clave]` como lista de tablas, descartando —con error— lo que no lo sea."""
    if clave not in datos:
        return []
    valor = datos[clave]
    if not isinstance(valor, list):
        hallazgos.append(Hallazgo(
            ERROR, clave,
            f"`{clave}` es {type(valor).__name__}, y tiene que ser una lista de tablas "
            f"`[[{clave}]]`"))
        return []
    limpias = []
    for i, entrada in enumerate(valor):
        if not isinstance(entrada, dict):
            hallazgos.append(Hallazgo(
                ERROR, f"{clave}[{i}]",
                f"la entrada es {type(entrada).__name__}, y tiene que ser una tabla "
                f"`[[{clave}]]`"))
            continue
        limpias.append((i, entrada))
    return limpias


def _entero(valor):
    """`True` es un `bool`, y en Python `True == 1`. Un `schema = true` NO es `schema = 1`."""
    return isinstance(valor, int) and not isinstance(valor, bool)


def _identificador(tabla, ambito, hallazgos):
    """Lee y valida un `id`. Devuelve None si no sirve como identificador."""
    valor = tabla.get("id")
    if valor is None:
        hallazgos.append(Hallazgo(ERROR, ambito, "falta `id`"))
        return None
    if not isinstance(valor, str):
        hallazgos.append(Hallazgo(
            ERROR, ambito, f"`id` es {type(valor).__name__}, y tiene que ser texto"))
        return None
    if not ID_VALIDO.match(valor):
        visible = valor.strip() or "(vacío)"
        hallazgos.append(Hallazgo(
            ERROR, ambito,
            f"`id` {visible!r} no es un identificador válido: se admiten letras, dígitos, "
            f"`.`, `-` y `_`, empezando por letra o dígito, hasta 64 caracteres"))
        return None
    return valor


def _texto_opcional(tabla, campo, ambito, hallazgos):
    """Un campo descriptivo puede faltar; si está, tiene que ser texto no vacío."""
    if campo not in tabla:
        return None
    valor = tabla[campo]
    if not isinstance(valor, str) or not valor.strip():
        hallazgos.append(Hallazgo(
            ERROR, ambito,
            f"`{campo}` está declarado y no es texto no vacío "
            f"({type(valor).__name__}). Es opcional: o se omite, o se escribe"))
        return None
    return valor


def leer_manifiesto(ads_root, workspace_root, hallazgos):
    ruta = os.path.join(ads_root, MANIFIESTO)
    if tomllib is None:
        hallazgos.append(Hallazgo(ERROR, MANIFIESTO,
                                  "se requiere Python 3.11 o superior para leer TOML"))
        return None
    try:
        with open(ruta, "rb") as fh:
            datos = tomllib.load(fh)
    except OSError as e:
        hallazgos.append(Hallazgo(ERROR, MANIFIESTO, f"no se puede leer: {e}"))
        return None
    except tomllib.TOMLDecodeError as e:
        hallazgos.append(Hallazgo(ERROR, MANIFIESTO, f"TOML inválido: {e}"))
        return None
    if not isinstance(datos, dict):                       # tomllib no lo produce; el
        hallazgos.append(Hallazgo(ERROR, MANIFIESTO,      # contrato se comprueba igual
                                  "el manifiesto no es una tabla TOML"))
        return None

    m = Manifiesto()

    m.schema = datos.get("schema")
    if m.schema is None:
        hallazgos.append(Hallazgo(ERROR, "schema", "falta `schema`: sin él, el formato es ambiguo"))
    elif not _entero(m.schema):
        hallazgos.append(Hallazgo(
            ERROR, "schema",
            f"`schema` es {type(m.schema).__name__}, y tiene que ser un entero "
            f"(soportados: {sorted(SCHEMAS_SOPORTADOS)})"))
    elif m.schema not in SCHEMAS_SOPORTADOS:
        hallazgos.append(Hallazgo(
            ERROR, "schema",
            f"schema {m.schema!r} no soportado (soportados: {sorted(SCHEMAS_SOPORTADOS)})"))

    ws = _tabla(datos, "workspace", "workspace", hallazgos, obligatoria=True)
    m.layout = ws.get("layout")
    if m.layout is None:
        hallazgos.append(Hallazgo(ERROR, "workspace", "falta `[workspace] layout`"))
    elif not isinstance(m.layout, str):
        hallazgos.append(Hallazgo(
            ERROR, "workspace",
            f"`layout` es {type(m.layout).__name__}, y tiene que ser texto "
            f"(soportados: {sorted(LAYOUTS_SOPORTADOS)})"))
    elif m.layout not in LAYOUTS_SOPORTADOS:
        hallazgos.append(Hallazgo(
            ERROR, "workspace",
            f"layout {m.layout!r} no soportado (soportados: {sorted(LAYOUTS_SOPORTADOS)})"))

    real_ads = _real_sin_crear(ads_root)
    ids_vistos, rutas_vistas = {}, {}
    for i, s in _lista_de_tablas(datos, "sources", hallazgos):
        ambito = f"sources[{i}]"
        sid = _identificador(s, ambito, hallazgos)
        if sid is None:
            continue
        ambito = f"source:{sid}"
        if sid in ids_vistos:
            hallazgos.append(Hallazgo(ERROR, ambito, f"`id` duplicado: ya lo usa sources[{ids_vistos[sid]}]"))
            continue
        ids_vistos[sid] = i

        remoto = s.get("remote")
        if not isinstance(remoto, str) or not remoto.strip():
            hallazgos.append(Hallazgo(ERROR, ambito, "falta `remote`: la identidad de una fuente es su remoto"))
            remoto = ""
        elif credencial_embebida(remoto):
            hallazgos.append(Hallazgo(
                ERROR, ambito,
                "`remote` embebe credenciales. El manifiesto declara identidad, nunca secretos"))

        ruta = s.get("path")
        destino = _ruta_segura(ruta, workspace_root, "path", ambito, hallazgos)
        if destino is None:
            continue
        # `ads` es la ruta convencional del control repo, y se rechaza por su nombre para
        # que el motivo sea legible. Pero el control repo es DONDE ESTÁ el manifiesto, no
        # una cadena: lo que decide es el destino real.
        if os.path.normpath(ruta) == RUTA_RESERVADA:
            hallazgos.append(Hallazgo(
                ERROR, ambito,
                f"`path` '{ruta}' está reservado para el repositorio ADS de control"))
            continue
        if _dentro(destino, real_ads):
            hallazgos.append(Hallazgo(
                ERROR, ambito,
                f"`path` '{ruta}' cae DENTRO del repositorio ADS de control ({real_ads}). "
                f"C6 prohíbe clonar las fuentes dentro del control repo"))
            continue
        if _dentro(real_ads, destino):
            hallazgos.append(Hallazgo(
                ERROR, ambito,
                f"`path` '{ruta}' CONTIENE al repositorio ADS de control ({real_ads}): "
                f"el control repo quedaría anidado dentro de una fuente"))
            continue
        colision = None
        for otra, sid_otro in rutas_vistas.items():
            if _dentro(destino, otra) or _dentro(otra, destino):
                colision = (otra, sid_otro)
                break
        if colision:
            otra, sid_otro = colision
            relacion = ("es la misma ruta que" if os.path.normcase(otra) == os.path.normcase(destino)
                        else "anida repositorios Git con")
            hallazgos.append(Hallazgo(
                ERROR, ambito,
                f"`path` '{ruta}' colisiona con la fuente '{sid_otro}': {relacion} la suya. "
                f"Git permanece INDEPENDIENTE por fuente (C6 N12)"))
            continue
        rutas_vistas[destino] = sid

        m.sources.append({"id": sid, "remote": remoto, "path": os.path.normpath(ruta),
                          "abs": destino})

    por_id = {s["id"]: s for s in m.sources}
    ids_comp = {}
    for i, c in _lista_de_tablas(datos, "components", hallazgos):
        ambito = f"components[{i}]"
        cid = _identificador(c, ambito, hallazgos)
        if cid is None:
            continue
        ambito = f"component:{cid}"
        if cid in ids_comp:
            hallazgos.append(Hallazgo(ERROR, ambito, "`id` de componente duplicado"))
            continue
        ids_comp[cid] = i

        src = c.get("source")
        if not isinstance(src, str) or not src.strip():
            hallazgos.append(Hallazgo(
                ERROR, ambito, "falta `source`: un componente referencia siempre una fuente"))
            continue
        if src not in por_id:
            hallazgos.append(Hallazgo(
                ERROR, ambito,
                f"referencia la fuente '{src}', que no está declarada en `sources`"))
            continue
        cpath = c.get("path", ".")
        # la ruta del componente se resuelve DENTRO de su fuente: un componente que
        # apunta fuera de su fuente no es un componente, es otra fuente sin declarar.
        # `path = "."` SÍ es válido: es el componente que ocupa la fuente entera.
        if _ruta_segura(cpath, por_id[src]["abs"], "path", ambito, hallazgos,
                        permitir_base=True) is None:
            continue
        # `kind` es DESCRIPTIVO y abierto (plantilla SOURCES.toml): opcional por el modelo
        # aprobado. Lo que no se admite es declararlo mal.
        kind = _texto_opcional(c, "kind", ambito, hallazgos)
        m.components.append({"id": cid, "source": src, "path": os.path.normpath(cpath),
                             "kind": kind})
    return m


# --------------------------------------------------------------------------- estado
def estado_de_fuente(s):
    """Fotografía de una fuente en disco. No modifica nada."""
    # Los remotos SALEN redactados. El de disco tampoco es de fiar: nada impide que
    # alguien haya clonado con un token en la URL, y `check` lo imprimiría.
    e = {"id": s["id"], "path": s["path"], "remote": redactar(s["remote"]), "present": False,
         "is_git": False, "branch": None, "head": None, "dirty": None,
         "remote_actual": None, "remote_ok": None}
    if not os.path.isdir(s["abs"]):
        return e
    e["present"] = True
    if not es_repo_git(s["abs"]):
        return e
    e["is_git"] = True
    cod, salida, _ = git(["rev-parse", "--abbrev-ref", "HEAD"], cwd=s["abs"])
    e["branch"] = salida if cod == 0 else None
    cod, salida, _ = git(["rev-parse", "--short", "HEAD"], cwd=s["abs"])
    e["head"] = salida if cod == 0 else None
    cod, salida, _ = git(["status", "--porcelain"], cwd=s["abs"])
    e["dirty"] = bool(salida) if cod == 0 else None
    cod, salida, _ = git(["remote", "get-url", "origin"], cwd=s["abs"])
    origen = salida if cod == 0 else None
    e["remote_actual"] = redactar(origen)
    if origen and s["remote"]:
        e["remote_ok"] = normalizar_remoto(origen) == normalizar_remoto(s["remote"])
    elif s["remote"]:
        e["remote_ok"] = False
    return e


def comprobar_disco(m, hallazgos, solo=None):
    estados = []
    for s in m.sources:
        if solo and s["id"] not in solo:
            continue
        e = estado_de_fuente(s)
        estados.append(e)
        amb = f"source:{s['id']}"
        if not e["present"]:
            hallazgos.append(Hallazgo(
                INFO, amb, f"no materializada en '{s['path']}' — `init {s['id']}` la clona"))
            continue
        if not e["is_git"]:
            hallazgos.append(Hallazgo(
                ERROR, amb,
                f"'{s['path']}' existe y NO es un repositorio Git. No se clona encima"))
            continue
        if e["remote_actual"] is None:
            hallazgos.append(Hallazgo(
                ERROR, amb, "el repositorio no tiene remoto `origin`: no puede demostrarse su identidad"))
        elif e["remote_ok"] is False:
            hallazgos.append(Hallazgo(
                ERROR, amb,
                f"identidad remota distinta de la declarada. Declarado "
                f"'{redactar(s['remote'])}', encontrado '{e['remote_actual']}'. "
                f"No se cambia el remoto automáticamente"))
        if e["dirty"]:
            hallazgos.append(Hallazgo(
                WARN, amb, "tiene cambios sin confirmar. No es un error, y no se tocan"))
    return estados


# --------------------------------------------------------------------------- órdenes
def orden_check(m, hallazgos):
    if m is not None and not m.sources:
        hallazgos.append(Hallazgo(
            INFO, "sources",
            "ninguna fuente declarada. Es válido: un producto nuevo aún no tiene código"))
    estados = comprobar_disco(m, hallazgos) if m else []
    return {"sources": estados}


def orden_init(m, hallazgos, pedidas):
    if m is None:
        return {"sources": []}
    conocidas = {s["id"] for s in m.sources}
    desconocidas = [i for i in pedidas if i not in conocidas]
    for i in desconocidas:
        hallazgos.append(Hallazgo(ERROR, f"source:{i}", "no está declarada en el manifiesto"))
    objetivo = [s for s in m.sources if not pedidas or s["id"] in pedidas]

    acciones = []
    for s in objetivo:
        amb = f"source:{s['id']}"
        e = estado_de_fuente(s)
        if e["present"]:
            if not e["is_git"]:
                hallazgos.append(Hallazgo(
                    ERROR, amb,
                    f"'{s['path']}' existe y no es un repositorio Git. "
                    f"No se borra, no se sobrescribe y no se clona encima"))
                acciones.append({"id": s["id"], "accion": "error-no-git"})
                continue
            if e["remote_ok"] is False:
                hallazgos.append(Hallazgo(
                    ERROR, amb,
                    f"'{s['path']}' es otro repositorio. Declarado "
                    f"'{redactar(s['remote'])}', encontrado '{e['remote_actual']}'. "
                    f"No se cambia el remoto ni se reemplaza"))
                acciones.append({"id": s["id"], "accion": "error-otra-identidad"})
                continue
            # Reutilizar es la regla, no una optimización: volver a clonar sobre trabajo
            # local existente es la forma más rápida de perderlo.
            hallazgos.append(Hallazgo(INFO, amb, "ya materializada y correcta: se reutiliza"))
            acciones.append({"id": s["id"], "accion": "reutilizada"})
            continue

        if not s["remote"]:
            hallazgos.append(Hallazgo(ERROR, amb, "sin `remote` declarado: no hay de dónde clonar"))
            acciones.append({"id": s["id"], "accion": "error-sin-remoto"})
            continue
        padre = os.path.dirname(s["abs"])
        try:
            os.makedirs(padre, exist_ok=True)
        except OSError as ex:
            hallazgos.append(Hallazgo(ERROR, amb, f"no se puede crear '{padre}': {ex}"))
            acciones.append({"id": s["id"], "accion": "error-directorio"})
            continue
        cod, _, err = git(["clone", s["remote"], s["abs"]])
        if cod != 0:
            # el mensaje de git puede contener la URL. Ni la URL declarada ni el stderr
            # de git salen en crudo: los dos pasan por `redactar`, y de stderr sólo se
            # publica su última línea.
            detalle = redactar(err.splitlines()[-1]) if err else "sin detalle"
            hallazgos.append(Hallazgo(
                ERROR, amb,
                f"clone falló desde '{redactar(s['remote'])}' — {detalle}"))
            acciones.append({"id": s["id"], "accion": "error-clone"})
            continue
        hallazgos.append(Hallazgo(INFO, amb, f"clonada en '{s['path']}'"))
        acciones.append({"id": s["id"], "accion": "clonada"})

    # `init` NO sincroniza: preparar un workspace y sincronizar un trabajo son
    # operaciones distintas, y confundirlas altera repos con trabajo local sin avisar.
    return {"sources": acciones}


def orden_status(m, hallazgos):
    estados = comprobar_disco(m, hallazgos) if m else []
    return {"sources": estados}


def imprimir_status(estados):
    if not estados:
        print("(ninguna fuente declarada)")
        return
    cab = f"{'SOURCE':<14}{'PATH':<14}{'PRESENT':<9}{'BRANCH':<18}{'HEAD':<10}{'DIRTY':<7}REMOTE"
    print(cab)
    for e in estados:
        presente = "yes" if e["present"] else "no"
        if e["present"] and not e["is_git"]:
            presente = "NO-GIT"
        remoto = "-" if not e["present"] else ("ok" if e["remote_ok"] else "MISMATCH")
        if e["present"] and e["is_git"] and e["remote_actual"] is None:
            remoto = "SIN-ORIGIN"
        print(f"{e['id']:<14}{e['path']:<14}{presente:<9}"
              f"{(e['branch'] or '-'):<18}{(e['head'] or '-'):<10}"
              f"{('yes' if e['dirty'] else 'no' if e['dirty'] is not None else '-'):<7}{remoto}")


def main():
    ap = argparse.ArgumentParser(description="workspace multi-fuente de un ADS Project")
    ap.add_argument("orden", choices=["check", "init", "status"])
    ap.add_argument("ids", nargs="*", help="fuentes concretas; sin ids, todas")
    ap.add_argument("--json", action="store_true", help="salida legible por máquina")
    ap.add_argument("--raiz", help="directorio desde el que localizar el control repo")
    args = ap.parse_args()

    # ANTES DE CORRER. No al fallar el primer `tomllib.load` a mitad del análisis: entonces
    # el defecto ya se ha disfrazado de defecto del manifiesto. Termina con código 78, que
    # no es ni el 1 de «hay errores» ni el 2 de «no se pudo empezar».
    if _entorno is not None:
        _entorno.exigir()
    elif tomllib is None:
        print("ERROR  se requiere Python 3.11 o superior para leer TOML, y falta además "
              "la guarda de entorno del kernel", file=sys.stderr)
        return 2

    ads_root, workspace_root = raices(args.raiz)
    if ads_root is None:
        msg = (f"no se encuentra {MANIFIESTO} ni aquí ni en ningún directorio superior. "
               f"Esta orden se ejecuta dentro del repositorio ADS de control")
        if args.json:
            print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False, indent=2))
        else:
            print(f"ERROR  {msg}", file=sys.stderr)
        return 2

    hallazgos = []
    m = leer_manifiesto(ads_root, workspace_root, hallazgos)
    # TODO O NADA. `init` es la única orden que MUTA el disco, y no puede empezar a
    # clonar mientras el manifiesto que le dice qué clonar tiene errores. La entrega
    # anterior clonaba las fuentes válidas de un manifiesto con layout inválido: el
    # workspace quedaba a medias y el error se leía después, ya sobre el destrozo.
    estatico_roto = m is None or any(h.nivel == ERROR for h in hallazgos)

    if args.orden == "check":
        datos = orden_check(m, hallazgos)
    elif args.orden == "init":
        if estatico_roto:
            hallazgos.append(Hallazgo(
                ERROR, MANIFIESTO,
                "init NO ha ejecutado ninguna acción: el manifiesto tiene errores "
                "estáticos. No se ha creado ningún directorio ni clonado ninguna fuente. "
                "Corrígelos y vuelve a ejecutarlo"))
            datos = {"sources": []}
        else:
            datos = orden_init(m, hallazgos, set(args.ids))
    else:
        datos = orden_status(m, hallazgos)

    errores = [h for h in hallazgos if h.nivel == ERROR]
    avisos = [h for h in hallazgos if h.nivel == WARN]

    if args.json:
        print(json.dumps({
            "ok": not errores,
            "orden": args.orden,
            "ads_root": ads_root,
            "workspace_root": workspace_root,
            "schema": m.schema if m else None,
            "layout": m.layout if m else None,
            "components": m.components if m else [],
            "hallazgos": [h.a_dict() for h in hallazgos],
            **datos,
        }, ensure_ascii=False, indent=2))
    else:
        print(f"control repo : {ads_root}")
        print(f"workspace    : {workspace_root}")
        if args.orden == "status":
            print()
            imprimir_status(datos.get("sources", []))
            print()
        for h in hallazgos:
            print(h, file=sys.stderr if h.nivel == ERROR else sys.stdout)
        print(f"\n{len(errores)} errores · {len(avisos)} avisos")

    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
