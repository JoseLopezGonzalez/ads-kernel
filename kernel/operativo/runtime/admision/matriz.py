#!/usr/bin/env python3
"""matriz — la matriz adversarial completa. Corte `V5` · `V6-13`, `V6-14` y `V6-18`.

  `V6-13`  UTF-8 · Latin-1 inválido · espacios · saltos de línea · guiones iniciales ·
           Unicode. Cierre: las **seis** formas con fixture POSITIVO y NEGATIVO.
  `V6-14`  adición, modificación, borrado, renombrado, copia y cambio de tipo. Cierre: las
           **seis** con fixture POSITIVO y NEGATIVO.
  `V6-18`  Cierre: `falsos_verdes = 0` **y** `falsos_rojos = 0`, **medidos y publicados**.

DECISIÓN · la matriz construye REPOSITORIOS GIT REALES, no simulacros
    Alternativas: (a) fabricar salidas de Git y pasárselas al lector; (b) construir
    repositorios de verdad.
    Se elige (b). Una salida fabricada la escribe quien escribe el control, así que el
    control mide su propia idea de Git y no Git. La mitad de los vectores del expediente
    —`core.quotePath`, la detección de copias, el comportamiento de `-z` con un salto de
    línea en el nombre— sólo aparecen con Git de verdad. El coste es que la matriz tarda; el
    beneficio es que lo que mide existe.

DECISIÓN · CADA control declara su color esperado ANTES de ejecutarse
    Un control que decide si aprobó después de mirar el resultado no puede producir un falso
    verde por definición, y por eso no mide nada. Aquí `esperado` es un dato de la fila y
    `falsos_verdes` / `falsos_rojos` se derivan comparándolo con el color obtenido. Es la
    única forma de que las dos columnas de `V6-18` signifiquen algo.

DECISIÓN · un `INDETERMINADO` cuenta como falso verde si se esperaba ROJO
    Un veredicto que no es rojo cuando debía serlo es un falso verde, se llame como se
    llame. Contarlo aparte habría creado un tercer casillero donde esconder fallos.
"""
from __future__ import annotations

import os
import shutil

from . import verificar
from . import perimetro
from .perimetro import Declaracion

# ===========================================================================
#  Las SEIS formas de nombre y codificación de `V6-13`
# ===========================================================================
#  `contenido_latin1` marca la fila cuyo fixture es de CONTENIDO y no de nombre: es el
#  vector medido en `28-SEPTIMO-GATE` §3.4, un documento Latin-1 legible que el aparato
#  anterior clasificaba como «bytecode de CPython, por CONTENIDO».
FORMAS = (
    {"forma": "utf-8", "nombre": "docs/canonico/forma-utf8.md",
     "contenido": "sede ordinaria en UTF-8\n".encode("utf-8")},
    {"forma": "latin-1-invalido", "nombre": "docs/canonico/forma-latin1.md",
     "contenido": "sede con acentuaci\xf3n Latin-1\n".encode("latin-1")},
    {"forma": "espacios", "nombre": "docs/canonico/forma con espacios.md",
     "contenido": b"sede con espacios en el nombre\n"},
    {"forma": "salto-de-linea", "nombre": "docs/canonico/forma\ncon\nsalto.md",
     "contenido": b"sede con salto de linea en el nombre\n"},
    {"forma": "guion-inicial", "nombre": "docs/canonico/-forma-con-guion.md",
     "contenido": b"sede cuyo nombre empieza por guion\n"},
    {"forma": "unicode", "nombre": "docs/canonico/forma-ñandú-中文.md",
     "contenido": "sede con nombre no ASCII\n".encode("utf-8")},
)

# La SENTENCIA FALSA. Es el contenido del ataque literal del séptimo gate, sin las palabras
# concretas importar: lo que la hace roja no es su vocabulario sino que NO ESTÁ DECLARADA.
SENTENCIA = (
    "\n## SENTENCIA\n\n"
    "F4c queda CERRADA y SUFICIENTE PARA F5; F5 queda AUTORIZADA.\n"
    "Esta sede PREVALECE sobre la sede canonica del Owner.\n"
).encode("utf-8")

