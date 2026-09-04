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
        SEDE: el bloque `ENCARGO` de abajo —ruta a ruta— **y `ZONAS_DEL_ENCARGO`, que mete
        DIRECTORIOS ENTEROS y los BARRE del árbol**, cada uno con su cláusula. Es lo único
        que cambia de un gate a otro, y por eso está declarado y anotado en vez de inferido
        GUARDA: ninguna fila sin cláusula, ninguna ruta repetida y ninguna inexistente; y
        ninguna zona vacía ni sin sus anclas
        `AA-01`. `docs/owner/` entraba como UNA RUTA LITERAL. Un SEGUNDO documento del
        Owner, añadido por la vía que el corpus sanciona —enlazado desde `00-INDICE.md`—,
        que declara `F4c` cerrada y `F5` autorizada, quedaba fuera del universo, del
        manifiesto y del sobre, en `38/38` verde. **El perímetro se DERIVA, no se enumera**:
        `docs/owner/` y `manifiestos/` entran ENTEROS

FALLA CERRADO
-------------
Si una sede no se puede leer, si un recuento derivado no coincide con el que su sede
declara, o si una ruta derivada no existe en el árbol, **sale con código 2 y diagnóstico**.
Nunca adivina y nunca reduce el universo en silencio: un universo que encoge sin decirlo es
exactamente el defecto que `P-08` describió. **Y eso se EJECUTA, no se promete**, en cuatro
puntos:

  · toda ruta que un manifiesto INMUTABLE declaró obligatoria tiene que seguir saliendo de
    algún componente — el cliquet de `universos_publicados()`;
  · **cada manifiesto tiene que aportar filas a ese cliquet** (`W2-03`): el lector exigía
    columna ordinal y el manifiesto del gate del documento 21 no la tiene, con lo que uno de
    los manifiestos inmutables aportaba CERO filas y **las rutas que aquel gate declaró
    obligatorias** no estaban protegidas. La guarda de entonces sólo miraba el total y no
    podía disparar. **`C-12` del OCTAVO GATE: aquí y en su gemela de abajo se escribía «30
    rutas», y el patrón `_FILA_MANIFIESTO` de este mismo fichero deriva OTRO número. Los dos
    cardinales se retiran y se remiten** —nunca se sustituye un número a mano por otro
    número a mano, que es lo que `J-07` prohíbe—: quien lo necesite lo deriva contando las
    filas de ese manifiesto con el patrón que este fichero publica;
  · un documento numerado que el componente (iv) no sepa clasificar para el derivador entero
    en vez de caerse del universo;
  · y **un documento numerado cuyo NOMBRE dice dictamen no se excluye por su H1** (`W2-06`):
    retitularlo lo sacaba del universo con `exit 0`.

**Y LO QUE ESTE FICHERO NO CIERRA, DICHO AQUÍ Y NO CALLADO** (`Z-08`): un documento numerado
NUEVO cuyo H1 lleve una voz de NO-DICTAMEN y cuyo NOMBRE no diga dictamen —
`25-SÍNTESIS-DEL-CIERRE.md` con un veredicto dentro— **sale del universo con `rc=0`**. La
guarda de `W2-06` cierra el caso en que el NOMBRE lo delata, y no éste. Lo que sí se ha
cerrado es que **deje de ser silencioso**: `EXCLUIDOS_IV` se publica con su H1 en TODOS los
modos —también en `--rutas`, que es el único que invocan el emisor y la RECETA, y donde
antes `main()` retornaba antes de imprimirlo (`Z-13`)—, y el SOBRE DE ANCLA lo copia. Un
universo que encoge lo dice, y lo dice por el camino que se audita.

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
import textwrap

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
MANIFIESTOS = "docs/evolucion/verificacion/manifiestos"


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
    except UnicodeDecodeError as e:
        # `EE-09`. Este `except` sólo capturaba `OSError`, y la cabecera de este fichero
        # promete FALLAR CERRADO ante una sede ilegible. Una sede que EXISTE y se abre pero
        # **no decodifica como UTF-8** levantaba `UnicodeDecodeError`, que no es `OSError`:
        # el proceso moría con traza y `rc=1` **sin el diagnóstico `FALLA CERRADO`**, y la
        # receta del sobre —que canaliza `--rutas` con `2>/dev/null`— entregaba una lista
        # VACÍA en silencio. Ilegible es ilegible, venga del sistema de ficheros o del
        # códec, y es la misma clase que `T-22` cerró en el fichero de al lado.
        raise SedeIlegible("sede %s ilegible: no decodifica como UTF-8 (%s). Una sede que "
                           "el corpus no puede leer no se interpreta: se falla cerrado"
                           % (rel, e))


# `Z1-03`≡`Z-05`. Se excluía `__pycache__` POR SU NOMBRE DE DIRECTORIO, con lo que una copia
# de una sede dentro de él era invisible para el resolutor y la resolución seguía siendo
# «única» con dos ficheros iguales en el árbol. Se excluyó entonces por lo que un fichero
# ES: `.git`, que no es corpus, y el bytecode, por su extensión.
#
# `DD-01` · **EL OCTAVO ÁRBOL, y «por su extensión» NO ES «por lo que ES».** El adjudicador
# del QUINTO GATE lo midió: un documento que declara `F4c` cerrada y `F5` autorizada,
# nombrado `<algo>.pyc` bajo `docs/owner/`, **alcanza el commit**, deja `git status` vacío,
# pasa 38/38 y 13/13, **no entra en el universo, no recibe fila ni revisor, no aparece en
# `EXCLUIDOS_IV` y produce el digest del sobre BIT A BIT IDÉNTICO**. Y `.git` se excluía
# **por nombre y a cualquier profundidad**, evaluando la poda sobre el NOMBRE DESNUDO del
# directorio: un `docs/.git/` cualquiera desaparecía del corpus sin decirlo.
#
# **El perímetro pasa a ser DOS predicados, y los dos son por NATURALEZA:**
#
#   · `.git` **ANCLADO A LA RAÍZ de la ruta relativa** —`^\.git(/|$)`—, y la poda se
#     evalúa **sobre la RUTA COMPLETA**, nunca sobre el nombre desnudo. Es el almacén
#     contra el que se compara, y sólo lo es el de la raíz.
#   · el bytecode, **POR SU CONTENIDO**: cabecera de CPython y no-texto. El SUFIJO ya no
#     excluye nada, de modo que `sentencia.pyc` con un H1 dentro es corpus, entra en el
#     universo, recibe fila y revisor, y `G-29` lo ve.
#
# **Y mientras algo quede fuera, se PUBLICA con su ruta**: `EXCLUIDOS_PERIMETRO` lo emite
# por todos los modos, como `EXCLUIDOS_IV` hace con el componente (iv). Una exclusión
# silenciosa es la puerta; una exclusión publicada es una línea que el revisor lee.
#
# `S1-04` · **Y AQUÍ SE DICE EL ALCANCE EXACTO DE ESA PROMESA, porque decirla entera era
# falso.** Este predicado se evalúa **donde el derivador RECORRE el árbol** —el resolutor
# de nombres y el barrido de las zonas del `ENCARGO`—, y el derivador **no recorre el árbol
# entero**: recorre lo que su `1bis` le manda mirar. Por tanto `EXCLUIDOS_PERIMETRO`
# publica **todo lo que este derivador excluye de su universo**, y NO «todo lo que hay
# fuera del universo»: un fichero que el `1bis` nunca alcanza no está excluido por el
# perímetro — está fuera del encargo, que es otra cosa y la dice el propio `1bis`.
# **Quien quiera la diferencia entre el árbol y el universo no la busca aquí**: la da
#     comm -13 <(python3 …/derivar-universo-obligatorio.py --rutas | sort) \
#              <(git ls-tree -r --name-only HEAD | sort)
# El séptimo gate midió que la promesa anterior —«todo lo excluido»— era más ancha que el
# código, y es la sexta condición de `O18`: ninguna promesa de garantía superior a la
# entregada. Se acota la promesa en vez de fingir que el derivador barre lo que no barre.
_EXCLUIDO_RAIZ = re.compile(r"^\.git(?:/|$)")

# Los excluidos por PERÍMETRO, con su ruta y su motivo. Se publica, no se supone.
EXCLUIDOS_PERIMETRO = []


def _es_bytecode(ruta_abs):
    """¿El fichero cumple el PREDICADO DE BYTECODE? Por CONTENIDO, no por sufijo.

    EL PREDICADO, dicho como se ejecuta y sin prometer nada más (`S1-05`):
      · los bytes 3 y 4 son `\r\n`
      · el byte 2 es menor que `0x20`
      · el contenido **no decodifica como UTF-8**

    `S1-05`. La versión anterior añadía que ningún documento «puede fabricarse para
    parecerlo sin dejar de ser ilegible como texto», y **eso es falso y está medido**: un
    documento legible en Latin-1 —o en cualquier codificación de un solo byte— satisface
    las tres condiciones y sigue siendo perfectamente legible para una persona. La
    imposibilidad se retira; el predicado se queda, porque para lo que existe —que el
    SUFIJO no decida— sirve, y el motivo publicado dice ahora lo que se comprobó y no lo
    que se supone.
    """
    try:
        with io.open(ruta_abs, "rb") as fh:
            cabecera = fh.read(4)
            resto = fh.read(65536)
    except OSError:
        return False
    if len(cabecera) < 4 or cabecera[2:4] != b"\r\n" or cabecera[1] > 0x1F:
        return False
    try:
        (cabecera + resto).decode("utf-8")
    except UnicodeDecodeError:
        return True
    return False


def _excluido(rel):
    """¿`rel` queda FUERA del perímetro? Por NATURALEZA, y registrando por qué."""
    if _EXCLUIDO_RAIZ.match(rel):
        motivo = "`.git` de la RAÍZ: almacén, no corpus"
    elif _es_bytecode(os.path.join(RAIZ, rel)):
        motivo = ("cumple el PREDICADO DE BYTECODE por CONTENIDO —cabecera `\\r\\n`, byte "
                  "alto pequeño y no-UTF-8—; NO se afirma que sea bytecode de CPython, que "
                  "es lo que el predicado no puede decidir (`S1-05`)")
    else:
        return False
    if (rel, motivo) not in EXCLUIDOS_PERIMETRO:
        EXCLUIDOS_PERIMETRO.append((rel, motivo))
    return True


def _podar(base, dirs):
    """Poda de `os.walk` evaluada sobre la RUTA COMPLETA, no sobre el nombre desnudo."""
    vivos = []
    for d in dirs:
        rel = os.path.relpath(os.path.join(base, d), RAIZ).replace(os.sep, "/")
        if _EXCLUIDO_RAIZ.match(rel):
            if (rel + "/", "`.git` de la RAÍZ: almacén, no corpus") not in EXCLUIDOS_PERIMETRO:
                EXCLUIDOS_PERIMETRO.append((rel + "/", "`.git` de la RAÍZ: almacén, no corpus"))
            continue
        vivos.append(d)
    dirs[:] = vivos


def _resolver(nombre):
    """Un nombre de fichero suelto a su ruta única en el árbol. Falla si no es única."""
    encontrados = []
    for base, dirs, ficheros in os.walk(RAIZ):
        _podar(base, dirs)
        if nombre in ficheros:
            rel = os.path.relpath(os.path.join(base, nombre), RAIZ).replace(os.sep, "/")
            if not _excluido(rel):
                encontrados.append(rel)
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
                     "ADJUDICACIÓN", "ADJUDICACION", "VEREDICTO",
                     # Añadidas el 2026-09-04. `--rutas` —el ÚNICO modo que invocan el
                     # emisor del sobre y la receta publicada— salía con código 2 desde
                     # antes de esta corrección: `33-CIERRE-DE-F4C-POR-COMPOSICION-O22.md`
                     # no casaba con ninguna de las dos listas, y el derivador se negaba a
                     # adivinar, que es lo correcto. Se resuelve DECLARÁNDOLO, que es lo
                     # que el propio mensaje de fallo pide: un documento que CIERRA una
                     # fase por composición de dos juicios independientes, o que RATIFICA
                     # una certificación, es un DICTAMEN. Ampliar esta lista mete más
                     # fuentes en el universo, que es la dirección segura: la que encoge
                     # es la otra.
                     "CIERRE", "RATIFICACIÓN", "RATIFICACION")

