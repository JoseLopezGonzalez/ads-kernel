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

  (i)   las fuentes del apartado «QUÉ HAY QUE LEER ÍNTEGRO» de `C-L.5`
        SEDE: `11-ARQUITECTURA-INTEGRADA.md`, la propia sección `C-L.5`
        CARDINAL: leído de `1bis`, no escrito aquí
  (ii)  las fuentes y las fichas de la condición `C-0.1` del documento 18
        SEDE: el bloque `G-24` de `comprobar-correccion-gate-de-cierre.py`, que es la única
        sede del árbol que las enumera nombre a nombre y que las contrasta contra el árbol
        en cada ejecución de la batería. Leerlas de aquí evita crear una SEGUNDA sede del
        mismo catálogo, que es justo la clase de defecto que `Q-04` castigó
        CARDINALES: leídos de `1bis`, y se exige además que las fuentes sean DISTINTAS —una
        entrada repetida dejaba el recuento en pie y el universo con una fuente menos
  (iii) el documento 11, el registro de decisiones y el checkpoint
        GUARDA: `1bis` tiene que seguir nombrando las TRES piezas, y las tres rutas tienen
        que existir y ser distintas. Antes eran tres constantes sin comprobar nada
  (iv)  todo dictamen de gate anterior aún no leído íntegro por nadie
        SEDE: barrido de `docs/evolucion/NN-*.md` por el TÍTULO de su H1
  (v)   el objeto que el gate juzga, según SU encargo
        SEDE: el bloque `ENCARGO` de abajo, con la cláusula del encargo que justifica cada
        entrada. Es lo único que cambia de un gate a otro, y por eso está declarado y
        anotado en vez de inferido
        GUARDA: ninguna fila sin cláusula, ninguna ruta repetida y ninguna inexistente

FALLA CERRADO
-------------
Si una sede no se puede leer, si un recuento derivado no coincide con el que su sede
declara, o si una ruta derivada no existe en el árbol, **sale con código 2 y diagnóstico**.
Nunca adivina y nunca reduce el universo en silencio: un universo que encoge sin decirlo es
exactamente el defecto que `P-08` describió. **Y eso se EJECUTA, no se promete**: toda ruta
que un manifiesto INMUTABLE declaró obligatoria tiene que seguir saliendo de algún
componente —el cliquet de `universos_publicados()`—, y un documento numerado que el
componente (iv) no sepa clasificar para el derivador entero en vez de caerse del universo.

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


# ── numerales, y los CARDINALES que `1bis` publica ───────────────────────────────
#
# Los cardinales de los componentes (i) y (ii) —CUATRO fuentes, CATORCE fuentes y QUINCE
# fichas— estaban ESCRITOS en este fichero, que existe precisamente porque una formulación
# manual ya había caducado una vez. Ahora se LEEN de `1bis`, que es su sede, y si la sede
# cambia el derivador se mueve con ella; si la sede no los publica, falla cerrado.
_PALABRA = {
    "cero": 0, "una": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12,
    "trece": 13, "catorce": 14, "quince": 15, "dieciseis": 16, "diecisiete": 17,
    "dieciocho": 18, "diecinueve": 19, "veinte": 20,
}
_ACENTOS = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")


def _num(txt):
    t = txt.translate(_ACENTOS).lower().strip()
    return int(t) if t.isdigit() else _PALABRA.get(t)


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


# ── la sede `1bis`, de donde salen la REGLA y sus CARDINALES ─────────────────────
def _bloque_1bis():
    texto = _leer(ARQ)
    m = re.search(r"^## `C-L\.5`.*?$", texto, re.M)
    if not m:
        raise SedeIlegible("no aparece la sección `C-L.5` en %s" % ARQ)
    seccion = texto[m.start():]
    fin = re.search(r"^## ", seccion[3:], re.M)
    if fin:
        seccion = seccion[:fin.start() + 3]
    i = seccion.find("1bis")
    if i < 0:
        raise SedeIlegible("`C-L.5` no contiene la regla `1bis`, que es la sede del "
                           "universo obligatorio")
    return seccion, seccion[i:]


