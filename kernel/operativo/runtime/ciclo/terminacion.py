#!/usr/bin/env python3
"""terminacion — los NIVELES DE TERMINACIÓN y el CIRCUITO BASE que impide reducirlos.

HECHO MEDIDO ANTES DE CONSTRUIR (La Pesquerapp, 2026-09-14). De 36 items «cerrados», 33
tenían una sola cadena de evidencia y su forma típica era «PR #14 … SIN FUSIONAR». Un
item con un solo estado terminal —`cerrado`— colapsaba en la misma palabra ocho hechos
distintos: que se implementó, que otro lo revisó, que se integró, que se verificó, que
alguien lo usó, que alguien lo miró, que el Owner lo aceptó y que el producto lo tiene. El
Owner lo dijo en una frase: «no quiero volver a ver un item considerado cerrado mientras el
propio estado reconoce que nadie ha abierto la pantalla».

Los niveles NO son un estado nuevo del item: son DERIVADOS. Cada uno existe cuando existe
el DICTAMEN de su gate, emitido por un revisor que no es el autor (`gates.aplicar` lo exige
por capacidad; aquí se exige además por TRABAJADOR, que es donde se cuela la
autocertificación). Un nivel sin dictamen no está alcanzado, diga lo que diga el diario.

    implementado         gate:implementacion-completa      lo juzga quien revisa, no quien hizo
    revisado             gate:revision-de-construccion     revisión independiente del diff
    integrado            gate:convergencia-de-fuentes      Integration Set con revisiones exactas
    verificado           gate:evidencia-suficiente         el dosier de VER
    validado-funcional   gate:uso-comprobado               evidencia de uso real (USO)
    validado-visual      gate:excelencia-visual            la pasada de FIDELIDAD de DIS
    aceptado             gate:aceptacion-del-owner         el Owner, sobre lo que él exige
    cerrado              cierre `completado` del item       y todos los exigidos, resueltos

El CIRCUITO BASE lo declara el PROYECTO en su `PROFILE.md` —bloques `ads:circuito-base`—
y fija, por clase de trabajo, qué niveles son obligatorios. La única forma de no alcanzar
un nivel obligatorio es que el circuito declare una INAPLICABILIDAD con una condición
sobre HECHOS del item, evaluada aquí, mecánicamente. «No hace falta» no es una condición.

DECISIÓN · las condiciones de inaplicabilidad tienen una gramática CERRADA y minúscula
    `<hecho> <operador> [<valor>]`, unidas con ` y ` / ` o `. Operadores: `==`, `!=`,
    `incluye`, `excluye`, `vacio`, `no-vacio`, `es-verdadero`, `es-falso`. Los HECHOS los
    aporta quien evalúa —la instancia deriva `escribe_fuentes`, `afecta_superficie`, etc.
    del item— y una condición que nombre un hecho ausente NO es verdadera: es un error que
    se publica. Una gramática mayor invitaría a escribir criterio; ésta sólo admite datos.
"""
from __future__ import annotations

import re

from . import formas
from .corpus import Corpus, bloques
from .errores import (
    AutocertificacionRechazada,
    CircuitoBaseIlegible,
    CircuitoBaseIncumplido,
)

NIVELES = (
    "implementado", "revisado", "integrado", "verificado", "validado-funcional",
    "validado-visual", "aceptado", "cerrado",
)

GATE_DEL_NIVEL = {
    "implementado": "gate:implementacion-completa",
    "revisado": "gate:revision-de-construccion",
    "integrado": "gate:convergencia-de-fuentes",
    "verificado": "gate:evidencia-suficiente",
    "validado-funcional": "gate:uso-comprobado",
    "validado-visual": "gate:excelencia-visual",
    "aceptado": "gate:aceptacion-del-owner",
}

ALCANZADO = "alcanzado"
PENDIENTE = "pendiente"
INAPLICABLE = "inaplicable"
NO_EXIGIDO = "no-exigido"
RECHAZADO = "rechazado"

PERFIL_DEL_PROYECTO = "PROFILE.md"
BLOQUE = "circuito-base"

OPERADORES = ("==", "!=", "incluye", "excluye", "vacio", "no-vacio", "es-verdadero",
              "es-falso")


# ===========================================================================
#  circuitos base, leídos del PROFILE del proyecto
# ===========================================================================
def circuitos_base_desde_texto(texto, *, corpus=None, sede=PERFIL_DEL_PROYECTO):
    """Los bloques `ads:circuito-base` de un texto, VALIDADOS, por clase de trabajo."""
    corpus = corpus or Corpus()
    esquema = corpus.esquema(BLOQUE)
    salida = {}
    for clase, datos, _ruta, linea in bloques(texto, sede):
        if clase != BLOQUE:
            continue
        fallos = formas.validar(datos, esquema, corpus=corpus, camino="circuito-base")
        if fallos:
            raise CircuitoBaseIlegible(
                sede + ":" + str(linea) + ": " + "; ".join(fallos), ruta=sede,
            )
        for regla in datos.get("inaplicabilidad") or []:
            comprobar_condicion(regla["condicion"])
            if regla["nivel"] not in datos["niveles_obligatorios"]:
                raise CircuitoBaseIlegible(
                    sede + ":" + str(linea) + ": `" + datos["id"] + "` declara inaplicable "
                    "el nivel `" + regla["nivel"] + "`, que no está entre sus obligatorios",
                    ruta=sede,
                )
        clave = datos["clase_de_trabajo"]
        if clave in salida:
            raise CircuitoBaseIlegible(
                sede + ": dos circuitos base para la clase `" + clave + "`", ruta=sede,
            )
        salida[clave] = datos
    return salida


