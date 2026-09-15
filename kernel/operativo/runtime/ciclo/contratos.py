"""contratos — el CONTRATO OPERATIVO EFECTIVO de un rol: base de familia + derivación + especialización.

HECHO MEDIDO ANTES DE CONSTRUIR (certificación de la oficina, 2026-09-15). Siete roles
tenían contrato operativo escrito a mano y treinta trabajaban con su bloque de rol y su
método: dos agentes competentes podían leer el mismo rol y ejecutar cosas sustancialmente
distintas. Escribir treinta documentos copiando la misma estructura era la otra forma de
fallar: treinta copias que divergen en la segunda semana.

DECISIÓN · el contrato efectivo se COMPONE de tres capas, y ninguna es prosa libre
    BASE        `ads:contrato-base`, una por FAMILIA (productor, revisor, consultor,
                investigador, operador, aprendizaje): lo que comparten todos los roles de
                la familia —comprobaciones previas, apertura y cierre de la secuencia,
                prohibiciones, checklist, reglas de escalado, gates que nunca se
                autocertifican—. Un rol pertenece a EXACTAMENTE una base, por su id.
    DERIVACIÓN  lo que los veintinueve campos del ROL ya dicen de forma estructurada y no
                hace falta repetir: misión, entradas, decisiones propias (`autoridad.decide`),
                escalados (`autoridad.escala`), artefactos (`salida`), devoluciones
                (`devolucion`), prohibiciones (`limites` + `antipatrones`), criterios
                (`criterios_calidad`), fuentes (`memoria_consulta`), incompatibilidades
                (`independencia.de_quien`), métodos (`metodo`), gate propio
                (`no_autocertifica`), y la evidencia que exige su gate.
    ESPECIALIZACIÓN `ads:contrato-de-rol`, opcional y corta: lo que ni la base ni la
                derivación pueden decir por el rol. Las listas SE SUMAN; `mision_operativa`,
                `secuencia`, `artefactos`, `ejemplo_bueno` y `ejemplo_malo` SUSTITUYEN.

    La fusión se valida contra `esquemas/contrato-operativo.yaml`, que es la forma que el
    brief entrega y la entrega comprueba. Un contrato escrito ENTERO como
    `ads:contrato-operativo` sigue valiendo tal cual: es la forma larga de lo mismo.

DECISIÓN · «materializable» es un DATO, no una opinión
    Un rol es materializable cuando figura en una composición (`ads:composicion`) de una
    capacidad que algún proceso (`ads:proceso`) nombra como obligatoria o condicional: es
    exactamente el conjunto de roles que `oficina.planificar` puede convertir en un
    paquete con brief. Los demás —DSP, que ejecuta el propio runtime; ENC, que ocurre
    ANTES de que exista ruta— son conceptuales u orquestados, y se publican como tales.
"""
from __future__ import annotations

from . import formas
from .errores import CorpusIlegible, CorpusIncompleto

FAMILIAS = ("productor", "revisor", "consultor", "investigador", "operador", "aprendizaje", "orquestador")

LISTAS_QUE_SE_SUMAN = (
    "conocimientos_exigibles", "entradas_obligatorias", "comprobaciones_previas",
    "fuentes_a_consultar", "evidencias_requeridas", "criterios_de_calidad_medibles",
    "condiciones_de_aceptacion", "condiciones_de_devolucion", "reglas_de_escalado",
    "incompatibilidades", "actuaciones_prohibidas", "entrega_a", "decisiones_propias",
    "metodos", "no_autocertifica", "checklist",
)
CAMPOS_QUE_SUSTITUYEN = ("mision_operativa", "secuencia", "artefactos", "ejemplo_bueno",
                         "ejemplo_malo")

ENTREGA_SEGUN_EL_PLAN = "segun-el-plan"


# ===========================================================================
#  clasificación de roles
# ===========================================================================
def capacidades_de_los_procesos(corpus):
    """Las capacidades que algún proceso nombra, obligatorias o condicionales."""
    salida = set()
    for proceso in corpus.de_tipo("proceso"):
        for obligatoria in proceso.get("obligatorias") or []:
            salida.add(str(obligatoria.get("capacidad_productora") or "").split(":", 1)[0])
        for condicional in proceso.get("condicionales") or []:
            salida.add(str(condicional.get("capacidad") or "").split(":", 1)[0])
    salida.discard("")
    return salida


def composiciones_por_rol(corpus):
    salida = {}
    for composicion in corpus.de_tipo("composicion"):
        for fila in composicion.get("roles") or []:
            salida.setdefault(str(fila.get("rol")), []).append(str(composicion.get("id")))
    return salida


