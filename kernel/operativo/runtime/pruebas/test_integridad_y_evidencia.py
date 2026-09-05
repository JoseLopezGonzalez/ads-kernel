#!/usr/bin/env python3
"""test_integridad_y_evidencia — `T306` a `T309`. Los cuatro hallazgos TRANSVERSALES.

    `T306`  `E-10`  PROCEDENCIA con `--repo`: módulos del APARATO, `PYTHONPATH` envenenado
                    que no entra, dos repositorios que no se contaminan, y la procedencia
                    PUBLICADA en la salida
    `T307`  `E-14`  EVIDENCIA: `OK` deja de equivaler a `OK (skipped=N)`; el resultado se
                    comprueba ENTERO —casos, fallos, errores y saltos—; y manipular el
                    contador INVALIDA la evidencia
    `T308`  `E-15`  CLI: ningún error TIPADO sale de `main()` como traza; código de salida
                    estable por clase de fallo; `stderr` útil y sin rutas del anfitrión
    `T309`  `E-16`  CONTENCIÓN CABLEADA en el camino PRODUCTIVO, con hijo, nieto y BISNIETO
            `E-18`  y el ALCANCE EXACTO de este anfitrión, medido y publicado

POR QUÉ ESTA BATERÍA EXISTE Y NO SE REPARTE EN LAS DEMÁS. Los cuatro hallazgos cruzan los
paquetes: `E-10` y `E-15` son de los CINCO puntos ejecutables a la vez, `E-14` es del
validador de evidencia, que vive fuera del runtime, y `E-16` es del adaptador, del runtime,
del ciclo y del paquete de contención en la misma prueba. Meter cada uno en la batería de su
paquete habría partido la propiedad en trozos que por separado no demuestran nada.

**LO QUE NO SE SIMULA.** Los procesos son procesos (`subprocess`, sesión nueva y entorno
construido entero), los repositorios son repositorios Git de verdad, y la contención se mide
con los PID reales del anfitrión sobre tres generaciones que hacen `setsid`.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, `HALLAZGO 3` del revisor 3 en el gate del
#  2026-09-05: veintiuna baterías de `runtime/pruebas/` y `tooling/tests/` no llevaban el
#  prólogo `E-10`, y el inventario de `T330` las eximía POR SU ZONA con `motivo: "bateria"`
#  —que es la lista escrita a mano que `ADJ-B2` prohibió, sólo que escrita por directorios—.
#  Y el canal que PRODUCE la evidencia, `registrar_evidencia.py` L212, lanzaba a sus hijos
#  con `subprocess.run` SIN `env=`: el veneno del padre llegaba entero a cada batería.
#
#  Lo que esto significa aquí: la salida de esta batería se PUBLICA como evidencia y
#  sostiene el estado de escenarios. Un `hashlib` o un `json` sustituidos por quien la corre
#  deciden qué dice esa evidencia. Se aplica el remedio ENTERO que el revisor adjudicó: el
#  prólogo entra en la batería —lo que cierra también la ejecución suelta— y el runner
#  sanea el entorno de sus hijos y lo publica en la cabecera de cada evidencia.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      La misma disciplina que `E-10` sigue debajo y que `T330` comprueba: lo que protege
#      está fijado y es idéntico en todos los puntos —`T380` lo exige con su digest—, y lo
#      que se lee dice qué se midió en ESTA sede. Un recital común mentiría en la mitad de
#      las sedes; un mecanismo por sede derivaría, y el que derive de menos es el que nadie
#      mira.
#
#  DECISIÓN · la guarda va ANTES del prólogo `E-10`, y no lo sustituye
#      Alternativas: (a) sustituir `E-10` por la guarda; (b) dejar `E-10` y añadir la
#      guarda encima.
#      Se elige (b). Cierran cosas distintas: `E-10` retira del `sys.path` lo que mete el
#      lanzador —y sigue haciendo falta cuando el punto se IMPORTA, donde la guarda no
#      reejecuta—; `G-03` impide que `sitecustomize` llegue siquiera a ejecutarse. Quitar
#      `E-10` reabriría la contaminación de la ruta en el caso importado.
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

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, `HALLAZGO 3` del gate del 2026-09-05: esta batería
#  no llevaba el prólogo, y el inventario de `T330` la eximía por vivir en una zona de
#  pruebas. Su salida se PUBLICA como evidencia; un `json.py` o un `hashlib.py` homónimos en
#  el `PYTHONPATH` de quien la corre deciden qué dice esa evidencia, que es exactamente el
#  daño que `H-01` midió sobre `huella.py`. La deuda ya no es de zona: la exclusión
#  `motivo: "bateria"` se ha RETIRADO del inventario y esta batería es un punto ejecutable
#  como cualquier otro.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      Es la decisión de `ADJ-B2`, sin cambio: `T330` exige que el mecanismo sea IDÉNTICO en
#      todos los puntos ejecutables, y cada sede escribe qué se midió en ella.
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

import ast
import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

RAIZ_RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ_OPERATIVO = os.path.dirname(RAIZ_RUNTIME)
RAIZ_REPO = os.path.dirname(os.path.dirname(RAIZ_OPERATIVO))
VALIDADORES = os.path.join(RAIZ_OPERATIVO, "validadores")

sys.path.insert(0, RAIZ_RUNTIME)

import contencion                                                    # noqa: E402
from admision import matriz                                          # noqa: E402
from contencion import deteccion                                     # noqa: E402
from gobierno.git import CanalGit                                    # noqa: E402

# ===========================================================================
#  `ADJ-B2` · `H-03` · EL INVENTARIO SE DERIVA DEL ÁRBOL ENTERO, Y TODO `.py` SE CLASIFICA
# ===========================================================================
#  HECHO REPRODUCIDO ANTES DE CORREGIR — DOS VECES, Y LA SEGUNDA ES LA GRAVE.
#
#  PRIMERA (`ADJ-B2`, gate del 2026-09-04): aquí había una TUPLA ESCRITA A MANO con los
#  cinco `ads_*.py`, y por eso `T306` cubría cinco puntos ejecutables «y ninguno más». Los
#  cuatro de `kernel/operativo/raiz-externa/` quedaban fuera, y en ellos `E-10` seguía vivo:
#  con un `json.py` homónimo en `PYTHONPATH`, `verificador.py capacidades` publicaba `{}`
#  con código 0 y `instalar.py` escribía un manifiesto de TRES bytes sobre 41 ficheros.
#
#  SEGUNDA (`H-03` de la auditoría independiente del 2026-09-04): el remedio adjudicado
#  decía «INVENTARIO MECÁNICO y no por lista», y lo que se hizo fue sustituir una tupla de
#  FICHEROS escrita a mano por una tupla de ZONAS escrita a mano —`runtime/` y
#  `raiz-externa/`, primer nivel—. El auditor inventarió el árbol con `ast` y midió:
#
#      144 ficheros `.py` · 140 con línea de intérprete o bloque `__main__`
#      `T306` juzgaba 9
#      fuera quedaban los 15 `comprobar_*.py`, `huella.py`, `registrar_evidencia.py`,
#      `registro_pruebas.py`, `tooling/workspace.py`, los 3 de `docs/evolucion/
#      verificacion/`, `docs/canonico/validar-fuentes-canonicas.py` y `docs/f5/validar-f5.py`
#
#  Y en esa zona invisible el defecto estaba VIVO, con consecuencia medida (`H-01`): un
#  `hashlib.py` homónimo en `PYTHONPATH` hacía que `validadores/huella.py` publicara la
#  huella ESPERADA sobre un árbol MUTADO y que `T150` —la prueba que dice «la huella detecta
#  su edición»— saliera SUPERADA con `EXIT=0`. Una zona nueva volvía a quedar fuera sin que
#  nadie se enterara, que es literalmente el modo de fallo que `ADJ-B2` describe.
#
#  DECISIÓN · se recorre el ÁRBOL ENTERO y NINGÚN `.py` queda sin clasificar
#      Alternativas: (a) ampliar la tupla de zonas con las que faltan; (b) recorrer el árbol
#      entero y exigir el prólogo a todo lo que tenga línea de intérprete; (c) recorrer el
#      árbol entero, clasificar CADA `.py` en exactamente UNA clase, exigir el prólogo a la
#      clase de los puntos ejecutables y DECLARAR CON MOTIVO —y comprobar— cada exclusión.
#      Se elige (c). Con (a) se repara la instancia y se deja la clase: la tupla siguiente se
#      queda corta el día que aparezca la zona siguiente, que es el defecto que se está
#      corrigiendo por segunda vez. Con (b) el inventario da rojo en un centenar de módulos
#      de biblioteca del runtime que llevan línea de intérprete RESIDUAL sin ser ejecutables
#      —un guardián que da cien rojos falsos se apaga—. Con (c) un fichero nuevo no puede
#      ser INVISIBLE: o es punto ejecutable y se le exige el mecanismo, o cae en una clase
#      de exclusión cuyo predicado se comprueba. Es la forma de `AMBITO_VIVO` en
#      `comprobar_recuentos.py` tras `ADJ-M5`: cada prefijo motivado, y nada sin clasificar.
#
#  DECISIÓN · el criterio de «punto ejecutable» es SER INVOCABLE, y admite las DOS formas
#      La equivalencia anterior era «`#!` ⟺ bloque `__main__` ⟺ prólogo `E-10`», y sobre las
#      dos zonas de origen era cierta porque las nueve piezas usan el idiom `main()`. Sobre
#      el árbol entero es FALSA, y se midió: `docs/evolucion/verificacion/
#      comprobar-correccion-gate-de-cierre.py` es un guion de nivel superior que termina en
#      `sys.exit(_informe())` y NO define `__main__`. Exigirle el bloque sería exigirle que
#      se reescriba para satisfacer una prueba. La equivalencia que se conserva —y que se
#      comprueba en los dos sentidos— es:
#
#          lleva `#!`   ⟺   es INVOCABLE   ⟺   lleva el MECANISMO `E-10`
#
#      donde INVOCABLE = define `if __name__ == "__main__":` **o** ejecuta `sys.exit(…)` /
#      `raise SystemExit(…)` en el nivel superior del módulo. Las dos formas se detectan
#      PARSEANDO, no buscando texto: el texto aparece en comentarios que hablan de esta
#      misma regla, y en las cadenas de mutación de `validadores/negativos_runtime.py`.
#
#  DECISIÓN · lo que se exige idéntico byte a byte es el MECANISMO, y no el recital
#      Alternativas: (a) exigir el prólogo entero idéntico, recital incluido; (b) exigir
#      idéntico sólo el mecanismo.
#      Se elige (b). Con (a) o el recital miente en veinte sedes —el hecho reproducido en
#      `huella.py` no es el reproducido en `ads_admision.py`— o no se puede escribir dónde
#      se midió cada cosa, que es la mitad del valor de estos bloques. Con (b) lo que
#      protege está fijado —1 869 bytes, digest `aa219465a6dd6a04`, comprobado aquí sobre
#      todos los puntos a la vez— y lo que se lee es propio de cada sede. Una divergencia de
#      un solo byte en el mecanismo pone esta prueba en rojo y nombra los grupos.
DIRECTORIOS_QUE_NO_SON_CORPUS = ("__pycache__", ".git", ".pytest_cache")

# Las zonas de baterías NO se escriben: se DERIVAN. Un directorio es zona de baterías si se
# llama `pruebas` o `tests` y contiene de verdad baterías. Se comprueba en `T330b`.
NOMBRES_DE_ZONA_DE_PRUEBAS = ("pruebas", "tests")
PREFIJOS_DE_BATERIA = ("test_", "escenario_", "catalogo_")

# El comienzo y el final del MECANISMO, que es lo que se exige idéntico. El recital que va
# encima queda fuera a propósito (ver la DECISIÓN de arriba).
_INICIO_DEL_MECANISMO = "import sys as _sys\nimport os as _os\n"
_FINAL_DEL_MECANISMO = "    raise SystemExit(5)\n"

# Las TRES clases de exclusión, cada una con su motivo y con el predicado que `T330b`
# comprueba sobre el disco. Que un motivo esté escrito no lo hace cierto: cada uno se
# verifica, y un `.py` que no case con ninguna clase pone la prueba en rojo.
#  `D-01` · LA EXCLUSIÓN POR ZONA `bateria` SE HA RETIRADO, Y NO VUELVE
#      HECHO REPRODUCIDO, `HALLAZGO 3` del revisor 3 en el gate del 2026-09-05: veintiún
#      ficheros de `runtime/pruebas/` no llevaban la purga, y este inventario los eximía por
#      su ZONA con `motivo: "bateria"`. La deuda estaba declarada —lo que es mejor que
#      callarla— pero eximir por vivir en un directorio es EXACTAMENTE la lista escrita a
#      mano que `ADJ-B2` prohibió, sólo que escrita por directorios en vez de por ficheros:
#      una batería nueva quedaba fuera sin que nadie lo decidiera.
#
#      DECISIÓN · se paga la deuda entera y se retira la clase
#          Alternativas: (a) conservar la exclusión y estrechar el cliquet; (b) sanear el
#          entorno de los hijos en el runner, que cierra las 21 de una vez; (c) las dos: el
#          prólogo y la guarda entran en las baterías Y el runner sanea y lo publica.
#          Se elige (c), que es lo que el revisor adjudicó con estas palabras: «lo segundo
#          cierra las 21 de una vez y es más barato; lo primero cierra también la ejecución
#          suelta». Con (a) la deuda sobrevive a su propio pago. Con (b) una batería
#          ejecutada A MANO —que es como se ejecutan mientras se escriben— sigue sin
#          protección. Con (c) no queda ninguna zona exenta: las clases de exclusión que
#          quedan son propiedades del fichero —no ser invocable—, no de su domicilio.
MOTIVOS_DE_EXCLUSION = {
    "biblioteca-de-paquete": (
        "no es invocable y vive en un PAQUETE importable —su directorio tiene "
        "`__init__.py`—: se importa, no se ejecuta. Su línea de intérprete es RESIDUAL, y "
        "el recuento de las que quedan se publica en el diagnóstico de `T330b`"),
    "biblioteca-suelta": (
        "no es invocable y no vive en un paquete: entonces tampoco puede llevar línea de "
        "intérprete, porque una línea de intérprete presenta un módulo como ejecutable. Es "
        "la regla que `ADJ-B2` ya aplicó a `errores.py`, `firma.py`, `atestacion.py` y "
        "`aislamiento.py` de la raíz externa, y que esta pasada aplica a los tres "
        "`negativos_*.py` de biblioteca de `validadores/`"),
}


def _arbol_de(fuente):
    try:
        return ast.parse(fuente)
    except SyntaxError:
        return None


def _tiene_bloque_main(fuente):
    """`True` si el módulo define `if __name__ == "__main__":` en su nivel superior.

    Se PARSEA y no se busca el texto: el texto aparece en comentarios que hablan de esta
    misma regla, y una derivación que se dejara engañar por un comentario no sería una
    derivación.
    """
    arbol = _arbol_de(fuente)
    if arbol is None:
        return False
    for nodo in arbol.body:
        if not isinstance(nodo, ast.If):
            continue
        for comparacion in ast.walk(nodo.test):
            if isinstance(comparacion, ast.Compare) \
                    and isinstance(comparacion.left, ast.Name) \
                    and comparacion.left.id == "__name__" \
                    and any(isinstance(c, ast.Constant) and c.value == "__main__"
                            for c in comparacion.comparators):
                return True
    return False


# `G-03`, HALLAZGO 5 DEL AUDITOR INDEPENDIENTE · LA CARGA SE INVIERTE
#
#     HECHO REPRODUCIDO. `invocable` era `main or salida_de_nivel_superior`, y con eso el
#     auditor coló en el árbol un fichero que se ejecuta y se envenena:
#
#         # tooling/punto_colado.py — sin shebang, sin `main`, sin `sys.exit`
#         import hashlib
#         def _trabajo():
#             print("huella del corpus:", hashlib.sha256(b"corpus").hexdigest()[:16])
#         _trabajo()
#
#         $ python3.12 …/punto_colado.py                       2d711642b726b044
#         $ PYTHONPATH=…/veneno python3.12 …/punto_colado.py   0000000000000000
#         $ cat …/TESTIGO                                      llego
#
#     El inventario lo clasificó `biblioteca-suelta`, `T380` siguió publicando «56 de 56» y
#     nada se puso rojo. La señal `interprete` se MEDÍA y no se usaba para decidir nada.
#
#     Y la clase ya estaba poblada en el árbol real: de las nueve `biblioteca-suelta`, DOS
#     tienen llamada en el nivel superior —`validadores/negativos_contratos19.py` y
#     `validadores/negativos_runtime.py`—, una con guarda y otra sin ella, y esa asimetría
#     no la medía nadie porque `T381` sólo recorre `puntos`.
#
# DECISIÓN · «ejecutable» deja de significar «termina el proceso» y pasa a significar
# «HACE ALGO al cargarse»
#     Alternativas: (a) añadir la señal `interprete` a `invocable`; (b) exigir la guarda a
#     todo `.py` que no sea demostrablemente INERTE al importarse.
#     Se elige (b). Con (a) el fichero del auditor —que no tiene shebang— seguiría fuera, y
#     la frontera seguiría dependiendo de cómo escribió el fichero su autor en vez de lo que
#     el fichero hace. Con (b) la frontera la pone una propiedad del código: un módulo cuyo
#     nivel superior sólo declara —importa, define, asigna constantes— no ejecuta nada al
#     cargarse y no puede ser el punto por el que entre un `sitecustomize`; cualquier otro
#     sí, y por tanto la guarda le toca.
#
#     LO QUE ESTA REGLA CUENTA COMO INERTE, dicho entero: `import`, `def`, `class`, `if`
#     de guardia, `try` de importación, asignaciones, docstrings, `pass`, y DOS familias de
#     llamada, cada una con su motivo:
#
#       · las del PRÓLOGO de aislamiento y de purga, porque son precisamente el mecanismo
#         que se está exigiendo y contarlas como defecto sería circular;
#       · las que sólo tocan `sys.path`, porque son FONTANERÍA DE IMPORTACIÓN: declaran de
#         dónde se importa y no hacen trabajo. Se midió: `python3.12 runtime/admision/
#         errores.py` no imprime nada, no escribe nada y sale con 0. Un módulo que sólo
#         ajusta la ruta no es un punto por el que entre un `sitecustomize`; y quien lo
#         importa sí lo es, y lleva la guarda.
#
#     Todo lo demás en el nivel superior —una llamada suelta, un `for`, un `while`, un
#     `with`— es TRABAJO, y trabajo al importar es lo que convierte a un fichero en un punto
#     ejecutable, lo declare su autor o no. Eso mete en el inventario a
#     `negativos_contratos19.py` y `negativos_runtime.py`, que registran su catálogo con
#     `CATALOGO.extend(...)` en el nivel superior: el auditor señaló que uno llevaba la
#     guarda y el otro no, y que esa asimetría no la medía nadie porque los dos estaban
#     fuera. Ahora los dos están dentro y los dos la llevan.
_NOMBRES_DEL_PROLOGO = ("_aislamiento_g03", "_sys_g03", "_purgar_la_ruta_de_importacion",
                        "_sys", "_os", "exigir", "print_function")


def _es_fontaneria_de_ruta(nodo):
    """¿La llamada sólo toca `sys.path`? Declara de dónde se importa; no hace trabajo."""
    objetivo = nodo.func
    if not isinstance(objetivo, ast.Attribute):
        return False
    duenno = objetivo.value
    return (isinstance(duenno, ast.Attribute) and duenno.attr == "path"
            and isinstance(duenno.value, ast.Name)
            and duenno.value.id in ("sys", "_sys", "_sys_g03"))


def _llamada_del_prologo(nodo):
    """¿Esa llamada del nivel superior es del prólogo de `E-10`/`G-03` y no trabajo propio?"""
    if _es_fontaneria_de_ruta(nodo):
        return True
    objetivo = nodo.func
    while isinstance(objetivo, ast.Attribute):
        objetivo = objetivo.value
    return isinstance(objetivo, ast.Name) and objetivo.id in _NOMBRES_DEL_PROLOGO


def _trabaja_al_importarse(fuente):
    """`True` si el nivel superior del módulo EJECUTA algo, y no sólo declara."""
    arbol = _arbol_de(fuente)
    if arbol is None:
        return False
    for nodo in arbol.body:
        if isinstance(nodo, (ast.Import, ast.ImportFrom, ast.FunctionDef,
                             ast.AsyncFunctionDef, ast.ClassDef, ast.Assign,
                             ast.AnnAssign, ast.AugAssign, ast.Pass, ast.If, ast.Try,
                             ast.Delete, ast.Global, ast.Nonlocal)):
            # `If` y `Try` son las dos formas en que el corpus escribe guardias de
            # importación y el `if __name__` final; el `main` lo detecta su propia señal.
            continue
        if isinstance(nodo, ast.Expr):
            if isinstance(nodo.value, (ast.Constant, ast.JoinedStr)):
                continue                      # docstring o cadena suelta: no hace nada
            if isinstance(nodo.value, ast.Call) and _llamada_del_prologo(nodo.value):
                continue                      # el propio mecanismo que se está exigiendo
        return True
    return False


def _sale_en_el_nivel_superior(fuente):
    """`True` si el módulo TERMINA el proceso desde su nivel superior.

    La segunda forma de punto ejecutable que el árbol usa de verdad: un guion sin `main()`
    que acaba en `sys.exit(...)` o `raise SystemExit(...)`. Se excluye el `raise
    SystemExit(5)` del propio mecanismo `E-10`, que está DENTRO de un `if` de guardia y no
    es la forma del guion: se distingue porque aquí sólo se miran los nodos del nivel
    superior, y ése cuelga de un `ast.If`.
    """
    arbol = _arbol_de(fuente)
    if arbol is None:
        return False
    for nodo in arbol.body:
        if isinstance(nodo, ast.Expr) and isinstance(nodo.value, ast.Call):
            objetivo = nodo.value.func
            if isinstance(objetivo, ast.Attribute) and objetivo.attr == "exit":
                return True
        if isinstance(nodo, ast.Raise):
            excepcion = nodo.exc
            if isinstance(excepcion, ast.Call):
                excepcion = excepcion.func
            if isinstance(excepcion, ast.Name) and excepcion.id == "SystemExit":
                return True
    return False


def _llama_a_la_purga(fuente):
    """`True` si el módulo EJECUTA la purga en su nivel superior. Se parsea, no se busca.

    `validadores/negativos_runtime.py` contiene el nombre `_purgar_la_ruta_de_importacion`
    DENTRO de las cadenas de una mutación que lo retira del verificador. Un inventario que
    buscara la subcadena daría por purgado un módulo de biblioteca que no purga nada.
    """
    arbol = _arbol_de(fuente)
    if arbol is None:
        return False
    for nodo in arbol.body:
        if not isinstance(nodo, ast.Assign) or not isinstance(nodo.value, ast.Call):
            continue
        objetivo = nodo.value.func
        if isinstance(objetivo, ast.Name) \
                and objetivo.id == "_purgar_la_ruta_de_importacion" \
                and any(isinstance(t, ast.Name) and t.id == "RETIRADAS_DE_LA_RUTA"
                        for t in nodo.targets):
            return True
    return False


# El comienzo y el final del MECANISMO de la guarda `G-03`, que es lo que se exige idéntico
# en todos los puntos. Igual que con `E-10`: el recital de encima es de cada sede.
_INICIO_DE_LA_GUARDA = "import os as _os_g03\nimport sys as _sys_g03\n"
_FINAL_DE_LA_GUARDA = "    _sys_g03.path.insert(0, _G03_PROPIA)\n"


def _llama_a_la_guarda(fuente):
    """`True` si el módulo EXIGE el aislamiento en su nivel superior. Se parsea, no se busca.

    El mismo cuidado que con `_llama_a_la_purga`, y por la misma razón medida: el nombre de
    la guarda aparece dentro de las cadenas de las mutaciones que la retiran, y un
    inventario que buscara la subcadena daría por guardado justo al fichero saboteado.
    """
    arbol = _arbol_de(fuente)
    if arbol is None:
        return False
    for nodo in arbol.body:
        if not isinstance(nodo, ast.Assign) or not isinstance(nodo.value, ast.Call):
            continue
        objetivo = nodo.value.func
        if isinstance(objetivo, ast.Attribute) and objetivo.attr == "exigir" \
                and isinstance(objetivo.value, ast.Name) \
                and objetivo.value.id == "_aislamiento_g03" \
                and any(isinstance(t, ast.Name) and t.id == "AISLAMIENTO"
                        for t in nodo.targets):
            return True
    return False


def mecanismo_de_la_guarda(fuente):
    """El MECANISMO `G-03` de un punto ejecutable, o `None`. El recital NO entra."""
    inicio = fuente.find(_INICIO_DE_LA_GUARDA)
    if inicio < 0:
        return None
    final = fuente.find(_FINAL_DE_LA_GUARDA, inicio)
    if final < 0:
        return None
    return fuente[inicio:final + len(_FINAL_DE_LA_GUARDA)]


def mecanismo_de_la_purga(fuente):
    """El MECANISMO `E-10` de un punto ejecutable, o `None`. El recital NO entra."""
    inicio = fuente.find(_INICIO_DEL_MECANISMO)
    if inicio < 0:
        return None
    final = fuente.find(_FINAL_DEL_MECANISMO, inicio)
    if final < 0:
        return None
    return fuente[inicio:final + len(_FINAL_DEL_MECANISMO)]


def zonas_de_baterias(raiz):
    """Las zonas de baterías, DERIVADAS del disco. Ni una escrita."""
    zonas = set()
    for dirpath, dirnames, filenames in os.walk(raiz):
        dirnames[:] = sorted(d for d in dirnames if d not in DIRECTORIOS_QUE_NO_SON_CORPUS)
        if os.path.basename(dirpath) in NOMBRES_DE_ZONA_DE_PRUEBAS and any(
                n.endswith(".py") and n.startswith(PREFIJOS_DE_BATERIA) for n in filenames):
            zonas.add(os.path.realpath(dirpath))
    return zonas


def inventariar_el_arbol(raiz=None):
    """`(puntos, excluidos)` sobre TODO `.py` del árbol. Nada queda sin clasificar.

    `puntos` son los PUNTOS EJECUTABLES: `{ruta relativa: {señales medidas}}`.
    `excluidos` son los demás, con la CLASE por la que quedan fuera: `{ruta: señales}` con
    la clave `motivo` puesta a una de las de `MOTIVOS_DE_EXCLUSION`.
    """
    base = os.path.realpath(raiz or RAIZ_REPO)
    puntos, excluidos = {}, {}
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if d not in DIRECTORIOS_QUE_NO_SON_CORPUS)
        es_paquete = os.path.isfile(os.path.join(dirpath, "__init__.py"))
        for nombre in sorted(filenames):
            if not nombre.endswith(".py"):
                continue
            completa = os.path.join(dirpath, nombre)
            if not os.path.isfile(completa):
                continue
            with open(completa, "rb") as manejador:
                crudo = manejador.read()
            fuente = crudo.decode("utf-8", "replace")
            senales = {
                "ruta": os.path.relpath(completa, base).replace(os.sep, "/"),
                "zona": os.path.relpath(dirpath, base).replace(os.sep, "/"),
                "completa": completa,
                "interprete": crudo.startswith(b"#!"),
                "main": _tiene_bloque_main(fuente),
                "salida_de_nivel_superior": _sale_en_el_nivel_superior(fuente),
                "paquete": es_paquete,
                "purga": _llama_a_la_purga(fuente),
                "mecanismo": mecanismo_de_la_purga(fuente),
                "guarda": _llama_a_la_guarda(fuente),
                "mecanismo_g03": mecanismo_de_la_guarda(fuente),
                "fuente": fuente,
            }
            senales["trabaja_al_importarse"] = _trabaja_al_importarse(fuente)
            senales["invocable"] = (senales["main"] or senales["salida_de_nivel_superior"]
                                    or senales["trabaja_al_importarse"])
            if senales["invocable"]:
                puntos[senales["ruta"]] = senales
            elif es_paquete:
                senales["motivo"] = "biblioteca-de-paquete"
                excluidos[senales["ruta"]] = senales
            else:
                senales["motivo"] = "biblioteca-suelta"
                excluidos[senales["ruta"]] = senales
    return puntos, excluidos


# El alcance de `T306`, DERIVADO del árbol entero. La tupla de FICHEROS escrita a mano dejó
# fuera a la raíz externa; la tupla de ZONAS que la sustituyó dejó fuera a `validadores/`,
# a `tooling/` y a `docs/`, que es donde `H-01` encontró el defecto vivo.
INVENTARIO, EXCLUIDOS_DEL_INVENTARIO = inventariar_el_arbol()
EJECUTABLES = tuple(sorted(INVENTARIO))

# `T308` mide otra cosa que `T306`, y por eso su alcance es OTRO, derivado igual y con la
# diferencia declarada. `T308` contrasta la TABLA DE CÓDIGOS DE SALIDA del kernel: 0 éxito,
# 1 fallo tipado, 2 uso, 3 adaptador, 4 contención, 5 procedencia. Sólo los cinco `ads_*.py`
# publican esa tabla, y las demás zonas NO deben publicarla: `O25` §2 le da a
# `anfitrion_firmante.py` un 3 —«no hay proveedor válido»— y un 4 —«este anfitrión SÓLO
# firma»— con significado propio, y los validadores documentales tienen el convenio de
# `comprobar_contratos` —0 superada, 1 fallida, 2 uso—, que es otro contrato. Meterlos a
# todos en la misma tabla borraría distinciones que los contratos hacen a propósito. El
# estrechamiento no se escribe fichero a fichero: se declara POR ZONA con su motivo, y
# `T308` comprueba que ninguna zona excluida deja de estar declarada.
ZONA_DEL_KERNEL = "kernel/operativo/runtime"
MOTIVO_DE_LA_EXCLUSION_DE_T308 = {
    "kernel/operativo/raiz-externa":
        "`O25` §2 le da a esta zona códigos 3 y 4 con significado propio",
    "kernel/operativo/validadores":
        "convenio documental de `comprobar_contratos`: 0 superada · 1 fallida · 2 uso",
    "tooling":
        "convenio del arranque: 0 · 1 error de materialización · 2 uso",
    "docs/canonico":
        "validador documental de una sede: 0 · 1 hallazgos · 2 uso",
    "docs/f5":
        "validador documental de una fase: 0 · 1 hallazgos · 2 uso",
    "docs/evolucion/verificacion":
        "instrumental del GATE, que no es del kernel y cuyo 0/1 es el del gate",
    # `D-01` · las dos zonas de baterías entran en el inventario desde que se retiró la
    # exención por domicilio, y por eso su motivo hay que ESCRIBIRLO aquí: son puntos
    # ejecutables, pero su convenio de salida es el de `unittest` —0 todo bien, 1 hubo
    # fallos— y no la tabla de seis códigos del kernel. Meterlas en `T308` obligaría a cada
    # batería a publicar una tabla que no usa.
    "kernel/operativo/runtime/pruebas":
        "batería de `unittest`: su convenio de salida es 0 todo bien · 1 hubo fallos",
    "tooling/tests":
        "batería de `unittest`: su convenio de salida es 0 todo bien · 1 hubo fallos",
}
EJECUTABLES_DEL_KERNEL = tuple(sorted(
    ruta for ruta, senales in INVENTARIO.items() if senales["zona"] == ZONA_DEL_KERNEL))

SEGUNDOS_DE_LA_TAREA = 90


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de las demás baterías del runtime, no importado: viven todas como guiones
    sueltos y ninguna está en la ruta de importación de las otras. La salida se PUBLICA como
    evidencia y tiene que ser byte-idéntica entre ejecuciones.
    """

    def run(self, test):
        import io as _io
        buffer = _io.StringIO()
        real, self.stream = self.stream, unittest.runner._WritelnDecorator(buffer)
        try:
            resultado = super().run(test)
        finally:
            self.stream = real
        real.write(re.sub(r"Ran (\d+) tests? in [\d.]+s",
                          r"Ran \1 tests  (duración no registrada: varía por ejecución)",
                          buffer.getvalue()))
        return resultado


