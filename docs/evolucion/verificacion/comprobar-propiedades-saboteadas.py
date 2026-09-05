#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
`O26-SAB` · ¿QUEDAN PROPIEDADES CRÍTICAS SIN UNA PRUEBA CAPAZ DE FALLAR?
=======================================================================

POR QUÉ EXISTE ESTE FICHERO
---------------------------
El gate válido del 2026-09-05 dejó `O26` §5.2 **NO DEMOSTRADA**, y con un contraejemplo
vivo que el propio derivador publica pegado a su cifra:

    B · con cobertura y SIN NI UN SABOTAJE imputado que la ponga roja 0
        NO demuestra `O26` §5.2. Mide EXISTENCIA DE AL MENOS UN SABOTAJE imputado a la
        obligación, no que sus propiedades estén cubiertas una a una. Contraejemplo
        medido y vivo: `V6-12` figuraba con `B=0` mientras el append-only de la sede del
        Owner más allá del prefijo del nacimiento no tenía sabotaje ninguno (`ADJ-B3`)

`B` cuenta sabotajes POR OBLIGACIÓN. Una obligación tiene muchas propiedades, y un solo
sabotaje las da todas por probadas. Ésa es la distancia exacta entre `B=0` y `O26` §5.2, y
este fichero la mide **cambiando la unidad**: la unidad es la PROPIEDAD, no la obligación.
**No reutiliza la etiqueta `B`**: `B` puede alimentar `S1`, y no lo sustituye.

QUÉ ES AQUÍ UNA PROPIEDAD CRÍTICA, Y DE DÓNDE SE DERIVA
------------------------------------------------------
Cada cláusula `falla_si:` de cada escenario que cubre una obligación del universo derivado
y que declara prueba. Es la sede donde el corpus escribe, con esas palabras, QUÉ tiene que
poner roja la prueba. No se inventa ninguna propiedad y no se escribe ninguna lista: se
leen las cláusulas de sus bloques `ads:escenario`, que están dentro del universo y bajo
cliquet. Una propiedad se identifica por `escenario/f<n>` y arrastra las obligaciones a las
que pertenece.

LAS SEIS CONDICIONES DE `O28` §3 PARA §5.2, CADA UNA POR SEPARADO
-----------------------------------------------------------------
  `S1` SABOTAJE IMPUTADO
       existe al menos una `Mutacion` del catálogo único imputada al escenario que escribe
       la propiedad. Sede: `comprobar_negativos.CATALOGO`, que se IMPORTA y no se copia.
  `S2` MOTIVO DECLARADO
       ese sabotaje declara `espera`: el trozo de diagnóstico por el que tiene que caer.
       Sin `espera` sólo puede comprobarse QUE hay rojo, y `O28` §3.4 pide el MOTIVO.
  `S3` CANAL PRODUCTIVO, NO PRUEBA TEXTUAL
       lo que el sabotaje toca —medido APLICÁNDOLO y comparando el árbol, no leyendo su
       código— no puede estar todo dentro de la sede de las pruebas ni de la evidencia. Un
       sabotaje que edita el enunciado de la prueba ejerce el texto, no el producto.
  `S4` NO ES SÓLO LA HUELLA GENERAL
       un sabotaje detectado únicamente por `comprobar_integridad` no prueba la propiedad:
       la huella enrojece ante CUALQUIER edición del ámbito sellado, y por tanto no
       distingue esta propiedad de ninguna otra. Es el hallazgo `#21` en pequeño.
  `S5` ALCANCE ESPECÍFICO DE ESTA CLÁUSULA
       el motivo declarado del sabotaje ancla en ESTA cláusula y en ninguna otra del mismo
       escenario. Es la condición que `V6-12` incumplía: tenía sabotajes, y no el de la
       propiedad que cayó.
  `S6` CICLO SANO / SABOTAJE / RESTAURADO, EJECUTADO
       el árbol sano queda VERDE por el canal, el sabotaje lo pone ROJO por el motivo
       declarado, y la restauración devuelve el VERDE. Los tres, o no cuenta.

Los faltantes se publican INDIVIDUALMENTE —propiedad, obligaciones, requisito, motivo y el
texto literal de la cláusula—. El cardinal se DERIVA de esa lista; aquí no hay ninguna cifra
escrita a mano.

LO QUE ESTE FICHERO **NO** DEMUESTRA — y hay que leerlo antes que las cifras
---------------------------------------------------------------------------
  · `S5` ANCLA POR LÉXICO, y eso no es una demostración de identidad. Compara los términos
    DISTINTIVOS de la cláusula —los que no comparte con ninguna otra cláusula del mismo
    escenario— con el motivo declarado del sabotaje, y exige que el mejor encaje sea único.
    Un sabotaje y una cláusula que comparten vocabulario por casualidad producirían un
    ancla falsa. **Lo que falta en el corpus es una declaración explícita del enlace
    sabotaje→propiedad**, y mientras no exista, esto es lo más que se puede derivar sin
    inventarlo. Por eso `S5` no acredita solo: hace falta `S6`, que lo ejecuta;
  · un `S6` verde no demuestra que la propiedad sea INDERROTABLE por otro camino. Demuestra
    que ESTE sabotaje la alcanza y que la prueba cae por su motivo. `ADJ-B3` derrotó una
    propiedad que tenía sabotaje —el caso fácil— por un camino distinto; eso lo cierra
    añadiendo sabotajes, no midiendo mejor;
  · no dice nada de `O26` §5.1: eso lo mide `O26-IMPL`, con otro universo y otro criterio.
    Los dos verdes hacen falta y ninguno suple al otro;
  · nada sobre §5.3, §5.4 ni §5.5.

FALLA CERRADO
-------------
Si una sede no se puede leer, si el derivador no deriva o si el catálogo de mutaciones no se
puede importar, sale con código 2 y diagnóstico. No aprueba por ausencia de dato.

