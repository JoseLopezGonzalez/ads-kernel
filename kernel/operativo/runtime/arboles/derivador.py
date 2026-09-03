#!/usr/bin/env python3
"""derivador — el CONJUNTO de árboles adversariales de `V6-15`, DERIVADO de su sede.

La sede la fija `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` §20.5, y no es una lista: es
una FORMA de cabecera publicada por cada gate en su documento inmutable.

    grep -nE '^## [0-9]+ · EL [A-ZÁÉÍÓÚ]+ ÁRBOL' docs/evolucion/[0-9][0-9]-*.md

**Aquí no se llama a `grep`: se analizan los ficheros.** Un derivador que delega en una orden
externa depende de la localización, del `grep` instalado y del `cwd`, y las tres cosas cambian
el resultado sin cambiar el corpus.

DECISIÓN · el conjunto NO se escribe, y su CARDINAL tampoco
    §20.5 lo dice con todas las letras y es la regla de `J-07`: «Ni "once", ni "tres", ni
    "cuatro" se escriben en esta sección ni en la fila de `V6-15`: quien necesite el número
    ejecuta el comando». Por eso en este módulo, en el contrato derivado y en la salida del
    punto ejecutable **no hay un solo cardinal del conjunto**. Si un gate futuro publica otro
    árbol con la misma cabecera, entra solo y nadie edita una línea.

DECISIÓN · se derivan ÁRBOLES, no identificadores de hallazgo
    §20.5 registra por qué: el remedio anterior barría las filas de las matrices de tres
    documentos y devolvía setenta y cinco identificadores de hallazgo, «de los que la inmensa
    mayoría son defectos de redacción que NO TIENEN ROJO QUE DAR». Un contrato cuyo cierre se
    mide sobre el objeto equivocado es insatisfacible. El objeto de `V6-15` es el ÁRBOL, y su
    identificador estable es la CABECERA, con el DOCUMENTO que la contiene como sede.

DECISIÓN · el hallazgo que CERRÓ cada árbol se deriva, no se escribe
    §20.5 pide «el identificador del hallazgo que lo cerró, que vive en el mismo documento».
    Se deriva con una regla mecánica y comprobable: dentro del MISMO documento, las líneas
    que nombran ese árbol por su ordinal y que son o bien una CABECERA de sección, o bien una
    FILA DE MATRIZ cuya primera celda es exactamente un identificador. De ahí sale el primer
    identificador de la línea.
    Alternativas descartadas: (a) una tabla escrita a mano en este fichero —caduca en cuanto
    un gate publique otro árbol, que es justamente lo que §20.5 prohíbe—; (b) recoger TODOS
    los identificadores que aparezcan en el documento —devuelve el censo entero del gate, que
    es el error de objeto que §20.5 acaba de corregir—; (c) recoger todos los de la sección
    del árbol —la sección de resumen no los nombra, y los que sí lo hacen viven en el
    dictamen del adjudicador, al final del documento—.

DECISIÓN · el ORDEN y las RUTAS son deterministas, y la salida es la misma desde cualquier `cwd`
    Las rutas se publican SIEMPRE relativas a la raíz del repositorio y con `/`, y el conjunto
    se ordena por (documento, línea). `I-g3` no admite que una evidencia publicada dependa del
    directorio desde el que se ejecutó el instrumento.
"""
from __future__ import annotations

import os
import re

from .errores import ArbolDuplicado, SedeAusente

# La SEDE de la forma de cabecera. Es §20.5 traducida a expresión regular, y ni una letra
# más: si la cabecera cambiara, cambiaría §20.5, que es material inmutable de un gate.
PATRON_DE_CABECERA = re.compile(r"^## \d+ · EL ([A-ZÁÉÍÓÚÑÜ]+) ÁRBOL")

# Los documentos donde se busca. Es el `docs/evolucion/[0-9][0-9]-*.md` del comando.
DIRECTORIO_DE_DOCUMENTOS = "docs/evolucion"
PATRON_DE_FICHERO = re.compile(r"^[0-9][0-9]-.*\.md$")

# Un identificador de hallazgo: prefijo de cadena o de revisor, guion y su ordinal.
PATRON_DE_HALLAZGO = re.compile(r"`([A-Z][A-Z0-9]{0,3}-[0-9]{2})`")
PATRON_DE_CELDA_UNICA = re.compile(r"^\|\s*\**\s*`([A-Z][A-Z0-9]{0,3}-[0-9]{2})`\s*\**\s*\|")
PATRON_DE_TITULO = re.compile(r"^#{1,6} ")


