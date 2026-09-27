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
    · los ARTEFACTOS OBLIGATORIOS del contrato operativo están, cada uno con el SUYO —por su
      tipo y por el nombre que declara `cumple`— y con su estructura mínima entera
      (`_artefactos_del_contrato`; hasta el 2026-09-26 sólo se miraba el tipo)
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
from .errores import CorpusIlegible, CorpusIncompleto, EntregaInvalida

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
    if veredicto == "escalado" and entrega.get("bloqueo"):
        # Directiva §20, §41, §76 (OWN-ADS-0074, 0161, 0271): no se escala lo que la
        # capacidad DECIDE SOLA. La materia se nombra entre las que su ficha declara que
        # ESCALA; una de `decide_sola` se rechaza, y una que no está en ninguna lista también:
        # escalar no es una opinión libre, es una cláusula de autoridad.
        fallos.extend(_materia_escalable(entrega, corpus))
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
            fallos.extend(_artefactos_del_contrato(entrega, contrato))
    if veredicto == "entregado" and corpus is not None:
        fallos.extend(_dictamenes_del_rol(entrega, corpus))
        # Los gates que el contrato dice que el rol NUNCA dictamina sobre su propio paquete.
        vedados = set(contrato.get("no_autocertifica") or [])
        for dictamen in list(entrega.get("dictamenes") or []) + ([entrega["dictamen"]] if entrega.get("dictamen") else []):
            if dictamen.get("sobre_paquete") == entrega["paquete"] and dictamen.get("gate") in vedados:
                fallos.append("entrega.dictamenes: el contrato operativo de `" + entrega["rol"]
                              + "` prohíbe dictaminar `" + str(dictamen.get("gate"))
                              + "` sobre su propio paquete (no_autocertifica)")
    return fallos


def _dictamenes_del_rol(entrega, corpus):
    """T516 · Un rol que DICTAMINA un gate no entrega `entregado` sin su dictamen.

    DEFECTO MEDIDO con un modelo real (La Pesquerapp, 2026-09-27): VER/dosier entregó
    `entregado` con un dosier impecable y SIN dictamen de `gate:evidencia-suficiente`, porque
    su brief le decía que nunca dictamina su gate sobre su propio paquete y entendió que lo
    firmaba otro. Ese gate declara `dictamina: VER/dosier`: nadie más puede dictaminarlo, y la
    oficina lo admitió, así que el nivel `verificado` se quedó sin quien lo alcanzara. El
    dictamen es SOBRE el paquete que el rol juzga, no sobre el suyo; y no cabe `entregado` sin
    él: si no se supera, el veredicto es `devuelto` con el dictamen `no-superado`.
    """
    rol = entrega["rol"]
    emitidos = {str(d.get("gate")) for d in (entrega.get("dictamenes") or [])
                if isinstance(d, dict)} | ({str(entrega["dictamen"].get("gate"))}
                                           if isinstance(entrega.get("dictamen"), dict) else set())
    fallos = []
    for gate in corpus.gates().values():
        if str(gate.get("dictamina") or "") == rol and gate["id"] not in emitidos:
            fallos.append("entrega.dictamenes: `" + rol + "` dictamina `" + gate["id"] + "` y entrega "
                          "sin su dictamen. Es SOBRE el paquete que juzgas (no el tuyo), nadie más "
                          "puede emitirlo y sin él el nivel no se alcanza nunca; si no se supera, "
                          "el veredicto es `devuelto` con el dictamen `no-superado` (T516)")
    return fallos


def _normal(texto):
    """Minúsculas, sin tildes y sin espacios repetidos: la misma pieza escrita igual."""
    import unicodedata  # noqa: PLC0415
    plano = unicodedata.normalize("NFKD", str(texto or "")).encode("ascii", "ignore").decode("ascii")
    return " ".join(plano.lower().split())


def _es_hueco(texto):
    """Un valor que todavía es la pista de la plantilla, o nada."""
    t = str(texto or "").strip()
    return not t or (t.startswith("<") and t.endswith(">"))