USO
    …/comprobar-propiedades-saboteadas.py                  # mide y publica (ejecuta `S6`)
    …/comprobar-propiedades-saboteadas.py --sin-ejecutar   # sin `S3` ni `S6` (se dice)
    …/comprobar-propiedades-saboteadas.py --solo T173      # un escenario
    …/comprobar-propiedades-saboteadas.py --autopruebas    # sabotajes del medidor
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
import io
import os
import re
import shutil
import subprocess
import sys
import unicodedata

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir, os.pardir, os.pardir))

DERIVADOR = "docs/evolucion/verificacion/derivar-universo-obligatorio.py"
MEDIDOR_IMPL = "docs/evolucion/verificacion/comprobar-obligaciones-implementadas.py"
NEGATIVOS = "kernel/operativo/validadores"
PRUEBAS = "kernel/operativo/pruebas"

# `S3` · las zonas cuya edición NO es ejercer el canal productivo. La sede de las pruebas es
# donde vive el ENUNCIADO de la propiedad; la de la evidencia, su registro. Un sabotaje que
# sólo toca eso demuestra que el texto cambió, no que el mecanismo falle.
ZONAS_DE_TEXTO = (PRUEBAS + "/",)

# `S4` · el canal que enrojece ante CUALQUIER edición del ámbito sellado. No distingue una
# propiedad de otra, y por eso no puede acreditar ninguna en particular.
CANALES_DE_HUELLA = ("comprobar_integridad", "huella")


class SedeIlegible(Exception):
    """Una sede que este instrumento necesita y no puede leer, o que dice algo imposible."""


# ---------------------------------------------------------------------------
#  las sedes, importadas — no copiadas
# ---------------------------------------------------------------------------

def _cargar(rel, nombre):
    import importlib.util                                          # noqa: PLC0415
    ruta = os.path.join(RAIZ, rel)
    if not os.path.isfile(ruta):
        raise SedeIlegible("falta la sede `%s`" % rel)
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    modulo = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(modulo)
    except Exception as e:                                         # noqa: BLE001
        raise SedeIlegible("`%s` no se puede cargar: %s: %s" % (rel, type(e).__name__, e))
    return modulo


def catalogo():
    """El catálogo ÚNICO de mutaciones, importado de su sede.

    `comprobar_negativos` monta su `CATALOGO` extendiéndolo con los cuatro módulos
    `negativos_*` al importarse. Se importa por eso: una segunda lectura del catálogo sería
    una segunda sede del mismo censo, que es lo que `Q-04` castigó.
    """
    if NEGATIVOS not in sys.path:
        sys.path.insert(0, os.path.join(RAIZ, NEGATIVOS))
    try:
        import comprobar_negativos as cn                           # noqa: PLC0415
    except Exception as e:                                         # noqa: BLE001
        raise SedeIlegible("el catálogo de mutaciones no se puede importar: %s: %s"
                           % (type(e).__name__, e))
    if not getattr(cn, "CATALOGO", None):
        raise SedeIlegible("el catálogo de mutaciones está VACÍO: sin sabotajes no hay nada "
                           "que medir, y un cero por catálogo vacío sería un falso verde")
    return cn


# ---------------------------------------------------------------------------
#  el universo de PROPIEDADES CRÍTICAS
# ---------------------------------------------------------------------------

class Propiedad:
    """Una cláusula `falla_si` de un escenario, con las obligaciones que arrastra."""

    def __init__(self, escenario, orden, texto, sede, validador):
        self.escenario = escenario
        self.orden = orden
        self.texto = texto
        self.sede = sede
        self.validador = validador
        self.obligaciones = []
        self.req = {}

    @property
    def id(self):
        return "%s/f%d" % (self.escenario, self.orden)


def universo_de_propiedades(solo=None):
    """`(propiedades, universo_de_obligaciones)`, derivado entero de sus sedes."""
    deriv = _cargar(DERIVADOR, "universo_obligatorio")
    medidor = _cargar(MEDIDOR_IMPL, "obligaciones_implementadas")
    try:
        obligaciones = deriv.universo_de_obligaciones()
    except Exception as e:                                         # noqa: BLE001
        raise SedeIlegible("el derivador no deriva el universo: %s: %s"
                           % (type(e).__name__, e))
    try:
        escenarios = medidor.escenarios()
    except Exception as e:                                         # noqa: BLE001
        raise SedeIlegible("los escenarios no se pueden leer: %s: %s"
                           % (type(e).__name__, e))
    if not obligaciones:
        raise SedeIlegible("el universo de obligaciones derivado está VACÍO")

    propiedades = {}
    for esc in escenarios:
        if not esc["validador"]:
            continue
        if solo and esc["id"] != solo:
            continue
        mias = sorted(o for o in obligaciones
                      if any(deriv._cubre(c, o) for c in esc["cubre"]))
        if not mias:
            continue
        if not esc["falla_si"]:
            # Un escenario que cubre una obligación y no escribe qué lo hace fallar no
            # aporta ninguna propiedad, y eso NO se calla: se publica como sede muda.
            propiedades.setdefault("__mudos__", []).append(esc["id"])
            continue
        for orden, texto in enumerate(esc["falla_si"], 1):
            prop = Propiedad(esc["id"], orden, texto, esc["sede"], esc["validador"])
            prop.obligaciones = mias
            propiedades[prop.id] = prop
    mudos = propiedades.pop("__mudos__", [])
    if not propiedades:
        raise SedeIlegible("no se ha derivado ni una propiedad crítica: sin propiedades no "
                           "hay nada que medir y el cero sería vacío por construcción")
    return propiedades, obligaciones, sorted(set(mudos))


# ---------------------------------------------------------------------------
#  `S5` · el ancla léxica, con su guarda de ambigüedad
# ---------------------------------------------------------------------------

# Palabras que aparecen en cualquier cláusula y por tanto no distinguen nada. La lista es
# corta a propósito: cuanto más se poda, más fácil es que un ancla salga por casualidad.
PARADAS = frozenset("""
    ninguna ningun ninguno alguna alguno cuando donde porque desde hasta entre sobre segun
    mismo misma mismos mismas sin con por para que los las una uno del de la el en al es son
    esta este estas estos como mas mientras puede pueden queda quedan sale salen dice dicen
    hace hacen tiene tienen ser sea haber sobre otra otro otras otros toda todo todas todos
""".split())


