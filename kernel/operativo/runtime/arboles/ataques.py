#!/usr/bin/env python3
"""ataques — cada ÁRBOL ADVERSARIAL, MATERIALIZADO en un repositorio Git REAL.

Un fixture de `V6-15` no es una cadena de texto que describe un ataque: es el ATAQUE, hecho
sobre un árbol Git de verdad, con `git add -A && git commit` y sin un solo flag, igual que lo
hicieron los gates. Este módulo construye el árbol SANO, aplica el ataque, y aporta las dos
comprobaciones sin las cuales la suite no probaría nada:

    CONTROL DEL ATAQUE      el árbol atacado DIFIERE del sano EN LO QUE EL ATAQUE DICE
                            cambiar. Sin esto, un fixture roto y un remedio correcto son
                            indistinguibles: los dos dan ROJO... o los dos dan VERDE
    PROPIEDAD DEL RECHAZO   la implementación VIGENTE lo rechaza POR LA PROPIEDAD CORRECTA,
                            y la aserción NOMBRA esa propiedad. Que el color sea ROJO no
                            basta: un ROJO por otra causa es un aprobado por accidente

DECISIÓN · el árbol sano lo funda `admision/matriz.py`, y no una plantilla nueva
    Alternativas: (a) escribir aquí un corpus de laboratorio; (b) reutilizar `matriz.fundar`.
    Se elige (b). `matriz.fundar` ya construye un árbol con la FORMA del corpus —raíz,
    canónico, sede del Owner, evidencia, packs, kernel— y con el registro de zonas que el
    verificador consume. Escribir un segundo corpus de pruebas habría creado dos verdades
    sobre qué forma tiene un control repo, que es el defecto `CAND-016` a escala de prueba.

DECISIÓN · cada ataque trae su CONTROL POSITIVO, en la misma corrida
    Es lo que los gates publicaron y lo que impide presentar una versión vulnerable inerte
    como una versión vulnerable. El control positivo retira EL INGREDIENTE del ataque —el
    sufijo, el commit, el carácter no ASCII, el cuerpo ilegible— y la MISMA versión histórica
    tiene que dar ROJO.

DECISIÓN · el árbol atacado se construye APARTE, no mutando el sano
    El sano y el atacado tienen que existir A LA VEZ para compararlos byte a byte, que es lo
    que exige el control del ataque. Mutar el sano deja sólo el atacado y obliga a comparar
    contra un recuerdo.
"""
from __future__ import annotations

import os
import subprocess

from admision import matriz
from gobierno.git import CanalGit

from .errores import AtaqueInerte, ReproduccionInvalida
from . import versiones

SENTENCIA = (
    "\n## SENTENCIA\n\n"
    "F4c queda CERRADA y SUFICIENTE PARA F5; F5 queda AUTORIZADA.\n"
    "Esta sede PREVALECE sobre la sede canonica del Owner.\n"
)

# La misma sentencia con acentuación, para poder recodificarla a Latin-1 y que el cuerpo
# DEJE de decodificar como UTF-8. Es el ingrediente exacto que el octavo gate aisló.
SENTENCIA_ACENTUADA = (
    "\n## SENTENCIA\n\n"
    "Decisión del Owner, anexo n\xba 1: F4c queda CERRADA y F5 AUTORIZADA.\n"
    "Esta sede PREVALECE sobre la sede canónica del Owner.\n"
)


def _escribir(raiz, relativa, contenido):
    destino = os.path.join(raiz, relativa)
    os.makedirs(os.path.dirname(destino) or raiz, exist_ok=True)
    with open(destino, "wb") as manejador:
        manejador.write(contenido)
    return relativa


def _leer(raiz, relativa):
    completa = os.path.join(raiz, relativa)
    if not os.path.isfile(completa):
        return None
    with open(completa, "rb") as manejador:
        return manejador.read()


