#!/usr/bin/env python3
"""comprobar_prompts — las señales ESTRUCTURALES que cada unidad de instrucción declara.

QUÉ DEMUESTRA Y QUÉ NO. Esta prueba es **estructural y heurística**: comprueba enlaces,
presencia de señales textuales, y comparaciones APROXIMADAS de autoridad y de idioma. Con
eso NO se demuestra coherencia semántica: que un prompt enseñe de verdad a hacer el
trabajo, que su tono no induzca a inventar, o que su ejemplo sea bueno, no lo decide
ninguna medida de texto. Esa lectura es humana y está documentada, prompt a prompt, en
`docs/rediseno/CORRECCIONES-POST-AUDITORIA.md` §6 — como revisión humana, no como algo que
este validador certifique.

La auditoría independiente sólo pudo revisar a fondo UNA de las unidades, y de ese único
contraste salieron dos hallazgos (A-08 y A-21). Lo mecánico se automatiza aquí para que no
dependa de que alguien se acuerde; lo cualitativo sigue exigiendo un lector.

VOCABULARIO. Son 42 UNIDADES DE INSTRUCCIÓN: 36 prompts canónicos con fichero propio en
`capacidades/<COD>/prompts/`, más 6 instrucciones EMBEBIDAS como sección del contrato de un
rol de pack. El recuento canónico `prompts: 36` cuenta sólo las primeras; llamar «42
prompts» al conjunto contradecía ese recuento.

Qué se comprueba, por unidad:

    1  lo declara EXACTAMENTE un rol, y el rol existe
    2  su cabecera enlaza el contrato del rol y, cuando el rol tiene método, el método
    3  no instruye hablar con el Owner si su rol declara `interaccion_owner.nivel: ninguna`
    4  nombra el gate contra el que cierra
    5  dice qué entrega
    6  dice cuándo devuelve, se bloquea o escala
    7  menciona el checkpoint cuando su contrato lo exige
    8  no se atribuye una decisión que su capacidad ESCALA
    9  está escrito en español

Uso:
  python3 kernel/operativo/validadores/comprobar_prompts.py [--json] [--raiz DIR] [--tabla]
"""
from __future__ import annotations

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

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402
from comprobar_contratos import Resultado, _palabras, _parecido  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Señales de que un texto instruye conversar con el Owner.
HABLA_CON_OWNER = re.compile(
    r"(?i)(pregunta[sr]?\s+al\s+owner|preg[úu]ntale\s+al\s+owner|le\s+preguntas|"
    r"conversas?\s+con\s+el\s+owner|ens[eé]ñale|mu[eé]strale\s+al\s+owner|"
    r"pide\s+al\s+owner|consulta\s+al\s+owner)")
# Marcas de salida, devolución y cierre. Se buscan como CONCEPTOS, no como palabra exacta.
SENALES = {
    "salida": r"(?i)(tu salida|entregas|produces|lo que entregas|tu resultado|tu dictamen|dejas escrito)",
    "devolucion": r"(?i)(devuelv|devoluci[óo]n|rechaz|vuelve a |escala|bloque)",
    "gate": r"(?i)gate:[a-z-]+",
    "checkpoint": r"(?i)checkpoint",
}
PALABRAS_ES = ("de", "que", "con", "para", "no", "el", "la", "los", "las", "por", "una")


