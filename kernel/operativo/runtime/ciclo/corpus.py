#!/usr/bin/env python3
"""corpus — el CICLO lee el corpus canónico del kernel, y lo lee con la stdlib.

El ciclo del `§7.2` no puede tener una copia de `b.16` escrita a mano: la ruta se COMPONE
desde `kernel/operativo/recorrido/01-PROCESOS.md`, los gates desde donde el corpus los
declara, los handoffs desde `kernel/operativo/circuitos/` y los equipos desde
`kernel/operativo/capacidades/<CAP>/composicion.md`. Este módulo es esa lectura, y nada
más: no interpreta, no decide y no escribe.

DECISIÓN · analizador YAML ACOTADO propio, y no PyYAML
    Alternativas: (a) `import yaml`, que los validadores ya usan; (b) escribir aquí un
    analizador del subconjunto que el corpus usa de verdad.
    Se elige (b), y cuesta ciento y pico líneas. La razón no es purismo: `estado/`,
    `runtime/`, `gobierno/`, `admision/`, `adaptadores/` e `identidad/` son **stdlib pura**,
    y ese directorio VIAJA a cada proyecto instalado. Meter PyYAML aquí convierte una
    dependencia de las herramientas de desarrollo —los validadores corren en el repositorio
    del kernel— en una dependencia del RUNTIME de todo producto gobernado. Un proyecto
    instalado que no pueda componer una ruta porque falta un paquete de terceros es un modo
    de fallo nuevo, y no lo pide ninguna norma.
    Lo que (b) cuesta se paga en la prueba: `test_ciclo.py` compara este analizador contra
    PyYAML **bloque a bloque sobre el corpus real** cuando PyYAML está disponible, de modo
    que la equivalencia se comprueba y no se promete.

DECISIÓN · el subconjunto es CERRADO y todo lo demás FALLA
    No hay «lo que no entienda, que lo ignore». Anclas, alias, etiquetas, documentos
    múltiples, claves complejas y tabuladores levantan `CorpusIlegible` con la línea. Un
    analizador que ignora lo que no entiende devuelve una ruta compuesta a partir de un
    proceso leído a medias, y eso es exactamente inventar estado.

DECISIÓN · la raíz del kernel se DERIVA de `__file__` y NUNCA del `cwd`
    Es la misma regla que las baterías del repositorio ya aplican. Dos ejecuciones desde
    directorios distintos deben leer el mismo corpus y producir los mismos bytes (`I-g3`).
    El constructor admite una raíz explícita para que un producto instalado, cuyo kernel
    está en otro sitio, pueda decirlo; lo que no hay es un valor por defecto que dependa de
    dónde se invocó.

DECISIÓN · el corpus se lee UNA VEZ por objeto `Corpus` y se conserva en memoria
    No es una caché de estado: el corpus es NORMA en el árbol de ficheros, no estado del
    producto, y no cambia mientras el proceso corre. Releerlo en cada consulta multiplicaría
    por veinte la lectura de ciento y pico ficheros sin cambiar ninguna respuesta. La huella
    (`huella()`) se calcula sobre lo leído, y es lo que hace que un corpus distinto sea un
    sujeto distinto en la `FASE 0` de `§9.6`.
"""
from __future__ import annotations

import hashlib
import os
import re

from .errores import CorpusIlegible, CorpusIncompleto

# ---------------------------------------------------------------------- forma
APERTURA = re.compile(r"^```yaml\s+ads:([a-z-]+)\s*$")
CIERRE = re.compile(r"^```\s*$")

# Las QUINCE capacidades de `§18`. Se escriben aquí para CONFRONTAR el árbol de
# `capacidades/`, no para sustituirlo: `Corpus.capacidades()` lee el árbol y
# `exigir_quince()` comprueba que coinciden. Dos sedes que se contrastan, no una copia.
CAPACIDADES = (
    "APR", "ARQ", "CON", "DIS", "DOM", "DSP", "ENC", "ENT", "INV", "PLT", "PRD", "SEG",
    "SIS", "USO", "VER",
)

