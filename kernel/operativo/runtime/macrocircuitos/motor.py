#!/usr/bin/env python3
"""motor — UN SOLO ejecutor de macrocircuito, PARAMETRIZADO por su definición.

    «compartir motor NO aplana las rutas: cada uno conserva su disparador, sus
     precondiciones, sus gates, su rollback, su reanudación y su cierre»     `CI-5`, `§18`

Los cuatro macrocircuitos son COMPOSICIONES DEL MISMO MOTOR, no cuatro runtimes paralelos.
Este módulo es ese motor: una clase, `Macrocircuito`, que recibe su definición de `§18` por
el constructor y no tiene una sola rama `if identificador == "N"`. Lo que cambia entre los
cuatro es el DATO; lo que ejecuta es el mismo código, entra por el mismo punto de despacho
—`ciclo.despacho.despachar`— y escribe por el mismo motor de estado.

DECISIÓN · la materia de cada fase se DERIVA invirtiendo la correspondencia de `b.16`
    `§18` fija el PROCESO de cada tramo; `ciclo.procesos` compone rutas a partir de una
    MATERIA declarada. La correspondencia materia → proceso es una biyección, así que la
    inversa existe y se calcula: no se escribe una segunda tabla que pudiera discrepar de
    la primera. Un proceso que dejara de tener materia única rompería la inversión, y eso
    lo detecta `procesos.exigir_coherente()` antes de que llegue aquí.

DECISIÓN · la AUTORIDAD sobre el producto es un objeto DURABLE y se toma por CAS
    Alternativas: (a) un fichero de bloqueo en el plano operacional; (b) una entrada en el
    estado canónico, tomada con comparación e intercambio.
    Se elige (b). El plano operacional es, por `g.1`, reconstruible y **fabricable por
    cualquiera** —es el ataque que le costó la vía rápida al lease—, así que un bloqueo ahí
    no prueba nada. Con (b), dos PROCESOS REALES que arranquen a la vez sobre el mismo
    producto compiten por una escritura CAS del motor y exactamente uno la consigue: el
    otro recibe `AutoridadIncompatible` y no muta nada. `test_macrocircuitos.py` lo corre
    con dos procesos de verdad, no con dos objetos en el mismo intérprete.

DECISIÓN · dos macrocircuitos DISTINTOS sobre el mismo producto son SIEMPRE incompatibles
    Alternativas: (a) una matriz de compatibilidad por pares; (b) exclusión total entre
    identificadores distintos, y entre ejecuciones distintas del mismo.
    Se elige (b). Los cuatro operan sobre el producto ENTERO —instalarlo, adoptarlo,
    migrarlo, actualizarlo—, y `§8.4` ya declara el caso extremo por su nombre: `U`
    bloquea, «ninguna otra actualización arranca». Una matriz de pares invitaría a razonar
    caso por caso sobre solapamientos que nadie ha decidido, y decidirlos no es de F6.
    Reentrar con el MISMO identificador y la MISMA ejecución sí se admite: eso no es un
    segundo macrocircuito, es `Continúa`.

DECISIÓN · la terminación es INEQUÍVOCA y se escribe
    Cuatro salidas y ninguna más: `completado`, `bloqueado`, `pausado`, `escalado`. Se
    escriben en `canonico/macrocircuitos/<id>.json`, de modo que «cómo terminó» se lee del
    estado y no se deduce de la ausencia de trabajo. Un macrocircuito que terminara sin
    dejar constancia sería indistinguible de uno interrumpido.
"""
from __future__ import annotations

import runtime as paquete_runtime
from ciclo import continuacion, despacho, durable, equipos, gates, handoffs, planificacion
from ciclo.corpus import Corpus
from ciclo.encuadre import encuadrar
from ciclo.procesos import CORRESPONDENCIA
from ciclo.rutas import (
    VIA_CONDICIONAL,
    VIA_ITEM_PROPIO,
    componer,
)
from estado.serializacion import cid_de_objeto

