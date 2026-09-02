#!/usr/bin/env python3
"""rotacion — estados, rotación y solapamiento de identidades. Instancia `O25` §5.

`O25` §5 enumera lo que el contrato tiene que permitir, y esto es esa lista ejecutada:

    rotación · periodo de solapamiento EXPLÍCITO · claves activas · retiradas · revocadas ·
    rechazo de claves desconocidas o revocadas · trazabilidad SIN revelación de secretos

DECISIÓN · el solapamiento se mide en ÉPOCAS, no en reloj
    Alternativas: (a) «treinta días»; (b) un número de ÉPOCAS.
    Se elige (b). Un solapamiento en reloj no se puede comprobar de forma determinista —dos
    ejecuciones de la misma prueba dan resultados distintos— y hace que la validez de una
    firma dependa de la hora de la máquina que la verifica, que es la peor propiedad posible
    para una raíz externa. Con épocas, «esta firma es de la época 3 y la identidad se retiró
    en la 4 con solapamiento 2, luego verifica hasta la 6» es una afirmación comprobable y
    reproducible. Es además coherente con `I-g3`, que expulsa el reloj de lo durable.

DECISIÓN · una identidad REVOCADA no verifica NUNCA, ni siquiera dentro del solapamiento
    Retirada y revocada no son grados de lo mismo. Retirada es «ya no firma, pero lo que
    firmó sigue valiendo un rato». Revocada es «lo que firmó no vale»: es lo que se hace
    cuando se cree que la clave se comprometió, y honrar su solapamiento anularía el acto.

DECISIÓN · la traza NO lleva material sensible, y por eso lleva la HUELLA PÚBLICA
    `O25` §2 prohíbe que la clave aparezca en trazas. Cada apunte identifica la identidad por
    su `id` y por su huella PÚBLICA, que es lo que `O25` §3 dice que la configuración externa
    establece. Con eso la trazabilidad de aprovisionamiento y rotación es completa y no hay
    nada que filtrar.
"""
from __future__ import annotations

from .errores import (
    ConfiguracionInvalida,
    IdentidadDesconocida,
    IdentidadFueraDeSolapamiento,
    IdentidadRevocada,
)

ACTIVA = "activa"
RETIRADA = "retirada"
REVOCADA = "revocada"
ESTADOS = (ACTIVA, RETIRADA, REVOCADA)

SOLAPAMIENTO_POR_DEFECTO = 2


class Identidad:
    """Una identidad pública aceptada, con su estado y sus épocas. NUNCA su clave."""

    __slots__ = ("id", "algoritmo", "huella_publica", "estado", "epoca_de_alta",
                 "epoca_de_retirada", "solapamiento", "motivo")

    def __init__(self, *, identificador, algoritmo, huella_publica, estado,
                 epoca_de_alta, epoca_de_retirada=None,
                 solapamiento=SOLAPAMIENTO_POR_DEFECTO, motivo=""):
        if estado not in ESTADOS:
            raise ConfiguracionInvalida(
                "estado de identidad fuera del vocabulario `activa · retirada · revocada`: "
                + str(estado)
            )
        if not isinstance(epoca_de_alta, int) or epoca_de_alta < 1:
            raise ConfiguracionInvalida("la época de alta es un entero mayor que cero")
        if estado in (RETIRADA, REVOCADA) and epoca_de_retirada is None:
            raise ConfiguracionInvalida(
                "una identidad `" + estado + "` declara la época en que dejó de estar "
                "activa; sin ella el solapamiento no se puede medir"
            )
        self.id = identificador
        self.algoritmo = algoritmo
        self.huella_publica = huella_publica
        self.estado = estado
        self.epoca_de_alta = epoca_de_alta
        self.epoca_de_retirada = epoca_de_retirada
        self.solapamiento = int(solapamiento)
        self.motivo = motivo

    def verifica_en(self, epoca):
        """¿Esta identidad puede verificar una firma de la época dada? Y por qué no."""
        if epoca < self.epoca_de_alta:
            return (False, "la firma es anterior al alta de la identidad")
        if self.estado == REVOCADA:
            return (False, "la identidad está REVOCADA: lo que firmó no vale, y su "
                           "solapamiento no se honra")
        if self.estado == ACTIVA:
            return (True, "")
        limite = self.epoca_de_retirada + self.solapamiento
        if epoca <= limite:
            return (True, "")
        return (False, "la identidad se retiró en la época " + str(self.epoca_de_retirada)
                       + " con solapamiento " + str(self.solapamiento) + ", luego verifica "
                       "hasta la " + str(limite) + " y la firma es de la " + str(epoca))

    def a_dict(self):
        """Forma publicable. Lleva la huella PÚBLICA y NINGÚN material sensible."""
        return {
            "id": self.id,
            "algoritmo": self.algoritmo,
            "huella_publica": self.huella_publica,
            "estado": self.estado,
            "epoca_de_alta": self.epoca_de_alta,
            "epoca_de_retirada": self.epoca_de_retirada,
            "solapamiento": self.solapamiento,
            "motivo": self.motivo,
        }


