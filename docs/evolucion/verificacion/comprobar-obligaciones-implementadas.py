#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
`O26-IMPL` · ¿QUEDAN OBLIGACIONES INTERNAS DE `F6` SIN IMPLEMENTAR?
==================================================================

POR QUÉ EXISTE ESTE FICHERO
---------------------------
El gate válido del 2026-09-05 dejó `O26` §5.1 **NO DEMOSTRADA**, y lo dejó así porque el
único instrumento que decía algo sobre ella publica, PEGADO A SU PROPIA CIFRA, que no la
demuestra:

    A · sin COBERTURA DECLARADA: ningún `cubre` con validador la nombra 0
        NO demuestra `O26` §5.1. Mide TRAZABILIDAD DECLARADA: que algún escenario nombre
        la obligación en su `cubre` y declare un validador. Un `cubre` es una declaración
        escrita, y este aparato no sabe si lo declarado está construido

`A` mide bien lo que mide. Lo que no hay —y ésta es la falta— es una medición del predicado
que `O26` §5.1 enuncia. `O28` §3 la hizo comprobable fijando su significado operativo, y
este fichero la ejecuta. **No reutiliza la etiqueta `A`**: `A` puede alimentar el requisito
`R2`, y no lo sustituye.

QUÉ MIDE, LITERALMENTE
----------------------
Para cada obligación del universo derivado, las CINCO condiciones de `O28` §3, cada una por
separado y cada una publicada con nombre y apellido cuando falta:

  `R1` PERTENENCIA DERIVADA Y PROTEGIDA
       la obligación sale de un universo derivado de las fuentes normativas —no de una
       lista escrita a mano— y el cliquet de los manifiestos inmutables la protege. Sede:
       `derivar-universo-obligatorio.py`, que se IMPORTA y no se copia.
  `R2` CÓDIGO PRODUCTIVO, CON TRAZABILIDAD INEQUÍVOCA
       desde la obligación hasta ficheros de código que NO son prueba ni evidencia,
       siguiendo la cadena `obligación → escenario que la cubre → prueba declarada →
       módulos que esa prueba importa o invoca`. «Inequívoca» se ejecuta: un nombre que
       resuelve en DOS raíces de paquete se publica como AMBIGUO y no cuenta.
  `R3` PRUEBA EJECUTABLE
       la prueba declarada existe, es un punto invocable —`__main__` o shebang— y su
       escenario declara cómo se ejecuta.
  `R4` EVIDENCIA LIGADA AL SHA Y AL TREE
       el fichero de evidencia existe, `HEAD` lo tiene confirmado, y sus bytes de trabajo
       producen EXACTAMENTE el mismo identificador de blob que el árbol de `HEAD`. Se
       publican el commit, el tree y el blob. Sin repositorio no se aprueba por defecto:
       se dice que no se puede comprobar y cuenta como faltante.
  `R5` CONDICIÓN DE CIERRE EJECUTADA
       la prueba se EJECUTA de verdad, tiene que terminar con código 0 y el identificador
       del escenario tiene que APARECER en su salida. «La batería pasa» no basta: una
       batería ajena que pasa sin ejecutar el escenario es el defecto que `T415` ya midió.

Una obligación está IMPLEMENTADA cuando cumple las cinco. Los faltantes se publican
INDIVIDUALMENTE —obligación, requisito y motivo—, nunca como cardinal a secas. El cardinal
se DERIVA de la lista; aquí no hay ninguna cifra escrita a mano.

LO QUE ESTE FICHERO **NO** DEMUESTRA
------------------------------------
  · que el código productivo al que llega sea CORRECTO. `R2` demuestra que existe y que la
    cadena hasta él no es ambigua; que haga lo que la obligación pide lo demuestra `R5` al
    ejecutar la condición de cierre, y sólo en la medida en que la prueba lo compruebe;
  · que la prueba sea CAPAZ DE FALLAR. Eso es `O26` §5.2 y lo mide `O26-SAB`, que es otro
    instrumento y con otro criterio. Una obligación puede salir implementada aquí y quedar
    con propiedades sin sabotaje allí; los dos verdes hacen falta, y ninguno suple al otro;
  · que el universo esté COMPLETO. Que ninguna obligación se caiga de él lo ejerce el
    cliquet del derivador con sus propios sabotajes;
  · nada sobre `O26` §5.3, §5.4 ni §5.5: no los mira y no los nombra en su veredicto.

FALLA CERRADO
-------------
Si una sede no se puede leer, si el derivador no deriva o si el árbol no está en un
repositorio del que leer `HEAD`, sale con código 2 y diagnóstico. No adivina, no aprueba
por ausencia de dato y no reduce el universo en silencio.

USO
    …/comprobar-obligaciones-implementadas.py                 # mide y publica
    …/comprobar-obligaciones-implementadas.py --sin-ejecutar  # sin `R5` (se dice)
    …/comprobar-obligaciones-implementadas.py --solo g.13     # una obligación
    …/comprobar-obligaciones-implementadas.py --autopruebas   # sabotajes del medidor
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
import os
import re
import subprocess
import sys

# La raíz se deriva de `__file__` —tres niveles por encima de `docs/evolucion/verificacion/`—
# y de NADA más. No hay ninguna variable de entorno que cambie QUÉ ÁRBOL se juzga: un
# instrumento que decide si `F6` puede certificarse no puede tener una puerta que lo apunte
# a un árbol amable.
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir, os.pardir, os.pardir))