# ===========================================================================
#  Cimientos: SESIÓN NUEVA de verdad y entorno CONSTRUIDO entero
# ===========================================================================
def texto_de_fichero(ruta):
    """Lectura que CIERRA: un `open(...).read()` suelto deja el descriptor al recolector."""
    with open(ruta, encoding="utf-8") as manejador:
        return manejador.read()


def bytes_de_fichero(ruta):
    with open(ruta, "rb") as manejador:
        return manejador.read()


class SesionNueva(unittest.TestCase):
    """Cada invocación es un PROCESO nuevo con un entorno construido desde cero.

    Nada se hereda del intérprete que corre la batería: si se heredara, una variable de la
    máquina de quien ejecuta podría explicar un verde, y la prueba mediría el anfitrión en
    vez de el aparato.
    """

    def setUp(self):
        self.taller = tempfile.mkdtemp(prefix="ads-integridad-")
        self.addCleanup(shutil.rmtree, self.taller, ignore_errors=True)

    def entorno(self, extra=None):
        entorno = {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "LC_ALL": "C.UTF-8",
            "LANG": "C.UTF-8",
            "TZ": "UTC",
            "HOME": self.taller,
        }
        if extra:
            entorno.update(extra)
        return entorno

    def correr(self, ejecutable, argumentos, *, extra=None, cwd=None, espera=300):
        # La ruta sale del INVENTARIO cuando el punto está en él: desde que el inventario
        # se deriva, `T306` recorre también `raiz-externa/`, que no cuelga de `runtime/`.
        senales = INVENTARIO.get(ejecutable)
        camino = senales["completa"] if senales else os.path.join(RAIZ_RUNTIME, ejecutable)
        return subprocess.run(
            [sys.executable, camino]
            + [str(a) for a in argumentos],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.entorno(extra), cwd=cwd or self.taller, check=False, timeout=espera,
        )

    def repo_de_pruebas(self, nombre="control"):
        """Un control repo Git REAL con la forma del corpus, y su commit base."""
        repo = os.path.join(self.taller, nombre)
        os.makedirs(repo, exist_ok=True)
        canal = CanalGit(repo)
        return repo, matriz.fundar(repo, canal), canal


# ===========================================================================
#  T306 · `E-10` · PROCEDENCIA con `--repo`
# ===========================================================================
class ProcedenciaDeLosModulos(SesionNueva):
    """`E-10`. De dónde salen los módulos con los que se juzga, y cómo se demuestra.

    HECHO REPRODUCIDO ANTES DE CORREGIR, sobre `ads_admision.py`: con
    `PYTHONPATH=<dir>` apuntando a un directorio con un `json.py` HOMÓNIMO, el proceso
    IMPORTABA el homónimo —`sys.path[0]` protege a los paquetes que viven junto al script,
    NO a la biblioteca estándar, que va después de `PYTHONPATH`— y
    `verificar --json` publicaba `{}` como veredicto con código 0. Los cinco puntos
    ejecutables importaban el módulo envenenado.

    Y REPRODUCIDO OTRA VEZ el 2026-09-04, en la zona que este control no alcanzaba (`H-01`
    y `H-03`): con un `hashlib.py` homónimo, `validadores/huella.py` publicaba
    `bc59513f7182130a` —la huella ESPERADA— sobre un árbol al que se le había añadido una
    línea a `ads_lint.py`, y `comprobar_integridad.py` sacaba `T150 SUPERADA · EXIT=0`.
    Desde entonces el alcance de esta prueba no es una tupla de zonas: es `EJECUTABLES`,
    derivado del ÁRBOL ENTERO, y son treinta y cinco puntos en siete zonas.
    """

    def paquete_envenenado(self):
        """Un directorio con homónimos que, si se importaran, SE NOTARÍA.

        Cada homónimo deja un FICHERO TESTIGO al importarse. Mirar sólo `stderr` no bastaría:
        una salida se puede tragar, y un fichero en disco, no.
        """
        veneno = os.path.join(self.taller, "veneno")
        os.makedirs(veneno, exist_ok=True)
        self.testigo = os.path.join(self.taller, "IMPORTADO-EL-HOMONIMO")
        cuerpo = (
            "import sys\n"
            "with open(" + repr(self.testigo) + ", 'a') as _m:\n"
            "    _m.write(__name__ + '\\n')\n"
            "sys.stderr.write('HOMONIMO MALICIOSO IMPORTADO: ' + __name__ + '\\n')\n"
        )
        # `json` es el que se coló de verdad: lo usan los cinco puntos ejecutables para
        # publicar su salida, y un `json.dumps` sustituido publica lo que quiera.
        with open(os.path.join(veneno, "json.py"), "w", encoding="utf-8") as manejador:
            manejador.write(cuerpo + "\ndef dumps(*a, **k):\n    return '{}'\n"
                            "def loads(*a, **k):\n    return {}\n")
        for paquete in ("admision", "estado", "runtime", "ciclo", "arboles",
                        "gobierno", "identidad", "contencion", "adaptadores",
                        "macrocircuitos"):
            carpeta = os.path.join(veneno, paquete)
            os.makedirs(carpeta, exist_ok=True)
            with open(os.path.join(carpeta, "__init__.py"), "w",
                      encoding="utf-8") as manejador:
                manejador.write(cuerpo)
        return veneno

    def test_T306_ningun_ejecutable_importa_un_homonimo_del_PYTHONPATH(self):
        """T306 · Defecto que previene: `E-10`, que el lanzador decida qué código juzga.

        SABOTAJE QUE LA PONE ROJA: retirar la purga de `sys.path` del preludio de
        CUALQUIERA de los treinta y cinco puntos —los `ads_*.py`, los cuatro de la raíz
        externa, los diecinueve de `validadores/`, `tooling/workspace.py`, los dos de
        `docs/` o los cuatro del instrumental del gate— o dejarla DESPUÉS de los `import`.
        """
        veneno = self.paquete_envenenado()
        repo, base, _canal = self.repo_de_pruebas()
        for ejecutable in EJECUTABLES:
            with self.subTest(ejecutable=ejecutable):
                resultado = self.correr(ejecutable, ["--help"],
                                        extra={"PYTHONPATH": veneno})
                self.assertNotIn(b"HOMONIMO MALICIOSO", resultado.stderr,
                                 ejecutable + " importó un homónimo del PYTHONPATH")
        self.assertFalse(os.path.exists(self.testigo),
                         "algún punto ejecutable importó un homónimo: "
                         + (open(self.testigo).read() if os.path.exists(self.testigo)
                            else ""))
        # CONTROL DEL CONTROL: el veneno SÍ se importa cuando nadie lo impide. Sin esto,
        # «no se importó» se explicaría por un paquete que no funciona.
        control = subprocess.run(
            [sys.executable, "-c", "import json"], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, env=self.entorno({"PYTHONPATH": veneno}),
            cwd=self.taller, check=False, timeout=60)
        self.assertIn(b"HOMONIMO MALICIOSO", control.stderr,
                      "el paquete envenenado no se importa ni cuando se le deja: esta "
                      "prueba no estaría midiendo nada")

    def test_T306b_el_veredicto_no_se_falsea_desde_el_PYTHONPATH(self):
        """T306 · Defecto que previene: publicar `{}` como veredicto y salir con código 0."""
        veneno = self.paquete_envenenado()
        repo, base, _canal = self.repo_de_pruebas()
        resultado = self.correr(
            "ads_admision.py",
            ["--repo", repo, "verificar", "--base", base, "--json"],
            extra={"PYTHONPATH": veneno})
        salida = resultado.stdout.decode("utf-8", "replace")
        self.assertTrue(salida.strip(), "el veredicto salió vacío")
        datos = json.loads(salida)
        self.assertIn("color", datos, "el veredicto publicado no tiene forma de veredicto")
        self.assertIn("procedencia", datos)
        self.assertFalse(os.path.exists(self.testigo))

    def test_T306c_la_procedencia_se_PUBLICA_y_nombra_cada_modulo(self):
        """T306 · Defecto que previene: una procedencia que hay que creerse."""
        repo, base, _canal = self.repo_de_pruebas()
        resultado = self.correr("ads_admision.py",
                                ["--repo", repo, "procedencia", "--json"])
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        datos = json.loads(resultado.stdout.decode("utf-8"))
        self.assertTrue(datos["modulos"], "no publica ningún módulo")
        for nombre, origen in sorted(datos["modulos"].items()):
            with self.subTest(modulo=nombre):
                self.assertTrue(origen.startswith("aparato:"),
                                nombre + " no viene del aparato: " + origen)
        # Y ninguna ruta ABSOLUTA del anfitrión viaja en la salida publicable.
        self.assertNotIn(os.path.realpath(RAIZ_REPO),
                         json.dumps(datos, ensure_ascii=False))

    def test_T306d_dos_repositorios_distintos_no_se_contaminan(self):
        """T306 · Defecto que previene: que el árbol juzgado aporte el código que lo juzga.

        Se construye un SEGUNDO repositorio que trae dentro su propio
        `kernel/operativo/runtime/admision/__init__.py`, envenenado. Se juzga ESE repo con el
        ejecutable del PRIMERO: el veredicto tiene que salir de los módulos del aparato, y la
        procedencia tiene que decirlo.
        """
        repo, base, canal = self.repo_de_pruebas("ajeno")
        intruso = os.path.join(repo, "kernel", "operativo", "runtime", "admision")
        os.makedirs(intruso, exist_ok=True)
        testigo = os.path.join(self.taller, "INTRUSO-DEL-REPO-AJENO")
        with open(os.path.join(intruso, "__init__.py"), "w", encoding="utf-8") as manejador:
            manejador.write("open(" + repr(testigo) + ", 'a').close()\n"
                            "def verificar(*a, **k):\n"
                            "    raise SystemExit(0)\n")
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "repo ajeno con su propio aparato")
        resultado = self.correr("ads_admision.py",
                                ["--repo", repo, "procedencia", "--json"])
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        datos = json.loads(resultado.stdout.decode("utf-8"))
        self.assertFalse(datos["repo_es_el_arbol_del_aparato"],
                         "el repo ajeno se confundió con el árbol del aparato")
        for nombre, origen in sorted(datos["modulos"].items()):
            with self.subTest(modulo=nombre):
                self.assertTrue(origen.startswith("aparato:"))
        self.assertFalse(os.path.exists(testigo),
                         "el aparato importó código del repositorio que estaba juzgando")

    def test_T306e_el_cwd_del_lanzador_no_sustituye_al_aparato(self):
        """T306 · Defecto que previene: colar un homónimo por el directorio de trabajo."""
        veneno = self.paquete_envenenado()
        repo, base, _canal = self.repo_de_pruebas()
        # Se ejecuta DESDE DENTRO del directorio envenenado y con él en `PYTHONPATH`: las
        # dos vías que `E-10` nombra, a la vez.
        resultado = self.correr("ads_admision.py",
                                ["--repo", repo, "procedencia", "--json"],
                                extra={"PYTHONPATH": veneno + os.pathsep + "."},
                                cwd=veneno)
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        datos = json.loads(resultado.stdout.decode("utf-8"))
        for origen in datos["modulos"].values():
            self.assertTrue(origen.startswith("aparato:"))
        self.assertFalse(os.path.exists(self.testigo))
        # `G-03` cambió lo que hay que exigir aquí, y por eso la afirmación es otra. Antes
        # el punto arrancaba contaminado y la purga retiraba dos entradas; ahora se
        # reejecuta aislado y las dos no llegan a entrar. Exigir «se retiró al menos una»
        # sería exigir que el defecto se produzca para poder corregirlo. Lo que se exige es
        # la propiedad, que es la misma en los dos mundos: ninguna entrada del lanzador
        # está en la ruta de importación, y el arranque lo declara.
        self.assertEqual(datos["entradas_del_lanzador_presentes"], 0,
                         "quedaron entradas del lanzador en la ruta de importación")
        for bandera in ("isolated", "no_site", "ignore_environment"):
            self.assertTrue(datos["aislamiento_de_arranque"][bandera],
                            "el punto no publicó `" + bandera + "`: se ejecutó sin aislar")


