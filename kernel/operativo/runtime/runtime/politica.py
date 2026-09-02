#!/usr/bin/env python3
"""politica — reintentos, y las CUATRO clases de fallo que el §4.2 exige distinguir.

No hay estado aquí: hay funciones puras sobre el paquete leído y sobre lo que el adaptador
devolvió. Todo lo que decidan se escribe después como `Transicion` sobre el `Almacen`.

LAS CUATRO CLASES, y por qué no son la misma cosa con distinto texto:

    REINTENTABLE          la operación puede volver a intentarse tal cual. Consume un
                          intento y el paquete vuelve a `listo` si quedan.
    DEFINITIVO            volver a intentarlo daría el mismo resultado. NO se reintenta:
                          `agotado` y registro de reconciliación, aunque queden intentos.
    CANCELACIÓN           la autoridad retiró el trabajo mientras corría. El paquete es
                          `cancelado`, que es TERMINAL: no hay reintento y no hay
                          pendencia que reconciliar, porque nada quedó a medias sin
                          decisión.
    PÉRDIDA DE AUTORIDAD  el lease cambió de titular o de época. NO se escribe NADA: quien
                          escribiera pisaría al titular vigente. Se levanta
                          `AutoridadPerdida` y se sale. Esta clase no aparece en
                          `clasificar` porque no la produce el adaptador: la produce la
                          relectura del lease, y por eso vive en `lease.exigir_titularidad`.

DECISIÓN · el tope por defecto es TRES, y viene de `a.9`
    §7.3 de `11-ARQ`: «REINTENTO sólo para operaciones idempotentes, y con tope. Un
    reintento sin tope es un livelock, y a.9 ya fijó el precedente: tres». No se inventa
    otro número y no se hace configurable por variable de entorno: es `max_intentos` del
    paquete, que es un dato durable y auditable.

DECISIÓN · el `timeout` del adaptador cuenta como REINTENTABLE
    Alternativas: (a) clase propia con tratamiento propio; (b) reintentable; (c)
    definitivo.
    Se elige (b), y `TiempoAgotado` sigue siendo su error tipado propio para que la
    evidencia distinga la causa. Un límite excedido describe casi siempre una condición del
    entorno —máquina cargada, red lenta—, no una orden imposible, y (c) convertiría un pico
    de carga en una pendencia de reconciliación permanente. Lo que impide el livelock no es
    negar el reintento, es el tope de `a.9`, que también se le aplica.

DECISIÓN · agotar NO toca más el estado canónico que el propio paso a `agotado`
    `g.6` y `g.9` lo dicen sin ambigüedad. El paquete pasa a `agotado` —eso es un cambio
    de estado, y es el que hace que deje de ser elegible— y a partir de ahí el runtime NO
    escribe nada más sobre él: la salida la decide la AUTORIDAD por la única vía que `g.9`
    admite, `resolver_reconciliacion`, y sólo entonces `agotado` → `listo`.
"""
from __future__ import annotations

from .errores import (
    EjecucionCancelada,
    EjecucionDefinitiva,
    EjecucionFallida,
    RuntimeInconsistente,
    TiempoAgotado,
)

MAX_INTENTOS_POR_DEFECTO = 3

CLASE_COMPLETADO = "completado"
CLASE_REINTENTABLE = "reintentable"
CLASE_DEFINITIVO = "definitivo"
CLASE_CANCELACION = "cancelacion"

CLASES = (CLASE_COMPLETADO, CLASE_REINTENTABLE, CLASE_DEFINITIVO, CLASE_CANCELACION)

# Lo que el §4.4 fija que devuelve `Adaptador.ejecutar`.
CLAVES_DE_RESULTADO = ("estado", "codigo", "salida", "detalle", "reintentable", "efecto",
                       "repetido")
ESTADOS_DE_RESULTADO = ("completado", "fallido", "cancelado", "timeout")

# Decisiones que `decidir` puede devolver, y ninguna otra palabra vale.
DECISION_CERRAR = "cerrar"
DECISION_REINTENTAR = "reintentar"
DECISION_AGOTAR = "agotar"