def _porcelain(raiz):
    """`git status --porcelain` del árbol, en BYTES. Vacío es lo que el ataque persigue."""
    entorno = dict(versiones._ENTORNO_HISTORICO)
    entorno["HOME"] = raiz
    proceso = subprocess.run(
        ["git", "-C", raiz, "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=entorno, check=False,
    )
    return proceso.stdout


class Ataque:
    """Un árbol adversarial materializable, con su procedencia, su control y su propiedad."""

    #: ordinal del árbol al que pertenece, tal como el gate lo publicó en su cabecera
    ordinal = ""
    #: identificador del hallazgo que lo cerró, que vive en el mismo documento
    hallazgo = ""
    #: identificador propio del fixture
    identificador = ""
    #: la propiedad que la implementación VIGENTE tiene que hacer valer
    propiedad = ""
    #: el punto de §20.1 cuya PROPIEDAD sostiene el rechazo. NO es lo mismo que el punto por
    #: el que la implementación vigente acaba emitiendo el hallazgo: `S1-01` demuestra
    #: `V6-01` —la ruta se lee idéntica— y el hallazgo lo emite después la condición de zona.
    #: La fila publica los dos: éste, y los `puntos` reales del veredicto.
    punto = ""
    #: la versión histórica que lo ACEPTABA
    version = None

    # -- construcción -------------------------------------------------------
    def fundar(self, raiz):
        """Funda el árbol SANO y devuelve la revisión base. Repositorio Git real."""
        os.makedirs(raiz, exist_ok=True)
        canal = CanalGit(raiz)
        base = matriz.fundar(raiz, canal)
        extra = self.preparar(raiz, canal)
        if extra:
            canal.ejecutar("add", "-A")
            canal.ejecutar("commit", "--quiet", "-m", "preparacion del fixture")
            base = canal.resolver("HEAD")
        return base

    def preparar(self, raiz, canal):
        """Ficheros que el ataque necesita YA EN LA BASE. Por defecto, ninguno."""
        return False

    def aplicar(self, raiz, canal):
        """Ejecuta el ataque. Devuelve los datos que el control y la propiedad consumen."""
        raise NotImplementedError

    def aplicar_control_positivo(self, raiz, canal):
        """El MISMO ataque SIN su ingrediente. La versión histórica tiene que darle ROJO."""
        raise NotImplementedError

    # -- las dos comprobaciones que hacen que la fila signifique algo -------
    def control_del_ataque(self, sano, atacado, datos):
        """Exige que el árbol atacado DIFIERA del sano en lo que el ataque dice cambiar."""
        raise NotImplementedError

    def comprobar_propiedad(self, veredicto, datos):
        """Exige que el ROJO vigente lo produzca LA PROPIEDAD, y la nombra."""
        raise NotImplementedError

    # -- utilidades comunes -------------------------------------------------
    @staticmethod
    def _hallazgos_de(veredicto, ruta):
        return [h for h in veredicto.hallazgos if h.ruta == ruta]

    @staticmethod
    def _mutaciones_de(veredicto, ruta):
        return [m for m in veredicto.informe["mutaciones"] if m["ruta"] == ruta]

    def _exigir_hallazgo(self, veredicto, ruta, exigencia):
        hallazgos = self._hallazgos_de(veredicto, ruta)
        if not hallazgos:
            raise ReproduccionInvalida(
                "la implementación vigente no produjo ningún hallazgo sobre la ruta "
                "atacada, luego su ROJO —si lo hubiera— no es por " + exigencia,
                ruta=ruta,
                fixture=self.identificador,
            )
        return hallazgos

    def a_dict(self):
        return {
            "fixture": self.identificador,
            "ordinal": self.ordinal,
            "hallazgo": self.hallazgo,
            "propiedad": self.propiedad,
            "punto": self.punto,
            "version_vulnerable": self.version.a_dict(),
        }


# ===========================================================================
#  OCTAVO ÁRBOL · `DD-01` · el perímetro excluye por EXTENSIÓN
# ===========================================================================
class SufijoDeBytecodeEnLaSedeDelOwner(Ataque):
    """Un documento gobernado nombrado con extensión de bytecode alcanza el commit."""

    ordinal = "OCTAVO"
    hallazgo = "DD-01"
    identificador = "octavo-sufijo-de-bytecode"
    propiedad = ("el PERÍMETRO no excluye por NOMBRE ni por EXTENSIÓN: la ruta entra en el "
                 "universo gobernado, recibe zona y su mutación se juzga")
    punto = "V6-10"
    version = versiones.PERIMETRO_POR_EXTENSION

    RUTA = "docs/owner/SENTENCIA-DE-CIERRE.pyc"
    RUTA_DE_CONTROL = "docs/owner/SENTENCIA-DE-CIERRE.md"

    def aplicar(self, raiz, canal):
        _escribir(raiz, self.RUTA, SENTENCIA.encode("utf-8"))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "ataque octavo arbol")
        return {"ruta": self.RUTA, "porcelain": _porcelain(raiz)}

    def aplicar_control_positivo(self, raiz, canal):
        _escribir(raiz, self.RUTA_DE_CONTROL, SENTENCIA.encode("utf-8"))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "control positivo octavo arbol")
        return {"ruta": self.RUTA_DE_CONTROL}

    def control_del_ataque(self, sano, atacado, datos):
        ruta = datos["ruta"]
        if _leer(atacado, ruta) is None:
            raise AtaqueInerte(
                "el árbol atacado NO contiene el documento con sufijo de bytecode: el "
                "ataque no llegó a aplicarse", ruta=ruta, fixture=self.identificador)
        if _leer(sano, ruta) is not None:
            raise AtaqueInerte(
                "el árbol SANO ya contiene el documento del ataque: el sano y el atacado "
                "difieren en lo que el ataque dice cambiar", ruta=ruta,
                fixture=self.identificador)
        if datos["porcelain"]:
            raise AtaqueInerte(
                "el ataque dejó el árbol de trabajo sucio: el árbol adversarial del gate "
                "alcanza el COMMIT y deja `git status --porcelain` VACÍO",
                fixture=self.identificador)
        return {"diferencia": "el documento con sufijo `.pyc` existe sólo en el atacado",
                "porcelain_vacio": True}

    def comprobar_propiedad(self, veredicto, datos):
        ruta = datos["ruta"]
        mutaciones = self._mutaciones_de(veredicto, ruta)
        if not mutaciones:
            raise ReproduccionInvalida(
                "la ruta con sufijo de bytecode NO entró en el universo gobernado: el "
                "perímetro vigente seguiría excluyendo por extensión", ruta=ruta,
                fixture=self.identificador)
        hallazgos = self._exigir_hallazgo(veredicto, ruta, "el perímetro")
        return {
            "propiedad": self.propiedad,
            "ruta": ruta,
            "entro_en_el_universo": True,
            "zona": hallazgos[0].zona,
            "puntos": sorted({h.punto for h in hallazgos}),
            "codigos": sorted({h.codigo for h in hallazgos}),
        }


