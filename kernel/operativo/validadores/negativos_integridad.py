"""negativos_integridad — infracciones deliberadas de la corrección del 2026-09-04.

POR QUÉ ESTE FICHERO EXISTE, Y NO UNA LÍNEA MÁS EN `comprobar_negativos.py`. La corrección
de los hallazgos `E-01`…`E-16` se reparte en tres ejes disjuntos que se escriben en
paralelo. Tres ejes escribiendo sobre la MISMA lista producen una integración que nadie
puede revisar por partes, y la lista de sabotajes es justamente lo que no puede quedar sin
revisar. Cada eje escribe el suyo AQUÍ, y `comprobar_negativos.py` los INCORPORA por
nombre, sin descubrimiento y sin `try/except ImportError`: si uno falta, el validador
revienta al importar, que es exactamente lo que tiene que pasar. El catálogo sigue siendo
UNO y la sede de ejecución sigue siendo UNA.

Cada entrada es una `comprobar_negativos.Mutacion`. Se construyen aquí y se comprueban
allí.

QUÉ SABOTEA ESTE EJE, y por qué son éstas y no otras. `E-14` es el hallazgo de este eje que
un validador del corpus puede juzgar: la evidencia publicada es un FICHERO del árbol, y
`comprobar_evidencia.py` es quien la mira. Los demás hallazgos de este eje —`E-07`, `E-08`,
`E-09`, `E-10`, `E-15`, `E-16`— viven en el runtime, y sus sabotajes se ejercen sobre el
CÓDIGO, no sobre el corpus: su matriz «sano → VERDE, sabotaje → ROJO, restaurado → VERDE»
está en el informe de la corrección y se reproduce ejecutando las baterías del runtime
sobre una copia saboteada. Meterlos aquí exigiría que `comprobar_negativos` ejecutara las
baterías del runtime dentro de cada copia del corpus, que es otro aparato y otra decisión.

DECISIÓN · se sabotea `contencion-salida.txt` y no un fichero inventado
    Alternativas: (a) crear un fichero de evidencia nuevo para saboteario; (b) mutar uno de
    los que el manifiesto ya declara.
    Se elige (b). Un fichero nuevo no lo declara ningún componente, y `comprobar_evidencia`
    lo rechazaría por HUÉRFANO —comprobación 9— antes de llegar a mirar su contenido: la
    mutación se «detectaría» por el motivo equivocado. Mutando uno declarado, lo único que
    cambia es aquello que se quiere medir.
"""
# ---------------------------------------------------------------------------
#  ADVERTENCIA DE FORMA · este módulo NO lleva línea de intérprete, y es deliberado.
#
#  `H-03` de la auditoría independiente del 2026-09-04 obligó a que el inventario de puntos
#  ejecutables se derive del ÁRBOL ENTERO y a que TODO `.py` quede clasificado —el
#  inventario anterior era mecánico DENTRO de dos zonas escritas a mano, y por eso
#  `validadores/` estaba entera fuera del control mientras `H-01` encontraba el defecto
#  `E-10` vivo en `huella.py`—. La equivalencia que `T330` comprueba sobre el disco es:
#
#      lleva `#!`   ⟺   es INVOCABLE   ⟺   lleva el MECANISMO `E-10`
#
#  Este módulo se IMPORTA —`comprobar_negativos.py` lo incorpora por nombre y sin
#  `try/except`— y no se ejecuta: no define `__main__` ni sale desde el nivel superior. No
#  cumple el segundo término, así que tampoco puede llevar el primero: una línea de
#  intérprete presenta un módulo como ejecutable, y a un ejecutable esta equivalencia le
#  exige la purga. Se retira la línea, y con ella la ambigüedad. Es exactamente lo que
#  `ADJ-B2` hizo con `errores.py`, `firma.py`, `atestacion.py` y `aislamiento.py` de la
#  raíz externa.
# ---------------------------------------------------------------------------

from __future__ import annotations

import os
import re
import subprocess
import sys

from comprobar_negativos import Mutacion, _escribir, _sustituir

EVIDENCIA = "kernel/operativo/pruebas/evidencia/contencion-salida.txt"


def m_e14_ok_con_saltos(raiz):
    """`E-14` · `OK` se convierte en `OK (skipped=3)`, que la firma vieja casaba igual."""
    _sustituir(raiz, EVIDENCIA, "\nOK\n", "\nOK (skipped=3)\n")


