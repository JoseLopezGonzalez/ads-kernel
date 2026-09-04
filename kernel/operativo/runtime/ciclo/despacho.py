#!/usr/bin/env python3
"""despacho — la etapa 5 del ciclo. DELEGA en el runtime; no reimplementa su máquina.

    «el runtime debe EJECUTAR O VALIDAR contratos existentes en lugar de duplicar su
     semántica en código independiente»                    regla 16.1, citada en `§7.1`

Lease, selección de adaptador, ejecución, progreso, resultado e idempotencia del efecto ya
están construidos y probados en `runtime/dispatcher.py`. Este módulo es **el único punto por
el que el ciclo y los cuatro macrocircuitos entran a despachar**, y su cuerpo entero cabe en
una pantalla a propósito: todo lo que hiciera de más sería una segunda máquina de despacho.

DECISIÓN · un ÚNICO punto de entrada, y es observable
    Alternativas: (a) que cada macrocircuito llame a `Runtime.despachar` por su cuenta; (b)
    que todos pasen por aquí.
    Se elige (b), y no por estética: `§9.6` regla 6 exige «el MISMO contrato y el MISMO
    mecanismo compartido» y prohíbe «cuatro implementaciones divergentes». Con (a) esa
    exigencia sólo se puede afirmar leyendo cuatro ficheros; con (b) se puede MEDIR, y
    `test_macrocircuitos.py` lo mide: instala un observador, ejecuta los cuatro
    macrocircuitos y comprueba que las cuatro ejecuciones pasan por este punto y no por
    otro.

DECISIÓN · el observador NO participa en ninguna decisión y no puede impedir nada
    Es una lista de invocables que reciben una copia del resumen. Si un observador fallara,
    su error se propaga —no se traga— pero ya se ha despachado: el efecto es del runtime y
    no de la observación. No hay ninguna ruta en la que lo observado cambie lo despachado.

DECISIÓN · IMPEDIR DOBLE EFECTO no se reimplementa aquí, y se dice dónde está
    El acuse durable `canonico/efectos/<efecto>.json` y el recibo del adaptador son los dos
    niveles, y viven en `runtime/dispatcher.py` y en `adaptadores/proceso.py`. Reescribir
    aquí una tercera comprobación daría una tercera respuesta posible ante la misma
    pregunta, y `I5` prohíbe la segunda copia editable de una verdad.
"""
from __future__ import annotations

from .errores import CicloInconsistente

# El nombre del punto ÚNICO, escrito una vez para que las pruebas lo puedan citar.
PUNTO_DE_ENTRADA = "ciclo.despacho.despachar"

_OBSERVADORES = []


def observar(invocable):
    """Registra un observador del punto único. Devuelve un retirador."""
    if not callable(invocable):
        raise CicloInconsistente("un observador del despacho es un invocable")
    _OBSERVADORES.append(invocable)

    def retirar():
        if invocable in _OBSERVADORES:
            _OBSERVADORES.remove(invocable)
    return retirar


def _anunciar(suceso):
    for observador in list(_OBSERVADORES):
        observador(dict(suceso))


def despachar(runtime, paquete, *, origen="ciclo"):
    """Despacha UN paquete por el runtime. El resultado es el del runtime, sin adornos."""
    resumen = runtime.despachar(paquete)
    _anunciar({"punto": PUNTO_DE_ENTRADA, "origen": str(origen), "paquete": paquete,
               "desenlace": resumen.get("desenlace"), "instancia": runtime.instancia})
    return resumen


def barrido(runtime, *, maximo=0, origen="ciclo"):
    """Un barrido completo del dispatcher: sanea lo que quedó a medias y despacha."""
    informe = runtime.ciclo(maximo=maximo)
    for atendido in informe.get("atendidos") or []:
        _anunciar({"punto": PUNTO_DE_ENTRADA, "origen": str(origen),
                   "paquete": atendido.get("paquete"),
                   "desenlace": atendido.get("desenlace"),
                   "instancia": runtime.instancia})
    return informe


def elegibles(runtime):
    """El trabajo elegible, DERIVADO del estado por el runtime. Aquí no se ordena nada.

    Y sigue sin ordenarse aquí, que es lo correcto: el orden de `b.12` paso 5 —prioridad,
    grado de salida, antigüedad de espera, identificador— vive en `runtime.politica` y lo
    aplica `Dispatcher.elegibles`. Lo que la auditoría midió no fue que este módulo delegara,
    fue que allí sólo estuvieran DOS de los cuatro criterios; reordenar aquí habría creado la
    segunda máquina de selección que este módulo existe para impedir.
    """
    return runtime.elegibles()


def seleccionar(runtime, *, cabida=1):
    """`b.12` pasos 5, 6 y 7 por el runtime: elige, y ESCRIBE por qué esperan los demás.

    Punto único también para la SELECCIÓN, por la misma razón que para el despacho: si cada
    macrocircuito eligiera por su cuenta, los contadores de inanición se llevarían en cuatro
    sitios y ninguno sería el bueno.
    """
    return runtime.seleccionar_siguiente(cabida=cabida)


def inanicion(runtime):
    """Qué lleva esperando y por qué, DERIVADO. `b.12`: DSP informa; no cambia prioridades."""
    return runtime.vistas()["que_lleva_esperando"]


def estado_de(runtime, paquete):
    return runtime.estado_de_paquete(paquete)
