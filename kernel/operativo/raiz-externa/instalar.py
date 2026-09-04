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

# ---------------------------------------------------------------------------
#  `ADJ-B2` · LA PURGA `E-10`, EN LA RAÍZ EXTERNA
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, sobre este mismo paquete. Con un `json.py` HOMÓNIMO
#  en `PYTHONPATH` y desde un `cwd` ajeno:
#
#      verificador.py capacidades            → {}   EXIT=0   (sano: las nueve condiciones)
#      instalar.py --destino … --arbol …     → {}   EXIT=0   manifiesto 3 BYTES (sano: 6734)
#                                                            y 41 ficheros instalados igual
#      … --comprobar sobre esa instalación   → KeyError: 'ficheros'  EXIT=1, cuatro rutas
#                                                            absolutas del anfitrión
#      grep de purga sobre TODO `raiz-externa/`                      CERO líneas
#
#  Es el MISMO defecto que el árbol declaraba cerrado para los cinco `ads_*.py`, vivo en la
#  única pieza que `O26` §1 juzga, e incumpliendo su condición 8 —«contaminación del entorno
#  falla cerrado»—, la única de las ocho que no se cumplía.
#
#  DECISIÓN · el prólogo se COPIA byte a byte, no se importa y no se adapta
#      Alternativas: (a) un módulo `procedencia.py` del paquete que los cuatro importen;
#      (b) una variante «para la raíz externa» del prólogo; (c) el MISMO prólogo, copiado.
#      Se elige (c), por dos razones y las dos se comprueban. (a) es la alternativa que el
#      propio `E-10` ya descartó: una guardia que necesita importar para poder purgar ya ha
#      perdido, porque el `import` es exactamente lo que está protegiendo. (b) produce dos
#      textos que divergen, y la divergencia se descubre el día que uno de los dos se queda
#      corto. Con (c) los NUEVE puntos ejecutables del árbol llevan el mismo texto y una
#      prueba lo comprueba por digest: si alguien toca uno, tiene que tocarlos todos.

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, sobre este mismo punto ejecutable: con
#  `PYTHONPATH=<dir>` apuntando a un directorio que contiene un `json.py` HOMÓNIMO, el
#  proceso IMPORTABA el homónimo. `sys.path[0]` —el directorio del script— protege a
#  `admision`, `estado` y `runtime`, que viven al lado; NO protege a la biblioteca estándar,
#  que va DESPUÉS de `PYTHONPATH`. Medido: `ads_admision.py --repo <dir> verificar --json`
#  publicaba `{}` como veredicto y terminaba con código 0, y los cinco `ads_*.py` importaban
#  el módulo envenenado.
#
#  DECISIÓN · la purga es lo PRIMERO del fichero y sólo usa `sys` y `os`
#      Alternativas: (a) purgar después de los imports normales; (b) purgar en un módulo
#      aparte e importarlo; (c) purgar aquí, con lo único que el intérprete ya ha cargado.
#      Se elige (c). Con (a) la purga llega tarde: el homónimo ya está en `sys.modules`. Con
#      (b) la purga depende de un `import` que es exactamente lo que se está protegiendo —una
#      guardia que necesita importar ya ha perdido—. `sys` es un módulo incorporado y `os` lo
#      carga el arranque del intérprete, así que los dos vienen de `sys.modules` y no de la
#      ruta de importación. Que `os` sea el bueno se COMPRUEBA, no se supone.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación
#      distinta y convertiría un fallo de entorno en un fallo del aparato. Lo que `E-10`
#      nombra es concreto: `PYTHONPATH` y el `cwd`. Se retiran ésos, se cuenta cuántos, y el
#      recuento se PUBLICA en la procedencia.
import sys as _sys
import os as _os

_RAIZ_DEL_APARATO = _os.path.dirname(_os.path.abspath(__file__))


def _entradas_del_lanzador():
    """Lo que el LANZADOR puede meter en la ruta de importación: `PYTHONPATH` y el `cwd`."""
    sospechosas = set()
    for entrada in (_os.environ.get("PYTHONPATH") or "").split(_os.pathsep):
        if entrada:
            sospechosas.add(_os.path.realpath(entrada))
    try:
        sospechosas.add(_os.path.realpath(_os.getcwd()))
    except OSError:
        # Un `cwd` borrado bajo los pies no es motivo para no purgar el resto.
        pass
    return sospechosas


