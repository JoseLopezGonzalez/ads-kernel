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

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import runtime                                                       # noqa: E402
from estado.errores import ErrorDeEstado                             # noqa: E402
from runtime.errores import ErrorDeRuntime                           # noqa: E402

EXITO, FALLO, USO = 0, 1, 2


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


def _registro(argumentos):
    # EL ADAPTADOR REAL VA PRIMERO. `--adaptador-local` registra el adaptador de PROCESO
    # LOCAL del corte `V7`, que lanza un `subprocess` de verdad y mata de verdad. Es el que
    # usa el escenario extremo a extremo, y el que un despliegue usaría. El registro en
    # pruebas existe sólo para ejercitar el dispatcher sin adaptador, y por eso se declara
    # el segundo y nombrándose a sí mismo.
    if getattr(argumentos, "adaptador_local", None):
        import adaptadores
        return adaptadores.RegistroDeAdaptadores([
            adaptadores.AdaptadorDeProcesoLocal(argumentos.adaptador_local),
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


ORDENES = {
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
    analizador.add_argument("--json", action="store_true",
                            help="salida JSON determinista")
    ordenes = analizador.add_subparsers(dest="orden", required=True)

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
    if not getattr(argumentos, "repo", None):
        return _uso("falta --repo: esta orden se ejecuta sobre un CONTROL REPO concreto")
    if not getattr(argumentos, "instancia", None):
        return _uso("falta --instancia: el runtime nombra al titular de cada lease durable")
    if not hasattr(argumentos, "json"):
        argumentos.json = False
    if not hasattr(argumentos, "paciencia") or argumentos.paciencia is None:
        argumentos.paciencia = runtime.PACIENCIA_POR_DEFECTO
    if not hasattr(argumentos, "registro_en_pruebas"):
        argumentos.registro_en_pruebas = None
    if not hasattr(argumentos, "adaptador_local"):
        argumentos.adaptador_local = None
    ejecutar = ORDENES.get(argumentos.orden)
    if ejecutar is None:
        return _uso("orden desconocida: " + str(argumentos.orden))
    try:
        return ejecutar(argumentos)
    except ErrorDeRuntime as error:
        if argumentos.json:
            sys.stdout.write(_volcar({"error": error.a_dict()}) + "\n")
        sys.stderr.write(str(error) + "\n")
        return FALLO
    except ErrorDeEstado as error:
        if argumentos.json:
            sys.stdout.write(_volcar({"error": error.a_dict()}) + "\n")
        sys.stderr.write(str(error) + "\n")
        return FALLO


if __name__ == "__main__":
    sys.exit(main())
