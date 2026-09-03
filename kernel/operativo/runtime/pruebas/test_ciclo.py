#!/usr/bin/env python3
"""test_ciclo — la batería del CICLO COMPLETO de `§7.2` (`F6`, macrobloque 3, agente A).

Instancia el `CONTRATO-CICLO-Y-MACROCIRCUITOS.md`, que a su vez instancia el `§7.2` y el
`§8.0` de `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, `b.16` en
`kernel/operativo/recorrido/01-PROCESOS.md`, `C4`, `C5` y la taxonomía de entrada.

CUATRO REGLAS QUE ESTA BATERÍA SE IMPONE, Y POR QUÉ:

  1. NINGUNA PRUEBA SE LIMITA A MIRAR. Ni un caso comprueba que un fichero existe o que un
     texto dice algo y se da por satisfecho. Todos mueven el ciclo sobre un control repo
     real y sobre el corpus real del kernel. Una batería que lee el árbol en vez de moverlo
     demuestra que alguien escribió los ficheros, no que la ruta se componga.

  2. LO QUE SE PRUEBA ES QUE NADA SE DECIDE POR TEXTO LIBRE. Hay dos pruebas simétricas y
     son el eje de `T196`: renombrar el título de un item NO cambia su ruta, y un sinónimo
     en la expresión literal del Owner NO activa ninguna capacidad. Si alguna vez alguien
     mete una regla léxica, esas dos fallan.

  3. EL ANALIZADOR YAML SE CONTRASTA CONTRA PyYAML SOBRE EL CORPUS REAL. El kernel es
     stdlib pura y por eso el analizador es propio; que sea equivalente no se promete, se
     mide, bloque a bloque sobre los doscientos y pico bloques canónicos. Cuando PyYAML no
     está instalado la prueba lo dice y comprueba las invariantes estructurales, que es
     todo lo que se puede comprobar sin él.

  4. LAS PROHIBICIONES SE PRUEBAN POR SU MECANISMO, NO POR SU TEXTO. Un gate que no puede
     escribir norma se prueba intentando que la escriba; un método que no es una capacidad
     se prueba pasándolo donde va una capacidad; una condición vaga se prueba escribiéndola.

Y una quinta, de forma: la salida se PUBLICA como evidencia, así que el resumen de
`unittest` no lleva duración (`_RunnerDeterminista`, COPIADO de `test_runtime.py`, no
importado) y todo fichero que se abre se cierra.

    python3 kernel/operativo/runtime/pruebas/test_ciclo.py

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
CLI = os.path.join(RUNTIME, "ads_ciclo.py")
sys.path.insert(0, RUNTIME)

try:
    import adaptadores
    import ciclo
    import runtime as paquete_runtime
    from ciclo import corpus as modulo_corpus, equipos, gates, handoffs, procesos, rutas
except ImportError as exc:      # el paquete todavía no está: que se vea por qué
    print(f"no se encuentra el paquete `ciclo` bajo {RUNTIME}: {exc}", file=sys.stderr)
    raise

SEGUNDOS_DE_ESPERA = 180

# Las QUINCE capacidades y las CUATRO vías, transcritas del `§18` y del `§8.0` para
# CONFRONTAR el dato del paquete, no para sustituirlo.
QUINCE = ("APR", "ARQ", "CON", "DIS", "DOM", "DSP", "ENC", "ENT", "INV", "PLT", "PRD",
          "SEG", "SIS", "USO", "VER")
CUATRO_VIAS = (1, 2, 3, 4)
TRES_PRESENCIAS = ("autoridad", "ejecutor", "encuadre")
DIEZ_PROCESOS = ("proceso:AUD", "proceso:DEF", "proceso:DEP", "proceso:DEU", "proceso:DIR",
                 "proceso:FEA", "proceso:GAP", "proceso:INC", "proceso:INV", "proceso:SIS")


def entrada_base(**cambios):
    """Una entrada del Owner completa y clasificable. Los casos la mutan."""
    base = {
        "clase": "candidato",
        "expresion_literal": "no se puede exportar la tabla",
        "canal": "chat",
        "fecha": "2026-09-03",
        "resultado_perseguido": "el usuario descarga la tabla completa en formato CSV",
        "evidencia_de_cierre": ["un CSV con las mismas filas que muestra la vista"],
        "anclaje_terminado": True,
        "materia": "capacidad-ausente",
        "estado_del_objeto": "no-existe",
    }
    base.update(cambios)
    return base


class BaseDelCiclo(unittest.TestCase):
    """Un control repo real por prueba, y el corpus real del kernel."""

    @classmethod
    def setUpClass(cls):
        cls.corpus = ciclo.Corpus(KERNEL)

    def setUp(self):
        self.repo = tempfile.mkdtemp(prefix="ads-ciclo-")
        self.espacio = os.path.join(self.repo, "espacio")
        os.makedirs(self.espacio, exist_ok=True)
        self.addCleanup(shutil.rmtree, self.repo, True)

    def abrir_runtime(self, instancia="ciclo-A"):
        registro = adaptadores.RegistroDeAdaptadores([
            adaptadores.AdaptadorDeProcesoLocal(self.espacio),
        ])
        rt = paquete_runtime.Runtime(
            self.repo, instancia=instancia, registro_de_adaptadores=registro,
        ).abrir()
        self.addCleanup(rt.cerrar)
        return rt

    def orden(self, capacidades):
        return {
            capacidad: {
                "adaptador": "proceso-local", "operacion": "ejecutar",
                "argumentos": ["/bin/sh", "-c", "exit 0"], "limite_segundos": 30,
            }
            for capacidad in capacidades
        }

    def plan_completo(self, rt, *, condiciones=(), entrada=None):
        marco = ciclo.encuadrar(self.repo, entrada or entrada_base(), corpus=self.corpus)
        ruta = ciclo.componer(marco, corpus=self.corpus, fase="unica",
                              condiciones_verdaderas=condiciones)
        capacidades = sorted({p["capacidad"] for p in ruta["participantes"]})
        planificador = ciclo.Planificador(rt, corpus=self.corpus)
        plan = planificador.planificar(
            marco, ruta, orden_por_capacidad=self.orden(capacidades),
        )
        return marco, ruta, plan


# =========================================================================
# T195 · encuadre y taxonomía de entrada
# =========================================================================
class Encuadre(BaseDelCiclo):

    def test_01_las_nueve_clases_y_solo_tres_crean_trabajo(self):
        """T195 · Defecto que previene: convertir cada comentario del Owner en un item.

        Las nueve clases se DERIVAN del corpus y las tres que crean trabajo se derivan de
        su campo `crea_item`, no de una lista escrita aquí. La regla 2 de la taxonomía dice
        «salvo las tres que lo declaran explícitamente», y «lo declaran» es literal.
        """
        catalogo = ciclo.Corpus(KERNEL).entradas()
        self.assertEqual(len(catalogo), 9, sorted(catalogo))
        crean = ciclo.clases_que_crean_trabajo(self.corpus)
        self.assertEqual(len(crean), 3, crean)
        self.assertEqual(
            set(crean), {"entrada:candidato", "entrada:decision", "entrada:item"},
        )
        for identificador in sorted(set(catalogo) - set(crean)):
            marco = ciclo.encuadrar(
                self.repo, entrada_base(clase=identificador), corpus=self.corpus,
            )
            self.assertFalse(marco["crea_trabajo"], identificador)
            self.assertIsNone(marco["proceso"], identificador)
            with self.assertRaises(ciclo.EntradaSinTrabajo):
                ciclo.encuadre.exigir_que_crea_trabajo(marco)

    def test_02_la_frontera_idea_inmadura_candidato_es_la_prueba_escrita(self):
        """T195 · Defecto que previene: llenar la cola con ideas que nadie sabe cerrar.

        Las TRES casillas de `01-TAXONOMIA.md`. Falla cualquiera → IDEA INMADURA, y lo que
        falla es exactamente lo que hay que madurar: se comprueba que el encuadre lo diga.
        """
        casos = [
            ({"resultado_perseguido": ""}, "RESULTADO PERSEGUIDO"),
            ({"resultado_perseguido": "mejorar"}, "único verbo"),
            ({"evidencia_de_cierre": []}, "EVIDENCIA DE CIERRE"),
            ({"anclaje_terminado": False}, "ANCLAJE"),
        ]
        for mutacion, esperado in casos:
            marco = ciclo.encuadrar(
                self.repo, entrada_base(**mutacion), corpus=self.corpus,
            )
            self.assertEqual(marco["clase"], "entrada:idea-inmadura", mutacion)
            self.assertFalse(marco["crea_trabajo"], mutacion)
            self.assertTrue(
                any(esperado in falta for falta in marco["lo_que_falta_para_madurar"]),
                (mutacion, marco["lo_que_falta_para_madurar"]),
            )

    def test_03_el_encuadre_descubre_fuentes_y_no_copia_ningun_remoto(self):
        """T195 · Defecto que previene: una credencial del manifiesto en el estado durable.

        `SOURCES.toml` declara identidad Git; el encuadre guarda `id` y `path` y jamás el
        remoto. Se pone un remoto con credencial y se comprueba que no aparece en NINGÚN
        byte del encuadre.
        """
        with open(os.path.join(self.repo, "SOURCES.toml"), "w", encoding="utf-8") as fichero:
            fichero.write(
                'schema = 1\n[workspace]\nlayout = "siblings"\n\n'
                '[[sources]]\nid = "frontend"\n'
                'remote = "https://usuario:tokensecreto@github.com/org/f.git"\n'
                'path = "frontend"\n'
            )
        marco = ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus)
        self.assertTrue(marco["fuentes"]["declarado"])
        self.assertEqual([f["id"] for f in marco["fuentes"]["fuentes"]], ["frontend"])
        self.assertEqual(marco["fuentes"]["fuentes"][0]["remoto"], "declarado")
        volcado = json.dumps(marco, ensure_ascii=False)
        self.assertNotIn("tokensecreto", volcado)
        self.assertNotIn("github.com", volcado)

    def test_04_el_encuadre_es_determinista_y_no_lleva_ruta_de_la_maquina(self):
        """T195 · Defecto que previene: un artefacto derivado que cambia con el directorio.

        Dos encuadres de la MISMA entrada sobre el MISMO repo dan el MISMO identificador, y
        ningún byte del encuadre contiene la ruta absoluta del control repo (`I-g3`).
        """
        uno = ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus)
        otro = ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus)
        self.assertEqual(uno, otro)
        self.assertNotIn(self.repo, json.dumps(uno, ensure_ascii=False))

    def test_05_la_politica_y_el_perfil_se_cargan_y_la_precondicion_falla_cerrado(self):
        """T195 · Defecto que previene: componer una ruta sin comprobar lo que se exigió.

        La política de `g.14` se carga por su sede y trae sus ocho operaciones; una
        precondición declarada y no cumplida levanta error tipado y NO se encuadra.
        """
        marco = ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus)
        self.assertEqual(len(marco["politica"]["operaciones"]), 8)
        self.assertEqual(marco["politica"]["publicacion_por_defecto"], "esperando-owner")
        self.assertFalse(marco["perfil"]["declarado"])
        with self.assertRaises(ciclo.PrecondicionIncumplida) as capturado:
            ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus,
                            precondiciones=("hay remoto para el control repo",))
        self.assertEqual(capturado.exception.codigo, "PRECONDICION_INCUMPLIDA")


# =========================================================================
# T196 · composición de rutas por `b.16`, las CUATRO vías y el GATE
# =========================================================================
class Composicion(BaseDelCiclo):

    def test_10_los_diez_procesos_se_derivan_del_fichero_y_todos_son_alcanzables(self):
        """T196 · Defecto que previene: una copia de `b.16` escrita a mano en el runtime.

        Los diez salen de los bloques `ads:proceso`; la correspondencia materia → proceso
        no nombra ninguno que no exista y no deja ninguno inalcanzable.
        """
        derivados = tuple(sorted(self.corpus.procesos()))
        self.assertEqual(derivados, DIEZ_PROCESOS)
        self.assertEqual(procesos.exigir_coherente(self.corpus), DIEZ_PROCESOS)
        self.assertEqual(len(procesos.MATERIAS), 10)

    def test_11_renombrar_el_titulo_no_cambia_la_ruta(self):
        """T196 · Defecto que previene: elegir el proceso por coincidencias léxicas.

        Es una de las dos mitades del eje de esta batería. Se cambia la expresión literal y
        el resultado perseguido —el «título»— dejando MATERIA y ESTADO intactos, y la ruta
        resultante tiene que ser IDÉNTICA salvo por el encuadre que la origina.
        """
        primera = ciclo.componer(
            ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus),
            corpus=self.corpus,
        )
        segunda = ciclo.componer(
            ciclo.encuadrar(self.repo, entrada_base(
                expresion_literal="el informe no se puede bajar a hoja de calculo",
                resultado_perseguido="quien usa la vista obtiene el listado en un fichero",
            ), corpus=self.corpus),
            corpus=self.corpus,
        )
        self.assertEqual(primera["proceso"], segunda["proceso"])
        self.assertEqual(primera["propietario_global"], segunda["propietario_global"])
        self.assertEqual(
            [(p["capacidad"], p["via"]) for p in primera["participantes"]],
            [(p["capacidad"], p["via"]) for p in segunda["participantes"]],
        )
        self.assertEqual(
            [p["capacidad"] for p in primera["no_activadas"]],
            [p["capacidad"] for p in segunda["no_activadas"]],
        )

    def test_12_un_sinonimo_no_activa_ninguna_capacidad(self):
        """T196 · Defecto que previene: una capacidad que entra porque alguien dijo «diseño».

        La otra mitad del eje. La expresión del Owner nombra explícitamente diseño,
        arquitectura, dominio y seguridad; sin condiciones DECLARADAS verdaderas, ninguna de
        las cuatro entra, y todas quedan en la lista de NO activadas CON MOTIVO.
        """
        marco = ciclo.encuadrar(self.repo, entrada_base(
            expresion_literal="el diseño visual, la arquitectura, el dominio y la seguridad "
                              "de esto hay que revisarlos por completo",
            interpretacion="parece que toca DIS, ARQ, DOM y SEG",
        ), corpus=self.corpus)
        ruta = ciclo.componer(marco, corpus=self.corpus)
        activadas = {p["capacidad"] for p in ruta["participantes"]}
        for capacidad in ("DIS", "ARQ", "DOM", "SEG"):
            self.assertNotIn(capacidad, activadas, capacidad)
        no_activadas = {p["capacidad"]: p["motivo"] for p in ruta["no_activadas"]}
        for capacidad in ("DIS", "ARQ", "DOM", "SEG"):
            self.assertIn(capacidad, no_activadas, capacidad)
            self.assertIn("no consta verdadera", no_activadas[capacidad])

    def test_13_las_cuatro_vias_y_ninguna_quinta(self):
        """T196 · Defecto que previene: un «participante sin vehículo» en la ruta.

        Vía 1 propietaria, vía 2 obligatoria, vía 3 condicional CON su condición nombrada, y
        vía 4 item propio enlazado a su item líder. Una vía fuera de las cuatro es error, y
        un item propio sin enlace también.
        """
        marco = ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus)
        ruta = ciclo.componer(
            marco, corpus=self.corpus, condiciones_verdaderas=["C-DIS"],
            items_enlazados=[{"capacidad": "INV", "proceso": "proceso:INV",
                              "item_lider": "it-lider"}],
        )
        vias = {p["via"] for p in ruta["participantes"]}
        self.assertEqual(vias, set(CUATRO_VIAS))
        for participante in ruta["participantes"]:
            self.assertIn(participante["via"], CUATRO_VIAS)
            if participante["via"] == rutas.VIA_CONDICIONAL:
                self.assertTrue(participante["condicion"])
            if participante["via"] == rutas.VIA_ITEM_PROPIO:
                self.assertEqual(participante["item_lider"], "it-lider")
        with self.assertRaises(ciclo.ViaInvalida):
            ciclo.componer(marco, corpus=self.corpus, items_enlazados=[
                {"capacidad": "INV", "proceso": "proceso:INV"},
            ])

    def test_14_las_tres_formas_de_estar_presente_no_participan(self):
        """T196 · Defecto que previene: confundir un EJECUTOR con un participante de la ruta.

        `PLT` ejecuta la materialización y NO deposita capa; el Owner autoriza y no deposita
        capa; `ENC` encuadra y `b.16` no la declara en ningún proceso. Las tres van a
        `presencias` con `participa: false`, y `ENC` no puede entrar como participante.
        """
        marco = ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus)
        ruta = ciclo.componer(marco, corpus=self.corpus, presencias=[
            {"forma": "ejecutor", "quien": "PLT", "motivo": "materializa por `C7:82`"},
            {"forma": "autoridad", "quien": "OWNER", "motivo": "autoriza la retirada"},
            {"forma": "encuadre", "quien": "ENC", "motivo": "produce el encuadre"},
        ])
        self.assertEqual(sorted({p["forma"] for p in ruta["presencias"]}),
                         sorted(TRES_PRESENCIAS))
        for presencia in ruta["presencias"]:
            self.assertFalse(presencia["participa"], presencia)
        participantes = {p["capacidad"] for p in ruta["participantes"]}
        self.assertNotIn("ENC", participantes)
        with self.assertRaises(ciclo.ViaInvalida):
            rutas._participante(self.corpus, "ENC", rutas.VIA_OBLIGATORIA, "proceso:FEA",
                                motivo="x", condicion=None, salida="y", criterio="z")
        with self.assertRaises(ciclo.ViaInvalida):
            ciclo.componer(marco, corpus=self.corpus,
                           presencias=[{"forma": "colaborador", "quien": "PLT"}])

    def test_15_el_gate_de_composicion_no_abre_la_fase_y_nombra_capacidad_y_fase(self):
        """T196 · Defecto que previene: abrir una fase con una capacidad sin vía.

        `composicion-incompleta`: la fase NO abre, DSP para y escala NOMBRANDO la capacidad
        y la fase. Se comprueban las dos cosas en el contexto del error, no en su texto.
        """
        marco = ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus)
        with self.assertRaises(ciclo.ComposicionIncompleta) as capturado:
            ciclo.componer(marco, corpus=self.corpus, fase="INS-0",
                           capacidades_de_la_fase=["PRD", "CON", "VER", "SEG"])
        error = capturado.exception
        self.assertEqual(error.codigo, "COMPOSICION_INCOMPLETA")
        self.assertEqual(error.contexto["capacidad"], "SEG")
        self.assertEqual(error.contexto["fase"], "INS-0")
        # Y la fase NO abre: componer es PURO y no ha escrito nada.
        self.assertFalse(os.path.isdir(os.path.join(self.repo, "estado")))

    def test_16_una_condicion_vaga_esta_prohibida(self):
        """T196 · Defecto que previene: una condición que nadie puede comprobar.

        `b.16` prohíbe la fórmula vaga; el vocabulario cerrado `C-*` pasa, una condición
        propia redactada pasa, y las fórmulas que el validador de vocabulario rechaza
        levantan `CONDICION_VAGA`.
        """
        for buena in modulo_corpus.CONDICIONES_DE_B16:
            self.assertEqual(procesos.comprobar_condicion(buena, capacidad="DIS"), buena)
        propia = "el cambio modifica el runtime: activación segura y reversible"
        self.assertEqual(procesos.comprobar_condicion(propia, capacidad="ENT"), propia)
        for mala in ("si aplica", "cuando corresponda", "si procede", "en su caso", ""):
            with self.assertRaises(ciclo.CondicionVaga, msg=mala):
                procesos.comprobar_condicion(mala, capacidad="DIS")

    def test_17_el_propietario_de_AUD_y_DIR_se_deriva_del_encargo_y_nunca_a_mano(self):
        """T196 · Defecto que previene: que DSP elija quién responde de una conclusión.

        `01-PROCESOS.md` L419 lo prohíbe expresamente para `AUD`, y `DIR` dice «NUNCA lo
        elige DSP». Sin declaración del encargo, `PROPIETARIO_NO_DERIVABLE`.
        """
        marco = ciclo.encuadrar(self.repo, entrada_base(
            materia="conclusion-sobre-lo-existente", estado_del_objeto="existe",
        ), corpus=self.corpus)
        with self.assertRaises(ciclo.PropietarioNoDerivable) as capturado:
            ciclo.componer(marco, corpus=self.corpus)
        self.assertEqual(capturado.exception.contexto["proceso"], "proceso:AUD")
        ruta = ciclo.componer(marco, corpus=self.corpus, propietario_declarado="PRD")
        self.assertEqual(ruta["propietario_global"], "PRD")
        self.assertIn("DERIVADO del encargo", ruta["origen_del_propietario"])

    def test_18_el_propietario_de_DEF_se_deriva_de_C_ARQ_y_no_de_la_prosa(self):
        """T196 · Defecto que previene: leer la prosa de `b.16` para decidir autoridad.

        `proceso:DEF` declara «ARQ cuando C-ARQ es verdadera; CON en caso contrario». La
        derivación es un DATO con su condición del vocabulario cerrado, y se comprueba en
        los dos sentidos.
        """
        marco = ciclo.encuadrar(self.repo, entrada_base(
            materia="comportamiento-especificado-roto", estado_del_objeto="existe",
        ), corpus=self.corpus)
        sin = ciclo.componer(marco, corpus=self.corpus)
        con = ciclo.componer(marco, corpus=self.corpus, condiciones_verdaderas=["C-ARQ"])
        self.assertEqual(sin["propietario_global"], "CON")
        self.assertEqual(con["propietario_global"], "ARQ")

    def test_19_la_materia_y_el_estado_deciden_la_ruta_y_el_par_se_comprueba(self):
        """T196 · Defecto que previene: confundir `FEA` con `GAP` por el texto del item.

        Las dos rutas se distinguen por el ESTADO del objeto —no existe frente a existe—, y
        un par que `b.1` no admite es error tipado con su materia y su estado nombrados.
        """
        self.assertEqual(
            procesos.proceso_de("capacidad-ausente", "no-existe", corpus=self.corpus),
            "proceso:FEA",
        )
        self.assertEqual(
            procesos.proceso_de("expectativa-no-alcanzada", "existe", corpus=self.corpus),
            "proceso:GAP",
        )
        with self.assertRaises(ciclo.EstadoDeMateriaInvalido) as capturado:
            procesos.proceso_de("capacidad-ausente", "existe", corpus=self.corpus)
        self.assertEqual(capturado.exception.contexto["materia"], "capacidad-ausente")
        with self.assertRaises(ciclo.MateriaSinProceso):
            procesos.proceso_de("inventada", "existe", corpus=self.corpus)

    def test_20_la_traza_declara_activadas_y_no_activadas_con_motivo(self):
        """T196 · Defecto que previene: una ruta sin la traza que su propio gate exige.

        `gate:despacho-coherente`, comprobación `traza-de-ruta`: «toda ruta declara activadas
        y NO activadas, cada una con motivo escrito».
        """
        marco = ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus)
        traza = ciclo.traza(ciclo.componer(marco, corpus=self.corpus,
                                           condiciones_verdaderas=["C-ENT"]))
        self.assertTrue(traza["activadas"])
        self.assertTrue(traza["no_activadas"])
        for entrada in traza["activadas"] + traza["no_activadas"]:
            self.assertTrue(entrada["motivo"].strip(), entrada)


# =========================================================================
# T197 · materialización de equipos por `C4`
# =========================================================================
class Equipos(BaseDelCiclo):

    def test_25_un_metodo_no_es_una_capacidad_y_se_dice_cual_es_cual(self):
        """T197 · Defecto que previene: materializar un equipo de `DOM:condiciones`.

        El corpus escribe participantes condicionales como `CAPACIDAD:metodo`. Lo que `C4`
        materializa es la CAPACIDAD; el método es CÓMO trabaja (`C1`). Se prueba por los dos
        lados: separar bien, y fallar al pasar un método donde va una capacidad.
        """
        self.assertEqual(procesos.capacidad_de("DOM:condiciones"), "DOM")
        self.assertEqual(procesos.metodo_de("DOM:condiciones"), "condiciones")
        self.assertEqual(procesos.capacidad_de("DIS/Reconstruccion"), "DIS")
        self.assertEqual(procesos.metodo_de("DIS/Reconstruccion"), "Reconstruccion")
        self.assertEqual(procesos.capacidad_de("CON"), "CON")
        self.assertIsNone(procesos.metodo_de("CON"))
        for metodo in ("DOM:condiciones", "Fundacion", "Continua", "Encaje"):
            with self.assertRaises(ciclo.MetodoNoEsCapacidad, msg=metodo):
                ciclo.exigir_capacidad(metodo, corpus=self.corpus)
        for capacidad in QUINCE:
            self.assertEqual(ciclo.exigir_capacidad(capacidad, corpus=self.corpus),
                             capacidad)

    def test_26_la_ruta_solo_deriva_capacidades_y_ningun_nombre_de_metodo(self):
        """T197 · Defecto que previene: que un método se cuele en la lista del equipo.

        Se compone una ruta con TODAS las condicionales activas —que son las que traen
        método— y se comprueba que las capacidades derivadas son todas de las quince y que
        el método viaja aparte, sin perderse.
        """
        marco = ciclo.encuadrar(self.repo, entrada_base(
            materia="forma-interna-costosa", estado_del_objeto="existe",
        ), corpus=self.corpus)
        ruta = ciclo.componer(
            marco, corpus=self.corpus,
            condiciones_verdaderas=list(modulo_corpus.CONDICIONES_DE_B16),
        )
        derivadas = ciclo.derivar_capacidades(ruta)
        for capacidad in derivadas:
            self.assertIn(capacidad, QUINCE, capacidad)
        metodos = {p["capacidad"]: p["metodo"] for p in ruta["participantes"]
                   if p["metodo"]}
        self.assertEqual(metodos.get("DOM"), "condiciones")
        self.assertEqual(metodos.get("SEG"), "condiciones")

    def test_27_la_composicion_se_elige_por_orden_escrito_y_ninguna_es_error(self):
        """T197 · Defecto que previene: materializar un equipo por defecto cuando no toca.

        `C4` paso 2: el PRIMERO cuya condición es verdadera, en el orden en que están
        escritas. Si ninguna lo es, es un defecto del catálogo y se escala a `SIS`: NO se
        inventa un equipo.
        """
        escritas = [c["id"] for c in self.corpus.composiciones("DIS")]
        self.assertGreater(len(escritas), 1)
        elegida = equipos.materializar(
            "DIS", corpus=self.corpus,
            composiciones_verdaderas=[escritas[-1], escritas[1]], slots=99,
        )
        # Manda el ORDEN ESCRITO, no el orden en que se declararon verdaderas.
        self.assertEqual(elegida["composicion"], escritas[1])
        self.assertEqual(
            [c["composicion"] for c in elegida["composiciones_descartadas"]],
            escritas[:1],
        )
        with self.assertRaises(ciclo.ComposicionDeEquipoAusente) as capturado:
            equipos.materializar("DIS", corpus=self.corpus, composiciones_verdaderas=[])
        self.assertEqual(capturado.exception.contexto["capacidad"], "DIS")

    def test_28_lo_que_no_cabe_espera_y_la_composicion_no_se_reduce(self):
        """T197 · Defecto que previene: recortar el equipo para que quepa en los slots.

        `C4` paso 6, literal: «Lo que no cabe queda `esperando-capacidad`. NO se reduce la
        composición para que quepa». El equipo escrito lleva las dos listas.
        """
        # Se elige la composición con MÁS roles obligatorios: con una de un solo rol el
        # recorte no se podría observar, y la prueba pasaría sin comprobar nada.
        escritas = self.corpus.composiciones("DIS")
        elegida = max(escritas, key=lambda c: len(
            [r for r in c["roles"] if r.get("obligatorio")]))["id"]
        holgado = equipos.materializar(
            "DIS", corpus=self.corpus, composiciones_verdaderas=[elegida], slots=99,
        )
        self.assertGreater(len(holgado["roles"]), 2)
        apretado = equipos.materializar(
            "DIS", corpus=self.corpus, composiciones_verdaderas=[elegida], slots=2,
        )
        self.assertEqual(len(apretado["roles"]), 2)
        self.assertTrue(apretado["esperando_capacidad"])
        self.assertEqual(
            sorted(r["rol"] for r in apretado["roles"] + apretado["esperando_capacidad"]),
            sorted(r["rol"] for r in holgado["roles"]),
        )
        for rol in apretado["esperando_capacidad"]:
            self.assertEqual(rol["estado"], "esperando-capacidad")

    def test_29_independientes_manda_sobre_combinables(self):
        """T197 · Defecto que previene: un agente que produce y se revisa a sí mismo.

        `C4` paso 5: ante conflicto entre las dos listas, MANDA `independientes`. Se
        comprueba sobre la composición real de `DSP`, cuya `supervision` es independiente de
        `enrutamiento`, y se comprueba que la separación exigida falla cuando se viola.
        """
        equipo = equipos.materializar(
            "DSP", corpus=self.corpus,
            composiciones_verdaderas=["composicion:dsp-supervisor"], slots=99,
        )
        self.assertTrue(equipo["independientes"])
        aplicadas = {tuple(c["roles"]) for c in equipo["combinaciones"] if c["aplicada"]}
        for entrada in equipo["independientes"]:
            for combinada in aplicadas:
                if entrada["rol"] in combinada:
                    for otro in combinada:
                        self.assertNotIn(otro, entrada["de"], (entrada, combinada))
        self.assertTrue(equipos.exigir_separacion(
            equipo, autor="DSP/enrutamiento", revisor="DSP/supervision",
        ))
        with self.assertRaises(ciclo.ConflictoDeRoles):
            equipos.exigir_separacion(equipo, autor="DSP/estado", revisor="DSP/estado")

    def test_29b_la_regla_de_independientes_TIENE_que_poder_ponerse_roja(self):
        """T197 · Defecto que previene: una prohibición que nadie puede violar en la prueba.

        DEFECTO QUE CIERRA, medido por la auditoría independiente: la regla «`independientes`
        manda sobre `combinables`» se podía BORRAR ENTERA del producto y las cuarenta y ocho
        pruebas seguían verdes. La de arriba recorre `aplicadas ∩ independientes`, que en el
        corpus real está VACÍO, y su `assertRaises` disparaba la rama TRIVIAL —el mismo rol
        en dos posiciones—, nunca la de `independientes`. Es la prohibición más sensible de
        `C4` —«PROHIBIDO un agente ocupando un rol productor y su crítico»— y no tenía rojo
        que dar.

        Aquí se construye el conflicto que el corpus no tiene: dos roles DISTINTOS que la
        composición declara independientes Y que comparten agente. Si alguien retira la
        comprobación, esta prueba se pone roja. Se verificó neutralizando `_choca` y la rama
        de `independientes`: las dos mitades fallan.
        """
        # (i) la rama de `independientes` de `exigir_separacion`, con roles DISTINTOS.
        equipo = {
            "roles": [
                {"rol": "DIS/produce", "comparte_agente_con": "DIS/critica"},
                {"rol": "DIS/critica", "comparte_agente_con": "DIS/produce"},
            ],
            "independientes": [{
                "rol": "DIS/critica", "de": ["DIS/produce"],
                "motivo": "quien critica no puede ser quien produjo",
            }],
        }
        with self.assertRaises(ciclo.ConflictoDeRoles) as capturado:
            equipos.exigir_separacion(equipo, autor="DIS/produce", revisor="DIS/critica")
        self.assertIn("independiente", str(capturado.exception))
        self.assertEqual(sorted(capturado.exception.contexto["roles"]),
                         ["DIS/critica", "DIS/produce"])
        # CONTROL: sin la declaración de independencia, los MISMOS roles compartiendo agente
        # pasan. Sin este control, el rojo de arriba podría venir de cualquier otra cosa.
        sin_declarar = {"roles": equipo["roles"], "independientes": []}
        self.assertTrue(equipos.exigir_separacion(
            sin_declarar, autor="DIS/produce", revisor="DIS/critica"))
        # (ii) el PASO 5: una pareja declarada combinable Y a la vez independiente NO se
        # combina, y el motivo lo dice.
        independientes = [{"rol": "DIS/critica", "de": ["DIS/produce"], "motivo": "x"}]
        self.assertTrue(equipos._choca(
            "DIS/critica", ["DIS/produce", "DIS/critica"], independientes))
        self.assertTrue(equipos._choca(
            "DIS/produce", ["DIS/produce", "DIS/critica"], independientes))
        self.assertFalse(equipos._choca(
            "DIS/critica", ["DIS/otro", "DIS/critica"], independientes))

    def test_29c_la_condicion_COMPUESTA_de_a5_y_el_freno_de_a7(self):
        """T197 · Etapa 5 del `§7.2`: las SEIS condiciones, y `escribe` disjunto NO basta.

        DEFECTO QUE CIERRA, encontrado por la auditoría independiente: la etapa 5 del `§7.2`
        —«DSP comprueba la condición COMPUESTA de paralelismo (a.5, seis condiciones)»— NO
        estaba implementada. Lo que había era un booleano que encadenaba todos los paquetes,
        y encadenar siempre no es comprobar: da el resultado seguro por el camino de no
        mirar. Con él, la prohibición central de `a.5` —que el aislamiento físico por sí
        solo NUNCA autoriza— no estaba en ninguna parte del código.
        """
        from ciclo import durable, paralelismo

        def paquete(identificador, **acoplamiento):
            declarado = {"escribe_ficheros": [], "afecta_contratos": [],
                         "afecta_decisiones": [], "based_on": [], "integra_en": "rama",
                         "lee_fuentes": [], "escribe_fuentes": []}
            declarado.update(acoplamiento)
            return {"id": identificador, "depende_de": [], "acoplamiento": declarado}

        # (i) físicamente disjuntos Y paralelizables: el caso positivo.
        uno = paquete("pq-1", escribe_ficheros=["a.py"], escribe_fuentes=["frontend"])
        dos = paquete("pq-2", escribe_ficheros=["b.py"], escribe_fuentes=["backend"])
        self.assertTrue(paralelismo.evaluar(uno, dos)[0])

        # (ii) LA PROHIBICIÓN CENTRAL: escrituras disjuntas y AUN ASÍ no paralelizables,
        # una por cada condición que no es la física.
        contrarios = {
            "sin-dependencia-de-salida":
                paquete("pq-3", escribe_ficheros=["c.py"], escribe_fuentes=["infra"]),
            "sin-autoridad-concurrente-sobre-la-misma-decision":
                paquete("pq-4", escribe_ficheros=["d.py"], escribe_fuentes=["infra"],
                        afecta_decisiones=["decision:formato-de-fecha"]),
            "sin-contratos-compartidos-incompatibles":
                paquete("pq-5", escribe_ficheros=["e.py"], escribe_fuentes=["infra"],
                        afecta_contratos=["api:pedidos"]),
            "versiones-de-entrada-compatibles":
                paquete("pq-6", escribe_ficheros=["f.py"], escribe_fuentes=["infra"],
                        based_on=["backend@r1"]),
            "estrategia-de-integracion-explicita":
                paquete("pq-7", escribe_ficheros=["g.py"], escribe_fuentes=["infra"],
                        integra_en=""),
        }
        contrarios["sin-dependencia-de-salida"]["depende_de"] = [uno["id"]]
        referencia = {
            "sin-dependencia-de-salida": uno,
            "sin-autoridad-concurrente-sobre-la-misma-decision":
                paquete("pq-r4", escribe_ficheros=["h.py"], escribe_fuentes=["frontend"],
                        afecta_decisiones=["decision:formato-de-fecha"]),
            "sin-contratos-compartidos-incompatibles":
                paquete("pq-r5", escribe_ficheros=["i.py"], escribe_fuentes=["frontend"],
                        afecta_contratos=["api:pedidos"]),
            "versiones-de-entrada-compatibles":
                paquete("pq-r6", escribe_ficheros=["j.py"], escribe_fuentes=["frontend"],
                        based_on=["backend@r2"]),
            "estrategia-de-integracion-explicita":
                paquete("pq-r7", escribe_ficheros=["k.py"], escribe_fuentes=["frontend"]),
        }
        for condicion, candidato in contrarios.items():
            otro = referencia[condicion]
            paralelizable, incumplidas = paralelismo.evaluar(candidato, otro)
            self.assertFalse(paralelizable, condicion)
            self.assertIn(condicion, [i["condicion"] for i in incumplidas], condicion)
            # LA MITAD QUE IMPORTA: sus escrituras son disjuntas y aun así NO se paralelizan.
            self.assertTrue(paralelismo.solo_lo_fisico_no_basta(candidato, otro), condicion)
        # Y las seis están cubiertas: la física por (iii), las otras cinco por el bucle.
        self.assertEqual(len(paralelismo.CONDICIONES), len(contrarios) + 1)

        # (iii) la física, que es NECESARIA aunque no suficiente.
        choca = paquete("pq-8", escribe_ficheros=["a.py"], escribe_fuentes=["frontend"])
        paralelizable, incumplidas = paralelismo.evaluar(uno, choca)
        self.assertFalse(paralelizable)
        self.assertIn("escrituras-fisicas-disjuntas-o-aisladas",
                      [i["condicion"] for i in incumplidas])
        self.assertFalse(paralelismo.solo_lo_fisico_no_basta(uno, choca))

        # (iv) `secuenciar` escribe la TRAZA, que `b.12` paso 7 exige.
        espera, traza = paralelismo.secuenciar([uno, dos, choca])
        self.assertEqual(espera[uno["id"]], [])
        self.assertEqual(espera[dos["id"]], [])
        self.assertEqual(espera[choca["id"]], [uno["id"]])
        self.assertTrue(all(entrada["motivos"] for entrada in traza))

    def test_29d_el_freno_de_devoluciones_de_a7_se_ACUMULA(self):
        """T197 · Defecto que previene: un contador que nadie suma.

        DEFECTO QUE CIERRA: `C5` escribía `cuenta_para_el_freno` en cada entrega y NADIE lo
        sumaba ni aplicaba el tope de dos de `a.7`. Un freno que no frena es una etiqueta.
        """
        from ciclo import durable, paralelismo

        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.plan_completo(rt)
        catalogo = ciclo.catalogo(self.corpus)["handoff:con-a-ver"]
        trazabilidad = {"item": plan["item"], "paquete": plan["paquetes"][0],
                        "ruta": plan["ruta"]}
        frenado, cuenta, _ = paralelismo.freno_de_devoluciones(rt.almacen, plan["item"])
        self.assertFalse(frenado)
        self.assertEqual(cuenta, 0)
        for numero in range(paralelismo.DEVOLUCIONES_MAXIMAS):
            entrega = ciclo.emitir(
                "handoff:con-a-ver", corpus=self.corpus,
                # Los artefactos varían por vuelta: la identidad de la entrega se deriva
                # del contenido de la EMISIÓN, así que dos emisiones idénticas serían la
                # misma entrega, y aquí hacen falta dos distintas.
                artefactos=["la rama con el cambio construido, vuelta " + str(numero)],
                checkpoint="el estado del paquete", trazabilidad=trazabilidad,
            )
            acusada = ciclo.acusar(
                entrega, receptor="VER",
                comprobaciones_superadas=catalogo["comprueba_al_recibir"])
            devuelta = ciclo.devolver(acusada, devolucion={
                campo: ["algo"] if campo.startswith("evidencia") else "algo"
                for campo in handoffs.CAMPOS_DE_DEVOLUCION})
            self.assertTrue(devuelta["cuenta_para_el_freno"])
            durable.escribir(
                rt.almacen, clase="ciclo.handoff.devuelto",
                motivo="devolucion " + str(numero),
                objetos={handoffs.ruta_de(devuelta["id"]): devuelta})
        frenado, cuenta, motivo = paralelismo.freno_de_devoluciones(rt.almacen, plan["item"])
        self.assertTrue(frenado, "el freno de `a.7` no se aplicó al agotar las devoluciones")
        self.assertEqual(cuenta, paralelismo.DEVOLUCIONES_MAXIMAS)
        self.assertIn("se PARA y se escala", motivo)
        # Un item DISTINTO no queda frenado por las devoluciones de otro.
        self.assertFalse(paralelismo.freno_de_devoluciones(rt.almacen, "it-ajeno")[0])

    def test_30_el_equipo_se_persiste_por_el_motor_y_es_idempotente(self):
        """T197 · Defecto que previene: una asignación de equipo que sólo vive en memoria.

        Se materializa, se persiste por el motor y se lee del estado canónico. Persistirlo
        dos veces NO mueve la revisión: el identificador se deriva del contenido.
        """
        rt = self.abrir_runtime()
        equipo = equipos.materializar(
            "DSP", corpus=self.corpus,
            composiciones_verdaderas=["composicion:dsp-supervisor"], slots=4,
        )
        planificador = ciclo.Planificador(rt, corpus=self.corpus)
        planificador.registrar_equipos([equipo])
        antes = rt.almacen.revision()
        planificador.registrar_equipos([equipo])
        despues = rt.almacen.revision()
        self.assertEqual(antes["revision_id"], despues["revision_id"])
        leido = rt.almacen.leer(equipos.ruta_de(equipo["id"]))
        self.assertEqual(leido["composicion"], "composicion:dsp-supervisor")
        self.assertEqual(leido["capacidad"], "DSP")


# =========================================================================
# T198 · planificación y despacho
# =========================================================================
class Planificacion(BaseDelCiclo):

    def test_35_planificar_crea_items_y_paquetes_por_el_runtime(self):
        """T198 · Defecto que previene: un alta de trabajo paralela a la del runtime.

        Los items y los paquetes salen de `Runtime.crear_item` y `Runtime.crear_paquete`, y
        se leen del estado canónico. El plan enriquece; no sustituye.
        """
        rt = self.abrir_runtime()
        marco, ruta, plan = self.plan_completo(rt)
        self.assertTrue(rt.almacen.leer("items/" + plan["item"] + ".json"))
        for paquete in plan["paquetes"]:
            objeto = rt.almacen.leer("paquetes/" + paquete + ".json")
            self.assertEqual(objeto["item"], plan["item"])
            self.assertEqual(objeto["max_intentos"], 3)     # el tope de `a.9`
        self.assertEqual(len(plan["correspondencia"]), len(ruta["participantes"]))
        # El paquete conserva el vocabulario CERRADO del runtime: no se le añaden campos.
        from runtime.modelo import CLAVES_DE_PAQUETE
        objeto = rt.almacen.leer("paquetes/" + plan["paquetes"][0] + ".json")
        self.assertEqual(sorted(set(objeto) - {"esquema"}), sorted(CLAVES_DE_PAQUETE))

    def test_36_la_prioridad_se_deriva_de_la_via_y_el_orden_es_determinista(self):
        """T198 · Defecto que previene: una selección que depende de quién la calculó.

        `gate:despacho-coherente`, comprobación `determinismo`: «mismo estado produce misma
        selección, con desempate por identificador». La prioridad no se escribe a mano: la
        vía la fija.
        """
        rt = self.abrir_runtime()
        _marco, ruta, plan = self.plan_completo(rt, condiciones=["C-DIS"])
        # La correspondencia lleva SU vía, y no la de la capacidad: una misma capacidad
        # puede entrar por dos vías —propietaria global y obligatoria— y son dos paquetes.
        for fila in plan["correspondencia"]:
            esperada = ciclo.planificacion.PRIORIDAD_POR_VIA[fila["via"]]
            self.assertEqual(fila["prioridad"], esperada, fila)
        self.assertEqual(
            sorted((p["capacidad"], p["via"]) for p in ruta["participantes"]),
            sorted((f["capacidad"], f["via"]) for f in plan["correspondencia"]),
        )
        primera = [e["paquete"] for e in rt.elegibles()]
        segunda = [e["paquete"] for e in rt.elegibles()]
        self.assertEqual(primera, segunda)

    def test_37_b_15_1_abre_el_desbloqueador_dentro_del_alcance_y_escala_fuera(self):
        """T198 · Defecto que previene: molestar al Owner por aritmética de la ruta.

        `b.15.1`: dentro del alcance ya autorizado, DSP crea y despacha SIN preguntar; sólo
        escala lo que amplía el alcance. La frontera es un DATO del plan.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.plan_completo(rt)
        bloqueado = plan["paquetes"][0]
        rt.pausar(bloqueado, motivo="para bloquearlo después", autoridad="OWNER")
        rt._mover(bloqueado, "listo", motivo="reanudado", autoridad="OWNER",
                  clase="runtime.paquete.reanudado")
        rt._mover(bloqueado, "bloqueado", motivo="falta una decisión externa",
                  autoridad="OWNER", clase="runtime.paquete.bloqueado")
        planificador = ciclo.Planificador(rt, corpus=self.corpus)
        capacidad = plan["alcance_autorizado"]["capacidades"][0]
        abierto = planificador.abrir_desbloqueador(
            plan, bloqueado, capacidad=capacidad,
            orden=self.orden([capacidad])[capacidad],
            motivo="crear el desbloqueador dentro del alcance autorizado",
        )
        self.assertIn(abierto["paquete"], abierto["plan"]["paquetes"])
        nuevo = rt.almacen.leer("paquetes/" + abierto["paquete"] + ".json")
        self.assertEqual(nuevo["estado"], "listo")
        self.assertEqual(nuevo["prioridad"], 95)
        with self.assertRaises(ciclo.AlcanceNoAutorizado) as capturado:
            planificador.abrir_desbloqueador(
                plan, bloqueado, capacidad="PLT",
                orden=self.orden(["PLT"])["PLT"], motivo="fuera del alcance",
            )
        self.assertEqual(capturado.exception.contexto["capacidad"], "PLT")

    def test_38_el_despacho_delega_y_pasa_por_un_unico_punto(self):
        """T198 · Defecto que previene: una segunda máquina de despacho en el ciclo.

        Todo el despacho del ciclo entra por `ciclo.despacho`, que es observable. Se instala
        un observador, se ejecuta un barrido, y se comprueba que lo observado casa con lo
        que el runtime dice haber atendido.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.plan_completo(rt)
        vistos = []
        retirar = ciclo.observar(vistos.append)
        self.addCleanup(retirar)
        informe = ciclo.barrido(rt, origen="prueba")
        self.assertTrue(informe["atendidos"])
        self.assertEqual(
            sorted(v["paquete"] for v in vistos),
            sorted(a["paquete"] for a in informe["atendidos"]),
        )
        for visto in vistos:
            self.assertEqual(visto["punto"], ciclo.PUNTO_DE_ENTRADA)
            self.assertEqual(visto["origen"], "prueba")

    def test_39_no_hay_doble_efecto_y_el_acuse_lo_impide(self):
        """T198 · Defecto que previene: aplicar dos veces un efecto ya confirmado.

        El ciclo no reimplementa la idempotencia: la delega. Se despacha, se comprueba el
        acuse durable, y un segundo barrido no vuelve a ejecutar nada.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.plan_completo(rt)
        for _vuelta in range(len(plan["paquetes"]) + 1):
            ciclo.barrido(rt, origen="prueba")
        completados = [
            rt.almacen.leer("paquetes/" + p + ".json") for p in plan["paquetes"]
        ]
        for paquete in completados:
            self.assertEqual(paquete["estado"], "completado", paquete["id"])
            acuse = rt.almacen.leer("efectos/" + paquete["efecto"] + ".json")
            self.assertTrue(acuse["aplicado"])
        antes = rt.almacen.revision()["revision_id"]
        ciclo.barrido(rt, origen="prueba")
        self.assertEqual(rt.almacen.revision()["revision_id"], antes)