DERIVADOR = "docs/evolucion/verificacion/derivar-universo-obligatorio.py"
PRUEBAS = "kernel/operativo/pruebas"
RUNTIME = "kernel/operativo/runtime"
VALIDADORES = "kernel/operativo/validadores"

# Raíces de paquete contra las que se resuelve un `import` de una prueba. Son las que las
# propias baterías insertan en `sys.path` (`RAIZ_RUNTIME`) más el directorio de validadores,
# que es de donde salen `huella`, `entorno` y compañía. Se declaran aquí, y la ambigüedad
# —el mismo nombre resolviendo en dos— se publica en vez de resolverse a favor de la
# primera: eso último es justo lo que hace que una trazabilidad deje de ser inequívoca.
RAICES_DE_PAQUETE = (RUNTIME, VALIDADORES, "tooling", "")

# Un fichero es PRUEBA —y por tanto no es código productivo— si vive en un directorio de
# pruebas o si su nombre lo declara. Se mira la RUTA, no el contenido: un `test_x.py` que
# importa a otro `test_y.py` no convierte a ninguno de los dos en producto.
_ES_PRUEBA = re.compile(r"(^|/)(pruebas|tests?)(/|$)|(^|/)(test_[^/]*|escenario_[^/]*)\.py$")


class SedeIlegible(Exception):
    """Una sede que este instrumento necesita y no puede leer, o que dice algo imposible."""


# ---------------------------------------------------------------------------
#  las sedes, leídas
# ---------------------------------------------------------------------------

def _leer(rel):
    ruta = os.path.join(RAIZ, rel)
    try:
        with io.open(ruta, encoding="utf-8") as fh:
            return fh.read()
    except OSError as e:
        raise SedeIlegible("no se puede leer la sede `%s`: %s" % (rel, e))
    except UnicodeDecodeError as e:
        raise SedeIlegible("la sede `%s` no es UTF-8 legible: %s" % (rel, e))


def derivador():
    """Importa el derivador QUE VIVE EN ESTE ÁRBOL y le pide el universo de obligaciones.

    Se IMPORTA, no se copia: dos derivaciones del mismo universo son dos sedes del mismo
    catálogo, y `Q-04` ya castigó esa duplicación. Si el derivador falla cerrado, este
    instrumento falla cerrado con él y dice por qué.
    """
    import importlib.util                                          # noqa: PLC0415
    ruta = os.path.join(RAIZ, DERIVADOR)
    if not os.path.isfile(ruta):
        raise SedeIlegible("falta el derivador del universo: `%s`" % DERIVADOR)
    spec = importlib.util.spec_from_file_location("universo_obligatorio", ruta)
    modulo = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(modulo)
    except Exception as e:                                         # noqa: BLE001
        raise SedeIlegible("el derivador no se puede cargar: %s: %s"
                           % (type(e).__name__, e))
    return modulo


_CLAVE = re.compile(r"^([a-z_]+):\s*(.*)$")


def _campo(bloque, clave):
    r"""El valor de `clave:` en el bloque, o cadena vacía si no lo hay.

    El separador es `[ \t]*` y NO `\s*`, y la diferencia no es de estilo: `\s` incluye el
    salto de línea, de modo que un `validador:` SIN valor se comía el salto y devolvía el
    valor del campo SIGUIENTE. Medido con el sabotaje que retira la prueba de `T172`: la
    obligación se quedaba sin prueba y el aparato publicaba `estado:` como si lo fuera. Un
    campo vacío tiene que leerse como vacío.
    """
    m = re.search(r"^%s:[ \t]*(.+)$" % clave, bloque, re.M)
    return m.group(1).strip().strip('"') if m else ""


def _lista(bloque, clave):
    m = re.search(r"^%s:\s*\n((?:[ \t]+-[ \t].*\n)+)" % clave, bloque, re.M)
    if not m:
        return []
    return [re.sub(r"^\s*-\s*", "", l).strip().strip('"')
            for l in m.group(1).splitlines() if l.strip()]


def escenarios():
    """Todo bloque `ads:escenario` del kernel y de los packs, con TODOS sus campos.

    El derivador lee cuatro campos porque cuatro le bastan. Aquí hacen falta también
    `ejecucion`, `falla_si` y la SEDE —fichero y línea—, porque un faltante que no dice
    dónde se arregla obliga a buscarlo, y buscarlo es lo que hace que no se arregle.
    """
    encontrados = []
    for ambito in ("kernel/operativo", "packs"):
        base = os.path.join(RAIZ, ambito)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
            for nombre in sorted(filenames):
                if not nombre.endswith(".md"):
                    continue
                rel = os.path.relpath(os.path.join(dirpath, nombre), RAIZ)
                texto = _leer(rel)
                for m in re.finditer(r"```yaml ads:escenario\n(.*?)```", texto, re.S):
                    bloque = m.group(1)
                    linea = texto.count("\n", 0, m.start()) + 1
                    cubre = re.search(r"^cubre:\s*\[(.*?)\]", bloque, re.M | re.S)
                    encontrados.append({
                        "id": _campo(bloque, "id"),
                        "nombre": _campo(bloque, "nombre"),
                        "cubre": [c.strip().strip('"') for c in
                                  (cubre.group(1).split(",") if cubre else [])],
                        "validador": _campo(bloque, "validador"),
                        "evidencia": _campo(bloque, "evidencia"),
                        "estado": _campo(bloque, "estado"),
                        "ejecucion": _campo(bloque, "ejecucion"),
                        "falla_si": _lista(bloque, "falla_si"),
                        "entonces": _lista(bloque, "entonces"),
                        "sede": "%s:%d" % (rel, linea),
                    })
    if not encontrados:
        raise SedeIlegible("no hay ni un bloque `ads:escenario` en el árbol: la sede de las "
                           "pruebas no se puede leer, y sin ella no se mide nada")
    return encontrados


