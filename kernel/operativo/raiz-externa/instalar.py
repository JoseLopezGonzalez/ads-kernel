#!/usr/bin/env python3
"""instalar — COPIA la raíz externa a una instalación FUERA del árbol verificado. `g.15`.

§11.8 lo dice de dos maneras y las dos hay que cumplirlas:

    NO SUSTITUIBLE POR   «no puede sustituirse por un script alojado ÚNICAMENTE dentro del
    UN SCRIPT INTERNO     mismo repositorio. Un verificador que vive donde vive lo verificado
                          no es externo, por muy bien escrito que esté»
    ENTORNO EXTERNO       «la batería se ejecuta desde un entorno limpio, construido de
    LIMPIO                nuevo, sin estado heredado»
    VERIFICACIÓN DE       «kernel, contratos, validadores y manifiestos, cada uno por su
    HASHES                huella, **recalculada en ese entorno externo y no leída del árbol**»

    python3 instalar.py --destino <dir fuera del árbol> --arbol <repo verificado>

DECISIÓN · la instalación se lleva también las DEPENDENCIAS, y no las importa del árbol
    Alternativas: (a) instalar sólo este paquete y añadir el `runtime/` del árbol al
    `sys.path`; (b) COPIAR las dependencias a la instalación.
    Se elige (b). Con (a) la raíz externa importaría el verificador DESDE EL ÁRBOL QUE
    VERIFICA, y quien pueda escribir ese árbol decide cómo se le verifica: es exactamente lo
    que `g.15` prohíbe con «su autoridad NO puede depender del árbol que verifica». El coste
    de (b) es que la instalación envejece respecto del árbol; el remedio es reinstalar, y el
    manifiesto hace visible con qué versión se emitió cada veredicto.

DECISIÓN · el destino se RECHAZA si cae dentro del árbol verificado
    Con `realpath` por los dos caminos —el directorio y el fichero—, igual que hace
    `identidad/configuracion.py` con la configuración de confianza, porque un enlace
    simbólico mete un destino dentro sin que la ruta lo parezca.

DECISIÓN · el manifiesto guarda SHA-256 por fichero, y la comprobación es SEPARADA
    Instalar y comprobar son dos actos. `verificar_instalacion()` recalcula todos los
    digests en el entorno externo y denuncia cualquier diferencia: es la mitad de §11.8 que
    dice «recalculada en ese entorno externo y no leída del árbol».

DECISIÓN · el manifiesto NO lleva fecha ni número de instalación
    `I-g3`. Dos instalaciones del mismo árbol producen el MISMO manifiesto, byte a byte, y
    esa propiedad es la que permite comparar dos instalaciones sin más herramienta que `cmp`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from errores import (                                                # noqa: E402
    ErrorDeRaizExterna,
    InstalacionAlterada,
    InstalacionDentroDelArbol,
)

AQUI = os.path.dirname(os.path.abspath(__file__))
NOMBRE_DEL_PAQUETE = "raiz-externa"
NOMBRE_DEL_RUNTIME = "runtime"
MANIFIESTO = "MANIFIESTO-DE-INSTALACION.json"

# Los paquetes del runtime de los que depende el verificador de admisión. Se COPIAN, no se
# importan del árbol. La lista es corta a propósito: cuanto más se copia, más envejece.
DEPENDENCIAS = ("estado", "admision", "gobierno", "identidad")

# Ficheros de este paquete que se instalan. Se DERIVAN del disco para que un módulo nuevo no
# se quede fuera por olvido, y se excluye lo que no es código ni dato.
EXCLUIDOS = ("__pycache__",)


def _dentro(candidata, arbol):
    return candidata == arbol or candidata.startswith(arbol + os.sep)


def _resolver_por_el_directorio(ruta):
    absoluta = os.path.abspath(ruta)
    directorio = os.path.dirname(absoluta) or "."
    return os.path.join(os.path.realpath(directorio), os.path.basename(absoluta))


def exigir_fuera_del_arbol(destino, arbol_verificado):
    """`g.15`: la raíz externa no se instala dentro de lo que verifica. Dos caminos, uno basta."""
    arbol = os.path.realpath(arbol_verificado)
    por_directorio = _resolver_por_el_directorio(destino)
    del_fichero = os.path.realpath(destino)
    for candidata, causa in (
        (por_directorio, "la ruta declarada apunta dentro del árbol"),
        (del_fichero, "la ruta parece externa pero se resuelve DENTRO del árbol"),
    ):
        if _dentro(candidata, arbol):
            raise InstalacionDentroDelArbol(
                "la raíz externa no se puede instalar dentro del árbol que verifica: "
                + causa + ". Un verificador que vive donde vive lo verificado no es "
                "externo",
                ruta=os.path.basename(candidata),
            )
    return del_fichero


def _digest(ruta):
    resumen = hashlib.sha256()
    with open(ruta, "rb") as manejador:
        for trozo in iter(lambda: manejador.read(65536), b""):
            resumen.update(trozo)
    return resumen.hexdigest()


def _copiar_arbol(origen, destino):
    shutil.copytree(
        origen, destino,
        ignore=shutil.ignore_patterns(*EXCLUIDOS),
        symlinks=False,
    )


def _inventariar(raiz):
    filas = []
    for carpeta, subcarpetas, ficheros in os.walk(raiz):
        subcarpetas[:] = sorted(s for s in subcarpetas if s not in EXCLUIDOS)
        for nombre in sorted(ficheros):
            completa = os.path.join(carpeta, nombre)
            relativa = os.path.relpath(completa, raiz).replace(os.sep, "/")
            if relativa == MANIFIESTO:
                continue
            filas.append({"ruta": relativa, "sha256": _digest(completa),
                          "bytes": os.path.getsize(completa)})
    filas.sort(key=lambda fila: fila["ruta"])
    return filas


def instalar(destino, *, arbol_verificado, runtime=None):
    """Copia el paquete y sus dependencias a `destino`, y escribe el manifiesto."""
    destino = exigir_fuera_del_arbol(destino, arbol_verificado)
    runtime = runtime or os.path.join(os.path.dirname(AQUI), "runtime")
    if os.path.exists(destino):
        shutil.rmtree(destino)
    os.makedirs(destino)

    _copiar_arbol(AQUI, os.path.join(destino, NOMBRE_DEL_PAQUETE))
    destino_runtime = os.path.join(destino, NOMBRE_DEL_RUNTIME)
    os.makedirs(destino_runtime)
    for paquete in DEPENDENCIAS:
        origen = os.path.join(runtime, paquete)
        if not os.path.isdir(origen):
            raise ErrorDeRaizExterna(
                "falta una dependencia del verificador en el árbol de origen: `"
                + paquete + "`. No se instala una raíz externa incompleta",
                ruta=paquete,
            )
        _copiar_arbol(origen, os.path.join(destino_runtime, paquete))

    for nombre in sorted(os.listdir(os.path.join(destino, NOMBRE_DEL_PAQUETE))):
        if nombre.endswith(".py"):
            os.chmod(os.path.join(destino, NOMBRE_DEL_PAQUETE, nombre), 0o755)

    manifiesto = {
        "esquema": 1,
        "tipo": "manifiesto-de-instalacion-de-raiz-externa",
        "paquete": NOMBRE_DEL_PAQUETE,
        "dependencias": list(DEPENDENCIAS),
        "ficheros": _inventariar(destino),
    }
    ruta_del_manifiesto = os.path.join(destino, MANIFIESTO)
    with open(ruta_del_manifiesto, "w", encoding="utf-8") as manejador:
        manejador.write(json.dumps(manifiesto, sort_keys=True, ensure_ascii=False,
                                   indent=2) + "\n")
    return {"destino": destino, "manifiesto": ruta_del_manifiesto,
            "verificador": os.path.join(destino, NOMBRE_DEL_PAQUETE, "verificador.py")}


def leer_manifiesto(destino):
    ruta = os.path.join(destino, MANIFIESTO)
    if not os.path.isfile(ruta):
        raise InstalacionAlterada(
            "la instalación no tiene manifiesto: sin él no se puede afirmar qué se está "
            "ejecutando", ruta=MANIFIESTO)
    with open(ruta, encoding="utf-8") as manejador:
        try:
            return json.load(manejador)
        except ValueError as exc:
            raise InstalacionAlterada(
                "el manifiesto de la instalación no es JSON válido", ruta=MANIFIESTO
            ) from exc


def verificar_instalacion(destino):
    """Recalcula TODOS los digests en el entorno externo. §11.8, verificación de hashes."""
    manifiesto = leer_manifiesto(destino)
    esperados = {fila["ruta"]: fila["sha256"] for fila in manifiesto["ficheros"]}
    reales = {fila["ruta"]: fila["sha256"] for fila in _inventariar(destino)}
    alteradas = sorted(ruta for ruta in set(esperados) & set(reales)
                       if esperados[ruta] != reales[ruta])
    ausentes = sorted(set(esperados) - set(reales))
    sobrantes = sorted(set(reales) - set(esperados))
    return {
        "alteradas": alteradas,
        "ausentes": ausentes,
        "sobrantes": sobrantes,
        "ok": not alteradas and not ausentes and not sobrantes,
    }


def exigir_instalacion_intacta(destino):
    """Fallo CERRADO: una instalación alterada NO emite veredicto."""
    informe = verificar_instalacion(destino)
    if not informe["ok"]:
        primera = (informe["alteradas"] or informe["ausentes"] or informe["sobrantes"])[0]
        raise InstalacionAlterada(
            "la instalación de la raíz externa no casa con su manifiesto: "
            + str(len(informe["alteradas"])) + " alteradas, "
            + str(len(informe["ausentes"])) + " ausentes, "
            + str(len(informe["sobrantes"])) + " sobrantes",
            ruta=primera,
        )
    return informe


def main(argv=None):
    analizador = argparse.ArgumentParser(
        prog="instalar", description="instala la raíz externa FUERA del árbol verificado")
    analizador.add_argument("--destino", required=True)
    analizador.add_argument("--arbol", required=True,
                            help="árbol verificado; el destino NO puede caer dentro")
    analizador.add_argument("--comprobar", action="store_true",
                            help="no instala: recalcula los digests de una instalación")
    argumentos = analizador.parse_args(argv)
    try:
        if argumentos.comprobar:
            informe = exigir_instalacion_intacta(argumentos.destino)
        else:
            informe = instalar(argumentos.destino,
                               arbol_verificado=argumentos.arbol)
    except ErrorDeRaizExterna as error:
        sys.stderr.write(str(error) + "\n")
        return 1
    salida = dict(informe)
    for clave in ("destino", "manifiesto", "verificador"):
        if clave in salida:
            salida[clave] = os.path.basename(salida[clave])
    sys.stdout.write(json.dumps(salida, sort_keys=True, ensure_ascii=False, indent=2)
                     + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
