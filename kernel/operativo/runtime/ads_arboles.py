#!/usr/bin/env python3
"""ads_arboles — punto ejecutable de `V6-15`, los ÁRBOLES ADVERSARIALES.

    python3 kernel/operativo/runtime/ads_arboles.py --repo <dir> conjunto
    python3 kernel/operativo/runtime/ads_arboles.py --repo <dir> cruce
    python3 kernel/operativo/runtime/ads_arboles.py --repo <dir> suite

Órdenes: `conjunto` · `cruce` · `suite`.
Códigos de salida:  0 éxito · 1 error tipado o suite no cerrada · 2 uso incorrecto.

DECISIÓN · la salida es JSON con claves ORDENADAS, y es la salida POR DEFECTO
    Alternativas: (a) texto legible por defecto y `--json` opcional, como `ads_admision.py`;
    (b) JSON siempre.
    Se elige (b). Lo que este instrumento publica es la ENTRADA de un criterio de cierre
    —las dos restas de `V6-15`— y esa entrada la consume otro instrumento, no una persona.
    Un formato legible que además tuviera que ser determinista sería dos formatos con una
    sola implementación. Se conserva `--legible` para leerlo a ojo, y ése NO es la evidencia.

DECISIÓN · NINGÚN CARDINAL del conjunto aparece en la salida
    §20.5 lo prohíbe expresamente para esta fila, y la prohibición alcanza a la salida del
    instrumento: publicar el recuento del conjunto reintroduce por la puerta de atrás el
    cardinal que la sección retiró. Lo que se publica es el CONJUNTO, con la procedencia de
    cada árbol; contar es del que lee.

DECISIÓN · misma salida desde cualquier `cwd`
    Todas las rutas se publican relativas a la raíz del repositorio, y `--repo` se resuelve a
    absoluta sólo para leer. Una evidencia que cambiara con el directorio desde el que se
    lanzó el instrumento no sería comparable entre máquinas, que es lo que `I-g3` exige.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR sobre esta zona, dos veces. La primera, `E-10`: con
#  `PYTHONPATH` apuntando a un directorio con un `json.py` HOMÓNIMO, `verificar --json`
#  publicaba `{}` como veredicto con código 0. La segunda, `G-03` en el gate del 2026-09-05:
#  la purga que cerró aquello vive DENTRO del programa y `site.py` importa `sitecustomize`
#  ANTES de que la primera sentencia del módulo se ejecute, de modo que un gancho puede
#  mutar la primitiva ya importada —`hashlib.sha256`— sin tocar ningún módulo.
#
#  Estos cinco puntos son el CAMINO PRODUCTIVO del runtime: lo que publican es el veredicto
#  y la evidencia. Con la guarda, se reejecutan con `-I -S -E` y el gancho no llega a
#  ejecutarse; sin ella, la contaminación decide qué dicen.
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
#  HECHO REPRODUCIDO ANTES DE CORREGIR, sobre este mismo punto ejecutable: con
#  `PYTHONPATH=<dir>` apuntando a un directorio que contiene un `json.py` HOMÓNIMO, el
#  proceso IMPORTABA el homónimo. `sys.path[0]` —el directorio del script— protege a
#  `admision`, `estado` y `runtime`, que viven al lado; NO protege a la biblioteca estándar,
#  que va DESPUÉS de `PYTHONPATH`. Medido: `ads_admision.py --repo <dir> verificar --json`
#  publicaba `{}` como veredicto y terminaba con código 0, y los cinco `ads_*.py` importaban
#  el módulo envenenado.
#
#  DECISIÓN · la purga es lo PRIMERO del fichero y sólo usa `sys` y `os`
#      Alternativas: (a) purgar después de los imports normales; (b) purgar en un módulo
#      aparte e importarlo; (c) purgar aquí, con lo único que el intérprete ya ha cargado.
#      Se elige (c). Con (a) la purga llega tarde: el homónimo ya está en `sys.modules`. Con
#      (b) la purga depende de un `import` que es exactamente lo que se está protegiendo —una
#      guardia que necesita importar ya ha perdido—. `sys` es un módulo incorporado y `os` lo
#      carga el arranque del intérprete, así que los dos vienen de `sys.modules` y no de la
#      ruta de importación. Que `os` sea el bueno se COMPRUEBA, no se supone.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación
#      distinta y convertiría un fallo de entorno en un fallo del aparato. Lo que `E-10`
#      nombra es concreto: `PYTHONPATH` y el `cwd`. Se retiran ésos, se cuenta cuántos, y el
#      recuento se PUBLICA en la procedencia.
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
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import arboles                                                       # noqa: E402
from arboles.errores import ErrorDeArboles                           # noqa: E402
from admision.errores import ErrorDeAdmision                         # noqa: E402
from gobierno.errores import ErrorDeGobierno                         # noqa: E402

from adaptadores.contrato import ErrorDeAdaptador               # noqa: E402
from contencion.errores import ErrorDeContencion                     # noqa: E402
from estado.errores import ErrorDeEstado                             # noqa: E402
from identidad.errores import ErrorDeIdentidad                       # noqa: E402

EXITO, FALLO, USO = 0, 1, 2


# ---------------------------------------------------------------------------
#  `E-10` · la PROCEDENCIA se PUBLICA. No basta con que sea correcta.
# ---------------------------------------------------------------------------
#  `g.15` pide evidencia «trazable»; una procedencia que sólo existe en la cabeza de quien
#  escribió el `sys.path` no es trazable. Aquí se publica de dónde salió cada módulo del
#  aparato, cuántas entradas del lanzador se retiraron, y si el `--repo` que se está
#  juzgando es o no el árbol del que sale el propio aparato.
MODULOS_DEL_APARATO = ("arboles", "admision", "gobierno")

CODIGO_DE_PROCEDENCIA = 5


def _origen_de(fichero):
    """Nunca una ruta absoluta del anfitrión: la evidencia se publica (`E-15`)."""
    if not fichero:
        return "(sin fichero)"
    real = os.path.realpath(fichero)
    propia = os.path.realpath(_RAIZ_DEL_APARATO)
    if real == propia or real.startswith(propia + os.sep):
        return "aparato:" + os.path.relpath(real, propia)
    return "FUERA-DEL-APARATO:" + os.path.basename(real)


def procedencia(repo=None):
    """De dónde salió cada módulo, y bajo qué árbol se está juzgando."""
    modulos = {}
    for nombre in MODULOS_DEL_APARATO:
        modulo = sys.modules.get(nombre)
        modulos[nombre] = _origen_de(getattr(modulo, "__file__", None))
    salida = {
        "aparato": os.path.basename(_RAIZ_DEL_APARATO),
        "modulos": modulos,
        "entradas_del_lanzador_retiradas": len(RETIRADAS_DE_LA_RUTA),
        # `G-03` · lo que de verdad importa no es cuántas se RETIRARON, sino cuántas QUEDAN.
        #     Desde que el punto se reejecuta aislado, `PYTHONPATH` y el `cwd` no llegan a
        #     entrar en `sys.path` y no hay nada que retirar: un cero en «retiradas» pasó de
        #     significar «la purga no hizo nada» a significar «no hizo falta». La propiedad
        #     que se publica y que las pruebas exigen es ésta, que es la misma en los dos
        #     mundos: NINGUNA entrada del lanzador está en la ruta de importación.
        "entradas_del_lanzador_presentes": len(
            _entradas_del_lanzador()
            & {_os.path.realpath(entrada) for entrada in _sys.path if entrada}),
        "aislamiento_de_arranque": dict(AISLAMIENTO.get("flags") or {}),
        "ruta_de_importacion": [_origen_de(e) if e else "(cwd)" for e in sys.path[:3]],
    }
    if repo:
        arbol_del_aparato = os.path.dirname(os.path.dirname(os.path.dirname(
            _RAIZ_DEL_APARATO)))
        salida["repo"] = os.path.basename(os.path.abspath(repo))
        salida["repo_es_el_arbol_del_aparato"] = (
            os.path.realpath(repo) == os.path.realpath(arbol_del_aparato))
    return salida


def exigir_procedencia_del_aparato():
    """FALLO CERRADO si un módulo del aparato no sale del aparato. `E-10`.

    Es la mitad que la purga no puede cubrir: purgar impide que un homónimo ENTRE, y esto
    comprueba que ninguno ENTRÓ. Las dos hacen falta, porque la ruta de importación se puede
    modificar de más formas de las que una purga puede prever.
    """
    intrusos = {nombre: origen for nombre, origen in procedencia()["modulos"].items()
                if origen.startswith("FUERA-DEL-APARATO") or origen == "(sin fichero)"}
    if intrusos:
        sys.stderr.write(
            "[PROCEDENCIA_NO_FIABLE] módulos del aparato importados desde fuera del "
            "aparato: " + ", ".join(sorted(intrusos)) + ". El veredicto lo emitiría un "
            "código que este punto ejecutable no controla, y NO se emite\n")
        return CODIGO_DE_PROCEDENCIA
    return None


_TABLA_DE_FALLOS = (
    ((ErrorDeAdaptador,), "error-del-adaptador"),
    ((ErrorDeContencion,), "error-de-contencion"),
    ((ErrorDeArboles, ErrorDeAdmision, ErrorDeGobierno, ErrorDeEstado,
      ErrorDeIdentidad), "error-del-kernel"),
)


# ---------------------------------------------------------------------------
#  `E-15` · NINGÚN ERROR TIPADO SALE DE `main()` COMO TRAZA
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR: `adaptadores.contrato.CapacidadNoSoportada`
#  escapaba de `main()` como TRACEBACK con rutas absolutas del anfitrión, `stdout` vacío y
#  código 1 —el mismo que un fallo tipado—, de modo que un guion no podía distinguir «la
#  operación falló» de «el programa reventó». Matiz medido y conservado: hay DOS clases
#  homónimas `CapacidadNoSoportada`. La del RUNTIME (`runtime/errores.py`) SÍ se capturaba y
#  producía `[CAPACIDAD_NO_SOPORTADA] ...` limpio; la del ADAPTADOR
#  (`adaptadores/contrato.py`) es otra raíz —`ErrorDeAdaptador`— y no la capturaba nadie.
#  El contrato del adaptador declara esa separación a propósito, así que la corrección no es
#  fundir las jerarquías: es que el punto ejecutable las conozca TODAS.
#
#  DECISIÓN · un código de salida POR CLASE DE FALLO, y los ya publicados no se mueven
#      Alternativas: (a) un único código 1 para todo lo tipado; (b) un código por clase.
#      Se elige (b) porque `E-15` lo pide y porque un `&&` de un guion necesita distinguir
#      «entrada mal escrita» de «el anfitrión no puede contener» de «no hay adaptador». Lo
#      que NO se mueve es lo ya publicado: 0 éxito, 1 fallo tipado del kernel, 2 uso, 70
#      corte inyectado. Cambiarlos rompería guiones que hoy funcionan, y `E-15` pide
#      estabilidad, no renumeración.
CODIGOS_DE_SALIDA = {
    "exito": 0,
    "error-del-kernel": 1,
    "uso-incorrecto": 2,
    "error-del-adaptador": 3,
    "error-de-contencion": 4,
    "procedencia-no-fiable": 5,
}


def _sin_rutas_del_anfitrion(texto):
    """Ninguna salida publica el árbol de directorios de quien ejecuta. `E-15`.

    Misma regla que `registrar_evidencia.py` aplica a la evidencia publicada: la raíz se
    sustituye por `<raiz>`, de la más larga a la más corta. Se aplica AQUÍ, en la puerta de
    salida, y no en cada `raise`: una garantía que dependa de que cada sitio se acuerde no
    es una garantía.
    """
    arbol = os.path.dirname(os.path.dirname(os.path.dirname(_RAIZ_DEL_APARATO)))
    for ruta in sorted({os.path.abspath(arbol), os.path.realpath(arbol),
                        os.path.abspath(_RAIZ_DEL_APARATO),
                        os.path.realpath(_RAIZ_DEL_APARATO)}, key=len, reverse=True):
        if ruta and ruta != os.sep:
            texto = texto.replace(ruta, "<raiz>")
    return texto


def _clase_de_fallo(error):
    """La CLASE de fallo de un error tipado, o `None` si no lo es."""
    for clases, clave in _TABLA_DE_FALLOS:
        if isinstance(error, clases):
            return clave
    return None


def _publicar_fallo(argumentos, error, clase):
    """`stderr` útil, salida ESTRUCTURADA y código estable. Nunca una traza."""
    codigo = CODIGOS_DE_SALIDA[clase]
    detalle = error.a_dict() if hasattr(error, "a_dict") else {
        "codigo": getattr(error, "codigo", type(error).__name__),
        "detalle": str(error),
    }
    estructura = {"error": detalle, "clase_de_fallo": clase, "codigo_de_salida": codigo}
    # `stdout` conserva EXACTAMENTE lo que ya publicaba con `--json`: quien lo consuma hoy
    # sigue leyendo lo mismo. Lo que se añade es que `stderr` lleve siempre las dos cosas
    # —la línea legible y la estructura—, también cuando no se pidió `--json`.
    if getattr(argumentos, "json", False):
        sys.stdout.write(_sin_rutas_del_anfitrion(_volcar({"error": detalle})) + "\n")
    sys.stderr.write(_sin_rutas_del_anfitrion(str(error)) + "\n")
    sys.stderr.write(_sin_rutas_del_anfitrion(_volcar(estructura)) + "\n")
    return codigo


def _volcar(objeto):
    return json.dumps(objeto, sort_keys=True, ensure_ascii=False, indent=2)


def _emitir(argumentos, datos, legible):
    if getattr(argumentos, "legible", False):
        sys.stdout.write("\n".join(legible) + "\n")
    else:
        sys.stdout.write(_volcar(datos) + "\n")
    return EXITO


def _uso(mensaje):
    sys.stderr.write("uso: " + mensaje + "\n")
    return USO


def _orden_conjunto(argumentos):
    """El CONJUNTO derivado, con la procedencia de cada árbol y su hallazgo."""
    conjunto = arboles.exigir_sin_duplicados(arboles.derivar(argumentos.repo))
    validacion = arboles.exigir_validas(argumentos.repo, conjunto)
    datos = {
        "esquema": 1,
        "punto": "V6-15",
        "sede": ("docs/evolucion/11-ARQUITECTURA-INTEGRADA.md §20.5 · las cabeceras "
                 "publicadas por cada gate en su documento inmutable"),
        "conjunto": [arbol.a_dict() for arbol in conjunto],
        "validacion": validacion,
    }
    legible = ["CONJUNTO DERIVADO DE ÁRBOLES ADVERSARIALES · `V6-15`"]
    for arbol in conjunto:
        legible.append("  " + arbol.ordinal + "  " + arbol.documento
                       + ":" + str(arbol.linea)
                       + "  cerrado por " + ", ".join(arbol.hallazgos))
    return _emitir(argumentos, datos, legible)


def _orden_cruce(argumentos):
    """Las DOS restas de cierre, sin ejecutar la matriz."""
    conjunto = arboles.exigir_sin_duplicados(arboles.derivar(argumentos.repo))
    arboles.exigir_validas(argumentos.repo, conjunto)
    cruce = arboles.exigir_cobertura(conjunto)
    legible = [
        "entrada − suite : " + (", ".join(cruce["entrada_menos_suite"]) or "∅"),
        "suite − entrada : " + (", ".join(cruce["suite_menos_entrada"]) or "∅"),
    ]
    return _emitir(argumentos, cruce, legible)


def _orden_suite(argumentos):
    """La suite entera: derivación, cruce y matriz de cuatro columnas."""
    informe = arboles.ejecutar(argumentos.repo,
                               censar_el_codigo=argumentos.censar_el_codigo)
    legible = ["MATRIZ ADVERSARIAL DERIVADA · `V6-15`"]
    for fila in informe["matriz"]:
        legible.append(
            "  " + fila["ordinal"] + " · " + fila["fixture"]
            + "  sano=VERDE · ataque=EXISTE · vulnerable="
            + fila["la_version_vulnerable_lo_acepta"]["veredicto"]
            + " · vigente=ROJO por " + fila["la_vigente_lo_rechaza"]["propiedad"][:60]
        )
    legible.append("entrada − suite : "
                   + (", ".join(informe["cruce"]["entrada_menos_suite"]) or "∅"))
    legible.append("suite − entrada : "
                   + (", ".join(informe["cruce"]["suite_menos_entrada"]) or "∅"))
    if not informe["ok"]:
        sys.stdout.write(_volcar(informe) + "\n")
        sys.stderr.write("la suite de árboles adversariales NO cierra\n")
        return FALLO
    return _emitir(argumentos, informe, legible)


def _orden_procedencia(argumentos):
    """`E-10` · publica de dónde sale cada módulo, sin emitir ningún veredicto.

    `ADJ-M2` · HECHO REPRODUCIDO ANTES DE CORREGIR: los CINCO puntos ejecutables llevaban
    el comentario «`E-10` · la PROCEDENCIA se PUBLICA. No basta con que sea correcta.» y
    calculaban `procedencia()`, pero sólo `ads_admision.py` tenía una ORDEN que la
    publicara. Medido en las cinco tablas `ORDENES`: 1 de 5. En los otros cuatro la
    procedencia se calculaba **para uso interno de `exigir_procedencia_del_aparato()`** y
    no llegaba a ninguna salida, de modo que el comentario prometía algo que el fichero no
    hacía y nadie podía comprobar la procedencia de este aparato sin leer su código.

    DECISIÓN · se PUBLICA en los cinco, en vez de retirar el comentario de los cuatro
        Alternativas: (a) retirar el comentario donde no hay orden; (b) añadir la orden
        donde falta.
        Se elige (b). `g.15` pide evidencia TRAZABLE, y una procedencia que sólo existe
        dentro del proceso no lo es: cuando un veredicto se discute, la primera pregunta es
        de dónde salió el código que lo emitió, y sin orden hay que responderla leyendo
        fuentes. Retirar el comentario habría alineado el texto con el árbol **bajando** la
        garantía, y `E-10` nació precisamente de un aparato que importaba módulos que no
        controlaba. El coste es una orden de diagnóstico por punto ejecutable; el precio de
        no tenerla ya se pagó una vez.
    """
    datos = procedencia(argumentos.repo)
    legible = ["aparato       " + datos["aparato"],
               "repo          " + str(datos.get("repo")),
               "mismo árbol   " + ("si" if datos.get("repo_es_el_arbol_del_aparato")
                                   else "NO"),
               "retiradas     " + str(datos["entradas_del_lanzador_retiradas"])]
    for modulo in sorted(datos["modulos"]):
        legible.append("  modulo  " + modulo + "  " + datos["modulos"][modulo])
    return _emitir(argumentos, datos, legible)


ORDENES = {
    "conjunto": _orden_conjunto,
    "cruce": _orden_cruce,
    "procedencia": _orden_procedencia,
    "suite": _orden_suite,
}

# Las órdenes que NO necesitan un `--repo`: `procedencia` habla del APARATO, no del árbol
# juzgado, y exigirle un repositorio impediría usarla justo cuando se sospecha del aparato.
ORDENES_SIN_REPO = ("procedencia",)


def construir_analizador():
    comun = argparse.ArgumentParser(add_help=False)
    comun.add_argument("--repo", default=argparse.SUPPRESS,
                       help="raíz del repositorio cuya sede documental se deriva")
    comun.add_argument("--legible", action="store_true", default=argparse.SUPPRESS,
                       help="salida para leer a ojo; la evidencia es el JSON")
    comun.add_argument("--censar-el-codigo", dest="censar_el_codigo",
                       action="store_true", default=argparse.SUPPRESS,
                       help="ejecuta además el censo derivado del código en cada fixture")

    analizador = argparse.ArgumentParser(
        prog="ads_arboles", parents=[comun],
        description="derivador y suite de los árboles adversariales de `V6-15`",
    )
    ordenes = analizador.add_subparsers(dest="orden", required=True)
    for nombre in sorted(ORDENES):
        ordenes.add_parser(nombre, parents=[comun])
    return analizador


def main(argv=None):
    analizador = construir_analizador()
    argumentos = analizador.parse_args(argv)
    for nombre, valor in (("repo", None), ("legible", False),
                          ("censar_el_codigo", False)):
        if not hasattr(argumentos, nombre):
            setattr(argumentos, nombre, valor)
    if not argumentos.repo and argumentos.orden not in ORDENES_SIN_REPO:
        return _uso("falta --repo: la sede del conjunto es el árbol documental")
    if argumentos.repo:
        argumentos.repo = os.path.abspath(argumentos.repo)
    ejecutar = ORDENES.get(argumentos.orden)
    if ejecutar is None:
        return _uso("orden desconocida: " + str(argumentos.orden))
    # `E-10` · antes de nada, de dónde ha salido lo que va a juzgar.
    intruso = exigir_procedencia_del_aparato()
    if intruso is not None:
        return intruso
    try:
        return ejecutar(argumentos)
    except BaseException as error:                                    # noqa: BLE001
        # `E-15` · toda jerarquía TIPADA que pueda alcanzar este `main()` sale por aquí, con
        # su clase de fallo y su código estable. Lo que NO es tipado se vuelve a levantar
        # tal cual: convertir un defecto de programación en un código de salida limpio lo
        # escondería, y eso es lo contrario de lo que `E-15` pide.
        clase = _clase_de_fallo(error)
        if clase is None:
            raise
        return _publicar_fallo(argumentos, error, clase)


if __name__ == "__main__":
    sys.exit(main())
