#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DERIVACIÓN MECÁNICA DEL UNIVERSO OBLIGATORIO DE UN GATE DE F4c
==============================================================

Materializa la regla `1bis` de `C-L.5` —`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`,
sección «`C-L.5` · La condición de COBERTURA del próximo gate»— y **publica el comando
auditable** que ella exige, de modo que cualquiera pueda reejecutarlo y obtener el mismo
universo.

POR QUÉ EXISTE ESTE FICHERO
---------------------------
`P-08` encontró que el manifiesto del gate anterior declaraba «FUENTES SIN ASIGNAR 0» sobre
un universo **ELEGIDO a mano**: el cero era verdadero por construcción, porque el universo
se escogía escogiendo lo ya asignado. `1bis` corrigió la REGLA, pero la materialización
seguía siendo una tabla escrita a mano. Una formulación manual que ya ha caducado una vez
no se vuelve a escribir a mano: **se deriva**. Éste es el derivador.

QUÉ DERIVA, Y DE QUÉ SEDE
-------------------------
El universo obligatorio es la UNIÓN, sin quitar nada, de los cinco componentes que `1bis`
enumera. Cada uno se lee de su SEDE NORMATIVA, no de una copia:

  (i)   las cuatro fuentes del apartado «QUÉ HAY QUE LEER ÍNTEGRO» de `C-L.5`
        SEDE: `11-ARQUITECTURA-INTEGRADA.md`, la propia sección `C-L.5`
  (ii)  las CATORCE fuentes y las QUINCE fichas de la condición `C-0.1` del documento 18
        SEDE: el bloque `G-24` de `comprobar-correccion-gate-de-cierre.py`, que es la única
        sede del árbol que las enumera nombre a nombre y que las contrasta contra el árbol
        en cada ejecución de la batería. Leerlas de aquí evita crear una SEGUNDA sede del
        mismo catálogo, que es justo la clase de defecto que `Q-04` castigó
  (iii) el documento 11, el registro de decisiones y el checkpoint
  (iv)  todo dictamen de gate anterior aún no leído íntegro por nadie
        SEDE: barrido de `docs/evolucion/NN-*.md` por el TÍTULO de su H1
  (v)   el objeto que el gate juzga, según SU encargo
        SEDE: el bloque `ENCARGO` de abajo, con la cláusula del encargo que justifica cada
        entrada. Es lo único que cambia de un gate a otro, y por eso está declarado y
        anotado en vez de inferido

FALLA CERRADO
-------------
Si una sede no se puede leer, si un recuento derivado no coincide con el que su sede
declara, o si una ruta derivada no existe en el árbol, **sale con código 2 y diagnóstico**.
Nunca adivina y nunca reduce el universo en silencio: un universo que encoge sin decirlo es
exactamente el defecto que `P-08` describió.

USO
---
    python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py            # tabla
    python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --md       # Markdown
    python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --rutas    # rutas
