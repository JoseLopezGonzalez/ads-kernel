#!/usr/bin/env python3
"""propiedad — la TABLA DE PROPIEDAD del control repo, leída como DATO.

`g.14` dice que la tabla de propiedad —quién crea, confirma, publica, abre rama, integra,
verifica, revierte y retira rama— es materia suya y la instancia su contrato derivado. Aquí
está ese contrato derivado, y está como DATO en `POLITICA-CONTROL-REPO.yml` y no como código.

DECISIÓN · la política es DATO, no código
    Alternativas: (a) un diccionario en Python; (b) un fichero de datos leído y validado.
    Se elige (b). Con (a) la política se cambia con la misma acción con la que se cambia el
    instrumento, y una mutación de la política pasaría por «un cambio de código más». Con
    (b) la política tiene ruta propia, entra en la HUELLA por esa ruta, y `V6-11` puede
    medir que una mutación suya da ROJO. La forma es la del registro canónico
    (`FUENTES-CANONICAS.yml`) y se lee con la MISMA fórmula: `admision/formulas.py`.

DECISIÓN · la política no puede eximirse a sí misma, y se comprueba al CARGARLA
    No basta con no escribir la exención: alguien podría añadirla mañana. `cargar()` verifica
    que los prefijos de auto-inclusión cubren la propia ruta de la política y la del
    verificador, y levanta `PoliticaViolada` si no. Una política que se autoriza a sí misma
    se rechaza en el momento de leerla, no en el de aplicarla.

DECISIÓN · `escribe: []` es una DECLARACIÓN, no una omisión
    `g.12` dice que la raíz externa NO tiene permiso de escritura. Si la ausencia de la
    clave significara «sin restricción», olvidarla concedería permiso total. Aquí la lista
    vacía es explícita y la ausencia de la clave es `PoliticaViolada`.
"""
from __future__ import annotations

import os

from admision.formulas import digest_de_contenido, leer_fichero_de_datos

from .errores import PoliticaViolada

FICHERO = "POLITICA-CONTROL-REPO.yml"
RUTA_EN_EL_ARBOL = "kernel/operativo/runtime/gobierno/" + FICHERO

CLAVES = ("version", "actores", "operaciones", "materia", "refs", "prohibiciones",
          "autoinclusion", "publicacion")

# Las ocho de `g.14`, literalmente. Si una falta, la política no instancia su sede.
OPERACIONES_EXIGIDAS = (
    "crear", "confirmar", "publicar", "abrir-rama", "integrar", "verificar", "revertir",
    "retirar-rama",
)


class Politica:
    """La tabla de propiedad ya validada. Responde preguntas; no las adivina."""

    def __init__(self, datos, ruta):
        self._datos = datos
        self.ruta = ruta
        self.digest = None

    # -- consultas ---------------------------------------------------------
    def operaciones(self):
        return tuple(entrada["id"] for entrada in self._datos["operaciones"])

    def puede(self, actor, operacion):
        for entrada in self._datos["operaciones"]:
            if entrada["id"] == operacion:
                return actor in entrada["quien"]
        raise PoliticaViolada("operación no declarada en la política: " + str(operacion))

    def serializa(self, operacion):
        for entrada in self._datos["operaciones"]:
            if entrada["id"] == operacion:
                return entrada["serializa"] == "si"
        raise PoliticaViolada("operación no declarada en la política: " + str(operacion))

    def exige_revision_base(self, operacion):
        for entrada in self._datos["operaciones"]:
            if entrada["id"] == operacion:
                return entrada["exige_revision_base"] == "si"
        raise PoliticaViolada("operación no declarada en la política: " + str(operacion))

    def escribe(self, actor):
        for entrada in self._datos["materia"]:
            if entrada["actor"] == actor:
                return tuple(entrada["escribe"] or ())
        raise PoliticaViolada("actor no declarado en la política: " + str(actor))

    def puede_escribir(self, actor, ruta):
        for prefijo in self.escribe(actor):
            if ruta.startswith(prefijo):
                return True
        return False

    def refs_protegidas(self):
        return tuple(self._datos["refs"]["protegidas"])

    def mueve(self, ref):
        for entrada in self._datos["refs"].get("mueve") or []:
            if entrada["ref"] == ref:
                return tuple(entrada["actores"])
        return ()

    def prefijos_de_autoinclusion(self):
        return tuple(self._datos["autoinclusion"]["prefijos"])

    def publicacion_por_defecto(self):
        return self._datos["publicacion"]["por_defecto"]

    def prohibiciones(self):
        return tuple(entrada["id"] for entrada in self._datos["prohibiciones"])

    def a_dict(self):
        """Forma determinista y SIN secretos: la política no contiene ninguno, y se dice."""
        return {
            "ruta": RUTA_EN_EL_ARBOL,
            "digest": self.digest,
            "version": self._datos["version"],
            "actores": [entrada["id"] for entrada in self._datos["actores"]],
            "operaciones": list(self.operaciones()),
            "refs_protegidas": list(self.refs_protegidas()),
            "prohibiciones": list(self.prohibiciones()),
            "publicacion_por_defecto": self.publicacion_por_defecto(),
            "prefijos_de_autoinclusion": list(self.prefijos_de_autoinclusion()),
        }