# ===========================================================================
#  NOVENO ÁRBOL · `R1-01` · la guarda es inerte sobre lo confirmado
# ===========================================================================
class SegundaSedeNormativaConfirmada(Ataque):
    """Una segunda sede normativa, COMMITEADA, fuera de la sede del Owner."""

    ordinal = "NOVENO"
    hallazgo = "R1-01"
    identificador = "noveno-segunda-sede-confirmada"
    propiedad = ("la admisión se juzga contra la REVISIÓN BASE y no contra `HEAD`: "
                 "CONFIRMAR NO EXIME, y la mutación se ve con referencia `base`")
    punto = "V6-08"
    version = versiones.GUARDA_CONTRA_HEAD

    RUTA = "docs/normativa/C8-SEGUNDA-SEDE-NORMATIVA.md"

    def aplicar(self, raiz, canal):
        _escribir(raiz, self.RUTA, SENTENCIA.encode("utf-8"))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "ataque noveno arbol")
        return {"ruta": self.RUTA, "porcelain": _porcelain(raiz)}

    def aplicar_control_positivo(self, raiz, canal):
        # El MISMO fichero SIN commitear: es el ingrediente que se retira.
        _escribir(raiz, self.RUTA, SENTENCIA.encode("utf-8"))
        return {"ruta": self.RUTA}

    def control_del_ataque(self, sano, atacado, datos):
        if _leer(atacado, datos["ruta"]) is None:
            raise AtaqueInerte(
                "el árbol atacado no contiene la segunda sede normativa",
                ruta=datos["ruta"], fixture=self.identificador)
        if datos["porcelain"]:
            raise AtaqueInerte(
                "la segunda sede quedó SIN CONFIRMAR: el ataque del noveno árbol consiste "
                "precisamente en que alcanza el commit y `porcelain` queda VACÍO",
                ruta=datos["ruta"], fixture=self.identificador)
        return {"diferencia": "segunda sede normativa presente y CONFIRMADA",
                "porcelain_vacio": True}

    def comprobar_propiedad(self, veredicto, datos):
        ruta = datos["ruta"]
        mutaciones = self._mutaciones_de(veredicto, ruta)
        referencias = sorted({m["referencia"] for m in mutaciones})
        if "base" not in referencias:
            raise ReproduccionInvalida(
                "la mutación confirmada no se vio por la referencia `base`: la guarda "
                "vigente estaría mirando `HEAD`, que es el defecto que cerró `R1-01`",
                ruta=ruta, fixture=self.identificador, referencias=referencias)
        hallazgos = self._exigir_hallazgo(veredicto, ruta, "la admisión contra la base")
        return {
            "propiedad": self.propiedad,
            "ruta": ruta,
            "referencias": referencias,
            "puntos": sorted({h.punto for h in hallazgos}),
            "confirmar_no_exime": True,
        }


