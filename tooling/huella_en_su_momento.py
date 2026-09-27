#!/usr/bin/env python3
"""La huella del kernel, juzgada en el momento del ciclo en que el juicio es válido (T519).

    python3 tooling/huella_en_su_momento.py \\
        --codigo N --salida FICHERO --ref RAMA --cambios-desde-el-sello N|desconocido

POR QUÉ EXISTE. La batería mínima de macOS existe para comprobar PORTABILIDAD: que las rutas
son portables (T153, T154), que la reejecución por `execve` sigue intacta en POSIX y que
`tooling/kernel-status.sh` funciona en ese sistema. Ejecutaba además `kernel-status.sh` con
`set -e` y exigía su código 0, es decir, LIMPIO. Pero la huella sólo coincide con
`kernel/.upstream-hash` DESPUÉS del sello, y el sello lo produce el job de release sobre la
rama `claude/*`: todo commit que edita `kernel/` antes de él sale DIVERGENTE por
construcción. Medido en r13, r15, r18 y r19: T153 y T154 pasaban, `kernel-status.sh` decía
DIVERGENTE —verdad— y el `set -e` cortaba el job antes de llegar a la comprobación de
`execve`, que no se ejecutó en ninguno. Un rojo permanente que no decía nada de macOS y
tapaba la única prueba POSIX del job.

QUÉ DECIDE, y por qué no afloja nada:

    sin veredicto de kernel-status          FALLA   no funciona aquí: ESO es de portabilidad
    LIMPIO                                  PASA
    DIVERGENTE en `main`                    FALLA   `main` sólo recibe cortes SELLADOS
    DIVERGENTE sin cambios desde el sello   FALLA   nada de la huella cambió y aun así diverge:
                                                    edición no declarada o sello roto
    DIVERGENTE con cambios desde el sello   PASA    divergencia que ES normal antes del sello;
                                                    la integridad se juzga al sellar (job de
                                                    release) y al vendorizar (`kernel-status`
                                                    LIMPIO que exige `actualizar_kernel`)

Esto es PURO: no invoca Git ni ningún proceso (T188, canal único). Los hechos —el código y la
salida de `kernel-status.sh`, la rama, cuántos ficheros de la huella cambiaron desde el último
commit de sello— los calcula quien lo llama.
"""
from __future__ import annotations

import argparse
import re
import sys

VEREDICTO = re.compile(r"^estado\s*:\s*(LIMPIO|DIVERGENTE|hash de referencia anotado)", re.M)
RAMAS_SELLADAS = ("main",)


def decidir(codigo, salida, ref, cambios_desde_el_sello):
    """`(pasa, veredicto, motivo)`. `cambios_desde_el_sello`: entero, o None si no se sabe."""
    hallado = VEREDICTO.search(salida or "")
    veredicto = hallado.group(1) if hallado else None
    if veredicto is None or codigo not in (0, 1) or (veredicto == "LIMPIO") != (codigo == 0):
        return False, veredicto, ("kernel-status.sh no dio un veredicto coherente (código %s, veredicto %s): "
                                  "no funciona en este sistema, y eso SÍ es un fallo de portabilidad" % (codigo, veredicto))
    if veredicto != "DIVERGENTE":
        return True, veredicto, "la huella coincide con la del sello"
    if ref in RAMAS_SELLADAS:
        return False, veredicto, ("`%s` sólo recibe cortes sellados: una huella DIVERGENTE ahí es una edición "
                                  "sin sellar, no una divergencia previa al sello" % ref)
    if cambios_desde_el_sello == 0:
        return False, veredicto, ("ningún fichero de la huella cambió desde el último sello y aun así diverge: "
                                  "edición no declarada o sello roto")
    return True, veredicto, ("divergencia esperada antes del sello (%s fichero(s) de la huella cambiaron desde "
                             "el último): la integridad se juzga al sellar y al vendorizar, no aquí"
                             % ("?" if cambios_desde_el_sello is None else cambios_desde_el_sello))


def main(argv=None):
    parser = argparse.ArgumentParser(prog="huella_en_su_momento", description=__doc__.splitlines()[0])
    parser.add_argument("--codigo", type=int, required=True)
    parser.add_argument("--salida", required=True, help="fichero con la salida de kernel-status.sh")
    parser.add_argument("--ref", required=True, help="la rama de esta ejecución")
    parser.add_argument("--cambios-desde-el-sello", required=True,
                        help="ficheros de la huella cambiados desde el último commit de sello, o `desconocido`")
    args = parser.parse_args(argv)
    with open(args.salida, encoding="utf-8", errors="replace") as fichero:
        salida = fichero.read()
    cambios = None if args.cambios_desde_el_sello == "desconocido" else int(args.cambios_desde_el_sello)
    pasa, veredicto, motivo = decidir(args.codigo, salida, args.ref, cambios)
    print("T519 %s · huella %s en `%s`: %s" % ("PASA" if pasa else "FALLA", veredicto, args.ref, motivo))
    return 0 if pasa else 1


if __name__ == "__main__":
    sys.exit(main())
