#!/usr/bin/env python3
"""estado_util — la ÚNICA forma en que este paquete escribe en el estado durable.

Dos cosas viven aquí, y viven juntas por la misma razón: ésta es la PUERTA. Una es el
reintento por revisión obsoleta —el motivo original del módulo—. La otra es la INVARIANTE
de `b.12` sobre la prioridad, que se interpone justo antes de confirmar.

No hay aquí ningún estado. Hay una función, y su razón de existir es que el motor aplica
cada transición con **comparación e intercambio** sobre la revisión base: con dos
instancias reales trabajando a la vez sobre el mismo almacén, la que llega segunda recibe
`RevisionObsoleta` aunque su intención sea legítima y toque otro paquete. Sin tratarlo, dos
dispatchers no pueden coexistir.

DECISIÓN · se reintenta la CONSTRUCCIÓN, no la transición ya construida
    Alternativas: (a) releer la revisión y reaplicar la MISMA `Transicion` con la base
    nueva; (b) volver a llamar a una función que reconstruye la transición sobre la
    revisión RELEÍDA.
    Se elige (b). Con (a) el CAS se convierte en «el último gana», que es exactamente lo
    que `g.6` prohíbe: la guarda —¿sigo siendo el titular del lease? ¿el paquete sigue en
    el estado que esperaba? ¿el acuse del efecto ya existe?— se habría evaluado contra un
    estado que ya no es el vigente, y se publicaría una decisión tomada sobre bytes
    caducados. Con (b) la guarda se reevalúa en cada vuelta contra el estado nuevo y, si
    resulta que se perdió el lease, sale `AutoridadPerdida` y NO se reintenta.

DECISIÓN · `construir` puede devolver `None`, y eso NO es un fallo
    Es la forma de decir «al releer, ya no hay nada que escribir»: el acuse del efecto
    apareció, otro cerró el paquete, la observación ya estaba anotada. Levantar una
    excepción para eso obligaría a que cada llamador la capturase, y capturar excepciones
    para expresar un camino normal es la vía por la que acaba apareciendo un
    `except Exception`. Devolver `None` deja el camino normal explícito.

DECISIÓN · agotar las vueltas es `RuntimeInconsistente`, no un reintento infinito
    Un reintento sin tope es un livelock, y §7.3 de `11-ARQ` ya fijó el precedente contra
    él. Perder la carrera DOCE veces seguidas describe una contención que ninguna política
    del contrato contempla, y el §4.2 reserva para eso el fallo cerrado. Agotar las vueltas
    NO toca el estado canónico: cada vuelta que perdió lo perdió por la comparación de la
    revisión, que es anterior a cualquier escritura.

DECISIÓN · `intentos_de_bloqueo` alto y no el 3 por defecto del motor
    El `flock` del motor se reintenta con espera fija de 50 ms. Con el valor 3 por defecto,
    dos dispatchers reales compitiendo agotarían los reintentos en 150 ms y el motor
    abriría un registro de reconciliación por CONTENCIÓN, no por un trabajo fallido: `g.9`
    se llenaría de pendencias que no describen nada. Con `INTENTOS_DE_BLOQUEO` la
    serialización tiene margen para ocurrir, que es lo que `g.6` pide —serializar—, y el
    registro auxiliar sigue reservado a lo que de verdad agota.

DECISIÓN · la PROHIBICIÓN de `b.12` sobre la prioridad se ejecuta AQUÍ, y no en `construir`
    `G-04` del cierre final de `F6`. `b.12` es terminante y el árbol la cita LITERAL en tres
    sedes —`ciclo/planificacion.py`, `runtime/vistas.py`, el docstring de
    `politica.clave_de_orden`—: «DSP informa de la inanición. **No cambia la prioridad.
    Nunca**». Estaba escrita en prosa y sólo en prosa. La reproducción del revisor 1 lo
    midió: añadir `nuevo["prioridad"] = int(actual["prioridad"]) + 10` al `construir` de la
    transición `runtime.seleccion.postergada` pasaba DOCE baterías con `EXIT=0`, con la
    línea ejecutándose dieciséis veces y mutando el estado DURABLE 50 -> 60 -> 70. La única
    afirmación ABSOLUTA del contrato era la única sin red.

    Alternativas para ponerle red: (a) una comprobación dentro del propio
    `_anotar_postergacion`; (b) una prueba más en la batería de selección; (c) una
    invariante en la PUERTA por la que toda transición pasa antes de confirmarse.

    Se elige (c), y (a) y (b) se descartan por lo mismo: no cierran la clase, cierran el
    caso. Una comprobación dentro de `construir` la esquiva quien escriba OTRA transición
    —basta con mover la línea a `_abrir_intento`, a `_marcar_ejecutando` o a una transición
    que todavía no existe—, y una prueba que mire el resultado de una postergación no ve la
    mutación que ocurre dentro de una transición de otra clase. Aquí, en cambio, no hay
    nada que esquivar: `aplicar_con_reintento` es la única forma en que el dispatcher y el
    ciclo escriben —lo declaran los dos módulos y lo comprueba una prueba—, así que una
    transición que mueva la prioridad no llega a `almacen.aplicar` venga de donde venga.

    La invariante no es «no subir la prioridad al postergar»: es que la prioridad de un
    paquete que YA EXISTE no cambia en ninguna transición del runtime. Es más fuerte que la
    prohibición literal y es la forma correcta de escribirla, porque la prohibición literal
    —«no la cambies COMO RESPUESTA a la inanición»— obligaría a leer la INTENCIÓN de quien
    escribe, y una invariante que dependa de la intención no es ejecutable. La prioridad la
    declara el Owner al dar de alta el paquete: ahí NACE, y en ninguna otra parte se mueve.
    La información de inanición vive donde `b.12` la puso —`tiempo_listo`,
    `postergaciones`, `adelantado_por` e `impedimento`— y esos cuatro campos siguen siendo
    escribibles, que es justo lo que separa «informar» de «cambiar».

DECISIÓN · el ALTA es la excepción, y se distingue por el ESTADO, no por el tipo de transición
    Alternativas: (a) eximir la transición `runtime.paquete.creado` por su tipo; (b) eximir
    toda escritura sobre una ruta que NO existía en la revisión leída.
    Se elige (b). Con (a) la exención sería una cadena de texto, y quien quisiera mover la
    prioridad sólo tendría que bautizar su transición `runtime.paquete.creado`; la
    invariante se esquivaría con un literal. Con (b) la exención es un HECHO del estado
    canónico —la ruta no estaba—, y `crear_paquete` ya se niega a sobrescribir un paquete
    existente, de modo que no hay forma de «crear» dos veces para colar una prioridad nueva.

DECISIÓN · además de la función, un ALMACÉN VIGILADO, porque `rt.almacen` es público
    `Runtime.almacen` es una propiedad pública —«se expone porque la verdad vive ahí y no
    aquí»— y con ella se puede construir una `Transicion` a mano y aplicarla sin pasar por
    `aplicar_con_reintento`. Eso es una EDICIÓN DIRECTA, y `G-04` la nombra entre los casos
    que tienen que caer. `AlmacenVigilado` envuelve el almacén que el runtime abre e
    interpone la misma invariante en `aplicar`, delegando todo lo demás: la puerta deja de
    depender de que el llamador use la función correcta.
    LO QUE ESTA ENVOLTURA NO ALCANZA, dicho para que no se crea más de lo que hay: un
    proceso que abra su PROPIO `estado.Almacen` sobre el mismo control repo escribe por el
    motor y no por el runtime. Cerrar también ese camino es una línea en
    `estado/motor.py::Almacen.aplicar`, que es de otro propietario; queda como PETICIÓN.
"""
from __future__ import annotations

