#!/usr/bin/env python3
"""workspace — materializa y comprueba el workspace multi-fuente de un ADS Project.

Un ADS Project gobierna un PRODUCTO, no un repositorio. El producto puede estar repartido
entre varios repositorios Git independientes, declarados en `SOURCES.toml` en la raíz del
repositorio ADS de control. Contrato:
`kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md`.

    <workspace>/          NO es un repositorio Git. Es el contenedor del producto.
    ├── ads/              este repositorio: el CONTROL REPO
    ├── frontend/  .git/  fuentes, en la ruta que declara el manifiesto
    └── backend/   .git/

Órdenes:
    python3 tooling/workspace.py check   [--json]
    python3 tooling/workspace.py init    [ids...]  [--json]
    python3 tooling/workspace.py status  [--json]

Sin ids, `init` materializa todas las fuentes declaradas.

Sólo biblioteca estándar y Git por línea de órdenes. `SOURCES.toml` se lee con `tomllib`,
que es estándar desde Python 3.11: leer el manifiesto NO introduce ninguna dependencia.

Códigos de salida:  0 sin errores · 1 hay errores · 2 no se pudo empezar
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11
    tomllib = None

MANIFIESTO = "SOURCES.toml"
SCHEMAS_SOPORTADOS = {1}
LAYOUTS_SOPORTADOS = {"siblings"}
RUTA_RESERVADA = "ads"

ERROR, WARN, INFO = "ERROR", "WARN", "INFO"

# Credenciales embebidas en el remoto. El manifiesto declara IDENTIDAD, nunca secretos:
# la autenticación la aporta el entorno (agente SSH, gestor de credenciales, token).
CREDENCIAL_EN_URL = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://[^/@]*@")


class Hallazgo:
    def __init__(self, nivel, ambito, mensaje):
        self.nivel, self.ambito, self.mensaje = nivel, ambito, mensaje

    def __str__(self):
        return f"{self.nivel:5}  {self.ambito:<24} {self.mensaje}"

    def a_dict(self):
        return {"nivel": self.nivel, "ambito": self.ambito, "mensaje": self.mensaje}


# --------------------------------------------------------------------------- Git
def git(args, cwd=None):
    """Ejecuta git y devuelve (codigo, stdout, stderr). Nunca lanza."""
    try:
        p = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except FileNotFoundError:
        return 127, "", "git no está instalado o no está en PATH"


def es_repo_git(ruta):
    if not os.path.isdir(os.path.join(ruta, ".git")):
        # un worktree tiene .git como FICHERO, no como directorio
        if not os.path.isfile(os.path.join(ruta, ".git")):
            return False
    cod, salida, _ = git(["rev-parse", "--is-inside-work-tree"], cwd=ruta)
    return cod == 0 and salida == "true"


def normalizar_remoto(url):
    """Identidad comparable de un remoto Git.

    Reconoce como el MISMO repositorio las tres formas habituales:

        https://github.com/org/repo.git
        git@github.com:org/repo.git
        ssh://git@github.com/org/repo.git

    La comparación textual ingenua diría que son tres repositorios distintos, y el
    resultado sería que `check` rechaza un workspace correcto por haberlo clonado con
    SSH en vez de HTTPS. Ante lo que no sabe interpretar, devuelve la cadena tal cual y
    la comparación falla de forma SEGURA: prefiere avisar de más a aceptar de menos.
    """
    if not url:
        return ""
    u = url.strip().rstrip("/")
    # scp-like: git@host:org/repo.git
    m = re.match(r"^(?:([^@/]+)@)?([^:/]+):(?!//)(.+)$", u)
    if m and "://" not in u:
        host, ruta = m.group(2), m.group(3)
    else:
        m = re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://(?:[^@/]*@)?([^/:]+)(?::\d+)?/(.+)$", u)
        if not m:
            return u.lower()
        host, ruta = m.group(1), m.group(2)
    host = host.lower()
    if host.startswith("www."):
        host = host[4:]
    if ruta.endswith(".git"):
        ruta = ruta[:-4]
    return f"{host}/{ruta.strip('/').lower()}"


# --------------------------------------------------------------------------- raíces
def localizar_control_repo(desde=None):
    """Sube desde `desde` hasta encontrar el SOURCES.toml del repositorio de control.

    Permite ejecutar la orden desde cualquier subdirectorio del control repo, que es lo
    que hace un agente que está trabajando dentro de `docs/` o de `kernel/`.
    """
    actual = os.path.abspath(desde or os.getcwd())
    while True:
        if os.path.isfile(os.path.join(actual, MANIFIESTO)):
            return actual
        padre = os.path.dirname(actual)
        if padre == actual:
            return None
        actual = padre


def raices(desde=None):
    ads_root = localizar_control_repo(desde)
    if ads_root is None:
        return None, None
    return ads_root, os.path.dirname(ads_root)


# --------------------------------------------------------------------------- manifiesto
class Manifiesto:
    def __init__(self):
        self.schema = None
        self.layout = None
        self.sources = []
        self.components = []


def _ruta_segura(valor, base, campo, ambito, hallazgos):
    """Comprueba que `valor` es una ruta relativa que no escapa de `base`.

    Un manifiesto es contenido versionado que un agente puede modificar. Una ruta
    `../../otro-proyecto` convertiría `init` en una herramienta para escribir fuera del
    workspace, y eso no puede depender de que nadie la escriba.
    """
    if not isinstance(valor, str) or not valor.strip():
        hallazgos.append(Hallazgo(ERROR, ambito, f"{campo} vacío o no es texto"))
        return None
    if os.path.isabs(valor) or re.match(r"^[a-zA-Z]:[\\/]", valor):
        hallazgos.append(Hallazgo(ERROR, ambito, f"{campo} '{valor}' es una ruta absoluta"))
        return None
    destino = os.path.normpath(os.path.join(base, valor))
    base_n = os.path.normpath(base)
    if destino != base_n and not destino.startswith(base_n + os.sep):
        hallazgos.append(Hallazgo(
            ERROR, ambito, f"{campo} '{valor}' escapa de {base_n}"))
        return None
    return destino


def leer_manifiesto(ads_root, workspace_root, hallazgos):
    ruta = os.path.join(ads_root, MANIFIESTO)
    if tomllib is None:
        hallazgos.append(Hallazgo(ERROR, MANIFIESTO,
                                  "se requiere Python 3.11 o superior para leer TOML"))
        return None
    try:
        with open(ruta, "rb") as fh:
            datos = tomllib.load(fh)
    except OSError as e:
        hallazgos.append(Hallazgo(ERROR, MANIFIESTO, f"no se puede leer: {e}"))
        return None
    except tomllib.TOMLDecodeError as e:
        hallazgos.append(Hallazgo(ERROR, MANIFIESTO, f"TOML inválido: {e}"))
        return None

    m = Manifiesto()

    m.schema = datos.get("schema")
    if m.schema is None:
        hallazgos.append(Hallazgo(ERROR, "schema", "falta `schema`: sin él, el formato es ambiguo"))
    elif m.schema not in SCHEMAS_SOPORTADOS:
        hallazgos.append(Hallazgo(
            ERROR, "schema",
            f"schema {m.schema!r} no soportado (soportados: {sorted(SCHEMAS_SOPORTADOS)})"))

    ws = datos.get("workspace") or {}
    m.layout = ws.get("layout")
    if m.layout is None:
        hallazgos.append(Hallazgo(ERROR, "workspace", "falta `[workspace] layout`"))
    elif m.layout not in LAYOUTS_SOPORTADOS:
        hallazgos.append(Hallazgo(
            ERROR, "workspace",
            f"layout {m.layout!r} no soportado (soportados: {sorted(LAYOUTS_SOPORTADOS)})"))

    ids_vistos, rutas_vistas = {}, {}
    for i, s in enumerate(datos.get("sources") or []):
        ambito = f"sources[{i}]"
        sid = s.get("id")
        if not isinstance(sid, str) or not sid.strip():
            hallazgos.append(Hallazgo(ERROR, ambito, "falta `id`"))
            continue
        ambito = f"source:{sid}"
        if sid in ids_vistos:
            hallazgos.append(Hallazgo(ERROR, ambito, f"`id` duplicado: ya lo usa sources[{ids_vistos[sid]}]"))
            continue
        ids_vistos[sid] = i

        remoto = s.get("remote")
        if not isinstance(remoto, str) or not remoto.strip():
            hallazgos.append(Hallazgo(ERROR, ambito, "falta `remote`: la identidad de una fuente es su remoto"))
            remoto = ""
        elif CREDENCIAL_EN_URL.match(remoto):
            hallazgos.append(Hallazgo(
                ERROR, ambito,
                "`remote` embebe credenciales. El manifiesto declara identidad, nunca secretos"))

        ruta = s.get("path")
        destino = _ruta_segura(ruta, workspace_root, "path", ambito, hallazgos)
        if destino is None:
            continue
        if os.path.normpath(ruta) == RUTA_RESERVADA:
            hallazgos.append(Hallazgo(
                ERROR, ambito,
                f"`path` '{ruta}' está reservado para el repositorio ADS de control"))
            continue
        clave = os.path.normcase(destino)
        if clave in rutas_vistas:
            hallazgos.append(Hallazgo(
                ERROR, ambito, f"`path` '{ruta}' colisiona con la fuente '{rutas_vistas[clave]}'"))
            continue
        rutas_vistas[clave] = sid

        m.sources.append({"id": sid, "remote": remoto, "path": os.path.normpath(ruta),
                          "abs": destino})

    por_id = {s["id"]: s for s in m.sources}
    ids_comp = {}
    for i, c in enumerate(datos.get("components") or []):
        ambito = f"components[{i}]"
        cid = c.get("id")
        if not isinstance(cid, str) or not cid.strip():
            hallazgos.append(Hallazgo(ERROR, ambito, "falta `id`"))
            continue
        ambito = f"component:{cid}"
        if cid in ids_comp:
            hallazgos.append(Hallazgo(ERROR, ambito, "`id` de componente duplicado"))
            continue
        ids_comp[cid] = i

        src = c.get("source")
        if src not in por_id:
            hallazgos.append(Hallazgo(
                ERROR, ambito,
                f"referencia la fuente '{src}', que no está declarada en `sources`"))
            continue
        cpath = c.get("path", ".")
        # la ruta del componente se resuelve DENTRO de su fuente: un componente que
        # apunta fuera de su fuente no es un componente, es otra fuente sin declarar
        if _ruta_segura(cpath, por_id[src]["abs"], "path", ambito, hallazgos) is None:
            continue
        m.components.append({"id": cid, "source": src, "path": os.path.normpath(cpath),
                             "kind": c.get("kind")})
    return m


# --------------------------------------------------------------------------- estado
def estado_de_fuente(s):
    """Fotografía de una fuente en disco. No modifica nada."""
    e = {"id": s["id"], "path": s["path"], "remote": s["remote"], "present": False,
         "is_git": False, "branch": None, "head": None, "dirty": None,
         "remote_actual": None, "remote_ok": None}
    if not os.path.isdir(s["abs"]):
        return e
    e["present"] = True
    if not es_repo_git(s["abs"]):
        return e
    e["is_git"] = True
    cod, salida, _ = git(["rev-parse", "--abbrev-ref", "HEAD"], cwd=s["abs"])
    e["branch"] = salida if cod == 0 else None
    cod, salida, _ = git(["rev-parse", "--short", "HEAD"], cwd=s["abs"])
    e["head"] = salida if cod == 0 else None
    cod, salida, _ = git(["status", "--porcelain"], cwd=s["abs"])
    e["dirty"] = bool(salida) if cod == 0 else None
    cod, salida, _ = git(["remote", "get-url", "origin"], cwd=s["abs"])
    e["remote_actual"] = salida if cod == 0 else None
    if e["remote_actual"] and s["remote"]:
        e["remote_ok"] = normalizar_remoto(e["remote_actual"]) == normalizar_remoto(s["remote"])
    elif s["remote"]:
        e["remote_ok"] = False
    return e


def comprobar_disco(m, hallazgos, solo=None):
    estados = []
    for s in m.sources:
        if solo and s["id"] not in solo:
            continue
        e = estado_de_fuente(s)
        estados.append(e)
        amb = f"source:{s['id']}"
        if not e["present"]:
            hallazgos.append(Hallazgo(
                INFO, amb, f"no materializada en '{s['path']}' — `init {s['id']}` la clona"))
            continue
        if not e["is_git"]:
            hallazgos.append(Hallazgo(
                ERROR, amb,
                f"'{s['path']}' existe y NO es un repositorio Git. No se clona encima"))
            continue
        if e["remote_actual"] is None:
            hallazgos.append(Hallazgo(
                ERROR, amb, "el repositorio no tiene remoto `origin`: no puede demostrarse su identidad"))
        elif e["remote_ok"] is False:
            hallazgos.append(Hallazgo(
                ERROR, amb,
                f"identidad remota distinta de la declarada. Declarado '{s['remote']}', "
                f"encontrado '{e['remote_actual']}'. No se cambia el remoto automáticamente"))
        if e["dirty"]:
            hallazgos.append(Hallazgo(
                WARN, amb, "tiene cambios sin confirmar. No es un error, y no se tocan"))
    return estados


# --------------------------------------------------------------------------- órdenes
def orden_check(m, hallazgos):
    if m is not None and not m.sources:
        hallazgos.append(Hallazgo(
            INFO, "sources",
            "ninguna fuente declarada. Es válido: un producto nuevo aún no tiene código"))
    estados = comprobar_disco(m, hallazgos) if m else []
    return {"sources": estados}


def orden_init(m, hallazgos, pedidas):
    if m is None:
        return {"sources": []}
    conocidas = {s["id"] for s in m.sources}
    desconocidas = [i for i in pedidas if i not in conocidas]
    for i in desconocidas:
        hallazgos.append(Hallazgo(ERROR, f"source:{i}", "no está declarada en el manifiesto"))
    objetivo = [s for s in m.sources if not pedidas or s["id"] in pedidas]

    acciones = []
    for s in objetivo:
        amb = f"source:{s['id']}"
        e = estado_de_fuente(s)
        if e["present"]:
            if not e["is_git"]:
                hallazgos.append(Hallazgo(
                    ERROR, amb,
                    f"'{s['path']}' existe y no es un repositorio Git. "
                    f"No se borra, no se sobrescribe y no se clona encima"))
                acciones.append({"id": s["id"], "accion": "error-no-git"})
                continue
            if e["remote_ok"] is False:
                hallazgos.append(Hallazgo(
                    ERROR, amb,
                    f"'{s['path']}' es otro repositorio. Declarado '{s['remote']}', "
                    f"encontrado '{e['remote_actual']}'. No se cambia el remoto ni se reemplaza"))
                acciones.append({"id": s["id"], "accion": "error-otra-identidad"})
                continue
            # Reutilizar es la regla, no una optimización: volver a clonar sobre trabajo
            # local existente es la forma más rápida de perderlo.
            hallazgos.append(Hallazgo(INFO, amb, "ya materializada y correcta: se reutiliza"))
            acciones.append({"id": s["id"], "accion": "reutilizada"})
            continue

        if not s["remote"]:
            hallazgos.append(Hallazgo(ERROR, amb, "sin `remote` declarado: no hay de dónde clonar"))
            acciones.append({"id": s["id"], "accion": "error-sin-remoto"})
            continue
        padre = os.path.dirname(s["abs"])
        try:
            os.makedirs(padre, exist_ok=True)
        except OSError as ex:
            hallazgos.append(Hallazgo(ERROR, amb, f"no se puede crear '{padre}': {ex}"))
            acciones.append({"id": s["id"], "accion": "error-directorio"})
            continue
        cod, _, err = git(["clone", s["remote"], s["abs"]])
        if cod != 0:
            # el mensaje de git puede contener la URL; el remoto declarado no lleva
            # credenciales por contrato, y aun así no se vuelca stderr entero
            hallazgos.append(Hallazgo(
                ERROR, amb,
                f"clone falló desde '{s['remote']}' — {err.splitlines()[-1] if err else 'sin detalle'}"))
            acciones.append({"id": s["id"], "accion": "error-clone"})
            continue
        hallazgos.append(Hallazgo(INFO, amb, f"clonada en '{s['path']}'"))
        acciones.append({"id": s["id"], "accion": "clonada"})

    # `init` NO sincroniza: preparar un workspace y sincronizar un trabajo son
    # operaciones distintas, y confundirlas altera repos con trabajo local sin avisar.
    return {"sources": acciones}


def orden_status(m, hallazgos):
    estados = comprobar_disco(m, hallazgos) if m else []
    return {"sources": estados}


def imprimir_status(estados):
    if not estados:
        print("(ninguna fuente declarada)")
        return
    cab = f"{'SOURCE':<14}{'PATH':<14}{'PRESENT':<9}{'BRANCH':<18}{'HEAD':<10}{'DIRTY':<7}REMOTE"
    print(cab)
    for e in estados:
        presente = "yes" if e["present"] else "no"
        if e["present"] and not e["is_git"]:
            presente = "NO-GIT"
        remoto = "-" if not e["present"] else ("ok" if e["remote_ok"] else "MISMATCH")
        if e["present"] and e["is_git"] and e["remote_actual"] is None:
            remoto = "SIN-ORIGIN"
        print(f"{e['id']:<14}{e['path']:<14}{presente:<9}"
              f"{(e['branch'] or '-'):<18}{(e['head'] or '-'):<10}"
              f"{('yes' if e['dirty'] else 'no' if e['dirty'] is not None else '-'):<7}{remoto}")


def main():
    ap = argparse.ArgumentParser(description="workspace multi-fuente de un ADS Project")
    ap.add_argument("orden", choices=["check", "init", "status"])
    ap.add_argument("ids", nargs="*", help="fuentes concretas; sin ids, todas")
    ap.add_argument("--json", action="store_true", help="salida legible por máquina")
    ap.add_argument("--raiz", help="directorio desde el que localizar el control repo")
    args = ap.parse_args()

    ads_root, workspace_root = raices(args.raiz)
    if ads_root is None:
        msg = (f"no se encuentra {MANIFIESTO} ni aquí ni en ningún directorio superior. "
               f"Esta orden se ejecuta dentro del repositorio ADS de control")
        if args.json:
            print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False, indent=2))
        else:
            print(f"ERROR  {msg}", file=sys.stderr)
        return 2

    hallazgos = []
    m = leer_manifiesto(ads_root, workspace_root, hallazgos)

    if args.orden == "check":
        datos = orden_check(m, hallazgos)
    elif args.orden == "init":
        datos = orden_init(m, hallazgos, set(args.ids))
    else:
        datos = orden_status(m, hallazgos)

    errores = [h for h in hallazgos if h.nivel == ERROR]
    avisos = [h for h in hallazgos if h.nivel == WARN]

    if args.json:
        print(json.dumps({
            "ok": not errores,
            "orden": args.orden,
            "ads_root": ads_root,
            "workspace_root": workspace_root,
            "schema": m.schema if m else None,
            "layout": m.layout if m else None,
            "components": m.components if m else [],
            "hallazgos": [h.a_dict() for h in hallazgos],
            **datos,
        }, ensure_ascii=False, indent=2))
    else:
        print(f"control repo : {ads_root}")
        print(f"workspace    : {workspace_root}")
        if args.orden == "status":
            print()
            imprimir_status(datos.get("sources", []))
            print()
        for h in hallazgos:
            print(h, file=sys.stderr if h.nivel == ERROR else sys.stdout)
        print(f"\n{len(errores)} errores · {len(avisos)} avisos")

    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
