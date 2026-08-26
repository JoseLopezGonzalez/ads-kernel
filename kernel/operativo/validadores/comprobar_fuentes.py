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
import sys

sys.path.insert(0, os.path.dirname(__file__))
from comprobar_contratos import Resultado  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "tooling"))

PLANTILLA = "kernel/operativo/plantillas/SOURCES.toml"

# Formulaciones del modelo anterior —ADS Project = repositorio de código— que quedaron
# derogadas por la enmienda E2. Cada una lleva los ficheros donde SÍ puede aparecer,
# porque un texto que declara una derogación tiene que poder citar lo derogado.
RETIRADAS = [
    {
        "frase": "el estado operativo ES los ficheros del repo",
        "por": "E2.1 — pasa a ser el repositorio ADS de control",
        "permitido_en": ["docs/rediseno/a-CAPACIDADES-APROBADA.md",
                         "docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md"],
    },
    {
        "frase": "cd tu-proyecto-existente",
        "por": "E2.0 y §49 — la adopción ya no copia ADS dentro del repositorio de código",
        "permitido_en": [],
    },
    {
        "frase": "Una tarea = una rama corta",
        "por": "E2.4 — item/paquete → 0..N source changes, uno por fuente",
        "permitido_en": ["kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md"],
    },
]


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
        # correcto para el repositorio del kernel: es el upstream, no el control repo
        # de ningún producto. La prueba se supera por ausencia justificada.
        return r
    m, errores = _analizar(ruta, base)
    for e in errores:
        r.fallo(f"SOURCES.toml: {e.ambito}: {e.mensaje}")
    return r


def t161_sin_restos_del_modelo_anterior(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T161", "El corpus no conserva la equivalencia proyecto = repositorio")

    import ads_lint  # noqa: E402
    lint = ads_lint.Lint(base, [])
    lint.cargar_exclusiones()

    for entrada in RETIRADAS:
        frase = entrada["frase"]
        permitido = {os.path.normpath(p) for p in entrada["permitido_en"]}
        for ruta in lint.ficheros_texto((".md", ".sh", ".py", ".yaml", ".toml")):
            rel = os.path.relpath(ruta, base).replace(os.sep, "/")
            # Este fichero contiene las frases retiradas como DATO: es la lista que las
            # declara. Igual que comprobar_negativos con sus fixtures, se excluye a sí
            # mismo o se acusaría de la infracción que existe para detectar.
            if (rel == "kernel/operativo/validadores/comprobar_fuentes.py"
                    or rel.startswith("ADS-")
                    or rel.startswith("kernel/operativo/pruebas/evidencia/")):
                continue
            if os.path.normpath(rel) in permitido:
                continue
            try:
                with open(ruta, encoding="utf-8") as fh:
                    texto = fh.read()
            except (OSError, UnicodeDecodeError):
                continue
            if frase in texto:
                r.fallo(f"{rel}: conserva «{frase}», retirada por {entrada['por']}")
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
                           "fallos": r.fallos} for r in resultados],
                         ensure_ascii=False, indent=2))
    else:
        for r in resultados:
            print(f"{r.id}  {'SUPERADA' if r.superada else 'FALLIDA '}  {r.nombre}")
            for f in r.fallos:
                print(f"          · {f}")
        superadas = sum(1 for r in resultados if r.superada)
        print(f"\n{superadas} superadas · {len(resultados) - superadas} fallidas")
    return 1 if any(not r.superada for r in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
