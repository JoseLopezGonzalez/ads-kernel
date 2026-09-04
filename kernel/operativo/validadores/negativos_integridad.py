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

from comprobar_negativos import Mutacion, _sustituir

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


CATALOGO = [
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