from estado.errores import RevisionObsoleta, RutaInvalida
from estado.transaccion import Escritura

from .errores import PrioridadInmutable, RuntimeInconsistente
from .modelo import DOMINIO_PAQUETES

# Vueltas de reconstrucción ante `RevisionObsoleta`. DOCE, y no cinco, porque el reintento
# no es «esperar»: es volver a leer y volver a decidir. Con dos instancias reales cada
# despacho publica media docena de revisiones, así que perder la carrera varias veces
# seguidas es normal y no describe ninguna anomalía. El tope existe para que un livelock
# sea imposible, no para acortar la contención: agotarlo es `RuntimeInconsistente`, y con
# cinco vueltas ese fallo cerrado se dispararía por tráfico corriente en vez de por un
# defecto, que es la peor clase de alarma —la que se aprende a ignorar—.
VUELTAS_POR_REVISION_OBSOLETA = 12

# Pasadas no bloqueantes sobre el `flock` de escritor del motor, a 50 ms cada una: 4 s.
INTENTOS_DE_BLOQUEO = 80

# ===========================================================================
#  LA INVARIANTE DE `b.12` · la prioridad de un paquete existente NO se mueve
# ===========================================================================
# Los campos del objeto durable de un paquete que, una vez escrito el alta, NINGUNA
# transición del runtime puede mover. Es una TUPLA y no un `if` sobre `"prioridad"` porque
# la lista es del contrato y puede crecer: `b.12` fija hoy uno, y el día que fije otro se
# añade aquí y las pruebas de `T400`-`T419` lo recorren sin reescribirse.
CAMPOS_INMUTABLES_DEL_PAQUETE = ("prioridad",)

