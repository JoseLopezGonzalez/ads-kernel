#!/usr/bin/env python3
"""formulas — SEDE ÚNICA de las fórmulas compartidas del aparato, y su censo DERIVADO.

Instancia `V6-19` de `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` §20.1: *cada fórmula
compartida por varios instrumentos tiene UNA SOLA SEDE, y sus consumidores la IMPORTAN en
vez de reescribirla*. El criterio de cierre de esa fila tiene tres mitades y las tres viven
aquí:

  1 · las fórmulas, escritas UNA vez
  2 · el censo, **derivado del código con `ast`** y no escrito a mano, que denuncia una
      SEGUNDA definición aunque hoy coincida con la sede
  3 · `exigir_sede()`: si la importación de la sede falla, el instrumento **NO emite**

DECISIÓN · el censo se deriva con `ast`, nunca con `grep`
    Alternativas: (a) `grep` de un patrón textual; (b) árbol sintáctico.
    Se elige (b). `grep` no distingue una definición de una mención en un comentario, no ve
    la forma equivalente escrita de otra manera —`len(x.splitlines())` frente a
    `x.count(b"\\n")`— y se puede burlar partiendo la cadena en dos. Con `ast` lo que se
    reconoce es la OPERACIÓN, no su ortografía, y la firma de detección de cada fórmula está
    escrita como código y no como expresión regular.

DECISIÓN · las firmas de detección describen la OPERACIÓN, no el nombre de la función
    Un censo que buscara funciones llamadas `contar_lineas` lo esquivaría cualquiera que la
    llamase `_n`. Lo que se detecta es el cálculo: contar separadores de línea, calcular un
    digest de contenido, o desmontar un documento de datos indentado. El nombre no importa.

DECISIÓN · tres fórmulas censadas, y se dice por qué son TRES
    §20.1 nombra explícitamente una —«hoy, la del recuento de líneas de un blob»— y dice
    «hoy», luego el conjunto crece. Las otras dos entran porque MÁS DE UN instrumento de
    este corte las necesita y ya habían empezado a duplicarse: el digest de contenido lo
    quieren el gobierno Git, el perímetro, la proyección de adaptadores y la identidad; y la
    lectura del subconjunto de datos indentado la quieren el censo de zonas
    (`FUENTES-CANONICAS.yml`) y la tabla de propiedad (`POLITICA-CONTROL-REPO.yml`). Dos
    lectores del mismo formato eran ya la segunda sede que `V6-19` prohíbe.

DECISIÓN · no se usa PyYAML, y no se implementa YAML
    El entorno sólo admite biblioteca estándar. Se implementa un lector ESTRICTO de un
    SUBCONJUNTO declarado, que falla cerrado ante cualquier construcción que no reconoce.
    La alternativa —aceptar «lo que se pueda» y seguir— es la que `V6-03` prohíbe: una
    estructura ajena tiene que producir diagnóstico, no una lectura a medias.
"""
from __future__ import annotations

import ast
import hashlib
import os
import re

from .errores import CensoDeFormulasSucio, DatoIlegible, SedeDeFormulaAusente

# El nombre de este módulo, tal y como lo ve el censo. Se deriva del fichero y no se escribe
# dos veces: si alguien renombra el módulo, la sede se mueve con él.
SEDE = os.path.basename(__file__)


# ===========================================================================
#  FÓRMULA 1 · recuento de líneas de un blob   (la que §20.1 nombra)
# ===========================================================================
def contar_lineas_de_blob(datos):
    """Líneas de un blob, con los DOS casos frontera que `V6-19` exige por su nombre.

    Definición: una línea es una secuencia de bytes terminada por `\\n`, más una última
    línea si quedan bytes sin terminador.

        b""            → 0     el fichero VACÍO no tiene ninguna línea
        b"a"           → 1     no termina en salto de línea, y aun así ES una línea
        b"a\\n"         → 1
        b"a\\n\\n"       → 2     una línea vacía es una línea
        b"a\\nb"        → 2

    El defecto que previene: `datos.count(b"\\n")` da 0 para `b"a"` y `len(splitlines())` da
    1 para `b"a\\n"` y 1 para `b"a"`, de modo que dos instrumentos que «cuentan líneas» se
    contradicen justo en los dos casos frontera. Que la contradicción no exista es lo que
    `V6-19` mide, y la única manera de garantizarla es que haya UNA definición.
    """
    if isinstance(datos, str):
        datos = datos.encode("utf-8")
    if not isinstance(datos, (bytes, bytearray)):
        raise CensoDeFormulasSucio(
            "el recuento de líneas se calcula sobre bytes, no sobre "
            + type(datos).__name__
        )
    datos = bytes(datos)
    if not datos:
        return 0
    completas = datos.count(b"\n")
    return completas if datos.endswith(b"\n") else completas + 1


