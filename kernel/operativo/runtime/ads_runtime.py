#!/usr/bin/env python3
"""ads_runtime — punto ejecutable del RUNTIME y del DISPATCHER del CONTROL REPO.

    python3 kernel/operativo/runtime/ads_runtime.py --repo <dir> --instancia <nombre> <orden>

Órdenes: `crear-item` · `crear-paquete` · `elegibles` · `adquirir` · `renovar` · `observar` ·
`reclamar` · `liberar` · `despachar` · `ciclo` · `pausar` · `reanudar` · `cancelar` ·
`vistas` · `estado-paquete`.

Códigos de salida:  0 éxito · 1 fallo de la operación (error tipado) · 2 uso incorrecto.

DECISIÓN · `--repo`, `--instancia`, `--paciencia` y `--json` se aceptan ANTES y DESPUÉS
    Es el patrón que ya usa `ads_estado.py`, y por la misma razón: una CLI que sólo admite
    una de las dos posiciones convierte un tecleo en un error de uso, y quien la invoca
    desde un script lo descubre en producción. `SUPPRESS` hace que el subanalizador no pise
    el valor puesto arriba cuando la opción no se repite.

DECISIÓN · NINGUNA salida imprime rutas absolutas de la máquina, tampoco las de error
    La evidencia de `F6` se publica. `ErrorDeRuntime` sanea la ruta en su constructor
    reutilizando `estado.errores.relativizar`, igual que hace el motor, así que la garantía
    no depende de que cada `raise` se acuerde. No se imprime traza: el código y el detalle
    son el contrato, y una traza publicaría el árbol de directorios de quien ejecuta.

DECISIÓN · las DOS jerarquías de error se capturan por separado
    `ErrorDeEstado` y `ErrorDeRuntime` son raíces distintas a propósito (ver
    `runtime/errores.py`). La CLI las trata con el mismo código de salida y el mismo
    formato, pero en dos `except` distintos: un `except (A, B)` escondería que son dos
    contratos, y el día que uno gane un tratamiento propio habría que descubrirlo.

DECISIÓN · `--registro-en-pruebas` existe, está marcado como tal y no es el camino normal
    `despachar` y `ciclo` necesitan un registro de adaptadores, y el productivo lo entrega
    el corte `V7` en `adaptadores/`. Mientras tanto, esta opción construye el
    `RegistroEnPruebas` del §4.4 sobre un directorio de trabajo. Sin ella, `despachar` y
    `ciclo` dan `CAPACIDAD_NO_SOPORTADA`, que es la respuesta correcta y no un cuelgue.
    Alternativa descartada: una variable de entorno. Una opción se ve en la línea de
    órdenes que queda en la evidencia; una variable de entorno, no.
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

import runtime                                                       # noqa: E402
from estado.errores import ErrorDeEstado                             # noqa: E402
from runtime.errores import ErrorDeRuntime                           # noqa: E402

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
MODULOS_DEL_APARATO = ("runtime", "estado")

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
    ((ErrorDeRuntime, ErrorDeEstado, ErrorDeAdmision, ErrorDeGobierno,
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
    """JSON determinista: mismas claves, mismo orden, mismos bytes."""
    return json.dumps(objeto, sort_keys=True, ensure_ascii=False, indent=2)


def _emitir(argumentos, objeto, lineas):
    if argumentos.json:
        print(_volcar(objeto))
    else:
        for linea in lineas:
            print(linea)
    return EXITO



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
    # EL ADAPTADOR REAL VA PRIMERO. `--adaptador-local` registra el adaptador de PROCESO
    # LOCAL del corte `V7`, que lanza un `subprocess` de verdad y mata de verdad. Es el que
    # usa el escenario extremo a extremo, y el que un despliegue usaría. El registro en
    # pruebas existe sólo para ejercitar el dispatcher sin adaptador, y por eso se declara
    # el segundo y nombrándose a sí mismo.
    if getattr(argumentos, "adaptador_local", None):
        import adaptadores
        return adaptadores.RegistroDeAdaptadores([
            adaptadores.AdaptadorDeProcesoLocal(
                argumentos.adaptador_local,
                politica_de_contencion=_politica_de_contencion(argumentos)),
        ])
    if not getattr(argumentos, "registro_en_pruebas", None):
        return None
    return runtime.RegistroEnPruebas([
        runtime.AdaptadorEnPruebas(argumentos.registro_en_pruebas,
                                   identificador="adaptador-en-pruebas",
                                   capacidades=["proceso-local"]),
    ])


def _abrir(argumentos):
    return runtime.Runtime(
        argumentos.repo, instancia=argumentos.instancia,
        paciencia=argumentos.paciencia,
        registro_de_adaptadores=_registro(argumentos),
    ).abrir()


def _lineas_de_lease(lease):
    return [
        "paquete       " + lease["paquete"],
        "titular       " + lease["titular"],
        "epoca         " + str(lease["epoca"]),
        "latido        " + str(lease["latido"]),
        "observado_por " + (", ".join(
            aspirante + "=" + str(anotacion["observaciones"])
            + "@" + str(anotacion["latido"])
            for aspirante, anotacion in sorted(lease["observado_por"].items())
        ) or "(nadie)"),
    ]


def _lineas_de_despacho(resumen):
    return [
        "paquete       " + resumen["paquete"],
        "desenlace     " + resumen["desenlace"],
        "estado        " + str(resumen.get("estado")),
        "intento       " + str(resumen.get("intento")) + " de "
        + str(resumen.get("max_intentos")),
        "efecto        " + str(resumen.get("efecto")),
        "decision      " + str(resumen.get("decision")),
        "repetido      " + ("si" if resumen.get("repetido") else "no"),
        "reconciliacion " + str(resumen.get("reconciliacion") or "(ninguna)"),
    ]


# --------------------------------------------------------------------- órdenes
def orden_crear_item(argumentos):
    with _abrir(argumentos) as rt:
        item = rt.crear_item(id=argumentos.id, titulo=argumentos.titulo,
                             motivo=argumentos.motivo)
    return _emitir(argumentos, item, [
        "item          " + item["id"],
        "titulo        " + item["titulo"],
    ])


def orden_crear_paquete(argumentos):
    orden = {
        "adaptador": argumentos.adaptador,
        "operacion": argumentos.operacion,
        "argumentos": list(argumentos.argumento or []),
        "limite_segundos": argumentos.limite_segundos,
    }
    with _abrir(argumentos) as rt:
        paquete = rt.crear_paquete(
            id=argumentos.id, item=argumentos.item,
            capacidades_requeridas=list(argumentos.capacidad or []),
            orden=orden, prioridad=argumentos.prioridad,
            max_intentos=argumentos.max_intentos,
            depende_de=list(argumentos.depende_de or []),
        )
    return _emitir(argumentos, paquete, [
        "paquete       " + paquete["id"],
        "item          " + paquete["item"],
        "estado        " + paquete["estado"],
        "prioridad     " + str(paquete["prioridad"]),
        "max_intentos  " + str(paquete["max_intentos"]),
        "capacidades   " + ", ".join(paquete["capacidades_requeridas"]),
    ])


def orden_elegibles(argumentos):
    # La RECUPERACIÓN se publica junto al trabajo elegible, y no es adorno: el §7 del corte
    # exige recuperar el estado ANTES de despachar, y una capacidad que no se puede observar
    # desde fuera no se puede demostrar. `marcado` es la que impide despachar: si la
    # recuperación terminó en MARCAR, la autoridad decide y el runtime no reparte trabajo.
    with _abrir(argumentos) as rt:
        elegibles = rt.elegibles()
        recuperacion = dict(rt.recuperacion or {})
        marcado = bool(rt.marcado)
    return _emitir(argumentos, {"elegibles": elegibles, "recuperacion": recuperacion,
                                "marcado": marcado}, [
        entrada["paquete"] + "  prioridad=" + str(entrada["prioridad"])
        + "  estado=" + entrada["estado"]
        + "  titular=" + str(entrada["titular"])
        for entrada in elegibles
    ] or ["(ninguno)"])


def orden_adquirir(argumentos):
    with _abrir(argumentos) as rt:
        lease = rt.adquirir(argumentos.paquete)
    return _emitir(argumentos, lease, _lineas_de_lease(lease))


def orden_renovar(argumentos):
    with _abrir(argumentos) as rt:
        lease = rt.renovar(argumentos.paquete)
    return _emitir(argumentos, lease, _lineas_de_lease(lease))


def orden_observar(argumentos):
    with _abrir(argumentos) as rt:
        lease = rt.observar(argumentos.paquete)
    return _emitir(argumentos, lease, _lineas_de_lease(lease))


def orden_reclamar(argumentos):
    with _abrir(argumentos) as rt:
        lease = rt.reclamar(argumentos.paquete)
    return _emitir(argumentos, lease, _lineas_de_lease(lease))


def orden_liberar(argumentos):
    with _abrir(argumentos) as rt:
        rt.liberar(argumentos.paquete)
    return _emitir(argumentos, {"paquete": argumentos.paquete, "liberado": True},
                   ["liberado      " + argumentos.paquete])


def orden_despachar(argumentos):
    with _abrir(argumentos) as rt:
        resumen = rt.despachar(argumentos.paquete)
    return _emitir(argumentos, resumen, _lineas_de_despacho(resumen))


def orden_ciclo(argumentos):
    with _abrir(argumentos) as rt:
        informe = rt.ciclo(maximo=argumentos.maximo)
    lineas = [
        "instancia     " + informe["instancia"],
        "ventana       " + informe["ventana"],
        "revision      " + str(informe["revision_inicial"]) + " → "
        + str(informe["revision_final"]),
        "elegibles     " + (", ".join(informe["elegibles"]) or "(ninguno)"),
        "reanudados    " + (", ".join(informe["reanudados"]) or "(ninguno)"),
        "liberados     " + (", ".join(informe["liberados"]) or "(ninguno)"),
        "pendencias    " + (", ".join(informe["reconciliaciones_pendientes"])
                            or "(ninguna)"),
    ]
    for atendido in informe["atendidos"]:
        lineas.append(
            "  " + atendido["paquete"] + "  " + atendido["desenlace"]
            + ("  " + atendido["codigo"] if atendido.get("codigo") else "")
        )
    return _emitir(argumentos, informe, lineas)


def _decision(argumentos, nombre):
    with _abrir(argumentos) as rt:
        paquete = getattr(rt, nombre)(argumentos.paquete, motivo=argumentos.motivo,
                                      autoridad=argumentos.autoridad)
    return _emitir(argumentos, paquete, [
        "paquete       " + paquete["id"],
        "estado        " + paquete["estado"],
        "autoridad     " + argumentos.autoridad,
    ])


def orden_pausar(argumentos):
    return _decision(argumentos, "pausar")


def orden_reanudar(argumentos):
    return _decision(argumentos, "reanudar")


def orden_cancelar(argumentos):
    return _decision(argumentos, "cancelar")


def orden_vistas(argumentos):
    with _abrir(argumentos) as rt:
        derivadas = rt.vistas()
    lineas = [
        "derivada      si",
        "revision      " + str(derivadas["revision"]),
        "ventana       " + derivadas["ventana"],
        "construyendo  " + (", ".join(e["paquete"] for e in
                                      derivadas["que_se_esta_construyendo"]) or "(nada)"),
        "bloqueado     " + (", ".join(e["paquete"] for e in
                                      derivadas["que_esta_bloqueado"]) or "(nada)"),
        "espera_owner  " + (", ".join(e["paquete"] for e in
                                      derivadas["que_espera_decision_del_owner"])
                            or "(nada)"),
        "reconciliar   " + (", ".join(r["registro"] for r in
                                      derivadas["reconciliaciones_abiertas"])
                            or "(nada)"),
        "recuento      " + (", ".join(estado + "=" + str(cuenta) for estado, cuenta
                                      in sorted(derivadas["recuento"].items()))
                            or "(sin paquetes)"),
    ]
    return _emitir(argumentos, derivadas, lineas)


def orden_estado_paquete(argumentos):
    with _abrir(argumentos) as rt:
        informe = rt.estado_de_paquete(argumentos.paquete)
    paquete = informe["paquete"]
    lineas = [
        "paquete       " + paquete["id"],
        "item          " + paquete["item"],
        "estado        " + paquete["estado"],
        "intentos      " + str(paquete["intentos"]) + " de " + str(paquete["max_intentos"]),
        "efecto        " + str(paquete["efecto"]),
        "acuse         " + ("si" if informe["acuse"] else "no"),
    ]
    if informe["lease"]:
        lineas.extend(_lineas_de_lease(informe["lease"]))
    else:
        lineas.append("lease         (ninguno)")
    return _emitir(argumentos, informe, lineas)


def orden_procedencia(argumentos):
    """`E-10` · publica de dónde sale cada módulo, sin abrir el runtime ni tomar lease.

    `ADJ-M2` · los cinco puntos ejecutables declaraban «la PROCEDENCIA se PUBLICA» y sólo
    uno tenía orden que la publicara. La razón entera está en
    `ads_arboles._orden_procedencia`. Aquí, además, esta orden **no adquiere ninguna
    instancia**: preguntar de dónde sale el dispatcher no puede exigir nombrar un titular.
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


