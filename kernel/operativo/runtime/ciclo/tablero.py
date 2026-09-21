#!/usr/bin/env python3
"""tablero — la VISTA DE ORGANIZACIÓN, derivada del estado canónico y de nada más.

    «Necesito poder conocer en cualquier momento, sin reconstruirlo leyendo veinte JSON:
     qué objetivos están activos, cómo se han descompuesto, qué paquetes están
     disponibles, cuáles ejecutándose, qué equipo posee cada uno, qué roles intervienen,
     qué workers están activos, qué espera y por qué, qué se entregó, qué handoffs están
     pendientes, qué devoluciones existen, qué gates faltan, qué necesita al Owner, y qué
     hará el sistema a continuación si el Owner no dice absolutamente nada.»
                                                                — el Owner, 2026-09-14

Cada pregunta es una clave de la salida, y cada clave se calcula del estado en cada
llamada. No se persiste: una vista que sabe más que el estado es una segunda verdad
(`§7.5`). El kernel responde por items, planes, paquetes, leases, equipos, entregas,
handoffs, dictámenes, checkpoints y cierres; lo que la instancia añada encima —objetivos,
decisiones del Owner— lo compone la instancia con su propio módulo, sin tocar éste.

DECISIÓN · «qué hará el sistema si nadie dice nada» se DERIVA de la cola, no se redacta
    Es la lista de paquetes tomables en el orden de `b.12`, más los externos en curso con
    su titular. Si está vacía y hay paquetes bloqueados o esperas inviables, lo siguiente
    es una decisión: se dice de quién.
"""
from __future__ import annotations

from . import cierre as modulo_cierre, durable, entregas, gates, handoffs, planificacion
from . import oficina
from .equipos import DOMINIO as DOMINIO_EQUIPOS
from .corpus import Corpus


def _leer_todos(almacen, dominio):
    salida = []
    for ruta in sorted(almacen.listar(dominio)):
        objeto = almacen.leer(ruta)
        if isinstance(objeto, dict):
            salida.append(objeto)
    return salida