# ---------------------------------------------------------------------------
#  `R2` · de la prueba al CÓDIGO PRODUCTIVO
# ---------------------------------------------------------------------------

_IMPORT = re.compile(r"^\s*(?:from\s+([\w.]+)\s+import\b|import\s+([\w.]+))", re.M)
_RUTA_LITERAL = re.compile(r"[\"']((?:kernel|tooling|docs)/[\w./-]+\.py)[\"']")


def _resolver_modulo(punteado):
    """Todas las rutas EXISTENTES a las que un nombre punteado puede referirse.

    Devuelve la lista completa a propósito. Si tiene más de un elemento, la traza no es
    inequívoca y eso se publica: elegir la primera es exactamente cómo una trazabilidad
    ambigua pasa por buena.
    """
    partes = punteado.split(".")
    hallazgos = []
    for base in RAICES_DE_PAQUETE:
        tronco = os.path.join(RAIZ, base, *partes) if base else os.path.join(RAIZ, *partes)
        for candidata in (tronco + ".py", os.path.join(tronco, "__init__.py")):
            if os.path.isfile(candidata):
                hallazgos.append(os.path.relpath(candidata, RAIZ).replace(os.sep, "/"))
    # Un mismo fichero alcanzado por dos raíces distintas —`""` y `tooling`, por ejemplo—
    # no es ambigüedad: es la misma respuesta dos veces.
    return sorted(set(hallazgos))


def codigo_productivo(rel_prueba):
    """`(productivos, ambiguos, motivo)` a partir de la PRUEBA declarada por el escenario.

    La cadena es `prueba → lo que importa` más `prueba → los ficheros `.py` que nombra por
    ruta literal`, que es como una prueba invoca a un punto ejecutable en un subproceso.
    Se descarta todo lo que sea prueba: lo que se busca es el PRODUCTO.
    """
    if not rel_prueba or not os.path.isfile(os.path.join(RAIZ, rel_prueba)):
        return [], [], "la prueba declarada no existe en el árbol"
    texto = _leer(rel_prueba)
    productivos, ambiguos = set(), set()
    for m in _IMPORT.finditer(texto):
        punteado = m.group(1) or m.group(2)
        if punteado.startswith("__"):
            continue
        rutas = [r for r in _resolver_modulo(punteado) if not _ES_PRUEBA.search(r)]
        if len(rutas) > 1:
            ambiguos.add("%s → %s" % (punteado, ", ".join(rutas)))
        elif rutas:
            productivos.add(rutas[0])
    for m in _RUTA_LITERAL.finditer(texto):
        rel = m.group(1)
        if _ES_PRUEBA.search(rel):
            continue
        if os.path.isfile(os.path.join(RAIZ, rel)):
            productivos.add(rel)
    return sorted(productivos), sorted(ambiguos), ""


# ---------------------------------------------------------------------------
#  `R4` · la ligadura al SHA y al TREE
# ---------------------------------------------------------------------------

def _git(*args):
    """Una orden `git` de SÓLO LECTURA sobre el árbol que se juzga.

    Este instrumento no escribe en ningún repositorio: `rev-parse` y `cat-file` no tocan
    refs, índice ni objetos. El identificador de blob del árbol de trabajo NO se pide a
    `git hash-object` —que puede escribir con `-w`— sino que se calcula aquí con la misma
    fórmula de `git`, que es dato público y no hace falta pedírsela a nadie.
    """
    try:
        proc = subprocess.run(["git", "-C", RAIZ] + list(args),
                              capture_output=True, text=True)
    except OSError as e:
        raise SedeIlegible("no se puede ejecutar `git`: %s" % e)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def _blob_de_los_bytes(datos):
    """El identificador que `git` daría a estos bytes: `sha1("blob <n>\\0" + datos)`."""
    cabecera = ("blob %d\x00" % len(datos)).encode("utf-8")
    return hashlib.sha1(cabecera + datos).hexdigest()             # noqa: S324


class Ancla:
    """El commit y el tree contra los que se liga toda la evidencia de esta corrida."""

    def __init__(self):
        rc, self.commit, err = _git("rev-parse", "HEAD")
        if rc != 0:
            raise SedeIlegible(
                "el árbol que se juzga no está en un repositorio con `HEAD` legible, y sin "
                "`HEAD` la condición 4 de `O28` §3 —evidencia ligada al SHA y al tree— no "
                "se puede comprobar. No se aprueba por ausencia de dato: %s" % (err or rc))
        rc, self.tree, err = _git("rev-parse", "HEAD^{tree}")
        if rc != 0:
            raise SedeIlegible("`HEAD` no resuelve a un tree: %s" % (err or rc))
        self._blobs = {}

    def blob_en_head(self, rel):
        if rel not in self._blobs:
            rc, salida, _ = _git("rev-parse", "HEAD:" + rel)
            self._blobs[rel] = salida if rc == 0 else None
        return self._blobs[rel]


# ---------------------------------------------------------------------------
#  `R5` · la CONDICIÓN DE CIERRE, ejecutada
# ---------------------------------------------------------------------------

# Las mismas banderas con las que la evidencia del árbol declara haber corrido cada punto:
# `-I -S -E -X ads_aislado=1`. Se copian del encabezado que `registrar_evidencia.py` escribe
# para que lo que aquí se ejecuta sea lo mismo que allí se publicó, y no una variante.
BANDERAS = ("-I", "-S", "-E", "-X", "ads_aislado=1")
TIEMPO_MAXIMO = 1800


