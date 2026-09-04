#!/usr/bin/env python3
"""ads_estado — punto ejecutable del motor de ESTADO DURABLE del CONTROL REPO.

    python3 kernel/operativo/runtime/ads_estado.py --repo <dir> <orden> [...]

Órdenes: `inicializar` · `revision` · `leer` · `listar` · `transicion` · `recuperar` ·
`verificar` · `auditar` · `reconciliacion` · `abrir-reconciliacion` · `resolver` ·
`migrar` · `atestar`.

Códigos de salida:  0 éxito · 1 fallo de la operación (error tipado) · 2 uso incorrecto.

DECISIÓN · NINGUNA salida imprime rutas absolutas de la máquina, tampoco las de error
    La evidencia de `F6` se publica, y una ruta como `/home/quien-sea/...` la vuelve
    dependiente de la máquina y del usuario: dos ejecuciones del escenario darían bytes
    distintos, contra el §12.1, y de paso se filtraría información del entorno. Todo lo que
    sale es relativo al almacén. `--json` sigue la misma regla por la misma razón.

    Durante un tiempo esto fue FALSO en los caminos de error, y merece decirse porque
    explica dónde vive ahora la garantía. Cada módulo componía sus errores por su cuenta:
    `motor` relativizaba y `bloqueo`, `diario`, `reconciliacion` y `atestacion` no, en unos
    veinte sitios. La promesa fallaba justo en las salidas que se publican. La garantía ya
    no depende de que cada `raise` se acuerde: `ErrorDeEstado` sanea la ruta en su propio
    constructor (`estado/errores.py`, `relativizar`), así que cubre los cuatro módulos, los
    caminos de error de la CLI y el módulo que alguien escriba mañana.

DECISIÓN · sólo las órdenes que MUTAN abren con `recuperar=True`
    Alternativas: (a) recuperar siempre al abrir; (b) recuperar sólo donde se va a escribir.
    Se elige (b). Recuperar exige el bloqueo de escritor y ESCRIBE en el diario. Con (a),
    una orden de lectura como `revision` mutaría el almacén y, peor, fallaría si otro
    proceso está escribiendo: consultar el estado dejaría de ser una operación segura. Las
    órdenes de lectura abren con `recuperar=False` y siguen viendo la ventana abierta, que
    es información útil y no un problema que haya que resolver a sus espaldas.

DECISIÓN · `--base -` significa «la vigente, sin comprobación CAS»
    El §9 reserva `base=None` a la inicialización. La CLI lo expone igualmente con `-`,
    porque sin él no habría forma de escribir desde línea de órdenes sin leer antes la
    revisión. Se documenta lo que cuesta: con `-` se RENUNCIA a la garantía de comparación e
    intercambio, y dos escritores que usen `-` se serializan pero ninguno detecta que el
    otro publicó. Para exigir la garantía se pasa el `revision_id` exacto.
"""
from __future__ import annotations

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

import estado                                                        # noqa: E402
from estado import atestacion as _atestacion                         # noqa: E402
from estado.errores import ErrorDeEstado                             # noqa: E402

from adaptadores.contrato import ErrorDeAdaptador               # noqa: E402
from contencion.errores import ErrorDeContencion                     # noqa: E402
from gobierno.errores import ErrorDeGobierno                         # noqa: E402

EXITO, FALLO, USO = 0, 1, 2


# ---------------------------------------------------------------------------
#  `E-10` · la PROCEDENCIA se PUBLICA. No basta con que sea correcta.
# ---------------------------------------------------------------------------
#  `g.15` pide evidencia «trazable»; una procedencia que sólo existe en la cabeza de quien
#  escribió el `sys.path` no es trazable. Aquí se publica de dónde salió cada módulo del
#  aparato, cuántas entradas del lanzador se retiraron, y si el `--repo` que se está
#  juzgando es o no el árbol del que sale el propio aparato.
MODULOS_DEL_APARATO = ("estado",)

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
    ((ErrorDeEstado, ErrorDeGobierno), "error-del-kernel"),
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


