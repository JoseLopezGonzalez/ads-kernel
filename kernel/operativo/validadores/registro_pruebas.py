#!/usr/bin/env python3
"""Regenera pruebas/REGISTRO-generado.md a partir de los bloques ads:escenario.

Determinista: mismo estado canónico produce bytes idénticos. Sin hora de pared,
sin telemetría (regla de determinismo de a.9).
"""
from __future__ import annotations

import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SALIDA = os.path.join(RAIZ, "kernel/operativo/pruebas/REGISTRO-generado.md")

ETIQUETA = {
    "contrato-definido": "CONTRATO DEFINIDO",
    "validador-implementado": "VALIDADOR IMPLEMENTADO",
    "prueba-ejecutada": "PRUEBA EJECUTADA",
    "prueba-superada": "PRUEBA SUPERADA",
    "prueba-fallida": "PRUEBA FALLIDA",
}


def clave(ident: str):
    m = re.match(r"^T(\d+)(?:\.(\d+))?$", ident)
    return (int(m.group(1)), int(m.group(2) or 0)) if m else (9999, 0)


def main() -> int:
    lint = Lint(RAIZ, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    escenarios = [(d, f) for t, d, f, _ in lint.bloques if t == "escenario"]
    escenarios.sort(key=lambda par: clave(par[0].get("id", "")))

    fuente = hashlib.sha256()
    for datos, ruta in escenarios:
        fuente.update(repr(sorted(datos.items())).encode("utf-8"))

    lineas = [
        "# REGISTRO DE PRUEBAS — generado",
        "",
        "<!-- GENERADO por validadores/registro_pruebas.py. No editar a mano. -->",
        f"<!-- source_revision: {fuente.hexdigest()[:16]} -->",
        "",
        "Fuente: los bloques `ads:escenario` de `kernel/operativo/` y `packs/`.",
        "Los cuatro estados y qué autoriza a decir cada uno: [`REGISTRO.md`](REGISTRO.md).",
        "",
    ]
    resumen = {}
    for datos, _ in escenarios:
        resumen[datos.get("estado", "?")] = resumen.get(datos.get("estado", "?"), 0) + 1
    lineas.append("## Recuento")
    lineas.append("")
    lineas.append("| estado | pruebas |")
    lineas.append("|---|---|")
    for estado in ["contrato-definido", "validador-implementado", "prueba-ejecutada",
                   "prueba-superada", "prueba-fallida"]:
        lineas.append(f"| {ETIQUETA[estado]} | {resumen.get(estado, 0)} |")
    lineas.append(f"| **total** | **{len(escenarios)}** |")
    lineas.append("")
    lineas.append("## Detalle")
    lineas.append("")
    lineas.append("| id | prueba | cubre | ejecución | estado | evidencia |")
    lineas.append("|---|---|---|---|---|---|")
    for datos, ruta in escenarios:
        rel = os.path.relpath(ruta, os.path.join(RAIZ, "kernel/operativo/pruebas"))
        cubre = " · ".join(datos.get("cubre", []))
        lineas.append(
            f"| [{datos.get('id')}]({rel}) | {datos.get('nombre','')} | {cubre} |"
            f" {datos.get('ejecucion','')} | **{ETIQUETA.get(datos.get('estado'), '?')}** |"
            f" {datos.get('evidencia') or '—'} |")
    lineas.append("")

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lineas))
    print(f"{len(escenarios)} escenarios · {SALIDA}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
