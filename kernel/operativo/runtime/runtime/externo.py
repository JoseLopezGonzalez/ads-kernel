#!/usr/bin/env python3
"""externo — el PROTOCOLO DE TRABAJADORES: ejecutar un paquete FUERA del proceso del runtime.

    «Todo lo que decide queda escrito en el estado canónico ANTES de que valga. Si el
     runtime muere, el estado sigue siendo el estado.»                       `11-ARQ` §7.1

HECHO MEDIDO ANTES DE CONSTRUIR, en la primera adopción real (La Pesquerapp, 2026-09-14).
El dispatcher sólo sabía ejecutar un paquete llamando a `adaptador.ejecutar(...)` dentro de
su propio proceso, y el único adaptador real lanzaba un `subprocess`. El trabajo real de un
producto lo hacían AGENTES —sesiones de agente de un proveedor, o personas— que no cabían en
esa llamada: nadie podía TOMAR un paquete, dejar un CHECKPOINT durable y ENTREGAR el
resultado desde otro proceso, otra sesión u otra máquina. La consecuencia se midió: cero
paquetes, cero leases, y una organización cuya única memoria de ejecución era el chat.

Este módulo añade al `Runtime` la ejecución EXTERNA, y lo hace SOBRE la máquina que ya
existe, sin una segunda: el lease sigue siendo el de `lease.py`, el intento y el efecto los
de `dispatcher.py`, el acuse el de `modelo.nuevo_acuse`, y la política de reintentos la de
`politica.py`. Lo único nuevo es que EJECUTAR se parte en tres actos durables separados en
el tiempo y, si hace falta, en el espacio:

    TOMAR       adquirir el lease · abrir el intento (`listo` → `despachado`) · marcar
                `ejecutando`. Devuelve el EFECTO fijado para este intento y el checkpoint
                vigente, si lo hay. Un paquete `ejecutando` sin lease —lo dejó un trabajador
                que murió y cuyo lease fue reclamado y soltado— se toma IGUAL y conserva
                su efecto: la reanudación reutiliza el mismo intento.
    CHECKPOINT  escribir `checkpoints/<paquete>.json` bajo titularidad, y LATIR. Es lo que
                hace que un trabajador que muere a medias no se lleve el trabajo: el que
                reclame después lee el checkpoint, no la conversación.
    ENTREGAR    publicar el resultado con la forma del §4.4 —el efecto lo pone el runtime,
                no el trabajador— por la MISMA transición que usa el dispatcher: resultado,
                acuse y latido en UNA `Transicion`. Después, la política: completado, fallo
                reintentable (vuelve a `listo`), definitivo o ambiguo (agotado y `g.9`).

DECISIÓN · un paquete EXTERNO se distingue por su ORDEN, y el dato es durable
    `orden.adaptador == "worker"` declara que el paquete lo ejecuta un trabajador que
    reclama, no un adaptador en proceso. Alternativas: (a) una lista de adaptadores externos
    en el registro; (b) el dato en el paquete. Se elige (b): el paquete es lo que sobrevive
    a la caída, y un barrido que arranque sin registro tiene que poder distinguir «esto
    espera a un trabajador» de «esto lo ejecuto yo» leyendo sólo el estado. El barrido
    `ciclo()` NO despacha paquetes externos: los lista como `externos` y no toca su lease.

DECISIÓN · el trabajador ES la instancia del runtime
    No hay un identificador de trabajador aparte del `titular` del lease. Dos sesiones que
    tomen el mismo paquete compiten por el MISMO lease que ya existía, con la misma
    comparación e intercambio, y exactamente una lo consigue (`T182`). Un trabajador que
    muere deja un lease sin latido; otro lo observa `PACIENCIA` veces y lo reclama por la
    única puerta que hay (`lease.py`). No se ha inventado ninguna vía nueva de autoridad.

DECISIÓN · el checkpoint vive en su propio dominio y NO dentro del paquete
    `runtime/modelo.py` valida el paquete contra una lista CERRADA de claves y rechaza las
    que sobran; abrirla para meter el checkpoint sería cambiar el contrato del corte 2 para
    ahorrarse un objeto. `checkpoints/<paquete>.json` se escribe en la misma transición que
    el latido del lease, de modo que un checkpoint sin autoridad no puede existir.

DECISIÓN · TOMAR no es RECLAMAR, y por eso se llaman distinto
    `Runtime.reclamar` ya existe y es la única puerta para quitarle el lease a otro tras
    `PACIENCIA` observaciones (`lease.py`). Tomar un paquete es lo contrario: pedir
    autoridad sobre trabajo LIBRE por `adquirir`, que nunca roba. Darles el mismo nombre
    haría que «un trabajador toma trabajo» y «una instancia se lleva el lease de un
    muerto» fuesen indistinguibles en el diario, y son dos hechos con dos autoridades.

DECISIÓN · `entregar` NO acepta un `efecto` del trabajador
    El efecto lo fijó `_abrir_intento` al tomar. Un trabajador que pudiera declarar el
    efecto podría acusar un intento que no es el suyo. Se toma del paquete, y se comprueba
    que el paquete sigue en `ejecutando` bajo la misma época del lease.
"""
from __future__ import annotations

