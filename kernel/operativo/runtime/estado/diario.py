#!/usr/bin/env python3
"""diario — el DIARIO CANÓNICO: la secuencia de eventos que EXPLICA el estado (`g.7`).

Es uno de los TRES componentes durables de `g.1`, y no es ninguno de los otros dos. Aquí
importa decir en qué se diferencia MATERIALMENTE, porque `I-g7` prohíbe colapsarlos:

    ESTADO CANÓNICO      JSON indentado, un fichero por entidad, SOBRESCRIBIBLE por
                         `os.replace`, sin orden entre entidades, sin cadena de hash.
                         Responde «¿qué es verdad ahora?» y se lee sin reproyectar nada.

    DIARIO CANÓNICO      JSONL append-only, UNA sola secuencia total, encadenado por hash.
                         Ninguna escritura ORDINARIA reescribe una línea; la única que las
                         toca es el SELLADO de `g.7`, que es una transición explícita, deja
                         su propio evento y no altera ni una huella ni un eslabón —ver más
                         abajo—. Responde «¿cómo llegó a serlo?».
                         No es sede del estado: borrar el diario no cambia ni un dato del
                         estado canónico, y borrar un objeto canónico no cambia ni una
                         línea del diario. Esa independencia es la prueba de `I-g7`.

    REGISTRO AUXILIAR    otro fichero, otra cadena, otro bloqueo, otro vocabulario
    (reconciliacion.py)  (`apertura`/`resolucion` frente a `transicion.*`) y otra
                         semántica: lo que el runtime NO PUDO hacer.

DECISIÓN · cadena de hash sobre el diario, y no un simple contador
    Alternativas: (a) confiar en `secuencia`; (b) encadenar cada evento con la huella del
    anterior.
    Se elige (b). Con (a), quitar una línea del medio y renumerar deja un diario
    perfectamente coherente, y entonces `g.13` —«todo cambio del estado canónico es
    explicable por el diario»— se puede satisfacer borrando lo inexplicable. Con la cadena,
    retirar, insertar o editar cualquier línea rompe `previo` en la siguiente y el fallo es
    cerrado. Se conserva ADEMÁS `secuencia`, porque el «momento» que `g.9` exige registrar
    es el MOMENTO LÓGICO —el número de secuencia—, y no una hora de pared que `I-g3` veda.

DECISIÓN · el anexado es UN SOLO `os.write` sobre un descriptor `O_APPEND`
    Alternativas: (a) `open(..., "a")` de `io`, con su búfer; (b) descriptor crudo en
    `O_APPEND` y una única llamada al sistema por línea.
    Se elige (b). Con (a), el búfer de `io` puede partir la línea en dos escrituras y un
    corte entre ambas deja media línea y media verdad. Con `O_APPEND` el desplazamiento y
    la escritura son atómicos respecto a otros escritores, y una sola llamada con la línea
    entera hace que el desgarro sólo sea posible por debajo, en el medio físico.

DECISIÓN · una COLA DESGARRADA se repara; un hueco INTERMEDIO es corrupción
    Un corte durante el anexado puede dejar una última línea incompleta. Alternativas:
    (a) declarar corrupto el diario y exigir intervención; (b) tratar la línea incompleta
    como un evento que NUNCA llegó a ser durable, descartarla bajo el bloqueo de escritor y
    seguir.
    Se elige (b), y sólo para la ÚLTIMA línea. Con (a) cualquier corte inyectado por el §10
    dejaría el almacén irrecuperable, y `g.8` exige justo lo contrario: que lo incompleto se
    detecte y se termine o se revierta. Un evento cuyos bytes no llegaron enteros al medio
    no es durable por definición de `g.4`, así que descartarlo no pierde ninguna verdad: la
    transacción que lo iba a explicar queda sin cerrar y la recuperación la ve. En cambio
    una línea rota EN MEDIO, o una huella que no casa, es manipulación o daño del medio, y
    ahí el fallo es CERRADO: `DiarioCorrupto`, sin tocar el estado canónico.
    `verificar_integridad` NO repara: si ve la cola desgarrada, la denuncia.

===========================================================================================
EL SELLADO (`g.7`) — se compacta el CUERPO, jamás el ESLABÓN
===========================================================================================

`g.7` escribe cinco puntos y los dos últimos son éstos: «el SELLADO compacta el diario
conservando lo que el estado y la auditabilidad exigen; su umbral es parámetro CALIBRABLE
del contrato derivado» y «retirar el cuerpo de un evento sellado exige una transición
explícita y auditable». Lo que sigue es cómo se instancian, y qué se descartó.

DECISIÓN · sellar RETIRA EL CUERPO de un evento; NO retira su LÍNEA
    Alternativas: (a) borrar del fichero las líneas viejas y renumerar; (b) reescribir el
    diario dejando sólo un resumen; (c) conservar TODAS las líneas y vaciar el CUERPO de las
    que se sellan, dejando intacto el ESLABÓN —`esquema`, `secuencia`, `tipo`, `previo`,
    `huella`—.
    Se elige (c), y manda la CADENA. Con (a) se rompe todo a la vez: `_verificar_eslabon`
    exige `secuencia == indice + 1`, así que quitar una línea del medio invalida el diario
    entero, y renumerar destruye el `previo` de la siguiente; además `exigir_coherente`
    compara el recuento de líneas con el `diario_secuencia` que `REVISION.json` publica, y
    un diario más corto que su propia revisión es corrupción por definición. Con (b) el
    diario deja de ser el diario. Con (c) el fichero sigue teniendo una línea por evento, en
    el mismo orden y con las mismas huellas, de modo que la verificación eslabón a eslabón,
    la detección de bifurcación y la recuperación siguen leyendo lo mismo que leían.
    Lo que se gana es el CUERPO, que es donde está el peso: `operaciones`, `motivo`,
    `divergencias` y los anexos.

DECISIÓN · la huella de un evento sellado NO se recalcula, y se dice por qué
    `huella` es el `cid` del evento SIN `huella`, es decir, de su contenido. Retirar
    contenido y pretender recalcular la misma huella es pedir una preimagen: no se puede, y
    fingir que sí sería el defecto. Alternativas ante ese hecho: (a) recalcular la huella del
    talón —y romper el `previo` de todos los eventos siguientes—; (b) conservar la huella y
    aceptarla sin más; (c) conservar la huella y ANCLARLA en un evento del propio diario.
    Se elige (c). (a) rompe la cadena, que es justo lo que no se puede tocar. (b) dejaría un
    talón editable a mano sin que nada lo notase. Con (c), el evento `diario.sellado` que
    explica la retirada declara `cid_sellados`, el `cid` de la lista ORDENADA de pares
    `[secuencia, cid del talón entero]` de todos los talones; ese evento se encadena y
    se huella como cualquier otro, así que alterar un talón cambia el `cid` calculado y no
    casa, y alterar el evento de sellado cambia su huella y rompe el `previo` del siguiente.
    RESIDUO, dicho y no callado: falsificar A LA VEZ un talón y el evento de sellado cuando
    éste es la ÚLTIMA línea del diario no es detectable desde dentro del árbol. Es el mismo
    residuo que el §6 declara para la cola del registro auxiliar, vuelve a ser detectable en
    cuanto el diario anexa otra vez, y es literalmente lo que `g.15` reserva a la raíz
    externa.

DECISIÓN · lo que NO se compacta, y por qué no
    `almacen.inicializado` · `auditar()` arranca el linaje en su `resultado` y sin él la
        historia del estado no empieza en ninguna parte. Es UNA línea por almacén.
    `transicion.preparada` · es el PUNTO DE NO RETORNO. Su `operaciones` lo lee la rama
        COMPLETAR de `g.8` para republicar, `auditar()` para reproyectar `raiz` y reproducir
        `cid_raiz` desde el origen, y `_resultado_si_repetida` para negarse a reutilizar un
        identificador con otro plan. Compactarlo obligaría a sustituir la reproducción por un
        ANCLA escrita por el sellador, y entonces `g.13` —«todo cambio del estado canónico es
        explicable por el diario»— pasaría a apoyarse en un resumen en vez de en la historia.
    `transicion.marcada`, y NINGÚN evento de una transacción marcada · una transacción
        marcada espera la decisión de LA AUTORIDAD (`g.8`). Su cuerpo todavía es prueba viva.
    toda transacción SIN evento terminal · es la ventana de `g.8`. Se dice más abajo.
    Lo que sí se sella son `transicion.abierta`, `transicion.confirmada`,
    `transicion.revertida`, los dos eventos de reconciliación y `migracion.aplicada`: dos de
    cada tres eventos del camino feliz, que es donde está la masa del fichero.

DECISIÓN · el UMBRAL se lee del CONTRATO DERIVADO, no de una constante de este módulo
    Alternativas: (a) una constante con nombre en mayúsculas; (b) una variable de entorno;
    (c) un bloque declarado en `CONTRATO-ESTADO-DURABLE.md`, que es la sede que `g.7` nombra.
    Se elige (c). Con (a) el parámetro no es calibrable: es código, y cambiarlo es tocar el
    motor. Con (b) el estado durable dependería del entorno de quien ejecuta, que es
    exactamente lo que `I-g3` y el precedente de `a.9` en `runtime/politica.py` rechazan. Con
    (c) el valor vive donde `g.7` dice que vive, viaja al proyecto instalado con el resto del
    contrato y se cambia editando el contrato. El precio es que el contrato pasa a ser
    material que el motor LEE, y por eso su ausencia, su ilegibilidad y un valor absurdo son
    FALLO CERRADO y no un valor por omisión: un motor que se inventa el umbral cuando no lo
    encuentra convierte la sede en decorado.

===========================================================================================
LA SEGMENTACIÓN — el diario se reparte en ficheros, y NI UNA LÍNEA cambia
===========================================================================================

MEDIDO el 2026-10-17 en una instancia real: 81.860 eventos, 59 MiB en un solo fichero que
crece de 2 a 5 MiB al día, y GitHub RECHAZA el push de un fichero de más de 100 MiB. El
sellado no lo resuelve: retira cuerpos —el Owner no autoriza retirarlos— y `preparada`, un
tercio del fichero, no se sella nunca.

DECISIÓN · se cierra el diario VIVO entero como segmento inmutable; no se reescribe nada
    Alternativas: (a) sellar; (b) comprimir; (c) mover las líneas, tal cual, a un fichero
    cerrado y seguir anexando en uno vacío.
    Se elige (c). Con (a) se pierde contenido del fichero de trabajo. Con (b) el diario deja
    de leerse con `tail` y cambia su formato. Con (c) cada línea conserva sus bytes, su
    `secuencia`, su `huella` y su `previo`: la cadena atraviesa el corte porque el primer
    evento del vivo nuevo lleva como `previo` la huella del último del segmento, que es
    exactamente lo que `anexar` ya calcula sobre la lista completa.

    estado/diario/DIARIO.jsonl                    el VIVO: el único que se anexa
    estado/diario/segmentos/DIARIO-<d>-<h>.jsonl  cerrados, con sus bytes, para siempre
    estado/diario/segmentos/INDICE.json           por segmento: desde, hasta, bytes,
                                                  sha256, huella del último, autor, motivo

DECISIÓN · la lista de líneas se COMPONE en un solo sitio, y todo lo demás no cambia
    `_lineas()` devuelve segmentos + vivo. Así la verificación eslabón a eslabón, el ancla
    del sellado, `exigir_coherente` frente a `REVISION.diario_secuencia`, `anexar`,
    `siguiente_secuencia`, la ventana y el linaje leen la MISMA lista que leían con un solo
    fichero. Sólo dos operaciones escriben sobre el vivo por su longitud y se acotan a él:
    `reparar_cola`, que trunca únicamente el vivo, y el sellado, que con segmentos se NIEGA
    (los segmentos son inmutables y el Owner no autoriza retirar cuerpos).

DECISIÓN · el ÍNDICE es el punto de no retorno de la rotación
    Tres pasos, cada uno atómico (`escribir_y_sincronizar` + `os.replace` + `fsync` del
    directorio):
        1 · publicar el segmento                  → punto `segmentacion-tras-el-segmento`
        2 · publicar el índice que lo nombra      → punto `segmentacion-tras-el-indice`
        3 · vaciar el vivo
    Un corte tras 1 deja un segmento HUÉRFANO —ningún índice lo nombra— cuyos bytes son un
    prefijo del vivo: el diario sigue siendo el vivo y el huérfano se retira al completar.
    Un corte tras 2 deja el vivo con las MISMAS bytes que el último segmento: se lee como
    vacío (no hay duplicados) y se vacía al completar. Cualquier otro huérfano, o un vivo
    que empiece igual que el último segmento sin serlo entero, es manipulación: FALLO
    CERRADO.

DECISIÓN · el lector toma el VIVO primero, y repite si algo se movió mientras leía
    Un rotador y un lector pueden coincidir. Leyendo primero el vivo se evita la peor mezcla
    —índice viejo con el vivo ya vacío, que perdería eventos—, pero NO basta: si entre las dos
    lecturas un escritor anexa Y rota, el vivo leído ya no es ni el último segmento ni vacío
    (revisión independiente, H3, reproducido). Por eso `_partes` toma la FIRMA del vivo, del
    índice y del listado de `segmentos/` antes y después de leer, y repite hasta que no cambie:
    lo compuesto es lo que el diario era en un instante sin escritores. Los escritores leen
    bajo el bloqueo, así que para ellos la firma no cambia nunca.

RESIDUO, dicho: un segmento cerrado se verifica por su `sha256` del índice y por la cadena;
alterar A LA VEZ un segmento, su `sha256` y la cadena entera hasta el final del vivo no es
detectable desde dentro del árbol, igual que el residuo del sellado: es lo que `g.15`
reserva a la raíz externa.
"""
from __future__ import annotations

