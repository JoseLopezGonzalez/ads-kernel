#!/usr/bin/env python3
"""comprobar-cobertura-de-gate — la cobertura de un gate deja de ser DECLARATIVA.

POR QUÉ EXISTE, Y QUÉ AGUJERO CIERRA. Dos gates consecutivos de `F6` han caído por lo mismo:
un revisor declaró al final que no había leído su lote, y hasta ese momento nada lo impedía ni
lo medía. El gate del 2026-09-03 cayó con seis fuentes o rangos sin abrir. El del 2026-09-04
cayó con **50 de 84 ficheros sin abrir y 29 329 de 48 143 líneas, el 60,9 %**, y su adjudicador
rechazó expresamente la atenuante del reparto —los dos lotes diferían en el 1,1 % y el otro
revisor terminó el suyo—.

`O27` §5 lo eleva a NORMA del Owner, y con estas palabras: «*Un gate no puede llegar a
adjudicación mientras algún revisor tenga una resta `ASIGNADO − LEÍDO` distinta del conjunto
vacío. Si un revisor todavía no ha terminado, debe continuar su lectura. Su lote no puede darse
por cerrado, sustituirse con búsquedas ni compensarse con lo leído por otro agente.*»

Este comprobador es lo que convierte esa norma en un HECHO MECÁNICO. Devuelve 0 sólo si las
CUATRO restas son vacías, y mientras no devuelva 0 **no se puede crear al adjudicador**.

    OBLIGATORIO − ASIGNADO              = ∅
    ASIGNADO − LEÍDO                    = ∅
    LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS    = ∅
    FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS = ∅

DECISIÓN · lo que NO cuenta como lectura, y por qué se comprueba en vez de pedirse
    `O27` §5 y el encargo lo enumeran: `grep`, `awk`, búsquedas, `diff`, ejecutar pruebas, y
    lo leído por otro agente. Un manifiesto de lectura que declarase «leída» una fuente por
    haberla `grep`-eado sería la misma declaración vacía que ya falló dos veces. Aquí el
    revisor declara, POR FUENTE, el rango de líneas que abrió y el SHA-256 del fichero que
    leyó; el comprobador exige que el SHA case con el árbol —si no casa, leyó otra cosa— y
    que los rangos CUBRAN el fichero entero. No se puede satisfacer con una búsqueda porque
    una búsqueda no produce rangos contiguos que cubran 2 000 líneas.

DECISIÓN · la unidad es la LÍNEA, no el fichero
    Un fichero «abierto» puede haberse mirado por encima. La tercera resta —líneas asignadas
    menos líneas leídas— es la que impide que «lo abrí» valga por «lo leí»: obliga a declarar
    QUÉ tramos, y la suma tiene que dar el fichero entero. Para un rango asignado
    explícitamente, el tramo declarado tiene que contener el rango.

DECISIÓN · las FUENTES MODIFICADAS llevan una resta propia
    Es la regla que los manifiestos de este expediente escriben desde el principio —«cobertura
    histórica delegada prohibida para un fichero modificado»— y que nunca se había comprobado.
    Un fichero que el corte modificó no admite delegación de ninguna clase: o está leído
    íntegro por el revisor que lo tiene asignado, o la resta no es vacía.

FORMATO. Dos ficheros JSON:

  manifiesto.json   {"candidata": "<sha>", "revisores": {"REV-1": {"fuentes": [...]}, ...},
                     "modificadas": ["ruta", ...]}
                    cada fuente: {"ruta": str, "lineas": int, "sha256": str,
                                  "rango": [inicio, fin] | null}
  lectura-<REV>.json {"revisor": "REV-1", "cerrado": bool,
                      "leidas": [{"ruta": str, "sha256": str,
                                  "tramos": [[inicio, fin], ...]}, ...]}

Uso:
  python3 comprobar-cobertura-de-gate.py --manifiesto M.json --lectura L1.json L2.json …
                                         [--raiz DIR] [--json]
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  El prólogo de `E-10` que sigue purga `sys.path` DESDE DENTRO del programa, y por eso
#  llega tarde contra `sitecustomize`: `site.py` lo importa mientras el intérprete arranca,
#  antes de que exista la primera sentencia de este fichero. La guarda cambia el MOMENTO
#  —comprueba las banderas de aislamiento y, si no están, se reejecuta con `-I -S -E`—, y
#  por eso las dos conviven: `G-03` impide que el gancho llegue a existir, y `E-10` sigue
#  cubriendo la contaminación de la ruta en el caso importado.
#
#  POR QUÉ ESTE PUNTO. Hasta hoy los cuatro ejecutables de `docs/evolucion/verificacion/`
#  eran los ÚNICOS del inventario sin guarda, declarados con motivo y con cliquet en `T380`
#  porque el agente que hizo `G-03` tenía prohibido tocar esta zona. Son el instrumento con
#  el que se mide si un gate cubre lo que dice cubrir y qué universo obligatorio existe: un
#  `hashlib` o un `json` sustituidos por quien los corre deciden esas dos respuestas. La
#  declaración se retira porque la excepción se ha cerrado, no porque haya caducado.

import os as _os_g03
import sys as _sys_g03

# LA GUARDA NO DEJA RASTRO EN EL ÁRBOL QUE JUZGA. Medido: al importar la guarda, Python
# escribía `validadores/__pycache__/aislamiento_de_arranque…pyc` en el árbol, y
# `comprobar_arranque.py` empezó a publicar «el proyecto arrastra `__pycache__`» sobre
# proyectos recién creados. Se desactiva la escritura de bytecode DURANTE la guarda y se
# devuelve al estado que tenía: lo que el punto importe después sigue cacheándose como
# siempre, y no se paga rendimiento por una comprobación que corre una vez.
_G03_BYTECODE = _sys_g03.dont_write_bytecode
_sys_g03.dont_write_bytecode = True
_G03_PROPIA = _os_g03.path.dirname(_os_g03.path.realpath(__file__))
_G03_SEDE = ""
_G03_RAIZ = _G03_PROPIA
while not _G03_SEDE:
    for _G03_CANDIDATA in (_G03_PROPIA,
                           _os_g03.path.join(_G03_RAIZ, "kernel", "operativo",
                                             "validadores")):
        if _os_g03.path.isfile(_os_g03.path.join(_G03_CANDIDATA,
                                                 "aislamiento_de_arranque.py")):
            _G03_SEDE = _G03_CANDIDATA
            break
    else:
        _G03_PADRE = _os_g03.path.dirname(_G03_RAIZ)
        if _G03_PADRE == _G03_RAIZ:
            _sys_g03.stderr.write(
                "[PROCEDENCIA_NO_FIABLE] no hay `aislamiento_de_arranque.py` ni junto a "
                "este punto ejecutable ni en el `kernel/operativo/validadores/` de ning\u00fan "
                "ancestro suyo: no se puede decidir si el arranque est\u00e1 aislado, y no se "
                "sigue\n")
            raise SystemExit(5)
        _G03_RAIZ = _G03_PADRE
_sys_g03.path.insert(0, _G03_SEDE)
import aislamiento_de_arranque as _aislamiento_g03                    # noqa: E402

AISLAMIENTO = _aislamiento_g03.exigir(__file__, __name__)
_sys_g03.dont_write_bytecode = _G03_BYTECODE

# `-I` deja FUERA de `sys.path` el directorio del guión —es lo que impide que un homónimo
# vecino se cuele— y los puntos que importan módulos hermanos lo necesitan. Se reintroduce
# por RUTA DERIVADA DE `__file__`, que no la escribe el lanzador.
if _G03_PROPIA not in _sys_g03.path:
    _sys_g03.path.insert(0, _G03_PROPIA)

# `E-10` · LA PROCEDENCIA DE LOS MÓDULOS, PURGADA ANTES DE NINGÚN `import` PROPIO
#
#  POR QUÉ ESTÁ AQUÍ, Y NO SÓLO EN `kernel/operativo/runtime/`. `H-01` de la auditoría del
#  2026-09-04 midió que `validadores/huella.py` no llevaba este prólogo y que, con un
#  `hashlib` homónimo en `PYTHONPATH`, **un árbol MUTADO producía la huella esperada y
#  `T150` publicaba SUPERADA con `EXIT=0`**. El mismo defecto vive en cualquier ejecutable
#  que decida algo y no purgue: éstos deciden qué universo obligatorio existe y si un gate
#  puede adjudicar, que es tanto o más que una huella.
#
#  DECISIÓN · se purga ANTES de importar nada propio, con lo único que el intérprete ya cargó
#      Purgar después de los `import` normales llega tarde —el homónimo ya está en
#      `sys.modules`— y purgar desde un módulo aparte depende de un `import`, que es
#      exactamente lo que se está protegiendo. `sys` es incorporado y `os` lo carga el
#      arranque, así que los dos vienen de `sys.modules` y no de la ruta. Que `os` sea el
#      bueno se COMPRUEBA, no se supone.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación y
#      convertiría un fallo de entorno en un fallo del aparato. `E-10` nombra dos cosas
#      concretas: `PYTHONPATH` y el `cwd`. Se retiran ésas y el recuento se publica.
import sys as _sys
import os as _os

_RAIZ_DEL_APARATO = _os.path.dirname(_os.path.abspath(__file__))


def _entradas_del_lanzador():
    """Lo que el LANZADOR puede meter en la ruta de importación: `PYTHONPATH` y el `cwd`."""
    sospechosas = set()
    for entrada in (_os.environ.get("PYTHONPATH") or "").split(_os.pathsep):
        if entrada:
            sospechosas.add(_os.path.realpath(entrada))
    try:
        sospechosas.add(_os.path.realpath(_os.getcwd()))
    except OSError:
        # Un `cwd` borrado bajo los pies no es motivo para no purgar el resto.
        pass
    return sospechosas


def _purgar_la_ruta_de_importacion():
    """Retira de `sys.path` lo que venga del lanzador. Devuelve cuántas entradas retiró."""
    del_lanzador = _entradas_del_lanzador()
    propia = _os.path.realpath(_RAIZ_DEL_APARATO)
    conservadas, retiradas = [], []
    for entrada in _sys.path:
        try:
            real = _os.path.realpath(entrada or _os.getcwd())
        except OSError:
            conservadas.append(entrada)
            continue
        if real != propia and real in del_lanzador:
            retiradas.append(real)
        else:
            conservadas.append(entrada)
    _sys.path[:] = conservadas
    return retiradas


RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()

# CONTROL DEL CONTROL de la purga: `os` se usa para poder purgar, así que si `os` mismo
# viniera del lanzador la purga no probaría nada. No hay forma honesta de seguir: se dice y
# se sale con el código de PROCEDENCIA.
if _os.path.realpath(_os.path.dirname(_os.__file__ or ".")) in _entradas_del_lanzador():
    _sys.stderr.write(
        "[PROCEDENCIA_NO_FIABLE] el módulo `os` procede de la ruta de importación del "
        "lanzador: este punto ejecutable no puede garantizar de dónde salen sus módulos y "
        "NO ejecuta\n")
    raise SystemExit(5)


import argparse
import hashlib
import io
import json
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Códigos de salida, estables y distintos. `2` es «no se pudo comprobar» y NO se confunde con
# `1`, que es «se comprobó y la cobertura está incompleta». La distinción importa: un gate que
# no puede medir su cobertura no es un gate con cobertura incompleta, es un gate sin medida.
COBERTURA_COMPLETA = 0
COBERTURA_INCOMPLETA = 1
NO_SE_PUDO_COMPROBAR = 2


class ManifiestoIlegible(Exception):
    pass


def _leer_json(ruta):
    try:
        with io.open(ruta, encoding="utf-8") as manejador:
            return json.load(manejador)
    except (OSError, ValueError) as error:
        raise ManifiestoIlegible("no se puede leer `%s`: %s" % (ruta, error))


def _sha256_y_lineas(base, relativa):
    destino = os.path.join(base, relativa)
    if not os.path.isfile(destino):
        return None, None
    with io.open(destino, "rb") as manejador:
        datos = manejador.read()
    return hashlib.sha256(datos).hexdigest(), datos.count(b"\n") + (
        0 if datos.endswith(b"\n") or not datos else 1)


def _normalizar(tramos):
    """Une tramos solapados o contiguos. `[[1,10],[11,20]]` → `[[1,20]]`."""
    limpios = sorted([int(a), int(b)] for a, b in tramos if int(b) >= int(a))
    salida = []
    for inicio, fin in limpios:
        if salida and inicio <= salida[-1][1] + 1:
            salida[-1][1] = max(salida[-1][1], fin)
        else:
            salida.append([inicio, fin])
    return salida


def _faltantes(tramos, desde, hasta):
    """Lo que queda SIN cubrir del intervalo `[desde, hasta]`."""
    huecos, cursor = [], desde
    for inicio, fin in _normalizar(tramos):
        if fin < desde or inicio > hasta:
            continue
        if inicio > cursor:
            huecos.append([cursor, min(inicio - 1, hasta)])
        cursor = max(cursor, fin + 1)
        if cursor > hasta:
            break
    if cursor <= hasta:
        huecos.append([cursor, hasta])
    return huecos


def _modificadas_del_arbol(manifiesto, base):
    """`G-07` · el conjunto obligatorio, DERIVADO con `git` entre la base y la candidata.

    Se usa `--name-status -M -C -z` a propósito, y no `--name-only`:

      · `-M` y `-C` detectan renombrados y copias, y de esas hay que leer **las DOS puntas**
        —la vieja para saber qué se movió y la nueva para saber qué hay que revisar—;
      · `-z` separa con `NUL`, de modo que una ruta con salto de línea o con caracteres no
        ASCII no parte el barrido en dos ni se pierde a la mitad. Con `\n` como separador,
        una ruta hostil desaparece del conjunto obligatorio SIN QUE NADA LO DIGA, y eso es
        exactamente la clase de fallo que este instrumento existe para impedir.

    Si no hay repositorio, o falta alguno de los dos SHA, se FALLA CERRADO: un conjunto
    obligatorio que no se puede derivar no es un conjunto obligatorio vacío.

    DOS PUERTAS TRASERAS, CERRADAS · las encontró el AUDITOR INDEPENDIENTE

        PUERTA 1 · `repo = manifiesto.get("repositorio") or RAIZ`. **El manifiesto elegía el
        repositorio.** Apuntándolo a cualquier otro y poniendo `base == candidata`, el
        derivado salía VACÍO, `perdidas` salía vacío y `declarado_obligatorio` volvía a ser
        exactamente `set(manifiesto["modificadas"])`: el comportamiento anterior a `G-07`,
        con `rc=0` y sin declarar nada. Se cierra: el repositorio es el ÁRBOL QUE SE MIDE y
        el manifiesto no lo elige. Si trae el campo, tiene que resolver a la misma raíz, y
        si no resuelve es fallo cerrado — no se ignora en silencio, porque un campo que se
        ignora es un campo que alguien creyó que hacía algo.

        PUERTA 2 · `"derivacion": "declarada-sin-arbol"` prometía en su propio mensaje de
        error «*y quedará publicado*», y **no se publicaba nada**: la palabra `derivacion`
        aparecía ocho veces en el fichero y ninguna escribía en `informe`. Se cierra abajo,
        en `comprobar`, publicando SIEMPRE el origen del conjunto derivado.
    """
    import subprocess                                                # noqa: PLC0415
    candidata = manifiesto.get("candidata")
    origen = manifiesto.get("base")
    declarado_repo = manifiesto.get("repositorio")
    if declarado_repo and os.path.realpath(declarado_repo) != os.path.realpath(base):
        raise ManifiestoIlegible(
            "el manifiesto declara `repositorio` = `%s`, y el árbol que se está midiendo es "
            "`%s`. El repositorio NO lo elige el manifiesto: derivar de otro árbol devuelve "
            "un conjunto vacío, deja la resta en cero y restaura el comportamiento anterior "
            "a `G-07` sin que nada lo diga" % (declarado_repo, base))
    if not candidata or not origen:
        # Sin las dos puntas no hay derivación posible. Se admite la declaración SÓLO si el
        # manifiesto lo dice expresamente, y entonces el informe lo publica: un instrumento
        # que degrada en silencio es el defecto, no el remedio.
        if manifiesto.get("derivacion") == "declarada-sin-arbol":
            return set(manifiesto.get("modificadas") or [])
        raise ManifiestoIlegible(
            "el manifiesto no declara `base` y `candidata`, de modo que el conjunto "
            "obligatorio no se puede DERIVAR del árbol. `G-07`: la declaración contrasta, "
            "no define. Si de verdad no hay árbol, decláralo con "
            "`\"derivacion\": \"declarada-sin-arbol\"` y quedará publicado")
    if origen == candidata:
        raise ManifiestoIlegible(
            "el manifiesto declara `base` y `candidata` IGUALES (`%s`): el árbol deriva el "
            "conjunto vacío y la resta sale en cero por construcción, no por cobertura"
            % origen[:12])
    orden = ["git", "-C", base, "diff", "--name-status", "-M", "-C", "-z",
             origen, candidata]
    try:
        proceso = subprocess.run(orden, capture_output=True, check=False)
    except OSError as error:
        raise ManifiestoIlegible("no se pudo invocar `git`: %s" % error)
    if proceso.returncode != 0:
        raise ManifiestoIlegible(
            "`git diff` entre `%s` y `%s` terminó con %d: %s"
            % (origen[:12], candidata[:12], proceso.returncode,
               proceso.stderr.decode("utf-8", "replace").strip()[:200]))
    piezas = proceso.stdout.decode("utf-8", "surrogateescape").split("\0")
    rutas, indice = set(), 0
    while indice < len(piezas):
        estado = piezas[indice]
        if not estado:
            indice += 1
            continue
        # `R` y `C` traen DOS rutas: la vieja y la nueva. Las dos entran.
        if estado[0] in ("R", "C"):
            rutas.update(p for p in piezas[indice + 1:indice + 3] if p)
            indice += 3
        else:
            if indice + 1 < len(piezas) and piezas[indice + 1]:
                rutas.add(piezas[indice + 1])
            indice += 2
    return rutas


def comprobar(manifiesto, lecturas, base=RAIZ):
    """Las CUATRO restas. Devuelve `(ok, informe)` y no levanta por cobertura incompleta."""
    informe = {"candidata": manifiesto.get("candidata"), "revisores": {}, "restas": {}}
    # `G-02` · LA CLAVE ERA LA RUTA, Y LA RELACIÓN ES (RUTA, RANGO). ES DEL AUTOR.
    #
    #     Estaba escrito `{f["ruta"]: f for f in fuentes}`: un diccionario indizado por RUTA.
    #     Un fichero asignado por VARIOS rangos colapsaba a UNA clave y **sólo sobrevivía el
    #     último**. El gate del 2026-09-05 lo midió por tres caminos independientes: `REV-2`
    #     declaró leídas 246 de las 4 600 líneas de `11-ARQ` que el manifiesto le asignaba y
    #     la salida salió **byte a byte idéntica** a su lectura honesta; `REV-1` midió 34 922
    #     de 40 630 líneas; `REV-3`, 46 649 de 47 534. Los tres revisores encontraron el
    #     mismo defecto sin verse.
    #
    #     El instrumento existe para impedir que un gate caiga por cobertura, y tenía un
    #     defecto que permitía exactamente eso: leer un tramo y cerrar con la resta vacía.
    #
    # DECISIÓN · la clave es `(ruta, inicio, fin, revisor)` y NO se normaliza a la ruta
    #     Alternativas: (a) prohibir varios rangos del mismo fichero en un lote; (b) fundir
    #     los rangos de una ruta en uno solo; (c) tratar cada asignación como una entrada
    #     propia.
    #     Se elige (c). Con (a) el manifiesto no podría repartir un documento grande por
    #     secciones, que es justo lo que hace falta para que los lotes sean asumibles. Con
    #     (b) se perdería QUIÉN tiene que leer QUÉ tramo, y dos revisores con rangos
    #     distintos del mismo fichero se taparían entre sí. Con (c) cada asignación se mide
    #     por separado, y el revisor aparece en la clave porque la cobertura de uno no
    #     compensa la de otro —`O27` §5—.
    def _clave(revisor, ficha):
        rango = ficha.get("rango")
        if rango:
            return (ficha["ruta"], int(rango[0]), int(rango[1]), revisor)
        return (ficha["ruta"], None, None, revisor)

    asignadas_por_revisor = {}
    for revisor, lote in sorted((manifiesto.get("revisores") or {}).items()):
        entradas = {}
        for ficha in lote.get("fuentes") or []:
            clave = _clave(revisor, ficha)
            if clave in entradas:
                raise ManifiestoIlegible(
                    "`%s` recibe DOS VECES la misma asignación %s: un rango atribuido dos "
                    "veces no describe más lectura, y esconde una asignación que falta"
                    % (revisor, clave[:3]))
            entradas[clave] = ficha
        asignadas_por_revisor[revisor] = entradas

    # `H-06` · LA PRIMERA RESTA ERA UNA TAUTOLOGÍA, Y SE DICE ENTERO PORQUE ES DEL AUTOR
    #
    #     Estaba escrito así: `obligatorio` se construía UNIENDO los lotes, y después se
    #     restaba `declarado_obligatorio - obligatorio` con `declarado_obligatorio` cayendo
    #     por omisión en el mismo conjunto. Es `X − X`. La auditoría del 2026-09-04 lo midió
    #     con dos manifiestos vacuos: `{"revisores":{}}` y `{"REV-1":{"fuentes":[]}}` daban
    #     los dos **COBERTURA COMPLETA · EXIT=0**, y el docstring de este mismo fichero
    #     prometía «devuelve 0 sólo si las CUATRO restas son vacías».
    #
    #     El instrumento medía que se leyera lo asignado, y NO que se asignara lo
    #     obligatorio. `O27` §5 pide las dos cosas: un lote vacío satisfacía la norma sin
    #     leer una línea, que es peor que el defecto que este fichero existe para impedir.
    #
    # DECISIÓN · `OBLIGATORIO` se DERIVA DEL ÁRBOL, y el manifiesto sólo puede AMPLIARLO
    #     Alternativas: (a) exigir que el manifiesto declare `obligatorio` y creerle; (b)
    #     derivarlo del árbol con `git diff` entre la base y la candidata; (c) las dos, con
    #     el árbol como suelo.
    #     Se elige (c). Con (a) volvemos a la declaración —el manifiesto que se equivoca al
    #     asignar se equivoca igual al declarar qué era obligatorio—. Con (b) sola, un
    #     manifiesto no podría añadir una sede normativa que el diff no toca y que sin
    #     embargo hay que leer. Con (c) el suelo lo pone el árbol: **toda fuente MODIFICADA
    #     entre la base y la candidata es obligatoria**, la declaración puede añadir, y
    #     ninguna de las dos puede quitar.
    #
    # DECISIÓN · un manifiesto SIN REVISORES, o con un revisor SIN LOTE, es fallo cerrado
    #     No es una resta vacía: es una medida que no se ha tomado. Se distingue del caso
    #     legítimo «no hay nada obligatorio» —que sobre un árbol real no ocurre— exigiendo
    #     que el universo obligatorio derivado NO esté vacío.
    obligatorio = set()
    for lote in asignadas_por_revisor.values():
        # Las claves son `(ruta, inicio, fin, revisor)` desde `G-02`: lo que cuenta como
        # ASIGNADO es la RUTA, y por eso se extrae en vez de usar la clave entera.
        obligatorio |= {clave[0] for clave in lote}
    # `G-07` · EL COMENTARIO PROMETÍA `git diff` Y EL CÓDIGO LEÍA EL MANIFIESTO. ES DEL AUTOR.
    #
    #     El bloque de decisión de abajo decía «el suelo lo pone el árbol: toda fuente
    #     MODIFICADA entre la base y la candidata es obligatoria, la declaración puede
    #     añadir, y ninguna de las dos puede quitar». El código hacía
    #     `set(manifiesto.get("modificadas") or [])` y el fichero **ni siquiera importaba
    #     `subprocess`**. `H-06` cerró el caso VACÍO; el INFRA-DECLARADO seguía abierto: un
    #     manifiesto con UNA ruta y UNA línea leída satisfacía las cuatro restas de `O27` §5.
    #     Lo midieron dos revisores del gate del 2026-09-05, por separado.
    #
    #     Ahora se deriva de verdad. `--base` y `--candidata` son SHA, y el conjunto sale de
    #     `git diff --name-status -M -C -z`, que da también renombrados y copias con sus DOS
    #     puntas. Lo que el manifiesto declare puede AMPLIAR ese conjunto y no puede quitar
    #     de él ni una ruta.
    derivado = _modificadas_del_arbol(manifiesto, base)
    # EL ORIGEN DEL CONJUNTO SE PUBLICA SIEMPRE, y no sólo cuando se degrada. El mensaje de
    # error de la vía declarada prometía «y quedará publicado» y no publicaba nada: una
    # derivación cuyo origen no consta no es auditable, y un lector no puede distinguir
    # «derivado de 188 ficheros de cambio» de «declarado a mano» mirando el informe.
    informe["derivacion"] = {
        "modo": ("declarada-sin-arbol"
                 if manifiesto.get("derivacion") == "declarada-sin-arbol"
                 else "derivada-del-arbol"),
        "repositorio": os.path.realpath(base),
        "base": manifiesto.get("base"),
        "candidata": manifiesto.get("candidata"),
        "rutas_derivadas": len(derivado),
    }
    declarado = set(manifiesto.get("obligatorio") or []) | set(
        manifiesto.get("modificadas") or [])
    perdidas = derivado - declarado
    if perdidas:
        raise ManifiestoIlegible(
            "el manifiesto declara %d fuentes modificadas y el árbol deriva %d: faltan %s. "
            "El manifiesto CONTRASTA contra el conjunto derivado, no lo define, y no puede "
            "quitar ninguna ruta de él"
            % (len(declarado), len(derivado), ", ".join(sorted(perdidas)[:8])))
    declarado_obligatorio = declarado | derivado
    if not declarado_obligatorio:
        raise ManifiestoIlegible(
            "el manifiesto no declara `modificadas` ni `obligatorio`, de modo que el "
            "universo obligatorio saldría VACÍO y la primera resta sería vacía por "
            "construcción. Un gate cuyo universo no se puede derivar no es un gate con "
            "cobertura completa: es un gate sin medida")
    if not asignadas_por_revisor:
        raise ManifiestoIlegible(
            "el manifiesto no declara ningún revisor: no hay a quién medir la cobertura")
    for revisor, lote in sorted(asignadas_por_revisor.items()):
        if not lote:
            raise ManifiestoIlegible(
                "el lote de `%s` está VACÍO. Un lote vacío satisface toda resta de lectura "
                "sin leer una línea, que es exactamente lo que `O27` §5 prohíbe" % revisor)
    informe["restas"]["obligatorio_menos_asignado"] = sorted(
        declarado_obligatorio - obligatorio)

    modificadas = set(manifiesto.get("modificadas") or [])
    leidas_integras = set()
    resta_lectura, resta_lineas, no_cerrados, sha_divergente = [], [], [], []

    for lectura in lecturas:
        revisor = lectura.get("revisor")
        if revisor not in asignadas_por_revisor:
            raise ManifiestoIlegible(
                "el manifiesto de lectura declara el revisor `%s`, que el manifiesto de "
                "asignación no conoce: %s" % (revisor, ", ".join(sorted(asignadas_por_revisor))))
        asignadas = asignadas_por_revisor[revisor]
        leidas = {}
        for entrada in lectura.get("leidas") or []:
            leidas.setdefault(entrada["ruta"], []).append(entrada)
        # Una fuente leída que NADIE le asignó no compensa nada: `O27` §5 prohíbe
        # expresamente compensar con lo leído por otro agente, y con más razón con lo leído
        # fuera del lote propio.
        rutas_asignadas = {c[0] for c in asignadas}
        cubierto_de = {}
        ajenas = sorted(set(leidas) - rutas_asignadas)
        pendientes, tramos_pendientes = [], []
        for clave, ficha in sorted(asignadas.items(),
                                   key=lambda x: (x[0][0], x[0][1] or 0)):
            ruta = clave[0]
            etiqueta = ruta if clave[1] is None else "%s [%d-%d]" % (ruta, clave[1], clave[2])
            sha_arbol, lineas_arbol = _sha256_y_lineas(base, ruta)
            if sha_arbol is None:
                raise ManifiestoIlegible(
                    "el manifiesto asigna `%s`, que no existe en el árbol comprobado" % ruta)
            if ficha.get("sha256") and ficha["sha256"] != sha_arbol:
                raise ManifiestoIlegible(
                    "el manifiesto declara para `%s` un sha256 que no es el del árbol: el "
                    "lote describe otro objeto" % ruta)
            # `G-01` · un rango tiene que caber en el fichero. `N+1` no se lee: no existe.
            rango = ficha.get("rango")
            if rango and (int(rango[0]) < 1 or int(rango[1]) > lineas_arbol
                          or int(rango[0]) > int(rango[1])):
                raise ManifiestoIlegible(
                    "el manifiesto asigna a `%s` el rango %d-%d sobre `%s`, que tiene %d "
                    "líneas: un rango que no cabe en el fichero no se puede leer, y un lote "
                    "que lo contiene NO PUEDE CERRARSE. Es exactamente lo que hundió al gate "
                    "del 2026-09-05" % (revisor, int(rango[0]), int(rango[1]), ruta,
                                        lineas_arbol))
            if ruta not in leidas:
                pendientes.append(etiqueta)
                continue
            # Todos los tramos que el revisor declaró para esa ruta, vengan en una entrada o
            # en varias: lo que se mide es la UNIÓN de lo leído contra CADA rango asignado.
            entradas = leidas[ruta]
            if any(e.get("sha256") and e["sha256"] != sha_arbol for e in entradas):
                sha_divergente.append("%s · %s" % (revisor, ruta))
                pendientes.append(etiqueta)
                continue
            leida = {"tramos": [tr for e in entradas for tr in (e.get("tramos") or [])]}
            desde, hasta = (rango if rango else [1, lineas_arbol])
            # `H-06` · un tramo `[1, 999999]` sobre un fichero de dos líneas no es una
            # lectura: es una declaración que no puede ser cierta. Se rechaza en vez de
            # aceptarla como cobertura holgada, porque el modo de fallo que este instrumento
            # persigue es precisamente el de la declaración cómoda.
            for inicio_t, fin_t in (leida.get("tramos") or []):
                if int(fin_t) > lineas_arbol or int(inicio_t) < 1:
                    raise ManifiestoIlegible(
                        "`%s` declara el tramo %s-%s sobre `%s`, que tiene %d líneas: un "
                        "tramo fuera del fichero no describe ninguna lectura"
                        % (revisor, inicio_t, fin_t, ruta, lineas_arbol))
            huecos = _faltantes(leida.get("tramos") or [], int(desde), int(hasta))
            if huecos:
                sin_leer = sum(b - a + 1 for a, b in huecos)
                tramos_pendientes.append({
                    "ruta": etiqueta, "revisor": revisor, "huecos": huecos,
                    "lineas_sin_leer": sin_leer,
                })
            elif ruta in modificadas:
                # Una fuente MODIFICADA cuenta como leída ÍNTEGRA cuando lo LEÍDO cubre
                # `[1, N]` entero, venga de una asignación sola o de varias que se reparten
                # el fichero. Un rango parcial NO la agota, y por eso la comprobación se
                # hace sobre la UNIÓN y no sobre esta asignación: es la regla que los
                # manifiestos de este expediente escriben desde el principio —«cobertura
                # histórica delegada prohibida para un fichero modificado»— y que hasta
                # ahora no se comprobaba.
                cubierto_de.setdefault(ruta, []).extend(leida["tramos"])
                if not _faltantes(cubierto_de[ruta], 1, lineas_arbol):
                    leidas_integras.add(ruta)
        if pendientes:
            resta_lectura.extend("%s · %s" % (revisor, r) for r in pendientes)
        resta_lineas.extend(tramos_pendientes)
        informe["revisores"][revisor] = {
            "asignadas": len(asignadas),
            "leidas_sin_hueco": len(asignadas) - len(pendientes) - len(tramos_pendientes),
            "sin_abrir": len(pendientes),
            "con_huecos": len(tramos_pendientes),
            "lineas_asignadas": sum(
                (int(f["rango"][1]) - int(f["rango"][0]) + 1) if f.get("rango")
                else (_sha256_y_lineas(base, f["ruta"])[1] or 0)
                for f in asignadas.values()),
            "lineas_sin_leer": sum(t["lineas_sin_leer"] for t in tramos_pendientes),
            "fuentes_ajenas_declaradas": ajenas,
            "cerrado_declarado": bool(lectura.get("cerrado")),
        }
        if not lectura.get("cerrado"):
            no_cerrados.append(revisor)

    sin_lectura = sorted(set(asignadas_por_revisor) - {l.get("revisor") for l in lecturas})
    informe["restas"]["asignado_menos_leido"] = sorted(resta_lectura)
    informe["restas"]["lineas_asignadas_menos_leidas"] = resta_lineas
    informe["restas"]["modificadas_menos_leidas_integras"] = sorted(
        modificadas - leidas_integras)
    informe["revisores_sin_manifiesto_de_lectura"] = sin_lectura
    informe["revisores_no_cerrados"] = no_cerrados
    informe["sha_divergente"] = sha_divergente

    ok = not (informe["restas"]["obligatorio_menos_asignado"]
              or informe["restas"]["asignado_menos_leido"]
              or informe["restas"]["lineas_asignadas_menos_leidas"]
              or informe["restas"]["modificadas_menos_leidas_integras"]
              or sin_lectura or no_cerrados or sha_divergente)
    informe["cobertura"] = "COMPLETA" if ok else "INCOMPLETA"
    return ok, informe


# ───────────────────────────────────────────────────────────────────────────────────────
#  AUTOPRUEBAS · un instrumento que decide si un gate puede adjudicar tiene que demostrar
#  que PUEDE FALLAR, y demostrarlo en la corrida, no en un informe.
#
#  Los seis modos son los seis por los que una cobertura puede estar incompleta, y cada uno
#  se ejerce por separado: si uno dejara de discriminar, el instrumento seguiría dando verde
#  sobre un lote sin leer, que es exactamente el defecto que existe para impedir.
# ───────────────────────────────────────────────────────────────────────────────────────
def _autopruebas(base):
    import tempfile                                                  # noqa: PLC0415
    controles, sin_detectar = [], []
    with tempfile.TemporaryDirectory(prefix="ads-cobertura-") as taller:
        uno = os.path.join(taller, "uno.txt")
        dos = os.path.join(taller, "dos.txt")
        with io.open(uno, "w", encoding="utf-8") as manejador:
            manejador.write("\n".join("linea %d" % n for n in range(1, 41)) + "\n")
        with io.open(dos, "w", encoding="utf-8") as manejador:
            manejador.write("\n".join("otra %d" % n for n in range(1, 21)) + "\n")

        def ficha(ruta, rango=None):
            sha, lineas = _sha256_y_lineas(taller, os.path.basename(ruta))
            return {"ruta": os.path.basename(ruta), "lineas": lineas,
                    "sha256": sha, "rango": rango}

        manifiesto = {
            "candidata": "AUTOPRUEBA",
            "derivacion": "declarada-sin-arbol",
            "modificadas": [os.path.basename(uno)],
            "revisores": {
                "REV-1": {"fuentes": [ficha(uno)]},
                "REV-2": {"fuentes": [ficha(dos)]},
            },
        }
        completo_1 = {"revisor": "REV-1", "cerrado": True,
                      "leidas": [{"ruta": "uno.txt", "tramos": [[1, 40]],
                                  "sha256": ficha(uno)["sha256"]}]}
        completo_2 = {"revisor": "REV-2", "cerrado": True,
                      "leidas": [{"ruta": "dos.txt", "tramos": [[1, 20]],
                                  "sha256": ficha(dos)["sha256"]}]}

        def caso(nombre, lecturas, espera_ok, espera_en_informe=None,
                 manifiesto_propio=None):
            ok, informe = comprobar(manifiesto_propio or manifiesto, lecturas, base=taller)
            bien = (ok == espera_ok)
            if bien and espera_en_informe:
                bien = bool(informe["restas"].get(espera_en_informe)
                            or informe.get(espera_en_informe))
            controles.append((nombre, "ok" if bien else "SIN DETECTAR"))
            if not bien:
                sin_detectar.append(nombre)

        import copy                                                   # noqa: PLC0415
        caso("control POSITIVO · dos lotes leídos enteros", [completo_1, completo_2], True)
        caso("una fuente SIN ABRIR",
             [{"revisor": "REV-1", "cerrado": True, "leidas": []}, completo_2],
             False, "asignado_menos_leido")
        hueco = copy.deepcopy(completo_1)
        hueco["leidas"][0]["tramos"] = [[1, 10]]
        caso("un HUECO de líneas dentro de la fuente", [hueco, completo_2],
             False, "lineas_asignadas_menos_leidas")
        ajeno = copy.deepcopy(completo_2)
        ajeno["leidas"].append({"ruta": "uno.txt", "tramos": [[1, 40]],
                                "sha256": ficha(uno)["sha256"]})
        caso("un revisor intenta COMPENSAR lo que otro no leyó",
             [{"revisor": "REV-1", "cerrado": True, "leidas": []}, ajeno],
             False, "asignado_menos_leido")
        otro_sha = copy.deepcopy(completo_1)
        otro_sha["leidas"][0]["sha256"] = "0" * 64
        caso("leyó OTRO OBJETO · sha256 divergente", [otro_sha, completo_2],
             False, "sha_divergente")
        abierto = copy.deepcopy(completo_1)
        abierto["cerrado"] = False
        caso("lote declarado NO CERRADO", [abierto, completo_2],
             False, "revisores_no_cerrados")
        caso("un revisor SIN manifiesto de lectura", [completo_1],
             False, "revisores_sin_manifiesto_de_lectura")

        # `H-06` · LOS TRES CASOS VACUOS. La auditoría midió que las siete autopruebas
        # anteriores NO ejercían ninguno, y que los tres daban COBERTURA COMPLETA con
        # EXIT=0. Un instrumento que sólo se prueba con manifiestos bien formados no mide
        # su propio modo de fallo más barato: el del manifiesto que no asigna nada.
        def caso_ilegible(nombre, manifiesto_hostil, lecturas):
            try:
                comprobar(manifiesto_hostil, lecturas, base=taller)
            except ManifiestoIlegible:
                controles.append((nombre, "ok"))
                return
            controles.append((nombre, "SIN DETECTAR"))
            sin_detectar.append(nombre)

        caso_ilegible("manifiesto SIN revisores", {"candidata": "X", "derivacion": "declarada-sin-arbol", "revisores": {},
                                                   "modificadas": ["uno.txt"]}, [])
        caso_ilegible("un revisor con el LOTE VACÍO",
                      {"candidata": "X", "derivacion": "declarada-sin-arbol", "modificadas": ["uno.txt"],
                       "revisores": {"REV-1": {"fuentes": []}}}, [])
        caso_ilegible("universo obligatorio VACÍO por construcción",
                      {"candidata": "X", "derivacion": "declarada-sin-arbol",
                       "revisores": {"REV-1": {"fuentes": [ficha(uno)]}}},
                      [completo_1])
        fuera = copy.deepcopy(completo_1)
        fuera["leidas"][0]["tramos"] = [[1, 999999]]
        caso_ilegible("un TRAMO fuera del fichero declarado como lectura",
                      manifiesto, [fuera, completo_2])

        # ── `G-01` y `G-02`, reproducidos EXACTAMENTE como el gate del 2026-09-05 los
        #    encontró. No son casos hipotéticos: son los dos defectos que hundieron aquel
        #    gate, uno en el manifiesto y otro en este mismo fichero.
        def man_con(fuentes_1, modificadas=None):
            return {"candidata": "X", "derivacion": "declarada-sin-arbol",
                    "modificadas": modificadas if modificadas is not None else ["uno.txt"],
                    "revisores": {"REV-1": {"fuentes": fuentes_1},
                                  "REV-2": {"fuentes": [ficha(dos)]}}}

        # `G-01` · la línea N+1. El manifiesto del gate anterior asignaba 11907-12153 sobre
        #          un fichero de 12152 líneas, y el lote NO PODÍA cerrarse jamás.
        caso_ilegible("`G-01` · un rango que llega a N+1, la línea que no existe",
                      man_con([ficha(uno, [1, 41])]), [completo_1, completo_2])
        caso_ilegible("`G-01` · un rango que empieza en 0",
                      man_con([ficha(uno, [0, 40])]), [completo_1, completo_2])
        caso_ilegible("`G-01` · un rango invertido, fin antes que inicio",
                      man_con([ficha(uno, [30, 10])]), [completo_1, completo_2])

        # `G-01` · las líneas 1-94 sin asignar. Aquí, 1-9 de `uno.txt`.
        parcial = {"revisor": "REV-1", "cerrado": True,
                   "leidas": [{"ruta": "uno.txt", "tramos": [[10, 40]],
                               "sha256": ficha(uno)["sha256"]}]}
        caso("`G-01` · el arranque del fichero sin asignar se ve como líneas SIN LEER",
             [parcial, completo_2], False, "lineas_asignadas_menos_leidas")

        # `G-02` · DOS rangos del mismo fichero. Con la indexación por ruta, sólo se medía
        #          el último: leer 21-40 y callar 1-20 cerraba con la resta vacía.
        dos_rangos = man_con([ficha(uno, [1, 20]), ficha(uno, [21, 40])])
        solo_el_ultimo = {"revisor": "REV-1", "cerrado": True,
                          "leidas": [{"ruta": "uno.txt", "tramos": [[21, 40]],
                                      "sha256": ficha(uno)["sha256"]}]}
        caso("`G-02` · dos rangos y sólo el ÚLTIMO leído — el defecto que hundió el gate",
             [solo_el_ultimo, completo_2], False, "lineas_asignadas_menos_leidas",
             manifiesto_propio=dos_rangos)
        los_dos = {"revisor": "REV-1", "cerrado": True,
                   "leidas": [{"ruta": "uno.txt", "tramos": [[1, 20], [21, 40]],
                               "sha256": ficha(uno)["sha256"]}]}
        caso("`G-02` · control POSITIVO · dos rangos y los DOS leídos",
             [los_dos, completo_2], True, manifiesto_propio=dos_rangos)
        caso_ilegible("`G-02` · el MISMO rango atribuido dos veces al mismo revisor",
                      man_con([ficha(uno, [1, 40]), ficha(uno, [1, 40])]),
                      [completo_1, completo_2])

        # solapamiento y hueco de UNA línea
        solapa = man_con([ficha(uno, [1, 25]), ficha(uno, [20, 40])])
        caso("`G-02` · rangos que SOLAPAN se miden los dos, no uno",
             [{"revisor": "REV-1", "cerrado": True,
               "leidas": [{"ruta": "uno.txt", "tramos": [[1, 25]],
                           "sha256": ficha(uno)["sha256"]}]}, completo_2],
             False, "lineas_asignadas_menos_leidas", manifiesto_propio=solapa)
        hueco_uno = copy.deepcopy(completo_1)
        hueco_uno["leidas"][0]["tramos"] = [[1, 19], [21, 40]]
        caso("`G-02` · un hueco de UNA sola línea", [hueco_uno, completo_2],
             False, "lineas_asignadas_menos_leidas")

        # `G-07` · el conjunto obligatorio INFRA-DECLARADO: una ruta y una línea leída
        #          satisfacían las cuatro restas.
        caso("`G-07` · una fuente modificada OMITIDA del manifiesto",
             [completo_1, completo_2], False, "obligatorio_menos_asignado",
             manifiesto_propio={"candidata": "X", "derivacion": "declarada-sin-arbol",
                                "modificadas": ["uno.txt", "dos.txt", "tres.txt"],
                                "revisores": {"REV-1": {"fuentes": [ficha(uno)]},
                                              "REV-2": {"fuentes": [ficha(dos)]}}})
        caso_ilegible("`G-07` · sin `base` y `candidata` NO se puede derivar: falla cerrado",
                      {"candidata": "X", "modificadas": ["uno.txt"],
                       "revisores": {"REV-1": {"fuentes": [ficha(uno)]}}}, [completo_1])


        # ==================================================================
        #  `G-07` · LA DERIVACIÓN DESDE EL ÁRBOL, EJERCIDA SOBRE UN GIT REAL
        # ==================================================================
        #  HECHO REPRODUCIDO POR EL AUDITOR INDEPENDIENTE. Los controles de arriba llevan
        #  todos `"derivacion": "declarada-sin-arbol"`, de modo que `_modificadas_del_arbol`
        #  no llegaba nunca a `subprocess.run`. El auditor lo midió poniendo un `git`
        #  instrumentado delante en el `PATH`:
        #
        #      $ PATH=…/falso:$PATH python3.12 …/comprobar-cobertura-de-gate.py --autopruebas
        #        23 controles · 0 sin detectar
        #      $ wc -l < …/git-llamadas.txt
        #        0
        #
        #  Con el control positivo de la sonda —`comprobar_evidencia.py`, mismo `PATH`— la
        #  cuenta era 32. La sonda funcionaba: era la derivación la que no se ejercía.
        #
        #  Es la clase de `G-05` —el instrumento cuyo autotest pasa y cuyo producto nadie
        #  ejerce— reaparecida dentro del instrumento que `G-05` no cubría. Y en la misma
        #  pasada `D-05` demostró que se sabe montar un repositorio Git de verdad dentro de
        #  una prueba: la disciplina existía y no se había aplicado aquí.
        #
        #  Estos controles montan un repositorio REAL —`git init`, dos commits— y ejercen
        #  las formas que el separador `-z` y las banderas `-M -C` existen para sostener:
        #  modificado, alta, baja, RENOMBRADO, COPIA, ruta NO ASCII con espacio y ruta con
        #  un SALTO DE LÍNEA en el nombre.
        import subprocess                                              # noqa: PLC0415

        entorno_git = dict(os.environ)
        entorno_git.update({
            "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull,
            "GIT_AUTHOR_NAME": "ads-g07", "GIT_AUTHOR_EMAIL": "g07@ads.local",
            "GIT_COMMITTER_NAME": "ads-g07", "GIT_COMMITTER_EMAIL": "g07@ads.local",
            "GIT_AUTHOR_DATE": "2026-01-01T00:00:00+00:00",
            "GIT_COMMITTER_DATE": "2026-01-01T00:00:00+00:00",
        })

        def _git(repo, *orden):
            proceso = subprocess.run(["git", "-C", repo] + list(orden),
                                     capture_output=True, text=True, env=entorno_git)
            if proceso.returncode != 0:
                raise RuntimeError("git %s: %s" % (" ".join(orden), proceso.stderr))
            return proceso.stdout

        def _escribir(repo, rel, contenido):
            destino = os.path.join(repo, rel)
            carpeta = os.path.dirname(destino)
            if carpeta:
                os.makedirs(carpeta, exist_ok=True)
            with io.open(destino, "w", encoding="utf-8") as manejador:
                manejador.write(contenido)

        arbol = os.path.join(taller, "repo-de-verdad")
        os.makedirs(arbol)
        _git(arbol, "init", "-q", "-b", "principal")
        _escribir(arbol, "modificado.txt", "uno\n")
        _escribir(arbol, "borrado.txt", "se va\n")
        _escribir(arbol, "viejo-nombre.txt", "\n".join("r %d" % n for n in range(60)))
        _escribir(arbol, "ñandú con espacio.txt", "\n".join("c %d" % n for n in range(60)))
        _git(arbol, "add", "-A")
        _git(arbol, "commit", "-q", "-m", "base")
        sha_base = _git(arbol, "rev-parse", "HEAD").strip()

        _escribir(arbol, "modificado.txt", "uno\ndos\n")
        _escribir(arbol, "alta.txt", "nuevo\n")
        os.remove(os.path.join(arbol, "borrado.txt"))
        os.rename(os.path.join(arbol, "viejo-nombre.txt"),
                  os.path.join(arbol, "nuevo-nombre.txt"))
        # UNA COPIA, con su fuente TAMBIÉN modificada. Es la condición que `git` necesita
        # para publicar `C100`: si la fuente no entra en el diff, la copia sale como un alta
        # corriente y este control no estaría midiendo `-C`. Se comprobó en el árbol:
        #
        #     fuente intacta      → `A  copiado.txt`
        #     fuente modificada   → `C100  "\303\261and\303\272 con espacio.txt"  copiado.txt`
        #                           `M     "\303\261and\303\272 con espacio.txt"`
        with io.open(os.path.join(arbol, "ñandú con espacio.txt"),
                     encoding="utf-8") as manejador:
            original = manejador.read()
        _escribir(arbol, "copiado.txt", original)
        _escribir(arbol, "ñandú con espacio.txt", original + "\nuna línea más\n")
        # y una ruta con un SALTO DE LÍNEA en el nombre, que es lo que `-z` sostiene y `\n`
        # como separador partiría en dos, perdiendo la mitad SIN QUE NADA LO DIGA
        con_salto = "raro\ncon-salto.txt"
        ruta_hostil = True
        try:
            _escribir(arbol, con_salto, "hostil\n")
        except OSError:
            ruta_hostil = False                       # sistema de ficheros que no lo admite
        _git(arbol, "add", "-A")
        _git(arbol, "commit", "-q", "-m", "candidata")
        sha_candidata = _git(arbol, "rev-parse", "HEAD").strip()

        derivado = _modificadas_del_arbol(
            {"base": sha_base, "candidata": sha_candidata}, arbol)
        esperado = {"modificado.txt", "alta.txt", "borrado.txt",
                    "viejo-nombre.txt", "nuevo-nombre.txt",
                    "ñandú con espacio.txt", "copiado.txt"}
        if ruta_hostil:
            esperado.add(con_salto)
        controles.append((
            "`G-07` · control POSITIVO · git REAL: M, A, D, renombrado, copia, ruta no "
            "ASCII y ruta con salto de línea",
            "ok" if derivado == esperado else "NO"))
        if derivado != esperado:
            sin_detectar.append(
                "la derivación del árbol devolvió %s y se esperaba %s"
                % (sorted(derivado), sorted(esperado)))

        # Y las DOS PUERTAS TRASERAS que el auditor abrió, cerradas y medidas.
        def _puerta(nombre, manifiesto_puerta, raiz_puerta):
            try:
                _modificadas_del_arbol(manifiesto_puerta, raiz_puerta)
            except ManifiestoIlegible:
                controles.append((nombre, "ok"))
                return
            controles.append((nombre, "NO"))
            sin_detectar.append(nombre)

        _puerta("`G-07` · el manifiesto NO elige el repositorio: `repositorio` ajeno",
                {"base": sha_base, "candidata": sha_candidata, "repositorio": taller},
                arbol)
        _puerta("`G-07` · `base` == `candidata` derivaría el conjunto VACÍO: falla cerrado",
                {"base": sha_base, "candidata": sha_base}, arbol)

        # un manifiesto de lectura de OTRO gate
        ajeno = {"revisor": "REV-9", "cerrado": True, "leidas": []}
        caso_ilegible("un manifiesto de lectura de OTRO gate, con un revisor desconocido",
                      manifiesto, [ajeno])
    return controles, sin_detectar


def main():
    analizador = argparse.ArgumentParser(
        description="comprueba mecánicamente la cobertura de un gate")
    analizador.add_argument("--autopruebas", action="store_true",
                            help="ejerce los modos de fallo del propio instrumento")
    analizador.add_argument("--manifiesto")
    analizador.add_argument("--lectura", nargs="*", default=[])
    analizador.add_argument("--raiz", default=RAIZ)
    analizador.add_argument("--json", action="store_true")
    argumentos = analizador.parse_args()
    if argumentos.autopruebas:
        controles, sin_detectar = _autopruebas(os.path.abspath(argumentos.raiz))
        for nombre, resultado in controles:
            sys.stdout.write("  %-4s %s\n" % (resultado if resultado != "ok" else "ok  ",
                                              nombre))
        sys.stdout.write("\n  %d controles · %d sin detectar\n"
                         % (len(controles), len(sin_detectar)))
        return COBERTURA_COMPLETA if not sin_detectar else COBERTURA_INCOMPLETA
    if not argumentos.manifiesto:
        sys.stderr.write("NO SE PUDO COMPROBAR · falta `--manifiesto`\n")
        return NO_SE_PUDO_COMPROBAR
    try:
        manifiesto = _leer_json(argumentos.manifiesto)
        lecturas = [_leer_json(r) for r in argumentos.lectura]
        ok, informe = comprobar(manifiesto, lecturas, base=os.path.abspath(argumentos.raiz))
    except ManifiestoIlegible as error:
        sys.stderr.write("NO SE PUDO COMPROBAR · %s\n" % error)
        return NO_SE_PUDO_COMPROBAR

    if argumentos.json:
        sys.stdout.write(json.dumps(informe, ensure_ascii=False, indent=2) + "\n")
        return COBERTURA_COMPLETA if ok else COBERTURA_INCOMPLETA

    sys.stdout.write("COBERTURA DEL GATE · candidata %s\n" % informe["candidata"])
    sys.stdout.write("=" * 78 + "\n")
    # DE DÓNDE SALE EL CONJUNTO OBLIGATORIO. Lo primero que se imprime, porque todo lo que
    # viene debajo se mide contra él: si el conjunto se declaró en vez de derivarse, las
    # cuatro restas miden lo que alguien escribió y no lo que el árbol cambió.
    derivacion = informe.get("derivacion") or {}
    sys.stdout.write(
        "  ORIGEN DEL CONJUNTO OBLIGATORIO · %s\n"
        "           repositorio %s\n"
        "           base %s · candidata %s · rutas derivadas del árbol: %d\n"
        % (derivacion.get("modo", "?"), derivacion.get("repositorio", "?"),
           (derivacion.get("base") or "—")[:12],
           (derivacion.get("candidata") or "—")[:12],
           derivacion.get("rutas_derivadas", 0)))
    if derivacion.get("modo") == "declarada-sin-arbol":
        sys.stdout.write(
            "           ATENCIÓN · el conjunto NO se ha derivado del árbol: lo declara el\n"
            "           manifiesto. La declaración contrasta, no define, y aquí no hay\n"
            "           contra qué contrastarla\n")
    sys.stdout.write("=" * 78 + "\n")
    for revisor, ficha in sorted(informe["revisores"].items()):
        sys.stdout.write(
            "  %-8s asignadas %3d · leídas sin hueco %3d · sin abrir %3d · con huecos %3d\n"
            "           líneas asignadas %6d · sin leer %6d · cerrado declarado: %s\n"
            % (revisor, ficha["asignadas"], ficha["leidas_sin_hueco"], ficha["sin_abrir"],
               ficha["con_huecos"], ficha["lineas_asignadas"], ficha["lineas_sin_leer"],
               "sí" if ficha["cerrado_declarado"] else "NO"))
        if ficha["fuentes_ajenas_declaradas"]:
            sys.stdout.write(
                "           NO COMPENSA · fuentes declaradas fuera de su lote: %s\n"
                % ", ".join(ficha["fuentes_ajenas_declaradas"]))
    sys.stdout.write("\nLAS CUATRO RESTAS\n" + "-" * 78 + "\n")
    for clave, titulo in (
            ("obligatorio_menos_asignado", "OBLIGATORIO − ASIGNADO"),
            ("asignado_menos_leido", "ASIGNADO − LEÍDO"),
            ("lineas_asignadas_menos_leidas", "LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS"),
            ("modificadas_menos_leidas_integras",
             "FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS")):
        valor = informe["restas"][clave]
        sys.stdout.write("  %-38s %s\n" % (titulo, "∅" if not valor else len(valor)))
        for entrada in valor[:40]:
            if isinstance(entrada, dict):
                sys.stdout.write(
                    "      %s · %s · faltan %d líneas en %s\n"
                    % (entrada["revisor"], entrada["ruta"], entrada["lineas_sin_leer"],
                       ", ".join("%d-%d" % (a, b) for a, b in entrada["huecos"][:6])))
            else:
                sys.stdout.write("      %s\n" % entrada)
    if informe["revisores_sin_manifiesto_de_lectura"]:
        sys.stdout.write("  SIN MANIFIESTO DE LECTURA: %s\n"
                         % ", ".join(informe["revisores_sin_manifiesto_de_lectura"]))
    if informe["revisores_no_cerrados"]:
        sys.stdout.write("  LOTE NO CERRADO: %s\n" % ", ".join(informe["revisores_no_cerrados"]))
    if informe["sha_divergente"]:
        sys.stdout.write("  LEYÓ OTRO OBJETO: %s\n" % ", ".join(informe["sha_divergente"]))
    sys.stdout.write("\n  COBERTURA %s\n" % informe["cobertura"])
    if not ok:
        sys.stdout.write(
            "  El adjudicador NO puede crearse. `O27` §5: el lote no se cierra, no se\n"
            "  sustituye con búsquedas y no se compensa con lo leído por otro agente.\n")
    return COBERTURA_COMPLETA if ok else COBERTURA_INCOMPLETA


if __name__ == "__main__":
    sys.exit(main())
