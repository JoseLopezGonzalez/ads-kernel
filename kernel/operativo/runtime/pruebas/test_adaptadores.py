#!/usr/bin/env python3
"""test_adaptadores — batería del CONTRATO DE ADAPTADOR y la HUELLA. Escenario `T191`.

Corte `V7`. Lo que se demuestra con procesos REALES, no con simulacros:

    ejecutar · progreso · terminar bien · fallar · exceder el timeout MATANDO el grupo de
    procesos · ser cancelado matando de verdad · morir abruptamente · reanudar tras el
    recibo · y que un resultado confirmado NO se aplica dos veces

Y de la proyección: compilar estampando la HUELLA de las entradas, y el validador de deriva
con sus TRES diagnósticos —`AL_DIA`, `EDITADA_A_MANO`, `OBSOLETA`—.

**FUERA DE ALCANCE, declarado:** la pieza 4 de `11-ARQ` §6, la prueba de humo en sesión
nueva. Exige abrir un entorno de agente real; §6.5 dice que sin ella el nivel alcanzado es
`desconocido`, y aquí no se declara ningún nivel.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import sys
import tempfile
import time
import unittest

RAIZ_RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ_RUNTIME)

import adaptadores                                                   # noqa: E402
from adaptadores import proyeccion                                   # noqa: E402


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de `tooling/tests/test_workspace.py`, no importado: la salida se PUBLICA como
    evidencia y «Ran 29 tests in 1.697s» cambiaría en cada ejecución.
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


def _vivo(pid):
    """`os.kill(pid, 0)` no manda señal: pregunta si el proceso sigue estando."""
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


# ===========================================================================
#  El registro y la ficha
# ===========================================================================
class _AdaptadorDeVersionAjena(adaptadores.Adaptador):
    identificador = "de-otra-version"
    version_de_contrato = 99
    capacidades = ("proceso-local",)


class _AdaptadorDeCapacidadUnica(adaptadores.Adaptador):
    identificador = "solo-remoto"
    version_de_contrato = adaptadores.VERSION_DE_CONTRATO
    capacidades = ("proceso-remoto",)


class RegistroYFicha(unittest.TestCase):

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-adp-")
        self.addCleanup(shutil.rmtree, self.directorio, True)
        self.adaptador = adaptadores.AdaptadorDeProcesoLocal(self.directorio)

    def test_la_ficha_declara_los_trece_campos_de_3_4(self):
        """T191 · Defecto que previene: una ficha con huecos que valida contra su tipo."""
        ficha = self.adaptador.ficha().a_dict()
        self.assertEqual(tuple(ficha), adaptadores.CAMPOS_DE_FICHA)
        self.assertEqual(ficha["version"], adaptadores.VERSION_DE_CONTRATO)

    def test_una_ficha_incompleta_no_se_construye(self):
        """T191 · Defecto que previene: que una ausencia se lea como valor por defecto."""
        with self.assertRaises(adaptadores.OrdenInvalida) as capturado:
            adaptadores.FichaDeAdaptador(identificador="x", version=1)
        self.assertIn("los trece campos", str(capturado.exception))

    def test_la_ficha_no_tiene_campo_nivel(self):
        """T191 · Defecto que previene: `nivel` editable, la segunda verdad que `I5` prohíbe."""
        self.assertNotIn("nivel", adaptadores.CAMPOS_DE_FICHA)
        self.assertNotIn("nivel", self.adaptador.ficha().a_dict())

    def test_se_selecciona_por_capacidad_declarada(self):
        """T191 · Control POSITIVO: el paquete pide capacidades, no nombres de proveedor."""
        registro = adaptadores.RegistroDeAdaptadores([self.adaptador])
        elegido = registro.seleccionar(["proceso-local"])
        self.assertIs(elegido, self.adaptador)
        self.assertEqual(registro.capacidades()["proceso-local"], ["proceso-local"])

    def test_capacidad_no_soportada(self):
        """T191 · Defecto que previene: despachar a un adaptador que no puede hacerlo."""
        registro = adaptadores.RegistroDeAdaptadores([self.adaptador])
        with self.assertRaises(adaptadores.CapacidadNoSoportada):
            registro.seleccionar(["proceso-remoto"])
        with self.assertRaises(adaptadores.CapacidadNoSoportada):
            registro.seleccionar([])

    def test_version_de_contrato_incompatible(self):
        """T191 · Defecto que previene: aceptar un adaptador de otra versión del contrato."""
        registro = adaptadores.RegistroDeAdaptadores()
        with self.assertRaises(adaptadores.AdaptadorIncompatible) as capturado:
            registro.registrar(_AdaptadorDeVersionAjena())
        self.assertEqual(capturado.exception.codigo, "ADAPTADOR_INCOMPATIBLE")

    def test_el_desempate_es_determinista(self):
        """T191 · Defecto que previene: que el despacho dependa del orden de importación."""
        otro = adaptadores.AdaptadorDeProcesoLocal(self.directorio)
        otro.identificador = "aaa-proceso-local"
        registro = adaptadores.RegistroDeAdaptadores([self.adaptador, otro])
        for _ in range(3):
            self.assertEqual(registro.seleccionar(["proceso-local"]).identificador,
                             "aaa-proceso-local")

    def test_la_interfaz_base_falla_cerrado(self):
        """T191 · Defecto que previene: un resultado inventado, y un acuse durable de nada."""
        base = adaptadores.Adaptador()
        with self.assertRaises(adaptadores.ErrorDeAdaptador):
            base.ejecutar({}, efecto="ef-1", limite_segundos=1)
        with self.assertRaises(adaptadores.ErrorDeAdaptador):
            base.ficha()

    def test_un_resultado_con_otra_forma_se_rechaza(self):
        """T191 · Defecto que previene: un acuse cruzado que aplica un efecto por otro."""
        with self.assertRaises(adaptadores.ErrorDeAdaptador):
            adaptadores.comprobar_resultado({"estado": "completado"}, "ef-1")
        completo = {"estado": "completado", "codigo": 0, "salida": "", "detalle": "",
                    "reintentable": False, "efecto": "ef-2", "repetido": False}
        with self.assertRaises(adaptadores.ErrorDeAdaptador) as capturado:
            adaptadores.comprobar_resultado(completo, "ef-1")
        self.assertIn("acuse cruzado", str(capturado.exception))
        completo["estado"] = "inventado"
        completo["efecto"] = "ef-1"
        with self.assertRaises(adaptadores.ErrorDeAdaptador):
            adaptadores.comprobar_resultado(completo, "ef-1")


# ===========================================================================
#  El adaptador local REAL
# ===========================================================================
class ProcesoLocalReal(unittest.TestCase):

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-proc-")
        self.addCleanup(shutil.rmtree, self.directorio, True)
        self.adaptador = adaptadores.AdaptadorDeProcesoLocal(self.directorio)

    def _orden(self, guion):
        return {"operacion": "ejecutar", "argumentos": ["/bin/sh", "-c", guion]}

    def test_ejecuta_una_tarea_y_emite_progreso_linea_a_linea(self):
        """T191 · Defecto que previene: «progreso» que es un diccionario devuelto al final."""
        recogido = []
        resultado = self.adaptador.ejecutar(
            self._orden("echo uno; echo dos; echo tres"),
            efecto="ef-progreso", limite_segundos=20, progreso=recogido.append,
        )
        self.assertEqual(resultado["estado"], "completado")
        self.assertEqual(resultado["codigo"], 0)
        self.assertEqual([entrada["texto"] for entrada in recogido], ["uno", "dos", "tres"])
        self.assertEqual([entrada["linea"] for entrada in recogido], [1, 2, 3])
        self.assertEqual({entrada["efecto"] for entrada in recogido}, {"ef-progreso"})

    def test_una_tarea_que_falla_no_es_reintentable(self):
        """T191 · Defecto que previene: reintentar en bucle un fallo que no puede cambiar."""
        resultado = self.adaptador.ejecutar(self._orden("echo mal >&2; exit 7"),
                                            efecto="ef-fallo", limite_segundos=20)
        self.assertEqual(resultado["estado"], "fallido")
        self.assertEqual(resultado["codigo"], 7)
        self.assertFalse(resultado["reintentable"])
        self.assertIn("mal", resultado["salida"])

    def test_el_timeout_mata_el_grupo_de_procesos_de_verdad(self):
        """T191 · Defecto que previene: un «timeout» que deja al nieto vivo y colgado."""
        recogido = []
        resultado = self.adaptador.ejecutar(
            self._orden("sleep 300 & echo $!; wait"),
            efecto="ef-timeout", limite_segundos=1.0, progreso=recogido.append,
        )
        self.assertEqual(resultado["estado"], "timeout")
        self.assertTrue(resultado["reintentable"])
        self.assertIn("GRUPO de procesos", resultado["detalle"])

        pid_hijo = resultado["pid"]
        pid_nieto = int(recogido[0]["texto"].strip())
        limite = time.monotonic() + 5
        while (_vivo(pid_hijo) or _vivo(pid_nieto)) and time.monotonic() < limite:
            time.sleep(0.05)
        self.assertFalse(_vivo(pid_hijo), "el hijo tiene que estar muerto")
        self.assertFalse(_vivo(pid_nieto),
                         "el NIETO también: por eso se mata el grupo y no el proceso")

    def test_la_cancelacion_tambien_mata(self):
        """T191 · Defecto que previene: una cancelación que sólo lo pide por favor."""
        cancelacion = adaptadores.Cancelacion()
        cancelacion.activar()
        resultado = self.adaptador.ejecutar(self._orden("sleep 300 & wait"),
                                            efecto="ef-cancelado", limite_segundos=60,
                                            cancelacion=cancelacion)
        self.assertEqual(resultado["estado"], "cancelado")
        self.assertFalse(resultado["reintentable"], "cancelar no es un fallo transitorio")
        limite = time.monotonic() + 5
        while _vivo(resultado["pid"]) and time.monotonic() < limite:
            time.sleep(0.05)
        self.assertFalse(_vivo(resultado["pid"]))

    def test_una_muerte_abrupta_se_distingue_de_un_fallo_de_la_tarea(self):
        """T191 · Defecto que previene: confundir «la mataron» con «salió mal»."""
        resultado = self.adaptador.ejecutar(
            self._orden("kill -9 $$"), efecto="ef-abrupto", limite_segundos=20
        )
        self.assertEqual(resultado["estado"], "fallido")
        self.assertLess(resultado["codigo"], 0)
        self.assertIn("murió por la señal", resultado["detalle"])
        self.assertTrue(resultado["reintentable"])

    def test_un_efecto_confirmado_no_se_aplica_dos_veces(self):
        """T191 · Defecto que previene: repetir un efecto ya aplicado tras una caída."""
        testigo = os.path.join(self.directorio, "testigo.txt")
        orden = self._orden("echo x >> " + json.dumps(testigo))
        primero = self.adaptador.ejecutar(orden, efecto="ef-idem", limite_segundos=20)
        self.assertFalse(primero["repetido"])
        with open(testigo, "rb") as manejador:
            self.assertEqual(manejador.read(), b"x\n")

        segundo = self.adaptador.ejecutar(orden, efecto="ef-idem", limite_segundos=20)
        self.assertTrue(segundo["repetido"])
        self.assertEqual(segundo["estado"], primero["estado"])
        self.assertEqual(segundo["codigo"], primero["codigo"])
        with open(testigo, "rb") as manejador:
            self.assertEqual(manejador.read(), b"x\n",
                             "la tarea NO se volvió a ejecutar")

    def test_el_recibo_es_durable_y_sobrevive_a_otra_instancia(self):
        """T191 · Defecto que previene: una idempotencia que vive sólo en memoria."""
        orden = self._orden("echo hecho")
        self.adaptador.ejecutar(orden, efecto="ef-durable", limite_segundos=20)
        otra = adaptadores.AdaptadorDeProcesoLocal(self.directorio)
        resultado = otra.ejecutar(orden, efecto="ef-durable", limite_segundos=20)
        self.assertTrue(resultado["repetido"])

    def test_un_timeout_no_deja_recibo_y_por_eso_se_puede_reintentar(self):
        """T191 · Defecto que previene: dar por aplicado un efecto que nunca terminó."""
        self.adaptador.ejecutar(self._orden("sleep 300"), efecto="ef-sin-recibo",
                                limite_segundos=1.0)
        self.assertIsNone(self.adaptador.recibo("ef-sin-recibo"))
        resultado = self.adaptador.ejecutar(self._orden("echo reanudado"),
                                            efecto="ef-sin-recibo", limite_segundos=20)
        self.assertFalse(resultado["repetido"])
        self.assertEqual(resultado["estado"], "completado")

    def test_el_recibo_no_guarda_ni_un_milisegundo(self):
        """T191 · Defecto que previene: meter reloj en algo que se compara byte a byte."""
        self.adaptador.ejecutar(self._orden("echo x"), efecto="ef-limpio",
                                limite_segundos=20)
        recibo = self.adaptador.recibo("ef-limpio")
        self.assertEqual(sorted(recibo),
                         ["codigo", "detalle", "efecto", "estado", "reintentable", "salida"])
        self.assertNotIn("pid", recibo)

    def test_una_orden_sin_argumentos_no_se_ejecuta(self):
        """T191 · Defecto que previene: lanzar «algo» cuando no se dijo qué."""
        for orden in ({}, {"argumentos": []}, {"argumentos": ["x"], "operacion": "otra"}):
            with self.subTest(orden=str(orden)):
                with self.assertRaises(adaptadores.OrdenInvalida):
                    self.adaptador.ejecutar(orden, efecto="ef-x", limite_segundos=1)

    def test_un_identificador_de_efecto_con_barra_se_rechaza(self):
        """T191 · Defecto que previene: escribir el recibo fuera del espacio de trabajo."""
        for efecto in ("../fuera", "a/b", "..", "."):
            with self.subTest(efecto=efecto):
                with self.assertRaises(adaptadores.OrdenInvalida):
                    self.adaptador.ejecutar(self._orden("echo x"), efecto=efecto,
                                            limite_segundos=5)


# ===========================================================================
#  La proyección, su huella y su validador de deriva
# ===========================================================================
class HuellaYDeriva(unittest.TestCase):

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-proy-")
        self.addCleanup(shutil.rmtree, self.directorio, True)
        self.entradas = {
            "definicion": b"ads:adaptador entorno-uno\n",
            "kernel": b"KERNEL v1\n",
            "packs": b"pack-web\n",
            "perfil": b"PROFILE=producto\n",
        }
        self.texto = proyeccion.compilar(
            adaptador="entorno-uno", version_de_ads="1.0",
            entradas=self.entradas, cuerpo="instrucciones del entorno\n",
            origen_canonico="ads/adaptadores/entorno-uno/",
        )

    def test_la_proyeccion_lleva_aviso_huella_y_origen(self):
        """T191 · Defecto que previene: una proyección que no dice que es generada."""
        self.assertIn(proyeccion.AVISO, self.texto)
        self.assertIn("ads:huella ", self.texto)
        self.assertIn("ads:origen ads/adaptadores/entorno-uno/", self.texto)
        self.assertIn("ads:version-de-ads 1.0", self.texto)

    def test_recompilar_con_las_mismas_entradas_da_los_mismos_bytes(self):
        """T191 · Control POSITIVO: recompilar y comparar es determinista (§6.3)."""
        otra = proyeccion.compilar(
            adaptador="entorno-uno", version_de_ads="1.0",
            entradas=dict(reversed(list(self.entradas.items()))),
            cuerpo="instrucciones del entorno\n",
            origen_canonico="ads/adaptadores/entorno-uno/",
        )
        self.assertEqual(self.texto, otra)

    def test_al_dia(self):
        """T191 · Control POSITIVO: sin tocar nada, la proyección está al día."""
        informe = proyeccion.validar_deriva(self.texto, self.entradas)
        self.assertEqual(informe["diagnostico"], proyeccion.AL_DIA)
        self.assertTrue(proyeccion.exigir_al_dia(self.texto, self.entradas))

    def test_editada_a_mano(self):
        """T191 · Defecto que previene: `P-06`, editar la proyección en vez de la fuente."""
        editada = self.texto.replace("instrucciones del entorno",
                                     "instrucciones EDITADAS a mano")
        informe = proyeccion.validar_deriva(editada, self.entradas)
        self.assertEqual(informe["diagnostico"], proyeccion.EDITADA_A_MANO)
        self.assertIn("recompilar", informe["remedio"])
        with self.assertRaises(adaptadores.ProyeccionDerivada):
            proyeccion.exigir_al_dia(editada, self.entradas)

    def test_quitar_la_cabecera_tambien_es_editar_a_mano(self):
        """T191 · Defecto que previene: borrar el aviso y que la huella no lo note."""
        sin_cabecera = "\n".join(linea for linea in self.texto.splitlines()
                                 if not linea.startswith("# ads:huella"))
        informe = proyeccion.validar_deriva(sin_cabecera + "\n", self.entradas)
        self.assertEqual(informe["diagnostico"], proyeccion.EDITADA_A_MANO)

    def test_obsoleta(self):
        """T191 · Defecto que previene: confundir «obsoleta» con «editada» (`P-08`)."""
        nuevas = dict(self.entradas)
        nuevas["kernel"] = b"KERNEL v2\n"
        informe = proyeccion.validar_deriva(self.texto, nuevas)
        self.assertEqual(informe["diagnostico"], proyeccion.OBSOLETA)
        self.assertNotEqual(informe["huella_declarada"], informe["huella_vigente"])
        with self.assertRaises(adaptadores.ProyeccionObsoleta):
            proyeccion.exigir_al_dia(self.texto, nuevas)

    def test_dos_proyecciones_que_dicen_cosas_distintas_sobre_lo_mismo(self):
        """T191 · Defecto que previene: `CAND-016`, dos memorias que divergieron 23 contra 32."""
        otras = dict(self.entradas)
        otras["packs"] = b"pack-movil\n"
        segunda = proyeccion.compilar(
            adaptador="entorno-dos", version_de_ads="1.0", entradas=otras,
            cuerpo="otras instrucciones\n", origen_canonico="ads/adaptadores/entorno-dos/",
        )
        informe = proyeccion.comparar_proyecciones(
            {"AGENTS.md": self.texto, "INSTRUCCIONES.md": segunda}
        )
        self.assertFalse(informe["coherentes"])
        self.assertIn("dicen cosas distintas", informe["detalle"])
        coherentes = proyeccion.comparar_proyecciones(
            {"AGENTS.md": self.texto, "INSTRUCCIONES.md": self.texto}
        )
        self.assertTrue(coherentes["coherentes"])

    def test_escribir_y_releer_conserva_el_diagnostico(self):
        """T191 · Defecto que previene: perder la huella al pasar por el disco."""
        ruta = os.path.join(self.directorio, "AGENTS.md")
        proyeccion.escribir(ruta, self.texto)
        with open(ruta, "r", encoding="utf-8") as manejador:
            releido = manejador.read()
        self.assertEqual(
            proyeccion.validar_deriva(releido, self.entradas)["diagnostico"],
            proyeccion.AL_DIA,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