VOCES_DE_NO_DICTAMEN = ("ÍNDICE", "INDICE", "BASELINE", "MAPA", "INVARIANTES",
                        "PLAN DE INVESTIGACIÓN", "PLAN DE INVESTIGACION", "INVENTARIO",
                        "CONTRASTE", "DECISIÓN", "DECISION", "DEMOSTRADO", "SÍNTESIS",
                        "SINTESIS", "ARQUITECTURA")


# `W2-06`. La clasificación total cerró el caso «no casa con NINGUNA lista» y dejó abierto el
# contrario, que es el que encoge: **un documento numerado cuyo H1 case con una voz de
# NO-DICTAMEN sale del universo con `exit 0` y sin que nadie se entere**. Retitular
# `23-SEGUNDO-GATE-…` como «# ÍNDICE DE …» lo saca del componente (iv) en silencio.
#
# El cliquet lo caza si algún manifiesto INMUTABLE declaró esa ruta; no lo caza para un
# dictamen NUEVO, que es justamente el que nadie ha leído. La guarda que sí lo cierra no
# necesita sede nueva: **el NOMBRE del fichero es la otra sede, y ya está en el árbol.** Un
# documento cuyo NOMBRE dice dictamen no puede excluirse por su H1. Al revés no se exige,
# porque hay nombres que no clasifican —`05-CANDIDATOS.md`, `08-EVIDENCIA-MULTIREPO.md`— y
# la regla sólo tiene que ser cerrada en la dirección que encoge.
#
# Y las exclusiones dejan de ser invisibles: `EXCLUIDOS_IV` las publica con su H1, y la
# salida de tabla las imprime. Un universo que encoge lo dice.
EXCLUIDOS_IV = []


def _voz(texto):
    if any(v in texto for v in VOCES_DE_DICTAMEN):
        return "dictamen"
    if any(v in texto for v in VOCES_DE_NO_DICTAMEN):
        return "no-dictamen"
    return None


def componente_iv():
    dir_ev = os.path.join(RAIZ, "docs/evolucion")
    salida, sin_clasificar, discrepan = [], [], []
    del EXCLUIDOS_IV[:]
    for nombre in sorted(os.listdir(dir_ev)):
        if not re.match(r"^\d\d-.*\.md$", nombre):
            continue
        rel = "docs/evolucion/" + nombre
        cabecera = ""
        for linea in _leer(rel).split("\n"):
            if linea.startswith("# "):
                cabecera = linea.upper()
                break
        titulo = " ".join(cabecera.split())[:90]
        por_h1 = _voz(cabecera)
        por_nombre = _voz(nombre.upper().replace("-", " ").replace(".", " "))
        if por_h1 == "dictamen":
            salida.append(rel)
        elif por_nombre == "dictamen":
            discrepan.append((rel, titulo))
        elif por_h1 == "no-dictamen":
            EXCLUIDOS_IV.append((rel, titulo))
        else:
            sin_clasificar.append((rel, titulo))
    if discrepan:
        raise SedeIlegible(
            "el componente (iv) iba a EXCLUIR del universo %d documento(s) cuyo NOMBRE dice "
            "que son dictamen y cuyo H1 ya no lo dice: %r. Un dictamen que se cae del "
            "universo porque le han cambiado el título es el encogimiento silencioso que "
            "`1bis` prohíbe, y el cliquet sólo lo caza si algún manifiesto INMUTABLE lo "
            "declaró — para el dictamen NUEVO, que es el que nadie ha leído, no hay red. "
            "Córrijase el H1, o renómbrese el fichero: las dos cosas las firma alguien"
            % (len(discrepan), discrepan))
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
#
# Cada fila declara la cláusula del encargo que la mete en el universo. Sin cláusula no
# entra, y la cláusula se lee en el informe del gate.
#
# `H-13`. Estas cláusulas describían el OCTAVO gate —«los 24 hallazgos del documento 21»,
# «el sobre que este gate ESTRENA»— mucho después de que ese gate cerrara, y un encargo
# caducado es una sede que miente sin ponerse en rojo: las RUTAS seguían siendo las
# correctas, de modo que nada fallaba y el revisor leía un motivo que ya no era el suyo.
# Se actualiza **el texto**, y sólo el texto: ni una ruta cambia, ni la lógica que las
# consume. El encargo vigente es el del gate posterior a `O20` y `O21`.
ENCARGO = [
    ("docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md",
     "la sede que origina M-04 y las condiciones C-L · el criterio que los gates "
     "posteriores heredan y no pueden ablandar"),
    ("docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py",
     "M-04 como proposición general · que ninguna deuda de F6 se presente como "
     "implementada · rótulos que atribuyen a una resolución una regla que no dictó"),
    ("docs/evolucion/verificacion/README.md",
     "lo que la batería declara de sí misma, frente a lo que hace"),
    ("docs/evolucion/verificacion/derivar-universo-obligatorio.py",
     "C-L.5 1bis · el comando auditable que deriva ESTE universo, juzgándose a sí mismo"),
    ("docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md",
     "las entradas que acotan dictámenes que no se editan"),
    ("docs/evolucion/verificacion/emitir-sobre-de-ancla.py",
     "O18 · C-20 · si el sobre transporta MATERIALMENTE el texto íntegro de la "
     "ratificación O19 y no sólo sus digest"),
    ("docs/evolucion/00-INDICE.md",
     "catálogo y contratos duplicados · cardinales escritos donde la propia cabecera "
     "ordena derivar"),
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
     "contratos C1-C7 · Git ausente · gobierno de ramas · que PesquerApp siga bloqueada"),
    ("docs/rediseno/a-CAPACIDADES-APROBADA.md",
     "material APROBADO (a) · PN-15 y PN-16 se derogan o no contra él"),
    ("docs/rediseno/b-RECORRIDO-APROBADA.md",
     "material APROBADO (b) · L836, la grafía canónica que origina PN-16"),
    ("docs/rediseno/a-ENMIENDA-E1-ENC.md", "material APROBADO E1"),
    ("docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md", "material APROBADO E2"),
    ("docs/rediseno/CHECKPOINT-OPERATIVO.md",
     "la batería del kernel, el runner y las trece evidencias"),
]

# ── las ZONAS que el encargo mete ENTERAS, y se BARREN ───────────────────────────
#
# `AA-01`. `docs/owner/` estaba en el `ENCARGO` como **una ruta literal escrita a mano**
# —`("docs/owner/ADS-OWNER-RESOLUCIONES.md", …)`—, y el adjudicador midió la consecuencia:
# un SEGUNDO documento del Owner, añadido **por la vía que el corpus sanciona** —enlazado
# desde `00-INDICE.md`—, que declara `F4c` cerrada y `F5` autorizada, pasa la batería en
# `38/38` commiteado y sin commitear y queda **fuera del universo obligatorio, sin fila de
# manifiesto, sin revisor asignado y sin huella en el sobre**. No explota ningún defecto:
# `G-29` admite en esa zona un conjunto ABIERTO —porque `O19` obligó a abrirla— y el
# derivador enumeraba un conjunto CERRADO de UNO. El aparato que `O19` creó para que la
# autoridad del Owner fuera comprobable anclaba UN NOMBRE DE FICHERO.
#
# `Z2-02`≡`Z-03`, la otra mitad: los manifiestos también estaban escritos fila a fila, y el
# del propio gate en curso **no estaba en ninguna**. Borrar un manifiesto y su fila del
# `ENCARGO` sacaba del universo la sede canónica del Owner con `rc=0`.
#
# **El perímetro se DERIVA, no se enumera.** Cada zona declara su directorio y su cláusula;
# el contenido sale del árbol. Un documento nuevo del Owner entra SOLO el día que se
# publica, y no hay fila que borrar. Se exigen las ANCLAS: una zona vacía, o una zona que
# haya perdido el fichero que su cláusula nombra, es código 2 — un universo que encoge lo
# dice, y aquí lo dice con el nombre delante.
ZONAS_DEL_ENCARGO = [
    ("docs/owner",
     ("docs/owner/ADS-OWNER-RESOLUCIONES.md",),
     "O19 · la ZONA del Owner ENTERA, barrida y no enumerada: la SEDE CANÓNICA de sus "
     "resoluciones, que el sobre de ancla ancla y cuya huella el revisor recibe FUERA del "
     "árbol antes de leer, y todo documento que el Owner publique junto a ella. `AA-01`: "
     "anclar la ruta literal de la sede dejaba fuera del universo, del manifiesto y del "
     "sobre a cualquier segundo documento del Owner añadido por la vía sancionada"),
    (MANIFIESTOS,
     (),
     "C-L.5 · los manifiestos de asignación INMUTABLES, barridos y no enumerados. Son la "
     "sede del cliquet que impide que el universo encoja, y el del gate EN CURSO no estaba "
     "en ninguna fila escrita: `Z2-02` borró un manifiesto y su fila y la sede canónica del "
     "Owner desapareció del universo con `rc=0`"),
]


def _barrer(zona):
    """Las rutas del corpus bajo `zona`, ordenadas. Excluye por NATURALEZA, no por sitio."""
    raiz_zona = os.path.join(RAIZ, zona)
    if not os.path.isdir(raiz_zona):
        raise SedeIlegible(
            "la zona `%s` que el `ENCARGO` mete ENTERA en el universo no existe en el "
            "árbol: un universo que encoge porque una zona desapareció es exactamente lo "
            "que `1bis` prohíbe" % zona)
    rutas = []
    for base, dirs, ficheros in os.walk(raiz_zona):
        _podar(base, dirs)
        for nombre in sorted(ficheros):
            rel = os.path.relpath(os.path.join(base, nombre), RAIZ).replace(os.sep, "/")
            if not _excluido(rel):
                rutas.append(rel)
    return sorted(rutas)


def zonas_del_encargo():
    """Las rutas de las zonas que el encargo mete enteras, con sus anclas EXIGIDAS."""
    salida = []
    for zona, anclas, clausula in ZONAS_DEL_ENCARGO:
        if not (clausula or "").strip():
            raise SedeIlegible("la zona `%s` entra sin cláusula del encargo: sin cláusula "
                               "no entra" % zona)
        rutas = _barrer(zona)
        if not rutas:
            raise SedeIlegible(
                "la zona `%s` del `ENCARGO` sale VACÍA del barrido: un universo vacío por "
                "no mirar es el defecto que `P-08` describió, y aquí lo sería sobre la zona "
                "que el gate está obligado a cubrir" % zona)
        faltan = [a for a in anclas if a not in rutas]
        if faltan:
            raise SedeIlegible(
                "la zona `%s` ya no contiene %r, que su cláusula del `ENCARGO` nombra como "
                "ancla. O la ruta se movió, o el árbol la ha perdido, y las dos cosas se "
                "responden aquí en vez de callarse" % (zona, faltan))
        salida.extend(rutas)
    return salida