# ===========================================================================
#  T307 · `E-14` · `OK` NO EQUIVALE A `OK (skipped=N)`
# ===========================================================================
class ResultadoExactoDeLaEvidencia(unittest.TestCase):
    """`E-14`. La evidencia se comprueba por su RESULTADO ENTERO, no por una subcadena.

    HECHO REPRODUCIDO ANTES DE CORREGIR: dieciséis componentes de `validadores.yaml`
    declaran `firma_de_exito: 'OK'`, y la comprobación es `re.search`, de modo que
    `re.search('OK', 'OK (skipped=17)')` casa. Medido en el mismo repositorio: hay 17
    llamadas a `skipTest` repartidas por seis baterías del runtime, ninguna contada y
    ninguna publicada.
    """

    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, VALIDADORES)
        import comprobar_evidencia                                    # noqa: PLC0415
        import comprobar_contratos                                    # noqa: PLC0415
        cls.validador = comprobar_evidencia
        cls.Resultado = comprobar_contratos.Resultado

    def salida(self, casos=3, resultado="OK", ran=None, desenlace="ok"):
        """Una salida de `unittest` sintética, con la MISMA forma que la real."""
        lineas = []
        for indice in range(casos):
            lineas.append("test_" + str(indice) + " (__main__.X.test_" + str(indice) + ")")
            lineas.append("docstring de la prueba ... " + desenlace)
        lineas.append("")
        lineas.append("-" * 70)
        lineas.append("Ran " + str(casos if ran is None else ran)
                      + " tests  (duración no registrada: varía por ejecución)")
        lineas.append("")
        lineas.append(resultado)
        return "\n".join(lineas) + "\n"

    def juzgar(self, texto, comp=None):
        r = self.Resultado("T158", "prueba")
        self.validador._comprobar_resultado_exacto("evidencia.txt", comp or {"id": "x"},
                                                   texto, r)
        return r

    def test_T307_control_positivo_una_corrida_limpia_pasa(self):
        """T307 · Control del CONTROL: sin él, «todo falla» explicaría el verde."""
        r = self.juzgar(self.salida(casos=5))
        self.assertEqual(r.fallos, [], r.fallos)

    def test_T307b_OK_con_saltos_NO_declarados_es_ROJO(self):
        """T307 · Defecto que previene: `E-14`, que `OK` valga por `OK (skipped=N)`.

        SABOTAJE QUE LA PONE ROJA: volver a comprobar la firma con `re.search('OK', texto)`
        y nada más.
        """
        texto = self.salida(casos=3, resultado="OK (skipped=3)", desenlace="skipped 'x'")
        r = self.juzgar(texto)
        self.assertTrue(r.fallos, "una corrida con 3 saltos no declarados pasó como OK")
        self.assertIn("skipped", " ".join(r.fallos))
        # Y el control del control de la reproducción: la firma vieja SÍ casaba.
        self.assertTrue(re.search("OK", texto),
                        "la firma `OK` ya no casa con `OK (skipped=3)`, luego esta prueba "
                        "no estaría reproduciendo el defecto que cierra")

    def test_T307c_los_saltos_DECLARADOS_con_su_motivo_se_admiten_y_se_cuentan(self):
        """T307 · Defecto que previene: permitir saltos sin decir CUÁLES ni POR QUÉ."""
        texto = self.salida(casos=2, resultado="OK (skipped=2)",
                            desenlace="skipped 'sin cgroup ejercitable'")
        comp = {"id": "x", "skips_permitidos": [
            {"id": "sin cgroup ejercitable", "motivo": "E-18: el anfitrión no lo ejerce"},
            {"id": "sin cgroup ejercitable", "motivo": "E-18: el anfitrión no lo ejerce"},
        ]}
        self.assertEqual(self.juzgar(texto, comp).fallos, [])
        # Un salto de MÁS no está declarado...
        de_mas = self.salida(casos=3, resultado="OK (skipped=3)",
                             desenlace="skipped 'sin cgroup ejercitable'")
        self.assertTrue(self.juzgar(de_mas, comp).fallos)
        # ...y una declaración que ya no ocurre también es ROJO: el contrato ha caducado.
        self.assertTrue(self.juzgar(self.salida(casos=2), comp).fallos)
        # Y una declaración sin `motivo` es un defecto del manifiesto, no un permiso.
        sin_motivo = {"id": "x", "skips_permitidos": [{"id": "sin cgroup ejercitable"}]}
        self.assertTrue(self.juzgar(texto, sin_motivo).fallos)

    def test_T307d_manipular_el_CONTADOR_invalida_la_evidencia(self):
        """T307 · Defecto que previene: publicar una cifra que no describe la corrida.

        La cifra `Ran N tests` la declara la propia evidencia. El recuento se DERIVA de los
        desenlaces que la salida verbosa imprime, y los dos tienen que casar.
        """
        r = self.juzgar(self.salida(casos=3, ran=38))
        self.assertTrue(r.fallos, "una evidencia con el contador inflado pasó")
        self.assertIn("desenlaces", " ".join(r.fallos))
        # Y hacia abajo tampoco: recortar la salida y bajar el contador no vale.
        self.assertTrue(self.juzgar(self.salida(casos=5, ran=2)).fallos)

    def test_T307e_fallos_errores_y_dos_corridas_pegadas_son_ROJO(self):
        """T307 · Defecto que previene: publicar la corrida buena y esconder la mala."""
        self.assertTrue(self.juzgar(
            self.salida(casos=2, resultado="FAILED (failures=1)")).fallos)
        self.assertTrue(self.juzgar(
            self.salida(casos=2, resultado="OK (failures=1)")).fallos)
        self.assertTrue(self.juzgar(
            self.salida(casos=2, resultado="OK (expected failures=1)")).fallos)
        pegadas = self.salida(casos=2, resultado="FAILED (errors=1)") + self.salida(casos=2)
        r = self.juzgar(pegadas)
        self.assertTrue(r.fallos)
        self.assertIn("EXACTAMENTE", " ".join(r.fallos))

    def test_T307f_la_evidencia_PUBLICADA_del_repositorio_supera_la_comprobacion(self):
        """T307 · Control POSITIVO sobre el corpus real: la regla nueva no es inaplicable.

        Se juzga la evidencia que el repositorio publica HOY. Si la comprobación fuese
        imposible de superar, sería indistinguible de una que no comprueba nada.
        """
        directorio = os.path.join(RAIZ_OPERATIVO, "pruebas", "evidencia")
        vistos = 0
        for nombre in sorted(os.listdir(directorio)):
            if not nombre.endswith(".txt"):
                continue
            with open(os.path.join(directorio, nombre), encoding="utf-8") as manejador:
                texto = manejador.read()
            if self.validador._resultado_de_unittest(texto) is None:
                continue
            vistos += 1
            with self.subTest(evidencia=nombre):
                self.assertEqual(self.juzgar(texto, {"id": nombre}).fallos, [])
        self.assertGreater(vistos, 5,
                           "no se encontró evidencia de `unittest` que juzgar: el control "
                           "positivo no habría podido fallar")

    def test_T307g_la_COBERTURA_DEL_CONTRASTE_va_publicada_en_la_evidencia(self):
        """T307 · Defecto que previene: `H-08`, una cifra que se calcula y no se publica.

        HECHO REPRODUCIDO POR LA AUDITORÍA INDEPENDIENTE DEL 2026-09-04: la línea base
        afirmaba «160 escenarios contrastados · 107 no contrastables»; el árbol producía
        `193 · 74`, y ninguna de las dos parejas de cifras aparecía en ningún fichero
        —un `grep` de las dos parejas sobre el árbol entero: vacío—.
        `comprobar_evidencia` CALCULABA `r.nota_cobertura` y no la imprimía nadie.

        DECISIÓN · se juzga la SALIDA DE UNA CORRIDA, no el fichero de evidencia publicado
            La primera versión de esta prueba leía `evidencia/evidencia-salida.txt`, y se
            midió lo que eso produce: un CICLO. La evidencia de `comprobar_evidencia` sólo
            se republica cuando ese validador termina en 0, y ese validador no termina en 0
            hasta que la evidencia de ESTA batería nombre a `T310` y a `T311`, que es lo que
            esta misma pasada corrige; y esta batería no termina en 0 hasta que aquella
            evidencia lleve la cifra. Ninguna de las dos puede ir primero. Corriendo el
            validador aquí se mide lo que de verdad importa —que el aparato PUBLIQUE la
            cifra— sin depender de en qué orden se regeneró nada, y además el sabotaje que
            retira el `print` se detecta EN EL ACTO en vez de en la regeneración siguiente.
            El fichero publicado lo cubre por su lado `debe_contener` en `validadores.yaml`.

        SABOTAJE QUE LA PONE ROJA: retirar de `main()` la línea que imprime
        `cobertura del contraste:` (`NH08`).
        """
        corrida = subprocess.run(
            [sys.executable, os.path.join(VALIDADORES, "comprobar_evidencia.py")],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            cwd=RAIZ_REPO, check=False, timeout=300)
        texto = corrida.stdout.decode("utf-8", "replace")
        self.assertIn("cobertura del contraste:", texto,
                      "`comprobar_evidencia` no publica la cobertura del contraste: la "
                      "cifra vuelve a calcularse y a no existir (`H-08`). stderr="
                      + corrida.stderr.decode("utf-8", "replace")[:300])
        medida = re.search(r"cobertura del contraste: contrastados (\d+) · no contrastables "
                           r"(\d+) · divergencias (\d+)", texto)
        self.assertIsNotNone(medida, "la cobertura se publica con otra forma: "
                                     "un número que nadie puede leer no es una cifra")
        contrastados, no_contrastables, divergencias = (int(g) for g in medida.groups())
        self.assertGreater(contrastados, 0)
        self.assertIn("no contrastables por estado declarado:", texto,
                      "no se publica el DESGLOSE de los no contrastables, que es lo que "
                      "mantuvo invisibles a los catorce de `H-02`")
        # Y la cifra publicada es la del ÁRBOL, no una escrita: se recalcula aquí, desde la
        # SEDE de la derivación, y tiene que coincidir.
        sys.path.insert(0, VALIDADORES)
        import registro_pruebas                                       # noqa: PLC0415
        from ads_lint import Lint                                     # noqa: PLC0415
        lint = Lint(RAIZ_REPO, ["kernel/operativo", "packs"])
        lint.cargar_esquemas()
        lint.cargar_bloques()
        escenarios = [d for tipo, d, _f, _l in lint.bloques if tipo == "escenario"]
        div, con, sin = registro_pruebas.contraste_de_estados(escenarios, RAIZ_REPO)
        self.assertEqual((contrastados, no_contrastables, divergencias),
                         (len(con), len(sin), len(div)),
                         "la cifra publicada no es la que el árbol produce hoy")

# ===========================================================================
#  T308 · `E-15` · NINGÚN ERROR TIPADO SALE COMO TRAZA
# ===========================================================================

# ===========================================================================
#  `D-05` · EL CANAL «LA EVIDENCIA ES LA CONFIRMADA EN `HEAD`», SABOTEADO DE VERDAD
# ===========================================================================
#  HECHO REPRODUCIDO ANTES DE CORREGIR. `comprobar_evidencia._contrastar_contra_head`
#  estaba implementado y no lo ponía rojo NADA: `comprobar_negativos.py` monta cada
#  sabotaje sobre una COPIA DEL CORPUS SIN `.git`, y esa función abre con
#
#      if not os.path.isdir(os.path.join(base, ".git")): return "sin repositorio Git…"
#
#  es decir, en el único banco de pruebas que teníamos, el canal entero se saltaba por la
#  primera línea. Medido: 164 mutaciones del catálogo, CERO sobre este camino. Un canal
#  sin sabotaje mecanizado no está probado; está escrito.
#
#  Lo que esta clase hace: monta un repositorio Git REAL en un temporal —blob, commit,
#  tree y `HEAD` de verdad, sin ningún mock—, y ejecuta contra él los OCHO ataques que el
#  canal tiene que resistir, más el CONTROL SANO sin el que «todo da rojo» explicaría
#  igual de bien los ocho verdes.
#
#  LO QUE ESTA CLASE NO AFIRMA. El canal juzga el DICTAMEN, no los bytes: una regeneración
#  legítima difiere de `HEAD` y eso NO es rojo, y así lo mide el ataque 4. Que el contenido
#  de la zona `EVIDENCIA` no mute sin declararlo lo juzga `V6-10` en el verificador de
#  admisión, y reescribir la historia de Git —`amend`, mover la referencia— lo juzga la
#  huella del kernel: los ataques 7 y 8 miden lo que ESTE canal hace ante ellos, que es
#  quedarse sin base de contraste, y exigen que lo DIGA en vez de dar verde callando.

class EvidenciaConfirmadaEnHead(unittest.TestCase):
    """`T420`-`T428` · `D-05`. Los ocho ataques al contraste contra `HEAD`, mecanizados.

    Cada caso construye su propio repositorio: `git init`, la evidencia escrita, `git add`
    y `git commit`. A partir de ahí el ataque toca UNA cosa —el árbol de trabajo, el blob,
    la referencia, el directorio `.git`— y se exige el veredicto exacto, por su motivo.
    """

    @classmethod
    def setUpClass(cls):
        if VALIDADORES not in sys.path:
            sys.path.insert(0, VALIDADORES)
        import comprobar_contratos                                    # noqa: PLC0415
        import comprobar_evidencia                                    # noqa: PLC0415
        cls.validador = comprobar_evidencia
        cls.Resultado = comprobar_contratos.Resultado

    # -- montaje ------------------------------------------------------------
    ENTORNO_GIT = {
        "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull,
        "GIT_AUTHOR_NAME": "ads-d05", "GIT_AUTHOR_EMAIL": "d05@ads.local",
        "GIT_COMMITTER_NAME": "ads-d05", "GIT_COMMITTER_EMAIL": "d05@ads.local",
        "GIT_AUTHOR_DATE": "2026-01-01T00:00:00+00:00",
        "GIT_COMMITTER_DATE": "2026-01-01T00:00:00+00:00",
    }

    def _git(self, base, *args):
        entorno = dict(os.environ)
        entorno.update(self.ENTORNO_GIT)
        proc = subprocess.run(["git", "-C", base] + list(args),
                              capture_output=True, text=True, env=entorno)
        self.assertEqual(proc.returncode, 0,
                         "git " + " ".join(args) + " falló: " + (proc.stderr or ""))
        return proc.stdout

    def salida_de_bateria(self, identificador, buenos, malos=0):
        """Una salida de `unittest` con veredictos NOMBRADOS para ese escenario."""
        lineas = []
        for indice in range(buenos):
            lineas.append(identificador + " · caso bueno " + str(indice) + " ... ok")
        for indice in range(malos):
            lineas.append(identificador + " · caso malo " + str(indice) + " ... FAIL")
        lineas.append("")
        lineas.append(str(buenos + malos) + " superadas · 0 fallidas")
        return "\n".join(lineas) + "\n"

    def montar(self, contenido, nombre="d05-salida.txt"):
        """Un repositorio Git REAL con esa evidencia confirmada en `HEAD`."""
        base = tempfile.mkdtemp(prefix="ads-d05-")
        self.addCleanup(shutil.rmtree, base, True)
        destino = os.path.join(base, self.validador.DIR_EVIDENCIA)
        os.makedirs(destino)
        ruta = os.path.join(destino, nombre)
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write(contenido)
        self._git(base, "init", "-q", "-b", "principal")
        self._git(base, "add", "-A")
        self._git(base, "commit", "-q", "-m", "evidencia inicial")
        return base, ruta

    def contrastar(self, base, escenarios):
        r = self.Resultado("T420", "contraste contra HEAD")
        nota = self.validador._contrastar_contra_head(base, escenarios, r)
        return r, nota

    ESCENARIO = [{"id": "T900", "evidencia": "evidencia/d05-salida.txt"}]

    # -- el control sano ----------------------------------------------------
    def test_T420_control_sano_blob_commit_tree_digest_y_arbol_limpio(self):
        """T420 · Control del CONTROL: sin él, «todo da rojo» explicaría los ocho verdes.

        Y no basta con que pase: se comprueba que el montaje es un repositorio DE VERDAD
        —hay un commit, hay un tree, el blob de la evidencia existe y su digest es el de
        su contenido, y el árbol de trabajo está limpio—. Si algo de esto fuera de mentira,
        los ocho ataques de abajo estarían atacando a un decorado.
        """
        contenido = self.salida_de_bateria("T900", buenos=6)
        base, ruta = self.montar(contenido)

        commit = self._git(base, "rev-parse", "HEAD").strip()
        self.assertRegex(commit, r"^[0-9a-f]{40}$", "no hay commit: no hay `HEAD`")
        tipo = self._git(base, "cat-file", "-t", commit).strip()
        self.assertEqual(tipo, "commit")
        tree = self._git(base, "rev-parse", "HEAD^{tree}").strip()
        self.assertEqual(self._git(base, "cat-file", "-t", tree).strip(), "tree")
        rel = os.path.join(self.validador.DIR_EVIDENCIA, "d05-salida.txt")
        blob = self._git(base, "rev-parse", "HEAD:" + rel).strip()
        self.assertEqual(self._git(base, "cat-file", "-t", blob).strip(), "blob")
        # el digest del blob es el que Git calcula para ESTE contenido, no otro
        with open(ruta, "rb") as fh:
            crudo = fh.read()
        cabecera = b"blob " + str(len(crudo)).encode("ascii") + b"\x00"
        self.assertEqual(blob, hashlib.sha1(cabecera + crudo).hexdigest(),
                         "el blob de `HEAD` no es el digest del contenido en disco")
        self.assertEqual(self._git(base, "status", "--porcelain"), "",
                         "el árbol de trabajo no está limpio: el contraste mediría otra cosa")

        r, nota = self.contrastar(base, self.ESCENARIO)
        self.assertEqual(r.fallos, [], "el control sano NO puede dar rojo")
        self.assertIn("evidencia contrastada contra el blob de HEAD: 1", nota)

    # -- los ocho ataques ---------------------------------------------------
    def test_T421_un_veredicto_bueno_se_edita_a_malo(self):
        """T421 · ataque 1 · `ok` reescrito como `FAIL` en el árbol de trabajo."""
        base, ruta = self.montar(self.salida_de_bateria("T900", buenos=6))
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write(self.salida_de_bateria("T900", buenos=5, malos=1))
        r, _ = self.contrastar(base, self.ESCENARIO)
        self.assertTrue(r.fallos, "un `ok` convertido en `FAIL` pasó sin ser detectado")
        self.assertIn("ha cambiado de DICTAMEN", " ".join(r.fallos))

    def test_T422_un_veredicto_malo_se_edita_a_bueno(self):
        """T422 · ataque 2 · el sentido contrario: un `FAIL` confirmado se borra del disco.

        Es el ataque que de verdad importa —tapar un rojo—, y es distinto del anterior: el
        conjunto de veredictos ENCOGE en vez de crecer, y la cuenta de malos baja.
        """
        base, ruta = self.montar(self.salida_de_bateria("T900", buenos=5, malos=1))
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write(self.salida_de_bateria("T900", buenos=6))
        r, _ = self.contrastar(base, self.ESCENARIO)
        self.assertTrue(r.fallos, "borrar un `FAIL` confirmado pasó sin ser detectado")
        self.assertIn("ha cambiado de DICTAMEN", " ".join(r.fallos))

    def test_T423_la_evidencia_encoge_en_silencio(self):
        """T423 · ataque 3 · misma clase de veredictos, MENOS casos. El cliquet."""
        base, ruta = self.montar(self.salida_de_bateria("T900", buenos=6))
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write(self.salida_de_bateria("T900", buenos=1))
        r, _ = self.contrastar(base, self.ESCENARIO)
        self.assertTrue(r.fallos, "la evidencia adelgazó de seis casos a uno sin rojo")
        self.assertIn("ha ENCOGIDO", " ".join(r.fallos))

    def test_T424_una_regeneracion_legitima_no_da_rojo(self):
        """T424 · ataque 4 · el FALSO POSITIVO, que es el ataque contra el guardián.

        Añadir un caso que pasa cambia los bytes y no cambia el dictamen. Si esto diera
        rojo, el canal castigaría reforzar una batería y acabaría apagado, que es la forma
        más barata de derrotarlo: no hace falta editar nada si el guardián ya está apagado.
        """
        base, ruta = self.montar(self.salida_de_bateria("T900", buenos=6))
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write(self.salida_de_bateria("T900", buenos=7))
        r, nota = self.contrastar(base, self.ESCENARIO)
        self.assertEqual(r.fallos, [], "una regeneración legítima dio ROJO")
        self.assertIn("sin cambiar ningún dictamen", nota)

    def test_T425_la_evidencia_se_vacia_entera(self):
        """T425 · ataque 5 · el fichero se queda sin un solo veredicto.

        Vaciar es la vía por la que se esquiva una comparación: sin veredictos que comparar,
        el canal podría no tener nada que decir. Tiene que decir que ENCOGIÓ.
        """
        base, ruta = self.montar(self.salida_de_bateria("T900", buenos=6))
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write("")
        r, _ = self.contrastar(base, self.ESCENARIO)
        self.assertTrue(r.fallos, "vaciar la evidencia entera pasó sin ser detectado")
        self.assertIn("NO PUBLICA NINGUNO", " ".join(r.fallos))

    def test_T426_el_escenario_se_renombra_para_no_ser_contrastado(self):
        """T426 · ataque 6 · el veredicto sigue ahí, pero deja de NOMBRAR al escenario.

        Con el identificador cambiado, la versión del disco no publica ningún veredicto
        para `T900`: si el canal exigiera que los hubiera en las dos versiones para
        comparar, este ataque lo atravesaría sin ruido. Mide qué hace de verdad.
        """
        base, ruta = self.montar(self.salida_de_bateria("T900", buenos=5, malos=1))
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write(self.salida_de_bateria("T901", buenos=6))
        r, nota = self.contrastar(base, self.ESCENARIO)
        # Mecanizar este ataque encontró el hueco: con la guarda anterior —`if not (antes
        # and despues): continue`— esto pasaba en VERDE, porque la versión del disco no
        # publica ningún veredicto para `T900` y no había nada que comparar. Es la vía más
        # limpia de retirar un rojo: no se edita el dictamen, se deja de emitirlo.
        self.assertTrue(r.fallos, "renombrar el escenario retiró su dictamen sin rojo")
        self.assertIn("NO PUBLICA NINGUNO", " ".join(r.fallos))
        self.assertIn("difieren de HEAD", nota)

    def test_T427_sin_repositorio_git_el_canal_lo_DICE(self):
        """T427 · ataque 7 · se borra `.git`. El peligro no es el rojo: es el verde MUDO.

        Es EXACTAMENTE la forma del defecto que `D-05` nombra: `comprobar_negativos` copia
        el corpus sin `.git` y por eso el canal entero no se ejercía. Sin base de contraste
        el canal no puede juzgar, y lo único que no puede hacer es callarse.
        """
        base, _ = self.montar(self.salida_de_bateria("T900", buenos=6))
        shutil.rmtree(os.path.join(base, ".git"))
        r, nota = self.contrastar(base, self.ESCENARIO)
        self.assertEqual(r.fallos, [])
        self.assertIn("NO se ha hecho", nota)
        self.assertIn("no se da por hecho", nota)

    def test_T429_borrar_la_evidencia_da_FALLIDA_igual_que_vaciarla(self):
        """T429 · ataque 9 · el que el auditor independiente encontró abierto.

        Vaciar el fichero era rojo (`T425`) y BORRARLO era verde: dos gestos con el mismo
        efecto —el dictamen deja de existir— y veredictos opuestos. La guarda era
        `if not os.path.isfile(ruta): continue`, y con ella el ataque más simple de los
        nueve —`rm`— atravesaba el canal sin ruido. Se comprueba también que el canal lo
        CUENTA, porque un fallo que no figura en el recuento no lo puede auditar nadie.
        """
        base, ruta = self.montar(self.salida_de_bateria("T900", buenos=5, malos=1))
        os.remove(ruta)
        r, nota = self.contrastar(base, self.ESCENARIO)
        self.assertTrue(r.fallos, "borrar la evidencia confirmada pasó sin ser detectado")
        self.assertIn("NO EXISTE", " ".join(r.fallos))
        self.assertIn("AUSENTES del árbol de trabajo: 1", nota)

    def test_T428_la_evidencia_no_esta_confirmada_en_HEAD(self):
        """T428 · ataque 8 · el fichero existe en disco y NO está en `HEAD`.

        Un fichero sin confirmar no tiene contra qué contrastarse. El canal tiene que
        contarlo y NOMBRARLO, porque un fichero que nadie confirmó es exactamente donde se
        escondería una evidencia fabricada.
        """
        base, _ = self.montar(self.salida_de_bateria("T900", buenos=6))
        otra = os.path.join(base, self.validador.DIR_EVIDENCIA, "d05-nueva-salida.txt")
        with open(otra, "w", encoding="utf-8") as fh:
            fh.write(self.salida_de_bateria("T901", buenos=3))
        escenarios = self.ESCENARIO + [{"id": "T901",
                                        "evidencia": "evidencia/d05-nueva-salida.txt"}]
        r, nota = self.contrastar(base, escenarios)
        self.assertEqual(r.fallos, [])
        self.assertIn("todavía NO confirmadas en HEAD: 1", nota)
        self.assertIn("d05-nueva-salida.txt", nota)

