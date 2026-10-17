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

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, `HALLAZGO 3` del revisor 3 en el gate del
#  2026-09-05: veintiuna baterías de `runtime/pruebas/` y `tooling/tests/` no llevaban el
#  prólogo `E-10`, y el inventario de `T330` las eximía POR SU ZONA con `motivo: "bateria"`
#  —que es la lista escrita a mano que `ADJ-B2` prohibió, sólo que escrita por directorios—.
#  Y el canal que PRODUCE la evidencia, `registrar_evidencia.py` L212, lanzaba a sus hijos
#  con `subprocess.run` SIN `env=`: el veneno del padre llegaba entero a cada batería.
#
#  Lo que esto significa aquí: la salida de esta batería se PUBLICA como evidencia y
#  sostiene el estado de escenarios. Un `hashlib` o un `json` sustituidos por quien la corre
#  deciden qué dice esa evidencia. Se aplica el remedio ENTERO que el revisor adjudicó: el
#  prólogo entra en la batería —lo que cierra también la ejecución suelta— y el runner
#  sanea el entorno de sus hijos y lo publica en la cabecera de cada evidencia.
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
#  HECHO REPRODUCIDO ANTES DE CORREGIR, `HALLAZGO 3` del gate del 2026-09-05: esta batería
#  no llevaba el prólogo, y el inventario de `T330` la eximía por vivir en una zona de
#  pruebas. Su salida se PUBLICA como evidencia; un `json.py` o un `hashlib.py` homónimos en
#  el `PYTHONPATH` de quien la corre deciden qué dice esa evidencia, que es exactamente el
#  daño que `H-01` midió sobre `huella.py`. La deuda ya no es de zona: la exclusión
#  `motivo: "bateria"` se ha RETIRADO del inventario y esta batería es un punto ejecutable
#  como cualquier otro.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      Es la decisión de `ADJ-B2`, sin cambio: `T330` exige que el mecanismo sea IDÉNTICO en
#      todos los puntos ejecutables, y cada sede escribe qué se midió en ella.
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
