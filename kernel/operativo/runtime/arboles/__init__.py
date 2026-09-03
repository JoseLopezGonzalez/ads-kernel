#!/usr/bin/env python3
"""arboles — `V6-15`: los ÁRBOLES ADVERSARIALES como FIXTURES OBLIGATORIOS.

Sede del punto: `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` §20.1, fila `V6-15`, y §20.5,
que fija de dónde sale el conjunto y por qué NO se enumera a mano.

    ENTRADA      los árboles adversariales que un gate publicó CON CABECERA PROPIA en su
                 documento inmutable, cada uno identificado por esa cabecera y por el
                 documento que la contiene. **Se DERIVA**, no se escribe
    SALIDA       la suite de regresión, con la procedencia —documento y cabecera— de cada
                 fixture y el identificador del hallazgo que cerró cada árbol
    CIERRE       `entrada − suite = ∅` **y** `suite − entrada = ∅`, las dos restas sobre el
                 MISMO conjunto de ÁRBOLES
    REPARTO      especifica `SIS` en `F4c`; CONSTRUYE `F6`. Este paquete es la construcción

**NINGÚN CARDINAL DEL CONJUNTO SE ESCRIBE AQUÍ.** Ni en el código, ni en el contrato
derivado, ni en la salida del punto ejecutable. Es la regla de `J-07` que §20.5 aplica a esta
fila: quien necesite el número ejecuta el derivador. Si un gate futuro publica otro árbol con
la misma cabecera, el conjunto crece solo y la resta `entrada − suite` lo denuncia.

Módulos:

    derivador.py   deriva el conjunto de la sede, valida cada entrada y detecta duplicados
    versiones.py   las versiones históricas VULNERABLES, una por propiedad atacada
    ataques.py     cada árbol MATERIALIZADO en un repositorio Git real, con su control
    suite.py       la matriz de cuatro columnas y las dos restas de cierre

Uso mínimo:

    from arboles import suite
    informe = suite.ejecutar("/ruta/al/repo")
    informe["ok"]           # True si las dos restas cierran y la matriz entera pasa
"""
from __future__ import annotations

from . import ataques, derivador, suite, versiones
from .ataques import ATAQUES, Ataque
from .derivador import Arbol, derivar, duplicados, exigir_sin_duplicados, exigir_validas
from .errores import (
    ArbolDuplicado,
    ArbolNoCubierto,
    AtaqueInerte,
    ErrorDeArboles,
    FixtureSinArbol,
    ReproduccionInvalida,
    SedeAusente,
)
from .suite import cruzar, ejecutar, exigir_cobertura, serializar
from .versiones import VERSIONES, VersionVulnerable

__all__ = [
    "derivar", "duplicados", "exigir_sin_duplicados", "exigir_validas", "Arbol",
    "cruzar", "exigir_cobertura", "ejecutar", "serializar",
    "ATAQUES", "Ataque", "VERSIONES", "VersionVulnerable",
    "ataques", "derivador", "suite", "versiones",
    "ErrorDeArboles", "SedeAusente", "ArbolDuplicado", "ArbolNoCubierto",
    "FixtureSinArbol", "AtaqueInerte", "ReproduccionInvalida",
]
