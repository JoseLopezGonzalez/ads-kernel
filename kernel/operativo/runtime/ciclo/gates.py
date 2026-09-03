#!/usr/bin/env python3
"""gates — los GATES DE CAPA, con su censo DERIVADO del corpus. No se inventa ninguno.

Cada gate del sistema se aplica con las seis piezas que `§7.2` le exige tener:

    ENTRADA        qué se le presenta, con su procedencia
    EVIDENCIA      la que el propio bloque `ads:gate` declara en su campo `evidencia`
    REVISOR        quién juzga, y NO puede ser quien produjo lo que se juzga
    DICTAMEN       superado o no, comprobación a comprobación
    SALIDA         lo que el gate deja pasar cuando el dictamen es positivo
    FALLO CERRADO  el texto de `fallo` del propio gate, aplicado. No hay «pasa con reparos»

DECISIÓN · el censo se DERIVA del corpus y no se escribe
    Alternativas: (a) una lista de gates en este módulo; (b) leer todos los bloques
    `ads:gate` del corpus.
    Se elige (b). Con (a) habría dos sedes del censo y añadir un gate al corpus no lo
    haría aplicable, o peor: aplicar un gate que el corpus no declara. `§7.2` sólo aplica
    «los gates que EL MODELO define», y el modelo son los bloques. `test_ciclo.py`
    contrasta el censo derivado contra un barrido independiente del árbol.

DECISIÓN · un gate NO puede ser fuente normativa, y se impide por MECANISMO
    `§8.0` lo dice del lado de la composición —«no se inventa un handoff para tapar una
    capacidad sin vía, y no se ensancha un proceso por conveniencia: ensanchar `b.16` es
    normativo»—. Aquí se instancia con dos guardas:
      · `exigir_no_normativo` · lo ÚNICO que un dictamen puede escribir en el estado
        durable es su propio objeto, en el dominio `dictamenes`. Cualquier operación fuera
        de ese dominio levanta `GateNormativo`.
      · `exigir_no_amplia` · la ruta ANTES y DESPUÉS del gate tiene los mismos
        participantes y las mismas obligaciones. Un gate que añade una capacidad a la ruta
        ha ensanchado el proceso, y eso es normativo.
    Las dos tienen prueba propia, porque una prohibición sin mecanismo es una intención.

DECISIÓN · un gate no aprueba con reparos, y por eso no hay estado intermedio
    El dictamen es `superado` o `no-superado`. La alternativa —un tercer valor «superado
    con observaciones»— convierte el fallo cerrado en fallo abierto: quien recibe el
    dictamen decide si las observaciones importan, y esa decisión no la tiene nadie
    asignada. Las observaciones existen, y viajan en `hallazgos`, pero no cambian el
    dictamen.
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto

from .corpus import CAPACIDADES, Corpus
from .errores import GateDesconocido, GateFallido, GateNormativo

DOMINIO = "dictamenes"
ESQUEMA = "ads.estado/1"

SUPERADO = "superado"
NO_SUPERADO = "no-superado"
DICTAMENES = (SUPERADO, NO_SUPERADO)

# Quién puede ser REVISOR de un gate: una de las quince capacidades, o el Owner. Ninguna
# otra palabra vale, y un revisor «el sistema» o «automático» no es un revisor: `C5` dice
# que una devolución sin autor es una opinión, y un dictamen sin revisor, lo mismo.
REVISOR_OWNER = "OWNER"


def censo(corpus=None):
    """Todos los gates que el corpus declara, por su `id`. DERIVADO, no escrito."""
    return (corpus or Corpus()).gates()


def gate(identificador, *, corpus=None):
    catalogo = censo(corpus)
    if identificador not in catalogo:
        raise GateDesconocido(
            "`" + str(identificador) + "` no está en el censo de gates DERIVADO del "
            "corpus; declarados: " + ", ".join(sorted(catalogo)),
            gate=str(identificador),
        )
    return catalogo[identificador]


def comprobaciones_de(identificador, *, corpus=None):
    return tuple(c["id"] for c in gate(identificador, corpus=corpus)["comprobaciones"])


def aplicar(identificador, *, entrada, evidencia, revisor, corpus=None,
            comprobaciones_superadas=(), hallazgos=(), autor=None, salida=None):
    """Aplica un gate del censo y devuelve su DICTAMEN. Fallo CERRADO si no lo supera."""
    corpus = corpus or Corpus()
    declarado = gate(identificador, corpus=corpus)
    _exigir_revisor(revisor, autor=autor, gate=identificador)

    exigidas = [c["id"] for c in declarado["comprobaciones"]]
    superadas = {str(c) for c in comprobaciones_superadas}
    faltan = [c for c in exigidas if c not in superadas]
    sobran = sorted(superadas - set(exigidas))
    if sobran:
        raise GateNormativo(
            "se declaran superadas comprobaciones que `" + identificador + "` no tiene: "
            + ", ".join(sobran) + "; un gate no crece por conveniencia",
            gate=identificador, comprobaciones=sobran,
        )

    exigida_evidencia = [str(e) for e in (declarado.get("evidencia") or [])]
    aportada = [str(e) for e in (evidencia or [])]
    sin_evidencia = [e for e in exigida_evidencia if e not in aportada]

    dictamen = SUPERADO if not faltan and not sin_evidencia else NO_SUPERADO
    cuerpo = {
        "esquema": ESQUEMA,
        "gate": identificador,
        "aplica_a": str(declarado.get("aplica_a") or ""),
        "entrada": dict(entrada) if isinstance(entrada, dict) else {"descripcion": str(entrada)},
        "evidencia_exigida": exigida_evidencia,
        "evidencia_aportada": aportada,
        "revisor": str(revisor),
        "autor": str(autor) if autor else None,
        "comprobaciones_exigidas": exigidas,
        "comprobaciones_superadas": sorted(superadas),
        "comprobaciones_pendientes": faltan,
        "evidencia_ausente": sin_evidencia,
        "dictamen": dictamen,
        "salida": (str(salida) if salida else None) if dictamen == SUPERADO else None,
        "fallo_declarado": str(declarado.get("fallo") or "").strip(),
        "hallazgos": [str(h) for h in hallazgos],
        "normativo": False,
    }
    cuerpo["id"] = _identificador(cuerpo)
    if dictamen == NO_SUPERADO:
        error = GateFallido(
            "`" + identificador + "` NO se supera; pendientes: "
            + (", ".join(faltan) or "(ninguna)") + "; evidencia ausente: "
            + (", ".join(sin_evidencia) or "(ninguna)") + ". " + cuerpo["fallo_declarado"],
            gate=identificador,
            pendientes=faltan,
            evidencia_ausente=sin_evidencia,
        )
        # El dictamen NEGATIVO también es un dictamen y también es evidencia: viaja con el
        # error para que quien lo capture pueda escribirlo, en vez de tener que reconstruir
        # por qué falló a partir de un texto.
        error.dictamen = cuerpo
        raise error
    return cuerpo


def _exigir_revisor(revisor, *, autor, gate):
    if not isinstance(revisor, str) or not revisor.strip():
        raise GateFallido(
            "el gate `" + str(gate) + "` se aplica sin revisor; un dictamen sin quien lo "
            "firme no detiene nada",
            gate=str(gate),
        )
    limpio = revisor.strip()
    if limpio != REVISOR_OWNER and limpio not in CAPACIDADES:
        raise GateFallido(
            "el revisor de `" + str(gate) + "` es una de las quince capacidades o el "
            "Owner; se recibió " + repr(revisor),
            gate=str(gate), revisor=limpio,
        )
    if autor and str(autor).strip() == limpio:
        raise GateFallido(
            "`" + limpio + "` produjo lo que se juzga y no puede revisarlo: la revisión "
            "independiente de quien construyó es criterio de satisfacción escrito en `b.16`",
            gate=str(gate), revisor=limpio,
        )
    return limpio


# ===========================================================================
#  ningún gate es fuente normativa
# ===========================================================================
def exigir_no_normativo(operaciones):
    """Lo único que un dictamen escribe es su propio objeto, en el dominio `dictamenes`."""
    for operacion in operaciones:
        ruta = getattr(operacion, "ruta", None)
        if not isinstance(ruta, str) or "/" not in ruta:
            raise GateNormativo(
                "una operación de un gate sin ruta lógica no es interpretable",
            )
        dominio = ruta.split("/", 1)[0]
        if dominio != DOMINIO:
            raise GateNormativo(
                "un gate intentó escribir en `" + dominio + "`; lo ÚNICO que un dictamen "
                "escribe es su propio objeto en `" + DOMINIO + "`. Un gate que escribe "
                "norma deja de ser un control y pasa a ser una fuente",
                ruta=ruta, dominio=dominio,
            )
    return True


def exigir_no_amplia(ruta_antes, ruta_despues):
    """La ruta no cambia al pasar por un gate. Ensancharla es ensanchar el proceso."""
    antes = _huella_de_ruta(ruta_antes)
    despues = _huella_de_ruta(ruta_despues)
    if antes != despues:
        anadidas = sorted(set(despues["participantes"]) - set(antes["participantes"]))
        retiradas = sorted(set(antes["participantes"]) - set(despues["participantes"]))
        raise GateNormativo(
            "la ruta cambió al pasar por el gate; añadidas: "
            + (", ".join(anadidas) or "(ninguna)") + "; retiradas: "
            + (", ".join(retiradas) or "(ninguna)") + ". Ensanchar `b.16` es normativo, y "
            "su sitio es una presión, no un gate",
            anadidas=anadidas, retiradas=retiradas,
        )
    return True


def _huella_de_ruta(ruta):
    return {
        "proceso": ruta["proceso"],
        "propietario_global": ruta["propietario_global"],
        "participantes": sorted(
            p["capacidad"] + "@" + str(p["via"]) for p in ruta["participantes"]
        ),
        "obligaciones": sorted(o["id"] for o in ruta["obligaciones"]),
    }


def _identificador(cuerpo):
    sin_id = {clave: valor for clave, valor in cuerpo.items() if clave != "id"}
    digest = cid_de_objeto(sin_id)
    return "dic-" + digest.split(":", 1)[-1][:16]


def ruta_de(identificador_de_dictamen):
    return DOMINIO + "/" + identificador_de_dictamen + ".json"