def _terminos(texto):
    """Los términos de un texto: sin acentos, sin marcas, de cinco letras para arriba."""
    plano = unicodedata.normalize("NFD", (texto or "").lower())
    plano = "".join(c for c in plano if unicodedata.category(c) != "Mn")
    return set(t for t in re.findall(r"[a-z0-9_.-]{5,}", plano) if t not in PARADAS)


def _distintivos(clausulas):
    """Para cada cláusula, los términos que NO comparte con ninguna otra del escenario."""
    todos = [_terminos(c) for c in clausulas]
    salida = []
    for i, propios in enumerate(todos):
        ajenos = set().union(*[t for j, t in enumerate(todos) if j != i]) if len(todos) > 1 \
            else set()
        salida.append(propios - ajenos)
    return salida


def ancla(clausulas, indice, motivo):
    """`(ancla, detalle)` · ¿el motivo ancla en la cláusula `indice` y en NINGUNA otra?"""
    distintivos = _distintivos(clausulas)
    terminos = _terminos(motivo)
    puntos = [len(d & terminos) for d in distintivos]
    mio = puntos[indice]
    if not distintivos[indice]:
        # Dos cláusulas que dicen lo mismo no se pueden separar por ningún motivo, y elegir
        # una es exactamente cómo `V6-12` daba por probada la propiedad equivocada.
        return False, ("la cláusula no tiene ni un término que la distinga de las otras "
                       "del escenario: el enlace no es inequívoco para ninguna de ellas")
    if mio == 0:
        return False, "el motivo no comparte ni un término distintivo con la cláusula"
    empatan = [i for i, p in enumerate(puntos) if i != indice and p >= mio]
    if empatan:
        return False, ("el motivo ancla igual de bien en la cláusula f%d: el enlace "
                       "sabotaje→propiedad no es inequívoco"
                       % (empatan[0] + 1))
    return True, "términos distintivos casados: %s" % ", ".join(
        sorted(distintivos[indice] & terminos)[:4])


# ---------------------------------------------------------------------------
#  `S3` y `S6` · lo que sólo se sabe APLICANDO y EJECUTANDO
# ---------------------------------------------------------------------------

def _copiar(a_donde):
    """Copia el corpus sin `.git` ni caché, igual que hace `comprobar_negativos`.

    Se excluye `.git` A PROPÓSITO y no por comodidad: con el repositorio enlazado, la propia
    mutación aparecería como una divergencia respecto de `HEAD` y algún canal se pondría
    rojo por eso y no por la propiedad, que es justo el motivo equivocado que `S6` existe
    para descartar. Lo que se pierde —y se dice— es que los canales que contrastan contra
    `HEAD` corren aquí sin repositorio, en el mismo modo en que ya los corre el catálogo.
    """
    shutil.copytree(RAIZ, a_donde, symlinks=True,
                    ignore=lambda d, n: [x for x in n
                                         if x in (".git", "__pycache__", ".pytest_cache")])


def _inventario(base):
    """`{ruta relativa: (tamaño, mtime)}` de un árbol, sin caché ni repositorio."""
    salida = {}
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "__pycache__", ".pytest_cache")]
        for nombre in filenames:
            ruta = os.path.join(dirpath, nombre)
            try:
                st = os.lstat(ruta)
            except OSError:
                continue
            salida[os.path.relpath(ruta, base).replace(os.sep, "/")] = (st.st_size,
                                                                        int(st.st_mtime))
    return salida


def tocados(antes, despues):
    """Las rutas que el sabotaje creó, borró o cambió. Es la MEDIDA de lo que tocó."""
    cambiadas = set()
    for rel, marca in despues.items():
        if antes.get(rel) != marca:
            cambiadas.add(rel)
    cambiadas.update(set(antes) - set(despues))
    return sorted(cambiadas)


def restaurar(destino, rutas):
    """Devuelve la copia a su estado anterior copiando de la RAÍZ las rutas tocadas."""
    for rel in rutas:
        origen = os.path.join(RAIZ, rel)
        copia = os.path.join(destino, rel)
        if os.path.isfile(origen):
            os.makedirs(os.path.dirname(copia), exist_ok=True)
            shutil.copy2(origen, copia)
        elif os.path.exists(copia):
            os.remove(copia)


# Las mismas banderas con las que el catálogo corre sus canales. Se declaran aquí una vez
# porque `_canal` es la ÚNICA invocación local; el juicio del rojo y de su motivo NO se
# reescribe: lo hace `comprobar_negativos.ejecutar`, que es su sede.
TIEMPO_MAXIMO = 1800


def _canal(cn, mut, destino):
    """Corre el canal del sabotaje sobre `destino` SIN sabotearlo. `(verde, detalle)`.

    Sirve para el paso SANO y para el paso RESTAURADO. El paso del SABOTAJE no pasa por
    aquí: lo ejecuta y lo juzga `comprobar_negativos.ejecutar`, que es donde vive la
    comprobación del MOTIVO, y duplicarla aquí crearía una segunda sede del mismo juicio.
    """
    if mut.clase == cn.CLASE_BATERIA:
        ruta = os.path.join(destino, mut.validador)
        orden = [sys.executable, ruta] + list(mut.casos)
    else:
        ruta = os.path.join(destino, NEGATIVOS, "%s.py" % mut.validador)
        orden = [sys.executable, ruta, "--json", "--raiz", destino]
    if not os.path.isfile(ruta):
        return False, "el canal `%s` no existe en la copia" % mut.validador
    try:
        proc = subprocess.run(orden, capture_output=True, text=True, cwd=destino,
                              timeout=TIEMPO_MAXIMO)
    except subprocess.TimeoutExpired:
        return False, "el canal no terminó en %d s" % TIEMPO_MAXIMO
    except OSError as e:
        return False, "no se pudo ejecutar el canal: %s" % e
    if proc.returncode == 0:
        return True, "EXIT=0"
    return False, "EXIT=%s · %s" % (proc.returncode, _porque(cn, mut, proc))


