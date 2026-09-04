#!/usr/bin/env python3
"""entorno — la guarda de versión del intérprete, comprobada ANTES de correr.

CIERRA `A14`, la limitación que el corpus registra así: «la versión mínima del intérprete
está declarada SÓLO en una cadena de documentación del tooling, y no se comprueba antes de
correr». Su consecuencia real ya ocurrió y está escrita en dos sitios del repositorio: bajo
un intérprete sin `tomllib`, el validador de fuentes falla, el runner —correctamente— NO
republica su evidencia, y la cobertura publicada queda describiendo un corpus anterior
mientras el comprobador de evidencia sigue en verde. Un defecto de ENTORNO subía a la capa
de certificación disfrazado de defecto del producto.

QUÉ HACE, Y POR QUÉ ASÍ:

  1. la versión mínima se declara UNA SOLA VEZ, aquí. Repetirla en cada script es
     exactamente cómo se llega a tres números para la misma cosa (hallazgo A-12)
  2. se comprueba ANTES de correr, no al fallar un import a mitad de una comprobación
  3. falla con un CÓDIGO DE SALIDA PROPIO —78, `EX_CONFIG`— distinto del 1 de «la
     comprobación no pasó» y del 2 de «me han invocado mal». Un entorno insuficiente ya no
     se puede confundir con un producto roto: son códigos distintos
  4. el mensaje dice qué falta, qué versión hay, qué versión hace falta y qué se rompería

Y UNA DECISIÓN QUE VA CONTRA LA COMODIDAD. La variable `ADS_ENTORNO_VERSION_MINIMA` sólo
puede SUBIR la exigencia, nunca bajarla. Una guarda que se puede relajar por entorno no es
una guarda: es un interruptor, y el primero que lo use en CI la apaga para todos. Se admite
para poder PROBAR la rama de fallo sin desinstalar Python, que es el único uso legítimo.

Uso:
  python3 kernel/operativo/validadores/entorno.py [--json]
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
import json
import os
import sys

# La versión mínima, y el motivo REAL de cada requisito. No es una preferencia: cada línea
# nombra la pieza de la biblioteca estándar sin la cual una comprobación concreta falla.
VERSION_MINIMA = (3, 11)
MOTIVOS = (
    "tomllib — `tooling/workspace.py` lee `SOURCES.toml` con la biblioteca TOML de la "
    "biblioteca estándar, disponible desde 3.11. Sin ella, el manifiesto de composición "
    "no se puede analizar y el validador de fuentes falla por el entorno",
)

# EX_CONFIG de sysexits(3). Se elige un código PROPIO a propósito: 1 ya significa «una
# comprobación no pasó» y 2 «uso incorrecto». Sin un tercer código, un entorno insuficiente
# es indistinguible de un producto defectuoso, que es justo el defecto que A14 describe.
CODIGO_ENTORNO_INSUFICIENTE = 78

VARIABLE_DE_EXIGENCIA = "ADS_ENTORNO_VERSION_MINIMA"


def _minimo_efectivo():
    """La exigencia vigente. La variable de entorno sólo puede SUBIRLA."""
    crudo = os.environ.get(VARIABLE_DE_EXIGENCIA, "").strip()
    if not crudo:
        return VERSION_MINIMA, None
    partes = crudo.split(".")
    try:
        pedido = tuple(int(p) for p in partes[:2])
    except ValueError:
        return VERSION_MINIMA, (f"{VARIABLE_DE_EXIGENCIA}={crudo!r} no es una versión "
                                f"«mayor.menor»: se ignora y manda la mínima declarada")
    if len(pedido) < 2:
        return VERSION_MINIMA, (f"{VARIABLE_DE_EXIGENCIA}={crudo!r} no declara «mayor.menor»: "
                                f"se ignora y manda la mínima declarada")
    if pedido <= VERSION_MINIMA:
        return VERSION_MINIMA, (f"{VARIABLE_DE_EXIGENCIA}={crudo} no supera la mínima "
                                f"declarada {'.'.join(map(str, VERSION_MINIMA))}: se ignora. "
                                f"Esta guarda no se puede relajar por entorno")
    return pedido, None


def informe():
    """Todo lo que hay que saber para decidir, sin decidir nada. Determinista."""
    minimo, aviso = _minimo_efectivo()
    actual = tuple(sys.version_info[:2])
    return {
        "version_actual": ".".join(map(str, actual)),
        "version_minima_declarada": ".".join(map(str, VERSION_MINIMA)),
        "version_minima_exigida": ".".join(map(str, minimo)),
        "suficiente": actual >= minimo,
        "codigo_si_insuficiente": CODIGO_ENTORNO_INSUFICIENTE,
        "motivos": list(MOTIVOS),
        "aviso": aviso,
    }


def mensaje(datos):
    lineas = [
        "ENTORNO INSUFICIENTE — no se ejecuta nada, y esto NO es un defecto del producto.",
        "",
        f"  intérprete en uso : {datos['version_actual']}  ({sys.executable})",
        f"  versión exigida   : {datos['version_minima_exigida']} o superior",
        "",
        "  por qué:",
    ]
    lineas += [f"    · {m}" for m in datos["motivos"]]
    lineas += [
        "",
        "  qué pasaría si se ejecutara igualmente: varias comprobaciones saldrían FALLIDAS",
        "  por el entorno, el runner NO republicaría su evidencia —correctamente— y la",
        "  cobertura publicada quedaría describiendo un corpus anterior sin que nada lo",
        "  dijera. Es la limitación A14, y esta guarda existe para cerrarla.",
        "",
        f"  código de salida  : {datos['codigo_si_insuficiente']}",
    ]
    return "\n".join(lineas)


def exigir(salida=sys.stderr):
    """Comprueba y, si no basta, TERMINA. Se llama antes de correr, no al primer import."""
    datos = informe()
    if datos["aviso"]:
        print(f"AVISO  {datos['aviso']}", file=salida)
    if datos["suficiente"]:
        return datos
    print(mensaje(datos), file=salida)
    raise SystemExit(CODIGO_ENTORNO_INSUFICIENTE)


def main():
    ap = argparse.ArgumentParser(description="guarda de versión del intérprete")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    datos = informe()
    if args.json:
        print(json.dumps(datos, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        if datos["aviso"]:
            print(f"AVISO  {datos['aviso']}", file=sys.stderr)
        if datos["suficiente"]:
            print(f"entorno suficiente : Python {datos['version_actual']} "
                  f"(mínima exigida {datos['version_minima_exigida']})")
        else:
            print(mensaje(datos), file=sys.stderr)
    return 0 if datos["suficiente"] else CODIGO_ENTORNO_INSUFICIENTE


if __name__ == "__main__":
    sys.exit(main())
