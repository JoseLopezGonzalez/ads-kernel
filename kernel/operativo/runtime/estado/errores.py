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

import os

# El nombre del directorio raíz del almacén. Vive AQUÍ, y no en `rutas`, porque quien lo
# necesita primero es el saneador de rutas de más abajo, y `rutas` importa de este módulo:
# la dependencia sólo puede ir en un sentido. `rutas.RAIZ_ALMACEN` lo reexporta, de modo que
# la disposición física sigue teniendo un único nombre y una única definición.
RAIZ_ALMACEN = "estado"


def relativizar(ruta):
    """Recorta una ruta ABSOLUTA de la máquina a partir de la raíz del almacén.

    Defecto que previene, y es doble:

      1 · DETERMINISMO. El §11 y `I-g3` exigen que la salida sea comparable byte a byte
          entre máquinas. Un `/home/quien-sea/proyecto/estado/diario/DIARIO.jsonl` dentro
          de un mensaje de error convierte la evidencia publicada en algo que cambia con el
          usuario, el directorio temporal y la máquina.
      2 · FUGA. Una ruta absoluta describe el árbol de directorios de quien ejecuta, y eso
          acaba en un log, en una captura de pantalla o en un issue.

    Se sanea AQUÍ, en el constructor del error, y no en cada `raise`. La alternativa era
    que cada módulo relativizara al construir su error: `motor` lo hacía y `bloqueo`,
    `diario`, `reconciliacion` y `atestacion` no, en unos veinte sitios, y el resultado fue
    que la promesa del docstring de la CLI era falsa justo en los caminos de error, que son
    los que se publican. Un saneador central no se puede olvidar, y cubre también el
    módulo que alguien escriba mañana.

    Lo que NO toca: las rutas ya relativas (`estado/diario/DIARIO.jsonl`), las rutas
    lógicas (`items/it-1.json`) y los identificadores (`rec-0001`, `tx-3`). Todas ellas ya
    son deterministas y se devuelven intactas.
    """
    if not isinstance(ruta, str) or not ruta:
        return ruta
    if not os.path.isabs(ruta):
        return ruta
    partes = ruta.replace("\\", "/").split("/")
    # El ÚLTIMO segmento `estado`, no el primero: si el control repo colgara de un
    # directorio llamado también `estado`, quedarse con el primero devolvería una ruta que
    # no es la del almacén.
    for indice in range(len(partes) - 1, -1, -1):
        if partes[indice] == RAIZ_ALMACEN:
            return "/".join(partes[indice:])
    # Fuera del almacén —la evidencia de atestación de `g.15` vive fuera a propósito— no
    # hay raíz respecto a la que relativizar, y el nombre a secas es lo único que se puede
    # decir sin publicar el árbol de directorios de quien ejecuta.
    return partes[-1]


class ErrorDeEstado(Exception):
    """Raíz de todo fallo del motor. Nadie captura `Exception` por encima de ésta."""

    CODIGO = "ERROR_DE_ESTADO"

    def __init__(self, detalle="", ruta=None, codigo=None, **contexto):
        # `codigo` explícito sólo se usa para los pocos fallos que no tienen clase propia
        # en el §8 (por ejemplo, operar sobre un almacén ya cerrado). No se ofrece como
        # atajo para inventar códigos nuevos: el §8 es la lista cerrada.
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


class PublicacionEnVuelo(ErrorDeEstado):
    """El objeto en disco es el NUEVO y `REVISION.json` todavía nombra el viejo.

    NO es corrupción, y llamarlo corrupción es un diagnóstico falso que manda al operador a
    buscar un fichero roto que no existe. Es la VENTANA DE PUBLICACION del protocolo: entre
    el paso 8 —que reemplaza los objetos en `canonico/`— y el paso 9 —que publica la
    revisión— un LECTOR CONCURRENTE, que no toma el bloqueo de escritor porque leer no lo
    exige, ve el objeto nuevo con la revisión vieja.

    Se emite sólo cuando el TESTIGO del paso 8 confirma que ese `cid` es exactamente el que
    esa transacción acaba de publicar; en cualquier otro caso el error sigue siendo
    `EstadoCorrupto`, y sigue siendo fallo CERRADO: aquí tampoco se devuelve contenido.
    La diferencia es el REMEDIO —esperar a que la transacción cierre, o recuperar por la
    rama COMPLETAR— frente a «un fichero fue modificado fuera del diario».
    """

    CODIGO = "PUBLICACION_EN_VUELO"


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


# --------------------------------------------------------- el SELLADO del diario (`g.7`)
#
# Los cuatro fallos del sellado son CUATRO y no uno, y la razón es la misma que el §8 da
# para el resto: el código es lo que una prueba compara y lo que un guion enrama. «No se
# pudo sellar» sirve para todo y no distingue el remedio, que aquí es distinto en cada caso:
# calibrar el contrato, cerrar la ventana, firmar la transición o no retirar ese cuerpo.
class UmbralDeSelladoInvalido(ErrorDeEstado):
    """El umbral no está declarado, no se puede leer, o el valor leído es absurdo.

    `g.7` lo declara CALIBRABLE del contrato derivado, y calibrable no es lo mismo que
    opcional: un umbral que falta NO se sustituye por un valor por omisión silencioso,
    porque entonces el contrato dejaría de ser la sede y el código volvería a serlo.
    """

    CODIGO = "UMBRAL_DE_SELLADO_INVALIDO"


class SelladoImposible(ErrorDeEstado):
    """Sellar no puede conservar lo que el estado o la auditabilidad exigen: NO se sella."""

    CODIGO = "SELLADO_IMPOSIBLE"


class RetiradaSinTransicion(ErrorDeEstado):
    """Se intentó retirar el cuerpo de un evento sin la transición que `g.7` exige."""

    CODIGO = "RETIRADA_SIN_TRANSICION"


class RetiradaNoAdmisible(ErrorDeEstado):
    """El cuerpo que se pide retirar todavía lo necesitan la recuperación o la auditoría."""

    CODIGO = "RETIRADA_NO_ADMISIBLE"


# Censo derivado, no escrito a mano dos veces: la CLI y las pruebas lo usan para comprobar
# que todo código emitido pertenece a la lista cerrada del §8.
CLASES = (
    ErrorDeEstado, AlmacenNoInicializado, AlmacenYaInicializado, FormatoDesconocido,
    VersionDesconocida, RutaInvalida, TransicionInvalida, IdentificadorDuplicado,
    RevisionObsoleta, EscritorConcurrente, BloqueoNoAdquirido, ReintentosAgotados,
    EstadoCorrupto, PublicacionEnVuelo, DiarioCorrupto, RegistroDeReconciliacionCorrupto,
    RecuperacionMarcada,
    ReconciliacionPendiente, ReconciliacionDesconocida, MigracionDesconocida,
    MigracionNoRecuperable, PermisoInsuficiente, SinProveedorDeAtestacion,
    AtestacionInvalida, EvidenciaDentroDelArbol,
    UmbralDeSelladoInvalido, SelladoImposible, RetiradaSinTransicion, RetiradaNoAdmisible,
)

CODIGOS = tuple(sorted(clase.CODIGO for clase in CLASES))
