#!/usr/bin/env python3
"""atestacion — INTERFAZ de la raíz externa de confianza (`g.15`). No es un despliegue.

`g.5` termina con una frase que este módulo existe para respetar: **ningún resumen calculado
por el propio árbol basta como prueba de la integridad de ese árbol**. `cid_raiz` identifica
contenido, pero quien puede reescribir un fichero puede reescribir también el digest que él
mismo calculó. La prueba pertenece a una raíz externa, y `g.15` fija sus condiciones: se
ejecuta FUERA, con identidad SIN permiso de escritura, recibe su política desde fuera, y
produce EVIDENCIA fuera del árbol verificado.

**Lo que este módulo NO es, dicho contra su propio interés:** no es la raíz externa. Es la
interfaz por la que una raíz externa se enchufaría, y un proveedor de pruebas para poder
demostrar el circuito. `FD-1` sigue abierta: aquí no se elige titular, ni custodio de clave,
ni tecnología de firma productiva.

DECISIÓN · la interfaz base FALLA en vez de estar vacía
    Alternativas: (a) `raise NotImplementedError` en cada método; (b) `pass` y devolver
    `None`; (c) levantar `SinProveedorDeAtestacion`, que es un error del §8.
    Se elige (c). Con (b) un almacén sin proveedor produciría una «evidencia» firmada con
    nada y `verificar_atestacion` diría que sí: sería un veredicto falseado desde dentro,
    exactamente lo que `G-A9` obliga a desmentir. Con (a) el fallo sería de tipo ajeno a la
    jerarquía y un llamador que captura `ErrorDeEstado` lo dejaría escapar. Con (c) el
    §7 se cumple literalmente: **sin proveedor válido, fallo cerrado**.

DECISIÓN · la evidencia se niega a escribirse DENTRO del control repo
    `g.13` dice que la evidencia de verificación NO vive dentro del árbol verificado. Si
    viviera dentro, el propio acto de escribirla cambiaría el árbol que acaba de certificar,
    y quien manipulase el árbol podría manipular a la vez su certificado. `atestar` resuelve
    de verdad la ruta —con `realpath`, porque un enlace simbólico coloca un fichero dentro
    sin que la ruta lo parezca— y levanta `EvidenciaDentroDelArbol`.

DECISIÓN · la firma cubre la evidencia CANÓNICA sin el campo `firma`
    Alternativas: (a) firmar sólo `cid_raiz`; (b) firmar el documento entero menos la firma.
    Se elige (b). Con (a), la identidad del firmante, la revisión y el linaje quedarían
    fuera de la firma y se podrían intercambiar entre evidencias distintas: una evidencia
    legítima de otra revisión pasaría por la de ésta. Con (b) cualquier alteración de
    cualquier campo invalida la firma.

DECISIÓN · el determinismo de `I-g3` NO se aplica a la evidencia, y por eso vive fuera
    Un proveedor efímero genera una clave aleatoria, así que dos atestaciones del mismo
    árbol producen firmas distintas. Eso sería inadmisible dentro de `estado/`. Es admisible
    fuera, porque `I-g3` habla de los artefactos DURABLES del estado, y la evidencia es
    justamente lo que `g.13` expulsa del árbol.
"""
from __future__ import annotations

import hashlib
import hmac
import os
import secrets

from .errores import (
    AtestacionInvalida,
    EvidenciaDentroDelArbol,
    SinProveedorDeAtestacion,
)
from .rutas import escribir_y_sincronizar, leer_bytes, sincronizar_directorio
from .serializacion import ESQUEMA, deserializar, serializar_canonico

CLAVE_FIRMA = "firma"


class ProveedorDeFirma:
    """Interfaz de firma de la raíz externa. Un proveedor concreto la implementa entera.

    No es abstracta por decoración sino por comportamiento: sus tres métodos fallan cerrado
    con `SinProveedorDeAtestacion`. Usarla tal cual NO produce una firma vacía ni un `True`
    complaciente, que es la única forma en que una interfaz vacía puede hacer daño.
    """

    def identidad(self):
        raise SinProveedorDeAtestacion(
            "`ProveedorDeFirma` es la interfaz de `g.15` y no firma nada por sí misma; "
            "se necesita un proveedor concreto con identidad declarada"
        )

    def firmar(self, datos):
        raise SinProveedorDeAtestacion(
            "`ProveedorDeFirma` no firma: sin proveedor válido el §7 manda fallar cerrado, "
            "y no existe una ruta por defecto que firme con nada"
        )

    def verificar(self, datos, firma):
        raise SinProveedorDeAtestacion(
            "`ProveedorDeFirma` no verifica: una verificación por defecto que devolviera "
            "`True` sería un veredicto falseado desde dentro del árbol"
        )