def derivar(runtime, *, corpus=None):
    """La vista completa. Determinista: mismo estado, mismos bytes."""
    corpus = corpus or Corpus()
    almacen = runtime.almacen
    revision = almacen.revision()
    items = {i["id"]: i for i in _leer_todos(almacen, "items")}
    paquetes = {p["id"]: p for p in _leer_todos(almacen, "paquetes")}
    leases = {l["paquete"]: l for l in _leer_todos(almacen, "leases")}
    checkpoints = {c["paquete"]: c for c in _leer_todos(almacen, "checkpoints")}
    planes = planificacion.planes(almacen)
    equipos = {e["id"]: e for e in _leer_todos(almacen, DOMINIO_EQUIPOS)}
    entregas_todas = _leer_todos(almacen, entregas.DOMINIO)
    handoffs_todos = _leer_todos(almacen, handoffs.DOMINIO)
    dictamenes = _leer_todos(almacen, gates.DOMINIO)
    cierres = _leer_todos(almacen, modulo_cierre.DOMINIO)

    vigentes = {}
    for plan in planes:
        vigente = oficina.plan_vigente_de_item(almacen, plan["item"])
        if vigente:
            vigentes[plan["item"]] = vigente
    fila_de_paquete = {}
    for plan in vigentes.values():
        for fila in plan.get("correspondencia") or []:
            fila_de_paquete[fila["paquete"]] = (plan, fila)

    def describir(identificador):
        paquete = paquetes[identificador]
        plan, fila = fila_de_paquete.get(identificador, (None, None))
        lease = leases.get(identificador)
        equipo = oficina.equipo_de(almacen, plan, fila["capacidad"]) if plan and fila else None
        agente = oficina.agente_del_rol(equipo, fila.get("rol")) if equipo and fila else None
        ultima = [e for e in entregas_todas if e.get("paquete") == identificador]
        ultima = sorted(ultima, key=lambda e: int(e.get("intento") or 0))[-1] if ultima else None
        pendientes, inviables = [], []
        try:
            pendientes, inviables = runtime._dependencias_pendientes(paquete)
        except Exception:                                    # noqa: BLE001 — se publica tal cual
            pass
        return {
            "paquete": identificador,
            "item": paquete["item"],
            "estado": paquete["estado"],
            "prioridad": paquete["prioridad"],
            "intentos": paquete["intentos"],
            "externo": str(paquete["orden"].get("adaptador")) == "worker",
            "adaptador": paquete["orden"].get("adaptador"),
            "capacidad": fila.get("capacidad") if fila else None,
            "rol": fila.get("rol") if fila else None,
            "obligacion": fila.get("obligacion") if fila else None,
            "gate": fila.get("gate") if fila else None,
            "equipo": equipo["id"] if equipo else None,
            "agente": (agente or {}).get("agente"),
            "modelo": (agente or {}).get("modelo"),
            "titular": lease["titular"] if lease else None,
            "epoca": lease["epoca"] if lease else None,
            "latido": lease["latido"] if lease else None,
            "checkpoint": (checkpoints.get(identificador) or {}).get("contenido"),
            "depende_de": list(paquete["depende_de"]),
            "espera_a": sorted(pendientes),
            "inviables": sorted(inviables),
            "correccion_de": fila.get("correccion_de") if fila else None,
            "reemplaza_a": fila.get("reemplaza_a") if fila else None,
            "ultima_entrega": {"id": ultima["id"], "veredicto": ultima["veredicto"],
                               "titular": ultima.get("titular")} if ultima else None,
        }

    descritos = {p: describir(p) for p in sorted(paquetes)}
    por_estado = {}
    for descrito in descritos.values():
        por_estado.setdefault(descrito["estado"], []).append(descrito["paquete"])

    tomables = runtime.tomables()
    en_ejecucion = [d for d in descritos.values() if d["estado"] in ("despachado", "ejecutando")]
    esperando = []
    for descrito in descritos.values():
        if descrito["estado"] in ("completado", "cancelado"):
            continue
        motivo = None
        if descrito["estado"] == "bloqueado":
            motivo = "bloqueado: " + str((descrito["checkpoint"] or {}).get("bloqueo", {}).get(
                "que_lo_impide") or "sin motivo en el checkpoint")
        elif descrito["inviables"]:
            motivo = "espera inviable: " + ", ".join(descrito["inviables"])
        elif descrito["espera_a"]:
            motivo = "espera a " + ", ".join(descrito["espera_a"])
        elif descrito["estado"] in ("despachado", "ejecutando") and descrito["titular"] \
                and descrito["titular"] != runtime.instancia:
            motivo = "en manos de " + descrito["titular"]
        elif descrito["estado"] == "agotado":
            motivo = "agotado: reconciliación de g.9 pendiente"
        elif descrito["estado"] == "pausado":
            motivo = "pausado por orden"
        if motivo:
            esperando.append({"paquete": descrito["paquete"], "rol": descrito["rol"],
                              "estado": descrito["estado"], "por_que": motivo})

    equipos_activos = []
    for identificador, equipo in sorted(equipos.items()):
        propios = [d for d in descritos.values() if d["equipo"] == identificador]
        vivos = [d for d in propios if d["estado"] not in ("completado", "cancelado")]
        equipos_activos.append({
            "equipo": identificador, "capacidad": equipo["capacidad"],
            "composicion": equipo["composicion"], "estado": equipo.get("estado"),
            "roles": [{"rol": r["rol"], "agente": r.get("agente"), "modelo": r.get("modelo")}
                      for r in equipo.get("roles") or []],
            "cola": sorted(d["paquete"] for d in vivos),
            "en_custodia": sorted(d["paquete"] for d in vivos if d["estado"] in
                                  ("despachado", "ejecutando")),
            "entregados": sorted(d["paquete"] for d in propios if d["estado"] == "completado"),
            "workers": sorted({d["titular"] for d in vivos if d["titular"]}),
            "activo": bool(vivos),
        })

    workers = {}
    for descrito in descritos.values():
        if descrito["titular"] and descrito["estado"] in ("despachado", "ejecutando"):
            workers.setdefault(descrito["titular"], []).append(descrito["paquete"])

    pendientes_de_acuse = [h for h in handoffs_todos if h.get("estado") == handoffs.EMITIDO]
    devueltos = [h for h in handoffs_todos if h.get("estado") == handoffs.DEVUELTO]
    rechazados = [h for h in handoffs_todos if h.get("estado") == handoffs.RECHAZADO]

    items_vista = []
    sin_plan = []
    for identificador, item in sorted(items.items()):
        plan = vigentes.get(identificador)
        propios = [d for d in descritos.values() if d["item"] == identificador]
        if plan is None and not propios:
            # Un item que la oficina no ha planificado no tiene nada que decir aquí: se
            # cuenta y se nombra, para que se vea que existe SIN plan, y no se detalla.
            # Medido en La Pesquerapp: 78 items en el estado y uno planificado; el tablero
            # enterraba ese uno bajo 77 fichas vacías.
            sin_plan.append(identificador)
            continue
        cierres_item = [c for c in cierres if c.get("item") == identificador]
        dictamenes_item = [d for d in dictamenes if (d.get("entrada") or {}).get("item") == identificador]
        items_vista.append({
            "item": identificador,
            "titulo": item.get("titulo"),
            "estado_del_item": item.get("estado"),
            "plan": plan["id"] if plan else None,
            "proceso": plan.get("proceso") if plan else None,
            "propietario_global": plan.get("propietario_global") if plan else None,
            "paquetes": {estado: sorted(d["paquete"] for d in propios if d["estado"] == estado)
                         for estado in sorted({d["estado"] for d in propios})},
            "ruta": [{"paquete": f["paquete"], "capacidad": f["capacidad"], "rol": f.get("rol"),
                      "estado": descritos[f["paquete"]]["estado"] if f["paquete"] in descritos
                      else "desconocido"}
                     for f in (plan.get("correspondencia") if plan else [])],
            "dictamenes": [{"gate": d["gate"], "dictamen": d["dictamen"], "revisor": d["revisor"],
                            "sobre": (d.get("entrada") or {}).get("sobre_paquete")}
                           for d in dictamenes_item],
            "gates_pendientes": sorted({f.get("gate") for f in (plan.get("correspondencia") if plan else [])
                                        if f.get("gate")} - {d["gate"] for d in dictamenes_item
                                                              if d["dictamen"] == "superado"}),
            "salidas": [{"salida": c["salida"], "motivo": c.get("motivo")} for c in cierres_item],
        })

    circulares = _dependencias_circulares(paquetes)

    # LO QUE SE OFRECE, SE ENTREGA. `runtime.tomables()` mira el plano operacional
    # —dependencias y leases— y no sabe qué es un plan vigente; `oficina.tomar` exige el plan
    # vigente y no sabe qué publicó esta vista. Con las dos nociones sueltas, replanificar un
    # item dejaba en `TOMABLES AHORA` los paquetes de la generación anterior, y el trabajador
    # que obedecía al tablero —tomar el primero de la lista— recibía `CICLO_INCONSISTENTE: no
    # está en ningún plan vigente`. El tablero es la sede que le dice a una sesión nueva qué
    # puede tomar (`§45`): si miente, el relevo se estrella en la primera orden.
    #
    # DECISIÓN · se retira de la oferta, y se PUBLICA la retirada con su motivo
    #     Alternativas: (a) filtrar en silencio; (b) publicar aparte lo retirado y por qué.
    #     Se elige (b), la misma disciplina que `rutas.no_activadas`: un paquete que
    #     desaparece de la lista sin explicación convierte un defecto ruidoso en uno mudo, y
    #     quien replanificó tiene derecho a ver que su generación anterior sigue ahí.
    ofrecibles, retirados = [], []
    for fila in tomables["tomables"]:
        if fila["paquete"] in fila_de_paquete:
            ofrecibles.append(fila)
        else:
            retirados.append({
                "paquete": fila["paquete"], "item": fila.get("item"),
                "motivo": "de un plan superado: su item tiene otro plan vigente y `tomar` lo "
                          "rechazaría; no se ofrece lo que la oficina no entregaría",
            })

    siguiente = [{"paquete": t["paquete"], "rol": descritos.get(t["paquete"], {}).get("rol"),
                  "item": t["item"]} for t in ofrecibles]
    if circulares and not siguiente:
        que_hara = ("nada: hay una dependencia circular entre " + ", ".join(circulares)
                    + " y ninguna pasada puede moverla; hace falta replanificar el item")
    elif siguiente:
        que_hara = ("tomar y trabajar, en este orden, sin que nadie diga nada: "
                    + ", ".join(s["paquete"] + " (" + str(s["rol"]) + ")" for s in siguiente))
    elif en_ejecucion:
        que_hara = ("esperar a que terminen los paquetes en manos de "
                    + ", ".join(sorted({d["titular"] for d in en_ejecucion if d["titular"]}) or
                                ["nadie: hay paquetes en curso sin titular, se pueden tomar"]))
    elif any(d["estado"] == "bloqueado" for d in descritos.values()):
        que_hara = "nada: todo el trabajo restante está bloqueado; hace falta un desbloqueador o una decisión"
    elif any(d["estado"] not in ("completado", "cancelado") for d in descritos.values()):
        que_hara = "nada hasta que una espera se resuelva: ver `esperando`"
    else:
        que_hara = "nada: no hay trabajo abierto en el estado"

    return {
        "derivada": True,
        "revision": revision["revision"],
        "revision_id": revision["revision_id"],
        "instancia": runtime.instancia,
        "items": items_vista,
        "items_sin_plan": sin_plan,
        "paquetes": descritos,
        "por_estado": por_estado,
        "tomables": [t["paquete"] for t in ofrecibles],
        "tomables_de_plan_superado": retirados,
        "en_ejecucion": [{"paquete": d["paquete"], "rol": d["rol"], "titular": d["titular"],
                          "latido": d["latido"]} for d in en_ejecucion],
        "esperando": esperando,
        "equipos": equipos_activos,
        "workers": {w: sorted(p) for w, p in sorted(workers.items())},
        "handoffs_pendientes_de_acuse": [
            {"id": h["id"], "de": h["de"], "a": h["a"], "destino": h["trazabilidad"].get("destino")}
            for h in pendientes_de_acuse],
        "devoluciones": [{"id": h["id"], "de": h["de"], "a": h["a"],
                          "que_falta": (h.get("devolucion") or {}).get("que_falta")}
                         for h in devueltos],
        "rechazos": [{"id": h["id"], "de": h["de"], "a": h["a"],
                      "motivo": (h.get("rechazo") or {}).get("motivo")} for h in rechazados],
        "escalados": [{"item": c["item"], "motivo": c.get("motivo"), "autoridad": c.get("autoridad")}
                      for c in cierres if c.get("salida") == "escalado"],
        "bloqueos": [{"item": c["item"], "motivo": c.get("motivo"),
                      "trabajo_de_reemplazo": c.get("trabajo_de_reemplazo")}
                     for c in cierres if c.get("salida") == "bloqueado"],
        "reconciliaciones_abiertas": [l["registro"] for l in almacen.reconciliacion_pendiente()],
        "dependencias_circulares": circulares,
        "que_hara_el_sistema_si_nadie_dice_nada": que_hara,
    }


