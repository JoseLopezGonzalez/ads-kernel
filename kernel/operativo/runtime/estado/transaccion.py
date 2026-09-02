#!/usr/bin/env python3
"""transaccion — la unidad de cambio y las formas deterministas que el motor devuelve.

`g.14` lo dice sin rodeos: **la unidad aislada de trabajo es la TRANSACCIÓN, no la rama**.
Aquí vive esa unidad —`Transicion`, con sus operaciones— y los informes que el §9 exige que
sean `dataclass` con `a_dict()` determinista.

DECISIÓN · operaciones DECLARATIVAS (`Escritura`/`Borrado`), no un callback
    Alternativas: (a) que el llamador pase una función que mute el árbol; (b) que declare
    la lista de operaciones y el motor las ejecute.
    Se elige (b). Con (a) el diario no podría registrar QUÉ se iba a hacer antes de hacerlo,
    y sin eso la rama COMPLETAR de `g.8` es imposible: reejecutar los pasos 8 a 10 exige
    saber, después del corte y sin el proceso original, qué objetos había que publicar y con
    qué `cid`. Con (b) el evento `transicion.preparada` contiene el plan entero, y la
    recuperación no necesita adivinar nada —«sin INVENTAR ESTADO», `I-g2`—.

DECISIÓN · el `cid` esperado forma parte de la operación desde el principio
    Se calcula al validar, antes de escribir un solo byte. Así el evento `transicion.abierta`
    ya declara el resultado esperado, y una recuperación puede comparar byte a byte contra
    él. Si el `cid` se calculase al publicar, el diario describiría lo que pasó en vez de lo
    que debía pasar, y la comprobación se volvería circular.

DECISIÓN · `a_dict()` ordena y no incluye rutas absolutas ni tiempos
    El §12.1 exige que el escenario extremo a extremo dé BYTES IDÉNTICOS en dos ejecuciones
    seguidas. Cualquier ruta de máquina, duración o pid en un informe lo impediría, y además
    `I-g3` lo prohíbe para los artefactos derivados. Los informes sólo llevan rutas lógicas,
    digests y números de secuencia.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .errores import TransicionInvalida
from .rutas import comprobar_identificador, comprobar_ruta_logica
from .serializacion import (
    calcular_cid_raiz,
    calcular_revision_id,
    cid_corto,
    cid_de_objeto,
    con_esquema,
)

ACCION_ESCRIBIR = "escribir"
ACCION_BORRAR = "borrar"


@dataclass
class Escritura:
    """Publicar `contenido` en la ruta lógica `ruta`. El `esquema` lo pone el motor."""

    ruta: str
    contenido: Dict[str, Any]

    def normalizada(self):
        """El contenido con `esquema` puesto, que es lo que de verdad se escribirá."""
        return con_esquema(self.contenido)

    def cid(self):
        return cid_de_objeto(self.normalizada())

    def a_dict(self):
        return {"accion": ACCION_ESCRIBIR, "ruta": self.ruta, "cid": self.cid()}


@dataclass
class Borrado:
    """Retirar la ruta lógica `ruta` del estado canónico."""

    ruta: str

    def a_dict(self):
        # Sin `cid`: el `cid` de lo que se retira lo aporta la revisión base, y duplicarlo
        # aquí abriría la puerta a que ambos discrepasen y a que nadie supiera cuál manda.
        return {"accion": ACCION_BORRAR, "ruta": self.ruta}


class Transicion:
    """Una transacción declarada: qué cambia, desde qué base, quién y por qué."""

    def __init__(self, *, tipo, base, operaciones, autor, motivo, id):
        self.tipo = tipo
        self.base = base
        self.operaciones = list(operaciones)
        self.autor = autor
        self.motivo = motivo
        self.id = id
        self.validar_forma()

    def validar_forma(self):
        """Lo que hace que la transición sea SIQUIERA una transición. Se exige al construir.

        Aquí sólo entra lo que no depende de ningún estado: el identificador, el tipo, la
        forma de la base y —lo importante— las RUTAS. Las rutas se validan en el
        constructor a propósito: una ruta que se escapa del árbol no es un dato malo, es
        una escritura fuera de `canonico/` esperando a ocurrir, y cuanto más lejos de la
        escritura se detecte, menos probable es que alguien la construya «para más tarde».

        Lo que NO entra aquí es lo que decide si la transición tiene SENTIDO —autor,
        motivo, y que cambie algo—: eso se comprueba en `validar()`, en el paso 3 del §3,
        porque una transición mal formada se puede construir para probar que `aplicar` la
        rechaza, y el rechazo tiene que venir del ejecutor, que es quien responde del
        estado canónico.
        """
        comprobar_identificador(self.id, "identificador de transacción")
        if not isinstance(self.tipo, str) or not self.tipo.strip():
            raise TransicionInvalida("una transición sin `tipo` no es clasificable")
        if self.base is not None and (
            not isinstance(self.base, str) or not self.base.startswith("sha256:")
        ):
            raise TransicionInvalida(
                "`base` es el `revision_id` esperado (`sha256:...`) o `None`", ruta=self.base
            )
        vistas = set()
        for operacion in self.operaciones:
            if not isinstance(operacion, (Escritura, Borrado)):
                raise TransicionInvalida(
                    "una operación es `Escritura` o `Borrado`; se recibió "
                    + type(operacion).__name__
                )
            comprobar_ruta_logica(operacion.ruta)
            if operacion.ruta in vistas:
                # Dos operaciones sobre la misma ruta harían que el resultado dependiese del
                # ORDEN de la lista, y entonces `cid_raiz` dejaría de ser función del
                # contenido. El §3 exige un plan sin ambigüedad.
                raise TransicionInvalida(
                    "la misma ruta aparece dos veces en la transición", ruta=operacion.ruta
                )
            vistas.add(operacion.ruta)
            if isinstance(operacion, Escritura):
                if not isinstance(operacion.contenido, dict):
                    raise TransicionInvalida(
                        "el contenido de una `Escritura` es un mapa JSON", ruta=operacion.ruta
                    )
                operacion.normalizada()   # valida el `esquema` declarado, si lo trae
        return self

    def validar(self, *, exige_cambio=True):
        """Validación COMPLETA, la del paso 3 del §3. La ejecuta `aplicar` antes de abrir.

        Añade a la forma las dos condiciones que hacen que la transición merezca una
        revisión:

          · CAMBIA ALGO. Una transición con la lista de operaciones vacía «tendría éxito»
            publicando una revisión nueva cuyo `cid_raiz` es idéntico al anterior: un
            eslabón en el linaje que no explica ningún cambio, y cuatro eventos en el
            diario que no cuentan nada. `g.13` pide lo contrario —que todo cambio sea
            explicable por el diario—, y un diario lleno de eventos sin contenido es la
            forma más barata de hacer ilegible una historia sin borrar una sola línea.

          · TIENE AUTOR Y MOTIVO. Sin ellos el evento del diario existe pero no es
            auditable: se sabe qué cambió y no se sabe quién lo decidió ni por qué, que es
            justo la mitad que `g.13` necesita.
        """
        self.validar_forma()
        # `exige_cambio=False` lo pasa el motor para las transacciones cuyo cambio durable
        # NO está en `canonico/` sino en un anexo que la propia transacción escribe: una
        # resolución de reconciliación puede no tocar ningún objeto y sigue cambiando algo
        # —retira una pendencia— y sigue siendo auditable. La excepción es del ejecutor,
        # que sabe qué anexos lleva; no del llamador, que podría abusar de ella.
        if exige_cambio and not self.operaciones:
            raise TransicionInvalida(
                "una transición sin operaciones no cambia nada: publicaría una revisión "
                "que no explica ningún cambio y ensuciaría el linaje sin aportar historia",
                ruta=self.id,
            )
        for nombre, valor in (("autor", self.autor), ("motivo", self.motivo)):
            if not isinstance(valor, str) or not valor.strip():
                raise TransicionInvalida(
                    "una transición sin `" + nombre + "` no es auditable, y `g.13` exige "
                    "que todo cambio del estado canónico sea explicable",
                    ruta=self.id,
                )
        return self

    def operaciones_a_dict(self):
        """El plan, en la forma exacta que viaja al diario (§2.4)."""
        return [operacion.a_dict() for operacion in self.operaciones]

    def escrituras(self):
        return [op for op in self.operaciones if isinstance(op, Escritura)]

    def borrados(self):
        return [op for op in self.operaciones if isinstance(op, Borrado)]

    def a_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "base": self.base,
            "autor": self.autor,
            "motivo": self.motivo,
            "operaciones": self.operaciones_a_dict(),
        }


# ------------------------------------------------------------------- proyección
def proyectar_raiz(raiz_base, operaciones):
    """Aplica el plan al mapa `raiz` y devuelve el mapa resultante. NO toca el disco.

    Es una función pura, y eso es lo que permite calcular `resultado` ANTES de escribir:
    la recuperación puede recalcularlo después del corte y comparar contra lo anotado en el
    diario, sin depender de haber presenciado nada.
    """
    proyectada = dict(raiz_base)
    for operacion in operaciones:
        if operacion["accion"] == ACCION_ESCRIBIR:
            proyectada[operacion["ruta"]] = operacion["cid"]
        elif operacion["accion"] == ACCION_BORRAR:
            proyectada.pop(operacion["ruta"], None)
        else:
            raise TransicionInvalida(
                "acción desconocida en el plan: " + repr(operacion["accion"]),
                ruta=operacion.get("ruta"),
            )
    return proyectada


def identificador_derivado(prefijo_revision, semilla):
    """`tx-<revision:04d>-<cid8>` para las transacciones que genera el propio motor (§2.3).

    Deriva del CONTENIDO de la semilla, nunca de `uuid`, del pid ni del reloj: `I-g3`. Dos
    inicializaciones de dos almacenes vacíos producen el mismo identificador, y eso es
    deseable —el mismo estado da los mismos bytes— y no una colisión, porque el
    identificador sólo tiene que ser único DENTRO de un almacén.
    """
    return "tx-" + str(prefijo_revision).zfill(4) + "-" + cid_corto(cid_de_objeto(semilla))


def componer_revision(revision, padre, raiz, transaccion, diario_secuencia):
    """El contenido exacto de `REVISION.json` (§2.3), reproducible a partir de sus partes."""
    cid_raiz = calcular_cid_raiz(raiz)
    return {
        "esquema": "ads.estado/1",
        "revision": revision,
        "revision_id": calcular_revision_id(revision, padre, cid_raiz, transaccion),
        "padre": padre,
        "cid_raiz": cid_raiz,
        "raiz": dict(raiz),
        "diario_secuencia": diario_secuencia,
        "transaccion": transaccion,
    }


# --------------------------------------------------------------------- informes
@dataclass
class ResultadoTransicion:
    transaccion: str
    revision: int
    revision_id: str
    padre: Optional[str]
    cid_raiz: str
    diario_secuencia: int
    operaciones: List[Dict[str, Any]] = field(default_factory=list)
    repetida: bool = False

    def a_dict(self):
        return {
            "transaccion": self.transaccion,
            "revision": self.revision,
            "revision_id": self.revision_id,
            "padre": self.padre,
            "cid_raiz": self.cid_raiz,
            "diario_secuencia": self.diario_secuencia,
            "operaciones": list(self.operaciones),
            "repetida": self.repetida,
        }


@dataclass
class InformeRecuperacion:
    rama: str                       # ninguna | completar | revertir | marcar
    ventana_previa: str             # abierta | preparada | cerrada
    transaccion: Optional[str] = None
    acciones: List[str] = field(default_factory=list)
    eventos_anexados: List[str] = field(default_factory=list)
    revision_id: Optional[str] = None
    conflicto: Optional[str] = None
    marcadas: List[str] = field(default_factory=list)
    cola_del_diario_descartada: int = 0

    def a_dict(self):
        return {
            "rama": self.rama,
            "ventana_previa": self.ventana_previa,
            "transaccion": self.transaccion,
            "acciones": list(self.acciones),
            "eventos_anexados": list(self.eventos_anexados),
            "revision_id": self.revision_id,
            "conflicto": self.conflicto,
            "marcadas": list(self.marcadas),
            "cola_del_diario_descartada": self.cola_del_diario_descartada,
        }


@dataclass
class InformeIntegridad:
    ok: bool
    revision: int
    revision_id: str
    cid_raiz: str
    objetos_verificados: int
    eventos_del_diario: int
    lineas_del_registro: int
    reconciliaciones_pendientes: int
    ventana: str
    hallazgos: List[Dict[str, Any]] = field(default_factory=list)

    def a_dict(self):
        return {
            "ok": self.ok,
            "revision": self.revision,
            "revision_id": self.revision_id,
            "cid_raiz": self.cid_raiz,
            "objetos_verificados": self.objetos_verificados,
            "eventos_del_diario": self.eventos_del_diario,
            "lineas_del_registro": self.lineas_del_registro,
            "reconciliaciones_pendientes": self.reconciliaciones_pendientes,
            "ventana": self.ventana,
            "hallazgos": list(self.hallazgos),
        }


@dataclass
class InformeAuditoria:
    ok: bool
    revision: int
    revision_id: str
    cid_raiz: str
    cid_raiz_reproducido: str
    transacciones_confirmadas: int
    eventos: int
    resoluciones_casadas: int
    hallazgos: List[Dict[str, Any]] = field(default_factory=list)

    def a_dict(self):
        return {
            "ok": self.ok,
            "revision": self.revision,
            "revision_id": self.revision_id,
            "cid_raiz": self.cid_raiz,
            "cid_raiz_reproducido": self.cid_raiz_reproducido,
            "transacciones_confirmadas": self.transacciones_confirmadas,
            "eventos": self.eventos,
            "resoluciones_casadas": self.resoluciones_casadas,
            "hallazgos": list(self.hallazgos),
        }


@dataclass
class InformeMigracion:
    ok: bool
    desde: int
    hasta: int
    aplicadas: List[Dict[str, Any]] = field(default_factory=list)
    transacciones: List[str] = field(default_factory=list)

    def a_dict(self):
        return {
            "ok": self.ok,
            "desde": self.desde,
            "hasta": self.hasta,
            "aplicadas": list(self.aplicadas),
            "transacciones": list(self.transacciones),
        }
