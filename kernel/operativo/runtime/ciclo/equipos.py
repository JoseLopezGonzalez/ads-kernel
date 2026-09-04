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

import math
import re
import unicodedata

from estado.serializacion import cid_de_objeto

from . import agentes as politica_de_agentes
from .corpus import CAPACIDADES, Corpus, bloques
from .errores import (
    AgenteSobreasignado,
    CardinalDeAgentesIlegible,
    CatalogoDeModelosAusente,
    ComposicionDeEquipoAusente,
    ConflictoDeRoles,
    CriterioDeComparacionAusente,
    LimiteDeCapacidadExcedido,
    MetodoNoEsCapacidad,
    PaqueteIlegible,
    RepartoIncoherente,
    RepartoSinUnidades,
    VariosAgentesSinIntegrador,
    VolumenExcedeElContexto,
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
# DECISIÓN · el CARDINAL se DERIVA del campo `agentes`, que NO es texto libre
#     El comentario que ocupaba este sitio decía lo contrario: que `agentes` era prosa y que
#     derivar de ahí un cardinal «exigiría reglas léxicas sobre texto libre». De esa premisa
#     salía todo lo demás —el reparto entraba como PARÁMETRO EXTERNO `varios_agentes`, y sin
#     parámetro se materializaba UN agente—, y el resultado medido fue el peor posible: las
#     TRES composiciones reales que declaran varios agentes producían un agente único, con
#     `reparto_de_agentes` vacío, sin error, sin aviso y sin `esperando-capacidad`, mientras
#     el registro durable publicaba «2 o 3» al lado de ese agente único.
#
#     La premisa era falsa y se puede medir: el campo `agentes` tiene NOVENTA Y NUEVE valores
#     en VEINTIDÓS formas, y exactamente TRES declaran más de uno. Veintidós formas sobre
#     noventa y nueve valores no son texto libre: son un vocabulario cerrado con dos partes,
#     un CARDINAL y un MODO DE REPARTO. `leer_cardinal` lo lee entero y ENUMERADO, y lo que
#     no encaja en ninguna forma declarada NO vale «1 por omisión»: levanta
#     `CardinalDeAgentesIlegible`. `exigir_censo_legible` recorre el corpus completo y falla
#     si aparece una forma nueva, para que una composición añadida mañana no pueda colarse en
#     silencio por la puerta que este comentario dejaba abierta.
#
# DECISIÓN · el INTEGRADOR sale de la COMPOSICIÓN, y el CONTENIDO del reparto del paquete
#     `C4`: «En los tres casos se declara QUIÉN INTEGRA el resultado», y «Varios agentes sin
#     integrador declarado está prohibido». Quién integra es una propiedad de la COMPOSICIÓN,
#     y estaba escrita en su campo `ampliacion` desde el principio —«con
#     `DIS/direccion-artistica` como integrador declarado»—: el runtime no lo leía y lo
#     pedía por la firma, de modo que la prohibición sólo se aplicaba a quien se molestara en
#     declarar el reparto. Ahora `integrador_de` lo lee de `ampliacion` y lo CONTRASTA contra
#     `roles`; un integrador que no es rol de la composición no integra nada.
#     Lo que sí sigue siendo del llamador es el CONTENIDO: cuáles son los territorios, cuáles
#     las direcciones exploradas, si la competencia está declarada y con qué criterio. Eso es
#     decidir contenido, y `gate:despacho-coherente` lo prohíbe a DSP con `sin-contenido`.
#
# DECISIÓN · las TRES condiciones de `C4` se COMPRUEBAN, y la tercera se MIDE
#     `C4` admite varios agentes «cuando se cumple alguna, y la composición lo declara»:
#     (a) reparto por artefacto o superficie sin solapamiento, (b) fase divergente declarada
#     por el método, (c) volumen que excede lo que un contexto puede sostener. (a) exige que
#     las unidades del reparto EXISTAN como dato: con cero territorios no hay reparto que
#     comprobar, y `RepartoSinUnidades` lo dice —un territorio es una respuesta, ninguno es
#     que nadie ha contestado—. (b) ya se leía de los pasos del método y se conserva. (c) se
#     mide: el volumen declarado del paquete contra la capacidad de contexto que el PERFIL
#     del rol exige, en la escala de cuatro escalones que `esquemas/perfil-agente.yaml`
#     declara. La medida es la POSICIÓN en esa escala y no un número de tokens, porque el
#     corpus no declara tokens y escribirlos aquí sería inventarlos.
#
# DECISIÓN · COMPETENCIA exige criterio ESCRITO ANTES, y el «antes» se mide con reloj lógico
#     `C4`: «Sólo si el método lo declara, y con criterio de comparación escrito ANTES de
#     empezar». El «antes» es la mitad de la regla y es la que se evapora: un criterio
#     escrito después de ver las dos propuestas no compara, justifica. El criterio viaja con
#     el instante en que se declaró y la materialización exige que sea ESTRICTAMENTE anterior
#     al inicio del trabajo. El instante es un entero lógico y monótono —la revisión del
#     estado durable—, nunca la hora de pared: `a.9` prohíbe el reloj en el estado canónico.

MODOS_DIVERGENTES = ("divergente",)


# ===========================================================================
#  el LECTOR del campo `agentes` · vocabulario CERRADO y ENUMERADO
# ===========================================================================
# Las formas están enumeradas una a una, no adivinadas por parecido. Cada tabla de este
# bloque se contrasta contra el corpus por `exigir_censo_legible`, de modo que la lista no
# puede quedarse corta sin que algo se ponga rojo.

MODO_NINGUNO = "ninguno"
MODO_TERRITORIO = "territorio"
MODO_DIRECCION = "direccion"
MODO_ARTEFACTO = "artefacto"
MODO_SUPERFICIE = "superficie"
MODO_COMPETENCIA = "competencia"
MODO_PAQUETE = "paquete"

MODOS_DE_REPARTO = (MODO_NINGUNO, MODO_TERRITORIO, MODO_DIRECCION, MODO_ARTEFACTO,
                    MODO_SUPERFICIE, MODO_COMPETENCIA, MODO_PAQUETE)

# Los CUATRO que reparten TRABAJO, que son los de la condición (a) de `C4`. `competencia` no
# está: `C4` la separa expresamente de «varios agentes» y le pone su propia regla. `paquete`
# tampoco: `1 por paquete; varios paquetes … pueden ir en paralelo` es paralelismo de
# PAQUETES —la condición compuesta de `a.5`—, y no pluralidad de agentes sobre un rol.
MODOS_QUE_DIVIDEN_EL_TRABAJO = (MODO_TERRITORIO, MODO_DIRECCION, MODO_ARTEFACTO,
                                MODO_SUPERFICIE)

# La clave por la que el llamador declara el CONTENIDO de cada modo de reparto.
CLAVE_DE_UNIDADES = {
    MODO_TERRITORIO: "territorios",
    MODO_DIRECCION: "direcciones",
    MODO_ARTEFACTO: "artefactos",
    MODO_SUPERFICIE: "superficies",
}

_CABEZA = re.compile(r"^(?P<min>\d+)(?:\s+o\s+(?P<max>\d+))?(?P<resto>.*)$")
_COMPARTIDO = re.compile(r"^el mismo agente que (?P<rol>[a-z0-9-]+)$")

# El resto de la CABEZA, tras el cardinal. Vacío es un modo legítimo: «1» a secas.
REPARTOS_DE_CABEZA = {
    "": MODO_NINGUNO,
    "repartidos por territorio": MODO_TERRITORIO,
    "repartidos por artefacto": MODO_ARTEFACTO,
    "repartidos por superficie": MODO_SUPERFICIE,
    "repartidos por dirección": MODO_DIRECCION,
    "en competencia declarada": MODO_COMPETENCIA,
    "por paquete": MODO_PAQUETE,
}

# Cláusulas posteriores que fijan el modo. `2 o 3, uno por dirección explorada` lo hace así.
REPARTOS_DE_CLAUSULA = {
    "uno por dirección explorada": MODO_DIRECCION,
    "uno por territorio": MODO_TERRITORIO,
    "uno por artefacto": MODO_ARTEFACTO,
    "uno por superficie": MODO_SUPERFICIE,
}

# `sin integrador` está ENUMERADA a propósito, y no es un descuido de la lista cerrada: una
# composición que escribe en voz alta que no hay integrador tiene que caer por la
# PROHIBICIÓN de `C4` que viola, no por una excusa léxica. «No lo entiendo» y «lo entiendo y
# está prohibido» son dos diagnósticos distintos, y el segundo es el que hace falta.
CLAUSULA_SIN_INTEGRADOR = "sin integrador"

# La cláusula de `CON`: paralelismo de PAQUETES del mismo item, que remite a `a.5`.
CLAUSULA_DE_PARALELISMO_DE_PAQUETES = (
    "varios paquetes del mismo item pueden ir en paralelo si cumplen las seis condiciones "
    "de a.5")

# Las anáforas de separación del corpus, enumeradas. No se interpretan: se reconocen, se
# publican en el equipo escrito y quien las hace cumplir es la lista `independientes`.
ANAFORAS_DE_SEPARACION = (
    "anterior", "los anteriores", "todos los anteriores", "todos los productores",
    "los otros dos", "que enruta", "los demás",
)


def _normalizar(valor):
    return unicodedata.normalize("NFC", str(valor or "")).strip()


def leer_cardinal(valor, *, roles=()):
    """Lee el campo `agentes` de un rol. Vocabulario CERRADO; lo que no encaja, falla.

    Devuelve `minimo`, `maximo`, `modo` de reparto, con quién comparte agente, de quién se
    declara separado y si la composición niega el integrador. NUNCA devuelve un valor por
    omisión: un cardinal ilegible levanta `CardinalDeAgentesIlegible`, porque «1 por
    omisión» ante lo que no se entiende es cómo `2 o 3` acabó materializando un agente.
    """
    literal = _normalizar(valor)
    sufijos = {str(r).split("/", 1)[-1] for r in roles}
    lectura = {
        "literal": literal, "minimo": 1, "maximo": 1, "modo": MODO_NINGUNO,
        "comparte_con": None, "separado_de": [], "integrador_negado": False,
        "paralelismo_de_paquetes": False,
    }
    if not literal:
        raise CardinalDeAgentesIlegible(
            "un rol sin campo `agentes` no declara cuántos agentes lo ocupan; el esquema "
            "`composicion.yaml` lo hace obligatorio y aquí no se suple",
        )

    compartido = _COMPARTIDO.match(literal)
    if compartido:
        companero = compartido.group("rol")
        if sufijos and companero not in sufijos:
            raise CardinalDeAgentesIlegible(
                "`" + literal + "` dice compartir agente con `" + companero + "`, que no es "
                "un rol de esta composición; los suyos son " + ", ".join(sorted(sufijos)),
                valor=literal, rol=companero,
            )
        lectura["comparte_con"] = companero
        return lectura

    partes = [p.strip() for p in re.split(r"[,;]", literal)]
    cabeza, cola = partes[0], [p for p in partes[1:] if p]

    casa = _CABEZA.match(cabeza)
    if not casa:
        raise CardinalDeAgentesIlegible(
            "`" + literal + "` no empieza por un cardinal (`N` o `N o M`) ni por `el mismo "
            "agente que <rol>`; el vocabulario de `agentes` está cerrado y no se amplía "
            "adivinando", valor=literal,
        )
    minimo = int(casa.group("min"))
    maximo = int(casa.group("max") or casa.group("min"))
    if minimo < 1 or maximo < minimo:
        raise CardinalDeAgentesIlegible(
            "`" + literal + "` declara un cardinal imposible: el mínimo es 1 y el máximo no "
            "puede ser menor que el mínimo", valor=literal, minimo=minimo, maximo=maximo,
        )
    resto = casa.group("resto").strip()
    if resto not in REPARTOS_DE_CABEZA:
        raise CardinalDeAgentesIlegible(
            "`" + literal + "` declara `" + resto + "` tras el cardinal, y no es ninguna de "
            "las formas de reparto declaradas: " + ", ".join(
                "`" + f + "`" for f in sorted(REPARTOS_DE_CABEZA) if f),
            valor=literal, encontrado=resto,
        )
    lectura["minimo"], lectura["maximo"] = minimo, maximo
    lectura["modo"] = REPARTOS_DE_CABEZA[resto]

    for clausula in cola:
        if clausula in REPARTOS_DE_CLAUSULA:
            modo = REPARTOS_DE_CLAUSULA[clausula]
            if lectura["modo"] not in (MODO_NINGUNO, modo):
                raise CardinalDeAgentesIlegible(
                    "`" + literal + "` declara dos modos de reparto distintos, `"
                    + lectura["modo"] + "` y `" + modo + "`; un rol se reparte de UNA forma",
                    valor=literal,
                )
            lectura["modo"] = modo
            continue
        if clausula == CLAUSULA_SIN_INTEGRADOR:
            lectura["integrador_negado"] = True
            continue
        if clausula == CLAUSULA_DE_PARALELISMO_DE_PAQUETES:
            lectura["paralelismo_de_paquetes"] = True
            continue
        separado = _leer_separacion(clausula, literal, sufijos)
        if separado is None:
            raise CardinalDeAgentesIlegible(
                "`" + literal + "` trae la cláusula `" + clausula + "`, que no está en el "
                "vocabulario cerrado de `agentes`", valor=literal, encontrado=clausula,
            )
        lectura["separado_de"] = sorted(set(lectura["separado_de"]) | set(separado))
    return lectura


def _leer_separacion(clausula, literal, sufijos):
    """`distinto …` · devuelve la lista de referencias, o `None` si no es una separación."""
    if clausula == "distinto":
        return ["los demás"]
    if not clausula.startswith("distinto "):
        return None
    complemento = clausula[len("distinto "):].strip()
    for prefijo in ("del ", "de "):
        if complemento.startswith(prefijo):
            complemento = complemento[len(prefijo):].strip()
            break
    else:
        return None
    if complemento in ANAFORAS_DE_SEPARACION:
        return [complemento]
    referencias = []
    for pieza in complemento.split(" y "):
        pieza = pieza.strip()
        for prefijo in ("del ", "de "):
            if pieza.startswith(prefijo):
                pieza = pieza[len(prefijo):].strip()
                break
        if pieza in ANAFORAS_DE_SEPARACION:
            referencias.append(pieza)
            continue
        if sufijos and pieza in sufijos:
            referencias.append(pieza)
            continue
        return None
    return referencias or None


def censo_de_cardinales(corpus):
    """Las FORMAS del campo `agentes` en todo el corpus, con dónde aparece cada una.

    Se deriva; no se transcribe. Es el dato con el que se desmontó «esto es texto libre», y
    es el mismo dato con el que `exigir_censo_legible` impide que se vuelva a colar una
    forma que nadie ha enseñado a leer.
    """
    censo = {}
    for capacidad in CAPACIDADES:
        for composicion in corpus.composiciones(capacidad):
            for entrada in composicion.get("roles") or []:
                forma = _normalizar(entrada.get("agentes"))
                censo.setdefault(forma, []).append(
                    composicion["id"] + " · " + str(entrada.get("rol")))
    return {forma: sorted(donde) for forma, donde in sorted(censo.items())}


def exigir_censo_legible(corpus):
    """Toda forma del corpus se lee, o el corpus no se materializa. Sin excepciones.

    Es la puerta que faltaba: mientras el cardinal se declaraba por la firma, una
    composición nueva con un `agentes` que nadie entiende entraba sin ruido y se
    materializaba como uno. Ahora entra por aquí o no entra.
    """
    ilegibles = []
    for capacidad in CAPACIDADES:
        for composicion in corpus.composiciones(capacidad):
            roles = [str(e.get("rol")) for e in (composicion.get("roles") or [])]
            for entrada in composicion.get("roles") or []:
                try:
                    leer_cardinal(entrada.get("agentes"), roles=roles)
                except CardinalDeAgentesIlegible as error:
                    ilegibles.append(composicion["id"] + " · " + str(entrada.get("rol"))
                                     + " · " + error.detalle)
    if ilegibles:
        raise CardinalDeAgentesIlegible(
            "el corpus declara formas del campo `agentes` que el lector no conoce: "
            + " | ".join(sorted(ilegibles)),
            formas=sorted(ilegibles),
        )
    return True


# ===========================================================================
#  el INTEGRADOR, leído de la COMPOSICIÓN
# ===========================================================================
# `C4` exige que se declare QUIÉN INTEGRA, y la composición lo declara en `ampliacion`. Las
# dos formas están enumeradas: son las dos que el corpus usa, y una tercera forma nueva
# dejaría el integrador SIN LEER, que es lo mismo que no declararlo — y entonces la
# prohibición de `C4` salta, que es lo correcto.
_FORMAS_DE_INTEGRADOR = (
    re.compile(r"(?P<rol>[A-Z]{2,4}/[a-z0-9-]+)\s+como integrador declarado"),
    re.compile(r"(?P<rol>[A-Z]{2,4}/[a-z0-9-]+)\s+es el integrador declarado"),
)


def integrador_de(composicion):
    """El rol INTEGRADOR que la composición declara en `ampliacion`, contrastado con `roles`.

    Devuelve `None` cuando la composición no lo declara: eso NO es un defecto por sí solo
    —una composición de un agente por rol no necesita integrador—, y es exactamente lo que
    convierte en prohibido el reparto plural.
    """
    texto = _normalizar(composicion.get("ampliacion"))
    nombres = {str(e.get("rol")) for e in (composicion.get("roles") or [])}
    for forma in _FORMAS_DE_INTEGRADOR:
        casa = forma.search(texto)
        if not casa:
            continue
        rol = casa.group("rol")
        if rol not in nombres:
            raise VariosAgentesSinIntegrador(
                "la `ampliacion` de `" + str(composicion.get("id")) + "` declara integrador "
                "a `" + rol + "`, que NO es un rol de esta composición; un integrador que no "
                "ocupa ningún rol no integra nada",
                composicion=str(composicion.get("id")), integrador=rol,
            )
        return {"rol": rol, "sede": "ampliacion", "texto": texto}
    return None


def leer_paquete(capacidad, *, corpus, paquete=None, metodo=None, nivel_de_calidad=None,
                 acoplamiento=None, objetivo=None, volumen=None, inicio=None):
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

    # --- VOLUMEN del paquete: la tercera condición de `C4` para admitir varios agentes.
    # Es un recuento de unidades de trabajo —artefactos, superficies— y no un tamaño en
    # tokens: el corpus no declara tokens y escribirlos aquí sería inventar la medida.
    if volumen is None:
        lectura["volumen"] = {
            "declarado": False, "unidades": None,
            "motivo": "el paquete no declara volumen; la condición (c) de `C4` —«el volumen "
                      "excede lo que un contexto puede sostener»— no se presupone ni a "
                      "favor ni en contra",
        }
    else:
        if not isinstance(volumen, int) or isinstance(volumen, bool) or volumen < 1:
            raise PaqueteIlegible(
                "el volumen del paquete es un entero >= 1 de unidades de trabajo; llegó "
                + repr(volumen), volumen=str(volumen),
            )
        lectura["volumen"] = {"declarado": True, "unidades": int(volumen), "motivo": ""}

    # --- INICIO: el instante LÓGICO en que empieza el trabajo. Es lo que hace medible el
    # «ANTES de empezar» del criterio de comparación de la COMPETENCIA. Entero monótono del
    # estado durable —la revisión—, nunca la hora de pared: `a.9` la prohíbe en el canónico.
    if inicio is None:
        lectura["inicio"] = {
            "declarado": False, "instante": None,
            "motivo": "el paquete no declara el instante lógico de inicio; sin él no se "
                      "puede comprobar que un criterio de comparación se escribió ANTES, y "
                      "`C4` no admite competencia sin esa comprobación",
        }
    else:
        if not isinstance(inicio, int) or isinstance(inicio, bool) or inicio < 0:
            raise PaqueteIlegible(
                "el instante lógico de inicio es un entero >= 0 del estado durable; llegó "
                + repr(inicio), inicio=str(inicio),
            )
        lectura["inicio"] = {"declarado": True, "instante": int(inicio), "motivo": ""}
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


CONDICION_REPARTO = "el trabajo se reparte por artefacto o superficie sin solapamiento"
CONDICION_DIVERGENTE = "el método declara una fase divergente con exploración en paralelo"
CONDICION_VOLUMEN = "el volumen excede lo que un contexto puede sostener"
CONDICION_COMPETENCIA = "competencia declarada por el método, con criterio escrito antes"


def capacidad_de_contexto(exigencia, politica):
    """Cuántas unidades de trabajo SOSTIENE un contexto, DERIVADO de la escala del corpus.

    `esquemas/perfil-agente.yaml` declara `contexto` como un enum ORDENADO de cuatro
    escalones —`corto < medio < amplio < maximo`— y no declara ningún tamaño en tokens. La
    única medida que se puede DERIVAR sin inventar nada es la posición en esa escala, y ésa
    es la que se usa: `corto` sostiene una unidad, `maximo` cuatro. Si mañana el esquema
    declara cinco escalones, esta función devuelve cinco sin que nadie la edite.
    """
    if not exigencia or not exigencia.get("contexto"):
        return None
    return politica.indice_de_contexto(exigencia["contexto"]) + 1


def derivar_reparto(composicion, roles, *, lectura, declarado=None, asignaciones=None,
                    politica=None):
    """CUÁNTOS AGENTES por rol, derivado de la composición. `C4`, «Cuántos agentes por rol».

    El cardinal y el modo salen del campo `agentes`; el integrador, de `ampliacion`; el
    CONTENIDO del reparto —qué territorios, qué direcciones, si hay competencia y con qué
    criterio—, del llamador, porque decidir contenido no es de DSP. Las tres condiciones de
    `C4` se comprueban aquí, y ninguna se da por buena por omisión.
    """
    declarado = dict(declarado or {})
    asignaciones = dict(asignaciones or {})
    nombres = [r["rol"] for r in roles]
    ajenos = sorted(set(declarado) - set(nombres))
    if ajenos:
        raise PaqueteIlegible(
            "se declara reparto para " + ", ".join(ajenos) + ", que no son roles expandidos "
            "de esta composición", roles=ajenos,
        )
    integrador = integrador_de(composicion)
    todos = [str(e.get("rol")) for e in (composicion.get("roles") or [])]

    plan = []
    for entrada in sorted(roles, key=lambda r: r["rol"]):
        rol = entrada["rol"]
        cardinal = leer_cardinal(entrada["agentes"], roles=todos)
        contenido = dict(declarado.get(rol) or {})
        registro = asignaciones.get(rol) or {}
        capacidad = None
        if politica is not None:
            capacidad = capacidad_de_contexto(registro.get("exigencia"), politica)

        cuantos, unidades, condicion, motivo = _cuantos_agentes(
            rol, cardinal, contenido, lectura=lectura)

        # `C4` condición (c), MEDIDA: volumen declarado contra la capacidad de contexto que
        # el PERFIL del rol exige. Un volumen que no cabe y no se reparte NO se despacha: el
        # agente empezaría un trabajo que no puede sostener y lo descubriría a la mitad.
        volumen = lectura["volumen"]["unidades"] if lectura["volumen"]["declarado"] else None
        if volumen is not None and capacidad:
            necesarios = int(math.ceil(volumen / float(capacidad)))
            if necesarios > 1:
                if cardinal["modo"] not in MODOS_QUE_DIVIDEN_EL_TRABAJO:
                    raise VolumenExcedeElContexto(
                        "el paquete declara un volumen de " + str(volumen) + " unidades y el "
                        "perfil de `" + rol + "` exige un contexto `"
                        + str((registro.get("exigencia") or {}).get("contexto"))
                        + "`, que sostiene " + str(capacidad) + "; harían falta "
                        + str(necesarios) + " agentes y el rol no declara reparto en su "
                        "campo `agentes` (`" + cardinal["literal"] + "`)",
                        rol=rol, volumen=volumen, capacidad=capacidad,
                        necesarios=necesarios,
                    )
                if cuantos < necesarios:
                    raise VolumenExcedeElContexto(
                        "el paquete declara un volumen de " + str(volumen) + " unidades, `"
                        + rol + "` sostiene " + str(capacidad) + " por agente y el reparto "
                        "declarado sólo trae " + str(cuantos) + " unidad(es): faltan "
                        + str(necesarios - cuantos),
                        rol=rol, volumen=volumen, capacidad=capacidad,
                        necesarios=necesarios, declaradas=cuantos,
                    )
                condicion = CONDICION_VOLUMEN

        integra = None
        if cuantos > 1:
            if cardinal["integrador_negado"]:
                raise VariosAgentesSinIntegrador(
                    "`" + rol + "` declara `" + cardinal["literal"] + "`: " + str(cuantos)
                    + " agentes y, en el mismo campo, que NO hay integrador. `C4` lo prohíbe "
                    "con todas las letras: «Varios agentes sin integrador declarado está "
                    "prohibido», porque produce tres propuestas y ninguna decisión",
                    rol=rol, agentes=cuantos, literal=cardinal["literal"],
                )
            if integrador is None:
                raise VariosAgentesSinIntegrador(
                    "`" + rol + "` materializa " + str(cuantos) + " agentes y la composición "
                    "`" + str(composicion.get("id")) + "` no declara QUIÉN INTEGRA en su "
                    "campo `ampliacion`; `C4` lo prohíbe expresamente",
                    rol=rol, agentes=cuantos, composicion=str(composicion.get("id")),
                )
            integra = integrador["rol"]
            if condicion is None:
                raise VariosAgentesSinIntegrador(
                    "`" + rol + "` materializa " + str(cuantos) + " agentes y no consta "
                    "NINGUNA de las tres condiciones que `C4` exige para admitirlos: ni "
                    "reparto sin solapamiento, ni fase divergente declarada por el método, "
                    "ni volumen que exceda un contexto",
                    rol=rol, agentes=cuantos,
                )

        plan.append({
            "rol": rol,
            "literal": cardinal["literal"],
            "minimo": cardinal["minimo"],
            "maximo": cardinal["maximo"],
            "modo": cardinal["modo"],
            "agentes": cuantos,
            "unidades": list(unidades),
            "integra": integra,
            "integrador_de_la_composicion": integrador["rol"] if integrador else None,
            "condicion_c4": condicion,
            "criterio_de_comparacion": contenido.get("criterio_de_comparacion") or None,
            "criterio_declarado_en": contenido.get("criterio_declarado_en"),
            "comparte_con": cardinal["comparte_con"],
            "separado_de": list(cardinal["separado_de"]),
            "paralelismo_de_paquetes": cardinal["paralelismo_de_paquetes"],
            "capacidad_de_contexto": capacidad,
            "volumen_del_paquete": volumen,
            "motivo": motivo,
        })
    return plan


def _cuantos_agentes(rol, cardinal, contenido, *, lectura):
    """El cardinal EFECTIVO: `1` por defecto, y varios sólo con su condición comprobada."""
    modo = cardinal["modo"]

    if modo in MODOS_QUE_DIVIDEN_EL_TRABAJO:
        clave = CLAVE_DE_UNIDADES[modo]
        unidades = [str(u).strip() for u in (contenido.get(clave) or []) if str(u).strip()]
        if not unidades:
            raise RepartoSinUnidades(
                "`" + rol + "` declara `" + cardinal["literal"] + "`, es decir un reparto "
                "por " + modo + ", y nadie ha dicho cuáles son los `" + clave + "`. `C4` "
                "condición (a) exige que el trabajo se reparta «sin solapamiento», y eso no "
                "se puede comprobar sin las unidades. Uno es una respuesta legítima; "
                "ninguno es que nadie ha contestado",
                rol=rol, modo=modo, clave=clave, literal=cardinal["literal"],
            )
        if len(unidades) != len(set(unidades)):
            raise RepartoSinUnidades(
                "`" + rol + "` declara unidades de reparto repetidas: " + ", ".join(unidades)
                + "; `C4` exige reparto SIN SOLAPAMIENTO y dos agentes sobre la misma unidad "
                "es exactamente el solapamiento que prohíbe",
                rol=rol, modo=modo, unidades=unidades,
            )
        cuantos = len(unidades)
        if cuantos < cardinal["minimo"] or cuantos > cardinal["maximo"]:
            raise RepartoIncoherente(
                "`" + rol + "` declara `" + cardinal["literal"] + "` y se le pasan "
                + str(cuantos) + " " + CLAVE_DE_UNIDADES[modo] + "; el cardinal escrito en "
                "la composición manda, y no se estira para que quepa lo que llega",
                rol=rol, literal=cardinal["literal"], recibidos=cuantos,
            )
        return cuantos, unidades, CONDICION_REPARTO, ""

    if modo == MODO_COMPETENCIA:
        cuantos = contenido.get("competencia")
        if cuantos is None:
            # `C4` separa COMPETENCIA de «varios agentes» y la condiciona a que el MÉTODO la
            # declare. Sin declaración no hay competencia, y el cardinal es el mínimo: es el
            # «1 AGENTE por defecto, siempre» aplicado, no un silencio.
            return cardinal["minimo"], _nombres_de_competencia(cardinal["minimo"]), None, (
                "la composición admite competencia y el paquete no la declara: se "
                "materializa el mínimo del cardinal escrito")
        if not isinstance(cuantos, int) or isinstance(cuantos, bool):
            raise RepartoIncoherente(
                "`" + rol + "` declara una competencia que no es un número de agentes: "
                + repr(cuantos), rol=rol,
            )
        if cuantos < cardinal["minimo"] or cuantos > cardinal["maximo"]:
            raise RepartoIncoherente(
                "`" + rol + "` declara `" + cardinal["literal"] + "` y se pide una "
                "competencia de " + str(cuantos) + " agentes", rol=rol,
                literal=cardinal["literal"], recibidos=cuantos,
            )
        if cuantos > 1:
            _exigir_criterio_previo(rol, contenido, lectura)
            if not lectura["modo"]["fase_divergente"]:
                raise CriterioDeComparacionAusente(
                    "`" + rol + "` entra en competencia y el método del paquete NO declara "
                    "ninguna fase divergente; `C4`: la competencia vale «sólo si el método "
                    "lo declara»", rol=rol, metodo=lectura["modo"]["metodo"],
                )
        return cuantos, _nombres_de_competencia(cuantos), CONDICION_COMPETENCIA, ""

    # `ninguno` y `paquete`. El segundo NO es pluralidad de agentes: `1 por paquete; varios
    # paquetes del mismo item pueden ir en paralelo si cumplen las seis condiciones de a.5`
    # habla de PAQUETES, y quien los pone en paralelo es `paralelismo.secuenciar` con la
    # condición compuesta de `a.5`. Contarlo como una cuarta composición plural sería leer
    # mal el corpus en la dirección contraria a la del defecto que se corrige.
    if cardinal["maximo"] > cardinal["minimo"]:
        if lectura["modo"]["fase_divergente"]:
            return cardinal["maximo"], _nombres_de_competencia(cardinal["maximo"]), \
                CONDICION_DIVERGENTE, ("el método declara fase divergente y el cardinal "
                                       "escrito admite varios")
        return cardinal["minimo"], _nombres_de_competencia(cardinal["minimo"]), None, (
            "cardinal con rango y sin modo de reparto declarado: se materializa el mínimo, "
            "que es el «1 AGENTE por defecto, siempre» de `C4`")
    return cardinal["minimo"], _nombres_de_competencia(cardinal["minimo"]), (
        CONDICION_REPARTO if cardinal["minimo"] > 1 else None), ""


def _nombres_de_competencia(cuantos):
    return ["propuesta " + str(i) for i in range(1, int(cuantos) + 1)]


def _exigir_criterio_previo(rol, contenido, lectura):
    """`C4`: «con criterio de comparación escrito ANTES de empezar». El ANTES se mide."""
    criterio = str(contenido.get("criterio_de_comparacion") or "").strip()
    if not criterio:
        raise CriterioDeComparacionAusente(
            "`" + rol + "` entra en competencia y no hay criterio de comparación escrito; "
            "`C4` lo exige, y sin él la comparación la gana la propuesta que más guste "
            "cuando ya están las dos encima de la mesa", rol=rol,
        )
    declarado_en = contenido.get("criterio_declarado_en")
    if not isinstance(declarado_en, int) or isinstance(declarado_en, bool):
        raise CriterioDeComparacionAusente(
            "el criterio de comparación de `" + rol + "` no dice CUÁNDO se escribió; sin el "
            "instante lógico de su declaración, «escrito ANTES de empezar» no es "
            "comprobable y `C4` no lo da por bueno", rol=rol,
        )
    if not lectura["inicio"]["declarado"]:
        raise CriterioDeComparacionAusente(
            "hay criterio de comparación para `" + rol + "` y el paquete no declara su "
            "instante lógico de inicio: no hay contra qué medir el «ANTES»", rol=rol,
        )
    inicio = lectura["inicio"]["instante"]
    if declarado_en >= inicio:
        raise CriterioDeComparacionAusente(
            "el criterio de comparación de `" + rol + "` se declaró en el instante "
            + str(declarado_en) + " y el trabajo empieza en el " + str(inicio) + ": no es "
            "ANTES. Un criterio escrito con las propuestas delante no compara, justifica",
            rol=rol, declarado_en=declarado_en, inicio=inicio,
        )
    return True


# ===========================================================================
#  el algoritmo de `C4`
# ===========================================================================
def materializar(capacidad, *, corpus=None, composiciones_verdaderas=(),
                 condiciones_de_rol=(), slots=SLOTS_POR_DEFECTO, metodo=None,
                 paquete=None, control_repo=None, catalogo=None, degradaciones=None,
                 politica=None, nivel_de_calidad=None, acoplamiento=None, objetivo=None,
                 reparto_declarado=None, capacidad_responsable=None, volumen=None,
                 inicio=None, equipo_previo=None):
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
        volumen=volumen, inicio=inicio,
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

    # `C4`, «Cuántos agentes por rol»: DERIVADO del campo `agentes` de la composición, con
    # el integrador leído de su `ampliacion` y las tres condiciones comprobadas. Va aquí,
    # después del paso 4, porque la condición (c) —volumen contra contexto— necesita la
    # exigencia de perfil que el paso 4 acaba de resolver.
    plan_de_reparto = derivar_reparto(
        elegida, roles, lectura=lectura, declarado=reparto_declarado,
        asignaciones=asignaciones, politica=politica,
    )
    plan_por_rol = {p["rol"]: p for p in plan_de_reparto}
    plurales = {p["rol"] for p in plan_de_reparto if p["agentes"] > 1}


    # PASO 5 · APLICAR COMBINACIÓN, con `independientes` mandando sobre `combinables`, y
    # sobre el CIERRE de las combinaciones: encadenar A-B y B-C no puede colar A con C.
    independientes = _independientes(elegida)
    combinaciones = []
    grupos = {nombre: (nombre,) for nombre in nombres}
    for entrada in elegida.get("combinables") or []:
        pareja = [str(r) for r in (entrada.get("roles") or [])]
        motivo = str(entrada.get("motivo") or "")
        condicion = str(entrada.get("condicion") or "").strip()
        pluralidad = sorted(r for r in pareja if r in plurales)
        if pluralidad:
            # `C4` paso 5 concede compartir agente; el reparto plural declara lo contrario
            # sobre el mismo rol. Aplicar la combinación obligaría a decidir cuál de los
            # tres agentes del rol ocupa además el otro rol, y esa decisión no está en
            # ninguna sede. La combinación NO se aplica, y queda escrito por qué.
            combinaciones.append({
                "roles": pareja, "aplicada": False,
                "motivo": "`" + ", ".join(pluralidad) + "` materializa varios agentes por "
                          "`C4`, y una combinación es UN agente ocupando dos roles: no se "
                          "puede aplicar sin elegir a cuál de los varios, y eso no lo "
                          "declara nadie",
            })
            continue
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
                unidades.extend(_replicar(
                    _agente_del_grupo(
                        (miembro,), asignaciones, politica=politica,
                        catalogo=catalogo_efectivo, degradaciones=degradaciones)
                    or _unidad_bloqueada((miembro,), asignaciones),
                    plan_por_rol.get(miembro)))
            continue
        unidades.extend(_replicar(unidad, plan_por_rol.get(grupo[0]) if len(grupo) == 1
                                  else None))

    # PASO 6 · COMPROBAR LÍMITES. La unidad que ocupa un slot es el AGENTE (`b.11`: la
    # concurrencia se calcula «a partir de agentes disponibles»), NUNCA el rol: por eso un
    # par combinable ocupa UN slot y jamás queda a los dos lados del corte.
    unidades.sort(key=lambda u: (u["roles"][0], _indice_de_reparto(u), u["modelo"] or "",
                                 u["agente"] or ""))
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
                # La ASIGNACIÓN DURABLE de ESTE agente: qué unidad del reparto ocupa, con
                # qué modo, con qué criterio y quién integra. Sin esto el registro publicaba
                # el cardinal por un lado y un agente por otro, sin nada que los uniera.
                "reparto": dict(unidad["reparto"]) if unidad.get("reparto") else None,
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
        "reparto_de_agentes": plan_de_reparto,
        "integrador": (integrador_de(elegida) or {}).get("rol"),
        "composicion": elegida["id"],
        "clase_de_trabajo": str(elegida.get("clase_de_trabajo") or ""),
        "condicion_que_la_eligio": str(elegida.get("condicion") or "").strip(),
        "composiciones_descartadas": descartadas,
        "roles": sorted(asignados, key=_orden_de_fila),
        "esperando_capacidad": sorted(esperando, key=_orden_de_fila),
        "bloqueados": sorted(bloqueados, key=_orden_de_fila),
        "roles_fuera": sorted(fuera, key=lambda r: r["rol"]),
        "combinaciones": sorted(combinaciones, key=lambda c: (tuple(c["roles"]),
                                                             c["aplicada"], c["motivo"])),
        "independientes": sorted(independientes, key=lambda i: i["rol"]),
        "agentes": sorted(unidades, key=lambda u: (u["roles"][0], _indice_de_reparto(u),
                                                   u["agente"] or "")),
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
    exigir_reparto_coherente(equipo)
    if equipo_previo is not None:
        exigir_reparto_reanudado(equipo_previo, equipo)
    return equipo


def _indice_de_reparto(unidad):
    return int((unidad.get("reparto") or {}).get("indice") or 0)


def _orden_de_fila(fila):
    """Orden TOTAL de las filas: mismo estado, misma salida byte a byte.

    Con reparto plural un mismo rol aparece varias veces, y ordenar sólo por `rol` dejaba el
    desempate al orden de inserción. `I-g3` exige determinismo, y un desempate implícito no
    lo es: se ordena por rol, índice de la unidad y agente.
    """
    return (fila["rol"], int((fila.get("reparto") or {}).get("indice") or 0),
            fila.get("agente") or "")


def _replicar(unidad, plan):
    """Un AGENTE REAL por cada unidad del reparto. Con cardinal 1 devuelve la unidad tal cual.

    Aquí es donde «2 o 3» deja de ser una cadena en el registro y pasa a ser dos o tres
    agentes que ocupan dos o tres `execution_slots`. `b.11` calcula la concurrencia «a partir
    de agentes disponibles»: si el reparto no se replica, el corte del paso 6 cuenta uno
    donde hay tres y el límite deja de limitar.
    """
    if plan is None or int(plan.get("agentes") or 1) <= 1:
        copia = dict(unidad)
        copia["reparto"] = None
        return [copia]
    salida = []
    for indice, nombre in enumerate(plan["unidades"], start=1):
        copia = dict(unidad)
        copia["roles"] = list(unidad["roles"])
        copia["reparto"] = {
            "rol": plan["rol"],
            "modo": plan["modo"],
            "unidad": nombre,
            "indice": indice,
            "de": plan["agentes"],
            "integra": plan["integra"],
            "condicion_c4": plan["condicion_c4"],
            "criterio_de_comparacion": plan["criterio_de_comparacion"],
        }
        if unidad["modelo"]:
            copia["agente"] = politica_de_agentes.identificador_de_agente(
                unidad["modelo"], unidad["roles"],
                reparto=plan["modo"] + ":" + str(indice) + ":" + nombre)
        salida.append(copia)
    return salida


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
    # Un rol REPARTIDO aparece tantas veces como agentes materializa, y sus agentes pueden
    # quedar a los dos lados del corte —eso es correcto: lo que no cabe ESPERA—. Lo que no
    # puede repetirse es la UNIDAD del reparto: dos veces la misma dirección explorada es
    # solapamiento, y `C4` condición (a) lo prohíbe con esas palabras.
    vistos = {}
    for lista in ("roles", "esperando_capacidad", "bloqueados"):
        for fila in equipo.get(lista) or []:
            clave = (fila["rol"], int((fila.get("reparto") or {}).get("indice") or 0))
            if clave in vistos:
                raise AgenteSobreasignado(
                    "el rol `" + fila["rol"] + "` aparece dos veces con la misma unidad de "
                    "reparto, en `" + vistos[clave] + "` y en `" + lista + "`: un agente "
                    "ocupa un estado, no dos",
                    rol=fila["rol"],
                )
            vistos[clave] = lista
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


def exigir_reparto_coherente(equipo):
    """El registro durable NO puede afirmar a la vez una cosa y su contraria.

    DEFECTO QUE CIERRA, medido por la auditoría: el equipo publicaba `agentes: "2 o 3"` en la
    fila del rol y UN agente en la lista de agentes, con `reparto_de_agentes` vacío. Un
    registro internamente contradictorio no es un registro: es dos afirmaciones y ninguna
    verdad, y el paso 7 de `C4` existe justamente para lo contrario. Si publica «2 o 3»,
    publica dos o tres agentes.
    """
    filas = []
    for lista in ("roles", "esperando_capacidad", "bloqueados"):
        filas.extend(equipo.get(lista) or [])
    por_rol = {}
    for fila in filas:
        por_rol.setdefault(fila["rol"], []).append(fila)
    for plan in equipo.get("reparto_de_agentes") or []:
        materializadas = por_rol.get(plan["rol"]) or []
        if len(materializadas) != int(plan["agentes"]):
            raise RepartoIncoherente(
                "el equipo publica para `" + plan["rol"] + "` el cardinal `"
                + plan["literal"] + "` con " + str(plan["agentes"]) + " agente(s) derivados, "
                "y en sus listas hay " + str(len(materializadas)),
                rol=plan["rol"], literal=plan["literal"],
                derivados=int(plan["agentes"]), publicados=len(materializadas),
            )
        if not (plan["minimo"] <= plan["agentes"] <= plan["maximo"]):
            raise RepartoIncoherente(
                "`" + plan["rol"] + "` declara `" + plan["literal"] + "` y materializa "
                + str(plan["agentes"]) + " agentes, fuera del cardinal escrito",
                rol=plan["rol"], literal=plan["literal"],
            )
        if plan["agentes"] > 1 and not plan["integra"]:
            raise RepartoIncoherente(
                "`" + plan["rol"] + "` materializa " + str(plan["agentes"]) + " agentes y el "
                "registro no publica integrador", rol=plan["rol"],
            )
        unidades = [str((f.get("reparto") or {}).get("unidad")) for f in materializadas]
        if plan["agentes"] > 1 and len(set(unidades)) != len(unidades):
            raise RepartoIncoherente(
                "`" + plan["rol"] + "` publica dos agentes sobre la misma unidad de reparto: "
                + ", ".join(sorted(unidades)), rol=plan["rol"],
            )
    return True


def firma_de_reparto(equipo):
    """Lo que NO puede cambiar al reanudar: rol, cardinal, modo, agentes, unidades, integrador."""
    return [
        (p["rol"], p["literal"], p["modo"], int(p["agentes"]), tuple(p["unidades"]),
         p["integra"])
        for p in sorted(equipo.get("reparto_de_agentes") or [], key=lambda p: p["rol"])
    ]


def exigir_reparto_reanudado(previo, actual):
    """Reanudar NO puede cambiar el reparto en silencio. Si difiere, se dice y se para.

    `C4` «Ampliación y reducción»: el equipo NO se rehace, se AÑADE lo que falta. Un reparto
    que cambia al volver a materializar deja agentes del intento anterior trabajando sobre
    unidades que ya no existen, y nadie se entera: los artefactos aparecen huérfanos tres
    pasos después. Es la misma familia de defecto que `esperando-capacidad` vino a impedir.
    """
    antes, ahora = firma_de_reparto(previo), firma_de_reparto(actual)
    if antes != ahora:
        cambiados = sorted({f[0] for f in set(antes) ^ set(ahora)})
        raise RepartoIncoherente(
            "la reanudación cambia el reparto ya escrito del equipo `"
            + str(previo.get("id")) + "`: " + ", ".join(cambiados) + ". `C4` no rehace el "
            "equipo al ampliar, y un reparto distinto deja al agente anterior trabajando "
            "sobre una unidad que ya no está declarada",
            equipo=str(previo.get("id")), roles=cambiados,
            antes=[list(f) for f in antes], ahora=[list(f) for f in ahora],
        )
    return True


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
