#!/usr/bin/env python3
"""comprobar_packs — conformidad estructural de los packs instalados.

Comprueba lo que un pack tiene PROHIBIDO hacer (packs/00-QUE-ES-UN-PACK.md) y que
T18 de la sección (a) exige: prefijo de espacio de nombres, ausencia de colisión de
autoridad con roles del kernel, y que los gates de pack SUMEN en vez de sustituir.

Uso:
  python3 kernel/operativo/validadores/comprobar_packs.py [--json]
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
