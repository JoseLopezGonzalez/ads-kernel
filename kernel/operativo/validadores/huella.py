#!/usr/bin/env python3
"""huella — los DOS sellos del árbol, definidos aquí y sólo aquí.

Este módulo publica DOS conceptos distintos, y no uno ensanchado:

  (A) HUELLA DEL KERNEL   `calcular()`  · `kernel/`, `packs/` y `tooling/`, con las cinco
                                          extensiones de su contrato vigente. Es la que
                                          `kernel-status.sh` compara con `.upstream-hash`
                                          para decir si un kernel VENDORIZADO diverge de su
                                          release. Su significado NO cambia aquí.
  (B) SELLO DEL PRODUCTO  `sellar()`    · kernel, packs, tooling y la DOCUMENTACIÓN
                                          NORMATIVA que gobierna el producto, DERIVADA de
                                          `docs/canonico/FUENTES-CANONICAS.yml`. Es lo que
                                          un gate ancla cuando dice «esta candidata».

POR QUÉ SON DOS Y NO UNO. Un kernel instalado dentro de un proyecto ajeno NO lleva `docs/`
de ADS: ensanchar (A) hasta cubrir `docs/` haría que todo proyecto vendorizado publicara
una divergencia permanente por material que no tiene. Y estrechar (B) hasta (A) es
exactamente el defecto que se midió. Cada uno responde a su pregunta, y la respuesta de uno
no vale para la otra.

HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-05, sobre una COPIA del árbol —hallazgo
`#21` del delta, `H2` de `REV-3`—:

    $ python3.12 kernel/operativo/validadores/huella.py --raiz <copia>
      2696627742081a01
    $ printf '\\nENTRADA FALSA DE A1\\n' >> <copia>/docs/owner/ADS-OWNER-RESOLUCIONES.md
    $ printf '\\nLINEA FALSA DE A1\\n'   >> <copia>/docs/f6/05-MATRIZ-CIERRE-G01-G08.md
    $ python3.12 kernel/operativo/validadores/huella.py --raiz <copia>
      2696627742081a01

La sede de las resoluciones del Owner y el documento donde la candidata reclama el cierre
de `G-01`…`G-08`, alteradas las dos a la vez, y el número no se movió. En un corpus donde
la prosa ES la norma, la mitad normativa del árbol no estaba sellada por nada.

Hallazgo A-04: `kernel-status.sh` calculaba su hash sobre `*.md` y `*.yaml` de `kernel/`.
Los cuatro validadores en Python y los scripts de `tooling/` quedaban FUERA, de modo que
un proyecto podía relajar `ads_lint.py`, neutralizar `comprobar_contratos.py` o quitar una
comprobación de `comprobar_packs.py` y seguir reportando LIMPIO indefinidamente. Es la vía
más barata para rebajar todos los gates a la vez, y era invisible.

La huella se define **aquí y sólo aquí**. `kernel-status.sh` llama a este módulo en vez de
recalcularla por su cuenta: dos implementaciones del mismo hash derivan, y cuando derivan
la que miente es siempre la que nadie mira.

Qué entra en la huella, y por qué:

    kernel/**.md      los contratos, fichas, métodos, prompts y pruebas
    kernel/**.yaml    los esquemas y las reglas: definen qué es conforme
    kernel/**.py      los VALIDADORES: son quienes ejecutan la conformidad
    kernel/**.sh      cualquier script que el kernel lleve dentro
    kernel/**.toml    la plantilla del manifiesto de composición del producto
    tooling/*.sh      el arranque y la propia comprobación de integridad
    tooling/*.py      workspace.py materializa repositorios: editarlo sin que se note
                      sería la vía silenciosa para clonar donde no se debe
    packs/**          la especialización instalada, sin los packs retirados

Qué NO entra:

    kernel/.upstream-hash   es el resultado, no la entrada
    docs/, README, PROFILE  no son kernel: son del proyecto o de su historia
    __pycache__, .git       artefactos de ejecución

Qué entra en el SELLO DEL PRODUCTO, y por qué: NO se enumera aquí. Se DERIVA de la clase
que `docs/canonico/FUENTES-CANONICAS.yml` asigna a cada ruta por PATRÓN DE ZONA, y la
política de cada clase —sellada o excluida, con su motivo escrito— está en
`POLITICA_DEL_SELLO`. Una lista de rutas escrita a mano dentro del instrumento que sella es
el mismo defecto que `D-04` existe para abolir: envejece en silencio, y lo que nace fuera
de ella nace fuera del sello.

Uso:
  python3 kernel/operativo/validadores/huella.py [--raiz DIR] [--listar]
  python3 kernel/operativo/validadores/huella.py --sello [--raiz DIR]
  python3 kernel/operativo/validadores/huella.py --ambito | --libro | --listar-sello
  python3 kernel/operativo/validadores/huella.py --anotar-sello
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-05, sobre esta zona. Con seis líneas de
#  veneno en un `sitecustomize.py` alcanzable desde `PYTHONPATH`:
#
#      $ cat veneno/sitecustomize.py
#        import hashlib; hashlib.sha256 = lambda *a, **k: _Falso()   # digest 0000…
#      $ PYTHONPATH=veneno python3.12 kernel/operativo/validadores/huella.py
#        0000000000000000                     ← la huella FORJADA sobre un árbol mutado
#      $ PYTHONPATH=veneno python3.12 kernel/operativo/validadores/comprobar_integridad.py
#        T150  SUPERADA · EXIT=0              ← VERDE sobre un árbol MUTADO
#
#  El prólogo `E-10` de abajo purga `sys.path` en su primera sentencia, y eso llega TARDE:
#  `site.py` importa `sitecustomize` mientras el intérprete arranca, antes de que la primera
#  línea de este módulo exista. Lo que cambia no es un módulo —`hashlib` es el bueno— sino
#  un atributo suyo, y el control del control de `E-10`, que mira la procedencia de `os`, no
#  lo ve. Con la guarda, este punto se reejecuta con `-I -S -E` y `sitecustomize` no llega a
#  importarse: medido en la tabla de los doce ataques de `T380`-`T399`.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      La misma disciplina que `E-10` sigue debajo y que `T330` comprueba: lo que protege
#      está fijado y es idéntico en todos los puntos —`T380` lo exige con su digest—, y lo
#      que se lee dice qué se midió en ESTA sede. Un recital común mentiría en la mitad de
#      las sedes; un mecanismo por sede derivaría, y el que derive de menos es el que nadie
#      mira.
#
#  DECISIÓN · la guarda va ANTES del prólogo `E-10`, y no lo sustituye
#      Alternativas: (a) sustituir `E-10` por la guarda; (b) dejar `E-10` y añadir la
#      guarda encima.
#      Se elige (b). Cierran cosas distintas: `E-10` retira del `sys.path` lo que mete el
#      lanzador —y sigue haciendo falta cuando el punto se IMPORTA, donde la guarda no
#      reejecuta—; `G-03` impide que `sitecustomize` llegue siquiera a ejecutarse. Quitar
#      `E-10` reabriría la contaminación de la ruta en el caso importado.
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

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-04, sobre `validadores/huella.py` —el
#  instrumento que produce el número que se publica como línea base— y con seis líneas de
#  veneno: un `hashlib.py` homónimo cuyo `sha256()` devuelve siempre el digest esperado.
#
#      $ echo "# CODIGO INYECTADO" >> mutado/kernel/operativo/validadores/ads_lint.py
#      $ cd mutado && python3.12 …/huella.py                     → 8b38fb4f4b07300c
#      $ python3.12 …/comprobar_integridad.py                    → T150 FALLIDA  EXIT=1
#      $ PYTHONPATH=veneno python3.12 …/huella.py                → bc59513f7182130a
#      $ PYTHONPATH=veneno python3.12 …/comprobar_integridad.py  → T150 SUPERADA EXIT=0
#
#  `T150` es la prueba que dice «la huella detecta su edición», y bajo veneno certificaba en
#  VERDE un árbol editado. La causa: la zona `validadores/` estaba ENTERA fuera del
#  inventario de `T306`, de modo que `E-10` —declarado «CERRADO POR INVENTARIO MECÁNICO»—
#  seguía vivo justo en el aparato que produce la evidencia de la certificación.
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
import hashlib
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

EXTENSIONES = (".md", ".yaml", ".yml", ".py", ".sh", ".toml")
AMBITOS = ("kernel", "packs", "tooling")
EXCLUIDOS_DIR = ("__pycache__", ".git", ".pytest_cache")
EXCLUIDOS_PREFIJO_DIR = ("legacy-",)
EXCLUIDOS_FICHERO = (".upstream-hash",)


def ficheros(raiz=None):
    """Los ficheros de la huella, en orden estable. Lista, no genera sorpresas."""
    base = os.path.abspath(raiz or RAIZ)
    salida = []
    for ambito in AMBITOS:
        origen = os.path.join(base, ambito)
        if not os.path.isdir(origen):
            continue
        for dirpath, dirnames, filenames in os.walk(origen):
            dirnames[:] = sorted(d for d in dirnames
                                 if d not in EXCLUIDOS_DIR
                                 and not d.startswith(EXCLUIDOS_PREFIJO_DIR))
            for nombre in sorted(filenames):
                if nombre in EXCLUIDOS_FICHERO:
                    continue
                if nombre.endswith(EXTENSIONES):
                    salida.append(os.path.join(dirpath, nombre))
    return sorted(salida, key=lambda p: os.path.relpath(p, base))


def calcular(raiz=None):
    """Hash del CONTENIDO y de las RUTAS. Renombrar un fichero cambia la huella."""
    base = os.path.abspath(raiz or RAIZ)
    acumulado = hashlib.sha256()
    for ruta in ficheros(base):
        rel = os.path.relpath(ruta, base).replace(os.sep, "/")
        acumulado.update(rel.encode("utf-8"))
        acumulado.update(b"\0")
        with open(ruta, "rb") as fh:
            acumulado.update(hashlib.sha256(fh.read()).digest())
    return acumulado.hexdigest()[:16]


# ===========================================================================
#  (B) · SELLO DEL PRODUCTO ADS · el material normativo se DERIVA, no se enumera
# ===========================================================================
#  DECISIÓN · la selección la hace la CLASE CANÓNICA, no una tupla de directorios
#      Alternativas: (a) añadir `"docs"` a `AMBITOS`; (b) escribir aquí la lista de sedes
#      normativas; (c) derivar de `docs/canonico/FUENTES-CANONICAS.yml` la clase de cada
#      ruta y dar a cada CLASE una política con su motivo.
#      Se elige (c). Con (a) el sello sería igual de ciego a lo que naciera fuera de esos
#      cuatro nombres, y además rompería (A) para todo kernel vendorizado. Con (b) la lista
#      envejece: es la forma exacta de `H-03` —«mecánico DENTRO de dos zonas escritas a
#      mano»— y de `ADJ-B2`. Con (c) quien decide qué material hay es el ÁRBOL, y quien
#      decide qué régimen le toca es el registro canónico, que ya es la sede de esa
#      clasificación y que ya se valida sola con `docs/canonico/validar-fuentes-canonicas.py`
#      (`V10`: ningún fichero versionado queda sin clasificar).
#
#  DECISIÓN · lo que ninguna zona clasifica se SELLA, y se publica
#      Dejarlo fuera sería la EXCLUSIÓN POR OMISIÓN, que es el defecto que `ADJ-M5` cerró en
#      `comprobar_recuentos`. Un fichero sin clase entra en el sello bajo la etiqueta
#      `SIN_CLASE`, y `comprobar_integridad` lo publica: así una zona nueva no puede nacer
#      invisible ni al sello ni al lector.
#
#  DECISIÓN · el sello NO se limita a las cinco extensiones de (A)
#      La evidencia publicada es `*.txt` y los manifiestos del gate son `*.json`: las dos
#      cosas estaban fuera de (A) por la extensión, no por la zona. El sello mira TODO
#      fichero, y las únicas exclusiones son las tres de abajo, derivadas y motivadas.
#
#  AUTORREFERENCIA, y cómo se cierra
#      Un sello no puede contener su propio resultado: el fichero que lo anota queda fuera,
#      por la misma razón por la que `kernel/.upstream-hash` queda fuera de (A). Y los
#      documentos del gate que JUZGA a una candidata no pueden cambiarle el sello a
#      posteriori, porque el sello de la candidata es el de su SHA CONGELADO: `sellar()`
#      acepta `ref=` y lee entonces el ÁRBOL DE OBJETOS de esa revisión, donde lo que se
#      escriba después no existe. Sobre el árbol de trabajo el sello describe el árbol de
#      trabajo, que es lo que un árbol de trabajo merece.
REGISTRO_DE_ZONAS = "docs/canonico/FUENTES-CANONICAS.yml"
SIN_CLASE = "SIN_CLASE"
SELLADA = "SELLADA"
EXCLUIDA = "EXCLUIDA"

# La política, clase a clase. NINGUNA CLASE SIN ENTRADA: una clase del registro que no
# aparezca aquí es ROJO en `comprobar_integridad`, y no «fuera por omisión».
POLITICA_DEL_SELLO = {
    "AUTORIDAD_SUPERIOR": (
        SELLADA,
        "SEDE DEL OWNER y directivas escritas en su voz. Es la autoridad del producto: "
        "una entrada falsa aquí cambia quién manda, y era lo primero que el sello no veía"),
    "APROBADA_POR_ENMIENDA": (
        SELLADA,
        "DOCUMENTO APROBADO que sólo cambia por enmienda —las especificaciones del "
        "rediseño y `kernel/KERNEL.md`—. Reescribirlo cambia la obligación que se "
        "implementa"),
    "CANONICA_OPERATIVA": (
        SELLADA,
        "NORMATIVA VIGENTE y ESTADO OPERATIVO: el corpus canónico, el contenido operativo "
        "instalable y los packs. Es la prosa que ES la norma"),
    "CONTRATO_O_ESQUEMA_TECNICO": (
        SELLADA,
        "contratos, esquemas, validadores, runtime y tooling: lo que EJECUTA la "
        "conformidad. Ya estaba en (A) y sigue estando aquí"),
    "HISTORICA": (
        SELLADA,
        "GATE HISTÓRICO y versiones superadas o rechazadas. Se conservan por trazabilidad, "
        "y una trazabilidad reescribible no traza nada: reescribir un gate pasado cambia el "
        "acto sobre el que se apoyan los actos siguientes"),
    "EVIDENCIA": (
        SELLADA,
        "EVIDENCIA publicada y MANIFIESTOS: salidas del runner, informes de auditoría y el "
        "aparato de verificación. Es lo que un informe cita como prueba de lo que afirma"),
    "DERIVADA": (
        SELLADA,
        "PROYECCIÓN DERIVADA: índices, checkpoints, registros regenerados y las áreas de "
        "trabajo de F5 y F6. No crean autoridad, y por eso mismo una proyección alterada "
        "es una mentira barata sobre lo que las sedes dicen"),
    "NO_APLICABLE_A_IMPLEMENTACION": (
        SELLADA,
        "BORRADORES no aprobados y material de trabajo. Se sellan precisamente porque NO "
        "son norma: si añadir un borrador no moviera el sello, un borrador podría "
        "aparecer junto a la norma sin que el sello lo notara, y ahí se lee como norma"),
    SIN_CLASE: (
        SELLADA,
        "lo que NINGUNA zona del registro clasifica. Se sella y se publica: dejarlo fuera "
        "sería la exclusión por omisión"),
}

# Las TRES exclusiones del sello. Cada una con su motivo, y las tres DERIVABLES de un
# criterio mecánico —no de una lista de rutas—.
EXCLUSIONES_DEL_SELLO = (
    ("directorio de artefacto de ejecución",
     "`__pycache__`, `.git` y `.pytest_cache` los escribe la EJECUCIÓN, no el autor: "
     "sellarlos haría que ejecutar el árbol cambiara el sello del árbol",
     ("__pycache__", ".git", ".pytest_cache")),
    ("fichero que ALMACENA el resultado",
     "`kernel/.upstream-hash` y `.sello-producto` son la SALIDA de este módulo. Un "
     "resultado dentro de su propia entrada no puede coincidir consigo mismo",
     ("kernel/.upstream-hash", ".sello-producto")),
    ("enlace simbólico",
     "un enlace no tiene contenido propio: lo que sella es su objetivo, que ya entra por "
     "su propia ruta. Sellar el enlace contaría el mismo byte dos veces y ataría el sello "
     "a una ruta del anfitrión",
     ()),
)

LIBRO_ANOTADO = ".sello-producto"


class RegistroIlegible(RuntimeError):
    """El registro canónico de zonas no se puede leer. El sello falla CERRADO."""


def zonas_canonicas(raiz=None, ref=None):
    """Las zonas del registro canónico, en su orden. `None` si el registro no está.

    Devuelve `[(regex, clase, motivo), …]`. Gana la PRIMERA que case, que es la regla que
    el propio registro escribe. No se reescriben aquí ni los patrones ni las clases.

    CNS `ref`, el registro se lee del ÁRBOL DE OBJETOS de esa revisión y NO del disco. Si
    se leyera del disco, reclasificar hoy una zona cambiaría el sello de una candidata
    congelada ayer, que es justo la autorreferencia que este módulo tiene que cerrar.
    """
    base = os.path.abspath(raiz or RAIZ)
    if ref is not None:
        import subprocess                                         # noqa: PLC0415
        blob = subprocess.run(["git", "-C", base, "show", f"{ref}:{REGISTRO_DE_ZONAS}"],
                              capture_output=True)
        if blob.returncode != 0:
            return None
        crudo = blob.stdout.decode("utf-8")
    else:
        ruta = os.path.join(base, REGISTRO_DE_ZONAS)
        if not os.path.isfile(ruta):
            return None
        with open(ruta, encoding="utf-8") as fh:
            crudo = fh.read()
    try:
        import re                                                 # noqa: PLC0415
        import yaml                                               # noqa: PLC0415
    except ImportError as exc:                                    # pragma: no cover
        raise RegistroIlegible(
            f"existe `{REGISTRO_DE_ZONAS}` y no se puede interpretar: {exc}. Sin la "
            f"clasificación por zonas el sello no sabe qué material normativo cubre, y un "
            f"sello que no sabe su alcance no se publica") from exc
    datos = yaml.safe_load(crudo) or {}
    entradas = datos.get("zonas")
    if not entradas:
        raise RegistroIlegible(
            f"`{REGISTRO_DE_ZONAS}` no declara `zonas`: sin clasificación no hay sello")
    zonas = []
    for entrada in entradas:
        if not isinstance(entrada, dict) or not entrada.get("patron") \
                or not entrada.get("clase"):
            raise RegistroIlegible(
                f"`{REGISTRO_DE_ZONAS}` trae una zona sin `patron` o sin `clase`")
        zonas.append((re.compile(entrada["patron"]), entrada["clase"],
                      (entrada.get("motivo") or "").strip()))
    return zonas


def _excluida_del_sello(rel, nombre_dir=None):
    """¿Cae `rel` en alguna de las tres exclusiones? Devuelve el rótulo, o `None`."""
    if nombre_dir is not None:
        return EXCLUSIONES_DEL_SELLO[0][0] if nombre_dir in EXCLUSIONES_DEL_SELLO[0][2] \
            else None
    if rel in EXCLUSIONES_DEL_SELLO[1][2]:
        return EXCLUSIONES_DEL_SELLO[1][0]
    return None


def ficheros_del_sello(raiz=None):
    """Las rutas relativas que entran en el sello, en orden estable.

    TODO fichero del árbol menos las tres exclusiones. La clase no filtra aquí: filtra en
    `POLITICA_DEL_SELLO`, y hoy las nueve políticas dicen `SELLADA`. Que la estructura
    admita `EXCLUIDA` y ninguna clase la use no es adorno: es lo que hace que retirar una
    clase del sello sea un acto ESCRITO, con su motivo, y no un patrón borrado en silencio.
    """
    base = os.path.abspath(raiz or RAIZ)
    zonas = zonas_canonicas(base)
    salida = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if not _excluida_del_sello(None, d))
        for nombre in sorted(filenames):
            ruta = os.path.join(dirpath, nombre)
            if os.path.islink(ruta):
                continue
            rel = os.path.relpath(ruta, base).replace(os.sep, "/")
            if _excluida_del_sello(rel):
                continue
            clase = clase_de(rel, zonas)
            if POLITICA_DEL_SELLO.get(clase, (SELLADA, ""))[0] != SELLADA:
                continue
            salida.append(rel)
    return sorted(salida)


def clase_de(rel, zonas):
    """La clase canónica de una ruta. `SIN_CLASE` si ninguna zona la nombra."""
    if zonas is None:
        return SIN_CLASE
    for patron, clase, _ in zonas:
        if patron.search(rel):
            return clase
    return SIN_CLASE


def _digerir(pares):
    """El mismo esquema que `calcular`: la RUTA entra en el hash, no sólo el contenido."""
    acumulado = hashlib.sha256()
    for rel, contenido in pares:
        acumulado.update(rel.encode("utf-8"))
        acumulado.update(b"\0")
        acumulado.update(hashlib.sha256(contenido).digest())
    return acumulado.hexdigest()[:16]


def _contenidos(base, ref=None):
    """`[(rel, bytes), …]` del árbol de trabajo, o del ÁRBOL DE OBJETOS de `ref`."""
    if ref is None:
        pares = []
        for rel in ficheros_del_sello(base):
            with open(os.path.join(base, rel), "rb") as fh:
                pares.append((rel, fh.read()))
        return pares
    import subprocess                                             # noqa: PLC0415
    listado = subprocess.run(["git", "-C", base, "ls-tree", "-r", "--name-only", "-z", ref],
                             capture_output=True)
    if listado.returncode != 0:
        raise RegistroIlegible(
            f"`git ls-tree` no responde para `{ref}`: el sello de una candidata se toma "
            f"sobre su SHA CONGELADO, y sin el árbol de objetos no se toma")
    zonas = zonas_canonicas(base, ref)
    pares = []
    for rel in sorted(x for x in listado.stdout.decode("utf-8").split("\0") if x):
        if _excluida_del_sello(rel):
            continue
        if any(parte in EXCLUSIONES_DEL_SELLO[0][2] for parte in rel.split("/")):
            continue
        if POLITICA_DEL_SELLO.get(clase_de(rel, zonas), (SELLADA, ""))[0] != SELLADA:
            continue
        blob = subprocess.run(["git", "-C", base, "show", f"{ref}:{rel}"],
                              capture_output=True)
        if blob.returncode != 0:
            continue
        pares.append((rel, blob.stdout))
    return pares


def sellar(raiz=None, ref=None):
    """El SELLO DEL PRODUCTO: contenido y ruta de todo el material, menos lo excluido."""
    base = os.path.abspath(raiz or RAIZ)
    return _digerir(_contenidos(base, ref))


def descripcion_del_ambito(raiz=None, ref=None):
    """El ALCANCE del sello, en texto canónico. Un dígito sin su alcance es una cifra
    que se cree: éste es el alcance, y su digest viaja pegado al sello."""
    base = os.path.abspath(raiz or RAIZ)
    lineas = [f"HUELLA_DEL_KERNEL ambitos={','.join(AMBITOS)}",
              f"HUELLA_DEL_KERNEL extensiones={','.join(EXTENSIONES)}",
              f"HUELLA_DEL_KERNEL excluidos_dir={','.join(EXCLUIDOS_DIR)}",
              f"HUELLA_DEL_KERNEL excluidos_prefijo={','.join(EXCLUIDOS_PREFIJO_DIR)}",
              f"HUELLA_DEL_KERNEL excluidos_fichero={','.join(EXCLUIDOS_FICHERO)}"]
    for clase in sorted(POLITICA_DEL_SELLO):
        destino, motivo = POLITICA_DEL_SELLO[clase]
        lineas.append(f"SELLO_POLITICA {clase}={destino} motivo={motivo}")
    for rotulo, motivo, objetivos in EXCLUSIONES_DEL_SELLO:
        lineas.append(f"SELLO_EXCLUSION {rotulo}={','.join(objetivos)} motivo={motivo}")
    zonas = zonas_canonicas(base, ref)
    if zonas is None:
        lineas.append("SELLO_REGISTRO ausente")
    else:
        for patron, clase, _ in zonas:
            lineas.append(f"SELLO_ZONA {patron.pattern}={clase}")
    return lineas


def ambito_del_sello(raiz=None, ref=None):
    """Digest del ALCANCE. Se mueve si se mueve la política, una exclusión o una zona."""
    texto = "\n".join(descripcion_del_ambito(raiz, ref)).encode("utf-8")
    return hashlib.sha256(texto).hexdigest()[:16]


def libro_del_sello(raiz=None, ref=None):
    """El sello, su ámbito y un digest POR CLASE con su cardinal.

    POR QUÉ POR CLASE, y no un número solo. Un sello que sólo publica dieciséis cifras dice
    «algo se movió» y nada más: el mismo diagnóstico para haber tocado la sede del Owner que
    para haber regenerado un índice. El libro reparte el mismo hash por la clase canónica de
    cada ruta, de modo que el rojo NOMBRA el régimen que se movió y el lector sabe si tiene
    delante una proyección regenerada o una autoridad reescrita. El cardinal va al lado
    porque añadir o borrar un fichero mueve el digest igual que editarlo, y sin el cardinal
    los dos gestos serían indistinguibles.
    """
    base = os.path.abspath(raiz or RAIZ)
    zonas = zonas_canonicas(base, ref)
    pares = _contenidos(base, ref)
    por_clase = {}
    for rel, contenido in pares:
        por_clase.setdefault(clase_de(rel, zonas), []).append((rel, contenido))
    return {
        "sello": _digerir(pares),
        "ambito": ambito_del_sello(base, ref),
        "clases": {clase: (_digerir(sorted(items)), len(items))
                   for clase, items in sorted(por_clase.items())},
    }


def formatear_libro(libro):
    """El libro en el formato que `.sello-producto` almacena. Una línea, un hecho."""
    lineas = ["# SELLO DEL PRODUCTO ADS. Lo escribe `huella.py --anotar-sello`; no se",
              "# edita a mano. `sello` es el digest del material sellado; `ambito` el de",
              "# su ALCANCE; cada `clase` reparte el mismo digest por clase canónica.",
              f"sello   {libro['sello']}",
              f"ambito  {libro['ambito']}"]
    for clase, (digest, cardinal) in sorted(libro["clases"].items()):
        lineas.append(f"clase   {clase:30} {digest}  {cardinal}")
    return "\n".join(lineas) + "\n"


def leer_libro_anotado(raiz=None):
    """El libro tal y como está anotado en `.sello-producto`. `None` si no hay ninguno."""
    base = os.path.abspath(raiz or RAIZ)
    ruta = os.path.join(base, LIBRO_ANOTADO)
    if not os.path.isfile(ruta):
        return None
    libro = {"sello": None, "ambito": None, "clases": {}}
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            partes = linea.split()
            if not partes or partes[0].startswith("#"):
                continue
            if partes[0] == "sello" and len(partes) >= 2:
                libro["sello"] = partes[1]
            elif partes[0] == "ambito" and len(partes) >= 2:
                libro["ambito"] = partes[1]
            elif partes[0] == "clase" and len(partes) >= 4:
                libro["clases"][partes[1]] = (partes[2], int(partes[3]))
    return libro


def anotar_libro(raiz=None):
    """Escribe `.sello-producto` con el libro del árbol de hoy. Devuelve el libro."""
    base = os.path.abspath(raiz or RAIZ)
    libro = libro_del_sello(base)
    with open(os.path.join(base, LIBRO_ANOTADO), "w", encoding="utf-8") as fh:
        fh.write(formatear_libro(libro))
    return libro


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", default=None)
    ap.add_argument("--listar", action="store_true", help="qué ficheros entran en la huella")
    ap.add_argument("--sello", action="store_true", help="el SELLO DEL PRODUCTO ADS")
    ap.add_argument("--ref", default=None,
                    help="sellar el ÁRBOL DE OBJETOS de esta revisión, no el de trabajo")
    ap.add_argument("--listar-sello", action="store_true", help="qué entra en el sello")
    ap.add_argument("--ambito", action="store_true", help="el ALCANCE del sello, escrito")
    ap.add_argument("--libro", action="store_true", help="sello, ámbito y digest por clase")
    ap.add_argument("--anotar-sello", action="store_true", help="escribe `.sello-producto`")
    args = ap.parse_args()
    base = os.path.abspath(args.raiz or RAIZ)
    if args.listar:
        for ruta in ficheros(base):
            print(os.path.relpath(ruta, base))
        print(f"\n{len(ficheros(base))} ficheros")
        return 0
    if args.listar_sello:
        rutas = [rel for rel, _ in _contenidos(base, args.ref)]
        for rel in rutas:
            print(rel)
        print(f"\n{len(rutas)} ficheros")
        return 0
    if args.ambito:
        for linea in descripcion_del_ambito(base, args.ref):
            print(linea)
        print(f"\nambito {ambito_del_sello(base, args.ref)}")
        return 0
    if args.libro:
        print(formatear_libro(libro_del_sello(base, args.ref)), end="")
        return 0
    if args.anotar_sello:
        print(formatear_libro(anotar_libro(base)), end="")
        return 0
    if args.sello:
        print(sellar(base, args.ref))
        return 0
    print(calcular(base))
    return 0


if __name__ == "__main__":
    sys.exit(main())