class ErroresTipadosDeLaCLI(SesionNueva):
    """`E-15`. Los cinco puntos ejecutables, y las jerarquías tipadas que los alcanzan.

    HECHO REPRODUCIDO ANTES DE CORREGIR: `adaptadores.contrato.CapacidadNoSoportada`
    escapaba de `ads_runtime.main()` como TRACEBACK con rutas absolutas del anfitrión,
    `stdout` vacío y código 1 —el mismo que un fallo tipado, luego indistinguible—. Matiz
    medido y conservado: la clase HOMÓNIMA del runtime (`runtime/errores.py`) SÍ se
    capturaba y salía como `[CAPACIDAD_NO_SOPORTADA] ...` limpio. Son dos jerarquías
    distintas a propósito, y el punto ejecutable tenía que conocer las dos.
    """

    def exigir_salida_limpia(self, resultado, *, codigo, donde):
        texto = (resultado.stdout + resultado.stderr).decode("utf-8", "replace")
        self.assertEqual(resultado.returncode, codigo,
                         donde + ": código " + str(resultado.returncode)
                         + " y se esperaba " + str(codigo) + " · " + texto[:400])
        self.assertNotIn("Traceback (most recent call last)", texto,
                         donde + ": salió una traza")
        for absoluta in (os.path.realpath(RAIZ_REPO), os.path.abspath(RAIZ_REPO)):
            self.assertNotIn(absoluta, texto,
                             donde + ": publicó una ruta absoluta del anfitrión")
        self.assertTrue(re.search(r"\[[A-Z][A-Z0-9_]{4,}\]", texto),
                        donde + ": no publicó ningún código tipado")
        return texto

    def paquete_de_prueba(self, capacidades):
        """Un control repo con un item y un paquete despachable. Nada simulado."""
        import runtime as runtime_ads                                 # noqa: PLC0415
        control = os.path.join(self.taller, "control")
        espacio = os.path.join(self.taller, "espacio")
        os.makedirs(control, exist_ok=True)
        os.makedirs(espacio, exist_ok=True)
        rt = runtime_ads.Runtime(control, instancia="mc-e15").abrir()
        try:
            rt.crear_item(id="it-1", titulo="item", motivo="E-15")
            rt.crear_paquete(id="pq-1", item="it-1",
                             capacidades_requeridas=list(capacidades),
                             orden={"adaptador": "proceso-local", "operacion": "ejecutar",
                                    "argumentos": ["/bin/true"], "limite_segundos": 30})
        finally:
            rt.cerrar()
        return control, espacio

    def test_T308_la_tabla_de_codigos_es_la_MISMA_en_los_cinco(self):
        """T308 · Defecto que previene: cinco CLI con cinco convenios de salida distintos.

        El alcance se DERIVA igual que el de `T306` y se estrecha a la zona del kernel por
        el motivo escrito junto a `EJECUTABLES_DEL_KERNEL`: la raíz externa tiene un
        convenio propio que `O25` §2 fija, y los validadores documentales tienen el de
        `comprobar_contratos`; forzarles la tabla del kernel borraría distinciones que los
        contratos hacen a propósito. Desde `H-03` el estrechamiento NO se escribe fichero a
        fichero: se declara POR ZONA con su motivo, y aquí se comprueba que ninguna zona
        excluida se quede sin declarar y que ninguna zona declarada haya dejado de existir.
        Así el estrechamiento no puede crecer en silencio: una zona nueva sin motivo escrito
        pone esta prueba en rojo.
        """
        excluidos = set(EJECUTABLES) - set(EJECUTABLES_DEL_KERNEL)
        self.assertTrue(excluidos, "el alcance de T308 no excluye nada: no se derivó")
        zonas_excluidas = {INVENTARIO[ruta]["zona"] for ruta in excluidos}
        for zona in sorted(zonas_excluidas):
            self.assertIn(zona, MOTIVO_DE_LA_EXCLUSION_DE_T308,
                          "la zona `" + zona + "` quedó fuera de `T308` y su motivo no "
                          "está declarado: el estrechamiento creció en silencio")
        for zona, motivo in sorted(MOTIVO_DE_LA_EXCLUSION_DE_T308.items()):
            self.assertIn(zona, zonas_excluidas,
                          "se declara el motivo de excluir `" + zona + "` y ya no hay "
                          "ningún punto ejecutable ahí: el motivo ha caducado")
            self.assertTrue(motivo.strip(), zona + " se excluye sin motivo escrito")
        self.assertNotIn(ZONA_DEL_KERNEL, zonas_excluidas)
        tablas = {}
        for ejecutable in EJECUTABLES_DEL_KERNEL:
            guion = (
                "import runpy, json\n"
                "modulo = runpy.run_path("
                + repr(INVENTARIO[ejecutable]["completa"])
                + ", run_name='no-main')\n"
                "print(json.dumps(modulo['CODIGOS_DE_SALIDA'], sort_keys=True))\n"
            )
            proceso = subprocess.run([sys.executable, "-c", guion],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     env=self.entorno(), cwd=self.taller, check=False,
                                     timeout=120)
            self.assertEqual(proceso.returncode, 0,
                             ejecutable + ": " + proceso.stderr.decode()[:300])
            tablas[ejecutable] = json.loads(proceso.stdout.decode())
        referencia = tablas[EJECUTABLES_DEL_KERNEL[0]]
        self.assertEqual(referencia["exito"], 0)
        self.assertEqual(referencia["error-del-kernel"], 1)
        self.assertEqual(referencia["uso-incorrecto"], 2)
        for ejecutable, tabla in tablas.items():
            with self.subTest(ejecutable=ejecutable):
                self.assertEqual(tabla, referencia)
        # Y los códigos son DISTINTOS entre sí: una tabla con dos claves al mismo número
        # no distingue nada.
        self.assertEqual(len(set(referencia.values())), len(referencia))

    def test_T308b_el_error_del_ADAPTADOR_no_sale_como_traza(self):
        """T308 · Defecto que previene: `E-15`, la clase homónima que nadie capturaba."""
        control, espacio = self.paquete_de_prueba(["capacidad-que-nadie-ofrece"])
        resultado = self.correr("ads_runtime.py",
                                ["--repo", control, "--instancia", "mc-externa",
                                 "--adaptador-local", espacio, "despachar", "pq-1"])
        texto = self.exigir_salida_limpia(resultado, codigo=3,
                                          donde="ads_runtime/adaptador")
        self.assertIn("CAPACIDAD_NO_SOPORTADA", texto)
        self.assertIn("error-del-adaptador", texto)

    def test_T308c_la_clase_HOMONIMA_del_runtime_sigue_saliendo_por_su_codigo(self):
        """T308 · El matiz, conservado: son DOS jerarquías y se distinguen en la salida."""
        control, espacio = self.paquete_de_prueba(["capacidad-que-nadie-ofrece"])
        resultado = self.correr("ads_runtime.py",
                                ["--repo", control, "--instancia", "mc-externa",
                                 "--registro-en-pruebas", espacio, "despachar", "pq-1"])
        texto = self.exigir_salida_limpia(resultado, codigo=1,
                                          donde="ads_runtime/runtime")
        self.assertIn("CAPACIDAD_NO_SOPORTADA", texto)

    def test_T308d_el_error_de_CONTENCION_tiene_su_propio_codigo(self):
        """T308 · Defecto que previene: confundir «no puedo contener» con «falló la tarea»."""
        control, espacio = self.paquete_de_prueba(["proceso-local"])
        resultado = self.correr(
            "ads_runtime.py",
            ["--repo", control, "--instancia", "mc-externa",
             "--adaptador-local", espacio,
             "--contencion", "arbol-de-procesos", "--contencion-backend", "simple",
             "despachar", "pq-1"])
        texto = self.exigir_salida_limpia(resultado, codigo=4,
                                          donde="ads_runtime/contencion")
        self.assertIn("CONTENCION_FUERTE_NO_DISPONIBLE", texto)
        self.assertIn("error-de-contencion", texto)

    def test_T308e_los_CINCO_ejecutables_fallan_tipados_y_sin_traza(self):
        """T308 · Defecto que previene: cerrar el agujero en uno y dejarlo en los otros.

        Cada punto ejecutable se lleva a un fallo TIPADO de su propia jerarquía, con una
        entrada que sólo él puede rechazar. Lo que se exige es lo mismo en los cinco: código
        estable, código tipado en la salida, cero trazas y cero rutas del anfitrión.
        """
        control, _base, _canal = self.repo_de_pruebas("sin-almacen")
        casos = [
            ("ads_estado.py", ["--repo", control, "revision"], 1),
            ("ads_admision.py",
             ["--repo", control, "verificar", "--base", "no-existe-esta-revision"], 1),
            ("ads_arboles.py", ["--repo", control, "conjunto"], 1),
            ("ads_runtime.py",
             ["--repo", control, "--instancia", "mc", "estado-paquete", "pq-inexistente"],
             1),
            ("ads_ciclo.py",
             ["encuadrar", "--repo", control, "--instancia", "mc",
              "--fuente", os.path.join(self.taller, "no-existe.md")], None),
        ]
        for ejecutable, argumentos, codigo in casos:
            with self.subTest(ejecutable=ejecutable):
                resultado = self.correr(ejecutable, argumentos)
                texto = (resultado.stdout + resultado.stderr).decode("utf-8", "replace")
                self.assertNotEqual(resultado.returncode, 0,
                                    ejecutable + " devolvió 0 sobre una entrada inválida")
                self.assertNotIn("Traceback (most recent call last)", texto,
                                 ejecutable + " salió con una traza")
                self.assertNotIn(os.path.realpath(RAIZ_REPO), texto,
                                 ejecutable + " publicó una ruta absoluta del anfitrión")
                if codigo is not None:
                    self.assertEqual(resultado.returncode, codigo, texto[:300])

    def test_T308f_no_hay_EXITO_PARCIAL_cuando_el_fallo_es_tipado(self):
        """T308 · Defecto que previene: publicar medio veredicto y además fallar."""
        control, espacio = self.paquete_de_prueba(["capacidad-que-nadie-ofrece"])
        resultado = self.correr("ads_runtime.py",
                                ["--repo", control, "--instancia", "mc-externa",
                                 "--adaptador-local", espacio, "despachar", "pq-1"])
        self.assertEqual(resultado.returncode, 3)
        self.assertEqual(resultado.stdout.decode("utf-8", "replace").strip(), "",
                         "se publicó salida de éxito junto con el fallo")
        # Y la salida estructurada existe y es interpretable, que es lo que `E-15` exige.
        estructuras = [linea for linea
                       in resultado.stderr.decode("utf-8", "replace").split("\n{")
                       if '"clase_de_fallo"' in linea]
        self.assertTrue(estructuras, "el fallo no publicó salida estructurada")
        datos = json.loads("{" + estructuras[-1])
        self.assertEqual(datos["codigo_de_salida"], 3)
        self.assertEqual(datos["error"]["codigo"], "CAPACIDAD_NO_SOPORTADA")


# ===========================================================================
#  T309 · `E-16` la CONTENCIÓN CABLEADA · `E-18` el ALCANCE de este anfitrión
# ===========================================================================
def _capa(marca, interior, segundos):
    """Una generación: se sale de su grupo con `setsid` y engendra la siguiente."""
    cuerpo = ": " + marca + "\n" + interior + "sleep " + str(segundos) + "\n"
    return "setsid sh -c " + shlex.quote(cuerpo) + " &\n"


def guion_generacional(prefijo, segundos=SEGUNDOS_DE_LA_TAREA):
    """El guion `sh` que engendra hijo, nieto y BISNIETO, los tres con `setsid`.

    Se escribe aquí y no se importa de `test_contencion.py`: las baterías del runtime son
    guiones sueltos y ninguna está en la ruta de importación de las otras. Lo que se conserva
    es la FORMA de la tarea, que es lo que hace comparables las dos medidas.
    """
    bisnieto = _capa(prefijo + "-BISNIETO", "", segundos)
    nieto = _capa(prefijo + "-NIETO", bisnieto, segundos)
    hijo = _capa(prefijo + "-HIJO", nieto, segundos)
    return (": " + prefijo + "-RAIZ\n" + hijo + "sleep 1.2\n" + "echo listo\n"
            + "sleep " + str(segundos) + "\n")


def generaciones(prefijo):
    """`{raiz, hijo, nieto, bisnieto}` con los PID del ANFITRIÓN de cada generación."""
    raiz = set(contencion.pids_con_marca(prefijo + "-RAIZ"))
    con_hijo = set(contencion.pids_con_marca(prefijo + "-HIJO"))
    con_nieto = set(contencion.pids_con_marca(prefijo + "-NIETO"))
    con_bisnieto = set(contencion.pids_con_marca(prefijo + "-BISNIETO"))
    return {
        "raiz": sorted(raiz),
        "hijo": sorted(con_hijo - raiz),
        "nieto": sorted(con_nieto - con_hijo),
        "bisnieto": sorted(con_bisnieto - con_nieto),
    }


