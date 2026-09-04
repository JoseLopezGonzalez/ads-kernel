#!/usr/bin/env python3
"""vistas — las vistas ejecutivas del §7.5, DERIVADAS y nunca fuente de verdad.

    «LA VISTA es DERIVADA del estado canónico, no un informe redactado. […] NO RESPONDE
     nada que no esté en el estado. Una vista que sabe más que el estado es una segunda
     verdad.»                                                     `11-ARQ` §7.5

DECISIÓN · se CALCULAN en cada llamada y NO se persisten
    Alternativas: (a) materializar la vista en `canonico/vistas/` y refrescarla; (b)
    cachearla en memoria del runtime; (c) recalcularla del estado en cada llamada.
    Se elige (c). Con (a) la vista sería estado canónico, y entonces habría dos sitios que
    afirman lo mismo y pueden discrepar: exactamente la segunda verdad que §7.5 prohíbe, y
    además un objeto durable derivado que `I5` obliga a recompilar y no a sincronizar. Con
    (b) la caché sobreviviría a un cambio hecho por OTRA instancia y la vista mentiría
    justo cuando hay concurrencia, que es cuando se mira. Con (c) la vista no puede saber
    más que el estado porque no tiene dónde guardarlo.

DECISIÓN · «qué cambió» sale del DIARIO, no de un registro propio de cambios
    El diario canónico ya registra los eventos que explican cada transición, con orden
    reconstruible (`g.7`). Un segundo registro de cambios en el runtime sería un diario
    paralelo, y el §0 del contrato lo prohíbe por su nombre.

Las cinco preguntas del §4.2 —qué se está construyendo · qué está bloqueado · qué espera
decisión del Owner · qué cambió · qué reconciliaciones hay abiertas— son las cinco claves
de la salida, con esos nombres, para que confrontar la vista con el contrato sea leer.

DECISIÓN · la INANICIÓN de `b.12` es una vista, y no una sexta pregunta disfrazada
    `b.12` remata su detección de inanición con una frase que no admite lectura: «DSP informa
    de la inanición. **No cambia la prioridad. Nunca**». Informar es exactamente esto: una
    vista DERIVADA, sin autoridad, que no puede escribir nada y por tanto no puede subir
    ninguna prioridad ni aunque quisiera. Poner la detección donde se decide —en el
    dispatcher, con capacidad de escritura— habría dejado a un paso el atajo que el contrato
    prohíbe. Los contadores los mantiene el dispatcher, porque son estado; MOSTRARLOS es de
    aquí, porque es vista.
"""
from __future__ import annotations

from .modelo import (
    DOMINIO_LEASES,
    DOMINIO_PAQUETES,
    ESTADOS_EN_CURSO,
    comprobar_paquete,
    identificador_de,
)

EVENTOS_RECIENTES_POR_DEFECTO = 10

# Los estados que, según el vocabulario cerrado del §3 y §7.3 de `11-ARQ`, describen a un
# paquete detenido a la espera de que alguien haga algo:
#   `bloqueado`             GENERA TRABAJO: crear el desbloqueador (b.15.1)
#   `esperando-dependencia` se resuelve solo y NO genera trabajo (b.8)
#   `agotado`               la salida la decide la AUTORIDAD por `g.9`
#   `pausado`               espera una reanudación explícita
ESTADOS_DETENIDOS = ("bloqueado", "esperando-dependencia", "agotado", "pausado")
ESTADOS_QUE_ESPERAN_AL_OWNER = ("agotado", "pausado", "bloqueado")


def _paquetes(almacen):
    """Todos los paquetes de la revisión vigente, comprobados y ordenados."""
    salida = []
    for ruta in almacen.listar(DOMINIO_PAQUETES):
        salida.append(comprobar_paquete(almacen.leer(ruta), ruta))
    salida.sort(key=lambda p: p["id"])
    return salida


def _leases(almacen):
    salida = {}
    for ruta in almacen.listar(DOMINIO_LEASES):
        salida[identificador_de(ruta)] = almacen.leer(ruta)
    return salida


