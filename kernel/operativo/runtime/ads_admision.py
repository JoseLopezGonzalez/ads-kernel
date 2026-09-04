#!/usr/bin/env python3
"""ads_admision — punto ejecutable del VERIFICADOR DE ADMISIÓN del control repo.

    python3 kernel/operativo/runtime/ads_admision.py --repo <dir> verificar --base <rev>

Órdenes: `verificar` · `censo-zonas` · `censo-lecturas` · `censo-formulas` · `matriz`.
Códigos de salida:  0 éxito · 1 veredicto ROJO o error tipado · 2 uso incorrecto.

DECISIÓN · `--repo` y `--json` se aceptan ANTES y DESPUÉS de la orden
    Es el patrón que ya usa `ads_estado.py`, y la razón es la de siempre: quien escribe
    `--json` al final no debería recibir un error de uso por una diferencia de estilo que no
    cambia lo que pide.

DECISIÓN · `INDETERMINADO` sale con código 1, igual que `ROJO`
    Alternativas: (a) 0, porque «no ha fallado nada»; (b) 1.
    Se elige (b). Un veredicto que no puede afirmar que el árbol está bien NO es un éxito, y
    darle 0 haría que un `&&` de un guion tratara la ausencia de ancla externa como una
    aprobación. `V6-17` existe justo para que eso no ocurra.

DECISIÓN · el veredicto se emite SÓLO si la sede de fórmulas está
    `admision.verificar` llama a `formulas.exigir_sede()` antes de nada. Si la sede no está,
    esta CLI no imprime un veredicto: imprime el error y sale con 1. Es `V6-19` literal —«si
    la importación de la sede falla, el instrumento NO emite»—.

DECISIÓN · NINGUNA salida imprime rutas absolutas de la máquina
    La evidencia se publica. Los errores tipados relativizan en su constructor y la salida
    legible sólo nombra rutas relativas al repositorio.
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
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import admision                                                      # noqa: E402
from admision import censo as _censo                                 # noqa: E402
from admision import formulas as _formulas                           # noqa: E402
from admision import matriz as _matriz                               # noqa: E402
from admision.errores import ErrorDeAdmision                         # noqa: E402
from gobierno.errores import ErrorDeGobierno                         # noqa: E402
from identidad.errores import ErrorDeIdentidad                       # noqa: E402

from adaptadores.contrato import ErrorDeAdaptador               # noqa: E402
from contencion.errores import ErrorDeContencion                     # noqa: E402
from estado.errores import ErrorDeEstado                             # noqa: E402

EXITO, FALLO, USO = 0, 1, 2


# ---------------------------------------------------------------------------
#  `E-10` · la PROCEDENCIA se PUBLICA. No basta con que sea correcta.
# ---------------------------------------------------------------------------
#  `g.15` pide evidencia «trazable»; una procedencia que sólo existe en la cabeza de quien
#  escribió el `sys.path` no es trazable. Aquí se publica de dónde salió cada módulo del
#  aparato, cuántas entradas del lanzador se retiraron, y si el `--repo` que se está
#  juzgando es o no el árbol del que sale el propio aparato.
MODULOS_DEL_APARATO = ("admision", "gobierno", "identidad")

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
    ((ErrorDeAdmision, ErrorDeGobierno, ErrorDeIdentidad, ErrorDeEstado),
     "error-del-kernel"),
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
    if getattr(argumentos, "json", False):
        sys.stdout.write(_volcar(datos) + "\n")
    else:
        sys.stdout.write("\n".join(legible) + "\n")
    return EXITO


def _uso(mensaje):
    sys.stderr.write("uso: " + mensaje + "\n")
    return USO


def _declaracion(argumentos):
    """La declaración llega de FUERA. Sin `--configuracion` sólo se puede anclar a mano."""
    if getattr(argumentos, "configuracion", None):
        import identidad
        configuracion = identidad.cargar(argumentos.configuracion,
                                         arbol_verificado=argumentos.repo)
        return configuracion.declaracion()
    return admision.Declaracion(
        ancla=getattr(argumentos, "ancla", None) or None,
        autoridad="linea-de-ordenes",
        admitidas=[{"ruta": ruta, "motivo": "admitida en la línea de órdenes"}
                   for ruta in (getattr(argumentos, "admitir", None) or [])],
    )


def orden_verificar(argumentos):
    declaracion = _declaracion(argumentos)
    veredicto = admision.verificar(argumentos.repo, base=argumentos.base,
                                   declaracion=declaracion)
    datos = veredicto.a_dict()
    # `E-10` · la PROCEDENCIA viaja CON el veredicto. Un veredicto que no dice de dónde
    # salió el código que lo emitió no se puede auditar: quien lo lea tendría que creerse
    # que el `sys.path` era el que debía ser.
    datos["procedencia"] = procedencia(argumentos.repo)
    legible = [
        "veredicto     " + veredicto.color,
        "base          " + datos["base"][:12],
        "mutaciones    " + str(len(datos["mutaciones"])),
        "zonas         " + str(len(datos["censo_de_zonas"]["zonas"]))
        + "  sin condición: " + str(len(datos["censo_de_zonas"]["sin_condicion"]))
        + "  sin zona: " + str(len(datos["censo_de_zonas"]["sin_zona"])),
        "hallazgos     " + str(len(datos["hallazgos"])),
    ]
    for hallazgo in datos["hallazgos"]:
        legible.append("  " + hallazgo["punto"] + "  " + hallazgo["codigo"] + "  "
                       + hallazgo["ruta"])
        legible.append("      " + hallazgo["causa"])
    fuera = datos.get("fuera_de_alcance") or {}
    legible.append("fuera de alcance declarado: "
                   + (", ".join(sorted(fuera)) if fuera else "(ninguno)"))
    legible.append("procedencia   aparato: " + datos["procedencia"]["aparato"]
                   + " · repo: " + str(datos["procedencia"].get("repo"))
                   + " · mismo árbol: "
                   + ("si" if datos["procedencia"].get("repo_es_el_arbol_del_aparato")
                      else "NO")
                   + " · entradas del lanzador retiradas: "
                   + str(datos["procedencia"]["entradas_del_lanzador_retiradas"]))
    for modulo in sorted(datos["procedencia"]["modulos"]):
        legible.append("  modulo  " + modulo + "  "
                       + datos["procedencia"]["modulos"][modulo])
    for punto, donde in sorted((datos.get("procedencia_de_los_puntos") or {}).items()):
        legible.append("  " + punto + "  " + donde)
    _emitir(argumentos, datos, legible)
    return EXITO if veredicto.color == "VERDE" else FALLO


def orden_censo_zonas(argumentos):
    zonas = _censo.cargar_zonas(argumentos.repo)
    metro = admision.Perimetro(zonas,
                               prefijos_de_instrumento=admision.prefijos_de_instrumento())
    canal = admision.CanalDeLecturaGit(argumentos.repo)
    rutas = set(canal.rutas_del_arbol("HEAD")) | set(canal.rutas_sin_rastrear())
    informe = metro.censo(rutas)
    legible = ["zonas derivadas: " + str(len(informe["zonas"]))]
    for fila in informe["zonas"]:
        legible.append("  " + ("OK " if fila["declarada"] else "SIN") + "  "
                       + str(fila["condicion"]) + "  " + fila["patron"]
                       + "  (" + str(fila["rutas"]) + " rutas)")
    legible.append("rutas sin zona: " + str(len(informe["sin_zona"])))
    for ruta in informe["sin_zona"]:
        legible.append("  " + ruta)
    _emitir(argumentos, informe, legible)
    return EXITO if informe["ok"] else FALLO


def orden_censo_lecturas(argumentos):
    modulos = _censo.modulos_del_aparato(os.path.dirname(os.path.abspath(__file__)))
    informe = _censo.censar_lecturas(modulos)
    legible = ["sedes de proceso declaradas:"]
    for nombre in sorted(informe["sedes_declaradas"]):
        legible.append("  " + nombre + "  " + informe["sedes_declaradas"][nombre])
    legible.append("invocaciones de proceso: " + str(len(informe["procesos"])))
    for entrada in informe["procesos"]:
        legible.append("  " + ("OK " if entrada["sede_declarada"] else "XX ")
                       + entrada["modulo"] + ":" + str(entrada["linea"]) + "  "
                       + entrada["llamada"])
    legible.append("lecturas de lista: " + str(len(informe["lecturas"])))
    for entrada in informe["lecturas"]:
        legible.append("  " + ("OK " if entrada["separador_seguro"] else "XX ")
                       + entrada["modulo"] + ":" + str(entrada["linea"]) + "  "
                       + entrada["orden"] + ("  -z" if entrada["separador_seguro"] else
                                             "  SIN -z"))
    legible.append("ok: " + ("si" if informe["ok"] else "no"))
    _emitir(argumentos, informe, legible)
    return EXITO if informe["ok"] else FALLO


def orden_censo_formulas(argumentos):
    # `ADJ-M1` · HECHO REPRODUCIDO ANTES DE CORREGIR. Esta orden censaba
    # `modulos_del_aparato` —TODO el runtime, que es el sujeto de `V6-04`— mientras el
    # VEREDICTO de `admision.verificar` y la prueba `T190` censaban
    # `modulos_del_verificador`, que es el sujeto que `V6-19` declara. Medido sobre el
    # propio candidato: `ads_admision.py --repo . censo-formulas` daba `segundas
    # definiciones: 7 · ok: no · EXIT=1` con la batería en verde, porque la orden y la
    # prueba medían CONJUNTOS DISTINTOS. Las siete «segundas definiciones» eran los
    # `hashlib.sha256` del MOTOR de estado durable y de `corpus.py`, que `V6-19` no reclama.
    #
    # DECISIÓN · manda el sujeto declarado de `V6-19`, y por tanto se alinea la ORDEN
    #     Alternativas: (a) ensanchar el veredicto y la prueba al runtime entero; (b)
    #     estrechar la orden al aparato de verificación; (c) dejar los dos y declarar la
    #     diferencia.
    #     Se elige (b). Con (a) el MOTOR tendría que importar su direccionamiento por
    #     contenido DESDE el verificador —la flecha de dependencia al revés, y el motor sin
    #     poder existir sin el verificador—; la razón entera está escrita en
    #     `censo.PAQUETES_DEL_VERIFICADOR`. Con (c) quedarían dos cifras para una misma
    #     pregunta, que es exactamente lo que `V6-19` prohíbe de las fórmulas y no hay razón
    #     para tolerarlo de su censo. Con (b) la orden publica lo mismo que el veredicto:
    #     una CLI de diagnóstico que contradice al instrumento que diagnostica no sirve.
    modulos = _censo.modulos_del_verificador(os.path.dirname(os.path.abspath(__file__)))
    informe = _formulas.censar_formulas(modulos)
    legible = ["fórmulas censadas:"]
    for entrada in informe["formulas"]:
        legible.append("  " + entrada["formula"] + "  sede " + entrada["sede"] + "  ("
                       + entrada["funcion"] + ")")
    legible.append("definiciones halladas: " + str(len(informe["definiciones"])))
    for entrada in informe["definiciones"]:
        legible.append("  " + ("OK " if entrada["en_la_sede"] else "XX ")
                       + entrada["formula"] + "  " + entrada["modulo"] + ":"
                       + str(entrada["linea"]))
    legible.append("segundas definiciones: " + str(len(informe["segundas_definiciones"])))
    legible.append("ok: " + ("si" if informe["ok"] else "no"))
    _emitir(argumentos, informe, legible)
    return EXITO if informe["ok"] else FALLO


def orden_matriz(argumentos):
    directorio = tempfile.mkdtemp(prefix="ads-matriz-")
    try:
        informe = _matriz.ejecutar(directorio)
    finally:
        import shutil
        shutil.rmtree(directorio, ignore_errors=True)
    legible = ["controles: " + str(informe["total"])]
    for fila in informe["controles"]:
        legible.append("  " + ("OK " if fila["acierta"] else "XX ") + fila["familia"]
                       + "  " + fila["caso"].ljust(18) + fila["signo"].ljust(9)
                       + "esperado " + fila["esperado"].ljust(6)
                       + "obtenido " + fila["obtenido"])
    legible.append("falsos_verdes  " + str(informe["falsos_verdes"]))
    legible.append("falsos_rojos   " + str(informe["falsos_rojos"]))
    legible.append("formas         " + ", ".join(informe["formas_cubiertas"]))
    legible.append("letras         " + ", ".join(informe["letras_cubiertas"]))
    _emitir(argumentos, informe, legible)
    return EXITO if informe["ok"] else FALLO


def orden_procedencia(argumentos):
    """`E-10` · publica de dónde sale cada módulo, sin emitir ningún veredicto."""
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
    "verificar": orden_verificar,
    "procedencia": orden_procedencia,
    "censo-zonas": orden_censo_zonas,
    "censo-lecturas": orden_censo_lecturas,
    "censo-formulas": orden_censo_formulas,
    "matriz": orden_matriz,
}


def construir_analizador():
    # `SUPPRESS` y no `None`: con un valor por defecto corriente, el subanalizador vuelve a
    # poner `None` encima del `--repo` que se escribió ANTES de la orden, y la promesa de
    # aceptarlo en las dos posiciones sería falsa justo para quien la usa desde un guion. Es
    # el mismo remedio que `ads_estado.py` ya aplica, y por la misma razón.
    comun = argparse.ArgumentParser(add_help=False)
    comun.add_argument("--repo", default=argparse.SUPPRESS,
                       help="ruta del CONTROL REPO que se verifica")
    comun.add_argument("--json", action="store_true", default=argparse.SUPPRESS,
                       help="salida determinista en JSON")

    analizador = argparse.ArgumentParser(
        prog="ads_admision", parents=[comun],
        description="verificador de admisión del control repo (cortes V2–V5 de F6)",
    )
    ordenes = analizador.add_subparsers(dest="orden", required=True)

    verificar = ordenes.add_parser("verificar", parents=[comun])
    verificar.add_argument("--base", required=True)
    verificar.add_argument("--ancla", default=None,
                           help="revisión que el ancla EXTERNA certifica (`V6-17`)")
    verificar.add_argument("--admitir", action="append", default=[])
    verificar.add_argument("--configuracion", default=None,
                           help="configuración externa de confianza, FUERA del árbol")

    ordenes.add_parser("censo-zonas", parents=[comun])
    ordenes.add_parser("censo-lecturas", parents=[comun])
    ordenes.add_parser("censo-formulas", parents=[comun])
    ordenes.add_parser("matriz", parents=[comun])
    ordenes.add_parser("procedencia", parents=[comun])
    return analizador


def main(argv=None):
    analizador = construir_analizador()
    argumentos = analizador.parse_args(argv)
    if not hasattr(argumentos, "repo"):
        argumentos.repo = None
    if not hasattr(argumentos, "json"):
        argumentos.json = False
    if argumentos.orden in ("verificar", "censo-zonas") and not argumentos.repo:
        return _uso("falta --repo: esta orden se ejecuta sobre un CONTROL REPO concreto")
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
