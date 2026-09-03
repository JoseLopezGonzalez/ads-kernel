#!/usr/bin/env python3
"""errores — la jerarquía tipada de los CUATRO MACROCIRCUITOS y de su `FASE 0`.

Misma forma que las tres raíces que ya existen —motor, runtime y ciclo—: el `codigo` vive en
la clase, `str()` lo incluye siempre, y la ruta se sanea en el constructor reutilizando
`estado.errores.relativizar`.

DECISIÓN · CUARTA raíz, y la razón es la tabla adversarial
    `§9.6` publica ONCE filas `X-S1`–`X-S11` y cada una declara «qué resultado es exigible».
    Un resultado exigible que se emitiera como `ErrorDeCiclo` genérico no se podría
    distinguir de una composición incompleta, y la prueba de la fila comprobaría que «algo
    falló» en vez de comprobar QUÉ falló. Cada fila tiene aquí su código, y la prueba lo
    compara: es la diferencia entre probar la tabla y probar que hay excepciones.

Cada clase declara la fila `X-S` que instancia, para que confrontarla sea leer.
"""
from __future__ import annotations

from estado.errores import relativizar


class ErrorDeMacrocircuito(Exception):
    """Raíz de todo fallo de los macrocircuitos. Nadie captura `Exception` por encima."""

    CODIGO = "ERROR_DE_MACROCIRCUITO"
    FILA = None

    def __init__(self, detalle="", ruta=None, codigo=None, **contexto):
        self.codigo = codigo or self.CODIGO
        self.detalle = detalle
        self.ruta = relativizar(ruta)
        self.contexto = dict(contexto)
        if self.FILA:
            self.contexto.setdefault("fila_adversarial", self.FILA)
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


class MacrocircuitoDesconocido(ErrorDeMacrocircuito):
    CODIGO = "MACROCIRCUITO_DESCONOCIDO"


class FaseDesconocida(ErrorDeMacrocircuito):
    CODIGO = "FASE_DESCONOCIDA"


class DefinicionIncoherente(ErrorDeMacrocircuito):
    """El conjunto derivado y la tabla de `§18` dejaron de coincidir."""

    CODIGO = "DEFINICION_INCOHERENTE"


class Fase0Omitida(ErrorDeMacrocircuito):
    """`X-S1`: se intenta mutar estado canónico sin haber hecho la `FASE 0`."""

    CODIGO = "FASE_0_OMITIDA"
    FILA = "X-S1"


class CertificacionCopiada(ErrorDeMacrocircuito):
    """`X-S2`: se presenta como propia una declaración de otra ejecución."""

    CODIGO = "CERTIFICACION_COPIADA"
    FILA = "X-S2"


class ReutilizacionInvalida(ErrorDeMacrocircuito):
    """`X-S3`: una sola huella distinta invalida la reutilización de evidencia."""

    CODIGO = "REUTILIZACION_INVALIDA"
    FILA = "X-S3"


class NivelNoAlcanzable(ErrorDeMacrocircuito):
    """`X-S4`: elevarse sin Estructural vigente DE ESA EJECUCIÓN."""

    CODIGO = "NIVEL_NO_ALCANZABLE"
    FILA = "X-S4"


class MutacionAntesDelGate(ErrorDeMacrocircuito):
    """`X-S5`: la `FASE 0` falla y el macrocircuito abre su iniciativa igualmente."""

    CODIGO = "MUTACION_ANTES_DEL_GATE"
    FILA = "X-S5"


class DosDeclaraciones(ErrorDeMacrocircuito):
    """`X-S6`: dos declaraciones Estructurales distintas en una misma ejecución."""

    CODIGO = "DOS_DECLARACIONES"
    FILA = "X-S6"


class ProductorIndebido(ErrorDeMacrocircuito):
    """`X-S7`: el propietario emite en vez de `SIS`, o continúa sin exigirla."""

    CODIGO = "PRODUCTOR_INDEBIDO"
    FILA = "X-S7"


class BloqueoDeSeguridad(ErrorDeMacrocircuito):
    """`X-S8`: `SEG` bloquea y su veto no lo levanta nadie."""

    CODIGO = "BLOQUEO_DE_SEGURIDAD"
    FILA = "X-S8"


class SujetoIncompleto(ErrorDeMacrocircuito):
    """`X-S9`: falta uno de los SEIS identificadores obligatorios de la regla 7."""

    CODIGO = "SUJETO_INCOMPLETO"
    FILA = "X-S9"


class IniciativaPrematura(ErrorDeMacrocircuito):
    """`X-S10`: la `FASE 0` abre iniciativa o consume contador para resolver su sujeto."""

    CODIGO = "INICIATIVA_PREMATURA"
    FILA = "X-S10"


class IncorporacionInvalida(ErrorDeMacrocircuito):
    """`X-S11`: escribir la celda en `estado/`, no incorporarla, o hacerlo con otra huella."""

    CODIGO = "INCORPORACION_INVALIDA"
    FILA = "X-S11"


class AutoridadIncompatible(ErrorDeMacrocircuito):
    """Dos macrocircuitos pretenden autoridad incompatible sobre el mismo producto."""

    CODIGO = "AUTORIDAD_INCOMPATIBLE"


class MacrocircuitoInconsistente(ErrorDeMacrocircuito):
    """FALLO CERRADO ante un estado que no casa con ninguna regla."""

    CODIGO = "MACROCIRCUITO_INCONSISTENTE"


CLASES = (
    ErrorDeMacrocircuito, MacrocircuitoDesconocido, FaseDesconocida, DefinicionIncoherente,
    Fase0Omitida, CertificacionCopiada, ReutilizacionInvalida, NivelNoAlcanzable,
    MutacionAntesDelGate, DosDeclaraciones, ProductorIndebido, BloqueoDeSeguridad,
    SujetoIncompleto, IniciativaPrematura, IncorporacionInvalida, AutoridadIncompatible,
    MacrocircuitoInconsistente,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))

# El censo de filas adversariales que esta jerarquía cubre, DERIVADO de las clases. Se
# ordena por el NÚMERO de la fila y no por su texto: `X-S10` va después de `X-S9`, y un
# orden lexicográfico lo pondría entre `X-S1` y `X-S2`, que es el orden de nadie.
FILAS_CUBIERTAS = tuple(sorted(
    (clase.FILA for clase in CLASES if clase.FILA),
    key=lambda fila: int(fila.rsplit("S", 1)[-1]),
))