# El vocabulario CERRADO de condiciones de la vía 3 (`§8.0`, `b.16`).
CONDICIONES_DE_B16 = ("C-DIS", "C-ARQ", "C-DOM", "C-SEG", "C-ENT", "C-USO", "C-APR")

RAIZ_POR_DEFECTO = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
)


# ===========================================================================
#  analizador YAML ACOTADO
# ===========================================================================
_ESCAPES = {"n": "\n", "t": "\t", "r": "\r", '"': '"', "\\": "\\", "/": "/", "0": "\0"}


def _sin_comentario(texto):
    """Recorta un comentario final. Sólo fuera de comillas, y sólo tras un espacio."""
    comilla = None
    for indice, caracter in enumerate(texto):
        if comilla:
            if caracter == comilla:
                comilla = None
            continue
        if caracter in ("'", '"'):
            comilla = caracter
            continue
        if caracter == "#" and (indice == 0 or texto[indice - 1] in (" ", "\t")):
            return texto[:indice].rstrip()
    return texto.rstrip()


def _escalar(texto, linea, ruta):
    """Un escalar simple: entre comillas, o plano con las conversiones de YAML 1.1."""
    texto = texto.strip()
    if not texto:
        return None
    if texto[0] == "'":
        if len(texto) < 2 or texto[-1] != "'":
            raise CorpusIlegible("comilla simple sin cerrar", ruta=ruta, linea=linea)
        return texto[1:-1].replace("''", "'")
    if texto[0] == '"':
        if len(texto) < 2 or texto[-1] != '"':
            raise CorpusIlegible("comilla doble sin cerrar", ruta=ruta, linea=linea)
        crudo, salida, indice = texto[1:-1], [], 0
        while indice < len(crudo):
            caracter = crudo[indice]
            if caracter == "\\":
                indice += 1
                if indice >= len(crudo):
                    raise CorpusIlegible("escape colgante", ruta=ruta, linea=linea)
                secuencia = crudo[indice]
                if secuencia not in _ESCAPES:
                    raise CorpusIlegible(
                        "escape no soportado `\\" + secuencia + "`", ruta=ruta, linea=linea,
                    )
                salida.append(_ESCAPES[secuencia])
            else:
                salida.append(caracter)
            indice += 1
        return "".join(salida)
    if texto[0] in ("&", "*", "!"):
        raise CorpusIlegible(
            "anclas, alias y etiquetas no pertenecen al subconjunto del corpus",
            ruta=ruta, linea=linea,
        )
    if texto in ("null", "~", "Null", "NULL"):
        return None
    if texto in ("true", "True", "TRUE", "yes", "Yes", "on", "On"):
        return True
    if texto in ("false", "False", "FALSE", "no", "No", "off", "Off"):
        return False
    if re.fullmatch(r"[-+]?[0-9]+", texto):
        return int(texto)
    if re.fullmatch(r"[-+]?([0-9]*\.[0-9]+|[0-9]+\.[0-9]*)", texto):
        return float(texto)
    return texto


def _cortar_flujo(texto, indice, ruta, linea):
    """Devuelve `(fragmento, resto)` del colección en flujo que empieza en `indice`."""
    apertura = texto[indice]
    cierre = "]" if apertura == "[" else "}"
    profundidad, comilla, cursor = 0, None, indice
    while cursor < len(texto):
        caracter = texto[cursor]
        if comilla:
            if caracter == comilla:
                comilla = None
        elif caracter in ("'", '"'):
            comilla = caracter
        elif caracter in ("[", "{"):
            profundidad += 1
        elif caracter in ("]", "}"):
            profundidad -= 1
            if profundidad == 0:
                if caracter != cierre:
                    raise CorpusIlegible(
                        "colección en flujo mal cerrada", ruta=ruta, linea=linea,
                    )
                return texto[indice: cursor + 1], texto[cursor + 1:]
        cursor += 1
    raise CorpusIlegible("colección en flujo sin cerrar", ruta=ruta, linea=linea)


