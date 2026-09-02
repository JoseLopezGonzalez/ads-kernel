#!/usr/bin/env python3
"""ejecucion — la FRONTERA con los adaptadores, y sólo la frontera.

El §7.6 de `11-ARQ` es literal: «el runtime no conoce ninguna marca». Este módulo declara
el contrato mínimo del §4.4 —lo que el runtime EXIGE de un adaptador— y nada más. La
implementación productiva la entrega el corte `V7` en `adaptadores/`, y el runtime la
acepta POR INYECCIÓN: `Runtime(..., registro_de_adaptadores=<el de B>)`.

    class RegistroDeAdaptadores:
        def seleccionar(self, capacidades_requeridas) -> Adaptador
    class Adaptador:
        identificador: str
        version_de_contrato: int          # el runtime exige == VERSION_DE_CONTRATO
        capacidades: list[str]
        def ejecutar(self, orden, *, efecto, limite_segundos, progreso=None,
                     cancelacion=None) -> dict

DECISIÓN · las bases levantan `NotImplementedError`, y es la única excepción del §0
    La regla dura prohíbe `pass`, `TODO` y `NotImplementedError` «salvo en la interfaz base
    que declara el fallo cerrado, y ahí se documenta». Esto es esa interfaz. Un método base
    que devolviera un resultado vacío haría que un adaptador incompleto pareciese
    funcionar: el runtime escribiría un `completado` durable por una ejecución que nunca
    ocurrió.

DECISIÓN · la compatibilidad se comprueba al SELECCIONAR, no al registrar
    Alternativas: (a) rechazar el adaptador incompatible al darlo de alta; (b) al elegirlo.
    Se elige (b) y se hace también en (a) cuando el registro es de este módulo. La razón es
    que el registro real lo construye B y el runtime no controla su alta: si la única
    comprobación viviera en el alta, un registro ajeno podría entregar un adaptador de otra
    versión de contrato y el runtime lo ejecutaría. La comprobación en la selección es la
    que el runtime SÍ puede garantizar.

DECISIÓN · `RegistroEnPruebas` vive aquí y está marcado como tal
    El §4.4 lo pide explícitamente para que A no se bloquee esperando a B. Lleva
    `EN_PRUEBAS = True`, su docstring lo dice en la primera línea y `Runtime` no lo
    construye nunca por su cuenta: hay que pasarlo. Nada del camino productivo lo importa.
"""
from __future__ import annotations

import json
import os

from .errores import (
    AdaptadorIncompatible,
    CapacidadNoSoportada,
    EfectoYaAplicado,
    RuntimeInconsistente,
)

VERSION_DE_CONTRATO = 1


# ============================================================================
#  el contrato mínimo del §4.4
# ============================================================================
class Adaptador:
    """Interfaz BASE de un adaptador. Declara el fallo cerrado; no ejecuta nada."""

    identificador = ""
    version_de_contrato = VERSION_DE_CONTRATO
    capacidades = ()

    def ejecutar(self, orden, *, efecto, limite_segundos, progreso=None, cancelacion=None):
        """Ejecuta la orden y devuelve el resultado del §4.4.

        `progreso` es un invocable `progreso(dict)`; `cancelacion` un objeto con
        `.activada()`. La base NO ejecuta: un adaptador que herede y no implemente esto
        tiene que fallar de forma ruidosa, porque la alternativa —devolver un resultado
        vacío— haría que el runtime publicase un `completado` durable de una ejecución
        que nunca ocurrió.
        """
        raise NotImplementedError(
            "un adaptador concreto implementa `ejecutar`; la base declara el fallo cerrado"
        )


class RegistroDeAdaptadores:
    """Interfaz BASE del registro. La implementación real la entrega el corte `V7`."""

    def seleccionar(self, capacidades_requeridas):
        """Devuelve el adaptador que declara TODAS las capacidades pedidas."""
        raise NotImplementedError(
            "el registro concreto implementa `seleccionar`; la base declara el fallo cerrado"
        )


def comprobar_adaptador(adaptador, capacidades_requeridas):
    """La guarda que el runtime aplica a TODO adaptador, venga del registro que venga."""
    if adaptador is None:
        raise CapacidadNoSoportada(
            "el registro no devolvió adaptador para " + ", ".join(capacidades_requeridas),
        )
    version = getattr(adaptador, "version_de_contrato", None)
    if version != VERSION_DE_CONTRATO:
        raise AdaptadorIncompatible(
            "el adaptador `" + str(getattr(adaptador, "identificador", "?"))
            + "` declara la versión de contrato " + str(version) + " y el runtime exige la "
            + str(VERSION_DE_CONTRATO),
            declarada=version, exigida=VERSION_DE_CONTRATO,
        )
    declaradas = list(getattr(adaptador, "capacidades", ()) or ())
    faltan = [c for c in capacidades_requeridas if c not in declaradas]
    if faltan:
        raise CapacidadNoSoportada(
            "el adaptador `" + str(adaptador.identificador) + "` no declara "
            + ", ".join(faltan),
            faltan=sorted(faltan),
        )
    if not callable(getattr(adaptador, "ejecutar", None)):
        raise AdaptadorIncompatible(
            "el adaptador `" + str(getattr(adaptador, "identificador", "?"))
            + "` no expone `ejecutar`",
        )
    return adaptador


