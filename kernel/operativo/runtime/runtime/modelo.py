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
    "max_intentos", "depende_de", "orden", "efecto", "resultado", "acoplamiento",
    "seleccion",
)

# ------------------------------------------------------- `b.12` · INANICIÓN
# Los CUATRO campos que `b.12` obliga a MANTENER Y MOSTRAR por cada paquete `listo` no
# despachado. De los cuatro sólo existía `impedimento`, y de nombre: el dispatcher ordenaba
# por `(-prioridad, id)` y no contaba nada.
#
# DECISIÓN · los contadores son DURABLES y viven en el PAQUETE, no en memoria
#     Alternativas: (a) contarlos en el planificador mientras corre; (b) un dominio canónico
#     propio de contadores; (c) en el objeto durable del paquete.
#     Se elige (c). Con (a) una caída borra la evidencia de inanición justo cuando más falta
#     hace —un paquete que lleva cuarenta postergaciones es EXACTAMENTE lo que hay que ver
#     tras un reinicio—, y dos planificadores tendrían cada uno su cuenta. Con (b) habría dos
#     objetos que hay que escribir juntos para que el estado sea coherente, y el motor ya
#     ofrece la transacción multiarchivo, pero el contador no tiene vida propia: es del
#     paquete, y separarlo sólo añade una forma de que discrepen. Con (c) la cuenta viaja con
#     su sujeto, la escribe la misma transición que lo mueve y sobrevive a la reanudación.
#
# DECISIÓN · `tiempo_listo` se mide con el RELOJ LÓGICO del estado durable
#     `a.9` prohíbe la hora de pared en el estado canónico, y `registro_pruebas.py` lo
#     repite: un estado que lleva `time.time()` deja de ser reproducible y dos ejecuciones
#     del mismo escenario dejan de producir los mismos bytes. El motor ya publica un contador
#     monótono por revisión —`Almacen.revision()["revision"]`—, que es el orden en que los
#     sucesos ocurrieron de verdad. `listo_en` guarda la revisión en la que el paquete entró
#     en `listo`, y la antigüedad es la resta contra la revisión vigente. No se inventa reloj
#     nuevo porque ya había uno, y tener dos sería tener dos órdenes del tiempo.
CAMPOS_DE_SELECCION = ("listo_en", "postergaciones", "adelantado_por", "impedimento")

