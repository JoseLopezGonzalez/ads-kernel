#!/usr/bin/env python3
"""errores — jerarquía tipada de la CONTENCIÓN DE PROCESOS. `FD-5`.

La regla que gobierna este paquete cabe en una línea, y es la que `FD-5` echaba en falta: **si
la política exige contención FUERTE y el anfitrión no la ofrece, el adaptador FALLA CERRADO.**
No degrada a `killpg` en silencio, no avisa y sigue, y no llama «aislamiento» a un grupo de
procesos del que cualquier `setsid` se sale.

Como en el resto del aparato, el saneado de rutas vive en el CONSTRUCTOR: ninguna salida de
este paquete imprime una ruta absoluta de la máquina.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estado.errores import relativizar                              # noqa: E402


class ErrorDeContencion(Exception):
    """Raíz de todo fallo de contención."""

    CODIGO = "ERROR_DE_CONTENCION"

    def __init__(self, detalle="", ruta=None, codigo=None, **contexto):
        self.codigo = codigo or self.CODIGO
        self.detalle = detalle
        self.ruta = relativizar(ruta)
        self.contexto = dict(contexto)
        super().__init__(str(self))

    def __str__(self):
        partes = ["[" + self.codigo + "]"]
        if self.detalle:
            partes.append(self.detalle)
        if self.ruta:
            partes.append("(" + str(self.ruta) + ")")
        return " ".join(partes)

    def a_dict(self):
        salida = {"codigo": self.codigo, "detalle": self.detalle, "ruta": self.ruta}
        if self.contexto:
            salida["contexto"] = {c: self.contexto[c] for c in sorted(self.contexto)}
        return salida


class ContencionFuerteNoDisponible(ErrorDeContencion):
    """La política exige `arbol-de-procesos` y el anfitrión no ofrece ningún backend fuerte.

    Es el fallo CERRADO de `FD-5`. Lo que NO se hace, y por eso tiene clase propia: elegir el
    backend simple, ejecutar igual y presentar el resultado como si estuviera contenido.
    """

    CODIGO = "CONTENCION_FUERTE_NO_DISPONIBLE"


class BackendNoDisponible(ErrorDeContencion):
    """Se pidió un backend concreto y su detección dice que este anfitrión no lo ofrece."""

    CODIGO = "BACKEND_NO_DISPONIBLE"


class NivelDesconocido(ErrorDeContencion):
    """El nivel de aislamiento pedido no pertenece al vocabulario cerrado."""

    CODIGO = "NIVEL_DESCONOCIDO"


class TareaInvalida(ErrorDeContencion):
    """La orden que se pide contener no es ejecutable."""

    CODIGO = "TAREA_INVALIDA"


class GrupoNoCancelado(ErrorDeContencion):
    """Tras cancelar quedaba descendencia viva. Es un fallo del backend, no del anfitrión."""

    CODIGO = "GRUPO_NO_CANCELADO"


CLASES = (
    ErrorDeContencion, ContencionFuerteNoDisponible, BackendNoDisponible,
    NivelDesconocido, TareaInvalida, GrupoNoCancelado,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