def _porque(cn, mut, proc):
    """QUÉ cayó, dicho con nombres. Un canal de validador termina su salida `--json` con un
    corchete, y publicar «]» como diagnóstico es no publicar ninguno: la primera versión de
    este fichero lo hizo y el faltante decía «sano → EXIT=1 · ]». Se lee el JSON y se
    nombran las pruebas caídas; si no es JSON, se recorta la última línea con contenido.
    """
    salida = proc.stdout + proc.stderr
    if mut.clase != cn.CLASE_BATERIA:
        import json                                                # noqa: PLC0415
        try:
            filas = json.loads(proc.stdout)
        except ValueError:
            filas = None
        if isinstance(filas, list):
            caidas = [f.get("id") for f in filas
                      if isinstance(f, dict) and f.get("estado") == "prueba-fallida"]
            if caidas:
                return "caen %s en el árbol SIN sabotear" % ", ".join(
                    str(c) for c in caidas[:6])
    lineas = [l for l in salida.strip().splitlines() if l.strip() and l.strip() != "]"]
    return (lineas or ["(sin salida)"])[-1][:160]


class Ciclos:
    """Ejecuta el ciclo SANO/SABOTAJE/RESTAURADO por mutación, y lo recuerda."""

    def __init__(self, cn, tmp_base):
        self.cn = cn
        self.tmp = tmp_base
        self._sanos = {}
        self._ciclos = {}

    def sano(self, mut):
        """El canal sobre el árbol INTACTO. Se memoriza por canal: el árbol es el mismo."""
        clave = "%s|%s" % (mut.validador, " ".join(mut.casos))
        if clave not in self._sanos:
            destino = os.path.join(self.tmp, "sano-%d" % len(self._sanos))
            _copiar(destino)
            self._sanos[clave] = self._canal_verde(mut, destino)
            shutil.rmtree(destino, ignore_errors=True)
        return self._sanos[clave]

    def _canal_verde(self, mut, destino):
        return _canal(self.cn, mut, destino)

    def de(self, mut):
        """`{"sano","sabotaje","restaurado","tocados"}` para una mutación."""
        if mut.id in self._ciclos:
            return self._ciclos[mut.id]
        paso = {}
        paso["sano"] = self.sano(mut)
        destino = os.path.join(self.tmp, mut.id)
        _copiar(destino)
        antes = _inventario(destino)
        try:
            mut.aplicar(destino)
        except Exception as e:                                     # noqa: BLE001
            paso["tocados"] = []
            paso["sabotaje"] = (False, "el sabotaje no se pudo aplicar: %s: %s"
                                % (type(e).__name__, e))
            paso["restaurado"] = (False, "no se llegó a restaurar")
            self._ciclos[mut.id] = paso
            shutil.rmtree(destino, ignore_errors=True)
            return paso
        paso["tocados"] = tocados(antes, _inventario(destino))
        # El ROJO y su MOTIVO los juzga el catálogo, que es su sede. Se le pide que corra
        # este caso sobre SU propia copia: `ejecutar` copia, aplica y juzga.
        mut.resultado, mut.detalle = None, ""
        self.cn.ejecutar(mut, os.path.join(self.tmp, "juicio"))
        paso["sabotaje"] = (mut.resultado == "detectada", "%s: %s"
                            % (mut.resultado, mut.detalle))
        restaurar(destino, paso["tocados"])
        residuo = tocados(antes, _inventario(destino))
        if residuo:
            paso["restaurado"] = (False, "la restauración no devolvió el árbol: siguen "
                                         "cambiadas %s" % ", ".join(residuo[:3]))
        else:
            paso["restaurado"] = self._canal_verde(mut, destino)
        shutil.rmtree(destino, ignore_errors=True)
        self._ciclos[mut.id] = paso
        return paso


# ---------------------------------------------------------------------------
#  la medición
# ---------------------------------------------------------------------------

REQUISITOS = (
    ("S1", "SABOTAJE IMPUTADO AL ESCENARIO"),
    ("S2", "MOTIVO DEL ROJO DECLARADO"),
    ("S3", "CANAL PRODUCTIVO, NO PRUEBA TEXTUAL"),
    ("S4", "NO ES SÓLO LA HUELLA GENERAL"),
    ("S5", "ALCANCE ESPECÍFICO DE ESTA CLÁUSULA"),
    ("S6", "CICLO SANO / SABOTAJE / RESTAURADO"),
)


def _es_textual(rutas):
    """¿Todo lo que el sabotaje tocó vive en la sede del ENUNCIADO y no en el producto?"""
    if not rutas:
        return True
    return all(any(r.startswith(z) for z in ZONAS_DE_TEXTO) for r in rutas)


