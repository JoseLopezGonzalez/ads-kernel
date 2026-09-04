#!/usr/bin/env python3
"""errores — la jerarquía tipada de fallos del CICLO de `§7.2` y de `Continúa` de `§7.4`.

Misma forma que `estado/errores.py` y `runtime/errores.py`, y por las mismas razones, que
no se repiten aquí y se citan: el `codigo` vive en la CLASE y es el contrato ESTABLE que la
evidencia publicada compara; el `detalle` es texto castellano y se puede reescribir sin
romper nada; y la ruta se SANEA EN EL CONSTRUCTOR reutilizando `estado.errores.relativizar`,
que ya está escrito y probado, en vez de escribir aquí un tercer saneador que pueda
desincronizarse de los otros dos.

DECISIÓN · TERCERA raíz, y no una rama de las dos que ya existen
    Alternativas: (a) colgar `ErrorDeCiclo` de `ErrorDeRuntime`, porque el ciclo se apoya en
    el runtime; (b) colgarlo de `ErrorDeEstado`; (c) una raíz propia.
    Se elige (c). El argumento es el mismo que `runtime/errores.py` da para no colgar de
    `ErrorDeEstado`, un piso más arriba: un fallo del MOTOR —revisión obsoleta—, un fallo del
    RUNTIME —autoridad perdida— y un fallo del CICLO —`composicion-incompleta`— tienen
    consecuencias y autoridades distintas. `composicion-incompleta` NO ABRE LA FASE y escala
    a una autoridad semántica; `AutoridadPerdida` no escala a nadie y se reintenta en la
    pasada siguiente. Con (a), un `except ErrorDeRuntime` escrito para tolerar contención
    tragaría una composición incompleta, que es exactamente lo que `§8.0` manda no tragar.
    El precio —tres raíces y tres `except` en la CLI— se paga explícitamente y está en
    `ads_ciclo.py`.

DECISIÓN · `composicion-incompleta` lleva SIEMPRE capacidad y fase en su `contexto`
    `§8.0` no dice «falla»: dice «la fase NO abre, DSP para y escala **nombrando la
    capacidad y la fase**». Un error que no las nombra no cumple el contrato aunque pare.
    El constructor de `ComposicionIncompleta` las exige, y sin ellas levanta
    `CicloInconsistente`: un fallo cerrado del propio mecanismo de fallo cerrado.
"""
from __future__ import annotations

from estado.errores import relativizar


class ErrorDeCiclo(Exception):
    """Raíz de todo fallo del ciclo. Nadie captura `Exception` por encima de ésta."""

    CODIGO = "ERROR_DE_CICLO"

    def __init__(self, detalle="", ruta=None, codigo=None, **contexto):
        self.codigo = codigo or self.CODIGO
        self.detalle = detalle
        self.ruta = relativizar(ruta)
        self.contexto = dict(contexto)
        super().__init__(str(self))

    def __str__(self):
        partes = ["[" + self.codigo + "]"]
        if self.detalle:
            partes.append(self.detalle)
        if self.ruta:
            partes.append("(" + str(self.ruta) + ")")
        return " ".join(partes)

    def a_dict(self):
        """Forma determinista del error, apta para `--json` y para evidencia publicada."""
        salida = {"codigo": self.codigo, "detalle": self.detalle, "ruta": self.ruta}
        if self.contexto:
            salida["contexto"] = {c: self.contexto[c] for c in sorted(self.contexto)}
        return salida


# ------------------------------------------------------------------- corpus
class CorpusIlegible(ErrorDeCiclo):
    """Un bloque canónico del kernel no se puede leer. NO se adivina su contenido."""

    CODIGO = "CORPUS_ILEGIBLE"


class CorpusIncompleto(ErrorDeCiclo):
    """El corpus no declara algo que el ciclo necesita —un proceso, un gate, un handoff."""

    CODIGO = "CORPUS_INCOMPLETO"


