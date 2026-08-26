#!/usr/bin/env python3
"""comprobar_packs — conformidad estructural de los packs instalados.

Comprueba lo que un pack tiene PROHIBIDO hacer (packs/00-QUE-ES-UN-PACK.md) y que
T18 de la sección (a) exige: prefijo de espacio de nombres, ausencia de colisión de
autoridad con roles del kernel, y que los gates de pack SUMEN en vez de sustituir.

Uso:
  python3 kernel/operativo/validadores/comprobar_packs.py [--json]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402
from comprobar_contratos import Resultado, cargar  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CODIGOS_KERNEL = {"PRD", "DIS", "ARQ", "DOM", "CON", "VER", "ENT", "USO", "APR",
                  "INV", "SEG", "PLT", "DSP", "SIS", "ENC"}
PREFIJO = re.compile(r"^([a-z0-9-]+):")


def es_de_pack(ident: str) -> bool:
    return bool(PREFIJO.match(ident or ""))


def t132_packs_no_reclaman_autoridad(b):
    r = Resultado("T132", "Un rol de pack no reclama autoridad de un rol del kernel")
    roles = {d["id"]: (d, ruta) for d, ruta, _ in b.get("rol", [])}
    gates = {d["id"]: (d, ruta) for d, ruta, _ in b.get("gate", [])}

    # 1. Todo artefacto declarado bajo packs/ usa prefijo de espacio de nombres.
    for tipo in ("rol", "capacidad", "gate"):
        for datos, ruta, _ in b.get(tipo, []):
            rel = os.path.relpath(ruta, RAIZ)
            if not rel.startswith("packs/"):
                continue
            ident = datos.get("id", "")
            if tipo == "gate":
                # los gates de pack llevan su pack en el slug: gate:<pack>-<algo>
                slug = ident.split(":", 1)[1] if ":" in ident else ""
                pack = rel.split("/")[1]
                corto = {"web-app": "web", "mobile-app": "mob", "wear-os": "wear"}.get(pack, pack)
                if not (slug.startswith(f"{pack}-") or slug.startswith(f"{corto}-")):
                    r.fallo(f"{rel}: el gate '{ident}' no identifica su pack en el slug")
            elif not es_de_pack(ident):
                r.fallo(f"{rel}: '{ident}' no usa prefijo de espacio de nombres")

    # 2. Ningún rol de pack decide lo que decide un rol del kernel de su misma capacidad.
    for rid, (datos, ruta) in roles.items():
        if not es_de_pack(rid):
            continue
        cap = datos.get("capacidad")
        mias = {d.strip().lower() for d in (datos.get("autoridad", {}).get("decide") or [])}
        for otro_id, (otro, _) in roles.items():
            if es_de_pack(otro_id) or otro.get("capacidad") != cap:
                continue
            suyas = {d.strip().lower() for d in (otro.get("autoridad", {}).get("decide") or [])}
            comunes = mias & suyas
            if comunes:
                r.fallo(f"{rid}: reclama decidir lo mismo que el rol de kernel {otro_id} → "
                        f"{sorted(comunes)[0][:60]}")

    # 3. Ningún rol de pack veta una materia ya vetada por una capacidad del kernel
    #    sin que su propia capacidad la tenga declarada.
    caps = {d["id"]: d for d, _, _ in b.get("capacidad", [])}
    for rid, (datos, ruta) in roles.items():
        if not es_de_pack(rid):
            continue
        if datos.get("autoridad", {}).get("veta"):
            cap = caps.get(datos.get("capacidad"))
            if cap and not (cap.get("autoridad", {}).get("veta") or []):
                r.fallo(f"{rid}: reclama veto y su capacidad {cap['id']} no veta nada")

    # 4. Ningún gate de pack repite el identificador de uno del kernel.
    for gid, (datos, ruta) in gates.items():
        rel = os.path.relpath(ruta, RAIZ)
        if rel.startswith("packs/"):
            continue
        for otro_id, (_, otra_ruta) in gates.items():
            if otro_id == gid and os.path.relpath(otra_ruta, RAIZ).startswith("packs/"):
                r.fallo(f"{gid}: un gate de pack usa el identificador de uno del kernel")

    # 5. Todo pack declara qué NO toca.
    for datos, ruta, _ in b.get("pack", []):
        if not datos.get("no_toca"):
            r.fallo(f"{datos.get('id')}: no declara qué contratos universales tiene prohibido tocar")
    return r


def t131_precedencia_declarada(b):
    r = Resultado("T131", "Todo pack declara su compatibilidad y su regla de precedencia")
    ids = {d.get("id") for d, _, _ in b.get("pack", [])}
    for datos, ruta, _ in b.get("pack", []):
        for otro in datos.get("compatible_con") or []:
            if otro not in ids:
                r.fallo(f"{datos['id']}: se declara compatible con '{otro}', que no existe")
        if not datos.get("precedencia"):
            r.fallo(f"{datos['id']}: no declara su regla de precedencia")
    return r


PRUEBAS = [t131_precedencia_declarada, t132_packs_no_reclaman_autoridad]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    b = cargar()
    resultados = [f(b) for f in PRUEBAS]
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