# `ADJ-M2` · `procedencia` entra en ESTA tabla y no en una aparte: `ORDENES` es lo que el
# gate midió para encontrar el defecto, y publicarla en otro sitio la escondería de la
# medición que la echó en falta. CONSECUENCIA CONOCIDA: `test_runtime.py` enumera esta tabla
# con una lista literal y falla hasta que incluya `procedencia`; esa batería está fuera de la
# zona de esta corrección.
ORDENES = {
    "procedencia": orden_procedencia,
    "crear-item": orden_crear_item,
    "crear-paquete": orden_crear_paquete,
    "elegibles": orden_elegibles,
    "adquirir": orden_adquirir,
    "renovar": orden_renovar,
    "observar": orden_observar,
    "reclamar": orden_reclamar,
    "liberar": orden_liberar,
    "despachar": orden_despachar,
    "ciclo": orden_ciclo,
    "pausar": orden_pausar,
    "reanudar": orden_reanudar,
    "cancelar": orden_cancelar,
    "vistas": orden_vistas,
    "estado-paquete": orden_estado_paquete,
}

# Las órdenes que NO necesitan `--repo` ni `--instancia`. Ver `orden_procedencia`.
ORDENES_SIN_REPO = ("procedencia",)


def _uso(mensaje):
    sys.stderr.write("uso: " + mensaje + "\n")
    return USO


