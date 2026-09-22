#!/usr/bin/env python3
"""base — de qué commit nació un paquete y si el mundo cambió debajo (Directiva §61, §63).

Un trabajador que sigue horas sobre una realidad obsoleta descubre al final que Git no
puede fusionar lo suyo, y para entonces ya ha pisado o ha sido pisado. La Directiva pide lo
contrario: antes de una implementación significativa y en los checkpoints de un trabajo
largo, saber DE QUÉ COMMIT nació el trabajo, cuál es AHORA la base, QUÉ cambió entre medias
y si TOCA LO MISMO; si el cambio es compatible, registrar la base nueva y seguir; si
contradice, generar dependencia o conflicto y no pisar el trabajo ajeno (§63). Y que la
rama del ADS y la de cada fuente consten por paquete, en la visión durable de la
concurrencia (§61).

Este módulo MIDE y CLASIFICA. No fusiona, no rebasa, no toca ningún árbol: reconciliar es
del trabajador, en su rama. Sólo biblioteca estándar y `git` sobre refs LOCALES —sin red:
`origin/main` es lo último que se trajo, no lo que hay en el remoto—. Un directorio que no
es un repositorio Git no se mide, y se dice (`no-medible`): los laboratorios de las
baterías no lo son, y en ellos nada cambia.

    VEREDICTO       no-medible · sin-cambio · compatible · contradiccion

`contradiccion` es que la base avanzó sobre un fichero que este trabajo también cambió, o
—en el control repo— que las dos ramas escriben `estado/` (§62: dos ramas que escriben el
estado durable divergen; `ads_estado.py divergencia` lo clasifica fino). `compatible` es
que la base avanzó sobre otra cosa: se registra la base nueva y se continúa.
"""
from __future__ import annotations

import os
import subprocess

NO_MEDIBLE = "no-medible"
SIN_CAMBIO = "sin-cambio"
COMPATIBLE = "compatible"
CONTRADICCION = "contradiccion"
VEREDICTOS = (NO_MEDIBLE, SIN_CAMBIO, COMPATIBLE, CONTRADICCION)

CONTROL_REPO = "control-repo"
ZONA_DE_ESTADO = "estado/"
# la referencia de INTEGRACIÓN contra la que se mide la base, por orden de preferencia
REFS_BASE = ("origin/HEAD", "origin/main", "main", "origin/master", "master")
TIEMPO_GIT = 20


def _git(args, cwd, tiempo=TIEMPO_GIT):
    """`git <args>` en `cwd`; None si falla, no está o tarda. Nunca pide credenciales.

    DEFECTO QUE CIERRA: este módulo nació con su PROPIO `subprocess.run` sobre Git, que es
    exactamente la via paralela que `T188` existe para impedir —«el canal UNICO de
    invocacion de Git»—. El censo del aparato lo denunciaba desde el primer dia y nadie lo
    vio, porque la CI del kernel no corre `test_admision.py`. No se declara una sede nueva
    en `SEDES_DE_PROCESO`: eso seria indultar el defecto en vez de corregirlo. Se pasa por
    el canal, que ademas trae entorno hermetico —sin configuracion de la maquina, sin red,
    sin prompt—, que es mas de lo que este `_git` conseguia a mano.
    """
    from gobierno.git import CanalGit, GitInvocacionProhibida                # noqa: PLC0415
    try:
        codigo, salida, _error = CanalGit(cwd).ejecutar(
            *args, exigir_exito=False, tiempo=tiempo)
    except (OSError, subprocess.SubprocessError, GitInvocacionProhibida):
        return None
    if codigo != 0:
        return None
    return salida.decode("utf-8", "replace").strip()