# La cita, LITERAL, para que el error diga la norma y no una paráfrasis de la norma. Es la
# misma que `ciclo/planificacion.py`, `runtime/vistas.py` y `politica.clave_de_orden`
# transcriben, y por eso `T414` puede confrontar las cuatro sedes entre sí.
CITA_DE_B12 = "DSP informa de la inanición. No cambia la prioridad. Nunca"


def es_ruta_de_paquete(ruta):
    """¿Esa ruta lógica es la de un paquete? Se decide por el DOMINIO, no por el texto."""
    return isinstance(ruta, str) and ruta.startswith(DOMINIO_PAQUETES + "/")


def _vigente(almacen, ruta):
    """El objeto que hoy vive en esa ruta lógica, o `None` si la ruta no existe todavía."""
    try:
        return almacen.leer(ruta)
    except RutaInvalida:
        # La ruta no está en la revisión vigente. Para la invariante eso es un ALTA, y un
        # alta es donde la prioridad NACE: no hay valor anterior que se pueda mover.
        return None


def exigir_inmutables_del_paquete(almacen, transicion):
    """Rechaza, ANTES de confirmar, toda transición que mueva un campo inmutable.

    Se llama con la transición ya construida y con el almacén sobre el que se va a aplicar.
    Lee el estado canónico VIGENTE —no la copia que el llamador tenga en memoria— porque la
    pregunta es «¿este cambio mueve lo que hoy está escrito?», y la única respuesta que vale
    es la del estado, que es la fuente de verdad del §7.1.

    Devuelve la transición para que se pueda encadenar. Levanta `PrioridadInmutable`, que
    NO se reintenta: no es una carrera, es una prohibición.
    """
    for operacion in getattr(transicion, "operaciones", ()) or ():
        if not isinstance(operacion, Escritura) or not es_ruta_de_paquete(operacion.ruta):
            continue
        anterior = _vigente(almacen, operacion.ruta)
        if anterior is None:
            continue
        contenido = operacion.contenido
        for campo in CAMPOS_INMUTABLES_DEL_PAQUETE:
            if campo not in anterior or campo not in contenido:
                # Un objeto al que le falta el campo lo rechaza `comprobar_paquete`, que es
                # de quien es esa responsabilidad. Aquí sólo se compara lo comparable: si
                # esta rama se tragara el caso, el fallo saldría igual, y por el error que
                # de verdad lo describe.
                continue
            if contenido[campo] == anterior[campo]:
                continue
            raise PrioridadInmutable(
                "la transición `" + str(getattr(transicion, "tipo", "?")) + "` mueve el "
                "campo `" + campo + "` del paquete de " + repr(anterior[campo]) + " a "
                + repr(contenido[campo]) + ", y `b.12` lo prohíbe con estas palabras: «"
                + CITA_DE_B12 + "». La prioridad la declara el Owner al dar de alta el "
                "paquete y no se mueve después; la inanición se INFORMA en `tiempo_listo`, "
                "`postergaciones`, `adelantado_por` e `impedimento`",
                ruta=operacion.ruta,
                campo=campo,
                transicion=str(getattr(transicion, "tipo", "?")),
                anterior=anterior[campo],
                pretendido=contenido[campo],
            )
    return transicion