def m_e14_contador_inflado(raiz):
    """`E-14` · el contador publicado deja de describir la corrida que lo acompaña.

    La cifra se LEE de la evidencia y no se escribe aquí. Estaba escrita —«Ran 20 tests»— y
    caducó en cuanto la batería de contención creció a veinticinco casos: la mutación dejó
    de encajar y el control negativo se apagó sin que su fallo dijera nada del corpus, sólo
    de sí mismo. Un sabotaje que hay que mantener a mano cada vez que una batería crece es
    un sabotaje que algún día no se mantendrá.
    """
    ruta = os.path.join(raiz, EVIDENCIA)
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    m = re.search(r"^Ran (\d+) tests", texto, re.M)
    if not m:
        raise RuntimeError("`%s` no publica ningún «Ran <n> tests»: sin contador no hay "
                           "contador que inflar, y este sabotaje no mide nada" % EVIDENCIA)
    _sustituir(raiz, EVIDENCIA, m.group(0), "Ran %d tests" % (int(m.group(1)) + 79))


def m_e14_salida_recortada(raiz):
    """`E-14` · se recorta la salida y el contador se queda diciendo lo que decía."""
    _sustituir(raiz, EVIDENCIA,
               "T214 · Defecto que previene: elegir un backend sin haber mirado los demás. ... ok",
               "T214 · Defecto que previene: elegir un backend sin haber mirado los demás.")


def m_e14_exito_con_fallos(raiz):
    """`E-14` · un `OK` que declara fallos dentro del paréntesis y aun así dice OK."""
    _sustituir(raiz, EVIDENCIA, "\nOK\n", "\nOK (failures=1)\n")


def m_e14_dos_corridas_pegadas(raiz):
    """`E-14` · dos corridas en el mismo fichero: se publica la buena y se esconde la mala."""
    _sustituir(
        raiz, EVIDENCIA, "\nOK\n",
        "\nFAILED (errors=1)\n\n"
        "----------------------------------------------------------------------\n"
        "Ran 20 tests  (duración no registrada: varía por ejecución)\n\nOK\n")


# ===========================================================================
#  `ADJ-G3` y `ADJ-M5` · LAS SEDES VERACES Y LA FRONTERA DEL BARRIDO
# ===========================================================================
#  Los dos hallazgos que este eje puede sabotear sobre el CORPUS, que es lo que
#  `comprobar_negativos` sabe mutar. Los otros cuatro del lote —`ADJ-M1`, `ADJ-M2`, `ADJ-M3`
#  y `ADJ-M11`— viven en el CÓDIGO y sus sabotajes se ejercen copiando el repositorio y
#  volviendo a correr el escenario que los mide; meterlos aquí exigiría que este validador
#  ejecutara los tres E2E dentro de cada copia, que es otro aparato y otra decisión.
#
#  DECISIÓN · se sabotea la PROPIEDAD, no la frase concreta que el gate citó
#      `NG3e` no reintroduce ninguna de las once líneas que el gate encontró: fabrica una
#      sede NUEVA —ruta nueva, nombre nuevo, contenido nuevo— que niega una pieza construida.
#      Si `T360` sólo cazara las once, la cuarta recurrencia se escribiría en otro fichero y
#      pasaría en verde, que es exactamente como llegó la tercera.
SEDE_CONTRATOS = "docs/canonico/04-CONTRATOS-TECNICOS.md"
SEDE_PLAN = "docs/canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md"
VALIDADOR_RECUENTOS = "kernel/operativo/validadores/comprobar_recuentos.py"


def m_g3_ninguno_existe(raiz):
    """`ADJ-G3` · vuelve a declarar inexistentes los adaptadores en §5.3.

    La frase se devuelve al PÁRRAFO donde estaba —el primero de §5.3, el que la cabecera
    encabeza—, y no a cualquier sitio de la sección: reproducir el defecto es reproducir
    dónde estaba, porque de eso depende a qué se refiere la negación.
    """
    _sustituir(raiz, SEDE_CONTRATOS,
               "[`CONTRATO-ADAPTADOR.md`](../../kernel/operativo/runtime/"
               "CONTRATO-ADAPTADOR.md).",
               "[`CONTRATO-ADAPTADOR.md`](../../kernel/operativo/runtime/"
               "CONTRATO-ADAPTADOR.md). **Ninguno existe y ninguno está certificado.**")


