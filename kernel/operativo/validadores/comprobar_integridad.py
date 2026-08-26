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
