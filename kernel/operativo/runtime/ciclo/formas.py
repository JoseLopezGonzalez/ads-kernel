#!/usr/bin/env python3
"""formas — validar un OBJETO DE ESTADO contra un esquema del corpus, con la stdlib.

`ads_lint.py` valida los BLOQUES del corpus contra `esquemas/*.yaml`, y lo hace con PyYAML
en el repositorio del kernel. Lo que este módulo valida es otra cosa: objetos que nacen EN
EJECUCIÓN —una entrega de un trabajador, un circuito base leído del PROFILE del proyecto,
un ejecutor— contra los MISMOS esquemas, en el runtime de un producto instalado, donde sólo
hay biblioteca estándar. Dos validadores contra un solo esquema: el esquema es la sede, y
ninguno de los dos lo copia.

DECISIÓN · los campos DESCONOCIDOS son ERROR, no aviso
    El lint avisa de un campo extra en un bloque del corpus porque el corpus lo escribe una
    persona y lo revisa otra. Una entrega la escribe un agente y la consume una máquina: un
    campo que ningún esquema declara es, en el mejor caso, un dato que nadie va a leer, y en
    el peor una forma de colar contenido por un nombre parecido. Aquí falla cerrado.

DECISIÓN · las `ref` se RESUELVEN contra el corpus cuando hay corpus, y siempre por forma
    `ref_a: rol` exige que el rol exista; `ref_a: gate`, que el gate esté en el censo. Sin
    corpus se comprueba sólo la forma del identificador. Se dice cuál de las dos se hizo.
"""
from __future__ import annotations

import re

from .corpus import CAPACIDADES

RESOLUTORES = {
    "rol": lambda corpus, valor: valor in corpus.roles(),
    "gate": lambda corpus, valor: valor in corpus.gates(),
    "capacidad": lambda corpus, valor: valor.split(":", 1)[0] in CAPACIDADES,
    "metodo": lambda corpus, valor: _existe_metodo(corpus, valor),
    "perfil-agente": lambda corpus, valor: valor in corpus.perfiles(),
    "entrada": lambda corpus, valor: valor in corpus.entradas(),
    "contrato-base": lambda corpus, valor: any(
        d.get("id") == valor for d in corpus.de_tipo("contrato-base")),
}


def _existe_metodo(corpus, valor):
    try:
        corpus.metodo(valor)
    except Exception:              # noqa: BLE001 - la ausencia es una respuesta, no un fallo
        return False
    return True


def validar(datos, esquema, *, corpus=None, camino=""):
    """Devuelve la lista de fallos, vacía si el objeto cumple el esquema. No levanta."""
    fallos = []
    campos = esquema.get("campos") or {}
    _validar_objeto(datos, campos, esquema.get("obligatorios") or [],
                    esquema.get("obligatorios_alternativos") or [], camino or esquema.get(
                        "esquema", "objeto"), corpus, fallos)
    return fallos


def exigir(datos, esquema, *, corpus=None, camino="", error=ValueError):
    fallos = validar(datos, esquema, corpus=corpus, camino=camino)
    if fallos:
        raise error("; ".join(fallos))
    return datos


def _validar_objeto(valor, campos, obligatorios, alternativos, camino, corpus, fallos):
    if not isinstance(valor, dict):
        fallos.append(camino + ": se esperaba un mapa")
        return
    for requerido in obligatorios:
        if requerido not in valor or valor[requerido] is None:
            fallos.append(camino + "." + requerido + ": obligatorio y no declarado; si la "
                          "respuesta es «ninguno», se declara vacío")
    for grupo in alternativos:
        puestos = [c for c in grupo if valor.get(c) is not None]
        if len(puestos) != 1:
            fallos.append(camino + ": de [" + ", ".join(grupo) + "] se declara EXACTAMENTE "
                          "uno, y hay " + str(len(puestos)))
    for clave in sorted(valor):
        if clave == "esquema":
            continue
        if clave not in campos:
            fallos.append(camino + "." + clave + ": campo que el esquema no declara")
            continue
        if valor[clave] is None:
            continue
        _validar_valor(valor[clave], campos[clave], camino + "." + clave, corpus, fallos)


def _validar_valor(valor, spec, camino, corpus, fallos):
    tipo = spec.get("tipo", "texto")
    if tipo == "texto":
        if not isinstance(valor, str):
            fallos.append(camino + ": se esperaba texto")
            return
        if "min" in spec and len(valor.strip()) < int(spec["min"]):
            fallos.append(camino + ": texto demasiado corto (" + str(len(valor.strip()))
                          + " < " + str(spec["min"]) + ")")
        if "patron" in spec and not re.fullmatch(str(spec["patron"]), valor):
            fallos.append(camino + ": '" + valor + "' no casa con " + str(spec["patron"]))
    elif tipo == "entero":
        if not isinstance(valor, int) or isinstance(valor, bool):
            fallos.append(camino + ": se esperaba entero")
            return
        if "min" in spec and valor < int(spec["min"]):
            fallos.append(camino + ": " + str(valor) + " < " + str(spec["min"]))
    elif tipo == "numero":
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            fallos.append(camino + ": se esperaba número")
    elif tipo == "booleano":
        if not isinstance(valor, bool):
            fallos.append(camino + ": se esperaba true/false")
    elif tipo == "enum":
        valores = spec.get("valores") or []
        if valor not in valores:
            fallos.append(camino + ": '" + str(valor) + "' no está en " + str(valores))
    elif tipo == "ref":
        if not isinstance(valor, str) or not valor.strip():
            fallos.append(camino + ": una ref es texto no vacío")
            return
        destino = spec.get("ref_a")
        resolutor = RESOLUTORES.get(destino)
        if corpus is not None and resolutor is not None and not resolutor(corpus, valor):
            fallos.append(camino + ": '" + valor + "' no existe como " + str(destino)
                          + " en el corpus")
    elif tipo == "lista":
        if not isinstance(valor, list):
            fallos.append(camino + ": se esperaba lista")
            return
        if "min" in spec and len(valor) < int(spec["min"]):
            fallos.append(camino + ": " + str(len(valor)) + " elementos < " + str(spec["min"]))
        de = spec.get("de", "texto")
        for indice, elemento in enumerate(valor):
            sub = dict(spec)
            sub.pop("min", None)
            sub["tipo"] = de
            _validar_valor(elemento, sub, camino + "[" + str(indice) + "]", corpus, fallos)
    elif tipo == "objeto":
        _validar_objeto(valor, spec.get("campos") or {}, spec.get("obligatorios") or [],
                        spec.get("obligatorios_alternativos") or [], camino, corpus, fallos)
    else:
        fallos.append(camino + ": tipo desconocido '" + str(tipo) + "' en el esquema")