def _partir_flujo(cuerpo, ruta, linea):
    """Parte por comas de primer nivel, respetando comillas y anidamiento."""
    piezas, profundidad, comilla, actual = [], 0, None, []
    for caracter in cuerpo:
        if comilla:
            actual.append(caracter)
            if caracter == comilla:
                comilla = None
            continue
        if caracter in ("'", '"'):
            comilla = caracter
            actual.append(caracter)
            continue
        if caracter in ("[", "{"):
            profundidad += 1
        elif caracter in ("]", "}"):
            profundidad -= 1
        if caracter == "," and profundidad == 0:
            piezas.append("".join(actual))
            actual = []
            continue
        actual.append(caracter)
    if comilla:
        raise CorpusIlegible("comilla sin cerrar en flujo", ruta=ruta, linea=linea)
    resto = "".join(actual).strip()
    if resto:
        piezas.append(resto)
    return [pieza.strip() for pieza in piezas]


def _valor_en_flujo(texto, ruta, linea):
    """`[a, b]` · `{k: v}` · un escalar. Recursivo y acotado."""
    texto = texto.strip()
    if not texto:
        return None
    if texto[0] == "[":
        fragmento, resto = _cortar_flujo(texto, 0, ruta, linea)
        if resto.strip():
            raise CorpusIlegible("sobra texto tras la lista en flujo", ruta=ruta, linea=linea)
        return [_valor_en_flujo(p, ruta, linea)
                for p in _partir_flujo(fragmento[1:-1], ruta, linea)]
    if texto[0] == "{":
        fragmento, resto = _cortar_flujo(texto, 0, ruta, linea)
        if resto.strip():
            raise CorpusIlegible("sobra texto tras el mapa en flujo", ruta=ruta, linea=linea)
        salida = {}
        for pieza in _partir_flujo(fragmento[1:-1], ruta, linea):
            clave, _, valor = _partir_clave(pieza, ruta, linea)
            salida[clave] = _valor_en_flujo(valor, ruta, linea)
        return salida
    return _escalar(texto, linea, ruta)


def _partir_clave(texto, ruta, linea):
    """`clave: resto` → `(clave, True, resto)`. `(texto, False, "")` si no hay clave."""
    comilla, profundidad = None, 0
    for indice, caracter in enumerate(texto):
        if comilla:
            if caracter == comilla:
                comilla = None
            continue
        if caracter in ("'", '"'):
            comilla = caracter
            continue
        if caracter in ("[", "{"):
            profundidad += 1
            continue
        if caracter in ("]", "}"):
            profundidad -= 1
            continue
        if caracter == ":" and profundidad == 0:
            siguiente = texto[indice + 1: indice + 2]
            if siguiente in ("", " ", "\t"):
                clave = _escalar(texto[:indice], linea, ruta)
                if not isinstance(clave, str):
                    raise CorpusIlegible(
                        "sólo se admiten claves de texto", ruta=ruta, linea=linea,
                    )
                return clave, True, texto[indice + 1:].strip()
    return texto, False, ""


class _Lineas:
    """Las líneas significativas del bloque, con su indentación y su número real."""

    def __init__(self, texto, ruta):
        self.ruta = ruta
        self.crudas = texto.split("\n")
        self.items = []
        for numero, cruda in enumerate(self.crudas, 1):
            if "\t" in cruda[: len(cruda) - len(cruda.lstrip())]:
                raise CorpusIlegible(
                    "tabulador en la indentación: YAML no lo admite y el corpus no lo usa",
                    ruta=ruta, linea=numero,
                )
            desnuda = cruda.strip()
            if not desnuda or desnuda.startswith("#"):
                continue
            if desnuda in ("---", "..."):
                raise CorpusIlegible(
                    "documentos múltiples no pertenecen al subconjunto del corpus",
                    ruta=ruta, linea=numero,
                )
            self.items.append((len(cruda) - len(cruda.lstrip(" ")), desnuda, numero))
        self.indice = 0

    def mirar(self):
        return self.items[self.indice] if self.indice < len(self.items) else None

    def avanzar(self):
        self.indice += 1


