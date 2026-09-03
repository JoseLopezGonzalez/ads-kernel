#!/usr/bin/env python3
"""errores — jerarquía tipada del derivador y de la suite de árboles adversariales.

`V6-15` mide su cierre con DOS restas —`entrada − suite = ∅` y `suite − entrada = ∅`— y con
la reproducción, uno a uno, de los árboles que la entrada entrega. Cada forma de fallar tiene
aquí su clase, porque un `AssertionError` genérico no dice CUÁL de las dos restas se abrió.

REGLA COMÚN A TODO EL PAQUETE, heredada de `estado/errores.py`: el saneado vive en el
CONSTRUCTOR. Ninguna salida de este paquete imprime una ruta absoluta de la máquina, y por
eso la ruta se relativiza al entrar y no al imprimir: relativizar al imprimir depende de que
todos los sitios que imprimen se acuerden, y uno solo que no lo haga publica la ruta entera.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estado.errores import relativizar                              # noqa: E402


class ErrorDeArboles(Exception):
    """Raíz de todo fallo del derivador y de la suite."""

    CODIGO = "ERROR_DE_ARBOLES"

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


class SedeAusente(ErrorDeArboles):
    """El documento o la cabecera que un árbol declara como sede no está en el árbol."""

    CODIGO = "SEDE_AUSENTE"


class ArbolDuplicado(ErrorDeArboles):
    """Dos entradas del conjunto derivado nombran el MISMO árbol."""

    CODIGO = "ARBOL_DUPLICADO"


class ArbolNoCubierto(ErrorDeArboles):
    """`entrada − suite ≠ ∅`: la entrada entrega un árbol que la suite no reproduce."""

    CODIGO = "ARBOL_NO_CUBIERTO"


class FixtureSinArbol(ErrorDeArboles):
    """`suite − entrada ≠ ∅`: la suite exige un árbol que la entrada no entrega."""

    CODIGO = "FIXTURE_SIN_ARBOL"


class AtaqueInerte(ErrorDeArboles):
    """El control DEL ATAQUE: el árbol atacado no difiere del sano en lo que el ataque dice.

    Es la clase que impide el peor falso verde de una suite adversarial: una prueba que pasa
    porque el ataque no llegó a aplicarse. Sin esta comprobación, un fixture roto y un
    remedio correcto son indistinguibles.
    """

    CODIGO = "ATAQUE_INERTE"


class ReproduccionInvalida(ErrorDeArboles):
    """La versión VULNERABLE no aceptó el ataque, o la VIGENTE no lo rechazó por su propiedad."""

    CODIGO = "REPRODUCCION_INVALIDA"


CLASES = (
    ErrorDeArboles, SedeAusente, ArbolDuplicado, ArbolNoCubierto, FixtureSinArbol,
    AtaqueInerte, ReproduccionInvalida,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
