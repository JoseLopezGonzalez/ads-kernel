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
    identificador del contenido, se repite con la semántica de idempotencia del §9. La
    frase decía «retoma» y NO retomaba; hoy retoma, y lo que cuesta cada punto de corte
    está medido en la DECISIÓN sobre el MARCAR, más abajo.

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

`ADJ-B1` · LA MIGRACIÓN 0->1 NO RETOMABA, Y LA PRUEBA QUE LA CUBRÍA NO ENTRABA EN LA RAMA
-----------------------------------------------------------------------------------------
HECHO REPRODUCIDO ANTES DE CORREGIR, con su orden y su salida, sobre un almacén heredado
GENUINO —`estado/canonico/items/it-uno.json` y NADA MÁS: sin `FORMATO.json`, sin diario y
sin `REVISION.json`—:

    $ ads_estado.py --repo mig migrar
    Traceback (most recent call last):
      ...
      File ".../estado/migracion.py", line 178, in _migrar_0_a_1
        almacen._publicar_revision(revision_cero)
    TypeError: Almacen._publicar_revision() missing 1 required keyword-only argument:
               'testigo'
    EXIT=1     stdout VACÍO · SIETE rutas absolutas del anfitrión · CERO códigos tipados

    $ ads_estado.py --repo mig migrar        (2ª y 3ª llamada, idénticas)
    [ESTADO_CORRUPTO] el fichero no existe (estado/REVISION.json)
    EXIT=1

Y LO QUE HACÍA ESTO MAYOR QUE UNA LÍNEA, TAMBIÉN MEDIDO: con la línea ya corregida en una
copia, un almacén heredado NUEVO migraba (EXIT=0) y el almacén que ya había pasado por el
fallo seguía dando `ESTADO_CORRUPTO`. El daño no lo reparaba la corrección: la fundación
del diario y la publicación de la revisión 0 eran DOS actos, la guarda de la rama miraba el
PRIMERO —«¿hay `almacen.inicializado`?»— y el corte entre los dos dejaba un almacén al que
la rama de fundación ya no volvía a entrar nunca. Y la única cobertura,
`test_09_migracion_del_formato_heredado_cero_a_uno`, fabricaba el heredado con un
`os.remove(FORMATO.json)` sobre un almacén YA inicializado: ese almacén tiene diario y
tiene `REVISION.json`, así que la rama rota no se entraba y la prueba pasaba sobre un
camino que el código productivo no recorre.

DECISIÓN · la guarda de la fundación mira `REVISION.json`, no el evento del diario
    Alternativas: (a) poner el `testigo` y dejar la guarda como estaba; (b) hacer la
    fundación atómica metiéndola en una transacción; (c) que la condición de entrada sea el
    ESTADO OBSERVABLE que falta —`REVISION.json`— y que dentro se reconozca lo ya hecho.
    Se elige (c). Con (a) el defecto de hoy se cierra y el almacén roto de ayer queda
    inmigrable para siempre, que es la mitad que el adjudicador señaló. (b) no existe: la
    revisión 0 ES el punto de publicación, no puede publicarse dentro de una transacción
    que necesita una revisión base. Con (c) la rama es RE-ENTRABLE: se entra siempre que
    falte la revisión, y el evento del diario se anexa sólo si no está. Los dos órdenes de
    corte —evento sí/revisión no, y evento no/revisión no— convergen en el mismo estado.

DECISIÓN · la revisión 0 que se republica se RECOMPONE, y se contrasta con el diario
    Republicar «algo» que sirva para seguir sería inventar estado, y `g.8` lo prohíbe. La
    revisión 0 es una función pura de sus partes —`componer_revision(0, None, {}, tx0)`— y
    su `revision_id` está anotado en el `resultado` del evento de fundación. Se recompone y
    se EXIGE que coincida: si no coincide, el diario habla de otra fundación y la migración
    falla cerrado con `MIGRACION_NO_RECUPERABLE` en vez de publicar una revisión ajena.

