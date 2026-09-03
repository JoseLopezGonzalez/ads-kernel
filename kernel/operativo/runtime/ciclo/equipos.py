#!/usr/bin/env python3
"""equipos — la MATERIALIZACIÓN de `C4`, con sus siete pasos y sus siete prohibiciones.

`C4` es un algoritmo, y está escrito como tal: leer el paquete · elegir composición ·
expandir roles · asignar agentes · aplicar combinación · comprobar límites · escribir el
equipo. Este módulo lo ejecuta sobre las composiciones REALES del corpus.

DECISIÓN · se derivan CAPACIDADES, y un MÉTODO nunca se usa como capacidad
    `C1` separa equipo, rol, agente y método. El corpus escribe participantes condicionales
    como `DOM:condiciones`, `ARQ:diagnostico`, `DIS/Reconstruccion` o `CON:experimental`:
    la parte de la izquierda es una CAPACIDAD y la de la derecha un MÉTODO del directorio
    `capacidades/<CAP>/metodos/`. Materializar `DOM:condiciones` como si fuera una
    capacidad produciría un equipo de una capacidad inexistente; ignorar el método perdería
    QUÉ se le pide. `procesos.capacidad_de` y `procesos.metodo_de` los separan, este módulo
    materializa la capacidad y ANOTA el método, y `test_ciclo.py` lo prueba por los dos
    lados: ningún nombre de método entra jamás como capacidad, y el método declarado
    sobrevive en el equipo escrito.

DECISIÓN · la composición se elige por CONDICIÓN DECLARADA, en el ORDEN ESCRITO
    `C4` paso 2 es literal: «recorrer los bloques `ads:composicion` de esa capacidad EN EL
    ORDEN EN QUE ESTÁN ESCRITOS y quedarse con el PRIMERO cuya `condicion` sea verdadera.
    El orden es parte del contrato, no casual». Quién declara verdadera una condición no es
    DSP —sería decidir contenido, y `gate:despacho-coherente` lo prohíbe con
    `sin-contenido`—: se declara al materializar, por el identificador de la composición, y
    el equipo escrito registra cuál la eligió. Si ninguna es verdadera, `C4` manda escalar
    a `SIS`, y eso es `ComposicionDeEquipoAusente`, no un equipo por defecto.

DECISIÓN · el límite de `execution_slots` DEJA FUERA, y NO reduce la composición
    `C4` paso 6, literal: «Lo que no cabe queda `esperando-capacidad`. NO se reduce la
    composición para que quepa». El equipo escrito lleva los dos: los roles despachados y
    los que ESPERAN CAPACIDAD, y los segundos no son «retirados». Un equipo que se recorta
    para caber es el sesgo barato que `a.7` derogó.

DECISIÓN · el PASO 4 se ejecuta de verdad, y la unidad del PASO 6 es el AGENTE
    `C4` paso 4 manda «por cada rol, aplicar la política de `C2`. Registrar modelo elegido,
    descartados y motivo», y esa política vive en `agentes.py`, contra el catálogo que el
    PROYECTO declara en su `PROFILE.md`. De ahí se sigue la corrección del corte por
    límites: `b.11` define `execution_slots` como «capacidad del equipo para trabajo
    AUTÓNOMO en paralelo» calculada a partir de «agentes disponibles», de modo que lo que
    ocupa un slot es un AGENTE y no un rol. Cortar por roles —lo que este módulo hacía—
    separaba a los dos lados del corte un par que la composición declara `combinables`, que
    por definición es UN agente: el paso 5 de `C4` va ANTES que el paso 6, y el corte no
    puede deshacer lo que el paso anterior acaba de unir. Ahora se agrupa primero y se
    corta después, y un grupo entra o espera ENTERO.

DECISIÓN · un rol SIN agente no se despacha, y el equipo lo dice
    `C4`: «PROHIBIDO materializar un rol sin asignarle agente: un rol vacío no es un rol».
    Los roles cuyo perfil no encuentra modelo —o cuyo proyecto no declara catálogo— no
    entran en `roles` ni consumen slot: van a `bloqueados`, con la capacidad de modelo que
    falta nombrada, que es lo que `C2` paso 6 exige. `esperando-capacidad` y `bloqueado` NO
    son lo mismo: el primero cabe y espera turno, el segundo no tiene con qué ocuparse.

DECISIÓN · el conflicto AUTOR / REVISOR / ADJUDICADOR se impide por DATO, no por criterio
    `C4` lo prohíbe dos veces: «PROHIBIDO combinar dos roles que la composición declara
    independientes» y «PROHIBIDO un agente ocupando un rol productor y su crítico en el
    mismo paquete». La lista `independientes` de la composición es la sede, y ante conflicto
    entre `combinables` e `independientes` MANDA `independientes` —también literal—. Aquí no
    se juzga si dos roles «se parecen»: se lee la lista.
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto

from . import agentes as politica_de_agentes
from .corpus import CAPACIDADES, Corpus, bloques
from .errores import (
    AgenteSobreasignado,
    CatalogoDeModelosAusente,
    ComposicionDeEquipoAusente,
    ConflictoDeRoles,
    LimiteDeCapacidadExcedido,
    MetodoNoEsCapacidad,
    PaqueteIlegible,
    VariosAgentesSinIntegrador,
    PerfilDesconocido,
    RolSinAgente,
)
from .procesos import capacidad_de, metodo_de

DOMINIO = "equipos"
ESQUEMA = "ads.estado/1"

# `C4`: los DOS equipos permanentemente activos, y `ENC` NO es uno de ellos (`E1.2`).
PERMANENTEMENTE_ACTIVOS = ("DSP", "SIS")

# `execution_slots` por defecto. `b.11` lo declara calibrable y `C4` usa `auto → 4` en su
# ejemplo; se toma ese valor como defecto EXPLÍCITO para que el recorte sea reproducible.
SLOTS_POR_DEFECTO = 4

ESTADO_DESPACHADO = "despachado"
ESTADO_ESPERANDO_CAPACIDAD = "esperando-capacidad"
ESTADO_BLOQUEADO = "bloqueado"

# El equipo entero: `materializado` cuando todos sus roles tienen agente; `bloqueado` en
# cuanto uno no lo tiene, que es lo que `C2` paso 6 manda declarar del paquete.
EQUIPO_MATERIALIZADO = "materializado"
EQUIPO_BLOQUEADO = "bloqueado"


def derivar_capacidades(ruta):
    """Las CAPACIDADES de la ruta. Nunca un método, y nunca `ENC`.

    Es la entrada de `C4`: se materializa un equipo por capacidad que participa, y sólo por
    ésas. Las presencias que NO participan —ejecutor, autoridad, encuadre— no materializan
    equipo, porque no depositan capa.
    """
    salida = []
    for participante in ruta["participantes"]:
        capacidad = participante["capacidad"]
        if capacidad not in CAPACIDADES:
            raise MetodoNoEsCapacidad(
                "la ruta trae `" + str(capacidad) + "` como capacidad y no lo es; las "
                "quince son " + ", ".join(CAPACIDADES),
                encontrado=str(capacidad),
            )
        if capacidad not in salida:
            salida.append(capacidad)
    return tuple(sorted(salida))


def exigir_capacidad(nombre, *, corpus=None):
    """Falla si `nombre` es un MÉTODO y no una capacidad. La confusión tiene error propio."""
    corpus = corpus or Corpus()
    if nombre in CAPACIDADES:
        return nombre
    posible = capacidad_de(nombre)
    metodo = metodo_de(nombre)
    if posible in CAPACIDADES and metodo:
        raise MetodoNoEsCapacidad(
            "`" + str(nombre) + "` nombra el MÉTODO `" + metodo + "` de la capacidad `"
            + posible + "`; lo que se materializa por `C4` es la capacidad, y el método es "
            "CÓMO trabaja (`C1`)",
            capacidad=posible, metodo=metodo,
        )
    for capacidad in CAPACIDADES:
        if nombre in corpus.metodos(capacidad):
            raise MetodoNoEsCapacidad(
                "`" + str(nombre) + "` es un método de `" + capacidad + "`, no una capacidad",
                capacidad=capacidad, metodo=str(nombre),
            )
    raise MetodoNoEsCapacidad(
        "`" + str(nombre) + "` no es ninguna de las quince capacidades", encontrado=str(nombre),
    )



# ===========================================================================
#  `C4` PASO 1 · LEER EL PAQUETE
# ===========================================================================
# `C4` paso 1 nombra CINCO materias: «capacidad responsable · modo · objetivo · nivel de
# calidad exigido · declaración de acoplamiento». Antes NO se leía ninguna: `paquete` y
# `metodo` entraban por la firma como cadenas opacas y salían intactas en el equipo escrito,
# de modo que el paso sólo existía en un comentario. Una auditoría independiente lo midió y
# lo llamó por su nombre: un passthrough rotulado como ejecución.
#
# DECISIÓN · el paso 1 LEE del corpus y del objeto DURABLE, y tiene EFECTO
#     Un paso cuyo resultado no puede cambiar nada es indistinguible de no ejecutarlo. Las
#     cinco materias se resuelven contra sus sedes —el método contra `capacidades/<CAP>/
#     metodos/`, el nivel de calidad contra los bloques `ads:nivel-novedad` de
#     `diseno/03-ESCALA-DE-NOVEDAD.md`, el acoplamiento contra `runtime.modelo`— y cada una
#     puede FALLAR CERRADO. La materialización de una capacidad que no es la responsable del
#     paquete es un error, no un aviso.
#
# DECISIÓN · «1 AGENTE por defecto, siempre», y VARIOS sólo DECLARADO y con integrador
#     `C4` lo escribe así, y remata: «Varios agentes sin integrador declarado está
#     prohibido». El campo `agentes` de la composición es PROSA —«1», «1 o 2 en competencia
#     declarada», «1 o 2 repartidos por territorio»— y derivar de ahí un cardinal exigiría
#     reglas léxicas sobre texto libre, que este paquete prohíbe. Por eso el reparto se
#     DECLARA como dato (`varios_agentes`), y sin integrador declarado NO se materializa.

MODOS_DIVERGENTES = ("divergente",)


def leer_paquete(capacidad, *, corpus, paquete=None, metodo=None, nivel_de_calidad=None,
                 acoplamiento=None, objetivo=None):
    """`C4` paso 1, con sus CINCO materias resueltas contra sus sedes. Falla cerrado.

    Devuelve la lectura; no la inventa. Lo que el llamador no declara se devuelve como
    ausencia EXPLÍCITA con su motivo, nunca como un valor por omisión que parezca leído.
    """
    lectura = {
        "paquete": paquete,
        "capacidad_responsable": capacidad,
        "objetivo": str(objetivo).strip() if objetivo else None,
    }

    # --- modo: se DERIVA de los pasos del método, que es donde el esquema lo declara.
    if metodo is None:
        lectura["modo"] = {"declarado": False, "metodo": None, "modos": [],
                           "fase_divergente": False,
                           "motivo": "el paquete no declara método; `C4` paso 4 sólo admite "
                                     "varios agentes cuando el MÉTODO declara una fase "
                                     "divergente, y sin método no hay tal declaración"}
    else:
        if metodo not in corpus.metodos(capacidad):
            raise PaqueteIlegible(
                "el paquete declara el método `" + str(metodo) + "`, que no es un método de "
                "`" + capacidad + "`; los suyos son " + (", ".join(corpus.metodos(capacidad))
                                                         or "(ninguno)"),
                capacidad=capacidad, metodo=str(metodo),
            )
        modos = _modos_del_metodo(corpus, capacidad, metodo)
        lectura["modo"] = {
            "declarado": True, "metodo": metodo, "modos": modos,
            "fase_divergente": any(m in MODOS_DIVERGENTES for m in modos),
            "motivo": "",
        }

    # --- nivel de calidad exigido: los bloques `ads:nivel-novedad` son su sede.
    if nivel_de_calidad is None:
        lectura["nivel_de_calidad"] = {
            "declarado": False, "id": None, "gates_obligatorios": [],
            "motivo": "el paquete no declara nivel de calidad exigido; los gates que el "
                      "nivel impone no se presuponen",
        }
    else:
        niveles = _niveles_de_calidad(corpus)
        if nivel_de_calidad not in niveles:
            raise PaqueteIlegible(
                "el paquete exige el nivel de calidad `" + str(nivel_de_calidad) + "`, que "
                "no está en la escala; los declarados son " + ", ".join(sorted(niveles)),
                nivel=str(nivel_de_calidad),
            )
        nivel = niveles[nivel_de_calidad]
        lectura["nivel_de_calidad"] = {
            "declarado": True,
            "id": nivel["id"],
            "nombre": str(nivel.get("nombre") or ""),
            "gates_obligatorios": sorted(str(g) for g in (nivel.get("gates_obligatorios") or [])),
            "critica_visual": str(nivel.get("critica_visual") or ""),
            "estaciones": sorted(int(e) for e in (nivel.get("estaciones") or [])),
            "motivo": "",
        }

    # --- declaración de acoplamiento: la normaliza su sede, no este módulo.
    if acoplamiento is None:
        lectura["acoplamiento"] = {
            "declarado": False, "campos": None,
            "motivo": "el paquete no trae declaración de acoplamiento; `a.5` distingue «no "
                      "toca nada» de «nadie ha dicho qué toca», y esto es lo segundo",
        }
    else:
        from runtime import modelo as _modelo
        lectura["acoplamiento"] = {
            "declarado": True,
            "campos": _modelo.normalizar_acoplamiento(acoplamiento),
            "motivo": "",
        }
    return lectura


def _modos_del_metodo(corpus, capacidad, metodo):
    """Los `modo` declarados por los PASOS del método. Sede: `esquemas/metodo.yaml`."""
    relativa = "capacidades/" + capacidad + "/metodos/" + metodo + ".md"
    modos = []
    for clase, datos, _ruta, _linea in bloques(corpus._texto(relativa), relativa):
        if clase != "metodo":
            continue
        for paso in datos.get("pasos") or []:
            modo = str(paso.get("modo") or "").strip()
            if modo and modo not in modos:
                modos.append(modo)
    return sorted(modos)


def _niveles_de_calidad(corpus):
    """La escala de novedad, DERIVADA de sus bloques. No se copia ningún cardinal."""
    relativa = "diseno/03-ESCALA-DE-NOVEDAD.md"
    salida = {}
    for clase, datos, _ruta, _linea in bloques(corpus._texto(relativa), relativa):
        if clase == "nivel-novedad" and datos.get("id"):
            salida[str(datos["id"])] = datos
    if not salida:
        raise PaqueteIlegible(
            "no hay ningún bloque `ads:nivel-novedad` en `" + relativa + "`: la escala de "
            "calidad no se presupone", ruta=relativa,
        )
    return salida


def exigir_integrador(reparto, roles):
    """`C4`: «Varios agentes sin integrador declarado está prohibido»."""
    nombres = {r["rol"] for r in roles}
    for rol, declarado in sorted((reparto or {}).items()):
        cuantos = int((declarado or {}).get("n") or 1)
        integra = str((declarado or {}).get("integra") or "").strip()
        if rol not in nombres:
            raise PaqueteIlegible(
                "se declaran varios agentes para `" + str(rol) + "`, que no es un rol de "
                "esta composición", rol=str(rol),
            )
        if cuantos < 1:
            raise PaqueteIlegible(
                "`" + str(rol) + "` declara " + str(cuantos) + " agentes; el mínimo es 1",
                rol=str(rol),
            )
        if cuantos > 1 and not integra:
            raise VariosAgentesSinIntegrador(
                "`" + str(rol) + "` declara " + str(cuantos) + " agentes y NO declara quién "
                "INTEGRA el resultado; `C4` lo prohíbe expresamente: produce tres propuestas "
                "y ninguna decisión",
                rol=str(rol), agentes=cuantos,
            )
        if cuantos > 1 and integra not in nombres:
            raise VariosAgentesSinIntegrador(
                "`" + str(rol) + "` declara como integrador a `" + integra + "`, que no es "
                "un rol de esta composición", rol=str(rol), integrador=integra,
            )
    return True


# ===========================================================================
#  el algoritmo de `C4`
# ===========================================================================
def materializar(capacidad, *, corpus=None, composiciones_verdaderas=(),
                 condiciones_de_rol=(), slots=SLOTS_POR_DEFECTO, metodo=None,
                 paquete=None, control_repo=None, catalogo=None, degradaciones=None,
                 politica=None, nivel_de_calidad=None, acoplamiento=None, objetivo=None,
                 varios_agentes=None, capacidad_responsable=None):
    """Los siete pasos de `C4`, en orden, sobre las composiciones reales del corpus.

    `control_repo` es de dónde sale el CATÁLOGO DE MODELOS del proyecto —su `PROFILE.md`—,
    porque `C2` lo sitúa ahí y NUNCA en el kernel. Sin él, o con un `PROFILE` que no declara
    catálogo, ningún rol recibe agente y ninguno se despacha: es el fallo cerrado, no un
    agente por defecto.
    """
    corpus = corpus or Corpus()
    exigir_capacidad(capacidad, corpus=corpus)
    if not isinstance(slots, int) or isinstance(slots, bool) or slots < 1:
        raise LimiteDeCapacidadExcedido(
            "`execution_slots` es un entero >= 1; con cero no se materializa nada y no es "
            "un límite, es una parada",
        )
    verdaderas = tuple(str(c) for c in composiciones_verdaderas)
    verdaderos_roles = {str(c) for c in condiciones_de_rol}

    # PASO 1 · LEER EL PAQUETE. Sus cinco materias se RESUELVEN contra sus sedes, y la
    # capacidad responsable que el paquete declare tiene que ser la que se materializa:
    # leer un paquete y obedecer a otro no es materializar, es improvisar.
    if capacidad_responsable is not None and str(capacidad_responsable) != capacidad:
        raise PaqueteIlegible(
            "el paquete declara responsable a `" + str(capacidad_responsable) + "` y se "
            "está materializando el equipo de `" + capacidad + "`",
            declarada=str(capacidad_responsable), materializada=capacidad,
        )
    lectura = leer_paquete(
        capacidad, corpus=corpus, paquete=paquete, metodo=metodo,
        nivel_de_calidad=nivel_de_calidad, acoplamiento=acoplamiento, objetivo=objetivo,
    )

    # PASO 2 · elegir composición, EN EL ORDEN EN QUE ESTÁN ESCRITAS.
    escritas = corpus.composiciones(capacidad)
    elegida = None
    descartadas = []
    for composicion in escritas:
        if composicion["id"] in verdaderas:
            elegida = composicion
            break
        descartadas.append({
            "composicion": composicion["id"],
            "motivo": "su condición no consta verdadera para este trabajo",
        })
    if elegida is None:
        raise ComposicionDeEquipoAusente(
            "ninguna composición de `" + capacidad + "` tiene condición verdadera para "
            "este trabajo; `C4` manda escalarlo a `SIS` como defecto del catálogo, no "
            "materializar un equipo por defecto",
            capacidad=capacidad,
            composiciones=[c["id"] for c in escritas],
        )

    # PASO 3 · expandir roles.
    roles = []
    fuera = []
    for entrada in elegida.get("roles") or []:
        obligatorio = bool(entrada.get("obligatorio"))
        condicion = str(entrada.get("condicion") or "").strip()
        if obligatorio or (condicion and condicion in verdaderos_roles):
            roles.append({
                "rol": entrada["rol"],
                "obligatorio": obligatorio,
                "agentes": str(entrada.get("agentes") or "1"),
                "condicion": condicion or None,
            })
        else:
            fuera.append({
                "rol": entrada["rol"],
                "motivo": "rol condicional cuya condición no consta verdadera: "
                          + (condicion or "(sin condición declarada)"),
            })
    por_rol = {r["rol"]: r for r in roles}
    nombres = sorted(por_rol)

    # PASO 4 · ASIGNAR AGENTES: por cada rol, la política de `C2` sobre el catálogo del
    # PROYECTO. El catálogo NO vive en el kernel; si el proyecto no lo declara, nadie
    # recibe agente y se dice por qué.
    politica = politica or politica_de_agentes.Politica(corpus)
    catalogo_efectivo, catalogo_declarado, motivo_del_catalogo = catalogo, True, ""
    if catalogo_efectivo is None:
        try:
            catalogo_efectivo = politica_de_agentes.cargar_catalogo(
                control_repo, politica=politica)
        except CatalogoDeModelosAusente as error:
            catalogo_efectivo, catalogo_declarado = None, False
            motivo_del_catalogo = error.detalle
    asignaciones = {}
    for nombre in nombres:
        try:
            asignaciones[nombre] = politica_de_agentes.asignar_rol(
                nombre, politica=politica, catalogo=catalogo_efectivo,
                degradaciones=degradaciones or {})
        except PerfilDesconocido as error:
            asignaciones[nombre] = {
                "rol": nombre, "perfil": None, "estado": politica_de_agentes.ESTADO_BLOQUEADO,
                "modelo": None, "coste": None, "dentro_del_techo": None,
                "candidatos": [], "descartados": [], "orden": [], "degradado": False,
                "degradacion": None, "degradacion_permitida": "",
                "exigencia": None, "eje_dominante": None, "perfiles": [],
                "catalogo": (catalogo_efectivo.huella if catalogo_efectivo else None),
                "falta": [error.detalle],
            }

    # `C4`, «Cuántos agentes por rol»: 1 por defecto SIEMPRE; varios sólo si se DECLARAN,
    # y NUNCA sin integrador. Va aquí, después del paso 3, porque necesita los roles ya
    # expandidos para comprobar que el rol y su integrador existen de verdad.
    exigir_integrador(varios_agentes, roles)
    if varios_agentes and not lectura["modo"]["fase_divergente"]:
        competencia = sorted(r for r, d in (varios_agentes or {}).items()
                             if int((d or {}).get("n") or 1) > 1)
        if competencia:
            raise VariosAgentesSinIntegrador(
                "se declaran varios agentes para " + ", ".join(competencia) + " y el método "
                "del paquete NO declara ninguna fase divergente; `C4` admite varios agentes "
                "cuando el trabajo se reparte sin solapamiento, cuando el método declara una "
                "fase divergente o cuando el volumen excede un contexto, y ninguna de las "
                "tres consta en la lectura del paso 1",
                roles=competencia, metodo=lectura["modo"]["metodo"],
            )


    # PASO 5 · APLICAR COMBINACIÓN, con `independientes` mandando sobre `combinables`, y
    # sobre el CIERRE de las combinaciones: encadenar A-B y B-C no puede colar A con C.
    independientes = _independientes(elegida)
    combinaciones = []
    grupos = {nombre: (nombre,) for nombre in nombres}
    for entrada in elegida.get("combinables") or []:
        pareja = [str(r) for r in (entrada.get("roles") or [])]
        motivo = str(entrada.get("motivo") or "")
        condicion = str(entrada.get("condicion") or "").strip()
        conflicto = [r for r in pareja if _choca(r, pareja, independientes)]
        if conflicto:
            combinaciones.append({
                "roles": pareja, "aplicada": False,
                "motivo": "`independientes` manda sobre `combinables` (`C4` paso 5): "
                          + ", ".join(sorted(conflicto)) + " no puede compartir agente",
            })
            continue
        if not all(nombre in por_rol for nombre in pareja):
            continue
        if condicion and condicion not in verdaderos_roles:
            combinaciones.append({
                "roles": pareja, "aplicada": False,
                "motivo": "la combinación está declarada bajo condición y la condición no "
                          "consta verdadera: " + condicion,
            })
            continue
        union = tuple(sorted(set(grupos[pareja[0]]) | set(grupos[pareja[1]])))
        choque = _choque_en_el_grupo(union, independientes)
        if choque:
            combinaciones.append({
                "roles": pareja, "aplicada": False,
                "motivo": "encadenar esta combinación pondría en el MISMO agente a "
                          + choque[0] + " y " + choque[1] + ", que la composición declara "
                          "independientes: `independientes` manda sobre `combinables`",
            })
            continue
        for nombre in union:
            grupos[nombre] = union
        combinaciones.append({"roles": pareja, "aplicada": True, "motivo": motivo})

    # Un grupo = un AGENTE. Si el grupo tiene más de un rol, el modelo tiene que cumplir
    # los DOS perfiles a la vez; si ninguno lo hace, la combinación NO se aplica —es una
    # licencia, no una obligación— y cada rol conserva su agente, con el motivo escrito.
    distintos = []
    for nombre in nombres:
        if grupos[nombre] not in distintos:
            distintos.append(grupos[nombre])
    unidades = []
    for grupo in sorted(distintos):
        unidad = _agente_del_grupo(grupo, asignaciones, politica=politica,
                                  catalogo=catalogo_efectivo, degradaciones=degradaciones)
        if unidad is None:
            motivo_de_ruptura = (
                "ningún modelo del catálogo cumple a la vez los perfiles de "
                + ", ".join(grupo) + ": la combinación es una licencia de `C4`, no una "
                "obligación, y separarlos no reduce la composición")
            # Y se RETIRAN las entradas que esta ruptura contradice. Añadir la ruptura sin
            # retirarlas dejaba el registro afirmando a la vez una cosa y su contraria, que
            # es justo lo que el paso 7 existe para impedir.
            for previa in combinaciones:
                if previa["aplicada"] and set(previa["roles"]) <= set(grupo):
                    previa["aplicada"] = False
                    previa["retirada_por"] = motivo_de_ruptura
                    previa["motivo"] = (
                        previa["motivo"] + " — RETIRADA: " + motivo_de_ruptura
                    ).strip(" —")
            combinaciones.append({
                "roles": list(grupo), "aplicada": False,
                "motivo": motivo_de_ruptura,
            })
            for miembro in grupo:
                grupos[miembro] = (miembro,)
                unidades.append(_agente_del_grupo(
                    (miembro,), asignaciones, politica=politica,
                    catalogo=catalogo_efectivo, degradaciones=degradaciones)
                    or _unidad_bloqueada((miembro,), asignaciones))
            continue
        unidades.append(unidad)

    # PASO 6 · COMPROBAR LÍMITES. La unidad que ocupa un slot es el AGENTE (`b.11`: la
    # concurrencia se calcula «a partir de agentes disponibles»), NUNCA el rol: por eso un
    # par combinable ocupa UN slot y jamás queda a los dos lados del corte.
    unidades.sort(key=lambda u: (u["roles"][0], u["modelo"] or "", u["agente"] or ""))
    ocupados = 0
    for unidad in unidades:
        if unidad["estado"] == ESTADO_BLOQUEADO:
            continue
        if ocupados < slots:
            ocupados += 1
            unidad["estado"] = ESTADO_DESPACHADO
            unidad["slot"] = ocupados
        else:
            unidad["estado"] = ESTADO_ESPERANDO_CAPACIDAD
            unidad["slot"] = None

    asignados, esperando, bloqueados = [], [], []
    for unidad in unidades:
        for nombre in unidad["roles"]:
            rol = por_rol[nombre]
            fila = {
                "rol": nombre,
                "obligatorio": rol["obligatorio"],
                "agentes": rol["agentes"],
                "condicion": rol["condicion"],
                "estado": unidad["estado"],
                "comparte_agente_con": _companero(nombre, unidad),
                "perfil": asignaciones[nombre].get("perfil"),
                "agente": unidad["agente"],
                "modelo": unidad["modelo"],
                "slot": unidad["slot"],
            }
            if unidad["estado"] == ESTADO_DESPACHADO:
                asignados.append(fila)
            elif unidad["estado"] == ESTADO_ESPERANDO_CAPACIDAD:
                esperando.append(fila)
            else:
                fila["falta"] = list(unidad["falta"])
                bloqueados.append(fila)

    equipo = {
        "esquema": ESQUEMA,
        "capacidad": capacidad,
        "metodo": metodo,
        "paquete": paquete,
        # `C4` PASO 1, PUBLICADO. Sin esto la lectura no tendría efecto observable y el
        # paso volvería a ser lo que la auditoría encontró: un rótulo sobre un passthrough.
        "lectura_del_paquete": lectura,
        "gates_del_nivel": list(lectura["nivel_de_calidad"]["gates_obligatorios"]),
        "fase_divergente": bool(lectura["modo"]["fase_divergente"]),
        "reparto_de_agentes": _reparto(varios_agentes),
        "composicion": elegida["id"],
        "clase_de_trabajo": str(elegida.get("clase_de_trabajo") or ""),
        "condicion_que_la_eligio": str(elegida.get("condicion") or "").strip(),
        "composiciones_descartadas": descartadas,
        "roles": sorted(asignados, key=lambda r: r["rol"]),
        "esperando_capacidad": sorted(esperando, key=lambda r: r["rol"]),
        "bloqueados": sorted(bloqueados, key=lambda r: r["rol"]),
        "roles_fuera": sorted(fuera, key=lambda r: r["rol"]),
        "combinaciones": sorted(combinaciones, key=lambda c: (tuple(c["roles"]),
                                                             c["aplicada"], c["motivo"])),
        "independientes": sorted(independientes, key=lambda i: i["rol"]),
        "agentes": sorted(unidades, key=lambda u: u["agente"] or u["roles"][0]),
        "asignaciones": [asignaciones[n] for n in nombres],
        "catalogo": {
            "declarado": bool(catalogo_declarado and catalogo_efectivo is not None),
            "sede": catalogo_efectivo.sede if catalogo_efectivo else None,
            "huella": catalogo_efectivo.huella if catalogo_efectivo else None,
            "modelos": list(catalogo_efectivo.ids) if catalogo_efectivo else [],
            "motivo": motivo_del_catalogo,
        },
        "slots": int(slots),
        "slots_ocupados": ocupados,
        "estado": EQUIPO_BLOQUEADO if bloqueados else EQUIPO_MATERIALIZADO,
        "permanentemente_activo": capacidad in PERMANENTEMENTE_ACTIVOS,
        "retirada": str(elegida.get("retirada") or ""),
    }
    equipo["id"] = identificador(equipo)
    exigir_slots_coherentes(equipo)
    return equipo


def _unidad_bloqueada(grupo, asignaciones):
    falta = []
    for nombre in grupo:
        falta.extend(asignaciones[nombre].get("falta") or [])
    return {
        "agente": None, "modelo": None, "roles": list(grupo),
        "perfiles": sorted({asignaciones[n].get("perfil") for n in grupo
                            if asignaciones[n].get("perfil")}),
        "estado": ESTADO_BLOQUEADO, "slot": None,
        "descartados": [], "falta": sorted(set(falta)) or ["sin agente asignable"],
        "exigencia": None, "eje_dominante": None, "degradado": False,
    }


def _agente_del_grupo(grupo, asignaciones, *, politica, catalogo, degradaciones=None):
    """El AGENTE que ocupa un grupo de roles: UN modelo que cumple TODOS sus perfiles."""
    grupo = tuple(sorted(grupo))
    if len(grupo) == 1:
        registro = asignaciones[grupo[0]]
        if registro["estado"] != politica_de_agentes.ESTADO_ASIGNADO:
            return _unidad_bloqueada(grupo, asignaciones)
        return {
            "agente": politica_de_agentes.identificador_de_agente(registro["modelo"], grupo),
            "modelo": registro["modelo"], "roles": list(grupo),
            "perfiles": list(registro.get("perfiles") or []),
            "estado": ESTADO_DESPACHADO, "slot": None,
            "descartados": list(registro["descartados"]),
            "falta": list(registro.get("falta") or []),
            "exigencia": registro.get("exigencia"),
            "eje_dominante": registro.get("eje_dominante"),
            "degradado": bool(registro.get("degradado")),
        }
    perfiles = [asignaciones[n].get("perfil") for n in grupo]
    if any(p is None for p in perfiles):
        return None
    exigencia = politica.combinar(
        [politica.exigencia_de_perfil(p) for p in perfiles])
    registro = politica_de_agentes.seleccionar(exigencia, catalogo, politica=politica)
    if registro["estado"] != politica_de_agentes.ESTADO_ASIGNADO:
        return None
    return {
        "agente": politica_de_agentes.identificador_de_agente(registro["modelo"], grupo),
        "modelo": registro["modelo"], "roles": list(grupo),
        "perfiles": sorted(set(perfiles)),
        "estado": ESTADO_DESPACHADO, "slot": None,
        "descartados": list(registro["descartados"]),
        "falta": list(registro.get("falta") or []),
        "exigencia": registro.get("exigencia"),
        "eje_dominante": registro.get("eje_dominante"),
        "degradado": bool(registro.get("degradado")),
    }


def _choque_en_el_grupo(grupo, independientes):
    """El primer par del grupo que la composición declara independiente, o `None`."""
    for uno in grupo:
        for otro in grupo:
            if uno >= otro:
                continue
            for entrada in independientes:
                if entrada["rol"] == uno and otro in entrada["de"]:
                    return (uno, otro)
                if entrada["rol"] == otro and uno in entrada["de"]:
                    return (otro, uno)
    return None


def exigir_agentes_asignados(equipo):
    """`C4`: un rol sin agente NO se despacha. Es la puerta antes de planificar.

    No basta con que el equipo lo escriba: alguien tiene que impedir el despacho. Esta
    función es esa puerta, y falla cerrado nombrando el rol y qué capacidad de modelo falta.
    """
    sin_agente = [r for r in equipo.get("roles") or [] if not r.get("agente")]
    if sin_agente:
        raise RolSinAgente(
            "el equipo `" + str(equipo.get("id")) + "` despacha roles SIN agente: "
            + ", ".join(sorted(r["rol"] for r in sin_agente))
            + "; `C4`: «PROHIBIDO materializar un rol sin asignarle agente»",
            roles=sorted(r["rol"] for r in sin_agente),
        )
    bloqueados = equipo.get("bloqueados") or []
    if bloqueados:
        falta = sorted({f for r in bloqueados for f in (r.get("falta") or [])})
        raise RolSinAgente(
            "el equipo `" + str(equipo.get("id")) + "` queda BLOQUEADO: "
            + ", ".join(sorted(r["rol"] for r in bloqueados)) + " no tienen agente; falta "
            + "; ".join(falta),
            roles=sorted(r["rol"] for r in bloqueados), falta=falta,
        )
    return True


def exigir_slots_coherentes(equipo):
    """Ni sobreasignación, ni colisión de slot, ni un rol en dos sitios (`b.11`, `C4` 6)."""
    ocupados = [u for u in equipo.get("agentes") or [] if u["estado"] == ESTADO_DESPACHADO]
    numeros = [u["slot"] for u in ocupados]
    if len(numeros) != len(set(numeros)) or any(n is None for n in numeros):
        raise AgenteSobreasignado(
            "dos agentes del equipo ocupan el mismo `execution_slot`, o un agente "
            "despachado no tiene slot: " + str(sorted(str(n) for n in numeros)),
        )
    if len(ocupados) > int(equipo.get("slots") or 0):
        raise AgenteSobreasignado(
            "el equipo ocupa " + str(len(ocupados)) + " slots y sólo declara "
            + str(equipo.get("slots")) + "; `C4` paso 6 deja fuera, no ensancha",
        )
    vistos = {}
    for lista in ("roles", "esperando_capacidad", "bloqueados"):
        for fila in equipo.get(lista) or []:
            if fila["rol"] in vistos:
                raise AgenteSobreasignado(
                    "el rol `" + fila["rol"] + "` aparece en `" + vistos[fila["rol"]]
                    + "` y en `" + lista + "`: un rol ocupa un estado, no dos",
                    rol=fila["rol"],
                )
            vistos[fila["rol"]] = lista
    por_agente = {}
    for unidad in equipo.get("agentes") or []:
        if not unidad["agente"]:
            continue
        if unidad["agente"] in por_agente:
            raise AgenteSobreasignado(
                "el agente `" + unidad["agente"] + "` aparece dos veces en el equipo",
                agente=unidad["agente"],
            )
        por_agente[unidad["agente"]] = unidad
    return True


def _reparto(varios_agentes):
    """El reparto DECLARADO de agentes por rol, normalizado y ordenado.

    `C4`, «Cuántos agentes por rol»: «1 AGENTE por defecto, siempre». Sin declaración este
    reparto sale VACÍO, que es lo que significa «uno por rol»: no se escribe un cardinal por
    cada rol para que parezca que alguien lo decidió.
    """
    salida = []
    for rol, declarado in sorted((varios_agentes or {}).items()):
        salida.append({
            "rol": str(rol),
            "agentes": int((declarado or {}).get("n") or 1),
            "integra": str((declarado or {}).get("integra") or "") or None,
            "motivo": str((declarado or {}).get("motivo") or ""),
        })
    return salida



def _independientes(composicion):
    salida = []
    for entrada in composicion.get("independientes") or []:
        salida.append({
            "rol": str(entrada["rol"]),
            "de": [str(d) for d in (entrada.get("de") or [])],
            "motivo": str(entrada.get("motivo") or ""),
        })
    return salida


def _choca(rol, pareja, independientes):
    for entrada in independientes:
        if entrada["rol"] == rol and any(otro in entrada["de"] for otro in pareja if otro != rol):
            return True
        if rol in entrada["de"] and entrada["rol"] in pareja:
            return True
    return False


def _companero(rol, unidad):
    """Con quién comparte agente ESTE rol, leído de la UNIDAD que lo ocupa.

    DECISIÓN · se deriva del AGENTE, no de la lista de combinaciones
        Derivarlo de `combinaciones` publicaba un hecho falso. Cuando un grupo se rompe
        porque ningún modelo cumple los dos perfiles, la ruptura se AÑADE a la lista y la
        entrada `aplicada: True` anterior se quedaba ahí: los dos roles seguían declarando
        que compartían un agente que ya NO compartían, y `exigir_separacion` —que es la
        instrumentación de `G13`— consultaba ese campo. Una auditoría independiente lo
        encontró y lo midió: dos agentes distintos y `_comparten()` diciendo `True`.
        La unidad SÍ es el hecho: un agente, los roles que ocupa. De ahí sale ahora.
    """
    otros = [r for r in unidad["roles"] if r != rol]
    return otros[0] if otros else None


def exigir_separacion(equipo, *, autor, revisor, adjudicador=None):
    """AUTOR, REVISOR y ADJUDICADOR no pueden ser el mismo agente cuando la composición lo veta.

    `C4`: «PROHIBIDO un agente ocupando un rol productor y su crítico en el mismo paquete».
    La sede de qué es «su crítico» es la lista `independientes` de la composición, y por eso
    esta comprobación LEE esa lista en vez de decidir por su cuenta qué roles se parecen.
    """
    implicados = [r for r in (autor, revisor, adjudicador) if r]
    if len(implicados) != len(set(implicados)):
        repetido = sorted({r for r in implicados if implicados.count(r) > 1})
        raise ConflictoDeRoles(
            "el mismo rol ocupa dos de las tres posiciones (autor, revisor, adjudicador): "
            + ", ".join(repetido),
            roles=repetido,
        )
    for entrada in equipo["independientes"]:
        for otro in implicados:
            if otro == entrada["rol"]:
                continue
            if otro in entrada["de"] and entrada["rol"] in implicados:
                if _comparten(equipo, entrada["rol"], otro):
                    raise ConflictoDeRoles(
                        "`" + entrada["rol"] + "` es independiente de `" + otro + "` y el "
                        "equipo los hace compartir agente: " + entrada["motivo"],
                        roles=[entrada["rol"], otro],
                    )
    return True


def _comparten(equipo, uno, otro):
    """Comparten agente si la combinación los unió O si el agente asignado es el MISMO.

    Lo segundo es lo que importa desde que el paso 4 existe: `comparte_agente_con` es la
    huella de la COMBINACIÓN declarada, y el `agente` es el hecho. Si algún día el agente
    se asignara por otro camino, la comprobación de `C4` seguiría viendo la colisión.
    """
    filas = []
    for lista in ("roles", "esperando_capacidad", "bloqueados"):
        filas.extend(equipo.get(lista) or [])
    for rol in filas:
        if rol["rol"] == uno and rol.get("comparte_agente_con") == otro:
            return True
        if rol["rol"] == otro and rol.get("comparte_agente_con") == uno:
            return True
    agentes_de = {}
    for rol in filas:
        if rol.get("agente"):
            agentes_de.setdefault(rol["rol"], rol["agente"])
    if uno in agentes_de and otro in agentes_de and agentes_de[uno] == agentes_de[otro]:
        return True
    return False


def identificador(equipo):
    """`eq-<16 hex>` derivado del CONTENIDO: mismo paquete y misma composición, mismo equipo."""
    sin_id = {clave: valor for clave, valor in equipo.items() if clave != "id"}
    digest = cid_de_objeto(sin_id)
    return "eq-" + digest.split(":", 1)[-1][:16]


def ruta_de(identificador_de_equipo):
    return DOMINIO + "/" + identificador_de_equipo + ".json"