def medir(ejecutar=True, solo=None, destino_traza=None):
    propiedades, obligaciones, mudos = universo_de_propiedades(solo=solo)
    cn = catalogo()
    por_prueba = {}
    for mut in cn.CATALOGO:
        por_prueba.setdefault(mut.prueba, []).append(mut)

    # Las cláusulas del escenario, para el ancla de `S5`. Se reconstruyen del propio
    # universo de propiedades, que es de donde salieron.
    clausulas = {}
    for prop in propiedades.values():
        clausulas.setdefault(prop.escenario, []).append((prop.orden, prop.texto))
    for esc in clausulas:
        clausulas[esc] = [t for _o, t in sorted(clausulas[esc])]

    import tempfile                                                # noqa: PLC0415
    tmp = tempfile.mkdtemp(prefix="ads-o26-sab-") if ejecutar else None
    ciclos = Ciclos(cn, tmp) if ejecutar else None
    try:
        for clave in sorted(propiedades):
            prop = propiedades[clave]
            candidatas = por_prueba.get(prop.escenario, [])
            prop.req["S1"] = (
                bool(candidatas),
                ("%d sabotajes imputados a `%s`: %s"
                 % (len(candidatas), prop.escenario,
                    ", ".join(m.id for m in candidatas[:6])))
                if candidatas else
                "ningún sabotaje del catálogo está imputado a `%s`" % prop.escenario)

            con_motivo = [m for m in candidatas if m.espera]
            prop.req["S2"] = (
                bool(con_motivo),
                "%d con `espera`: %s" % (len(con_motivo),
                                         ", ".join(m.id for m in con_motivo[:6]))
                if con_motivo else
                ("los %d sabotajes de `%s` (%s) no declaran `espera`: sólo puede "
                 "comprobarse que hay rojo, no por qué"
                 % (len(candidatas), prop.escenario,
                    ", ".join(m.id for m in candidatas[:4]))
                 if candidatas else "no hay sabotaje del que exigir motivo"))

            no_huella = [m for m in con_motivo
                         if not any(h in m.validador for h in CANALES_DE_HUELLA)]
            prop.req["S4"] = (
                bool(no_huella),
                "canales: %s" % ", ".join(sorted({m.validador for m in no_huella}))[:120]
                if no_huella else
                ("los sabotajes de `%s` sólo los detecta la huella general (%s), que "
                 "enrojece ante cualquier edición del ámbito sellado y no distingue esta "
                 "propiedad de ninguna otra"
                 % (prop.escenario, ", ".join(sorted({m.validador for m in con_motivo})))
                 if con_motivo else "no hay sabotaje con motivo del que mirar el canal"))

            # `S5` · el ancla, sobre las candidatas que han llegado hasta aquí.
            elegidas, detalles = [], []
            indice = prop.orden - 1
            for mut in no_huella:
                anclado, detalle = ancla(clausulas[prop.escenario], indice,
                                         "%s %s" % (mut.descripcion or "", mut.espera or ""))
                if anclado:
                    elegidas.append((mut, detalle))
                else:
                    detalles.append("%s: %s" % (mut.id, detalle))
            prop.req["S5"] = (
                bool(elegidas),
                "%s ancla en esta cláusula y en ninguna otra · %s"
                % (elegidas[0][0].id, elegidas[0][1]) if elegidas else
                ("ningún sabotaje de `%s` se puede imputar a ESTA cláusula y a ninguna "
                 "otra — falta la declaración del enlace sabotaje→propiedad: %s"
                 % (prop.escenario, "; ".join(detalles[:2]))
                 if no_huella else "no hay sabotaje que anclar"))

            # `S3` y `S6` · lo que sólo se sabe aplicando y ejecutando.
            if not ejecutar:
                prop.req["S3"] = (None, "NO COMPROBADO (`--sin-ejecutar`)")
                prop.req["S6"] = (None, "NO EJECUTADO (`--sin-ejecutar`)")
                continue
            if not elegidas:
                prop.req["S3"] = (False, "no hay sabotaje que aplicar")
                prop.req["S6"] = (False, "no hay sabotaje que ejecutar")
                continue
            aprobada_s3, aprobada_s6, quejas3, quejas6 = None, None, [], []
            for mut, _detalle in elegidas:
                if destino_traza is not None:
                    destino_traza.write("    · ciclo de %s (%s) …\n" % (mut.id, prop.id))
                    destino_traza.flush()
                paso = ciclos.de(mut)
                if _es_textual(paso["tocados"]):
                    quejas3.append("%s: sólo toca la sede del enunciado (%s)"
                                   % (mut.id, ", ".join(paso["tocados"][:2]) or "nada"))
                    continue
                aprobada_s3 = aprobada_s3 or (mut, paso)
                mal = [n for n in ("sano", "sabotaje", "restaurado") if not paso[n][0]]
                if mal:
                    quejas6.append("%s: %s" % (mut.id, "; ".join(
                        "%s → %s" % (n, paso[n][1]) for n in mal)))
                else:
                    aprobada_s6 = (mut, paso)
                    break
            prop.req["S3"] = (bool(aprobada_s3),
                              "%s toca %s" % (aprobada_s3[0].id,
                                              ", ".join(aprobada_s3[1]["tocados"][:3]))
                              if aprobada_s3 else "; ".join(quejas3[:2]))
            prop.req["S6"] = (bool(aprobada_s6),
                              "%s · sano VERDE · rojo por el motivo · restaurado VERDE"
                              % aprobada_s6[0].id if aprobada_s6 else
                              ("; ".join(quejas6[:2]) or "ningún sabotaje llegó al ciclo"))
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)
    return propiedades, obligaciones, mudos


# El orden en que se DIAGNOSTICA no es el orden en que se publica. Se mira primero lo que
# se sabe sin ejecutar —hay sabotaje, declara motivo, no es sólo la huella, ancla en esta
# cláusula— y sólo después lo que exige aplicar y correr. Al revés, un `S3` sin comprobar
# taparía un `S5` roto y la lista de faltantes diría dónde NO está el problema.
ORDEN_DE_DIAGNOSTICO = ("S1", "S2", "S4", "S5", "S3", "S6")


def faltantes(propiedades):
    lista = []
    for clave in sorted(propiedades):
        prop = propiedades[clave]
        for req in ORDEN_DE_DIAGNOSTICO:
            cumple, motivo = prop.req[req]
            if cumple is not True:
                lista.append((prop, req, motivo))
                break        # el primero que falta es el que hay que arreglar
    return lista


# ---------------------------------------------------------------------------
#  publicación
# ---------------------------------------------------------------------------

