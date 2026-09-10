#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
`O30` · EL CATÁLOGO CERRADO `K01`–`K24`, DERIVADO Y EJERCIDO
============================================================

POR QUÉ EXISTE ESTE FICHERO
---------------------------
`O30` §1 rechaza la unidad con la que `O26-SAB` medía —una cláusula `falla_si`, clasificada
por las palabras que contiene— y §2 la sustituye por VEINTICUATRO invariantes
arquitectónicos nombrados uno a uno. Cambiar la unidad no basta: mientras nadie la mida, el
catálogo es prosa. Este punto lo convierte en HECHO MECÁNICO.

LA UNIDAD, Y DE DÓNDE SALE
--------------------------
El conjunto de invariantes **NO SE ESCRIBE AQUÍ NI EN NINGUNA SEDE**: se DERIVA leyendo la
resolución `O30` §2 de `docs/owner/ADS-OWNER-RESOLUCIONES.md`, que es su sede canónica y
está bajo cliquet de append-only. De ahí salen el conjunto —`K01`…`K24`— y la FORMULACIÓN
LITERAL de cada uno. La sede canónica del catálogo
—`docs/canonico/08-INVARIANTES-CRITICOS-DE-F6.md`— aporta lo demás: fuentes, implementación,
canal, pruebas, evidencia, estado y límites. Si las dos no coinciden EXACTAMENTE, esto sale
rojo. **En ninguna de las dos hay un cardinal escrito a mano**, y por eso el día que el Owner
inscriba un `K25` el instrumento lo exigirá solo.

QUÉ SE EXIGE POR INVARIANTE — `O30` §3, punto por punto
--------------------------------------------------------
  1 fuente normativa            → `C-04`   ruta que existe y ancla que aparece en ella
  2 mecanismo implementado      → `C-05`   rutas de implementación que existen en el árbol
  3 canal productivo ejercido   → `C-06`   el canal DECLARADO es el que sus sabotajes corren
  4 al menos un caso sano       → `C-07`   la prueba positiva figura SUPERADA en su evidencia
  5 prueba adversarial capaz de
    poner rojo el mecanismo     → `C-08`   sabotaje del catálogo único, ligado a una positiva
  6 resultado esperado          → `C-11`   se EJECUTA, y lo observado tiene que coincidir
  7 evidencia reproducible      → `C-09`   evidencia publicada, en el árbol
  8 vínculo a commit y tree     → `C-09`   su blob es el de `HEAD`, o no cuenta

LAS TRECE CONDICIONES DE FALLO CERRADO
--------------------------------------
  `C-01` falta un `K` del catálogo derivado
  `C-02` sobra un `K` que `O30` §2 no autoriza
  `C-03` la formulación de la sede no es la LITERAL de `O30` §2
  `C-04` un `K` sin fuente normativa, o con una fuente que no existe o no dice lo que cita
  `C-05` un `K` sin implementación, o con una ruta que no está en el árbol
  `C-06` un `K` sin canal productivo, o con un canal que no es el que ejercen sus sabotajes
  `C-07` un `K` sin prueba positiva, o con una positiva que su evidencia no da por superada
  `C-08` un `K` sin prueba adversarial, o con un sabotaje que no existe o no la nombra
  `C-09` un `K` sin evidencia, o con evidencia que no está ligada al commit y al tree
  `C-10` una prueba COMPARTIDA entre invariantes que no explica su vínculo con cada uno
  `C-11` el resultado OBSERVADO al ejercer el sabotaje no coincide con el esperado
  `C-12` el commit o el tree no corresponden al objeto juzgado
  `C-13` una prueba se salta, o un ejecutable requerido no llega a ejercerse

LA PRUEBA COMPARTIDA, Y LAS CUATRO CONDICIONES DE `O30` §3
-----------------------------------------------------------
Un mismo sabotaje puede acreditar a varios invariantes SÓLO si (a) ejecuta de verdad el
mecanismo compartido —aquí se ejecuta, no se lee—; (b) el vínculo prueba→invariante se
declara sin ambigüedad —lo impone `C-08`: el sabotaje tiene que apuntar a una prueba que el
propio invariante declara como positiva—; (c) se explica qué observación DISTINTA demuestra
para cada uno —lo impone `C-10`: sin una línea `vinculo:` por cada invariante que lo comparte,
rojo—; y (d) al retirar la protección común la prueba se pone roja POR EL MOTIVO DECLARADO
—lo impone `C-11`, que es el `espera` del catálogo de mutaciones—.

CÓMO SE EJERCE, Y QUÉ SIGNIFICA «SANO / SABOTAJE / RESTAURADO»
---------------------------------------------------------------
  SANO        la evidencia publicada, LIGADA al commit y al tree, dice que la prueba
              positiva quedó superada sobre este objeto. No se vuelve a correr para decir
              que el árbol sano está verde: se comprueba que la evidencia que lo dice es
              la de ESTE árbol, blob a blob.
  SABOTAJE    `comprobar_negativos` copia el corpus, mete la infracción EN CÓDIGO
              PRODUCTIVO, ejecuta el canal y exige que caiga la prueba declarada Y por el
              motivo declarado. Esto se EJECUTA en cada pasada.
  RESTAURADO  la mutación vive y muere en una copia temporal. Lo que aquí se comprueba
              —y se publica— es que, terminado el ciclo, cada ruta de implementación y cada
              evidencia del árbol JUZGADO siguen teniendo el mismo blob que antes de
              empezar. Es la forma honesta de decir «restaurado» cuando el original nunca
              se tocó, y se dice así en vez de afirmar una restauración que no ocurrió.

LO QUE ESTE INSTRUMENTO **NO** DEMUESTRA — y va antes que las cifras
--------------------------------------------------------------------
  · no demuestra que un invariante sea INDERROTABLE. Demuestra que el sabotaje declarado lo
    alcanza y que el canal cae por su motivo. Un camino distinto que lo derrote sigue siendo
    posible, y se cierra añadiendo sabotajes, no midiendo mejor;
  · no juzga si la adscripción de una propiedad a un `Knn` es la CORRECTA. Juzga que el
    vínculo esté declarado, que el sabotaje nombre una prueba que el invariante declara, y
    que la ejecución lo confirme. La adscripción la decide `O30` §2 y la escribe la sede;
  · no mide las obligaciones funcionales NO críticas de `O30` §4: ésas son de
    `O26-IMPL`, con otro universo y otro criterio;
  · no ejerce las ocho condiciones de `O26` §1 (`O30` §5), ni `M-04`, ni `C-L.7`;
  · no certifica `F6`. `O30` §7 reserva eso a un verificador independiente.

FALLA CERRADO
-------------
Si la resolución no se puede leer, si la sede no se puede leer, si el catálogo de mutaciones
no se puede importar o si el árbol no está en un repositorio con `HEAD` legible, sale con
código 2 y diagnóstico. **No aprueba por ausencia de dato.**

USO
    …/comprobar-invariantes-criticos.py                 # deriva, comprueba y EJERCE
    …/comprobar-invariantes-criticos.py --sin-ejercer   # sólo estructura (se dice, y no acredita)
    …/comprobar-invariantes-criticos.py --solo K13      # un invariante
    …/comprobar-invariantes-criticos.py --autopruebas   # los trece modos de fallo, saboteados
    …/comprobar-invariantes-criticos.py --json

