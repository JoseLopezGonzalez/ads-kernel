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
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
VALIDADORES = "kernel/operativo/validadores"


class Mutacion:
    """Una infracción deliberada, y la prueba que TIENE que detectarla."""

    def __init__(self, mid, hallazgo, prueba, validador, descripcion, aplicar, espera=None):
        self.id = mid
        self.hallazgo = hallazgo
        self.prueba = prueba
        self.validador = validador
        self.descripcion = descripcion
        self.aplicar = aplicar          # f(raiz_copia) -> None
        # `espera` es el trozo de DIAGNÓSTICO que el validador debe producir. Sin él, una
        # mutación se da por detectada porque la prueba falló, sin comprobar que falló POR
        # ESO. Con manifiestos inválidos importa el doble: un traceback también «falla».
        self.espera = espera
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
    """A-18 · un rol se concede lo que su capacidad ESCALA."""
    _sustituir(raiz, "kernel/operativo/capacidades/CON/roles/implementacion.md",
               "  decide:",
               '  decide:\n    - "la implementación exige una decisión de forma, alcance o dominio"')


def m_rol_decide_materia_ajena(raiz):
    """A-18 · un rol se concede la materia declarada por otra capacidad."""
    _sustituir(raiz, "kernel/operativo/capacidades/CON/roles/implementacion.md",
               "  decide:",
               '  decide:\n    - "los valores del sistema de diseño: escala, ritmo, roles de color, elevación"')


def m_metodo_huerfano(raiz):
    """A-15 · un método deja de estar declarado por su capacidad, como ENC/Critica."""
    _sustituir(raiz, "kernel/operativo/capacidades/ENC/CAPACIDAD.md",
               "metodos: [ENC/Escucha, ENC/Anclaje, ENC/Maduracion, ENC/Critica, ENC/Orden, ENC/Formulacion]",
               "metodos: [ENC/Escucha, ENC/Anclaje, ENC/Maduracion, ENC/Orden, ENC/Formulacion]")


def m_marca_en_esquema(raiz):
    """T92 · una marca comercial entra por un fichero que antes no se miraba."""
    _sustituir(raiz, "kernel/operativo/esquemas/perfil-agente.yaml",
               "  contexto: {tipo: enum,", "  # exige gpt-4 para este perfil\n  contexto: {tipo: enum,")


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


def m_frontera_para_silenciar_un_enlace_roto(raiz):
    """La frontera del proyecto instalado, usada para tapar un enlace roto de AQUÍ.

    `enlaces_no_embarcados` declara qué se queda aguas arriba. Si su ruta pudiera no existir
    en este repositorio, la lista dejaría de declarar una frontera y pasaría a ser un
    silenciador: bastaría añadir el destino roto para que `ads_lint` dejara de verlo. Por eso
    T147 exige que cada entrada EXISTA aquí, y esto lo demuestra.
    """
    _sustituir(raiz, VALIDADORES + "/exclusiones.yaml",
               "  - ruta: docs/evolucion/03-INVARIANTES.md",
               "  - ruta: docs/evolucion/DOCUMENTO-QUE-NO-EXISTE.md\n"
               "    motivo: >\n"
               "      entrada introducida por comprobar_negativos para tapar un enlace roto\n"
               "  - ruta: docs/evolucion/03-INVARIANTES.md")


def m_frontera_sin_motivo(raiz):
    """Una frontera sin motivo escrito no es revisable, y por eso no se admite."""
    _sustituir(raiz, VALIDADORES + "/exclusiones.yaml",
               "  - ruta: docs/rediseno/README.md\n    motivo: >",
               "  - ruta: docs/rediseno/README.md\n    sin_motivo: >")


def m_exclusion_caducada(raiz):
    """A-05 · una exclusión cuyo objetivo ya no existe: restos que nadie revisa."""
    _sustituir(raiz, VALIDADORES + "/exclusiones.yaml",
               "no_analizados:",
               'no_analizados:\n  - ruta: packs/pack-que-ya-no-existe.md\n'
               '    motivo: "resto de una exclusión antigua"')


def m_con_sin_usabilidad(raiz):
    """A-13 · se rompe el vínculo entre CON y gate:usabilidad.

    Era el único hallazgo grave sin infracción deliberada, y por tanto el único cuya
    prueba nunca se había visto fallar.
    """
    _sustituir(raiz, "kernel/operativo/capacidades/CON/CAPACIDAD.md",
               "  - id: superficie-usable", "  - id: superficie-construida")


def m_con_usabilidad_sin_juez(raiz):
    """A-13 · el vínculo existe pero no dice QUIÉN juzga: lo juzgaría quien la produjo."""
    _sustituir(raiz, "kernel/operativo/capacidades/CON/CAPACIDAD.md",
               "el dictamen de los seis ejes lo emite DIS/validacion-de-uso, que no la produjo",
               "el dictamen de los seis ejes se emite al cerrar")


def m_evidencia_sin_py(raiz):
    """El defecto EXACTO de la entrega anterior: se archiva una invocación sin .py."""
    ruta = os.path.join(raiz, "kernel/operativo/pruebas/evidencia/contratos-salida.txt")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("# evidencia de: contratos\n"
                 "# orden:        python3 kernel/operativo/validadores/comprobar_contratos\n"
                 "# codigo:       0\n"
                 "# ---------------------------------------------------------------\n"
                 "python3: can't open file "
                 "'/x/kernel/operativo/validadores/comprobar_contratos': "
                 "[Errno 2] No such file or directory\n")