# ------------------------------------------------------------------ encuadre
class EntradaNoClasificable(ErrorDeCiclo):
    """La expresión del Owner no cae en ninguna de las NUEVE clases de la taxonomía."""

    CODIGO = "ENTRADA_NO_CLASIFICABLE"


class EncuadreIncompleto(ErrorDeCiclo):
    """Falta un campo estructural del encuadre. Sin él no se puede componer ruta."""

    CODIGO = "ENCUADRE_INCOMPLETO"


class PrecondicionIncumplida(ErrorDeCiclo):
    """Una precondición declarada del encuadre o del proceso no se cumple."""

    CODIGO = "PRECONDICION_INCUMPLIDA"


class EntradaSinTrabajo(ErrorDeCiclo):
    """SEÑAL, no defecto: la clase de entrada NO crea trabajo (regla 2 de la taxonomía).

    Seis de las nueve clases se registran, se anclan y esperan. Pedirle a `componer` que
    haga una ruta con una de ellas es el error; que la entrada no cree trabajo, no.
    """

    CODIGO = "ENTRADA_SIN_TRABAJO"


# --------------------------------------------------------- proceso y ruta
class ProcesoDesconocido(ErrorDeCiclo):
    """El identificador no está entre los diez de `b.16` declarados en el corpus."""

    CODIGO = "PROCESO_DESCONOCIDO"


class MateriaSinProceso(ErrorDeCiclo):
    """La materia declarada no tiene proceso en la correspondencia DECLARADA de `b.16`."""

    CODIGO = "MATERIA_SIN_PROCESO"


class EstadoDeMateriaInvalido(ErrorDeCiclo):
    """La materia y el estado del objeto no son compatibles: `b.1` no admite ese par."""

    CODIGO = "ESTADO_DE_MATERIA_INVALIDO"


class PropietarioNoDerivable(ErrorDeCiclo):
    """`AUD` y `DIR` DERIVAN su propietario del encargo, y el encargo no lo trae."""

    CODIGO = "PROPIETARIO_NO_DERIVABLE"


class ViaInvalida(ErrorDeCiclo):
    """Una capacidad entra por una vía que no es ninguna de las CUATRO de `§8.0`."""

    CODIGO = "VIA_INVALIDA"


class CondicionVaga(ErrorDeCiclo):
    """Una condición de la vía 3 no es comprobable. `b.16` la prohíbe con su fórmula."""

    CODIGO = "CONDICION_VAGA"


class ComposicionIncompleta(ErrorDeCiclo):
    """`§8.0`: la fase NO ABRE. DSP para y escala nombrando la capacidad y la fase."""

    CODIGO = "COMPOSICION_INCOMPLETA"

    def __init__(self, detalle="", *, capacidad=None, fase=None, ruta=None, **contexto):
        if not capacidad or not fase:
            raise CicloInconsistente(
                "`composicion-incompleta` se emite SIEMPRE nombrando la capacidad y la "
                "fase: sin ellas el error para, pero no escala a nadie, y `§8.0` exige "
                "las dos cosas",
                capacidad=str(capacidad), fase=str(fase),
            )
        contexto["capacidad"] = capacidad
        contexto["fase"] = fase
        super().__init__(detalle, ruta=ruta, **contexto)


# --------------------------------------------------------------- equipos
class ComposicionDeEquipoAusente(ErrorDeCiclo):
    """Ninguna `condicion` de las composiciones de la capacidad es verdadera (`C4`, paso 2)."""

    CODIGO = "COMPOSICION_DE_EQUIPO_AUSENTE"


class ConflictoDeRoles(ErrorDeCiclo):
    """Se pretende combinar dos roles que la composición declara `independientes` (`C4`)."""

    CODIGO = "CONFLICTO_DE_ROLES"