def ruta_por_defecto():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), FICHERO)


def cargar(ruta=None):
    """Lee, VALIDA y devuelve la política. Falla cerrado; no completa lo que falte."""
    ruta = ruta or ruta_por_defecto()
    datos = leer_fichero_de_datos(ruta)
    if not isinstance(datos, dict):
        raise PoliticaViolada("la política no es un mapa de claves", ruta=ruta)
    faltan = [clave for clave in CLAVES if clave not in datos]
    if faltan:
        raise PoliticaViolada(
            "la política no declara " + ", ".join(faltan)
            + "; una clave ausente NUNCA significa «sin restricción»",
            ruta=ruta,
        )
    declaradas = {entrada.get("id") for entrada in datos["operaciones"] or []}
    sin_declarar = [nombre for nombre in OPERACIONES_EXIGIDAS if nombre not in declaradas]
    if sin_declarar:
        raise PoliticaViolada(
            "la tabla de propiedad de `g.14` exige las ocho operaciones y faltan: "
            + ", ".join(sin_declarar),
            ruta=ruta,
        )
    for entrada in datos["materia"] or []:
        if "escribe" not in entrada:
            raise PoliticaViolada(
                "el actor `" + str(entrada.get("actor")) + "` no declara `escribe`; la "
                "lista VACÍA es una declaración y la ausencia es un defecto",
                ruta=ruta,
            )
    if datos["publicacion"].get("por_defecto") != "esperando-owner":
        raise PoliticaViolada(
            "`g.14`: la política de publicación tiene valor por defecto `esperando-owner`, "
            "y la ausencia de política declarada NUNCA significa «publica»",
            ruta=ruta,
        )
    if not datos["refs"].get("protegidas"):
        raise PoliticaViolada("la política no protege ninguna ref", ruta=ruta)
    if datos["refs"].get("borrado_permitido"):
        raise PoliticaViolada(
            "ninguna política puede autorizar el borrado de una ref protegida (`g.14`)",
            ruta=ruta,
        )

    politica = Politica(datos, ruta)
    # AUTO-INCLUSIÓN, comprobada al cargar y no al aplicar: la política tiene que cubrir su
    # propia ruta y la del verificador. Una política que se dejara fuera se autorizaría.
    prefijos = politica.prefijos_de_autoinclusion()
    for obligatoria in (RUTA_EN_EL_ARBOL, "kernel/operativo/runtime/admision/perimetro.py"):
        if not any(obligatoria.startswith(prefijo) for prefijo in prefijos):
            raise PoliticaViolada(
                "la política no se incluye a sí misma: `" + obligatoria + "` queda fuera "
                "de sus prefijos de auto-inclusión, y `V6-11` no lo admite",
                ruta=ruta,
            )
    with open(ruta, "rb") as manejador:
        politica.digest = digest_de_contenido(manejador.read())
    return politica
