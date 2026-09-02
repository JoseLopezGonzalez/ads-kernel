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
