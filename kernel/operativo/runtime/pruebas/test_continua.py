#!/usr/bin/env python3
"""test_continua — la batería de `Continúa` de `§7.4` (`F6`, macrobloque 3, agente A).

Instancia los SIETE pasos de `b.14` con la desviación declarada del paso 2, y los DIEZ
escenarios que el encargo del macrobloque exige, cada uno con PROCESO Y ESTADO REALES.

CUATRO REGLAS QUE ESTA BATERÍA SE IMPONE, Y POR QUÉ:

  1. LAS MUERTES SON MUERTES DE VERDAD. El escenario del proceso muerto lanza un
     `subprocess` que toma el lease y se queda ejecutando, y el padre lo mata con
     `SIGKILL`: sin `finally`, sin cerrar ficheros, sin soltar el `flock` desde Python. Un
     proceso «simulado» no distingue un lease durable de una variable en memoria.

  2. CADA ESCENARIO DECLARA QUÉ DEBE VER `Continúa` ANTES DE MIRARLO. No «lo que salga»:
     el paquete concreto, el hallazgo concreto y si bloquea o no. Una prueba de reanudación
     que acepta cualquier resultado no distingue un `Continúa` correcto de uno que informa
     de lo primero que encuentra.

  3. LA PROPIEDAD CENTRAL SE MIDE POR BYTES Y POR REVISIÓN. Dos ejecuciones consecutivas
     sin cambios producen el MISMO plan byte a byte y NO mueven el estado: se comparan
     `revision_id` y `cid_raiz` antes y después, y el volcado JSON de los dos planes.

  4. `Continúa` NO SIGNIFICA «HAZ TODO LO PENDIENTE», y hay una prueba que lo comprueba:
     con varios paquetes elegibles, el modo PLAN retoma el FRENTE y deja el resto listado
     como inanición, sin despachar nada.

Y una quinta, de forma: la salida se PUBLICA como evidencia, así que el resumen de
`unittest` no lleva duración y todo fichero que se abre se cierra.

    python3 kernel/operativo/runtime/pruebas/test_continua.py

Sale con 0 si todo pasa. Se ejecuta desde cualquier directorio.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
RUNTIME = os.path.join(RAIZ, "kernel", "operativo", "runtime")
KERNEL = os.path.join(RAIZ, "kernel", "operativo")
sys.path.insert(0, RUNTIME)

try:
    import adaptadores
    import ciclo
    import runtime as paquete_runtime
    from ciclo import continuacion, durable, gates, handoffs
except ImportError as exc:
    print(f"no se encuentra el paquete `ciclo` bajo {RUNTIME}: {exc}", file=sys.stderr)
    raise

# El entorno de las pruebas NO hereda las variables de corte del runtime ni del motor: si
# alguien las tuviera puestas en su terminal, media batería moriría por una causa que no es
# la que se está probando.
ENTORNO = {
    clave: valor for clave, valor in os.environ.items()
    if clave not in ("ADS_RUNTIME_FALLO", "ADS_ESTADO_FALLO")
}

SEGUNDOS_DE_ESPERA = 180
SEGUNDOS_DE_ARRANQUE = 60

# Los SIETE pasos de `b.14`, transcritos para CONFRONTAR el dato del paquete.
SIETE_PASOS = ("1-reconstruir", "2-verificar", "3-consumir", "4-seleccionar",
               "5-reportar", "6-cargar", "7-trabajar")

# Las OCHO comprobaciones del paso 2 que `§7.4` enumera, por el nombre con el que el módulo
# las emite. Se escriben aquí para comprobar que ninguna se queda sin implementar.
COMPROBACIONES_DEL_PASO_2 = (
    "artefactos-declarados",
    "transacciones-abiertas",
    "deriva-no-transaccional",
    "reconciliacion-pendiente",
    "derivados-divergentes",
    "proyecciones-con-huella-rota",
    "esperas-no-viables",
    "cobertura-vencida",
)

GUION_DEL_MORIBUNDO = textwrap.dedent(
    """
    import os, sys
    sys.path.insert(0, {runtime!r})
    import adaptadores, runtime
    registro = adaptadores.RegistroDeAdaptadores([
        adaptadores.AdaptadorDeProcesoLocal({espacio!r}),
    ])
    rt = runtime.Runtime({repo!r}, instancia={instancia!r},
                         registro_de_adaptadores=registro).abrir()
    lease = rt.adquirir({paquete!r})
    with open({testigo!r}, "w", encoding="utf-8") as fichero:
        fichero.write(str(os.getpid()))
    rt.despachar({paquete!r})
    """
)


def entrada_base(**cambios):
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


class BaseDeContinua(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.corpus = ciclo.Corpus(KERNEL)

    def setUp(self):
        self.repo = tempfile.mkdtemp(prefix="ads-continua-")
        self.espacio = os.path.join(self.repo, "espacio")
        os.makedirs(self.espacio, exist_ok=True)
        self.addCleanup(shutil.rmtree, self.repo, True)

    def abrir_runtime(self, instancia="continua-A"):
        registro = adaptadores.RegistroDeAdaptadores([
            adaptadores.AdaptadorDeProcesoLocal(self.espacio),
        ])
        rt = paquete_runtime.Runtime(
            self.repo, instancia=instancia, registro_de_adaptadores=registro,
        ).abrir()
        self.addCleanup(rt.cerrar)
        return rt

    def orden(self, capacidades, argumentos=("/bin/sh", "-c", "exit 0")):
        return {
            capacidad: {
                "adaptador": "proceso-local", "operacion": "ejecutar",
                "argumentos": list(argumentos), "limite_segundos": 120,
            }
            for capacidad in capacidades
        }

    def preparar(self, rt, *, argumentos=("/bin/sh", "-c", "exit 0"), entrada=None):
        marco = ciclo.encuadrar(self.repo, entrada or entrada_base(), corpus=self.corpus)
        ruta = ciclo.componer(marco, corpus=self.corpus)
        capacidades = sorted({p["capacidad"] for p in ruta["participantes"]})
        planificador = ciclo.Planificador(rt, corpus=self.corpus)
        plan = planificador.planificar(
            marco, ruta,
            orden_por_capacidad=self.orden(capacidades, argumentos),
            secuencial=False,
        )
        return marco, ruta, plan

    def continuar(self, rt, **argumentos):
        return continuacion.Continuacion(rt, corpus=self.corpus).plan(**argumentos)


# =========================================================================
# T203 · los SIETE pasos y las OCHO comprobaciones del paso 2
# =========================================================================
class LosSietePasos(BaseDeContinua):

    def test_01_el_plan_recorre_los_siete_pasos_en_orden(self):
        """T203 · Defecto que previene: un paso de `b.14` que se salta sin que se note.

        Los siete están declarados como DATO y el plan los recorre en orden. El paso 7 sólo
        se ejecuta en modo EJECUCIÓN, y el modo PLAN lo declara no ejecutado.
        """
        rt = self.abrir_runtime()
        self.preparar(rt)
        plan = self.continuar(rt)
        self.assertEqual(tuple(plan["pasos"]), SIETE_PASOS)
        self.assertEqual(tuple(continuacion.PASOS), SIETE_PASOS)
        for paso in SIETE_PASOS:
            self.assertIn(paso.replace("-", "_", 1), plan, paso)
        self.assertFalse(plan["7_trabajar"]["ejecutado"])
        self.assertTrue(plan["no_significa_hacer_todo_lo_pendiente"])

    def test_02_el_paso_2_ejecuta_las_ocho_comprobaciones(self):
        """T203 · Defecto que previene: una comprobación del paso 2 que nadie implementó.

        Las ocho se comprueban por su presencia en el informe del paso 2, no por su texto:
        cada una tiene una clave propia en la salida, y las que hallan algo lo dicen con su
        nombre de comprobación.
        """
        rt = self.abrir_runtime()
        self.preparar(rt)
        plan = self.continuar(rt)
        verificacion = plan["2_verificar"]
        for clave in ("artefactos_ausentes", "rama_de_recuperacion",
                      "transacciones_marcadas", "reconciliaciones_pendientes",
                      "derivados_divergentes", "proyecciones_rotas",
                      "esperas_no_viables", "cobertura_vencida", "ventana"):
            self.assertIn(clave, verificacion, clave)
        self.assertEqual(verificacion["ventana"], "cerrada")
        self.assertFalse(verificacion["bloqueante"])

    def test_03_la_deriva_no_transaccional_se_reporta_y_escala(self):
        """T203 · Defecto que previene: seguir despachando sobre un árbol adulterado.

        Se retira a mano un objeto que la revisión declara —una escritura fuera del diario,
        que es la definición de deriva—, y `Continúa` la reporta como BLOQUEANTE, escala y
        NO selecciona nada.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        ruta_fisica = os.path.join(self.repo, "estado", "canonico", "planes",
                                   plan["id"] + ".json")
        self.assertTrue(os.path.isfile(ruta_fisica))
        os.remove(ruta_fisica)
        continuado = self.continuar(rt)
        verificacion = continuado["2_verificar"]
        self.assertTrue(verificacion["bloqueante"])
        nombres = {h["comprobacion"] for h in verificacion["hallazgos"]}
        self.assertIn("deriva-no-transaccional", nombres)
        self.assertEqual(continuado["4_seleccionar"]["retoma"], [])

    def test_04_una_espera_no_viable_se_convierte_en_bloqueo(self):
        """T203 · Defecto que previene: una espera muerta que nadie vuelve a mirar (`b.8`).

        Un paquete espera a otro que se CANCELA. En modo PLAN se REPORTA; en modo EJECUCIÓN
        con `--reparar` se convierte en BLOQUEO, que es lo que `b.8` obliga.
        """
        rt = self.abrir_runtime()
        marco = ciclo.encuadrar(self.repo, entrada_base(), corpus=self.corpus)
        ruta = ciclo.componer(marco, corpus=self.corpus)
        planificador = ciclo.Planificador(rt, corpus=self.corpus)
        plan = planificador.planificar(
            marco, ruta,
            orden_por_capacidad=self.orden(
                sorted({p["capacidad"] for p in ruta["participantes"]})),
            secuencial=True,
        )
        primero, segundo = plan["paquetes"][0], plan["paquetes"][1]
        rt.cancelar(primero, motivo="se retira", autoridad="OWNER")
        rt._mover(segundo, "esperando-dependencia", motivo="espera al primero",
                  autoridad="DSP", clase="runtime.paquete.espera")
        del segundo
        pendiente = [p for p in plan["paquetes"]
                     if rt.almacen.leer("paquetes/" + p + ".json")["estado"]
                     == "esperando-dependencia"]
        self.assertTrue(pendiente)
        informado = self.continuar(rt)
        self.assertEqual(informado["2_verificar"]["esperas_no_viables"], pendiente)
        continuacion.Continuacion(rt, corpus=self.corpus).verificar(
            continuacion.Continuacion(rt, corpus=self.corpus).reconstruir(), reparar=True,
        )
        for identificador in pendiente:
            self.assertEqual(
                rt.almacen.leer("paquetes/" + identificador + ".json")["estado"],
                "bloqueado", identificador,
            )

    def test_05_las_celdas_de_cobertura_vencidas_solo_se_reportan(self):
        """T203 · Defecto que previene: abrir trabajo por una certificación caducada.

        `§7.4` es literal: «¿hay celdas de cobertura vencidas? → SÓLO REPORTAR, no abrir».
        Se escribe una celda con otra huella de corpus y se comprueba que se reporta y que
        NO aparece trabajo nuevo.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        antes = len(rt.almacen.listar("paquetes"))
        durable.escribir(
            rt.almacen, clase="prueba.cobertura", motivo="celda con huella vieja",
            objetos={"cobertura/cel-vieja.json": {
                "id": "cel-vieja", "aspecto": "aspecto:certificacion/estructural",
                "estado": "verificado",
                "sujeto": {"revision_de_esquemas_y_contratos": "sha256:" + "0" * 64},
            }},
        )
        continuado = self.continuar(rt)
        self.assertIn("cel-vieja", continuado["2_verificar"]["cobertura_vencida"])
        hallazgo = [h for h in continuado["2_verificar"]["hallazgos"]
                    if h["comprobacion"] == "cobertura-vencida"][0]
        self.assertEqual(hallazgo["gravedad"], "informativo")
        self.assertEqual(len(rt.almacen.listar("paquetes")), antes)

    def test_06_un_derivado_divergente_se_regenera_y_una_proyeccion_rota_se_reporta(self):
        """T203 · Defecto que previene: sincronizar un derivado en vez de recompilarlo.

        `I5`: se regenera, no se sincroniza. Y una proyección editada a mano se diagnostica
        con `adaptadores.validar_deriva`, que ya existe: aquí no hay un segundo validador.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        fuente = "planes/" + plan["id"] + ".json"
        durable.escribir(
            rt.almacen, clase="prueba.derivado", motivo="derivado con fuente vieja",
            objetos={"derivados/dv-1.json": {
                "id": "dv-1", "fuente": fuente,
                "source_revision": "sha256:" + "0" * 64, "contenido": None,
            }},
        )
        entradas = {"a": "1"}
        texto = adaptadores.compilar(
            adaptador="proceso-local", version_de_ads="1", entradas=entradas,
            cuerpo="linea\n", origen_canonico="prueba",
        )
        fichero = os.path.join(self.repo, "proyeccion.txt")
        with open(fichero, "w", encoding="utf-8") as manejador:
            manejador.write(texto.replace("linea", "editada a mano"))
        durable.escribir(
            rt.almacen, clase="prueba.proyeccion", motivo="proyección declarada",
            objetos={"proyecciones/py-1.json": {
                "id": "py-1", "fichero": "proyeccion.txt", "entradas": entradas,
            }},
        )
        informado = self.continuar(rt)
        self.assertEqual(informado["2_verificar"]["derivados_divergentes"], ["dv-1"])
        self.assertEqual(informado["2_verificar"]["proyecciones_rotas"], ["py-1"])
        motor = continuacion.Continuacion(rt, corpus=self.corpus)
        motor.verificar(motor.reconstruir(), reparar=True)
        regenerado = rt.almacen.leer("derivados/dv-1.json")
        self.assertEqual(regenerado["source_revision"],
                         rt.almacen.revision()["raiz"][fuente])

    def test_07_las_ordenes_se_consumen_una_vez_y_una_orden_caduca_no_se_aplica(self):
        """T203 · Defecto que previene: aplicar una orden emitida sobre otro estado.

        Paso 3. La orden conserva la BASE sobre la que se emitió (`entrada:orden`): si esa
        base dejó de ser vigente, se reporta como CADUCA y NO se aplica. Y una orden ya
        consumida no se vuelve a consumir.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        paquete = plan["paquetes"][0]
        base = rt.almacen.revision()["raiz"]["paquetes/" + paquete + ".json"]
        durable.escribir(
            rt.almacen, clase="prueba.orden", motivo="dos órdenes del Owner",
            objetos={
                "ordenes/or-1.json": {"id": "or-1", "verbo": "pausar", "paquete": paquete,
                                      "base": base, "autoridad": "OWNER",
                                      "motivo": "el Owner lo aparca", "consumida": False},
                "ordenes/or-2.json": {"id": "or-2", "verbo": "cancelar",
                                      "paquete": paquete,
                                      "base": "sha256:" + "0" * 64, "autoridad": "OWNER",
                                      "motivo": "emitida sobre otro estado",
                                      "consumida": False},
                "ordenes/or-3.json": {"id": "or-3", "verbo": "inventar", "paquete": paquete,
                                      "base": base, "autoridad": "OWNER",
                                      "motivo": "verbo fuera de `b.13`", "consumida": False},
            },
        )
        motor = continuacion.Continuacion(rt, corpus=self.corpus)
        consumo = motor.consumir(aplicar=True)
        self.assertEqual(consumo["aplicadas"], ["or-1"])
        self.assertEqual(consumo["caducas"], ["or-2"])
        self.assertEqual(consumo["verbo_desconocido"], ["or-3"])
        self.assertEqual(rt.almacen.leer("paquetes/" + paquete + ".json")["estado"],
                         "pausado")
        segunda = motor.consumir(aplicar=True)
        self.assertEqual(segunda["aplicadas"], [])

    def test_08_continua_no_significa_haz_todo_lo_pendiente(self):
        """T203 · Defecto que previene: vaciar la cola porque alguien escribió `Continúa`.

        Con varios paquetes elegibles, el modo PLAN retoma el FRENTE y deja el resto
        listado como inanición, sin despachar nada: la revisión no se mueve.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        self.assertGreater(len(plan["paquetes"]), 1)
        antes = rt.almacen.revision()
        continuado = self.continuar(rt, frente=1)
        self.assertEqual(len(continuado["4_seleccionar"]["retoma"]), 1)
        self.assertTrue(continuado["5_reportar"]["que_esta_en_inanicion"])
        self.assertEqual(rt.almacen.revision()["revision_id"], antes["revision_id"])
        for paquete in plan["paquetes"]:
            self.assertEqual(rt.almacen.leer("paquetes/" + paquete + ".json")["estado"],
                             "listo")


