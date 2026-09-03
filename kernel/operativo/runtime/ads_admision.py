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

EXITO, FALLO, USO = 0, 1, 2


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
    modulos = _censo.modulos_del_aparato(os.path.dirname(os.path.abspath(__file__)))
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


ORDENES = {
    "verificar": orden_verificar,
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
    try:
        return ejecutar(argumentos)
    except (ErrorDeAdmision, ErrorDeGobierno, ErrorDeIdentidad) as error:
        if argumentos.json:
            sys.stdout.write(_volcar({"error": error.a_dict()}) + "\n")
        sys.stderr.write(str(error) + "\n")
        return FALLO


if __name__ == "__main__":
    sys.exit(main())
