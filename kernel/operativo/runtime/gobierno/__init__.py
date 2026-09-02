#!/usr/bin/env python3
"""gobierno — GOBIERNO GIT del REPOSITORIO DE CONTROL de ADS.

Instancia `g.14` de `docs/rediseno/g-ESTADO-DURABLE-APROBADA.md` —sede fijada por `O16`,
aprobada por `O23`— y demuestra `G-A8` de `g.16` con sus dos mitades:

    IMPOSIBLE    hook `reference-transaction` que rechaza toda actualización no
                 fast-forward y todo borrado de ref protegida
    DETECTABLE   `verificar_refs()` denuncia un forzado contra el linaje durable, aunque
                 el hook se hubiera retirado

Uso mínimo:

    import gobierno
    g = gobierno.inicializar("/ruta/al/control-repo", titular="runtime-A")
    g.conceder("refs/heads/canonica")
    preparacion = g.preparar("refs/heads/canonica", mensaje="alta", ficheros={"a.txt": b"1"})
    g.confirmar("refs/heads/canonica", preparacion)
    g.exigir_refs_intactas()

Sólo biblioteca estándar. `kernel/operativo/runtime` está en `sys.path` por el patrón del
repositorio, y desde ahí `import gobierno` funciona sin más.
"""
from __future__ import annotations

from .control import (
    DIGEST_DEL_HOOK,
    RAMA_CANONICA,
    GobiernoDelControlRepo,
    inicializar,
)
from .errores import (
    AutoridadDeRefNoConcedida,
    DobleEscritor,
    ErrorDeGobierno,
    EstadoParcialEnLaRama,
    ForzadoDetectado,
    GitFallo,
    GitInvocacionProhibida,
    HistoriaNoLineal,
    HookAusente,
    PoliticaViolada,
    RefProtegida,
    RevisionBaseObsoleta,
)
from .git import (
    BANDERAS_PROHIBIDAS,
    CONTENIDO_DEL_HOOK,
    NOMBRE_DEL_HOOK,
    NULO,
    ORDENES_DE_LISTA,
    CanalGit,
)
from .propiedad import Politica, cargar as cargar_politica

__all__ = [
    "GobiernoDelControlRepo", "inicializar", "RAMA_CANONICA", "DIGEST_DEL_HOOK",
    "CanalGit", "NULO", "BANDERAS_PROHIBIDAS", "ORDENES_DE_LISTA",
    "CONTENIDO_DEL_HOOK", "NOMBRE_DEL_HOOK",
    "Politica", "cargar_politica",
    "ErrorDeGobierno", "AutoridadDeRefNoConcedida", "RevisionBaseObsoleta",
    "DobleEscritor", "RefProtegida", "HistoriaNoLineal", "PoliticaViolada",
    "EstadoParcialEnLaRama", "ForzadoDetectado", "HookAusente",
    "GitInvocacionProhibida", "GitFallo",
]
