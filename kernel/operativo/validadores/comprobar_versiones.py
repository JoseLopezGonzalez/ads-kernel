#!/usr/bin/env python3
"""comprobar_versiones — los puntos de entrada no se contradicen sobre la versión.

Hallazgo A-12: tres números para el mismo artefacto —2.0.0-alpha.1 en kernel/VERSION,
1.3.0 en la cabecera de KERNEL.md, 1.0.0 en el árbol del README— y un bloque «Contenido»
que describía el repositorio de la versión anterior. `ads_lint` no lo veía porque su ámbito
por defecto era `kernel/operativo` y `packs`: la portada del repositorio quedaba fuera.

La política está en `kernel/VERSIONES.md` y distingue CUATRO versiones de cosas distintas.
Esto comprueba que nadie las mezcla.

Uso:
  python3 kernel/operativo/validadores/comprobar_versiones.py [--json] [--raiz DIR]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from comprobar_contratos import Resultado  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")


def t152_versiones(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T152", "Los puntos de entrada no se contradicen sobre la versión")

    politica = os.path.join(base, "kernel/VERSIONES.md")
    if not os.path.exists(politica):
        r.fallo("no existe kernel/VERSIONES.md: sin política declarada, cualquier número "
                "es defendible")
        return r
    with open(politica, encoding="utf-8") as fh:
        texto_politica = fh.read()

    ruta_version = os.path.join(base, "kernel/VERSION")
    if not os.path.exists(ruta_version):
        r.fallo("no existe kernel/VERSION")
        return r
    with open(ruta_version, encoding="utf-8") as fh:
        release = fh.read().strip()
    if not SEMVER.match(release):
        r.fallo(f"kernel/VERSION = '{release}' no es una versión reconocible")

    # la política tiene que nombrar la versión del release vigente
    if release not in texto_politica:
        r.fallo(f"kernel/VERSIONES.md no nombra la versión vigente del release ({release}): "
                f"la política y el artefacto van por separado")

    # la línea histórica que declara KERNEL.md tiene que ser la que la política declara
    ruta_kernel = os.path.join(base, "kernel/KERNEL.md")
    linea_historica = None
    if os.path.exists(ruta_kernel):
        with open(ruta_kernel, encoding="utf-8") as fh:
            cabecera = fh.read(2000)
        m = re.search(r"\*\*Versión del kernel:\*\*\s*(\S+)", cabecera)
        if not m:
            r.fallo("kernel/KERNEL.md no declara su versión en la cabecera")
        else:
            linea_historica = m.group(1)
            if linea_historica == release:
                r.fallo(f"KERNEL.md declara {linea_historica}, igual que el release. Son "
                        f"contadores distintos: subir uno no sube el otro")
            if linea_historica not in texto_politica:
                r.fallo(f"la política no reconoce la línea histórica {linea_historica} que "
                        f"declara KERNEL.md")

    # el CHANGELOG más reciente coincide con el release
    ruta_ch = os.path.join(base, "kernel/KERNEL_CHANGELOG.md")
    if os.path.exists(ruta_ch):
        with open(ruta_ch, encoding="utf-8") as fh:
            m = re.search(r"^##\s+(\S+)", fh.read(), re.M)
        if not m:
            r.fallo("kernel/KERNEL_CHANGELOG.md no tiene ninguna entrada de versión")
        elif m.group(1) != release:
            r.fallo(f"la entrada más reciente del CHANGELOG es {m.group(1)} y el release es "
                    f"{release}: o falta la entrada, o falta el cambio de versión")

    # ningún punto de entrada declara una versión de un artefacto que la política no tenga
    conocidas = {release} | ({linea_historica} if linea_historica else set())
    for rel in ("README.md", "START_HERE.md"):
        ruta = os.path.join(base, rel)
        if not os.path.exists(ruta):
            continue
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        for m in re.finditer(r"(?:KERNEL\.md|kernel/KERNEL\.md|kernel)[^\n]{0,60}?"
                             r"\b(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)\b", texto):
            if m.group(1) not in conocidas:
                r.fallo(f"{rel}: declara la versión {m.group(1)} para el kernel, y la "
                        f"política sólo reconoce {sorted(conocidas)}")
    return r


PRUEBAS = [t152_versiones]


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