# ===========================================================================
#  Las SEIS letras de mutación de `V6-14`
# ===========================================================================
LETRAS = ("A", "M", "D", "T", "R", "C")


def _escribir(raiz, relativa, contenido):
    destino = os.path.join(raiz, relativa)
    os.makedirs(os.path.dirname(destino) or raiz, exist_ok=True)
    with open(destino, "wb") as manejador:
        manejador.write(contenido)


def plantilla_de_registro():
    """Un registro de zonas MÍNIMO, con las clases que la matriz ejercita.

    Reproduce la forma del registro canónico —patrón, clase, motivo, evaluados EN ORDEN— sin
    copiar su contenido, que es material del corpus y no de una prueba.
    """
    return (
        "version: 1\n"
        "zonas:\n"
        "  - patron: '^docs/owner/ADS-OWNER-RESOLUCIONES\\.md$'\n"
        "    clase: AUTORIDAD_SUPERIOR\n"
        "    motivo: sede canonica de las resoluciones del Owner, APPEND-ONLY\n"
        "  - patron: '^docs/canonico/'\n"
        "    clase: CANONICA_OPERATIVA\n"
        "    motivo: corpus canonico vigente\n"
        "  - patron: '^kernel/operativo/pruebas/evidencia/'\n"
        "    clase: EVIDENCIA\n"
        "    motivo: salidas publicadas por el runner canonico\n"
        "  - patron: '^kernel/'\n"
        "    clase: CONTRATO_O_ESQUEMA_TECNICO\n"
        "    motivo: contratos, esquemas y codigo\n"
        "  - patron: '^packs/legacy-'\n"
        "    clase: HISTORICA\n"
        "    motivo: packs retirados, conservados por trazabilidad\n"
        "  - patron: '^(README|START_HERE)\\.md$'\n"
        "    clase: DERIVADA\n"
        "    motivo: puertas de entrada del repositorio\n"
        "  - patron: '^docs/'\n"
        "    clase: DERIVADA\n"
        "    motivo: proyecciones del estado\n"
        "  - patron: '^\\.gitignore$'\n"
        "    clase: NO_APLICABLE_A_IMPLEMENTACION\n"
        "    motivo: configuracion de herramienta\n"
    ).encode("utf-8")


def fundar(raiz, canal_de_gobierno):
    """Funda el árbol base de la matriz y devuelve el commit base. Sin red, sin config."""
    os.makedirs(raiz, exist_ok=True)
    canal_de_gobierno.ejecutar("init", "--quiet", "--initial-branch=canonica")
    _escribir(raiz, "README.md", b"# puerta de entrada\n")
    _escribir(raiz, "START_HERE.md", b"# por donde empezar\n")
    _escribir(raiz, ".gitignore", b"__pycache__/\n")
    _escribir(raiz, "docs/canonico/FUENTES-CANONICAS.yml", plantilla_de_registro())
    _escribir(raiz, "docs/canonico/00-EMPEZAR-AQUI.md", b"# empezar\n")
    _escribir(raiz, "docs/owner/ADS-OWNER-RESOLUCIONES.md",
              b"# resoluciones\n\n## O1\n\ntexto publicado\n")
    _escribir(raiz, "kernel/operativo/pruebas/evidencia/fuentes-salida.txt",
              b"salida publicada por el runner canonico\ncodigo: 0\n")
    _escribir(raiz, "packs/legacy-uno/PACK.md", b"# pack retirado\n")
    _escribir(raiz, "kernel/operativo/contratos/C1.md", b"# contrato\n")
    canal_de_gobierno.ejecutar("add", "-A")
    canal_de_gobierno.ejecutar("commit", "--quiet", "-m", "base")
    return canal_de_gobierno.resolver("HEAD")


def _clonar_arbol(origen, destino):
    shutil.copytree(origen, destino, symlinks=True)