class MetodoNoEsCapacidad(ErrorDeCiclo):
    """Se pasó un MÉTODO donde el contrato exige una CAPACIDAD. Son cosas distintas."""

    CODIGO = "METODO_NO_ES_CAPACIDAD"


# --------------------------------------------------- agentes y modelos (`C2`)
class CatalogoDeModelosAusente(ErrorDeCiclo):
    """El PROYECTO no declara catálogo de modelos. `C2` lo sitúa en su `PROFILE`.

    FALLO CERRADO: sin catálogo no hay agente que asignar, y el kernel NO puede traer uno
    por defecto sin nombrar un proveedor, que es lo que `K0.8` prohíbe.
    """

    CODIGO = "CATALOGO_DE_MODELOS_AUSENTE"


class CatalogoDeModelosInvalido(ErrorDeCiclo):
    """El catálogo del proyecto no es el ESPEJO del esquema `perfil-agente`."""

    CODIGO = "CATALOGO_DE_MODELOS_INVALIDO"


class PerfilDesconocido(ErrorDeCiclo):
    """El rol no declara `perfil_agente`, o el perfil que declara no está en el corpus."""

    CODIGO = "PERFIL_DESCONOCIDO"


class RolSinAgente(ErrorDeCiclo):
    """`C4`: «PROHIBIDO materializar un rol sin asignarle agente: un rol vacío no es un rol»."""

    CODIGO = "ROL_SIN_AGENTE"


class AgenteSobreasignado(ErrorDeCiclo):
    """Un agente ocupa un slot dos veces, o dos agentes ocupan el mismo slot (`b.11`)."""

    CODIGO = "AGENTE_SOBREASIGNADO"


class DegradacionInvalida(ErrorDeCiclo):
    """Una degradación se DECLARA con sus ejes, su motivo y quién la autoriza (`C2` paso 6)."""

    CODIGO = "DEGRADACION_INVALIDA"


# ----------------------------------------------------------- planificación
class PlanificacionInvalida(ErrorDeCiclo):
    CODIGO = "PLANIFICACION_INVALIDA"


class LimiteDeCapacidadExcedido(ErrorDeCiclo):
    """SEÑAL: lo que no cabe en `execution_slots` espera. NO se reduce la composición."""

    CODIGO = "LIMITE_DE_CAPACIDAD_EXCEDIDO"


class AlcanceNoAutorizado(ErrorDeCiclo):
    """`b.15.1`: el desbloqueador sale del alcance autorizado. Se escala, no se despacha."""

    CODIGO = "ALCANCE_NO_AUTORIZADO"


# ----------------------------------------------------------------- gates
class GateDesconocido(ErrorDeCiclo):
    """El gate no está en el censo DERIVADO del corpus. No se inventan gates."""

    CODIGO = "GATE_DESCONOCIDO"


class GateFallido(ErrorDeCiclo):
    """El dictamen es NEGATIVO. Fallo CERRADO: la salida del gate no se produce."""

    CODIGO = "GATE_FALLIDO"


class GateNormativo(ErrorDeCiclo):
    """Un gate intentó escribir norma o ampliar el proceso. Ningún gate es fuente normativa."""

    CODIGO = "GATE_NORMATIVO"


# -------------------------------------------------------------- handoffs
class HandoffDesconocido(ErrorDeCiclo):
    CODIGO = "HANDOFF_DESCONOCIDO"


class HandoffIncompleto(ErrorDeCiclo):
    """Faltan campos de los ONCE que `esquemas/handoff.yaml` declara obligatorios."""

    CODIGO = "HANDOFF_INCOMPLETO"


class HandoffRechazado(ErrorDeCiclo):
    """`C5`: quien recibe comprobó ANTES de tomar custodia y rechazó. NO cambia de custodia."""

    CODIGO = "HANDOFF_RECHAZADO"


class DevolucionSinEvidencia(ErrorDeCiclo):
    """`C5`: una devolución sin los CUATRO campos se rechaza COMO devolución."""

    CODIGO = "DEVOLUCION_SIN_EVIDENCIA"


