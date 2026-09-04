#!/usr/bin/env python3
"""test_runtime — la batería del RUNTIME y del DISPATCHER (`F6`, corte 2, agente A).

Instancia el §4.5 del CONTRATO DEL CORTE 2, que a su vez instancia el §7 de
`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` y las materias que `(g)` deja al contrato
derivado: `g.6` (concurrencia), `g.9` (reconciliación) y `g.16` (condiciones observables).

CUATRO REGLAS QUE ESTA BATERÍA SE IMPONE, Y POR QUÉ:

  1. NINGUNA PRUEBA SE LIMITA A MIRAR. Ni un caso comprueba que un fichero existe o que un
     texto dice algo y se da por satisfecho. Todos mueven el runtime. Una batería que lee
     el árbol en vez de moverlo demuestra que alguien escribió los ficheros, no que el
     estado durable sea durable.

  2. LAS CAÍDAS SON CAÍDAS DE VERDAD y LA CONCURRENCIA ES CONCURRENCIA DE VERDAD. Los
     nueve puntos de `runtime/fallos.py` se ejercitan con `subprocess` y
     `ADS_RUNTIME_FALLO`, y el proceso muere por `os._exit(70)`: sin `finally`, sin cerrar
     ficheros, sin vaciar búferes, sin soltar el `flock` desde Python. Las carreras se
     corren con PROCESOS, no con hilos: dos hilos comparten el `flock` del mismo proceso y
     comparten memoria, así que una prueba con hilos no puede distinguir un lease durable
     de una variable compartida, que es exactamente lo que hay que distinguir.

  3. CADA CAÍDA DECLARA SU EXPECTATIVA ANTES DE MIRAR EL RESULTADO. Para los nueve puntos
     está escrito, en `EXPECTATIVAS_DE_CAIDA`, qué DEBE haber pasado justo tras el corte y
     qué DEBE haber pasado tras reiniciar. Nunca «lo que salga». Una prueba de recuperación
     que acepta las dos ramas no distingue un runtime correcto de uno que publica basura.

  4. LO QUE SE CUENTA SON DOS BITÁCORAS, NO UNA. El adaptador en pruebas registra las
     INVOCACIONES por separado de las EJECUCIONES. Con una sola no se podría probar la
     idempotencia: «no se aplicó dos veces» sería indistinguible de «no se intentó dos
     veces», y la segunda no demuestra nada.

Y una quinta, de forma: la salida se PUBLICA como evidencia, así que el resumen de
`unittest` no lleva duración (`_RunnerDeterminista`, COPIADO de `tooling/tests/`, no
importado) y todo fichero que se abre se cierra: un `ResourceWarning` lleva dentro la ruta
absoluta y aleatoria de un temporal.

    python3 kernel/operativo/runtime/pruebas/test_runtime.py

Sale con 0 si todo pasa. Se ejecuta desde cualquier directorio: la raíz se deriva de
`__file__` y NUNCA del `cwd`.
"""
from __future__ import annotations

import ast
import fcntl
import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest

# --- localización del paquete ------------------------------------------------------
# `kernel/` no es un paquete Python. El patrón del repositorio es insertar el directorio
# del runtime en `sys.path`. La raíz se DERIVA de `__file__`: este fichero vive en
# <raiz>/kernel/operativo/runtime/pruebas/, luego la raíz está cuatro niveles arriba.
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
RUNTIME = os.path.join(RAIZ, "kernel", "operativo", "runtime")
CLI = os.path.join(RUNTIME, "ads_runtime.py")
CLI_ESTADO = os.path.join(RUNTIME, "ads_estado.py")
PAQUETE = os.path.join(RUNTIME, "runtime")
sys.path.insert(0, RUNTIME)

try:
    import estado
    import runtime as paquete_runtime
    from runtime import fallos, lease as modulo_lease, modelo, politica
except ImportError as exc:      # el paquete todavía no está: que se vea por qué
    print(f"no se encuentra el paquete `runtime` bajo {RUNTIME}: {exc}", file=sys.stderr)
    raise

# El entorno de las pruebas NO hereda ninguna de las dos variables de corte. Si alguien las
# tuviera puestas en su terminal, media batería moriría por una causa que no es la que se
# está probando, y el informe culparía al runtime.
ENTORNO = {
    clave: valor for clave, valor in os.environ.items()
    if clave not in ("ADS_RUNTIME_FALLO", "ADS_ESTADO_FALLO")
}

# Los nueve puntos del §4.2 del contrato, escritos aquí SÓLO para poder confrontarlos con
# el censo que el runtime declara. El runtime los deriva; esta lista existe para
# contrastarlos, no para sustituirlos.
PUNTOS_DEL_CONTRATO = [
    "antes-de-adquirir",
    "despues-de-adquirir",
    "antes-de-ejecutar",
    "durante-la-ejecucion",
    "despues-del-efecto-antes-del-acuse",
    "despues-del-acuse-antes-de-liberar",
    "antes-de-reintentar",
    "antes-de-agotar",
    "antes-de-liberar",
]

# El vocabulario CERRADO del §3 y la tabla de transiciones del §4.2, transcritos del
# contrato. Se escriben aquí para CONFRONTAR el dato del runtime, no para sustituirlo.
VOCABULARIO_DEL_CONTRATO = [
    "listo", "despachado", "ejecutando", "completado", "fallido", "agotado",
    "pausado", "cancelado", "bloqueado", "esperando-dependencia",
]
TABLA_DEL_CONTRATO = {
    "listo": {"despachado", "pausado", "cancelado", "bloqueado", "esperando-dependencia"},
    "despachado": {"ejecutando", "listo", "fallido", "cancelado"},
    "ejecutando": {"completado", "fallido", "cancelado"},
    "fallido": {"listo", "agotado"},
    "agotado": {"listo"},
    "pausado": {"listo", "cancelado"},
    "bloqueado": {"listo", "cancelado"},
    "esperando-dependencia": {"listo", "bloqueado", "cancelado"},
    "completado": set(),
    "cancelado": set(),
}

CODIGO_SALIDA_CAIDA = 70          # `os._exit(70)` del §4.2
SEGUNDOS_DE_ESPERA = 180          # techo de cada subproceso; ninguna prueba debe colgarse


# ===================================================================================
# utilidades — todas ejecutan cosas, ninguna «comprueba» por su cuenta
# ===================================================================================
def texto_de(ruta):
    """Lectura que CIERRA. Un `open(...).read()` suelto deja el descriptor al recolector."""
    with open(ruta, "r", encoding="utf-8") as fichero:
        return fichero.read()


def json_de(ruta):
    return json.loads(texto_de(ruta))


def lineas_de(ruta):
    if not os.path.exists(ruta):
        return []
    return [linea for linea in texto_de(ruta).splitlines() if linea]


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as fichero:
        fichero.write(texto)


def codigo_de_error(proceso):
    """El `[CODIGO]` que la CLI imprime en `stderr`, o `None`."""
    casacion = re.search(r"\[([A-Z_]+)\]", proceso.stderr + proceso.stdout)
    return casacion.group(1) if casacion else None


# --- guiones que corren como PROCESOS REALES ---------------------------------------
# Un guión, y no un hilo. El §4.5 lo exige y la razón es física: dos hilos del mismo
# proceso comparten el `flock` del testigo de vida y comparten memoria, de modo que una
# carrera entre hilos no puede distinguir un lease DURABLE de una variable compartida.

GUION_TITULAR = textwrap.dedent('''\
    """Toma el lease de un paquete y se queda VIVO hasta que la prueba cierre su stdin."""
    import sys
    sys.path.insert(0, sys.argv[1])
    import runtime
    rt = runtime.Runtime(sys.argv[2], instancia=sys.argv[3]).abrir()
    lease = rt.adquirir(sys.argv[4])
    sys.stdout.write("titular epoca=" + str(lease["epoca"]) + "\\n")
    sys.stdout.flush()
    sys.stdin.readline()
    rt.cerrar()
    sys.stdout.write("cerrado\\n")
    sys.stdout.flush()
''')

GUION_MUERTE_CON_LEASE = textwrap.dedent('''\
    """Toma el lease y MUERE con `os._exit(70)`, sin soltar nada desde Python."""
    import os, sys
    sys.path.insert(0, sys.argv[1])
    import runtime
    rt = runtime.Runtime(sys.argv[2], instancia=sys.argv[3]).abrir()
    rt.adquirir(sys.argv[4])
    sys.stdout.write("adquirido\\n")
    sys.stdout.flush()
    os._exit(70)
''')


class Caso(unittest.TestCase):
    """Base con el andamiaje: un control repo temporal por prueba y nada compartido."""

    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory(prefix="ads-runtime-")
        self.addCleanup(self.temporal.cleanup)
        self.base = self.temporal.name
        self.repo = os.path.join(self.base, "repo")
        self.espacio = os.path.join(self.base, "adaptador")
        os.makedirs(self.repo)
        os.makedirs(self.espacio)

    # ------------------------------------------------------------------ procesos
    def cli(self, argumentos, *, instancia="runtime-A", fallo=None, adaptador=True,
            adaptador_local=False, paciencia=None, cwd=None):
        """Ejecuta `ads_runtime.py` en un PROCESO REAL.

        `cwd` por defecto es el temporal del sistema y no la raíz del repositorio: así cada
        invocación demuestra, de paso, que el runtime no depende del directorio actual.
        """
        entorno = dict(ENTORNO)
        if fallo:
            entorno["ADS_RUNTIME_FALLO"] = fallo
        orden = [sys.executable, CLI, "--repo", self.repo, "--instancia", instancia]
        if adaptador:
            orden += ["--registro-en-pruebas", self.espacio]
        if adaptador_local:
            # El adaptador de PROCESO REAL del corte `V7`, que lanza un `subprocess` de
            # verdad. Es el único que produce un `pid`, y por eso hace falta para cruzar
            # «adaptador real × invariante durable».
            orden += ["--adaptador-local", os.path.join(self.base, "proceso-real")]
        if paciencia is not None:
            orden += ["--paciencia", str(paciencia)]
        orden += [str(a) for a in argumentos]
        return subprocess.run(orden, capture_output=True, text=True, env=entorno,
                              timeout=SEGUNDOS_DE_ESPERA,
                              cwd=cwd or tempfile.gettempdir())

    def cli_estado(self, argumentos):
        return subprocess.run(
            [sys.executable, CLI_ESTADO, "--repo", self.repo] + [str(a) for a in argumentos],
            capture_output=True, text=True, env=dict(ENTORNO),
            timeout=SEGUNDOS_DE_ESPERA, cwd=tempfile.gettempdir())

    def guion(self, nombre, cuerpo, argumentos):
        """Escribe un guión y lo lanza como proceso REAL, sin esperar a que termine."""
        ruta = os.path.join(self.base, nombre)
        escribir(ruta, cuerpo)
        return subprocess.Popen(
            [sys.executable, ruta, RUNTIME, self.repo] + [str(a) for a in argumentos],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, env=dict(ENTORNO), cwd=tempfile.gettempdir())

    # ------------------------------------------------------------------ atajos
    def exito(self, proceso, que=""):
        self.assertEqual(
            proceso.returncode, 0,
            f"{que}: la orden salió con {proceso.returncode}\n"
            f"stdout: {proceso.stdout}\nstderr: {proceso.stderr}")
        return proceso

    def alta(self, paquetes, *, item="it-0001"):
        """Da de alta un item y sus paquetes. `paquetes` es una lista de diccionarios."""
        self.exito(self.cli(["crear-item", "--id", item, "--titulo", "trabajo del owner",
                             "--motivo", "alta de prueba"]), "crear-item")
        for definicion in paquetes:
            orden = ["crear-paquete", "--id", definicion["id"], "--item", item]
            for capacidad in definicion.get("capacidades", ["proceso-local"]):
                orden += ["--capacidad", capacidad]
            for argumento in definicion.get("argumentos", ["exito"]):
                orden += ["--argumento", argumento]
            if "prioridad" in definicion:
                orden += ["--prioridad", str(definicion["prioridad"])]
            if "max_intentos" in definicion:
                orden += ["--max-intentos", str(definicion["max_intentos"])]
            for dependencia in definicion.get("depende_de", []):
                orden += ["--depende-de", dependencia]
            self.exito(self.cli(orden), "crear-paquete " + definicion["id"])

    # ------------------------------------------------------------------ lecturas
    def canonico(self, dominio, identificador):
        ruta = os.path.join(self.repo, "estado", "canonico", dominio,
                            identificador + ".json")
        return json_de(ruta) if os.path.exists(ruta) else None

    def paquete(self, identificador):
        return self.canonico("paquetes", identificador)

    def lease(self, identificador):
        return self.canonico("leases", identificador)

    def efectos(self):
        directorio = os.path.join(self.repo, "estado", "canonico", "efectos")
        if not os.path.isdir(directorio):
            return []
        return sorted(os.listdir(directorio))

    def vivos(self):
        """Los testigos de vida que hay AHORA en el plano operacional, ordenados.

        NO se llama `testigos`: `unittest` descubre por el prefijo `test`, y con ese nombre
        el andamiaje se colaba en el informe publicado como un caso que no comprueba nada.

        Es el instrumento de la vía rápida del §3, y por eso se mira directamente: el
        fichero `<instancia>.vivo` sólo debe quedar cuando su proceso murió sin poder
        limpiarlo.
        """
        directorio = os.path.join(self.repo, "estado", "operacional", "runtime")
        if not os.path.isdir(directorio):
            return []
        return sorted(os.listdir(directorio))

    def flock_libre(self, instancia):
        """¿El `flock` del testigo está LIBRE? Se sondea de verdad, no se supone.

        Un descriptor propio, un `flock` no bloqueante y su liberación inmediata. Es la
        misma pregunta que hace `TestigoDeVida.titular_muerto`, planteada desde fuera para
        que la prueba no dependa de la implementación que está comprobando.
        """
        ruta = os.path.join(self.repo, "estado", "operacional", "runtime",
                            instancia + ".vivo")
        descriptor = os.open(ruta, os.O_RDWR)
        try:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                return False
            fcntl.flock(descriptor, fcntl.LOCK_UN)
            return True
        finally:
            os.close(descriptor)

    def ejecuciones(self):
        return lineas_de(os.path.join(self.espacio, "ejecuciones.log"))

    def invocaciones(self):
        return lineas_de(os.path.join(self.espacio, "invocaciones.log"))

    def pendencias(self):
        """Las APERTURAS sin resolución, deducidas por el motor. `lineas` trae su cuerpo."""
        proceso = self.exito(self.cli_estado(["--json", "reconciliacion", "--pendientes"]),
                             "reconciliacion")
        return json.loads(proceso.stdout)["lineas"]

    def revision(self):
        proceso = self.exito(self.cli_estado(["--json", "revision"]), "revision")
        return json.loads(proceso.stdout)["revision"]


