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

EXITO, FALLO, USO = 0, 1, 2

ORDENES = ("encuadrar", "componer", "materializar", "planificar", "ciclo", "continuar",
           "macrocircuito")


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


def _registro(argumentos):
    if getattr(argumentos, "adaptador_local", None):
        import adaptadores
        return adaptadores.RegistroDeAdaptadores([
            adaptadores.AdaptadorDeProcesoLocal(argumentos.adaptador_local),
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
    equipo = ciclo.materializar(
        argumentos.capacidad, corpus=_corpus(argumentos),
        composiciones_verdaderas=list(argumentos.composicion or []),
        condiciones_de_rol=list(argumentos.condicion or []),
        slots=argumentos.slots,
    )
    lineas = [
        "equipo        " + equipo["id"],
        "capacidad     " + equipo["capacidad"],
        "composicion   " + equipo["composicion"],
        "roles         " + (", ".join(r["rol"] for r in equipo["roles"]) or "(ninguno)"),
        "esperando     " + (", ".join(r["rol"] for r in equipo["esperando_capacidad"])
                            or "(ninguno)"),
    ]
    return _emitir(argumentos, equipo, lineas)


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


DESPACHADOR = {
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

    seis = subordenes.add_parser("continuar", parents=[comun])
    seis.add_argument("--ejecutar", action="store_true")
    seis.add_argument("--reparar", action="store_true")
    seis.add_argument("--interactivo", action="store_true")
    seis.add_argument("--frente", type=int, default=1)
    seis.add_argument("--adaptador-local", dest="adaptador_local")

    siete = subordenes.add_parser("macrocircuito", parents=[comun])
    siete.add_argument("--id")
    siete.add_argument("--censo", action="store_true")
    siete.add_argument("--disparador")
    siete.add_argument("--comprobacion", action="append")
    siete.add_argument("--evidencia", action="append")
    siete.add_argument("--abrir", action="store_true")
    siete.add_argument("--adaptador-local", dest="adaptador_local")
    return analizador


def main(argv=None):
    analizador = construir_analizador()
    argumentos = analizador.parse_args(argv if argv is not None else sys.argv[1:])
    if not argumentos.subcomando:
        analizador.print_help(sys.stderr)
        return USO
    if argumentos.subcomando != "macrocircuito" or not argumentos.censo:
        if not argumentos.repo:
            print("falta `--repo <dir>`: sin control repo no hay nada que encuadrar",
                  file=sys.stderr)
            return USO
    try:
        return DESPACHADOR[argumentos.subcomando](argumentos)
    except ErrorDeCiclo as error:
        return _fallo(argumentos, error)
    except ErrorDeMacrocircuito as error:
        return _fallo(argumentos, error)
    except ErrorDeRuntime as error:
        return _fallo(argumentos, error)
    except ErrorDeEstado as error:
        return _fallo(argumentos, error)
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
