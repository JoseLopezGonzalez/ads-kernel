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

    filas = _controles_de_forma() + _controles_de_mutacion()
    resultados = []
    falsos_verdes = 0
    falsos_rojos = 0

    for numero, fila in enumerate(filas):
        arbol = os.path.join(directorio, "c" + str(numero).zfill(3))
        _clonar_arbol(plantilla, arbol)
        canal = CanalGit(arbol)
        if fila["familia"] == "V6-13":
            declarar = _aplicar_forma(arbol, canal, fila)
        else:
            declarar = _aplicar_mutacion(arbol, canal, fila)
        declaracion = Declaracion(
            ancla=base, autoridad="matriz-adversarial",
            admitidas=[{"ruta": ruta, "motivo": "control positivo declarado"}
                       for ruta in declarar],
        )
        veredicto = verificar(arbol, base=base, declaracion=declaracion,
                              registro=registro, censar_el_codigo=False)
        obtenido = veredicto.color
        acierta = obtenido == fila["esperado"]
        if not acierta:
            if fila["esperado"] == "ROJO":
                falsos_verdes += 1
            else:
                falsos_rojos += 1
        resultados.append({
            "familia": fila["familia"],
            "caso": fila["caso"],
            "signo": fila["signo"],
            "esperado": fila["esperado"],
            "obtenido": obtenido,
            "acierta": acierta,
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
        "formas_cubiertas": cubiertas_forma,
        "letras_cubiertas": cubiertas_letra,
        "ok": falsos_verdes == 0 and falsos_rojos == 0
              and len(cubiertas_forma) == len(FORMAS)
              and len(cubiertas_letra) == len(LETRAS),
    }
