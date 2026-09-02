#!/usr/bin/env python3
"""validar-fuentes-canonicas — comprueba el registro de sedes canonicas.

QUE COMPRUEBA, y nada mas:

  V1  el fichero es YAML valido y tiene las claves de primer nivel obligatorias
  V2  el SHA de la base de consolidacion tiene forma de commit completo
  V3  todo identificador de materia es unico
  V4  toda materia declara UNA sola sede, y esa ruta existe
  V5  ninguna pareja (sede, seccion) esta declarada dos veces: dos nombres para una misma
      sede serian dos materias donde hay una
  V6  el estado de cada materia esta en `estados_validos`
  V7  toda `autoridad_superior`, todo `acto_declarativo` y toda `fuentes_tecnicas` existen
  V8  ninguna materia VIGENTE tiene por sede un documento de GATE, un DICTAMEN, un
      MANIFIESTO o un CORRIGENDUM  —es la prohibicion PRH-2, ejecutada y no declarada—
  V9  ninguna materia vigente se apoya en si misma: `autoridad_superior` no puede ser la
      propia sede
  V10 los patrones de zona compilan, sus clases estan en `clases_validas`, y NINGUN fichero
      versionado del repositorio queda sin zona que lo clasifique
  V11 cada fichero del PRIMER NIVEL de docs/canonico/ esta enlazado por su ruta completa
      desde el indice de la iniciativa. NO recorre subdirectorios: un fichero en
      docs/canonico/<sub>/ NO lo ve esta comprobacion, y quien lo cubre es G-29 de la
      bateria, que evalua la zona entera contra la revision base

QUE NO COMPRUEBA, y se dice: no juzga si una materia esta bien asignada, no lee el
contenido de las sedes y no certifica nada.

Uso:
  python3 docs/canonico/validar-fuentes-canonicas.py [--raiz DIR] [--json] [--autoprueba]

Codigos de salida:  0 sin fallos  ·  1 hay fallos  ·  2 no se pudo empezar
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:                                          # pragma: no cover
    print("validar-fuentes-canonicas requiere PyYAML", file=sys.stderr)
    sys.exit(2)

# La raiz se deriva de la ubicacion de este fichero y de nada mas. No se usa el cwd: la
# bateria del corpus aprendio por un defecto real que caer al directorio del autor hace que
# el validador compruebe un arbol que no es el que le han dado.
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
REGISTRO = "docs/canonico/FUENTES-CANONICAS.yml"
INDICE = "docs/evolucion/00-INDICE.md"
DIR_CANONICO = "docs/canonico"

CLAVES = ("version", "base_de_consolidacion", "regla_de_precedencia", "prohibiciones",
          "estados_validos", "clases_validas", "zonas", "materias")

# Un documento de gate, un dictamen, un manifiesto o un corrigendum, reconocidos por su
# NOMBRE y no por una lista escrita: una lista se queda corta en cuanto nace el siguiente.
ES_APARATO_DE_GATE = re.compile(
    r"(?:^|/)(?:[0-9]{2}-.*GATE.*\.md|.*MANIFIESTO.*\.md|.*ASIGNACION-GATE.*\.md"
    r"|.*DICTAMEN.*\.md|CORRIGENDUM.*\.md)$", re.IGNORECASE)


def ficheros_versionados(raiz):
    """Las rutas que Git publica. Sin Git no hay censo, y se dice en vez de suponerlo."""
    try:
        salida = subprocess.run(["git", "-C", raiz, "ls-files", "-z"],
                                capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as e:
        return None, f"no se puede consultar Git ({e})"
    if salida.returncode != 0:
        return None, "`git ls-files` no responde: sin censo no hay clasificacion que comprobar"
    return [r for r in salida.stdout.split("\0") if r], None


def validar(datos, raiz, censo):
    """Devuelve la lista de fallos. Lista vacia = el registro es coherente."""
    fallos = []

    def existe(rel):
        return os.path.exists(os.path.join(raiz, rel))

    # V1
    for clave in CLAVES:
        if clave not in datos:
            fallos.append(f"V1 · falta la clave de primer nivel `{clave}`")
    if fallos:
        return fallos

    # V2
    sha = str((datos.get("base_de_consolidacion") or {}).get("commit", ""))
    if not re.fullmatch(r"[0-9a-f]{40}", sha):
        fallos.append(f"V2 · `base_de_consolidacion.commit` no es un SHA completo: {sha!r}")

    estados = set(datos["estados_validos"])
    clases = set(datos["clases_validas"])
    materias = datos["materias"] or []

    vistos_id, vistas_sedes = set(), {}
    for m in materias:
        mid = m.get("id")
        sede = m.get("sede")
        if not mid:
            fallos.append(f"V3 · una materia sin `id`: {m.get('materia')!r}")
            continue
        # V3
        if mid in vistos_id:
            fallos.append(f"V3 · identificador de materia repetido: `{mid}`")
        vistos_id.add(mid)
        # V4
        if not sede:
            fallos.append(f"V4 · `{mid}` no declara sede")
            continue
        if isinstance(sede, list):
            fallos.append(f"V4 · `{mid}` declara MAS DE UNA sede: una materia, una sede")
            continue
        if not existe(sede):
            fallos.append(f"V4 · `{mid}` · la sede no existe en el arbol: {sede}")
        # V5
        clave_sede = (sede, str(m.get("seccion", "")))
        if clave_sede in vistas_sedes:
            fallos.append(f"V5 · `{mid}` y `{vistas_sedes[clave_sede]}` declaran la MISMA "
                          f"sede y seccion ({sede} §{clave_sede[1] or '-'}): son dos "
                          f"nombres para una sola materia")
        vistas_sedes[clave_sede] = mid
        # V6
        estado = m.get("estado")
        if estado not in estados:
            fallos.append(f"V6 · `{mid}` · estado no valido: {estado!r}")
        # V7
        for campo in ("autoridad_superior", "acto_declarativo"):
            ruta = m.get(campo)
            if ruta and not existe(ruta):
                fallos.append(f"V7 · `{mid}` · `{campo}` no existe en el arbol: {ruta}")
        for ruta in (m.get("fuentes_tecnicas") or []):
            if not existe(ruta):
                fallos.append(f"V7 · `{mid}` · fuente tecnica que no existe: {ruta}")
        # V8 — PRH-2, ejecutada
        if estado == "vigente" and ES_APARATO_DE_GATE.search(sede):
            fallos.append(f"V8 · `{mid}` · una materia VIGENTE no puede tener por sede el "
                          f"aparato de un gate: {sede}. Se registra como EVIDENCIA y se "
                          f"cita como acto, nunca como norma (PRH-2)")
        # V9
        if m.get("autoridad_superior") == sede:
            fallos.append(f"V9 · `{mid}` · se declara autoridad superior de si misma")

    # V10
    compilados = []
    for z in (datos["zonas"] or []):
        patron, clase = z.get("patron"), z.get("clase")
        if clase not in clases:
            fallos.append(f"V10 · zona con clase no valida: {clase!r}")
        if not z.get("motivo"):
            fallos.append(f"V10 · zona sin motivo: {patron!r}. Una clasificacion sin motivo "
                          f"escrito no es revisable")
        try:
            compilados.append((re.compile(patron), clase))
        except (re.error, TypeError) as e:
            fallos.append(f"V10 · patron de zona invalido {patron!r}: {e}")
    if censo is not None and compilados:
        sin_zona = [r for r in censo if not any(rx.search(r) for rx, _ in compilados)]
        for r in sorted(sin_zona)[:20]:
            fallos.append(f"V10 · fichero versionado SIN ZONA que lo clasifique: {r}. "
                          f"Lo que ninguna zona nombra queda sin clasificar, y la "
                          f"clasificacion existe para que eso no ocurra")
        if len(sin_zona) > 20:
            fallos.append(f"V10 · y {len(sin_zona) - 20} mas")

    # V11
    ruta_indice = os.path.join(raiz, INDICE)
    if not os.path.exists(ruta_indice):
        fallos.append(f"V11 · no existe {INDICE}: sin el no hay sede desde la que este "
                      f"corpus este enlazado")
    else:
        with open(ruta_indice, encoding="utf-8") as fh:
            texto_indice = fh.read()
        enlazados = {"docs/canonico/" + n for n in re.findall(
            r"\]\(\.\./canonico/([A-Za-z0-9][-A-Za-z0-9_.]*\.(?:md|yml|yaml|py))\)",
            texto_indice)}
        dir_abs = os.path.join(raiz, DIR_CANONICO)
        presentes = sorted(DIR_CANONICO + "/" + n for n in os.listdir(dir_abs)
                           if os.path.isfile(os.path.join(dir_abs, n))
                           and not n.endswith(".pyc"))
        for rel in presentes:
            if rel not in enlazados:
                fallos.append(f"V11 · {rel} no esta enlazado por su RUTA COMPLETA desde "
                              f"{INDICE}. Es la condicion de admision de esta zona, y sin "
                              f"ella el fichero existe para nadie")
    return fallos


# ---------------------------------------------------------------------------
# AUTOPRUEBA · controles NEGATIVOS.
#
# Un validador que solo se ha visto pasar no esta verificado. Cada control introduce un
# defecto DELIBERADO sobre una copia EN MEMORIA del registro —el fichero real nunca se
# toca— y exige que la comprobacion señalada FALLE. Si no falla, el control no detecta.
# ---------------------------------------------------------------------------
def _con(datos, fn):
    d = copy.deepcopy(datos)
    fn(d)
    return d


def autoprueba(datos, raiz, censo):
    def dup_id(d):
        d["materias"].append(dict(d["materias"][0]))

    def dos_sedes(d):
        d["materias"][0]["sede"] = ["docs/canonico/00-EMPEZAR-AQUI.md",
                                    "docs/canonico/01-MODELO-DEL-SISTEMA.md"]

    def sede_inexistente(d):
        d["materias"][0]["sede"] = "docs/canonico/NO-EXISTE.md"

    def misma_sede(d):
        m = dict(d["materias"][0])
        m["id"] = "MAT-999"
        d["materias"].append(m)

    def estado_invalido(d):
        d["materias"][0]["estado"] = "casi-vigente"

    def gate_como_sede(d):
        d["materias"][0]["sede"] = "docs/evolucion/32-GATE-VERIFICACION-DOCE-HH2-F4C.md"
        d["materias"][0]["estado"] = "vigente"

    def sha_corto(d):
        d["base_de_consolidacion"]["commit"] = "ab35659"

    def zona_perdida(d):
        d["zonas"] = [z for z in d["zonas"] if not z["patron"].startswith("^kernel/")]

    def fuente_inexistente(d):
        d["materias"][0]["fuentes_tecnicas"] = ["kernel/operativo/NO-EXISTE.yaml"]

    def autoridad_circular(d):
        d["materias"][0]["autoridad_superior"] = d["materias"][0]["sede"]

    def clase_invalida(d):
        d["zonas"][0]["clase"] = "MUY_IMPORTANTE"

    casos = [
        ("N01 · identificador de materia repetido", dup_id, "V3"),
        ("N02 · una materia con dos sedes", dos_sedes, "V4"),
        ("N03 · sede que no existe en el arbol", sede_inexistente, "V4"),
        ("N04 · dos materias sobre la misma sede y seccion", misma_sede, "V5"),
        ("N05 · estado fuera del vocabulario", estado_invalido, "V6"),
        ("N06 · fuente tecnica que no existe", fuente_inexistente, "V7"),
        ("N07 · un GATE como sede de materia vigente", gate_como_sede, "V8"),
        ("N08 · autoridad superior de si misma", autoridad_circular, "V9"),
        ("N09 · SHA de base incompleto", sha_corto, "V2"),
        ("N10 · una zona retirada deja ficheros sin clasificar", zona_perdida, "V10"),
        ("N11 · clase de zona fuera del vocabulario", clase_invalida, "V10"),
    ]
    resultados = []
    for nombre, mutacion, esperado in casos:
        fallos = validar(_con(datos, mutacion), raiz, censo)
        detectado = any(f.startswith(esperado + " ") for f in fallos)
        resultados.append({"caso": nombre, "espera": esperado,
                           "detectado": bool(detectado)})
    return resultados


def main():
    ap = argparse.ArgumentParser(description="valida el registro de sedes canonicas de ADS")
    ap.add_argument("--raiz", default=RAIZ)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--autoprueba", action="store_true",
                    help="ejecuta los controles negativos sobre una copia en memoria")
    args = ap.parse_args()

    raiz = os.path.abspath(args.raiz)
    ruta = os.path.join(raiz, REGISTRO)
    if not os.path.isfile(ruta):
        print(f"no se encuentra {REGISTRO} bajo {raiz}", file=sys.stderr)
        return 2
    try:
        with open(ruta, encoding="utf-8") as fh:
            datos = yaml.safe_load(fh)
    except yaml.YAMLError as e:
        print(f"FALLO · el registro no es YAML valido: {e}", file=sys.stderr)
        return 1
    if not isinstance(datos, dict):
        print("FALLO · el registro no es un mapa de primer nivel", file=sys.stderr)
        return 1

    censo, aviso = ficheros_versionados(raiz)
    fallos = validar(datos, raiz, censo)
    negativos = autoprueba(datos, raiz, censo) if args.autoprueba else []
    no_detectados = [n for n in negativos if not n["detectado"]]

    if args.json:
        print(json.dumps({"ok": not fallos and not no_detectados, "fallos": fallos,
                          "aviso": aviso, "negativos": negativos,
                          "materias": len(datos.get("materias") or []),
                          "zonas": len(datos.get("zonas") or [])},
                         ensure_ascii=False, indent=2))
    else:
        print("VALIDACION DEL REGISTRO DE FUENTES CANONICAS")
        print(f"  materias declaradas : {len(datos.get('materias') or [])}")
        print(f"  zonas de clasificacion: {len(datos.get('zonas') or [])}")
        print(f"  ficheros versionados clasificados: "
              f"{len(censo) if censo is not None else 'NO DERIVABLE'}")
        if aviso:
            print(f"  AVISO: {aviso}")
        for f in fallos:
            print(f"  FALLO  {f}")
        for n in negativos:
            print(f"  {'OK    ' if n['detectado'] else 'NO DET'} {n['caso']} "
                  f"(espera {n['espera']})")
        print()
        if negativos:
            print(f"{len(negativos) - len(no_detectados)}/{len(negativos)} controles "
                  f"negativos detectados · {len(no_detectados)} NO detectados")
        print(f"{len(fallos)} fallos")
    return 1 if (fallos or no_detectados) else 0


if __name__ == "__main__":
    sys.exit(main())
