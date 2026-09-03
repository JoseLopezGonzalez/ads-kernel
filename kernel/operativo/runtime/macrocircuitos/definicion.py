#!/usr/bin/env python3
"""definicion — los CUATRO macrocircuitos, DERIVADOS de la tabla de `§18`.

    «SEDE CANÓNICA · la tabla de `§18`, “Los cuatro macrocircuitos, mapeados a los procesos
     de `b.16`”, fase a fase. Los bloques de `§8.1`–`§8.4` son su LECTURA narrativa: si
     alguna vez difieren, MANDA `§18`.»                                          `§8.0`

DECISIÓN · la definición vive aquí como DATO, y la tabla se contrasta desde la PRUEBA
    Alternativas: (a) leer la tabla de `11-ARQUITECTURA-INTEGRADA.md` en tiempo de
    ejecución; (b) escribirla aquí como dato derivado y comprobar desde la batería que
    sigue coincidiendo con la tabla.
    Se elige (b), y no por comodidad. `11-ARQ` vive en `docs/evolucion/` y **no viaja al
    proyecto instalado** —el propio `CONTRATO-RUNTIME-Y-DISPATCHER.md` lo dice—: un runtime
    que necesitara ese documento para arrancar no arrancaría en ningún producto gobernado.
    Con (b) el kernel es autosuficiente y la coincidencia se COMPRUEBA:
    `test_macrocircuitos.py` analiza la tabla de `§18` en el repositorio del kernel, deriva
    de ella macrocircuito, fase, proceso, propietario y gate, y **falla si el conjunto
    derivado y la tabla dejan de coincidir**. La sede sigue siendo `§18`; esto es su
    proyección comprobada, que es lo que un contrato derivado puede ser.

DECISIÓN · lo que aquí se escribe es el MAPEO, y el CONTRATO de la `FASE 0` está en `fase0.py`
    `§9.6` fija la jerarquía y no deja zona muerta: «`§18` manda sobre el MAPEO —qué fase,
    qué proceso de `b.16`, qué participantes y por qué vía, qué entra y qué sale—; `§9.6`
    manda sobre el CONTENIDO DEL CONTRATO `gate:sistema-conforme`». Este módulo instancia lo
    primero y no dice una palabra de lo segundo.

DECISIÓN · `SEG` en la `FASE 0` entra SIN VÍA y CONSERVA su bloqueo
    Es la primera divergencia real que `§9.6` resuelve a favor de su propia sede: «la vía de
    participación de una capacidad en el contrato compartido es contenido del contrato y no
    mapeo de tramos». Aquí, por tanto, `SEG` figura como PRESENCIA con forma `autoridad` y
    con su bloqueo declarado, y NO como participante.

DECISIÓN · `AUD` y `DEU` y `DEP` son PROCESOS y nunca aparecen como capacidades
    Las quince son `APR ARQ CON DIS DOM DSP ENC ENT INV PLT PRD SEG SIS USO VER`. Confundir
    el nombre de un proceso con el de una capacidad es el modo de fallo que `G1` corrigió, y
    `comprobar()` lo verifica fila a fila contra el censo del corpus.
"""
from __future__ import annotations

from ciclo.corpus import CAPACIDADES, Corpus
from ciclo.rutas import (
    PRESENCIA_AUTORIDAD,
    PRESENCIA_EJECUTOR,
    PRESENCIA_ENCUADRE,
    VIA_CONDICIONAL,
    VIA_ITEM_PROPIO,
    VIA_OBLIGATORIA,
    VIA_PROPIETARIA,
)

from .errores import DefinicionIncoherente, FaseDesconocida, MacrocircuitoDesconocido

FASE_0 = "FASE 0"
GATE_DE_FASE_0 = "gate:sistema-conforme"

