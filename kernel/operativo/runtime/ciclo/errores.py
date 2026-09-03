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


# Censo derivado, no escrito a mano dos veces: la CLI y las pruebas lo usan para comprobar
# que todo código emitido pertenece a esta lista cerrada.
CLASES = (
    ErrorDeCiclo, CorpusIlegible, CorpusIncompleto,
    EntradaNoClasificable, EncuadreIncompleto, PrecondicionIncumplida, EntradaSinTrabajo,
    ProcesoDesconocido, MateriaSinProceso, EstadoDeMateriaInvalido, PropietarioNoDerivable,
    ViaInvalida, CondicionVaga, ComposicionIncompleta,
    ComposicionDeEquipoAusente, ConflictoDeRoles, MetodoNoEsCapacidad,
    PlanificacionInvalida, LimiteDeCapacidadExcedido, AlcanceNoAutorizado,
    GateDesconocido, GateFallido, GateNormativo,
    HandoffDesconocido, HandoffIncompleto, HandoffRechazado, DevolucionSinEvidencia,
    ObligacionHuerfana, RetiradaSinAutoridad, CierreBloqueado,
    DecisionDelOwnerPendiente, TrabajoAmbiguo, DerivaNoTransaccional, CicloInconsistente,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