# ----------------------------------------------------------------- cierre
class ObligacionHuerfana(ErrorDeCiclo):
    """Ni satisfecha ni retirada. `gate:cierre-de-item` no deja cerrar."""

    CODIGO = "OBLIGACION_HUERFANA"


class RetiradaSinAutoridad(ErrorDeCiclo):
    """DSP NO RETIRA. Retirar es autoridad semántica (regla dura 2 de `00-OBLIGACIONES`)."""

    CODIGO = "RETIRADA_SIN_AUTORIDAD"


class CierreBloqueado(ErrorDeCiclo):
    CODIGO = "CIERRE_BLOQUEADO"


# ------------------------------------------------------------ continuación
class DecisionDelOwnerPendiente(ErrorDeCiclo):
    """El plan de continuación exige al Owner. NO se ejecuta de forma no interactiva."""

    CODIGO = "DECISION_DEL_OWNER_PENDIENTE"


class TrabajoAmbiguo(ErrorDeCiclo):
    """Dos lecturas del estado son igual de defendibles. `b.14.3`: se para y se escala."""

    CODIGO = "TRABAJO_AMBIGUO"


class DerivaNoTransaccional(ErrorDeCiclo):
    """Hay cambios en el árbol que el diario no explica. Se REPORTA y se ESCALA."""

    CODIGO = "DERIVA_NO_TRANSACCIONAL"


class CicloInconsistente(ErrorDeCiclo):
    """FALLO CERRADO ante un estado que no casa con ninguna regla. Nunca se inventa estado."""

    CODIGO = "CICLO_INCONSISTENTE"


class PaqueteIlegible(ErrorDeCiclo):
    """`C4` paso 1 · el paquete no se puede LEER: una de sus cinco materias no resuelve.

    El paso 1 dejó de ser un passthrough y pasó a resolver método, nivel de calidad y
    acoplamiento contra sus sedes. Resolver de verdad crea la posibilidad de no resolver, y
    eso tiene que fallar cerrado: materializar con un método que no es de la capacidad, o
    con un nivel de calidad que no está en la escala, sería inventar la lectura.
    """

    CODIGO = "PAQUETE_ILEGIBLE"


class VariosAgentesSinIntegrador(ErrorDeCiclo):
    """`C4`: «Varios agentes sin integrador declarado está prohibido».

    Su motivo está escrito en el contrato: «Produce tres propuestas y ninguna decisión, que
    es ceremonia con apariencia de profundidad».
    """

    CODIGO = "VARIOS_AGENTES_SIN_INTEGRADOR"



class CardinalDeAgentesIlegible(ErrorDeCiclo):
    """`C4`, «Cuántos agentes por rol» · el campo `agentes` no encaja en NINGUNA forma.

    El comentario que este error deroga decía que `agentes` era prosa y que derivar de ahí
    un cardinal «exigiría reglas léxicas sobre texto libre». La medición lo desmintió: el
    campo tiene noventa y nueve valores en VEINTIDÓS formas, y esas veintidós son un
    vocabulario CERRADO. Lo que no se puede hacer es leerlo a medias: si aparece una forma
    que el lector no conoce, la composición NO se materializa. Suponer «1 por omisión»
    ante un valor ilegible es exactamente cómo `2 o 3` acabó produciendo un agente.
    """

    CODIGO = "CARDINAL_DE_AGENTES_ILEGIBLE"


class RepartoSinUnidades(ErrorDeCiclo):
    """`C4` condición (a) · se declara reparto por territorio, dirección, artefacto o
    superficie, y NADIE dice cuáles son.

    «El trabajo se reparte por artefacto o superficie SIN SOLAPAMIENTO» no se puede
    comprobar sin saber cuáles son los artefactos. Con cero unidades declaradas no hay una
    respuesta por defecto: un territorio es una respuesta legítima; ninguno es que nadie ha
    contestado, y repartir sin saber entre qué es inventar la división.
    """

    CODIGO = "REPARTO_SIN_UNIDADES"


