#!/usr/bin/env python3
"""contrato — la interfaz de ADAPTADOR. Corte `V7`.

La forma de `ejecutar` es EXACTAMENTE la del §4.4 del contrato del macrobloque, porque el
runtime del AGENTE A programa contra ella y una diferencia de un byte rompe el despacho:

    def ejecutar(self, orden: dict, *, efecto: str, limite_segundos: float,
                 progreso=None, cancelacion=None) -> dict
        # {"estado": "completado"|"fallido"|"cancelado"|"timeout",
        #  "codigo": int, "salida": str, "detalle": str,
        #  "reintentable": bool, "efecto": str, "repetido": bool}

Y la FICHA declarada es la de `11-ARQUITECTURA-INTEGRADA.md` §3.4, con sus trece campos.

DECISIÓN · `nivel` NO es un campo de la ficha, y esto NO es un olvido
    §6.5 lo corrige explícitamente: `nivel` era campo editable y a la vez conclusión derivada
    de una prueba de humo ejecutada, que es la segunda verdad que `I5` prohíbe. La ficha
    declara `compatibilidad`, que es una INTENCIÓN, y el nivel alcanzado se lee de las celdas
    de cobertura. Aquí no se escribe ningún nivel y no se ofrece ningún campo para escribirlo.

DECISIÓN · los errores del adaptador viven aquí y NO se importan del runtime
    Alternativas: (a) `from runtime.errores import CapacidadNoSoportada`; (b) definirlos aquí
    con el MISMO `codigo` estable.
    Se elige (b), y se dice lo que cuesta. El paquete `runtime/` lo construye otro agente en
    paralelo y un adaptador que no se pueda importar sin él sería inservible para probarse a
    sí mismo. El riesgo asumido es que existan dos clases con el mismo código: se mitiga
    porque lo que el runtime compara es el `codigo`, que es el contrato estable, y no la
    identidad de la clase. Si más adelante los dos paquetes se funden, la sede única es
    `runtime/errores.py` y estas clases se retiran.

DECISIÓN · la interfaz base FALLA en vez de estar vacía
    Es el mismo criterio que `estado/atestacion.py` ya aplicó a `ProveedorDeFirma`: un
    `ejecutar` por defecto que devolviera «completado» sería un efecto inventado, y el
    runtime escribiría un acuse durable de algo que no ocurrió. `NotImplementedError` queda
    fuera de la jerarquía y se escaparía de quien captura `ErrorDeAdaptador`, así que se
    levanta un error del propio §.
"""
from __future__ import annotations

VERSION_DE_CONTRATO = 1

# Los CINCO estados que `ejecutar` puede devolver, y ninguna otra palabra.
#
# `ambiguo` es el quinto y se añadió por un defecto MEDIDO: si el proceso del runtime moría
# entre ejecutar la tarea y escribir su recibo, al reiniciar se volvía a ejecutar y el efecto
# se aplicaba DOS VECES en silencio. Con un proceso externo cualquiera no existe «exactamente
# una vez»; lo que sí existe es NO DUPLICAR EN SILENCIO. `ambiguo` es la clase propia de ese
# desenlace: ni completado, ni fallido, ni cancelado, ni reintentable. El runtime lo trata
# como terminal y abre la reconciliación de `g.9`.
ESTADOS = ("completado", "fallido", "cancelado", "timeout", "ambiguo")
AMBIGUO = "ambiguo"

# Los trece campos de la ficha de §3.4, en su orden.
CAMPOS_DE_FICHA = (
    "identificador", "version", "capacidades", "operaciones", "limites", "timeout",
    "cancelacion", "idempotencia", "forma_de_progreso", "resultado", "errores",
    "evidencia", "compatibilidad",
)


