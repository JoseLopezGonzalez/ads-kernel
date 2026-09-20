#!/usr/bin/env python3
"""oficina — la OFICINA sobre el ciclo: paquetes por rol, briefs, entregas, handoffs, niveles.

Aquí no hay ninguna máquina nueva. Hay la COMPOSICIÓN de las que ya existían y nadie
encadenaba en una instancia real:

    planificar     encuadrar → componer → materializar equipos → planificar paquetes POR ROL
    tomar          `Runtime.tomar` + el BRIEF derivado del estado y del corpus
    entregar       validar la ENTREGA → publicar por el dispatcher → registrar la entrega →
                   dictamen del gate si el rol juzga → handoffs a los sucesores, o
                   devolución con paquete de corrección, o bloqueo, o escalado
    aceptar        el dictamen del OWNER sobre `gate:aceptacion-del-owner`
    cerrar_item    los NIVELES DE TERMINACIÓN del circuito base, y `gate:cierre-de-item`

Lo que este módulo garantiza, y una prueba ejerce cada garantía:

    · un paquete de revisión ESPERA al de construcción porque su contrato de rol exige
      independencia, y ninguna composición lo puede evitar
    · quien juzga una capa no es quien la produjo: por capacidad (`gates.aplicar`) y por
      TRABAJADOR (`terminacion`): la autocertificación se rechaza con su nombre
    · una devolución crea SIEMPRE su paquete de corrección y un nuevo paquete de revisión
      que espera a la corrección; los sucesores se reapuntan ANTES de cerrar el paquete
      que devuelve, para que nadie pueda tomar un sucesor sobre una capa devuelta
    · el freno de `a.7` se cuenta y a la tercera devolución se ESCALA, no se recompone
    · un trabajador bloqueado deja el paquete `bloqueado` con qué lo desbloquearía, y no
      un `fallido` que consuma intentos
    · un item no se cierra como producto mientras un nivel exigido por su circuito base no
      tenga dictamen ni condición de inaplicabilidad
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto

from . import base as modulo_base, briefs, cierre as modulo_cierre, durable, entregas, formas, gates, handoffs, impacto as modulo_impacto
from . import encuadre as modulo_encuadre, equipos as modulo_equipos, paralelismo
from . import planificacion, rutas as modulo_rutas, terminacion
from .corpus import CAPACIDADES, Corpus
from .errores import (
    BaseContradicha,
    ImpactoNoCubierto,
    AutocertificacionRechazada,
    CicloInconsistente,
    EntregaInvalida,
    FrenoDisparado,
    GateFallido,
    RolSinAgente,
)

PRIORIDAD_DE_CORRECCION = 95
SLUG_DE_CAPACIDAD = {"CNS": "con"}


def _slug(capacidad):
    return SLUG_DE_CAPACIDAD.get(capacidad, capacidad.lower())


# ===========================================================================
#  lecturas DERIVADAS del estado
# ===========================================================================
def planes_de_item(almacen, item):
    return [p for p in planificacion.planes(almacen) if p.get("item") == item]


def plan_vigente_de_item(almacen, item):
    """El plan que nadie ha sustituido. Con corrección hay varios y sólo uno manda."""
    candidatos = planes_de_item(almacen, item)
    sustituidos = {p.get("sustituye_a") for p in candidatos if p.get("sustituye_a")}
    vigentes = [p for p in candidatos if p["id"] not in sustituidos]
    if not vigentes:
        return None
    vigentes.sort(key=lambda p: (len(p.get("paquetes") or []), p["id"]))
    return vigentes[-1]


def plan_de_paquete(almacen, paquete):
    """`(plan vigente, fila de correspondencia)` del paquete, o `(None, None)`."""
    objeto = durable.leer(almacen, "paquetes/" + paquete + ".json")
    if objeto is None:
        return None, None
    plan = plan_vigente_de_item(almacen, objeto["item"])
    if plan is None:
        return None, None
    for fila in plan.get("correspondencia") or []:
        if fila.get("paquete") == paquete:
            return plan, fila
    return plan, None


def equipo_de(almacen, plan, capacidad):
    for identificador in plan.get("equipos") or []:
        equipo = durable.leer(almacen, modulo_equipos.ruta_de(identificador))
        if equipo and equipo.get("capacidad") == capacidad:
            return equipo
    return None


def agente_del_rol(equipo, rol):
    for fila in (equipo or {}).get("roles") or []:
        if fila.get("rol") == rol:
            return {"agente": fila.get("agente"), "modelo": fila.get("modelo"),
                    "estado": fila.get("estado"), "slot": fila.get("slot")}
    for fila in (equipo or {}).get("esperando_capacidad") or []:
        if fila.get("rol") == rol:
            return {"agente": fila.get("agente"), "modelo": fila.get("modelo"),
                    "estado": fila.get("estado"), "slot": None}
    return None


def handoffs_del_item(almacen, item):
    salida = []
    for ruta in sorted(almacen.listar(handoffs.DOMINIO)):
        objeto = almacen.leer(ruta)
        if str((objeto.get("trazabilidad") or {}).get("item") or "") == item:
            salida.append(objeto)
    return salida


def handoffs_pendientes_para(almacen, paquete):
    """Entregas EMITIDAS cuyo destino es este paquete: hay que acusarlas o rechazarlas."""
    salida = []
    for ruta in sorted(almacen.listar(handoffs.DOMINIO)):
        objeto = almacen.leer(ruta)
        trazabilidad = objeto.get("trazabilidad") or {}
        if trazabilidad.get("destino") == paquete and objeto.get("estado") == handoffs.EMITIDO:
            salida.append(objeto)
    return salida


def handoff_acusado_por(almacen, paquete):
    for ruta in sorted(almacen.listar(handoffs.DOMINIO)):
        objeto = almacen.leer(ruta)
        trazabilidad = objeto.get("trazabilidad") or {}
        if trazabilidad.get("destino") == paquete and objeto.get("estado") == handoffs.ACUSADO:
            return objeto
    return None


def dictamenes_de_item(almacen, item):
    salida = []
    for ruta in sorted(almacen.listar(gates.DOMINIO)):
        objeto = almacen.leer(ruta)
        entrada = objeto.get("entrada") or {}
        if str(entrada.get("item") or "") == item:
            salida.append(objeto)
    return salida


def cierres_de_item(almacen, item):
    salida = []
    for ruta in sorted(almacen.listar(modulo_cierre.DOMINIO)):
        objeto = almacen.leer(ruta)
        if objeto.get("item") == item:
            salida.append(objeto)
    return salida


def entregas_del_item(almacen, item):
    salida = []
    for ruta in sorted(almacen.listar(entregas.DOMINIO)):
        objeto = almacen.leer(ruta)
        if objeto.get("item") == item or _item_de_entrega(almacen, objeto) == item:
            salida.append(objeto)
    return salida


def _item_de_entrega(almacen, entrega):
    objeto = durable.leer(almacen, "paquetes/" + str(entrega.get("paquete")) + ".json")
    return objeto["item"] if objeto else None


# ===========================================================================
#  PLANIFICAR: de una entrada a paquetes por rol
# ===========================================================================
def planificar(runtime, *, corpus=None, entrada, circuito, control_repo, fase="unica",
               item=None, titulo=None, acoplamiento_por_capacidad=None,
               acoplamiento_por_rol=None, slots=4,
               ordenes=None, capacidades_de_adaptador_por_rol=None, degradaciones=None,
               secuencial=None, precondiciones=(), generacion=0):
    """Encuadra, compone, materializa y planifica POR ROL. Fallo cerrado en cada etapa.

    `ordenes(capacidad, rol)` devuelve la orden de adaptador de cada paquete: la instancia
    decide si un rol lo ejecuta un trabajador que reclama (`worker`) o un agente sin chat
    (`agente`). Sin función, todos los paquetes nacen externos.
    """
    corpus = corpus or Corpus()
    from runtime.externo import orden_externa, CAPACIDAD_EXTERNA       # noqa: PLC0415

    def orden_por_defecto(capacidad, rol):
        return orden_externa(argumentos=[capacidad, rol or ""])

    ordenes = ordenes or orden_por_defecto
    independencias_declaradas = {
        str(regla["rol"]): [str(d) for d in (regla.get("de") or [])]
        for regla in (circuito.get("independencias") or [])
    }
    anterior = plan_vigente_de_item(runtime.almacen, item) if item else None
    entrada = dict(entrada)
    entrada.setdefault("materia", circuito["materia"])
    entrada.setdefault("estado_del_objeto", circuito["estado_del_objeto"])
    marco = modulo_encuadre.encuadrar(control_repo, entrada, corpus=corpus,
                                      precondiciones=precondiciones)
    modulo_encuadre.exigir_que_crea_trabajo(marco)
    # `proceso:DIR` DERIVA su propietario global del encargo (`01-PROCESOS.md`, `b.16`): la
    # entrada lo trae en `propietario_global` y aquí se entrega a la composición. Antes no
    # se pasaba y ningún cambio de dirección se podía planificar desde la oficina.
    ruta = modulo_rutas.componer(
        marco, corpus=corpus, fase=fase,
        condiciones_verdaderas=list(circuito.get("condiciones_de_ruta") or []),
        propietario_declarado=(str(entrada.get("propietario_global")).strip()
                               if entrada.get("propietario_global") else None),
        productores_declarados={str(k): str(v) for k, v in
                                (entrada.get("productores_declarados") or {}).items()},
    )
    equipos, roles_por_capacidad = [], {}
    for capacidad in sorted({p["capacidad"] for p in ruta["participantes"]}):
        equipo = modulo_equipos.materializar(
            capacidad, corpus=corpus,
            composiciones_verdaderas=list(circuito.get("composiciones") or []),
            slots=slots, control_repo=control_repo, degradaciones=degradaciones,
            paquete=item,
        )
        if equipo.get("estado") == modulo_equipos.EQUIPO_BLOQUEADO:
            faltan = [b["rol"] + ": " + "; ".join(b.get("falta") or []) for b in equipo["bloqueados"]]
            raise RolSinAgente(
                "el equipo de `" + capacidad + "` queda BLOQUEADO: " + " | ".join(faltan)
                + ". Sin agente para un rol no se planifica: el catálogo de modelos del "
                "PROFILE tiene que cubrir cada perfil, o declararse una degradación",
                capacidad=capacidad, bloqueados=[b["rol"] for b in equipo["bloqueados"]],
            )
        equipos.append(equipo)
        orden_de_composicion = _orden_de_roles(corpus, capacidad, equipo["composicion"])
        presentes = {r["rol"] for r in equipo["roles"]} | {
            r["rol"] for r in equipo.get("esperando_capacidad") or []}
        roles_por_capacidad[capacidad] = [r for r in orden_de_composicion if r in presentes]
    # Circuito base: todo rol mínimo tiene que estar materializado en alguna capacidad.
    materializados = {r for roles in roles_por_capacidad.values() for r in roles}
    faltan = [r for r in (circuito.get("roles_minimos") or []) if r not in materializados]
    if faltan:
        raise CicloInconsistente(
            "el circuito base `" + circuito["id"] + "` exige los roles " + ", ".join(faltan)
            + " y la ruta compuesta no los materializa; o la ruta activa la capacidad que "
            "los trae, o el circuito no es el de este trabajo",
        )
    planificador = planificacion.Planificador(runtime, corpus=corpus)
    capacidades = sorted(roles_por_capacidad)
    plan = planificador.planificar(
        marco, ruta, equipos=equipos, item=item, titulo=titulo,
        orden_por_capacidad={c: ordenes(c, None) for c in capacidades},
        orden_por_rol={r: ordenes(c, r) for c, roles in roles_por_capacidad.items() for r in roles},
        roles_por_capacidad=roles_por_capacidad,
        capacidades_de_adaptador=(CAPACIDAD_EXTERNA,),
        capacidades_de_adaptador_por_rol=capacidades_de_adaptador_por_rol,
        acoplamiento_por_capacidad=acoplamiento_por_capacidad,
        acoplamiento_por_rol=acoplamiento_por_rol, slots=slots,
        secuencial=secuencial, independencias_declaradas=independencias_declaradas,
        generacion=generacion,
    )
    if generacion and anterior is not None and anterior["id"] != plan["id"]:
        # REPLANIFICAR: el plan nuevo sustituye al vigente —con su marca de impacto, si la
        # tenía— y desde aquí el vigente es el nuevo (`plan_vigente_de_item`).
        sustituto = dict(plan, sustituye_a=anterior["id"])
        durable.escribir(
            runtime.almacen, clase="ciclo.plan.sustituido",
            motivo="el plan " + plan["id"] + " (generación " + str(generacion) + ") sustituye a " + anterior["id"],
            objetos={planificacion.ruta_de(plan["id"]): sustituto},
        )
        plan = sustituto
    return {"encuadre": marco, "ruta": ruta, "equipos": equipos, "plan": plan}


def _orden_de_roles(corpus, capacidad, composicion_id):
    for composicion in corpus.composiciones(capacidad):
        if composicion["id"] == composicion_id:
            return [str(e["rol"]) for e in composicion.get("roles") or []]
    return []


# ===========================================================================
#  TOMAR, con brief
# ===========================================================================
def brief_de(runtime, *, corpus=None, paquete, item_datos=None, circuito=None, ordenes=None,
             instrucciones=(), fuentes=()):
    corpus = corpus or Corpus()
    almacen = runtime.almacen
    objeto = durable.leer(almacen, "paquetes/" + paquete + ".json")
    if objeto is None:
        raise CicloInconsistente("no hay paquete `" + paquete + "`", ruta=paquete)
    plan, fila = plan_de_paquete(almacen, paquete)
    if plan is None or fila is None:
        raise CicloInconsistente(
            "el paquete `" + paquete + "` no está en ningún plan vigente: no se puede decir "
            "qué rol lo ejecuta ni contra qué gate cierra", ruta=paquete,
        )
    if not fila.get("rol"):
        raise CicloInconsistente(
            "la fila del plan del paquete `" + paquete + "` no declara rol: fue planificado "
            "sin `roles_por_capacidad` y la oficina exige paquetes por rol", ruta=paquete,
        )
    equipo = equipo_de(almacen, plan, fila["capacidad"])
    item_base = durable.leer(almacen, "items/" + objeto["item"] + ".json") or {}
    item_completo = dict(item_base)
    item_completo.update(item_datos or {})
    from runtime.externo import leer_checkpoint                        # noqa: PLC0415
    brief = briefs.componer(
        corpus=corpus, paquete=paquete, item=item_completo, fila_del_plan=fila,
        rol=fila["rol"], equipo=agente_del_rol(equipo, fila["rol"]),
        intento=int(objeto.get("intentos") or 0) or 1, efecto=objeto.get("efecto"),
        handoffs_pendientes=handoffs_pendientes_para(almacen, paquete),
        entregas_previas=entregas_del_item(almacen, objeto["item"]),
        checkpoint=leer_checkpoint(runtime, paquete), circuito=circuito,
        instrucciones_del_proyecto=instrucciones, ordenes=ordenes, fuentes=fuentes,
    )
    return brief


def tomar(runtime, *, corpus=None, paquete, **opciones_del_brief):
    """`Runtime.tomar` y el brief. Si hay una entrega emitida a este paquete, la lista.

    DEFECTO MEDIDO (`T461`, primera versión): se tomaba el lease y DESPUÉS se derivaba el
    brief; un paquete sin plan fallaba con `CICLO_INCONSISTENTE` dejando el lease en manos de
    quien no iba a trabajarlo. Ahora la pertenencia a un plan se exige ANTES de tomar, y si
    el brief falla por cualquier otra causa el lease se SUELTA antes de propagar el error.
    """
    plan, fila = plan_de_paquete(runtime.almacen, paquete)
    if plan is None or fila is None:
        raise CicloInconsistente(
            "el paquete `" + paquete + "` no está en ningún plan vigente: no se toma lo que "
            "no tiene rol ni gate", ruta=paquete,
        )
    _exigir_que_no_juzgue_lo_suyo(runtime, corpus or Corpus(), paquete, fila,
                                  opciones_del_brief.get("circuito"))
    marca = modulo_impacto.pendiente(plan)
    if marca and marca.get("paquete") != paquete:
        raise ImpactoNoCubierto(
            "el item `" + str(plan.get("item")) + "` tiene impacto sin cubrir: " + marca["rol"] + " declaró "
            + ", ".join(marca["disparadores"]) + " y el circuito no cubre " + ", ".join(marca["condiciones_no_cubiertas"])
            + ". No se toma ningún otro paquete hasta replanificar (§5, b.1)", ruta=paquete,
        )
    toma = runtime.tomar(paquete)
    try:
        brief = brief_de(runtime, corpus=corpus, paquete=paquete, **opciones_del_brief)
    except Exception:
        runtime.soltar(paquete)
        raise
    # LA BASE DE PARTIDA (Directiva §61, §63; OWN-ADS-0220, 0227): al nacer el trabajo se
    # conserva, por repo medible, la rama, de qué commit nace y qué base hay. Es el
    # checkpoint 0, bajo el lease recién adquirido; en un laboratorio sin Git no se escribe.
    base = None
    if toma.get("checkpoint") is None:
        evaluacion = modulo_base.evaluar(runtime.ruta)
        if evaluacion["veredicto"] != modulo_base.NO_MEDIBLE:
            nacimiento = modulo_base.nacimiento_de(evaluacion["medidas"])
            base = modulo_base.resumen(evaluacion, nacimiento)
            runtime.checkpoint(paquete, {"paso": 0, "base": base})
    else:
        base = (toma["checkpoint"].get("contenido") or {}).get("base")
    return {"toma": toma, "brief": brief, "brief_md": briefs.como_markdown(brief), "base": base}


def _nacimiento_de(runtime, paquete):
    from runtime.externo import leer_checkpoint                        # noqa: PLC0415
    previo = leer_checkpoint(runtime, paquete)
    return (((previo or {}).get("contenido") or {}).get("base") or {}).get("nacimiento")


def checkpoint(runtime, *, paquete, contenido, corpus=None):
    """`Runtime.checkpoint` MIRANDO LA BASE (Directiva §63; OWN-ADS-0227, 0229, 0230).

    Cada checkpoint mide otra vez el control repo y las fuentes: si la base avanzó sobre
    otra cosa, `compatible` y la base nueva queda registrada; si avanzó sobre lo mismo que
    este trabajo cambió, `contradiccion`, y el checkpoint se escribe igual —el latido no se
    pierde— con los ficheros en conflicto, para que el trabajador reconcilie en su rama o
    entregue `bloqueado`. `entregar` no admite `entregado` con una contradicción vigente.
    """
    del corpus
    contenido = dict(contenido or {})
    nacimiento = _nacimiento_de(runtime, paquete)
    evaluacion = modulo_base.evaluar(runtime.ruta, nacimiento=nacimiento)
    if evaluacion["veredicto"] != modulo_base.NO_MEDIBLE or nacimiento:
        contenido["base"] = modulo_base.resumen(
            evaluacion, nacimiento or modulo_base.nacimiento_de(evaluacion["medidas"]))
    return runtime.checkpoint(paquete, contenido)


def _exigir_que_no_juzgue_lo_suyo(runtime, corpus, paquete, fila, circuito=None):
    """G13 en la PUERTA: quien produjo lo que este paquete va a juzgar no lo toma.

    DEFECTO MEDIDO (dogfood de La Pesquerapp, evidencia 23-24): la autocertificación se
    rechazaba al ENTREGAR, y para entonces el lease ya era del que no podía juzgar; el
    revisor legítimo recibía AUTORIDAD_NO_DISPONIBLE hasta que aquél soltara. Ahora se
    rechaza antes de tomar, y no queda lease detrás.
    """
    from . import entregas as modulo_entregas                          # noqa: PLC0415
    rol = fila.get("rol")
    if not rol:
        return
    independiente_de = set((corpus.rol(rol).get("independencia") or {}).get("de_quien") or [])
    for regla in (circuito or {}).get("independencias") or []:
        if str(regla.get("rol")) == rol:
            independiente_de.update(str(d) for d in (regla.get("de") or []))
    if not independiente_de:
        return
    objeto = runtime._leer_paquete(paquete) or {}
    recibidos = [h for h in handoffs_del_item(runtime.almacen, str(objeto.get("item") or ""))
                 if (h.get("trazabilidad") or {}).get("destino") == paquete
                 and h.get("estado") in (handoffs.EMITIDO, handoffs.ACUSADO)]
    for pendiente in recibidos:
        emisor = str((pendiente.get("trazabilidad") or {}).get("paquete") or "")
        if not emisor:
            continue
        entrega = modulo_entregas.ultima(runtime.almacen, emisor)
        if entrega is None or entrega.get("titular") != runtime.instancia:
            continue
        if entrega.get("rol") in independiente_de:
            raise AutocertificacionRechazada(
                "`" + runtime.instancia + "` produjo la entrega de `" + emisor + "` como "
                + str(entrega.get("rol")) + " y quiere tomar `" + paquete + "` como " + rol
                + ", que exige independencia de ese rol: G13 no admite que quien construye "
                "sea quien juzga. Otra instancia tiene que tomarlo",
                paquete=paquete, titular=runtime.instancia,
            )
    # Y no sólo lo que llega por handoff: TODO lo que esta instancia entregó para el item en
    # un rol del que hay que ser independiente. DEFECTO MEDIDO (quinto dogfood, tres
    # workers): quien hizo la CORRECCIÓN de la implementación pasaba la puerta de VER/dosier
    # —el handoff a VER venía de la implementación original, de otro— y la entrega se le
    # rechazaba después por dictaminar lo suyo, consumiendo un intento del paquete.
    plan, _fila = plan_de_paquete(runtime.almacen, paquete)
    for fila_del_plan in (plan or {}).get("correspondencia") or []:
        otro = str(fila_del_plan.get("paquete") or "")
        if not otro or otro == paquete:
            continue
        entrega = modulo_entregas.ultima(runtime.almacen, otro)
        if entrega is None or entrega.get("titular") != runtime.instancia:
            continue
        if entrega.get("rol") in independiente_de:
            raise AutocertificacionRechazada(
                "`" + runtime.instancia + "` entregó `" + otro + "` como "
                + str(entrega.get("rol")) + " para este item y quiere tomar `" + paquete
                + "` como " + rol + ", que exige independencia de ese rol: G13 no admite que "
                "quien construye sea quien juzga. Otra instancia tiene que tomarlo",
                paquete=paquete, titular=runtime.instancia,
            )


# ===========================================================================
#  ACUSAR y RECHAZAR una entrega recibida
# ===========================================================================
def _escribir_handoff(almacen, entrega, *, autor, clase, motivo):
    durable.escribir(
        almacen, clase=clase, motivo=motivo,
        objetos={handoffs.ruta_de(entrega["id"]): entrega},
        semilla={"handoff": entrega["id"], "estado": entrega["estado"]}, autor=autor,
    )
    return entrega


def acusar(runtime, *, corpus=None, handoff, comprobaciones_superadas):
    almacen = runtime.almacen
    entrega = durable.leer(almacen, handoffs.ruta_de(handoff))
    if entrega is None:
        raise CicloInconsistente("no hay handoff `" + str(handoff) + "`", ruta=str(handoff))
    nueva = handoffs.acusar(entrega, comprobaciones_superadas=comprobaciones_superadas,
                            receptor=entrega["a"])
    return _escribir_handoff(almacen, nueva, autor=runtime.instancia,
                             clase="ciclo.handoff.acusado",
                             motivo="acuse de " + nueva["id"] + " por " + runtime.instancia)


def rechazar(runtime, *, corpus=None, handoff, motivo, paquete_receptor):
    """Rechazo ANTES de tomar custodia: corrección para el emisor, y el receptor se reabre."""
    corpus = corpus or Corpus()
    almacen = runtime.almacen
    entrega = durable.leer(almacen, handoffs.ruta_de(handoff))
    if entrega is None:
        raise CicloInconsistente("no hay handoff `" + str(handoff) + "`", ruta=str(handoff))
    nueva = handoffs.rechazar(entrega, receptor=entrega["a"], motivo=motivo)
    _escribir_handoff(almacen, nueva, autor=runtime.instancia,
                      clase="ciclo.handoff.rechazado",
                      motivo="rechazo de " + nueva["id"] + ": " + str(motivo)[:120])
    plan, fila = plan_de_paquete(almacen, paquete_receptor)
    emisor = str(entrega["trazabilidad"]["paquete"])
    correccion = _abrir_correccion(runtime, corpus, plan, emisor=emisor,
                                   receptor=paquete_receptor,
                                   motivo="rechazo al recibir: " + str(motivo),
                                   cuenta_para_el_freno=False)
    # El paquete receptor vigente ya no puede seguir: su entrada fue rechazada. Se cancela
    # con la autoridad de la capacidad receptora, y el reemplazo espera a la corrección.
    runtime.cancelar(paquete_receptor, motivo="su entrada `" + emisor + "` fue rechazada al "
                     "recibir; lo sustituye " + correccion["receptor"],
                     autoridad=entrega["a"])
    runtime._soltar_si_es_mio(paquete_receptor)
    return {"handoff": nueva, **correccion}


# ===========================================================================
#  ENTREGAR
# ===========================================================================
def entregar(runtime, *, corpus=None, paquete, entrega, circuito=None, hechos=None):
    """Valida, publica, registra, dictamina, entrega o devuelve. En este orden, y no otro."""
    corpus = corpus or Corpus()
    almacen = runtime.almacen
    objeto = durable.leer(almacen, "paquetes/" + paquete + ".json")
    if objeto is None:
        raise CicloInconsistente("no hay paquete `" + paquete + "`", ruta=paquete)
    plan, fila = plan_de_paquete(almacen, paquete)
    if plan is None or fila is None or not fila.get("rol"):
        raise CicloInconsistente("el paquete `" + paquete + "` no tiene fila con rol en un "
                                 "plan vigente", ruta=paquete)
    # LA AUTORIDAD, ANTES DE ESCRIBIR NADA. Entregar son varias transacciones —dictamen,
    # devolución, corrección, publicación, registro, handoffs— y sólo la publicación (4)
    # exigía titularidad. MEDIDO (sexto dogfood): un supervisor reclamó el lease de un
    # worker vivo pero lento; el worker ya había escrito el dictamen, la devolución y la
    # corrección cuando la publicación le dijo AUTORIDAD_PERDIDA. Lo escrito a medias era
    # idempotente, pero a medias. Sin lease no se escribe ni la primera.
    from runtime.lease import exigir_titularidad                       # noqa: PLC0415
    exigir_titularidad(runtime._leer_lease(paquete), runtime.instancia, None, paquete=paquete)
    # NO EXISTE «seguimos» como transferencia implícita (Directiva §78; OWN-ADS-0280): lo que
    # este paquete recibió se acusa —o se rechaza— ANTES de entregar. Un receptor que entrega
    # con un handoff en `emitido` nunca tomó custodia de lo que dice haber usado.
    sin_acusar = handoffs_pendientes_para(almacen, paquete)
    if sin_acusar:
        raise EntregaInvalida(
            "hay " + str(len(sin_acusar)) + " handoff(s) recibido(s) sin acusar ni rechazar ("
            + ", ".join(h["id"] for h in sin_acusar) + "): se acusa o se rechaza ANTES de "
            "entregar; no existe «seguimos» como transferencia implícita", paquete=paquete,
        )
    if entrega.get("paquete") != paquete:
        raise EntregaInvalida("la entrega dice ser de `" + str(entrega.get("paquete"))
                              + "` y se entrega sobre `" + paquete + "`", paquete=paquete)
    if entrega.get("rol") != fila["rol"]:
        raise EntregaInvalida("la entrega la firma el rol `" + str(entrega.get("rol"))
                              + "` y el paquete es de `" + fila["rol"] + "`", paquete=paquete)
    contrato = corpus.contrato_operativo_de(fila["rol"])
    entregas.exigir_forma(entrega, corpus=corpus, contrato=contrato, gate=fila.get("gate"))
    veredicto = entrega["veredicto"]
    intento = int(objeto.get("intentos") or 1)
    item = objeto["item"]

    # 1 · un DICTAMEN, si el rol juzga. Antes de publicar nada: un dictamen que no cabe
    #     invalida la entrega entera.
    dictamenes_emitidos = []
    declarados = list(entrega.get("dictamenes") or [])
    if any(d.get("gate") == GATE_DE_CONVERGENCIA for d in declarados):
        _exigir_integration_set(corpus, entrega, hechos or {}, paquete)
    if entrega.get("dictamen"):
        declarados.append(entrega["dictamen"])
    for datos in declarados:
        cuerpo = _dictaminar(runtime, corpus, plan, fila, paquete, datos)
        dictamenes_emitidos.append(cuerpo)
    if veredicto == "entregado" and any(d["dictamen"] != gates.SUPERADO for d in dictamenes_emitidos):
        raise EntregaInvalida(
            "la entrega dice `entregado` y alguno de sus dictámenes es `no-superado`: un "
            "revisor que no supera un gate DEVUELVE, no entrega", paquete=paquete,
        )
    if veredicto == "devuelto" and dictamenes_emitidos and all(
            d["dictamen"] == gates.SUPERADO for d in dictamenes_emitidos):
        raise EntregaInvalida(
            "la entrega dice `devuelto` y todos sus dictámenes son `superado`: las dos "
            "cosas no pueden ser ciertas a la vez", paquete=paquete,
        )
    dictamen = dictamenes_emitidos[-1] if dictamenes_emitidos else None

    # 1 bis · el impacto declarado se contrasta con el circuito ANTES de escribir nada: un
    #         disparador fuera de los dieciséis de §5 es una entrega inválida sin efecto.
    impacto = None
    if entrega.get("impacto"):
        impacto = modulo_impacto.evaluar(circuito, entrega["impacto"], paquete=paquete)

    # 1 ter · LA BASE (Directiva §63; OWN-ADS-0231): antes de escribir nada, si el mundo
    #         cambió debajo sobre lo mismo que este paquete tocó, no se entrega `entregado`
    #         como si no hubiera pasado. Se reconcilia en la rama, o se entrega `bloqueado`
    #         (dependencia interna: espera). Un laboratorio sin Git no mide y no frena.
    if veredicto == "entregado":
        nacimiento = _nacimiento_de(runtime, paquete)
        evaluacion_de_base = modulo_base.evaluar(runtime.ruta, nacimiento=nacimiento)
        if evaluacion_de_base["veredicto"] == modulo_base.CONTRADICCION:
            raise BaseContradicha(
                "la base avanzó sobre lo mismo que este paquete cambió —"
                + modulo_base.frase(evaluacion_de_base["conflictos"]) + "—: no se entrega "
                "`entregado` sobre una realidad obsoleta (§63). Reconcilia la rama con la base "
                "y vuelve a entregar, o entrega `bloqueado` con clase dependencia-interna",
                paquete=paquete,
            )
        if evaluacion_de_base["veredicto"] != modulo_base.NO_MEDIBLE or nacimiento:
            runtime.checkpoint(paquete, {"paso": "entrega", "base": modulo_base.resumen(
                evaluacion_de_base, nacimiento or modulo_base.nacimiento_de(evaluacion_de_base["medidas"]))})

    # 2 · BLOQUEADO / ESCALADO: el paquete queda `bloqueado`, no consume intento.
    if veredicto in ("bloqueado", "escalado"):
        registrada = entregas.registrar(almacen, entrega, intento=intento,
                                        titular=runtime.instancia, corpus=corpus,
                                        contrato=contrato)
        runtime.checkpoint(paquete, {"bloqueo": entrega["bloqueo"], "entrega": registrada["id"]})
        runtime.bloquear(paquete, motivo=entrega["bloqueo"]["que_lo_impide"],
                         autoridad=fila["capacidad"],
                         clase_de_bloqueo=(entrega["bloqueo"].get("clase") if veredicto == "bloqueado" else "decision"))
        runtime._soltar_si_es_mio(paquete)
        cierre = modulo_cierre.Cierre(runtime, corpus=corpus)
        if veredicto == "bloqueado":
            salida = cierre.bloquear(plan, motivo=entrega["bloqueo"]["que_lo_impide"],
                                     trabajo_de_reemplazo=entrega["bloqueo"]["que_lo_desbloquearia"])
        else:
            salida = cierre.escalar(plan, motivo=entrega["bloqueo"]["que_lo_impide"],
                                    autoridad=entrega["bloqueo"]["autoridad"],
                                    posturas=entrega["bloqueo"].get("posturas") or [])
        return {"veredicto": veredicto, "entrega": registrada, "paquete": paquete,
                "cierre": salida, "dictamen": dictamen}

    # 3 · DEVUELTO: la corrección y el nuevo receptor se abren ANTES de cerrar este paquete,
    #     para que ningún sucesor pueda volverse elegible sobre una capa devuelta.
    correccion = None
    if veredicto == "devuelto":
        correccion = _devolver(runtime, corpus, plan, fila, paquete, entrega)

    # 4 · PUBLICAR por el dispatcher: resultado, acuse y latido en una transición.
    resumen = runtime.entregar(paquete, {
        "estado": "completado", "codigo": 0,
        "salida": entregas.identificador(paquete, intento),
        "detalle": "entrega del rol " + fila["rol"] + " · " + veredicto,
        "reintentable": False,
    })
    registrada = entregas.registrar(almacen, entrega, intento=intento,
                                    titular=runtime.instancia, corpus=corpus,
                                    contrato=contrato)

    # 4 bis · LA ESTACIÓN DE IMPACTO (§5): lo que este rol vio y el circuito no preveía
    #         marca el plan; el resto del item se para hasta replanificar (b.1). El
    #         vocabulario se comprobó ANTES de escribir nada (arriba).
    if impacto is not None:
        if impacto["no_cubiertas"]:
            marcado = dict(plan)
            marcado["impacto"] = modulo_impacto.marca_del_plan(impacto, paquete=paquete, rol=fila["rol"],
                                                              entrega=registrada["id"])
            durable.escribir(
                almacen, clase="ciclo.plan.impacto",
                motivo="impacto sin cubrir declarado por " + fila["rol"] + " en " + paquete + ": "
                       + ", ".join(impacto["no_cubiertas"]),
                objetos={planificacion.ruta_de(plan["id"]): marcado},
            )
    # 5 · ENTREGADO: handoffs a los sucesores.
    emitidos = []
    if veredicto == "entregado":
        emitidos = _emitir_a_sucesores(runtime, corpus, plan, fila, paquete, registrada)
    return {"veredicto": veredicto, "entrega": registrada, "paquete": paquete, "impacto": impacto,
            "resumen": resumen, "dictamen": dictamen, "dictamenes": dictamenes_emitidos,
            "handoffs_emitidos": emitidos, "correccion": correccion}


def _autor_de(almacen, paquete_juzgado):
    ultima = entregas.ultima(almacen, paquete_juzgado)
    return str(ultima.get("titular") or "") if ultima else ""


GATE_DE_CONVERGENCIA = "gate:convergencia-de-fuentes"
ESTADOS_CONVERGENTES = ("verificado", "integrado")


def _exigir_integration_set(corpus, entrega, hechos, paquete):
    """Un dictamen de convergencia sólo entra con un Integration Set EXACTO y COMPLETO.

    `C7`: la convergencia se declara con la revisión exacta de cada fuente, probada
    conjuntamente. Aquí se comprueba mecánicamente lo que el gate declara: la forma
    canónica, que nombra todas las fuentes que el item escribe (`hechos.fuentes_escritas`),
    que ninguna entra dos veces, que la verificación no tiene pendientes ni fallos y que el
    estado no es parcial. Sin eso, `integrado` sería una palabra.
    """
    conjunto = entrega.get("integration_set")
    if not isinstance(conjunto, dict):
        raise EntregaInvalida(
            "un dictamen de `" + GATE_DE_CONVERGENCIA + "` exige el Integration Set ENTERO en "
            "`integration_set`; sin conjunto no hay convergencia que dictaminar", paquete=paquete,
        )
    fallos = list(formas.validar(conjunto, corpus.esquema("integration-set"), corpus=corpus,
                                 camino="integration_set"))
    fuentes = [str(f.get("source")) for f in (conjunto.get("fuentes") or []) if isinstance(f, dict)]
    if len(set(fuentes)) != len(fuentes):
        fallos.append("integration_set.fuentes: una fuente entra dos veces")
    escritas = [str(f) for f in (hechos.get("fuentes_escritas") or [])]
    faltan = [f for f in escritas if f not in fuentes]
    if faltan:
        fallos.append("integration_set.fuentes: el item escribe " + ", ".join(faltan)
                      + " y el conjunto no las nombra: integración PARCIAL, que no es terminado")
    if conjunto.get("estado") not in ESTADOS_CONVERGENTES:
        fallos.append("integration_set.estado: `" + str(conjunto.get("estado")) + "` no es un estado "
                      "convergente (" + ", ".join(ESTADOS_CONVERGENTES) + ")")
    for fila in conjunto.get("verificacion") or []:
        if isinstance(fila, dict) and fila.get("resultado") not in ("pasa", "no-aplica"):
            fallos.append("integration_set.verificacion: el ámbito `" + str(fila.get("ambito"))
                          + "` está `" + str(fila.get("resultado")) + "`: no está probado conjuntamente")
    fallos.extend(_fallos_de_71(conjunto, fuentes))
    if fallos:
        raise EntregaInvalida("la convergencia no es admisible: " + "; ".join(fallos), paquete=paquete)


def _fallos_de_71(conjunto, fuentes):
    """Directiva §71: con VARIAS fuentes, el conjunto define el orden de merge, la
    compatibilidad, el despliegue y las dependencias; con una, son triviales."""
    fallos = []
    conocidas = set(fuentes)
    orden = conjunto.get("orden_de_merge")
    despliegue = conjunto.get("despliegue")
    compatibilidad = conjunto.get("compatibilidad")
    if len(conocidas) > 1:
        if not orden:
            fallos.append("integration_set.orden_de_merge: el bloque toca " + ", ".join(sorted(conocidas))
                          + " y el conjunto no dice en qué orden se fusionan (§71)")
        if not despliegue:
            fallos.append("integration_set.despliegue: el bloque toca varias fuentes y el conjunto no "
                          "dice cómo ni en qué orden se despliegan (§71)")
        if not compatibilidad:
            fallos.append("integration_set.compatibilidad: el bloque toca varias fuentes y el conjunto no "
                          "dice qué combinación de revisiones es compatible (§71)")
    if orden:
        nombrados = [str(f) for f in orden]
        if sorted(nombrados) != sorted(fuentes):
            fallos.append("integration_set.orden_de_merge: nombra " + ", ".join(nombrados) + " y las fuentes "
                          "del conjunto son " + ", ".join(fuentes) + ": cada una UNA vez, y ninguna ajena")
    if despliegue:
        desplegadas = [str(f.get("source")) for f in despliegue if isinstance(f, dict)]
        faltan = sorted(conocidas - set(desplegadas))
        ajenas = sorted(set(desplegadas) - conocidas)
        if faltan:
            fallos.append("integration_set.despliegue: no dice cómo se despliega " + ", ".join(faltan))
        if ajenas:
            fallos.append("integration_set.despliegue: nombra fuentes que el conjunto no tiene: " + ", ".join(ajenas))
        ordenes = [f.get("orden") for f in despliegue if isinstance(f, dict)]
        if len(set(ordenes)) != len(ordenes):
            fallos.append("integration_set.despliegue: dos fuentes con el mismo `orden`: el despliegue no es una secuencia")
    for fila in compatibilidad or []:
        if not isinstance(fila, dict):
            continue
        ajenas = sorted(set(str(x) for x in (fila.get("entre") or [])) - conocidas)
        if ajenas:
            fallos.append("integration_set.compatibilidad: `entre` nombra fuentes que el conjunto no tiene: "
                          + ", ".join(ajenas))
    return fallos


def _dictaminar(runtime, corpus, plan, fila, paquete, datos):
    """Un dictamen de un gate, emitido por el rol que juzga, sobre un paquete ANTERIOR del plan."""
    almacen = runtime.almacen
    juzgado = str(datos["sobre_paquete"])
    _plan_j, fila_j = plan_de_paquete(almacen, juzgado)
    if fila_j is None or _plan_j["item"] != plan["item"]:
        raise EntregaInvalida(
            "el dictamen juzga `" + juzgado + "`, que no es un paquete del mismo item",
            paquete=paquete,
        )
    if juzgado == paquete:
        raise AutocertificacionRechazada(
            "el paquete `" + paquete + "` se dictamina a sí mismo", gate=datos["gate"],
        )
    autor_titular = _autor_de(almacen, juzgado)
    if autor_titular and autor_titular == runtime.instancia:
        raise AutocertificacionRechazada(
            "`" + runtime.instancia + "` produjo la entrega de `" + juzgado + "` y quiere "
            "dictaminarla: G13 no admite que quien construye sea quien juzga",
            gate=datos["gate"], titular=runtime.instancia,
        )
    entrada = {
        "item": plan["item"], "sobre_paquete": juzgado, "paquete_revisor": paquete,
        "autor_titular": autor_titular, "revisor_titular": runtime.instancia,
        "rol_revisor": fila["rol"], "rol_autor": fila_j.get("rol"),
        "entrega_revisora": entregas.identificador(paquete, int(durable.leer(
            almacen, "paquetes/" + paquete + ".json").get("intentos") or 1)),
    }
    # Revisor y autor se declaran por ROL cuando lo hay: es la granularidad a la que la
    # oficina separa a quien construye de quien juzga (`gates._exigir_revisor`).
    comun = dict(entrada=entrada, evidencia=list(datos.get("evidencia") or []),
                 revisor=fila.get("rol") or fila["capacidad"],
                 autor=fila_j.get("rol") or fila_j["capacidad"], corpus=corpus,
                 comprobaciones_superadas=list(datos.get("comprobaciones_superadas") or []),
                 hallazgos=list(datos.get("hallazgos") or []))
    try:
        cuerpo = gates.aplicar(datos["gate"], salida="dictamen del rol " + fila["rol"], **comun)
    except GateFallido as error:
        cuerpo = getattr(error, "dictamen", None)
        if cuerpo is None:
            raise
    if datos["dictamen"] != cuerpo["dictamen"]:
        raise EntregaInvalida(
            "la entrega declara el dictamen `" + datos["dictamen"] + "` y el gate `"
            + datos["gate"] + "` recorrido dice `" + cuerpo["dictamen"] + "`: pendientes "
            + ", ".join(cuerpo["comprobaciones_pendientes"]) + "; evidencia ausente "
            + ", ".join(cuerpo["evidencia_ausente"]), paquete=paquete,
        )
    durable.escribir(
        almacen, clase="ciclo.dictamen." + cuerpo["dictamen"],
        motivo="dictamen de " + datos["gate"] + " sobre " + juzgado + " por " + runtime.instancia,
        objetos={gates.ruta_de(cuerpo["id"]): cuerpo}, semilla={"dictamen": cuerpo["id"]},
        autor=runtime.instancia,
    )
    return cuerpo


def _sucesores(plan, paquete):
    return [f for f in plan.get("correspondencia") or []
            if paquete in (f.get("depende_de") or [])]


def _emitir_a_sucesores(runtime, corpus, plan, fila, paquete, registrada):
    almacen = runtime.almacen
    emitidos = []
    for sucesor in _sucesores(plan, paquete):
        de, a = fila["capacidad"], sucesor["capacidad"]
        identificador = "handoff:" + _slug(de) + "-a-" + _slug(a)
        catalogo = handoffs.catalogo(corpus)
        declarada = catalogo.get(identificador) or handoffs.generica(de, a, corpus=corpus)
        artefactos = [a_["tipo"] + ":" + a_["referencia"] for a_ in registrada["artefactos"]]
        cuerpo = handoffs.emitir(
            declarada["id"], artefactos=artefactos, checkpoint=str(registrada["siguiente"]),
            trazabilidad={"item": plan["item"], "paquete": paquete, "ruta": plan["ruta"],
                          "encuadre": plan["encuadre"], "destino": sucesor["paquete"],
                          "entrega": registrada["id"]},
            corpus=corpus, declarada=declarada,
            contenido=_contenido_de_78(almacen, plan, fila, paquete, sucesor, registrada, declarada),
        )
        _escribir_handoff(almacen, cuerpo, autor=runtime.instancia,
                          clase="ciclo.handoff.emitido",
                          motivo="entrega de " + paquete + " a " + sucesor["paquete"])
        emitidos.append(cuerpo["id"])
    return emitidos


def _contenido_de_78(almacen, plan, fila, paquete, sucesor, registrada, declarada):
    """Los CATORCE campos de §78, DERIVADOS: de la entrega registrada, del plan, del item y de
    lo que este paquete acusó. La correspondencia está escrita en CONTRATO-OFICINA §4."""
    item = durable.leer(almacen, "items/" + str(plan["item"]) + ".json") or {}
    acusados = [h["id"] for h in handoffs_del_item(almacen, str(plan["item"]))
                if (h.get("trazabilidad") or {}).get("destino") == paquete and h.get("estado") == handoffs.ACUSADO]
    receptor_rol = str(sucesor.get("rol") or sucesor.get("capacidad") or "")
    return {
        "origen": {"capacidad": fila["capacidad"], "rol": fila.get("rol"), "paquete": paquete},
        "destino": {"capacidad": sucesor["capacidad"], "rol": receptor_rol, "paquete": sucesor["paquete"]},
        "paquete": paquete,
        "objetivo": str(item.get("objetivo") or ""),
        "entrada_recibida": acusados,
        "trabajo_realizado": {"entrega": registrada["id"], "veredicto": registrada["veredicto"],
                              "siguiente": registrada.get("siguiente")},
        "entregables": [dict(a) for a in registrada["artefactos"]],
        "decisiones": list(registrada.get("decisiones_asumidas") or []),
        "riesgos": list(registrada.get("riesgos") or []),
        "evidencia": [dict(e) for e in registrada.get("evidencias") or []],
        "criterios_de_aceptacion": {"comprueba_al_recibir": list(declarada["comprueba_al_recibir"]),
                                    "gate_del_emisor": (registrada.get("autoevaluacion") or {}).get("gate")},
        "deuda": [dict(d) for d in registrada.get("deuda_aceptada") or []],
        "cuestiones_abiertas": list(registrada.get("no_hecho") or []) + list(registrada.get("diferencias_declaradas") or []),
        "que_puede_devolver_el_receptor": {"rechaza_si": list(declarada["rechaza_si"]),
                                           "devolucion": str(declarada["devolucion"])},
    }


# ===========================================================================
#  la entrega de un AGENTE SIN CHAT, ya publicada por el dispatcher
# ===========================================================================
def registrar_entrega_de_agente(runtime, *, corpus=None, paquete, circuito=None):
    """El cierre de oficina de un paquete que despachó el adaptador de agente.

    El dispatcher ya publicó `completado` con la entrega del agente dentro de
    `resultado.salida`. Aquí se VALIDA esa entrega contra su rol, se registra en
    `entregas/`, se dictamina si el rol juzga, y se emiten los handoffs, o se abre la
    corrección, o se bloquea con reemplazo. Es idempotente: una entrega ya registrada no se
    registra dos veces.

    VENTANA DECLARADA. Entre el `completado` del dispatcher y este registro hay un instante
    en el que un sucesor ya es elegible. Con un supervisor por control repo la ventana no
    tiene testigo; con varios, otro supervisor podría despachar un sucesor antes de que una
    devolución lo reapunte. Se dice aquí y en `CONTRATO-OFICINA.md`; cerrarla exige que el
    dispatcher registre la entrega en la MISMA transición que el acuse, y eso es otro corte.
    """
    corpus = corpus or Corpus()
    almacen = runtime.almacen
    objeto = durable.leer(almacen, "paquetes/" + paquete + ".json")
    if objeto is None or objeto["estado"] != "completado":
        raise CicloInconsistente("`" + paquete + "` no está completado: no hay entrega que "
                                 "registrar", ruta=paquete)
    intento = int(objeto.get("intentos") or 1)
    ya = entregas.leer(almacen, entregas.identificador(paquete, intento))
    if ya is not None:
        return {"paquete": paquete, "entrega": ya["id"], "repetido": True}
    plan, fila = plan_de_paquete(almacen, paquete)
    if plan is None or fila is None or not fila.get("rol"):
        raise CicloInconsistente("el paquete `" + paquete + "` no tiene fila con rol", ruta=paquete)
    import json as _json                                              # noqa: PLC0415
    crudo = (objeto.get("resultado") or {}).get("salida") or ""
    try:
        entrega = _json.loads(crudo)
    except ValueError as exc:
        raise EntregaInvalida("la salida del agente no es una entrega JSON: " + str(exc),
                              paquete=paquete) from exc
    if not isinstance(entrega, dict):
        raise EntregaInvalida("la salida del agente no es un mapa", paquete=paquete)
    entrega.setdefault("paquete", paquete)
    entrega.setdefault("rol", fila["rol"])
    contrato = corpus.contrato_operativo_de(fila["rol"])
    entregas.exigir_forma(entrega, corpus=corpus, contrato=contrato, gate=fila.get("gate"))
    veredicto = entrega["veredicto"]
    titular = str((objeto.get("resultado") or {}).get("detalle") or "")  # informativo
    dictamenes_emitidos = []
    declarados = list(entrega.get("dictamenes") or [])
    if entrega.get("dictamen"):
        declarados.append(entrega["dictamen"])
    for datos in declarados:
        dictamenes_emitidos.append(_dictaminar(runtime, corpus, plan, fila, paquete, datos))
    registrada = entregas.registrar(almacen, entrega, intento=intento,
                                    titular=_titular_del_agente(almacen, paquete) or runtime.instancia,
                                    corpus=corpus, contrato=contrato)
    salida = {"paquete": paquete, "entrega": registrada["id"], "veredicto": veredicto,
              "dictamenes": [d["id"] for d in dictamenes_emitidos]}
    if veredicto == "entregado":
        salida["handoffs_emitidos"] = _emitir_a_sucesores(runtime, corpus, plan, fila, paquete,
                                                          registrada)
    elif veredicto == "devuelto":
        salida["correccion"] = _devolver(runtime, corpus, plan, fila, paquete, entrega)
    else:
        salida["bloqueo"] = _bloquear_con_reemplazo(runtime, corpus, plan, fila, paquete, entrega)
    del titular
    return salida


def _titular_del_agente(almacen, paquete):
    """Quién ejecutó el paquete: el titular del último acuse, leído del diario del paquete."""
    ultima = None
    for evento in almacen.diario():
        if evento.get("tipo") == "runtime.efecto.acusado" and paquete in str(evento.get("motivo") or ""):
            ultima = evento.get("autor")
    return ultima


def _bloquear_con_reemplazo(runtime, corpus, plan, fila, paquete, entrega):
    """Un agente que entrega `bloqueado`/`escalado` ya tiene su paquete completado: se abre
    un REEMPLAZO en `bloqueado`, los sucesores se reapuntan a él, y el item queda con su
    salida escrita. Al desbloquear, el reemplazo vuelve a `listo` y se vuelve a despachar."""
    almacen = runtime.almacen
    objeto = durable.leer(almacen, "paquetes/" + paquete + ".json")
    bloqueo = entrega["bloqueo"]
    id_reemplazo = "pq-" + cid_de_objeto({"reemplaza_bloqueado": paquete,
                                          "motivo": bloqueo["que_lo_impide"]}).split(":", 1)[-1][:12]
    if durable.leer(almacen, "paquetes/" + id_reemplazo + ".json") is None:
        runtime.crear_paquete(
            id=id_reemplazo, item=plan["item"],
            capacidades_requeridas=list(objeto["capacidades_requeridas"]), orden=objeto["orden"],
            prioridad=objeto["prioridad"], max_intentos=objeto["max_intentos"], depende_de=[],
            acoplamiento=objeto.get("acoplamiento"),
        )
        runtime.bloquear(id_reemplazo, motivo=bloqueo["que_lo_impide"], autoridad=fila["capacidad"])
    reapuntados = []
    for sucesor in _sucesores(plan, paquete):
        actual = durable.leer(almacen, "paquetes/" + sucesor["paquete"] + ".json")
        if actual is None or actual["estado"] in ("completado", "cancelado"):
            continue
        nuevo = dict(actual)
        nuevo["depende_de"] = sorted((set(actual["depende_de"]) - {paquete}) | {id_reemplazo})
        durable.escribir(
            almacen, clase="ciclo.dependencia.reapuntada",
            motivo="`" + sucesor["paquete"] + "` espera al reemplazo " + id_reemplazo + " de " + paquete,
            objetos={"paquetes/" + sucesor["paquete"] + ".json": nuevo},
            semilla={"paquete": sucesor["paquete"], "nuevo": id_reemplazo}, autor=runtime.instancia,
        )
        reapuntados.append(sucesor["paquete"])
    filas = [dict(f) for f in plan.get("correspondencia") or []]
    fila_r = dict(fila)
    fila_r.update({"paquete": id_reemplazo, "reemplaza_a": paquete, "depende_de": [],
                   "motivo_de_bloqueo": bloqueo["que_lo_impide"]})
    filas.append(fila_r)
    for fila_s in filas:
        if fila_s["paquete"] in reapuntados:
            fila_s["depende_de"] = sorted((set(fila_s["depende_de"]) - {paquete}) | {id_reemplazo})
    nuevo_plan = dict(plan)
    nuevo_plan["paquetes"] = sorted(set(plan["paquetes"]) | {id_reemplazo})
    nuevo_plan["correspondencia"] = filas
    nuevo_plan["sustituye_a"] = plan["id"]
    nuevo_plan["id"] = planificacion._identificador(nuevo_plan)
    durable.escribir(
        almacen, clase="ciclo.plan.bloqueo", motivo="reemplazo bloqueado " + id_reemplazo + " de " + paquete,
        objetos={planificacion.ruta_de(nuevo_plan["id"]): nuevo_plan},
        semilla={"plan": nuevo_plan["id"]}, autor=runtime.instancia,
    )
    cierre = modulo_cierre.Cierre(runtime, corpus=corpus)
    if entrega["veredicto"] == "bloqueado":
        salida = cierre.bloquear(nuevo_plan, motivo=bloqueo["que_lo_impide"],
                                 trabajo_de_reemplazo=bloqueo["que_lo_desbloquearia"])
    else:
        salida = cierre.escalar(nuevo_plan, motivo=bloqueo["que_lo_impide"],
                                autoridad=bloqueo["autoridad"], posturas=bloqueo.get("posturas") or [])
    return {"reemplazo": id_reemplazo, "reapuntados": reapuntados, "cierre": salida["id"],
            "salida": salida["salida"]}


# ===========================================================================
#  DEVOLVER: corrección + nuevo receptor + freno
# ===========================================================================
def _devolver(runtime, corpus, plan, fila, paquete, entrega):
    almacen = runtime.almacen
    recibido = handoff_acusado_por(almacen, paquete)
    candidatos = list(entrega.get("dictamenes") or []) + (
        [entrega["dictamen"]] if entrega.get("dictamen") else [])
    fallidos = [d for d in candidatos if d.get("dictamen") == gates.NO_SUPERADO]
    juzgado = str((fallidos[0] if fallidos else (candidatos[0] if candidatos else {})).get(
        "sobre_paquete") or (recibido["trazabilidad"]["paquete"] if recibido else ""))
    if not juzgado:
        raise EntregaInvalida(
            "una devolución tiene que decir QUÉ paquete devuelve: no hay handoff acusado "
            "por `" + paquete + "` ni dictamen que lo nombre", paquete=paquete,
        )
    # El freno se mide sobre las devoluciones ANTERIORES: dos ya contadas y ésta es la
    # tercera, que es la que `a.7` para. Medirlo después de escribir ésta frenaba a la segunda.
    frenado, cuenta, motivo = paralelismo.freno_de_devoluciones(almacen, plan["item"])
    if recibido is not None:
        devuelto = handoffs.devolver(recibido, devolucion=entrega["devolucion"])
        _escribir_handoff(almacen, devuelto, autor=runtime.instancia,
                          clase="ciclo.handoff.devuelto",
                          motivo="devolución de " + paquete + " a " + juzgado)
    if frenado:
        modulo_cierre.Cierre(runtime, corpus=corpus).escalar(
            plan, motivo=motivo, autoridad="OWNER",
            posturas=["el rol " + fila["rol"] + " devuelve: " + entrega["devolucion"]["que_falta"],
                      "el rol productor de `" + juzgado + "` sostiene su última entrega"],
        )
        raise FrenoDisparado(motivo, item=plan["item"], devoluciones=cuenta)
    return _abrir_correccion(runtime, corpus, plan, emisor=juzgado, receptor=paquete,
                             motivo=entrega["devolucion"]["que_falta"],
                             cuenta_para_el_freno=True)


def _abrir_correccion(runtime, corpus, plan, *, emisor, receptor, motivo, cuenta_para_el_freno):
    """Un paquete de CORRECCIÓN para el rol emisor y un NUEVO paquete receptor que lo espera.

    Los sucesores del receptor se reapuntan al nuevo receptor en la misma pasada, antes de
    que el receptor viejo cierre: es lo que impide que una capa devuelta siga adelante.
    """
    almacen = runtime.almacen
    _, fila_emisor = plan_de_paquete(almacen, emisor)
    _, fila_receptor = plan_de_paquete(almacen, receptor)
    if fila_emisor is None or fila_receptor is None:
        raise CicloInconsistente("emisor o receptor sin fila en el plan", ruta=emisor)
    objeto_emisor = durable.leer(almacen, "paquetes/" + emisor + ".json")
    objeto_receptor = durable.leer(almacen, "paquetes/" + receptor + ".json")
    vuelta = 1 + sum(1 for f in plan.get("correspondencia") or []
                     if f.get("correccion_de") == emisor)
    id_correccion = "pq-" + cid_de_objeto({
        "correccion_de": emisor, "vuelta": vuelta, "motivo": motivo,
    }).split(":", 1)[-1][:12]
    id_receptor = "pq-" + cid_de_objeto({
        "reemplaza_a": receptor, "vuelta": vuelta, "correccion": id_correccion,
    }).split(":", 1)[-1][:12]
    if durable.leer(almacen, "paquetes/" + id_correccion + ".json") is None:
        runtime.crear_paquete(
            id=id_correccion, item=plan["item"],
            capacidades_requeridas=list(objeto_emisor["capacidades_requeridas"]),
            orden=objeto_emisor["orden"], prioridad=PRIORIDAD_DE_CORRECCION,
            max_intentos=objeto_emisor["max_intentos"], depende_de=[],
            acoplamiento=objeto_emisor.get("acoplamiento"),
        )
    if durable.leer(almacen, "paquetes/" + id_receptor + ".json") is None:
        runtime.crear_paquete(
            id=id_receptor, item=plan["item"],
            capacidades_requeridas=list(objeto_receptor["capacidades_requeridas"]),
            orden=objeto_receptor["orden"], prioridad=PRIORIDAD_DE_CORRECCION,
            max_intentos=objeto_receptor["max_intentos"], depende_de=[id_correccion],
            acoplamiento=objeto_receptor.get("acoplamiento"),
        )
    # Reapuntar los sucesores del receptor viejo al nuevo, ANTES de que el viejo cierre.
    reapuntados = []
    for sucesor in _sucesores(plan, receptor):
        actual = durable.leer(almacen, "paquetes/" + sucesor["paquete"] + ".json")
        if actual is None or actual["estado"] in ("completado", "cancelado"):
            continue
        nuevo = dict(actual)
        nuevo["depende_de"] = sorted((set(actual["depende_de"]) - {receptor}) | {id_receptor})
        durable.escribir(
            almacen, clase="ciclo.dependencia.reapuntada",
            motivo="`" + sucesor["paquete"] + "` deja de esperar a " + receptor
                   + " y espera a " + id_receptor,
            objetos={"paquetes/" + sucesor["paquete"] + ".json": nuevo},
            semilla={"paquete": sucesor["paquete"], "nuevo": id_receptor},
            autor=runtime.instancia,
        )
        reapuntados.append(sucesor["paquete"])
    filas = list(plan.get("correspondencia") or [])
    fila_c = dict(fila_emisor)
    fila_c.update({"paquete": id_correccion, "prioridad": PRIORIDAD_DE_CORRECCION,
                   "depende_de": [], "correccion_de": emisor, "vuelta": vuelta,
                   "motivo_de_correccion": str(motivo),
                   "cuenta_para_el_freno": bool(cuenta_para_el_freno)})
    fila_r = dict(fila_receptor)
    fila_r.update({"paquete": id_receptor, "prioridad": PRIORIDAD_DE_CORRECCION,
                   "depende_de": [id_correccion], "reemplaza_a": receptor, "vuelta": vuelta})
    for fila_nueva in (fila_c, fila_r):
        filas = [f for f in filas if f["paquete"] != fila_nueva["paquete"]] + [fila_nueva]
    for fila_s in filas:
        if fila_s["paquete"] in reapuntados:
            fila_s["depende_de"] = sorted((set(fila_s["depende_de"]) - {receptor}) | {id_receptor})
    nuevo_plan = dict(plan)
    nuevo_plan["paquetes"] = sorted(set(plan["paquetes"]) | {id_correccion, id_receptor})
    nuevo_plan["correspondencia"] = filas
    nuevo_plan["sustituye_a"] = plan["id"]
    nuevo_plan["id"] = planificacion._identificador(nuevo_plan)
    durable.escribir(
        almacen, clase="ciclo.plan.corregido",
        motivo="corrección " + id_correccion + " de " + emisor + " y nuevo receptor "
               + id_receptor + " (vuelta " + str(vuelta) + ")",
        objetos={planificacion.ruta_de(nuevo_plan["id"]): nuevo_plan},
        semilla={"plan": nuevo_plan["id"]}, autor=runtime.instancia,
    )
    return {"correccion": id_correccion, "receptor": id_receptor, "vuelta": vuelta,
            "reapuntados": reapuntados, "plan": nuevo_plan["id"]}


# ===========================================================================
#  el OWNER acepta
# ===========================================================================
def aceptar(runtime, *, corpus=None, item, comprobaciones_superadas, evidencia, hallazgos=(),
            autor_capacidad=None):
    """El dictamen del Owner sobre `gate:aceptacion-del-owner`. Sólo el Owner lo firma."""
    corpus = corpus or Corpus()
    almacen = runtime.almacen
    plan = plan_vigente_de_item(almacen, item)
    if plan is None:
        raise CicloInconsistente("el item `" + item + "` no tiene plan vigente", ruta=item)
    autor = autor_capacidad or plan["propietario_global"]
    entrada = {"item": item, "sobre_item": item, "revisor_titular": "OWNER",
               "autor_titular": ""}
    try:
        cuerpo = gates.aplicar(
            terminacion.GATE_DEL_NIVEL["aceptado"], entrada=entrada, evidencia=list(evidencia),
            revisor=gates.REVISOR_OWNER, autor=autor, corpus=corpus,
            comprobaciones_superadas=list(comprobaciones_superadas), hallazgos=list(hallazgos),
            salida="aceptación del Owner",
        )
    except GateFallido as error:
        cuerpo = getattr(error, "dictamen", None)
        if cuerpo is None:
            raise
    durable.escribir(
        almacen, clase="ciclo.dictamen." + cuerpo["dictamen"],
        motivo="aceptación del Owner sobre " + item + ": " + cuerpo["dictamen"],
        objetos={gates.ruta_de(cuerpo["id"]): cuerpo}, semilla={"dictamen": cuerpo["id"]},
        autor="OWNER",
    )
    return cuerpo


# ===========================================================================
#  NIVELES y CIERRE
# ===========================================================================
def evaluar_terminacion(runtime, *, corpus=None, item, circuito, hechos):
    almacen = runtime.almacen
    plan = plan_vigente_de_item(almacen, item)
    paquetes = list(plan["paquetes"]) if plan else []
    cierres = [c for c in cierres_de_item(almacen, item) if c.get("salida") == "completado"]
    evaluacion = terminacion.evaluar(
        circuito, item=item, paquetes_del_item=paquetes,
        dictamenes=dictamenes_de_item(almacen, item), hechos=hechos,
        cierre=cierres[-1] if cierres else None,
    )
    # Las fronteras previas a la construcción (§77), derivadas de qué paquetes entregaron.
    estados = {}
    for pq in paquetes:
        objeto = durable.leer(almacen, "paquetes/" + str(pq) + ".json") or {}
        estados[str(pq)] = objeto.get("estado")
    evaluacion["fronteras"] = terminacion.evaluar_fronteras(plan, estados)
    evaluacion["impacto"] = modulo_impacto.pendiente(plan)
    return evaluacion


def obligaciones_satisfechas(almacen, plan):
    """Una obligación está satisfecha cuando su último paquete por rol entregó."""
    por_obligacion = {}
    for fila in plan.get("correspondencia") or []:
        if not fila.get("obligacion"):
            continue
        por_obligacion.setdefault(fila["obligacion"], []).append(fila["paquete"])
    satisfechas = []
    for obligacion, paquetes in sorted(por_obligacion.items()):
        vigentes = [p for p in paquetes if not _reemplazado(plan, p)]
        if all(_entregado(almacen, p) for p in vigentes):
            satisfechas.append(obligacion)
    return satisfechas


def _reemplazado(plan, paquete):
    return any(f.get("reemplaza_a") == paquete for f in plan.get("correspondencia") or [])


def _entregado(almacen, paquete):
    objeto = durable.leer(almacen, "paquetes/" + paquete + ".json")
    if objeto is None or objeto["estado"] != "completado":
        return False
    ultima = entregas.ultima(almacen, paquete)
    return bool(ultima and ultima.get("veredicto") == "entregado")


def cerrar_item(runtime, *, corpus=None, item, circuito, hechos, integracion, aprendizaje,
                retiradas=()):
    """Cierra el item como PRODUCTO: niveles del circuito base + `gate:cierre-de-item`."""
    corpus = corpus or Corpus()
    almacen = runtime.almacen
    evaluacion = evaluar_terminacion(runtime, corpus=corpus, item=item, circuito=circuito,
                                     hechos=hechos)
    terminacion.exigir_cierre({**evaluacion, "faltan": [
        n for n in evaluacion["faltan"] if n != "cerrado"]})
    plan = plan_vigente_de_item(almacen, item)
    cierre = modulo_cierre.Cierre(runtime, corpus=corpus)
    salida = cierre.cerrar(
        plan, satisfechas=obligaciones_satisfechas(almacen, plan), retiradas=retiradas,
        integracion=integracion, aprendizaje=aprendizaje,
    )
    return {"cierre": salida, "terminacion": evaluacion}
