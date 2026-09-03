#!/usr/bin/env python3
"""fase0 — UN SOLO CONTRATO, INVOCADO CUATRO VECES. `gate:sistema-conforme` y su soporte.

    «UN SOLO CONTRATO, INVOCADO CUATRO VECES. Es la regla 6 de `O17`: los cuatro
     macrocircuitos invocan el MISMO contrato y el MISMO mecanismo compartido, y no se
     crean cuatro implementaciones divergentes.»                                 `§9.6`

Este módulo es ese mecanismo. Cubre lo que `§9.6` enumera como contenido de la fase:
encuadre · identidad del producto · control repo · repositorios · perfil · política · estado
durable · recuperación · precondiciones · autoridad · decisión de entrada.

LOS SEIS IDENTIFICADORES DEL SUJETO (regla 7, y son un MÍNIMO):

    1 producto o instalación
    2 ejecución del macrocircuito · ACUÑADO POR HUELLA del disparador y de los otros cinco.
      NO consume contador, NO abre iniciativa, NO escribe canónico
    3 revisión del kernel
    4 revisión de esquemas y contratos APLICABLES
    5 configuración y fuentes relevantes
    6 huella de la evidencia

DECISIÓN · el identificador nº 2 se calcula DESPUÉS de los otros cinco, y por eso es huella
    `§9.6` lo escribe así: «lo ACUÑA la propia `FASE 0`, y es la HUELLA de su disparador
    junto con los otros cinco identificadores de este sujeto». Se implementa literalmente:
    se resuelven 1, 3, 4, 5 y 6, y sólo entonces se deriva 2. Un identificador monotónico
    —`INI-002`— exigiría un contador, y consumir un contador es mutar estado: `X-S10` lo
    prueba. Direccionado por contenido, repetir la `FASE 0` sobre el mismo disparador
    produce **la misma** declaración, que es lo que conserva la regla 1 —«ni cero ni dos»—
    cuando el chat se agota dentro de la fase.

DECISIÓN · el SOPORTE DURABLE DE LA FASE 0 es propio, ANTERIOR a `estado/`, y ESCRIBE UNA VEZ
    Alternativas: (a) escribir la declaración en `estado/`; (b) no escribirla y recalcularla;
    (c) un soporte propio, anterior a `estado/`, direccionado por contenido.
    Se elige (c), que es lo que `§9.6` manda. (a) es imposible y `X-S11` lo prueba: `estado/`
    nace en `INS-0`/`A0`/`M0`/`U0`, DESPUÉS de esta fase. (b) haría que «una por ejecución»
    fuera indemostrable: no habría nada que contar. (c) da un soporte que contiene **la
    declaración, su dosier y su celda, y NADA del macrocircuito**, y por eso un bloqueo del
    gate «no deja nada que deshacer»: la frontera no es «no escribir nada», es **no escribir
    nada DEL MACROCIRCUITO**.
    Y no es un segundo sistema de estado: es INMUTABLE y direccionado por contenido. Se
    escribe una vez; escribir lo mismo otra vez produce los MISMOS bytes en la MISMA ruta, y
    escribir algo distinto bajo el mismo sujeto es `DosDeclaraciones`. No tiene diario, no
    tiene revisiones, no tiene transiciones y no admite mutación. `I-g4` sigue entero: el
    único ejecutor de mutaciones CANÓNICAS sigue siendo el `Almacen`, y aquí no hay estado
    canónico del macrocircuito.

DECISIÓN · INCORPORAR no es CERTIFICAR, y la huella tiene que ser IDÉNTICA
    «la PRIMERA fase que crea `estado/` INCORPORA la declaración a `estado/cobertura/` como
    su primer acto, sin reemitirla y sin volver a certificar. Si la huella incorporada no es
    idéntica a la emitida es OTRO sujeto, y la regla 8 lo rechaza». `incorporar()` compara
    huella a huella y levanta `IncorporacionInvalida` ante cualquier diferencia.
"""
from __future__ import annotations

import hashlib
import json
import os