import estado

from . import politica
from .errores import EstadoDePaqueteInvalido, RecursoOcupado, RuntimeInconsistente
from .lease import con_latido, exigir_titularidad
from .modelo import ESQUEMA, ruta_lease, ruta_paquete

# El adaptador DECLARADO de un paquete externo. Es un dato del paquete, no un adaptador
# registrado: ningún registro lo ofrece, y por eso `despachar` sobre uno de estos paquetes
# levanta `CapacidadNoSoportada` en vez de ejecutar algo por su cuenta.
ADAPTADOR_EXTERNO = "worker"
CAPACIDAD_EXTERNA = "worker"

DOMINIO_CHECKPOINTS = "checkpoints"

# Lo que un trabajador declara al entregar. `efecto` y `repetido` los pone el runtime.
CLAVES_DE_ENTREGA_EXTERNA = ("estado", "codigo", "salida", "detalle", "reintentable")
ESTADOS_DE_ENTREGA_EXTERNA = ("completado", "fallido", "cancelado", "ambiguo")


def es_externo(paquete):
    """¿Este paquete lo ejecuta un trabajador que reclama, y no un adaptador en proceso?"""
    return str((paquete.get("orden") or {}).get("adaptador") or "") == ADAPTADOR_EXTERNO


def orden_externa(*, operacion="trabajar", argumentos=(), limite_segundos=86400):
    """La orden de un paquete externo, con la forma cerrada del §3."""
    return {
        "adaptador": ADAPTADOR_EXTERNO,
        "operacion": str(operacion),
        "argumentos": [str(a) for a in argumentos],
        "limite_segundos": limite_segundos,
    }


def ruta_checkpoint(paquete):
    return DOMINIO_CHECKPOINTS + "/" + paquete + ".json"


def comprobar_entrega_externa(resultado):
    """La forma que un trabajador entrega, validada ANTES de tocar el estado. Fallo cerrado."""
    if not isinstance(resultado, dict):
        raise RuntimeInconsistente("una entrega externa es un mapa")
    faltan = [c for c in CLAVES_DE_ENTREGA_EXTERNA if c not in resultado]
    if faltan:
        raise RuntimeInconsistente(
            "la entrega externa no declara " + ", ".join(faltan) + "; sin ellos el runtime "
            "no puede clasificar el desenlace y clasificarlo de todos modos sería inventar "
            "estado",
        )
    if resultado["estado"] not in ESTADOS_DE_ENTREGA_EXTERNA:
        raise RuntimeInconsistente(
            "`estado` de la entrega externa fuera del vocabulario: " + repr(resultado["estado"])
            + "; válidos: " + ", ".join(ESTADOS_DE_ENTREGA_EXTERNA),
        )
    if not isinstance(resultado["reintentable"], bool):
        raise RuntimeInconsistente("`reintentable` de la entrega externa es booleano")
    if not isinstance(resultado["codigo"], int) or isinstance(resultado["codigo"], bool):
        raise RuntimeInconsistente("`codigo` de la entrega externa es un entero")
    for clave in ("salida", "detalle"):
        if not isinstance(resultado[clave], str):
            raise RuntimeInconsistente("`" + clave + "` de la entrega externa es texto")
    return resultado