def _bloque_escalar(lineas, cabecera, indentacion_padre, ruta, linea):
    """`>` o `|` con su indicador de recorte. Devuelve el texto y consume las líneas."""
    estilo, indicador = cabecera[0], cabecera[1:].strip()
    if indicador not in ("", "-", "+"):
        raise CorpusIlegible(
            "indicador de bloque no soportado: " + repr(indicador), ruta=ruta, linea=linea,
        )
    crudas, sangria = [], None
    numero = linea
    while numero < len(lineas.crudas):
        cruda = lineas.crudas[numero]
        desnuda = cruda.strip()
        if desnuda:
            actual = len(cruda) - len(cruda.lstrip(" "))
            if actual <= indentacion_padre:
                break
            if sangria is None:
                sangria = actual
        crudas.append(cruda)
        numero += 1
    # Cuántas líneas en blanco había DESPUÉS del contenido, y si el contenido termina en
    # salto de línea. El RECORTE de YAML depende de las dos cosas: un bloque que llega al
    # final del texto sin salto no lleva salto final, y uno seguido de otra clave sí. Sin
    # este matiz el analizador difiere de PyYAML en el último campo de cada bloque, que es
    # justo donde el corpus pone `criterio_de_cierre`, `fallo` y `retirada`.
    region = "\n".join(lineas.crudas[linea:numero])
    if numero < len(lineas.crudas):
        region += "\n"
    saltos_finales = len(region) - len(region.rstrip("\n"))
    hay_salto_final = saltos_finales > 0
    while crudas and not crudas[-1].strip():
        crudas.pop()
    if sangria is None:
        contenido = ""
    else:
        recortadas = [cruda[sangria:] if len(cruda) > sangria else "" for cruda in crudas]
        if estilo == "|":
            contenido = "\n".join(recortadas)
        else:
            parrafos, actual = [], []
            for recortada in recortadas:
                if not recortada.strip():
                    parrafos.append(actual)
                    actual = []
                else:
                    actual.append(recortada.rstrip())
            parrafos.append(actual)
            contenido = "\n".join(" ".join(p) for p in parrafos if p is not None)
    contenido = contenido.rstrip("\n")
    # Consumir en el flujo de líneas significativas todo lo que quedó dentro del bloque.
    while True:
        siguiente = lineas.mirar()
        if siguiente is None or siguiente[2] > numero:
            break
        lineas.avanzar()
    if not contenido:
        return ""
    if indicador == "-":                       # RECORTAR: sin salto final
        return contenido
    if indicador == "+":                       # CONSERVAR: todos los saltos que había
        return contenido + "\n" * saltos_finales
    return contenido + ("\n" if hay_salto_final else "")   # PODAR: uno como mucho


def _analizar_nodo(lineas, indentacion, ruta):
    entrada = lineas.mirar()
    if entrada is None or entrada[0] < indentacion:
        return None
    if entrada[1].startswith("- "):
        return _analizar_lista(lineas, entrada[0], ruta)
    return _analizar_mapa(lineas, entrada[0], ruta)


def _analizar_lista(lineas, indentacion, ruta):
    salida = []
    while True:
        entrada = lineas.mirar()
        if entrada is None or entrada[0] != indentacion or not entrada[1].startswith("- "):
            if entrada is not None and entrada[0] > indentacion:
                raise CorpusIlegible(
                    "indentación incoherente dentro de una lista",
                    ruta=ruta, linea=entrada[2],
                )
            break
        _, texto, numero = entrada
        resto = texto[2:].strip()
        lineas.avanzar()
        clave, hay_clave, valor = _partir_clave(resto, ruta, numero)
        if hay_clave:
            # Un elemento que es un MAPA: su primera clave va en la misma línea que el `-`,
            # y las demás vienen indentadas dos posiciones más.
            elemento = {clave: _valor_de_clave(lineas, valor, indentacion + 2, ruta, numero)}
            elemento.update(_analizar_mapa_continuado(lineas, indentacion + 2, ruta))
            salida.append(elemento)
        elif resto:
            salida.append(_valor_en_flujo(resto, ruta, numero))
        else:
            anidado = _analizar_nodo(lineas, indentacion + 1, ruta)
            if anidado is None:
                raise CorpusIlegible("elemento de lista vacío", ruta=ruta, linea=numero)
            salida.append(anidado)
    return salida