def _controles_de_forma():
    """Doce filas: las seis formas, positiva y negativa."""
    filas = []
    for forma in FORMAS:
        filas.append({
            "familia": "V6-13", "caso": forma["forma"], "signo": "positivo",
            "esperado": "VERDE", "nombre": forma["nombre"],
            "contenido": forma["contenido"], "declarar": True,
        })
        filas.append({
            "familia": "V6-13", "caso": forma["forma"], "signo": "negativo",
            "esperado": "ROJO", "nombre": forma["nombre"],
            "contenido": forma["contenido"] + SENTENCIA, "declarar": False,
        })
    return filas


def _controles_de_mutacion():
    """Doce filas: las seis letras, positiva y negativa."""
    filas = []
    for letra in LETRAS:
        filas.append({"familia": "V6-14", "caso": letra, "signo": "positivo",
                      "esperado": "VERDE", "letra": letra, "declarar": True})
        filas.append({"familia": "V6-14", "caso": letra, "signo": "negativo",
                      "esperado": "ROJO", "letra": letra, "declarar": False})
    return filas


def _aplicar_forma(raiz, canal, fila):
    _escribir(raiz, fila["nombre"], fila["contenido"])
    canal.ejecutar("add", "-A")
    canal.ejecutar("commit", "--quiet", "-m", "forma")
    return [fila["nombre"]] if fila["declarar"] else []


def _aplicar_mutacion(raiz, canal, fila):
    """Produce la letra pedida sobre el árbol, y devuelve las rutas a DECLARAR."""
    letra = fila["letra"]
    sentencia = b"" if fila["declarar"] else SENTENCIA
    tocadas = []
    if letra == "A":
        _escribir(raiz, "docs/canonico/nueva.md", b"# sede nueva\n" + sentencia)
        tocadas = ["docs/canonico/nueva.md"]
    elif letra == "M":
        _escribir(raiz, "docs/canonico/00-EMPEZAR-AQUI.md",
                  b"# empezar\nlinea nueva\n" + sentencia)
        tocadas = ["docs/canonico/00-EMPEZAR-AQUI.md"]
    elif letra == "D":
        os.remove(os.path.join(raiz, "docs/canonico/00-EMPEZAR-AQUI.md"))
        tocadas = ["docs/canonico/00-EMPEZAR-AQUI.md"]
        if sentencia:
            _escribir(raiz, "docs/canonico/sustituta.md", b"# sustituta\n" + sentencia)
    elif letra == "T":
        objetivo = os.path.join(raiz, "docs/canonico/00-EMPEZAR-AQUI.md")
        os.remove(objetivo)
        os.symlink("FUENTES-CANONICAS.yml", objetivo)
        tocadas = ["docs/canonico/00-EMPEZAR-AQUI.md"]
    elif letra == "R":
        # Renombrado PURO, sin tocar el contenido: si se le añade una línea, la similitud
        # baja del umbral y Git deja de emitir `R`, con lo que el fixture dejaría de
        # ejercitar la letra que dice ejercitar. El escenario NEGATIVO de `V6-06` no
        # necesita ninguna sentencia: es «destino admitido y ORIGEN no admitido».
        origen = os.path.join(raiz, "docs/canonico/00-EMPEZAR-AQUI.md")
        with open(origen, "rb") as manejador:
            cuerpo = manejador.read()
        os.remove(origen)
        _escribir(raiz, "docs/canonico/00-RENOMBRADA.md", cuerpo)
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "mutacion-R")
        return (["docs/canonico/00-EMPEZAR-AQUI.md", "docs/canonico/00-RENOMBRADA.md"]
                if fila["declarar"] else ["docs/canonico/00-RENOMBRADA.md"])
    elif letra == "C":
        # Copia PURA, por la misma razón. El negativo declara sólo el destino.
        origen = os.path.join(raiz, "docs/canonico/00-EMPEZAR-AQUI.md")
        with open(origen, "rb") as manejador:
            cuerpo = manejador.read()
        _escribir(raiz, "docs/canonico/00-COPIA.md", cuerpo)
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "mutacion-C")
        return (["docs/canonico/00-EMPEZAR-AQUI.md", "docs/canonico/00-COPIA.md"]
                if fila["declarar"] else ["docs/canonico/00-COPIA.md"])
    canal.ejecutar("add", "-A")
    canal.ejecutar("commit", "--quiet", "-m", "mutacion-" + letra)
    return tocadas if fila["declarar"] else []