# ===========================================================================
#  los tres actos, sobre el Runtime
# ===========================================================================
def tomar(runtime, paquete):
    """TOMAR: lease + intento + `ejecutando`, y devolver efecto y checkpoint vigentes.

    Nunca roba. Si el lease es de otro, es `AutoridadNoDisponible` y el trabajador tiene
    que observar y reclamar por la puerta de `lease.py`, como cualquier instancia.
    """
    runtime._exigir_operable()
    runtime._exigir_no_marcado()
    actual = runtime._leer_paquete(paquete)
    if not es_externo(actual):
        raise EstadoDePaqueteInvalido(
            "el paquete `" + paquete + "` no es externo: su orden declara el adaptador `"
            + str(actual["orden"]["adaptador"]) + "` y lo ejecuta el dispatcher, no un "
            "trabajador", ruta=paquete,
        )
    lease = runtime.adquirir(paquete)
    try:
        # Directiva §68: listo funcionalmente, pero otra ejecución posee un recurso que este
        # paquete también escribe. No se toma; se publica quién lo posee.
        conflicto = runtime._conflicto_de_recursos(
            actual, runtime._recursos_ocupados(runtime._todos_los_paquetes(), salvo=paquete))
        if conflicto:
            raise RecursoOcupado(
                "el paquete `" + paquete + "` es temporalmente incompatible: "
                + "; ".join(c["recurso"] + " lo posee `" + c["lo_posee"] + "`" for c in conflicto)
                + " (§68). Se toma cuando el otro entregue", ruta=paquete,
            )
        actual = runtime._resolver_dependencias(paquete, actual, lease)
        if actual["estado"] == "listo":
            actual = runtime._abrir_intento(paquete, lease)
        elif actual["estado"] not in ("despachado", "ejecutando"):
            raise EstadoDePaqueteInvalido(
                "un paquete en `" + actual["estado"] + "` no se toma; la tabla del §4.2 "
                "no lleva de ahí a `ejecutando`", ruta=paquete,
            )
        if actual["estado"] == "despachado":
            actual = runtime._marcar_ejecutando(paquete, lease)
    except BaseException:
        # Nada se ha ejecutado: retener la autoridad dejaría el paquete inalcanzable.
        runtime._soltar_si_es_mio(paquete)
        raise
    return {
        "paquete": paquete,
        "item": actual["item"],
        "estado": actual["estado"],
        "intento": actual["intentos"],
        "max_intentos": actual["max_intentos"],
        "efecto": actual["efecto"],
        "lease": runtime._leer_lease(paquete),
        "checkpoint": leer_checkpoint(runtime, paquete),
        "orden": dict(actual["orden"]),
    }


def leer_checkpoint(runtime, paquete):
    return runtime._leer_opcional(ruta_checkpoint(paquete))


def checkpoint(runtime, paquete, contenido):
    """Escribe el checkpoint del trabajador bajo titularidad y LATE en la misma transición.

    `contenido` es un mapa del trabajador; se conserva ENTERO bajo `contenido`, y el runtime
    añade lo que hace al checkpoint auditable: paquete, intento y efecto. Un checkpoint que
    no case con el intento vigente no se escribe.
    """
    runtime._exigir_operable()
    if not isinstance(contenido, dict):
        raise RuntimeInconsistente("el checkpoint es un mapa", ruta=paquete)
    escrito = {}

    def construir(revision):
        actual = runtime._leer_paquete(paquete)
        vigente = exigir_titularidad(runtime._leer_lease(paquete), runtime.instancia, None,
                                     paquete=paquete)
        if actual["estado"] != "ejecutando":
            raise EstadoDePaqueteInvalido(
                "sólo se escribe checkpoint de un paquete `ejecutando`; está `"
                + actual["estado"] + "`", ruta=paquete,
            )
        nuevo = {
            "esquema": ESQUEMA,
            "paquete": paquete,
            "item": actual["item"],
            "intento": int(actual["intentos"]),
            "efecto": actual["efecto"],
            "titular": runtime.instancia,
            "epoca": int(vigente["epoca"]),
            "contenido": dict(contenido),
        }
        escrito["checkpoint"] = nuevo
        return runtime._transicion(
            "runtime.checkpoint.escrito", revision,
            [estado.Escritura(ruta_checkpoint(paquete), nuevo),
             estado.Escritura(ruta_lease(paquete), con_latido(vigente))],
            "checkpoint del trabajador `" + runtime.instancia + "` sobre " + paquete,
            {"paquete": paquete, "intento": nuevo["intento"],
             "contenido_cid": estado.cid_de_objeto(nuevo["contenido"])},
        )

    runtime._aplicar("runtime.checkpoint.escrito", construir,
                     descripcion="checkpoint de " + paquete)
    return escrito["checkpoint"]


def entregar(runtime, paquete, entrega):
    """ENTREGAR: el resultado del trabajador, publicado por la máquina del dispatcher.

    Devuelve el mismo resumen que `Runtime.despachar` —desenlace, decisión, intento— para
    que quien lea el informe no tenga que saber si el paquete lo ejecutó un adaptador o un
    trabajador. La autoridad se suelta al final, como allí.
    """
    runtime._exigir_operable()
    comprobar_entrega_externa(entrega)
    actual = runtime._leer_paquete(paquete)
    if not es_externo(actual):
        raise EstadoDePaqueteInvalido(
            "el paquete `" + paquete + "` no es externo; su resultado lo publica el "
            "dispatcher al ejecutar su adaptador", ruta=paquete,
        )
    if actual["estado"] != "ejecutando":
        raise EstadoDePaqueteInvalido(
            "sólo se entrega un paquete `ejecutando`; está `" + actual["estado"]
            + "`. Un trabajador entrega lo que tomó, no lo que le apetece", ruta=paquete,
        )
    lease = exigir_titularidad(runtime._leer_lease(paquete), runtime.instancia, None,
                               paquete=paquete)
    efecto = actual["efecto"]
    resultado = {
        "estado": entrega["estado"],
        "codigo": int(entrega["codigo"]),
        "salida": str(entrega["salida"]),
        "detalle": str(entrega["detalle"]),
        "reintentable": bool(entrega["reintentable"]),
        "efecto": efecto,
        "repetido": False,
    }
    politica.comprobar_resultado(resultado, efecto=efecto, paquete=paquete)
    clase, error = politica.clasificar(resultado)
    estado_final = politica.estado_de_paquete(clase)
    registro = politica.durable(resultado)
    actual, _acuse = runtime._publicar_resultado(paquete, lease, efecto, registro, estado_final)
    resumen = runtime._cerrar(paquete, actual, lease, efecto, registro,
                              repetido=False, error=error, clase=clase)
    resumen["externo"] = True
    if error is not None:
        error.contexto.update({"paquete": paquete, "intento": resumen["intento"],
                               "desenlace": resumen["desenlace"]})
        resumen["error"] = error.a_dict()
    return resumen