import hashlib
import json
import os
import re

from . import fallos
from .errores import (
    DiarioCorrupto,
    RetiradaNoAdmisible,
    RetiradaSinTransicion,
    EscritorConcurrente,
    SegmentacionImposible,
    SelladoImposible,
    UmbralDeSelladoInvalido,
)
from .rutas import (
    SUFIJO_TEMPORAL,
    asegurar_directorio,
    borrar_si_existe,
    escribir_y_sincronizar,
    publicar,
    sincronizar_directorio,
    traducir_error_de_sistema,
)
from .serializacion import (
    ESQUEMA,
    cid,
    cid_de_objeto,
    comprobar_esquema,
    deserializar,
    serializar_canonico,
    serializar_compacto,
)

# Los tipos que el §2.4 declara obligatorios. La tupla es el censo: `anexar` rechaza
# cualquier otro, para que no aparezca un vocabulario paralelo por descuido.
TIPOS = (
    "almacen.inicializado",
    "transicion.abierta",
    "transicion.preparada",
    "transicion.confirmada",
    "transicion.revertida",
    "transicion.marcada",
    "reconciliacion.abierta",
    "reconciliacion.resuelta",
    "migracion.aplicada",
    # `g.7` · la transición EXPLÍCITA Y AUDITABLE que retira cuerpos. No es un evento de
    # transacción: no lleva `transaccion`, no cambia el estado canónico y no participa del
    # linaje. Explica una operación sobre el DIARIO, que es la única que puede explicarla.
    "diario.sellado",
)

TERMINALES = ("transicion.confirmada", "transicion.revertida", "transicion.marcada")
TIPO_INICIALIZADO = "almacen.inicializado"
TIPO_PREPARADA = "transicion.preparada"
TIPO_CONFIRMADA = "transicion.confirmada"
# Los tipos que CIERRAN una transacción, por su nombre de contrato. Es `TERMINALES`.
TIPOS_QUE_CIERRAN = TERMINALES


def linaje_de(eventos):
    """La sucesión de `revision_id`, de la revisión 0 a la vigente, según UNA lista de eventos.

    Es LA regla del linaje —la que `Almacen._linaje` aplica sobre su propio diario y la que
    `estado/ramas.py` aplica sobre el diario de otra referencia Git—. Vive aquí, una vez:
    dos definiciones de «qué revisiones ha publicado este diario» serían dos verdades, y la
    segunda sería la que nadie mira. Cuenta la inicialización y cada `preparada` que tenga
    su `confirmada` en la misma transacción; una preparada sin confirmar no publicó nada."""
    agrupados = {}
    for evento in eventos:
        transaccion = evento.get("transaccion")
        if transaccion is not None:
            agrupados.setdefault(transaccion, []).append(evento)
    linaje = []
    for evento in eventos:
        if evento.get("tipo") == TIPO_INICIALIZADO:
            linaje.append(evento["resultado"])
        elif evento.get("tipo") == TIPO_PREPARADA:
            tipos = {e.get("tipo") for e in agrupados.get(evento.get("transaccion"), ())}
            if TIPO_CONFIRMADA in tipos:
                linaje.append(evento["resultado"])
    return linaje

CLAVE_HUELLA = "huella"
CLAVE_PREVIO = "previo"

# ------------------------------------------------------------------ el sellado (`g.7`)
TIPO_SELLADO = "diario.sellado"
CLAVE_SELLADO = "sellado"
ESQUEMA_DEL_SELLADO = 1

# EL ESLABÓN. Es lo que hace verificable la cadena, y el sellado no lo toca NUNCA.
CLAVES_DEL_ESLABON = ("esquema", "secuencia", "tipo", CLAVE_PREVIO, CLAVE_HUELLA)

# Lo que un evento sellado SIGUE DICIENDO además del eslabón. `tipo` y `secuencia` ya están
# en el eslabón, y son el «QUÉ fue» y el «CUÁNDO» —el momento LÓGICO, que es el único que
# `I-g3` admite— que `g.7` exige que sobrevivan. Estos tres se conservan porque hay
# deducciones que los leen sobre eventos ya cerrados y seguirían leyéndolos tras el sellado:
# `por_transaccion` y `transaccion_sin_cerrar` agrupan por `transaccion`, `_linaje` y
# `detectar_bifurcacion` recorren `resultado`, y `_auditar_reconciliacion` casa el diario con
# el registro auxiliar por `registro`.
CLAVES_CONSERVADAS = ("transaccion", "resultado", "registro")

CONSERVADO = CLAVES_DEL_ESLABON + CLAVES_CONSERVADAS

# Tipos cuyo cuerpo NO se retira nunca. El porqué de cada uno está en el docstring.
NO_SELLABLES = (
    "almacen.inicializado",
    "transicion.preparada",
    "transicion.marcada",
    TIPO_SELLADO,
)

# El mínimo de CORRECCIÓN de la cola sin sellar: una transacción entera del camino feliz son
# tres eventos —`abierta`, `preparada`, `confirmada`—, y una cola más corta que una
# transacción no deja legible ni la última. No es la garantía de la recuperación: ésa la da
# la regla de la ventana, que no sella NINGÚN evento de una transacción sin cerrar, y que no
# depende del umbral en absoluto.
MINIMO_DE_LA_COLA = 3

# El nombre del parámetro en el contrato derivado, y el esquema del bloque que lo declara.
CLAVE_UMBRAL = "sellado_umbral_eventos"
ESQUEMA_DE_CALIBRACION = "ads.estado.calibracion/1"
NOMBRE_DEL_CONTRATO = "CONTRATO-ESTADO-DURABLE.md"

# El contrato derivado vive UN nivel por encima del paquete: `runtime/CONTRATO-...md` frente
# a `runtime/estado/diario.py`. Se compone desde `__file__` y NUNCA desde el `cwd`, por la
# misma razón por la que la batería lo hace: el motor se ejecuta desde cualquier directorio.
RUTA_DEL_CONTRATO_DERIVADO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), NOMBRE_DEL_CONTRATO
)

# El bloque de calibración se delimita como un bloque de código JSON del Markdown. Es JSON y
# no YAML por una razón dura: este paquete importa SÓLO biblioteca estándar (`__init__`), y
# `yaml` no lo es. `json` sí, y de paso el bloque se lee con `json.loads` sin analizador
# propio, que es el analizador que no hay que escribir ni mantener.
BLOQUE_JSON = re.compile(r"^```json\s*$")
FIN_DE_BLOQUE = re.compile(r"^```\s*$")