class ErrorDeAdaptador(Exception):
    """Raíz de los fallos del contrato de adaptador."""

    CODIGO = "ERROR_DE_ADAPTADOR"

    def __init__(self, detalle="", codigo=None, **contexto):
        self.codigo = codigo or self.CODIGO
        self.detalle = detalle
        self.contexto = dict(contexto)
        super().__init__(str(self))

    def __str__(self):
        return "[" + self.codigo + "] " + self.detalle if self.detalle \
            else "[" + self.codigo + "]"

    def a_dict(self):
        salida = {"codigo": self.codigo, "detalle": self.detalle}
        if self.contexto:
            salida["contexto"] = {c: self.contexto[c] for c in sorted(self.contexto)}
        return salida


class CapacidadNoSoportada(ErrorDeAdaptador):
    CODIGO = "CAPACIDAD_NO_SOPORTADA"


class AdaptadorIncompatible(ErrorDeAdaptador):
    CODIGO = "ADAPTADOR_INCOMPATIBLE"


class OrdenInvalida(ErrorDeAdaptador):
    CODIGO = "ORDEN_INVALIDA"


class ProyeccionDerivada(ErrorDeAdaptador):
    """`I5`: una proyección es derivada y NO editable. Su huella está rota."""

    CODIGO = "PROYECCION_DERIVADA"


class ProyeccionObsoleta(ErrorDeAdaptador):
    """La proyección se compiló desde entradas que ya no son las vigentes."""

    CODIGO = "PROYECCION_OBSOLETA"


class Cancelacion:
    """Señal de cancelación cooperativa. El runtime pasa un objeto con `.activada()`."""

    def __init__(self):
        self._activada = False

    def activar(self):
        self._activada = True

    def activada(self):
        return self._activada


class FichaDeAdaptador:
    """La ficha declarada de §3.4. Es DATO: se lee, no se calcula."""

    def __init__(self, **campos):
        faltan = [nombre for nombre in CAMPOS_DE_FICHA if nombre not in campos]
        if faltan:
            raise OrdenInvalida(
                "la ficha de adaptador no declara " + ", ".join(faltan)
                + "; §3.4 exige los trece campos y una ausencia no es un valor por defecto"
            )
        sobran = [nombre for nombre in campos if nombre not in CAMPOS_DE_FICHA]
        if sobran:
            raise OrdenInvalida(
                "la ficha declara campos que §3.4 no tiene: " + ", ".join(sorted(sobran))
            )
        self._campos = dict(campos)

    def __getitem__(self, nombre):
        return self._campos[nombre]

    def a_dict(self):
        return {nombre: self._campos[nombre] for nombre in CAMPOS_DE_FICHA}


class Adaptador:
    """Interfaz base. Falla cerrado; no ejecuta nada y no inventa un resultado."""

    identificador = ""
    version_de_contrato = VERSION_DE_CONTRATO
    capacidades = ()

    def ficha(self):
        raise ErrorDeAdaptador(
            "`Adaptador` es la interfaz del corte `V7` y no declara ficha por sí misma"
        )

    def ejecutar(self, orden, *, efecto, limite_segundos, progreso=None, cancelacion=None):
        raise ErrorDeAdaptador(
            "`Adaptador` no ejecuta: un resultado por defecto haría que el runtime "
            "escribiera un acuse durable de un efecto que nunca ocurrió"
        )


def comprobar_resultado(resultado, efecto):
    """El resultado tiene la forma del §4.4, o no es un resultado. Fallo cerrado."""
    if not isinstance(resultado, dict):
        raise ErrorDeAdaptador("el adaptador no devolvió un mapa")
    for clave in ("estado", "codigo", "salida", "detalle", "reintentable", "efecto",
                  "repetido"):
        if clave not in resultado:
            raise ErrorDeAdaptador(
                "el resultado del adaptador no declara `" + clave + "`"
            )
    if resultado["estado"] not in ESTADOS:
        raise ErrorDeAdaptador(
            "estado de resultado fuera del vocabulario cerrado: " + str(resultado["estado"])
        )
    if resultado["efecto"] != efecto:
        raise ErrorDeAdaptador(
            "el resultado declara el efecto `" + str(resultado["efecto"]) + "` y se pidió `"
            + str(efecto) + "`: un acuse cruzado aplicaría un efecto por otro"
        )
    return resultado