class Arbol:
    """Un árbol adversarial del conjunto derivado, con su procedencia documental."""

    __slots__ = ("ordinal", "documento", "linea", "cabecera", "hallazgos")

    def __init__(self, ordinal, documento, linea, cabecera, hallazgos):
        self.ordinal = ordinal
        self.documento = documento
        self.linea = int(linea)
        self.cabecera = cabecera
        self.hallazgos = tuple(hallazgos)

    @property
    def clave(self):
        """La identidad del árbol: su cabecera y el documento que la contiene."""
        return (self.documento, self.cabecera)

    def a_dict(self):
        return {
            "ordinal": self.ordinal,
            "documento": self.documento,
            "linea": self.linea,
            "cabecera": self.cabecera,
            "hallazgos_que_lo_cerraron": list(self.hallazgos),
        }

    def __repr__(self):
        return "Arbol(" + self.ordinal + " @" + self.documento + ":" + str(self.linea) + ")"


def _documentos(raiz):
    """Los documentos numerados de la iniciativa, ordenados. Derivados del disco."""
    directorio = os.path.join(raiz, DIRECTORIO_DE_DOCUMENTOS)
    if not os.path.isdir(directorio):
        raise SedeAusente(
            "no existe el directorio de documentos numerados que §20.5 designa como sede "
            "del conjunto de árboles adversariales",
            ruta=DIRECTORIO_DE_DOCUMENTOS,
        )
    nombres = [nombre for nombre in sorted(os.listdir(directorio))
               if PATRON_DE_FICHERO.match(nombre)]
    if not nombres:
        raise SedeAusente(
            "el directorio de documentos numerados no contiene ninguno: sin sede no se "
            "deriva conjunto, y no se devuelve el conjunto vacío como si fuera un hecho",
            ruta=DIRECTORIO_DE_DOCUMENTOS,
        )
    return nombres


def _lineas(raiz, relativa):
    """Lee un documento como texto estricto. Un documento ilegible es SEDE AUSENTE."""
    completa = os.path.join(raiz, relativa)
    try:
        with open(completa, "rb") as manejador:
            crudo = manejador.read()
    except OSError as exc:
        raise SedeAusente(
            "no se pudo leer un documento de la sede: " + str(exc.strerror),
            ruta=relativa,
        ) from exc
    try:
        texto = crudo.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise SedeAusente(
            "un documento de la sede no es UTF-8 válido en el byte " + str(exc.start)
            + ": se DENUNCIA y no se interpreta a medias",
            ruta=relativa,
        ) from exc
    return texto.split("\n")


def _hallazgos_declarados(lineas):
    """Los identificadores que el documento DECLARA como hallazgos SUYOS.

    Un documento de gate declara sus hallazgos en una matriz cuya primera celda es el
    identificador. Ese es el censo del documento, y sirve de FILTRO: un identificador que el
    documento cita pero no declara —una proposición general como `M-04`, un hallazgo de otro
    gate— no puede ser «el hallazgo que cerró este árbol», porque no es un hallazgo de este
    documento. Sin el filtro, la cabecera «¿HAY UN OCTAVO ÁRBOL?» del ataque del adjudicador
    aportaba `M-04`, que es la proposición ATACADA y no el hallazgo que la cerró.
    """
    declarados = set()
    for linea in lineas:
        celda = PATRON_DE_CELDA_UNICA.match(linea)
        if celda is not None:
            declarados.add(celda.group(1))
    return declarados


def _hallazgos_del_arbol(lineas, ordinal):
    """Los identificadores de hallazgo que cierran este árbol, DENTRO de su documento.

    Se admiten dos formas de línea, y sólo dos:
      · una CABECERA de sección que nombre el árbol por su ordinal;
      · una FILA DE MATRIZ cuya PRIMERA CELDA sea exactamente un identificador.
    De cada línea admitida se toma el PRIMER identificador, y se conserva sólo si el propio
    documento lo DECLARA como hallazgo suyo. La restricción de la primera celda es la que
    impide que una fila de resumen —cuya primera celda es prosa que cita más de un árbol— aporte
    el identificador de otro.
    """
    aguja = ordinal + " ÁRBOL"
    declarados = _hallazgos_declarados(lineas)
    encontrados = []
    for linea in lineas:
        if aguja not in linea:
            continue
        if PATRON_DE_TITULO.match(linea):
            hallazgo = PATRON_DE_HALLAZGO.search(linea)
            if hallazgo is not None and hallazgo.group(1) not in encontrados:
                encontrados.append(hallazgo.group(1))
            continue
        celda = PATRON_DE_CELDA_UNICA.match(linea)
        if celda is not None and celda.group(1) not in encontrados:
            encontrados.append(celda.group(1))
    return sorted(identificador for identificador in encontrados
                  if identificador in declarados)