class ContencionEnElCaminoProductivo(SesionNueva):
    """`E-16`. La política de contención, alcanzable desde el PUNTO EJECUTABLE.

    HECHO REPRODUCIDO ANTES DE CORREGIR: la cadena `contencion` no aparecía en NINGUNO de
    los cinco `ads_*.py`, ni en `ciclo/`, ni en `runtime/`; sólo dentro de
    `adaptadores/proceso.py`. La política estaba construida y probada y NINGÚN punto
    ejecutable podía activarla: el camino productivo lanzaba siempre el adaptador sin
    política, es decir con `killpg`, cuyo límite medido es que el bisnieto ESCAPA.

    `test_contencion.py` conserva el control que impide presentar el débil como fuerte —el
    backend fuerte deja 0 supervivientes sobre tres generaciones y el simple deja escapar el
    bisnieto—. Lo que falta y se añade aquí es el camino PRODUCTIVO.
    """

    def setUp(self):
        super().setUp()
        self.prefijo = "ADSE16" + os.urandom(6).hex().upper()
        self.capacidades = contencion.capacidades()
        self.addCleanup(self._rematar)

    def _rematar(self):
        """Ningún superviviente de esta prueba sobrevive a la batería. Ni uno."""
        import signal                                                 # noqa: PLC0415
        for generacion in generaciones(self.prefijo).values():
            for pid in generacion:
                try:
                    os.kill(pid, signal.SIGKILL)
                except OSError:
                    continue

    def preparar(self, *, capacidades=("proceso-local",), segundos=6):
        """Un control repo con un paquete cuya tarea engendra TRES generaciones."""
        import runtime as runtime_ads                                 # noqa: PLC0415
        control = os.path.join(self.taller, "control")
        espacio = os.path.join(self.taller, "espacio")
        os.makedirs(control, exist_ok=True)
        os.makedirs(espacio, exist_ok=True)
        rt = runtime_ads.Runtime(control, instancia="mc-e16").abrir()
        try:
            rt.crear_item(id="it-c", titulo="tarea generacional", motivo="E-16")
            rt.crear_paquete(
                id="pq-c", item="it-c", capacidades_requeridas=list(capacidades),
                orden={"adaptador": "proceso-local", "operacion": "ejecutar",
                       "argumentos": ["sh", "-c", guion_generacional(self.prefijo)],
                       "limite_segundos": segundos})
        finally:
            rt.cerrar()
        return control, espacio

    def despachar_y_capturar(self, argumentos, *, espera=240):
        """Lanza el despacho y MUESTREA los PID mientras la tarea todavía vive.

        Muestrear al final no sirve: si la contención funciona, al terminar no queda nada
        que contar y «no se capturó el bisnieto» sería indistinguible de «el bisnieto nunca
        existió». Se muestrea durante la ventana en que la tarea está viva, que es donde la
        pregunta tiene respuesta.
        """
        import time                                                   # noqa: PLC0415
        proceso = subprocess.Popen(
            [sys.executable, os.path.join(RAIZ_RUNTIME, "ads_runtime.py")]
            + [str(a) for a in argumentos],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.entorno(), cwd=self.taller)
        capturadas = {"raiz": [], "hijo": [], "nieto": [], "bisnieto": []}
        limite = time.monotonic() + espera
        while time.monotonic() < limite:
            visto = generaciones(self.prefijo)
            for generacion, pids in visto.items():
                for pid in pids:
                    if pid not in capturadas[generacion]:
                        capturadas[generacion].append(pid)
            if all(capturadas[g] for g in ("raiz", "hijo", "nieto", "bisnieto")):
                break
            if proceso.poll() is not None and any(capturadas.values()):
                break
            time.sleep(0.2)
        salida, error = proceso.communicate(timeout=espera)
        texto = (salida + error).decode("utf-8", "replace")
        return proceso, capturadas, texto

    def test_T309_el_punto_ejecutable_ACTIVA_la_politica_y_contiene_al_bisnieto(self):
        """T309 · Defecto que previene: `E-16`, una política que nadie puede activar.

        SABOTAJE QUE LA PONE ROJA: retirar `politica_de_contencion=` de `_registro()` en
        `ads_runtime.py`, que es exactamente el estado reproducido antes de corregir.
        """
        if not self.capacidades["fuertes_disponibles"]:
            self.skipTest("este anfitrión no ofrece contención fuerte; el fallo cerrado lo "
                          "cubre la prueba siguiente y el alcance queda en `T309d`")
        control, espacio = self.preparar()
        proceso, capturadas, texto = self.despachar_y_capturar(
            ["--repo", control, "--instancia", "mc-ext", "--adaptador-local", espacio,
             "--contencion", "arbol-de-procesos", "despachar", "pq-c", "--json"])
        for generacion in ("hijo", "nieto", "bisnieto"):
            self.assertTrue(capturadas.get(generacion),
                            "no se capturó el " + generacion + ": la tarea no engendró lo "
                            "que esta prueba dice medir · " + texto[:400])
        # Las tres generaciones cambiaron de grupo: sin eso, medir `killpg` y medir el
        # árbol de procesos darían lo mismo y la prueba no distinguiría los dos niveles.
        self.assertNotEqual(capturadas["hijo"], capturadas["nieto"])
        self.assertNotEqual(capturadas["nieto"], capturadas["bisnieto"])
        todos = (capturadas["raiz"] + capturadas["hijo"] + capturadas["nieto"]
                 + capturadas["bisnieto"])
        vivos = contencion.esperar_a_que_mueran(todos)
        self.assertEqual(vivos, [],
                         "sobrevivió descendencia al camino PRODUCTIVO con política de "
                         "contención: " + str(vivos))

    def test_T309b_sin_backend_fuerte_el_punto_ejecutable_FALLA_CERRADO(self):
        """T309 · Defecto que previene: «caigo al débil y sigo», que es la peor salida.

        Se pide el nivel fuerte con un backend cuyo nivel es INFERIOR. No hay ejecución de
        ninguna clase: se comprueba que la tarea no llegó a engendrar ni una generación.
        """
        control, espacio = self.preparar()
        resultado = self.correr(
            "ads_runtime.py",
            ["--repo", control, "--instancia", "mc-ext", "--adaptador-local", espacio,
             "--contencion", "arbol-de-procesos", "--contencion-backend", "simple",
             "despachar", "pq-c"], espera=240)
        texto = (resultado.stdout + resultado.stderr).decode("utf-8", "replace")
        self.assertEqual(resultado.returncode, 4, texto[:400])
        self.assertIn("CONTENCION_FUERTE_NO_DISPONIBLE", texto)
        self.assertNotIn("Traceback (most recent call last)", texto)
        capturadas = generaciones(self.prefijo)
        self.assertEqual(sum(len(v) for v in capturadas.values()), 0,
                         "se ejecutó algo pese al fallo cerrado: " + str(capturadas))

    def test_T309c_ads_ciclo_tambien_puede_activarla(self):
        """T309 · Defecto que previene: cablearla en un punto ejecutable y no en el otro."""
        ayuda = self.correr("ads_ciclo.py", ["ciclo", "--help"])
        self.assertEqual(ayuda.returncode, 0, ayuda.stderr.decode()[:300])
        texto = ayuda.stdout.decode("utf-8", "replace")
        self.assertIn("--contencion", texto)
        self.assertIn("--contencion-backend", texto)
        # Y no es sólo una opción declarada: el fallo cerrado llega hasta el final.
        control, espacio = self.preparar()
        resultado = self.correr(
            "ads_ciclo.py",
            ["ciclo", "--repo", control, "--instancia", "mc-ext",
             "--adaptador-local", espacio, "--contencion", "arbol-de-procesos",
             "--contencion-backend", "simple"], espera=240)
        salida = (resultado.stdout + resultado.stderr).decode("utf-8", "replace")
        self.assertNotEqual(resultado.returncode, 0, salida[:300])
        self.assertIn("CONTENCION_FUERTE_NO_DISPONIBLE", salida)
        self.assertNotIn("Traceback (most recent call last)", salida)

    def test_T309d_el_ALCANCE_de_este_anfitrion_se_MIDE_y_se_declara(self):
        """T309 · `E-18` · Defecto que previene: afirmar una contención que no se ejerció.

        `E-18` permanece como LIMITACIÓN DE ANFITRIÓN, y su alcance no se adivina: se mide.
        Lo que esta prueba exige es que cada backend diga si está DISPONIBLE y, cuando no lo
        está, POR QUÉ; que un backend no ejercitable NO se cuente como ejercido; y que su
        ausencia no produzca un falso rojo.
        """
        informe = self.capacidades
        por_identificador = {fila["backend"]: fila for fila in informe["backends"]}
        self.assertIn("cgroup-v2", por_identificador,
                      "`cgroup v2` tiene que estar SONDEADO aunque no se pueda ejercer")
        for fila in informe["backends"]:
            with self.subTest(backend=fila["backend"]):
                self.assertTrue(fila["motivo"],
                                "un backend sin motivo no distingue «no está» de «no se "
                                "pudo comprobar»")
                self.assertIn(fila["nivel"], deteccion.NIVELES)
        # Un backend NO disponible no aparece entre los fuertes disponibles: no se cuenta
        # como ejercido. Es la mitad que impide presentar lo no ejercido como certificado.
        for identificador in informe["fuertes_disponibles"]:
            self.assertTrue(por_identificador[identificador]["disponible"])
        for fila in informe["backends"]:
            if not fila["disponible"]:
                self.assertNotIn(fila["backend"], informe["fuertes_disponibles"])
        # Y la ausencia de un backend NO es un rojo: mientras haya alguno fuerte, la
        # política se sirve. Lo que sería rojo es afirmar el que no se ejerció.
        if informe["hay_contencion_fuerte"]:
            elegido, _evidencia = contencion.elegir(
                contencion.Politica(deteccion.ARBOL_DE_PROCESOS), informe)
            self.assertIn(elegido, informe["fuertes_disponibles"])
            self.assertTrue(por_identificador[elegido]["disponible"])

    def test_T309e_ninguna_salida_de_esta_zona_afirma_custodia_productiva(self):
        """T309 · `E-17` · Defecto que previene: llamar custodia a una clave efímera.

        `E-17` permanece EXTERNA. Lo que esta prueba impide es que una salida de esta zona
        afirme lo contrario: se barren el README y el contrato de la raíz externa buscando
        una afirmación de custodia productiva, y se exige que lo que digan sea que NO la hay.
        """
        readme = os.path.join(RAIZ_OPERATIVO, "raiz-externa", "README.md")
        with open(readme, encoding="utf-8") as manejador:
            texto = manejador.read()
        # El REGISTRO que `E-17` exige: propietario, mecanismo previsto y condición de
        # cierre. Se comprueba que están, porque una deuda sin dueño ni cierre no es una
        # deuda: es una frase.
        for exigido in ("CUSTODIA PRODUCTIVA DE CLAVES", "PROPIETARIO",
                        "MECANISMO PREVISTO", "CONDICIÓN DE CIERRE",
                        "no constituyen custodia productiva"):
            with self.subTest(exigido=exigido):
                self.assertIn(exigido, texto,
                              "el README de la raíz externa no registra `E-17`: " + exigido)
        # Y NINGUNA sede de esta zona afirma que la custodia productiva esté resuelta.
        for sede in (readme, os.path.join(RAIZ_RUNTIME, "CONTRATO-RAIZ-EXTERNA.md")):
            with self.subTest(sede=os.path.basename(sede)):
                with open(sede, encoding="utf-8") as manejador:
                    contenido = manejador.read()
                for prohibida in ("custodia productiva RESUELTA",
                                  "custodia productiva implementada",
                                  "custodia productiva certificada"):
                    self.assertNotIn(prohibida, contenido)



# ===========================================================================
#  `T310` · `T311` — LA VENTANA DE PUBLICACIÓN, VISTA POR UN LECTOR CONCURRENTE
#
#  Aparecida AL INTEGRAR los tres ejes, y por eso vive aquí y no en el lote de nadie.
#  `test_continua.py::test_21` —que mata con `SIGKILL` a un escritor real mientras otra
#  instancia lee el mismo paquete en bucle y sin bloqueo— empezó a reventar con
#  `ESTADO_CORRUPTO` diciendo «el fichero fue modificado fuera del diario, o está truncado».
#  Ninguna de las dos cosas era cierta: el lector estaba viendo el objeto NUEVO con la
#  revisión VIEJA, que es la ventana entre el paso 8 y el paso 9.
#
#  La carrera era LATENTE desde el primer corte —el paso 8 ya reemplazaba antes de que el 9
#  publicara— y la corrección de `E-08` la ENSANCHÓ al meter entre los dos el testigo con
#  sus dos `fsync`. Se dice así de claro: no la introdujo el testigo, la hizo visible.
#
#  Las dos pruebas son las dos mitades, y hacen falta las dos. Una sola que exigiera «no
#  revientes» se satisfaría devolviendo el objeto nuevo —publicar una transición que aún
#  puede revertirse—, y una sola que exigiera «revienta» volvería a dar el diagnóstico
#  falso. Juntas fijan que la ventana y la corrupción se distinguen y NINGUNA devuelve
#  contenido.
#
#  `H-02` · POR QUÉ LOS DOS DOCSTRINGS EMPIEZAN POR SU IDENTIFICADOR, DESDE EL 2026-09-04
#      La auditoría independiente midió que `T310` y `T311` declaraban `estado:
#      prueba-superada` sobre `evidencia/integridad-evidencia-salida.txt`, un fichero que
#      NO LOS NOMBRABA: `grep -oE "^T[0-9]+" integridad-evidencia-salida.txt` publicaba
#      `T306 T307 T308 T309 T330 … T337` y ninguno de estos dos. La derivación del estado
#      —`validadores/registro_pruebas.py`— sacaba `prueba-ejecutada`, escribía el motivo y
#      LO DESCARTABA por no ser contrastable, y así los dos subían de estado por argumento.
#      La causa era de FORMA y estaba aquí: `unittest` imprime la primera línea del
#      docstring bajo el nombre del caso, todas las demás pruebas de esta batería la
#      empiezan por su identificador, y estas dos no lo hacían. Se corrige donde estaba el
#      defecto —la salida no nombraba lo que sí había ejecutado— y no bajando el estado:
#      bajarlo habría sido correcto y habría escondido que la ejecución EXISTE.
#      Los otros doce escenarios que `H-02` destapó no se pueden cerrar así desde aquí
#      —sus baterías son otras—, y a ésos se les baja el estado al derivado, que es el dato.
# ===========================================================================
class LaVentanaDePublicacion(unittest.TestCase):

    def _almacen(self):
        import estado
        espacio = tempfile.mkdtemp(prefix="ads-ventana-")
        self.addCleanup(shutil.rmtree, espacio, ignore_errors=True)
        os.makedirs(espacio, exist_ok=True)
        almacen = estado.inicializar(espacio)
        almacen.aplicar(estado.Transicion(
            tipo="prueba", base=almacen.revision()["revision_id"],
            operaciones=[estado.Escritura(
                "paquetes/pq-ventana.json",
                {"esquema": "ads.estado/1", "id": "pq-ventana", "estado": "listo"})],
            autor="prueba-de-la-ventana", motivo="fundar el objeto que se va a leer",
            id="tx-alta-ventana"))
        return almacen

    def _sustituir_el_objeto_sin_publicar_la_revision(self, almacen, nuevo):
        """Deja el disco EXACTAMENTE como lo deja el paso 8, y no ejecuta el paso 9."""
        from estado.serializacion import cid, serializar_canonico
        destino = almacen._d.ruta_canonica("paquetes/pq-ventana.json")
        datos = serializar_canonico(nuevo)
        with open(destino, "wb") as manejador:
            manejador.write(datos)
        return cid(datos)

    def test_T310_la_ventana_de_publicacion_NO_se_diagnostica_como_corrupcion(self):
        """T310 · `E-08` bis · el objeto es el que el testigo dice haber publicado.

        Se reproduce la ventana con fidelidad: el objeto nuevo en `canonico/`, el TESTIGO del
        paso 8 escrito con ese mismo `cid`, y `REVISION.json` todavía en la revisión
        anterior. El lector NO puede devolver contenido —seguiría siendo publicar una
        transición reversible— y NO puede llamarlo corrupción, porque el remedio de una
        cosa y de la otra son distintos: aquí se RECUPERA, allí se investiga un fichero.
        """
        from estado.errores import PublicacionEnVuelo
        from estado.rutas import TESTIGO_DE_PUBLICACION
        from estado.serializacion import serializar_canonico
        almacen = self._almacen()
        nuevo = {"esquema": "ads.estado/1", "id": "pq-ventana", "estado": "ejecutando"}
        cid_nuevo = self._sustituir_el_objeto_sin_publicar_la_revision(almacen, nuevo)

        zona = almacen._d.zona_tx("tx-de-la-ventana")
        os.makedirs(zona, exist_ok=True)
        with open(os.path.join(zona, TESTIGO_DE_PUBLICACION), "wb") as manejador:
            manejador.write(serializar_canonico({
                "esquema": 1, "transaccion": "tx-de-la-ventana", "resultado": "publicado",
                "publicados": {"paquetes/pq-ventana.json": cid_nuevo}}))

        with self.assertRaises(PublicacionEnVuelo) as capturado:
            almacen.leer("paquetes/pq-ventana.json")
        self.assertEqual(capturado.exception.codigo, "PUBLICACION_EN_VUELO")
        self.assertIn("tx-de-la-ventana", str(capturado.exception))
        self.assertIn("COMPLETAR", str(capturado.exception))

    def test_T311_sin_testigo_que_lo_avale_sigue_siendo_ESTADO_CORRUPTO(self):
        """T311 · El control que impide que la corrección de `T310` se coma la corrupción.

        Mismo disco alterado, y NINGÚN testigo que diga que esa transacción publicó ese
        `cid`. Es una modificación fuera del diario, y el diagnóstico tiene que seguir
        siendo ése: sin esta mitad, `T310` se satisfaría llamando «ventana» a cualquier
        fichero que no case, que es la degradación silenciosa que este encargo persigue.
        """
        from estado.errores import EstadoCorrupto, PublicacionEnVuelo
        almacen = self._almacen()
        self._sustituir_el_objeto_sin_publicar_la_revision(
            almacen, {"esquema": "ads.estado/1", "id": "pq-ventana", "estado": "alterado"})
        with self.assertRaises(EstadoCorrupto) as capturado:
            almacen.leer("paquetes/pq-ventana.json")
        self.assertNotIsInstance(capturado.exception, PublicacionEnVuelo)
        self.assertEqual(capturado.exception.codigo, "ESTADO_CORRUPTO")
        self.assertIn("fuera del diario", str(capturado.exception))