from ciclo import durable
from ciclo.corpus import Corpus
from ciclo.encuadre import cargar_perfil, cargar_politica, descubrir_fuentes, \
    identificar_producto
from ciclo.gates import NO_SUPERADO, SUPERADO
from estado.serializacion import cid_de_objeto, serializar_canonico

from .errores import (
    BloqueoDeSeguridad,
    CertificacionCopiada,
    DosDeclaraciones,
    Fase0Omitida,
    IncorporacionInvalida,
    IniciativaPrematura,
    MutacionAntesDelGate,
    NivelNoAlcanzable,
    ProductorIndebido,
    ReutilizacionInvalida,
    SujetoIncompleto,
)

# El soporte propio. Cuelga del control repo y NO de `estado/`, que todavía no existe.
SOPORTE = "fase0"
DECLARACION = "declaracion.json"
DOSIER = "dosier.json"
CELDA = "celda.json"

DOMINIO_COBERTURA = "cobertura"
GATE = "gate:sistema-conforme"

PRODUCTOR = "SIS"                 # productor y propietario de la declaración
VERIFICADOR = "VER"               # el dosier, SIN apropiarse de la decisión
MAQUINARIA = "PLT"                # cuando el contrato se la atribuya
BLOQUEO = "SEG"                   # el bloqueo que nadie levanta
NO_PARTICIPA = "ENC"              # la FASE 0 es anterior a que haya ruta

NIVEL = "estructural"
ASPECTO = "aspecto:certificacion/estructural"
VERIFICADO = "verificado"

# Los SEIS identificadores, en su orden y con su nombre. Es un MÍNIMO: falta uno y FALLA
# nombrándolo; sobran, y se conservan.
IDENTIFICADORES = (
    "producto_o_instalacion",
    "ejecucion_del_macrocircuito",
    "revision_del_kernel",
    "revision_de_esquemas_y_contratos",
    "configuracion_y_fuentes",
    "huella_de_la_evidencia",
)

# Los niveles que `§9.2` presupone sobre Estructural. Elevarse a cualquiera de ellos sin
# Estructural vigente DE ESA EJECUCIÓN es `X-S4`.
NIVELES_SUPERIORES = ("operativa", "integrada", "completa")


# ===========================================================================
#  el SUJETO
# ===========================================================================
def revision_del_kernel(raiz_kernel=None):
    """Huella del kernel operativo EJECUTABLE: `runtime/`, sin el corpus documental."""
    raiz = os.path.abspath(raiz_kernel or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), ".."))
    digestor = hashlib.sha256()
    for directorio, subdirectorios, ficheros in os.walk(raiz):
        subdirectorios[:] = sorted(
            d for d in subdirectorios if d not in ("__pycache__", ".git", "pruebas")
        )
        for nombre in sorted(ficheros):
            if not nombre.endswith(".py") and not nombre.endswith(".yml"):
                continue
            absoluta = os.path.join(directorio, nombre)
            relativa = os.path.relpath(absoluta, raiz).replace(os.sep, "/")
            digestor.update(relativa.encode("utf-8"))
            digestor.update(b"\0")
            with open(absoluta, "rb") as manejador:
                digestor.update(hashlib.sha256(manejador.read()).digest())
    return "sha256:" + digestor.hexdigest()


def resolver_sujeto(ruta_control_repo, *, disparador, corpus=None, evidencia=(),
                    raiz_kernel=None):
    """Los SEIS identificadores. El nº 2 se acuña por HUELLA, el ÚLTIMO y de los otros cinco."""
    corpus = corpus or Corpus()
    if not str(disparador or "").strip():
        raise SujetoIncompleto(
            "la `FASE 0` se acuña sobre un DISPARADOR y no se ha declarado ninguno",
            falta="disparador",
        )
    fuentes = descubrir_fuentes(ruta_control_repo)
    perfil = cargar_perfil(ruta_control_repo)
    politica = cargar_politica()
    sujeto = {
        "producto_o_instalacion": "instalacion:transversal/"
                                  + identificar_producto(ruta_control_repo),
        "revision_del_kernel": revision_del_kernel(raiz_kernel),
        "revision_de_esquemas_y_contratos": corpus.huella(),
        "configuracion_y_fuentes": cid_de_objeto({
            "fuentes": fuentes, "perfil": perfil, "politica": politica,
        }),
        "huella_de_la_evidencia": cid_de_objeto(
            [str(pieza) for pieza in sorted(evidencia)]
        ),
    }
    # nº 2, EL ÚLTIMO: la huella del disparador junto con los otros cinco. Direccionado por
    # contenido, no monotónico, sin contador y sin abrir nada.
    sujeto["ejecucion_del_macrocircuito"] = "ejec-" + cid_de_objeto({
        "disparador": str(disparador),
        **{clave: sujeto[clave] for clave in sorted(sujeto)},
    }).split(":", 1)[-1][:24]
    exigir_sujeto_completo(sujeto)
    return sujeto