def m_g3_lo_que_no_hay(raiz):
    """`ADJ-G3` · vuelve a declarar inexistentes el verificador y la raíz externa en §5.4."""
    _sustituir(raiz, SEDE_CONTRATOS,
               "LA BATERÍA INTERNA  comprueba",
               "LO QUE NO HAY       el VERIFICADOR DE ADMISIÓN y la RAÍZ EXTERNA DE "
               "CONFIANZA\n\nLA BATERÍA INTERNA  comprueba")


def m_g3_negacion_en_bloque(raiz):
    """`ADJ-G3` · vuelve a negar EN BLOQUE el estado de construcción, en `05-PLAN`."""
    _sustituir(raiz, SEDE_PLAN,
               "> **ESTE DOCUMENTO ES UN PLAN, y por tanto NO ES SEDE DE ESTADO.**",
               "> **ESTE DOCUMENTO ES UN PLAN.** Nada de lo que describe está implementado.")


def m_g3_negacion_en_bloque_de_texto(raiz):
    """La exención de `console` NO puede convertirse en una exención de toda cerca.

    `T360` dejó de juzgar lo que se dice dentro de un bloque ```console, porque ahí el
    texto lo escribió una EJECUCIÓN y no la sede —el registro del gate transcribe
    literalmente el `printf` con el que un revisor comprobó que `T360` funciona—. La
    tentación era eximir TODAS las cercas, y eso sí sería un agujero: el corpus escribe
    afirmaciones normativas dentro de bloques ```text. Este sabotaje pone la frase en un
    bloque ```text de una sede nueva y exige que `T360` la siga cazando.
    """
    _escribir(raiz, "docs/canonico/ZZ-NEGACION-EN-BLOQUE-DE-TEXTO.md",
              "# sede nueva con la negacion dentro de una cerca\n\n"
              "```text\n"
              "Del verificador de admision no existe ninguno, y la raiz externa tampoco.\n"
              "```\n")


def m_g3_negacion_en_cerca_de_consola_vacia(raiz):
    """El sabotaje del AUDITOR INDEPENDIENTE, mecanizado. `T360`, hallazgo 2.

    La exención de las transcripciones de consola la concedía el RÓTULO: tres tildes
    invertidas y la palabra `console`, escritas por el mismo autor cuya afirmación se está
    juzgando. El auditor puso la misma frase dos veces en la misma sede —suelta salía
    `T360 FALLIDA`; envuelta en una cerca `console` VACÍA de toda orden y de toda salida,
    `T360 SUPERADA`— y con eso cualquier documento podía desactivar el guardián sobre sí
    mismo. Aquí se reproduce ese gesto exacto: una cerca `console` sin una sola línea que
    parezca transcripción de nada.
    """
    _escribir(raiz, "docs/canonico/ZZ-CERCA-DE-CONSOLA-VACIA.md",
              "# sede nueva con la negacion dentro de una cerca console SIN transcripcion\n\n"
              "```console\n"
              "Del verificador de admision no existe ninguno, y la raiz externa tampoco.\n"
              "```\n")


def m_g3_sonda_desaparecida(raiz):
    """`ADJ-G3` · la sonda de una pieza construida desaparece: la tabla ha envejecido."""
    os.remove(os.path.join(raiz, "kernel/operativo/runtime/adaptadores/proceso.py"))


def m_g3_sede_nueva_que_niega(raiz):
    """`ADJ-G3` · una sede que NINGUNA lista podría contener niega una pieza construida."""
    _escribir(raiz, "docs/canonico/ZZ-SEDE-QUE-NADIE-ENUMERO.md",
              "# sede nueva\n\nDel verificador de admisión no existe ninguno, y la raíz "
              "externa tampoco: ninguno implementado.\n")


def m_m5_inclusion_sin_motivo(raiz):
    """`ADJ-M5` · un prefijo de INCLUSIÓN se queda otra vez sin motivo escrito."""
    _sustituir(raiz, VALIDADOR_RECUENTOS,
               '"el corpus canónico vigente: es la sede que el resto del árbol cita"',
               '""')


