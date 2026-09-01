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
                     "ADJUDICACIÓN", "ADJUDICACION", "VEREDICTO")

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