def construir_analizador():
    comun = argparse.ArgumentParser(add_help=False)
    comun.add_argument("--repo", default=argparse.SUPPRESS, help="ruta del CONTROL REPO")
    comun.add_argument("--instancia", default=argparse.SUPPRESS,
                       help="nombre de esta instancia del runtime")
    comun.add_argument("--paciencia", type=int, default=argparse.SUPPRESS,
                       help="observaciones consecutivas sin latido para reclamar")
    comun.add_argument("--adaptador-local", default=argparse.SUPPRESS, metavar="DIR",
                       help="espacio de trabajo del ADAPTADOR DE PROCESO LOCAL real (V7)")
    comun.add_argument("--registro-en-pruebas", default=argparse.SUPPRESS,
                       metavar="DIR", help="SÓLO PRUEBAS: registro mínimo del §4.4")
    comun.add_argument("--contencion", dest="contencion", default=argparse.SUPPRESS,
                       choices=("grupo-de-procesos", "arbol-de-procesos"),
                       help="`FD-5`: nivel de AISLAMIENTO exigido a la ejecución local. Sin backend que lo dé, FALLO CERRADO: no se ejecuta nada y no se degrada al débil")
    comun.add_argument("--contencion-backend", dest="contencion_backend",
                       default=argparse.SUPPRESS, help="pedir un backend concreto de contención. Es legítimo y queda registrado; si su nivel es inferior al exigido, FALLO CERRADO")
    comun.add_argument("--json", action="store_true", default=argparse.SUPPRESS,
                       help="salida JSON determinista")

    analizador = argparse.ArgumentParser(
        prog="ads_runtime", description="runtime y dispatcher del control repo de ADS",
    )
    analizador.add_argument("--repo", default=None, help="ruta del CONTROL REPO")
    analizador.add_argument("--instancia", default=None,
                            help="nombre de esta instancia del runtime")
    analizador.add_argument("--paciencia", type=int,
                            default=runtime.PACIENCIA_POR_DEFECTO,
                            help="observaciones consecutivas sin latido para reclamar")
    analizador.add_argument("--adaptador-local", default=None, metavar="DIR",
                            help="espacio de trabajo del ADAPTADOR DE PROCESO LOCAL real")
    analizador.add_argument("--registro-en-pruebas", default=None, metavar="DIR",
                            help="SÓLO PRUEBAS: registro mínimo del §4.4")
    analizador.add_argument("--contencion", dest="contencion", default=None,
                            choices=("grupo-de-procesos", "arbol-de-procesos"),
                            help="`FD-5`: nivel de AISLAMIENTO exigido a la ejecución local. Sin backend que lo dé, FALLO CERRADO: no se ejecuta nada y no se degrada al débil")
    analizador.add_argument("--contencion-backend", dest="contencion_backend",
                            default=None, help="pedir un backend concreto de contención. Es legítimo y queda registrado; si su nivel es inferior al exigido, FALLO CERRADO")
    analizador.add_argument("--json", action="store_true",
                            help="salida JSON determinista")
    ordenes = analizador.add_subparsers(dest="orden", required=True)

    ordenes.add_parser("procedencia", parents=[comun])
    ordenes.add_parser("elegibles", parents=[comun])
    ordenes.add_parser("vistas", parents=[comun])

    item = ordenes.add_parser("crear-item", parents=[comun])
    item.add_argument("--id", required=True)
    item.add_argument("--titulo", required=True)
    item.add_argument("--motivo", required=True)

    paquete = ordenes.add_parser("crear-paquete", parents=[comun])
    paquete.add_argument("--id", required=True)
    paquete.add_argument("--item", required=True)
    paquete.add_argument("--capacidad", action="append", metavar="CAPACIDAD")
    paquete.add_argument("--adaptador", default="proceso-local")
    paquete.add_argument("--operacion", default="ejecutar")
    paquete.add_argument("--argumento", action="append", metavar="ARG")
    paquete.add_argument("--limite-segundos", type=float, default=30.0,
                         dest="limite_segundos")
    paquete.add_argument("--prioridad", type=int, default=50)
    paquete.add_argument("--max-intentos", type=int,
                         default=runtime.MAX_INTENTOS_POR_DEFECTO, dest="max_intentos")
    paquete.add_argument("--depende-de", action="append", metavar="PAQUETE",
                         dest="depende_de")

    for nombre in ("adquirir", "renovar", "observar", "reclamar", "liberar", "despachar",
                   "estado-paquete"):
        sub = ordenes.add_parser(nombre, parents=[comun])
        sub.add_argument("paquete")

    for nombre in ("pausar", "reanudar", "cancelar"):
        sub = ordenes.add_parser(nombre, parents=[comun])
        sub.add_argument("paquete")
        sub.add_argument("--motivo", required=True)
        sub.add_argument("--autoridad", required=True)

    ciclo = ordenes.add_parser("ciclo", parents=[comun])
    ciclo.add_argument("--maximo", type=int, default=0,
                       help="tope de paquetes atendidos en la pasada; 0 = sin tope")
    return analizador


def main(argv=None):
    analizador = construir_analizador()
    argumentos = analizador.parse_args(argv)
    sin_repo = argumentos.orden in ORDENES_SIN_REPO
    if not getattr(argumentos, "repo", None) and not sin_repo:
        return _uso("falta --repo: esta orden se ejecuta sobre un CONTROL REPO concreto")
    if not getattr(argumentos, "instancia", None) and not sin_repo:
        return _uso("falta --instancia: el runtime nombra al titular de cada lease durable")
    if not hasattr(argumentos, "json"):
        argumentos.json = False
    if not hasattr(argumentos, "paciencia") or argumentos.paciencia is None:
        argumentos.paciencia = runtime.PACIENCIA_POR_DEFECTO
    if not hasattr(argumentos, "registro_en_pruebas"):
        argumentos.registro_en_pruebas = None
    if not hasattr(argumentos, "adaptador_local"):
        argumentos.adaptador_local = None
    for nombre in ("contencion", "contencion_backend"):
        if not hasattr(argumentos, nombre):
            setattr(argumentos, nombre, None)
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