def m_evidencia_afirma_exito_sin_salida(raiz):
    """Una evidencia que dice código 0 y no contiene el resumen que su validador produce."""
    ruta = os.path.join(raiz, "kernel/operativo/pruebas/evidencia/packs-salida.txt")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("# evidencia de: packs\n"
                 "# orden:        python3 kernel/operativo/validadores/comprobar_packs.py\n"
                 "# codigo:       0\n"
                 "# ---------------------------------------------------------------\n"
                 "todo bien\n")


def m_evidencia_de_otro_validador(raiz):
    """La evidencia de un validador ocupa el fichero de otro."""
    ruta = os.path.join(raiz, "kernel/operativo/pruebas/evidencia/versiones-salida.txt")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("# evidencia de: recuentos\n"
                 "# orden:        python3 kernel/operativo/validadores/comprobar_recuentos.py\n"
                 "# codigo:       0\n"
                 "# ---------------------------------------------------------------\n"
                 "T151  SUPERADA\n\n1 superadas · 0 fallidas\n")


def m_evidencia_con_codigo_no_cero(raiz):
    """Se publica una ejecución que terminó mal."""
    ruta = os.path.join(raiz, "kernel/operativo/pruebas/evidencia/recuentos-salida.txt")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto.replace("# codigo:       0", "# codigo:       1"))


def m_evidencia_falta(raiz):
    """Falta un fichero de evidencia que el manifiesto exige."""
    os.unlink(os.path.join(raiz, "kernel/operativo/pruebas/evidencia/referencias-salida.txt"))


def m_evidencia_caducada(raiz):
    """El caso REAL: evidencia intacta y CADUCADA, y T158 la daba por buena.

    Reproduce lo que ocurrió: bajo un intérprete sin `tomllib` el validador `fuentes` falla,
    el runner —correctamente— NO sobrescribe su evidencia, y la cobertura publicada se queda
    describiendo un corpus anterior. Cabecera de procedencia, código 0, firma de éxito y
    `debe_contener` siguen siendo VÁLIDOS: ninguna de las comprobaciones anteriores de T158
    responde distinto cuando la evidencia envejece.

    La cifra caducada se DERIVA DEL CORPUS VIGENTE, no de la evidencia previa. Es la
    corrección de un defecto real: derivarla de lo publicado hacía que el fixture dependiera
    de lo que la ejecución ANTERIOR hubiera dejado escrito, y con ello del ORDEN DEL
    MANIFIESTO —`negativos` corre antes que `fuentes`—. La primera ejecución leía evidencia
    vieja, `fuentes` la actualizaba después, y la segunda producía otra salida de negativos:
    dos ejecuciones seguidas no coincidían byte a byte.

    Lo que la prueba debe representar es «la evidencia publica DOS FICHEROS MENOS QUE EL
    CORPUS VIGENTE», y no «dos menos que lo que publicaba antes». Por eso el recuento actual
    se obtiene de la definición canónica —`comprobar_fuentes.ficheros_recorridos`— y no se
    reimplementa aquí: dos implementaciones del mismo recuento derivan, y la que miente es
    siempre la que nadie mira.

    El fichero se sigue leyendo, y para dos cosas: comprobar que TODAVÍA publica una cifra
    —si dejara de publicarla no habría vigencia que comprobar, y eso es otro defecto— y
    localizar esa cifra para sustituir exactamente una.

    NINGÚN número del corpus queda escrito a mano, y el fixture es INDEPENDIENTE del orden
    del runner.
    """
    ruta = os.path.join(raiz, "kernel/operativo/pruebas/evidencia/fuentes-salida.txt")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    apariciones = list(re.finditer(r"(\d+) ficheros recorridos", texto))
    if not apariciones:
        raise RuntimeError("la evidencia de `fuentes` ya no publica su cobertura: sin cifra "
                           "publicada no hay vigencia que comprobar, y eso es otro defecto")
    if len(apariciones) != 1:
        raise RuntimeError(
            f"la evidencia de `fuentes` publica {len(apariciones)} cifras de cobertura y se "
            "esperaba exactamente una: el fixture no puede sustituir sin ambigüedad, y "
            "adivinar cuál mutar produciría una prueba que a veces no prueba nada")

    import comprobar_fuentes                                    # noqa: PLC0415
    actual = comprobar_fuentes.ficheros_recorridos(raiz)
    if actual < 3:
        raise RuntimeError(
            f"el corpus vigente recorre {actual} ficheros y no permite construir el fixture: "
            "la mutación exige restar dos y seguir siendo un recuento positivo")

    m = apariciones[0]
    caducada = actual - 2
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto[:m.start(1)] + str(caducada) + texto[m.end(1):])


VIG_PATRON = "        patron: '(\\d+) ficheros recorridos'"
VIG_ID = "      - id: T161-cobertura"
VIG_BLOQUE = """    vigencia:
      - id: T161-cobertura
        patron: '(\\d+) ficheros recorridos'
        recuento: fuentes.ficheros_recorridos
        motivo: >"""


def m_vigencia_sin_patron(raiz):
    """El caso REPRODUCIDO: una entrada sin `patron`, y T158 reventaba con KeyError.

    Un manifiesto inválido es un defecto de conformidad y se dice con un fallo. Una traza
    no dice qué corregir, tumba las comprobaciones que venían detrás, y deja la evidencia
    sin comprobar sin que nadie declare que quedó sin comprobar.
    """
    _sustituir(raiz, "kernel/operativo/validadores/validadores.yaml", VIG_PATRON + "\n", "")