def _abrir(argumentos, *, para_escribir):
    return estado.abrir(argumentos.repo, recuperar=para_escribir)


# --------------------------------------------------------------------- órdenes
def orden_inicializar(argumentos):
    with estado.inicializar(argumentos.repo) as almacen:
        revision = almacen.revision()
    return _emitir(argumentos, revision, [
        "almacen inicializado en estado/",
        "revision      " + str(revision["revision"]),
        "revision_id   " + revision["revision_id"],
        "cid_raiz      " + revision["cid_raiz"],
    ])


def orden_revision(argumentos):
    with _abrir(argumentos, para_escribir=False) as almacen:
        revision = almacen.revision()
        ventana = almacen.estado_de_la_ventana()
    lineas = [
        "revision           " + str(revision["revision"]),
        "revision_id        " + revision["revision_id"],
        "padre              " + str(revision["padre"]),
        "cid_raiz           " + revision["cid_raiz"],
        "transaccion        " + revision["transaccion"],
        "diario_secuencia   " + str(revision["diario_secuencia"]),
        "ventana            " + ventana,
        "objetos            " + str(len(revision["raiz"])),
    ]
    # `--json` imprime `REVISION.json` y NADA MÁS, como manda el §11. Añadir aquí un campo
    # calculado —`ventana` lo era— rompe la comparación byte a byte contra el fichero
    # publicado, y entonces quien quiera comprobar una afirmación sobre el estado tendría
    # que comprobarla contra la salida de esta orden en vez de contra el estado, que es
    # exactamente lo que `g.13` prohíbe. La ventana sí se cuenta en la salida legible,
    # donde no hay nada que comparar.
    return _emitir(argumentos, revision, lineas)


def orden_leer(argumentos):
    with _abrir(argumentos, para_escribir=False) as almacen:
        objeto = almacen.leer(argumentos.ruta)
    return _emitir(argumentos, {"ruta": argumentos.ruta, "contenido": objeto},
                   [_volcar(objeto)])


def orden_listar(argumentos):
    with _abrir(argumentos, para_escribir=False) as almacen:
        rutas = almacen.listar(argumentos.dominio or "")
    return _emitir(argumentos, {"dominio": argumentos.dominio or "", "rutas": rutas}, rutas)


def orden_transicion(argumentos):
    operaciones = []
    for pareja in argumentos.escribir or []:
        if "=" not in pareja:
            raise SystemExit(_uso("--escribir se escribe `<ruta>=<fichero.json>`"))
        ruta, fichero = pareja.split("=", 1)
        try:
            with open(fichero, "rb") as origen:
                contenido = json.loads(origen.read().decode("utf-8"))
        except (OSError, ValueError, UnicodeDecodeError) as exc:
            # El contenido lo aporta el llamador: un JSON roto en la ENTRADA es un error de
            # uso, no una corrupción del almacén, y confundirlos haría creer que el estado
            # está dañado cuando lo que está mal es el argumento.
            raise SystemExit(_uso("no se pudo leer " + os.path.basename(fichero)
                                  + ": " + str(exc)))
        operaciones.append(estado.Escritura(ruta, contenido))
    for ruta in argumentos.borrar or []:
        operaciones.append(estado.Borrado(ruta))

    base = None if argumentos.base in (None, "-") else argumentos.base
    transicion = estado.Transicion(
        tipo=argumentos.tipo, base=base, operaciones=operaciones,
        autor=argumentos.autor, motivo=argumentos.motivo, id=argumentos.id,
    )
    with _abrir(argumentos, para_escribir=True) as almacen:
        resultado = almacen.aplicar(transicion, intentos=argumentos.intentos)
    datos = resultado.a_dict()
    return _emitir(argumentos, datos, [
        "transaccion   " + datos["transaccion"],
        "revision      " + str(datos["revision"]),
        "revision_id   " + datos["revision_id"],
        "cid_raiz      " + datos["cid_raiz"],
        "repetida      " + ("si" if datos["repetida"] else "no"),
        "operaciones   " + str(len(datos["operaciones"])),
    ])


