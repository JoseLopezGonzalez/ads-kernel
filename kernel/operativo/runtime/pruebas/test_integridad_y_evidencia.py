#!/usr/bin/env python3
"""test_integridad_y_evidencia — `T306` a `T309`. Los cuatro hallazgos TRANSVERSALES.

    `T306`  `E-10`  PROCEDENCIA con `--repo`: módulos del APARATO, `PYTHONPATH` envenenado
                    que no entra, dos repositorios que no se contaminan, y la procedencia
                    PUBLICADA en la salida
    `T307`  `E-14`  EVIDENCIA: `OK` deja de equivaler a `OK (skipped=N)`; el resultado se
                    comprueba ENTERO —casos, fallos, errores y saltos—; y manipular el
                    contador INVALIDA la evidencia
    `T308`  `E-15`  CLI: ningún error TIPADO sale de `main()` como traza; código de salida
                    estable por clase de fallo; `stderr` útil y sin rutas del anfitrión
    `T309`  `E-16`  CONTENCIÓN CABLEADA en el camino PRODUCTIVO, con hijo, nieto y BISNIETO
            `E-18`  y el ALCANCE EXACTO de este anfitrión, medido y publicado

POR QUÉ ESTA BATERÍA EXISTE Y NO SE REPARTE EN LAS DEMÁS. Los cuatro hallazgos cruzan los
paquetes: `E-10` y `E-15` son de los CINCO puntos ejecutables a la vez, `E-14` es del
validador de evidencia, que vive fuera del runtime, y `E-16` es del adaptador, del runtime,
del ciclo y del paquete de contención en la misma prueba. Meter cada uno en la batería de su
paquete habría partido la propiedad en trozos que por separado no demuestran nada.

**LO QUE NO SE SIMULA.** Los procesos son procesos (`subprocess`, sesión nueva y entorno
construido entero), los repositorios son repositorios Git de verdad, y la contención se mide
con los PID reales del anfitrión sobre tres generaciones que hacen `setsid`.
"""
from __future__ import annotations

import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

RAIZ_RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ_OPERATIVO = os.path.dirname(RAIZ_RUNTIME)
RAIZ_REPO = os.path.dirname(os.path.dirname(RAIZ_OPERATIVO))
VALIDADORES = os.path.join(RAIZ_OPERATIVO, "validadores")

sys.path.insert(0, RAIZ_RUNTIME)

import contencion                                                    # noqa: E402
from admision import matriz                                          # noqa: E402
from contencion import deteccion                                     # noqa: E402
from gobierno.git import CanalGit                                    # noqa: E402

EJECUTABLES = ("ads_admision.py", "ads_estado.py", "ads_runtime.py",
               "ads_ciclo.py", "ads_arboles.py")

SEGUNDOS_DE_LA_TAREA = 90


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de las demás baterías del runtime, no importado: viven todas como guiones
    sueltos y ninguna está en la ruta de importación de las otras. La salida se PUBLICA como
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
#  Cimientos: SESIÓN NUEVA de verdad y entorno CONSTRUIDO entero
# ===========================================================================
class SesionNueva(unittest.TestCase):
    """Cada invocación es un PROCESO nuevo con un entorno construido desde cero.

    Nada se hereda del intérprete que corre la batería: si se heredara, una variable de la
    máquina de quien ejecuta podría explicar un verde, y la prueba mediría el anfitrión en
    vez de el aparato.
    """

    def setUp(self):
        self.taller = tempfile.mkdtemp(prefix="ads-integridad-")
        self.addCleanup(shutil.rmtree, self.taller, ignore_errors=True)

    def entorno(self, extra=None):
        entorno = {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "LC_ALL": "C.UTF-8",
            "LANG": "C.UTF-8",
            "TZ": "UTC",
            "HOME": self.taller,
        }
        if extra:
            entorno.update(extra)
        return entorno

    def correr(self, ejecutable, argumentos, *, extra=None, cwd=None, espera=300):
        return subprocess.run(
            [sys.executable, os.path.join(RAIZ_RUNTIME, ejecutable)]
            + [str(a) for a in argumentos],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.entorno(extra), cwd=cwd or self.taller, check=False, timeout=espera,
        )

    def repo_de_pruebas(self, nombre="control"):
        """Un control repo Git REAL con la forma del corpus, y su commit base."""
        repo = os.path.join(self.taller, nombre)
        os.makedirs(repo, exist_ok=True)
        canal = CanalGit(repo)
        return repo, matriz.fundar(repo, canal), canal


