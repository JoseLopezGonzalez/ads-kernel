#!/usr/bin/env python3
"""test_contencion — batería de `FD-5`, el AISLAMIENTO DE PROCESOS. `T214` a `T216`.

    `T214`  DETECCIÓN de las capacidades del anfitrión, sonda a sonda y con su motivo
    `T215`  CONTENCIÓN FUERTE: hijo, nieto y bisnieto, los tres haciendo `setsid`, y
            NINGUNO sobrevive a la cancelación ni al timeout
    `T216`  el backend SIMPLE, con su nivel INFERIOR declarado, el bisnieto que SÍ escapa, y
            el FALLO CERRADO cuando la política exige contención fuerte y no la hay

**LA PAREJA `T215`/`T216` ES LA PRUEBA QUE IMPIDE PRESENTAR EL DÉBIL COMO FUERTE.** Con el
backend fuerte no sobrevive nadie; con el simple sobrevive quien se salió del grupo. Si las
dos dieran lo mismo, una de las dos estaría mal escrita.

Todo con procesos REALES: se localizan por su marca en `/proc/<pid>/cmdline` —que es la única
forma de verlos desde fuera de un espacio de nombres de PID— y se comprueban uno a uno con
`os.kill(pid, 0)`.
"""
from __future__ import annotations

import os
import re
import shlex
import shutil
import signal
import sys
import tempfile
import unittest

RAIZ_RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ_RUNTIME)

import contencion                                                    # noqa: E402
from adaptadores.contrato import Cancelacion                         # noqa: E402
from contencion import backends, deteccion, politica as modulo_politica  # noqa: E402

SEGUNDOS_DE_LA_TAREA = 90


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de `tooling/tests/test_workspace.py`, no importado: esa batería vive en
    `tooling/` y no está en la ruta de importación del runtime. La salida se PUBLICA como
    evidencia y tiene que ser byte-idéntica entre ejecuciones.
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


# ===========================================================================
#  La TAREA GENERACIONAL: hijo, nieto y bisnieto, los tres con `setsid`
# ===========================================================================
#  Cada generación lleva su propia MARCA en la línea de órdenes, y las marcas ANIDAN: la del
#  bisnieto está también en el cuerpo del nieto, del hijo y de la raíz, porque cada capa
#  contiene el texto de la siguiente. Por eso una generación se identifica RESTANDO: los
#  procesos que llevan la marca del nieto y NO la del hijo son los nietos.
def _capa(marca, interior, segundos):
    cuerpo = ": " + marca + "\n" + interior + "sleep " + str(segundos) + "\n"
    return "setsid sh -c " + shlex.quote(cuerpo) + " &\n"


def tarea_generacional(prefijo, segundos=SEGUNDOS_DE_LA_TAREA):
    """`sh` que engendra hijo, nieto y bisnieto, cada uno con `setsid`, y anuncia `listo`."""
    bisnieto = _capa(prefijo + "-BISNIETO", "", segundos)
    nieto = _capa(prefijo + "-NIETO", bisnieto, segundos)
    hijo = _capa(prefijo + "-HIJO", nieto, segundos)
    guion = (": " + prefijo + "-RAIZ\n" + hijo
             + "sleep 0.6\n"
             + "echo listo\n"
             + "sleep " + str(segundos) + "\n")
    return ["sh", "-c", guion]


def generaciones(prefijo):
    """`{raiz, hijo, nieto, bisnieto}` con los PID del ANFITRIÓN de cada generación."""
    raiz = set(contencion.pids_con_marca(prefijo + "-RAIZ"))
    con_hijo = set(contencion.pids_con_marca(prefijo + "-HIJO"))
    con_nieto = set(contencion.pids_con_marca(prefijo + "-NIETO"))
    con_bisnieto = set(contencion.pids_con_marca(prefijo + "-BISNIETO"))
    return {
        "raiz": sorted(raiz),
        "hijo": sorted(con_hijo - raiz),
        "nieto": sorted(con_nieto - con_hijo),
        "bisnieto": sorted(con_bisnieto - con_nieto),
    }