class CriterioDeComparacionAusente(ErrorDeCiclo):
    """`C4` COMPETENCIA · «con criterio de comparación escrito ANTES de empezar».

    El «antes» es la mitad de la regla y es la que se pierde siempre: un criterio escrito
    después de ver las dos propuestas no compara, justifica la que ya gustaba. Por eso el
    criterio viaja con el instante lógico en que se declaró y la materialización exige que
    sea ANTERIOR al inicio del trabajo.
    """

    CODIGO = "CRITERIO_DE_COMPARACION_AUSENTE"


class VolumenExcedeElContexto(ErrorDeCiclo):
    """`C4` condición (c) · «el volumen excede lo que un contexto puede sostener».

    Es la única de las tres condiciones que se puede MEDIR con lo que el corpus ya declara,
    y por eso se mide: el volumen del paquete contra la capacidad de contexto del agente. Si
    excede y el rol no declara reparto, el trabajo no cabe y no se despacha a ciegas.
    """

    CODIGO = "VOLUMEN_EXCEDE_EL_CONTEXTO"


class RepartoIncoherente(ErrorDeCiclo):
    """El registro durable del equipo afirmaría a la vez una cosa y su contraria.

    Los dos casos: publicar «2 o 3» junto a UN agente —lo que la auditoría midió—, y
    reanudar una materialización cambiando en silencio el reparto ya escrito. Los dos
    producen un registro que nadie puede creer, y `C4` paso 7 existe para lo contrario.
    """

    CODIGO = "REPARTO_INCOHERENTE"


class ObligacionSinProductora(ErrorDeCiclo):
    """Una obligación que no declara NI capacidad NI autoridad que produzca su capa.

    `F-02` separó las dos claves para que `OWNER` dejara de viajar como capacidad. La
    separación crea un estado nuevo que antes no existía —ninguna de las dos— y que sería
    indistinguible de una capa sin dueño. Falla cerrado en vez de elegir una por defecto.
    """

    CODIGO = "OBLIGACION_SIN_PRODUCTORA"


# Censo derivado, no escrito a mano dos veces: la CLI y las pruebas lo usan para comprobar
# que todo código emitido pertenece a esta lista cerrada.
CLASES = (
    ObligacionSinProductora, PaqueteIlegible, VariosAgentesSinIntegrador,
    CardinalDeAgentesIlegible, RepartoSinUnidades, CriterioDeComparacionAusente,
    VolumenExcedeElContexto, RepartoIncoherente,
    ErrorDeCiclo, CorpusIlegible, CorpusIncompleto,
    EntradaNoClasificable, EncuadreIncompleto, PrecondicionIncumplida, EntradaSinTrabajo,
    ProcesoDesconocido, MateriaSinProceso, EstadoDeMateriaInvalido, PropietarioNoDerivable,
    ViaInvalida, CondicionVaga, ComposicionIncompleta,
    ComposicionDeEquipoAusente, ConflictoDeRoles, MetodoNoEsCapacidad,
    CatalogoDeModelosAusente, CatalogoDeModelosInvalido, PerfilDesconocido,
    RolSinAgente, AgenteSobreasignado, DegradacionInvalida,
    PlanificacionInvalida, LimiteDeCapacidadExcedido, AlcanceNoAutorizado,
    GateDesconocido, GateFallido, GateNormativo,
    HandoffDesconocido, HandoffIncompleto, HandoffRechazado, DevolucionSinEvidencia,
    ObligacionHuerfana, RetiradaSinAutoridad, CierreBloqueado,
    DecisionDelOwnerPendiente, TrabajoAmbiguo, DerivaNoTransaccional, CicloInconsistente,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