def _analizar_mapa_continuado(lineas, indentacion, ruta):
    salida = {}
    while True:
        entrada = lineas.mirar()
        if entrada is None or entrada[0] != indentacion or entrada[1].startswith("- "):
            break
        _, texto, numero = entrada
        clave, hay_clave, valor = _partir_clave(texto, ruta, numero)
        if not hay_clave:
            break
        lineas.avanzar()
        salida[clave] = _valor_de_clave(lineas, valor, indentacion, ruta, numero)
    return salida


def _analizar_mapa(lineas, indentacion, ruta):
    salida = {}
    while True:
        entrada = lineas.mirar()
        if entrada is None or entrada[0] < indentacion:
            break
        if entrada[0] > indentacion:
            raise CorpusIlegible(
                "indentación incoherente dentro de un mapa", ruta=ruta, linea=entrada[2],
            )
        _, texto, numero = entrada
        if texto.startswith("- "):
            break
        clave, hay_clave, valor = _partir_clave(texto, ruta, numero)
        if not hay_clave:
            raise CorpusIlegible(
                "se esperaba `clave: valor` y se encontró " + repr(texto),
                ruta=ruta, linea=numero,
            )
        lineas.avanzar()
        if clave in salida:
            raise CorpusIlegible(
                "clave duplicada `" + clave + "`: dos verdades sobre el mismo campo",
                ruta=ruta, linea=numero,
            )
        salida[clave] = _valor_de_clave(lineas, valor, indentacion, ruta, numero)
    return salida


def _valor_de_clave(lineas, valor, indentacion, ruta, numero):
    """El valor de una clave: en la línea, en bloque escalar, o anidado debajo."""
    valor = _sin_comentario(valor)
    if valor[:1] in (">", "|"):
        return _bloque_escalar(lineas, valor, indentacion, ruta, numero)
    if valor[:1] in ("[", "{"):
        return _flujo_multilinea(lineas, valor, indentacion, ruta, numero)
    if valor:
        return _escalar(valor, numero, ruta)
    # Valor vacío en la línea de la clave: o viene un nodo anidado debajo, o viene una
    # colección EN FLUJO en la línea siguiente, que es como el corpus escribe las listas
    # largas para que quepan (`ejes_nunca_reutilizables` de `03-ESCALA-DE-NOVEDAD.md`).
    siguiente = lineas.mirar()
    if siguiente is not None and siguiente[0] > indentacion and siguiente[1][:1] in ("[", "{"):
        lineas.avanzar()
        return _flujo_multilinea(lineas, siguiente[1], indentacion, ruta, siguiente[2])
    anidado = _analizar_nodo(lineas, indentacion + 1, ruta)
    return anidado if anidado is not None else None


def _flujo_multilinea(lineas, comienzo, indentacion, ruta, numero):
    """Una colección en flujo que puede continuar en las líneas siguientes."""
    piezas = [comienzo]
    while _desequilibrio("\n".join(piezas)) > 0:
        entrada = lineas.mirar()
        if entrada is None or entrada[0] <= indentacion:
            raise CorpusIlegible(
                "colección en flujo sin cerrar", ruta=ruta, linea=numero,
            )
        piezas.append(entrada[1])
        lineas.avanzar()
    return _valor_en_flujo(" ".join(piezas), ruta, numero)


def _desequilibrio(texto):
    profundidad, comilla = 0, None
    for caracter in texto:
        if comilla:
            if caracter == comilla:
                comilla = None
            continue
        if caracter in ("'", '"'):
            comilla = caracter
        elif caracter in ("[", "{"):
            profundidad += 1
        elif caracter in ("]", "}"):
            profundidad -= 1
    return profundidad