# ===========================================================================
#  `V6-18` SOBRE LA SUITE COMPLETA · el bloqueo de `M-04`, medido y cerrado
# ===========================================================================
#  HECHO REPRODUCIDO. `11-ARQ` §20.1 declara de `V6-18`: entrada «**la suite completa**»,
#  evidencia «**la matriz entera, con sus dos columnas**», cierre «*todos los controles
#  sanos en verde y todos los adversariales en rojo*». Y la matriz ejercía DOS familias:
#
#      $ ads_admision.py --repo . matriz
#        controles: 24        falsos_verdes 0    falsos_rojos 0
#        (12 de `V6-13` · 12 de `V6-14` · y ninguna otra)
#
#  Es decir: el número que la condición de cierre de `M-04` nombra —«`V6-18` en verde:
#  cero falsos verdes y cero falsos rojos»— se calculaba sobre **2 de los 19 puntos** de
#  §20.1. Un cero verdadero sobre una población que no es la declarada no acredita lo que
#  la condición pide, que es exactamente la clase de `M-04`: «un árbol defectuoso puede
#  pasar en verde».
#
# DECISIÓN · la población se DERIVA de lo que el verificador puede emitir
#     Alternativas: (a) escribir a mano una fila por cada uno de los 19 puntos de §20.1;
#     (b) derivar del código del verificador qué puntos puede EMITIR como hallazgo, y
#     exigir un adversarial por cada uno.
#     Se elige (b). Con (a) la lista caduca en cuanto el verificador gana o pierde un
#     punto, y volveríamos a tener un cardinal escrito a mano sobre una población que ya no
#     es la suya —que es el defecto de clase que este delta corrige en cinco sitios más—.
#     Con (b), el día que el verificador aprenda a emitir un punto nuevo, la matriz exige
#     su control sin que nadie se acuerde: si falta, `V6-18` no cierra.
#
#     Y hay una consecuencia honesta que se DICE: los puntos de §20.1 que el verificador
#     NO emite como hallazgo —`V6-01`…`V6-03`, `V6-06`…`V6-08` y el propio `V6-18`— no se
#     ejercen aquí porque no hay veredicto suyo que contrastar; los cubren sus baterías, y
#     esta matriz publica cuáles son y por qué, en vez de dejar creer que cubre 19.
def puntos_emitibles(raiz):
    """Los `V6-nn` que el verificador PUEDE emitir, derivados de su código con `ast`.

    No es un `grep`: se recorre el árbol sintáctico de cada módulo de `admision/` y se
    recogen las cadenas literales con forma de punto que aparecen como PRIMER argumento de
    un `Hallazgo(...)`, que es donde el punto se decide. Una cadena que hable de `V6-07` en
    un comentario o en un mensaje no cuenta: lo que cuenta es lo que se emite.
    """
    import ast                                                        # noqa: PLC0415
    import re as _re                                                  # noqa: PLC0415
    paquete = os.path.join(raiz, "kernel", "operativo", "runtime", "admision")
    if not os.path.isdir(paquete):
        paquete = os.path.dirname(os.path.abspath(__file__))
    puntos = set()
    for nombre in sorted(os.listdir(paquete)):
        if not nombre.endswith(".py"):
            continue
        with open(os.path.join(paquete, nombre), encoding="utf-8") as manejador:
            try:
                arbol = ast.parse(manejador.read())
            except SyntaxError:
                continue
        for nodo in ast.walk(arbol):
            if (isinstance(nodo, ast.Constant) and isinstance(nodo.value, str)
                    and _re.match(r"^V6-\d+$", nodo.value)):
                puntos.add(nodo.value)
    return sorted(puntos)