class AlmacenVigilado:
    """El `Almacen` del motor con la invariante de `b.12` interpuesta en `aplicar`.

    Delega TODO lo demás por `__getattr__`: no reimplementa nada del motor, no guarda
    estado y no cambia ningún comportamiento salvo el rechazo. Lo envuelve el `Runtime` al
    abrir, de modo que `rt.almacen` —que es público— tampoco es una vía para mover la
    prioridad con una `Transicion` escrita a mano.
    """

    def __init__(self, almacen):
        # `object.__setattr__` no hace falta: no se intercepta la escritura de atributos, y
        # el único atributo propio es el envuelto. Se nombra con guión bajo para que
        # `__getattr__` no lo busque en el delegado.
        self._almacen = almacen

    @property
    def envuelto(self):
        """El `Almacen` de verdad. Se expone para que nadie tenga que adivinar cuál es."""
        return self._almacen

    def aplicar(self, transicion, **resto):
        exigir_inmutables_del_paquete(self._almacen, transicion)
        return self._almacen.aplicar(transicion, **resto)

    def __getattr__(self, nombre):
        # La guarda no es paranoia: `__getattr__` sólo se llama cuando la búsqueda normal
        # falla, y si `__init__` no llegó a fijar `_almacen` —una excepción en medio— la
        # búsqueda de `_almacen` fallaría y volvería aquí, en recursión infinita. Un
        # `AttributeError` explícito dice qué pasó; una recursión dice `RecursionError`.
        if nombre == "_almacen":
            raise AttributeError(
                "`AlmacenVigilado` no llegó a envolver ningún almacén")
        return getattr(self._almacen, nombre)

    def __enter__(self):
        self._almacen.__enter__()
        return self

    def __exit__(self, tipo, valor, traza):
        return self._almacen.__exit__(tipo, valor, traza)

    def __repr__(self):
        return "AlmacenVigilado(" + repr(self._almacen) + ")"


def aplicar_con_reintento(almacen, construir, *,
                          intentos=VUELTAS_POR_REVISION_OBSOLETA,
                          intentos_de_bloqueo=INTENTOS_DE_BLOQUEO,
                          descripcion="transición del runtime"):
    """Aplica una transición como FUNCIÓN de la revisión leída.

    `construir(revision)` recibe el `dict` de `REVISION.json` recién leído y DEVUELVE la
    `Transicion` a aplicar, o `None` si al releer ya no hay nada que escribir. Se vuelve a
    llamar en cada vuelta, sobre la revisión RELEÍDA: es ahí donde el llamador reevalúa su
    guarda. Cualquier error tipado que `construir` levante sale sin reintento, porque una
    guarda que falla no mejora repitiéndola.
    """
    ultima = None
    for _vuelta in range(max(1, int(intentos))):
        revision = almacen.revision()
        transicion = construir(revision)
        if transicion is None:
            return None
        # LA PUERTA. Se comprueba aquí y no dentro de cada `construir` porque `construir`
        # lo escribe quien añade una transición, y una invariante que dependa de que cada
        # autor se acuerde no es una invariante. Va DENTRO del bucle, sobre la transición
        # RECONSTRUIDA, porque cada vuelta se construye contra un estado distinto.
        exigir_inmutables_del_paquete(almacen, transicion)
        try:
            return almacen.aplicar(transicion, intentos=intentos_de_bloqueo)
        except RevisionObsoleta as exc:
            # Otro escritor publicó entre la lectura y la escritura. No se reaplica lo ya
            # construido: se vuelve arriba, se relee y se reevalúa la guarda.
            ultima = exc
            continue
    raise RuntimeInconsistente(
        "la revisión cambió bajo los pies en las " + str(intentos) + " vueltas concedidas "
        "a «" + descripcion + "»; el estado canónico no se ha tocado",
        vueltas=int(intentos),
        vigente=ultima.contexto.get("vigente") if ultima is not None else None,
    )