def exigir_sujeto_completo(sujeto):
    """`X-S9`: falta uno de los seis y FALLA NOMBRÁNDOLO. La regla 7 es un MÍNIMO."""
    if not isinstance(sujeto, dict):
        raise SujetoIncompleto("el sujeto es un mapa con los seis identificadores")
    for identificador in IDENTIFICADORES:
        if not str(sujeto.get(identificador) or "").strip():
            raise SujetoIncompleto(
                "al sujeto le falta el identificador `" + identificador + "`; la regla 7 "
                "es un mínimo y omitir uno es un fallo del gate, no una simplificación",
                falta=identificador,
            )
    return sujeto


def huella_del_sujeto(sujeto):
    exigir_sujeto_completo(sujeto)
    return cid_de_objeto({clave: sujeto[clave] for clave in IDENTIFICADORES})


# ===========================================================================
#  REUTILIZACIÓN de evidencia — reglas 8, 9 y 10
# ===========================================================================
def reutilizar_evidencia(sujeto_anterior, sujeto):
    """`X-S3`: una sola huella distinta invalida la reutilización, y se nombra cuál."""
    exigir_sujeto_completo(sujeto)
    exigir_sujeto_completo(sujeto_anterior)
    distintos = [
        identificador for identificador in IDENTIFICADORES
        # El nº 2 identifica la EJECUCIÓN y por definición cambia entre dos ejecuciones: no
        # se compara. Lo que la regla 8 exige idéntico son las ENTRADAS y sus huellas.
        if identificador != "ejecucion_del_macrocircuito"
        and sujeto_anterior.get(identificador) != sujeto.get(identificador)
    ]
    if distintos:
        raise ReutilizacionInvalida(
            "no hay reutilización: difiere(n) " + ", ".join(distintos)
            + ". La regla 8 exige que TODAS las entradas y huellas sigan idénticas, y una "
            "basta para invalidarla; la evidencia se REPRODUCE",
            difieren=distintos,
        )
    return {"reutilizable": True, "comparados": [
        i for i in IDENTIFICADORES if i != "ejecucion_del_macrocircuito"
    ]}


# ===========================================================================
#  el soporte durable de la FASE 0
# ===========================================================================
def directorio_del_soporte(ruta_control_repo, sujeto):
    """`<control_repo>/fase0/<ejecucion>/`. Fuera de `estado/`, y ANTERIOR a él."""
    exigir_sujeto_completo(sujeto)
    return os.path.join(ruta_control_repo, SOPORTE, sujeto["ejecucion_del_macrocircuito"])