# ===================================================================================
# T182 · ciclo y despacho
# ===================================================================================
class CicloYDespacho(Caso):

    def test_01_un_ciclo_despacha_lo_elegible_y_deja_el_efecto_acusado(self):
        """T182 · Defecto que previene: dar por despachado lo que nunca quedó escrito.

        Un ciclo completo sobre dos paquetes. Lo que se comprueba NO es que la orden
        devuelva éxito, sino que el ESTADO CANÓNICO lo diga: los dos paquetes en
        `completado`, un acuse durable por cada efecto, `aplicado: true`, y el `intentos`
        consumido escrito en el paquete. Si el runtime fuese la fuente de verdad, todo eso
        viviría en memoria y aquí no habría nada que leer.
        """
        self.alta([{"id": "pq-0001"}, {"id": "pq-0002"}])
        informe = json.loads(self.exito(self.cli(["--json", "ciclo"]), "ciclo").stdout)

        self.assertEqual(informe["elegibles"], ["pq-0001", "pq-0002"])
        self.assertEqual([a["desenlace"] for a in informe["atendidos"]],
                         ["completado", "completado"])
        for identificador in ("pq-0001", "pq-0002"):
            objeto = self.paquete(identificador)
            self.assertEqual(objeto["estado"], "completado", identificador)
            self.assertEqual(objeto["intentos"], 1, identificador)
            acuse = self.canonico("efectos", objeto["efecto"])
            self.assertIsNotNone(acuse, "no hay acuse durable de " + identificador)
            self.assertTrue(acuse["aplicado"])
            self.assertEqual(acuse["paquete"], identificador)
            self.assertEqual(acuse["intento"], 1)
        self.assertEqual(len(self.ejecuciones()), 2)
        self.assertEqual(self.efectos(), sorted(
            self.paquete(p)["efecto"] + ".json" for p in ("pq-0001", "pq-0002")))

    def test_02_elegibles_se_deriva_del_estado_y_ordena_igual_para_toda_instancia(self):
        """T182 · Defecto que previene: dos instancias con listas distintas de trabajo.

        `elegibles()` no puede depender de quién pregunta ni del orden en que el sistema de
        ficheros devolvió los nombres: si dos instancias vieran listas distintas, la carrera
        por un paquete sería un accidente y no una propiedad.

        CORREGIDA HACIA ARRIBA: esta prueba afirmaba «prioridad descendente, después
        identificador», que son DOS de los CUATRO criterios que `b.12` paso 5 ordena
        estrictamente —prioridad declarada · grado de salida en el grafo · antigüedad de
        espera · identificador—. Con sólo esos dos, un paquete cuyo identificador ordena
        tarde queda por detrás de CADA paquete nuevo que entre con su misma prioridad, para
        siempre: es la inanición que `b.12` existe para impedir, y la prueba la daba por
        buena. `pq-media-b` se da de alta ANTES que `pq-media-a`, así que lleva más tiempo
        `listo` y el criterio (c) lo pone delante; el identificador sólo desempata cuando los
        tres criterios anteriores empatan, y para eso está `pq-empate-*`.
        """
        self.alta([
            {"id": "pq-baja", "prioridad": 10},
            {"id": "pq-alta", "prioridad": 90},
            {"id": "pq-media-b", "prioridad": 50},
            {"id": "pq-media-a", "prioridad": 50},
        ])
        esperada = ["pq-alta", "pq-media-b", "pq-media-a", "pq-baja"]
        for instancia in ("runtime-A", "runtime-B"):
            proceso = self.exito(self.cli(["--json", "elegibles"], instancia=instancia),
                                 "elegibles " + instancia)
            elegibles = json.loads(proceso.stdout)["elegibles"]
            vista = [e["paquete"] for e in elegibles]
            self.assertEqual(vista, esperada, "la lista de " + instancia + " difiere")
            # Y la antigüedad es la que manda entre los dos de en medio: se PUBLICA, para
            # que el orden se pueda contrastar y no haya que creérselo.
            por_id = {e["paquete"]: e for e in elegibles}
            self.assertGreater(por_id["pq-media-b"]["tiempo_listo"],
                               por_id["pq-media-a"]["tiempo_listo"])
            for entrada in elegibles:
                for campo in ("tiempo_listo", "postergaciones", "adelantado_por",
                              "impedimento", "grado_de_salida"):
                    self.assertIn(campo, entrada, entrada["paquete"])

    def test_03_sin_adaptador_para_la_capacidad_el_paquete_no_se_toca(self):
        """T182 · Defecto que previene: consumir un intento por no encontrar adaptador.

        Un paquete que pide una capacidad que nadie declara tiene que dar
        `CAPACIDAD_NO_SOPORTADA` SIN abrir intento y SIN retener la autoridad: si abriese
        intento, tres pasadas sin adaptador agotarían el paquete y abrirían una pendencia de
        reconciliación que no describe ningún trabajo fallido; si retuviera el lease, ningún
        otro runtime podría tomarlo sin acumular tres observaciones.
        """
        self.alta([{"id": "pq-0001", "capacidades": ["capacidad-que-nadie-declara"]}])
        proceso = self.cli(["despachar", "pq-0001"])
        self.assertEqual(proceso.returncode, 1)
        self.assertEqual(codigo_de_error(proceso), "CAPACIDAD_NO_SOPORTADA")
        objeto = self.paquete("pq-0001")
        self.assertEqual(objeto["estado"], "listo")
        self.assertEqual(objeto["intentos"], 0)
        self.assertIsNone(objeto["efecto"])
        self.assertIsNone(self.lease("pq-0001"), "el lease se quedó tomado")
        self.assertEqual(self.efectos(), [])

    def test_04_un_adaptador_de_otra_version_de_contrato_es_incompatible(self):
        """T182 · Defecto que previene: ejecutar contra una interfaz que no es la pactada.

        El §4.4 fija `VERSION_DE_CONTRATO = 1`. Un adaptador que declara otra versión no se
        ejecuta «a ver si va»: se rechaza con `ADAPTADOR_INCOMPATIBLE`, y lo mismo un
        objeto que no expone `ejecutar`. La comprobación vive en la SELECCIÓN y no sólo en
        el alta, porque el registro productivo lo construye otro y el runtime no controla
        su alta.
        """
        class DeOtraVersion(paquete_runtime.Adaptador):
            identificador = "de-otra-version"
            version_de_contrato = 2
            capacidades = ["proceso-local"]

        with self.assertRaises(paquete_runtime.AdaptadorIncompatible) as capturado:
            paquete_runtime.comprobar_adaptador(DeOtraVersion(), ["proceso-local"])
        self.assertEqual(capturado.exception.codigo, "ADAPTADOR_INCOMPATIBLE")

        registro = paquete_runtime.RegistroEnPruebas([
            paquete_runtime.AdaptadorEnPruebas(self.espacio),
        ])
        with self.assertRaises(paquete_runtime.CapacidadNoSoportada):
            registro.seleccionar(["capacidad-inexistente"])
        with self.assertRaises(paquete_runtime.CapacidadNoSoportada):
            registro.seleccionar([])
        self.assertEqual(
            registro.seleccionar(["proceso-local"]).identificador,
            "adaptador-en-pruebas")

    def test_05_una_dependencia_aparca_el_paquete_y_completarla_lo_libera(self):
        """T182 · Defecto que previene: despachar trabajo cuyo insumo no existe todavía.

        `pq-hijo` depende de `pq-padre`. El primer ciclo tiene que dejar al hijo en
        `esperando-dependencia` —no en `fallido`, que consumiría un intento, y no
        despachado— y el segundo, ya con el padre `completado`, tiene que completarlo. Se
        comprueba además que el hijo no ejecutó nada mientras esperaba: una sola ejecución
        tras el primer ciclo.

        CORREGIDA HACIA ARRIBA: el hijo iba primero por su identificador, que es el CUARTO
        criterio de `b.12` paso 5 y sólo desempata. Con el criterio (b) —«desbloquea a más
        paquetes»— implementado, el PADRE va primero porque libera al hijo, y el barrido los
        cerraba los dos de una pasada: la propiedad que esta prueba mide —una espera aparca,
        y aparcar no consume intento— dejaba de ejercitarse. Para conservarla se declara al
        hijo URGENTE, que es el primer criterio y el único que el Owner gobierna: así el
        hijo vuelve a ir delante, se aparca, y lo que se prueba se sigue probando.
        """
        self.alta([{"id": "pq-padre"},
                   {"id": "pq-hijo", "depende_de": ["pq-padre"], "prioridad": 90}])
        self.exito(self.cli(["ciclo"]), "primer ciclo")
        self.assertEqual(self.paquete("pq-padre")["estado"], "completado")
        self.assertEqual(self.paquete("pq-hijo")["estado"], "esperando-dependencia")
        self.assertEqual(self.paquete("pq-hijo")["intentos"], 0)
        self.assertEqual(len(self.ejecuciones()), 1)

        self.exito(self.cli(["ciclo"]), "segundo ciclo")
        self.assertEqual(self.paquete("pq-hijo")["estado"], "completado")
        self.assertEqual(len(self.ejecuciones()), 2)

    def test_06_una_espera_que_deja_de_ser_viable_se_convierte_en_bloqueo(self):
        """T182 · Defecto que previene: una espera muerta que nadie vuelve a mirar (`b.8`).

        `b.8` es explícito: `esperando-dependencia` se resuelve solo y NO genera trabajo,
        pero «si deja de ser viable, DEBE convertirse en bloqueo: no puede quedar muerta».
        Se cancela el padre y se comprueba que el hijo pasa a `bloqueado` —que sí genera
        trabajo— y no se queda esperando a algo que ya no va a completarse nunca.
        """
        self.alta([{"id": "pq-padre"}, {"id": "pq-hijo", "depende_de": ["pq-padre"]}])
        self.exito(self.cli(["cancelar", "pq-padre", "--motivo", "el owner lo retira",
                             "--autoridad", "owner"]), "cancelar")
        self.exito(self.cli(["ciclo"]), "ciclo")
        self.assertEqual(self.paquete("pq-hijo")["estado"], "bloqueado")
        vista = json.loads(self.exito(self.cli(["--json", "vistas"]), "vistas").stdout)
        self.assertIn("pq-hijo",
                      [e["paquete"] for e in vista["que_esta_bloqueado"]])

    def test_07_la_tabla_de_transiciones_es_exactamente_la_del_contrato(self):
        """T182 · Defecto que previene: un estado alcanzado por un camino que nadie aprobó.

        Se recorren las CIEN combinaciones del vocabulario cerrado y se confronta cada una
        con la tabla del §4.2 transcrita en esta prueba. Una permitida de más es un camino
        que el contrato no autoriza; una de menos es trabajo que se quedaría atascado. El
        vocabulario se compara entero: ninguna palabra de más, ninguna de menos.
        """
        self.assertEqual(sorted(modelo.ESTADOS), sorted(VOCABULARIO_DEL_CONTRATO))
        for desde in VOCABULARIO_DEL_CONTRATO:
            for hasta in VOCABULARIO_DEL_CONTRATO:
                permitida = hasta in TABLA_DEL_CONTRATO[desde]
                if permitida:
                    self.assertEqual(modelo.comprobar_transicion(desde, hasta), hasta)
                else:
                    with self.assertRaises(paquete_runtime.EstadoDePaqueteInvalido,
                                           msg=f"{desde} → {hasta} debería estar prohibida"):
                        modelo.comprobar_transicion(desde, hasta)

    def test_08_las_vistas_son_derivadas_y_no_se_persisten(self):
        """T182 · Defecto que previene: una vista que sabe más que el estado (§7.5).

        Dos mitades. Primera: las vistas responden las cinco preguntas del §7.5 con datos
        que están en el estado. Segunda, y es la que importa: pedirlas NO escribe nada. Se
        compara el número de revisión antes y después, y se comprueba que no ha aparecido
        ningún dominio canónico nuevo. Una vista materializada sería una segunda verdad.
        """
        self.alta([{"id": "pq-0001"}, {"id": "pq-0002", "argumentos": ["fallo-definitivo"]}])
        self.exito(self.cli(["ciclo"]), "ciclo")
        antes = self.revision()
        dominios_antes = sorted(os.listdir(
            os.path.join(self.repo, "estado", "canonico")))

        vista = json.loads(self.exito(self.cli(["--json", "vistas"]), "vistas").stdout)
        self.assertTrue(vista["derivada"])
        for clave in ("que_se_esta_construyendo", "que_esta_bloqueado",
                      "que_espera_decision_del_owner", "que_cambio",
                      "reconciliaciones_abiertas"):
            self.assertIn(clave, vista)
        self.assertEqual([e["paquete"] for e in vista["que_espera_decision_del_owner"]],
                         ["pq-0002"])
        self.assertEqual([r["registro"] for r in vista["reconciliaciones_abiertas"]],
                         ["rec-0001"])
        self.assertTrue(vista["que_cambio"], "la vista no explica qué cambió")

        self.assertEqual(self.revision(), antes, "pedir la vista movió la revisión")
        self.assertEqual(sorted(os.listdir(
            os.path.join(self.repo, "estado", "canonico"))), dominios_antes)

    def test_09_no_hay_un_segundo_sistema_de_estado(self):
        """T182 · Defecto que previene: un diario paralelo o un fichero de trabajo propio.

        Tras un ciclo completo con éxito, fallo y agotamiento, se enumera TODO lo que hay
        bajo el control repo. Lo único admisible es lo que el motor ya define: `FORMATO`,
        `REVISION`, `canonico/`, `diario/`, `reconciliacion/`, `.gitignore` y el plano
        OPERACIONAL. Cualquier otra cosa escrita por el runtime sería un segundo sistema de
        estado, y el §0 del contrato lo prohíbe por su nombre.
        """
        self.alta([{"id": "pq-0001"},
                   {"id": "pq-0002", "argumentos": ["fallo-definitivo"]}])
        self.exito(self.cli(["ciclo"]), "ciclo")

        permitidas = {"FORMATO.json", "REVISION.json", ".gitignore"}
        prefijos = ("canonico/", "diario/", "reconciliacion/", "operacional/")
        raiz = os.path.join(self.repo, "estado")
        intrusas = []
        for directorio, _sub, ficheros in os.walk(raiz):
            for nombre in ficheros:
                relativa = os.path.relpath(os.path.join(directorio, nombre), raiz)
                relativa = relativa.replace(os.sep, "/")
                if relativa in permitidas or relativa.startswith(prefijos):
                    continue
                intrusas.append(relativa)
        self.assertEqual(intrusas, [], "hay ficheros fuera de la disposición del motor")

        # Y nada del runtime vive FUERA de `estado/` dentro del control repo.
        fuera = [n for n in os.listdir(self.repo) if n != "estado"]
        self.assertEqual(fuera, [], "el runtime escribió fuera de `estado/`")

        # Los dominios canónicos son exactamente los CUATRO del §3.
        self.assertEqual(
            sorted(os.listdir(os.path.join(raiz, "canonico"))),
            ["efectos", "items", "leases", "paquetes"])

    def test_10_operar_sin_abrir_o_tras_cerrar_es_fallo_cerrado(self):
        """T182 · Defecto que previene: despachar con un almacén que nadie ha recuperado.

        `abrir()` recupera ANTES de despachar, y ese orden no se puede saltar. Un runtime
        sin abrir —o ya cerrado— no responde «vacío»: falla cerrado. Devolver una lista
        vacía haría creer que no hay trabajo cuando lo que no hay es almacén.
        """
        rt = paquete_runtime.Runtime(self.repo, instancia="runtime-A")
        with self.assertRaises(paquete_runtime.RuntimeInconsistente):
            rt.elegibles()
        self.alta([{"id": "pq-0001"}])
        with paquete_runtime.Runtime(self.repo, instancia="runtime-Z") as abierto:
            self.assertEqual([e["paquete"] for e in abierto.elegibles()], ["pq-0001"])
        with self.assertRaises(paquete_runtime.RuntimeInconsistente):
            abierto.elegibles()