# ===========================================================================
#  T306 · `E-10` · PROCEDENCIA con `--repo`
# ===========================================================================
class ProcedenciaDeLosModulos(SesionNueva):
    """`E-10`. De dónde salen los módulos con los que se juzga, y cómo se demuestra.

    HECHO REPRODUCIDO ANTES DE CORREGIR, sobre `ads_admision.py`: con
    `PYTHONPATH=<dir>` apuntando a un directorio con un `json.py` HOMÓNIMO, el proceso
    IMPORTABA el homónimo —`sys.path[0]` protege a los paquetes que viven junto al script,
    NO a la biblioteca estándar, que va después de `PYTHONPATH`— y
    `verificar --json` publicaba `{}` como veredicto con código 0. Los cinco puntos
    ejecutables importaban el módulo envenenado.
    """

    def paquete_envenenado(self):
        """Un directorio con homónimos que, si se importaran, SE NOTARÍA.

        Cada homónimo deja un FICHERO TESTIGO al importarse. Mirar sólo `stderr` no bastaría:
        una salida se puede tragar, y un fichero en disco, no.
        """
        veneno = os.path.join(self.taller, "veneno")
        os.makedirs(veneno, exist_ok=True)
        self.testigo = os.path.join(self.taller, "IMPORTADO-EL-HOMONIMO")
        cuerpo = (
            "import sys\n"
            "with open(" + repr(self.testigo) + ", 'a') as _m:\n"
            "    _m.write(__name__ + '\\n')\n"
            "sys.stderr.write('HOMONIMO MALICIOSO IMPORTADO: ' + __name__ + '\\n')\n"
        )
        # `json` es el que se coló de verdad: lo usan los cinco puntos ejecutables para
        # publicar su salida, y un `json.dumps` sustituido publica lo que quiera.
        with open(os.path.join(veneno, "json.py"), "w", encoding="utf-8") as manejador:
            manejador.write(cuerpo + "\ndef dumps(*a, **k):\n    return '{}'\n"
                            "def loads(*a, **k):\n    return {}\n")
        for paquete in ("admision", "estado", "runtime", "ciclo", "arboles",
                        "gobierno", "identidad", "contencion", "adaptadores",
                        "macrocircuitos"):
            carpeta = os.path.join(veneno, paquete)
            os.makedirs(carpeta, exist_ok=True)
            with open(os.path.join(carpeta, "__init__.py"), "w",
                      encoding="utf-8") as manejador:
                manejador.write(cuerpo)
        return veneno

    def test_T306_ningun_ejecutable_importa_un_homonimo_del_PYTHONPATH(self):
        """T306 · Defecto que previene: `E-10`, que el lanzador decida qué código juzga.

        SABOTAJE QUE LA PONE ROJA: retirar la purga de `sys.path` del preludio de los
        `ads_*.py` —o dejarla DESPUÉS de los `import`—.
        """
        veneno = self.paquete_envenenado()
        repo, base, _canal = self.repo_de_pruebas()
        for ejecutable in EJECUTABLES:
            with self.subTest(ejecutable=ejecutable):
                resultado = self.correr(ejecutable, ["--help"],
                                        extra={"PYTHONPATH": veneno})
                self.assertNotIn(b"HOMONIMO MALICIOSO", resultado.stderr,
                                 ejecutable + " importó un homónimo del PYTHONPATH")
        self.assertFalse(os.path.exists(self.testigo),
                         "algún punto ejecutable importó un homónimo: "
                         + (open(self.testigo).read() if os.path.exists(self.testigo)
                            else ""))
        # CONTROL DEL CONTROL: el veneno SÍ se importa cuando nadie lo impide. Sin esto,
        # «no se importó» se explicaría por un paquete que no funciona.
        control = subprocess.run(
            [sys.executable, "-c", "import json"], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, env=self.entorno({"PYTHONPATH": veneno}),
            cwd=self.taller, check=False, timeout=60)
        self.assertIn(b"HOMONIMO MALICIOSO", control.stderr,
                      "el paquete envenenado no se importa ni cuando se le deja: esta "
                      "prueba no estaría midiendo nada")

    def test_T306b_el_veredicto_no_se_falsea_desde_el_PYTHONPATH(self):
        """T306 · Defecto que previene: publicar `{}` como veredicto y salir con código 0."""
        veneno = self.paquete_envenenado()
        repo, base, _canal = self.repo_de_pruebas()
        resultado = self.correr(
            "ads_admision.py",
            ["--repo", repo, "verificar", "--base", base, "--json"],
            extra={"PYTHONPATH": veneno})
        salida = resultado.stdout.decode("utf-8", "replace")
        self.assertTrue(salida.strip(), "el veredicto salió vacío")
        datos = json.loads(salida)
        self.assertIn("color", datos, "el veredicto publicado no tiene forma de veredicto")
        self.assertIn("procedencia", datos)
        self.assertFalse(os.path.exists(self.testigo))

    def test_T306c_la_procedencia_se_PUBLICA_y_nombra_cada_modulo(self):
        """T306 · Defecto que previene: una procedencia que hay que creerse."""
        repo, base, _canal = self.repo_de_pruebas()
        resultado = self.correr("ads_admision.py",
                                ["--repo", repo, "procedencia", "--json"])
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        datos = json.loads(resultado.stdout.decode("utf-8"))
        self.assertTrue(datos["modulos"], "no publica ningún módulo")
        for nombre, origen in sorted(datos["modulos"].items()):
            with self.subTest(modulo=nombre):
                self.assertTrue(origen.startswith("aparato:"),
                                nombre + " no viene del aparato: " + origen)
        # Y ninguna ruta ABSOLUTA del anfitrión viaja en la salida publicable.
        self.assertNotIn(os.path.realpath(RAIZ_REPO),
                         json.dumps(datos, ensure_ascii=False))

    def test_T306d_dos_repositorios_distintos_no_se_contaminan(self):
        """T306 · Defecto que previene: que el árbol juzgado aporte el código que lo juzga.

        Se construye un SEGUNDO repositorio que trae dentro su propio
        `kernel/operativo/runtime/admision/__init__.py`, envenenado. Se juzga ESE repo con el
        ejecutable del PRIMERO: el veredicto tiene que salir de los módulos del aparato, y la
        procedencia tiene que decirlo.
        """
        repo, base, canal = self.repo_de_pruebas("ajeno")
        intruso = os.path.join(repo, "kernel", "operativo", "runtime", "admision")
        os.makedirs(intruso, exist_ok=True)
        testigo = os.path.join(self.taller, "INTRUSO-DEL-REPO-AJENO")
        with open(os.path.join(intruso, "__init__.py"), "w", encoding="utf-8") as manejador:
            manejador.write("open(" + repr(testigo) + ", 'a').close()\n"
                            "def verificar(*a, **k):\n"
                            "    raise SystemExit(0)\n")
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "repo ajeno con su propio aparato")
        resultado = self.correr("ads_admision.py",
                                ["--repo", repo, "procedencia", "--json"])
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        datos = json.loads(resultado.stdout.decode("utf-8"))
        self.assertFalse(datos["repo_es_el_arbol_del_aparato"],
                         "el repo ajeno se confundió con el árbol del aparato")
        for nombre, origen in sorted(datos["modulos"].items()):
            with self.subTest(modulo=nombre):
                self.assertTrue(origen.startswith("aparato:"))
        self.assertFalse(os.path.exists(testigo),
                         "el aparato importó código del repositorio que estaba juzgando")

    def test_T306e_el_cwd_del_lanzador_no_sustituye_al_aparato(self):
        """T306 · Defecto que previene: colar un homónimo por el directorio de trabajo."""
        veneno = self.paquete_envenenado()
        repo, base, _canal = self.repo_de_pruebas()
        # Se ejecuta DESDE DENTRO del directorio envenenado y con él en `PYTHONPATH`: las
        # dos vías que `E-10` nombra, a la vez.
        resultado = self.correr("ads_admision.py",
                                ["--repo", repo, "procedencia", "--json"],
                                extra={"PYTHONPATH": veneno + os.pathsep + "."},
                                cwd=veneno)
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        datos = json.loads(resultado.stdout.decode("utf-8"))
        for origen in datos["modulos"].values():
            self.assertTrue(origen.startswith("aparato:"))
        self.assertFalse(os.path.exists(self.testigo))
        self.assertGreaterEqual(datos["entradas_del_lanzador_retiradas"], 1,
                                "no se retiró ninguna entrada del lanzador y había dos")


