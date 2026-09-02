#!/usr/bin/env python3
"""fallos — puntos de fallo controlados del RUNTIME, para que la recuperación se DEMUESTRE.

Mismo mecanismo que `estado/fallos.py` y por las mismas razones, con otra variable de
entorno y otro censo: los nueve puntos del §4.2 del contrato del corte 2. Se repite el
mecanismo en vez de importarlo a propósito, y conviene decir por qué:

DECISIÓN · variable PROPIA (`ADS_RUNTIME_FALLO`), y no reutilizar `ADS_ESTADO_FALLO`
    Alternativas: (a) una sola variable con los dieciocho puntos; (b) una por capa.
    Se elige (b). Con (a), una prueba del runtime que exportara la variable haría que el
    motor muriese en SU punto homónimo más cercano, y la evidencia diría «cayó en el
    runtime» cuando cayó dentro de `aplicar`. Peor: los dos censos crecerían juntos y un
    nombre nuevo en una capa podría colisionar con el de la otra. Dos variables mantienen
    separadas las dos superficies de corte, que es lo que permite afirmar DÓNDE cayó.

DECISIÓN · `os._exit(70)`, exactamente como el motor
    `sys.exit()` levanta `SystemExit`: correrían los `finally`, se liberarían los `flock`,
    se cerrarían los ficheros y se vaciarían los búferes. Es decir, se demostraría una
    recuperación tras un cierre ORDENADO, que es justo el caso que nunca hace falta
    recuperar. `os._exit` no ejecuta nada de eso: el `flock` lo suelta el núcleo al morir
    el proceso, que es lo que de verdad ocurre en un corte. 70 es `EX_SOFTWARE`, elegido
    por no colisionar con 0, 1 y 2, que la CLI reserva.

DECISIÓN · un punto desconocido es un FALLO, no un silencio
    Idéntica a la del motor, y por la misma razón: con `ADS_RUNTIME_FALLO=antes-del-acuse`
    —el nombre a medias de `despues-del-efecto-antes-del-acuse`— una prueba pasaría en
    verde sin haber inyectado corte alguno, y estaríamos publicando como evidencia de
    idempotencia una ejecución en la que nunca hubo caída.

Sin la variable exportada este módulo no hace nada: ni lee ficheros, ni escribe, ni importa
nada caro. Viaja dentro del runtime de producción.
"""
from __future__ import annotations

import os
import sys

from .errores import ErrorDeRuntime

VARIABLE = "ADS_RUNTIME_FALLO"

# El orden es el del §4.2 del contrato, que es el orden en que `despachar` los atraviesa.
# No se ordena alfabéticamente a propósito: leer esta tupla de arriba abajo es leer el
# ciclo de despacho.
PUNTOS = (
    "antes-de-adquirir",
    "despues-de-adquirir",
    "antes-de-ejecutar",
    "durante-la-ejecucion",
    "despues-del-efecto-antes-del-acuse",
    "despues-del-acuse-antes-de-liberar",
    "antes-de-reintentar",
    "antes-de-agotar",
    "antes-de-liberar",
)

CODIGO_DE_SALIDA = 70


def puntos():
    """Los nueve puntos declarados, en el orden del §4.2."""
    return list(PUNTOS)


def activo():
    """El punto pedido por el entorno, o `None`. Valida el nombre: no adivina."""
    nombre = os.environ.get(VARIABLE)
    if not nombre:
        return None
    if nombre not in PUNTOS:
        raise ErrorDeRuntime(
            "el punto de fallo pedido no está declarado en el §4.2; puntos válidos: "
            + ", ".join(PUNTOS),
            codigo="PUNTO_DE_FALLO_DESCONOCIDO",
            punto=nombre,
        )
    return nombre


def punto(nombre):
    """Frontera del ciclo de despacho. Si el entorno la nombra, el proceso muere AQUÍ.

    `nombre` se comprueba contra `PUNTOS` aunque el entorno no pida nada: una llamada con
    un nombre inventado es un defecto del runtime, y descubrirlo sólo cuando alguien
    exporta la variable sería descubrirlo tarde.
    """
    if nombre not in PUNTOS:
        raise ErrorDeRuntime(
            "el runtime llama a un punto de fallo no declarado en el §4.2",
            codigo="PUNTO_DE_FALLO_DESCONOCIDO",
            punto=nombre,
        )
    if activo() != nombre:
        return
    # `os.write` directo sobre el descriptor 2 y no `print`: el búfer de `sys.stderr` no se
    # vacía con `os._exit`, y sin esta línea la prueba no podría distinguir «murió en el
    # punto» de «murió por otra cosa con el mismo código».
    try:
        sys.stderr.flush()
    except (ValueError, OSError):
        # stderr puede estar ya cerrado o redirigido a un descriptor muerto. Que no se
        # pueda avisar no cambia el contrato: el corte se produce igual.
        pass
    try:
        os.write(2, ("ADS_RUNTIME_FALLO: corte inyectado en " + nombre + "\n").encode("utf-8"))
    except OSError:
        pass
    os._exit(CODIGO_DE_SALIDA)
