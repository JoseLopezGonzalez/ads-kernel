#!/usr/bin/env python3
"""contencion — `FD-5`: AISLAMIENTO DE PROCESOS del adaptador local.

Lo que este paquete cierra, y lo que NO.

    LO QUE CIERRA   un descendiente que ejecuta `setsid` deja de escapar cuando la política
                    exige `arbol-de-procesos` y el anfitrión ofrece un contenedor de
                    recursos: espacio de nombres de PID, `cgroup v2`, ámbito de `systemd` o
                    contenedor. La cancelación y el timeout limpian TODA la descendencia
    LO QUE NO       no retira el backend simple ni finge que sea otra cosa. `killpg` sigue
                    disponible con su nivel `grupo-de-procesos` DECLARADO, y su límite
                    —medido y probado— es que el bisnieto que hace `setsid` SOBREVIVE

**LA LIMITACIÓN NO SE OCULTA: SE MIDE.** La batería lanza hijo, nieto y bisnieto, los tres
haciendo `setsid`, y comprueba por PID que con el backend fuerte NO sobrevive ninguno y con
el simple SÍ sobrevive el que se salió del grupo. Esa pareja de pruebas es la que impide
presentar el débil como fuerte.

Módulos:

    deteccion.py   sondas REALES de las capacidades del anfitrión, con su motivo
    backends.py    un backend por mecanismo, con su nivel y su forma de matar
    politica.py    la elección del mejor disponible y el FALLO CERRADO
    ejecutor.py    el lanzamiento, el progreso, el timeout y la cancelación
    errores.py     la jerarquía tipada

Uso mínimo:

    from contencion import Politica, ejecutar
    resultado = ejecutar(["sh", "-c", "echo hola"], espacio="/tmp/x",
                         limite_segundos=5, politica=Politica("arbol-de-procesos"))
    resultado.nivel_de_aislamiento     # `arbol-de-procesos`
"""
from __future__ import annotations

from . import backends, deteccion, ejecutor, politica
from .backends import pids_con_marca, sigue_vivo
from .deteccion import (
    ARBOL_DE_PROCESOS,
    GRUPO_DE_PROCESOS,
    NIVELES,
    ORDEN_DE_PREFERENCIA,
    capacidades,
)
from .ejecutor import Resultado, ejecutar, esperar_a_que_mueran
from .errores import (
    BackendNoDisponible,
    ContencionFuerteNoDisponible,
    ErrorDeContencion,
    GrupoNoCancelado,
    NivelDesconocido,
    TareaInvalida,
)
from .politica import Politica, elegir, instanciar

__all__ = [
    "capacidades", "ORDEN_DE_PREFERENCIA", "NIVELES",
    "GRUPO_DE_PROCESOS", "ARBOL_DE_PROCESOS",
    "Politica", "elegir", "instanciar",
    "ejecutar", "Resultado", "esperar_a_que_mueran",
    "pids_con_marca", "sigue_vivo",
    "backends", "deteccion", "ejecutor", "politica",
    "ErrorDeContencion", "ContencionFuerteNoDisponible", "BackendNoDisponible",
    "NivelDesconocido", "TareaInvalida", "GrupoNoCancelado",
]
