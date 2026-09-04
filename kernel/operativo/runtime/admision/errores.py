#!/usr/bin/env python3
"""errores — jerarquía tipada del verificador de admisión (`V2`–`V5`).

Todos llevan `codigo` estable en MAYUSCULAS_CON_GUION_BAJO, `str(error)` incluye el código,
y `a_dict()` produce la forma determinista que viaja en `--json` y en la evidencia.

DECISIÓN · jerarquía PROPIA, y no una rama de `ErrorDeEstado`
    Alternativas: (a) colgar de `estado.errores.ErrorDeEstado`; (b) raíz propia.
    Se elige (b). El §8 del motor es una lista CERRADA de fallos del estado durable, y
    `estado` documenta que no se ofrece un atajo para inventar códigos nuevos. Un fallo de
    ADMISIÓN no es un fallo del almacén: quien captura `ErrorDeEstado` alrededor de una
    transición no debe tragarse un veredicto rojo del verificador. Lo que sí se reutiliza es
    `relativizar`, porque la prohibición de publicar rutas absolutas es la misma.

DECISIÓN · el verificador NUNCA devuelve «lista vacía con éxito»
    Es `V6-03` literal. Cada una de las tres causas —truncamiento, codificación inválida y
    estructura ajena— tiene su clase, y su `detalle` NOMBRA la causa. Un `return []` ante
    una salida ilegible sería un falso verde silencioso, que es exactamente el modo de fallo
    que este corte existe para cerrar.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estado.errores import relativizar                              # noqa: E402


class ErrorDeAdmision(Exception):
    """Raíz de todo fallo del verificador de admisión."""

    CODIGO = "ERROR_DE_ADMISION"

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


# ── lectura de Git · `V6-01` a `V6-04` ────────────────────────────────────
class LecturaInsegura(ErrorDeAdmision):
    """Se ha pedido una lista de rutas con un separador que una ruta puede contener."""

    CODIGO = "LECTURA_INSEGURA"


class SalidaTruncada(ErrorDeAdmision):
    CODIGO = "SALIDA_TRUNCADA"


class SalidaNoDecodificable(ErrorDeAdmision):
    CODIGO = "SALIDA_NO_DECODIFICABLE"


class EstructuraAjena(ErrorDeAdmision):
    CODIGO = "ESTRUCTURA_AJENA"


class GitNoResponde(ErrorDeAdmision):
    CODIGO = "GIT_NO_RESPONDE"


class CensoDeLecturasSucio(ErrorDeAdmision):
    """Hay una invocación de Git fuera del canal único, o una lista sin `-z`."""

    CODIGO = "CENSO_DE_LECTURAS_SUCIO"


# ── perímetro y zonas · `V6-10` a `V6-12` ─────────────────────────────────
class ZonaSinCondicion(ErrorDeAdmision):
    """Una zona del censo derivado no declara condición de CONTENIDO. No pasa por omisión."""

    CODIGO = "ZONA_SIN_CONDICION"


class MutacionNoDeclarada(ErrorDeAdmision):
    CODIGO = "MUTACION_NO_DECLARADA"


class SedeDelOwnerAlterada(ErrorDeAdmision):
    """La sede APPEND-ONLY del Owner ha perdido o cambiado bytes ya publicados."""

    CODIGO = "SEDE_DEL_OWNER_ALTERADA"


class SedeIlegible(ErrorDeAdmision):
    """La estructura de una sede APPEND-ONLY no se puede derivar sin adivinar (`O27` §3).

    No es lo mismo que `SedeDelOwnerAlterada`: aquélla dice «esto cambió», y ésta dice «no
    he podido saber qué hay». Se separan porque confundirlas es exactamente el modo de
    fallo que `V6-03` cierra en el canal de lectura: un «no lo entiendo» que se contesta
    con una lista vacía y un verde.
    """

    CODIGO = "SEDE_ILEGIBLE"


class InstrumentoAlterado(ErrorDeAdmision):
    """El propio verificador o su política han mutado en la pasada que juzgan (`V6-11`)."""

    CODIGO = "INSTRUMENTO_ALTERADO"


class SinAnclaExterna(ErrorDeAdmision):
    """`V6-17`: el veredicto no puede sostenerse sólo en un digest del propio árbol."""

    CODIGO = "SIN_ANCLA_EXTERNA"


# ── fórmulas compartidas · `V6-19` ────────────────────────────────────────
class SedeDeFormulaAusente(ErrorDeAdmision):
    """La sede única de una fórmula compartida no se pudo importar: no se emite."""

    CODIGO = "SEDE_DE_FORMULA_AUSENTE"


class CensoDeFormulasSucio(ErrorDeAdmision):
    """Hay una SEGUNDA definición de una fórmula ya censada fuera de su sede."""

    CODIGO = "CENSO_DE_FORMULAS_SUCIO"


class DatoIlegible(ErrorDeAdmision):
    """Un fichero de datos del corpus no se pudo leer o no respeta el subconjunto admitido."""

    CODIGO = "DATO_ILEGIBLE"


CLASES = (
    ErrorDeAdmision, LecturaInsegura, SalidaTruncada, SalidaNoDecodificable,
    EstructuraAjena, GitNoResponde, CensoDeLecturasSucio, ZonaSinCondicion,
    MutacionNoDeclarada, SedeDelOwnerAlterada, SedeIlegible, InstrumentoAlterado,
    SinAnclaExterna, SedeDeFormulaAusente, CensoDeFormulasSucio, DatoIlegible,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