def m_vigencia_no_es_lista(raiz):
    """`vigencia` declarada como mapa suelto en vez de como lista de entradas."""
    _sustituir(raiz, "kernel/operativo/validadores/validadores.yaml",
               "    vigencia:\n      - id: T161-cobertura",
               "    vigencia:\n        id: T161-cobertura")


def m_vigencia_entrada_no_es_mapa(raiz):
    """Una entrada de la lista es una cadena, no un mapa con sus cuatro campos."""
    _sustituir(raiz, "kernel/operativo/validadores/validadores.yaml",
               VIG_ID, "      - T161-cobertura\n      - id: T161-otra")


def m_vigencia_regex_invalida(raiz):
    """El patrón no compila: nunca casaría, y su comprobación pasaría siempre."""
    _sustituir(raiz, "kernel/operativo/validadores/validadores.yaml",
               VIG_PATRON, "        patron: '(\\d+ ficheros recorridos'")


def m_vigencia_sin_grupo_de_captura(raiz):
    """El patrón compila y no captura nada: sin grupo no hay cifra que comparar."""
    _sustituir(raiz, "kernel/operativo/validadores/validadores.yaml",
               VIG_PATRON, "        patron: '\\d+ ficheros recorridos'")


def m_vigencia_captura_no_entera(raiz):
    """El grupo captura texto en vez de la cifra. Una vigencia compara recuentos."""
    _sustituir(raiz, "kernel/operativo/validadores/validadores.yaml",
               VIG_PATRON, "        patron: '\\d+ (ficheros) recorridos'")


def m_vigencia_id_duplicado(raiz):
    """Dos entradas con el mismo id: en el informe una tapa a la otra."""
    _sustituir(raiz, "kernel/operativo/validadores/validadores.yaml",
               VIG_ID, VIG_ID + "\n        patron: '(\\d+) ficheros recorridos'\n"
                       "        recuento: fuentes.ficheros_recorridos\n"
                       "        motivo: duplicada a proposito\n" + VIG_ID)


def m_vigencia_sin_implementacion(raiz):
    """Una `vigencia` declara un recuento que nadie implementa.

    El mecanismo tiene que FALLAR CERRADO: dar por buena una evidencia que no se sabe
    comprobar es exactamente el defecto que la vigencia existe para corregir.
    """
    _sustituir(raiz, "kernel/operativo/validadores/validadores.yaml",
               "        recuento: fuentes.ficheros_recorridos",
               "        recuento: fuentes.recuento_que_nadie_implementa")


def m_validador_fuera_del_manifiesto(raiz):
    """Un validador nuevo que nadie registra queda fuera de la evidencia en silencio."""
    ruta = os.path.join(raiz, VALIDADORES, "comprobar_algo_nuevo.py")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("#!/usr/bin/env python3\nraise SystemExit(0)\n")


def m_prompt_sin_gate(raiz):
    """Revisión de prompts · un prompt deja de nombrar el gate contra el que cierra."""
    _sustituir(raiz, "kernel/operativo/capacidades/ARQ/prompts/encaje.md",
               "Cierras contra **`gate:plan-tecnico`**", "Cierras cuando lo veas terminado")


def m_prompt_habla_con_owner(raiz):
    """Revisión de prompts · un prompt instruye conversar con el Owner sin autoridad."""
    _sustituir(raiz, "kernel/operativo/capacidades/CON/prompts/implementacion.md",
               "## Cómo cierras",
               "Si dudas del alcance, pregunta al Owner qué prefiere.\n\n## Cómo cierras")


def m_prompt_sin_metodo(raiz):
    """Revisión de prompts · un prompt pierde el enlace a su método."""
    _sustituir(raiz, "kernel/operativo/capacidades/ARQ/prompts/encaje.md",
               "> Método: [`ARQ/Encaje`](../metodos/Encaje.md)", "> Método: el que proceda")


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
               'EXTENSIONES = (".md", ".yaml", ".yml", ".py", ".sh", ".toml")',
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
               "./tooling/new-project.sh mi-producto web-app",
               "./tooling/new-project.sh mi-producto pack-web-app")


def m_recuento_a_mano(raiz):
    """A-24 · una cifra de prosa vuelve a divergir del corpus."""
    _sustituir(raiz, "kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md",
               "## Contrato común de rol — veintinueve campos",
               "## Contrato común de rol — veintiocho campos")


def m_version_incoherente(raiz):
    """A-12 · el release cambia y ningún punto de entrada se entera."""
    ruta = os.path.join(raiz, "kernel/VERSION")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("9.9.9\n")


def m_kernel_md_iguala_release(raiz):
    """A-12 · la línea histórica se sube al ritmo del release, que es otro contador.

    Ni la línea histórica ni el release se escriben aquí a mano: se leen del árbol. La
    versión anterior de esta mutación los tenía fijos y dejó de encajar en cuanto uno de
    los dos cambió — una prueba negativa que no se aplica no prueba nada, y su fallo era
    silencioso hasta que alguien miraba el recuento.
    """
    with open(os.path.join(raiz, "kernel/VERSION"), encoding="utf-8") as fh:
        release = fh.read().strip()
    with open(os.path.join(raiz, "kernel/KERNEL.md"), encoding="utf-8") as fh:
        m = re.search(r"> \*\*Versión del kernel:\*\* (\S+)", fh.read())
    historica = m.group(1) if m else "1.4.0"
    _sustituir(raiz, "kernel/KERNEL.md",
               f"> **Versión del kernel:** {historica}",
               f"> **Versión del kernel:** {release}")


