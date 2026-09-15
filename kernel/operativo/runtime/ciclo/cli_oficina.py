#!/usr/bin/env python3
"""cli_oficina — las ÓRDENES de la oficina para `ads_ciclo.py`. Sin lógica propia.

Cada orden compone piezas de `oficina.py`, `tablero.py`, `terminacion.py` y
`runtime/supervisor.py`, y publica el resultado por el mismo `_emitir` de `ads_ciclo.py`.
Vive aparte para que `ads_ciclo.py` no crezca en lógica: aquí sólo hay traducción de la
línea de órdenes a llamadas, y ninguna decisión que no esté ya en un módulo probado.

DECISIÓN · el trabajador ES `--instancia`
    No hay `--worker`: el trabajador es la instancia del runtime, que es el titular del
    lease. Un `--instancia trabajador-jose-1` en `tomar` y el mismo en `entregar` son lo
    que hace que la autoridad sobre el paquete se conserve entre las dos órdenes.

DECISIÓN · el circuito base se lee del PROFILE por `--clase-de-trabajo`
    Es donde el proyecto lo declara. Sin clase no hay circuito, y sin circuito ni el brief
    puede decir qué niveles se exigen ni el cierre puede exigirlos: la orden lo dice.
"""
from __future__ import annotations

import json
import os
import time


def _cargar(argumentos, corpus):
    from ciclo import terminacion                                     # noqa: PLC0415
    clase = getattr(argumentos, "clase_de_trabajo", None)
    if not clase:
        return None
    circuitos = terminacion.cargar_circuitos_base(argumentos.repo, corpus=corpus)
    return terminacion.circuito_de(circuitos, clase)


def _leer_json(ruta):
    with open(ruta, "r", encoding="utf-8") as manejador:
        return json.load(manejador)


def _hechos(argumentos):
    hechos = {}
    for par in (getattr(argumentos, "hecho", None) or []):
        if "=" not in par:
            raise ValueError("un hecho se escribe `nombre=valor`; llegó " + repr(par))
        nombre, valor = par.split("=", 1)
        if valor.lower() in ("true", "false"):
            hechos[nombre] = valor.lower() == "true"
        elif "," in valor:
            hechos[nombre] = [v for v in valor.split(",") if v]
        else:
            hechos[nombre] = valor
    return hechos


def orden_tomar(argumentos, *, abrir, corpus, emitir):
    from ciclo import oficina                                         # noqa: PLC0415
    circuito = _cargar(argumentos, corpus)
    with abrir(argumentos) as rt:
        if not argumentos.paquete:
            tomables = rt.tomables()
            return emitir(argumentos, tomables, [
                "tomables      " + (", ".join(t["paquete"] for t in tomables["tomables"]) or "(nada)"),
                "esperando     " + (", ".join(t["paquete"] + " (" + (t.get("titular") or ", ".join(
                    t.get("espera_a") or [])) + ")" for t in tomables["esperando"]) or "(nada)"),
            ])
        resultado = oficina.tomar(
            rt, corpus=corpus, paquete=argumentos.paquete, circuito=circuito,
            ordenes=_ordenes_del_brief(argumentos),
        )
    if argumentos.brief_a:
        with open(argumentos.brief_a, "w", encoding="utf-8") as manejador:
            manejador.write(resultado["brief_md"])
    salida = dict(resultado)
    salida.pop("brief_md", None)
    return emitir(argumentos, salida, [
        "tomado        " + argumentos.paquete + " · intento " + str(resultado["toma"]["intento"])
        + " · efecto " + str(resultado["toma"]["efecto"]),
        "rol           " + str(resultado["brief"]["rol"]["id"]),
        "recibes       " + (", ".join(h["id"] for h in resultado["brief"]["recibes"]) or "(nada que acusar)"),
        "brief         " + (argumentos.brief_a or "(no escrito: usa --brief-a <fichero>)"),
    ] + ([] if argumentos.brief_a else resultado["brief_md"].splitlines()))


def _ordenes_del_brief(argumentos):
    return {
        "checkpoint": "python3 kernel/operativo/runtime/ads_ciclo.py --repo <repo> --instancia "
                      "<tu instancia> checkpoint --paquete <paquete> --contenido <fichero.json>",
        "entregar": "python3 kernel/operativo/runtime/ads_ciclo.py --repo <repo> --instancia "
                    "<tu instancia> entregar --paquete <paquete> --entrega <fichero.json>",
        "acusar": "python3 kernel/operativo/runtime/ads_ciclo.py --repo <repo> --instancia "
                  "<tu instancia> acusar --handoff <id> --comprobacion <texto> ...",
    }