def _entorno_limpio():
    """El entorno del hijo, CONSTRUIDO, no heredado: nada de la familia `PYTHON*`."""
    limpio = {k: v for k, v in os.environ.items() if not k.startswith("PYTHON")}
    limpio["PYTHONDONTWRITEBYTECODE"] = "1"
    return limpio


class Corridas:
    """Ejecuta cada prueba UNA VEZ y recuerda su resultado. Memoriza por orden completa."""

    def __init__(self):
        self._hechas = {}

    def de(self, orden):
        if orden in self._hechas:
            return self._hechas[orden]
        partes = orden.split()
        rel = partes[0]
        ruta = os.path.join(RAIZ, rel)
        if not os.path.isfile(ruta):
            resultado = (None, "", "la prueba declarada no existe: %s" % rel)
        else:
            try:
                proc = subprocess.run(
                    [sys.executable] + list(BANDERAS) + [ruta] + partes[1:],
                    capture_output=True, text=True, cwd=RAIZ, env=_entorno_limpio(),
                    timeout=TIEMPO_MAXIMO)
                resultado = (proc.returncode, proc.stdout + proc.stderr, "")
            except subprocess.TimeoutExpired:
                resultado = (None, "", "la prueba no terminó en %d s" % TIEMPO_MAXIMO)
            except OSError as e:
                resultado = (None, "", "no se pudo ejecutar: %s" % e)
        self._hechas[orden] = resultado
        return resultado


# ---------------------------------------------------------------------------
#  la medición
# ---------------------------------------------------------------------------

REQUISITOS = (
    ("R1", "PERTENENCIA DERIVADA Y PROTEGIDA POR EL CLIQUET"),
    ("R2", "CÓDIGO PRODUCTIVO CON TRAZA INEQUÍVOCA"),
    ("R3", "PRUEBA EJECUTABLE"),
    ("R4", "EVIDENCIA LIGADA AL SHA Y AL TREE"),
    ("R5", "CONDICIÓN DE CIERRE EJECUTADA"),
)


def _invocable(rel):
    texto = _leer(rel)
    return ('if __name__ == "__main__"' in texto
            or "if __name__ == '__main__'" in texto
            or texto.startswith("#!"))