# =========================================================================
# T199 · gates de capa
# =========================================================================
class Gates(BaseDelCiclo):

    def test_45_el_censo_de_gates_se_deriva_del_corpus_y_no_se_inventa(self):
        """T199 · Defecto que previene: aplicar un gate que el modelo no define.

        El censo se contrasta contra un barrido INDEPENDIENTE del árbol, hecho con una
        expresión regular sobre los ficheros: dos formas distintas de contar lo mismo.
        """
        derivado = set(ciclo.censo_de_gates(self.corpus))
        encontrados = set()
        patron = re.compile(r"^id:\s*(gate:[a-z0-9-]+)\s*$")
        for directorio, subdirectorios, ficheros in os.walk(KERNEL):
            subdirectorios[:] = [d for d in subdirectorios
                                 if d not in ("runtime", "validadores", "pruebas",
                                              "__pycache__")]
            for nombre in ficheros:
                if not nombre.endswith(".md"):
                    continue
                with open(os.path.join(directorio, nombre), encoding="utf-8") as fichero:
                    dentro = False
                    for linea in fichero:
                        if linea.startswith("```yaml ads:gate"):
                            dentro = True
                            continue
                        if dentro and linea.startswith("```"):
                            dentro = False
                            continue
                        if dentro:
                            casado = patron.match(linea.strip())
                            if casado:
                                encontrados.add(casado.group(1))
        self.assertEqual(derivado, encontrados)
        self.assertIn("gate:sistema-conforme", derivado)
        with self.assertRaises(ciclo.GateDesconocido):
            ciclo.aplicar_gate("gate:inventado", entrada={}, evidencia=[], revisor="VER",
                               autor="CON", corpus=self.corpus)

    def test_46_un_gate_falla_cerrado_y_el_dictamen_negativo_es_evidencia(self):
        """T199 · Defecto que previene: un gate que aprueba «con reparos».

        Sin todas las comprobaciones y sin toda la evidencia declarada, el dictamen es
        NEGATIVO y no hay salida. El dictamen viaja con el error para que quede escrito.
        """
        declarado = gates.gate("gate:cierre-de-item", corpus=self.corpus)
        with self.assertRaises(ciclo.GateFallido) as capturado:
            ciclo.aplicar_gate(
                "gate:cierre-de-item", corpus=self.corpus, entrada={"item": "it-1"},
                evidencia=declarado["evidencia"], revisor="VER", autor="CON",
                comprobaciones_superadas=[declarado["comprobaciones"][0]["id"]],
            )
        error = capturado.exception
        self.assertEqual(error.codigo, "GATE_FALLIDO")
        self.assertEqual(error.dictamen["dictamen"], gates.NO_SUPERADO)
        self.assertIsNone(error.dictamen["salida"])
        self.assertTrue(error.dictamen["fallo_declarado"])
        superado = ciclo.aplicar_gate(
            "gate:cierre-de-item", corpus=self.corpus, entrada={"item": "it-1"},
            evidencia=declarado["evidencia"], revisor="VER", autor="CON",
            comprobaciones_superadas=[c["id"] for c in declarado["comprobaciones"]],
            salida="el item cierra",
        )
        self.assertEqual(superado["dictamen"], gates.SUPERADO)
        self.assertEqual(superado["salida"], "el item cierra")

    def test_47_ningun_gate_puede_ser_fuente_normativa(self):
        """T199 · Defecto que previene: un gate que escribe norma o ensancha el proceso.

        Dos mecanismos y dos pruebas: lo único que un dictamen escribe es su propio objeto
        en `dictamenes/`, y la ruta ANTES y DESPUÉS del gate es la misma. Añadir una
        capacidad a la ruta al pasar por un gate es ensanchar `b.16`.
        """
        import estado as motor
        self.assertTrue(ciclo.exigir_no_normativo(
            [motor.Escritura("dictamenes/dic-1.json", {"a": 1})],
        ))
        for prohibida in ("procesos/proceso.json", "rutas/rt-1.json",
                          "paquetes/pq-1.json", "items/it-1.json"):
            with self.assertRaises(ciclo.GateNormativo, msg=prohibida):
                ciclo.exigir_no_normativo([motor.Escritura(prohibida, {"a": 1})])
        marco = ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus)
        antes = ciclo.componer(marco, corpus=self.corpus)
        self.assertTrue(ciclo.exigir_no_amplia(antes, antes))
        ensanchada = ciclo.componer(marco, corpus=self.corpus,
                                    condiciones_verdaderas=["C-DIS"])
        with self.assertRaises(ciclo.GateNormativo) as capturado:
            ciclo.exigir_no_amplia(antes, ensanchada)
        self.assertTrue(
            any(a.startswith("DIS@") for a in capturado.exception.contexto["anadidas"]),
            capturado.exception.contexto["anadidas"],
        )

    def test_48_el_revisor_no_puede_ser_quien_construyo(self):
        """T199 · Defecto que previene: un dictamen firmado por el autor de lo juzgado.

        «revisión independiente de quien construyó» es criterio de satisfacción escrito en
        `b.16`, y sin revisor no hay dictamen que detenga nada.
        """
        declarado = gates.gate("gate:evidencia-suficiente", corpus=self.corpus)
        argumentos = {
            "corpus": self.corpus, "entrada": {}, "evidencia": declarado["evidencia"],
            "comprobaciones_superadas": [c["id"] for c in declarado["comprobaciones"]],
        }
        with self.assertRaises(ciclo.GateFallido):
            ciclo.aplicar_gate("gate:evidencia-suficiente", revisor="CON", autor="CON",
                               **argumentos)
        with self.assertRaises(ciclo.GateFallido):
            ciclo.aplicar_gate("gate:evidencia-suficiente", revisor="", autor="CON",
                               **argumentos)
        with self.assertRaises(ciclo.GateFallido):
            ciclo.aplicar_gate("gate:evidencia-suficiente", revisor="el sistema",
                               autor="CON", **argumentos)
        # EL AUTOR ES OBLIGATORIO, y omitirlo NO es la vía para revisarse a sí mismo.
        # Defecto que previene, medido por la auditoría independiente: con `autor`
        # opcional, los VEINTIDÓS gates del censo se superaban firmándolos uno mismo.
        with self.assertRaises(TypeError):
            ciclo.aplicar_gate("gate:evidencia-suficiente", revisor="CON", **argumentos)
        with self.assertRaises(ciclo.GateFallido):
            ciclo.aplicar_gate("gate:evidencia-suficiente", revisor="CON", autor="",
                               **argumentos)
        with self.assertRaises(ciclo.GateFallido):
            ciclo.aplicar_gate("gate:evidencia-suficiente", revisor="CON",
                               autor="el sistema", **argumentos)
        self.assertEqual(
            ciclo.aplicar_gate("gate:evidencia-suficiente", revisor="VER", autor="CON",
                               **argumentos)["dictamen"],
            gates.SUPERADO,
        )