def cargar_circuitos_base(ruta_control_repo, *, corpus=None):
    import os
    sede = os.path.join(ruta_control_repo, PERFIL_DEL_PROYECTO)
    if not os.path.isfile(sede):
        raise CircuitoBaseIlegible(
            "el control repo no trae `" + PERFIL_DEL_PROYECTO + "`, que es donde el "
            "proyecto declara sus circuitos base", ruta=PERFIL_DEL_PROYECTO,
        )
    with open(sede, "r", encoding="utf-8") as manejador:
        texto = manejador.read()
    circuitos = circuitos_base_desde_texto(texto, corpus=corpus)
    if not circuitos:
        raise CircuitoBaseIlegible(
            "`" + PERFIL_DEL_PROYECTO + "` no declara ningún bloque `ads:circuito-base`: sin "
            "circuito base no hay suelo que impida cerrar un item a medias",
            ruta=PERFIL_DEL_PROYECTO,
        )
    return circuitos


def circuito_de(circuitos, clase_de_trabajo):
    if clase_de_trabajo not in circuitos:
        raise CircuitoBaseIlegible(
            "no hay circuito base para la clase de trabajo `" + str(clase_de_trabajo)
            + "`; declaradas: " + ", ".join(sorted(circuitos)),
        )
    return circuitos[clase_de_trabajo]


# ===========================================================================
#  la gramática de condiciones
# ===========================================================================
_TERMINO = re.compile(
    r"^(?P<hecho>[a-z_][a-z0-9_.]*)\s+(?P<operador>==|!=|incluye|excluye|vacio|no-vacio|"
    r"es-verdadero|es-falso)(?:\s+(?P<valor>\S+))?$"
)


def comprobar_condicion(condicion):
    """La condición cabe en la gramática, o no es una condición. No evalúa."""
    for disyuncion in str(condicion).split(" o "):
        for termino in disyuncion.split(" y "):
            casa = _TERMINO.match(termino.strip())
            if not casa:
                raise CircuitoBaseIlegible(
                    "condición fuera de la gramática cerrada: `" + termino.strip() + "`. "
                    "Forma: `<hecho> <operador> [<valor>]` con operador en "
                    + ", ".join(OPERADORES),
                )
            if casa.group("operador") in ("==", "!=", "incluye", "excluye") \
                    and not casa.group("valor"):
                raise CircuitoBaseIlegible(
                    "el operador `" + casa.group("operador") + "` exige un valor: `"
                    + termino.strip() + "`",
                )
    return condicion


def evaluar_condicion(condicion, hechos):
    """`(verdadera, detalle)`. Un hecho ausente hace FALSO el término y lo dice."""
    comprobar_condicion(condicion)
    detalles = []
    resultado_or = False
    for disyuncion in str(condicion).split(" o "):
        resultado_and = True
        for termino in disyuncion.split(" y "):
            casa = _TERMINO.match(termino.strip())
            hecho, operador, valor = casa.group("hecho"), casa.group("operador"), casa.group("valor")
            if hecho not in hechos:
                detalles.append(termino.strip() + " → FALSO (hecho `" + hecho + "` ausente)")
                resultado_and = False
                continue
            dato = hechos[hecho]
            verdad = _aplicar(operador, dato, valor)
            detalles.append(termino.strip() + " → " + ("VERDADERO" if verdad else "FALSO"))
            resultado_and = resultado_and and verdad
        resultado_or = resultado_or or resultado_and
    return resultado_or, detalles


def _aplicar(operador, dato, valor):
    if operador == "==":
        return str(dato).lower() == str(valor).lower()
    if operador == "!=":
        return str(dato).lower() != str(valor).lower()
    if operador == "incluye":
        return isinstance(dato, (list, tuple, set)) and str(valor) in {str(d) for d in dato}
    if operador == "excluye":
        return isinstance(dato, (list, tuple, set)) and str(valor) not in {str(d) for d in dato}
    if operador == "vacio":
        return not dato
    if operador == "no-vacio":
        return bool(dato)
    if operador == "es-verdadero":
        return dato is True
    if operador == "es-falso":
        return dato is False
    return False


