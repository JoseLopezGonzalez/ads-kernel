#!/usr/bin/env python3
"""politica — la ELECCIÓN del backend y el FALLO CERRADO de `FD-5`.

Las dos reglas que `FD-5` fija, y son las dos mitades de lo mismo:

    · si la política exige CONTENCIÓN FUERTE y no está disponible, se FALLA CERRADO
    · NO se degrada en silencio a `killpg`

DECISIÓN · el nivel se PIDE, no se deduce del backend elegido
    Alternativas: (a) pedir un backend concreto; (b) pedir un NIVEL y que el aparato elija.
    Se elige (b) como forma normal, conservando (a) para las pruebas y el diagnóstico. Quien
    escribe una política no quiere «cgroups»: quiere que la descendencia no escape. Pedir el
    nivel hace que un anfitrión distinto siga cumpliendo la política con otro mecanismo, y
    que uno que no pueda cumplirla lo diga en vez de aparentarlo.

DECISIÓN · pedir explícitamente `grupo-de-procesos` es LEGÍTIMO, y se registra
    El backend simple no se retira: se conserva «sólo con nivel de aislamiento explícitamente
    inferior, declarado», que es lo que `FD-5` permite. Pedirlo es una decisión consciente y
    queda en el resultado; lo que no existe es la vía por la que se acaba usando sin haberlo
    pedido.

DECISIÓN · la degradación NO es un aviso: es una excepción
    Alternativas: (a) registrar un aviso y seguir con el simple; (b) `ContencionFuerteNoDisponible`.
    Se elige (b). Un aviso lo lee quien opera y lo ignora quien ataca, y sobre todo: el
    resultado de una ejecución degradada es indistinguible del de una contenida cuando nadie
    lee el aviso. Con la excepción, la ausencia de contención fuerte NO produce ejecución.
"""
from __future__ import annotations

from . import backends, deteccion
from .errores import BackendNoDisponible, ContencionFuerteNoDisponible, NivelDesconocido


class Politica:
    """Qué nivel de aislamiento se exige, y qué se hace cuando el anfitrión no lo da."""

    def __init__(self, nivel_exigido=deteccion.ARBOL_DE_PROCESOS, *, backend=None):
        if nivel_exigido not in deteccion.NIVELES:
            raise NivelDesconocido(
                "nivel de aislamiento fuera del vocabulario `"
                + " · ".join(deteccion.NIVELES) + "`: " + str(nivel_exigido)
            )
        self.nivel_exigido = nivel_exigido
        self.backend_pedido = backend

    def a_dict(self):
        return {"nivel_exigido": self.nivel_exigido,
                "backend_pedido": self.backend_pedido}


def elegir(politica, capacidades=None):
    """Devuelve `(identificador, evidencia)` del backend elegido, o FALLA CERRADO."""
    informe = capacidades if capacidades is not None else deteccion.capacidades()
    por_identificador = {fila["backend"]: fila for fila in informe["backends"]}

    if politica.backend_pedido is not None:
        fila = por_identificador.get(politica.backend_pedido)
        if fila is None:
            raise BackendNoDisponible(
                "backend de contención desconocido: " + str(politica.backend_pedido))
        if not fila["disponible"]:
            raise BackendNoDisponible(
                "el backend `" + fila["backend"] + "` no está disponible en este "
                "anfitrión: " + fila["motivo"], backend=fila["backend"])
        if (politica.nivel_exigido == deteccion.ARBOL_DE_PROCESOS
                and fila["nivel"] != deteccion.ARBOL_DE_PROCESOS):
            raise ContencionFuerteNoDisponible(
                "se pidió el backend `" + fila["backend"] + "`, cuyo nivel es `"
                + fila["nivel"] + "`, y la política exige `"
                + deteccion.ARBOL_DE_PROCESOS + "`. No se degrada en silencio",
                backend=fila["backend"], nivel=fila["nivel"])
        return fila["backend"], fila["evidencia"]

    for identificador in informe["orden_de_preferencia"]:
        fila = por_identificador.get(identificador)
        if fila is None or not fila["disponible"]:
            continue
        if politica.nivel_exigido == deteccion.ARBOL_DE_PROCESOS:
            if fila["nivel"] != deteccion.ARBOL_DE_PROCESOS:
                continue
        return fila["backend"], fila["evidencia"]

    if politica.nivel_exigido == deteccion.ARBOL_DE_PROCESOS:
        raise ContencionFuerteNoDisponible(
            "la política exige contención FUERTE (`" + deteccion.ARBOL_DE_PROCESOS
            + "`) y este anfitrión no ofrece ningún backend que la dé. NO se degrada a "
            "`killpg`: sin contención fuerte no se ejecuta",
            sondas=[fila["backend"] + ": " + fila["motivo"]
                    for fila in informe["backends"]
                    if fila["nivel"] == deteccion.ARBOL_DE_PROCESOS],
        )
    raise BackendNoDisponible(
        "no hay ningún backend de contención disponible en este anfitrión")


def instanciar(politica, *, espacio, capacidades=None):
    """Elige el backend según la política y lo instancia. Falla cerrado si no lo hay."""
    identificador, evidencia = elegir(politica, capacidades)
    return backends.crear(identificador, espacio=espacio, evidencia=evidencia)