DECISIÓN · sin `REVISION.json` y con diario POBLADO, se falla cerrado en vez de adivinar
    Un almacén sin revisión cuyo diario ya lleva transiciones no dice cuál era la vigente.
    Reconstruirla exigiría reproyectar el diario entero, que es justamente lo que `I-g7`
    proscribe («ninguna lectura del estado necesita reproyectar el diario»), y elegir una
    sería adivinar. Se levanta `MigracionNoRecuperable` nombrando cuántos eventos sobran.

DECISIÓN · la migración CIERRA la ventana de su propio intento anterior antes de aplicar
    `g.11` exige que una migración interrumpida «se detecte y se termine o se revierta», y
    el docstring de este módulo promete que «volver a llamar a `migrar()` retoma». Medido:
    no retomaba. `_aplicar_bajo_bloqueo` levanta `VENTANA_SIN_CERRAR` ante una transacción
    abierta, y el `migrar` siguiente moría ahí. Alternativas: (a) pedirle al operador que
    llame antes a `recuperar()`; (b) que la migración cierre la ventana ella misma.
    Se elige (b): (a) convierte una promesa del contrato en una nota de manual, y además
    `recuperar()` público exige `_exigir_operable()`, que un almacén heredado no pasa. Se
    llama a `_recuperar_bajo_bloqueo()`, que es el MISMO cierre de siempre —completar,
    revertir o marcar— bajo el bloqueo que la migración ya tiene tomado.

DECISIÓN · una migración ya aplicada se RECONOCE por su evento, y no se vuelve a aplicar
    Tras un corte entre la confirmación de la transacción y la escritura de `FORMATO.json`,
    el contenido ya está migrado. Recomputar la transacción daría una revisión NUEVA con el
    mismo contenido: una migración que se aplica dos veces, que es exactamente lo que
    `test_10` prohíbe. El reconocimiento se hace sobre `migracion.aplicada` —el evento que
    `g.11` obliga a anexar— y no sobre `FORMATO.json`, porque el fichero de formato es lo
    ÚLTIMO que se escribe y por tanto es la señal que falta precisamente aquí.

DECISIÓN · un corte ANTERIOR al punto de no retorno se cierra por MARCAR, y se dice
    MEDIDO sobre los DIEZ puntos de corte de `estado/fallos.py`, con un almacén heredado
    GENUINO y `ADS_ESTADO_FALLO`: los diez convergen en el MISMO `cid_raiz`
    `sha256:adc7cdb5…`, y siete de ellos con UNA sola llamada a `migrar()`. Los tres
    anteriores al punto de no retorno —`antes-de-escribir-temporal`,
    `despues-de-escribir-temporal` y `despues-de-sincronizar-temporal`— necesitan DOS: la
    primera cierra la ventana y sale con `RECUPERACION_MARCADA`, la segunda retoma.
    La causa es real y conviene nombrarla en vez de esconderla: la rama REVERTIR comprueba
    que nada de lo PUBLICADO se destruyó comparando `canonico/` con la raíz de la revisión
    base, y en un almacén heredado la revisión 0 tiene la raíz VACÍA mientras `canonico/`
    ya contiene los ficheros heredados. Esa diferencia no la produjo la transacción: es la
    forma que tiene un almacén de versión 0, y es exactamente lo que la migración existe
    para explicar.
    Alternativas consideradas y descartadas: (a) que la revisión 0 ADOPTE los `cid` de los
    bytes heredados, con lo que la reversión casaría —descartada porque `auditar` reproduce
    la raíz proyectando el diario desde `almacen.inicializado` con raíz VACÍA, y un `cid`
    adoptado ahí produciría `ESTADO_NO_EXPLICABLE` en toda auditoría posterior—; (b) relajar
    la comprobación de la rama REVERTIR cuando la base no declara la ruta —descartada
    porque esa comprobación existe para otro fallo, y ablandarla aquí la ablanda para
    todos—; (c) que la migración absorba el MARCAR y siga —descartada porque `g.8` reserva
    la salida de una transacción marcada a la autoridad, y absorberla sería decidirla—.
    Se elige decirlo: el corte queda MARCADO con su copia íntegra en
    `reconciliacion/conflictos/`, el error es TIPADO, y la llamada siguiente retoma con
    identificador propio. Ninguna de las tres deja el almacén inmigrable, y está medido.