def publicar(destino, ejecutar=True, solo=None, traza=False):
    propiedades, obligaciones, mudos = medir(
        ejecutar=ejecutar, solo=solo, destino_traza=destino if traza else None)
    faltas = faltantes(propiedades)
    pendientes = sorted({p.id for p, _r, _m in faltas})
    afectadas = sorted({o for p, _r, _m in faltas for o in p.obligaciones})

    destino.write("`O26-SAB` · PROPIEDADES CRÍTICAS CON UNA PRUEBA CAPAZ DE FALLAR\n")
    destino.write("=" * 78 + "\n\n")
    destino.write("  UNIDAD    la CLÁUSULA `falla_si`, no la obligación. `B` cuenta "
                  "sabotajes por\n            obligación; ésta es la distancia exacta entre "
                  "`B=0` y `O26` §5.2\n")
    destino.write("  CRITERIO  `O28` §3, las seis condiciones de §5.2, cada una por "
                  "separado\n")
    for clave, titulo in REQUISITOS:
        destino.write("            %s  %s\n" % (clave, titulo))
    destino.write("\n")

    destino.write("EL UNIVERSO DE PROPIEDADES, DERIVADO\n")
    destino.write("-" * 78 + "\n")
    escenarios = sorted({p.escenario for p in propiedades.values()})
    destino.write("  %d propiedades críticas · %d escenarios · %d obligaciones del "
                  "universo\n" % (len(propiedades), len(escenarios), len(obligaciones)))
    if mudos:
        destino.write("  escenarios que cubren obligación y NO escriben `falla_si` "
                      "—sedes mudas, no aportan propiedad y no se callan— (%d): %s\n"
                      % (len(mudos), ", ".join(mudos)))

    destino.write("\nPOR REQUISITO — dónde se rompe la cadena\n")
    destino.write("-" * 78 + "\n")
    for clave, titulo in REQUISITOS:
        cuantas = sum(1 for _p, r, _m in faltas if r == clave)
        destino.write("  %s  %-42s  primeras faltas: %d\n" % (clave, titulo, cuantas))

    destino.write("\nFALTANTES, UNO A UNO — propiedad, obligaciones, requisito y motivo\n")
    destino.write("-" * 78 + "\n")
    if not faltas:
        destino.write("  ninguno\n")
    for prop, req, motivo in faltas:
        destino.write("  %-12s %-3s %s\n" % (prop.id, req, ",".join(prop.obligaciones)))
        destino.write("       «%s»\n" % prop.texto[:150])
        destino.write("       %s · sede %s\n" % (motivo[:260], prop.sede))

    destino.write("\n")
    destino.write("  %d propiedades críticas medidas · %d PENDIENTES · %d obligaciones "
                  "afectadas\n" % (len(propiedades), len(pendientes), len(afectadas)))
    destino.write("  obligaciones con alguna propiedad pendiente: %s\n"
                  % (", ".join(afectadas) if afectadas else "∅"))
    destino.write("  pendientes de `O26-SAB`: %s\n"
                  % ("∅" if not pendientes else "%d propiedades, enumeradas arriba"
                     % len(pendientes)))
    destino.write("  `O26` §5.2 · %s por este instrumento\n"
                  % ("ACREDITADA" if not pendientes and ejecutar else "NO ACREDITADA"))
    destino.write("\nLO QUE ESTE VEREDICTO NO DEMUESTRA\n")
    destino.write("-" * 78 + "\n")
    destino.write("  · `S5` ancla por LÉXICO con guarda de ambigüedad; lo que falta en el\n"
                  "    corpus es una declaración explícita del enlace sabotaje→propiedad\n")
    destino.write("  · un `S6` verde demuestra que ESE sabotaje alcanza la propiedad, no\n"
                  "    que la propiedad sea inderrotable por otro camino (`ADJ-B3`)\n")
    destino.write("  · no dice nada de `O26` §5.1 —eso es `O26-IMPL`— ni de §5.3 a §5.5\n")
    if not ejecutar:
        destino.write("  · `S3` y `S6` NO se han comprobado en esta corrida: el veredicto\n"
                      "    es NO ACREDITADA por construcción, y no por lo medido\n")
    return 1 if pendientes else 0


# ---------------------------------------------------------------------------
#  autopruebas · un medidor cuyo autotest no puede fallar no mide
# ---------------------------------------------------------------------------

SABOTAJES = []


def _sabotaje(rotulo, espera, argumentos=("--sin-ejecutar",)):
    def envoltorio(fn):
        SABOTAJES.append((rotulo, espera, argumentos, fn))
        return fn
    return envoltorio


def _fichero_del_escenario(destino, identificador):
    base = os.path.join(destino, PRUEBAS)
    for nombre in sorted(os.listdir(base)):
        if not nombre.endswith(".md"):
            continue
        ruta = os.path.join(base, nombre)
        with io.open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        if re.search(r"^id: %s$" % re.escape(identificador), texto, re.M):
            return ruta, texto
    raise AssertionError("no encuentro el escenario %s en la copia" % identificador)


def _reescribir_escenario(destino, identificador, viejo, nuevo):
    """Sustituye SÓLO dentro del bloque del escenario pedido."""
    ruta, texto = _fichero_del_escenario(destino, identificador)
    cabeza, cola = texto.split("id: %s\n" % identificador, 1)
    corte = cola.find("```")
    bloque, resto = cola[:corte], cola[corte:]
    if viejo not in bloque:
        raise AssertionError("el sabotaje no encuentra %r en el bloque de %s"
                             % (viejo[:50], identificador))
    with io.open(ruta, "w", encoding="utf-8") as fh:
        fh.write(cabeza + "id: %s\n" % identificador
                 + bloque.replace(viejo, nuevo, 1) + resto)


@_sabotaje("una cláusula `falla_si` se BORRA: la propiedad desaparece del universo",
           "propiedades críticas medidas")
def _s_clausula_borrada(destino):
    """El universo de propiedades tiene que ENCOGER visiblemente, y el cardinal derivarse.

    Este sabotaje no busca un rojo: busca que la cifra se MUEVA. El control lo hace la
    autoprueba comparando el cardinal con el de la copia intacta; si el instrumento tuviera
    el número escrito, no se movería y esto lo cazaría.
    """
    ruta, texto = _fichero_del_escenario(destino, "T173")
    cabeza, cola = texto.split("id: T173\n", 1)
    corte = cola.find("```")
    bloque, resto = cola[:corte], cola[corte:]
    lineas = bloque.splitlines(True)
    dentro, salida = False, []
    for linea in lineas:
        if linea.startswith("falla_si:"):
            dentro = True
            salida.append(linea)
            continue
        if dentro and re.match(r"^\s+-\s", linea):
            dentro = False        # se cae la PRIMERA cláusula, y sólo ella
            continue
        salida.append(linea)
    with io.open(ruta, "w", encoding="utf-8") as fh:
        fh.write(cabeza + "id: T173\n" + "".join(salida) + resto)


