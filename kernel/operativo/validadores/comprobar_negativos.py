#!/usr/bin/env python3
"""comprobar_negativos — demuestra que los validadores FALLAN cuando deben fallar.

Un validador que sólo se ha visto pasar no está verificado: puede estar comprobando
menos de lo que su nombre afirma, y nadie lo sabría. Es exactamente el defecto que la
auditoría independiente encontró en T131 y T134.

Cómo funciona, y por qué es seguro:

  1. copia el repositorio COMPLETO a un directorio temporal del sistema
  2. introduce en la COPIA una infracción deliberada y concreta
  3. ejecuta el validador contra la copia, con --raiz
  4. exige que la prueba señalada FALLE
  5. borra el directorio temporal

El corpus real NUNCA se modifica. No hay restauración que pueda salir mal porque no hay
nada que restaurar: se trabaja siempre sobre la copia.

Uso:
  python3 kernel/operativo/validadores/comprobar_negativos.py [--json] [--caso N136]
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
VALIDADORES = "kernel/operativo/validadores"


class Mutacion:
    """Una infracción deliberada, y la prueba que TIENE que detectarla."""

    def __init__(self, mid, hallazgo, prueba, validador, descripcion, aplicar):
        self.id = mid
        self.hallazgo = hallazgo
        self.prueba = prueba
        self.validador = validador
        self.descripcion = descripcion
        self.aplicar = aplicar          # f(raiz_copia) -> None
        self.resultado = None           # "detectada" | "NO DETECTADA" | "error: ..."
        self.detalle = ""


# ---------------------------------------------------------------------------
# utilidades de mutación
# ---------------------------------------------------------------------------

def _sustituir(raiz, rel, viejo, nuevo):
    ruta = os.path.join(raiz, rel)
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    if viejo not in texto:
        raise RuntimeError(f"la mutación no encaja: no encuentro el texto en {rel}")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto.replace(viejo, nuevo, 1))


def _escribir(raiz, rel, contenido):
    ruta = os.path.join(raiz, rel)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(contenido)


# ---------------------------------------------------------------------------
# el catálogo de mutaciones
# ---------------------------------------------------------------------------

def m_veto_arbitra(raiz):
    _sustituir(raiz, "kernel/operativo/capacidades/DOM/CAPACIDAD.md",
               "Frente al veto de DIS por degradación de forma, DOM NO prevalece",
               "Frente al veto de DIS por degradación de forma, prevalece DOM")


def m_veto_sin_escalado(raiz):
    _sustituir(raiz, "kernel/operativo/capacidades/VER/CAPACIDAD.md",
               "y escalan\n  al Owner.", "y se resuelven entre ellos.")


def m_dsp_decide_cancelar(raiz):
    _sustituir(raiz, "kernel/operativo/capacidades/DSP/roles/estado.md",
               '    - "detener el ciclo tras tres fallos de comparación e intercambio, dejando las órdenes intactas"',
               '    - "detener el ciclo tras tres fallos de comparación e intercambio, dejando las órdenes intactas"\n'
               '    - "cancelar el paquete cuando la espera deja de ser viable"')


def m_rol_decide_de_mas(raiz):
    _sustituir(raiz, "kernel/operativo/capacidades/CON/roles/implementacion.md",
               "  decide:",
               '  decide:\n    - "el alcance de producto que se implementa"')


def m_metodo_sin_termina_cuando(raiz):
    _sustituir(raiz, "kernel/operativo/capacidades/INV/metodos/Investigacion.md",
               "    termina_cuando:", "    termina_cuandoX:")


def m_documento_huerfano_con_nombre_repetido(raiz):
    """A-05 · el caso EXACTO que derrotaba a T134.

    Un documento al que nadie enlaza, en un directorio que nadie referencia, pero cuyo
    nombre base coincide con el de otros dieciocho ficheros del corpus.
    """
    _escribir(raiz, "kernel/operativo/capacidades/DIS/huerfano/composicion.md",
              "# huerfano\n\nNadie enlaza esto por ruta y no declara ningun bloque canonico.\n")


def m_enlace_a_basename_equivocado(raiz):
    _sustituir(raiz, "kernel/operativo/00-INDICE.md",
               "[`00-LENGUAJE.md`](esquemas/00-LENGUAJE.md)",
               "[`00-LENGUAJE.md`](contratos/00-LENGUAJE.md)")


def m_exclusion_sin_motivo(raiz):
    """A-05 · una exclusión sin justificación escrita deja de ser revisable."""
    _sustituir(raiz, VALIDADORES + "/exclusiones.yaml",
               '  - ruta: docs/rediseno/a-EQUIPOS-v1-RECHAZADA.md\n'
               '    motivo: "versión rechazada del rediseño; se conserva para trazabilidad de (a)"',
               '  - ruta: docs/rediseno/a-EQUIPOS-v1-RECHAZADA.md')


def m_exclusion_caducada(raiz):
    """A-05 · una exclusión cuyo objetivo ya no existe: restos que nadie revisa."""
    _sustituir(raiz, VALIDADORES + "/exclusiones.yaml",
               "no_analizados:",
               'no_analizados:\n  - ruta: packs/pack-que-ya-no-existe.md\n'
               '    motivo: "resto de una exclusión antigua"')


def m_validador_editado(raiz):
    """A-04 · fork silencioso de un validador: kernel-status DEBE verlo."""
    ruta = os.path.join(raiz, VALIDADORES, "ads_lint.py")
    with open(ruta, "a", encoding="utf-8") as fh:
        fh.write("\n# fork silencioso introducido por comprobar_negativos\n")


def m_tooling_editado(raiz):
    ruta = os.path.join(raiz, "tooling/new-project.sh")
    with open(ruta, "a", encoding="utf-8") as fh:
        fh.write("\n# fork silencioso introducido por comprobar_negativos\n")


def m_huella_estrechada(raiz):
    """A-04 · alguien «arregla» la integridad estrechando la huella hasta no ver nada."""
    _sustituir(raiz, VALIDADORES + "/huella.py",
               'EXTENSIONES = (".md", ".yaml", ".yml", ".py", ".sh")',
               'EXTENSIONES = (".md", ".yaml")')


def m_pack_menos_restrictivo_gana(raiz):
    """A-03 · la resolución deja de tomar lo más restrictivo. T149 tiene que verlo.

    Se invierte la semántica de la dirección en el resolutor: `minimo` pasa a quedarse con
    el valor menor. Es EXACTAMENTE el defecto que T131 no podía detectar cuando sólo
    comprobaba que dos campos de YAML no estuvieran vacíos.
    """
    _sustituir(raiz, VALIDADORES + "/composicion_packs.py",
               'if direccion == "minimo":\n        return max(a, b)',
               'if direccion == "minimo":\n        return min(a, b)')


def m_composicion_sin_motivo(raiz):
    """A-03 · la resolución deja de registrar POR QUÉ gana el valor elegido."""
    _sustituir(raiz, VALIDADORES + "/composicion_packs.py",
               '            "motivo": (f"la propiedad es un', '            "motivo": "",\n            "_motivo_desactivado": (f"la propiedad es un')


def m_composicion_depende_del_orden(raiz):
    """A-03 · la resolución deja de ser independiente del orden de entrada."""
    _sustituir(raiz, VALIDADORES + "/composicion_packs.py",
               'packs = sorted(packs, key=lambda p: p.get("id", ""))',
               'packs = list(packs)')


def m_composicion_incompatible_silenciosa(raiz):
    """A-03 · dos packs no comparables dejan de fallar de forma explícita."""
    _sustituir(raiz, VALIDADORES + "/composicion_packs.py",
               "        if len(direcciones) > 1:", "        if False:")


def m_arranque_con_pack_derogado(raiz):
    _sustituir(raiz, "README.md",
               "./tooling/new-project.sh mi-web-app web-app",
               "./tooling/new-project.sh mi-web-app pack-web-app")


def m_version_incoherente(raiz):
    _sustituir(raiz, "kernel/VERSION", "2.0.0", "9.9.9")


def m_encuadre_sin_estado_exigido(raiz):
    _sustituir(raiz, "kernel/operativo/esquemas/encuadre.yaml",
               "esperando-owner, ", "")


def m_nivel_sin_gate(raiz):
    """A-08 · la tabla de estaciones vuelve a saltarse los dos gates en N0."""
    _sustituir(raiz, "kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md",
               "N0  1 · 8 · 9 · 10 · 11 · 13", "N0  1 · 10 · 11")


def m_nivel_sin_gate_obligatorio(raiz):
    """A-08 · un nivel deja de declarar obligatorio el gate visual."""
    _sustituir(raiz, "kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md",
               "id: N0\nnombre: Extensión de patrón vigente\norden: 5\nmetodo: DIS/Evolucion",
               "id: N0\nnombre: Extensión de patrón vigente\norden: 5\nmetodo: DIS/Evolucion")
    _sustituir(raiz, "kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md",
               "gates_obligatorios: [gate:usabilidad, gate:excelencia-visual]\nejes_reutilizables: [personalidad, intencion, jerarquia, sistema, actualidad, respuesta, alma]",
               "gates_obligatorios: [gate:usabilidad]\nejes_reutilizables: [personalidad, intencion, jerarquia, sistema, actualidad, respuesta, alma]")


def m_n3_inalcanzable(raiz):
    """A-07 · se vuelve a la condición que hacía inalcanzable la Reconstrucción."""
    _sustituir(raiz, "kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md",
               'condicion_formal: "dir_sustituye or (not superficie_construida and not memoria_vigente)"',
               'condicion_formal: "dir_sustituye or not memoria_vigente"')


def m_escala_no_total(raiz):
    """A-07 · una condición se estrecha y quedan casos sin ningún nivel."""
    _sustituir(raiz, "kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md",
               'condicion_formal: "memoria_vigente and patron_cubre"',
               'condicion_formal: "memoria_vigente and patron_cubre and premium_o_nuevo"')


def m_cierre_sin_obligaciones(raiz):
    """A-09 · el gate de cierre pierde la comprobación de obligaciones huérfanas."""
    _sustituir(raiz, "kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md",
               "  - id: obligaciones-resueltas", "  - id: obligaciones-contadas")


def m_dsp_retira_obligacion(raiz):
    """A-09 · DSP se concede la autoridad de retirar una obligación."""
    _sustituir(raiz, "kernel/operativo/recorrido/01-PROCESOS.md",
               "    autoridad_de_retirada: >\n      PRD, y el Owner cuando el alcance retirado es materia suya (a.8)",
               "    autoridad_de_retirada: >\n      DSP, al recomponer la ruta sin avance material")


def m_informe_suma(raiz):
    """A-09 · la plantilla de cierre deja de separar satisfechas de retiradas."""
    _sustituir(raiz, "kernel/operativo/plantillas/CIERRE.md",
               "OBLIGACIONES RETIRADAS     <M>", "OBLIGACIONES TOTALES       <N+M>")


def m_freno_sin_ejecutor(raiz):
    """A-10 · DSP se queda sin el rol que ejecuta los frenos."""
    _sustituir(raiz, "kernel/operativo/capacidades/DSP/CAPACIDAD.md",
               "roles: [DSP/enrutamiento, DSP/estado, DSP/supervision]",
               "roles: [DSP/enrutamiento, DSP/estado]")


def m_freno_sin_gate(raiz):
    """A-10 · el gate de despacho deja de exigir que los frenos se hayan evaluado."""
    _sustituir(raiz, "kernel/operativo/capacidades/DSP/CAPACIDAD.md",
               "  - id: frenos-evaluados", "  - id: frenos-mencionados")


def m_supervisor_no_independiente(raiz):
    """A-10 · quien recompone pasa a contar sus propias recomposiciones."""
    _sustituir(raiz, "kernel/operativo/capacidades/DSP/roles/supervision.md",
               "independencia:\n  requiere_independencia: true",
               "independencia:\n  requiere_independencia: false")


def m_umbral_inventado(raiz):
    """A-10 · alguien ajusta un umbral aprobado porque el caso parecía merecerlo."""
    _sustituir(raiz, "kernel/operativo/capacidades/DSP/prompts/supervision.md",
               "RACHA SIS    = 2", "RACHA SIS    = 5")


CATALOGO = [
    Mutacion("N136", "A-06", "T136", "comprobar_contratos",
             "un veto levantable (DOM) se declara prevaleciente sobre otro (DIS)",
             m_veto_arbitra),
    Mutacion("N136b", "A-06", "T136", "comprobar_contratos",
             "una cláusula de colisión resuelve el conflicto sin escalar al Owner",
             m_veto_sin_escalado),
    Mutacion("N137", "A-23", "T137", "comprobar_contratos",
             "DSP/estado vuelve a DECIDIR una cancelación",
             m_dsp_decide_cancelar),
    Mutacion("N146", "A-18", "T146", "comprobar_contratos",
             "un rol decide algo que su capacidad no tiene en decide_sola",
             m_rol_decide_de_mas),
    Mutacion("N91", "—", "T91", "comprobar_contratos",
             "un paso de método pierde su condición de salida",
             m_metodo_sin_termina_cuando),
    Mutacion("N147", "A-05", "T147", "comprobar_referencias",
             "documento huérfano cuyo nombre base coincide con otros dieciocho",
             m_documento_huerfano_con_nombre_repetido),
    Mutacion("N147b", "A-05", "T147", "comprobar_referencias",
             "un enlace apunta al nombre correcto en la carpeta equivocada",
             m_enlace_a_basename_equivocado),
    Mutacion("N147c", "A-05", "T147", "comprobar_referencias",
             "una exclusión se queda sin motivo escrito",
             m_exclusion_sin_motivo),
    Mutacion("N147d", "A-05", "T147", "comprobar_referencias",
             "una exclusión apunta a algo que ya no existe",
             m_exclusion_caducada),
    Mutacion("N150", "A-04", "T150", "comprobar_integridad",
             "un validador del kernel se edita localmente",
             m_validador_editado),
    Mutacion("N150b", "A-04", "T150", "comprobar_integridad",
             "un script de tooling se edita localmente",
             m_tooling_editado),
    Mutacion("N150c", "A-04", "T150", "comprobar_integridad",
             "la definición de la huella se estrecha hasta dejar fuera a los validadores",
             m_huella_estrechada),
    Mutacion("N149", "A-03", "T149", "comprobar_packs",
             "la resolución se queda con el valor MENOS restrictivo",
             m_pack_menos_restrictivo_gana),
    Mutacion("N149b", "A-03", "T149", "comprobar_packs",
             "la resolución deja de registrar por qué gana el valor elegido",
             m_composicion_sin_motivo),
    Mutacion("N149c", "A-03", "T149", "comprobar_packs",
             "la resolución pasa a depender del orden de los packs de entrada",
             m_composicion_depende_del_orden),
    Mutacion("N149d", "A-03", "T149", "comprobar_packs",
             "una composición no comparable se resuelve en silencio en vez de fallar",
             m_composicion_incompatible_silenciosa),
    Mutacion("N148", "A-02", "T148", "comprobar_arranque",
             "la documentación vuelve a citar un pack derogado",
             m_arranque_con_pack_derogado),
    Mutacion("N151", "A-12", "T151", "comprobar_versiones",
             "kernel/VERSION deja de concordar con la política de versiones",
             m_version_incoherente),
    Mutacion("N142", "A-11", "T142", "comprobar_contratos",
             "el esquema de encuadre pierde un estado que sus métodos exigen",
             m_encuadre_sin_estado_exigido),
    Mutacion("N139", "A-08", "T139", "comprobar_contratos",
             "la tabla de estaciones vuelve a saltarse los dos gates en N0",
             m_nivel_sin_gate),
    Mutacion("N139b", "A-08", "T139", "comprobar_contratos",
             "un nivel deja de declarar obligatorio el gate de excelencia visual",
             m_nivel_sin_gate_obligatorio),
    Mutacion("N138", "A-07", "T138", "comprobar_contratos",
             "se vuelve a la condición que hacía inalcanzable la Reconstrucción (N3)",
             m_n3_inalcanzable),
    Mutacion("N138b", "A-07", "T138", "comprobar_contratos",
             "una condición se estrecha y quedan casos sin ningún nivel",
             m_escala_no_total),
    Mutacion("N140", "A-09", "T140", "comprobar_contratos",
             "el gate de cierre pierde la comprobación de obligaciones huérfanas",
             m_cierre_sin_obligaciones),
    Mutacion("N140b", "A-09", "T140", "comprobar_contratos",
             "DSP se concede la autoridad de retirar una obligación",
             m_dsp_retira_obligacion),
    Mutacion("N140c", "A-09", "T140", "comprobar_contratos",
             "la plantilla de cierre suma satisfechas y retiradas",
             m_informe_suma),
    Mutacion("N141", "A-10", "T141", "comprobar_contratos",
             "DSP se queda sin el rol que ejecuta los frenos",
             m_freno_sin_ejecutor),
    Mutacion("N141b", "A-10", "T141", "comprobar_contratos",
             "el gate de despacho deja de exigir que los frenos se hayan evaluado",
             m_freno_sin_gate),
    Mutacion("N141c", "A-10", "T141", "comprobar_contratos",
             "quien recompone la ruta pasa a contar sus propias recomposiciones",
             m_supervisor_no_independiente),
    Mutacion("N141d", "A-10", "T141", "comprobar_contratos",
             "se ajusta un umbral aprobado porque el caso parecía merecerlo",
             m_umbral_inventado),
]


def copiar_corpus(destino):
    def ignorar(directorio, nombres):
        return [n for n in nombres if n in (".git", "__pycache__", ".pytest_cache")]
    shutil.copytree(RAIZ, destino, ignore=ignorar, symlinks=True)


def ejecutar(mut, tmp_base):
    destino = os.path.join(tmp_base, mut.id)
    copiar_corpus(destino)
    try:
        mut.aplicar(destino)
    except Exception as exc:                                   # noqa: BLE001
        mut.resultado = "error"
        mut.detalle = f"no se pudo aplicar la mutación: {exc}"
        return
    script = os.path.join(destino, VALIDADORES, f"{mut.validador}.py")
    if not os.path.exists(script):
        mut.resultado = "error"
        mut.detalle = f"el validador {mut.validador}.py todavía no existe"
        return
    proc = subprocess.run([sys.executable, script, "--json", "--raiz", destino],
                          capture_output=True, text=True)
    try:
        datos = json.loads(proc.stdout)
    except json.JSONDecodeError:
        mut.resultado = "error"
        mut.detalle = f"salida no interpretable (exit {proc.returncode}): {proc.stderr[:200]}"
        return
    fila = next((d for d in datos if d.get("id") == mut.prueba), None)
    if fila is None:
        mut.resultado = "NO DETECTADA"
        mut.detalle = f"{mut.prueba} no aparece en la salida de {mut.validador}"
    elif fila.get("estado") == "prueba-fallida":
        mut.resultado = "detectada"
        mut.detalle = (fila.get("fallos") or ["(sin detalle)"])[0][:120]
    else:
        mut.resultado = "NO DETECTADA"
        mut.detalle = f"{mut.prueba} siguió SUPERADA con la infracción introducida"


def main():
    ap = argparse.ArgumentParser(description="pruebas negativas de los validadores ADS")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--caso", default=None, help="ejecutar sólo una mutación por id")
    args = ap.parse_args()

    casos = [m for m in CATALOGO if not args.caso or m.id == args.caso]
    tmp_base = tempfile.mkdtemp(prefix="ads-negativos-")
    try:
        for mut in casos:
            ejecutar(mut, tmp_base)
    finally:
        shutil.rmtree(tmp_base, ignore_errors=True)

    fallidas = [m for m in casos if m.resultado != "detectada"]
    if args.json:
        print(json.dumps([{"id": m.id, "hallazgo": m.hallazgo, "prueba": m.prueba,
                           "validador": m.validador, "infraccion": m.descripcion,
                           "resultado": m.resultado, "detalle": m.detalle}
                          for m in casos], ensure_ascii=False, indent=2))
    else:
        for m in casos:
            marca = "OK  " if m.resultado == "detectada" else "FALLO"
            print(f"{marca} {m.id:7} {m.hallazgo:5} {m.prueba:5} {m.descripcion}")
            print(f"                          → {m.resultado}: {m.detalle}")
        print(f"\n{len(casos) - len(fallidas)} infracciones detectadas · "
              f"{len(fallidas)} NO detectadas")
    return 1 if fallidas else 0


if __name__ == "__main__":
    sys.exit(main())