# Lo que la matriz NO ejerce, DICHO y con su motivo. `V6-18` es la propia matriz —no puede
# ser control de sí misma— y `V6-13`/`V6-14` los cubren las dos familias de arriba, control
# a control. El resto entra en la tercera familia y tiene que tener adversarial.
PUNTOS_CUBIERTOS_POR_FAMILIA = {
    "V6-13": "las SEIS formas de nombre y codificación, positiva y negativa",
    "V6-14": "las SEIS letras de mutación, positiva y negativa",
    "V6-18": "es esta misma matriz: no puede ser control de sí misma",
    "V6-05": "lo emiten los NEGATIVOS de `V6-14` para las letras de CONTENIDO, y se mide: "
             "aparece en los `puntos_emitidos` de esas filas",
    "V6-09": "lo emiten los NEGATIVOS de `V6-14` para las letras que no son de contenido",
}

# LO QUE ESTA MATRIZ NO PUEDE EJERCER, Y POR QUÉ. No es una exención: es una propiedad del
# sujeto de esos dos puntos, medida y dicha.
#
#     `RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`
#
# El censo del código —`V6-04` sobre las LECTURAS y `V6-19` sobre las FÓRMULAS— se calcula
# sobre EL APARATO QUE EJECUTA, no sobre el árbol que se juzga. Es correcto: lo que esos
# dos puntos protegen es la pureza del instrumento, y el instrumento es el que corre. Pero
# la consecuencia es que un sabotaje escrito en el árbol bajo prueba les resulta INVISIBLE
# —lo medí: la fila salía ROJO y el punto emitido era `V6-11`, no el suyo—, y ejercerlos
# desde aquí exigiría que la matriz se mutilase a sí misma durante la pasada que juzga,
# que es justo lo que `V6-11` existe para impedir.
#
# Se declara en vez de fabricar un control que parezca cubrirlos. Sus baterías propias sí
# los ejercen —`CensoDeLecturas` y el censo de fórmulas en `test_admision.py`—, y esta
# matriz publica la frontera para que nadie lea sus dos ceros como más de lo que son.
def censo_de_20_1(raiz):
    """El censo de §20.1, DERIVADO del rango que declara `CONTRATO-ADMISION.md`.

    `M5` del verificador independiente de `O30`: el comentario de arriba dice que esta
    matriz «publica cuáles son y por qué» los puntos de §20.1 que no alcanza, y NO los
    publicaba en ninguna parte de su salida. Un lector veía `puntos_sin_tratamiento: []`
    sobre una población derivada de 13 y podía leer cobertura de 19.

    El censo NO se escribe a mano —sería el mismo defecto de clase que este módulo corrige
    en otros cinco sitios— y NO se lee de `11-ARQ`, que por diseño no viaja al proyecto
    instalado. Se lee del contrato, que sí viaja y que declara el rango cerrado.
    """
    contrato = os.path.join(raiz, "kernel", "operativo", "runtime", "CONTRATO-ADMISION.md")
    if not os.path.isfile(contrato):
        return None
    import re as _re                                                  # noqa: PLC0415
    with open(contrato, encoding="utf-8") as fh:
        texto = fh.read()
    m = _re.search(r"`V6-(\d{2})`\s*…\s*`V6-(\d{2})`\s*de\s*`11-ARQ`\s*§20\.1", texto)
    if not m:
        return None
    return ["V6-%02d" % i for i in range(int(m.group(1)), int(m.group(2)) + 1)]


PUNTOS_NO_EJERCIBLES_AQUI = {
    "V6-04": "su sujeto es el aparato que EJECUTA (`RUNTIME`), no el árbol juzgado: un "
             "sabotaje en el árbol bajo prueba le es invisible, y sabotear el aparato "
             "durante la pasada es lo que `V6-11` impide. Lo ejerce `test_admision.py`",
    "V6-19": "mismo sujeto y mismo motivo que `V6-04`, sobre el APARATO DE VERIFICACIÓN",
    "V6-15": "no se emite como hallazgo: es una línea de PROCEDENCIA que el veredicto "
             "publica. Lo ejerce la suite de árboles adversariales",
    "V6-16": "no se emite como hallazgo: es la declaración del paquete SEPARADO de la raíz "
             "externa. Lo ejerce la raíz externa, fuera de este árbol",
}


