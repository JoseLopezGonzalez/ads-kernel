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


def desde_el_nacimiento(ahora, nacimiento, ruta):
    """T518 · La base se juzga contra la que había cuando NACIÓ el trabajo, no contra el punto
    en que la rama se separó de ella.

    DEFECTO MEDIDO en la primera ejecución de producto por la oficina (La Pesquerapp,
    2026-09-27): la rama de la campaña ya divergía de `main` en dos commits que tocan `estado/`
    ANTES de que se tomara ningún paquete. `medir` cuenta la base desde el `merge-base`, así
    que todo paquete del control repo —y todos escriben el estado— salía `contradiccion` al
    entregar, aunque la base no se hubiera movido ni un commit durante su trabajo. Ninguna
    entrega era posible en esa rama; cada intento gastaba un modelo para ser rechazado.

    Con nacimiento: si la base es la misma que al nacer, no avanzó —la divergencia previa se
    anota y no se juzga, es de la rama y no del paquete—; si avanzó, cuentan sólo los commits y
    ficheros de la base DESDE su nacimiento."""
    if not ahora.get("medible") or not nacimiento or not nacimiento.get("base_ahora"):
        return ahora
    nacida = str(nacimiento["base_ahora"])
    salida = dict(ahora, divergencia_previa=ahora.get("commits_de_la_base_que_no_tengo", 0))
    if str(ahora.get("base_ahora") or "")[:12] == nacida[:12]:
        salida.update(commits_de_la_base_que_no_tengo=0, ficheros_de_la_base=[])
        return salida
    completo = _git(["rev-parse", ahora["ref_base"]], ruta) or ""
    # desde el nacimiento, o desde lo que el trabajo YA incorporó si reconcilió después
    comun = _git(["merge-base", "HEAD", completo], ruta) or ""
    desde = comun if comun and _git(["merge-base", "--is-ancestor", nacida, comun], ruta) is not None else nacida
    nuevos = int(_git(["rev-list", "--count", desde + ".." + completo], ruta) or 0)
    salida.update(commits_de_la_base_que_no_tengo=nuevos,
                  ficheros_de_la_base=sorted(f for f in _rutas_tocadas(desde, completo, ruta) if f) if nuevos else [])
    return salida


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


def repos_del_trabajo(control_repo, fuentes=None, nacimiento=None):
    """T520 · Los repos que se miden son LOS DEL PAQUETE, no todos los hermanos del control repo.

    DEFECTO MEDIDO en la primera ejecución de producto por la oficina (La Pesquerapp,
    2026-09-28): `repos_de` medía el control repo y los clones PRINCIPALES de `SOURCES.toml`,
    no el árbol donde el paquete trabaja (un worktree por encargo). En el control repo, además,
    «lo mío» es todo lo que hizo la rama de la campaña —el estado que escribe el runtime en cada
    transición y el diario del coordinador—, así que un push a `main` desde otra sesión, sobre
    `estado/` y `docs/JOURNAL.md`, declaró `contradiccion` todo paquete vivo aunque su trabajo
    estuviera entero en el frontend. La divergencia del control repo es DE LA RAMA: la vigila
    `ads_estado.py divergencia` (§62) y se resuelve al integrar, no paquete a paquete.

    DECISIÓN · por orden: (1) lo que midió el nacimiento, si guardó sus rutas —lo que se juzga
    es lo que se midió al nacer—; (2) las fuentes que el brief declara con ruta en disco —el
    control repo NO entra: es donde corre la oficina, no donde trabaja el paquete—; (3) sin
    fuentes declaradas, el control repo y los hermanos de `SOURCES.toml`, que es el caso en que
    el control repo ES el lugar del trabajo (los laboratorios, y los encargos de reconstrucción
    del propio ADS)."""
    guardadas = [(id, n.get("ruta")) for id, n in (nacimiento or {}).items() if isinstance(n, dict) and n.get("ruta")]
    if guardadas and len(guardadas) == len(nacimiento or {}):
        return guardadas
    declaradas = _declaradas(fuentes)
    if declaradas:
        return declaradas
    return repos_de(control_repo)


def _declaradas(fuentes):
    """Las fuentes del brief con ruta en disco: `(id, ruta)`."""
    return [(str(f.get("id")), str(f["path"])) for f in (fuentes or ())
            if isinstance(f, dict) and f.get("path") and not f.get("ausente") and os.path.isdir(str(f["path"]))]


def nacimiento_de(medidas, rutas=None):
    """Lo que se conserva del nacimiento: por repo, rama, de qué commit nació, qué base había y
    —desde T520— QUÉ RUTA se midió, para que cada medida posterior mire el mismo árbol."""
    return {id: dict({"rama": m.get("rama"), "nacio_de": m.get("nacio_de"), "base_ahora": m.get("base_ahora"),
                      "ref_base": m.get("ref_base")}, **({"ruta": rutas[id]} if rutas and id in rutas else {}))
            for id, m in medidas.items() if m.get("medible")}


def mide_otros_repos(nacimiento, fuentes):
    """¿El nacimiento guardado NO es la medida de las fuentes del paquete? (T520: los
    nacimientos anteriores no guardaban ruta y medían los clones principales).

    T521 · Sin nacimiento y con fuentes declaradas, también: no hay medida de las fuentes.
    MEDIDO al vendorizar T520 (2026-09-28): un paquete que se entregó `bloqueado` perdía su
    nacimiento, al retomarlo esta función devolvía False —«no hay nacimiento que comparar»—,
    `tomar` no medía, y `entregar` volvía a medir la rama del control repo."""
    rutas = dict(_declaradas(fuentes))
    if not rutas:
        return False
    if not nacimiento:
        return True
    return any(not (isinstance(n, dict) and n.get("ruta") == rutas.get(id)) for id, n in nacimiento.items()) \
        or set(nacimiento) != set(rutas)


def evaluar(control_repo, nacimiento=None, fuentes=None):
    """Mide los repos del trabajo (T520) y, si hay nacimiento, clasifica el cambio de cada uno.
    El veredicto global es el peor de los medibles."""
    rutas = dict(repos_del_trabajo(control_repo, fuentes=fuentes, nacimiento=nacimiento))
    medidas = {id: medir(ruta, id=id) for id, ruta in rutas.items()}
    for id, m in medidas.items():
        medidas[id] = desde_el_nacimiento(m, (nacimiento or {}).get(id), rutas[id])
    cambios = {id: comparar((nacimiento or {}).get(id), m) for id, m in medidas.items()}
    medibles = [c for c in cambios.values() if c["veredicto"] != NO_MEDIBLE]
    veredicto = max((c["veredicto"] for c in medibles), key=VEREDICTOS.index) if medibles else NO_MEDIBLE
    return {"veredicto": veredicto, "medidas": medidas, "cambios": cambios, "rutas": rutas,
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
