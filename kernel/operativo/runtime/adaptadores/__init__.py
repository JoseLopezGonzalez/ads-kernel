#!/usr/bin/env python3
"""adaptadores — contrato de ADAPTADOR y huella de PROYECCIÓN. Corte `V7`.

Sede: `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` §6 (las cuatro piezas) y §3.4 (la ficha
del tipo `adaptador`). Interfaz de ejecución: §4.4 del contrato del macrobloque 2 de `F6`,
respetada al byte porque el runtime programa contra ella.

Qué entra en este corte y qué no:

    SÍ   pieza 1 · la ficha declarada, con sus trece campos
    SÍ   pieza 2 · compilar una proyección estampando la HUELLA de sus entradas
    SÍ   pieza 3 · el validador de deriva, con sus TRES diagnósticos
    SÍ   un adaptador local REAL, con proceso, progreso, timeout que mata e idempotencia
    NO   pieza 4 · la prueba de humo en sesión nueva. Exige abrir un entorno de agente de
         verdad, y §6.5 dice que sin ella el nivel alcanzado es `desconocido`. Se declara,
         no se finge.

Y una frase de §6.5 que este paquete respeta literalmente: **un adaptador NO PUEDE
DECLARARSE `soportado`**. Aquí no hay ningún campo `nivel` y no se ofrece ninguno.
"""
from __future__ import annotations

from .contrato import (
    AMBIGUO,
    CAMPOS_DE_FICHA,
    ESTADOS,
    VERSION_DE_CONTRATO,
    Adaptador,
    AdaptadorIncompatible,
    Cancelacion,
    CapacidadNoSoportada,
    ErrorDeAdaptador,
    FichaDeAdaptador,
    OrdenInvalida,
    ProyeccionDerivada,
    ProyeccionObsoleta,
    comprobar_resultado,
)
from .proceso import (
    PUNTOS_DE_FALLO,
    VARIABLE_DE_FALLO,
    AdaptadorDeProcesoLocal,
    puntos_de_fallo,
)
from .proyeccion import (
    AL_DIA,
    EDITADA_A_MANO,
    OBSOLETA,
    comparar_proyecciones,
    compilar,
    exigir_al_dia,
    huella_de_entradas,
    validar_deriva,
)
from .registro import RegistroDeAdaptadores

__all__ = [
    "VERSION_DE_CONTRATO", "ESTADOS", "AMBIGUO", "CAMPOS_DE_FICHA",
    "PUNTOS_DE_FALLO", "VARIABLE_DE_FALLO", "puntos_de_fallo",
    "Adaptador", "FichaDeAdaptador", "Cancelacion", "comprobar_resultado",
    "RegistroDeAdaptadores", "AdaptadorDeProcesoLocal",
    "compilar", "validar_deriva", "exigir_al_dia", "huella_de_entradas",
    "comparar_proyecciones", "AL_DIA", "EDITADA_A_MANO", "OBSOLETA",
    "ErrorDeAdaptador", "CapacidadNoSoportada", "AdaptadorIncompatible",
    "OrdenInvalida", "ProyeccionDerivada", "ProyeccionObsoleta",
]