def m_m5_zona_en_silencio(raiz):
    """`ADJ-M5` · una zona nueva de documentos cae fuera de las dos mitades, sin decirlo."""
    _escribir(raiz, "docs/f7/00-ZONA-QUE-NADIE-CLASIFICO.md",
              "# zona nueva\n\nDocumentos de una fase que todavía no existe.\n")


CATALOGO = [
    Mutacion("NG3a", "ADJ-G3", "T360", "comprobar_recuentos",
             "§5.3 vuelve a declarar que no existe ningún adaptador, con el ejecutor "
             "local real en el árbol",
             m_g3_ninguno_existe,
             espera="Ninguno existe"),
    Mutacion("NG3b", "ADJ-G3", "T360", "comprobar_recuentos",
             "§5.4 vuelve a declarar inexistentes el verificador de admisión y la raíz "
             "externa, con los dos construidos y con evidencia publicada",
             m_g3_lo_que_no_hay,
             espera="LO QUE NO HAY"),
    Mutacion("NG3c", "ADJ-G3", "T360", "comprobar_recuentos",
             "`05-PLAN` vuelve a negar EN BLOQUE que nada de lo que describe esté "
             "implementado",
             m_g3_negacion_en_bloque,
             espera="niega EN BLOQUE"),
    Mutacion("NG3d", "ADJ-G3", "T360", "comprobar_recuentos",
             "la sonda de una pieza construida desaparece del árbol y la tabla de piezas "
             "se queda describiendo un árbol que ya no existe",
             m_g3_sonda_desaparecida,
             espera="ha envejecido"),
    Mutacion("NG3e", "ADJ-G3", "T360", "comprobar_recuentos",
             "una sede NUEVA, que ninguna lista podría contener, niega dos piezas "
             "construidas: la cobertura se descubre, no se enumera",
             m_g3_sede_nueva_que_niega,
             espera="ZZ-SEDE-QUE-NADIE-ENUMERO"),
    Mutacion("NG3f", "ADJ-G3", "T360", "comprobar_recuentos",
             "la negación se esconde dentro de un bloque ```text: la exención de las "
             "transcripciones de consola no puede extenderse a toda cerca",
             m_g3_negacion_en_bloque_de_texto,
             espera="ZZ-NEGACION-EN-BLOQUE-DE-TEXTO"),
    Mutacion("NG3g", "ADJ-G3", "T360", "comprobar_recuentos",
             "la negación se esconde en una cerca ```console VACÍA de toda transcripción: "
             "la exención se gana con la forma del bloque, no con su rótulo",
             m_g3_negacion_en_cerca_de_consola_vacia,
             espera="ZZ-CERCA-DE-CONSOLA-VACIA"),
    Mutacion("NM5a", "ADJ-M5", "T361", "comprobar_recuentos",
             "un prefijo de INCLUSIÓN del ámbito vivo se queda sin motivo escrito, que es "
             "la exclusión por omisión volviendo",
             m_m5_inclusion_sin_motivo,
             espera="no dice por qué barre"),
    Mutacion("NM5b", "ADJ-M5", "T361", "comprobar_recuentos",
             "una zona nueva de documentos cae fuera de las dos mitades de la frontera, "
             "que es exactamente como `docs/f5/` quedó fuera del barrido",
             m_m5_zona_en_silencio,
             espera="EN SILENCIO"),
    Mutacion("NE14a", "E-14", "T158", "comprobar_evidencia",
             "la evidencia dice `OK (skipped=3)` y la firma `OK` la casaba igual",
             m_e14_ok_con_saltos,
             espera="SALTÓ"),
    Mutacion("NE14b", "E-14", "T158", "comprobar_evidencia",
             "el contador de casos se infla y nadie lo contrasta con la salida",
             m_e14_contador_inflado,
             espera="desenlaces de caso"),
    Mutacion("NE14c", "E-14", "T158", "comprobar_evidencia",
             "se recorta un caso de la salida y el contador sigue diciendo lo que decía",
             m_e14_salida_recortada,
             espera="desenlaces de caso"),
    Mutacion("NE14d", "E-14", "T158", "comprobar_evidencia",
             "un `OK` que declara `failures` dentro del paréntesis",
             m_e14_exito_con_fallos,
             espera="no es un éxito"),
    Mutacion("NE14e", "E-14", "T158", "comprobar_evidencia",
             "dos corridas pegadas en el mismo fichero de evidencia",
             m_e14_dos_corridas_pegadas,
             espera="EXACTAMENTE"),
]