def _rutas_tocadas(desde, hasta, cwd):
    """Las rutas que cambiaron entre dos revisiones, POR EL CANAL DE LECTURA.

    Una lista de rutas de Git no se lee con `--name-only`: se lee con `-z`, porque un
    nombre con salto de linea parte la lista en dos y el aparato cuenta mal. Eso es lo que
    `admision/lectura.py` es, y lo que `T188` comprueba con `separador_seguro`.

    NO se traga ninguna excepcion. La primera version de esto devolvia `[]` ante cualquier
    fallo «para no romper el ciclo», y el efecto se midio en el acto: `test_oficina` paso a
    declarar `compatible` un avance que CONTRADICE, porque una lista vacia no solapa con
    nada. Un error convertido en lista vacia no es prudencia: es un veredicto inventado.
    """
    from admision.lectura import CanalDeLecturaGit                           # noqa: PLC0415
    # `referencia` es el vocabulario CERRADO de `V6-07` —contra que ESTADO se juzga—, no la
    # revision: aqui siempre se juzga contra la base de la que nacio el trabajo.
    filas = CanalDeLecturaGit(cwd).diferencia(str(desde), str(hasta), referencia="base")
    return sorted({str(fila["ruta"]) for fila in filas if fila.get("ruta")})


def es_repo(ruta):
    return bool(ruta) and os.path.isdir(ruta) and _git(["rev-parse", "--is-inside-work-tree"], ruta) == "true"


def ref_base(ruta, rama):
    """La referencia de integración: `origin/HEAD` si apunta a otra rama, si no la primera
    de REFS_BASE que exista y no sea la rama actual."""
    for candidata in REFS_BASE:
        if candidata.endswith("/HEAD"):
            destino = _git(["symbolic-ref", "-q", "--short", "refs/remotes/" + candidata], ruta)
            if destino and destino != rama and not destino.endswith("/" + rama):
                return destino
            continue
        if candidata == rama or candidata.endswith("/" + rama):
            continue
        if _git(["rev-parse", "--verify", "--quiet", candidata], ruta):
            return candidata
    return None


def medir(ruta, *, id):
    """La medida de UN repositorio: rama, cabeza, base, de qué commit nació el trabajo,
    cuánto avanzó la base y qué ficheros cambian a cada lado."""
    if not es_repo(ruta):
        return {"id": id, "medible": False, "motivo": "no es un repositorio Git"}
    rama = _git(["rev-parse", "--abbrev-ref", "HEAD"], ruta) or ""
    cabeza = _git(["rev-parse", "HEAD"], ruta)
    if not cabeza:
        return {"id": id, "medible": False, "motivo": "el repositorio no tiene ningún commit", "rama": rama}
    ref = ref_base(ruta, rama)
    if not ref:
        return {"id": id, "medible": False, "rama": rama, "cabeza": cabeza[:12],
                "motivo": "sin referencia de integración (origin/HEAD, origin/main, main)"}
    nacio = _git(["merge-base", "HEAD", ref], ruta) or ""
    base_ahora = _git(["rev-parse", ref], ruta) or ""
    faltan = int(_git(["rev-list", "--count", "HEAD.." + ref], ruta) or 0)
    mios = int(_git(["rev-list", "--count", ref + "..HEAD"], ruta) or 0)
    de_la_base = _rutas_tocadas(nacio, base_ahora, ruta) if (faltan and nacio) else []
    de_los_mios = _rutas_tocadas(nacio, "HEAD", ruta) if (mios and nacio) else []
    return {
        "id": id, "medible": True, "rama": rama, "cabeza": cabeza[:12], "ref_base": ref,
        "nacio_de": nacio[:12], "base_ahora": base_ahora[:12],
        "commits_de_la_base_que_no_tengo": faltan, "commits_mios_que_la_base_no_tiene": mios,
        "ficheros_de_la_base": sorted(f for f in de_la_base if f),
        "ficheros_mios": sorted(f for f in de_los_mios if f),
    }


def comparar(nacimiento, ahora):
    """Clasifica el cambio de base de UN repositorio desde su nacimiento hasta ahora."""
    if not ahora.get("medible"):
        return {"id": ahora.get("id"), "veredicto": NO_MEDIBLE, "motivo": ahora.get("motivo", "")}
    nacio = (nacimiento or {}).get("base_ahora") or ahora["nacio_de"]
    if ahora["commits_de_la_base_que_no_tengo"] == 0:
        return {"id": ahora["id"], "veredicto": SIN_CAMBIO, "nacio_de": nacio,
                "base_registrada": ahora["base_ahora"], "commits_nuevos": 0, "ficheros_en_conflicto": []}
    conflicto = set(ahora["ficheros_de_la_base"]) & set(ahora["ficheros_mios"])
    if ahora["id"] == CONTROL_REPO:
        base_escribe_estado = any(f.startswith(ZONA_DE_ESTADO) for f in ahora["ficheros_de_la_base"])
        yo_escribo_estado = any(f.startswith(ZONA_DE_ESTADO) for f in ahora["ficheros_mios"])
        if base_escribe_estado and yo_escribo_estado:
            conflicto.add(ZONA_DE_ESTADO)
    veredicto = CONTRADICCION if conflicto else COMPATIBLE
    return {"id": ahora["id"], "veredicto": veredicto, "nacio_de": nacio,
            "base_registrada": ahora["base_ahora"] if veredicto == COMPATIBLE else nacio,
            "commits_nuevos": ahora["commits_de_la_base_que_no_tengo"],
            "ficheros_en_conflicto": sorted(conflicto)}