# ===========================================================================
#  T307 · `E-14` · `OK` NO EQUIVALE A `OK (skipped=N)`
# ===========================================================================
class ResultadoExactoDeLaEvidencia(unittest.TestCase):
    """`E-14`. La evidencia se comprueba por su RESULTADO ENTERO, no por una subcadena.

    HECHO REPRODUCIDO ANTES DE CORREGIR: dieciséis componentes de `validadores.yaml`
    declaran `firma_de_exito: 'OK'`, y la comprobación es `re.search`, de modo que
    `re.search('OK', 'OK (skipped=17)')` casa. Medido en el mismo repositorio: hay 17
    llamadas a `skipTest` repartidas por seis baterías del runtime, ninguna contada y
    ninguna publicada.
    """

    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, VALIDADORES)
        import comprobar_evidencia                                    # noqa: PLC0415
        import comprobar_contratos                                    # noqa: PLC0415
        cls.validador = comprobar_evidencia
        cls.Resultado = comprobar_contratos.Resultado

    def salida(self, casos=3, resultado="OK", ran=None, desenlace="ok"):
        """Una salida de `unittest` sintética, con la MISMA forma que la real."""
        lineas = []
        for indice in range(casos):
            lineas.append("test_" + str(indice) + " (__main__.X.test_" + str(indice) + ")")
            lineas.append("docstring de la prueba ... " + desenlace)
        lineas.append("")
        lineas.append("-" * 70)
        lineas.append("Ran " + str(casos if ran is None else ran)
                      + " tests  (duración no registrada: varía por ejecución)")
        lineas.append("")
        lineas.append(resultado)
        return "\n".join(lineas) + "\n"

    def juzgar(self, texto, comp=None):
        r = self.Resultado("T158", "prueba")
        self.validador._comprobar_resultado_exacto("evidencia.txt", comp or {"id": "x"},
                                                   texto, r)
        return r

    def test_T307_control_positivo_una_corrida_limpia_pasa(self):
        """T307 · Control del CONTROL: sin él, «todo falla» explicaría el verde."""
        r = self.juzgar(self.salida(casos=5))
        self.assertEqual(r.fallos, [], r.fallos)

    def test_T307b_OK_con_saltos_NO_declarados_es_ROJO(self):
        """T307 · Defecto que previene: `E-14`, que `OK` valga por `OK (skipped=N)`.

        SABOTAJE QUE LA PONE ROJA: volver a comprobar la firma con `re.search('OK', texto)`
        y nada más.
        """
        texto = self.salida(casos=3, resultado="OK (skipped=3)", desenlace="skipped 'x'")
        r = self.juzgar(texto)
        self.assertTrue(r.fallos, "una corrida con 3 saltos no declarados pasó como OK")
        self.assertIn("skipped", " ".join(r.fallos))
        # Y el control del control de la reproducción: la firma vieja SÍ casaba.
        self.assertTrue(re.search("OK", texto),
                        "la firma `OK` ya no casa con `OK (skipped=3)`, luego esta prueba "
                        "no estaría reproduciendo el defecto que cierra")

    def test_T307c_los_saltos_DECLARADOS_con_su_motivo_se_admiten_y_se_cuentan(self):
        """T307 · Defecto que previene: permitir saltos sin decir CUÁLES ni POR QUÉ."""
        texto = self.salida(casos=2, resultado="OK (skipped=2)",
                            desenlace="skipped 'sin cgroup ejercitable'")
        comp = {"id": "x", "skips_permitidos": [
            {"id": "sin cgroup ejercitable", "motivo": "E-18: el anfitrión no lo ejerce"},
            {"id": "sin cgroup ejercitable", "motivo": "E-18: el anfitrión no lo ejerce"},
        ]}
        self.assertEqual(self.juzgar(texto, comp).fallos, [])
        # Un salto de MÁS no está declarado...
        de_mas = self.salida(casos=3, resultado="OK (skipped=3)",
                             desenlace="skipped 'sin cgroup ejercitable'")
        self.assertTrue(self.juzgar(de_mas, comp).fallos)
        # ...y una declaración que ya no ocurre también es ROJO: el contrato ha caducado.
        self.assertTrue(self.juzgar(self.salida(casos=2), comp).fallos)
        # Y una declaración sin `motivo` es un defecto del manifiesto, no un permiso.
        sin_motivo = {"id": "x", "skips_permitidos": [{"id": "sin cgroup ejercitable"}]}
        self.assertTrue(self.juzgar(texto, sin_motivo).fallos)

    def test_T307d_manipular_el_CONTADOR_invalida_la_evidencia(self):
        """T307 · Defecto que previene: publicar una cifra que no describe la corrida.

        La cifra `Ran N tests` la declara la propia evidencia. El recuento se DERIVA de los
        desenlaces que la salida verbosa imprime, y los dos tienen que casar.
        """
        r = self.juzgar(self.salida(casos=3, ran=38))
        self.assertTrue(r.fallos, "una evidencia con el contador inflado pasó")
        self.assertIn("desenlaces", " ".join(r.fallos))
        # Y hacia abajo tampoco: recortar la salida y bajar el contador no vale.
        self.assertTrue(self.juzgar(self.salida(casos=5, ran=2)).fallos)

    def test_T307e_fallos_errores_y_dos_corridas_pegadas_son_ROJO(self):
        """T307 · Defecto que previene: publicar la corrida buena y esconder la mala."""
        self.assertTrue(self.juzgar(
            self.salida(casos=2, resultado="FAILED (failures=1)")).fallos)
        self.assertTrue(self.juzgar(
            self.salida(casos=2, resultado="OK (failures=1)")).fallos)
        self.assertTrue(self.juzgar(
            self.salida(casos=2, resultado="OK (expected failures=1)")).fallos)
        pegadas = self.salida(casos=2, resultado="FAILED (errors=1)") + self.salida(casos=2)
        r = self.juzgar(pegadas)
        self.assertTrue(r.fallos)
        self.assertIn("EXACTAMENTE", " ".join(r.fallos))

    def test_T307f_la_evidencia_PUBLICADA_del_repositorio_supera_la_comprobacion(self):
        """T307 · Control POSITIVO sobre el corpus real: la regla nueva no es inaplicable.

        Se juzga la evidencia que el repositorio publica HOY. Si la comprobación fuese
        imposible de superar, sería indistinguible de una que no comprueba nada.
        """
        directorio = os.path.join(RAIZ_OPERATIVO, "pruebas", "evidencia")
        vistos = 0
        for nombre in sorted(os.listdir(directorio)):
            if not nombre.endswith(".txt"):
                continue
            with open(os.path.join(directorio, nombre), encoding="utf-8") as manejador:
                texto = manejador.read()
            if self.validador._resultado_de_unittest(texto) is None:
                continue
            vistos += 1
            with self.subTest(evidencia=nombre):
                self.assertEqual(self.juzgar(texto, {"id": nombre}).fallos, [])
        self.assertGreater(vistos, 5,
                           "no se encontró evidencia de `unittest` que juzgar: el control "
                           "positivo no habría podido fallar")