# =========================================================================
# T200 · handoffs por `C5`
# =========================================================================
class Handoffs(BaseDelCiclo):

    def test_55_las_instancias_traen_los_once_campos_del_esquema(self):
        """T200 · Defecto que previene: un handoff al que le falta lo que hace falta.

        Los once obligatorios se DERIVAN de `esquemas/handoff.yaml`, no se escriben aquí, y
        se exigen tanto a las diecisiete de `circuitos/` como a las cinco de `§8.0`.
        """
        obligatorios = self.corpus.obligatorios_de("handoff")
        self.assertEqual(len(obligatorios), 11)
        catalogado = ciclo.catalogo(self.corpus)
        self.assertGreaterEqual(len(catalogado), 17 + 5)
        for identificador, datos in sorted(catalogado.items()):
            for campo in obligatorios:
                self.assertIn(campo, datos, identificador)
            self.assertIn(datos["de"], QUINCE, identificador)
            self.assertIn(datos["a"], QUINCE, identificador)

    def test_56_las_cinco_entregas_de_8_0_estan_materializadas(self):
        """T200 · Defecto que previene: una composición completa que no puede entregar nada.

        `§8.0` declara cinco entregas que `circuitos/` no tenía: `SIS`→`PLT`, `SIS`→`CON`,
        `SIS`→`VER`, `CON`→`ENT` y `ENT`→`VER`. Se comprueban una a una, por sus extremos.
        """
        esperadas = {
            "handoff:sis-a-plt": ("SIS", "PLT"),
            "handoff:sis-a-con": ("SIS", "CON"),
            "handoff:sis-a-ver": ("SIS", "VER"),
            "handoff:con-a-ent": ("CON", "ENT"),
            "handoff:ent-a-ver": ("ENT", "VER"),
        }
        catalogado = ciclo.catalogo(self.corpus)
        for identificador, (de, a) in sorted(esperadas.items()):
            self.assertIn(identificador, catalogado)
            self.assertEqual((catalogado[identificador]["de"],
                              catalogado[identificador]["a"]), (de, a), identificador)
        # Y la solicitud a `PLT` NO se lleva el source change entero (`I-04`).
        entrega = catalogado["handoff:sis-a-plt"]
        texto = " ".join(entrega["entrega"]).lower()
        self.assertIn("materializaci", texto)
        self.assertTrue(any("no incluye rama, commit, push ni pr" in c.lower()
                            for c in entrega["comprueba_al_recibir"]))

    def test_57_rechazar_no_cambia_la_custodia_y_devolver_si(self):
        """T200 · Defecto que previene: aceptar por cortesía y gastar una devolución.

        `C5`: quien recibe comprueba ANTES de tomar custodia. Rechazar deja el paquete en el
        emisor y NO cuenta para el freno; devolver, después del acuse, SÍ cuenta.
        """
        trazabilidad = {"item": "it-1", "paquete": "pq-1", "ruta": "rt-1"}
        entrega = ciclo.emitir(
            "handoff:con-a-ver", corpus=self.corpus,
            artefactos=["la rama con el cambio construido"],
            checkpoint="el estado del paquete y su base", trazabilidad=trazabilidad,
        )
        self.assertEqual(entrega["custodia"], "CON")
        rechazada = ciclo.rechazar(entrega, receptor="VER",
                                   motivo="faltan las diferencias declaradas")
        self.assertEqual(rechazada["custodia"], "CON")
        self.assertFalse(rechazada["cuenta_para_el_freno"])
        with self.assertRaises(ciclo.HandoffRechazado):
            ciclo.acusar(rechazada, comprobaciones_superadas=[], receptor="VER")
        acusada = ciclo.acusar(
            entrega, comprobaciones_superadas=entrega["comprueba_al_recibir"],
            receptor="VER",
        )
        self.assertEqual(acusada["custodia"], "VER")
        devuelta = ciclo.devolver(acusada, devolucion={
            "que_falta": "la comparación contra la especificación",
            "por_que_es_insuficiente": "sin ella no se puede juzgar fidelidad",
            "que_la_cerraria": "la tabla de diferencias declaradas",
            "evidencia": ["la captura del estado actual"],
        })
        self.assertTrue(devuelta["cuenta_para_el_freno"])
        self.assertEqual(devuelta["custodia"], "CON")

    def test_58_una_devolucion_sin_los_cuatro_campos_no_es_una_devolucion(self):
        """T200 · Defecto que previene: una devolución que es una opinión.

        `C5` lo dice con esas palabras: sin los cuatro campos se rechaza COMO devolución, y
        no cuenta para el freno.
        """
        entrega = ciclo.acusar(
            ciclo.emitir("handoff:con-a-ver", corpus=self.corpus,
                         artefactos=["la rama"], checkpoint="el estado",
                         trazabilidad={"item": "i", "paquete": "p", "ruta": "r"}),
            comprobaciones_superadas=ciclo.catalogo(self.corpus)["handoff:con-a-ver"][
                "comprueba_al_recibir"],
            receptor="VER",
        )
        for campo in handoffs.CAMPOS_DE_DEVOLUCION:
            devolucion = {c: "algo" for c in handoffs.CAMPOS_DE_DEVOLUCION}
            devolucion[campo] = ""
            with self.assertRaises(ciclo.DevolucionSinEvidencia, msg=campo) as capturado:
                ciclo.devolver(entrega, devolucion=devolucion)
            self.assertIn(campo, capturado.exception.contexto["faltan"])

    def test_59_la_entrega_es_durable_y_el_receptor_reanuda_sin_hablar_con_el_emisor(self):
        """T200 · Defecto que previene: un handoff que sólo existe en la conversación.

        La entrega se escribe por el motor y su reanudación trae artefactos, checkpoint,
        trazabilidad y la siguiente acción exacta.
        """
        rt = self.abrir_runtime()
        entrega = ciclo.emitir(
            "handoff:arq-a-con", corpus=self.corpus,
            artefactos=["el plan técnico con su radio medido"],
            checkpoint="las decisiones del Owner captadas",
            trazabilidad={"item": "it-1", "paquete": "pq-1", "ruta": "rt-1"},
        )
        from ciclo import durable
        durable.escribir(
            rt.almacen, clase="ciclo.handoff.emitido", motivo="prueba",
            objetos={handoffs.ruta_de(entrega["id"]): entrega},
        )
        leida = rt.almacen.leer(handoffs.ruta_de(entrega["id"]))
        self.assertEqual(leida["estado"], "emitido")
        reanudacion = ciclo.reanudacion(leida)
        self.assertEqual(reanudacion["trazabilidad"]["item"], "it-1")
        self.assertTrue(reanudacion["artefactos"])
        self.assertIn("comprueba", reanudacion["siguiente_accion"])
        with self.assertRaises(ciclo.HandoffIncompleto):
            ciclo.emitir("handoff:arq-a-con", corpus=self.corpus, artefactos=[],
                         checkpoint="x", trazabilidad={"item": "i", "paquete": "p",
                                                       "ruta": "r"})


