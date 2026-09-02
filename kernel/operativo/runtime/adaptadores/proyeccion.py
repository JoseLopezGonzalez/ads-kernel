#!/usr/bin/env python3
"""proyeccion — piezas 2 y 3 de `11-ARQUITECTURA-INTEGRADA.md` §6. Corte `V7`.

    Pieza 2 · PROYECCIONES GENERADAS
        se COMPILAN desde definición canónica + kernel + packs + PERFIL + overrides, y
        llevan versión de ADS, versión del adaptador, origen canónico, aviso de generado y
        HUELLA. Regla `I5`: derivadas, NO editables.

    Pieza 3 · HUELLA Y VALIDADOR DE DERIVA
        detecta una proyección editada a mano, una obsoleta respecto de su fuente, y dos
        que dicen cosas distintas sobre lo mismo. El remedio ante huella rota es
        RECOMPILAR, no sincronizar.

DECISIÓN · la huella cubre las ENTRADAS, y además el CUERPO se sella aparte
    Alternativas: (a) sólo huella de las entradas; (b) sólo digest del cuerpo; (c) las dos.
    Se elige (c), y las dos son necesarias porque detectan cosas distintas. La huella de las
    entradas detecta la proyección OBSOLETA: las fuentes cambiaron y ésta no se recompiló.
    El digest del cuerpo detecta la proyección EDITADA A MANO: las fuentes no han cambiado y
    el fichero sí. Con sólo (a), editar la proyección a mano pasa desapercibido —la huella
    de las entradas sigue casando—, que es exactamente `P-06` y las cuatro skills que
    divergieron. Con sólo (b) no se distingue «editada» de «obsoleta», y §6.3 exige los dos
    diagnósticos por separado.

DECISIÓN · el diagnóstico distingue tres desenlaces, y NO dos
    `AL_DIA` · `EDITADA_A_MANO` · `OBSOLETA`. Confundir «editada» con «obsoleta» bajo un
    mismo «no casa» es el defecto que §11.2 corrige en `P-08` y que §6.7 vuelve a nombrar:
    dos causas bajo un mismo diagnóstico llevan al remedio equivocado. Editada se arregla
    recompilando y perdiendo la edición; obsoleta se arregla recompilando y ganando lo nuevo.

DECISIÓN · la proyección se marca GENERADA en su primera línea, y el aviso entra en el digest
    Un aviso que no entrara en el digest se podría quitar sin que la huella lo notara, y la
    siguiente persona editaría el fichero creyendo que es fuente.
"""
from __future__ import annotations

import os

from admision.formulas import digest_de_contenido, digest_de_lista

from .contrato import ProyeccionDerivada, ProyeccionObsoleta

AVISO = "FICHERO GENERADO POR ADS. NO SE EDITA A MANO: se RECOMPILA."
MARCA_DE_HUELLA = "ads:huella"
MARCA_DE_CUERPO = "ads:sello"

AL_DIA = "AL_DIA"
EDITADA_A_MANO = "EDITADA_A_MANO"
OBSOLETA = "OBSOLETA"


def huella_de_entradas(entradas):
    """Huella de las ENTRADAS de la compilación. `entradas` es `{nombre: bytes}`."""
    partes = []
    for nombre in sorted(entradas):
        partes.append(nombre + ":" + digest_de_contenido(entradas[nombre]))
    return digest_de_lista(partes)


def compilar(*, adaptador, version_de_ads, entradas, cuerpo, origen_canonico):
    """Compila una proyección y la ESTAMPA con la huella de sus entradas.

    Devuelve el TEXTO de la proyección. No lo escribe: dónde vive lo impone el entorno, y
    §6.2 dice que ADS no lo elige.
    """
    huella = huella_de_entradas(entradas)
    cabecera = [
        "# " + AVISO,
        "# ads:adaptador " + str(adaptador),
        "# ads:version-de-ads " + str(version_de_ads),
        "# ads:origen " + str(origen_canonico),
        "# " + MARCA_DE_HUELLA + " " + huella,
        "# ads:entradas " + " ".join(sorted(entradas)),
    ]
    texto = "\n".join(cabecera) + "\n\n" + cuerpo.rstrip("\n") + "\n"
    sello = digest_de_contenido(texto)
    return texto + "# " + MARCA_DE_CUERPO + " " + sello + "\n"