class BaseDeContencion(unittest.TestCase):
    """Espacio de trabajo temporal, marca única por prueba y remate de supervivientes."""

    def setUp(self):
        self.espacio = tempfile.mkdtemp(prefix="ads-cont-")
        self.addCleanup(shutil.rmtree, self.espacio, ignore_errors=True)
        self.prefijo = "ADSFD5" + os.urandom(6).hex().upper()
        self.addCleanup(self._rematar)
        self.capacidades = contencion.capacidades()

    def _rematar(self):
        """Ningún superviviente de una prueba sobrevive a la batería. Ni uno."""
        for pid in contencion.pids_con_marca(self.prefijo):
            try:
                os.kill(pid, signal.SIGKILL)
            except OSError:
                # Ya no está, o no es nuestro. En los dos casos no hay nada que rematar.
                continue

    def _correr(self, backend, nivel, *, modo, limite=25.0):
        """Lanza la tarea generacional y devuelve `(resultado, generaciones capturadas)`.

        `modo` es `cancelacion` o `timeout`. En los dos casos las generaciones se capturan
        DESDE DENTRO del progreso, cuando la tarea anuncia `listo`: es el único instante en
        que consta que las tres existen.
        """
        cancelacion = Cancelacion()
        capturadas = {}

        def progreso(apunte):
            if apunte["texto"].strip() != "listo" or capturadas:
                return
            capturadas.update(generaciones(self.prefijo))
            if modo == "cancelacion":
                cancelacion.activar()

        resultado = contencion.ejecutar(
            tarea_generacional(self.prefijo),
            espacio=self.espacio,
            limite_segundos=limite if modo == "cancelacion" else 2.5,
            politica=contencion.Politica(nivel, backend=backend),
            marca=self.prefijo,
            progreso=progreso,
            cancelacion=cancelacion if modo == "cancelacion" else None,
            capacidades=self.capacidades,
        )
        return resultado, capturadas


# ===========================================================================
#  T214 · DETECCIÓN de capacidades del anfitrión
# ===========================================================================
class DeteccionDeCapacidades(BaseDeContencion):

    def test_se_sondean_todos_los_backends_del_orden_declarado(self):
        """T214 · Defecto que previene: elegir un backend sin haber mirado los demás."""
        sondeados = [fila["backend"] for fila in self.capacidades["backends"]]
        self.assertEqual(sondeados, list(deteccion.ORDEN_DE_PREFERENCIA))

    def test_cada_sonda_publica_su_motivo(self):
        """T214 · Defecto que previene: un «no disponible» sin causa, que nadie puede corregir."""
        for fila in self.capacidades["backends"]:
            with self.subTest(backend=fila["backend"]):
                self.assertTrue(fila["motivo"])
                self.assertIn(fila["nivel"], deteccion.NIVELES)

    def test_el_nivel_de_cada_backend_es_del_vocabulario_cerrado(self):
        """T214 · Defecto que previene: inventar un nivel intermedio que no significa nada."""
        for identificador, clase in backends.CLASES.items():
            with self.subTest(backend=identificador):
                self.assertIn(clase.nivel, deteccion.NIVELES)
                self.assertEqual(clase.nivel,
                                 deteccion.NIVEL_POR_BACKEND[identificador])

    def test_la_sonda_de_cgroup_ejerce_el_mismo_envoltorio_que_el_backend(self):
        """T214 · Defecto que previene: sondear una vía distinta de la que después se usa."""
        instancia = None
        if deteccion.raiz_delegada() is not None:
            instancia = backends.CgroupV2(espacio=self.espacio)
            envoltura = instancia.envolver(["sh", "-c", "true"])
            self.assertIn(deteccion.GUION_DE_MIGRACION, envoltura)
            instancia.limpiar()
        else:
            self.skipTest("este anfitrión no delega ningún subárbol de `cgroup2`")

    def test_la_deteccion_no_descarga_imagenes_de_contenedor(self):
        """T214 · Defecto que previene: que la disponibilidad dependa de la red."""
        fila = [f for f in self.capacidades["backends"]
                if f["backend"] == "contenedor"][0]
        if fila["disponible"]:
            self.assertIn(fila["evidencia"]["imagen"], deteccion.IMAGENES_ACEPTADAS)
        else:
            self.assertTrue(fila["motivo"])

    def test_el_backend_simple_siempre_esta_disponible_y_con_nivel_inferior(self):
        """T214 · Defecto que previene: quedarse sin vía cuando no hay contención fuerte."""
        fila = [f for f in self.capacidades["backends"] if f["backend"] == "simple"][0]
        self.assertTrue(fila["disponible"])
        self.assertEqual(fila["nivel"], deteccion.GRUPO_DE_PROCESOS)
        self.assertIn("setsid", fila["motivo"])