def m_encuadre_sin_estado_exigido(raiz):
    """A-11 · el esquema pierde un estado que sus propios documentos exigen."""
    _sustituir(raiz, "kernel/operativo/esquemas/encuadre.yaml",
               "              esperando-owner, esperando-externo, bloqueado, devuelto, cerrado, cancelado]",
               "              esperando-externo, bloqueado, devuelto, cerrado, cancelado]")


def m_encuadre_con_aparcado(raiz):
    """A-11 · vuelve el vocabulario paralelo: aparcado como estado de paquete."""
    _sustituir(raiz, "kernel/operativo/esquemas/encuadre.yaml",
               "  estado: {tipo: enum, valores: [en-conversacion, listo-para-dsp, entregado, descartado]}",
               "  estado: {tipo: enum, valores: [en-conversacion, listo-para-dsp, entregado, descartado, aparcado-por-owner]}")


def m_critica_por_grado_final(raiz):
    """A-14 · la crítica vuelve a activarse por el grado FINAL y puede evaporarse."""
    _sustituir(raiz, "kernel/operativo/capacidades/ENC/CAPACIDAD.md",
               'comprueba: "si incertidumbre.grado_INICIAL fue alta, o nivel_owner es obligatorio, o la composición materializó ENC/critica-de-encuadre, existe su dictamen enlazado"',
               'comprueba: "si incertidumbre.grado es alta o nivel_owner es obligatorio, existe dictamen de ENC/critica-de-encuadre"')


def m_sin_grado_inicial(raiz):
    """A-14 · el encuadre deja de persistir con qué grado entró."""
    _sustituir(raiz, "kernel/operativo/esquemas/encuadre.yaml",
               "obligatorios: [grado, grado_inicial, ejes, motivo]",
               "obligatorios: [grado, ejes, motivo]")


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




def m_t171_bootstrap_sin_la_regla_de_no_copiar(raiz):
    """§100.9 · el prompt de arranque deja de decir que ADS no se copia en una fuente."""
    _sustituir(raiz, "kernel/BOOTSTRAP_PROMPT.md",
               "  · NO copies el PROFILE, el estado, la memoria, los ADR globales, el kernel "
               "ni los packs\n    dentro de una fuente. Una verdad vive en un sitio, y ese "
               "sitio es este repositorio.\n",
               "")


def m_t171_sin_como_materializar(raiz):
    """§100.6 · el criterio desaparece de LOS DOS sitios donde podía leerse.

    Quitarlo de uno solo no es una infracción: el §100 pide que se pueda descubrir, no que
    esté escrito en un fichero concreto. La prueba negativa tiene que borrar la respuesta,
    no moverla — si no, comprobaría una redacción en vez de una propiedad.
    """
    _sustituir(raiz, "kernel/BOOTSTRAP_PROMPT.md",
               "  · para materializar las que falten: python3 tooling/workspace.py init [ids]",
               "  · si falta alguna, apáñate")
    _sustituir(raiz, "START_HERE.md",
               "python3 tooling/workspace.py init      # clona lo que falte; reutiliza lo que ya está",
               "# apáñate")


# --- T161 · las formulaciones semánticas que E2 retiró ----------------------
# No basta con que T161 pase: hay que demostrar que FALLA cuando alguien devuelve al
# corpus el modelo anterior escrito con otras palabras.
#
# Los textos NO están aquí. Viven en `pruebas/fixtures/formulaciones-retiradas.yaml`,
# que `exclusiones.yaml` ya declara como material de prueba. Escribirlos en este fichero
# obligaría a eximirlo de T161, y una exención es un agujero: el día que alguien escriba
# aquí una frase de verdad, nadie la vería.

FIXTURES_E2 = "kernel/operativo/pruebas/fixtures/formulaciones-retiradas.yaml"


def _casos_e2():
    import yaml
    with open(os.path.join(RAIZ, FIXTURES_E2), encoding="utf-8") as fh:
        return (yaml.safe_load(fh) or {}).get("casos") or []


def _caso_e2(mid):
    caso = next((c for c in _casos_e2() if c.get("id") == mid), None)
    if caso is None:
        raise RuntimeError(f"{FIXTURES_E2} no declara el caso '{mid}'")
    return caso


def _mutaciones_e2():
    """Una mutación por formulación declarada en el fixture. La descripción viene de allí."""
    return [Mutacion(c["id"], "E2", "T161", "comprobar_fuentes",
                     c["descripcion"], _reintroducir(c["id"]))
            for c in _casos_e2()]


def _reintroducir(mid):
    """Devuelve la mutación que añade al final del fichero real su formulación retirada."""
    def aplicar(raiz):
        caso = _caso_e2(mid)
        ruta = os.path.join(raiz, caso["en"])
        if not os.path.isfile(ruta):
            raise RuntimeError(f"la mutación no encaja: no existe {caso['en']}")
        with open(ruta, "a", encoding="utf-8") as fh:
            fh.write("\n" + caso["texto"].rstrip("\n") + "\n")
    return aplicar


def m_t161_patron_desafilado(raiz):
    """Alguien 'arregla' un patrón hasta que deja de detectar lo que declara detectar."""
    _sustituir(raiz, "kernel/operativo/validadores/comprobar_fuentes.py",
               '"patron": r"[Ee]l repositorio es la memoria del proyecto"',
               '"patron": r"ESTO-YA-NO-DETECTA-NADA"')