# ===========================================================================
#  `#21` Y `#23` DEL DELTA (`H2` y `H4` de `REV-3`) · EL SELLO DEL PRODUCTO
# ===========================================================================
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-05, sobre una COPIA del árbol:
#
#      $ python3.12 kernel/operativo/validadores/huella.py --raiz <copia>
#        2696627742081a01
#      $ printf '\nENTRADA FALSA\n' >> <copia>/docs/owner/ADS-OWNER-RESOLUCIONES.md
#      $ printf '\nLINEA FALSA\n'   >> <copia>/docs/f6/05-MATRIZ-CIERRE-G01-G08.md
#      $ python3.12 kernel/operativo/validadores/huella.py --raiz <copia>
#        2696627742081a01
#
#  La sede del Owner y el documento que reclama el cierre de `F6`, movidas las dos, y el
#  número quieto. `AMBITOS = ("kernel", "packs", "tooling")`.
#
#  DECISIÓN · cada mutación ANOTA los dos sellos en la copia ANTES de infringir
#      Alternativas: (a) sabotear la copia tal cual llega; (b) anotar primero la huella del
#      kernel y el sello del producto de la copia, y sabotear después.
#      Se elige (b), y no es comodidad: es lo que hace que el rojo signifique algo. La copia
#      sale del ÁRBOL DE TRABAJO, y un árbol de trabajo en el que se está trabajando nunca
#      coincide con sus referencias anotadas —basta con que otro fichero esté a medio
#      escribir—. Con (a) `T150` llegaría ROJA a la mutación y el catálogo daría por
#      «detectada» una infracción que no ha detectado nadie: exactamente el falso verde al
#      revés. Anotar primero fija el VERDE de partida dentro de la propia copia, de modo que
#      el único cambio entre el verde y el rojo es la infracción. La `espera` de cada
#      entrada remata el control: no basta con que caiga, tiene que caer por SU motivo.
SEDE_DEL_OWNER = "docs/owner/ADS-OWNER-RESOLUCIONES.md"
NORMA_CANONICA = "docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md"
SEDE_DE_LA_DEUDA = "docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md"
PROYECCION = "docs/f6/05-MATRIZ-CIERRE-G01-G08.md"
GATE_HISTORICO = "docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md"
MATERIAL_HISTORICO = "docs/rediseno/00-MAPA.md"
HUELLA = "kernel/operativo/validadores/huella.py"


def _anotar_los_dos_sellos(raiz):
    """Fija en la COPIA el verde de partida: huella del kernel y sello del producto."""
    guion = os.path.join(raiz, HUELLA)
    subprocess.run([sys.executable, guion, "--raiz", raiz, "--anotar-sello"],
                   capture_output=True, check=True)
    calculada = subprocess.run([sys.executable, guion, "--raiz", raiz],
                               capture_output=True, text=True, check=True)
    with open(os.path.join(raiz, "kernel/.upstream-hash"), "w", encoding="utf-8") as fh:
        fh.write(calculada.stdout.strip() + "\n")


def _tras_anotar(accion):
    """Envuelve una infracción para que se aplique DESPUÉS de fijar el verde de partida."""
    def aplicar(raiz):
        _anotar_los_dos_sellos(raiz)
        accion(raiz)
    return aplicar


def _anexar(rel):
    def accion(raiz):
        with open(os.path.join(raiz, rel), "a", encoding="utf-8") as fh:
            fh.write("\nLINEA FALSA DEL SABOTAJE\n")
    return accion


def m_21_borrar_sede_normativa(raiz):
    """`#21` · desaparece la sede de una materia vigente, y con ella la materia."""
    os.remove(os.path.join(raiz, SEDE_DE_LA_DEUDA))


def m_21_anadir_borrador(raiz):
    """`#21` · un borrador NO APROBADO aparece junto a la norma sin mover el sello."""
    _escribir(raiz, "docs/f5/borradores/ZZ-BORRADOR-QUE-NADIE-APROBO.md",
              "# borrador que nadie aprobo\n\nTexto que se leeria como norma.\n")