# La FASE 0 es IGUAL EN LOS CUATRO (`§9.6`). Se escribe UNA vez y se referencia cuatro, que
# es exactamente lo que la regla 6 de `O17` exige: «el MISMO contrato y el MISMO mecanismo
# compartido», y «no se crean cuatro implementaciones divergentes».
FILA_DE_FASE_0 = {
    "fase": FASE_0,
    "nombre": "CERTIFICACIÓN ESTRUCTURAL",
    "proceso": "proceso:SIS",
    "propietario_global": "SIS",
    "propietario_via": VIA_PROPIETARIA,
    "participantes": [
        {"capacidad": "VER", "via": VIA_OBLIGATORIA,
         "motivo": "produce el DOSIER y no se apropia de la decisión"},
    ],
    "presencias": [
        {"forma": PRESENCIA_EJECUTOR, "quien": "PLT",
         "motivo": "la maquinaria técnica cuando el contrato vigente se la atribuya; no "
                   "por defecto y nunca en lugar de `SIS`"},
        {"forma": PRESENCIA_AUTORIDAD, "quien": "SIS",
         "motivo": "autoridad de la declaración Estructural, con el veto de `SEG`"},
        {"forma": PRESENCIA_AUTORIDAD, "quien": "SEG",
         "motivo": "SIN VÍA por `PN-13`, y CONSERVA su BLOQUEO, que es lo único que `O17` "
                   "le da; su veto no lo levanta ninguna de las otras tres ni el "
                   "propietario del macrocircuito"},
    ],
    "entrada": "el disparador del macrocircuito, con CERO mutaciones canónicas hechas, y "
               "el SUJETO de los seis identificadores de `§9.6` resuelto",
    "salida": "la declaración Estructural de ESTA ejecución, con su sujeto, su evidencia y "
              "su huella. Una por ejecución, y ninguna heredada",
    "gate": GATE_DE_FASE_0,
    "gate_declarado": "`gate:sistema-conforme` (`§9.6`) — el MISMO contrato para los "
                      "cuatro. Si falla, BLOQUEA antes de mutar estado",
    "estado_persistido": "celda `aspecto:certificacion/estructural` del sujeto, con su "
                         "vigencia y su condición de invalidación, en el SOPORTE DURABLE "
                         "DE LA FASE 0 —anterior al `estado/` del macrocircuito—, que la "
                         "primera fase que crea `estado/` INCORPORA sin reemitirla",
    "crea_estado": False,
}


def _fase0():
    """Una COPIA de la fila compartida. Cuatro referencias, una sola definición."""
    import copy
    return copy.deepcopy(FILA_DE_FASE_0)


