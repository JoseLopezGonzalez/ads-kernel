#!/usr/bin/env python3
"""versiones — las VERSIONES HISTÓRICAS VULNERABLES, una por propiedad atacada.

Cada árbol adversarial del conjunto de `V6-15` atacó **una propiedad concreta** de una
implementación concreta. Reproducir el árbol contra la implementación VIGENTE demuestra que
hoy da ROJO; no demuestra que el ataque fuera real. Para eso hace falta la otra mitad: la
versión con la propiedad DEBILITADA tal y como estaba cuando el gate la derribó, que ACEPTA
el mismo árbol. Con las dos, la fila de la matriz significa algo.

DECISIÓN · se REPRODUCE la regla, no se edita el script antiguo
    `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` es evidencia de
    proceso e INMUTABLE, y además está clasificado `EVIDENCIA` por el registro canónico. Lo
    que se reproduce aquí es su REGLA, con la línea y el documento de los que sale, de modo
    que lo que se compara son REGLAS y no versiones de un fichero. Es el mismo criterio que
    `pruebas/test_admision.py` ya adoptó para la regla que `S1-02` derribó.

DECISIÓN · las versiones vulnerables NO usan el canal único de Git, y es deliberado
    `gobierno/git.py` fija `core.quotePath=false`, prohíbe leer listas sin `-z` y construye
    un entorno hermético. Una versión histórica que pasara por ese canal **no podría
    reproducir su propio defecto**: `S1-01` existe precisamente porque la lectura NO iba por
    ahí. Por eso este módulo abre su propio proceso de Git, con la configuración POR DEFECTO,
    y lo declara. `admision/censo.py` deriva su censo sobre `admision`, `gobierno`,
    `adaptadores` e `identidad`, y este paquete no está entre ellos: la vía histórica no se
    cuela en el canal del verificador, y una petición de integración propone que el censo
    barra también este paquete con su sede declarada.

DECISIÓN · cada versión trae su CONTROL POSITIVO, y sin él no se publica su fila
    Una versión vulnerable que dijera VERDE a todo no demostraría nada: sería un `return
    "VERDE"` con adornos. Cada una declara el INGREDIENTE del ataque —el sufijo `.pyc`, el
    `git commit`, el carácter no ASCII, la mutación de un preexistente, el cuerpo que no
    decodifica, el borrado confirmado— y la suite comprueba que **sin ese ingrediente la
    misma versión da ROJO**. Es lo que los gates llamaron «control positivo» y publicaron en
    la misma corrida.
"""
from __future__ import annotations

import os
import re
import subprocess

# ---------------------------------------------------------------------------
#  Lectura de Git de la ÉPOCA. Sin `-z`, sin `core.quotePath=false`, con `.split()`.
#  Es el defecto de `S1-01` conservado a propósito; ver la DECISIÓN de arriba.
# ---------------------------------------------------------------------------
_ENTORNO_HISTORICO = {
    "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "GIT_CONFIG_GLOBAL": os.devnull,
    "GIT_CONFIG_SYSTEM": os.devnull,
    "GIT_TERMINAL_PROMPT": "0",
}


def _git_historico(raiz, *argumentos):
    """`git` con la configuración POR DEFECTO. `core.quotePath` queda ACTIVO, como entonces."""
    entorno = dict(_ENTORNO_HISTORICO)
    entorno["HOME"] = raiz
    proceso = subprocess.run(
        ["git", "-C", raiz] + list(argumentos),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=entorno, check=False,
    )
    return proceso.returncode, proceso.stdout.decode("utf-8", "replace")


def _rutas_por_split(raiz, *argumentos):
    """La lectura de lista de la época: `--name-only` y `.split()` sobre blancos."""
    _, salida = _git_historico(raiz, *argumentos)
    return salida.split()


def _disco(raiz, excluido=None):
    """Los ficheros del árbol de trabajo, podados por el perímetro que se le pase."""
    salida = set()
    for carpeta, subcarpetas, ficheros in os.walk(raiz):
        if ".git" in subcarpetas:
            subcarpetas.remove(".git")
        for nombre in ficheros:
            relativa = os.path.relpath(os.path.join(carpeta, nombre), raiz)
            relativa = relativa.replace(os.sep, "/")
            if excluido is not None and excluido(raiz, relativa):
                continue
            salida.add(relativa)
    return salida