def _publicar(ruta, cuerpo):
    """Escribe bytes canónicos con `fsync`, y sólo si no estaban ya escritos IGUALES."""
    datos = serializar_canonico(cuerpo)
    if os.path.exists(ruta):
        with open(ruta, "rb") as manejador:
            if manejador.read() == datos:
                return False
        raise DosDeclaraciones(
            "ya hay un artefacto DISTINTO para esta ejecución en el soporte de la `FASE 0`; "
            "la regla 1 fija exactamente una declaración por ejecución: dos son dos "
            "verdades sobre el mismo hecho",
            ruta=ruta,
        )
    temporal = ruta + ".tmp"
    with open(temporal, "wb") as manejador:
        manejador.write(datos)
        manejador.flush()
        os.fsync(manejador.fileno())
    os.replace(temporal, ruta)
    descriptor = os.open(os.path.dirname(ruta), os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    return True


def leer_declaracion(ruta_control_repo, sujeto):
    ruta = os.path.join(directorio_del_soporte(ruta_control_repo, sujeto), DECLARACION)
    if not os.path.isfile(ruta):
        return None
    with open(ruta, "r", encoding="utf-8") as manejador:
        return json.load(manejador)


def declaraciones_del_soporte(ruta_control_repo):
    """Todas las ejecuciones que dejaron declaración. Se leen; no se recuerdan."""
    raiz = os.path.join(ruta_control_repo, SOPORTE)
    if not os.path.isdir(raiz):
        return []
    salida = []
    for nombre in sorted(os.listdir(raiz)):
        ruta = os.path.join(raiz, nombre, DECLARACION)
        if os.path.isfile(ruta):
            with open(ruta, "r", encoding="utf-8") as manejador:
                salida.append(json.load(manejador))
    return salida


# ===========================================================================
#  `gate:sistema-conforme`
# ===========================================================================
def ejecutar(ruta_control_repo, *, macrocircuito, disparador, corpus=None,
             comprobaciones_superadas=(), evidencia=(), bloqueo_de_seg=None,
             productor=PRODUCTOR, dosier_de=VERIFICADOR, raiz_kernel=None,
             sujeto_anterior=None):
    """La `FASE 0` entera: sujeto, dosier, gate y declaración. CERO mutaciones canónicas.

    Devuelve `{sujeto, dosier, declaracion, celda, dictamen}`. Si el gate no se supera,
    levanta el error tipado que corresponde y **no escribe nada del macrocircuito**.
    """
    corpus = corpus or Corpus()
    # `X-S7`, primera mitad: el propietario del macrocircuito NO puede sustituir a `SIS`.
    if productor != PRODUCTOR:
        raise ProductorIndebido(
            "la declaración Estructural la emite `" + PRODUCTOR + "` y responde de ella; `"
            + str(productor) + "` no puede sustituirla. En `U5b` el propietario global es `"
            + MAQUINARIA + "`, y `" + MAQUINARIA + "` no certifica: EXIGE",
            productor=str(productor), macrocircuito=str(macrocircuito),
        )
    if dosier_de != VERIFICADOR:
        raise ProductorIndebido(
            "el dosier lo produce `" + VERIFICADOR + "`, que verifica y NO certifica",
            dosier=str(dosier_de),
        )
    # `X-S10`: resolver el sujeto NO abre iniciativa y NO consume contador. Se comprueba
    # ANTES y DESPUÉS, porque la afirmación es sobre lo que la fase hace, no sobre lo que
    # promete: si `estado/` existiera ya, esta fase estaría corriendo fuera de su sitio.
    habia_estado = os.path.isdir(os.path.join(ruta_control_repo, "estado"))
    sujeto = resolver_sujeto(
        ruta_control_repo, disparador=disparador, corpus=corpus, evidencia=evidencia,
        raiz_kernel=raiz_kernel,
    )
    if os.path.isdir(os.path.join(ruta_control_repo, "estado")) and not habia_estado:
        raise IniciativaPrematura(
            "resolver el sujeto de la `FASE 0` creó `estado/`: el identificador nº 2 se "
            "ACUÑA POR HUELLA, sin abrir nada y sin consumir contador",
            ruta="estado",
        )

    reutilizacion = None
    if sujeto_anterior is not None:
        reutilizacion = reutilizar_evidencia(sujeto_anterior, sujeto)

    # El DOSIER de `VER`: verifica y no se apropia de la decisión.
    dosier = {
        "esquema": "ads.estado/1",
        "productor": VERIFICADOR,
        "sujeto": dict(sujeto),
        "evidencia": sorted(str(pieza) for pieza in evidencia),
        "comprobaciones_declaradas": sorted(str(c) for c in comprobaciones_superadas),
        "reutilizacion": reutilizacion,
        "nota": "`VER` verifica y NO certifica: la decisión final es de `" + PRODUCTOR + "`",
    }
    dosier["huella"] = cid_de_objeto(dosier)

    # El GATE. `SEG` primero: su veto no lo levanta nadie, tampoco un dictamen positivo.
    if bloqueo_de_seg:
        raise BloqueoDeSeguridad(
            "`" + BLOQUEO + "` bloquea por incumplimiento de seguridad de la estructura: "
            + str(bloqueo_de_seg) + ". Su veto no lo levantan `" + PRODUCTOR + "`, `"
            + VERIFICADOR + "`, `" + MAQUINARIA + "` ni el propietario del macrocircuito",
            macrocircuito=str(macrocircuito),
        )
    from ciclo import gates as modulo_gates
    dictamen = modulo_gates.aplicar(
        GATE, corpus=corpus,
        entrada={"macrocircuito": str(macrocircuito), "disparador": str(disparador),
                 "sujeto": dict(sujeto), "mutaciones_canonicas": 0},
        evidencia=[str(pieza) for pieza in modulo_gates.gate(GATE, corpus=corpus)["evidencia"]],
        revisor=VERIFICADOR, autor=PRODUCTOR,
        comprobaciones_superadas=comprobaciones_superadas,
        salida="la declaración Estructural de ESTA ejecución",
    )

    declaracion = {
        "esquema": "ads.estado/1",
        "nivel": NIVEL,
        "aspecto": ASPECTO,
        "macrocircuito": str(macrocircuito),
        "productor": PRODUCTOR,
        "dosier_de": VERIFICADOR,
        "sujeto": dict(sujeto),
        "huella_del_sujeto": huella_del_sujeto(sujeto),
        "dosier": dosier["huella"],
        "dictamen": dictamen["dictamen"],
        "gate": GATE,
        "hereda": False,
        "reutilizo_evidencia": bool(reutilizacion),
    }
    declaracion["id"] = "dec-" + cid_de_objeto(declaracion).split(":", 1)[-1][:16]

    celda = {
        "esquema": "ads.estado/1",
        "id": "cel-" + cid_de_objeto({
            "aspecto": ASPECTO, "sujeto": huella_del_sujeto(sujeto),
        }).split(":", 1)[-1][:16],
        "aspecto": ASPECTO,
        "estado": VERIFICADO,
        "sujeto": dict(sujeto),
        "huella_del_sujeto": huella_del_sujeto(sujeto),
        "declaracion": declaracion["id"],
        "vigencia": "vigente mientras la celda esté `verificado` y ninguno de los SEIS "
                    "identificadores de su sujeto haya cambiado",
        "condicion_de_invalidacion": "cambia el corpus instalado · cambia un esquema · "
                                     "falla un validador · cambia cualquiera de los seis",
        "responsables": None,
        "reside_en": "soporte-de-fase-0",
    }

    directorio = directorio_del_soporte(ruta_control_repo, sujeto)
    os.makedirs(directorio, exist_ok=True)
    _publicar(os.path.join(directorio, DOSIER), dosier)
    _publicar(os.path.join(directorio, DECLARACION), declaracion)
    _publicar(os.path.join(directorio, CELDA), celda)
    return {"sujeto": sujeto, "dosier": dosier, "declaracion": declaracion,
            "celda": celda, "dictamen": dictamen}


# ===========================================================================
#  las guardas de la tabla adversarial
# ===========================================================================
def exigir_fase0_antes_de_mutar(ruta_control_repo, *, macrocircuito, mutacion, sujeto=None):
    """`X-S1`: sin declaración no hay primera mutación. Se nombra el circuito y la mutación."""
    if sujeto is not None:
        declaracion = leer_declaracion(ruta_control_repo, sujeto)
        if declaracion is not None:
            return declaracion
    else:
        declaraciones = declaraciones_del_soporte(ruta_control_repo)
        for declaracion in declaraciones:
            if declaracion.get("macrocircuito") == str(macrocircuito):
                return declaracion
    raise Fase0Omitida(
        "el macrocircuito `" + str(macrocircuito) + "` intenta `" + str(mutacion)
        + "` sin declaración Estructural de esta ejecución; la certificación Estructural es "
        "PRECONDICIÓN, no un paso recomendado, y sin ella la primera mutación está prohibida",
        macrocircuito=str(macrocircuito), mutacion=str(mutacion),
    )


def exigir_gate_superado(resultado, *, macrocircuito, mutacion):
    """`X-S5`: si la `FASE 0` falla, se BLOQUEA ANTES de mutar. Abrir la iniciativa YA es estado."""
    dictamen = (resultado or {}).get("dictamen") or {}
    if dictamen.get("dictamen") != SUPERADO:
        raise MutacionAntesDelGate(
            "`" + GATE + "` no está superado (" + str(dictamen.get("dictamen", NO_SUPERADO))
            + ") y `" + str(macrocircuito) + "` pretende `" + str(mutacion)
            + "`; una iniciativa abierta YA es estado, y ésa es la frontera exacta",
            macrocircuito=str(macrocircuito), mutacion=str(mutacion),
        )
    return resultado


def exigir_declaracion_propia(declaracion, sujeto):
    """`X-S2`: una declaración de otra ejecución, copiada, NO vale para ésta."""
    exigir_sujeto_completo(sujeto)
    if declaracion is None:
        raise CertificacionCopiada(
            "no hay declaración propia de esta ejecución y no se admite ninguna anterior: "
            "la regla 9 exige la declaración de ESTA ejecución, aunque toda la evidencia "
            "material se haya reutilizado",
        )
    suyo = (declaracion.get("sujeto") or {}).get("ejecucion_del_macrocircuito")
    if suyo != sujeto["ejecucion_del_macrocircuito"]:
        raise CertificacionCopiada(
            "la declaración presentada pertenece a la ejecución `" + str(suyo)
            + "` y ésta es `" + sujeto["ejecucion_del_macrocircuito"] + "`; la regla 10 "
            "prohíbe copiar una certificación anterior y prohíbe presumirla vigente",
            presentada=str(suyo), esperada=sujeto["ejecucion_del_macrocircuito"],
        )
    if declaracion.get("hereda"):
        raise CertificacionCopiada(
            "una declaración que se declara HEREDADA no certifica esta ejecución (regla 3)",
        )
    return declaracion


def exigir_estructural_vigente(declaracion, sujeto, *, nivel):
    """`X-S4`: no se sube a Operativa, Integrada ni Completa sin Estructural de ESA ejecución."""
    if str(nivel).lower() not in NIVELES_SUPERIORES:
        raise NivelNoAlcanzable(
            "nivel fuera de los que presuponen Estructural: " + repr(nivel)
            + "; son " + ", ".join(NIVELES_SUPERIORES),
        )
    try:
        exigir_declaracion_propia(declaracion, sujeto)
    except CertificacionCopiada as exc:
        raise NivelNoAlcanzable(
            "no se puede alcanzar `" + str(nivel) + "`: " + exc.detalle
            + ". Un nivel superior ya `verificado` NO vale como prueba de que Estructural "
            "siga vigente (regla 4)",
            nivel=str(nivel),
        ) from exc
    if declaracion.get("dictamen") != SUPERADO:
        raise NivelNoAlcanzable(
            "la declaración Estructural de esta ejecución no está superada, y por la "
            "definición de «NIVEL ALCANZADO» de `§9.2` ningún nivel superior es alcanzable",
            nivel=str(nivel),
        )
    if declaracion.get("huella_del_sujeto") != huella_del_sujeto(sujeto):
        raise NivelNoAlcanzable(
            "la huella del sujeto cambió respecto a la declarada: es OTRO sujeto, y la "
            "declaración Estructural ya no es vigente para él",
            nivel=str(nivel),
        )
    return declaracion


def exigir_una_sola(ruta_control_repo, macrocircuito):
    """`X-S6`: EXACTAMENTE UNA por ejecución. Ni cero ni dos."""
    declaraciones = [
        d for d in declaraciones_del_soporte(ruta_control_repo)
        if d.get("macrocircuito") == str(macrocircuito)
    ]
    ejecuciones = {
        (d.get("sujeto") or {}).get("ejecucion_del_macrocircuito") for d in declaraciones
    }
    for ejecucion in ejecuciones:
        de_esa = [
            d for d in declaraciones
            if (d.get("sujeto") or {}).get("ejecucion_del_macrocircuito") == ejecucion
        ]
        if len({d["id"] for d in de_esa}) > 1:
            raise DosDeclaraciones(
                "la ejecución `" + str(ejecucion) + "` tiene " + str(len(de_esa))
                + " declaraciones distintas; la regla 1 fija exactamente una",
                ejecucion=str(ejecucion),
            )
    return len(declaraciones)


# ===========================================================================
#  INCORPORACIÓN a `estado/cobertura/`
# ===========================================================================
def incorporar(runtime, resultado, *, macrocircuito):
    """El PRIMER ACTO de la primera fase que crea `estado/`: incorpora SIN reemitir."""
    celda = resultado["celda"]
    declaracion = resultado["declaracion"]
    if declaracion.get("dictamen") != SUPERADO:
        raise MutacionAntesDelGate(
            "no se incorpora una declaración que no superó `" + GATE + "`: si el gate "
            "bloquea, no hay nada que incorporar y nada que deshacer",
            macrocircuito=str(macrocircuito),
        )
    existente = durable.leer(runtime.almacen, DOMINIO_COBERTURA + "/" + celda["id"] + ".json")
    if existente is not None and existente.get("huella_del_sujeto") != celda["huella_del_sujeto"]:
        raise IncorporacionInvalida(
            "ya hay una celda incorporada con OTRA huella de sujeto: incorporarla así sería "
            "OTRO sujeto, y la regla 8 lo rechaza",
            celda=celda["id"],
        )
    incorporada = dict(celda)
    incorporada["reside_en"] = "estado/cobertura"
    incorporada["incorporada_por"] = str(macrocircuito)
    incorporada["reemitida"] = False
    durable.escribir(
        runtime.almacen, clase="macrocircuito.fase0.incorporada",
        motivo="incorporación de la declaración Estructural de " + str(macrocircuito)
               + " a `estado/cobertura/`, sin reemitirla",
        objetos={DOMINIO_COBERTURA + "/" + celda["id"] + ".json": incorporada},
        autor=PRODUCTOR,
        semilla={"celda": celda["id"]},
    )
    return incorporada


def exigir_incorporada(runtime, resultado):
    """`X-S11`, segunda y tercera mitad: no incorporarla, o hacerlo con otra huella."""
    celda = resultado["celda"]
    incorporada = durable.leer(
        runtime.almacen, DOMINIO_COBERTURA + "/" + celda["id"] + ".json")
    if incorporada is None:
        raise IncorporacionInvalida(
            "la primera fase creó `estado/` y NO incorporó la declaración ya emitida; sin "
            "incorporarla el nivel Estructural se queda sin sede canónica",
            celda=celda["id"],
        )
    if incorporada.get("huella_del_sujeto") != celda["huella_del_sujeto"]:
        raise IncorporacionInvalida(
            "la celda incorporada lleva otra huella de sujeto: es OTRO sujeto y la regla 8 "
            "lo rechaza",
            celda=celda["id"],
        )
    return incorporada


def exigir_soporte_fuera_de_estado(ruta_control_repo, sujeto):
    """`X-S11`, primera mitad: la `FASE 0` no escribe su celda DENTRO de `estado/`."""
    directorio = os.path.abspath(directorio_del_soporte(ruta_control_repo, sujeto))
    dentro = os.path.abspath(os.path.join(ruta_control_repo, "estado"))
    if directorio == dentro or directorio.startswith(dentro + os.sep):
        raise IncorporacionInvalida(
            "el soporte de la `FASE 0` cae dentro de `estado/`, que nace DESPUÉS de esta "
            "fase: escribir ahí antes es imposible y pretenderlo oculta que la fase no "
            "tenía soporte",
            ruta=SOPORTE,
        )
    return directorio