def medir(ejecutar=True, solo=None):
    """Devuelve `(ancla, fichas, protegidas)`. Cada ficha trae los cinco requisitos."""
    deriv = derivador()
    try:
        universo = deriv.universo_de_obligaciones()
        ejercidas = deriv.obligaciones_ejercidas_por_el_corpus()
    except Exception as e:                                         # noqa: BLE001
        raise SedeIlegible("el derivador no deriva el universo: %s: %s"
                           % (type(e).__name__, e))
    if not universo:
        raise SedeIlegible("el universo derivado está VACÍO: sin obligaciones no hay nada "
                           "que medir, y un cero por universo vacío sería el falso verde "
                           "que `P-08` describió")

    todos = escenarios()
    ancla = Ancla()
    corridas = Corridas()
    fichas = {}

    for obligacion in sorted(universo):
        if solo and obligacion != solo:
            continue
        ficha = universo[obligacion]
        mios = [e for e in todos
                if any(deriv._cubre(c, obligacion) for c in e["cubre"])]
        con_prueba = [e for e in mios if e["validador"]]
        salida = {"clase": ficha["clase"], "sede": ficha["sede"],
                  "escenarios": [e["id"] for e in mios], "req": {}}

        # `R1` · pertenencia derivada, y protegida por el cliquet de los manifiestos.
        if obligacion in ejercidas:
            salida["req"]["R1"] = (True, "componente `%s` · sede `%s` · cliquet: sí"
                                   % (ficha["clase"], ficha["sede"]))
        else:
            salida["req"]["R1"] = (False, "deriva del componente `%s` pero NINGÚN manifiesto "
                                          "inmutable la ejerce: sin cliquet, puede caerse "
                                          "del universo sin que nada lo diga" % ficha["clase"])

        # `R2` · código productivo, con traza inequívoca.
        productivos, ambiguos, motivos = set(), [], []
        for esc in con_prueba:
            rel = esc["validador"].split()[0]
            p, a, motivo = codigo_productivo(rel)
            productivos.update(p)
            ambiguos.extend("%s · %s" % (esc["id"], x) for x in a)
            if motivo:
                motivos.append("%s · %s" % (esc["id"], motivo))
        if not con_prueba:
            salida["req"]["R2"] = (False, "ningún escenario la cubre con una prueba "
                                          "declarada: no hay por dónde llegar al código")
        elif ambiguos:
            salida["req"]["R2"] = (False, "la traza hasta el código NO es inequívoca: %s"
                                   % "; ".join(sorted(ambiguos)[:3]))
        elif not productivos:
            salida["req"]["R2"] = (False, "las pruebas que la cubren (%s) no alcanzan ni un "
                                          "fichero de código que no sea prueba%s"
                                   % (", ".join(e["id"] for e in con_prueba),
                                      "; " + "; ".join(motivos) if motivos else ""))
        else:
            salida["req"]["R2"] = (True, "%d ficheros productivos · %s"
                                   % (len(productivos),
                                      ", ".join(sorted(productivos)[:4])
                                      + (" …" if len(productivos) > 4 else "")))
        salida["productivos"] = sorted(productivos)

        # `R3` · prueba ejecutable.
        faltas = []
        for esc in con_prueba:
            rel = esc["validador"].split()[0]
            if not os.path.isfile(os.path.join(RAIZ, rel)):
                faltas.append("%s: la prueba `%s` no existe" % (esc["id"], rel))
            elif not _invocable(rel):
                faltas.append("%s: `%s` no es un punto invocable (ni `__main__` ni shebang)"
                              % (esc["id"], rel))
            elif not esc["ejecucion"]:
                faltas.append("%s: el escenario no declara `ejecucion`" % esc["id"])
        if not con_prueba:
            salida["req"]["R3"] = (False, "ningún escenario la cubre con una prueba "
                                          "declarada")
        elif faltas:
            salida["req"]["R3"] = (False, "; ".join(faltas))
        else:
            salida["req"]["R3"] = (True, "%d pruebas invocables · %s"
                                   % (len({e["validador"] for e in con_prueba}),
                                      ", ".join(sorted(e["id"] for e in con_prueba)[:4])))

        # `R4` · evidencia ligada al SHA y al tree.
        ligadas, sueltas = [], []
        con_evidencia = [e for e in con_prueba if e["evidencia"]]
        for esc in sorted({e["evidencia"] for e in con_evidencia}):
            rel = "%s/%s" % (PRUEBAS, esc)
            ruta = os.path.join(RAIZ, rel)
            if not os.path.isfile(ruta):
                sueltas.append("%s: no está en el árbol" % esc)
                continue
            with io.open(ruta, "rb") as fh:
                mio = _blob_de_los_bytes(fh.read())
            suyo = ancla.blob_en_head(rel)
            if suyo is None:
                sueltas.append("%s: `HEAD` no la tiene confirmada (blob del árbol de "
                               "trabajo %s)" % (esc, mio[:12]))
            elif suyo != mio:
                sueltas.append("%s: el árbol de trabajo (%s) DIFIERE del blob de `HEAD` "
                               "(%s)" % (esc, mio[:12], suyo[:12]))
            else:
                ligadas.append("%s=%s" % (esc, mio[:12]))
        if not con_evidencia:
            salida["req"]["R4"] = (False, "ningún escenario que la cubra declara evidencia")
        elif sueltas:
            salida["req"]["R4"] = (False, "; ".join(sueltas))
        else:
            salida["req"]["R4"] = (True, "%d evidencias ligadas a commit %s · tree %s · %s"
                                   % (len(ligadas), ancla.commit[:12], ancla.tree[:12],
                                      ", ".join(ligadas[:2])))

        # `R5` · la condición de cierre, EJECUTADA.
        if not ejecutar:
            salida["req"]["R5"] = (None, "NO EJECUTADA en esta corrida (`--sin-ejecutar`): "
                                         "este requisito queda SIN COMPROBAR y no se cuenta "
                                         "como cumplido")
        elif not con_prueba:
            salida["req"]["R5"] = (False, "no hay condición de cierre que ejecutar: ningún "
                                          "escenario la cubre con una prueba")
        else:
            malas, buenas = [], []
            for esc in con_prueba:
                rc, texto, error = corridas.de(esc["validador"])
                if error:
                    malas.append("%s: %s" % (esc["id"], error))
                elif rc != 0:
                    # EL MOTIVO, NO SÓLO EL CÓDIGO. Medido el 2026-09-06: `FD-5` figuraba
                    # como «terminó con EXIT=1» y nada más, y hubo que reejecutar su canal
                    # a mano para descubrir que aislado sale VERDE. Un faltante que no dice
                    # por qué obliga a reproducirlo, y reproducirlo es lo que no se hace.
                    # Se publican las últimas líneas NO vacías de la corrida, que es donde
                    # `unittest` y los validadores de este corpus escriben la causa.
                    cola = [l for l in (texto or "").splitlines() if l.strip()][-3:]
                    malas.append("%s: `%s` terminó con EXIT=%s%s"
                                 % (esc["id"], esc["validador"], rc,
                                    (" · última salida: " + " ⏎ ".join(
                                        l.strip()[:120] for l in cola)) if cola else ""))
                elif not re.search(r"(?<![\w-])%s(?![\w-])" % re.escape(esc["id"]), texto):
                    malas.append("%s: `%s` pasó SIN NOMBRARLO en su salida — una batería "
                                 "ajena que pasa no ejecuta la condición de cierre"
                                 % (esc["id"], esc["validador"]))
                else:
                    buenas.append(esc["id"])
            if malas:
                salida["req"]["R5"] = (False, "; ".join(malas))
            else:
                salida["req"]["R5"] = (True, "%d escenarios ejecutados y nombrados en su "
                                             "salida con EXIT=0 · %s"
                                       % (len(buenas), ", ".join(sorted(buenas)[:4])))
        fichas[obligacion] = salida
    if solo and not fichas:
        raise SedeIlegible("`--solo %s` no nombra ninguna obligación del universo" % solo)
    return ancla, fichas


def faltantes(fichas):
    """La lista INDIVIDUAL de faltantes: `(obligación, requisito, motivo)`. El cardinal se
    deriva de aquí y no se escribe en ningún sitio."""
    lista = []
    for obligacion in sorted(fichas):
        for clave, _titulo in REQUISITOS:
            cumple, motivo = fichas[obligacion]["req"][clave]
            if cumple is not True:
                lista.append((obligacion, clave, motivo))
    return lista


# ---------------------------------------------------------------------------
#  publicación
# ---------------------------------------------------------------------------

