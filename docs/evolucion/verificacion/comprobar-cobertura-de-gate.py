#!/usr/bin/env python3
"""comprobar-cobertura-de-gate — la cobertura de un gate deja de ser DECLARATIVA.

POR QUÉ EXISTE, Y QUÉ AGUJERO CIERRA. Dos gates consecutivos de `F6` han caído por lo mismo:
un revisor declaró al final que no había leído su lote, y hasta ese momento nada lo impedía ni
lo medía. El gate del 2026-09-03 cayó con seis fuentes o rangos sin abrir. El del 2026-09-04
cayó con **50 de 84 ficheros sin abrir y 29 329 de 48 143 líneas, el 60,9 %**, y su adjudicador
rechazó expresamente la atenuante del reparto —los dos lotes diferían en el 1,1 % y el otro
revisor terminó el suyo—.

`O27` §5 lo eleva a NORMA del Owner, y con estas palabras: «*Un gate no puede llegar a
adjudicación mientras algún revisor tenga una resta `ASIGNADO − LEÍDO` distinta del conjunto
vacío. Si un revisor todavía no ha terminado, debe continuar su lectura. Su lote no puede darse
por cerrado, sustituirse con búsquedas ni compensarse con lo leído por otro agente.*»

Este comprobador es lo que convierte esa norma en un HECHO MECÁNICO. Devuelve 0 sólo si las
CUATRO restas son vacías, y mientras no devuelva 0 **no se puede crear al adjudicador**.

    OBLIGATORIO − ASIGNADO              = ∅
    ASIGNADO − LEÍDO                    = ∅
    LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS    = ∅
    FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS = ∅

DECISIÓN · lo que NO cuenta como lectura, y por qué se comprueba en vez de pedirse
    `O27` §5 y el encargo lo enumeran: `grep`, `awk`, búsquedas, `diff`, ejecutar pruebas, y
    lo leído por otro agente. Un manifiesto de lectura que declarase «leída» una fuente por
    haberla `grep`-eado sería la misma declaración vacía que ya falló dos veces. Aquí el
    revisor declara, POR FUENTE, el rango de líneas que abrió y el SHA-256 del fichero que
    leyó; el comprobador exige que el SHA case con el árbol —si no casa, leyó otra cosa— y
    que los rangos CUBRAN el fichero entero. No se puede satisfacer con una búsqueda porque
    una búsqueda no produce rangos contiguos que cubran 2 000 líneas.

DECISIÓN · la unidad es la LÍNEA, no el fichero
    Un fichero «abierto» puede haberse mirado por encima. La tercera resta —líneas asignadas
    menos líneas leídas— es la que impide que «lo abrí» valga por «lo leí»: obliga a declarar
    QUÉ tramos, y la suma tiene que dar el fichero entero. Para un rango asignado
    explícitamente, el tramo declarado tiene que contener el rango.

DECISIÓN · las FUENTES MODIFICADAS llevan una resta propia
    Es la regla que los manifiestos de este expediente escriben desde el principio —«cobertura
    histórica delegada prohibida para un fichero modificado»— y que nunca se había comprobado.
    Un fichero que el corte modificó no admite delegación de ninguna clase: o está leído
    íntegro por el revisor que lo tiene asignado, o la resta no es vacía.

FORMATO. Dos ficheros JSON:

  manifiesto.json   {"candidata": "<sha>", "revisores": {"REV-1": {"fuentes": [...]}, ...},
                     "modificadas": ["ruta", ...]}
                    cada fuente: {"ruta": str, "lineas": int, "sha256": str,
                                  "rango": [inicio, fin] | null}
  lectura-<REV>.json {"revisor": "REV-1", "cerrado": bool,
                      "leidas": [{"ruta": str, "sha256": str,
                                  "tramos": [[inicio, fin], ...]}, ...]}

Uso:
  python3 comprobar-cobertura-de-gate.py --manifiesto M.json --lectura L1.json L2.json …
                                         [--raiz DIR] [--json]
"""
from __future__ import annotations