# ============================================================================
#  SÓLO PRUEBAS — registro mínimo del §4.4, mientras B no entrega el real
# ============================================================================
class RegistroEnPruebas(RegistroDeAdaptadores):
    """SÓLO PRUEBAS. Registro mínimo del §4.4 para no bloquear a A esperando a B.

    Selecciona por capacidad DECLARADA, exactamente como exige el §4.4, y aplica las mismas
    guardas que el runtime aplicaría a un registro ajeno.
    """

    EN_PRUEBAS = True

    def __init__(self, adaptadores=()):
        self._adaptadores = []
        for adaptador in adaptadores:
            self.registrar(adaptador)

    def registrar(self, adaptador):
        if getattr(adaptador, "version_de_contrato", None) != VERSION_DE_CONTRATO:
            raise AdaptadorIncompatible(
                "no se registra un adaptador de otra versión de contrato: "
                + str(getattr(adaptador, "version_de_contrato", None)),
            )
        self._adaptadores.append(adaptador)
        return self

    def identificadores(self):
        return sorted(a.identificador for a in self._adaptadores)

    def seleccionar(self, capacidades_requeridas):
        pedidas = list(capacidades_requeridas)
        if not pedidas:
            raise CapacidadNoSoportada(
                "un paquete sin `capacidades_requeridas` no puede seleccionar adaptador: "
                "elegir «el primero» sería inventar la decisión",
            )
        candidatos = [
            a for a in self._adaptadores
            if all(c in list(a.capacidades) for c in pedidas)
        ]
        if not candidatos:
            raise CapacidadNoSoportada(
                "ningún adaptador registrado declara " + ", ".join(sorted(pedidas))
                + "; registrados: "
                + (", ".join(self.identificadores()) or "(ninguno)"),
                requeridas=sorted(pedidas),
            )
        # Orden estable por identificador: dos instancias deben elegir el MISMO adaptador
        # para la misma capacidad, o el efecto derivado dejaría de ser reproducible.
        candidatos.sort(key=lambda a: a.identificador)
        return comprobar_adaptador(candidatos[0], pedidas)


