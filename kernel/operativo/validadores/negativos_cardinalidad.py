#!/usr/bin/env python3
"""negativos_cardinalidad — infracciones deliberadas de la corrección del 2026-09-04.

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

DECISIÓN · este módulo es ADEMÁS el VALIDADOR que ejecuta la propiedad de `E-01`
    `comprobar_negativos` aplica la infracción sobre una copia del repositorio y ejecuta
    `kernel/operativo/validadores/<validador>.py --json --raiz <copia>`, esperando la forma
    `[{"id": "Tnnn", "estado": …, "fallos": […]}]`. La propiedad que tiene que detectar el
    sabotaje de `E-01` —«varios agentes sin integrador declarado está prohibido»— es
    SEMÁNTICA: hay que LEER el campo `agentes` de cada rol con el lector de vocabulario
    cerrado y CONTRASTAR el integrador contra la `ampliacion` de su composición. Eso no lo
    puede hacer un validador estructural, y ejecutarlo desde la batería del runtime no vale
    aquí, porque la sede de ejecución de los negativos es ésta.
    Alternativas: (a) un validador nuevo, `comprobar_cardinalidad.py`; (b) que este módulo
    tenga también un `main()`.
    Se elige (b) mientras el reparto de ficheros de esta corrección esté vigente: (a) toca
    una sede que en esta pasada pertenece a otro eje, y una sede compartida editada por dos
    manos a la vez es exactamente lo que este fichero existe para evitar. La propiedad se
    ejecuta contra el CORPUS de la raíz que se le pase, de modo que sirve igual para el
    corpus real y para la copia mutada. Si el coordinador prefiere (a), el cuerpo de
    `comprobar()` se mueve entero y aquí queda sólo el `CATALOGO`.

DECISIÓN · el sabotaje tiene que caer POR SEMÁNTICA, y por eso el lector lo ENTIENDE
    `agentes: "7 repartidos por artefacto, sin integrador"` es, palabra por palabra, lo que
    `C4` llama prohibido. Si el lector no supiera leer esa forma, la materialización caería
    por «cardinal ilegible», que es un diagnóstico distinto y mucho peor: diría que no se
    entiende el corpus cuando lo que pasa es que el corpus declara una infracción. Por eso
    la cláusula `sin integrador` está ENUMERADA en el vocabulario cerrado del lector: para
    que el caso caiga por la prohibición que viola. Antes de esta corrección el mismo valor
    dejaba la batería `agentes` en VERDE y el único rojo era la huella del kernel, que
    saltaría igual con cualquier edición legítima: un centinela que no distingue.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

RAIZ_POR_DEFECTO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Las TRES formas plurales que el corpus declara, medidas sobre los noventa y nueve valores
# del campo `agentes`. Se transcriben para CONFRONTAR el censo derivado, no para
# sustituirlo: una cuarta forma plural que aparezca sin declararse pone `T250` en rojo.
PLURALES_MEDIDAS = {
    "1 o 2 repartidos por territorio",
    "2 o 3, uno por dirección explorada",
    "1 o 2 en competencia declarada",
}


# ===========================================================================
#  el VALIDADOR · la propiedad de `E-01`, ejecutada sobre el corpus de `--raiz`
# ===========================================================================
def _cargar(raiz):
    """Importa el paquete `ciclo` DE LA RAÍZ QUE SE PASA, no el del árbol de trabajo.

    Es lo que hace que la comprobación mida la copia mutada y no el original: si importara
    el del repositorio, el sabotaje sobre la copia no se vería y el caso saldría «no
    detectado» por una razón que no tiene nada que ver con la propiedad.
    """
    runtime = os.path.join(raiz, "kernel", "operativo", "runtime")
    if runtime not in sys.path:
        sys.path.insert(0, runtime)
    for modulo in [n for n in list(sys.modules) if n == "ciclo" or n.startswith("ciclo.")]:
        del sys.modules[modulo]
    import ciclo                                                       # noqa: PLC0415
    from ciclo import equipos                                          # noqa: PLC0415
    return ciclo, equipos, ciclo.Corpus(os.path.join(raiz, "kernel", "operativo"))


def comprobar(raiz):
    """Las TRES pruebas de `E-01` que se pueden ejercitar sobre el corpus solo."""
    filas = [
        {"id": "T250", "nombre": "Las composiciones plurales del corpus son las medidas",
         "estado": "prueba-superada", "fallos": []},
        {"id": "T254", "nombre": "Ningún rol plural se queda sin integrador declarado",
         "estado": "prueba-superada", "fallos": []},
        {"id": "T259", "nombre": "Toda forma del campo agentes se lee con el lector cerrado",
         "estado": "prueba-superada", "fallos": []},
    ]
    por_id = {fila["id"]: fila for fila in filas}

    def fallo(identificador, texto):
        por_id[identificador]["fallos"].append(texto)
        por_id[identificador]["estado"] = "prueba-fallida"

    try:
        ciclo, equipos, corpus = _cargar(raiz)
    except Exception as error:                                          # noqa: BLE001
        for fila in filas:
            fila["estado"] = "prueba-fallida"
            fila["fallos"].append("no se puede leer el corpus de `" + raiz + "`: "
                                  + type(error).__name__ + ": " + str(error))
        return filas

    plurales = set()
    for capacidad in ciclo.CAPACIDADES:
        for composicion in corpus.composiciones(capacidad):
            roles = [str(entrada.get("rol")) for entrada in (composicion.get("roles") or [])]
            try:
                integrador = equipos.integrador_de(composicion)
            except Exception as error:                                  # noqa: BLE001
                integrador = None
                fallo("T254", composicion["id"] + ": la `ampliacion` declara un integrador "
                      "que no es rol de la composición — " + str(error))
            for entrada in composicion.get("roles") or []:
                donde = composicion["id"] + " · " + str(entrada.get("rol"))
                try:
                    lectura = equipos.leer_cardinal(entrada.get("agentes"), roles=roles)
                except Exception as error:                              # noqa: BLE001
                    fallo("T259", donde + ": el campo `agentes` no encaja en ninguna forma "
                          "declarada del vocabulario cerrado — " + str(error))
                    continue
                if lectura["maximo"] <= 1:
                    continue
                plurales.add(lectura["literal"])
                if lectura["integrador_negado"]:
                    fallo("T254", donde + ": declara " + str(lectura["maximo"]) + " agentes "
                          "y, en el mismo campo, que NO hay integrador. `C4`: «Varios "
                          "agentes sin integrador declarado está prohibido»")
                    continue
                if integrador is None:
                    fallo("T254", donde + ": materializa hasta " + str(lectura["maximo"])
                          + " agentes y su composición no declara QUIÉN INTEGRA en el campo "
                          "`ampliacion`. `C4`: «Varios agentes sin integrador declarado está "
                          "prohibido»")

    nuevas = sorted(plurales - PLURALES_MEDIDAS)
    perdidas = sorted(PLURALES_MEDIDAS - plurales)
    if nuevas:
        fallo("T250", "el corpus declara formas plurales del campo `agentes` que el censo "
              "medido no contempla: " + ", ".join("`" + f + "`" for f in nuevas))
    if perdidas:
        fallo("T250", "el censo medido declara formas plurales que ya no están en el "
              "corpus: " + ", ".join("`" + f + "`" for f in perdidas))
    return filas


def main(argv=None):
    analizador = argparse.ArgumentParser(
        prog="negativos_cardinalidad",
        description="la propiedad de `E-01`: cardinal derivado e integrador declarado")
    analizador.add_argument("--raiz", default=RAIZ_POR_DEFECTO)
    analizador.add_argument("--json", action="store_true")
    argumentos = analizador.parse_args(argv)
    filas = comprobar(os.path.abspath(argumentos.raiz))
    if argumentos.json:
        print(json.dumps(filas, ensure_ascii=False, indent=2))
    else:
        for fila in filas:
            marca = "OK  " if fila["estado"] == "prueba-superada" else "FALLO"
            print(marca + " " + fila["id"] + "  " + fila["nombre"])
            for texto in fila["fallos"]:
                print("      → " + texto)
    return 1 if any(f["estado"] != "prueba-superada" for f in filas) else 0


# ===========================================================================
#  el CATÁLOGO de infracciones deliberadas
# ===========================================================================
COMPOSICION_DE_DIS = "kernel/operativo/capacidades/DIS/composicion.md"

_ROL_PLURAL = ('  - rol: DIS/diseno-visual\n    obligatorio: true\n'
               '    agentes: "2 o 3, uno por dirección explorada"')


def _sustituir(raiz, rel, viejo, nuevo):
    ruta = os.path.join(raiz, rel)
    with open(ruta, encoding="utf-8") as manejador:
        texto = manejador.read()
    if viejo not in texto:
        raise RuntimeError("la mutación no encaja: no encuentro el texto en " + rel)
    with open(ruta, "w", encoding="utf-8") as manejador:
        manejador.write(texto.replace(viejo, nuevo, 1))


def m_siete_agentes_sin_integrador(raiz):
    """`E-01` · EL SABOTAJE QUE CIERRA EL HALLAZGO.

    Literalmente lo que `C4` llama prohibido, escrito en el corpus. Antes de la corrección
    dejaba la batería `agentes` en VERDE y el único rojo era la huella del kernel, que
    salta igual con cualquier edición legítima: no distinguía una infracción de un cambio.
    """
    _sustituir(raiz, COMPOSICION_DE_DIS, _ROL_PLURAL,
               '  - rol: DIS/diseno-visual\n    obligatorio: true\n'
               '    agentes: "7 repartidos por artefacto, sin integrador"')


def m_integrador_borrado_de_la_ampliacion(raiz):
    """`E-01` · el reparto plural sigue declarado y desaparece QUIÉN INTEGRA."""
    _sustituir(raiz, COMPOSICION_DE_DIS,
               "Un agente de DIS/diseno-visual por cada dirección explorada, con "
               "DIS/direccion-artistica\n  como integrador declarado.",
               "Un agente de DIS/diseno-visual por cada dirección explorada.")


def m_cardinal_inventado(raiz):
    """`E-01` · una forma del campo `agentes` que el vocabulario cerrado no declara."""
    _sustituir(raiz, COMPOSICION_DE_DIS, _ROL_PLURAL,
               '  - rol: DIS/diseno-visual\n    obligatorio: true\n'
               '    agentes: "unos cuantos, los que hagan falta"')


def m_cuarta_composicion_plural(raiz):
    """`E-01` · una composición pasa a declarar varios agentes y nadie se entera.

    Es el caso que impide que el censo se quede corto: si mañana una composición nueva
    declara pluralidad, tiene que verse. `DIS/critica-visual` es además el peor sitio
    posible —es el rol independiente de todos los productores—, así que un reparto ahí sin
    integrador declarado es exactamente el defecto de `C4`.
    """
    _sustituir(raiz, COMPOSICION_DE_DIS,
               '  - rol: DIS/critica-visual\n    obligatorio: true\n'
               '    agentes: "1, distinto de todos los productores"',
               '  - rol: DIS/critica-visual\n    obligatorio: true\n'
               '    agentes: "1 o 2 repartidos por superficie"')


def _mutacion():
    """La clase `Mutacion` de la sede de ejecución, sin importar en círculo.

    `comprobar_negativos` importa este módulo desde su propio cuerpo, así que un `import
    comprobar_negativos` aquí lo pillaría a medias y reventaría. La clase, en cambio, está
    definida mucho antes de esa línea, de modo que se toma del módulo YA cargado. Se busca
    por sus DOS nombres posibles —`comprobar_negativos` cuando alguien lo importa, y
    `__main__` cuando se ejecuta como guión, que es lo normal— y sólo si no aparece se
    importa de la forma corriente, que es el caso de ejecutar este fichero solo. La clase NO
    se copia: la sede sigue siendo una.
    """
    for nombre in ("comprobar_negativos", "__main__"):
        cargado = sys.modules.get(nombre)
        if cargado is not None and hasattr(cargado, "Mutacion"):
            return cargado.Mutacion
    from comprobar_negativos import Mutacion                            # noqa: PLC0415
    return Mutacion


def _catalogo():
    Mutacion = _mutacion()
    return [
        Mutacion("N250", "E-01", "T254", "negativos_cardinalidad",
                 "una composición declara SIETE agentes por artefacto y, en el mismo campo, "
                 "que no hay integrador — lo que `C4` llama prohibido",
                 m_siete_agentes_sin_integrador,
                 espera="Varios agentes sin integrador declarado está prohibido"),
        Mutacion("N250b", "E-01", "T254", "negativos_cardinalidad",
                 "el reparto plural sigue declarado y desaparece quién integra el resultado",
                 m_integrador_borrado_de_la_ampliacion,
                 espera="no declara QUIÉN INTEGRA"),
        Mutacion("N250c", "E-01", "T259", "negativos_cardinalidad",
                 "el campo `agentes` estrena una forma que el vocabulario cerrado no declara",
                 m_cardinal_inventado,
                 espera="no encaja en ninguna forma declarada"),
        Mutacion("N250d", "E-01", "T250", "negativos_cardinalidad",
                 "una composición pasa a declarar varios agentes y el censo no lo ve",
                 m_cuarta_composicion_plural,
                 espera="formas plurales del campo `agentes` que el censo medido no contempla"),
    ]


CATALOGO = _catalogo()


if __name__ == "__main__":
    sys.exit(main())