def orden_soltar(argumentos, *, abrir, corpus, emitir):
    with abrir(argumentos) as rt:
        objeto = rt.soltar(argumentos.paquete)
    return emitir(argumentos, objeto, ["soltado       " + argumentos.paquete + " · queda `"
                                       + objeto["estado"] + "`"])


def orden_checkpoint(argumentos, *, abrir, corpus, emitir):
    contenido = _leer_json(argumentos.contenido) if argumentos.contenido else {
        "nota": argumentos.nota or ""}
    with abrir(argumentos) as rt:
        cuerpo = rt.checkpoint(argumentos.paquete, contenido)
    return emitir(argumentos, cuerpo, ["checkpoint    " + argumentos.paquete + " · intento "
                                       + str(cuerpo["intento"]) + " · titular " + cuerpo["titular"]])


def orden_entregar(argumentos, *, abrir, corpus, emitir):
    from ciclo import oficina                                         # noqa: PLC0415
    circuito = _cargar(argumentos, corpus)
    entrega = _leer_json(argumentos.entrega)
    with abrir(argumentos) as rt:
        resultado = oficina.entregar(rt, corpus=corpus, paquete=argumentos.paquete,
                                     entrega=entrega, circuito=circuito)
    lineas = ["entregado     " + argumentos.paquete + " · " + resultado["veredicto"]
              + " · entrega " + resultado["entrega"]["id"]]
    for dictamen in resultado.get("dictamenes") or []:
        lineas.append("dictamen      " + dictamen["gate"] + " = " + dictamen["dictamen"])
    if resultado.get("handoffs_emitidos"):
        lineas.append("handoffs      " + ", ".join(resultado["handoffs_emitidos"]))
    if resultado.get("correccion"):
        lineas.append("correccion    " + resultado["correccion"]["correccion"] + " · nuevo receptor "
                      + resultado["correccion"]["receptor"])
    if resultado.get("cierre"):
        lineas.append("salida        " + resultado["cierre"]["salida"] + " · " + resultado["cierre"]["motivo"])
    return emitir(argumentos, resultado, lineas)


def orden_acusar(argumentos, *, abrir, corpus, emitir):
    from ciclo import oficina                                         # noqa: PLC0415
    with abrir(argumentos) as rt:
        if argumentos.rechazar:
            resultado = oficina.rechazar(rt, corpus=corpus, handoff=argumentos.handoff,
                                         motivo=argumentos.motivo or "",
                                         paquete_receptor=argumentos.paquete)
            return emitir(argumentos, resultado, [
                "rechazado     " + argumentos.handoff + " · corrección "
                + resultado["correccion"] + " · nuevo receptor " + resultado["receptor"]])
        entrega = rt.almacen.leer("handoffs/" + argumentos.handoff + ".json")
        comprobaciones = list(argumentos.comprobacion or []) or list(entrega["comprueba_al_recibir"]) \
            if argumentos.todas else list(argumentos.comprobacion or [])
        resultado = oficina.acusar(rt, corpus=corpus, handoff=argumentos.handoff,
                                   comprobaciones_superadas=comprobaciones)
    return emitir(argumentos, resultado, ["acusado       " + argumentos.handoff
                                          + " · custodia " + resultado["custodia"]])


def orden_brief(argumentos, *, abrir, corpus, emitir):
    from ciclo import briefs, oficina                                 # noqa: PLC0415
    circuito = _cargar(argumentos, corpus)
    with abrir(argumentos) as rt:
        brief = oficina.brief_de(rt, corpus=corpus, paquete=argumentos.paquete,
                                 circuito=circuito, ordenes=_ordenes_del_brief(argumentos))
    texto = briefs.como_markdown(brief)
    if argumentos.brief_a:
        with open(argumentos.brief_a, "w", encoding="utf-8") as manejador:
            manejador.write(texto)
        return emitir(argumentos, brief, ["brief         " + argumentos.brief_a + " · huella "
                                          + brief["huella"]])
    return emitir(argumentos, brief, texto.splitlines())


def orden_cronica(argumentos, *, abrir, corpus, emitir):
    from ciclo import cronica                                          # noqa: PLC0415
    with abrir(argumentos) as rt:
        filas = cronica.derivar(rt.almacen, item=getattr(argumentos, "item", None) or None)
    return emitir(argumentos, {"sucesos": filas, "por_trabajador": cronica.por_trabajador(filas)},
                  cronica.como_texto(filas).splitlines())