@_sabotaje("el catálogo de mutaciones se VACÍA — un cero por catálogo vacío es falso verde",
           "el catálogo de mutaciones está VACÍO")
def _s_catalogo_vacio(destino):
    ruta = os.path.join(destino, NEGATIVOS, "comprobar_negativos.py")
    with io.open(ruta, "a", encoding="utf-8") as fh:
        fh.write("\n\nCATALOGO = []\n")


# Los tres sabotajes que siguen INYECTAN un catálogo de una sola mutación imputada a `T244`
# —que cubre `F-04` y escribe sus cláusulas— por el mismo camino por el que
# `_s_catalogo_vacio` lo vacía: al nivel del módulo, que es donde el catálogo se monta.
# Reescribir el `Mutacion(...)` concreto dentro de `negativos_runtime.py` ataba el sabotaje
# a la POSICIÓN de un literal que cualquiera puede mover, y un autotest que se rompe al
# reordenar el catálogo no mide el instrumento: mide el catálogo.
_SIN_MOTIVO = '''

def m_sin_motivo(raiz):
    """Nunca llega a aplicarse: `S2` corta la cadena antes de ejecutar nada."""
    return None


CATALOGO[:] = [Mutacion("NSINESPERA", "S2", "T244", "comprobar_contratos",
                        "el grado inicial del encuadre se declara de otra manera",
                        m_sin_motivo)]
'''


@_sabotaje("el único sabotaje de la propiedad pierde su `espera`: hay rojo y no hay MOTIVO",
           "no declaran `espera`",
           ("--sin-ejecutar", "--solo", "T244"))
def _s_espera_retirada(destino):
    """`S2` · sin `espera` sólo se comprueba QUE hay rojo. `O28` §3.4 pide el motivo."""
    ruta = os.path.join(destino, NEGATIVOS, "comprobar_negativos.py")
    with io.open(ruta, "a", encoding="utf-8") as fh:
        fh.write(_SIN_MOTIVO)


_SOLO_HUELLA = '''

def m_solo_la_huella(raiz):
    """Nunca llega a aplicarse: `S4` corta la cadena antes de ejecutar nada."""
    return None


CATALOGO[:] = [Mutacion("NHUELLA", "S4", "T244", "comprobar_integridad",
                        "el grado inicial del encuadre se declara de otra manera",
                        m_solo_la_huella,
                        espera="la huella del kernel no coincide")]
'''


@_sabotaje("el único sabotaje de la propiedad pasa a detectarlo SÓLO la huella general",
           "sólo los detecta la huella general",
           ("--sin-ejecutar", "--solo", "T244"))
def _s_solo_huella(destino):
    """`S4` · el hallazgo `#21` en pequeño: la huella enrojece ante cualquier edición del
    ámbito sellado, y por eso no acredita ninguna propiedad en particular."""
    ruta = os.path.join(destino, NEGATIVOS, "comprobar_negativos.py")
    with io.open(ruta, "a", encoding="utf-8") as fh:
        fh.write(_SOLO_HUELLA)


_SABOTAJE_MUDO = r'''

def m_toca_el_producto_y_no_enrojece(raiz):
    """Toca código productivo de verdad y NO derrota ninguna propiedad: el canal sigue
    verde. Es el sabotaje que existe en el papel y no prueba nada."""
    with open(raiz + "/kernel/operativo/runtime/runtime/politica.py", "a",
              encoding="utf-8") as fh:
        fh.write("\n# sabotaje inerte\n")


CATALOGO[:] = [Mutacion("NMUDO", "S6", "T244", "comprobar_contratos",
                        "el grado inicial persistido difiere del global del paso 5",
                        m_toca_el_producto_y_no_enrojece,
                        espera="difiere")]
'''


@_sabotaje("el sabotaje toca el producto y NO pone rojo: el ciclo tiene que decirlo",
           "siguió SUPERADA con la infracción introducida",
           ("--solo", "T244"))
def _s_ciclo_sin_rojo(destino):
    """`S6` · un sabotaje que no derrota la propiedad no la prueba. Pasa `S1` a `S5` —está
    imputado, declara motivo, no es la huella, ancla en `f1` por «difiere» y toca código
    productivo— y se cae en el único sitio donde puede caerse: al EJECUTARLO. Sin este
    control, `O26-SAB` acreditaría propiedades cuyo sabotaje sólo existe en el catálogo.
    """
    ruta = os.path.join(destino, NEGATIVOS, "comprobar_negativos.py")
    with io.open(ruta, "a", encoding="utf-8") as fh:
        fh.write(_SABOTAJE_MUDO)


@_sabotaje("dos cláusulas de un escenario se hacen INDISTINGUIBLES: el ancla deja de serlo",
           "no tiene ni un término que la distinga",
           ("--sin-ejecutar", "--solo", "T173"))
def _s_ancla_ambigua(destino):
    """`S5` · si dos cláusulas dicen lo mismo, ningún motivo puede imputarse a una y no a la
    otra. El instrumento tiene que DECIRLO en vez de quedarse con la primera, que es cómo
    `V6-12` daba por probada la propiedad equivocada."""
    ruta, texto = _fichero_del_escenario(destino, "T173")
    cabeza, cola = texto.split("id: T173\n", 1)
    corte = cola.find("```")
    bloque, resto = cola[:corte], cola[corte:]
    m = re.search(r"^falla_si:\n((?:\s+-\s.*\n)+)", bloque, re.M)
    if not m:
        raise AssertionError("`T173` no escribe `falla_si`")
    primera = m.group(1).splitlines(True)[0]
    with io.open(ruta, "w", encoding="utf-8") as fh:
        fh.write(cabeza + "id: T173\n"
                 + bloque.replace(m.group(1), primera + primera, 1) + resto)