def _publicado(raiz, revision, excluido=None):
    """Las rutas versionadas en una revisión, leídas con `-z` (aquí la lectura no es el punto)."""
    entorno = dict(_ENTORNO_HISTORICO)
    entorno["HOME"] = raiz
    proceso = subprocess.run(
        ["git", "-C", raiz, "ls-tree", "-r", "-z", "--name-only", revision],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=entorno, check=False,
    )
    crudo = proceso.stdout
    rutas = set()
    for trozo in crudo.split(b"\0"):
        if not trozo:
            continue
        ruta = trozo.decode("utf-8", "surrogateescape")
        if excluido is not None and excluido(raiz, ruta):
            continue
        rutas.add(ruta)
    return rutas


# ---------------------------------------------------------------------------
#  Los PERÍMETROS históricos
# ---------------------------------------------------------------------------
#  El literal del OCTAVO ÁRBOL, transcrito del documento 26 §2:
#      _EXCLUIDO = re.compile(r"(?:^|/)\.git(?:/|$)|\.py[co]$")
#  Excluye POR NOMBRE de directorio y POR EXTENSIÓN. `DD-01` ordenó sustituirlo por una
#  exclusión POR NATURALEZA: `.git` sólo en la raíz, y el bytecode por CONTENIDO.
_EXCLUIDO_POR_EXTENSION = re.compile(r"(?:^|/)\.git(?:/|$)|\.py[co]$")


def _perimetro_por_extension(raiz, ruta):
    """El perímetro del OCTAVO ÁRBOL: excluye por nombre y por EXTENSIÓN."""
    return bool(_EXCLUIDO_POR_EXTENSION.search(ruta))


def _perimetro_por_contenido(raiz, ruta):
    """El perímetro POSTERIOR a `DD-01`: `.git` en la raíz y bytecode POR CONTENIDO.

    `S1-05` midió que el predicado de bytecode es FABRICABLE —«un documento en Latin-1 lo
    satisface y se lee sin problema»— y esta es la puerta del UNDÉCIMO ÁRBOL: el predicado se
    evalúa sobre el CONTENIDO DE HOY del fichero mutado, y el filtro corre ANTES de la guarda.
    """
    if ruta == ".git" or ruta.startswith(".git/"):
        return True
    return es_bytecode_por_contenido(raiz, ruta)


def es_bytecode_por_contenido(raiz, ruta):
    """El predicado de bytecode POR CONTENIDO, tal y como `DD-01` lo dejó y `S1-05` lo midió.

    Lee el fichero DEL DISCO y lo declara bytecode si su cuerpo no es texto decodificable.
    Ese es exactamente el ingrediente que el octavo gate aisló: «el ÚNICO ingrediente que
    separa el rojo del verde es que el cuerpo no decodifique como UTF-8».
    """
    completa = os.path.join(raiz, ruta)
    if not os.path.isfile(completa) or os.path.islink(completa):
        return False
    with open(completa, "rb") as manejador:
        crudo = manejador.read()
    if not crudo:
        return False
    try:
        crudo.decode("utf-8", "strict")
    except UnicodeDecodeError:
        return True
    return False


# ---------------------------------------------------------------------------
#  La VERSIÓN, con su procedencia documental
# ---------------------------------------------------------------------------
class VersionVulnerable:
    """Una implementación histórica con UNA propiedad debilitada, y su procedencia."""

    def __init__(self, identificador, propiedad_debilitada, procedencia, ingrediente,
                 juicio):
        self.identificador = identificador
        self.propiedad_debilitada = propiedad_debilitada
        self.procedencia = dict(procedencia)
        self.ingrediente = ingrediente
        self._juicio = juicio

    def juzgar(self, raiz, base, admitidas=()):
        """Emite el veredicto de la versión histórica. `VERDE` o `ROJO`, nunca otra cosa."""
        return self._juicio(raiz, base, tuple(admitidas))

    def a_dict(self):
        return {
            "version": self.identificador,
            "propiedad_debilitada": self.propiedad_debilitada,
            "procedencia": {clave: self.procedencia[clave]
                            for clave in sorted(self.procedencia)},
            "ingrediente_del_ataque": self.ingrediente,
        }

    def __repr__(self):
        return "VersionVulnerable(" + self.identificador + ")"


