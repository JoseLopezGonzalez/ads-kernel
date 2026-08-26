#!/usr/bin/env python3
"""comprobar_contratos — pruebas de conformidad ESTRUCTURALES, ejecutables hoy.

A diferencia de ads_lint (que valida forma), esto comprueba propiedades del contenido
que las secciones (a) y (b) y los contratos C1-C5 declaran obligatorias, y que NO
necesitan runtime para verificarse.

Cada comprobación corresponde a una prueba numerada. La salida dice, por prueba,
SUPERADA o FALLIDA, con el detalle de cada fallo.

Uso:
  python3 kernel/operativo/validadores/comprobar_contratos.py [--json] [--prueba T86]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def fijar_raiz(nueva):
    """Permite ejecutar las pruebas contra una COPIA del corpus.

    Lo usa `comprobar_negativos.py` para introducir una infracción deliberada en un
    directorio temporal y demostrar que la prueba falla. El corpus real nunca se toca.
    """
    global RAIZ
    RAIZ = os.path.abspath(nueva)

# Marcas comerciales que NO pueden aparecer como requisito en kernel ni packs (K0.8, C2).
# Expresiones regulares, no subcadenas: «llama» es un verbo corriente en castellano y
# «cómo llama el Owner a esto» no es una marca. Se exige la forma en que la marca aparece
# de verdad cuando alguien la usa como requisito.
MARCAS = [
    r"\bclaude\b", r"\banthropic\b", r"\bopenai\b", r"\bgpt-?[0-9]", r"\bchatgpt\b",
    r"\bcodex\b", r"\bgemini\b", r"\bcopilot\b", r"\bllama[ -][0-9]", r"\bllama\.cpp\b",
    r"\bmistral\b", r"\bcohere\b", r"\bollama\b", r"\bbedrock\b", r"\bvertex ai\b",
]
# Ficheros donde nombrar una marca es legítimo: hablan del adaptador o de la prohibición.
EXENTOS_MARCA = {
    "kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md",
}


class Resultado:
    def __init__(self, pid, nombre):
        self.id, self.nombre, self.fallos = pid, nombre, []

    @property
    def superada(self):
        return not self.fallos

    def fallo(self, msg):
        self.fallos.append(msg)


def cargar():
    lint = Lint(RAIZ, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    porTipo = {}
    for tipo, datos, ruta, linea in lint.bloques:
        porTipo.setdefault(tipo, []).append((datos, ruta, linea))
    return porTipo


def t86_autoridad_subconjunto(b):
    r = Resultado("T86", "La autoridad de un rol no excede la de su capacidad")
    caps = {d["id"]: d for d, _, _ in b.get("capacidad", [])}
    for datos, ruta, _ in b.get("rol", []):
        cap = caps.get(datos.get("capacidad"))
        if not cap:
            r.fallo(f"{datos.get('id')}: su capacidad '{datos.get('capacidad')}' no tiene ficha")
            continue
        veta_rol = datos.get("autoridad", {}).get("veta") or []
        veta_cap = cap.get("autoridad", {}).get("veta") or []
        if veta_rol and not veta_cap:
            r.fallo(f"{datos['id']}: veta {veta_rol} pero {cap['id']} no declara veto alguno")
        if datos.get("veto") and not veta_cap:
            r.fallo(f"{datos['id']}: declara contrato de veto y {cap['id']} no veta nada")
    return r


def t87_independencia_gana(b):
    r = Resultado("T87", "Ninguna composición permite combinar dos roles que ella declara independientes")
    for datos, ruta, _ in b.get("composicion", []):
        prohibidos = set()
        for indep in datos.get("independientes") or []:
            sujeto = indep.get("rol")
            for objeto in indep.get("de") or []:
                if isinstance(objeto, str) and re.fullmatch(r"([a-z0-9-]+:)?[A-Z]{3}/[a-z0-9-]+", objeto):
                    prohibidos.add(frozenset((sujeto, objeto)))
        for comb in datos.get("combinables") or []:
            roles = comb.get("roles") or []
            for i, a in enumerate(roles):
                for bb in roles[i + 1:]:
                    if frozenset((a, bb)) in prohibidos:
                        r.fallo(f"{datos['id']}: combina '{a}' con '{bb}', "
                                f"y la misma composición los declara independientes")
    return r


def t88_prompt_existe(b):
    r = Resultado("T88", "Todo rol apunta a un prompt operativo que existe")
    for datos, ruta, _ in b.get("rol", []):
        prompt = datos.get("prompt")
        if not prompt:
            r.fallo(f"{datos.get('id')}: sin prompt declarado")
            continue
        # el prompt puede vivir en su propio fichero, o como sección del contrato
        fichero = prompt.split("#")[0]
        ancla = prompt.split("#")[1] if "#" in prompt else None
        ruta_prompt = os.path.join(RAIZ, fichero)
        if not os.path.exists(ruta_prompt):
            r.fallo(f"{datos['id']}: el prompt declarado no existe → {fichero}")
            continue
        if ancla:
            with open(ruta_prompt, encoding="utf-8") as fh:
                cuerpo = fh.read().lower()
            if f"## {ancla.replace('-', ' ')}" not in cuerpo and f"## {ancla}" not in cuerpo:
                r.fallo(f"{datos['id']}: el prompt apunta a la sección '#{ancla}', que no existe en {fichero}")
    return r


# T01-T74 están definidas en las secciones (a) y (b) aprobadas: son referencias válidas
# aunque no existan como bloque ads:escenario en este corpus.
HEREDADAS = {f"T{n:02d}" for n in range(1, 75)}


def t89_reanudacion_con_prueba(b):
    r = Resultado("T89", "Toda prueba de reanudación cita un escenario que existe")
    ids = {d.get("id") for d, _, _ in b.get("escenario", [])} | HEREDADAS
    for datos, ruta, _ in b.get("metodo", []):
        texto = datos.get("prueba_de_reanudacion", "")
        citadas = set(re.findall(r"\bT\d{2,3}\b", texto))
        if not citadas:
            r.fallo(f"{datos.get('id')}: su prueba de reanudación no cita ningún escenario numerado")
            continue
        for t in citadas:
            if t not in ids:
                r.fallo(f"{datos['id']}: cita {t}, que no está declarada como ads:escenario "
                        f"ni pertenece a T01-T74 de las secciones aprobadas")
    return r


def t90_roles_coherentes(b):
    r = Resultado("T90", "Capacidades y roles se referencian mutuamente sin huérfanos")
    caps = {d["id"]: d for d, _, _ in b.get("capacidad", [])}
    roles = {d["id"]: d for d, _, _ in b.get("rol", [])}
    for cid, cap in caps.items():
        for rid in cap.get("roles", []):
            if rid not in roles:
                r.fallo(f"{cid}: declara el rol {rid}, que no tiene contrato")
            elif roles[rid].get("capacidad") != cid:
                r.fallo(f"{cid}: declara {rid}, pero ese rol dice pertenecer a {roles[rid].get('capacidad')}")
    for rid, rol in roles.items():
        cid = rol.get("capacidad")
        # Los roles de pack se ADJUNTAN a la capacidad al materializar (packs/00-QUE-ES-UN-PACK):
        # la capacidad del kernel no los conoce y no puede listarlos.
        if ":" in rid:
            continue
        if cid in caps and rid not in caps[cid].get("roles", []):
            r.fallo(f"{rid}: dice pertenecer a {cid}, que no lo lista entre sus roles")
    return r


def t91_metodos_con_gate_y_pasos(b):
    r = Resultado("T91", "Todo paso de todo método declara cuándo termina")
    for datos, ruta, _ in b.get("metodo", []):
        for paso in datos.get("pasos", []):
            if not paso.get("termina_cuando"):
                r.fallo(f"{datos.get('id')} paso {paso.get('n')}: sin `termina_cuando`")
            if paso.get("hace", "").strip().lower().startswith(("valorar si", "decidir si conviene")):
                r.fallo(f"{datos.get('id')} paso {paso.get('n')}: el paso delega el criterio en vez de escribirlo")
    return r


def t92_sin_marca(_b):
    r = Resultado("T92", "Ningún contrato del kernel ni de un pack exige una marca concreta")
    for ambito in ("kernel/operativo", "packs"):
        for dirpath, dirnames, filenames in os.walk(os.path.join(RAIZ, ambito)):
            dirnames[:] = [d for d in dirnames if not d.startswith("legacy-") and d != "__pycache__"]
            for nombre in filenames:
                if not nombre.endswith(".md"):
                    continue
                ruta = os.path.join(dirpath, nombre)
                rel = os.path.relpath(ruta, RAIZ)
                if rel in EXENTOS_MARCA:
                    continue
                with open(ruta, encoding="utf-8") as fh:
                    bajo = fh.read().lower()
                for patron in MARCAS:
                    hallado = re.search(patron, bajo)
                    if hallado:
                        r.fallo(f"{rel}: nombra «{hallado.group(0)}»; el contrato canónico es neutral de proveedor")
    return r


def t134_sin_documentos_para_nadie(b):
    """Un documento que ningún otro enlaza y cuyos bloques nadie cita existe para nadie.

    Es el hallazgo que la revisión adversarial busca bajo el nombre de
    «autorreferencia sin producto», y aquí queda comprobado de forma permanente.
    """
    r = Resultado("T134", "Ningún documento del corpus existe para nadie")
    corpus = {}
    for ambito in ("kernel/operativo", "packs"):
        for dirpath, dirnames, filenames in os.walk(os.path.join(RAIZ, ambito)):
            dirnames[:] = [d for d in dirnames
                           if d not in ("__pycache__",) and not d.startswith("legacy-")]
            for nombre in filenames:
                if nombre.endswith((".md", ".py", ".yaml")):
                    ruta = os.path.join(dirpath, nombre)
                    with open(ruta, encoding="utf-8") as fh:
                        corpus[os.path.abspath(ruta)] = fh.read()

    ids_por_fichero = {}
    for _, datos, ruta, _ in [(t, d, f, l) for t, d, f, l in
                              [(tt, dd, ff, ll) for tt in b for dd, ff, ll in b[tt]]]:
        ids_por_fichero.setdefault(os.path.abspath(ruta), []).append(datos.get("id"))

    for ruta, _ in corpus.items():
        if not ruta.endswith(".md"):
            continue
        base = os.path.basename(ruta)
        otros = {k: v for k, v in corpus.items() if k != ruta}
        entrante = any(base in txt for txt in otros.values())
        citado = any(i and any(i in txt for txt in otros.values())
                     for i in ids_por_fichero.get(ruta, []))
        if not entrante and not citado:
            r.fallo(f"{os.path.relpath(ruta, RAIZ)}: nadie lo enlaza y nadie cita sus bloques")
    return r


def t135_composicion_respeta_el_contrato(b):
    """Ninguna composición combina dos roles que el CONTRATO de uno declara independientes.

    T87 comprueba la coherencia interna de cada composición. Esto comprueba algo distinto
    y más fuerte: que ninguna composición rebaje lo que el contrato del rol exige.
    """
    r = Resultado("T135", "Ninguna composición rebaja la independencia que exige un contrato")
    roles = {d["id"]: d for d, _, _ in b.get("rol", [])}
    for datos, ruta, _ in b.get("composicion", []):
        for comb in datos.get("combinables") or []:
            pareja = comb.get("roles") or []
            for i, a in enumerate(pareja):
                for bb in pareja[i + 1:]:
                    for uno, otro in ((a, bb), (bb, a)):
                        rol = roles.get(uno)
                        if not rol:
                            continue
                        ind = rol.get("independencia") or {}
                        if not ind.get("requiere_independencia"):
                            continue
                        if otro in (ind.get("de") or []):
                            r.fallo(f"{datos['id']}: combina '{uno}' con '{otro}', y el "
                                    f"contrato de {uno} exige independencia de él")
    return r


# ---------------------------------------------------------------------------
# Pruebas añadidas en la corrección post-auditoría. Cada una nombra su hallazgo.
# ---------------------------------------------------------------------------

CODIGO_CAP = re.compile(r"\b([A-Z]{3})\b")


def t136_vetos_no_se_arbitran(b):
    """A-06 · a.5: dos vetos incompatibles NO se arbitran entre las capacidades.

    Escalan al Owner con ambas materias. La ÚNICA excepción es un veto declarado
    no levantable por regla dura del kernel (G27). Por tanto:
      · un veto LEVANTABLE nunca puede aparecer como el que prevalece;
      · toda cláusula de colisión debe declarar el escalado al Owner.
    """
    r = Resultado("T136", "Ningún veto arbitra a otro veto levantable: ambos detienen y escalan")
    vetos = {d["id"]: d for d, _, _ in b.get("veto", [])}
    por_capacidad = {d.get("capacidad"): d for d in vetos.values()}
    for vid, datos in vetos.items():
        colision = (datos.get("colision") or "")
        # (a) nadie declara que prevalece un veto levantable
        for m in re.finditer(r"(?i)\bprevalece[nr]?\s+(?:el\s+veto\s+de\s+)?([A-Z]{3})\b", colision):
            otro = por_capacidad.get(m.group(1))
            if otro is None:
                continue
            if otro.get("levantable") == "si":
                r.fallo(f"{vid}: declara que prevalece {m.group(1)}, cuyo veto es LEVANTABLE. "
                        f"a.5 sólo admite prevalencia de un veto no levantable por regla dura")
        # (b) el propio veto, si es levantable, no puede reclamar prevalencia para sí
        if datos.get("levantable") == "si":
            propio = datos.get("capacidad", "")
            if re.search(r"(?i)prevalece\s+" + re.escape(propio) + r"\b", colision):
                r.fallo(f"{vid}: es levantable y se declara prevaleciente sobre otro veto")
        # (c) toda colisión declara el escalado al Owner
        if not re.search(r"(?i)escala\w*\s+al\s+owner", colision):
            r.fallo(f"{vid}: su cláusula de colisión no declara el escalado al Owner (a.5)")
    return r


def t137_dsp_no_cancela_por_contenido(b):
    """A-23 · b.7: DSP NUNCA posee por sí mismo la autoridad semántica para cancelar."""
    r = Resultado("T137", "DSP no declara autoridad semántica sobre ninguna cancelación")
    for datos, ruta, _ in b.get("rol", []) + b.get("capacidad", []):
        cap = datos.get("capacidad") or datos.get("id")
        if cap != "DSP":
            continue
        aut = datos.get("autoridad", {}) or {}
        decide = list(aut.get("decide") or []) + list(aut.get("decide_sola") or [])
        for item in decide:
            if re.search(r"(?i)cancela", str(item)):
                r.fallo(f"{datos.get('id')}: DECIDE «{str(item)[:70]}». "
                        f"b.7: la cancelación se propone y se ejecuta, nunca se decide desde DSP")
    return r


VARIABLES_NOVEDAD = ("superficie_construida", "memoria_vigente", "dir_sustituye",
                     "patron_cubre", "premium_o_nuevo")
EJES_VISUALES = ("personalidad", "intencion", "jerarquia", "sistema", "actualidad",
                 "respuesta", "acabado", "fidelidad", "alma")


def _evaluar_condicion(expr, entorno):
    """Evalúa una condición booleana SIN ejecutar código arbitrario.

    Sólo se admiten nombres de variable declarados, `and`, `or`, `not` y paréntesis. Una
    condición que no encaje en eso no es comprobable, y por tanto no es una condición.
    """
    import ast

    def visitar(nodo):
        if isinstance(nodo, ast.Expression):
            return visitar(nodo.body)
        if isinstance(nodo, ast.BoolOp):
            valores = [visitar(v) for v in nodo.values]
            return all(valores) if isinstance(nodo.op, ast.And) else any(valores)
        if isinstance(nodo, ast.UnaryOp) and isinstance(nodo.op, ast.Not):
            return not visitar(nodo.operand)
        if isinstance(nodo, ast.Name):
            if nodo.id not in entorno:
                raise ValueError(f"variable no declarada: {nodo.id}")
            return entorno[nodo.id]
        if isinstance(nodo, ast.Constant) and isinstance(nodo.value, bool):
            return nodo.value
        raise ValueError(f"expresión no admitida: {ast.dump(nodo)[:60]}")

    return visitar(ast.parse(expr, mode="eval"))


def t138_escala_total_y_alcanzable(b):
    """A-07 · la escala de novedad cubre todos los casos y ningún nivel es inalcanzable.

    La versión anterior preguntaba en N4 «¿no existe memoria de diseño?», que es cierto
    también para un producto construido sin dirección escrita. Como N4 se evaluaba antes,
    N3 no se alcanzaba nunca y un brownfield recibía el método de fundación.
    """
    r = Resultado("T138", "La escala de novedad es total y sus cinco niveles son alcanzables")
    niveles = sorted((d for d, _, _ in b.get("nivel-novedad", [])),
                     key=lambda d: d.get("orden", 0))
    if len(niveles) != 5:
        r.fallo(f"se declaran {len(niveles)} niveles y la escala tiene cinco")
        return r
    ordenes = [n["orden"] for n in niveles]
    if len(set(ordenes)) != len(ordenes):
        r.fallo(f"dos niveles comparten orden de evaluación: {ordenes}")

    alcanzados, sin_nivel = {}, []
    for combo in range(2 ** len(VARIABLES_NOVEDAD)):
        entorno = {v: bool(combo >> i & 1) for i, v in enumerate(VARIABLES_NOVEDAD)}
        elegido = None
        for nivel in niveles:
            try:
                cierto = _evaluar_condicion(nivel["condicion_formal"], entorno)
            except ValueError as exc:
                r.fallo(f"{nivel['id']}: condición no comprobable — {exc}")
                return r
            if cierto:
                elegido = nivel["id"]
                break
        if elegido is None:
            sin_nivel.append(entorno)
        else:
            alcanzados.setdefault(elegido, []).append(entorno)

    if sin_nivel:
        muestra = ", ".join(k for k, v in sin_nivel[0].items() if v) or "(todas falsas)"
        r.fallo(f"{len(sin_nivel)} combinaciones no producen NINGÚN nivel. "
                f"Ejemplo: {muestra}. La escala no es total")
    for nivel in niveles:
        if nivel["id"] not in alcanzados:
            r.fallo(f"{nivel['id']} ({nivel['nombre']}) es INALCANZABLE: ninguna de las "
                    f"{2 ** len(VARIABLES_NOVEDAD)} combinaciones lo produce. Su método "
                    f"{nivel['metodo']} no se elige nunca")
    return r


def t139_ningun_nivel_omite_un_gate(b):
    """A-08 · ningún nivel de novedad omite un gate obligatorio de Diseño."""
    r = Resultado("T139", "Ningún nivel de novedad omite un gate: lo que cambia es la evidencia reutilizable")
    niveles = {d["id"]: d for d, _, _ in b.get("nivel-novedad", [])}
    if not niveles:
        r.fallo("no hay ningún bloque ads:nivel-novedad declarado")
        return r
    for nid, nivel in sorted(niveles.items()):
        for gate in ("gate:usabilidad", "gate:excelencia-visual"):
            if gate not in (nivel.get("gates_obligatorios") or []):
                r.fallo(f"{nid}: no declara {gate} como obligatorio. Un nivel pequeño "
                        f"explora menos; no verifica menos")
        reut = set(nivel.get("ejes_reutilizables") or [])
        nunca = set(nivel.get("ejes_nunca_reutilizables") or [])
        if reut & nunca:
            r.fallo(f"{nid}: {sorted(reut & nunca)} está a la vez en reutilizables y en "
                    f"nunca reutilizables")
        if reut | nunca != set(EJES_VISUALES):
            faltan = set(EJES_VISUALES) - (reut | nunca)
            sobran = (reut | nunca) - set(EJES_VISUALES)
            if faltan:
                r.fallo(f"{nid}: los ejes {sorted(faltan)} no se declaran ni reutilizables "
                        f"ni propios: quedarían sin régimen")
            if sobran:
                r.fallo(f"{nid}: declara ejes que la rúbrica no tiene: {sorted(sobran)}")
        for imprescindible in ("acabado", "fidelidad"):
            if imprescindible in reut:
                r.fallo(f"{nid}: declara `{imprescindible}` reutilizable, y depende de esta "
                        f"aplicación concreta: nunca se hereda de un patrón")
        if reut and not (nivel.get("evidencia_de_vigencia") or []):
            r.fallo(f"{nid}: reutiliza ejes y no declara qué evidencia demuestra que el "
                    f"patrón previo sigue siendo aplicable")
        # las estaciones de los dos gates son la 8 y la 9 del ciclo de calidad
        estaciones = set(nivel.get("estaciones") or [])
        for est, nombre in ((8, "validación de uso · gate:usabilidad"),
                            (9, "validación visual · gate:excelencia-visual")):
            if est not in estaciones:
                r.fallo(f"{nid}: su lista de estaciones omite la {est} ({nombre}), y declara "
                        f"ese gate obligatorio")

    # la tabla de 04-CICLO se DERIVA de estos bloques: se comprueba que coincide
    ruta = os.path.join(RAIZ, "kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md")
    if os.path.exists(ruta):
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        for nid, nivel in sorted(niveles.items()):
            m = re.search(rf"^{nid}\s+(.+)$", texto, re.M)
            if not m:
                r.fallo(f"04-CICLO-DE-CALIDAD.md no declara las estaciones de {nid}")
                continue
            linea = m.group(1)
            if "las trece" in linea:
                declaradas = set(range(1, 14))
            else:
                declaradas = {int(x) for x in re.findall(r"\b(\d+)\b", linea.split("(")[0])}
            if declaradas != set(nivel.get("estaciones") or []):
                r.fallo(f"{nid}: 04-CICLO declara {sorted(declaradas)} y su bloque canónico "
                        f"declara {sorted(nivel.get('estaciones') or [])}. Dos fuentes para "
                        f"la misma verdad")
    return r


def t144_usabilidad_tiene_portador_en_con(b):
    """A-13 · gate:usabilidad dice aplicarse a las capas de CON, y nada lo vinculaba."""
    r = Resultado("T144", "El gate de usabilidad tiene portador computable en Construcción")
    gates = {d["id"]: d for d, _, _ in b.get("gate", [])}
    usab = gates.get("gate:usabilidad")
    impl = gates.get("gate:implementacion-completa")
    if not usab or not impl:
        r.fallo("falta gate:usabilidad o gate:implementacion-completa")
        return r
    if "CON" not in (usab.get("aplica_a") or ""):
        return r      # si deja de aplicarse a CON, no hay nada que vincular
    ids = {c.get("id") for c in impl.get("comprobaciones") or []}
    textos = " ".join(str(c.get("comprueba", "")) + str(c.get("como", ""))
                      for c in impl.get("comprobaciones") or [])
    if "superficie-usable" not in ids:
        r.fallo("gate:implementacion-completa no comprueba la usabilidad de lo construido, "
                "y gate:usabilidad declara aplicarse a las capas de CON")
    if "gate:usabilidad" not in textos:
        r.fallo("la comprobación de superficie usable no cita gate:usabilidad: el vínculo "
                "no es rastreable")
    if "validacion-de-uso" not in textos:
        r.fallo("no se declara QUIÉN juzga la evidencia de usabilidad de lo construido: "
                "sin eso, la juzga quien la produjo")
    return r


PRUEBAS = [t86_autoridad_subconjunto, t87_independencia_gana, t88_prompt_existe,
           t89_reanudacion_con_prueba, t90_roles_coherentes, t91_metodos_con_gate_y_pasos,
           t92_sin_marca, t135_composicion_respeta_el_contrato,
           t136_vetos_no_se_arbitran, t137_dsp_no_cancela_por_contenido,
           t138_escala_total_y_alcanzable, t139_ningun_nivel_omite_un_gate,
           t144_usabilidad_tiene_portador_en_con]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--prueba", default=None)
    ap.add_argument("--raiz", default=None, help="ejecutar contra otra copia del corpus")
    args = ap.parse_args()
    if args.raiz:
        fijar_raiz(args.raiz)
    b = cargar()
    resultados = [f(b) for f in PRUEBAS]
    if args.prueba:
        resultados = [r for r in resultados if r.id == args.prueba]
    if args.json:
        print(json.dumps([{"id": r.id, "nombre": r.nombre,
                           "estado": "prueba-superada" if r.superada else "prueba-fallida",
                           "fallos": r.fallos} for r in resultados], ensure_ascii=False, indent=2))
    else:
        for r in resultados:
            estado = "SUPERADA" if r.superada else "FALLIDA "
            print(f"{r.id}  {estado}  {r.nombre}")
            for f in r.fallos:
                print(f"          · {f}")
        fallidas = [r for r in resultados if not r.superada]
        print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if any(not r.superada for r in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