def publicar(destino, ejecutar=True, solo=None):
    ancla, fichas = medir(ejecutar=ejecutar, solo=solo)
    faltas = faltantes(fichas)
    sin_implementar = sorted({o for o, _r, _m in faltas})

    destino.write("`O26-IMPL` · OBLIGACIONES INTERNAS DE `F6` REALMENTE IMPLEMENTADAS\n")
    destino.write("=" * 78 + "\n\n")
    destino.write("  ANCLA   commit %s · tree %s\n" % (ancla.commit, ancla.tree))
    destino.write("  CRITERIO  `O28` §3, las cinco condiciones, cada una por separado\n")
    for clave, titulo in REQUISITOS:
        destino.write("            %s  %s\n" % (clave, titulo))
    destino.write("\n")

    destino.write("POR OBLIGACIÓN — una fila por obligación, un requisito por columna\n")
    destino.write("-" * 78 + "\n")
    destino.write("  %-14s %-7s %s\n" % ("obligación", "clase", "  ".join(
        c for c, _t in REQUISITOS)))
    for obligacion in sorted(fichas):
        marcas = []
        for clave, _t in REQUISITOS:
            cumple = fichas[obligacion]["req"][clave][0]
            marcas.append("ok" if cumple is True else ("--" if cumple is None else "NO"))
        destino.write("  %-14s %-7s %s\n"
                      % (obligacion, fichas[obligacion]["clase"], "  ".join(marcas)))

    destino.write("\nFALTANTES, UNO A UNO — con obligación, requisito y motivo\n")
    destino.write("-" * 78 + "\n")
    if not faltas:
        destino.write("  ninguno\n")
    for obligacion, clave, motivo in faltas:
        destino.write("  %-14s %-3s %s\n" % (obligacion, clave, motivo))

    destino.write("\n")
    destino.write("  %d obligaciones medidas · %d SIN IMPLEMENTAR · %d faltantes "
                  "individuales\n" % (len(fichas), len(sin_implementar), len(faltas)))
    destino.write("  pendientes de `O26-IMPL`: %s\n"
                  % (", ".join(sin_implementar) if sin_implementar else "∅"))
    veredicto = ("ACREDITADA" if not sin_implementar and ejecutar
                 else "NO ACREDITADA")
    destino.write("  `O26` §5.1 · %s por este instrumento\n" % veredicto)
    destino.write("\nLO QUE ESTE VEREDICTO NO DEMUESTRA\n")
    destino.write("-" * 78 + "\n")
    destino.write("  · no demuestra `O26` §5.2: que las pruebas sean CAPACES DE FALLAR lo\n"
                  "    mide `O26-SAB`, con otro criterio y otro universo. Los dos hacen\n"
                  "    falta y ninguno suple al otro\n")
    destino.write("  · no demuestra que el código productivo alcanzado sea correcto: `R2`\n"
                  "    demuestra que existe y que la cadena hasta él no es ambigua\n")
    destino.write("  · no dice nada de `O26` §5.3, §5.4 ni §5.5\n")
    if not ejecutar:
        destino.write("  · `R5` NO SE HA EJECUTADO en esta corrida: el veredicto es NO\n"
                      "    ACREDITADA por construcción, y no por lo que se haya medido\n")
    return 1 if sin_implementar else 0


# ---------------------------------------------------------------------------
#  autopruebas · un medidor cuyo autotest no puede fallar no mide
# ---------------------------------------------------------------------------
#
#  DECISIÓN · los sabotajes se aplican a una COPIA y se mide con el instrumento QUE VIVE EN
#      LA COPIA. Es la misma decisión del derivador y por el mismo motivo: la alternativa
#      —una variable de entorno que apunte la raíz— sería una puerta abierta en la pieza que
#      decide si `F6` puede certificarse.
#
#  DECISIÓN · la copia ENLAZA `.git` en lugar de copiarlo. `R4` liga la evidencia al `HEAD`
#      del repositorio, así que una copia sin repositorio no puede ejercerlo y el sabotaje
#      de `R4` sería incomprobable. Copiar 50 MB por sabotaje es el precio de no pensarlo;
#      el enlace da el MISMO `HEAD` y este instrumento sólo ejecuta `git rev-parse`, que no
#      escribe. Lo que se pierde —y se dice— es que el sabotaje de `R4` prueba la
#      DIVERGENCIA respecto de `HEAD`, no un `HEAD` distinto.
#
#  DECISIÓN · los sabotajes corren con `--sin-ejecutar` salvo el que ataca `R5`. Ejecutar
#      la regresión entera una vez por sabotaje son horas; el sabotaje de `R5` usa `--solo`
#      y ejerce el requisito de verdad sobre una obligación. Un autotest que tarda tanto que
#      no se corre tampoco mide.

SABOTAJES = []


def _sabotaje(rotulo, espera, argumentos=("--sin-ejecutar",)):
    def envoltorio(fn):
        SABOTAJES.append((rotulo, espera, argumentos, fn))
        return fn
    return envoltorio


def _sustituir_en(destino, rel, viejo, nuevo):
    ruta = os.path.join(destino, rel)
    with io.open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    if viejo not in texto:
        raise AssertionError("el sabotaje no encuentra su ancla en %s: %r"
                             % (rel, viejo[:70]))
    with io.open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto.replace(viejo, nuevo, 1))


def _escenario_de(destino, identificador):
    """`(ruta, texto, bloque)` del escenario `Tnnn` dentro de la copia."""
    base = os.path.join(destino, PRUEBAS)
    for nombre in sorted(os.listdir(base)):
        if not nombre.endswith(".md"):
            continue
        ruta = os.path.join(base, nombre)
        with io.open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        for bloque in re.findall(r"```yaml ads:escenario\n(.*?)```", texto, re.S):
            if _campo(bloque, "id") == identificador:
                return ruta, texto, bloque
    raise AssertionError("no encuentro el escenario %s en la copia" % identificador)


