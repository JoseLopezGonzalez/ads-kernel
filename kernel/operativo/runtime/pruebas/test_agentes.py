#!/usr/bin/env python3
"""test_agentes — el PASO 4 de `C4` y la política de `C2`, sobre catálogo y corpus REALES.

`T226`–`T235`. Instancia el paso 4 de
[`C4-MATERIALIZACION.md`](../../contratos/C4-MATERIALIZACION.md) —«ASIGNAR AGENTES: por cada
rol, aplicar la política de `C2`. Registrar modelo elegido, descartados y motivo»— y los
SEIS pasos de [`C2-AGENTES-Y-MODELOS.md`](../../contratos/C2-AGENTES-Y-MODELOS.md), más el
corte por `execution_slots` de `b.11`, cuya unidad es el AGENTE y no el rol.

CINCO REGLAS QUE ESTA BATERÍA SE IMPONE:

  1. NINGUNA PRUEBA MIRA UN FICHERO Y SE DA POR SATISFECHA. Todas materializan equipos sobre
     el corpus REAL del kernel y sobre un `PROFILE.md` REAL de un control repo temporal, que
     es donde `C2` sitúa el catálogo de modelos del proyecto.

  2. NINGÚN NOMBRE COMERCIAL. `K0.8` prohíbe que un proveedor, un modelo o una herramienta
     de marca aparezcan en `kernel/` o en `packs/`, y estas pruebas viven en `kernel/`. Los
     modelos del catálogo se llaman `modelo:alfa`, `modelo:beta`, `modelo:gamma`,
     `modelo:delta` y `modelo:epsilon`, y son evidentemente inventados.

  3. LOS DESCARTES SE VERIFICAN UNO A UNO. No basta con que exista una lista de descartados:
     `T232` recorre los VEINTIÚN perfiles del kernel, lee el motivo de cada descarte y lo
     RECALCULA contra el catálogo. Un motivo que no se sostiene es un fallo.

  4. LO QUE SE CORRIGE TIENE QUE PODER PONERSE ROJO. `T235` copia el árbol, BORRA la regla
     —el filtro por ejes, el filtro por herramientas, el corte por agente, la precedencia de
     `independientes`, el orden de `C2`— y comprueba en un PROCESO REAL que la prueba que la
     cubre FALLA. Una propiedad que se puede borrar sin que ninguna prueba parpadee no está
     probada, y ésa fue la lección del corte anterior.

  5. DETERMINISMO Y FORMA. La salida se PUBLICA como evidencia: el resumen no lleva duración
     (`_RunnerDeterminista`, COPIADO de `test_ciclo.py`, no importado, por la misma razón).

    python3 kernel/operativo/runtime/pruebas/test_agentes.py

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

try:
    import catalogo_de_prueba
    import ciclo
    import estado as motor_de_estado
    from ciclo import agentes, durable, equipos, errores
except ImportError as exc:      # el paquete todavía no está: que se vea por qué
    print(f"no se encuentra el paquete `ciclo` bajo {RUNTIME}: {exc}", file=sys.stderr)
    raise

SEGUNDOS_DE_ESPERA = 300

# La composición REAL de `DIS` sobre la que se mide el corte: cuatro roles obligatorios, un
# par `combinables` bajo condición y DOS entradas de `independientes`.
COMPOSICION_DE_DIS = "composicion:dis-gap-de-diseno"
CONDICION_DE_LA_COMBINACION = "el gap afecta a una sola superficie"
COMPOSICION_DE_DSP = "composicion:dsp-supervisor"

# El bloque que se AÑADE a una COPIA del corpus para medir el cierre de las combinaciones:
# `A`+`B` y `B`+`C` declarados combinables, con `C` independiente de `A`. Encadenarlas
# metería a `A` y a `C` en el mismo agente, que es lo que `C4` prohíbe.
COMPOSICION_ENCADENADA = """
```yaml ads:composicion
id: composicion:dsp-cadena-de-prueba
capacidad: DSP
clase_de_trabajo: "cadena de combinables para medir el cierre de C4 paso 5"
condicion: >
  Se ejercita el cierre transitivo de las combinaciones declaradas, para comprobar que
  encadenarlas no puede colar en un mismo agente dos roles independientes.
roles:
  - rol: DSP/enrutamiento
    obligatorio: true
    agentes: "1"
  - rol: DSP/estado
    obligatorio: true
    agentes: "1"
  - rol: DSP/supervision
    obligatorio: true
    agentes: "1"
combinables:
  - roles: [DSP/enrutamiento, DSP/estado]
    motivo: "ambos son mecánicos y deterministas y ninguno juzga contenido"
  - roles: [DSP/estado, DSP/supervision]
    motivo: "declarada a propósito para que encadenarla choque con independientes"
independientes:
  - rol: DSP/supervision
    de: [DSP/enrutamiento]
    motivo: "quien compone y despacha la ruta es parte interesada en su propia supervisión"
ampliacion: "no se amplía: existe para medir el cierre de las combinaciones."
reduccion: "no admite reducción: los tres roles son el objeto de la medida."
retirada: "al terminar la comprobación del cierre."
```
"""


def copiar_arbol(destino):
    """Una COPIA REAL de `kernel/operativo` bajo `<destino>/kernel/operativo`.

    No es un fixture que sustituya comportamiento: es el mismo corpus y el mismo runtime,
    en otro sitio, para poder alterarlos sin tocar el árbol de trabajo.
    """
    copia = os.path.join(destino, "kernel", "operativo")
    os.makedirs(os.path.dirname(copia), exist_ok=True)
    shutil.copytree(KERNEL, copia,
                    ignore=shutil.ignore_patterns("__pycache__", "evidencia"))
    return copia


class BaseDeAgentes(unittest.TestCase):
    """El corpus real del kernel y un control repo real con su catálogo de modelos."""

    @classmethod
    def setUpClass(cls):
        cls.corpus = ciclo.Corpus(KERNEL)
        cls.politica = agentes.Politica(cls.corpus)

    def setUp(self):
        self.repo = tempfile.mkdtemp(prefix="ads-agentes-")
        self.addCleanup(shutil.rmtree, self.repo, True)
        catalogo_de_prueba.escribir(self.repo, self.politica, self.corpus)
        self.catalogo = agentes.cargar_catalogo(self.repo, politica=self.politica)

    def catalogo_de(self, *ids):
        """Un catálogo del proyecto con SÓLO los modelos nombrados. Sigue siendo real."""
        otro = tempfile.mkdtemp(prefix="ads-catalogo-")
        self.addCleanup(shutil.rmtree, otro, True)
        catalogo_de_prueba.escribir(otro, self.politica, self.corpus, seleccion=ids)
        return otro, agentes.cargar_catalogo(otro, politica=self.politica)

    def equipo_de_dis(self, *, slots=99, repo=None):
        return equipos.materializar(
            "DIS", corpus=self.corpus, control_repo=repo or self.repo,
            composiciones_verdaderas=[COMPOSICION_DE_DIS], slots=slots,
            condiciones_de_rol=[CONDICION_DE_LA_COMBINACION],
        )


# =========================================================================
# T226 · el paso 4 de `C4` sobre una composición con VARIOS roles
# =========================================================================
class AsignacionDeAgentes(BaseDeAgentes):

    def test_01_una_composicion_con_varios_roles_recibe_agente_modelo_y_traza(self):
        """T226 · Defecto que previene: un equipo cuyo eje AGENTE se declara en prosa.

        `C4` paso 4 no es documentación: por cada rol expandido hay que aplicar la política
        de `C2` y REGISTRAR el modelo elegido, los descartados y el motivo de cada descarte.
        Se mide sobre `composicion:dis-gap-de-diseno`, que tiene CUATRO roles obligatorios,
        tres perfiles distintos y un par combinable, y se comprueba la cadena entera:
        paquete → composición → rol → perfil → agente → modelo → slot.
        """
        equipo = self.equipo_de_dis(slots=99, repo=self.repo)
        self.assertEqual(equipo["composicion"], COMPOSICION_DE_DIS)
        self.assertEqual(equipo["estado"], "materializado")
        self.assertEqual(len(equipo["roles"]), 4)
        self.assertTrue(equipo["catalogo"]["declarado"])
        self.assertEqual(equipo["catalogo"]["sede"], "PROFILE.md")

        cadena = {r["rol"]: (r["perfil"], r["agente"], r["modelo"], r["slot"])
                  for r in equipo["roles"]}
        # La cadena COMPLETA, y ninguna pieza vacía.
        for rol, (perfil, agente, modelo, slot) in cadena.items():
            self.assertTrue(perfil and perfil.startswith("perfil:"), rol)
            self.assertTrue(agente and agente.startswith("ag-"), rol)
            self.assertTrue(modelo and modelo.startswith("modelo:"), rol)
            self.assertIsInstance(slot, int)
            self.assertEqual(perfil, self.politica.perfil_de_rol(rol))
        # El perfil sale del CONTRATO DEL ROL, no del nombre del rol.
        self.assertEqual(cadena["DIS/critica-visual"][0], "perfil:critica-independiente")
        self.assertEqual(cadena["DIS/diseno-visual"][0], "perfil:diseno-visual")
        self.assertEqual(cadena["DIS/sistema-de-diseno"][0], "perfil:sistema-de-diseno")
        self.assertEqual(cadena["DIS/revision-de-fidelidad"][0], "perfil:verificacion")

        # El MODELO elegido es el que sale de la clave de orden de `C2` paso 4, y se
        # escribe aquí a mano para que cambiarla ponga la prueba roja:
        #   a) eje dominante  b) dentro del techo de `coste`  c) coste  d) identificador.
        # `perfil:critica-independiente` exige `critica: maximo` (fuera `modelo:beta`),
        # `contexto: amplio` y techo `alto`: quedan `alfa` (sin-techo, FUERA del techo),
        # `gamma` y `delta` (los dos `contenido`) y `epsilon` (`alto`). Empatan en el eje
        # dominante `razonamiento`, los tres últimos están dentro del techo, y entre
        # `delta` y `gamma` —mismo coste— gana el identificador.
        self.assertEqual(cadena["DIS/critica-visual"][2], "modelo:delta")
        # `perfil:direccion-artistica` no entra en esta composición, pero `diseno-visual`
        # y `sistema-de-diseno` exigen `vision: requerida` y la herramienta de imágenes en
        # el segundo caso; el par combinable comparte UN agente y UN modelo.
        self.assertEqual(cadena["DIS/diseno-visual"][1],
                         cadena["DIS/sistema-de-diseno"][1])
        self.assertEqual(cadena["DIS/diseno-visual"][2],
                         cadena["DIS/sistema-de-diseno"][2])

        # El REGISTRO del paso 4, rol a rol, con descartados y motivo.
        registros = {a["rol"]: a for a in equipo["asignaciones"]}
        self.assertEqual(sorted(registros), sorted(cadena))
        for rol, registro in registros.items():
            self.assertEqual(registro["estado"], "asignado")
            self.assertEqual(registro["perfil"], self.politica.perfil_de_rol(rol))
            self.assertEqual(registro["catalogo"], self.catalogo.huella)
            self.assertTrue(registro["descartados"], rol)
            for descarte in registro["descartados"]:
                self.assertIn(descarte["modelo"], self.catalogo.ids)
                self.assertTrue(descarte["motivo"])
                self.assertTrue(descarte["regla"].startswith("`C2` paso"))
            self.assertTrue(registro["eje_dominante"]["eje"] in self.politica.ejes)
        # Y la traza vive en el objeto DURABLE, no en la conversación: el equipo se
        # identifica por su contenido, y el contenido lleva la asignación.
        self.assertTrue(equipo["id"].startswith("eq-"))
        self.assertIn("asignaciones", equipo)

    def test_02_la_seleccion_es_determinista_y_se_repite_byte_a_byte(self):
        """T227 · Defecto que previene: una asignación que depende de quién la calculó.

        `C2`: «mismo perfil y mismo catálogo instalado producen la misma elección». Se
        repite la materialización completa, se repite la selección suelta, y se repite en
        OTRO PROCESO con OTRO `cwd`: los tres tienen que dar lo mismo, byte a byte.
        """
        primero = self.equipo_de_dis()
        for _ in range(4):
            self.assertEqual(json.dumps(self.equipo_de_dis(), sort_keys=True,
                                        ensure_ascii=False),
                             json.dumps(primero, sort_keys=True, ensure_ascii=False))
        exigencia = self.politica.exigencia_de_perfil("perfil:sistema")
        elecciones = {json.dumps(agentes.seleccionar(
            exigencia, self.catalogo, politica=self.politica), sort_keys=True,
            ensure_ascii=False) for _ in range(5)}
        self.assertEqual(len(elecciones), 1)

        # Y en OTRO proceso, desde OTRO directorio: la raíz se deriva de `__file__`.
        guion = os.path.join(self.repo, "repetir.py")
        with open(guion, "w", encoding="utf-8") as manejador:
            manejador.write(
                "import json, sys\n"
                "sys.path.insert(0, " + repr(RUNTIME) + ")\n"
                "import ciclo\n"
                "equipo = ciclo.materializar('DIS', corpus=ciclo.Corpus(" + repr(KERNEL)
                + "), control_repo=" + repr(self.repo) + ",\n"
                "    composiciones_verdaderas=[" + repr(COMPOSICION_DE_DIS) + "],\n"
                "    condiciones_de_rol=[" + repr(CONDICION_DE_LA_COMBINACION) + "],\n"
                "    slots=99)\n"
                "print(json.dumps(equipo, sort_keys=True, ensure_ascii=False))\n")
        otro = tempfile.mkdtemp(prefix="ads-cwd-")
        self.addCleanup(shutil.rmtree, otro, True)
        salidas = set()
        for cwd in (RAIZ, otro, os.sep):
            proceso = subprocess.run([sys.executable, guion], cwd=cwd, capture_output=True,
                                     text=True, timeout=SEGUNDOS_DE_ESPERA)
            self.assertEqual(proceso.returncode, 0, proceso.stderr)
            salidas.add(proceso.stdout.strip())
        self.assertEqual(len(salidas), 1)
        self.assertEqual(json.loads(salidas.pop())["id"], primero["id"])

    def test_03_un_modelo_que_no_cumple_un_eje_se_descarta_con_su_motivo(self):
        """T228 · Defecto que previene: ocupar un rol con un modelo que no cumple el perfil.

        `C2` paso 2: «los modelos que CUMPLEN O SUPERAN cada exigencia del perfil. Un modelo
        sin visión no puede ocupar un rol que declara `vision: requerida`, por barato que
        sea». `modelo:beta` es el más barato del catálogo y le falta UN escalón en `critica`:
        para `perfil:sistema` —que exige `critica: maximo`— queda descartado, el motivo
        nombra el eje, lo exigido y lo ofrecido, y el paquete queda BLOQUEADO si es el único.
        """
        exigencia = self.politica.exigencia_de_perfil("perfil:sistema")
        registro = agentes.seleccionar(exigencia, self.catalogo, politica=self.politica)
        descarte = [d for d in registro["descartados"] if d["modelo"] == "modelo:beta"]
        self.assertEqual(len(descarte), 1)
        self.assertIn("el eje `critica` exige `maximo`", descarte[0]["motivo"])
        self.assertIn("el modelo ofrece `alto`", descarte[0]["motivo"])
        self.assertEqual(descarte[0]["regla"], agentes.REGLA_EJES)
        self.assertNotEqual(registro["modelo"], "modelo:beta")

        # Y con `modelo:beta` como ÚNICO modelo del catálogo, el rol NO se ocupa a medias:
        # `C2` paso 6 manda bloquear nombrando qué capacidad de modelo falta.
        repo, catalogo = self.catalogo_de("modelo:beta")
        solo = agentes.seleccionar(exigencia, catalogo, politica=self.politica)
        self.assertEqual(solo["estado"], "bloqueado")
        self.assertIsNone(solo["modelo"])
        self.assertIn("eje `critica` al nivel `maximo`", solo["falta"])
        # El texto de `degradacion_permitida` viaja VERBATIM para quien tenga que decidir,
        # y NO se interpreta: `perfil:sistema` dice «ninguna».
        self.assertIn("ninguna", solo["degradacion_permitida"].lower())
        equipo = equipos.materializar(
            "SIS", corpus=self.corpus, control_repo=repo,
            composiciones_verdaderas=["composicion:sis-cambio"], slots=4)
        self.assertEqual(equipo["estado"], "bloqueado")
        self.assertEqual(equipo["roles"], [])
        with self.assertRaises(ciclo.RolSinAgente):
            equipos.exigir_agentes_asignados(equipo)

    def test_04_un_modelo_sin_la_herramienta_o_el_contexto_declarados_se_descarta(self):
        """T229 · Defecto que previene: un agente que no puede hacer lo que el rol necesita.

        `C2` paso 3: «los que ofrecen las herramientas declaradas y el tamaño de contexto».
        `modelo:gamma` cumple los siete ejes y NO ofrece `lectura de imágenes`;
        `modelo:delta` cumple los siete ejes y su contexto es `amplio`. Los dos se descartan
        donde el perfil los exige, y el motivo nombra exactamente lo que falta.
        """
        exigencia = self.politica.exigencia_de_perfil("perfil:direccion-artistica")
        self.assertIn(catalogo_de_prueba.HERRAMIENTA_DE_VISION, exigencia["herramientas"])
        registro = agentes.seleccionar(exigencia, self.catalogo, politica=self.politica)
        por_modelo = {d["modelo"]: d for d in registro["descartados"]}
        self.assertIn("modelo:gamma", por_modelo)
        self.assertEqual(por_modelo["modelo:gamma"]["regla"], agentes.REGLA_HERRAMIENTAS)
        self.assertIn("no ofrece la herramienta declarada `"
                      + catalogo_de_prueba.HERRAMIENTA_DE_VISION + "`",
                      por_modelo["modelo:gamma"]["motivo"])

        contexto = self.politica.exigencia_de_perfil("perfil:sistema-de-diseno")
        self.assertEqual(contexto["contexto"], "maximo")
        otro = agentes.seleccionar(contexto, self.catalogo, politica=self.politica)
        por_modelo = {d["modelo"]: d for d in otro["descartados"]}
        self.assertIn("modelo:delta", por_modelo)
        self.assertEqual(por_modelo["modelo:delta"]["regla"], agentes.REGLA_CONTEXTO)
        self.assertIn("el contexto exige `maximo` y el modelo ofrece `amplio`",
                      por_modelo["modelo:delta"]["motivo"])

        # Con SÓLO `modelo:gamma`, el rol que exige leer imágenes queda BLOQUEADO y se
        # nombra la herramienta que falta. No se ocupa con lo que hay.
        _repo, catalogo = self.catalogo_de("modelo:gamma")
        solo = agentes.seleccionar(exigencia, catalogo, politica=self.politica)
        self.assertEqual(solo["estado"], "bloqueado")
        self.assertIn("herramienta `" + catalogo_de_prueba.HERRAMIENTA_DE_VISION + "`",
                      solo["falta"])

    def test_05_agotar_los_slots_deja_esperando_y_no_reduce_la_composicion(self):
        """T230 · Defecto que previene: recortar el equipo para que quepa en los slots.

        `C4` paso 6: «Lo que no cabe queda `esperando-capacidad`. NO se reduce la
        composición para que quepa». Y `b.11` calcula `execution_slots` «a partir de agentes
        disponibles»: la unidad que ocupa un slot es el AGENTE. Por eso el par que la
        composición declara `combinables` entra o espera JUNTO, y con dos slots caben TRES
        roles: dos agentes, uno de ellos con dos roles.
        """
        holgado = self.equipo_de_dis(slots=99)
        todos = sorted(r["rol"] for r in holgado["roles"])
        self.assertEqual(len(todos), 4)

        apretado = self.equipo_de_dis(slots=2)
        despachados = sorted(r["rol"] for r in apretado["roles"])
        esperando = sorted(r["rol"] for r in apretado["esperando_capacidad"])
        # DOS slots, DOS agentes, TRES roles despachados: el par no se parte.
        self.assertEqual(apretado["slots_ocupados"], 2)
        self.assertEqual(len(despachados), 3)
        self.assertEqual(esperando, ["DIS/revision-de-fidelidad"])
        combinados = {"DIS/diseno-visual", "DIS/sistema-de-diseno"}
        self.assertTrue(combinados.issubset(set(despachados)))
        self.assertEqual(len({r["agente"] for r in apretado["roles"]
                              if r["rol"] in combinados}), 1)
        # LA COMPOSICIÓN NO SE REDUCE: la unión de las listas es la composición entera.
        self.assertEqual(sorted(despachados + esperando), todos)
        self.assertFalse(apretado["bloqueados"])
        for rol in apretado["esperando_capacidad"]:
            self.assertEqual(rol["estado"], "esperando-capacidad")
            self.assertTrue(rol["agente"], "esperar capacidad no es quedarse sin agente")

        # Con UN slot, el par sigue junto y son los DOS únicos despachados si les toca.
        minimo = self.equipo_de_dis(slots=1)
        self.assertEqual(minimo["slots_ocupados"], 1)
        agentes_despachados = [a for a in minimo["agentes"] if a["estado"] == "despachado"]
        self.assertEqual(len(agentes_despachados), 1)
        self.assertEqual(sorted(r["rol"] for r in minimo["roles"]
                                + minimo["esperando_capacidad"]), todos)
        self.assertTrue(equipos.exigir_slots_coherentes(minimo))
        # Y la sobreasignación se impide: nadie ocupa más slots de los declarados.
        for slots in (1, 2, 3, 4):
            equipo = self.equipo_de_dis(slots=slots)
            ocupados = [a for a in equipo["agentes"] if a["estado"] == "despachado"]
            self.assertLessEqual(len(ocupados), slots)
            self.assertEqual(len({a["slot"] for a in ocupados}), len(ocupados))

    def test_06_dos_roles_independientes_nunca_comparten_agente(self):
        """T231 · Defecto que previene: un agente que produce y se critica a sí mismo.

        `C4` paso 5: «dos roles comparten agente SÓLO si la composición los declara
        `combinables` Y ninguno aparece en `independientes`. Ante conflicto entre ambas
        listas, MANDA `independientes`». Se mide por dos caminos: (i) sobre `DSP`, donde
        `supervision` es independiente de `enrutamiento` y los dos resuelven al MISMO
        modelo —compartir modelo no es compartir agente—; (ii) sobre una COPIA REAL del
        corpus a la que se añade una cadena `A`+`B` y `B`+`C` con `C` independiente de `A`:
        encadenarlas metería a `A` y `C` en un agente, y el cierre lo impide.
        """
        equipo = equipos.materializar(
            "DSP", corpus=self.corpus, control_repo=self.repo,
            composiciones_verdaderas=[COMPOSICION_DE_DSP], slots=99)
        por_rol = {r["rol"]: r for r in equipo["roles"]}
        self.assertEqual(por_rol["DSP/enrutamiento"]["agente"],
                         por_rol["DSP/estado"]["agente"])
        self.assertNotEqual(por_rol["DSP/enrutamiento"]["agente"],
                            por_rol["DSP/supervision"]["agente"])
        # MISMO modelo y AGENTES DISTINTOS: la separación no se consigue por el catálogo.
        self.assertEqual(por_rol["DSP/enrutamiento"]["modelo"],
                         por_rol["DSP/supervision"]["modelo"])
        self.assertTrue(equipos.exigir_separacion(
            equipo, autor="DSP/enrutamiento", revisor="DSP/supervision"))

        # (ii) el CIERRE, sobre una copia real del corpus.
        base = tempfile.mkdtemp(prefix="ads-corpus-")
        self.addCleanup(shutil.rmtree, base, True)
        copia = copiar_arbol(base)
        ruta = os.path.join(copia, "capacidades", "DSP", "composicion.md")
        with open(ruta, "a", encoding="utf-8") as manejador:
            manejador.write(COMPOSICION_ENCADENADA)
        corpus = ciclo.Corpus(copia)
        encadenado = equipos.materializar(
            "DSP", corpus=corpus, control_repo=self.repo,
            composiciones_verdaderas=["composicion:dsp-cadena-de-prueba"], slots=99)
        agrupados = {tuple(sorted(a["roles"])) for a in encadenado["agentes"]}
        self.assertIn(("DSP/enrutamiento", "DSP/estado"), agrupados)
        self.assertIn(("DSP/supervision",), agrupados)
        for grupo in agrupados:
            self.assertFalse({"DSP/enrutamiento", "DSP/supervision"}.issubset(set(grupo)),
                             "el cierre de las combinaciones juntó dos independientes")
        rechazada = [c for c in encadenado["combinaciones"]
                     if not c["aplicada"] and "DSP/supervision" in c["roles"]]
        self.assertTrue(rechazada)
        self.assertIn("independientes", rechazada[0]["motivo"])
        # CONTROL: la primera combinación SÍ se aplicó, así que el rojo de arriba no puede
        # venir de que ninguna combinación se aplique nunca.
        aplicadas = [c for c in encadenado["combinaciones"] if c["aplicada"]]
        self.assertEqual([c["roles"] for c in aplicadas],
                         [["DSP/enrutamiento", "DSP/estado"]])

    def test_07_todo_candidato_descartado_lleva_un_motivo_verificable_uno_a_uno(self):
        """T232 · Defecto que previene: una lista de descartes que nadie puede comprobar.

        `C2` paso 5: «Se registra: rol, perfil, modelo elegido, modelos descartados y el
        motivo de cada descarte». Aquí se recorren los VEINTIÚN perfiles del kernel y, para
        cada descarte, se RECALCULA el motivo contra el catálogo: si dice que falla un eje,
        el eje falla; si dice que falta una herramienta, falta; si dice que el contexto no
        llega, no llega. Y candidatos = descartados ∪ ordenados, sin que nadie desaparezca.
        """
        patron_eje = re.compile(r"el eje `([a-z_]+)` exige `([a-z-]+)` y el modelo ofrece "
                                r"`([a-z-]+)`")
        patron_herramienta = re.compile(r"no ofrece la herramienta declarada `(.+?)`")
        patron_contexto = re.compile(r"el contexto exige `([a-z-]+)` y el modelo ofrece "
                                     r"`([a-z-]+)`")
        por_id = {m["id"]: m for m in self.catalogo.modelos}
        perfiles = sorted(self.politica.perfiles())
        self.assertEqual(len(perfiles), 21)
        comprobados = 0
        for identificador in perfiles:
            exigencia = self.politica.exigencia_de_perfil(identificador)
            registro = agentes.seleccionar(exigencia, self.catalogo,
                                           politica=self.politica)
            partido = ({d["modelo"] for d in registro["descartados"]}
                       | {o["modelo"] for o in registro["orden"]})
            self.assertEqual(partido, set(self.catalogo.ids), identificador)
            self.assertEqual(len(registro["descartados"]) + len(registro["orden"]),
                             len(self.catalogo.ids), identificador)
            for descarte in registro["descartados"]:
                modelo = por_id[descarte["modelo"]]
                encontrado = False
                for eje, exigido, ofrecido in patron_eje.findall(descarte["motivo"]):
                    self.assertEqual(exigencia["ejes"][eje], exigido)
                    self.assertEqual(modelo["ofrece"][eje], ofrecido)
                    self.assertLess(self.politica.indice(eje, ofrecido),
                                    self.politica.indice(eje, exigido))
                    encontrado = True
                for herramienta in patron_herramienta.findall(descarte["motivo"]):
                    self.assertIn(herramienta, exigencia["herramientas"])
                    self.assertNotIn(herramienta, modelo["herramientas"])
                    encontrado = True
                for exigido, ofrecido in patron_contexto.findall(descarte["motivo"]):
                    self.assertEqual(exigencia["contexto"], exigido)
                    self.assertEqual(modelo["contexto"], ofrecido)
                    self.assertLess(self.politica.indice_de_contexto(ofrecido),
                                    self.politica.indice_de_contexto(exigido))
                    encontrado = True
                self.assertTrue(encontrado, (identificador, descarte))
                comprobados += 1
            # El elegido NUNCA está entre los descartados, y está en el catálogo.
            if registro["estado"] == "asignado":
                self.assertNotIn(registro["modelo"],
                                 [d["modelo"] for d in registro["descartados"]])
                self.assertIn(registro["modelo"], self.catalogo.ids)
                self.assertEqual(registro["orden"][0]["modelo"], registro["modelo"])
        self.assertGreater(comprobados, 20)

    def test_08_reanudar_no_reasigna_en_silencio(self):
        """T233 · Defecto que previene: un relevo de agente que cambia el rol sin decirlo.

        `C2`, relevo de agente: «el rol NO cambia: la identidad, la memoria y la autoridad
        son del rol». Lo que se prueba: (i) el equipo se persiste por el motor y volver a
        leerlo devuelve EXACTAMENTE el mismo vínculo rol → agente → modelo; (ii) escribirlo
        dos veces no mueve la revisión; (iii) con OTRO catálogo el modelo cambia y el
        equipo es OTRO objeto durable, con OTRO identificador, de modo que una reasignación
        no puede pasar por la misma materialización de antes; y (iv) los ROLES son los
        mismos en los dos, porque el rol no depende del agente.
        """
        import adaptadores
        import runtime as paquete_runtime

        espacio = os.path.join(self.repo, "espacio")
        os.makedirs(espacio, exist_ok=True)
        registro = adaptadores.RegistroDeAdaptadores(
            [adaptadores.AdaptadorDeProcesoLocal(espacio)])
        rt = paquete_runtime.Runtime(self.repo, instancia="agentes-A",
                                     registro_de_adaptadores=registro).abrir()
        self.addCleanup(rt.cerrar)
        equipo = self.equipo_de_dis(slots=99)
        planificador = ciclo.Planificador(rt, corpus=self.corpus)
        planificador.registrar_equipos([equipo])
        antes = rt.almacen.revision()
        planificador.registrar_equipos([equipo])
        self.assertEqual(antes["revision_id"], rt.almacen.revision()["revision_id"])

        leido = durable.leer(rt.almacen, equipos.ruta_de(equipo["id"]))
        self.assertEqual({r["rol"]: (r["agente"], r["modelo"]) for r in leido["roles"]},
                         {r["rol"]: (r["agente"], r["modelo"]) for r in equipo["roles"]})
        # Releer NO reasigna: rematerializar con la misma entrada da el mismo objeto.
        self.assertEqual(self.equipo_de_dis(slots=99)["id"], equipo["id"])

        # Un RELEVO: el proyecto retira un modelo de su catálogo. El rol es el mismo; el
        # agente cambia, y el cambio es VISIBLE porque el equipo es otro objeto durable.
        otro_repo, _ = self.catalogo_de("modelo:alfa", "modelo:epsilon")
        relevado = self.equipo_de_dis(slots=99, repo=otro_repo)
        self.assertEqual(sorted(r["rol"] for r in relevado["roles"]),
                         sorted(r["rol"] for r in equipo["roles"]))
        self.assertNotEqual(relevado["id"], equipo["id"])
        self.assertNotEqual({r["modelo"] for r in relevado["roles"]},
                            {r["modelo"] for r in equipo["roles"]})
        # Y el objeto ANTERIOR sigue diciendo lo que decía: nada se reasignó en silencio.
        self.assertEqual(durable.leer(rt.almacen, equipos.ruta_de(equipo["id"]))["roles"],
                         leido["roles"])

    def test_09_varios_procesos_reales_no_producen_doble_ocupacion_de_slot(self):
        """T234 · Defecto que previene: dos agentes ocupando el mismo `execution_slot`.

        Cuatro PROCESOS REALES, tres carreras, el mismo control repo y el mismo estado
        durable. Cada uno materializa el equipo y lo publica por el motor. Lo que tiene que
        salir: un solo objeto de equipo, cada slot ocupado UNA vez, ningún rol en dos
        agentes, y nunca más agentes despachados que slots declarados.
        """
        motor_de_estado.inicializar(self.repo)
        guion = os.path.join(self.repo, "ocupar.py")
        with open(guion, "w", encoding="utf-8") as manejador:
            manejador.write(
                "import json, sys\n"
                "sys.path.insert(0, " + repr(RUNTIME) + ")\n"
                "import estado, ciclo\n"
                "from ciclo import durable, equipos\n"
                "equipo = ciclo.materializar('DIS', corpus=ciclo.Corpus(" + repr(KERNEL)
                + "), control_repo=" + repr(self.repo) + ",\n"
                "    composiciones_verdaderas=[" + repr(COMPOSICION_DE_DIS) + "],\n"
                "    condiciones_de_rol=[" + repr(CONDICION_DE_LA_COMBINACION) + "],\n"
                "    slots=2)\n"
                "almacen = estado.abrir(" + repr(self.repo) + ")\n"
                "durable.escribir(almacen, clase='ciclo.equipos.materializados',\n"
                "                 motivo='carrera', objetos={equipos.ruta_de(equipo['id']):"
                " equipo})\n"
                "print(equipo['id'])\n")
        vistos = set()
        for _carrera in range(3):
            procesos = [subprocess.Popen([sys.executable, guion], cwd=self.repo,
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                         text=True) for _ in range(4)]
            salidas = [p.communicate(timeout=SEGUNDOS_DE_ESPERA) for p in procesos]
            exitosos = [s for p, s in zip(procesos, salidas) if p.returncode == 0]
            self.assertTrue(exitosos, salidas)
            for salida, _err in exitosos:
                vistos.add(salida.strip())
        self.assertEqual(len(vistos), 1, vistos)

        almacen = motor_de_estado.abrir(self.repo)
        escritos = durable.listar(almacen, equipos.DOMINIO)
        self.assertEqual(len(escritos), 1, "la carrera produjo más de un equipo")
        publicado = durable.leer(almacen, equipos.ruta_de(vistos.pop()))
        self.assertIsNotNone(publicado)
        self.assertTrue(equipos.exigir_slots_coherentes(publicado))
        ocupados = [a for a in publicado["agentes"] if a["estado"] == "despachado"]
        self.assertEqual(len({a["slot"] for a in ocupados}), len(ocupados))
        self.assertLessEqual(len(ocupados), publicado["slots"])
        por_rol = {}
        for unidad in publicado["agentes"]:
            for rol in unidad["roles"]:
                self.assertNotIn(rol, por_rol, "un rol ocupa dos agentes")
                por_rol[rol] = unidad["agente"]


# =========================================================================
# T236-T239 y T249 · lo que la AUDITORÍA INDEPENDIENTE encontró, con su prueba
# =========================================================================
class LoQueLaAuditoriaEncontro(BaseDeAgentes):
    """Cada prueba de aquí cubre un hallazgo REAL, y se pone roja si se reintroduce.

    Cuatro de los cinco defectos que cubre esta clase eran PROPIEDADES BORRABLES: el
    producto las cumplía y ninguna prueba se enteraba de que dejara de cumplirlas. Es la
    misma lección del corte anterior, encontrada otra vez por un auditor que no construyó
    nada de esto, y por eso cada una entra en la tabla de sabotaje de `T235`.
    """

    def test_11_el_paso_1_de_c4_LEE_el_paquete_y_falla_cerrado(self):
        """T236 · Defecto que previene: rotular como PASO 1 un passthrough de dos cadenas.

        `C4` paso 1 nombra CINCO materias: «capacidad responsable · modo · objetivo · nivel
        de calidad exigido · declaración de acoplamiento». Antes ninguna se leía: `paquete`
        y `metodo` entraban por la firma y salían intactos, y el E2E comprobaba que dos
        cadenas volvían sin cambiar. Aquí se exige que las cinco se RESUELVAN contra sus
        sedes —el método contra `capacidades/<CAP>/metodos/`, el nivel contra los bloques
        `ads:nivel-novedad`, el acoplamiento contra `runtime.modelo`— y que resolver mal
        FALLE CERRADO, que es lo que distingue leer de transportar.
        """
        equipo = equipos.materializar(
            "DIS", corpus=self.corpus, control_repo=self.repo,
            composiciones_verdaderas=[COMPOSICION_DE_DIS], slots=99,
            condiciones_de_rol=[CONDICION_DE_LA_COMBINACION],
            metodo="Fundacion", nivel_de_calidad="N4", paquete="FEA-014/02",
            objetivo="dirección visual del producto", capacidad_responsable="DIS",
            acoplamiento={"lee_fuentes": ["app"], "escribe_fuentes": []},
        )
        lectura = equipo["lectura_del_paquete"]

        # 1 · capacidad responsable, 2 · objetivo: no se inventan.
        self.assertEqual(lectura["capacidad_responsable"], "DIS")
        self.assertEqual(lectura["objetivo"], "dirección visual del producto")

        # 3 · modo: DERIVADO de los pasos del método REAL, no del nombre del método.
        self.assertTrue(lectura["modo"]["declarado"])
        self.assertEqual(lectura["modo"]["metodo"], "Fundacion")
        self.assertTrue(lectura["modo"]["modos"],
                        "el modo sale vacío: no se han leído los pasos del método")
        for modo in lectura["modo"]["modos"]:
            self.assertIn(modo, ("divergente", "convergente", "lineal", "conversacional"),
                          "el modo `" + modo + "` no está en el enum de `esquemas/metodo.yaml`")
        self.assertEqual(lectura["modo"]["fase_divergente"],
                         "divergente" in lectura["modo"]["modos"])

        # 4 · nivel de calidad: sus gates y sus estaciones salen de la ESCALA, y llegan al
        #     equipo escrito. Si esto fuera un passthrough, `gates_del_nivel` estaría vacío.
        self.assertTrue(lectura["nivel_de_calidad"]["declarado"])
        self.assertEqual(lectura["nivel_de_calidad"]["id"], "N4")
        self.assertTrue(equipo["gates_del_nivel"],
                        "el nivel de calidad no aporta sus gates: el paso 1 no tiene efecto")
        for gate in equipo["gates_del_nivel"]:
            self.assertTrue(gate.startswith("gate:"), gate)
        self.assertTrue(lectura["nivel_de_calidad"]["estaciones"])

        # 5 · acoplamiento: NORMALIZADO por su sede, con sus siete campos.
        self.assertTrue(lectura["acoplamiento"]["declarado"])
        campos = lectura["acoplamiento"]["campos"]
        self.assertEqual(campos["lee_fuentes"], ["app"])
        self.assertEqual(campos["escribe_fuentes"], [])
        self.assertIn("afecta_contratos", campos)

        # Y la AUSENCIA se declara como ausencia, no como valor por omisión.
        sin_declarar = equipos.materializar(
            "DIS", corpus=self.corpus, control_repo=self.repo,
            composiciones_verdaderas=[COMPOSICION_DE_DIS], slots=99,
            condiciones_de_rol=[CONDICION_DE_LA_COMBINACION],
        )["lectura_del_paquete"]
        for materia in ("modo", "nivel_de_calidad", "acoplamiento"):
            self.assertFalse(sin_declarar[materia]["declarado"], materia)
            self.assertTrue(sin_declarar[materia]["motivo"],
                            "una ausencia sin motivo es indistinguible de un olvido: " + materia)

        # LAS RUTAS DE FALLO CERRADO. Sin ellas, «leer» sería «aceptar». Las tres que
        # DECLARABAN el reparto por la firma ya no existen: el cardinal se DERIVA del
        # campo `agentes` y el integrador de la `ampliacion` de la composición, y sus
        # negativos —diez, uno por caso— se prueban en
        # `test_cardinalidad_y_seleccion.py`. Aquí quedan las del paso 1.
        comun = dict(corpus=self.corpus, control_repo=self.repo,
                     composiciones_verdaderas=[COMPOSICION_DE_DIS], slots=99,
                     condiciones_de_rol=[CONDICION_DE_LA_COMBINACION])
        with self.assertRaises(errores.PaqueteIlegible):   # método que no es de la capacidad
            equipos.materializar("DIS", metodo="Despacho", **comun)
        with self.assertRaises(errores.PaqueteIlegible):   # nivel fuera de la escala
            equipos.materializar("DIS", nivel_de_calidad="N9", **comun)
        with self.assertRaises(errores.PaqueteIlegible):   # responsable distinta
            equipos.materializar("DIS", capacidad_responsable="ARQ", **comun)
        with self.assertRaises(errores.PaqueteIlegible):   # rol ajeno en el reparto
            equipos.materializar("DIS", metodo="Fundacion",
                                 reparto_declarado={"ARQ/lo-que-sea": {"territorios": ["x"]}},
                                 **comun)
        with self.assertRaises(errores.PaqueteIlegible):   # volumen que no es un recuento
            equipos.materializar("DIS", volumen=0, **comun)
        with self.assertRaises(errores.PaqueteIlegible):   # inicio lógico inválido
            equipos.materializar("DIS", inicio=-1, **comun)

        # Y las dos materias NUEVAS del paso 1 se leen igual que las otras cinco: declaradas
        # llegan al equipo con su valor, ausentes llegan como ausencia CON motivo. Sin ellas,
        # `C4` condición (c) —volumen contra contexto— y el «ANTES de empezar» del criterio
        # de comparación serían dos reglas sin insumo, que es como estaban.
        con_volumen = equipos.materializar("DIS", volumen=2, inicio=7, **comun)
        self.assertTrue(con_volumen["lectura_del_paquete"]["volumen"]["declarado"])
        self.assertEqual(con_volumen["lectura_del_paquete"]["volumen"]["unidades"], 2)
        self.assertEqual(con_volumen["lectura_del_paquete"]["inicio"]["instante"], 7)
        for materia in ("volumen", "inicio"):
            self.assertFalse(sin_declarar[materia]["declarado"], materia)
            self.assertTrue(sin_declarar[materia]["motivo"], materia)

    def test_12_el_agente_combinado_cumple_los_DOS_perfiles(self):
        """T237 · Defecto que previene: un agente que ocupa dos roles cumpliendo el más débil.

        Es el hallazgo más grave de la auditoría —su `D17`—: `Politica.combinar` toma el
        MÁXIMO eje a eje, y sustituirlo por el MÍNIMO dejaba los treinta y un validadores en
        verde mientras un modelo SIN VISIÓN ocupaba un rol que declara `vision` requerida o
        útil. `C2` define el agente como UN modelo que ocupa «rol o roles»: si son dos, el
        modelo tiene que cumplir los dos perfiles, y eso es el máximo, nunca el mínimo.
        """
        combinada = self.politica.combinar([
            self.politica.exigencia_de_perfil(identificador)
            for identificador in ("perfil:direccion-artistica", "perfil:despacho")
        ])
        # `direccion-artistica` exige `vision: requerida`; `despacho`, `vision: no`.
        self.assertEqual(combinada["ejes"]["vision"], "requerida",
                         "la exigencia combinada rebaja `vision`: un agente ciego podría "
                         "ocupar un rol que necesita ver")
        # Y en TODOS los ejes, contra los dos perfiles de origen, sin excepción.
        for identificador in ("perfil:direccion-artistica", "perfil:despacho"):
            una = self.politica.exigencia_de_perfil(identificador)
            for eje in self.politica.ejes:
                self.assertGreaterEqual(
                    self.politica.indice(eje, combinada["ejes"][eje]),
                    self.politica.indice(eje, una["ejes"][eje]),
                    "la exigencia combinada queda POR DEBAJO de `" + identificador
                    + "` en el eje `" + eje + "`")
            # Las herramientas se UNEN: perder una es perder una capacidad que el rol pide.
            for herramienta in una["herramientas"]:
                self.assertIn(herramienta, combinada["herramientas"])
            self.assertGreaterEqual(
                self.politica.indice_de_contexto(combinada["contexto"]),
                self.politica.indice_de_contexto(una["contexto"]))

        # Y la consecuencia MEDIDA sobre el catálogo real: ningún agente que ocupa varios
        # roles puede estar por debajo de ninguno de los perfiles que ocupa.
        equipo = self.equipo_de_dis()
        combinados = [u for u in equipo["agentes"] if len(u["roles"]) > 1]
        self.assertTrue(combinados, "esta composición debería producir un agente combinado")
        modelos = {m["id"]: m for m in self.catalogo.modelos}
        for unidad in combinados:
            modelo = modelos[unidad["modelo"]]
            for nombre in unidad["roles"]:
                una = self.politica.exigencia_de_perfil(
                    self.politica.perfil_de_rol(nombre))
                for eje in self.politica.ejes:
                    self.assertGreaterEqual(
                        self.politica.indice(eje, agentes._texto_de_nivel(
                            modelo["ofrece"][eje])),
                        self.politica.indice(eje, una["ejes"][eje]),
                        unidad["modelo"] + " ocupa `" + nombre + "` sin cumplir `" + eje + "`")

    def test_13_el_techo_de_coste_combinado_es_el_MENOR(self):
        """T238 · Defecto que previene: un agente combinado que gasta por encima del más estricto.

        Hallazgo `D12` de la auditoría: cambiar el `min` por `max` no ponía nada rojo. Un
        techo compartido no puede ser más alto que el más estricto de los que comparte, o el
        techo del rol barato deja de existir en cuanto se le combina con uno caro.
        """
        for pareja in (("perfil:despacho", "perfil:direccion-artistica"),
                       ("perfil:anclaje", "perfil:sistema"),
                       ("perfil:despacho", "perfil:anclaje")):
            exigencias = [self.politica.exigencia_de_perfil(p) for p in pareja]
            combinada = self.politica.combinar(exigencias)
            menor = min((e["coste"] for e in exigencias),
                        key=self.politica.indice_de_coste)
            self.assertEqual(
                combinada["coste"], menor,
                "el techo combinado de " + " + ".join(pareja) + " no es el MENOR de los dos")
            for una in exigencias:
                self.assertLessEqual(
                    self.politica.indice_de_coste(combinada["coste"]),
                    self.politica.indice_de_coste(una["coste"]))

    def test_14_el_eje_dominante_es_el_nivel_maximo_de_C2_al_pie_de_la_letra(self):
        """T239 · Defecto que previene: publicar como razón de la elección una regla que no es `C2`.

        Hallazgo `D13`+`#4` de la auditoría, en sus dos mitades. `C2` paso 4 (a) dice «el
        declarado en `exige` con nivel `maximo`, y si hay varios, el primero por orden del
        esquema». La implementación generalizaba a «el tope de su eje», y como el tope de
        `vision` es `requerida` —esa escala NO tiene `maximo`—, `vision` se adelantaba a un
        eje que sí pedía `maximo` en dos de los veintiún perfiles del kernel. Y además la
        regla no la probaba NADA: sustituirla por «siempre el primer eje» dejaba los treinta
        y un validadores en verde. Aquí se recalcula la regla de `C2` sobre los VEINTIÚN.
        """
        perfiles = self.politica.perfiles()
        self.assertGreaterEqual(len(perfiles), 21, "faltan perfiles del kernel")
        con_maximo, sin_maximo = 0, 0
        for identificador in sorted(perfiles):
            exigencia = self.politica.exigencia_de_perfil(identificador)
            eje, nivel, motivo = self.politica.eje_dominante(exigencia)
            # `C2` recalculado aquí, desde su texto, sin usar la implementación.
            esperados = [e for e in self.politica.ejes
                         if exigencia["ejes"][e] == agentes.Politica.NIVEL_DOMINANTE]
            if esperados:
                con_maximo += 1
                self.assertEqual(
                    eje, esperados[0],
                    identificador + ": `C2` paso 4 (a) manda el PRIMERO por orden del "
                    "esquema con nivel `maximo`, que es `" + esperados[0] + "`")
                self.assertEqual(nivel, agentes.Politica.NIVEL_DOMINANTE)
                self.assertNotIn("DERIVADO", motivo)
            else:
                sin_maximo += 1
                # `C2` no contempla este caso: el motivo TIENE que decir que es derivación.
                self.assertIn("DERIVADO", motivo,
                              identificador + ": se aplica una regla que `C2` no escribe y "
                              "el motivo publicado no lo declara")
            # `vision` no puede ser NUNCA el eje dominante: su escala no tiene `maximo`.
            self.assertNotEqual(
                eje, "vision",
                identificador + ": `vision` no puede ser el eje dominante, porque su escala "
                "—`no` · `util` · `requerida`— no contiene el nivel `maximo` que `C2` nombra")
        self.assertTrue(con_maximo, "ningún perfil declara `maximo`: la regla no se ejerce")
        self.assertTrue(sin_maximo, "ningún perfil sin `maximo`: la derivación no se ejerce")

    def test_15_el_registro_de_combinaciones_no_se_autocontradice(self):
        """T249 · Defecto que previene: un equipo escrito que afirma una cosa y su contraria.

        Hallazgo `#3` de la auditoría. Cuando ningún modelo cumple los dos perfiles de un par
        `combinables`, el grupo se rompe —correcto, `C4` la llama licencia y no obligación—,
        pero la ruptura se AÑADÍA a la lista sin retirar la entrada `aplicada: True` previa:
        el mismo par salía publicado con las dos, y `comparte_agente_con` nombraba a un
        compañero con el que NO se compartía agente. `exigir_separacion` —la instrumentación
        de `G13`— consulta ese campo, así que la contradicción no era cosmética.

        Se reproduce con un catálogo HOSTIL REAL: dos modelos, cada uno a la medida exacta de
        UNO de los dos perfiles, de modo que ninguno cumple los dos.
        """
        rol_a, rol_b = "ENC/interlocutor", "ENC/anclaje"
        exigencias = {nombre: self.politica.exigencia_de_perfil(
            self.politica.perfil_de_rol(nombre)) for nombre in (rol_a, rol_b)}
        repo = tempfile.mkdtemp(prefix="ads-hostil-")
        self.addCleanup(shutil.rmtree, repo, True)
        catalogo_de_prueba.escribir_a_medida(repo, self.politica, exigencias)

        equipo = equipos.materializar(
            "ENC", corpus=self.corpus, control_repo=repo, slots=99,
            composiciones_verdaderas=["composicion:enc-conversacion-simple"],
            condiciones_de_rol=["el anclaje se cierra con menos de cinco búsquedas"],
        )
        # 1 · ninguna combinación queda `aplicada` sobre un par que se rompió.
        rotas = [c for c in equipo["combinaciones"]
                 if not c["aplicada"] and "ningún modelo" in c["motivo"]]
        self.assertTrue(rotas, "el catálogo hostil no llegó a romper la combinación")
        for rota in rotas:
            for otra in equipo["combinaciones"]:
                if otra is rota or not otra["aplicada"]:
                    continue
                self.assertFalse(
                    set(otra["roles"]) <= set(rota["roles"]),
                    "el registro publica `aplicada: True` para " + str(otra["roles"])
                    + " y a la vez la ruptura de " + str(rota["roles"]))

        # 2 · `comparte_agente_con` dice la VERDAD, contrastado contra el agente real.
        filas = {f["rol"]: f for f in
                 equipo["roles"] + equipo["esperando_capacidad"] + equipo["bloqueados"]}
        for nombre, fila in filas.items():
            companero = fila["comparte_agente_con"]
            if companero is None:
                for otro, otra in filas.items():
                    if otro != nombre and otra["agente"] and otra["agente"] == fila["agente"]:
                        self.fail(nombre + " comparte agente con " + otro + " y publica "
                                  "`comparte_agente_con: None`")
                continue
            self.assertEqual(
                fila["agente"], filas[companero]["agente"],
                nombre + " dice compartir agente con " + companero + " y NO lo comparte")

        # 3 · y `_comparten`, que es lo que `exigir_separacion` consulta, coincide.
        if rol_a in filas and rol_b in filas:
            realmente = filas[rol_a]["agente"] == filas[rol_b]["agente"]
            self.assertEqual(equipos._comparten(equipo, rol_a, rol_b), realmente,
                             "`_comparten()` no coincide con los agentes realmente asignados")

# =========================================================================
# T235 · el sabotaje: cada corrección tiene que poder ponerse ROJA
# =========================================================================
class Sabotaje(BaseDeAgentes):
    """Borra la regla en una COPIA del árbol y comprueba que la prueba FALLA de verdad."""

    # (fichero, texto que se borra o sustituye, sustituto, prueba que TIENE que ponerse roja)
    SABOTAJES = (
        (
            "el filtro por EJES de `C2` paso 2",
            "ciclo/agentes.py",
            "def _motivo_por_ejes(exigencia, modelo, politica):\n    fallos = []",
            "def _motivo_por_ejes(exigencia, modelo, politica):\n    return []\n    fallos = []",
            "AsignacionDeAgentes.test_03_un_modelo_que_no_cumple_un_eje_se_descarta_con_su_motivo",
        ),
        (
            "el filtro por HERRAMIENTAS de `C2` paso 3",
            "ciclo/agentes.py",
            "def _motivo_por_herramientas(exigencia, modelo):\n    ofrecidas",
            "def _motivo_por_herramientas(exigencia, modelo):\n    return []\n    ofrecidas",
            "AsignacionDeAgentes.test_04_un_modelo_sin_la_herramienta_o_el_contexto_declarados_se_descarta",
        ),
        (
            "el ORDEN de `C2` paso 4: el techo de coste y el coste dejan de contar",
            "ciclo/agentes.py",
            "        0 if dentro[m[\"id\"]] else 1,\n        politica.indice_de_coste(m[\"coste\"]),\n        m[\"id\"],\n    ))",
            "        m[\"id\"],\n    ))",
            "AsignacionDeAgentes.test_01_una_composicion_con_varios_roles_recibe_agente_modelo_y_traza",
        ),
        (
            "el corte por AGENTE de `C4` paso 6, devuelto al corte por ROL que separaba "
            "un par combinable",
            "ciclo/equipos.py",
            "    ocupados = 0\n    for unidad in unidades:",
            "    unidades = [dict(u, roles=[r]) for u in unidades"
            " for r in sorted(u[\"roles\"])]\n"
            "    ocupados = 0\n    for unidad in unidades:",
            "AsignacionDeAgentes.test_05_agotar_los_slots_deja_esperando_y_no_reduce_la_composicion",
        ),
        (
            "la precedencia de `independientes` sobre el CIERRE de `combinables`",
            "ciclo/equipos.py",
            "def _choque_en_el_grupo(grupo, independientes):",
            "def _choque_en_el_grupo(grupo, independientes):\n    return None",
            "AsignacionDeAgentes.test_06_dos_roles_independientes_nunca_comparten_agente",
        ),
        # --- los CINCO que la AUDITORÍA INDEPENDIENTE encontró. Cuatro de ellos eran
        # --- propiedades que se podían borrar sin que ninguna prueba parpadeara.
        (
            "`C4` PASO 1 vuelve a ser un passthrough: no se lee el nivel de calidad",
            "ciclo/equipos.py",
            "        niveles = _niveles_de_calidad(corpus)",
            "        niveles = {}\n        return lectura\n        niveles = _niveles_de_calidad(corpus)",
            "LoQueLaAuditoriaEncontro.test_11_el_paso_1_de_c4_LEE_el_paquete_y_falla_cerrado",
        ),
        (
            "la exigencia del agente COMBINADO baja al MÍNIMO eje a eje, y un modelo "
            "ciego puede ocupar un rol que necesita ver",
            "ciclo/agentes.py",
            "            ejes[eje] = max((e[\"ejes\"][eje] for e in exigencias),",
            "            ejes[eje] = min((e[\"ejes\"][eje] for e in exigencias),",
            "LoQueLaAuditoriaEncontro.test_12_el_agente_combinado_cumple_los_DOS_perfiles",
        ),
        (
            "el techo de coste del agente combinado deja de ser el MENOR",
            "ciclo/agentes.py",
            "        coste = min((e[\"coste\"] for e in exigencias), key=self.indice_de_coste)",
            "        coste = max((e[\"coste\"] for e in exigencias), key=self.indice_de_coste)",
            "LoQueLaAuditoriaEncontro.test_13_el_techo_de_coste_combinado_es_el_MENOR",
        ),
        (
            "el EJE DOMINANTE vuelve a «el tope de su eje» y `vision` se adelanta a un "
            "eje que sí pide `maximo`",
            "ciclo/agentes.py",
            "            if exigencia[\"ejes\"][eje] == self.NIVEL_DOMINANTE:",
            "            if exigencia[\"ejes\"][eje] == self.tope(eje):",
            "LoQueLaAuditoriaEncontro.test_14_el_eje_dominante_es_el_nivel_maximo_de_C2_al_pie_de_la_letra",
        ),
        (
            "la ruptura de una combinación deja de RETIRAR la entrada `aplicada: True` "
            "que la contradice",
            "ciclo/equipos.py",
            "                if previa[\"aplicada\"] and set(previa[\"roles\"]) <= set(grupo):",
            "                if False and set(previa[\"roles\"]) <= set(grupo):",
            "LoQueLaAuditoriaEncontro.test_15_el_registro_de_combinaciones_no_se_autocontradice",
        ),
        (
            "el FALLO CERRADO sin catálogo: un modelo por defecto ocupa el rol",
            "ciclo/agentes.py",
            "    if not ordenados:\n        registro[\"estado\"] = ESTADO_BLOQUEADO",
            "    if not ordenados and catalogo is not None and catalogo.modelos:\n"
            "        ordenados = [catalogo.modelos[0]]\n"
            "        dentro[ordenados[0][\"id\"]] = True\n"
            "    if not ordenados:\n        registro[\"estado\"] = ESTADO_BLOQUEADO",
            "AsignacionDeAgentes.test_03_un_modelo_que_no_cumple_un_eje_se_descarta_con_su_motivo",
        ),
    )

    def test_10_borrar_la_regla_pone_la_prueba_roja(self):
        """T235 · Defecto que previene: una propiedad que se puede borrar sin que nada avise.

        La lección de método del corte anterior: la regla «`independientes` manda sobre
        `combinables`» se podía BORRAR ENTERA y las cuarenta y ocho pruebas seguían verdes.
        Aquí no se promete que la batería detecte la regresión: se COMPRUEBA, en un PROCESO
        REAL, sobre una COPIA del árbol a la que se le ha quitado la regla, una por una.

        El control positivo va primero: la copia SIN sabotear tiene que pasar en verde. Sin
        él, un rojo podría venir de que la copia esté rota, no de que la regla falte.
        """
        base = tempfile.mkdtemp(prefix="ads-sabotaje-")
        self.addCleanup(shutil.rmtree, base, True)
        copia = copiar_arbol(base)
        prueba = os.path.join(copia, "runtime", "pruebas", "test_agentes.py")
        entorno = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}

        def correr(nombre):
            return subprocess.run(
                [sys.executable, prueba, nombre], cwd=base, capture_output=True,
                text=True, timeout=SEGUNDOS_DE_ESPERA, env=entorno)

        # CONTROL POSITIVO: la copia intacta pasa.
        for _titulo, _fichero, _viejo, _nuevo, caso in self.SABOTAJES:
            verde = correr(caso)
            self.assertEqual(verde.returncode, 0,
                             "la copia SIN sabotear ya falla en " + caso + ": "
                             + verde.stderr[-2000:])
            # Y ha EJECUTADO la prueba: un runner que no encuentra el caso y sale con 0
            # daría un verde vacío, y el rojo posterior no querría decir nada.
            self.assertIn("Ran 1 test", verde.stderr, caso)

        for titulo, fichero, viejo, nuevo, caso in self.SABOTAJES:
            ruta = os.path.join(copia, "runtime", fichero)
            with open(ruta, encoding="utf-8") as manejador:
                original = manejador.read()
            self.assertIn(viejo, original,
                          "el sabotaje «" + titulo + "» no encuentra qué borrar: sería un "
                          "no-op y la prueba pasaría sin haber atacado nada")
            self.assertNotEqual(viejo, nuevo, titulo)
            try:
                with open(ruta, "w", encoding="utf-8") as manejador:
                    manejador.write(original.replace(viejo, nuevo, 1))
                roja = correr(caso)
                self.assertNotEqual(
                    roja.returncode, 0,
                    "SABOTAJE SIN ROJO · " + titulo + " · la prueba `" + caso
                    + "` siguió pasando con la regla borrada")
            finally:
                with open(ruta, "w", encoding="utf-8") as manejador:
                    manejador.write(original)
            # Y restaurada, vuelve al verde: el rojo era del sabotaje y no del entorno.
            self.assertEqual(correr(caso).returncode, 0, titulo)


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de `test_ciclo.py`, no importado: una batería no puede depender de otra para
    poder ejecutarse. La salida se PUBLICA como evidencia, y «Ran 10 tests in 12.481s»
    cambiaría en cada ejecución y ensuciaría el árbol en cada comprobación.
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
