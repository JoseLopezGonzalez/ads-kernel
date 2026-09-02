#!/usr/bin/env python3
"""fallos — puntos de fallo controlados, para que la recuperación se DEMUESTRE.

Una recuperación que sólo se ha visto no ejecutarse no está verificada. `g.4` exige que lo
confirmado como durable sobreviva a un corte, y un corte no se puede argumentar: hay que
provocarlo. Este módulo provoca cortes REALES en fronteras conocidas.

Cómo mata, y por qué así:
    `os._exit(70)` termina el proceso sin ejecutar `finally`, sin `atexit`, sin vaciar
    los búferes de `io` y sin cerrar ordenadamente los descriptores. Es lo más parecido a
    un corte de corriente que un proceso puede hacerse a sí mismo. `sys.exit()` NO sirve:
    levanta `SystemExit`, los `finally` corren, los ficheros se cierran y se vacían, y
    entonces la prueba demostraría una recuperación que en la realidad nunca haría falta.
    `raise` tampoco sirve, por lo mismo. 70 es `EX_SOFTWARE` de `sysexits.h`, elegido por
    no colisionar con 0, 1 y 2, que el §11 reserva a la semántica de la CLI.

Cómo se activa:
    Sólo por `ADS_ESTADO_FALLO=<punto>`. **Sin esa variable el módulo no hace nada**: no
    lee ficheros, no escribe, no importa nada caro. Es requisito del §10 y también de
    higiene, porque este código viaja dentro del motor de producción.

DECISIÓN · un punto desconocido en la variable de entorno es un FALLO, no un silencio
    Alternativas: (a) ignorar un nombre no declarado; (b) fallar cerrado.
    Se elige (b). Con (a), una prueba con el nombre mal escrito —`antes-del-commit` en vez
    de `antes-del-commit-atomico`— pasaría en verde sin haber inyectado nada, y estaríamos
    publicando como evidencia de recuperación una ejecución en la que nunca hubo corte. Es
    exactamente el defecto que `g.13` prohíbe: comprobar contra un informe y no contra el
    estado. Fallar cerrado convierte la errata en un error visible.

DECISIÓN · `punto()` dispara en la PRIMERA visita al punto nombrado
    Alternativas: (a) disparar siempre que se pase por el punto; (b) permitir «a la N-ésima
    visita». Como el proceso muere en la primera, (a) y (b) coinciden salvo para el punto
    `durante-el-diario`, por el que una transición pasa varias veces. Se elige (a) por ser
    la más simple y la más determinista: con `ADS_ESTADO_FALLO=durante-el-diario` el corte
    cae siempre en el primer anexado del proceso, que en `aplicar` es `transicion.abierta`,
    justo donde el §3 lo sitúa. Un «a la N-ésima» introduciría un contador de ejecución, y
    aunque viviera sólo en memoria acercaría el motor a lo que `I-g3` proscribe.

`puntos()` devuelve la lista declarada para que una prueba compruebe, contra el propio
código fuente, que **ningún punto declarado quedó sin llamar**: censo derivado, no una
lista escrita a mano en la prueba.
"""
from __future__ import annotations

import os
import sys

from .errores import ErrorDeEstado

VARIABLE = "ADS_ESTADO_FALLO"

# El orden es el del §10 del contrato, que a su vez es el orden en que el protocolo
# transaccional los atraviesa. No se ordena alfabéticamente a propósito: leer esta tupla
# de arriba abajo es leer el protocolo.
PUNTOS = (
    "antes-de-escribir-temporal",
    "despues-de-escribir-temporal",
    "despues-de-sincronizar-temporal",
    "antes-del-commit-atomico",
    "despues-del-commit-atomico",
    "antes-de-sincronizar-directorio",
    "durante-el-diario",
    "durante-el-registro-auxiliar",
    "antes-de-devolver-exito",
)

CODIGO_DE_SALIDA = 70


def puntos():
    """Los puntos declarados, en el orden del §10."""
    return list(PUNTOS)


def activo():
    """El punto pedido por el entorno, o `None`. Valida el nombre: no adivina."""
    nombre = os.environ.get(VARIABLE)
    if not nombre:
        return None
    if nombre not in PUNTOS:
        raise ErrorDeEstado(
            "el punto de fallo pedido no está declarado en el §10; puntos válidos: "
            + ", ".join(PUNTOS),
            codigo="PUNTO_DE_FALLO_DESCONOCIDO",
            punto=nombre,
        )
    return nombre


def punto(nombre):
    """Frontera del protocolo. Si el entorno la nombra, el proceso muere AQUÍ.

    `nombre` se comprueba contra `PUNTOS` aunque el entorno no pida nada: una llamada con
    un nombre inventado es un defecto del motor, y descubrirlo sólo cuando alguien exporta
    la variable sería descubrirlo tarde.
    """
    if nombre not in PUNTOS:
        raise ErrorDeEstado(
            "el motor llama a un punto de fallo no declarado en el §10",
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
        os.write(2, ("ADS_ESTADO_FALLO: corte inyectado en " + nombre + "\n").encode("utf-8"))
    except OSError:
        pass
    os._exit(CODIGO_DE_SALIDA)