def cardinales():
    """(n_fuentes_i, n_fuentes_ii, n_fichas_ii), LEÍDOS de `1bis`."""
    _, b = _bloque_1bis()
    plano = re.sub(r"\s+", " ", re.sub(r"[`*]", "", b))
    mi = re.search(r"\(i\)\s+las\s+([a-zA-Záéíóú]+|\d+)\s+fuentes", plano)
    mii = re.search(r"\(ii\)\s+las\s+([a-zA-Záéíóú]+|\d+)\s+fuentes\s+y\s+"
                    r"([a-zA-Záéíóú]+|\d+)\s+fichas", plano)
    if not mi:
        raise SedeIlegible("`1bis` no publica el cardinal del componente (i): "
                           "«(i) las <n> fuentes …»")
    if not mii:
        raise SedeIlegible("`1bis` no publica los cardinales del componente (ii): "
                           "«(ii) las <n> fuentes y <n> fichas …»")
    crudos = (mi.group(1), mii.group(1), mii.group(2))
    valores = tuple(_num(c) for c in crudos)
    if any(v is None for v in valores):
        # `T-22`. Aquí había `"… %r" % (a, b, c)`: un `%r` con una tupla de TRES es
        # `TypeError`. **La única rama del derivador que existe para fallar cerrado era la
        # única que no fallaba cerrado**: reventaba con traza y código 1 —no 2— y sin la
        # línea `FALLA CERRADO ·` que el manifiesto enseña a buscar. La tupla va envuelta.
        raise SedeIlegible("`1bis` publica cardinales que no son numerales legibles: %r"
                           % (crudos,))
    return valores


# ── (i) · las fuentes de «QUÉ HAY QUE LEER ÍNTEGRO», con su cardinal leído ───────
def componente_i():
    seccion, _ = _bloque_1bis()
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
    esperado = cardinales()[0]
    if len(orden) != esperado:
        raise SedeIlegible("`1bis` declara %d fuentes en su componente (i) y «QUÉ HAY QUE "
                           "LEER ÍNTEGRO» nombra %d: %r" % (esperado, len(orden), orden))
    return [_resolver(n) for n in orden]


# ── (ii) · las CATORCE fuentes y las QUINCE fichas de `C-0.1` ────────────────────
def componente_ii():
    texto = _leer(BATERIA)
    mf = re.search(r'^fuentes\s*=\s*"""(.*?)"""', texto, re.S | re.M)
    if not mf:
        raise SedeIlegible("no aparece el catálogo `fuentes` de `G-24` en %s" % BATERIA)
    fuentes = [l.strip() for l in mf.group(1).split("\n") if l.strip()]
    n_fuentes, n_fichas = cardinales()[1], cardinales()[2]
    if len(fuentes) != n_fuentes:
        raise SedeIlegible("`1bis` declara %d fuentes en `C-0.1` y `G-24` enumera %d"
                           % (n_fuentes, len(fuentes)))
    # La UNICIDAD, que no se comprobaba: dos entradas iguales dejaban el recuento en pie y
    # el universo con una fuente menos de las que dice. Es la misma clase de defecto que
    # `P-08` describió — un cero verdadero por construcción — un piso más abajo.
    if len(set(fuentes)) != n_fuentes:
        repetidas = sorted(f for f in set(fuentes) if fuentes.count(f) > 1)
        raise SedeIlegible("`G-24` enumera %d fuentes pero sólo %d DISTINTAS; repetidas: %r"
                           % (len(fuentes), len(set(fuentes)), repetidas))
    mc = re.search(r"^CAPACIDADES\s*=\s*\[(.*?)\]", texto, re.S | re.M)
    if not mc:
        raise SedeIlegible("no aparece `CAPACIDADES` de `G-24` en %s" % BATERIA)
    fichas = re.findall(r'"([A-Z]{3})"', mc.group(1))
    if len(fichas) != n_fichas or len(set(fichas)) != n_fichas:
        raise SedeIlegible("`1bis` declara %d fichas y `G-24` enumera %d (%d distintas)"
                           % (n_fichas, len(fichas), len(set(fichas))))
    return fuentes + ["kernel/operativo/capacidades/%s/CAPACIDAD.md" % c for c in fichas]


# ── (iii) · documento 11, registro de decisiones y checkpoint ────────────────────
def componente_iii():
    """El documento 11, el registro de decisiones y el checkpoint — CON GUARDA.

    Este componente devolvía tres constantes y no comprobaba nada: si una de las tres rutas
    cambiaba de sitio, el universo encogía en silencio, que es exactamente lo que `P-08`
    denunció. Ahora se exige que `1bis` siga nombrando las TRES piezas, que las tres rutas
    existan y que ninguna esté repetida.
    """
    _, b = _bloque_1bis()
    plano = re.sub(r"\s+", " ", re.sub(r"[`*]", "", b))
    m = re.search(r"\(iii\)(.*?)\(iv\)", plano, re.S)
    if not m:
        raise SedeIlegible("`1bis` no publica el componente (iii)")
    piezas = {"documento 11": r"documento 11",
              "registro de decisiones": r"registro de decisiones",
              "checkpoint": r"checkpoint"}
    faltan = [k for k, pat in piezas.items() if not re.search(pat, m.group(1), re.I)]
    if faltan:
        raise SedeIlegible("`1bis` (iii) ya no nombra: %r; el componente devolvía tres "
                           "constantes que su sede ha dejado de respaldar" % faltan)
    rutas = [ARQ, DECISIONES, CHECKPOINT]
    if len(set(rutas)) != len(piezas):
        raise SedeIlegible("el componente (iii) resuelve %d rutas distintas para %d piezas"
                           % (len(set(rutas)), len(piezas)))
    for rel in rutas:
        if not os.path.isfile(os.path.join(RAIZ, rel)):
            raise SedeIlegible("el componente (iii) nombra %s y no existe en el árbol" % rel)
    return rutas