class AdaptadorEnPruebas(Adaptador):
    """SÓLO PRUEBAS. Adaptador con RECIBO DURABLE por efecto y contador de ejecuciones.

    Es lo mínimo que hace falta para que las pruebas de A puedan afirmar algo que importa:
    que un efecto CONFIRMADO no se aplica dos veces. Su «efecto» es una línea anexada a
    `ejecuciones.log` —un cambio real, observable y NO idempotente por sí mismo—, y su
    recibo es `recibos/<efecto>.json`, escrito y sincronizado tras el efecto. Una segunda
    llamada con el mismo `efecto` devuelve `repetido: true` SIN volver a anexar.

    El comportamiento lo dicta el primer argumento de la orden, para que una prueba pueda
    pedir un fallo reintentable, uno definitivo, una cancelación o un exceso de tiempo sin
    parchear nada:

        argumentos: ["exito"] · ["fallo-reintentable"] · ["fallo-definitivo"]
                    ["cancelacion"] · ["timeout"] · ["exito", "<texto de salida>"]
    """

    EN_PRUEBAS = True

    version_de_contrato = VERSION_DE_CONTRATO

    COMPORTAMIENTOS = ("exito", "fallo-reintentable", "fallo-definitivo", "cancelacion",
                       "timeout")

    def __init__(self, espacio, *, identificador="adaptador-en-pruebas",
                 capacidades=("proceso-local",)):
        self.identificador = identificador
        self.capacidades = list(capacidades)
        self.espacio = espacio
        self.recibos = os.path.join(espacio, "recibos")
        self.bitacora = os.path.join(espacio, "ejecuciones.log")
        # Dos bitácoras, y las dos hacen falta para poder afirmar cosas distintas:
        #   `invocaciones.log`  toda LLAMADA, incluida la que el recibo va a cortar. Es lo
        #                       que distingue «se despachó una vez» de «se despachó dos y
        #                       la segunda no hizo nada».
        #   `ejecuciones.log`   sólo el EFECTO real. Es lo que distingue «no se aplicó dos
        #                       veces» de «se aplicó dos veces y nadie lo vio».
        # Con una sola no se puede probar la idempotencia: la ausencia de duplicados sería
        # indistinguible de la ausencia de segundo intento.
        self.invocaciones_log = os.path.join(espacio, "invocaciones.log")

    # ------------------------------------------------------------- recibo durable
    def _ruta_recibo(self, efecto):
        return os.path.join(self.recibos, efecto + ".json")

    def recibo(self, efecto):
        ruta = self._ruta_recibo(efecto)
        if not os.path.exists(ruta):
            return None
        with open(ruta, "r", encoding="utf-8") as fichero:
            return json.loads(fichero.read())

    def _guardar_recibo(self, efecto, resultado):
        os.makedirs(self.recibos, exist_ok=True)
        ruta = self._ruta_recibo(efecto)
        temporal = ruta + ".tmp"
        with open(temporal, "w", encoding="utf-8") as fichero:
            fichero.write(json.dumps(resultado, sort_keys=True, ensure_ascii=False,
                                     indent=2) + "\n")
            fichero.flush()
            os.fsync(fichero.fileno())
        os.replace(temporal, ruta)
        descriptor = os.open(self.recibos, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)

    def _lineas(self, ruta):
        if not os.path.exists(ruta):
            return []
        with open(ruta, "r", encoding="utf-8") as fichero:
            return [linea for linea in fichero.read().splitlines() if linea]

    def ejecuciones(self):
        """Los EFECTOS reales aplicados. Es lo que una prueba de idempotencia cuenta."""
        return self._lineas(self.bitacora)

    def invocaciones(self):
        """Todas las LLAMADAS a `ejecutar`, incluidas las que el recibo cortó."""
        return self._lineas(self.invocaciones_log)

    # ------------------------------------------------------------------ ejecución
    def ejecutar(self, orden, *, efecto, limite_segundos, progreso=None, cancelacion=None):
        os.makedirs(self.espacio, exist_ok=True)
        with open(self.invocaciones_log, "a", encoding="utf-8") as fichero:
            fichero.write(efecto + "\n")
            fichero.flush()
            os.fsync(fichero.fileno())
        previo = self.recibo(efecto)
        if previo is not None:
            # Idempotencia del ADAPTADOR: el efecto ya se aplicó, y volver a aplicarlo
            # duplicaría la línea. Se devuelve lo mismo, marcado como repetido.
            repetido = dict(previo)
            repetido["repetido"] = True
            return repetido

        argumentos = list(orden.get("argumentos") or [])
        comportamiento = argumentos[0] if argumentos else "exito"
        if comportamiento not in self.COMPORTAMIENTOS:
            raise RuntimeInconsistente(
                "el adaptador en pruebas no conoce el comportamiento "
                + repr(comportamiento) + "; declarados: " + ", ".join(self.COMPORTAMIENTOS),
            )
        if cancelacion is not None and cancelacion.activada():
            return {"estado": "cancelado", "codigo": 130, "salida": "",
                    "detalle": "cancelado antes de empezar", "reintentable": False,
                    "efecto": efecto, "repetido": False}
        if progreso is not None:
            progreso({"fase": "adaptador", "operacion": orden.get("operacion", "")})

        # EL EFECTO. Una línea anexada, sincronizada: si el proceso muere justo después,
        # la línea ya está y contarla dos veces sería el defecto que se quiere impedir.
        os.makedirs(self.espacio, exist_ok=True)
        with open(self.bitacora, "a", encoding="utf-8") as fichero:
            fichero.write(efecto + " " + comportamiento + "\n")
            fichero.flush()
            os.fsync(fichero.fileno())

        resultado = self._resultado_de(comportamiento, efecto, argumentos)
        self._guardar_recibo(efecto, resultado)
        return dict(resultado)

    def _resultado_de(self, comportamiento, efecto, argumentos):
        salida = argumentos[1] if len(argumentos) > 1 else ""
        if comportamiento == "exito":
            return {"estado": "completado", "codigo": 0, "salida": salida,
                    "detalle": "", "reintentable": False, "efecto": efecto,
                    "repetido": False}
        if comportamiento == "fallo-reintentable":
            return {"estado": "fallido", "codigo": 1, "salida": salida,
                    "detalle": "fallo transitorio simulado", "reintentable": True,
                    "efecto": efecto, "repetido": False}
        if comportamiento == "fallo-definitivo":
            return {"estado": "fallido", "codigo": 2, "salida": salida,
                    "detalle": "fallo definitivo simulado", "reintentable": False,
                    "efecto": efecto, "repetido": False}
        if comportamiento == "cancelacion":
            return {"estado": "cancelado", "codigo": 130, "salida": salida,
                    "detalle": "cancelacion simulada", "reintentable": False,
                    "efecto": efecto, "repetido": False}
        return {"estado": "timeout", "codigo": 124, "salida": salida,
                "detalle": "limite excedido simulado", "reintentable": True,
                "efecto": efecto, "repetido": False}


def exigir_efecto_no_aplicado(acuse, efecto):
    """Levanta la SEÑAL `EfectoYaAplicado` si el acuse durable ya declara el efecto.

    El dispatcher NO usa esta función en su camino normal: comprueba el acuse y reutiliza
    el resultado sin excepción alguna, porque un camino normal expresado con excepciones
    acaba capturándose de forma laxa. Existe para quien quiera EXIGIR la ausencia del
    acuse —una orden explícita de «ejecuta esto», una prueba— y quiera el fallo tipado.
    """
    if acuse is not None:
        raise EfectoYaAplicado(
            "hay acuse durable del efecto `" + efecto + "`: ya se aplicó y no se repite",
            ruta=efecto, paquete=acuse.get("paquete"), intento=acuse.get("intento"),
        )
    return None