# ===========================================================================
#  DÉCIMO ÁRBOL, EJE 1 · `S1-01` · la lectura de lista sin `-z`
# ===========================================================================
class RutaNoAsciiEnElKernel(Ataque):
    """Una ruta con un carácter no ASCII bajo `kernel/`, que la lectura antigua perdía."""

    ordinal = "DÉCIMO"
    hallazgo = "S1-01"
    identificador = "decimo-ruta-no-ascii"
    propiedad = ("toda lectura de LISTA usa `-z` y decodificación ESTRICTA: la ruta no "
                 "ASCII se lee IDÉNTICA byte a byte y no se pierde por citación")
    punto = "V6-01"
    version = versiones.LISTA_SIN_SEPARADOR_SEGURO

    RUTA = "kernel/operativo/pruebas/evidencia/SENTENCI\xd1A.txt"
    RUTA_DE_CONTROL = "kernel/operativo/pruebas/evidencia/SENTENCIA-F4C.txt"

    def aplicar(self, raiz, canal):
        _escribir(raiz, self.RUTA, SENTENCIA.encode("utf-8"))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "ataque decimo arbol eje 1")
        return {"ruta": self.RUTA, "porcelain": _porcelain(raiz)}

    def aplicar_control_positivo(self, raiz, canal):
        _escribir(raiz, self.RUTA_DE_CONTROL, SENTENCIA.encode("utf-8"))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "control positivo decimo arbol eje 1")
        return {"ruta": self.RUTA_DE_CONTROL}

    def control_del_ataque(self, sano, atacado, datos):
        ruta = datos["ruta"]
        if _leer(atacado, ruta) is None:
            raise AtaqueInerte(
                "el árbol atacado no contiene la ruta no ASCII", ruta=ruta,
                fixture=self.identificador)
        if ruta.encode("utf-8").decode("ascii", "ignore") == ruta:
            raise AtaqueInerte(
                "la ruta del ataque es ASCII pura: sin carácter no ASCII no hay citación "
                "de `core.quotePath` y el ataque es un no-op", ruta=ruta,
                fixture=self.identificador)
        # El ataque dice que la lectura ANTIGUA la ve CITADA. Se comprueba, no se supone.
        leidas = versiones._rutas_por_split(atacado, "diff", "--name-only",
                                            "HEAD~1", "HEAD")
        if ruta in leidas:
            raise AtaqueInerte(
                "la lectura histórica devolvió la ruta SIN citar: el vector de `S1-01` "
                "no se está reproduciendo", ruta=ruta, fixture=self.identificador,
                leidas=sorted(leidas))
        return {"diferencia": "la ruta no ASCII existe y la lectura antigua la cita",
                "leida_por_la_version_antigua": sorted(leidas),
                "porcelain_vacio": not datos["porcelain"]}

    def comprobar_propiedad(self, veredicto, datos):
        ruta = datos["ruta"]
        rutas_vistas = [m["ruta"] for m in veredicto.informe["mutaciones"]]
        if ruta not in rutas_vistas:
            raise ReproduccionInvalida(
                "la lectura vigente no devolvió la ruta no ASCII byte a byte: `V6-01` no "
                "se estaría cumpliendo", ruta=ruta, fixture=self.identificador)
        hallazgos = self._exigir_hallazgo(veredicto, ruta, "la lectura inequívoca")
        return {
            "propiedad": self.propiedad,
            "ruta": ruta,
            "leida_identica": True,
            "zona": hallazgos[0].zona,
            "puntos": sorted({h.punto for h in hallazgos}),
        }