from . import definicion, fase0
from .errores import (
    AutoridadIncompatible,
    MacrocircuitoInconsistente,
)

DOMINIO = "macrocircuitos"
DOMINIO_AUTORIDAD = "autoridad"
ESQUEMA = "ads.estado/1"

COMPLETADO = "completado"
BLOQUEADO = "bloqueado"
PAUSADO = "pausado"
ESCALADO = "escalado"
TERMINACIONES = (COMPLETADO, BLOQUEADO, PAUSADO, ESCALADO)

# El estado del objeto sobre el que trabaja cada macrocircuito. `N` instala lo que todavía
# no existe; los otros tres operan sobre algo que ya está.
ESTADO_DEL_OBJETO = {"N": "no-existe", "A": "existe", "M": "existe", "U": "existe"}


def materia_de(proceso):
    """La materia que corresponde a un proceso, INVIRTIENDO la correspondencia de `b.16`."""
    candidatas = [m for m, fila in CORRESPONDENCIA.items() if fila["proceso"] == proceso]
    if len(candidatas) != 1:
        raise MacrocircuitoInconsistente(
            "la correspondencia materia → proceso no es invertible para `" + str(proceso)
            + "`: hay " + str(len(candidatas)) + " materias que lo nombran",
            proceso=str(proceso),
        )
    return candidatas[0]


def _clave_de_producto(producto):
    """Un segmento válido para el estado canónico, derivado del nombre del producto."""
    return "pr-" + cid_de_objeto({"producto": str(producto)}).split(":", 1)[-1][:16]