# ------------------------------------------------------------------ la segmentación
DIRECTORIO_DE_SEGMENTOS = "segmentos"
FICHERO_INDICE = "INDICE.json"
ESQUEMA_DEL_INDICE = "ads.estado.segmentos/1"
PATRON_DE_SEGMENTO = re.compile(r"^DIARIO-(\d{7,})-(\d{7,})\.jsonl$")
# Lecturas de una vez antes de rendirse ante un escritor que no para (`_partes`).
INTENTOS_DE_LECTURA_ESTABLE = 50
CLAVES_DE_UN_SEGMENTO = ("fichero", "desde", "hasta", "bytes", "sha256", "huella_ultima",
                         "autor", "motivo")


def nombre_de_segmento(desde, hasta):
    """`DIARIO-0000001-0081860.jsonl`: el rango en el nombre, y ordenable como texto."""
    return "DIARIO-%07d-%07d.jsonl" % (desde, hasta)


def sha256_de(datos):
    return "sha256:" + hashlib.sha256(datos).hexdigest()


def interpretar_indice(crudo, ruta=None):
    """Las entradas de `INDICE.json`, VALIDADAS. `crudo` ausente → ningún segmento.

    Lo que se exige es lo que hace falta para que la composición sea la historia y no otra:
    rangos contiguos desde la secuencia 1, nombre que dice su rango, y las claves con su
    tipo. Un índice que no cumple es FALLO CERRADO: componer «lo que se pueda» es inventar
    historia.
    """
    if crudo is None:
        return []
    try:
        indice = json.loads(crudo.decode("utf-8") if isinstance(crudo, bytes) else crudo)
    except (ValueError, UnicodeDecodeError) as exc:
        raise DiarioCorrupto("el índice de segmentos no es JSON legible: " + str(exc), ruta=ruta)
    if not isinstance(indice, dict) or indice.get("esquema") != ESQUEMA_DEL_INDICE \
            or not isinstance(indice.get("segmentos"), list):
        raise DiarioCorrupto("el índice de segmentos no declara `" + ESQUEMA_DEL_INDICE
                             + "` con su lista de segmentos", ruta=ruta)
    esperado = 1
    for posicion, entrada in enumerate(indice["segmentos"], start=1):
        if not isinstance(entrada, dict) or any(clave not in entrada for clave in CLAVES_DE_UN_SEGMENTO):
            raise DiarioCorrupto("la entrada " + str(posicion) + " del índice de segmentos no "
                                 "tiene sus claves", ruta=ruta, posicion=posicion)
        desde, hasta = entrada["desde"], entrada["hasta"]
        if any(isinstance(v, bool) or not isinstance(v, int) for v in (desde, hasta, entrada["bytes"])):
            raise DiarioCorrupto("la entrada " + str(posicion) + " del índice de segmentos "
                                 "no da su rango y su tamaño como enteros", ruta=ruta, posicion=posicion)
        if desde != esperado or hasta < desde or entrada["bytes"] <= 0:
            raise DiarioCorrupto(
                "los segmentos no son contiguos: la entrada " + str(posicion) + " empieza en "
                + str(desde) + " y se esperaba " + str(esperado) + ". Falta o sobra un segmento",
                ruta=ruta, posicion=posicion, esperado=esperado, encontrado=desde)
        if entrada["fichero"] != nombre_de_segmento(desde, hasta):
            raise DiarioCorrupto("el segmento " + str(posicion) + " se llama `"
                                 + str(entrada["fichero"]) + "` y su rango dice otro nombre",
                                 ruta=ruta, posicion=posicion)
        esperado = hasta + 1
    return indice["segmentos"]


def lineas_de_un_segmento(datos, entrada, ruta=None):
    """Las líneas de un segmento CERRADO, comprobado contra su entrada del índice."""
    if datos is None:
        raise DiarioCorrupto("falta el segmento `" + entrada["fichero"] + "` que el índice "
                             "nombra: se han perdido eventos completos", ruta=ruta,
                             desde=entrada["desde"], hasta=entrada["hasta"])
    if len(datos) != entrada["bytes"] or sha256_de(datos) != entrada["sha256"]:
        raise DiarioCorrupto("el segmento `" + entrada["fichero"] + "` no es el que el índice "
                             "registró: sus bytes cambiaron después de cerrarse", ruta=ruta,
                             desde=entrada["desde"], hasta=entrada["hasta"])
    if not datos.endswith(b"\n") or datos.count(b"\n") != entrada["hasta"] - entrada["desde"] + 1:
        raise DiarioCorrupto("el segmento `" + entrada["fichero"] + "` no tiene una línea "
                             "completa por evento de su rango", ruta=ruta)
    lineas = datos[:-1].split(b"\n")
    ultimo = deserializar(lineas[-1], ruta=ruta, error=DiarioCorrupto)
    if not isinstance(ultimo, dict) or ultimo.get(CLAVE_HUELLA) != entrada["huella_ultima"]:
        raise DiarioCorrupto("el último evento del segmento `" + entrada["fichero"] + "` no "
                             "es el que el índice registró", ruta=ruta)
    return lineas


def componer_lineas(vivo, entradas, lineas_de_segmento, ruta=None):
    """`(lineas_de_segmentos, datos_del_vivo, pendiente)` — la ÚNICA regla de composición.

    La usan `Diario` sobre el disco y `ramas.py` sobre los blobs de otra referencia: dos
    reglas serían dos historias. `lineas_de_segmento(entrada)` devuelve las líneas de un
    segmento ya comprobado contra su entrada. El vivo se compara con el ÚLTIMO segmento por su
    tamaño y su `sha256` del índice, sin retener sus bytes: `pendiente` dice que una rotación
    se cortó tras publicar el índice (el vivo ES el último segmento, y se lee como vacío).
    """
    lineas = []
    for entrada in entradas:
        lineas.extend(lineas_de_segmento(entrada))
    pendiente = False
    if entradas and vivo:
        ultimo = entradas[-1]
        if len(vivo) == ultimo["bytes"] and sha256_de(vivo) == ultimo["sha256"]:
            pendiente, vivo = True, b""
        elif len(vivo) > ultimo["bytes"] and sha256_de(vivo[:ultimo["bytes"]]) == ultimo["sha256"]:
            raise DiarioCorrupto(
                "el diario vivo empieza con las líneas del último segmento y sigue después: "
                "una rotación no deja ese estado; alguien anexó sobre una rotación a medias",
                ruta=ruta)
    return lineas, vivo, pendiente


def calcular_huella(evento):
    """`huella` = `cid` de la forma canónica del evento SIN el campo `huella` (§2.4)."""
    cuerpo = {clave: evento[clave] for clave in evento if clave != CLAVE_HUELLA}
    return cid_de_objeto(cuerpo)


# ===========================================================================
#  el UMBRAL, leído del contrato derivado (`g.7`)
# ===========================================================================
def _bloques_de_calibracion(texto):
    """Los bloques ```json del contrato que declaran ser calibración de este motor."""
    encontrados = []
    dentro, acumulado = False, []
    for linea in texto.splitlines():
        if not dentro:
            if BLOQUE_JSON.match(linea):
                dentro, acumulado = True, []
            continue
        if FIN_DE_BLOQUE.match(linea):
            dentro = False
            try:
                objeto = json.loads("\n".join(acumulado))
            except ValueError:
                # Un bloque JSON roto en el contrato no se ignora en silencio: se recoge
                # como candidato ILEGIBLE, para que el fallo diga «no se puede leer» en vez
                # de «no está», que mandan a sitios distintos.
                encontrados.append(None)
                continue
            if isinstance(objeto, dict) and objeto.get("esquema") == ESQUEMA_DE_CALIBRACION:
                encontrados.append(objeto)
            continue
        acumulado.append(linea)
    return encontrados


def comprobar_umbral(valor, ruta=None):
    """Un umbral que no sirve para calibrar nada es FALLO CERRADO, no un valor por omisión.

    Cuatro formas de no servir, y el §8 las distingue con un solo código porque el remedio
    es el mismo en las cuatro —editar el contrato—: ausente, no entero, cero o negativo, y
    más corto que una transacción entera.
    """
    if valor is None:
        raise UmbralDeSelladoInvalido(
            "el contrato derivado no declara `" + CLAVE_UMBRAL + "`; `g.7` lo hace "
            "CALIBRABLE del contrato, y un umbral ausente NO se sustituye por un valor por "
            "omisión: se falla cerrado y no se sella",
            ruta=ruta, parametro=CLAVE_UMBRAL,
        )
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise UmbralDeSelladoInvalido(
            "el umbral de sellado es un ENTERO de eventos; se declara "
            + type(valor).__name__ + ". Un umbral que no es un recuento no acota ninguna "
            "cola",
            ruta=ruta, parametro=CLAVE_UMBRAL, encontrado=repr(valor),
        )
    if valor < MINIMO_DE_LA_COLA:
        raise UmbralDeSelladoInvalido(
            "el umbral de sellado es " + str(valor) + " y el mínimo es "
            + str(MINIMO_DE_LA_COLA) + ": con cero o menos no hay cola sin sellar, y con "
            "menos de una transacción entera la cola no explica ni la última transición",
            ruta=ruta, parametro=CLAVE_UMBRAL, encontrado=valor,
            minimo=MINIMO_DE_LA_COLA,
        )
    return valor


