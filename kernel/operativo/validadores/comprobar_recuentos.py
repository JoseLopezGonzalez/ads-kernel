#!/usr/bin/env python3
"""comprobar_recuentos — ninguna cifra del corpus se escribe a mano.

Hallazgo A-24: once recuentos incorrectos, repartidos por cuatro de los cinco contratos
transversales, el índice, la nota de versión y el registro de pruebas. «Diecisiete
esquemas» cuando eran dieciséis, «35 métodos» cuando eran treinta y cuatro, «veintiocho
campos» sobre una tabla de veintinueve filas, «trece estaciones» sobre un diagrama de
catorce. Ninguno rompía la ejecución; en conjunto invalidaban la lectura del corpus como
fuente fiable, y aparecían en la propia nota que resumía el trabajo.

La fuente canónica de cada cifra es **el corpus**. Este validador la deriva, publica
`pruebas/RECUENTOS-generado.md` y comprueba que ningún documento afirme otra cosa.

Uso:
  python3 kernel/operativo/validadores/comprobar_recuentos.py [--json] [--raiz DIR]
                                                             [--generar]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402
from comprobar_contratos import Resultado  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

CARDINALES = {
    1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete",
    8: "ocho", 9: "nueve", 10: "diez", 11: "once", 12: "doce", 13: "trece",
    14: "catorce", 15: "quince", 16: "dieciséis", 17: "diecisiete", 18: "dieciocho",
    19: "diecinueve", 20: "veinte", 28: "veintiocho", 29: "veintinueve", 30: "treinta",
    34: "treinta y cuatro", 35: "treinta y cinco", 41: "cuarenta y uno",
}


def derivar(base=None):
    """Todas las cifras, calculadas desde el corpus. Es la única fuente."""
    base = os.path.abspath(base or RAIZ)
    lint = Lint(base, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    por_tipo = {}
    for tipo, datos, ruta, _l in lint.bloques:
        por_tipo.setdefault(tipo, []).append((datos, ruta))

    def n(tipo):
        return len(por_tipo.get(tipo, []))

    def ficheros(patron, raiz_rel):
        origen = os.path.join(base, raiz_rel)
        salida = []
        for dirpath, dirnames, filenames in os.walk(origen):
            dirnames[:] = [d for d in dirnames
                           if d != "__pycache__" and not d.startswith("legacy-")]
            for f in filenames:
                if re.search(patron, os.path.join(dirpath, f)):
                    salida.append(os.path.join(dirpath, f))
        return salida

    import yaml as _yaml
    def campos_obligatorios(esquema):
        ruta = os.path.join(base, f"kernel/operativo/esquemas/{esquema}.yaml")
        with open(ruta, encoding="utf-8") as fh:
            return len(_yaml.safe_load(fh).get("obligatorios") or [])

    cuenta = {
        "capacidades": n("capacidad"),
        "roles": n("rol"),
        "metodos": n("metodo"),
        "gates": n("gate"),
        "composiciones": n("composicion"),
        "escenarios": n("escenario"),
        "packs": n("pack"),
        "vetos": n("veto"),
        "rubricas": n("rubrica"),
        "handoffs": n("handoff"),
        "procesos": n("proceso"),
        "niveles_de_novedad": n("nivel-novedad"),
        "formas_de_conversacion": n("forma-conversacion"),
        "clases_de_entrada": n("entrada"),
        "secciones_de_memoria": n("memoria"),
        "esquemas": len(ficheros(r"/esquemas/.+\.yaml$", "kernel/operativo")),
        "validadores": len(ficheros(r"/validadores/.+\.py$", "kernel/operativo")),
        "prompts": len(ficheros(r"/prompts/.+\.md$", "kernel/operativo")),
        "campos_de_rol": campos_obligatorios("rol"),
        "campos_de_metodo": campos_obligatorios("metodo"),
        "campos_de_capacidad": campos_obligatorios("capacidad"),
        "campos_de_pack": campos_obligatorios("pack"),
        "contratos_transversales": len(ficheros(r"/contratos/C\d.*\.md$", "kernel/operativo")),
    }
    cuenta["composiciones_de_dis"] = len(
        [1 for d, ruta in por_tipo.get("composicion", []) if "/DIS/" in ruta])
    cuenta["roles_de_dis"] = len(
        [1 for d, _ in por_tipo.get("rol", []) if d.get("capacidad") == "DIS" and ":" not in d["id"]])
    cuenta["metodos_de_dis"] = len(
        [1 for d, _ in por_tipo.get("metodo", []) if d.get("capacidad") == "DIS"])
    return cuenta


# Dónde se AFIRMA cada cifra en prosa. Cada entrada es explícita y revisable: si una cifra
# nueva aparece en un documento, se añade aquí y deja de poder divergir en silencio.
AFIRMACIONES = [
    ("kernel/operativo/00-INDICE.md", r"el lenguaje canónico y los (\S+) tipos", "esquemas"),
    ("kernel/operativo/00-INDICE.md", r"PASOS 4 y 5 — las (\S+) capacidades", "capacidades"),
    ("kernel/operativo/00-INDICE.md", r"### Las (\S+) capacidades", "capacidades"),
    ("kernel/operativo/00-INDICE.md", r"los (\S+) contratos transversales", "contratos_transversales"),
    ("kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md",
     r"Contrato común de rol — (\S+) campos", "campos_de_rol"),
    ("kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md",
     r"declara los (\S+) campos del esquema", "campos_de_rol"),
    ("kernel/operativo/contratos/C3-METODO-EJECUTABLE.md",
     r"declara los (\S+) campos del esquema", "campos_de_metodo"),
    ("kernel/operativo/entrada/00-INDICE.md", r"las (\S+) estaciones", "estaciones_de_entrada"),
    ("kernel/operativo/entrada/00-INDICE.md", r"(\S+) formas de conversación", "formas_de_conversacion"),
    ("kernel/operativo/entrada/00-INDICE.md", r"las (\S+) clases de expresión", "clases_de_entrada"),
    ("kernel/operativo/entrada/02-CIRCUITO.md", r"^(\S+) estaciones\.", "estaciones_de_entrada"),
    ("kernel/operativo/entrada/03-FORMAS.md", r"Contiene (\S+) bloques", "formas_de_conversacion"),
    ("kernel/operativo/entrada/03-FORMAS.md",
     r"las clases de expresión son (\S+)", "clases_de_entrada"),
    ("kernel/operativo/capacidades/DIS/CAPACIDAD.md", r"— (\S+) contratos", "roles_de_dis"),
    ("kernel/operativo/capacidades/DIS/CAPACIDAD.md", r"— (\S+) procedimientos", "metodos_de_dis"),
    ("kernel/operativo/capacidades/DIS/CAPACIDAD.md", r"— (\S+) instrucciones operativas", "roles_de_dis"),
    ("kernel/operativo/capacidades/DIS/CAPACIDAD.md", r"— (\S+) matrices de composición", "composiciones_de_dis"),
    ("kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md",
     r"con sus (\S+) roles y sus (\S+) métodos", "roles_de_dis|metodos_de_dis"),
    ("kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md", r"Las (\S+) secciones del corpus", "secciones_de_memoria"),
    ("packs/00-QUE-ES-UN-PACK.md", r"los (\S+) códigos están reservados", "capacidades"),
]


def _palabra_a_numero(txt):
    txt = txt.strip().lower().strip(".,;:*_`")
    if txt.isdigit():
        return int(txt)
    for valor, palabra in CARDINALES.items():
        if txt == palabra:
            return valor
    return None


def t151_recuentos_derivados(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T151", "Ninguna cifra del corpus contradice el recuento derivado")
    cuenta = derivar(base)
    # las estaciones del circuito de entrada se cuentan del propio diagrama
    ruta_circ = os.path.join(base, "kernel/operativo/entrada/02-CIRCUITO.md")
    if os.path.exists(ruta_circ):
        with open(ruta_circ, encoding="utf-8") as fh:
            cuenta["estaciones_de_entrada"] = len(
                set(re.findall(r"│\s*(\d{1,2})\s{2}[A-ZÁÉÍÓÚÑ]", fh.read())))

    for rel, patron, claves in AFIRMACIONES:
        ruta = os.path.join(base, rel)
        if not os.path.exists(ruta):
            r.fallo(f"{rel}: no existe, y se declara como sitio donde vive una cifra")
            continue
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        m = re.search(patron, texto, re.M)
        if not m:
            r.fallo(f"{rel}: ya no contiene la afirmación «{patron}». Si la cifra se movió, "
                    f"esta tabla se actualiza; si desapareció, se borra la entrada")
            continue
        for i, clave in enumerate(claves.split("|")):
            declarado = _palabra_a_numero(m.group(i + 1))
            esperado = cuenta.get(clave)
            if declarado is None:
                r.fallo(f"{rel}: «{m.group(i + 1)}» no es un número reconocible para {clave}")
            elif esperado is None:
                r.fallo(f"{rel}: no sé derivar '{clave}'")
            elif declarado != esperado:
                r.fallo(f"{rel}: declara {declarado} {clave} y el corpus tiene {esperado}")
    return r


# ===========================================================================
#  LAS DOS CABECERAS QUE AFIRMABAN UN RECUENTO FALSO — `F-10` y `F-11`
# ===========================================================================
#  `06-DEUDA` §7 las resume así: los hallazgos externos con propietario y fase alcanzan
#  «a dos cabeceras que afirman recuentos falsos». Aquí se cierran por PROPIEDAD y no por
#  redacción: la primera deriva los dos cardinales y prohíbe la biyección MIENTRAS
#  difieran; la segunda deriva del propio fichero qué pruebas contiene y exige que la
#  cabecera nombre ésas y no otras.

# Formulaciones de la BIYECCIÓN entre formas de conversación y clases de expresión. Se
# declaran una a una y con su motivo: la aposición «uno por clase de expresión» era falsa
# por catorce contra nueve (`11-ARQ` §19, `F-10`).
# El salto de línea y la marca de cita del Markdown se toleran: una aposición no deja de
# afirmarse porque el párrafo se envuelva.
_HUECO = r"[\s>]+"
BIYECCIONES_PROHIBIDAS = [
    r"uno" + _HUECO + r"por" + _HUECO + r"clase" + _HUECO + r"de" + _HUECO + r"expresi[oó]n",
    r"una" + _HUECO + r"por" + _HUECO + r"clase" + _HUECO + r"de" + _HUECO + r"expresi[oó]n",
    r"uno" + _HUECO + r"por" + _HUECO + r"cada" + _HUECO + r"clase" + _HUECO + r"de" + _HUECO + r"expresi[oó]n",
    r"una" + _HUECO + r"por" + _HUECO + r"cada" + _HUECO + r"clase" + _HUECO + r"de" + _HUECO + r"expresi[oó]n",
]
DONDE_SE_AFIRMABA = [
    "kernel/operativo/entrada/03-FORMAS.md",
    "kernel/operativo/entrada/00-INDICE.md",
    "kernel/operativo/entrada/01-TAXONOMIA.md",
    "kernel/operativo/00-INDICE.md",
]


def t245_ninguna_cabecera_afirma_una_biyeccion_falsa(raiz=None):
    """`F-10`. La aposición sólo es falsa cuando se predica de las FORMAS.

    `01-TAXONOMIA.md` dice «uno por clase de expresión» de los bloques `ads:entrada`, y
    ahí es CIERTO: hay una clase de entrada por clase de expresión. Lo que era falso es
    predicarlo de las catorce formas de conversación. La regla mira la frase que contiene
    la aposición, no el fichero entero: prohibir la formulación en abstracto habría
    borrado una verdad para tapar una mentira.
    """
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T245", "Ninguna cabecera afirma una correspondencia uno a uno entre formas y clases")
    cuenta = derivar(base)
    formas, clases = cuenta.get("formas_de_conversacion"), cuenta.get("clases_de_entrada")
    if formas is None or clases is None:
        r.fallo("no se derivan las formas de conversación o las clases de expresión")
        return r
    if formas == clases:
        # La regla se APAGA sola si algún día los dos cardinales coinciden: entonces la
        # aposición dejaría de ser falsa y prohibirla sería censurar una verdad.
        return r
    for rel in DONDE_SE_AFIRMABA:
        ruta = os.path.join(base, rel)
        if not os.path.exists(ruta):
            continue
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        for patron in BIYECCIONES_PROHIBIDAS:
            for m in re.finditer(patron, texto, re.I):
                linea = texto[:m.start()].count("\n") + 1
                # La FRASE que contiene la aposición, acotada por su puntuación. Ampliar la
                # ventana a un número fijo de caracteres metía dentro la frase siguiente, y
                # con ella su negación: la regla se apagaba sola sobre la infracción.
                abre = max(texto.rfind(".", 0, m.start()),
                           texto.rfind("\n\n", 0, m.start())) + 1
                cierra = texto.find(".", m.end())
                frase = texto[abre:(cierra + 1) if cierra != -1 else m.end() + 80]
                if not re.search(r"forma-conversacion|formas de conversaci[oó]n", frase, re.I):
                    continue          # se predica de otra cosa, y de otra cosa puede ser cierto
                if re.search(r"\bNo hay\b|era falsa|deja de afirmar", frase, re.I):
                    continue          # la cita que DESMIENTE la aposición, no la afirma
                r.fallo(f"{rel}:{linea}: afirma «{m.group(0)}» de las formas de "
                        f"conversación, y hay {formas} formas frente a {clases} clases de "
                        f"expresión. La aposición es falsa (`11-ARQ` §19, `F-10`)")
    return r


def _rangos(texto):
    """Los identificadores `Tnn` que un texto cita, con los rangos EXPANDIDOS.

    `T75`–`T80` cita seis pruebas y escribe dos. Comparar sólo los extremos daría por
    enumerada una cabecera que se salta lo de en medio.
    """
    limpio = re.sub(r"\]\([^)]*\)", "]", texto)          # fuera los destinos de enlace
    citados, consumidos = set(), []
    for m in re.finditer(r"T(\d{2,3})\s*[`*]*\s*[–—-]\s*[`*]*\s*T(\d{2,3})", limpio):
        a, b = int(m.group(1)), int(m.group(2))
        if a <= b:
            citados |= set(range(a, b + 1))
        consumidos.append(m.span())
    for m in re.finditer(r"T(\d{2,3})", limpio):
        if any(ini <= m.start() < fin for ini, fin in consumidos):
            continue
        citados.add(int(m.group(1)))
    return citados


def t246_la_cabecera_enumera_las_pruebas_que_contiene(raiz=None):
    """`F-11`."""
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T246", "La cabecera de los escenarios enumera las pruebas que el fichero contiene")
    rel = "kernel/operativo/entrada/05-ESCENARIOS.md"
    ruta = os.path.join(base, rel)
    if not os.path.exists(ruta):
        r.fallo(f"{rel}: no existe, y es donde vive la cabecera que `F-11` corrige")
        return r
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    contenidas = {int(x) for x in re.findall(r"^id:\s*T(\d{2,3})\s*$", texto, re.M)}
    if not contenidas:
        r.fallo(f"{rel}: no contiene ningún bloque con `id: T…`")
        return r
    cabecera = texto.split("\n---\n", 1)[0]
    # Lo que la cabecera declara EXPRESAMENTE que vive en OTRO fichero no se cuenta como
    # citado, y además se comprueba: si está aquí, la cabecera miente por el otro lado.
    fuera = set()
    for m in re.finditer(r"([^.\n]*NO están aquí)", cabecera):
        fuera |= _rangos(m.group(1))
    citadas = _rangos(cabecera) - fuera
    for ident in sorted(citadas - contenidas):
        r.fallo(f"{rel}: la cabecera nombra T{ident} y el fichero NO lo contiene "
                f"(`11-ARQ` §19, `F-11`)")
    for ident in sorted(contenidas - citadas):
        r.fallo(f"{rel}: el fichero contiene T{ident} y la cabecera no lo enumera "
                f"(`11-ARQ` §19, `F-11`)")
    for ident in sorted(fuera & contenidas):
        r.fallo(f"{rel}: la cabecera declara que T{ident} NO está aquí, y sí está")
    return r


CABECERA = """# RECUENTOS — generado

<!-- GENERADO por validadores/comprobar_recuentos.py. No editar a mano. -->

La fuente canónica de estas cifras **es el corpus**, no este fichero ni ningún otro texto.
Cualquier documento que afirme una distinta hace fallar la prueba T151.

| qué | cuántos |
|---|---|
"""


def generar(base=None):
    base = os.path.abspath(base or RAIZ)
    cuenta = derivar(base)
    filas = "".join(f"| {k.replace('_', ' ')} | **{v}** |\n" for k, v in sorted(cuenta.items()))
    destino = os.path.join(base, "kernel/operativo/pruebas/RECUENTOS-generado.md")
    with open(destino, "w", encoding="utf-8") as fh:
        fh.write(CABECERA + filas)
    return destino, len(cuenta)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None)
    ap.add_argument("--generar", action="store_true")
    args = ap.parse_args()
    if args.generar:
        destino, n = generar(args.raiz)
        print(f"{n} recuentos · {destino}")
        return 0
    resultados = [t151_recuentos_derivados(args.raiz),
                  t245_ninguna_cabecera_afirma_una_biyeccion_falsa(args.raiz),
                  t246_la_cabecera_enumera_las_pruebas_que_contiene(args.raiz)]
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
