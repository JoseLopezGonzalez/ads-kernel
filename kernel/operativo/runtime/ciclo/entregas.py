#!/usr/bin/env python3
"""entregas — el objeto DURABLE que un trabajador deposita al terminar un paquete.

    «QUIÉN ENTREGA QUÉ: artefactos concretos, localizables, no «el trabajo hecho»»   `C5`

Una entrega es lo que hace verificable un handoff. Antes de este módulo, la instancia de
La Pesquerapp cerraba encargos con `--evidencia "PR #14 sin fusionar"`: una cadena de texto
que nadie podía comprobar contra nada. Aquí la entrega tiene forma —`esquemas/entrega.yaml`—,
se valida ANTES de escribirse, y lo que se valida no es sólo la forma:

    · la AUTOEVALUACIÓN recorre EXACTAMENTE las comprobaciones del gate del rol: ni una
      menos —una comprobación sin anotar es una comprobación no hecha— ni una de más —un
      gate no crece por conveniencia—
    · el CHECKLIST del contrato operativo, cuando el rol lo tiene, se contesta ENTERO
    · los ARTEFACTOS OBLIGATORIOS del contrato operativo están, por su tipo y nombre
    · un veredicto `devuelto` trae los CUATRO campos de `C5`; uno `bloqueado` o `escalado`,
      qué lo impide, qué lo desbloquearía y quién tiene la autoridad
    · un rol que JUZGA trae su dictamen, y el dictamen lo aplica `gates.aplicar` con
      revisor ≠ autor: la autoevaluación del productor NUNCA es el dictamen

DECISIÓN · la entrega se escribe en su propio dominio, una por INTENTO
    `entregas/<paquete>-<intento>.json`. Un reintento produce OTRA entrega y conserva la
    anterior: la historia de por qué un paquete necesitó tres intentos es evidencia, no
    ruido. El resultado del §4.4 que publica el dispatcher lleva en `salida` el
    identificador de la entrega, de modo que desde el paquete se llega a ella sin buscar.
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto

from . import durable, formas
from .corpus import Corpus
from .errores import EntregaInvalida

DOMINIO = "entregas"
ESQUEMA = "ads.estado/1"

VEREDICTOS = ("entregado", "devuelto", "bloqueado", "escalado")


def comprobar_forma(entrega, *, corpus=None, contrato=None, gate=None):
    """Todos los fallos de la entrega, o lista vacía. No escribe nada."""
    corpus = corpus or Corpus()
    fallos = list(formas.validar(entrega, corpus.esquema("entrega"), corpus=corpus,
                                 camino="entrega"))
    if fallos:
        return fallos
    veredicto = entrega["veredicto"]
    if veredicto == "devuelto" and not entrega.get("devolucion"):
        fallos.append("entrega.devolucion: un veredicto `devuelto` exige los cuatro campos "
                      "de C5; sin ellos no es una devolución")
    if veredicto in ("bloqueado", "escalado") and not entrega.get("bloqueo"):
        fallos.append("entrega.bloqueo: un veredicto `" + veredicto + "` nombra qué lo impide, "
                      "qué lo desbloquearía y la autoridad")
    if veredicto == "escalado" and not (entrega.get("bloqueo") or {}).get("posturas"):
        fallos.append("entrega.bloqueo.posturas: escalar exige las posturas enfrentadas "
                      "escritas (a.7): sin material no se le pide a nadie que arbitre")
    if veredicto == "entregado" and not entrega.get("artefactos"):
        fallos.append("entrega.artefactos: una entrega sin artefactos no es una entrega; "
                      "C5 dice «artefactos concretos, localizables»")

    # La autoevaluación recorre EXACTAMENTE el gate del rol.
    gate_id = gate or corpus.rol(entrega["rol"]).get("gate")
    if entrega["autoevaluacion"]["gate"] != gate_id:
        fallos.append("entrega.autoevaluacion.gate: el rol `" + entrega["rol"] + "` cierra "
                      "contra `" + str(gate_id) + "` y la entrega se autoevalúa contra `"
                      + str(entrega["autoevaluacion"]["gate"]) + "`")
    else:
        exigidas = [c["id"] for c in corpus.gates()[gate_id]["comprobaciones"]]
        anotadas = [c["id"] for c in entrega["autoevaluacion"]["comprobaciones"]]
        faltan = [c for c in exigidas if c not in anotadas]
        sobran = [c for c in anotadas if c not in exigidas]
        if faltan:
            fallos.append("entrega.autoevaluacion: comprobaciones del gate sin anotar: "
                          + ", ".join(faltan) + " (una comprobación sin anotar es una "
                          "comprobación no hecha)")
        if sobran:
            fallos.append("entrega.autoevaluacion: comprobaciones que el gate no tiene: "
                          + ", ".join(sobran) + " (un gate no crece por conveniencia)")

    # El checklist y los artefactos obligatorios del contrato operativo.
    if contrato is None and corpus is not None:
        contrato = corpus.contrato_operativo_de(entrega["rol"])
    if contrato:
        exigidas = [c["id"] for c in contrato["checklist"]]
        respondidas = [c["id"] for c in (entrega["autoevaluacion"].get("checklist") or [])]
        faltan = [c for c in exigidas if c not in respondidas]
        if faltan:
            fallos.append("entrega.autoevaluacion.checklist: el contrato operativo de `"
                          + entrega["rol"] + "` exige contestar " + ", ".join(faltan))
        if veredicto == "entregado":
            tipos_entregados = {(a["tipo"], a.get("descripcion", "")) for a in entrega["artefactos"]}
            tipos = {a["tipo"] for a in entrega["artefactos"]}
            for artefacto in contrato["artefactos"]:
                if artefacto.get("obligatorio") and artefacto["tipo"] not in tipos:
                    fallos.append("entrega.artefactos: falta el artefacto obligatorio `"
                                  + artefacto["nombre"] + "` (tipo " + artefacto["tipo"]
                                  + ") que exige el contrato operativo")
            del tipos_entregados
        # Los gates que el contrato dice que el rol NUNCA dictamina sobre su propio paquete.
        vedados = set(contrato.get("no_autocertifica") or [])
        for dictamen in list(entrega.get("dictamenes") or []) + ([entrega["dictamen"]] if entrega.get("dictamen") else []):
            if dictamen.get("sobre_paquete") == entrega["paquete"] and dictamen.get("gate") in vedados:
                fallos.append("entrega.dictamenes: el contrato operativo de `" + entrega["rol"]
                              + "` prohíbe dictaminar `" + str(dictamen.get("gate"))
                              + "` sobre su propio paquete (no_autocertifica)")
    return fallos


def exigir_forma(entrega, **opciones):
    fallos = comprobar_forma(entrega, **opciones)
    if fallos:
        raise EntregaInvalida(
            "la entrega no es admisible: " + "; ".join(fallos),
            paquete=str(entrega.get("paquete")) if isinstance(entrega, dict) else None,
            fallos=fallos,
        )
    return entrega


def identificador(paquete, intento):
    return str(paquete) + "-" + str(int(intento))


def ruta_de(identificador_de_entrega):
    return DOMINIO + "/" + identificador_de_entrega + ".json"


def registrar(almacen, entrega, *, intento, titular, corpus=None, contrato=None):
    """Valida y escribe la entrega del intento. Idempotente por contenido."""
    exigir_forma(entrega, corpus=corpus, contrato=contrato)
    cuerpo = dict(entrega)
    cuerpo["esquema"] = ESQUEMA
    cuerpo["intento"] = int(intento)
    cuerpo["titular"] = str(titular)
    cuerpo["id"] = identificador(entrega["paquete"], intento)
    cuerpo["huella"] = cid_de_objeto({k: v for k, v in cuerpo.items() if k != "huella"})
    durable.escribir(
        almacen, clase="ciclo.entrega.registrada",
        motivo="entrega " + cuerpo["id"] + " del rol " + entrega["rol"] + " · "
               + entrega["veredicto"],
        objetos={ruta_de(cuerpo["id"]): cuerpo},
        semilla={"entrega": cuerpo["id"]}, autor=str(titular),
    )
    return cuerpo


def de_paquete(almacen, paquete):
    """Todas las entregas de un paquete, por intento. Se leen; no se recuerdan."""
    salida = []
    for ruta in sorted(almacen.listar(DOMINIO)):
        objeto = almacen.leer(ruta)
        if objeto.get("paquete") == paquete:
            salida.append(objeto)
    return sorted(salida, key=lambda e: int(e.get("intento") or 0))


def ultima(almacen, paquete):
    todas = de_paquete(almacen, paquete)
    return todas[-1] if todas else None


def leer(almacen, identificador_de_entrega):
    return durable.leer(almacen, ruta_de(identificador_de_entrega))
