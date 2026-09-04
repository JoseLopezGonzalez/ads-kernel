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

DECISIÓN · lo que la evidencia NO NOMBRA se declara NO CONTRASTABLE, y no se aprueba ni se suspende
    Alternativas: (a) exigir que toda evidencia nombre a todo escenario que la cita, y dar
    ROJO si no; (b) contrastar donde se puede y PUBLICAR la cobertura del contraste.
    Se elige (b). Con (a) el corpus se pondría rojo en 30 escenarios que están bien —hay
    baterías cuya salida no imprime una línea por escenario, y hay escenarios cuya
    evidencia se regenera en otra pasada—, y un guardián que da treinta rojos falsos se
    apaga en una semana. Con (b) no hay ni un rojo falso, la cobertura del contraste se
    PUBLICA con su cifra, y quien la vea bajar tiene delante el número. Es la sexta
    condición de `O18`: no se promete más garantía de la que se entrega.
"""
from __future__ import annotations

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


def estado_publicable(datos, raiz):
    """El estado que el registro PUBLICA: el derivado si hay contraste, el declarado si no.

    Y cuando no hay contraste se dice. La alternativa —publicar el derivado igualmente—
    bajaría de estado a treinta y tantos escenarios que están bien sólo porque la salida de
    su batería no imprime una línea por escenario, y un registro que suspende lo que no
    entiende deja de ser un registro.
    """
    derivado, contrastado, _motivos = derivar_estado(datos, raiz)
    return (derivado if contrastado else datos.get("estado")), contrastado


def contraste_de_estados(escenarios, raiz):
    """`(divergencias, contrastados, no_contrastables)` sobre todos los escenarios.

    Una DIVERGENCIA sólo se declara cuando la evidencia NOMBRA al escenario y dice otra
    cosa que su campo `estado:`. «No lo he podido contrastar» no es «diverge», y tampoco es
    «está bien»: es la tercera respuesta, y va publicada con su cifra.
    """
    divergencias, contrastados, sin_contraste = [], [], []
    for datos in escenarios:
        derivado, contrastado, motivos = derivar_estado(datos, raiz)
        (contrastados if contrastado else sin_contraste).append(datos.get("id"))
        if contrastado and derivado != datos.get("estado"):
            divergencias.append({
                "id": datos.get("id"), "declarado": datos.get("estado"),
                "derivado": derivado, "motivos": motivos,
                "evidencia": datos.get("evidencia") or "—",
            })
    return divergencias, contrastados, sin_contraste


def clave(ident: str):
    m = re.match(r"^T(\d+)(?:\.(\d+))?$", ident)
    return (int(m.group(1)), int(m.group(2) or 0)) if m else (9999, 0)


def main() -> int:
    lint = Lint(RAIZ, ["kernel/operativo", "packs"])
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
        [d for d, _ in escenarios], RAIZ)
    sin_contraste_ids = set(sin_contraste)
    for datos, _ in escenarios:
        derivados[datos.get("id")] = estado_publicable(datos, RAIZ)[0]
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
        rel = os.path.relpath(ruta, os.path.join(RAIZ, "kernel/operativo/pruebas"))
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

    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lineas))
    print(f"{len(escenarios)} escenarios · {SALIDA}")
    print(f"contraste del estado: {len(contrastados)} contrastados · "
          f"{len(sin_contraste)} no contrastables · {len(divergencias)} divergencias")
    for d in divergencias:
        print(f"  · {d['id']}: declara {d['declarado']} y su evidencia sostiene "
              f"{d['derivado']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
