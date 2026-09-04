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
import os

from errores import (
    AtestacionInvalida,
    SecuenciaDeVerificacionIncompleta,
    VinculoDeCommitRoto,
    VinculoDeTreeRoto,
)

ESQUEMA = 1
TIPO = "atestacion-de-raiz-externa"

# ---------------------------------------------------------------------------
#  `E-07` · LOS SIETE PASOS, EN SU ORDEN, Y LA EVIDENCIA DESPUÉS DE LOS SIETE
# ---------------------------------------------------------------------------
#  Hecho reproducido antes de corregir: `exigir_vinculo` comprobaba las dos mitades del
#  vínculo —commit y `tree`— con el mismo código de salida y el mismo mensaje, y NINGUNA DE
#  LAS DOS tenía cobertura individual: neutralizar la mitad `tree` dejaba la batería en
#  38/38 verde, y neutralizar la mitad `commit`, también. La causa no es que faltara una
#  prueba: es que las dos mitades eran INDISTINGUIBLES desde fuera, así que ninguna prueba
#  podía apuntar a una sola.
#
#  DECISIÓN · cada mitad tiene su propia FUNCIÓN y su propio CÓDIGO DE ERROR
#      Alternativas: (a) dejar una sola función y escribir dos pruebas que miren el texto del
#      mensaje; (b) partirla en dos funciones con dos clases de error estables.
#      Se elige (b). Con (a) la distinción vive en una cadena de texto que cualquier retoque
#      de redacción borra, y además una prueba que compara mensajes no ejercita la PROPIEDAD:
#      ejercita la ortografía. Con (b) sabotear la mitad `commit` pone en rojo exactamente la
#      prueba del commit, y sabotear la mitad `tree`, exactamente la del `tree`.
#
#  DECISIÓN · la evidencia se escribe por UNA función que EXIGE la secuencia completa
#      Alternativas: (a) confiar en que el `open(...)` esté escrito después de las
#      comprobaciones; (b) un testigo en memoria que enumere los pasos hechos y su orden, y
#      una función de escritura que lo exija.
#      Se elige (b), y por la misma razón que `E-08`: un orden que sólo existe porque el
#      código está escrito en cierto orden no es una garantía, es una costumbre. Reordenar
#      dos bloques no rompe nada y nadie se entera. Con el testigo, ADELANTAR la escritura
#      —o saltarse un paso— produce un error tipado y NINGÚN fichero.
PASOS_DE_VERIFICACION = (
    "firma",                    # 1 · la firma verifica contra los firmantes autorizados
    "clave-aceptada",           # 2 · esa identidad está inscrita en el anillo externo
    "epoca",                    # 3 · y es válida en la época que la atestación declara
    "commit",                   # 4 · la atestación habla del commit que se comprueba
    "tree",                     # 5 · y del `tree` de ese commit
    "politica",                 # 6 · el veredicto se calculó bajo el ancla de la config
    "identidad-del-emisor",     # 7 · la huella pública atestada es la del anillo
)