# ── (iv) · todo dictamen de gate anterior ────────────────────────────────────────
# Se derivan del TÍTULO de su H1 y no de una lista: una lista escrita a mano deja fuera el
# dictamen que se publique después, y ése es precisamente el que nadie ha leído.
# `T-15`. La lista era SÓLO positiva, y lo que no casaba con ella se caía del universo **en
# silencio**: un `23-DICTAMEN-…` cuyo H1 no usara una de estas ocho voces no entraba, y nadie
# se enteraba — que es palabra por palabra lo que `1bis` dice que hay que impedir. Faltaban
# además las voces obvias: `DICTAMEN`, `AUDITORÍA`, `CERTIFICACIÓN`, `ADJUDICACIÓN`.
#
# Ahora la clasificación es TOTAL y falla CERRADO: cada documento numerado tiene que caer en
# una de las dos listas, y **el que no case con ninguna para el derivador entero**. Una lista
# positiva puede olvidarse de un dictamen nuevo; una clasificación total, no: el olvido se
# convierte en código 2 con el nombre del documento, y se cierra añadiéndolo a la lista que
# le corresponda, que es una decisión que alguien toma y firma.
VOCES_DE_DICTAMEN = ("GATE", "CRÍTICA", "CRITICA", "REVISIÓN", "REVISION",
                     "DEVOLUCIÓN", "DEVOLUCION", "COMPLEMENTO", "DICTAMEN",
                     "AUDITORÍA", "AUDITORIA", "CERTIFICACIÓN", "CERTIFICACION",
                     "ADJUDICACIÓN", "ADJUDICACION", "VEREDICTO")

VOCES_DE_NO_DICTAMEN = ("ÍNDICE", "INDICE", "BASELINE", "MAPA", "INVARIANTES",
                        "PLAN DE INVESTIGACIÓN", "PLAN DE INVESTIGACION", "INVENTARIO",
                        "CONTRASTE", "DECISIÓN", "DECISION", "DEMOSTRADO", "SÍNTESIS",
                        "SINTESIS", "ARQUITECTURA")


def componente_iv():
    dir_ev = os.path.join(RAIZ, "docs/evolucion")
    salida, sin_clasificar = [], []
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
        elif not any(v in cabecera for v in VOCES_DE_NO_DICTAMEN):
            sin_clasificar.append((rel, " ".join(cabecera.split())[:90]))
    if sin_clasificar:
        raise SedeIlegible(
            "el componente (iv) NO sabe clasificar %d documento(s) numerado(s): %r. Un "
            "documento que no case con ninguna de las dos listas de voces se caía del "
            "universo EN SILENCIO, que es exactamente lo que `1bis` prohíbe. Dígase si es "
            "dictamen —`VOCES_DE_DICTAMEN`— o no lo es —`VOCES_DE_NO_DICTAMEN`—: el "
            "derivador no lo adivina" % (len(sin_clasificar), sin_clasificar))
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
    ("docs/evolucion/verificacion/derivar-universo-obligatorio.py",
     "C-L.5 1bis · el comando auditable que deriva ESTE universo, juzgándose a sí mismo"),
    ("docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md",
     "C-L.5 · el manifiesto previo del gate del documento 21, inmutable"),
    ("docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md",
     "C-L.5 · el manifiesto previo del gate del documento 22, inmutable"),
    ("docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md",
     "C-L.5 · el addendum que reasignó 21 fuentes mal agotadas, inmutable"),
    ("docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md",
     "las cinco entradas que acotan dictámenes que no se editan"),
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
    """El objeto que ESTE gate juzga — CON GUARDA sobre su propia declaración.

    `ENCARGO` es lo único escrito a mano de todo el derivador, y por eso es lo único que
    hay que vigilar aquí: una fila sin cláusula no dice por qué está, y una ruta repetida
    infla el universo sin ampliarlo. Ninguna de las dos se detectaba.
    """
    if not ENCARGO:
        raise SedeIlegible("el componente (v) está VACÍO: un gate sin objeto declarado no "
                           "tiene universo, y un universo que encoge por omisión es el "
                           "defecto de `P-08`")
    sin_clausula = [r for r, c in ENCARGO if not (c or "").strip()]
    if sin_clausula:
        raise SedeIlegible("el componente (v) trae filas sin cláusula del encargo: %r. Sin "
                           "cláusula no entra: la cláusula es lo que se lee en el informe"
                           % sin_clausula)
    rutas = [r for r, _ in ENCARGO]
    repetidas = sorted({r for r in rutas if rutas.count(r) > 1})
    if repetidas:
        raise SedeIlegible("el componente (v) repite rutas: %r" % repetidas)
    for rel in rutas:
        if not os.path.isfile(os.path.join(RAIZ, rel)):
            raise SedeIlegible("el componente (v) nombra %s y no existe en el árbol" % rel)
    return rutas


