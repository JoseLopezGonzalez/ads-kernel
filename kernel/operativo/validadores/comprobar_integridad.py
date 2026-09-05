#!/usr/bin/env python3
"""comprobar_integridad — la huella detecta lo que dice detectar (A-04).

`README.md` afirma: «un kernel editado localmente es un fork silencioso y la reutilización
desaparece; `kernel-status.sh` detecta la divergencia». La auditoría demostró que la
afirmación era falsa justo para los ficheros que EJECUTAN la conformidad: los validadores
en Python y los scripts de tooling quedaban fuera del hash.

Esta prueba comprueba CUATRO cosas distintas, y las cuatro se EJECUTAN y se PUBLICAN una
a una en la salida, con su rótulo y su veredicto:

  1. la huella del kernel almacenada coincide con la calculada  → el kernel está limpio
  2. la huella del kernel CUBRE lo que el corpus le adjudica    → derivado de
     `validadores.yaml` y de `FUENTES-CANONICAS.yml`, no de una lista escrita aquí
  3. huella y sello son sensibles al CONTENIDO y a la RUTA      → se EJERCE sobre una copia
     del árbol: se altera un byte, y se mueve un fichero a otra ruta con el mismo
     contenido, y las dos veces el número tiene que moverse
  4. el SELLO DEL PRODUCTO coincide con el anotado, y su ÁMBITO es el declarado → la
     documentación normativa, clase a clase, derivada del registro canónico

La (2), la (3) y la (4) son las que impiden que alguien «arregle» un fallo de integridad
estrechando la definición de la huella hasta que deje de ver nada.

HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-05 —hallazgo `#23` del delta, `H4` de
`REV-3`—. La comprobación 3 estaba DECLARADA con este mismo rótulo y no estaba escrita:

    # 3 · sensible al contenido y a la ruta
    if huella.calcular(base) != calculada:
        r.fallo("la huella no es determinista: dos cálculos seguidos difieren")

Dos cálculos seguidos del MISMO árbol. Eso es DETERMINISMO —y el propio mensaje de fallo
lo confesaba—, no sensibilidad: no movía un fichero de sitio ni cambiaba un byte. Y la (2)
era `IMPRESCINDIBLES`, una lista de nueve rutas escritas a mano, las nueve dentro de
`kernel/` y `tooling/`: por construcción no podía notar que `docs/` entero estaba fuera del
ámbito, que es el hallazgo `#21`. Las dos defensas declaradas contra el estrechamiento
eran, una, una lista que sólo miraba donde ya se cumplía, y la otra, una comprobación que
no existía.

QUÉ NO PUEDE VOLVER A PASAR, dicho en los cuatro modos: ninguna comprobación DECLARADA sin
código —el rótulo de arriba y las cuatro funciones `_comprobacion_N` son la misma lista—,
ninguna IMPLEMENTADA sin ejecución —`PLAN` las recorre todas—, ninguna EJECUTADA sin
evidencia —la salida publica una línea por comprobación, también cuando pasa— y ninguna
ABSORBIDA en silencio por otra —cada una tiene su rótulo, y sus fallos se atribuyen al
suyo—.

Uso:
  python3 kernel/operativo/validadores/comprobar_integridad.py [--json] [--raiz DIR]
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
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import huella  # noqa: E402
from comprobar_contratos import Resultado  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

RUTA_HUELLA = "kernel/.upstream-hash"
MANIFIESTO_DE_VALIDADORES = "kernel/operativo/validadores/validadores.yaml"


# ===========================================================================
#  DE DÓNDE SALE «LO QUE NO PUEDE DEJAR DE ESTAR CUBIERTO»
# ===========================================================================
#  DECISIÓN · se DERIVA de dos censos canónicos, y no se escribe aquí
#      Alternativas: (a) mantener `IMPRESCINDIBLES` y añadirle rutas de `docs/`; (b)
#      derivar el conjunto de los censos que el propio corpus ya mantiene.
#      Se elige (b). Con (a) la lista seguiría siendo una lista: cada validador nuevo, cada
#      esquema nuevo y cada sede nueva nacerían fuera de ella, y nadie se enteraría —es la
#      forma exacta de `H-03` y de `ADJ-B2`, y es lo que hizo que la lista de nueve rutas no
#      pudiera ver que `docs/` entero estaba fuera—. Con (b) quien decide qué es
#      imprescindible es el corpus:
#
#          `validadores.yaml`        el censo de lo que EJECUTA la conformidad
#          `FUENTES-CANONICAS.yml`   las sedes de cada materia y sus fuentes técnicas
#
#      Un validador nuevo entra en el censo el día que se registra, y desde ese día esta
#      comprobación lo exige. Ninguna de las dos sedes es editable «de paso»: la primera la
#      juzga `comprobar_evidencia`, la segunda `validar-fuentes-canonicas.py`.
def _registro_canonico(base):
    """El registro canónico ya interpretado, o `None` si no está. Falla CERRADO si está
    y no se puede leer: un sello que no sabe su alcance no se publica."""
    ruta = os.path.join(base, huella.REGISTRO_DE_ZONAS)
    if not os.path.isfile(ruta):
        return None
    import yaml                                                   # noqa: PLC0415
    with open(ruta, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _rutas_adjudicadas(base):
    """Las rutas que los censos canónicos declaran, con quién las declara."""
    adjudicadas = {}
    datos = _registro_canonico(base)
    for materia in ((datos or {}).get("materias") or []):
        identificador = materia.get("id", "?")
        sede = (materia.get("sede") or "").strip()
        if sede:
            adjudicadas.setdefault(sede, f"es la SEDE de `{identificador}`")
        for fuente in (materia.get("fuentes_tecnicas") or []):
            adjudicadas.setdefault(fuente.strip(),
                                   f"es FUENTE TÉCNICA de `{identificador}`")
    ruta_manifiesto = os.path.join(base, MANIFIESTO_DE_VALIDADORES)
    if os.path.isfile(ruta_manifiesto):
        import yaml                                               # noqa: PLC0415
        with open(ruta_manifiesto, encoding="utf-8") as fh:
            manifiesto = yaml.safe_load(fh) or {}
        for comp in (manifiesto.get("componentes") or []):
            guion = (comp.get("script") or "").strip()
            if not guion:
                continue
            # El manifiesto ya dice DÓNDE vive cada componente: `dir` cuando no es el
            # directorio de los validadores. Suponer el directorio dejaría las baterías del
            # runtime y las de `tooling/` apuntando a rutas que no existen.
            carpeta = (comp.get("dir") or "kernel/operativo/validadores").strip("/")
            rel = f"{carpeta}/{guion}"
            adjudicadas[rel] = (f"EJECUTA la conformidad: `validadores.yaml` lo "
                                f"registra como `{comp.get('id', guion)}`")
    return adjudicadas


# ---------------------------------------------------------------------------
#  1 · la huella del kernel almacenada coincide con la calculada
# ---------------------------------------------------------------------------
def _comprobacion_1(base):
    fallos = []
    ruta_hash = os.path.join(base, RUTA_HUELLA)
    calculada = huella.calcular(base)
    if not os.path.exists(ruta_hash):
        fallos.append(f"no existe {RUTA_HUELLA}: no hay referencia contra la que comparar")
        return fallos
    with open(ruta_hash, encoding="utf-8") as fh:
        almacenada = fh.read().strip()
    if almacenada != calculada:
        fallos.append(f"el kernel DIVERGE de su release: almacenada {almacenada}, "
                      f"calculada {calculada}. Algún fichero de la huella se editó "
                      f"localmente")
    return fallos


# ---------------------------------------------------------------------------
#  2 · la huella del kernel cubre lo que los censos canónicos le adjudican
# ---------------------------------------------------------------------------
def _comprobacion_2(base):
    fallos = []
    cubiertos = {os.path.relpath(p, base).replace(os.sep, "/")
                 for p in huella.ficheros(base)}
    adjudicadas = _rutas_adjudicadas(base)
    if not adjudicadas:
        fallos.append("ningún censo canónico adjudica una sola ruta a la huella: sin "
                      "`validadores.yaml` ni `FUENTES-CANONICAS.yml` esta comprobación no "
                      "tiene sujeto, y una comprobación sin sujeto no pasa por omisión")
        return fallos
    # LA EXTENSIÓN NO FILTRA AQUÍ, Y ES DELIBERADO. MEDIDO: con el filtro
    # `rel.endswith(huella.EXTENSIONES)` puesto, el sabotaje `NS23c` —quitar `.py` de
    # `EXTENSIONES`, que es el estrechamiento clásico— sacaba a los veintitantos validadores
    # de la huella Y a la vez los sacaba de esta comprobación, porque el filtro se derivaba
    # de la misma tupla que el ataque acababa de estrechar. Una comprobación que usa como
    # criba lo mismo que vigila no vigila nada. Lo que el corpus adjudica a la huella entra
    # en la huella, y con qué extensión esté escrito no es asunto del adjudicatario.
    del_kernel = 0
    for rel, motivo in sorted(adjudicadas.items()):
        if rel.split("/")[0] not in huella.AMBITOS:
            continue
        del_kernel += 1
        if not os.path.exists(os.path.join(base, rel)):
            fallos.append(f"{rel}: {motivo} y NO EXISTE en el árbol")
        elif rel not in cubiertos:
            fallos.append(f"{rel} NO entra en la huella del kernel, y {motivo}: un fork "
                          f"silencioso de ese fichero sería indetectable")
    if not del_kernel:
        fallos.append("ninguna de las rutas adjudicadas cae dentro del ámbito de la huella "
                      "del kernel: o los censos están vacíos o el ámbito se ha estrechado "
                      "hasta dejar de contener lo que ejecuta la conformidad")
    for ext in huella.EXTENSIONES:
        if not any(c.endswith(ext) for c in cubiertos):
            fallos.append(f"la huella del kernel no cubre ningún fichero {ext}, y su "
                          f"contrato la declara entre sus extensiones")
    return fallos


# ---------------------------------------------------------------------------
#  3 · sensibilidad al CONTENIDO y a la RUTA, EJERCIDA sobre una copia del árbol
# ---------------------------------------------------------------------------
#  DECISIÓN · se ejerce sobre una COPIA, y no sobre el árbol que se juzga
#      Alternativas: (a) mutar el árbol y restaurarlo; (b) copiarlo a un temporal FUERA del
#      árbol y mutar la copia.
#      Se elige (b). Con (a) una interrupción a mitad —o un fallo de la restauración— deja
#      el árbol que se está certificando con una mutación dentro, escrita por el propio
#      instrumento que certifica. El temporal va fuera del árbol a propósito: dentro, la
#      copia entraría en el sello del original y la comprobación se mediría a sí misma.
def _sensibilidad(base, fallos, rotulo, rel, medir):
    """Un byte y una ruta, sobre `rel`. `medir(raiz)` devuelve el número que debe moverse."""
    antes = medir(base)
    ruta = os.path.join(base, rel)
    with open(ruta, "rb") as fh:
        original = fh.read()
    with open(ruta, "wb") as fh:
        fh.write(original + b"\n")
    if medir(base) == antes:
        fallos.append(f"{rotulo}: se ALTERA el contenido de `{rel}` y el número no se "
                      f"mueve ({antes}). No es sensible al CONTENIDO")
    with open(ruta, "wb") as fh:
        fh.write(original)
    if medir(base) != antes:
        fallos.append(f"{rotulo}: restaurado el contenido de `{rel}`, el número NO vuelve "
                      f"a {antes}. Sin retorno al valor sano, un rojo no distingue la "
                      f"mutación de la deriva del propio instrumento")
        return
    carpeta, nombre = os.path.split(ruta)
    troncal, extension = os.path.splitext(nombre)
    destino = os.path.join(carpeta, f"{troncal}-MOVIDO{extension}")
    os.rename(ruta, destino)
    if medir(base) == antes:
        fallos.append(f"{rotulo}: el MISMO contenido se mueve a `{troncal}-MOVIDO"
                      f"{extension}`, en la misma zona y con la misma extensión, y el "
                      f"número no se mueve ({antes}). No es sensible a la RUTA")
    os.rename(destino, ruta)


def _comprobacion_3(base):
    import shutil                                                 # noqa: PLC0415
    import tempfile                                               # noqa: PLC0415
    fallos = []
    del_kernel = [os.path.relpath(p, base).replace(os.sep, "/")
                  for p in huella.ficheros(base)]
    sellados = huella.ficheros_del_sello(base)
    normativos = [r for r in sellados if r.startswith("docs/")]
    if not del_kernel:
        fallos.append("la huella del kernel no cubre NI UN fichero: no hay sobre qué "
                      "ejercer la sensibilidad, y eso ya es el estrechamiento")
    if not normativos:
        fallos.append("el sello del producto no cubre NI UN fichero de `docs/`: no hay "
                      "sobre qué ejercer la sensibilidad de la documentación normativa, y "
                      "eso ya es el estrechamiento que `#21` midió")
    if fallos:
        return fallos
    copia = tempfile.mkdtemp(prefix="ads-sensibilidad-")
    destino = os.path.join(copia, "arbol")
    try:
        shutil.copytree(base, destino, symlinks=True,
                        ignore=shutil.ignore_patterns("__pycache__", ".git",
                                                      ".pytest_cache"))
        _sensibilidad(destino, fallos, "HUELLA DEL KERNEL", del_kernel[0],
                      lambda raiz: huella.calcular(raiz))
        _sensibilidad(destino, fallos, "SELLO DEL PRODUCTO", normativos[0],
                      lambda raiz: huella.sellar(raiz))
        # CONTROL DEL CONTROL de la separación: que los dos números existan no demuestra
        # que sean dos cosas distintas. Una norma de `docs/` tiene que mover el SELLO y NO
        # la HUELLA DEL KERNEL: es el hallazgo `#21` mecanizado y su remedio a la vez.
        huella_antes, sello_antes = huella.calcular(destino), huella.sellar(destino)
        ruta = os.path.join(destino, normativos[0])
        with open(ruta, "rb") as fh:
            original = fh.read()
        with open(ruta, "wb") as fh:
            fh.write(original + b"\n")
        if huella.sellar(destino) == sello_antes:
            fallos.append(f"SEPARACIÓN: alterada la norma `{normativos[0]}`, el SELLO DEL "
                          f"PRODUCTO no se mueve. Es el hallazgo `#21` vivo")
        if huella.calcular(destino) != huella_antes:
            fallos.append(f"SEPARACIÓN: alterada la norma `{normativos[0]}`, se mueve la "
                          f"HUELLA DEL KERNEL. Su contrato es `kernel/`, `packs/` y "
                          f"`tooling/`, y ensancharlo rompe todo kernel vendorizado")
        with open(ruta, "wb") as fh:
            fh.write(original)
    finally:
        shutil.rmtree(copia, ignore_errors=True)
    return fallos


# ---------------------------------------------------------------------------
#  4 · el SELLO DEL PRODUCTO, su ÁMBITO y la cobertura de la norma
# ---------------------------------------------------------------------------
def _comprobacion_4(base):
    fallos = []
    datos = _registro_canonico(base)
    if datos is None:
        fallos.append(f"no existe `{huella.REGISTRO_DE_ZONAS}`: el sello del producto "
                      f"deriva de él qué material normativo cubre, y sin registro no hay "
                      f"sello que publicar")
        return fallos

    # 4a · la política es TOTAL sobre las clases que el registro declara
    declaradas = list(datos.get("clases_validas") or [])
    if not declaradas:
        fallos.append(f"`{huella.REGISTRO_DE_ZONAS}` no declara `clases_validas`")
    for clase in declaradas:
        if clase not in huella.POLITICA_DEL_SELLO:
            fallos.append(f"la clase canónica `{clase}` no tiene política de sello "
                          f"escrita: una clase sin política quedaría fuera POR OMISIÓN, "
                          f"que es la exclusión que no se escribe")
        elif not huella.POLITICA_DEL_SELLO[clase][1].strip():
            fallos.append(f"la clase canónica `{clase}` tiene política de sello SIN "
                          f"MOTIVO escrito: una exclusión sin motivo no es una exclusión")
    for clase in sorted(huella.POLITICA_DEL_SELLO):
        if clase != huella.SIN_CLASE and clase not in declaradas:
            fallos.append(f"la política del sello nombra `{clase}`, que el registro "
                          f"canónico NO declara entre sus `clases_validas`: la política "
                          f"no puede inventar clases que nadie asigna")
    for rotulo, motivo, _ in huella.EXCLUSIONES_DEL_SELLO:
        if not motivo.strip():
            fallos.append(f"la exclusión del sello «{rotulo}» no tiene motivo escrito")

    # 4b · el libro anotado frente al derivado, clase a clase
    libro = huella.libro_del_sello(base)
    anotado = huella.leer_libro_anotado(base)
    if anotado is None:
        fallos.append(f"no existe `{huella.LIBRO_ANOTADO}`: el SELLO DEL PRODUCTO no está "
                      f"anotado, y un sello sin referencia no sella nada. Se anota con "
                      f"`huella.py --anotar-sello`")
    else:
        if anotado.get("ambito") != libro["ambito"]:
            fallos.append(
                f"el ÁMBITO del sello CAMBIÓ: anotado {anotado.get('ambito')}, derivado "
                f"{libro['ambito']}. El alcance del sello —la política de cada clase, las "
                f"exclusiones y las zonas del registro— no es el que se anotó. Un dígito "
                f"de dieciséis cifras sin su alcance al lado es una cifra que se cree")
        for clase in sorted(set(anotado["clases"]) | set(libro["clases"])):
            viejo = anotado["clases"].get(clase)
            nuevo = libro["clases"].get(clase)
            if viejo and not nuevo:
                fallos.append(
                    f"la clase `{clase}` tenía {viejo[1]} ficheros sellados y ahora NO "
                    f"TIENE NI UNO: una clase entera salió del sello")
            elif nuevo and not viejo:
                fallos.append(f"la clase `{clase}` aparece con {nuevo[1]} ficheros "
                              f"sellados y NO figura en el libro anotado")
            elif viejo != nuevo:
                fallos.append(
                    f"la clase `{clase}` DIVERGE del libro anotado: {viejo[0]} sobre "
                    f"{viejo[1]} ficheros, ahora {nuevo[0]} sobre {nuevo[1]}")
        if anotado.get("sello") != libro["sello"] and not fallos:
            fallos.append(f"el SELLO DEL PRODUCTO diverge: anotado {anotado.get('sello')}, "
                          f"calculado {libro['sello']}")

    # 4c · toda clase que el registro ASIGNA de verdad tiene material sellado
    zonas = huella.zonas_canonicas(base) or []
    asignadas = {clase for _, clase, _ in zonas}
    for clase in sorted(asignadas):
        if huella.POLITICA_DEL_SELLO.get(clase, (huella.SELLADA, ""))[0] != huella.SELLADA:
            continue
        if not libro["clases"].get(clase):
            fallos.append(f"el registro asigna la clase `{clase}` a alguna zona del árbol "
                          f"y el sello no cubre NI UN fichero suyo: esa zona quedó fuera")

    # 4d · toda sede y toda fuente técnica que el registro adjudica está SELLADA
    sellados = set(huella.ficheros_del_sello(base))
    for rel, motivo in sorted(_rutas_adjudicadas(base).items()):
        if not os.path.exists(os.path.join(base, rel)):
            fallos.append(f"{rel}: {motivo} y NO EXISTE en el árbol. Borrar una sede "
                          f"normativa retira la materia que gobernaba")
        elif rel not in sellados:
            fallos.append(f"{rel} NO entra en el SELLO DEL PRODUCTO, y {motivo}: se puede "
                          f"reescribir sin que el sello de la candidata se mueva")
    return fallos


PLAN = [
    ("1 · la huella del kernel almacenada coincide con la calculada", _comprobacion_1),
    ("2 · la huella del kernel cubre lo que los censos canónicos le adjudican",
     _comprobacion_2),
    ("3 · huella y sello son sensibles al CONTENIDO y a la RUTA, ejercido", _comprobacion_3),
    ("4 · el SELLO DEL PRODUCTO, su ÁMBITO y la cobertura de la norma", _comprobacion_4),
]


def t150_integridad(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T150",
                  "La huella de integridad cubre a los validadores y detecta su edición")
    # NINGUNA COMPROBACIÓN SE ABSORBE EN OTRA: cada una publica su veredicto, también
    # cuando pasa, y sus fallos se atribuyen a su rótulo.
    r.comprobaciones = []
    for rotulo, funcion in PLAN:
        try:
            fallos = funcion(base)
        except Exception as exc:                                  # noqa: BLE001
            fallos = [f"la comprobación no llegó a emitir veredicto: "
                      f"{type(exc).__name__}: {exc}"]
        r.comprobaciones.append({"comprobacion": rotulo,
                                 "veredicto": "VERDE" if not fallos else "ROJO",
                                 "fallos": fallos})
        for fallo in fallos:
            r.fallo(f"[{rotulo.split(' · ')[0]}] {fallo}")
    return r


PRUEBAS = [t150_integridad]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None)
    args = ap.parse_args()
    resultados = [f(args.raiz) for f in PRUEBAS]
    if args.json:
        print(json.dumps([{"id": x.id, "nombre": x.nombre,
                           "estado": "prueba-superada" if x.superada else "prueba-fallida",
                           "comprobaciones": getattr(x, "comprobaciones", []),
                           "fallos": x.fallos} for x in resultados],
                         ensure_ascii=False, indent=2))
    else:
        for x in resultados:
            print(f"{x.id}  {'SUPERADA' if x.superada else 'FALLIDA '}  {x.nombre}")
            # EJECUTADA SIN EVIDENCIA es uno de los cuatro modos que `#23` prohíbe: una
            # comprobación que pasa y no se publica es indistinguible de una que no corrió.
            for c in getattr(x, "comprobaciones", []):
                print(f"     {c['veredicto']:5}  comprobación {c['comprobacion']}")
                for f in c["fallos"]:
                    print(f"          · {f}")
        fallidas = [x for x in resultados if not x.superada]
        print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if any(not x.superada for x in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
