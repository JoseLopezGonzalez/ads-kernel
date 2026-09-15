#!/usr/bin/env python3
"""briefs — la INSTRUCCIÓN COMPLETA que recibe un trabajador al tomar un paquete.

    «Si dos agentes competentes pueden leer el mismo contrato de trabajo y ejecutar de
     forma sustancialmente diferente lo que se espera de ellos, el contrato es insuficiente.»
                                                          — el Owner, 2026-09-14

El brief es la respuesta mecánica a esa frase. Se COMPONE desde el estado y el corpus —no lo
redacta nadie— y contiene TODO lo que el rol necesita para ejecutar sin criterio general:
el contrato del rol (veintinueve campos), su contrato operativo si lo tiene (entradas
obligatorias, comprobaciones previas, secuencia, artefactos con estructura mínima,
checklist), el método paso a paso con sus `termina_cuando`, el gate comprobación a
comprobación, lo que recibe de la capa anterior con lo que tiene que comprobar antes de
tomar custodia, el checkpoint desde el que reanuda, y la FORMA EXACTA de la entrega.

DECISIÓN · el brief se DERIVA y no se persiste como estado canónico
    Es una proyección de objetos que ya son durables —plan, equipo, rol, método, gate,
    handoffs, checkpoint—. Persistirlo sería una segunda verdad que envejece. Se escribe en
    el plano OPERACIONAL del espacio del trabajador para que un agente sin chat lo lea, y su
    huella entra en la entrega para poder decir contra qué brief se trabajó.

DECISIÓN · el brief NO lleva rutas absolutas ni identidad de proceso
    Dos trabajadores en dos máquinas sobre el mismo estado reciben el MISMO brief byte a
    byte. Lo que varía —dónde está el espacio, cómo se invoca la orden de entrega— lo pasa
    quien lo compone como `ordenes`, y se imprime como texto, no como ruta del anfitrión.
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto

from .corpus import Corpus
from .errores import BriefIncomponible

VERSION_DEL_BRIEF = 1


def componer(*, corpus=None, paquete, item, fila_del_plan, rol, equipo=None, intento=1,
             efecto=None, handoffs_pendientes=(), entregas_previas=(), checkpoint=None,
             circuito=None, instrucciones_del_proyecto=(), ordenes=None, fuentes=()):
    """El brief como DATO. `como_markdown` lo vuelve legible; el dato es lo que se firma."""
    corpus = corpus or Corpus()
    if not isinstance(fila_del_plan, dict) or not fila_del_plan.get("capacidad"):
        raise BriefIncomponible("falta la fila del plan del paquete: sin capacidad, obligación "
                                "y gate no hay brief", paquete=str(paquete))
    contrato_de_rol = corpus.rol(rol)
    if contrato_de_rol["capacidad"] != fila_del_plan["capacidad"]:
        raise BriefIncomponible(
            "el rol `" + rol + "` es de `" + contrato_de_rol["capacidad"] + "` y el paquete "
            "es de `" + fila_del_plan["capacidad"] + "`", paquete=str(paquete),
        )
    metodo_id = fila_del_plan.get("metodo") or (contrato_de_rol.get("metodo") or [None])[0]
    metodo = corpus.metodo(metodo_id) if metodo_id else None
    gate_id = fila_del_plan.get("gate") or contrato_de_rol.get("gate")
    gate = corpus.gates().get(gate_id)
    if gate is None:
        raise BriefIncomponible("el gate `" + str(gate_id) + "` no está en el censo",
                                paquete=str(paquete))
    contrato_operativo = corpus.contrato_operativo_de(rol)
    esquema_entrega = corpus.esquema("entrega")
    brief = {
        "version": VERSION_DEL_BRIEF,
        "paquete": str(paquete),
        "intento": int(intento),
        "efecto": efecto,
        "item": dict(item),
        "capacidad": fila_del_plan["capacidad"],
        "via": fila_del_plan.get("via"),
        "obligacion": fila_del_plan.get("obligacion"),
        "criterio_de_satisfaccion": fila_del_plan.get("criterio_de_satisfaccion"),
        "salida_exigida": fila_del_plan.get("salida"),
        "rol": contrato_de_rol,
        "contrato_operativo": contrato_operativo,
        "metodo": metodo,
        "gate": gate,
        "equipo": dict(equipo) if equipo else None,
        "recibes": [dict(h) for h in handoffs_pendientes],
        "entregas_previas": [
            {"id": e.get("id"), "rol": e.get("rol"), "veredicto": e.get("veredicto"),
             "artefactos": e.get("artefactos"), "diferencias_declaradas":
             e.get("diferencias_declaradas"), "no_hecho": e.get("no_hecho"),
             "siguiente": e.get("siguiente")}
            for e in entregas_previas
        ],
        "checkpoint": dict(checkpoint) if checkpoint else None,
        "circuito": {
            "id": circuito.get("id"), "niveles_obligatorios": circuito.get("niveles_obligatorios"),
            "independencias": circuito.get("independencias"),
        } if circuito else None,
        "fuentes": [dict(f) for f in fuentes],
        "instrucciones_del_proyecto": [str(i) for i in instrucciones_del_proyecto],
        "forma_de_la_entrega": {
            "obligatorios": list(esquema_entrega.get("obligatorios") or []),
            "veredictos": ["entregado", "devuelto", "bloqueado", "escalado"],
            "comprobaciones_del_gate": [c["id"] for c in gate["comprobaciones"]],
            "checklist": [c["id"] for c in (contrato_operativo or {}).get("checklist") or []],
            "artefactos_obligatorios": [
                a for a in (contrato_operativo or {}).get("artefactos") or []
                if a.get("obligatorio")
            ],
        },
        "ordenes": dict(ordenes or {}),
        "prohibiciones": _prohibiciones(contrato_de_rol, contrato_operativo),
        "prompt": corpus.prompt_de(rol),
    }
    brief["huella"] = cid_de_objeto({k: v for k, v in brief.items() if k != "huella"})
    return brief


def _prohibiciones(rol, contrato):
    salida = [
        "NO escribes en la rama principal de ninguna fuente; todo cambio va en rama propia",
        "NO juzgas lo que tú mismo produjiste: un dictamen lo firma otro trabajador",
        "NO cierras el item: entregas, y el cierre lo decide el estado con sus gates",
        "NO inventas estado: si algo no cuadra, entregas `bloqueado` o `escalado` y lo dices",
        "NO trabajas sin latir: escribes checkpoint al terminar cada paso; un lease sin "
        "latido se reclama y el trabajo vuelve a la cola",
    ]
    if (rol.get("interaccion_owner") or {}).get("nivel") == "ninguna":
        salida.append("NO hablas con el Owner: lo que necesita su juicio va por la capacidad "
                      "propietaria de esa materia")
    for limite in rol.get("limites") or []:
        salida.append("NO: " + str(limite))
    for prohibida in (contrato or {}).get("actuaciones_prohibidas") or []:
        salida.append("PROHIBIDO: " + str(prohibida))
    return salida


# ===========================================================================
#  texto
# ===========================================================================
def _lista(titulo, valores, *, sangria="  "):
    lineas = [titulo]
    valores = valores or []
    if not valores:
        lineas.append(sangria + "(ninguno)")
    for valor in valores:
        lineas.append(sangria + "· " + str(valor))
    return lineas


def como_markdown(brief):
    """El brief legible. Determinista: mismo dato, mismos bytes."""
    rol = brief["rol"]
    lineas = [
        "# BRIEF · " + brief["paquete"] + " · " + rol["id"],
        "",
        "huella " + brief["huella"] + " · intento " + str(brief["intento"]) + " · efecto "
        + str(brief["efecto"]),
        "",
        "## 1 · Qué es este paquete",
        "",
        "item        " + str(brief["item"].get("id")) + " — " + str(brief["item"].get("titulo") or ""),
        "capacidad   " + brief["capacidad"] + " · vía " + str(brief["via"]),
        "obligación  " + str(brief["obligacion"]),
        "satisfecha  cuando: " + str(brief["criterio_de_satisfaccion"]),
        "salida      " + str(brief["salida_exigida"]),
        "gate        " + brief["gate"]["id"],
        "método      " + str((brief["metodo"] or {}).get("id")),
    ]
    definicion = brief["item"].get("definicion_de_terminado")
    if definicion:
        lineas += [""] + _lista("definición de terminado del item:", definicion)
    if brief.get("circuito"):
        lineas += ["", "circuito base " + str(brief["circuito"]["id"]) + " · niveles obligatorios: "
                   + ", ".join(brief["circuito"]["niveles_obligatorios"] or [])]
    if brief.get("fuentes"):
        lineas += [""] + _lista("fuentes del alcance:", [
            str(f.get("id")) + " (" + str(f.get("path") or "") + ")" for f in brief["fuentes"]])

    lineas += ["", "## 2 · Tu rol: " + rol["nombre"], "", "misión     " + str(rol["mision"]).strip(),
               "resultado  " + str(rol["resultado"]).strip(), ""]
    lineas += _lista("responsabilidades:", rol.get("responsabilidades"))
    lineas += _lista("límites:", rol.get("limites"))
    autoridad = rol.get("autoridad") or {}
    lineas += _lista("decides:", autoridad.get("decide"))
    lineas += _lista("propones:", autoridad.get("propone"))
    lineas += _lista("escalas:", autoridad.get("escala"))
    lineas += _lista("entradas:", rol.get("entradas"))
    lineas += _lista("conocimientos:", rol.get("conocimientos"))
    lineas += _lista("memoria que consultas ANTES:", rol.get("memoria_consulta"))
    lineas += _lista("memoria que actualizas ANTES de soltar:", rol.get("memoria_actualiza"))
    independencia = rol.get("independencia") or {}
    lineas += ["independencia: " + ("exigida de " + ", ".join(independencia.get("de_quien") or [])
                                    if independencia.get("requiere_independencia")
                                    else "no exigida") + " — " + str(independencia.get("motivo") or "").strip()]
    lineas += _lista("checkpoint cuando:", rol.get("checkpoint"))
    lineas += _lista("devuelves cuando:", rol.get("devolucion"))
    lineas += _lista("te bloquea:", rol.get("bloqueo"))
    lineas += _lista("criterios de calidad:", rol.get("criterios_calidad"))
    lineas += _lista("antipatrones:", rol.get("antipatrones"))

    contrato = brief.get("contrato_operativo")
    lineas += ["", "## 3 · Contrato operativo"]
    if not contrato:
        lineas += ["", "(este rol NO tiene contrato operativo declarado: se ejecuta con su "
                   "contrato de rol y su método; la ausencia se publica, no se disimula)"]
    else:
        lineas += ["", str(contrato["mision_operativa"]).strip(), ""]
        lineas += _lista("conocimientos exigibles:", contrato["conocimientos_exigibles"])
        lineas += _lista("entradas obligatorias (si falta → acción):", [
            e["que"] + " — en " + e["donde"] + " — si falta: " + e["si_falta"]
            for e in contrato["entradas_obligatorias"]])
        lineas += _lista("comprobaciones previas, ANTES de empezar:", [
            c["id"] + ": " + c["comprueba"] + " — cómo: " + c["como"] + " — si falla: "
            + c["si_falla"] for c in contrato["comprobaciones_previas"]])
        lineas += _lista("secuencia:", [
            str(p["n"]) + ". " + p["hace"] + " → produce: " + p["produce"]
            + " → termina cuando: " + p["termina_cuando"] for p in contrato["secuencia"]])
        lineas += _lista("fuentes a consultar:", contrato["fuentes_a_consultar"])
        lineas += _lista("artefactos (tipo · nombre · obligatorio · estructura mínima):", [
            a["tipo"] + " · " + a["nombre"] + " · " + ("OBLIGATORIO" if a["obligatorio"] else
                                                       "opcional") + " · "
            + "; ".join(a["estructura_minima"]) for a in contrato["artefactos"]])
        lineas += _lista("evidencias requeridas:", [
            e["que"] + " — forma: " + e["forma"] + " — la juzga: " + e["quien_la_puede_juzgar"]
            for e in contrato["evidencias_requeridas"]])
        lineas += _lista("criterios de calidad medibles:", [
            c["criterio"] + " — se mide: " + c["como_se_mide"]
            for c in contrato["criterios_de_calidad_medibles"]])
        lineas += _lista("se acepta si:", contrato["condiciones_de_aceptacion"])
        lineas += _lista("se devuelve si:", contrato["condiciones_de_devolucion"])
        lineas += _lista("escalas cuando → a quién → con qué:", [
            r["cuando"] + " → " + r["a_quien"] + " → " + r["con_que"]
            for r in contrato["reglas_de_escalado"]])
        lineas += _lista("incompatibilidades:", contrato["incompatibilidades"])
        lineas += ["", "ejemplo BUENO: " + str(contrato["ejemplo_bueno"]).strip(),
                   "", "ejemplo MALO: " + str(contrato["ejemplo_malo"]).strip()]

    metodo = brief.get("metodo")
    lineas += ["", "## 4 · Método"]
    if metodo:
        lineas += _lista("preguntas iniciales:", metodo.get("preguntas_iniciales"))
        lineas += _lista("carga antes del primer paso:", metodo.get("carga"))
        lineas += _lista("pasos:", [
            str(p["n"]) + ". " + p["nombre"] + " [" + str(p.get("modo") or "") + "] — "
            + str(p["hace"]).strip() + " → termina cuando: " + str(p["termina_cuando"]).strip()
            + (" · CHECKPOINT" if p.get("checkpoint") else "") for p in metodo.get("pasos") or []])
        lineas += _lista("crítica al terminar:", metodo.get("critica"))
        lineas += _lista("consultas con pregunta cerrada:", metodo.get("consultas"))
        lineas += ["prueba de reanudación: " + str(metodo.get("prueba_de_reanudacion") or "").strip()]
    else:
        lineas += ["(sin método declarado en la fila del plan)"]

    gate = brief["gate"]
    lineas += ["", "## 5 · Gate: " + gate["id"], "", "aplica a: " + str(gate.get("aplica_a") or "")]
    lineas += _lista("comprobaciones (cada una se anota en la entrega como si/no/no-aplica):", [
        c["id"] + ": " + c["comprueba"] + " — cómo: " + c["como"] for c in gate["comprobaciones"]])
    lineas += _lista("evidencia exigida:", gate.get("evidencia"))
    lineas += ["si falla: " + str(gate.get("fallo") or "").strip()]

    lineas += ["", "## 6 · Lo que recibes"]
    if brief["recibes"]:
        for entrega in brief["recibes"]:
            lineas += ["", "handoff " + str(entrega.get("id")) + " · " + str(entrega.get("instancia"))
                       + " · de " + str(entrega.get("de")) + " · estado " + str(entrega.get("estado"))]
            lineas += _lista("  artefactos:", entrega.get("artefactos"))
            lineas += _lista("  COMPRUEBA antes de tomar custodia (y acusa, o rechaza):",
                             entrega.get("comprueba_al_recibir"))
            lineas += _lista("  rechaza si:", entrega.get("rechaza_si"))
    else:
        lineas += ["(no hay handoff pendiente de acusar)"]
    if brief["entregas_previas"]:
        lineas += [""] + _lista("entregas previas del item:", [
            str(e["id"]) + " · " + str(e["rol"]) + " · " + str(e["veredicto"]) + " · siguiente: "
            + str(e["siguiente"]) for e in brief["entregas_previas"]])
    if brief["checkpoint"]:
        lineas += ["", "## 7 · Reanudas desde un checkpoint", "",
                   "intento " + str(brief["checkpoint"].get("intento")) + " · titular anterior "
                   + str(brief["checkpoint"].get("titular")),
                   "contenido: " + repr(brief["checkpoint"].get("contenido"))]
    else:
        lineas += ["", "## 7 · Sin checkpoint previo: empiezas desde el paso 1"]

    forma = brief["forma_de_la_entrega"]
    lineas += ["", "## 8 · Cómo entregas", "",
               "La entrega es un JSON con los campos obligatorios: " + ", ".join(forma["obligatorios"]),
               "veredicto ∈ " + ", ".join(forma["veredictos"]),
               "autoevaluacion.gate = " + gate["id"] + " y autoevaluacion.comprobaciones cubre "
               "EXACTAMENTE: " + ", ".join(forma["comprobaciones_del_gate"])]
    if forma["checklist"]:
        lineas += ["autoevaluacion.checklist contesta: " + ", ".join(forma["checklist"])]
    if forma["artefactos_obligatorios"]:
        lineas += _lista("artefactos obligatorios:", [
            a["tipo"] + " · " + a["nombre"] for a in forma["artefactos_obligatorios"]])
    lineas += ["`devuelto` exige devolucion.{que_falta, por_que_es_insuficiente, que_la_cerraria, evidencia}",
               "`bloqueado`/`escalado` exigen bloqueo.{que_lo_impide, que_lo_desbloquearia, autoridad[, posturas]}"]
    if brief["ordenes"]:
        lineas += [""] + _lista("órdenes:", [k + ": " + str(v) for k, v in sorted(brief["ordenes"].items())])
    lineas += ["", "## 9 · Prohibiciones"] + [""] + ["· " + p for p in brief["prohibiciones"]]
    if brief["instrucciones_del_proyecto"]:
        lineas += ["", "## 10 · Instrucciones del proyecto"] + [""] + [
            "· " + i for i in brief["instrucciones_del_proyecto"]]
    if brief.get("prompt"):
        lineas += ["", "## 11 · Prompt operativo del rol", "", brief["prompt"].rstrip()]
    return "\n".join(lineas) + "\n"