def m_21_cambiar_una_exclusion(raiz):
    """`#21` · la sede del Owner se cuela en la lista de EXCLUSIONES del sello.

    Es la forma barata de «arreglar» un rojo de integridad: no se toca la norma, se retira
    del alcance. El ÁMBITO del sello existe para que retirar algo del alcance sea un acto
    visible y no una línea que nadie relee.
    """
    _sustituir(raiz, HUELLA,
               '("kernel/.upstream-hash", ".sello-producto")',
               '("kernel/.upstream-hash", ".sello-producto",\n'
               '      "docs/owner/ADS-OWNER-RESOLUCIONES.md")')


def m_21_omitir_docs_entero(raiz):
    """`#21` · el estrechamiento ORIGINAL, escrito hoy: `docs/` entero fuera del sello."""
    _sustituir(raiz, HUELLA,
               '            rel = os.path.relpath(ruta, base).replace(os.sep, "/")\n'
               '            if _excluida_del_sello(rel):',
               '            rel = os.path.relpath(ruta, base).replace(os.sep, "/")\n'
               '            if rel.startswith("docs/"):\n'
               '                continue\n'
               '            if _excluida_del_sello(rel):')


def m_23_huella_ciega_a_la_ruta(raiz):
    """`#23` · la huella deja de mirar la RUTA: el mismo contenido en otro sitio pasa."""
    _sustituir(raiz, HUELLA,
               "        acumulado.update(rel.encode(\"utf-8\"))\n"
               "        acumulado.update(b\"\\0\")\n"
               "        with open(ruta, \"rb\") as fh:",
               "        with open(ruta, \"rb\") as fh:")


def m_23_sello_ciego_al_contenido(raiz):
    """`#23` · el sello deja de mirar el CONTENIDO: reescribir una norma no lo mueve."""
    _sustituir(raiz, HUELLA,
               "        acumulado.update(hashlib.sha256(contenido).digest())",
               "        acumulado.update(b\"\")")


def m_23_estrechar_las_extensiones(raiz):
    """`#23` · se estrecha la huella hasta que los validadores dejan de entrar.

    Es el estrechamiento que la lista escrita a mano de nueve rutas SÍ veía. Se conserva
    porque lo que sustituye a esa lista tiene que ver por lo menos lo mismo, y ahora lo ve
    DERIVADO de `validadores.yaml`: un validador nuevo entra el día que se registra.
    """
    _sustituir(raiz, HUELLA,
               'EXTENSIONES = (".md", ".yaml", ".yml", ".py", ".sh", ".toml")',
               'EXTENSIONES = (".md", ".yaml", ".yml", ".sh", ".toml")')


def m_23_clase_sin_politica(raiz):
    """`#23` · una clase canónica se queda sin política de sello, y caería POR OMISIÓN."""
    _sustituir(raiz, HUELLA, '    "HISTORICA": (\n        SELLADA,',
               '    "HISTORICA_RETIRADA": (\n        SELLADA,')