# `E-10` · LA PROCEDENCIA DE LOS MÓDULOS, PURGADA ANTES DE NINGÚN `import` PROPIO
#
#  POR QUÉ ESTÁ AQUÍ, Y NO SÓLO EN `kernel/operativo/runtime/`. `H-01` de la auditoría del
#  2026-09-04 midió que `validadores/huella.py` no llevaba este prólogo y que, con un
#  `hashlib` homónimo en `PYTHONPATH`, **un árbol MUTADO producía la huella esperada y
#  `T150` publicaba SUPERADA con `EXIT=0`**. El mismo defecto vive en cualquier ejecutable
#  que decida algo y no purgue: éstos deciden qué universo obligatorio existe y si un gate
#  puede adjudicar, que es tanto o más que una huella.
#
#  DECISIÓN · se purga ANTES de importar nada propio, con lo único que el intérprete ya cargó
#      Purgar después de los `import` normales llega tarde —el homónimo ya está en
#      `sys.modules`— y purgar desde un módulo aparte depende de un `import`, que es
#      exactamente lo que se está protegiendo. `sys` es incorporado y `os` lo carga el
#      arranque, así que los dos vienen de `sys.modules` y no de la ruta. Que `os` sea el
#      bueno se COMPRUEBA, no se supone.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación y
#      convertiría un fallo de entorno en un fallo del aparato. `E-10` nombra dos cosas
#      concretas: `PYTHONPATH` y el `cwd`. Se retiran ésas y el recuento se publica.
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
import io
import json
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Códigos de salida, estables y distintos. `2` es «no se pudo comprobar» y NO se confunde con
# `1`, que es «se comprobó y la cobertura está incompleta». La distinción importa: un gate que
# no puede medir su cobertura no es un gate con cobertura incompleta, es un gate sin medida.
COBERTURA_COMPLETA = 0
COBERTURA_INCOMPLETA = 1
NO_SE_PUDO_COMPROBAR = 2


class ManifiestoIlegible(Exception):
    pass


def _leer_json(ruta):
    try:
        with io.open(ruta, encoding="utf-8") as manejador:
            return json.load(manejador)
    except (OSError, ValueError) as error:
        raise ManifiestoIlegible("no se puede leer `%s`: %s" % (ruta, error))


def _sha256_y_lineas(base, relativa):
    destino = os.path.join(base, relativa)
    if not os.path.isfile(destino):
        return None, None
    with io.open(destino, "rb") as manejador:
        datos = manejador.read()
    return hashlib.sha256(datos).hexdigest(), datos.count(b"\n") + (
        0 if datos.endswith(b"\n") or not datos else 1)


def _normalizar(tramos):
    """Une tramos solapados o contiguos. `[[1,10],[11,20]]` → `[[1,20]]`."""
    limpios = sorted([int(a), int(b)] for a, b in tramos if int(b) >= int(a))
    salida = []
    for inicio, fin in limpios:
        if salida and inicio <= salida[-1][1] + 1:
            salida[-1][1] = max(salida[-1][1], fin)
        else:
            salida.append([inicio, fin])
    return salida


def _faltantes(tramos, desde, hasta):
    """Lo que queda SIN cubrir del intervalo `[desde, hasta]`."""
    huecos, cursor = [], desde
    for inicio, fin in _normalizar(tramos):
        if fin < desde or inicio > hasta:
            continue
        if inicio > cursor:
            huecos.append([cursor, min(inicio - 1, hasta)])
        cursor = max(cursor, fin + 1)
        if cursor > hasta:
            break
    if cursor <= hasta:
        huecos.append([cursor, hasta])
    return huecos