def _resumen(paquete, leases):
    lease = leases.get(paquete["id"])
    return {
        "paquete": paquete["id"],
        "item": paquete["item"],
        "estado": paquete["estado"],
        "prioridad": paquete["prioridad"],
        "intentos": paquete["intentos"],
        "max_intentos": paquete["max_intentos"],
        "titular": lease["titular"] if lease else None,
        "epoca": lease["epoca"] if lease else None,
        "latido": lease["latido"] if lease else None,
    }


def _inanicion(paquete, revision):
    """Los CUATRO campos de `b.12` de un paquete `listo` no despachado, tal cual se guardan.

    `b.12` no pide sólo que se cuenten: pide que se MUESTREN —«DSP mantiene y muestra»—, y
    una cuenta durable que ninguna vista publica es una cuenta que nadie va a mirar. La
    antigüedad se calcula aquí, contra la revisión vigente, porque es una RESTA de dos datos
    del estado y no un dato nuevo: la vista no puede saber más que el estado (`§7.5`).
    """
    seleccion = paquete["seleccion"]
    listo_en = seleccion["listo_en"]
    return {
        "paquete": paquete["id"],
        "item": paquete["item"],
        "prioridad": paquete["prioridad"],
        "listo_en": listo_en,
        "tiempo_listo": (int(revision["revision"]) - listo_en) if listo_en is not None else 0,
        "postergaciones": seleccion["postergaciones"],
        "adelantado_por": list(seleccion["adelantado_por"]),
        "impedimento": seleccion["impedimento"],
    }


def derivar(almacen, *, eventos_recientes=EVENTOS_RECIENTES_POR_DEFECTO):
    """Las cinco vistas del §7.5, calculadas del estado canónico. No escribe nada."""
    revision = almacen.revision()
    paquetes = _paquetes(almacen)
    leases = _leases(almacen)

    construyendo = [_resumen(p, leases) for p in paquetes if p["estado"] in ESTADOS_EN_CURSO]
    bloqueado = [_resumen(p, leases) for p in paquetes if p["estado"] in ESTADOS_DETENIDOS]
    del_owner = [_resumen(p, leases) for p in paquetes
                 if p["estado"] in ESTADOS_QUE_ESPERAN_AL_OWNER]

    eventos = almacen.diario()
    ultimos = eventos[-int(eventos_recientes):] if eventos_recientes else []
    cambios = [
        {
            "secuencia": evento["secuencia"],
            "tipo": evento["tipo"],
            "transaccion": evento.get("transaccion"),
            "autor": evento.get("autor"),
            "motivo": evento.get("motivo"),
        }
        for evento in ultimos
    ]

    pendientes = [
        {
            "registro": linea["registro"],
            "producto": linea["producto"],
            "repositorio": linea["repositorio"],
            "item": linea["item"],
            "intento": linea["intento"],
            "causa": linea["causa"],
            "momento": linea["momento"],
        }
        for linea in almacen.reconciliacion_pendiente()
    ]

    # `b.12`, detección de inanición: «Por cada paquete `listo` no despachado, DSP mantiene
    # y muestra». Se ordena por el que más lleva esperando, que es el que hay que ver
    # primero; el desempate es el identificador, como en todo lo demás.
    inanicion = sorted(
        (_inanicion(p, revision) for p in paquetes if p["estado"] == "listo"),
        key=lambda fila: (-fila["tiempo_listo"], -fila["postergaciones"], fila["paquete"]),
    )

    return {
        "derivada": True,
        "que_lleva_esperando": inanicion,
        "revision": revision["revision"],
        "revision_id": revision["revision_id"],
        "ventana": almacen.estado_de_la_ventana(),
        "que_se_esta_construyendo": construyendo,
        "que_esta_bloqueado": bloqueado,
        "que_espera_decision_del_owner": del_owner,
        "que_cambio": cambios,
        "reconciliaciones_abiertas": pendientes,
        "recuento": {
            estado: len([p for p in paquetes if p["estado"] == estado])
            for estado in sorted({p["estado"] for p in paquetes})
        },
    }