def orden_tablero(argumentos, *, abrir, corpus, emitir):
    from ciclo import tablero                                         # noqa: PLC0415
    with abrir(argumentos) as rt:
        vista = tablero.derivar(rt, corpus=corpus)
    return emitir(argumentos, vista, tablero.como_texto(vista).splitlines())


def orden_terminacion(argumentos, *, abrir, corpus, emitir):
    from ciclo import oficina                                         # noqa: PLC0415
    circuito = _cargar(argumentos, corpus)
    if circuito is None:
        raise ValueError("`terminacion` exige --clase-de-trabajo para leer el circuito base")
    with abrir(argumentos) as rt:
        evaluacion = oficina.evaluar_terminacion(rt, corpus=corpus, item=argumentos.item,
                                                 circuito=circuito, hechos=_hechos(argumentos))
    return emitir(argumentos, evaluacion, ["item          " + argumentos.item + " · circuito "
                                           + evaluacion["circuito"]] + [
        "  " + f["nivel"].ljust(20) + f["estado"].ljust(12) + f["motivo"] for f in evaluacion["niveles"]
    ] + ["nivel         " + str(evaluacion["nivel_mas_alto"]) + " · puede cerrar: "
         + ("sí" if evaluacion["puede_cerrar"] else "NO: faltan " + ", ".join(evaluacion["faltan"]))])


def orden_aceptar(argumentos, *, abrir, corpus, emitir):
    from ciclo import oficina                                         # noqa: PLC0415
    with abrir(argumentos) as rt:
        cuerpo = oficina.aceptar(
            rt, corpus=corpus, item=argumentos.item,
            comprobaciones_superadas=list(argumentos.comprobacion or []),
            evidencia=list(argumentos.evidencia or []), hallazgos=list(argumentos.hallazgo or []),
        )
    return emitir(argumentos, cuerpo, ["aceptacion    " + argumentos.item + " · " + cuerpo["dictamen"]
                                       + (" · pendientes " + ", ".join(cuerpo["comprobaciones_pendientes"])
                                          if cuerpo["comprobaciones_pendientes"] else "")])


def orden_cerrar_item(argumentos, *, abrir, corpus, emitir):
    from ciclo import oficina                                         # noqa: PLC0415
    circuito = _cargar(argumentos, corpus)
    if circuito is None:
        raise ValueError("`cerrar-item` exige --clase-de-trabajo para leer el circuito base")
    with abrir(argumentos) as rt:
        resultado = oficina.cerrar_item(
            rt, corpus=corpus, item=argumentos.item, circuito=circuito, hechos=_hechos(argumentos),
            integracion={"propietario_global": argumentos.propietario,
                         "declaracion": argumentos.declaracion or ""},
            aprendizaje=argumentos.aprendizaje or "none",
        )
    return emitir(argumentos, resultado, ["cerrado       " + argumentos.item + " · "
                                          + resultado["cierre"]["salida"]])


def orden_supervisar(argumentos, *, abrir, corpus, emitir, registro):
    from ciclo import briefs, oficina                                 # noqa: PLC0415
    from runtime import supervisor as modulo_supervisor               # noqa: PLC0415
    circuito = _cargar(argumentos, corpus)
    adaptador = None
    for candidato in (registro(argumentos)._por_identificador.values()
                      if registro(argumentos) is not None else []):
        if getattr(candidato, "identificador", "") == "agente":
            adaptador = candidato
    with abrir(argumentos) as rt:
        def brief_de(paquete):
            brief = oficina.brief_de(rt, corpus=corpus, paquete=paquete, circuito=circuito,
                                     ordenes={"entregar": "escribe la entrega en {entrega}"})
            return brief, briefs.como_markdown(brief)

        def tras_completar(paquete):
            return oficina.registrar_entrega_de_agente(rt, corpus=corpus, paquete=paquete,
                                                       circuito=circuito)

        sup = modulo_supervisor.Supervisor(
            rt, corpus=corpus, adaptador_de_agente=adaptador, brief_de=brief_de,
            tras_completar=tras_completar, espera=argumentos.espera, reloj=time.sleep,
        )
        resultado = sup.bucle(pasadas=argumentos.pasadas, maximo=argumentos.maximo)
    return emitir(argumentos, resultado, modulo_supervisor.como_texto(resultado).splitlines())