def m_t161_cobertura_estrechada(raiz):
    """El corpus queda fuera del recorrido: T161 pasaría por no mirar."""
    _sustituir(raiz, "kernel/operativo/validadores/exclusiones.yaml",
               "no_analizados:",
               "no_analizados:\n"
               "  - ruta: kernel/operativo\n"
               "    motivo: 'estrechamiento deliberado para la prueba negativa N161g'\n"
               "  - ruta: kernel/operativo/capacidades\n"
               "    motivo: 'estrechamiento deliberado para la prueba negativa N161g'\n"
               "  - ruta: docs\n"
               "    motivo: 'estrechamiento deliberado para la prueba negativa N161g'\n"
               "  - ruta: packs\n"
               "    motivo: 'estrechamiento deliberado para la prueba negativa N161g'\n")


# ---------------------------------------------------------------------------
#  `F6-H` · los hallazgos externos con propietario y fase `F6` (`11-ARQ` §19)
#  Cada mutación REINTRODUCE el defecto exacto que la fila describía.
# ---------------------------------------------------------------------------

def m_f01_metodo_donde_va_capacidad(raiz):
    """`F-01` · vuelve a nombrarse el MÉTODO donde va la CAPACIDAD."""
    _sustituir(raiz, "kernel/operativo/recorrido/01-PROCESOS.md",
               '  - capacidad: "DIS"\n    condicion: "C-DIS"',
               '  - capacidad: "DIS/Reconstruccion"\n    condicion: "C-DIS"')


def m_f02_owner_como_capacidad(raiz):
    """`F-02` punto 5 · `OWNER` vuelve a viajar como si fuera una de las quince."""
    _sustituir(raiz, "kernel/operativo/recorrido/01-PROCESOS.md",
               '    autoridad_productora: "OWNER"\n', "")


def m_f02_owner_duplicado(raiz):
    """`F-02` punto 5 · `OWNER` vuelve a estar en los DOS campos a la vez.

    Es el estado exacto que el remedio retira: el hallazgo dice MOVER, y añadir el campo de
    autoridad sin quitar el token viejo deja la fila «cerrada» sin haber movido nada.
    """
    _sustituir(raiz, "kernel/operativo/recorrido/01-PROCESOS.md",
               '    autoridad_productora: "OWNER"\n',
               '    capacidad_productora: "OWNER"\n    autoridad_productora: "OWNER"\n')


def m_f02_esquema_sin_tipar(raiz):
    """`F-02` punto 1 · el esquema vuelve a admitir texto libre donde va una capacidad."""
    _sustituir(raiz, "kernel/operativo/esquemas/proceso.yaml",
               "      capacidad_productora:\n        tipo: ref\n        ref_a: capacidad",
               "      capacidad_productora:\n        tipo: texto\n        min: 3\n        _ref_a: capacidad")


def m_f02_variante_sin_declarar(raiz):
    """`F-02` punto 2 · entra una variante que el esquema no declara.

    REAPUNTADA el 2026-09-04, y conviene decir por que en vez de dejarlo en el `git log`.
    Mutaba `DOM:condiciones` a `DOM:revision`, que entonces NO estaba declarada. `D104`
    obligo a declararla —es su caso positivo de la via 4— y en el momento en que el esquema
    la admite este sabotaje deja de discriminar: `T240` seguiria SUPERADA y el control se
    volveria decorativo sin que nadie lo notase. Se reapunta a una variante que sigue SIN
    declarar, `DOM:auditoria`, de modo que el control mide lo mismo que media: que una
    variante ausente del esquema no entra. No se relaja nada; se conserva el poder de
    discriminacion que la ampliacion del esquema le habria quitado en silencio.
    """
    _sustituir(raiz, "kernel/operativo/recorrido/01-PROCESOS.md",
               '  - capacidad: "DOM:condiciones"', '  - capacidad: "DOM:auditoria"')


def m_f02_conjunto_de_variantes_sin_sede(raiz):
    """`F-02` punto 2 · el campo apunta a un conjunto de variantes que ya no existe."""
    _sustituir(raiz, "kernel/operativo/esquemas/proceso.yaml",
               "variantes_de_capacidad:\n", "variantes_de_capacidad_RETIRADA:\n")


def m_f06_dis_a_ver_sin_ancla(raiz):
    """`F-06` · el `cuando` vuelve a no decir CUÁNDO."""
    ruta = os.path.join(raiz, "kernel/operativo/circuitos/DIS-handoffs.md")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    inicio = texto.index('id: handoff:dis-a-ver')
    fin = texto.index("\nentrega:", inicio)
    linea = texto.index("\ncuando:", inicio)
    texto = texto[:linea] + '\ncuando: "DIS cierra su capa y el item continúa hacia verificación"' + texto[fin:]
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto)


def m_f06_dictamen_sin_pasada(raiz):
    """`F-06`, segunda mitad · la entrega deja de decir de qué pasada procede el dictamen."""
    _sustituir(raiz, "kernel/operativo/circuitos/DIS-handoffs.md",
               '  - "el dictamen de excelencia visual con sus nueve ejes, y de qué PASADA procede cada uno: '
               'los ocho de la PASADA DE DISEÑO —estación 9, antes de entregar a Construcción— y el eje '
               'fidelidad de la PASADA DE FIDELIDAD —estación 11, con la capa ya construida—"',
               '  - "el dictamen de excelencia visual con sus nueve ejes"')


def m_f07_sin_declaracion_de_autoridad(raiz):
    """`F-07` · la distinción aprobada/trabajo vuelve a estar sólo en prosa."""
    ruta = os.path.join(raiz, "kernel/operativo/validadores/exclusiones.yaml")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    corte = texto.index("autoridad_de_documentos_del_owner:")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto[:corte])