def analizar(texto, ruta="(en memoria)"):
    """El subconjunto YAML del corpus → estructuras Python. FALLA ante lo que no cubre."""
    lineas = _Lineas(texto, ruta)
    if lineas.mirar() is None:
        return {}
    raiz = _analizar_nodo(lineas, lineas.mirar()[0], ruta)
    sobrante = lineas.mirar()
    if sobrante is not None:
        raise CorpusIlegible(
            "texto sobrante tras el nodo raíz", ruta=ruta, linea=sobrante[2],
        )
    return raiz


def bloques(texto, ruta="(en memoria)"):
    """Los bloques ```yaml ads:<tipo>``` de un documento, en el ORDEN EN QUE ESTÁN ESCRITOS.

    El orden es parte del contrato: `C4` paso 2 recorre las composiciones de una capacidad
    «EN EL ORDEN EN QUE ESTÁN ESCRITAS» y se queda con la primera cuya condición es
    verdadera. Devolver un diccionario los desordenaría y `C4` dejaría de ser aplicable.
    """
    salida, lineas, indice = [], texto.split("\n"), 0
    while indice < len(lineas):
        apertura = APERTURA.match(lineas[indice])
        if not apertura:
            indice += 1
            continue
        tipo, inicio, cuerpo = apertura.group(1), indice + 1, []
        indice += 1
        while indice < len(lineas) and not CIERRE.match(lineas[indice]):
            cuerpo.append(lineas[indice])
            indice += 1
        if indice >= len(lineas):
            raise CorpusIlegible(
                "bloque `ads:" + tipo + "` sin cerrar", ruta=ruta, linea=inicio,
            )
        indice += 1
        salida.append((tipo, analizar("\n".join(cuerpo), ruta), ruta, inicio))
    return salida


