#!/usr/bin/env python3
"""validar-f5 — controles pequenos sobre la matriz de F5 y sus borradores.

QUE COMPRUEBA, y nada mas:

  F1  la matriz es YAML valido y tiene las claves de primer nivel obligatorias
  F2  los siete entregables F5-A...F5-G estan declarados, y ninguno sobra
  F3  los siete criterios A1...A7 estan declarados, y ninguno sobra
  F4  todo identificador de fila es unico
  F5  el estado de cada fila esta en `estados_validos`, y NINGUNA fila usa una categoria
      vaga: el vocabulario es cerrado y se comprueba contra el declarado
  F6  COBERTURA DE PRESIONES: el censo VIGENTE se DERIVA del arbol —del barrido de las
      cabeceras `## `PN-` de la sede unica, excluyendo RETIRADA y FUSIONADA— y toda presion
      derivada tiene fila. Ninguna cifra se escribe a mano
  F7  toda fila con `decision_owner: SI` nombra una `decision_id`, y toda fila con
      `decision_owner: NO` no la nombra
  F8  toda `decision_id` de la matriz existe en el paquete de decisiones, y toda decision
      del paquete esta referenciada por al menos una fila. En los dos sentidos: una
      decision sin fila es una pregunta inventada, y una fila sin decision es una
      obligacion que nadie contesta
  F9  todo `artefacto` declarado existe en el arbol
  F10 TODO fichero de docs/f5/borradores/ lleva la marca `ESTADO-DEL-BORRADOR: NO_APROBADO`
      en sus primeras lineas. Un borrador sin marca podria presentarse como aprobado
  F11 NINGUN fichero de docs/f5/ lleva `ESTADO-DEL-BORRADOR: APROBADO`. Este arbol no
      contiene ninguna aprobacion del Owner, y esta comprobacion lo hace comprobable
  F12 todo marcador `PENDIENTE-DECISION-DEL-OWNER: <id>` de un borrador nombra una decision
      que existe en el paquete
  F13 el estado de fase NO se copia. Se comprueban DOS cosas, porque una sola no basta:
      (a) el ROTULO de estado aparece a lo sumo en UNA sede, que es
          docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md. «A lo sumo» y no «exactamente»: cuando
          F5 cambie de estado el rotulo desaparecera, y eso NO es un fallo;
      (b) NINGUN otro documento AFIRMA el estado de F5 con sus propias palabras. Es la
          forma por la que el estado se copia de verdad: no repitiendo el rotulo, sino
          escribiendo la frase al lado de la promesa de no copiarlo.
      EL BARRIDO NO SE LIMITA a docs/canonico/: alcanza tambien el indice de la iniciativa
      y todo docs/f5/, que son las zonas donde este macrobloque escribe.
      EXENCION DECLARADA, Y UNA SOLA: docs/f5/01-ACTO-DE-INICIO-DE-F5.md TRANSCRIBE
      literalmente el acto del Owner, que contiene esa frase. Reescribirla seria reescribir
      la orden, que es la misma razon por la que el corpus exime los documentos en voz del
      Owner. La exencion es POR FICHERO y esta escrita aqui, no en una lista aparte.

QUE NO COMPRUEBA, y se dice: no juzga si una clasificacion es correcta, no lee el contenido
de las sedes superiores, no verifica ninguna enmienda y NO CERTIFICA NADA. Un verde de aqui
no aprueba ninguna decision y no cierra ninguna fila.

LIMITACION HEREDADA, DECLARADA Y NO OCULTADA. Este fichero es codigo ejecutable sin guarda
de integridad: no esta en el manifiesto de validadores del kernel y no entra en la huella.
Es exactamente la limitacion CD-3 que el corpus registra de
docs/canonico/validar-fuentes-canonicas.py. NO se corrige aqui: meterlo en el manifiesto o
en la huella exige tocar kernel/ o tooling/, y CD-3 pertenece al endurecimiento instrumental
de F6. Se declara para que nadie lo cuente como garantia que no da.

Uso:
  python3 docs/f5/validar-f5.py [--raiz DIR] [--json]

Codigos de salida:  0 sin fallos  ·  1 hay fallos  ·  2 no se pudo empezar
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

try:
    import yaml
except ImportError:                                          # pragma: no cover
    print("validar-f5 requiere PyYAML", file=sys.stderr)
    sys.exit(2)

# La raiz se deriva de la ubicacion de este fichero y de nada mas. No se usa el cwd: es la
# leccion que la bateria del corpus aprendio por un defecto real.
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

MATRIZ = "docs/f5/MATRIZ-F5.yml"
PAQUETE = "docs/f5/20-PAQUETE-DE-DECISIONES-DEL-OWNER.md"
BORRADORES = "docs/f5/borradores"
SEDE_DEL_ESTADO = "docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md"
DIR_CANONICO = "docs/canonico"
# Las zonas donde este macrobloque escribe, y por tanto donde puede copiar un estado.
ZONAS_DEL_BARRIDO = ("docs/canonico", "docs/f5")
INDICE_INICIATIVA = "docs/evolucion/00-INDICE.md"
# La UNICA exencion, y su motivo esta en el docstring: transcribe el acto del Owner.
EXENTO_POR_TRANSCRIPCION = "docs/f5/01-ACTO-DE-INICIO-DE-F5.md"
SEDE_PRESIONES = "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md"

CLAVES = ("version", "descripcion", "derivacion", "entregables",
          "criterios_de_aceptacion", "estados_validos", "filas")

ENTREGABLES = ("F5-A", "F5-B", "F5-C", "F5-D", "F5-E", "F5-F", "F5-G")
CRITERIOS = ("A1", "A2", "A3", "A4", "A5", "A6", "A7")

MARCA_NO_APROBADO = "ESTADO-DEL-BORRADOR: NO_APROBADO"
MARCA_APROBADO = "ESTADO-DEL-BORRADOR: APROBADO"
RE_PENDIENTE = re.compile(r"PENDIENTE-DECISION-DEL-OWNER:\s*([DR]-[0-9]{2})")
RE_DECISION_PAQUETE = re.compile(r"^#{2,3}\s+`([DR]-[0-9]{2})`", re.M)
# La cabecera de una presion en su sede unica. El censo se DERIVA de aqui.
RE_PRESION = re.compile(r"^## `(PN-[0-9]+)` ·(.*)$", re.M)


class Resultado:
    def __init__(self):
        self.fallos = []
        self.datos = {}

    def fallo(self, control, msg):
        self.fallos.append(f"{control} · {msg}")


def _leer(raiz, rel):
    with open(os.path.join(raiz, rel), encoding="utf-8") as fh:
        return fh.read()


def presiones_vigentes(raiz):
    """El censo VIGENTE, DERIVADO del arbol. Excluye RETIRADA y FUSIONADA."""
    texto = _leer(raiz, SEDE_PRESIONES)
    vivas = []
    for ident, resto in RE_PRESION.findall(texto):
        if "RETIRADA" in resto or "FUSIONADA" in resto:
            continue
        vivas.append(ident)
    return vivas


def validar(raiz):
    r = Resultado()

    # ---- F1 -------------------------------------------------------------
    ruta_matriz = os.path.join(raiz, MATRIZ)
    if not os.path.exists(ruta_matriz):
        print(f"no se encuentra {MATRIZ}", file=sys.stderr)
        sys.exit(2)
    try:
        m = yaml.safe_load(_leer(raiz, MATRIZ))
    except yaml.YAMLError as exc:
        r.fallo("F1", f"la matriz no es YAML valido: {exc}")
        return r
    for clave in CLAVES:
        if clave not in m:
            r.fallo("F1", f"falta la clave de primer nivel `{clave}`")
    if r.fallos:
        return r

    filas = m["filas"]
    validos = set(m["estados_validos"])
    r.datos["filas"] = len(filas)
    r.datos["estados_validos"] = len(validos)

    # ---- F2 · los siete entregables -------------------------------------
    declarados = [e["id"] for e in m["entregables"]]
    if sorted(declarados) != sorted(ENTREGABLES):
        r.fallo("F2", f"los entregables declarados no son F5-A...F5-G: {declarados}")
    r.datos["entregables"] = len(declarados)

    # ---- F3 · los siete criterios ---------------------------------------
    crits = [c["id"] for c in m["criterios_de_aceptacion"]]
    if sorted(crits) != sorted(CRITERIOS):
        r.fallo("F3", f"los criterios declarados no son A1...A7: {crits}")
    r.datos["criterios"] = len(crits)

    # ---- F4 · unicidad ---------------------------------------------------
    ids = [f["id"] for f in filas]
    repes = {i for i in ids if ids.count(i) > 1}
    if repes:
        r.fallo("F4", f"identificadores de fila repetidos: {sorted(repes)}")

    # ---- F5 · vocabulario cerrado de estados -----------------------------
    for f in filas:
        if f.get("estado") not in validos:
            r.fallo("F5", f"{f['id']}: estado `{f.get('estado')}` fuera del vocabulario "
                          f"declarado. Una fila sin ubicacion inequivoca es el defecto")

    # ---- F6 · cobertura de presiones, DERIVADA ---------------------------
    vivas = presiones_vigentes(raiz)
    r.datos["presiones_vigentes_derivadas"] = len(vivas)
    cubiertas = {f["presion"] for f in filas if f.get("presion")}
    sin_fila = [p for p in vivas if p not in cubiertas]
    if sin_fila:
        r.fallo("F6", f"presiones VIGENTES sin fila en la matriz: {sin_fila}. El censo se "
                      f"deriva del arbol, y la matriz tiene que cubrirlo entero")
    sobran = [p for p in sorted(cubiertas) if p not in vivas]
    if sobran:
        r.fallo("F6", f"la matriz cubre presiones que su sede NO declara vigentes: {sobran}")

    # ---- F7 · coherencia decision_owner / decision_id --------------------
    for f in filas:
        tiene = bool(f.get("decision_id"))
        if f.get("decision_owner") == "SI" and not tiene:
            r.fallo("F7", f"{f['id']}: declara decision del Owner y no nombra `decision_id`")
        if f.get("decision_owner") == "NO" and tiene:
            r.fallo("F7", f"{f['id']}: no declara decision del Owner y nombra `decision_id`")

    # ---- F8 · el paquete y la matriz se cubren en los DOS sentidos -------
    ruta_paquete = os.path.join(raiz, PAQUETE)
    if not os.path.exists(ruta_paquete):
        r.fallo("F8", f"no existe el paquete de decisiones {PAQUETE}")
        del_paquete = set()
    else:
        del_paquete = set(RE_DECISION_PAQUETE.findall(_leer(raiz, PAQUETE)))
    de_la_matriz = {f["decision_id"] for f in filas if f.get("decision_id")}
    r.datos["decisiones_en_el_paquete"] = len(del_paquete)
    huerfanas = sorted(de_la_matriz - del_paquete)
    if huerfanas:
        r.fallo("F8", f"la matriz nombra decisiones que el paquete no plantea: {huerfanas}")
    inventadas = sorted(del_paquete - de_la_matriz)
    if inventadas:
        r.fallo("F8", f"el paquete plantea decisiones que ninguna fila necesita: "
                      f"{inventadas}. Una pregunta sin obligacion detras es una pregunta "
                      f"inventada")

    # ---- F9 · los artefactos declarados existen --------------------------
    for f in filas:
        art = f.get("artefacto")
        if art and not os.path.exists(os.path.join(raiz, art)):
            r.fallo("F9", f"{f['id']}: el artefacto declarado no existe: {art}")

    # ---- F10 y F12 · los borradores -------------------------------------
    dir_b = os.path.join(raiz, BORRADORES)
    n_borr = 0
    if os.path.isdir(dir_b):
        for nombre in sorted(os.listdir(dir_b)):
            if not nombre.endswith(".md"):
                continue
            n_borr += 1
            rel = f"{BORRADORES}/{nombre}"
            texto = _leer(raiz, rel)
            if MARCA_NO_APROBADO not in "\n".join(texto.splitlines()[:20]):
                r.fallo("F10", f"{rel}: sin la marca `{MARCA_NO_APROBADO}` en sus primeras "
                               f"veinte lineas. Un borrador sin marca puede presentarse "
                               f"como material aprobado")
            for ident in RE_PENDIENTE.findall(texto):
                if ident not in del_paquete:
                    r.fallo("F12", f"{rel}: el marcador nombra `{ident}`, que el paquete "
                                   f"no plantea")
    r.datos["borradores"] = n_borr

    # ---- F11 · nada esta aprobado en este arbol --------------------------
    for base, _dirs, ficheros in os.walk(os.path.join(raiz, "docs/f5")):
        for nombre in ficheros:
            ruta = os.path.join(base, nombre)
            rel = os.path.relpath(ruta, raiz).replace(os.sep, "/")
            if not nombre.endswith((".md", ".yml")):
                continue
            if MARCA_APROBADO in _leer(raiz, rel):
                r.fallo("F11", f"{rel}: contiene `{MARCA_APROBADO}`. Este arbol no puede "
                               f"contener ninguna aprobacion del Owner")

    # ---- F13 · una sola sede para el estado de fase ----------------------
    rotulo = re.compile(r"INICIADA\s*·\s*EN CURSO")
    # La forma en que un estado se copia de verdad: afirmandolo con palabras propias.
    afirmacion = re.compile(r"`?F5`?\s+(?:est[aá]|queda|sigue)\s+\**\s*(?:EN CURSO|INICIADA)",
                            re.IGNORECASE)

    candidatos = []
    for zona in ZONAS_DEL_BARRIDO:
        for base, _dirs, ficheros in os.walk(os.path.join(raiz, zona)):
            for nombre in sorted(ficheros):
                if nombre.endswith(".md"):
                    candidatos.append(os.path.relpath(os.path.join(base, nombre),
                                                      raiz).replace(os.sep, "/"))
    if os.path.exists(os.path.join(raiz, INDICE_INICIATIVA)):
        candidatos.append(INDICE_INICIATIVA)

    con_rotulo, con_afirmacion = [], []
    for rel in sorted(set(candidatos)):
        texto = _leer(raiz, rel)
        if rotulo.search(texto):
            con_rotulo.append(rel)
        if rel != EXENTO_POR_TRANSCRIPCION and afirmacion.search(texto):
            con_afirmacion.append(rel)

    r.datos["ficheros_barridos_por_F13"] = len(set(candidatos))
    r.datos["sedes_con_el_rotulo_de_estado"] = len(con_rotulo)
    if [x for x in con_rotulo if x != SEDE_DEL_ESTADO]:
        r.fallo("F13", f"el rotulo de estado de `F5` aparece fuera de su unica sede: "
                       f"{[x for x in con_rotulo if x != SEDE_DEL_ESTADO]}. Su sede es "
                       f"{SEDE_DEL_ESTADO}")
    if [x for x in con_afirmacion if x != SEDE_DEL_ESTADO]:
        r.fallo("F13", f"estos documentos AFIRMAN el estado de `F5` con sus propias "
                       f"palabras: {[x for x in con_afirmacion if x != SEDE_DEL_ESTADO]}. "
                       f"Un estado copiado caduca solo en cuanto la fase avanza")
    return r


def main():
    ap = argparse.ArgumentParser(description="controles de la matriz de F5")
    ap.add_argument("--raiz", default=RAIZ)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    raiz = os.path.abspath(args.raiz)

    r = validar(raiz)

    if args.json:
        print(json.dumps({"fallos": r.fallos, "datos": r.datos}, ensure_ascii=False, indent=2))
    else:
        print("CONTROLES DE LA MATRIZ DE F5")
        for clave, valor in r.datos.items():
            print(f"  {clave:34s}: {valor}")
        print()
        for f in r.fallos:
            print(f"  FALLO  {f}")
        print()
        print(f"{len(r.fallos)} fallos")
    return 1 if r.fallos else 0


if __name__ == "__main__":
    sys.exit(main())