def soltar(runtime, paquete):
    """Devolver la autoridad sin entregar. El paquete queda donde estaba, sin lease.

    Un `despachado` sin empezar vuelve a `listo` (lo hace `liberar`); un `ejecutando` se
    queda `ejecutando` con su efecto, y el siguiente que lo tome lo reanuda leyendo el
    checkpoint. Es la salida honesta de un trabajador que se va: no finge un fallo ni un
    resultado.
    """
    runtime._exigir_operable()
    runtime.liberar(paquete)
    return runtime._leer_paquete(paquete)


def externos(runtime):
    """Los paquetes externos, por estado, con su titular y su checkpoint. DERIVADO."""
    salida = []
    for paquete in runtime._todos_los_paquetes():
        if not es_externo(paquete):
            continue
        lease = runtime._leer_lease(paquete["id"])
        salida.append({
            "paquete": paquete["id"],
            "item": paquete["item"],
            "estado": paquete["estado"],
            "prioridad": paquete["prioridad"],
            "intentos": paquete["intentos"],
            "titular": lease["titular"] if lease else None,
            "epoca": lease["epoca"] if lease else None,
            "checkpoint": leer_checkpoint(runtime, paquete["id"]),
            "capacidades_requeridas": list(paquete["capacidades_requeridas"]),
            "depende_de": list(paquete["depende_de"]),
        })
    return salida


def tomables(runtime):
    """Lo que un trabajador PUEDE tomar ahora: externos sin dependencia pendiente y sin lease ajeno.

    Un paquete `ejecutando` con lease de OTRO no es tomable: hay que observarlo `PACIENCIA`
    veces. Uno con dependencias sin completar tampoco. Los dos se listan aparte —con su
    titular, o con lo que esperan— para que el trabajador sepa qué espera y por qué.
    """
    runtime._exigir_operable()
    elegibles = {e["paquete"] for e in runtime.elegibles()}
    incompatibles = {i["paquete"]: i["incompatible_por"] for i in runtime.incompatibles_por_recurso()}
    libres, ajenos = [], []
    for fila in externos(runtime):
        if fila["paquete"] in incompatibles:
            # Directiva §68: listo, y temporalmente incompatible por un recurso exclusivo
            fila["incompatible_por"] = incompatibles[fila["paquete"]]
            fila["espera_a"] = sorted({c["lo_posee"] for c in incompatibles[fila["paquete"]]})
            ajenos.append(fila)
            continue
        if fila["estado"] in ("listo", "esperando-dependencia") and fila["paquete"] in elegibles:
            # `elegibles()` publica los `listo` sin mirar sus dependencias —las resuelve el
            # despacho—, pero un trabajador que tome uno con dependencias pendientes sólo
            # conseguiría mandarlo a `esperando-dependencia`. Aquí se dice la verdad: lo que
            # espera, espera, y se publica a quién.
            objeto = runtime._leer_paquete(fila["paquete"])
            pendientes, inviables = runtime._dependencias_pendientes(objeto)
            if pendientes or inviables:
                fila["espera_a"] = sorted(pendientes)
                fila["inviables"] = sorted(inviables)
                ajenos.append(fila)
                continue
            libres.append(fila)
        elif fila["estado"] in ("despachado", "ejecutando"):
            if fila["titular"] is None or fila["titular"] == runtime.instancia:
                libres.append(fila)
            else:
                ajenos.append(fila)
    orden = {e["paquete"]: n for n, e in enumerate(runtime.elegibles())}
    libres.sort(key=lambda f: (0 if f["estado"] in ("despachado", "ejecutando") else 1,
                               orden.get(f["paquete"], 10 ** 6), f["paquete"]))
    return {"tomables": libres, "esperando": ajenos}