class AnilloDeIdentidades:
    """Las identidades públicas aceptadas. Vive FUERA del árbol verificado (`O25` §3)."""

    def __init__(self, identidades=(), *, epoca_vigente=1):
        self._por_id = {}
        for identidad in identidades:
            self.inscribir(identidad)
        self.epoca_vigente = int(epoca_vigente)
        self._traza = []

    def inscribir(self, identidad):
        if identidad.id in self._por_id:
            raise ConfiguracionInvalida(
                "identidad duplicada en el anillo: " + str(identidad.id)
            )
        self._por_id[identidad.id] = identidad
        return identidad

    def identidades(self):
        return tuple(self._por_id[clave] for clave in sorted(self._por_id))

    def obtener(self, identificador):
        identidad = self._por_id.get(identificador)
        if identidad is None:
            raise IdentidadDesconocida(
                "la configuración externa de confianza no acepta la identidad `"
                + str(identificador) + "`. El repositorio verificado no puede añadirla",
                identidad=str(identificador),
            )
        return identidad

    def activa(self):
        for identidad in self.identidades():
            if identidad.estado == ACTIVA:
                return identidad
        raise IdentidadDesconocida(
            "el anillo no tiene ninguna identidad ACTIVA con la que firmar"
        )

    # -- las tres operaciones de `O25` §3 -----------------------------------
    def rotar(self, *, nueva, motivo, solapamiento=SOLAPAMIENTO_POR_DEFECTO):
        """Retira la activa y da de alta la nueva, con solapamiento EXPLÍCITO en épocas."""
        saliente = self.activa()
        self.epoca_vigente += 1
        saliente.estado = RETIRADA
        saliente.epoca_de_retirada = self.epoca_vigente
        saliente.solapamiento = int(solapamiento)
        saliente.motivo = motivo
        nueva.epoca_de_alta = self.epoca_vigente
        nueva.estado = ACTIVA
        self.inscribir(nueva)
        self._anotar("rotacion", saliente, motivo)
        self._anotar("alta", nueva, motivo)
        return {"saliente": saliente.a_dict(), "entrante": nueva.a_dict(),
                "epoca": self.epoca_vigente, "solapamiento": int(solapamiento)}

    def revocar(self, identificador, *, motivo):
        identidad = self.obtener(identificador)
        self.epoca_vigente += 1
        identidad.estado = REVOCADA
        if identidad.epoca_de_retirada is None:
            identidad.epoca_de_retirada = self.epoca_vigente
        identidad.motivo = motivo
        self._anotar("revocacion", identidad, motivo)
        return identidad.a_dict()

    def exigir_valida(self, identificador, epoca):
        """Fallo cerrado. Desconocida · revocada · fuera de solapamiento, cada una con lo suyo."""
        identidad = self.obtener(identificador)
        puede, causa = identidad.verifica_en(int(epoca))
        if puede:
            return identidad
        if identidad.estado == REVOCADA:
            raise IdentidadRevocada(causa, identidad=identidad.id)
        raise IdentidadFueraDeSolapamiento(causa, identidad=identidad.id)

    # -- trazabilidad SIN revelación de secretos ---------------------------
    def _anotar(self, acto, identidad, motivo):
        self._traza.append({
            "acto": acto,
            "identidad": identidad.id,
            "huella_publica": identidad.huella_publica,
            "estado": identidad.estado,
            "epoca": self.epoca_vigente,
            "motivo": motivo,
        })

    def traza(self):
        """La traza de aprovisionamiento y rotación. Sin una sola clave privada dentro."""
        return [dict(apunte) for apunte in self._traza]

    def a_dict(self):
        return {
            "epoca_vigente": self.epoca_vigente,
            "identidades": [identidad.a_dict() for identidad in self.identidades()],
            "traza": self.traza(),
        }