# ===================================================================================
# T183 · autoridad y leases
# ===================================================================================
class AutoridadYLeases(Caso):

    def test_20_dos_dispatchers_reales_no_despachan_el_mismo_paquete(self):
        """T183 · Defecto que previene: dos dispatchers despachando el mismo paquete.

        DOS PROCESOS, no dos hilos. `runtime-A` toma el lease y se queda VIVO sosteniendo
        su testigo; mientras tanto `runtime-B` intenta despachar el mismo paquete. La
        expectativa está escrita antes de mirar: B tiene que salir con 1 y
        `AUTORIDAD_NO_DISPONIBLE`, el paquete tiene que seguir intacto —`listo`, cero
        intentos, sin efecto— y el adaptador NO puede haber sido invocado ni una sola vez.
        Cero invocaciones, y no «cero ejecuciones»: si B hubiese llegado a llamar al
        adaptador, el recibo habría escondido el doble despacho.
        """
        self.alta([{"id": "pq-0001"}])
        titular = self.guion("titular.py", GUION_TITULAR, ["runtime-A", "pq-0001"])
        try:
            aviso = titular.stdout.readline()
            self.assertIn("titular", aviso, "el titular no llegó a tomar el lease")
            self.assertEqual(self.lease("pq-0001")["titular"], "runtime-A")

            competidor = self.cli(["despachar", "pq-0001"], instancia="runtime-B")
            self.assertEqual(competidor.returncode, 1,
                             "el segundo dispatcher no fue rechazado:\n"
                             + competidor.stdout + competidor.stderr)
            self.assertEqual(codigo_de_error(competidor), "AUTORIDAD_NO_DISPONIBLE")
        finally:
            titular.stdin.close()
            titular.wait(timeout=SEGUNDOS_DE_ESPERA)
            titular.stdout.close()
            titular.stderr.close()

        objeto = self.paquete("pq-0001")
        self.assertEqual(objeto["estado"], "listo")
        self.assertEqual(objeto["intentos"], 0)
        self.assertIsNone(objeto["efecto"])
        self.assertEqual(self.invocaciones(), [])
        self.assertEqual(self.efectos(), [])
        self.assertEqual(self.lease("pq-0001")["titular"], "runtime-A")

    def test_21_una_carrera_real_no_ejecuta_ningun_paquete_dos_veces(self):
        """T183 · Defecto que previene: doble despacho cuando la carrera es de verdad.

        SEIS paquetes y DOS procesos lanzados a la vez sobre el mismo almacén, sin
        coordinación entre ellos. La expectativa: los seis terminan `completado`, hay
        exactamente SEIS invocaciones del adaptador y SEIS efectos acusados. Una invocación
        de más significa que dos dispatchers entraron en el mismo paquete, y el recibo del
        adaptador no lo taparía porque lo que se cuenta son invocaciones.
        """
        self.alta([{"id": "pq-000" + str(n)} for n in range(1, 7)])
        entorno = dict(ENTORNO)
        procesos = [
            subprocess.Popen(
                [sys.executable, CLI, "--repo", self.repo, "--instancia", instancia,
                 "--registro-en-pruebas", self.espacio, "ciclo"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                env=entorno, cwd=tempfile.gettempdir())
            for instancia in ("runtime-A", "runtime-B")
        ]
        salidas = []
        for proceso in procesos:
            salida, error = proceso.communicate(timeout=SEGUNDOS_DE_ESPERA)
            salidas.append((proceso.returncode, salida, error))
        for codigo, salida, error in salidas:
            self.assertEqual(codigo, 0, "un ciclo falló:\n" + salida + error)

        for n in range(1, 7):
            self.assertEqual(self.paquete("pq-000" + str(n))["estado"], "completado")
        self.assertEqual(len(self.invocaciones()), 6,
                         "hubo invocaciones de más: dos dispatchers entraron en el mismo "
                         "paquete")
        self.assertEqual(len(self.ejecuciones()), 6)
        self.assertEqual(len(self.efectos()), 6)

    def test_22_renovar_sube_el_latido_y_borra_las_observaciones(self):
        """T183 · Defecto que previene: reclamar a un titular que sí estaba avanzando.

        El `latido` no mide tiempo: mide progreso. Renovar lo sube y borra las
        observaciones acumuladas, de modo que un aspirante que ya llevaba dos tiene que
        empezar de cero. Se comprueba en el ESTADO DURABLE, no en el valor devuelto.
        """
        self.alta([{"id": "pq-0001"}])
        self.exito(self.cli(["adquirir", "pq-0001"]), "adquirir")
        # La orden de A terminó LIMPIAMENTE, así que su testigo ya no está y su estado es
        # INDECIDIBLE: manda la regla de las observaciones, que es lo que aquí se mide.
        self.assertEqual(self.vivos(), [], "una salida limpia dejó testigo")
        self.exito(self.cli(["observar", "pq-0001"], instancia="runtime-B"), "observar 1")
        self.exito(self.cli(["observar", "pq-0001"], instancia="runtime-B"), "observar 2")
        self.assertEqual(
            self.lease("pq-0001")["observado_por"]["runtime-B"]["observaciones"], 2)

        self.exito(self.cli(["renovar", "pq-0001"]), "renovar")
        vigente = self.lease("pq-0001")
        self.assertEqual(vigente["latido"], 1)
        self.assertEqual(vigente["observado_por"], {})

        proceso = self.cli(["reclamar", "pq-0001"], instancia="runtime-B")
        self.assertEqual(proceso.returncode, 1)
        self.assertEqual(codigo_de_error(proceso), "RECLAMACION_PREMATURA")

    def test_23_la_expiracion_se_decide_por_observaciones_y_no_por_un_plazo(self):
        """T183 · Defecto que previene: una caducidad de reloj dentro del estado durable.

        `I-g3` prohíbe el reloj en cualquier byte durable, así que un lease no caduca: se
        RECLAMA tras `PACIENCIA` observaciones consecutivas sin que el latido avance. Se
        borra el testigo de vida del titular para forzar el camino LENTO —el de entre
        máquinas, donde no hay `flock` compartido— y se comprueba que con dos observaciones
        la reclamación es PREMATURA y con la tercera prospera, subiendo la época.
        """
        self.alta([{"id": "pq-0001"}])
        self.exito(self.cli(["adquirir", "pq-0001"]), "adquirir")
        # La orden de A salió bien y retiró su testigo, luego su estado es INDECIDIBLE y
        # no hay vía rápida: manda la regla de las observaciones. Es exactamente lo que
        # `runtime-B` vería si A viviera en OTRA máquina, reproducido sin dos máquinas.
        self.assertEqual(self.vivos(), [])

        for numero in (1, 2):
            self.exito(self.cli(["observar", "pq-0001"], instancia="runtime-B"),
                       "observar " + str(numero))
            prematura = self.cli(["reclamar", "pq-0001"], instancia="runtime-B")
            self.assertEqual(prematura.returncode, 1, "reclamó con " + str(numero))
            self.assertEqual(codigo_de_error(prematura), "RECLAMACION_PREMATURA")

        self.exito(self.cli(["observar", "pq-0001"], instancia="runtime-B"), "observar 3")
        self.exito(self.cli(["reclamar", "pq-0001"], instancia="runtime-B"), "reclamar")
        vigente = self.lease("pq-0001")
        self.assertEqual(vigente["titular"], "runtime-B")
        self.assertEqual(vigente["epoca"], 2)
        self.assertEqual(vigente["latido"], 0)
        self.assertEqual(vigente["observado_por"], {})

    def test_24_ni_siquiera_una_muerte_real_permite_reclamar_sin_observar(self):
        """T183 · Defecto que previene: reponer la vía rápida por comodidad.

        Antes había un atajo: si el testigo de vida del titular existía con el `flock`
        libre, se concluía MUERTE y se reclamaba en el acto. La auditoría independiente lo
        rompió sustituyendo el fichero —ver `test_33`—, y se retiró entero.

        Aquí se comprueba el coste de haberlo retirado, que es real y se paga a gusto: un
        titular que MURIÓ de verdad, con `os._exit(70)` y sin ejecutar `finally`, deja la
        huella más favorable que existe —testigo presente, `flock` libre— y **aun así** no
        se le puede quitar el lease sin observar. La expectativa: `adquirir` rechaza,
        `reclamar` es PREMATURA, y sólo tras `PACIENCIA` observaciones durables prospera.

        Que la prueba compruebe que el atajo NO funciona, teniendo delante el único caso en
        que sería correcto, es lo que impide que alguien lo reponga sin darse cuenta.
        """
        self.alta([{"id": "pq-0001"}])
        muerto = self.guion("muerte.py", GUION_MUERTE_CON_LEASE, ["runtime-A", "pq-0001"])
        salida, error = muerto.communicate(timeout=SEGUNDOS_DE_ESPERA)
        self.assertEqual(muerto.returncode, CODIGO_SALIDA_CAIDA,
                         "el proceso no murió como se le pidió:\n" + salida + error)
        self.assertIn("adquirido", salida)
        self.assertEqual(self.lease("pq-0001")["titular"], "runtime-A")
        # La huella más favorable posible: el testigo QUEDÓ y su `flock` está libre.
        self.assertEqual(self.vivos(), ["runtime-A.vivo"])
        self.assertTrue(self.flock_libre("runtime-A"))

        negado = self.cli(["adquirir", "pq-0001"], instancia="runtime-B")
        self.assertEqual(negado.returncode, 1, "`adquirir` robó a un muerto")
        self.assertEqual(codigo_de_error(negado), "AUTORIDAD_NO_DISPONIBLE")
        prematura = self.cli(["reclamar", "pq-0001"], instancia="runtime-B")
        self.assertEqual(prematura.returncode, 1,
                         "se reclamó sin observar, apoyándose en el testigo")
        self.assertEqual(codigo_de_error(prematura), "RECLAMACION_PREMATURA")

        for numero in (1, 2, 3):
            self.exito(self.cli(["observar", "pq-0001"], instancia="runtime-B"),
                       "observar " + str(numero))
        self.exito(self.cli(["reclamar", "pq-0001"], instancia="runtime-B"), "reclamar")
        vigente = self.lease("pq-0001")
        self.assertEqual(vigente["titular"], "runtime-B")
        self.assertEqual(vigente["epoca"], 2)
        self.assertEqual(vigente["observado_por"], {})

    def test_25_la_perdida_de_autoridad_no_escribe_absolutamente_nada(self):
        """T183 · Defecto que previene: pisar al titular vigente con un resultado viejo.

        `runtime-A` tiene el lease; `runtime-B` se lo lleva por observaciones. Cuando A
        vuelve a escribir, la expectativa está escrita: `AUTORIDAD_PERDIDA`, y el estado
        canónico EXACTAMENTE igual que antes del intento —misma revisión, mismo lease—.
        No basta con que A falle: tiene que no haber tocado nada.
        """
        self.alta([{"id": "pq-0001"}])
        self.exito(self.cli(["adquirir", "pq-0001"]), "adquirir A")
        for _ in range(3):
            self.exito(self.cli(["observar", "pq-0001"], instancia="runtime-B"), "observar")
        self.exito(self.cli(["reclamar", "pq-0001"], instancia="runtime-B"), "reclamar")

        revision_antes = self.revision()
        lease_antes = self.lease("pq-0001")

        for orden in (["renovar", "pq-0001"], ["liberar", "pq-0001"]):
            proceso = self.cli(orden, instancia="runtime-A")
            self.assertEqual(proceso.returncode, 1, " ".join(orden))
            self.assertEqual(codigo_de_error(proceso), "AUTORIDAD_PERDIDA")
        self.assertEqual(self.revision(), revision_antes,
                         "la pérdida de autoridad movió la revisión")
        self.assertEqual(self.lease("pq-0001"), lease_antes)

    def test_26_liberar_devuelve_a_listo_un_intento_que_nadie_ejecuto(self):
        """T183 · Defecto que previene: dejar un `despachado` que nadie va a recoger.

        Se corta en `antes-de-ejecutar`, que deja el paquete `ejecutando`, y se comprueba el
        otro lado: liberar un `despachado` lo devuelve a `listo`, que es la única
        transición que la tabla permite desde ahí. Un `ejecutando` NO se toca, porque la
        tabla no lleva de vuelta y su reanudación reutiliza el mismo efecto.
        """
        self.alta([{"id": "pq-0001"}])
        with paquete_runtime.Runtime(self.repo, instancia="runtime-A") as rt:
            lease = rt.adquirir("pq-0001")
            rt._abrir_intento("pq-0001", lease)
            self.assertEqual(self.paquete("pq-0001")["estado"], "despachado")
            rt.liberar("pq-0001")
        self.assertEqual(self.paquete("pq-0001")["estado"], "listo")
        self.assertIsNone(self.lease("pq-0001"))

    def test_27_ningun_byte_durable_lleva_reloj_pid_ni_uuid(self):
        """T183 · Defecto que previene: un tiempo lógico que en realidad es el reloj.

        `I-g3` prohíbe reloj de pared, duración, número de ejecución e identidad de proceso
        en cualquier cosa que se escriba en `canonico/`, `diario/` o `reconciliacion/`. La
        comprobación se hace en dos planos y los dos hacen falta: contra el CÓDIGO —ningún
        módulo del paquete importa `time`, `datetime`, `uuid` o `random`, ni nombra
        `getpid`— y contra el DISCO, donde no puede aparecer ninguna de esas huellas. El
        `flock` del testigo de vida vive en `operacional/`, que está gitignorado y queda
        fuera de la prohibición a propósito.
        """
        prohibidos = {"time", "datetime", "uuid", "random", "calendar"}
        for nombre in sorted(os.listdir(PAQUETE)):
            if not nombre.endswith(".py"):
                continue
            fuente = texto_de(os.path.join(PAQUETE, nombre))
            arbol = ast.parse(fuente, filename=nombre)
            for nodo in ast.walk(arbol):
                if isinstance(nodo, ast.Import):
                    for alias in nodo.names:
                        self.assertNotIn(alias.name.split(".")[0], prohibidos,
                                         nombre + " importa " + alias.name)
                elif isinstance(nodo, ast.ImportFrom) and nodo.module:
                    self.assertNotIn(nodo.module.split(".")[0], prohibidos,
                                     nombre + " importa de " + nodo.module)
            self.assertNotIn("getpid", fuente, nombre + " nombra `getpid`")

        self.alta([{"id": "pq-0001"},
                   {"id": "pq-0002", "argumentos": ["fallo-definitivo"]}])
        self.exito(self.cli(["ciclo"]), "ciclo")
        self._exigir_bytes_durables_sin_reloj_ni_pid("registro en pruebas")

    def test_27b_el_adaptador_de_proceso_REAL_tampoco_mete_un_pid_en_el_estado(self):
        """T183 · Defecto que previene: un `pid` en el ESTADO CANÓNICO DURABLE.

        Lo encontró la auditoría independiente, y el hueco no estaba en la comprobación
        sino en su COBERTURA: `test_27` mira el disco de verdad, pero sólo corría contra el
        registro EN PRUEBAS, que no produce pid; y el escenario extremo a extremo, que sí
        usa el adaptador real, no comprobaba `I-g3`. Nadie cruzaba «adaptador real ×
        invariante durable», y por esa rendija `canonico/paquetes/<id>.json` acabó llevando
        `"pid": 1700531`. Esta prueba es exactamente ese cruce.

        El adaptador de proceso REAL de `adaptadores/` lanza un `subprocess` de verdad y su
        resultado incluye el `pid`. La expectativa: el paquete se completa —con la salida
        real del proceso, para que conste que se ejecutó—, el `resultado` durable contiene
        EXACTAMENTE las siete claves del §4.4 y ni una más, y no queda rastro de `pid` en
        ningún byte de `canonico/`, `diario/` ni `reconciliacion/`.
        """
        try:
            import adaptadores
        except ImportError as fallo:      # el corte `V7` todavía no está en el árbol
            self.skipTest("el adaptador real de `adaptadores/` no está disponible: "
                          + str(fallo))
        self.assertTrue(hasattr(adaptadores, "AdaptadorDeProcesoLocal"))

        self.exito(self.cli(["crear-item", "--id", "it-0001", "--titulo", "trabajo",
                             "--motivo", "alta"], adaptador=False), "crear-item")
        self.exito(self.cli(["crear-paquete", "--id", "pq-real", "--item", "it-0001",
                             "--capacidad", "proceso-local",
                             "--argumento", "/bin/echo", "--argumento", "hola"],
                            adaptador=False), "crear-paquete")
        self.exito(self.cli(["ciclo"], adaptador=False, adaptador_local=True),
                   "ciclo con el adaptador REAL")

        objeto = self.paquete("pq-real")
        self.assertEqual(objeto["estado"], "completado")
        self.assertEqual(objeto["resultado"]["salida"], "hola",
                         "el proceso real no llegó a ejecutarse: la prueba no cruza nada")
        self.assertEqual(sorted(objeto["resultado"]), sorted(politica.CLAVES_DE_RESULTADO),
                         "el resultado durable lleva claves que el §4.4 no declara")
        self._exigir_bytes_durables_sin_reloj_ni_pid("adaptador de proceso real")

    def _exigir_bytes_durables_sin_reloj_ni_pid(self, contexto):
        """`I-g3` sobre el DISCO: ni reloj, ni duración, ni identidad de proceso."""
        raiz = os.path.join(self.repo, "estado")
        for plano in ("canonico", "diario", "reconciliacion"):
            for directorio, _sub, ficheros in os.walk(os.path.join(raiz, plano)):
                for nombre in ficheros:
                    contenido = texto_de(os.path.join(directorio, nombre))
                    for huella in ("epoch", "timestamp", "duracion_segundos", "pid",
                                   "duracion", "inicio_utc", "fin_utc"):
                        self.assertNotIn(
                            '"' + huella + '"', contenido,
                            "hay `" + huella + "` en " + plano + "/" + nombre
                            + " (" + contexto + ")")

    def test_28_dos_procesos_no_pueden_llamarse_igual(self):
        """T183 · Defecto que previene: que `titular` deje de identificar a UNO solo.

        El nombre de instancia es el `titular` del lease durable y el nombre del testigo de
        vida. Si dos procesos vivos usaran el mismo, la vía rápida daría «muerto» sobre un
        titular vivo y habría doble despacho. Se comprueba que el segundo no arranca.
        """
        self.alta([{"id": "pq-0001"}])
        titular = self.guion("titular.py", GUION_TITULAR, ["runtime-A", "pq-0001"])
        try:
            self.assertIn("titular", titular.stdout.readline())
            gemelo = self.cli(["elegibles"], instancia="runtime-A")
            self.assertEqual(gemelo.returncode, 1)
            self.assertEqual(codigo_de_error(gemelo), "RUNTIME_INCONSISTENTE")
        finally:
            titular.stdin.close()
            titular.wait(timeout=SEGUNDOS_DE_ESPERA)
            titular.stdout.close()
            titular.stderr.close()


    def test_29_adquirir_nunca_roba_el_lease_de_otro_proceso(self):
        """T183 · Defecto que previene: el lease se lo lleva el siguiente que lo pida.

        LA REGRESIÓN, y es la que se escapó. Dos órdenes de CLI, dos procesos, dos
        instancias, sin trucos:

            ads_runtime --instancia runtime-A adquirir pq-ok   → titular runtime-A, época 1
            ads_runtime --instancia runtime-B adquirir pq-ok   → época 2, ¡robado!

        La primera orden TERMINABA BIEN y dejaba su testigo de vida en el disco con el
        `flock` ya suelto, que es exactamente la huella que un proceso MUERTO deja. La vía
        rápida no podía distinguirlos y elegía la lectura peligrosa, así que en el modelo de
        la CLI —un proceso por orden, donde el titular nunca está vivo entre dos órdenes— el
        lease no protegía absolutamente nada.

        La expectativa, escrita antes de mirar: `runtime-B` sale con 1 y
        `AUTORIDAD_NO_DISPONIBLE`; el titular durable SIGUE siendo `runtime-A`; la época NO
        se mueve; y una salida limpia no deja testigo.
        """
        self.alta([{"id": "pq-ok"}])
        self.exito(self.cli(["adquirir", "pq-ok"], instancia="runtime-A"), "adquirir A")
        self.assertEqual(self.lease("pq-ok")["titular"], "runtime-A")
        self.assertEqual(self.lease("pq-ok")["epoca"], 1)
        self.assertEqual(self.vivos(), [],
                         "una orden que terminó bien dejó su testigo, y ésa es la huella "
                         "que sólo debería dejar una muerte")

        ladron = self.cli(["adquirir", "pq-ok"], instancia="runtime-B")
        self.assertEqual(ladron.returncode, 1,
                         "el segundo proceso se llevó el lease:\n"
                         + ladron.stdout + ladron.stderr)
        self.assertEqual(codigo_de_error(ladron), "AUTORIDAD_NO_DISPONIBLE")
        vigente = self.lease("pq-ok")
        self.assertEqual(vigente["titular"], "runtime-A")
        self.assertEqual(vigente["epoca"], 1)

    def test_30_despachar_tampoco_roba_el_lease_de_otro_proceso(self):
        """T183 · Defecto que previene: el mismo robo, por el camino que sí ejecuta.

        `adquirir` es la puerta, pero la que hace daño es `despachar`: si robase, EJECUTARÍA
        el trabajo de otro. La expectativa: `AUTORIDAD_NO_DISPONIBLE`, código 1, el paquete
        intacto —`listo`, cero intentos, sin efecto—, CERO invocaciones del adaptador y el
        titular sin cambiar. Cero invocaciones y no «cero ejecuciones»: si hubiera llegado a
        llamar al adaptador, el recibo habría escondido el doble despacho.
        """
        self.alta([{"id": "pq-ok"}])
        self.exito(self.cli(["adquirir", "pq-ok"], instancia="runtime-A"), "adquirir A")

        ladron = self.cli(["despachar", "pq-ok"], instancia="runtime-B")
        self.assertEqual(ladron.returncode, 1,
                         "el segundo proceso despachó trabajo ajeno:\n"
                         + ladron.stdout + ladron.stderr)
        self.assertEqual(codigo_de_error(ladron), "AUTORIDAD_NO_DISPONIBLE")
        objeto = self.paquete("pq-ok")
        self.assertEqual(objeto["estado"], "listo")
        self.assertEqual(objeto["intentos"], 0)
        self.assertIsNone(objeto["efecto"])
        self.assertEqual(self.invocaciones(), [])
        self.assertEqual(self.efectos(), [])
        self.assertEqual(self.lease("pq-ok")["titular"], "runtime-A")

        # Y un ciclo entero tampoco lo toca: la reanudación reclama SÓLO ante muerte
        # probada, y aquí el estado del titular es indecidible.
        informe = json.loads(self.exito(self.cli(["--json", "ciclo"],
                                                 instancia="runtime-B"), "ciclo").stdout)
        self.assertEqual(informe["reclamados"], [])
        self.assertEqual(self.lease("pq-ok")["titular"], "runtime-A")
        self.assertEqual(self.invocaciones(), [])

    def test_31_la_reclamacion_tiene_UNA_puerta_y_deja_su_evento_en_el_diario(self):
        """T183 · Defecto que previene: un robo con papeles en regla.

        Tras retirar la vía rápida queda una sola puerta —`PACIENCIA` observaciones
        consecutivas sin que el latido avance— y esta prueba la recorre entera comprobando
        que cada paso es DURABLE y auditable, que es lo que la hace resistente: falsificar
        una observación exige falsificar el estado canónico, y eso sí se detecta.

        La expectativa: tres observaciones anotadas en el lease con su latido; la
        reclamación sube la época y deja un evento `runtime.lease.reclamado` propio en el
        diario, con su autor, distinguible de una adquisición corriente; y el estado sigue
        íntegro después.
        """
        self.alta([{"id": "pq-0001"}])
        self.exito(self.cli(["adquirir", "pq-0001"], instancia="runtime-A"), "adquirir A")
        for numero in (1, 2, 3):
            self.exito(self.cli(["observar", "pq-0001"], instancia="runtime-B"),
                       "observar " + str(numero))
            anotacion = self.lease("pq-0001")["observado_por"]["runtime-B"]
            self.assertEqual(anotacion["observaciones"], numero)
            self.assertEqual(anotacion["latido"], self.lease("pq-0001")["latido"])

        self.exito(self.cli(["reclamar", "pq-0001"], instancia="runtime-B"), "reclamar")
        self.assertEqual(self.lease("pq-0001")["titular"], "runtime-B")
        self.assertEqual(self.lease("pq-0001")["epoca"], 2)

        eventos = [json.loads(linea) for linea in lineas_de(
            os.path.join(self.repo, "estado", "diario", "DIARIO.jsonl"))]
        reclamaciones = [e for e in eventos
                         if e["tipo"] == "transicion.confirmada"
                         and e.get("clase") == "runtime.lease.reclamado"]
        self.assertEqual(len(reclamaciones), 1)
        self.assertEqual(reclamaciones[0]["autor"], "runtime-B")
        observaciones = [e for e in eventos
                         if e["tipo"] == "transicion.confirmada"
                         and e.get("clase") == "runtime.lease.observado"]
        self.assertEqual(len(observaciones), 3,
                         "las observaciones tienen que ser transiciones DURABLES")
        self.exito(self.cli_estado(["verificar"]), "integridad tras la reclamación")

    def test_33_sustituir_el_testigo_de_un_titular_VIVO_no_da_autoridad(self):
        """T183 · Defecto que previene: robar el lease de un titular VIVO. LA REGRESIÓN.

        El ataque de la auditoría independiente, ejecutado tal cual. Con `runtime-A` VIVO y
        sosteniendo el lease, un tercero **borra su testigo de vida y crea otro en su
        sitio**. El testigo nuevo existe y su `flock` está libre, que es exactamente la
        huella que la vía rápida leía como MUERTE:

            A vivo? poll = None    testigo de A presente: True
            >>> testigo de runtime-A SUSTITUIDO. A sigue vivo: True
            reclamar de B  exit= 0   → {"titular": "runtime-B", "epoca": 2}
            >>> B despacha pq-ok con A todavía ejecutándolo
            integridad del estado: VERDE

        No hizo falta matar a nadie ni tocar el estado. Y era peor que tocarlo: editar el
        lease a mano da `ESTADO_CORRUPTO` y se ve; esto dejaba la integridad VERDE y un
        `runtime.lease.reclamado` de aspecto legítimo en el diario. El plano operacional es
        reconstruible y no durable por definición de `g.1` —fuera de la huella, fuera de la
        admisión, fuera del versionado—, así que **una credencial que cualquiera puede
        fabricar no puede decidir autoridad**, y no hay forma de autenticarla desde dentro.

        La expectativa, escrita antes de mirar: `reclamar` de B FALLA con
        `RECLAMACION_PREMATURA`; `adquirir` de B FALLA con `AUTORIDAD_NO_DISPONIBLE`; el
        titular durable SIGUE siendo `runtime-A` en la época 1; y el paquete NO se ejecuta
        dos veces.
        """
        self.alta([{"id": "pq-ok"}])
        vivo = self.guion("titular.py", GUION_TITULAR, ["runtime-A", "pq-ok"])
        try:
            self.assertIn("titular", vivo.stdout.readline())
            self.assertIsNone(vivo.poll(), "el titular tenía que seguir VIVO")
            testigo = os.path.join(self.repo, "estado", "operacional", "runtime",
                                   "runtime-A.vivo")
            self.assertTrue(os.path.exists(testigo))

            # EL ATAQUE: se sustituye el fichero. Inodo nuevo, `flock` libre, A vivo.
            os.remove(testigo)
            with open(testigo, "w", encoding="utf-8"):
                pass
            self.assertIsNone(vivo.poll(), "el titular murió por su cuenta y la prueba "
                                           "dejaría de demostrar lo que dice")
            self.assertTrue(self.flock_libre("runtime-A"),
                            "la sustitución no dejó el `flock` libre: no hay ataque")

            robo = self.cli(["reclamar", "pq-ok"], instancia="runtime-B")
            self.assertEqual(robo.returncode, 1,
                             "SE ROBÓ EL LEASE DE UN TITULAR VIVO:\n"
                             + robo.stdout + robo.stderr)
            self.assertEqual(codigo_de_error(robo), "RECLAMACION_PREMATURA")

            negado = self.cli(["adquirir", "pq-ok"], instancia="runtime-B")
            self.assertEqual(negado.returncode, 1)
            self.assertEqual(codigo_de_error(negado), "AUTORIDAD_NO_DISPONIBLE")

            despacho = self.cli(["despachar", "pq-ok"], instancia="runtime-B")
            self.assertEqual(despacho.returncode, 1)
            self.assertEqual(codigo_de_error(despacho), "AUTORIDAD_NO_DISPONIBLE")

            vigente = self.lease("pq-ok")
            self.assertEqual(vigente["titular"], "runtime-A")
            self.assertEqual(vigente["epoca"], 1)
            self.assertEqual(self.invocaciones(), [],
                             "el paquete se ejecutó pese a no tener autoridad")
        finally:
            vivo.stdin.close()
            vivo.wait(timeout=SEGUNDOS_DE_ESPERA)
            vivo.stdout.close()
            vivo.stderr.close()

    def test_34_ninguna_ruta_de_decision_consulta_el_plano_operacional(self):
        """T183 · Defecto que previene: que el atajo vuelva por la puerta de atrás.

        El diagnóstico del testigo sobrevive —un operador quiere poder mirarlo— pero SÓLO
        como diagnóstico. Se comprueba contra el ÁRBOL SINTÁCTICO del dispatcher que la
        única llamada a `diagnostico_del_testigo` está en `estado_de_paquete`, que es una
        lectura y no decide nada, y que el nombre viejo no ha vuelto a aparecer en ninguna
        parte del paquete. Comprobarlo contra el código y no contra el comportamiento es lo
        que hace que el día que alguien lo llame desde `adquirir` la prueba se entere.
        """
        fuente = texto_de(os.path.join(PAQUETE, "dispatcher.py"))
        arbol = ast.parse(fuente, filename="dispatcher.py")
        llamantes = []
        for nodo in ast.walk(arbol):
            if not isinstance(nodo, ast.FunctionDef):
                continue
            for interno in ast.walk(nodo):
                if isinstance(interno, ast.Call) and isinstance(interno.func, ast.Attribute) \
                        and interno.func.attr == "diagnostico_del_testigo":
                    llamantes.append(nodo.name)
        self.assertEqual(sorted(llamantes), ["estado_de_paquete"],
                         "el diagnóstico del plano operacional se consulta desde una ruta "
                         "de decisión: es fabricable y no puede decidir autoridad")

        for nombre in sorted(os.listdir(PAQUETE)):
            if nombre.endswith(".py"):
                cuerpo = texto_de(os.path.join(PAQUETE, nombre))
                self.assertNotIn("def titular_muerto", cuerpo, nombre)
                self.assertNotIn("_reclamar_si_murio", cuerpo, nombre)

    def test_32_ninguna_salida_limpia_deja_testigo_de_vida(self):
        """T183 · Defecto que previene: que terminar bien parezca haber muerto.

        La otra mitad de la corrección, y la que hace válidas las tres lecturas. Se ejercen
        órdenes de las tres clases —lectura, autoridad y despacho— y tras cada una el plano
        operacional tiene que quedar SIN testigos. Un testigo que sobrevive a una salida
        limpia vuelve a hacer indistinguible el final ordenado del abrupto, que es
        exactamente el defecto que se está cerrando.
        """
        self.alta([{"id": "pq-0001"}])
        ordenes = (
            ["elegibles"],
            ["adquirir", "pq-0001"],
            ["renovar", "pq-0001"],
            ["liberar", "pq-0001"],
            ["vistas"],
            ["ciclo"],
            ["estado-paquete", "pq-0001"],
        )
        for orden in ordenes:
            self.exito(self.cli(orden), " ".join(orden))
            self.assertEqual(self.vivos(), [],
                             "`" + " ".join(orden) + "` dejó testigo tras salir bien")
        self.assertEqual(self.paquete("pq-0001")["estado"], "completado")

        # Y el cierre por gestor de contexto se comporta igual, que es como lo usa quien
        # embebe el runtime en vez de invocar la CLI.
        with paquete_runtime.Runtime(self.repo, instancia="runtime-C") as rt:
            self.assertEqual(self.vivos(), ["runtime-C.vivo"])
            self.assertFalse(self.flock_libre("runtime-C"),
                             "un runtime VIVO debe sostener su `flock`")
            rt.vistas()
        self.assertEqual(self.vivos(), [])


# ===================================================================================
# T184 · reintentos, agotamiento y reconciliación
# ===================================================================================
class ReintentosYReconciliacion(Caso):

    def test_40_un_fallo_reintentable_consume_un_intento_y_vuelve_a_listo(self):
        """T184 · Defecto que previene: un reintento sin tope, que es un livelock.

        El precedente de `a.9` es tres. La expectativa está escrita: tras la primera pasada
        el paquete queda `listo` con `intentos = 1`; tras la segunda, `listo` con 2; tras la
        tercera, `agotado` con 3, y NUNCA un cuarto intento. Cada intento tiene su propio
        efecto, así que hay tres acuses distintos y tres ejecuciones reales.
        """
        self.alta([{"id": "pq-0001", "argumentos": ["fallo-reintentable"]}])
        for pasada, esperado in ((1, "listo"), (2, "listo"), (3, "agotado")):
            self.exito(self.cli(["ciclo"]), "pasada " + str(pasada))
            objeto = self.paquete("pq-0001")
            self.assertEqual(objeto["estado"], esperado, "pasada " + str(pasada))
            self.assertEqual(objeto["intentos"], pasada, "pasada " + str(pasada))
        self.assertEqual(len(self.efectos()), 3, "los tres intentos comparten efecto")
        self.assertEqual(len(self.ejecuciones()), 3)

        # Una cuarta pasada NO puede volver a ejecutar: `agotado` no es elegible.
        self.exito(self.cli(["ciclo"]), "cuarta pasada")
        self.assertEqual(self.paquete("pq-0001")["intentos"], 3)
        self.assertEqual(len(self.ejecuciones()), 3)

    def test_41_agotar_abre_la_reconciliacion_en_la_misma_pasada(self):
        """T184 · Defecto que previene: agotar sin dejar rastro deducible (`g.9`).

        `g.6` y `g.9`: agotar deja las órdenes intactas y PRODUCE el registro auxiliar. La
        expectativa: en la MISMA pasada en que el paquete pasa a `agotado` aparece una
        apertura sin resolución, con el item y el número de intento correctos, y a partir de
        ahí el estado canónico del trabajo no se toca más —una pasada adicional no cambia
        la revisión—.
        """
        self.alta([{"id": "pq-0001", "argumentos": ["fallo-definitivo"]}])
        self.assertEqual(self.pendencias(), [])
        informe = json.loads(self.exito(self.cli(["--json", "ciclo"]), "ciclo").stdout)

        self.assertEqual(self.paquete("pq-0001")["estado"], "agotado")
        self.assertEqual(informe["reconciliaciones_pendientes"], ["rec-0001"])
        pendencias = self.pendencias()
        self.assertEqual(len(pendencias), 1)
        self.assertEqual(pendencias[0]["item"], "it-0001")
        self.assertEqual(pendencias[0]["intento"], 1)
        self.assertEqual(pendencias[0]["repositorio"], "control")
        self.assertIn("EJECUCION_DEFINITIVA", pendencias[0]["causa"])

        revision_antes = self.revision()
        self.exito(self.cli(["ciclo"]), "segunda pasada")
        self.assertEqual(self.revision(), revision_antes,
                         "el estado canónico se tocó después de agotar")

    def test_42_un_fallo_definitivo_no_gasta_los_intentos_que_quedan(self):
        """T184 · Defecto que previene: repetir una operación que ya se sabe imposible.

        «Sólo se reintenta el fallo REINTENTABLE» (§4.2). Un fallo definitivo va a `agotado`
        en el PRIMER intento aunque queden dos: gastarlos sería tres ejecuciones para llegar
        al mismo sitio, y tres pendencias donde debía haber una.
        """
        self.alta([{"id": "pq-0001", "argumentos": ["fallo-definitivo"]}])
        self.exito(self.cli(["ciclo"]), "ciclo")
        objeto = self.paquete("pq-0001")
        self.assertEqual(objeto["estado"], "agotado")
        self.assertEqual(objeto["intentos"], 1)
        self.assertEqual(objeto["max_intentos"], 3)
        self.assertEqual(len(self.ejecuciones()), 1)
        self.assertEqual(len(self.pendencias()), 1)

    def test_43_las_cuatro_clases_de_fallo_dan_cuatro_errores_distintos(self):
        """T184 · Defecto que previene: tratar cuatro cosas distintas como si fueran una.

        Reintentable, definitivo, cancelación y tiempo agotado tienen consecuencias
        distintas, así que tienen error tipado distinto y transición propia. La cuarta clase
        del §4.2 —la pérdida de autoridad— no la produce el adaptador sino la relectura del
        lease, y tiene su propia prueba en `T183`.
        """
        self.alta([
            {"id": "pq-reintentable", "argumentos": ["fallo-reintentable"]},
            {"id": "pq-definitivo", "argumentos": ["fallo-definitivo"]},
            {"id": "pq-cancelado", "argumentos": ["cancelacion"]},
            {"id": "pq-timeout", "argumentos": ["timeout"]},
        ])
        esperados = {
            "pq-reintentable": ("EJECUCION_FALLIDA", "listo"),
            "pq-definitivo": ("EJECUCION_DEFINITIVA", "agotado"),
            "pq-cancelado": ("EJECUCION_CANCELADA", "cancelado"),
            "pq-timeout": ("TIEMPO_AGOTADO", "listo"),
        }
        for identificador, (codigo, estado_final) in sorted(esperados.items()):
            proceso = self.cli(["despachar", identificador])
            self.assertEqual(proceso.returncode, 1, identificador)
            self.assertEqual(codigo_de_error(proceso), codigo, identificador)
            self.assertEqual(self.paquete(identificador)["estado"], estado_final,
                             identificador)

    def test_46_un_paquete_agotado_no_vuelve_a_adquirirse(self):
        """T184 · Defecto que previene: reservar autoridad sobre trabajo que nadie moverá.

        El §4 lo afirma —«un paquete agotado no vuelve a adquirirse»— y `despachar` sí lo
        rechazaba, así que no había daño práctico; pero `adquirir` lo concedía, y una
        afirmación del contrato que no se sostiene es una afirmación que alguien acabará
        usando. Lo señaló la auditoría independiente.

        La expectativa: `adquirir` sobre `agotado` da `ESTADO_DE_PAQUETE_INVALIDO`, no se
        crea lease, y el estado no se mueve. Y lo mismo para los dos terminales, por la
        misma razón: de `completado` y `cancelado` la tabla del §4.2 no lleva a ninguna
        parte, así que tomar autoridad ahí es reservar algo que nadie va a mover.
        """
        self.alta([{"id": "pq-agotado", "argumentos": ["fallo-definitivo"]},
                   {"id": "pq-hecho"},
                   {"id": "pq-retirado"}])
        # La cancelación va ANTES del ciclo: `cancelado` es terminal, y un paquete que ya
        # se completó no se puede cancelar —la tabla del §4.2 no lo permite—.
        self.exito(self.cli(["cancelar", "pq-retirado", "--motivo", "el owner lo retira",
                             "--autoridad", "owner"]), "cancelar")
        self.exito(self.cli(["ciclo"]), "ciclo")
        self.assertEqual(self.paquete("pq-agotado")["estado"], "agotado")
        self.assertEqual(self.paquete("pq-hecho")["estado"], "completado")
        self.assertEqual(self.paquete("pq-retirado")["estado"], "cancelado")

        revision_antes = self.revision()
        for identificador in ("pq-agotado", "pq-hecho", "pq-retirado"):
            proceso = self.cli(["adquirir", identificador])
            self.assertEqual(proceso.returncode, 1, identificador)
            self.assertEqual(codigo_de_error(proceso), "ESTADO_DE_PAQUETE_INVALIDO",
                             identificador + ":\n" + proceso.stderr)
            self.assertIsNone(self.lease(identificador),
                              "se creó un lease sobre `" + identificador + "`")
        self.assertEqual(self.revision(), revision_antes,
                         "un rechazo de adquisición movió el estado")

    def test_47_un_resultado_AMBIGUO_ni_se_reintenta_ni_se_da_por_bueno(self):
        """T184 · Defecto que previene: duplicar un efecto en silencio, o inventar un éxito.

        La ventana que encontró la auditoría independiente: si el proceso muere ENTRE
        ejecutar y escribir el recibo, al reiniciar no hay recibo, se vuelve a invocar y el
        efecto se aplica dos veces. El adaptador la cierra escribiendo un recibo de
        INTENCIÓN antes de ejecutar y cerrándolo después; una segunda llamada que encuentre
        uno abierto y sin cerrar devuelve `estado: "ambiguo"`.

        Con un proceso externo cualquiera NO se puede prometer «exactamente una vez»: entre
        lanzar el trabajo y anotar que se lanzó hay siempre una ventana. Lo que sí se puede
        —y es lo que se comprueba aquí— es que la ambigüedad **se DETECTE en vez de
        duplicarse en silencio**, y que la resuelva quien tiene autoridad.

        La expectativa: error tipado `EJECUCION_AMBIGUA`; el paquete queda `agotado` —NO
        `completado`, que inventaría un éxito, y NO `listo`, que arriesgaría aplicar el
        efecto otra vez—; queda una pendencia de `g.9` cuya causa NOMBRA la ambigüedad; y
        los intentos que quedaban NO se gastan, porque reintentar es precisamente el riesgo
        que se está evitando.
        """
        self.alta([{"id": "pq-ambiguo", "argumentos": ["ambiguo"], "max_intentos": 3}])
        proceso = self.cli(["despachar", "pq-ambiguo"])
        self.assertEqual(proceso.returncode, 1)
        self.assertEqual(codigo_de_error(proceso), "EJECUCION_AMBIGUA")

        objeto = self.paquete("pq-ambiguo")
        self.assertEqual(objeto["estado"], "agotado")
        self.assertEqual(objeto["intentos"], 1, "un ambiguo NO gasta los intentos")
        self.assertEqual(objeto["resultado"]["estado"], "ambiguo",
                         "el resultado durable tiene que conservar la ambigüedad")
        self.assertIsNotNone(self.canonico("efectos", objeto["efecto"]))

        pendencias = self.pendencias()
        self.assertEqual(len(pendencias), 1)
        self.assertIn("EJECUCION_AMBIGUA", pendencias[0]["causa"],
                      "la causa del registro de `g.9` no nombra la ambigüedad")
        self.assertIn("ambigua", pendencias[0]["causa"])

        # Y no se reintenta sola: una pasada más no vuelve a invocar al adaptador.
        invocaciones = len(self.invocaciones())
        self.exito(self.cli(["ciclo"]), "pasada posterior")
        self.assertEqual(len(self.invocaciones()), invocaciones,
                         "un ambiguo se reintentó, que es justo lo que no puede pasar")
        self.assertEqual(self.paquete("pq-ambiguo")["estado"], "agotado")

    def test_48_la_ambiguedad_se_clasifica_aunque_la_politica_se_aplique_despues(self):
        """T184 · Defecto que previene: confundir un ambiguo con un fallo definitivo.

        Los dos aterrizan en `fallido` y de ahí en `agotado`, así que el estado del paquete
        no basta para distinguirlos: hay que mirar el RESULTADO escrito. Si se confundieran,
        la causa del registro de `g.9` nombraría la cosa equivocada y quien tenga que
        decidir leería «falló» donde dice «no se sabe si se hizo», que son decisiones
        opuestas. Se ejerce el camino en que la política se aplica en una pasada POSTERIOR
        —el proceso murió antes de aplicarla— y se comprueba que la clase se reconstruye
        del resultado.
        """
        self.alta([{"id": "pq-ambiguo", "argumentos": ["ambiguo"]}])
        caida = self.cli(["despachar", "pq-ambiguo"], fallo="antes-de-agotar")
        self.assertEqual(caida.returncode, CODIGO_SALIDA_CAIDA)
        self.assertEqual(self.paquete("pq-ambiguo")["estado"], "fallido")
        self.assertEqual(self.pendencias(), [])

        self.exito(self.cli(["ciclo"]), "reinicio")
        self.assertEqual(self.paquete("pq-ambiguo")["estado"], "agotado")
        pendencias = self.pendencias()
        self.assertEqual(len(pendencias), 1)
        self.assertIn("EJECUCION_AMBIGUA", pendencias[0]["causa"],
                      "al aplicar la política más tarde, el ambiguo se degradó a otra cosa")

    def test_44_la_pendencia_se_retira_solo_por_una_transicion_explicita(self):
        """T184 · Defecto que previene: cerrar una pendencia borrando una línea.

        `g.9` es taxativo: la pendencia «desaparece ÚNICAMENTE mediante una transición
        explícita y auditable de reconciliación». Se resuelve por la vía del motor y se
        comprueba que la pendencia deja de deducirse y que el registro conserva las DOS
        líneas —apertura y resolución—, porque es append-only.
        """
        self.alta([{"id": "pq-0001", "argumentos": ["fallo-definitivo"]}])
        self.exito(self.cli(["ciclo"]), "ciclo")
        self.assertEqual(len(self.pendencias()), 1)

        registro = os.path.join(self.repo, "estado", "reconciliacion", "REGISTRO.jsonl")
        lineas_antes = len(lineas_de(registro))
        self.exito(self.cli_estado(["resolver", "rec-0001", "--autoridad", "owner",
                                    "--motivo", "el owner decide seguir"]), "resolver")
        self.assertEqual(self.pendencias(), [])
        self.assertEqual(len(lineas_de(registro)), lineas_antes + 1,
                         "el registro dejó de ser append-only")

    def test_45_agotar_no_reintenta_pero_la_autoridad_se_suelta(self):
        """T184 · Defecto que previene: un lease huérfano sobre trabajo ya cerrado.

        Al agotar, la unidad de trabajo no se toca más: su salida la decide la autoridad. La
        AUTORIDAD, en cambio, sí se suelta, porque un lease puesto sobre un `agotado` no
        gobierna nada y obligaría a cualquier otra instancia a acumular tres observaciones
        para retirarlo.
        """
        self.alta([{"id": "pq-0001", "argumentos": ["fallo-definitivo"]}])
        self.exito(self.cli(["ciclo"]), "ciclo")
        self.assertEqual(self.paquete("pq-0001")["estado"], "agotado")
        self.assertIsNone(self.lease("pq-0001"), "quedó un lease sobre un `agotado`")


# ===================================================================================
# T185 · pausa, cancelación y reanudación
# ===================================================================================
class PausaCancelacionYReanudacion(Caso):

    def test_60_pausar_impide_el_despacho_y_reanudar_lo_devuelve(self):
        """T185 · Defecto que previene: seguir trabajando en lo que el Owner detuvo.

        La expectativa: pausado, el paquete deja de ser elegible y despacharlo da
        `ESTADO_DE_PAQUETE_INVALIDO` sin ejecutar nada; reanudado, vuelve a la lista y se
        completa. Se comprueba el contador de invocaciones: cero mientras está pausado.
        """
        self.alta([{"id": "pq-0001"}])
        self.exito(self.cli(["pausar", "pq-0001", "--motivo", "presupuesto",
                             "--autoridad", "owner"]), "pausar")
        self.assertEqual(self.paquete("pq-0001")["estado"], "pausado")
        elegibles = json.loads(
            self.exito(self.cli(["--json", "elegibles"]), "elegibles").stdout)["elegibles"]
        self.assertEqual(elegibles, [])

        rechazado = self.cli(["despachar", "pq-0001"])
        self.assertEqual(rechazado.returncode, 1)
        self.assertEqual(codigo_de_error(rechazado), "ESTADO_DE_PAQUETE_INVALIDO")
        self.assertEqual(self.invocaciones(), [])

        self.exito(self.cli(["reanudar", "pq-0001", "--motivo", "hay presupuesto",
                             "--autoridad", "owner"]), "reanudar")
        self.exito(self.cli(["ciclo"]), "ciclo")
        self.assertEqual(self.paquete("pq-0001")["estado"], "completado")
        self.assertEqual(len(self.ejecuciones()), 1)

    def test_61_cancelar_es_terminal_y_no_admite_reanudacion(self):
        """T185 · Defecto que previene: resucitar trabajo que la autoridad retiró.

        `cancelado` es terminal en la tabla del §4.2. Reanudarlo o pausarlo tiene que dar
        `ESTADO_DE_PAQUETE_INVALIDO`, y el paquete tiene que seguir `cancelado`.
        """
        self.alta([{"id": "pq-0001"}])
        self.exito(self.cli(["cancelar", "pq-0001", "--motivo", "cambio de plan",
                             "--autoridad", "owner"]), "cancelar")
        self.assertEqual(self.paquete("pq-0001")["estado"], "cancelado")
        for orden in (["reanudar", "pq-0001"], ["pausar", "pq-0001"]):
            proceso = self.cli(orden + ["--motivo", "insistir", "--autoridad", "owner"])
            self.assertEqual(proceso.returncode, 1, " ".join(orden))
            self.assertEqual(codigo_de_error(proceso), "ESTADO_DE_PAQUETE_INVALIDO")
        self.assertEqual(self.paquete("pq-0001")["estado"], "cancelado")

    def test_62_una_decision_sin_motivo_o_sin_autoridad_no_es_auditable(self):
        """T185 · Defecto que previene: un cambio de estado que nadie puede atribuir.

        `g.13` exige que todo cambio del estado canónico sea explicable. Una pausa sin
        motivo, o sin autoridad, no lo es, y el runtime la rechaza antes de escribir nada.
        """
        self.alta([{"id": "pq-0001"}])
        with paquete_runtime.Runtime(self.repo, instancia="runtime-A") as rt:
            for motivo, autoridad in (("", "owner"), ("   ", "owner"), ("un motivo", "")):
                with self.assertRaises(paquete_runtime.RuntimeInconsistente):
                    rt.pausar("pq-0001", motivo=motivo, autoridad=autoridad)
        self.assertEqual(self.paquete("pq-0001")["estado"], "listo")

    def test_63_la_cancelacion_se_lee_del_estado_y_no_de_una_bandera(self):
        """T185 · Defecto que previene: una bandera en memoria que puede mentir.

        El objeto `cancelacion` que el runtime entrega al adaptador no lleva una bandera:
        LEE el estado canónico cada vez que se le pregunta. Así una cancelación decidida por
        OTRO proceso —el caso normal, porque quien cancela no es quien ejecuta— se ve. Se
        comprueba sobre el mismo objeto antes y después de cancelar.
        """
        self.alta([{"id": "pq-0001"}])
        with paquete_runtime.Runtime(self.repo, instancia="runtime-A") as rt:
            testigo = paquete_runtime.Cancelacion(rt, "pq-0001")
            self.assertFalse(testigo.activada())
            self.exito(self.cli(["cancelar", "pq-0001", "--motivo", "el owner para",
                                 "--autoridad", "owner"], instancia="runtime-B"),
                       "cancelar desde otro proceso")
            self.assertTrue(testigo.activada(),
                            "la cancelación de otro proceso no se vio")

    def test_64_un_paquete_cancelado_a_medias_termina_cancelado(self):
        """T185 · Defecto que previene: publicar un `completado` de trabajo ya retirado.

        El adaptador declara la ejecución cancelada. La expectativa: el paquete termina en
        `cancelado` —terminal—, con su acuse durable escrito, sin reintento y SIN pendencia
        de reconciliación, porque nada quedó a medias esperando una decisión.
        """
        self.alta([{"id": "pq-0001", "argumentos": ["cancelacion"]}])
        proceso = self.cli(["despachar", "pq-0001"])
        self.assertEqual(proceso.returncode, 1)
        self.assertEqual(codigo_de_error(proceso), "EJECUCION_CANCELADA")
        objeto = self.paquete("pq-0001")
        self.assertEqual(objeto["estado"], "cancelado")
        self.assertIsNotNone(self.canonico("efectos", objeto["efecto"]))
        self.assertEqual(self.pendencias(), [])
        self.assertIsNone(self.lease("pq-0001"))


# ===================================================================================
# T186 · caída, recuperación e idempotencia del efecto
# ===================================================================================
#
# LA EXPECTATIVA DE CADA CAÍDA, ESCRITA ANTES DE MIRAR EL RESULTADO.
#
# Para cada punto del §4.2: qué paquete se usa, qué DEBE verse justo tras el corte y qué
# DEBE verse tras reiniciar. Ninguna entrada dice «lo que salga».
#
#   comportamiento          qué le pide la prueba al adaptador
#   tras_la_caida           (estado, hay_acuse, hay_lease, invocaciones, ejecuciones)
#   tras_reiniciar          (estado, intentos, invocaciones, ejecuciones, pendencias)
#
EXPECTATIVAS_DE_CAIDA = {
    # Muere antes de tocar nada: no hay lease, no hay intento, no hay invocación.
    "antes-de-adquirir": {
        "comportamiento": "exito",
        "tras_la_caida": ("listo", False, False, 0, 0),
        "tras_reiniciar": ("completado", 1, 1, 1, 0),
    },
    # La autoridad ya está escrita y sobrevive; el intento aún no se abrió.
    "despues-de-adquirir": {
        "comportamiento": "exito",
        "tras_la_caida": ("listo", False, True, 0, 0),
        "tras_reiniciar": ("completado", 1, 1, 1, 0),
    },
    # El intento está abierto y el efecto fijado, pero el adaptador no se ha llamado.
    "antes-de-ejecutar": {
        "comportamiento": "exito",
        "tras_la_caida": ("ejecutando", False, True, 0, 0),
        "tras_reiniciar": ("completado", 1, 1, 1, 0),
    },
    # El corte cae en el evento de progreso que el propio runtime emite AL ENTREGAR el
    # control, así que el adaptador todavía no ha sido invocado.
    "durante-la-ejecucion": {
        "comportamiento": "exito",
        "tras_la_caida": ("ejecutando", False, True, 0, 0),
        "tras_reiniciar": ("completado", 1, 1, 1, 0),
    },
    # EL CASO QUE HAY QUE CLAVAR. El efecto YA se aplicó y el acuse NO está escrito. Al
    # reiniciar hay que volver a invocar —el runtime no puede saber que se aplicó— y el
    # recibo del adaptador tiene que impedir que se aplique OTRA VEZ: dos invocaciones,
    # UNA sola ejecución.
    "despues-del-efecto-antes-del-acuse": {
        "comportamiento": "exito",
        "tras_la_caida": ("ejecutando", False, True, 1, 1),
        "tras_reiniciar": ("completado", 1, 2, 1, 0),
    },
    # Resultado y acuse ya son durables; lo único pendiente era soltar la autoridad.
    "despues-del-acuse-antes-de-liberar": {
        "comportamiento": "exito",
        "tras_la_caida": ("completado", True, True, 1, 1),
        "tras_reiniciar": ("completado", 1, 1, 1, 0),
    },
    # Falló de forma reintentable y el acuse está escrito, pero la política no se aplicó.
    # Al reiniciar se aplica y, en la misma pasada, se consume el segundo intento.
    "antes-de-reintentar": {
        "comportamiento": "fallo-reintentable",
        "tras_la_caida": ("fallido", True, True, 1, 1),
        "tras_reiniciar": ("listo", 2, 2, 2, 0),
    },
    # Falló de forma definitiva y el acuse está escrito, pero no se agotó ni se abrió la
    # pendencia. Al reiniciar aparecen las dos cosas, y exactamente una pendencia.
    "antes-de-agotar": {
        "comportamiento": "fallo-definitivo",
        "tras_la_caida": ("fallido", True, True, 1, 1),
        "tras_reiniciar": ("agotado", 1, 1, 1, 1),
    },
    # Todo está hecho salvo soltar el lease.
    "antes-de-liberar": {
        "comportamiento": "exito",
        "tras_la_caida": ("completado", True, True, 1, 1),
        "tras_reiniciar": ("completado", 1, 1, 1, 0),
    },
}


class CaidaRecuperacionEIdempotencia(Caso):

    def _estado_observado(self):
        objeto = self.paquete("pq-0001")
        acuse = (objeto["efecto"] is not None
                 and self.canonico("efectos", objeto["efecto"]) is not None)
        return (objeto["estado"], bool(acuse), self.lease("pq-0001") is not None,
                len(self.invocaciones()), len(self.ejecuciones()))

    def test_80_los_nueve_puntos_cortan_donde_dicen_y_se_recuperan_como_se_declaro(self):
        """T186 · Defecto que previene: aceptar cualquier recuperación como la buena.

        Los nueve puntos del §4.2, uno por uno, con PROCESOS REALES y `os._exit(70)`. Para
        cada uno, `EXPECTATIVAS_DE_CAIDA` declara ARRIBA —antes de mirar nada— qué debe
        verse tras el corte y qué tras reiniciar. Una prueba de recuperación que aceptase
        las dos ramas no distinguiría un runtime correcto de uno que publica basura.
        """
        self.assertEqual(sorted(EXPECTATIVAS_DE_CAIDA), sorted(PUNTOS_DEL_CONTRATO))
        for punto in PUNTOS_DEL_CONTRATO:
            with self.subTest(punto=punto):
                self._un_punto(punto, EXPECTATIVAS_DE_CAIDA[punto])

    def _un_punto(self, punto, expectativa):
        # Cada punto estrena control repo y espacio de adaptador: un residuo de otro punto
        # convertiría el recuento de ejecuciones en una suma de dos historias.
        self.setUp()
        self.alta([{"id": "pq-0001", "argumentos": [expectativa["comportamiento"]]}])

        caida = self.cli(["despachar", "pq-0001"], fallo=punto)
        self.assertEqual(
            caida.returncode, CODIGO_SALIDA_CAIDA,
            f"{punto}: el proceso salió con {caida.returncode} en vez de morir\n"
            f"{caida.stdout}{caida.stderr}")
        self.assertIn("ADS_RUNTIME_FALLO: corte inyectado en " + punto, caida.stderr)
        self.assertEqual(self._estado_observado(), expectativa["tras_la_caida"],
                         punto + ": el estado tras la caída no es el declarado")

        self.exito(self.cli(["ciclo"]), punto + ": reinicio")
        objeto = self.paquete("pq-0001")
        observado = (objeto["estado"], objeto["intentos"], len(self.invocaciones()),
                     len(self.ejecuciones()), len(self.pendencias()))
        self.assertEqual(observado, expectativa["tras_reiniciar"],
                         punto + ": la recuperación no es la declarada")

    def test_81_caer_entre_el_efecto_y_el_acuse_no_aplica_el_efecto_dos_veces(self):
        """T186 · Defecto que previene: aplicar dos veces un efecto ya aplicado.

        Es el caso del §4.5, escrito por separado porque es el que sostiene la propiedad 3
        del corte. La expectativa, ANTES de mirar:

          tras el corte    el efecto está aplicado —una línea en la bitácora del
                           adaptador— y NO hay acuse durable: el runtime no puede saber que
                           se aplicó. El paquete sigue `ejecutando`.
          tras reiniciar   el runtime VUELVE A INVOCAR al adaptador con el MISMO `efecto`
                           —dos invocaciones—, el recibo del adaptador corta la segunda
                           aplicación —UNA sola ejecución— y el acuse queda escrito en la
                           misma transición que el resultado.

        Y una comprobación que sólo tiene sentido aquí: el acuse y el resultado del paquete
        se publican en la MISMA revisión. Si se vieran por separado, existiría un instante
        con el efecto aplicado y el paquete sin cerrar, que es el agujero que se está
        tapando.
        """
        self.alta([{"id": "pq-0001"}])
        caida = self.cli(["despachar", "pq-0001"],
                         fallo="despues-del-efecto-antes-del-acuse")
        self.assertEqual(caida.returncode, CODIGO_SALIDA_CAIDA)

        objeto = self.paquete("pq-0001")
        efecto = objeto["efecto"]
        self.assertEqual(objeto["estado"], "ejecutando")
        self.assertIsNone(self.canonico("efectos", efecto), "el acuse no debía existir")
        self.assertEqual(self.ejecuciones(), [efecto + " exito"])
        self.assertEqual(len(self.invocaciones()), 1)

        self.exito(self.cli(["ciclo"]), "reinicio")
        final = self.paquete("pq-0001")
        self.assertEqual(final["estado"], "completado")
        self.assertEqual(final["efecto"], efecto, "el efecto cambió al reanudar")
        self.assertEqual(len(self.invocaciones()), 2, "no se reintentó la entrega")
        self.assertEqual(self.ejecuciones(), [efecto + " exito"],
                         "EL EFECTO SE APLICÓ DOS VECES")
        acuse = self.canonico("efectos", efecto)
        self.assertTrue(acuse["aplicado"])
        self.assertTrue(final["resultado"]["repetido"],
                        "el adaptador no declaró la segunda entrega como repetida")

        # Acuse y resultado en la MISMA revisión: la `raiz` publicada los nombra a los dos.
        revision = json_de(os.path.join(self.repo, "estado", "REVISION.json"))
        self.assertIn("efectos/" + efecto + ".json", revision["raiz"])
        self.assertIn("paquetes/pq-0001.json", revision["raiz"])
        eventos = [json.loads(linea) for linea in lineas_de(
            os.path.join(self.repo, "estado", "diario", "DIARIO.jsonl"))]
        acusadoras = [e for e in eventos
                      if e["tipo"] == "transicion.confirmada"
                      and e.get("clase") == "runtime.efecto.acusado"]
        self.assertEqual(len(acusadoras), 1)
        rutas = {operacion["ruta"] for operacion in acusadoras[0]["operaciones"]}
        self.assertEqual(rutas, {"paquetes/pq-0001.json", "efectos/" + efecto + ".json",
                                 "leases/pq-0001.json"})

    def test_82_un_paquete_ya_completado_no_se_vuelve_a_despachar(self):
        """T186 · Defecto que previene: repetir el trabajo de un paquete ya cerrado.

        Despachar dos veces seguidas. La segunda tiene que dar `ESTADO_DE_PAQUETE_INVALIDO`
        —la tabla del §4.2 no lleva de `completado` a ninguna parte— y el adaptador no puede
        haber sido invocado una segunda vez.
        """
        self.alta([{"id": "pq-0001"}])
        self.exito(self.cli(["despachar", "pq-0001"]), "primer despacho")
        self.assertEqual(len(self.invocaciones()), 1)

        repetido = self.cli(["despachar", "pq-0001"])
        self.assertEqual(repetido.returncode, 1)
        self.assertEqual(codigo_de_error(repetido), "ESTADO_DE_PAQUETE_INVALIDO")
        self.assertEqual(len(self.invocaciones()), 1, "se volvió a invocar al adaptador")
        self.assertEqual(len(self.ejecuciones()), 1)
        self.assertEqual(len(self.efectos()), 1)

    def test_83_un_efecto_ya_acusado_se_rechaza_con_su_senal(self):
        """T186 · Defecto que previene: tratar la idempotencia como si fuera un fallo mudo.

        `EfectoYaAplicado` es una SEÑAL, y el §4.1 la pone en la jerarquía para que quien
        EXIJA la ausencia de acuse obtenga un error tipado y no un silencio. El camino
        normal del dispatcher no la usa —comprueba el acuse y no ejecuta—, y por eso se
        ejerce aquí de forma explícita.
        """
        self.alta([{"id": "pq-0001"}])
        self.exito(self.cli(["despachar", "pq-0001"]), "despachar")
        efecto = self.paquete("pq-0001")["efecto"]
        acuse = self.canonico("efectos", efecto)
        self.assertIsNone(paquete_runtime.exigir_efecto_no_aplicado(None, efecto))
        with self.assertRaises(paquete_runtime.EfectoYaAplicado) as capturado:
            paquete_runtime.exigir_efecto_no_aplicado(acuse, efecto)
        self.assertEqual(capturado.exception.codigo, "EFECTO_YA_APLICADO")

    def test_84_un_estado_que_ninguna_regla_explica_es_fallo_cerrado(self):
        """T186 · Defecto que previene: inventar estado cuando el estado no casa (`b.14.3`).

        Tres formas de romper el estado desde fuera, con el motor como escritor para que
        todo siga siendo íntegro: una palabra que no está en el vocabulario cerrado, un
        `intentos` mayor que su tope, y un acuse durable sobre un paquete que sigue
        `ejecutando` —imposible, porque acuse y resultado viajan en la misma transición—.
        Las tres tienen que dar `RUNTIME_INCONSISTENTE`, no una interpretación amable.
        """
        self.alta([{"id": "pq-0001"}])
        base = self.paquete("pq-0001")
        carga = os.path.join(self.base, "carga.json")

        for numero, mutacion in enumerate((
            {"estado": "en-marcha"},
            {"intentos": 9},
            {"estado": "ejecutando", "efecto": "ef-000000000000"},
        ), start=1):
            objeto = dict(base)
            objeto.update(mutacion)
            escribir(carga, json.dumps(objeto, sort_keys=True, ensure_ascii=False))
            self.exito(self.cli_estado([
                "transicion", "--id", "tx-mutar-" + str(numero), "--autor", "prueba",
                "--motivo", "romper el estado a propósito",
                "--escribir", "paquetes/pq-0001.json=" + carga]), "mutar " + str(numero))
            if numero == 3:
                # El acuse se escribe aparte, y por eso su sola presencia con el paquete en
                # `ejecutando` describe un estado que el protocolo no puede producir.
                escribir(carga, json.dumps({
                    "esquema": "ads.estado/1", "efecto": "ef-000000000000",
                    "paquete": "pq-0001", "intento": 1,
                    "resultado_cid": "sha256:" + "0" * 64, "aplicado": True,
                }, sort_keys=True))
                self.exito(self.cli_estado([
                    "transicion", "--id", "tx-acuse-falso", "--autor", "prueba",
                    "--motivo", "un acuse imposible",
                    "--escribir", "efectos/ef-000000000000.json=" + carga]), "acuse")
            proceso = self.cli(["despachar", "pq-0001"])
            self.assertEqual(proceso.returncode, 1, "mutación " + str(numero))
            self.assertEqual(codigo_de_error(proceso), "RUNTIME_INCONSISTENTE",
                             "mutación " + str(numero) + ":\n" + proceso.stderr)

    def test_85_el_censo_de_puntos_es_el_del_contrato_y_todos_se_llaman(self):
        """T186 · Defecto que previene: dar por inyectada una caída que nunca se inyectó.

        Dos mitades, y las dos importan:

          · EL CENSO. `fallos.puntos()` se EJECUTA —no se lee el fichero— y se confronta con
            los nueve del §4.2; y se comprueba, DERIVÁNDOLO del árbol sintáctico del
            paquete, que cada punto declarado tiene al menos una llamada `fallos.punto(...)`
            con ese literal. Un punto declarado y no llamado es una caída que nadie podrá
            provocar nunca.

          · LA ERRATA. Un `ADS_RUNTIME_FALLO` con el nombre a medias tiene que FALLAR
            RUIDOSAMENTE. Si se ignorase en silencio, escribir `antes-del-acuse` en vez de
            `despues-del-efecto-antes-del-acuse` daría una prueba en verde que no inyectó
            nada, y estaríamos publicando como evidencia de idempotencia una ejecución en la
            que nunca hubo corte. La expectativa es explícita: código de salida 1 —no 70 y
            no 0—, código tipado `PUNTO_DE_FALLO_DESCONOCIDO`, el punto pedido nombrado en
            la salida, y el estado sin tocar.
        """
        self.assertEqual(sorted(fallos.puntos()), sorted(PUNTOS_DEL_CONTRATO))

        llamados = set()
        for nombre in sorted(os.listdir(PAQUETE)):
            if not nombre.endswith(".py") or nombre == "fallos.py":
                continue
            arbol = ast.parse(texto_de(os.path.join(PAQUETE, nombre)), filename=nombre)
            for nodo in ast.walk(arbol):
                if not isinstance(nodo, ast.Call):
                    continue
                destino = nodo.func
                if not (isinstance(destino, ast.Attribute) and destino.attr == "punto"):
                    continue
                if nodo.args and isinstance(nodo.args[0], ast.Constant) \
                        and isinstance(nodo.args[0].value, str):
                    llamados.add(nodo.args[0].value)
        self.assertEqual(sorted(llamados), sorted(PUNTOS_DEL_CONTRATO),
                         "hay puntos declarados que nadie llama, o llamadas a puntos que "
                         "no están declarados")

        self.alta([{"id": "pq-0001"}])
        revision_antes = self.revision()
        errata = "antes-del-acuse"
        self.assertNotIn(errata, fallos.puntos())
        proceso = self.cli(["despachar", "pq-0001"], fallo=errata)
        self.assertEqual(proceso.returncode, 1,
                         f"un punto inexistente salió con {proceso.returncode}: ni cortó "
                         f"(70) ni avisó (1), luego se ignoró en silencio")
        self.assertEqual(codigo_de_error(proceso), "PUNTO_DE_FALLO_DESCONOCIDO")
        self.assertIn(errata, proceso.stdout + proceso.stderr,
                      "el error no nombra el punto que se pidió")
        self.assertEqual(self.revision(), revision_antes)
        self.assertEqual(self.invocaciones(), [])

    def test_86_el_efecto_se_deriva_del_contenido_y_cambia_con_el_intento(self):
        """T186 · Defecto que previene: un acuse que bloquearía todos los reintentos.

        El §3 fija `efecto = "ef-" + cid(orden + paquete + intento)[:12]`. Que el INTENTO
        entre es lo que permite que la política de reintentos funcione: sin él, el acuse del
        primer intento fallido impediría para siempre el segundo. Y que sea función pura del
        contenido es lo que hace que el acuse de una instancia valga para otra.
        """
        orden = {"adaptador": "proceso-local", "operacion": "ejecutar",
                 "argumentos": ["exito"], "limite_segundos": 30}
        primero = modelo.derivar_efecto(orden, "pq-0001", 1)
        segundo = modelo.derivar_efecto(orden, "pq-0001", 2)
        otro = modelo.derivar_efecto(orden, "pq-0002", 1)
        self.assertNotEqual(primero, segundo)
        self.assertNotEqual(primero, otro)
        self.assertEqual(primero, modelo.derivar_efecto(dict(orden), "pq-0001", 1))
        self.assertTrue(primero.startswith("ef-"))
        self.assertEqual(len(primero), 3 + 12)
        # Escribible como objeto canónico: si llevase `:` no habría acuse posible.
        self.assertEqual(modelo.ruta_efecto(primero), "efectos/" + primero + ".json")

    def test_87_abrir_recupera_antes_de_despachar(self):
        """T186 · Defecto que previene: despachar sobre una ventana sin cerrar.

        `abrir()` llama a `recuperar()` ANTES de nada, y el informe queda a la vista. Se
        provoca una caída del MOTOR en su punto de no retorno —`ADS_ESTADO_FALLO`, que es
        del motor y no del runtime— y se comprueba que el runtime, al abrir, cierra la
        ventana por la rama COMPLETAR y sigue trabajando sobre un estado íntegro.
        """
        self.alta([{"id": "pq-0001"}])
        carga = os.path.join(self.base, "carga.json")
        escribir(carga, json.dumps({"esquema": "ads.estado/1", "id": "it-0002",
                                    "titulo": "otro", "estado": "abierto"},
                                   sort_keys=True))
        entorno = dict(ENTORNO)
        entorno["ADS_ESTADO_FALLO"] = "despues-del-commit-atomico"
        corte = subprocess.run(
            [sys.executable, CLI_ESTADO, "--repo", self.repo, "transicion",
             "--id", "tx-corte", "--autor", "prueba", "--motivo", "cortar a propósito",
             "--escribir", "items/it-0002.json=" + carga],
            capture_output=True, text=True, env=entorno, timeout=SEGUNDOS_DE_ESPERA,
            cwd=tempfile.gettempdir())
        self.assertEqual(corte.returncode, CODIGO_SALIDA_CAIDA)

        with paquete_runtime.Runtime(self.repo, instancia="runtime-A") as rt:
            self.assertEqual(rt.recuperacion["ventana_previa"], "preparada")
            self.assertEqual(rt.recuperacion["rama"], "completar")
            self.assertFalse(rt.marcado)
        self.exito(self.cli(["ciclo"]), "ciclo tras recuperar")
        self.assertEqual(self.paquete("pq-0001")["estado"], "completado")
        self.assertEqual(self.canonico("items", "it-0002")["titulo"], "otro")


# ===================================================================================
# unidad — piezas que no necesitan un almacén, y que por eso se prueban aparte
# ===================================================================================
class Piezas(unittest.TestCase):

    def test_90_los_codigos_de_error_son_estables_y_salen_en_el_texto(self):
        """T182 · Defecto que previene: una evidencia que depende del texto castellano.

        El contrato de la salida es el CÓDIGO, no el detalle. Se comprueba que los
        dieciséis del §4.1 —los quince originales más `EJECUCION_AMBIGUA`— están, que
        cada `str(error)` lleva el suyo entre corchetes y que `a_dict()` es determinista.
        """
        esperados = {
            "ERROR_DE_RUNTIME", "AUTORIDAD_NO_DISPONIBLE", "AUTORIDAD_PERDIDA",
            "RECLAMACION_PREMATURA", "PAQUETE_DESCONOCIDO", "ESTADO_DE_PAQUETE_INVALIDO",
            "DEPENDENCIA_NO_RESUELTA", "CAPACIDAD_NO_SOPORTADA", "ADAPTADOR_INCOMPATIBLE",
            "EJECUCION_FALLIDA", "EJECUCION_DEFINITIVA", "EJECUCION_CANCELADA",
            "TIEMPO_AGOTADO", "EFECTO_YA_APLICADO", "RUNTIME_INCONSISTENTE",
            "EJECUCION_AMBIGUA",
        }
        from runtime import errores as errores_runtime
        self.assertEqual(set(errores_runtime.CODIGOS), esperados)
        for clase in errores_runtime.CLASES:
            error = clase("un detalle", ruta="paquetes/pq-1.json", extra=1)
            self.assertIn("[" + clase.CODIGO + "]", str(error))
            self.assertEqual(error.a_dict()["codigo"], clase.CODIGO)
            self.assertEqual(error.a_dict()["contexto"], {"extra": 1})

    def test_91_ninguna_salida_de_error_publica_una_ruta_absoluta(self):
        """T182 · Defecto que previene: publicar el árbol de directorios de quien ejecuta.

        La evidencia de `F6` se publica y se compara byte a byte. Una ruta absoluta la hace
        dependiente de la máquina y del usuario, y de paso filtra el entorno. El saneador es
        el del motor, reutilizado en el constructor del error: cubre también el módulo que
        alguien escriba mañana.
        """
        from runtime import errores as errores_runtime
        absoluta = "/home/quien-sea/proyecto/estado/canonico/paquetes/pq-1.json"
        error = errores_runtime.AutoridadPerdida("detalle", ruta=absoluta)
        self.assertEqual(error.ruta, "estado/canonico/paquetes/pq-1.json")
        self.assertNotIn("/home/", str(error))
        fuera = errores_runtime.RuntimeInconsistente("detalle", ruta="/var/tmp/algo.vivo")
        self.assertEqual(fuera.ruta, "algo.vivo")

    def test_92_la_politica_clasifica_y_decide_sin_tocar_nada(self):
        """T184 · Defecto que previene: una decisión de reintento que depende del estado.

        `politica` son funciones puras sobre el paquete leído y el resultado del adaptador.
        Se recorren las cuatro clases y las dos situaciones de tope, y se comprueba que un
        resultado con forma ajena al §4.4 —estado inventado, efecto que no casa— es fallo
        cerrado y no una clasificación amable.
        """
        base = {"estado": "fallido", "codigo": 1, "salida": "", "detalle": "",
                "reintentable": True, "efecto": "ef-1", "repetido": False}
        politica.comprobar_resultado(dict(base), efecto="ef-1", paquete="pq-1")
        for mutacion in ({"estado": "inventado"}, {"efecto": "ef-otro"},
                         {"reintentable": "si"}):
            roto = dict(base)
            roto.update(mutacion)
            with self.assertRaises(paquete_runtime.RuntimeInconsistente):
                politica.comprobar_resultado(roto, efecto="ef-1", paquete="pq-1")
        with self.assertRaises(paquete_runtime.RuntimeInconsistente):
            politica.comprobar_resultado({"estado": "fallido"}, efecto="ef-1",
                                         paquete="pq-1")

        clase, error = politica.clasificar(dict(base))
        self.assertEqual(clase, politica.CLASE_REINTENTABLE)
        self.assertEqual(error.codigo, "EJECUCION_FALLIDA")
        con_intentos = {"intentos": 1, "max_intentos": 3}
        agotado = {"intentos": 3, "max_intentos": 3}
        self.assertEqual(politica.decidir(clase, con_intentos), "reintentar")
        self.assertEqual(politica.decidir(clase, agotado), "agotar")
        self.assertEqual(politica.decidir(politica.CLASE_DEFINITIVO, con_intentos),
                         "agotar")
        self.assertEqual(politica.decidir(politica.CLASE_CANCELACION, con_intentos),
                         "cerrar")
        self.assertEqual(politica.decidir(politica.CLASE_COMPLETADO, con_intentos),
                         "cerrar")

    def test_93_la_observacion_reinicia_su_cuenta_si_el_latido_avanzo(self):
        """T183 · Defecto que previene: contar observaciones que no fueron consecutivas.

        La consecutividad NO puede depender de que el titular limpie `observado_por`: el
        titular que se está midiendo es precisamente el que se presume muerto. El aspirante
        anota el latido VISTO y reinicia su cuenta él mismo cuando el latido avanza.
        """
        lease = modulo_lease.nuevo_lease(paquete="pq-1", titular="runtime-A",
                                         revision_adquirida="sha256:" + "0" * 64)
        for esperado in (1, 2, 3):
            lease = modulo_lease.con_observacion(lease, "runtime-B")
            self.assertEqual(
                lease["observado_por"]["runtime-B"]["observaciones"], esperado)
            self.assertEqual(modulo_lease.observaciones_de(lease, "runtime-B"), esperado)

        # El titular late SIN limpiar las observaciones: aun así la racha se rompe.
        avanzado = dict(lease)
        avanzado["latido"] = lease["latido"] + 1
        self.assertEqual(modulo_lease.observaciones_de(avanzado, "runtime-B"), 0)
        avanzado = modulo_lease.con_observacion(avanzado, "runtime-B")
        self.assertEqual(modulo_lease.observaciones_de(avanzado, "runtime-B"), 1)

        # El titular no se observa a sí mismo: para eso está `renovar`.
        with self.assertRaises(paquete_runtime.RuntimeInconsistente):
            modulo_lease.con_observacion(lease, "runtime-A")

        # Y `con_latido` sí limpia, que es la otra mitad de la garantía.
        self.assertEqual(modulo_lease.con_latido(lease)["observado_por"], {})

    def test_94_un_lease_o_un_paquete_mal_formados_son_fallo_cerrado(self):
        """T182 · Defecto que previene: rellenar lo que falta en vez de denunciarlo.

        `comprobar_paquete` y `comprobar_lease` no ponen valores por defecto: un objeto al
        que le falta un campo del §3, o cuyo `estado` no está en el vocabulario cerrado, no
        es «un objeto raro», es uno que ninguna regla sabe interpretar.
        """
        orden = {"adaptador": "a", "operacion": "ejecutar", "argumentos": [],
                 "limite_segundos": 1}
        sano = modelo.nuevo_paquete(identificador="pq-1", item="it-1",
                                    capacidades_requeridas=["c"], orden=orden)
        modelo.comprobar_paquete(dict(sano), "paquetes/pq-1.json")
        for mutacion in ({"estado": "inventado"}, {"intentos": -1},
                         {"max_intentos": 0}, {"depende_de": "pq-2"},
                         {"capacidades_requeridas": "c"},
                         {"estado": "ejecutando", "efecto": None}):
            roto = dict(sano)
            roto.update(mutacion)
            with self.assertRaises(paquete_runtime.RuntimeInconsistente, msg=str(mutacion)):
                modelo.comprobar_paquete(roto, "paquetes/pq-1.json")
        for clave in modelo.CLAVES_DE_PAQUETE:
            roto = {k: v for k, v in sano.items() if k != clave}
            with self.assertRaises(paquete_runtime.RuntimeInconsistente, msg=clave):
                modelo.comprobar_paquete(roto, "paquetes/pq-1.json")

        for mutacion in ({"orden": {"adaptador": "a"}},
                         {"orden": dict(orden, limite_segundos=0)},
                         {"orden": dict(orden, sobra=1)}):
            roto = dict(sano)
            roto.update(mutacion)
            with self.assertRaises(paquete_runtime.RuntimeInconsistente, msg=str(mutacion)):
                modelo.comprobar_paquete(roto, "paquetes/pq-1.json")

        lease = modulo_lease.nuevo_lease(paquete="pq-1", titular="runtime-A",
                                         revision_adquirida="sha256:" + "0" * 64)
        modulo_lease.comprobar_lease(dict(lease), "leases/pq-1.json")
        for mutacion in ({"titular": ""}, {"epoca": 0}, {"latido": -1},
                         {"observado_por": []}, {"observado_por": {"x": 2}}):
            roto = dict(lease)
            roto.update(mutacion)
            with self.assertRaises(paquete_runtime.RuntimeInconsistente, msg=str(mutacion)):
                modulo_lease.comprobar_lease(roto, "leases/pq-1.json")

    def test_95_la_cli_distingue_uso_incorrecto_de_fallo_de_la_operacion(self):
        """T182 · Defecto que previene: confundir un tecleo con un fallo del estado.

        0 éxito · 1 error tipado · 2 uso incorrecto. Y `--repo`/`--instancia`/`--json` se
        aceptan ANTES y DESPUÉS de la orden, como en `ads_estado.py`: una CLI que sólo
        admite una posición convierte un tecleo en un error de uso.
        """
        import importlib
        modulo = importlib.import_module("ads_runtime")
        self.assertEqual(modulo.main(["elegibles"]), modulo.USO)
        self.assertEqual(modulo.main(["--repo", "/no/importa", "elegibles"]), modulo.USO)
        analizador = modulo.construir_analizador()
        delante = analizador.parse_args(["--repo", "r", "--instancia", "i", "--json",
                                         "elegibles"])
        detras = analizador.parse_args(["elegibles", "--repo", "r", "--instancia", "i",
                                        "--json"])
        self.assertEqual((delante.repo, delante.instancia, delante.json),
                         (detras.repo, detras.instancia, detras.json))
        self.assertEqual(sorted(modulo.ORDENES), sorted([
            "adquirir", "cancelar", "ciclo", "crear-item", "crear-paquete", "despachar",
            "elegibles", "estado-paquete", "liberar", "observar", "pausar", "reanudar",
            "reclamar", "renovar", "vistas",
        ]))


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de `tooling/tests/test_workspace.py`, no importado: la batería del runtime no
    puede depender de un módulo de `tooling/` para poder ejecutarse. La salida de estas
    pruebas se PUBLICA como evidencia, y la regla del repositorio es que los artefactos
    generados sean deterministas: «Ran 40 tests in 12.481s» cambia en cada ejecución y
    ensuciaría el árbol en cada comprobación, hasta que alguien dejara de mirarlo.
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