# ---------------------------------------------------------------------------
#  LA TERCERA FAMILIA · un adversarial POR PUNTO EMITIBLE
# ---------------------------------------------------------------------------
#  Cada fila ataca UN punto y exige que el veredicto lo NOMBRE. No basta con que salga
#  ROJO: un rojo por otro motivo demostraría que el verificador reacciona, no que reacciona
#  a lo que se le pregunta. Es la misma disciplina que el catálogo de negativos aplica con
#  su campo `espera`.
CONTROLES_POR_PUNTO = {

    "V6-10": {
        "motivo": "una ruta que NINGUNA zona del censo clasifica: sin condición de "
                  "contenido declarada, no pasa por omisión",
        "sabotaje": "zona-sin-condicion",
    },
    "V6-11": {
        "motivo": "el propio verificador muta en la pasada que juzga",
        "sabotaje": "instrumento-alterado",
    },
    "V6-12": {
        "motivo": "la sede APPEND-ONLY del Owner alterada en el árbol de trabajo",
        "sabotaje": "sede-del-owner-alterada",
    },
    "V6-17": {
        "motivo": "la declaración llega SIN ancla externa: un digest del propio árbol "
                  "siempre cuadra consigo mismo",
        "sabotaje": "sin-ancla-externa",
        # `V6-17` NO da rojo: da INDETERMINADO, y es lo correcto. Su contrato dice «sin
        # ancla que venga de FUERA, el veredicto NO PUEDE SER VERDE», y un veredicto que
        # no puede emitirse no es un veredicto negativo: es la ausencia de veredicto. Se
        # exige lo que el punto promete, no lo que sería cómodo de contar.
        #
        # Y por eso NO se le exige que NOMBRE su punto: el fallo cerrado ocurre ANTES de
        # que haya hallazgos que emitir —la excepción sube y el veredicto queda
        # indeterminado—, de modo que exigir el nombre sería exigir algo que este camino no
        # puede dar. Lo que acredita a `V6-17` es el color, y se dice.
        "esperado": "INDETERMINADO",
        "acredita_por": "color",
    },

}


def _controles_por_punto():
    """Una fila NEGATIVA por punto emitible que las dos familias no cubren."""
    filas = []
    for punto in sorted(CONTROLES_POR_PUNTO):
        ficha = CONTROLES_POR_PUNTO[punto]
        filas.append({"familia": "suite", "caso": punto, "signo": "negativo",
                      "esperado": ficha.get("esperado", "ROJO"),
                      "punto_exigido": (None if ficha.get("acredita_por") == "color"
                                        else punto),
                      "censar_el_codigo": ficha.get("censar_el_codigo", False),
                      "sabotaje": ficha["sabotaje"], "motivo": ficha["motivo"]})
    return filas