def _veredicto(color, **detalle):
    salida = {"color": color}
    salida.update({clave: detalle[clave] for clave in sorted(detalle)})
    return salida


# ---------------------------------------------------------------------------
#  1 · OCTAVO ÁRBOL · el perímetro excluye por EXTENSIÓN
# ---------------------------------------------------------------------------
def _juicio_perimetro_por_extension(raiz, base, admitidas):
    universo = _disco(raiz, _perimetro_por_extension) | _publicado(
        raiz, "HEAD", _perimetro_por_extension)
    gobernada = _publicado(raiz, base, _perimetro_por_extension)
    ampliaciones = sorted((universo - gobernada) - set(admitidas))
    if ampliaciones:
        return _veredicto("ROJO", ampliaciones=ampliaciones,
                          universo=len(universo),
                          causa="ampliación sin clasificar")
    return _veredicto("VERDE", ampliaciones=[], universo=len(universo),
                      causa="")


PERIMETRO_POR_EXTENSION = VersionVulnerable(
    identificador="perimetro-excluye-por-extension",
    propiedad_debilitada=(
        "el PERÍMETRO del universo gobernado se deriva excluyendo POR NOMBRE y POR "
        "EXTENSIÓN, de modo que quien controla el nombre controla lo que el ancla ve"
    ),
    procedencia={
        "documento": "docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md",
        "cabecera": "## 2 · EL OCTAVO ÁRBOL, QUE LO ENCONTRÓ EL ADJUDICADOR Y NO LOS REVISORES",
        "hallazgo": "DD-01",
        "literal": r'_EXCLUIDO = re.compile(r"(?:^|/)\.git(?:/|$)|\.py[co]$")',
    },
    ingrediente="el sufijo de bytecode en el NOMBRE de un documento gobernado",
    juicio=_juicio_perimetro_por_extension,
)


# ---------------------------------------------------------------------------
#  2 · NOVENO ÁRBOL · la guarda de admisión se evalúa contra `HEAD`
# ---------------------------------------------------------------------------
def _juicio_guarda_contra_head(raiz, base, admitidas):
    """La guarda mira sólo lo que AÚN NO ESTÁ en `HEAD`. Confirmar la vuelve inerte."""
    universo = _disco(raiz, _perimetro_por_extension)
    publicado = _publicado(raiz, "HEAD", _perimetro_por_extension)
    ampliaciones = sorted((universo - publicado) - set(admitidas))
    if ampliaciones:
        return _veredicto("ROJO", ampliaciones=ampliaciones,
                          referencia="HEAD",
                          causa="ampliación sin clasificar respecto de `HEAD`")
    return _veredicto("VERDE", ampliaciones=[], referencia="HEAD", causa="")


GUARDA_CONTRA_HEAD = VersionVulnerable(
    identificador="guarda-de-admision-contra-head",
    propiedad_debilitada=(
        "la GUARDA DE ADMISIÓN se evalúa contra `HEAD` y no contra la REVISIÓN BASE: es "
        "INERTE sobre todo lo ya confirmado, y `git commit` la apaga"
    ),
    procedencia={
        "documento": "docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md",
        "cabecera": ("## 2 · EL NOVENO ÁRBOL, Y LO ENCONTRÓ UN REVISOR Y LO REPRODUJO EL "
                     "ADJUDICADOR"),
        "hallazgo": "R1-01",
        "literal": "`_nuevos = sorted(f for f in _disco - _publicado …)`",
    },
    ingrediente="`git add -A && git commit`, sin un solo flag",
    juicio=_juicio_guarda_contra_head,
)


# ---------------------------------------------------------------------------
#  3 · DÉCIMO ÁRBOL, EJE 1 · una lectura de lista sin `-z`
# ---------------------------------------------------------------------------
PREFIJO_VIGILADO = "kernel/"


