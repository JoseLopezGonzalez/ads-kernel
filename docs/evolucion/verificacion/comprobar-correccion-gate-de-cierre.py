#!/usr/bin/env python3
"""Bateria mecanica de la correccion del gate de cierre de F4c.

Cada comprobacion DERIVA su resultado del arbol. Ninguna cifra esta escrita a mano:
las que aparecen abajo son las EXIGIDAS, y el fallo se produce cuando lo derivado difiere.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  El prólogo de `E-10` que sigue purga `sys.path` DESDE DENTRO del programa, y por eso
#  llega tarde contra `sitecustomize`: `site.py` lo importa mientras el intérprete arranca,
#  antes de que exista la primera sentencia de este fichero. La guarda cambia el MOMENTO
#  —comprueba las banderas de aislamiento y, si no están, se reejecuta con `-I -S -E`—, y
#  por eso las dos conviven: `G-03` impide que el gancho llegue a existir, y `E-10` sigue
#  cubriendo la contaminación de la ruta en el caso importado.
#
#  POR QUÉ ESTE PUNTO. Hasta hoy los cuatro ejecutables de `docs/evolucion/verificacion/`
#  eran los ÚNICOS del inventario sin guarda, declarados con motivo y con cliquet en `T380`
#  porque el agente que hizo `G-03` tenía prohibido tocar esta zona. Son el instrumento con
#  el que se mide si un gate cubre lo que dice cubrir y qué universo obligatorio existe: un
#  `hashlib` o un `json` sustituidos por quien los corre deciden esas dos respuestas. La
#  declaración se retira porque la excepción se ha cerrado, no porque haya caducado.

import os as _os_g03
import sys as _sys_g03

# LA GUARDA NO DEJA RASTRO EN EL ÁRBOL QUE JUZGA. Medido: al importar la guarda, Python
# escribía `validadores/__pycache__/aislamiento_de_arranque…pyc` en el árbol, y
# `comprobar_arranque.py` empezó a publicar «el proyecto arrastra `__pycache__`» sobre
# proyectos recién creados. Se desactiva la escritura de bytecode DURANTE la guarda y se
# devuelve al estado que tenía: lo que el punto importe después sigue cacheándose como
# siempre, y no se paga rendimiento por una comprobación que corre una vez.
_G03_BYTECODE = _sys_g03.dont_write_bytecode
_sys_g03.dont_write_bytecode = True
_G03_PROPIA = _os_g03.path.dirname(_os_g03.path.realpath(__file__))
_G03_SEDE = ""
_G03_RAIZ = _G03_PROPIA
while not _G03_SEDE:
    for _G03_CANDIDATA in (_G03_PROPIA,
                           _os_g03.path.join(_G03_RAIZ, "kernel", "operativo",
                                             "validadores")):
        if _os_g03.path.isfile(_os_g03.path.join(_G03_CANDIDATA,
                                                 "aislamiento_de_arranque.py")):
            _G03_SEDE = _G03_CANDIDATA
            break
    else:
        _G03_PADRE = _os_g03.path.dirname(_G03_RAIZ)
        if _G03_PADRE == _G03_RAIZ:
            _sys_g03.stderr.write(
                "[PROCEDENCIA_NO_FIABLE] no hay `aislamiento_de_arranque.py` ni junto a "
                "este punto ejecutable ni en el `kernel/operativo/validadores/` de ning\u00fan "
                "ancestro suyo: no se puede decidir si el arranque est\u00e1 aislado, y no se "
                "sigue\n")
            raise SystemExit(5)
        _G03_RAIZ = _G03_PADRE
_sys_g03.path.insert(0, _G03_SEDE)
import aislamiento_de_arranque as _aislamiento_g03                    # noqa: E402

AISLAMIENTO = _aislamiento_g03.exigir(__file__, __name__)
_sys_g03.dont_write_bytecode = _G03_BYTECODE

# `-I` deja FUERA de `sys.path` el directorio del guión —es lo que impide que un homónimo
# vecino se cuele— y los puntos que importan módulos hermanos lo necesitan. Se reintroduce
# por RUTA DERIVADA DE `__file__`, que no la escribe el lanzador.
if _G03_PROPIA not in _sys_g03.path:
    _sys_g03.path.insert(0, _G03_PROPIA)

# `E-10` · LA PROCEDENCIA DE LOS MÓDULOS, PURGADA ANTES DE NINGÚN `import` PROPIO
#
#  POR QUÉ ESTÁ AQUÍ, Y NO SÓLO EN `kernel/operativo/runtime/`. `H-01` de la auditoría del
#  2026-09-04 midió que `validadores/huella.py` no llevaba este prólogo y que, con un
#  `hashlib` homónimo en `PYTHONPATH`, **un árbol MUTADO producía la huella esperada y
#  `T150` publicaba SUPERADA con `EXIT=0`**. El mismo defecto vive en cualquier ejecutable
#  que decida algo y no purgue: éstos deciden qué universo obligatorio existe y si un gate
#  puede adjudicar, que es tanto o más que una huella.
#
#  DECISIÓN · se purga ANTES de importar nada propio, con lo único que el intérprete ya cargó
#      Purgar después de los `import` normales llega tarde —el homónimo ya está en
#      `sys.modules`— y purgar desde un módulo aparte depende de un `import`, que es
#      exactamente lo que se está protegiendo. `sys` es incorporado y `os` lo carga el
#      arranque, así que los dos vienen de `sys.modules` y no de la ruta. Que `os` sea el
#      bueno se COMPRUEBA, no se supone.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación y
#      convertiría un fallo de entorno en un fallo del aparato. `E-10` nombra dos cosas
#      concretas: `PYTHONPATH` y el `cwd`. Se retiran ésas y el recuento se publica.
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



import atexit, hashlib, io, os, re, subprocess, sys, traceback
from collections import Counter

# La raíz se DERIVA de `__file__` y de nada más.
#
# Este fichero vive en `docs/evolucion/verificacion/`, luego la raíz del repositorio está
# TRES niveles por encima. No se usa el cwd —una batería que dependiera de desde dónde se
# invoca no sería auditable—, y no se codifica la ruta de ninguna máquina: la versión
# anterior caía a `/home/jose/ads-kernel` y, en cualquier otro clon o worktree, comprobaba
# el repositorio del autor en vez del que tenía delante. Eso hacía que la batería diera
# verde sobre un árbol que nadie estaba mirando.
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir, os.pardir, os.pardir))

_ESPERADOS = ("docs/evolucion", "docs/rediseno", "kernel/operativo")
_faltan = [d for d in _ESPERADOS if not os.path.isdir(os.path.join(RAIZ, d))]
if _faltan:
    sys.stderr.write(
        f"ESTRUCTURA NO ENCONTRADA bajo la raíz derivada de __file__.\n"
        f"  raíz derivada : {RAIZ}\n"
        f"  script        : {os.path.abspath(__file__)}\n"
        f"  faltan        : {', '.join(_faltan)}\n"
        f"Esta batería espera vivir en `docs/evolucion/verificacion/` dentro del "
        f"repositorio ADS. No se adivina otra raíz ni se recurre al cwd: comprobar un "
        f"árbol que no es el que se pidió comprobar es peor que no comprobar nada.\n")
    sys.exit(2)
D11 = os.path.join(RAIZ, "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md")
DEC = os.path.join(RAIZ, "docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md")
CHK = os.path.join(RAIZ, "docs/evolucion/CHECKPOINT-ADS-NEXT.md")
IDX = os.path.join(RAIZ, "docs/evolucion/00-INDICE.md")

# ── lectura que FALLA CERRADO y NOMBRA la causa (`Q-24`) ──────────────────
#
# `Q-24`. `leer()` era `io.open(p, encoding="utf-8").read()` a secas, y se invoca desde
# `_derivar_vigiladas()` y desde el barrido de sedes del catálogo, las dos ANTES de que
# `G-24` —la comprobación cuyo objeto es exactamente ése— llegue a ejecutarse. Un fichero
# del kernel ausente o no-UTF-8 tumbaba el proceso con un `traceback` y SIN INFORME: cero
# comprobaciones impresas, ningún diagnóstico, y un código de salida que nadie sabía leer.
# Una batería que aborta no dice «rojo»: dice nada, que es peor.
#
# Ahora toda lectura pasa por aquí, cualquier fallo se convierte en `SedeIlegible` con el
# fichero y el motivo NOMBRADOS, y —abajo— el informe se emite pase lo que pase.
class SedeIlegible(Exception):
    """Un fichero que la batería necesita no se puede leer. Nombra ruta y motivo."""

def _motivo_ilegible(ruta):
    """El motivo por el que `ruta` no se puede leer como UTF-8 con contenido, o None."""
    try:
        with io.open(ruta, encoding="utf-8") as fh:
            if not fh.read().strip():
                return "vacío"
    except FileNotFoundError:
        return "no existe"
    except IsADirectoryError:
        return "es un directorio, no un fichero"
    except UnicodeDecodeError:
        return "no es UTF-8"
    except OSError as e:
        return "no se puede abrir: %s" % (e.strerror or e)
    return None

# `T-18`. La rama «vacío» de `_motivo_ilegible` era INALCANZABLE: `leer()` sólo la
# consultaba desde su `except (OSError, UnicodeDecodeError)`, y abrir un fichero vacío no
# lanza ninguna de las dos. Vaciar el registro de decisiones daba `OK G-00` y la batería
# seguía adelante sobre sedes sin contenido. Ahora `leer()` PREGUNTA por el motivo SIEMPRE,
# y una sede vacía es una sede ilegible: falla CERRADO con su nombre.
def leer(p):
    motivo = _motivo_ilegible(p)
    if motivo:
        rel = os.path.relpath(p, RAIZ) if p.startswith(RAIZ) else p
        raise SedeIlegible("%s: %s" % (rel, motivo))
    with io.open(p, encoding="utf-8") as fh:
        return fh.read()

def lineas(p): return leer(p).split("\n")

# ── lexicón de numerales, compartido por varias comprobaciones ───────────
_PALABRA = {
    "cero": 0, "una": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12,
    "trece": 13, "catorce": 14, "quince": 15, "dieciseis": 16, "diecisiete": 17,
    "dieciocho": 18, "diecinueve": 19, "veinte": 20, "treinta": 30, "cuarenta": 40,
    "cincuenta": 50, "sesenta": 60,
}
_ACENTOS = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")

# numeral: dígitos, o una/dos palabras unidas por «y», con negritas opcionales
_NUM = r"\*{0,2}((?:[0-9]{1,3})|(?:[A-Za-zÁÉÍÓÚáéíóú]+(?:\s+y\s+[A-Za-zÁÉÍÓÚáéíóú]+)?))\*{0,2}"

def _num(txt):
    """Convierte a entero un numeral en dígitos o en letra, con decenas compuestas."""
    t = txt.translate(_ACENTOS).lower().strip()
    if t.isdigit():
        return int(t)
    partes = [w for w in re.split(r"\s+y\s+|\s+", t) if w]
    if len(partes) == 1:
        return _PALABRA.get(partes[0])
    if len(partes) == 2 and partes[0] in _PALABRA and partes[1] in _PALABRA:
        d, u = _PALABRA[partes[0]], _PALABRA[partes[1]]
        if d >= 20 and u < 10:
            return d + u
    return None

# ── Git, que FALLA CERRADO ────────────────────────────────────────────────
#
# Añadido por la corrección del GATE DE COBERTURA (`M-12`). `G-21`, `G-22` y `G-23`
# llamaban a `subprocess.run(...)` y usaban su `stdout` SIN mirar el `returncode`. Sobre
# una copia sin `.git` —un tarball, un `git archive`, la forma en que este corpus viajaría
# a un revisor externo— `git` fallaba, `stdout` venía vacío, y las tres interpretaban el
# vacío como «nada cambió»: declaraban intacto un árbol con (a) mutilada, el documento 18
# alterado y `C7` modificado.
#
# `_git()` devuelve la salida SÓLO si el comando tuvo éxito. Si falla, si no existe, o si
# el repositorio no responde, devuelve None — y las comprobaciones que dependen de él
# fallan CERRADO, con diagnóstico.
# `EE-17` · **EL ALCANCE SE DERIVA DE LA PROPIEDAD, NO DE LA REDACCIÓN DEL TÍTULO.**
# El informe publicaba qué comprobaciones exigen un repositorio CON HISTORIA filtrando sus
# TÍTULOS por la cadena «sin git». Es una convención de redacción, y caduca en cuanto
# alguien no la sigue: `G-34` empezó a usar git y no reescribió su título, con lo que el
# censo derivado daba OCHO y la medición NUEVE — que es `DD-21`, nacido de esta misma
# convención. Ahora la PROPIEDAD se declara UNA VEZ y en un sitio —qué comprobaciones
# contrastan contra la HISTORIA de git—, el ALCANCE se deriva de esa declaración, y el
# TÍTULO se CONTRASTA contra ella: si divergen en un solo identificador, es ROJO y se
# nombra. El título deja de ser el discriminante y pasa a ser lo contrastado.
_EXIGEN_HISTORIA = frozenset({"G-11", "G-11b", "G-21", "G-22", "G-23",
                              "G-28", "G-29", "G-30", "G-34"})


def _git(*args):
    try:
        r = subprocess.run(["git", "-C", RAIZ, *args],
                           capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    return r.stdout if r.returncode == 0 else None

RES = []
def check(id_, titulo, ok, detalle=""):
    RES.append((id_, titulo, bool(ok), detalle))

# ── el CENSO de comprobaciones, contrastado contra su SEDE (`T-20`) ───────
#
# `T-20`, elevado a GRAVE por el adjudicador **porque lo reprodujo**: amputó la llamada
# `check("G-31")` y obtuvo `36/36 comprobaciones en verde`, `EXIT=0`, **sin que la que
# faltaba apareciera en el informe**. Y el README lo declaraba como virtud: «*el número de
# comprobaciones no se escribe en ningún sitio*» — que es justamente lo que impedía notar
# una amputación. Un censo que sale de lo que se ejecuta y no se contrasta con nada no es
# un censo: es un recuento de lo que quedó.
#
# La SEDE contra la que se contrasta es la tabla «Qué comprueba cada una» del README, que
# es donde este directorio declara qué comprobaciones existen y de qué hallazgo sale cada
# una. El contraste es en las DOS direcciones: una comprobación publicada que no se ejecuta
# es una AMPUTACIÓN, y una que se ejecuta sin estar publicada es una comprobación SIN
# DECLARAR. Y la batería y su README entran, por fin, en un inventario: el README tiene que
# ENUMERARSE a sí mismo y enumerar la batería, y las dos tienen que estar PUBLICADAS.
#
# Esto NO cierra `M-04` y no lo pretende: quien pueda escribir el repositorio puede editar
# las dos sedes a la vez. Cierra lo que estaba abierto —que amputar una comprobación no se
# viera— y lo dice en el README.
_ID_CHECK = re.compile(r"`(G-\d+[a-z]?)`")
_README_REL = "docs/evolucion/verificacion/README.md"
_DIR_INSTRUMENTAL = "docs/evolucion/verificacion"
# La sede de la declaración de instrumental EN CORRECCIÓN es una sección del README con este
# título exacto. No hay lista escrita en la batería: quien corrige un instrumento lo declara
# donde el revisor lo lee.
_SEC_EN_CORRECCION = "## Instrumental EN CORRECCIÓN en esta tanda"


def _instrumental_en_correccion(texto):
    """Rutas que el README declara EN CORRECCIÓN. Conjunto vacío si no hay sección."""
    m = re.search(r"^%s(.*?)(?=^## |\Z)" % re.escape(_SEC_EN_CORRECCION),
                  texto, re.S | re.M)
    if not m:
        return set()
    return set(re.findall(r"`(%s/[A-Za-z0-9_.-]+)`" % re.escape(_DIR_INSTRUMENTAL),
                          m.group(1)))


def _declarado_en_correccion(texto):
    """TODA ruta que el README declara EN CORRECCIÓN, no sólo la del instrumental.

    `S1-02`. La guarda de mutación necesita una sede donde una tanda declare qué rutas
    GOBERNADAS está tocando fuera de su objeto documental. Es la MISMA sede que ya existe
    para el instrumental, con el mismo comportamiento: **caduca sola**, porque declarar una
    ruta idéntica a `HEAD` es también ROJO. No se crea una segunda sede.
    """
    m = re.search(r"^%s(.*?)(?=^## |\Z)" % re.escape(_SEC_EN_CORRECCION),
                  texto, re.S | re.M)
    if not m:
        return set()
    return set(re.findall(r"`((?:docs|kernel|tooling|packs)/[A-Za-z0-9_./-]+"
                          r"|[A-Za-z0-9_.-]+\.(?:md|py|sh|toml|yaml|yml))`", m.group(1)))

def _censo_de_comprobaciones(ejecutadas):
    """Fallos del censo de comprobaciones contra su sede. Lista vacía si cuadra."""
    fallos = []
    try:
        texto = leer(os.path.join(RAIZ, _README_REL))
    except SedeIlegible as e:
        return [f"la sede del censo no se puede leer ({e}): sin ella el número de "
                f"comprobaciones no se contrasta con nada, y amputar una `check()` vuelve "
                f"a imprimir «N/N en verde» sin que la que falta aparezca"]
    m = re.search(r"^## Qué comprueba cada una(.*?)(?=^## |\Z)", texto, re.S | re.M)
    if not m:
        return ["el README no publica su tabla «Qué comprueba cada una», que es la sede "
                "donde este directorio declara qué comprobaciones existen"]
    publicadas = []
    for linea in m.group(1).split("\n"):
        if not linea.startswith("|"):
            continue
        for i in _ID_CHECK.findall(linea.strip("|").split("|")[0]):
            if i not in publicadas:
                publicadas.append(i)
    if not publicadas:
        return ["la tabla del README no publica ni un identificador `G-nn`: un censo "
                "vacío no puede detectar ninguna amputación"]
    amputadas = [i for i in publicadas if i not in ejecutadas]
    sin_declarar = [i for i in ejecutadas if i not in publicadas]
    if amputadas:
        fallos.append(f"COMPROBACIONES AMPUTADAS: el README publica {amputadas} y esta "
                      f"ejecución NO las ha ejecutado. Quien borre una llamada `check()` "
                      f"responde de ello: el informe ya no puede callar la que falta")
    if sin_declarar:
        fallos.append(f"COMPROBACIONES SIN DECLARAR: se ejecutan {sin_declarar} y el README "
                      f"no las publica. Una comprobación que nadie declara no la puede "
                      f"refutar nadie")
    repetidas = sorted({i for i in ejecutadas if ejecutadas.count(i) > 1})
    if repetidas:
        fallos.append(f"identificadores de comprobación REPETIDOS: {repetidas}")
    # ── el INVENTARIO DE INTEGRIDAD del instrumental ─────────────────────────────
    #
    # `X-01` / `A5` / `A6`, y es el punto 3 del remedio que el adjudicador `X` deja
    # determinado: «el emisor y el derivador entran en el inventario de integridad».
    # El inventario cubría DOS ficheros —esta batería y su README— y sólo en dos
    # dimensiones: enumerado y publicado. Fuera quedaban `emitir-sobre-de-ancla.py` y
    # `derivar-universo-obligatorio.py`, **que son los que producen el ANCLA**: `G-22` cubre
    # documentos numerados y manifiestos, `G-34` cubría la batería y su README, `G-29` cubre
    # topología y duplicados, y ninguno cubría `verificacion/*.py`. Con eso `X` puso tres
    # líneas de puerta trasera en el emisor —SIN COMMITEAR— y obtuvo un sobre idéntico al
    # honesto sobre un corpus corrupto, con la batería en 38/38; y una puerta trasera en el
    # derivador que devolvía `{}` en `universos_publicados()` desarmaba el cliquet entero,
    # también en 38/38.
    #
    # Esto NO es una comprobación nueva: es el mismo inventario, con el mismo id, en la
    # misma sede —el README—, con el perímetro DERIVADO del directorio en vez de escrito, y
    # con una tercera dimensión: **IDÉNTICO A `HEAD`, o DECLARADO EN CORRECCIÓN**.
    #
    # La declaración se lee del README y **caduca sola**: declarar en corrección un fichero
    # que YA coincide con `HEAD` es rojo. Una exención que sobrevive a la tanda que la
    # justificaba es una puerta abierta, y ésa es la clase de defecto que este corpus lleva
    # cuatro gates persiguiendo.
    rel_bat = os.path.relpath(os.path.abspath(__file__), RAIZ).replace(os.sep, "/")
    _dir_inst = os.path.join(RAIZ, _DIR_INSTRUMENTAL)
    try:
        # `Z1-07`. Aquí decía `and not n.startswith(".")`: el inventario de integridad del
        # instrumental que produce el ANCLA **se saltaba todo fichero cuyo nombre empezara
        # por punto**, sin motivo escrito y sin que nada lo dijera. Un
        # `.emitir-sobre-de-ancla.py` vivía en el directorio, fuera del inventario, fuera
        # del README y fuera del contraste contra `HEAD`. Se excluye por lo mismo que en el
        # resto de la batería —`_EXCLUIDO`: bytecode y `.git`— y por nada más.
        inventario = sorted(_DIR_INSTRUMENTAL + "/" + n for n in os.listdir(_dir_inst)
                            if os.path.isfile(os.path.join(_dir_inst, n))
                            and _en_zona(_DIR_INSTRUMENTAL + "/" + n))
    except OSError as e:
        return fallos + [f"no se puede derivar el inventario de `{_DIR_INSTRUMENTAL}` "
                         f"({e.strerror}): sin inventario no hay integridad que comprobar"]
    for f in (rel_bat, _README_REL):
        if f not in inventario:
            fallos.append(f"{f} no sale del barrido de `{_DIR_INSTRUMENTAL}`: el inventario "
                          f"no ve ni los dos ficheros que ya cubría, y un inventario que no "
                          f"se ve a sí mismo no cubre nada")
    for f in inventario:
        if "`%s`" % f not in texto:
            fallos.append(f"{f} no está ENUMERADO en el README, que es el inventario de "
                          f"este instrumental: un fichero que no está en ningún inventario "
                          f"no lo echa de menos nadie")
    try:
        publicados, modificados = _head_arbol, _mod_head
    except NameError:
        publicados, modificados = None, None
    if publicados is None:
        fallos.append("GIT NO RESPONDE: el instrumental no se puede contrastar con su "
                      "versión publicada, y un instrumento sin contraste es el que `X-01` "
                      "modificó sin que nadie lo viera")
    else:
        declarados = _instrumental_en_correccion(texto)
        for f in inventario:
            if f not in publicados:
                fallos.append(f"{f} NO está publicado en `HEAD`: un instrumento sin versión "
                              f"publicada no se puede contrastar con nada")
                continue
            if f in modificados and f not in declarados:
                fallos.append(
                    f"{f}: MODIFICADO respecto de `HEAD` y NO DECLARADO en corrección. "
                    f"Éste es el inventario de integridad del instrumental que produce el "
                    f"ANCLA, y una modificación que nadie declara es exactamente la puerta "
                    f"de `X-01`: tres líneas sin commitear bastaban para emitir un sobre "
                    f"idéntico al honesto sobre un corpus corrupto")
        for f in sorted(declarados - set(inventario)):
            fallos.append(f"{f}: DECLARADO en corrección en el README y no existe en "
                          f"`{_DIR_INSTRUMENTAL}`")
        for f in sorted(declarados & set(inventario)):
            if f in publicados and f not in modificados:
                fallos.append(
                    f"{f}: DECLARADO en corrección y sin embargo IDÉNTICO a `HEAD`. La "
                    f"declaración ha caducado: se retira del README en el mismo commit que "
                    f"confirma el cambio. Una exención que sobrevive a la tanda que la "
                    f"justificaba es una puerta abierta")
    return fallos

# ── el INFORME se emite SIEMPRE, también si la batería aborta (`Q-24`) ────
#
# El informe vivía al final del fichero, en código de nivel superior: cualquier excepción
# entre la primera comprobación y él se llevaba por delante las comprobaciones ya hechas.
# Aquí se registra un emisor con `atexit` y se captura la excepción con `sys.excepthook`,
# de modo que el fallo se convierte en una comprobación ROJA —`G-00`— con el fichero y el
# motivo NOMBRADOS, y el informe sale igual. **Falla CERRADO: código 2 y diagnóstico.**
_ABORTO = []
_EMITIDO = []

def _informe(codigo_normal=None):
    if _EMITIDO:
        return 0
    _EMITIDO.append(True)
    if _ABORTO:
        RES.insert(0, ("G-00", "la batería COMPLETA su ejecución y emite informe", False,
                       _ABORTO[0]))
    else:
        # `S1-01`. `G-00` deja de significar sólo «no hubo excepción» y pasa a significar
        # «la batería pudo LEER lo que tenía que leer». Una lista de rutas truncada, mal
        # decodificada o citada por `core.quotePath` es un universo encogido en silencio, y
        # antes no lo denunciaba nadie: la comprobación NOMBRABA el fichero en su detalle y
        # seguía imprimiendo verde. Aquí se juntan las dos mitades del remedio: la lectura
        # única falla cerrado, y el BARRIDO comprueba que no haya quedado otra vía.
        # `S1-06`. El desajuste del ALCANCE se IMPRIMÍA y el comentario de `EE-17` decía
        # «es ROJO»: una afirmación falsa del instrumento sobre sí mismo, en el remedio que
        # `EE-17` acababa de escribir. Ahora **es rojo de verdad**, y sin añadir ninguna
        # comprobación al censo: entra en `G-00`, que ya es la fila de «la batería pudo
        # hacer su trabajo». Un alcance que no cuadra con lo que se ejecuta no es fiable, y
        # publicarlo como si lo fuera es la sexta condición de `O18`.
        _lect = list(_LECTURAS_ROTAS) + _lecturas_seguras()
        RES.insert(0, ("G-00", "la batería COMPLETA su ejecución, LEE sin ambigüedad toda "
                               "lista de rutas de git, y emite informe",
                       not _lect,
                       "; ".join(_lect) or
                       "ninguna sede tumbó la ejecución · todas las listas de rutas se leen "
                       "por `NUL` con `core.quotePath=false`, decodificación estricta y "
                       "control de truncamiento, y el barrido no encuentra ninguna lectura "
                       "partida por blancos (`S1-01`)"))
    if _ABORTO:
        RES.append(("G-34", "el CENSO de comprobaciones cuadra con su sede, y amputar una "
                            "da ROJO (falla CERRADO sin git)", False,
                    "la ejecución abortó antes de terminar: el censo no se puede contrastar "
                    "sobre una corrida incompleta, y darlo por bueno sería el verde por "
                    "omisión que `G-00` acaba de denunciar"))
    else:
        # `G-34` se cuenta a sí misma: se emite siempre y está publicada como las demás
        _censo = _censo_de_comprobaciones([r[0] for r in RES] + ["G-34"])
        RES.append(("G-34", "el CENSO de comprobaciones cuadra con su sede, y amputar una "
                            "da ROJO (falla CERRADO sin git)", not _censo,
                    "; ".join(_censo) or
                    "%d comprobaciones ejecutadas y las mismas %d publicadas en el "
                    "README, una a una; la batería y su README, enumerados y publicados"
                    % (len(RES) + 1, len(RES) + 1)))
    # `S1-06`. El desajuste del ALCANCE se calcula **con `G-34` ya en la lista**, y se
    # PLIEGA sobre la fila de `G-00`, que es la que dice si la batería pudo hacer su
    # trabajo. Antes se IMPRIMÍA mientras el comentario de `EE-17` decía «es ROJO»: una
    # afirmación falsa del instrumento sobre sí mismo, dentro del remedio que la escribía.
    # Ahora es ROJO de verdad y **sin añadir ninguna comprobación al censo**.
    _ids_g0 = {i for i, _, _, _ in RES}
    _titulan_g0 = {i for i, t, _, _ in RES if "sin git" in t}
    _desaj_g0 = sorted((_titulan_g0 ^ (_EXIGEN_HISTORIA & _ids_g0))
                       | (_EXIGEN_HISTORIA - _ids_g0))
    if _desaj_g0 and RES and RES[0][0] == "G-00":
        _id0, _t0, _ok0, _d0 = RES[0]
        RES[0] = (_id0, _t0, False,
                  (_d0 + "; " if not _ok0 else "") +
                  f"ALCANCE DESAJUSTADO (`EE-17`/`S1-06`): {_desaj_g0} — el TÍTULO de una "
                  f"comprobación y la PROPIEDAD declarada en `_EXIGEN_HISTORIA` no "
                  f"coinciden, o se declara una comprobación que no se ejecuta. El alcance "
                  f"que el informe publica no es fiable hasta que cuadren")
    print("BATERÍA MECÁNICA DE LA CORRECCIÓN DEL GATE DE CIERRE\n")
    for id_, t, ok, det in RES:
        print(f"{'OK  ' if ok else 'FALLO'} {id_:7s} {t}")
        if det: print(f"{'':13s}└─ {det}")
    verde = sum(1 for _, _, ok, _ in RES if ok)
    # `DD-21` · **QUÉ CERTIFICA ESTE «N/N», Y QUÉ NO.** Nueve de las comprobaciones no son
    # propiedades del COMMIT sino de **un repositorio CON HISTORIA**: contrastan contra
    # `HEAD` y contra la revisión base con `git`. Sobre la materialización que la RECETA
    # del sobre prescribe —árbol desplegado SIN `.git`— esas nueve fallan CERRADO, que es
    # lo correcto, y la batería da menos que su total. **No es un defecto: era que ninguna
    # sede lo acotaba**, y quien leyera «N/N en verde» podía creer que certificaba el
    # commit desnudo.
    #
    # `EE-17`. El censo se derivaba de los TÍTULOS —`"sin git" in t`—, que es una
    # convención de redacción y no una propiedad: `G-34` empezó a usar git sin reescribir
    # su título y el censo dio OCHO donde la medición daba NUEVE. Hoy sale de
    # `_EXIGEN_HISTORIA`, que declara la propiedad, y el TÍTULO se contrasta contra ella.
    _ids = [i for i, _, _, _ in RES]
    _con_git = [i for i in _ids if i in _EXIGEN_HISTORIA]
    _titulan = {i for i, t, _, _ in RES if "sin git" in t}
    _desajuste = sorted(_titulan ^ set(_con_git)) + sorted(_EXIGEN_HISTORIA - set(_ids))
    print(f"\n{verde}/{len(RES)} comprobaciones en verde")
    print(f"ALCANCE (`DD-21`): {len(_con_git)} de las {len(RES)} exigen un repositorio CON "
          f"HISTORIA y fallan CERRADO sin `.git` — {', '.join(_con_git)}. "
          f"Las otras {len(RES) - len(_con_git)} son propiedades del ÁRBOL DESNUDO. "
          f"Un «{len(RES)}/{len(RES)}» certifica el commit CON su historia; sobre la "
          f"materialización sin `.git` que prescribe la receta del sobre, el máximo "
          f"alcanzable es {len(RES) - len(_con_git)}.")
    if _ABORTO:
        return 2
    return 0 if verde == len(RES) else 1

def _hook(tipo, valor, tb):
    if issubclass(tipo, SedeIlegible):
        _ABORTO.append("SEDE ILEGIBLE, y la batería no puede comprobar lo que no puede "
                       "leer → %s" % valor)
    else:
        ultimo = traceback.extract_tb(tb)[-1] if tb else None
        donde = f" (batería L{ultimo.lineno})" if ultimo else ""
        _ABORTO.append(f"ABORTO NO PREVISTO{donde}: {tipo.__name__}: {valor}")

sys.excepthook = _hook

@atexit.register
def _salida_de_emergencia():
    if not _EMITIDO:
        codigo = _informe()
        sys.stdout.flush()      # `os._exit` no vacía los búferes: sin esto el informe
        sys.stderr.flush()      # de una corrida abortada se perdería, que es el defecto
        os._exit(codigo)        # que esta salida existe para no repetir

# ── secciones de 11, para localizar cada linea ────────────────────────────
def secciones(ls):
    out = []
    for i, l in enumerate(ls, 1):
        m = re.match(r'^#{1,4} (?:§)?([0-9]+(?:\.[0-9]+)*) ·', l)
        if m: out.append((i, m.group(1)))
    return out
L11 = lineas(D11); S11 = secciones(L11)
def sec_de(n):
    cur = "?"
    for i, name in S11:
        if i <= n: cur = name
        else: break
    return cur

t11 = leer(D11)

# Los MACROCIRCUITOS se derivan de las secciones §8.x —§8.0 es el encuadre y no es un
# recorrido—, y se derivan AQUÍ, una sola vez, porque los usan `G-25` y `G-33`. Escribir
# `("8.1","8.2","8.3","8.4")` en cada sitio es el censo a mano que la batería persigue: el
# día que naciera un quinto recorrido, las dos comprobaciones seguirían verdes sobre un mapa
# que ya no es el suyo.
_MACROS = sorted({s for _, s in S11 if re.match(r"^8\.[1-9]\d*$", s)},
                 key=lambda s: [int(x) for x in s.split(".")])

# ── POLARIDAD SEMÁNTICA, compartida ──────────────────────────────────────
#
# Protección 4 del adjudicador, y su generalización, la 10. La versión anterior de `G-01`
# eximía un párrafo entero si contenía la palabra «RETIRADA» **en cualquier posición**, sin
# polaridad y sin sujeto. El adjudicador insertó en §16 un párrafo que **DEROGA** la
# retirada —«*esa ruta es CANONICA y fuente de verdad … La nota que hablaba de una RETIRADA
# queda SIN EFECTO*»— y `G-01` imprimió `OK` sobre el texto que reinstalaba lo que la
# comprobación existe para prohibir. **Encontrar la palabra «RETIRADA» no demuestra que una
# regla esté retirada.**
#
# Aquí la polaridad se decide con TRES piezas, y ninguna es una palabra suelta:
#
#   1 · un predicado de RETIRADA atribuido al objeto,
#   2 · un VETO: cualquier predicado que REINSTALE el objeto —que lo declare canónico,
#       vigente o fuente de verdad, o que deje sin efecto su retirada— **manda sobre el
#       anterior**. Un texto que dice las dos cosas afirma la viva,
#   3 · el ANCLA en la SEDE CANÓNICA: el registro de decisiones tiene que declarar la
#       retirada. Si esa sede se mueve, esto se pone en rojo aunque el documento 11 no se
#       toque, y ninguna redacción del documento 11 puede sustituirla.
#
# Y la ausencia de las dos primeras no es silencio favorable: un párrafo que no se
# pronuncia es INDETERMINADO, y un indeterminado **falla**.
_REINSTALA = (
    r"\b(?:esa|esta|la|dicha)\s+ruta\b[^.\n]{0,70}?\b(?:es|son|sigue siendo|queda|"
    r"vuelve a ser)\b[^.\n]{0,50}?\b(?:CAN[ÓO]NICA|can[óo]nica|VIGENTE|vigente|"
    r"fuente de verdad)\b",
    r"\bqueda\s+SIN\s+EFECTO\b",
    r"\bREINSTAURAD[AO]\b|\bse\s+reinstaura\b|\bse\s+reinstala\b",
    r"\bNORMA\s+VIGENTE\b",
    r"\bderoga\b[^.\n]{0,60}\bretirada\b",
)
_RETIRA = (
    r"\bRETIRAD[AO]\b",
    r"\bse\s+retira\b|\bqueda\s+retirad[ao]\b",
    r"\bsustituid[ao]\s+por\b",
    r"\bse resuelve sin crear una tercera fuente\b",
)

def _polaridad(texto):
    """`VIGENTE` · `RETIRADO` · `INDETERMINADO`, en ese orden de precedencia.

    El VETO manda: si el texto reinstala el objeto, da igual cuántas veces diga
    «RETIRADA». Es lo que impide que una palabra suelta desactive la comprobación.

    Y el veto se aplica al PREDICADO, no a la frase: «la ruta queda RETIRADA de la
    arquitectura vigente» empareja «ruta … queda … vigente» y **no** es una reinstalación,
    porque el predicado que la une es la retirada. Se comprueba sobre el tramo emparejado.
    """
    for p in _REINSTALA:
        for m in re.finditer(p, texto):
            if not re.search(r"RETIRAD[AO]|retirad[ao]|sustituid[ao]", m.group(0)):
                return "VIGENTE"
    if any(re.search(p, texto, re.I) for p in _RETIRA):
        return "RETIRADO"
    return "INDETERMINADO"

# ── G-01 · cero `estado/cuarentena/` VIGENTE, por POLARIDAD ──────────────
parrafos11 = re.split(r"\n\s*\n", t11)
_g01, _pol = [], Counter()
for par in parrafos11:
    if "estado/cuarentena" not in par:
        continue
    p = _polaridad(par)
    _pol[p] += 1
    if p == "VIGENTE":
        _g01.append(f"un párrafo REINSTALA `estado/cuarentena/` en vez de retirarla: "
                    f"«{' '.join(par.split())[:110]}…»")
    elif p == "INDETERMINADO":
        _g01.append(f"un párrafo menciona `estado/cuarentena/` y NO se pronuncia sobre su "
                    f"retirada; el silencio no es una retirada: "
                    f"«{' '.join(par.split())[:110]}…»")
# ancla en la SEDE CANÓNICA: el registro de decisiones, no el documento 11
_tdec = leer(DEC)
_fila87 = [l for l in _tdec.split("\n") if re.match(r"^\| `?D87`? \|", l)]
if not _fila87:
    _g01.append("la sede canónica de la retirada —la fila `D87` del registro— no aparece: "
                "sin ella el documento 11 no puede acreditar nada por sí solo")
elif _polaridad(_fila87[0]) != "RETIRADO":
    _g01.append(f"la fila `D87` del registro NO declara la retirada: la polaridad de la "
                f"sede canónica es {_polaridad(_fila87[0])}")
elif ".ads/run/quarantine" not in _fila87[0]:
    _g01.append("`D87` retira `estado/cuarentena/` y no nombra la ruta que la sustituye: "
                "una retirada sin destino deja el plano sin sede")
n_menc = sum(1 for l in L11 if "estado/cuarentena" in l)
check("G-01", "cero `estado/cuarentena/` VIGENTE: cada mención se juzga por POLARIDAD y la sede canónica la ancla",
      not _g01,
      f"{n_menc} menciones en {sum(_pol.values())} párrafos, todos con polaridad RETIRADO, "
      f"y `D87` lo ancla en el registro" if not _g01 else "; ".join(_g01))

# ── G-02 · `.ads/run/quarantine/` clasificado y con ciclo ────────────────
q = "`.ads/run/quarantine/"
faltan = []
if q not in t11: faltan.append("no aparece")
# clasificado en §2.4
s24 = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "2.4")
if "quarantine" not in s24: faltan.append("no clasificado en §2.4")
if "OPERACIONAL" not in s24: faltan.append("§2.4 sin plano operacional")
# listado en §2.3
s23 = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "2.3")
if "quarantine" not in s23: faltan.append("no listado en §2.3")
# ciclo: crea antes de restaurar / verifica por hash / elimina despues del commit
s269 = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "2.6.9")
for frase, etq in [("ANTES de restaurar", "crear antes de restaurar"),
                   ("POR HASH", "verificar por hash"),
                   ("commit del incidente", "eliminar tras el commit")]:
    if frase not in s269: faltan.append("§2.6.9 sin " + etq)
# no canonica y no fuente de verdad
if "NO CANÓNICA" not in s269 and "no canónica" not in s269.lower(): faltan.append("sin declarar no canonica")
if "NO es fuente de verdad" not in s269: faltan.append("sin declarar que no es fuente de verdad")
if "SEG" not in s269: faltan.append("sin el bloqueo de SEG")
check("G-02", "`.ads/run/quarantine/` clasificado, con ciclo y sin ser fuente de verdad",
      not faltan, "; ".join(faltan) or "plano, arbol, ciclo, hash, SEG y perdida aceptada")

# ── G-03 · `estado/deriva/` con las siete piezas ────────────────────────
piezas = {
  "arbol §2.3":        "deriva/<ID>.abierta" in s23,
  "excepcion §2.4":    "estado/deriva" in s24,
  "ignore en positivo": bool(re.search(r"NADA de `estado/deriva/`", t11)),
  "reconstruccion §2.9": bool(re.search(r"\| el marcador `estado/deriva/<ID>\.abierta` \|", t11)),
  "creacion paso E":   "crear su marcador `estado/deriva/<ID>.abierta`" in t11,
  "retirada":          "se retira\n                   `estado/deriva/<ID>.abierta`" in t11
                        or "**se retira\n" in t11 or "retira\n                   `estado/deriva" in t11
                        or "lo RETIRA la transacción CERRADA" in t11,
  "prueba adversarial": "`X59`" in t11 and "`X60`" in t11,
}
check("G-03", "`estado/deriva/` en arbol, excepcion, ignore, reconstruccion, creacion, retirada y prueba",
      all(piezas.values()), ", ".join(k for k, v in piezas.items() if not v) or "las siete")

# ── G-04 · predicado `abierta(tx)` unico: ninguna sede lo redeclara ──────
redecl = []
for i, l in enumerate(L11, 1):
    if sec_de(i) == "2.6.1": continue
    if re.search(r"durable y SIN `derivada`", l) or re.search(r"`preparada` durable y SIN `derivada`", l):
        redecl.append(i)
citas = sorted({sec_de(i) for i, l in enumerate(L11, 1)
                if "abierta(tx)" in l and sec_de(i) not in ("2.6.1", "15.8")})
check("G-04", "predicado `abierta(tx)` UNICO: ninguna sede vigente lo redeclara",
      not redecl, f"sedes que lo citan y remiten: {citas}" if not redecl else f"redeclaran: {redecl}")

# ── G-05 · cero reglas de intentos/agotado en la capa B ────────────────
i_capaB = t11.index("#### B · Qué comprueba el VALIDADOR SEMÁNTICO DEL DIARIO")
i_capaC = t11.index("#### C · Qué garantizan o DEMUESTRAN el RUNTIME")
capaB = t11[i_capaB:i_capaC]
malas = []
if re.search(r"#observaciones = #intentos", capaB) and "Corregido por el gate" not in capaB:
    malas.append("#observaciones = #intentos")
if re.search(r"exactamente un `derivada` por transacción cerrada", capaB) and "decía «exactamente un" not in capaB:
    malas.append("terminalidad sobre `derivada`")
# ninguna regla VIGENTE (fuera de la nota de correccion) puede llevarlas
vigentes = [l for l in capaB.split("\n")
            if l.startswith("· ") and ("agotado: true" in l or "#intentos" in l)]
check("G-05", "cero reglas de `#intentos` / `agotado` VIGENTES en la capa B",
      not malas and not vigentes, "; ".join(malas + vigentes) or "sólo quedan en la nota de retirada")

# ── G-06 · DOS terminales, en la capa B y en el automata ───────────────
dos = ("`derivada` **o** `abandonada`" in capaB
       or "es `derivada` o\n  `abandonada`" in capaB
       or re.search(r"exactamente UN terminal, y es `derivada`", capaB))
check("G-06", "la capa B declara DOS terminales, no uno", bool(dos),
      "terminalidad reescrita sobre los dos" if dos else "no encontrado")

# ── G-07 · cero atribuciones «PLT para cada source change» ─────────────
mal = []
for i, l in enumerate(L11, 1):
    if re.search(r"`PLT`[^|\n]{0,80}cada source change", l) and "Corregido" not in l and not l.lstrip().startswith(">"):
        mal.append(i)
check("G-07", "cero atribuciones «`PLT` para cada source change» vigentes",
      not mal, "" if not mal else f"lineas {mal}")

# ── G-08 · las sedes de §8 y §18 usan C7 correctamente ────────────────
#
# `T-17`. Aquí vivía `sedes = {"§8.0": None, …}`: un diccionario que se ASIGNABA y que **no
# leía nadie**, y que además OMITÍA `§8.3` mientras el título prometía «las SEIS sedes».
# Era código muerto de la clase `M-11`/`Q-15`/`Q-22` que esta tanda declara purgada, y el
# hueco de `§8.3` en él habría pasado por bueno el día que alguien lo hubiera puesto a
# funcionar. Las sedes se DERIVAN ahora de §8 —todas sus subsecciones, encuadre incluido—
# más §18, se usan para construir los bloques, y el cardinal del título se deriva de ellas.
# `§8` a secas es el encabezado de encuadre del capítulo y no tiene cuerpo propio: las
# sedes son sus SUBSECCIONES —`§8.0` incluida, que sí es texto— más `§18`.
_SEDES_C7 = tuple(sorted({s for _, s in S11 if re.match(r"^8\.\d+$", s)},
                         key=lambda s: [int(x) for x in s.split(".")])) + ("18",)
bloques = {"§" + s: "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == s)
           for s in _SEDES_C7}
faltan = []
if len(_SEDES_C7) < 2:
    faltan.append("cero sedes de §8 derivadas del documento 11: sin objeto, esta "
                  "comprobación sería un verde por omisión")
for nombre in ("§" + s for s in _SEDES_C7):
    b = bloques[nombre]
    if not b.strip():
        faltan.append(f"{nombre} se deriva VACÍA: no hay texto que citara `C7`")
        continue
    if "C7:82" not in b: faltan.append(f"{nombre} sin `C7:82` (PLT materializa)")
    if nombre != "§18" and "C7:83" not in b: faltan.append(f"{nombre} sin `C7:83`-`C7:86` (custodia)")
    if "C7:88" not in b: faltan.append(f"{nombre} sin `C7:88`-`C7:89` (ENT convergencia)")
check("G-08", "las sedes DERIVADAS de §8 y §18 citan `C7` operacion a operacion",
      not faltan,
      "; ".join(faltan) or "%d sedes derivadas: %s" % (
          len(_SEDES_C7), " ".join("§" + s for s in _SEDES_C7)))

# ── G-09 · INS-5 completo en §18 ──────────────────────────────────────
s18 = bloques["§18"]
need = ["INS-5` BASELINE APROBADO POR EL OWNER", "CLASIFICACIÓN DE DESCONOCIDOS CRÍTICOS",
        "BASELINE de producto, dominio y diseño de `INS-5`", "TRES condiciones y el productor de cada una"]
falta = [x for x in need if x not in s18]
check("G-09", "§18 lleva el gate de `INS-5`, su salida y los tres productores de `O12`",
      not falta, "; ".join(falta) or "gate, salida y productores")

# ── G-10 · las extensiones de ficha, DERIVADAS y contrastadas en tres sedes ───
#
# `DD-12` · **ESTA COMPROBACIÓN NO DERIVABA NADA, y era el aval con el que §0 se permite
# escribir uno de los pocos cardinales que el documento se permite.** Comprobaba TRES
# substrings literales —«Son SEIS», «las SEIS extensiones», «`+6` extensiones»— y SEIS
# nombres escritos a mano en esta misma línea. Una SÉPTIMA extensión añadida a la
# enumeración de §5.2 dejaba «Son SEIS» caducado **con `G-10` en verde**, que es exactamente
# el modo de fallo que la regla de titulares de §0 persigue — y §0 nombra a `G-10` como su
# excepción. El guardián no guardaba.
#
# **Ahora el censo se DERIVA de la enumeración de §5.2** —las fichas que el bloque «QUÉ
# TRABAJO GENERA» nombra, `capacidades/<CAP>/`— y de ahí sale TODO: el cardinal en letra,
# el cardinal en cifra y la lista de nombres que las tres sedes tienen que publicar. Nada
# se escribe aquí: añadir una séptima ficha a §5.2 pone en ROJO las tres sedes que sigan
# diciendo SEIS.
_CARD_LETRA = {1: "UNA", 2: "DOS", 3: "TRES", 4: "CUATRO", 5: "CINCO", 6: "SEIS",
               7: "SIETE", 8: "OCHO", 9: "NUEVE", 10: "DIEZ", 11: "ONCE", 12: "DOCE"}
_i52 = t11.find("QUÉ TRABAJO GENERA")
_b52 = t11[_i52:t11.find("\n```", _i52)] if _i52 >= 0 else ""
_EXT_FICHA = []
for _c in re.findall(r"`capacidades/([A-Z]{3})/`", _b52):
    if _c not in _EXT_FICHA:
        _EXT_FICHA.append(_c)
falta = []
if _i52 < 0 or not _EXT_FICHA:
    falta.append("§5.2 no publica la ENUMERACIÓN `capacidades/<CAP>/` de las extensiones de "
                 "ficha bajo «QUÉ TRABAJO GENERA»: sin enumeración no hay censo que derivar, "
                 "y el cardinal de las tres sedes no se contrasta contra nada")
else:
    _n = len(_EXT_FICHA)
    _letra = _CARD_LETRA.get(_n)
    if not _letra:
        falta.append(f"el censo derivado de §5.2 da {_n} y esta comprobación no sabe "
                     f"escribirlo en letra: se amplía `_CARD_LETRA` antes de seguir")
    else:
        # §5.2 · el cardinal en letra, junto a su enumeración, en cualquier plegado
        if not re.search(r"\*\*Son\s+" + _letra + r"\*\*|Son\s+\**\s*" + _letra,
                         _b52.replace("\n", " ")):
            falta.append(f"§5.2: su enumeración da {_n} fichas ({', '.join(_EXT_FICHA)}) y "
                         f"su titular no dice «Son {_letra}»")
        # §16 · el cardinal en letra Y los nombres
        _i16 = t11.find("extensiones de ficha de §5.2 —")
        _b16 = t11[max(0, _i16 - 300):_i16 + 400] if _i16 >= 0 else ""
        if _i16 < 0:
            falta.append("§16 no publica la sede de las extensiones de ficha")
        else:
            if _letra not in _b16.replace("\n> ", " ").replace("\n", " "):
                falta.append(f"§16: no dice «{_letra}» sobre un censo derivado de {_n}")
            falta += [f"§16: no nombra `{c}`" for c in _EXT_FICHA if f"`{c}`" not in _b16]
        # §17 · el cardinal en CIFRA Y los nombres
        _i17 = t11.find("extensiones de ficha**: `")
        if _i17 < 0:
            falta.append("§17 no publica la fila `+N extensiones de ficha` con sus nombres")
        else:
            _fila17 = t11[t11.rfind("\n", 0, _i17) + 1:t11.find("\n", _i17)]
            _m17 = re.search(r"\+(\d+)`? extensiones de ficha", _fila17)
            if not _m17:
                falta.append("§17: su fila no publica el cardinal en la forma `+N`")
            elif int(_m17.group(1)) != _n:
                falta.append(f"§17: escribe `+{_m17.group(1)}` y el censo derivado de §5.2 "
                             f"da {_n}")
            falta += [f"§17: no nombra `{c}`" for c in _EXT_FICHA if f"`{c}`" not in _fila17]
check("G-10",
      "las extensiones de ficha se DERIVAN de la enumeración de §5.2, y su cardinal y sus nombres se contrastan en §5.2, §16 y §17",
      not falta, "; ".join(falta) or
      f"censo DERIVADO de §5.2: {len(_EXT_FICHA)} extensiones ({', '.join(_EXT_FICHA)}), "
      f"y las tres sedes publican ese cardinal y esos nombres. Ninguno escrito aquí "
      f"(`DD-12`)")

# ── G-11 · D67 identica byte a byte a la de 7e99388 ───────────────────
_base_raw = _git("show", "7e99388:docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md")
base = _base_raw.split("\n") if _base_raw is not None else []
o = [l for l in base if l.startswith("| D67 |")]
a = [l for l in lineas(DEC) if l.startswith("| D67 |")]
check("G-11", "la fila `D67` es identica BYTE A BYTE a la de `7e99388` (falla CERRADO sin git)",
      _base_raw is not None and len(o) == 1 and len(a) == 1 and o[0] == a[0],
      "identica" if o and a and o[0] == a[0] else "DIFIERE")

# ── G-11b · D1-D86 intactas salvo D67 ────────────────────────────────
#
# FALLA CERRADO desde `Q-01`. Era la ÚNICA comprobación dependiente de Git que no lo hacía:
# sin `.git`, `_base_raw` es `None`, `base` queda vacía, el bucle no encuentra ni una fila
# con la que comparar y `difs` sale vacío — con lo que declaraba «ninguna difiere» sobre
# OCHENTA Y SEIS filas que no había mirado. Es el defecto que `M-12` cerró en `G-21`, `G-22`
# y `G-23`, sobreviviendo en la de mayor alcance de las cuatro.
#
# `A1` del documento 24, y es la MISMA guarda en las DOS comprobaciones que contrastan
# filas del registro contra la base: `if ob and ac and ob[0] != ac[0]` **no compara lo que
# no está**. Borrar una fila entera la hacía invisible, y el informe imprimía «ninguna
# difiere». El contraste se deriva una sola vez, aquí, y lo usan `G-11b` y `G-21`: una fila
# que estaba en la base y ya no está es una DESAPARICIÓN, y se nombra.
def _filas_contra_base(ids, letra):
    """Filas `| <letra><n> |` de la base que ya no están, están duplicadas o han cambiado."""
    salida, vigentes = [], lineas(DEC)
    for n in ids:
        ob = [l for l in base if l.startswith(f"| {letra}{n} |")]
        ac = [l for l in vigentes if l.startswith(f"| {letra}{n} |")]
        if not ob:
            continue                       # no estaba en la base: no hay nada que conservar
        if not ac:
            salida.append(f"{letra}{n}: DESAPARECIDA — estaba en `7e99388` y ya no está en "
                          f"el registro vigente. Una fila borrada no «difiere»: deja de "
                          f"existir, y eso es lo que la guarda no miraba")
        elif len(ac) > 1:
            salida.append(f"{letra}{n}: DUPLICADA {len(ac)} veces en el registro vigente")
        elif ob[0] != ac[0]:
            salida.append(f"{letra}{n}: DIFIERE de la de `7e99388`")
    return salida

difs = _filas_contra_base(range(1, 87), "D")
if _base_raw is None:
    difs.append("GIT NO RESPONDE: no se puede comparar contra `7e99388`")
elif not _base_raw.strip():
    # `Q-22`. La guarda decía `elif not base:` y `base` es `_base_raw.split("\n")`, de modo
    # que sobre una salida vacía valía `['']`, que es VERDADERO. La guarda no podía disparar
    # jamás: es la misma clase de código muerto que `M-11` y `Q-15`. Se mira el texto crudo.
    difs.append("la base de `7e99388` viene VACÍA: no hay nada contra lo que comparar")
elif not [l for l in base if l.startswith("| D")]:
    difs.append("la base de `7e99388` no contiene ni una fila `| D`: lo que se ha traído "
                "no es el registro de decisiones")
check("G-11b", "`D1`-`D86` conservan su texto (D67 restaurada al de 7e99388; falla CERRADO sin git)",
      _base_raw is not None and not difs,
      "ninguna difiere" if (_base_raw is not None and not difs) else "DIFIEREN: " + ", ".join(difs))

# ── G-12 · PN-14 presente y SIN enmienda redactada ───────────────────
tiene = "## `PN-14`" in t11
i = t11.index("## `PN-14`") if tiene else -1
cuerpo = t11[i:t11.index("**Resumen para el Owner", i)] if tiene else ""
sin_enmienda = tiene and "no se redacta ninguna enmienda" in cuerpo.lower()
campos = ["QUÉ PRESIONA", "TEXTO VIGENTE", "MATERIA MÍNIMA", "ALCANCE", "BLOQUEA",
          "CONDICIÓN DE", "ORIGEN"]
falta = [c for c in campos if c not in cuerpo]
check("G-12", "`PN-14` presente, con sus campos, y SIN enmienda redactada",
      tiene and sin_enmienda and not falta,
      "; ".join(falta) if falta else ("presente y sin redactar" if sin_enmienda else "falta la declaracion"))

# ── G-13 · el censo de presiones es COHERENTE, y su tope se DERIVA ───
#
# La versión anterior exigía literalmente 14 cabeceras y 12 vigentes: dos cifras escritas
# a mano en la comprobación que existe para que las cifras no se escriban a mano. Fallaba
# en rojo el día que nacía `PN-15`, que es exactamente lo que §16 existe para permitir.
# Lo comprobable es la COHERENCIA: la serie es continua, las excluidas están marcadas una
# a una, y el resumen de §16 declara lo mismo que derivan las cabeceras.
cab = re.findall(r"^## `PN-(\d+)` ·(.*)$", t11, re.M)
_nums = sorted(int(n) for n, _ in cab)
vigentes = [n for n, resto in cab if "RETIRADA" not in resto and "FUSIONADA" not in resto]
_excluidas = [f"PN-{n}" for n, resto in cab if "RETIRADA" in resto or "FUSIONADA" in resto]
_g13 = []
if _nums != list(range(1, (_nums[-1] if _nums else 0) + 1)):
    _g13.append(f"la serie PN no es continua: {_nums}")
if len(_nums) != len(set(_nums)):
    _g13.append("hay cabeceras PN repetidas")
# el resumen de §16 tiene que declarar lo MISMO que derivan las cabeceras
_m = re.search(r"^VIGENTES · ([A-ZÁÉÍÓÚa-z]+)$", t11, re.M)
if not _m:
    _g13.append("el resumen de §16 no declara «VIGENTES · <n>»")
elif _num(_m.group(1)) != len(vigentes):
    _g13.append(f"el resumen dice {_m.group(1)} y las cabeceras derivan {len(vigentes)}")
# y el BARRIDO de `PN-15` sobre el material APROBADO, derivado fichero a fichero (`P-06`)
#
# El bloque de evidencia declaraba «cero apariciones de `G20`, `G21` y `G23` en el documento
# 11, en (a), en (b) y en `E2`», y era falso del documento 11 —donde hay decenas, casi todas
# introducidas por el propio bloque que lo negaba: la evidencia se destruía al registrarla—.
# La tesis que sí se sostiene, y la única que la presión necesita, es que **el material
# APROBADO no contiene una derogación válida**. Aquí se deriva ese barrido y se contrasta
# contra las tres cifras publicadas. El documento 11 queda fuera a propósito: sus
# apariciones son documentales y contarlas no probaría nada.
_APROBADO = {"(a)": "docs/rediseno/a-CAPACIDADES-APROBADA.md",
             "(b)": "docs/rediseno/b-RECORRIDO-APROBADA.md",
             "E2":  "docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md"}
_m_bar = re.search(r"\(a\) (\d+) · \(b\) (\d+) · E2 (\d+)", t11)
if not _m_bar:
    _g13.append("el bloque de `PN-15` no publica el barrido «(a) n · (b) n · E2 n»")
else:
    _pub = dict(zip(("(a)", "(b)", "E2"), (int(g) for g in _m_bar.groups())))
    for _k, _ruta in _APROBADO.items():
        _real = sum(1 for l in lineas(os.path.join(RAIZ, _ruta))
                    if re.search(r"\bG2[0-3]\b", l))
        if _pub[_k] != _real:
            _g13.append(f"barrido de `PN-15`: publica {_pub[_k]} en {_k} y el fichero "
                        f"deriva {_real}")

check("G-13", "el censo de presiones es coherente y el barrido de `PN-15` sobre el material APROBADO, derivado",
      not _g13,
      "; ".join(_g13) or
      f"{len(cab)} cabeceras - {len(_excluidas)} marcadas ({', '.join(_excluidas)}) "
      f"= {len(vigentes)} vigentes, y el resumen de §16 dice lo mismo")

# ── G-14 · F-01 reclasificado ────────────────────────────────────────
tchk = leer(CHK)
m = re.search(r"^\| `F-01` \| (\w+) \| \*\*`([A-Z_0-9]+)`\*\* \|(.*)$", tchk, re.M)
cols = [c.strip() for c in m.group(3).split(" | ")] if m else []
ok = (m and m.group(2) == "PRESION_LISTA_PARA_F5"
      and cols[2] != "no" and cols[3] != "no")
check("G-14", "`F-01` reclasificado a `PRESION_LISTA_PARA_F5`, con requiere_f5 y requiere_f6",
      ok, f"estado={m.group(2) if m else '?'} f5={cols[2] if cols else '?'} f6={'sí' if cols and cols[3]!='no' else '?'}")

# ── G-15 · el contrato de `<CAP>:revision`, DERIVADO Y EJECUTADO ─────
#
# Reescrita por la corrección del GATE DE COBERTURA (`D104`). La versión anterior derivaba
# de verdad la CIFRA, y aun así el gate la refutó por cuatro caminos: no implementaba la vía
# PROPIETARIA que su criterio nombra en primer lugar (`O-01`), no evaluaba la vía CONDICIONAL
# de `proceso:AUD` (`M-01`), partía estático/dinámico buscando la palabra «DERIVADO» en un
# campo `{tipo: texto}` (`N-02`), y comparaba sólo la PRIMERA proyección del bloque, con lo
# que una segunda contradictoria pasaba en verde (`M-04`, refutación 2).
#
# Ahora deriva las CUATRO vías, parte por pertenencia al conjunto de las quince, deriva el
# ancla de posición, y exige que la proyección publicada sea ÚNICA y coincida.

_DIR_CAPS = os.path.join(RAIZ, "kernel/operativo/capacidades")
_PROC_MD = os.path.join(RAIZ, "kernel/operativo/recorrido/01-PROCESOS.md")

# El catálogo de capacidades se deriva UNA VEZ, aquí, y lo usan `G-15` y `G-24`.
#
# `Q-27`. `_CAPS` era `frozenset(os.listdir(_DIR_CAPS))` —que incluye FICHEROS— y `G-24`
# filtraba por `os.path.isdir`: dos comprobaciones que dicen derivar el mismo conjunto y
# derivaban conjuntos distintos, de modo que un fichero suelto en el directorio ampliaba el
# discriminante estructural de `G-15` sin que `G-24` lo viera. Una capacidad es un
# DIRECTORIO con su ficha dentro, y eso se dice una sola vez.
def _capacidades():
    if not os.path.isdir(_DIR_CAPS):
        raise SedeIlegible("kernel/operativo/capacidades: no existe, y sin el catálogo de "
                           "capacidades no hay discriminante que aplicar")
    return tuple(sorted(d for d in os.listdir(_DIR_CAPS)
                        if os.path.isdir(os.path.join(_DIR_CAPS, d))))

_CAPS_DIRS = _capacidades()
_CAPS = frozenset(_CAPS_DIRS)

# ── el conjunto VIGILADO se DERIVA de una DECLARACIÓN ESTRUCTURADA ────────
#
# `Q-09` del dictamen, en su primera mitad, y `Q-10`. El literal `("DOM", "SEG")` había
# desaparecido, pero lo que lo sustituyó era `re.search(r"participa dos veces", leer(ficha))`
# sobre el fichero ENTERO: una frase escrita en cualquier párrafo de prosa de cualquier
# ficha daba de alta una capacidad en el conjunto vigilado. Y el fixture «7bis» que decía
# respaldarlo **recomputaba la misma comprensión de conjunto sobre los mismos ficheros**:
# una tautología que no puede fallar, contada entre los «17 fixtures en verde».
#
# La sede real es el campo `deriva_de:` de la ficha, que cita el material APROBADO. Aquí se
# exige que la declaración (a) viva en ese campo y no en la prosa, (b) cite su origen en
# `b.16` y (c) tenga como SUJETO el código de la propia capacidad, que es el nombre de su
# directorio. Y el fixture de abajo es real: alimenta textos sintéticos y exige que los tres
# casos negativos NO deriven.
def _declara_doble_participacion(codigo, texto):
    """¿La ficha de `codigo` DECLARA su doble participación, en su campo y con su sujeto?"""
    m = re.search(r"^deriva_de:\s*$(.*?)(?=^[A-Za-z_][A-Za-z0-9_]*:|\Z)",
                  texto, re.M | re.S)
    if not m:
        return False
    for item in re.findall(r"^\s*-\s*(.*)$", m.group(1), re.M):
        if not re.search(r"\bb\.16\b", item):
            continue
        if re.search(r"\b%s\b\s+participa\s+dos\s+veces\b" % re.escape(codigo), item):
            return True
    return False

def _derivar_vigiladas(fichas):
    """`fichas` es {codigo: texto}. Devuelve la tupla ordenada de las que lo declaran."""
    return tuple(sorted(c for c, txt in fichas.items()
                        if _declara_doble_participacion(c, txt)))

_FICHAS = {}
for _c in _CAPS_DIRS:
    _ruta_ficha = os.path.join(_DIR_CAPS, _c, "CAPACIDAD.md")
    if os.path.isfile(_ruta_ficha):
        _FICHAS[_c] = leer(_ruta_ficha)
_VIGILADAS = _derivar_vigiladas(_FICHAS)

def _base(valor):
    """Capacidad BASE: segmento anterior al primer `:` y al primer `/`. Nada más."""
    return valor.strip().strip('"').strip("'").split(":")[0].split("/")[0].strip()

def _limpio(valor):
    return valor.strip().strip('"').strip("'").strip()

def _bloques_proceso(texto):
    return re.findall(r"```yaml ads:proceso\n(.*?)```", texto, re.S)

def _campos(bloque):
    """Los campos REALES del bloque, leyendo INDENTACIÓN y ESCALARES DE BLOQUE.

    Devuelve `(campos, prosa_sospechosa)`. `campos` es [(seccion, clave, valor, sangria)].

    `Q-05`. La versión anterior troceaba el bloque con `find("obligatorias:")` /
    `find("condicionales:")` y sacaba las participaciones con un `re.findall` sobre esos
    SEGMENTOS DE TEXTO. Eso no es leer YAML: es buscar una cadena. Una línea escrita dentro
    del escalar de prosa de un `criterio_de_satisfaccion` —o de `capa_exigida`, `condicion`
    o `autoridad_de_retirada`— entraba en la derivación como si fuera un campo, y `G-15`
    seguía en verde. El contrato de `D104` declara que esos cuatro campos NO se leen, y el
    mecanismo no lo sostenía.

    Aquí una línea sólo es campo si vive al nivel de sangría de su sección y NO está dentro
    de un escalar `>` o `|`. Lo que aparece dentro de un escalar es PROSA, siempre — y si esa
    prosa tiene aspecto de campo de participación, se devuelve en `prosa_sospechosa` para
    poder fallar NOMBRANDO el campo que la contiene, en vez de acusar a la proyección.
    """
    campos, prosa = [], []
    seccion = None            # `obligatorias` · `condicionales` · None
    ind_seccion = None        # sangría de la clave de sección, siempre 0 en este esquema
    ind_item = None           # sangría de las claves DIRECTAS del item en curso
    esc_ind = esc_clave = None
    for linea in bloque.split("\n"):
        if not linea.strip():
            continue
        ind = len(linea) - len(linea.lstrip(" "))
        if esc_ind is not None:
            if ind > esc_ind:
                if re.match(r"\s*(?:capacidad_productora|capacidad)\s*:", linea):
                    prosa.append((seccion, esc_clave, linea.strip()))
                continue
            esc_ind = esc_clave = None
        cuerpo = linea.strip()
        nuevo_item = cuerpo.startswith("- ")
        if nuevo_item:
            cuerpo, ind = cuerpo[2:].strip(), ind + 2
        m = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", cuerpo)
        if not m:
            continue
        clave, valor = m.group(1), m.group(2).strip()

        # ── ESTRUCTURA · quién es sección, quién es item, quién es hijo colgado ──
        #
        # `Q-09`, segunda mitad. La docstring prometía «una línea sólo es campo si vive al
        # nivel de sangría de su sección», y el código **no lo aplicaba**: `seccion` se
        # asignaba cuando `ind == 0` y desde ahí se pegaba a TODA línea siguiente, con
        # independencia de a qué profundidad viviera. Un `capacidad_productora: "DOM"`
        # anidado dos niveles bajo una clave inventada se derivaba como participación
        # obligatoria, `prosa_sospechosa` quedaba VACÍA —de modo que el fallo no se
        # denunciaba por ninguna vía— y además **desplazaba el ancla del proceso**. Era peor
        # que el defecto que la corrección anterior decía haber cerrado.
        #
        # Ahora la sangría manda: la sección vive en columna 0, el item fija la sangría de
        # sus claves DIRECTAS, y todo lo que cuelgue por debajo de esa sangría **no es un
        # campo del item**. Si además tiene aspecto de campo de participación, se DENUNCIA
        # con el contenedor que lo cobija, igual que la prosa de un escalar.
        if ind == 0:
            seccion = clave if clave in ("obligatorias", "condicionales") else None
            ind_seccion = 0
            ind_item = None
        elif seccion is not None:
            if nuevo_item:
                ind_item = ind
            elif ind_item is None:
                ind_item = ind
            elif ind > ind_item:
                if clave in ("capacidad_productora", "capacidad"):
                    prosa.append((seccion, "una clave anidada bajo el item", linea.strip()))
                continue
            elif ind < ind_item:
                # sube de nivel sin volver a columna 0: ya no es un campo del item
                ind_item = ind

        if valor in (">", "|", ">-", "|-", ">+", "|+"):
            esc_ind, esc_clave = ind, clave
            valor = ""
        campos.append((seccion, clave, valor, ind))
    return campos, prosa

def _analizar(bloque):
    """(pid, propietario, es_estatico, ancla, participaciones, prosa_sospechosa).

    `participaciones` es [(capacidad_base, via, seccion)] con via ∈ {1,2,3,4}:
      1 propietaria · 2 obligatoria desnuda · 3 condicional desnuda · 4 item enlazado tipado
    y `seccion` ∈ {propietaria, obligatorias, condicionales}. **La PROCEDENCIA se conserva**
    (`Q-03`, `Q-10`): una obligatoria se exige SIEMPRE —también tipada por la vía 4— y una
    condicional sólo cuando su condición está activa, luego la vía por sí sola ya no basta
    para saber qué exige un item.

    `capa_exigida`, `condicion`, `criterio_de_satisfaccion` y `autoridad_de_retirada` NO se
    leen, y ahora el mecanismo lo garantiza: sus escalares se saltan como prosa (`_campos`).
    Toda la inferencia sigue siendo UNA prueba de pertenencia a `_CAPS`.
    """
    campos, prosa = _campos(bloque)
    pid = next(_limpio(v) for sec, k, v, i in campos if k == "id" and i == 0).split(":", 1)[1]
    pg = next(_limpio(v) for sec, k, v, i in campos if k == "propietario_global" and i == 0)
    obl = [_limpio(v) for sec, k, v, i in campos
           if sec == "obligatorias" and k == "capacidad_productora"]
    cond = [_limpio(v) for sec, k, v, i in campos
            if sec == "condicionales" and k == "capacidad"]

    # DISCRIMINANTE ESTRUCTURAL: igualdad contra el conjunto de las quince, no subcadena
    estatico = pg in _CAPS

    # ANCLA DE POSICIÓN: la obligatoria de `VER` si existe; si no, la última obligatoria.
    # Se compara sobre la capacidad BASE (`Q-02`): antes se comparaba la cadena CRUDA, y un
    # `capacidad_productora: "VER:dosier"` —referencia tipada LEGÍTIMA por el propio
    # contrato— dejaba de ser `VER`, desplazaba el ancla del proceso en silencio y `G-15`
    # imprimía verde. `D104` declara que normalizar a la capacidad base ES TODA LA
    # INFERENCIA QUE HAY: el ancla no puede ser la excepción.
    obl_base = [_base(v) for v in obl]
    ancla = "VER" if "VER" in obl_base else (obl_base[-1] if obl_base else None)

    part = []
    if estatico and _base(pg) in _VIGILADAS:
        part.append((_base(pg), 1, "propietaria"))     # vía 1 · propietaria
    for v in obl:
        b = _base(v)
        if b in _VIGILADAS:
            part.append((b, 2 if v == b else 4, "obligatorias"))
    for v in cond:
        b = _base(v)
        if b in _VIGILADAS:
            part.append((b, 3 if v == b else 4, "condicionales"))
    return pid, pg, estatico, ancla, part, prosa

def _derivar(texto):
    """(estaticos, dinamicos, anclas, prosa) — estaticos: {(proc,cap): (via, seccion)}."""
    estaticos, dinamicos, anclas, prosa = {}, {}, {}, []
    for b in _bloques_proceso(texto):
        pid, pg, est, ancla, part, pr = _analizar(b)
        anclas[pid] = ancla
        prosa += [(pid, sec, clave, linea) for sec, clave, linea in pr]
        if est:
            for cap, via, sec in part:
                estaticos[(pid, cap)] = (via, sec)
        else:
            dinamicos[pid] = part
    return estaticos, dinamicos, anclas, prosa

def _exige_item(proceso_part, propietario_efectivo, condicionales_activos):
    """REGLA POR ITEM: propietario del item ∪ obligatorias ∪ condicionales ACTIVADAS.

    Manda la PROCEDENCIA, no la vía (`Q-10`). La versión anterior escribía
    `if via in (3, 4)`, con lo que una participación tipada de la sección `obligatorias`
    —vía 4 legítima— se trataba como condicional y dejaba de exigirse cuando su condición
    no estaba activa. Hoy ninguna vía 4 procede de `obligatorias` en el árbol real, así que
    el defecto era LATENTE: se corrige antes de que tenga instancias, y el fixture de abajo
    lo mantiene cerrado.
    """
    out = set()
    b = _base(propietario_efectivo)
    if b in _VIGILADAS:
        out.add(b)
    for cap, via, seccion in proceso_part:
        if seccion == "obligatorias":
            out.add(cap)
        elif seccion == "condicionales" and cap in condicionales_activos:
            out.add(cap)
    return out

_g15 = []
_PROC = leer(_PROC_MD)
_est, _din, _anclas, _prosa = _derivar(_PROC)
_procs_est = sorted({p for p, _ in _est})
_FIXTURES = []          # censo de fixtures EJECUTADOS, derivado y contrastado (`Q-12`)

# 0 · ninguna PROSA se cuela como participación (`Q-05`)
#
# Falla NOMBRANDO el campo que contiene la línea, que es lo que el gate pidió: acusar a la
# proyección publicada de no cuadrar cuando el defecto está en un escalar de prosa mandaría
# a corregir la sede equivocada.
for _pid, _sec, _clave, _linea in _prosa:
    _g15.append(f"prosa con aspecto de campo en `proceso:{_pid}` → `{_clave}` "
                f"(sección {_sec}): «{_linea}». Un escalar de prosa NO declara participación")

# 1 · el contrato tiene que traer sus piezas y nombrar las cuatro vías
i19 = t11.index("### `DOM` y `SEG` participan DOS veces")
b19 = t11[i19:t11.index("**Y dos más, que no son defectos de F4", i19)]
b19p = re.sub(r"[`*]", "", re.sub(r"\s+", " ", b19))
for pieza in ("PROPIETARIA", "OBLIGATORIA", "CONDICIONAL", "ITEM PROPIO",
              "DATOS DE ENTRADA", "ALGORITMO DE", "SALIDA ESPERADA", "CASOS POSITIVOS",
              "CONTRAEJEMPLOS", "composicion-incompleta", "PROPIETARIO", "F6",
              "ANCLA DE", "REGLA POR ITEM"):
    if pieza not in b19:
        _g15.append(f"el contrato no trae «{pieza}»")
if "NO se analizan `capa_exigida` ni `condicion`" not in b19 and \
   "capa_exigida, condicion, criterio_de_satisfaccion y autoridad_de_retirada NO se leen" not in b19p:
    _g15.append("no declara que los campos de prosa NO se leen")
if "pertenencia al conjunto de las QUINCE" not in b19p:
    _g15.append("no declara el discriminante estructural por pertenencia")

# 2 · la proyección publicada tiene que ser ÚNICA y coincidir con lo derivado.
#     Ni el número ni el conteo de proyecciones se escriben aquí: se derivan.
#
# `Q-03` del dictamen. El patrón era
# `([A-ZÁÉÍÓÚa-z]+) procesos . ([A-ZÁÉÍÓÚa-z]+) pares`, y ese `.` exige **exactamente UN
# carácter** entre «procesos» y el numeral siguiente. El adjudicador escribió una segunda
# proyección con dos palabras de por medio —«*SEIS procesos y en total DIEZ pares, y es la
# vigente*»— y la comprobación que el contrato de `D104` promete que «suspende» el bloque
# no vio nada: **30/30 en verde**. La unicidad que se prometía no existía; existía la
# unicidad de una redacción.
#
# Ahora la unicidad se comprueba por TRES caminos independientes, y ninguno depende de
# cómo esté redactada la frase:
#   a) el EMPAREJAMIENTO «<n> procesos … <n> pares» dentro de la misma cláusula, con el
#      hueco acotado por los separadores del bloque y no por un carácter,
#   b) toda cifra que califique al CATÁLOGO ESTÁTICO en procesos,
#   c) toda cifra de PARES que no sea componente de un desglose declarado —por vía o por
#      procedencia— es una afirmación del TOTAL, y como tal se contrasta.
_SEP = r"[^.·;\n]"
_proys = re.findall(_NUM + r"\s+procesos\b" + _SEP + r"{0,80}?" + _NUM + r"\s+pares\b",
                    b19p)
if not _proys:
    _g15.append("la proyección no publica «<n> procesos · <n> pares» de forma legible")
elif len(_proys) > 1:
    _g15.append(f"hay {len(_proys)} proyecciones «<n> procesos … <n> pares» en el bloque y "
                f"debe haber UNA: {_proys}. Una segunda proyección del mismo objeto es el "
                f"contraejemplo de `M-04`, y el contrato promete que suspende el bloque")
else:
    _p, _q = _num(_proys[0][0]), _num(_proys[0][1])
    if _p != len(_procs_est):
        _g15.append(f"publica {_proys[0][0]} procesos y el catálogo deriva {len(_procs_est)}")
    if _q != len(_est):
        _g15.append(f"publica {_proys[0][1]} pares y el catálogo deriva {len(_est)}")

# 2bis · el REPARTO EXACTO POR VÍA, no sólo el total (`Q-03`)
#
# Un total de nueve pares admite repartos semánticamente distintos: mover `DOM` y `SEG` de
# `FEA` de la vía 4 a la vía 3 deja el total intacto y cambia lo que el contrato significa.
# La proyección publica el reparto y aquí se contrasta vía a vía.
_reparto_real = Counter(via for via, _ in _est.values())
_reparto_pub = {int(v): int(n) for v, n in re.findall(r"vía (\d) . (\d+) par", b19p)}
if not _reparto_pub:
    _g15.append("la proyección no publica el REPARTO POR VÍA «vía <n> · <n> pares»")
else:
    for _v in (1, 2, 3, 4):
        if _reparto_pub.get(_v, 0) != _reparto_real.get(_v, 0):
            _g15.append(f"reparto por vía {_v}: publica {_reparto_pub.get(_v, 0)} y "
                        f"el catálogo deriva {_reparto_real.get(_v, 0)}")

# 2bis-2 · el REPARTO POR PROCEDENCIA, que no se contrastaba contra nada (`Q-28`)
#
# La procedencia —propietaria, `obligatorias`, `condicionales`— se conservaba en la
# derivación desde `Q-10` y **no se publicaba en ninguna sede**: era el único de los tres
# desgloses sin proyección contra la que compararse, que es exactamente la magnitud
# derivada sin contraste que `M-04` describe. §19 la publica ahora, una sola vez, y aquí
# se contrasta procedencia a procedencia.
_PROCEDENCIAS = ("propietaria", "obligatorias", "condicionales")
_proc_real = Counter(sec for _, sec in _est.values())
_proc_pub = {}
for _p_, _n_ in re.findall(r"(propietaria|obligatorias|condicionales)\s*·\s*(\d+)\s+par",
                           b19p):
    _proc_pub.setdefault(_p_, int(_n_))
if not _proc_pub:
    _g15.append("§19 no publica el REPARTO POR PROCEDENCIA «<procedencia> · <n> pares»; sin "
                "sede publicada, la procedencia se deriva y no se contrasta contra nada")
else:
    for _p_ in _PROCEDENCIAS:
        if _proc_pub.get(_p_, 0) != _proc_real.get(_p_, 0):
            _g15.append(f"reparto por procedencia «{_p_}»: publica {_proc_pub.get(_p_, 0)} "
                        f"y el catálogo deriva {_proc_real.get(_p_, 0)}")
    if sum(_proc_pub.get(_p_, 0) for _p_ in _PROCEDENCIAS) != len(_est):
        _g15.append(f"el reparto por procedencia suma "
                    f"{sum(_proc_pub.get(_p_, 0) for _p_ in _PROCEDENCIAS)} y los pares "
                    f"derivados son {len(_est)}")

# 2bis-3 · ninguna cifra suelta del bloque contradice al total ni al catálogo
#
# Los dos desgloses de arriba consumen las cifras que les pertenecen. Cualquier OTRA cifra
# de «pares» del bloque afirma el TOTAL, y cualquier cifra que califique al catálogo
# estático en procesos afirma su tamaño. Es lo que convierte la unicidad en general: no hay
# redacción que se escape porque no se comprueba una redacción, se comprueban las cifras.
_componentes = set()
for _m_c in re.finditer(r"(?:vía \d|propietaria|obligatorias|condicionales)\s*·\s*(\d+)\s+par",
                        b19p):
    _componentes.add(_m_c.start(1))
for _m_c in re.finditer(_NUM + r"\s+pares?\b", b19p):
    if _m_c.start(1) in _componentes:
        continue
    _v = _num(_m_c.group(1))
    if _v is not None and _v != len(_est):
        _g15.append(f"el bloque afirma «{_m_c.group(1)} pares» fuera de todo desglose "
                    f"declarado y el catálogo deriva {len(_est)}")
for _m_c in re.finditer(r"cat[áa]logo(?:\s+est[áa]tico)?[^.·;]{0,40}?" + _NUM
                        + r"\s+procesos\b", b19p):
    _v = _num(_m_c.group(1))
    if _v is not None and _v != len(_procs_est):
        _g15.append(f"el bloque atribuye al catálogo estático «{_m_c.group(1)} procesos» y "
                    f"se derivan {len(_procs_est)}")

# 2ter · las ANCLAS publicadas, proceso a proceso, contra las derivadas (`Q-11`)
#
# La sede publicaba «`INV` `AUD` → tras su única obligatoria, `conclusion-fundada` de
# `INV`», y `conclusion-fundada` es la obligatoria de `AUD`: la de `INV` es
# `evidencia-producida`. Una sola frase atribuía el mismo item a dos procesos. Ahora la
# proyección publica el ancla de cada proceso y esto la contrasta.
_m_anclas = re.search(r"ANCLA DERIVADA HOY(.{0,600})", b19p)
_anclas_pub = dict(re.findall(r"\b([A-Z]{3}) → ([A-Z]{3})\b", _m_anclas.group(1))) \
    if _m_anclas else {}
if not _anclas_pub:
    _g15.append("la proyección no publica «ANCLA DERIVADA HOY» con «<PROC> → <CAP>» "
                "proceso a proceso")
else:
    for _pr, _an in sorted(_anclas.items()):
        if _anclas_pub.get(_pr) != _an:
            _g15.append(f"ancla de `{_pr}`: publica {_anclas_pub.get(_pr)} y se deriva {_an}")
    for _pr in sorted(set(_anclas_pub) - set(_anclas)):
        _g15.append(f"la proyección publica un ancla para `{_pr}`, que no es un proceso")

# 3 · las cuatro vías, ejercitadas sobre FIXTURES SINTÉTICOS
#
# Los fixtures se construyen aquí, enteros, y NO mutando el árbol real: un fixture que
# depende de que cierta cadena exista en el corpus se rompe el día que el corpus cambia,
# y entonces la comprobación deja de comprobar en vez de fallar con diagnóstico.
_FX = """```yaml ads:proceso
id: proceso:FX
propietario_global: "%s"
obligatorias:
  - id: uno
    capacidad_productora: "%s"
  - id: dos
    capacidad_productora: "VER"
condicionales:
  - capacidad: "%s"
```"""

# vía 1 · PROPIETARIA — el fixture que `O-01` demostró que la versión anterior no veía
_FIXTURES.append("vía 1 · propietaria")
_e1, _, _, _ = _derivar(_FX % ("DOM", "CON", "APR"))
if _e1.get(("FX", "DOM")) != (1, "propietaria"):
    _g15.append("fixture VÍA 1: un `propietario_global: \"DOM\"` no emite par propietario")

# vía 2 y vía 4 sobre el fixture, con las dos formas del mismo campo
_FIXTURES += ["vía 2 · obligatoria desnuda", "vía 4 · item enlazado tipado"]
_e2, _, _, _ = _derivar(_FX % ("PRD", "SEG", "DOM:condiciones"))
if _e2.get(("FX", "SEG")) != (2, "obligatorias"):
    _g15.append("fixture VÍA 2: `capacidad_productora: \"SEG\"` no emite par obligatorio")
if _e2.get(("FX", "DOM")) != (4, "condicionales"):
    _g15.append("fixture VÍA 4: `DOM:condiciones` no emite par tipado")

# vía 3 sobre el fixture, con la capacidad BASE desnuda
_FIXTURES.append("vía 3 · condicional desnuda")
_e3, _, _, _ = _derivar(_FX % ("PRD", "CON", "SEG"))
if _e3.get(("FX", "SEG")) != (3, "condicionales"):
    _g15.append("fixture VÍA 3: `capacidad: \"SEG\"` desnuda no emite par condicional")

# y el discriminante: un propietario que NO es uno de los quince cae en dinámico
_FIXTURES.append("discriminante estructural")
_, _d4, _, _ = _derivar(_FX % ("la capacidad que decida el encargo", "CON", "APR"))
if "FX" not in _d4:
    _g15.append("el discriminante no clasifica como dinámico un propietario que no es "
                "uno de los quince")

# y sobre el ÁRBOL REAL, las dos vías que hoy tienen instancias
if _est.get(("DEP", "SEG")) != (2, "obligatorias"):
    _g15.append("árbol real: `(DEP, SEG)` no se deriva por la vía obligatoria")
if sum(1 for via, _ in _est.values() if via == 4) == 0:
    _g15.append("árbol real: ninguna participación tipada `<CAP>:condiciones` se deriva")

# vía 3 · CONDICIONAL desnuda — `AUD` declara `DOM` y `SEG` así
_aud = dict((c, v) for c, v, _ in _din.get("AUD", []))
if _aud.get("DOM") != 3 or _aud.get("SEG") != 3:
    _g15.append("fixture VÍA 3: los condicionales desnudos de `AUD` no se derivan")

# 3bis · el ANCLA no se deja desplazar por una referencia TIPADA legítima (`Q-02`)
_FIXTURES.append("ancla ante `VER:dosier`")
_, _, _a5, _ = _derivar(_FX % ("PRD", "CON", "APR"))
_FXVER = _FX.replace('capacidad_productora: "VER"', 'capacidad_productora: "VER:dosier"')
_, _, _a6, _ = _derivar(_FXVER % ("PRD", "CON", "APR"))
if _a5.get("FX") != "VER" or _a6.get("FX") != "VER":
    _g15.append(f"fixture ANCLA TIPADA: `VER` da {_a5.get('FX')} y `VER:dosier` da "
                f"{_a6.get('FX')}; una referencia tipada legítima desplaza el ancla")

# 3ter · una PROSA con aspecto de campo no participa, y se DENUNCIA (`Q-05`)
_FIXTURES.append("prosa con aspecto de campo")
_FXPROSA = """```yaml ads:proceso
id: proceso:FY
propietario_global: "PRD"
obligatorias:
  - id: uno
    capacidad_productora: "CON"
    criterio_de_satisfaccion: >
      el criterio menciona, sin ser un campo,
      capacidad_productora: "DOM"
      y no debe contar como participación
condicionales:
  - capacidad: "APR"
```"""
_ey, _, _, _py = _derivar(_FXPROSA)
if ("FY", "DOM") in _ey:
    _g15.append("fixture PROSA: una línea dentro de un escalar `>` emite participación")
if not _py:
    _g15.append("fixture PROSA: la línea sospechosa no se denuncia con su campo contenedor")

# 3ter-bis · la INDENTACIÓN, que la docstring prometía y el código no aplicaba (`Q-09`)
#
# El fixture del adjudicador, literal: un `capacidad_productora: "DOM"` anidado bajo una
# clave inventada dentro del item. Antes se derivaba como participación obligatoria, la
# lista de prosa sospechosa quedaba vacía y el ancla del proceso se desplazaba a `DOM`.
_FIXTURES.append("clave anidada bajo el item, por indentación")
_FXIND = """```yaml ads:proceso
id: proceso:FI
propietario_global: "PRD"
obligatorias:
  - id: uno
    capacidad_productora: "CON"
    notas_internas:
      comentario: algo
      capacidad_productora: "DOM"
  - id: dos
    capacidad_productora: "VER"
condicionales:
  - capacidad: "APR"
```"""
_ei, _di, _ai, _pi = _derivar(_FXIND)
if ("FI", "DOM") in _ei or any(c == "DOM" for c, _, _ in _di.get("FI", [])):
    _g15.append("fixture INDENTACIÓN: una clave anidada dos niveles bajo el item emite "
                "participación como si fuera un campo del item")
if not _pi:
    _g15.append("fixture INDENTACIÓN: la clave anidada no se DENUNCIA con su contenedor, "
                "de modo que el defecto no sale por ninguna vía")
if _ai.get("FI") != "VER":
    _g15.append(f"fixture INDENTACIÓN: la clave anidada desplaza el ancla del proceso a "
                f"{_ai.get('FI')}")

# 3quater · una OBLIGATORIA tipada se exige SIEMPRE, no como condicional (`Q-10`)
_FIXTURES.append("obligatoria tipada de vía 4")
_FXOBL = """```yaml ads:proceso
id: proceso:FZ
propietario_global: "la capacidad que decida el encargo"
obligatorias:
  - id: uno
    capacidad_productora: "SEG:condiciones"
condicionales:
  - capacidad: "DOM"
```"""
_, _dz, _, _ = _derivar(_FXOBL)
if _exige_item(_dz.get("FZ", []), "PRD", set()) != {"SEG"}:
    _g15.append("fixture OBLIGATORIA TIPADA: una `SEG:condiciones` declarada en "
                "`obligatorias` deja de exigirse cuando ninguna condición está activa")
if _exige_item(_dz.get("FZ", []), "PRD", {"DOM"}) != {"SEG", "DOM"}:
    _g15.append("fixture OBLIGATORIA TIPADA: activar la condicional no acumula sobre la "
                "obligatoria")

# 4 · `AUD` dinámico, con sus CUATRO combinaciones por item
_pa = _din.get("AUD", [])
for prop, activos, esperado in (
    ("DOM", set(),               {"DOM"}),
    ("SEG", set(),               {"SEG"}),
    ("PRD", set(),               set()),
    ("PRD", {"DOM", "SEG"},      {"DOM", "SEG"}),
    ("DOM", {"SEG"},             {"DOM", "SEG"}),
):
    _FIXTURES.append(f"AUD · propietario {prop} · activos {sorted(activos) or '∅'}")
    obtenido = _exige_item(_pa, prop, activos)
    if obtenido != esperado:
        _g15.append(f"fixture AUD (propietario {prop}, activos {sorted(activos) or '∅'}): "
                    f"esperado {sorted(esperado) or '∅'}, obtenido {sorted(obtenido) or '∅'}")

# 5 · `DIR` — dinámico por la MISMA regla, sin excepción escrita
_FIXTURES += ["DIR · propietario vigilado", "DIR · propietario ajeno"]
if "DIR" not in _din:
    _g15.append("`DIR` no se clasifica como propietario derivado por item")
if _exige_item(_din.get("DIR", []), "DOM", set()) != {"DOM"}:
    _g15.append("fixture DIR: propietario `DOM` no exige `DOM:revision`")
if _exige_item(_din.get("DIR", []), "ARQ", set()) != set():
    _g15.append("fixture DIR: propietario ajeno exige algo")
if any(p == "DIR" for p, _ in _est):
    _g15.append("`DIR` aparece en el catálogo ESTÁTICO, y su propietario no es uno de los quince")

# 6 · el ANCLA no exige `VER` donde no hay `VER`
_sin_ver = sorted(p for p, a in _anclas.items() if a != "VER")
if "AUD" not in _sin_ver:
    _g15.append("`AUD` recibe ancla `VER` y `AUD` no declara `VER`")
for _p in _sin_ver:
    if _anclas[_p] is None:
        _g15.append(f"`{_p}` no tiene ancla derivable")

# 7 · fixture NEGATIVO · quitar la obligatoria SEG de DEP retira el par
_FIXTURES.append("negativo · retirar la obligatoria de DEP")
_sin_seg = re.sub(r"  - id: condiciones-de-seguridad\n(?:    .*\n|      .*\n)*", "",
                  _PROC[_PROC.index("id: proceso:DEP"):_PROC.index("id: proceso:AUD")])
_ffix = _PROC[:_PROC.index("id: proceso:DEP")] + _sin_seg + _PROC[_PROC.index("id: proceso:AUD"):]
_efix, _, _, _ = _derivar(_ffix)
if ("DEP", "SEG") in _efix or len(_efix) >= len(_est):
    _g15.append("fixture negativo: quitar la obligatoria SEG de DEP no retira el par")

# 7bis · el conjunto VIGILADO, con fixtures que PUEDEN FALLAR (`Q-10`)
#
# El fixture anterior era
# `if set(_VIGILADAS) != {c for c in _CAPS if re.search("participa dos veces", leer(...))}`,
# es decir: **la misma comprensión de conjunto, sobre los mismos ficheros, que `_VIGILADAS`
# acababa de evaluar**. La condición no podía ser verdadera nunca, y se contaba entre los
# «17 fixtures en verde». Un contraste que recomputa la misma expresión sobre los mismos
# datos no es un contraste: es una tautología, y ocupa el sitio de la prueba que falta.
#
# Éstos alimentan TEXTO SINTÉTICO al derivador y exigen resultados distintos entre sí.
_FX_FICHA_OK = ('roles: [XX/uno]\n'
                'deriva_de:\n'
                '  - "b.16 · XX participa dos veces: condiciones antes de CON"\n'
                'materializacion: >\n  cualquier cosa\n')
_FX_FICHA_PROSA = ('roles: [XX/uno]\n'
                   'deriva_de:\n'
                   '  - "a.3 · XX: modelo y vocabulario"\n'
                   'materializacion: >\n'
                   '  aquí se explica que XX participa dos veces en el recorrido, y esto\n'
                   '  es PROSA, no una declaración\n')
_FX_FICHA_AJENA = ('roles: [XX/uno]\n'
                   'deriva_de:\n'
                   '  - "b.16 · YY participa dos veces: y YY no es esta ficha"\n')
_FIXTURES += ["ficha que DECLARA la doble participación",
              "ficha que sólo la menciona en PROSA",
              "ficha cuya declaración tiene OTRO sujeto"]
if _derivar_vigiladas({"XX": _FX_FICHA_OK}) != ("XX",):
    _g15.append("fixture FICHA: una declaración en `deriva_de` citando `b.16` con su propio "
                "sujeto no da de alta la capacidad en el conjunto vigilado")
if _derivar_vigiladas({"XX": _FX_FICHA_PROSA}) != ():
    _g15.append("fixture FICHA EN PROSA: una frase dentro de un escalar de prosa da de alta "
                "una capacidad en el conjunto vigilado")
if _derivar_vigiladas({"XX": _FX_FICHA_AJENA}) != ():
    _g15.append("fixture FICHA AJENA: una declaración cuyo sujeto es OTRA capacidad da de "
                "alta a la que la cita")
# y sobre el árbol real: el conjunto no puede quedar vacío, y cada miembro tiene ficha
if not _VIGILADAS:
    _g15.append("ninguna ficha DECLARA la doble participación en su campo `deriva_de`: el "
                "conjunto vigilado es vacío y `G-15` no vigilaría nada")
for _v in _VIGILADAS:
    if _v not in _CAPS:
        _g15.append(f"`{_v}` está en el conjunto vigilado y no es una capacidad del catálogo")

# 8 · el contrato exige que la prueba prescrita falle HOY nombrando DEP
if not re.search(r"FALLIDA nombrando.{0,80}?proceso:DEP → SEG:revision AUSENTE", b19p):
    _g15.append("su prueba no exige fallar HOY nombrando `proceso:DEP`")

# 9 · el CENSO DE FIXTURES publicado coincide con el EJECUTADO (`Q-12`)
#
# La sede decía «cinco fixtures, uno por vía y uno por proceso dinámico» junto a una
# enumeración de seis grupos, con tres procesos dinámicos. La cifra era manual y no
# describía lo que la batería ejecuta. Ahora el censo se DERIVA de los fixtures realmente
# corridos, y la sede publica ese número.
_censo_pub = re.search(r"CENSO DE FIXTURES[^.]{0,80}?(\d+) fixtures", b19p)
if not _censo_pub:
    _g15.append("la sede no publica el «CENSO DE FIXTURES … <n> fixtures»")
elif int(_censo_pub.group(1)) != len(_FIXTURES):
    _g15.append(f"censo de fixtures: la SEDE —§19 del documento 11, bloque «CENSO DE "
                f"FIXTURES»— publica {_censo_pub.group(1)} y la batería ejecuta "
                f"{len(_FIXTURES)}. La cifra la escribe la sede y la deriva la batería: "
                f"el responsable de cerrarlo es quien mantiene §19, y el remedio es una "
                f"línea: «{len(_FIXTURES)} fixtures». La batería no puede escribir en el "
                f"documento 11 y no se ablanda para que cuadre")

check("G-15",
      "`<CAP>:revision` derivado por las CUATRO vías, con procedencia, ancla normalizada, prosa excluida y censos derivados",
      not _g15,
      "; ".join(_g15) or
      f"catálogo {len(_procs_est)} procesos {sorted(_procs_est)} · {len(_est)} pares "
      f"(reparto por vía: {sorted(_reparto_real.items())}) · dinámicos {sorted(_din)} · "
      f"vigiladas {sorted(_VIGILADAS)} · anclas sin VER {_sin_ver} · "
      f"{len(_FIXTURES)} fixtures ejecutados, todos en verde")

# ── G-16 · 43 estados primarios, sin duplicados ─────────────────────
filas = re.findall(r"^\| `([A-Za-z0-9-]+)` \| (BLOQUEANTE|GRAVE|MEDIO|MENOR) \| \*\*`([A-Z_0-9]+)`\*\* \|(.*)$",
                   tchk, re.M)
ids = [f[0] for f in filas]
dup = [k for k, v in Counter(ids).items() if v > 1]
# `comp = [... if " y " in f[2] or "+" in f[2]]` vivía aquí y se RETIRA: el grupo 3 está
# restringido a `[A-Z_0-9]+` y nunca podía contener un espacio ni un `+`, luego la
# comprobación de estados compuestos no podía disparar jamás. Es `M-11`. La sustituye la
# detección sobre la LÍNEA ENTERA, más abajo.
# La MISMA regla, sobre el otro objeto que la necesita: las trece condiciones de cierre
# `C-L.1`–`C-L.13`. Se comprueba AQUÍ, dentro de `G-16`, porque es la misma norma y porque
# la batería no crece: sigue teniendo TREINTA comprobaciones.
#
# Reescrita por la corrección del GATE DE COBERTURA. La versión anterior comprobaba la
# COHERENCIA INTERNA del bloque resumen —que la cifra declarada casara con los ids
# nombrados— y nada más, con lo que mover `C-L.12` de estado ajustando los contadores
# pasaba en verde contradiciendo su propio detalle (`M-04`, refutación 3). Además llevaba
# DOS censos escritos a mano dentro de la comprobación cuyo objeto es esa disciplina
# (`O-02`), y una detección de estados compuestos que no podía disparar jamás (`M-11`).
#
# Ahora contrasta el resumen contra las TRECE FILAS DE DETALLE, deriva los componentes de
# `C-L.13` de esa misma fuente, y deriva su propio mensaje de éxito.
# `X-04` del documento 24 falsó `C-L.7` sobre el árbol que se juzgaba —el bloque de estado
# del checkpoint iba dos eventos atrasado bajo `actualizado: 2026-08-30`— y la clasificación
# vigente la mueve a **NO CERRADA**. El canon de estados tenía CINCO escritos y ése no
# estaba, de modo que `G-16` daba ROJO **con razón**: no reconocía el estado. Lo que se
# corrige es el CANON, no el contraste — que sigue siendo por IGUALDAD EXACTA, `Q-06`—:
# una condición puede volver a abrirse, y el instrumento tiene que saber decirlo. Escribir
# «CERRADA» para poner la comprobación en verde habría sido el mutante de `Q-06`.
# `AA` / CUARTO GATE. El canon vuelve a quedarse corto, y por la MISMA razón que la vez
# anterior: el cuarto gate midió `ASIGNADO − LEÍDO = 1` y la regla de cierre de `C-L.5`
# excluye la suficiencia, con lo que la clasificación vigente la mueve a **ABIERTA** — la
# primera vez en cuatro gates que deja de estar certificada. El canon tenía SEIS estados
# escritos y ése no estaba, de modo que `G-16` daba ROJO **con razón**: no reconocía el
# estado. **Lo que se corrige es el CANON, no el contraste**, que sigue siendo por IGUALDAD
# EXACTA (`Q-06`): una condición puede volver a abrirse y el instrumento tiene que saber
# decirlo. Escribir «CERTIFICADA» en el checkpoint para poner esto en verde habría sido el
# mutante que esta comprobación existe para cazar.
_ESTADOS_CL = ("CORREGIDAS EN F4c", "NO CERRADA", "ABIERTA", "REGISTRADAS PARA F5",
               "CONTRATADA PARA F6", "MIXTA POR DESGLOSE", "CERTIFICADA POR")

# `Z1-04`≡`Z-06`. El contraste de ESTADO era una expresión escrita EN LÍNEA dentro de
# `G-16c` —`if _det not in _admitidos`—, y por eso el bloque `c` de `G-31`, que existe para
# probar que ese contraste no se apaga con una palabra, no tenía a quién llamar: se escribió
# como `if f"CERRADA {_w}" in ("CERRADA",)`, **dos condiciones insatisfacibles por
# construcción** que no invocaban nada. Medido: se revirtió `G-16c` de igualdad exacta a
# `startswith` —la regresión que ese bloque existe para cazar— y `G-31` siguió en `OK`.
#
# El evaluador se extrae aquí, con UNA sede, y las dos lo llaman: `G-16c` para juzgar el
# árbol y `G-31c` para ejercitarlo con las palabras gatillo pegadas. No es una comprobación
# nueva: es la que ya estaba, invocando por fin lo que decía probar.
def _estado_casa(detalle, admitidos):
    """¿La fila de detalle declara EXACTAMENTE uno de los estados admitidos? (`Q-06`)

    Por IGUALDAD, que es la única comparación que ninguna calificación posterior puede
    invertir: «CERRADA SOLO EN PARTE, SIGUE ABIERTA Y BLOQUEA F5» no es «CERRADA».
    """
    return detalle in admitidos

_g16c = []
_asig, _declarado = {}, {}
# La clasificación VIGENTE está delimitada, y su detalle se lee DENTRO de ella (`Q-14`).
#
# Antes, las filas de detalle se buscaban en TODO el checkpoint y se tomaba la primera
# aparición de cada `C-L.n`: una fila de un bloque HISTÓRICO satisfacía el contraste de la
# clasificación vigente. Es la puerta por la que `C-L.3` podía estar descrita a la vez como
# CERRADA por la regla de `D103` —que `M-01` refutó— y como NO CERRADA, sin que nada lo
# viera. Ahora el bloque vigente se abre con «CÓMO QUEDA CADA CONDICIÓN», se cierra con
# «FIN DE LA CLASIFICACIÓN VIGENTE», y **todo lo que se contrasta sale de ahí dentro**.
_i = tchk.find("CÓMO QUEDA CADA CONDICIÓN")
_fin_vig = tchk.find("FIN DE LA CLASIFICACIÓN VIGENTE", _i) if _i >= 0 else -1
if _i < 0:
    _g16c.append("no se encuentra el bloque de clasificación VIGENTE de las condiciones")
elif _fin_vig < 0:
    _g16c.append("el bloque de clasificación vigente no se cierra con «FIN DE LA "
                 "CLASIFICACIÓN VIGENTE»: su alcance no es determinable")
else:
    _vigente = tchk[_i:_fin_vig]
    _fin_blq = tchk.find("= los trece ids distintos", _i)
    _blq = tchk[_i:_fin_blq if 0 < _fin_blq < _fin_vig else _fin_vig]
    for _est in _ESTADOS_CL:
        _m = re.search(rf"^\s*{re.escape(_est)}\s+(\d+)\s+(.*)$", _blq, re.M)
        if not _m:
            # `_ESTADOS_CL` es el VOCABULARIO ADMITIDO, no una lista de presencia
            # obligatoria: una clasificación no tiene por qué usar los seis estados, y
            # exigirlo ponía en ROJO cualquier árbol en el que ninguna condición estuviera
            # —por ejemplo— NO CERRADA. Lo obligatorio se comprueba igual y más abajo: que
            # TODA condición tenga estado, que ninguna tenga dos, que la suma dé trece, que
            # cada resumen coincida por IGUALDAD con su fila de detalle, y que ningún estado
            # que la sede canónica USE falte del resumen.
            continue
        _ini = _m.end()
        _sig = [_blq.find(e, _ini) for e in _ESTADOS_CL if _blq.find(e, _ini) > 0]
        _texto = _m.group(2) + " " + _blq[_ini: min(_sig) if _sig else len(_blq)]
        _ids = set(re.findall(r"\bC-L\.\d+\b", _texto))
        _declarado[_est] = int(_m.group(1))
        if _declarado[_est] != len(_ids):
            _g16c.append(f"«{_est}» declara {_m.group(1)} y nombra {len(_ids)} ids")
        for _x in _ids:
            _asig.setdefault(_x, []).append(_est)
        if re.search(r"\b[JKLMNO]-\d+\b", _m.group(2)):
            _g16c.append(f"«{_est}» cuenta un subhallazgo como condición: "
                         f"{re.findall(r'[JKLMNO]-[0-9]+', _m.group(2))}")

    _esperados = {f"C-L.{n}" for n in range(1, 14)}
    _faltan = sorted(_esperados - set(_asig), key=lambda x: int(x[4:]))
    _sobran = sorted(set(_asig) - _esperados)
    _dobles = sorted((k for k, v in _asig.items() if len(v) > 1), key=lambda x: int(x[4:]))
    if _faltan: _g16c.append(f"sin estado primario: {_faltan}")
    if _sobran: _g16c.append(f"ids que no son condiciones: {_sobran}")
    if _dobles: _g16c.append(f"con DOS estados primarios: {_dobles}")
    if sum(_declarado.values()) != len(_esperados):
        _g16c.append(f"la suma de los estados declara {sum(_declarado.values())} "
                     f"y las condiciones son {len(_esperados)}")

    # ── contraste contra la SEDE CANÓNICA: las trece filas de DETALLE ──────────
    # Sin esto, mover `C-L.12` de estado ajustando contadores pasaba en verde.
    _CANON = {
        "CORREGIDAS EN F4c":    ("CERRADA",),
        "NO CERRADA":           ("NO CERRADA",),
        "ABIERTA":              ("ABIERTA",),
        "REGISTRADAS PARA F5":  ("REGISTRADA PARA F5", "REGISTRADA"),
        "CONTRATADA PARA F6":   ("CONTRATADA PARA F6", "CONTRATADA"),
        "MIXTA POR DESGLOSE":   ("MIXTA",),
        "CERTIFICADA POR":      ("CERTIFICADA",),
    }
    _detalle = {}
    # el estado puede llevar dígitos —«REGISTRADA PARA F5», «CONTRATADA PARA F6»—, y una
    # clase que los excluya deja tres filas sin reconocer
    for _m in re.finditer(r"^\s*(C-L\.\d+)\s+([A-ZÁÉÍÓÚ][A-ZÁÉÍÓÚ0-9 ,]*?)(?:\s+·|\s*$)",
                          _vigente, re.M):
        _detalle.setdefault(_m.group(1), _m.group(2).strip())
    _sin_detalle = sorted(_esperados - set(_detalle), key=lambda x: int(x[4:]))
    if _sin_detalle:
        _g16c.append(f"sin fila de detalle en su sede: {_sin_detalle}")
    # y la dirección contraria: un estado que la SEDE CANÓNICA usa y que el resumen no
    # cuenta. Es la forma que tiene una condición de desaparecer del recuento sin
    # desaparecer del fichero.
    _INVERSO = {_d: _e for _e, _ds in _CANON.items() for _d in _ds}
    for _id, _det in sorted(_detalle.items()):
        _esp = _INVERSO.get(_det)
        if _id in _esperados and _esp and _esp not in _declarado:
            _g16c.append(f"{_id}: su fila de detalle dice «{_det}» y el resumen NO tiene "
                         f"línea «{_esp}»: un estado que la sede canónica usa y que el "
                         f"resumen no cuenta es una condición que no cuenta nadie")
    # `Q-06` · protección 3 del adjudicador. El contraste era `_det.startswith(a)`, y un
    # PREFIJO no es un estado: la fila de detalle vigente de `C-L.1` reescrita como
    # «CERRADA SOLO EN PARTE, SIGUE ABIERTA Y BLOQUEA F5 · D96 no cierra nada» seguía
    # empezando por «CERRADA» y se contaba entre las CORREGIDAS — con el árbol declarando
    # a la vez que la condición está cerrada y que sigue abierta y bloquea F5. La
    # comprobación se añadió EXACTAMENTE para cerrar la refutación 3 de `M-04`, y no la
    # cerraba. **Ahora se contrasta por IGUALDAD EXACTA del estado**, que es la única
    # comparación que ninguna calificación posterior puede invertir.
    for _id, _estados in _asig.items():
        _det = _detalle.get(_id)
        if not _det:
            continue
        _admitidos = _CANON.get(_estados[0], ())
        if not _estado_casa(_det, _admitidos):
            _g16c.append(f"{_id}: el resumen lo pone en «{_estados[0]}» y su fila de detalle "
                         f"dice «{_det}», que NO es ninguno de los estados admitidos "
                         f"{list(_admitidos)}. El contraste es por IGUALDAD, no por prefijo: "
                         f"una calificación añadida detrás cambia el estado")

    # ── `C-L.13`: sus componentes se DERIVAN de la fila de detalle, no de una lista ──
    _m13 = re.search(r"^\s*C-L\.13\s+.*?(?=^\s*C-L\.\d|\Z)", _vigente, re.M | re.S)
    _comp13 = sorted(set(re.findall(r"\b[JKL]-\d+\b", _m13.group(0)))) if _m13 else []
    if _asig.get("C-L.13") != ["MIXTA POR DESGLOSE"]:
        _g16c.append(f"`C-L.13` no está exactamente una vez como MIXTA: {_asig.get('C-L.13')}")
    if len(_comp13) < 2:
        _g16c.append("`C-L.13` no declara sus componentes en su fila de detalle")
    _b13 = _blq[_blq.find("MIXTA POR DESGLOSE"):]
    _falt13 = [c for c in _comp13 if c not in _b13]
    if _falt13:
        _g16c.append(f"el resumen de `C-L.13` omite componentes que su detalle declara: {_falt13}")
    if _comp13 and not re.search(rf"{_comp13[0] if 'J-11' not in _comp13 else 'J-11'}"
                                 r"[^\n]*(?:contratad|NO implementad)", _b13, re.I):
        if "J-11" in _comp13:
            _g16c.append("`J-11` no consta como contratado para F6 y no implementado")
    # Aquí había `if _asig.get("C-L.5") != ["CERTIFICADA POR"]`, y **se RETIRA**: era un
    # ESTADO ESCRITO A MANO dentro de la comprobación cuyo objeto es esa disciplina —la
    # clase `O-02`—, y ha caducado en cuanto el CUARTO GATE reabrió `C-L.5`. No aportaba
    # nada que no estuviera ya ejecutado dos bloques más arriba y de forma general: que
    # TODA condición tenga estado, que ninguna tenga DOS, que la suma dé trece, y que
    # **cada resumen coincida por IGUALDAD EXACTA con su fila de detalle**. Lo único que
    # añadía era exigir que el estado fuera uno concreto, que es justo lo que el instrumento
    # no puede decidir: la sede canónica de la clasificación es el checkpoint, no esto.
    # NO SE ABLANDA NADA: un estado fuera del canon, un prefijo del tipo «CERRADA SOLO EN
    # PARTE» y el borrado de la línea de resumen siguen dando ROJO los tres, por las tres
    # guardas generales de arriba.
    # `C-L.3` tiene que estar descrita por `D104` y NO por la regla que `M-01` refutó
    _m3 = re.search(r"^\s*C-L\.3\s+.*?(?=^\s*C-L\.\d|\Z)", _vigente, re.M | re.S)
    if not _m3 or "D104" not in _m3.group(0):
        _g16c.append("`C-L.3` vigente no nombra `D104`")
    if _m3 and re.search(r"cero o un par, nunca dos", _m3.group(0)):
        _g16c.append("`C-L.3` vigente conserva la regla de `D103` que `M-01` refutó")

_g16 = []
# el TAMAÑO de la matriz se DERIVA de la cabecera que la titula, y no se escribe (`Q-11`).
# `### Matriz de cierre de los N hallazgos distintos` es la sede que declara su cardinal;
# comparar contra un `43` literal era escribir a mano justo lo que se quiere contrastar.
_m_card43 = re.search(r"^#{1,6} .*Matriz de cierre de los\s+" + _NUM + r"\s+hallazgos",
                      tchk, re.M)
_card43 = _num(_m_card43.group(1)) if _m_card43 else None
if _card43 is None:
    _g16.append("la matriz de hallazgos no publica su cardinal en su propia cabecera "
                "«Matriz de cierre de los <n> hallazgos distintos», y sin sede no hay "
                "censo contra el que contrastar")
elif len(filas) != _card43 or len(set(ids)) != _card43:
    _g16.append(f"matriz: {len(filas)} filas / {len(set(ids))} ids, y su cabecera declara "
                f"{_card43}")
if dup:
    _g16.append(f"matriz: ids DUPLICADOS {dup}")
# ESTADO COMPUESTO en la matriz: se detecta sobre la línea ENTERA, no sobre el grupo
# capturado. El grupo está restringido a [A-Z_0-9]+ y nunca podía contener " y " ni "+":
# la comprobación anterior era código muerto y no podía disparar jamás (`M-11`).
_comp = re.findall(r"^\| `([A-Za-z0-9-]+)` \| (?:BLOQUEANTE|GRAVE|MEDIO|MENOR) \| "
                   r"\*\*`[A-Z_0-9]+`(?: y |\s*\+\s*)`?[A-Z_0-9]+", tchk, re.M)
if _comp:
    _g16.append(f"matriz: estados COMPUESTOS {_comp}")
_g16 += [f"condiciones C-L: {x}" for x in _g16c]

# El mensaje de éxito se DERIVA de lo comprobado. La versión anterior llevaba la cadena
# «8+2+1+1+1 = 13» codificada, y la imprimía intacta sobre un bloque que declaraba otra
# distribución (`O-02`).
#
# `BT-02` · **Y ARRASTRABA UN ESTADO ESCRITO A MANO EN LA MISMA LÍNEA**: el mensaje
# terminaba en el literal «C-L.5 CERTIFICADA», y `C-L.5` está ABIERTA desde el CUARTO GATE.
# La batería IMPRIMÍA en verde una afirmación FALSA sobre la condición que el gate acababa
# de reabrir, dentro de la comprobación cuyo objeto es que nadie copie estados. Es
# exactamente el defecto que el comentario de `C-L.5` de más arriba dice haber cerrado
# —allí se retiró la GUARDA escrita a mano y se dejó intacto el MENSAJE—: instancia
# corregida, clase abierta. Lo encontró el BARRIDO TRANSVERSAL de la tanda del quinto gate,
# y no lo señaló ninguno de los ocho participantes. **Ahora el estado se DERIVA de la sede
# canónica, como todo lo demás de esta línea.**
_resumen = "+".join(str(_declarado[e]) for e in _ESTADOS_CL if e in _declarado) \
           if not _g16c or _declarado else "?"
_cl5 = (_asig.get("C-L.5") or ["SIN ESTADO"])[0]
check("G-16",
      "un estado primario por elemento y ninguno compuesto: la matriz de hallazgos con el cardinal de su cabecera, y las condiciones `C-L` contra su detalle",
      not _g16,
      "; ".join(_g16) or
      f"matriz {len(filas)} filas / {len(set(ids))} ids · condiciones "
      f"{sum(_declarado.values())}/{len(_esperados)} con estado único, {_resumen} = "
      f"{sum(_declarado.values())}, cada resumen coincide con su fila de detalle · "
      f"C-L.13 MIXTA con {len(_comp13)} componentes derivados · "
      f"C-L.5 {_cl5}, DERIVADA de la sede y no escrita aquí")

# ── G-16b · A11 absorbido, A14 excluido ────────────────────────────
check("G-16b", "`A11` absorbido en `M-8` y `A14` excluido: ninguno es fila de la matriz",
      "A11" not in ids and "A14" not in ids,
      "ninguno aparece como fila")

# ── G-17 · recuentos DERIVADOS coinciden con lo publicado ──────────
est = Counter(f[2] for f in filas)
# `Q-11`. Aquí vivía un diccionario `esperado` con cinco cifras ESCRITAS A MANO — 31, 2, 2,
# 7, 1 — que **no lo leía nadie después**: `G-17` compara `pubv == derv`. Un censo manual
# muerto dentro de la comprobación cuyo objeto es que no haya censos manuales. Se retira.
pub = re.search(r"CORREGIDO_EN_F4\s+(\d+).*?PRESION_LISTA_PARA_F5\s+(\d+).*?"
                r"CONTRATO_COMPLETO_PARA_F6\s+(\d+).*?EXTERNO_CON_PROPIETARIO\s+(\d+).*?"
                r"HISTORICO_NO_APLICABLE\s+(\d+)", tchk, re.S)
pubv = [int(x) for x in pub.groups()] if pub else []
derv = [est["CORREGIDO_EN_F4"], est["PRESION_LISTA_PARA_F5"],
        est["CONTRATO_COMPLETO_PARA_F6"], est["EXTERNO_CON_PROPIETARIO"],
        est["HISTORICO_NO_APLICABLE"]]
# y la MATRIZ DE LOS 24 del gate del documento 21, con la misma disciplina: un id por
# fila, cada uno exactamente una vez, la severidad ADJUDICADA, y el recuento DERIVADO de
# las filas —no copiado— coincidiendo con el publicado. Ninguno puede declararse SUPERADO:
# corregido por quien lo recibió no es superado por revisión independiente.
_g17 = []
_m24 = re.findall(r"^\| \d+ \| `([A-Z]-\d+(?:≡[A-Z]-\d+)?)` \| \*\*(BLOQUEANTE|GRAVE|MEDIO|MENOR)\*\* \|(.*)$",
                  tchk, re.M)
if not _m24:
    _g17.append("no se encuentra la matriz de trazabilidad de los 24 hallazgos")
else:
    _ids24 = [a for a, _, _ in _m24]
    _dup24 = sorted(k for k, v in Counter(_ids24).items() if v > 1)
    if _dup24:
        _g17.append(f"matriz de los 24: ids duplicados {_dup24}")
    # el cardinal de esta matriz también se DERIVA de su cabecera (`Q-11`)
    _m_card24 = re.search(r"^#{1,6} .*Matriz de trazabilidad · los\s+" + _NUM
                          + r"\s+hallazgos", tchk, re.M)
    _card24 = _num(_m_card24.group(1)) if _m_card24 else None
    if _card24 is None:
        _g17.append("la matriz de trazabilidad no publica su cardinal en su cabecera "
                    "«Matriz de trazabilidad · los <n> hallazgos del documento 21»")
    elif len(_ids24) != _card24:
        _g17.append(f"matriz de trazabilidad: {len(_ids24)} filas y su cabecera declara "
                    f"{_card24}")
    _sev24 = Counter(b for _, b, _ in _m24)
    _der24 = [_sev24["BLOQUEANTE"], _sev24["GRAVE"], _sev24["MEDIO"], _sev24["MENOR"]]
    _pub24 = re.search(r"BLOQUEANTE\s+(\d+).*?GRAVE\s+(\d+).*?MEDIO\s+(\d+).*?MENOR\s+(\d+)",
                       tchk, re.S)
    if not _pub24:
        _g17.append("la matriz de los 24 no publica su recuento por severidad")
    elif [int(x) for x in _pub24.groups()] != _der24:
        _g17.append(f"matriz de los 24: publica {[int(x) for x in _pub24.groups()]} "
                    f"y las filas derivan {_der24}")
    _superados = [a for a, _, resto in _m24 if "SUPERAD" in resto.upper()]
    if _superados:
        _g17.append(f"matriz de los 24: se declaran SUPERADOS {_superados}, y quien aplica "
                    f"no certifica")
    _sin_estado = [a for a, _, resto in _m24 if "APLICADA, NO CERTIFICADA" not in resto]
    if _sin_estado:
        _g17.append(f"matriz de los 24: sin «APLICADA, NO CERTIFICADA» {_sin_estado}")

check("G-17", "los recuentos publicados coinciden con lo DERIVADO: la matriz de hallazgos y la de trazabilidad, con su cardinal leído de su cabecera",
      pubv == derv and _card43 is not None and sum(derv) == _card43 and not _g17,
      "; ".join(_g17) or
      f"derivado {derv} suma {sum(derv)} · publicado {pubv} · matriz de los 24: "
      f"{len(_m24)} ids únicos, severidades {_der24} = {sum(_der24)}")

# ── G-17b · atributos secundarios derivados ───────────────────────
f5 = [f[0] for f in filas if [c.strip() for c in f[3].split(" | ")][2] != "no"]
f6 = [f[0] for f in filas if [c.strip() for c in f[3].split(" | ")][3] != "no"]
check("G-17b", "requiere_f5 sube por `PN-14` y requiere_f6 conserva `F-01`",
      len(f5) == 3 and "F-01" in f5 and "F-01" in f6 and len(f6) == 11,
      f"F5={len(f5)} {f5} · F6={len(f6)}")

# ── G-18 · vallas Markdown balanceadas ────────────────────────────
desb = []
for p in (D11, DEC, CHK, IDX):
    n = sum(1 for l in lineas(p) if l.strip().startswith("```"))
    if n % 2: desb.append(f"{os.path.basename(p)}={n}")
check("G-18", "vallas Markdown balanceadas en los cuatro ficheros tocados",
      not desb, "; ".join(desb) or "todas pares")

# ── G-19 · cero parrafos duplicados introducidos ─────────────────
def dup_parrafos(p):
    txt = leer(p)
    trozos = [t.strip() for t in re.split(r"\n\s*\n", txt) if len(t.strip()) > 220]
    c = Counter(trozos)
    return [t[:70] for t, n in c.items() if n > 1]
dups = {os.path.basename(p): dup_parrafos(p) for p in (D11, DEC, CHK, IDX)}
malos = {k: v for k, v in dups.items() if v}
check("G-19", "cero parrafos largos duplicados en los cuatro ficheros",
      not malos, "; ".join(f"{k}: {v}" for k, v in malos.items()) or "ninguno")

# ── G-20 · el registro D sin hueco y sin repetir ─────────────────
#
# El tope se DERIVA de la última fila del registro, no se escribe: la versión anterior
# exigía literalmente `D1`-`D95` y fallaba en rojo el día que nacía `D96`, que es
# precisamente lo que el registro existe para permitir. Lo que hay que comprobar es que
# la serie sea CONTINUA y SIN REPETIR, no que se detenga en un número concreto.
ns = sorted(int(x) for x in re.findall(r"^\| D(\d+) ", leer(DEC), re.M))
_huecos = [i for i in range(1, ns[-1] + 1) if i not in ns] if ns else []
_reps = sorted(k for k, v in Counter(
    int(x) for x in re.findall(r"^\| D(\d+) ", leer(DEC), re.M)).items() if v > 1)
check("G-20", "el registro `D` es una serie CONTINUA desde `D1`, sin huecos y sin repetir",
      bool(ns) and not _huecos and not _reps,
      f"D1-D{ns[-1] if ns else '?'}, {len(ns)} filas, huecos {_huecos}, repetidas {_reps}")

# ── G-21 · O1-O16 intactas ───────────────────────────────────────
#
# `A1`. El cardinal que hacía de red —`len(set(ac)) >= len(set(ob))`— tampoco veía la
# desaparición, porque **el registro CRECE**: con dieciocho resoluciones vigentes y
# dieciséis en la base, borrar la fila `| O5 |` seguía cumpliendo `17 >= 16`. Se conserva,
# porque sigue cazando una amputación masiva, pero quien detecta el borrado de UNA fila es
# el contraste de arriba, que ahora sí mira lo que no está.
ob = re.findall(r"^\| O(\d+) \|", "\n".join(base), re.M)
ac = re.findall(r"^\| O(\d+) \|", leer(DEC), re.M)
difs = _filas_contra_base(sorted(set(ob), key=int), "O")
if _base_raw is None:
    difs.append("GIT NO RESPONDE: no se puede comparar contra `7e99388`")
elif not ob:
    difs.append("la base de `7e99388` no contiene ni una fila `| O`: lo que se ha traído no "
                "es el registro de resoluciones del Owner, y comparar contra nada da verde "
                "siempre")
# ── y la SEDE CANÓNICA del Owner, con su PROYECCIÓN, DESDE `O19` ─────────
#
# `X-03`, resuelto por el Owner en `O19`: la autoridad canónica deja de ser la paráfrasis
# del coordinador y pasa a `docs/owner/ADS-OWNER-RESOLUCIONES.md`. El registro de decisiones
# queda declarado **PROYECCIÓN DERIVADA**, y `O19` fija dos reglas que se pueden comprobar
# sin interpretar nada: **la proyección ENLAZA a la resolución canónica**, y **una paráfrasis
# nunca puede ampliar el texto canónico**.
#
# Esto NO es una comprobación nueva ni una protección de clase nueva: es `G-21` —la que ya
# custodia las resoluciones del Owner en el registro— mirando la sede que `O19` puso por
# encima del registro. Nada de aquí se escribe a mano:
#
#   · las resoluciones se DERIVAN de los encabezados `# `Onn`` de la sede
#   · desde qué resolución rige la regla se DERIVA de la propia sede —«esta sede nace por
#     `Onn`»—, no de un número escrito aquí: cuando nazca `O20` la regla la alcanza sola
#   · «no ampliar» se mide sobre las VALLAS de la proyección, que son la forma en que este
#     registro cita texto resolutivo: cada bloque tiene que estar LITERALMENTE en la sede
#
# Lo que NO mide, y se dice en el README: la prosa de la proyección no se compara palabra a
# palabra con la sede. Lo que se cierra es que una valla de la proyección diga algo que el
# texto canónico no dice, que es exactamente de lo que nació `O19`.
_REL_SEDE_OWNER = "docs/owner/ADS-OWNER-RESOLUCIONES.md"
_ENLACE_SEDE = "../owner/ADS-OWNER-RESOLUCIONES.md"
try:
    _t_sede = leer(os.path.join(RAIZ, _REL_SEDE_OWNER))
except SedeIlegible as _e:
    _t_sede = None
    difs.append(f"LA SEDE CANÓNICA `{_REL_SEDE_OWNER}` NO SE PUEDE LEER ({_e}). Desde `O19` "
                f"la autoridad de las resoluciones del Owner vive ahí y el registro es una "
                f"PROYECCIÓN DERIVADA: sin sede no hay nada contra lo que contrastar la "
                f"proyección, y darla por buena sería creer a la paráfrasis, que es "
                f"exactamente lo que `O19` retira")
if _t_sede is not None:
    _res_sede = re.findall(r"^# `(O\d+)`", _t_sede, re.M)
    _nace = re.findall(r"[Ee]sta sede nace por `(O(\d+))`", _t_sede)
    if not _res_sede:
        difs.append(f"la SEDE CANÓNICA no publica NI UN bloque `# `Onn``: una sede sin "
                    f"texto canónico no es autoridad de nada, y el sobre de ancla no "
                    f"tendría digest que anclar")
    _reps_sede = sorted(k for k, v in Counter(_res_sede).items() if v > 1)
    if _reps_sede:
        difs.append(f"la SEDE CANÓNICA declara DOS VECES {_reps_sede}: dos bloques con el "
                    f"mismo identificador son dos textos canónicos, y entonces no hay uno")
    if not _nace:
        difs.append("la SEDE CANÓNICA no declara POR QUÉ RESOLUCIÓN nace —«esta sede nace "
                    "por `Onn`»—, y ése es el dato del que se deriva desde cuándo rige la "
                    "regla de enlace. Sin él habría que escribir el número aquí, y un "
                    "número escrito caduca")
    _desde = int(_nace[0][1]) if _nace else None
    for _id in sorted(set(_res_sede), key=lambda s: int(s[1:])):
        _m_pro = re.search(r"^### `%s`(.*?)(?=^#{2,3} |\Z)" % _id, leer(DEC), re.S | re.M)
        if not _m_pro:
            difs.append(f"`{_id}` vive en la SEDE CANÓNICA y NO tiene proyección `### "
                        f"`{_id}`` en el registro de decisiones. `O19` ordena que toda "
                        f"resolución se materialice en la sede y DESPUÉS se proyecte: una "
                        f"resolución sin proyección no la lee nadie donde se trabaja")
            continue
        _pro = _m_pro.group(1)
        if _desde is not None and int(_id[1:]) >= _desde:
            if _ENLACE_SEDE not in _pro:
                difs.append(f"la proyección de `{_id}` NO ENLAZA a la sede canónica "
                            f"(`{_ENLACE_SEDE}`). Es la regla 4 de `O19`, y sin el enlace "
                            f"el lector del registro no tiene cómo llegar al texto que "
                            f"manda: vuelve a creer a la paráfrasis")
            for _valla in re.findall(r"^```[a-z]*\n(.*?)^```", _pro, re.S | re.M):
                if _valla not in _t_sede:
                    difs.append(
                        f"la proyección de `{_id}` cita en una VALLA un texto que NO está "
                        f"en la sede canónica: «{_valla.strip().splitlines()[0][:70]}…». "
                        f"UNA PARÁFRASIS NUNCA PUEDE AMPLIAR EL TEXTO CANÓNICO, y `O19` "
                        f"nació precisamente de una proyección que decía menos de lo que "
                        f"el Owner había resuelto")
check("G-21", "las resoluciones del Owner de `7e99388` siguen en el registro, y la SEDE CANÓNICA de `O19` manda sobre su proyección (falla CERRADO sin git y sin sede)",
      _base_raw is not None and bool(ob) and not difs and len(set(ac)) >= len(set(ob)),
      f"{len(set(ob))} resoluciones de la base presentes y con su texto; {len(set(ac))} "
      f"vigentes; sede canónica con {len(set(_res_sede))} resoluciones "
      f"({' · '.join(sorted(set(_res_sede), key=lambda s: int(s[1:])))}), cada una con "
      f"proyección, y las nacidas desde `O{_desde}` enlazan a la sede y no amplían su texto "
      f"en ninguna valla"
      if (_base_raw is not None and bool(ob) and not difs) else "; ".join(difs))

# ── el CORPUS GOBERNADO y su reparto, derivados una sola vez ─────────────
#
# Sede única de las tres cosas que varias comprobaciones necesitan y que antes cada una
# derivaba a su manera: qué ficheros gobierna esta batería, cuáles de ellos son INMUTABLES
# y cuáles están EN CORRECCIÓN. Escribirlo dos veces es crear la segunda sede que este
# corpus lleva doce tandas persiguiendo.
# ── `S1-01` · TODA LECTURA DE UNA LISTA DE RUTAS PASA POR AQUÍ, Y NO HAY OTRA VÍA ──────
#
# `EE-11` puso `-z` en TRES de las CUATRO lecturas de la batería y dejó `_tocados_raw` —de
# la que salen `tocados`, los `prohibidos` de `G-23`, `_kern`/`_kern_dir`/`_kern_ev` y el
# contraste de prosa del checkpoint— partiéndose por BLANCOS. El séptimo gate lo midió: un
# fichero con una letra castellana en su ruta llegaba al commit con **38/38** y `G-23`
# publicaba «6 ficheros … todos enumerados» sobre SIETE. **Instancia cerrada, clase
# abierta**, dentro del propio remedio que la cerraba.
#
# **Aquí se cierra la CLASE, y la forma de cerrarla es que no quede una segunda vía.**
# `_rutas_z()` es la ÚNICA lectura de listas de rutas de este fichero, y falla CERRADO ante
# todo lo que puede corromper una lista:
#
#   · SEPARACIÓN POR `NUL`, que ninguna ruta puede contener — inmune a espacios, saltos de
#     línea, tabuladores y a cualquier nombre adversarial
#   · `core.quotePath=false` FORZADO en la propia invocación, para que la salida no venga
#     citada y case byte a byte con la del disco. `git` cita por defecto lo no-ASCII, y esa
#     configuración es del ENTORNO de quien ejecuta: fijarla aquí es lo único que hace la
#     lectura independiente del `.gitconfig` del que corre
#   · DECODIFICACIÓN EXPLÍCITA en UTF-8 con `errors="strict"`: una ruta que no decodifique
#     no se interpreta a medias, se DENUNCIA
#   · ESTRUCTURA: si la salida no termina en `NUL` teniendo contenido, está TRUNCADA, y una
#     lista truncada es un universo encogido en silencio — que es la clase que este corpus
#     lleva cinco gates persiguiendo
#
# Cualquiera de esas condiciones deja constancia en `_LECTURAS_ROTAS`, y `G-00` la publica
# en ROJO. **Ninguna comprobación puede volver a partir por blancos la salida de git**: el
# control positivo `_lecturas_seguras()` de más abajo lo demuestra sobre este mismo fichero.
_LECTURAS_ROTAS = []


def _rutas_z(*args):
    """La ÚNICA lectura de una lista de rutas de git. Falla CERRADO (`S1-01`)."""
    try:
        r = subprocess.run(["git", "-C", RAIZ, "-c", "core.quotePath=false", *args, "-z"],
                           capture_output=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as e:
        _LECTURAS_ROTAS.append(f"`git {' '.join(args)} -z` no se pudo ejecutar ({e})")
        return None
    if r.returncode != 0:
        return None
    crudo = r.stdout
    if crudo and not crudo.endswith(b"\0"):
        _LECTURAS_ROTAS.append(
            f"`git {' '.join(args)} -z` devuelve una lista TRUNCADA: no termina en NUL. "
            f"Una lista truncada es un universo que encoge en silencio, y se falla cerrado")
        return None
    try:
        texto = crudo.decode("utf-8", errors="strict")
    except UnicodeDecodeError as e:
        _LECTURAS_ROTAS.append(
            f"`git {' '.join(args)} -z` devuelve una ruta que NO decodifica como UTF-8 "
            f"({e}). Una ruta que no se puede leer no se interpreta a medias: se denuncia")
        return None
    return set(x for x in texto.split("\0") if x)


def _lecturas_seguras():
    """¿Queda alguna lectura de git partida por blancos en este fichero? (`S1-01`)

    Se comprueba sobre el TEXTO de la propia batería: cualquier `_git(` cuya salida se
    parta con `.split()` es una lectura de la clase que el séptimo gate falsó. La única
    forma admitida de leer una lista de rutas es `_rutas_z()`.
    """
    try:
        yo = leer(os.path.abspath(__file__))
    except SedeIlegible as e:
        return [f"la batería no puede leerse a sí misma ({e}): sin eso, el barrido de "
                f"`S1-01` no se puede ejecutar y se falla cerrado"]
    malas = []
    for n, linea in enumerate(yo.split("\n"), 1):
        if re.search(r"_git\([^)]*\)\s*\.split\(\)", linea) or \
           re.search(r"_raw\s*\.split\(\)", linea):
            malas.append(f"L{n}: {linea.strip()[:90]}")
    return [f"lectura de git PARTIDA POR BLANCOS, que es la clase de `S1-01`: {m}"
            for m in malas]


_tocados_raw = _git("diff", "--name-only", "05f71b7")
tocados = sorted(_rutas_z("diff", "--name-only", "05f71b7") or [])
_mod_head_raw = _git("diff", "--name-only", "HEAD")
_mod_head = _rutas_z("diff", "--name-only", "HEAD") or set()
_base_arbol_raw = _git("ls-tree", "-r", "--name-only", "05f71b7")
_base_arbol = _rutas_z("ls-tree", "-r", "--name-only", "05f71b7") or set()
_head_arbol_raw = _git("ls-tree", "-r", "--name-only", "HEAD")
_head_arbol = _rutas_z("ls-tree", "-r", "--name-only", "HEAD") or set()

def _rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")

# ── el PERÍMETRO DE EXCLUSIÓN, y se excluye por lo que un fichero ES ─────
#
# `Z1-03`≡`Z-05`. Esto decía `(?:^|/)(?:\.git|__pycache__)(?:/|$)|\.pyc$`: excluía un
# DIRECTORIO POR SU NOMBRE, con el motivo escrito «los artefactos de bytecode, que no son
# fuente». Un directorio no es un artefacto de bytecode: admite cualquier cosa. El revisor
# `Z` puso dentro de `__pycache__` una copia **byte a byte** del material APROBADO, una
# segunda sede con su propio bloque `ads:proceso` y una copia del EMISOR DEL SOBRE, y la
# batería dio **38/38** —también con `git add -f`—. El comentario de `G-29` escribe la regla
# que esta línea incumplía: «una lista de lo que se excluye no puede caducar por omisión: lo
# que olvide nombrar se queda DENTRO».
#
# Se excluyó entonces por NATURALEZA: **el bytecode, por su extensión**, y `.git`, que no
# es corpus sino el almacén contra el que se compara. Un `.md` dentro de `__pycache__` es
# corpus, y `G-29` lo ve como lo que es: una ampliación sin clasificar.
#
# `DD-01` · **Y «POR SU EXTENSIÓN» NO ES «POR NATURALEZA», que era el argumento entero.**
# El adjudicador del QUINTO GATE plantó el octavo árbol: un documento que declara `F4c`
# cerrada y `F5` autorizada, nombrado `<algo>.pyc` bajo `docs/owner/`, **alcanzaba el
# commit**, dejaba `git status` vacío, pasaba **38/38** y **13/13**, no entraba en el
# universo, no recibía fila ni revisor, no aparecía en `EXCLUIDOS_IV` y **producía el
# digest del sobre bit a bit idéntico**. Y `.git` se excluía **por nombre y a cualquier
# profundidad**, con la poda evaluada sobre el NOMBRE DESNUDO del directorio.
#
# **Hoy los dos predicados son de verdad por naturaleza**, y son los mismos que el
# derivador aplica —una sola regla en los dos instrumentos, que es lo que `CC3` pidió:
#
#   · `.git` **ANCLADO A LA RAÍZ** de la ruta relativa, y la poda de `os.walk` evaluada
#     **sobre la RUTA COMPLETA**, no sobre el nombre desnudo, en TODAS sus sedes.
#   · el bytecode, **POR SU CONTENIDO**: cabecera de CPython y no-texto. El SUFIJO ya no
#     excluye nada.
#
# **Y lo que quede fuera se PUBLICA con su ruta**, en `EXCLUIDOS_PERIMETRO`, que `G-29`
# emite en su detalle. Una exclusión silenciosa es la puerta por la que entró el octavo
# árbol; una exclusión publicada es una línea que el revisor lee.
_EXCLUIDO_RAIZ = re.compile(r"^\.git(?:/|$)")

# Lo que queda fuera del perímetro, con su ruta y su motivo. Se publica, no se supone.
EXCLUIDOS_PERIMETRO = []


def _es_bytecode(ruta_abs):
    """¿El fichero cumple el PREDICADO DE BYTECODE? Por CONTENIDO, no por sufijo (`DD-01`).

    EL PREDICADO, dicho como se ejecuta: bytes 3 y 4 iguales a `\r\n`, byte 2 menor que
    `0x20`, y contenido que **no decodifica como UTF-8**. `S1-05`: la versión anterior
    prometía además que un documento «no puede fabricarse para parecerlo sin dejar de ser
    legible», y es FALSO Y MEDIDO —un documento en Latin-1 lo satisface y se lee sin
    problema—. La imposibilidad se retira. **Ésta es una GEMELA de la del derivador y se
    conserva a propósito**: los dos instrumentos tienen que poder juzgar el perímetro sin
    importarse el uno al otro, que es lo que `O18` pide de una raíz externa. Lo que NO se
    admite es que divergan, y por eso las dos publican el mismo predicado escrito igual.
    """
    try:
        with io.open(ruta_abs, "rb") as fh:
            cabecera = fh.read(4)
            resto = fh.read(65536)
    except OSError:
        return False
    if len(cabecera) < 4 or cabecera[2:4] != b"\r\n" or cabecera[1] > 0x1F:
        return False
    try:
        (cabecera + resto).decode("utf-8")
    except UnicodeDecodeError:
        return True
    return False


def _en_zona(rel):
    """¿`rel` cae dentro del corpus gobernado? Todo, salvo lo excluido CON MOTIVO y CON RUTA."""
    if _EXCLUIDO_RAIZ.match(rel):
        motivo = "`.git` de la RAÍZ: almacén, no corpus"
    elif _es_bytecode(os.path.join(RAIZ, rel)):
        motivo = ("cumple el PREDICADO DE BYTECODE por CONTENIDO; NO se afirma que sea "
                  "bytecode de CPython (`S1-05`)")
    else:
        return True
    if (rel, motivo) not in EXCLUIDOS_PERIMETRO:
        EXCLUIDOS_PERIMETRO.append((rel, motivo))
    return False


def _podar(base, dirs):
    """Poda de `os.walk` sobre la RUTA COMPLETA, nunca sobre el nombre desnudo (`DD-01`)."""
    vivos = []
    for d in dirs:
        rel = _rel(os.path.join(base, d))
        if _EXCLUIDO_RAIZ.match(rel):
            par = (rel + "/", "`.git` de la RAÍZ: almacén, no corpus")
            if par not in EXCLUIDOS_PERIMETRO:
                EXCLUIDOS_PERIMETRO.append(par)
            continue
        vivos.append(d)
    dirs[:] = vivos

# Los ficheros EN CORRECCIÓN son los que esta batería declara como objeto de la tanda, y
# ya los declaraba: son los mismos cuatro que `G-18` y `G-19` recorren. No se escribe una
# segunda lista.
_EN_CORRECCION = frozenset(_rel(p) for p in (D11, DEC, CHK, IDX))

# ── G-22 · el rango INMUTABLE se DERIVA del árbol, y no se escribe ───────
#
# Protecciones 1 y 7. La versión anterior decía `re.search(r"docs/evolucion/1[5-8]-", f)`,
# un rango ESCRITO: cuando nacieron los documentos 19, 20, 21 y 22 quedaron fuera sin que
# nada lo dijera, y el adjudicador **volteó los veredictos de los documentos 19, 20 y 21 a
# `SUFICIENTE PARA F5` con la batería en 30/30 verde**. Es `Q-26`. Un rango escrito vuelve
# a caducar con el documento 23, y la corrección que sólo añadiera «19, 20, 21, 22» habría
# repetido exactamente el defecto que este gate castiga: arreglar el perímetro del
# contraejemplo y ninguna otra parte.
#
# Aquí el inventario se DERIVA: es **todo documento numerado de `docs/evolucion/` más todo
# manifiesto de gate**, MENOS los ficheros que la batería declara en corrección. El
# documento 23 nace inmutable el día que se confirma, sin tocar una línea de esto.
#
# Y el contraste es DOBLE, que es lo que `Q-23` pedía: contra `HEAD` —lo que caza cualquier
# edición del árbol de trabajo— y contra la revisión base para los que ya existían en ella
# —lo que caza una edición confirmada—. Sin Git, falla CERRADO.
def _inmutables():
    salida = []
    dir_ev = os.path.join(RAIZ, "docs/evolucion")
    for nombre in sorted(os.listdir(dir_ev)):
        if re.match(r"^\d\d-.*\.md$", nombre):
            rel = "docs/evolucion/" + nombre
            if rel not in _EN_CORRECCION:
                salida.append(rel)
    dir_man = os.path.join(dir_ev, "verificacion/manifiestos")
    if os.path.isdir(dir_man):
        for nombre in sorted(os.listdir(dir_man)):
            salida.append("docs/evolucion/verificacion/manifiestos/" + nombre)
    # `O19`. **`docs/owner/` entra en ESTE inventario**, que es el que ya existe: mismo id,
    # mismo doble contraste contra `HEAD` y contra la revisión base, mismo perímetro DERIVADO
    # del árbol. NO se escribe una protección nueva —el Owner lo prohíbe expresamente— sino
    # que se extiende el inventario de integridad a la zona que su resolución convierte en
    # AUTORIDAD CANÓNICA: material del Owner, que **no puede alterarse en silencio**. Hasta
    # aquí ninguna comprobación miraba el contenido de `docs/owner/`: `G-29` veía si nacía o
    # desaparecía un fichero, y editar el texto de una resolución suya no lo veía nadie.
    # Se barre el DIRECTORIO ENTERO y no `*.md`: un fichero de otra extensión que naciera
    # ahí quedaría fuera sin que nada lo dijera, que es la clase de perímetro escrito que
    # este corpus lleva cuatro gates persiguiendo.
    dir_own = os.path.join(RAIZ, "docs/owner")
    # `Z1-07`. Este barrido saltaba los nombres que empiezan por punto —directorios y
    # ficheros— y volvía a ser un perímetro escrito: `docs/owner/.RESOLUCIONES.md` quedaba
    # fuera del inventario sin que nada lo dijera. Se excluye por lo mismo que en todas las
    # demás sedes de esta batería, `_EXCLUIDO`: bytecode y `.git`, y nada más.
    for base, dirs, ficheros in os.walk(dir_own):
        _podar(base, dirs)
        for nombre in sorted(ficheros):
            rel = _rel(os.path.join(base, nombre))
            if _en_zona(rel) and rel not in _EN_CORRECCION:
                salida.append(rel)
    return salida

_INMUTABLES = _inmutables()
# `T-05`. La guarda de BASE VACÍA que `G-11b` ya tenía escrita, y que faltaba aquí.
# `_git()` devuelve `None` sólo si el comando FALLA; un `git ls-tree HEAD` que sale con
# ÉXITO y sin stdout devuelve la cadena vacía, `_head_arbol` queda vacío, y el bucle se
# salta con `continue` los veintiséis inmutables uno a uno **listándolos en el detalle**
# mientras imprime `OK`. Es `M-12` —«interpretaban el vacío como “nada cambió”»—
# sobreviviendo en la comprobación cuyo título dice «falla CERRADO sin git».
def _base_vacia(bruto, comando, para_que):
    """El diagnóstico si `bruto` vino VACÍO CON ÉXITO, o None. `G-11b`, generalizada."""
    if bruto is not None and not bruto.strip():
        return (f"`{comando}` responde con ÉXITO y VACÍO: {para_que}. Comparar contra nada "
                f"da verde siempre, y eso no es comparar")
    return None

_g22, _sin_base = [], []
if _tocados_raw is None or _mod_head_raw is None or _head_arbol_raw is None:
    _g22.append("GIT NO RESPONDE: no se puede saber qué documentos históricos se han tocado")
else:
    for _b, _c, _q in ((_head_arbol_raw, "git ls-tree -r --name-only HEAD",
                        "no hay árbol publicado con el que contrastar los inmutables"),
                       (_base_arbol_raw, "git ls-tree -r --name-only 05f71b7",
                        "no hay revisión base con la que contrastar los inmutables")):
        _d = _base_vacia(_b, _c, _q)
        if _d:
            _g22.append(_d)
    if not _INMUTABLES:
        _g22.append("el inventario de inmutables sale VACÍO: el barrido no ve el corpus, y "
                    "un rango vacío por no mirar es un verde por omisión")
    if not any(f.startswith("docs/evolucion/verificacion/manifiestos/") for f in _INMUTABLES):
        _g22.append("ningún manifiesto de gate entra en el inventario de inmutables")
    if not any(f.startswith("docs/owner/") for f in _INMUTABLES):
        _g22.append("NINGÚN fichero de `docs/owner/` entra en el inventario de inmutables: "
                    "desde `O19` esa zona es la SEDE CANÓNICA de las resoluciones del Owner, "
                    "y un inventario que no la ve deja que su texto se altere en silencio")
    # `H-11`. La REGLA es de `O19`, que es quien CREA `docs/owner/` y le da su contrato;
    # la tanda de `O20` es sólo la OCASIÓN en que este inventario se corrigió. Rotularlo
    # «`O20`» atribuía a una resolución una regla que no dictó, y este fichero se lee como
    # sede: quien buscara el origen del append-only habría ido al bloque equivocado.
    # **La SEDE DEL OWNER es APPEND-ONLY, no byte-inmutable, y la diferencia
    # importa.** Este inventario la trataba como un documento histórico —idéntica a `HEAD`—
    # y con eso **el corpus no podía registrar una resolución nueva del Owner**: el
    # procedimiento que `O19` prescribe —materializar en la sede y después proyectar— ponía
    # el instrumento en ROJO. Un instrumento que impide ejercer la regla que dice guardar es
    # una afirmación falsa sobre sí mismo, y es la sexta condición de `O18`.
    # **La propiedad correcta de esa zona ya la comprueba `G-29`**: su contenido de hoy
    # tiene que EMPEZAR POR el de la versión que la creó, contrastado contra el commit del
    # nacimiento y no contra `HEAD`, de modo que **añadir una resolución es legítimo y
    # alterar una letra de lo publicado sigue siendo ROJO**. Aquí se retira el contraste
    # byte a byte y se REMITE a esa guarda, que es más fuerte y no depende de `HEAD`.
    _APPEND_ONLY = "docs/owner/"
    for rel in _INMUTABLES:
        if rel not in _head_arbol:
            _sin_base.append(rel)          # documento en curso, todavía sin confirmar
            continue
        if rel.startswith(_APPEND_ONLY):
            continue                       # APPEND-ONLY · lo juzga `G-29`, contra el nacimiento
        if rel in _mod_head:
            _g22.append(f"{rel}: MODIFICADO en el árbol de trabajo respecto de `HEAD`. Es "
                        f"un documento histórico y no se reescribe; quien lo cambie es "
                        f"quien tiene que responder de ello")
        if rel in _base_arbol and rel in tocados:
            _g22.append(f"{rel}: MODIFICADO respecto de la revisión base `05f71b7`, y ya "
                        f"existía en ella")
    _g22_ow = sorted(f for f in _INMUTABLES if f.startswith(_APPEND_ONLY))
    # y el segundo brazo se DECLARA: `T-02` mostró que ocho de los inmutables no existen en
    # `05f71b7`, con lo que su contraste contra la base no se ejecuta para ellos. Eso no es
    # un defecto —nacieron después— pero callarlo sí lo era: el detalle lo dice.
    _sin_base_rev = [f for f in _INMUTABLES if f in _head_arbol and f not in _base_arbol]
check("G-22",
      "los documentos históricos y los manifiestos de gate, DERIVADOS del árbol, están intactos (falla CERRADO sin git)",
      not _g22,
      "; ".join(_g22) or
      f"{len(_INMUTABLES)} inmutables derivados —{len([f for f in _INMUTABLES if '/manifiestos/' in f])} "
      f"manifiestos, {len([f for f in _INMUTABLES if f.startswith('docs/owner/')])} de la "
      f"SEDE DEL OWNER y "
      f"{len([f for f in _INMUTABLES if '/manifiestos/' not in f and not f.startswith('docs/owner/')])} "
      f"documentos numerados— intactos frente a `HEAD` y a `05f71b7`" +
      f" · de ellos, {len(_g22_ow)} de `docs/owner/` se juzgan APPEND-ONLY y NO byte a byte "
      f"(`O19`, que crea la sede con ese contrato): lo comprueba `G-29` contra el COMMIT "
      f"QUE LOS CREÓ, que es más "
      f"fuerte que contra `HEAD` y permite registrar una resolución nueva del Owner sin "
      f"poner el instrumento en rojo" +
      # `AA-03`. La exención de los cuatro ficheros EN CORRECCIÓN no se decía en ninguna
      # parte, y `00-INDICE.md` es uno de ellos: es **la sede que gobierna qué se admite en
      # `docs/owner/` y qué documento numerado nuevo se admite**, y editarla sola daba
      # `38/38`. La exención es legítima —son el objeto de la tanda, y `G-18` y `G-19` los
      # recorren— pero callarla no lo era. Se NOMBRA, para que quien lea el informe sepa
      # qué NO se ha contrastado. Que además CADUQUE, como caduca la de `G-34`, es una
      # decisión de la tanda que la declara y no del instrumento.
      f" · {len(_EN_CORRECCION)} EXENTOS y NOMBRADOS, por ser el objeto declarado de esta "
      f"tanda —`00-INDICE.md` entre ellos, que es la sede que gobierna la ADMISIÓN—: "
      f"{sorted(_EN_CORRECCION)}" +
      (f" · {len(_sin_base)} todavía sin confirmar y por tanto sin línea base: "
       f"{_sin_base}" if _sin_base else "") +
      (f" · {len(_sin_base_rev)} nacidos DESPUÉS de `05f71b7` y contrastados sólo contra "
       f"`HEAD`" if _g22 == [] and _sin_base_rev else ""))

# ── G-23 · lo normativo intacto, y el kernel con su EXCEPCIÓN NOMBRADA ──
#
# La versión anterior afirmaba «`kernel/operativo/` intacto» y excluía en bloque todo
# `pruebas/evidencia/`. Dejó de ser cierta en `1b588ac`, que corrigió `comprobar_negativos.py`
# para hacer `N158g` independiente del orden del runner, y reancló `.upstream-hash` porque la
# huella cubre el código de los validadores.
#
# Se sustituye la afirmación falsa por la comprobación EXACTA: lo normativo sigue intacto, el
# kernel operativo SUSTANTIVO sigue intacto, y la única excepción de código es la que se
# nombra. Una exclusión amplia volvería a dejar pasar cualquier otro cambio del kernel, que es
# justo lo que esta comprobación existe para impedir.
# `DD-04` · **«LO NORMATIVO INTACTO» SOBRE UN PERÍMETRO ENUMERADO, y era falso.**
# Aquí vivía un regex de SEIS patrones escritos a mano que cubría **4 de los 14 ficheros
# de `docs/rediseno/`**, la zona que el `00-INDICE` declara ESPECIFICACIÓN NORMATIVA
# VIGENTE. El adjudicador del quinto gate lo midió con su control positivo: `00-MAPA.md`
# reescrito **declarando que prevalece sobre el material APROBADO y que deja `O17`, `O18`
# y `O19` sin efecto** daba **38/38 VERDE**; el mismo texto en `a-CAPACIDADES-APROBADA.md`
# daba `37/38 FALLO G-23`. Diez ficheros normativos sin guardia, y la comprobación
# imprimiendo «lo normativo intacto».
#
# **Se DERIVA, como `G-23` ya hace con el kernel:** la zona entera es normativa, y las
# excepciones se NOMBRAN una a una con su motivo. Lo que queda enumerado no es el
# perímetro —que es el conjunto de ficheros del árbol— sino su EXCEPCIÓN, que es lo único
# que una lista puede decir sin caducar por omisión. Un fichero nuevo en `docs/rediseno/`
# nace protegido; con el regex nacía libre.
_ZONA_NORMATIVA = "docs/rediseno/"
DOC_REDISENO_AUTORIZADO = {"docs/rediseno/CHECKPOINT-OPERATIVO.md"}
# `S1-02`. La guarda de MUTACIÓN alcanza el corpus entero, y con ella apareció una
# mutación legítima que hasta hoy **no estaba guardada por nadie**: `G-23` sólo mira
# `kernel/`, y `tooling/` quedaba fuera de toda comprobación de contenido. Se NOMBRA con su
# motivo, como todas las demás excepciones, y no se abre ningún comodín sobre `tooling/`:
#
#   `tooling/new-project.sh` — la tanda de `O19` (`dc9be3f`) le añadió la copia de
#   `docs/owner/ADS-OWNER-RESOLUCIONES.md` al proyecto que crea. Es propagación DERIVADA
#   de `O19`: desde esa resolución la sede canónica es especificación normativa, el
#   registro de decisiones ENLAZA a ella, y sin copiarla el proyecto instalado queda con un
#   enlace roto — lo detectó `T148` en cuanto la sede existió. No es una decisión de una
#   tanda: es la resolución del Owner propagada al instalador.
TOOLING_AUTORIZADO = {"tooling/new-project.sh"}
NORMATIVO = (r"kernel/operativo/contratos/C4-MATERIALIZACION|"
             r"kernel/operativo/contratos/C7-GOBIERNO")


def _normativo_no_autorizado(f):
    """¿`f` es material normativo tocado sin autorización? Zona DERIVADA, excepción NOMBRADA."""
    if re.search(NORMATIVO, f):
        return True
    if not f.startswith(_ZONA_NORMATIVA):
        return False
    # Las excepciones, NOMBRADAS una a una y con su motivo, exactamente como `G-23` las
    # nombra para el kernel. Lo que NO se enumera es el perímetro: ése se deriva del árbol.
    #
    #   · el registro de decisiones — objeto declarado de esta tanda, ya en
    #     `_EN_CORRECCION`, y que `G-18`, `G-19` y `G-22` recorren y nombran. No se
    #     escribe aquí una segunda vez: sería una segunda sede.
    #   · `CHECKPOINT-OPERATIVO.md` — es el checkpoint DERIVADO del kernel operativo, no
    #     material APROBADO: lo tocó `Q-15` del documento 22 para que el censo de
    #     validadores dejara de escribirse a mano, en `55d8ce1`. Se nombra con su motivo,
    #     que es lo que una excepción tiene que llevar para no ser un comodín.
    if f in _EN_CORRECCION or f in DOC_REDISENO_AUTORIZADO:
        return False
    return True

# Excepciones AUTORIZADAS, una a una. No hay comodines sobre directorios de código.
#
# `entrada/02-CIRCUITO.md` entra por la corrección del gate definitivo (`K-09`, MENOR):
# su L54 citaba `04-CONFIRMACION.md`, que NO existe — el fichero es
# `04-INCERTIDUMBRE-Y-CONFIRMACION.md`. Es un enlace colgante y su remedio es de una línea.
# Se nombra AQUÍ, fichero a fichero, y no se abre ningún comodín sobre `entrada/`: la
# comprobación tiene que seguir cazando cualquier otro cambio del kernel.
COD_AUTORIZADO = {"kernel/operativo/validadores/comprobar_negativos.py"}
DOC_AUTORIZADO = {"kernel/operativo/entrada/02-CIRCUITO.md"}
HUELLA         = {"kernel/.upstream-hash"}

def _kernel_no_autorizado(f):
    if not f.startswith("kernel/"):
        return False
    if f in COD_AUTORIZADO or f in DOC_AUTORIZADO or f in HUELLA:
        return False
    # la evidencia derivada SÍ puede cambiar: la publica el runner, no una mano
    if f.startswith("kernel/operativo/pruebas/evidencia/"):
        return False
    return True

prohibidos = [f for f in tocados if _kernel_no_autorizado(f)]
prohibidos += [f for f in tocados if _normativo_no_autorizado(f)]
# El censo de la zona normativa se DERIVA del árbol y se publica: quien lea el detalle ve
# cuántos ficheros protege esta comprobación, y no tiene que creerse un cardinal escrito.
_ZONA_NORM_ARBOL = sorted(f for f in _head_arbol if f.startswith(_ZONA_NORMATIVA)) \
    if _head_arbol_raw is not None else []
if _head_arbol_raw is not None and not _ZONA_NORM_ARBOL:
    prohibidos.append("`git ls-tree -r HEAD docs/rediseno/` no devuelve ningún fichero: la "
                      "ESPECIFICACIÓN NORMATIVA no está en el commit, y un perímetro vacío "
                      "se satisface por omisión")
# ── y la PROSA del checkpoint contrastada contra lo que Git deriva ────────
#
# Añadido por la verificación previa a publicación. El bloque «EXCEPCIÓN EXACTA DEL
# KERNEL» del checkpoint enumeraba la lista A MANO, y envejeció dos veces: primero
# decía «y sólo ésta» sobre TRES ficheros omitiendo `entrada/02-CIRCUITO.md` (`M-06`),
# y su corrección dijo «CUATRO rutas más la evidencia derivada» enumerando cuatro
# entradas de las cuales la cuarta ERA la evidencia — contándola dentro y fuera, y
# llamando «ruta» a una categoría junto a tres ficheros.
#
# Ahora la lista se CONTRASTA contra `git diff -- kernel/`: si el conjunto cambia y la
# prosa no, esto se pone en rojo. No hay ninguna cifra escrita aquí.
_kern = sorted(f for f in tocados if f.startswith("kernel/"))
_kern_ev = [f for f in _kern if "/pruebas/evidencia/" in f]
_kern_dir = [f for f in _kern if f not in _kern_ev]
_i_exc = tchk.find("EXCEPCIÓN EXACTA")
if _i_exc < 0:
    prohibidos.append("el checkpoint no declara la excepción exacta del kernel")
elif _tocados_raw is not None:
    # el bloque llega hasta la SIGUIENTE etiqueta de campo en columna 0, no hasta la
    # primera línea en blanco: el bloque tiene líneas en blanco dentro
    # la etiqueta del campo ocupa DOS líneas —«EXCEPCIÓN EXACTA / DEL KERNEL»—, luego se
    # busca la siguiente a partir de 200 caracteres, y no desde el principio
    _m_fin = re.search(r"^[A-ZÁÉÍÓÚ][A-ZÁÉÍÓÚ ]{4,}\s{2,}\S", tchk[_i_exc + 200:], re.M)
    _blq_exc = tchk[_i_exc: _i_exc + 200 + (_m_fin.start() if _m_fin else 4000)]
    # sólo se consideran RUTAS DE FICHERO: el último segmento tiene extensión. Una
    # mención en prosa a un directorio —«`kernel/operativo/` está intacto»— no es una
    # entrada del recuento y no debe contarse como sobrante.
    _listados = {f for f in re.findall(r"kernel/[A-Za-z0-9_./-]+", _blq_exc)
                 if "." in f.rsplit("/", 1)[-1]}
    _faltan_exc = [f for f in _kern if f not in _listados]
    _sobran_exc = [f for f in _listados if f not in _kern]
    if _faltan_exc:
        prohibidos.append(f"el checkpoint NO enumera ficheros del kernel tocados: {_faltan_exc}")
    if _sobran_exc:
        prohibidos.append(f"el checkpoint enumera ficheros que no se han tocado: {_sobran_exc}")
    # los recuentos publicados, contrastados contra lo derivado
    for _pat, _real, _que in (
        (r"TOTAL (\d+) = (\d+) directos \+ (\d+) de evidencia derivada",
         (len(_kern), len(_kern_dir), len(_kern_ev)), "total/directos/evidencia"),):
        _m = re.search(_pat, _blq_exc)
        if not _m:
            prohibidos.append("el checkpoint no publica el recuento «TOTAL n = n directos + n de evidencia derivada»")
        elif tuple(int(g) for g in _m.groups()) != _real:
            prohibidos.append(f"el checkpoint publica {_m.groups()} y Git deriva {_real} ({_que})")
    # ninguna categoría contada como fichero. Una CITA de la formulación vieja —entre
    # comillas angulares, para decir que era incorrecta— no es una afirmación viva: es la
    # misma distinción que `G-26` hace entre sede vigente y cita histórica.
    for _m_cat in re.finditer(r"(?:CUATRO|CINCO|SEIS|TRES) rutas más la evidencia", _blq_exc):
        _lin_ini = _blq_exc.rfind("\n", 0, _m_cat.start()) + 1
        _lin_fin = _blq_exc.find("\n", _m_cat.end())
        _lin = _blq_exc[_lin_ini: _lin_fin if _lin_fin > 0 else len(_blq_exc)]
        _dentro = any(c.start() <= _m_cat.start() - _lin_ini <= c.end()
                      for c in re.finditer(r"«[^»]*»", _lin))
        if not _dentro:
            prohibidos.append("el checkpoint cuenta la evidencia dentro de las rutas "
                              "Y otra vez fuera")

# La TOPOLOGÍA del árbol y la UNICIDAD de las fuentes canónicas vivían aquí, y **sólo para
# `kernel/`**. Se han mudado a `G-29`, que las aplica a TODO el corpus gobernado: el
# adjudicador movió el ataque de `Q-04` un directorio afuera —a `docs/rediseno/`, sobre
# material APROBADO— y volvió a dar 30/30 en verde. Una comprobación que existe para
# impedir la segunda sede de una verdad no puede tener ella misma dos sedes, así que aquí
# no queda copia: `G-29` es la única.

# ── y el PUNTO DE ENTRADA no reproduce la excepción: REMITE ───────────────
#
# `R-02`. La sección «Siguiente acción exacta» —la que la cabecera del checkpoint designa
# como punto de entrada de un agente sin contexto— llevaba su PROPIA copia de la excepción
# del kernel, con TRES ficheros, mientras la sede derivada enumeraba SEIS. Es `M-06`
# reproducido en la misma tanda que lo declaraba corregido. Una lista copiada envejece sola:
# aquí se exige que esa sección REMITA a la sede derivada en vez de copiarla.
_i_sig = tchk.find("## Siguiente acción exacta")
if _i_sig < 0:
    prohibidos.append("el checkpoint no tiene sección «Siguiente acción exacta»")
else:
    _sig = tchk[_i_sig:]
    _rutas_sig = {f for f in re.findall(r"kernel/[A-Za-z0-9_./-]+", _sig)
                  if "." in f.rsplit("/", 1)[-1]}
    if _rutas_sig:
        prohibidos.append(f"«Siguiente acción exacta» copia rutas del kernel en vez de "
                          f"remitir a la sede derivada: {sorted(_rutas_sig)}")
    if "EXCEPCIÓN EXACTA" not in _sig:
        prohibidos.append("«Siguiente acción exacta» no remite al campo «EXCEPCIÓN EXACTA "
                          "DEL KERNEL», que es la sede derivada")

if _tocados_raw is None:
    prohibidos.append("GIT NO RESPONDE: no se puede saber qué se tocó")
check("G-23", "lo normativo intacto y la excepción del kernel contrastada contra la prosa del checkpoint (falla CERRADO sin git)",
      _tocados_raw is not None and not prohibidos,
      f"{len(_kern)} ficheros de kernel = {len(_kern_dir)} directos + {len(_kern_ev)} de "
      f"evidencia derivada, todos enumerados en el checkpoint · ZONA NORMATIVA DERIVADA "
      f"(`DD-04`): {len(_ZONA_NORM_ARBOL)} ficheros de `docs/rediseno/` en `HEAD`, la zona "
      f"ENTERA protegida y no un regex de seis patrones, con "
      f"{len([f for f in _EN_CORRECCION if f.startswith(_ZONA_NORMATIVA)]) + len(DOC_REDISENO_AUTORIZADO)} "
      f"excepción(es) NOMBRADA(S) con su motivo: "
      f"{sorted(set(f for f in _EN_CORRECCION if f.startswith(_ZONA_NORMATIVA)) | DOC_REDISENO_AUTORIZADO)}"
      if (_tocados_raw is not None and not prohibidos) else ", ".join(sorted(set(prohibidos))))

# ── G-24 · las catorce fuentes y las quince fichas existen ──────
fuentes = """kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md
kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md
kernel/operativo/diseno/02-RUBRICAS.md
kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md
kernel/operativo/diseno/05-FIDELIDAD.md
kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md
kernel/operativo/contratos/C3-METODO-EJECUTABLE.md
kernel/operativo/contratos/C4-MATERIALIZACION.md
kernel/operativo/entrada/00-INDICE.md
kernel/operativo/entrada/02-CIRCUITO.md
kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md
docs/rediseno/a-ENMIENDA-E1-ENC.md
docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md
docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md""".split("\n")
# «legibles» tiene que significar LEÍDAS, y «quince fichas» tiene que significar ESTAS
# quince. La versión anterior comprobaba `os.path.exists` y `len(fichas) == 15`: con eso,
# una ficha sustituida por otra, renombrada o ilegible pasaba en verde, y quince
# directorios cualesquiera contaban como el catálogo. Aquí se comparan los NOMBRES exactos
# y se ABRE cada fichero en UTF-8.
CAPACIDADES = ["APR", "ARQ", "CON", "DIS", "DOM", "DSP", "ENC", "ENT",
               "INV", "PLT", "PRD", "SEG", "SIS", "USO", "VER"]

# `T-19`. Aquí vivía `_ilegible()`, que era `_motivo_ilegible()` escrita por segunda vez y
# DIVERGENTE —no capturaba `IsADirectoryError`—: una segunda sede de la misma derivación
# dentro de la batería que persigue las segundas sedes. Se usa la única que hay.
problemas = []
for f in fuentes:
    motivo = _motivo_ilegible(os.path.join(RAIZ, f))
    if motivo:
        problemas.append(f"{f}: {motivo}")

# `T-16`. `Q-27` prometió derivar el catálogo de capacidades UNA SOLA VEZ y compartirlo
# entre `G-15` y `G-24`, y el README lo daba por corregido; `G-24` seguía recomputándolo
# sobre su propia constante `_dir_cap`. Dos sedes de la misma derivación. Se usa la única.
_dir_cap = _DIR_CAPS
presentes = list(_CAPS_DIRS)
sobran = [d for d in presentes if d not in CAPACIDADES]
ausentes = [c for c in CAPACIDADES if c not in presentes]
if ausentes:
    problemas.append("faltan capacidades: " + ", ".join(ausentes))
if sobran:
    problemas.append("capacidades no declaradas: " + ", ".join(sobran))

for c in CAPACIDADES:
    if c in presentes:
        motivo = _motivo_ilegible(os.path.join(_dir_cap, c, "CAPACIDAD.md"))
        if motivo:
            problemas.append(f"{c}/CAPACIDAD.md: {motivo}")

check("G-24", "las CATORCE fuentes y las QUINCE fichas se LEEN, y son EXACTAMENTE ésas",
      not problemas,
      f"{len(fuentes)} fuentes leídas · {len(CAPACIDADES)} fichas leídas, "
      f"nombre a nombre" if not problemas else "; ".join(problemas))

# ── G-25 · CATORCE campos en los cuatro macrocircuitos ─────────
campos = ["DISPARADOR","PRECONDICIONES","PROCESO","PARTICIPANTES","LEE","ESCRIBE","ESTADO",
          "HANDOFFS","EVIDENCIA","GATES","ROLLBACK","REANUDACIÓN","CERTIFICACIÓN","CIERRE"]
falt = []
if not _MACROS:
    falt.append("cero macrocircuitos derivados de §8: sin objeto, esto sería un verde por "
                "omisión")
for k in _MACROS:
    b = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == k)
    f = [c for c in campos if not re.search(r"^"+c+r"(\s|$)", b, re.M)]
    if f: falt.append(f"§{k}: {f}")
check("G-25", "los macrocircuitos DERIVADOS de §8 declaran sus CATORCE campos, handoffs incluidos",
      not falt, "; ".join(falt) or
      f"{len(campos)}/{len(campos)} en los {len(_MACROS)} macrocircuitos derivados "
      f"({', '.join('§' + m for m in _MACROS)})")

# ── G-26 · recuentos DERIVADOS, en cuatro planos ───────────────
#
# Ampliada por la corrección del gate definitivo (`J-07` + `K-04`; `C-L.9`). La versión
# anterior comparaba filas contra ids Y contra un 45 ESCRITO A MANO — que es exactamente
# el defecto que esta comprobación existe para cazar, y por eso no vio que cuatro sedes
# de prosa decían «cuarenta y dos» mientras la tabla tenía cuarenta y cinco filas.
#
# **Aquí no hay ni una cifra constante.** Todo se deriva del árbol: la tabla se cuenta, la
# prosa se lee, y se comparan. Si mañana nace una fila nueva, esta comprobación se mueve
# sola; si nace una sede de prosa nueva con la cifra vieja, la caza sin tocar el validador.
#
# Y distingue SEDE VIGENTE de CITA HISTÓRICA, que es la misma disciplina que `X47` aplica
# al enum de `fase`: la proyección normativa vigente es UNA y las citas históricas son
# MUCHAS y están marcadas. Una cifra entre comillas angulares, o en una línea que la
# corrige, o en un bloque marcado HISTÓRICO, es una cita — no una afirmación viva.

# el patrón `_NUM` vive con `_num`, arriba: lo usan `G-15` y `G-26`, y una segunda
# definición aquí sería la segunda sede de la misma expresión.

# Una cifra es CITA HISTÓRICA, y no afirmación viva, en tres casos y sólo en tres.
# La distinción se hace sobre LA OCURRENCIA CONCRETA del numeral, no sobre la línea
# entera: si bastara que la línea contuviera «corregido», la propia prosa que corrige
# una cifra desactivaría la comprobación de la cifra que acaba de escribir — que es el
# modo de fallo exacto que esta batería existe para no repetir.
_CITA_ENTRE_COMILLAS = re.compile(r"«[^»]*»")

# `A3` del documento 24. Aquí vivía `_VERBO_DE_CITA`, una tercera rama de `_es_cita` que
# eximía la cifra cuando el texto que la precedía terminaba en uno de estos verbos. Era **un
# interruptor léxico**, exactamente lo que el corpus tiene escrito que ninguna comprobación
# puede ser: escribir «decía » delante de una cifra viva falsa apagaba `G-26` y la batería
# volvía a 38/38. `W` lo encontró y `X` lo reprodujo con tres de los verbos, y midió además
# que `G-31` —la comprobación que existe para cazar interruptores léxicos— **no probaba ni
# uno de ellos**: su lista de palabras gatillo eran las de `T-06` y ninguna de éstas.
#
# La rama SE RETIRA, y no se sustituye por otra: el corpus ya tiene DOS formas
# ESTRUCTURALES de citar una cifra pasada —las comillas angulares «…», que delimitan la
# ocurrencia, y la etiqueta de región histórica, que delimita el bloque— y ninguna de las
# dos depende de que aparezca una palabra. Se comprobó antes de retirarla: sobre el árbol
# vivo y sobre `HEAD`, **ninguna sede del corpus dependía de esta rama**; la batería queda
# en 38/38 con ella retirada.
#
# La lista NO se borra: se conserva como SEDE DE LOS FIXTURES de `G-31`, que ahora prueba
# uno a uno que ninguno de estos verbos apaga nada. Una lista de interruptores retirados es
# el mejor corpus de prueba que hay para que no vuelvan.
_VERBOS_QUE_YA_NO_APAGAN = ("decía", "decían", "dijo", "habiendo", "frente a", "en vez de",
                            "se escribió cuando", "NO REPRODUCIDO", "reanclado",
                            "reanclada", "conteo a")

# ── la MARCA de bloque histórico es ESTRUCTURAL, no una palabra suelta ────
#
# `Q-04` del dictamen · protección 2 del adjudicador, y su generalización, la 10.
#
# Esta rama era `re.compile(r"\[HISTÓRICO|\bHISTÓRICO\b|\bcaducad|\bregresión\b")` evaluada
# sobre **la LÍNEA ENTERA**, al contrario que las otras dos ramas de `_es_cita`, que se
# evalúan sobre la OCURRENCIA — y el propio corpus había fijado esa disciplina por escrito
# tres renglones más arriba. Con ella, escribir « (sin regresión)» al final de la línea que
# lleva la cifra al Owner desactivaba el control de esa cifra: el adjudicador reinstaló con
# DOS PALABRAS el único GRAVE del gate anterior, y la batería siguió en 30/30.
#
# «regresión», «histórico», «caducado», «retirada» y «sustituida» son vocabulario corriente
# del corpus —`01-PROCESOS.md` usa «regresión» como sustantivo técnico en cuatro líneas—, y
# **ninguna comprobación puede depender de que una palabra suelta aparezca o no en una
# línea**. Lo que sí es una marca es una ETIQUETA ESTRUCTURAL: un corchete abierto al
# principio del bloque, que sólo se escribe para marcar, que no aparece en prosa por
# casualidad y que se ve al leer. Eso es lo que se reconoce aquí, **anclado al comienzo de
# la línea** y no en cualquier posición de ella.
_TAG = (r"\[(?:HISTÓRICO|HISTORICO|ESTADO ANTERIOR|CADUCADO|SUPERADO|NO REPRODUCIDO)\b")
# la etiqueta abre SECCIÓN cuando encabeza la línea, con la decoración de cita, viñeta o
# negrita que el corpus usa: `> **[ESTADO ANTERIOR · …]**`, `· **[HISTÓRICO · …]**`
_ETIQUETA_HISTORICA = re.compile(r"^[\s>|*_·-]*" + _TAG)
# y abre CAMPO cuando va detrás de una etiqueta de campo en columna 0, que es la otra forma
# que el corpus usa: `PRESIONES           **[HISTÓRICO]** ONCE vigentes …`. Las dos son
# estructurales y visibles; ninguna es una palabra suelta dentro de una frase
_CAMPO_HISTORICO = re.compile(
    r"^[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ0-9 ]{2,}\s{2,}[\s>|*_·-]*" + _TAG)
_CIERRA_REGION = re.compile(r"^#{1,6} ")
_LINEA_DE_CITA = re.compile(r"^\s*>")
_VALLA = re.compile(r"^\s*```")
# La OTRA forma de marcar historia que el corpus ya usa y que no es una etiqueta: una CLAVE
# en columna 0 que NOMBRA LA TANDA PASADA cuyo registro abre —`corregido_en_la_TANDA_…`,
# `devuelto_por_la_TERCERA_REVISION_…`, `resuelto_en_la_SEGUNDA_devolucion_…`—. Es
# estructural, está en columna 0, nombra el hecho pasado y se ve al leer, exactamente como
# la etiqueta; y su alcance es SU campo, que termina donde empieza la clave siguiente.
_CAMPO_DE_TANDA_PASADA = re.compile(
    r"^[a-z]+(?:ado|ada|ido|ida|to|cho)_(?:en|por|para)_(?:la|el)_[A-Za-z0-9_]+:\s*$")
_ABRE_CLAVE = re.compile(r"^\S")

def _regiones_historicas(texto):
    """Los tramos [ini, fin) que una marca ESTRUCTURAL declara históricos.

    Una región ABRE en una línea que EMPIEZA por la etiqueta —admitiendo la decoración de
    cita, viñeta o negrita que el corpus usa: `> **[ESTADO ANTERIOR · …]**`, `· **[HISTÓRICO
    · …]**`, `[HISTÓRICO]`— o en una CLAVE que nombra una tanda pasada, y CIERRA **al
    terminar el bloque que esa marca encabeza**.

    `T-06`. La protección 2 sustituyó el interruptor de PALABRA por uno de ETIQUETA, y eso
    se cerró bien; pero la región que la etiqueta abría cerraba SÓLO en `^#{1,6} `, un
    encabezado en columna 0 **que dentro de una cita `>` no llega nunca**. Con eso, UNA
    línea `> **[ESTADO ANTERIOR · …]**` eximía todo lo que viniera detrás hasta el siguiente
    encabezado: el adjudicador plantó una cifra viva falsa en el documento 11, `G-26` la
    cazó —36/37—, le puso encima esa única línea y la batería volvió a **37/37**. Y no era
    un caso de laboratorio: en el checkpoint, la marca de la L509 eximía de todo control de
    cifra **el bloque VIVO entero** que empieza en la L577, mil cien líneas más abajo.

    La frontera es ahora CUÁDRUPLE, y las cuatro son visibles al leer:

      · un ENCABEZADO Markdown, como antes,
      · la VALLA de un bloque de código, que abre y cierra contenedor,
      · la LÍNEA EN BLANCO que separa un bloque del siguiente, **también dentro de una
        valla** — y **NO para la clase `tanda`**, cuya clave abarca su bloque entero,
        blancos incluidos, y cierra en la siguiente línea que empieza en COLUMNA 0
        (`_ABRE_CLAVE`). `DD-15`: esta enumeración y la del README declaraban la línea en
        blanco sin esa excepción, y el código nunca la aplicó a `tanda`. La región de
        clase `tanda` **está acotada** —no es de longitud libre—, pero por OTRA frontera,
      · y la SALIDA DE LA CITA: si la marca se escribió dentro de un `>`, la región muere
        donde muere la cita. Lo que no está en la cita no lo declara histórico una etiqueta
        que sí lo está.

    `A4` del documento 24, y es `T-06` OTRA VEZ, un piso más abajo. La frontera cuádruple
    llevaba escrita la excepción `not en_valla`: **dentro de un bloque de código una línea
    en blanco no cerraba nada**, y dentro de un bloque de código tampoco hay encabezados ni
    se sale de ninguna cita. Es decir: una etiqueta escrita dentro de una valla eximía **de
    la etiqueta hasta el cierre de la valla**, cientos de líneas después, y las etiquetas
    siguientes no cerraban la anterior sino que quedaban dentro de ella. No hacía falta
    atacar nada: en el checkpoint del árbol juzgado, **1 899 de 3 562 líneas (53 %) estaban
    exentas de todo control de cifra**, entre ellas el bloque VIVO de «Siguiente acción
    exacta» entero, a partir de la etiqueta de la L3053. `X` lo reprodujo plantando una
    cifra falsa seis líneas más abajo de esa etiqueta: **38/38 verde**.

    La excepción se retira: una línea en blanco separa bloques también dentro de una valla
    —en el corpus las vallas son tablas de campos, y una línea en blanco es justo lo que
    separa un campo del siguiente—, y una marca nueva cierra la anterior. Con eso la
    exención del checkpoint baja de 1 899 líneas a 1 229, y ninguna de las que pierde estaba
    marcada por nadie.

    Marcar histórico un bloque entero sigue siendo posible y sigue siendo legítimo —es lo
    que el README declara—: lo que ya no se puede es marcarlo **desde fuera de él**, ni
    dejar la marca abierta hasta el final de la valla.
    """
    regiones, abierta, clase, en_cita, en_valla = [], None, None, False, False
    pos = 0
    for linea in texto.split("\n"):
        ini = pos
        pos += len(linea) + 1
        if _VALLA.match(linea):
            if abierta is not None:
                regiones.append((abierta, ini))
                abierta, clase, en_cita = None, None, False
            en_valla = not en_valla
            continue
        abre = None
        if _ETIQUETA_HISTORICA.match(linea):
            abre = "seccion"
        elif _CAMPO_HISTORICO.match(linea):
            abre = "campo"
        elif _CAMPO_DE_TANDA_PASADA.match(linea):
            abre = "tanda"
        if abre is not None:
            if abierta is None:
                abierta, clase = ini, abre
                en_cita = bool(_LINEA_DE_CITA.match(linea))
            else:
                # `A4`. Una marca nueva CIERRA la anterior, sea de la clase que sea. Antes
                # sólo lo hacía una clave de tanda sobre otra clave de tanda, y con eso el
                # primer `[HISTÓRICO]` de un bloque se tragaba los que venían detrás y todo
                # lo que hubiera entre ellos.
                regiones.append((abierta, ini))
                abierta, clase = ini, abre
                en_cita = bool(_LINEA_DE_CITA.match(linea))
            continue
        if abierta is None:
            continue
        if (_CIERRA_REGION.match(linea)
                or (clase == "tanda" and _ABRE_CLAVE.match(linea))
                or (not linea.strip() and clase != "tanda")
                or (en_cita and not _LINEA_DE_CITA.match(linea))):
            regiones.append((abierta, ini))
            abierta, clase, en_cita = None, None, False
    if abierta is not None:
        regiones.append((abierta, len(texto)))
    return regiones

_CACHE_REGIONES = {}

def _en_region_historica(texto, pos):
    clave = id(texto)
    if clave not in _CACHE_REGIONES:
        _CACHE_REGIONES[clave] = _regiones_historicas(texto)
    return any(a <= pos < b for a, b in _CACHE_REGIONES[clave])

def _es_cita(linea, ini_rel, fin_rel):
    """¿La ocurrencia [ini_rel:fin_rel] de esta línea es una cita y no una afirmación?

    UNA rama, y es ESTRUCTURAL: el numeral está entre comillas angulares, que delimitan la
    ocurrencia y se ven al leer. La otra forma legítima de citar —marcar el bloque como
    histórico— es también estructural y vive en `_en_region_historica`.

    `A3`. La tercera rama, la de los VERBOS, se retiró: era un interruptor léxico, y ninguna
    comprobación de esta batería puede depender de que una palabra aparezca en una línea.
    """
    for c in _CITA_ENTRE_COMILLAS.finditer(linea):
        if c.start() <= ini_rel and fin_rel <= c.end():
            return True                     # el numeral está DENTRO de «…»
    return False

def _sedes(patron, texto=None, contexto=None, ventana=6):
    """[(línea, valor)] de cada sede VIVA que afirma una cifra.

    `contexto` es un patrón que debe aparecer en la VENTANA de líneas alrededor para
    que la afirmación se considere sobre ESE objeto: sin él, «la tabla tiene siete
    filas» de §3.6 se compararía con la tabla adversarial, que es otra tabla. La
    ventana existe porque una afirmación y el nombre de su objeto rara vez caben en
    la misma línea de un bloque de texto justificado.
    """
    texto = t11 if texto is None else texto
    ls = texto.split("\n")
    out = []
    for m in re.finditer(patron, texto, re.I):
        n = _num(m.group(1))
        if n is None:
            continue
        ini = texto.rfind("\n", 0, m.start()) + 1
        fin = texto.find("\n", m.end())
        linea = texto[ini: fin if fin > 0 else len(texto)]
        if _es_cita(linea, m.start() - ini, m.end() - ini):
            continue
        # `§16 · presiones` no afirma «dieciséis presiones»: el numeral es el número de
        # sección. Una referencia a una sede no es un censo.
        if m.start() > ini and texto[m.start() - 1] == "§":
            continue
        # la REGIÓN histórica se evalúa SIEMPRE y de la misma manera para todas las sedes.
        # Antes esto era opcional —`por_bloque`—, de modo que dos sedes del mismo censo se
        # juzgaban con reglas distintas; y la regla de la que dependía era una palabra
        # suelta en la línea. Ahora es una sola regla estructural para todas.
        if _en_region_historica(texto, m.start()):
            continue
        if contexto:
            nl = texto.count("\n", 0, m.start())
            bloque = "\n".join(ls[max(0, nl - ventana): nl + ventana + 1])
            if not re.search(contexto, bloque, re.I):
                continue
        out.append((texto.count("\n", 0, m.start()) + 1, n))
    return out

_fallos_26 = []

# ── 26.a · filas FÍSICAS frente a IDS ÚNICOS ──────────────────────────────
xs = re.findall(r"^\| \*{0,2}`(X[0-9]+)`\*{0,2} \|", t11, re.M)
n_x = len(xs)
if n_x == 0:
    _fallos_26.append("a) la tabla adversarial no se encontró: el patrón de fila no casa")
elif n_x != len(set(xs)):
    dup = sorted(k for k, v in Counter(xs).items() if v > 1)
    _fallos_26.append(f"a) {n_x} filas frente a {len(set(xs))} ids únicos; duplicados: {dup}")

# ── 26.b · PROSA VIGENTE frente al valor DERIVADO ─────────────────────────
# Sólo sedes que hablan de LA TABLA ADVERSARIAL: la línea tiene que nombrarla.
_CTX_X = r"adversarial|§2\.6\.7|\bX[0-9]{2}\b"
for pat, que in (
    (_NUM + r"\s+filas\s+(?:físicas|de datos|escritas)", "filas"),
    (_NUM + r"\s+identificadores", "ids"),
    (r"(?:las|como las)\s+" + _NUM + r"\s+de\s+§2\.6\.7", "filas"),
    (_NUM + r"\s+filas\s+de\s+la\s+tabla\s+adversarial", "filas"),
):
    for ln, val in _sedes(pat, contexto=_CTX_X):
        if val != n_x:
            _fallos_26.append(f"b) L{ln}: la prosa dice {val} {que} y el conteo da {n_x}")

# ── 26.c · AGREGADOS frente a sus MIEMBROS ────────────────────────────────
# c1 · presiones normativas: cabeceras de §16 menos RETIRADA y FUSIONADA
_pn = re.findall(r"^## `(PN-[0-9]+)`([^\n]*)$", t11, re.M)
n_pn = sum(1 for _, resto in _pn if "RETIRADA" not in resto and "FUSIONADA" not in resto)
if not _pn:
    _fallos_26.append("c1) no se encontró ninguna cabecera `## `PN-` en §16")
# El contexto exigido distingue una AFIRMACIÓN DE CENSO —«N presiones vigentes»— de un
# uso incidental del sustantivo, como «presentar al Owner dos presiones donde hay una
# enmienda», que no cuenta nada. Las dos formas específicas de abajo no necesitan
# contexto: ya son inequívocas por sí mismas.
_CTX_PN = r"vigente|VIGENTES|§16"
for pat, ctx in (
    (_NUM + r"\s+(?:presiones|PRESIONES|puntos de presión)", _CTX_PN),
    (r"VIGENTES\s*·\s*" + _NUM, None),
    (r"presiona material aprobado en\s+" + _NUM + r"\s+puntos", None),
):
    for ln, val in _sedes(pat, contexto=ctx):
        if val != n_pn:
            _fallos_26.append(f"c1) L{ln}: dice {val} y las cabeceras de §16 derivan {n_pn}")

# y el MISMO censo sobre el CHECKPOINT, que es el fichero que un agente lee al reanudar.
#
# `P-05`≡`Q-08`. La sección «Siguiente acción exacta» mandaba al Owner DOCE presiones donde
# el derivado daba TRECE, por SEGUNDA vez seguida sobre la misma línea —la corrección
# anterior, `I-28`, estaba escrita dos renglones más abajo—. Estos patrones sólo barrían el
# documento 11: la sede que va al Owner quedaba fuera del control que existe para ella.
for ln, val in _sedes(_NUM + r"\s+(?:presiones|PRESIONES)", tchk,
                      contexto=r"§16|vigente|VIGENTES|Owner"):
    if val != n_pn:
        _fallos_26.append(f"c1) checkpoint L{ln}: dice {val} presiones y las cabeceras "
                          f"de §16 derivan {n_pn}")

# c2 · externos de §19: la tabla frente a la prosa que la reconcilia
_i19 = t11.find("## Lo que esta fase NO puede corregir")
if _i19 < 0:
    _fallos_26.append("c2) no se encontró la sección de externos de §19")
else:
    _seg = t11[_i19:_i19 + 12000]
    _off = t11.count("\n", 0, _i19)
    _filas_f = re.findall(r"^\| `(F-[0-9]+)`", _seg, re.M)
    # miembros que la propia reconciliación declara NO externos
    _no_ext = set(re.findall(
        r"`(F-[0-9]+)`[^\n]{0,120}?(?:deja de ser externo|NO es externo|nunca lo fue)", _seg))
    n_ext = len(_filas_f) - len(_no_ext)
    for pat, que in ((r"los externos son\s+" + _NUM, "externos"),
                     (_NUM + r"\s+de los cuarenta y tres hallazgos", "externos")):
        for ln, val in _sedes(pat, _seg, contexto=r"externo"):
            if val != n_ext:
                _fallos_26.append(
                    f"c2) L{_off+ln}: «{val} externos» y la tabla deriva {n_ext} "
                    f"({len(_filas_f)} filas − {len(_no_ext)} declaradas no externas)")
    for ln, val in _sedes(r"La tabla tiene\s+" + _NUM + r"\s+filas", _seg, contexto=r"externo"):
        if val != len(_filas_f):
            _fallos_26.append(f"c2) L{_off+ln}: «la tabla tiene {val} filas» y tiene {len(_filas_f)}")

# ── 26.e · la fila que BARRE TODAS LAS VENTANAS, contra las filas W ───────
#
# `P-01`≡`Q-13`. `X54` decía «las diecisiete ventanas» mientras §2.6.5 deriva DIECIOCHO de
# sus filas, y ninguna de las 46 filas adversariales nombraba `W17` — la ventana que `D105`
# creó para cerrar `M-03` y `O-03`. La tabla se declara convertible en pruebas de F6 «sin
# traducción»: lo que no tiene fila, no se prueba. Aquí el censo se DERIVA de las filas `W`
# y se contrasta contra el numeral de la fila que dice barrerlas todas.
_ws = re.findall(r"^\| \*{0,2}(W[0-9]+[ab]?)\*{0,2} \|", t11, re.M)
if not _ws:
    _fallos_26.append("e) no se encontró la tabla de ventanas de §2.6.5")
else:
    _x_barre = [l for l in t11.split("\n")
                if re.match(r"^\| `X[0-9]+` \|", l) and "ventanas" in l and "cada una" in l]
    if not _x_barre:
        _fallos_26.append("e) ninguna fila adversarial dice barrer todas las ventanas")
    for _l in _x_barre:
        _m = re.search(_NUM + r"\s+ventanas", _l)
        _v = _num(_m.group(1)) if _m else None
        _id = re.match(r"^\| `(X[0-9]+)`", _l).group(1)
        if _v != len(_ws):
            _fallos_26.append(f"e) `{_id}` dice {_m.group(1) if _m else '?'} ventanas y "
                              f"§2.6.5 deriva {len(_ws)} filas")
        if _ws[-1] not in _l:
            _fallos_26.append(f"e) `{_id}` barre todas las ventanas y no nombra `{_ws[-1]}`, "
                              f"que es la última que la tabla declara")

# ── 26.f · los RANGOS de presiones, no sólo los numerales ─────────────────
#
# `Q-07`. §16 decía «`PN-6` a `PN-14`» cuando ya existía `PN-15`, y omitía precisamente la
# que va al Owner. Es la TERCERA vez que esa frase caduca —`m2` y luego `I-11` la
# corrigieron—, y las dos veces anteriores se corrigió el numeral: un RANGO no es un
# numeral, y por eso `G-13` y `G-26` no lo veían. Aquí se deriva el último vigente de las
# cabeceras y se exige que todo rango VIVO termine en él.
_pn_vig = [int(n) for n, resto in re.findall(r"^## `PN-(\d+)` ·(.*)$", t11, re.M)
           if "RETIRADA" not in resto and "FUSIONADA" not in resto]
_ultimo = max(_pn_vig) if _pn_vig else None
for _txt, _quien in ((t11, "11"), (tchk, "checkpoint")):
    for _m in re.finditer(r"`PN-(\d+)`\s*a\s*`PN-(\d+)`", _txt):
        _ini = _txt.rfind("\n", 0, _m.start()) + 1
        _fin = _txt.find("\n", _m.end())
        _lin = _txt[_ini: _fin if _fin > 0 else len(_txt)]
        # la marca de histórico es la REGIÓN estructural, la misma que usa `_sedes`
        if _es_cita(_lin, _m.start() - _ini, _m.end() - _ini) or \
           _en_region_historica(_txt, _m.start()):
            continue
        if int(_m.group(2)) != _ultimo:
            _fallos_26.append(
                f"f) {_quien} L{_txt.count(chr(10), 0, _m.start()) + 1}: el rango vivo "
                f"«PN-{_m.group(1)} a PN-{_m.group(2)}» no termina en la última vigente, "
                f"que es PN-{_ultimo}")

# ── 26.d · TOTALES INCOMPATIBLES entre sedes VIVAS ────────────────────────
# Dos sedes vivas que afirmen cifras distintas del MISMO objeto es un fallo aunque
# ninguna difiera del derivado por el patrón que la caza.
for etiqueta, sedes in (
    ("filas adversariales",
     _sedes(_NUM + r"\s+filas\s+(?:físicas|de datos|escritas)", contexto=_CTX_X)),
    ("presiones vigentes",
     _sedes(_NUM + r"\s+(?:presiones|PRESIONES)", contexto=_CTX_PN)),
):
    vals = sorted({v for _, v in sedes})
    if len(vals) > 1:
        _fallos_26.append(f"d) sedes vivas incompatibles para «{etiqueta}»: {vals}")

# `Z1-07`. El README publicaba «1 899 de 3 562 líneas del checkpoint (53 %) exentas …
# retirada, bajan a 1 229»: DOS cifras escritas a mano, medidas sobre un árbol que ya no
# existe y que **ninguna comprobación contrastaba**. `Z3` volvió a medirlas y le dieron
# 1 240 de 3 817. Una cifra publicada que nadie deriva es exactamente lo que `P-01` castiga,
# en el fichero que declara la disciplina. Aquí se DERIVA, sobre el árbol que se tiene
# delante, y el README deja de escribirla: la lee de este detalle.
_pos_chk, _exentas_chk = 0, 0
for _l_chk in tchk.split("\n"):
    if _en_region_historica(tchk, _pos_chk):
        _exentas_chk += 1
    _pos_chk += len(_l_chk) + 1
_tot_chk = len(tchk.split("\n"))

check("G-26",
      "recuentos DERIVADOS: filas/ids · prosa/derivado · agregados/miembros · sin totales incompatibles",
      not _fallos_26,
      "; ".join(_fallos_26) or
      f"{n_x} filas = {len(set(xs))} ids · {n_pn} presiones derivadas de §16 · "
      f"prosa viva y agregados coinciden · EXENCIÓN VIGENTE POR REGIÓN HISTÓRICA, DERIVADA "
      f"del árbol que se tiene delante: {_exentas_chk} de {_tot_chk} líneas del checkpoint "
      f"({100.0 * _exentas_chk / _tot_chk:.1f} %), y ninguna cifra de este renglón se "
      f"escribe a mano")

# ── G-27 · A7 · los cinco CAMPOS en la regla 1 de §2.6.10 ─────
r1 = re.search(r"1  EL COMMIT LOCAL SE HACE[^\n]*\n(?:[^\n]*\n){0,3}", t11)
ok = r1 and "CAMPOS DE PROCEDENCIA" in r1.group(0)
mal = re.search(r"con los CINCO conceptos de `a\.9`:", t11)
check("G-27", "la regla 1 de §2.6.10 usa «los cinco CAMPOS», no «los cinco conceptos»",
      bool(ok) and not mal, "corregida" if ok and not mal else "sigue diciendo conceptos")

# ── informe ──────────────────────────────────────────────────
# `ancho = max(len(t) ...)` vivía aquí y se RETIRA: se calculaba en cada corrida y no lo
# leía nadie —las dos `f-string` de abajo usan anchos fijos—. Es `Q-15`, y es la misma
# clase que `M-11`: código que aparenta gobernar el formato y no gobierna nada.

# ── G-28 · VEREDICTO, POLARIDAD y ESTADO de los documentos de gate ──────
#
# Protección 8. `G-22` impide tocar un documento histórico, y eso ya bastaría; pero el
# ataque que hay que hacer imposible **en silencio** es uno concreto —voltear un
# `INSUFICIENTE PARA F5` a `SUFICIENTE PARA F5`— y una comprobación que sólo dice «el
# fichero cambió» manda a leer un diff de tres mil líneas. Aquí el cambio se NOMBRA: qué
# documento, qué veredicto había, qué veredicto hay.
#
# El censo de veredictos se DERIVA del documento —no se escribe cuál es el suyo— y se
# contrasta contra el mismo documento en `HEAD`. Se cubren tres familias de polaridad, y
# las tres se derivan del par: veredicto de fase, cierre de condición y superación de
# hallazgo. **Sin Git, falla CERRADO.**
_POLARIDADES = (
    ("el veredicto de fase", r"\bINSUFICIENTE PARA F5\b", r"(?<!IN)\bSUFICIENTE PARA F5\b"),
    ("la superación de hallazgo", r"\bNO SUPERADO\b", r"(?<!NO )\bSUPERADO\b"),
    ("el cumplimiento de condición", r"\bFALLIDA\b", r"\bCUMPLIDA\b"),
)

def _censo_polaridad(texto):
    return {nombre: (len(re.findall(neg, texto)), len(re.findall(pos, texto)))
            for nombre, neg, pos in _POLARIDADES}

_g28, _revisados = [], 0
# `H-11`. La REGLA es de `O19`; la tanda de `O20` fue la ocasión de la corrección, no su
# fuente. **`docs/owner/` NO es un documento de gate**, y esta comprobación lo metía en la
# familia de polaridad de los veredictos: registrar una resolución nueva del Owner —que es
# el procedimiento que `O19` prescribe— disparaba «la superación de hallazgo CAMBIÓ» sobre
# una sede que no emite veredictos de gate. Su contrato es APPEND-ONLY y lo comprueba
# `G-29` contra el commit que la creó; aquí se excluye por lo que la zona ES, no por su
# nombre: es la SEDE DEL OWNER, no un dictamen.
_docs_gate = [f for f in _INMUTABLES
              if f.endswith(".md") and not f.startswith("docs/owner/")]
_vacia28 = _base_vacia(_head_arbol_raw, "git ls-tree -r --name-only HEAD",
                       "no hay ningún documento publicado contra el que contrastar un "
                       "veredicto")
if _mod_head_raw is None or _head_arbol_raw is None:
    _g28.append("GIT NO RESPONDE: no se puede contrastar ningún veredicto contra su "
                "versión publicada")
elif _vacia28:
    # `T-05`, la misma guarda que `G-11b` ya tenía y que faltaba aquí: con `_head_arbol`
    # vacío el bucle se salta con `continue` los veintiséis documentos y esta comprobación
    # daba `OK` sobre CERO documentos revisados.
    _g28.append(_vacia28)
elif not _docs_gate:
    _g28.append("cero documentos de gate derivados: sin objeto, esta comprobación sería "
                "un verde por omisión")
else:
    for rel in _docs_gate:
        if rel not in _head_arbol:
            continue
        publicado = _git("show", "HEAD:" + rel)
        if publicado is None:
            _g28.append(f"{rel}: `git show HEAD:` no devuelve contenido y el fichero está "
                        f"rastreado; no hay contra qué contrastar su veredicto")
            continue
        try:
            actual = leer(os.path.join(RAIZ, rel))
        except SedeIlegible as e:
            _g28.append(f"{rel}: ilegible ({e})")
            continue
        _revisados += 1
        antes, ahora = _censo_polaridad(publicado), _censo_polaridad(actual)
        for nombre in antes:
            if antes[nombre] != ahora[nombre]:
                _g28.append(
                    f"{rel}: {nombre} CAMBIÓ — publicado (negativo {antes[nombre][0]}, "
                    f"positivo {antes[nombre][1]}) y en el árbol (negativo "
                    f"{ahora[nombre][0]}, positivo {ahora[nombre][1]}). Un veredicto "
                    f"emitido no se reescribe: lo revisa otro gate, con su documento")
    if not _revisados:
        _g28.append(f"CERO documentos de gate contrastados de los {len(_docs_gate)} "
                    f"derivados: ninguno tiene versión publicada contra la que comparar, y "
                    f"un `OK` sobre cero documentos es un verde por omisión")
check("G-28",
      "ningún documento de gate cambia de VEREDICTO, POLARIDAD o ESTADO en silencio (falla CERRADO sin git)",
      not _g28,
      "; ".join(_g28) or
      f"{_revisados} documentos de gate contrastados contra `HEAD` en las "
      f"{len(_POLARIDADES)} familias de polaridad derivadas, sin una sola inversión")

# ── G-29 · TOPOLOGÍA y UNICIDAD de TODO el corpus gobernado ─────────────
#
# Protecciones 5 y 9. La comparación de CONJUNTOS —la única que ve un fichero AÑADIDO y sin
# rastrear, porque `git diff --name-only` no lo lista— existía **sólo para `kernel/`**. El
# adjudicador movió el ataque de `Q-04` un directorio afuera: un `C8-SEGUNDA-SEDE.md` en
# `docs/rediseno/` que declara por escrito contradecir a `C4` y a `C7` y prevalecer sobre
# los dos, más copias íntegras de `a-CAPACIDADES-APROBADA.md` y del registro de decisiones.
# **30/30 en verde.** La corrección anterior se había aplicado al perímetro exacto de su
# contraejemplo y a ninguna otra parte.
#
# Aquí el control es del CORPUS GOBERNADO entero, zona a zona, con el régimen de cada una
# DECLARADO y las ampliaciones admitidas **clasificadas**, no exentas por ruta:
#
#   `kernel/`             ninguna ampliación salvo la excepción publicada de `G-23`
#   `docs/rediseno/`      ninguna: es material APROBADO y el registro de decisiones
#   `docs/evolucion/`     un documento numerado nuevo es el producto legítimo de un gate;
#                         el instrumental de `verificacion/` sólo entra si el README lo
#                         ENUMERA, que es la sede que lo declara y que se puede leer
#   `docs/canonico/`      el CORPUS CANÓNICO VIGENTE, que el Owner ordenó consolidar antes
#                         de `F5`: se admite si `00-INDICE.md` lo enlaza por RUTA COMPLETA
#
# Y sobre todo el corpus, dos controles de UNICIDAD que no dependen de ninguna lista:
# ningún fichero puede tener un gemelo byte a byte, y ningún marcador de bloque canónico
# —derivados del árbol, no escritos— puede ganar sedes nuevas.
# `T-03` y el vector que el adjudicador `U` ejecutó y nadie había ejecutado. `_ZONAS` eran
# TRES directorios, y el README prometía «TODO el corpus gobernado». Fuera quedaban **la
# RAÍZ** —`README.md`, `START_HERE.md`—, **`docs/owner/`** —que ya existe en el árbol y
# guarda material APROBADO—, **`packs/`** y **`tooling/`**. Sobre esas cuatro zonas `U`
# plantó segundas sedes normativas íntegras con cabecera «PREVALECE SOBRE TODO» y la
# batería dio **37/37 en verde**.
#
# `A2` del documento 24, y es la TERCERA vez que el mismo defecto sale por el mismo sitio.
# Aquella corrección volvió a escribir una LISTA —siete zonas—, y una lista escrita caduca:
# `X` puso copias **byte a byte** del material APROBADO y del registro de decisiones en
# `docs/normativa/` —un directorio que no existía— y en la raíz de `docs/`, y la batería dio
# **38/38 verde**; el MISMO gemelo dentro de una zona listada daba **37/38 · FALLO G-29**.
# Defecto de PERÍMETRO, no de idea, exactamente como `Q-04` y `T-03` antes.
#
# Aquí el perímetro DEJA DE ESCRIBIRSE. **El corpus gobernado es el repositorio entero**,
# menos lo que se excluye con nombre y con motivo: el propio `.git`, que no es corpus sino
# el almacén contra el que se compara, y los artefactos de bytecode, que no son fuente. Un
# directorio nuevo —`docs/normativa/`, o el que venga— entra SOLO, sin tocar una línea de
# esto; y quien quiera sacar algo del perímetro tiene que escribirlo aquí y responder de
# ello. Una lista de lo que se excluye no puede caducar por omisión: lo que olvide nombrar
# se queda DENTRO.
# `Z1-03`≡`Z-05`. La definición vive ARRIBA, junto a `_rel()`, porque el inventario de
# inmutables la necesita antes que `G-29`: escribirla dos veces era crear la segunda sede.
# Aquí sólo se usa.

def _ficheros_zona():
    salida = set()
    for base, dirs, ficheros in os.walk(RAIZ):
        _podar(base, dirs)
        for nombre in ficheros:
            rel = _rel(os.path.join(base, nombre))
            if _en_zona(rel):
                salida.add(rel)
    return salida

_g29 = []
_disco = _ficheros_zona()
_publicado = {f for f in _head_arbol if _en_zona(f)}

# el instrumental de `verificacion/` se declara en su README, y esa declaración se lee
_README = os.path.join(RAIZ, "docs/evolucion/verificacion/README.md")
try:
    _t_readme = leer(_README)
except SedeIlegible as e:
    _t_readme = ""
    _g29.append(f"el README de `verificacion/` no se puede leer ({e}): sin él no hay sede "
                f"donde esté declarado el instrumental, y una ampliación sin sede es una "
                f"ampliación sin declarar")
_INSTRUMENTAL = set(re.findall(r"`(docs/evolucion/verificacion/[A-Za-z0-9_.-]+)`", _t_readme))

# las dos sedes que CLASIFICAN un documento numerado nuevo, derivadas y no escritas
try:
    _t_idx = leer(IDX)
except SedeIlegible as _e:
    _t_idx = ""
    _g29.append(f"`00-INDICE.md` no se puede leer ({_e}): sin él no hay sede desde la que "
                f"un documento numerado nuevo esté enlazado, y admitirlo sin ella es el "
                f"`return True` en blanco que `T-03` explotó")
# `Z1-01`≡`W-04`≡`Z-02`, y `AA-E1`/`AA-E3`. Los dos conjuntos guardaban NOMBRES DE FICHERO
# y la admisión comparaba `rel.split("/")[-1]`, de modo que un enlace a
# `../owner/ADS-OWNER-RESOLUCIONES.md` admitía ese nombre **a cualquier profundidad**:
# `docs/owner/vigente/…` y `docs/owner/x/y/z/…` pasaban en 38/38 declarando PREVALECER
# sobre la sede canónica, y `G-22` los NOMBRABA en su detalle mientras imprimía `OK`. La
# línea nació en `1d3b5d4`, el commit que implementa `O19`.
#
# Aquí se guardan RUTAS COMPLETAS, resueltas contra el directorio del índice: un enlace
# admite **una ruta**, no un nombre. Es el mismo defecto de perímetro que `G-29` cierra un
# piso más arriba —derivar en vez de enumerar—, aplicado al discriminante.
_ENLAZADOS_INDICE = {"docs/evolucion/" + n for n in
                     re.findall(r"\]\(([A-Za-z0-9][-A-Za-z0-9_.]*\.md)\)", _t_idx)}
# La misma sede, para la otra zona: `00-INDICE.md` enlaza `docs/owner/` con ruta relativa
# `../owner/`, que el patrón de arriba no puede recoger porque empieza por punto. El
# subcamino se conserva ENTERO: `../owner/vigente/X.md` admite `docs/owner/vigente/X.md` y
# NO admite `docs/owner/X.md`, ni al revés.
# `EE-01`/`EE-03`. Los enlaces del índice a `verificacion/` —instrumental y manifiestos—,
# por RUTA COMPLETA y no por nombre, con la misma disciplina que las otras dos zonas.
_ENLAZADOS_INDICE_VERIF = {"docs/evolucion/" + n for n in re.findall(
    r"\]\((verificacion/(?:[A-Za-z0-9][-A-Za-z0-9_.]*/)*[A-Za-z0-9][-A-Za-z0-9_.]*\.md)\)",
    _t_idx)}
_ENLAZADOS_INDICE_OWNER = {"docs/owner/" + n for n in re.findall(
    r"\]\(\.\./owner/((?:[A-Za-z0-9][-A-Za-z0-9_.]*/)*[A-Za-z0-9][-A-Za-z0-9_.]*\.md)\)",
    _t_idx)}
# La MISMA sede y la MISMA disciplina, para la zona del CORPUS CANÓNICO VIGENTE. Nace
# porque el Owner ordenó consolidar el estado vigente en `docs/canonico/` antes de `F5`, y
# esa zona no existía cuando se escribió la guarda: sin clasificar, la ampliación que la
# propia orden manda publicar sería ROJA — que es exactamente lo que ocurrió con
# `docs/owner/` cuando `O19` ordenó crear allí la sede canónica, y se resuelve igual: la
# zona **se admite CLASIFICADA y con UNA condición**, que es la que el código ejecuta y toda
# la que ejecuta. **No se relaja ninguna condición existente y no se exime nada**: lo que se
# añade es una zona más con guarda propia, derivada contra la REVISIÓN BASE como las demás.
#
# A diferencia de `docs/owner/`, aquí se admiten además `.yml` y `.py`: el registro de sedes
# canónicas es un fichero de datos y su validador es un fichero de código, y los dos tienen
# que estar enlazados igual que los documentos. Lo que NO cambia es el discriminante:
# **RUTA COMPLETA**, resuelta contra el directorio del índice, y no un nombre a cualquier
# profundidad — que es el defecto `Z1-01`≡`W-04`≡`Z-02` que esta misma guarda cerró un piso
# más arriba.
_ENLAZADOS_INDICE_CANONICO = {"docs/canonico/" + n for n in re.findall(
    r"\]\(\.\./canonico/((?:[A-Za-z0-9][-A-Za-z0-9_.]*/)*"
    r"[A-Za-z0-9][-A-Za-z0-9_.]*\.(?:md|yml|yaml|py))\)",
    _t_idx)}
# `EE-01`. Esto era `_ORDINALES_PUBLICADOS`, derivado de `_publicado`: el ordinal de un
# documento ya confirmado figuraba como OCUPADO **por él mismo**, de modo que la condición
# «el ordinal está libre» sólo podía cumplirla un documento que aún no estuviera en `HEAD`.
# Al derivar el alcance contra la REVISIÓN BASE, esa forma ponía en rojo los nueve
# documentos legítimos. Lo que la regla quiere decir —y lo que ahora ejecuta— es que **NO
# HAYA DOS documentos con el mismo ordinal**: dos sedes con la misma identidad. El censo se
# deriva del corpus gobernado entero, y lo que se prohíbe es la COLISIÓN, no la existencia.
_POR_ORDINAL = {}
for _f in sorted(_disco | _publicado):
    _m_o = re.match(r"^docs/evolucion/(\d\d)-.*\.md$", _f)
    if _m_o:
        _POR_ORDINAL.setdefault(_m_o.group(1), set()).add(_f)
_ORDINALES_COLISION = {o for o, fs in _POR_ORDINAL.items() if len(fs) > 1}

def _ampliacion_admitida(rel):
    """¿La aparición de `rel`, que no está publicada, está CLASIFICADA y admitida?"""
    if rel.startswith("kernel/"):
        return rel in COD_AUTORIZADO or rel in DOC_AUTORIZADO or rel in HUELLA \
            or rel.startswith("kernel/operativo/pruebas/evidencia/")
    if rel.startswith("docs/rediseno/"):
        return False
    if rel.startswith("docs/owner/"):
        # `O19`. `docs/owner/` no admitía NINGUNA ampliación, y el Owner ordenó crear ahí la
        # SEDE CANÓNICA de sus resoluciones: la zona tenía que admitir el fichero que su
        # propia resolución manda publicar, o la batería habría bloqueado el remedio. Se
        # admite CLASIFICADA y con UNA condición, que es la que el código ejecuta y toda la
        # que ejecuta: **la RUTA COMPLETA está enlazada desde `00-INDICE.md`**. Una segunda
        # sede plantada en `docs/owner/` —al lado, o en un subdirectorio— sin ese enlace es
        # ROJA. Y una vez confirmada, su contenido queda bajo el inventario de inmutables de
        # `G-22`, que alcanza esta zona.
        #
        # `AA-03`. Aquí decía además «**y en el mismo commit que lo crea**». **Esa condición
        # no estaba implementada, ni podía estarlo en este punto**: la función sólo se
        # consulta para ficheros que NO están en `HEAD`, y el commit que los crea todavía no
        # existe. Una condición que el comentario declara y el código no ejecuta es una
        # afirmación falsa del instrumento —la clase `V-04`—, y se retira en vez de
        # adornarse. Queda dicho lo que falta, y no se presume cubierto: quien confirme el
        # fichero y su enlace en commits distintos no encuentra aquí quien se lo diga.
        return rel in _ENLAZADOS_INDICE_OWNER
    if rel.startswith("docs/canonico/"):
        # CORPUS CANÓNICO VIGENTE. Se admite CLASIFICADA y con UNA condición, que es la que
        # esta línea ejecuta y toda la que ejecuta: **la RUTA COMPLETA está enlazada desde
        # `00-INDICE.md`**. Un fichero plantado en `docs/canonico/` —al lado, o en un
        # subdirectorio— sin ese enlace es ROJO, igual que en `docs/owner/`.
        #
        # Lo que esta rama NO comprueba, y se dice en vez de presumirlo: que el enlace se
        # confirme en el MISMO commit que crea el fichero. Es la misma limitación que
        # `AA-03` retiró de las otras dos zonas —esta función sólo se consulta para lo que
        # todavía no está en `HEAD`, y el commit que lo crea aún no existe—, y la regla del
        # índice sigue siendo la regla del índice.
        return rel in _ENLAZADOS_INDICE_CANONICO
    if rel.startswith("docs/evolucion/verificacion/manifiestos/"):
        # `EE-01`. Aquí había un `return False` seco, y con él **la zona no tenía condición
        # de admisión**: era admisible sólo por estar ya en `HEAD`, es decir, por haber sido
        # confirmada. La condición que la zona SÍ tiene está escrita en `00-INDICE.md` y es
        # de `C-L.5`: «*todo documento que `C-L.5` obligue a publicar se enlaza desde la
        # lista de abajo EN EL MISMO COMMIT que lo crea*». Se ejecuta, en vez de suponerse.
        return rel in _ENLAZADOS_INDICE_VERIF
    if rel.startswith("docs/evolucion/verificacion/"):
        return rel in _INSTRUMENTAL
    m_ord = re.match(r"^docs/evolucion/(\d\d)-.*\.md$", rel)
    if m_ord:
        # `T-03`. Aquí había un `return True` EN BLANCO —«el documento que un gate nuevo
        # publica»— que admitía CUALQUIER fichero numerado sin mirar su contenido ni su
        # procedencia: `U` publicó con él una `23-SEGUNDA-SEDE-NORMATIVA.md` que declara
        # contradecir a `C4` y a `C7` y prevalecer sobre los dos, y `G-22` y `G-29` la
        # NOMBRARON en su detalle mientras imprimían `OK`.
        #
        # Publicar un documento numerado sigue siendo el producto legítimo de un gate, pero
        # deja de ser gratis: se admite CLASIFICADO, con DOS condiciones, que son las dos
        # que el código ejecuta —**la RUTA COMPLETA enlazada desde `00-INDICE.md`** y **el
        # ordinal libre**, porque dos documentos con el mismo número son dos sedes con la
        # misma identidad—.
        #
        # `AA-03`. El índice escribe una TERCERA —«se enlaza desde la lista de abajo EN EL
        # MISMO COMMIT que lo crea», `00-INDICE.md` L102-108— y este comentario la declaraba
        # como si aquí se comprobara. **No se comprueba, y no se puede comprobar aquí**: esta
        # rama sólo se consulta para lo que todavía no está en `HEAD`. La declaración se
        # retira; la regla del índice sigue siendo la regla del índice, y quien la incumpla
        # no encuentra en esta batería quien se lo diga.
        if rel not in _ENLAZADOS_INDICE:
            return False
        if m_ord.group(1) in _ORDINALES_COLISION:
            return False
        return True
    return False

if _head_arbol_raw is None:
    _g29.append("GIT NO RESPONDE: no se puede derivar el conjunto publicado del corpus")
else:
    if not _publicado:
        _g29.append("el conjunto publicado del corpus sale VACÍO: sin él no hay "
                    "comparación, y comparar contra nada da verde siempre")
    # ── `EE-01` · EL NOVENO ÁRBOL, Y POR QUÉ EL ALCANCE SE DERIVA ──────────
    #
    # **La guarda era INERTE sobre todo lo CONFIRMADO, salvo en una zona.** `_nuevos` se
    # calculaba sobre `_disco - _publicado`, es decir, sobre lo que aún no está en `HEAD`:
    # **confirmar un fichero lo sacaba para siempre del alcance de la única condición que
    # su zona impone**. El adjudicador del sexto gate lo midió y lo reprodujo dos veces:
    # `git add -A && git commit` **sin un solo flag** añadía `docs/normativa/…`, `docs/…` o
    # un fichero en la RAÍZ declarando `F4c` CERRADA y `F5` AUTORIZADA, dejaba
    # `git status` vacío, pasaba **38/38**, no entraba en el universo obligatorio ni en
    # `EXCLUIDOS_PERIMETRO` ni en `EXCLUIDOS_IV`, no recibía fila ni revisor, **y producía
    # el digest del sobre BIT A BIT idéntico al anclado**. `DD-02` había cerrado
    # exactamente esto **para `docs/owner/` y sólo para esa zona**: instancia cerrada,
    # clase abierta — la frase de `BB4`, medida por segunda vez.
    #
    # **El alcance deja de enumerarse zona a zona y se DERIVA**: es AMPLIACIÓN todo lo que
    # existe hoy —en disco o en `HEAD`— y **no existía en la REVISIÓN BASE**, que es el
    # ancla fija que `G-22`, `G-23` y `G-30` ya usan y que el SOBRE publica. Con eso,
    # confirmar deja de ser una forma de admitirse: quien añade una sede tiene que
    # satisfacer la condición de su zona **esté o no commiteada**, y la condición de cada
    # zona sigue siendo la que su sede escribe, no una lista nueva.
    # ── `S1-02` · LA GUARDA DERIVA SU **PROPIEDAD**, NO SÓLO SU CONJUNTO ──────
    #
    # `EE-01` derivó QUÉ CONJUNTO se examina —lo que existe hoy y no existía en la revisión
    # base— y con eso cerró las cinco variantes del noveno árbol. **Pero derivó el conjunto
    # y no la PROPIEDAD**: un fichero que YA EXISTÍA en la base no es una ampliación, luego
    # **MODIFICARLO no quedaba sometido a ninguna condición**. El adjudicador del séptimo
    # gate derivó y midió la clase entera: **OCHO rutas** —`.gitignore`, `README.md`,
    # `START_HERE.md`, la directiva del Owner, el prompt de arranque y las TRES evidencias
    # reejecutadas— en las que una sentencia de cierre de `F4c` daba **38/38**, `EXIT=0`,
    # `porcelain` vacío y **el digest del sobre bit a bit el anclado**. Y **no crea ningún
    # fichero**, de modo que los cinco controles positivos de la tanda anterior no lo
    # tocaban.
    #
    # **La guarda pasa a evaluar la MUTACIÓN y no la EXISTENCIA.** Se deriva la diferencia
    # semántica entre la REVISIÓN BASE y la candidata —`git diff --name-status`, con `-z`—
    # y **toda mutación de una ruta gobernada** tiene que estar admitida, sea cual sea su
    # naturaleza:
    #
    #   AÑADIDA (`A`)        la condición de su zona, como hasta ahora
    #   MODIFICADA (`M`)     **NUEVO**: existir en la base ya no exime. Si la ruta no está
    #                        declarada como objeto de la tanda ni autorizada por su zona,
    #                        es ROJO — y `.gitignore`, `README.md`, `START_HERE.md` y la
    #                        directiva del Owner no lo están
    #   BORRADA (`D`)        una sede del corpus no desaparece en silencio
    #   RENOMBRADA (`R`)     se juzgan LAS DOS puntas: el destino como añadido y el origen
    #                        como borrado. Un renombrado es la forma más barata de mover
    #                        una sede fuera del alcance de su zona
    #   COPIADA (`C`)        el destino, como añadido
    #   TIPO (`T`)           un fichero que pasa a enlace simbólico cambia de naturaleza
    #                        sin cambiar de nombre, y eso es exactamente lo que la regla
    #                        persigue
    #
    # **Y se evalúa sobre el CONTENIDO DEL COMMIT y sobre el disco a la vez**, de modo que
    # confirmar no exime: la diferencia se toma contra `HEAD` y contra el árbol de trabajo,
    # y se unen. Ninguna de las dos vías puede quedar ciega.
    _base_gobernada = {f for f in _base_arbol if _en_zona(f)}
    _universo_gobernado = (_disco | _publicado)

    def _mutaciones_desde_base():
        """Ruta → letras de mutación entre la REVISIÓN BASE y la candidata (`S1-02`).

        Se derivan las DOS diferencias —contra `HEAD` y contra el árbol de trabajo— y se
        unen: confirmar un cambio no puede sacarlo del alcance de la guarda.
        """
        fuera = {}
        for extremo in ("HEAD", None):
            orden = ["diff", "--name-status", "-M", "-C", "05f71b7"]
            if extremo:
                orden.append(extremo)
            bruto = _git(*orden, "-z")
            if bruto is None:
                _g29.append(f"GIT NO RESPONDE a `git diff --name-status 05f71b7 "
                            f"{extremo or '<árbol de trabajo>'}`: sin la diferencia contra "
                            f"la revisión base NO se puede saber qué ha mutado, y una "
                            f"guarda que no sabe qué mutó no guarda nada")
                continue
            campos = [c for c in bruto.split("\0") if c]
            i = 0
            while i < len(campos):
                est = campos[i]
                if est[:1] in ("R", "C"):
                    if i + 2 >= len(campos):
                        break
                    origen, destino = campos[i + 1], campos[i + 2]
                    fuera.setdefault(origen, set()).add("D")
                    fuera.setdefault(destino, set()).add("A")
                    i += 3
                else:
                    if i + 1 >= len(campos):
                        break
                    fuera.setdefault(campos[i + 1], set()).add(est[:1])
                    i += 2
        return fuera

    # Lo que SÍ puede mutar, y cada cosa con la comprobación que la gobierna. No hay
    # ninguna lista nueva: las cinco fuentes ya existían y cada una tiene su dueño.
    _MUT_DECLARADA = _declarado_en_correccion(_t_readme)

    def _mutacion_admitida(rel):
        """¿Está esta MUTACIÓN de una ruta preexistente autorizada, y por quién? (`S1-02`)"""
        if rel in _EN_CORRECCION:
            return True                       # objeto documental de la tanda · `G-22` la nombra
        if rel in _MUT_DECLARADA:
            return True                       # declarada en el README · `G-34`, y caduca sola
        if rel.startswith("kernel/operativo/pruebas/evidencia/"):
            return True                       # evidencia derivada · `G-30` la contrasta
        if rel in COD_AUTORIZADO or rel in DOC_AUTORIZADO or rel in HUELLA:
            return True                       # excepción NOMBRADA del kernel · `G-23`
        if rel in DOC_REDISENO_AUTORIZADO or rel in TOOLING_AUTORIZADO:
            return True                       # excepción NOMBRADA, con su motivo escrito
        return False

    _MUT = {"A": "AÑADIDA", "M": "MODIFICADA", "D": "BORRADA", "T": "CAMBIA DE TIPO"}
    _mutaciones = _mutaciones_desde_base()
    _ampliaciones, _mutadas = [], []
    for _f, _letras in sorted(_mutaciones.items()):
        if not _en_zona(_f):
            continue
        if _ampliacion_admitida(_f):
            continue
        if "D" in _letras and _f not in _universo_gobernado:
            _mutadas.append((_f, "BORRADA"))
            continue
        if _f in _base_gobernada:
            if _mutacion_admitida(_f):
                continue
            _mutadas.append((_f, " y ".join(sorted(_MUT.get(l, l) for l in _letras))))
        else:
            _ampliaciones.append(_f)
    _idos = sorted(_publicado - _disco)
    for f in _ampliaciones:
        _g29.append(f"AMPLIACIÓN NO CLASIFICADA del corpus gobernado, CONFIRMADA O NO: {f}. "
                    f"Añadir una sede es la forma más simple de crear una segunda verdad, y "
                    f"no la autoriza ninguna zona. El alcance de esta guarda se DERIVA "
                    f"contra la REVISIÓN BASE y no contra `HEAD` (`EE-01`): confirmar un "
                    f"fichero NO lo exime de la condición de su zona")
    # ── `S1-02`, CUARTA CARA · LA SEDE DEL OWNER ES APPEND-ONLY, Y ESO SE COMPRUEBA ──
    #
    # El banco adversarial de esta tanda encontró el residuo: **modificar
    # `docs/owner/ADS-OWNER-RESOLUCIONES.md` daba 38/38 una vez commiteado.** La sede nació
    # DESPUÉS de la revisión base, de modo que no es una mutación contra ella —el `diff`
    # base→candidata la ve como una ADICIÓN—, y `G-22` la contrasta contra `HEAD`, que
    # confirmar vuelve idéntico. Es la misma inercia-tras-confirmar, en la zona que `O19`
    # convierte en AUTORIDAD CANÓNICA.
    #
    # **`O19` declara esa zona APPEND-ONLY, y eso es una propiedad comprobable sin `HEAD`:**
    # el contenido de hoy tiene que EMPEZAR POR el contenido de la versión que la creó, que
    # se deriva de la historia con `--diff-filter=A`. Añadir una resolución es legítimo;
    # tocar una letra de lo ya publicado, no. **Ningún commit posterior puede volver
    # legítima una alteración**, porque la referencia no es `HEAD`: es el nacimiento.
    for _f in sorted(f for f in _universo_gobernado if f.startswith("docs/owner/")):
        _nac = _git("log", "--diff-filter=A", "--format=%H", "--", _f)
        if _nac is None or not _nac.strip():
            _g29.append(f"{_f}: no se puede derivar el commit que lo CREÓ, y sin él no hay "
                        f"contra qué comprobar que la sede del Owner es APPEND-ONLY. Se "
                        f"falla cerrado")
            continue
        _primero = _nac.strip().split("\n")[-1]
        _orig = _git("show", f"{_primero}:{_f}")
        if _orig is None:
            _g29.append(f"{_f}: su primera versión (`{_primero[:8]}`) no se puede leer")
            continue
        try:
            _hoy = leer(os.path.join(RAIZ, _f))
        except SedeIlegible as _e:
            _g29.append(f"{_f}: ilegible ({_e})")
            continue
        if not _hoy.startswith(_orig):
            _g29.append(
                f"LA SEDE CANÓNICA DEL OWNER NO ES APPEND-ONLY: {_f} — su contenido de hoy "
                f"NO empieza por el de la versión que la creó (`{_primero[:8]}`). `O19` "
                f"declara esta zona APPEND-ONLY: se añaden resoluciones, no se altera una "
                f"letra de las publicadas. **Se contrasta contra el NACIMIENTO y no contra "
                f"`HEAD` (`S1-02`), de modo que confirmar la alteración no la vuelve "
                f"legítima**")

    for f, _que in _mutadas:
        _g29.append(f"MUTACIÓN NO CLASIFICADA de una ruta que YA EXISTÍA en la revisión "
                    f"base: {f} — {_que}. **Existir en la base NO exime a una mutación** "
                    f"(`S1-02`): la guarda deriva su PROPIEDAD y no sólo su conjunto, y "
                    f"esta ruta no está declarada como objeto de la tanda ni autorizada por "
                    f"su zona. Es la superficie por la que una sentencia de cierre de `F4c` "
                    f"entraba con la batería en verde SIN CREAR NINGÚN FICHERO")
    for f in _idos:
        _g29.append(f"fichero del corpus DESAPARECIDO: {f}")

    # ── `DD-02` · LA ADMISIÓN SE EVALÚA SOBRE EL CONTENIDO DEL COMMIT ─────
    #
    # **La guarda de arriba era INERTE sobre todo fichero ya en `HEAD`**, y el adjudicador
    # del quinto gate lo midió: la misma segunda sede plantada en `docs/owner/` daba
    # `37/38 FALLO G-29` **sin commitear** y **`38/38` commiteada**. `_nuevos` se calcula
    # sobre `_disco - _publicado`, de modo que confirmar el fichero lo sacaba para siempre
    # del alcance de la única condición que la zona impone. **Y el objeto que un gate
    # audita es un COMMIT**, no un árbol de trabajo: la promesa del README —«*una segunda
    # sede plantada en esa zona sin ese enlace es ROJA*»— era falsa para todo commit.
    #
    # El remedio es una llamada, y es la que `DD` determinó: la zona se contrasta contra
    # **`git ls-tree -r HEAD docs/owner/`**, y cada ruta publicada tiene que estar
    # enlazada desde `00-INDICE.md`. La condición no cambia; cambia el CONJUNTO sobre el
    # que se evalúa, que pasa a ser el commit entero y no sólo lo que aún no está en él.
    _owner_publicado = sorted(f for f in _publicado if f.startswith("docs/owner/"))
    if not _owner_publicado:
        _g29.append("`git ls-tree -r HEAD docs/owner/` no devuelve ningún fichero: la SEDE "
                    "CANÓNICA del Owner no está en el commit, y una zona vacía satisface "
                    "por omisión cualquier condición que se le imponga")
    for f in _owner_publicado:
        if f not in _ENLAZADOS_INDICE_OWNER:
            _g29.append(f"SEGUNDA SEDE EN `docs/owner/`, YA CONFIRMADA EN `HEAD` y SIN "
                        f"ENLACE desde `00-INDICE.md`: {f}. La condición de admisión de "
                        f"esta zona se evalúa sobre el CONTENIDO DEL COMMIT —`DD-02`—, y "
                        f"no sólo sobre lo que todavía no está en él: confirmar un fichero "
                        f"no lo exime de la única regla que la zona tiene")

    # ── unicidad 1 · ningún fichero tiene un gemelo byte a byte ───────────
    _por_huella = {}
    for rel in sorted(_disco):
        try:
            with io.open(os.path.join(RAIZ, rel), "rb") as fh:
                _por_huella.setdefault(hashlib.sha256(fh.read()).hexdigest(),
                                       []).append(rel)
        except OSError as e:
            _g29.append(f"{rel}: no se puede leer para su huella ({e.strerror})")
    for _h, _rutas in sorted(_por_huella.items()):
        if len(_rutas) > 1:
            _g29.append(f"FUENTE DUPLICADA byte a byte: {_rutas}. Una copia íntegra de una "
                        f"sede canónica es una segunda sede, se llame como se llame")

    # ── unicidad 2 · los marcadores de bloque canónico no ganan sedes ─────
    # Los marcadores se DERIVAN del árbol —`ads:proceso`, `ads:memoria`, los que haya— y
    # no se escribe ninguno: si mañana nace `ads:certificacion`, entra solo.
    # `A2`, y por la misma razón que arriba: la zona normativa tampoco se escribe. La
    # EXCEPCIÓN sí, porque tiene motivo — en `docs/evolucion/` el mismo bloque es una CITA
    # —el documento 11 reproduce el formato para explicarlo— y citar no es duplicar la
    # fuente. Todo lo demás del corpus es zona normativa: `kernel/`, `docs/rediseno/`,
    # `docs/owner/`, `packs/`, `tooling/`, la raíz, y el directorio que nazca mañana.
    _CITA_NO_SEDE = ("docs/evolucion/",)
    _sedes_disco, _marcadores = {}, set()
    for rel in sorted(_disco):
        if not rel.endswith(".md") or rel.startswith(_CITA_NO_SEDE):
            continue
        try:
            cuerpo = leer(os.path.join(RAIZ, rel))
        except SedeIlegible:
            continue
        for marca in set(re.findall(r"```yaml\s+(ads:[a-z0-9_-]+)", cuerpo)):
            _marcadores.add(marca)
            _sedes_disco.setdefault(marca, set()).add(rel)
    # `S1-03`. Esta SEGUNDA guarda derivaba `base_marca` contra **`HEAD`**, de modo que
    # **confirmar una segunda sede de un bloque canónico la volvía legítima**: 37/38 sin
    # commitear, 38/38 commiteada. Es la inercia-tras-confirmar que `DD-02` cerró para
    # `docs/owner/` y `EE-01` para las ampliaciones — **en la sub-guarda de al lado, bajo
    # un título que esta misma tanda ensanchó a «CONFIRMADO O NO»**. La fila `EE-01` del
    # README llegó a nombrar el rango `L3107-3118`: el remedio se aplicó a UNA de las DOS
    # sedes. Aquí se deriva contra la **REVISIÓN BASE**, como la primera.
    for marca in sorted(_marcadores):
        publicado_marca = _git("grep", "-l", "```yaml " + marca, "05f71b7", "--", ".",
                               *[":(exclude)%s" % z.rstrip("/") for z in _CITA_NO_SEDE])
        if publicado_marca is None:
            _g29.append(f"GIT NO RESPONDE: no se puede derivar dónde vivía `{marca}` en la "
                        f"REVISIÓN BASE, y sin base no hay contraste")
            continue
        base_marca = {l.split(":", 1)[1] for l in publicado_marca.split("\n") if ":" in l}
        nuevas = sorted(_sedes_disco[marca] - base_marca)
        if nuevas:
            _g29.append(f"SEGUNDA SEDE del bloque canónico `{marca}`, CONFIRMADA O NO: "
                        f"{nuevas}. La fuente única no admite copias, y esto vale en "
                        f"cualquier zona normativa, no sólo bajo `kernel/`. Se deriva "
                        f"contra la REVISIÓN BASE (`S1-03`): confirmar una segunda sede NO "
                        f"la vuelve legítima")
check("G-29",
      "topología y unicidad de TODO el corpus gobernado, CONFIRMADO O NO: ninguna ampliación sin clasificar respecto de la REVISIÓN BASE, ningún gemelo byte a byte y ninguna segunda sede de un bloque canónico (falla CERRADO sin git)",
      not _g29,
      "; ".join(sorted(set(_g29))) or
      f"{len(_disco)} ficheros —el repositorio ENTERO menos `.git` y el bytecode, no una "
      f"lista de zonas—, todos publicados o clasificados · "
      f"cero duplicados byte a byte · {len(_marcadores)} marcadores canónicos derivados "
      f"({', '.join(sorted(_marcadores))}), cada uno en sus sedes publicadas · "
      f"{len(_owner_publicado)} ficheros de `docs/owner/` YA EN `HEAD`, cada uno enlazado "
      f"desde `00-INDICE.md` (`DD-02`: la admisión se evalúa sobre el CONTENIDO DEL "
      f"COMMIT) · PERÍMETRO: {len(EXCLUIDOS_PERIMETRO)} exclusiones, publicadas con su "
      f"RUTA COMPLETA y su motivo (`DD-01`) — "
      f"{'; '.join(f'{r} · {m}' for r, m in sorted(EXCLUIDOS_PERIMETRO))}")


# ── G-30 · la excepción del kernel, por CONTENIDO y por CLASIFICACIÓN ───
#
# Protección 6. `G-23` autorizaba RUTAS: `COD_AUTORIZADO` nombraba
# `comprobar_negativos.py`, `HUELLA` nombraba `.upstream-hash`, y un comodín entero eximía
# `pruebas/evidencia/` —tres renglones después de prometer que «no hay comodines sobre
# directorios de código»—. Con eso, el adjudicador **vació el validador a `sys.exit(0)`,
# falsificó su evidencia y sobrescribió la huella**, y la batería dio 30/30 en verde. Una
# autorización de ruta dice DÓNDE se puede escribir y no dice QUÉ, que es lo único que
# importaba.
#
# Aquí cada excepción lleva su CLASE declarada y su clase impone una regla sobre el
# CONTENIDO:
#
#   CÓDIGO DE VALIDADOR   idéntico a lo publicado en `HEAD`. La autorización era para un
#                         arreglo NOMBRADO —`N158g`—, no para el fichero a perpetuidad
#   HUELLA DE INTEGRIDAD  igual a la que esta batería RECALCULA por su cuenta sobre el
#                         árbol. Es el único campo que no se puede creer: es la evidencia
#                         que detectaría la mutilación del resto
#   EVIDENCIA DERIVADA    idéntica a lo publicado. La publica el runner y es determinista;
#                         si difiere, o el runner no se ha vuelto a pasar o alguien la
#                         escribió a mano. **Ya no hay comodín de directorio**: se enumera
#                         fichero a fichero desde el disco
#   DOCUMENTO             idéntico a lo publicado
#
# La huella se RECALCULA aquí, con la especificación que `kernel/operativo/validadores/
# huella.py` publica en su propia cabecera —ámbitos, extensiones y exclusiones—, y **no se
# ejecuta el código del kernel para obtenerla**: pedirle su huella al árbol que se está
# auditando es preguntarle al sospechoso.
_HUELLA_AMBITOS = ("kernel", "packs", "tooling")
_HUELLA_EXT = (".md", ".yaml", ".yml", ".py", ".sh", ".toml")
_HUELLA_DIR_FUERA = ("__pycache__", ".git", ".pytest_cache")
_HUELLA_PREFIJO_FUERA = ("legacy-",)
_HUELLA_FICHERO_FUERA = (".upstream-hash",)

def _recalcular_huella():
    acumulado = hashlib.sha256()
    vistos = 0
    for ambito in _HUELLA_AMBITOS:
        origen = os.path.join(RAIZ, ambito)
        if not os.path.isdir(origen):
            continue
        rutas = []
        for base, dirs, ficheros in os.walk(origen):
            dirs[:] = sorted(d for d in dirs
                             if d not in _HUELLA_DIR_FUERA
                             and not d.startswith(_HUELLA_PREFIJO_FUERA))
            for nombre in sorted(ficheros):
                if nombre in _HUELLA_FICHERO_FUERA:
                    continue
                if nombre.endswith(_HUELLA_EXT):
                    rutas.append(os.path.join(base, nombre))
        for ruta in sorted(rutas, key=lambda p: os.path.relpath(p, RAIZ)):
            rel = _rel(ruta)
            acumulado.update(rel.encode("utf-8"))
            acumulado.update(b"\0")
            with io.open(ruta, "rb") as fh:
                acumulado.update(hashlib.sha256(fh.read()).digest())
            vistos += 1
    return acumulado.hexdigest()[:16], vistos

_CLASES = {}
for _f in sorted(COD_AUTORIZADO):
    _CLASES[_f] = "CÓDIGO DE VALIDADOR"
for _f in sorted(DOC_AUTORIZADO):
    _CLASES[_f] = "DOCUMENTO"
for _f in sorted(HUELLA):
    _CLASES[_f] = "HUELLA DE INTEGRIDAD"
_dir_ev_kernel = os.path.join(RAIZ, "kernel/operativo/pruebas/evidencia")
if os.path.isdir(_dir_ev_kernel):
    for _n in sorted(os.listdir(_dir_ev_kernel)):
        _r = "kernel/operativo/pruebas/evidencia/" + _n
        if os.path.isfile(os.path.join(RAIZ, _r)):
            _CLASES[_r] = "EVIDENCIA DERIVADA"

# ── `S1-02`, TERCERA SEDE · LA EVIDENCIA DERIVADA NO SE JUZGA CONTRA `HEAD` ──────
#
# La regla «EVIDENCIA DERIVADA idéntica a lo publicado» se evalúa contra `HEAD`, y por eso
# **confirmar una evidencia manipulada la volvía legítima**: el séptimo gate midió que una
# sentencia de cierre añadida a `fuentes-salida.txt` daba `38/38` una vez commiteada. Es la
# misma inercia-tras-confirmar de `S1-02`, en la tercera sede.
#
# **La evidencia no puede compararse contra la base** —cambia legítimamente en cada tanda—
# ni la batería puede ejecutar el runner. Lo que SÍ puede hacer es exigir la **FORMA que su
# PRODUCTOR garantiza**, que es una propiedad del fichero y no de ningún commit:
#
#   · la CABECERA son las CUATRO líneas exactas que `registrar_evidencia.py` escribe, con
#     `# evidencia de:`, `# orden:`, `# codigo:` y el separador
#   · el `# codigo:` tiene que ser **0**: el runner publica SÓLO si el código fue cero, de
#     modo que una evidencia publicada con código distinto no la escribió él
#   · la última línea no vacía es el CIERRE que su validador emite —«N superadas · M
#     fallidas», «N infracciones detectadas · M NO detectadas», el resumen del linter o el
#     `OK` de `unittest`—. **Nada puede venir después del cierre de su productor**: eso es
#     texto que el runner no escribió, y es exactamente por donde entraba la sentencia
#
# Es de RESTA: no añade ninguna comprobación al censo, vive dentro de `G-30`, y cierra la
# tercera cara de la clase que `S1-02` nombra.
_CIERRE_EVIDENCIA = re.compile(
    r"^(?:\d+ superadas · \d+ fallidas"
    r"|\d+ infracciones detectadas · \d+ NO detectadas"
    r"|OK"
    r"|FAILED \(.*\)"
    r"|bloques canónicos: .*errores: \d+.*"
    r"|\d+/\d+ .*)$")


def _forma_de_evidencia(rel):
    """Los defectos de FORMA de una evidencia derivada, o lista vacía (`S1-02`)."""
    try:
        cuerpo = leer(os.path.join(RAIZ, rel))
    except SedeIlegible as e:
        return [f"{rel} [EVIDENCIA DERIVADA]: ilegible ({e})"]
    lineas = cuerpo.split("\n")
    if len(lineas) < 5:
        return [f"{rel} [EVIDENCIA DERIVADA]: no tiene la cabecera de cuatro líneas que su "
                f"productor escribe"]
    fallos = []
    if not lineas[0].startswith("# evidencia de: ") \
       or not lineas[1].startswith("# orden:") \
       or not lineas[2].startswith("# codigo:") \
       or not lineas[3].startswith("# ----"):
        fallos.append(f"{rel} [EVIDENCIA DERIVADA]: su cabecera no es la que "
                      f"`registrar_evidencia.py` escribe. Una evidencia sin la cabecera de "
                      f"su productor no dice de quién es")
    _m_cod = re.match(r"# codigo:\s+(\d+)", lineas[2])
    if not _m_cod or _m_cod.group(1) != "0":
        fallos.append(f"{rel} [EVIDENCIA DERIVADA]: su cabecera declara un código distinto "
                      f"de 0, y el runner PUBLICA SÓLO si el código fue cero: esta "
                      f"evidencia no la escribió él")
    _vivas = [l for l in lineas if l.strip()]
    if _vivas and not _CIERRE_EVIDENCIA.match(_vivas[-1].strip()):
        fallos.append(f"{rel} [EVIDENCIA DERIVADA]: TEXTO DESPUÉS DEL CIERRE de su "
                      f"productor — «{_vivas[-1].strip()[:70]}». El runner no escribe nada "
                      f"tras el resumen de su validador, luego esto lo escribió una mano. "
                      f"La evidencia se juzga por la FORMA QUE SU PRODUCTOR GARANTIZA y no "
                      f"contra `HEAD`, porque contra `HEAD` bastaba confirmarla (`S1-02`)")
    return fallos


_g30 = []
if _mod_head_raw is None or _head_arbol_raw is None:
    _g30.append("GIT NO RESPONDE: no se puede fijar el contenido publicado de ninguna "
                "excepción del kernel")
else:
    for _ev in sorted(f for f in _CLASES if _CLASES[f] == "EVIDENCIA DERIVADA"):
        _g30 += _forma_de_evidencia(_ev)
    _kernel_disco = sorted(f for f in _disco if f.startswith("kernel/"))
    # 1 · CONTENIDO · ningún fichero del kernel difiere de lo publicado, excepción incluida
    for _f in sorted(f for f in _mod_head if f.startswith("kernel/")):
        _g30.append(f"{_f} [{_CLASES.get(_f, 'SIN CLASIFICAR')}]: su CONTENIDO difiere del "
                    f"publicado en `HEAD`. La excepción autoriza un cambio NOMBRADO y ya "
                    f"confirmado, no ediciones posteriores del mismo fichero")
    # 2 · CLASIFICACIÓN · toda excepción declarada tiene clase, y toda clase tiene regla
    for _f in sorted(set(COD_AUTORIZADO) | set(DOC_AUTORIZADO) | set(HUELLA)):
        if _f not in _CLASES:
            _g30.append(f"{_f}: autorizado sin CLASE declarada, luego sin regla de "
                        f"contenido que cumplir")
        if _f not in _head_arbol:
            _g30.append(f"{_f}: autorizado y NO publicado en `HEAD`; una excepción sobre un "
                        f"fichero sin versión publicada no fija ningún contenido")
    if not any(v == "EVIDENCIA DERIVADA" for v in _CLASES.values()):
        _g30.append("cero ficheros de evidencia derivada enumerados: el comodín de "
                    "directorio se retiró y no lo sustituye ninguna enumeración")
    # 2bis · CONTENIDO · cada clase impone una REGLA SOBRE EL CONTENIDO, y no «ser igual
    #        a `HEAD`», que deja de decir nada en cuanto el cambio se confirma.
    #
    # `T-01`. El adjudicador vació el validador a `import sys; sys.exit(0)`, falsificó sus
    # tres evidencias, reancló la huella **con el valor que esta misma batería publica al
    # fallar**, hizo `git commit` — y obtuvo `37/37 en verde` con el porcelain vacío. Lo
    # reprodujimos igual. La causa es que las dos referencias —`HEAD` y `.upstream-hash`—
    # las escribe quien edita, de modo que confirmar el ataque lo volvía invisible.
    #
    # Aquí la clase CÓDIGO DE VALIDADOR se fija por lo que el fichero TIENE QUE SER, y se
    # contrasta contra la EVIDENCIA que él mismo produce, que es otro fichero y otra clase:
    # un validador vaciado no puede a la vez declarar cero mutaciones y publicar una
    # evidencia que reporta sesenta y siete. **La huella deja de ser el conjunto libre por
    # el que se lavaba la mutilación**: ya no basta con reanclarla, porque la mutilación se
    # ve en el contenido y no en la huella.
    _EV_KERNEL = "kernel/operativo/pruebas/evidencia/"
    for _f, _clase in sorted(_CLASES.items()):
        try:
            _cuerpo = leer(os.path.join(RAIZ, _f))
        except SedeIlegible as _e:
            _g30.append(f"{_f} [{_clase}]: {_e}")
            continue
        if _clase == "CÓDIGO DE VALIDADOR":
            _ids_cod = re.findall(r'Mutacion\(\s*"([A-Za-z0-9_]+)"', _cuerpo)
            if not _ids_cod:
                _g30.append(f"{_f} [CÓDIGO DE VALIDADOR]: no define NI UNA mutación. Un "
                            f"validador de pruebas negativas sin mutaciones no prueba "
                            f"nada, y la autorización era para un arreglo NOMBRADO, no "
                            f"para vaciarlo")
                continue
            _base_ev = os.path.basename(_f).replace("comprobar_", "").replace(".py", "")
            _ruta_ev = _EV_KERNEL + _base_ev + "-salida.txt"
            if _ruta_ev not in _CLASES:
                _g30.append(f"{_f} [CÓDIGO DE VALIDADOR]: no hay evidencia derivada "
                            f"`{_ruta_ev}` con la que contrastar su contenido")
                continue
            try:
                _tev = leer(os.path.join(RAIZ, _ruta_ev))
            except SedeIlegible as _e:
                _g30.append(f"{_ruta_ev}: {_e}")
                continue
            _ids_ev = re.findall(r"^(?:OK|FALLO)\s+(\S+)\s", _tev, re.M)
            _huerfanas = sorted(set(_ids_cod) - set(_ids_ev))
            if _huerfanas:
                _g30.append(f"{_f}: define mutaciones que su evidencia NO reporta: "
                            f"{_huerfanas}. O el validador cambió sin volver a pasarlo, o "
                            f"la evidencia describe otro código")
            _m_cola = re.search(r"(\d+) infracciones detectadas · (\d+) NO detectadas",
                                _tev)
            if not _m_cola:
                _g30.append(f"{_ruta_ev}: no publica su cola «N infracciones detectadas · "
                            f"M NO detectadas», que es lo único que dice si la suite corrió")
            else:
                _n_det, _n_no = int(_m_cola.group(1)), int(_m_cola.group(2))
                if _n_det != len(_ids_ev):
                    _g30.append(f"{_ruta_ev}: su cola dice {_n_det} detectadas y el cuerpo "
                                f"enumera {len(_ids_ev)}")
                if _n_no:
                    _g30.append(f"{_ruta_ev}: {_n_no} mutaciones NO detectadas")
                if _n_det < len(_ids_cod):
                    _g30.append(f"{_ruta_ev}: reporta {_n_det} y el código define "
                                f"{len(_ids_cod)} mutaciones explícitas")
            # y el censo del campo `espera`, DERIVADO y publicado: sin él una mutación se
            # da por detectada porque la prueba falló, sin comprobar que falló POR ESO
            # (`T-13`). Se publica aquí porque el remedio vive en `kernel/`, fuera del
            # perímetro de escritura de esta tanda, y una carencia publicada es refutable
            _sin_espera = len(_ids_cod) - len(re.findall(r"espera\s*=", _cuerpo))
        elif _clase == "EVIDENCIA DERIVADA":
            if not re.search(r"^#\s*orden:\s*\S", _cuerpo, re.M):
                _g30.append(f"{_f} [EVIDENCIA DERIVADA]: no declara la ORDEN que la "
                            f"produce, luego no se puede volver a derivar ni refutar")
            _m_ord = re.search(r"^#\s*orden:.*?(kernel/[A-Za-z0-9_./-]+\.py)",
                               _cuerpo, re.M)
            if _m_ord and not os.path.isfile(os.path.join(RAIZ, _m_ord.group(1))):
                _g30.append(f"{_f}: dice derivarse de `{_m_ord.group(1)}`, que no existe")
        elif _clase == "HUELLA DE INTEGRIDAD":
            if not re.fullmatch(r"[0-9a-f]{8,64}", _cuerpo.strip()):
                _g30.append(f"{_f} [HUELLA DE INTEGRIDAD]: su contenido no es una huella "
                            f"hexadecimal: «{_cuerpo.strip()[:40]}»")
    # 3 · HUELLA · recalculada por esta batería, contra la que el árbol publica
    try:
        _huella_calc, _n_huella = _recalcular_huella()
        _huella_pub = leer(os.path.join(RAIZ, "kernel/.upstream-hash")).strip()
    except (SedeIlegible, OSError) as _e:
        _huella_calc = _huella_pub = None
        _n_huella = 0
        _g30.append(f"la huella no se puede establecer ({_e}), y sin ella la mutilación de "
                    f"un validador no deja rastro")
    if _huella_calc is not None and _huella_calc != _huella_pub:
        _g30.append(f"`kernel/.upstream-hash` publica `{_huella_pub}` y el árbol deriva "
                    f"`{_huella_calc}` sobre {_n_huella} ficheros. La huella cubre el "
                    f"CÓDIGO de los validadores: si no cuadra, o el kernel cambió sin "
                    f"reanclarla o la huella se escribió a mano")
check("G-30",
      "la excepción del kernel se fija por CONTENIDO y por CLASIFICACIÓN, con la huella RECALCULADA (falla CERRADO sin git)",
      not _g30,
      "; ".join(_g30) or
      f"{len(_CLASES)} ficheros del kernel con clase declarada "
      f"({len(set(_CLASES.values()))} clases) · ninguno difiere de `HEAD` · el validador "
      f"autorizado define {len(_ids_cod)} mutaciones y su evidencia reporta "
      f"{len(_ids_ev)}, sin una NO detectada · huella recalculada sobre {_n_huella} "
      f"ficheros = `{_huella_pub}`" +
      (f" · LIMITACIÓN DECLARADA: {_sin_espera} de esas {len(_ids_cod)} mutaciones no "
       f"llevan campo `espera` y son VACUAS EN POTENCIA (`T-13`); el remedio vive en "
       f"`kernel/`, que esta batería no escribe" if _sin_espera > 0 else ""))


# ── G-31 · ninguna comprobación se apaga con una PALABRA ────────────────
#
# Protección 10, que es la generalización de la 2 y la 4. Dos de los ocho árboles
# defectuosos del gate se construyeron **añadiendo palabras**: « (sin regresión)» al final
# de la línea que lleva la cifra al Owner apagaba `G-26`, y la palabra «RETIRADA» dentro de
# un párrafo que DEROGABA la retirada apagaba `G-01`. Las dos correcciones podrían haberse
# escrito para esos dos casos y dejar viva la clase entera.
#
# Esto la cierra como clase: se toma cada evaluador que decidía por presencia de palabra, se
# le pone delante el mismo dato con cada una de las palabras gatillo pegadas, y **se exige
# que el veredicto NO cambie**. Si mañana alguien vuelve a introducir un interruptor léxico,
# estos fixtures se ponen rojos aunque el contraejemplo no exista todavía.
# `A3`. Esta lista eran las palabras de `T-06` y de `Q-04`, y **ninguna de las que apagaban
# de verdad**: `X` apagó `G-26` con «decía », «en vez de » y «reanclado », y ninguna de las
# tres estaba aquí. La comprobación que existe para cazar interruptores léxicos no probaba
# el interruptor léxico que había. Los verbos retirados entran, y su sede es la constante
# `_VERBOS_QUE_YA_NO_APAGAN`: si mañana alguien reinstala uno, este fixture lo caza sin
# esperar a que exista el contraejemplo.
_PALABRAS_GATILLO = ("histórico", "HISTÓRICO", "[HISTÓRICO]", "regresión", "sin regresión",
                     "retirada", "RETIRADA", "sustituida", "caducado", "superado") \
    + _VERBOS_QUE_YA_NO_APAGAN
_g31 = []
# `Z1-04`≡`Z-06`. El detalle publicaba «21 palabras gatillo × **4 evaluadores**» mientras el
# bloque `c` no invocaba ninguno: se ejercitaban TRES y el número estaba escrito a mano.
# Aquí cada bloque REGISTRA el evaluador que llama, y el detalle publica lo que se ejecutó.
_ejercitados_g31 = set()

# a · el control de RECUENTOS no se apaga: la cifra falsa se sigue viendo
_PLANTILLA_SEDE = (
    "## Siguiente acción exacta\n\n"
    "5  QUÉ LLEVAR AL OWNER   las **ONCE** presiones de §16 vigentes%s\n")
for _w in ("",) + _PALABRAS_GATILLO:
    _sufijo = "" if not _w else f" ({_w})"
    _txt = _PLANTILLA_SEDE % _sufijo
    _hallado = _sedes(_NUM + r"\s+(?:presiones|PRESIONES)", _txt,
                      contexto=r"§16|vigente|VIGENTES|Owner")
    _ejercitados_g31.add(_sedes.__name__)
    if [v for _, v in _hallado] != [11]:
        _g31.append(f"recuentos: añadir «{_w or '∅'}» a la línea del Owner cambia lo que la "
                    f"comprobación ve — esperado [11], obtenido {[v for _, v in _hallado]}")

# b · la POLARIDAD no se apaga: el párrafo que reinstala sigue siendo VIGENTE
_PLANTILLA_POL = ("NORMA VIGENTE REINSTAURADA: el estado en cuarentena vive en "
                  "`estado/cuarentena/<ID>/` y esa ruta es CANONICA y fuente de verdad "
                  "para todo el sistema.%s")
for _w in ("",) + _PALABRAS_GATILLO:
    _sufijo = "" if not _w else f" La nota que hablaba de una {_w} queda SIN EFECTO."
    _ejercitados_g31.add(_polaridad.__name__)
    if _polaridad(_PLANTILLA_POL % _sufijo) != "VIGENTE":
        _g31.append(f"polaridad: añadir «{_w or '∅'}» convierte en RETIRADO un párrafo que "
                    f"declara la ruta CANÓNICA y fuente de verdad")
# y la mitad contraria, que es lo que impide que esto sea un «siempre VIGENTE»:
if _polaridad("la ruta `estado/cuarentena/<TX>/` queda RETIRADA de la arquitectura "
              "vigente, y la preservación vive donde ya existe un plano") != "RETIRADO":
    _g31.append("polaridad: una retirada limpia deja de reconocerse como RETIRADO, y "
                "entonces la comprobación sería un rojo permanente que nadie puede cerrar")
if _polaridad("aquí se menciona `estado/cuarentena/` y no se dice nada más") \
        != "INDETERMINADO":
    _g31.append("polaridad: el silencio no se clasifica como INDETERMINADO, luego un "
                "párrafo que no se pronuncia pasaría por bueno")

# c · el contraste de ESTADO no se apaga: una calificación añadida no lo conserva.
# `Z1-04`≡`Z-06`. Esto eran DOS `if` sobre f-strings comparadas con un literal
# —`if f"CERRADA {_w}" in ("CERRADA",)`—, **insatisfacibles por construcción y sin invocar
# ningún evaluador de esta batería**: un fixture que no puede fallar dentro de la
# comprobación cuya tesis es que ninguno puede serlo. Ahora llama a `_estado_casa`, que es
# el mismo que `G-16c` usa para juzgar el árbol: revertirlo a `startswith` pone esto en rojo.
_ADMITIDOS_G31 = ("CERRADA",)
for _sufijo in ("SOLO EN PARTE, SIGUE ABIERTA Y BLOQUEA F5",) + _PALABRAS_GATILLO:
    _ejercitados_g31.add(_estado_casa.__name__)
    if _estado_casa(f"CERRADA {_sufijo}", _ADMITIDOS_G31):
        _g31.append(f"estado: «CERRADA {_sufijo}» se considera igual a «CERRADA». El "
                    f"contraste de `G-16c` ha dejado de ser por IGUALDAD, y una "
                    f"calificación añadida detrás vuelve a cambiar el estado (`Q-06`)")
# y la mitad contraria, que es lo que impide que esto sea un «siempre falso» —que es
# exactamente lo que era—: el estado limpio SÍ tiene que casar
if not _estado_casa("CERRADA", _ADMITIDOS_G31):
    _g31.append("estado: el estado limpio «CERRADA» deja de casar con el estado admitido, y "
                "entonces ninguna condición podría declararse cerrada nunca")

# d · la MARCA histórica es estructural: una palabra suelta no abre región, una etiqueta sí
_ejercitados_g31.add(_regiones_historicas.__name__)
if _regiones_historicas("una línea que habla de una regresión y de algo histórico\n"):
    _g31.append("región histórica: una palabra suelta en la línea abre una región histórica")
if not _regiones_historicas("**[HISTÓRICO · lo que aquella tanda validó]**\ncifra vieja\n"):
    _g31.append("región histórica: una etiqueta estructural NO abre región, y entonces no "
                "hay forma legítima de marcar un bloque histórico")
if not _regiones_historicas("PRESIONES           **[HISTÓRICO]** ONCE vigentes entonces\n"):
    _g31.append("región histórica: la forma de CAMPO con etiqueta no abre región")
# y la mitad que `T-06` explotó: una etiqueta NO exime lo que queda FUERA de su bloque
_FIX_FUGA = ("> **[ESTADO ANTERIOR · lo que aquella tanda validó]**\n"
             "ONCE presiones vigentes de §16\n")
_regs_fuga = _regiones_historicas(_FIX_FUGA)
if not _regs_fuga:
    _g31.append("región histórica: una etiqueta dentro de una cita no abre región, y "
                "entonces no hay forma legítima de marcar histórico un bloque citado")
if any(a <= _FIX_FUGA.index("ONCE") < b for a, b in _regs_fuga):
    _g31.append("región histórica: una etiqueta escrita DENTRO de una cita exime una línea "
                "que está FUERA de la cita. Es el vector de `T-06`: una sola línea devolvía "
                "la batería a verde sobre una cifra viva falsa")
_FIX_BLOQUE = ("**[HISTÓRICO · el censo de entonces]**\nONCE presiones vigentes\n\n"
               "DIECISÉIS presiones vigentes de §16\n")
if any(a <= _FIX_BLOQUE.index("DIECISÉIS") < b
       for a, b in _regiones_historicas(_FIX_BLOQUE)):
    _g31.append("región histórica: una etiqueta exime el bloque SIGUIENTE al suyo, separado "
                "por una línea en blanco. La marca declara alcance, y su alcance es su "
                "bloque")
if not any(a <= _FIX_BLOQUE.index("ONCE") < b
           for a, b in _regiones_historicas(_FIX_BLOQUE)):
    _g31.append("región histórica: una etiqueta no exime ni su propio bloque, y entonces "
                "marcar historia dejaría de ser posible")
# e · los VERBOS RETIRADOS, puestos DELANTE de la cifra, que es exactamente donde apagaban.
# El sufijo de `a` los pega DETRÁS, y detrás nunca apagaron nada: `_VERBO_DE_CITA` anclaba
# al final del texto que PRECEDE a la ocurrencia. Sin este fixture, `A3` volvería a pasar.
for _v in _VERBOS_QUE_YA_NO_APAGAN:
    _txt = ("## Siguiente acción exacta\n\n"
            "5  QUÉ LLEVAR AL OWNER   %s ONCE presiones de §16 vigentes\n" % _v)
    _hallado = [v for _, v in _sedes(_NUM + r"\s+(?:presiones|PRESIONES)", _txt,
                                     contexto=r"§16|vigente|VIGENTES|Owner")]
    if _hallado != [11]:
        _g31.append(f"recuentos: escribir «{_v} » DELANTE de la cifra la hace invisible — "
                    f"esperado [11], obtenido {_hallado}. Es `A3`: un verbo en prosa no "
                    f"puede desactivar una comprobación")
# y la mitad contraria, que impide que esto sea un «siempre visible»: la cita ESTRUCTURAL
# —comillas angulares— sí exime, porque delimita la ocurrencia y se ve al leer
_TXT_COMILLAS = ("## Siguiente acción exacta\n\n"
                 "5  QUÉ LLEVAR AL OWNER   la línea de la tanda anterior «ONCE presiones "
                 "de §16 vigentes» quedó atrás\n")
if _sedes(_NUM + r"\s+(?:presiones|PRESIONES)", _TXT_COMILLAS,
          contexto=r"§16|vigente|VIGENTES|Owner"):
    _g31.append("citas: una cifra DENTRO de «…» se cuenta como afirmación viva, y entonces "
                "no queda ninguna forma de citar una cifra pasada en una línea")

check("G-31",
      "ninguna comprobación se desactiva escribiendo una palabra: recuentos, polaridad, estado y marca histórica, con el mismo dato y las palabras gatillo pegadas",
      not _g31,
      "; ".join(_g31) or
      f"{len(_PALABRAS_GATILLO)} palabras gatillo × {len(_ejercitados_g31)} evaluadores "
      f"REALMENTE INVOCADOS ({', '.join(sorted(_ejercitados_g31))}), y ninguno cambia de "
      f"veredicto; las formas legítimas de marcar historia siguen funcionando, y una "
      f"etiqueta no exime lo que queda fuera de su bloque ni fuera de su cita")

# ── G-32 · PRODUCTOR declarado para TODOS los niveles de certificación ──
#
# Protección 11 del Owner. `O17` regla 12: «cada nivel conserva PRODUCTOR, EVIDENCIA,
# SUJETO, VIGENCIA y CONDICIÓN DE INVALIDACIÓN propios». El GRAVE nº 2 del documento 22 fue
# exactamente que el nivel **Estructural no tenía productor**, y con él `O12` no era
# satisfacible por ningún recorrido. Aquí los niveles se DERIVAN de la tabla de §9.1 —no se
# escriben «cuatro» ni sus nombres— y se exige productor para cada uno en las DOS sedes que
# lo declaran: la tabla de §9.1 y el bloque «PRODUCTOR DE CADA NIVEL» de §9.2.
# ── `O17` y `D107`, LEÍDAS de verdad ────────────────────────────────────
#
# `T-08`. `G-32` y `G-33` llevan escrito en su comentario que sus reglas «derivan de `O17`
# y de su propagación `D107`», y **ninguna línea de código leía la fila `| O17 |`**:
# `grep -n 'O17'` daba cinco golpes y los cinco eran comentario o diagnóstico. `G-21`
# protege `O1`-`O16` y se detiene justo antes. El adjudicador **sustituyó la fila `O17` por
# su negación exacta y borró la fila `D107`** —que no deja hueco en `G-20`, por ser la
# última— y la batería siguió en `37/37`. Lo reprodujimos igual. La resolución del Owner
# que ESTE gate existe para certificar podía negarse entera sin que nada se moviera.
#
# Aquí se leen las dos: la FILA de `O17`, sus DOCE reglas —cuyo cardinal se deriva de la
# frase que las anuncia y se contrasta con las que enumera—, y la fila de PROPAGACIÓN que
# declara a `O17` su única fuente. Cada regla que esta batería aplica se exige PRESENTE en
# su sede: si `O17` deja de decirlo, lo que la batería comprueba deja de derivar de nada, y
# eso es rojo, no verde.
# cada hallazgo se anota con la comprobación que lo tiene que publicar: `"32"`, `"33"` o
# `"ambas"` — la sede de `O17` sostiene a las dos y ninguna puede callarla
_o17 = []
_fila_o17 = [l for l in _tdec.split("\n") if re.match(r"^\|\s*`?O17`?\s*\|", l)]
if not _fila_o17:
    _o17.append(("ambas",
                 "la fila `| O17 |` NO aparece en el registro de decisiones: la resolución "
                 "del Owner de la que estas comprobaciones dicen derivar no está"))
else:
    _celda_o17 = _fila_o17[0].strip("|").split("|")[1]
    if not re.search(r"NIVEL\s+ESTRUCTURAL\s+SE\s+PRODUCE\s+AL\s+INICIO\s+DE\s+CADA\s+"
                     r"MACROCIRCUITO", _celda_o17, re.I):
        _o17.append(("ambas",
                     f"la fila `O17` ya NO resuelve que el nivel Estructural se produce al "
                    f"inicio de CADA macrocircuito; su celda dice «"
                    f"{' '.join(_celda_o17.split())[:120]}…». `G-32` y `G-33` comprueban "
                     f"una resolución que su sede ha dejado de contener"))
# las DOCE reglas, con su cardinal DERIVADO de la frase que las anuncia
_m_n_reglas = re.search(r"[Ll]as\s+" + _NUM + r"\s+reglas obligatorias que\s+`?O17`?\s+fija",
                        _tdec)
_m_blq_reglas = re.search(r"reglas obligatorias que\s+`?O17`?\s+fija.*?```text\n(.*?)```",
                          _tdec, re.S)
_REGLAS_O17 = {}
if not _m_n_reglas or not _m_blq_reglas:
    _o17.append(("ambas", "`O17` no publica su bloque «las <n> reglas obligatorias»: sin "
                 "él, las reglas que `G-32` y `G-33` aplican no tienen sede"))
else:
    for _mr in re.finditer(r"^\s*(\d{1,2})\s{2,}(.*(?:\n(?!\s*\d{1,2}\s{2,}).*)*)",
                           _m_blq_reglas.group(1), re.M):
        _REGLAS_O17[int(_mr.group(1))] = " ".join(_mr.group(2).split())
    _n_pub = _num(_m_n_reglas.group(1))
    if _n_pub is not None and _n_pub != len(_REGLAS_O17):
        _o17.append(("ambas", f"`O17` anuncia {_n_pub} reglas obligatorias y su bloque "
                     f"enumera {len(_REGLAS_O17)}"))
# y cada regla que ESTA batería aplica, exigida PRESENTE en la regla que la sostiene
_APLICADAS = (
    (1,  r"EXACTAMENTE UNA certificaci[óo]n Estructural",      "`G-33` FASE 0 propia"),
    (2,  r"ANTES de cualquier mutaci[óo]n can[óo]nica",         "`G-33` `_fase0_conforme`"),
    (4,  r"nivel superior NO implica",                          "`G-33` prueba negativa 3"),
    (5,  r"se BLOQUEA",                                         "`G-33` `_fase0_conforme`"),
    (7,  r"SUJETO de la certificaci[óo]n identifica",           "`G-33` sujeto de §9.6"),
    (8,  r"todas sus entradas y huellas siguen ID[ÉE]NTICAS",   "`G-33` prueba negativa 2"),
    (9,  r"cada ejecuci[óo]n produce SU PROPIA declaraci[óo]n", "`G-33` prueba negativa 2"),
    (10, r"copiar una certificaci[óo]n anterior",               "`G-33` prueba negativa 2"),
    (12, r"PRODUCTOR, EVIDENCIA, SUJETO, VIGENCIA y CONDICI[ÓO]N DE INVALIDACI[ÓO]N",
         "`G-32` productor de cada nivel"),
)
for _nr, _pat, _quien in _APLICADAS:
    _dest = "32" if _quien.startswith("`G-32`") else "33"
    _txt_r = _REGLAS_O17.get(_nr, "")
    if not _txt_r:
        _o17.append((_dest,
                     f"`O17` no publica su regla {_nr}, y {_quien} dice derivar de ella"))
    elif not re.search(_pat, _txt_r):
        _o17.append((_dest, f"la regla {_nr} de `O17` ya no dice lo que {_quien} "
                     f"comprueba: «{_txt_r[:100]}…»"))
# la PROPAGACIÓN: la fila del registro que declara a `O17` su única fuente
_filas_prop = [l for l in _tdec.split("\n")
               if re.match(r"^\|\s*D\d+\s*\|", l) and re.search(r"`O17`[^|]*[úu]nica fuente", l)]
if not _filas_prop:
    _o17.append(("33",
                 "ninguna fila `D` del registro declara a `O17` su ÚNICA FUENTE: la "
                 "propagación que `G-33` dice comprobar no está registrada. Borrarla no "
                 "deja hueco en `G-20` si era la última, y por eso se busca por lo que "
                 "dice y no por su número"))
else:
    _prop = _filas_prop[0]
    _id_prop = re.match(r"^\|\s*(D\d+)\s*\|", _prop).group(1)
    _macros_prop = sorted(set(re.findall(r"§(8\.\d+)", _prop)))
    if _macros_prop != sorted(_MACROS):
        _o17.append(("33", f"`{_id_prop}` propaga `O17` a {_macros_prop} y §8 deriva "
                     f"{sorted(_MACROS)}"))
    if "gate:sistema-conforme" not in _prop:
        _o17.append(("33", f"`{_id_prop}` no nombra el contrato compartido "
                     f"`gate:sistema-conforme`, que es lo que la propagación instala"))

_b91 = bloques.get("§9.1", "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "9.1"))
_b92 = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "9.2")
_g32 = [m for d, m in _o17 if d in ("32", "ambas")]
_cab91 = [l for l in _b91.split("\n") if l.startswith("| nivel |")]
_niveles = {}
if not _cab91:
    _g32.append("§9.1 no publica su tabla de niveles con cabecera `| nivel |`")
else:
    _cols = [c.strip().strip("*").lower() for c in _cab91[0].strip("|").split("|")]
    if "propietario" not in _cols:
        _g32.append(f"la tabla de §9.1 no tiene columna de propietario: {_cols}")
    else:
        _ipro = _cols.index("propietario")
        for _l in _b91.split("\n"):
            _m = re.match(r"^\| \*\*([A-Za-zÁÉÍÓÚáéíóú]+)\*\* \|", _l)
            if not _m:
                continue
            _celdas = [c.strip() for c in _l.strip("|").split("|")]
            _niveles[_m.group(1)] = _celdas[_ipro] if _ipro < len(_celdas) else ""
if not _niveles:
    _g32.append("cero niveles derivados de la tabla de §9.1: sin objeto, esta comprobación "
                "sería un verde por omisión")
for _n, _prod in sorted(_niveles.items()):
    if not re.search(r"`[A-Z]{3}`", _prod):
        _g32.append(f"el nivel «{_n}» no declara PRODUCTOR en §9.1: su celda dice «{_prod}»")
# la cadena de §9.2, DERIVADA de su propia línea, y el bloque de productores
_m_cadena = re.search(r"^([a-záéíóú]+(?:\s*◀──\s*[a-záéíóú]+)+)\s*$", _b92, re.M)
_CADENA = [x.strip() for x in _m_cadena.group(1).split("◀──")] if _m_cadena else []
if not _CADENA:
    _g32.append("§9.2 no publica la cadena `estructural ◀── operativo ◀── …`, que es de "
                "donde sale la jerarquía")
elif len(_CADENA) != len(_niveles):
    _g32.append(f"la cadena de §9.2 tiene {len(_CADENA)} niveles {_CADENA} y la tabla de "
                f"§9.1 deriva {len(_niveles)} {sorted(_niveles)}")
_m_prod92 = re.search(r"PRODUCTOR DE CADA(.*?)(?=^## |\Z)", _b92, re.S | re.M)
_b_prod92 = _m_prod92.group(1) if _m_prod92 else ""
if not _b_prod92:
    _g32.append("§9.2 no publica el bloque «PRODUCTOR DE CADA NIVEL», que es la sede donde "
                "`O17` obliga a que cada nivel tenga el suyo")
else:
    for _n in _CADENA:
        _m_l = re.search(r"^\s*" + re.escape(_n) + r"\s{2,}(.+)$", _b_prod92, re.M)
        if not _m_l:
            _g32.append(f"§9.2 no nombra productor para el nivel «{_n}»")
        elif not _m_l.group(1).strip():
            _g32.append(f"§9.2 nombra el nivel «{_n}» con productor VACÍO")
check("G-32",
      "todos los niveles de certificación —derivados de §9.1, no escritos— tienen PRODUCTOR declarado en §9.1 y en §9.2",
      not _g32,
      "; ".join(_g32) or
      f"{len(_niveles)} niveles derivados ({', '.join(sorted(_niveles))}) · cadena de §9.2 "
      f"{' ◀── '.join(_CADENA)} · cada uno con productor en las dos sedes")

# ── G-33 · los MACROCIRCUITOS, su FASE 0 y las tres pruebas negativas ───
#
# Protecciones 12, 13, 14 y 15, todas derivadas de `O17` y de su propagación `D107`.
# **Nada de esto se escribe:** los macrocircuitos se derivan de las secciones §8.x del
# documento 11 —§8.0 es el encuadre y no es un macrocircuito—, las reglas se derivan de
# `O17` en el registro, y los seis identificadores del sujeto se derivan de §9.6. Escribir
# «cuatro» aquí sería exactamente el censo a mano que esta batería existe para cazar: el
# día que naciera un quinto recorrido, la comprobación seguiría verde sobre un mapa que ya
# no es el suyo.
_b96 = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "9.6")
_g33 = [m for d, m in _o17 if d in ("33", "ambas")]
if not _MACROS:
    _g33.append("cero macrocircuitos derivados de §8: sin objeto, esto sería un verde por "
                "omisión")

# 1 · cada macrocircuito produce su Estructural en FASE 0, ANTES de mutar
def _fase0_conforme(bloque):
    """Los requisitos de la FASE 0 que `O17` impone, evaluados sobre el texto de una fase.

    Devuelve la lista de los que FALTAN. Se usa sobre los macrocircuitos reales y sobre los
    fixtures sintéticos, que es lo que convierte la prueba negativa en una prueba.
    """
    faltan = []
    if not re.search(r"FASE 0", bloque):
        faltan.append("no declara FASE 0")
    if "gate:sistema-conforme" not in bloque:
        faltan.append("no invoca el contrato compartido `gate:sistema-conforme`")
    if not re.search(r"[Ee]structural", bloque):
        faltan.append("no nombra la certificación Estructural")
    if not re.search(r"(?:antes|anterior)\s+(?:de|a)[^.\n]{0,60}mutaci[óo]n\s+can[óo]nica",
                     bloque, re.I | re.S):
        faltan.append("no declara que va ANTES de toda mutación canónica (regla 2)")
    if not re.search(r"BLOQUEA|se BLOQUEA|bloquea", bloque):
        faltan.append("no declara el bloqueo si la FASE 0 falla (regla 5)")
    if not re.search(r"NO heredada|no heredada|DE ESTA EJECUCIÓN|de ESTA ejecución", bloque):
        faltan.append("no declara que la certificación es de ESTA ejecución y no heredada "
                      "(reglas 1, 3 y 9)")
    return faltan

for _mc in _MACROS:
    _bmc = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == _mc)
    for _f in _fase0_conforme(_bmc):
        _g33.append(f"§{_mc}: {_f}")

# y §18 mapea la FASE 0 de cada macrocircuito, que es la otra sede que la proyecta
_n18 = len(re.findall(r"`FASE 0`", bloques["§18"]))
if _n18 != len(_MACROS):
    _g33.append(f"§18 mapea {_n18} filas de `FASE 0` y los macrocircuitos derivados son "
                f"{len(_MACROS)}")

# 2 · el CENSO de macrocircuitos, contrastado contra la prosa que lo publica.
#     La cifra no se escribe aquí: se deriva de §8 y se compara con lo que dicen §9.6 y el
#     registro de decisiones.
for _txt_c, _quien_c in ((_b96, "§9.6"), (leer(DEC), "el registro (`D107`)")):
    for _m_c in re.finditer(_NUM + r"\s+macrocircuitos\b", _txt_c):
        _v = _num(_m_c.group(1))
        if _v is not None and _v != len(_MACROS):
            _g33.append(f"{_quien_c} dice «{_m_c.group(1)} macrocircuitos» y §8 deriva "
                        f"{len(_MACROS)}")

# 3 · los SEIS identificadores del sujeto, DERIVADOS de §9.6
_m_suj = re.search(r"El SUJETO — los\s+" + _NUM + r"\s+identificadores", _b96)
_n_suj_pub = _num(_m_suj.group(1)) if _m_suj else None
_IDENT = [" ".join(m.group(2).split()) for m in
          re.finditer(r"^(\d) ([A-ZÁÉÍÓÚ][A-ZÁÉÍÓÚ /]*?)\s{2,}\S", _b96, re.M)]
if _n_suj_pub is None:
    _g33.append("§9.6 no publica «El SUJETO — los <n> identificadores»")
elif len(_IDENT) != _n_suj_pub:
    _g33.append(f"§9.6 dice {_n_suj_pub} identificadores de sujeto y su bloque enumera "
                f"{len(_IDENT)}: {_IDENT}")

# ── PRUEBA NEGATIVA 1 (protección 13) · un macrocircuito SIN Estructural ──
#
# Se toma el texto real del primer macrocircuito, se le quitan las líneas de FASE 0, y se
# exige que `_fase0_conforme` lo DENUNCIE. Un evaluador que no sepa decir que no está es un
# evaluador que no comprueba nada.
# `T-09`. `_NEGATIVAS` era una lista que se llenaba y **no se contrastaba con nada**: su
# largo se imprimía —«4 pruebas negativas ejecutadas»— mientras el título de la comprobación
# publicaba «las TRES pruebas negativas», y el desajuste 3/4 salía en la propia salida del
# baseline, en la batería cuya tesis es que los censos no se escriben a mano. Y tres de las
# cuatro no llevaban CONTROL: se comprobaba que el mutante cae, y no que el caso sano pasa,
# con lo que un evaluador que dijera «no» a todo habría pasado por bueno.
#
# Ahora cada prueba negativa se REGISTRA con sus dos mitades —el CONTROL, que tiene que
# pasar, y el MUTANTE, que tiene que caer—, las dos se verifican, y **el censo no se
# escribe**: sale de las registradas. Un fixture que no pueda fallar deja de contar.
#
# `W2` del documento 24, comprobado por mí y CONFIRMADO: de las cinco pruebas negativas que
# esta comprobación publicaba, **CUATRO no tocan el árbol**. La primera sí —toma el texto
# real del macrocircuito de §8 y le quita la FASE 0—, pero las otras cuatro evalúan
# funciones puras sobre diccionarios sintéticos, y sus dos aserciones se cumplen **para toda
# cadena y todo conjunto de identificadores no vacíos**: se verificó por barrido exhaustivo
# sobre cadenas de 1 a 8 niveles en cualquier orden. Es decir: **ningún árbol las pone en
# rojo**. Contarlas junto a la primera, bajo el rótulo «pruebas negativas ejecutadas», decía
# de ellas algo que no es cierto.
#
# NO SE RETIRAN, porque no son inútiles: cazan una amputación del EVALUADOR —si alguien
# vacía `_nivel_alcanzado` o `_reutilizacion`, se ponen rojas—. Lo que se retira es la
# CLASIFICACIÓN FALSA. Se registran aparte, como FIXTURES DEL EVALUADOR, y el informe
# publica los dos censos separados diciendo cuál toca el árbol y cuál no. El README dice lo
# mismo. Ninguna comprobación nueva: la misma, contando lo que de verdad tiene.
_NEGATIVAS = []
_FIXTURES_EVAL = []

def _registrar(registro, nombre, proteccion, control_pasa, mutante_denunciado, clase):
    """Registra un par CONTROL/MUTANTE en `registro` y devuelve sus fallos."""
    registro.append((nombre, proteccion))
    fallos = []
    if not control_pasa:
        fallos.append(f"{clase} «{nombre}» (protección {proteccion}): su CONTROL —el caso "
                      f"SANO— no pasa, luego sería un rojo permanente que nadie puede "
                      f"cerrar y no prueba nada")
    if not mutante_denunciado:
        fallos.append(f"{clase} «{nombre}» (protección {proteccion}): el caso MUTADO NO se "
                      f"denuncia, luego el evaluador no comprueba nada")
    return fallos


def _negativa(nombre, proteccion, control_pasa, mutante_denunciado):
    """Prueba negativa ANCLADA EN EL ÁRBOL: su mutante sale del texto del corpus."""
    return _registrar(_NEGATIVAS, nombre, proteccion, control_pasa, mutante_denunciado,
                      "PRUEBA NEGATIVA")


def _fixture_evaluador(nombre, proteccion, control_pasa, mutante_denunciado):
    """Fixture del EVALUADOR: sintético, NO toca el árbol, y ningún árbol lo pone rojo."""
    return _registrar(_FIXTURES_EVAL, nombre, proteccion, control_pasa, mutante_denunciado,
                      "FIXTURE DEL EVALUADOR")

# `DD-11` · **LA MITAD MUTANTE ERA TAUTOLÓGICA, y era la ÚNICA prueba negativa anclada.**
# El mutante borraba **LAS DOS** cadenas gatillo —`FASE 0` y `gate:sistema-conforme`—, con
# lo que `_fase0_conforme()` tenía garantizado devolver al menos dos faltas **sea cual sea
# el corpus**. El adjudicador lo verificó estructuralmente y con **200 000 textos
# aleatorios: CERO contraejemplos**. El README promete «*su mutante sale del texto del
# corpus y **un corpus distinto la mueve**»*, y ningún corpus podía moverla: era un fixture
# sintético disfrazado de prueba anclada, contado en la única casilla que el instrumento no
# puede fabricar.
#
# **Hoy se muta UNA SOLA de las dos cadenas** —la del contrato compartido— **y se exige que
# la denuncia sea EXACTAMENTE la que corresponde a esa cadena y ninguna otra.** Con eso la
# aserción vuelve a depender del texto: un §8.1 que escribiera `gate:sistema-conforme` en
# la MISMA línea que su `FASE 0` haría caer también la primera falta, la denuncia dejaría
# de ser exacta y **esta prueba se pondría en rojo sin que nadie la ataque**. Eso es lo que
# significa estar anclada en el árbol.
_b_real = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == (_MACROS[0] if _MACROS else "8.1"))
_FALTA_CONTRATO = "no invoca el contrato compartido `gate:sistema-conforme`"
_b_mutilado = "\n".join(l for l in _b_real.split("\n")
                        if "gate:sistema-conforme" not in l)
_g33 += _negativa("macrocircuito que OMITE el contrato compartido de la FASE 0", 13,
                  not _fase0_conforme(_b_real),
                  _fase0_conforme(_b_mutilado) == [_FALTA_CONTRATO])

# ── PRUEBA NEGATIVA 2 (protección 14) · reutilizar con OTRA huella ────────
#
# Reglas 8, 9 y 10 de `O17`, implementadas sobre los identificadores DERIVADOS de §9.6:
# la reutilización sólo es admisible si TODAS las entradas y huellas siguen idénticas, y
# **aun así cada ejecución emite su propia declaración**.
def _reutilizacion(sujeto_previo, sujeto_actual, identificadores):
    """(admisible, motivo). `identificadores` son los campos derivados de §9.6."""
    difieren = [k for k in identificadores
                if sujeto_previo.get(k) != sujeto_actual.get(k)]
    if difieren:
        return False, ("una sola huella distinta invalida la reutilización: difieren "
                       + ", ".join(difieren))
    return True, "todas las entradas y huellas idénticas"

def _declaracion_valida(reutiliza, emite_declaracion_propia, copia_anterior):
    """Reglas 9 y 10: emitir declaración propia SIEMPRE, y nunca copiar la anterior."""
    if copia_anterior:
        return False, "copiar una certificación anterior está prohibido (regla 10)"
    if not emite_declaracion_propia:
        return False, ("cada ejecución emite SU PROPIA declaración, también cuando toda la "
                       "evidencia se reutiliza (regla 9)")
    return True, "declaración propia de esta ejecución"

_CLAVES = tuple(_IDENT) if _IDENT else ("1", "2", "3", "4", "5", "6")
_sujeto_a = {k: "v%d" % i for i, k in enumerate(_CLAVES)}
_sujeto_b = dict(_sujeto_a)
_sujeto_b[_CLAVES[-1]] = "OTRA-HUELLA"
_g33 += _fixture_evaluador("reutilización con UNA huella de entrada distinta", 14,
                  _reutilizacion(_sujeto_a, _sujeto_a, _CLAVES)[0] is True,
                  not _reutilizacion(_sujeto_a, _sujeto_b, _CLAVES)[0])
_g33 += _fixture_evaluador("reutilización sin declaración propia, y copia de la anterior", 14,
                  _declaracion_valida(True, True, False)[0] is True,
                  not _declaracion_valida(True, False, False)[0]
                  and not _declaracion_valida(True, True, True)[0])

# ── PRUEBA NEGATIVA 3 (protección 15) · elevarse sin Estructural vigente ──
#
# «NIVEL ALCANZADO» de §9.2: el mayor nivel cuya celda está `verificado` Y VIGENTE **y**
# cuyos niveles presupuestos están todos `verificado` y vigentes. La cadena se DERIVA de
# §9.2 (arriba, `_CADENA`) y no se escribe.
def _nivel_alcanzado(celdas, cadena):
    alcanzado = None
    for nivel in cadena:
        if celdas.get(nivel) != "verificado-vigente":
            break
        alcanzado = nivel
    return alcanzado

if _CADENA:
    _todo_ok = {n: "verificado-vigente" for n in _CADENA}
    _sin_estructural = dict(_todo_ok)
    _sin_estructural[_CADENA[0]] = "vencido"
    _solo_superiores = {n: "verificado-vigente" for n in _CADENA[1:]}
    _g33 += _fixture_evaluador("Operativa e Integrada sin Estructural vigente de esta ejecución", 15,
                      _nivel_alcanzado(_todo_ok, _CADENA) == _CADENA[-1],
                      _nivel_alcanzado(_sin_estructural, _CADENA) is None)
    _g33 += _fixture_evaluador("un nivel superior verificado que pretende revalidar el inferior", 15,
                      _nivel_alcanzado(_todo_ok, _CADENA) == _CADENA[-1],
                      _nivel_alcanzado(_solo_superiores, _CADENA) is None)
else:
    _g33.append("sin cadena derivada de §9.2 no se puede evaluar la alcanzabilidad de "
                "ningún nivel")
# el CENSO de las pruebas negativas, contrastado: ni se escribe en el título ni se imprime
# sin comprobar. Cada una tiene protección declarada y las protecciones cubiertas se
# contrastan contra las que el bloque de reglas de `O17` sostiene.
_TODOS_PARES = _NEGATIVAS + _FIXTURES_EVAL
_prot_cubiertas = sorted({p for _, p in _TODOS_PARES})
_prot_arbol = sorted({p for _, p in _NEGATIVAS})
if not _NEGATIVAS:
    _g33.append("CERO pruebas negativas ANCLADAS EN EL ÁRBOL registradas: el censo que esta "
                "comprobación publica saldría de una lista de fixtures sintéticos, y ningún "
                "árbol podría ponerla en rojo")
if len({n for n, _ in _TODOS_PARES}) != len(_TODOS_PARES):
    _g33.append(f"dos pares control/mutante comparten nombre: "
                f"{[n for n, _ in _TODOS_PARES]}")
check("G-33",
      "los macrocircuitos DERIVADOS producen su Estructural en FASE 0; sus pruebas negativas ANCLADAS EN EL ÁRBOL y sus fixtures del evaluador se cuentan POR SEPARADO, cada par con su CONTROL y su MUTANTE",
      not _g33,
      "; ".join(_g33) or
      f"{len(_MACROS)} macrocircuitos derivados de §8 ({', '.join('§' + m for m in _MACROS)}), "
      f"cada uno con FASE 0 `gate:sistema-conforme` anterior a toda mutación · §18 mapea "
      f"{_n18} · sujeto de {len(_IDENT)} identificadores derivados de §9.6 · "
      f"{len(_NEGATIVAS)} prueba(s) negativa(s) ANCLADAS EN EL ÁRBOL —su mutante sale del "
      f"texto del corpus y un corpus distinto las mueve— protección(es) {_prot_arbol}: "
      + " · ".join(n for n, _ in _NEGATIVAS) +
      f" · y {len(_FIXTURES_EVAL)} FIXTURES DEL EVALUADOR —sintéticos, protección(es) "
      f"{sorted({p for _, p in _FIXTURES_EVAL})}—, que cazan una amputación del evaluador y "
      f"NO tocan el árbol: NINGÚN árbol los pone en rojo, y por eso se cuentan aparte "
      f"(`W2`): " + " · ".join(n for n, _ in _FIXTURES_EVAL))

sys.exit(_informe())