CATALOGO_DEL_SELLO = [
    Mutacion("NS21a", "#21", "T150", "comprobar_integridad",
             "se altera una NORMA VIGENTE dentro de `docs/`, que es donde la prosa ES la "
             "norma, y el sello del producto tiene que moverse",
             _tras_anotar(_anexar(NORMA_CANONICA)),
             espera="la clase `CANONICA_OPERATIVA` DIVERGE"),
    Mutacion("NS21b", "#21", "T150", "comprobar_integridad",
             "se altera la SEDE DEL OWNER: es el gesto exacto que `REV-3` reprodujo y que "
             "no movía la huella",
             _tras_anotar(_anexar(SEDE_DEL_OWNER)),
             espera="la clase `AUTORIDAD_SUPERIOR` DIVERGE"),
    Mutacion("NS21c", "#21", "T150", "comprobar_integridad",
             "se altera una PROYECCIÓN DERIVADA —la matriz donde la candidata reclama el "
             "cierre de `G-01`…`G-08`—, el segundo fichero del hecho reproducido",
             _tras_anotar(_anexar(PROYECCION)),
             espera="la clase `DERIVADA` DIVERGE"),
    Mutacion("NS21d", "#21", "T150", "comprobar_integridad",
             "se altera SÓLO un GATE HISTÓRICO: una trazabilidad reescribible no traza, "
             "porque los actos siguientes se apoyan en el acto pasado",
             _tras_anotar(_anexar(GATE_HISTORICO)),
             espera="la clase `EVIDENCIA` DIVERGE"),
    Mutacion("NS21e", "#21", "T150", "comprobar_integridad",
             "se altera material HISTÓRICO conservado por trazabilidad, que es la otra "
             "clase que sólo existe para poder mirar atrás",
             _tras_anotar(_anexar(MATERIAL_HISTORICO)),
             espera="la clase `HISTORICA` DIVERGE"),
    Mutacion("NS21f", "#21", "T150", "comprobar_integridad",
             "se AÑADE un borrador no aprobado junto a la norma: si añadirlo no moviera el "
             "sello, se leería como norma sin que nada lo hubiera aprobado",
             _tras_anotar(m_21_anadir_borrador),
             espera="la clase `NO_APLICABLE_A_IMPLEMENTACION` DIVERGE"),
    Mutacion("NS21g", "#21", "T150", "comprobar_integridad",
             "se BORRA una sede normativa vigente: retirar la sede retira la materia que "
             "gobernaba, y un sello que sólo suma contenidos no lo dice",
             _tras_anotar(m_21_borrar_sede_normativa),
             espera="es la SEDE de `MAT-008` y NO EXISTE en el árbol"),
    Mutacion("NS21h", "#21", "T150", "comprobar_integridad",
             "se CAMBIA una exclusión del sello para sacar del alcance la sede del Owner: "
             "el alcance viaja pegado al número, y moverlo es un acto visible",
             _tras_anotar(m_21_cambiar_una_exclusion),
             espera="el ÁMBITO del sello CAMBIÓ"),
    Mutacion("NS21i", "#21", "T150", "comprobar_integridad",
             "se OMITE `docs/` ENTERO del sello, que es el defecto original escrito hoy: "
             "las clases normativas se quedan sin un solo fichero sellado",
             _tras_anotar(m_21_omitir_docs_entero),
             espera="y el sello no cubre NI UN fichero suyo"),
    Mutacion("NS23a", "#23", "T150", "comprobar_integridad",
             "la huella deja de mirar la RUTA: el mismo contenido en otro sitio produce el "
             "mismo número, que es la mitad de lo que la comprobación 3 declaraba y no "
             "escribía",
             _tras_anotar(m_23_huella_ciega_a_la_ruta),
             espera="No es sensible a la RUTA"),
    Mutacion("NS23b", "#23", "T150", "comprobar_integridad",
             "el sello deja de mirar el CONTENIDO: reescribir una norma entera no lo mueve, "
             "y la comprobación 3 tiene que EJERCERLO, no declararlo",
             _tras_anotar(m_23_sello_ciego_al_contenido),
             espera="No es sensible al CONTENIDO"),
    Mutacion("NS23c", "#23", "T150", "comprobar_integridad",
             "se estrecha `EXTENSIONES` hasta que los validadores en Python salen de la "
             "huella: el estrechamiento que la lista de nueve rutas veía, ahora derivado "
             "de `validadores.yaml`",
             _tras_anotar(m_23_estrechar_las_extensiones),
             espera="NO entra en la huella del kernel"),
    Mutacion("NS23d", "#23", "T150", "comprobar_integridad",
             "una clase canónica se queda SIN POLÍTICA de sello escrita, y con ella caería "
             "fuera POR OMISIÓN, que es la exclusión que nadie escribe",
             _tras_anotar(m_23_clase_sin_politica),
             espera="no tiene política de sello escrita"),
]

# LA INCORPORACIÓN ES UNA ASIGNACIÓN, Y NO UN `CATALOGO.extend(...)`. MEDIDO: con la
# llamada, `T330` y `T380` pusieron este módulo en el inventario de PUNTOS EJECUTABLES
# —`_trabaja_al_importarse` cuenta toda llamada del nivel superior como trabajo— y exigieron
# a un módulo que sólo se IMPORTA la línea de intérprete que la advertencia de forma de
# arriba retira a propósito. Una asignación declara sin ejecutar, que es lo que este fichero
# hace: construir un catálogo que `comprobar_negativos` recorre.
CATALOGO = CATALOGO + CATALOGO_DEL_SELLO
