#!/usr/bin/env python3
"""proveedor — `ProveedorProductivo`, que DELEGA la firma en el anfitrión. `O25` §2 y §5.

**REUTILIZA `estado.ProveedorDeFirma`. No lo duplica.** Este módulo no implementa ninguna
primitiva criptográfica: `O25` §5 dice que `F6` «utilizará criptografía estándar y una
biblioteca o proveedor mantenido» y que «no implementará primitivas criptográficas propias».
Aquí lo que hay es una FRONTERA: entra el mensaje, sale la firma, y la clave privada no
cruza en ningún sentido.

DECISIÓN · se delega en una ORDEN EXTERNA declarada en la configuración externa
    Alternativas: (a) leer la clave de un fichero y firmar aquí; (b) pedirle la firma al
    anfitrión.
    Se elige (b), y es lo que `O25` §2 exige: la clave la custodia «una identidad de servicio
    dedicada del verificador externo mediante un proveedor de secretos o claves del sistema
    anfitrión», «no será accesible por el runtime ni por los agentes del repositorio» y «será
    no exportable cuando el proveedor lo permita». Con (a) el proceso que verifica tendría la
    clave en su espacio de memoria y cualquier volcado la publicaría. Con (b) este proceso
    nunca la ve, y en un anfitrión con clave no exportable —un HSM, un llavero del sistema—
    es que no puede verla ni queriendo.

DECISIÓN · qué NO es esto, dicho contra su propio interés
    Esto NO es un despliegue de raíz externa y NO cierra `V6-16`. Es la interfaz por la que
    un anfitrión se enchufa, más un anfitrión de PRUEBAS para poder demostrar el circuito.
    §6 del contrato del macrobloque excluye explícitamente «un proveedor productivo de claves
    concreto», y `O25` §6 dice que la resolución «no declara implementada ni certificada la
    raíz externa». Aquí no se elige tecnología de firma productiva.

DECISIÓN · el anfitrión de pruebas usa HMAC, y su limitación se declara
    HMAC-SHA256 de `hmac`/`hashlib` es criptografía estándar de una biblioteca mantenida
    (CPython), luego usarlo NO viola `O25` §5. Lo que sí hay que decir es que es SIMÉTRICO:
    quien verifica puede firmar. Una raíz externa de verdad necesita lo contrario —verificar
    sin poder firmar—, y eso lo aporta un anfitrión con firma asimétrica, que este entorno no
    ofrece y que `O25` §2 deja al anfitrión. `estado/atestacion.py` ya dejó escrita la misma
    advertencia sobre `ProveedorEfimero`, y aquí no se contradice.

DECISIÓN · un fallo del anfitrión NO degrada a un proveedor propio
    `AnfitrionNoResponde`, y se acabó. Caer a una firma local ante un anfitrión caído
    produciría evidencia firmada por una autoridad que nadie aceptó, que es un veredicto
    falseado desde dentro con papeles en regla.
"""
from __future__ import annotations

import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estado.atestacion import ProveedorDeFirma                       # noqa: E402

from .errores import (                                               # noqa: E402
    AnfitrionNoResponde,
    FirmaInvalida,
    SinProveedorDeIdentidad,
)

LIMITE_DE_ESPERA = 30.0


