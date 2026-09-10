#!/usr/bin/env python3
"""comprobar_rutas_portables — ninguna ruta del kernel es imposible en Windows.

POR QUE EXISTE ESTE VALIDADOR
-----------------------------
Porque el kernel contuvo durante toda su vida el directorio
`kernel/operativo/capacidades/CON/`, y `CON` es un nombre de dispositivo
RESERVADO en Windows desde MS-DOS. Git en Windows se niega a crear esa ruta:

    error: invalid path 'kernel/operativo/capacidades/CON/CAPACIDAD.md'
    fatal: ... exit code 128

No fallaba un guion: **fallaba el `git clone` entero**. Cualquier proyecto que
instalara este kernel en Windows se encontraba con un repositorio que no se
podia obtener. No se detecto antes porque nadie habia ejecutado nada en
Windows: el defecto era invisible desde Linux y desde macOS, donde `CON` es un
nombre de directorio perfectamente corriente.

Este validador existe para que no vuelva a ser invisible. Corre en cualquier
sistema —no hace falta un Windows para detectarlo— y falla en cuanto alguien
anade un `aux.txt`, un directorio `PRN`, un fichero con `:` en el nombre o uno
que termine en punto.

QUE COMPRUEBA, Y POR QUE CADA COSA
-----------------------------------
    nombres de dispositivo reservados   CON, PRN, AUX, NUL, CLOCK$, COM1..9,
                                        LPT1..9 — lo son CON CUALQUIER
                                        EXTENSION: `con.txt` falla igual que
                                        `CON`, y sin importar mayusculas
    caracteres prohibidos               < > : " | ? *  no existen en un nombre
                                        de fichero de Windows
    final en espacio o punto            Windows los recorta en silencio, asi
                                        que dos rutas distintas colisionan
    colision por mayusculas             NTFS y APFS no distinguen may/min por
                                        defecto: dos ficheros que solo se
                                        diferencian en eso son un conflicto
                                        que en Linux no se ve

Uso:
  python3 kernel/operativo/validadores/comprobar_rutas_portables.py [--json] [--raiz DIR]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from comprobar_contratos import Resultado  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Nombres de dispositivo de MS-DOS. Siguen reservados en Windows moderno.
RESERVADOS = (
    {"CON", "PRN", "AUX", "NUL", "CLOCK$"}
    | {f"COM{i}" for i in range(1, 10)}
    | {f"LPT{i}" for i in range(1, 10)}
)

PROHIBIDOS = '<>:"|?*'

# Lo que no se inspecciona: no forma parte del material que viaja a un proyecto.
FUERA = (".git/",)


def _rutas(raiz: str) -> list[str]:
    """Todas las rutas del arbol, relativas y con barras normales."""
    encontradas = []
    for base, directorios, ficheros in os.walk(raiz):
        directorios[:] = [d for d in directorios if d != ".git"]
        for nombre in ficheros + directorios:
            completa = os.path.join(base, nombre)
            relativa = os.path.relpath(completa, raiz).replace(os.sep, "/")
            if any(relativa.startswith(f) for f in FUERA):
                continue
            encontradas.append(relativa)
    return sorted(set(encontradas))


def _problemas(ruta: str) -> list[str]:
    fallos = []
    for segmento in ruta.split("/"):
        # El nombre reservado lo es con cualquier extension: `CON`, `CON.md` y
        # `con.txt` fallan los tres. Se compara el tramo anterior al primer punto.
        base = segmento.split(".")[0].upper()
        if base in RESERVADOS:
            fallos.append(f"«{segmento}» usa el nombre de dispositivo reservado «{base}»")
        malos = sorted(set(segmento) & set(PROHIBIDOS))
        if malos:
            fallos.append(f"«{segmento}» contiene {''.join(malos)}, prohibidos en Windows")
        if segmento not in (".", "..") and segmento.endswith((" ", ".")):
            fallos.append(f"«{segmento}» termina en espacio o punto: Windows lo recorta")
    return fallos


def t153_rutas_portables(raiz=None):
    """T153 · ninguna ruta del arbol es imposible de crear en Windows."""
    raiz = raiz or RAIZ
    r = Resultado("T153", "Ninguna ruta del arbol es imposible en Windows")

    invalidas = []
    for ruta in _rutas(raiz):
        for fallo in _problemas(ruta):
            invalidas.append(f"{ruta}: {fallo}")

    for i in invalidas:
        r.fallo(i)
    if invalidas:
        r.fallo("un `git clone` en Windows fallaria ENTERO con «invalid path». "
                "No es un aviso de estilo: el repositorio no se puede obtener alli")
    return r


def t154_sin_colision_por_mayusculas(raiz=None):
    """T154 · dos rutas que solo difieren en mayusculas colisionan fuera de Linux."""
    raiz = raiz or RAIZ
    r = Resultado("T154", "Ninguna pareja de rutas colisiona al ignorar mayusculas")

    vistas: dict[str, str] = {}
    for ruta in _rutas(raiz):
        clave = ruta.lower()
        if clave in vistas and vistas[clave] != ruta:
            r.fallo(f"«{ruta}» y «{vistas[clave]}» son la MISMA ruta en NTFS y en APFS")
        vistas[clave] = ruta
    return r


COMPROBACIONES = [t153_rutas_portables, t154_sin_colision_por_mayusculas]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--raiz", default=RAIZ)
    p.add_argument("--json", action="store_true", dest="como_json")
    args = p.parse_args()

    resultados = [c(args.raiz) for c in COMPROBACIONES]
    superadas = [r for r in resultados if not r.fallos]
    fallidas = [r for r in resultados if r.fallos]

    if args.como_json:
        print(json.dumps({"superadas": len(superadas), "fallidas": len(fallidas),
                          "detalle": [{"id": r.id, "titulo": r.nombre, "fallos": r.fallos}
                                      for r in resultados]},
                         ensure_ascii=False, indent=2))
    else:
        for r in resultados:
            estado = "SUPERADA" if not r.fallos else "FALLIDA "
            print(f"{r.id}  {estado}  {r.nombre}")
            for f in r.fallos:
                print(f"          · {f}")
        print(f"\n{len(superadas)} superadas · {len(fallidas)} fallidas")
    return 1 if fallidas else 0


if __name__ == "__main__":
    raise SystemExit(main())