def _juicio_lista_sin_separador(raiz, base, admitidas):
    """`git diff --name-only` + `.split()`: `core.quotePath` cita la ruta y se pierde."""
    tocados = _rutas_por_split(raiz, "diff", "--name-only", base, "HEAD")
    del_kernel = [ruta for ruta in tocados if ruta.startswith(PREFIJO_VIGILADO)]
    sin_declarar = sorted(set(del_kernel) - set(admitidas))
    if sin_declarar:
        return _veredicto("ROJO", del_kernel=sorted(del_kernel),
                          enumerados=len(del_kernel), leidos=sorted(tocados),
                          causa="fichero de `kernel/` tocado y no enumerado")
    # Publica su recuento, y ése es el recuento FALSO que `S1-01` midió.
    return _veredicto("VERDE", del_kernel=sorted(del_kernel),
                      enumerados=len(del_kernel), leidos=sorted(tocados), causa="")


LISTA_SIN_SEPARADOR_SEGURO = VersionVulnerable(
    identificador="lectura-de-lista-sin-separador-seguro",
    propiedad_debilitada=(
        "una de las lecturas de LISTA de Git conserva `--name-only` y `.split()`: con "
        "`core.quotePath` activo, una ruta no ASCII llega CITADA, deja de empezar por su "
        "prefijo y desaparece del inventario, que además publica un recuento falso"
    ),
    procedencia={
        "documento": "docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md",
        "cabecera": "## 3 · EL DÉCIMO ÁRBOL, Y ESTA VEZ SON DOS EJES DISTINTOS",
        "hallazgo": "S1-01",
        "literal": '_tocados_raw = _git("diff","--name-only", …) · tocados = _tocados_raw.split()',
    },
    ingrediente="un carácter no ASCII en la ruta",
    juicio=_juicio_lista_sin_separador,
)


# ---------------------------------------------------------------------------
#  4 · DÉCIMO ÁRBOL, EJE 2 · el universo se deriva por EXISTENCIA y no por CONTENIDO
# ---------------------------------------------------------------------------
def _juicio_universo_por_existencia(raiz, base, admitidas):
    """`_ampliaciones = (disco ∪ publicado) − base`: sólo TOPOLOGÍA. El contenido no se mira."""
    disco = _disco(raiz, _perimetro_por_extension)
    publicado = _publicado(raiz, "HEAD", _perimetro_por_extension)
    gobernada = _publicado(raiz, base, _perimetro_por_extension)
    ampliaciones = sorted(((disco | publicado) - gobernada) - set(admitidas))
    idos = sorted(gobernada - (disco | publicado))
    if ampliaciones or idos:
        return _veredicto("ROJO", ampliaciones=ampliaciones, idos=idos,
                          causa="topología alterada respecto de la revisión base")
    return _veredicto("VERDE", ampliaciones=[], idos=[], causa="")


UNIVERSO_POR_EXISTENCIA = VersionVulnerable(
    identificador="universo-derivado-por-existencia",
    propiedad_debilitada=(
        "el universo gobernado se deriva por EXISTENCIA —qué ficheros aparecen y "
        "desaparecen— y no por CONTENIDO: un fichero que YA EXISTÍA en la revisión base no "
        "es ampliación diga lo que diga hoy"
    ),
    procedencia={
        "documento": "docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md",
        "cabecera": "## 3 · EL DÉCIMO ÁRBOL, Y ESTA VEZ SON DOS EJES DISTINTOS",
        "hallazgo": "S1-02",
        "literal": "_ampliaciones = (_disco ∪ _publicado) − _base_gobernada",
    },
    ingrediente="mutar un fichero PREEXISTENTE en vez de crear uno nuevo",
    juicio=_juicio_universo_por_existencia,
)


# ---------------------------------------------------------------------------
#  5 · UNDÉCIMO ÁRBOL, PRIMERA PUERTA · el perímetro se evalúa ANTES que la mutación
# ---------------------------------------------------------------------------
def _juicio_perimetro_antes_que_mutacion(raiz, base, admitidas):
    """`if not _en_zona(_f): continue` — y `_en_zona` mira el CONTENIDO DE HOY."""
    _, salida = _git_historico(raiz, "diff", "--name-status", "-z", base, "HEAD")
    mutadas = []
    trozos = [t for t in salida.split("\0") if t]
    indice = 0
    while indice + 1 < len(trozos):
        letra = trozos[indice][0]
        if letra in ("R", "C"):
            ruta = trozos[indice + 2] if indice + 2 < len(trozos) else trozos[indice + 1]
            indice += 3
        else:
            ruta = trozos[indice + 1]
            indice += 2
        # AQUÍ está la puerta: el perímetro corre ANTES de juzgar la mutación, y se evalúa
        # sobre el contenido de HOY del fichero mutado.
        if _perimetro_por_contenido(raiz, ruta):
            continue
        if ruta in admitidas:
            continue
        mutadas.append((letra, ruta))
    if mutadas:
        return _veredicto("ROJO", mutadas=[letra + " " + ruta for letra, ruta in mutadas],
                          causa="mutación de una ruta gobernada sin admitir")
    return _veredicto("VERDE", mutadas=[], causa="")