def repos_de(control_repo):
    """El control repo y las fuentes de `SOURCES.toml` que existen en disco (layout de
    hermanos: `path` relativo al directorio padre del control repo)."""
    repos = [(CONTROL_REPO, control_repo)]
    try:
        from . import encuadre                                             # noqa: PLC0415
        manifiesto = encuadre.descubrir_fuentes(control_repo)
    except Exception:                                                      # noqa: BLE001
        manifiesto = {"fuentes": []}   # la base es una MEDIDA: un manifiesto ilegible no impide tomar
    workspace = os.path.dirname(os.path.abspath(control_repo))
    for fuente in manifiesto.get("fuentes") or []:
        ruta = fuente.get("path") or ""
        if not ruta:
            continue
        if not os.path.isabs(ruta):
            ruta = os.path.join(workspace, ruta)
        if os.path.isdir(ruta):
            repos.append((fuente["id"], ruta))
    return repos


def nacimiento_de(medidas):
    """Lo que se conserva del nacimiento: por repo, rama, de qué commit nació y qué base había."""
    return {id: {"rama": m.get("rama"), "nacio_de": m.get("nacio_de"), "base_ahora": m.get("base_ahora"),
                 "ref_base": m.get("ref_base")}
            for id, m in medidas.items() if m.get("medible")}


def evaluar(control_repo, nacimiento=None):
    """Mide todos los repos y, si hay nacimiento, clasifica el cambio de cada uno. El
    veredicto global es el peor de los medibles."""
    medidas = {id: medir(ruta, id=id) for id, ruta in repos_de(control_repo)}
    cambios = {id: comparar((nacimiento or {}).get(id), m) for id, m in medidas.items()}
    medibles = [c for c in cambios.values() if c["veredicto"] != NO_MEDIBLE]
    veredicto = max((c["veredicto"] for c in medibles), key=VEREDICTOS.index) if medibles else NO_MEDIBLE
    return {"veredicto": veredicto, "medidas": medidas, "cambios": cambios,
            "conflictos": [c for c in medibles if c["veredicto"] == CONTRADICCION]}


def resumen(evaluacion, nacimiento):
    """Lo que viaja en el checkpoint bajo `base`: nacimiento, ahora, veredicto y conflictos."""
    ahora = {id: {k: m.get(k) for k in ("rama", "cabeza", "base_ahora", "commits_de_la_base_que_no_tengo",
                                        "commits_mios_que_la_base_no_tiene")}
             for id, m in evaluacion["medidas"].items() if m.get("medible")}
    return {
        "veredicto": evaluacion["veredicto"],
        "nacimiento": nacimiento,
        "ahora": ahora,
        "registrada": {id: c.get("base_registrada") for id, c in evaluacion["cambios"].items()
                       if c["veredicto"] in (SIN_CAMBIO, COMPATIBLE)},
        "conflictos": [{"repo": c["id"], "commits_nuevos": c["commits_nuevos"],
                        "ficheros": c["ficheros_en_conflicto"]} for c in evaluacion["conflictos"]],
        "no_medibles": {id: c.get("motivo", "") for id, c in evaluacion["cambios"].items()
                        if c["veredicto"] == NO_MEDIBLE},
    }


def frase(conflictos):
    """Los conflictos de `evaluar` (comparaciones), en una línea para un error."""
    return "; ".join(c["id"] + ": " + str(c["commits_nuevos"]) + " commit(s) nuevo(s) en la base tocan "
                     + ", ".join(c["ficheros_en_conflicto"]) for c in conflictos)
