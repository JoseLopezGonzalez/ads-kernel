#!/usr/bin/env python3
"""huella — la huella de integridad del kernel vendorizado, en un solo sitio.

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
    tooling/*.sh      el arranque y la propia comprobación de integridad
    packs/**          la especialización instalada, sin los packs retirados

Qué NO entra:

    kernel/.upstream-hash   es el resultado, no la entrada
    docs/, README, PROFILE  no son kernel: son del proyecto o de su historia
    __pycache__, .git       artefactos de ejecución

Uso:
  python3 kernel/operativo/validadores/huella.py [--raiz DIR] [--listar]
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

EXTENSIONES = (".md", ".yaml", ".yml", ".py", ".sh")
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", default=None)
    ap.add_argument("--listar", action="store_true", help="qué ficheros entran en la huella")
    args = ap.parse_args()
    base = os.path.abspath(args.raiz or RAIZ)
    if args.listar:
        for ruta in ficheros(base):
            print(os.path.relpath(ruta, base))
        print(f"\n{len(ficheros(base))} ficheros")
        return 0
    print(calcular(base))
    return 0


if __name__ == "__main__":
    sys.exit(main())
