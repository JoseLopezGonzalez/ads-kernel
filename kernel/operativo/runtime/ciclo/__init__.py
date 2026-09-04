#!/usr/bin/env python3
"""ciclo — EL CICLO COMPLETO de `§7.2` y `Continúa` de `§7.4`, sobre el runtime que ya existe.

Las OCHO etapas del `§7.2`, una por módulo, y ninguna reimplementa lo que ya está escrito:

    1 ENCUADRE                  `encuadre.py`      producto, control repo, fuentes, perfil,
                                                   política, precondiciones, capacidades, y
                                                   la clase de entrada entre las NUEVE
    2 COMPOSICIÓN DE RUTAS      `procesos.py`      `b.16` DERIVADO de los bloques
                                `rutas.py`         las CUATRO vías y el GATE DE COMPOSICIÓN
    3 MATERIALIZACIÓN           `equipos.py`       `C4`, sus siete pasos y sus prohibiciones
    4 PLANIFICACIÓN             `planificacion.py` items y paquetes POR EL RUNTIME
    5 DESPACHO                  `despacho.py`      DELEGA; punto único y observable
    6 GATES DE CAPA             `gates.py`         censo DERIVADO; ningún gate es normativo
    7 HANDOFFS                  `handoffs.py`      `C5` sobre las instancias declaradas
    8 CIERRE O CONTINUACIÓN     `cierre.py`        completar, bloquear, pausar, escalar,
                                                   continuar y DERIVAR con enlace durable

    `Continúa`                  `continuacion.py`  los SIETE pasos de `b.14`

Y tres módulos de servicio: `corpus.py` —el corpus canónico, leído con la stdlib—,
`durable.py` —la única puerta de escritura, que va al motor— y `errores.py`.

TRES REGLAS QUE ESTE PAQUETE SE IMPONE:

  1 · NO HAY UN SEGUNDO SISTEMA DE ESTADO. Todo lo durable es una `Transicion` sobre el
      `Almacen` de `estado/`, y el alta de trabajo pasa por `Runtime.crear_item` y
      `Runtime.crear_paquete`. Ni cola, ni diario, ni fichero de plan propio.
  2 · NADA SE DECIDE POR TEXTO LIBRE. El proceso se elige por MATERIA y ESTADO declarados;
      la vía 3 se activa por una CONDICIÓN declarada verdadera; la composición de equipo se
      elige por el identificador de la composición. Renombrar un item no mueve nada.
  3 · DETERMINISMO. Ningún artefacto de este paquete lleva reloj de pared, duración, número
      de ejecución ni pid. Todos los identificadores se derivan del CONTENIDO, de modo que
      repetir una operación produce el MISMO objeto y no un segundo.

Sólo biblioteca estándar. `kernel/` no es un paquete Python: el patrón del repositorio es
insertar `kernel/operativo/runtime` en `sys.path` e `import ciclo`.
"""
from __future__ import annotations

from .agentes import (
    Catalogo,
    Politica,
    asignar,
    asignar_rol,
    cargar_catalogo,
    catalogo_desde_texto,
    identificador_de_agente,
    seleccionar,
)
from .cierre import Cierre, resolver_obligaciones
from .continuacion import MODO_EJECUCION, MODO_PLAN, PASOS, Continuacion, como_texto
from .corpus import CAPACIDADES, CONDICIONES_DE_B16, Corpus, analizar, bloques
from .despacho import PUNTO_DE_ENTRADA, barrido, despachar, observar
from .encuadre import clases_que_crean_trabajo, clasificar, encuadrar
from .equipos import (
    derivar_capacidades,
    exigir_agentes_asignados,
    exigir_capacidad,
    exigir_separacion,
    exigir_slots_coherentes,
    materializar,
)
from .errores import (
    AgenteSobreasignado,
    AlcanceNoAutorizado,
    CatalogoDeModelosAusente,
    CardinalDeAgentesIlegible,
    CatalogoDeModelosInvalido,
    CicloInconsistente,
    CierreBloqueado,
    ComposicionDeEquipoAusente,
    ComposicionIncompleta,
    CondicionVaga,
    ConflictoDeRoles,
    CriterioDeComparacionAusente,
    CorpusIlegible,
    CorpusIncompleto,
    DecisionDelOwnerPendiente,
    DegradacionInvalida,
    DerivaNoTransaccional,
    DevolucionSinEvidencia,
    EncuadreIncompleto,
    EntradaNoClasificable,
    EntradaSinTrabajo,
    ErrorDeCiclo,
    EstadoDeMateriaInvalido,
    GateDesconocido,
    GateFallido,
    GateNormativo,
    HandoffDesconocido,
    HandoffIncompleto,
    HandoffRechazado,
    LimiteDeCapacidadExcedido,
    MateriaSinProceso,
    MetodoNoEsCapacidad,
    ObligacionHuerfana,
    ObligacionSinProductora,
    PaqueteIlegible,
    PerfilDesconocido,
    PlanificacionInvalida,
    PrecondicionIncumplida,
    ProcesoDesconocido,
    PropietarioNoDerivable,
    RetiradaSinAutoridad,
    RepartoIncoherente,
    RepartoSinUnidades,
    RolSinAgente,
    TrabajoAmbiguo,
    VariosAgentesSinIntegrador,
    VolumenExcedeElContexto,
    ViaInvalida,
)
from .gates import aplicar as aplicar_gate, censo as censo_de_gates, exigir_no_amplia, \
    exigir_no_normativo