# =========================================================================
# T201 · cierre, obligaciones y trabajo derivado
# =========================================================================
class Cierre(BaseDelCiclo):

    def test_65_cancelar_un_paquete_no_retira_su_obligacion(self):
        """T201 · Defecto que previene: cerrar un item vaciando su cola.

        Regla dura 1 de `00-OBLIGACIONES`: cancelar detiene la ejecución y deja la
        obligación HUÉRFANA. Un item con todos sus paquetes cancelados y ninguna retirada
        aprobada no puede cerrar nunca.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.plan_completo(rt)
        for paquete in plan["paquetes"]:
            rt.cancelar(paquete, motivo="se retira el trabajo", autoridad="OWNER")
        cerrador = ciclo.Cierre(rt, corpus=self.corpus)
        with self.assertRaises(ciclo.ObligacionHuerfana) as capturado:
            cerrador.cerrar(
                plan, integracion={"propietario_global": plan["propietario_global"],
                                   "declaracion": "todo integrado"},
                aprendizaje="none",
            )
        self.assertTrue(capturado.exception.contexto["huerfanas"])

    def test_66_DSP_no_retira_y_la_retirada_exige_autoridad_y_efecto(self):
        """T201 · Defecto que previene: reducir el alcance por la puerta de atrás.

        Regla dura 2: DSP NO RETIRA. Y toda retirada identifica quién tuvo autoridad y
        explica CÓMO AFECTA al resultado perseguido.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.plan_completo(rt)
        obligacion = plan["obligaciones"][0]["id"]
        with self.assertRaises(ciclo.RetiradaSinAutoridad):
            ciclo.resolver_obligaciones(plan, retiradas=[
                {"obligacion": obligacion, "autoridad": "DSP", "como_afecta": "nada"},
            ])
        with self.assertRaises(ciclo.RetiradaSinAutoridad):
            ciclo.resolver_obligaciones(plan, retiradas=[
                {"obligacion": obligacion, "autoridad": "OWNER", "como_afecta": ""},
            ])
        resueltas = ciclo.resolver_obligaciones(plan, retiradas=[
            {"obligacion": obligacion, "autoridad": "OWNER",
             "como_afecta": "el resultado pierde la evidencia de verificación"},
        ])
        estados = {r["obligacion"]: r["estado"] for r in resueltas}
        self.assertEqual(estados[obligacion], "retirada")

    def test_67_el_informe_separa_satisfechas_de_retiradas_y_no_las_suma(self):
        """T201 · Defecto que previene: informar de que se entregó lo que se eliminó.

        `gate:cierre-de-item`, comprobación `informe-separa`. El informe lleva DOS cifras y
        no lleva total, y declarar una obligación satisfecha Y retirada es error.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.plan_completo(rt)
        obligaciones = [o["id"] for o in plan["obligaciones"]]
        resueltas = ciclo.resolver_obligaciones(
            plan, satisfechas=obligaciones[:1],
            retiradas=[{"obligacion": obligaciones[-1], "autoridad": "OWNER",
                        "como_afecta": "se renuncia a esa evidencia"}],
        )
        informe = ciclo.cierre.informe(plan, resueltas, paquetes={})
        self.assertEqual(informe["cuantas_satisfechas"], 1)
        self.assertEqual(informe["cuantas_retiradas"], 1)
        self.assertNotIn("total", informe)
        with self.assertRaises(ciclo.CierreBloqueado):
            ciclo.resolver_obligaciones(
                plan, satisfechas=[obligaciones[0]],
                retiradas=[{"obligacion": obligaciones[0], "autoridad": "OWNER",
                            "como_afecta": "x"}],
            )

    def test_68_el_cierre_lo_declara_el_propietario_global_y_no_DSP(self):
        """T201 · Defecto que previene: que DSP declare la integración semántica.

        `00-OBLIGACIONES`: «DSP verifica; no declara». Sin la firma del propietario global,
        el gate no pasa; con ella y con las obligaciones resueltas, el item cierra.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.plan_completo(rt)
        for _vuelta in range(len(plan["paquetes"]) + 1):
            ciclo.barrido(rt, origen="prueba")
        cerrador = ciclo.Cierre(rt, corpus=self.corpus)
        obligaciones = [o["id"] for o in plan["obligaciones"]]
        with self.assertRaises(ciclo.CierreBloqueado) as capturado:
            cerrador.cerrar(plan, satisfechas=obligaciones,
                            integracion={"propietario_global": "DSP",
                                         "declaracion": "yo lo declaro"},
                            aprendizaje="none")
        self.assertTrue(any("integracion" in f for f in capturado.exception.contexto["fallos"]))
        cierre = cerrador.cerrar(
            plan, satisfechas=obligaciones,
            integracion={"propietario_global": plan["propietario_global"],
                         "declaracion": "integración semántica completa"},
            aprendizaje="none",
        )
        self.assertEqual(cierre["salida"], "completado")
        self.assertEqual(cierre["informe"]["huerfanas"], [])
        leido = rt.almacen.leer("cierres/" + cierre["id"] + ".json")
        self.assertEqual(leido["salida"], "completado")

    def test_69_pausar_exige_la_siguiente_accion_exacta_y_escalar_la_autoridad(self):
        """T201 · Defecto que previene: una pausa que obliga a reconstruir el contexto.

        `§12`: completar unidad segura · verificar · persistir · dejar la siguiente acción
        exacta. Y `b.14.3`: escalar exige nombrar a quién.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.plan_completo(rt)
        cerrador = ciclo.Cierre(rt, corpus=self.corpus)
        with self.assertRaises(ciclo.CierreBloqueado):
            cerrador.pausar(plan, motivo="presupuesto", siguiente_accion="")
        pausa = cerrador.pausar(plan, motivo="presupuesto agotado",
                                siguiente_accion="retomar el paquete " + plan["paquetes"][0])
        self.assertEqual(pausa["salida"], "pausado")
        self.assertIn(plan["paquetes"][0], pausa["siguiente_accion"])
        with self.assertRaises(ciclo.CierreBloqueado):
            cerrador.escalar(plan, motivo="dos posturas", autoridad="")
        escalada = cerrador.escalar(plan, motivo="dos vetos incompatibles",
                                    autoridad="OWNER",
                                    posturas=["SEG bloquea", "ENT necesita entregar"])
        self.assertEqual(escalada["salida"], "escalado")
        self.assertEqual(escalada["autoridad"], "OWNER")

    def test_70_el_trabajo_derivado_conserva_el_enlace_con_su_origen(self):
        """T201 · Defecto que previene: un item derivado huérfano de su causa.

        Se abre trabajo derivado y se comprueba que desde el item NUEVO se llega al de
        ORIGEN recorriendo el ESTADO, sin leer ningún texto.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.plan_completo(rt)
        cerrador = ciclo.Cierre(rt, corpus=self.corpus)
        planificador = ciclo.Planificador(rt, corpus=self.corpus)
        marco_nuevo = ciclo.encuadrar(self.repo, entrada_base(
            expresion_literal="y ademas hay que medir el hueco que dejo",
            resultado_perseguido="la distancia entre lo esperado y lo real, medida",
            materia="expectativa-no-alcanzada", estado_del_objeto="existe",
        ), corpus=self.corpus)
        ruta_nueva = ciclo.componer(marco_nuevo, corpus=self.corpus)
        derivado = cerrador.derivar(
            plan, encuadre_derivado=marco_nuevo, ruta_derivada=ruta_nueva,
            planificador=planificador,
            orden_por_capacidad=self.orden(
                sorted({p["capacidad"] for p in ruta_nueva["participantes"]})),
            motivo="la corrección deja un hueco de producto que hay que medir",
        )
        self.assertNotEqual(derivado["plan"]["item"], plan["item"])
        enlace = cerrador.enlace_de_derivacion(derivado["plan"]["item"])
        self.assertIsNotNone(enlace)
        self.assertEqual(enlace["origen"], plan["item"])
        self.assertEqual(derivado["plan"]["derivado_de"]["item"], plan["item"])


