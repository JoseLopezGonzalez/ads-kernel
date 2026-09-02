#!/usr/bin/env python3
"""configuracion — la CONFIGURACIÓN EXTERNA DE CONFIANZA. Instancia `O25` §3 y `g.15`.

    `O25` §3   «La configuración externa de confianza establece la identidad o huella
               pública aceptada. **El repositorio verificado no puede cambiar por sí mismo
               qué identidad acepta la raíz externa.**»
    `g.15`     «recibe DESDE FUERA su configuración y su política de admisión: su autoridad
               NO puede depender del árbol que verifica»

DECISIÓN · la configuración se RECHAZA si está dentro del árbol verificado
    Alternativas: (a) avisar y seguir; (b) `ConfiguracionDentroDelArbol` y no arrancar.
    Se elige (b). Un aviso lo lee quien opera y lo ignora quien ataca. Si la configuración
    vive dentro, quien puede escribir en el árbol decide quién lo verifica, y todo el
    aparato deja de significar nada: no es una degradación, es la pérdida completa de la
    propiedad. La comprobación resuelve la ruta con `realpath`, como ya hace
    `estado/atestacion.py`, porque un enlace simbólico mete un fichero dentro sin que la
    ruta lo parezca.

DECISIÓN · lo que la configuración APORTA es la autoridad, no una preferencia
    Trae tres cosas y las tres son autoridad: qué identidades se aceptan y en qué estado
    (`O25` §3), cuál es el ANCLA de la revisión y del censo de zonas (`V6-17`), y qué
    mutaciones están ADMITIDAS. Ninguna de las tres puede salir del árbol, porque el árbol
    las usaría para aprobarse a sí mismo.

DECISIÓN · `exportar()` no publica NADA sensible, y no depende de acordarse
    No se filtra por nombres de clave «que suenen a secreto»: se construye desde una lista
    BLANCA de campos publicables. Un campo nuevo no aparece en la exportación hasta que
    alguien lo añada a la lista, que es el sentido correcto del fallo por omisión. `O25` §2
    prohíbe que la clave aparezca en «configuración exportada», literalmente.

DECISIÓN · la orden de firma se declara aquí y la ejecuta el ANFITRIÓN
    `O25` §2 deja la custodia al proveedor de secretos o claves del sistema anfitrión, y §6
    del contrato del macrobloque excluye elegir un proveedor productivo concreto. Lo que se
    declara es CÓMO se le pide una firma —una orden externa— y la clave nunca cruza esta
    frontera: entra el mensaje, sale la firma.
"""
from __future__ import annotations

import os

from admision.formulas import leer_fichero_de_datos

from .errores import ConfiguracionDentroDelArbol, ConfiguracionInvalida
from .rotacion import SOLAPAMIENTO_POR_DEFECTO, AnilloDeIdentidades, Identidad

CLAVES = ("version", "autoridad", "orden_de_firma", "identidades", "ancla")

# Lista BLANCA de lo publicable. Todo lo que no esté aquí NO se exporta.
CAMPOS_PUBLICABLES = ("version", "autoridad", "epoca_vigente", "identidades", "ancla",
                      "admitidas", "orden_de_firma_declarada")


