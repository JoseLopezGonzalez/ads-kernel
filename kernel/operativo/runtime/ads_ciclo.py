#!/usr/bin/env python3
"""ads_ciclo — punto ejecutable del CICLO de `§7.2`, de `Continúa` y de los MACROCIRCUITOS.

    python3 kernel/operativo/runtime/ads_ciclo.py --repo <dir> <orden> [opciones]

Órdenes: `encuadrar` · `componer` · `materializar` · `planificar` · `ciclo` · `continuar` ·
`macrocircuito`.

Códigos de salida:  0 éxito · 1 fallo de la operación (error tipado) · 2 uso incorrecto.

DECISIÓN · `--repo`, `--instancia`, `--kernel` y `--json` se aceptan ANTES y DESPUÉS
    Es el patrón que ya usan `ads_estado.py` y `ads_runtime.py`, y por la misma razón: una
    CLI que sólo admite una de las dos posiciones convierte un tecleo en un error de uso, y
    quien la invoca desde un guion lo descubre en producción. Las opciones PROPIAS de cada
    orden —`--adaptador-local`, `--materia`, `--fase`…— van DESPUÉS de la orden, que es
    donde el subanalizador las declara.

DECISIÓN · el subanalizador guarda en `subcomando`, y no en `orden`
    Defecto MEDIDO, no hipotético: la orden `planificar` declara `--orden`, un fichero JSON
    con la orden de adaptador de cada capacidad, y `argparse` deriva de ese nombre el
    destino `orden`. Con el subanalizador guardando también en `orden`, el valor por defecto
    de la opción PISABA el nombre del subcomando y `planificar` salía por «uso incorrecto»
    sin haber hecho nada. Las dos cosas se llaman «orden» en este dominio —la del Owner y la
    del adaptador— y por eso la colisión era fácil; el destino del subanalizador se llama
    ahora `subcomando`, que no colisiona con nada. Lo comprueba `T202`.

DECISIÓN · las CUATRO jerarquías de error se capturan POR SEPARADO
    `ErrorDeEstado`, `ErrorDeRuntime`, `ErrorDeCiclo` y `ErrorDeMacrocircuito` son cuatro
    raíces distintas a propósito. Se tratan con el mismo código de salida y el mismo
    formato, pero en cuatro `except` distintos: un `except (A, B, C, D)` escondería que son
    cuatro contratos, y el día que uno gane tratamiento propio habría que descubrirlo.

DECISIÓN · `--json` es DETERMINISTA y NINGUNA salida imprime rutas absolutas
    `sort_keys=True`, sin duración, sin pid y sin instancia dentro del plan de continuación.
    Las cuatro jerarquías sanean la ruta en su constructor reutilizando
    `estado.errores.relativizar`, así que la garantía no depende de que cada `raise` se
    acuerde. No se imprime traza: el código y el detalle son el contrato.

DECISIÓN · la orden `ciclo` NO despacha por su cuenta si no hay adaptador, y lo dice
    Sin `--adaptador-local` no hay con qué ejecutar, y la respuesta correcta es
    `CAPACIDAD_NO_SOPORTADA` —un error tipado— y no un cuelgue ni un éxito vacío.
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

import ciclo                                                          # noqa: E402
import macrocircuitos                                                 # noqa: E402
import runtime                                                        # noqa: E402
from ciclo.errores import ErrorDeCiclo                                # noqa: E402
from estado.errores import ErrorDeEstado                              # noqa: E402
from macrocircuitos.errores import ErrorDeMacrocircuito               # noqa: E402
from runtime.errores import ErrorDeRuntime                            # noqa: E402

from adaptadores.contrato import ErrorDeAdaptador               # noqa: E402
from admision.errores import ErrorDeAdmision                         # noqa: E402
from contencion.errores import ErrorDeContencion                     # noqa: E402
from gobierno.errores import ErrorDeGobierno                         # noqa: E402
from identidad.errores import ErrorDeIdentidad                       # noqa: E402

EXITO, FALLO, USO = 0, 1, 2


# ---------------------------------------------------------------------------
#  `E-10` · la PROCEDENCIA se PUBLICA. No basta con que sea correcta.
# ---------------------------------------------------------------------------
#  `g.15` pide evidencia «trazable»; una procedencia que sólo existe en la cabeza de quien
#  escribió el `sys.path` no es trazable. Aquí se publica de dónde salió cada módulo del
#  aparato, cuántas entradas del lanzador se retiraron, y si el `--repo` que se está
#  juzgando es o no el árbol del que sale el propio aparato.
MODULOS_DEL_APARATO = ("ciclo", "macrocircuitos", "runtime", "estado")

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
    ((ErrorDeCiclo, ErrorDeMacrocircuito, ErrorDeRuntime, ErrorDeEstado,
      ErrorDeAdmision, ErrorDeGobierno, ErrorDeIdentidad), "error-del-kernel"),
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

# `ADJ-M2` · `procedencia` entra en ESTA tabla, y no en una tabla aparte de «órdenes de
# diagnóstico», porque la tabla `ORDENES` es lo que el gate MIDIÓ para encontrar el defecto:
# los cinco puntos ejecutables declaraban «la PROCEDENCIA se PUBLICA» y sólo uno la tenía
# aquí. Publicarla en otro sitio la escondería justo de la medición que la echó en falta.
#
# CONSECUENCIA CONOCIDA, dicha para que nadie la diagnostique dos veces: `test_ciclo.py`
# —`test_79`, T202— y `test_runtime.py` —`test_2028`— ENUMERAN estas tablas con una lista
# literal escrita a mano, y por eso fallan hasta que esa lista incluya `procedencia`. Las
# dos baterías están fuera de la zona de esta corrección; la petición al coordinador es
# añadir el nombre, y mejor aún derivar la lista en vez de escribirla.
ORDENES = ("encuadrar", "componer", "materializar", "planificar", "ciclo", "continuar",
           "macrocircuito", "procedencia")

# Las órdenes que NO necesitan `--repo`. Ver `orden_procedencia`.
ORDENES_SIN_REPO = ("procedencia",)


def _volcar(objeto):
    """JSON determinista: mismas claves, mismo orden, mismos bytes."""
    return json.dumps(objeto, sort_keys=True, ensure_ascii=False, indent=2)


def _emitir(argumentos, objeto, lineas):
    if argumentos.json:
        print(_volcar(objeto))
    else:
        for linea in lineas:
            print(linea)
    return EXITO


def _corpus(argumentos):
    return ciclo.Corpus(argumentos.kernel) if argumentos.kernel else ciclo.Corpus()



# ---------------------------------------------------------------------------
#  `E-16` · LA POLÍTICA DE CONTENCIÓN, CABLEADA DE VERDAD
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR: la cadena `contencion` no aparecía en NINGUNO de los
#  cinco `ads_*.py`, ni en `ciclo/`, ni en `runtime/`. El paquete `contencion/` estaba
#  construido y probado, y `adaptadores/proceso.py` aceptaba `politica_de_contencion=...`,
#  pero NINGÚN punto ejecutable podía pasarla: el camino productivo lanzaba siempre el
#  adaptador sin política, es decir, con `killpg` y su límite medido —el bisnieto que hace
#  `setsid` ESCAPA—. La política existía y no era alcanzable.
#
#  DECISIÓN · se PIDE por la línea de órdenes, y no se activa sola
#      Alternativas: (a) activarla siempre; (b) una variable de entorno; (c) una opción.
#      Se elige (c). Con (a) cambiaría el comportamiento de todo despliegue existente sin que
#      nadie lo decidiera, y en un anfitrión sin contención fuerte el fallo cerrado dejaría
#      de ejecutar lo que hoy ejecuta. Con (b) la decisión no aparece en la orden que queda
#      en la evidencia —es el mismo criterio que `--registro-en-pruebas` ya aplica—. Con (c)
#      la política se ve en la línea, se publica en la evidencia y quien no la pide obtiene
#      exactamente lo de antes, con su límite declarado.
#
#  DECISIÓN · sin backend fuerte se FALLA CERRADO al construir, y no se degrada
#      `AdaptadorDeProcesoLocal` elige el backend en su constructor, de modo que un anfitrión
#      que no puede contener detiene el proceso ANTES de adquirir ningún lease y de abrir
#      ningún recibo. CERO ejecución, y nunca «caigo al débil y sigo».
def _politica_de_contencion(argumentos):
    """La `contencion.Politica` que la línea de órdenes pide, o `None` si no pide ninguna."""
    nivel = getattr(argumentos, "contencion", None)
    backend = getattr(argumentos, "contencion_backend", None)
    if not nivel and not backend:
        return None
    import contencion                                                 # noqa: PLC0415
    return contencion.Politica(nivel or contencion.ARBOL_DE_PROCESOS, backend=backend)

def _registro(argumentos):
    if getattr(argumentos, "adaptador_local", None):
        import adaptadores
        return adaptadores.RegistroDeAdaptadores([
            adaptadores.AdaptadorDeProcesoLocal(
                argumentos.adaptador_local,
                politica_de_contencion=_politica_de_contencion(argumentos)),
        ])
    return None


def _abrir(argumentos):
    return runtime.Runtime(
        argumentos.repo, instancia=argumentos.instancia,
        registro_de_adaptadores=_registro(argumentos),
    ).abrir()


def _entrada(argumentos):
    """La entrada del Owner, leída de un fichero JSON o compuesta de las opciones."""
    if argumentos.entrada:
        with open(argumentos.entrada, "r", encoding="utf-8") as manejador:
            return json.load(manejador)
    return {
        "clase": argumentos.clase,
        "expresion_literal": argumentos.expresion or "",
        "canal": argumentos.canal or "",
        "fecha": argumentos.fecha or "",
        "resultado_perseguido": argumentos.resultado or "",
        "evidencia_de_cierre": list(argumentos.evidencia or []),
        "anclaje_terminado": bool(argumentos.anclaje),
        "materia": argumentos.materia or "",
        "estado_del_objeto": argumentos.estado_del_objeto or "",
    }


def _orden_por_capacidad(argumentos, capacidades):
    """La orden de adaptador de cada capacidad. Sin ella un paquete no es despachable."""
    if argumentos.orden:
        with open(argumentos.orden, "r", encoding="utf-8") as manejador:
            return json.load(manejador)
    plantilla = {
        "adaptador": argumentos.adaptador or "proceso-local",
        "operacion": "ejecutar",
        "argumentos": list(argumentos.argumento or []),
        "limite_segundos": argumentos.limite_segundos,
    }
    return {capacidad: dict(plantilla) for capacidad in capacidades}


# --------------------------------------------------------------------- órdenes
def orden_encuadrar(argumentos):
    marco = ciclo.encuadrar(argumentos.repo, _entrada(argumentos), corpus=_corpus(argumentos))
    return _emitir(argumentos, marco, [
        "encuadre      " + marco["id"],
        "producto      " + marco["producto"],
        "clase         " + marco["clase"],
        "crea trabajo  " + ("si" if marco["crea_trabajo"] else "no"),
        "proceso       " + str(marco["proceso"]),
        "capacidades   " + (", ".join(marco["capacidades_necesarias"]) or "(ninguna)"),
        "fuentes       " + (", ".join(f["id"] for f in marco["fuentes"]["fuentes"])
                            or "(ninguna declarada)"),
    ])


def orden_componer(argumentos):
    corpus = _corpus(argumentos)
    marco = ciclo.encuadrar(argumentos.repo, _entrada(argumentos), corpus=corpus)
    ciclo.encuadre.exigir_que_crea_trabajo(marco)
    ruta = ciclo.componer(
        marco, corpus=corpus, fase=argumentos.fase,
        condiciones_verdaderas=list(argumentos.condicion or []),
        propietario_declarado=argumentos.propietario,
        capacidades_de_la_fase=list(argumentos.capacidad_de_la_fase or []),
    )
    lineas = [
        "ruta          " + ruta["id"],
        "proceso       " + ruta["proceso"],
        "propietario   " + ruta["propietario_global"] + " (" + ruta["origen_del_propietario"] + ")",
    ]
    for participante in ruta["participantes"]:
        lineas.append("  via " + str(participante["via"]) + "  " + participante["capacidad"]
                      + "  " + participante["motivo"])
    for no_activada in ruta["no_activadas"]:
        lineas.append("  NO    " + no_activada["capacidad"] + "  " + no_activada["motivo"])
    return _emitir(argumentos, ruta, lineas)


def orden_materializar(argumentos):
    # `C4` paso 4 necesita el catálogo de modelos, y su sede es el `PROFILE` del CONTROL
    # REPO —`C2`: el adaptador «vive en el PROFILE del proyecto o en la instalación, NUNCA
    # en el kernel»—. Sin reenviar `--repo` la orden materializaba SIEMPRE sin catálogo, y
    # el fallo cerrado correcto —ningún rol recibe agente— se leía como un equipo vacío.
    equipo = ciclo.materializar(
        argumentos.capacidad, corpus=_corpus(argumentos),
        composiciones_verdaderas=list(argumentos.composicion or []),
        condiciones_de_rol=list(argumentos.condicion or []),
        slots=argumentos.slots,
        control_repo=getattr(argumentos, "repo", None),
    )
    lineas = [
        "equipo        " + equipo["id"],
        "capacidad     " + equipo["capacidad"],
        "composicion   " + equipo["composicion"],
        "estado        " + str(equipo.get("estado") or ""),
        "catalogo      " + _catalogo(equipo),
        "roles         " + (", ".join(_rol_con_agente(r) for r in equipo["roles"])
                            or "(ninguno)"),
        "esperando     " + (", ".join(_rol_con_agente(r)
                                      for r in equipo["esperando_capacidad"])
                            or "(ninguno)"),
        "bloqueados    " + (", ".join(_rol_con_agente(r)
                                      for r in equipo.get("bloqueados") or [])
                            or "(ninguno)"),
    ]
    return _emitir(argumentos, equipo, lineas)


def _catalogo(equipo):
    """La sede y la huella del catálogo, o el motivo por el que no hay ninguno."""
    catalogo = equipo.get("catalogo") or {}
    if not catalogo.get("declarado"):
        return "(no declarado) " + str(catalogo.get("motivo") or "")
    modelos = catalogo.get("modelos") or []
    if not isinstance(modelos, list):
        modelos = [modelos]
    return (str(catalogo.get("sede") or "") + " · " + str(len(modelos))
            + " modelos: " + ", ".join(str(m) for m in modelos))


def _rol_con_agente(fila):
    """`rol → modelo`. Un rol sin agente se IMPRIME sin agente, no se calla."""
    modelo = fila.get("modelo")
    return fila["rol"] + (" → " + modelo if modelo else " → (sin agente)")


def orden_planificar(argumentos):
    corpus = _corpus(argumentos)
    marco = ciclo.encuadrar(argumentos.repo, _entrada(argumentos), corpus=corpus)
    ciclo.encuadre.exigir_que_crea_trabajo(marco)
    ruta = ciclo.componer(
        marco, corpus=corpus, fase=argumentos.fase,
        condiciones_verdaderas=list(argumentos.condicion or []),
        propietario_declarado=argumentos.propietario,
        capacidades_de_la_fase=list(argumentos.capacidad_de_la_fase or []),
    )
    with _abrir(argumentos) as rt:
        planificador = ciclo.Planificador(rt, corpus=corpus)
        capacidades = sorted({p["capacidad"] for p in ruta["participantes"]})
        plan = planificador.planificar(
            marco, ruta, orden_por_capacidad=_orden_por_capacidad(argumentos, capacidades),
        )
    return _emitir(argumentos, plan, [
        "plan          " + plan["id"],
        "item          " + plan["item"],
        "proceso       " + plan["proceso"],
        "paquetes      " + ", ".join(plan["paquetes"]),
        "intervencion  " + plan["intervencion_del_owner"],
    ])


def orden_ciclo(argumentos):
    with _abrir(argumentos) as rt:
        informe = ciclo.barrido(rt, maximo=argumentos.maximo, origen="ads_ciclo")
    return _emitir(argumentos, informe, [
        "revision      " + str(informe["revision_inicial"]) + " → "
        + str(informe["revision_final"]),
        "elegibles     " + (", ".join(informe["elegibles"]) or "(ninguno)"),
        "atendidos     " + (", ".join(
            str(a.get("paquete")) + ":" + str(a.get("desenlace"))
            for a in informe["atendidos"]) or "(ninguno)"),
    ])


def orden_continuar(argumentos):
    modo = ciclo.MODO_EJECUCION if argumentos.ejecutar else ciclo.MODO_PLAN
    with _abrir(argumentos) as rt:
        plan = ciclo.Continuacion(rt, corpus=_corpus(argumentos)).plan(
            modo=modo, frente=argumentos.frente, reparar=argumentos.reparar,
            no_interactivo=not argumentos.interactivo,
        )
    return _emitir(argumentos, plan, ciclo.como_texto(plan) + [
        "huella        " + plan["huella"],
    ])


def orden_macrocircuito(argumentos):
    corpus = _corpus(argumentos)
    if argumentos.censo:
        censo = {
            identificador: {
                "nombre": macrocircuitos.macrocircuito(identificador)["nombre"],
                "fases": [f["fase"] for f in
                          macrocircuitos.macrocircuito(identificador)["fases"]],
                "secuencia": list(macrocircuitos.secuencia_de_procesos(identificador)),
            }
            for identificador in macrocircuitos.IDENTIFICADORES
        }
        macrocircuitos.comprobar(corpus)
        return _emitir(argumentos, censo, [
            identificador + "  " + censo[identificador]["nombre"] + "  ["
            + " ".join(censo[identificador]["secuencia"]) + "]"
            for identificador in macrocircuitos.IDENTIFICADORES
        ])
    if not argumentos.id:
        print("falta `--id` con uno de " + ", ".join(macrocircuitos.IDENTIFICADORES),
              file=sys.stderr)
        return USO
    circuito = macrocircuitos.Macrocircuito(
        argumentos.id, argumentos.repo, corpus=corpus,
        instancia=argumentos.instancia, registro_de_adaptadores=_registro(argumentos),
    )
    resultado = circuito.ejecutar_fase0(
        disparador=argumentos.disparador,
        comprobaciones_superadas=list(argumentos.comprobacion or []),
        evidencia=list(argumentos.evidencia or []),
    )
    salida = {
        "macrocircuito": argumentos.id,
        "sujeto": resultado["sujeto"],
        "declaracion": resultado["declaracion"]["id"],
        "dictamen": resultado["dictamen"]["dictamen"],
        "huella_del_sujeto": resultado["declaracion"]["huella_del_sujeto"],
    }
    if argumentos.abrir:
        circuito.abrir()
        try:
            salida["autoridad"] = circuito.autoridad["macrocircuito"]
            salida["estado"] = circuito.estado()
        finally:
            circuito.cerrar()
    return _emitir(argumentos, salida, [
        "macrocircuito " + argumentos.id,
        "ejecucion     " + resultado["sujeto"]["ejecucion_del_macrocircuito"],
        "declaracion   " + resultado["declaracion"]["id"],
        "dictamen      " + resultado["dictamen"]["dictamen"],
    ])


def orden_procedencia(argumentos):
    """`E-10` · publica de dónde sale cada módulo, sin encuadrar nada.

    `ADJ-M2` · los cinco puntos ejecutables declaraban «la PROCEDENCIA se PUBLICA» y sólo
    uno tenía orden que la publicara. La razón entera está en
    `ads_arboles._orden_procedencia`.
    """
    datos = procedencia(argumentos.repo)
    return _emitir(argumentos, datos, [
        "aparato       " + datos["aparato"],
        "repo          " + str(datos.get("repo")),
        "mismo árbol   " + ("si" if datos.get("repo_es_el_arbol_del_aparato") else "NO"),
        "retiradas     " + str(datos["entradas_del_lanzador_retiradas"]),
    ] + ["  modulo  " + m + "  " + datos["modulos"][m] for m in sorted(datos["modulos"])])


DESPACHADOR = {
    "procedencia": orden_procedencia,
    "encuadrar": orden_encuadrar,
    "componer": orden_componer,
    "materializar": orden_materializar,
    "planificar": orden_planificar,
    "ciclo": orden_ciclo,
    "continuar": orden_continuar,
    "macrocircuito": orden_macrocircuito,
}


def construir_analizador():
    comun = argparse.ArgumentParser(add_help=False)
    comun.add_argument("--repo", default=argparse.SUPPRESS)
    comun.add_argument("--instancia", default=argparse.SUPPRESS)
    comun.add_argument("--kernel", default=argparse.SUPPRESS)
    comun.add_argument("--json", action="store_true", default=argparse.SUPPRESS)

    analizador = argparse.ArgumentParser(
        prog="ads_ciclo", description="el ciclo de `§7.2`, `Continúa` y los macrocircuitos",
    )
    analizador.add_argument("--repo")
    analizador.add_argument("--instancia", default="ciclo-A")
    analizador.add_argument("--kernel")
    analizador.add_argument("--json", action="store_true")
    subordenes = analizador.add_subparsers(dest="subcomando")

    def entrada(sub):
        sub.add_argument("--entrada")
        sub.add_argument("--clase", default="candidato")
        sub.add_argument("--expresion")
        sub.add_argument("--canal")
        sub.add_argument("--fecha")
        sub.add_argument("--resultado")
        sub.add_argument("--evidencia", action="append")
        sub.add_argument("--anclaje", action="store_true")
        sub.add_argument("--materia")
        sub.add_argument("--estado-del-objeto", dest="estado_del_objeto")

    def ruta(sub):
        sub.add_argument("--fase", default="unica")
        sub.add_argument("--condicion", action="append")
        sub.add_argument("--propietario")
        sub.add_argument("--capacidad-de-la-fase", dest="capacidad_de_la_fase",
                         action="append")

    def orden_de_adaptador(sub):
        sub.add_argument("--orden")
        sub.add_argument("--adaptador", default="proceso-local")
        sub.add_argument("--argumento", action="append")
        sub.add_argument("--limite-segundos", dest="limite_segundos", type=float, default=60.0)
        sub.add_argument("--adaptador-local", dest="adaptador_local")
        sub.add_argument("--contencion", dest="contencion", default=None,
                         choices=("grupo-de-procesos", "arbol-de-procesos"),
                         help="`FD-5`: nivel de AISLAMIENTO exigido a la ejecución local. Sin backend que lo dé, FALLO CERRADO: no se ejecuta nada y no se degrada al débil")
        sub.add_argument("--contencion-backend", dest="contencion_backend",
                         default=None, help="pedir un backend concreto de contención. Es legítimo y queda registrado; si su nivel es inferior al exigido, FALLO CERRADO")

    uno = subordenes.add_parser("encuadrar", parents=[comun])
    entrada(uno)

    dos = subordenes.add_parser("componer", parents=[comun])
    entrada(dos)
    ruta(dos)

    tres = subordenes.add_parser("materializar", parents=[comun])
    tres.add_argument("--capacidad", required=True)
    tres.add_argument("--composicion", action="append")
    tres.add_argument("--condicion", action="append")
    tres.add_argument("--slots", type=int, default=4)

    cuatro = subordenes.add_parser("planificar", parents=[comun])
    entrada(cuatro)
    ruta(cuatro)
    orden_de_adaptador(cuatro)

    cinco = subordenes.add_parser("ciclo", parents=[comun])
    cinco.add_argument("--maximo", type=int, default=0)
    cinco.add_argument("--adaptador-local", dest="adaptador_local")
    cinco.add_argument("--contencion", dest="contencion", default=None,
                      choices=("grupo-de-procesos", "arbol-de-procesos"),
                      help="`FD-5`: nivel de AISLAMIENTO exigido a la ejecución local. Sin backend que lo dé, FALLO CERRADO: no se ejecuta nada y no se degrada al débil")
    cinco.add_argument("--contencion-backend", dest="contencion_backend",
                      default=None, help="pedir un backend concreto de contención. Es legítimo y queda registrado; si su nivel es inferior al exigido, FALLO CERRADO")

    seis = subordenes.add_parser("continuar", parents=[comun])
    seis.add_argument("--ejecutar", action="store_true")
    seis.add_argument("--reparar", action="store_true")
    seis.add_argument("--interactivo", action="store_true")
    seis.add_argument("--frente", type=int, default=1)
    seis.add_argument("--adaptador-local", dest="adaptador_local")
    seis.add_argument("--contencion", dest="contencion", default=None,
                      choices=("grupo-de-procesos", "arbol-de-procesos"),
                      help="`FD-5`: nivel de AISLAMIENTO exigido a la ejecución local. Sin backend que lo dé, FALLO CERRADO: no se ejecuta nada y no se degrada al débil")
    seis.add_argument("--contencion-backend", dest="contencion_backend",
                      default=None, help="pedir un backend concreto de contención. Es legítimo y queda registrado; si su nivel es inferior al exigido, FALLO CERRADO")

    siete = subordenes.add_parser("macrocircuito", parents=[comun])
    siete.add_argument("--id")
    siete.add_argument("--censo", action="store_true")
    siete.add_argument("--disparador")
    siete.add_argument("--comprobacion", action="append")
    siete.add_argument("--evidencia", action="append")
    siete.add_argument("--abrir", action="store_true")
    siete.add_argument("--adaptador-local", dest="adaptador_local")
    siete.add_argument("--contencion", dest="contencion", default=None,
                      choices=("grupo-de-procesos", "arbol-de-procesos"),
                      help="`FD-5`: nivel de AISLAMIENTO exigido a la ejecución local. Sin backend que lo dé, FALLO CERRADO: no se ejecuta nada y no se degrada al débil")
    siete.add_argument("--contencion-backend", dest="contencion_backend",
                      default=None, help="pedir un backend concreto de contención. Es legítimo y queda registrado; si su nivel es inferior al exigido, FALLO CERRADO")

    subordenes.add_parser("procedencia", parents=[comun])
    return analizador


def main(argv=None):
    analizador = construir_analizador()
    argumentos = analizador.parse_args(argv if argv is not None else sys.argv[1:])
    if not argumentos.subcomando:
        analizador.print_help(sys.stderr)
        return USO
    if argumentos.subcomando in ORDENES_SIN_REPO:
        pass
    elif argumentos.subcomando != "macrocircuito" or not argumentos.censo:
        if not argumentos.repo:
            print("falta `--repo <dir>`: sin control repo no hay nada que encuadrar",
                  file=sys.stderr)
            return USO
    # `E-10` · antes de nada, de dónde ha salido lo que va a juzgar.
    intruso = exigir_procedencia_del_aparato()
    if intruso is not None:
        return intruso
    try:
        return DESPACHADOR[argumentos.subcomando](argumentos)
    except (ErrorDeCiclo, ErrorDeMacrocircuito, ErrorDeRuntime, ErrorDeEstado) as error:
        # `E-15` · las cuatro raíces que esta CLI ya conocía conservan su código 1 y su
        # formato: lo publicado no se mueve. Lo que se añade abajo son las que ESCAPABAN.
        return _fallo(argumentos, error)
    except (ErrorDeAdaptador, ErrorDeContencion, ErrorDeAdmision, ErrorDeGobierno,
            ErrorDeIdentidad) as error:
        return _publicar_fallo(argumentos, error, _clase_de_fallo(error))
    except FileNotFoundError as error:
        print("no se encuentra el fichero: " + os.path.basename(str(error.filename or "")),
              file=sys.stderr)
        return USO
    except json.JSONDecodeError as error:
        print("JSON ilegible en la posición " + str(error.pos) + ": " + error.msg,
              file=sys.stderr)
        return USO


def _fallo(argumentos, error):
    if getattr(argumentos, "json", False):
        print(_volcar(error.a_dict()), file=sys.stderr)
    else:
        print(str(error), file=sys.stderr)
    return FALLO


if __name__ == "__main__":
    sys.exit(main())
