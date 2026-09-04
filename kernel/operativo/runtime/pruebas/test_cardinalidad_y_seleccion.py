#!/usr/bin/env python3
"""test_cardinalidad_y_seleccion — `C4` «cuántos agentes por rol» y `b.12` «paso 5 e inanición».

Cierra dos hallazgos de la certificación del 2026-09-03, y los cierra por la propiedad y no
por el texto:

  `E-01`  las TRES composiciones reales que declaran varios agentes materializaban UNO, con
          `reparto_de_agentes` vacío, sin error, sin aviso y sin `esperando-capacidad`,
          mientras el registro durable publicaba «2 o 3» al lado de ese agente único. El
          reparto entraba como PARÁMETRO EXTERNO porque el módulo declaraba que el campo
          `agentes` era «prosa». La medición desmintió la premisa: noventa y nueve valores
          en veintidós formas, tres de ellas plurales. Aquí el cardinal se DERIVA.

  `E-06`  de los cuatro criterios de orden de `b.12` paso 5 sólo estaban (a) y (d), y de los
          cuatro campos de inanición no existía ninguno. `elegibles()` ordenaba por
          `(-prioridad, id)` y no contaba nada. Aquí están los cuatro y los cuatro, con su
          persistencia durable, su reanudación y su concurrencia.

LAS CUATRO REGLAS QUE ESTA BATERÍA SE IMPONE:

  1. NINGUNA PRUEBA MIRA TEXTO. Ni una sola comprueba que un `.md` diga algo. Todas mueven
     el código sobre el corpus REAL del kernel, sobre un control repo REAL con su catálogo
     de modelos, y sobre un estado durable REAL escrito por el motor.

  2. CADA NEGATIVO TIENE SU PROPIA PRUEBA. Los diez casos negativos de `C4` no comparten un
     `assertRaises` genérico: cada uno nombra su error tipado y su contexto, porque «falla»
     y «falla por esto» son cosas distintas y la primera se puede conseguir rompiendo el
     entorno.

  3. LO QUE SE CORRIGE TIENE QUE PODER PONERSE ROJO. `T269` sabotea, en una COPIA del árbol
     y en PROCESOS REALES, cada uno de los cuatro criterios de orden, cada uno de los cuatro
     campos de inanición y tres piezas de la cardinalidad, y exige que cada sabotaje ponga
     roja una prueba DISTINTA de esta misma batería. Ningún criterio queda decorativo.

  4. NADA DEPENDE DEL RELOJ DE PARED. `a.9` lo prohíbe en el estado canónico. La antigüedad
     de espera se mide con la REVISIÓN del motor, que es monótona y reproducible, y `T267`
     lo comprueba leyendo lo durable.

    python3 kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py

Sale con 0 si todo pasa. Se ejecuta desde cualquier directorio: la raíz se deriva de
`__file__` y NUNCA del `cwd`.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
RUNTIME = os.path.join(RAIZ, "kernel", "operativo", "runtime")
KERNEL = os.path.join(RAIZ, "kernel", "operativo")
sys.path.insert(0, RUNTIME)
sys.path.insert(0, AQUI)

import adaptadores                                                     # noqa: E402
import catalogo_de_prueba                                              # noqa: E402
import ciclo                                                           # noqa: E402
import runtime as paquete_runtime                                      # noqa: E402
from ciclo import agentes, equipos, errores                            # noqa: E402
from estado.errores import RutaInvalida                                # noqa: E402
from runtime import modelo, politica as politica_de_seleccion          # noqa: E402

SEGUNDOS_DE_ESPERA = 300

# Las TRES composiciones del corpus que declaran más de un agente sobre un mismo rol, con el
# cardinal que su campo `agentes` escribe. Se transcriben para CONFRONTAR el censo derivado,
# no para sustituirlo: `test_01` comprueba que el corpus no tiene ninguna más.
PLURALES = {
    ("composicion:dis-proyecto-nuevo", "DIS/investigacion-visual"):
        "1 o 2 repartidos por territorio",
    ("composicion:dis-proyecto-nuevo", "DIS/diseno-visual"):
        "2 o 3, uno por dirección explorada",
    ("composicion:dis-feature-visual", "DIS/diseno-visual"):
        "1 o 2 en competencia declarada",
}

# El campo `agentes` de `CON/implementacion`. NO es pluralidad de agentes: es paralelismo de
# PAQUETES del mismo item, que gobierna la condición compuesta de `a.5`. Se prueba aparte
# para que nadie lo cuente como una cuarta composición plural.
CON_PARALELISMO = ("1 por paquete; varios paquetes del mismo item pueden ir en paralelo si "
                   "cumplen las seis condiciones de a.5")

INTEGRADOR_DE_DIS = "DIS/direccion-artistica"

ORDEN_DE_PRUEBA = {"adaptador": "proceso-local", "operacion": "ejecutar",
                   "argumentos": ["true"], "limite_segundos": 30.0}


def copiar_kernel(destino):
    """Una COPIA REAL de `kernel/operativo`. Mismo corpus y mismo runtime, en otro sitio."""
    copia = os.path.join(destino, "kernel", "operativo")
    os.makedirs(os.path.dirname(copia), exist_ok=True)
    shutil.copytree(KERNEL, copia,
                    ignore=shutil.ignore_patterns("__pycache__", "evidencia"))
    return copia


def sustituir(ruta, viejo, nuevo):
    with open(ruta, encoding="utf-8") as manejador:
        texto = manejador.read()
    if viejo not in texto:
        raise AssertionError("la mutación no encaja en " + ruta + ": " + viejo[:80])
    with open(ruta, "w", encoding="utf-8") as manejador:
        manejador.write(texto.replace(viejo, nuevo, 1))


# =========================================================================
#  `E-01` · T250…T259 · el CARDINAL de `C4`, derivado del corpus
# =========================================================================
class Cardinalidad(unittest.TestCase):
    """El corpus real del kernel y un control repo real con su catálogo de modelos."""

    @classmethod
    def setUpClass(cls):
        cls.corpus = ciclo.Corpus(KERNEL)
        cls.politica = agentes.Politica(cls.corpus)

    def setUp(self):
        self.repo = tempfile.mkdtemp(prefix="ads-cardinal-")
        self.addCleanup(shutil.rmtree, self.repo, True)
        catalogo_de_prueba.escribir(self.repo, self.politica, self.corpus)

    # ------------------------------------------------------------- ayudas
    def proyecto_nuevo(self, *, corpus=None, slots=99, **extra):
        """`composicion:dis-proyecto-nuevo` con sus DOS repartos declarados como contenido."""
        declarado = {
            "DIS/investigacion-visual": {"territorios": ["marca", "producto"]},
            "DIS/diseno-visual": {"direcciones": ["calida", "sobria", "brutal"]},
        }
        declarado.update(extra.pop("reparto_declarado", None) or {})
        return equipos.materializar(
            "DIS", corpus=corpus or self.corpus, control_repo=self.repo,
            composiciones_verdaderas=["composicion:dis-proyecto-nuevo"], slots=slots,
            reparto_declarado=declarado, **extra)

    def feature_visual(self, *, corpus=None, slots=99, **extra):
        return equipos.materializar(
            "DIS", corpus=corpus or self.corpus, control_repo=self.repo,
            composiciones_verdaderas=["composicion:dis-feature-visual"], slots=slots,
            **extra)

    def filas(self, equipo, rol):
        todas = (equipo["roles"] + equipo["esperando_capacidad"] + equipo["bloqueados"])
        return [f for f in todas if f["rol"] == rol]

    def plan(self, equipo, rol):
        for entrada in equipo["reparto_de_agentes"]:
            if entrada["rol"] == rol:
                return entrada
        raise AssertionError("el equipo no publica reparto para " + rol)

    # --------------------------------------------------------------- T250
    def test_250_el_cardinal_se_DERIVA_del_corpus_y_hay_tantos_agentes_como_dice(self):
        """T250 · Defecto que previene: publicar «2 o 3» junto a UN agente.

        Es el hecho central de `E-01`, medido: las tres composiciones plurales del corpus
        materializaban un agente y `reparto_de_agentes` salía VACÍO. Aquí se exige lo
        contrario y por el mismo camino: la composición dice el cardinal, el runtime lo
        DERIVA, y hay tantos agentes REALES —con su identificador propio— como el cardinal
        publica. Si alguien vuelve a no replicar, esta prueba cuenta uno donde dice tres.
        """
        # El censo del corpus se DERIVA, y las plurales son exactamente TRES.
        censo = equipos.censo_de_cardinales(self.corpus)
        self.assertTrue(equipos.exigir_censo_legible(self.corpus))
        derivadas = {}
        for capacidad in ciclo.CAPACIDADES:
            for composicion in self.corpus.composiciones(capacidad):
                todos = [str(e["rol"]) for e in composicion["roles"]]
                for entrada in composicion["roles"]:
                    lectura = equipos.leer_cardinal(entrada["agentes"], roles=todos)
                    if lectura["maximo"] > 1:
                        derivadas[(composicion["id"], entrada["rol"])] = lectura["literal"]
        self.assertEqual(derivadas, PLURALES,
                         "el censo de composiciones plurales no es el medido: si aparece "
                         "una nueva hay que leerla, no ignorarla")
        self.assertIn("1", censo, "el censo no se ha derivado del corpus")

        equipo = self.proyecto_nuevo()
        # TRES agentes en `DIS/diseno-visual`, uno por dirección explorada, y DOS en
        # `DIS/investigacion-visual`, uno por territorio. Con su integrador declarado.
        visual = self.plan(equipo, "DIS/diseno-visual")
        self.assertEqual((visual["minimo"], visual["maximo"]), (2, 3))
        self.assertEqual(visual["modo"], equipos.MODO_DIRECCION)
        self.assertEqual(visual["agentes"], 3)
        self.assertEqual(visual["integra"], INTEGRADOR_DE_DIS)
        self.assertEqual(visual["unidades"], ["calida", "sobria", "brutal"])

        investigacion = self.plan(equipo, "DIS/investigacion-visual")
        self.assertEqual(investigacion["agentes"], 2)
        self.assertEqual(investigacion["modo"], equipos.MODO_TERRITORIO)
        self.assertEqual(investigacion["integra"], INTEGRADOR_DE_DIS)

        # AGENTES REALES: tres filas, tres identificadores distintos, cada uno con SU unidad
        # del reparto y su integrador escritos en el registro durable.
        filas = self.filas(equipo, "DIS/diseno-visual")
        self.assertEqual(len(filas), 3)
        self.assertEqual(len({f["agente"] for f in filas}), 3,
                         "tres agentes con el mismo identificador son uno solo para el "
                         "corte por `execution_slots`")
        self.assertEqual(sorted(f["reparto"]["unidad"] for f in filas),
                         ["brutal", "calida", "sobria"])
        for fila in filas:
            self.assertEqual(fila["reparto"]["integra"], INTEGRADOR_DE_DIS)
            self.assertEqual(fila["reparto"]["modo"], equipos.MODO_DIRECCION)
            self.assertTrue(fila["modelo"])
        self.assertEqual(equipo["integrador"], INTEGRADOR_DE_DIS)
        # El registro NO se autocontradice, y hay una función que lo exige.
        self.assertTrue(equipos.exigir_reparto_coherente(equipo))

        # Un rol PLURAL consume tantos slots como agentes: con holgura, los cinco caben.
        self.assertEqual(
            len([u for u in equipo["agentes"] if u["estado"] == "despachado"]),
            equipo["slots_ocupados"])
        self.assertGreaterEqual(equipo["slots_ocupados"], 5)

    # --------------------------------------------------------------- T251
    def test_251_el_registro_durable_no_puede_publicar_dos_o_tres_y_un_agente(self):
        """T251 · Defecto que previene: un registro internamente contradictorio.

        `C4` paso 7 es lo que hace auditable la materialización. Un equipo que publica el
        cardinal por un lado y un agente por otro no es un registro: son dos afirmaciones y
        ninguna verdad. Se comprueba con el equipo REAL, y después se FUERZA la
        contradicción sobre el objeto ya escrito para ver que la comprobación la caza.
        """
        equipo = self.proyecto_nuevo()
        self.assertTrue(equipos.exigir_reparto_coherente(equipo))

        # Se retiran dos de las tres filas, que es exactamente lo que la auditoría midió:
        # el cardinal sigue diciendo tres y en el equipo hay uno.
        roto = json.loads(json.dumps(equipo))
        conservada = False
        supervivientes = []
        for fila in roto["roles"]:
            if fila["rol"] == "DIS/diseno-visual":
                if conservada:
                    continue
                conservada = True
            supervivientes.append(fila)
        roto["roles"] = supervivientes
        with self.assertRaises(errores.RepartoIncoherente) as capturado:
            equipos.exigir_reparto_coherente(roto)
        self.assertEqual(capturado.exception.contexto["rol"], "DIS/diseno-visual")
        self.assertEqual(capturado.exception.contexto["derivados"], 3)

        # Y el cardinal FUERA de su rango escrito tampoco pasa.
        otro = json.loads(json.dumps(equipo))
        for entrada in otro["reparto_de_agentes"]:
            if entrada["rol"] == "DIS/diseno-visual":
                entrada["agentes"] = 9
        with self.assertRaises(errores.RepartoIncoherente):
            equipos.exigir_reparto_coherente(otro)

    # --------------------------------------------------------------- T252
    def test_252_reparto_por_territorio_SIN_territorios_falla_cerrado(self):
        """T252 · Defecto que previene: repartir sin saber entre qué.

        `C4` condición (a) exige que el trabajo se reparta «sin solapamiento», y eso no se
        puede comprobar sin las unidades del reparto. Un territorio es una respuesta
        legítima; NINGUNO es que nadie ha contestado, y ahí no hay un valor por omisión.
        """
        with self.assertRaises(errores.RepartoSinUnidades) as capturado:
            equipos.materializar(
                "DIS", corpus=self.corpus, control_repo=self.repo,
                composiciones_verdaderas=["composicion:dis-proyecto-nuevo"], slots=99,
                reparto_declarado={"DIS/diseno-visual": {"direcciones": ["a", "b"]}})
        self.assertEqual(capturado.exception.contexto["rol"], "DIS/investigacion-visual")
        self.assertEqual(capturado.exception.contexto["clave"], "territorios")

        # Y con territorios REPETIDOS tampoco: dos agentes sobre el mismo territorio es
        # exactamente el solapamiento que `C4` prohíbe.
        with self.assertRaises(errores.RepartoSinUnidades):
            self.proyecto_nuevo(reparto_declarado={
                "DIS/investigacion-visual": {"territorios": ["marca", "marca"]}})

        # CONTROL: con UN territorio se materializa UN agente, dentro del cardinal escrito.
        uno = self.proyecto_nuevo(reparto_declarado={
            "DIS/investigacion-visual": {"territorios": ["marca"]}})
        self.assertEqual(self.plan(uno, "DIS/investigacion-visual")["agentes"], 1)
        self.assertEqual(len(self.filas(uno, "DIS/investigacion-visual")), 1)

        # Y MÁS unidades que el cardinal máximo tampoco: el cardinal escrito manda.
        with self.assertRaises(errores.RepartoIncoherente):
            self.proyecto_nuevo(reparto_declarado={
                "DIS/investigacion-visual": {"territorios": ["a", "b", "c"]}})

    # --------------------------------------------------------------- T253
    def test_253_la_competencia_exige_criterio_de_comparacion_escrito_ANTES(self):
        """T253 · Defecto que previene: comparar con un criterio escrito después de mirar.

        `C4`: la competencia vale «sólo si el método lo declara, y con criterio de
        comparación escrito ANTES de empezar». El «antes» se mide contra el instante lógico
        de inicio del trabajo, no contra la buena voluntad de nadie.
        """
        comun = dict(metodo="Fundacion", inicio=10)
        # 1 · sin criterio.
        with self.assertRaises(errores.CriterioDeComparacionAusente):
            self.feature_visual(reparto_declarado={
                "DIS/diseno-visual": {"competencia": 2}}, **comun)
        # 2 · con criterio y SIN instante de declaración: el «antes» no es comprobable.
        with self.assertRaises(errores.CriterioDeComparacionAusente):
            self.feature_visual(reparto_declarado={"DIS/diseno-visual": {
                "competencia": 2, "criterio_de_comparacion": "cuál sostiene la diferencia"}},
                **comun)
        # 3 · criterio declarado DESPUÉS de empezar: es justificación, no comparación.
        with self.assertRaises(errores.CriterioDeComparacionAusente) as capturado:
            self.feature_visual(reparto_declarado={"DIS/diseno-visual": {
                "competencia": 2, "criterio_de_comparacion": "cuál gusta más",
                "criterio_declarado_en": 11}}, **comun)
        self.assertEqual(capturado.exception.contexto["declarado_en"], 11)
        self.assertEqual(capturado.exception.contexto["inicio"], 10)
        # 4 · criterio a la vez que el inicio: tampoco es ANTES.
        with self.assertRaises(errores.CriterioDeComparacionAusente):
            self.feature_visual(reparto_declarado={"DIS/diseno-visual": {
                "competencia": 2, "criterio_de_comparacion": "c",
                "criterio_declarado_en": 10}}, **comun)
        # 5 · sin instante de inicio en el paquete no hay contra qué medir.
        with self.assertRaises(errores.CriterioDeComparacionAusente):
            self.feature_visual(metodo="Fundacion", reparto_declarado={
                "DIS/diseno-visual": {"competencia": 2, "criterio_de_comparacion": "c",
                                      "criterio_declarado_en": 3}})
        # 6 · el método sin fase divergente no admite competencia, aunque haya criterio.
        with self.assertRaises(errores.CriterioDeComparacionAusente):
            self.feature_visual(metodo="CriticaVisual", inicio=10, reparto_declarado={
                "DIS/diseno-visual": {"competencia": 2, "criterio_de_comparacion": "c",
                                      "criterio_declarado_en": 3}})

        # CONTROL POSITIVO: criterio ESCRITO ANTES y método con fase divergente.
        bien = self.feature_visual(reparto_declarado={"DIS/diseno-visual": {
            "competencia": 2, "criterio_de_comparacion": "cuál sostiene la diferencia",
            "criterio_declarado_en": 4}}, **comun)
        plan = self.plan(bien, "DIS/diseno-visual")
        self.assertEqual(plan["agentes"], 2)
        self.assertEqual(plan["modo"], equipos.MODO_COMPETENCIA)
        self.assertEqual(plan["integra"], INTEGRADOR_DE_DIS)
        self.assertEqual(plan["criterio_de_comparacion"], "cuál sostiene la diferencia")
        self.assertEqual(len(self.filas(bien, "DIS/diseno-visual")), 2)
        for fila in self.filas(bien, "DIS/diseno-visual"):
            self.assertTrue(fila["reparto"]["criterio_de_comparacion"])

        # Y sin competencia declarada se materializa el MÍNIMO: es el «1 AGENTE por defecto,
        # siempre» de `C4`, no un silencio.
        solo = self.feature_visual()
        self.assertEqual(self.plan(solo, "DIS/diseno-visual")["agentes"], 1)

    # --------------------------------------------------------------- T254
    def test_254_varios_agentes_SIN_integrador_declarado_esta_prohibido(self):
        """T254 · Defecto que previene: tres propuestas y ninguna decisión.

        `C4` lo dice con todas las letras. El integrador vive en el campo `ampliacion` de la
        composición y el runtime no lo leía: lo pedía por la firma, de modo que la
        prohibición sólo alcanzaba a quien se molestara en declarar el reparto. Aquí se
        BORRA la declaración en una COPIA del corpus y se exige que la materialización caiga.
        """
        base = tempfile.mkdtemp(prefix="ads-sin-integrador-")
        self.addCleanup(shutil.rmtree, base, True)
        copia = copiar_kernel(base)
        sustituir(os.path.join(copia, "capacidades", "DIS", "composicion.md"),
                  "Un agente de DIS/diseno-visual por cada dirección explorada, con "
                  "DIS/direccion-artistica\n  como integrador declarado.",
                  "Un agente de DIS/diseno-visual por cada dirección explorada.")
        mutado = ciclo.Corpus(copia)
        self.assertIsNone(equipos.integrador_de(
            [c for c in mutado.composiciones("DIS")
             if c["id"] == "composicion:dis-proyecto-nuevo"][0]))
        with self.assertRaises(errores.VariosAgentesSinIntegrador) as capturado:
            self.proyecto_nuevo(corpus=mutado)
        self.assertEqual(capturado.exception.contexto["composicion"],
                         "composicion:dis-proyecto-nuevo")
        # CONTROL: sobre el corpus INTACTO el mismo equipo se materializa.
        self.assertTrue(self.proyecto_nuevo()["reparto_de_agentes"])

    # --------------------------------------------------------------- T255
    def test_255_un_integrador_que_no_es_rol_de_la_composicion_no_integra_nada(self):
        """T255 · Defecto que previene: un integrador nombrado que no ocupa ningún rol.

        El integrador se CONTRASTA contra la lista `roles` de la composición. Declararlo y
        que no exista es peor que no declararlo: parece que hay quien decide.
        """
        base = tempfile.mkdtemp(prefix="ads-integrador-fantasma-")
        self.addCleanup(shutil.rmtree, base, True)
        copia = copiar_kernel(base)
        sustituir(os.path.join(copia, "capacidades", "DIS", "composicion.md"),
                  "con DIS/direccion-artistica\n  como integrador declarado.",
                  "con DIS/no-existe\n  como integrador declarado.")
        mutado = ciclo.Corpus(copia)
        with self.assertRaises(errores.VariosAgentesSinIntegrador) as capturado:
            self.proyecto_nuevo(corpus=mutado)
        self.assertEqual(capturado.exception.contexto["integrador"], "DIS/no-existe")

    # --------------------------------------------------------------- T256
    def test_256_un_volumen_que_excede_el_contexto_no_se_despacha_a_ciegas(self):
        """T256 · Defecto que previene: dar un trabajo que no cabe y descubrirlo a la mitad.

        `C4` condición (c): «el volumen excede lo que un contexto puede sostener». Es la
        única de las tres que se puede MEDIR con lo que el corpus ya declara, y se mide: el
        volumen del paquete contra la capacidad de contexto que el perfil del rol exige, en
        la escala de cuatro escalones de `esquemas/perfil-agente.yaml`.
        """
        escala = len(self.politica.contextos)
        self.assertGreaterEqual(escala, 4, "la escala de contexto salió vacía del esquema")
        exceso = escala + 1

        # Un rol de un solo agente y un volumen que no cabe: no hay reparto que lo salve.
        with self.assertRaises(errores.VolumenExcedeElContexto) as capturado:
            equipos.materializar(
                "DIS", corpus=self.corpus, control_repo=self.repo,
                composiciones_verdaderas=["composicion:dis-gap-de-diseno"], slots=99,
                volumen=exceso)
        contexto = capturado.exception.contexto
        self.assertGreater(contexto["volumen"], contexto["capacidad"])
        self.assertGreater(contexto["necesarios"], 1)

        # Con reparto DECLARADO, el reparto tiene que traer al menos tantas unidades como
        # agentes hacen falta: repartir en dos lo que necesita tres sigue sin caber.
        with self.assertRaises(errores.VolumenExcedeElContexto):
            self.proyecto_nuevo(volumen=exceso, reparto_declarado={
                "DIS/investigacion-visual": {"territorios": ["marca"]}})

        # CONTROL: un volumen que cabe no levanta nada.
        cabe = equipos.materializar(
            "DIS", corpus=self.corpus, control_repo=self.repo,
            composiciones_verdaderas=["composicion:dis-gap-de-diseno"], slots=99, volumen=1)
        self.assertEqual(cabe["lectura_del_paquete"]["volumen"]["unidades"], 1)
        self.assertEqual(cabe["estado"], "materializado")

    # --------------------------------------------------------------- T257
    def test_257_slots_insuficientes_dejan_agentes_esperando_y_nunca_dos_en_uno(self):
        """T257 · Defecto que previene: contar un slot donde hay tres agentes.

        `b.11` calcula la concurrencia «a partir de agentes disponibles» y `C4` paso 6 deja
        fuera lo que no cabe SIN reducir la composición. Con un rol de tres agentes eso
        significa tres slots, y si sólo hay dos, uno de los tres espera —el rol NO se
        recorta a dos—. Y dos agentes en el mismo slot es error, no una casualidad.
        """
        holgado = self.proyecto_nuevo(slots=99)
        apretado = self.proyecto_nuevo(slots=3)
        self.assertEqual(apretado["slots_ocupados"], 3)
        self.assertTrue(apretado["esperando_capacidad"])
        # La composición NO se reduce: la unión de las listas es la misma con y sin holgura,
        # y cada AGENTE de un rol plural sigue estando, esperando o despachado.
        def censo(equipo):
            filas = equipo["roles"] + equipo["esperando_capacidad"] + equipo["bloqueados"]
            return sorted((f["rol"], (f.get("reparto") or {}).get("indice")) for f in filas)
        self.assertEqual(censo(apretado), censo(holgado))
        self.assertEqual(len(self.filas(apretado, "DIS/diseno-visual")), 3)
        for fila in apretado["esperando_capacidad"]:
            self.assertEqual(fila["estado"], "esperando-capacidad")
            self.assertIsNone(fila["slot"])
            self.assertTrue(fila["agente"], "esperar capacidad no es quedarse sin agente")

        # DOBLE OCUPACIÓN: dos agentes en el mismo `execution_slot` es error tipado.
        roto = json.loads(json.dumps(holgado))
        despachados = [u for u in roto["agentes"] if u["estado"] == "despachado"]
        self.assertGreater(len(despachados), 1)
        despachados[1]["slot"] = despachados[0]["slot"]
        with self.assertRaises(errores.AgenteSobreasignado):
            equipos.exigir_slots_coherentes(roto)
        # Y dos agentes del mismo rol sobre la MISMA unidad del reparto, también.
        otro = json.loads(json.dumps(holgado))
        filas = [f for f in otro["roles"] if f["rol"] == "DIS/diseno-visual"]
        filas[1]["reparto"]["indice"] = filas[0]["reparto"]["indice"]
        with self.assertRaises(errores.AgenteSobreasignado):
            equipos.exigir_slots_coherentes(otro)

    # --------------------------------------------------------------- T258
    def test_258_reanudar_no_puede_cambiar_el_reparto_en_silencio(self):
        """T258 · Defecto que previene: agentes trabajando sobre unidades que ya no existen.

        `C4` «Ampliación y reducción»: el equipo NO se rehace. Volver a materializar sobre un
        equipo ya escrito con un reparto distinto dejaría al agente del intento anterior
        produciendo sobre una dirección que nadie declara ya, y nadie se enteraría hasta tres
        pasos después. Y dos materializaciones del MISMO estado tienen que dar los mismos
        bytes: `I-g3`.
        """
        primero = self.proyecto_nuevo()
        # Reanudación idéntica: pasa, y produce el MISMO equipo byte a byte.
        segundo = self.proyecto_nuevo(equipo_previo=primero)
        self.assertEqual(json.dumps(primero, ensure_ascii=False, sort_keys=True),
                         json.dumps(segundo, ensure_ascii=False, sort_keys=True))
        self.assertEqual(primero["id"], segundo["id"])

        # Reanudación con OTRO reparto: error explícito, con los roles que cambian nombrados.
        with self.assertRaises(errores.RepartoIncoherente) as capturado:
            self.proyecto_nuevo(equipo_previo=primero, reparto_declarado={
                "DIS/diseno-visual": {"direcciones": ["calida", "sobria"]}})
        self.assertIn("DIS/diseno-visual", capturado.exception.contexto["roles"])

        # También si cambian las unidades sin cambiar el cardinal: tres direcciones OTRAS
        # son otro reparto, aunque sean tres.
        with self.assertRaises(errores.RepartoIncoherente):
            self.proyecto_nuevo(equipo_previo=primero, reparto_declarado={
                "DIS/diseno-visual": {"direcciones": ["uno", "dos", "tres"]}})

    # --------------------------------------------------------------- T259
    def test_259_un_cardinal_ilegible_falla_cerrado_y_nunca_vale_uno_por_omision(self):
        """T259 · Defecto que previene: «lo que no entiendo, que sea uno».

        El vocabulario del campo `agentes` es CERRADO y ENUMERADO. Una forma que el lector no
        conoce NO se materializa: suponer «1 por omisión» es exactamente cómo «2 o 3» acabó
        produciendo un agente. Y el sabotaje que cierra `E-01` —`agentes: "7 repartidos por
        artefacto, sin integrador"`, literalmente lo que `C4` llama prohibido— tiene que
        caer por SEMÁNTICA y no por una excusa léxica ni por la huella del kernel.
        """
        roles = ["DIS/diseno-visual", "DIS/direccion-artistica"]
        for ilegible in ("dos o tres", "unos cuantos", "1 o 2 repartidos por el aire",
                         "el mismo agente que nadie", "0", "3 o 2", "1, distinto del vecino",
                         "", "varios"):
            with self.assertRaises(errores.CardinalDeAgentesIlegible, msg=repr(ilegible)):
                equipos.leer_cardinal(ilegible, roles=roles)

        # Las VEINTIDÓS formas del corpus sí se leen, y el censo lo comprueba entero.
        self.assertTrue(equipos.exigir_censo_legible(self.corpus))
        # `1 por paquete; …` es paralelismo de PAQUETES y NO pluralidad de agentes.
        lectura = equipos.leer_cardinal(CON_PARALELISMO, roles=["CON/implementacion"])
        self.assertEqual((lectura["minimo"], lectura["maximo"]), (1, 1))
        self.assertEqual(lectura["modo"], equipos.MODO_PAQUETE)
        self.assertTrue(lectura["paralelismo_de_paquetes"])
        equipo_con = equipos.materializar(
            "CON", corpus=self.corpus, control_repo=self.repo,
            composiciones_verdaderas=["composicion:con-implementacion"], slots=99)
        self.assertEqual(self.plan(equipo_con, "CON/implementacion")["agentes"], 1)

        # EL SABOTAJE DE `E-01`, sobre una COPIA del corpus.
        base = tempfile.mkdtemp(prefix="ads-siete-agentes-")
        self.addCleanup(shutil.rmtree, base, True)
        copia = copiar_kernel(base)
        sustituir(os.path.join(copia, "capacidades", "DIS", "composicion.md"),
                  '  - rol: DIS/diseno-visual\n    obligatorio: true\n'
                  '    agentes: "2 o 3, uno por dirección explorada"',
                  '  - rol: DIS/diseno-visual\n    obligatorio: true\n'
                  '    agentes: "7 repartidos por artefacto, sin integrador"')
        mutado = ciclo.Corpus(copia)
        # Se LEE —el cardinal es 7 y el modo `artefacto`—, y por eso puede caer por la
        # prohibición que viola en vez de por no entenderse.
        lectura = equipos.leer_cardinal("7 repartidos por artefacto, sin integrador",
                                        roles=roles)
        self.assertEqual((lectura["minimo"], lectura["maximo"]), (7, 7))
        self.assertEqual(lectura["modo"], equipos.MODO_ARTEFACTO)
        self.assertTrue(lectura["integrador_negado"])
        with self.assertRaises(errores.VariosAgentesSinIntegrador) as capturado:
            equipos.materializar(
                "DIS", corpus=mutado, control_repo=self.repo,
                composiciones_verdaderas=["composicion:dis-proyecto-nuevo"], slots=99,
                reparto_declarado={
                    "DIS/investigacion-visual": {"territorios": ["marca", "producto"]},
                    "DIS/diseno-visual": {"artefactos": ["a" + str(i) for i in range(7)]}})
        self.assertEqual(capturado.exception.codigo, "VARIOS_AGENTES_SIN_INTEGRADOR")
        self.assertEqual(capturado.exception.contexto["agentes"], 7)


# =========================================================================
#  `E-06` · T260…T269 · `b.12` paso 5 y la detección de inanición
# =========================================================================
class SeleccionEInanicion(unittest.TestCase):
    """Un control repo real, un estado durable real y procesos reales."""

    def setUp(self):
        self.repo = tempfile.mkdtemp(prefix="ads-seleccion-")
        self.addCleanup(shutil.rmtree, self.repo, True)
        self.espacio = os.path.join(self.repo, "espacio")
        os.makedirs(self.espacio, exist_ok=True)

    def abrir(self, instancia="planificador-A"):
        registro = adaptadores.RegistroDeAdaptadores([
            adaptadores.AdaptadorDeProcesoLocal(self.espacio)])
        rt = paquete_runtime.Runtime(self.repo, instancia=instancia,
                                     registro_de_adaptadores=registro).abrir()
        self.addCleanup(rt.cerrar)
        return rt

    def alta(self, rt, paquetes, *, item="it-1"):
        if not self.existe(rt, "items/" + item + ".json"):
            rt.crear_item(id=item, titulo="trabajo de prueba", motivo="alta de la batería")
        for declarado in paquetes:
            rt.crear_paquete(
                id=declarado["id"], item=item,
                capacidades_requeridas=["proceso-local"], orden=dict(ORDEN_DE_PRUEBA),
                prioridad=declarado.get("prioridad", 50),
                depende_de=declarado.get("depende_de", []))

    def cola(self, rt):
        return {e["paquete"]: e for e in rt.elegibles()}

    def existe(self, rt, ruta_logica):
        """Si el objeto está en la revisión vigente. El motor NO devuelve `None`: falla.

        Es la forma correcta de preguntar y conviene decirla: `Almacen.leer` levanta
        `RutaInvalida` porque leer algo que no está es un error, no una ausencia con valor.
        Preguntar y capturar es explícito; el `None` de conveniencia sería la puerta por la
        que entra el estado inventado.
        """
        try:
            rt.almacen.leer(ruta_logica)
        except RutaInvalida:
            return False
        return True

    def durable(self, rt, paquete):
        return rt.almacen.leer("paquetes/" + paquete + ".json")

    # --------------------------------------------------------------- T260
    def test_260_criterio_a_la_prioridad_declarada_manda_sobre_todo_lo_demas(self):
        """T260 · Defecto que previene: que la prioridad del Owner deje de mandar.

        Es el PRIMER criterio de `b.12` paso 5 y el único que gobierna el Owner. Se monta la
        cola en su contra: el de prioridad baja desbloquea a dos y lleva más tiempo listo, y
        aun así el urgente va delante. Si alguien quita la prioridad de la clave de orden,
        gana el otro y esta prueba se pone roja.
        """
        rt = self.abrir()
        self.alta(rt, [
            {"id": "pq-fondo", "prioridad": 10},
            {"id": "pq-hijo-1", "prioridad": 10, "depende_de": ["pq-fondo"]},
            {"id": "pq-hijo-2", "prioridad": 10, "depende_de": ["pq-fondo"]},
            {"id": "pq-urgente", "prioridad": 90},
        ])
        orden = [e["paquete"] for e in rt.elegibles()]
        cola = self.cola(rt)
        # El de fondo gana en los otros dos criterios, y pierde por prioridad.
        self.assertEqual(cola["pq-fondo"]["grado_de_salida"], 2)
        self.assertEqual(cola["pq-urgente"]["grado_de_salida"], 0)
        self.assertGreater(cola["pq-fondo"]["tiempo_listo"],
                           cola["pq-urgente"]["tiempo_listo"])
        self.assertEqual(orden[0], "pq-urgente",
                         "la prioridad declarada dejó de ser el primer criterio")

    # --------------------------------------------------------------- T261
    def test_261_criterio_b_desbloquear_a_mas_paquetes_decide_entre_iguales(self):
        """T261 · Defecto que previene: dejar la cola parada detrás de lo que no libera nada.

        `b.12` paso 5 (b): «desbloquea a más paquetes (grado de salida en el grafo)». El
        grafo es `depende_de`, y el grado de salida sólo cuenta dependientes VIVOS: liberar a
        un paquete cancelado no libera a nadie. Se monta la cola EN CONTRA del que desbloquea:
        `pq-zzz-raiz` entra DESPUÉS —así lleva menos tiempo listo— y su identificador ordena
        el último, de modo que pierde en los criterios (c) y (d) y sólo (b) puede ponerlo
        delante. Al cancelar a sus dos dependientes su grado cae a cero y el turno vuelve al
        otro, que es lo que demuestra que el grado se cuenta sobre dependientes VIVOS.
        """
        rt = self.abrir()
        self.alta(rt, [
            {"id": "pq-aaa-suelto"},
            {"id": "pq-zzz-raiz"},
            {"id": "pq-hijo-1", "depende_de": ["pq-zzz-raiz"]},
            {"id": "pq-hijo-2", "depende_de": ["pq-zzz-raiz"]},
        ])
        cola = self.cola(rt)
        self.assertEqual(cola["pq-zzz-raiz"]["grado_de_salida"], 2)
        self.assertEqual(sorted(cola["pq-zzz-raiz"]["desbloquea"]),
                         ["pq-hijo-1", "pq-hijo-2"])
        self.assertEqual(cola["pq-aaa-suelto"]["grado_de_salida"], 0)
        self.assertGreater(cola["pq-aaa-suelto"]["tiempo_listo"],
                           cola["pq-zzz-raiz"]["tiempo_listo"],
                           "el que desbloquea tiene que ir en desventaja en (c) y en (d), o "
                           "esta prueba no mide (b)")
        self.assertEqual([e["paquete"] for e in rt.elegibles()][0], "pq-zzz-raiz",
                         "el grado de salida no está decidiendo: el que libera media cola "
                         "espera detrás del que no libera nada")

        # Y un dependiente CANCELADO deja de contar: el grado baja, y con él el turno.
        rt.cancelar("pq-hijo-1", motivo="ya no hace falta", autoridad="Owner")
        rt.cancelar("pq-hijo-2", motivo="ya no hace falta", autoridad="Owner")
        cola = self.cola(rt)
        self.assertEqual(cola["pq-zzz-raiz"]["grado_de_salida"], 0)
        self.assertEqual([e["paquete"] for e in rt.elegibles()][0], "pq-aaa-suelto")

    # --------------------------------------------------------------- T262
    def test_262_criterio_c_la_antiguedad_saca_de_la_cola_al_que_lleva_mas_esperando(self):
        """T262 · Defecto que previene: la inanición, medida — y sin tocar la prioridad.

        `b.12` es terminante: «DSP informa de la inanición. No cambia la prioridad. Nunca».
        La prevención tiene que salir del criterio (c), que es para lo que está. Se construye
        la inanición exacta que (c) impide: un paquete cuyo identificador ordena AL FINAL, y
        una corriente de paquetes nuevos de su misma prioridad cuyos identificadores ordenan
        antes. Sin (c), el veterano queda detrás de CADA nuevo y no se ejecuta nunca; con
        (c), sale el primero y TERMINA. Y su `prioridad` durable es la misma al final que al
        principio: nadie se la ha tocado.
        """
        rt = self.abrir()
        self.alta(rt, [{"id": "pq-zzz-veterano", "prioridad": 10}])
        prioridad_inicial = self.durable(rt, "pq-zzz-veterano")["prioridad"]

        # Cinco rondas: entra un competidor nuevo con el MISMO fondo de prioridad y un
        # identificador que ordena antes, y se despacha UNO por pasada.
        for ronda in range(5):
            self.alta(rt, [{"id": "pq-aaa-" + str(ronda), "prioridad": 10}])
            cola = rt.elegibles()
            self.assertEqual(
                cola[0]["paquete"], "pq-zzz-veterano",
                "el veterano dejó de ir primero en la ronda " + str(ronda) + ": sin el "
                "criterio (c) cada paquete nuevo lo adelanta, para siempre")
            self.assertGreater(cola[0]["tiempo_listo"], cola[1]["tiempo_listo"])
            ultima_ronda = ronda
        self.assertEqual(ultima_ronda, 4, "las cinco rondas no se ejecutaron")

        # Y TERMINA: se despacha de verdad, con un proceso real.
        resumen = rt.despachar("pq-zzz-veterano")
        self.assertEqual(resumen["desenlace"], "completado")
        final = self.durable(rt, "pq-zzz-veterano")
        self.assertEqual(final["estado"], "completado")
        self.assertEqual(final["prioridad"], prioridad_inicial,
                         "alguien le subió la prioridad para sacarlo: `b.12` lo prohíbe con "
                         "todas las letras")
        self.assertEqual(final["prioridad"], 10)

    # --------------------------------------------------------------- T263
    def test_263_criterio_d_el_identificador_hace_TOTAL_el_orden(self):
        """T263 · Defecto que previene: dejar el desempate al orden del sistema de ficheros.

        `gate:despacho-coherente`: «mismo estado produce misma selección, con desempate por
        identificador». Los tres primeros criterios PUEDEN empatar; el cuarto no empata
        nunca. Sin él, dos entradas producen la MISMA clave y el orden lo decide la
        estabilidad del `sort`, es decir el orden en que se leyó el directorio: dos
        instancias podrían ver colas distintas.
        """
        empatados = [
            {"paquete": "pq-b", "prioridad": 50, "grado_de_salida": 1, "tiempo_listo": 7},
            {"paquete": "pq-a", "prioridad": 50, "grado_de_salida": 1, "tiempo_listo": 7},
        ]
        claves = [politica_de_seleccion.clave_de_orden(e) for e in empatados]
        self.assertEqual(len(set(claves)), 2,
                         "dos paquetes empatados en los tres primeros criterios producen la "
                         "MISMA clave: el orden deja de ser total y de ser determinista")
        self.assertEqual([e["paquete"] for e in sorted(empatados,
                                                       key=politica_de_seleccion.clave_de_orden)],
                         ["pq-a", "pq-b"])

        # Y sobre el estado real: la cola es exactamente la ordenada por la clave, y dos
        # lecturas seguidas dan los mismos bytes.
        rt = self.abrir()
        self.alta(rt, [{"id": "pq-0001"}, {"id": "pq-0002"}, {"id": "pq-0003"}])
        primera = rt.elegibles()
        segunda = rt.elegibles()
        self.assertEqual(json.dumps(primera, sort_keys=True),
                         json.dumps(segunda, sort_keys=True))
        self.assertEqual(primera,
                         sorted(primera, key=politica_de_seleccion.clave_de_orden))
        self.assertEqual(len({politica_de_seleccion.clave_de_orden(e) for e in primera}),
                         len(primera))

    # --------------------------------------------------------------- T264
    def test_264_las_postergaciones_se_CUENTAN_pasada_a_pasada_y_son_durables(self):
        """T264 · Defecto que previene: un campo de inanición que nadie incrementa.

        `b.12`: «postergaciones · cuántas veces fue postergado en el paso 5». Se despacha de
        uno en uno y se comprueba que el que espera SUBE, el que se lleva el turno NO, y que
        la cuenta está en el objeto durable y no en la memoria de nadie.
        """
        rt = self.abrir()
        self.alta(rt, [{"id": "pq-elegido", "prioridad": 90},
                       {"id": "pq-espera-1"}, {"id": "pq-espera-2"}])
        for _ in range(3):
            rt.seleccionar_siguiente(cabida=1)
        self.assertEqual(self.durable(rt, "pq-espera-1")["seleccion"]["postergaciones"], 3)
        self.assertEqual(self.durable(rt, "pq-espera-2")["seleccion"]["postergaciones"], 3)
        self.assertEqual(self.durable(rt, "pq-elegido")["seleccion"]["postergaciones"], 0,
                         "el que se llevó el turno no fue postergado por nadie")
        cola = self.cola(rt)
        self.assertEqual(cola["pq-espera-1"]["postergaciones"], 3)

        # Y con cabida para dos, sólo el tercero se posterga.
        rt.seleccionar_siguiente(cabida=2)
        self.assertEqual(self.durable(rt, "pq-espera-1")["seleccion"]["postergaciones"], 3)
        self.assertEqual(self.durable(rt, "pq-espera-2")["seleccion"]["postergaciones"], 4)

    # --------------------------------------------------------------- T265
    def test_265_adelantado_por_dice_QUIEN_le_paso_por_delante(self):
        """T265 · Defecto que previene: saber que un paquete espera y no saber por culpa de quién.

        `b.12`: «adelantado_por · qué items lo adelantaron». Sin este campo, la inanición se
        ve pero no se explica, y `b.12` paso 7 exige explicar. Se comprueba que se puebla con
        quien REALMENTE se llevó el turno, que no se repite y que es un conjunto ordenado
        —`I-g3`: dos ejecuciones del mismo escenario escriben los mismos bytes—.
        """
        rt = self.abrir()
        self.alta(rt, [{"id": "pq-primero", "prioridad": 90},
                       {"id": "pq-segundo", "prioridad": 70},
                       {"id": "pq-ultimo", "prioridad": 10}])
        rt.seleccionar_siguiente(cabida=1)
        self.assertEqual(self.durable(rt, "pq-ultimo")["seleccion"]["adelantado_por"],
                         ["pq-primero"])
        rt.despachar("pq-primero")
        rt.seleccionar_siguiente(cabida=1)
        self.assertEqual(self.durable(rt, "pq-ultimo")["seleccion"]["adelantado_por"],
                         ["pq-primero", "pq-segundo"])
        # Repetir la misma pasada NO duplica: es un conjunto, y está ordenado.
        rt.seleccionar_siguiente(cabida=1)
        adelantado = self.durable(rt, "pq-ultimo")["seleccion"]["adelantado_por"]
        self.assertEqual(adelantado, ["pq-primero", "pq-segundo"])
        self.assertEqual(adelantado, sorted(set(adelantado)))
        self.assertEqual(self.durable(rt, "pq-primero")["seleccion"]["adelantado_por"], [])

    # --------------------------------------------------------------- T266
    def test_266_el_impedimento_nombra_el_criterio_que_de_verdad_decidio(self):
        """T266 · Defecto que previene: «espera» como explicación de por qué espera.

        `b.12`: «impedimento · qué recurso, límite o condición lo impide», y paso 7: «un
        dispatcher que elige sin explicar es una caja negra». El motivo se DERIVA comparando
        criterio a criterio contra el que se llevó el turno y se para en el PRIMERO que
        decide, de modo que cada uno de los cuatro produce un texto DISTINTO. Aquí se
        comprueban los cuatro.
        """
        rt = self.abrir()
        self.alta(rt, [
            {"id": "pq-cabeza", "prioridad": 90},
            {"id": "pq-por-prioridad", "prioridad": 10},
        ])
        rt.seleccionar_siguiente(cabida=1)
        self.assertIn("prioridad declarada",
                      self.durable(rt, "pq-por-prioridad")["seleccion"]["impedimento"])

        # Los otros tres se miden sobre la función pura, que es donde vive la derivación.
        cabeza = {"paquete": "pq-cabeza", "prioridad": 50, "grado_de_salida": 3,
                  "tiempo_listo": 9}
        casos = {
            "grado de salida": {"paquete": "pq-x", "prioridad": 50, "grado_de_salida": 0,
                                "tiempo_listo": 9},
            "antigüedad de espera": {"paquete": "pq-y", "prioridad": 50,
                                     "grado_de_salida": 3, "tiempo_listo": 1},
            "manda el identificador": {"paquete": "pq-z", "prioridad": 50,
                                       "grado_de_salida": 3, "tiempo_listo": 9},
        }
        textos = set()
        for esperado, entrada in casos.items():
            motivo = politica_de_seleccion.motivo_de_postergacion(entrada, cabeza)
            self.assertIn(esperado, motivo)
            textos.add(motivo)
        self.assertEqual(len(textos), 3, "dos criterios distintos producen el mismo motivo: "
                                         "desde fuera son indistinguibles")
        self.assertEqual(politica_de_seleccion.motivo_de_postergacion(cabeza, cabeza), "",
                         "el que se lleva el turno no tiene impedimento")

        # Y la vista del `§7.5` lo MUESTRA, que es lo que `b.12` pide: «mantiene y muestra».
        esperando = rt.vistas()["que_lleva_esperando"]
        self.assertTrue(esperando)
        fila = [f for f in esperando if f["paquete"] == "pq-por-prioridad"][0]
        for campo in ("tiempo_listo", "postergaciones", "adelantado_por", "impedimento"):
            self.assertIn(campo, fila)
        self.assertIn("prioridad declarada", fila["impedimento"])

    # --------------------------------------------------------------- T267
    def test_267_la_antiguedad_se_mide_con_el_reloj_LOGICO_y_no_con_el_de_pared(self):
        """T267 · Defecto que previene: meter la hora de pared en el estado canónico.

        `a.9` lo prohíbe y `registro_pruebas.py` lo repite: un estado con `time.time()` deja
        de ser reproducible. `tiempo_listo` es una RESTA de revisiones, que es el orden en
        que los sucesos ocurrieron de verdad. Se comprueba que lo durable guarda un entero
        monótono, que crece SÓLO cuando el estado avanza, y que en el objeto escrito no hay
        ninguna marca de tiempo real.
        """
        rt = self.abrir()
        self.alta(rt, [{"id": "pq-medido"}])
        durable = self.durable(rt, "pq-medido")
        listo_en = durable["seleccion"]["listo_en"]
        self.assertIsInstance(listo_en, int)
        self.assertGreater(listo_en, 0)
        self.assertLessEqual(listo_en, rt.almacen.revision()["revision"])

        # Nada que se parezca a una hora de pared en el paquete durable.
        texto = json.dumps(durable, ensure_ascii=False)
        self.assertNotRegex(texto, r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}")
        self.assertNotRegex(texto, r"\b1[6-9]\d{8}\b")

        # La antigüedad NO cambia si el estado no avanza, y cambia cuando avanza.
        antes = self.cola(rt)["pq-medido"]["tiempo_listo"]
        self.assertEqual(self.cola(rt)["pq-medido"]["tiempo_listo"], antes)
        self.alta(rt, [{"id": "pq-otro"}])
        despues = self.cola(rt)["pq-medido"]["tiempo_listo"]
        self.assertGreater(despues, antes,
                           "la antigüedad no avanza con las revisiones: `tiempo_listo` no "
                           "se está midiendo con el reloj lógico")
        # Y volver a `listo` reinicia la espera: es una espera nueva, no la anterior.
        rt.pausar("pq-otro", motivo="prueba", autoridad="Owner")
        rt.reanudar("pq-otro", motivo="prueba", autoridad="Owner")
        self.assertGreater(self.durable(rt, "pq-otro")["seleccion"]["listo_en"], listo_en)

    # --------------------------------------------------------------- T268
    def test_268_los_contadores_sobreviven_a_la_caida_y_a_dos_planificadores(self):
        """T268 · Defecto que previene: perder la evidencia de inanición justo al reiniciar.

        Un contador en memoria se borra con el proceso, y un paquete que lleva cuarenta
        postergaciones es EXACTAMENTE lo que hay que ver después de un reinicio. Aquí el
        estado se escribe en un proceso, el proceso MUERE, y otro proceso distinto lee lo que
        el primero contó. Y después dos planificadores sobre el mismo estado: ninguno puede
        corromper la cuenta ni ver una cola incompatible con la del otro.
        """
        rt = self.abrir()
        self.alta(rt, [{"id": "pq-cabeza", "prioridad": 90}, {"id": "pq-cola"}])
        rt.seleccionar_siguiente(cabida=1)
        rt.seleccionar_siguiente(cabida=1)
        self.assertEqual(self.durable(rt, "pq-cola")["seleccion"]["postergaciones"], 2)
        rt.cerrar()

        # OTRO PROCESO, de verdad: lee el estado que dejó el anterior.
        guion = (
            "import json, os, sys\n"
            "sys.path.insert(0, " + repr(RUNTIME) + ")\n"
            "import adaptadores, runtime as pr\n"
            "reg = adaptadores.RegistroDeAdaptadores(["
            "adaptadores.AdaptadorDeProcesoLocal(" + repr(self.espacio) + ")])\n"
            "rt = pr.Runtime(" + repr(self.repo) + ", instancia='reanudado',"
            " registro_de_adaptadores=reg).abrir()\n"
            "cola = {e['paquete']: e for e in rt.elegibles()}\n"
            "rt.seleccionar_siguiente(cabida=1)\n"
            "despues = rt.almacen.leer('paquetes/pq-cola.json')['seleccion']\n"
            "rt.cerrar()\n"
            "print(json.dumps({'antes': cola['pq-cola']['postergaciones'],"
            " 'despues': despues['postergaciones'],"
            " 'adelantado_por': despues['adelantado_por']}))\n"
        )
        proceso = subprocess.run([sys.executable, "-c", guion], capture_output=True,
                                 text=True, timeout=SEGUNDOS_DE_ESPERA)
        self.assertEqual(proceso.returncode, 0, proceso.stderr[-2000:])
        leido = json.loads(proceso.stdout)
        self.assertEqual(leido["antes"], 2,
                         "el proceso nuevo no ve lo que contó el anterior: la cuenta estaba "
                         "en memoria y no en el estado durable")
        self.assertEqual(leido["despues"], 3, "la cuenta no continúa tras la reanudación")
        self.assertEqual(leido["adelantado_por"], ["pq-cabeza"])

        # DOS PLANIFICADORES sobre el mismo estado, a la vez.
        uno = self.abrir(instancia="planificador-uno")
        dos = self.abrir(instancia="planificador-dos")
        self.assertEqual([e["paquete"] for e in uno.elegibles()],
                         [e["paquete"] for e in dos.elegibles()],
                         "dos planificadores ven colas distintas: la carrera dejaría de ser "
                         "una propiedad y sería un accidente")
        antes = self.durable(uno, "pq-cola")["seleccion"]["postergaciones"]
        uno.seleccionar_siguiente(cabida=1)
        dos.seleccionar_siguiente(cabida=1)
        despues = self.durable(uno, "pq-cola")["seleccion"]["postergaciones"]
        self.assertEqual(despues, antes + 2,
                         "dos pasadas concurrentes no dejaron exactamente dos "
                         "postergaciones: una se perdió o se contó dos veces")
        # Y el objeto durable sigue siendo válido para el vocabulario cerrado del §3.
        modelo.comprobar_paquete(self.durable(uno, "pq-cola"), "paquetes/pq-cola.json")

    # --------------------------------------------------------------- T269
    SABOTAJES = (
        # (título, fichero bajo `runtime/`, texto que se sustituye, sustituto, prueba roja)
        (
            "`b.12` paso 5 (a): la prioridad declarada sale de la clave de orden",
            "runtime/politica.py",
            "    return (-int(entrada[\"prioridad\"]),",
            "    return (0 * int(entrada[\"prioridad\"]),",
            "SeleccionEInanicion.test_260_criterio_a_la_prioridad_declarada_manda_sobre_todo_lo_demas",
        ),
        (
            "`b.12` paso 5 (b): el grado de salida en el grafo sale de la clave",
            "runtime/politica.py",
            "            -int(entrada[\"grado_de_salida\"]),",
            "            0 * int(entrada[\"grado_de_salida\"]),",
            "SeleccionEInanicion.test_261_criterio_b_desbloquear_a_mas_paquetes_decide_entre_iguales",
        ),
        (
            "`b.12` paso 5 (c): la antigüedad de espera sale de la clave, y vuelve la "
            "inanición que el criterio existe para impedir",
            "runtime/politica.py",
            "            -int(entrada[\"tiempo_listo\"]),",
            "            0 * int(entrada[\"tiempo_listo\"]),",
            "SeleccionEInanicion.test_262_criterio_c_la_antiguedad_saca_de_la_cola_al_que_lleva_mas_esperando",
        ),
        (
            "`b.12` paso 5 (d): el identificador deja de desempatar y el orden deja de ser total",
            "runtime/politica.py",
            "            str(entrada[\"paquete\"]))",
            "            str(entrada[\"prioridad\"]))",
            "SeleccionEInanicion.test_263_criterio_d_el_identificador_hace_TOTAL_el_orden",
        ),
        (
            "`b.12` inanición: `postergaciones` deja de contarse",
            "runtime/dispatcher.py",
            "seleccion[\"postergaciones\"] = int(seleccion[\"postergaciones\"]) + 1",
            "seleccion[\"postergaciones\"] = int(seleccion[\"postergaciones\"])",
            "SeleccionEInanicion.test_264_las_postergaciones_se_CUENTAN_pasada_a_pasada_y_son_durables",
        ),
        (
            "`b.12` inanición: `adelantado_por` deja de decir quién adelantó",
            "runtime/dispatcher.py",
            "                seleccion[\"adelantado_por\"] = sorted(\n"
            "                    set(seleccion[\"adelantado_por\"]) | set(frente))",
            "                seleccion[\"adelantado_por\"] = sorted(\n"
            "                    set(seleccion[\"adelantado_por\"]))",
            "SeleccionEInanicion.test_265_adelantado_por_dice_QUIEN_le_paso_por_delante",
        ),
        (
            "`b.12` inanición: `impedimento` deja de nombrar el criterio que decidió",
            "runtime/dispatcher.py",
            "                seleccion[\"impedimento\"] = politica.motivo_de_postergacion(\n"
            "                    entrada, cabeza)",
            "                seleccion[\"impedimento\"] = \"\"",
            "SeleccionEInanicion.test_266_el_impedimento_nombra_el_criterio_que_de_verdad_decidio",
        ),
        (
            "`b.12` inanición: `tiempo_listo` deja de anclarse al reloj lógico",
            "runtime/dispatcher.py",
            "                listo_en=revision[\"revision\"] + 1,",
            "                listo_en=None,",
            "SeleccionEInanicion.test_267_la_antiguedad_se_mide_con_el_reloj_LOGICO_y_no_con_el_de_pared",
        ),
        (
            "`C4`: el reparto deja de REPLICARSE y tres agentes vuelven a ser uno",
            "ciclo/equipos.py",
            "    if plan is None or int(plan.get(\"agentes\") or 1) <= 1:",
            "    if True:",
            "Cardinalidad.test_250_el_cardinal_se_DERIVA_del_corpus_y_hay_tantos_agentes_como_dice",
        ),
        (
            "`C4` condición (a): repartir sin unidades declaradas deja de fallar cerrado",
            "ciclo/equipos.py",
            "        if not unidades:\n            raise RepartoSinUnidades(",
            "        if not unidades:\n            return 1, [\"por omisión\"], None, \"\"\n"
            "        if False:\n            raise RepartoSinUnidades(",
            "Cardinalidad.test_252_reparto_por_territorio_SIN_territorios_falla_cerrado",
        ),
        (
            "`C4` paso 6: el corte por límites vuelve a contar UN slot por rol y no por agente",
            "ciclo/equipos.py",
            "        if ocupados < slots:",
            "        if ocupados < slots or len(unidad.get(\"roles\") or []) >= 1:",
            "Cardinalidad.test_257_slots_insuficientes_dejan_agentes_esperando_y_nunca_dos_en_uno",
        ),
    )

    def test_269_cada_sabotaje_pone_roja_una_prueba_DISTINTA(self):
        """T269 · Defecto que previene: un criterio decorativo que nadie echaría de menos.

        La lección de método de los dos cortes anteriores: una regla que se puede BORRAR
        entera sin que ninguna prueba parpadee no está probada, está descrita. Aquí se
        sabotean, en una COPIA del árbol y en PROCESOS REALES, los CUATRO criterios de orden
        de `b.12` paso 5, los CUATRO campos de inanición y TRES piezas de la cardinalidad de
        `C4`, uno por uno, y se exige que cada uno ponga roja una prueba DISTINTA de esta
        batería. Que las pruebas rojas sean once distintas es lo que demuestra que ningún
        criterio queda decorativo.

        El control positivo va primero: la copia SIN sabotear tiene que pasar en verde. Sin
        él, un rojo podría venir de que la copia esté rota y no de que falte la regla.
        """
        base = tempfile.mkdtemp(prefix="ads-sabotaje-seleccion-")
        self.addCleanup(shutil.rmtree, base, True)
        copia = copiar_kernel(base)
        prueba = os.path.join(copia, "runtime", "pruebas",
                              "test_cardinalidad_y_seleccion.py")
        entorno = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}

        def correr(nombre):
            return subprocess.run([sys.executable, prueba, nombre], cwd=base,
                                  capture_output=True, text=True,
                                  timeout=SEGUNDOS_DE_ESPERA, env=entorno)

        casos = sorted({s[4] for s in self.SABOTAJES})
        self.assertEqual(len(casos), len(self.SABOTAJES),
                         "dos sabotajes apuntan a la misma prueba: uno de los dos no está "
                         "demostrando nada propio")
        for caso in casos:
            verde = correr(caso)
            self.assertEqual(verde.returncode, 0,
                             "la copia SIN sabotear ya falla en " + caso + ": "
                             + verde.stderr[-2000:])
            self.assertIn("Ran 1 test", verde.stderr, caso)

        for titulo, fichero, viejo, nuevo, caso in self.SABOTAJES:
            ruta = os.path.join(copia, "runtime", fichero)
            with open(ruta, encoding="utf-8") as manejador:
                original = manejador.read()
            self.assertIn(viejo, original,
                          "el sabotaje «" + titulo + "» no encuentra qué romper: sería un "
                          "no-op y la prueba pasaría sin haber atacado nada")
            self.assertNotEqual(viejo, nuevo, titulo)
            try:
                with open(ruta, "w", encoding="utf-8") as manejador:
                    manejador.write(original.replace(viejo, nuevo, 1))
                roja = correr(caso)
                self.assertNotEqual(
                    roja.returncode, 0,
                    "SABOTAJE NO DETECTADO · " + titulo + " · " + caso + " siguió VERDE "
                    "con la regla rota: la propiedad es decorativa")
            finally:
                with open(ruta, "w", encoding="utf-8") as manejador:
                    manejador.write(original)
            # RESTAURADA: vuelve a verde, o el rojo anterior no probaba nada del sabotaje.
            self.assertEqual(correr(caso).returncode, 0,
                             "la copia restaurada no vuelve a verde en " + caso)


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de `test_ciclo.py`, no importado: una batería no puede depender de otra para
    poder ejecutarse. La salida se PUBLICA como evidencia, y «Ran 20 tests in 12.481s»
    cambia en cada ejecución y ensuciaría el árbol en cada comprobación.
    """

    def run(self, test):
        import io as _io
        buffer = _io.StringIO()
        real, self.stream = self.stream, unittest.runner._WritelnDecorator(buffer)
        try:
            resultado = super().run(test)
        finally:
            self.stream = real
        real.write(re.sub(r"Ran (\d+) tests? in [\d.]+s",
                          r"Ran \1 tests  (duración no registrada: varía por ejecución)",
                          buffer.getvalue()))
        return resultado


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