MACROCIRCUITOS = {
    "N": {
        "id": "N",
        "nombre": "instalación en proyecto nuevo",
        "disparador": "el Owner quiere gobernar un producto que todavía no existe",
        "primera_fase_que_crea_estado": "INS-0–INS-5",
        "fases": [
            _fase0(),
            {
                "fase": "INS-0–INS-5",
                "nombre": "control repo, topología, especialización y baseline",
                "proceso": "proceso:SIS",
                "propietario_global": "SIS",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "CON", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "APR", "via": VIA_CONDICIONAL, "condicion": "C-APR",
                     "motivo": "vía 3 de `§18`"},
                    {"capacidad": "PRD", "via": VIA_ITEM_PROPIO, "proceso": "proceso:INV",
                     "motivo": "item `INV` enlazado de discovery"},
                    {"capacidad": "ARQ", "via": VIA_ITEM_PROPIO, "proceso": "proceso:INV",
                     "motivo": "item `INV` enlazado de discovery"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_EJECUTOR, "quien": "PLT",
                     "motivo": "MATERIALIZA las fuentes (`C7:82`)"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER",
                     "motivo": "aprueba el BASELINE de `INS-5`"},
                    {"forma": PRESENCIA_ENCUADRE, "quien": "ENC",
                     "motivo": "produce el encuadre ANTES de que haya ruta"},
                ],
                "sin_via": ["DOM", "DIS", "SEG"],
                "entrada": "decisión del Owner de instalar",
                "salida": "control repo, topología, especialización y adaptadores; el "
                          "BASELINE de producto, dominio y diseño de `INS-5`; y la "
                          "CLASIFICACIÓN DE DESCONOCIDOS CRÍTICOS",
                "gate": None,
                "gate_declarado": "`INS-4` certificación Operativa · `INS-5` BASELINE "
                                  "APROBADO POR EL OWNER",
                "estado_persistido": "`estado/` e `INI-001` desde `INS-0`, sobre el item "
                                     "`SIS-001`",
                "crea_estado": True,
            },
            {
                "fase": "INS-6–INS-7",
                "nombre": "punteros propagados y nivel Integrada",
                "proceso": "proceso:SIS",
                "propietario_global": "SIS",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "CON", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "ENT", "via": VIA_CONDICIONAL,
                     "condicion": "el cambio modifica el runtime: activación segura y reversible",
                     "motivo": "vía 3 de `§18`, «modifica el runtime»"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_EJECUTOR, "quien": "PLT",
                     "motivo": "MATERIALIZA (`C7:82`)"},
                    {"forma": PRESENCIA_EJECUTOR, "quien": "CON",
                     "motivo": "con custodia hace rama, commit, push y PR (`C7:83`–`C7:86`)"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "SEG",
                     "motivo": "puede bloquear el push (`C7:85`)"},
                    {"forma": PRESENCIA_EJECUTOR, "quien": "ENT",
                     "motivo": "merge y convergencia (`C7:88`–`C7:89`)"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER", "motivo": "autoridad"},
                ],
                "entrada": "especialización aprobada Y baseline de `INS-5` aprobado por el Owner",
                "salida": "punteros propagados y nivel Integrada",
                "gate": None,
                "gate_declarado": "`INS-7` = `O12`, con sus TRES condiciones y el productor "
                                  "de cada una",
                "estado_persistido": "evidencia + celdas de cobertura",
                "crea_estado": False,
            },
        ],
    },
    "A": {
        "id": "A",
        "nombre": "adopción de un producto con historia",
        "disparador": "el Owner quiere gobernar un producto con historia",
        "primera_fase_que_crea_estado": "A0–A1",
        "fases": [
            _fase0(),
            {
                "fase": "A0–A1",
                "nombre": "perímetro y topología",
                "proceso": "proceso:SIS",
                "propietario_global": "SIS",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "CON", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_EJECUTOR, "quien": "PLT",
                     "motivo": "MATERIALIZA (`C7:82`)"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER", "motivo": "autoridad"},
                ],
                "entrada": "el Owner quiere gobernar un producto con historia",
                "salida": "perímetro y topología",
                "gate": None,
                "gate_declarado": "modo no destructivo declarado",
                "estado_persistido": "iniciativa + `estado/`",
                "crea_estado": True,
            },
            {
                "fase": "A2–A7",
                "nombre": "inventario, baseline y producto reconstruido",
                "proceso": "proceso:AUD",
                "propietario_global": None,
                "propietario_via": VIA_PROPIETARIA,
                "propietario_derivado": "DERIVADO por item del encargo (`b.16`): la "
                                        "capacidad responsable de esa conclusión. NUNCA a mano",
                "items_enlazados": "uno por conclusión",
                "participantes": [
                    {"capacidad": "INV", "via": VIA_OBLIGATORIA,
                     "motivo": "única obligatoria; ejecuta y no responde de la conclusión"},
                    {"capacidad": "DOM", "via": VIA_CONDICIONAL, "condicion": "C-DOM",
                     "motivo": "vía 3 de `§18`"},
                    {"capacidad": "SEG", "via": VIA_CONDICIONAL, "condicion": "C-SEG",
                     "motivo": "vía 3 de `§18`"},
                    {"capacidad": "DIS", "via": VIA_CONDICIONAL, "condicion": "C-DIS",
                     "motivo": "vía 3 de `§18`"},
                    {"capacidad": "PRD", "via": VIA_CONDICIONAL,
                     "condicion": "la auditoría produce una decisión de producto",
                     "motivo": "vía 3 de `§18`"},
                    {"capacidad": "APR", "via": VIA_CONDICIONAL, "condicion": "C-APR",
                     "motivo": "vía 3 de `§18`"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_ENCUADRE, "quien": "ENC",
                     "motivo": "previo a la ruta"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER",
                     "motivo": "autoridad en `A3`"},
                ],
                "entrada": "acceso de lectura a las fuentes",
                "salida": "inventario, baseline, producto reconstruido y trabajo vivo",
                "gate": None,
                "gate_declarado": "`A3` baseline aprobado por el Owner",
                "estado_persistido": "capas por item, con procedencia",
                "crea_estado": False,
            },
            {
                "fase": "A8",
                "nombre": "retirada de copias organizativas y verdades paralelas",
                "proceso": "proceso:DEU",
                "propietario_global": "ARQ",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "CON", "via": VIA_OBLIGATORIA,
                     "motivo": "vía 2 por `cambio-construido`"},
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "DOM", "via": VIA_CONDICIONAL, "condicion": "C-DOM",
                     "metodo": "condiciones", "motivo": "vía 3 de `§18`"},
                    {"capacidad": "SEG", "via": VIA_CONDICIONAL, "condicion": "C-SEG",
                     "metodo": "condiciones", "motivo": "vía 3 de `§18`"},
                    {"capacidad": "ENT", "via": VIA_CONDICIONAL, "condicion": "C-ENT",
                     "motivo": "vía 3 de `§18`"},
                    {"capacidad": "USO", "via": VIA_CONDICIONAL, "condicion": "C-USO",
                     "motivo": "vía 3 de `§18`"},
                    {"capacidad": "APR", "via": VIA_CONDICIONAL, "condicion": "C-APR",
                     "motivo": "vía 3 de `§18`"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_EJECUTOR, "quien": "PLT",
                     "motivo": "MATERIALIZA (`C7:82`)"},
                    {"forma": PRESENCIA_EJECUTOR, "quien": "CON",
                     "motivo": "con custodia hace rama, commit, push y PR"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "SEG",
                     "motivo": "puede bloquear el push"},
                    {"forma": PRESENCIA_EJECUTOR, "quien": "ENT",
                     "motivo": "merge y convergencia"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER",
                     "motivo": "autoridad POR FUENTE"},
                ],
                "entrada": "autorización de retirada",
                "salida": "copias organizativas y verdades paralelas retiradas",
                "gate": None,
                "gate_declarado": "`A8` autorizado por el Owner",
                "estado_persistido": "source changes por fuente",
                "crea_estado": False,
            },
            {
                "fase": "A9–A10",
                "nombre": "limpieza cerrada y nivel Integrada",
                "proceso": "proceso:SIS",
                "propietario_global": "SIS",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "CON", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_EJECUTOR, "quien": "PLT",
                     "motivo": "MATERIALIZA (`C7:82`)"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER", "motivo": "autoridad"},
                ],
                "sin_via": ["SEG"],
                "entrada": "limpieza cerrada",
                "salida": "nivel Integrada",
                "gate": None,
                "gate_declarado": "`A10` = `O12`",
                "estado_persistido": "celdas de certificación",
                "crea_estado": False,
            },
        ],
    },
    "M": {
        "id": "M",
        "nombre": "migración desde una versión anterior",
        "disparador": "existe una instalación de una versión anterior",
        "primera_fase_que_crea_estado": "M0–M5",
        "fases": [
            _fase0(),
            {
                "fase": "M0–M5",
                "nombre": "estado migrado, verificado y certificado",
                "proceso": "proceso:SIS",
                "propietario_global": "SIS",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "CON", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "ENT", "via": VIA_CONDICIONAL,
                     "condicion": "el cambio modifica el runtime: activación segura y reversible",
                     "motivo": "vía 3 de `§18`"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_EJECUTOR, "quien": "PLT",
                     "motivo": "MATERIALIZA (`C7:82`)"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER", "motivo": "autoridad"},
                ],
                "entrada": "existe una instalación de una versión anterior",
                "salida": "estado migrado, verificado y certificado",
                "gate": None,
                "gate_declarado": "`M3` equivalencia · `M5` Integrada",
                "estado_persistido": "`estado/` migrado + evento `migracion`",
                "crea_estado": True,
            },
            {
                "fase": "M6–M7",
                "nombre": "heredado retirado y verificado",
                "proceso": "proceso:DEU",
                "propietario_global": "ARQ",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "CON", "via": VIA_OBLIGATORIA,
                     "motivo": "vía 2 por `cambio-construido`"},
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA,
                     "motivo": "vía 2 de `§18`, y verifica `M7`"},
                    {"capacidad": "DOM", "via": VIA_CONDICIONAL, "condicion": "C-DOM",
                     "metodo": "condiciones", "motivo": "vía 3 de `§18`"},
                    {"capacidad": "SEG", "via": VIA_CONDICIONAL, "condicion": "C-SEG",
                     "metodo": "condiciones", "motivo": "vía 3 de `§18`"},
                    {"capacidad": "ENT", "via": VIA_CONDICIONAL, "condicion": "C-ENT",
                     "motivo": "vía 3 de `§18`"},
                    {"capacidad": "USO", "via": VIA_CONDICIONAL, "condicion": "C-USO",
                     "motivo": "vía 3 de `§18`"},
                    {"capacidad": "APR", "via": VIA_CONDICIONAL, "condicion": "C-APR",
                     "motivo": "vía 3 de `§18`"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_EJECUTOR, "quien": "PLT",
                     "motivo": "MATERIALIZA (`C7:82`)"},
                    {"forma": PRESENCIA_EJECUTOR, "quien": "CON",
                     "motivo": "con custodia hace rama, commit, push y PR"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "SEG",
                     "motivo": "puede bloquear el push"},
                    {"forma": PRESENCIA_EJECUTOR, "quien": "ENT",
                     "motivo": "merge y convergencia"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER",
                     "motivo": "autoridad POR FUENTE"},
                ],
                "entrada": "`M5` certificado y autorización POR FUENTE",
                "salida": "heredado retirado y verificado",
                "gate": None,
                "gate_declarado": "`M6` autorizado · `M7` verificado",
                "estado_persistido": "source changes + `INTEGRACIÓN PARCIAL`",
                "crea_estado": False,
            },
        ],
    },
    "U": {
        "id": "U",
        "nombre": "actualización del propio ADS",
        "disparador": "hay una versión nueva de ADS",
        "primera_fase_que_crea_estado": "U0–U4",
        "bloqueo": "ninguna otra actualización arranca mientras ésta corre (`§8.4`)",
        "fases": [
            _fase0(),
            {
                "fase": "U0–U4",
                "nombre": "compatibilidad decidida y migración aplicada",
                "proceso": "proceso:SIS",
                "propietario_global": "SIS",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "CON", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "ENT", "via": VIA_CONDICIONAL,
                     "condicion": "el cambio modifica el runtime: activación segura y reversible",
                     "motivo": "vía 3 de `§18`"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_EJECUTOR, "quien": "PLT",
                     "motivo": "MATERIALIZA (`C7:82`)"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER",
                     "motivo": "autoridad en `U3`"},
                ],
                "entrada": "hay una versión nueva de ADS",
                "salida": "compatibilidad decidida y migración aplicada",
                "gate": None,
                "gate_declarado": "`U3` punto de no retorno",
                "estado_persistido": "instantánea de `U3` + progreso por pasos",
                "crea_estado": True,
            },
            {
                "fase": "U5a",
                "nombre": "proyecciones del control repo recompiladas",
                "proceso": "proceso:SIS",
                "propietario_global": "SIS",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "CON", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_EJECUTOR, "quien": "SIS",
                     "motivo": "ejecutor el runtime del control repo"},
                ],
                "entrada": "migración aplicada",
                "salida": "proyecciones del control repo recompiladas",
                "gate": None,
                "gate_declarado": "ninguno propio: cae en `U6`",
                "estado_persistido": "huella de proyección (`§6.3`)",
                "crea_estado": False,
            },
            {
                "fase": "U5b",
                "nombre": "punteros propagados a cada fuente",
                "proceso": "proceso:DEP",
                "propietario_global": "PLT",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "SEG", "via": VIA_OBLIGATORIA,
                     "motivo": "vía 2 por `condiciones-de-seguridad`, ANTES de construir; "
                               "`G28` la hace irretirable"},
                    {"capacidad": "CON", "via": VIA_OBLIGATORIA,
                     "motivo": "vía 2 por `cambio-construido`"},
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                    {"capacidad": "DOM", "via": VIA_CONDICIONAL, "condicion": "C-DOM",
                     "metodo": "condiciones", "motivo": "vía 3 de `§18`"},
                    {"capacidad": "ARQ", "via": VIA_CONDICIONAL,
                     "condicion": "el cambio de versión altera contratos",
                     "motivo": "vía 3 de `§18`"},
                    {"capacidad": "ENT", "via": VIA_CONDICIONAL, "condicion": "C-ENT",
                     "motivo": "vía 3 de `§18`"},
                ],
                "presencias": [
                    {"forma": PRESENCIA_EJECUTOR, "quien": "PLT",
                     "motivo": "MATERIALIZA (`C7:82`) y participa además por la vía 1"},
                    {"forma": PRESENCIA_EJECUTOR, "quien": "CON",
                     "motivo": "con custodia hace rama, commit, push y PR"},
                    {"forma": PRESENCIA_EJECUTOR, "quien": "ENT",
                     "motivo": "merge y convergencia"},
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER",
                     "motivo": "autoridad si hay retirada"},
                ],
                "entrada": "`U5a` cerrado",
                "salida": "punteros propagados a cada fuente",
                "gate": None,
                "gate_declarado": "gate por fuente, con Integration Set si hay más de una",
                "estado_persistido": "`INTEGRACIÓN PARCIAL` por fuente",
                "crea_estado": False,
            },
            {
                "fase": "U6",
                "nombre": "ADS actualizado y recertificado",
                "proceso": "proceso:SIS",
                "propietario_global": "SIS",
                "propietario_via": VIA_PROPIETARIA,
                "participantes": [
                    {"capacidad": "VER", "via": VIA_OBLIGATORIA, "motivo": "vía 2 de `§18`"},
                ],
                # HALLAZGO, declarado en vez de callado. La columna de participantes de
                # `§18` para `U6` nombra sólo a `VER`, y el proceso que la MISMA fila mapea
                # —`proceso:SIS`— declara `cambio-construido` entre sus `obligatorias`, con
                # `CON` como capacidad productora. `§8.0` dice de la vía 2 que «entra
                # SIEMPRE, y su obligación tiene que quedar SATISFECHA para cerrar», así que
                # `CON` entra en `U6` la nombre `§18` o no: no es una elección de F6, es lo
                # que `b.16` obliga. No se toca `§18` —es norma y no es de esta zona— y no se
                # esconde la diferencia: se declara aquí, y `test_macrocircuitos.py` la
                # comprueba fila a fila para que deje de ser cierta el día que `§18` la
                # recoja.
                "participantes_obligatorios_derivados": ["CON"],
                "presencias": [
                    {"forma": PRESENCIA_AUTORIDAD, "quien": "OWNER",
                     "motivo": "autoridad si la revalidación baja el nivel"},
                ],
                "entrada": "`U5b` convergido",
                "salida": "ADS actualizado y recertificado",
                "gate": None,
                "gate_declarado": "revalidación del nivel VIGENTE, no `O12`; bajar de nivel "
                                  "es un fallo, no un resultado",
                "estado_persistido": "celdas de certificación",
                "crea_estado": False,
            },
        ],
    },
}

