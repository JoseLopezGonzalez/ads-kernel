#!/usr/bin/env python3
"""supervisor — el BUCLE de ejecución que no vive en ningún chat.

    «El final de una conversación NO debe equivaler al final de la ejecución. El chat es
     solamente una interfaz del Owner con el ADS. No es el runtime del ADS.»
                                                            — el Owner, 2026-09-14

HECHO MEDIDO ANTES DE CONSTRUIR: `ads_runtime.py ciclo` era UN barrido, y nada lo repetía.
Un paquete elegible se despachaba si alguien tecleaba la orden; si nadie la tecleaba, la
cola se quedaba quieta con trabajo autorizado delante. Este módulo es lo que la repite: un
proceso que da PASADAS sobre el estado hasta que se cumple una condición LEGÍTIMA de
parada, y sólo una de éstas:

    sin-trabajo          no queda ningún paquete que despachar, tomar ni esperar
    todo-en-manos-ajenas lo que queda lo tienen trabajadores externos vivos: se espera
    bloqueado            lo que queda está bloqueado: hace falta un desbloqueador o una
                         decisión, y eso no lo decide el supervisor
    marcado              hay transacciones marcadas o reconciliaciones de `g.9` abiertas:
                         la autoridad decide, y el runtime no despacha nada
    pasadas-agotadas     el tope de pasadas que se le dio, para que un bucle sin límite no
                         sea posible por construcción

En cada pasada el supervisor hace TRES cosas, y las tres son de la máquina que ya existía:
(1) `Runtime.ciclo()`, que sanea lo que quedó a medias, recupera leases muertos y despacha
lo elegible por el adaptador que corresponda; (2) para los paquetes de AGENTE, escribe el
BRIEF en el espacio del adaptador ANTES de que `ciclo()` los despache, porque el agente sin
chat lee ahí; (3) para los despachados con entrega, cierra el circuito de la oficina:
registra la entrega, dictamina, emite handoffs, abre correcciones. Los paquetes EXTERNOS
(`worker`) no los ejecuta: los publica como tomables y espera.

DECISIÓN · varias pasadas en un proceso, varios procesos si se quiere paralelismo
    Cada supervisor es UNA instancia del runtime y despacha paquetes en serie. El
    paralelismo real se obtiene lanzando N supervisores con N instancias distintas sobre
    el mismo control repo: los leases serializan, y dos supervisores no pueden despachar el
    mismo paquete (`T182`). No se ha construido un planificador de hilos porque el estado
    durable ya es el árbitro y otro árbitro en memoria sería el segundo sistema de estado.

DECISIÓN · el supervisor NO decide por el Owner, y lo dice en su informe
    Si la única salida es una decisión, la pasada termina en `bloqueado` con la lista de
    lo bloqueado y de quién es la autoridad. No inventa un desbloqueador que amplíe el
    alcance (`b.15.1`), y no cancela nada.
"""
from __future__ import annotations

import json
import os

from . import externo
from .errores import RuntimeInconsistente

PARADAS = ("sin-trabajo", "todo-en-manos-ajenas", "bloqueado", "marcado", "pasadas-agotadas",
           "hay-trabajo", "riesgo-extraordinario", "barrera-externa")
# Directiva §36: el ejecutor solo interrumpe al Owner por (2) una decision que solo el puede
# tomar, (3) un riesgo extraordinario o (4) una barrera externa. Las dos ultimas son paradas
# PROPIAS, derivadas de la clase del bloqueo que la entrega declaro; `bloqueado` sigue
# cubriendo la decision y la dependencia interna.
PARADAS_QUE_NECESITAN_AL_OWNER = ("riesgo-extraordinario", "barrera-externa")

PASADAS_POR_DEFECTO = 1
ESPERA_ENTRE_PASADAS_SEGUNDOS = 2.0