Códigos de salida: 0 los veinticuatro satisfechos · 1 hay incumplidos · 2 no se pudo comprobar
"""
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
import re
import subprocess
import sys
import tempfile

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

SEDE_DEL_OWNER = "docs/owner/ADS-OWNER-RESOLUCIONES.md"
SEDE_DEL_CATALOGO = "docs/canonico/08-INVARIANTES-CRITICOS-DE-F6.md"
VALIDADORES = "kernel/operativo/validadores"
NEGATIVOS = VALIDADORES + "/comprobar_negativos.py"
EVIDENCIA = "kernel/operativo/pruebas/evidencia"

TODOS_SATISFECHOS = 0
HAY_INCUMPLIDOS = 1
NO_SE_PUDO_COMPROBAR = 2

TIEMPO_MAXIMO = 3600


class SedeIlegible(Exception):
    """No se puede leer una sede, o no se puede derivar de ella. Nunca es un verde."""


# ===========================================================================
#  1 · LA DERIVACIÓN · el catálogo sale de `O30` §2 y de ningún otro sitio
# ===========================================================================
# EL CARDINAL NO SE ESCRIBE. La regla reconoce las líneas de viñeta de `O30` §2 con la forma
# «- `Knn` · <formulación>» y las lee hasta la viñeta siguiente, de modo que una formulación
# de varias líneas —las hay— llega entera. Lo que sale de aquí ES el universo: si el Owner
# inscribe un `K25`, aparece solo; si alguien borra un `K`, la resta lo dice.
_VINETA = re.compile(r"^- `(K\d\d)` · (.*)$")
_CABECERA_DE_SECCION = re.compile(r"^#{1,3} ")


def _leer(rel, raiz=None):
    ruta = os.path.join(raiz or RAIZ, rel)
    try:
        with io.open(ruta, encoding="utf-8") as manejador:
            return manejador.read()
    except OSError as error:
        raise SedeIlegible("no se puede leer `%s`: %s" % (rel, error))


def derivar_catalogo(raiz=None):
    """`{Knn: formulación literal}` derivado de `O30` §2. Falla cerrado si no hay §2."""
    texto = _leer(SEDE_DEL_OWNER, raiz)
    lineas = texto.splitlines()
    inicio = None
    for numero, linea in enumerate(lineas):
        if linea.startswith("## 2. Catálogo cerrado de invariantes críticos"):
            inicio = numero + 1
            break
    if inicio is None:
        raise SedeIlegible(
            "`%s` no publica la sección «2. Catálogo cerrado de invariantes críticos» de "
            "`O30`: sin ella no hay universo que derivar, y este punto NO inventa uno"
            % SEDE_DEL_OWNER)
    catalogo, actual = {}, None
    for linea in lineas[inicio:]:
        if _CABECERA_DE_SECCION.match(linea):
            break
        encaje = _VINETA.match(linea)
        if encaje:
            actual = encaje.group(1)
            if actual in catalogo:
                raise SedeIlegible(
                    "`O30` §2 publica DOS veces el invariante `%s`: con dos textos bajo el "
                    "mismo nombre, cuál rige deja de ser una pregunta con respuesta" % actual)
            catalogo[actual] = encaje.group(2).strip()
        elif actual and linea.startswith("  ") and linea.strip():
            catalogo[actual] += " " + linea.strip()
        elif not linea.strip():
            actual = None
    if not catalogo:
        raise SedeIlegible(
            "`O30` §2 existe y no publica ni una viñeta con la forma «- `Knn` · …»: el "
            "universo saldría VACÍO, y un universo vacío se satisface solo")
    return catalogo


# ===========================================================================
#  2 · LA SEDE CANÓNICA · se lee, no se cree
# ===========================================================================
# FORMATO, y por qué no es YAML. El corpus se lee con la biblioteca estándar (`T202`) y aquí
# no entra ninguna dependencia por comodidad. Cada invariante vive en un bloque vallado
# ```ads:invariante con pares `clave: valor`; una clave sola abre una LISTA cuyas entradas
# van en líneas `  - …`; y una clave con valor admite continuación en líneas de cuatro
# espacios. Nada más. Un formato pequeño se puede comprobar entero, y éste se comprueba.
_APERTURA = "```ads:invariante"
_CIERRE = "```"

CLAVES_DE_LISTA = ("fuentes", "implementacion", "canal", "evidencia", "vinculo")
CLAVES_DE_TEXTO = ("id", "formulacion", "resultado", "estado", "limites")
CLAVES_DE_PRUEBAS = ("positivas", "adversariales")
CLAVES = CLAVES_DE_LISTA + CLAVES_DE_TEXTO + CLAVES_DE_PRUEBAS
OBLIGATORIAS = tuple(c for c in CLAVES if c != "vinculo")

ESTADOS = ("SATISFECHO", "NO SATISFECHO")


def leer_sede(raiz=None, sede=None):
    """`{Knn: ficha}` tal y como la sede lo escribe. No valida: LEE, y se queja si no puede."""
    texto = _leer(sede or SEDE_DEL_CATALOGO, raiz)
    fichas, bloque, dentro = {}, None, False
    for numero, linea in enumerate(texto.splitlines(), 1):
        if not dentro:
            if linea.strip() == _APERTURA:
                dentro, bloque = True, {"_linea": numero}
            continue
        if linea.strip() == _CIERRE:
            dentro = False
            identificador = (bloque.get("id") or "").strip()
            if not identificador:
                raise SedeIlegible(
                    "el bloque `ads:invariante` que abre en la línea %d no declara `id`: "
                    "una ficha sin identificador no se puede contrastar con nada"
                    % bloque["_linea"])
            if identificador in fichas:
                raise SedeIlegible(
                    "la sede publica DOS fichas para `%s`" % identificador)
            fichas[identificador] = bloque
            bloque = None
            continue
        if not linea.strip():
            continue
        if linea.startswith("  - "):
            clave = bloque.get("_ultima")
            if clave not in CLAVES_DE_LISTA:
                raise SedeIlegible(
                    "línea %d: una entrada de lista `  - …` fuera de una clave de lista "
                    "(%s)" % (numero, clave))
            bloque.setdefault(clave, []).append(linea[4:].strip())
            continue
        if linea.startswith("    ") and bloque.get("_ultima") in CLAVES_DE_TEXTO:
            bloque[bloque["_ultima"]] += " " + linea.strip()
            continue
        if ":" not in linea:
            raise SedeIlegible("línea %d: «%s» no es ni una clave ni una entrada de lista"
                               % (numero, linea.strip()[:60]))
        clave, _, valor = linea.partition(":")
        clave = clave.strip()
        if clave not in CLAVES:
            raise SedeIlegible("línea %d: clave desconocida `%s`. Las admitidas son: %s"
                               % (numero, clave, ", ".join(sorted(CLAVES))))
        bloque["_ultima"] = clave
        if clave in CLAVES_DE_LISTA:
            bloque.setdefault(clave, [])
            if valor.strip():
                raise SedeIlegible("línea %d: `%s` es una clave de LISTA y lleva valor en "
                                   "la misma línea" % (numero, clave))
        else:
            bloque[clave] = valor.strip()
    if dentro:
        raise SedeIlegible("un bloque `ads:invariante` se quedó SIN CERRAR")
    if not fichas:
        raise SedeIlegible(
            "la sede `%s` no publica ni un bloque `ads:invariante`: no hay nada que "
            "contrastar, y una sede vacía no satisface un catálogo" % (sede or SEDE_DEL_CATALOGO))
    return fichas


# ===========================================================================
#  3 · LA LIGADURA AL COMMIT Y AL TREE · `O30` §3.8
# ===========================================================================
# Este instrumento NO ESCRIBE en ningún repositorio: `rev-parse` no toca refs, índice ni
# objetos, y el identificador de blob del árbol de trabajo se CALCULA aquí con la fórmula
# pública de `git` en vez de pedírselo a `hash-object`, que con `-w` escribiría.

def _git(*args, raiz=None):
    try:
        proceso = subprocess.run(["git", "-C", raiz or RAIZ] + list(args),
                                 capture_output=True, text=True)
    except OSError as error:
        raise SedeIlegible("no se puede ejecutar `git`: %s" % error)
    return proceso.returncode, proceso.stdout.strip(), proceso.stderr.strip()


def _blob_de_los_bytes(datos):
    """El identificador que `git` daría a estos bytes: `sha1(\"blob <n>\\0\" + datos)`."""
    cabecera = ("blob %d\x00" % len(datos)).encode("utf-8")
    return hashlib.sha1(cabecera + datos).hexdigest()             # noqa: S324


class Ancla:
    """El commit y el tree contra los que se liga TODA la evidencia de esta corrida."""

    def __init__(self, raiz=None):
        self.raiz = raiz or RAIZ
        codigo, self.commit, error = _git("rev-parse", "HEAD", raiz=self.raiz)
        if codigo != 0:
            raise SedeIlegible(
                "el árbol que se juzga no está en un repositorio con `HEAD` legible, y sin "
                "`HEAD` la condición 8 de `O30` §3 —evidencia ligada al commit y al tree— "
                "no se puede comprobar. NO se aprueba por ausencia de dato: %s"
                % (error or codigo))
        codigo, self.tree, error = _git("rev-parse", "HEAD^{tree}", raiz=self.raiz)
        if codigo != 0:
            raise SedeIlegible("`HEAD` no resuelve a un tree: %s" % (error or codigo))
        self._blobs = {}

    def blob_en_head(self, rel):
        if rel not in self._blobs:
            codigo, salida, _ = _git("rev-parse", "HEAD:" + rel, raiz=self.raiz)
            self._blobs[rel] = salida if codigo == 0 else None
        return self._blobs[rel]

    def blob_en_disco(self, rel):
        ruta = os.path.join(self.raiz, rel)
        if not os.path.isfile(ruta):
            return None
        with io.open(ruta, "rb") as manejador:
            return _blob_de_los_bytes(manejador.read())


# ===========================================================================
#  4 · EL VEREDICTO DE UNA PRUEBA EN SU EVIDENCIA · el CASO SANO de `O30` §3.4
# ===========================================================================
# Las dos formas que el corpus publica, y ninguna más: la de `unittest` con `verbosity=2`
# —«Tnnn · <docstring> ... ok»— y la de los validadores documentales —«Tnnn  SUPERADA …»—.
# El veredicto es lo que va DESPUÉS del último « ... », y por eso «que `OK` valga por
# `OK (skipped=N)`» —que es texto de un docstring de `T307`— no se confunde con un salto.
_VERDICTO_UNITTEST = " ... "


def veredicto_en_evidencia(texto, prueba):
    """`(superada, saltada)` de una prueba dentro del texto de una evidencia publicada."""
    superada = saltada = False
    for linea in texto.splitlines():
        if not (linea.startswith(prueba + " ") or linea.startswith(prueba + "\t")):
            continue
        if _VERDICTO_UNITTEST in linea:
            cola = linea.rsplit(_VERDICTO_UNITTEST, 1)[1].strip()
            if cola.startswith("ok"):
                superada = True
            elif cola.startswith("skipped"):
                saltada = True
            continue
        if "SUPERADA" in linea:
            superada = True
        if "skipped" in linea:
            saltada = True
    return superada, saltada


# ===========================================================================
#  5 · EL CANAL DERIVADO · de los sabotajes, no de lo que la sede diga
# ===========================================================================
def canal_de_la_mutacion(mutacion):
    """La RUTA del ejecutable que ese sabotaje corre de verdad. Se deriva, no se escribe."""
    if getattr(mutacion, "clase", "") == "bateria":
        return mutacion.validador
    return VALIDADORES + "/" + mutacion.validador + ".py"


# Los sabotajes que este instrumento ejerce DIRECTAMENTE, porque el catálogo único no puede.
#
#   POR QUÉ EXISTE ESTA TABLA, Y POR QUÉ ES DE TRES ENTRADAS Y NO DE TREINTA.
#   `comprobar_negativos` sabe correr dos cosas: una batería `unittest` —de la que lee `Ran
#   N tests` y las cabeceras `FAIL:`— y un validador documental —del que lee una fila JSON—.
#   `T364` vive en `escenario_e2e_f6.py`, que no es ni una cosa ni la otra: publica su
#   veredicto por LÍNEAS. Registrar ahí un `Mutacion` de clase `bateria` publicaría «NO
#   LLEGÓ A CORRER» en cada pasada, que es un rojo falso, y de los peores: uno que se
#   acostumbra a ver. La mutación se escribe igual, en `negativos_runtime.py` y junto a las
#   demás, y se ejerce desde aquí contra el MECANISMO que `T364` mide —la orden
#   `procedencia` de cada punto ejecutable—, sano y saboteado, en el mismo ciclo.
DIRECTOS = {
    "NK12c": {
        "funcion": "m_o30_un_punto_pierde_la_orden_procedencia",
        "prueba": "T364",
        "canal": "kernel/operativo/runtime/ads_ciclo.py",
        "espera": "invalid choice: 'procedencia'",
        "descripcion": "un punto ejecutable pierde la orden que publica su procedencia",
    },
}


def _entorno_limpio():
    """El entorno del hijo, CONSTRUIDO y no heredado: nada de la familia `PYTHON*`."""
    limpio = {c: v for c, v in os.environ.items() if not c.startswith("PYTHON")}
    limpio["PYTHONDONTWRITEBYTECODE"] = "1"
    return limpio


def ejercer_directo(identificador, catalogo_de_negativos):
    """El ciclo SANO → SABOTAJE → RESTAURADO de un sabotaje que corre fuera del catálogo."""
    ficha = DIRECTOS[identificador]
    modulo = catalogo_de_negativos["negativos_runtime"]
    funcion = getattr(modulo, ficha["funcion"], None)
    if funcion is None:
        return (False, "el sabotaje directo `%s` declara la función `%s` y "
                       "`negativos_runtime.py` no la tiene: no hay nada que ejercer"
                % (identificador, ficha["funcion"]))
    copiar = catalogo_de_negativos["comprobar_negativos"].copiar_corpus
    base = tempfile.mkdtemp(prefix="ads-k-directo-")
    try:
        arbol = os.path.join(base, "arbol")
        copiar(arbol)
        punto = os.path.join(arbol, ficha["canal"])
        entorno = _entorno_limpio()
        sano = subprocess.run([sys.executable, punto, "procedencia", "--json"],
                              capture_output=True, text=True, env=entorno,
                              timeout=TIEMPO_MAXIMO)
        if sano.returncode != 0 or "aparato" not in (sano.stdout or ""):
            return (False, "el CONTROL SANO de `%s` no está verde antes de sabotear nada: "
                           "el ciclo no mediría el sabotaje sino un árbol ya roto (código "
                           "%s)" % (identificador, sano.returncode))
        funcion(arbol)
        roto = subprocess.run([sys.executable, punto, "procedencia", "--json"],
                              capture_output=True, text=True, env=entorno,
                              timeout=TIEMPO_MAXIMO)
        salida = (roto.stdout or "") + (roto.stderr or "")
        if roto.returncode == 0 and "aparato" in (roto.stdout or ""):
            return (False, "`%s` NO detectó nada: el punto sigue publicando su procedencia "
                           "con la orden retirada" % identificador)
        if ficha["espera"] not in salida:
            return (False, "`%s` cayó, y NO por el motivo esperado. Se buscaba «%s» y se "
                           "obtuvo: %s" % (identificador, ficha["espera"], salida[-160:]))
        return (True, "sano VERDE · saboteado ROJO por «%s»" % ficha["espera"])
    except subprocess.TimeoutExpired:
        return (False, "el ciclo de `%s` no terminó en %d s" % (identificador, TIEMPO_MAXIMO))
    except Exception as error:                                       # noqa: BLE001
        return (False, "no se pudo ejercer `%s`: %s" % (identificador, error))
    finally:
        import shutil
        shutil.rmtree(base, ignore_errors=True)


def importar_negativos(raiz=None):
    """El catálogo ÚNICO de mutaciones, IMPORTADO. No se copia, y no se resume.

    Se importa desde el árbol que se juzga y con `sys.path` restaurado después: un catálogo
    transcrito aquí caducaría el día que alguien añadiera un sabotaje, y un instrumento que
    mide con una copia vieja publica un verde de otro árbol.
    """
    sede = os.path.join(raiz or RAIZ, VALIDADORES)
    if not os.path.isfile(os.path.join(sede, "comprobar_negativos.py")):
        raise SedeIlegible(
            "no hay `%s/comprobar_negativos.py` en el árbol que se juzga: sin el catálogo "
            "único de mutaciones no se puede decir de ningún invariante que tenga prueba "
            "adversarial" % VALIDADORES)
    anterior = list(sys.path)
    sys.path.insert(0, sede)
    try:
        import comprobar_negativos                                   # noqa: E402
        import negativos_runtime                                     # noqa: E402
    except Exception as error:                                       # noqa: BLE001
        raise SedeIlegible("el catálogo de mutaciones no se puede importar: %s" % error)
    finally:
        sys.path[:] = anterior
    return {"comprobar_negativos": comprobar_negativos,
            "negativos_runtime": negativos_runtime,
            "por_id": {m.id: m for m in comprobar_negativos.CATALOGO}}


def ejercer_mutacion(identificador, raiz=None):
    """Corre UN sabotaje del catálogo único por su canal oficial y devuelve `(ok, detalle)`."""
    guion = os.path.join(raiz or RAIZ, NEGATIVOS)
    try:
        proceso = subprocess.run(
            [sys.executable, guion, "--caso", identificador, "--json"],
            capture_output=True, text=True, cwd=(raiz or RAIZ), env=_entorno_limpio(),
            timeout=TIEMPO_MAXIMO)
    except subprocess.TimeoutExpired:
        return (False, "el sabotaje `%s` no terminó en %d s" % (identificador, TIEMPO_MAXIMO))
    except OSError as error:
        return (False, "no se pudo ejecutar `comprobar_negativos.py`: %s" % error)
    try:
        filas = json.loads(proceso.stdout)
    except ValueError:
        return (False, "`comprobar_negativos.py --caso %s` no devolvió JSON (código %s): %s"
                % (identificador, proceso.returncode, (proceso.stderr or "")[:200]))
    fila = next((f for f in filas if f.get("id") == identificador), None)
    if fila is None:
        return (False, "el catálogo no contiene el sabotaje `%s`" % identificador)
    if fila.get("resultado") != "detectada":
        return (False, "%s: %s — %s" % (identificador, fila.get("resultado"),
                                        fila.get("detalle")))
    return (True, fila.get("detalle") or "")


# ===========================================================================
#  6 · EL JUICIO · las trece condiciones, una a una y sobre cada invariante
# ===========================================================================
class Juicio:
    """Lo comprobado sobre UN invariante. `fallos` vacío significa satisfecho."""

    def __init__(self, identificador):
        self.id = identificador
        self.fallos = []
        self.notas = []
        self.ejercidos = []

    def falla(self, condicion, causa):
        self.fallos.append({"condicion": condicion, "causa": causa})

    @property
    def satisfecho(self):
        return not self.fallos


def _compartidas(fichas):
    """`{prueba o sabotaje: [invariantes que lo declaran]}`, para los que van en más de uno."""
    reparto = {}
    for identificador, ficha in fichas.items():
        for prueba in (ficha.get("positivas") or "").split():
            reparto.setdefault(prueba, set()).add(identificador)
        for sabotaje in (ficha.get("adversariales") or "").split():
            reparto.setdefault(sabotaje, set()).add(identificador)
    return {c: sorted(v) for c, v in reparto.items() if len(v) > 1}


def juzgar(fichas, catalogo, negativos, ancla, *, ejercer=True, solo=None, raiz=None):
    """Devuelve `[Juicio]`, uno por invariante DERIVADO, más los que sobran en la sede."""
    juicios = []
    compartidas = _compartidas(fichas)
    corridas = {}

    # `C-01` y `C-02` · la resta, en los dos sentidos. Ninguna de las dos se escribe.
    faltan = sorted(set(catalogo) - set(fichas))
    sobran = sorted(set(fichas) - set(catalogo))
    for identificador in faltan:
        juicio = Juicio(identificador)
        juicio.falla("C-01", "`O30` §2 lo inscribe y la sede canónica NO lo publica: «"
                             + catalogo[identificador] + "»")
        juicios.append(juicio)
    for identificador in sobran:
        juicio = Juicio(identificador)
        juicio.falla("C-02", "la sede publica un invariante que `O30` §2 NO autoriza. El "
                             "catálogo es CERRADO para este ciclo, y `O30` §2 sólo admite "
                             "un `K25` que demuestre un efecto material distinto")
        juicios.append(juicio)

    for identificador in sorted(set(catalogo) & set(fichas)):
        if solo and identificador != solo:
            continue
        ficha = fichas[identificador]
        juicio = Juicio(identificador)
        juicios.append(juicio)

        # --- lo que tiene que estar escrito, antes de mirar si es cierto ----------------
        for clave in OBLIGATORIAS:
            valor = ficha.get(clave)
            if not valor or (isinstance(valor, str) and not valor.strip()):
                condicion = {"fuentes": "C-04", "implementacion": "C-05", "canal": "C-06",
                             "positivas": "C-07", "adversariales": "C-08",
                             "evidencia": "C-09"}.get(clave, "C-03")
                juicio.falla(condicion, "la ficha no declara `%s`" % clave)
        if ficha.get("estado") not in ESTADOS:
            juicio.falla("C-03", "`estado` vale «%s» y el vocabulario cerrado es %s"
                         % (ficha.get("estado"), " / ".join(ESTADOS)))
        if juicio.fallos:
            continue

        # `C-03` · la formulación es la LITERAL de `O30` §2, normalizando sólo el blanco.
        derivada = " ".join(catalogo[identificador].split())
        publicada = " ".join(ficha["formulacion"].split())
        if derivada != publicada:
            juicio.falla("C-03",
                         "la formulación publicada NO es la de `O30` §2.\n"
                         "        `O30` §2: " + derivada + "\n"
                         "        la sede : " + publicada)

        # `C-04` · fuente normativa: la ruta existe y el ancla APARECE en ella.
        for fuente in ficha["fuentes"]:
            ruta, _, ancla_texto = fuente.partition(" :: ")
            ruta, ancla_texto = ruta.strip(), ancla_texto.strip()
            if not ruta or not ancla_texto:
                juicio.falla("C-04", "la fuente «%s» no tiene la forma `ruta :: ancla`"
                             % fuente[:70])
                continue
            if not os.path.isfile(os.path.join(raiz or RAIZ, ruta)):
                juicio.falla("C-04", "la fuente `%s` no está en el árbol" % ruta)
                continue
            try:
                cuerpo = _leer(ruta, raiz)
            except SedeIlegible as error:
                juicio.falla("C-04", str(error))
                continue
            if ancla_texto not in cuerpo:
                juicio.falla("C-04", "la fuente `%s` NO dice «%s»: se cita una norma que "
                                     "esa sede no publica" % (ruta, ancla_texto[:60]))

        # `C-05` · el mecanismo implementado está en el árbol.
        for ruta in ficha["implementacion"]:
            if not os.path.exists(os.path.join(raiz or RAIZ, ruta.strip())):
                juicio.falla("C-05", "la ruta de implementación `%s` NO está en el árbol: "
                                     "un invariante cuyo mecanismo no existe no está "
                                     "implementado, esté donde esté escrito" % ruta.strip())

        positivas = ficha["positivas"].split()
        adversariales = ficha["adversariales"].split()

        # `C-08` · cada sabotaje EXISTE y NOMBRA una prueba que este invariante declara.
        #          Es la segunda condición de `O30` §3 para la prueba compartida —el vínculo
        #          prueba→invariante declarado sin ambigüedad— convertida en comprobación.
        canales_derivados = set()
        for sabotaje in adversariales:
            if sabotaje in DIRECTOS:
                ficha_directa = DIRECTOS[sabotaje]
                canales_derivados.add(ficha_directa["canal"])
                if ficha_directa["prueba"] not in positivas:
                    juicio.falla("C-08", "el sabotaje directo `%s` ejerce `%s`, que este "
                                         "invariante NO declara como prueba positiva"
                                 % (sabotaje, ficha_directa["prueba"]))
                continue
            mutacion = negativos["por_id"].get(sabotaje)
            if mutacion is None:
                juicio.falla("C-08", "el sabotaje `%s` NO está en el catálogo único de "
                                     "mutaciones: se cita una prueba adversarial que no "
                                     "existe" % sabotaje)
                continue
            canales_derivados.add(canal_de_la_mutacion(mutacion))
            if mutacion.prueba not in positivas:
                juicio.falla("C-08", "el sabotaje `%s` pone roja a `%s`, que este "
                                     "invariante NO declara como prueba positiva: el "
                                     "vínculo prueba→invariante no es inequívoco"
                             % (sabotaje, mutacion.prueba))

        # `C-06` · el canal DECLARADO es exactamente el que sus sabotajes ejercen.
        declarados = {c.strip() for c in ficha["canal"]}
        for canal in sorted(declarados):
            if not os.path.isfile(os.path.join(raiz or RAIZ, canal)):
                juicio.falla("C-06", "el canal productivo `%s` no está en el árbol" % canal)
        if canales_derivados and declarados != canales_derivados:
            juicio.falla("C-06",
                         "el canal declarado NO es el que ejercen sus sabotajes.\n"
                         "        declarado: " + (", ".join(sorted(declarados)) or "∅") + "\n"
                         "        derivado : " + (", ".join(sorted(canales_derivados)) or "∅"))

        # `C-07`, `C-09` y `C-13` · el CASO SANO, la evidencia y los saltos, a la vez.
        textos = {}
        for relativa in ficha["evidencia"]:
            relativa = relativa.strip()
            en_disco = ancla.blob_en_disco(relativa)
            if en_disco is None:
                juicio.falla("C-09", "la evidencia `%s` NO está en el árbol" % relativa)
                continue
            en_head = ancla.blob_en_head(relativa)
            if en_head is None:
                juicio.falla("C-09", "`HEAD` no tiene confirmada la evidencia `%s` (blob "
                                     "del árbol de trabajo %s): no está ligada al commit "
                                     "ni al tree que se juzgan" % (relativa, en_disco[:12]))
                continue
            if en_head != en_disco:
                juicio.falla("C-12", "la evidencia `%s` del árbol de trabajo (%s) DIFIERE "
                                     "del blob de `HEAD` (%s): el commit y el tree no "
                                     "corresponden al objeto juzgado"
                             % (relativa, en_disco[:12], en_head[:12]))
                continue
            textos[relativa] = _leer(relativa, raiz)
        for prueba in positivas:
            superada = saltada = False
            for relativa, cuerpo in textos.items():
                una, otra = veredicto_en_evidencia(cuerpo, prueba)
                superada = superada or una
                saltada = saltada or otra
            if saltada:
                juicio.falla("C-13", "la prueba positiva `%s` figura SALTADA en la "
                                     "evidencia publicada: una prueba que se salta no es un "
                                     "caso sano" % prueba)
            elif not superada:
                juicio.falla("C-07", "ninguna de las evidencias declaradas da por SUPERADA "
                                     "la prueba positiva `%s`" % prueba)

        # `C-10` · la prueba compartida explica su vínculo CON ESTE invariante.
        vinculos = {}
        for linea in ficha.get("vinculo") or []:
            clave, _, explicacion = linea.partition(" :: ")
            vinculos[clave.strip()] = explicacion.strip()
        for compartida in sorted(set(positivas + adversariales)):
            if compartida not in compartidas:
                continue
            otros = [k for k in compartidas[compartida] if k != identificador]
            if not vinculos.get(compartida):
                juicio.falla("C-10",
                             "`%s` está compartida con %s y esta ficha NO explica qué "
                             "observación DISTINTA demuestra aquí. `O30` §3 lo admite sólo "
                             "con el vínculo declarado" % (compartida, ", ".join(otros)))
        for clave in vinculos:
            if clave not in compartidas:
                juicio.notas.append("`vinculo` declara `%s`, que no está compartida con "
                                    "ningún otro invariante: sobra, y no acredita nada"
                                    % clave)

        # `C-11` y `C-13` · SE EJERCE. Sin esto la ficha es una promesa.
        if not ejercer:
            juicio.falla("C-13", "los sabotajes NO se han ejercido en esta corrida "
                                 "(`--sin-ejercer`): ningún ejecutable requerido llegó a "
                                 "correr, y este invariante queda SIN ACREDITAR")
        else:
            for sabotaje in adversariales:
                if sabotaje in corridas:
                    ok, detalle = corridas[sabotaje]
                    # Un sabotaje COMPARTIDO se corre UNA vez y se cuenta en los dos: correr
                    # dos veces la misma copia del corpus no añade una observación, añade
                    # una hora. Lo que distingue a los dos invariantes es el `vinculo:`,
                    # que `C-10` exige, no una repetición del mismo ciclo.
                elif sabotaje in DIRECTOS:
                    ok, detalle = ejercer_directo(sabotaje, negativos)
                    corridas[sabotaje] = (ok, detalle)
                else:
                    # El progreso va a `stderr` y NUNCA a `stdout`: la salida publicable
                    # tiene que ser byte-idéntica entre corridas, y una barra de progreso
                    # no lo es. Sin ella, una corrida de horas es indistinguible de una
                    # colgada, y eso acaba en que alguien la mata y publica lo que tenía.
                    sys.stderr.write("  · %s ejerciendo %s\n" % (identificador, sabotaje))
                    sys.stderr.flush()
                    ok, detalle = ejercer_mutacion(sabotaje, raiz)
                    corridas[sabotaje] = (ok, detalle)
                juicio.ejercidos.append({"sabotaje": sabotaje, "ok": ok, "detalle": detalle})
                if not ok:
                    juicio.falla("C-11", "el sabotaje `%s` NO produjo el resultado "
                                         "esperado: %s" % (sabotaje, detalle))
            if not juicio.ejercidos:
                juicio.falla("C-13", "no llegó a ejercerse ni un sabotaje")

        # El estado DECLARADO no puede ir por delante de lo comprobado. Sólo se contrasta
        # cuando la corrida EJERCE: con `--sin-ejercer` el único fallo posible es el `C-13`
        # que la propia bandera provoca, y encadenarle un `C-03` diría que la ficha miente
        # cuando lo que pasa es que no se ha medido.
        if ejercer and ficha["estado"] == "SATISFECHO" and juicio.fallos:
            juicio.falla("C-03", "la ficha se declara SATISFECHO y arriba hay %d "
                                 "incumplimientos: un estado escrito no supera una medida"
                         % len(juicio.fallos))
        if ejercer and ficha["estado"] == "NO SATISFECHO" and not juicio.fallos:
            juicio.notas.append("la ficha se declara NO SATISFECHO y todo lo comprobable "
                                "ha salido verde: su motivo tiene que estar en `limites`")
    return juicios


# ===========================================================================
#  7 · LA PUBLICACIÓN · el cardinal se DERIVA de la lista, y no al revés
# ===========================================================================
def publicar(destino, juicios, catalogo, ancla, ejercido, fichas=None,
             negativos=None):
    destino.write("`O30` §2 · CATÁLOGO CERRADO DE INVARIANTES CRÍTICOS, DERIVADO Y EJERCIDO\n")
    destino.write("=" * 78 + "\n\n")
    destino.write("  UNIVERSO derivado de `%s`, sección «2. Catálogo cerrado de "
                  "invariantes críticos»\n" % SEDE_DEL_OWNER)
    destino.write("  SEDE canónica del catálogo: `%s`\n" % SEDE_DEL_CATALOGO)
    destino.write("  ANCLA   commit %s · tree %s\n" % (ancla.commit, ancla.tree))
    destino.write("  CICLO   %s\n\n" % (
        "sano (evidencia ligada a HEAD) → SABOTAJE ejecutado → restaurado (el árbol juzgado "
        "no se toca: la mutación vive en una copia)" if ejercido
        else "NO EJERCIDO en esta corrida: ningún sabotaje llegó a correr"))

    destino.write("EL UNIVERSO, DERIVADO Y LITERAL\n")
    destino.write("-" * 78 + "\n")
    for identificador in sorted(catalogo):
        destino.write("  %s · %s\n" % (identificador, catalogo[identificador]))
    destino.write("\n")

    incumplidos = [j for j in juicios if not j.satisfecho]
    destino.write("LOS INCUMPLIMIENTOS, UNO A UNO\n")
    destino.write("-" * 78 + "\n")
    if not incumplidos:
        destino.write("  ninguno\n")
    for juicio in incumplidos:
        destino.write("  %s\n" % juicio.id)
        for fallo in juicio.fallos:
            destino.write("      [%s] %s\n" % (fallo["condicion"], fallo["causa"]))
    destino.write("\n")

    destino.write("LO EJERCIDO, SABOTAJE A SABOTAJE\n")
    destino.write("-" * 78 + "\n")
    corridas = {}
    for juicio in juicios:
        for hecho in juicio.ejercidos:
            corridas.setdefault(hecho["sabotaje"], hecho)
    if not corridas:
        destino.write("  ninguno\n")
    for identificador in sorted(corridas):
        hecho = corridas[identificador]
        destino.write("  %-8s %-14s %s\n" % (
            identificador, "DETECTADO" if hecho["ok"] else "NO DETECTADO",
            (hecho["detalle"] or "")[:110]))
    destino.write("\n")

    notas = [(j.id, n) for j in juicios for n in j.notas]
    if notas:
        destino.write("OBSERVACIONES\n")
        destino.write("-" * 78 + "\n")
        for identificador, nota in notas:
            destino.write("  %s · %s\n" % (identificador, nota))
        destino.write("\n")

    destino.write("LO QUE ESTE VEREDICTO NO DEMUESTRA\n")
    destino.write("-" * 78 + "\n")
    destino.write(
        "  · no demuestra que un invariante sea INDERROTABLE: demuestra que el sabotaje\n"
        "    declarado lo alcanza y que su canal cae por el motivo declarado;\n"
        "  · no juzga si la adscripción de una propiedad a su `Knn` es la correcta: juzga\n"
        "    que el vínculo esté declarado y que la ejecución lo confirme;\n"
        "  · no mide las obligaciones funcionales no críticas de `O30` §4, ni las ocho\n"
        "    condiciones de `O26` §1, ni `M-04`, ni `C-L.7`;\n"
        "  · no certifica `F6`: `O30` §7 reserva eso a un verificador independiente.\n\n")

    # `M2` DEL VERIFICADOR INDEPENDIENTE DE `O30` · LA COBERTURA ADVERSARIAL, CNS CARDINAL.
    #
    #     El auditor dejó `K13` con 1 de sus 5 sabotajes y la corrida salió VERDE, porque la
    #     firma de éxito era `[1-9]\d* sabotajes` —sin cardinal— y nada contrastaba lo
    #     EJERCIDO contra lo que el catálogo de mutaciones tiene para las pruebas de cada
    #     ficha. El corpus podía bajar de 57 a 24 sin que nada lo dijera.
    #
    #     Lo que se hace, y lo que NO. Se DERIVAN dos cardinales —los declarados por las
    #     fichas y los que el catálogo único tiene para sus pruebas positivas— y se publican
    #     junto a los no seleccionados, con nombre y por ficha. Una caída de cobertura deja
    #     de ser invisible: aparece como un número que baja y una lista que crece.
    #     NO se convierte en fallo que un invariante seleccione un subconjunto: decidir si
    #     una ficha DEBE ejercer todo mutante catalogado de sus pruebas es una decisión
    #     normativa que `O30` no contiene, y este instrumento no las inventa (§16). Queda
    #     publicada la frontera para que la decida quien puede.
    no_seleccionados = {}
    declarados = set()
    catalogados = set()
    ocurrencias = 0
    if fichas and negativos:
        por_prueba = {}
        for mut in negativos["por_id"].values():
            por_prueba.setdefault(mut.prueba, set()).add(mut.id)
        for kid, ficha in sorted(fichas.items()):
            adv = set((ficha.get("adversariales") or "").split())
            declarados |= adv
            ocurrencias += len(adv)
            suyos = set()
            for prueba in (ficha.get("positivas") or "").split():
                suyos |= por_prueba.get(prueba, set())
            catalogados |= suyos
            if suyos - adv:
                no_seleccionados[kid] = sorted(suyos - adv)
        destino.write("COBERTURA ADVERSARIAL · LO DECLARADO Y LO QUE EL CATÁLOGO TIENE\n")
        destino.write("-" * 78 + "\n")
        # DISTINTOS Y OCURRENCIAS SE PUBLICAN POR SEPARADO. Un sabotaje declarado por DOS
        # invariantes se ejerce UNA vez —`C-10` exige que cada uno explique su vínculo—,
        # de modo que «declarados» contado por ocurrencias sale mayor que «ejercidos» sin
        # que falte ninguno. Se dan los dos números para que la resta no engañe.
        destino.write("  sabotajes DISTINTOS declarados .. %d\n" % len(declarados))
        destino.write("  ocurrencias en las fichas ....... %d  (los compartidos, una por "
                      "invariante que los declara)\n" % ocurrencias)
        destino.write("  ejercidos en esta corrida ....... %d\n" % len(corridas))
        destino.write("  sin ejercer ..................... %s\n"
                      % (" ".join(sorted(declarados - set(corridas))) or "ninguno"))
        destino.write("  catalogados sobre sus positivas . %d distintos\n" % len(catalogados))
        if no_seleccionados:
            for kid, sueltos in sorted(no_seleccionados.items()):
                destino.write("  %-5s NO seleccionados: %s\n" % (kid, " ".join(sueltos)))
        else:
            destino.write("  ninguna ficha deja fuera un mutante catalogado de sus pruebas\n")
        destino.write("\n")

    destino.write("%d invariantes medidos · %d SATISFECHOS · %d INCUMPLIDOS · "
                  "%d sabotajes declarados · %d ejercidos · %d catalogados · "
                  "%d no seleccionados · %d sin detectar\n"
                  % (len(juicios), len(juicios) - len(incumplidos), len(incumplidos),
                     len(declarados), len(corridas), len(catalogados),
                     len(catalogados - declarados),
                     len([h for h in corridas.values() if not h["ok"]])))
    return HAY_INCUMPLIDOS if incumplidos else TODOS_SATISFECHOS


# ===========================================================================
#  8 · LAS AUTOPRUEBAS · trece modos de fallo, saboteados sobre el propio juez
# ===========================================================================
#  POR QUÉ EXISTEN, Y POR QUÉ NO BASTA CNS QUE EL PRODUCTO SALGA VERDE. La lección `G-05`
#  del manifiesto de validadores: un instrumento cuyo autotest pasa y cuyo producto no corre
#  está roto y sale verde. Aquí se ejerce la mitad contraria: se comprueba que el juez SABE
#  DECIR QUE NO. Cada control monta una sede sintética con UN defecto y exige que el juez
#  publique la condición que le toca —no «alguna»: LA suya—.

_FICHA_MODELO = """```ads:invariante
id: %(id)s
formulacion: %(formulacion)s
fuentes:
  - %(fuente)s
implementacion:
  - %(implementacion)s
canal:
  - %(canal)s
positivas: %(positivas)s
adversariales: %(adversariales)s
resultado: el canal cae por el motivo declarado
evidencia:
  - %(evidencia)s
estado: SATISFECHO
limites: ninguno declarado por este control
```
"""


class _AnclaFingida(Ancla):
    """Un ancla real a la que se le CAMBIA una respuesta, para ejercer `C-12` de verdad."""

    def __init__(self, ruta_torcida, raiz=None):
        Ancla.__init__(self, raiz=raiz)
        self._torcida = ruta_torcida

    def blob_en_head(self, rel):
        if rel == self._torcida:
            return "0" * 40
        return Ancla.blob_en_head(self, rel)


def autopruebas(destino):
    """Los trece modos de fallo cerrado, cada uno con su control. Devuelve el código."""
    catalogo = derivar_catalogo()
    negativos = importar_negativos()
    ancla = Ancla()
    fichas_reales = leer_sede()

    # El control POSITIVO va PRIMERO: un juez que no puede aprobar no mide nada. Se toma la
    # ficha real de un invariante y se exige que, sin ejercer, no tenga ningún fallo
    # estructural. Si esto sale rojo, todo lo que siga es ruido.
    modelo = None
    for identificador in sorted(set(catalogo) & set(fichas_reales)):
        juicios = juzgar(fichas_reales, catalogo, negativos, ancla,
                         ejercer=False, solo=identificador)
        propio = [j for j in juicios if j.id == identificador][0]
        estructurales = [f for f in propio.fallos if f["condicion"] != "C-13"]
        if not estructurales:
            modelo = identificador
            break

    controles = []

    def control(nombre, condicion, fichas, *, ancla_usada=None, solo=None, ejercer=False):
        juicios = juzgar(fichas, catalogo, negativos, ancla_usada or ancla,
                         ejercer=ejercer, solo=solo)
        condiciones = {f["condicion"] for j in juicios for f in j.fallos}
        controles.append({"control": nombre, "espera": condicion,
                          "detectado": condicion in condiciones,
                          "obtenidas": sorted(condiciones)})

    controles.append({"control": "control POSITIVO · una ficha real pasa la estructura",
                      "espera": "sin fallos", "detectado": modelo is not None,
                      "obtenidas": [] if modelo else ["ninguna ficha real pasa"]})
    if modelo is None:
        destino.write("el CONTROL POSITIVO ha caído: ninguna ficha de la sede pasa la "
                      "comprobación estructural, y sin él los controles negativos no "
                      "significan nada\n")
        _publicar_controles(destino, controles)
        return HAY_INCUMPLIDOS

    def copia(cambios=None, quitar=None):
        nuevas = {k: dict(v) for k, v in fichas_reales.items()}
        for clave in quitar or []:
            nuevas.pop(clave, None)
        for clave, valores in (cambios or {}).items():
            nuevas.setdefault(clave, dict(fichas_reales[modelo]))
            nuevas[clave].update(valores)
            nuevas[clave]["id"] = clave
        return nuevas

    control("falta un `K` del catálogo derivado", "C-01", copia(quitar=[modelo]))
    control("sobra un `K` que `O30` §2 no autoriza", "C-02",
            copia(cambios={"K99": {"formulacion": "un invariante que nadie inscribió"}}))
    control("la formulación no es la LITERAL de `O30` §2", "C-03",
            copia(cambios={modelo: {"formulacion": "una paráfrasis que suena parecida"}}),
            solo=modelo)
    control("un `K` sin fuente normativa", "C-04",
            copia(cambios={modelo: {"fuentes": []}}), solo=modelo)
    control("una fuente que NO dice lo que se le cita", "C-04",
            copia(cambios={modelo: {"fuentes": [SEDE_DEL_OWNER + " :: ZZ-ANCLA-QUE-NADIE-ESCRIBIO"]}}),
            solo=modelo)
    control("un `K` sin implementación", "C-05",
            copia(cambios={modelo: {"implementacion": []}}), solo=modelo)
    control("una implementación que no está en el árbol", "C-05",
            copia(cambios={modelo: {"implementacion": ["kernel/zz-no-existe.py"]}}),
            solo=modelo)
    control("un `K` sin canal productivo", "C-06",
            copia(cambios={modelo: {"canal": []}}), solo=modelo)
    control("un canal que NO es el que ejercen sus sabotajes", "C-06",
            copia(cambios={modelo: {"canal": [NEGATIVOS]}}), solo=modelo)
    control("un `K` sin prueba positiva", "C-07",
            copia(cambios={modelo: {"positivas": ""}}), solo=modelo)
    control("una positiva que su evidencia NO da por superada", "C-07",
            copia(cambios={modelo: {"positivas": fichas_reales[modelo]["positivas"] + " T9999",
                                    "adversariales": fichas_reales[modelo]["adversariales"]}}),
            solo=modelo)
    control("un `K` sin prueba adversarial", "C-08",
            copia(cambios={modelo: {"adversariales": ""}}), solo=modelo)
    control("un sabotaje que no está en el catálogo único", "C-08",
            copia(cambios={modelo: {"adversariales": "NZZ-INEXISTENTE"}}), solo=modelo)
    control("un `K` sin evidencia", "C-09",
            copia(cambios={modelo: {"evidencia": []}}), solo=modelo)
    control("una evidencia que no está en el árbol", "C-09",
            copia(cambios={modelo: {"evidencia": [EVIDENCIA + "/zz-no-existe.txt"]}}),
            solo=modelo)

    # `C-10` · la prueba COMPARTIDA sin vínculo. Se fabrica el reparto: un invariante nuevo
    # declara la MISMA positiva y el MISMO sabotaje que el modelo, y ninguno de los dos
    # explica qué observación distinta demuestra.
    gemelo = dict(fichas_reales[modelo])
    gemelo.pop("vinculo", None)
    sin_vinculo = copia()
    sin_vinculo[modelo] = dict(fichas_reales[modelo])
    sin_vinculo[modelo].pop("vinculo", None)
    for otro in sorted(set(catalogo) & set(fichas_reales)):
        if otro == modelo:
            continue
        sin_vinculo[otro] = dict(gemelo)
        sin_vinculo[otro]["id"] = otro
        sin_vinculo[otro]["formulacion"] = catalogo[otro]
        break
    control("una prueba compartida que no explica su vínculo", "C-10", sin_vinculo,
            solo=modelo)

    # `C-11` · el resultado observado no coincide con el esperado. Se ejerce DE VERDAD: se
    # declara un sabotaje directo cuya función no existe en `negativos_runtime.py`, y el
    # ciclo tiene que volver diciendo que no pudo poner nada rojo.
    DIRECTOS["NZZ-CONTROL"] = {"funcion": "zz_funcion_que_no_existe", "prueba": "T364",
                               "canal": "kernel/operativo/runtime/ads_ciclo.py",
                               "espera": "nada", "descripcion": "control de `C-11`"}
    try:
        control("el resultado observado NO coincide con el esperado", "C-11",
                copia(cambios={modelo: {"adversariales": "NZZ-CONTROL",
                                        "positivas": "T364",
                                        "canal": ["kernel/operativo/runtime/ads_ciclo.py"],
                                        "evidencia": [EVIDENCIA + "/e2e-f6-salida.txt"]}}),
                solo=modelo, ejercer=True)
    finally:
        DIRECTOS.pop("NZZ-CONTROL", None)

    # `C-12` · el commit o el tree no corresponden al objeto juzgado. Se tuerce UNA respuesta
    # del ancla —la de una evidencia real— y se exige que el juez lo vea. Y aparte: sin
    # repositorio, el ancla NO se construye y no hay veredicto que dar.
    primera = (fichas_reales[modelo]["evidencia"] or [""])[0].strip()
    control("el blob de la evidencia no es el de `HEAD`", "C-12", copia(), solo=modelo,
            ancla_usada=_AnclaFingida(primera))
    sin_repositorio = tempfile.mkdtemp(prefix="ads-k-sin-git-")
    try:
        Ancla(raiz=sin_repositorio)
        controles.append({"control": "sin repositorio, el ancla NO se construye",
                          "espera": "SedeIlegible", "detectado": False,
                          "obtenidas": ["se construyó un ancla sin `HEAD`"]})
    except SedeIlegible:
        controles.append({"control": "sin repositorio, el ancla NO se construye",
                          "espera": "SedeIlegible", "detectado": True, "obtenidas": []})
    finally:
        import shutil
        shutil.rmtree(sin_repositorio, ignore_errors=True)

    # `C-13` · una prueba que se SALTA, y un ejecutable requerido que no llega a ejercerse.
    #
    #   POR QUÉ EL PRIMERO NO PASA POR `juzgar`, y se dice. Con `--sin-ejercer` toda ficha
    #   arrastra ya un `C-13` —el de «no se ejerció»—, de modo que un control que montara
    #   una sede con una positiva saltada saldría verde SIN HABER MEDIDO NADA: el `C-13`
    #   que viera sería el otro. Se ejerce entonces el detector directamente, con las dos
    #   mitades que lo hacen significar: una línea REALMENTE saltada tiene que verse, y la
    #   línea real de `T307` —cuyo docstring contiene la palabra `skipped` dentro del texto—
    #   NO puede confundirse con un salto. Sin la segunda mitad, un detector que buscara la
    #   subcadena pasaría este control y pondría roja la sede entera.
    saltada_de_verdad = veredicto_en_evidencia(
        "T999 · una prueba que el anfitrión no puede correr ... skipped 'sin backend'", "T999")
    controles.append({"control": "una positiva SALTADA se ve como salto, no como éxito",
                      "espera": "C-13", "detectado": saltada_de_verdad == (False, True),
                      "obtenidas": ["superada=%s saltada=%s" % saltada_de_verdad]})
    falso_salto = veredicto_en_evidencia(
        "T307 · Defecto que previene: `E-14`, que `OK` valga por `OK (skipped=N)`. ... ok",
        "T307")
    controles.append({"control": "la palabra `skipped` DENTRO del enunciado no es un salto",
                      "espera": "C-13", "detectado": falso_salto == (True, False),
                      "obtenidas": ["superada=%s saltada=%s" % falso_salto]})
    control("ningún ejecutable requerido llega a ejercerse", "C-13", copia(), solo=modelo)

    return _publicar_controles(destino, controles)


def _publicar_controles(destino, controles):
    destino.write("AUTOPRUEBAS · los modos de fallo cerrado, saboteados sobre el propio juez\n")
    destino.write("=" * 78 + "\n\n")
    for fila in controles:
        marca = "OK   " if fila["detectado"] else "FALLO"
        destino.write("%s %-6s %s\n" % (marca, fila["espera"], fila["control"]))
        if not fila["detectado"]:
            destino.write("            obtenidas: %s\n"
                          % (", ".join(fila["obtenidas"]) or "ninguna"))
    sin_detectar = [f for f in controles if not f["detectado"]]
    destino.write("\n%d controles · %d sin detectar\n"
                  % (len(controles), len(sin_detectar)))
    return HAY_INCUMPLIDOS if sin_detectar else TODOS_SATISFECHOS


# ===========================================================================
#  9 · main
# ===========================================================================
def main(argv=None):
    analizador = argparse.ArgumentParser(
        description="`O30` §2 · el catálogo `K01`–`K24`, derivado de la sede del Owner y "
                    "ejercido sobre el árbol")
    analizador.add_argument("--raiz", default=None,
                            help="árbol a juzgar (por defecto, el del propio aparato)")
    analizador.add_argument("--sede", default=None,
                            help="sede canónica del catálogo (por defecto, la de `O30` §8)")
    analizador.add_argument("--solo", default=None, metavar="Knn",
                            help="medir un solo invariante")
    analizador.add_argument("--sin-ejercer", action="store_true",
                            help="no ejecutar los sabotajes; NO acredita, y se dice")
    analizador.add_argument("--autopruebas", action="store_true",
                            help="ejercer los modos de fallo cerrado sobre el propio juez")
    analizador.add_argument("--json", action="store_true")
    argumentos = analizador.parse_args(argv)

    raiz = os.path.abspath(argumentos.raiz) if argumentos.raiz else RAIZ

    try:
        if argumentos.autopruebas:
            return autopruebas(sys.stdout)
        catalogo = derivar_catalogo(raiz)
        fichas = leer_sede(raiz, argumentos.sede)
        negativos = importar_negativos(raiz)
        ancla = Ancla(raiz)
    except SedeIlegible as error:
        sys.stderr.write("[NO SE PUDO COMPROBAR] %s\n" % error)
        return NO_SE_PUDO_COMPROBAR

    juicios = juzgar(fichas, catalogo, negativos, ancla,
                     ejercer=not argumentos.sin_ejercer, solo=argumentos.solo, raiz=raiz)

    if argumentos.json:
        print(json.dumps(
            {"commit": ancla.commit, "tree": ancla.tree,
             "universo": catalogo,
             "invariantes": [{"id": j.id, "satisfecho": j.satisfecho,
                              "fallos": j.fallos, "notas": j.notas,
                              "ejercidos": j.ejercidos} for j in juicios]},
            ensure_ascii=False, indent=2))
        return HAY_INCUMPLIDOS if any(not j.satisfecho for j in juicios) else TODOS_SATISFECHOS

    return publicar(sys.stdout, juicios, catalogo, ancla,
                    not argumentos.sin_ejercer, fichas, negativos)


if __name__ == "__main__":
    sys.exit(main())