def derivar(raiz):
    """El conjunto de árboles adversariales, DERIVADO. Ordenado por documento y línea."""
    raiz = os.path.abspath(raiz)
    arboles = []
    for nombre in _documentos(raiz):
        relativa = DIRECTORIO_DE_DOCUMENTOS + "/" + nombre
        lineas = _lineas(raiz, relativa)
        for indice, linea in enumerate(lineas, start=1):
            casado = PATRON_DE_CABECERA.match(linea)
            if casado is None:
                continue
            ordinal = casado.group(1)
            arboles.append(Arbol(
                ordinal=ordinal,
                documento=relativa,
                linea=indice,
                cabecera=linea.rstrip(),
                hallazgos=_hallazgos_del_arbol(lineas, ordinal),
            ))
    arboles.sort(key=lambda arbol: (arbol.documento, arbol.linea))
    return arboles


def duplicados(arboles):
    """Dos entradas que nombran el MISMO árbol. Se mide por ORDINAL y por CLAVE.

    Por ordinal, porque el ordinal lo pone el gate que encontró el árbol y es único por
    construcción: dos documentos que publiquen «EL NOVENO ÁRBOL» describen el mismo objeto
    dos veces, y la suite lo reproduciría dos veces creyendo que son dos.
    """
    por_ordinal = {}
    por_clave = {}
    salida = []
    for arbol in arboles:
        por_ordinal.setdefault(arbol.ordinal, []).append(arbol)
        por_clave.setdefault(arbol.clave, []).append(arbol)
    for ordinal in sorted(por_ordinal):
        grupo = por_ordinal[ordinal]
        if len(grupo) > 1:
            salida.append({
                "motivo": "ordinal repetido",
                "ordinal": ordinal,
                "sedes": [{"documento": a.documento, "linea": a.linea} for a in grupo],
            })
    for clave in sorted(por_clave):
        grupo = por_clave[clave]
        if len(grupo) > 1:
            salida.append({
                "motivo": "cabecera repetida en el mismo documento",
                "ordinal": grupo[0].ordinal,
                "sedes": [{"documento": a.documento, "linea": a.linea} for a in grupo],
            })
    return salida


def exigir_sin_duplicados(arboles):
    """Fallo CERRADO: un conjunto con duplicados no se usa como entrada de la suite."""
    repetidos = duplicados(arboles)
    if repetidos:
        primero = repetidos[0]
        raise ArbolDuplicado(
            "el conjunto derivado trae un árbol repetido (" + primero["motivo"] + "): `"
            + primero["ordinal"] + "`. La suite no se ejecuta sobre una entrada ambigua",
            ruta=primero["sedes"][0]["documento"],
            sedes=[sede["documento"] + ":" + str(sede["linea"])
                   for sede in primero["sedes"]],
        )
    return arboles


def validar(raiz, arboles):
    """Comprueba que CADA entrada EXISTE: documento presente y cabecera presente y exacta."""
    filas = []
    for arbol in arboles:
        completa = os.path.join(os.path.abspath(raiz), arbol.documento)
        documento_presente = os.path.isfile(completa)
        cabecera_presente = False
        if documento_presente:
            lineas = _lineas(raiz, arbol.documento)
            cabecera_presente = (
                len(lineas) >= arbol.linea
                and lineas[arbol.linea - 1].rstrip() == arbol.cabecera
            )
        filas.append({
            "ordinal": arbol.ordinal,
            "documento": arbol.documento,
            "linea": arbol.linea,
            "documento_presente": documento_presente,
            "cabecera_presente": cabecera_presente,
            "hallazgos_que_lo_cerraron": list(arbol.hallazgos),
            "ok": documento_presente and cabecera_presente and bool(arbol.hallazgos),
        })
    return {"entradas": filas, "ok": all(fila["ok"] for fila in filas)}


def exigir_validas(raiz, arboles):
    """Fallo CERRADO ante una entrada cuya sede no existe o cuya cabecera no está."""
    informe = validar(raiz, arboles)
    for fila in informe["entradas"]:
        if fila["ok"]:
            continue
        if not fila["documento_presente"]:
            causa = "el documento que la contiene no está en el árbol"
        elif not fila["cabecera_presente"]:
            causa = ("la cabecera declarada no está en la línea registrada: la sede es "
                     "inmutable y una discrepancia significa que se leyó otra cosa")
        else:
            causa = ("el documento no publica ningún hallazgo que cierre este árbol, y "
                     "§20.5 exige que cada árbol traiga el suyo")
        raise SedeAusente(
            "entrada inválida del conjunto derivado (`" + fila["ordinal"] + "`): " + causa,
            ruta=fila["documento"],
            linea=fila["linea"],
        )
    return informe
