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

Y una QUINTA, que la auditoría independiente obligó a nombrar:

    AMBIGUO               no se sabe si el efecto se aplicó. El adaptador encontró un recibo
                          de INTENCIÓN abierto y sin cerrar: empezó, y no consta que
                          terminara. NO es completado, NO es reintentable y NO es
                          cancelación. El paquete queda `agotado` y se abre el registro de
                          `g.9` nombrando la ambigüedad.

DECISIÓN · con un proceso externo cualquiera no se puede prometer «exactamente una vez»
    Entre lanzar el trabajo y anotar que se lanzó hay siempre una ventana; un corte dentro
    de ella deja un estado que desde fuera no se puede leer. Alternativas ante esa ventana:
    (a) reintentar, y arriesgarse a aplicar el efecto dos veces; (b) darlo por completado, y
    arriesgarse a dar por hecho algo que no ocurrió; (c) DETECTARLA y escalarla.
    Se elige (c). (a) y (b) son decisiones de negocio disfrazadas de detalle técnico, y las
    dos las toma el runtime a espaldas de quien responde del trabajo. Lo que sí se puede
    garantizar —y es lo que se garantiza— es que la ambigüedad **se detecte en vez de
    duplicarse en silencio**, y que la salga quien tiene autoridad para decidirla.

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
    EjecucionAmbigua,
    EjecucionCancelada,
    EjecucionDefinitiva,
    EjecucionFallida,
    RuntimeInconsistente,
    TiempoAgotado,
)

MAX_INTENTOS_POR_DEFECTO = 3

# ===========================================================================
#  `b.12` paso 5 · el ORDEN de selección, y por qué está aquí
# ===========================================================================
# DECISIÓN · el orden de `b.12` es POLÍTICA, y se escribe como función PURA
#     Estaba dentro de `Dispatcher.elegibles` como un `sort(key=...)` de una línea, y por eso
#     nadie podía probarlo sin montar un almacén: para comprobar que el criterio (b) importa
#     había que fabricar un grafo durable entero. Sacarlo aquí lo hace lo que ya son las
#     cuatro clases de fallo de este módulo —una función pura sobre objetos ya leídos— y
#     permite sabotear UN criterio y ver qué prueba se pone roja. El dispatcher sigue siendo
#     el único que escribe.
#
# DECISIÓN · el orden es TOTAL, y su último criterio es el identificador
#     `gate:despacho-coherente` exige «mismo estado produce misma selección, con desempate
#     por identificador». Los tres primeros criterios pueden empatar; el cuarto no empata
#     nunca, porque dos paquetes no comparten identificador. Sin él, dos instancias podrían
#     ver la misma cola en orden distinto y competir por paquetes distintos creyendo cada una
#     que va la primera.

CRITERIOS_DE_ORDEN = (
    ("prioridad", "prioridad declarada"),
    ("grado_de_salida", "desbloquea a más paquetes (grado de salida en el grafo)"),
    ("tiempo_listo", "antigüedad de espera"),
    ("paquete", "id del paquete"),
)


def clave_de_orden(entrada):
    """Los CUATRO criterios de `b.12` paso 5, en el orden en que el contrato los escribe.

    Los tres primeros van NEGADOS porque los tres se ordenan de mayor a menor: más prioridad,
    más paquetes desbloqueados, más tiempo esperando. El cuarto, ascendente, es el desempate
    determinista. Quitar cualquiera de los cuatro cambia el orden de una cola real, y en
    `test_cardinalidad_y_seleccion.py` cada uno tiene su prueba y su sabotaje.

    Y `prioridad` entra aquí como DATO LEÍDO y nunca como dato escrito. `b.12` es terminante:

        «DSP informa de la inanición. No cambia la prioridad. Nunca»

    La prevención de la inanición es el criterio (c) —la antigüedad adelanta entre IGUALES en
    prioridad— y no una corrección del valor. `G-04` del cierre de `F6` encontró que esta
    sede decía tener la cita y no la tenía —la tenían `ciclo/planificacion.py` y
    `runtime/vistas.py`, y el gate dio por citadas las tres—, de modo que la prohibición se
    apoyaba en una sede menos de las que se creía. Se escribe LITERAL, y `T419` confronta las
    cuatro sedes entre sí: las tres que la citan y `estado_util.CITA_DE_B12`, que es la que
    la EJECUTA en la puerta por la que toda transición pasa antes de confirmarse.
    """
    return (-int(entrada["prioridad"]),
            -int(entrada["grado_de_salida"]),
            -int(entrada["tiempo_listo"]),
            str(entrada["paquete"]))