def _purgar_la_ruta_de_importacion():
    """Retira de `sys.path` lo que venga del lanzador. Devuelve cuántas entradas retiró."""
    del_lanzador = _entradas_del_lanzador()
    propia = _os.path.realpath(_RAIZ_DEL_APARATO)
    conservadas, retiradas = [], []
    for entrada in _sys.path:
        try:
            real = _os.path.realpath(entrada or _os.getcwd())
        except OSError:
            conservadas.append(entrada)
            continue
        if real != propia and real in del_lanzador:
            retiradas.append(real)
        else:
            conservadas.append(entrada)
    _sys.path[:] = conservadas
    return retiradas


RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()

# CONTROL DEL CONTROL de la purga: `os` se usa para poder purgar, así que si `os` mismo
# viniera del lanzador la purga no probaría nada. No hay forma honesta de seguir: se dice y
# se sale con el código de PROCEDENCIA.
if _os.path.realpath(_os.path.dirname(_os.__file__ or ".")) in _entradas_del_lanzador():
    _sys.stderr.write(
        "[PROCEDENCIA_NO_FIABLE] el módulo `os` procede de la ruta de importación del "
        "lanzador: este punto ejecutable no puede garantizar de dónde salen sus módulos y "
        "NO ejecuta\n")
    raise SystemExit(5)

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


# ---------------------------------------------------------------------------
#  `ADJ-B2` · NO SE INSTALA A MEDIAS
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO: `instalar()` empezaba por `shutil.rmtree(destino)` y copiaba encima.
#  Una dependencia que faltara —o cualquier fallo a mitad de copia— dejaba en el destino un
#  árbol con parte de los ficheros y SIN manifiesto, es decir, una instalación que no se
#  puede comprobar y que aun así está ahí para que alguien la ejecute. Y con el entorno
#  contaminado el manifiesto salía de TRES bytes sobre 41 ficheros instalados: 41 ficheros
#  con código 0 y nada que los cubriera.
#
#  DECISIÓN · se construye en una zona APARTE y se publica por RENOMBRADO
#      Alternativas: (a) copiar sobre el destino y borrarlo si algo falla; (b) construir en
#      una zona aparte, renombrar la anterior, publicar la nueva y borrar la anterior.
#      Se elige (b). Con (a) el destino pasa por un estado incompleto que es observable —y
#      ejecutable— mientras dura la copia, y si el proceso muere ahí no queda nadie para
#      borrarlo. Con (b) el destino nunca contiene una instalación a medias: o la anterior
#      entera, o la nueva entera. `os.rename` dentro del mismo directorio padre es atómico
#      en POSIX, y ésa es toda la garantía que hace falta.
#      Lo que NO se promete: que el borrado de la anterior sobreviva a un corte. Puede
#      quedar `<destino>.anterior`, que es basura nombrada y no una instalación: no lleva
#      el nombre que nadie ejecuta ni el que el manifiesto cubre.
SUFIJO_EN_CURSO = ".en-curso"
SUFIJO_ANTERIOR = ".anterior"


def _publicable(nombre):
    """`True` si el fichero es un PUNTO EJECUTABLE: lleva línea de intérprete.

    Es el mismo criterio que la prueba `T330` deriva del disco para saber a quién exigirle
    la purga `E-10`. Aquí decide a quién se le dan permisos de ejecución: antes se daban a
    TODO `.py` del paquete, y con eso un módulo que no es un punto ejecutable acababa
    presentándose como si lo fuera.
    """
    try:
        with open(nombre, "rb") as manejador:
            return manejador.read(2) == b"#!"
    except OSError:
        return False