from .handoffs import ENTREGAS_DECLARADAS_EN_8_0, acusar, catalogo, devolver, emitir, \
    rechazar, reanudacion
from .planificacion import Planificador
from .procesos import (
    CORRESPONDENCIA,
    ESTADOS_DEL_OBJETO,
    MATERIAS,
    capacidad_de,
    metodo_de,
    proceso_de,
)
from .rutas import PRESENCIAS, VIAS, componer, exigir_composicion_completa, traza

__all__ = [
    "Corpus", "analizar", "bloques", "CAPACIDADES", "CONDICIONES_DE_B16",
    "encuadrar", "clasificar", "clases_que_crean_trabajo",
    "CORRESPONDENCIA", "MATERIAS", "ESTADOS_DEL_OBJETO", "proceso_de",
    "capacidad_de", "metodo_de",
    "componer", "exigir_composicion_completa", "traza", "VIAS", "PRESENCIAS",
    "materializar", "derivar_capacidades", "exigir_capacidad",
    "exigir_agentes_asignados", "exigir_slots_coherentes", "exigir_separacion",
    "Politica", "Catalogo", "cargar_catalogo", "catalogo_desde_texto",
    "asignar", "asignar_rol", "seleccionar", "identificador_de_agente",
    "Planificador",
    "despachar", "barrido", "observar", "PUNTO_DE_ENTRADA",
    "aplicar_gate", "censo_de_gates", "exigir_no_normativo", "exigir_no_amplia",
    "catalogo", "emitir", "acusar", "rechazar", "devolver", "reanudacion",
    "ENTREGAS_DECLARADAS_EN_8_0",
    "Cierre", "resolver_obligaciones",
    "Continuacion", "PASOS", "MODO_PLAN", "MODO_EJECUCION", "como_texto",
    "ErrorDeCiclo", "CorpusIlegible", "CorpusIncompleto", "EntradaNoClasificable",
    "EncuadreIncompleto", "PrecondicionIncumplida", "EntradaSinTrabajo",
    "ProcesoDesconocido", "MateriaSinProceso", "EstadoDeMateriaInvalido",
    "PropietarioNoDerivable", "ViaInvalida", "CondicionVaga", "ComposicionIncompleta",
    "ComposicionDeEquipoAusente", "ConflictoDeRoles", "MetodoNoEsCapacidad",
    "ObligacionSinProductora", "PaqueteIlegible", "VariosAgentesSinIntegrador", "CardinalDeAgentesIlegible", "RepartoSinUnidades",
    "CriterioDeComparacionAusente", "VolumenExcedeElContexto", "RepartoIncoherente",
    "CatalogoDeModelosAusente", "CatalogoDeModelosInvalido", "PerfilDesconocido",
    "RolSinAgente", "AgenteSobreasignado", "DegradacionInvalida",
    "PlanificacionInvalida", "LimiteDeCapacidadExcedido", "AlcanceNoAutorizado",
    "GateDesconocido", "GateFallido", "GateNormativo",
    "HandoffDesconocido", "HandoffIncompleto", "HandoffRechazado",
    "DevolucionSinEvidencia", "ObligacionHuerfana", "RetiradaSinAutoridad",
    "CierreBloqueado", "DecisionDelOwnerPendiente", "TrabajoAmbiguo",
    "DerivaNoTransaccional", "CicloInconsistente",
]