def m_f07_autoridad_que_no_deriva(raiz):
    """`F-07` · alguien ESCRIBE la autoridad en vez de derivarla de la clase canónica."""
    _sustituir(raiz, "kernel/operativo/validadores/exclusiones.yaml",
               "  - ruta: docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md\n    autoridad: aprobada",
               "  - ruta: docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md\n    autoridad: trabajo")


def m_f07_documento_del_owner_sin_autoridad(raiz):
    """`F-07` · entra un documento nuevo a `docs/owner/` y pasa por omisión."""
    _escribir(raiz, "docs/owner/ADS-NOTA-NUEVA.md",
              "# Nota del Owner\n\nUn documento nuevo que nadie clasificó.\n")


def m_f05_entrega_de_8_0_que_falta(raiz):
    """`F-05` (i) · desaparece una de las cinco instancias que §8.0 declara."""
    ruta = os.path.join(raiz, "kernel/operativo/circuitos/entregas-de-8-0.md")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    inicio = texto.index("```yaml ads:handoff\nid: handoff:sis-a-ver")
    fin = texto.index("```", texto.index("checkpoint:", inicio)) + 4
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto[:inicio] + texto[fin:])


def m_f04_grado_inicial_que_no_coincide(raiz):
    """`F-04` · el grado de entrada deja de coincidir con el que midió el paso 5."""
    _sustituir(raiz, "kernel/operativo/entrada/05-ESCENARIOS.md",
               "  grado: media\n  grado_inicial: alta",
               "  grado: media\n  grado_inicial: media")


def m_f10_biyeccion_falsa(raiz):
    """`F-10` · la cabecera vuelve a afirmar una forma por clase de expresión."""
    _sustituir(raiz, "kernel/operativo/entrada/03-FORMAS.md",
               "> Catálogo. Contiene catorce bloques `ads:forma-conversacion`. **No hay uno por clase de",
               "> Catálogo. Contiene catorce bloques `ads:forma-conversacion`, uno por clase de expresión.\n> **No hay uno por clase de")


