#!/usr/bin/env python3
"""errores — la jerarquía tipada de fallos del RUNTIME y del DISPATCHER.

Instancia el §4.1 del contrato del corte 2. Cada clase lleva un `codigo` ESTABLE en
MAYUSCULAS_CON_GUION_BAJO, y `str(error)` lo incluye siempre: la evidencia de `F6` se
publica y se compara byte a byte, así que el contrato no puede ser el texto castellano del
detalle, que se puede reescribir, sino el código.

DECISIÓN · esta jerarquía NO deriva de `ErrorDeEstado`, y es a propósito
    Alternativas: (a) colgar `ErrorDeRuntime` de `estado.errores.ErrorDeEstado`, para que
    un solo `except` cubriese las dos; (b) dos raíces separadas.
    Se elige (b). El §7.1 de `11-ARQ` dice que el runtime NO es una fuente de verdad y que
    ejecuta contratos que ya existen: un fallo del MOTOR —revisión obsoleta, estado
    corrupto, diario corrupto— y un fallo del RUNTIME —autoridad perdida, ejecución
    fallida— tienen consecuencias distintas y autoridades distintas. Con (a), un
    `except ErrorDeEstado` escrito para tolerar una carrera del motor tragaría también una
    `AutoridadPerdida`, que es exactamente lo que nunca se puede tragar. Separarlas obliga
    a nombrar cuál se está tratando. La CLI captura las dos raíces, por separado y con el
    mismo código de salida.

DECISIÓN · la ruta se relativiza REUTILIZANDO `estado.errores.relativizar`
    La regla dura del §0 —«ninguna ruta absoluta de la máquina en ninguna salida»— ya tiene
    un saneador escrito y probado en el motor. Escribir aquí un segundo saneador sería una
    segunda definición de la misma fórmula, con dos sitios donde puede desincronizarse.
    Se importa el del motor.

`EfectoYaAplicado` está en la jerarquía porque el §4.1 lo pone ahí, pero se documenta lo
que es: una SEÑAL de idempotencia, no un fallo del usuario. El dispatcher no la levanta en
su camino normal —comprueba el acuse y reutiliza el resultado sin excepción alguna—; la
levanta `runtime.ejecucion` cuando alguien pide ejecutar un efecto que un acuse durable ya
declara aplicado, que es la única forma de que ese error signifique algo.
"""
from __future__ import annotations

from estado.errores import relativizar


class ErrorDeRuntime(Exception):
    """Raíz de todo fallo del runtime. Nadie captura `Exception` por encima de ésta."""

    CODIGO = "ERROR_DE_RUNTIME"

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
        """Forma determinista del error, apta para `--json` y para evidencia publicada."""
        salida = {"codigo": self.codigo, "detalle": self.detalle, "ruta": self.ruta}
        if self.contexto:
            salida["contexto"] = {c: self.contexto[c] for c in sorted(self.contexto)}
        return salida


class AutoridadNoDisponible(ErrorDeRuntime):
    """Otro titular VIVO tiene el lease del paquete. No se reintenta: sería doble despacho."""

    CODIGO = "AUTORIDAD_NO_DISPONIBLE"


class AutoridadPerdida(ErrorDeRuntime):
    """El lease cambió de titular o de época bajo los pies. NO se escribe nada."""

    CODIGO = "AUTORIDAD_PERDIDA"


class ReclamacionPrematura(ErrorDeRuntime):
    """Aún no hay `PACIENCIA` observaciones consecutivas sin que el latido avance."""

    CODIGO = "RECLAMACION_PREMATURA"


class PaqueteDesconocido(ErrorDeRuntime):
    CODIGO = "PAQUETE_DESCONOCIDO"


class EstadoDePaqueteInvalido(ErrorDeRuntime):
    """Transición de estado que el vocabulario cerrado del §3 no permite."""

    CODIGO = "ESTADO_DE_PAQUETE_INVALIDO"


class DependenciaNoResuelta(ErrorDeRuntime):
    CODIGO = "DEPENDENCIA_NO_RESUELTA"


class CapacidadNoSoportada(ErrorDeRuntime):
    """Ningún adaptador declara la capacidad requerida."""

    CODIGO = "CAPACIDAD_NO_SOPORTADA"


class AdaptadorIncompatible(ErrorDeRuntime):
    """Versión de contrato de adaptador incompatible con `VERSION_DE_CONTRATO`."""

    CODIGO = "ADAPTADOR_INCOMPATIBLE"


class EjecucionFallida(ErrorDeRuntime):
    """Fallo REINTENTABLE. Consume un intento y vuelve a `listo` si quedan."""

    CODIGO = "EJECUCION_FALLIDA"


class EjecucionDefinitiva(ErrorDeRuntime):
    """Fallo NO reintentable. Va directo a `agotado` con su registro de reconciliación."""

    CODIGO = "EJECUCION_DEFINITIVA"


class EjecucionCancelada(ErrorDeRuntime):
    CODIGO = "EJECUCION_CANCELADA"


class TiempoAgotado(ErrorDeRuntime):
    CODIGO = "TIEMPO_AGOTADO"


class EfectoYaAplicado(ErrorDeRuntime):
    """SEÑAL de idempotencia, no error de usuario: hay acuse durable de este efecto."""

    CODIGO = "EFECTO_YA_APLICADO"


class RuntimeInconsistente(ErrorDeRuntime):
    """FALLO CERRADO ante un estado que no casa con ninguna regla. Nunca se inventa estado."""

    CODIGO = "RUNTIME_INCONSISTENTE"


# Censo derivado, no escrito a mano dos veces: la CLI y las pruebas lo usan para comprobar
# que todo código emitido pertenece a la lista cerrada del §4.1.
CLASES = (
    ErrorDeRuntime, AutoridadNoDisponible, AutoridadPerdida, ReclamacionPrematura,
    PaqueteDesconocido, EstadoDePaqueteInvalido, DependenciaNoResuelta,
    CapacidadNoSoportada, AdaptadorIncompatible, EjecucionFallida, EjecucionDefinitiva,
    EjecucionCancelada, TiempoAgotado, EfectoYaAplicado, RuntimeInconsistente,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
