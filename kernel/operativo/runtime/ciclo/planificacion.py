#!/usr/bin/env python3
"""planificacion — la etapa 4 del ciclo: items, paquetes, dependencias, límites y frenos.

Es la etapa que CONVIERTE una ruta compuesta en trabajo despachable, y lo hace **por el
runtime que ya existe**: `Runtime.crear_item` y `Runtime.crear_paquete`. Este módulo no
tiene una segunda alta de trabajo, ni una cola propia, ni un fichero de plan: el plan es un
objeto durable más, en su dominio, escrito por el motor.

DECISIÓN · el paquete conserva el vocabulario CERRADO del runtime, y el plan lo enriquece
    Alternativas: (a) añadir campos al objeto `paquete` —capacidad ADS, obligación, rol—;
    (b) dejar el paquete exactamente como el `§3` del contrato del corte 2 lo declara, y
    poner la correspondencia en el objeto `plan`.
    Se elige (b). `runtime/modelo.py` valida el paquete contra una lista CERRADA de claves y
    rechaza las que sobran; ensancharla desde aquí sería cambiar un contrato ajeno para
    ahorrarse un objeto. Con (b) `canonico/planes/<id>.json` dice qué paquete cubre qué
    obligación de qué capacidad, el runtime sigue despachando lo que sabe despachar, y las
    dos cosas se leen juntas sin que ninguna dependa de la otra.

DECISIÓN · `capacidades_requeridas` del paquete son CAPACIDADES DE ADAPTADOR, no de ADS
    Es una colisión de nombres real y conviene decirla: en `runtime/`, `capacidades_requeridas`
    selecciona el ADAPTADOR (`proceso-local`), y en `b.16` una «capacidad» es `PRD`, `CNS`
    o `VER`. No son lo mismo y no se mezclan: el plan declara la capacidad ADS de cada
    paquete y el paquete declara las del adaptador que lo ejecutará.

DECISIÓN · la PRIORIDAD se deriva de la VÍA, y NADIE la toca después
    `gate:despacho-coherente` exige determinismo: «mismo estado produce misma selección, con
    desempate por identificador». Lo que aporta este módulo es que la prioridad no la escriba
    nadie a mano: vía 1 → 90, vía 2 → 70, vía 3 → 50, vía 4 → 30. La propietaria global va
    primero porque su capa DEFINE el resultado, y sin ella las demás no tienen contra qué
    medirse.

    Y aquí termina la prioridad: `b.12` es terminante —«DSP informa de la inanición. No
    cambia la prioridad. Nunca»—, de modo que un paquete que lleva veinte pasadas esperando
    NO sube de vía ni de número. Lo que lo saca de la cola es el criterio (c) de `b.12`, la
    antigüedad de espera, que adelanta entre IGUALES en prioridad. `elegibles()` ordena por
    los CUATRO criterios del paso 5 —prioridad, grado de salida en el grafo `depende_de`,
    antigüedad de espera e identificador—, no por dos como hacía.

DECISIÓN · el grafo del criterio (b) es el `depende_de` que este módulo escribe
    El «grado de salida en el grafo» de `b.12` paso 5 (b) no es una estimación de impacto:
    es cuántos paquetes declaran depender de éste, y esa declaración la produce
    `paralelismo.secuenciar` con la condición compuesta de `a.5`. Por eso secuenciar mal se
    paga dos veces —en el paralelismo y en el orden de despacho— y por eso la traza de
    `condicion_de_paralelismo` que este plan publica es también la explicación del orden.

DECISIÓN · el tope de reintentos es TRES y viene de `a.9`, no de este módulo
    Se toma de `runtime.politica.MAX_INTENTOS_POR_DEFECTO`, que ya lo instancia. Escribir
    aquí un `3` sería una segunda sede del mismo número.

DECISIÓN · `b.15.1` abre y despacha SIN preguntar, y el alcance autorizado es un DATO
    «Dentro del alcance ya autorizado, DSP crea y despacha el desbloqueador sin preguntar.
    Sólo escala el que amplía o cambia el alcance.» El alcance autorizado se declara en el
    plan —lista de capacidades y de fuentes—, y `abrir_desbloqueador` compara contra ella:
    dentro, crea; fuera, `AlcanceNoAutorizado` y escala. Que la frontera sea un dato es lo
    que impide que «dentro del alcance» acabe significando «lo que parecía razonable».
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto
from runtime import modelo
from runtime.politica import MAX_INTENTOS_POR_DEFECTO

from . import durable, paralelismo
from .corpus import Corpus
from .encuadre import DOMINIO as DOMINIO_ENCUADRES, ruta_de as ruta_de_encuadre
from .equipos import DOMINIO as DOMINIO_EQUIPOS, ruta_de as ruta_de_equipo
from .errores import AlcanceNoAutorizado, PlanificacionInvalida
from .rutas import (
    DOMINIO as DOMINIO_RUTAS,
    VIA_CONDICIONAL,
    VIA_ITEM_PROPIO,
    VIA_OBLIGATORIA,
    VIA_PROPIETARIA,
    ruta_de as ruta_de_ruta,
    traza,
)

DOMINIO = "planes"
ESQUEMA = "ads.estado/1"

# EL ORDEN DE LAS ESTACIONES de una ruta, como DATO. `rutas.componer` ordena los
# participantes por (vía, capacidad) —un orden de LECTURA, alfabético—, y
# `paralelismo.secuenciar` hace que cada paquete espere a los ANTERIORES con los que no es
# paralelizable: con ese orden, `CNS` (C) quedaba antes que `PRD` (P) y la construcción
# esperaba a nada mientras la definición de producto esperaba a la construcción. Lo que
# manda es el orden de las OBLIGACIONES del proceso (`b.16`, campo `obligatorias`, en el
# orden en que están escritas) y, para las capacidades condicionales, el orden de las
# estaciones que los diez circuitos de `circuitos/00-CIRCUITOS.md` dibujan: las
# condiciones de DOM y SEG ANTES de construir, ENT, USO y APR DESPUÉS de verificar, y las
# revisiones de DOM y SEG tras VER. Se declara aquí una vez, con su fuente, y se contrasta
# en la batería contra los diagramas.
ORDEN_DE_ESTACIONES = ("ENC", "PRD", "INV", "ARQ", "DIS", "DOM", "SEG", "PLT", "CNS", "VER",
                       "ENT", "USO", "APR", "SIS", "DSP")
METODOS_POSTERIORES_A_VER = ("revision",)

PRIORIDAD_POR_VIA = {
    VIA_PROPIETARIA: 90,
    VIA_OBLIGATORIA: 70,
    VIA_CONDICIONAL: 50,
    VIA_ITEM_PROPIO: 30,
}

# `a.8` — los TRES niveles de intervención del Owner. Vocabulario cerrado.
INTERVENCION_OBLIGATORIA = "obligatorio"
INTERVENCION_ACUMULADA = "opcional-acumulada"
INTERVENCION_NINGUNA = "ninguna"
NIVELES_DE_INTERVENCION = (INTERVENCION_OBLIGATORIA, INTERVENCION_ACUMULADA,
                           INTERVENCION_NINGUNA)

CAPACIDADES_DE_ADAPTADOR_POR_DEFECTO = ("proceso-local",)


class Planificador:
    """Crea items y paquetes por el runtime, y escribe el plan por el motor."""

    def __init__(self, runtime, *, corpus=None):
        self.runtime = runtime
        self.corpus = corpus or Corpus()

    # ------------------------------------------------------------ registro
    @property
    def almacen(self):
        return self.runtime.almacen

    def registrar_encuadre(self, encuadre):
        durable.escribir(
            self.almacen, clase="ciclo.encuadre.registrado",
            motivo="encuadre " + encuadre["id"] + " de la clase " + encuadre["clase"],
            objetos={ruta_de_encuadre(encuadre["id"]): encuadre},
            semilla={"encuadre": encuadre["id"]},
        )
        return encuadre

    def registrar_ruta(self, ruta):
        durable.escribir(
            self.almacen, clase="ciclo.ruta.compuesta",
            motivo="ruta " + ruta["id"] + " de " + ruta["proceso"] + " para la fase "
                   + ruta["fase"],
            objetos={ruta_de_ruta(ruta["id"]): ruta},
            semilla={"ruta": ruta["id"]},
        )
        return ruta

    def _independencias_de(self, roles_por_capacidad):
        """`{rol: [roles de la MISMA capacidad de los que exige independencia]}`."""
        salida = {}
        for capacidad, roles in roles_por_capacidad.items():
            for rol in roles:
                independencia = self.corpus.rol(rol).get("independencia") or {}
                if not independencia.get("requiere_independencia"):
                    continue
                salida[rol] = [otro for otro in roles
                               if otro != rol and otro in (independencia.get("de_quien") or [])]
        return salida

    def registrar_equipos(self, equipos):
        objetos = {ruta_de_equipo(e["id"]): e for e in equipos}
        durable.escribir(
            self.almacen, clase="ciclo.equipos.materializados",
            motivo="materialización de " + str(len(equipos)) + " equipo(s) por `C4`",
            objetos=objetos, semilla=sorted(objetos),
        )
        return equipos

    # ---------------------------------------------------------- planificar
    def planificar(self, encuadre, ruta, *, equipos=(), titulo=None,
                   capacidades_de_adaptador=CAPACIDADES_DE_ADAPTADOR_POR_DEFECTO,
                   orden_por_capacidad=None, slots=0,
                   intervencion=INTERVENCION_NINGUNA, alcance_autorizado=None,
                   secuencial=None, acoplamiento_por_capacidad=None,
                   roles_por_capacidad=None, orden_por_rol=None, item=None,
                   capacidades_de_adaptador_por_rol=None):
        """Crea el item y sus paquetes, y escribe el plan. Idempotente por contenido.

        PAQUETES POR ROL (`CONTRATO-OFICINA.md`). Cuando `roles_por_capacidad` declara los
        roles que el equipo materializó para una capacidad, se crea UN paquete por
        (participante, rol) en vez de uno por participante, y dentro de la misma capacidad
        un rol que se declara INDEPENDIENTE de otro de la composición ESPERA a ese otro:
        la revisión de construcción espera a la implementación porque su contrato dice que
        no puede compartir agente con ella, y esa es la única fuente del orden. Sin
        `roles_por_capacidad` el comportamiento es EXACTAMENTE el de antes.

        `item` permite planificar sobre un item que YA EXISTE en el estado —el de la
        instancia que gobierna el producto—, en vez de acuñar uno nuevo desde el encuadre.
        `orden_por_rol` y `capacidades_de_adaptador_por_rol` afinan la orden por rol; si no
        están, manda la de la capacidad.
        """
        if intervencion not in NIVELES_DE_INTERVENCION:
            raise PlanificacionInvalida(
                "nivel de intervención del Owner fuera de los TRES de `a.8`: "
                + repr(intervencion) + "; válidos: " + ", ".join(NIVELES_DE_INTERVENCION),
            )
        if ruta["encuadre"] != encuadre["id"]:
            raise PlanificacionInvalida(
                "la ruta dice componer el encuadre `" + str(ruta["encuadre"])
                + "` y se planifica con `" + encuadre["id"] + "`",
            )
        self.registrar_encuadre(encuadre)
        self.registrar_ruta(ruta)
        if equipos:
            self.registrar_equipos(equipos)

        if item is None:
            item = "it-" + cid_de_objeto({"encuadre": encuadre["id"], "ruta": ruta["id"]}
                                         ).split(":", 1)[-1][:12]
        titulo_real = titulo or (encuadre["resultado_perseguido"]
                                 or encuadre["expresion_literal"])[:120]
        if durable.leer(self.almacen, "items/" + item + ".json") is None:
            self.runtime.crear_item(
                id=item, titulo=titulo_real,
                motivo="alta del item desde el encuadre " + encuadre["id"],
            )
        roles_por_capacidad = {k: list(v) for k, v in (roles_por_capacidad or {}).items()}
        orden_por_rol = dict(orden_por_rol or {})
        adaptador_por_rol = dict(capacidades_de_adaptador_por_rol or {})
        independencias = self._independencias_de(roles_por_capacidad)

        ordenes = dict(orden_por_capacidad or {})
        acoplamientos = dict(acoplamiento_por_capacidad or {})
        # PRIMERA PASADA: se construyen los paquetes en memoria, CON su declaración de
        # acoplamiento, para poder evaluar entre ellos la condición compuesta de `a.5`.
        # Sin la declaración no hay nada que evaluar, y por eso la etapa 4 va antes que la 5
        # en el `§7.2` y también aquí.
        # Cada UNIDAD es (participante, rol) cuando hay roles declarados, o el participante a
        # secas. El identificador entra el rol para que dos roles de la misma capacidad no
        # colisionen, y NO lo entra cuando no hay rol, para que ningún plan ya escrito
        # cambie de identidad.
        unidades = []
        capacidades_con_obligacion = {p["capacidad"] for p in ruta["participantes"]
                                      if p.get("obligacion")}
        participantes = sorted(ruta["participantes"],
                               key=lambda p: _orden_de_estacion(ruta, p))
        for participante in participantes:
            roles = roles_por_capacidad.get(participante["capacidad"]) or [None]
            # LA PROPIETARIA GLOBAL (vía 1) sin obligación propia. `b.10`: «la integración
            # la declara el propietario global, y sólo él». Cuando esa capacidad además
            # participa con obligación, su vía 1 NO repite el trabajo de sus roles: produce
            # UN paquete de INTEGRACIÓN SEMÁNTICA, que espera a todos los demás del item.
            # Sin roles declarados el comportamiento es exactamente el de antes.
            es_integracion = (
                roles != [None] and participante["via"] == VIA_PROPIETARIA
                and not participante.get("obligacion")
                and participante["capacidad"] in capacidades_con_obligacion
            )
            if es_integracion:
                roles = [roles[0]]
            for rol in roles:
                semilla = {
                    "item": item,
                    "capacidad": participante["capacidad"],
                    "via": participante["via"],
                    "obligacion": participante["obligacion"],
                }
                if rol is not None:
                    semilla["rol"] = rol
                unidades.append({
                    "id": "pq-" + cid_de_objeto(semilla).split(":", 1)[-1][:12],
                    "participante": participante,
                    "rol": rol,
                    "integracion": es_integracion,
                })
        por_rol_y_cap = {(u["participante"]["capacidad"], u["rol"]): u["id"]
                         for u in unidades if not u["integracion"]}
        proyectados = []
        for unidad in unidades:
            participante = unidad["participante"]
            # Dependencia INTRA-capacidad por independencia declarada: el rol que exige
            # independencia de otro de la misma composición espera a ese otro.
            previos = []
            if unidad["integracion"]:
                previos = [u["id"] for u in unidades if u["id"] != unidad["id"]]
            for de_quien in independencias.get(unidad["rol"], ()):
                previo = por_rol_y_cap.get((participante["capacidad"], de_quien))
                if previo and previo != unidad["id"]:
                    previos.append(previo)
            proyectados.append({
                "id": unidad["id"],
                "depende_de": sorted(set(previos)),
                "acoplamiento": modelo.normalizar_acoplamiento(
                    acoplamientos.get(participante["capacidad"])),
            })
        if secuencial is True:
            # Secuenciar SIN evaluar sigue estando permitido —es el fallback seguro—, pero
            # es una DECISIÓN explícita del llamador y queda escrita como tal.
            espera = {}
            previo = None
            for proyectado in proyectados:
                espera[proyectado["id"]] = [previo] if previo else []
                previo = proyectado["id"]
            traza_de_paralelismo = [{
                "paquete": identificador, "espera_a": esperados,
                "incumplidas": ["(no evaluadas: secuenciación declarada por el llamador)"],
                "motivos": ["el llamador pidió `secuencial=True`; `b.11` lo admite como "
                            "FALLBACK SEGURO y aquí queda escrito que no se evaluó"],
            } for identificador, esperados in espera.items() if esperados]
        else:
            espera, traza_de_paralelismo = paralelismo.secuenciar(proyectados)

        paquetes, correspondencia, anterior = [], [], None
        previos_declarados = {p["id"]: p["depende_de"] for p in proyectados}
        for unidad in unidades:
            participante = unidad["participante"]
            identificador = unidad["id"]
            depende_de = sorted(set(espera.get(identificador, []))
                                | set(previos_declarados.get(identificador, [])))
            orden = orden_por_rol.get(unidad["rol"]) if unidad["rol"] else None
            if orden is None:
                orden = ordenes.get(participante["capacidad"])
            if orden is None:
                raise PlanificacionInvalida(
                    "no hay orden declarada para la capacidad `" + participante["capacidad"]
                    + "`; un paquete sin orden no es despachable y no se inventa una",
                    capacidad=participante["capacidad"],
                )
            requeridas = adaptador_por_rol.get(unidad["rol"]) if unidad["rol"] else None
            if requeridas is None and orden_por_rol.get(unidad["rol"]) is not None:
                # Una orden afinada POR ROL nombra su adaptador: el paquete exige la
                # capacidad de ESE adaptador, no la genérica. Medido en `T470`: un paquete de
                # agente con `capacidades_requeridas: [worker]` no lo atendía nadie.
                requeridas = [str(orden.get("adaptador") or "")]
            if requeridas is None:
                requeridas = capacidades_de_adaptador
            if durable.leer(self.almacen, "paquetes/" + identificador + ".json") is None:
                self.runtime.crear_paquete(
                    id=identificador, item=item,
                    capacidades_requeridas=list(requeridas),
                    orden=orden,
                    prioridad=PRIORIDAD_POR_VIA[participante["via"]],
                    max_intentos=MAX_INTENTOS_POR_DEFECTO,
                    depende_de=depende_de,
                    acoplamiento=acoplamientos.get(participante["capacidad"]),
                )
            paquetes.append(identificador)
            fila = {
                "paquete": identificador,
                "capacidad": participante["capacidad"],
                "metodo": participante["metodo"],
                "via": participante["via"],
                "obligacion": participante["obligacion"],
                "gate": participante["gate"],
                "salida": participante["salida"],
                "criterio_de_satisfaccion": participante["criterio_de_satisfaccion"],
                "prioridad": PRIORIDAD_POR_VIA[participante["via"]],
                "depende_de": depende_de,
            }
            if unidad["rol"] is not None:
                fila["rol"] = unidad["rol"]
                fila["metodo"] = _metodo_del_rol(self.corpus, unidad["rol"], fila["metodo"])
                fila["gate"] = _gate_del_rol(self.corpus, unidad["rol"], fila["gate"])
            if unidad["integracion"]:
                fila["obligacion"] = "integracion-semantica"
                fila["salida"] = ("la declaración de integración semántica del propietario "
                                  "global, sobre todas las capas depositadas del item")
                fila["criterio_de_satisfaccion"] = (
                    "el propietario global declara, con las entregas del item delante, que "
                    "el resultado perseguido está integrado y nombra lo que no")
                fila["integracion_semantica"] = True
            correspondencia.append(fila)
            anterior = identificador

        plan = {
            "esquema": ESQUEMA,
            "item": item,
            "encuadre": encuadre["id"],
            "ruta": ruta["id"],
            "proceso": ruta["proceso"],
            "fase": ruta["fase"],
            "propietario_global": ruta["propietario_global"],
            "paquetes": paquetes,
            "correspondencia": correspondencia,
            "equipos": sorted(e["id"] for e in equipos),
            "traza_de_ruta": traza(ruta),
            "obligaciones": ruta["obligaciones"],
            "max_intentos": MAX_INTENTOS_POR_DEFECTO,
            "slots": int(slots) if slots else 0,
            "intervencion_del_owner": intervencion,
            "puntos_de_intervencion": _puntos_de_intervencion(ruta, intervencion),
            "alcance_autorizado": _alcance(alcance_autorizado, ruta, encuadre),
            "secuencial": bool(secuencial),
            # La etapa 5 del `§7.2`, ESCRITA: qué paquete espera a cuál y por qué condición
            # de `a.5`. `b.12` paso 7 lo exige —«un dispatcher que elige sin explicar es una
            # caja negra»— y sin esto la secuenciación sería una afirmación sin traza.
            "condicion_de_paralelismo": {
                "condiciones": list(paralelismo.CONDICIONES),
                "traza": traza_de_paralelismo,
            },
            "derivado_de": None,
        }
        plan["id"] = _identificador(plan)
        durable.escribir(
            self.almacen, clase="ciclo.plan.escrito",
            motivo="plan " + plan["id"] + " del item " + item,
            objetos={ruta_de(plan["id"]): plan},
            semilla={"plan": plan["id"]},
        )
        return plan

    # ------------------------------------------------------- desbloqueador
    def abrir_desbloqueador(self, plan, paquete_bloqueado, *, capacidad, orden,
                            capacidades_de_adaptador=CAPACIDADES_DE_ADAPTADOR_POR_DEFECTO,
                            motivo):
        """`b.15.1`: dentro del alcance autorizado, DSP crea y despacha SIN preguntar."""
        alcance = plan["alcance_autorizado"]
        if capacidad not in alcance["capacidades"]:
            raise AlcanceNoAutorizado(
                "el desbloqueador necesita `" + str(capacidad) + "` y el alcance autorizado "
                "de este plan no la incluye; `b.15.1` sólo autoriza a crear y despachar "
                "DENTRO del alcance ya autorizado, y lo que lo amplía se escala",
                capacidad=str(capacidad), autorizadas=list(alcance["capacidades"]),
            )
        actual = durable.leer(self.almacen, "paquetes/" + paquete_bloqueado + ".json")
        if actual is None:
            raise PlanificacionInvalida(
                "no hay paquete `" + str(paquete_bloqueado) + "` que desbloquear",
                ruta=str(paquete_bloqueado),
            )
        if actual["estado"] != "bloqueado":
            raise PlanificacionInvalida(
                "`b.15.1` abre desbloqueadores para paquetes BLOQUEADOS, y `"
                + paquete_bloqueado + "` está en `" + actual["estado"] + "`",
                ruta=paquete_bloqueado,
            )
        identificador = "pq-" + cid_de_objeto({
            "desbloquea": paquete_bloqueado, "capacidad": capacidad, "motivo": motivo,
        }).split(":", 1)[-1][:12]
        if durable.leer(self.almacen, "paquetes/" + identificador + ".json") is None:
            self.runtime.crear_paquete(
                id=identificador, item=actual["item"],
                capacidades_requeridas=list(capacidades_de_adaptador),
                orden=orden, prioridad=95, max_intentos=MAX_INTENTOS_POR_DEFECTO,
                depende_de=[],
            )
        nuevo = dict(plan)
        nuevo["paquetes"] = sorted(set(plan["paquetes"]) | {identificador})
        nuevo["correspondencia"] = plan["correspondencia"] + [{
            "paquete": identificador,
            "capacidad": capacidad,
            "metodo": None,
            "via": None,
            "obligacion": None,
            "gate": None,
            "salida": "el desbloqueador de `" + paquete_bloqueado + "`",
            "criterio_de_satisfaccion": motivo,
            "prioridad": 95,
            "depende_de": [],
            "desbloquea": paquete_bloqueado,
            "abierto_por": "b.15.1",
        }]
        nuevo["id"] = _identificador(nuevo)
        durable.escribir(
            self.almacen, clase="ciclo.desbloqueador.abierto",
            motivo="b.15.1: desbloqueador " + identificador + " de " + paquete_bloqueado,
            objetos={ruta_de(nuevo["id"]): nuevo},
            semilla={"plan": nuevo["id"]},
        )
        return {"plan": nuevo, "paquete": identificador}


def _orden_de_estacion(ruta, participante):
    """La posición del participante en la ruta: obligación de `b.16` primero, estación después."""
    obligaciones = [o["id"] for o in ruta.get("obligaciones") or []]
    capacidad = participante["capacidad"]
    posicion = ORDEN_DE_ESTACIONES.index(capacidad) if capacidad in ORDEN_DE_ESTACIONES else 99
    if str(participante.get("metodo") or "") in METODOS_POSTERIORES_A_VER \
            and "VER" in ORDEN_DE_ESTACIONES:
        posicion = ORDEN_DE_ESTACIONES.index("VER") + 0.5
    if participante.get("obligacion") in obligaciones:
        # Entre dos obligatorias manda el orden del proceso; la estación sólo desempata.
        return (0, obligaciones.index(participante["obligacion"]), posicion, participante["via"])
    # La propietaria global sin obligación cierra: va la última (integración semántica).
    if participante["via"] == VIA_PROPIETARIA and not participante.get("obligacion"):
        return (2, 0, posicion, participante["via"])
    return (1, posicion, 0, participante["via"])


def _metodo_del_rol(corpus, rol, por_defecto):
    """El PRIMER método que el rol declara, salvo que la ruta ya fije uno de ese rol."""
    declarados = list(corpus.rol(rol).get("metodo") or [])
    if por_defecto in declarados:
        return por_defecto
    return declarados[0] if declarados else por_defecto


def _gate_del_rol(corpus, rol, por_defecto):
    """El gate del ROL manda sobre el de la capacidad: es contra lo que ese rol cierra."""
    return corpus.rol(rol).get("gate") or por_defecto


def _puntos_de_intervencion(ruta, intervencion):
    """Dónde espera el Owner. `a.8`: por AUTORIDAD o por incertidumbre, nunca por aritmética."""
    puntos = []
    if intervencion == INTERVENCION_NINGUNA:
        return puntos
    for participante in ruta["participantes"]:
        if participante["gate"]:
            puntos.append({
                "capacidad": participante["capacidad"],
                "gate": participante["gate"],
                "nivel": intervencion,
                "motivo": "la ruta declara intervención `" + intervencion + "` y esta "
                          "capacidad cierra su capa con un gate",
            })
    return sorted(puntos, key=lambda p: (p["capacidad"], p["gate"]))


def _alcance(declarado, ruta, encuadre):
    """El alcance autorizado, como DATO. Lo que no está dentro, se escala."""
    if declarado is None:
        capacidades = sorted({p["capacidad"] for p in ruta["participantes"]})
        fuentes = sorted(f["id"] for f in (encuadre["fuentes"].get("fuentes") or []))
        return {"capacidades": capacidades, "fuentes": fuentes,
                "origen": "derivado de la ruta compuesta y de `SOURCES.toml`"}
    return {
        "capacidades": sorted(str(c) for c in (declarado.get("capacidades") or [])),
        "fuentes": sorted(str(f) for f in (declarado.get("fuentes") or [])),
        "origen": str(declarado.get("origen") or "declarado por quien autoriza"),
    }


def _identificador(plan):
    sin_id = {clave: valor for clave, valor in plan.items() if clave != "id"}
    digest = cid_de_objeto(sin_id)
    return "pl-" + digest.split(":", 1)[-1][:16]


def ruta_de(identificador_de_plan):
    return DOMINIO + "/" + identificador_de_plan + ".json"


def planes(almacen):
    """Todos los planes de la revisión vigente, ordenados. Se leen; no se recuerdan."""
    return [almacen.leer(ruta) for ruta in sorted(almacen.listar(DOMINIO))]


def plan_de_item(almacen, item):
    for plan in planes(almacen):
        if plan["item"] == item:
            return plan
    return None