# ===========================================================================
#  T215 · CONTENCIÓN FUERTE
# ===========================================================================
class ContencionFuerte(BaseDeContencion):

    def _comprobar_generacional(self, backend, modo):
        resultado, capturadas = self._correr(
            backend, deteccion.ARBOL_DE_PROCESOS, modo=modo)
        self.assertEqual(resultado.nivel_de_aislamiento, deteccion.ARBOL_DE_PROCESOS)
        self.assertEqual(resultado.backend, backend)
        self.assertEqual(resultado.estado,
                         "cancelado" if modo == "cancelacion" else "timeout")
        for generacion in ("hijo", "nieto", "bisnieto"):
            self.assertTrue(capturadas.get(generacion),
                            "no se capturó el " + generacion + ": la tarea no engendró "
                            "lo que la prueba dice medir")
        todos = (capturadas["raiz"] + capturadas["hijo"]
                 + capturadas["nieto"] + capturadas["bisnieto"])
        vivos = contencion.esperar_a_que_mueran(todos)
        self.assertEqual(vivos, [],
                         "sobrevivió descendencia al backend `" + backend + "`: "
                         + str(vivos))
        return resultado, capturadas

    def test_el_bisnieto_con_setsid_no_escapa_al_backend_elegido(self):
        """T215 · Defecto que previene: llamar contención a un `killpg` que `setsid` esquiva."""
        if not self.capacidades["fuertes_disponibles"]:
            self.skipTest("no hay contención fuerte en este anfitrión; el fallo cerrado "
                          "lo cubre `T216`")
        elegido, _ = modulo_politica.elegir(
            contencion.Politica(deteccion.ARBOL_DE_PROCESOS), self.capacidades)
        self._comprobar_generacional(elegido, "cancelacion")

    def test_cada_backend_fuerte_disponible_contiene_las_tres_generaciones(self):
        """T215 · Defecto que previene: probar sólo el backend cómodo y declarar la clase."""
        disponibles = self.capacidades["fuertes_disponibles"]
        if not disponibles:
            self.skipTest("no hay contención fuerte en este anfitrión")
        for backend in disponibles:
            with self.subTest(backend=backend):
                self.setUp()
                self._comprobar_generacional(backend, "cancelacion")

    def test_el_timeout_tambien_limpia_la_descendencia(self):
        """T215 · Defecto que previene: un timeout que termina el informe y no la tarea."""
        if not self.capacidades["fuertes_disponibles"]:
            self.skipTest("no hay contención fuerte en este anfitrión")
        elegido, _ = modulo_politica.elegir(
            contencion.Politica(deteccion.ARBOL_DE_PROCESOS), self.capacidades)
        resultado, _ = self._comprobar_generacional(elegido, "timeout")
        self.assertEqual(resultado.estado, "timeout")

    def test_la_contencion_sobrevive_al_cambio_de_grupo_de_procesos(self):
        """T215 · Defecto que previene: contener por grupo, que es lo que `setsid` rompe."""
        if not self.capacidades["fuertes_disponibles"]:
            self.skipTest("no hay contención fuerte en este anfitrión")
        elegido, _ = modulo_politica.elegir(
            contencion.Politica(deteccion.ARBOL_DE_PROCESOS), self.capacidades)
        _, capturadas = self._comprobar_generacional(elegido, "cancelacion")
        # El control del control: si las generaciones NO hubieran cambiado de grupo, la
        # prueba no distinguiría el backend fuerte del simple. Se comprueba que la tarea
        # engendró tres generaciones distintas y separadas.
        self.assertNotEqual(capturadas["hijo"], capturadas["nieto"])
        self.assertNotEqual(capturadas["nieto"], capturadas["bisnieto"])

    def test_el_resultado_publicable_no_lleva_pid_ni_duracion(self):
        """T215 · Defecto que previene: `I-g3`, un pid o una duración en lo derivado."""
        resultado = contencion.ejecutar(
            ["sh", "-c", "echo hecho"], espacio=self.espacio, limite_segundos=20,
            politica=contencion.Politica(deteccion.GRUPO_DE_PROCESOS, backend="simple"),
            marca=self.prefijo, capacidades=self.capacidades)
        publicable = resultado.a_dict()
        self.assertEqual(resultado.estado, "completado")
        self.assertNotIn("pid", publicable)
        for clave in publicable:
            self.assertNotIn("duracion", clave)
            self.assertNotIn("ejecucion", clave)