@_sabotaje("la EVIDENCIA de `g.13` se edita: el árbol de trabajo se aparta de `HEAD`",
           "DIFIERE del blob de `HEAD`")
def _s_evidencia_apartada_de_head(destino):
    """`R4` · el defecto de `#3` en pequeño: una evidencia editada que nadie contrasta.

    Se le añade una línea al final. El fichero sigue existiendo y sigue enlazado; lo único
    que cambia es que sus bytes ya no son los que `HEAD` confirmó. Si `R4` sólo mirase la
    PRESENCIA del fichero —que es lo que mide la resta `C`—, esto pasaría por bueno.
    """
    ruta = os.path.join(destino, PRUEBAS, "evidencia", "admision-salida.txt")
    with io.open(ruta, "a", encoding="utf-8") as fh:
        fh.write("\n# 0 infracciones detectadas\n")


@_sabotaje("la evidencia de un escenario se RETIRA del árbol",
           "no está en el árbol")
def _s_evidencia_borrada(destino):
    os.remove(os.path.join(destino, PRUEBAS, "evidencia", "estado-durable-salida.txt"))


def _reescribir_bloque(destino, identificador, viejo, nuevo):
    """Sustituye SÓLO dentro del bloque del escenario pedido, y no en sus vecinos."""
    ruta, texto, _bloque = _escenario_de(destino, identificador)
    cabeza, cola = texto.split("id: %s\n" % identificador, 1)
    corte = cola.find("```")
    bloque, resto = cola[:corte], cola[corte:]
    if viejo not in bloque:
        raise AssertionError("el sabotaje no encuentra %r en el bloque de %s"
                             % (viejo[:60], identificador))
    with io.open(ruta, "w", encoding="utf-8") as fh:
        fh.write(cabeza + "id: %s\n" % identificador
                 + bloque.replace(viejo, nuevo, 1) + resto)


@_sabotaje("`T172` deja de declarar prueba y `A14` se queda sin traza hasta el código",
           "ningún escenario la cubre con una prueba declarada")
def _s_escenario_sin_validador(destino):
    """`R2`/`R3` · lo que la resta `A` mide es que ALGUIEN nombre la obligación en un
    `cubre` con validador. `A14` la cubre `T172` y sólo `T172`: retirándole la prueba, la
    obligación se queda sin ninguna cadena hasta el código, que es el caso que `A` no
    distingue de una obligación implementada."""
    _reescribir_bloque(destino, "T172",
                       "validador: kernel/operativo/runtime/pruebas/test_estado_durable.py",
                       "validador:")


@_sabotaje("la PRUEBA declarada por `T173` deja de existir",
           "no existe")
def _s_prueba_inexistente(destino):
    os.remove(os.path.join(destino, RUNTIME, "pruebas", "test_estado_durable.py"))


@_sabotaje("el código productivo se hace AMBIGUO: un `estado_util.py` homónimo en la raíz "
           "de validadores",
           "NO es inequívoca")
def _s_traza_ambigua(destino):
    """`R2` · «inequívoca» no es un adorno. Con dos ficheros que responden al mismo nombre,
    la cadena `prueba → módulo → código` deja de tener una sola respuesta, y elegir la
    primera es cómo una traza ambigua pasa por buena."""
    origen = os.path.join(destino, RUNTIME, "runtime", "estado_util.py")
    with io.open(origen, encoding="utf-8") as fh:
        texto = fh.read()
    os.makedirs(os.path.join(destino, VALIDADORES, "runtime"), exist_ok=True)
    with io.open(os.path.join(destino, VALIDADORES, "runtime", "__init__.py"), "w",
                 encoding="utf-8") as fh:
        fh.write("")
    with io.open(os.path.join(destino, VALIDADORES, "runtime", "estado_util.py"), "w",
                 encoding="utf-8") as fh:
        fh.write(texto)


@_sabotaje("una obligación se cae del universo derivado — el cliquet tiene que hablar",
           "EL UNIVERSO HA ENCOGIDO")
def _s_universo_encogido(destino):
    """El derivador se importa, no se copia: si su cliquet deja de disparar, este
    instrumento tiene que caer con él y no seguir midiendo un universo mutilado."""
    ruta = os.path.join(destino, "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md")
    with io.open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    linea = [l for l in texto.splitlines() if l.startswith("| `F-07`")][0]
    _sustituir_en(destino, "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md", linea,
                  linea.replace("| **F6** |", "| **F5** |"))


@_sabotaje("`T172` se ata a una batería AJENA que pasa sin nombrarlo — `R5` ejecutado",
           "SIN NOMBRARLO en su salida",
           ("--sin-ejecutar-no", "--solo", "A14"))
def _s_bateria_ajena(destino):
    """`R5` · el defecto que `T415` describe, ejercido contra este medidor.

    `A14` la cubre `T172`, cuya batería es `test_estado_durable.py`. Se le cambia la prueba
    por `test_ciclo.py`, que existe, pasa y NO nombra a `T172`. Un `R5` que se contentara
    con «la batería salió con EXIT=0» daría la condición de cierre por ejecutada sin que
    nadie haya ejecutado nada de `A14`.
    """
    ruta, texto, _bloque = _escenario_de(destino, "T172")
    # Se corta por el `id:` y se sustituye SÓLO en la cola: el mismo `validador:` aparece en
    # otros escenarios del mismo fichero, y cambiarlos todos mediría otra cosa.
    cabeza, cola = texto.split("id: T172", 1)
    nueva = cola.replace(
        "validador: kernel/operativo/runtime/pruebas/test_estado_durable.py",
        "validador: kernel/operativo/runtime/pruebas/test_ciclo.py", 1)
    if nueva == cola:
        raise AssertionError("el sabotaje no encuentra la prueba de `T172`")
    with io.open(ruta, "w", encoding="utf-8") as fh:
        fh.write(cabeza + "id: T172" + nueva)