class ProveedorEfimero(ProveedorDeFirma):
    """HMAC-SHA256 con clave en memoria. **EXCLUSIVAMENTE PARA PRUEBAS.**

    **Este proveedor es EXCLUSIVAMENTE PARA PRUEBAS y NO es una solución de custodia
    productiva.** Su clave se genera en memoria, no se guarda en ninguna parte, muere con el
    proceso y no está respaldada por ninguna autoridad. Una evidencia firmada por él sólo
    puede verificarla el mismo proceso que la produjo, o quien reciba la clave por otro
    canal, lo cual no es custodia: es una comodidad de laboratorio.

    Además, HMAC es un esquema SIMÉTRICO: quien puede verificar puede firmar. Una raíz
    externa de verdad necesita lo contrario —verificar sin poder firmar—, y por eso `g.15`
    exige una identidad SIN permiso de escritura sobre lo que verifica. Sustituir esto por
    firma asimétrica con custodia real es materia del contrato de raíz externa de `F6`, y
    `FD-1` sigue abierta.
    """

    ALGORITMO = "hmac-sha256"

    def __init__(self, clave=None, nombre="efimero"):
        # `secrets` y no `random`: una clave predecible convertiría la firma en un adorno.
        # Que sea aleatoria es también la razón por la que la evidencia vive FUERA del árbol.
        self._clave = clave if clave is not None else secrets.token_bytes(32)
        if not isinstance(self._clave, (bytes, bytearray)) or len(self._clave) < 16:
            raise SinProveedorDeAtestacion(
                "la clave de un proveedor efímero son al menos 16 bytes"
            )
        self._nombre = nombre

    def identidad(self):
        # La identidad NO revela la clave: es el digest de la clave con un dominio de
        # separación. Publicar la clave en la evidencia sería publicar una credencial.
        digest = hashlib.sha256(b"ads.estado/identidad\x00" + bytes(self._clave)).hexdigest()
        return self.ALGORITMO + ":" + self._nombre + ":" + digest[:16]

    def firmar(self, datos):
        if not isinstance(datos, (bytes, bytearray)):
            raise AtestacionInvalida("sólo se firman bytes")
        return hmac.new(bytes(self._clave), bytes(datos), hashlib.sha256).digest()

    def verificar(self, datos, firma):
        if not isinstance(firma, (bytes, bytearray)):
            return False
        esperada = self.firmar(datos)
        # `compare_digest` y no `==`: la comparación byte a byte con salida temprana filtra
        # información por tiempo, y una verificación que se puede sondear no verifica.
        return hmac.compare_digest(esperada, bytes(firma))


def _exigir_proveedor(proveedor):
    if proveedor is None:
        raise SinProveedorDeAtestacion(
            "no se ha dado proveedor de firma; el §7 no admite una ruta por defecto"
        )
    for metodo in ("identidad", "firmar", "verificar"):
        if not callable(getattr(proveedor, metodo, None)):
            raise SinProveedorDeAtestacion(
                "el proveedor no implementa `" + metodo + "`"
            )
    identidad = proveedor.identidad()
    if not isinstance(identidad, str) or not identidad.strip():
        raise SinProveedorDeAtestacion("el proveedor no declara identidad")
    return identidad


def _exigir_fuera_del_arbol(almacen, destino):
    """La evidencia no puede caer dentro del control repo verificado (`g.13`, `g.15`)."""
    repo = os.path.realpath(almacen.ruta)
    absoluto = os.path.abspath(destino)
    directorio = os.path.dirname(absoluto) or "."
    # Se resuelve el DIRECTORIO padre, que sí existe: `realpath` sobre un fichero aún
    # inexistente no seguiría el enlace que lo colocaría dentro del árbol.
    resuelto = os.path.join(os.path.realpath(directorio), os.path.basename(absoluto))
    if resuelto == repo or resuelto.startswith(repo + os.sep):
        raise EvidenciaDentroDelArbol(
            "la evidencia de verificación no vive dentro del árbol verificado; escribirla "
            "ahí cambiaría el árbol que acaba de certificar",
            ruta=os.path.basename(resuelto),
        )
    return resuelto