# =========================================================================
# T204 · los DIEZ escenarios, cada uno con proceso y estado REALES
# =========================================================================
class LosDiezEscenarios(BaseDeContinua):

    def test_20_proceso_detenido_limpiamente(self):
        """T204 · escenario 1 · Defecto que previene: no saber retomar tras un cierre bueno.

        Un proceso REAL abre el runtime, despacha un paquete y CIERRA limpiamente. `Continúa`
        desde otro proceso ve el paquete completado, ningún lease huérfano y el resto listo.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        rt.cerrar()
        guion = textwrap.dedent(
            """
            import sys
            sys.path.insert(0, {runtime!r})
            import adaptadores, runtime
            registro = adaptadores.RegistroDeAdaptadores([
                adaptadores.AdaptadorDeProcesoLocal({espacio!r}),
            ])
            with runtime.Runtime({repo!r}, instancia="limpio",
                                 registro_de_adaptadores=registro) as rt:
                rt.despachar({paquete!r})
            """
        ).format(runtime=RUNTIME, espacio=self.espacio, repo=self.repo,
                 paquete=plan["paquetes"][0])
        completado = subprocess.run([sys.executable, "-c", guion], capture_output=True,
                                    timeout=SEGUNDOS_DE_ESPERA, env=ENTORNO)
        self.assertEqual(completado.returncode, 0,
                         completado.stderr.decode("utf-8", "replace"))
        otro = self.abrir_runtime("continua-B")
        continuado = self.continuar(otro)
        estado = otro.almacen.leer("paquetes/" + plan["paquetes"][0] + ".json")
        self.assertEqual(estado["estado"], "completado")
        self.assertFalse(continuado["2_verificar"]["bloqueante"])
        self.assertNotIn(plan["paquetes"][0],
                         [r["paquete"] for r in continuado["4_seleccionar"]["retoma"]])
        self.assertEqual(continuado["2_verificar"]["artefactos_ausentes"], [])

    def test_21_proceso_muerto_con_sigkill_de_verdad(self):
        """T204 · escenario 2 · Defecto que previene: creer que un lease caduca solo.

        Un proceso REAL toma el lease, empieza a ejecutar y el padre lo mata con `SIGKILL`:
        sin `finally`, sin soltar el `flock` desde Python. `Continúa` desde otra instancia
        ve el paquete EN CURSO, con su efecto abierto y sin acuse, y NO lo selecciona.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt, argumentos=("/bin/sh", "-c", "sleep 120"))
        paquete = plan["paquetes"][0]
        rt.cerrar()
        testigo = os.path.join(self.repo, "vivo.txt")
        guion = GUION_DEL_MORIBUNDO.format(
            runtime=RUNTIME, espacio=self.espacio, repo=self.repo,
            instancia="moribundo", paquete=paquete, testigo=testigo,
        )
        proceso = subprocess.Popen([sys.executable, "-c", guion], env=ENTORNO,
                                   stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        try:
            limite = SEGUNDOS_DE_ARRANQUE * 20
            while limite and not os.path.isfile(testigo):
                time.sleep(0.05)
                limite -= 1
            self.assertTrue(os.path.isfile(testigo), "el moribundo no llegó a despachar")
            # Se le da margen a que ABRA el intento —esa transición es la que deja el
            # paquete en `ejecutando`— antes de matarlo. Se comprueba leyendo el ESTADO,
            # que es lo único que no se puede fingir.
            limite = SEGUNDOS_DE_ARRANQUE * 20
            observador = self.abrir_runtime("observador")
            while limite:
                actual = observador.almacen.leer("paquetes/" + paquete + ".json")
                if actual["estado"] in ("despachado", "ejecutando"):
                    break
                time.sleep(0.05)
                limite -= 1
            self.assertIn(actual["estado"], ("despachado", "ejecutando"), actual["estado"])
            os.kill(proceso.pid, signal.SIGKILL)
        finally:
            proceso.wait(timeout=SEGUNDOS_DE_ESPERA)
            # La tubería de `stderr` se cierra: `wait()` no lo hace, y el descriptor
            # abierto acababa como `ResourceWarning` con ruta absoluta en la evidencia.
            if proceso.stderr is not None and not proceso.stderr.closed:
                proceso.stderr.close()
        self.assertEqual(proceso.returncode, -signal.SIGKILL)

        otro = self.abrir_runtime("continua-C")
        continuado = self.continuar(otro)
        en_curso = otro.almacen.leer("paquetes/" + paquete + ".json")
        self.assertIn(en_curso["estado"], ("despachado", "ejecutando"))
        self.assertTrue(en_curso["efecto"])
        self.assertIn(paquete, continuado["5_reportar"]["que_se_esta_construyendo"])
        self.assertIn(paquete, continuado["2_verificar"]["efectos_sin_acuse"])
        # El lease sigue puesto y `Continúa` NO lo roba: `adquirir` nunca roba.
        lease = otro.almacen.leer("leases/" + paquete + ".json")
        self.assertEqual(lease["titular"], "moribundo")
        self.assertNotIn(paquete,
                         [r["paquete"] for r in continuado["4_seleccionar"]["retoma"]])

    def test_22_transicion_confirmada_sin_acuse(self):
        """T204 · escenario 3 · Defecto que previene: dar por producido lo que no consta.

        Se retira del árbol el acuse de un efecto que un paquete `completado` declara haber
        aplicado. `Continúa` lo detecta —el artefacto que dice haber producido no está—, lo
        escala y NO selecciona nada.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        paquete = plan["paquetes"][0]
        rt.despachar(paquete)
        completado = rt.almacen.leer("paquetes/" + paquete + ".json")
        self.assertEqual(completado["estado"], "completado")
        efecto = completado["efecto"]
        os.remove(os.path.join(self.repo, "estado", "canonico", "efectos",
                               efecto + ".json"))
        continuado = self.continuar(rt)
        verificacion = continuado["2_verificar"]
        self.assertTrue(verificacion["bloqueante"])
        nombres = {h["comprobacion"] for h in verificacion["hallazgos"]}
        self.assertTrue(
            {"artefactos-declarados", "deriva-no-transaccional"} & nombres, nombres,
        )
        self.assertEqual(continuado["4_seleccionar"]["retoma"], [])

    def test_23_handoff_pendiente(self):
        """T204 · escenario 4 · Defecto que previene: perder una entrega esperando acuse.

        Una entrega EMITIDA y sin acusar sigue en el emisor. `Continúa` la reporta con su
        instancia, y la reanudación dice la siguiente acción exacta sin hablar con nadie.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        entrega = ciclo.emitir(
            "handoff:con-a-ver", corpus=self.corpus,
            artefactos=["la rama con el cambio construido"],
            checkpoint="las diferencias declaradas",
            trazabilidad={"item": plan["item"], "paquete": plan["paquetes"][0],
                          "ruta": plan["ruta"]},
        )
        durable.escribir(
            rt.almacen, clase="ciclo.handoff.emitido", motivo="entrega pendiente",
            objetos={handoffs.ruta_de(entrega["id"]): entrega},
        )
        continuado = self.continuar(rt)
        self.assertIn("handoff:con-a-ver", continuado["2_verificar"]["handoffs_pendientes"])
        leida = rt.almacen.leer(handoffs.ruta_de(entrega["id"]))
        reanudacion = ciclo.reanudacion(leida)
        self.assertEqual(reanudacion["custodia"], "CON")
        self.assertIn("VER", reanudacion["siguiente_accion"])

        # Y DEJA DE ESTAR PENDIENTE EN CUANTO SE ACUSA. Sin esta mitad, la de arriba
        # pasaría igual con un `Continúa` que reportase la misma entrega para siempre.
        #
        # DEFECTO QUE CIERRA, encontrado por la auditoría independiente: cada transición
        # volvía a derivar el `id` del contenido, así que el acuse se escribía en una RUTA
        # LÓGICA NUEVA y el objeto `emitido` original nunca quedaba superado. `Continúa`
        # publicaba un pendiente FALSO en cada ejecución, indefinidamente, y ninguna prueba
        # lo cogía porque ninguna comprobaba que dejara de estarlo.
        acusada = ciclo.acusar(
            leida, receptor="VER",
            comprobaciones_superadas=ciclo.catalogo(self.corpus)["handoff:con-a-ver"][
                "comprueba_al_recibir"],
        )
        self.assertEqual(acusada["id"], entrega["id"],
                         "la entrega cambió de identidad al acusarse: el objeto anterior "
                         "queda huérfano y `Continúa` lo verá pendiente para siempre")
        durable.escribir(
            rt.almacen, clase="ciclo.handoff.acusado", motivo="acuse de la entrega",
            objetos={handoffs.ruta_de(acusada["id"]): acusada},
        )
        self.assertEqual(len(rt.almacen.listar(handoffs.DOMINIO)), 1,
                         "el acuse creó un objeto NUEVO en vez de superar al anterior")
        despues = self.continuar(rt)
        self.assertNotIn("handoff:con-a-ver",
                         despues["2_verificar"]["handoffs_pendientes"],
                         "la entrega sigue reportándose pendiente DESPUÉS de acusarse")

    def test_24_gate_fallido(self):
        """T204 · escenario 5 · Defecto que previene: seguir como si el gate hubiera pasado.

        Un gate NO superado deja su dictamen escrito y bloquea el paquete. `Continúa` lo ve
        bloqueado, no lo selecciona, y lo presenta en lo que espera decisión del Owner.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        paquete = plan["paquetes"][0]
        declarado = gates.gate("gate:evidencia-suficiente", corpus=self.corpus)
        with self.assertRaises(ciclo.GateFallido) as capturado:
            ciclo.aplicar_gate(
                "gate:evidencia-suficiente", corpus=self.corpus,
                entrada={"paquete": paquete}, evidencia=[], revisor="VER", autor="CON",
                comprobaciones_superadas=[],
            )
        dictamen = capturado.exception.dictamen
        durable.escribir(
            rt.almacen, clase="ciclo.gate.dictaminado", motivo="dictamen negativo",
            objetos={gates.ruta_de(dictamen["id"]): dictamen},
        )
        rt._mover(paquete, "bloqueado", motivo="el gate no se superó", autoridad="VER",
                  clase="runtime.paquete.bloqueado")
        continuado = self.continuar(rt)
        self.assertIn(paquete, continuado["5_reportar"]["que_espera_decision_del_owner"])
        self.assertNotIn(paquete,
                         [r["paquete"] for r in continuado["4_seleccionar"]["retoma"]])
        self.assertEqual(rt.almacen.leer(gates.ruta_de(dictamen["id"]))["dictamen"],
                         "no-superado")
        del declarado

    def test_25_paquete_pausado(self):
        """T204 · escenario 6 · Defecto que previene: desaparcar lo que el Owner aparcó.

        Un paquete PAUSADO no es elegible y `Continúa` no lo retoma: lo lista como aparcado.
        Reanudarlo es una orden explícita, no una consecuencia de continuar.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        paquete = plan["paquetes"][0]
        rt.pausar(paquete, motivo="el Owner lo aparca", autoridad="OWNER")
        continuado = self.continuar(rt)
        self.assertIn(paquete, continuado["5_reportar"]["que_esta_aparcado"])
        self.assertNotIn(paquete,
                         [r["paquete"] for r in continuado["4_seleccionar"]["retoma"]])
        self.assertEqual(rt.almacen.leer("paquetes/" + paquete + ".json")["estado"],
                         "pausado")

    def test_26_reconciliacion_abierta(self):
        """T204 · escenario 7 · Defecto que previene: despachar con una pendencia abierta.

        `§7.4`: «¿hay `reconciliacion_pendiente`? → resolverla antes de nada». `Continúa` la
        reporta como BLOQUEANTE, escala a la autoridad que `g.9` nombra y no selecciona.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        registro = rt.almacen.abrir_reconciliacion(
            producto="prueba", repositorio="control", item=plan["paquetes"][0],
            intento=1, causa="AMBIGUO: no se sabe si el efecto se aplicó",
        )
        continuado = self.continuar(rt)
        verificacion = continuado["2_verificar"]
        self.assertIn(registro, verificacion["reconciliaciones_pendientes"])
        self.assertTrue(verificacion["bloqueante"])
        hallazgo = [h for h in verificacion["hallazgos"]
                    if h["comprobacion"] == "reconciliacion-pendiente"][0]
        self.assertIn("g.9", hallazgo["escala_a"] or hallazgo["detalle"])
        self.assertEqual(continuado["4_seleccionar"]["retoma"], [])

    def test_27_trabajo_automatico_por_politica(self):
        """T204 · escenario 8 · Defecto que previene: preguntar por lo que ya está autorizado.

        `b.15.1`: dentro del alcance ya autorizado, DSP crea y despacha el desbloqueador SIN
        preguntar. `Continúa` lo encuentra elegible, con la prioridad más alta, y lo retoma
        sin que aparezca ninguna decisión del Owner.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        bloqueado = plan["paquetes"][0]
        rt._mover(bloqueado, "bloqueado", motivo="falta una decisión externa",
                  autoridad="DSP", clase="runtime.paquete.bloqueado")
        planificador = ciclo.Planificador(rt, corpus=self.corpus)
        capacidad = plan["alcance_autorizado"]["capacidades"][0]
        abierto = planificador.abrir_desbloqueador(
            plan, bloqueado, capacidad=capacidad,
            orden=self.orden([capacidad])[capacidad],
            motivo="el desbloqueador que `b.15.1` autoriza",
        )
        continuado = self.continuar(rt, frente=1)
        self.assertEqual(continuado["4_seleccionar"]["retoma"][0]["paquete"],
                         abierto["paquete"])
        fila = [f for f in abierto["plan"]["correspondencia"]
                if f["paquete"] == abierto["paquete"]][0]
        self.assertEqual(fila["abierto_por"], "b.15.1")
        self.assertEqual(fila["desbloquea"], bloqueado)

    def test_28_proyecto_con_dos_repositorios(self):
        """T204 · escenario 9 · Defecto que previene: un `Continúa` que sólo ve una fuente.

        Dos repositorios Git REALES, declarados en `SOURCES.toml` y materializados como
        hermanos. El encuadre descubre los dos, el alcance autorizado los lleva y `Continúa`
        planifica sobre el control repo sin confundirlos.
        """
        taller = tempfile.mkdtemp(prefix="ads-workspace-")
        self.addCleanup(shutil.rmtree, taller, True)
        for nombre in ("frontend", "backend"):
            destino = os.path.join(taller, nombre)
            os.makedirs(destino)
            subprocess.run(["git", "init", "-q", destino], check=True,
                           capture_output=True, timeout=SEGUNDOS_DE_ESPERA)
        with open(os.path.join(self.repo, "SOURCES.toml"), "w", encoding="utf-8") as fichero:
            fichero.write(
                'schema = 1\n[workspace]\nlayout = "siblings"\n\n'
                '[[sources]]\nid = "frontend"\nremote = "ssh://git@host/org/f.git"\n'
                'path = "frontend"\n\n'
                '[[sources]]\nid = "backend"\nremote = "ssh://git@host/org/b.git"\n'
                'path = "backend"\n'
            )
        rt = self.abrir_runtime()
        marco, ruta, plan = self.preparar(rt)
        self.assertEqual([f["id"] for f in marco["fuentes"]["fuentes"]],
                         ["backend", "frontend"])
        self.assertEqual(plan["alcance_autorizado"]["fuentes"], ["backend", "frontend"])
        continuado = self.continuar(rt)
        self.assertTrue(continuado["4_seleccionar"]["retoma"])
        self.assertNotIn("ssh://", json.dumps(marco, ensure_ascii=False))
        del ruta

    def test_29_estado_sin_trabajo_elegible(self):
        """T204 · escenario 10 · Defecto que previene: fabricar trabajo para parecer útil.

        `b.15`, punto 8: «no hay trabajo listo» es una respuesta correcta y completa. Con el
        estado vacío, `Continúa` lo dice, no selecciona nada y NO abre nada.
        """
        rt = self.abrir_runtime()
        antes = rt.almacen.revision()
        continuado = self.continuar(rt)
        self.assertEqual(continuado["4_seleccionar"]["retoma"], [])
        self.assertIn("no hay trabajo", continuado["4_seleccionar"]["motivo"])
        self.assertEqual(continuado["6_cargar"], [])
        self.assertEqual(rt.almacen.revision()["revision_id"], antes["revision_id"])
        self.assertEqual(rt.almacen.listar("paquetes"), [])


# =========================================================================
# T205 · la propiedad central, la carga y la ejecución no interactiva
# =========================================================================
class PropiedadCentral(BaseDeContinua):

    def test_40_dos_ejecuciones_seguidas_dan_los_mismos_bytes_y_no_mueven_el_estado(self):
        """T205 · Defecto que previene: un `Continúa` que cambia lo que observa.

        LA PROPIEDAD CENTRAL. Dos ejecuciones consecutivas sin cambios producen el MISMO
        plan byte a byte y NO modifican el estado: se comparan `revision_id` y `cid_raiz`
        antes y después, y el volcado JSON de los dos planes.
        """
        rt = self.abrir_runtime()
        self.preparar(rt)
        antes = rt.almacen.revision()
        primera = self.continuar(rt)
        intermedia = rt.almacen.revision()
        segunda = self.continuar(rt)
        despues = rt.almacen.revision()
        self.assertEqual(json.dumps(primera, sort_keys=True, ensure_ascii=False),
                         json.dumps(segunda, sort_keys=True, ensure_ascii=False))
        self.assertEqual(primera["huella"], segunda["huella"])
        self.assertEqual(antes["revision_id"], intermedia["revision_id"])
        self.assertEqual(antes["revision_id"], despues["revision_id"])
        self.assertEqual(antes["cid_raiz"], despues["cid_raiz"])

    def test_41_dos_instancias_distintas_producen_el_mismo_plan(self):
        """T205 · Defecto que previene: un plan que depende de quién lo calculó.

        El plan de continuación no lleva la instancia del runtime, ni el `cwd`, ni ninguna
        ruta de la máquina. Dos runtimes con nombres distintos sobre el MISMO estado dan el
        mismo plan.
        """
        rt = self.abrir_runtime("continua-uno")
        self.preparar(rt)
        primera = self.continuar(rt)
        rt.cerrar()
        otro = self.abrir_runtime("continua-dos")
        segunda = self.continuar(otro)
        self.assertEqual(primera["huella"], segunda["huella"])
        self.assertNotIn(self.repo, json.dumps(primera, ensure_ascii=False))
        self.assertNotIn("continua-uno", json.dumps(primera, ensure_ascii=False))

    def test_42_el_paso_6_entrega_el_checkpoint_de_la_capacidad_con_custodia(self):
        """T205 · Defecto que previene: retomar sin saber quién tenía la custodia.

        Paso 6 de `b.14`: cargar el checkpoint de la capacidad con custodia y comprobar su
        `based_on`. El plan trae capacidad, método, gate, obligación y `based_on` leído del
        estado.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        continuado = self.continuar(rt, frente=2)
        self.assertEqual(len(continuado["6_cargar"]), 2)
        for carga in continuado["6_cargar"]:
            self.assertIn(carga["paquete"], plan["paquetes"])
            self.assertEqual(carga["plan"], plan["id"])
            self.assertIn(carga["capacidad"], [f["capacidad"]
                                               for f in plan["correspondencia"]])
            self.assertEqual(
                carga["checkpoint"]["based_on"],
                rt.almacen.revision()["raiz"]["paquetes/" + carga["paquete"] + ".json"],
            )

    def test_43_la_ejecucion_no_interactiva_se_niega_si_falta_una_decision(self):
        """T205 · Defecto que previene: que `Continúa` elija por el Owner.

        Con una decisión pendiente y ejecución NO INTERACTIVA, se levanta
        `DECISION_DEL_OWNER_PENDIENTE` y no se despacha nada. Sin decisión pendiente, la
        ejecución no interactiva sí trabaja.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        pausado = plan["paquetes"][0]
        rt.pausar(pausado, motivo="espera al Owner", autoridad="OWNER")
        with self.assertRaises(ciclo.DecisionDelOwnerPendiente) as capturado:
            self.continuar(rt, modo=ciclo.MODO_EJECUCION, no_interactivo=True)
        self.assertIn(pausado, capturado.exception.contexto["espera"])
        rt.reanudar(pausado, motivo="el Owner lo retoma", autoridad="OWNER")
        ejecutado = self.continuar(rt, modo=ciclo.MODO_EJECUCION, no_interactivo=True)
        self.assertTrue(ejecutado["7_trabajar"]["ejecutado"])
        self.assertEqual(len(ejecutado["7_trabajar"]["atendidos"]), 1)

    def test_44_el_trabajo_ambiguo_para_y_escala_sin_inventar_estado(self):
        """T205 · Defecto que previene: elegir entre dos lecturas igual de defendibles.

        `b.14.3`: DSP para y escala, NUNCA inventa estado. Un paquete elegible que ningún
        plan reconoce es exactamente eso, y `Continúa` lo nombra.
        """
        rt = self.abrir_runtime()
        _marco, _ruta, plan = self.preparar(rt)
        rt.crear_item(id="it-suelto", titulo="sin plan", motivo="alta suelta")
        rt.crear_paquete(
            id="pq-suelto", item="it-suelto", capacidades_requeridas=["proceso-local"],
            orden=self.orden(["X"])["X"], prioridad=99,
        )
        with self.assertRaises(ciclo.TrabajoAmbiguo) as capturado:
            self.continuar(rt)
        self.assertIn("pq-suelto", capturado.exception.contexto["paquetes"])
        del plan

    def test_45_el_reporte_del_paso_5_es_breve_y_no_pide_permiso(self):
        """T205 · Defecto que previene: un informe que hay que leer entero para actuar.

        `b.14`, nota 2: el paso 5 es obligatorio y BREVE, y no se pide permiso. Seis líneas
        con las cinco preguntas, deterministas y sin rutas de la máquina.
        """
        rt = self.abrir_runtime()
        self.preparar(rt)
        lineas = continuacion.como_texto(self.continuar(rt))
        self.assertEqual(len(lineas), 7)
        texto = "\n".join(lineas)
        for etiqueta in ("construyendo", "retoma", "por que", "espera owner", "aparcado",
                         "inanicion", "hallazgos"):
            self.assertIn(etiqueta, texto)
        self.assertNotIn(self.repo, texto)


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de `test_runtime.py`, no importado: la batería de `Continúa` no puede depender
    de otra batería para poder ejecutarse. La salida se PUBLICA como evidencia.
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
