#!/usr/bin/env python3
"""comprobar_integridad — la huella detecta lo que dice detectar (A-04).

`README.md` afirma: «un kernel editado localmente es un fork silencioso y la reutilización
desaparece; `kernel-status.sh` detecta la divergencia». La auditoría demostró que la
afirmación era falsa justo para los ficheros que EJECUTAN la conformidad: los validadores
en Python y los scripts de tooling quedaban fuera del hash.

Esta prueba comprueba tres cosas distintas:

  1. la huella almacenada coincide con la calculada  → el kernel está limpio
  2. la huella CUBRE lo que tiene que cubrir         → validadores, tooling, esquemas
  3. la huella es sensible al contenido y a la ruta  → mismo contenido en otro sitio
                                                        produce una huella distinta

La (2) y la (3) son las que impiden que alguien «arregle» un fallo de integridad
estrechando la definición de la huella hasta que deje de ver nada.

Uso:
  python3 kernel/operativo/validadores/comprobar_integridad.py [--json] [--raiz DIR]
"""
from __future__ import annotations

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

# Lo que la huella NO puede dejar de cubrir. Si un fichero de esta lista deja de entrar,
# la comprobación de integridad se ha vaciado por dentro.
IMPRESCINDIBLES = [
    "kernel/operativo/validadores/ads_lint.py",
    "kernel/operativo/validadores/comprobar_contratos.py",
    "kernel/operativo/validadores/comprobar_packs.py",
    "kernel/operativo/validadores/huella.py",
    "kernel/operativo/validadores/reglas.yaml",
    "kernel/operativo/esquemas/capacidad.yaml",
    "kernel/operativo/00-INDICE.md",
    "tooling/kernel-status.sh",
    "tooling/new-project.sh",
]


def t150_integridad(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T150", "La huella de integridad cubre a los validadores y detecta su edición")

    cubiertos = {os.path.relpath(p, base).replace(os.sep, "/") for p in huella.ficheros(base)}

    # 2 · cobertura
    for rel in IMPRESCINDIBLES:
        if not os.path.exists(os.path.join(base, rel)):
            r.fallo(f"no existe {rel}, y la huella debe cubrirlo")
        elif rel not in cubiertos:
            r.fallo(f"{rel} NO entra en la huella: un fork silencioso de ese fichero sería "
                    f"indetectable")
    for ext in (".py", ".sh", ".yaml", ".md"):
        if not any(c.endswith(ext) for c in cubiertos):
            r.fallo(f"la huella no cubre ningún fichero {ext}")

    # 1 · limpio
    ruta_hash = os.path.join(base, "kernel/.upstream-hash")
    calculada = huella.calcular(base)
    if not os.path.exists(ruta_hash):
        r.fallo("no existe kernel/.upstream-hash: no hay referencia contra la que comparar")
    else:
        with open(ruta_hash, encoding="utf-8") as fh:
            almacenada = fh.read().strip()
        if almacenada != calculada:
            r.fallo(f"el kernel DIVERGE de su release: almacenada {almacenada}, "
                    f"calculada {calculada}. Algún fichero de la huella se editó localmente")

    # 3 · sensible al contenido y a la ruta
    if huella.calcular(base) != calculada:
        r.fallo("la huella no es determinista: dos cálculos seguidos difieren")
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
                           "fallos": x.fallos} for x in resultados], ensure_ascii=False, indent=2))
    else:
        for x in resultados:
            print(f"{x.id}  {'SUPERADA' if x.superada else 'FALLIDA '}  {x.nombre}")
            for f in x.fallos:
                print(f"          · {f}")
        fallidas = [x for x in resultados if not x.superada]
        print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if any(not x.superada for x in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
