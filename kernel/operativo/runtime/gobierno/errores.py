#!/usr/bin/env python3
"""errores — jerarquía tipada del gobierno Git del control repo (`g.14`).

Misma forma que la del motor de estado: `codigo` estable, `str(error)` con el código, y
`a_dict()` determinista. Y por la misma razón, raíz PROPIA: un fallo de gobierno de refs no
es un fallo del almacén, y quien captura `ErrorDeEstado` no debe tragarse un forzado
detectado.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estado.errores import relativizar                              # noqa: E402


class ErrorDeGobierno(Exception):
    """Raíz de todo fallo del gobierno Git del control repo."""

    CODIGO = "ERROR_DE_GOBIERNO"

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


class AutoridadDeRefNoConcedida(ErrorDeGobierno):
    """Se ha pedido mutar una ref sin concesión vigente, o la concesión es de otro."""

    CODIGO = "AUTORIDAD_DE_REF_NO_CONCEDIDA"


class RevisionBaseObsoleta(ErrorDeGobierno):
    """La revisión base contra la que se preparó la mutación ya no es la vigente."""

    CODIGO = "REVISION_BASE_OBSOLETA"


class DobleEscritor(ErrorDeGobierno):
    CODIGO = "DOBLE_ESCRITOR"


class RefProtegida(ErrorDeGobierno):
    """Se ha intentado borrar o mover fuera de política una ref protegida."""

    CODIGO = "REF_PROTEGIDA"


class HistoriaNoLineal(ErrorDeGobierno):
    """La actualización propuesta no es fast-forward respecto del valor viejo."""

    CODIGO = "HISTORIA_NO_LINEAL"


class PoliticaViolada(ErrorDeGobierno):
    CODIGO = "POLITICA_VIOLADA"


class EstadoParcialEnLaRama(ErrorDeGobierno):
    """`g.14`: la rama canónica NUNCA contiene estado parcial."""

    CODIGO = "ESTADO_PARCIAL_EN_LA_RAMA"


class ForzadoDetectado(ErrorDeGobierno):
    """La mitad DETECTABLE de `G-A8`: alguien movió una ref fuera del linaje registrado.

    Se levanta aunque el hook `reference-transaction` haya sido retirado, porque no depende
    de él: contrasta el linaje DURABLE del almacén contra las refs vivas del repositorio.
    """

    CODIGO = "FORZADO_DETECTADO"


class HookAusente(ErrorDeGobierno):
    """La mitad IMPOSIBLE de `G-A8`: falta el hook, o su contenido no es el esperado."""

    CODIGO = "HOOK_AUSENTE"


class GitInvocacionProhibida(ErrorDeGobierno):
    """Se ha intentado invocar Git con una bandera que el canal único no admite."""

    CODIGO = "GIT_INVOCACION_PROHIBIDA"


class GitFallo(ErrorDeGobierno):
    """Git devolvió un código distinto de cero en una invocación que exigía éxito."""

    CODIGO = "GIT_FALLO"


CLASES = (
    ErrorDeGobierno, AutoridadDeRefNoConcedida, RevisionBaseObsoleta, DobleEscritor,
    RefProtegida, HistoriaNoLineal, PoliticaViolada, EstadoParcialEnLaRama,
    ForzadoDetectado, HookAusente, GitInvocacionProhibida, GitFallo,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