def m_f11_cabecera_con_rango_falso(raiz):
    """`F-11` · la cabecera vuelve a afirmar un rango que el fichero no contiene."""
    _sustituir(raiz, "kernel/operativo/entrada/05-ESCENARIOS.md",
               "son las pruebas **T75–T80** y **T154–T157**",
               "son las pruebas T75 a T84")


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
             "un rol se concede lo que su capacidad ESCALA",
             m_rol_decide_de_mas),
    Mutacion("N146b", "A-18", "T146", "comprobar_contratos",
             "un rol se concede la materia declarada por otra capacidad",
             m_rol_decide_materia_ajena),
    Mutacion("N90", "A-15", "T90", "comprobar_contratos",
             "un método deja de estar declarado por su capacidad, como ENC/Critica",
             m_metodo_huerfano),
    Mutacion("N92", "—", "T92", "comprobar_contratos",
             "una marca comercial entra por un esquema, que antes no se miraba",
             m_marca_en_esquema),
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
    Mutacion("N144", "A-13", "T144", "comprobar_contratos",
             "se rompe el vínculo entre CON y gate:usabilidad",
             m_con_sin_usabilidad),
    Mutacion("N144b", "A-13", "T144", "comprobar_contratos",
             "el vínculo existe pero deja de decir quién juzga la evidencia",
             m_con_usabilidad_sin_juez),
    Mutacion("N158", "evidencia", "T158", "comprobar_evidencia",
             "se archiva una invocación SIN .py — el defecto exacto de la entrega anterior",
             m_evidencia_sin_py),
    Mutacion("N158b", "evidencia", "T158", "comprobar_evidencia",
             "una evidencia afirma éxito sin la salida que lo respalda",
             m_evidencia_afirma_exito_sin_salida),
    Mutacion("N158c", "evidencia", "T158", "comprobar_evidencia",
             "la evidencia de un validador ocupa el fichero de otro",
             m_evidencia_de_otro_validador),
    Mutacion("N158d", "evidencia", "T158", "comprobar_evidencia",
             "se publica una ejecución cuyo código no fue cero",
             m_evidencia_con_codigo_no_cero),
    Mutacion("N158e", "evidencia", "T158", "comprobar_evidencia",
             "falta un fichero de evidencia que el manifiesto exige",
             m_evidencia_falta),
    Mutacion("N158f", "evidencia", "T158", "comprobar_evidencia",
             "un validador nuevo queda fuera del manifiesto y de la evidencia",
             m_validador_fuera_del_manifiesto),
    Mutacion("N158g", "evidencia", "T158", "comprobar_evidencia",
             "la cobertura publicada describe un corpus con dos ficheros menos que el vigente",
             m_evidencia_caducada,
             espera="La evidencia está CADUCADA"),
    Mutacion("N158h", "evidencia", "T158", "comprobar_evidencia",
             "una vigencia declara un recuento que nadie implementa",
             m_vigencia_sin_implementacion,
             espera="no está registrado en RECUENTOS_DE_VIGENCIA"),
    Mutacion("N158i", "evidencia", "T158", "comprobar_evidencia",
             "una entrada de vigencia no declara `patron` — el caso que reventaba con KeyError",
             m_vigencia_sin_patron,
             espera="no declara `patron`"),
    Mutacion("N158j", "evidencia", "T158", "comprobar_evidencia",
             "`vigencia` se declara como mapa suelto en vez de como lista",
             m_vigencia_no_es_lista,
             espera="tiene que ser una lista de entradas"),
    Mutacion("N158k", "evidencia", "T158", "comprobar_evidencia",
             "una entrada de vigencia es una cadena en vez de un mapa",
             m_vigencia_entrada_no_es_mapa,
             espera="tiene que ser un mapa"),
    Mutacion("N158l", "evidencia", "T158", "comprobar_evidencia",
             "el patrón de una vigencia no es una expresión regular válida",
             m_vigencia_regex_invalida,
             espera="no es una expresión regular válida"),
    Mutacion("N158m", "evidencia", "T158", "comprobar_evidencia",
             "el patrón de una vigencia no declara grupo de captura",
             m_vigencia_sin_grupo_de_captura,
             espera="no declara ningún grupo de captura"),
    Mutacion("N158n", "evidencia", "T158", "comprobar_evidencia",
             "el grupo de captura de una vigencia no devuelve un entero",
             m_vigencia_captura_no_entera,
             espera="que no es un entero"),
    Mutacion("N158o", "evidencia", "T158", "comprobar_evidencia",
             "dos entradas de vigencia comparten identificador",
             m_vigencia_id_duplicado,
             espera="está declarada dos veces"),
    Mutacion("N153", "prompts", "T153", "comprobar_prompts",
             "un prompt deja de nombrar el gate contra el que cierra",
             m_prompt_sin_gate),
    Mutacion("N153b", "prompts", "T153", "comprobar_prompts",
             "un prompt instruye hablar con el Owner sin que su rol pueda",
             m_prompt_habla_con_owner),
    Mutacion("N153c", "prompts", "T153", "comprobar_prompts",
             "un prompt pierde el enlace a su método",
             m_prompt_sin_metodo),
    Mutacion("N148", "A-02", "T148", "comprobar_arranque",
             "la documentación vuelve a citar un pack derogado",
             m_arranque_con_pack_derogado),
    Mutacion("N152", "A-12", "T152", "comprobar_versiones",
             "el release cambia y ningún punto de entrada se entera",
             m_version_incoherente),
    Mutacion("N152b", "A-12", "T152", "comprobar_versiones",
             "la línea histórica se sube al ritmo del release, que es otro contador",
             m_kernel_md_iguala_release),
    Mutacion("N151", "A-24", "T151", "comprobar_recuentos",
             "un documento vuelve a escribir a mano una cifra que ya no cuadra",
             m_recuento_a_mano),
    Mutacion("N142", "A-11", "T142", "comprobar_contratos",
             "el esquema de encuadre pierde un estado que sus métodos exigen",
             m_encuadre_sin_estado_exigido),
    Mutacion("N142b", "A-11", "T142", "comprobar_contratos",
             "vuelve `aparcado` como estado propio, contra b.2",
             m_encuadre_con_aparcado),
    Mutacion("N145", "A-14", "T145", "comprobar_contratos",
             "la crítica vuelve a activarse por el grado final y puede evaporarse",
             m_critica_por_grado_final),
    Mutacion("N145b", "A-14", "T145", "comprobar_contratos",
             "el encuadre deja de persistir con qué grado de incertidumbre entró",
             m_sin_grado_inicial),
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
    *_mutaciones_e2(),
    Mutacion("N171", "§100", "T171", "comprobar_arranque",
             "el prompt de arranque deja de declarar dónde se lee un criterio del §100",
             m_t171_bootstrap_sin_la_regla_de_no_copiar),
    Mutacion("N171b", "§100", "T171", "comprobar_arranque",
             "cómo materializar una fuente ausente deja de estar en ningún sitio",
             m_t171_sin_como_materializar),
    Mutacion("N161f", "E2", "T161", "comprobar_fuentes",
             "un patrón de T161 se desafila hasta dejar de detectar su propia formulación",
             m_t161_patron_desafilado),
    Mutacion("N161g", "E2", "T161", "comprobar_fuentes",
             "el corpus queda fuera del recorrido y T161 pasaría por no mirar",
             m_t161_cobertura_estrechada),
    Mutacion("N147e", "E5", "T147", "comprobar_referencias",
             "la frontera del proyecto instalado se usa para tapar un enlace roto de aquí",
             m_frontera_para_silenciar_un_enlace_roto,
             espera="no existe en este repositorio"),
    Mutacion("N147f", "E5", "T147", "comprobar_referencias",
             "una frontera declarada se queda sin motivo escrito",
             m_frontera_sin_motivo,
             espera="sin `ruta` o sin `motivo`"),
    Mutacion("N240", "F-01", "T240", "comprobar_contratos",
             "vuelve a nombrarse un MÉTODO donde va una CAPACIDAD",
             m_f01_metodo_donde_va_capacidad,
             espera="MÉTODO donde va"),
    Mutacion("N240b", "F-02", "T240", "comprobar_contratos",
             "la obligación del Owner se queda sin ninguna de las dos claves",
             m_f02_owner_como_capacidad,
             espera="EXACTAMENTE UNA"),
    Mutacion("N240f", "F-02", "T240", "comprobar_contratos",
             "`OWNER` vuelve a estar en el campo de CAPACIDAD, además del de autoridad",
             m_f02_owner_duplicado,
             espera="sigue nombrando `OWNER` en el campo de CAPACIDAD"),
    Mutacion("N240c", "F-02", "T240", "comprobar_contratos",
             "el esquema vuelve a admitir texto libre donde va una capacidad",
             m_f02_esquema_sin_tipar,
             espera="no tipa `capacidad_productora`"),
    Mutacion("N240d", "F-02", "T240", "comprobar_contratos",
             "entra una variante de capacidad que el esquema no declara",
             m_f02_variante_sin_declarar,
             espera="que el esquema no declara"),
    Mutacion("N240e", "F-02", "T240", "comprobar_contratos",
             "el conjunto de variantes admitidas se queda sin sede en el esquema",
             m_f02_conjunto_de_variantes_sin_sede,
             espera="el esquema no declara esa lista"),
    Mutacion("N241", "F-06", "T241", "comprobar_contratos",
             "el `cuando` de la entrega de DIS a VER vuelve a no nombrar estación",
             m_f06_dis_a_ver_sin_ancla,
             espera="no nombra ninguna estación"),
    Mutacion("N241b", "F-06", "T241", "comprobar_contratos",
             "el dictamen visual deja de decir de qué pasada procede",
             m_f06_dictamen_sin_pasada,
             espera="de qué PASADA procede"),
    Mutacion("N242", "F-07", "T242", "comprobar_contratos",
             "la autoridad de los documentos del Owner vuelve a estar sólo en prosa",
             m_f07_sin_declaracion_de_autoridad,
             espera="autoridad_de_documentos_del_owner"),
    Mutacion("N242b", "F-07", "T242", "comprobar_contratos",
             "alguien ESCRIBE la autoridad en vez de derivarla de la clase canónica",
             m_f07_autoridad_que_no_deriva,
             espera="su clase canónica"),
    Mutacion("N242c", "F-07", "T242", "comprobar_contratos",
             "un documento nuevo entra en docs/owner/ y pasaría por omisión",
             m_f07_documento_del_owner_sin_autoridad,
             espera="NO declara su autoridad"),
    Mutacion("N243", "F-05", "T243", "comprobar_contratos",
             "desaparece una de las cinco instancias de handoff que §8.0 declara",
             m_f05_entrega_de_8_0_que_falta,
             espera="qué viaja de SIS a VER"),
    Mutacion("N244", "F-04", "T244", "comprobar_contratos",
             "el grado inicial deja de coincidir con el que midió el paso 5",
             m_f04_grado_inicial_que_no_coincide,
             espera="grado_inicial"),
    Mutacion("N245", "F-10", "T245", "comprobar_recuentos",
             "la cabecera vuelve a afirmar una forma por clase de expresión",
             m_f10_biyeccion_falsa,
             espera="La aposición es falsa"),
    Mutacion("N246", "F-11", "T246", "comprobar_recuentos",
             "la cabecera vuelve a afirmar un rango de pruebas que no contiene",
             m_f11_cabecera_con_rango_falso,
             espera="`F-11`"),
]