# ===========================================================================
#  el corpus
# ===========================================================================
class Corpus:
    """Lectura del corpus canónico de `kernel/operativo/`. No decide nada."""

    def __init__(self, raiz=None):
        self.raiz = os.path.abspath(raiz or RAIZ_POR_DEFECTO)
        if not os.path.isdir(os.path.join(self.raiz, "recorrido")):
            raise CorpusIncompleto(
                "la raíz del kernel operativo no contiene `recorrido/`: sin `b.16` no hay "
                "proceso del que derivar una ruta",
                ruta=self.raiz,
            )
        self._leidos = {}
        self._bloques = None

    # ------------------------------------------------------------- lectura
    def _texto(self, relativa):
        absoluta = os.path.join(self.raiz, relativa)
        if relativa not in self._leidos:
            try:
                with open(absoluta, "r", encoding="utf-8") as manejador:
                    self._leidos[relativa] = manejador.read()
            except OSError as exc:
                raise CorpusIncompleto(
                    "no se puede leer del corpus: " + exc.strerror, ruta=relativa,
                ) from exc
        return self._leidos[relativa]

    def _documentos(self):
        """Todo `.md` bajo la raíz, en orden estable. Sin `legacy-`, sin `__pycache__`."""
        encontrados = []
        for directorio, subdirectorios, ficheros in os.walk(self.raiz):
            subdirectorios[:] = sorted(
                d for d in subdirectorios
                if d not in (".git", "__pycache__", "runtime", "validadores", "pruebas")
                and not d.startswith("legacy-")
            )
            for nombre in sorted(ficheros):
                if nombre.endswith(".md"):
                    ruta = os.path.join(directorio, nombre)
                    encontrados.append(os.path.relpath(ruta, self.raiz).replace(os.sep, "/"))
        return sorted(encontrados)

    def todos_los_bloques(self):
        """Todos los bloques canónicos del corpus, con su tipo, su fichero y su línea."""
        if self._bloques is None:
            acumulados = []
            for relativa in self._documentos():
                acumulados.extend(bloques(self._texto(relativa), relativa))
            self._bloques = acumulados
        return self._bloques

    def de_tipo(self, tipo):
        return [datos for clase, datos, _r, _l in self.todos_los_bloques() if clase == tipo]

    # ------------------------------------------------------------ esquemas
    def esquema(self, nombre):
        datos = analizar(self._texto("esquemas/" + nombre + ".yaml"),
                         "esquemas/" + nombre + ".yaml")
        if not isinstance(datos, dict) or datos.get("esquema") != nombre:
            raise CorpusIncompleto(
                "el fichero de esquema no declara `esquema: " + nombre + "`",
                ruta="esquemas/" + nombre + ".yaml",
            )
        return datos

    def obligatorios_de(self, nombre):
        """Los campos que el esquema declara obligatorios. Se DERIVAN, no se copian."""
        campos = self.esquema(nombre).get("obligatorios")
        if not isinstance(campos, list) or not campos:
            raise CorpusIncompleto(
                "el esquema `" + nombre + "` no declara campos obligatorios",
                ruta="esquemas/" + nombre + ".yaml",
            )
        return tuple(campos)

    # ------------------------------------------------------------- b.16
    def procesos(self):
        """Los diez procesos de `b.16`, por su `id`. DERIVADOS del fichero, no copiados."""
        salida = {}
        for datos in self.de_tipo("proceso"):
            identificador = datos.get("id")
            if not isinstance(identificador, str):
                raise CorpusIlegible("un bloque `ads:proceso` sin `id`", ruta="recorrido")
            if identificador in salida:
                raise CorpusIlegible(
                    "dos bloques declaran el proceso `" + identificador + "`",
                    ruta="recorrido",
                )
            self._exigir_campos(datos, self.obligatorios_de("proceso"), identificador,
                                "proceso")
            salida[identificador] = datos
        if not salida:
            raise CorpusIncompleto("el corpus no declara ningún proceso de `b.16`")
        return salida

    def proceso(self, identificador):
        procesos = self.procesos()
        if identificador not in procesos:
            raise CorpusIncompleto(
                "el corpus no declara `" + str(identificador) + "`; declarados: "
                + ", ".join(sorted(procesos)),
                ruta=str(identificador),
            )
        return procesos[identificador]

    # -------------------------------------------------------------- gates
    def gates(self):
        """El CENSO de gates DERIVADO del corpus. No se inventa ninguno."""
        salida = {}
        obligatorios = self.obligatorios_de("gate")
        for datos in self.de_tipo("gate"):
            identificador = datos.get("id")
            if not isinstance(identificador, str):
                raise CorpusIlegible("un bloque `ads:gate` sin `id`")
            if identificador in salida:
                raise CorpusIlegible("dos bloques declaran `" + identificador + "`")
            self._exigir_campos(datos, obligatorios, identificador, "gate")
            salida[identificador] = datos
        return salida

    # ----------------------------------------------------------- handoffs
    def handoffs(self):
        """Las instancias de `C5` declaradas en `circuitos/`, con sus ONCE campos."""
        salida = {}
        obligatorios = self.obligatorios_de("handoff")
        for datos in self.de_tipo("handoff"):
            identificador = datos.get("id")
            if not isinstance(identificador, str):
                raise CorpusIlegible("un bloque `ads:handoff` sin `id`")
            if identificador in salida:
                raise CorpusIlegible("dos bloques declaran `" + identificador + "`")
            self._exigir_campos(datos, obligatorios, identificador, "handoff")
            salida[identificador] = datos
        return salida

    # ------------------------------------------------------- composiciones
    def composiciones(self, capacidad):
        """Las composiciones de una capacidad EN EL ORDEN EN QUE ESTÁN ESCRITAS (`C4`)."""
        if capacidad not in CAPACIDADES:
            raise CorpusIncompleto(
                "`" + str(capacidad) + "` no es una de las quince capacidades",
                ruta=str(capacidad),
            )
        relativa = "capacidades/" + capacidad + "/composicion.md"
        salida = []
        for clase, datos, _ruta, _linea in bloques(self._texto(relativa), relativa):
            if clase == "composicion":
                salida.append(datos)
        return salida

    def capacidad(self, identificador):
        """La ficha `ads:capacidad` de una de las quince, con sus campos declarados."""
        if identificador not in CAPACIDADES:
            raise CorpusIncompleto(
                "`" + str(identificador) + "` no es una de las quince capacidades",
                ruta=str(identificador),
            )
        relativa = "capacidades/" + identificador + "/CAPACIDAD.md"
        for clase, datos, _ruta, _linea in bloques(self._texto(relativa), relativa):
            if clase == "capacidad" and datos.get("id") == identificador:
                return datos
        raise CorpusIncompleto(
            "no hay bloque `ads:capacidad` para `" + identificador + "`", ruta=relativa,
        )

    def metodos(self, capacidad):
        """Los MÉTODOS de una capacidad, por el nombre de su fichero. NO son capacidades."""
        directorio = os.path.join(self.raiz, "capacidades", capacidad, "metodos")
        if not os.path.isdir(directorio):
            return ()
        return tuple(sorted(
            nombre[: -len(".md")] for nombre in os.listdir(directorio)
            if nombre.endswith(".md")
        ))

    def capacidades(self):
        """Las capacidades DERIVADAS del árbol `capacidades/`, no de una lista escrita."""
        directorio = os.path.join(self.raiz, "capacidades")
        return tuple(sorted(
            nombre for nombre in os.listdir(directorio)
            if os.path.isfile(os.path.join(directorio, nombre, "CAPACIDAD.md"))
        ))

    def exigir_quince(self):
        """El árbol y la lista de `§18` dicen lo mismo, o se dice cuál sobra y cuál falta."""
        derivadas = set(self.capacidades())
        declaradas = set(CAPACIDADES)
        if derivadas != declaradas:
            raise CorpusIncompleto(
                "el árbol de capacidades y las quince de `§18` no coinciden; sobran: "
                + (", ".join(sorted(derivadas - declaradas)) or "(ninguna)")
                + "; faltan: " + (", ".join(sorted(declaradas - derivadas)) or "(ninguna)"),
            )
        return tuple(sorted(derivadas))

    # ----------------------------------------------------------- entradas
    def entradas(self):
        """Las NUEVE clases de la taxonomía de entrada, por su `id`."""
        salida = {}
        for datos in self.de_tipo("entrada"):
            identificador = datos.get("id")
            if not isinstance(identificador, str):
                raise CorpusIlegible("un bloque `ads:entrada` sin `id`")
            salida[identificador] = datos
        if not salida:
            raise CorpusIncompleto("el corpus no declara ninguna clase de entrada")
        return salida

    # ------------------------------------------------------------- huella
    def huella(self):
        """`sha256` del corpus leído. Es el identificador nº 3 y nº 4 del sujeto de `§9.6`.

        Se calcula sobre los ficheros LEÍDOS —ruta y contenido, en orden estable— y no
        sobre el árbol entero: lo que define el sujeto es el corpus del que se derivó la
        ruta, no los ficheros que nadie abrió. Es determinista y no lleva rutas absolutas.
        """
        digestor = hashlib.sha256()
        for relativa in self._documentos():
            digestor.update(relativa.encode("utf-8"))
            digestor.update(b"\0")
            digestor.update(hashlib.sha256(self._texto(relativa).encode("utf-8")).digest())
        for nombre in sorted(os.listdir(os.path.join(self.raiz, "esquemas"))):
            if not nombre.endswith(".yaml"):
                continue
            relativa = "esquemas/" + nombre
            digestor.update(relativa.encode("utf-8"))
            digestor.update(b"\0")
            digestor.update(hashlib.sha256(self._texto(relativa).encode("utf-8")).digest())
        return "sha256:" + digestor.hexdigest()

    # ---------------------------------------------------------- auxiliares
    @staticmethod
    def _exigir_campos(datos, obligatorios, identificador, tipo):
        faltan = [campo for campo in obligatorios if campo not in datos]
        if faltan:
            raise CorpusIlegible(
                "el bloque `ads:" + tipo + "` `" + str(identificador) + "` no declara "
                + ", ".join(faltan),
                ruta=str(identificador),
            )
        return datos
