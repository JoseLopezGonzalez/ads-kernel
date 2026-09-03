#!/usr/bin/env python3
"""handoffs — `C5` aplicado sobre las instancias declaradas, con ACUSE, RECHAZO y REANUDACIÓN.

`C5` define la FORMA; las instancias viven en `kernel/operativo/circuitos/`. Este módulo no
inventa ninguna: las lee, comprueba que traen los ONCE campos que
`esquemas/handoff.yaml` declara obligatorios, y ejecuta la entrega como un objeto DURABLE.

    «QUIEN RECIBE COMPRUEBA ANTES DE TOMAR CUSTODIA. Si rechaza, el paquete NO cambia de
     custodia: sigue en el emisor, con el motivo escrito. Eso NO cuenta como devolución a
     efectos del freno de `a.7`, porque la capa nunca se depositó.»            `C5`

Esa frase es el eje del módulo, y la razón de que RECHAZO y DEVOLUCIÓN sean dos operaciones
distintas con dos efectos distintos sobre la custodia y sobre el contador del freno.

DECISIÓN · RECHAZO y DEVOLUCIÓN no comparten camino, ni siquiera parcialmente
    Alternativas: (a) una operación `devolver` con una bandera `antes_de_aceptar`; (b) dos
    operaciones.
    Se elige (b). Con (a) el contador del freno de `a.7` depende de un booleano que alguien
    puede pasar mal, y el defecto que `C5` describe —«un equipo acepta trabajo malo por
    cortesía y luego lo devuelve, gastando una de las dos devoluciones»— reaparece por la
    puerta de atrás. Con (b), `rechazar` sólo es válido mientras el estado es `emitido`, y
    `devolver` sólo lo es después del acuse: la máquina impide la confusión en vez de
    confiar en el llamador.

DECISIÓN · una DEVOLUCIÓN sin los CUATRO campos NO es una devolución
    `C5` es literal: «Una devolución sin los cuatro campos se rechaza COMO devolución y el
    paquete vuelve al receptor: no cuenta para el freno, porque no era una devolución». Se
    instancia con `DevolucionSinEvidencia`, y el paquete NO cambia de custodia.

DECISIÓN · las CINCO entregas que `§8.0` declara y `circuitos/` no tiene viven aquí, como DATO
    `§8.0` las escribe una a una —`SIS`→`PLT`, `SIS`→`CON`, `SIS`→`VER`, `CON`→`ENT`,
    `ENT`→`VER`— y dice que «las instancias las crea `F6`» en `kernel/operativo/circuitos/`.
    Ese directorio es NORMA y no está en la zona de escritura de este corte, así que se
    materializan aquí en `ENTREGAS_DECLARADAS_EN_8_0`, con sus ONCE campos, validadas
    contra el MISMO esquema que las diecisiete de `circuitos/` y ejecutables por el mismo
    camino. Queda una PETICIÓN DE INTEGRACIÓN para trasladarlas a su sede: el día que estén
    allí, `Catalogo` las leerá del corpus y esta constante se retira sin tocar nada más,
    porque `catalogo()` funde las dos fuentes por `id` y la del corpus MANDA.

DECISIÓN · el catálogo funde, y ante colisión MANDA el corpus
    Si mañana `circuitos/` declara `handoff:sis-a-plt`, la instancia del corpus sustituye a
    la de aquí sin aviso y sin conflicto. La alternativa —fallar por duplicado— convertiría
    la integración de la petición en una rotura, que es la forma de que nunca se integre.
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto

from .corpus import CAPACIDADES, Corpus
from .errores import (
    DevolucionSinEvidencia,
    HandoffDesconocido,
    HandoffIncompleto,
    HandoffRechazado,
)

DOMINIO = "handoffs"
ESQUEMA = "ads.estado/1"

EMITIDO = "emitido"
ACUSADO = "acusado"
RECHAZADO = "rechazado"
DEVUELTO = "devuelto"
ESTADOS = (EMITIDO, ACUSADO, RECHAZADO, DEVUELTO)

# Los CUATRO campos que `C5` exige a toda devolución, sin excepción.
CAMPOS_DE_DEVOLUCION = ("que_falta", "por_que_es_insuficiente", "que_la_cerraria", "evidencia")


# ===========================================================================
#  las CINCO entregas que `§8.0` declara y `circuitos/` todavía no tiene
# ===========================================================================
ENTREGAS_DECLARADAS_EN_8_0 = {
    "handoff:sis-a-plt": {
        "id": "handoff:sis-a-plt",
        "de": "SIS",
        "a": "PLT",
        "cuando": "el alcance del paquete declara fuentes que no están materializadas en "
                  "el workspace y `C7:82` atribuye la materialización a PLT",
        "entrega": [
            "la SOLICITUD DE MATERIALIZACIÓN de las fuentes del alcance, por su `id` de "
            "SOURCES.toml y su `path` declarado",
            "la revisión exacta que el paquete necesita de cada fuente, `<source-id>@<sha>`",
        ],
        "comprueba_al_recibir": [
            "cada fuente solicitada está declarada en SOURCES.toml con `id` y `path`",
            "ninguna ruta de destino escapa del workspace ni cae dentro del control repo",
            "la solicitud NO incluye rama, commit, push ni PR: eso es de la capacidad con "
            "custodia y no de PLT (`C7:83`-`C7:86`)",
        ],
        "rechaza_si": [
            "la solicitud pide a PLT una operación que `C7` no le atribuye",
            "el destino está ocupado por otro repositorio o el remoto no corresponde",
        ],
        "devolucion": "PLT devuelve a SIS cuando la solicitud nombra una fuente que el "
                      "manifiesto no declara, o pide una operación fuera de `C7:82`. El "
                      "paquete queda esperando-dependencia y NO se despacha.",
        "evidencia_de_devolucion": [
            "el `id` de la fuente que el manifiesto no declara, o la operación pedida y la "
            "fila de `C7` que la atribuye a otro",
        ],
        "owner": "ninguna: materializar una fuente declarada no es materia del Owner.",
        "checkpoint": "SIS lee de PLT: qué fuentes quedaron materializadas y en qué "
                      "revisión, para no volver a pedirlas.",
    },
    "handoff:sis-a-con": {
        "id": "handoff:sis-a-con",
        "de": "SIS",
        "a": "CON",
        "cuando": "un paquete declara `escribe_fuentes` y la obligación `cambio-construido` "
                  "del proceso está sin satisfacer",
        "entrega": [
            "el SOURCE CHANGE: el paquete con su `lee_fuentes` y su `escribe_fuentes`",
            "la custodia de rama, commit, push, PR y CI POR FUENTE bajo `C7:83`-`C7:86`",
            "la capa de SIS que declara qué cambia en la fábrica y por qué",
        ],
        "comprueba_al_recibir": [
            "cada fuente de escritura está justificada por el objetivo del paquete",
            "las fuentes del alcance están materializadas: `gate:workspace-conforme` pasa",
            "la capa de SIS enlaza el problema real que justifica el cambio",
        ],
        "rechaza_si": [
            "hay una fuente en `escribe_fuentes` que el objetivo del paquete no justifica",
            "el paquete no declara `lee_fuentes` ni `escribe_fuentes` y toca código",
        ],
        "devolucion": "CON devuelve a SIS cuando lo declarado por SIS no se puede construir "
                      "sin ampliar el alcance. La devolución cuenta para el freno de `a.7` "
                      "sólo si CON ya había tomado custodia.",
        "evidencia_de_devolucion": [
            "qué parte de la capa de SIS no es construible y qué alcance haría falta",
        ],
        "owner": "la autorización de retirada POR FUENTE, cuando el cambio retira algo "
                 "heredado (`A8`, `M6`).",
        "checkpoint": "CON lee de SIS: la justificación de producto enlazada y las "
                      "decisiones del Owner captadas, para no volver a preguntarlas.",
    },
    "handoff:sis-a-ver": {
        "id": "handoff:sis-a-ver",
        "de": "SIS",
        "a": "VER",
        "cuando": "el cambio de la fábrica está construido y hay que proponer un nivel de "
                  "certificación con su evidencia",
        "entrega": [
            "el dosier de certificación: las celdas de cobertura del sujeto",
            "la evidencia ejecutada, con el estado real de cada prueba",
            "el nivel PROPUESTO, que VER verifica y no decide",
        ],
        "comprueba_al_recibir": [
            "cada celda propuesta trae la evidencia que la sostiene, ejecutada",
            "ninguna prueba se declara superada sin haberse ejecutado",
            "el sujeto de la certificación trae sus identificadores resueltos",
        ],
        "rechaza_si": [
            "hay una celda propuesta sin evidencia enlazada",
            "el nivel propuesto presupone otro nivel que no está verificado y vigente",
        ],
        "devolucion": "VER devuelve a SIS con la celda concreta cuya evidencia falta o no "
                      "sostiene lo que afirma. VER verifica y NO certifica.",
        "evidencia_de_devolucion": [
            "la celda concreta, qué evidencia falta y qué comprobación la cerraría",
        ],
        "owner": "ninguna: verificar no es aprobar, y el nivel lo emite SIS.",
        "checkpoint": "VER lee de SIS: el sujeto con sus identificadores y la huella de la "
                      "evidencia, para poder contrastar sin reproducirla entera.",
    },
    "handoff:con-a-ent": {
        "id": "handoff:con-a-ent",
        "de": "CON",
        "a": "ENT",
        "cuando": "el cambio está construido en una o varias fuentes y hay que declarar "
                  "convergencia (`C7:88`-`C7:89`)",
        "entrega": [
            "el RESULTADO POR FUENTE: qué quedó construido en cada `<source-id>@<sha>`",
            "el estado de CI por fuente, que verifica push y PR",
        ],
        "comprueba_al_recibir": [
            "cada fuente del alcance trae su resultado, sin huecos",
            "CI está en verde en cada fuente, o consta por qué no aplica",
            "ninguna fuente quedó con trabajo a medias sin declararlo",
        ],
        "rechaza_si": [
            "falta el resultado de alguna fuente del alcance",
            "hay una fuente con CI en rojo y sin motivo escrito",
        ],
        "devolucion": "ENT devuelve a CON nombrando la fuente sin resultado o con CI en "
                      "rojo. Mientras no converjan todas, ENT sostiene el estado "
                      "INTEGRACIÓN PARCIAL, que no es un fallo: es un estado declarado.",
        "evidencia_de_devolucion": [
            "el `id` de la fuente, su revisión y la salida de CI que lo sostiene",
        ],
        "owner": "materia reservada en el merge, el release y el rollback irreversible, "
                 "donde `C7` la exige.",
        "checkpoint": "ENT lee de CON: la revisión exacta de cada fuente, nunca una copia "
                      "de su contenido (`C5`).",
    },
    "handoff:ent-a-ver": {
        "id": "handoff:ent-a-ver",
        "de": "ENT",
        "a": "VER",
        "cuando": "ENT ha declarado la convergencia y ha emitido el Integration Set",
        "entrega": [
            "la convergencia declarada, con su Integration Set",
            "la revisión de cada fuente que entra en el conjunto",
        ],
        "comprueba_al_recibir": [
            "el Integration Set nombra todas las fuentes del alcance y ninguna más",
            "cada fuente entra por una revisión exacta y no por una rama",
            "`gate:convergencia-de-fuentes` consta superado",
        ],
        "rechaza_si": [
            "el Integration Set deja fuera una fuente del alcance",
            "alguna fuente entra por una referencia móvil en vez de por su revisión",
        ],
        "devolucion": "VER devuelve a ENT cuando el conjunto no es verificable: falta una "
                      "fuente, o una entra por una referencia que puede moverse.",
        "evidencia_de_devolucion": [
            "el conjunto recibido y la fuente que falta o la referencia móvil concreta",
        ],
        "owner": "el release, donde `C7` reserva la decisión al Owner.",
        "checkpoint": "VER lee de ENT: el Integration Set con sus revisiones, para poder "
                      "reproducir el conjunto sin hablar con ENT.",
    },
}


# ===========================================================================
#  catálogo
# ===========================================================================
def catalogo(corpus=None):
    """Las instancias de `circuitos/` MÁS las cinco de `§8.0`. Ante colisión, manda el corpus."""
    corpus = corpus or Corpus()
    salida = dict(ENTREGAS_DECLARADAS_EN_8_0)
    salida.update(corpus.handoffs())
    obligatorios = corpus.obligatorios_de("handoff")
    for identificador, datos in sorted(salida.items()):
        faltan = [campo for campo in obligatorios if campo not in datos]
        if faltan:
            raise HandoffIncompleto(
                "la instancia `" + identificador + "` no declara " + ", ".join(faltan)
                + "; `esquemas/handoff.yaml` exige los once campos",
                handoff=identificador, faltan=faltan,
            )
        for extremo in ("de", "a"):
            if datos[extremo] not in CAPACIDADES:
                raise HandoffIncompleto(
                    "la instancia `" + identificador + "` declara `" + extremo + ": "
                    + str(datos[extremo]) + "`, que no es una de las quince capacidades",
                    handoff=identificador,
                )
    return salida


def instancia(identificador, *, corpus=None):
    catalogado = catalogo(corpus)
    if identificador not in catalogado:
        raise HandoffDesconocido(
            "`" + str(identificador) + "` no está declarado ni en `circuitos/` ni entre las "
            "cinco entregas de `§8.0`; declarados: " + ", ".join(sorted(catalogado)),
            handoff=str(identificador),
        )
    return catalogado[identificador]


# ===========================================================================
#  la entrega, como objeto DURABLE
# ===========================================================================
def emitir(identificador, *, artefactos, checkpoint, trazabilidad, corpus=None):
    """El productor entrega. La custodia NO cambia todavía: cambia con el ACUSE."""
    declarada = instancia(identificador, corpus=corpus)
    if not artefactos:
        raise HandoffIncompleto(
            "un handoff sin artefactos concretos no es una entrega: `C5` dice «artefactos "
            "concretos, localizables, no “el trabajo hecho”»",
            handoff=identificador,
        )
    for clave in ("item", "paquete", "ruta"):
        if not str((trazabilidad or {}).get(clave) or "").strip():
            raise HandoffIncompleto(
                "la entrega no declara `" + clave + "` en su trazabilidad; sin ella el "
                "receptor no puede reanudar sin hablar con el emisor",
                handoff=identificador,
            )
    cuerpo = {
        "esquema": ESQUEMA,
        "instancia": identificador,
        "de": declarada["de"],
        "a": declarada["a"],
        "cuando": str(declarada["cuando"]),
        "artefactos": sorted(str(a) for a in artefactos),
        "comprueba_al_recibir": [str(c) for c in declarada["comprueba_al_recibir"]],
        "rechaza_si": [str(c) for c in declarada["rechaza_si"]],
        "owner": str(declarada["owner"]),
        "checkpoint": str(checkpoint),
        "checkpoint_exigido": str(declarada["checkpoint"]),
        "trazabilidad": {
            "item": str(trazabilidad["item"]),
            "paquete": str(trazabilidad["paquete"]),
            "ruta": str(trazabilidad["ruta"]),
            "encuadre": str(trazabilidad.get("encuadre") or ""),
        },
        "estado": EMITIDO,
        "custodia": declarada["de"],
        "acuse": None,
        "rechazo": None,
        "devolucion": None,
        "cuenta_para_el_freno": False,
    }
    cuerpo["id"] = _identificador(cuerpo)
    return cuerpo


def acusar(entrega, *, comprobaciones_superadas, receptor):
    """El receptor comprobó ANTES de tomar custodia y ACEPTA. La custodia cambia aquí."""
    _exigir_estado(entrega, EMITIDO, "acusar")
    if receptor != entrega["a"]:
        raise HandoffRechazado(
            "quien acusa no es el receptor declarado: la entrega va a `" + entrega["a"]
            + "` y acusa `" + str(receptor) + "`",
            handoff=entrega["instancia"],
        )
    superadas = {str(c) for c in comprobaciones_superadas}
    faltan = [c for c in entrega["comprueba_al_recibir"] if c not in superadas]
    if faltan:
        raise HandoffRechazado(
            "quedan comprobaciones sin superar y `C5` las exige ANTES de tomar custodia: "
            + "; ".join(faltan),
            handoff=entrega["instancia"], pendientes=faltan,
        )
    nueva = dict(entrega)
    nueva["estado"] = ACUSADO
    nueva["custodia"] = entrega["a"]
    nueva["acuse"] = {
        "receptor": str(receptor),
        "comprobaciones_superadas": sorted(superadas),
    }
    nueva["id"] = _identificador(nueva)
    return nueva


def rechazar(entrega, *, receptor, motivo):
    """El receptor rechaza ANTES de tomar custodia. NO cuenta para el freno de `a.7`."""
    _exigir_estado(entrega, EMITIDO, "rechazar")
    if not str(motivo or "").strip():
        raise HandoffRechazado(
            "un rechazo sin motivo escrito no es un rechazo: `C5` exige condiciones "
            "escritas, no impresión de calidad",
            handoff=entrega["instancia"],
        )
    nueva = dict(entrega)
    nueva["estado"] = RECHAZADO
    nueva["custodia"] = entrega["de"]          # NO cambia de custodia: sigue en el emisor
    nueva["rechazo"] = {"receptor": str(receptor), "motivo": str(motivo)}
    nueva["cuenta_para_el_freno"] = False
    nueva["id"] = _identificador(nueva)
    return nueva


def devolver(entrega, *, devolucion):
    """DESPUÉS del acuse. Con los CUATRO campos; sin ellos no es una devolución."""
    _exigir_estado(entrega, ACUSADO, "devolver")
    faltan = [
        campo for campo in CAMPOS_DE_DEVOLUCION
        if not str((devolucion or {}).get(campo) or "").strip()
        and not (isinstance((devolucion or {}).get(campo), list)
                 and (devolucion or {}).get(campo))
    ]
    if faltan:
        raise DevolucionSinEvidencia(
            "la devolución no trae " + ", ".join(faltan) + "; `C5`: una devolución sin los "
            "cuatro campos se rechaza COMO devolución, no cuenta para el freno, y el "
            "paquete vuelve al receptor",
            handoff=entrega["instancia"], faltan=faltan,
        )
    nueva = dict(entrega)
    nueva["estado"] = DEVUELTO
    nueva["custodia"] = entrega["de"]
    nueva["devolucion"] = {campo: devolucion[campo] for campo in CAMPOS_DE_DEVOLUCION}
    # Aceptó y DESPUÉS descubrió que la capa anterior es insuficiente: `C5` dice que esto
    # SÍ es devolución y SÍ cuenta para el freno de dos.
    nueva["cuenta_para_el_freno"] = True
    nueva["id"] = _identificador(nueva)
    return nueva


def reanudacion(entrega):
    """Lo que el receptor necesita para retomar SIN hablar con el emisor (`C5`)."""
    return {
        "instancia": entrega["instancia"],
        "custodia": entrega["custodia"],
        "estado": entrega["estado"],
        "artefactos": list(entrega["artefactos"]),
        "checkpoint": entrega["checkpoint"],
        "checkpoint_exigido": entrega["checkpoint_exigido"],
        "trazabilidad": dict(entrega["trazabilidad"]),
        "siguiente_accion": _siguiente(entrega),
    }


def _siguiente(entrega):
    if entrega["estado"] == EMITIDO:
        return "el receptor `" + entrega["a"] + "` comprueba y acusa o rechaza"
    if entrega["estado"] == ACUSADO:
        return "el receptor `" + entrega["a"] + "` trabaja desde su checkpoint"
    if entrega["estado"] == RECHAZADO:
        return "el emisor `" + entrega["de"] + "` corrige: la custodia nunca cambió"
    return "el emisor `" + entrega["de"] + "` atiende la devolución con sus cuatro campos"


def _exigir_estado(entrega, esperado, operacion):
    if entrega.get("estado") != esperado:
        raise HandoffRechazado(
            "`" + operacion + "` exige el estado `" + esperado + "` y la entrega está en `"
            + str(entrega.get("estado")) + "`",
            handoff=str(entrega.get("instancia")), estado=str(entrega.get("estado")),
        )
    return entrega


def _identificador(cuerpo):
    sin_id = {clave: valor for clave, valor in cuerpo.items() if clave != "id"}
    digest = cid_de_objeto(sin_id)
    return "ho-" + digest.split(":", 1)[-1][:16]


def ruta_de(identificador_de_entrega):
    return DOMINIO + "/" + identificador_de_entrega + ".json"