class ConfiguracionDeConfianza:
    """La configuración externa ya validada y localizada FUERA del árbol verificado."""

    def __init__(self, datos, ruta, arbol_verificado):
        self._datos = datos
        self.ruta = os.path.basename(ruta)
        self.arbol_verificado = arbol_verificado

    # -- lo que aporta ------------------------------------------------------
    def autoridad(self):
        return self._datos["autoridad"]

    def orden_de_firma(self):
        return list(self._datos["orden_de_firma"])

    def orden_de_verificacion(self):
        declarada = self._datos.get("orden_de_verificacion")
        return list(declarada) if declarada else None

    def anillo(self):
        identidades = []
        for entrada in self._datos["identidades"] or []:
            identidades.append(Identidad(
                identificador=entrada["id"],
                algoritmo=entrada["algoritmo"],
                huella_publica=entrada["huella_publica"],
                estado=entrada["estado"],
                epoca_de_alta=int(entrada["epoca_de_alta"]),
                epoca_de_retirada=(int(entrada["epoca_de_retirada"])
                                   if entrada.get("epoca_de_retirada") not in (None, "")
                                   else None),
                solapamiento=int(entrada.get("solapamiento", SOLAPAMIENTO_POR_DEFECTO)),
                motivo=entrada.get("motivo", ""),
            ))
        return AnilloDeIdentidades(
            identidades, epoca_vigente=int(self._datos.get("epoca_vigente", 1))
        )

    def declaracion(self):
        """La DECLARACIÓN DE ADMISIÓN que el verificador consume. Viene de FUERA."""
        from admision.perimetro import Declaracion
        ancla = self._datos["ancla"] or {}
        return Declaracion(
            ancla=ancla.get("base"),
            autoridad=self.autoridad(),
            admitidas=self._datos.get("admitidas") or [],
            digest_del_censo=ancla.get("digest_del_censo"),
        )

    # -- exportación, sin un solo secreto -----------------------------------
    def exportar(self):
        salida = {
            "version": self._datos["version"],
            "autoridad": self._datos["autoridad"],
            "epoca_vigente": int(self._datos.get("epoca_vigente", 1)),
            "identidades": [identidad.a_dict() for identidad in self.anillo().identidades()],
            "ancla": dict(self._datos["ancla"] or {}),
            "admitidas": [dict(entrada) for entrada in (self._datos.get("admitidas") or [])],
            # La orden de firma se publica sólo por su PROGRAMA, no por sus argumentos: un
            # argumento puede llevar un identificador de secreto del anfitrión, y `O25` §2
            # prohíbe que nada de eso viaje en la configuración exportada.
            "orden_de_firma_declarada": os.path.basename(self._datos["orden_de_firma"][0]),
        }
        return {clave: salida[clave] for clave in CAMPOS_PUBLICABLES if clave in salida}


def _resolver(ruta):
    absoluta = os.path.abspath(ruta)
    directorio = os.path.dirname(absoluta) or "."
    return os.path.join(os.path.realpath(directorio), os.path.basename(absoluta))


def exigir_fuera_del_arbol(ruta, arbol_verificado):
    """`O25` §3: la configuración NO puede vivir dentro de lo que gobierna."""
    arbol = os.path.realpath(arbol_verificado)
    resuelta = _resolver(ruta)
    if resuelta == arbol or resuelta.startswith(arbol + os.sep):
        raise ConfiguracionDentroDelArbol(
            "la configuración externa de confianza está DENTRO del árbol verificado. Si "
            "viviera ahí, el repositorio decidiría por sí mismo qué identidad se acepta, y "
            "`O25` §3 lo prohíbe",
            ruta=os.path.basename(resuelta),
        )
    return resuelta


def cargar(ruta, *, arbol_verificado):
    """Carga la configuración externa. Falla cerrado; no completa lo que falte."""
    resuelta = exigir_fuera_del_arbol(ruta, arbol_verificado)
    datos = leer_fichero_de_datos(resuelta)
    if not isinstance(datos, dict):
        raise ConfiguracionInvalida("la configuración externa no es un mapa", ruta=ruta)
    faltan = [clave for clave in CLAVES if clave not in datos]
    if faltan:
        raise ConfiguracionInvalida(
            "la configuración externa no declara " + ", ".join(faltan), ruta=ruta
        )
    if not isinstance(datos["orden_de_firma"], list) or not datos["orden_de_firma"]:
        raise ConfiguracionInvalida(
            "`orden_de_firma` es la orden del ANFITRIÓN que produce la firma, y tiene que "
            "ser una lista no vacía. Sin ella no hay proveedor válido (`O25` §2)",
            ruta=ruta,
        )
    if not datos["identidades"]:
        raise ConfiguracionInvalida(
            "la configuración externa no acepta ninguna identidad: sin identidades "
            "aceptadas no se verifica nada, y el fallo es CERRADO",
            ruta=ruta,
        )
    for entrada in datos["identidades"]:
        for clave in ("id", "algoritmo", "huella_publica", "estado", "epoca_de_alta"):
            if clave not in entrada:
                raise ConfiguracionInvalida(
                    "una identidad de la configuración no declara `" + clave + "`",
                    ruta=ruta,
                )
        # Guarda explícita: la configuración declara HUELLAS PÚBLICAS. Si alguien mete ahí
        # una clave, se rechaza el fichero entero en vez de usarlo.
        for prohibida in ("clave", "clave_privada", "secreto", "material"):
            if prohibida in entrada:
                raise ConfiguracionInvalida(
                    "la configuración externa declara `" + prohibida + "` en una identidad. "
                    "`O25` §2 dice que la clave privada permanece fuera de todos los "
                    "repositorios y de la configuración exportada: aquí sólo va la huella "
                    "pública",
                    ruta=ruta,
                )
    return ConfiguracionDeConfianza(datos, resuelta, os.path.realpath(arbol_verificado))