# --- los sabotajes de la corrección del 2026-09-04, por eje ------------------------------
# El catálogo sigue siendo UNO. Lo que se reparte es DÓNDE se escribe cada entrada, porque
# tres correcciones disjuntas escribiendo sobre la misma lista no se pueden revisar por
# partes. La incorporación es POR NOMBRE y SIN `try/except ImportError`: si un módulo falta
# o no importa, este validador revienta al arrancar en vez de publicar un catálogo más corto
# y un verde más barato, que es la degradación silenciosa que `E-14` describe.
import negativos_cardinalidad  # noqa: E402
import negativos_contratos19  # noqa: E402
import negativos_integridad  # noqa: E402

for _eje in (negativos_cardinalidad, negativos_contratos19, negativos_integridad):
    CATALOGO.extend(_eje.CATALOGO)

_vistos = [m.id for m in CATALOGO]
if len(_vistos) != len(set(_vistos)):
    _repes = sorted({i for i in _vistos if _vistos.count(i) > 1})
    raise SystemExit(
        "dos infracciones comparten identificador: " + ", ".join(_repes)
        + ". Un identificador repetido hace indistinguibles dos sabotajes distintos"
    )


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

    # Una traza NO es una detección. Un validador que revienta ante una entrada inválida no
    # dice qué corregir, tumba las comprobaciones que venían detrás y deja sin comprobar lo
    # que nadie declara sin comprobar. Se mide aparte, y descalifica el caso.
    if "Traceback (most recent call last)" in proc.stderr:
        mut.resultado = "NO DETECTADA"
        traza = [l for l in proc.stderr.strip().splitlines() if l.strip()][-1][:160]
        mut.detalle = (f"{mut.validador} terminó con TRAZA en vez de con un fallo "
                       f"explicativo: {traza}")
        return
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
        return
    if fila.get("estado") != "prueba-fallida":
        mut.resultado = "NO DETECTADA"
        mut.detalle = f"{mut.prueba} siguió SUPERADA con la infracción introducida"
        return

    fallos = fila.get("fallos") or []
    # El truncado a 120 puede caer justo en un espacio, y entonces la línea publicada
    # termina en blanco: `git diff --check` lo marca como trailing whitespace en cada
    # regeneración. Se recorta DESPUÉS de truncar, en los dos diagnósticos —el esperado y
    # el general—, porque el defecto está en el corte y no en el texto de origen.
    def _corta(texto):
        return texto[:120].rstrip()

    if mut.espera and not any(mut.espera in f for f in fallos):
        mut.resultado = "NO DETECTADA"
        mut.detalle = (f"{mut.prueba} falló, y NO por el motivo esperado. Se buscaba "
                       f"«{mut.espera}» y se obtuvo: "
                       f"{_corta((fallos or ['(sin detalle)'])[0])}")
        return
    elegido = next((f for f in fallos if mut.espera and mut.espera in f), None)
    mut.resultado = "detectada"
    mut.detalle = _corta(elegido or (fallos or ["(sin detalle)"])[0])


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