# ===========================================================================
#  FÓRMULA 2 · digest de contenido
# ===========================================================================
DOMINIO_CONTENIDO = b"ads.admision/contenido\x00"


def digest_de_contenido(datos):
    """SHA-256 con separación de dominio, en hexadecimal.

    La separación de dominio no es adorno: sin ella, el digest de un contenido y el digest
    de una estructura serializada que casualmente tuviera los mismos bytes serían el mismo
    valor, y un instrumento podría presentar el uno como prueba del otro.
    """
    if isinstance(datos, str):
        datos = datos.encode("utf-8")
    if not isinstance(datos, (bytes, bytearray)):
        raise CensoDeFormulasSucio(
            "el digest se calcula sobre bytes, no sobre " + type(datos).__name__
        )
    return hashlib.sha256(DOMINIO_CONTENIDO + bytes(datos)).hexdigest()


def digest_de_lista(valores):
    """Digest de una lista de cadenas, estable frente al orden de llegada."""
    cuerpo = "\n".join(sorted(str(valor) for valor in valores))
    return digest_de_contenido(cuerpo)


# ===========================================================================
#  FÓRMULA 3 · lectura del SUBCONJUNTO de datos indentado
# ===========================================================================
#  Lo que ADMITE, y nada más:
#     · mapas `clave: valor` anidados por indentación de dos espacios o más
#     · secuencias `- ` de mapas y de escalares
#     · escalares planos, entre comillas simples y entre comillas dobles
#     · bloques `>` (plegado) y `|` (literal)
#     · listas en línea `[a, b, c]`
#     · comentarios `#` fuera de comillas, y líneas en blanco
#  Cualquier otra cosa —anclas, alias, etiquetas, documentos múltiples, mapas en línea—
#  produce `DatoIlegible` y NO una lectura parcial.

_COMILLAS = ("'", '"')
_ENTERO = re.compile(r"^-?(0|[1-9][0-9]*)$")


def _quitar_comentario(linea):
    """Recorta el comentario respetando las comillas. Un `#` dentro de un escalar no lo es."""
    dentro = ""
    for indice, caracter in enumerate(linea):
        if dentro:
            if caracter == dentro:
                dentro = ""
        elif caracter in _COMILLAS:
            dentro = caracter
        elif caracter == "#" and (indice == 0 or linea[indice - 1] in " \t"):
            return linea[:indice].rstrip()
    return linea.rstrip()


def _escalar(texto, ruta):
    texto = texto.strip()
    if not texto:
        return ""
    if texto[0] in _COMILLAS:
        if len(texto) < 2 or texto[-1] != texto[0]:
            raise DatoIlegible("escalar entrecomillado sin cerrar: " + texto, ruta=ruta)
        return texto[1:-1]
    if texto.startswith("[") and texto.endswith("]"):
        interior = texto[1:-1].strip()
        if not interior:
            return []
        return [_escalar(parte, ruta) for parte in interior.split(",")]
    if texto in ("true", "false"):
        return texto == "true"
    if texto == "null":
        return None
    # Se convierte a entero SÓLO lo que es inequívocamente un número escrito como número.
    # Defecto que previene: un digest o un SHA de sólo dígitos —`0000…0` es el caso más
    # común, el valor nulo de una ref— se convertía en el entero `0` y dejaba de casar con
    # la cadena que lo declaró. Un identificador con ceros a la izquierda NO es un número.
    if _ENTERO.match(texto) and len(texto) <= 18:
        return int(texto)
    return texto


_CLAVE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*\s*:(\s|$)")


def _parece_clave(contenido):
    """¿Esta línea abre una clave, o continúa el escalar de la anterior?

    Defecto que previene: el corpus escribe escalares planos partidos en varias líneas
    —`materia:` de `MAT-048`, por ejemplo—. Leerlas como claves nuevas hacía que el lector
    fallara sobre el registro canónico real, y aceptar «lo que se pueda» habría sido la
    lectura a medias que `V6-03` prohíbe. Se reconoce la CONTINUACIÓN explícitamente.
    """
    return bool(_CLAVE.match(contenido)) or contenido.startswith("- ")