def _artefactos_del_contrato(entrega, contrato):
    """Cada artefacto obligatorio del contrato tiene SU artefacto entregado, y entero.

    HALLAZGO del 2026-09-26 (revisión independiente G13 del ledger de La Pesquerapp): esta
    comprobación miraba sólo que hubiera ALGÚN artefacto de cada TIPO obligatorio. Un único
    `documento` cumplía los dos obligatorios de `DIS/investigacion-ux` y los tres de
    `DIS/direccion-artistica`; la estructura mínima de cada uno no se miraba nunca; y el
    conjunto que calculaba tipo y descripción se construía y se borraba sin usarse. Los
    fixtures de las baterías entregaban un artefacto de cada tipo, que es exactamente el
    atajo, y una entrega con commits «de laboratorio» se admitió con un modelo real.

    Ahora, para cada artefacto obligatorio del contrato:
      · hay un artefacto entregado de su TIPO que declara `cumple: <su nombre>`; cada
        artefacto entregado cumple uno solo, así que tres obligatorios son tres entregados
      · si el contrato le fija `estructura_minima`, el entregado la declara ENTERA en
        `estructura`: cada apartado con `donde` está (sección, línea, ancla) y sin pistas
        de plantilla por rellenar
    Que el apartado diga de verdad lo que promete lo juzga quien revisa (G13), no esto: el
    mecanismo exige que no falte ninguno y que cada uno se pueda ir a mirar.
    """
    fallos = []
    entregados = list(entrega.get("artefactos") or [])
    for artefacto in contrato.get("artefactos") or []:
        if not artefacto.get("obligatorio"):
            continue
        nombre = str(artefacto["nombre"])
        suyos = [a for a in entregados
                 if a.get("tipo") == artefacto["tipo"] and _normal(a.get("cumple")) == _normal(nombre)]
        if not suyos:
            del_tipo = [a for a in entregados if a.get("tipo") == artefacto["tipo"]]
            fallos.append("entrega.artefactos: falta el artefacto obligatorio `" + nombre + "` (tipo "
                          + artefacto["tipo"] + ") que exige el contrato operativo"
                          + (": hay " + str(len(del_tipo)) + " de ese tipo, pero ninguno declara "
                             "`cumple: " + nombre + "` (un artefacto no vale por varios)"
                             if del_tipo else ""))
            continue
        exigida = [str(x) for x in artefacto.get("estructura_minima") or []]
        if not exigida:
            continue
        declarados = {}
        for a in suyos:
            for e in a.get("estructura") or []:
                if isinstance(e, dict) and not _es_hueco(e.get("donde")):
                    declarados[_normal(e.get("apartado"))] = e.get("donde")
        faltan = [x for x in exigida if _normal(x) not in declarados]
        if faltan:
            fallos.append("entrega.artefactos: `" + nombre + "` no declara dónde está "
                          + str(len(faltan)) + " apartado(s) de su estructura mínima: "
                          + " · ".join("«" + x + "»" for x in faltan))
    return fallos


def _materia_escalable(entrega, corpus):
    capacidad = str(entrega.get("rol") or "").split("/", 1)[0]
    try:
        autoridad = (corpus.capacidad(capacidad) or {}).get("autoridad") or {}
    except (CorpusIlegible, CorpusIncompleto) as exc:
        return ["entrega.bloqueo.materia: no se pudo comprobar la autoridad de `"
                + capacidad + "`: " + str(exc)]
    escala = [str(x) for x in autoridad.get("escala") or []]
    decide = [str(x) for x in autoridad.get("decide_sola") or []]
    materia = str((entrega.get("bloqueo") or {}).get("materia") or "").strip()
    if not materia:
        return ["entrega.bloqueo.materia: escalar exige nombrar la materia, una de las que `"
                + capacidad + "` ESCALA según su ficha: " + " · ".join(escala)]
    if materia in decide:
        return ["entrega.bloqueo.materia: «" + materia + "» la decide sola `" + capacidad
                + "` (decide_sola): no se escala al Owner lo que el equipo resuelve (Directiva §20, §41, §76)"]
    if materia not in escala:
        return ["entrega.bloqueo.materia: «" + materia + "» no es una de las materias que `"
                + capacidad + "` escala según su ficha: " + " · ".join(escala)]
    return []


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