def comprobar(manifiesto, lecturas, base=RAIZ):
    """Las CUATRO restas. Devuelve `(ok, informe)` y no levanta por cobertura incompleta."""
    informe = {"candidata": manifiesto.get("candidata"), "revisores": {}, "restas": {}}
    asignadas_por_revisor = {}
    for revisor, lote in sorted((manifiesto.get("revisores") or {}).items()):
        asignadas_por_revisor[revisor] = {f["ruta"]: f for f in lote.get("fuentes") or []}

    # `H-06` · LA PRIMERA RESTA ERA UNA TAUTOLOGÍA, Y SE DICE ENTERO PORQUE ES DEL AUTOR
    #
    #     Estaba escrito así: `obligatorio` se construía UNIENDO los lotes, y después se
    #     restaba `declarado_obligatorio - obligatorio` con `declarado_obligatorio` cayendo
    #     por omisión en el mismo conjunto. Es `X − X`. La auditoría del 2026-09-04 lo midió
    #     con dos manifiestos vacuos: `{"revisores":{}}` y `{"REV-1":{"fuentes":[]}}` daban
    #     los dos **COBERTURA COMPLETA · EXIT=0**, y el docstring de este mismo fichero
    #     prometía «devuelve 0 sólo si las CUATRO restas son vacías».
    #
    #     El instrumento medía que se leyera lo asignado, y NO que se asignara lo
    #     obligatorio. `O27` §5 pide las dos cosas: un lote vacío satisfacía la norma sin
    #     leer una línea, que es peor que el defecto que este fichero existe para impedir.
    #
    # DECISIÓN · `OBLIGATORIO` se DERIVA DEL ÁRBOL, y el manifiesto sólo puede AMPLIARLO
    #     Alternativas: (a) exigir que el manifiesto declare `obligatorio` y creerle; (b)
    #     derivarlo del árbol con `git diff` entre la base y la candidata; (c) las dos, con
    #     el árbol como suelo.
    #     Se elige (c). Con (a) volvemos a la declaración —el manifiesto que se equivoca al
    #     asignar se equivoca igual al declarar qué era obligatorio—. Con (b) sola, un
    #     manifiesto no podría añadir una sede normativa que el diff no toca y que sin
    #     embargo hay que leer. Con (c) el suelo lo pone el árbol: **toda fuente MODIFICADA
    #     entre la base y la candidata es obligatoria**, la declaración puede añadir, y
    #     ninguna de las dos puede quitar.
    #
    # DECISIÓN · un manifiesto SIN REVISORES, o con un revisor SIN LOTE, es fallo cerrado
    #     No es una resta vacía: es una medida que no se ha tomado. Se distingue del caso
    #     legítimo «no hay nada obligatorio» —que sobre un árbol real no ocurre— exigiendo
    #     que el universo obligatorio derivado NO esté vacío.
    obligatorio = set()
    for lote in asignadas_por_revisor.values():
        obligatorio |= set(lote)
    derivado = set(manifiesto.get("modificadas") or [])
    declarado_obligatorio = set(manifiesto.get("obligatorio") or []) | derivado
    if not declarado_obligatorio:
        raise ManifiestoIlegible(
            "el manifiesto no declara `modificadas` ni `obligatorio`, de modo que el "
            "universo obligatorio saldría VACÍO y la primera resta sería vacía por "
            "construcción. Un gate cuyo universo no se puede derivar no es un gate con "
            "cobertura completa: es un gate sin medida")
    if not asignadas_por_revisor:
        raise ManifiestoIlegible(
            "el manifiesto no declara ningún revisor: no hay a quién medir la cobertura")
    for revisor, lote in sorted(asignadas_por_revisor.items()):
        if not lote:
            raise ManifiestoIlegible(
                "el lote de `%s` está VACÍO. Un lote vacío satisface toda resta de lectura "
                "sin leer una línea, que es exactamente lo que `O27` §5 prohíbe" % revisor)
    informe["restas"]["obligatorio_menos_asignado"] = sorted(
        declarado_obligatorio - obligatorio)

    modificadas = set(manifiesto.get("modificadas") or [])
    leidas_integras = set()
    resta_lectura, resta_lineas, no_cerrados, sha_divergente = [], [], [], []

    for lectura in lecturas:
        revisor = lectura.get("revisor")
        if revisor not in asignadas_por_revisor:
            raise ManifiestoIlegible(
                "el manifiesto de lectura declara el revisor `%s`, que el manifiesto de "
                "asignación no conoce: %s" % (revisor, ", ".join(sorted(asignadas_por_revisor))))
        asignadas = asignadas_por_revisor[revisor]
        leidas = {l["ruta"]: l for l in lectura.get("leidas") or []}
        # Una fuente leída que NADIE le asignó no compensa nada: `O27` §5 prohíbe
        # expresamente compensar con lo leído por otro agente, y con más razón con lo leído
        # fuera del lote propio.
        ajenas = sorted(set(leidas) - set(asignadas))
        pendientes, tramos_pendientes = [], []
        for ruta, ficha in sorted(asignadas.items()):
            sha_arbol, lineas_arbol = _sha256_y_lineas(base, ruta)
            if sha_arbol is None:
                raise ManifiestoIlegible(
                    "el manifiesto asigna `%s`, que no existe en el árbol comprobado" % ruta)
            if ficha.get("sha256") and ficha["sha256"] != sha_arbol:
                raise ManifiestoIlegible(
                    "el manifiesto declara para `%s` un sha256 que no es el del árbol: el "
                    "lote describe otro objeto" % ruta)
            if ruta not in leidas:
                pendientes.append(ruta)
                continue
            leida = leidas[ruta]
            if leida.get("sha256") and leida["sha256"] != sha_arbol:
                sha_divergente.append("%s · %s" % (revisor, ruta))
                pendientes.append(ruta)
                continue
            rango = ficha.get("rango")
            desde, hasta = (rango if rango else [1, lineas_arbol])
            # `H-06` · un tramo `[1, 999999]` sobre un fichero de dos líneas no es una
            # lectura: es una declaración que no puede ser cierta. Se rechaza en vez de
            # aceptarla como cobertura holgada, porque el modo de fallo que este instrumento
            # persigue es precisamente el de la declaración cómoda.
            for inicio_t, fin_t in (leida.get("tramos") or []):
                if int(fin_t) > lineas_arbol or int(inicio_t) < 1:
                    raise ManifiestoIlegible(
                        "`%s` declara el tramo %s-%s sobre `%s`, que tiene %d líneas: un "
                        "tramo fuera del fichero no describe ninguna lectura"
                        % (revisor, inicio_t, fin_t, ruta, lineas_arbol))
            huecos = _faltantes(leida.get("tramos") or [], int(desde), int(hasta))
            if huecos:
                sin_leer = sum(b - a + 1 for a, b in huecos)
                tramos_pendientes.append({
                    "ruta": ruta, "revisor": revisor, "huecos": huecos,
                    "lineas_sin_leer": sin_leer,
                })
            elif ruta in modificadas:
                leidas_integras.add(ruta)
        if pendientes:
            resta_lectura.extend("%s · %s" % (revisor, r) for r in pendientes)
        resta_lineas.extend(tramos_pendientes)
        informe["revisores"][revisor] = {
            "asignadas": len(asignadas),
            "leidas_sin_hueco": len(asignadas) - len(pendientes) - len(tramos_pendientes),
            "sin_abrir": len(pendientes),
            "con_huecos": len(tramos_pendientes),
            "lineas_asignadas": sum(
                (f["rango"][1] - f["rango"][0] + 1) if f.get("rango")
                else (_sha256_y_lineas(base, f["ruta"])[1] or 0)
                for f in asignadas.values()),
            "lineas_sin_leer": sum(t["lineas_sin_leer"] for t in tramos_pendientes),
            "fuentes_ajenas_declaradas": ajenas,
            "cerrado_declarado": bool(lectura.get("cerrado")),
        }
        if not lectura.get("cerrado"):
            no_cerrados.append(revisor)

    sin_lectura = sorted(set(asignadas_por_revisor) - {l.get("revisor") for l in lecturas})
    informe["restas"]["asignado_menos_leido"] = sorted(resta_lectura)
    informe["restas"]["lineas_asignadas_menos_leidas"] = resta_lineas
    informe["restas"]["modificadas_menos_leidas_integras"] = sorted(
        modificadas - leidas_integras)
    informe["revisores_sin_manifiesto_de_lectura"] = sin_lectura
    informe["revisores_no_cerrados"] = no_cerrados
    informe["sha_divergente"] = sha_divergente

    ok = not (informe["restas"]["obligatorio_menos_asignado"]
              or informe["restas"]["asignado_menos_leido"]
              or informe["restas"]["lineas_asignadas_menos_leidas"]
              or informe["restas"]["modificadas_menos_leidas_integras"]
              or sin_lectura or no_cerrados or sha_divergente)
    informe["cobertura"] = "COMPLETA" if ok else "INCOMPLETA"
    return ok, informe


