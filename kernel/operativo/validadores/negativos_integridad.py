#!/usr/bin/env python3
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
from __future__ import annotations

import os

from comprobar_negativos import Mutacion, _escribir, _sustituir

EVIDENCIA = "kernel/operativo/pruebas/evidencia/contencion-salida.txt"


def m_e14_ok_con_saltos(raiz):
    """`E-14` · `OK` se convierte en `OK (skipped=3)`, que la firma vieja casaba igual."""
    _sustituir(raiz, EVIDENCIA, "\nOK\n", "\nOK (skipped=3)\n")


def m_e14_contador_inflado(raiz):
    """`E-14` · el contador publicado deja de describir la corrida que lo acompaña."""
    _sustituir(raiz, EVIDENCIA, "Ran 20 tests", "Ran 99 tests")


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