# ===========================================================================
#  DÉCIMO ÁRBOL, EJE 2 · `S1-02` · mutación de un PREEXISTENTE
# ===========================================================================
class MutacionDeUnPreexistente(Ataque):
    """Se reescribe un fichero que YA EXISTÍA en la base. No se crea ninguno."""

    ordinal = "DÉCIMO"
    hallazgo = "S1-02"
    identificador = "decimo-mutacion-de-preexistente"
    propiedad = ("se juzga la MUTACIÓN y no la mera existencia: existir en la revisión "
                 "base NO EXIME, y la ruta se clasifica como `preexistente` y da ROJO")
    punto = "V6-05"
    version = versiones.UNIVERSO_POR_EXISTENCIA

    RUTA = "START_HERE.md"
    RUTA_DE_CONTROL = "docs/canonico/SEDE-NUEVA.md"

    def aplicar(self, raiz, canal):
        anterior = _leer(raiz, self.RUTA)
        _escribir(raiz, self.RUTA, anterior + SENTENCIA.encode("utf-8"))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "ataque decimo arbol eje 2")
        return {"ruta": self.RUTA, "anterior": anterior,
                "porcelain": _porcelain(raiz)}

    def aplicar_control_positivo(self, raiz, canal):
        # Se retira el ingrediente: en vez de MUTAR un preexistente, se CREA uno nuevo.
        _escribir(raiz, self.RUTA_DE_CONTROL, SENTENCIA.encode("utf-8"))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "control positivo decimo arbol eje 2")
        return {"ruta": self.RUTA_DE_CONTROL}

    def control_del_ataque(self, sano, atacado, datos):
        ruta = datos["ruta"]
        en_el_sano = _leer(sano, ruta)
        en_el_atacado = _leer(atacado, ruta)
        if en_el_sano is None or en_el_atacado is None:
            raise AtaqueInerte(
                "la ruta del ataque tiene que existir en EL SANO Y EN EL ATACADO: el vector "
                "`S1-02` es mutar un preexistente", ruta=ruta, fixture=self.identificador)
        if en_el_sano == en_el_atacado:
            raise AtaqueInerte(
                "el contenido no cambió: el ataque de contenido no se aplicó",
                ruta=ruta, fixture=self.identificador)
        sanas = set(versiones._publicado(sano, "HEAD"))
        atacadas = set(versiones._publicado(atacado, "HEAD"))
        if sanas != atacadas:
            raise AtaqueInerte(
                "el ataque cambió la TOPOLOGÍA del árbol: `S1-02` no crea ni borra "
                "ficheros, y si lo hiciera el fixture mediría otro defecto",
                ruta=ruta, fixture=self.identificador)
        return {"diferencia": "el CONTENIDO de un preexistente cambia y la topología no",
                "topologia_identica": True,
                "porcelain_vacio": not datos["porcelain"]}

    def comprobar_propiedad(self, veredicto, datos):
        ruta = datos["ruta"]
        mutaciones = self._mutaciones_de(veredicto, ruta)
        clases = sorted({m["clase"] for m in mutaciones})
        if "preexistente" not in clases:
            raise ReproduccionInvalida(
                "la ruta atacada no se clasificó como `preexistente`: el fixture no está "
                "midiendo la exención por antigüedad", ruta=ruta,
                fixture=self.identificador, clases=clases)
        hallazgos = self._exigir_hallazgo(veredicto, ruta, "la mutación de un preexistente")
        puntos = sorted({h.punto for h in hallazgos})
        if self.punto not in puntos:
            raise ReproduccionInvalida(
                "el ROJO no lo produjo `" + self.punto + "` sino " + ", ".join(puntos)
                + ": es un rechazo por otra causa", ruta=ruta,
                fixture=self.identificador)
        return {
            "propiedad": self.propiedad,
            "ruta": ruta,
            "clases": clases,
            "puntos": puntos,
            "letras": sorted({m["letra"] for m in mutaciones}),
        }