def umbral_de_sellado(ruta=None):
    """El umbral CALIBRADO en el contrato derivado. Nunca una constante de este módulo.

    `ruta` sólo se pasa para leer OTRA sede del contrato —la batería lo hace para demostrar
    qué pasa cuando el bloque falta o está roto—. En producción es la del aparato.
    """
    ruta = ruta or RUTA_DEL_CONTRATO_DERIVADO
    if not os.path.isfile(ruta):
        raise UmbralDeSelladoInvalido(
            "no se encuentra el contrato derivado `" + NOMBRE_DEL_CONTRATO + "`, que es la "
            "sede donde `g.7` sitúa el umbral. Sin sede no hay calibración, y sin "
            "calibración no se sella",
            ruta=ruta, parametro=CLAVE_UMBRAL,
        )
    try:
        with open(ruta, encoding="utf-8") as fichero:
            texto = fichero.read()
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "leer el contrato derivado") from exc
    except UnicodeDecodeError as exc:
        raise UmbralDeSelladoInvalido(
            "el contrato derivado no es UTF-8 legible: " + str(exc), ruta=ruta,
        ) from exc
    bloques = _bloques_de_calibracion(texto)
    if any(bloque is None for bloque in bloques):
        raise UmbralDeSelladoInvalido(
            "hay un bloque de calibración en el contrato derivado que no es JSON válido; "
            "leerlo «a lo que se pueda» sería adivinar el umbral",
            ruta=ruta, parametro=CLAVE_UMBRAL,
        )
    if not bloques:
        raise UmbralDeSelladoInvalido(
            "el contrato derivado no declara ningún bloque `" + ESQUEMA_DE_CALIBRACION
            + "`: el umbral no está calibrado en su sede",
            ruta=ruta, parametro=CLAVE_UMBRAL,
        )
    if len(bloques) > 1:
        # DOS declaraciones no son «una y una de repuesto»: son dos verdades a la vez, y
        # elegir una es elegir por el contrato. Se falla cerrado.
        raise UmbralDeSelladoInvalido(
            "el contrato derivado declara " + str(len(bloques)) + " bloques de "
            "calibración; la sede es UNA y no se elige entre dos",
            ruta=ruta, parametro=CLAVE_UMBRAL, bloques=len(bloques),
        )
    return comprobar_umbral(bloques[0].get(CLAVE_UMBRAL), ruta=ruta)


# ===========================================================================
#  talones: la forma de un evento cuyo cuerpo se ha retirado
# ===========================================================================
def es_sellado(evento):
    """¿Es este evento un TALÓN, es decir, un evento cuyo cuerpo ya se retiró?"""
    return isinstance(evento, dict) and isinstance(evento.get(CLAVE_SELLADO), dict)


def cuerpo_retirable(evento):
    """Los campos que el sellado retira: todo lo que no es eslabón ni conservado."""
    return {clave: evento[clave] for clave in evento if clave not in CONSERVADO}


def talon_de(evento):
    """El TALÓN de un evento: su eslabón intacto, lo conservado, y el cuerpo resumido.

    El talón NO recalcula `huella`: la copia. Ver la `DECISIÓN` del docstring de módulo.
    `cuerpo` es el `cid` de lo retirado, de modo que quien conserve una copia del evento
    entero puede demostrar que era ése y no otro; `retirados` nombra lo que se fue, para que
    un lector sepa qué falta en vez de creer que el evento nunca lo tuvo.
    """
    retirado = cuerpo_retirable(evento)
    talon = {clave: evento[clave] for clave in evento if clave in CONSERVADO}
    talon[CLAVE_SELLADO] = {
        "esquema": ESQUEMA_DEL_SELLADO,
        "cuerpo": cid_de_objeto(retirado),
        "retirados": sorted(retirado),
    }
    return talon


def cid_de_los_talones(eventos):
    """El `cid` de la lista ORDENADA de pares `[secuencia, cid del talón ENTERO]`.

    Es el ancla que hace verificable un talón. Lista de pares y no un mapa, por la misma
    razón que `calcular_cid_raiz`: el orden queda en los propios bytes y no confiado a una
    opción del serializador.

    DECISIÓN · el ancla cubre el TALÓN ENTERO, y no tres campos suyos
        La primera versión anclaba `[secuencia, huella, cuerpo]`, que es lo que PARECE
        suficiente: la huella identifica el evento y `cuerpo` identifica lo retirado. No lo
        era, y las pruebas de `T319` lo pusieron ROJO antes de que esto se escribiera. Se
        colaban enteros dos ataques: cambiar un campo CONSERVADO —el `resultado` de un
        talón, que es lo que `_linaje` y `detectar_bifurcacion` recorren— y REPONER un campo
        del cuerpo retirado, inventando un `motivo` que el evento nunca tuvo. Ninguno de los
        dos toca los tres campos anclados, así que ninguno de los dos se veía. Con el `cid`
        del talón ENTERO, cualquier byte que cambie en cualquier talón cambia el ancla.
    """
    pares = [[evento["secuencia"], cid_de_objeto(evento)]
             for evento in eventos if es_sellado(evento)]
    return cid(serializar_canonico(pares))


class InformeSellado:
    """Qué retiró un sellado, y cuánto compactó. Determinista: ni reloj ni pid (`I-g3`).

    Vive aquí y no en `transaccion.py` —donde están los demás informes— porque el sellado no
    es una transacción del estado canónico: no publica revisión, no toca `canonico/` y no
    entra en el linaje. Es una operación SOBRE EL DIARIO, y su informe pertenece al diario.
    """

    def __init__(self, *, umbral, autor, motivo, bytes_antes, bytes_despues,
                 cid_sellados, secuencias=(), evento=None):
        self.umbral = umbral
        self.autor = autor
        self.motivo = motivo
        self.secuencias = list(secuencias)
        self.evento = evento
        self.bytes_antes = bytes_antes
        self.bytes_despues = bytes_despues
        self.cid_sellados = cid_sellados

    @property
    def sellados(self):
        return len(self.secuencias)

    @property
    def bytes_retirados(self):
        return self.bytes_antes - self.bytes_despues

    def a_dict(self):
        return {
            "umbral": self.umbral,
            "autor": self.autor,
            "motivo": self.motivo,
            "sellados": self.sellados,
            "secuencias": list(self.secuencias),
            "evento": self.evento,
            "bytes_antes": self.bytes_antes,
            "bytes_despues": self.bytes_despues,
            "bytes_retirados": self.bytes_retirados,
            "cid_sellados": self.cid_sellados,
        }


class InformeSegmentacion:
    """Qué cerró una rotación del diario, o por qué no cerró nada. Determinista (`I-g3`)."""

    def __init__(self, *, autor, motivo, segmentado, razon="", entrada=None, segmentos=0,
                 bytes_vivo_antes=0, bytes_vivo_despues=0):
        self.autor = autor
        self.motivo = motivo
        self.segmentado = segmentado
        self.razon = razon
        self.entrada = dict(entrada) if entrada else None
        self.segmentos = segmentos
        self.bytes_vivo_antes = bytes_vivo_antes
        self.bytes_vivo_despues = bytes_vivo_despues

    def a_dict(self):
        return {
            "autor": self.autor, "motivo": self.motivo, "segmentado": self.segmentado,
            "razon": self.razon, "entrada": self.entrada, "segmentos": self.segmentos,
            "bytes_vivo_antes": self.bytes_vivo_antes,
            "bytes_vivo_despues": self.bytes_vivo_despues,
        }


