#!/usr/bin/env python3
"""huella — la huella de integridad del kernel vendorizado, en un solo sitio.

Hallazgo A-04: `kernel-status.sh` calculaba su hash sobre `*.md` y `*.yaml` de `kernel/`.
Los cuatro validadores en Python y los scripts de `tooling/` quedaban FUERA, de modo que
un proyecto podía relajar `ads_lint.py`, neutralizar `comprobar_contratos.py` o quitar una
comprobación de `comprobar_packs.py` y seguir reportando LIMPIO indefinidamente. Es la vía
más barata para rebajar todos los gates a la vez, y era invisible.

La huella se define **aquí y sólo aquí**. `kernel-status.sh` llama a este módulo en vez de
recalcularla por su cuenta: dos implementaciones del mismo hash derivan, y cuando derivan
la que miente es siempre la que nadie mira.

Qué entra en la huella, y por qué:

    kernel/**.md      los contratos, fichas, métodos, prompts y pruebas
    kernel/**.yaml    los esquemas y las reglas: definen qué es conforme
    kernel/**.py      los VALIDADORES: son quienes ejecutan la conformidad
    kernel/**.sh      cualquier script que el kernel lleve dentro
    kernel/**.toml    la plantilla del manifiesto de composición del producto
    tooling/*.sh      el arranque y la propia comprobación de integridad
    tooling/*.py      workspace.py materializa repositorios: editarlo sin que se note
                      sería la vía silenciosa para clonar donde no se debe
    packs/**          la especialización instalada, sin los packs retirados

Qué NO entra:

    kernel/.upstream-hash   es el resultado, no la entrada
    docs/, README, PROFILE  no son kernel: son del proyecto o de su historia
    __pycache__, .git       artefactos de ejecución

Uso:
  python3 kernel/operativo/validadores/huella.py [--raiz DIR] [--listar]
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-04, sobre `validadores/huella.py` —el
#  instrumento que produce el número que se publica como línea base— y con seis líneas de
#  veneno: un `hashlib.py` homónimo cuyo `sha256()` devuelve siempre el digest esperado.
#
#      $ echo "# CODIGO INYECTADO" >> mutado/kernel/operativo/validadores/ads_lint.py
#      $ cd mutado && python3.12 …/huella.py                     → 8b38fb4f4b07300c
#      $ python3.12 …/comprobar_integridad.py                    → T150 FALLIDA  EXIT=1
#      $ PYTHONPATH=veneno python3.12 …/huella.py                → bc59513f7182130a
#      $ PYTHONPATH=veneno python3.12 …/comprobar_integridad.py  → T150 SUPERADA EXIT=0
#
#  `T150` es la prueba que dice «la huella detecta su edición», y bajo veneno certificaba en
#  VERDE un árbol editado. La causa: la zona `validadores/` estaba ENTERA fuera del
#  inventario de `T306`, de modo que `E-10` —declarado «CERRADO POR INVENTARIO MECÁNICO»—
#  seguía vivo justo en el aparato que produce la evidencia de la certificación.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      Alternativas: (a) importar la purga de un módulo común; (b) copiar el prólogo entero
#      —recital incluido— desde `ads_runtime.py`; (c) copiar el MECANISMO byte a byte y
#      escribir el recital de esta sede.
#      Se elige (c). Con (a) la guardia dependería de un `import`, que es exactamente lo que
#      está protegiendo: una guardia que necesita importar ya ha perdido. Con (b) el recital
#      mentiría, porque el hecho reproducido allí no es el de aquí. Con (c) `T330` exige
#      —y comprueba— que el MECANISMO sea IDÉNTICO byte a byte en todos los puntos
#      ejecutables del árbol (digest `aa219465a6dd6a04`, 1 869 bytes), mientras cada sede
#      dice qué se midió en ella. Lo que protege es el mecanismo; lo que se lee, el recital.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación
#      distinta y convertiría un fallo de entorno en un fallo del aparato. Lo que `E-10`
#      nombra es concreto: `PYTHONPATH` y el `cwd`. Se retiran ésos, se cuenta cuántos, y el
#      recuento queda en `RETIRADAS_DE_LA_RUTA`.
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
import hashlib
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

EXTENSIONES = (".md", ".yaml", ".yml", ".py", ".sh", ".toml")
AMBITOS = ("kernel", "packs", "tooling")
EXCLUIDOS_DIR = ("__pycache__", ".git", ".pytest_cache")
EXCLUIDOS_PREFIJO_DIR = ("legacy-",)
EXCLUIDOS_FICHERO = (".upstream-hash",)


def ficheros(raiz=None):
    """Los ficheros de la huella, en orden estable. Lista, no genera sorpresas."""
    base = os.path.abspath(raiz or RAIZ)
    salida = []
    for ambito in AMBITOS:
        origen = os.path.join(base, ambito)
        if not os.path.isdir(origen):
            continue
        for dirpath, dirnames, filenames in os.walk(origen):
            dirnames[:] = sorted(d for d in dirnames
                                 if d not in EXCLUIDOS_DIR
                                 and not d.startswith(EXCLUIDOS_PREFIJO_DIR))
            for nombre in sorted(filenames):
                if nombre in EXCLUIDOS_FICHERO:
                    continue
                if nombre.endswith(EXTENSIONES):
                    salida.append(os.path.join(dirpath, nombre))
    return sorted(salida, key=lambda p: os.path.relpath(p, base))


def calcular(raiz=None):
    """Hash del CONTENIDO y de las RUTAS. Renombrar un fichero cambia la huella."""
    base = os.path.abspath(raiz or RAIZ)
    acumulado = hashlib.sha256()
    for ruta in ficheros(base):
        rel = os.path.relpath(ruta, base).replace(os.sep, "/")
        acumulado.update(rel.encode("utf-8"))
        acumulado.update(b"\0")
        with open(ruta, "rb") as fh:
            acumulado.update(hashlib.sha256(fh.read()).digest())
    return acumulado.hexdigest()[:16]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", default=None)
    ap.add_argument("--listar", action="store_true", help="qué ficheros entran en la huella")
    args = ap.parse_args()
    base = os.path.abspath(args.raiz or RAIZ)
    if args.listar:
        for ruta in ficheros(base):
            print(os.path.relpath(ruta, base))
        print(f"\n{len(ficheros(base))} ficheros")
        return 0
    print(calcular(base))
    return 0


if __name__ == "__main__":
    sys.exit(main())