def clasificar(corpus):
    """`{rol: clase}` con clase en materializable · consultivo · conceptual · huerfano."""
    procesos = capacidades_de_los_procesos(corpus)
    por_rol = composiciones_por_rol(corpus)
    bases = bases_por_rol(corpus)
    salida = {}
    for rol, datos in corpus.roles().items():
        capacidad = str(datos.get("capacidad"))
        if rol in bases:
            # Declarado en una base: contratable por decisión explícita del corpus, aunque
            # ningún proceso nombre su capacidad (PLT entra por el desbloqueador de b.15.1).
            salida[rol] = "consultivo" if bases[rol].get("familia") == "consultor" else "materializable"
        elif rol not in por_rol:
            salida[rol] = "huerfano"
        elif capacidad not in procesos:
            salida[rol] = "conceptual"
        else:
            # Lo materializa un proceso y NINGUNA base lo cubre: es exactamente lo que
            # `comprobar_contratos` tiene que hacer fallar.
            salida[rol] = "sin-base"
    return salida


# ===========================================================================
#  bases
# ===========================================================================
def bases(corpus):
    salida = {}
    for datos in corpus.de_tipo("contrato-base"):
        identificador = datos.get("id")
        if not isinstance(identificador, str):
            raise CorpusIlegible("un bloque `ads:contrato-base` sin `id`")
        if identificador in salida:
            raise CorpusIlegible("dos bloques declaran la base `" + identificador + "`")
        salida[identificador] = datos
    return salida


def bases_por_rol(corpus):
    """`{rol: base}`. Un rol en dos bases es una contradicción y se levanta."""
    salida = {}
    for base in bases(corpus).values():
        for rol in base.get("roles") or []:
            if rol in salida:
                raise CorpusIlegible(
                    "el rol `" + str(rol) + "` hereda de dos bases: `" + salida[rol]["id"]
                    + "` y `" + base["id"] + "`; un rol pertenece a UNA familia",
                )
            salida[str(rol)] = base
    return salida


def especializaciones(corpus):
    salida = {}
    for datos in corpus.de_tipo("contrato-de-rol"):
        rol = datos.get("rol")
        if not isinstance(rol, str):
            raise CorpusIlegible("un bloque `ads:contrato-de-rol` sin `rol`")
        if rol in salida:
            raise CorpusIlegible("dos especializaciones para el rol `" + rol + "`")
        salida[rol] = datos
    return salida


# ===========================================================================
#  derivación desde el rol
# ===========================================================================
def _texto(valor):
    return " ".join(str(valor or "").split())


def derivar(corpus, rol_id):
    """Lo que el ROL ya declara de forma estructurada, en la forma del contrato."""
    rol = corpus.rol(rol_id)
    gate_id = str(rol.get("gate") or "")
    gate = corpus.gates().get(gate_id) or {}
    autoridad = rol.get("autoridad") or {}
    independencia = rol.get("independencia") or {}
    juez = "quien dictamina " + gate_id if gate_id else "el revisor del gate del rol"
    return {
        "mision_operativa": _texto(rol.get("mision")),
        "conocimientos_exigibles": [_texto(c) for c in rol.get("conocimientos") or []],
        "entradas_obligatorias": [
            {"que": _texto(e),
             "donde": "las entregas previas del item y los handoffs de este paquete, que el brief lista",
             "si_falta": "devolver"}
            for e in rol.get("entradas") or []],
        "comprobaciones_previas": [],
        "secuencia": [
            {"hace": _texto(r), "produce": "lo que esa responsabilidad nombra, como artefacto de la entrega",
             "termina_cuando": "consta en la entrega con su evidencia", "checkpoint": True}
            for r in rol.get("responsabilidades") or []],
        "fuentes_a_consultar": [_texto(f) for f in rol.get("memoria_consulta") or []],
        "artefactos": [
            {"tipo": "documento", "nombre": _texto(s)[:80] or "salida", "estructura_minima": [_texto(s)],
             "obligatorio": True}
            for s in rol.get("salida") or []],
        "evidencias_requeridas": [
            {"que": _texto(e), "forma": "adjunta en la entrega como artefacto localizable",
             "quien_la_puede_juzgar": juez}
            for e in gate.get("evidencia") or []],
        "criterios_de_calidad_medibles": [
            {"criterio": _texto(c), "como_se_mide": "lo contrasta " + juez + " con la evidencia adjunta"}
            for c in rol.get("criterios_calidad") or []],
        "condiciones_de_aceptacion": [],
        "condiciones_de_devolucion": [_texto(d) for d in rol.get("devolucion") or []],
        "reglas_de_escalado": [
            {"cuando": _texto(e), "a_quien": "DSP, que enruta a la autoridad de la materia o al Owner",
             "con_que": "las posturas escritas y la evidencia que las sostiene"}
            for e in autoridad.get("escala") or []],
        "incompatibilidades": [
            "no comparte trabajador con " + _texto(q) + " en el mismo item"
            for q in independencia.get("de_quien") or []],
        "actuaciones_prohibidas": [_texto(l) for l in rol.get("limites") or []]
                                  + [_texto(a) for a in rol.get("antipatrones") or []],
        "entrega_a": [ENTREGA_SEGUN_EL_PLAN],
        "decisiones_propias": [_texto(d) for d in autoridad.get("decide") or []],
        "metodos": [str(m) for m in rol.get("metodo") or []],
        "no_autocertifica": [gate_id] if gate_id else [],
        "ejemplo_bueno": "",
        "ejemplo_malo": "",
        "checklist": [],
    }