# =========================================================================
# T202 · el corpus, el analizador YAML y el determinismo
# =========================================================================
class CorpusYDeterminismo(BaseDelCiclo):

    def test_75_el_analizador_acotado_coincide_con_pyyaml_bloque_a_bloque(self):
        """T202 · Defecto que previene: un analizador propio que lee el corpus a su manera.

        El kernel es stdlib pura y por eso el analizador es propio. La equivalencia no se
        promete: se mide sobre los doscientos y pico bloques canónicos del corpus real y
        sobre todos los ficheros de `esquemas/`. Sin PyYAML instalado se comprueba lo que se
        puede sin él: que TODO bloque se analiza y que ninguno queda vacío.
        """
        try:
            import yaml
        except ImportError:
            yaml = None
        analizados = 0
        for tipo, datos, ruta, linea in self.corpus.todos_los_bloques():
            analizados += 1
            self.assertIsInstance(datos, (dict, list), (ruta, linea, tipo))
            self.assertTrue(datos, (ruta, linea, tipo))
        self.assertGreater(analizados, 200)
        if yaml is None:
            self.skipTest("PyYAML no está instalado: se comprobó la parte estructural")
        for relativa in self.corpus._documentos():
            texto = self.corpus._texto(relativa)
            crudos = re.split(r"^```yaml ads:[a-z-]+\s*$", texto, flags=re.M)[1:]
            for crudo in crudos:
                cuerpo = crudo.split("\n```", 1)[0]
                self.assertEqual(modulo_corpus.analizar(cuerpo, relativa),
                                 yaml.safe_load(cuerpo), relativa)
        directorio = os.path.join(KERNEL, "esquemas")
        for nombre in sorted(os.listdir(directorio)):
            if not nombre.endswith(".yaml"):
                continue
            with open(os.path.join(directorio, nombre), encoding="utf-8") as fichero:
                texto = fichero.read()
            self.assertEqual(modulo_corpus.analizar(texto, nombre),
                             yaml.safe_load(texto), nombre)

    def test_76_el_analizador_falla_cerrado_ante_lo_que_no_cubre(self):
        """T202 · Defecto que previene: ignorar en silencio lo que no se entiende.

        Anclas, alias, etiquetas, documentos múltiples, tabuladores y claves duplicadas
        levantan `CORPUS_ILEGIBLE` con su fichero. Un analizador que ignora lo que no
        entiende compone rutas desde procesos leídos a medias.
        """
        casos = [
            "a: &ancla 1\n",
            "a: *alias\n",
            "a: !!str 1\n",
            "---\na: 1\n",
            "a:\n\tb: 1\n",
            "a: 1\na: 2\n",
            "a: [1, 2\n",
            "a: 'sin cerrar\n",
        ]
        for crudo in casos:
            with self.assertRaises(ciclo.CorpusIlegible, msg=crudo):
                modulo_corpus.analizar(crudo, "(prueba)")

    def test_77_las_quince_capacidades_del_arbol_y_de_18_coinciden(self):
        """T202 · Defecto que previene: una capacidad inventada o una perdida.

        El árbol de `capacidades/` y la lista de `§18` se contrastan; no se copia una en la
        otra. `DEU`, `DEP` y `AUD` son PROCESOS y no están entre ellas.
        """
        self.assertEqual(self.corpus.exigir_quince(), QUINCE)
        for proceso in ("AUD", "DEU", "DEP"):
            self.assertNotIn(proceso, QUINCE)
            self.assertIn("proceso:" + proceso, self.corpus.procesos())

    def test_78_dos_ejecuciones_desde_cwd_distintos_dan_bytes_identicos(self):
        """T202 · Defecto que previene: una salida que depende de dónde se invocó.

        `I-g3`. Se ejecuta la CLI dos veces, desde dos directorios de trabajo distintos, y
        se comparan los bytes de su salida `--json`.
        """
        entorno = dict(os.environ)
        argumentos = [
            sys.executable, CLI, "--repo", self.repo, "--json", "componer",
            "--clase", "candidato", "--expresion", "no se puede exportar la tabla",
            "--canal", "chat", "--resultado",
            "el usuario descarga la tabla completa en formato CSV",
            "--evidencia", "un CSV con las mismas filas", "--anclaje",
            "--materia", "capacidad-ausente", "--estado-del-objeto", "no-existe",
            "--condicion", "C-DIS",
        ]
        primera = subprocess.run(argumentos, cwd=RAIZ, capture_output=True,
                                 timeout=SEGUNDOS_DE_ESPERA, env=entorno)
        otro = tempfile.mkdtemp(prefix="ads-cwd-")
        self.addCleanup(shutil.rmtree, otro, True)
        segunda = subprocess.run(argumentos, cwd=otro, capture_output=True,
                                 timeout=SEGUNDOS_DE_ESPERA, env=entorno)
        self.assertEqual(primera.returncode, 0, primera.stderr.decode("utf-8", "replace"))
        self.assertEqual(segunda.returncode, 0, segunda.stderr.decode("utf-8", "replace"))
        self.assertEqual(primera.stdout, segunda.stdout)
        self.assertNotIn(RAIZ.encode("utf-8"), primera.stdout)

    def test_79_la_cli_distingue_uso_incorrecto_de_fallo_de_la_operacion(self):
        """T202 · Defecto que previene: confundir un tecleo con un fallo del ciclo.

        0 éxito · 1 error tipado · 2 uso incorrecto, como en los otros dos puntos
        ejecutables. Y las órdenes son exactamente las siete declaradas.
        """
        import importlib
        modulo = importlib.import_module("ads_ciclo")
        self.assertEqual(sorted(modulo.ORDENES), sorted([
            "ciclo", "componer", "continuar", "encuadrar", "macrocircuito",
            "materializar", "planificar",
        ]))
        self.assertEqual(modulo.main(["encuadrar"]), modulo.USO)
        self.assertEqual(modulo.main([]), modulo.USO)
        # REGRESIÓN MEDIDA: `planificar` declara `--orden` y el subanalizador guardaba en el
        # MISMO destino, de modo que el valor por defecto de la opción pisaba el nombre del
        # subcomando y la orden salía por «uso incorrecto» sin haber hecho nada. Las tres
        # órdenes que declaran `--orden` se recorren enteras, y con el ciclo despachando.
        import contextlib
        import io as _io
        comunes = ["--repo", self.repo, "planificar", "--clase", "candidato",
                   "--expresion", "no se puede exportar la tabla", "--canal", "chat",
                   "--resultado", "el usuario descarga la tabla completa en formato CSV",
                   "--evidencia", "un CSV con las mismas filas", "--anclaje",
                   "--materia", "capacidad-ausente",
                   "--estado-del-objeto", "no-existe",
                   "--argumento=/bin/sh", "--argumento=-c", "--argumento=exit 0"]
        with contextlib.redirect_stdout(_io.StringIO()) as capturada:
            self.assertEqual(modulo.main(comunes), modulo.EXITO)
        self.assertIn("plan          pl-", capturada.getvalue())
        with contextlib.redirect_stdout(_io.StringIO()) as capturada:
            self.assertEqual(
                modulo.main(["--repo", self.repo, "ciclo",
                             "--adaptador-local", self.espacio]),
                modulo.EXITO,
            )
        self.assertIn("completado", capturada.getvalue())
        with contextlib.redirect_stdout(_io.StringIO()) as capturada:
            self.assertEqual(modulo.main(["--repo", self.repo, "continuar"]), modulo.EXITO)
        self.assertIn("huella        sha256:", capturada.getvalue())
        self.assertEqual(
            modulo.main(["--repo", self.repo, "encuadrar", "--clase", "inventada",
                         "--expresion", "x", "--canal", "y"]),
            modulo.FALLO,
        )
        # El censo IMPRIME, y esta salida se publica como evidencia: se captura para que la
        # evidencia de la batería no lleve el volcado de una orden de la CLI.
        import contextlib
        import io as _io
        with contextlib.redirect_stdout(_io.StringIO()) as capturada:
            self.assertEqual(modulo.main(["macrocircuito", "--censo"]), modulo.EXITO)
        self.assertIn("instalación en proyecto nuevo", capturada.getvalue())

    def test_80_todo_error_del_ciclo_lleva_codigo_estable_y_forma_determinista(self):
        """T202 · Defecto que previene: una evidencia que depende del texto castellano.

        El contrato estable es el `codigo`, no el detalle. Y ninguna forma serializada lleva
        una ruta absoluta de la máquina.
        """
        from ciclo import errores as modulo_errores
        self.assertEqual(len(modulo_errores.CODIGOS), len(set(modulo_errores.CODIGOS)))
        for clase in modulo_errores.CLASES:
            self.assertRegex(clase.CODIGO, r"^[A-Z][A-Z_0-9]*$")
        error = ciclo.CicloInconsistente("detalle", ruta=os.path.join(self.repo, "estado",
                                                                     "canonico", "x.json"))
        self.assertEqual(error.a_dict()["codigo"], "CICLO_INCONSISTENTE")
        self.assertNotIn(self.repo, json.dumps(error.a_dict(), ensure_ascii=False))
        self.assertTrue(error.a_dict()["ruta"].startswith("estado/"))


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de `test_runtime.py`, no importado: la batería del ciclo no puede depender de
    otra batería para poder ejecutarse. La salida se PUBLICA como evidencia, y la regla del
    repositorio es que los artefactos generados sean deterministas: «Ran 40 tests in
    12.481s» cambia en cada ejecución y ensuciaría el árbol en cada comprobación, hasta que
    alguien dejara de mirarlo.
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