# ===========================================================================
#  T308 · `E-15` · NINGÚN ERROR TIPADO SALE COMO TRAZA
# ===========================================================================
class ErroresTipadosDeLaCLI(SesionNueva):
    """`E-15`. Los cinco puntos ejecutables, y las jerarquías tipadas que los alcanzan.

    HECHO REPRODUCIDO ANTES DE CORREGIR: `adaptadores.contrato.CapacidadNoSoportada`
    escapaba de `ads_runtime.main()` como TRACEBACK con rutas absolutas del anfitrión,
    `stdout` vacío y código 1 —el mismo que un fallo tipado, luego indistinguible—. Matiz
    medido y conservado: la clase HOMÓNIMA del runtime (`runtime/errores.py`) SÍ se
    capturaba y salía como `[CAPACIDAD_NO_SOPORTADA] ...` limpio. Son dos jerarquías
    distintas a propósito, y el punto ejecutable tenía que conocer las dos.
    """

    def exigir_salida_limpia(self, resultado, *, codigo, donde):
        texto = (resultado.stdout + resultado.stderr).decode("utf-8", "replace")
        self.assertEqual(resultado.returncode, codigo,
                         donde + ": código " + str(resultado.returncode)
                         + " y se esperaba " + str(codigo) + " · " + texto[:400])
        self.assertNotIn("Traceback (most recent call last)", texto,
                         donde + ": salió una traza")
        for absoluta in (os.path.realpath(RAIZ_REPO), os.path.abspath(RAIZ_REPO)):
            self.assertNotIn(absoluta, texto,
                             donde + ": publicó una ruta absoluta del anfitrión")
        self.assertTrue(re.search(r"\[[A-Z][A-Z0-9_]{4,}\]", texto),
                        donde + ": no publicó ningún código tipado")
        return texto

    def paquete_de_prueba(self, capacidades):
        """Un control repo con un item y un paquete despachable. Nada simulado."""
        import runtime as runtime_ads                                 # noqa: PLC0415
        control = os.path.join(self.taller, "control")
        espacio = os.path.join(self.taller, "espacio")
        os.makedirs(control, exist_ok=True)
        os.makedirs(espacio, exist_ok=True)
        rt = runtime_ads.Runtime(control, instancia="mc-e15").abrir()
        try:
            rt.crear_item(id="it-1", titulo="item", motivo="E-15")
            rt.crear_paquete(id="pq-1", item="it-1",
                             capacidades_requeridas=list(capacidades),
                             orden={"adaptador": "proceso-local", "operacion": "ejecutar",
                                    "argumentos": ["/bin/true"], "limite_segundos": 30})
        finally:
            rt.cerrar()
        return control, espacio

    def test_T308_la_tabla_de_codigos_es_la_MISMA_en_los_cinco(self):
        """T308 · Defecto que previene: cinco CLI con cinco convenios de salida distintos."""
        tablas = {}
        for ejecutable in EJECUTABLES:
            guion = (
                "import runpy, json\n"
                "modulo = runpy.run_path("
                + repr(os.path.join(RAIZ_RUNTIME, ejecutable))
                + ", run_name='no-main')\n"
                "print(json.dumps(modulo['CODIGOS_DE_SALIDA'], sort_keys=True))\n"
            )
            proceso = subprocess.run([sys.executable, "-c", guion],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     env=self.entorno(), cwd=self.taller, check=False,
                                     timeout=120)
            self.assertEqual(proceso.returncode, 0,
                             ejecutable + ": " + proceso.stderr.decode()[:300])
            tablas[ejecutable] = json.loads(proceso.stdout.decode())
        referencia = tablas[EJECUTABLES[0]]
        self.assertEqual(referencia["exito"], 0)
        self.assertEqual(referencia["error-del-kernel"], 1)
        self.assertEqual(referencia["uso-incorrecto"], 2)
        for ejecutable, tabla in tablas.items():
            with self.subTest(ejecutable=ejecutable):
                self.assertEqual(tabla, referencia)
        # Y los códigos son DISTINTOS entre sí: una tabla con dos claves al mismo número
        # no distingue nada.
        self.assertEqual(len(set(referencia.values())), len(referencia))

    def test_T308b_el_error_del_ADAPTADOR_no_sale_como_traza(self):
        """T308 · Defecto que previene: `E-15`, la clase homónima que nadie capturaba."""
        control, espacio = self.paquete_de_prueba(["capacidad-que-nadie-ofrece"])
        resultado = self.correr("ads_runtime.py",
                                ["--repo", control, "--instancia", "mc-externa",
                                 "--adaptador-local", espacio, "despachar", "pq-1"])
        texto = self.exigir_salida_limpia(resultado, codigo=3,
                                          donde="ads_runtime/adaptador")
        self.assertIn("CAPACIDAD_NO_SOPORTADA", texto)
        self.assertIn("error-del-adaptador", texto)

    def test_T308c_la_clase_HOMONIMA_del_runtime_sigue_saliendo_por_su_codigo(self):
        """T308 · El matiz, conservado: son DOS jerarquías y se distinguen en la salida."""
        control, espacio = self.paquete_de_prueba(["capacidad-que-nadie-ofrece"])
        resultado = self.correr("ads_runtime.py",
                                ["--repo", control, "--instancia", "mc-externa",
                                 "--registro-en-pruebas", espacio, "despachar", "pq-1"])
        texto = self.exigir_salida_limpia(resultado, codigo=1,
                                          donde="ads_runtime/runtime")
        self.assertIn("CAPACIDAD_NO_SOPORTADA", texto)

    def test_T308d_el_error_de_CONTENCION_tiene_su_propio_codigo(self):
        """T308 · Defecto que previene: confundir «no puedo contener» con «falló la tarea»."""
        control, espacio = self.paquete_de_prueba(["proceso-local"])
        resultado = self.correr(
            "ads_runtime.py",
            ["--repo", control, "--instancia", "mc-externa",
             "--adaptador-local", espacio,
             "--contencion", "arbol-de-procesos", "--contencion-backend", "simple",
             "despachar", "pq-1"])
        texto = self.exigir_salida_limpia(resultado, codigo=4,
                                          donde="ads_runtime/contencion")
        self.assertIn("CONTENCION_FUERTE_NO_DISPONIBLE", texto)
        self.assertIn("error-de-contencion", texto)

    def test_T308e_los_CINCO_ejecutables_fallan_tipados_y_sin_traza(self):
        """T308 · Defecto que previene: cerrar el agujero en uno y dejarlo en los otros.

        Cada punto ejecutable se lleva a un fallo TIPADO de su propia jerarquía, con una
        entrada que sólo él puede rechazar. Lo que se exige es lo mismo en los cinco: código
        estable, código tipado en la salida, cero trazas y cero rutas del anfitrión.
        """
        control, _base, _canal = self.repo_de_pruebas("sin-almacen")
        casos = [
            ("ads_estado.py", ["--repo", control, "revision"], 1),
            ("ads_admision.py",
             ["--repo", control, "verificar", "--base", "no-existe-esta-revision"], 1),
            ("ads_arboles.py", ["--repo", control, "conjunto"], 1),
            ("ads_runtime.py",
             ["--repo", control, "--instancia", "mc", "estado-paquete", "pq-inexistente"],
             1),
            ("ads_ciclo.py",
             ["encuadrar", "--repo", control, "--instancia", "mc",
              "--fuente", os.path.join(self.taller, "no-existe.md")], None),
        ]
        for ejecutable, argumentos, codigo in casos:
            with self.subTest(ejecutable=ejecutable):
                resultado = self.correr(ejecutable, argumentos)
                texto = (resultado.stdout + resultado.stderr).decode("utf-8", "replace")
                self.assertNotEqual(resultado.returncode, 0,
                                    ejecutable + " devolvió 0 sobre una entrada inválida")
                self.assertNotIn("Traceback (most recent call last)", texto,
                                 ejecutable + " salió con una traza")
                self.assertNotIn(os.path.realpath(RAIZ_REPO), texto,
                                 ejecutable + " publicó una ruta absoluta del anfitrión")
                if codigo is not None:
                    self.assertEqual(resultado.returncode, codigo, texto[:300])

    def test_T308f_no_hay_EXITO_PARCIAL_cuando_el_fallo_es_tipado(self):
        """T308 · Defecto que previene: publicar medio veredicto y además fallar."""
        control, espacio = self.paquete_de_prueba(["capacidad-que-nadie-ofrece"])
        resultado = self.correr("ads_runtime.py",
                                ["--repo", control, "--instancia", "mc-externa",
                                 "--adaptador-local", espacio, "despachar", "pq-1"])
        self.assertEqual(resultado.returncode, 3)
        self.assertEqual(resultado.stdout.decode("utf-8", "replace").strip(), "",
                         "se publicó salida de éxito junto con el fallo")
        # Y la salida estructurada existe y es interpretable, que es lo que `E-15` exige.
        estructuras = [linea for linea
                       in resultado.stderr.decode("utf-8", "replace").split("\n{")
                       if '"clase_de_fallo"' in linea]
        self.assertTrue(estructuras, "el fallo no publicó salida estructurada")
        datos = json.loads("{" + estructuras[-1])
        self.assertEqual(datos["codigo_de_salida"], 3)
        self.assertEqual(datos["error"]["codigo"], "CAPACIDAD_NO_SOPORTADA")


