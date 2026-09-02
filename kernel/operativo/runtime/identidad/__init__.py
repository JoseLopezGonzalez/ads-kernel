#!/usr/bin/env python3
"""identidad — TITULARIDAD Y CUSTODIA de la identidad de firma externa. Instancia `O25`.

`O25`, de 2026-09-02, cierra `FD-1` como decisión del Owner y fija:

    §1 titularidad     la identidad pertenece a la RAÍZ EXTERNA de cada instalación, y la
                       autoridad administrativa es del Owner. NO pertenece al repositorio
                       verificado, al control repo, al kernel, al runtime ni a un agente
    §2 custodia        la clave la custodia el ANFITRIÓN. Fuera de todo repositorio, sin
                       versionar, ausente de estado, diarios, evidencia, configuración
                       exportada, logs y errores. Sin proveedor válido, FALLO CERRADO
    §3 autoridad       la configuración externa establece la identidad pública aceptada, y
                       el repositorio verificado NO puede cambiar por sí mismo cuál es
    §4 evidencia       firmas y huellas públicas SÍ entran al repositorio; la clave y la
                       autoridad de validar, no
    §5 implementación  criptografía estándar de biblioteca mantenida, NUNCA primitivas
                       propias. Rotación, solapamiento explícito, activa · retirada ·
                       revocada, rechazo de desconocida y de revocada, trazabilidad sin
                       revelación

Lo que este paquete NO hace, y `O25` §6 lo dice antes que nadie: no declara implementada ni
certificada la raíz externa, no completa `F6` y no desbloquea PesquerApp.

Reutiliza `estado.ProveedorDeFirma` y `estado.ProveedorEfimero`; no los duplica.
"""
from __future__ import annotations

from .configuracion import (
    ConfiguracionDeConfianza,
    cargar,
    exigir_fuera_del_arbol,
)
from .errores import (
    AnfitrionNoResponde,
    ConfiguracionDentroDelArbol,
    ConfiguracionInvalida,
    ErrorDeIdentidad,
    FirmaInvalida,
    IdentidadDesconocida,
    IdentidadFueraDeSolapamiento,
    IdentidadRevocada,
    SinProveedorDeIdentidad,
)
from .proveedor import ProveedorProductivo, exigir_proveedor
from .rotacion import (
    ACTIVA,
    ESTADOS,
    REVOCADA,
    RETIRADA,
    SOLAPAMIENTO_POR_DEFECTO,
    AnilloDeIdentidades,
    Identidad,
)

__all__ = [
    "cargar", "ConfiguracionDeConfianza", "exigir_fuera_del_arbol",
    "ProveedorProductivo", "exigir_proveedor",
    "AnilloDeIdentidades", "Identidad", "ACTIVA", "RETIRADA", "REVOCADA", "ESTADOS",
    "SOLAPAMIENTO_POR_DEFECTO",
    "ErrorDeIdentidad", "SinProveedorDeIdentidad", "ConfiguracionDentroDelArbol",
    "ConfiguracionInvalida", "IdentidadDesconocida", "IdentidadRevocada",
    "IdentidadFueraDeSolapamiento", "FirmaInvalida", "AnfitrionNoResponde",
]