class SecuenciaDeVerificacion:
    """El TESTIGO de que los siete pasos se hicieron, y en su orden. `E-07`.

    No comprueba nada por sí misma: es la parte que hace OBSERVABLE lo que se comprobó. Las
    comprobaciones viven donde tienen los datos —`verificador.py`—; lo que aquí se impide es
    publicar evidencia sin haberlas hecho todas.
    """

    def __init__(self, pasos=PASOS_DE_VERIFICACION):
        self.pasos_exigidos = tuple(pasos)
        self.hechos = []

    def anotar(self, paso):
        """Anota un paso SUPERADO. Fuera de orden es un fallo, no un reordenamiento."""
        if paso not in self.pasos_exigidos:
            raise SecuenciaDeVerificacionIncompleta(
                "paso de verificación fuera del vocabulario cerrado `"
                + " · ".join(self.pasos_exigidos) + "`: " + str(paso)
            )
        esperado = self.pasos_exigidos[len(self.hechos)] \
            if len(self.hechos) < len(self.pasos_exigidos) else None
        if paso != esperado:
            raise SecuenciaDeVerificacionIncompleta(
                "los pasos de verificación se anotaron fuera de orden: tocaba `"
                + str(esperado) + "` y se anotó `" + str(paso) + "`. El orden ES la "
                "garantía: comprobar el `tree` antes que la firma acepta bytes que nadie "
                "ha autenticado",
                hechos=list(self.hechos), esperado=str(esperado),
            )
        self.hechos.append(paso)
        return self

    def completa(self):
        return tuple(self.hechos) == self.pasos_exigidos

    def pendientes(self):
        return tuple(p for p in self.pasos_exigidos if p not in self.hechos)

    def exigir_completa(self):
        if not self.completa():
            raise SecuenciaDeVerificacionIncompleta(
                "faltan pasos de verificación antes de publicar evidencia: "
                + ", ".join(self.pendientes()) + ". `g.15` falla CERRADO: una atestación "
                "que no ha superado los siete pasos NO se escribe, porque escribirla la "
                "convierte en un artefacto durable que alguien leerá como verificado",
                hechos=list(self.hechos), pendientes=list(self.pendientes()),
            )
        return True

    def a_dict(self):
        return {"pasos": list(self.pasos_exigidos), "hechos": list(self.hechos),
                "completa": self.completa()}


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


def exigir_commit(atestacion, commit):
    """MITAD 1 de 2 del vínculo. Tiene su propia función y su propio código a propósito."""
    exigir_forma(atestacion)
    registrado = atestacion["repositorio"]
    if registrado["commit"] != commit:
        raise VinculoDeCommitRoto(
            "la atestación habla del commit " + str(registrado["commit"])[:12]
            + " y se está comprobando " + str(commit)[:12],
            atestado=str(registrado["commit"])[:12], comprobado=str(commit)[:12],
        )
    return True


def exigir_tree(atestacion, tree):
    """MITAD 2 de 2. Un commit correcto con un `tree` que no es el suyo NO ata nada.

    No es redundante con `exigir_commit`, y por eso se comprueba aparte: el `tree` que la
    atestación registra es el que el verificador MIDIÓ, y el que se compara es el que Git
    resuelve AHORA para ese commit. Si alguien reescribe el objeto commit conservando su
    SHA —o, mucho más barato, si la atestación se fabricó a mano con un commit real y un
    árbol inventado—, la mitad `commit` pasa y sólo ésta lo detecta.
    """
    exigir_forma(atestacion)
    registrado = atestacion["repositorio"]
    if registrado["tree"] != tree:
        raise VinculoDeTreeRoto(
            "la atestación habla del árbol " + str(registrado["tree"])[:12]
            + " y el commit comprobado tiene el árbol " + str(tree)[:12]
            + ": el commit coincide y su CONTENIDO no",
            atestado=str(registrado["tree"])[:12], comprobado=str(tree)[:12],
        )
    return True


def exigir_vinculo(atestacion, *, commit, tree):
    """La atestación tiene que hablar EXACTAMENTE del commit y del árbol que se comprueban.

    Se conserva como una sola puerta —§11.8 ata la atestación a los DOS— y por dentro llama
    a las dos mitades, que son las que tienen cobertura individual.
    """
    exigir_commit(atestacion, commit)
    exigir_tree(atestacion, tree)
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


def escribir_evidencia(ruta, sobre, secuencia):
    """La ÚNICA puerta por la que la evidencia llega al disco. `E-07`.

    Exige el testigo COMPLETO antes de abrir nada. El orden importa dentro de la propia
    función: primero se exige, y sólo después se crea el directorio y se escribe. Al revés
    quedaría un directorio creado por una emisión que no llegó a emitir, y un `ls` diría que
    algo se publicó.
    """
    if not isinstance(secuencia, SecuenciaDeVerificacion):
        raise SecuenciaDeVerificacionIncompleta(
            "se intentó publicar evidencia sin testigo de verificación. La evidencia de la "
            "raíz externa NO se escribe «porque el código llegó hasta aquí»"
        )
    secuencia.exigir_completa()
    directorio = os.path.dirname(os.path.abspath(ruta)) or "."
    os.makedirs(directorio, exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as manejador:
        manejador.write(sobre.serializar())
    return ruta
