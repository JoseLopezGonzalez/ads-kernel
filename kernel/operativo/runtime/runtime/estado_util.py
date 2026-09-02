#!/usr/bin/env python3
"""estado_util — la ÚNICA forma en que este paquete escribe en el estado durable.

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
"""
from __future__ import annotations

from estado.errores import RevisionObsoleta

from .errores import RuntimeInconsistente

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