COMPONENTES = [
    ("i", "las fuentes de «QUÉ HAY QUE LEER ÍNTEGRO» de `C-L.5`", componente_i),
    ("ii", "las fuentes y las fichas de `C-0.1` / `C-0.2`", componente_ii),
    ("iii", "documento 11 · registro de decisiones · checkpoint", componente_iii),
    ("iv", "todo dictamen de gate anterior", componente_iv),
    ("v", "el objeto que ESTE gate juzga, según su encargo", componente_v),
]


# ── la promesa de la cabecera, EJECUTADA: «nunca reduce el universo en silencio» ─────
#
# `T-15`. La promesa cubría la MANIPULACIÓN y no la OMISIÓN: **borrar una fila del `ENCARGO`
# reducía el universo en uno con `exit 0` y sin un solo aviso** —lo reprodujimos: de 65 a
# 64—, y el adjudicador lo reprodujo antes de 64 a 63. Una promesa que el código no ejecuta
# es una afirmación falsa en el fichero cuya tesis es que el universo no se escribe.
#
# El universo obligatorio de un gate es un CLIQUET: cada manifiesto publicado declaró, con
# fila propia, ruta y SHA-256, las fuentes que aquel gate estaba obligado a cubrir, y esos
# manifiestos son INMUTABLES. Ninguna de esas rutas puede desaparecer del universo derivado
# sin que alguien lo diga: si desaparece, o el derivador encogió o el árbol perdió la
# fuente, y las dos cosas son código 2.
MANIFIESTOS = "docs/evolucion/verificacion/manifiestos"
_FILA_MANIFIESTO = re.compile(
    r"^\|\s*\d+\s*\|\s*`([A-Za-z0-9][-A-Za-z0-9_./]*\.(?:md|py|ya?ml|txt))`\s*\|", re.M)


def universos_publicados():
    """{ruta: [manifiestos que la declararon obligatoria]}, de las sedes INMUTABLES."""
    dir_man = os.path.join(RAIZ, MANIFIESTOS)
    if not os.path.isdir(dir_man):
        raise SedeIlegible("no existe %s: sin manifiestos publicados no hay nada contra lo "
                           "que comprobar que el universo no ha encogido" % MANIFIESTOS)
    publicadas, con_filas = {}, []
    for nombre in sorted(os.listdir(dir_man)):
        if not nombre.endswith(".md"):
            continue
        rutas = set(_FILA_MANIFIESTO.findall(_leer(MANIFIESTOS + "/" + nombre)))
        if rutas:
            con_filas.append(nombre)
        for r in rutas:
            publicadas.setdefault(r, []).append(nombre)
    if not con_filas:
        raise SedeIlegible("ningún manifiesto de %s publica filas de fuente con ruta: el "
                           "cliquet que impide que el universo encoja se quedaría sin sede, "
                           "y una guarda sin sede es un verde por omisión" % MANIFIESTOS)
    return publicadas


def derivar():
    """Devuelve (universo_ordenado, procedencia) o lanza SedeIlegible."""
    procedencia = {}
    for clave, _titulo, fn in COMPONENTES:
        for rel in fn():
            procedencia.setdefault(rel, []).append(clave)
    faltan = [r for r in procedencia if not os.path.isfile(os.path.join(RAIZ, r))]
    if faltan:
        raise SedeIlegible("rutas derivadas que NO existen en el árbol: %r" % sorted(faltan))
    perdidas = sorted((r, m) for r, m in universos_publicados().items()
                      if r not in procedencia)
    if perdidas:
        raise SedeIlegible(
            "EL UNIVERSO HA ENCOGIDO, y esto es lo que la cabecera promete no hacer en "
            "silencio: %d ruta(s) que un manifiesto INMUTABLE declaró obligatoria(s) ya no "
            "salen de ningún componente: %r. O una fila del `ENCARGO` se ha borrado, o una "
            "sede ha dejado de nombrarla. Quien la quite responde de ello, y lo dice aquí"
            % (len(perdidas), perdidas))
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