# ===========================================================================
#  T330 · T337 — `ADJ-B2` · LA PURGA `E-10` EN TODA LA RAÍZ EXTERNA
# ===========================================================================
class PurgaEnLaRaizExterna(SesionNueva):
    """`ADJ-B2`. La contaminación del entorno, en la única pieza que `O26` §1 juzga.

    HECHO REPRODUCIDO ANTES DE CORREGIR, con `json.py` homónimo en `PYTHONPATH` y desde un
    `cwd` ajeno:

        verificador.py capacidades           → {}          EXIT=0  (sano: las nueve)
        instalar.py --destino … --arbol …    → {}          EXIT=0  manifiesto 3 BYTES
                                                                   (sano: 6 734) y 41
                                                                   ficheros instalados igual
        … --comprobar sobre esa instalación  → KeyError: 'ficheros'  EXIT=1, cuatro rutas
                                                                   absolutas del anfitrión
        grep de purga sobre TODO raiz-externa/                       CERO líneas
        `T306` EJECUTABLES                                           cinco, y ninguno más

    Es el MISMO defecto que el árbol declaraba cerrado para los cinco `ads_*.py`, e incumple
    la condición 8 de `O26` §1 —«contaminación del entorno falla cerrado»—, que era la única
    de las ocho sin cumplir.
    """

    PAQUETE = os.path.join(RAIZ_OPERATIVO, "raiz-externa")
    VERIFICADOR = os.path.join(PAQUETE, "verificador.py")
    INSTALADOR = os.path.join(PAQUETE, "instalar.py")

    # ------------------------------------------------------------------ utilidades
    def paquete_envenenado(self):
        """Un `json` homónimo que, si se importa, deja FICHERO TESTIGO y falsea la salida.

        Es el mismo veneno de `T306`: `json.dumps` sustituido publica lo que quiera, y eso
        es literalmente lo que produjo el `{}` con código 0 y el manifiesto de tres bytes.
        """
        veneno = os.path.join(self.taller, "veneno")
        os.makedirs(veneno, exist_ok=True)
        self.testigo = os.path.join(self.taller, "IMPORTADO-EL-HOMONIMO")
        cuerpo = (
            "import sys\n"
            "with open(" + repr(self.testigo) + ", 'a') as _m:\n"
            "    _m.write(__name__ + '\\n')\n"
            "sys.stderr.write('HOMONIMO MALICIOSO IMPORTADO: ' + __name__ + '\\n')\n"
        )
        with open(os.path.join(veneno, "json.py"), "w", encoding="utf-8") as manejador:
            manejador.write(cuerpo + "\ndef dumps(*a, **k):\n    return '{}'\n"
                            "def loads(*a, **k):\n    return {}\n"
                            "def load(*a, **k):\n    return {}\n"
                            "def dump(o, f, *a, **k):\n    f.write('{}')\n")
        for paquete in ("errores", "firma", "atestacion", "instalar", "aislamiento",
                        "admision", "estado", "identidad", "gobierno"):
            carpeta = os.path.join(veneno, paquete)
            os.makedirs(carpeta, exist_ok=True)
            with open(os.path.join(carpeta, "__init__.py"), "w",
                      encoding="utf-8") as manejador:
                manejador.write(cuerpo)
        return veneno

    def correr_ruta(self, camino, argumentos, *, extra=None, cwd=None, espera=300):
        return subprocess.run(
            [sys.executable, camino] + [str(a) for a in argumentos],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.entorno(extra), cwd=cwd or self.taller, check=False, timeout=espera,
        )

    def prologo_de(self, fuente):
        """El bloque `E-10` de un punto ejecutable, del encabezado al `SystemExit(5)`."""
        inicio = fuente.index("#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA")
        fin = fuente.index("    raise SystemExit(5)\n", inicio) + len(
            "    raise SystemExit(5)\n")
        return fuente[inicio:fin]

    # ------------------------------------------------------------------ T330
    def test_T330_el_inventario_se_DERIVA_del_arbol_ENTERO_y_es_coherente(self):
        """T330 · Defecto que previene: `ADJ-B2` y `H-03`, un inventario que no ve una zona.

        La equivalencia, comprobada EN LOS DOS SENTIDOS sobre el disco y sobre el ÁRBOL
        ENTERO —no sobre dos zonas escritas a mano—:

            lleva `#!`   ⟺   es INVOCABLE   ⟺   lleva el MECANISMO `E-10`

        Un punto ejecutable nuevo sin purga la rompe; un módulo de biblioteca que se
        disfrace de ejecutable, también; y una zona nueva ya no puede ser invisible, porque
        el recorrido no conoce zonas: conoce el árbol.

        SABOTAJE QUE LA PONE ROJA: retirar la purga de CUALQUIERA de los puntos
        —`raiz-externa/verificador.py` (`N330`) o `validadores/huella.py` (`NH01`)—, o
        volver a acotar el recorrido a un par de zonas escritas (`NH03`).

        DESDE `D-01`, EL ALCANCE SON 56 Y NO 35. La exclusión por zona `motivo: "bateria"`
        se ha retirado: las veintiuna baterías de `runtime/pruebas/` y `tooling/tests/` son
        puntos ejecutables como cualquier otro y se les exige lo mismo.
        """
        puntos, excluidos = inventariar_el_arbol()
        self.assertTrue(puntos, "el inventario salió vacío: no estaría midiendo nada")
        # 1 · NINGÚN `.py` del árbol queda sin clasificar. Es la propiedad que `H-03` pedía:
        #     lo que no está en el inventario tiene que estar excluido POR UNA CLASE, no
        #     ausente. Se recuenta contra el disco, no contra el propio inventario.
        del_disco = set()
        for dirpath, dirnames, filenames in os.walk(RAIZ_REPO):
            dirnames[:] = sorted(d for d in dirnames
                                 if d not in DIRECTORIOS_QUE_NO_SON_CORPUS)
            for nombre in filenames:
                if nombre.endswith(".py"):
                    del_disco.add(os.path.relpath(os.path.join(dirpath, nombre), RAIZ_REPO)
                                  .replace(os.sep, "/"))
        self.assertEqual(del_disco, set(puntos) | set(excluidos),
                         "hay ficheros `.py` del árbol que el inventario no clasifica: "
                         + repr(sorted(del_disco - set(puntos) - set(excluidos))))
        self.assertFalse(set(puntos) & set(excluidos),
                         "algún fichero está a la vez dentro y fuera del inventario")
        # 2 · la equivalencia, en los dos sentidos, sobre cada punto ejecutable.
        for ruta, senales in sorted(puntos.items()):
            with self.subTest(punto=ruta):
                self.assertTrue(senales["interprete"],
                                ruta + " es invocable y no lleva línea de intérprete")
                self.assertTrue(senales["invocable"],
                                ruta + " está en el inventario y no es invocable")
                self.assertTrue(senales["purga"],
                                ruta + " es un punto ejecutable SIN la purga `E-10`")
                self.assertIsNotNone(senales["mecanismo"],
                                     ruta + " llama a la purga y no lleva su MECANISMO")
        # 3 · y los treinta y tantos llevan el MISMO MECANISMO, byte a byte. Copiado, no
        #     adaptado. El recital de encima es de cada sede y no entra: ver la DECISIÓN
        #     escrita junto a `mecanismo_de_la_purga`.
        digests = {}
        for ruta, senales in sorted(puntos.items()):
            digests.setdefault(
                hashlib.sha256(senales["mecanismo"].encode("utf-8")).hexdigest(),
                []).append(ruta)
        self.assertEqual(len(digests), 1,
                         "los mecanismos `E-10` han divergido entre puntos ejecutables: "
                         + repr({d[:12]: r for d, r in digests.items()}))
        # 4 · CONTROL DEL CONTROL: el recorrido llega DE VERDAD a cada zona en la que hay
        #     un punto ejecutable. Sin esto, «todos cumplen» se explicaría por un inventario
        #     que sólo mira donde ya sabíamos que se cumple, que es literalmente `H-03`.
        for canario in ("kernel/operativo/runtime/ads_admision.py",
                        "kernel/operativo/raiz-externa/verificador.py",
                        "kernel/operativo/validadores/huella.py",
                        "kernel/operativo/validadores/comprobar_integridad.py",
                        "tooling/workspace.py",
                        "docs/canonico/validar-fuentes-canonicas.py",
                        "docs/f5/validar-f5.py",
                        "docs/evolucion/verificacion/derivar-universo-obligatorio.py",
                        # `D-01`: las dos zonas de baterías, que estaban EXENTAS por su
                        # domicilio y ahora son puntos ejecutables como los demás.
                        "kernel/operativo/runtime/pruebas/test_admision.py",
                        "tooling/tests/test_workspace.py"):
            self.assertIn(canario, puntos,
                          "el inventario no ve " + canario + ": el recorrido no alcanza su "
                          "zona, que es el defecto de `H-03`")
        self.assertGreaterEqual(len(puntos), 50)
        self.assertGreaterEqual(
            len({senales["zona"] for senales in puntos.values()}), 8,
            "el inventario cubre menos de ocho zonas: volvió a estrecharse")
        # 5 · `D-01` · NINGUNA ZONA DE BATERÍAS QUEDA EXENTA. Se derivan del disco —igual
        #     que antes— pero ya no para EXIMIR, sino para comprobar que todo lo invocable
        #     que vive en ellas está DENTRO del inventario. La exclusión por domicilio era
        #     la lista escrita a mano de `ADJ-B2`, sólo que escrita por directorios.
        self.assertNotIn("bateria", MOTIVOS_DE_EXCLUSION,
                         "ha vuelto la exclusión por zona que `D-01` retiró")
        zonas = zonas_de_baterias(RAIZ_REPO)
        self.assertTrue(zonas, "no se derivó ninguna zona de baterías del disco")
        for zona in sorted(zonas):
            de_la_zona = [ruta for ruta, senales in puntos.items()
                          if os.path.realpath(os.path.dirname(senales["completa"])) == zona]
            self.assertTrue(de_la_zona,
                            "la zona de baterías " + zona + " no aporta ni un punto "
                            "ejecutable al inventario: ha vuelto a quedar exenta")

    def test_T330b_cada_exclusion_esta_DECLARADA_con_su_motivo_y_SE_COMPRUEBA(self):
        """T330 · Defecto que previene: un alcance que se estrecha sin que se note.

        Lo que queda fuera del inventario tiene que quedar fuera por una razón DECLARADA y
        CIERTA, no por descuido. Cada clase de exclusión tiene su motivo escrito en
        `MOTIVOS_DE_EXCLUSION` y aquí se comprueba su PREDICADO contra el disco, de forma
        independiente de la clasificación que hizo el inventario.

        SABOTAJE QUE LA PONE ROJA: darle a un módulo de biblioteca una línea de intérprete
        para colarlo fuera del inventario, o llamar `pruebas/` a un directorio que no
        contiene baterías para sacar de él lo que sea.
        """
        puntos, excluidos = inventariar_el_arbol()
        self.assertTrue(excluidos, "no hay ninguna exclusión: no estaría midiendo nada")
        residuales = []
        for ruta, senales in sorted(excluidos.items()):
            motivo = senales["motivo"]
            with self.subTest(excluido=ruta, motivo=motivo):
                self.assertIn(motivo, MOTIVOS_DE_EXCLUSION,
                              ruta + " está excluido por un motivo que nadie declara")
                if motivo == "biblioteca-de-paquete":
                    self.assertFalse(senales["invocable"],
                                     ruta + " es invocable y está fuera como biblioteca")
                    self.assertTrue(
                        os.path.isfile(os.path.join(os.path.dirname(senales["completa"]),
                                                    "__init__.py")),
                        ruta + " se excluyó como módulo de paquete y su directorio no es un "
                               "paquete")
                    if senales["interprete"]:
                        residuales.append(ruta)
                else:
                    self.assertFalse(senales["invocable"],
                                     ruta + " es invocable y está fuera como biblioteca")
                    self.assertFalse(
                        senales["interprete"],
                        ruta + " no es invocable, no vive en un paquete y lleva línea de "
                               "intérprete: es la ambigüedad que `ADJ-B2` retiró de "
                               "`errores.py`, `firma.py`, `atestacion.py` y "
                               "`aislamiento.py`")
        # `D-01` · LA DEUDA DE LAS BATERÍAS ESTÁ PAGADA, Y ESTO ES SU CLIQUET. Donde antes
        # se comprobaba que la ÚNICA batería con mecanismo no lo perdiera, ahora se
        # comprueba que NINGUNA batería vuelva a estar excluida: esta misma es un punto
        # ejecutable del inventario, con el mecanismo `E-10` y con la guarda `G-03`.
        yo = os.path.relpath(os.path.abspath(__file__), RAIZ_REPO).replace(os.sep, "/")
        self.assertNotIn(yo, excluidos,
                         "esta batería ha vuelto a quedar EXCLUIDA del inventario: es la "
                         "exención por domicilio que `D-01` retiró")
        self.assertIn(yo, puntos, "esta batería no aparece como punto ejecutable")
        self.assertIsNotNone(puntos[yo]["mecanismo"],
                             "esta batería ha perdido el MECANISMO `E-10`")
        self.assertIsNotNone(puntos[yo]["mecanismo_g03"],
                             "esta batería ha perdido la GUARDA `G-03`")
        self.assertTrue(residuales, "ningún módulo de paquete conserva línea de intérprete "
                                    "residual: si de verdad se retiraron todas, este "
                                    "recuento sobra y esta rama hay que quitarla")


    # ------------------------------------------------------------------ T331
    def test_T331_la_raiz_externa_no_se_falsea_desde_el_PYTHONPATH(self):
        """T331 · Defecto que previene: `capacidades` publicando `{}` con código 0.

        Control SANO y control ENVENENADO sobre el mismo binario, y se exige que la salida
        sea la MISMA: las nueve condiciones de certificación, con `disponible` verdadero.
        """
        sano = self.correr_ruta(self.VERIFICADOR, ["capacidades"])
        self.assertEqual(sano.returncode, 0, sano.stderr.decode())
        limpio = json.loads(sano.stdout.decode("utf-8"))
        self.assertEqual(len(limpio["condiciones_de_certificacion"]), 9)

        veneno = self.paquete_envenenado()
        envenenado = self.correr_ruta(self.VERIFICADOR, ["capacidades"],
                                      extra={"PYTHONPATH": veneno + os.pathsep + "."},
                                      cwd=veneno)
        self.assertEqual(envenenado.returncode, 0, envenenado.stderr.decode())
        sucio = json.loads(envenenado.stdout.decode("utf-8"))
        self.assertEqual(sucio["condiciones_de_certificacion"],
                         limpio["condiciones_de_certificacion"],
                         "el entorno cambió las condiciones que la raíz externa publica")
        self.assertTrue(sucio["condiciones_de_certificacion"],
                        "`capacidades` volvió a publicar el vacío")
        self.assertNotIn(b"HOMONIMO MALICIOSO", envenenado.stderr)
        self.assertFalse(os.path.exists(self.testigo),
                         "la raíz externa importó un homónimo del entorno")
        self.assertEqual(sucio["procedencia"]["entradas_del_lanzador_presentes"], 0,
                         "quedaron entradas del lanzador en la ruta de importación")
        for nombre, origen in sorted(sucio["procedencia"]["modulos"].items()):
            self.assertTrue(origen.startswith("instalacion:"),
                            nombre + " no vino de la instalación: " + origen)

    def test_T331b_el_instalador_no_escribe_un_manifiesto_truncado(self):
        """T331 · Defecto que previene: 41 ficheros instalados y un manifiesto de 3 bytes.

        La instalación sana y la instalación con el entorno envenenado tienen que producir
        el MISMO manifiesto, byte a byte: es la propiedad `I-g3` que el propio instalador
        declara —«dos instalaciones del mismo árbol producen el MISMO manifiesto»—, y era
        justo la que el entorno rompía.
        """
        veneno = self.paquete_envenenado()
        sano = os.path.join(self.taller, "sana")
        sucio = os.path.join(self.taller, "sucia")
        primero = self.correr_ruta(self.INSTALADOR,
                                   ["--destino", sano, "--arbol", RAIZ_REPO])
        self.assertEqual(primero.returncode, 0, primero.stderr.decode())
        segundo = self.correr_ruta(self.INSTALADOR,
                                   ["--destino", sucio, "--arbol", RAIZ_REPO],
                                   extra={"PYTHONPATH": veneno + os.pathsep + "."},
                                   cwd=veneno)
        self.assertEqual(segundo.returncode, 0, segundo.stderr.decode())
        manifiesto_sano = bytes_de_fichero(
            os.path.join(sano, "MANIFIESTO-DE-INSTALACION.json"))
        manifiesto_sucio = bytes_de_fichero(
            os.path.join(sucio, "MANIFIESTO-DE-INSTALACION.json"))
        self.assertGreater(len(manifiesto_sano), 1000,
                           "el manifiesto sano no cubre la instalación")
        self.assertEqual(manifiesto_sucio, manifiesto_sano,
                         "el entorno cambió el manifiesto de la instalación")
        self.assertFalse(os.path.exists(self.testigo))
        # Y la instalación hecha bajo veneno se comprueba SIN veneno y sale intacta: ése es
        # el paso que antes moría con `KeyError: 'ficheros'`.
        comprobacion = self.correr_ruta(
            self.INSTALADOR, ["--destino", sucio, "--arbol", RAIZ_REPO, "--comprobar"])
        self.assertEqual(comprobacion.returncode, 0, comprobacion.stderr.decode())
        self.assertTrue(json.loads(comprobacion.stdout.decode("utf-8"))["ok"])

    # ------------------------------------------------------------------ T332
    def test_T332_un_manifiesto_truncado_se_rechaza_TIPADO(self):
        """T332 · Defecto que previene: `KeyError: 'ficheros'` con cuatro rutas del anfitrión.

        Un manifiesto que no cubre nada es una instalación ALTERADA —lo que `V6-16` obliga a
        rechazar— y no un defecto de programación del comprobador. Tres formas de estar
        truncado, y las tres tienen que salir tipadas y sin traza.
        """
        destino = os.path.join(self.taller, "instalacion")
        primero = self.correr_ruta(self.INSTALADOR,
                                   ["--destino", destino, "--arbol", RAIZ_REPO])
        self.assertEqual(primero.returncode, 0, primero.stderr.decode())
        manifiesto = os.path.join(destino, "MANIFIESTO-DE-INSTALACION.json")
        for nombre, contenido in (("vacío", "{}\n"),
                                  ("sin ficheros", '{"esquema": 1}\n'),
                                  ("lista vacía", '{"esquema": 1, "ficheros": []}\n')):
            with self.subTest(manifiesto=nombre):
                with open(manifiesto, "w", encoding="utf-8") as manejador:
                    manejador.write(contenido)
                proceso = self.correr_ruta(
                    self.INSTALADOR,
                    ["--destino", destino, "--arbol", RAIZ_REPO, "--comprobar"])
                self.assertEqual(proceso.returncode, 1,
                                 nombre + ": un manifiesto truncado no salió como fallo")
                salida = proceso.stdout.decode() + proceso.stderr.decode()
                self.assertNotIn("Traceback", salida, nombre + ": salió una traza")
                self.assertNotIn("KeyError", salida)
                self.assertIn("INSTALACION_ALTERADA", salida,
                              nombre + ": el fallo no llegó tipado")
                self.assertNotIn(os.path.realpath(RAIZ_REPO), salida,
                                 nombre + ": la salida publicó una ruta del anfitrión")

    # ------------------------------------------------------------------ T333
    def test_T333_no_se_instala_a_medias(self):
        """T333 · Defecto que previene: un destino con parte de los ficheros y sin manifiesto.

        Se instala contra un `runtime` al que le falta una dependencia. El destino tiene que
        quedar AUSENTE por completo si no había instalación previa, y ENTERO Y VÁLIDO si la
        había: nunca a medias, que era lo que dejaba el `rmtree` + copia encima.
        """
        sys.path.insert(0, self.PAQUETE)
        try:
            import instalar as modulo_de_instalacion         # noqa: PLC0415
        finally:
            sys.path.remove(self.PAQUETE)

        cojo = os.path.join(self.taller, "runtime-cojo")
        os.makedirs(cojo)
        for paquete in modulo_de_instalacion.DEPENDENCIAS[:-1]:
            shutil.copytree(os.path.join(RAIZ_RUNTIME, paquete),
                            os.path.join(cojo, paquete),
                            ignore=shutil.ignore_patterns("__pycache__"))
        que_falta = modulo_de_instalacion.DEPENDENCIAS[-1]

        # 1 · sin instalación previa: el destino NO queda.
        destino = os.path.join(self.taller, "instalacion")
        with self.assertRaises(Exception) as capturado:
            modulo_de_instalacion.instalar(destino, arbol_verificado=RAIZ_REPO,
                                           runtime=cojo)
        self.assertIn(que_falta, str(capturado.exception))
        self.assertFalse(os.path.exists(destino),
                         "quedó una instalación a medias en el destino")
        for residuo in (destino + modulo_de_instalacion.SUFIJO_EN_CURSO,
                        destino + modulo_de_instalacion.SUFIJO_ANTERIOR):
            self.assertFalse(os.path.exists(residuo),
                             "quedó la zona de construcción: " + os.path.basename(residuo))

        # 2 · con instalación previa: la previa sobrevive ENTERA y sigue comprobando.
        buena = modulo_de_instalacion.instalar(destino, arbol_verificado=RAIZ_REPO,
                                               runtime=RAIZ_RUNTIME)
        antes = bytes_de_fichero(buena["manifiesto"])
        with self.assertRaises(Exception):
            modulo_de_instalacion.instalar(destino, arbol_verificado=RAIZ_REPO,
                                           runtime=cojo)
        self.assertTrue(os.path.isdir(destino), "la instalación previa desapareció")
        self.assertEqual(bytes_de_fichero(buena["manifiesto"]), antes,
                         "el intento fallido tocó el manifiesto de la instalación previa")
        self.assertTrue(
            modulo_de_instalacion.verificar_instalacion(destino)["ok"],
            "el intento fallido dejó la instalación previa sin casar con su manifiesto")

    # ------------------------------------------------------------------ T334
    def test_T334_un_repo_ajeno_no_aporta_el_codigo_que_lo_verifica(self):
        """T334 · Defecto que previene: `g.15`, que el árbol verificado decida cómo se le
        verifica.

        Se instala la raíz externa desde ESTE árbol y se le pide juzgar OTRO repositorio que
        trae dentro su propio `kernel/operativo/raiz-externa/` y su propio
        `runtime/admision/`, los dos envenenados. La procedencia publicada tiene que decir
        que todo salió de la instalación, y el testigo del veneno no puede aparecer.
        """
        destino = os.path.join(self.taller, "instalacion")
        instalacion = self.correr_ruta(self.INSTALADOR,
                                       ["--destino", destino, "--arbol", RAIZ_REPO])
        self.assertEqual(instalacion.returncode, 0, instalacion.stderr.decode())
        verificador = os.path.join(destino, "raiz-externa", "verificador.py")

        ajeno = os.path.join(self.taller, "repo-ajeno")
        testigo = os.path.join(self.taller, "INTRUSO-DEL-REPO-AJENO")
        cuerpo = "open(" + repr(testigo) + ", 'a').close()\n"
        for relativa in (("kernel", "operativo", "raiz-externa"),
                         ("kernel", "operativo", "runtime", "admision")):
            carpeta = os.path.join(ajeno, *relativa)
            os.makedirs(carpeta, exist_ok=True)
            with open(os.path.join(carpeta, "__init__.py"), "w",
                      encoding="utf-8") as manejador:
                manejador.write(cuerpo)
            for modulo in ("errores.py", "firma.py", "instalar.py", "verificador.py"):
                with open(os.path.join(carpeta, modulo), "w",
                          encoding="utf-8") as manejador:
                    manejador.write(cuerpo)

        proceso = self.correr_ruta(verificador, ["procedencia", "--repo", ajeno],
                                   cwd=os.path.join(ajeno, "kernel", "operativo",
                                                    "raiz-externa"))
        self.assertEqual(proceso.returncode, 0, proceso.stderr.decode())
        datos = json.loads(proceso.stdout.decode("utf-8"))
        for nombre, origen in sorted(datos["modulos"].items()):
            with self.subTest(modulo=nombre):
                self.assertTrue(origen.startswith("instalacion:"),
                                nombre + " no vino de la instalación: " + origen)
        self.assertFalse(datos["repo_es_el_arbol_del_aparato"],
                         "el repo ajeno se confundió con el árbol de la instalación")
        self.assertFalse(os.path.exists(testigo),
                         "la raíz externa importó código del repositorio que juzgaba")
        # Y ninguna ruta absoluta del anfitrión viaja en la salida publicable.
        self.assertNotIn(os.path.realpath(RAIZ_REPO),
                         json.dumps(datos, ensure_ascii=False))

    # ------------------------------------------------------------------ T335
    def test_T335_los_argumentos_obligatorios_ausentes_fallan_por_USO(self):
        """T335 · Defecto que previene: juzgar «lo que haya» cuando no se dice qué juzgar.

        `--repo`, `--configuracion` y `--evidencia` no tienen valor por omisión, y su
        ausencia no puede resolverse con el `cwd`. Se exige código 2 —uso incorrecto, que es
        distinto de «el veredicto no fue favorable»— y ninguna traza.
        """
        casos = (
            ("verificar sin --repo", self.VERIFICADOR,
             ["verificar", "--base", "HEAD", "--configuracion", "x", "--evidencia", "y"]),
            ("comprobar sin --evidencia", self.VERIFICADOR,
             ["comprobar", "--repo", self.taller, "--configuracion", "x"]),
            ("instalar sin --arbol", self.INSTALADOR, ["--destino", self.taller]),
            ("instalar sin --destino", self.INSTALADOR, ["--arbol", RAIZ_REPO]),
        )
        for nombre, camino, argumentos in casos:
            with self.subTest(caso=nombre):
                proceso = self.correr_ruta(camino, argumentos)
                self.assertEqual(proceso.returncode, 2,
                                 nombre + ": un argumento obligatorio ausente no dio "
                                 "«uso incorrecto»")
                salida = proceso.stdout.decode() + proceso.stderr.decode()
                self.assertNotIn("Traceback", salida)

    # ------------------------------------------------------------------ T336
    def test_T336_CONTROL_DEL_CONTROL_sin_la_purga_el_veneno_SI_entra(self):
        """T336 · CONTROL DEL CONTROL: se retira la purga y se mira qué se pone rojo.

        Sin esto, «no se importó el homónimo» se explicaría igual de bien por un veneno que
        no funciona. Se copia el paquete a una instalación, se le QUITA el prólogo `E-10` al
        verificador —que es exactamente el estado del árbol antes de esta corrección— y se
        comprueba que entonces el homónimo SÍ entra y la salida SÍ se falsea.
        """
        veneno = self.paquete_envenenado()
        destino = os.path.join(self.taller, "instalacion")
        instalacion = self.correr_ruta(self.INSTALADOR,
                                       ["--destino", destino, "--arbol", RAIZ_REPO])
        self.assertEqual(instalacion.returncode, 0, instalacion.stderr.decode())
        verificador = os.path.join(destino, "raiz-externa", "verificador.py")

        con_purga = self.correr_ruta(verificador, ["capacidades"],
                                     extra={"PYTHONPATH": veneno + os.pathsep + "."},
                                     cwd=veneno)
        self.assertEqual(con_purga.returncode, 0, con_purga.stderr.decode())
        self.assertEqual(
            len(json.loads(con_purga.stdout.decode())["condiciones_de_certificacion"]), 9)
        self.assertFalse(os.path.exists(self.testigo))

        fuente = texto_de_fichero(verificador)
        prologo = self.prologo_de(fuente)
        with open(verificador, "w", encoding="utf-8") as manejador:
            manejador.write(fuente.replace(
                prologo,
                "def _purgar_la_ruta_de_importacion():\n    return []\n\n"
                "RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()\n", 1))
        sin_purga = self.correr_ruta(verificador, ["capacidades"],
                                     extra={"PYTHONPATH": veneno + os.pathsep + "."},
                                     cwd=veneno)
        entro = (b"HOMONIMO MALICIOSO" in sin_purga.stderr
                 or os.path.exists(self.testigo)
                 or sin_purga.stdout.decode().strip() in ("{}", ""))
        self.assertTrue(entro,
                        "sin la purga el veneno tampoco entra: esta prueba no estaría "
                        "midiendo la purga. stdout=" + sin_purga.stdout.decode()[:200])

    # ------------------------------------------------------------------ T337
    def test_T337_la_procedencia_no_fiable_es_FALLO_CERRADO(self):
        """T337 · Defecto que previene: emitir veredicto sin poder demostrar la procedencia.

        `O26` §1, condición 8. Se instala la raíz externa y se le SUSTITUYE un módulo del
        aparato por uno que vive fuera de la instalación, de modo que la purga no lo puede
        impedir —no viene del lanzador— y sólo la comprobación de procedencia lo caza. El
        proceso tiene que salir con el código de procedencia y NO emitir nada.
        """
        destino = os.path.join(self.taller, "instalacion")
        instalacion = self.correr_ruta(self.INSTALADOR,
                                       ["--destino", destino, "--arbol", RAIZ_REPO])
        self.assertEqual(instalacion.returncode, 0, instalacion.stderr.decode())
        verificador = os.path.join(destino, "raiz-externa", "verificador.py")

        fuera = os.path.join(self.taller, "fuera-de-la-instalacion")
        os.makedirs(fuera)
        shutil.copy(os.path.join(destino, "raiz-externa", "firma.py"),
                    os.path.join(fuera, "firma.py"))
        fuente = texto_de_fichero(verificador)
        # El módulo se importa desde FUERA de la instalación, sin pasar por el lanzador:
        # es la mitad que la purga no puede cubrir y la comprobación sí.
        ancla = "import atestacion as modulo_de_atestacion"
        with open(verificador, "w", encoding="utf-8") as manejador:
            manejador.write(fuente.replace(
                ancla, "sys.path.insert(0, " + repr(fuera) + ")\n" + ancla, 1))
        proceso = self.correr_ruta(verificador, ["capacidades"])
        self.assertEqual(proceso.returncode, 5,
                         "una procedencia no demostrable no salió con su código propio")
        self.assertIn("PROCEDENCIA_NO_FIABLE", proceso.stderr.decode())
        self.assertEqual(proceso.stdout.decode().strip(), "",
                         "se publicó algo pese a no poder demostrar la procedencia")


