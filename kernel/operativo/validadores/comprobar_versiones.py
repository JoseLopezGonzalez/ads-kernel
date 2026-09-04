#!/usr/bin/env python3
"""comprobar_versiones — los puntos de entrada no se contradicen sobre la versión.

Hallazgo A-12: tres números para el mismo artefacto —2.0.0-alpha.1 en kernel/VERSION,
1.3.0 en la cabecera de KERNEL.md, 1.0.0 en el árbol del README— y un bloque «Contenido»
que describía el repositorio de la versión anterior. `ads_lint` no lo veía porque su ámbito
por defecto era `kernel/operativo` y `packs`: la portada del repositorio quedaba fuera.

La política está en `kernel/VERSIONES.md` y distingue CUATRO versiones de cosas distintas.
Esto comprueba que nadie las mezcla.

CONTRATO 2 de `11-ARQ` §19 · el ALCANCE de `T152` ya no son dos ficheros escritos a mano:
es TODA SEDE QUE PUBLIQUE VERSIÓN, descubierta por barrido y resuelta contra
`kernel/VERSIONES.md`, que es su sede única. Ver `sedes_que_publican_version`.

Uso:
  python3 kernel/operativo/validadores/comprobar_versiones.py [--json] [--raiz DIR]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from comprobar_contratos import Resultado  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")


# ===========================================================================
#  CONTRATO 2 de `11-ARQ` §19 · TODA SEDE QUE PUBLIQUE VERSIÓN, DESCUBIERTA
# ===========================================================================
#  `T152` recorría **sólo `README.md` y `START_HERE.md`**, escritos a mano en un `for`. Por
#  eso pasaba en verde mientras `kernel/operativo/00-INDICE.md` declaraba `KERNEL.md`
#  «1.3.0» y `KERNEL.md` decía **1.5.0**: la sede que mentía no estaba en la lista, y una
#  lista no puede contener la sede que todavía no existe.
#
#  El contrato lo dice sin margen: «toda sede que publique una versión, DESCUBIERTA POR
#  BARRIDO … La lista anterior es un EJEMPLO de lo que el barrido encuentra hoy, no la
#  definición del alcance». Y la condición de cierre son dos cosas, no una: que ninguna sede
#  VIVA publique una versión obsoleta, **y que el ALCANCE de `T152` sea derivado**.

# El corpus que VIAJA, y cuyo remedio es F6. Patrones, no rutas.
AMBITO_F6 = [r"^README\.md$", r"^START_HERE\.md$", r"^kernel/", r"^packs/"]
FUERA_DEL_AMBITO = [
    (r"^kernel/KERNEL_CHANGELOG\.md$", "registro histórico de versiones: su materia es citarlas"),
    (r"^kernel/operativo/pruebas/evidencia/", "salidas capturadas de ejecuciones pasadas"),
    (r"^kernel/operativo/validadores/", "código, con las infracciones deliberadas de los negativos"),
    (r"^packs/legacy-", "packs retirados, conservados sólo para trazabilidad"),
]

# Los ARTEFACTOS versionados y cómo los nombra el corpus cuando publica su versión. La
# versión vigente NO se escribe aquí: se resuelve contra `kernel/VERSIONES.md`.
# `en_politica` es CÓMO se nombra el artefacto en su sede única, donde la identificación
# tiene que ser exacta; `en_corpus` es cómo lo nombra cualquier documento cuando publica su
# versión, donde el corpus escribe «el kernel» tanto como la ruta entera. Separarlos evita
# que «qué copia **del kernel** lleva un proyecto», escrito en la fila del RELEASE, haga que
# la política parezca declarar dos versiones para la línea histórica.
ARTEFACTOS = [
    ("kernel/KERNEL.md",
     r"`?kernel/KERNEL\.md`?",
     r"(?:`?kernel/KERNEL\.md`?|`?KERNEL\.md`?|\bel kernel\b|\bkernel\b(?!/))"),
    ("kernel/VERSION", r"`?kernel/VERSION`?", r"(?:`?kernel/VERSION`?|\brelease\b)"),
]

# Una versión NOMBRADA no siempre se PUBLICA: el corpus también la CITA. «el procedimiento
# de gaps que el kernel 1.3.0 no tenía» no declara la versión vigente de nada, y exigirle que
# diga 1.5.0 sería falsear la frase. La cita se reconoce por su marca, y las marcas se
# declaran: sin ellas el validador denunciaría la historia del corpus como si fuera su
# estado. `G53 — … *(kernel 1.3.0)*` es el mismo caso en forma estructural: la procedencia de
# una regla, entre paréntesis y en cursiva.
MARCAS_DE_CITA = [
    r"\bno ten[ií]a\b", r"\bno exist[ií]a\b", r"\bdec[ií]a\b", r"\bllegó a declarar\b",
    r"\bera\b", r"\blegado\b", r"\bretirad[oa]s?\b", r"\bsuperad[oa]s?\b",
    r"\bversión anterior\b", r"\bhistóric[oa]s?\b", r"\bexcluido\b", r"\bfrente a\b",
    r"\bconviviendo con la línea\b", r"\bya no se instalan\b",
    r"\bdeclaró\b", r"\bausentes\b", r"\bno ten[ií]an\b", r"\bhaya declarado\b",
]
_CITA_ESTRUCTURAL = re.compile(r"\*\([^)]*\d+\.\d+\.\d+[^)]*\)\*")

# Los REMEDIOS, por clase de sede. El contrato es explícito: «no todas las sedes se corrigen
# igual, y el validador lo REPORTA sin decidirlo». Aquí se declara QUIÉN y EN QUÉ FASE, no
# qué hay que escribir.
REMEDIOS = [
    (r"^docs/rediseno/", "F5", "material APROBADO: la enmienda es de F5, no de F6"),
    (r"^docs/owner/", "OWNER", "resolución del Owner: pide NOTA, no reescritura"),
    (r"^docs/evolucion/\d", "—", "documento histórico e inmutable: no se corrige, se cita"),
    (r"^docs/", "F6", "proyección vigente de la capa documental"),
    (r"^(?:README|START_HERE)\.md$", "F6", "punto de entrada del repositorio"),
    (r"^kernel/|^packs/", "F6", "corpus operativo vigente"),
]


def _clase_de_sede(rel):
    for patron, fase, forma in REMEDIOS:
        if re.search(patron, rel):
            return fase, forma
    return "?", "sin clase de remedio declarada"


def version_vigente(base):
    """La versión vigente de cada artefacto, resuelta en su SEDE ÚNICA.

    `kernel/VERSIONES.md`, regla 5: «Ningún documento declara una versión de un artefacto
    que no esté en esta tabla». Se lee de sus bloques cercados, que son la tabla; la prosa
    de arriba CITA los tres números del hallazgo `A-12` y leerla sería tomar el defecto por
    la política.
    """
    ruta = os.path.join(base, "kernel/VERSIONES.md")
    if not os.path.exists(ruta):
        return {}, ["no existe kernel/VERSIONES.md: sin política declarada, cualquier "
                    "número es defendible"]
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    bloques = re.findall(r"```text\n(.*?)```", texto, re.S)
    vigentes, problemas = {}, []
    for artefacto, patron, _corpus in ARTEFACTOS:
        hallados = set()
        for bloque in bloques:
            for m in re.finditer(patron + r"[^\n]*\n?[^\n]*?"
                                 r"\b(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)\b", bloque):
                hallados.add(m.group(1))
        if not hallados:
            problemas.append(f"`kernel/VERSIONES.md` no declara la versión vigente de "
                             f"`{artefacto}`: su sede única no la tiene")
        elif len(hallados) > 1:
            problemas.append(f"`kernel/VERSIONES.md` declara {sorted(hallados)} para "
                             f"`{artefacto}`: la sede única publica dos verdades")
        else:
            vigentes[artefacto] = hallados.pop()
    return vigentes, problemas


def sedes_que_publican_version(base, ambito=None):
    """El ALCANCE de `T152`, DESCUBIERTO. Nunca una lista de ficheros."""
    ambito = ambito or AMBITO_F6
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "__pycache__", ".pytest_cache")]
        for nombre in sorted(filenames):
            if not nombre.endswith(".md"):
                continue
            ruta = os.path.join(dirpath, nombre)
            rel = os.path.relpath(ruta, base).replace(os.sep, "/")
            if not any(re.search(p, rel) for p in ambito):
                continue
            if any(re.search(p, rel) for p, _m in FUERA_DEL_AMBITO):
                continue
            with open(ruta, encoding="utf-8") as fh:
                texto = fh.read()
            if not re.search(r"\d+\.\d+\.\d+", texto):
                continue
            yield rel, texto


def _frase(texto, inicio, fin):
    """La FRASE que contiene el hallazgo, no la línea.

    El corpus envuelve los párrafos, y la marca que convierte una versión en CITA cae
    muchas veces en la línea anterior: «a.11 declaró **ausentes por completo** / en el
    kernel 1.3.0». Mirar sólo la línea del número denunciaba esa frase como si publicara
    una versión vigente, que es exactamente lo contrario de lo que dice.
    """
    abre = max(texto.rfind(". ", 0, inicio), texto.rfind("\n\n", 0, inicio),
               texto.rfind("| ", 0, inicio)) + 1
    cierra = texto.find(". ", fin)
    return texto[abre:(cierra + 1) if cierra != -1 else min(len(texto), fin + 120)]


def _es_cita(frase):
    if _CITA_ESTRUCTURAL.search(frase):
        return True
    return any(re.search(p, frase, re.I) for p in MARCAS_DE_CITA)


def barrer_versiones(base, vigentes, ambito=None):
    """`(ruta, línea, artefacto, versión publicada, versión vigente, fase, remedio)`."""
    divergencias = []
    for rel, texto in sedes_que_publican_version(base, ambito):
        for artefacto, _politica, patron in ARTEFACTOS:
            for m in re.finditer(patron + r"[^\n]{0,70}?"
                                 r"\b(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)\b", texto):
                publicada, vigente = m.group(1), vigentes.get(artefacto)
                if vigente is None or publicada == vigente:
                    continue
                # `^1.0.0` es un RANGO de compatibilidad, no una versión publicada
                if texto[max(0, m.start(1) - 1)] in "^~>=<":
                    continue
                if _es_cita(_frase(texto, m.start(), m.end())):
                    continue
                numero = texto[:m.start(1)].count("\n") + 1
                fase, forma = _clase_de_sede(rel)
                divergencias.append((rel, numero, artefacto, publicada, vigente,
                                     fase, forma))
    return divergencias


def t152_versiones(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T152", "Los puntos de entrada no se contradicen sobre la versión")

    politica = os.path.join(base, "kernel/VERSIONES.md")
    if not os.path.exists(politica):
        r.fallo("no existe kernel/VERSIONES.md: sin política declarada, cualquier número "
                "es defendible")
        return r
    with open(politica, encoding="utf-8") as fh:
        texto_politica = fh.read()

    ruta_version = os.path.join(base, "kernel/VERSION")
    if not os.path.exists(ruta_version):
        r.fallo("no existe kernel/VERSION")
        return r
    with open(ruta_version, encoding="utf-8") as fh:
        release = fh.read().strip()
    if not SEMVER.match(release):
        r.fallo(f"kernel/VERSION = '{release}' no es una versión reconocible")

    # la política tiene que nombrar la versión del release vigente
    if release not in texto_politica:
        r.fallo(f"kernel/VERSIONES.md no nombra la versión vigente del release ({release}): "
                f"la política y el artefacto van por separado")

    # la línea histórica que declara KERNEL.md tiene que ser la que la política declara
    ruta_kernel = os.path.join(base, "kernel/KERNEL.md")
    linea_historica = None
    if os.path.exists(ruta_kernel):
        with open(ruta_kernel, encoding="utf-8") as fh:
            cabecera = fh.read(2000)
        m = re.search(r"\*\*Versión del kernel:\*\*\s*(\S+)", cabecera)
        if not m:
            r.fallo("kernel/KERNEL.md no declara su versión en la cabecera")
        else:
            linea_historica = m.group(1)
            if linea_historica == release:
                r.fallo(f"KERNEL.md declara {linea_historica}, igual que el release. Son "
                        f"contadores distintos: subir uno no sube el otro")
            if linea_historica not in texto_politica:
                r.fallo(f"la política no reconoce la línea histórica {linea_historica} que "
                        f"declara KERNEL.md")

    # el CHANGELOG más reciente coincide con el release
    ruta_ch = os.path.join(base, "kernel/KERNEL_CHANGELOG.md")
    if os.path.exists(ruta_ch):
        with open(ruta_ch, encoding="utf-8") as fh:
            m = re.search(r"^##\s+(\S+)", fh.read(), re.M)
        if not m:
            r.fallo("kernel/KERNEL_CHANGELOG.md no tiene ninguna entrada de versión")
        elif m.group(1) != release:
            r.fallo(f"la entrada más reciente del CHANGELOG es {m.group(1)} y el release es "
                    f"{release}: o falta la entrada, o falta el cambio de versión")

    # CONTRATO 2 · el alcance ya no es una lista. Ninguna sede VIVA del corpus que viaja
    # puede publicar una versión que no sea la vigente de su artefacto.
    vigentes, problemas = version_vigente(base)
    for p in problemas:
        r.fallo(p)
    for rel, numero, artefacto, publicada, vigente, fase, forma in barrer_versiones(
            base, vigentes):
        r.fallo(f"{rel}:{numero}: publica {publicada} para `{artefacto}` y la vigente es "
                f"{vigente}. REMEDIO {fase} — {forma}. La sede no se enumeró: la encontró "
                f"el barrido (`11-ARQ` §19, CONTRATO 2)")
    return r


def t272_alcance_derivado_y_remedios_declarados(raiz=None):
    """CONTRATO 2, condición de cierre · el ALCANCE deriva, y cada sede tiene remedio.

    Dos propiedades, y las dos se EJERCEN, no se leen:

    1 · una sede NUEVA que publique una versión falsa se detecta sin tocar el validador.
        Se fabrica en un directorio temporal —ruta nueva, nombre nuevo— y se barre con el
        mismo `barrer_versiones` que corre `T152`. Es la prueba negativa que el contrato
        pide con esas palabras.
    2 · toda sede del corpus documental que publique una versión obsoleta tiene una CLASE
        DE REMEDIO declarada, con su fase. El contrato exige «reportar remedios distintos
        por sede SIN DECIDIRLOS»: lo que no se tolera es que una sede quede sin clase, que
        es como se ignora una en silencio.
    """
    import tempfile
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T272", "El alcance de T152 se descubre, y cada sede tiene remedio declarado")
    vigentes, problemas = version_vigente(base)
    for p in problemas:
        r.fallo(p)
    if not vigentes:
        return r

    with tempfile.TemporaryDirectory(prefix="ads-alcance-") as tmp:
        nueva = os.path.join(tmp, "kernel", "SEDE-QUE-NADIE-ENUMERO.md")
        os.makedirs(os.path.dirname(nueva), exist_ok=True)
        with open(nueva, "w", encoding="utf-8") as fh:
            fh.write("# sede nueva\n\nEsta sede declara `kernel/KERNEL.md` 9.9.9.\n")
        if not barrer_versiones(tmp, vigentes):
            r.fallo("una sede NUEVA que publica `kernel/KERNEL.md` 9.9.9 NO fue detectada: "
                    "el alcance sigue enumerándose (`11-ARQ` §19, CONTRATO 2, prueba "
                    "negativa)")
        with open(nueva, "w", encoding="utf-8") as fh:
            fh.write(f"# sede nueva\n\nEsta sede declara `kernel/KERNEL.md` "
                     f"{vigentes['kernel/KERNEL.md']}.\n")
        if barrer_versiones(tmp, vigentes):
            r.fallo("la MISMA sede con la versión vigente también se denuncia: un barrido "
                    "que falla siempre no distingue nada")

    # La capa documental: se REPORTA, y su remedio no lo decide este validador.
    pendientes = barrer_versiones(base, vigentes, ambito=[r"^docs/"])
    for rel, numero, artefacto, publicada, vigente, fase, forma in pendientes:
        if fase == "?":
            r.fallo(f"{rel}:{numero}: publica {publicada} para `{artefacto}` (vigente "
                    f"{vigente}) y NINGUNA clase de remedio la cubre. Una sede sin "
                    f"propietario declarado es una sede que se ignora en silencio")
    return r


PRUEBAS = [t152_versiones, t272_alcance_derivado_y_remedios_declarados]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None)
    args = ap.parse_args()
    resultados = [f(args.raiz) for f in PRUEBAS]
    if args.json:
        print(json.dumps([{"id": x.id, "nombre": x.nombre,
                           "estado": "prueba-superada" if x.superada else "prueba-fallida",
                           "fallos": x.fallos} for x in resultados], ensure_ascii=False, indent=2))
    else:
        for x in resultados:
            print(f"{x.id}  {'SUPERADA' if x.superada else 'FALLIDA '}  {x.nombre}")
            for f in x.fallos:
                print(f"          · {f}")
        fallidas = [x for x in resultados if not x.superada]
        print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if any(not x.superada for x in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