def comprobar_resultado(resultado, *, efecto, paquete):
    """El resultado del adaptador, validado por FORMA antes de que decida nada.

    Un adaptador que devuelve un `estado` fuera de los cuatro del §4.4 no es «un adaptador
    con un bug menor»: es una respuesta que ninguna regla sabe clasificar, y clasificarla
    de todos modos sería inventar estado.
    """
    if not isinstance(resultado, dict):
        raise RuntimeInconsistente(
            "el adaptador devolvió " + type(resultado).__name__ + " y el §4.4 fija un mapa",
            ruta=paquete,
        )
    faltan = [clave for clave in CLAVES_DE_RESULTADO if clave not in resultado]
    if faltan:
        raise RuntimeInconsistente(
            "el resultado del adaptador no declara " + ", ".join(faltan), ruta=paquete,
        )
    if resultado["estado"] not in ESTADOS_DE_RESULTADO:
        raise RuntimeInconsistente(
            "`estado` del resultado fuera del §4.4: " + repr(resultado["estado"])
            + "; válidos: " + ", ".join(ESTADOS_DE_RESULTADO),
            ruta=paquete,
        )
    if resultado["efecto"] != efecto:
        raise RuntimeInconsistente(
            "el adaptador acusa un efecto distinto del pedido: pedido `" + efecto
            + "`, devuelto `" + str(resultado["efecto"]) + "`",
            ruta=paquete, pedido=efecto, devuelto=str(resultado["efecto"]),
        )
    if not isinstance(resultado["reintentable"], bool):
        raise RuntimeInconsistente("`reintentable` es booleano", ruta=paquete)
    if not isinstance(resultado["repetido"], bool):
        raise RuntimeInconsistente("`repetido` es booleano", ruta=paquete)
    return resultado


def clasificar(resultado):
    """Devuelve `(clase, error)` — el error es `None` cuando la ejecución fue bien.

    El error se CONSTRUYE aquí y no se levanta: quien despacha necesita escribir el
    resultado durable ANTES de propagarlo, y levantar aquí obligaría a capturarlo allí.
    """
    estado = resultado["estado"]
    detalle = str(resultado.get("detalle") or "")
    if estado == "completado":
        return CLASE_COMPLETADO, None
    if estado == "cancelado":
        return CLASE_CANCELACION, EjecucionCancelada(
            "el adaptador declara la ejecución cancelada" + (": " + detalle if detalle else ""),
        )
    if estado == "timeout":
        return CLASE_REINTENTABLE, TiempoAgotado(
            "el adaptador excedió su `limite_segundos`"
            + (": " + detalle if detalle else ""),
        )
    if resultado["reintentable"]:
        return CLASE_REINTENTABLE, EjecucionFallida(
            "fallo reintentable del adaptador" + (": " + detalle if detalle else ""),
            codigo_del_adaptador=resultado.get("codigo"),
        )
    return CLASE_DEFINITIVO, EjecucionDefinitiva(
        "fallo NO reintentable del adaptador" + (": " + detalle if detalle else ""),
        codigo_del_adaptador=resultado.get("codigo"),
    )


def estado_de_paquete(clase):
    """El estado del vocabulario cerrado al que lleva cada clase, recién ejecutado."""
    if clase == CLASE_COMPLETADO:
        return "completado"
    if clase == CLASE_CANCELACION:
        return "cancelado"
    if clase in (CLASE_REINTENTABLE, CLASE_DEFINITIVO):
        return "fallido"
    raise RuntimeInconsistente("clase de fallo desconocida: " + repr(clase))


def quedan_intentos(paquete):
    return int(paquete["intentos"]) < int(paquete["max_intentos"])


def decidir(clase, paquete):
    """Qué hacer con un paquete que acaba de quedar en `fallido` (o terminal).

    `cerrar` · nada más que hacer: el paquete ya está en su estado final.
    `reintentar` · `fallido` → `listo`, porque el fallo es REINTENTABLE y quedan intentos.
    `agotar` · `fallido` → `agotado` y registro de reconciliación de `g.9`.
    """
    if clase in (CLASE_COMPLETADO, CLASE_CANCELACION):
        return DECISION_CERRAR
    if clase == CLASE_DEFINITIVO:
        # Sólo se reintenta el fallo REINTENTABLE (§4.2). Quedar intentos no cambia nada:
        # repetir una operación que ya se sabe imposible es gastar el tope por nada.
        return DECISION_AGOTAR
    if clase == CLASE_REINTENTABLE:
        return DECISION_REINTENTAR if quedan_intentos(paquete) else DECISION_AGOTAR
    raise RuntimeInconsistente("clase de fallo desconocida: " + repr(clase))


def causa_de_reconciliacion(clase, error, paquete):
    """El texto de `causa` que va al registro auxiliar de `g.9`. Determinista y sin rutas."""
    codigo = error.codigo if error is not None else "SIN_ERROR"
    return (codigo + ": " + clase + " tras " + str(paquete["intentos"]) + " de "
            + str(paquete["max_intentos"]) + " intento(s)")