# ===========================================================================
#  T380 – T397 · `G-03` y `D-01` · EL AISLAMIENTO DE ARRANQUE, ATACADO
# ===========================================================================
#  QUÉ CIERRAN Y POR QUÉ ESTÁN AQUÍ Y NO EN OTRA BATERÍA. `G-03` es de la misma clase que
#  `E-10` —de dónde sale el código con el que se juzga— y se mide con el mismo inventario
#  derivado, que vive en este fichero. `D-01` es el canal que PRODUCE la evidencia, y el
#  comprobador de esa evidencia ya se ejercita aquí (`T307`). Partirlos habría dejado la
#  propiedad en trozos que por separado no demuestran nada.
#
#  EL ATAQUE QUE SEPARA «LO ARREGLÉ» DE «CREO QUE LO ARREGLÉ». Un `sitecustomize.py` que
#  sustituye `hashlib.sha256` y DEJA UN TESTIGO EN DISCO al ejecutarse. Se exige las dos
#  mitades: que el testigo APAREZCA sobre la versión sin guarda —si no apareciera, la
#  prueba no estaría midiendo nada— y que NO APAREZCA por la vía oficial. Mirar sólo el
#  valor publicado no bastaría: un valor correcto es compatible con «el gancho corrió y no
#  le tocó el turno».
#
#  `G-03` · LA GUARDA SE EXIGE A TODO PUNTO EJECUTABLE DEL INVENTARIO DERIVADO, SIN EXENCIÓN
#      Aquí hubo una zona declarada: los cuatro ejecutables de `docs/evolucion/verificacion/`
#      quedaban fuera porque `G-01`, `G-02` y `G-07` estaban abiertos sobre esos mismos
#      ficheros y dos pasadas simultáneas sobre el mismo texto se pisan. La declaración
#      llevaba cliquet y una caducidad, y las dos han hecho su trabajo: cerradas `G-01`,
#      `G-02` y `G-07`, el coordinador aplicó la guarda a los cuatro y la declaración se
#      RETIRA. El diccionario se queda vacío A PROPÓSITO —y no se borra— porque su prueba
#      exige que toda zona con puntos sin guarda esté declarada Y que toda zona declarada
#      tenga puntos sin guarda: vacío, las dos mitades siguen midiendo, y la primera zona
#      que aparezca sin declarar pone `T380` en rojo sin que nadie tenga que acordarse.
ZONA_SIN_GUARDA_POR_PROPIETARIO = {}
PUNTOS_SIN_GUARDA_ADMITIDOS = 0