def motivo_de_postergacion(entrada, cabeza):
    """POR QUÉ este paquete no fue el elegido. Es el `impedimento` de `b.12`.

    Se deriva comparando criterio a criterio contra el que sí se llevó el turno, y se para en
    el PRIMERO que decide: así el texto publicado nombra el criterio que realmente mandó, y
    no una lista de los cuatro. Que cada criterio produzca un `impedimento` distinto es lo que
    hace que sabotear uno solo se pueda ver desde fuera.
    """
    if entrada["paquete"] == cabeza["paquete"]:
        return ""
    if int(entrada["prioridad"]) < int(cabeza["prioridad"]):
        return ("prioridad declarada: `" + str(cabeza["paquete"]) + "` la tiene en "
                + str(cabeza["prioridad"]) + " y este paquete en "
                + str(entrada["prioridad"]) + " (`b.12` paso 5 a)")
    if int(entrada["grado_de_salida"]) < int(cabeza["grado_de_salida"]):
        return ("grado de salida: `" + str(cabeza["paquete"]) + "` desbloquea "
                + str(cabeza["grado_de_salida"]) + " paquete(s) y este "
                + str(entrada["grado_de_salida"]) + " (`b.12` paso 5 b)")
    if int(entrada["tiempo_listo"]) < int(cabeza["tiempo_listo"]):
        return ("antigüedad de espera: `" + str(cabeza["paquete"]) + "` lleva "
                + str(cabeza["tiempo_listo"]) + " revisiones esperando y este "
                + str(entrada["tiempo_listo"]) + " (`b.12` paso 5 c)")
    return ("empate en prioridad, grado de salida y antigüedad: manda el identificador, y `"
            + str(cabeza["paquete"]) + "` ordena antes (`b.12` paso 5 d)")

CLASE_COMPLETADO = "completado"
CLASE_REINTENTABLE = "reintentable"
CLASE_DEFINITIVO = "definitivo"
CLASE_CANCELACION = "cancelacion"
CLASE_AMBIGUA = "ambigua"

CLASES = (CLASE_COMPLETADO, CLASE_REINTENTABLE, CLASE_DEFINITIVO, CLASE_CANCELACION,
          CLASE_AMBIGUA)

# Lo que el §4.4 fija que devuelve `Adaptador.ejecutar`. Es también, y sobre todo, la LISTA
# BLANCA de lo que puede llegar al estado canónico: ver `durable()`.
CLAVES_DE_RESULTADO = ("estado", "codigo", "salida", "detalle", "reintentable", "efecto",
                       "repetido")
ESTADOS_DE_RESULTADO = ("completado", "fallido", "cancelado", "timeout", "ambiguo")

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


def durable(resultado):
    """La parte del resultado que PUEDE escribirse en el estado canónico. LISTA BLANCA.

    Defecto que previene, y lo encontró la auditoría independiente: el adaptador de proceso
    real devuelve `"pid": 1700531` en su resultado, y el resultado entero se copiaba al
    paquete. Un pid en `canonico/paquetes/<id>.json` es identidad de proceso en un byte
    durable, y `I-g3` lo prohíbe sin matices.

    DECISIÓN · lista BLANCA de lo que entra, y no lista negra de lo que no
        Alternativas: (a) borrar las claves conocidas como volátiles —`pid`, `duracion`,
        `inicio`, `fin`—; (b) conservar sólo las claves que el §4.4 declara.
        Se elige (b). Una lista negra envieja con el primer campo nuevo que añada cualquier
        adaptador: el día que uno devuelva `host`, `reintento_numero` o `sesion`, entrará
        solo y en silencio, y el defecto reaparecerá exactamente donde ya estuvo. La lista
        blanca es el contrato del §4.4 y no crece por accidente; un adaptador que quiera
        publicar un campo nuevo tendrá que pasar por el contrato, que es donde se decide.

    Lo que se descarta NO se pierde: sigue en la evidencia del adaptador, que vive en su
    espacio de trabajo y fuera del árbol verificado, que es su sitio.
    """
    return {clave: resultado[clave] for clave in CLAVES_DE_RESULTADO}


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
    if estado == "ambiguo":
        return CLASE_AMBIGUA, EjecucionAmbigua(
            "el adaptador NO PUEDE AFIRMAR si el efecto se aplicó"
            + (": " + detalle if detalle else "")
            + "; la salida la decide la autoridad por `g.9`",
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
    if clase in (CLASE_REINTENTABLE, CLASE_DEFINITIVO, CLASE_AMBIGUA):
        # `ambigua` también aterriza en `fallido`, y desde ahí la política la manda a
        # `agotado`. No es que se dé por fallida: es que `fallido` → `agotado` es el único
        # camino de la tabla del §4.2 que lleva a donde tiene que llegar, que es a manos de
        # la autoridad. El paquete conserva su resultado con `estado: "ambiguo"`, y la
        # causa del registro de `g.9` lo nombra.
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
    if clase == CLASE_AMBIGUA:
        # NUNCA se reintenta, queden los intentos que queden: reintentar es exactamente el
        # riesgo de aplicar dos veces un efecto que quizá ya se aplicó.
        return DECISION_AGOTAR
    if clase == CLASE_REINTENTABLE:
        return DECISION_REINTENTAR if quedan_intentos(paquete) else DECISION_AGOTAR
    raise RuntimeInconsistente("clase de fallo desconocida: " + repr(clase))


def causa_de_reconciliacion(clase, error, paquete):
    """El texto de `causa` que va al registro auxiliar de `g.9`. Determinista y sin rutas."""
    codigo = error.codigo if error is not None else "SIN_ERROR"
    return (codigo + ": " + clase + " tras " + str(paquete["intentos"]) + " de "
            + str(paquete["max_intentos"]) + " intento(s)")