def _construir(destino, *, runtime):
    """Deja la instalación COMPLETA en `destino`, que aquí es siempre la zona en curso."""
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

    paquete_instalado = os.path.join(destino, NOMBRE_DEL_PAQUETE)
    for nombre in sorted(os.listdir(paquete_instalado)):
        completa = os.path.join(paquete_instalado, nombre)
        if nombre.endswith(".py") and _publicable(completa):
            os.chmod(completa, 0o755)

    filas = _inventariar(destino)
    if not filas:
        raise ErrorDeRaizExterna(
            "el inventario de la instalación salió VACÍO con ficheros en el destino: el "
            "manifiesto no cubriría nada de lo instalado, y una instalación sin manifiesto "
            "efectivo no se puede comprobar",
            ruta=MANIFIESTO,
        )
    manifiesto = {
        "esquema": 1,
        "tipo": "manifiesto-de-instalacion-de-raiz-externa",
        "paquete": NOMBRE_DEL_PAQUETE,
        "dependencias": list(DEPENDENCIAS),
        "ficheros": filas,
    }
    texto = json.dumps(manifiesto, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
    # CONTROL DEL CONTROL del serializador, por la misma razón que en `verificador.py`: un
    # `json.dumps` sustituido publicaba un manifiesto de tres bytes sobre 41 ficheros.
    comprobado = json.loads(texto) if texto.strip() else {}
    if len(comprobado.get("ficheros") or ()) != len(filas):
        raise ErrorDeRaizExterna(
            "el manifiesto serializado no reproduce las " + str(len(filas)) + " filas "
            "inventariadas: lo que se escribiría no describe lo que se ha instalado",
            ruta=MANIFIESTO,
        )
    ruta_del_manifiesto = os.path.join(destino, MANIFIESTO)
    with open(ruta_del_manifiesto, "w", encoding="utf-8") as manejador:
        manejador.write(texto)
    return ruta_del_manifiesto


def instalar(destino, *, arbol_verificado, runtime=None):
    """Copia el paquete y sus dependencias a `destino`, y escribe el manifiesto.

    O deja la instalación ENTERA, o no deja ninguna: nunca una a medias.
    """
    destino = exigir_fuera_del_arbol(destino, arbol_verificado)
    runtime = runtime or os.path.join(os.path.dirname(AQUI), "runtime")
    en_curso = destino + SUFIJO_EN_CURSO
    anterior = destino + SUFIJO_ANTERIOR
    for residuo in (en_curso, anterior):
        if os.path.exists(residuo):
            shutil.rmtree(residuo)
    try:
        _construir(en_curso, runtime=runtime)
    except BaseException:
        # Ni un fichero del intento fallido queda en pie, y el destino ANTERIOR sigue
        # exactamente como estaba: no se ha tocado todavía.
        shutil.rmtree(en_curso, ignore_errors=True)
        raise
    habia = os.path.exists(destino)
    if habia:
        os.rename(destino, anterior)
    try:
        os.rename(en_curso, destino)
    except OSError:
        if habia:
            os.rename(anterior, destino)
        shutil.rmtree(en_curso, ignore_errors=True)
        raise
    if habia:
        shutil.rmtree(anterior, ignore_errors=True)
    return {"destino": destino,
            "manifiesto": os.path.join(destino, MANIFIESTO),
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


def exigir_manifiesto_bien_formado(manifiesto):
    """El manifiesto tiene la FORMA que `verificar_instalacion` va a leer, o falla TIPADO.

    HECHO REPRODUCIDO (`ADJ-B2`): sobre una instalación cuyo manifiesto se escribió con el
    entorno contaminado —tres bytes, `{}`—, `--comprobar` moría con
    `KeyError: 'ficheros'`, traza y CUATRO rutas absolutas del anfitrión. Un manifiesto
    truncado no es un defecto de programación del comprobador: es exactamente la clase de
    instalación alterada que `V6-16` obliga a rechazar, y como tal se declara.
    """
    if not isinstance(manifiesto, dict):
        raise InstalacionAlterada(
            "el manifiesto de la instalación no es un objeto JSON", ruta=MANIFIESTO)
    filas = manifiesto.get("ficheros")
    if not isinstance(filas, list) or not filas:
        raise InstalacionAlterada(
            "el manifiesto de la instalación no lleva la lista `ficheros`, o la lleva "
            "vacía: sin ella no cubre NADA de lo instalado y no se puede afirmar qué se "
            "está ejecutando",
            ruta=MANIFIESTO)
    for indice, fila in enumerate(filas):
        if not isinstance(fila, dict) or not isinstance(fila.get("ruta"), str) \
                or not isinstance(fila.get("sha256"), str):
            raise InstalacionAlterada(
                "la fila " + str(indice) + " del manifiesto no declara `ruta` y `sha256`",
                ruta=MANIFIESTO)
    return filas


def verificar_instalacion(destino):
    """Recalcula TODOS los digests en el entorno externo. §11.8, verificación de hashes."""
    manifiesto = leer_manifiesto(destino)
    esperados = {fila["ruta"]: fila["sha256"]
                 for fila in exigir_manifiesto_bien_formado(manifiesto)}
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


# ---------------------------------------------------------------------------
#  `E-10` · la PROCEDENCIA se PUBLICA también aquí
# ---------------------------------------------------------------------------
#  El instalador es el punto ejecutable que CONSTRUYE la instalación autorizada. Si sus
#  módulos no salen de este paquete, lo que construya no es la raíz externa de nadie.
MODULOS_DEL_APARATO = ("errores",)

CODIGO_DE_PROCEDENCIA = 5


def _origen_de(fichero):
    """Nunca una ruta absoluta del anfitrión: la evidencia se publica (`E-15`)."""
    if not fichero:
        return "(sin fichero)"
    real = os.path.realpath(fichero)
    propia = os.path.realpath(_RAIZ_DEL_APARATO)
    if real == propia or real.startswith(propia + os.sep):
        return "aparato:" + os.path.relpath(real, propia)
    return "FUERA-DEL-APARATO:" + os.path.basename(real)


def procedencia():
    modulos = {}
    for nombre in MODULOS_DEL_APARATO:
        modulo = sys.modules.get(nombre)
        modulos[nombre] = _origen_de(getattr(modulo, "__file__", None))
    return {
        "aparato": os.path.basename(_RAIZ_DEL_APARATO),
        "modulos": modulos,
        "entradas_del_lanzador_retiradas": len(RETIRADAS_DE_LA_RUTA),
    }


def exigir_procedencia_del_aparato():
    """FALLO CERRADO si un módulo del aparato no sale del aparato. `E-10`."""
    intrusos = {nombre: origen for nombre, origen in procedencia()["modulos"].items()
                if origen.startswith("FUERA-DEL-APARATO") or origen == "(sin fichero)"}
    if intrusos:
        sys.stderr.write(
            "[PROCEDENCIA_NO_FIABLE] módulos del instalador importados desde fuera del "
            "paquete: " + ", ".join(sorted(intrusos)) + ". Lo que construyera este proceso "
            "no sería la raíz externa de este árbol, y NO se construye\n")
        return CODIGO_DE_PROCEDENCIA
    return None


def _volcar(objeto):
    """JSON determinista, con el mismo CONTROL DEL CONTROL que `verificador.py`.

    Publicar `{}` con código 0 era la mitad visible de `ADJ-B2`: la orden decía que todo
    había ido bien y no decía qué había hecho.
    """
    texto = json.dumps(objeto, sort_keys=True, ensure_ascii=False, indent=2)
    if objeto and texto.strip() in ("{}", "[]", "null", '""'):
        sys.stderr.write(
            "[PROCEDENCIA_NO_FIABLE] el serializador JSON de este proceso devuelve el "
            "vacío para un objeto que no lo está: lo que se publicaría no es la salida de "
            "este instalador, y NO se publica\n")
        raise SystemExit(CODIGO_DE_PROCEDENCIA)
    return texto


def main(argv=None):
    analizador = argparse.ArgumentParser(
        prog="instalar", description="instala la raíz externa FUERA del árbol verificado")
    analizador.add_argument("--destino", required=True)
    analizador.add_argument("--arbol", required=True,
                            help="árbol verificado; el destino NO puede caer dentro")
    analizador.add_argument("--comprobar", action="store_true",
                            help="no instala: recalcula los digests de una instalación")
    analizador.add_argument("--procedencia", action="store_true",
                            help="no instala: publica de dónde sale el código que instala")
    argumentos = analizador.parse_args(argv)
    # `E-10` · antes de copiar un solo byte, de dónde ha salido lo que va a copiar.
    intruso = exigir_procedencia_del_aparato()
    if intruso is not None:
        return intruso
    if argumentos.procedencia:
        sys.stdout.write(_volcar(procedencia()) + "\n")
        return 0
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
    salida["procedencia"] = procedencia()
    sys.stdout.write(_volcar(salida) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
