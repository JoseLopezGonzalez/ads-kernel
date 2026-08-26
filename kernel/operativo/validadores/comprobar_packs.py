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

import yaml

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402
import comprobar_contratos  # noqa: E402
from comprobar_contratos import Resultado, cargar  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def fijar_raiz(nueva):
    """Ejecuta contra una COPIA del corpus. Ver comprobar_contratos.fijar_raiz."""
    global RAIZ
    RAIZ = os.path.abspath(nueva)
    comprobar_contratos.fijar_raiz(nueva)


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

    # 4. Los gates de pack SUMAN: ni repiten el identificador de uno del kernel ni
    #    rebajan una de sus comprobaciones.
    #    (La versión anterior de esta comprobación era INALCANZABLE: recorría un dict
    #     indexado por id preguntando si un id era igual a sí mismo y a la vez estaba en
    #     otro sitio, lo que no puede ocurrir. Hallazgo A-17.)
    ids_kernel, ids_pack = {}, {}
    for datos, ruta, _ in b.get("gate", []):
        rel = os.path.relpath(ruta, RAIZ)
        (ids_pack if rel.startswith("packs/") else ids_kernel)[datos["id"]] = (datos, rel)
    for gid, (datos, rel) in ids_pack.items():
        if gid in ids_kernel:
            r.fallo(f"{gid} ({rel}): un gate de pack usa el identificador de uno del kernel")
        # un gate de pack no puede repetir el id de una comprobación del kernel: si lo
        # hiciera, la del pack sustituiría a la del kernel en vez de sumarse
        mias = {c.get("id") for c in datos.get("comprobaciones") or []}
        for kid, (kdatos, krel) in ids_kernel.items():
            suyas = {c.get("id") for c in kdatos.get("comprobaciones") or []}
            for choque in sorted(mias & suyas):
                r.fallo(f"{gid}: su comprobación '{choque}' repite la de {kid} ({krel}): "
                        f"un gate de pack SUMA, no sustituye")

    # 5. Todo pack declara qué NO toca.
    for datos, ruta, _ in b.get("pack", []):
        if not datos.get("no_toca"):
            r.fallo(f"{datos.get('id')}: no declara qué contratos universales tiene prohibido tocar")
    return r


def t131_precedencia_declarada(b):
    """Compatibilidad declarada y SIMÉTRICA, más regla de precedencia escrita.

    No se comprueba que el otro pack EXISTA en el corpus: en un proyecto instalado sólo
    están los packs que ese proyecto instaló, y declarar compatibilidad con uno no
    instalado es correcto. Lo que sí se comprueba es que, cuando los dos están presentes,
    se reconozcan MUTUAMENTE: una compatibilidad unilateral es una afirmación que el otro
    lado no sostiene.
    """
    r = Resultado("T131", "La compatibilidad entre packs es simétrica y la precedencia está escrita")
    presentes = {d["id"]: d for d, _, _ in b.get("pack", [])}
    for pid, datos in sorted(presentes.items()):
        for otro in datos.get("compatible_con") or []:
            if otro == pid:
                r.fallo(f"{pid}: se declara compatible consigo mismo")
            elif otro in presentes:
                suyos = presentes[otro].get("compatible_con") or []
                if pid not in suyos:
                    r.fallo(f"{pid}: se declara compatible con '{otro}', y '{otro}' no lo "
                            f"reconoce: la compatibilidad tiene que ser simétrica")
        if not datos.get("precedencia"):
            r.fallo(f"{pid}: no declara su regla de precedencia")
        for prop in datos.get("propiedades_medibles") or []:
            tiene_valor = prop.get("valor") is not None
            if tiene_valor and prop.get("fija_el_profile"):
                r.fallo(f"{pid}/{prop['id']}: declara valor Y delega en el PROFILE. "
                        f"Son excluyentes: o lo conoce el pack, o lo fija el proyecto")
            if not tiene_valor and not prop.get("fija_el_profile"):
                r.fallo(f"{pid}/{prop['id']}: no declara valor y tampoco delega en el "
                        f"PROFILE: la propiedad queda sin umbral posible")
    return r


def t149_lo_mas_restrictivo_gana(_b):
    """A-03 · P1 demostrada como COMPORTAMIENTO, no como campo no vacío.

    La versión anterior de T131 se declaraba superada comprobando que dos campos de YAML
    no estuvieran vacíos, mientras su enunciado afirmaba que el sistema resuelve conflictos
    tomando el valor más restrictivo. Esto ejecuta la resolución sobre fixtures.
    """
    import composicion_packs as cp
    r = Resultado("T149", "Lo más restrictivo gana entre dos packs, y queda registrado por qué")
    ruta = os.path.join(RAIZ, "kernel/operativo/pruebas/fixtures/packs-composicion.yaml")
    if not os.path.exists(ruta):
        r.fallo(f"no existe el fixture {ruta}")
        return r
    with open(ruta, encoding="utf-8") as fh:
        casos = yaml.safe_load(fh)

    for nombre, caso in sorted(casos.items()):
        packs, espera = caso["packs"], caso["espera"]
        if espera.get("conflicto"):
            for orden in (packs, list(reversed(packs))):
                try:
                    cp.resolver(orden)
                except cp.ConflictoDeComposicion:
                    continue
                r.fallo(f"{nombre}: una composición NO comparable se resolvió en silencio "
                        f"en vez de fallar explícitamente")
            continue

        resultados = []
        for orden in (packs, list(reversed(packs))):
            try:
                resultados.append(cp.resolver(orden))
            except cp.ConflictoDeComposicion as exc:
                r.fallo(f"{nombre}: conflicto inesperado — {exc}")
                break
        if len(resultados) != 2:
            continue
        # invertir el orden de entrada no altera el resultado
        if resultados[0] != resultados[1]:
            r.fallo(f"{nombre}: el resultado depende del ORDEN de los packs de entrada")
        obtenido = resultados[0].get(espera["propiedad"])
        if obtenido is None:
            r.fallo(f"{nombre}: la propiedad '{espera['propiedad']}' no aparece en la resolución")
            continue
        if "estado" in espera and obtenido.get("estado") != espera["estado"]:
            r.fallo(f"{nombre}: estado {obtenido.get('estado')}, se esperaba {espera['estado']}")
        if "valor" in espera and obtenido.get("valor") != espera["valor"]:
            r.fallo(f"{nombre}: gana {obtenido.get('valor')}, y lo más restrictivo era "
                    f"{espera['valor']}")
        if "gana" in espera and obtenido.get("gana") != espera["gana"]:
            r.fallo(f"{nombre}: la restricción vencedora se atribuye a "
                    f"{obtenido.get('gana')}, y procede de {espera['gana']}")
        if "perdedores" in espera and obtenido.get("perdedores") != espera["perdedores"]:
            r.fallo(f"{nombre}: los valores descartados no se registran: "
                    f"{obtenido.get('perdedores')}")
        if obtenido.get("estado") != "pendiente-de-profile" and not obtenido.get("motivo"):
            r.fallo(f"{nombre}: la resolución no registra POR QUÉ gana el valor elegido")
    return r


PRUEBAS = [t131_precedencia_declarada, t132_packs_no_reclaman_autoridad,
           t149_lo_mas_restrictivo_gana]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None, help="ejecutar contra otra copia del corpus")
    args = ap.parse_args()
    if args.raiz:
        fijar_raiz(args.raiz)
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
