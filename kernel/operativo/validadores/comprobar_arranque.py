#!/usr/bin/env python3
"""comprobar_arranque — el arranque documentado FUNCIONA, no sólo está escrito.

Hallazgo A-02: `README.md` y `START_HERE.md` documentaban un comando que terminaba con
código 3 porque citaba packs retirados a `packs/legacy-1.3.0/`. Ninguna prueba lo cubría,
porque los sesenta y un escenarios auditaban el corpus y nadie ejecutaba el tooling.

Esto lo ejecuta de verdad, para CADA pack instalable:

  1. copia el repositorio a un directorio temporal del sistema
  2. crea un proyecto con ese pack —y con la COMBINACIÓN que el checkpoint documenta como
     siguiente comando real—, con el comando real
  2b. comprueba la TOPOLOGÍA: <workspace>/ads es el control repo, y el workspace NO es
     un repositorio Git —ni él ni ninguno de sus antecesores hasta el temporal—. Un ADS
     Project gobierna un producto, no un repositorio (C6)
  2c. comprueba la RAMA INICIAL y su coherencia con el comando documentado. Se ejecuta con
     la configuración global de Git VACÍA, que es donde el defecto aparece: `git init` sin
     `-b` tomaba `master` de `init.defaultBranch` mientras el script y START_HERE.md
     documentaban `git push -u origin main`
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
    "SOURCES.toml",
    "PROFILE.md", "PROJECT.md", "BOOTSTRAP_PROMPT.md", "START_HERE.md",
    "kernel/VERSION", "kernel/KERNEL.md", "kernel/operativo/00-INDICE.md",
    "kernel/operativo/validadores/ads_lint.py",
    "kernel/templates/PROJECT_LEARNINGS.md",
    "docs/UPSTREAM.md", "docs/JOURNAL.md", "docs/PROJECT_LEARNINGS.md",
    "docs/agentic/ORG_LEARNINGS.md",
    "docs/rediseno/a-CAPACIDADES-APROBADA.md",
    "docs/rediseno/b-RECORRIDO-APROBADA.md",
    "docs/rediseno/g-ESTADO-DURABLE-APROBADA.md",
    "docs/rediseno/a-ENMIENDA-E1-ENC.md",
    "docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md",
    # `F5` aprobó la sección `(g)` y las enmiendas `E3`–`E6`, y la lista de copia de
    # `new-project.sh` no las llevaba (deuda `FD-3`). Ahora esa lista se DERIVA del árbol;
    # esto es lo que comprueba que la derivación entrega de verdad lo que debe viajar, y
    # no sólo que el `find` no explota.
    "docs/rediseno/a-ENMIENDA-E3-ARRANQUE-Y-POLITICA.md",
    "docs/rediseno/a-ENMIENDA-E4-COMPOSICION-DE-RUTAS.md",
    "docs/rediseno/a-ENMIENDA-E5-CORRECCIONES-EDITORIALES.md",
    "docs/rediseno/a-ENMIENDA-E6-REANUDACION.md",
    # El motor de estado durable de `F6` es kernel, y por tanto VIAJA al proyecto
    # instalado. Sin esta línea, el runtime podría quedarse en el repositorio del kernel
    # sin que nada lo delatara: un proyecto instalado sin motor no puede sostener el
    # estado durable que la sección `(g)` le exige.
    "kernel/operativo/runtime/estado/motor.py",
    "tooling/new-project.sh", "tooling/kernel-status.sh", "tooling/workspace.py",
    "packs/00-QUE-ES-UN-PACK.md", "packs/COMPOSICION.md",
]

VALIDADORES_EN_PROYECTO = ["ads_lint", "comprobar_contratos", "comprobar_packs"]

# El arranque se ejecuta con la configuración de Git NEUTRALIZADA. No es cosmética: el
# defecto de la rama inicial sólo aparece cuando `init.defaultBranch` no está puesto, que
# es el caso de una máquina recién configurada y el de casi toda CI. Con la configuración
# del que ejecuta las pruebas, la prueba pasaría por casualidad.
ENTORNO_GIT_LIMPIO = {
    **os.environ,
    "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull,
    "GIT_AUTHOR_NAME": "ads-arranque", "GIT_AUTHOR_EMAIL": "arranque@ads.local",
    "GIT_COMMITTER_NAME": "ads-arranque", "GIT_COMMITTER_EMAIL": "arranque@ads.local",
    # el arranque no necesita red, y aquí no la tiene: Git sólo admite transporte `file`
    "GIT_ALLOW_PROTOCOL": "file", "GIT_TERMINAL_PROMPT": "0",
}

# El comando de publicación, tal y como lo documentan el script y la guía de arranque.
# La rama que nombra tiene que ser la que `new-project.sh` crea de verdad.
PUSH_DOCUMENTADO = re.compile(r"git push -u origin (\S+)")


def _git(args, cwd):
    return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True,
                          env=ENTORNO_GIT_LIMPIO)


def _ramas_documentadas(raiz, r):
    """La rama que citan los documentos de arranque. Si citan dos distintas, ya hay fallo."""
    ramas = set()
    for doc in DOCS_DE_ARRANQUE:
        ruta = os.path.join(raiz, doc)
        if not os.path.exists(ruta):
            continue
        with open(ruta, encoding="utf-8") as fh:
            ramas.update(PUSH_DOCUMENTADO.findall(fh.read()))
    if len(ramas) > 1:
        r.fallo(f"la documentación de arranque publica sobre ramas distintas: "
                f"{sorted(ramas)}. Una sola es la correcta")
    return ramas


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


# Combinaciones que la documentación presenta como reales y que por tanto hay que
# ejecutar EXACTAMENTE. `packs/COMPOSICION.md` prevé tres; el checkpoint documenta
# `wear-os,mobile-app` como el siguiente comando del piloto, y probar cada pack por
# separado no demuestra que esa orden funcione.
COMBINACIONES = ["wear-os,mobile-app"]


def t148_arranque(raiz=None):
    raiz = os.path.abspath(raiz or RAIZ)
    r = Resultado("T148", "El arranque documentado crea un proyecto conforme, pack a pack y combinado")
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
    casos = list(disponibles) + [c for c in COMBINACIONES
                                 if all(p in disponibles for p in c.split(","))]
    for c in COMBINACIONES:
        faltan = [p for p in c.split(",") if p not in disponibles]
        if faltan:
            r.fallo(f"la combinación documentada '{c}' cita packs no instalables: {faltan}")

    documentadas = _ramas_documentadas(raiz, r)

    tmp = tempfile.mkdtemp(prefix="ads-arranque-")
    try:
        for caso in casos:
            pedidos = caso.split(",")
            pack = caso                      # etiqueta del caso, suelto o combinado
            caja = os.path.join(tmp, caso.replace(",", "+"))
            os.makedirs(caja)
            fuente = os.path.join(caja, "ads-kernel")
            _copiar(raiz, fuente)
            nombre = "proyecto-" + caso.replace(",", "-")
            proc = subprocess.run(["./tooling/new-project.sh", nombre, caso],
                                  cwd=fuente, capture_output=True, text=True,
                                  env=ENTORNO_GIT_LIMPIO)
            if proc.returncode != 0:
                r.fallo(f"[{pack}] new-project.sh terminó con código {proc.returncode}: "
                        f"{(proc.stderr or proc.stdout).strip().splitlines()[:1]}")
                continue
            workspace = os.path.join(caja, nombre)
            proyecto = os.path.join(workspace, "ads")
            if not os.path.isdir(proyecto):
                r.fallo(f"[{pack}] el control repo no se creó en {proyecto}")
                continue

            # 2b · topología: el workspace es un contenedor, no un repositorio
            if os.path.exists(os.path.join(workspace, ".git")):
                r.fallo(f"[{pack}] se ha inicializado Git en el propio workspace. Sólo "
                        f"ads/ y las fuentes son repositorios; si no, las fuentes quedarían "
                        f"anidadas dentro de otro repo")
            if not os.path.isdir(os.path.join(proyecto, ".git")):
                r.fallo(f"[{pack}] el control repo no tiene .git propio")
            # ...y tampoco lo es ningún antecesor hasta el temporal. Basta un `.git` más
            # arriba para que las fuentes queden dentro de otro repositorio sin que
            # `ls <workspace>` lo delate.
            subida = os.path.dirname(workspace)
            while subida.startswith(tmp):
                if os.path.exists(os.path.join(subida, ".git")):
                    r.fallo(f"[{pack}] hay un repositorio Git en '{subida}', por encima del "
                            f"workspace: las fuentes quedarían anidadas")
                    break
                padre = os.path.dirname(subida)
                if padre == subida:
                    break
                subida = padre
            # el workspace contiene el control repo y NADA más: un proyecto nuevo no
            # arranca con fuentes materializadas que nadie declaró
            if sorted(os.listdir(workspace)) != ["ads"]:
                r.fallo(f"[{pack}] el workspace no contiene sólo ads/: "
                        f"{sorted(os.listdir(workspace))}")

            # 2c · la rama inicial, y el comando que la documenta
            rama = _git(["rev-parse", "--abbrev-ref", "HEAD"], proyecto).stdout.strip()
            del_script = set(PUSH_DOCUMENTADO.findall(proc.stdout))
            esperadas = documentadas | del_script
            if not del_script:
                r.fallo(f"[{pack}] new-project.sh no imprime el comando de publicación: "
                        f"quien arranca no sabe sobre qué rama publicar")
            if not rama:
                r.fallo(f"[{pack}] el control repo no tiene rama: `git init` no dejó HEAD "
                        f"apuntando a ninguna")
            elif len(esperadas) != 1 or rama not in esperadas:
                r.fallo(f"[{pack}] el control repo nació en la rama '{rama}' y lo "
                        f"documentado es {sorted(esperadas)}. Se documenta una rama y se "
                        f"crea otra: `git init` sin `-b` toma `init.defaultBranch`, que "
                        f"con la configuración global vacía es 'master'")
            # y esa rama tiene un commit de verdad, no un HEAD simbólico sin nada detrás
            if _git(["rev-parse", "--verify", "HEAD"], proyecto).returncode != 0:
                r.fallo(f"[{pack}] el control repo no tiene commit inicial")

            # 3 · estructura
            for rel in ESTRUCTURA_MINIMA:
                if not os.path.exists(os.path.join(proyecto, rel)):
                    r.fallo(f"[{pack}] falta en el proyecto creado: {rel}")

            # 4 · composición: están TODOS los pedidos y NINGUNO de los no pedidos
            for p in pedidos:
                if not os.path.isfile(os.path.join(proyecto, "packs", p, "PACK.md")):
                    r.fallo(f"[{pack}] el pack pedido '{p}' no quedó instalado")
            for otro in disponibles:
                if otro not in pedidos and os.path.isdir(os.path.join(proyecto, "packs", otro)):
                    r.fallo(f"[{pack}] se instaló además '{otro}', que no se pidió")
            if os.path.exists(os.path.join(proyecto, "packs", "legacy-1.3.0")):
                r.fallo(f"[{pack}] el proyecto arrastra packs/legacy-1.3.0")
            for dirpath, _dn, fn in os.walk(proyecto):
                if "__pycache__" in dirpath:
                    r.fallo(f"[{pack}] el proyecto arrastra __pycache__")
                    break
                del fn

            # 4b · con DOS packs: la composición tiene que ser computable, y ningún
            #      fichero puede haberse sobrescrito en silencio al instalar el segundo
            if len(pedidos) > 1:
                comunes = ["packs/00-QUE-ES-UN-PACK.md", "packs/COMPOSICION.md"]
                for rel in comunes:
                    if not os.path.isfile(os.path.join(proyecto, rel)):
                        r.fallo(f"[{pack}] falta {rel}, que la composición necesita")
                # ningún fichero de un pack pisa al de otro: sus árboles son disjuntos
                por_pack = {}
                for p in pedidos:
                    base_p = os.path.join(proyecto, "packs", p)
                    por_pack[p] = {os.path.relpath(os.path.join(d, f), base_p)
                                   for d, _sd, fs in os.walk(base_p) for f in fs}
                for i, a in enumerate(pedidos):
                    for b_ in pedidos[i + 1:]:
                        # comparten NOMBRES relativos por diseño (PACK.md, gates/gates.md);
                        # lo que no puede ocurrir es que compartan RUTA dentro de packs/
                        rutas_a = {os.path.join("packs", a, x) for x in por_pack[a]}
                        rutas_b = {os.path.join("packs", b_, x) for x in por_pack[b_]}
                        if rutas_a & rutas_b:
                            r.fallo(f"[{pack}] '{a}' y '{b_}' comparten ruta: "
                                    f"{sorted(rutas_a & rutas_b)[:3]}")
                # la resolución de P1 se computa, y declara qué queda para el PROFILE
                res = subprocess.run(
                    [sys.executable, "kernel/operativo/validadores/composicion_packs.py"],
                    cwd=proyecto, capture_output=True, text=True)
                if res.returncode != 0:
                    r.fallo(f"[{pack}] la composición no es computable "
                            f"(exit {res.returncode}): {res.stderr.strip()[:160]}")
                else:
                    salida = res.stdout
                    for p in pedidos:
                        if p not in salida:
                            r.fallo(f"[{pack}] la resolución no menciona el pack '{p}'")
                    if "PENDIENTE DE PROFILE" not in salida:
                        r.fallo(f"[{pack}] la resolución no declara qué queda pendiente de "
                                f"que lo fije el PROFILE")
                    if "gana" not in salida:
                        r.fallo(f"[{pack}] la resolución no declara qué valor gana ni de "
                                f"qué pack procede")

            # 4c · el manifiesto del proyecto recién creado valida, y arranca sin fuentes
            pw = subprocess.run([sys.executable, "tooling/workspace.py", "check", "--json"],
                                cwd=proyecto, capture_output=True, text=True)
            if pw.returncode != 0:
                r.fallo(f"[{pack}] workspace check falla en el proyecto creado "
                        f"(exit {pw.returncode}): {pw.stdout.strip()[:200]}")
            else:
                try:
                    datos = json.loads(pw.stdout)
                except json.JSONDecodeError:
                    r.fallo(f"[{pack}] workspace check --json no devolvió JSON")
                else:
                    if datos.get("sources"):
                        r.fallo(f"[{pack}] el proyecto nuevo arranca con fuentes declaradas; "
                                f"debe arrancar vacío")
                    if os.path.normpath(datos.get("workspace_root", "")) != os.path.normpath(workspace):
                        r.fallo(f"[{pack}] workspace_root mal resuelto: "
                                f"{datos.get('workspace_root')} != {workspace}")

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
                              cwd=fuente, capture_output=True, text=True,
                              env=ENTORNO_GIT_LIMPIO)
        salida = (proc.stdout + proc.stderr)
        if proc.returncode == 0:
            r.fallo("un identificador de pack inexistente NO hizo fallar el arranque")
        if "pack-inventado" not in salida:
            r.fallo("el error no nombra el identificador que el usuario escribió")
        if not all(p in salida for p in disponibles):
            r.fallo("el error no lista los packs instalables")
        if os.path.exists(os.path.join(caja, "proyecto-x")):
            r.fallo("un arranque fallido dejó un workspace a medio crear")
    finally:
        # 6 · sólo el temporal que hemos creado nosotros
        shutil.rmtree(tmp, ignore_errors=True)
    return r



# ---------------------------------------------------------------------------
# T171 — los diez criterios de descubrimiento del §100
#
# QUÉ DEMUESTRA ESTO, Y QUÉ NO. El §100 pide que un agente que sólo abra `workspace/ads`
# pueda DESCUBRIR diez cosas sin información oral adicional. Eso, literalmente, exige un
# agente y un piloto. Lo que sí puede comprobarse sin ninguno de los dos es la condición
# NECESARIA: que cada una de las diez tenga un sitio declarado donde leerse, dentro del
# proyecto recién creado, y que ese sitio exista y lo diga.
#
# Es COBERTURA ESTRUCTURAL, no la demostración del §100. La entrega anterior afirmó «los
# diez criterios del §100 demostrados» sin ninguna de las dos cosas; esta prueba entrega la
# primera y deja escrito que la segunda sigue pendiente de piloto.
# ---------------------------------------------------------------------------
DESCUBRIMIENTO_100 = [
    {"n": 1, "pregunta": "que está ante un ADS control repo",
     "en": ["BOOTSTRAP_PROMPT.md", "PROJECT.md"],
     "anclas": ["repositorio ADS de CONTROL", "control plane versionado"]},
    {"n": 2, "pregunta": "cuál es el producto",
     "en": ["PROJECT.md", "PROFILE.md"],
     "anclas": ["# PROJECT", "# PROFILE"]},
    {"n": 3, "pregunta": "qué sources existen",
     "en": ["SOURCES.toml", "BOOTSTRAP_PROMPT.md"],
     "anclas": ["[[sources]]", "SOURCES.toml"]},
    {"n": 4, "pregunta": "dónde deberían estar localmente",
     "en": ["SOURCES.toml", "BOOTSTRAP_PROMPT.md"],
     "anclas": ["ruta relativa al workspace", "hermanos de éste dentro del workspace"]},
    {"n": 5, "pregunta": "cómo comprobarlas",
     "en": ["BOOTSTRAP_PROMPT.md", "PROJECT.md", "START_HERE.md"],
     "anclas": ["workspace.py status", "workspace.py check"]},
    {"n": 6, "pregunta": "cómo materializar las ausentes",
     "en": ["BOOTSTRAP_PROMPT.md", "START_HERE.md"],
     "anclas": ["workspace.py init"]},
    {"n": 7, "pregunta": "qué componentes viven en ellas",
     "en": ["SOURCES.toml"],
     "anclas": ["[[components]]"]},
    {"n": 8, "pregunta": "dónde vive la documentación global",
     "en": ["BOOTSTRAP_PROMPT.md", "PROJECT.md"],
     "anclas": ["Una verdad vive en un sitio, y ese sitio es este repositorio",
                "No contiene el código"]},
    {"n": 9, "pregunta": "que no debe copiar ADS en las sources",
     "en": ["BOOTSTRAP_PROMPT.md"],
     "anclas": ["NO copies el PROFILE, el estado, la memoria, los ADR globales, el kernel "
                "ni los packs\n    dentro de una fuente"]},
    {"n": 10, "pregunta": "que un cambio puede afectar varias sources",
     "en": ["BOOTSTRAP_PROMPT.md", "kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md"],
     "anclas": ["0..N source changes", "por fuente"]},
]


def t171_descubrimiento(raiz=None):
    raiz = os.path.abspath(raiz or RAIZ)
    r = Resultado("T171",
                  "El proyecto recién creado declara dónde se lee cada criterio del §100")
    disponibles = packs_instalables(raiz)
    tmp = tempfile.mkdtemp(prefix="ads-descubrimiento-")
    try:
        fuente = os.path.join(tmp, "ads-kernel")
        _copiar(raiz, fuente)
        pack = disponibles[0] if disponibles else ""
        orden = ["./tooling/new-project.sh", "descubrimiento"] + ([pack] if pack else [])
        proc = subprocess.run(orden, cwd=fuente, capture_output=True, text=True,
                              env=ENTORNO_GIT_LIMPIO)
        if proc.returncode != 0:
            r.fallo(f"new-project.sh terminó con código {proc.returncode}")
            return r
        proyecto = os.path.join(tmp, "descubrimiento", "ads")

        vistos = set()
        for criterio in DESCUBRIMIENTO_100:
            vistos.add(criterio["n"])
            textos = []
            for rel in criterio["en"]:
                ruta = os.path.join(proyecto, rel)
                if not os.path.isfile(ruta):
                    r.fallo(f"§100.{criterio['n']} ({criterio['pregunta']}): el proyecto "
                            f"creado no lleva {rel}, que es donde debería leerse")
                    continue
                with open(ruta, encoding="utf-8") as fh:
                    textos.append(fh.read())
            if textos and not any(a in t for a in criterio["anclas"] for t in textos):
                r.fallo(f"§100.{criterio['n']} ({criterio['pregunta']}): ninguno de "
                        f"{criterio['en']} lo dice. Anclas buscadas: {criterio['anclas']}")
        faltan = sorted(set(range(1, 11)) - vistos)
        if faltan:
            r.fallo(f"la tabla de descubrimiento no cubre los criterios {faltan} del §100")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    r.detalle = ("cobertura ESTRUCTURAL de los diez criterios del §100: cada uno tiene un "
                 "sitio declarado donde leerse en el proyecto recién creado. NO demuestra "
                 "que un agente lo descubra: eso exige piloto (limitación abierta)")
    return r


def t194_actualizacion(raiz=None):
    """T194 — ACTUALIZAR un control repo que ya existe, sin perder lo que el proyecto tiene.

    QUÉ COMPRUEBA, y por qué no lo cubría `T148`. `T148` mide la INSTALACIÓN: un proyecto
    nuevo, creado desde cero. La otra mitad del ciclo —traer una versión más nueva del
    kernel a un control repo que ya está en uso— no la medía nadie, y es la que puede
    destruir trabajo: el kernel vendorizado se sustituye, pero `PROFILE.md`, `PROJECT.md`,
    `SOURCES.toml`, `docs/` y el ESTADO DURABLE del producto son del proyecto y NO se tocan.

    Se ejecuta de verdad: se crea el proyecto, se le mete estado durable y contenido propio,
    se simula que su kernel es viejo, se actualiza copiando el kernel y el tooling del
    origen, y se comprueba que (a) lo del proyecto sigue intacto, (b) el kernel quedó al
    día, (c) la huella del proyecto se reancla a su nuevo contenido y (d) los validadores
    siguen en verde DENTRO del proyecto actualizado.
    """
    raiz = os.path.abspath(raiz or RAIZ)
    r = Resultado("T194", "Un control repo existente se actualiza sin perder lo suyo")
    disponibles = packs_instalables(raiz)
    tmp = tempfile.mkdtemp(prefix="ads-actualizacion-")
    try:
        fuente = os.path.join(tmp, "ads-kernel")
        _copiar(raiz, fuente)
        pack = disponibles[0] if disponibles else ""
        orden = ["./tooling/new-project.sh", "proyecto"] + ([pack] if pack else [])
        proc = subprocess.run(orden, cwd=fuente, capture_output=True, text=True,
                              env=ENTORNO_GIT_LIMPIO)
        if proc.returncode != 0:
            r.fallo(f"no se pudo crear el proyecto de partida: {proc.returncode}")
            return r
        proyecto = os.path.join(tmp, "proyecto", "ads")

        # 1 · el proyecto adquiere COSAS SUYAS: perfil, estado durable y un documento
        propio = os.path.join(proyecto, "PROFILE.md")
        with open(propio, "a", encoding="utf-8") as fh:
            fh.write("\n## Particularidad del producto\n\nesto es del proyecto\n")
        with open(propio, "rb") as fh:
            perfil_antes = fh.read()
        cli_estado = os.path.join(proyecto, "kernel", "operativo", "runtime", "ads_estado.py")
        if not os.path.exists(cli_estado):
            r.fallo("el proyecto instalado no lleva el motor de estado durable")
            return r
        pe = subprocess.run([sys.executable, cli_estado, "--repo", proyecto, "inicializar"],
                            capture_output=True, text=True, env=ENTORNO_GIT_LIMPIO)
        if pe.returncode != 0:
            r.fallo(f"el motor no pudo fundar el estado en el proyecto: {pe.stderr.strip()[:160]}")
            return r
        with open(os.path.join(proyecto, "estado", "REVISION.json"), "rb") as fh:
            revision_antes = fh.read()

        # 2 · su kernel se queda ATRÁS: se le quita una pieza y se le ensucia otra
        retirado = os.path.join(proyecto, "kernel", "operativo", "runtime",
                                "CONTRATO-ADMISION.md")
        if os.path.exists(retirado):
            os.remove(retirado)
        with open(os.path.join(proyecto, "kernel", "VERSION"), "w", encoding="utf-8") as fh:
            fh.write("0.0.0-viejo\n")

        # 3 · ACTUALIZACIÓN: el kernel y el tooling se sustituyen; lo del proyecto, no
        shutil.rmtree(os.path.join(proyecto, "kernel", "operativo"))
        shutil.copytree(os.path.join(fuente, "kernel", "operativo"),
                        os.path.join(proyecto, "kernel", "operativo"),
                        ignore=shutil.ignore_patterns("__pycache__"))
        for nombre in sorted(os.listdir(os.path.join(fuente, "kernel"))):
            origen = os.path.join(fuente, "kernel", nombre)
            if os.path.isfile(origen) and nombre != ".upstream-hash":
                shutil.copy2(origen, os.path.join(proyecto, "kernel", nombre))
        for nombre in sorted(os.listdir(os.path.join(fuente, "tooling"))):
            origen = os.path.join(fuente, "tooling", nombre)
            if os.path.isfile(origen):
                shutil.copy2(origen, os.path.join(proyecto, "tooling", nombre))
        os.remove(os.path.join(proyecto, "kernel", ".upstream-hash"))
        subprocess.run(["./tooling/kernel-status.sh"], cwd=proyecto, capture_output=True,
                       text=True, env=ENTORNO_GIT_LIMPIO)

        # 4 · lo del proyecto sigue intacto
        with open(propio, "rb") as fh:
            if fh.read() != perfil_antes:
                r.fallo("la actualización pisó el PROFILE del proyecto")
        with open(os.path.join(proyecto, "estado", "REVISION.json"), "rb") as fh:
            if fh.read() != revision_antes:
                r.fallo("la actualización tocó el ESTADO DURABLE del producto")
        # 5 · el kernel quedó al día
        if not os.path.exists(retirado):
            r.fallo("la actualización no repuso la pieza que faltaba del kernel")
        with open(os.path.join(proyecto, "kernel", "VERSION"), encoding="utf-8") as fh:
            if fh.read().strip() == "0.0.0-viejo":
                r.fallo("la actualización no sustituyó la versión vieja del kernel")
        # 6 · la huella se reancla al contenido nuevo, y queda LIMPIA
        estado_huella = subprocess.run(["./tooling/kernel-status.sh"], cwd=proyecto,
                                       capture_output=True, text=True,
                                       env=ENTORNO_GIT_LIMPIO)
        if "LIMPIO" not in estado_huella.stdout:
            r.fallo(f"la huella del proyecto actualizado no queda limpia: "
                    f"{estado_huella.stdout.strip().splitlines()[-1:]}")
        # 7 · los validadores siguen en verde DENTRO del proyecto actualizado
        for v in VALIDADORES_EN_PROYECTO:
            script = os.path.join(proyecto, "kernel/operativo/validadores", f"{v}.py")
            pv = subprocess.run([sys.executable, script], cwd=proyecto,
                                capture_output=True, text=True)
            if pv.returncode != 0:
                primeras = [ln for ln in pv.stdout.splitlines() if ln.strip()][:2]
                r.fallo(f"{v} falla en el proyecto ACTUALIZADO (exit {pv.returncode}): "
                        f"{primeras}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return r


PRUEBAS = [t148_arranque, t171_descubrimiento, t194_actualizacion]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None)
    args = ap.parse_args()
    resultados = [f(args.raiz) for f in PRUEBAS]
    if args.json:
        print(json.dumps([{"id": x.id, "nombre": x.nombre,
                           "estado": "prueba-superada" if x.superada else "prueba-fallida",
                           "alcance": getattr(x, "detalle", ""),
                           "fallos": x.fallos} for x in resultados], ensure_ascii=False, indent=2))
    else:
        for x in resultados:
            print(f"{x.id}  {'SUPERADA' if x.superada else 'FALLIDA '}  {x.nombre}")
            if getattr(x, "detalle", ""):
                print(f"          alcance: {x.detalle}")
            for f in x.fallos:
                print(f"          · {f}")
        fallidas = [x for x in resultados if not x.superada]
        print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if any(not x.superada for x in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