IDENTIFICADORES = tuple(sorted(MACROCIRCUITOS))

# La SECUENCIA DE PROCESOS que `§8.0` escribe para el FRENO 3 de `a.7`. Se DERIVA de las
# fases y se compara con lo escrito allí; no se copia.
SECUENCIA_DECLARADA_EN_8_0 = {
    "N": ("SIS", "SIS", "SIS"),
    "A": ("SIS", "SIS", "AUD", "DEU", "SIS"),
    "M": ("SIS", "SIS", "DEU"),
    "U": ("SIS", "SIS", "SIS", "DEP", "SIS"),
}


def macrocircuito(identificador):
    if identificador not in MACROCIRCUITOS:
        raise MacrocircuitoDesconocido(
            "los CUATRO son " + ", ".join(IDENTIFICADORES) + "; se pidió "
            + repr(identificador),
        )
    return MACROCIRCUITOS[identificador]


def fase(identificador, nombre_de_fase):
    definido = macrocircuito(identificador)
    for candidata in definido["fases"]:
        if candidata["fase"] == nombre_de_fase:
            return candidata
    raise FaseDesconocida(
        "`" + identificador + "` no declara la fase " + repr(nombre_de_fase) + "; declara: "
        + ", ".join(f["fase"] for f in definido["fases"]),
    )