def atestar(almacen, proveedor, destino):
    """Produce evidencia firmada de la revisión vigente, FUERA del árbol verificado."""
    identidad = _exigir_proveedor(proveedor)
    resuelto = _exigir_fuera_del_arbol(almacen, destino)
    revision = almacen.revision()

    evidencia = {
        "esquema": ESQUEMA,
        "tipo": "atestacion",
        "identidad": identidad,
        "revision": revision["revision"],
        "revision_id": revision["revision_id"],
        "padre": revision["padre"],
        "cid_raiz": revision["cid_raiz"],
        "raiz": dict(revision["raiz"]),
        "transaccion": revision["transaccion"],
        "diario_secuencia": revision["diario_secuencia"],
        # Se dice DENTRO de la evidencia, para que quien la lea no la confunda con una
        # certificación productiva. `g.15` exige declarar las condiciones de certificación.
        "condiciones": [
            "la evidencia se produce fuera del árbol verificado",
            "el proveedor de firma se recibe desde fuera y no del árbol",
            "esta interfaz NO constituye una raíz externa desplegada ni certificada",
        ],
    }
    firma = proveedor.firmar(serializar_canonico(evidencia))
    if not isinstance(firma, (bytes, bytearray)) or not firma:
        raise AtestacionInvalida("el proveedor devolvió una firma vacía")
    evidencia[CLAVE_FIRMA] = firma.hex()

    escribir_y_sincronizar(resuelto, serializar_canonico(evidencia))
    sincronizar_directorio(os.path.dirname(resuelto) or ".")
    return evidencia


def verificar_atestacion(ruta_evidencia, proveedor, almacen=None):
    """Falla cerrado si la evidencia está manipulada, truncada o firmada por otra identidad.

    `almacen` es opcional y no altera la firma declarada en el §7: cuando se da, además de
    verificar la evidencia se CONTRASTA contra el árbol vivo, y ahí es donde `G-A9` se
    demuestra —un veredicto falseado desde dentro del árbol queda desmentido por una
    evidencia externa que ya no casa—.
    """
    identidad = _exigir_proveedor(proveedor)
    datos = leer_bytes(ruta_evidencia, error=AtestacionInvalida)
    evidencia = deserializar(datos, ruta=ruta_evidencia, error=AtestacionInvalida)
    if not isinstance(evidencia, dict):
        raise AtestacionInvalida("la evidencia no es un objeto JSON", ruta=ruta_evidencia)
    for clave in ("esquema", "tipo", "identidad", "revision_id", "cid_raiz", CLAVE_FIRMA):
        if clave not in evidencia:
            raise AtestacionInvalida(
                "la evidencia está truncada: falta `" + clave + "`", ruta=ruta_evidencia
            )
    if evidencia["identidad"] != identidad:
        raise AtestacionInvalida(
            "la evidencia está firmada por otra identidad: declara "
            + str(evidencia["identidad"]) + " y se verifica contra " + identidad,
            ruta=ruta_evidencia,
        )
    cuerpo = {clave: evidencia[clave] for clave in evidencia if clave != CLAVE_FIRMA}
    try:
        firma = bytes.fromhex(evidencia[CLAVE_FIRMA])
    except ValueError as exc:
        raise AtestacionInvalida(
            "la firma no es hexadecimal", ruta=ruta_evidencia
        ) from exc
    if not proveedor.verificar(serializar_canonico(cuerpo), firma):
        raise AtestacionInvalida(
            "la firma no casa con el contenido: la evidencia fue manipulada",
            ruta=ruta_evidencia,
        )

    informe = {
        "valida": True,
        "identidad": identidad,
        "revision": evidencia.get("revision"),
        "revision_id": evidencia["revision_id"],
        "cid_raiz": evidencia["cid_raiz"],
        "contrastada_con_el_arbol": False,
        "casa_con_el_arbol": None,
    }
    if almacen is not None:
        vigente = almacen.revision()
        informe["contrastada_con_el_arbol"] = True
        casa = (
            vigente["revision_id"] == evidencia["revision_id"]
            and vigente["cid_raiz"] == evidencia["cid_raiz"]
        )
        informe["casa_con_el_arbol"] = casa
        if not casa:
            raise AtestacionInvalida(
                "la evidencia externa no casa con el árbol: el árbol declara "
                + vigente["cid_raiz"] + " y la evidencia certificó " + evidencia["cid_raiz"]
                + ". Un veredicto falseado desde dentro queda así desmentido",
                ruta=ruta_evidencia,
            )
    return informe