# ───────────────────────────────────────────────────────────────────────────────────────
#  AUTOPRUEBAS · un instrumento que decide si un gate puede adjudicar tiene que demostrar
#  que PUEDE FALLAR, y demostrarlo en la corrida, no en un informe.
#
#  Los seis modos son los seis por los que una cobertura puede estar incompleta, y cada uno
#  se ejerce por separado: si uno dejara de discriminar, el instrumento seguiría dando verde
#  sobre un lote sin leer, que es exactamente el defecto que existe para impedir.
# ───────────────────────────────────────────────────────────────────────────────────────
def _autopruebas(base):
    import tempfile                                                  # noqa: PLC0415
    controles, sin_detectar = [], []
    with tempfile.TemporaryDirectory(prefix="ads-cobertura-") as taller:
        uno = os.path.join(taller, "uno.txt")
        dos = os.path.join(taller, "dos.txt")
        with io.open(uno, "w", encoding="utf-8") as manejador:
            manejador.write("\n".join("linea %d" % n for n in range(1, 41)) + "\n")
        with io.open(dos, "w", encoding="utf-8") as manejador:
            manejador.write("\n".join("otra %d" % n for n in range(1, 21)) + "\n")

        def ficha(ruta, rango=None):
            sha, lineas = _sha256_y_lineas(taller, os.path.basename(ruta))
            return {"ruta": os.path.basename(ruta), "lineas": lineas,
                    "sha256": sha, "rango": rango}

        manifiesto = {
            "candidata": "AUTOPRUEBA",
            "modificadas": [os.path.basename(uno)],
            "revisores": {
                "REV-1": {"fuentes": [ficha(uno)]},
                "REV-2": {"fuentes": [ficha(dos)]},
            },
        }
        completo_1 = {"revisor": "REV-1", "cerrado": True,
                      "leidas": [{"ruta": "uno.txt", "tramos": [[1, 40]],
                                  "sha256": ficha(uno)["sha256"]}]}
        completo_2 = {"revisor": "REV-2", "cerrado": True,
                      "leidas": [{"ruta": "dos.txt", "tramos": [[1, 20]],
                                  "sha256": ficha(dos)["sha256"]}]}

        def caso(nombre, lecturas, espera_ok, espera_en_informe=None):
            ok, informe = comprobar(manifiesto, lecturas, base=taller)
            bien = (ok == espera_ok)
            if bien and espera_en_informe:
                bien = bool(informe["restas"].get(espera_en_informe)
                            or informe.get(espera_en_informe))
            controles.append((nombre, "ok" if bien else "SIN DETECTAR"))
            if not bien:
                sin_detectar.append(nombre)

        import copy                                                   # noqa: PLC0415
        caso("control POSITIVO · dos lotes leídos enteros", [completo_1, completo_2], True)
        caso("una fuente SIN ABRIR",
             [{"revisor": "REV-1", "cerrado": True, "leidas": []}, completo_2],
             False, "asignado_menos_leido")
        hueco = copy.deepcopy(completo_1)
        hueco["leidas"][0]["tramos"] = [[1, 10]]
        caso("un HUECO de líneas dentro de la fuente", [hueco, completo_2],
             False, "lineas_asignadas_menos_leidas")
        ajeno = copy.deepcopy(completo_2)
        ajeno["leidas"].append({"ruta": "uno.txt", "tramos": [[1, 40]],
                                "sha256": ficha(uno)["sha256"]})
        caso("un revisor intenta COMPENSAR lo que otro no leyó",
             [{"revisor": "REV-1", "cerrado": True, "leidas": []}, ajeno],
             False, "asignado_menos_leido")
        otro_sha = copy.deepcopy(completo_1)
        otro_sha["leidas"][0]["sha256"] = "0" * 64
        caso("leyó OTRO OBJETO · sha256 divergente", [otro_sha, completo_2],
             False, "sha_divergente")
        abierto = copy.deepcopy(completo_1)
        abierto["cerrado"] = False
        caso("lote declarado NO CERRADO", [abierto, completo_2],
             False, "revisores_no_cerrados")
        caso("un revisor SIN manifiesto de lectura", [completo_1],
             False, "revisores_sin_manifiesto_de_lectura")

        # `H-06` · LOS TRES CASOS VACUOS. La auditoría midió que las siete autopruebas
        # anteriores NO ejercían ninguno, y que los tres daban COBERTURA COMPLETA con
        # EXIT=0. Un instrumento que sólo se prueba con manifiestos bien formados no mide
        # su propio modo de fallo más barato: el del manifiesto que no asigna nada.
        def caso_ilegible(nombre, manifiesto_hostil, lecturas):
            try:
                comprobar(manifiesto_hostil, lecturas, base=taller)
            except ManifiestoIlegible:
                controles.append((nombre, "ok"))
                return
            controles.append((nombre, "SIN DETECTAR"))
            sin_detectar.append(nombre)

        caso_ilegible("manifiesto SIN revisores", {"candidata": "X", "revisores": {},
                                                   "modificadas": ["uno.txt"]}, [])
        caso_ilegible("un revisor con el LOTE VACÍO",
                      {"candidata": "X", "modificadas": ["uno.txt"],
                       "revisores": {"REV-1": {"fuentes": []}}}, [])
        caso_ilegible("universo obligatorio VACÍO por construcción",
                      {"candidata": "X", "revisores": {"REV-1": {"fuentes": [ficha(uno)]}}},
                      [completo_1])
        fuera = copy.deepcopy(completo_1)
        fuera["leidas"][0]["tramos"] = [[1, 999999]]
        caso_ilegible("un TRAMO fuera del fichero declarado como lectura",
                      manifiesto, [fuera, completo_2])
    return controles, sin_detectar