class AislamientoDeArranque(SesionNueva):
    """`G-03`. El aislamiento se decide ANTES de que el intérprete arranque, o no se decide.

    HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-05, con la orden y la salida literales:

        $ PYTHONPATH=veneno python3.12 <huella.py SIN la guarda> --raiz <repo>
          0000000000000000                     ← la huella FORJADA sobre el árbol real
          testigo en disco: `sitecustomize`    ← el gancho LLEGÓ a ejecutarse
        $ PYTHONPATH=veneno python3.12 kernel/operativo/validadores/huella.py
          078074dae8f687e8                     ← el valor SANO
          testigo en disco: `sitecustomize`    ← llegó al LANZADOR, no al trabajo
        $ PYTHONPATH=veneno python3.12 -I -S -E kernel/operativo/validadores/huella.py
          078074dae8f687e8                     ← el valor SANO
          testigo en disco: NINGUNO            ← el gancho NO LLEGÓ a existir
    """

    HUELLA = os.path.join(VALIDADORES, "huella.py")
    GUARDA = os.path.join(VALIDADORES, "aislamiento_de_arranque.py")
    VERIFICADOR = os.path.join(RAIZ_OPERATIVO, "raiz-externa", "verificador.py")
    INSTALADOR = os.path.join(RAIZ_OPERATIVO, "raiz-externa", "instalar.py")

    # ---------------------------------------------------------------- utillaje
    def sede_del_testigo(self, nombre="TESTIGO-DEL-GANCHO"):
        """El fichero donde el gancho deja constancia de haberse ejecutado.

        No se llama `testigo` porque `unittest` recoge por prefijo `test` y se lo llevaba
        por delante como si fuera un caso: la batería declaraba diecinueve pruebas donde
        hay dieciocho. Medido en la primera corrida de esta tanda.
        """
        return os.path.join(self.taller, nombre)

    def gancho(self, nombre_del_modulo, marca=None):
        """Un `sitecustomize.py`/`usercustomize.py` que ENVENENA y DEJA TESTIGO.

        La ruta del testigo va COMPILADA en el fichero y no en una variable de entorno: si
        dependiera del entorno, el saneamiento que se está midiendo la borraría y «no hay
        testigo» dejaría de distinguir «no corrió» de «corrió y no supo dónde escribir».
        """
        veneno = os.path.join(self.taller, "veneno-" + nombre_del_modulo)
        os.makedirs(veneno, exist_ok=True)
        marca = marca or nombre_del_modulo
        cuerpo = (
            "import hashlib, json\n"
            "open(" + repr(self.sede_del_testigo()) + ", 'a').write(" + repr(marca + "\n") + ")\n"
            "class _Falso:\n"
            "    def update(self, *a, **k):\n        pass\n"
            "    def hexdigest(self, *a, **k):\n        return '0' * 64\n"
            "    def digest(self, *a, **k):\n        return b'\\x00' * 32\n"
            "hashlib.sha256 = lambda *a, **k: _Falso()\n"
            "json.dumps = lambda *a, **k: '{}'\n"
        )
        with open(os.path.join(veneno, nombre_del_modulo + ".py"), "w",
                  encoding="utf-8") as manejador:
            manejador.write(cuerpo)
        return veneno

    def sin_guarda(self, origen, nombre="punto_vulnerable.py"):
        """Una copia del punto a la que se le ha RETIRADO el bloque de la guarda.

        Es la VERSIÓN VULNERABLE contra la que se contrasta. Sin ella no habría control del
        control: «el veneno no entró» se explicaría por un veneno que no funciona.
        """
        fuente = texto_de_fichero(origen)
        if _FINAL_DE_LA_GUARDA in fuente:
            inicio = fuente.rindex(
                "# ---", 0, fuente.index("#  `G-03` · AISLAMIENTO DE ARRANQUE"))
            final = fuente.index(_FINAL_DE_LA_GUARDA) + len(_FINAL_DE_LA_GUARDA)
            fuente = fuente[:inicio] + fuente[final:]
        # Y si el punto YA venía sin guarda, la copia es el punto tal cual. Lo que esta
        # ayuda tiene que devolver es una versión SIN guarda, no la operación de recortarla:
        # cuando la matriz de ataques sabotea el árbol quitándosela, exigir el recorte
        # convertiría el ROJO esperado en un error del andamiaje, que dice otra cosa.
        destino = os.path.join(self.taller, nombre)
        with open(destino, "w", encoding="utf-8") as manejador:
            manejador.write(fuente)
        os.chmod(destino, 0o755)
        return destino

    def correr_ruta(self, ejecutable, argumentos, *, extra=None, cwd=None, espera=300,
                    banderas=()):
        return subprocess.run(
            [sys.executable] + list(banderas) + [ejecutable] + [str(a) for a in argumentos],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.entorno(extra), cwd=cwd or self.taller, check=False, timeout=espera)

    def lineas_del_testigo(self):
        if not os.path.exists(self.sede_del_testigo()):
            return []
        return [l for l in texto_de_fichero(self.sede_del_testigo()).splitlines() if l.strip()]

    # ------------------------------------------------------------------ T380
    def test_T380_la_guarda_alcanza_a_TODO_punto_del_inventario_derivado(self):
        """T380 · Defecto que previene: `G-03` cerrado en una lista y abierto en la clase.

        SABOTAJE QUE LA PONE ROJA: retirar la guarda de cualquier punto ejecutable, o añadir
        un punto nuevo sin ella en cualquier zona.
        """
        puntos, _excluidos = inventariar_el_arbol()
        sin_guarda = sorted(ruta for ruta, senales in puntos.items()
                            if not senales["guarda"])
        zonas = {puntos[ruta]["zona"] for ruta in sin_guarda}
        for zona in sorted(zonas):
            self.assertIn(zona, ZONA_SIN_GUARDA_POR_PROPIETARIO,
                          "hay puntos ejecutables sin la guarda `G-03` en `" + zona
                          + "`, y esa zona no está declarada: " + repr(sin_guarda))
        self.assertLessEqual(
            len(sin_guarda), PUNTOS_SIN_GUARDA_ADMITIDOS,
            "el número de puntos sin guarda ha SUBIDO: " + repr(sin_guarda))
        # El motivo declarado no puede caducar en silencio: si la zona ya no tiene puntos
        # sin guarda, lo que sobra es la declaración y hay que retirarla.
        for zona in sorted(ZONA_SIN_GUARDA_POR_PROPIETARIO):
            self.assertIn(zona, zonas,
                          "se declara el motivo de eximir `" + zona + "` y ahí ya no queda "
                          "ningún punto sin guarda: el motivo ha caducado")
        # Y el CONTROL DEL CONTROL: la inmensa mayoría SÍ la lleva, en todas sus zonas.
        con_guarda = [ruta for ruta, senales in puntos.items() if senales["guarda"]]
        self.assertGreaterEqual(len(con_guarda), 50)
        self.assertGreaterEqual(len({puntos[r]["zona"] for r in con_guarda}), 7)

        # LA FRONTERA DEL INVENTARIO, EJERCIDA · hallazgo 5 del auditor independiente.
        # No basta con que los puntos que hay lleven la guarda: hay que medir que la
        # DEFINICIÓN de punto no deje fuera una clase entera. El fichero de abajo es el que
        # el auditor coló —sin shebang, sin `main`, sin `sys.exit`, y con una llamada que
        # imprime en el nivel superior—: se ejecuta y se envenena igual que cualquier otro,
        # y con la definición anterior salía clasificado `biblioteca-suelta` mientras
        # «56 de 56» se seguía publicando. Se ejerce sobre un temporal, no sobre el árbol.
        with tempfile.TemporaryDirectory(prefix="ads-frontera-") as taller:
            copia = os.path.join(taller, "arbol")
            os.makedirs(os.path.join(copia, "tooling"))
            with open(os.path.join(copia, "tooling", "colado.py"), "w",
                      encoding="utf-8") as manejador:
                manejador.write('"""Punto ejecutable que la definición anterior no veía."""\n'
                                "import hashlib\n"
                                "def _trabajo():\n"
                                "    print(hashlib.sha256(b'corpus').hexdigest()[:16])\n"
                                "_trabajo()\n")
            # y su CONTROL: un módulo que sólo declara NO puede entrar, o la regla sería
            # «todo `.py` es un punto» y la guarda acabaría exigida a las bibliotecas.
            with open(os.path.join(copia, "tooling", "inerte.py"), "w",
                      encoding="utf-8") as manejador:
                manejador.write('"""Sólo declara: importa, define y asigna."""\n'
                                "import os\n"
                                "import sys\n"
                                "sys.path.insert(0, os.path.dirname(__file__))\n"
                                "CONSTANTE = 3\n"
                                "def f():\n    return CONSTANTE\n"
                                "class C:\n    pass\n")
            colados, fuera = inventariar_el_arbol(copia)
            self.assertIn(
                "tooling/colado.py", colados,
                "un `.py` que HACE TRABAJO al importarse queda fuera del inventario: la "
                "guarda `G-03` se exige sobre una población que no incluye a todo lo que "
                "se ejecuta, y «N de N» deja de significar lo que dice")
            self.assertIn(
                "tooling/inerte.py", fuera,
                "un módulo que sólo declara ha entrado en el inventario: la regla se ha "
                "vuelto «todo `.py` es un punto» y acabará exigiendo la guarda a las "
                "bibliotecas, que es como una regla demasiado ancha se termina apagando")

    # ------------------------------------------------------------------ T381
    def test_T381_el_MECANISMO_de_la_guarda_es_identico_byte_a_byte(self):
        """T381 · Defecto que previene: una guarda que se adapta y deja de proteger.

        SABOTAJE QUE LA PONE ROJA: cambiar un byte del mecanismo en un solo punto.
        """
        puntos, _ = inventariar_el_arbol()
        digests = {}
        for ruta, senales in sorted(puntos.items()):
            if not senales["guarda"]:
                continue
            self.assertIsNotNone(senales["mecanismo_g03"],
                                 ruta + " exige el aislamiento y no lleva el MECANISMO")
            digests.setdefault(
                hashlib.sha256(senales["mecanismo_g03"].encode("utf-8")).hexdigest(),
                []).append(ruta)
        self.assertEqual(len(digests), 1,
                         "los mecanismos `G-03` han divergido: "
                         + repr({d[:12]: len(r) for d, r in digests.items()}))

    # ------------------------------------------------------------------ T382
    def test_T382_el_sitecustomize_LLEGA_sin_guarda_y_NO_LLEGA_por_la_via_oficial(self):
        """T382 · Defecto que previene: `H-1`, la contaminación que produce VERDE FALSO.

        Las TRES filas, con el testigo en disco como juez:
          versión SIN guarda        → huella FORJADA  ·  el gancho LLEGA
          versión con guarda        → huella SANA     ·  el gancho llega al LANZADOR
          vía oficial `-I -S -E`    → huella SANA     ·  el gancho NO LLEGA

        SABOTAJE QUE LA PONE ROJA: retirar la guarda de `huella.py`, o retirar `-S` de las
        banderas de aislamiento.
        """
        veneno = self.gancho("sitecustomize")
        entorno = {"PYTHONPATH": veneno}
        sano = self.correr_ruta(self.HUELLA, ["--raiz", RAIZ_REPO])
        self.assertEqual(sano.returncode, 0, sano.stderr.decode())
        valor_sano = sano.stdout.decode().strip()
        self.assertRegex(valor_sano, r"^[0-9a-f]{16}$")
        self.assertNotEqual(valor_sano, "0" * 16)

        # 1 · SIN GUARDA. El gancho llega y la huella sale FORJADA.
        vulnerable = self.sin_guarda(self.HUELLA)
        forjada = self.correr_ruta(vulnerable, ["--raiz", RAIZ_REPO], extra=entorno)
        self.assertEqual(forjada.stdout.decode().strip(), "0" * 16,
                         "la versión SIN guarda no se dejó falsificar: el veneno no "
                         "funciona y esta prueba no estaría midiendo nada")
        self.assertIn("sitecustomize", self.lineas_del_testigo(),
                      "el gancho no llegó a ejecutarse ni sobre la versión vulnerable")

        # 2 · CON GUARDA, invocada directamente. El valor es el SANO.
        os.unlink(self.sede_del_testigo())
        directa = self.correr_ruta(self.HUELLA, ["--raiz", RAIZ_REPO], extra=entorno)
        self.assertEqual(directa.returncode, 0, directa.stderr.decode())
        self.assertEqual(directa.stdout.decode().strip(), valor_sano,
                         "la huella cambió bajo `sitecustomize` pese a la guarda")
        self.assertEqual(self.lineas_del_testigo(), ["sitecustomize"],
                         "el gancho tenía que llegar al proceso LANZADOR —eso no se puede "
                         "impedir desde Python— y sólo a ése")

        # 3 · POR LA VÍA OFICIAL. El gancho NO LLEGA A EXISTIR.
        os.unlink(self.sede_del_testigo())
        oficial = self.correr_ruta(self.HUELLA, ["--raiz", RAIZ_REPO], extra=entorno,
                                   banderas=("-I", "-S", "-E"))
        self.assertEqual(oficial.returncode, 0, oficial.stderr.decode())
        self.assertEqual(oficial.stdout.decode().strip(), valor_sano)
        self.assertEqual(self.lineas_del_testigo(), [],
                         "el gancho se ejecutó por la vía oficial: " + repr(
                             self.lineas_del_testigo()))

    # ------------------------------------------------------------------ T383
    def test_T383_el_usercustomize_tampoco_llega(self):
        """T383 · Defecto que previene: cerrar `sitecustomize` y dejar abierto su gemelo.

        SABOTAJE QUE LA PONE ROJA: retirar `-S` y quedarse con `-I -E`.
        """
        veneno = self.gancho("usercustomize")
        entorno = {"PYTHONPATH": veneno}
        vulnerable = self.sin_guarda(self.HUELLA)
        forjada = self.correr_ruta(vulnerable, ["--raiz", RAIZ_REPO], extra=entorno)
        self.assertEqual(forjada.stdout.decode().strip(), "0" * 16,
                         "el `usercustomize` no envenena ni la versión vulnerable")
        self.assertIn("usercustomize", self.lineas_del_testigo())

        # LA INVOCACIÓN DIRECTA, que es la que mide la GUARDA. Sin esta fila la prueba no
        # discriminaba: pasar `-I -S -E` a mano funciona igual sobre un punto SIN guarda, de
        # modo que sólo con la fila oficial el sabotaje salía verde. Medido en la matriz de
        # los doce ataques, y ésta es la corrección.
        os.unlink(self.sede_del_testigo())
        directa = self.correr_ruta(self.HUELLA, ["--raiz", RAIZ_REPO], extra=entorno)
        self.assertEqual(directa.returncode, 0, directa.stderr.decode())
        self.assertNotEqual(directa.stdout.decode().strip(), "0" * 16,
                            "la huella se falsificó con `usercustomize` pese a la guarda")
        self.assertEqual(self.lineas_del_testigo(), ["usercustomize"])

        os.unlink(self.sede_del_testigo())
        oficial = self.correr_ruta(self.HUELLA, ["--raiz", RAIZ_REPO], extra=entorno,
                                   banderas=("-I", "-S", "-E"))
        self.assertEqual(oficial.returncode, 0, oficial.stderr.decode())
        self.assertNotEqual(oficial.stdout.decode().strip(), "0" * 16)
        self.assertEqual(self.lineas_del_testigo(), [])

    # ------------------------------------------------------------------ T384
    def test_T384_el_PYTHONPATH_con_un_homonimo_no_decide_la_huella(self):
        """T384 · Defecto que previene: `E-10` por la vía del módulo homónimo.

        SABOTAJE QUE LA PONE ROJA: retirar la purga `E-10` y la guarda a la vez.
        """
        veneno = os.path.join(self.taller, "homonimo")
        os.makedirs(veneno)
        with open(os.path.join(veneno, "hashlib.py"), "w", encoding="utf-8") as manejador:
            manejador.write(
                "open(" + repr(self.sede_del_testigo()) + ", 'a').write('hashlib-homonimo\n')\n"
                "class _F:\n"
                "    def update(self, *a, **k):\n        pass\n"
                "    def hexdigest(self, *a, **k):\n        return '0' * 64\n"
                "def sha256(*a, **k):\n    return _F()\n")
        salida = self.correr_ruta(self.HUELLA, ["--raiz", RAIZ_REPO],
                                  extra={"PYTHONPATH": veneno}, cwd=veneno)
        self.assertEqual(salida.returncode, 0, salida.stderr.decode())
        self.assertNotEqual(salida.stdout.decode().strip(), "0" * 16)
        self.assertEqual(self.lineas_del_testigo(), [],
                         "se importó el `hashlib` homónimo del `PYTHONPATH`")

    # ------------------------------------------------------------------ T385
    def test_T385_un_PAQUETE_homonimo_no_entra_ni_desde_el_cwd(self):
        """T385 · Defecto que previene: `capacidades` publicando `{}` con código 0.

        SABOTAJE QUE LA PONE ROJA: retirar la guarda de `verificador.py`.
        """
        veneno = os.path.join(self.taller, "paquete-homonimo")
        for paquete in ("json", "errores", "firma", "atestacion"):
            carpeta = os.path.join(veneno, paquete)
            os.makedirs(carpeta, exist_ok=True)
            with open(os.path.join(carpeta, "__init__.py"), "w",
                      encoding="utf-8") as manejador:
                manejador.write("open(" + repr(self.sede_del_testigo()) + ", 'a').write("
                                "'paquete-homonimo:' + __name__ + '\n')\n"
                                "def dumps(*a, **k):\n    return '{}'\n")
        salida = self.correr_ruta(self.VERIFICADOR, ["capacidades"],
                                  extra={"PYTHONPATH": veneno + os.pathsep + "."},
                                  cwd=veneno)
        self.assertEqual(salida.returncode, 0, salida.stderr.decode())
        datos = json.loads(salida.stdout.decode("utf-8"))
        self.assertEqual(len(datos["condiciones_de_certificacion"]), 9,
                         "`capacidades` volvió a publicar un conjunto encogido")
        self.assertEqual(self.lineas_del_testigo(), [])

    # ------------------------------------------------------------------ T386
    def test_T386_un_PATH_con_interprete_falso_no_decide_el_resultado(self):
        """T386 · Defecto que previene: colar el veneno por el intérprete que resuelve `PATH`.

        El intérprete falso es un guion que reexporta `PYTHONPATH` hacia el veneno y llama
        al real. Control del control: sobre un `python3` desnudo, el guion SÍ envenena.

        SABOTAJE QUE LA PONE ROJA: retirar `-E` de las banderas de aislamiento.
        """
        veneno = self.gancho("sitecustomize", marca="por-el-PATH")
        falso = os.path.join(self.taller, "bin-falso")
        os.makedirs(falso)
        atajo = os.path.join(falso, "python3")
        with open(atajo, "w", encoding="utf-8") as manejador:
            manejador.write("#!/bin/sh\n"
                            "PYTHONPATH=" + veneno + " exec " + sys.executable + " \"$@\"\n")
        os.chmod(atajo, 0o755)
        camino = falso + os.pathsep + os.environ.get("PATH", "/usr/bin:/bin")

        # CONTROL DEL CONTROL: el intérprete falso envenena de verdad a quien no se defiende.
        control = subprocess.run([atajo, self.sin_guarda(self.HUELLA), "--raiz", RAIZ_REPO],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 env=self.entorno({"PATH": camino}), cwd=self.taller,
                                 check=False, timeout=300)
        self.assertEqual(control.stdout.decode().strip(), "0" * 16,
                         "el intérprete falso no envenena ni a la versión vulnerable")
        os.unlink(self.sede_del_testigo())

        salida = subprocess.run([atajo, self.HUELLA, "--raiz", RAIZ_REPO],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                env=self.entorno({"PATH": camino}), cwd=self.taller,
                                check=False, timeout=300)
        self.assertEqual(salida.returncode, 0, salida.stderr.decode())
        self.assertNotEqual(salida.stdout.decode().strip(), "0" * 16,
                            "el intérprete del `PATH` decidió la huella")
        self.assertEqual(self.lineas_del_testigo(), ["por-el-PATH"],
                         "el gancho llegó a más procesos que al lanzador: "
                         + repr(self.lineas_del_testigo()))

    # ------------------------------------------------------------------ T387
    def test_T387_un_punto_del_arbol_B_usa_la_guarda_de_B_y_no_la_de_A(self):
        """T387 · Defecto que previene: el árbol juzgado aporta la guarda que lo protege.

        SABOTAJE QUE LA PONE ROJA: buscar la guarda desde el `cwd` en vez de desde
        `__file__`.
        """
        arbol_b = os.path.join(self.taller, "arbol-b", "kernel", "operativo", "validadores")
        os.makedirs(arbol_b)
        shutil.copy(self.HUELLA, arbol_b)
        shutil.copy(self.GUARDA, arbol_b)

        arbol_a = os.path.join(self.taller, "arbol-a", "kernel", "operativo", "validadores")
        os.makedirs(arbol_a)
        # La guarda del árbol A está SABOTEADA: no comprueba nada y lo grita.
        with open(os.path.join(arbol_a, "aislamiento_de_arranque.py"), "w",
                  encoding="utf-8") as manejador:
            manejador.write(
                "import sys\n"
                "sys.stderr.write('GUARDA DEL ARBOL A\\n')\n"
                "BANDERAS_DE_AISLAMIENTO = ()\n"
                "def exigir(*a, **k):\n    return {'aislado': False}\n")
        raiz_a = os.path.join(self.taller, "arbol-a")

        salida = self.correr_ruta(os.path.join(arbol_b, "huella.py"),
                                  ["--raiz", RAIZ_REPO],
                                  extra={"PYTHONPATH": arbol_a}, cwd=raiz_a)
        self.assertEqual(salida.returncode, 0, salida.stderr.decode())
        self.assertNotIn("GUARDA DEL ARBOL A", salida.stderr.decode(),
                         "el punto del árbol B cargó la guarda del árbol A")
        self.assertRegex(salida.stdout.decode().strip(), r"^[0-9a-f]{16}$")

    # ------------------------------------------------------------------ T388
    def test_T388_un_modulo_importado_ANTES_de_la_purga_se_ve_y_falla_cerrado(self):
        """T388 · Defecto que previene: lo que ya está en `sys.modules` cuando llega la purga.

        SABOTAJE QUE LA PONE ROJA: dejar de mirar `sys.modules` en la guarda.
        """
        intruso = os.path.join(self.taller, "fuera-del-arbol")
        os.makedirs(intruso)
        with open(os.path.join(intruso, "colado.py"), "w", encoding="utf-8") as manejador:
            manejador.write("VALOR = 1\n")
        # El intruso NO se cuela por `sys.path`: se carga por RUTA ABSOLUTA, que es la forma
        # que ni `-I` ni la purga pueden impedir —un `.pth`, un `sitecustomize` o un módulo
        # del propio árbol manipulado hacen exactamente esto—. Cuando la guarda toma la
        # palabra, el intruso YA ESTÁ en `sys.modules`, y ahí es donde se le ve.
        programa = (
            "import sys, importlib.util\n"
            "_e = importlib.util.spec_from_file_location("
            "'colado', " + repr(os.path.join(intruso, "colado.py")) + ")\n"
            "_m = importlib.util.module_from_spec(_e)\n"
            "_e.loader.exec_module(_m)\n"
            "sys.modules['colado'] = _m\n"
            "sys.path.insert(0, " + repr(VALIDADORES) + ")\n"
            "import aislamiento_de_arranque as a\n"
            "ajenos = a.modulos_de_procedencia_ajena()\n"
            "sys.stderr.write('AJENOS=' + repr([n for n, _ in ajenos]) + chr(10))\n"
            "a.exigir(" + repr(self.HUELLA) + ")\n"
            "sys.stderr.write('NO DEBERIA LLEGAR AQUI' + chr(10))\n")
        salida = subprocess.run([sys.executable, "-I", "-S", "-E", "-c", programa],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                env=self.entorno(), cwd=self.taller, check=False,
                                timeout=120)
        error = salida.stderr.decode()
        self.assertIn("'colado'", error, "el módulo colado no se vio: " + error)
        self.assertEqual(salida.returncode, 5,
                         "un módulo de procedencia ajena no produjo fallo cerrado: " + error)
        self.assertIn("PROCEDENCIA_NO_FIABLE", error)
        self.assertNotIn("NO DEBERIA LLEGAR AQUI", error)

    # ------------------------------------------------------------------ T389
    def test_T389_el_lanzamiento_DIRECTO_no_evita_la_guarda(self):
        """T389 · Defecto que previene: un aislamiento que sólo existe si se usa el envoltorio.

        SABOTAJE QUE LA PONE ROJA: que la guarda se limite a avisar en vez de reejecutar.
        """
        veneno = self.gancho("sitecustomize", marca="lanzamiento-directo")
        # Invocado A PELO, sin banderas y con el veneno puesto: tiene que reejecutarse solo.
        salida = self.correr_ruta(self.HUELLA, ["--raiz", RAIZ_REPO],
                                  extra={"PYTHONPATH": veneno})
        self.assertEqual(salida.returncode, 0, salida.stderr.decode())
        self.assertNotEqual(salida.stdout.decode().strip(), "0" * 16)
        # Y el ADS_AISLADO del padre no viaja a los nietos: si viajara, un hijo NO aislado
        # creería haberse reejecutado ya y fallaría cerrado. Se comprueba lanzando un punto
        # desde dentro de un proceso que YA venía marcado.
        conmarca = self.correr_ruta(self.HUELLA, ["--raiz", RAIZ_REPO],
                                    extra={"ADS_AISLADO": "1"})
        self.assertEqual(conmarca.returncode, 0,
                         "una marca heredada impidió el aislamiento: "
                         + conmarca.stderr.decode())

    # ------------------------------------------------------------------ T390
    def test_T390_el_manifiesto_de_la_instalacion_no_encoge_bajo_el_gancho(self):
        """T390 · Defecto que previene: `{}` EXIT=0 y un manifiesto de TRES bytes.

        SABOTAJE QUE LA PONE ROJA: retirar la guarda de `instalar.py`.
        """
        veneno = self.gancho("sitecustomize", marca="contra-el-instalador")
        limpio = os.path.join(self.taller, "instalacion-limpia")
        sano = self.correr_ruta(self.INSTALADOR, ["--destino", limpio, "--arbol", RAIZ_REPO])
        self.assertEqual(sano.returncode, 0, sano.stderr.decode())
        manifiesto_sano = json.loads(texto_de_fichero(
            os.path.join(limpio, "MANIFIESTO-DE-INSTALACION.json")))
        self.assertGreater(len(manifiesto_sano["ficheros"]), 10)

        atacado = os.path.join(self.taller, "instalacion-atacada")
        bajo_veneno = self.correr_ruta(self.INSTALADOR,
                                       ["--destino", atacado, "--arbol", RAIZ_REPO],
                                       extra={"PYTHONPATH": veneno})
        self.assertEqual(bajo_veneno.returncode, 0, bajo_veneno.stderr.decode())
        ruta = os.path.join(atacado, "MANIFIESTO-DE-INSTALACION.json")
        self.assertGreater(os.path.getsize(ruta), 3,
                           "el manifiesto volvió a tener tres bytes")
        manifiesto = json.loads(texto_de_fichero(ruta))
        self.assertEqual(len(manifiesto["ficheros"]), len(manifiesto_sano["ficheros"]))
        self.assertEqual([f["sha256"] for f in manifiesto["ficheros"]],
                         [f["sha256"] for f in manifiesto_sano["ficheros"]],
                         "los digests del manifiesto se fabricaron desde el entorno")
        self.assertEqual(self.lineas_del_testigo(), ["contra-el-instalador"])

    # ------------------------------------------------------------------ T391
    def test_T391_capacidades_no_publica_el_vacio_bajo_el_gancho(self):
        """T391 · Defecto que previene: `capacidades` → `{}` con código 0 (`ADJ-B2`).

        SABOTAJE QUE LA PONE ROJA: retirar la guarda de `verificador.py`.
        """
        veneno = self.gancho("sitecustomize", marca="contra-capacidades")
        sano = self.correr_ruta(self.VERIFICADOR, ["capacidades"])
        self.assertEqual(sano.returncode, 0, sano.stderr.decode())
        limpio = json.loads(sano.stdout.decode("utf-8"))

        atacado = self.correr_ruta(self.VERIFICADOR, ["capacidades"],
                                   extra={"PYTHONPATH": veneno})
        self.assertEqual(atacado.returncode, 0, atacado.stderr.decode())
        sucio = json.loads(atacado.stdout.decode("utf-8"))
        self.assertEqual(sucio["condiciones_de_certificacion"],
                         limpio["condiciones_de_certificacion"])
        self.assertEqual(len(sucio["condiciones_de_certificacion"]), 9)

    # ------------------------------------------------------------------ T392
    def test_T392_una_instalacion_a_la_que_le_falta_la_guarda_NO_ejecuta(self):
        """T392 · Defecto que previene: una instalación parcial que corre igual.

        La guarda viaja DENTRO de la instalación y entra en su manifiesto. Si falta, los
        puntos de la raíz externa no se ejecutan sin protección: fallan cerrado.

        SABOTAJE QUE LA PONE ROJA: que la guarda no falle cuando no encuentra su módulo.
        """
        destino = os.path.join(self.taller, "instalacion")
        instalacion = self.correr_ruta(self.INSTALADOR,
                                       ["--destino", destino, "--arbol", RAIZ_REPO])
        self.assertEqual(instalacion.returncode, 0, instalacion.stderr.decode())
        verificador = os.path.join(destino, "raiz-externa", "verificador.py")
        guarda = os.path.join(destino, "raiz-externa", "aislamiento_de_arranque.py")
        self.assertTrue(os.path.isfile(guarda),
                        "la guarda no viajó con la instalación: los cuatro puntos de la "
                        "raíz externa no podrían exigir el aislamiento")
        manifiesto = json.loads(texto_de_fichero(
            os.path.join(destino, "MANIFIESTO-DE-INSTALACION.json")))
        self.assertIn("raiz-externa/aislamiento_de_arranque.py",
                      [f["ruta"] for f in manifiesto["ficheros"]],
                      "la guarda instalada no entra en el manifiesto: se podría cambiar "
                      "sin que la verificación lo notara")

        sano = self.correr_ruta(verificador, ["capacidades"])
        self.assertEqual(sano.returncode, 0, sano.stderr.decode())

        os.unlink(guarda)
        mutilada = self.correr_ruta(verificador, ["capacidades"])
        self.assertEqual(mutilada.returncode, 5,
                         "una instalación sin la guarda ejecutó igual: "
                         + mutilada.stdout.decode()[:200])
        self.assertIn("PROCEDENCIA_NO_FIABLE", mutilada.stderr.decode())
        self.assertEqual(mutilada.stdout.decode().strip(), "",
                         "publicó algo pese a no poder decidir su aislamiento")

    # ------------------------------------------------------------------ T393
    def test_T393_una_bateria_NUEVA_ya_no_queda_exenta_por_su_zona(self):
        """T393 · Defecto que previene: `D-01`, eximir por domicilio.

        SABOTAJE QUE LA PONE ROJA: devolver la clase `bateria` a `MOTIVOS_DE_EXCLUSION`.
        """
        arbol = os.path.join(self.taller, "arbol-sintetico")
        zona = os.path.join(arbol, "kernel", "operativo", "runtime", "pruebas")
        os.makedirs(zona)
        for nombre, cuerpo in (
                ("test_ya_estaba.py", "#!/usr/bin/env python3\nimport sys\n"
                                      "if __name__ == '__main__':\n    sys.exit(0)\n"),
                ("test_NUEVA_sin_guarda.py", "#!/usr/bin/env python3\nimport sys\n"
                                             "if __name__ == '__main__':\n"
                                             "    sys.exit(0)\n")):
            with open(os.path.join(zona, nombre), "w", encoding="utf-8") as manejador:
                manejador.write(cuerpo)
        puntos, excluidos = inventariar_el_arbol(arbol)
        relativa = "kernel/operativo/runtime/pruebas/test_NUEVA_sin_guarda.py"
        self.assertIn(relativa, puntos,
                      "una batería nueva volvió a quedar fuera del inventario por su zona")
        self.assertNotIn(relativa, excluidos)
        self.assertFalse(puntos[relativa]["guarda"])
        self.assertFalse(puntos[relativa]["purga"])
        self.assertNotIn("bateria", MOTIVOS_DE_EXCLUSION)

    # ------------------------------------------------------------------ T394
    def test_T394_el_runner_SANEA_el_entorno_de_sus_hijos_y_lo_PUBLICA(self):
        """T394 · Defecto que previene: `HALLAZGO 3`, `subprocess.run` sin `env=`.

        SABOTAJE QUE LA PONE ROJA: quitar el `env=` de `registrar_evidencia.ejecutar`, o
        dejar de escribir la línea `aislamiento` en la cabecera.
        """
        sys.path.insert(0, VALIDADORES)
        import registrar_evidencia                                    # noqa: PLC0415

        sonda = os.path.join(self.taller, "sonda")
        os.makedirs(sonda)
        with open(os.path.join(sonda, "sonda.py"), "w", encoding="utf-8") as manejador:
            manejador.write("#!/usr/bin/env python3\n"
                            "import os, sys\n"
                            "print('VARIABLES ' + ' '.join(sorted(os.environ)))\n"
                            "print('FLAGS %d%d%d' % (sys.flags.isolated, sys.flags.no_site,"
                            " sys.flags.ignore_environment))\n"
                            "print('1 superadas · 0 fallidas')\n"
                            "sys.exit(0)\n")
        ejecucion = registrar_evidencia.Ejecucion(
            {"id": "sonda", "script": "sonda.py", "dir": "sonda", "tipo": "validador",
             "evidencia": "sonda-salida.txt"})
        veneno = self.gancho("sitecustomize", marca="contra-el-runner")
        anterior = os.environ.get("PYTHONPATH")
        os.environ["PYTHONPATH"] = veneno
        try:
            registrar_evidencia.ejecutar(self.taller, ejecucion)
        finally:
            if anterior is None:
                os.environ.pop("PYTHONPATH", None)
            else:
                os.environ["PYTHONPATH"] = anterior
        self.assertEqual(ejecucion.codigo, 0, ejecucion.motivo)
        publicada = texto_de_fichero(os.path.join(
            self.taller, "kernel", "operativo", "pruebas", "evidencia", "sonda-salida.txt"))
        # 1 · el hijo no recibió el `PYTHONPATH` del padre
        variables = [l for l in publicada.splitlines() if l.startswith("VARIABLES ")][0]
        self.assertNotIn("PYTHONPATH", variables,
                         "el entorno del padre llegó al hijo: " + variables)
        # 2 · y arrancó AISLADO
        self.assertIn("FLAGS 111", publicada, "el hijo no arrancó con `-I -S -E`")
        # 3 · y la GARANTÍA está PUBLICADA en la cabecera
        cabecera = [l for l in publicada.splitlines() if l.startswith("# aislamiento:")]
        self.assertTrue(cabecera, "la cabecera no publica el aislamiento del hijo")
        for bandera in ("-I", "-S", "-E"):
            self.assertIn(bandera, cabecera[0])
        self.assertIn("PYTHONPATH", cabecera[0],
                      "la cabecera no dice que se retiró el `PYTHONPATH` del lanzador")
        # 4 · el gancho NO llegó a ejecutarse en el hijo. Y el CONTROL DEL CONTROL: el
        #     mismo hijo, lanzado como lo lanzaba el runner antes —heredando el entorno—,
        #     SÍ lo ejecuta. Sin este control, «no hay testigo» se explicaría por un veneno
        #     que no funciona.
        self.assertEqual(self.lineas_del_testigo(), [],
                         "el gancho llegó a un hijo del runner: "
                         + repr(self.lineas_del_testigo()))
        heredado = dict(os.environ)
        heredado["PYTHONPATH"] = veneno
        como_antes = subprocess.run(
            [sys.executable, os.path.join(sonda, "sonda.py")],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=heredado, cwd=self.taller,
            check=False, timeout=120)
        self.assertEqual(como_antes.returncode, 0, como_antes.stderr.decode())
        self.assertEqual(self.lineas_del_testigo(), ["contra-el-runner"],
                         "sin el saneamiento el gancho tampoco llega: esta prueba no "
                         "estaría midiendo el `env=`")
        self.assertNotIn("FLAGS 111", como_antes.stdout.decode(),
                         "el hijo heredado salió aislado sin que nadie lo aislara")

    # ------------------------------------------------------------------ T395
    def test_T395_comprobar_evidencia_EXIGE_la_garantia_publicada(self):
        """T395 · Defecto que previene: publicar la garantía y que nadie la comprueba.

        SABOTAJE QUE LA PONE ROJA: retirar la comprobación de `comprobar_evidencia.py`.
        """
        sys.path.insert(0, VALIDADORES)
        import comprobar_evidencia                                    # noqa: PLC0415
        import comprobar_contratos                                    # noqa: PLC0415

        def juzgar(cabecera):
            resultado = comprobar_contratos.Resultado("T158", "prueba")
            comprobar_evidencia._comprobar_aislamiento_publicado(
                "evidencia.txt", cabecera, resultado)
            return resultado.fallos

        buena = ("# aislamiento:  banderas -I -S -E · entorno CONSTRUIDO con 3 variables "
                 "(HOME LANG PATH) · retiradas del lanzador: PYTHONPATH\n")
        self.assertEqual(juzgar(buena), [], "una cabecera correcta salió con fallos")
        self.assertTrue(juzgar("# evidencia de: x\n"),
                        "una evidencia SIN la línea de aislamiento pasó")
        self.assertTrue(juzgar("# aislamiento:  banderas -I · entorno CONSTRUIDO con 3 "
                               "variables (HOME LANG PATH)\n"),
                        "una cabecera que no nombra `-S` ni `-E` pasó")
        self.assertTrue(juzgar("# aislamiento:  banderas -I -S -E · entorno CONSTRUIDO con "
                               "4 variables (HOME LANG PATH PYTHONPATH)\n"),
                        "una cabecera que declara haber entregado `PYTHONPATH` pasó")

    # ------------------------------------------------------------------ T396
    def test_T396_la_primitiva_sustituida_EN_SITIO_se_caza_con_el_vector_conocido(self):
        """T396 · Defecto que previene: la mutación que no llega por `sitecustomize`.

        SABOTAJE QUE LA PONE ROJA: retirar la autocomprobación contra el vector conocido.
        """
        programa = (
            "import sys, hashlib\n"
            "class _F:\n"
            "    def hexdigest(self, *a, **k):\n        return '0' * 64\n"
            "hashlib.sha256 = lambda *a, **k: _F()\n"
            "sys.path.insert(0, " + repr(VALIDADORES) + ")\n"
            "import aislamiento_de_arranque as a\n"
            "a.exigir(" + repr(self.HUELLA) + ")\n"
            "sys.stderr.write('NO DEBERIA LLEGAR AQUI' + chr(10))\n")
        salida = subprocess.run([sys.executable, "-I", "-S", "-E", "-c", programa],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                env=self.entorno(), cwd=self.taller, check=False,
                                timeout=120)
        error = salida.stderr.decode()
        self.assertEqual(salida.returncode, 5, error)
        self.assertIn("PROCEDENCIA_NO_FIABLE", error)
        self.assertIn("hashlib.sha256", error)
        self.assertNotIn("NO DEBERIA LLEGAR AQUI", error)

    # ------------------------------------------------------------------ T397
    def test_T397_las_CUATRO_banderas_se_exigen_y_una_sola_que_falte_no_basta(self):
        """T397 · Defecto que previene: declarar aislamiento con tres banderas de cuatro.

        SABOTAJE QUE LA PONE ROJA: aceptar `-S -E` sin `-I`, que devolvería `sys.path[0]`.
        """
        programa = ("import sys\n"
                    "sys.path.insert(0, " + repr(VALIDADORES) + ")\n"
                    "import aislamiento_de_arranque as a\n"
                    "print(int(a.esta_aislado()), a.flags_de_aislamiento())\n")
        matriz = {(): 0, ("-S",): 0, ("-E",): 0, ("-S", "-E"): 0, ("-I",): 0,
                  ("-I", "-S", "-E"): 1}
        for banderas, esperado in sorted(matriz.items()):
            with self.subTest(banderas=banderas):
                salida = subprocess.run(
                    [sys.executable] + list(banderas) + ["-c", programa],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=self.entorno(),
                    cwd=self.taller, check=False, timeout=120)
                self.assertEqual(salida.returncode, 0, salida.stderr.decode())
                obtenido = int(salida.stdout.decode().split()[0])
                self.assertEqual(obtenido, esperado,
                                 "con " + repr(banderas) + " el aislamiento se declaró "
                                 + repr(bool(obtenido)) + ": " + salida.stdout.decode())
        # Y la cuarta bandera se MIDE donde existe: en 3.11+ `-I` implica `-P`.
        self.assertTrue(hasattr(sys.flags, "safe_path"),
                        "este intérprete no expone `safe_path` y el aparato declara 3.12")


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