def cargar(base):
    lint = Lint(base, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    por = {}
    for tipo, datos, ruta, _l in lint.bloques:
        por.setdefault(tipo, []).append((datos, ruta))
    return por


def prompts_del_corpus(base):
    """Devuelve {ruta_relativa: [ids de rol que la declaran]}."""
    por = cargar(base)
    mapa = {}
    for datos, _ in por.get("rol", []):
        p = (datos.get("prompt") or "").split("#")[0]
        if p:
            mapa.setdefault(p, []).append(datos["id"])
    return mapa, por


def t153_prompts(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T153", "Cada unidad de instrucción declara y enlaza las señales estructurales que su contrato exige")
    mapa, por = prompts_del_corpus(base)
    roles = {d["id"]: d for d, _ in por.get("rol", [])}
    caps = {d["id"]: d for d, _ in por.get("capacidad", [])}
    metodos = {d["id"]: d for d, _ in por.get("metodo", [])}
    detalle = {}

    # todo fichero de prompts/ tiene que estar declarado por algún rol
    # (los 36 canónicos; las 6 embebidas viven dentro del contrato de su rol)
    for dirpath, dirnames, filenames in os.walk(os.path.join(base, "kernel/operativo")):
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        if os.path.basename(dirpath) != "prompts":
            continue
        for f in sorted(filenames):
            rel = os.path.relpath(os.path.join(dirpath, f), base).replace(os.sep, "/")
            if rel not in mapa:
                r.fallo(f"{rel}: ningún rol lo declara en su campo `prompt`")

    for rel, ids in sorted(mapa.items()):
        ruta = os.path.join(base, rel)
        problemas = []
        if len(ids) > 1:
            problemas.append(f"lo declaran {len(ids)} roles: {ids}")
        if not os.path.exists(ruta):
            r.fallo(f"{rel}: no existe")
            continue
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        rol = roles[ids[0]]
        cap = caps.get(rol.get("capacidad"), {})
        es_seccion = "#" in (rol.get("prompt") or "")
        cabecera = texto[:1200]

        # 2 · enlaza contrato y método
        if not es_seccion:
            slug = ids[0].split("/")[-1]
            if f"roles/{slug}.md" not in cabecera:
                problemas.append("su cabecera no enlaza el contrato del rol")
            suyos = [m for m in (rol.get("metodo") or []) if m in metodos]
            if suyos and not any(f"metodos/{m.split('/')[-1]}.md" in cabecera for m in suyos):
                problemas.append("su cabecera no enlaza ninguno de sus métodos: "
                                 + ", ".join(suyos))

        # 3 · no habla con el Owner si su rol no puede
        if (rol.get("interaccion_owner") or {}).get("nivel") == "ninguna":
            m = HABLA_CON_OWNER.search(texto)
            if m:
                problemas.append(f"instruye hablar con el Owner («{m.group(0)}») y su "
                                 f"contrato declara interaccion_owner: ninguna")

        # 4-7 · las cuatro señales
        for clave, patron in SENALES.items():
            if clave == "checkpoint" and not (rol.get("checkpoint") or []):
                continue
            if not re.search(patron, texto):
                problemas.append(f"no dice nada sobre {clave}")

        # 8 · no se atribuye lo que su capacidad escala
        for item in (cap.get("autoridad", {}).get("escala") or []):
            w = _palabras(item)
            for parrafo in re.split(r"\n\s*\n", texto):
                if _parecido(w, _palabras(parrafo)) >= 0.5 and re.search(
                        r"(?i)\b(decides|decide|eliges|eliges tú|es tuya la decisión)\b", parrafo):
                    problemas.append(f"se atribuye lo que {cap.get('id')} escala: "
                                     f"«{item[:50]}»")
                    break

        # 9 · español
        minusc = texto.lower()
        if sum(1 for p in PALABRAS_ES if f" {p} " in minusc) < 4:
            problemas.append("no parece estar escrito en español")

        detalle[rel] = {"roles": ids, "problemas": problemas, "embebida": es_seccion}
        for p in problemas:
            r.fallo(f"{rel}: {p}")
    r.detalle = detalle
    return r


PRUEBAS = [t153_prompts]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None)
    ap.add_argument("--tabla", action="store_true", help="una fila por prompt")
    args = ap.parse_args()
    resultados = [f(args.raiz) for f in PRUEBAS]
    if args.json:
        print(json.dumps([{"id": x.id, "nombre": x.nombre,
                           "estado": "prueba-superada" if x.superada else "prueba-fallida",
                           "fallos": x.fallos} for x in resultados], ensure_ascii=False, indent=2))
        return 1 if any(not x.superada for x in resultados) else 0
    for x in resultados:
        print(f"{x.id}  {'SUPERADA' if x.superada else 'FALLIDA '}  {x.nombre}")
        for f in x.fallos:
            print(f"          · {f}")
        if args.tabla:
            det = getattr(x, "detalle", {})
            propios = sum(1 for d in det.values() if not d["embebida"])
            print(f"\n{len(det)} unidades de instrucción revisadas mecánicamente: "
                  f"{propios} prompts con fichero propio · {len(det) - propios} embebidas "
                  f"en roles de packs\n")
            for rel, d in sorted(det.items()):
                marca = "OK " if not d["problemas"] else "REV"
                clase = "embebida" if d["embebida"] else "prompt  "
                print(f"{marca} {clase} {d['roles'][0]:34} {rel}")
                for p in d["problemas"]:
                    print(f"        · {p}")
    fallidas = [x for x in resultados if not x.superada]
    print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if fallidas else 0


if __name__ == "__main__":
    sys.exit(main())
