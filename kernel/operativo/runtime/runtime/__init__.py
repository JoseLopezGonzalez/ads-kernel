#!/usr/bin/env python3
"""runtime — el RUNTIME y el DISPATCHER de ADS sobre el motor de ESTADO DURABLE.

Instancia el §7 de `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` a través del §4 del
contrato derivado del corte 2 de `F6`, y se apoya en `estado/`, que ya existe y no se toca.

La frase que gobierna el paquete entero está en el §7.1 y conviene tenerla delante:

    ES        el EJECUTOR de contratos que ya existen.
    NO ES     una fuente de verdad. Todo lo que decide queda escrito en el estado canónico
              ANTES de que valga. Si el runtime muere, el estado sigue siendo el estado.

De ahí salen las cuatro propiedades que este paquete se compromete a sostener, y que sus
pruebas ejercen sobre procesos reales:

  1 · NO HAY UN SEGUNDO SISTEMA DE ESTADO. Todo lo durable —items, paquetes, leases y
      acuses de efecto— es una `Transicion` sobre el `Almacen` de `estado/`. Ni cola en
      memoria, ni fichero de trabajo propio, ni diario paralelo, ni recuperación
      alternativa. El único fichero que este paquete escribe fuera del motor es el testigo
      de vida del §3, y vive en `estado/operacional/`, que está gitignorado, no es durable
      y es reconstruible.
  2 · NO PUEDE HABER DOBLE DESPACHO. La autoridad sobre un paquete es un lease durable, y
      tomarlo es una comparación e intercambio sobre la revisión: de dos instancias reales
      que compitan, exactamente una lo consigue.
  3 · UN EFECTO CONFIRMADO NO SE APLICA DOS VECES. El resultado del paquete y el acuse
      `efectos/<efecto>.json` se escriben en la MISMA transición: o se ven los dos, o no se
      ve ninguno.
  4 · EL TIEMPO LÓGICO ES LA REVISIÓN, NO EL RELOJ. `I-g3` prohíbe reloj de pared,
      duración, número de ejecución e identidad de proceso en cualquier byte durable. La
      expiración de un lease se decide por OBSERVACIONES CONTADAS, no por un plazo.

Uso mínimo:

    import runtime
    with runtime.Runtime(repo, instancia="runtime-A",
                         registro_de_adaptadores=registro) as rt:
        rt.crear_item(id="it-0001", titulo="primero", motivo="alta")
        rt.crear_paquete(id="pq-0001", item="it-0001",
                         capacidades_requeridas=["proceso-local"],
                         orden={"adaptador": "proceso-local", "operacion": "ejecutar",
                                "argumentos": ["exito"], "limite_segundos": 30})
        rt.ciclo()

Sólo biblioteca estándar. `kernel/` no es un paquete Python: el patrón del repositorio es
insertar `kernel/operativo/runtime` en `sys.path` e `import runtime`.
"""
from __future__ import annotations

from .dispatcher import Cancelacion, Runtime
from .ejecucion import (
    VERSION_DE_CONTRATO,
    Adaptador,
    AdaptadorEnPruebas,
    RegistroDeAdaptadores,
    RegistroEnPruebas,
    comprobar_adaptador,
    exigir_efecto_no_aplicado,
)
from .errores import (
    AdaptadorIncompatible,
    AutoridadNoDisponible,
    AutoridadPerdida,
    CapacidadNoSoportada,
    DependenciaNoResuelta,
    EfectoYaAplicado,
    EjecucionCancelada,
    EjecucionDefinitiva,
    EjecucionFallida,
    ErrorDeRuntime,
    EstadoDePaqueteInvalido,
    PaqueteDesconocido,
    ReclamacionPrematura,
    RuntimeInconsistente,
    TiempoAgotado,
)
from .lease import PACIENCIA_POR_DEFECTO, TestigoDeVida
from .modelo import (
    ESTADOS,
    ESTADOS_TERMINALES,
    TRANSICIONES,
    comprobar_paquete,
    comprobar_transicion,
    derivar_efecto,
    ruta_efecto,
    ruta_item,
    ruta_lease,
    ruta_paquete,
)
from .politica import MAX_INTENTOS_POR_DEFECTO

__all__ = [
    "Runtime", "Cancelacion",
    "PACIENCIA_POR_DEFECTO", "MAX_INTENTOS_POR_DEFECTO", "VERSION_DE_CONTRATO",
    "TestigoDeVida",
    "Adaptador", "RegistroDeAdaptadores", "comprobar_adaptador",
    "AdaptadorEnPruebas", "RegistroEnPruebas", "exigir_efecto_no_aplicado",
    "ESTADOS", "ESTADOS_TERMINALES", "TRANSICIONES",
    "comprobar_paquete", "comprobar_transicion", "derivar_efecto",
    "ruta_item", "ruta_paquete", "ruta_lease", "ruta_efecto",
    "ErrorDeRuntime", "AutoridadNoDisponible", "AutoridadPerdida",
    "ReclamacionPrematura", "PaqueteDesconocido", "EstadoDePaqueteInvalido",
    "DependenciaNoResuelta", "CapacidadNoSoportada", "AdaptadorIncompatible",
    "EjecucionFallida", "EjecucionDefinitiva", "EjecucionCancelada", "TiempoAgotado",
    "EfectoYaAplicado", "RuntimeInconsistente",
]