# ===========================================================================
#  fusión
# ===========================================================================
def _suma(*listas):
    salida = []
    vistos = set()
    for lista in listas:
        for elemento in lista or []:
            clave = repr(elemento)
            if clave in vistos:
                continue
            vistos.add(clave)
            salida.append(elemento)
    return salida


def fusionar(base, derivado, especializacion, *, rol_id):
    """El contrato efectivo: base + derivado + especialización, con las reglas de arriba."""
    base = dict(base or {})
    especializacion = dict(especializacion or {})
    contrato = {
        "id": especializacion.get("id") or ("contrato:" + rol_id.lower().replace("/", "-")),
        "rol": rol_id,
    }
    for campo in LISTAS_QUE_SE_SUMAN:
        contrato[campo] = _suma(base.get(campo), derivado.get(campo), especializacion.get(campo))
    # los gates que la base añade a los que nadie autocertifica
    contrato["no_autocertifica"] = _suma(contrato["no_autocertifica"],
                                         base.get("no_autocertifica_ademas"))
    for campo in CAMPOS_QUE_SUSTITUYEN:
        if campo == "secuencia":
            continue
        valor = especializacion.get(campo)
        if valor in (None, "", []):
            valor = derivado.get(campo)
        if valor in (None, "", []):
            valor = base.get(campo)
        contrato[campo] = valor
    # la secuencia: apertura de la base · pasos del rol · cierre de la base, numerados
    medio = especializacion.get("secuencia") or derivado.get("secuencia") or []
    pasos = list(base.get("secuencia_inicial") or []) + list(medio) + list(base.get("secuencia_final") or [])
    contrato["secuencia"] = [dict(p, n=n) for n, p in enumerate(pasos, 1)]
    if not contrato.get("ejemplo_bueno"):
        contrato["ejemplo_bueno"] = ("Lo que este rol entrega cuando cumple: " + _texto(derivado.get("mision_operativa"))
                                     + " Consta en su entrega con los artefactos y la evidencia que su gate exige.")
    if not contrato.get("ejemplo_malo"):
        prohibidas = contrato.get("actuaciones_prohibidas") or ["saltarse su gate"]
        contrato["ejemplo_malo"] = ("Lo que este rol NO puede hacer y se ha visto hacer: " + _texto(prohibidas[0])
                                    + ". Una entrega así se rechaza al recibirla, sin tocar el estado.")
    return contrato


def contrato_efectivo(corpus, rol_id, *, validar=True):
    """El contrato que el brief entrega y la entrega comprueba, o `None` si el rol no tiene base
    ni contrato completo. Con `validar`, levanta `CorpusIncompleto` si la fusión no cumple
    el esquema: un contrato insuficiente no se entrega como si bastara."""
    completo = corpus.contratos_operativos_completos().get(rol_id)
    if completo is not None:
        return completo
    base = bases_por_rol(corpus).get(rol_id)
    if base is None:
        return None
    contrato = fusionar(base, derivar(corpus, rol_id), especializaciones(corpus).get(rol_id), rol_id=rol_id)
    if validar:
        fallos = formas.validar(contrato, corpus.esquema("contrato-operativo"), corpus=corpus,
                                camino="contrato-operativo(" + rol_id + ")")
        if fallos:
            raise CorpusIncompleto(
                "el contrato efectivo de `" + rol_id + "` no cumple el esquema: " + "; ".join(fallos),
                ruta=rol_id,
            )
    return contrato


def fallos_del_contrato(corpus, rol_id):
    """Los fallos del contrato efectivo, sin levantar. Lo que `comprobar_contratos` publica."""
    try:
        contrato = contrato_efectivo(corpus, rol_id, validar=False)
    except (CorpusIlegible, CorpusIncompleto) as exc:
        return [str(exc)]
    if contrato is None:
        return ["sin base de familia ni contrato completo: no tiene contrato operativo"]
    fallos = list(formas.validar(contrato, corpus.esquema("contrato-operativo"), corpus=corpus,
                                 camino="contrato-operativo(" + rol_id + ")"))
    rol = corpus.rol(rol_id)
    metodos_del_rol = set(str(m) for m in rol.get("metodo") or [])
    for metodo in contrato.get("metodos") or []:
        if metodo not in metodos_del_rol:
            fallos.append("metodos: `" + str(metodo) + "` no es un método del rol")
    if rol.get("gate") and rol["gate"] not in (contrato.get("no_autocertifica") or []):
        fallos.append("no_autocertifica: no incluye el gate propio `" + str(rol["gate"]) + "`")
    for de_quien in (rol.get("independencia") or {}).get("de_quien") or []:
        if not any(_texto(de_quien) in _texto(i) for i in contrato.get("incompatibilidades") or []):
            fallos.append("incompatibilidades: no cubre la independencia de `" + _texto(de_quien) + "`")
    return fallos
