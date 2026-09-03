#!/usr/bin/env python3
"""equipos — la MATERIALIZACIÓN de `C4`, con sus siete pasos y sus siete prohibiciones.

`C4` es un algoritmo, y está escrito como tal: leer el paquete · elegir composición ·
expandir roles · asignar agentes · aplicar combinación · comprobar límites · escribir el
equipo. Este módulo lo ejecuta sobre las composiciones REALES del corpus.

DECISIÓN · se derivan CAPACIDADES, y un MÉTODO nunca se usa como capacidad
    `C1` separa equipo, rol, agente y método. El corpus escribe participantes condicionales
    como `DOM:condiciones`, `ARQ:diagnostico`, `DIS/Reconstruccion` o `CON:experimental`:
    la parte de la izquierda es una CAPACIDAD y la de la derecha un MÉTODO del directorio
    `capacidades/<CAP>/metodos/`. Materializar `DOM:condiciones` como si fuera una
    capacidad produciría un equipo de una capacidad inexistente; ignorar el método perdería
    QUÉ se le pide. `procesos.capacidad_de` y `procesos.metodo_de` los separan, este módulo
    materializa la capacidad y ANOTA el método, y `test_ciclo.py` lo prueba por los dos
    lados: ningún nombre de método entra jamás como capacidad, y el método declarado
    sobrevive en el equipo escrito.

DECISIÓN · la composición se elige por CONDICIÓN DECLARADA, en el ORDEN ESCRITO
    `C4` paso 2 es literal: «recorrer los bloques `ads:composicion` de esa capacidad EN EL
    ORDEN EN QUE ESTÁN ESCRITOS y quedarse con el PRIMERO cuya `condicion` sea verdadera.
    El orden es parte del contrato, no casual». Quién declara verdadera una condición no es
    DSP —sería decidir contenido, y `gate:despacho-coherente` lo prohíbe con
    `sin-contenido`—: se declara al materializar, por el identificador de la composición, y
    el equipo escrito registra cuál la eligió. Si ninguna es verdadera, `C4` manda escalar
    a `SIS`, y eso es `ComposicionDeEquipoAusente`, no un equipo por defecto.

DECISIÓN · el límite de `execution_slots` DEJA FUERA, y NO reduce la composición
    `C4` paso 6, literal: «Lo que no cabe queda `esperando-capacidad`. NO se reduce la
    composición para que quepa». El equipo escrito lleva los dos: los roles despachados y
    los que ESPERAN CAPACIDAD, y los segundos no son «retirados». Un equipo que se recorta
    para caber es el sesgo barato que `a.7` derogó.

DECISIÓN · el conflicto AUTOR / REVISOR / ADJUDICADOR se impide por DATO, no por criterio
    `C4` lo prohíbe dos veces: «PROHIBIDO combinar dos roles que la composición declara
    independientes» y «PROHIBIDO un agente ocupando un rol productor y su crítico en el
    mismo paquete». La lista `independientes` de la composición es la sede, y ante conflicto
    entre `combinables` e `independientes` MANDA `independientes` —también literal—. Aquí no
    se juzga si dos roles «se parecen»: se lee la lista.
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto

from .corpus import CAPACIDADES, Corpus
from .errores import (
    ComposicionDeEquipoAusente,
    ConflictoDeRoles,
    LimiteDeCapacidadExcedido,
    MetodoNoEsCapacidad,
)
from .procesos import capacidad_de, metodo_de

DOMINIO = "equipos"
ESQUEMA = "ads.estado/1"

# `C4`: los DOS equipos permanentemente activos, y `ENC` NO es uno de ellos (`E1.2`).
PERMANENTEMENTE_ACTIVOS = ("DSP", "SIS")

# `execution_slots` por defecto. `b.11` lo declara calibrable y `C4` usa `auto → 4` en su
# ejemplo; se toma ese valor como defecto EXPLÍCITO para que el recorte sea reproducible.
SLOTS_POR_DEFECTO = 4

ESTADO_DESPACHADO = "despachado"
ESTADO_ESPERANDO_CAPACIDAD = "esperando-capacidad"


def derivar_capacidades(ruta):
    """Las CAPACIDADES de la ruta. Nunca un método, y nunca `ENC`.

    Es la entrada de `C4`: se materializa un equipo por capacidad que participa, y sólo por
    ésas. Las presencias que NO participan —ejecutor, autoridad, encuadre— no materializan
    equipo, porque no depositan capa.
    """
    salida = []
    for participante in ruta["participantes"]:
        capacidad = participante["capacidad"]
        if capacidad not in CAPACIDADES:
            raise MetodoNoEsCapacidad(
                "la ruta trae `" + str(capacidad) + "` como capacidad y no lo es; las "
                "quince son " + ", ".join(CAPACIDADES),
                encontrado=str(capacidad),
            )
        if capacidad not in salida:
            salida.append(capacidad)
    return tuple(sorted(salida))


def exigir_capacidad(nombre, *, corpus=None):
    """Falla si `nombre` es un MÉTODO y no una capacidad. La confusión tiene error propio."""
    corpus = corpus or Corpus()
    if nombre in CAPACIDADES:
        return nombre
    posible = capacidad_de(nombre)
    metodo = metodo_de(nombre)
    if posible in CAPACIDADES and metodo:
        raise MetodoNoEsCapacidad(
            "`" + str(nombre) + "` nombra el MÉTODO `" + metodo + "` de la capacidad `"
            + posible + "`; lo que se materializa por `C4` es la capacidad, y el método es "
            "CÓMO trabaja (`C1`)",
            capacidad=posible, metodo=metodo,
        )
    for capacidad in CAPACIDADES:
        if nombre in corpus.metodos(capacidad):
            raise MetodoNoEsCapacidad(
                "`" + str(nombre) + "` es un método de `" + capacidad + "`, no una capacidad",
                capacidad=capacidad, metodo=str(nombre),
            )
    raise MetodoNoEsCapacidad(
        "`" + str(nombre) + "` no es ninguna de las quince capacidades", encontrado=str(nombre),
    )


# ===========================================================================
#  el algoritmo de `C4`
# ===========================================================================
def materializar(capacidad, *, corpus=None, composiciones_verdaderas=(),
                 condiciones_de_rol=(), slots=SLOTS_POR_DEFECTO, metodo=None,
                 paquete=None):
    """Los siete pasos de `C4`, en orden, sobre las composiciones reales del corpus."""
    corpus = corpus or Corpus()
    exigir_capacidad(capacidad, corpus=corpus)
    if not isinstance(slots, int) or isinstance(slots, bool) or slots < 1:
        raise LimiteDeCapacidadExcedido(
            "`execution_slots` es un entero >= 1; con cero no se materializa nada y no es "
            "un límite, es una parada",
        )
    verdaderas = tuple(str(c) for c in composiciones_verdaderas)
    verdaderos_roles = {str(c) for c in condiciones_de_rol}

    # PASO 2 · elegir composición, EN EL ORDEN EN QUE ESTÁN ESCRITAS.
    escritas = corpus.composiciones(capacidad)
    elegida = None
    descartadas = []
    for composicion in escritas:
        if composicion["id"] in verdaderas:
            elegida = composicion
            break
        descartadas.append({
            "composicion": composicion["id"],
            "motivo": "su condición no consta verdadera para este trabajo",
        })
    if elegida is None:
        raise ComposicionDeEquipoAusente(
            "ninguna composición de `" + capacidad + "` tiene condición verdadera para "
            "este trabajo; `C4` manda escalarlo a `SIS` como defecto del catálogo, no "
            "materializar un equipo por defecto",
            capacidad=capacidad,
            composiciones=[c["id"] for c in escritas],
        )

    # PASO 3 · expandir roles.
    roles = []
    fuera = []
    for entrada in elegida.get("roles") or []:
        obligatorio = bool(entrada.get("obligatorio"))
        condicion = str(entrada.get("condicion") or "").strip()
        if obligatorio or (condicion and condicion in verdaderos_roles):
            roles.append({
                "rol": entrada["rol"],
                "obligatorio": obligatorio,
                "agentes": str(entrada.get("agentes") or "1"),
                "condicion": condicion or None,
            })
        else:
            fuera.append({
                "rol": entrada["rol"],
                "motivo": "rol condicional cuya condición no consta verdadera: "
                          + (condicion or "(sin condición declarada)"),
            })

    # PASO 5 · combinación, con `independientes` mandando sobre `combinables`.
    independientes = _independientes(elegida)
    combinaciones = []
    for entrada in elegida.get("combinables") or []:
        pareja = [str(r) for r in (entrada.get("roles") or [])]
        conflicto = [r for r in pareja if _choca(r, pareja, independientes)]
        if conflicto:
            combinaciones.append({
                "roles": pareja,
                "aplicada": False,
                "motivo": "`independientes` manda sobre `combinables` (`C4` paso 5): "
                          + ", ".join(sorted(conflicto)) + " no puede compartir agente",
            })
            continue
        if all(any(r["rol"] == nombre for r in roles) for nombre in pareja):
            combinaciones.append({
                "roles": pareja, "aplicada": True,
                "motivo": str(entrada.get("motivo") or ""),
            })

    # PASO 4 · asignar agentes, y PASO 6 · comprobar límites.
    asignados, esperando = [], []
    for indice, rol in enumerate(sorted(roles, key=lambda r: r["rol"])):
        destino = asignados if indice < slots else esperando
        destino.append({
            "rol": rol["rol"],
            "obligatorio": rol["obligatorio"],
            "agentes": rol["agentes"],
            "condicion": rol["condicion"],
            "estado": ESTADO_DESPACHADO if indice < slots else ESTADO_ESPERANDO_CAPACIDAD,
            "comparte_agente_con": _companero(rol["rol"], combinaciones),
        })

    equipo = {
        "esquema": ESQUEMA,
        "capacidad": capacidad,
        "metodo": metodo,
        "paquete": paquete,
        "composicion": elegida["id"],
        "clase_de_trabajo": str(elegida.get("clase_de_trabajo") or ""),
        "condicion_que_la_eligio": str(elegida.get("condicion") or "").strip(),
        "composiciones_descartadas": descartadas,
        "roles": asignados,
        "esperando_capacidad": esperando,
        "roles_fuera": sorted(fuera, key=lambda r: r["rol"]),
        "combinaciones": sorted(combinaciones, key=lambda c: tuple(c["roles"])),
        "independientes": sorted(independientes, key=lambda i: i["rol"]),
        "slots": int(slots),
        "permanentemente_activo": capacidad in PERMANENTEMENTE_ACTIVOS,
        "retirada": str(elegida.get("retirada") or ""),
    }
    equipo["id"] = identificador(equipo)
    return equipo


def _independientes(composicion):
    salida = []
    for entrada in composicion.get("independientes") or []:
        salida.append({
            "rol": str(entrada["rol"]),
            "de": [str(d) for d in (entrada.get("de") or [])],
            "motivo": str(entrada.get("motivo") or ""),
        })
    return salida


def _choca(rol, pareja, independientes):
    for entrada in independientes:
        if entrada["rol"] == rol and any(otro in entrada["de"] for otro in pareja if otro != rol):
            return True
        if rol in entrada["de"] and entrada["rol"] in pareja:
            return True
    return False


def _companero(rol, combinaciones):
    for entrada in combinaciones:
        if entrada["aplicada"] and rol in entrada["roles"]:
            otros = [r for r in entrada["roles"] if r != rol]
            if otros:
                return otros[0]
    return None


def exigir_separacion(equipo, *, autor, revisor, adjudicador=None):
    """AUTOR, REVISOR y ADJUDICADOR no pueden ser el mismo agente cuando la composición lo veta.

    `C4`: «PROHIBIDO un agente ocupando un rol productor y su crítico en el mismo paquete».
    La sede de qué es «su crítico» es la lista `independientes` de la composición, y por eso
    esta comprobación LEE esa lista en vez de decidir por su cuenta qué roles se parecen.
    """
    implicados = [r for r in (autor, revisor, adjudicador) if r]
    if len(implicados) != len(set(implicados)):
        repetido = sorted({r for r in implicados if implicados.count(r) > 1})
        raise ConflictoDeRoles(
            "el mismo rol ocupa dos de las tres posiciones (autor, revisor, adjudicador): "
            + ", ".join(repetido),
            roles=repetido,
        )
    for entrada in equipo["independientes"]:
        for otro in implicados:
            if otro == entrada["rol"]:
                continue
            if otro in entrada["de"] and entrada["rol"] in implicados:
                if _comparten(equipo, entrada["rol"], otro):
                    raise ConflictoDeRoles(
                        "`" + entrada["rol"] + "` es independiente de `" + otro + "` y el "
                        "equipo los hace compartir agente: " + entrada["motivo"],
                        roles=[entrada["rol"], otro],
                    )
    return True


def _comparten(equipo, uno, otro):
    for rol in equipo["roles"]:
        if rol["rol"] == uno and rol["comparte_agente_con"] == otro:
            return True
        if rol["rol"] == otro and rol["comparte_agente_con"] == uno:
            return True
    return False


def identificador(equipo):
    """`eq-<16 hex>` derivado del CONTENIDO: mismo paquete y misma composición, mismo equipo."""
    sin_id = {clave: valor for clave, valor in equipo.items() if clave != "id"}
    digest = cid_de_objeto(sin_id)
    return "eq-" + digest.split(":", 1)[-1][:16]


def ruta_de(identificador_de_equipo):
    return DOMINIO + "/" + identificador_de_equipo + ".json"