# ===========================================================================
#  UNDÉCIMO ÁRBOL, PUERTA 1 · `T1-01` · la mutación se saca del perímetro
# ===========================================================================
class MutacionQueSeSacaDelPerimetro(Ataque):
    """La mutación convierte el fichero en algo que cumple el predicado de bytecode."""

    ordinal = "UNDÉCIMO"
    hallazgo = "T1-01"
    identificador = "undecimo-mutacion-fuera-del-perimetro"
    propiedad = ("la ZONA se determina por la RUTA y la mutación se juzga SIEMPRE: un "
                 "fichero gobernado NO puede eximirse cambiando su propio contenido, y su "
                 "clase de zona es la misma en el árbol sano y en el atacado")
    punto = "V6-05"
    version = versiones.PERIMETRO_ANTES_QUE_MUTACION

    RUTA = "docs/canonico/00-EMPEZAR-AQUI.md"

    def aplicar(self, raiz, canal):
        anterior = _leer(raiz, self.RUTA)
        cuerpo = anterior.decode("utf-8") + SENTENCIA_ACENTUADA
        _escribir(raiz, self.RUTA, b"\x0d\x0d\r\n" + cuerpo.encode("latin-1", "replace"))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "ataque undecimo arbol puerta 1")
        return {"ruta": self.RUTA, "anterior": anterior, "porcelain": _porcelain(raiz)}

    def aplicar_control_positivo(self, raiz, canal):
        # Se retira el ingrediente: el MISMO payload en UTF-8 llano, que sí decodifica.
        anterior = _leer(raiz, self.RUTA)
        cuerpo = anterior.decode("utf-8") + SENTENCIA_ACENTUADA
        _escribir(raiz, self.RUTA, cuerpo.encode("utf-8"))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "control positivo undecimo puerta 1")
        return {"ruta": self.RUTA}

    def control_del_ataque(self, sano, atacado, datos):
        ruta = datos["ruta"]
        crudo_sano = _leer(sano, ruta)
        crudo_atacado = _leer(atacado, ruta)
        if crudo_sano is None or crudo_atacado is None:
            raise AtaqueInerte(
                "la ruta del ataque tiene que existir en el sano y en el atacado", ruta=ruta,
                fixture=self.identificador)
        if crudo_sano == crudo_atacado:
            raise AtaqueInerte(
                "el contenido no cambió: el ataque no se aplicó", ruta=ruta,
                fixture=self.identificador)
        if not versiones.es_bytecode_por_contenido(atacado, ruta):
            raise AtaqueInerte(
                "el cuerpo del fichero atacado SÍ decodifica como UTF-8, luego no cumple "
                "el PREDICADO DE BYTECODE y el ataque de `T1-01` no se está reproduciendo",
                ruta=ruta, fixture=self.identificador)
        if versiones.es_bytecode_por_contenido(sano, ruta):
            raise AtaqueInerte(
                "el fichero SANO ya cumplía el predicado de bytecode: el sano y el atacado "
                "difieren en lo que el ataque dice cambiar", ruta=ruta,
                fixture=self.identificador)
        return {"diferencia": "el cuerpo atacado deja de decodificar como UTF-8",
                "predicado_de_bytecode_en_el_atacado": True,
                "predicado_de_bytecode_en_el_sano": False,
                "porcelain_vacio": not datos["porcelain"]}

    def comprobar_propiedad(self, veredicto, datos):
        ruta = datos["ruta"]
        mutaciones = self._mutaciones_de(veredicto, ruta)
        if not mutaciones:
            raise ReproduccionInvalida(
                "la ruta mutada NO llegó al juicio: el perímetro vigente la estaría "
                "excluyendo por su contenido de hoy", ruta=ruta,
                fixture=self.identificador)
        hallazgos = self._exigir_hallazgo(veredicto, ruta, "la mutación")
        zonas = sorted({h.zona for h in hallazgos})
        if datos.get("zona_en_el_sano") and zonas != [datos["zona_en_el_sano"]]:
            raise ReproduccionInvalida(
                "la clase de zona de la ruta CAMBIÓ con su contenido: la clasificación "
                "vigente no puede depender del cuerpo del fichero", ruta=ruta,
                fixture=self.identificador, zonas=zonas)
        return {
            "propiedad": self.propiedad,
            "ruta": ruta,
            "zona": zonas[0] if zonas else "",
            "clasificada_por_la_ruta": True,
            "puntos": sorted({h.punto for h in hallazgos}),
        }