# ===========================================================================
#  evaluar los niveles de un item
# ===========================================================================
def _dictamen_del_nivel(nivel, dictamenes, *, paquetes_del_item, item):
    """El dictamen SUPERADO del gate del nivel sobre el item, o `None`, o RECHAZO."""
    gate = GATE_DEL_NIVEL[nivel]
    mejor = None
    for dictamen in dictamenes:
        if dictamen.get("gate") != gate or dictamen.get("dictamen") != "superado":
            continue
        entrada = dictamen.get("entrada") or {}
        sobre = str(entrada.get("sobre_paquete") or entrada.get("paquete") or "")
        sobre_item = str(entrada.get("item") or "")
        if sobre and sobre not in paquetes_del_item and sobre_item != item:
            continue
        if not sobre and sobre_item != item:
            continue
        autor = str(entrada.get("autor_titular") or "")
        revisor = str(entrada.get("revisor_titular") or "")
        if autor and revisor and autor == revisor:
            raise AutocertificacionRechazada(
                "el dictamen `" + str(dictamen.get("id")) + "` de `" + gate + "` lo firma el "
                "MISMO trabajador que produjo lo juzgado (`" + autor + "`); un nivel no se "
                "alcanza por autocertificación", gate=gate, titular=autor,
            )
        mejor = dictamen
    return mejor


def evaluar(circuito, *, item, paquetes_del_item, dictamenes, hechos, cierre=None):
    """El estado de cada nivel del circuito para un item. DERIVADO; no escribe nada."""
    exigidos = list(circuito["niveles_obligatorios"])
    reglas = {r["nivel"]: r for r in (circuito.get("inaplicabilidad") or [])}
    filas = []
    faltan = []
    for nivel in NIVELES:
        if nivel == "cerrado":
            continue
        fila = {"nivel": nivel, "gate": GATE_DEL_NIVEL[nivel], "exigido": nivel in exigidos,
                "estado": NO_EXIGIDO, "motivo": "", "dictamen": None}
        if nivel in exigidos:
            regla = reglas.get(nivel)
            inaplicable, detalle = (False, [])
            if regla is not None:
                inaplicable, detalle = evaluar_condicion(regla["condicion"], hechos)
            try:
                dictamen = _dictamen_del_nivel(nivel, dictamenes,
                                               paquetes_del_item=paquetes_del_item, item=item)
            except AutocertificacionRechazada as error:
                fila["estado"] = RECHAZADO
                fila["motivo"] = error.detalle
                faltan.append(nivel)
                filas.append(fila)
                continue
            if dictamen is not None:
                fila["estado"] = ALCANZADO
                fila["dictamen"] = dictamen.get("id")
                fila["motivo"] = "dictamen superado de `" + fila["gate"] + "` por `" + str(
                    dictamen.get("revisor")) + "`"
            elif inaplicable:
                fila["estado"] = INAPLICABLE
                fila["motivo"] = ("inaplicable por `" + regla["condicion"] + "` (" + "; ".join(
                    detalle) + "), declarado por " + regla["quien_lo_declara"])
            else:
                fila["estado"] = PENDIENTE
                fila["motivo"] = ("sin dictamen superado de `" + fila["gate"] + "`"
                                  + ("; la condición de inaplicabilidad no se cumple: "
                                     + "; ".join(detalle) if regla is not None else ""))
                faltan.append(nivel)
        filas.append(fila)
    cerrado = bool(cierre and cierre.get("salida") == "completado")
    filas.append({
        "nivel": "cerrado", "gate": "gate:cierre-de-item", "exigido": True,
        "estado": ALCANZADO if (cerrado and not faltan) else PENDIENTE,
        "motivo": ("cierre completado y todos los niveles exigidos resueltos" if cerrado and
                   not faltan else ("faltan: " + ", ".join(faltan) if faltan else
                                    "sin cierre completado del item")),
        "dictamen": cierre.get("id") if cierre else None,
    })
    return {
        "item": item,
        "circuito": circuito["id"],
        "clase_de_trabajo": circuito["clase_de_trabajo"],
        "niveles": filas,
        "alcanzados": [f["nivel"] for f in filas if f["estado"] == ALCANZADO],
        "inaplicables": [f["nivel"] for f in filas if f["estado"] == INAPLICABLE],
        "faltan": faltan,
        "puede_cerrar": not faltan,
        "nivel_mas_alto": _mas_alto(filas),
    }


def _mas_alto(filas):
    """El nivel más alto alcanzado SIN huecos por debajo: no se salta un escalón."""
    alto = None
    for fila in filas:
        if fila["nivel"] == "cerrado":
            break
        if not fila["exigido"] or fila["estado"] == INAPLICABLE:
            continue
        if fila["estado"] == ALCANZADO:
            alto = fila["nivel"]
        else:
            break
    return alto


def exigir_cierre(evaluacion):
    if not evaluacion["puede_cerrar"]:
        raise CircuitoBaseIncumplido(
            "el item `" + evaluacion["item"] + "` NO puede cerrarse como producto: faltan los "
            "niveles " + ", ".join(evaluacion["faltan"]) + " del circuito `"
            + evaluacion["circuito"] + "`. Un nivel se alcanza con el dictamen de su gate "
            "por un revisor que no es el autor, o se declara inaplicable por una condición "
            "del circuito; no hay una tercera vía",
            item=evaluacion["item"], faltan=list(evaluacion["faltan"]),
        )
    return evaluacion