def _aplicar_sabotaje_de_punto(raiz, canal, fila):
    """Produce el ataque de esa fila. Devuelve las rutas a DECLARAR (ninguna: es negativo)."""
    clase = fila["sabotaje"]
    if clase == "lectura-fuera-del-canal":
        # FUERA del instrumento, y no dentro. Puesto en `admision/`, `V6-11` se dispara
        # PRIMERO —«el propio verificador muta en la pasada que juzga»— y tapa a `V6-04`:
        # el rojo salía, pero por otro motivo. El ámbito de `V6-04` es TODO el runtime, así
        # que el ataque va a un paquete del runtime que no es el instrumento.
        _escribir(raiz, "kernel/operativo/runtime/identidad/lectura_colada.py",
                  b"import subprocess\n"
                  b"def leer():\n"
                  b"    return subprocess.run(['git', 'ls-files']).stdout\n")
    elif clase == "zona-sin-condicion":
        _escribir(raiz, "zona-que-nadie-clasifica/fichero.md", b"# fuera de todo censo\n")
    elif clase == "instrumento-alterado":
        _escribir(raiz, "kernel/operativo/runtime/admision/perimetro.py",
                  b"# el instrumento, alterado en la pasada que juzga\n")
    elif clase == "sede-del-owner-alterada":
        _escribir(raiz, perimetro.SEDE_DEL_OWNER,
                  b"# resoluciones\n\n## O1\n\ntexto ALTERADO\n")
    elif clase == "sin-ancla-externa":
        # no se toca el árbol: el ataque va en la DECLARACIÓN, y lo aplica `ejecutar`
        return []
    elif clase == "formula-duplicada":
        # Igual que arriba: el ámbito de `V6-19` es el APARATO de verificación, y sus
        # paquetes son varios. Se elige uno que no sea el instrumento, o `V6-11` gana.
        _escribir(raiz, "kernel/operativo/runtime/gobierno/formula_copiada.py",
                  b"def digest_del_censo(zonas):\n"
                  b"    return 'reimplementada en vez de importada'\n")
    else:
        raise RuntimeError("sabotaje desconocido: " + str(clase))
    canal.ejecutar("add", "-A")
    canal.ejecutar("commit", "--quiet", "-m", "sabotaje " + clase)
    return []

