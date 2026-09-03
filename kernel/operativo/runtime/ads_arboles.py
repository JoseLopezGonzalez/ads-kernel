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

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import arboles                                                       # noqa: E402
from arboles.errores import ErrorDeArboles                           # noqa: E402
from admision.errores import ErrorDeAdmision                         # noqa: E402
from gobierno.errores import ErrorDeGobierno                         # noqa: E402

EXITO, FALLO, USO = 0, 1, 2


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


ORDENES = {
    "conjunto": _orden_conjunto,
    "cruce": _orden_cruce,
    "suite": _orden_suite,
}


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
    if not argumentos.repo:
        return _uso("falta --repo: la sede del conjunto es el árbol documental")
    argumentos.repo = os.path.abspath(argumentos.repo)
    ejecutar = ORDENES.get(argumentos.orden)
    if ejecutar is None:
        return _uso("orden desconocida: " + str(argumentos.orden))
    try:
        return ejecutar(argumentos)
    except (ErrorDeArboles, ErrorDeAdmision, ErrorDeGobierno) as error:
        sys.stderr.write(str(error) + "\n")
        return FALLO


if __name__ == "__main__":
    sys.exit(main())