# `S3` se mide APLICANDO el sabotaje y mirando qué tocó, no leyendo su código. Para
# ejercerlo hace falta un sabotaje que sólo toque la sede del enunciado; se inyecta uno en
# el catálogo —por el mismo camino por el que `_s_catalogo_vacio` lo vacía— con un motivo
# que ancla en la primera cláusula de `T173` («reconstruirlo desde los eventos»), de modo
# que llegue hasta `S3` en vez de caerse antes en `S5`.
_SABOTAJE_TEXTUAL = '''

def m_solo_el_enunciado(raiz):
    """Edita el `.md` de la prueba y NADA del producto: la prueba textual del `S3`."""
    _sustituir(raiz, "kernel/operativo/pruebas/T172-T181-estado-durable.md",
               "leer el estado exige reconstruirlo desde los eventos",
               "leer el estado exige reconstruirlo desde los eventos ")


CATALOGO[:] = [Mutacion("NTEXTO", "S3", "T173",
                        "kernel/operativo/runtime/pruebas/test_estado_durable.py",
                        "leer el estado exige reconstruirlo desde los eventos",
                        m_solo_el_enunciado,
                        espera="reconstruirlo desde los eventos",
                        clase=CLASE_BATERIA)]
'''


@_sabotaje("el único sabotaje de la propiedad pasa a tocar SÓLO la sede del enunciado",
           "sólo toca la sede del enunciado",
           ("--solo", "T173"))
def _s_prueba_textual(destino):
    ruta = os.path.join(destino, NEGATIVOS, "comprobar_negativos.py")
    with io.open(ruta, "a", encoding="utf-8") as fh:
        fh.write(_SABOTAJE_TEXTUAL)


def _medir_en_la_copia(destino, argumentos):
    ruta = os.path.join(destino, "docs/evolucion/verificacion",
                        os.path.basename(os.path.abspath(__file__)))
    limpio = {k: v for k, v in os.environ.items() if not k.startswith("PYTHON")}
    limpio["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.run([sys.executable, ruta] + list(argumentos),
                          capture_output=True, text=True, cwd=destino, env=limpio,
                          timeout=TIEMPO_MAXIMO)
    return proc.returncode, proc.stdout + proc.stderr


def autopruebas(destino_stdout):
    import tempfile                                                # noqa: PLC0415

    destino_stdout.write("META-PRUEBAS DE `O26-SAB`\n")
    destino_stdout.write("=" * 78 + "\n\n")
    fallidos = 0
    raiz_tmp = tempfile.mkdtemp(prefix="ads-o26-sab-meta-")
    try:
        limpio = os.path.join(raiz_tmp, "control")
        _copiar(limpio)
        rc, texto = _medir_en_la_copia(limpio, ("--sin-ejecutar",))
        m = re.search(r"(\d+) propiedades críticas medidas", texto)
        bien = bool(m) and int(m.group(1)) > 0 and "FALTANTES, UNO A UNO" in texto
        cardinal = int(m.group(1)) if m else -1
        destino_stdout.write("  %-4s CONTROL POSITIVO · la copia intacta deriva %d "
                             "propiedades y publica\n"
                             % ("ok" if bien else "FALLA", cardinal))
        if not bien:
            fallidos += 1
            destino_stdout.write("       %s\n" % texto[-400:])

        for indice, (rotulo, espera, argumentos, aplicar) in enumerate(SABOTAJES):
            destino = os.path.join(raiz_tmp, "s%02d" % indice)
            _copiar(destino)
            try:
                aplicar(destino)
            except Exception as e:                                 # noqa: BLE001
                fallidos += 1
                destino_stdout.write("  %-4s %s\n" % ("ROTO", rotulo))
                destino_stdout.write("       el sabotaje no se pudo aplicar: %s: %s\n"
                                     % (type(e).__name__, e))
                continue
            rc, texto = _medir_en_la_copia(destino, argumentos)
            if espera == "propiedades críticas medidas":
                # El único control de CARDINAL: la cifra tiene que MOVERSE, porque se
                # deriva. Una cifra escrita a mano no se movería y este control lo dice.
                m = re.search(r"(\d+) propiedades críticas medidas", texto)
                movida = bool(m) and int(m.group(1)) == cardinal - 1
                resultado = "ok" if movida else "NO DETECTADA"
                detalle = "cardinal antes %d · ahora %s" % (
                    cardinal, m.group(1) if m else "(no publicado)")
            elif espera in texto:
                resultado, detalle = "ok", ""
            elif "Traceback (most recent call last)" in texto:
                resultado, detalle = "TRAZA", texto[-400:]
            else:
                resultado = "MOTIVO EQUIVOCADO" if rc else "NO DETECTADA"
                detalle = texto[-400:]
            if resultado != "ok":
                fallidos += 1
            destino_stdout.write("  %-4s %s\n" % (resultado, rotulo))
            destino_stdout.write("       espera «%s»%s\n"
                                 % (espera, " · " + detalle if detalle else ""))
    finally:
        shutil.rmtree(raiz_tmp, ignore_errors=True)
    destino_stdout.write("\n  %d sabotajes · %d sin detectar\n"
                         % (len(SABOTAJES), fallidos))
    return 1 if fallidos else 0


def main():
    ap = argparse.ArgumentParser(
        description="`O26-SAB` · las seis condiciones de `O28` §3 sobre cada propiedad")
    ap.add_argument("--autopruebas", action="store_true")
    ap.add_argument("--sin-ejecutar", action="store_true",
                    help="no comprueba `S3` ni `S6`; el veredicto lo dice y no acredita")
    ap.add_argument("--solo", default=None, help="mide un solo escenario")
    ap.add_argument("--traza", action="store_true", help="dice qué ciclo está corriendo")
    args = ap.parse_args()
    if args.autopruebas:
        return autopruebas(sys.stdout)
    try:
        return publicar(sys.stdout, ejecutar=not args.sin_ejecutar, solo=args.solo,
                        traza=args.traza)
    except SedeIlegible as e:
        sys.stderr.write("FALLA CERRADO · %s\n" % e)
        return 2


if __name__ == "__main__":
    sys.exit(main())