# ===========================================================================
#  T309 · `E-16` la CONTENCIÓN CABLEADA · `E-18` el ALCANCE de este anfitrión
# ===========================================================================
def _capa(marca, interior, segundos):
    """Una generación: se sale de su grupo con `setsid` y engendra la siguiente."""
    cuerpo = ": " + marca + "\n" + interior + "sleep " + str(segundos) + "\n"
    return "setsid sh -c " + shlex.quote(cuerpo) + " &\n"


def guion_generacional(prefijo, segundos=SEGUNDOS_DE_LA_TAREA):
    """El guion `sh` que engendra hijo, nieto y BISNIETO, los tres con `setsid`.

    Se escribe aquí y no se importa de `test_contencion.py`: las baterías del runtime son
    guiones sueltos y ninguna está en la ruta de importación de las otras. Lo que se conserva
    es la FORMA de la tarea, que es lo que hace comparables las dos medidas.
    """
    bisnieto = _capa(prefijo + "-BISNIETO", "", segundos)
    nieto = _capa(prefijo + "-NIETO", bisnieto, segundos)
    hijo = _capa(prefijo + "-HIJO", nieto, segundos)
    return (": " + prefijo + "-RAIZ\n" + hijo + "sleep 1.2\n" + "echo listo\n"
            + "sleep " + str(segundos) + "\n")


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