PERIMETRO_ANTES_QUE_MUTACION = VersionVulnerable(
    identificador="perimetro-evaluado-antes-que-la-mutacion",
    propiedad_debilitada=(
        "el PERÍMETRO se evalúa sobre el CONTENIDO DE HOY y corre ANTES de la guarda: una "
        "mutación que convierte un fichero gobernado en algo que cumple el predicado de "
        "bytecode SE EXIME A SÍ MISMA de la guarda que juzga esa misma mutación"
    ),
    procedencia={
        "documento": "docs/evolucion/29-OCTAVO-GATE-DE-CERTIFICACION-F4C.md",
        "cabecera": "## 2 · EL UNDÉCIMO ÁRBOL, Y ESTA VEZ LO CONSTRUYÓ EL ADJUDICADOR",
        "hallazgo": "T1-01",
        "literal": "if not _en_zona(_f): continue   ·   _en_zona → _es_bytecode(DEL DISCO)",
    },
    ingrediente="un cuerpo que NO decodifica como UTF-8",
    juicio=_juicio_perimetro_antes_que_mutacion,
)


# ---------------------------------------------------------------------------
#  6 · UNDÉCIMO ÁRBOL, SEGUNDA PUERTA · el borrado confirmado no se ve
# ---------------------------------------------------------------------------
def _juicio_borrado_tras_confirmar(raiz, base, admitidas):
    """`_idos = _publicado − _disco`: vacío en cuanto se confirma, porque `_publicado` es `HEAD`."""
    disco = _disco(raiz, _perimetro_por_contenido)
    publicado = _publicado(raiz, "HEAD", _perimetro_por_contenido)
    gobernada = _publicado(raiz, base, _perimetro_por_contenido)
    # `_ampliacion_admitida` se consulta ANTES de la rama `D`, y para un documento numerado
    # sus condiciones las satisface trivialmente un fichero BORRADO. Se reproduce con la
    # forma que tenía: toda ruta admitida sale del bucle antes de llegar a la rama `D`.
    ampliaciones = sorted(((disco | publicado) - gobernada) - set(admitidas))
    idos = sorted(publicado - disco)
    if ampliaciones or idos:
        return _veredicto("ROJO", ampliaciones=ampliaciones, idos=idos,
                          causa="topología alterada")
    return _veredicto("VERDE", ampliaciones=[], idos=[], causa="")


BORRADO_TRAS_CONFIRMAR = VersionVulnerable(
    identificador="borrado-invisible-tras-confirmar",
    propiedad_debilitada=(
        "la desaparición se mide con `_idos = _publicado − _disco`, y `_publicado` sale de "
        "`HEAD`: en cuanto el borrado se confirma la resta es vacía y la sede desaparece "
        "en silencio"
    ),
    procedencia={
        "documento": "docs/evolucion/29-OCTAVO-GATE-DE-CERTIFICACION-F4C.md",
        "cabecera": "## 2 · EL UNDÉCIMO ÁRBOL, Y ESTA VEZ LO CONSTRUYÓ EL ADJUDICADOR",
        "hallazgo": "T1-02",
        "literal": "_idos = sorted(_publicado - _disco)",
    },
    ingrediente="confirmar el borrado con `git commit`",
    juicio=_juicio_borrado_tras_confirmar,
)


VERSIONES = (
    PERIMETRO_POR_EXTENSION,
    GUARDA_CONTRA_HEAD,
    LISTA_SIN_SEPARADOR_SEGURO,
    UNIVERSO_POR_EXISTENCIA,
    PERIMETRO_ANTES_QUE_MUTACION,
    BORRADO_TRAS_CONFIRMAR,
)


def por_identificador(identificador):
    for version in VERSIONES:
        if version.identificador == identificador:
            return version
    raise KeyError(identificador)