def _lineas_utiles(texto, ruta):
    """(indentación, contenido, número) de cada línea con contenido, ya sin comentarios."""
    salida = []
    for numero, cruda in enumerate(texto.splitlines(), start=1):
        if cruda.strip().startswith("#"):
            continue
        limpia = _quitar_comentario(cruda)
        if not limpia.strip():
            continue
        if "\t" in limpia[: len(limpia) - len(limpia.lstrip())]:
            raise DatoIlegible(
                "indentación con tabulador en la línea " + str(numero), ruta=ruta
            )
        salida.append((len(limpia) - len(limpia.lstrip()), limpia.strip(), numero))
    return salida


def _bloque_plegado(texto, ruta, desde, indentacion, plegar):
    """Recoge un bloque `>` o `|`, que se corta por indentación y NO por línea en blanco."""
    partes = []
    lineas = texto.splitlines()
    indice = desde
    while indice < len(lineas):
        cruda = lineas[indice]
        if not cruda.strip():
            partes.append("")
            indice += 1
            continue
        actual = len(cruda) - len(cruda.lstrip())
        if actual <= indentacion:
            break
        partes.append(cruda[indentacion + 1:].rstrip())
        indice += 1
    while partes and not partes[-1]:
        partes.pop()
    if plegar:
        return " ".join(parte.strip() for parte in partes if parte.strip())
    return "\n".join(partes)


def leer_datos_indentados(texto, ruta=None):
    """Lector ESTRICTO del subconjunto declarado. Falla cerrado, nunca a medias."""
    if not isinstance(texto, str):
        raise DatoIlegible("el documento de datos se lee como texto ya decodificado", ruta=ruta)
    if "\n---\n" in texto or texto.startswith("---\n"):
        raise DatoIlegible("documentos múltiples: fuera del subconjunto admitido", ruta=ruta)
    for prohibido, motivo in ((" &", "anclas"), (" *", "alias"), (" !!", "etiquetas")):
        for linea in texto.splitlines():
            recorte = _quitar_comentario(linea)
            if ": " + prohibido.strip() in recorte and not recorte.strip().startswith("#"):
                raise DatoIlegible(
                    motivo + ": fuera del subconjunto admitido", ruta=ruta
                )
    crudas = texto.splitlines()
    utiles = _lineas_utiles(texto, ruta)
    return _construir(utiles, 0, len(utiles), crudas, texto, ruta)[0]


def _construir(utiles, inicio, fin, crudas, texto, ruta):
    if inicio >= fin:
        return {}, inicio
    if utiles[inicio][1].startswith("- "):
        return _construir_lista(utiles, inicio, fin, crudas, texto, ruta)
    return _construir_mapa(utiles, inicio, fin, crudas, texto, ruta)


def _construir_mapa(utiles, inicio, fin, crudas, texto, ruta):
    mapa = {}
    base = utiles[inicio][0]
    indice = inicio
    while indice < fin:
        indentacion, contenido, numero = utiles[indice]
        if indentacion < base:
            break
        if indentacion > base:
            raise DatoIlegible(
                "indentación inesperada en la línea " + str(numero), ruta=ruta
            )
        if ":" not in contenido:
            raise DatoIlegible(
                "se esperaba `clave: valor` en la línea " + str(numero), ruta=ruta
            )
        clave, _, resto = contenido.partition(":")
        clave = clave.strip()
        resto = resto.strip()
        if not clave:
            raise DatoIlegible("clave vacía en la línea " + str(numero), ruta=ruta)
        if resto in (">", "|", ">-", "|-"):
            mapa[clave] = _bloque_plegado(
                texto, ruta, numero, indentacion, resto[0] == ">"
            )
            indice += 1
            while indice < fin and utiles[indice][0] > indentacion:
                indice += 1
            continue
        if resto:
            partes = [resto]
            avance = indice + 1
            while (avance < fin and utiles[avance][0] > indentacion
                   and not _parece_clave(utiles[avance][1])):
                partes.append(utiles[avance][1])
                avance += 1
            if len(partes) == 1:
                mapa[clave] = _escalar(resto, ruta)
            else:
                mapa[clave] = " ".join(partes)
            indice = avance
            continue
        siguiente = indice + 1
        if siguiente >= fin or utiles[siguiente][0] <= indentacion:
            mapa[clave] = None
            indice = siguiente
            continue
        limite = siguiente
        while limite < fin and utiles[limite][0] > indentacion:
            limite += 1
        mapa[clave], _ = _construir(utiles, siguiente, limite, crudas, texto, ruta)
        indice = limite
    return mapa, indice