class Supervisor:
    """Pasadas sobre el estado hasta una condición legítima de parada."""

    def __init__(self, runtime, *, corpus=None, adaptador_de_agente=None, brief_de=None,
                 tras_completar=None, espera=ESPERA_ENTRE_PASADAS_SEGUNDOS, reloj=None):
        self.runtime = runtime
        self.corpus = corpus
        self.adaptador = adaptador_de_agente
        self.brief_de = brief_de
        self.tras_completar = tras_completar
        self.espera = float(espera)
        # El reloj lo INYECTA quien manda (el punto ejecutable, con `time.sleep`): en este
        # paquete no entra ningún reloj, `T183` lo mide. Sin reloj no se espera entre pasadas.
        self.reloj = reloj if callable(reloj) else (lambda segundos: None)

    # ------------------------------------------------------------------ una pasada
    def pasada(self, *, maximo=0):
        """UNA pasada: briefs, barrido, cierre de la oficina. Devuelve el informe."""
        rt = self.runtime
        informe = {"instancia": rt.instancia, "briefs": [], "atendidos": [], "oficina": [],
                   "externos": [], "reofrecidos": [], "parada": None, "motivo": ""}
        if rt.marcado:
            informe["parada"] = "marcado"
            informe["motivo"] = "la recuperación dejó transacciones MARCADAS: la autoridad decide"
            return informe
        # (2) briefs para los paquetes de AGENTE que van a despacharse en esta pasada.
        if self.adaptador is not None and self.brief_de is not None:
            for entrada in rt.elegibles():
                paquete = rt._leer_paquete(entrada["paquete"])
                if str(paquete["orden"].get("adaptador")) != self.adaptador.identificador:
                    continue
                if os.path.isfile(self.adaptador.ruta_de_brief(paquete["id"])):
                    continue
                try:
                    brief, texto = self.brief_de(paquete["id"])
                except Exception as exc:                      # noqa: BLE001 — se publica
                    informe["briefs"].append({"paquete": paquete["id"], "error": str(exc)})
                    continue
                self.adaptador.escribir_brief(paquete["id"], texto, brief)
                informe["briefs"].append({"paquete": paquete["id"], "huella": brief["huella"]})
        # (1) el barrido de la máquina que ya existía.
        barrido = rt.ciclo(maximo=maximo)
        informe["atendidos"] = barrido.get("atendidos") or []
        informe["externos"] = barrido.get("externos") or []
        informe["reofrecidos"] = barrido.get("reofrecidos") or []
        informe["reconciliaciones_pendientes"] = barrido.get("reconciliaciones_pendientes") or []
        # (3) el cierre de la oficina para lo que un agente entregó.
        if self.tras_completar is not None:
            for atendido in informe["atendidos"]:
                if atendido.get("desenlace") != "completado":
                    continue
                try:
                    informe["oficina"].append(self.tras_completar(atendido["paquete"]))
                except Exception as exc:                      # noqa: BLE001 — se publica
                    informe["oficina"].append({"paquete": atendido["paquete"],
                                               "error": str(exc)})
        informe["parada"], informe["motivo"] = self._condicion_de_parada(informe)
        return informe

    def _condicion_de_parada(self, informe):
        rt = self.runtime
        if rt.marcado or informe.get("reconciliaciones_pendientes"):
            return "marcado", "reconciliaciones de g.9 abiertas o transacciones marcadas"
        paquetes = rt._todos_los_paquetes()
        abiertos = [p for p in paquetes if p["estado"] not in ("completado", "cancelado")]
        if not abiertos:
            return "sin-trabajo", "no queda ningún paquete abierto"
        elegibles = rt.elegibles()
        propios = [e for e in elegibles if not externo.es_externo(rt._leer_paquete(e["paquete"]))]
        if propios:
            return "hay-trabajo", str(len(propios)) + " paquete(s) despachable(s) en la siguiente pasada"
        tomables = rt.tomables()
        if tomables["tomables"]:
            return "todo-en-manos-ajenas", (str(len(tomables["tomables"])) + " paquete(s) tomable(s) "
                                            "esperan a un trabajador")
        en_curso = [p for p in abiertos if p["estado"] in ("despachado", "ejecutando")]
        if en_curso:
            return "todo-en-manos-ajenas", ", ".join(p["id"] for p in en_curso) + " en manos de otros"
        bloqueados = [p for p in abiertos if p["estado"] in ("bloqueado", "agotado", "pausado")]
        for clase in PARADAS_QUE_NECESITAN_AL_OWNER:
            propios = [p for p in bloqueados if p.get("clase_de_bloqueo") == clase]
            if propios:
                return clase, (clase + ": " + ", ".join(p["id"] + " (" + str(p.get("motivo_de_bloqueo") or p.get("motivo") or "") + ")"
                                                         for p in propios)
                               + ("; lo escala el Owner (§36.3)" if clase == "riesgo-extraordinario"
                                  else "; no se resuelve autónomamente (§36.4)"))
        if bloqueados:
            return "bloqueado", ("bloqueados: " + ", ".join(p["id"] for p in bloqueados)
                                 + "; hace falta un desbloqueador o una decisión")
        return "bloqueado", "queda trabajo que ninguna pasada puede mover: " + ", ".join(
            p["id"] + "(" + p["estado"] + ")" for p in abiertos)

    # ------------------------------------------------------------------ el bucle
    def bucle(self, *, pasadas=PASADAS_POR_DEFECTO, maximo=0, hasta=("sin-trabajo", "bloqueado",
                                                                    "marcado", "riesgo-extraordinario",
                                                                    "barrera-externa")):
        """Repite pasadas hasta una parada legítima o hasta agotar `pasadas`. NUNCA infinito."""
        if not isinstance(pasadas, int) or isinstance(pasadas, bool) or pasadas < 1:
            raise RuntimeInconsistente("`pasadas` es un entero >= 1: un bucle sin tope no se "
                                       "construye")
        historial = []
        for numero in range(1, pasadas + 1):
            informe = self.pasada(maximo=maximo)
            informe["pasada"] = numero
            historial.append(informe)
            if informe["parada"] in hasta:
                return {"parada": informe["parada"], "motivo": informe["motivo"],
                        "pasadas": historial}
            if numero < pasadas and informe["parada"] in ("todo-en-manos-ajenas", "hay-trabajo"):
                self.reloj(self.espera)
        ultimo = historial[-1]
        return {"parada": "pasadas-agotadas" if ultimo["parada"] not in hasta else ultimo["parada"],
                "motivo": ultimo["motivo"], "pasadas": historial}


def como_texto(resultado):
    lineas = ["SUPERVISOR · parada: " + str(resultado["parada"]) + " · " + str(resultado["motivo"])]
    for pasada in resultado["pasadas"]:
        atendidos = ", ".join(str(a.get("paquete")) + ":" + str(a.get("desenlace"))
                              for a in pasada["atendidos"]) or "(nada)"
        lineas.append("  pasada " + str(pasada["pasada"]) + " · atendidos " + atendidos
                      + " · externos " + str(len(pasada["externos"])) + " · briefs "
                      + str(len(pasada["briefs"])) + " · parada " + str(pasada["parada"]))
        for cierre in pasada["oficina"]:
            lineas.append("    oficina: " + json.dumps(cierre, sort_keys=True, ensure_ascii=False)[:160])
    return "\n".join(lineas) + "\n"
