#!/usr/bin/env python3
"""errores — jerarquía tipada de la RAÍZ EXTERNA DE CONFIANZA. `g.15` y `O25`.

La regla de este paquete, y no admite matices: **la ausencia de cualquiera de sus condiciones
NO produce veredicto favorable.** Ni «verde con reserva», ni «verde porque no se pudo
comprobar». `g.15` lo dice —«FALLA CERRADO ante entrada inválida, truncamiento o estructura
inesperada»— y `O25` §2 lo repite para el proveedor de firma.

Este paquete vive FUERA de `runtime/` a propósito, y por eso NO importa la jerarquía de
errores del runtime: una raíz externa que dependiera de los módulos del árbol que verifica
dejaría de ser externa en cuanto ese árbol cambiara uno. El saneado de rutas se hace aquí,
con la misma regla —en el CONSTRUCTOR— y sin importar nada del árbol verificado.
"""
from __future__ import annotations

import os


def relativizar(ruta):
    """Recorta una ruta absoluta de la máquina a su nombre. Determinismo y no filtración.

    Es la misma regla que `estado/errores.py` aplica dentro del runtime, REESCRITA y no
    importada: este paquete se instala fuera y no puede depender de un módulo del árbol que
    verifica. Lo que se conserva es la propiedad —ninguna salida publica el árbol de
    directorios de quien ejecuta—, no la implementación.
    """
    if not isinstance(ruta, str) or not ruta:
        return ruta
    if not os.path.isabs(ruta):
        return ruta
    return os.path.basename(ruta.rstrip(os.sep)) or ruta


class ErrorDeRaizExterna(Exception):
    """Raíz de todo fallo de la raíz externa."""

    CODIGO = "ERROR_DE_RAIZ_EXTERNA"

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
        salida = {"codigo": self.codigo, "detalle": self.detalle, "ruta": self.ruta}
        if self.contexto:
            salida["contexto"] = {c: self.contexto[c] for c in sorted(self.contexto)}
        return salida


class ProveedorDeFirmaAusente(ErrorDeRaizExterna):
    """`O25` §2: sin proveedor de firma válido, FALLO CERRADO."""

    CODIGO = "PROVEEDOR_DE_FIRMA_AUSENTE"


class ClaveNoDisponible(ErrorDeRaizExterna):
    """La clave o el fichero de firmantes que la configuración declara no está."""

    CODIGO = "CLAVE_NO_DISPONIBLE"


class FirmaNoVerificada(ErrorDeRaizExterna):
    """La atestación no verifica contra los firmantes autorizados."""

    CODIGO = "FIRMA_NO_VERIFICADA"


class IdentidadNoAceptada(ErrorDeRaizExterna):
    """La identidad que firma no está en el anillo, o no verifica en esa época."""

    CODIGO = "IDENTIDAD_NO_ACEPTADA"


class InstalacionDentroDelArbol(ErrorDeRaizExterna):
    """`g.15`: la raíz externa NO se instala dentro del árbol que verifica."""

    CODIGO = "INSTALACION_DENTRO_DEL_ARBOL"


class EvidenciaDentroDelArbol(ErrorDeRaizExterna):
    """`g.13` y `g.15`: la evidencia NO vive dentro del árbol verificado."""

    CODIGO = "EVIDENCIA_DENTRO_DEL_ARBOL"


class InstalacionAlterada(ErrorDeRaizExterna):
    """El manifiesto de la instalación no casa con lo instalado."""

    CODIGO = "INSTALACION_ALTERADA"


class AtestacionInvalida(ErrorDeRaizExterna):
    """La atestación no tiene la forma esperada, o no habla del commit que se comprueba."""

    CODIGO = "ATESTACION_INVALIDA"


class VeredictoDesmentido(ErrorDeRaizExterna):
    """`G-A9`: el árbol se declara sano y la atestación externa lo DESMIENTE."""

    CODIGO = "VEREDICTO_DESMENTIDO"


class AislamientoNoDisponible(ErrorDeRaizExterna):
    """No hay forma de ejercer una identidad sin permiso de escritura sobre el árbol."""

    CODIGO = "AISLAMIENTO_NO_DISPONIBLE"


class EscrituraNoImpedida(ErrorDeRaizExterna):
    """Un intento de escritura que TENÍA que fallar no falló. Es la peor noticia posible."""

    CODIGO = "ESCRITURA_NO_IMPEDIDA"


class VinculoDeCommitRoto(AtestacionInvalida):
    """`E-07` · la atestación habla de OTRO commit que el que se está comprobando.

    Es una clase PROPIA y no un `AtestacionInvalida` genérico, y la razón es exactamente el
    defecto que cierra: mientras las dos mitades del vínculo —commit y `tree`— compartían
    código de salida y mensaje, una prueba que sólo mirase «falló» no distinguía cuál de las
    dos lo detectó, y sabotear una sola mitad dejaba la batería entera en verde. Con dos
    códigos estables, sabotear una mitad pone en rojo UNA prueba y sabotear la otra, OTRA.
    """

    CODIGO = "VINCULO_DE_COMMIT_ROTO"


class VinculoDeTreeRoto(AtestacionInvalida):
    """`E-07` · el commit coincide y su CONTENIDO no. La otra mitad, con su propio código."""

    CODIGO = "VINCULO_DE_TREE_ROTO"


class SecuenciaDeVerificacionIncompleta(ErrorDeRaizExterna):
    """`E-07` · se intentó escribir evidencia sin haber completado los SIETE pasos, o fuera
    de su orden. Escribir antes de terminar de verificar es publicar lo no verificado."""

    CODIGO = "SECUENCIA_DE_VERIFICACION_INCOMPLETA"


class AnclaNoCoincide(ErrorDeRaizExterna):
    """`E-07` · paso 6. La atestación no habla de la POLÍTICA que la configuración externa
    declara: otra base anclada, u otro digest de censo. Un veredicto calculado bajo otra
    política no es el veredicto de esta raíz externa."""

    CODIGO = "ANCLA_NO_COINCIDE"


class EmisorNoCoincide(ErrorDeRaizExterna):
    """`E-07` · paso 7. La atestación se atribuye a una identidad cuya huella PÚBLICA no es
    la que el anillo tiene inscrita para ese identificador."""

    CODIGO = "EMISOR_NO_COINCIDE"


CLASES = (
    ErrorDeRaizExterna, ProveedorDeFirmaAusente, ClaveNoDisponible, FirmaNoVerificada,
    IdentidadNoAceptada, InstalacionDentroDelArbol, EvidenciaDentroDelArbol,
    InstalacionAlterada, AtestacionInvalida, VeredictoDesmentido,
    AislamientoNoDisponible, EscrituraNoImpedida,
    VinculoDeCommitRoto, VinculoDeTreeRoto, SecuenciaDeVerificacionIncompleta,
    AnclaNoCoincide, EmisorNoCoincide,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
