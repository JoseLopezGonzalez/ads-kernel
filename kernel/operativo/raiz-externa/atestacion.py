#!/usr/bin/env python3
"""atestacion — la ATESTACIÓN de la raíz externa, VINCULADA al commit y al `tree`.

§11.8, literal: «la atestación queda **vinculada al SHA del commit y al `tree` SHA**, y no a
un nombre de rama, a una fecha ni a un número de ejecución». Y `g.15`: la evidencia es
«trazable y vinculada a la revisión exacta».

DECISIÓN · el objeto firmado es la ATESTACIÓN CANÓNICA, y la firma va FUERA de ella
    Alternativas: (a) meter la firma dentro del mismo objeto y firmar el resto; (b) firmar
    el objeto entero y publicar la firma al lado.
    Se elige (b). Con (a) hay que definir «el resto», y esa definición es una segunda regla
    que puede discrepar de la primera: quien firma y quien verifica tienen que estar de
    acuerdo en qué bytes se excluyen, y una discrepancia produce firmas que no verifican o,
    peor, campos que quedan fuera de lo firmado sin que se note. Con (b) lo firmado es
    exactamente el documento, byte a byte, y el sobre lleva la firma al lado.

DECISIÓN · la serialización canónica es JSON con claves ORDENADAS y `ensure_ascii=False`
    Firmar depende de los BYTES. Dos serializaciones del mismo objeto con distinto orden de
    claves producen firmas distintas y una verificación que falla sin que nada esté mal. El
    orden se fija, la indentación se fija, y el resultado termina en un salto de línea.

DECISIÓN · NI FECHA, NI DURACIÓN, NI NÚMERO DE EJECUCIÓN, NI PID
    `I-g3`. Una atestación con hora de pared cambia entre dos ejecuciones sobre el mismo
    commit, y entonces «la misma entrada produce la misma evidencia» deja de ser cierto. Lo
    que ancla la atestación en el tiempo es la ÉPOCA de la identidad, que es tiempo lógico.

DECISIÓN · la atestación lleva la VERSIÓN de la herramienta de firma y su ALGORITMO
    Una dependencia externa sin versión registrada no es reproducible, y §11.8 exige que las
    huellas se recalculen «en ese entorno externo». Registrar `OpenSSH_8.9p1` y `ssh-ed25519`
    dentro de lo firmado hace que un cambio de herramienta sea visible en la evidencia.
"""
from __future__ import annotations

import hashlib
import json

from errores import AtestacionInvalida

ESQUEMA = 1
TIPO = "atestacion-de-raiz-externa"

CAMPOS_OBLIGATORIOS = (
    "esquema", "tipo", "autoridad", "identidad", "huella_publica", "epoca",
    "repositorio", "veredicto", "proveedor",
)


def canonizar(atestacion):
    """Los BYTES exactos que se firman y que se verifican. Una sola forma, siempre."""
    return (json.dumps(atestacion, sort_keys=True, ensure_ascii=False, indent=2)
            + "\n").encode("utf-8")


def digest(atestacion):
    """SHA-256 de la forma canónica. Es lo que la trazabilidad publica sin repetir el cuerpo."""
    return hashlib.sha256(canonizar(atestacion)).hexdigest()


def construir(*, autoridad, identidad, huella_publica, epoca, commit, tree, veredicto,
              proveedor, alcance=None):
    """La atestación, vinculada al COMMIT y al `tree`. Ningún nombre de rama entra aquí."""
    if not commit or not tree:
        raise AtestacionInvalida(
            "una atestación sin `commit` y sin `tree` no está vinculada a nada: `§11.8` "
            "prohíbe atestar sobre un nombre de rama"
        )
    cuerpo = {
        "esquema": ESQUEMA,
        "tipo": TIPO,
        "autoridad": autoridad,
        "identidad": identidad,
        "huella_publica": huella_publica,
        "epoca": int(epoca),
        "repositorio": {"commit": commit, "tree": tree},
        "veredicto": veredicto,
        "proveedor": proveedor,
    }
    if alcance is not None:
        cuerpo["alcance"] = alcance
    return cuerpo


def exigir_forma(atestacion):
    """Fallo CERRADO ante una atestación que no tiene la forma que este esquema define."""
    if not isinstance(atestacion, dict):
        raise AtestacionInvalida("la atestación no es un mapa")
    faltan = [clave for clave in CAMPOS_OBLIGATORIOS if clave not in atestacion]
    if faltan:
        raise AtestacionInvalida(
            "la atestación no declara " + ", ".join(faltan)
            + "; una clave ausente NUNCA se completa con un valor por defecto"
        )
    if atestacion["esquema"] != ESQUEMA:
        raise AtestacionInvalida(
            "versión de esquema desconocida en la atestación: "
            + str(atestacion["esquema"]) + ". No se adivina"
        )
    if atestacion["tipo"] != TIPO:
        raise AtestacionInvalida("la atestación no es del tipo `" + TIPO + "`")
    repositorio = atestacion["repositorio"]
    if not isinstance(repositorio, dict) or not repositorio.get("commit") \
            or not repositorio.get("tree"):
        raise AtestacionInvalida(
            "la atestación no está vinculada a un commit y a un `tree` concretos"
        )
    return True


def exigir_vinculo(atestacion, *, commit, tree):
    """La atestación tiene que hablar EXACTAMENTE del commit y del árbol que se comprueban."""
    exigir_forma(atestacion)
    registrado = atestacion["repositorio"]
    if registrado["commit"] != commit:
        raise AtestacionInvalida(
            "la atestación habla del commit " + str(registrado["commit"])[:12]
            + " y se está comprobando " + str(commit)[:12]
        )
    if registrado["tree"] != tree:
        raise AtestacionInvalida(
            "la atestación habla del árbol " + str(registrado["tree"])[:12]
            + " y el commit comprobado tiene el árbol " + str(tree)[:12]
            + ": el commit coincide y su CONTENIDO no"
        )
    return True


class Sobre:
    """La atestación y su FIRMA, juntas en un fichero y separadas en el objeto."""

    def __init__(self, atestacion, firma_hex):
        self.atestacion = atestacion
        self.firma_hex = firma_hex

    @property
    def firma(self):
        return bytes.fromhex(self.firma_hex)

    def a_dict(self):
        return {
            "atestacion": self.atestacion,
            "firma": {
                "formato": "ssh-signature-armored-hex",
                "valor": self.firma_hex,
                "digest_de_lo_firmado": digest(self.atestacion),
            },
        }

    def serializar(self):
        return (json.dumps(self.a_dict(), sort_keys=True, ensure_ascii=False, indent=2)
                + "\n")

    @classmethod
    def desde_texto(cls, texto):
        try:
            datos = json.loads(texto)
        except ValueError as exc:
            raise AtestacionInvalida(
                "el sobre de atestación no es JSON válido: se DENUNCIA y no se interpreta "
                "a medias"
            ) from exc
        if not isinstance(datos, dict) or "atestacion" not in datos \
                or "firma" not in datos:
            raise AtestacionInvalida(
                "el sobre de atestación no trae `atestacion` y `firma`"
            )
        firma = datos["firma"]
        if not isinstance(firma, dict) or not firma.get("valor"):
            raise AtestacionInvalida("el sobre no trae el valor de la firma")
        sobre = cls(datos["atestacion"], firma["valor"])
        esperado = firma.get("digest_de_lo_firmado")
        if esperado and esperado != digest(sobre.atestacion):
            raise AtestacionInvalida(
                "el digest que el sobre publica no es el de la atestación que contiene: "
                "el sobre se ha manipulado"
            )
        return sobre
