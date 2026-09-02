#!/usr/bin/env python3
"""migracion — migraciones REGISTRADAS y explícitas (`g.10`, `g.11`).

`g.11` no deja margen: toda migración es EXPLÍCITA, declarada y auditable, y **no hay
migración implícita al leer**. Este módulo es el registro de las que existen, y el §5 del
contrato exige que exista **la del formato 0 al 1** —el almacén heredado, sin
`FORMATO.json`— para que la compatibilidad sea demostrable y no una promesa.

DECISIÓN · una migración es una TRANSACCIÓN normal, no un procedimiento aparte
    Alternativas: (a) un procedimiento propio que reescribe el árbol y luego anota que
    migró; (b) el mismo protocolo del §3, con su `abierta`/`preparada`/`confirmada`, más un
    evento `migracion.aplicada` dentro de la misma transacción.
    Se elige (b). `g.11` exige que una migración sea RECUPERABLE: interrumpida, se detecta y
    se termina o se revierte. Con (a) habría que escribir un segundo motor de recuperación
    para las migraciones, y el segundo motor es el que nunca se prueba. Con (b) una
    migración cortada por la mitad la cierra exactamente el mismo `recuperar()` que cierra
    cualquier otra transacción, y su auditoría es la auditoría de siempre.

DECISIÓN · `FORMATO.json` se escribe EL ÚLTIMO
    Alternativas: (a) marcar el formato nuevo al empezar; (b) marcarlo al terminar.
    Se elige (b). `FORMATO.json` es la única señal por la que `abrir` distingue un almacén
    heredado de uno vigente. Con (a), un corte a mitad de migración dejaría un almacén que
    se presenta como formato 1 con la mitad del contenido fuera de `raiz`, y la verificación
    lo leería como estado no explicable por el diario. Con (b), un corte deja el almacén
    exactamente donde estaba a ojos de `abrir` —heredado—, y volver a llamar a `migrar()`
    retoma: los pasos ya hechos se reconocen y se saltan, y la transacción, que deriva su
    identificador del contenido, se repite con la semántica de idempotencia del §9.

DECISIÓN · la migración 0→1 REESCRIBE los ficheros heredados, no los adopta tal cual
    Alternativas: (a) calcular el `cid` de los bytes heredados y adoptarlos; (b) volver a
    serializarlos en forma canónica y publicarlos por el protocolo.
    Se elige (b). Un fichero heredado puede venir con otro orden de claves, otra
    indentación o sin `esquema`. Adoptarlo tal cual metería en `raiz` un `cid` que ninguna
    escritura futura podría reproducir, y `I-g3` —mismo estado, bytes idénticos— quedaría
    roto desde el primer día. Reescribirlos cuesta una pasada y deja el árbol en la única
    forma que el motor sabe reproducir.

DECISIÓN · no existe migración DESCENDENTE, y se dice en vez de simularla
    Bajar de versión exigiría descartar información que la versión alta puede tener y la
    baja no. `g.10` obliga a fallar cerrado ante lo que no se entiende; inventar una bajada
    sería justo lo contrario. `migrar(a_version)` hacia atrás levanta `MigracionDesconocida`.
"""
from __future__ import annotations

import os

from .errores import (
    ErrorDeEstado,
    MigracionDesconocida,
    MigracionNoRecuperable,
    VersionDesconocida,
)
from .serializacion import cid_de_objeto, deserializar
from .transaccion import (
    Escritura,
    InformeMigracion,
    Transicion,
    identificador_derivado,
)


def migrar(almacen, a_version):
    """Aplica en cadena las migraciones registradas hasta `a_version`. Sin adivinar nada."""
    if not isinstance(a_version, int) or isinstance(a_version, bool):
        raise MigracionDesconocida(
            "la versión de destino es un entero; se recibió " + repr(a_version)
        )
    desde = almacen.version_de_formato()
    if a_version == desde:
        return InformeMigracion(ok=True, desde=desde, hasta=desde)
    if a_version < desde:
        raise MigracionDesconocida(
            "no hay migración descendente registrada de " + str(desde) + " a "
            + str(a_version) + "; bajar de versión descartaría información y `g.10` "
            "prohíbe adivinar",
            desde=desde, hasta=a_version,
        )
    cadena = []
    actual = desde
    while actual < a_version:
        paso = (actual, actual + 1)
        if paso not in MIGRACIONES:
            raise MigracionDesconocida(
                "no hay migración registrada de " + str(paso[0]) + " a " + str(paso[1])
                + "; migraciones registradas: "
                + ", ".join(str(a) + "->" + str(b) for a, b in sorted(MIGRACIONES)),
                desde=paso[0], hasta=paso[1],
            )
        cadena.append((paso, MIGRACIONES[paso]))
        actual += 1

    aplicadas = []
    transacciones = []
    for paso, funcion in cadena:
        resultado = funcion(almacen)
        aplicadas.append({
            "desde": paso[0], "hasta": paso[1],
            "transaccion": resultado.transaccion,
            "objetos": len(resultado.operaciones),
            "repetida": resultado.repetida,
        })
        transacciones.append(resultado.transaccion)
    return InformeMigracion(
        ok=True, desde=desde, hasta=a_version, aplicadas=aplicadas,
        transacciones=transacciones,
    )


