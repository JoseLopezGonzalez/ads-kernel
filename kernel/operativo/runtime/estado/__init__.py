#!/usr/bin/env python3
"""estado — motor de ESTADO DURABLE del CONTROL REPO de ADS.

Instancia la sección `(g)` (`docs/rediseno/g-ESTADO-DURABLE-APROBADA.md`), aprobada por el
Owner mediante `O23`, a través del contrato derivado del corte vertical 1 de `F6`.

Los TRES componentes durables de `g.1` viven en tres módulos distintos, con tres formatos
distintos y tres semánticas distintas, porque `I-g7` prohíbe colapsarlos:

    ESTADO CANÓNICO       `estado/canonico/<dominio>/<id>.json`   → `motor.py`
                          JSON indentado, legible sin herramienta, publicado por `os.replace`
    DIARIO CANÓNICO       `estado/diario/DIARIO.jsonl`            → `diario.py`
                          JSONL append-only encadenado por hash; explica el estado
    REGISTRO AUXILIAR     `estado/reconciliacion/REGISTRO.jsonl`  → `reconciliacion.py`
                          JSONL append-only, otra cadena, otro bloqueo; lo que NO se pudo hacer

Y un cuarto plano que NO es durable y se nombra para que no se confunda: `estado/operacional/`
—bloqueos y zona de preparación— es reconstruible y está excluido de la rama canónica.

Uso mínimo:

    import estado
    almacen = estado.inicializar("/ruta/al/control-repo")
    resultado = almacen.aplicar(estado.Transicion(
        tipo="alta", base=almacen.revision()["revision_id"],
        operaciones=[estado.Escritura("items/it-1.json", {"titulo": "primero"})],
        autor="DSP", motivo="alta del primer item", id="tx-alta-1",
    ))
    almacen.leer("items/it-1.json")

Este paquete importa **sólo biblioteca estándar**. `kernel/` no es un paquete Python: el
patrón del repositorio es insertar `kernel/operativo/runtime` en `sys.path` e `import estado`.
"""
from __future__ import annotations

from .atestacion import (
    ProveedorDeFirma,
    ProveedorEfimero,
    atestar,
    verificar_atestacion,
)
from .errores import (
    AlmacenNoInicializado,
    AlmacenYaInicializado,
    AtestacionInvalida,
    BloqueoNoAdquirido,
    DiarioCorrupto,
    ErrorDeEstado,
    EscritorConcurrente,
    EstadoCorrupto,
    PublicacionEnVuelo,
    EvidenciaDentroDelArbol,
    FormatoDesconocido,
    IdentificadorDuplicado,
    MigracionDesconocida,
    MigracionNoRecuperable,
    PermisoInsuficiente,
    ReconciliacionDesconocida,
    ReconciliacionPendiente,
    RecuperacionMarcada,
    RegistroDeReconciliacionCorrupto,
    ReintentosAgotados,
    RetiradaNoAdmisible,
    RetiradaSinTransicion,
    RevisionObsoleta,
    RutaInvalida,
    SelladoImposible,
    SinProveedorDeAtestacion,
    TransicionInvalida,
    UmbralDeSelladoInvalido,
    VersionDesconocida,
)
from .diario import InformeSellado, umbral_de_sellado
from .migracion import registradas as migraciones_registradas
from .motor import VERSION_DE_FORMATO, Almacen, abrir, inicializar
from .serializacion import VERSION_DE_ESQUEMA, cid, cid_de_objeto
from .transaccion import (
    Borrado,
    Escritura,
    InformeAuditoria,
    InformeIntegridad,
    InformeMigracion,
    InformeRecuperacion,
    ResultadoTransicion,
    Transicion,
)

__all__ = [
    "VERSION_DE_ESQUEMA", "VERSION_DE_FORMATO",
    "inicializar", "abrir", "Almacen",
    "Escritura", "Borrado", "Transicion",
    "ResultadoTransicion", "InformeRecuperacion", "InformeIntegridad",
    "InformeAuditoria", "InformeMigracion", "InformeSellado", "umbral_de_sellado",
    "ProveedorDeFirma", "ProveedorEfimero", "atestar", "verificar_atestacion",
    "cid", "cid_de_objeto", "migraciones_registradas",
    "ErrorDeEstado", "AlmacenNoInicializado", "AlmacenYaInicializado",
    "FormatoDesconocido", "VersionDesconocida", "RutaInvalida", "TransicionInvalida",
    "IdentificadorDuplicado", "RevisionObsoleta", "EscritorConcurrente",
    "BloqueoNoAdquirido", "ReintentosAgotados", "EstadoCorrupto", "PublicacionEnVuelo", "DiarioCorrupto",
    "RegistroDeReconciliacionCorrupto", "RecuperacionMarcada", "ReconciliacionPendiente",
    "ReconciliacionDesconocida", "MigracionDesconocida", "MigracionNoRecuperable",
    "PermisoInsuficiente", "SinProveedorDeAtestacion", "AtestacionInvalida",
    "EvidenciaDentroDelArbol",
    "UmbralDeSelladoInvalido", "SelladoImposible", "RetiradaSinTransicion",
    "RetiradaNoAdmisible",
]