class Macrocircuito:
    """El ejecutor ÚNICO, parametrizado por la definición de `§18`. Sin ramas por circuito."""

    def __init__(self, identificador, ruta_control_repo, *, corpus=None,
                 instancia="macrocircuito", registro_de_adaptadores=None,
                 raiz_kernel=None):
        self.definicion = definicion.macrocircuito(identificador)
        self.id = self.definicion["id"]
        self.ruta = ruta_control_repo
        self.corpus = corpus or Corpus()
        self.instancia = instancia
        self.registro = registro_de_adaptadores
        self.raiz_kernel = raiz_kernel
        self.runtime = None
        self.fase0 = None
        self.autoridad = None

    # =====================================================================
    #  FASE 0 · el MISMO contrato, invocado por los cuatro
    # =====================================================================
    def ejecutar_fase0(self, *, disparador=None, comprobaciones_superadas=(),
                       evidencia=(), bloqueo_de_seg=None, sujeto_anterior=None,
                       productor=fase0.PRODUCTOR, dosier_de=fase0.VERIFICADOR):
        """La `FASE 0`. CERO mutaciones canónicas: `estado/` no existe todavía."""
        self.fase0 = fase0.ejecutar(
            self.ruta,
            macrocircuito=self.id,
            disparador=disparador or self.definicion["disparador"],
            corpus=self.corpus,
            comprobaciones_superadas=comprobaciones_superadas,
            evidencia=evidencia,
            bloqueo_de_seg=bloqueo_de_seg,
            productor=productor,
            dosier_de=dosier_de,
            raiz_kernel=self.raiz_kernel,
            sujeto_anterior=sujeto_anterior,
        )
        fase0.exigir_soporte_fuera_de_estado(self.ruta, self.fase0["sujeto"])
        fase0.exigir_una_sola(self.ruta, self.id)
        return self.fase0

    # =====================================================================
    #  apertura · la PRIMERA fase que crea `estado/` incorpora la declaración
    # =====================================================================
    def abrir(self):
        """Crea `estado/`, toma AUTORIDAD e INCORPORA la declaración. En ese orden."""
        mutacion = "crear `estado/` y abrir iniciativa"
        if self.fase0 is None:
            # `X-S1`: sin `FASE 0` no hay primera mutación, y se nombra cuál se intentaba.
            fase0.exigir_fase0_antes_de_mutar(
                self.ruta, macrocircuito=self.id, mutacion=mutacion,
            )
        # `X-S5`: si el gate no está superado, se BLOQUEA ANTES de mutar. Abrir la
        # iniciativa YA es estado, y ésa es la frontera exacta.
        fase0.exigir_gate_superado(self.fase0, macrocircuito=self.id, mutacion=mutacion)
        fase0.exigir_declaracion_propia(self.fase0["declaracion"], self.fase0["sujeto"])
        self.runtime = paquete_runtime.Runtime(
            self.ruta, instancia=self.instancia,
            registro_de_adaptadores=self.registro,
        ).abrir()
        self._tomar_autoridad()
        fase0.incorporar(self.runtime, self.fase0, macrocircuito=self.id)
        fase0.exigir_incorporada(self.runtime, self.fase0)
        self._escribir_estado(abierto=True, terminacion=None,
                              motivo="apertura de " + self.id)
        return self

    def cerrar(self):
        if self.runtime is not None:
            self.runtime.cerrar()
            self.runtime = None

    def __enter__(self):
        return self

    def __exit__(self, tipo, valor, traza):
        self.cerrar()
        return False

    # ------------------------------------------------------------ autoridad
    def _tomar_autoridad(self):
        producto = self.fase0["sujeto"]["producto_o_instalacion"]
        ejecucion = self.fase0["sujeto"]["ejecucion_del_macrocircuito"]
        clave = _clave_de_producto(producto)
        ruta = DOMINIO_AUTORIDAD + "/" + clave + ".json"
        pretendida = {
            "esquema": ESQUEMA,
            "id": clave,
            "producto": producto,
            "macrocircuito": self.id,
            "ejecucion": ejecucion,
            "bloqueo": self.definicion.get("bloqueo") or
                       "los cuatro operan sobre el producto entero: dos a la vez es "
                       "autoridad incompatible",
        }

        def guarda(revision):
            vigente = durable.leer(self.runtime.almacen, ruta)
            if vigente is None:
                return
            if (vigente["macrocircuito"], vigente["ejecucion"]) != (self.id, ejecucion):
                raise AutoridadIncompatible(
                    "el producto ya está bajo la autoridad de `" + str(vigente["macrocircuito"])
                    + "` (ejecución `" + str(vigente["ejecucion"]) + "`) y `" + self.id
                    + "` (ejecución `" + ejecucion + "`) pretende la suya; dos "
                    "macrocircuitos sobre el mismo producto NO pueden adquirir autoridad "
                    "incompatible",
                    vigente=str(vigente["macrocircuito"]), pretendida=self.id,
                    producto=producto,
                )

        durable.escribir(
            self.runtime.almacen, clase="macrocircuito.autoridad.adquirida",
            motivo="autoridad de " + self.id + " sobre " + producto,
            objetos={ruta: pretendida}, autor=self.id, semilla={"autoridad": clave},
            guarda=guarda,
        )
        # Se RELEE del estado: quien ganó la carrera es lo que el estado dice, no lo que
        # este proceso creyó al construir. Con dos procesos reales, el perdedor ve aquí al
        # ganador aunque su propia escritura no levantara la guarda.
        vigente = durable.leer(self.runtime.almacen, ruta)
        if vigente is None or (vigente["macrocircuito"], vigente["ejecucion"]) != (
            self.id, ejecucion
        ):
            raise AutoridadIncompatible(
                "otra ejecución tomó la autoridad sobre `" + producto + "` en la misma "
                "carrera: la tiene `" + str((vigente or {}).get("macrocircuito"))
                + "` y no `" + self.id + "`",
                vigente=str((vigente or {}).get("macrocircuito")), pretendida=self.id,
                producto=producto,
            )
        self.autoridad = vigente
        return vigente

    # =====================================================================
    #  una FASE cualquiera, con el MISMO código para los cuatro
    # =====================================================================
    def componer_fase(self, nombre_de_fase, *, propietario_declarado=None,
                      condiciones_extra=(), item_lider=None):
        """La ruta de la fase, compuesta por `ciclo.rutas` desde `b.16`. Sin ramas propias."""
        una = definicion.fase(self.id, nombre_de_fase)
        materia = materia_de(una["proceso"])
        marco = encuadrar(self.ruta, {
            "clase": "candidato",
            "expresion_literal": self.definicion["disparador"],
            "canal": "macrocircuito:" + self.id,
            "resultado_perseguido": una["salida"],
            "evidencia_de_cierre": [una["gate_declarado"] or una["salida"]],
            "anclaje_terminado": True,
            "materia": materia,
            "estado_del_objeto": ESTADO_DEL_OBJETO[self.id],
        }, corpus=self.corpus)
        condiciones = {
            p["condicion"] for p in una["participantes"]
            if p["via"] == VIA_CONDICIONAL and p.get("condicion")
        }
        condiciones.update(str(c) for c in condiciones_extra)
        enlazados = [
            {"capacidad": p["capacidad"], "proceso": p["proceso"],
             "item_lider": item_lider or (self.id + "-" + nombre_de_fase),
             "salida": una["salida"], "criterio": una["gate_declarado"] or una["salida"]}
            for p in una["participantes"] if p["via"] == VIA_ITEM_PROPIO
        ]
        capacidades = definicion.capacidades_de_la_fase(una)
        ruta = componer(
            marco, corpus=self.corpus, fase=self.id + "/" + nombre_de_fase,
            condiciones_verdaderas=sorted(condiciones),
            items_enlazados=enlazados,
            presencias=una["presencias"],
            propietario_declarado=propietario_declarado,
            capacidades_de_la_fase=capacidades,
        )
        return {"encuadre": marco, "ruta": ruta, "definicion": una}

    def ejecutar_fase(self, nombre_de_fase, *, orden_por_capacidad,
                      propietario_declarado=None, condiciones_extra=(),
                      composiciones_por_capacidad=None, slots=equipos.SLOTS_POR_DEFECTO,
                      despachar=True, maximo=0):
        """Compone, materializa, planifica y despacha. El MISMO camino para los cuatro."""
        if self.runtime is None:
            raise MacrocircuitoInconsistente(
                "la fase se ejecuta con el macrocircuito ABIERTO; `abrir()` crea `estado/`, "
                "toma autoridad e incorpora la declaración, y ese orden no se salta",
            )
        compuesta = self.componer_fase(
            nombre_de_fase, propietario_declarado=propietario_declarado,
            condiciones_extra=condiciones_extra,
        )
        materializados = []
        for capacidad in sorted({p["capacidad"] for p in compuesta["ruta"]["participantes"]}):
            elegidas = (composiciones_por_capacidad or {}).get(capacidad)
            if not elegidas:
                continue
            materializados.append(equipos.materializar(
                capacidad, corpus=self.corpus, composiciones_verdaderas=elegidas,
                slots=slots,
            ))
        planificador = planificacion.Planificador(self.runtime, corpus=self.corpus)
        plan = planificador.planificar(
            compuesta["encuadre"], compuesta["ruta"], equipos=materializados,
            orden_por_capacidad=orden_por_capacidad,
            titulo=self.id + " · " + nombre_de_fase,
        )
        informe = None
        if despachar:
            informe = despacho.barrido(
                self.runtime, maximo=maximo, origen="macrocircuito:" + self.id,
            )
        return {"fase": nombre_de_fase, "ruta": compuesta["ruta"], "plan": plan,
                "equipos": materializados, "despacho": informe}

    # =====================================================================
    #  gates y handoffs de la fase
    # =====================================================================
    def aplicar_gate(self, identificador, *, entrada, evidencia, revisor, autor,
                     comprobaciones_superadas=(), salida=None):
        dictamen = gates.aplicar(
            identificador, corpus=self.corpus, entrada=entrada, evidencia=evidencia,
            revisor=revisor, autor=autor,
            comprobaciones_superadas=comprobaciones_superadas, salida=salida,
        )
        durable.escribir(
            self.runtime.almacen, clase="macrocircuito.gate.dictaminado",
            motivo=identificador + " sobre " + self.id,
            objetos={gates.ruta_de(dictamen["id"]): dictamen},
            autor=self.id, semilla={"dictamen": dictamen["id"]},
        )
        return dictamen

    def emitir_handoff(self, identificador, *, artefactos, checkpoint, trazabilidad):
        entrega = handoffs.emitir(
            identificador, artefactos=artefactos, checkpoint=checkpoint,
            trazabilidad=trazabilidad, corpus=self.corpus,
        )
        self._persistir_entrega(entrega, "emitido")
        return entrega

    def acusar_handoff(self, entrega, *, comprobaciones_superadas, receptor):
        acusada = handoffs.acusar(
            entrega, comprobaciones_superadas=comprobaciones_superadas, receptor=receptor,
        )
        self._persistir_entrega(acusada, "acusado")
        return acusada

    def rechazar_handoff(self, entrega, *, receptor, motivo):
        rechazada = handoffs.rechazar(entrega, receptor=receptor, motivo=motivo)
        self._persistir_entrega(rechazada, "rechazado")
        return rechazada

    def _persistir_entrega(self, entrega, clase):
        durable.escribir(
            self.runtime.almacen, clase="macrocircuito.handoff." + clase,
            motivo=entrega["instancia"] + " " + clase,
            objetos={handoffs.ruta_de(entrega["id"]): entrega},
            autor=entrega["de"], semilla={"entrega": entrega["id"]},
        )
        return entrega

    # =====================================================================
    #  pausa · reanudación · `Continúa` · terminación
    # =====================================================================
    def pausar(self, *, motivo):
        return self._escribir_estado(abierto=True, terminacion=PAUSADO, motivo=motivo)

    def reanudar(self, *, motivo):
        return self._escribir_estado(abierto=True, terminacion=None, motivo=motivo)

    def continuar(self, *, modo=continuacion.MODO_PLAN, frente=1, reparar=False,
                  no_interactivo=True):
        """`Continúa` sobre este macrocircuito. Es el MISMO `Continúa` del ciclo."""
        return continuacion.Continuacion(self.runtime, corpus=self.corpus).plan(
            modo=modo, frente=frente, reparar=reparar, no_interactivo=no_interactivo,
        )

    def terminar(self, terminacion, *, motivo):
        """Termina de forma INEQUÍVOCA. Cuatro salidas, y ninguna más."""
        if terminacion not in TERMINACIONES:
            raise MacrocircuitoInconsistente(
                "terminación fuera del vocabulario cerrado: " + repr(terminacion)
                + "; válidas: " + ", ".join(TERMINACIONES),
            )
        return self._escribir_estado(abierto=False, terminacion=terminacion, motivo=motivo)

    def _escribir_estado(self, *, abierto, terminacion, motivo):
        cuerpo = {
            "esquema": ESQUEMA,
            "id": self.id,
            "nombre": self.definicion["nombre"],
            "disparador": self.definicion["disparador"],
            "ejecucion": self.fase0["sujeto"]["ejecucion_del_macrocircuito"],
            "declaracion": self.fase0["declaracion"]["id"],
            "huella_del_sujeto": self.fase0["declaracion"]["huella_del_sujeto"],
            "fases": [f["fase"] for f in self.definicion["fases"]],
            "secuencia_de_procesos": list(definicion.secuencia_de_procesos(self.id)),
            "abierto": bool(abierto),
            "terminacion": terminacion,
            "motivo": str(motivo),
        }
        durable.escribir(
            self.runtime.almacen, clase="macrocircuito.estado",
            motivo=motivo,
            objetos={DOMINIO + "/" + self.id + ".json": cuerpo},
            autor=self.id, semilla={"macrocircuito": self.id, "terminacion": terminacion,
                                    "abierto": abierto, "motivo": str(motivo)},
        )
        return cuerpo

    def estado(self):
        """Cómo terminó, LEÍDO del estado canónico. No se deduce de la ausencia de trabajo."""
        return durable.leer(self.runtime.almacen, DOMINIO + "/" + self.id + ".json")