def orden_recuperar(argumentos):
    # `recuperar=False` al abrir: la recuperación la hace la orden, explícitamente, y no el
    # acto de abrir. Así el informe describe UNA pasada y no dos encadenadas.
    with estado.abrir(argumentos.repo, recuperar=False) as almacen:
        informe = almacen.recuperar().a_dict()
    return _emitir(argumentos, informe, [
        "rama              " + informe["rama"],
        "ventana_previa    " + informe["ventana_previa"],
        "transaccion       " + str(informe["transaccion"]),
        "revision_id       " + str(informe["revision_id"]),
        "eventos           " + ", ".join(informe["eventos_anexados"] or ["(ninguno)"]),
        "marcadas          " + ", ".join(informe["marcadas"] or ["(ninguna)"]),
    ])


def orden_verificar(argumentos):
    with _abrir(argumentos, para_escribir=False) as almacen:
        informe = almacen.verificar_integridad().a_dict()
    return _emitir(argumentos, informe, [
        "ok                          " + ("si" if informe["ok"] else "no"),
        "revision                    " + str(informe["revision"]),
        "cid_raiz                    " + informe["cid_raiz"],
        "objetos_verificados         " + str(informe["objetos_verificados"]),
        "eventos_del_diario          " + str(informe["eventos_del_diario"]),
        "lineas_del_registro         " + str(informe["lineas_del_registro"]),
        "reconciliaciones_pendientes " + str(informe["reconciliaciones_pendientes"]),
        "ventana                     " + informe["ventana"],
    ])


def orden_auditar(argumentos):
    with _abrir(argumentos, para_escribir=False) as almacen:
        informe = almacen.auditar().a_dict()
    return _emitir(argumentos, informe, [
        "ok                        " + ("si" if informe["ok"] else "no"),
        "revision                  " + str(informe["revision"]),
        "cid_raiz                  " + informe["cid_raiz"],
        "cid_raiz_reproducido      " + informe["cid_raiz_reproducido"],
        "transacciones_confirmadas " + str(informe["transacciones_confirmadas"]),
        "eventos                   " + str(informe["eventos"]),
        "resoluciones_casadas      " + str(informe["resoluciones_casadas"]),
    ])


def orden_reconciliacion(argumentos):
    with _abrir(argumentos, para_escribir=False) as almacen:
        pendientes = almacen.reconciliacion_pendiente()
        todas = almacen._registro.lineas()
    lineas = pendientes if argumentos.pendientes else todas
    salida = {
        "pendientes": [linea["registro"] for linea in pendientes],
        "lineas": lineas if not argumentos.pendientes else pendientes,
    }
    legible = [
        linea["tipo"] + "  " + linea["registro"] + "  item=" + str(linea.get("item", "-"))
        + "  intento=" + str(linea.get("intento", "-"))
        + "  momento=" + str(linea["momento"]["diario_secuencia"])
        + "/" + str(linea["momento"]["revision"])
        for linea in lineas
    ] or ["(sin registros)"]
    return _emitir(argumentos, salida, legible)


