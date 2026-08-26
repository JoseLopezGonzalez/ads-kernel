#!/usr/bin/env python3
"""comprobar_arranque — el arranque documentado FUNCIONA, no sólo está escrito.

Hallazgo A-02: `README.md` y `START_HERE.md` documentaban un comando que terminaba con
código 3 porque citaba packs retirados a `packs/legacy-1.3.0/`. Ninguna prueba lo cubría,
porque los sesenta y un escenarios auditaban el corpus y nadie ejecutaba el tooling.

Esto lo ejecuta de verdad, para CADA pack instalable:

  1. copia el repositorio a un directorio temporal del sistema
  2. crea un proyecto con ese pack, con el comando real
  3. comprueba la estructura resultante, fichero a fichero
  4. comprueba la composición: el pack pedido está, los otros NO, y no hay rastro de legacy
  5. ejecuta los validadores DENTRO del proyecto creado
  6. borra únicamente el temporal que creó
  7. sale con código cero si todo lo anterior se cumple

Además comprueba que los identificadores de pack citados en la documentación de arranque
existen de verdad, que es lo que fallaba.

Uso:
  python3 kernel/operativo/validadores/comprobar_arranque.py [--json] [--raiz DIR]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(__file__))
from comprobar_contratos import Resultado  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Ficheros que documentan el arranque y por tanto citan identificadores de pack.
DOCS_DE_ARRANQUE = ["README.md", "START_HERE.md"]

# Lo que un proyecto recién creado DEBE contener. Si esto cambia, la prueba tiene que
# cambiar con ello: es el contrato de lo que `new-project.sh` entrega.
ESTRUCTURA_MINIMA = [
    "PROFILE.md", "PROJECT.md", "BOOTSTRAP_PROMPT.md", "START_HERE.md",
    "kernel/VERSION", "kernel/KERNEL.md", "kernel/operativo/00-INDICE.md",
    "kernel/operativo/validadores/ads_lint.py",
    "kernel/templates/PROJECT_LEARNINGS.md",
    "docs/UPSTREAM.md", "docs/JOURNAL.md", "docs/PROJECT_LEARNINGS.md",
    "docs/agentic/ORG_LEARNINGS.md",
    "docs/rediseno/a-CAPACIDADES-APROBADA.md",
    "docs/rediseno/b-RECORRIDO-APROBADA.md",
    "docs/rediseno/a-ENMIENDA-E1-ENC.md",
    "tooling/new-project.sh", "tooling/kernel-status.sh",
    "packs/00-QUE-ES-UN-PACK.md", "packs/COMPOSICION.md",
]

VALIDADORES_EN_PROYECTO = ["ads_lint", "comprobar_contratos", "comprobar_packs"]


def packs_instalables(raiz):
    base = os.path.join(raiz, "packs")
    if not os.path.isdir(base):
        return []
    return sorted(n for n in os.listdir(base)
                  if not n.startswith("legacy-")
                  and os.path.isfile(os.path.join(base, n, "PACK.md")))


def _copiar(raiz, destino):
    def ignorar(_d, nombres):
        return [n for n in nombres if n in (".git", "__pycache__")]
    shutil.copytree(raiz, destino, ignore=ignorar, symlinks=True)


def t148_arranque(raiz=None):
    raiz = os.path.abspath(raiz or RAIZ)
    r = Resultado("T148", "El arranque documentado crea un proyecto conforme con cada pack")
    disponibles = packs_instalables(raiz)
    if not disponibles:
        r.fallo("no hay ningún pack instalable: packs/<nombre>/PACK.md no existe")
        return r

    # --- los identificadores citados en la documentación existen -------------
    citados = set()
    for doc in DOCS_DE_ARRANQUE:
        ruta = os.path.join(raiz, doc)
        if not os.path.exists(ruta):
            r.fallo(f"{doc}: no existe, y documenta el arranque")
            continue
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        # sólo las LÍNEAS DE ORDEN completas, no las menciones en prosa
        for linea in texto.splitlines():
            m = re.match(r"\s*(?:\$\s*)?\./tooling/new-project\.sh\s+(\S+)(?:\s+(\S+))?\s*$",
                         linea)
            if m and m.group(2):
                citados.update(p for p in m.group(2).split(",") if p)
    for p in sorted(citados):
        if p not in disponibles:
            r.fallo(f"la documentación de arranque cita el pack '{p}', que no es instalable. "
                    f"Instalables: {', '.join(disponibles)}")

    # --- el flujo real, un pack cada vez -------------------------------------
    tmp = tempfile.mkdtemp(prefix="ads-arranque-")
    try:
        for pack in disponibles:
            caja = os.path.join(tmp, pack)
            os.makedirs(caja)
            fuente = os.path.join(caja, "ads-kernel")
            _copiar(raiz, fuente)
            nombre = f"proyecto-{pack}"
            proc = subprocess.run(["./tooling/new-project.sh", nombre, pack],
                                  cwd=fuente, capture_output=True, text=True)
            if proc.returncode != 0:
                r.fallo(f"[{pack}] new-project.sh terminó con código {proc.returncode}: "
                        f"{(proc.stderr or proc.stdout).strip().splitlines()[:1]}")
                continue
            proyecto = os.path.join(caja, nombre)
            if not os.path.isdir(proyecto):
                r.fallo(f"[{pack}] el proyecto no se creó en {proyecto}")
                continue

            # 3 · estructura
            for rel in ESTRUCTURA_MINIMA:
                if not os.path.exists(os.path.join(proyecto, rel)):
                    r.fallo(f"[{pack}] falta en el proyecto creado: {rel}")

            # 4 · composición
            if not os.path.isfile(os.path.join(proyecto, "packs", pack, "PACK.md")):
                r.fallo(f"[{pack}] el pack pedido no quedó instalado")
            for otro in disponibles:
                if otro != pack and os.path.isdir(os.path.join(proyecto, "packs", otro)):
                    r.fallo(f"[{pack}] se instaló además '{otro}', que no se pidió")
            if os.path.exists(os.path.join(proyecto, "packs", "legacy-1.3.0")):
                r.fallo(f"[{pack}] el proyecto arrastra packs/legacy-1.3.0")
            for dirpath, _dn, fn in os.walk(proyecto):
                if "__pycache__" in dirpath:
                    r.fallo(f"[{pack}] el proyecto arrastra __pycache__")
                    break
                del fn

            # 5 · los validadores, DENTRO del proyecto creado
            for v in VALIDADORES_EN_PROYECTO:
                script = os.path.join(proyecto, "kernel/operativo/validadores", f"{v}.py")
                if not os.path.exists(script):
                    r.fallo(f"[{pack}] el proyecto no lleva {v}.py")
                    continue
                pv = subprocess.run([sys.executable, script], cwd=proyecto,
                                    capture_output=True, text=True)
                if pv.returncode != 0:
                    primeras = [ln for ln in pv.stdout.splitlines() if ln.strip()][:2]
                    r.fallo(f"[{pack}] {v} falla dentro del proyecto creado "
                            f"(exit {pv.returncode}): {primeras}")

        # --- el mensaje ante un identificador inexistente es útil ------------
        caja = os.path.join(tmp, "_inexistente")
        os.makedirs(caja)
        fuente = os.path.join(caja, "ads-kernel")
        _copiar(raiz, fuente)
        proc = subprocess.run(["./tooling/new-project.sh", "proyecto-x", "pack-inventado"],
                              cwd=fuente, capture_output=True, text=True)
        salida = (proc.stdout + proc.stderr)
        if proc.returncode == 0:
            r.fallo("un identificador de pack inexistente NO hizo fallar el arranque")
        if "pack-inventado" not in salida:
            r.fallo("el error no nombra el identificador que el usuario escribió")
        if not all(p in salida for p in disponibles):
            r.fallo("el error no lista los packs instalables")
        if os.path.exists(os.path.join(caja, "proyecto-x")):
            r.fallo("un arranque fallido dejó un proyecto a medio crear")
    finally:
        # 6 · sólo el temporal que hemos creado nosotros
        shutil.rmtree(tmp, ignore_errors=True)
    return r


PRUEBAS = [t148_arranque]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None)
    args = ap.parse_args()
    resultados = [f(args.raiz) for f in PRUEBAS]
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