def main():
    analizador = argparse.ArgumentParser(
        description="comprueba mecánicamente la cobertura de un gate")
    analizador.add_argument("--autopruebas", action="store_true",
                            help="ejerce los modos de fallo del propio instrumento")
    analizador.add_argument("--manifiesto")
    analizador.add_argument("--lectura", nargs="*", default=[])
    analizador.add_argument("--raiz", default=RAIZ)
    analizador.add_argument("--json", action="store_true")
    argumentos = analizador.parse_args()
    if argumentos.autopruebas:
        controles, sin_detectar = _autopruebas(os.path.abspath(argumentos.raiz))
        for nombre, resultado in controles:
            sys.stdout.write("  %-4s %s\n" % (resultado if resultado != "ok" else "ok  ",
                                              nombre))
        sys.stdout.write("\n  %d controles · %d sin detectar\n"
                         % (len(controles), len(sin_detectar)))
        return COBERTURA_COMPLETA if not sin_detectar else COBERTURA_INCOMPLETA
    if not argumentos.manifiesto:
        sys.stderr.write("NO SE PUDO COMPROBAR · falta `--manifiesto`\n")
        return NO_SE_PUDO_COMPROBAR
    try:
        manifiesto = _leer_json(argumentos.manifiesto)
        lecturas = [_leer_json(r) for r in argumentos.lectura]
        ok, informe = comprobar(manifiesto, lecturas, base=os.path.abspath(argumentos.raiz))
    except ManifiestoIlegible as error:
        sys.stderr.write("NO SE PUDO COMPROBAR · %s\n" % error)
        return NO_SE_PUDO_COMPROBAR

    if argumentos.json:
        sys.stdout.write(json.dumps(informe, ensure_ascii=False, indent=2) + "\n")
        return COBERTURA_COMPLETA if ok else COBERTURA_INCOMPLETA

    sys.stdout.write("COBERTURA DEL GATE · candidata %s\n" % informe["candidata"])
    sys.stdout.write("=" * 78 + "\n")
    for revisor, ficha in sorted(informe["revisores"].items()):
        sys.stdout.write(
            "  %-8s asignadas %3d · leídas sin hueco %3d · sin abrir %3d · con huecos %3d\n"
            "           líneas asignadas %6d · sin leer %6d · cerrado declarado: %s\n"
            % (revisor, ficha["asignadas"], ficha["leidas_sin_hueco"], ficha["sin_abrir"],
               ficha["con_huecos"], ficha["lineas_asignadas"], ficha["lineas_sin_leer"],
               "sí" if ficha["cerrado_declarado"] else "NO"))
        if ficha["fuentes_ajenas_declaradas"]:
            sys.stdout.write(
                "           NO COMPENSA · fuentes declaradas fuera de su lote: %s\n"
                % ", ".join(ficha["fuentes_ajenas_declaradas"]))
    sys.stdout.write("\nLAS CUATRO RESTAS\n" + "-" * 78 + "\n")
    for clave, titulo in (
            ("obligatorio_menos_asignado", "OBLIGATORIO − ASIGNADO"),
            ("asignado_menos_leido", "ASIGNADO − LEÍDO"),
            ("lineas_asignadas_menos_leidas", "LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS"),
            ("modificadas_menos_leidas_integras",
             "FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS")):
        valor = informe["restas"][clave]
        sys.stdout.write("  %-38s %s\n" % (titulo, "∅" if not valor else len(valor)))
        for entrada in valor[:40]:
            if isinstance(entrada, dict):
                sys.stdout.write(
                    "      %s · %s · faltan %d líneas en %s\n"
                    % (entrada["revisor"], entrada["ruta"], entrada["lineas_sin_leer"],
                       ", ".join("%d-%d" % (a, b) for a, b in entrada["huecos"][:6])))
            else:
                sys.stdout.write("      %s\n" % entrada)
    if informe["revisores_sin_manifiesto_de_lectura"]:
        sys.stdout.write("  SIN MANIFIESTO DE LECTURA: %s\n"
                         % ", ".join(informe["revisores_sin_manifiesto_de_lectura"]))
    if informe["revisores_no_cerrados"]:
        sys.stdout.write("  LOTE NO CERRADO: %s\n" % ", ".join(informe["revisores_no_cerrados"]))
    if informe["sha_divergente"]:
        sys.stdout.write("  LEYÓ OTRO OBJETO: %s\n" % ", ".join(informe["sha_divergente"]))
    sys.stdout.write("\n  COBERTURA %s\n" % informe["cobertura"])
    if not ok:
        sys.stdout.write(
            "  El adjudicador NO puede crearse. `O27` §5: el lote no se cierra, no se\n"
            "  sustituye con búsquedas y no se compensa con lo leído por otro agente.\n")
    return COBERTURA_COMPLETA if ok else COBERTURA_INCOMPLETA


if __name__ == "__main__":
    sys.exit(main())
