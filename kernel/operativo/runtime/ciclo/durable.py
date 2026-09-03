#!/usr/bin/env python3
"""durable — la ÚNICA puerta por la que el CICLO escribe, y va al motor que ya existe.

No hay aquí ningún estado. Hay una función, y su razón de existir es la misma que la de
`runtime/estado_util.py`, que se reutiliza tal cual: el motor aplica cada transición con
comparación e intercambio sobre la revisión base, así que la transición se construye como
FUNCIÓN de la revisión releída y la guarda se reevalúa en cada vuelta.

DECISIÓN · el ciclo NO tiene almacén propio y NO abre el suyo
    Recibe el `Almacen` que el `Runtime` ya abrió —y que ya RECUPERÓ antes de despachar—.
    Abrir un segundo almacén sobre el mismo control repo daría dos escritores donde `g.12`
    declara UNO, y la recuperación se ejecutaría dos veces sobre la misma ventana.

DECISIÓN · escribir es IDEMPOTENTE por contenido, y por eso repetir no duplica
    Todo objeto del ciclo lleva un identificador DERIVADO de su contenido. Antes de
    escribir se comprueba si la ruta lógica ya existe con el mismo `cid`: si existe, no se
    escribe nada y se devuelve `None`. Encuadrar dos veces la misma entrada, componer dos
    veces la misma ruta o materializar dos veces el mismo equipo dejan el estado EXACTAMENTE
    igual, que es lo que hace que `Continúa` pueda ejecutarse dos veces seguidas sin mover
    la revisión.

DECISIÓN · el identificador de transacción entra la revisión y el autor, como en el runtime
    Por el mismo motivo que allí: sin la revisión, dos vueltas del reintento producirían el
    mismo identificador y el motor devolvería la primera como `repetida` en vez de aplicar
    la segunda, que es la construida sobre el estado nuevo.
"""
from __future__ import annotations

import estado
from estado.serializacion import cid_de_objeto
from runtime.estado_util import aplicar_con_reintento

from .errores import CicloInconsistente

AUTOR_POR_DEFECTO = "DSP"


def identificador_de_transaccion(clase, autor, revision, semilla):
    digest = cid_de_objeto({
        "clase": clase, "autor": autor,
        "revision": revision["revision_id"], "semilla": semilla,
    })
    return "tx-cl-" + digest.split(":", 1)[-1][:16]


def ya_escrito(almacen, ruta, cuerpo):
    """¿Está ya ese contenido EXACTO en esa ruta? Lee el estado; no recuerda nada."""
    revision = almacen.revision()
    esperado = revision["raiz"].get(ruta)
    if esperado is None:
        return False
    return esperado == cid_de_objeto(_con_esquema(cuerpo))


def _con_esquema(cuerpo):
    from estado.serializacion import con_esquema
    return con_esquema(cuerpo)


def escribir(almacen, *, clase, motivo, objetos, autor=AUTOR_POR_DEFECTO, borrados=(),
             semilla=None, guarda=None):
    """Publica `objetos` —`{ruta_logica: cuerpo}`— en UNA transición. `None` si nada cambia.

    `guarda(revision)` se reevalúa en cada vuelta y puede levantar un error tipado: es
    donde el llamador comprueba que sigue siendo cierto lo que creía al construir.
    """
    if not isinstance(objetos, dict):
        raise CicloInconsistente("`objetos` es un mapa de ruta lógica a cuerpo")
    if not objetos and not borrados:
        return None

    def construir(revision):
        if guarda is not None:
            guarda(revision)
        operaciones = []
        for ruta in sorted(objetos):
            cuerpo = objetos[ruta]
            if ya_escrito(almacen, ruta, cuerpo):
                continue
            operaciones.append(estado.Escritura(ruta, cuerpo))
        for ruta in sorted(borrados):
            if revision["raiz"].get(ruta) is not None:
                operaciones.append(estado.Borrado(ruta))
        if not operaciones:
            return None
        return estado.Transicion(
            tipo=clase, base=revision["revision_id"], operaciones=operaciones,
            autor=autor, motivo=motivo,
            id=identificador_de_transaccion(
                clase, autor, revision,
                semilla if semilla is not None else sorted(objetos),
            ),
        )

    return aplicar_con_reintento(almacen, construir, descripcion=clase + ": " + motivo)


def leer(almacen, ruta):
    """El objeto de una ruta lógica, o `None`. Nunca se inventa lo que no está."""
    from estado.errores import RutaInvalida
    try:
        return almacen.leer(ruta)
    except RutaInvalida:
        return None


def listar(almacen, dominio):
    return list(almacen.listar(dominio))