def _leer_marca(texto, marca):
    for linea in texto.splitlines():
        recorte = linea.strip()
        if recorte.startswith("# " + marca + " "):
            return recorte[len("# " + marca + " "):].strip()
    return None


def validar_deriva(texto, entradas):
    """Diagnóstico de una proyección: `AL_DIA`, `EDITADA_A_MANO` u `OBSOLETA`.

    Se comprueba PRIMERO el sello del cuerpo y DESPUÉS la huella de las entradas. El orden
    importa: si el fichero está editado a mano, su huella declarada ya no es de fiar y
    compararla contra las entradas produciría un diagnóstico inventado.
    """
    sello_declarado = _leer_marca(texto, MARCA_DE_CUERPO)
    huella_declarada = _leer_marca(texto, MARCA_DE_HUELLA)
    if sello_declarado is None or huella_declarada is None:
        return {
            "diagnostico": EDITADA_A_MANO,
            "detalle": "la proyección no declara su sello o su huella: o no la generó ADS, "
                       "o alguien le quitó la cabecera",
            "remedio": "recompilar",
        }
    marca = "# " + MARCA_DE_CUERPO + " " + sello_declarado + "\n"
    if not texto.endswith(marca):
        return {
            "diagnostico": EDITADA_A_MANO,
            "detalle": "el sello no está al final del fichero",
            "remedio": "recompilar",
        }
    cuerpo = texto[: -len(marca)]
    if digest_de_contenido(cuerpo) != sello_declarado:
        return {
            "diagnostico": EDITADA_A_MANO,
            "detalle": "el cuerpo de la proyección no casa con su sello: ha sido editada a "
                       "mano. Editar una proyección no es configurar, es fabricar deriva",
            "remedio": "recompilar, no sincronizar",
        }
    vigente = huella_de_entradas(entradas)
    if vigente != huella_declarada:
        return {
            "diagnostico": OBSOLETA,
            "detalle": "las entradas de la compilación han cambiado y esta proyección se "
                       "compiló desde las anteriores",
            "remedio": "recompilar",
            "huella_declarada": huella_declarada,
            "huella_vigente": vigente,
        }
    return {"diagnostico": AL_DIA, "detalle": "", "remedio": ""}


def exigir_al_dia(texto, entradas):
    """Fallo cerrado: `ProyeccionDerivada` si editada, `ProyeccionObsoleta` si obsoleta."""
    informe = validar_deriva(texto, entradas)
    if informe["diagnostico"] == EDITADA_A_MANO:
        raise ProyeccionDerivada(informe["detalle"])
    if informe["diagnostico"] == OBSOLETA:
        raise ProyeccionObsoleta(informe["detalle"])
    return informe


def comparar_proyecciones(proyecciones):
    """§6.3: «dos proyecciones que dicen cosas distintas sobre lo mismo».

    `proyecciones` es `{nombre: texto}`. Devuelve las que no comparten huella de entradas:
    si dos proyecciones del mismo producto declaran huellas distintas, se compilaron desde
    fuentes distintas y al menos una miente sobre el estado del producto.
    """
    por_huella = {}
    for nombre in sorted(proyecciones):
        huella = _leer_marca(proyecciones[nombre], MARCA_DE_HUELLA)
        por_huella.setdefault(huella, []).append(nombre)
    if len(por_huella) <= 1:
        return {"coherentes": True, "grupos": {k: v for k, v in por_huella.items()}}
    return {
        "coherentes": False,
        "grupos": {str(k): v for k, v in sorted(por_huella.items(), key=lambda p: str(p[0]))},
        "detalle": "dos proyecciones declaran huellas de entrada distintas: se compilaron "
                   "desde fuentes distintas y dicen cosas distintas sobre lo mismo",
    }


def escribir(ruta, texto):
    """Escribe una proyección. Cierra el fichero y sincroniza el directorio."""
    directorio = os.path.dirname(os.path.abspath(ruta)) or "."
    os.makedirs(directorio, exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as manejador:
        manejador.write(texto)
        manejador.flush()
        os.fsync(manejador.fileno())
    descriptor = os.open(directorio, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    return ruta