DECISIÓN · el identificador deriva del contenido NORMALIZADO, y numera los intentos fallidos
    Dos correcciones de la misma idea. (1) El `cid` que se deriva es el del objeto tal como
    se va a ESCRIBIR —con su `esquema`, `Escritura.cid()`— y no el de los bytes heredados:
    de lo contrario, repetir la migración después de un corte POSTERIOR al paso 8 leería
    los objetos ya normalizados, derivaría otro identificador y la idempotencia del §9 no
    se aplicaría justo en el caso para el que existe. (2) Un intento que la recuperación
    REVIRTIÓ deja en el diario `transicion.revertida` con ese identificador, y reutilizarlo
    levanta `IdentificadorDuplicado`: el número de intentos cerrados sin confirmar entra en
    la carga derivada, de modo que el reintento tiene identificador propio. Sigue siendo
    una función del diario y del contenido —ni reloj ni azar—, así que `I-g3` se conserva.
"""
from __future__ import annotations

import os

from .errores import (
    ErrorDeEstado,
    MigracionDesconocida,
    MigracionNoRecuperable,
    VersionDesconocida,
)
from .serializacion import deserializar
from .transaccion import (
    Escritura,
    InformeMigracion,
    ResultadoTransicion,
    Transicion,
    identificador_derivado,
)

# El evento que funda el diario, y el que declara la migración hecha. Se nombran una vez:
# la re-entrada de la fundación y el reconocimiento de lo ya aplicado los comparan los dos,
# y dos literales sueltos acaban divergiendo en cuanto alguien renombra uno.
TIPO_DE_FUNDACION = "almacen.inicializado"
TIPO_DE_MIGRACION_APLICADA = "migracion.aplicada"
CLASE_DE_MIGRACION = "migracion"


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


def _fundacion_en(eventos):
    """El evento que funda el diario, o `None`. Es el ancla de la revisión 0."""
    for evento in eventos:
        if evento.get("tipo") == TIPO_DE_FUNDACION:
            return evento
    return None


def _asegurar_revision_cero(motor, almacen, disposicion, eventos):
    """Deja `REVISION.json` publicado, entre por donde entre. RE-ENTRABLE e idempotente.

    Es la corrección de `ADJ-B1`. Los cuatro estados posibles al llegar aquí, y qué hace
    con cada uno:

        diario vacío        · sin revisión   →  anexa la fundación Y publica la revisión 0
        fundación anexada   · sin revisión   →  NO reanexa; publica la revisión 0 que el
                                                propio evento declara. Es el estado que el
                                                corte de `ADJ-B1` dejaba, y el que antes
                                                era terminal
        fundación anexada   · con revisión   →  no toca nada
        diario CON HISTORIA · sin revisión   →  falla cerrado: no hay de dónde deducir cuál
                                                era la revisión vigente

    Devuelve `True` si publicó la revisión 0, para que quien llame pueda decirlo.
    """
    hay_revision = os.path.exists(disposicion.revision)
    fundacion = _fundacion_en(eventos)

    if hay_revision:
        if fundacion is None:
            raise MigracionNoRecuperable(
                "el almacén heredado ya tiene `REVISION.json` pero su diario no arranca "
                "en `" + TIPO_DE_FUNDACION + "`: no se puede reconstruir su historia, y "
                "`g.8` prohíbe inventar estado",
                ruta=disposicion.relativa(disposicion.revision),
            )
        return False

    sobrantes = [evento for evento in eventos
                 if evento.get("tipo") != TIPO_DE_FUNDACION]
    if sobrantes:
        raise MigracionNoRecuperable(
            "el almacén heredado no tiene `REVISION.json` y su diario ya lleva "
            + str(len(sobrantes)) + " evento(s) posteriores a la fundación: cuál era la "
            "revisión vigente no se deduce sin reproyectar el diario, que es lo que `I-g7` "
            "proscribe, y elegir una sería adivinar",
            ruta=disposicion.relativa(disposicion.revision),
            eventos_sobrantes=len(sobrantes),
        )

    # `diario_secuencia` sale del evento cuando el evento ya está: es SU secuencia la que
    # la revisión publicada tiene que nombrar, y darla por 1 sería suponer que nadie anexó
    # nada antes. En un diario recién creado el primer anexado es, en efecto, el 1.
    secuencia = int(fundacion["secuencia"]) if fundacion else 1
    transaccion_cero = identificador_derivado(
        0, {"tipo": TIPO_DE_FUNDACION, "revision": 0}
    )
    revision_cero = motor.componer_revision(
        0, None, {}, transaccion_cero, diario_secuencia=secuencia
    )
    if fundacion is None:
        almacen._diario.anexar(
            TIPO_DE_FUNDACION,
            transaccion=transaccion_cero, base=None,
            resultado=revision_cero["revision_id"], operaciones=[],
            autor=motor.AUTOR_RUNTIME,
            motivo="fundación del diario durante la migración 0->1",
        )
    elif fundacion.get("resultado") != revision_cero["revision_id"]:
        raise MigracionNoRecuperable(
            "el diario arranca en `" + TIPO_DE_FUNDACION + "` pero el `resultado` que "
            "declara no es la revisión 0 que este motor recompone: publicar la recompuesta "
            "sustituiría la historia del almacén por otra",
            ruta=disposicion.relativa(disposicion.revision),
            esperado=fundacion.get("resultado"),
            encontrado=revision_cero["revision_id"],
        )
    # `E-08` · el testigo NO tiene valor por defecto, y la fundación no publica ningún
    # objeto: su plan está vacío y por tanto no hay paso 8 que testificar. Se pasa el
    # testigo DECLARADO de fundación, que es el mismo que usa `motor.inicializar`. Ésta es
    # la línea que `ADJ-B1` encontró sin argumento, y la única de las cinco del árbol que
    # no lo pasaba.
    almacen._publicar_revision(revision_cero, testigo=motor.TESTIGO_DE_FUNDACION)
    return True


def _cerrar_ventana_de_un_intento_anterior(almacen):
    """`g.11`: una migración interrumpida se TERMINA o se REVIERTE antes de reintentarla.

    Se usa `_recuperar_bajo_bloqueo` y no `recuperar()` porque el bloqueo de escritor ya lo
    tiene tomado la migración, y porque `recuperar()` empieza por `_exigir_operable()`, que
    un almacén heredado —el nuestro— nunca pasa. Es el mismo cierre de ventana de siempre:
    no hay un segundo motor de recuperación para las migraciones, que es justo lo que la
    primera DECISIÓN de este módulo se comprometió a no escribir.
    """
    if not almacen._hay_ventana_que_cerrar():
        return None
    return almacen._recuperar_bajo_bloqueo()


def _migracion_aplicada_en(eventos):
    """El evento `migracion.aplicada` de una 0->1 ya hecha, o `None`."""
    for evento in reversed(eventos):
        if evento.get("tipo") == TIPO_DE_MIGRACION_APLICADA \
                and evento.get("desde") == 0 and evento.get("hasta") == 1:
            return evento
    return None


def _intentos_cerrados_sin_confirmar(eventos):
    """Cuántas migraciones se abrieron y se cerraron SIN confirmar, según el diario.

    Es lo que distingue el identificador de un reintento del de la tentativa que la
    recuperación revirtió: reutilizar aquél levantaría `IdentificadorDuplicado` y la
    migración quedaría bloqueada por su propio intento anterior. El número sale del DIARIO,
    así que sigue siendo una función del estado y no de un reloj ni de un contador vivo.
    """
    de_migracion = {
        evento.get("transaccion") for evento in eventos
        if evento.get("tipo") in ("transicion.abierta", "transicion.preparada")
        and evento.get("clase") == CLASE_DE_MIGRACION
    }
    cerradas_sin_confirmar = {
        evento.get("transaccion") for evento in eventos
        if evento.get("tipo") in ("transicion.revertida", "transicion.marcada")
    }
    return len(de_migracion & cerradas_sin_confirmar)


def _resultado_de_una_migracion_ya_hecha(almacen, aplicada, eventos):
    """El informe de una migración que el diario ya declara aplicada. No reescribe nada."""
    revision = almacen._leer_revision()
    operaciones = []
    for evento in eventos:
        if evento.get("tipo") == "transicion.confirmada" \
                and evento.get("transaccion") == aplicada.get("transaccion"):
            operaciones = list(evento.get("operaciones") or [])
            break
    return ResultadoTransicion(
        transaccion=aplicada.get("transaccion"),
        revision=revision["revision"],
        revision_id=revision["revision_id"],
        padre=revision["padre"],
        cid_raiz=revision["cid_raiz"],
        diario_secuencia=revision["diario_secuencia"],
        operaciones=operaciones,
        repetida=True,
    )


def _declarar_el_formato(motor, disposicion):
    """El ÚLTIMO byte de la migración. Hasta aquí el almacén es heredado a ojos de `abrir`."""
    motor.escribir_y_sincronizar(
        disposicion.formato, motor.serializar_canonico(motor._contenido_formato())
    )
    motor.sincronizar_directorio(disposicion.almacen)


def _migrar_0_a_1(almacen):
    """Formato heredado (sin `FORMATO.json`) → formato 1, como transacción auditable.

    Los cuatro pasos, en este orden y por esta razón: se funda lo que falte, se cierra la
    ventana que un intento anterior dejara abierta, se reconoce lo ya aplicado, y sólo
    entonces se aplica. Cada uno es idempotente por separado, así que la secuencia entera
    lo es, y ése es el contenido operativo de «volver a llamar a `migrar()` retoma».
    """
    from . import motor                      # tardío: el motor importa este módulo

    disposicion = almacen._d

    bloqueo = motor.BloqueoExclusivo(disposicion.bloqueo_escritor, "escritor")
    bloqueo.adquirir(intentos=10)
    try:
        motor._fundar_estructura_sin_formato(disposicion)
        almacen._diario.crear()
        almacen._registro.crear()

        # Paso 1 · la revisión 0. Con `tolerar_cola`: un corte a mitad de anexado deja una
        # línea desgarrada, y quien la descarta es la recuperación del paso 2, no esto.
        _asegurar_revision_cero(
            motor, almacen, disposicion, almacen._diario.eventos(tolerar_cola=True)
        )

        # Paso 2 · la ventana de un intento anterior. Puede publicar la revisión y anexar
        # `migracion.aplicada` por la rama COMPLETAR, y por eso va ANTES del paso 3.
        _cerrar_ventana_de_un_intento_anterior(almacen)

        # Paso 3 · lo ya hecho se reconoce y se salta.
        eventos = almacen._diario.eventos()
        aplicada = _migracion_aplicada_en(eventos)
        if aplicada is not None:
            resultado = _resultado_de_una_migracion_ya_hecha(almacen, aplicada, eventos)
            _declarar_el_formato(motor, disposicion)
            almacen.heredado = False
            return resultado

        # Paso 4 · la migración propiamente dicha. Los objetos se leen AQUÍ y no antes del
        # bloqueo: la recuperación del paso 2 puede haber publicado en `canonico/` los
        # objetos ya normalizados, y leerlos antes daría una foto que ya no es la del
        # árbol sobre el que se va a escribir.
        objetos = _leer_objetos_heredados(motor, almacen)
        escrituras = [Escritura(ruta, contenido) for ruta, contenido in objetos]
        base = almacen._leer_revision()
        # El identificador deriva del CONTENIDO NORMALIZADO —el que de verdad se escribe—,
        # de modo que repetir la migración tras un corte posterior al paso 8 produce el
        # MISMO identificador y con él la idempotencia del §9. `intento` sólo aparece
        # cuando lo hay: sin él, el primer intento conserva el identificador histórico.
        carga = {
            "tipo": CLASE_DE_MIGRACION, "desde": 0, "hasta": 1,
            "objetos": [[escritura.ruta, escritura.cid()] for escritura in escrituras],
        }
        intentos = _intentos_cerrados_sin_confirmar(eventos)
        if intentos:
            carga["intento"] = intentos
        transaccion = identificador_derivado(base["revision"] + 1, carga)
        transicion = Transicion(
            tipo=CLASE_DE_MIGRACION,
            base=base["revision_id"],
            operaciones=escrituras,
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
        _declarar_el_formato(motor, disposicion)
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