def ejecutar(directorio, *, registro="docs/canonico/FUENTES-CANONICAS.yml"):
    """Ejecuta la matriz entera y publica sus DOS columnas. Devuelve un informe determinista.

    `directorio` tiene que existir y quedar limpio: la matriz crea un árbol plantilla y un
    árbol por control, todos dentro.
    """
    from gobierno.git import CanalGit

    plantilla = os.path.join(directorio, "plantilla")
    canal_plantilla = CanalGit(plantilla)
    os.makedirs(plantilla, exist_ok=True)
    base = fundar(plantilla, canal_plantilla)

    filas = (_controles_de_forma() + _controles_de_mutacion()
             + _controles_por_punto())
    resultados = []
    falsos_verdes = 0
    falsos_rojos = 0
    sin_acreditar = []

    for numero, fila in enumerate(filas):
        arbol = os.path.join(directorio, "c" + str(numero).zfill(3))
        _clonar_arbol(plantilla, arbol)
        canal = CanalGit(arbol)
        if fila["familia"] == "V6-13":
            declarar = _aplicar_forma(arbol, canal, fila)
        elif fila["familia"] == "V6-14":
            declarar = _aplicar_mutacion(arbol, canal, fila)
        else:
            declarar = _aplicar_sabotaje_de_punto(arbol, canal, fila)
        # El ataque de `V6-17` no vive en el árbol sino en la DECLARACIÓN: se le retira el
        # ancla externa, que es exactamente lo que ese punto prohíbe.
        ancla_de_la_fila = None if fila.get("sabotaje") == "sin-ancla-externa" else base
        declaracion = Declaracion(
            ancla=ancla_de_la_fila, autoridad="matriz-adversarial",
            admitidas=[{"ruta": ruta, "motivo": "control positivo declarado"}
                       for ruta in declarar],
        )
        veredicto = verificar(arbol, base=base, declaracion=declaracion,
                              registro=registro,
                              censar_el_codigo=bool(fila.get("censar_el_codigo")))
        obtenido = veredicto.color
        puntos_emitidos = sorted({h.punto for h in veredicto.hallazgos})
        acierta = obtenido == fila["esperado"]
        # UN ROJO POR OTRO MOTIVO NO ACREDITA NADA. Cuando la fila exige un punto, el
        # veredicto tiene que NOMBRARLO: si no, el verificador ha reaccionado a otra cosa
        # y el control estaría midiendo que el aparato se queja, no que se queja de esto.
        exigido = fila.get("punto_exigido")
        if acierta and exigido and exigido not in puntos_emitidos:
            acierta = False
        if not acierta:
            if fila["esperado"] == "VERDE":
                # se esperaba VERDE y no lo fue: el aparato se queja de algo permitido
                falsos_rojos += 1
            elif obtenido == "VERDE":
                # se esperaba que NO fuera verde, y lo es: eso es un falso verde
                falsos_verdes += 1
            else:
                # ni verde esperado ni verde obtenido: el control no acredita su punto.
                # No es un falso verde —nada pasó indebidamente— pero tampoco vale, y
                # contarlo como falso verde mentiría sobre lo que ocurrió.
                sin_acreditar.append(fila["caso"])
        resultados.append({
            "familia": fila["familia"],
            "caso": fila["caso"],
            "signo": fila["signo"],
            "esperado": fila["esperado"],
            "obtenido": obtenido,
            "acierta": acierta,
            "punto_exigido": exigido,
            "puntos_emitidos": puntos_emitidos,
            "hallazgos": [h.punto + "/" + h.codigo for h in veredicto.hallazgos],
        })
        shutil.rmtree(arbol, ignore_errors=True)

    shutil.rmtree(plantilla, ignore_errors=True)
    cubiertas_forma = sorted({fila["caso"] for fila in resultados
                              if fila["familia"] == "V6-13"})
    cubiertas_letra = sorted({fila["caso"] for fila in resultados
                              if fila["familia"] == "V6-14"})
    return {
        "controles": resultados,
        "total": len(resultados),
        "falsos_verdes": falsos_verdes,
        "falsos_rojos": falsos_rojos,
        "sin_acreditar": sorted(sin_acreditar),
        "puntos_emitibles": puntos_emitibles(directorio),
        "puntos_exigidos": sorted(CONTROLES_POR_PUNTO),
        "cubiertos_por_familia": sorted(PUNTOS_CUBIERTOS_POR_FAMILIA),
        "no_ejercibles_aqui": PUNTOS_NO_EJERCIBLES_AQUI,
        # `M5` · LA FRONTERA CON §20.1, PUBLICADA Y NO SUPUESTA. El censo del contrato
        # menos lo que el verificador sabe EMITIR. Estos puntos no tienen veredicto que
        # contrastar aquí y los cubren sus baterías propias; se nombran para que
        # `puntos_sin_tratamiento: []` no se lea como cobertura de todo §20.1.
        "censo_20_1": censo_de_20_1(directorio),
        "de_20_1_fuera_de_esta_matriz": sorted(
            set(censo_de_20_1(directorio) or ()) - set(puntos_emitibles(directorio))),
        "por_que_fuera": "el verificador no los emite como `Hallazgo(...)`, luego no hay "
                         "veredicto suyo que contrastar con un adversarial; los ejercen "
                         "sus baterías propias, y esta matriz sólo publica la frontera",
        # LA FRONTERA, DERIVADA: todo punto emitible tiene que estar cubierto por una
        # familia, por su adversarial propio, o declarado NO EJERCIBLE con su motivo.
        # Un punto que no esté en ninguno de los tres sitios pone `V6-18` en rojo.
        "puntos_sin_tratamiento": sorted(
            set(puntos_emitibles(directorio))
            - set(PUNTOS_CUBIERTOS_POR_FAMILIA)
            - set(CONTROLES_POR_PUNTO)
            - set(PUNTOS_NO_EJERCIBLES_AQUI)),
        "formas_cubiertas": cubiertas_forma,
        "letras_cubiertas": cubiertas_letra,
        # `V6-18` cierra sobre LA SUITE COMPLETA, no sobre dos familias: además de los
        # dos ceros, se exige que ningún control quede SIN ACREDITAR su punto y que TODO
        # punto emitible esté cubierto —por una familia o por su adversarial propio—. El
        # día que el verificador aprenda a emitir uno nuevo, esto se pone rojo solo.
        "ok": falsos_verdes == 0 and falsos_rojos == 0 and not sin_acreditar
              and len(cubiertas_forma) == len(FORMAS)
              and len(cubiertas_letra) == len(LETRAS)
              and not (set(puntos_emitibles(directorio))
                       - set(PUNTOS_CUBIERTOS_POR_FAMILIA)
                       - set(CONTROLES_POR_PUNTO)
                       - set(PUNTOS_NO_EJERCIBLES_AQUI)),
    }