def capacidades_de_la_fase(una):
    """Las capacidades que la fase declara: las de `§18` más las que `b.16` obliga.

    La segunda lista existe por una diferencia REAL y está documentada en la fila que la
    necesita: `§18` puede no nombrar en su columna de participantes a una capacidad que el
    proceso mapeado declara OBLIGATORIA, y una obligatoria «entra SIEMPRE» (`§8.0`). El
    conjunto que hay que comparar contra la ruta compuesta es la unión, y por eso se deriva
    aquí en vez de escribirse en cada prueba.
    """
    declaradas = {p["capacidad"] for p in una["participantes"]}
    declaradas.update(una.get("participantes_obligatorios_derivados") or [])
    if una.get("propietario_global"):
        declaradas.add(una["propietario_global"])
    return tuple(sorted(declaradas))


def secuencia_de_procesos(identificador):
    """La racha de `a.7` FRENO 3, DERIVADA de las fases y con la `FASE 0` DENTRO."""
    return tuple(
        f["proceso"].split(":", 1)[-1] for f in macrocircuito(identificador)["fases"]
    )


def comprobar(corpus=None):
    """El conjunto derivado casa con `b.16`, con las quince capacidades y con `§8.0`."""
    corpus = corpus or Corpus()
    procesos = set(corpus.procesos())
    gates = set(corpus.gates())
    for identificador in IDENTIFICADORES:
        definido = MACROCIRCUITOS[identificador]
        if not definido["fases"] or definido["fases"][0]["fase"] != FASE_0:
            raise DefinicionIncoherente(
                "`" + identificador + "` no empieza por su `FASE 0`, y `§9.6` la exige "
                "ANTES de cualquier mutación canónica",
                macrocircuito=identificador,
            )
        for una in definido["fases"]:
            if una["proceso"] not in procesos:
                raise DefinicionIncoherente(
                    "la fase `" + una["fase"] + "` de `" + identificador + "` mapea a `"
                    + una["proceso"] + "`, que `b.16` no declara",
                    macrocircuito=identificador, fase=una["fase"],
                )
            propietario = una.get("propietario_global")
            if propietario is not None and propietario not in CAPACIDADES:
                raise DefinicionIncoherente(
                    "la fase `" + una["fase"] + "` de `" + identificador + "` declara el "
                    "propietario global `" + str(propietario) + "`, que no es una de las "
                    "quince capacidades; `DEU`, `DEP` y `AUD` son PROCESOS",
                    macrocircuito=identificador, fase=una["fase"],
                )
            if propietario is None and not una.get("propietario_derivado"):
                raise DefinicionIncoherente(
                    "la fase `" + una["fase"] + "` de `" + identificador + "` no fija "
                    "propietario global ni declara cómo se DERIVA",
                    macrocircuito=identificador, fase=una["fase"],
                )
            for participante in una["participantes"]:
                if participante["capacidad"] not in CAPACIDADES:
                    raise DefinicionIncoherente(
                        "participante que no es capacidad: "
                        + str(participante["capacidad"]),
                        macrocircuito=identificador, fase=una["fase"],
                    )
                if participante["capacidad"] == "ENC":
                    raise DefinicionIncoherente(
                        "`ENC` NO participa en ninguna ruta (`§8.0`)",
                        macrocircuito=identificador, fase=una["fase"],
                    )
                if participante["via"] == VIA_CONDICIONAL and not participante.get("condicion"):
                    raise DefinicionIncoherente(
                        "la vía 3 exige condición nombrada: "
                        + str(participante["capacidad"]),
                        macrocircuito=identificador, fase=una["fase"],
                    )
            if una.get("gate") and una["gate"] not in gates:
                raise DefinicionIncoherente(
                    "la fase `" + una["fase"] + "` invoca `" + str(una["gate"])
                    + "`, que el corpus no declara",
                    macrocircuito=identificador, fase=una["fase"],
                )
        derivada = secuencia_de_procesos(identificador)
        if derivada != SECUENCIA_DECLARADA_EN_8_0[identificador]:
            raise DefinicionIncoherente(
                "la secuencia de procesos derivada de las fases de `" + identificador
                + "` es " + " ".join(derivada) + " y `§8.0` escribe "
                + " ".join(SECUENCIA_DECLARADA_EN_8_0[identificador]),
                macrocircuito=identificador,
            )
        # La `FASE 0` es LA MISMA en los cuatro: mismo proceso, mismo propietario, mismo
        # gate y misma salida. Es la regla 6 de `O17`, comprobada y no prometida.
        suya = definido["fases"][0]
        for clave in ("proceso", "propietario_global", "gate", "salida", "entrada"):
            if suya[clave] != FILA_DE_FASE_0[clave]:
                raise DefinicionIncoherente(
                    "la `FASE 0` de `" + identificador + "` difiere de la compartida en `"
                    + clave + "`; `O17` regla 6 exige el MISMO contrato para los cuatro",
                    macrocircuito=identificador,
                )
    return IDENTIFICADORES
