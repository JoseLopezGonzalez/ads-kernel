#!/usr/bin/env python3
"""registro — selección de adaptador por CAPACIDAD DECLARADA. Corte `V7`.

Es la implementación real de `RegistroDeAdaptadores` del §4.4 del contrato: el runtime la
recibe por inyección y programa contra ella.

DECISIÓN · se selecciona por CAPACIDAD y no por identificador
    Alternativas: (a) el paquete nombra al adaptador; (b) el paquete declara qué
    CAPACIDADES necesita y el registro elige.
    Se elige (b). Con (a), cambiar de proveedor obliga a reescribir los paquetes ya
    despachados, que es justo lo que §6.6 dice que NO puede pasar: «el estado, la memoria,
    los items y los checkpoints NO SE TOCAN» al cambiar de entorno. Con (b) el paquete
    declara `capacidades_requeridas` y el registro resuelve; el estado canónico no menciona
    a ningún proveedor concreto.

DECISIÓN · la versión de contrato se comprueba al REGISTRAR y al SELECCIONAR
    Comprobarla sólo al registrar dejaría pasar un adaptador cuya versión cambiara después
    por reasignación de atributo. Es barato y cierra el hueco.

DECISIÓN · el desempate entre dos adaptadores capaces es DETERMINISTA
    Si dos adaptadores declaran la misma capacidad, gana el de identificador menor. Un
    desempate por orden de registro haría que el despacho dependiera del orden de importación
    y dos ejecuciones del mismo escenario podrían usar adaptadores distintos.
"""
from __future__ import annotations

from .contrato import (
    VERSION_DE_CONTRATO,
    AdaptadorIncompatible,
    CapacidadNoSoportada,
    OrdenInvalida,
)


class RegistroDeAdaptadores:
    """Selecciona el adaptador que cubre TODAS las capacidades requeridas."""

    def __init__(self, adaptadores=()):
        self._por_identificador = {}
        for adaptador in adaptadores:
            self.registrar(adaptador)

    def registrar(self, adaptador):
        identificador = getattr(adaptador, "identificador", "")
        if not isinstance(identificador, str) or not identificador.strip():
            raise OrdenInvalida("un adaptador sin identificador no se registra")
        self._comprobar_version(adaptador)
        capacidades = getattr(adaptador, "capacidades", None)
        if not capacidades:
            raise OrdenInvalida(
                "el adaptador `" + identificador + "` no declara capacidades; un adaptador "
                "sin capacidad declarada nunca sería seleccionable y su registro sería mudo"
            )
        if identificador in self._por_identificador:
            raise OrdenInvalida(
                "ya hay un adaptador registrado con el identificador `" + identificador
                + "`: dos sedes para el mismo nombre"
            )
        self._por_identificador[identificador] = adaptador
        return adaptador

    @staticmethod
    def _comprobar_version(adaptador):
        version = getattr(adaptador, "version_de_contrato", None)
        if version != VERSION_DE_CONTRATO:
            raise AdaptadorIncompatible(
                "el adaptador `" + str(getattr(adaptador, "identificador", "?"))
                + "` declara la versión de contrato " + str(version) + " y el runtime exige "
                + str(VERSION_DE_CONTRATO),
                declarada=version, exigida=VERSION_DE_CONTRATO,
            )

    def identificadores(self):
        return tuple(sorted(self._por_identificador))

    def capacidades(self):
        """El censo de capacidades ofrecidas, DERIVADO de los adaptadores registrados."""
        salida = {}
        for identificador in sorted(self._por_identificador):
            for capacidad in self._por_identificador[identificador].capacidades:
                salida.setdefault(capacidad, []).append(identificador)
        return {capacidad: sorted(salida[capacidad]) for capacidad in sorted(salida)}

    def seleccionar(self, capacidades_requeridas):
        """El adaptador que cubre TODAS las capacidades. `CapacidadNoSoportada` si ninguno."""
        requeridas = tuple(capacidades_requeridas or ())
        if not requeridas:
            raise CapacidadNoSoportada(
                "un paquete sin capacidades requeridas no se despacha: no hay criterio de "
                "selección y elegir «el primero» sería inventar uno"
            )
        candidatos = []
        for identificador in sorted(self._por_identificador):
            adaptador = self._por_identificador[identificador]
            if all(capacidad in adaptador.capacidades for capacidad in requeridas):
                self._comprobar_version(adaptador)
                candidatos.append(adaptador)
        if not candidatos:
            raise CapacidadNoSoportada(
                "ningún adaptador declara todas las capacidades requeridas: "
                + ", ".join(sorted(requeridas)),
                requeridas=sorted(requeridas),
                ofrecidas=sorted(self.capacidades()),
            )
        return candidatos[0]