class ProveedorProductivo(ProveedorDeFirma):
    """Firma delegando en el anfitrión. No toca la clave privada y no la puede tocar."""

    def __init__(self, configuracion, *, identidad=None, limite_segundos=LIMITE_DE_ESPERA):
        if configuracion is None:
            raise SinProveedorDeIdentidad(
                "no hay configuración externa de confianza: `O25` §2 manda fallar cerrado "
                "ante la ausencia de un proveedor válido"
            )
        self._configuracion = configuracion
        self._anillo = configuracion.anillo()
        self._identidad = (self._anillo.obtener(identidad) if identidad
                           else self._anillo.activa())
        self._orden = configuracion.orden_de_firma()
        self._orden_de_verificacion = configuracion.orden_de_verificacion()
        self._limite = float(limite_segundos)
        if not self._orden:
            raise SinProveedorDeIdentidad(
                "la configuración externa no declara la orden de firma del anfitrión"
            )
        programa = self._orden[0]
        if not os.path.isfile(programa) or not os.access(programa, os.X_OK):
            raise SinProveedorDeIdentidad(
                "la orden de firma declarada por la configuración externa no es un "
                "ejecutable disponible. Sin proveedor válido no se firma con nada",
                ruta=os.path.basename(programa),
            )

    # -- interfaz de `estado.ProveedorDeFirma` -----------------------------
    def identidad(self):
        """La identidad PÚBLICA. No revela la clave, y no puede: no la tiene."""
        return (self._identidad.algoritmo + ":" + self._identidad.id + ":"
                + self._identidad.huella_publica)

    def firmar(self, datos):
        if not isinstance(datos, (bytes, bytearray)):
            raise FirmaInvalida("sólo se firman bytes")
        salida = self._invocar(self._orden + ["firmar", self._identidad.id], bytes(datos))
        try:
            firma = bytes.fromhex(salida.decode("ascii", "strict").strip())
        except (UnicodeDecodeError, ValueError) as exc:
            raise AnfitrionNoResponde(
                "el anfitrión no devolvió una firma hexadecimal. No se firma con nada en "
                "su lugar"
            ) from exc
        if not firma:
            raise AnfitrionNoResponde("el anfitrión devolvió una firma vacía")
        return firma

    def verificar(self, datos, firma):
        if not isinstance(firma, (bytes, bytearray)) or not firma:
            return False
        orden = self._orden_de_verificacion or self._orden
        salida = self._invocar(
            orden + ["verificar", self._identidad.id, firma.hex()], bytes(datos),
            tolerar_fallo=True,
        )
        return salida.strip() == b"valida"

    # -- la frontera con el anfitrión --------------------------------------
    def _invocar(self, orden, entrada, *, tolerar_fallo=False):
        entorno = {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "LC_ALL": "C", "LANG": "C",
        }
        # El anfitrión puede necesitar localizar su propio almacén de secretos. Lo hace por
        # una variable que la configuración externa fija; este proceso la PASA y no la lee.
        for nombre in ("ADS_ANFITRION_ALMACEN",):
            if nombre in os.environ:
                entorno[nombre] = os.environ[nombre]
        try:
            proceso = subprocess.run(
                orden, input=entrada, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                env=entorno, timeout=self._limite, check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise AnfitrionNoResponde(
                "no se pudo obtener respuesta del anfitrión de firma: "
                + type(exc).__name__
            ) from exc
        if proceso.returncode != 0 and not tolerar_fallo:
            # NO se publica `stderr`: podría llevar material del anfitrión, y `O25` §2
            # prohíbe que nada de eso aparezca en un error.
            raise AnfitrionNoResponde(
                "el anfitrión de firma devolvió el código " + str(proceso.returncode)
                + ". Su salida de error NO se publica, por si llevara material sensible"
            )
        return proceso.stdout

    # -- consultas ----------------------------------------------------------
    def anillo(self):
        return self._anillo

    def a_dict(self):
        """Forma publicable del proveedor. Sin clave, sin ruta absoluta, sin argumentos."""
        return {
            "identidad": self.identidad(),
            "estado": self._identidad.estado,
            "autoridad": self._configuracion.autoridad(),
            "anfitrion": os.path.basename(self._orden[0]),
            "custodia": "el anfitrión; este proceso no accede a la clave privada (`O25` §2)",
        }


def exigir_proveedor(proveedor):
    """`O25` §2: sin proveedor válido, FALLO CERRADO. No hay ruta por defecto."""
    if proveedor is None:
        raise SinProveedorDeIdentidad(
            "no se ha dado proveedor de identidad; `O25` §2 no admite una ruta por defecto"
        )
    for metodo in ("identidad", "firmar", "verificar"):
        if not callable(getattr(proveedor, metodo, None)):
            raise SinProveedorDeIdentidad(
                "el proveedor no implementa `" + metodo + "`"
            )
    valor = proveedor.identidad()
    if not isinstance(valor, str) or not valor.strip():
        raise SinProveedorDeIdentidad("el proveedor no declara identidad pública")
    return valor
