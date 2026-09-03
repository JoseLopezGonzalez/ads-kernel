#!/usr/bin/env python3
"""rutas — LA COMPOSICIÓN DE RUTA de `§8.0`: las CUATRO vías y el GATE DE COMPOSICIÓN.

    «ninguna fase de ningún macrocircuito abre hasta que, para CADA capacidad que la fase
     declara, consta UNA de las cuatro vías, con su proceso y —si es la 3— su condición
     nombrada»                                                            `§8.0`

Las CUATRO vías, y no hay una quinta:

    1 PROPIETARIA GLOBAL     la capacidad cuya capa DEFINE el resultado del item. La fija
                             `b.16`; en `AUD` y `DIR` se DERIVA del encargo
    2 OBLIGATORIA            figura en las `obligatorias` del proceso. Entra SIEMPRE
    3 CONDICIONAL            figura en las `condicionales` CON SU CONDICIÓN comprobable
    4 ITEM PROPIO ENLAZADO   no cabe en el proceso de la fase: entra con SU PROPIO ITEM,
                             bajo el proceso que sí la declara, enlazado al item líder

Y las TRES formas de estar presente que NO son participar —`EJECUTOR`, `AUTORIDAD`,
`ENCUADRE`—, que se registran en `presencias` y **nunca** en `participantes`. Confundirlas
con la vía 3 es lo que produjo la lista de «participantes sin vehículo» que `§8.0` corrige.

DECISIÓN · la vía 3 se activa por una CONDICIÓN DECLARADA VERDADERA, no por adivinarla
    Alternativas: (a) que el ciclo evalúe la condición leyendo el estado o el texto; (b)
    que quien compone declare qué condiciones del vocabulario de `b.16` —`C-DIS`, `C-ARQ`,
    `C-DOM`, `C-SEG`, `C-ENT`, `C-USO`, `C-APR`— o qué condiciones propias son verdaderas,
    y que el ciclo las case CONTRA LAS QUE EL PROCESO DECLARA.
    Se elige (b). (a) exige que el runtime sepa juzgar «el cambio modifica el runtime», que
    es contenido y por tanto materia de una capacidad, no de DSP: `gate:despacho-coherente`
    tiene una comprobación entera —`sin-contenido`— para impedir exactamente eso. Con (b)
    DSP transporta y registra, que es lo que `a.5` le deja hacer, y la traza dice quién
    declaró la condición.

DECISIÓN · lo NO ACTIVADO deja MOTIVO, y el motivo es un dato, no una frase libre
    `a.6` y `gate:despacho-coherente` («toda ruta declara activadas y NO activadas, cada
    una con motivo escrito»). El motivo se compone de la condición que no consta verdadera,
    citada literalmente desde el proceso. Una ruta sin la lista de no activadas no pasa su
    propio gate, y por eso la lista se construye siempre, incluso cuando está vacía.

DECISIÓN · `composicion-incompleta` NO ABRE LA FASE, y se levanta ANTES de escribir nada
    `§8.0`: «la fase NO abre, DSP para y escala nombrando la capacidad y la fase». Componer
    es una función PURA: no toca el estado. Quien escribe la ruta es `planificacion.py`, y
    sólo recibe rutas que ya pasaron el gate. Así un fallo de composición no puede dejar
    media ruta publicada, que es la forma en que un gate se convierte en decorativo.
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto

from .corpus import CAPACIDADES, Corpus
from .errores import (
    ComposicionIncompleta,
    PropietarioNoDerivable,
    ViaInvalida,
)
from .procesos import capacidad_de, comprobar_condicion, metodo_de, obligaciones_de

DOMINIO = "rutas"
ESQUEMA = "ads.estado/1"

VIA_PROPIETARIA = 1
VIA_OBLIGATORIA = 2
VIA_CONDICIONAL = 3
VIA_ITEM_PROPIO = 4
VIAS = (VIA_PROPIETARIA, VIA_OBLIGATORIA, VIA_CONDICIONAL, VIA_ITEM_PROPIO)

NOMBRE_DE_VIA = {
    VIA_PROPIETARIA: "propietaria-global",
    VIA_OBLIGATORIA: "obligatoria",
    VIA_CONDICIONAL: "condicional",
    VIA_ITEM_PROPIO: "item-propio-enlazado",
}

# Las TRES formas de estar presente que NO son participar (`§8.0`, corregido por `I-20`).
PRESENCIA_EJECUTOR = "ejecutor"
PRESENCIA_AUTORIDAD = "autoridad"
PRESENCIA_ENCUADRE = "encuadre"
PRESENCIAS = (PRESENCIA_EJECUTOR, PRESENCIA_AUTORIDAD, PRESENCIA_ENCUADRE)

# `ENC` produce el encuadre ANTES de que haya ruta y `b.16` no la declara en ningún
# proceso: encuadrar no es depositar capa, luego `ENC` NUNCA es participante.
NUNCA_PARTICIPA = ("ENC",)

# El propietario global de `proceso:DEF` no es una capacidad a secas: `b.16` lo escribe como
# una derivación con UNA condición del vocabulario cerrado. Se declara aquí como DATO —qué
# condición y qué dos capacidades— porque leerlo del texto sería adivinar prosa, y una
# prueba comprueba que las dos capacidades siguen nombradas en el corpus.
PROPIETARIO_POR_CONDICION = {
    "proceso:DEF": {"condicion": "C-ARQ", "si": "ARQ", "si_no": "CON"},
}

# Procesos cuyo propietario `b.16` NO fija y PROHÍBE asignar a mano: lo DERIVA el encargo.
PROPIETARIO_DEL_ENCARGO = ("proceso:AUD", "proceso:DIR")


# ===========================================================================
#  propietario global
# ===========================================================================
def propietario_global(proceso, *, condiciones_verdaderas=(), propietario_declarado=None):
    """La capacidad de la VÍA 1, y de dónde sale. Nunca se elige a ojo."""
    identificador = proceso["id"]
    declarado_en_b16 = str(proceso.get("propietario_global") or "").strip()
    if declarado_en_b16 in CAPACIDADES:
        return {"capacidad": declarado_en_b16, "origen": "fijado por `b.16`",
                "condicion": None}
    regla = PROPIETARIO_POR_CONDICION.get(identificador)
    if regla is not None:
        activa = regla["condicion"] in tuple(condiciones_verdaderas)
        return {
            "capacidad": regla["si"] if activa else regla["si_no"],
            "origen": "derivado por la condición `" + regla["condicion"] + "` de `b.16`",
            "condicion": regla["condicion"],
        }
    if identificador in PROPIETARIO_DEL_ENCARGO:
        if propietario_declarado not in CAPACIDADES:
            raise PropietarioNoDerivable(
                "`" + identificador + "` DERIVA su propietario global del encargo y `b.16` "
                "prohíbe asignarlo a mano; el encargo debe declarar cuál de las quince "
                "capacidades responde de la conclusión",
                proceso=identificador,
                declarado=str(propietario_declarado),
            )
        return {"capacidad": propietario_declarado,
                "origen": "DERIVADO del encargo (`01-PROCESOS.md`)", "condicion": None}
    raise PropietarioNoDerivable(
        "el proceso `" + identificador + "` declara un propietario global que no es una de "
        "las quince capacidades y para el que no hay regla de derivación declarada",
        proceso=identificador,
    )


# ===========================================================================
#  composición
# ===========================================================================
def componer(encuadre, *, corpus=None, fase="unica", condiciones_verdaderas=(),
             productores_declarados=None, items_enlazados=(), presencias=(),
             propietario_declarado=None, capacidades_de_la_fase=None):
    """La ruta de una fase: participantes con su vía, no activadas con motivo, y presencias.

    Función PURA: lee el corpus y devuelve un objeto. No escribe en el estado durable, y no
    puede: `§8.0` exige que la fase NO ABRA si la composición está incompleta, y una
    composición que escribiera mientras compone ya habría abierto algo.
    """
    corpus = corpus or Corpus()
    proceso = corpus.proceso(encuadre["proceso"])
    condiciones = tuple(sorted({str(c) for c in condiciones_verdaderas}))
    productores = dict(productores_declarados or {})

    participantes, no_activadas = [], []

    # --- VÍA 1 ---------------------------------------------------------------
    duenio = propietario_global(
        proceso, condiciones_verdaderas=condiciones,
        propietario_declarado=propietario_declarado,
    )
    participantes.append(_participante(
        corpus, duenio["capacidad"], VIA_PROPIETARIA, proceso["id"],
        motivo=duenio["origen"], condicion=duenio["condicion"],
        salida="la capa que DEFINE el resultado del item: " + str(proceso.get("intencion", "")).strip(),
        criterio=str(proceso.get("criterio_de_cierre", "")).strip(),
    ))

    # --- VÍA 2 ---------------------------------------------------------------
    for obligacion in obligaciones_de(proceso):
        productora = obligacion["capacidad_productora"]
        capacidad = capacidad_de(productora)
        if capacidad not in CAPACIDADES:
            # `b.16` escribe aquí, en tres sitios, algo que NO es una capacidad: `OWNER` en
            # `proceso:DIR`, y dos derivaciones redactadas. `OWNER` es AUTORIDAD y no
            # participa; una derivación exige que el encargo diga qué capacidad la cumple,
            # y si no lo dice la fase NO ABRE.
            if productora.strip().upper() == "OWNER":
                continue
            declarada = productores.get(obligacion["id"])
            if declarada not in CAPACIDADES:
                raise ComposicionIncompleta(
                    "la obligación `" + obligacion["id"] + "` de `" + proceso["id"]
                    + "` declara una capacidad productora DERIVADA y el encargo no dice "
                    "cuál es; la fase NO ABRE",
                    capacidad=productora, fase=fase, ruta=proceso["id"],
                    obligacion=obligacion["id"],
                )
            capacidad = declarada
        participantes.append(_participante(
            corpus, capacidad, VIA_OBLIGATORIA, proceso["id"],
            motivo="obligación `" + obligacion["id"] + "` de `" + proceso["id"] + "`",
            condicion=None, salida=obligacion["capa_exigida"],
            criterio=obligacion["criterio_de_satisfaccion"],
            obligacion=obligacion["id"], metodo=metodo_de(productora),
        ))

    # --- VÍA 3 ---------------------------------------------------------------
    for condicional in proceso.get("condicionales") or []:
        participante = condicional["capacidad"]
        capacidad = capacidad_de(participante)
        condicion = comprobar_condicion(condicional["condicion"], capacidad=participante)
        if condicion in condiciones:
            participantes.append(_participante(
                corpus, capacidad, VIA_CONDICIONAL, proceso["id"],
                motivo="la condición `" + condicion + "` consta verdadera",
                condicion=condicion, salida=None, criterio=None,
                metodo=metodo_de(participante),
            ))
        else:
            no_activadas.append({
                "capacidad": capacidad,
                "participante": participante,
                "via": VIA_CONDICIONAL,
                "condicion": condicion,
                "motivo": "la condición `" + condicion + "` no consta verdadera en este "
                          "encuadre; `a.6` exige que lo no activado deje motivo",
            })

    # --- VÍA 4 ---------------------------------------------------------------
    for enlazado in items_enlazados:
        capacidad = capacidad_de(enlazado.get("capacidad", ""))
        if capacidad not in CAPACIDADES:
            raise ViaInvalida(
                "un item propio enlazado nombra `" + str(enlazado.get("capacidad"))
                + "`, que no es una de las quince capacidades",
            )
        if not enlazado.get("proceso") or not enlazado.get("item_lider"):
            raise ViaInvalida(
                "la vía 4 exige el PROCESO bajo el que entra la capacidad y el ITEM LÍDER "
                "al que se enlaza; sin el enlace no es una vía, es un item suelto",
                capacidad=capacidad,
            )
        corpus.proceso(enlazado["proceso"])
        participantes.append(_participante(
            corpus, capacidad, VIA_ITEM_PROPIO, enlazado["proceso"],
            motivo="no cabe en `" + proceso["id"] + "`; entra con su propio item bajo `"
                   + enlazado["proceso"] + "`",
            condicion=None, salida=enlazado.get("salida"), criterio=enlazado.get("criterio"),
            item_lider=enlazado["item_lider"],
        ))

    # --- las TRES formas de estar presente que NO son participar --------------
    presencias_normalizadas = _normalizar_presencias(presencias)

    ruta = {
        "esquema": ESQUEMA,
        "encuadre": encuadre["id"],
        "fase": str(fase),
        "proceso": proceso["id"],
        "propietario_global": duenio["capacidad"],
        "origen_del_propietario": duenio["origen"],
        "participantes": sorted(participantes, key=lambda p: (p["via"], p["capacidad"])),
        "no_activadas": sorted(no_activadas, key=lambda p: p["capacidad"]),
        "presencias": presencias_normalizadas,
        "condiciones_verdaderas": list(condiciones),
        "obligaciones": obligaciones_de(proceso),
        "huella_del_corpus": corpus.huella(),
    }
    exigir_composicion_completa(ruta, capacidades_de_la_fase or ())
    ruta["id"] = identificador(ruta)
    return ruta


def _participante(corpus, capacidad, via, proceso, *, motivo, condicion, salida, criterio,
                  obligacion=None, metodo=None, item_lider=None):
    if capacidad not in CAPACIDADES:
        raise ViaInvalida(
            "`" + str(capacidad) + "` no es una de las quince capacidades", capacidad=str(capacidad),
        )
    if capacidad in NUNCA_PARTICIPA:
        raise ViaInvalida(
            "`" + capacidad + "` NO participa en ninguna ruta: produce el encuadre ANTES de "
            "que haya ruta, y encuadrar no es depositar capa (`§8.0`)",
            capacidad=capacidad,
        )
    if via not in VIAS:
        raise ViaInvalida("vía fuera de las CUATRO de `§8.0`: " + repr(via))
    ficha = corpus.capacidad(capacidad)
    if salida is None:
        # `§8.0`: «Una capacidad sin salida declarada es una capacidad que no tenía por qué
        # estar». La salida por defecto NO se inventa: se toma de la ficha de la capacidad,
        # que declara qué deposita. Es derivación, no relleno.
        salida = "; ".join(str(s) for s in (ficha.get("salida") or []))
    if criterio is None:
        criterio = str(ficha.get("capa_de_valor") or "").strip()
    if not str(salida).strip():
        raise ViaInvalida(
            "la capacidad `" + capacidad + "` entra en la ruta sin salida declarada",
            capacidad=capacidad,
        )
    entrada = {
        "capacidad": capacidad,
        "via": via,
        "via_nombre": NOMBRE_DE_VIA[via],
        "proceso": proceso,
        "motivo": motivo,
        "condicion": condicion,
        "salida": str(salida).strip(),
        "criterio_de_satisfaccion": str(criterio).strip(),
        "gate": ficha.get("gate"),
        "metodo": metodo,
        "obligacion": obligacion,
        "item_lider": item_lider,
    }
    return entrada


def _normalizar_presencias(presencias):
    salida = []
    for presencia in presencias:
        forma = presencia.get("forma")
        if forma not in PRESENCIAS:
            raise ViaInvalida(
                "forma de presencia fuera de las TRES de `§8.0`: " + repr(forma)
                + "; válidas: " + ", ".join(PRESENCIAS),
            )
        quien = str(presencia.get("quien") or "").strip()
        if not quien:
            raise ViaInvalida("una presencia sin `quien` no dice nada")
        salida.append({
            "forma": forma,
            "quien": quien,
            "motivo": str(presencia.get("motivo") or "").strip(),
            "participa": False,
        })
    return sorted(salida, key=lambda p: (p["forma"], p["quien"]))


# ===========================================================================
#  GATE DE COMPOSICIÓN
# ===========================================================================
def exigir_composicion_completa(ruta, capacidades_de_la_fase):
    """Para CADA capacidad que la fase declara, consta UNA de las cuatro vías (`§8.0`)."""
    por_capacidad = {}
    for participante in ruta["participantes"]:
        por_capacidad.setdefault(participante["capacidad"], []).append(participante)
    for capacidad in sorted({capacidad_de(c) for c in capacidades_de_la_fase}):
        if capacidad in NUNCA_PARTICIPA:
            raise ComposicionIncompleta(
                "la fase declara `" + capacidad + "` como capacidad de la ruta, y `§8.0` "
                "fija que no participa en ninguna: encuadrar no es depositar capa",
                capacidad=capacidad, fase=ruta["fase"],
            )
        if capacidad not in por_capacidad:
            raise ComposicionIncompleta(
                "la fase `" + str(ruta["fase"]) + "` declara la capacidad `" + capacidad
                + "` y NO consta ninguna de las cuatro vías para ella; la fase NO ABRE y "
                "DSP escala. No se inventa un handoff para tapar una capacidad sin vía, y "
                "no se ensancha `b.16` por conveniencia",
                capacidad=capacidad, fase=ruta["fase"], proceso=ruta["proceso"],
            )
    for participante in ruta["participantes"]:
        if participante["via"] == VIA_CONDICIONAL and not participante["condicion"]:
            raise ComposicionIncompleta(
                "la capacidad `" + participante["capacidad"] + "` entra por la vía 3 sin "
                "condición nombrada",
                capacidad=participante["capacidad"], fase=ruta["fase"],
            )
        if participante["via"] == VIA_ITEM_PROPIO and not participante["item_lider"]:
            raise ComposicionIncompleta(
                "la capacidad `" + participante["capacidad"] + "` entra por la vía 4 sin "
                "enlace a su item líder",
                capacidad=participante["capacidad"], fase=ruta["fase"],
            )
    return ruta


def traza(ruta):
    """Lo que `gate:despacho-coherente` exige ver: activadas y NO activadas, con motivo."""
    return {
        "activadas": [
            {"capacidad": p["capacidad"], "via": p["via"], "motivo": p["motivo"]}
            for p in ruta["participantes"]
        ],
        "no_activadas": [
            {"capacidad": p["capacidad"], "motivo": p["motivo"]}
            for p in ruta["no_activadas"]
        ],
        "presencias_que_no_participan": list(ruta["presencias"]),
        "propietario_global": ruta["propietario_global"],
    }


def identificador(ruta):
    """`rt-<16 hex>` derivado del CONTENIDO. Componer dos veces lo mismo da la MISMA ruta."""
    sin_id = {clave: valor for clave, valor in ruta.items() if clave != "id"}
    digest = cid_de_objeto(sin_id)
    return "rt-" + digest.split(":", 1)[-1][:16]


def ruta_de(identificador_de_ruta):
    return DOMINIO + "/" + identificador_de_ruta + ".json"
