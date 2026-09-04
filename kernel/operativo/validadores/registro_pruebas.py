#!/usr/bin/env python3
"""Regenera pruebas/REGISTRO-generado.md a partir de los bloques ads:escenario.

Determinista: mismo estado canónico produce bytes idénticos. Sin hora de pared,
sin telemetría (regla de determinismo de a.9).

**Y ADEMÁS ES LA SEDE DE UNA FÓRMULA: el ESTADO DE UN ESCENARIO, DERIVADO DE SU EVIDENCIA.**

    LO QUE FALLABA (`ADJ-G2`, `03-GATE-DE-CERTIFICACION-FINAL-20260904.md` §4.5)
    El campo `estado:` se escribía a mano en el bloque `ads:escenario` y este generador lo
    COPIABA VERBATIM —líneas 57 y 76 de la versión anterior—. Ningún validador del corpus
    lo contrastaba contra la evidencia: se barrieron los veinticinco. Y no hacía falta
    mutar nada para verlo, porque el árbol YA PUBLICABA la divergencia:

        T270-T289…md, bloque `T273`      estado: prueba-fallida
        REGISTRO-generado.md L220        **PRUEBA FALLIDA**
        evidencia/composicion-procesos-salida.txt
                                         # codigo: 0
                                         T273  SUPERADA  Todo par del catálogo …
                                         4 superadas · 0 fallidas

    Tres sedes decían VERDE, la cuarta publicaba `PRUEBA FALLIDA`, y los 34 validadores
    estaban en verde. `REGISTRO.md` escribe «**Regla dura:** ninguna prueba sube de estado
    por argumento. Sube porque se ejecutó y su salida quedó registrada». **Esa regla no
    estaba mecanizada**, y una regla dura que nadie ejecuta es una frase.

    Y midiendo para corregir apareció una SEGUNDA divergencia viva que nadie había
    registrado: `T277` declaraba `estado: prueba-ejecutada` citando
    `evidencia/universo-obligatorio-salida.txt`, **un fichero que no existe en el árbol ni
    ha existido en ningún commit** (`git log --all --` sobre esa ruta: vacío).

DECISIÓN · el estado se DERIVA aquí y se VALIDA en `comprobar_evidencia`, y la fórmula es UNA
    Alternativas: (a) que el generador derive y nadie más mire; (b) que un validador
    contraste y el generador siga copiando; (c) las dos cosas, con UNA sola fórmula.
    Se elige (c). Con (a) el registro publicaría la verdad y el bloque `ads:escenario`
    —que es la sede que un lector cita— seguiría mintiendo. Con (b) el registro publicado
    seguiría copiando el campo escrito a mano. Con (c) el registro publica lo DERIVADO y el
    validador exige que lo declarado coincida, de modo que la divergencia no se puede
    esconder por ninguno de los dos lados. Y la fórmula vive en UN sitio —aquí— porque dos
    definiciones de «qué estado tiene esta prueba» son dos verdades, que es lo que `V6-19`
    cierra en el paquete de admisión por la misma razón.

`H-02` · Y LO QUE «NO CONTRASTABLE» ESTABA TAPANDO, MEDIDO POR LA AUDITORÍA DEL 2026-09-04

    La corrección anterior cerró `ADJ-G2` para las divergencias que la evidencia
    CONTRADICE, y dejó abiertas las que la evidencia NO SOSTIENE. El aparato calculaba la
    divergencia, escribía el motivo y LA TIRABA porque marcaba `contrastado=False`:

        $ python3.12 kernel/operativo/validadores/registro_pruebas.py
        267 escenarios · … contraste del estado: 193 contrastados · 74 no contrastables ·
        0 divergencias
        $ (de esos 74, por estado DECLARADO)
        56  contrato-definido       sin evidencia   → honesto, no afirma ejecución
         4  validador-implementado  sin evidencia   → honesto
        14  prueba-superada         CON evidencia   → SILENCIADOS
        $ grep -c "T16[2-8]" kernel/operativo/pruebas/evidencia/workspace-salida.txt
        0

    Catorce escenarios —`T162`…`T168`, `T180`, `T181`, `T193`, `T225`, `T301`, `T310`,
    `T311`— declaraban `prueba-superada`; este mismo módulo derivaba `prueba-ejecutada`,
    escribía el motivo —«la ejecución consta, el resultado DE ESTE escenario no»— y lo
    descartaba. `T350` quedaba VERDE. `REGISTRO.md` escribe «**Regla dura:** ninguna prueba
    sube de estado por argumento», y catorce subían por argumento, ese día, con todo en
    verde.

DECISIÓN · un `estado` SUPERIOR al derivado es DIVERGENCIA, se pueda contrastar o no
    Alternativas: (a) que un estado superior al derivado sea divergencia aunque la evidencia
    no nombre al escenario; (b) exigir que la evidencia sea NOMINAL por escenario —que toda
    salida publique una línea de veredicto con el identificador— y dar rojo si no.
    Se elige (a), y se MIDE el coste de (b) en vez de suponerlo: de los catorce, seis
    (`T162`…`T167`) los produce `tooling/tests/test_workspace.py`, uno (`T180`)
    `escenario_extremo_a_extremo.py`, uno (`T193`) `escenario_e2e_runtime.py` y dos
    (`T225`, `T301`) `escenario_e2e_f6.py`; cuatro ficheros que hay que reescribir para que
    su salida nombre escenarios, más los dos —`T168`, `T181`— cuya evidencia la produce
    `comprobar_arranque.py`, que hoy publica veredictos de `T148`, `T171` y `T194` y de
    ninguno más. (b) es más ambiciosa y es el destino correcto; también es una reescritura
    de la salida de cuatro baterías, y una reescritura de salidas es la clase de cambio que
    se hace con su propia pasada y su propia evidencia, no de paso.
    (a) cierra la REGLA hoy y no depende de nadie: `contrastado` sigue significando lo que
    significaba —si la evidencia NOMBRA al escenario—, sigue publicándose con su cifra, y
    deja de ser una LICENCIA. Lo que no se puede contrastar ya no autoriza a afirmar más de
    lo que la evidencia sostiene: autoriza a afirmar eso, o menos.

DECISIÓN · sólo se persigue SUBIR, y bajar se admite con su motivo escrito
    Los cinco estados no son una escala: `prueba-fallida` no es «más» que `prueba-superada`,
    es OTRA COSA, y por eso se compara por igualdad cuando alguno de los dos es ése. Entre
    los cuatro progresivos sí hay orden, y lo que la regla dura prohíbe es SUBIR: afirmar
    una garantía que la evidencia no entrega. DECLARAR MENOS de lo que la evidencia sostiene
    no engaña a nadie —es prudencia, y la sexta condición de `O18` la ampara—, así que no se
    convierte en rojo cuando no hay contraste. Cuando SÍ lo hay, cualquier diferencia sigue
    siendo divergencia, porque entonces la evidencia dice exactamente qué pasó.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-04, sobre `validadores/huella.py` —el
#  instrumento que produce el número que se publica como línea base— y con seis líneas de
#  veneno: un `hashlib.py` homónimo cuyo `sha256()` devuelve siempre el digest esperado.
#
#      $ echo "# CODIGO INYECTADO" >> mutado/kernel/operativo/validadores/ads_lint.py
#      $ cd mutado && python3.12 …/huella.py                     → 8b38fb4f4b07300c
#      $ python3.12 …/comprobar_integridad.py                    → T150 FALLIDA  EXIT=1
#      $ PYTHONPATH=veneno python3.12 …/huella.py                → bc59513f7182130a
#      $ PYTHONPATH=veneno python3.12 …/comprobar_integridad.py  → T150 SUPERADA EXIT=0
#
#  `T150` es la prueba que dice «la huella detecta su edición», y bajo veneno certificaba en
#  VERDE un árbol editado. La causa: la zona `validadores/` estaba ENTERA fuera del
#  inventario de `T306`, de modo que `E-10` —declarado «CERRADO POR INVENTARIO MECÁNICO»—
#  seguía vivo justo en el aparato que produce la evidencia de la certificación.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      Alternativas: (a) importar la purga de un módulo común; (b) copiar el prólogo entero
#      —recital incluido— desde `ads_runtime.py`; (c) copiar el MECANISMO byte a byte y
#      escribir el recital de esta sede.
#      Se elige (c). Con (a) la guardia dependería de un `import`, que es exactamente lo que
#      está protegiendo: una guardia que necesita importar ya ha perdido. Con (b) el recital
#      mentiría, porque el hecho reproducido allí no es el de aquí. Con (c) `T330` exige
#      —y comprueba— que el MECANISMO sea IDÉNTICO byte a byte en todos los puntos
#      ejecutables del árbol (digest `aa219465a6dd6a04`, 1 869 bytes), mientras cada sede
#      dice qué se midió en ella. Lo que protege es el mecanismo; lo que se lee, el recital.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación
#      distinta y convertiría un fallo de entorno en un fallo del aparato. Lo que `E-10`
#      nombra es concreto: `PYTHONPATH` y el `cwd`. Se retiran ésos, se cuenta cuántos, y el
#      recuento queda en `RETIRADAS_DE_LA_RUTA`.
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
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SALIDA = os.path.join(RAIZ, "kernel/operativo/pruebas/REGISTRO-generado.md")

ETIQUETA = {
    "contrato-definido": "CONTRATO DEFINIDO",
    "validador-implementado": "VALIDADOR IMPLEMENTADO",
    "prueba-ejecutada": "PRUEBA EJECUTADA",
    "prueba-superada": "PRUEBA SUPERADA",
    "prueba-fallida": "PRUEBA FALLIDA",
}


# ===========================================================================
#  `ADJ-G2` · EL ESTADO DE UN ESCENARIO, DERIVADO DE SU EVIDENCIA
# ===========================================================================
DIR_PRUEBAS = "kernel/operativo/pruebas"

# Los cinco estados, ORDENADOS por lo que autorizan a decir (`pruebas/REGISTRO.md`). El
# orden importa: `prueba-fallida` NO es «menos» que `prueba-superada`, es OTRA COSA, y por
# eso no se comparan por índice sino por igualdad.
ESTADOS = ("contrato-definido", "validador-implementado", "prueba-ejecutada",
           "prueba-superada", "prueba-fallida")

# Las TRES formas en que una salida publicada dice que TERMINÓ. Se derivan de las tres
# familias de ejecutable que el corpus tiene —validador documental, batería `unittest` y
# guion de escenario extremo a extremo—, y su ausencia con el escenario NOMBRADO significa
# que la salida se cortó: no que la prueba fallara.
CIERRES_DE_SALIDA = (
    re.compile(r"(?m)^\d+ superadas · \d+ fallidas\s*$"),
    re.compile(r"(?m)^(?:OK|OK \([^)]*\)|FAILED \([^)]*\))\s*$"),
    re.compile(r"(?m)^\d+ de \d+ pasos CUMPLIDOS\s*$"),
)

# Los veredictos que una salida publica POR ESCENARIO, en sus dos formas vivas.
_VEREDICTO_DE_VALIDADOR = r"(?m)^%s\s+(SUPERADA|FALLIDA)\b"
_VEREDICTO_DE_BATERIA = (r"(?m)^%s\s+·[^\n]*?\.\.\.\s*"
                         r"(ok|FAIL|ERROR|skipped[^\n]*|expected failure|unexpected success)"
                         r"\s*$")
_VEREDICTOS_BUENOS = ("SUPERADA", "ok")


def veredictos_publicados(texto, identificador):
    """Todo veredicto que una salida publica PARA ESE escenario. Lista vacía = no lo nombra."""
    escapado = re.escape(identificador)
    return (re.findall(_VEREDICTO_DE_VALIDADOR % escapado, texto)
            + re.findall(_VEREDICTO_DE_BATERIA % escapado, texto))


def veredicto_es_bueno(veredicto):
    """`True` si ese veredicto publicado significa que el caso PASÓ.

    Se publica —en vez de dejar `_VEREDICTOS_BUENOS` privado— porque `comprobar_evidencia`
    necesita distinguir un veredicto bueno de uno malo para juzgar si una evidencia
    regenerada ha cambiado de DICTAMEN, y dos definiciones de «esto pasó» son dos verdades.
    Misma razón por la que la derivación del estado vive aquí y no allí.
    """
    return veredicto in _VEREDICTOS_BUENOS


def _script_declarado(datos):
    """El ejecutable que el escenario declara, sin sus argumentos."""
    declarado = (datos.get("validador") or "").strip()
    return os.path.basename(declarado.split()[0]) if declarado else ""


def derivar_estado(datos, raiz):
    """`(estado_derivado, contrastado, motivos)` de un bloque `ads:escenario`.

    `contrastado` dice si la evidencia NOMBRA al escenario. Cuando no lo nombra, el estado
    derivado se queda en lo que la evidencia SÍ sostiene y `contrastado` es `False`: esa
    distinción es la que impide que «no he podido comprobarlo» se convierta en «está bien»,
    que es el modo de fallo que `E-09` cerró en el verificador de admisión.
    """
    motivos = []
    evidencia = (datos.get("evidencia") or "").strip()
    script = _script_declarado(datos)
    if not evidencia:
        if script:
            return "validador-implementado", False, [
                "declara el validador `%s` y no publica evidencia: no consta que se haya "
                "ejecutado sobre material real" % script]
        return "contrato-definido", False, []

    ruta = os.path.join(raiz, DIR_PRUEBAS, evidencia)
    if not os.path.isfile(ruta):
        return "validador-implementado", True, [
            "declara la evidencia `%s` y ese fichero NO EXISTE en el árbol. Una evidencia "
            "que no está no registra ninguna ejecución" % evidencia]
    with open(ruta, encoding="utf-8") as manejador:
        texto = manejador.read()

    codigo = re.search(r"^# codigo:\s*(-?\d+)", texto, re.M)
    orden = re.search(r"^# orden:\s*(.+)$", texto, re.M)
    if not (codigo and orden):
        return "prueba-ejecutada", True, [
            "`%s` no tiene cabecera de procedencia: sin `# orden:` y `# codigo:` no se "
            "puede saber qué la produjo ni cómo terminó" % evidencia]
    if codigo.group(1) != "0":
        return "prueba-fallida", True, [
            "`%s` registra código %s: la ejecución que la produjo no terminó bien"
            % (evidencia, codigo.group(1))]
    if script and script not in orden.group(1):
        return "prueba-ejecutada", True, [
            "`%s` la produjo «%s», que no invoca `%s`, que es el ejecutable que este "
            "escenario declara. Es evidencia de OTRA cosa"
            % (evidencia, orden.group(1).strip(), script)]

    veredictos = veredictos_publicados(texto, datos.get("id", ""))
    if not veredictos:
        return "prueba-ejecutada", False, [
            "`%s` no nombra a `%s` en ninguna línea de veredicto: la ejecución consta, el "
            "resultado DE ESTE escenario no" % (evidencia, datos.get("id"))]
    if not any(c.search(texto) for c in CIERRES_DE_SALIDA):
        return "prueba-ejecutada", True, [
            "`%s` nombra a `%s` y no publica su resumen de cierre: la salida está TRUNCADA, "
            "y una salida cortada no sostiene un verde" % (evidencia, datos.get("id"))]
    malos = [v for v in veredictos if v not in _VEREDICTOS_BUENOS]
    if malos:
        return "prueba-fallida", True, [
            "`%s` publica para `%s` el/los veredicto(s) %s"
            % (evidencia, datos.get("id"), ", ".join(sorted(set(malos))))]
    return "prueba-superada", True, []


# `H-02` · el ORDEN de los cuatro estados PROGRESIVOS, que es lo único comparable.
# `prueba-fallida` queda fuera del orden a propósito: no es «más» ni «menos» que
# `prueba-superada`, es otra cosa, y meterla en una escala convertiría «declaró fallida y la
# evidencia dice superada» en «bajó de estado», que no es lo que pasó.
RANGO_PROGRESIVO = {
    "contrato-definido": 0,
    "validador-implementado": 1,
    "prueba-ejecutada": 2,
    "prueba-superada": 3,
}


def sube_de_estado(declarado, derivado):
    """`True` si `declarado` afirma MÁS garantía de la que `derivado` sostiene.

    Sólo entre los cuatro progresivos. Con `prueba-fallida` en cualquiera de los dos lados
    devuelve `False`: ahí no hay «más», hay «distinto», y eso se juzga por igualdad cuando
    la evidencia nombra al escenario.
    """
    if declarado not in RANGO_PROGRESIVO or derivado not in RANGO_PROGRESIVO:
        return False
    return RANGO_PROGRESIVO[declarado] > RANGO_PROGRESIVO[derivado]


def estado_publicable(datos, raiz):
    """El estado que el registro PUBLICA, y nunca uno superior al que la evidencia sostiene.

    Con contraste, el derivado: la evidencia dice qué pasó. Sin contraste, el declarado —un
    registro que suspende lo que no entiende deja de ser un registro—, SALVO que el
    declarado SUBA por encima del derivado, y entonces se publica el derivado. Ésa era la
    grieta de `H-02`: catorce escenarios publicaban `prueba-superada` sobre una evidencia
    que ni los nombraba, y el registro los copiaba.
    """
    derivado, contrastado, _motivos = derivar_estado(datos, raiz)
    declarado = datos.get("estado")
    if contrastado or sube_de_estado(declarado, derivado):
        return derivado, contrastado
    return declarado, contrastado


def contraste_de_estados(escenarios, raiz):
    """`(divergencias, contrastados, no_contrastables)` sobre todos los escenarios.

    DOS formas de divergencia, y la segunda es la que `H-02` abrió:

      1 · la evidencia NOMBRA al escenario y dice otra cosa que su campo `estado:`. La
          evidencia CONTRADICE lo declarado.
      2 · la evidencia NO lo nombra y el campo `estado:` afirma MÁS de lo que la evidencia
          sostiene. La evidencia NO SOSTIENE lo declarado, que es exactamente «subir de
          estado por argumento».

    «No lo he podido contrastar» sigue siendo la tercera respuesta y sigue publicándose con
    su cifra; lo que ya no es, es un permiso. Cada divergencia lleva `contrastado`, para que
    el diagnóstico diga cuál de las dos formas es.
    """
    divergencias, contrastados, sin_contraste = [], [], []
    for datos in escenarios:
        derivado, contrastado, motivos = derivar_estado(datos, raiz)
        declarado = datos.get("estado")
        (contrastados if contrastado else sin_contraste).append(datos.get("id"))
        if contrastado:
            diverge, porque = derivado != declarado, list(motivos)
        else:
            diverge = sube_de_estado(declarado, derivado)
            porque = list(motivos) + [
                "declara `%s` sobre una evidencia que NO lo nombra y que sólo sostiene "
                "`%s`: eso es subir de estado por argumento, y la regla dura de "
                "`REGISTRO.md` lo prohíbe con o sin contraste" % (declarado, derivado)]
        if diverge:
            divergencias.append({
                "id": datos.get("id"), "declarado": declarado,
                "derivado": derivado, "motivos": porque,
                "contrastado": contrastado,
                "evidencia": datos.get("evidencia") or "—",
            })
    return divergencias, contrastados, sin_contraste


def no_contrastables_por_estado(escenarios, raiz):
    """`{estado declarado: cuántos}` entre los NO contrastables. La frontera, desglosada.

    La cifra agregada de «no contrastables» mezclaba dos cosas muy distintas: los que no
    afirman ninguna ejecución —`contrato-definido`, `validador-implementado`— y los que
    afirmaban `prueba-superada` sin que nada lo sostuviera. El desglose se publica para que
    la mezcla no vuelva a esconder a los segundos.
    """
    reparto = {}
    for datos in escenarios:
        _derivado, contrastado, _motivos = derivar_estado(datos, raiz)
        if not contrastado:
            clave = datos.get("estado")
            reparto[clave] = reparto.get(clave, 0) + 1
    return reparto


def clave(ident: str):
    m = re.match(r"^T(\d+)(?:\.(\d+))?$", ident)
    return (int(m.group(1)), int(m.group(2) or 0)) if m else (9999, 0)


# `H-03` · POR QUÉ ESTE PUNTO EJECUTABLE ANALIZA SUS ARGUMENTOS, Y ANTES NO
#     Al derivar el inventario de puntos ejecutables sobre el árbol entero, `T306` pasó a
#     invocar los treinta y cinco con `--help` bajo un `PYTHONPATH` envenenado. Medido: este
#     módulo NO analizaba `argv`, de modo que `registro_pruebas.py --help` IGNORABA la
#     opción y REGENERABA `REGISTRO-generado.md` sobre el árbol real —`SALIDA` se derivaba
#     de `__file__`—. Un punto ejecutable que ignora lo que se le pide y escribe en el árbol
#     es un defecto por sí solo, y aquí además habría convertido una prueba en un mutador
#     del repositorio que la ejecuta. Se analizan los argumentos, y `--raiz` sirve además
#     para regenerar sobre una copia, que es como lo usan las mutaciones.
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="registro_pruebas",
        description="Regenera pruebas/REGISTRO-generado.md derivando el estado de cada "
                    "escenario de su evidencia.")
    ap.add_argument("--raiz", default=None,
                    help="raíz del corpus sobre la que derivar y escribir (por omisión, "
                         "la del propio árbol)")
    args = ap.parse_args(argv)
    raiz = os.path.abspath(args.raiz or RAIZ)
    salida = os.path.join(raiz, "kernel/operativo/pruebas/REGISTRO-generado.md")
    lint = Lint(raiz, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    escenarios = [(d, f) for t, d, f, _ in lint.bloques if t == "escenario"]
    escenarios.sort(key=lambda par: clave(par[0].get("id", "")))

    fuente = hashlib.sha256()
    for datos, ruta in escenarios:
        fuente.update(repr(sorted(datos.items())).encode("utf-8"))

    lineas = [
        "# REGISTRO DE PRUEBAS — generado",
        "",
        "<!-- GENERADO por validadores/registro_pruebas.py. No editar a mano. -->",
        f"<!-- source_revision: {fuente.hexdigest()[:16]} -->",
        "",
        "Fuente: los bloques `ads:escenario` de `kernel/operativo/` y `packs/`.",
        "Los cuatro estados y qué autoriza a decir cada uno: [`REGISTRO.md`](REGISTRO.md).",
        "",
    ]
    # `ADJ-G2` · el registro publica el estado DERIVADO de la evidencia, no el escrito a
    # mano. Lo escrito a mano sigue apareciendo, pero SÓLO cuando diverge y marcado como lo
    # que es: una declaración que su evidencia no sostiene.
    derivados = {}
    divergencias, contrastados, sin_contraste = contraste_de_estados(
        [d for d, _ in escenarios], raiz)
    reparto = no_contrastables_por_estado([d for d, _ in escenarios], raiz)
    sin_contraste_ids = set(sin_contraste)
    for datos, _ in escenarios:
        derivados[datos.get("id")] = estado_publicable(datos, raiz)[0]
    por_id = {d["id"]: d for d in divergencias}

    resumen = {}
    for datos, _ in escenarios:
        estado = derivados[datos.get("id")]
        resumen[estado] = resumen.get(estado, 0) + 1
    lineas.append("## Recuento")
    lineas.append("")
    lineas.append("| estado | pruebas |")
    lineas.append("|---|---|")
    for estado in ["contrato-definido", "validador-implementado", "prueba-ejecutada",
                   "prueba-superada", "prueba-fallida"]:
        lineas.append(f"| {ETIQUETA[estado]} | {resumen.get(estado, 0)} |")
    lineas.append(f"| **total** | **{len(escenarios)}** |")
    lineas.append("")
    lineas.append("## Detalle")
    lineas.append("")
    lineas.append("| id | prueba | cubre | ejecución | estado DERIVADO | evidencia |")
    lineas.append("|---|---|---|---|---|---|")
    for datos, ruta in escenarios:
        rel = os.path.relpath(ruta, os.path.join(raiz, "kernel/operativo/pruebas"))
        cubre = " · ".join(datos.get("cubre", []))
        estado = derivados[datos.get("id")]
        marca = ""
        if datos.get("id") in sin_contraste_ids:
            marca = " · SIN CONTRASTE: su evidencia no lo nombra"
        if datos.get("id") in por_id:
            marca = (" · DECLARA `" + str(datos.get("estado"))
                     + "`, que su evidencia NO sostiene")
        lineas.append(
            f"| [{datos.get('id')}]({rel}) | {datos.get('nombre','')} | {cubre} |"
            f" {datos.get('ejecucion','')} | **{ETIQUETA.get(estado, '?')}**{marca} |"
            f" {datos.get('evidencia') or '—'} |")
    lineas.append("")

    # `ADJ-G2` · la COBERTURA DEL CONTRASTE, publicada. Un contraste que se aplica a la
    # mitad del corpus sin decirlo es peor que ninguno: hace creer que cubre el todo.
    lineas.append("## Contraste del estado contra la evidencia")
    lineas.append("")
    lineas.append(f"Escenarios cuya evidencia los NOMBRA y por tanto se contrastan: "
                  f"**{len(contrastados)}** de **{len(escenarios)}**.")
    lineas.append("")
    lineas.append(f"No contrastables —su evidencia no publica una línea de veredicto con su "
                  f"identificador—: **{len(sin_contraste)}**. Para éstos el estado derivado "
                  f"es el que la evidencia SÍ sostiene, y no se sube por omisión.")
    lineas.append("")
    # `H-02` · el DESGLOSE de esa cifra. Agregada escondía dos cosas distintas: los que no
    # afirman ninguna ejecución y los que afirmaban `prueba-superada` sin sostén.
    lineas.append("Desglose de los NO contrastables por el estado que DECLARAN —la cifra "
                  "agregada mezclaba a los que no afirman ninguna ejecución con los que "
                  "afirmaban una que su evidencia no nombra, que es lo que `H-02` "
                  "encontró—:")
    lineas.append("")
    lineas.append("| estado declarado | escenarios |")
    lineas.append("|---|---|")
    for estado in ["contrato-definido", "validador-implementado", "prueba-ejecutada",
                   "prueba-superada", "prueba-fallida"]:
        if reparto.get(estado):
            lineas.append(f"| {estado} | {reparto[estado]} |")
    lineas.append("")
    if divergencias:
        lineas.append("| id | declarado a mano | derivado de la evidencia | motivo |")
        lineas.append("|---|---|---|---|")
        for d in divergencias:
            lineas.append(f"| {d['id']} | {d['declarado']} | {d['derivado']} |"
                          f" {' · '.join(d['motivos']) or '—'} |")
    else:
        lineas.append("Ninguna divergencia: todo `estado:` declarado coincide con el que su "
                      "evidencia sostiene.")
    lineas.append("")

    with open(salida, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lineas))
    print(f"{len(escenarios)} escenarios · {salida}")
    print(f"contraste del estado: {len(contrastados)} contrastados · "
          f"{len(sin_contraste)} no contrastables · {len(divergencias)} divergencias")
    print("no contrastables por estado declarado: "
          + " · ".join(f"{e} {n}" for e, n in sorted(reparto.items())))
    for d in divergencias:
        print(f"  · {d['id']}: declara {d['declarado']} y su evidencia sostiene "
              f"{d['derivado']}"
              + ("" if d["contrastado"] else " (y ni siquiera lo nombra)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