# La DECLARACIÓN DE ACOPLAMIENTO de `a.5`, con los dos campos que `E2.2` le añade.
#
# DEFECTO QUE CIERRA, encontrado por la auditoría independiente: el paquete durable NO
# llevaba esta declaración, de modo que la etapa 4 del `§7.2` —«DSP crea paquetes con su
# declaración de acoplamiento, incluidas `lee_fuentes` y `escribe_fuentes` (E2.2)»— no
# estaba implementada, y con ella faltaba TODO el insumo de la condición compuesta de
# paralelismo de `a.5`. Sin estos campos, la única condición evaluable habría sido la
# física, que es exactamente la que `a.5` prohíbe usar por sí sola.
CAMPOS_DE_ACOPLAMIENTO = (
    "escribe_ficheros",     # qué artefactos físicos modifica
    "afecta_contratos",     # qué contratos, endpoints, esquemas o APIs toca
    "afecta_decisiones",    # sobre qué decisiones ejerce autoridad
    "based_on",             # fuentes y VERSIONES de las que parte
    "integra_en",           # dónde y cómo vuelve su resultado
    "lee_fuentes",          # `E2.2`: qué sources necesita como CONTEXTO, sin autoridad
    "escribe_fuentes",      # `E2.2`: qué sources puede MODIFICAR
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


def normalizar_acoplamiento(declarado=None):
    """La declaración de acoplamiento, con sus siete campos y NINGUNO por omisión.

    Una ausencia se escribe como lista VACÍA declarada, no como campo que falta: «no toca
    ningún contrato» y «nadie ha dicho qué contratos toca» son cosas distintas, y la
    condición compuesta de `a.5` necesita distinguirlas para no autorizar en silencio.
    """
    declarado = dict(declarado or {})
    sobran = sorted(set(declarado) - set(CAMPOS_DE_ACOPLAMIENTO))
    if sobran:
        raise RuntimeInconsistente(
            "la declaración de acoplamiento trae campos que `a.5` y `E2.2` no contemplan: "
            + ", ".join(sobran),
        )
    salida = {}
    for campo in CAMPOS_DE_ACOPLAMIENTO:
        valor = declarado.get(campo, [])
        if campo == "integra_en":
            salida[campo] = str(valor or "")
            continue
        if not isinstance(valor, (list, tuple)):
            raise RuntimeInconsistente(
                "`acoplamiento." + campo + "` es una lista de identificadores",
            )
        salida[campo] = sorted(str(elemento) for elemento in valor)
    return salida


def nueva_seleccion(*, listo_en=None):
    """Los cuatro campos de inanición de `b.12`, recién nacidos y explícitos."""
    return {"listo_en": listo_en, "postergaciones": 0, "adelantado_por": [],
            "impedimento": ""}


def normalizar_seleccion(declarado, *, ruta=None):
    """FALLO CERRADO sobre los cuatro campos. Ni se rellenan ni se toleran de más."""
    if not isinstance(declarado, dict):
        raise RuntimeInconsistente(
            "`seleccion` es el mapa de los cuatro campos de inanición de `b.12`: "
            + ", ".join(CAMPOS_DE_SELECCION), ruta=ruta,
        )
    sobran = sorted(set(declarado) - set(CAMPOS_DE_SELECCION))
    faltan = [c for c in CAMPOS_DE_SELECCION if c not in declarado]
    if sobran or faltan:
        raise RuntimeInconsistente(
            "`seleccion` declara " + (", ".join(sobran) or "(nada)") + " de más y le "
            "faltan " + (", ".join(faltan) or "(nada)") + "; `b.12` nombra CUATRO campos "
            "y son exactamente esos", ruta=ruta,
        )
    listo_en = declarado["listo_en"]
    if listo_en is not None and (not isinstance(listo_en, int) or isinstance(listo_en, bool)
                                 or listo_en < 0):
        raise RuntimeInconsistente(
            "`seleccion.listo_en` es la REVISIÓN en que el paquete entró en `listo`: un "
            "entero >= 0 del reloj lógico, o `null` si nunca entró", ruta=ruta,
        )
    postergaciones = declarado["postergaciones"]
    if not isinstance(postergaciones, int) or isinstance(postergaciones, bool) \
            or postergaciones < 0:
        raise RuntimeInconsistente(
            "`seleccion.postergaciones` es un recuento entero >= 0", ruta=ruta,
        )
    adelantado = declarado["adelantado_por"]
    if not isinstance(adelantado, (list, tuple)):
        raise RuntimeInconsistente(
            "`seleccion.adelantado_por` es la lista de paquetes que lo adelantaron",
            ruta=ruta,
        )
    if not isinstance(declarado["impedimento"], str):
        raise RuntimeInconsistente(
            "`seleccion.impedimento` es el texto de QUÉ lo impide, vacío si nada lo impide",
            ruta=ruta,
        )
    return {
        "listo_en": listo_en,
        "postergaciones": int(postergaciones),
        # Ordenado y sin repetidos: es un CONJUNTO de quién le pasó por delante, y `I-g3`
        # exige que dos ejecuciones del mismo escenario escriban los mismos bytes.
        "adelantado_por": sorted({str(p) for p in adelantado}),
        "impedimento": str(declarado["impedimento"]),
    }


def nuevo_paquete(*, identificador, item, capacidades_requeridas, orden,
                  prioridad=50, max_intentos=3, depende_de=(), acoplamiento=None,
                  listo_en=None):
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
        "acoplamiento": normalizar_acoplamiento(acoplamiento),
        # Nace `listo`, así que su espera empieza AQUÍ y no cuando alguien se acuerde.
        "seleccion": nueva_seleccion(listo_en=listo_en),
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
    normalizar_acoplamiento(objeto.get("acoplamiento"))
    normalizar_seleccion(objeto.get("seleccion"), ruta=ruta)
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


def con_estado(paquete, estado, *, reloj=None, **cambios):
    """Copia del paquete con el `estado` nuevo YA comprobado contra la tabla del §4.2.

    `reloj` es el instante LÓGICO —la revisión que la transición va a escribir— y es
    OBLIGATORIO cuando el paquete ENTRA en `listo`, porque es ahí donde empieza la espera que
    `b.12` obliga a medir. Pasarlo por omisión sería dejar `listo_en` a `null` en el camino
    que más importa —el reintento y la liberación, que es cuando un paquete vuelve a la cola
    y se le empieza a acumular la antigüedad—, y un `tiempo_listo` que no se mide es un campo
    publicado que no dice nada.

    Los contadores `postergaciones` y `adelantado_por` NO se ponen a cero al salir de
    `listo`: son la historia de la inanición del paquete, y borrarla en el despacho es
    perder justo la evidencia de que estuvo a punto de no despacharse nunca.
    """
    comprobar_transicion(paquete["estado"], estado, paquete=paquete["id"])
    nuevo = dict(paquete)
    nuevo["estado"] = estado
    seleccion = normalizar_seleccion(paquete.get("seleccion"), ruta=paquete["id"])
    if estado == "listo" and paquete["estado"] != "listo":
        if not isinstance(reloj, int) or isinstance(reloj, bool) or reloj < 0:
            raise RuntimeInconsistente(
                "un paquete que entra en `listo` necesita el instante lógico en que entra: "
                "sin él, `b.12` no puede medir la antigüedad de espera y la prevención de "
                "inanición se queda sin su tercer criterio", ruta=paquete["id"],
            )
        seleccion["listo_en"] = int(reloj)
        seleccion["impedimento"] = ""
    nuevo["seleccion"] = seleccion
    nuevo.update(cambios)
    return nuevo