def orden_abrir_reconciliacion(argumentos):
    """La vía EXPLÍCITA de apertura del registro auxiliar (`g.9`).

    Existen dos vías, y hasta ahora sólo una era alcanzable desde fuera: la automática, que
    abre el registro al agotar los reintentos. Que la explícita viviera sólo en la API
    dejaba un camino del motor sin puerta, y un camino sin puerta es un camino que nadie
    ejercita. A diferencia de la automática, ésta SÍ toma el bloqueo de escritor y SÍ anota
    `reconciliacion.abierta` en el diario, porque aquí no hay ninguna contención que lo
    impida: la asimetría no es un descuido, es lo que `g.6` obliga.
    """
    with _abrir(argumentos, para_escribir=True) as almacen:
        registro = almacen.abrir_reconciliacion(
            producto=argumentos.producto, repositorio=argumentos.repositorio,
            item=argumentos.item, intento=argumentos.intento, causa=argumentos.causa,
        )
        pendientes = [linea["registro"] for linea in almacen.reconciliacion_pendiente()]
    salida = {"registro": registro, "producto": argumentos.producto,
              "repositorio": argumentos.repositorio, "item": argumentos.item,
              "intento": argumentos.intento, "causa": argumentos.causa,
              "pendientes": pendientes}
    return _emitir(argumentos, salida, [
        "registro      " + registro,
        "item          " + argumentos.item,
        "intento       " + str(argumentos.intento),
        "pendientes    " + ", ".join(pendientes or ["(ninguna)"]),
    ])


def orden_resolver(argumentos):
    with _abrir(argumentos, para_escribir=True) as almacen:
        resultado = almacen.resolver_reconciliacion(
            argumentos.registro, autoridad=argumentos.autoridad, motivo=argumentos.motivo
        )
    datos = resultado.a_dict()
    datos["registro"] = argumentos.registro
    return _emitir(argumentos, datos, [
        "registro      " + argumentos.registro,
        "transaccion   " + datos["transaccion"],
        "revision      " + str(datos["revision"]),
        "revision_id   " + datos["revision_id"],
    ])


def orden_migrar(argumentos):
    with estado.abrir(argumentos.repo, recuperar=False) as almacen:
        informe = almacen.migrar(argumentos.a).a_dict()
    return _emitir(argumentos, informe, [
        "desde         " + str(informe["desde"]),
        "hasta         " + str(informe["hasta"]),
        "aplicadas     " + str(len(informe["aplicadas"])),
        "transacciones " + ", ".join(informe["transacciones"] or ["(ninguna)"]),
    ])


def orden_atestar(argumentos):
    # Se declara en la salida, como pide el §11: el proveedor es EFÍMERO y de pruebas.
    proveedor = _atestacion.ProveedorEfimero()
    with _abrir(argumentos, para_escribir=False) as almacen:
        evidencia = _atestacion.atestar(almacen, proveedor, argumentos.destino)
        informe = _atestacion.verificar_atestacion(
            argumentos.destino, proveedor, almacen=almacen
        )
    salida = {
        "proveedor": "ProveedorEfimero/" + proveedor.ALGORITMO,
        "advertencia": "EXCLUSIVAMENTE PARA PRUEBAS: la clave es efímera y no es una "
                       "solución de custodia productiva",
        "identidad": evidencia["identidad"],
        "revision": evidencia["revision"],
        "revision_id": evidencia["revision_id"],
        "cid_raiz": evidencia["cid_raiz"],
        "destino": os.path.basename(argumentos.destino),
        "verificada_en_proceso": informe["valida"],
        "casa_con_el_arbol": informe["casa_con_el_arbol"],
    }
    return _emitir(argumentos, salida, [
        "proveedor             ProveedorEfimero/" + proveedor.ALGORITMO,
        "advertencia           EXCLUSIVAMENTE PARA PRUEBAS, sin custodia productiva",
        "revision              " + str(evidencia["revision"]),
        "revision_id           " + evidencia["revision_id"],
        "cid_raiz              " + evidencia["cid_raiz"],
        "destino               " + os.path.basename(argumentos.destino),
        "verificada_en_proceso " + ("si" if informe["valida"] else "no"),
    ])


ORDENES = {
    "inicializar": orden_inicializar,
    "revision": orden_revision,
    "leer": orden_leer,
    "listar": orden_listar,
    "transicion": orden_transicion,
    "recuperar": orden_recuperar,
    "verificar": orden_verificar,
    "auditar": orden_auditar,
    "reconciliacion": orden_reconciliacion,
    "abrir-reconciliacion": orden_abrir_reconciliacion,
    "resolver": orden_resolver,
    "migrar": orden_migrar,
    "atestar": orden_atestar,
}