"""

import hashlib
import io
import os
import re
import sys

# La raíz se deriva de `__file__` —tres niveles por encima de docs/evolucion/verificacion/—
# y de NADA más. No usa el cwd. Es la misma lección que la batería aprendió: tomar el
# directorio del proceso hacía comprobar el repositorio del autor en vez del que se tiene
# delante.
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir, os.pardir, os.pardir))

ARQ = "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md"
BATERIA = "docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py"
DECISIONES = "docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md"
CHECKPOINT = "docs/evolucion/CHECKPOINT-ADS-NEXT.md"


class SedeIlegible(Exception):
    """Una sede normativa no se puede leer, o no dice lo que la regla dice que dice."""


def _leer(rel):
    ruta = os.path.join(RAIZ, rel)
    try:
        with io.open(ruta, encoding="utf-8") as fh:
            return fh.read()
    except OSError as e:
        raise SedeIlegible("sede %s ilegible: %s" % (rel, e))


def _resolver(nombre):
    """Un nombre de fichero suelto a su ruta única en el árbol. Falla si no es única."""
    encontrados = []
    for base, dirs, ficheros in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
        if nombre in ficheros:
            encontrados.append(os.path.relpath(os.path.join(base, nombre), RAIZ))
    if len(encontrados) != 1:
        raise SedeIlegible("«%s» no resuelve a UNA ruta: %r" % (nombre, encontrados))
    return encontrados[0].replace(os.sep, "/")


# ── (i) · las cuatro fuentes de «QUÉ HAY QUE LEER ÍNTEGRO» ───────────────────────
def componente_i():
    texto = _leer(ARQ)
    m = re.search(r"^## `C-L\.5`.*?$", texto, re.M)
    if not m:
        raise SedeIlegible("no aparece la sección `C-L.5` en %s" % ARQ)
    seccion = texto[m.start():]
    fin = re.search(r"^## ", seccion[3:], re.M)
    if fin:
        seccion = seccion[:fin.start() + 3]
    b = re.search(r"QUÉ HAY QUE LEER\s*\n?.*?ÍNTEGRO(.*?)\n\s*DOS MANIFIESTOS",
                  seccion, re.S)
    if not b:
        raise SedeIlegible("no aparece el bloque «QUÉ HAY QUE LEER ÍNTEGRO» en `C-L.5`")
    nombres = re.findall(r"`([A-Za-z0-9][-A-Za-z0-9_.]*\.md)`", b.group(1))
    vistos, orden = set(), []
    for n in nombres:
        if n not in vistos:
            vistos.add(n)
            orden.append(n)
    if len(orden) != 4:
        raise SedeIlegible("«QUÉ HAY QUE LEER ÍNTEGRO» debe nombrar CUATRO fuentes; "
                           "derivadas %d: %r" % (len(orden), orden))
    return [_resolver(n) for n in orden]


# ── (ii) · las CATORCE fuentes y las QUINCE fichas de `C-0.1` ────────────────────
def componente_ii():
    texto = _leer(BATERIA)
    mf = re.search(r'^fuentes\s*=\s*"""(.*?)"""', texto, re.S | re.M)
    if not mf:
        raise SedeIlegible("no aparece el catálogo `fuentes` de `G-24` en %s" % BATERIA)
    fuentes = [l.strip() for l in mf.group(1).split("\n") if l.strip()]
    if len(fuentes) != 14:
        raise SedeIlegible("`C-0.1` declara CATORCE fuentes; `G-24` enumera %d"
                           % len(fuentes))
    mc = re.search(r"^CAPACIDADES\s*=\s*\[(.*?)\]", texto, re.S | re.M)
    if not mc:
        raise SedeIlegible("no aparece `CAPACIDADES` de `G-24` en %s" % BATERIA)
    fichas = re.findall(r'"([A-Z]{3})"', mc.group(1))
    if len(fichas) != 15 or len(set(fichas)) != 15:
        raise SedeIlegible("`C-0.2` declara QUINCE fichas; `G-24` enumera %d (%d distintas)"
                           % (len(fichas), len(set(fichas))))
    return fuentes + ["kernel/operativo/capacidades/%s/CAPACIDAD.md" % c for c in fichas]


# ── (iii) · documento 11, registro de decisiones y checkpoint ────────────────────
def componente_iii():
    return [ARQ, DECISIONES, CHECKPOINT]


# ── (iv) · todo dictamen de gate anterior ────────────────────────────────────────
# Se derivan del TÍTULO de su H1 y no de una lista: una lista escrita a mano deja fuera el
# dictamen que se publique después, y ése es precisamente el que nadie ha leído.
VOCES_DE_DICTAMEN = ("GATE", "CRÍTICA", "CRITICA", "REVISIÓN", "REVISION",
                     "DEVOLUCIÓN", "DEVOLUCION", "COMPLEMENTO")


def componente_iv():
    dir_ev = os.path.join(RAIZ, "docs/evolucion")
    salida = []
    for nombre in sorted(os.listdir(dir_ev)):
        if not re.match(r"^\d\d-.*\.md$", nombre):
            continue
        rel = "docs/evolucion/" + nombre
        cabecera = ""
        for linea in _leer(rel).split("\n"):
            if linea.startswith("# "):
                cabecera = linea.upper()
                break
        if any(v in cabecera for v in VOCES_DE_DICTAMEN):
            salida.append(rel)
    if not salida:
        raise SedeIlegible("cero dictámenes derivados de docs/evolucion: el barrido no ve "
                           "el corpus, y un universo vacío por no mirar es el defecto que "
                           "`N161g` describe")
    return salida


# ── (v) · el objeto que ESTE gate juzga, según su encargo ────────────────────────
# Cada fila declara la cláusula del encargo que la mete en el universo. Sin cláusula no
# entra, y la cláusula se lee en el informe del gate.
ENCARGO = [
    ("docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md",
     "los 24 hallazgos del documento 21 · M-04 · Q-01 Q-04 Q-05"),
    ("docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py",
     "M-04 como proposición general · lector estructurado frente a prosa · "
     "distribución de vías · conjunto vigilado · adiciones no rastreadas · Git ausente"),
    ("docs/evolucion/verificacion/README.md",
     "lo que la batería declara de sí misma, frente a lo que hace"),
    ("docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md",
     "C-L.5 · el manifiesto previo del gate anterior, inmutable"),
    ("docs/evolucion/00-INDICE.md",
     "catálogo y contratos duplicados · trazabilidad de las tandas"),
    ("kernel/KERNEL.md",
     "material APROBADO que PN-16 y PN-15 invocan"),
    ("kernel/operativo/recorrido/01-PROCESOS.md",
     "catálogo de procesos · UNA sede · distribución exacta de vías"),
    ("kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md",
     "obligatorias frente a condicionales"),
    ("kernel/operativo/esquemas/proceso.yaml",
     "lector estructurado · obligatorias frente a condicionales"),
    ("kernel/operativo/contratos/00-INDICE.md",
     "catálogo y contratos duplicados"),
    ("kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md", "contratos C1-C7"),
    ("kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md", "contratos C1-C7"),
    ("kernel/operativo/contratos/C3-METODO-EJECUTABLE.md", "contratos C1-C7"),
    ("kernel/operativo/contratos/C4-MATERIALIZACION.md", "contratos C1-C7"),
    ("kernel/operativo/contratos/C5-HANDOFF.md", "contratos C1-C7"),
    ("kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md", "contratos C1-C7"),
    ("kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md",
     "contratos C1-C7 · Git ausente · gobierno de ramas"),
    ("docs/rediseno/a-CAPACIDADES-APROBADA.md",
     "material APROBADO (a) · PN-15 y PN-16 se derogan o no contra él"),
    ("docs/rediseno/b-RECORRIDO-APROBADA.md",
     "material APROBADO (b) · L836, la grafía canónica que origina PN-16"),
    ("docs/rediseno/a-ENMIENDA-E1-ENC.md", "material APROBADO E1"),
    ("docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md", "material APROBADO E2"),
    ("docs/rediseno/CHECKPOINT-OPERATIVO.md",
     "la batería del kernel, el runner y las trece evidencias"),
]


def componente_v():
    return [r for r, _ in ENCARGO]


COMPONENTES = [
    ("i", "las CUATRO fuentes de «QUÉ HAY QUE LEER ÍNTEGRO» de `C-L.5`", componente_i),
    ("ii", "las CATORCE fuentes y las QUINCE fichas de `C-0.1` / `C-0.2`", componente_ii),
    ("iii", "documento 11 · registro de decisiones · checkpoint", componente_iii),
    ("iv", "todo dictamen de gate anterior", componente_iv),
    ("v", "el objeto que ESTE gate juzga, según su encargo", componente_v),
]


def derivar():
    """Devuelve (universo_ordenado, procedencia) o lanza SedeIlegible."""
    procedencia = {}
    for clave, _titulo, fn in COMPONENTES:
        for rel in fn():
            procedencia.setdefault(rel, []).append(clave)
    faltan = [r for r in procedencia if not os.path.isfile(os.path.join(RAIZ, r))]
    if faltan:
        raise SedeIlegible("rutas derivadas que NO existen en el árbol: %r" % sorted(faltan))
    return sorted(procedencia), procedencia


def metricas(rel):
    ruta = os.path.join(RAIZ, rel)
    with io.open(ruta, "rb") as fh:
        crudo = fh.read()
    lineas = crudo.count(b"\n")
    if crudo and not crudo.endswith(b"\n"):
        lineas += 1
    return lineas, hashlib.sha256(crudo).hexdigest()


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "--tabla"
    try:
        universo, procedencia = derivar()
    except SedeIlegible as e:
        sys.stderr.write("FALLA CERRADO · %s\n" % e)
        return 2

    if modo == "--rutas":
        for rel in universo:
            sys.stdout.write(rel + "\n")
        return 0

    filas = [(rel, ) + metricas(rel) + ("+".join(procedencia[rel]), ) for rel in universo]
    total = sum(f[1] for f in filas)

    if modo == "--md":
        out = ["| ruta | líneas | SHA-256 | componentes `1bis` |", "|---|---|---|---|"]
        for rel, lin, sha, comp in filas:
            out.append("| `%s` | %d | `%s` | %s |" % (rel, lin, sha, comp))
        sys.stdout.write("\n".join(out) + "\n")
    else:
        for rel, lin, sha, comp in filas:
            sys.stdout.write("%-6s %7d  %s  %s\n" % (comp, lin, sha[:16] + "…", rel))

    sys.stdout.write("\n%d fuentes obligatorias · %d líneas\n" % (len(filas), total))
    for clave, titulo, fn in COMPONENTES:
        n = sum(1 for r in universo if clave in procedencia[r])
        sys.stdout.write("  (%-3s) %3d   %s\n" % (clave, n, titulo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