class ContencionEnElCaminoProductivo(SesionNueva):
    """`E-16`. La política de contención, alcanzable desde el PUNTO EJECUTABLE.

    HECHO REPRODUCIDO ANTES DE CORREGIR: la cadena `contencion` no aparecía en NINGUNO de
    los cinco `ads_*.py`, ni en `ciclo/`, ni en `runtime/`; sólo dentro de
    `adaptadores/proceso.py`. La política estaba construida y probada y NINGÚN punto
    ejecutable podía activarla: el camino productivo lanzaba siempre el adaptador sin
    política, es decir con `killpg`, cuyo límite medido es que el bisnieto ESCAPA.

    `test_contencion.py` conserva el control que impide presentar el débil como fuerte —el
    backend fuerte deja 0 supervivientes sobre tres generaciones y el simple deja escapar el
    bisnieto—. Lo que falta y se añade aquí es el camino PRODUCTIVO.
    """

    def setUp(self):
        super().setUp()
        self.prefijo = "ADSE16" + os.urandom(6).hex().upper()
        self.capacidades = contencion.capacidades()
        self.addCleanup(self._rematar)

    def _rematar(self):
        """Ningún superviviente de esta prueba sobrevive a la batería. Ni uno."""
        import signal                                                 # noqa: PLC0415
        for generacion in generaciones(self.prefijo).values():
            for pid in generacion:
                try:
                    os.kill(pid, signal.SIGKILL)
                except OSError:
                    continue

    def preparar(self, *, capacidades=("proceso-local",), segundos=6):
        """Un control repo con un paquete cuya tarea engendra TRES generaciones."""
        import runtime as runtime_ads                                 # noqa: PLC0415
        control = os.path.join(self.taller, "control")
        espacio = os.path.join(self.taller, "espacio")
        os.makedirs(control, exist_ok=True)
        os.makedirs(espacio, exist_ok=True)
        rt = runtime_ads.Runtime(control, instancia="mc-e16").abrir()
        try:
            rt.crear_item(id="it-c", titulo="tarea generacional", motivo="E-16")
            rt.crear_paquete(
                id="pq-c", item="it-c", capacidades_requeridas=list(capacidades),
                orden={"adaptador": "proceso-local", "operacion": "ejecutar",
                       "argumentos": ["sh", "-c", guion_generacional(self.prefijo)],
                       "limite_segundos": segundos})
        finally:
            rt.cerrar()
        return control, espacio

    def despachar_y_capturar(self, argumentos, *, espera=240):
        """Lanza el despacho y MUESTREA los PID mientras la tarea todavía vive.

        Muestrear al final no sirve: si la contención funciona, al terminar no queda nada
        que contar y «no se capturó el bisnieto» sería indistinguible de «el bisnieto nunca
        existió». Se muestrea durante la ventana en que la tarea está viva, que es donde la
        pregunta tiene respuesta.
        """
        import time                                                   # noqa: PLC0415
        proceso = subprocess.Popen(
            [sys.executable, os.path.join(RAIZ_RUNTIME, "ads_runtime.py")]
            + [str(a) for a in argumentos],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.entorno(), cwd=self.taller)
        capturadas = {"raiz": [], "hijo": [], "nieto": [], "bisnieto": []}
        limite = time.monotonic() + espera
        while time.monotonic() < limite:
            visto = generaciones(self.prefijo)
            for generacion, pids in visto.items():
                for pid in pids:
                    if pid not in capturadas[generacion]:
                        capturadas[generacion].append(pid)
            if all(capturadas[g] for g in ("raiz", "hijo", "nieto", "bisnieto")):
                break
            if proceso.poll() is not None and any(capturadas.values()):
                break
            time.sleep(0.2)
        salida, error = proceso.communicate(timeout=espera)
        texto = (salida + error).decode("utf-8", "replace")
        return proceso, capturadas, texto

    def test_T309_el_punto_ejecutable_ACTIVA_la_politica_y_contiene_al_bisnieto(self):
        """T309 · Defecto que previene: `E-16`, una política que nadie puede activar.

        SABOTAJE QUE LA PONE ROJA: retirar `politica_de_contencion=` de `_registro()` en
        `ads_runtime.py`, que es exactamente el estado reproducido antes de corregir.
        """
        if not self.capacidades["fuertes_disponibles"]:
            self.skipTest("este anfitrión no ofrece contención fuerte; el fallo cerrado lo "
                          "cubre la prueba siguiente y el alcance queda en `T309d`")
        control, espacio = self.preparar()
        proceso, capturadas, texto = self.despachar_y_capturar(
            ["--repo", control, "--instancia", "mc-ext", "--adaptador-local", espacio,
             "--contencion", "arbol-de-procesos", "despachar", "pq-c", "--json"])
        for generacion in ("hijo", "nieto", "bisnieto"):
            self.assertTrue(capturadas.get(generacion),
                            "no se capturó el " + generacion + ": la tarea no engendró lo "
                            "que esta prueba dice medir · " + texto[:400])
        # Las tres generaciones cambiaron de grupo: sin eso, medir `killpg` y medir el
        # árbol de procesos darían lo mismo y la prueba no distinguiría los dos niveles.
        self.assertNotEqual(capturadas["hijo"], capturadas["nieto"])
        self.assertNotEqual(capturadas["nieto"], capturadas["bisnieto"])
        todos = (capturadas["raiz"] + capturadas["hijo"] + capturadas["nieto"]
                 + capturadas["bisnieto"])
        vivos = contencion.esperar_a_que_mueran(todos)
        self.assertEqual(vivos, [],
                         "sobrevivió descendencia al camino PRODUCTIVO con política de "
                         "contención: " + str(vivos))

    def test_T309b_sin_backend_fuerte_el_punto_ejecutable_FALLA_CERRADO(self):
        """T309 · Defecto que previene: «caigo al débil y sigo», que es la peor salida.

        Se pide el nivel fuerte con un backend cuyo nivel es INFERIOR. No hay ejecución de
        ninguna clase: se comprueba que la tarea no llegó a engendrar ni una generación.
        """
        control, espacio = self.preparar()
        resultado = self.correr(
            "ads_runtime.py",
            ["--repo", control, "--instancia", "mc-ext", "--adaptador-local", espacio,
             "--contencion", "arbol-de-procesos", "--contencion-backend", "simple",
             "despachar", "pq-c"], espera=240)
        texto = (resultado.stdout + resultado.stderr).decode("utf-8", "replace")
        self.assertEqual(resultado.returncode, 4, texto[:400])
        self.assertIn("CONTENCION_FUERTE_NO_DISPONIBLE", texto)
        self.assertNotIn("Traceback (most recent call last)", texto)
        capturadas = generaciones(self.prefijo)
        self.assertEqual(sum(len(v) for v in capturadas.values()), 0,
                         "se ejecutó algo pese al fallo cerrado: " + str(capturadas))

    def test_T309c_ads_ciclo_tambien_puede_activarla(self):
        """T309 · Defecto que previene: cablearla en un punto ejecutable y no en el otro."""
        ayuda = self.correr("ads_ciclo.py", ["ciclo", "--help"])
        self.assertEqual(ayuda.returncode, 0, ayuda.stderr.decode()[:300])
        texto = ayuda.stdout.decode("utf-8", "replace")
        self.assertIn("--contencion", texto)
        self.assertIn("--contencion-backend", texto)
        # Y no es sólo una opción declarada: el fallo cerrado llega hasta el final.
        control, espacio = self.preparar()
        resultado = self.correr(
            "ads_ciclo.py",
            ["ciclo", "--repo", control, "--instancia", "mc-ext",
             "--adaptador-local", espacio, "--contencion", "arbol-de-procesos",
             "--contencion-backend", "simple"], espera=240)
        salida = (resultado.stdout + resultado.stderr).decode("utf-8", "replace")
        self.assertNotEqual(resultado.returncode, 0, salida[:300])
        self.assertIn("CONTENCION_FUERTE_NO_DISPONIBLE", salida)
        self.assertNotIn("Traceback (most recent call last)", salida)

    def test_T309d_el_ALCANCE_de_este_anfitrion_se_MIDE_y_se_declara(self):
        """T309 · `E-18` · Defecto que previene: afirmar una contención que no se ejerció.

        `E-18` permanece como LIMITACIÓN DE ANFITRIÓN, y su alcance no se adivina: se mide.
        Lo que esta prueba exige es que cada backend diga si está DISPONIBLE y, cuando no lo
        está, POR QUÉ; que un backend no ejercitable NO se cuente como ejercido; y que su
        ausencia no produzca un falso rojo.
        """
        informe = self.capacidades
        por_identificador = {fila["backend"]: fila for fila in informe["backends"]}
        self.assertIn("cgroup-v2", por_identificador,
                      "`cgroup v2` tiene que estar SONDEADO aunque no se pueda ejercer")
        for fila in informe["backends"]:
            with self.subTest(backend=fila["backend"]):
                self.assertTrue(fila["motivo"],
                                "un backend sin motivo no distingue «no está» de «no se "
                                "pudo comprobar»")
                self.assertIn(fila["nivel"], deteccion.NIVELES)
        # Un backend NO disponible no aparece entre los fuertes disponibles: no se cuenta
        # como ejercido. Es la mitad que impide presentar lo no ejercido como certificado.
        for identificador in informe["fuertes_disponibles"]:
            self.assertTrue(por_identificador[identificador]["disponible"])
        for fila in informe["backends"]:
            if not fila["disponible"]:
                self.assertNotIn(fila["backend"], informe["fuertes_disponibles"])
        # Y la ausencia de un backend NO es un rojo: mientras haya alguno fuerte, la
        # política se sirve. Lo que sería rojo es afirmar el que no se ejerció.
        if informe["hay_contencion_fuerte"]:
            elegido, _evidencia = contencion.elegir(
                contencion.Politica(deteccion.ARBOL_DE_PROCESOS), informe)
            self.assertIn(elegido, informe["fuertes_disponibles"])
            self.assertTrue(por_identificador[elegido]["disponible"])

    def test_T309e_ninguna_salida_de_esta_zona_afirma_custodia_productiva(self):
        """T309 · `E-17` · Defecto que previene: llamar custodia a una clave efímera.

        `E-17` permanece EXTERNA. Lo que esta prueba impide es que una salida de esta zona
        afirme lo contrario: se barren el README y el contrato de la raíz externa buscando
        una afirmación de custodia productiva, y se exige que lo que digan sea que NO la hay.
        """
        readme = os.path.join(RAIZ_OPERATIVO, "raiz-externa", "README.md")
        with open(readme, encoding="utf-8") as manejador:
            texto = manejador.read()
        # El REGISTRO que `E-17` exige: propietario, mecanismo previsto y condición de
        # cierre. Se comprueba que están, porque una deuda sin dueño ni cierre no es una
        # deuda: es una frase.
        for exigido in ("CUSTODIA PRODUCTIVA DE CLAVES", "PROPIETARIO",
                        "MECANISMO PREVISTO", "CONDICIÓN DE CIERRE",
                        "no constituyen custodia productiva"):
            with self.subTest(exigido=exigido):
                self.assertIn(exigido, texto,
                              "el README de la raíz externa no registra `E-17`: " + exigido)
        # Y NINGUNA sede de esta zona afirma que la custodia productiva esté resuelta.
        for sede in (readme, os.path.join(RAIZ_RUNTIME, "CONTRATO-RAIZ-EXTERNA.md")):
            with self.subTest(sede=os.path.basename(sede)):
                with open(sede, encoding="utf-8") as manejador:
                    contenido = manejador.read()
                for prohibida in ("custodia productiva RESUELTA",
                                  "custodia productiva implementada",
                                  "custodia productiva certificada"):
                    self.assertNotIn(prohibida, contenido)



