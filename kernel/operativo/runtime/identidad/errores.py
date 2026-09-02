#!/usr/bin/env python3
"""errores — jerarquía tipada de la identidad de firma externa. Instancia `O25`.

`O25` §2 termina con una frase que fija el comportamiento de todo este paquete: **la ausencia
de un proveedor válido provoca fallo cerrado**. No hay ruta por defecto, no hay firma vacía y
no hay `verificar` que devuelva `True` por cortesía.

Y §2 fija además qué NO puede aparecer nunca en un error de aquí: la clave privada «no
aparecerá en estado, diarios, evidencia, configuración exportada, logs o errores». Por eso
ningún error de este módulo lleva material sensible en su `detalle`, y una prueba con un
marcador único lo comprueba sobre TODAS las salidas.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estado.errores import relativizar                              # noqa: E402


class ErrorDeIdentidad(Exception):
    """Raíz de todo fallo de identidad y firma."""

    CODIGO = "ERROR_DE_IDENTIDAD"

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


class SinProveedorDeIdentidad(ErrorDeIdentidad):
    """`O25` §2: sin proveedor válido, FALLO CERRADO."""

    CODIGO = "SIN_PROVEEDOR_DE_IDENTIDAD"


class ConfiguracionDentroDelArbol(ErrorDeIdentidad):
    """`O25` §3 y `g.15`: la autoridad NO puede depender del árbol que verifica."""

    CODIGO = "CONFIGURACION_DENTRO_DEL_ARBOL"


class ConfiguracionInvalida(ErrorDeIdentidad):
    CODIGO = "CONFIGURACION_INVALIDA"


class IdentidadDesconocida(ErrorDeIdentidad):
    CODIGO = "IDENTIDAD_DESCONOCIDA"


class IdentidadRevocada(ErrorDeIdentidad):
    CODIGO = "IDENTIDAD_REVOCADA"


class IdentidadFueraDeSolapamiento(ErrorDeIdentidad):
    """Una identidad RETIRADA verifica dentro de su solapamiento, y fuera no."""

    CODIGO = "IDENTIDAD_FUERA_DE_SOLAPAMIENTO"


class FirmaInvalida(ErrorDeIdentidad):
    CODIGO = "FIRMA_INVALIDA"


class AnfitrionNoResponde(ErrorDeIdentidad):
    """La orden externa de firma del anfitrión falló. No se firma con nada en su lugar."""

    CODIGO = "ANFITRION_NO_RESPONDE"


CLASES = (
    ErrorDeIdentidad, SinProveedorDeIdentidad, ConfiguracionDentroDelArbol,
    ConfiguracionInvalida, IdentidadDesconocida, IdentidadRevocada,
    IdentidadFueraDeSolapamiento, FirmaInvalida, AnfitrionNoResponde,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