def _leer_objetos_heredados(motor, almacen):
    """Los objetos del almacén heredado, normalizados. Falla cerrado si alguno no encaja."""
    disposicion = almacen._d
    objetos = []
    try:
        rutas = motor.recorrer_canonico(disposicion.canonico)
    except ErrorDeEstado as exc:  # ya viene tipado; aquí sólo se recontextualiza el porqué
        raise MigracionNoRecuperable(
            "el árbol heredado no tiene la forma `canonico/<dominio>/<id>.json`: "
            + str(exc),
            ruta=disposicion.relativa(disposicion.canonico),
        ) from exc
    for ruta in rutas:
        fisica = os.path.join(disposicion.canonico, *ruta.split("/"))
        datos = motor.leer_bytes(fisica, error=MigracionNoRecuperable)
        contenido = deserializar(datos, ruta=ruta, error=MigracionNoRecuperable)
        if not isinstance(contenido, dict):
            raise MigracionNoRecuperable(
                "un objeto heredado no es un mapa JSON y no se puede versionar", ruta=ruta
            )
        declarado = contenido.get("esquema")
        if declarado is not None and declarado != "ads.estado/1":
            # Un objeto heredado que YA declara otra versión no es un objeto de formato 0:
            # es un objeto de una versión que este motor no entiende, y `g.10` manda fallar.
            raise VersionDesconocida(
                "un objeto heredado declara " + repr(declarado) + ", que este motor no "
                "entiende; la migración 0->1 sólo trata objetos sin versión declarada",
                ruta=ruta,
            )
        objetos.append((ruta, contenido))
    return objetos


def _migrar_0_a_1(almacen):
    """Formato heredado (sin `FORMATO.json`) → formato 1, como transacción auditable."""
    from . import motor                      # tardío: el motor importa este módulo

    disposicion = almacen._d
    objetos = _leer_objetos_heredados(motor, almacen)

    bloqueo = motor.BloqueoExclusivo(disposicion.bloqueo_escritor, "escritor")
    bloqueo.adquirir(intentos=10)
    try:
        motor._fundar_estructura_sin_formato(disposicion)
        almacen._diario.crear()
        almacen._registro.crear()

        eventos = almacen._diario.eventos(tolerar_cola=True)
        if not any(evento["tipo"] == "almacen.inicializado" for evento in eventos):
            if os.path.exists(disposicion.revision):
                raise MigracionNoRecuperable(
                    "el almacén heredado ya tiene `REVISION.json` pero su diario no "
                    "arranca en `almacen.inicializado`: no se puede reconstruir su "
                    "historia, y `g.8` prohíbe inventar estado",
                    ruta=disposicion.relativa(disposicion.revision),
                )
            transaccion_cero = identificador_derivado(
                0, {"tipo": "almacen.inicializado", "revision": 0}
            )
            revision_cero = motor.componer_revision(
                0, None, {}, transaccion_cero, diario_secuencia=1
            )
            almacen._diario.anexar(
                "almacen.inicializado",
                transaccion=transaccion_cero, base=None,
                resultado=revision_cero["revision_id"], operaciones=[],
                autor=motor.AUTOR_RUNTIME,
                motivo="fundación del diario durante la migración 0->1",
            )
            almacen._publicar_revision(revision_cero)

        base = almacen._leer_revision()
        # El identificador deriva del CONTENIDO migrado (`I-g3`): repetir la migración tras
        # un corte produce el MISMO identificador, y con él la idempotencia del §9.
        transaccion = identificador_derivado(base["revision"] + 1, {
            "tipo": "migracion", "desde": 0, "hasta": 1,
            "objetos": [[ruta, cid_de_objeto(contenido)] for ruta, contenido in objetos],
        })
        transicion = Transicion(
            tipo="migracion",
            base=base["revision_id"],
            operaciones=[Escritura(ruta, contenido) for ruta, contenido in objetos],
            autor=motor.AUTOR_RUNTIME,
            motivo="migración registrada del formato 0 al 1",
            id=transaccion,
        )
        resultado = almacen._aplicar_bajo_bloqueo(transicion, {
            "migracion": {"desde": 0, "hasta": 1,
                          "motivo": "migración registrada del formato 0 al 1"}
        })
        # `FORMATO.json` EL ÚLTIMO: hasta este byte el almacén sigue siendo heredado a ojos
        # de `abrir`, y por eso un corte anterior es retomable en vez de irrecuperable.
        motor.escribir_y_sincronizar(
            disposicion.formato, motor.serializar_canonico(motor._contenido_formato())
        )
        motor.sincronizar_directorio(disposicion.almacen)
        almacen.heredado = False
        return resultado
    finally:
        bloqueo.liberar()


# El registro. Es explícito y se lee de un vistazo: `g.11` exige que las migraciones estén
# DECLARADAS, y una tabla que se rellena por descubrimiento automático no está declarada.
MIGRACIONES = {
    (0, 1): _migrar_0_a_1,
}


def registradas():
    """Censo de migraciones, para que una prueba compruebe que la 0->1 existe de verdad."""
    return sorted(MIGRACIONES)