def _construir_lista(utiles, inicio, fin, crudas, texto, ruta):
    lista = []
    base = utiles[inicio][0]
    indice = inicio
    while indice < fin:
        indentacion, contenido, numero = utiles[indice]
        if indentacion < base:
            break
        if indentacion > base or not contenido.startswith("- "):
            raise DatoIlegible(
                "elemento de secuencia mal formado en la línea " + str(numero), ruta=ruta
            )
        cabeza = contenido[2:].strip()
        limite = indice + 1
        while limite < fin and utiles[limite][0] > base:
            limite += 1
        if ":" in cabeza and not cabeza.startswith(tuple(_COMILLAS)):
            # Elemento que ES un mapa: su primera clave viene en la propia línea del guion.
            sintetico = [(base + 2, cabeza, numero)] + list(utiles[indice + 1:limite])
            elemento, _ = _construir_mapa(sintetico, 0, len(sintetico), crudas, texto, ruta)
            lista.append(elemento)
        elif limite > indice + 1:
            raise DatoIlegible(
                "elemento de secuencia con hijos pero sin clave, línea " + str(numero),
                ruta=ruta,
            )
        else:
            lista.append(_escalar(cabeza, ruta))
        indice = limite
    return lista, indice


def leer_fichero_de_datos(ruta):
    """Lee y desmonta un documento de datos del corpus. Cierra el fichero SIEMPRE."""
    try:
        with open(ruta, "rb") as manejador:
            crudo = manejador.read()
    except OSError as exc:
        raise DatoIlegible("no se pudo leer el documento de datos: " + exc.strerror,
                           ruta=ruta) from exc
    try:
        texto = crudo.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise DatoIlegible(
            "el documento de datos no es UTF-8 válido en el byte " + str(exc.start),
            ruta=ruta,
        ) from exc
    return leer_datos_indentados(texto, ruta=ruta)


# ===========================================================================
#  CENSO DERIVADO de las fórmulas · `V6-19`
# ===========================================================================
#  Cada entrada declara: el identificador de la fórmula, su sede única, la función que la
#  encarna y la FIRMA DE DETECCIÓN, que es un invocable sobre un nodo `ast`.

def _es_recuento_de_lineas(nodo):
    """`x.count("\\n")`, `len(x.splitlines())` o `len(x.split("\\n"))`."""
    if isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Attribute):
        if nodo.func.attr == "count" and len(nodo.args) == 1:
            argumento = nodo.args[0]
            if isinstance(argumento, ast.Constant) and argumento.value in ("\n", b"\n"):
                return True
    if (isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Name)
            and nodo.func.id == "len" and len(nodo.args) == 1):
        interior = nodo.args[0]
        if isinstance(interior, ast.Call) and isinstance(interior.func, ast.Attribute):
            if interior.func.attr == "splitlines":
                return True
            if interior.func.attr == "split" and len(interior.args) == 1:
                argumento = interior.args[0]
                if isinstance(argumento, ast.Constant) and argumento.value in ("\n", b"\n"):
                    return True
    return False


def _es_digest_de_contenido(nodo):
    """Cualquier llamada a `hashlib.sha256` / `sha512` / `blake2b` fuera de la sede."""
    if isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Attribute):
        if nodo.func.attr in ("sha256", "sha512", "blake2b", "md5", "sha1"):
            raiz = nodo.func.value
            if isinstance(raiz, ast.Name) and raiz.id == "hashlib":
                return True
    return False


def _es_lector_de_datos(nodo):
    """Una función que a la vez trocea por líneas y parte por `:`. Es un lector de datos."""
    if not isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return False
    por_lineas = False
    por_dos_puntos = False
    for hijo in ast.walk(nodo):
        if isinstance(hijo, ast.Call) and isinstance(hijo.func, ast.Attribute):
            if hijo.func.attr in ("splitlines", "readlines"):
                por_lineas = True
            if hijo.func.attr in ("split", "partition") and hijo.args:
                argumento = hijo.args[0]
                if isinstance(argumento, ast.Constant) and argumento.value == ":":
                    por_dos_puntos = True
    return por_lineas and por_dos_puntos


