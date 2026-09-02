#!/usr/bin/env python3
"""errores — la jerarquía tipada de fallos del motor de estado durable.

Instancia la regla dura del §0 del contrato: **nunca `except Exception: pass`, nunca un
`assert` como control**. Todo lo que puede salir mal sale por una de estas clases, y cada
una lleva un `codigo` ESTABLE en MAYUSCULAS_CON_GUION_BAJO que la CLI imprime y que una
prueba puede comparar sin depender del texto castellano del `detalle`.

DECISIÓN · el código vive en la CLASE, no en la instancia
    Alternativas razonables: (a) pasar el código en cada `raise`; (b) derivarlo del nombre
    de la clase; (c) declararlo como atributo de clase.
    Se elige (c). (a) permite que dos `raise` de la misma clase emitan códigos distintos,
    y entonces el código deja de ser el contrato estable que el §8 promete. (b) parece
    elegante pero ata el texto del contrato al nombre Python: renombrar una clase cambiaría
    silenciosamente la evidencia publicada. Con (c) el código es un dato explícito,
    revisable de un vistazo contra el §8, y `codigo` sigue siendo legible en la instancia.
    Preserva `g.5` y `g.13`: un fallo cerrado se identifica siempre igual en la evidencia.

DECISIÓN · el error transporta `ruta` y un `contexto` libre
    El §8 exige `.codigo`, `.detalle` y `.ruta`. Se añade `contexto`, un diccionario
    determinista y ordenable, porque sin él la única forma de dar detalle estructurado
    (revisión esperada frente a encontrada, cid esperado frente a calculado) sería
    incrustarlo en el texto del `detalle`, y entonces la evidencia dejaría de ser
    comparable byte a byte. `a_dict()` lo emite ordenado.

Ninguna salida de este módulo reproduce credenciales: `detalle` y `contexto` los compone el
motor con rutas lógicas y digests, nunca con contenido de fichero ni con entorno.
"""
from __future__ import annotations


class ErrorDeEstado(Exception):
    """Raíz de todo fallo del motor. Nadie captura `Exception` por encima de ésta."""

    CODIGO = "ERROR_DE_ESTADO"

    def __init__(self, detalle="", ruta=None, codigo=None, **contexto):
        # `codigo` explícito sólo se usa para los pocos fallos que no tienen clase propia
        # en el §8 (por ejemplo, operar sobre un almacén ya cerrado). No se ofrece como
        # atajo para inventar códigos nuevos: el §8 es la lista cerrada.
        self.codigo = codigo or self.CODIGO
        self.detalle = detalle
        self.ruta = ruta
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


class AlmacenNoInicializado(ErrorDeEstado):
    CODIGO = "ALMACEN_NO_INICIALIZADO"


class AlmacenYaInicializado(ErrorDeEstado):
    CODIGO = "ALMACEN_YA_INICIALIZADO"


class FormatoDesconocido(ErrorDeEstado):
    CODIGO = "FORMATO_DESCONOCIDO"


class VersionDesconocida(ErrorDeEstado):
    CODIGO = "VERSION_DESCONOCIDA"


class RutaInvalida(ErrorDeEstado):
    CODIGO = "RUTA_INVALIDA"


class TransicionInvalida(ErrorDeEstado):
    CODIGO = "TRANSICION_INVALIDA"


class IdentificadorDuplicado(ErrorDeEstado):
    CODIGO = "IDENTIFICADOR_DUPLICADO"


class RevisionObsoleta(ErrorDeEstado):
    CODIGO = "REVISION_OBSOLETA"


class EscritorConcurrente(ErrorDeEstado):
    CODIGO = "ESCRITOR_CONCURRENTE"


class BloqueoNoAdquirido(ErrorDeEstado):
    CODIGO = "BLOQUEO_NO_ADQUIRIDO"


class ReintentosAgotados(ErrorDeEstado):
    CODIGO = "REINTENTOS_AGOTADOS"


class EstadoCorrupto(ErrorDeEstado):
    CODIGO = "ESTADO_CORRUPTO"


class DiarioCorrupto(ErrorDeEstado):
    CODIGO = "DIARIO_CORRUPTO"


class RegistroDeReconciliacionCorrupto(ErrorDeEstado):
    CODIGO = "REGISTRO_DE_RECONCILIACION_CORRUPTO"


class RecuperacionMarcada(ErrorDeEstado):
    CODIGO = "RECUPERACION_MARCADA"


class ReconciliacionPendiente(ErrorDeEstado):
    CODIGO = "RECONCILIACION_PENDIENTE"


class ReconciliacionDesconocida(ErrorDeEstado):
    CODIGO = "RECONCILIACION_DESCONOCIDA"


class MigracionDesconocida(ErrorDeEstado):
    CODIGO = "MIGRACION_DESCONOCIDA"


class MigracionNoRecuperable(ErrorDeEstado):
    CODIGO = "MIGRACION_NO_RECUPERABLE"


class PermisoInsuficiente(ErrorDeEstado):
    CODIGO = "PERMISO_INSUFICIENTE"


class SinProveedorDeAtestacion(ErrorDeEstado):
    CODIGO = "SIN_PROVEEDOR_DE_ATESTACION"


class AtestacionInvalida(ErrorDeEstado):
    CODIGO = "ATESTACION_INVALIDA"


class EvidenciaDentroDelArbol(ErrorDeEstado):
    CODIGO = "EVIDENCIA_DENTRO_DEL_ARBOL"


# Censo derivado, no escrito a mano dos veces: la CLI y las pruebas lo usan para comprobar
# que todo código emitido pertenece a la lista cerrada del §8.
CLASES = (
    ErrorDeEstado, AlmacenNoInicializado, AlmacenYaInicializado, FormatoDesconocido,
    VersionDesconocida, RutaInvalida, TransicionInvalida, IdentificadorDuplicado,
    RevisionObsoleta, EscritorConcurrente, BloqueoNoAdquirido, ReintentosAgotados,
    EstadoCorrupto, DiarioCorrupto, RegistroDeReconciliacionCorrupto, RecuperacionMarcada,
    ReconciliacionPendiente, ReconciliacionDesconocida, MigracionDesconocida,
    MigracionNoRecuperable, PermisoInsuficiente, SinProveedorDeAtestacion,
    AtestacionInvalida, EvidenciaDentroDelArbol,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