def _copiar(a_donde):
    """Copia el corpus SIN `__pycache__` y ENLAZA `.git`: ver la decisión de arriba."""
    import shutil                                                  # noqa: PLC0415
    shutil.copytree(RAIZ, a_donde, symlinks=True,
                    ignore=lambda d, n: [x for x in n if x in (".git", "__pycache__",
                                                               ".pytest_cache")])
    real = os.path.join(RAIZ, ".git")
    if os.path.exists(real):
        os.symlink(real, os.path.join(a_donde, ".git"))


def _soltar_el_enlace_al_repositorio(raiz_tmp):
    """Retira los `.git` ENLAZADOS antes de borrar nada.

    `shutil.rmtree` no sigue los enlaces a directorio —los desenlaza— y por tanto el
    repositorio real no corre peligro hoy. Se hace igualmente y de forma explícita: la
    seguridad del árbol que se juzga no puede depender de un detalle de implementación de la
    biblioteca, y este punto crea esos enlaces a sabiendas.
    """
    for entrada in sorted(os.listdir(raiz_tmp)) if os.path.isdir(raiz_tmp) else []:
        enlace = os.path.join(raiz_tmp, entrada, ".git")
        if os.path.islink(enlace):
            os.unlink(enlace)


def _medir_en_la_copia(destino, argumentos):
    """Ejecuta el instrumento QUE VIVE EN LA COPIA y devuelve `(rc, salida)`."""
    ruta = os.path.join(destino, "docs/evolucion/verificacion",
                        os.path.basename(os.path.abspath(__file__)))
    proc = subprocess.run([sys.executable, ruta] + [a for a in argumentos
                                                    if a != "--sin-ejecutar-no"],
                          capture_output=True, text=True, cwd=destino,
                          env=_entorno_limpio(), timeout=TIEMPO_MAXIMO)
    return proc.returncode, proc.stdout + proc.stderr


def autopruebas(destino_stdout):
    """Ejerce CADA requisito con una infracción deliberada. Devuelve 0 si todas se cazan."""
    import shutil                                                  # noqa: PLC0415
    import tempfile                                                # noqa: PLC0415

    destino_stdout.write("META-PRUEBAS DE `O26-IMPL`\n")
    destino_stdout.write("=" * 78 + "\n\n")
    fallidos = 0
    raiz_tmp = tempfile.mkdtemp(prefix="ads-o26-impl-")
    try:
        # CONTROL POSITIVO. Un control que no puede aprobar no vale: sobre la copia intacta
        # el instrumento tiene que MEDIR y publicar su tabla. Si no publica, ningún rojo
        # posterior significa nada, porque no se sabría si es el sabotaje o el aparato.
        limpio = os.path.join(raiz_tmp, "control")
        _copiar(limpio)
        rc, texto = _medir_en_la_copia(limpio, ("--sin-ejecutar",))
        bien = "FALTANTES, UNO A UNO" in texto and "obligaciones medidas" in texto
        destino_stdout.write("  %-4s CONTROL POSITIVO · la copia intacta mide y publica\n"
                             % ("ok" if bien else "FALLA"))
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
            if espera in texto:
                resultado = "ok"
            elif "Traceback (most recent call last)" in texto:
                # Una traza NO es una detección: es el aparato reventando. `V6-03` manda no
                # confundir las dos cosas, y aquí se separan.
                resultado = "TRAZA"
            else:
                resultado = "MOTIVO EQUIVOCADO" if rc else "NO DETECTADA"
            if resultado != "ok":
                fallidos += 1
            destino_stdout.write("  %-4s %s\n" % (resultado, rotulo))
            destino_stdout.write("       espera «%s»\n" % espera)
            if resultado != "ok":
                destino_stdout.write("       rc=%s · %s\n" % (rc, texto[-500:]))
    finally:
        _soltar_el_enlace_al_repositorio(raiz_tmp)
        shutil.rmtree(raiz_tmp, ignore_errors=True)
    destino_stdout.write("\n  %d sabotajes · %d sin detectar\n"
                         % (len(SABOTAJES), fallidos))
    return 1 if fallidos else 0


def main():
    ap = argparse.ArgumentParser(
        description="`O26-IMPL` · las cinco condiciones de `O28` §3 sobre cada obligación")
    ap.add_argument("--autopruebas", action="store_true",
                    help="ejerce cada requisito con un sabotaje")
    ap.add_argument("--sin-ejecutar", action="store_true",
                    help="no ejecuta `R5`; el veredicto lo dice y no acredita")
    ap.add_argument("--solo", default=None, help="mide una sola obligación")
    args = ap.parse_args()
    if args.autopruebas:
        return autopruebas(sys.stdout)
    try:
        return publicar(sys.stdout, ejecutar=not args.sin_ejecutar, solo=args.solo)
    except SedeIlegible as e:
        sys.stderr.write("FALLA CERRADO · %s\n" % e)
        return 2


if __name__ == "__main__":
    sys.exit(main())