FORMULAS_CENSADAS = (
    {
        "formula": "recuento-de-lineas-de-un-blob",
        "sede": SEDE,
        "funcion": "contar_lineas_de_blob",
        "firma": _es_recuento_de_lineas,
        "fuente": "11-ARQUITECTURA-INTEGRADA.md §20.1 fila `V6-19`, que la nombra",
    },
    {
        "formula": "digest-de-contenido",
        "sede": SEDE,
        "funcion": "digest_de_contenido",
        "firma": _es_digest_de_contenido,
        "fuente": "cuatro instrumentos de este corte la necesitan",
    },
    {
        "formula": "lectura-de-datos-indentados",
        "sede": SEDE,
        "funcion": "leer_datos_indentados",
        "firma": _es_lector_de_datos,
        "fuente": "el censo de zonas y la tabla de propiedad leen el mismo formato",
    },
)


def _arbol_de(ruta):
    try:
        with open(ruta, "rb") as manejador:
            fuente = manejador.read()
    except OSError as exc:
        raise CensoDeFormulasSucio(
            "no se pudo leer un módulo para censarlo: " + exc.strerror, ruta=ruta
        ) from exc
    try:
        return ast.parse(fuente, filename=os.path.basename(ruta))
    except SyntaxError as exc:
        raise CensoDeFormulasSucio(
            "un módulo del censo no es Python analizable: " + str(exc.msg), ruta=ruta
        ) from exc


def censar_formulas(rutas):
    """Censo DERIVADO. Devuelve `{formulas, definiciones, consumidores, ok}`.

    `definiciones` lista TODA aparición de una fórmula censada, con su módulo y su línea.
    Una que no esté en la sede es una SEGUNDA DEFINICIÓN, y el censo no está limpio.
    """
    definiciones = []
    consumidores = {}
    for ruta in sorted(rutas):
        modulo = os.path.basename(ruta)
        arbol = _arbol_de(ruta)
        importa_la_sede = False
        for nodo in ast.walk(arbol):
            if isinstance(nodo, ast.ImportFrom) and (nodo.module or "").endswith("formulas"):
                importa_la_sede = True
            if isinstance(nodo, ast.Import):
                for alias in nodo.names:
                    if alias.name.endswith("formulas"):
                        importa_la_sede = True
        consumidores[modulo] = importa_la_sede
        for nodo in ast.walk(arbol):
            for censada in FORMULAS_CENSADAS:
                if censada["firma"](nodo):
                    definiciones.append({
                        "formula": censada["formula"],
                        "modulo": modulo,
                        "linea": getattr(nodo, "lineno", 0),
                        "en_la_sede": modulo == censada["sede"],
                    })
    fuera = [entrada for entrada in definiciones if not entrada["en_la_sede"]]
    return {
        "formulas": [
            {"formula": c["formula"], "sede": c["sede"], "funcion": c["funcion"],
             "fuente": c["fuente"]}
            for c in FORMULAS_CENSADAS
        ],
        "definiciones": sorted(
            definiciones, key=lambda e: (e["formula"], e["modulo"], e["linea"])
        ),
        "segundas_definiciones": sorted(
            fuera, key=lambda e: (e["formula"], e["modulo"], e["linea"])
        ),
        "consumidores": {m: consumidores[m] for m in sorted(consumidores)},
        "ok": not fuera,
    }


def exigir_sede():
    """`V6-19`: si la importación de la sede falla, el instrumento NO emite.

    No calcula «una suya equivalente» y no degrada a un valor por defecto: levanta
    `SedeDeFormulaAusente` y quien la llame deja de emitir veredicto.
    """
    faltan = []
    for censada in FORMULAS_CENSADAS:
        funcion = globals().get(censada["funcion"])
        if not callable(funcion):
            faltan.append(censada["formula"])
    if faltan:
        raise SedeDeFormulaAusente(
            "la sede de fórmulas compartidas no ofrece " + ", ".join(sorted(faltan))
            + "; el instrumento no emite veredicto con una fórmula propia"
        )
    # Contrato de los dos casos frontera que `V6-19` exige por su nombre. Si la sede
    # importada no los cumple, no es la sede: es otra cosa con el mismo nombre.
    if contar_lineas_de_blob(b"") != 0 or contar_lineas_de_blob(b"a") != 1:
        raise SedeDeFormulaAusente(
            "la sede de fórmulas no respeta los casos frontera del fichero VACÍO y del "
            "fichero que no termina en salto de línea"
        )
    return True
