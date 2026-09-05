#!/usr/bin/env python3
"""comprobar_referencias — el grafo del corpus por RUTA, no por nombre de fichero.

Hallazgo A-05. La comprobación anterior (T134) decidía que un documento tenía enlace
entrante así:

    entrante = any(os.path.basename(ruta) in texto for texto in otros_ficheros)

Es una búsqueda de subcadena del NOMBRE BASE. Como el corpus da a propósito el mismo
nombre a los ficheros homólogos de cada capacidad —`composicion.md` dieciocho veces,
`CAPACIDAD.md` quince—, una sola mención satisfacía a todos a la vez: 119 de 188
documentos quedaban exentos sin que nadie lo hubiera declarado.

Aquí el grafo se construye con rutas normalizadas y con las cuatro formas reales en que un
documento del corpus se alcanza:

    1  enlace Markdown a un fichero          resuelto por ruta, no por nombre
    2  enlace Markdown a un directorio       alcanza a sus hijos directos
    3  campo `prompt:` o `validador:`        de un bloque canónico, que es una ruta
    4  cita de un IDENTIFICADOR canónico     declarado en ese fichero — los ids son únicos

Y comprueba, además de los huérfanos:

    ·  enlaces rotos, con la ruta exacta que no existe
    ·  enlaces al NOMBRE correcto en la CARPETA equivocada, nombrando los candidatos
    ·  ficheros distintos con el mismo nombre base, para que la ambigüedad sea visible
    ·  que toda exclusión esté declarada, justificada y siga siendo necesaria

Uso:
  python3 kernel/operativo/validadores/comprobar_referencias.py [--json] [--raiz DIR]
                                                               [--exclusiones]
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
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402
from comprobar_contratos import Resultado  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ENLACE_MD = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
DIRS_IGNORADOS = {".git", "__pycache__", ".pytest_cache", "node_modules"}
# Campos de un bloque canónico cuyo valor es una RUTA, no un identificador.
CAMPOS_RUTA = ("prompt", "validador")


def cargar_exclusiones(base):
    ruta = os.path.join(base, "kernel/operativo/validadores/exclusiones.yaml")
    if not os.path.exists(ruta):
        return {}
    with open(ruta, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _bajo(rel, prefijo):
    return rel == prefijo or rel.startswith(prefijo.rstrip("/") + "/")


def documentos(base, no_analizados):
    salida = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if d not in DIRS_IGNORADOS)
        for nombre in sorted(filenames):
            if not nombre.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, nombre), base).replace(os.sep, "/")
            if any(_bajo(rel, x) for x in no_analizados):
                continue
            salida.append(rel)
    return salida


def t147_referencias(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T147", "Todo documento es alcanzable por ruta, y ninguna referencia es ambigua")
    exc = cargar_exclusiones(base)

    no_analizados, entradas = [], []
    for clave, destino in (("no_analizados", no_analizados), ("puntos_de_entrada", entradas)):
        for item in exc.get(clave) or []:
            if not isinstance(item, dict) or not item.get("ruta") or not item.get("motivo"):
                r.fallo(f"exclusiones.yaml/{clave}: una entrada sin `ruta` o sin `motivo`. "
                        f"Una exclusión sin justificación escrita no es revisable")
                continue
            if not os.path.exists(os.path.join(base, item["ruta"])):
                r.fallo(f"exclusiones.yaml/{clave}: '{item['ruta']}' ya no existe. "
                        f"Las exclusiones caducadas se borran, no se acumulan")
                continue
            destino.append(item["ruta"])

    # LA FRONTERA DEL PROYECTO INSTALADO se valida aquí, y con la misma disciplina: motivo
    # escrito y objetivo que EXISTE. Que exista es lo que impide usar esta lista para
    # silenciar un enlace roto de este repositorio: si la ruta no está, la entrada es un
    # fallo, no una excepción.
    no_embarcados = 0
    for item in exc.get("enlaces_no_embarcados") or []:
        if not isinstance(item, dict) or not item.get("ruta") or not item.get("motivo"):
            r.fallo("exclusiones.yaml/enlaces_no_embarcados: una entrada sin `ruta` o sin "
                    "`motivo`. Una frontera sin justificación escrita no es revisable")
            continue
        if not os.path.exists(os.path.join(base, item["ruta"])):
            r.fallo(f"exclusiones.yaml/enlaces_no_embarcados: '{item['ruta']}' no existe en "
                    f"este repositorio. La frontera declara qué se queda AGUAS ARRIBA, no "
                    f"qué falta: una entrada cuya ruta no existe aquí serviría para "
                    f"silenciar un enlace roto de verdad")
            continue
        no_embarcados += 1
    r.detalle = f"{no_embarcados} rutas declaradas como no embarcadas"

    docs = documentos(base, no_analizados)
    conjunto = set(docs)
    todos_los_ficheros = set()
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in DIRS_IGNORADOS]
        for n in filenames:
            todos_los_ficheros.add(
                os.path.relpath(os.path.join(dirpath, n), base).replace(os.sep, "/"))

    # ficheros distintos con el mismo nombre base: no es un fallo, es una ambigüedad que
    # tiene que ser VISIBLE, porque es la que derrotaba a la comprobación anterior
    por_nombre = {}
    for rel in docs:
        por_nombre.setdefault(os.path.basename(rel), []).append(rel)
    homonimos = {n: v for n, v in por_nombre.items() if len(v) > 1}

    entrantes = {rel: set() for rel in docs}

    def marcar(destino_rel, origen_rel):
        if destino_rel in entrantes:
            entrantes[destino_rel].add(origen_rel)

    # --- 1 y 2 · enlaces Markdown -------------------------------------------
    for rel in docs:
        carpeta = os.path.dirname(rel)
        with open(os.path.join(base, rel), encoding="utf-8") as fh:
            texto = fh.read()
        dentro_de_bloque = False
        for linea_n, linea in enumerate(texto.splitlines(), 1):
            if linea.lstrip().startswith("```"):
                dentro_de_bloque = not dentro_de_bloque
                continue
            # Un enlace dentro de un bloque cercado es una ILUSTRACIÓN —el ejemplo de un
            # tablero, la salida de un comando—, no una referencia del corpus. Se muestra
            # tal cual y no tiene por qué resolver.
            if dentro_de_bloque:
                continue
            for destino in ENLACE_MD.findall(linea):
                if destino.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                limpio = destino.split("#")[0]
                if not limpio:
                    continue
                objetivo = os.path.normpath(os.path.join(carpeta, limpio)).replace(os.sep, "/")
                absoluto = os.path.join(base, objetivo)
                if os.path.isdir(absoluto):
                    for hijo in sorted(os.listdir(absoluto)):
                        marcar(f"{objetivo}/{hijo}", rel)
                    continue
                if os.path.isfile(absoluto):
                    marcar(objetivo, rel)
                    continue
                # roto: ¿existe el mismo NOMBRE en otra carpeta?
                candidatos = por_nombre.get(os.path.basename(limpio), [])
                if candidatos:
                    r.fallo(f"{rel}:{linea_n}: '{destino}' no existe, y sí existe ese nombre "
                            f"en {', '.join(candidatos)}. Es un enlace al nombre correcto en "
                            f"la carpeta equivocada, no una referencia resoluble")
                else:
                    r.fallo(f"{rel}:{linea_n}: enlace roto → {destino}")

    # --- 3 · campos de bloque canónico que son rutas -------------------------
    lint = Lint(base, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    ids_por_fichero = {}
    for _tipo, datos, ruta, _l in lint.bloques:
        origen = os.path.relpath(ruta, base).replace(os.sep, "/")
        ident = datos.get("id")
        if isinstance(ident, str):
            ids_por_fichero.setdefault(origen, set()).add(ident)
        for campo in CAMPOS_RUTA:
            valor = datos.get(campo)
            if isinstance(valor, str) and valor:
                # `validador` puede declarar la invocación completa; la ruta es lo primero
                objetivo = valor.split("#")[0].split()[0] if valor.split() else ""
                if objetivo in todos_los_ficheros:
                    marcar(objetivo, origen)
                elif objetivo:
                    r.fallo(f"{origen}: el campo `{campo}` apunta a '{objetivo}', "
                            f"que no existe")

    # --- 4 · cita de un identificador canónico ------------------------------
    contenidos = {}
    for rel in docs:
        with open(os.path.join(base, rel), encoding="utf-8") as fh:
            contenidos[rel] = fh.read()
    for rel, ids in ids_por_fichero.items():
        for otro, texto in contenidos.items():
            if otro == rel:
                continue
            if any(i in texto for i in ids):
                marcar(rel, otro)

    # --- huérfanos ----------------------------------------------------------
    for rel in docs:
        if entrantes[rel]:
            continue
        if any(_bajo(rel, e) for e in entradas):
            continue
        r.fallo(f"{rel}: no lo alcanza ningún enlace por ruta, ninguna referencia de campo "
                f"y ninguna cita de sus identificadores. Existe para nadie")

    r.informe = {
        "documentos_analizados": len(docs),
        "no_analizados": no_analizados,
        "puntos_de_entrada": entradas,
        "nombres_repetidos": {n: v for n, v in sorted(homonimos.items())},
    }
    return r


PRUEBAS = [t147_referencias]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None)
    ap.add_argument("--exclusiones", action="store_true",
                    help="mostrar qué queda fuera del análisis y por qué")
    args = ap.parse_args()
    resultados = [f(args.raiz) for f in PRUEBAS]
    if args.json:
        print(json.dumps([{"id": x.id, "nombre": x.nombre,
                           "estado": "prueba-superada" if x.superada else "prueba-fallida",
                           "fallos": x.fallos} for x in resultados], ensure_ascii=False, indent=2))
        return 1 if any(not x.superada for x in resultados) else 0

    base = os.path.abspath(args.raiz or RAIZ)
    exc = cargar_exclusiones(base)
    for x in resultados:
        inf = getattr(x, "informe", {})
        print(f"{x.id}  {'SUPERADA' if x.superada else 'FALLIDA '}  {x.nombre}")
        for f in x.fallos:
            print(f"          · {f}")
        print(f"\ndocumentos analizados: {inf.get('documentos_analizados', 0)}")
        print(f"nombres base repetidos: {len(inf.get('nombres_repetidos', {}))} "
              f"(resueltos por ruta, nunca por nombre)")
        if args.exclusiones:
            print("\nFUERA DEL ANÁLISIS")
            for clave in ("no_analizados", "puntos_de_entrada"):
                for item in exc.get(clave) or []:
                    print(f"  [{clave}] {item['ruta']}")
                    print(f"        {' '.join(item['motivo'].split())}")
            print("\nNOMBRES BASE REPETIDOS")
            for n, v in inf.get("nombres_repetidos", {}).items():
                print(f"  {n}  ×{len(v)}")
    fallidas = [x for x in resultados if not x.superada]
    print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if fallidas else 0


if __name__ == "__main__":
    sys.exit(main())
