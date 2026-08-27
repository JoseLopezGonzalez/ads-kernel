#!/usr/bin/env python3
"""comprobar_fuentes — validación ESTÁTICA de la composición del producto.

Un ADS Project es VÁLIDO aunque su workspace no esté materializado. Son dos cosas
distintas y se comprueban por separado (C6):

    comprobar_fuentes.py   el manifiesto está bien formado y el corpus no se contradice.
                           NO exige que ninguna fuente esté clonada. Corre en CI sin
                           credenciales de ningún repositorio privado.

    workspace.py check     el workspace está disponible: qué fuentes están en disco, si
                           son el repositorio esperado y en qué estado. Exige el disco.

El análisis del manifiesto NO se reimplementa aquí: se importa de `tooling/workspace.py`.
Dos implementaciones de la misma validación derivan, y la que miente acaba siendo la que
nadie mira — es el mismo motivo por el que `kernel-status.sh` no recalcula la huella.

Uso:
  python3 kernel/operativo/validadores/comprobar_fuentes.py [--json] [--raiz DIR]
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
sys.path.insert(0, os.path.join(RAIZ, "tooling"))

PLANTILLA = "kernel/operativo/plantillas/SOURCES.toml"

# ---------------------------------------------------------------------------
# T161 — el corpus no conserva la equivalencia proyecto = repositorio
#
# POR QUÉ ESTO NO ES UNA LISTA DE TRES FRASES. La versión anterior buscaba tres cadenas
# literales y con eso afirmaba que «el corpus no conserva la equivalencia». Tres literales
# no demuestran nada sobre un corpus de doscientos documentos: una reformulación de la
# misma idea —«el repositorio es la memoria del proyecto», «una tarea = una rama»— pasaba
# sin que nada lo dijera, y el validador quedaba verde por no mirar.
#
# QUÉ SE COMPRUEBA AHORA, y por qué es mantenible:
#
#   1. cada FORMULACIÓN retirada se declara una vez, con su PATRÓN, la enmienda que la
#      retiró y los ficheros donde sí puede citarse porque declaran su derogación;
#   2. cada formulación trae un FIXTURE POSITIVO —un texto que DEBE detectar— y un
#      CONTRAEJEMPLO —un texto parecido que NO debe detectar—. La prueba se comprueba a sí
#      misma antes de recorrer el corpus: un patrón que ha dejado de detectar su propia
#      formulación es un fallo, y un patrón que dispara contra la formulación VIGENTE
#      también. Añadir una formulación obliga a escribir las dos;
#   3. se declara y se comprueba la COBERTURA: cuántos ficheros se recorrieron. Un
#      validador que pasa porque no leyó nada es el modo de fallo que esto evita.
#
# LO QUE ESTO NO ES. No es un buscador de la palabra «repositorio». El corpus habla de
# repositorios Git concretos, del repositorio de control, de una fuente y del conjunto de
# fuentes necesarias, y las cuatro cosas son legítimas. Lo que se persigue es la
# EQUIVALENCIA retirada, no la palabra.

# Ficheros que pueden citar CUALQUIER formulación retirada, y por qué.
CITAN_LO_DEROGADO = [
    # Los dos documentos del Owner: material normativo escrito en su voz, no corpus
    # operativo. Reescribirlos sería reescribir la orden.
    "ADS-ARQUITECTURA-MULTIREPO-APROBADA.md",
    "ADS-IDEAS-PENDIENTES-MULTIREPO.md",
    # La enmienda existe para citar lo que deroga.
    "docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md",
    # (a) y (b) permanecen íntegras: E2 las enmienda por sustitución explícita.
    "docs/rediseno/a-CAPACIDADES-APROBADA.md",
    "docs/rediseno/b-RECORRIDO-APROBADA.md",
    # El registro de la decisión y el contraste que la originó citan el modelo anterior
    # para explicar por qué se retiró.
    "docs/evolucion/07-DECISION-MULTIREPO.md",
    "docs/evolucion/06-CONTRASTE.md",
    "docs/evolucion/01-BASELINE-ADS.md",
    "docs/evolucion/02-MAPA-DIRECTIVA.md",
    "docs/evolucion/CHECKPOINT-ADS-NEXT.md",
    # El changelog dice qué cambió, y para eso tiene que nombrar lo anterior.
    "kernel/KERNEL_CHANGELOG.md",
    # Este fichero DECLARA las formulaciones: es la lista, no una infracción.
    "kernel/operativo/validadores/comprobar_fuentes.py",
    # El escenario de T161 enuncia qué formulaciones busca.
    "kernel/operativo/pruebas/T159-T170-multirepo.md",
]

# Directorios cuyo contenido es SALIDA, no corpus: citan lo que los validadores imprimen.
PREFIJOS_EXENTOS = ("kernel/operativo/pruebas/evidencia/",)

RETIRADAS = [
    {
        "id": "R1-estado-es-el-repo",
        "patron": r"el estado operativo (?:ES|es) los ficheros del repo\b",
        "por": "E2.1 — pasa a ser el repositorio ADS de control",
        "permitido_en": [],
        "fixture": "Requisito del Owner: el estado operativo ES los ficheros del repo, legibles.",
        "contraejemplo": "el estado operativo ES los ficheros del repositorio ADS de control",
    },
    {
        "id": "R2-adopcion-dentro-del-codigo",
        "patron": r"cd tu-proyecto-existente",
        "por": "E2.0 y §49 — la adopción ya no copia ADS dentro del repositorio de código",
        "permitido_en": [],
        "fixture": "cd tu-proyecto-existente && cp -r ads-kernel/kernel .",
        "contraejemplo": "cd ../mi-producto/ads",
    },
    {
        "id": "R3-tarea-igual-rama",
        "patron": r"\b(?:Una|una|Un|un) (?:tarea|item)\s*=\s*(?:una|1)\s*rama",
        "por": "E2.4 — item/paquete → 0..N source changes, uno por fuente",
        "permitido_en": ["kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md"],
        "fixture": "Una tarea = una rama corta, y un PR por tarea.",
        "contraejemplo": "Dentro de cada fuente: una rama corta por trabajo.",
    },
    {
        "id": "R4-item-una-rama-un-pr",
        "patron": r"un item\s*(?:→|->)\s*una rama\s*(?:→|->)\s*un PR",
        "por": "E2.4 — la relación universal queda derogada; C7 la conserva como cita",
        "permitido_en": ["kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md",
                         "kernel/KERNEL.md"],
        "fixture": "La relación es siempre un item → una rama → un PR.",
        "contraejemplo": "item/package → 0..N source changes, uno por fuente",
    },
    {
        "id": "R5-proyecto-es-un-repositorio",
        "patron": (r"(?:un |el |Un |El )?(?:ADS )?[Pp]ro(?:yecto|ject)(?: ADS)?"
                   r"\s+(?:es|ES)\s+(?:un|el)\s+repositorio"),
        "por": "E2.0 — PRODUCTO != REPOSITORIO GIT, ADS PROJECT != REPOSITORIO DE CÓDIGO",
        "permitido_en": [],
        "fixture": "Un ADS Project es un repositorio de código con el kernel dentro.",
        "contraejemplo": "Un ADS Project gobierna un PRODUCTO, no un repositorio.",
    },
    {
        "id": "R6-un-repo-un-proyecto",
        "patron": r"\b1\s*repo\s*=\s*1\s*(?:proyecto|componente)\b",
        "por": "E2.0 y C6 N7 — componente y fuente no tienen cardinalidad 1:1 obligatoria",
        "permitido_en": ["kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md"],
        "fixture": "El modelo asume 1 repo = 1 componente y no admite monorepo.",
        "contraejemplo": "MONOREPO   web → repo app, ruta apps/web",
    },
    {
        "id": "R7-repositorio-es-la-memoria",
        "patron": r"[Ee]l repositorio es la memoria del proyecto",
        "por": "E2.1 — la memoria es del repositorio ADS de CONTROL, no de «el repositorio»",
        "permitido_en": [],
        "fixture": "El chat es una interfaz temporal. El repositorio es la memoria del proyecto.",
        "contraejemplo": "El repositorio ADS de control es la memoria del proyecto.",
    },
    {
        "id": "R8-kernel-dentro-del-codigo",
        "patron": (r"(?:copia|copiar|instala|instalar|vive|viven)\w*\s+"
                   r"(?:el\s+)?(?:kernel|ADS)\s+dentro del repositorio de c[oó]digo"),
        "por": "E2.1 e I5 — kernel, packs y PROFILE viven una sola vez, en el control repo",
        "permitido_en": [],
        "fixture": "El arranque instala ADS dentro del repositorio de código del producto.",
        "contraejemplo": "ADS se instala en su propio repositorio de control, hermano del código.",
    },
    {
        "id": "R9-workspace-es-un-repositorio",
        "patron": r"[Ee]l workspace\s+(?:es|ES)\s+un repositorio",
        "por": "C6 topología — el workspace es el contenedor del producto y NO es un repo Git",
        "permitido_en": [],
        "fixture": "El workspace es un repositorio Git que contiene las fuentes.",
        "contraejemplo": "El workspace NO es un repositorio Git: es el contenedor del producto.",
    },
    {
        "id": "R10-una-rama-global-del-producto",
        "patron": r"(?<!No hay )(?<!no hay )una rama global del producto",
        "por": "E2.4 — el estado del producto no vive en ninguna rama: se calcula en el control repo",
        "permitido_en": [],
        "fixture": "La integración se hace fusionando una rama global del producto.",
        "contraejemplo": "No hay una rama global del producto, ni un PR global.",
    },
]

# Cobertura mínima esperada del recorrido. No es una cifra decorativa: si una exclusión
# mal escrita dejara el corpus fuera, el validador pasaría por no leer nada, que es
# exactamente el modo de fallo que T161 existe para no repetir.
COBERTURA_MINIMA = 150


def _compilados():
    import re as _re
    return [(e, _re.compile(e["patron"])) for e in RETIRADAS]



def _analizar(ruta_manifiesto, raiz):
    """Devuelve (manifiesto, hallazgos) usando el analizador único de workspace.py."""
    import workspace as ws  # noqa: E402

    ads_root = os.path.dirname(ruta_manifiesto)
    workspace_root = os.path.dirname(ads_root)
    hallazgos = []
    m = ws.leer_manifiesto(ads_root, workspace_root, hallazgos)
    errores = [h for h in hallazgos if h.nivel == ws.ERROR]
    return m, errores


def t159_plantilla_valida(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T159", "La plantilla de SOURCES.toml es válida y arranca sin fuentes")
    ruta = os.path.join(base, PLANTILLA)
    if not os.path.exists(ruta):
        r.fallo(f"no existe {PLANTILLA}: sin plantilla, cada proyecto inventa su manifiesto")
        return r
    m, errores = _analizar(ruta, base)
    for e in errores:
        r.fallo(f"{PLANTILLA}: {e.ambito}: {e.mensaje}")
    if m is None:
        return r
    if m.sources:
        r.fallo(f"{PLANTILLA} declara {len(m.sources)} fuentes. La plantilla arranca VACÍA: "
                f"un producto nuevo todavía no tiene código, y el Circuito 0 decide su "
                f"arquitectura física")
    return r


def t160_manifiesto_del_proyecto(raiz=None):
    """Si este repositorio ES un ADS Project, su manifiesto tiene que ser válido.

    El repositorio del kernel NO lo es: es el upstream, no el control repo de ningún
    producto. Que no tenga SOURCES.toml es correcto y la prueba lo dice en vez de
    inventarse un fallo.
    """
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T160", "El manifiesto del ADS Project, cuando existe, es válido")
    ruta = os.path.join(base, "SOURCES.toml")
    if not os.path.exists(ruta):
        # Correcto para el repositorio del kernel: es el upstream, no el control repo de
        # ningún producto. La prueba se supera POR AUSENCIA JUSTIFICADA — y lo dice en la
        # evidencia, porque una prueba que pasa por no tener nada que comprobar y no lo
        # declara es indistinguible de una que comprueba algo.
        # La ruta ABSOLUTA no entra en la evidencia: cambia con la máquina, y la regla del
        # repositorio es que los artefactos generados sean deterministas.
        r.detalle = ("ausencia justificada: no hay SOURCES.toml en la raíz analizada, luego "
                     "no es el control repo de ningún producto. NADA se ha validado aquí")
        return r
    r.detalle = "validado el SOURCES.toml de la raíz analizada"
    m, errores = _analizar(ruta, base)
    for e in errores:
        r.fallo(f"SOURCES.toml: {e.ambito}: {e.mensaje}")
    return r


def corpus_recorrido(raiz=None):
    """Genera `(rel, texto)` de cada fichero que T161 recorre.

    **Definición ÚNICA del recorrido.** La reutiliza `comprobar_evidencia` para comprobar
    que la cobertura publicada describe el corpus vigente y no uno anterior. Dos
    implementaciones del mismo recorrido derivan, y cuando derivan la que miente es siempre
    la que nadie mira — que es el hallazgo A-04 aplicado a otra materia.

    Un fichero ilegible NO cuenta: se salta igual aquí que en T161, porque la cifra que se
    publica es «cuántos se recorrieron de verdad», no «cuántos hay».
    """
    base = os.path.abspath(raiz or RAIZ)
    import ads_lint  # noqa: E402
    lint = ads_lint.Lint(base, [])
    lint.cargar_exclusiones()
    for ruta in lint.ficheros_texto((".md", ".sh", ".py", ".yaml", ".toml")):
        rel = os.path.relpath(ruta, base).replace(os.sep, "/")
        if rel.startswith(PREFIJOS_EXENTOS):
            continue
        try:
            with open(ruta, encoding="utf-8") as fh:
                texto = fh.read()
        except (OSError, UnicodeDecodeError):
            continue
        yield rel, texto


def ficheros_recorridos(raiz=None):
    """Cuántos ficheros recorre T161 sobre el corpus vigente.

    Es el valor que T161 publica en su cobertura, y el que `comprobar_evidencia` recalcula
    para detectar una evidencia caducada. Determinista: sólo depende del corpus.
    """
    return sum(1 for _ in corpus_recorrido(raiz))


def t161_sin_restos_del_modelo_anterior(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T161", "El corpus no conserva la equivalencia proyecto = repositorio")

    entradas = _compilados()

    # 1 · la prueba se comprueba a sí misma ANTES de mirar el corpus
    ids = [e["id"] for e in RETIRADAS]
    for repetido in sorted({i for i in ids if ids.count(i) > 1}):
        r.fallo(f"la formulación '{repetido}' está declarada dos veces")
    for entrada, patron in entradas:
        if not patron.search(entrada["fixture"]):
            r.fallo(f"{entrada['id']}: su patrón ya no detecta su propia formulación "
                    f"retirada. El fixture es «{entrada['fixture']}»")
        if patron.search(entrada["contraejemplo"]):
            r.fallo(f"{entrada['id']}: su patrón dispara contra la formulación VIGENTE "
                    f"«{entrada['contraejemplo']}». Un patrón que acusa a lo correcto se "
                    f"desactiva a la primera y deja de proteger")

    # 2 · el recorrido del corpus, por su definición única
    exentos_globales = {os.path.normpath(p) for p in CITAN_LO_DEROGADO}
    revisados = 0
    for rel, texto in corpus_recorrido(base):
        revisados += 1
        if os.path.normpath(rel) in exentos_globales:
            continue
        for entrada, patron in entradas:
            if os.path.normpath(rel) in {os.path.normpath(p) for p in entrada["permitido_en"]}:
                continue
            m = patron.search(texto)
            if m:
                linea = texto[:m.start()].count("\n") + 1
                r.fallo(f"{rel}:{linea}: conserva «{m.group(0)}» "
                        f"[{entrada['id']}], retirada por {entrada['por']}")

    # 3 · la cobertura se declara, y una cobertura insuficiente es un fallo
    # La cobertura se PUBLICA, no se supone. Sin esta línea, «el corpus está limpio» es
    # una afirmación sin alcance declarado.
    r.detalle = (f"{len(RETIRADAS)} formulaciones retiradas comprobadas con su fixture y "
                 f"su contraejemplo · {revisados} ficheros recorridos")
    if revisados < COBERTURA_MINIMA:
        r.fallo(f"sólo se recorrieron {revisados} ficheros, por debajo del mínimo "
                f"({COBERTURA_MINIMA}). Una exclusión mal escrita deja el corpus fuera y "
                f"esta prueba pasaría por no mirar")
    return r


PRUEBAS = [t159_plantilla_valida, t160_manifiesto_del_proyecto,
           t161_sin_restos_del_modelo_anterior]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz")
    args = ap.parse_args()
    resultados = [p(args.raiz) for p in PRUEBAS]
    if args.json:
        print(json.dumps([{"id": r.id, "nombre": r.nombre,
                           "estado": "prueba-superada" if r.superada else "prueba-fallida",
                           "cobertura": getattr(r, "detalle", ""),
                           "fallos": r.fallos} for r in resultados],
                         ensure_ascii=False, indent=2))
    else:
        for r in resultados:
            print(f"{r.id}  {'SUPERADA' if r.superada else 'FALLIDA '}  {r.nombre}")
            if getattr(r, "detalle", ""):
                print(f"          cobertura: {r.detalle}")
            for f in r.fallos:
                print(f"          · {f}")
        superadas = sum(1 for r in resultados if r.superada)
        print(f"\n{superadas} superadas · {len(resultados) - superadas} fallidas")
    return 1 if any(not r.superada for r in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