# ===========================================================================
#  T216 · el backend SIMPLE y el FALLO CERRADO
# ===========================================================================
class BackendSimpleYFalloCerrado(BaseDeContencion):

    def test_con_el_backend_simple_el_bisnieto_SI_escapa(self):
        """T216 · Defecto que previene: presentar el nivel débil como si fuera el fuerte.

        Es la mitad negativa de `T215`. `adaptadores/proceso.py` declara este límite —«un
        descendiente que hace `setsid` ESCAPA, y esto está MEDIDO»— y aquí se vuelve a medir
        en vez de creerlo.
        """
        resultado, capturadas = self._correr(
            "simple", deteccion.GRUPO_DE_PROCESOS, modo="cancelacion")
        self.assertEqual(resultado.nivel_de_aislamiento, deteccion.GRUPO_DE_PROCESOS)
        self.assertTrue(capturadas.get("bisnieto"))
        vivos = [pid for pid in capturadas["bisnieto"] if contencion.sigue_vivo(pid)]
        self.assertEqual(vivos, capturadas["bisnieto"],
                         "el bisnieto NO sobrevivió al backend simple: o la tarea no hizo "
                         "`setsid`, o esta prueba dejó de distinguir los dos niveles")

    def test_el_backend_simple_declara_su_alcance_en_el_resultado(self):
        """T216 · Defecto que previene: degradar sin dejar rastro en la evidencia."""
        resultado, _ = self._correr("simple", deteccion.GRUPO_DE_PROCESOS,
                                    modo="cancelacion")
        self.assertIn("setsid", resultado.ficha_del_backend["detalle"]["alcance"])
        self.assertEqual(resultado.a_dict()["nivel_de_aislamiento"],
                         deteccion.GRUPO_DE_PROCESOS)

    def test_pedir_el_simple_con_politica_fuerte_falla_cerrado(self):
        """T216 · Defecto que previene: cumplir una política fuerte con un backend débil."""
        with self.assertRaises(contencion.ContencionFuerteNoDisponible):
            modulo_politica.elegir(
                contencion.Politica(deteccion.ARBOL_DE_PROCESOS, backend="simple"),
                self.capacidades)

    def test_sin_ningun_backend_fuerte_la_politica_fuerte_falla_cerrado(self):
        """T216 · Defecto que previene: degradar en silencio a `killpg`."""
        fabricadas = {
            "orden_de_preferencia": list(deteccion.ORDEN_DE_PREFERENCIA),
            "niveles": list(deteccion.NIVELES),
            "backends": [
                {"backend": fila["backend"], "nivel": fila["nivel"],
                 "disponible": fila["nivel"] == deteccion.GRUPO_DE_PROCESOS,
                 "motivo": "anfitrión sin contenedores de recursos", "evidencia": {}}
                for fila in self.capacidades["backends"]
            ],
            "fuertes_disponibles": [],
            "hay_contencion_fuerte": False,
            "mejor_disponible": "simple",
        }
        with self.assertRaises(contencion.ContencionFuerteNoDisponible) as capturado:
            modulo_politica.elegir(
                contencion.Politica(deteccion.ARBOL_DE_PROCESOS), fabricadas)
        self.assertIn("NO se degrada", str(capturado.exception))
        # Y la ejecución tampoco ocurre: no hay resultado degradado que nadie pueda leer.
        with self.assertRaises(contencion.ContencionFuerteNoDisponible):
            contencion.ejecutar(["sh", "-c", "echo no deberia correr"],
                                espacio=self.espacio, limite_segundos=5,
                                politica=contencion.Politica(deteccion.ARBOL_DE_PROCESOS),
                                capacidades=fabricadas)

    def test_la_eleccion_nunca_devuelve_el_simple_cuando_se_exige_lo_fuerte(self):
        """T216 · Defecto que previene: una degradación por el camino del `for`."""
        if not self.capacidades["fuertes_disponibles"]:
            self.skipTest("no hay contención fuerte en este anfitrión")
        elegido, _ = modulo_politica.elegir(
            contencion.Politica(deteccion.ARBOL_DE_PROCESOS), self.capacidades)
        self.assertNotEqual(elegido, "simple")
        self.assertEqual(deteccion.NIVEL_POR_BACKEND[elegido],
                         deteccion.ARBOL_DE_PROCESOS)

    def test_pedir_el_simple_explicitamente_es_legitimo_y_queda_registrado(self):
        """T216 · Defecto que previene: retirar el backend débil en vez de declararlo."""
        elegido, _ = modulo_politica.elegir(
            contencion.Politica(deteccion.GRUPO_DE_PROCESOS, backend="simple"),
            self.capacidades)
        self.assertEqual(elegido, "simple")

    def test_un_nivel_fuera_del_vocabulario_falla_cerrado(self):
        """T216 · Defecto que previene: una política con un nivel que nadie implementa."""
        with self.assertRaises(contencion.NivelDesconocido):
            contencion.Politica("aislamiento-total")

    def test_un_backend_desconocido_falla_cerrado(self):
        """T216 · Defecto que previene: pedir un mecanismo que no existe y seguir."""
        with self.assertRaises(contencion.BackendNoDisponible):
            modulo_politica.elegir(
                contencion.Politica(deteccion.ARBOL_DE_PROCESOS, backend="jaula"),
                self.capacidades)

    def test_una_orden_vacia_falla_cerrado(self):
        """T216 · Defecto que previene: lanzar una contención alrededor de nada."""
        with self.assertRaises(contencion.TareaInvalida):
            contencion.ejecutar([], espacio=self.espacio, limite_segundos=5,
                                capacidades=self.capacidades)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