def _uso(mensaje):
    sys.stderr.write("uso: " + mensaje + "\n")
    return USO


def construir_analizador():
    # `--repo` y `--json` se aceptan ANTES y DESPUÉS de la orden. No es comodidad: una CLI
    # que sólo admite una de las dos posiciones convierte un tecleo en un error de uso, y
    # quien la invoca desde un script acaba descubriéndolo en producción. `SUPPRESS` hace
    # que el subanalizador no pise el valor puesto arriba cuando la opción no se repite.
    comun = argparse.ArgumentParser(add_help=False)
    comun.add_argument("--repo", default=argparse.SUPPRESS, help="ruta del CONTROL REPO")
    comun.add_argument("--json", action="store_true", default=argparse.SUPPRESS,
                       help="salida JSON determinista")

    analizador = argparse.ArgumentParser(
        prog="ads_estado", description="motor de estado durable del control repo de ADS",
    )
    analizador.add_argument("--repo", default=None, help="ruta del CONTROL REPO")
    analizador.add_argument("--json", action="store_true", help="salida JSON determinista")
    ordenes = analizador.add_subparsers(dest="orden", required=True)

    ordenes.add_parser("inicializar", parents=[comun])
    ordenes.add_parser("revision", parents=[comun])
    ordenes.add_parser("recuperar", parents=[comun])
    ordenes.add_parser("verificar", parents=[comun])
    ordenes.add_parser("auditar", parents=[comun])

    leer = ordenes.add_parser("leer", parents=[comun])
    leer.add_argument("ruta")

    listar = ordenes.add_parser("listar", parents=[comun])
    listar.add_argument("dominio", nargs="?", default="")

    transicion = ordenes.add_parser("transicion", parents=[comun])
    transicion.add_argument("--id", required=True)
    transicion.add_argument("--autor", required=True)
    transicion.add_argument("--motivo", required=True)
    transicion.add_argument("--base", default="-", help="`revision_id` esperado, o `-`")
    transicion.add_argument("--tipo", default="transicion")
    transicion.add_argument("--escribir", action="append", metavar="RUTA=FICHERO.json")
    transicion.add_argument("--borrar", action="append", metavar="RUTA")
    transicion.add_argument("--intentos", type=int, default=3)

    reconciliacion = ordenes.add_parser("reconciliacion", parents=[comun])
    reconciliacion.add_argument("--pendientes", action="store_true")

    abrir_rec = ordenes.add_parser("abrir-reconciliacion", parents=[comun])
    abrir_rec.add_argument("--producto", required=True)
    abrir_rec.add_argument("--repositorio", required=True)
    abrir_rec.add_argument("--item", required=True)
    abrir_rec.add_argument("--intento", type=int, required=True)
    abrir_rec.add_argument("--causa", required=True)

    resolver = ordenes.add_parser("resolver", parents=[comun])
    resolver.add_argument("registro")
    resolver.add_argument("--autoridad", required=True)
    resolver.add_argument("--motivo", required=True)

    migrar = ordenes.add_parser("migrar", parents=[comun])
    migrar.add_argument("--a", type=int, default=estado.VERSION_DE_FORMATO)

    atestar = ordenes.add_parser("atestar", parents=[comun])
    atestar.add_argument("--destino", required=True,
                         help="fichero FUERA del control repo verificado")
    return analizador


def main(argv=None):
    analizador = construir_analizador()
    argumentos = analizador.parse_args(argv)
    if not getattr(argumentos, "repo", None):
        return _uso("falta --repo: esta orden se ejecuta sobre un CONTROL REPO concreto")
    if not hasattr(argumentos, "json"):
        argumentos.json = False
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
