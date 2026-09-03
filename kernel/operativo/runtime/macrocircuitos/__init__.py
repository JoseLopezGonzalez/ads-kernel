#!/usr/bin/env python3
"""macrocircuitos — los CUATRO de `§8`, como COMPOSICIONES DEL MISMO MOTOR.

    N   instalación en proyecto nuevo
    A   adopción de un producto con historia
    M   migración desde una versión anterior
    U   actualización del propio ADS

Tres módulos, y ni uno más:

    `definicion.py`   el MAPEO de `§18`, fase a fase, DERIVADO y comprobado contra `b.16`
    `fase0.py`        `gate:sistema-conforme` y su SOPORTE DURABLE. UN contrato, cuatro veces
    `motor.py`        el ejecutor ÚNICO, parametrizado. Sin una sola rama por circuito

LO QUE ESTE PAQUETE SE COMPROMETE A SOSTENER, y sus pruebas ejercen:

  1 · LOS CUATRO PASAN POR EL MISMO PUNTO. No hay cuatro runtimes: hay una clase y cuatro
      definiciones. El despacho entra por `ciclo.despacho.despachar`, que es observable, y
      la batería lo mide en las cuatro ejecuciones.
  2 · LA `FASE 0` ES LA MISMA. Un solo contrato invocado cuatro veces (regla 6 de `O17`), y
      `definicion.comprobar()` verifica que las cuatro filas coinciden campo a campo.
  3 · NINGUNA MUTACIÓN CANÓNICA ANTES DEL GATE. La `FASE 0` no escribe en `estado/` —no
      puede: `estado/` nace después— y si `gate:sistema-conforme` no se supera, el
      macrocircuito no abre nada.
  4 · DOS MACROCIRCUITOS NO COMPARTEN AUTORIDAD. La autoridad sobre un producto es un
      objeto durable tomado por comparación e intercambio: de dos procesos reales que
      compitan, exactamente uno la consigue.

Sólo biblioteca estándar. `kernel/` no es un paquete Python: el patrón del repositorio es
insertar `kernel/operativo/runtime` en `sys.path` e `import macrocircuitos`.
"""
from __future__ import annotations

from .definicion import (
    FASE_0,
    GATE_DE_FASE_0,
    IDENTIFICADORES,
    MACROCIRCUITOS,
    SECUENCIA_DECLARADA_EN_8_0,
    capacidades_de_la_fase,
    comprobar,
    fase,
    macrocircuito,
    secuencia_de_procesos,
)
from .errores import (
    AutoridadIncompatible,
    BloqueoDeSeguridad,
    CertificacionCopiada,
    DefinicionIncoherente,
    DosDeclaraciones,
    ErrorDeMacrocircuito,
    FaseDesconocida,
    Fase0Omitida,
    FILAS_CUBIERTAS,
    IncorporacionInvalida,
    IniciativaPrematura,
    MacrocircuitoDesconocido,
    MacrocircuitoInconsistente,
    MutacionAntesDelGate,
    NivelNoAlcanzable,
    ProductorIndebido,
    ReutilizacionInvalida,
    SujetoIncompleto,
)
from .fase0 import (
    IDENTIFICADORES as IDENTIFICADORES_DEL_SUJETO,
    SOPORTE,
    exigir_estructural_vigente,
    exigir_fase0_antes_de_mutar,
    exigir_sujeto_completo,
    huella_del_sujeto,
    incorporar,
    resolver_sujeto,
    reutilizar_evidencia,
)
from .motor import TERMINACIONES, Macrocircuito, materia_de

__all__ = [
    "MACROCIRCUITOS", "IDENTIFICADORES", "macrocircuito", "fase", "comprobar",
    "secuencia_de_procesos", "SECUENCIA_DECLARADA_EN_8_0", "FASE_0", "GATE_DE_FASE_0",
    "capacidades_de_la_fase",
    "Macrocircuito", "TERMINACIONES", "materia_de",
    "IDENTIFICADORES_DEL_SUJETO", "SOPORTE", "resolver_sujeto", "huella_del_sujeto",
    "exigir_sujeto_completo", "exigir_fase0_antes_de_mutar", "exigir_estructural_vigente",
    "reutilizar_evidencia", "incorporar",
    "ErrorDeMacrocircuito", "MacrocircuitoDesconocido", "FaseDesconocida",
    "DefinicionIncoherente", "Fase0Omitida", "CertificacionCopiada",
    "ReutilizacionInvalida", "NivelNoAlcanzable", "MutacionAntesDelGate",
    "DosDeclaraciones", "ProductorIndebido", "BloqueoDeSeguridad", "SujetoIncompleto",
    "IniciativaPrematura", "IncorporacionInvalida", "AutoridadIncompatible",
    "MacrocircuitoInconsistente", "FILAS_CUBIERTAS",
]