def _dependencias_circulares(paquetes):
    """Los paquetes abiertos que participan en un ciclo de `depende_de`. Determinista.

    Un paquete que se espera a sí mismo por un camino no se toma nunca y no falla nunca:
    es la espera silenciosa que `T471` vino a nombrar. Se detecta por color, sobre los
    paquetes no terminales, y se publica ordenado.
    """
    abiertos = {i for i, p in paquetes.items() if p.get("estado") not in ("completado", "cancelado")}
    grafo = {i: [d for d in (paquetes[i].get("depende_de") or []) if d in abiertos] for i in abiertos}
    color, en_ciclo = {}, set()

    def visitar(nodo, camino):
        color[nodo] = "gris"
        camino.append(nodo)
        for vecino in grafo.get(nodo, []):
            estado = color.get(vecino)
            if estado is None:
                visitar(vecino, camino)
            elif estado == "gris":
                en_ciclo.update(camino[camino.index(vecino):])
        camino.pop()
        color[nodo] = "negro"

    for nodo in sorted(abiertos):
        if nodo not in color:
            visitar(nodo, [])
    return sorted(en_ciclo)


def como_texto(vista):
    """El tablero legible. Determinista."""
    lineas = ["TABLERO DE LA OFICINA · revisión " + str(vista["revision"]), "=" * 78]
    if not vista["items"]:
        lineas.append("(ningún item planificado por la oficina)")
    if vista.get("items_sin_plan"):
        lineas += ["", "SIN PLAN DE OFICINA: " + str(len(vista["items_sin_plan"])) + " item(s) del estado — "
                   + ", ".join(vista["items_sin_plan"][:8])
                   + (" …" if len(vista["items_sin_plan"]) > 8 else "")]
    for item in vista["items"]:
        lineas.append("")
        lineas.append("ITEM " + item["item"] + " — " + str(item.get("titulo") or ""))
        lineas.append("  proceso " + str(item["proceso"]) + " · propietario "
                      + str(item["propietario_global"]) + " · plan " + str(item["plan"]))
        for paso in item["ruta"]:
            lineas.append("    " + paso["paquete"] + "  " + paso["capacidad"] + "  "
                          + str(paso["rol"]) + "  [" + paso["estado"] + "]")
        if item["dictamenes"]:
            lineas.append("  dictámenes: " + "; ".join(
                d["gate"] + "=" + d["dictamen"] + " por " + d["revisor"] for d in item["dictamenes"]))
        lineas.append("  gates sin superar: " + (", ".join(item["gates_pendientes"]) or "(ninguno)"))
        if item["salidas"]:
            lineas.append("  salidas: " + "; ".join(s["salida"] + " · " + str(s["motivo"])[:80]
                                                   for s in item["salidas"]))
    lineas += ["", "EN EJECUCIÓN"]
    for fila in vista["en_ejecucion"] or []:
        lineas.append("  " + fila["paquete"] + "  " + str(fila["rol"]) + "  en manos de "
                      + str(fila["titular"]) + "  latido " + str(fila["latido"]))
    if not vista["en_ejecucion"]:
        lineas.append("  (nada)")
    lineas += ["", "TOMABLES AHORA: " + (", ".join(vista["tomables"]) or "(nada)")]
    for fila in vista.get("tomables_de_plan_superado") or []:
        lineas.append("  NO se ofrece " + fila["paquete"] + ": " + fila["motivo"])
    lineas += ["", "ESPERANDO"]
    for fila in vista["esperando"] or []:
        lineas.append("  " + fila["paquete"] + "  " + str(fila["rol"]) + "  " + fila["por_que"])
    if not vista["esperando"]:
        lineas.append("  (nada)")
    lineas += ["", "EQUIPOS"]
    for equipo in vista["equipos"]:
        lineas.append("  " + equipo["capacidad"] + " · " + equipo["composicion"] + " · "
                      + ("activo" if equipo["activo"] else "sin cola") + " · roles: "
                      + ", ".join(r["rol"] + "→" + str(r["modelo"]) for r in equipo["roles"])
                      + " · workers: " + (", ".join(equipo["workers"]) or "-"))
    lineas += ["", "HANDOFFS pendientes de acuse: " + (", ".join(
        h["id"] + " (" + h["de"] + "→" + h["a"] + ")" for h in vista["handoffs_pendientes_de_acuse"]) or "(ninguno)")]
    lineas += ["DEVOLUCIONES: " + (", ".join(h["id"] + ": " + str(h["que_falta"])[:60]
                                            for h in vista["devoluciones"]) or "(ninguna)")]
    lineas += ["ESCALADOS: " + (", ".join(e["item"] + " → " + str(e["autoridad"])
                                          for e in vista["escalados"]) or "(ninguno)")]
    lineas += ["BLOQUEOS: " + (", ".join(b["item"] + ": " + str(b["motivo"])[:60]
                                         for b in vista["bloqueos"]) or "(ninguno)")]
    lineas += ["RECONCILIACIONES ABIERTAS: " + (", ".join(vista["reconciliaciones_abiertas"]) or "(ninguna)")]
    lineas += ["", "SI NADIE DICE NADA: " + vista["que_hara_el_sistema_si_nadie_dice_nada"]]
    return "\n".join(lineas) + "\n"