def componente_v():
    """El objeto que ESTE gate juzga — CON GUARDA sobre su propia declaración.

    `Z2-07`≡`Z-14`. Aquí decía «`ENCARGO` es **lo único** escrito a mano de todo el
    derivador», y era falso: `VOCES_DE_DICTAMEN` (16) y `VOCES_DE_NO_DICTAMEN` (15) son
    listas escritas **de las que depende la pertenencia al componente (iv)** —un dictamen
    nuevo entra o sale del universo por ellas—, y `ARQ`, `BATERIA`, `DECISIONES`,
    `CHECKPOINT` y `MANIFIESTOS` son cinco rutas fijas. **Lo escrito a mano en este fichero
    es, dicho entero: `ENCARGO`, `ZONAS_DEL_ENCARGO`, las dos listas de voces y esas cinco
    rutas.** Todo lo demás se lee de una sede o se barre del árbol.

    Lo que se vigila aquí: una fila sin cláusula no dice por qué está, una ruta repetida
    infla el universo sin ampliarlo, y una ruta que no existe encoge el universo en
    silencio. Ninguna de las tres se detectaba.
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
    for rel in rutas:
        if not os.path.isfile(os.path.join(RAIZ, rel)):
            raise SedeIlegible("el componente (v) nombra %s y no existe en el árbol" % rel)
    # y las ZONAS que el encargo mete ENTERAS, DERIVADAS del árbol y no enumeradas
    rutas = rutas + zonas_del_encargo()
    repetidas = sorted({r for r in rutas if rutas.count(r) > 1})
    if repetidas:
        raise SedeIlegible(
            "el componente (v) repite rutas: %r. Una ruta escrita a mano en `ENCARGO` que "
            "ya sale del barrido de una zona infla el universo sin ampliarlo, y esconde que "
            "la zona ya la cubre: se borra la fila, no se duplica" % repetidas)
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
#
# `Z2-02`≡`Z-03`, Y SE ACOTA LO QUE ESTA GUARDA PRUEBA, porque la promesa era más ancha que
# el mecanismo. **El cliquet protege las rutas que un manifiesto PRESENTE declara.** Su sede
# es un directorio, y un directorio del que se borra un fichero no recuerda que lo tuvo:
# borrar un manifiesto se lleva por delante las filas que ese manifiesto aportaba. Dos cosas
# lo acotan, y son las que hay:
#
#   · el directorio entero es hoy una ZONA DEL ENCARGO y se BARRE: no queda fila que borrar,
#     y el manifiesto del gate EN CURSO —que no estaba en ninguna fila escrita— entra solo;
#   · **quien caza el borrado del fichero es la BATERÍA, no esto**: `G-22` contrasta el
#     inventario de inmutables contra `HEAD` y contra la revisión base, y `G-29` da ROJO por
#     «fichero del corpus DESAPARECIDO». Este derivador **no puede** hacerlo: se ejecuta
#     también sobre un árbol desplegado FUERA del repositorio, sin `.git`, que es como lo
#     invocan el emisor del sobre y la RECETA publicada.
#
# Se dice aquí para que nadie vuelva a leer en esta guarda una garantía que no da.
# `W2-03`. El patrón exigía COLUMNA ORDINAL —`| 7 | \`ruta\` |`— y el manifiesto del gate
# del documento 21 no la tiene: su tabla empieza por la ruta. Resultado medido sobre el
# árbol, sin que nadie atacara nada: **de los manifiestos INMUTABLES, uno aportaba CERO
# filas al cliquet**, y **las rutas que aquel gate declaró obligatorias** no estaban
# protegidas contra el encogimiento —el cardinal se retira por `C-12`, y se deriva contando
# las filas de ese manifiesto con `_FILA_MANIFIESTO`—. La guarda que existía —«ningún manifiesto publica
# filas»— sólo miraba el total, y con cuatro manifiestos aportando filas nunca disparaba.
# Ahora la ruta puede ir en la primera o en la segunda celda, y **cada manifiesto tiene que
# aportar filas**: uno que no aporte ninguna es código 2 con su nombre.
_FILA_MANIFIESTO = re.compile(
    r"^\|\s*(?:\d+\s*\|\s*)?`([A-Za-z0-9][-A-Za-z0-9_./]*\.(?:md|py|ya?ml|txt))`\s*\|", re.M)


def universos_publicados():
    """{ruta: [manifiestos que la declararon obligatoria]}, de las sedes INMUTABLES."""
    dir_man = os.path.join(RAIZ, MANIFIESTOS)
    if not os.path.isdir(dir_man):
        raise SedeIlegible("no existe %s: sin manifiestos publicados no hay nada contra lo "
                           "que comprobar que el universo no ha encogido" % MANIFIESTOS)
    publicadas, con_filas, sin_filas = {}, [], []
    for nombre in sorted(os.listdir(dir_man)):
        if not nombre.endswith(".md"):
            continue
        rutas = set(_FILA_MANIFIESTO.findall(_leer(MANIFIESTOS + "/" + nombre)))
        (con_filas if rutas else sin_filas).append(nombre)
        for r in rutas:
            publicadas.setdefault(r, []).append(nombre)
    if not con_filas:
        raise SedeIlegible("ningún manifiesto de %s publica filas de fuente con ruta: el "
                           "cliquet que impide que el universo encoja se quedaría sin sede, "
                           "y una guarda sin sede es un verde por omisión" % MANIFIESTOS)
    if sin_filas:
        raise SedeIlegible(
            "%d manifiesto(s) INMUTABLE(s) de %s no aportan NI UNA fila al cliquet: %r. Un "
            "manifiesto es la sede que declaró qué fuentes eran obligatorias en su gate; si "
            "el lector no las ve, esas rutas pueden desaparecer del universo sin que nada lo "
            "diga, y la guarda del total no lo nota mientras los demás manifiestos aporten "
            "filas. O la tabla ha cambiado de forma, o el fichero no es un manifiesto: las "
            "dos cosas se responden, no se callan" % (len(sin_filas), MANIFIESTOS, sin_filas))
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


def lineas_de_blob(crudo):
    """Líneas de un blob. Sede de la fórmula (`S1-08`), con su alcance dicho (`C-11`).

    Un fichero vacío tiene CERO líneas.

    **ALCANCE EXACTO, y decirlo entero era falso.** `EE-16` cerró la divergencia escribiendo
    una TERCERA copia y afirmando «se usa UNA»; `S1-08` hizo que el emisor la IMPORTARA en
    su cálculo del universo y **volvió a afirmar «ÚNICA SEDE»** — y el octavo gate midió que
    el emisor sigue calculando líneas por su cuenta en otros dos sitios, uno de los cuales
    PUBLICA las cifras de las resoluciones del Owner en el sobre. Hoy esta función es la
    sede de la fórmula **para el universo obligatorio**, y **no se afirma que sea la única
    del corpus**: unificar los tres usos es trabajo de `F6` y va contratado en `V6-04` de
    §20 del documento 11. La divergencia está acotada —los tres dan el mismo resultado sobre
    todo fichero no vacío— y **declarada**, que es lo que la sexta condición de `O18` exige.
    """
    n = crudo.count(b"\n")
    if crudo and not crudo.endswith(b"\n"):
        n += 1
    return n


def metricas(rel):
    ruta = os.path.join(RAIZ, rel)
    with io.open(ruta, "rb") as fh:
        crudo = fh.read()
    return lineas_de_blob(crudo), hashlib.sha256(crudo).hexdigest()


def _excluidos(destino):
    """Publica lo que queda FUERA. Se emite por TODOS los modos.

    Dos listas, y las dos con su RUTA: la del componente (iv) —voz de NO-DICTAMEN en el
    H1— y la del PERÍMETRO —`DD-01`—. Mientras algo se excluya, se dice cuál y por qué:
    una exclusión silenciosa es el octavo árbol.
    """
    destino.write("\n  (iv) EXCLUIDOS por voz de NO-DICTAMEN en su H1: %d\n"
                  % len(EXCLUIDOS_IV))
    for rel, titulo in EXCLUIDOS_IV:
        destino.write("        %-46s %s\n" % (rel.split("/")[-1], titulo))
    destino.write("\n  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: %d\n"
                  % len(EXCLUIDOS_PERIMETRO))
    for rel, motivo in sorted(EXCLUIDOS_PERIMETRO):
        destino.write("        %-60s %s\n" % (rel, motivo))



# ════════════════════════════════════════════════════════════════════════════════
#  EL UNIVERSO DE OBLIGACIONES DE `F6`, Y LAS TRES RESTAS
# ════════════════════════════════════════════════════════════════════════════════
#
# POR QUÉ SE AÑADE AQUÍ, Y NO EN OTRO FICHERO. Lo que este derivador ya hacía era derivar el
# universo de FUENTES que un gate debe leer. Lo que faltaba —y es lo que `F6-H` declaró
# completo sin tenerlo— es el universo de OBLIGACIONES que `F6` debe cerrar. Son el mismo
# problema y la misma lección: `P-08` encontró que un manifiesto declaraba «FUENTES SIN
# ASIGNAR 0» sobre un universo ELEGIDO A MANO, y el cero era verdadero por construcción.
# `F6-H` se declaró completo sobre un universo que **omitía las cuatro obligaciones de fase
# `F6` de su propia sede** —`11-ARQ` §19—, y el completo era verdadero por la misma razón.
# Dos universos escritos en dos ficheros distintos vuelven a ser dos verdades: va aquí.
#
# LO QUE ESTE MODO GARANTIZA. Que una obligación **no pueda omitirse en silencio**. Cada
# componente se lee de su SEDE NORMATIVA y publica su CARDINAL derivado; si una sede no se
# puede leer, o si un componente sale VACÍO donde su sede declara filas, el modo sale con
# código 2. Nunca adivina y nunca reduce el universo sin decirlo.
#
# LAS TRES RESTAS, y qué significa cada una. Se derivan cruzando el universo contra el
# corpus ejecutable, y **ninguna se escribe a mano**:
#
#   A · obligaciones internas SIN IMPLEMENTACIÓN
#       ninguna prueba del corpus la declara en su `cubre`, o las que la declaran no
#       nombran validador. Nadie ha construido nada que la cierre.
#
#   B · implementadas SIN PRUEBA CAPAZ DE FALLAR
#       tienen prueba y validador, y NINGUNA infracción deliberada del catálogo de
#       `comprobar_negativos` apunta a esa prueba. Una prueba que sólo se ha visto pasar no
#       está verificada: es el defecto exacto que la auditoría independiente encontró en
#       `T131` y `T134`.
#
#   C · obligaciones SIN TRAZABILIDAD HASTA EVIDENCIA EJECUTABLE
#       tienen prueba y validador, y ninguna de sus pruebas declara un fichero de evidencia
#       que exista en el árbol. La cadena obligación → código → prueba → evidencia se corta
#       antes del último eslabón, que es el único que un tercero puede reejecutar.

KERNEL_PRUEBAS = "kernel/operativo"
VALIDADORES = "kernel/operativo/validadores"
DEUDA = "docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md"
ESTADO_DURABLE = "docs/rediseno/g-ESTADO-DURABLE-APROBADA.md"


# ===========================================================================
#  `ADJ-G1` · LAS GUARDAS DEL UNIVERSO DE OBLIGACIONES
# ===========================================================================
#  EL HECHO, reproducido por el adjudicador del gate del 2026-09-04 y vuelto a reproducir
#  aquí antes de tocar una línea. `--obligaciones` ENCOGÍA CON `exit 0` por TRES vías:
#
#      10a  cambiar la FASE de la fila `F-07` de `**F6**` a `**F5**`
#           EXIT=0 · (F-nn) 7 · TOTAL 57 · `grep F-07` en la salida → 0
#      10e  retirar la fila `F-10` entera
#           EXIT=0 · (F-nn) 6 · TOTAL 56 · `grep F-10` en la salida → 0
#      10d  retirar el bloque `--- CONTRATO 2 · AMPLIAR T152 … ---` de §19
#           EXIT=0 · (§19) 4 · TOTAL 57 · `CONTRATO 2` en la salida → 0
#
#  Y LA CAUSA no eran tres descuidos: era UNA CLASE. Los suelos estaban ESCRITOS —`< 4`
#  con cinco reales, `< 19`, `!= 16`, `!= 3`— y el componente `F-nn` no tenía suelo
#  ninguno: su guarda sólo disparaba con CERO filas. La cabecera de este fichero promete
#  «nunca reduce el universo en silencio», y para `--obligaciones` no se cumplía.
#
#  DECISIÓN · el suelo del universo NO se escribe: se DERIVA, y por DOS vías distintas
#      Alternativas: (a) subir los cardinales escritos a su valor de hoy; (b) publicar un
#      fichero-cliquet con la lista de obligaciones y compararse contra él; (c) derivar el
#      suelo de propiedades que el propio corpus ya publica.
#      Se descarta (a): es lo que ya había, y caduca en la obligación siguiente —de hecho
#      YA había caducado, y ésa es la unidad de holgura que el adjudicador midió—.
#      Se descarta (b): un fichero-cliquet es una sede nueva que hay que mantener a mano, y
#      quien borra la obligación puede borrar su fila; el cliquet de FUENTES funciona
#      porque sus manifiestos son INMUTABLES y hay una batería que caza su borrado, y aquí
#      no existe ni lo uno ni lo otro.
#      Se elige (c), con dos vías que fallan por motivos distintos:
#        · CONSECUTIVIDAD de la numeración que la sede publica. Retirar `CONTRATO 2` deja
#          {1, 3}: un hueco. Retirar `V6-07` deja un hueco. No hace falta saber cuántos
#          «debería» haber, que es justo la cifra que caduca.
#        · CLIQUET DEL CORPUS: toda obligación que el corpus EJERCE —la nombra el `cubre`
#          de un escenario o la `obligacion` de un sabotaje— tiene que seguir en el
#          universo. Cambiar la fase de `F-07` no mueve ninguna numeración, pero `T242` y
#          los sabotajes `N242`, `N242b` y `N242c` la siguen ejerciendo, y una obligación
#          ejercida que ya no está en el universo es una DESAPARICIÓN.
#      MEDIDO sobre el árbol intacto: el cliquet nombra 58 obligaciones y el universo tiene
#      58; la intersección es total y no hay ni una citada de más ni una de menos. No es
#      una promesa: es el control positivo que `T353` ejecuta.
#
#  DECISIÓN · el CRITERIO DE PERTENENCIA de cada componente se DECLARA (`ADJ-M10`)
#      El adjudicador midió que el criterio no es UNO: el componente `deuda` pertenece por
#      FASE y las condiciones `C-L` se separan por SECCIÓN. El resultado es correcto y la
#      frontera no está trazada por la propiedad que dice trazarla. No se homogeneiza a la
#      fuerza —hacerlo metería `C-L` en el universo o sacaría deuda legítima—: se DECLARA,
#      componente a componente, y se PUBLICA en la salida. Una frontera declarada se puede
#      discutir; una supuesta, no.
CRITERIOS_DE_PERTENENCIA = {
    "§19": "por FASE declarada en el bloque del contrato (`FASE **F6**`)",
    "F-nn": "por FASE declarada en la celda de la fila, leída por POSICIÓN y por CONTENIDO",
    "V6": "por ESTRUCTURA: toda fila `V6-nn` de §20 es obligación de `F6` por definición",
    "g": "por ESTRUCTURA: cabecera `## `g.n`` dentro de la ventana 1..16 que la sede enumera",
    # `ADJ-M10` · LA FRONTERA DEL COMPONENTE `C`, DICHA COMO LO QUE ES Y NO COMO LO QUE
    # PARECE. `kernel/operativo/contratos/` publica SIETE contratos —`C1`…`C7`— y este
    # componente se queda con TRES. El criterio no es estructural: es una SELECCIÓN
    # ESCRITA en el patrón `^(C[245])-`, y NINGUNA sede del corpus declara por qué esos
    # tres son los de `F6` y los otros cuatro no. Se dice aquí en vez de dejar que el
    # rótulo «por estructura» lo tape, y va como PETICIÓN al coordinador: mientras no
    # exista sede que lo derive, este componente tiene una frontera que no se puede
    # auditar contra nada.
    "C": "SELECCIÓN ESCRITA `C2`, `C4`, `C5` — sin sede que la derive (PETICIÓN abierta); "
         "los otros cuatro contratos del directorio se publican como excluidos",
    "deuda": "por FASE declarada en la celda de la fila, o en el campo `FASE` de la sección",
}

# La FORMA de un identificador de cada familia. Un identificador que no case NO se admite
# «porque venía de la sede»: una familia nueva o un identificador mal formado son las dos
# maneras de que entre en el universo algo que nadie sabe cruzar con nada.
FORMA_DE_IDENTIFICADOR = {
    "§19": r"CONTRATO \d+(?:bis)?|D104",
    "F-nn": r"F-\d\d",
    "V6": r"V6-\d\d",
    "g": r"g\.\d+",
    "C": r"C[0-9]+",
    "deuda": r"FD-\d+|M-04|A14|E5-\d+|S1-\d+",
}

# El PATRÓN ÚNICO con el que se lee el corpus para el cliquet. Se compone de las formas de
# arriba y no se escribe aparte: dos listas de familias serían dos verdades.
_PATRON_DEL_CLIQUET = re.compile(
    r"(?<![\w.-])(" + "|".join(FORMA_DE_IDENTIFICADOR[c] for c in FORMA_DE_IDENTIFICADOR)
    + r")(?![\w.-])")

# Lo que cada componente deja fuera, CON SU MOTIVO. Una exclusión sin motivo escrito es la
# forma callada de encoger, y `--obligaciones` la publica entera.
EXCLUIDOS_DE_OBLIGACION = []


def _excluir_obligacion(clase, identificador, motivo):
    # ALCANCE DE `--autopruebas`, DICHO: esta guarda y la de identificador duplicado entre
    # componentes NO llevan sabotaje, y no por descuido. Hoy las seis familias son DISJUNTAS
    # POR FORMA, así que ningún estado del CORPUS puede producir un duplicado entre
    # componentes; y ninguna llamada del código deja el motivo vacío. Las dos guardas existen
    # para que AMPLIAR una familia o añadir un componente no vuelva alcanzable ese estado en
    # silencio. Un sabotaje que hubiera que fabricar cambiando este mismo fichero no probaría
    # nada del corpus: probaría que se puede romper el instrumento, que ya se sabe. Se dice
    # en vez de fingir que están probadas.
    if (clase, identificador, motivo) in EXCLUIDOS_DE_OBLIGACION:
        return
    if not motivo:
        raise SedeIlegible(
            "se ha intentado dejar `%s` fuera del componente `%s` SIN MOTIVO ESCRITO. Una "
            "exclusión sin motivo no es una frontera: es un recorte" % (identificador, clase))
    EXCLUIDOS_DE_OBLIGACION.append((clase, identificador, motivo))


def _exigir_identificadores(clase, halladas):
    """Forma, familia y no-vaciedad de lo que un componente deriva. Falla cerrado."""
    forma = re.compile(r"^(?:" + FORMA_DE_IDENTIFICADOR[clase] + r")$")
    ajenos = sorted(i for i in halladas if not forma.match(i))
    if ajenos:
        raise SedeIlegible(
            "el componente `%s` ha derivado %d identificador(es) que NO tienen la forma de "
            "su familia (%s): %r. O la sede ha cambiado de forma, o el barrido está leyendo "
            "otra cosa: las dos se responden, no se callan"
            % (clase, len(ajenos), FORMA_DE_IDENTIFICADOR[clase], ajenos))
    if not halladas:
        # `ADJ-G1` · DISTINGUIR EL VACÍO LEGÍTIMO DEL FALLO DE DERIVACIÓN. Ninguno de los
        # seis componentes puede estar legítimamente vacío —cada uno tiene sede propia y
        # contenido publicado—, así que un conjunto vacío aquí no es «no hay ninguna»: es
        # «no he sabido leerlas», y se dice con esas palabras.
        raise SedeIlegible(
            "el componente `%s` ha derivado CERO obligaciones. Su sede publica contenido y "
            "su criterio de pertenencia es «%s»: un conjunto vacío aquí no es un universo "
            "vacío legítimo, es una derivación que ha dejado de funcionar"
            % (clase, CRITERIOS_DE_PERTENENCIA[clase]))
    return halladas


def _exigir_consecutividad(clase, identificadores, patron):
    """La numeración que la sede publica no puede tener huecos. Suelo DERIVADO."""
    numeros = sorted({int(m.group(1)) for i in identificadores
                      for m in [re.search(patron, i)] if m})
    if not numeros:
        raise SedeIlegible(
            "el componente `%s` no publica ningún identificador numerado con la forma %r: "
            "la lectura de su sede ha dejado de funcionar" % (clase, patron))
    huecos = [n for n in range(numeros[0], numeros[-1] + 1) if n not in numeros]
    if huecos:
        raise SedeIlegible(
            "EL UNIVERSO HA ENCOGIDO. El componente `%s` publica la numeración %r y le "
            "faltan %r: un hueco en la numeración es una obligación que ha desaparecido de "
            "su sede, y este fichero promete no reducir el universo en silencio"
            % (clase, numeros, huecos))
    return numeros


def obligaciones_ejercidas_por_el_corpus():
    """`{obligacion: [quién la ejerce]}` — el CLIQUET, derivado del corpus ejecutable.

    Dos fuentes, las dos del árbol y ninguna escrita a mano: el `cubre` de cada bloque
    `ads:escenario` y la `obligacion` que declara cada `Mutacion` del catálogo de sabotajes.
    Se leen con el MISMO patrón que compone `FORMA_DE_IDENTIFICADOR`, y se buscan DENTRO de
    la celda y no por igualdad: el corpus escribe `g.2 I-g1`, y exigir igualdad exacta
    dejaría `g.2` sin cliquet sin que nadie se enterara.
    """
    ejercidas = {}
    for esc in _escenarios():
        for celda in esc["cubre"]:
            for m in _PATRON_DEL_CLIQUET.finditer(celda):
                ejercidas.setdefault(m.group(1), []).append(esc["id"])
    base = os.path.join(RAIZ, VALIDADORES)
    for nombre in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        if not nombre.endswith(".py"):
            continue
        with io.open(os.path.join(base, nombre), encoding="utf-8") as fh:
            texto = fh.read()
        for m in re.finditer(r'Mutacion\(\s*"([^"]+)"\s*,\s*"([^"]*)"', texto):
            for t in _PATRON_DEL_CLIQUET.finditer(m.group(2)):
                ejercidas.setdefault(t.group(1), []).append(m.group(1))
    return {o: sorted(set(q)) for o, q in sorted(ejercidas.items())}


# EL ALCANCE DEL CLIQUET, DICHO ENTERO Y COMPROBADO — no una promesa, una medición.
#
#     El cliquet exige que toda obligación que el corpus EJERCE siga en el universo. Sobre
#     el árbol intacto eso da 58 ejercidas y 58 en el universo... salvo CINCO identificadores
#     que tienen la FORMA de una familia del universo, que el corpus ejerce de verdad, y que
#     NO son obligaciones de `F6`. Se midieron, no se supusieron:
#
#         C1 · C3 · C6 · C7   contratos transversales de fase ANTERIOR. El componente `C`
#                             selecciona `C2`, `C4` y `C5`, y los otros cuatro existen y se
#                             ejercen desde `F4c` y `F5`
#         S1-01               hallazgo del OCTAVO gate de `F4c`. Su sede es el documento del
#                             gate, no `06-DEUDA`: no es una fila de deuda viva
#
#     DECISIÓN · la excepción se ESCRIBE, y su motivo se COMPRUEBA en cada corrida
#         Alternativas: (a) ensanchar el patrón del cliquet hasta que no las vea —lo que
#         apagaría el cliquet para media familia—; (b) tolerar toda obligación «declarada
#         fuera» —lo que sería el agujero entero, porque un cambio de fase produce
#         exactamente una declaración de fuera y `10a` volvería a pasar—; (c) enumerar las
#         cinco excepciones con su motivo y EXIGIR que el motivo siga siendo cierto.
#         Se elige (c). Una lista de excepciones que nadie comprueba se estira; una que se
#         comprueba en cada corrida no: si `C1-*.md` desaparece del árbol o `S1-01` deja de
#         constar en un documento de gate, la excepción deja de sostenerse y esto FALLA
#         CERRADO en vez de seguir tolerando. Y ampliarla es tocar el INSTRUMENTO, que
#         `V6-11` no deja pasar en la misma pasada que juzga.
FUERA_DEL_CLIQUET = {
    "C1": ("kernel/operativo/contratos", "C1-",
           "contrato transversal de fase ANTERIOR; el componente `C` selecciona C2, C4 y C5"),
    "C3": ("kernel/operativo/contratos", "C3-",
           "contrato transversal de fase ANTERIOR; el componente `C` selecciona C2, C4 y C5"),
    "C6": ("kernel/operativo/contratos", "C6-",
           "contrato transversal de fase ANTERIOR; el componente `C` selecciona C2, C4 y C5"),
    "C7": ("kernel/operativo/contratos", "C7-",
           "contrato transversal de fase ANTERIOR; el componente `C` selecciona C2, C4 y C5"),
    "S1-01": ("docs/evolucion", "29-OCTAVO-GATE",
              "hallazgo del OCTAVO gate de `F4c`; su sede es el documento del gate y no "
              "`06-DEUDA`, luego no es una fila de deuda viva de `F6`"),
}


def _exigir_que_las_excepciones_sigan_siendo_ciertas():
    """Cada excepción del cliquet tiene que seguir sosteniéndose, o esto falla cerrado."""
    for ident, (directorio, prefijo, motivo) in sorted(FUERA_DEL_CLIQUET.items()):
        base = os.path.join(RAIZ, directorio)
        if not os.path.isdir(base) or not [n for n in os.listdir(base)
                                           if n.startswith(prefijo)]:
            raise SedeIlegible(
                "la excepción del cliquet para `%s` decía «%s» y su sede `%s/%s*` ya no "
                "está: una excepción cuyo motivo ha dejado de ser cierto no tolera nada, se "
                "responde" % (ident, motivo, directorio, prefijo))


def _exigir_que_ninguna_desaparezca(universo):
    """`ADJ-G1` · una obligación que el corpus EJERCE no puede caerse del universo."""
    _exigir_que_las_excepciones_sigan_siendo_ciertas()
    ejercidas = obligaciones_ejercidas_por_el_corpus()
    sobrantes = sorted(i for i in FUERA_DEL_CLIQUET if i in universo)
    if sobrantes:
        raise SedeIlegible(
            "%r figuran a la vez en el universo y en las excepciones del cliquet. Una "
            "excepción que ya no hace falta se retira: mientras esté, tolera algo que no "
            "hay que tolerar" % sobrantes)
    desaparecidas = sorted(o for o in ejercidas
                           if o not in universo and o not in FUERA_DEL_CLIQUET)
    if desaparecidas:
        raise SedeIlegible(
            "EL UNIVERSO HA ENCOGIDO, y esto es lo que la cabecera promete no hacer en "
            "silencio: %d obligación(es) que el corpus EJERCE ya no salen de ningún "
            "componente: %s. O una sede ha dejado de declararlas, o han cambiado de fase, o "
            "el barrido ha dejado de verlas. Quien la quite responde de ello, y lo dice aquí"
            % (len(desaparecidas),
               ", ".join("%s (la ejercen %s)" % (o, ", ".join(ejercidas[o][:4]))
                         for o in desaparecidas)))
    return ejercidas


def procedencia_de_los_componentes():
    """Las SEDES de cada componente, con su digest y sus líneas. Se publica, no se supone."""
    sedes = {"§19": (ARQ,), "F-nn": (ARQ,), "V6": (ARQ,), "g": (ESTADO_DURABLE,),
             "C": ("kernel/operativo/contratos/",), "deuda": (DEUDA,)}
    salida = []
    for clase, _titulo, _fn in COMPONENTES_DE_OBLIGACION:
        for rel in sedes[clase]:
            ruta = os.path.join(RAIZ, rel)
            if os.path.isdir(ruta):
                cuantos = len([n for n in sorted(os.listdir(ruta))])
                salida.append((clase, rel, "directorio", "%d ficheros" % cuantos))
                continue
            if not os.path.isfile(ruta):
                raise SedeIlegible(
                    "la sede `%s` del componente `%s` no existe: sin sede no hay derivación, "
                    "y una derivación que no se puede hacer no devuelve un conjunto vacío"
                    % (rel, clase))
            with io.open(ruta, "rb") as fh:
                crudo = fh.read()
            salida.append((clase, rel, hashlib.sha256(crudo).hexdigest()[:16],
                           "%d líneas" % lineas_de_blob(crudo)))
    return salida


def _seccion_19():
    """El cuerpo de §19, acotado por sus dos cabeceras. Falla cerrado si no está."""
    texto = _leer(ARQ)
    marca = "--- CONTRATO 1 · DERIVAR EL CENSO"
    if marca not in texto:
        raise SedeIlegible(
            "`%s` no contiene el bloque de contratos de §19: la sede de las cuatro "
            "obligaciones de fase F6 no se puede leer, y sin ella el universo estaría "
            "incompleto por construcción" % ARQ)
    return texto


def obligaciones_de_19():
    """Las obligaciones de fase `F6` que §19 declara, DESCUBIERTAS por barrido.

    No se enumeran cuatro: se buscan TODOS los bloques `--- CONTRATO n … ---` y la ficha
    `D104`, y se conserva el que declara `FASE F6`. Si §19 añadiera un quinto contrato,
    entraría solo; si retirara uno, el cardinal se movería y se vería.
    """
    texto = _seccion_19()
    halladas = {}
    trozos = re.split(r"^--- (CONTRATO [^·]+?) ·", texto, flags=re.M)
    for i in range(1, len(trozos), 2):
        nombre = trozos[i].strip()
        cuerpo = trozos[i + 1][:4000]
        if re.search(r"FASE\s+\*\*F6\*\*|FASE\s+\*\*F6\.|\bFASE\b[^\n]*\bF6\b", cuerpo):
            halladas[nombre] = "11-ARQ §19 · %s" % nombre
    # La ficha `D104`, que no es un `--- CONTRATO ---` pero es la cuarta obligación.
    if re.search(r"FASE\s+\*\*F6\.\*\*\s+`?D104`?|`D104` fija las cuatro vías", texto):
        halladas["D104"] = "11-ARQ §19 · ficha D104"
    # `ADJ-G1` · EL SUELO SE DERIVA, Y EL CARDINAL ESCRITO SE RETIRA.
    #
    #     HECHO REPRODUCIDO, y es el que el adjudicador midió: la guarda decía
    #     `if len(halladas) < 4` con CINCO obligaciones reales, o sea UNA UNIDAD DE
    #     HOLGURA. Retirar el bloque `--- CONTRATO 2 · AMPLIAR T152 … ---` entero daba
    #     `(§19) 4 · TOTAL 57 · EXIT=0`, y `CONTRATO 2` desaparecía de la salida sin que
    #     nada lo dijera. Un cardinal escrito al lado de su enumeración caduca en cuanto
    #     la enumeración crece, y mientras tanto REGALA holgura.
    #
    #     Lo que lo sustituye son DOS suelos derivados, y ninguno se escribe:
    #       · la CONSECUTIVIDAD de la numeración de los contratos que la sede publica
    #         —de cualquier fase—: retirar el bloque de `CONTRATO 2` deja {1, 3}, que es
    #         un hueco, y el hueco falla cerrado;
    #       · el CLIQUET del corpus (`_exigir_que_ninguna_desaparezca`), que exige que
    #         toda obligación que el corpus EJERCE siga en el universo.
    #     El primero caza la retirada del bloque; el segundo caza el cambio de fase, que
    #     no mueve la numeración. Hacen falta los dos, y por eso están los dos.
    todos = sorted({m.group(1) for m in re.finditer(r"^--- (CONTRATO [^\u00b7]+?) \u00b7",
                                                   texto, re.M)})
    _exigir_consecutividad("§19", todos, r"CONTRATO (\d+)")
    _exigir_identificadores("§19", halladas)
    return halladas


# `H-01` · LAS CELDAS DE UNA FILA MARKDOWN SE PARTEN POR LOS PIPES NO ESCAPADOS
#
#     HECHO REPRODUCIDO. `hallazgos_externos_f6()` partía la fila con `linea.split("|")` y
#     leía la fase en `celdas[5]`. La fila de `F-07` contiene un PIPE ESCAPADO dentro de su
#     texto —«`autoridad: aprobada \| trabajo`»— y por eso salían NUEVE celdas en vez de
#     ocho: `celdas[5]` era la columna PROPIETARIO y la fase de verdad, `**F6**`, estaba en
#     `celdas[6]`. **`F-07` desaparecía del universo, y la guarda `if not halladas: raise`
#     sólo dispara si se pierden TODAS.** Perder una era silencioso.
#
#     Es EXACTAMENTE el defecto `P-08` que este fichero declara existir para cerrar —«un
#     universo que encoge sin decirlo»— cometido por el propio instrumento que lo cierra. Y
#     no es un detalle de estilo: `O26` §5 convierte estas tres restas en criterio de
#     certificación, de modo que una obligación que se cae del universo se cae del criterio.
def _celdas(linea):
    r"""Las celdas de una fila Markdown. Un `\|` es TEXTO, no un separador."""
    return [c.replace("\\|", "|").strip() for c in re.split(r"(?<!\\)\|", linea)]


def hallazgos_externos_f6():
    """Los `F-nn` cuya FILA de §19 declara fase `F6`, con DOBLE derivación.

    La fase se lee de DOS maneras independientes —por POSICIÓN de columna y por CONTENIDO de
    celda— y se exige que coincidan. Un instrumento que se lee a sí mismo de una sola manera
    no puede detectar que su manera dejó de funcionar: eso es lo que pasó, y por eso la
    guarda no es «que no salga vacío» sino «que las dos lecturas den el mismo conjunto».
    """
    texto = _leer(ARQ)
    filas = list(re.finditer(r"^\|\s*`(F-\d\d)`[^\n]*$", texto, re.M))
    if not filas:
        raise SedeIlegible("§19 no publica ninguna fila `F-nn`, y su tabla las declara: la "
                           "lectura de la fila ha dejado de funcionar")
    por_posicion, por_contenido, anchuras = {}, {}, {}
    for m in filas:
        celdas = _celdas(m.group(0))
        anchuras[m.group(1)] = len(celdas)
        if len(celdas) > 5 and re.search(r"\bF6\b", celdas[5]):
            por_posicion[m.group(1)] = "11-ARQ §19 · tabla de hallazgos externos"
        # Por CONTENIDO: la celda de fase es la que ES una fase y nada más.
        for celda in celdas:
            if re.fullmatch(r"\**\s*`?F\d[a-c]?`?\s*(?:y\s+`?F\d[a-c]?`?\s*)?\**", celda) \
                    and re.search(r"\bF6\b", celda):
                por_contenido[m.group(1)] = "11-ARQ §19 · tabla de hallazgos externos"
                break
    # La ANCHURA uniforme es la propiedad que el defecto rompió, y se comprueba aparte para
    # que el diagnóstico nombre la causa y no sólo el síntoma.
    anchura_comun = max(set(anchuras.values()), key=list(anchuras.values()).count)
    descolocadas = sorted(f for f, n in anchuras.items() if n != anchura_comun)
    if descolocadas:
        raise SedeIlegible(
            "las filas %s de la tabla de §19 no tienen el mismo número de celdas que las "
            "demás (%d frente a %d): la lectura por POSICIÓN de columna deja de ser fiable "
            "y una obligación puede caerse del universo en silencio"
            % (", ".join(descolocadas), anchuras[descolocadas[0]], anchura_comun))
    if por_posicion != por_contenido:
        solo_una = sorted(set(por_posicion) ^ set(por_contenido))
        raise SedeIlegible(
            "las dos lecturas de la fase de §19 —por posición y por contenido— discrepan "
            "en %s: el universo no se puede derivar mientras el instrumento no se entienda "
            "a sí mismo" % ", ".join(solo_una))
    if not por_contenido:
        raise SedeIlegible("§19 no publica ningún hallazgo externo con fase F6, y su tabla "
                           "los declara")
    # `ADJ-G1` · el componente `F-nn` era el ÚNICO SIN SUELO: su guarda sólo disparaba con
    # CERO filas, de modo que perder UNA era silencioso. La numeración de esta tabla NO es
    # consecutiva —la sede publica `F-01`, `F-02`, `F-04`… y `F-03` y `F-09` no existen—,
    # así que aquí no hay consecutividad que exigir sin inventarse un hueco: el suelo de
    # este componente lo pone entero el CLIQUET DEL CORPUS, y por eso el cliquet no es un
    # adorno. Lo que queda fuera se publica con su motivo, que es su fase.
    for ident in sorted(set(anchuras) - set(por_contenido)):
        _excluir_obligacion("F-nn", ident,
                            "su fila de §19 no declara fase `F6`; el criterio de este "
                            "componente es «" + CRITERIOS_DE_PERTENENCIA["F-nn"] + "»")
    _exigir_identificadores("F-nn", por_contenido)
    return por_contenido


def contratos_v6():
    """`V6-01`…`V6-19`, derivados de §20 del documento 11."""
    texto = _leer(ARQ)
    halladas = {v: "11-ARQ §20 · contratos de F6"
                for v in sorted(set(re.findall(r"\bV6-\d\d\b", texto)))}
    # `ADJ-G1` · el `< 19` era un cardinal ESCRITO, y además con holgura por abajo. Lo
    # sustituye la CONSECUTIVIDAD, que se deriva: si falta `V6-07`, el conjunto tiene un
    # hueco y el hueco se ve sin que nadie sepa cuántos contratos «debería» haber.
    _exigir_consecutividad("V6", halladas, r"V6-(\d\d)")
    _exigir_identificadores("V6", halladas)
    return halladas


def obligaciones_g():
    """`g.1`…`g.16`, derivadas de las cabeceras de la sección aprobada del estado durable.

    `g.0` es la frontera entre norma y mecanismo, y `g.17`/`g.18` declaran lo derivado y lo
    que la sección NO hace: ninguna de las tres es una obligación de contenido, y por eso el
    barrido se queda con las numeradas de 1 a 16, que es lo que la sede enumera.
    """
    texto = _leer(ESTADO_DURABLE)
    todas = {m.group(1): int(m.group(2))
             for m in re.finditer(r"^##\s+`(g\.(\d+))`", texto, re.M)}
    # `ADJ-G1` · la CONSECUTIVIDAD se comprueba sobre TODAS las cabeceras `g.n` que la sede
    # publica —`g.0` incluida—, antes de aplicar ninguna ventana. Si desaparece `g.7`, el
    # hueco aparece aquí y no hay cardinal escrito que lo tape.
    _exigir_consecutividad("g", sorted(todas), r"g\.(\d+)")
    halladas = {ident: "g-ESTADO-DURABLE-APROBADA.md · cabecera"
                for ident, n in todas.items() if 1 <= n <= 16}
    # LA VENTANA, DECLARADA CON SU MOTIVO Y NO SUPUESTA (`ADJ-M10`). Lo que queda fuera se
    # publica en `EXCLUIDOS_DE_OBLIGACION` con la razón por la que queda fuera, que es la
    # diferencia entre una frontera y un recorte.
    for ident, n in sorted(todas.items(), key=lambda par: par[1]):
        if ident not in halladas:
            _excluir_obligacion(
                "g", ident,
                "`g.0` es la frontera entre norma y mecanismo y `g.17`/`g.18` declaran lo "
                "derivado y lo que la sección NO hace: ninguna es una obligación de "
                "contenido" if n in (0, 17, 18) else
                "la cabecera `%s` queda fuera de la ventana 1..16 que la sede enumera"
                % ident)
    _exigir_identificadores("g", halladas)
    return halladas


def contratos_transversales():
    """`C2`, `C4` y `C5`, derivados de los ficheros del árbol y no de una lista."""
    base = os.path.join(RAIZ, "kernel/operativo/contratos")
    halladas = {}
    for nombre in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        m = re.match(r"^(C[245])-", nombre)
        if m:
            halladas[m.group(1)] = "kernel/operativo/contratos/" + nombre
            continue
        # `ADJ-M10` · lo que la selección deja fuera se PUBLICA con su motivo. Cuatro de
        # los siete contratos del directorio no entran, y hasta hoy no lo decía nadie.
        otro = re.match(r"^(C\d+)-", nombre)
        if otro:
            _excluir_obligacion(
                "C", otro.group(1),
                "el componente selecciona `C2`, `C4` y `C5` por lista ESCRITA; este "
                "contrato existe en el árbol y es de fase ANTERIOR")
    # `ADJ-G1` · el `!= 3` era el último cardinal escrito. El suelo de este componente lo
    # pone el CLIQUET DEL CORPUS: `C2`, `C4` y `C5` están nombrados en el `cubre` de sus
    # escenarios, y retirar el fichero de uno los deja ejercidos y fuera del universo, que
    # es lo que `_exigir_que_ninguna_desaparezca` convierte en fallo cerrado. Aquí queda la
    # comprobación que este barrido SÍ puede hacer por sí solo: que el directorio exista y
    # que lo hallado tenga la forma declarada.
    if not os.path.isdir(base):
        raise SedeIlegible(
            "no existe `kernel/operativo/contratos/`: la sede de los contratos "
            "transversales no está, y un directorio ausente no es un conjunto vacío "
            "legítimo — es una derivación que no se ha podido hacer")
    _exigir_identificadores("C", halladas)
    return halladas


# `H-01` bis · LA DEUDA SE DERIVA POR SU FASE, Y NO POR UNA LISTA DE PREFIJOS
#
#     HECHO REPRODUCIDO. La derivación anterior era `re.findall(r"`(FD-\d+|M-04|A14|E5-\d+)`")`
#     —una LISTA DE PREFIJOS escrita a mano— y por eso **`S1-02` no entraba**, siendo una fila
#     de `06-DEUDA` §10 bis con fase `F6` y hermana de `FD-1`…`FD-6`. Y por la misma razón
#     entraban `FD-2` y `FD-4`, que esa sede declara con fase **«no consta»**, propietario
#     **el Owner** y condición «*NO se corrige aquí, y no puede corregirse aquí*»: **no son
#     obligaciones INTERNAS de `F6`**, y contarlas como tales hacía que la resta `A` publicara
#     dos filas que nadie podía cerrar sin reabrir `F5`.
#
#     Ahora la pertenencia se DERIVA de lo que la sede dice de cada fila —su FASE—, que es el
#     criterio que la propia sede publica. Una fila nueva con fase `F6` entra sola; una que
#     pierda la fase sale sola y se ve. Lo que quedó fuera NO se calla: se publica aparte.
FASE_F6 = re.compile(r"\**\s*`?F6`?\s*\**$")


def _filas_de_deuda(texto):
    """`{id: (fase, celdas)}` de toda fila de tabla de la sede que empiece por un id."""
    filas = {}
    for m in re.finditer(r"^\|\s*\**\s*`([A-Z0-9]+-[A-Za-z0-9.]+)`[^\n]*$", texto, re.M):
        celdas = _celdas(m.group(0))
        fase = ""
        for celda in celdas:
            if FASE_F6.match(celda) or re.fullmatch(r"\**\s*`?F\d[a-c]?`?\s*\**", celda) \
                    or celda == "no consta":
                fase = celda
                break
        filas[m.group(1)] = (fase, celdas)
    return filas


# LA FRONTERA DEL COMPONENTE «deuda», DICHA EN VEZ DE SUPUESTA
#
#     El universo que hay que derivar es el que el encargo enumera, y su sexta entrada dice
#     «deudas y límites EXTERNOS». `06-DEUDA` publica DOS censos distintos y no los mezcla:
#     §2 son las CONDICIONES DE CIERRE `C-L` heredadas de `F4c` y `F5`, y §3, §4, §7, §8,
#     §10 bis y §10 ter son la DEUDA con propietario y fase. El componente se ciñe al
#     segundo, que es el enumerado.
#
#     Y LO QUE QUEDA FUERA NO SE CALLA, que es la mitad que importa: `--obligaciones`
#     publica aparte, con su sede y su estado, (a) la deuda que la sede registra SIN fase
#     `F6` —`FD-2` y `FD-4`, cuyo propietario es el Owner y cuya condición dice «no puede
#     corregirse aquí»—, (b) `E-17` y `E-18`, que §10 ter clasifica como EXTERNA y como
#     LÍMITE DE ANFITRIÓN, y (c) las condiciones `C-L` cuya fase nombra `F6`. Un universo
#     que encoge en silencio es `P-08`; uno que encoge DICIENDO QUÉ deja fuera y POR QUÉ es
#     una frontera, y se puede discutir.
SECCIONES_DE_DEUDA = re.compile(
    r"^##\s+(?:3|4|7|8|10 bis|10 ter)\s+·", re.M)
SECCION_C_L = re.compile(r"^##\s+2\s+·", re.M)


def _bloques_de_seccion(texto, patron):
    """El texto de cada sección cuya cabecera casa, hasta la cabecera `##` siguiente."""
    cabeceras = [(m.start(), m.group(0)) for m in re.finditer(r"^##\s+[^\n]*$", texto, re.M)]
    trozos = []
    for i, (inicio, cabecera) in enumerate(cabeceras):
        fin = cabeceras[i + 1][0] if i + 1 < len(cabeceras) else len(texto)
        if patron.match(cabecera):
            trozos.append(texto[inicio:fin])
    return trozos


def _menciona_f6(celda):
    return bool(re.search(r"\bF6\b", celda or ""))


def deudas_sin_fase_f6():
    """Deuda que la sede registra y que NO declara fase `F6`. Se publica, no se calla.

    Cada una con la SECCIÓN de la que sale, porque no todas quedan fuera por lo mismo:
    `FD-2` y `FD-4` son de §10 bis con fase «no consta» y propietario el Owner, y `E-17` y
    `E-18` son de §10 ter, que las clasifica como DEUDA EXTERNA y como LÍMITE DE ANFITRIÓN.
    """
    texto = _leer(DEUDA)
    fuera = {}
    for bloque in _bloques_de_seccion(texto, SECCIONES_DE_DEUDA):
        cabecera = bloque.splitlines()[0].lstrip("# ").strip()
        for ident, (fase, _c) in _filas_de_deuda(bloque).items():
            if not _menciona_f6(fase):
                fuera[ident] = (fase or "(sin celda de fase)", cabecera[:58])
    return dict(sorted(fuera.items()))


def condiciones_c_l_con_fase_f6():
    """Las condiciones de cierre `C-L` de §2 cuya fase nombra `F6`. Otro censo, publicado.

    La celda de fase de §2 no siempre es una fase sola: `C-L.7` escribe «**`F5`** la
    especificación · **`F6`** el instrumento», que es DOS fases con su reparto. Se busca la
    mención en cualquier celda breve, y no un `fullmatch`, porque una fase repartida sigue
    siendo una fase y quedarse sólo con las simples volvería a esconder una fila.
    """
    texto = _leer(DEUDA)
    salida = {}
    for bloque in _bloques_de_seccion(texto, SECCION_C_L):
        for ident, (_fase, celdas) in _filas_de_deuda(bloque).items():
            candidatas = [c for c in celdas if len(c) < 80 and _menciona_f6(c)
                          and not c.startswith("`" + ident)]
            if candidatas:
                salida[ident] = min(candidatas, key=len)
    return dict(sorted(salida.items()))


def deudas_y_limites():
    """La deuda con fase `F6` de su sede canónica, derivada por SECCIÓN y por FASE.

    Dos formas, las dos derivadas y ninguna escrita a mano: las FILAS de tabla de las
    secciones de deuda cuya celda de fase nombra `F6`, y las SECCIONES numeradas que son
    ellas mismas una deuda y declaran su fase en un campo `FASE` —`M-04` y `A14`, que no
    viven en tabla—. La guarda no es «que no salga vacío»: es que las secciones de deuda que
    la sede declara SIGAN siendo legibles como tales.
    """
    texto = _leer(DEUDA)
    bloques = _bloques_de_seccion(texto, SECCIONES_DE_DEUDA)
    if len(bloques) < 6:
        raise SedeIlegible(
            "`%s` publica %d de las seis secciones de deuda que su índice declara (3, 4, 7, "
            "8, 10 bis y 10 ter): el barrido ha dejado de encontrarlas y el universo "
            "encogería en silencio" % (DEUDA, len(bloques)))
    halladas = {}
    for bloque in bloques:
        cabecera = bloque.splitlines()[0]
        for ident, (fase, _c) in _filas_de_deuda(bloque).items():
            if _menciona_f6(fase):
                halladas[ident] = "06-DEUDA · fila con fase F6"
        # Una sección que ES una deuda declara su fase en un campo `FASE`, no en una celda.
        propia = re.match(r"^##\s+\d+[a-z ]*·\s*`([A-Z0-9]+-?\d*)`", cabecera)
        if propia and re.search(r"\bFASE\s+[^\n]*\bF6\b", bloque):
            halladas[propia.group(1)] = "06-DEUDA · sección con campo FASE F6"
    if not halladas:
        raise SedeIlegible("`%s` no publica ninguna deuda con fase F6, y su sede es la "
                           "única del censo de deuda viva" % DEUDA)
    _exigir_identificadores("deuda", halladas)
    return halladas


COMPONENTES_DE_OBLIGACION = [
    ("§19", "las obligaciones de fase F6 de `11-ARQ` §19", obligaciones_de_19),
    ("F-nn", "los hallazgos EXTERNOS con fase F6", hallazgos_externos_f6),
    ("V6", "los contratos `V6-01`…`V6-19` de §20", contratos_v6),
    ("g", "las obligaciones `g.1`…`g.16` del estado durable", obligaciones_g),
    ("C", "los contratos transversales `C2`, `C4` y `C5`", contratos_transversales),
    ("deuda", "las deudas y límites externos vigentes", deudas_y_limites),
]


# ── el corpus EJECUTABLE contra el que se cruza el universo ──────────────────────

def _escenarios():
    """Todo bloque `ads:escenario` del kernel y de los packs, leído sin PyYAML.

    Se lee con el mismo subconjunto que el runtime usa —líneas `clave: valor`— porque este
    derivador tiene que poder correr donde PyYAML no esté. Sólo se necesitan cuatro campos.
    """
    encontrados = []
    for ambito in (KERNEL_PRUEBAS, "packs"):
        base = os.path.join(RAIZ, ambito)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
            for nombre in sorted(filenames):
                if not nombre.endswith(".md"):
                    continue
                with io.open(os.path.join(dirpath, nombre), encoding="utf-8") as fh:
                    texto = fh.read()
                for bloque in re.findall(r"```yaml ads:escenario\n(.*?)```", texto, re.S):
                    def campo(clave):
                        m = re.search(r"^%s:\s*(.+)$" % clave, bloque, re.M)
                        return m.group(1).strip().strip('"') if m else ""
                    cubre = re.search(r"^cubre:\s*\[(.*?)\]", bloque, re.M | re.S)
                    encontrados.append({
                        "id": campo("id"),
                        "cubre": [c.strip().strip('"') for c in
                                  (cubre.group(1).split(",") if cubre else [])],
                        "validador": campo("validador"),
                        "evidencia": campo("evidencia"),
                        "estado": campo("estado"),
                    })
    return encontrados


def _mutaciones():
    """Las pruebas a las que apunta alguna infracción deliberada del catálogo único."""
    apuntadas = {}
    base = os.path.join(RAIZ, VALIDADORES)
    for nombre in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        if not nombre.endswith(".py"):
            continue
        with io.open(os.path.join(base, nombre), encoding="utf-8") as fh:
            texto = fh.read()
        for m in re.finditer(r'Mutacion\(\s*"([^"]+)"\s*,\s*"[^"]*"\s*,\s*"(T\d+)"', texto):
            apuntadas.setdefault(m.group(2), []).append(m.group(1))
    return apuntadas


def _cubre(entrada, obligacion):
    """Si una entrada de `cubre` nombra ESTA obligación, y no otra que la contiene.

    `CONTRATO 1` es prefijo de `CONTRATO 1bis`: sin frontera de palabra, cerrar la segunda
    daría por cerrada la primera, que es exactamente la absorción que §19 prohíbe.
    """
    return re.search(r"(?<![\w.-])" + re.escape(obligacion) + r"(?![\w.-])", entrada)


def universo_de_obligaciones():
    """`{obligacion: {"clase", "sede", "escenarios", "validadores", "evidencias",
    "sabotajes"}}`, derivado entero."""
    escenarios, apuntadas = _escenarios(), _mutaciones()
    universo = {}
    de_quien = {}
    for clase, _titulo, fn in COMPONENTES_DE_OBLIGACION:
        for obligacion, sede in fn().items():
            # `ADJ-G1` · un identificador DUPLICADO entre componentes se tragaba en
            # silencio: `setdefault` conservaba la primera clase y la segunda desaparecía
            # del recuento por componentes sin mover el TOTAL. Dos componentes que reclaman
            # la misma obligación no es un detalle: es que una de las dos fronteras está
            # mal trazada, y hasta saber cuál no se deriva nada.
            if de_quien.setdefault(obligacion, clase) != clase:
                raise SedeIlegible(
                    "la obligación `%s` la reclaman DOS componentes, `%s` y `%s`. Con dos "
                    "fronteras que se solapan, el recuento por componentes deja de sumar el "
                    "total y una de las dos filas desaparece sin que nada lo diga"
                    % (obligacion, de_quien[obligacion], clase))
            ficha = universo.setdefault(obligacion, {
                "clase": clase, "sede": sede, "escenarios": [], "validadores": set(),
                "evidencias": [], "sabotajes": []})
            for esc in escenarios:
                if not any(_cubre(c, obligacion) for c in esc["cubre"]):
                    continue
                ficha["escenarios"].append(esc["id"])
                if esc["validador"]:
                    ficha["validadores"].add(esc["validador"])
                if esc["evidencia"] and os.path.isfile(
                        os.path.join(RAIZ, KERNEL_PRUEBAS, "pruebas", esc["evidencia"])):
                    ficha["evidencias"].append(esc["evidencia"])
                ficha["sabotajes"].extend(apuntadas.get(esc["id"], []))
    # `ADJ-G1` · EL CLIQUET, y va AL FINAL: hace falta el universo entero para poder decir
    # qué se ha caído de él.
    _exigir_que_ninguna_desaparezca(universo)
    return universo


# `H-07` · EL RÓTULO DE LA RESTA `A`, CORREGIDO PARA QUE DIGA LO QUE MIDE
#
#     La resta `A` se publicaba como «obligaciones internas SIN IMPLEMENTACIÓN» y se
#     calculaba como «ninguna prueba la declara en su `cubre` con validador», que es
#     TRAZABILIDAD. La auditoría lo verificó fila a fila y encontró CINCO falsos positivos:
#     `CONTRATO 3`, `g.7` y `FD-6` están implementados y ejecutados en el árbol, y `FD-2` y
#     `FD-4` ni son internas ni son de `F6` —`06-DEUDA` las declara del Owner y con fase «no
#     consta»—. Un instrumento que rotula «sin implementación» lo que mide como «sin
#     cobertura declarada» hace creer que sabe qué está construido, y no lo sabe.
#
#     Se corrige por los DOS lados y ninguno es cosmético: las dos que no eran de `F6` salen
#     del universo por su FASE —y se publican aparte, no se callan—, y el rótulo pasa a
#     nombrar el predicado real. Lo que queda dentro es lo que hay que resolver: una
#     obligación sin escenario que la cubra es indistinguible, PARA ESTE APARATO, de una sin
#     implementar, y esa indistinción es justamente el defecto —no se tapa rotulándola de
#     una de las dos maneras—.
#
# `ADJ-M4` · Y LO QUE UNA RESTA VACÍA **NO** DEMUESTRA, DICHO AL LADO DE LA CIFRA
#
#     El adjudicador del gate del 2026-09-04 lo midió así: «`A=0` no demuestra `O26` §5.1 y
#     `B=0` no demuestra `O26` §5.2», con un CONTRAEJEMPLO VIVO — `V6-12` figuraba con
#     `B=0`, o sea «tiene sabotaje declarado», y la propiedad que `ADJ-B3` derribó —el
#     append-only de la sede del Owner más allá del prefijo del nacimiento— **no tenía
#     ningún sabotaje que la pusiera roja**. Los sabotajes imputados a `V6-12` eran `N189`,
#     `N242` y `N242b`, y `N189` está declarado contra `V6-11`.
#
#     La cifra era correcta y la lectura era falsa, y la culpa no es del lector: un rótulo
#     que dice «implementadas SIN sabotaje» invita a leer «las demás tienen sabotaje
#     SUFICIENTE», que es otra cosa. El remedio no es cambiar el cálculo —mide bien lo que
#     mide— sino publicar, PEGADO A CADA CIFRA, qué proposición NO queda demostrada por
#     ella. Es la sexta condición de `O18`: ninguna promesa de garantía superior a la
#     realmente entregada.
LO_QUE_UNA_RESTA_VACIA_NO_DEMUESTRA = {
    "A": ("NO demuestra `O26` §5.1 —«no quedan obligaciones internas sin implementar»—. "
          "Mide TRAZABILIDAD DECLARADA: que algún escenario nombre la obligación en su "
          "`cubre` y declare un validador. Un `cubre` es una declaración escrita, y este "
          "aparato no sabe si lo declarado está construido"),
    "B": ("NO demuestra `O26` §5.2 —«no quedan propiedades críticas sin una prueba capaz "
          "de fallar»—. Mide EXISTENCIA DE AL MENOS UN SABOTAJE imputado a la obligación, "
          "no que sus propiedades estén cubiertas una a una. Contraejemplo medido y vivo: "
          "`V6-12` figuraba con `B=0` mientras el append-only de la sede del Owner más "
          "allá del prefijo del nacimiento no tenía sabotaje ninguno (`ADJ-B3`)"),
    "C": ("NO demuestra que la evidencia sea VIGENTE ni que describa el árbol de hoy. Mide "
          "que exista un fichero de evidencia enlazado y presente en el árbol. Que la "
          "evidencia demuestre lo que el informe afirma lo comprueba `T158`, y que el "
          "ESTADO declarado de cada escenario se derive de ella, `T350`"),
}

ROTULOS_DE_RESTA = (
    ("A", "sin COBERTURA DECLARADA: ningún `cubre` con validador la nombra"),
    ("B", "con cobertura y SIN NI UN SABOTAJE imputado que la ponga roja"),
    ("C", "con cobertura y SIN FICHERO DE EVIDENCIA presente en el árbol"),
)


def restas():
    """Las TRES RESTAS, derivadas. Se publican aunque no estén vacías."""
    universo = universo_de_obligaciones()
    a = sorted(o for o, f in universo.items() if not f["validadores"])
    b = sorted(o for o, f in universo.items() if f["validadores"] and not f["sabotajes"])
    c = sorted(o for o, f in universo.items() if f["validadores"] and not f["evidencias"])
    return universo, a, b, c


def publicar_obligaciones(destino):
    universo, a, b, c = restas()
    destino.write("UNIVERSO OBLIGATORIO DE `F6`, DERIVADO\n")
    destino.write("=" * 78 + "\n\n")
    for clase, titulo, fn in COMPONENTES_DE_OBLIGACION:
        suyas = sorted(o for o, f in universo.items() if f["clase"] == clase)
        destino.write("  (%-6s) %3d   %s\n" % (clase, len(suyas), titulo))
        destino.write("            criterio de pertenencia: %s\n"
                      % CRITERIOS_DE_PERTENENCIA[clase])
        destino.write("            %s\n" % ", ".join(suyas))
    destino.write("\n  TOTAL %d obligaciones\n\n" % len(universo))

    # `ADJ-G1` · LA PROCEDENCIA, PUBLICADA. De qué fichero sale cada componente, con su
    # digest y su tamaño. Sin esto, «58 obligaciones» es una cifra sin origen, y una cifra
    # sin origen no se puede volver a derivar ni contrastar contra nada.
    destino.write("PROCEDENCIA DE CADA COMPONENTE — sede, digest y tamaño\n")
    destino.write("-" * 78 + "\n")
    for clase, rel, digest, tamano in procedencia_de_los_componentes():
        destino.write("  %-7s %-58s %s  %s\n" % (clase, rel, digest, tamano))
    ejercidas = obligaciones_ejercidas_por_el_corpus()
    protegidas = sorted(o for o in universo if o in ejercidas)
    destino.write("\n  CLIQUET · obligaciones que el corpus EJERCE: %d  ·  de ellas en el "
                  "universo: %d\n" % (len(ejercidas), len(protegidas)))
    destino.write("  del universo, SIN cliquet que las proteja: %s\n"
                  % (", ".join(sorted(set(universo) - set(ejercidas))) or "ninguna"))
    destino.write("  fuera del cliquet por declaración COMPROBADA: %s\n\n"
                  % ", ".join(sorted(FUERA_DEL_CLIQUET)))

    # LO QUE QUEDA FUERA, DICHO. Un universo que encoge en silencio es `P-08`; uno que dice
    # QUÉ deja fuera y POR QUÉ es una frontera, y una frontera se puede discutir.
    destino.write("FUERA DEL UNIVERSO, Y POR QUÉ — no se calla ninguno\n")
    destino.write("-" * 78 + "\n")
    if EXCLUIDOS_DE_OBLIGACION:
        destino.write("  excluidos por los componentes, CADA UNO CON SU MOTIVO (%d)\n"
                      % len(EXCLUIDOS_DE_OBLIGACION))
        for clase, ident, motivo in EXCLUIDOS_DE_OBLIGACION:
            destino.write("      %-7s %-10s %s\n" % (clase, ident, motivo))
    sin_fase = deudas_sin_fase_f6()
    destino.write("  deuda registrada SIN fase `F6` (%d)  ·  no es obligación interna de F6\n"
                  % len(sin_fase))
    for ident, (fase, seccion) in sin_fase.items():
        destino.write("      %-8s fase declarada: %-14s  ·  %s\n"
                      % (ident, fase or "(ninguna)", seccion))
    c_l = condiciones_c_l_con_fase_f6()
    destino.write("  condiciones de cierre `C-L` con fase `F6` (%d)  ·  OTRO censo: "
                  "`06-DEUDA` §2, heredado de `F4c` y `F5`\n" % len(c_l))
    for ident, fase in c_l.items():
        destino.write("      %-8s fase declarada: %s\n" % (ident, fase))
    destino.write("\n")
    destino.write("%-16s %-7s %-28s %-22s %s\n"
                  % ("obligación", "clase", "pruebas", "sabotajes", "evidencia"))
    for obligacion in sorted(universo):
        f = universo[obligacion]
        destino.write("%-16s %-7s %-28s %-22s %s\n" % (
            obligacion, f["clase"],
            ",".join(f["escenarios"][:4]) or "—",
            ",".join(sorted(set(f["sabotajes"]))[:3]) or "—",
            (sorted(set(f["evidencias"]))[:1] or ["—"])[0]))
    destino.write("\nLAS TRES RESTAS, DERIVADAS — Y LO QUE UNA RESTA VACÍA NO DEMUESTRA\n")
    destino.write("-" * 78 + "\n")
    for (letra, titulo), lista in zip(ROTULOS_DE_RESTA, (a, b, c)):
        destino.write("  %s · %-58s %d\n" % (letra, titulo, len(lista)))
        if lista:
            destino.write("      %s\n" % ", ".join(lista))
        for linea in textwrap.wrap(LO_QUE_UNA_RESTA_VACIA_NO_DEMUESTRA[letra], 74):
            destino.write("      %s\n" % linea)
        destino.write("\n")
    return 0 if not (a or b or c) else 1


# ===========================================================================
#  `ADJ-G1` · LAS META-PRUEBAS · un canal que no se puede sabotear no es un canal
# ===========================================================================
#  Cada guarda de arriba tiene aquí una infracción deliberada que la pone ROJA. No es un
#  adorno: el defecto que este fichero acaba de cerrar existía porque las guardas estaban
#  escritas y NADIE LAS HABÍA PROBADO — `< 4` con cinco obligaciones reales llevaba tiempo
#  regalando una unidad de holgura, y nadie lo vio porque ninguna prueba retiraba nunca un
#  contrato.
#
#  DECISIÓN · cada sabotaje corre sobre una COPIA y contra el script DE LA COPIA
#      Alternativas: (a) parchear `RAIZ` con una variable de entorno; (b) copiar el corpus
#      y ejecutar el derivador que vive DENTRO de la copia.
#      Se elige (b). Con (a) el instrumento tendría una variable que cambia QUÉ ÁRBOL
#      juzga, que es una puerta abierta en la pieza que decide si el universo ha encogido:
#      un `ADS_UNIVERSO_RAIZ` apuntando a un árbol amable produce un verde honesto sobre el
#      árbol equivocado. Con (b) no hay puerta: cada corrida juzga el árbol donde está.
#      La copia son 19 MB y tarda dos décimas; el coste no es el argumento, la puerta sí.
SABOTAJES_DEL_UNIVERSO = []


def _sabotaje(rotulo, espera):
    def envoltorio(fn):
        SABOTAJES_DEL_UNIVERSO.append((rotulo, espera, fn))
        return fn
    return envoltorio


def _sustituir_en(destino, rel, viejo, nuevo):
    ruta = os.path.join(destino, rel)
    with io.open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    if viejo not in texto:
        raise AssertionError("el sabotaje no encuentra su ancla en %s: %r" % (rel, viejo[:60]))
    with io.open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto.replace(viejo, nuevo, 1))


@_sabotaje("la fila `F-07` cambia de fase `F6` a `F5` — el id DESAPARECE",
           "EL UNIVERSO HA ENCOGIDO")
def _s_fase_de_f07(destino):
    with io.open(os.path.join(destino, ARQ), encoding="utf-8") as fh:
        texto = fh.read()
    linea = [l for l in texto.splitlines() if l.startswith("| `F-07`")][0]
    _sustituir_en(destino, ARQ, linea, linea.replace("| **F6** |", "| **F5** |"))


@_sabotaje("se retira la fila `F-10` entera", "EL UNIVERSO HA ENCOGIDO")
def _s_retirar_f10(destino):
    with io.open(os.path.join(destino, ARQ), encoding="utf-8") as fh:
        texto = fh.read()
    linea = [l for l in texto.splitlines() if l.startswith("| `F-10`")][0]
    _sustituir_en(destino, ARQ, linea + "\n", "")


@_sabotaje("se retira el bloque `--- CONTRATO 2 … ---` de §19",
           "EL UNIVERSO HA ENCOGIDO")
def _s_retirar_contrato_2(destino):
    ruta = os.path.join(destino, ARQ)
    with io.open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    i = texto.index("--- CONTRATO 2 \u00b7")
    j = texto.index("--- CONTRATO", i + 10)
    with io.open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto[:i] + texto[j:])


@_sabotaje("desaparece `V6-07` de §20 — hueco en la numeración",
           "EL UNIVERSO HA ENCOGIDO")
def _s_hueco_en_v6(destino):
    ruta = os.path.join(destino, ARQ)
    with io.open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    with io.open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto.replace("V6-07", "V6-XX"))


@_sabotaje("desaparece la cabecera `g.7` — hueco en la numeración",
           "EL UNIVERSO HA ENCOGIDO")
def _s_hueco_en_g(destino):
    _sustituir_en(destino, ESTADO_DURABLE, "## `g.7`", "## `g.7bis`")


@_sabotaje("la sede del estado durable NO EXISTE", "ilegible")
def _s_sede_ausente(destino):
    os.remove(os.path.join(destino, ESTADO_DURABLE))


@_sabotaje("la sede de deuda no decodifica como UTF-8", "no decodifica como UTF-8")
def _s_sede_no_utf8(destino):
    with io.open(os.path.join(destino, DEUDA), "ab") as fh:
        fh.write(b"\xff\xfe basura binaria\n")


@_sabotaje("§19 pierde su bloque de contratos — PARSEO PARCIAL",
           "no contiene el bloque de contratos")
def _s_parseo_parcial(destino):
    _sustituir_en(destino, ARQ, "--- CONTRATO 1 \u00b7 DERIVAR EL CENSO",
                  "--- APUNTE 1 \u00b7 DERIVAR EL CENSO")


@_sabotaje("una fila de deuda con fase F6 estrena FAMILIA de identificador",
           "NO tienen la forma de su familia")
def _s_identificador_mal_formado(destino):
    # `FD-1` es una fila de `06-DEUDA` con fase `F6`. Renombrada a `ZZ-1` sigue siendo una
    # fila con fase `F6` y el barrido la sigue viendo: lo que cambia es que su identificador
    # ya no pertenece a ninguna familia declarada. Sin la guarda de FORMA entraría en el
    # universo un identificador que nadie sabe cruzar con nada.
    _sustituir_en(destino, DEUDA, "**`FD-1`**", "**`ZZ-1`**")


@_sabotaje("la tabla de §19 se queda SIN NINGUNA fila `F-nn` — vacío SOSPECHOSO",
           "no publica ninguna fila `F-nn`")
def _s_conjunto_vacio(destino):
    ruta = os.path.join(destino, ARQ)
    with io.open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    lineas = [l for l in texto.splitlines() if not l.startswith("| `F-")]
    with io.open(ruta, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lineas) + "\n")


@_sabotaje("desaparece `C1-*.md`: una excepción del cliquet deja de sostenerse",
           "ha dejado de ser cierto")
def _s_excepcion_caducada(destino):
    base = os.path.join(destino, "kernel/operativo/contratos")
    for nombre in os.listdir(base):
        if nombre.startswith("C1-"):
            os.remove(os.path.join(base, nombre))


def _derivar_en_la_copia(destino):
    """Importa el derivador QUE VIVE EN LA COPIA y le pide el universo."""
    import importlib.util                                          # noqa: PLC0415
    ruta = os.path.join(destino, "docs/evolucion/verificacion",
                        "derivar-universo-obligatorio.py")
    spec = importlib.util.spec_from_file_location("universo_en_copia", ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    salida = io.StringIO()
    modulo.publicar_obligaciones(salida)
    return salida.getvalue()


def autopruebas(destino_stdout):
    """Ejerce CADA guarda con una infracción deliberada. Devuelve 0 si todas la cazan."""
    import shutil                                                  # noqa: PLC0415
    import tempfile                                                # noqa: PLC0415

    def copiar(a_donde):
        shutil.copytree(RAIZ, a_donde, symlinks=True,
                        ignore=lambda d, n: [x for x in n
                                             if x in (".git", "__pycache__")])

    destino_stdout.write("META-PRUEBAS DEL UNIVERSO OBLIGATORIO\n")
    destino_stdout.write("=" * 78 + "\n\n")
    fallidos = 0
    raiz_tmp = tempfile.mkdtemp(prefix="ads-universo-")
    try:
        # CONTROL POSITIVO. Un control que no puede aprobar no sirve de nada: sobre la copia
        # intacta la derivación tiene que salir, y si no sale es que el aparato de prueba
        # está roto y ningún rojo posterior significaría nada.
        limpio = os.path.join(raiz_tmp, "control")
        copiar(limpio)
        try:
            texto = _derivar_en_la_copia(limpio)
            marca = "TOTAL" in texto
        except SedeIlegible as e:
            marca, texto = False, str(e)
        destino_stdout.write("  %-4s CONTROL POSITIVO · la copia intacta deriva el universo\n"
                             % ("ok" if marca else "FALLA"))
        if not marca:
            fallidos += 1

        for indice, (rotulo, espera, aplicar) in enumerate(SABOTAJES_DEL_UNIVERSO):
            destino = os.path.join(raiz_tmp, "s%02d" % indice)
            copiar(destino)
            aplicar(destino)
            try:
                _derivar_en_la_copia(destino)
                resultado, detalle = "NO DETECTADA", "la derivación salió sin levantar"
            except Exception as error:                             # noqa: BLE001
                # La copia trae su PROPIA clase `SedeIlegible` —es otro módulo—, así que no
                # se puede capturar por identidad de clase y se reconoce por NOMBRE. Y una
                # traza de cualquier otra clase NO es una detección: es el aparato
                # reventando, que es lo que `V6-03` manda no confundir con un juicio.
                detalle = str(error)
                if type(error).__name__ != "SedeIlegible":
                    resultado = "TRAZA"
                    detalle = "%s: %s" % (type(error).__name__, error)
                else:
                    resultado = "ok" if espera in detalle else "MOTIVO EQUIVOCADO"
            if resultado != "ok":
                fallidos += 1
            destino_stdout.write("  %-4s %-62s\n" % (resultado, rotulo))
            destino_stdout.write("       espera «%s»\n" % espera)
            if resultado != "ok":
                destino_stdout.write("       %s\n" % detalle[:300])
    finally:
        shutil.rmtree(raiz_tmp, ignore_errors=True)
    destino_stdout.write("\n  %d sabotajes · %d sin detectar\n"
                         % (len(SABOTAJES_DEL_UNIVERSO), fallidos))
    return 1 if fallidos else 0


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "--tabla"
    if modo == "--autopruebas":
        return autopruebas(sys.stdout)
    if modo == "--obligaciones":
        # El universo de OBLIGACIONES, que es el que `F6-H` declaró completo sin tenerlo.
        # Es un universo distinto del de FUENTES y por eso no comparte su derivación; lo
        # que comparte es la regla: falla cerrado y no encoge en silencio.
        try:
            return publicar_obligaciones(sys.stdout)
        except SedeIlegible as e:
            sys.stderr.write("FALLA CERRADO · %s\n" % e)
            return 2
    try:
        universo, procedencia = derivar()
    except SedeIlegible as e:
        sys.stderr.write("FALLA CERRADO · %s\n" % e)
        return 2

    if modo == "--rutas":
        for rel in universo:
            sys.stdout.write(rel + "\n")
        # `Z2-...`≡`Z-13`, y es la tercera vía por la que el universo encogía en silencio.
        # `EXCLUIDOS_IV` sólo se imprimía en `--tabla` y en `--md`, y **`--rutas` es el
        # único modo que invocan el emisor del sobre y la RECETA publicada**: lo que el
        # componente (iv) excluye era invisible por el camino que se audita. Un dictamen
        # NUEVO cuyo H1 lleve una voz de NO-DICTAMEN —`25-SÍNTESIS-DEL-CIERRE.md` con
        # veredicto invertido— salía del universo con `rc=0` y sin que nada lo dijera.
        # Ahora lo dice **por el camino que se audita**, en `stderr` para no contaminar la
        # lista de rutas, y el emisor lo copia al SOBRE.
        _excluidos(sys.stderr)
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
    # `W2-06`. Lo que el componente (iv) DEJA FUERA se publica: un universo que encoge lo
    # dice, y quien lee la tabla ve por qué cada documento numerado no está.
    _excluidos(sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