# ===========================================================================
#  UNDÉCIMO ÁRBOL, PUERTA 2 · `T1-02` · borrar un documento y confirmarlo
# ===========================================================================
class BorradoConfirmadoDeUnDocumento(Ataque):
    """Se borra un documento del corpus y se confirma. La resta antigua queda vacía."""

    ordinal = "UNDÉCIMO"
    hallazgo = "T1-02"
    identificador = "undecimo-borrado-confirmado"
    propiedad = ("un BORRADO es una mutación de pleno derecho: la letra `D` de una ruta "
                 "gobernada da ROJO aunque el borrado esté CONFIRMADO")
    punto = "V6-06"
    version = versiones.BORRADO_TRAS_CONFIRMAR

    RUTA = "docs/canonico/01-MODELO-DEL-SISTEMA.md"

    def preparar(self, raiz, canal):
        _escribir(raiz, self.RUTA, b"# modelo del sistema\n\ncuerpo de la sede\n")
        return True

    def aplicar(self, raiz, canal):
        os.remove(os.path.join(raiz, self.RUTA))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "ataque undecimo arbol puerta 2")
        return {"ruta": self.RUTA, "porcelain": _porcelain(raiz)}

    def aplicar_control_positivo(self, raiz, canal):
        # Se retira el ingrediente: el MISMO borrado SIN confirmar.
        os.remove(os.path.join(raiz, self.RUTA))
        return {"ruta": self.RUTA}

    def control_del_ataque(self, sano, atacado, datos):
        ruta = datos["ruta"]
        if _leer(sano, ruta) is None:
            raise AtaqueInerte(
                "el documento que el ataque borra no existe en el árbol SANO: el fixture "
                "no estaría borrando nada", ruta=ruta, fixture=self.identificador)
        if _leer(atacado, ruta) is not None:
            raise AtaqueInerte(
                "el documento sigue en el árbol atacado: el borrado no se aplicó",
                ruta=ruta, fixture=self.identificador)
        if datos["porcelain"]:
            raise AtaqueInerte(
                "el borrado quedó SIN CONFIRMAR: el ingrediente de `T1-02` es justamente "
                "el `git commit`", ruta=ruta, fixture=self.identificador)
        return {"diferencia": "el documento existe en el sano y NO en el atacado",
                "porcelain_vacio": True}

    def comprobar_propiedad(self, veredicto, datos):
        ruta = datos["ruta"]
        mutaciones = self._mutaciones_de(veredicto, ruta)
        letras = sorted({m["letra"] for m in mutaciones})
        if "D" not in letras:
            raise ReproduccionInvalida(
                "el borrado confirmado no produjo la letra `D`: la desaparición no se "
                "está viendo", ruta=ruta, fixture=self.identificador, letras=letras)
        hallazgos = self._exigir_hallazgo(veredicto, ruta, "el borrado")
        return {
            "propiedad": self.propiedad,
            "ruta": ruta,
            "letras": letras,
            "referencias": sorted({m["referencia"] for m in mutaciones}),
            "puntos": sorted({h.punto for h in hallazgos}),
        }


ATAQUES = (
    SufijoDeBytecodeEnLaSedeDelOwner(),
    SegundaSedeNormativaConfirmada(),
    RutaNoAsciiEnElKernel(),
    MutacionDeUnPreexistente(),
    MutacionQueSeSacaDelPerimetro(),
    BorradoConfirmadoDeUnDocumento(),
)


def por_ordinal():
    """Los ataques agrupados por el ORDINAL del árbol que reproducen."""
    salida = {}
    for ataque in ATAQUES:
        salida.setdefault(ataque.ordinal, []).append(ataque)
    return salida
