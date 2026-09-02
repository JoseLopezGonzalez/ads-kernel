#!/usr/bin/env python3
"""modelo — la forma DURABLE del trabajo del runtime, y su vocabulario cerrado.

Instancia el §3 del contrato del corte 2. Aquí no hay estado: hay la DESCRIPCIÓN de los
objetos que el runtime escribe en el estado canónico del motor y las reglas que decidem si
un objeto leído es admisible. Ningún módulo de este paquete guarda una copia en memoria de
lo que este módulo describe; se lee del `Almacen` cada vez.

Los cuatro dominios del §3, y ni uno más:

    canonico/items/<id>.json          la unidad de trabajo del Owner
    canonico/paquetes/<id>.json       la unidad de DESPACHO
    canonico/leases/<paquete>.json    la autoridad temporal sobre un paquete
    canonico/efectos/<efecto>.json    el acuse durable de un efecto ya aplicado

DECISIÓN · `efecto` = `"ef-" + <12 hex del cid>`, y no los doce primeros del `cid` entero
    El §3 escribe `"ef-" + cid(orden + paquete + intento)[:12]`. `cid()` del motor
    devuelve `"sha256:<64 hex>"`, de modo que sus doce primeros caracteres serían
    `sha256:hexde`: llevan dos puntos, y `rutas.SEGMENTO_VALIDO` no admite `:` en el
    nombre de un objeto canónico. El acuse no podría escribirse. Se toman los doce
    primeros del DIGEST, que es lo que la fórmula quiere decir y lo único que produce un
    identificador escribible. Doce hex son 48 bits, y el identificador sólo tiene que ser
    único dentro de un almacén.

DECISIÓN · el `intento` entra en el efecto, y por eso un reintento NO reutiliza el acuse
    Alternativas: (a) derivar el efecto sólo de `orden + paquete`; (b) incluir el intento.
    Se elige (b), que es lo que el §3 escribe. Con (a), el acuse del primer intento
    fallido impediría para siempre el segundo, y la política de reintentos del §4.2 sería
    letra muerta. Con (b), cada intento tiene su propio acuse y la idempotencia protege lo
    que tiene que proteger: que UN intento ya aplicado no se aplique dos veces.

DECISIÓN · la tabla de transiciones es un DATO, no una cadena de `if`
    El §4.2 la publica como tabla. Escribirla como tabla permite que una prueba recorra
    las cien combinaciones y compruebe que las permitidas son exactamente ésas; escrita
    como condicionales, la prueba tendría que reproducir los condicionales, y comprobaría
    la copia en vez del original.
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto

from .errores import EstadoDePaqueteInvalido, RuntimeInconsistente

ESQUEMA = "ads.estado/1"

DOMINIO_ITEMS = "items"
DOMINIO_PAQUETES = "paquetes"
DOMINIO_LEASES = "leases"
DOMINIO_EFECTOS = "efectos"

PREFIJO_EFECTO = "ef-"
LONGITUD_DEL_EFECTO = 12

# ------------------------------------------------------------- vocabulario CERRADO
# El §3 lo fija y ninguna otra palabra vale. Se declara como tupla ordenada por el propio
# texto del contrato para que confrontarla sea leer, no interpretar.
ESTADOS = (
    "listo", "despachado", "ejecutando", "completado", "fallido", "agotado",
    "pausado", "cancelado", "bloqueado", "esperando-dependencia",
)

ESTADOS_TERMINALES = ("completado", "cancelado")
ESTADOS_EN_CURSO = ("despachado", "ejecutando")

# Tabla del §4.2, literal. Cualquier par que no esté aquí es `EstadoDePaqueteInvalido`.
TRANSICIONES = {
    "listo": ("despachado", "pausado", "cancelado", "bloqueado", "esperando-dependencia"),
    "despachado": ("ejecutando", "listo", "fallido", "cancelado"),
    "ejecutando": ("completado", "fallido", "cancelado"),
    "fallido": ("listo", "agotado"),
    "agotado": ("listo",),
    "pausado": ("listo", "cancelado"),
    "bloqueado": ("listo", "cancelado"),
    "esperando-dependencia": ("listo", "bloqueado", "cancelado"),
    "completado": (),
    "cancelado": (),
}

CLAVES_DE_PAQUETE = (
    "id", "item", "estado", "capacidades_requeridas", "prioridad", "intentos",
    "max_intentos", "depende_de", "orden", "efecto", "resultado",
)

CLAVES_DE_ORDEN = ("adaptador", "operacion", "argumentos", "limite_segundos")


# ------------------------------------------------------------------------ rutas
def ruta_item(identificador):
    return DOMINIO_ITEMS + "/" + identificador + ".json"


def ruta_paquete(identificador):
    return DOMINIO_PAQUETES + "/" + identificador + ".json"


def ruta_lease(paquete):
    return DOMINIO_LEASES + "/" + paquete + ".json"


def ruta_efecto(efecto):
    return DOMINIO_EFECTOS + "/" + efecto + ".json"


def identificador_de(ruta):
    """`paquetes/pq-1.json` → `pq-1`. La ruta lógica del motor tiene siempre dos segmentos."""
    return ruta.split("/", 1)[1][: -len(".json")]


# ---------------------------------------------------------------------- efectos
def derivar_efecto(orden, paquete, intento):
    """`ef-<12 hex>` del contenido de la orden, el paquete y el intento (§3).

    Es una función PURA de datos durables: sin reloj, sin pid, sin contador de ejecución.
    Dos runtimes distintos que atiendan el mismo intento del mismo paquete derivan el
    MISMO efecto, y por eso el acuse de uno vale para el otro, que es lo que hace que la
    idempotencia sobreviva a un cambio de titular.
    """
    digest = cid_de_objeto({
        "orden": orden,
        "paquete": paquete,
        "intento": int(intento),
    })
    return PREFIJO_EFECTO + digest.split(":", 1)[-1][:LONGITUD_DEL_EFECTO]


def nuevo_acuse(*, efecto, paquete, intento, resultado):
    """El acuse durable del §3. Se escribe en la MISMA transición que el resultado."""
    return {
        "esquema": ESQUEMA,
        "efecto": efecto,
        "paquete": paquete,
        "intento": int(intento),
        "resultado_cid": cid_de_objeto(resultado),
        "aplicado": True,
    }


# ----------------------------------------------------------------------- objetos
def nuevo_item(*, identificador, titulo):
    return {
        "esquema": ESQUEMA,
        "id": identificador,
        "titulo": titulo,
        "estado": "abierto",
    }


def nuevo_paquete(*, identificador, item, capacidades_requeridas, orden,
                  prioridad=50, max_intentos=3, depende_de=()):
    """Un paquete recién creado. Nace en `listo` y sin efecto: aún no hay intento abierto."""
    return {
        "esquema": ESQUEMA,
        "id": identificador,
        "item": item,
        "estado": "listo",
        "capacidades_requeridas": list(capacidades_requeridas),
        "prioridad": int(prioridad),
        "intentos": 0,
        "max_intentos": int(max_intentos),
        "depende_de": list(depende_de),
        "orden": normalizar_orden(orden),
        "efecto": None,
        "resultado": None,
    }


def normalizar_orden(orden):
    """La orden del §3, con sus cuatro campos y nada más. Falla cerrado si no casa."""
    if not isinstance(orden, dict):
        raise RuntimeInconsistente(
            "la `orden` de un paquete es un mapa con "
            + ", ".join(CLAVES_DE_ORDEN),
        )
    faltan = [clave for clave in CLAVES_DE_ORDEN if clave not in orden]
    if faltan:
        raise RuntimeInconsistente(
            "la `orden` del paquete no declara " + ", ".join(faltan),
        )
    sobran = sorted(set(orden) - set(CLAVES_DE_ORDEN))
    if sobran:
        raise RuntimeInconsistente(
            "la `orden` del paquete declara campos que el §3 no contempla: "
            + ", ".join(sobran),
        )
    if not isinstance(orden["adaptador"], str) or not orden["adaptador"].strip():
        raise RuntimeInconsistente("`orden.adaptador` es una cadena no vacía")
    if not isinstance(orden["operacion"], str) or not orden["operacion"].strip():
        raise RuntimeInconsistente("`orden.operacion` es una cadena no vacía")
    if not isinstance(orden["argumentos"], list):
        raise RuntimeInconsistente("`orden.argumentos` es una lista")
    limite = orden["limite_segundos"]
    if not isinstance(limite, (int, float)) or isinstance(limite, bool) or limite <= 0:
        raise RuntimeInconsistente("`orden.limite_segundos` es un número positivo")
    return {
        "adaptador": orden["adaptador"],
        "operacion": orden["operacion"],
        "argumentos": list(orden["argumentos"]),
        "limite_segundos": limite,
    }


# ------------------------------------------------------------------ validaciones
def comprobar_paquete(objeto, ruta):
    """FALLO CERRADO (§4.2, capacidad 20) ante un paquete que no casa con ninguna regla.

    No se rellena lo que falte y no se supone un estado por defecto: un paquete cuyo
    `estado` no está en el vocabulario cerrado no es «un paquete raro», es un objeto que
    ninguna regla del contrato sabe interpretar, y despacharlo sería inventar estado, que
    es lo que `b.14.3` prohíbe en letra.
    """
    if not isinstance(objeto, dict):
        raise RuntimeInconsistente("el paquete no es un mapa JSON", ruta=ruta)
    faltan = [clave for clave in CLAVES_DE_PAQUETE if clave not in objeto]
    if faltan:
        raise RuntimeInconsistente(
            "el paquete no declara " + ", ".join(faltan), ruta=ruta,
        )
    if objeto["estado"] not in ESTADOS:
        raise RuntimeInconsistente(
            "`estado` no pertenece al vocabulario cerrado del §3: "
            + repr(objeto["estado"]) + "; válidos: " + ", ".join(ESTADOS),
            ruta=ruta, encontrado=str(objeto["estado"]),
        )
    if not isinstance(objeto["capacidades_requeridas"], list):
        raise RuntimeInconsistente("`capacidades_requeridas` es una lista", ruta=ruta)
    if not isinstance(objeto["depende_de"], list):
        raise RuntimeInconsistente("`depende_de` es una lista", ruta=ruta)
    for nombre in ("intentos", "max_intentos", "prioridad"):
        valor = objeto[nombre]
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise RuntimeInconsistente("`" + nombre + "` es un entero", ruta=ruta)
    if objeto["intentos"] < 0 or objeto["max_intentos"] < 1:
        raise RuntimeInconsistente(
            "`intentos` no puede ser negativo ni `max_intentos` menor que 1", ruta=ruta,
        )
    if objeto["intentos"] > objeto["max_intentos"]:
        raise RuntimeInconsistente(
            "el paquete declara más intentos consumidos (" + str(objeto["intentos"])
            + ") que su tope (" + str(objeto["max_intentos"]) + "); la política del §4.2 "
            "no puede haber producido este estado",
            ruta=ruta,
        )
    normalizar_orden(objeto["orden"])
    if objeto["efecto"] is not None and not isinstance(objeto["efecto"], str):
        raise RuntimeInconsistente("`efecto` es una cadena o `null`", ruta=ruta)
    if objeto["estado"] in ESTADOS_EN_CURSO and not objeto["efecto"]:
        raise RuntimeInconsistente(
            "un paquete en `" + objeto["estado"] + "` sin `efecto` no es interpretable: "
            "no hay forma de saber si su efecto ya se aplicó",
            ruta=ruta,
        )
    return objeto


def comprobar_transicion(desde, hasta, *, paquete=None):
    """La tabla del §4.2 aplicada. Cualquier par que no esté en ella es un error tipado."""
    if desde not in TRANSICIONES:
        raise RuntimeInconsistente(
            "estado de origen fuera del vocabulario cerrado: " + repr(desde),
            ruta=paquete,
        )
    if hasta not in ESTADOS:
        raise RuntimeInconsistente(
            "estado de destino fuera del vocabulario cerrado: " + repr(hasta),
            ruta=paquete,
        )
    if hasta not in TRANSICIONES[desde]:
        raise EstadoDePaqueteInvalido(
            "la tabla del §4.2 no permite `" + desde + "` → `" + hasta + "`; permitidas "
            "desde `" + desde + "`: "
            + (", ".join(TRANSICIONES[desde]) if TRANSICIONES[desde] else "(ninguna: es terminal)"),
            ruta=paquete, desde=desde, hasta=hasta,
        )
    return hasta


def con_estado(paquete, estado, **cambios):
    """Copia del paquete con el `estado` nuevo YA comprobado contra la tabla del §4.2."""
    comprobar_transicion(paquete["estado"], estado, paquete=paquete["id"])
    nuevo = dict(paquete)
    nuevo["estado"] = estado
    nuevo.update(cambios)
    return nuevo