# ===========================================================================
#  `T310` · `T311` — LA VENTANA DE PUBLICACIÓN, VISTA POR UN LECTOR CONCURRENTE
#
#  Aparecida AL INTEGRAR los tres ejes, y por eso vive aquí y no en el lote de nadie.
#  `test_continua.py::test_21` —que mata con `SIGKILL` a un escritor real mientras otra
#  instancia lee el mismo paquete en bucle y sin bloqueo— empezó a reventar con
#  `ESTADO_CORRUPTO` diciendo «el fichero fue modificado fuera del diario, o está truncado».
#  Ninguna de las dos cosas era cierta: el lector estaba viendo el objeto NUEVO con la
#  revisión VIEJA, que es la ventana entre el paso 8 y el paso 9.
#
#  La carrera era LATENTE desde el primer corte —el paso 8 ya reemplazaba antes de que el 9
#  publicara— y la corrección de `E-08` la ENSANCHÓ al meter entre los dos el testigo con
#  sus dos `fsync`. Se dice así de claro: no la introdujo el testigo, la hizo visible.
#
#  Las dos pruebas son las dos mitades, y hacen falta las dos. Una sola que exigiera «no
#  revientes» se satisfaría devolviendo el objeto nuevo —publicar una transición que aún
#  puede revertirse—, y una sola que exigiera «revienta» volvería a dar el diagnóstico
#  falso. Juntas fijan que la ventana y la corrupción se distinguen y NINGUNA devuelve
#  contenido.
# ===========================================================================
class LaVentanaDePublicacion(unittest.TestCase):

    def _almacen(self):
        import estado
        espacio = tempfile.mkdtemp(prefix="ads-ventana-")
        self.addCleanup(shutil.rmtree, espacio, ignore_errors=True)
        os.makedirs(espacio, exist_ok=True)
        almacen = estado.inicializar(espacio)
        almacen.aplicar(estado.Transicion(
            tipo="prueba", base=almacen.revision()["revision_id"],
            operaciones=[estado.Escritura(
                "paquetes/pq-ventana.json",
                {"esquema": "ads.estado/1", "id": "pq-ventana", "estado": "listo"})],
            autor="prueba-de-la-ventana", motivo="fundar el objeto que se va a leer",
            id="tx-alta-ventana"))
        return almacen

    def _sustituir_el_objeto_sin_publicar_la_revision(self, almacen, nuevo):
        """Deja el disco EXACTAMENTE como lo deja el paso 8, y no ejecuta el paso 9."""
        from estado.serializacion import cid, serializar_canonico
        destino = almacen._d.ruta_canonica("paquetes/pq-ventana.json")
        datos = serializar_canonico(nuevo)
        with open(destino, "wb") as manejador:
            manejador.write(datos)
        return cid(datos)

    def test_T310_la_ventana_de_publicacion_NO_se_diagnostica_como_corrupcion(self):
        """`E-08` bis · el objeto es el que el testigo dice haber publicado.

        Se reproduce la ventana con fidelidad: el objeto nuevo en `canonico/`, el TESTIGO del
        paso 8 escrito con ese mismo `cid`, y `REVISION.json` todavía en la revisión
        anterior. El lector NO puede devolver contenido —seguiría siendo publicar una
        transición reversible— y NO puede llamarlo corrupción, porque el remedio de una
        cosa y de la otra son distintos: aquí se RECUPERA, allí se investiga un fichero.
        """
        from estado.errores import PublicacionEnVuelo
        from estado.rutas import TESTIGO_DE_PUBLICACION
        from estado.serializacion import serializar_canonico
        almacen = self._almacen()
        nuevo = {"esquema": "ads.estado/1", "id": "pq-ventana", "estado": "ejecutando"}
        cid_nuevo = self._sustituir_el_objeto_sin_publicar_la_revision(almacen, nuevo)

        zona = almacen._d.zona_tx("tx-de-la-ventana")
        os.makedirs(zona, exist_ok=True)
        with open(os.path.join(zona, TESTIGO_DE_PUBLICACION), "wb") as manejador:
            manejador.write(serializar_canonico({
                "esquema": 1, "transaccion": "tx-de-la-ventana", "resultado": "publicado",
                "publicados": {"paquetes/pq-ventana.json": cid_nuevo}}))

        with self.assertRaises(PublicacionEnVuelo) as capturado:
            almacen.leer("paquetes/pq-ventana.json")
        self.assertEqual(capturado.exception.codigo, "PUBLICACION_EN_VUELO")
        self.assertIn("tx-de-la-ventana", str(capturado.exception))
        self.assertIn("COMPLETAR", str(capturado.exception))

    def test_T311_sin_testigo_que_lo_avale_sigue_siendo_ESTADO_CORRUPTO(self):
        """El control que impide que la corrección de `T310` se coma la corrupción real.

        Mismo disco alterado, y NINGÚN testigo que diga que esa transacción publicó ese
        `cid`. Es una modificación fuera del diario, y el diagnóstico tiene que seguir
        siendo ése: sin esta mitad, `T310` se satisfaría llamando «ventana» a cualquier
        fichero que no case, que es la degradación silenciosa que este encargo persigue.
        """
        from estado.errores import EstadoCorrupto, PublicacionEnVuelo
        almacen = self._almacen()
        self._sustituir_el_objeto_sin_publicar_la_revision(
            almacen, {"esquema": "ads.estado/1", "id": "pq-ventana", "estado": "alterado"})
        with self.assertRaises(EstadoCorrupto) as capturado:
            almacen.leer("paquetes/pq-ventana.json")
        self.assertNotIsInstance(capturado.exception, PublicacionEnVuelo)
        self.assertEqual(capturado.exception.codigo, "ESTADO_CORRUPTO")
        self.assertIn("fuera del diario", str(capturado.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