class Diario:
    """El diario canónico de un almacén. Append-only y verificable de principio a fin."""

    def __init__(self, ruta):
        self.ruta = ruta
        self.directorio_de_segmentos = os.path.join(os.path.dirname(ruta), DIRECTORIO_DE_SEGMENTOS)
        self.ruta_del_indice = os.path.join(self.directorio_de_segmentos, FICHERO_INDICE)
        # Un segmento cerrado no cambia: se verifica una vez por proceso y por identidad de
        # fichero (inodo, tamaño, mtime) y su lista de líneas se reutiliza. Cambiar el fichero
        # cambia la clave y obliga a verificarlo otra vez.
        self._segmentos_verificados = {}

    # ------------------------------------------------------------------ lectura
    def existe(self):
        return os.path.exists(self.ruta)

    def crear(self):
        """Crea el fichero vacío y sincroniza su directorio: el NOMBRE debe ser durable."""
        asegurar_directorio(os.path.dirname(self.ruta))
        if not os.path.exists(self.ruta):
            try:
                descriptor = os.open(self.ruta, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
            except FileExistsError:
                return
            except OSError as exc:
                raise traducir_error_de_sistema(exc, self.ruta, "crear el diario") from exc
            os.fsync(descriptor)
            os.close(descriptor)

    def _bytes(self):
        if not os.path.exists(self.ruta):
            return b""
        try:
            with open(self.ruta, "rb") as fichero:
                return fichero.read()
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "leer el diario") from exc

    @staticmethod
    def _partir(datos):
        """`(lineas_completas, cola)` de unos bytes de diario. Una línea acaba en `\\n`."""
        if not datos:
            return [], b""
        corte = datos.rfind(b"\n")
        if corte == -1:
            return [], datos
        return datos[: corte + 1].split(b"\n")[:-1], datos[corte + 1:]

    def _leer_indice(self):
        if not os.path.exists(self.ruta_del_indice):
            return []
        try:
            with open(self.ruta_del_indice, "rb") as fichero:
                crudo = fichero.read()
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta_del_indice, "leer el índice de segmentos") from exc
        return interpretar_indice(crudo, ruta=self.ruta_del_indice)

    def _leer_segmento(self, nombre):
        ruta = os.path.join(self.directorio_de_segmentos, nombre)
        try:
            with open(ruta, "rb") as fichero:
                return fichero.read()
        except FileNotFoundError:
            return None
        except OSError as exc:
            raise traducir_error_de_sistema(exc, ruta, "leer un segmento del diario") from exc

    def _lineas_de_segmento(self, entrada):
        """Las líneas de un segmento, verificado UNA vez por identidad de fichero.

        Se cachean las líneas y no las bytes: comparar el vivo con el último segmento se hace
        por el `sha256` del índice, así que retener las bytes duplicaría el historial en memoria.
        """
        ruta = os.path.join(self.directorio_de_segmentos, entrada["fichero"])
        try:
            info = os.stat(ruta)
            clave = (entrada["fichero"], entrada["sha256"], info.st_ino, info.st_size, info.st_mtime_ns)
        except FileNotFoundError:
            clave = None
        if clave is not None and clave in self._segmentos_verificados:
            return self._segmentos_verificados[clave]
        lineas = lineas_de_un_segmento(self._leer_segmento(entrada["fichero"]), entrada, ruta=ruta)
        if clave is not None:
            self._segmentos_verificados[clave] = lineas
        return lineas

    def _huerfanos(self, entradas, vivo):
        """Los ficheros de `segmentos/` que ningún índice nombra, y si son explicables.

        Devuelve `(huerfanos_tolerados, temporales)`. Un huérfano es tolerable sólo si es el
        segmento SIGUIENTE y sus bytes son un prefijo del vivo: es el rastro de una rotación
        cortada tras el paso 1, y no contiene nada que el vivo no tenga. Cualquier otro
        fichero ahí es inexplicable, y por eso FALLO CERRADO.
        """
        if not os.path.isdir(self.directorio_de_segmentos):
            return [], []
        nombrados = {entrada["fichero"] for entrada in entradas}
        siguiente = (entradas[-1]["hasta"] + 1) if entradas else 1
        tolerados, temporales = [], []
        for nombre in sorted(os.listdir(self.directorio_de_segmentos)):
            if nombre == FICHERO_INDICE or nombre in nombrados:
                continue
            ruta = os.path.join(self.directorio_de_segmentos, nombre)
            if nombre.endswith(SUFIJO_TEMPORAL):
                temporales.append(ruta)
                continue
            encaje = PATRON_DE_SEGMENTO.match(nombre)
            datos = self._leer_segmento(nombre) if encaje else None
            # Si desapareció entre el listado y la lectura, lo retiró un escritor al completar
            # una rotación: la firma de `_partes` lo detecta y la lectura se repite.
            if not encaje or int(encaje.group(1)) != siguiente or not datos \
                    or not vivo.startswith(datos):
                raise DiarioCorrupto(
                    "hay en los segmentos del diario un fichero que ningún índice nombra y que "
                    "no es el rastro de una rotación cortada: `" + nombre + "`",
                    ruta=ruta)
            tolerados.append(ruta)
        return tolerados, temporales

    def _firma_de_lectura(self):
        """Lo que cambia si un escritor toca el diario mientras se lee: vivo, índice y listado."""
        def identidad(ruta):
            try:
                info = os.stat(ruta)
            except FileNotFoundError:
                return None
            return (info.st_ino, info.st_size, info.st_mtime_ns)
        try:
            listado = tuple(sorted(os.listdir(self.directorio_de_segmentos)))
        except FileNotFoundError:
            listado = None
        return identidad(self.ruta), identidad(self.ruta_del_indice), listado

    @staticmethod
    def _sigue_estable(antes, despues):
        """¿Lo leído entre las dos firmas es un instante del diario? Un ANEXADO no lo impide.

        Re-revisión independiente, N1 (reproducido): exigir la firma IDÉNTICA hacía repetir la
        lectura ante cualquier anexado, incluso en un diario sin segmentar, y con escritura
        sostenida el lector agotaba los intentos (`ESCRITOR_CONCURRENTE`) sin rotación alguna. Un
        vivo que sólo CRECIÓ —mismo inodo, tamaño no menor— deja leído un prefijo válido, que es
        lo que garantizaba un solo fichero. Sólo se repite si el vivo se sustituyó o encogió
        (vaciado, truncado de la cola) o si cambió el índice o el listado de `segmentos/`.
        """
        vivo_antes, indice_antes, listado_antes = antes
        vivo_despues, indice_despues, listado_despues = despues
        if indice_antes != indice_despues or listado_antes != listado_despues:
            return False
        if vivo_antes is None or vivo_despues is None:
            return vivo_antes == vivo_despues
        return vivo_antes[0] == vivo_despues[0] and vivo_despues[1] >= vivo_antes[1]

    def _partes(self):
        """`(lineas_de_segmentos, lineas_del_vivo, cola, pendiente)`, de una lectura ESTABLE.

        DEFECTO QUE CIERRA (revisión independiente de la segmentación, H3, reproducido con una
        intercalación determinista): leer el vivo y después el índice NO basta cuando entre las
        dos lecturas un escritor anexa y además rota. El lector componía el vivo VIEJO detrás
        del segmento nuevo —contaba eventos dos veces, o daba `DIARIO_CORRUPTO` sobre un almacén
        sano—, o veía un huérfano que ya no era prefijo del vivo que había leído. Ahora se toma
        la firma del vivo, del índice y del listado de `segmentos/` ANTES y DESPUÉS de leer, y si
        algo se sustituyó o encogió se vuelve a leer (`_sigue_estable`: un vivo que sólo creció
        sigue siendo un prefijo válido): el resultado es siempre un instante del diario.
        Un `DIARIO_CORRUPTO` con la firma estable es corrupción de verdad y se propaga.
        """
        for intento in range(INTENTOS_DE_LECTURA_ESTABLE):
            antes = self._firma_de_lectura()
            try:
                resultado = self._partes_una_vez()
            except DiarioCorrupto:
                if not self._sigue_estable(antes, self._firma_de_lectura()):
                    continue
                raise
            if self._sigue_estable(antes, self._firma_de_lectura()):
                return resultado
        raise EscritorConcurrente(
            "el diario cambió durante " + str(INTENTOS_DE_LECTURA_ESTABLE) + " lecturas "
            "seguidas: no se obtuvo una lectura estable. Reintente; si persiste, hay un escritor "
            "que no respeta el bloqueo", ruta=self.ruta)

    def _partes_una_vez(self):
        """El VIVO se lee ANTES que el índice y que el listado; la firma de `_partes` hace el resto."""
        crudo = self._bytes()
        entradas = self._leer_indice()
        segmentos, vivo, pendiente = componer_lineas(crudo, entradas, self._lineas_de_segmento,
                                                     ruta=self.ruta)
        self._huerfanos(entradas, crudo)
        completas, cola = self._partir(vivo)
        return segmentos, completas, cola, pendiente

    def _lineas(self):
        """Devuelve `(lineas_completas, bytes_de_cola_desgarrada)`, de TODO el diario.

        Las completas son las de los segmentos cerrados seguidas de las del vivo; la cola,
        si la hay, sólo puede estar en el vivo, que es el único que se anexa. Una línea es
        completa cuando termina en `\\n`; lo que quede detrás del último salto es un
        anexado que no llegó a terminar.
        """
        segmentos, vivo, cola, _pendiente = self._partes()
        return segmentos + vivo, cola

    def segmentos(self):
        """Las entradas del índice de segmentos, validadas. Lista vacía sin segmentar."""
        return self._leer_indice()

    def cola_desgarrada(self):
        return bool(self._lineas()[1])

    def instantanea(self, *, verificar=True, tolerar_cola=False):
        """UNA sola lectura del diario. Todo lo que se deduzca sale de ELLA y de nada más.

        Defecto que previene, y no es teórico: el diario es APPEND-ONLY y otro proceso
        puede estar anexando justo ahora. Dos llamadas seguidas a `eventos()` devuelven,
        legítimamente, dos listas distintas. Cruzar los resultados de las dos —recorrer una
        y buscar en la otra— produce una conclusión que no corresponde a ningún estado que
        el diario haya tenido nunca, y en el mejor de los casos revienta con un `KeyError`
        crudo; en el peor, decide que no hay ventana cuando la hay.

        La regla es: quien vaya a deducir algo del diario pide UNA instantánea y trabaja
        sobre ella. Un `read()` del fichero entero es un corte coherente por construcción:
        lo que llegue después de ese `read()` no aparece a medias, aparece en la siguiente
        instantánea. Que la conclusión sea de hace un instante es aceptable —`g.3` dice
        expresamente que NO se afirma aislamiento de lecturas—; que sea de dos instantes a
        la vez, no lo es.

        Devuelve `(eventos, bytes_de_cola_desgarrada)`.
        """
        completas, cola = self._lineas()
        if cola and not tolerar_cola:
            raise DiarioCorrupto(
                "el diario termina en una línea incompleta de " + str(len(cola))
                + " byte(s): un anexado quedó a medias. `recuperar()` la descarta bajo el "
                "bloqueo de escritor; leer no la descarta nunca",
                ruta=self.ruta,
                bytes_sueltos=len(cola),
            )
        return self._interpretar(completas, verificar), cola

    def _interpretar(self, completas, verificar):
        """Líneas crudas → eventos, con la cadena comprobada eslabón a eslabón."""
        eventos = []
        anterior = None
        for indice, linea in enumerate(completas):
            evento = deserializar(linea, ruta=self.ruta, error=DiarioCorrupto)
            if not isinstance(evento, dict):
                raise DiarioCorrupto(
                    "la línea " + str(indice + 1) + " del diario no es un objeto JSON",
                    ruta=self.ruta,
                )
            comprobar_esquema(evento, ruta=self.ruta, error=DiarioCorrupto)
            if verificar:
                self._verificar_eslabon(evento, anterior, indice)
            eventos.append(evento)
            anterior = evento
        if verificar:
            self._verificar_sellado(eventos)
        return eventos

    def _verificar_sellado(self, eventos):
        """Los TALONES casan con el ancla del evento de sellado que los explica (`g.7`).

        Se hace DESPUÉS del recorrido eslabón a eslabón y no dentro, porque el ancla es una
        propiedad del diario entero —la lista ordenada de todos los talones— y no de un
        evento contra el anterior. Comprueba las dos mitades de la obligación de `g.7`:

          RETIRAR EXIGE TRANSICIÓN · si hay cuerpos retirados y NO hay ningún evento
            `diario.sellado` que los explique, alguien vació líneas a mano. Es corrupción, y
            se denuncia aunque la cadena de `previo` esté perfecta: precisamente por eso hace
            falta esta comprobación, porque vaciar un cuerpo conservando la huella no rompe
            ningún eslabón.

          LA TRANSICIÓN DICE QUÉ RETIRÓ · el último `diario.sellado` declara el `cid` de la
            lista de talones que había cuando se escribió. Si un talón se edita, se añade o
            se quita después, el `cid` recalculado no casa. Y ese evento se huella y se
            encadena como cualquier otro, así que rehacer el ancla rompe el `previo` del
            siguiente evento.
        """
        talones = [evento for evento in eventos if es_sellado(evento)]
        sellados = [evento for evento in eventos if evento.get("tipo") == TIPO_SELLADO]
        if talones and not sellados:
            raise DiarioCorrupto(
                "hay " + str(len(talones)) + " evento(s) con el cuerpo retirado y ningún "
                "`" + TIPO_SELLADO + "` que lo explique: `g.7` exige que retirar el cuerpo "
                "de un evento sea una transición EXPLÍCITA Y AUDITABLE, y aquí no hay "
                "ninguna",
                ruta=self.ruta, talones=len(talones),
                posicion=talones[0].get("secuencia"),
            )
        if not sellados:
            return
        declarado = sellados[-1].get("cid_sellados")
        reproducido = cid_de_los_talones(eventos)
        if declarado != reproducido:
            raise DiarioCorrupto(
                "el ancla del último `" + TIPO_SELLADO + "` no casa con los talones que hay "
                "en el diario: un evento sellado se editó, se selló uno más a mano o se "
                "repuso el cuerpo de otro después de la transición que lo retiró",
                ruta=self.ruta, posicion=sellados[-1].get("secuencia"),
                esperada=reproducido, encontrada=declarado,
            )

    def eventos(self, desde=0, verificar=True, tolerar_cola=False):
        """Los eventos del diario, verificados de principio a fin.

        Es `instantanea()` para quien sólo quiere la lista. Quien vaya a CRUZAR dos
        deducciones sobre el diario debe pedir la instantánea y pasarla, no llamar aquí
        dos veces.

        `verificar=False` sólo lo usa la propia verificación de integridad para poder
        describir el daño en vez de detenerse en el primer síntoma.
        """
        eventos, _ = self.instantanea(verificar=verificar, tolerar_cola=tolerar_cola)
        if desde:
            eventos = [evento for evento in eventos if evento.get("secuencia", 0) >= desde]
        return eventos

    def _verificar_eslabon(self, evento, anterior, indice):
        esperada = indice + 1
        if evento.get("secuencia") != esperada:
            raise DiarioCorrupto(
                "la secuencia del diario salta: se esperaba " + str(esperada)
                + " y se lee " + str(evento.get("secuencia")),
                ruta=self.ruta,
                posicion=esperada,
            )
        if evento.get("tipo") not in TIPOS:
            raise DiarioCorrupto(
                "tipo de evento no declarado en el §2.4: " + repr(evento.get("tipo")),
                ruta=self.ruta,
                posicion=esperada,
            )
        previo_esperado = anterior[CLAVE_HUELLA] if anterior is not None else None
        if evento.get(CLAVE_PREVIO) != previo_esperado:
            raise DiarioCorrupto(
                "la cadena de hash se rompe en la secuencia " + str(esperada)
                + ": `previo` no es la huella del evento anterior. Falta una línea, se "
                "insertó una, o se editó el diario a mano",
                ruta=self.ruta,
                posicion=esperada,
            )
        if es_sellado(evento):
            # Un TALÓN no recalcula su huella, y no es una excepción cómoda: es que su
            # contenido es exactamente lo que se retiró, y recalcular el `cid` de lo que ya
            # no está no es una comprobación, es una imposibilidad. Lo que sí se exige aquí
            # es que el talón CONSERVE la huella —sin ella el `previo` del siguiente evento
            # no tendría contra qué casar— y que el resumen del sellado tenga forma. Lo que
            # ata el talón a su contenido original es `_verificar_sellado`.
            if not isinstance(evento.get(CLAVE_HUELLA), str):
                raise DiarioCorrupto(
                    "el evento sellado " + str(esperada) + " no conserva su `huella`: el "
                    "sellado retira el CUERPO y nunca el eslabón",
                    ruta=self.ruta, posicion=esperada,
                )
            resumen = evento[CLAVE_SELLADO]
            if not isinstance(resumen.get("cuerpo"), str) \
                    or not isinstance(resumen.get("retirados"), list):
                raise DiarioCorrupto(
                    "el evento sellado " + str(esperada) + " no declara qué se retiró: un "
                    "talón sin `cuerpo` ni `retirados` no dice qué falta",
                    ruta=self.ruta, posicion=esperada,
                )
            return
        huella = calcular_huella(evento)
        if evento.get(CLAVE_HUELLA) != huella:
            raise DiarioCorrupto(
                "la huella del evento " + str(esperada) + " no casa con su contenido: el "
                "evento fue editado después de escribirse",
                ruta=self.ruta,
                posicion=esperada,
                esperada=huella,
                encontrada=evento.get(CLAVE_HUELLA),
            )

    def exigir_coherente(self, hasta_secuencia=None, *, tolerar_cola=False):
        """Fallo CERRADO al LEER si el diario está truncado o roto (`g.5`).

        Distingue DOS daños que se parecen en el fichero y no se parecen en nada más:

          ÚLTIMA LÍNEA TORCIDA · un corte a mitad de `append` deja bytes sin su `\\n`. El
            evento no llegó entero al medio, así que por `g.4` nunca fue durable, y la
            transacción que iba a explicar queda sin cerrar. Es una VENTANA RECUPERABLE:
            `recuperar()`, que tiene el bloqueo de escritor, descarta la cola y cierra la
            ventana. Por eso se tolera cuando se abre con `recuperar=True`.
            Con `recuperar=False` NO se tolera, y la razón es que un lector que no puede
            reparar tampoco puede DISTINGUIR el corte de una truncación deliberada: dar
            por buena la parte legible es exactamente cómo se pierde una transición sin
            que nadie se entere.

          DIARIO QUE NO ALCANZA LA REVISIÓN PUBLICADA · `REVISION.json` declara el
            `diario_secuencia` del evento que la explica. Si el diario ya no llega hasta
            ahí, se han perdido eventos COMPLETOS: hay estado publicado sin diario que lo
            explique, contra `g.13`, y ninguna recuperación puede reconstruirlo sin
            inventar, que es lo que `I-g2` prohíbe. Eso es corrupción SIEMPRE, se abra
            como se abra, y no hay rama de `g.8` que lo arregle.
        """
        completas, cola = self._lineas()
        if cola and not tolerar_cola:
            raise DiarioCorrupto(
                "el diario termina en una línea incompleta de " + str(len(cola))
                + " byte(s); abrir con `recuperar=True` cierra esa ventana, leer no la "
                "cierra nunca",
                ruta=self.ruta, bytes_sueltos=len(cola),
            )
        # Aquí NO se verifica la cadena de huellas, y es deliberado. Esta comprobación es
        # ESTRUCTURAL —¿está el fichero entero?— y se paga en cada apertura, incluidas las
        # de sólo lectura. La cadena responde a otra pregunta —¿lo escribió el motor o lo
        # editó alguien?— y la contestan quienes de verdad leen los eventos: `eventos()`,
        # `verificar_integridad()`, `auditar()`, `recuperar()` y `aplicar()`. Separarlas
        # evita que abrir para mirar la revisión tenga que reconstruir el diario entero, y
        # ninguna corrupción se escapa: nadie usa un evento sin haberlo verificado antes.
        if hasta_secuencia is not None and len(completas) < hasta_secuencia:
            raise DiarioCorrupto(
                "la revisión publicada se explica por el evento " + str(hasta_secuencia)
                + " y el diario sólo llega al " + str(len(completas)) + ": se han perdido "
                "eventos completos, y hay estado publicado que ya nada explica",
                ruta=self.ruta,
                declarada=hasta_secuencia, encontrada=len(completas),
            )
        return len(completas)

    def ultimo(self):
        eventos = self.eventos(tolerar_cola=True)
        return eventos[-1] if eventos else None

    def siguiente_secuencia(self):
        """La secuencia que llevará el próximo evento. Empieza en 1, como el §2.5."""
        completas, _ = self._lineas()
        return len(completas) + 1

    # ----------------------------------------------------------------- escritura
    def reparar_cola(self):
        """Descarta un anexado desgarrado. Sólo se llama con el bloqueo de escritor tomado.

        Devuelve los bytes descartados. Es idempotente: sin cola desgarrada no hace nada y
        no toca el fichero, que es lo que `recuperar()` necesita para poder invocarse N
        veces sin efectos.
        """
        self.completar_rotacion()
        _segmentos, completas, cola, _pendiente = self._partes()
        if not cola:
            return 0
        # Sólo el VIVO: es el único fichero que se anexa y el único que se trunca. Medir la
        # longitud sobre todo el diario cortaría el vivo por un sitio que no es el suyo.
        longitud = sum(len(linea) + 1 for linea in completas)
        try:
            descriptor = os.open(self.ruta, os.O_WRONLY)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "reparar la cola del diario") from exc
        try:
            os.ftruncate(descriptor, longitud)
            os.fsync(descriptor)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "truncar el diario") from exc
        finally:
            os.close(descriptor)
        return len(cola)

    def anexar(self, tipo, **campos):
        """Añade un evento encadenado y lo hace DURABLE antes de devolver.

        El punto `durante-el-diario` cae entre la escritura y el `fsync`: es la ventana en
        la que el evento está en la caché de página y no en el medio. Un corte ahí es el
        caso interesante, porque produce exactamente la cola desgarrada que `reparar_cola`
        tiene que saber descartar.
        """
        if tipo not in TIPOS:
            raise DiarioCorrupto(
                "tipo de evento no declarado en el §2.4: " + repr(tipo), ruta=self.ruta
            )
        # Anexar sobre una rotación cortada tras el índice duplicaría el último segmento en el
        # vivo. Se completa ANTES: es idempotente y se hace bajo el mismo bloqueo de escritor.
        self.completar_rotacion()
        completas, cola = self._lineas()
        if cola:
            raise DiarioCorrupto(
                "no se anexa sobre un diario con la cola desgarrada: primero `recuperar()`",
                ruta=self.ruta,
            )
        previo = None
        if completas:
            ultimo = deserializar(completas[-1], ruta=self.ruta, error=DiarioCorrupto)
            previo = ultimo.get(CLAVE_HUELLA)

        evento = {"esquema": ESQUEMA, "secuencia": len(completas) + 1, "tipo": tipo}
        evento.update(campos)
        evento[CLAVE_PREVIO] = previo
        evento[CLAVE_HUELLA] = calcular_huella(evento)

        linea = serializar_compacto(evento) + b"\n"
        asegurar_directorio(os.path.dirname(self.ruta))
        try:
            descriptor = os.open(self.ruta, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "abrir el diario") from exc
        try:
            escritos = os.write(descriptor, linea)
            if escritos != len(linea):
                # Con `O_APPEND` una escritura corta de un búfer pequeño es anómala. No se
                # completa el resto en un segundo `write`: eso mezclaría la línea con la de
                # otro escritor. Se denuncia, y la cola desgarrada la limpia `recuperar()`.
                raise DiarioCorrupto(
                    "el anexado al diario quedó corto: " + str(escritos) + " de "
                    + str(len(linea)) + " bytes",
                    ruta=self.ruta,
                )
            fallos.punto("durante-el-diario")
            os.fsync(descriptor)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "anexar al diario") from exc
        finally:
            os.close(descriptor)
        return evento

    # ------------------------------------------------------------ segmentación
    def completar_rotacion(self):
        """Termina una rotación que un corte dejó a medias. Idempotente; con el bloqueo tomado.

        Devuelve qué hizo: `vivo_vaciado` si el corte fue tras publicar el índice (el vivo
        tenía las mismas bytes que el último segmento) y los huérfanos o temporales retirados
        si fue antes. Sin rotación a medias no toca nada.
        """
        hecho = {"vivo_vaciado": False, "retirados": []}
        crudo = self._bytes()
        entradas = self._leer_indice()
        _segmentos, _vivo, pendiente = componer_lineas(crudo, entradas, self._lineas_de_segmento,
                                                       ruta=self.ruta)
        if pendiente:
            self._vaciar_vivo()
            hecho["vivo_vaciado"] = True
            crudo = b""
        tolerados, temporales = self._huerfanos(entradas, crudo)
        for ruta in tolerados + temporales:
            if borrar_si_existe(ruta):
                hecho["retirados"].append(os.path.basename(ruta))
        if hecho["retirados"]:
            sincronizar_directorio(self.directorio_de_segmentos)
        return hecho

    def _vaciar_vivo(self):
        temporal = self.ruta + SUFIJO_TEMPORAL
        escribir_y_sincronizar(temporal, b"")
        publicar(temporal, self.ruta)
        sincronizar_directorio(os.path.dirname(self.ruta))

    def rotar(self, *, autor, motivo, umbral_bytes=None):
        """Cierra el diario VIVO entero como segmento y deja uno vacío que continúa la cadena.

        Se llama con el bloqueo de ESCRITOR tomado, como `anexar` y `sellar`. Ninguna línea
        se reescribe: el segmento son las mismas bytes que el vivo tenía. Falla CERRADO si
        hay cola desgarrada o una transacción sin evento terminal —su ventana se recupera
        leyendo el vivo y no se parte entre dos ficheros— y si la transición no se firma.
        Con `umbral_bytes`, no cierra un vivo más pequeño.
        """
        if not isinstance(autor, str) or not autor.strip() \
                or not isinstance(motivo, str) or not motivo.strip():
            raise SegmentacionImposible(
                "cerrar un segmento del diario es una transición EXPLÍCITA Y AUDITABLE: sin "
                "`autor` y sin `motivo` no se sabría quién lo decidió ni por qué",
                ruta=self.ruta)
        self.completar_rotacion()
        segmentos, vivo, cola, _pendiente = self._partes()
        datos = self._bytes()
        entradas = self._leer_indice()
        informe = dict(autor=autor, motivo=motivo, segmentos=len(entradas),
                       bytes_vivo_antes=len(datos), bytes_vivo_despues=len(datos))
        if cola:
            raise SegmentacionImposible(
                "el diario vivo termina en una línea incompleta de " + str(len(cola))
                + " byte(s): primero `recuperar()`, que es quien puede cerrar esa ventana",
                ruta=self.ruta, bytes_sueltos=len(cola))
        if not vivo:
            return InformeSegmentacion(segmentado=False, razon="el diario vivo está vacío",
                                       **informe)
        if umbral_bytes is not None and len(datos) < umbral_bytes:
            return InformeSegmentacion(
                segmentado=False,
                razon="el diario vivo ocupa %d bytes, por debajo del umbral de %d" % (
                    len(datos), umbral_bytes),
                **informe)
        eventos = self._interpretar(segmentos + vivo, True)      # la cadena ENTERA, antes
        if self.transaccion_sin_cerrar(eventos) is not None:
            raise SegmentacionImposible(
                "hay una transacción sin evento terminal: `g.8` la recupera leyendo el diario "
                "vivo, y partirla entre dos ficheros no se hace. Llame a `recuperar()` y "
                "vuelva a segmentar",
                ruta=self.ruta)
        primero, ultimo = eventos[len(segmentos)], eventos[-1]
        entrada = {
            "fichero": nombre_de_segmento(primero["secuencia"], ultimo["secuencia"]),
            "desde": primero["secuencia"], "hasta": ultimo["secuencia"],
            "bytes": len(datos), "sha256": sha256_de(datos),
            "huella_ultima": ultimo[CLAVE_HUELLA], "autor": autor, "motivo": motivo,
        }
        # 1 · el segmento, publicado y durable
        nuevo_directorio = not os.path.isdir(self.directorio_de_segmentos)
        asegurar_directorio(self.directorio_de_segmentos)
        if nuevo_directorio:
            # El NOMBRE de `segmentos/` tiene que ser durable antes de que el índice dependa de
            # él (revisión independiente, H4): se sincroniza `diario/`.
            sincronizar_directorio(os.path.dirname(self.ruta))
        destino = os.path.join(self.directorio_de_segmentos, entrada["fichero"])
        escribir_y_sincronizar(destino + SUFIJO_TEMPORAL, datos)
        publicar(destino + SUFIJO_TEMPORAL, destino)
        sincronizar_directorio(self.directorio_de_segmentos)
        fallos.punto("segmentacion-tras-el-segmento")
        # 2 · el índice que lo nombra: el PUNTO DE NO RETORNO
        indice = {"esquema": ESQUEMA_DEL_INDICE, "segmentos": list(entradas) + [entrada]}
        escribir_y_sincronizar(self.ruta_del_indice + SUFIJO_TEMPORAL,
                               (json.dumps(indice, ensure_ascii=False, sort_keys=True, indent=2)
                                + "\n").encode("utf-8"))
        publicar(self.ruta_del_indice + SUFIJO_TEMPORAL, self.ruta_del_indice)
        sincronizar_directorio(self.directorio_de_segmentos)
        fallos.punto("segmentacion-tras-el-indice")
        # 3 · el vivo, vacío: el siguiente evento encadena con `huella_ultima`
        self._vaciar_vivo()
        informe.update(segmentos=len(indice["segmentos"]), bytes_vivo_despues=self._tamano())
        return InformeSegmentacion(segmentado=True, entrada=entrada, **informe)

    # -------------------------------------------------------------- agregaciones
    def por_transaccion(self, eventos=None):
        """Mapa `transaccion -> [eventos]`, en orden. Base de la detección de la ventana.

        Sin `eventos` lee el diario una vez. Si el llamador va a usar el mapa JUNTO a otro
        recorrido, tiene que pasar su propia instantánea: dos lecturas producen dos mapas y
        cruzarlos es el defecto que `instantanea()` existe para impedir.
        """
        if eventos is None:
            eventos, _ = self.instantanea(tolerar_cola=True)
        agrupados = {}
        for evento in eventos:
            transaccion = evento.get("transaccion")
            if transaccion is None:
                continue
            agrupados.setdefault(transaccion, []).append(evento)
        return agrupados

    def transaccion_sin_cerrar(self, eventos=None):
        """La última transacción abierta o preparada SIN evento terminal, o `None`.

        Se recorre de atrás hacia delante porque el §3 habla de «la última». Como el
        protocolo sólo permite una transacción viva a la vez —el bloqueo de escritor lo
        garantiza—, en la práctica hay como mucho una; recorrer entero y quedarse con la
        última hace que un almacén con historia anómala se comporte igual de bien.

        UNA sola lectura, y las dos deducciones —la agrupación y el recorrido— salen de
        ella. Antes eran dos: se agrupaba sobre una lectura y se recorría sobre otra, y con
        varios escritores anexando en paralelo la transacción elegida en el recorrido podía
        no existir en la agrupación. Eso reventaba con un `KeyError` CRUDO, sin código
        estable, en la ruta de recuperación al abrir —la que más falta hace que aguante— y
        volcando además un traceback con rutas absolutas de la máquina. El §0 no admite
        ninguna de las tres cosas.
        """
        if eventos is None:
            # `tolerar_cola=True` a propósito: un anexado a medias ES una ventana, y
            # preguntar si la hay tiene que poder responderse justo cuando la hay.
            eventos, _ = self.instantanea(tolerar_cola=True)
        agrupados = self.por_transaccion(eventos)
        candidata = None
        for evento in eventos:
            transaccion = evento.get("transaccion")
            if transaccion is None or evento.get("tipo") not in (
                "transicion.abierta", "transicion.preparada"
            ):
                continue
            tipos = {suceso.get("tipo") for suceso in agrupados.get(transaccion, ())}
            if tipos.isdisjoint(TERMINALES):
                candidata = transaccion
        if candidata is None:
            return None
        propios = agrupados.get(candidata)
        if not propios:
            # Imposible con una instantánea coherente: `candidata` sale del mismo recorrido
            # que alimentó la agrupación. Sólo se llega aquí si el llamador pasó una lista
            # que no es una lectura coherente del diario. Se falla CERRADO y TIPADO, con
            # código estable, en vez de dejar escapar el `KeyError` que el §0 prohíbe.
            raise DiarioCorrupto(
                "la transacción " + str(candidata) + " aparece al recorrer el diario y no "
                "al agruparlo: la lista de eventos recibida no es una lectura coherente. "
                "Pida una `instantanea()` y trabaje sobre ella",
                ruta=self.ruta, transaccion=candidata,
            )
        return candidata, propios

    # ------------------------------------------------------------- sellado (`g.7`)
    def _transacciones_cerradas(self, eventos):
        """`(cerradas, marcadas)` — qué transacciones ya no pueden estar en su ventana.

        Una transacción está CERRADA cuando tiene un evento terminal. Es exactamente el
        criterio de `transaccion_sin_cerrar`, y se deduce de la MISMA instantánea: preguntar
        dos veces al diario si una transacción sigue viva es cómo se acaba sellando la que
        todavía lo estaba.
        """
        cerradas, marcadas = set(), set()
        for transaccion, propios in self.por_transaccion(eventos).items():
            tipos = {evento.get("tipo") for evento in propios}
            if not tipos.isdisjoint(TERMINALES):
                cerradas.add(transaccion)
            if "transicion.marcada" in tipos:
                marcadas.add(transaccion)
        return cerradas, marcadas

    def motivo_de_no_sellar(self, evento, eventos, *, cerradas=None, marcadas=None):
        """POR QUÉ este evento no se puede sellar, o `""` si sí se puede.

        Devuelve el motivo en vez de un booleano para que el fallo de una retirada DIRIGIDA
        pueda nombrar la razón concreta: «la recuperación todavía lo necesita» y «la
        auditoría lo reproyecta» mandan a sitios distintos, y un `False` no distingue.
        """
        if cerradas is None or marcadas is None:
            cerradas, marcadas = self._transacciones_cerradas(eventos)
        if es_sellado(evento):
            return "su cuerpo ya se retiró en un sellado anterior"
        tipo = evento.get("tipo")
        if tipo in NO_SELLABLES:
            return ("`" + str(tipo) + "` no se sella nunca: la recuperación de `g.8` o la "
                    "auditoría de `g.13` leen su cuerpo entero")
        transaccion = evento.get("transaccion")
        if transaccion is not None:
            if transaccion not in cerradas:
                return ("la transacción `" + str(transaccion) + "` no tiene evento "
                        "terminal: todavía puede estar en su ventana, y `g.8` la recupera "
                        "leyendo este cuerpo")
            if transaccion in marcadas:
                return ("la transacción `" + str(transaccion) + "` está MARCADA y su salida "
                        "la decide la autoridad: su cuerpo sigue siendo prueba viva")
        return ""

    def sellables(self, eventos, *, umbral=None, secuencia_publicada=None):
        """Las secuencias cuyo cuerpo se puede retirar, en orden.

        `umbral` acota la COLA que se deja intacta: los últimos `umbral` eventos no se tocan
        aunque fueran admisibles. Con `umbral=None` no hay cola reservada, y es el modo de la
        retirada DIRIGIDA, que no es una compactación periódica sino un acto de autoridad
        sobre un evento concreto.
        """
        cerradas, marcadas = self._transacciones_cerradas(eventos)
        tope = len(eventos) if umbral is None else max(0, len(eventos) - umbral)
        elegidos = []
        for indice, evento in enumerate(eventos):
            if indice >= tope:
                break
            if secuencia_publicada is not None \
                    and evento.get("secuencia") == secuencia_publicada:
                # El evento que `REVISION.json` declara que la explica se deja entero
                # aunque las demás reglas lo permitieran. Hoy es siempre una
                # `transicion.preparada` —y ésas no se sellan nunca—, así que esta guarda
                # no cambia ninguna decisión: existe para que siga sin cambiarla el día
                # que la revisión cite otro evento.
                continue
            if self.motivo_de_no_sellar(evento, eventos, cerradas=cerradas,
                                        marcadas=marcadas):
                continue
            elegidos.append(evento["secuencia"])
        return elegidos

    def sellar(self, *, autor, motivo, umbral, secuencia_publicada=None):
        """Compacta el diario retirando el CUERPO de lo que ya no se necesita entero (`g.7`).

        Se llama con el bloqueo de ESCRITOR tomado, y no se comprueba aquí que lo esté por la
        misma razón que `anexar` tampoco lo comprueba: el bloqueo es del motor, que es el
        único ejecutor de mutaciones (`I-g4`).
        """
        comprobar_umbral(umbral)
        eventos = self._exigir_diario_sellable()
        secuencias = self.sellables(eventos, umbral=umbral,
                                    secuencia_publicada=secuencia_publicada)
        return self._retirar(eventos, secuencias, autor=autor, motivo=motivo, umbral=umbral)

    def retirar_cuerpo(self, secuencias, *, autor, motivo):
        """Retira el cuerpo de eventos CONCRETOS. Un acto de autoridad, no una compactación.

        Es la mitad de `g.7` que dice «retirar el cuerpo de un evento sellado exige una
        transición explícita y auditable»: aquí la transición se firma con `autor` y
        `motivo`, deja su propio evento en el diario y falla CERRADO si el cuerpo que se pide
        retirar todavía lo necesitan la recuperación o la auditoría.
        """
        eventos = self._exigir_diario_sellable()
        por_secuencia = {evento["secuencia"]: evento for evento in eventos}
        pedidas = []
        for secuencia in secuencias:
            if not isinstance(secuencia, int) or isinstance(secuencia, bool):
                raise RetiradaNoAdmisible(
                    "la secuencia a retirar es un entero; se recibió "
                    + type(secuencia).__name__,
                    ruta=self.ruta,
                )
            evento = por_secuencia.get(secuencia)
            if evento is None:
                raise RetiradaNoAdmisible(
                    "el diario no tiene ningún evento con la secuencia " + str(secuencia),
                    ruta=self.ruta, posicion=secuencia,
                )
            impedimento = self.motivo_de_no_sellar(evento, eventos)
            if impedimento:
                raise RetiradaNoAdmisible(
                    "no se puede retirar el cuerpo del evento " + str(secuencia) + ": "
                    + impedimento,
                    ruta=self.ruta, posicion=secuencia, tipo=str(evento.get("tipo")),
                )
            pedidas.append(secuencia)
        return self._retirar(eventos, pedidas, autor=autor, motivo=motivo, umbral=None)

    def _exigir_diario_sellable(self):
        """La instantánea sobre la que se sella, o el fallo cerrado que lo impide.

        Se VERIFICA la cadena antes de tocar nada. Sellar un diario que ya está roto
        congelaría el daño detrás de un talón y lo haría irreconstruible: la comprobación no
        es una cortesía, es lo que impide convertir una corrupción detectable en una
        definitiva.
        """
        # Revisión independiente, H1 (reproducido): un corte tras el paso 1 deja un huérfano,
        # y sellar sobre él reescribía el vivo, dejaba de ser su prefijo y el almacén quedaba
        # DIARIO_CORRUPTO para siempre. Se completa la rotación cortada ANTES de nada.
        self.completar_rotacion()
        if self._leer_indice():
            raise SelladoImposible(
                "el diario está SEGMENTADO: los segmentos cerrados son inmutables y el sellado "
                "reescribiría el diario entero dentro del vivo. Sellar un diario segmentado no "
                "está definido, y por eso no se hace",
                ruta=self.ruta,
            )
        completas, cola = self._lineas()
        if cola:
            raise SelladoImposible(
                "el diario termina en una línea incompleta de " + str(len(cola))
                + " byte(s): hay una transacción en su ventana. Primero `recuperar()`, que "
                "es quien puede cerrarla; sellar ahora retiraría cuerpos que `g.8` todavía "
                "necesita",
                ruta=self.ruta, bytes_sueltos=len(cola),
            )
        return self._interpretar(completas, True)

    def _retirar(self, eventos, secuencias, *, autor, motivo, umbral):
        """El acto material: reescribe el diario con los talones y anexa su transición.

        DECISIÓN · el diario sellado se PUBLICA con `os.replace`, no se edita en su sitio
            Alternativas: (a) truncar y reescribir sobre el mismo descriptor; (b) componer el
            fichero entero al lado y publicarlo con el intercambio de nombre atómico.
            Se elige (b), que es la misma primitiva del §2 para `REVISION.json` y por la
            misma razón: con (a) un corte a mitad de reescritura deja un diario a medias, sin
            cola desgarrada que lo delate —los bytes cortados están EN MEDIO— y por tanto sin
            reparación posible. Con (b) el corte deja el diario ANTERIOR intacto: sellar es
            entonces una operación que, o se ve entera, o no se ve, igual que una transición.
        """
        if not isinstance(autor, str) or not autor.strip() \
                or not isinstance(motivo, str) or not motivo.strip():
            raise RetiradaSinTransicion(
                "retirar el cuerpo de un evento del diario exige una transición EXPLÍCITA Y "
                "AUDITABLE (`g.7`), y una transición sin `autor` y sin `motivo` no es "
                "auditable: se sabría qué se retiró y no quién lo decidió ni por qué",
                ruta=self.ruta,
            )
        secuencias = sorted(set(secuencias))
        if not secuencias:
            # No se anexa un evento de sellado que no retira nada: sería una línea que no
            # explica ningún cambio, que es justo lo que `Transicion.validar` prohíbe para
            # el estado canónico y no hay motivo para admitir aquí.
            return InformeSellado(
                umbral=umbral, autor=autor, motivo=motivo,
                bytes_antes=self._tamano(), bytes_despues=self._tamano(),
                cid_sellados=cid_de_los_talones(eventos),
            )

        antes = self._tamano()
        pendientes = set(secuencias)
        nuevos = [talon_de(evento) if evento["secuencia"] in pendientes else evento
                  for evento in eventos]
        sellado = {
            "esquema": ESQUEMA, "secuencia": len(nuevos) + 1, "tipo": TIPO_SELLADO,
            "autor": autor, "motivo": motivo,
            "umbral": umbral,
            "desde": secuencias[0], "hasta": secuencias[-1],
            "sellados": len(secuencias),
            "cid_sellados": cid_de_los_talones(nuevos),
        }
        sellado[CLAVE_PREVIO] = nuevos[-1][CLAVE_HUELLA] if nuevos else None
        sellado[CLAVE_HUELLA] = calcular_huella(sellado)
        nuevos.append(sellado)

        datos = b"".join(serializar_compacto(evento) + b"\n" for evento in nuevos)
        temporal = self.ruta + SUFIJO_TEMPORAL
        asegurar_directorio(os.path.dirname(self.ruta))
        escribir_y_sincronizar(temporal, datos)
        fallos.punto("durante-el-diario")
        publicar(temporal, self.ruta)
        sincronizar_directorio(os.path.dirname(self.ruta))
        return InformeSellado(
            umbral=umbral, autor=autor, motivo=motivo,
            secuencias=secuencias, evento=sellado["secuencia"],
            bytes_antes=antes, bytes_despues=self._tamano(),
            cid_sellados=sellado["cid_sellados"],
        )

    def _tamano(self):
        try:
            return os.path.getsize(self.ruta)
        except FileNotFoundError:
            return 0
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "medir el diario") from exc
