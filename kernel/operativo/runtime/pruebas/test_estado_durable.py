#!/usr/bin/env python3
"""test_estado_durable — la batería del MOTOR DE ESTADO DURABLE (`F6`, corte vertical 1).

Instancia el §12.2 del CONTRATO DEL CORTE, que a su vez instancia la sección `(g)` de la
especificación aprobada. La batería NO comprueba que el motor «funcione»: comprueba que NO
hace lo que la norma le prohíbe hacer, que es donde estas cosas se rompen.

TRES REGLAS QUE ESTA BATERÍA SE IMPONE, Y POR QUÉ:

  1. NINGUNA PRUEBA SE LIMITA A MIRAR. No hay ni un caso que compruebe que un fichero
     existe o que un texto dice algo y se dé por satisfecho: todos ejecutan el motor. Una
     batería que lee el árbol en vez de moverlo demuestra que alguien escribió los
     ficheros, no que el estado durable sea durable.

  2. LAS CAÍDAS SON CAÍDAS DE VERDAD. Los nueve puntos de `estado/fallos.py` se ejercitan
     con `subprocess` y `ADS_ESTADO_FALLO`, y el proceso muere por `os._exit(70)`: sin
     `finally`, sin cerrar ficheros, sin vaciar buffers. Un `mock` que simula una caída
     simula también, sin querer, un cierre ordenado, y ese cierre ordenado es justo lo que
     no ocurre cuando se va la luz.

  3. CADA CAÍDA DECLARA SU EXPECTATIVA ANTES DE MIRAR EL RESULTADO. Para cada punto de
     fallo está escrito, en el propio caso, qué DEBE haber pasado tras reiniciar:
     «transición perdida y no publicada» o «transición completada». Nunca «lo que salga».
     Una prueba de recuperación que acepta las dos ramas no distingue un motor correcto de
     uno que publica basura.

Y una cuarta, de forma: la salida se PUBLICA como evidencia, así que el resumen de
`unittest` no lleva duración (`_RunnerDeterminista`, copiado de `tooling/tests/`).

    python3 kernel/operativo/runtime/pruebas/test_estado_durable.py

Sale con 0 si todo pasa. Se ejecuta desde cualquier directorio: la raíz se deriva de
`__file__` y NUNCA del `cwd`, que es la lección que este repositorio ya aprendió a base de
pruebas que sólo pasaban desde la raíz.
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
import time
import unittest

# --- localización del paquete ------------------------------------------------------
# `kernel/` no es un paquete Python. El patrón del repositorio es insertar el directorio
# del runtime en `sys.path`. La raíz se DERIVA de `__file__`: este fichero vive en
# <raiz>/kernel/operativo/runtime/pruebas/, luego la raíz está cuatro niveles arriba.
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
RUNTIME = os.path.join(RAIZ, "kernel", "operativo", "runtime")
CLI = os.path.join(RUNTIME, "ads_estado.py")
sys.path.insert(0, RUNTIME)

try:
    import estado
    from estado import atestacion, diario as diario_mod, errores, fallos
except ImportError as exc:  # el motor todavía no está: que se vea por qué
    print(f"no se encuentra el paquete `estado` bajo {RUNTIME}: {exc}", file=sys.stderr)
    raise

# El entorno de las pruebas NO hereda `ADS_ESTADO_FALLO`. Si alguien lo tuviera puesto en
# su terminal, la mitad de esta batería moriría por una causa que no es la que se está
# probando, y el informe culparía al motor.
ENTORNO = {k: v for k, v in os.environ.items() if k != "ADS_ESTADO_FALLO"}

# Los DIEZ puntos de corte del protocolo, escritos aquí SÓLO para poder comprobar que el
# censo que el motor declara coincide con el que la norma exige. El motor los deriva; esta
# lista existe para confrontarlos, no para sustituirlos.
#
# `entre-el-paso-8-y-el-9` es el décimo y se añade con `E-08`: los nueve anteriores no
# permitían cortar en el único sitio donde la inversión de los pasos 8 y 9 se distingue de
# su orden correcto —objetos publicados y testigo escrito, revisión todavía no—.
PUNTOS_DEL_CONTRATO = [
    "antes-de-escribir-temporal",
    "despues-de-escribir-temporal",
    "despues-de-sincronizar-temporal",
    "antes-del-commit-atomico",
    "despues-del-commit-atomico",
    "antes-de-sincronizar-directorio",
    "entre-el-paso-8-y-el-9",
    "durante-el-diario",
    "durante-el-registro-auxiliar",
    "antes-de-devolver-exito",
]

CODIGO_SALIDA_CAIDA = 70          # `os._exit(70)` del §10
SEGUNDOS_DE_ESPERA = 120          # techo de cada subproceso; ninguna prueba debe colgarse


# ===================================================================================
# utilidades — todas ejecutan cosas, ninguna «comprueba» por su cuenta
# ===================================================================================

def escribir_json(ruta, datos):
    """Escribe el fichero de carga útil que la orden `transicion` del CLI consume."""
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as fh:
        json.dump(datos, fh, ensure_ascii=False, sort_keys=True, indent=2)
        fh.write("\n")


def cli(repo, argumentos, *, fallo=None, cwd=None, espera=SEGUNDOS_DE_ESPERA):
    """Ejecuta el CLI en un PROCESO REAL.

    `cwd` por defecto es el temporal del sistema, no la raíz del repositorio: así cada
    invocación demuestra, de paso, que el motor no depende del directorio actual.
    """
    entorno = dict(ENTORNO)
    if fallo:
        entorno["ADS_ESTADO_FALLO"] = fallo
    return subprocess.run(
        [sys.executable, CLI, "--repo", repo] + [str(a) for a in argumentos],
        capture_output=True, text=True, env=entorno, timeout=espera,
        cwd=cwd or tempfile.gettempdir())


# Lecturas que CIERRAN. Un `open(...).read()` suelto deja el descriptor a merced del
# recolector y CPython avisa con un `ResourceWarning` que lleva dentro la ruta del
# temporal: una ruta absoluta y aleatoria en una salida que tiene que ser determinista.
def texto_de(ruta, **kw):
    with open(ruta, encoding="utf-8", **kw) as fh:
        return fh.read()


def bytes_de(ruta):
    with open(ruta, "rb") as fh:
        return fh.read()


def lineas_json(ruta):
    """Los eventos de un JSONL, ya decodificados. Es la lectura más repetida de aquí."""
    return [json.loads(linea) for linea in texto_de(ruta).splitlines() if linea.strip()]


def codigo_de_error(proceso):
    """El código tipado que el §11 obliga a imprimir en `stderr`. Vacío si no lo imprime."""
    hallados = re.findall(r"\b[A-Z][A-Z0-9_]{5,}\b", proceso.stderr or "")
    return hallados[0] if hallados else ""


# Las claves DURABLES de `REVISION.json`: exactamente las que enumera el §2.3.
#
# POR QUÉ EXISTE ESTA PROYECCIÓN. La revisión se puede obtener por dos accesos distintos
# —`revision --json` del CLI y `Almacen.revision()` de la API— y cada uno puede añadir
# campos informativos propios: el CLI añade `ventana`, que es una lectura del momento y no
# forma parte de la revisión publicada. Comparar los dos diccionarios en crudo es comparar
# peras con manzanas, y una prueba que lo haga falla por la forma del acceso en vez de por
# el estado, que es justo lo que una prueba no debe hacer. Se comparan las claves durables,
# que son las que el §2.3 fija y las únicas cuya igualdad significa «el estado no se movió».
CLAVES_DURABLES_DE_REVISION = ("esquema", "revision", "revision_id", "padre", "cid_raiz",
                               "raiz", "diario_secuencia", "transaccion")


def solo_durables(revision):
    """La parte durable de una revisión, venga del CLI o de la API."""
    return {clave: revision[clave] for clave in CLAVES_DURABLES_DE_REVISION
            if clave in revision}


class Caso(unittest.TestCase):
    """Base: un control repo temporal por caso, borrado al terminar."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ads-estado-")
        self.repo = os.path.join(self.tmp, "control")
        os.makedirs(self.repo)
        self.cargas = os.path.join(self.tmp, "cargas")
        os.makedirs(self.cargas)
        self.addCleanup(self._limpiar)

    def _limpiar(self):
        # Los casos de PERMISOS dejan directorios sin permiso de escritura; sin esto, el
        # borrado del temporal fallaría y ensuciaría la máquina de quien ejecute.
        for base, dirs, _f in os.walk(self.tmp):
            for d in dirs:
                try:
                    os.chmod(os.path.join(base, d), 0o755)
                except OSError:
                    pass
        shutil.rmtree(self.tmp, ignore_errors=True)

    # -- construcción ---------------------------------------------------------------
    def inicializar(self):
        proceso = cli(self.repo, ["inicializar", "--json"])
        self.assertEqual(proceso.returncode, 0,
                         f"`inicializar` falló: {proceso.stderr or proceso.stdout}")
        return proceso

    def revision(self):
        proceso = cli(self.repo, ["revision", "--json"])
        self.assertEqual(proceso.returncode, 0,
                         f"`revision` falló: {proceso.stderr or proceso.stdout}")
        return json.loads(proceso.stdout)

    def transicion(self, ident, ruta, datos, *, base=None, fallo=None,
                   autor="agente-b", motivo="prueba de la batería"):
        """Una transición de una sola escritura, ejecutada por el CLI en otro proceso."""
        carga = os.path.join(self.cargas, ident + ".json")
        escribir_json(carga, datos)
        if base is None:
            base = self.revision()["revision_id"]
        return cli(self.repo, ["transicion", "--id", ident, "--autor", autor,
                               "--motivo", motivo, "--base", base,
                               "--escribir", f"{ruta}={carga}"], fallo=fallo)

    def transicion_ok(self, ident, ruta, datos, **kw):
        proceso = self.transicion(ident, ruta, datos, **kw)
        self.assertEqual(proceso.returncode, 0,
                         f"la transición '{ident}' debía confirmarse y no lo hizo: "
                         f"{proceso.stderr or proceso.stdout}")
        return proceso

    # -- inspección del árbol, siempre a través del motor ---------------------------
    def almacen(self, *, recuperar=True):
        return estado.abrir(self.repo, recuperar=recuperar)

    def tipos_del_diario(self):
        with self.almacen(recuperar=False) as alm:
            return [ev["tipo"] for ev in alm.diario()]

    def ruta_estado(self, *partes):
        return os.path.join(self.repo, "estado", *partes)

    # -- aserciones con nombre ------------------------------------------------------
    def assertFalloCerrado(self, tipo, invocable, *args, **kw):
        """El §0 obliga a error TIPADO ante corrupción, y a no tocar el estado canónico.

        Se exige la excepción, no un informe con `ok=False`: un informe se puede ignorar
        por descuido; una excepción, no. Es la diferencia entre fallar cerrado y avisar.
        """
        with self.assertRaises(tipo) as capturado:
            invocable(*args, **kw)
        error = capturado.exception
        self.assertTrue(getattr(error, "codigo", ""),
                        f"{tipo.__name__} sin `codigo`: el §8 lo exige estable")
        self.assertIn(error.codigo, str(error),
                      "`str(error)` debe incluir el código (§8)")
        return error


# ===================================================================================
# POSITIVOS · lo que el motor tiene que saber hacer
# ===================================================================================

class GuardaDeEntorno(unittest.TestCase):
    """`T172` — la guarda de entorno, ejecutada, no leída.

    Cierra `A14`. El defecto que previene ya ocurrió y está escrito en dos sitios del
    repositorio: bajo un intérprete insuficiente algunos validadores fallan por el ENTORNO,
    el runner —correctamente— no republica su evidencia, y la cobertura publicada queda
    describiendo un corpus anterior mientras el comprobador de evidencia sigue en verde. Un
    defecto de entorno subía a la capa de certificación disfrazado de defecto del producto.

    NO se comprueba leyendo el fichero de la guarda: se ejecuta, y se ejecutan además los
    dos que dependen de ella. Sobre una COPIA temporal cuando la orden publica evidencia,
    porque una prueba no puede tocar la evidencia del árbol real.
    """

    GUARDA = os.path.join(RAIZ, "kernel", "operativo", "validadores", "entorno.py")
    RUNNER = os.path.join("kernel", "operativo", "validadores", "registrar_evidencia.py")
    WORKSPACE = os.path.join("tooling", "workspace.py")
    INSUFICIENTE = "99.0"

    def _correr(self, orden, cwd, minima=None):
        entorno = dict(os.environ)
        if minima is None:
            entorno.pop("ADS_ENTORNO_VERSION_MINIMA", None)
        else:
            entorno["ADS_ENTORNO_VERSION_MINIMA"] = minima
        return subprocess.run([sys.executable] + orden, cwd=cwd, env=entorno,
                              capture_output=True, text=True)

    def test_72a_la_guarda_para_con_codigo_propio(self):
        """T172 · Un entorno insuficiente no se puede confundir con un producto roto."""
        p = self._correr([self.GUARDA], RAIZ, self.INSUFICIENTE)
        self.assertEqual(p.returncode, 78,
                         "el entorno insuficiente tiene que salir con un código PROPIO: 1 ya "
                         "significa «una comprobación no pasó» y 2 «uso incorrecto»")
        salida = p.stdout + p.stderr
        self.assertIn("ENTORNO INSUFICIENTE", salida)
        self.assertIn("78", salida, "el mensaje tiene que nombrar su propio código")
        self.assertIn("NO es un defecto del producto", salida)

    def test_72b_la_guarda_no_se_puede_relajar_por_entorno(self):
        """T172 · Una guarda que se puede bajar por variable es un interruptor."""
        p = self._correr([self.GUARDA], RAIZ, "3.8")
        self.assertEqual(p.returncode, 0,
                         "pedir MENOS de la mínima declarada no puede rebajar la exigencia")
        salida = p.stdout + p.stderr
        self.assertIn("no supera la mínima declarada", salida)
        self.assertIn("no se puede relajar por entorno", salida)

    def test_72c_el_runner_no_publica_nada_bajo_un_entorno_insuficiente(self):
        """T172 · Publicar a medias es peor que no publicar: aquí no se empieza."""
        tmp = tempfile.mkdtemp(prefix="ads-guarda-")
        self.addCleanup(shutil.rmtree, tmp, True)
        copia = os.path.join(tmp, "arbol")
        # Se excluyen la caché del intérprete y TODO directorio de herramienta —los que
        # empiezan por punto—, sin nombrar ninguno: el corpus es neutral de proveedor, y una
        # marca comercial escrita en un fichero del kernel es un defecto de conformidad que
        # `T92` detecta. Además, así no hay que volver aquí cada vez que aparezca una
        # herramienta nueva que planta su directorio en la raíz.
        def _ignorar(directorio, nombres):
            return [n for n in nombres
                    if n == "__pycache__"
                    or (n.startswith(".") and os.path.isdir(os.path.join(directorio, n)))]

        shutil.copytree(RAIZ, copia, symlinks=True, ignore=_ignorar)
        evidencia = os.path.join(copia, "kernel", "operativo", "pruebas", "evidencia")

        def _huella_de_la_evidencia():
            # Se CIERRA cada fichero. Un `open(...).read()` suelto deja un ResourceWarning
            # con la RUTA ABSOLUTA del temporal dentro, y esa ruta cambia en cada ejecución:
            # la evidencia publicada dejaría de ser determinista y el árbol nunca quedaría
            # limpio tras regenerarla.
            resumen = {}
            for nombre in sorted(os.listdir(evidencia)):
                with open(os.path.join(evidencia, nombre), "rb") as fh:
                    resumen[nombre] = fh.read()
            return resumen

        antes = _huella_de_la_evidencia()

        p = self._correr([self.RUNNER], copia, self.INSUFICIENTE)
        self.assertEqual(p.returncode, 78, p.stdout + p.stderr)
        self.assertIn("ENTORNO INSUFICIENTE", p.stdout + p.stderr)

        despues = _huella_de_la_evidencia()
        self.assertEqual(antes, despues,
                         "el runner ha tocado la evidencia bajo un entorno que no basta: es "
                         "exactamente cómo la cobertura publicada acaba describiendo un "
                         "corpus que ya no existe")

    def test_72d_el_workspace_para_antes_de_analizar_el_manifiesto(self):
        """T172 · Antes de correr, y no al fallar el primer `tomllib.load`."""
        p = self._correr([self.WORKSPACE, "check"], RAIZ, self.INSUFICIENTE)
        self.assertEqual(p.returncode, 78, p.stdout + p.stderr)
        self.assertIn("ENTORNO INSUFICIENTE", p.stdout + p.stderr)
        self.assertNotIn("SOURCES.toml", p.stdout,
                         "ha llegado a analizar el manifiesto: la guarda va ANTES")

    def test_72e_con_entorno_suficiente_la_guarda_no_estorba(self):
        """T172 · Una guarda que da falsos rojos se acaba desactivando."""
        p = self._correr([self.GUARDA], RAIZ)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn("entorno suficiente", p.stdout)
        datos = json.loads(self._correr([self.GUARDA, "--json"], RAIZ).stdout)
        self.assertTrue(datos["suficiente"])
        self.assertEqual(datos["codigo_si_insuficiente"], 78)
        self.assertTrue(datos["motivos"], "la guarda tiene que decir POR QUÉ exige lo que exige")


class Positivos(Caso):

    def test_01_inicializacion_deja_un_almacen_publicable(self):
        """T173 · Defecto que previene: un almacén recién creado que ya nace incoherente.

        La revisión 0 tiene que existir, tener `padre` nulo y estar explicada por un
        evento del diario. Un almacén sin revisión publicada obliga a adivinar la base de
        la primera transición, y adivinar la base es como se publican mezclas parciales.
        """
        self.inicializar()
        rev = self.revision()
        self.assertEqual(rev["esquema"], "ads.estado/1")
        self.assertEqual(rev["revision"], 0)
        self.assertIsNone(rev["padre"], "la revisión 0 no tiene padre (§2.3)")
        self.assertTrue(rev["revision_id"].startswith("sha256:"))
        self.assertTrue(rev["cid_raiz"].startswith("sha256:"))
        self.assertIn("almacen.inicializado", self.tipos_del_diario())

    def test_02_lo_operacional_queda_fuera_de_la_rama_canonica(self):
        """T174 · Defecto que previene: publicar estado PARCIAL en la rama canónica (`g.14`).

        `operacional/` es reconstruible y NO es estado durable. Si no queda excluido, un
        `git add -A` durante la ventana de una transacción sube la zona de preparación.
        Se comprueba ejecutando el motor y mirando lo que el motor dejó, no una plantilla.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "v": 1})
        ignorar = self.ruta_estado(".gitignore")
        self.assertTrue(os.path.isfile(ignorar), "falta estado/.gitignore (§2)")
        with open(ignorar, encoding="utf-8") as fh:
            self.assertIn("operacional", fh.read())

    def test_03_lectura_y_escritura(self):
        """T173 · Defecto que previene: un estado que sólo se puede leer reproyectando el diario.

        `I-g1` exige que el estado canónico se lea directamente. Se comprueba que `leer`
        devuelve lo escrito y que `listar` lo enumera.
        """
        self.inicializar()
        contenido = {"esquema": "ads.estado/1", "titulo": "primero", "n": 1}
        self.transicion_ok("tx-a", "items/it-1.json", contenido)
        with self.almacen() as alm:
            self.assertEqual(alm.leer("items/it-1.json"), contenido)
            self.assertIn("items/it-1.json", alm.listar())
            self.assertIn("items/it-1.json", alm.listar("items"))
            self.assertEqual(alm.listar("otro-dominio"), [])

    def test_04_varias_transiciones_consecutivas_encadenan_linaje(self):
        """T174 · Defecto que previene: revisiones que avanzan sin linaje comprobable.

        Cada revisión tiene que apuntar a la anterior por `revision_id`. Sin esa cadena,
        `detectar_bifurcacion` no puede decidir nada y dos máquinas divergen en silencio.
        """
        self.inicializar()
        rev0 = self.revision()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        rev1 = self.revision()
        self.transicion_ok("tx-b", "items/it-2.json", {"esquema": "ads.estado/1", "n": 2})
        rev2 = self.revision()
        self.transicion_ok("tx-c", "items/it-3.json", {"esquema": "ads.estado/1", "n": 3})
        rev3 = self.revision()

        self.assertEqual([rev0["revision"], rev1["revision"], rev2["revision"],
                          rev3["revision"]], [0, 1, 2, 3])
        self.assertEqual(rev1["padre"], rev0["revision_id"])
        self.assertEqual(rev2["padre"], rev1["revision_id"])
        self.assertEqual(rev3["padre"], rev2["revision_id"])
        self.assertEqual(len({rev0["cid_raiz"], rev1["cid_raiz"],
                              rev2["cid_raiz"], rev3["cid_raiz"]}), 4,
                         "cuatro contenidos distintos no pueden compartir `cid_raiz`")
        self.assertEqual(len(rev3["raiz"]), 3)
        with self.almacen() as alm:
            alm.verificar_integridad()
            alm.auditar()

    def test_05_el_diario_encadena_por_huella(self):
        """T177 · Defecto que previene: un diario reescribible sin dejar rastro.

        `previo` es la `huella` del evento anterior. Si la cadena no se construye, quitar
        o alterar un evento pasa desapercibido y la auditabilidad de `g.13` es decorativa.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        self.transicion_ok("tx-b", "items/it-2.json", {"esquema": "ads.estado/1", "n": 2})
        with self.almacen(recuperar=False) as alm:
            eventos = alm.diario()
        self.assertGreaterEqual(len(eventos), 4)
        self.assertIsNone(eventos[0]["previo"], "el primer evento no tiene previo (§2.4)")
        for anterior, siguiente in zip(eventos, eventos[1:]):
            self.assertEqual(siguiente["previo"], anterior["huella"],
                             "la cadena de hash del diario está rota")
            self.assertEqual(siguiente["secuencia"], anterior["secuencia"] + 1)
        for ev in eventos:
            self.assertEqual(ev["esquema"], "ads.estado/1")

    def test_06_recuperacion_limpia_no_inventa_nada(self):
        """T175 · Defecto que previene: una recuperación que «arregla» un almacén sano.

        Sobre un almacén sin ventana abierta, `recuperar()` NO puede añadir eventos ni
        mover la revisión. Un motor que anota algo en cada arranque acaba con un diario
        que no explica nada.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        antes_rev = self.revision()
        antes_diario = self.tipos_del_diario()
        with self.almacen() as alm:
            self.assertEqual(alm.estado_de_la_ventana(), "cerrada")
            alm.recuperar()
        self.assertEqual(self.revision(), antes_rev)
        self.assertEqual(self.tipos_del_diario(), antes_diario)

    def test_07_recuperar_es_idempotente_n_veces(self):
        """T175 · Defecto que previene: una recuperación que se acumula.

        El §3 exige que `recuperar()` invocada N veces produzca el mismo estado y no añada
        eventos después de la pasada que resolvió la ventana. Se ejecuta cinco veces.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        caida = self.transicion("tx-b", "items/it-2.json",
                                {"esquema": "ads.estado/1", "n": 2},
                                fallo="antes-de-escribir-temporal")
        self.assertEqual(caida.returncode, CODIGO_SALIDA_CAIDA)
        with self.almacen(recuperar=False) as alm:
            alm.recuperar()
        tras_la_primera = (self.revision(), self.tipos_del_diario())
        for _ in range(4):
            with self.almacen(recuperar=False) as alm:
                alm.recuperar()
            self.assertEqual((self.revision(), self.tipos_del_diario()), tras_la_primera,
                             "una recuperación posterior cambió el estado: no es idempotente")

    def test_08_aplicar_dos_veces_el_mismo_id_no_reaplica(self):
        """T174 · Defecto que previene: duplicar una transición al reintentar tras un timeout.

        El §9 fija que un `id` ya confirmado devuelve el resultado de la primera con
        `repetida=True`. Si en vez de eso se reaplica, un reintento del llamador duplica
        el efecto y la revisión avanza dos veces por una sola orden.
        """
        self.inicializar()
        contenido = {"esquema": "ads.estado/1", "n": 1}
        with self.almacen() as alm:
            base = alm.revision()["revision_id"]
            t = estado.Transicion(tipo="prueba", base=base,
                                  operaciones=[estado.Escritura("items/it-1.json", contenido)],
                                  autor="agente-b", motivo="idempotencia", id="tx-a")
            primero = alm.aplicar(t)
            self.assertFalse(getattr(primero, "repetida", False))
            rev_tras_el_primero = alm.revision()

            repetido = estado.Transicion(
                tipo="prueba", base=base,
                operaciones=[estado.Escritura("items/it-1.json", contenido)],
                autor="agente-b", motivo="idempotencia", id="tx-a")
            segundo = alm.aplicar(repetido)
            self.assertTrue(getattr(segundo, "repetida", False),
                            "el segundo `aplicar` con el mismo id debe venir con repetida=True")
            self.assertEqual(alm.revision(), rev_tras_el_primero,
                             "una repetición movió la revisión: se reaplicó")

    def test_09_migracion_del_formato_heredado_cero_a_uno(self):
        """T179 · Defecto que previene: una compatibilidad prometida y no demostrable.

        El §5 exige una migración REGISTRADA de la versión 0 —formato heredado, sin
        `FORMATO.json`— a la 1. Si `abrir` rechazara el almacén heredado, esa migración
        sería inalcanzable y la promesa de compatibilidad sería literalmente inejecutable:
        por eso este caso abre primero y migra después.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        os.remove(self.ruta_estado("FORMATO.json"))          # almacén heredado, versión 0

        with self.almacen(recuperar=False) as alm:
            informe = alm.migrar(1)
            self.assertIsInstance(informe.a_dict(), dict)
        formato = json.loads(texto_de(self.ruta_estado("FORMATO.json")))
        self.assertEqual(formato["version_formato"], estado.VERSION_DE_FORMATO)
        self.assertIn("migracion.aplicada", self.tipos_del_diario(),
                      "una migración sin evento en el diario no es auditable (§5)")
        with self.almacen() as alm:
            alm.verificar_integridad()
            self.assertEqual(alm.leer("items/it-1.json")["n"], 1,
                             "la migración perdió el estado que debía conservar")

    def test_10_migrar_a_la_version_vigente_es_inocuo(self):
        """T179 · Defecto que previene: una migración que se aplica dos veces.

        Migrar a la versión que ya se tiene no puede escribir nada. Un motor que anota
        `migracion.aplicada` en cada arranque convierte el diario en ruido.
        """
        self.inicializar()
        antes = self.tipos_del_diario()
        with self.almacen() as alm:
            alm.migrar(estado.VERSION_DE_ESQUEMA)
        self.assertEqual(self.tipos_del_diario(), antes)

    def test_11_reconciliacion_abierta_deducida_y_resuelta(self):
        """T178 · Defecto que previene: una reconciliación que se cierra borrando su registro.

        `g.9` obliga a que `reconciliacion_pendiente` se DEDUZCA —apertura sin resolución—
        y a que sólo desaparezca por una transición explícita y auditable.
        """
        self.inicializar()
        with self.almacen() as alm:
            registro = alm.abrir_reconciliacion(
                producto="pesquerapp", repositorio="backend", item="it-1",
                intento=3, causa="reintentos agotados")
            self.assertTrue(registro)
            pendientes = alm.reconciliacion_pendiente()
            self.assertEqual([p["registro"] for p in pendientes], [registro])
            rev_antes = alm.revision()["revision"]

            alm.resolver_reconciliacion(registro, autoridad="SIS",
                                        motivo="resuelto por la autoridad")
            self.assertEqual(alm.reconciliacion_pendiente(), [],
                             "la resolución no retiró la pendencia")
            self.assertGreater(alm.revision()["revision"], rev_antes,
                               "resolver es una TRANSICIÓN: tiene que mover la revisión")
        tipos = self.tipos_del_diario()
        self.assertIn("reconciliacion.abierta", tipos)
        self.assertIn("reconciliacion.resuelta", tipos)

    def test_12_abrir_reconciliacion_no_toca_el_estado_canonico(self):
        """T178 · Defecto que previene: colapsar el registro auxiliar en el estado canónico.

        `I-g7` los mantiene SEPARADOS. Abrir una reconciliación no puede alterar ni un
        byte de `canonico/` ni la revisión publicada.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        rev_antes = self.revision()
        with self.almacen() as alm:
            alm.abrir_reconciliacion(producto="p", repositorio="r", item="i",
                                     intento=3, causa="prueba")
        self.assertEqual(self.revision(), rev_antes,
                         "el registro auxiliar movió el estado canónico (`g.9` lo prohíbe)")

    def test_13_el_registro_auxiliar_encadena_y_fecha_por_momento_logico(self):
        """T178 · Defecto que previene: usar el reloj como «momento» (`I-g3`).

        El §2.5 obliga a que el momento sea `{diario_secuencia, revision}`. Un reloj de
        pared en un artefacto durable rompe el determinismo y el árbol deja de reproducirse.
        """
        self.inicializar()
        with self.almacen() as alm:
            alm.abrir_reconciliacion(producto="p", repositorio="r", item="i",
                                     intento=2, causa="prueba")
        with open(self.ruta_estado("reconciliacion", "REGISTRO.jsonl"), encoding="utf-8") as fh:
            lineas = [json.loads(l) for l in fh if l.strip()]
        self.assertTrue(lineas)
        apertura = lineas[0]
        self.assertEqual(apertura["tipo"], "apertura")
        self.assertIsNone(apertura["previo"])
        self.assertEqual(sorted(apertura["momento"]), ["diario_secuencia", "revision"])
        for campo in ("producto", "repositorio", "item", "intento", "causa"):
            self.assertIn(campo, apertura, f"`g.9` exige identificar {campo}")

    def test_14_mismo_estado_mismos_bytes(self):
        """T173 · Defecto que previene: la no reproducibilidad silenciosa (`I-g3`).

        Dos almacenes construidos con las MISMAS transiciones tienen que dar el mismo
        `cid_raiz` y los mismos bytes canónicos. Basta una hora de pared o un contador de
        ejecución escondido para que esto falle, y es justo lo que se quiere detectar.
        """
        segundo = os.path.join(self.tmp, "control-2")
        os.makedirs(segundo)
        for repo in (self.repo, segundo):
            self.assertEqual(cli(repo, ["inicializar", "--json"]).returncode, 0)
            carga = os.path.join(self.cargas, "gemelo.json")
            escribir_json(carga, {"esquema": "ads.estado/1", "n": 7, "t": "gemelo"})
            base = json.loads(cli(repo, ["revision", "--json"]).stdout)["revision_id"]
            proceso = cli(repo, ["transicion", "--id", "tx-a", "--autor", "agente-b",
                                 "--motivo", "gemelo", "--base", base,
                                 "--escribir", f"items/it-1.json={carga}"])
            self.assertEqual(proceso.returncode, 0, proceso.stderr)

        a = json.loads(cli(self.repo, ["revision", "--json"]).stdout)
        b = json.loads(cli(segundo, ["revision", "--json"]).stdout)
        self.assertEqual(a["cid_raiz"], b["cid_raiz"])
        self.assertEqual(a["revision_id"], b["revision_id"])
        ruta_a = os.path.join(self.repo, "estado", "canonico", "items", "it-1.json")
        ruta_b = os.path.join(segundo, "estado", "canonico", "items", "it-1.json")
        self.assertEqual(bytes_de(ruta_a), bytes_de(ruta_b))

    def test_15_ningun_artefacto_durable_lleva_reloj_ni_pid(self):
        """T173 · Defecto que previene: el determinismo roto por un campo «inofensivo».

        Se recorre TODO lo que el motor acaba de escribir en `canonico/`, `diario/` y
        `reconciliacion/` buscando marcas de tiempo, epochs y el pid del proceso que las
        escribió. El §0 lo prohíbe expresamente.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        with self.almacen() as alm:
            alm.abrir_reconciliacion(producto="p", repositorio="r", item="i",
                                     intento=1, causa="prueba")
        sospechosos = [
            re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}"),          # ISO-8601
            re.compile(r"\b1[6-9]\d{8}\b"),                        # epoch en segundos
            re.compile(r"\bpid\b", re.IGNORECASE),
            re.compile(r"\bduracion\b|\bduration\b", re.IGNORECASE),
        ]
        for sub in ("canonico", "diario", "reconciliacion"):
            base = self.ruta_estado(sub)
            for dirpath, _d, ficheros in os.walk(base):
                for nombre in ficheros:
                    ruta = os.path.join(dirpath, nombre)
                    texto = texto_de(ruta, errors="replace")
                    for patron in sospechosos:
                        self.assertIsNone(
                            patron.search(texto),
                            f"{os.path.relpath(ruta, self.repo)} contiene «{patron.pattern}»: "
                            f"el §0 prohíbe reloj, duración y pid en lo durable")

    def test_16_borrado_como_operacion_de_transicion(self):
        """T174 · Defecto que previene: un borrado que deja la ruta en `raiz` o el fichero en disco.

        Tras borrar, ni `leer` puede devolverlo ni `raiz` puede seguir citándolo: un
        `cid_raiz` que menciona lo que ya no está hace fallar toda verificación posterior.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        with self.almacen() as alm:
            base = alm.revision()["revision_id"]
            alm.aplicar(estado.Transicion(
                tipo="prueba", base=base, operaciones=[estado.Borrado("items/it-1.json")],
                autor="agente-b", motivo="borrado", id="tx-borra"))
            self.assertNotIn("items/it-1.json", alm.revision()["raiz"])
            self.assertNotIn("items/it-1.json", alm.listar())
            alm.verificar_integridad()
            alm.auditar()

    def test_17_auditar_reproduce_la_raiz_desde_el_diario(self):
        """T177 · Defecto que previene: un diario que no explica el estado que dice explicar.

        `g.13`: todo cambio del estado canónico es explicable por el diario. `auditar()`
        reproduce el `cid_raiz` vigente aplicando el diario desde el principio.
        """
        self.inicializar()
        for n in range(1, 4):
            self.transicion_ok(f"tx-{n}", f"items/it-{n}.json",
                               {"esquema": "ads.estado/1", "n": n})
        with self.almacen() as alm:
            informe = alm.auditar()
            datos = informe.a_dict()
            self.assertIsInstance(datos, dict)
            self.assertEqual(json.dumps(datos, sort_keys=True, ensure_ascii=False),
                             json.dumps(informe.a_dict(), sort_keys=True, ensure_ascii=False),
                             "`a_dict()` no es determinista entre dos llamadas")

    def test_18_detectar_bifurcacion_distingue_el_mismo_linaje_del_ajeno(self):
        """T176 · Defecto que previene: dos máquinas divergiendo sin que nadie lo note (`g.6`).

        No se comprueba CÓMO se resuelve —`g.6` reserva eso al contrato— sino que el
        informe de una revisión del MISMO linaje difiere del de una revisión ajena. Si los
        dos informes salen iguales, la detección no está detectando nada.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        with self.almacen() as alm:
            propia = alm.revision()
            ajena = dict(propia)
            ajena["revision_id"] = "sha256:" + "0" * 64
            ajena["padre"] = "sha256:" + "1" * 64
            ajena["cid_raiz"] = "sha256:" + "2" * 64
            informe_propio = alm.detectar_bifurcacion(propia)
            informe_ajeno = alm.detectar_bifurcacion(ajena)
        self.assertIsInstance(informe_propio, dict)
        self.assertIsInstance(informe_ajeno, dict)
        self.assertNotEqual(informe_propio, informe_ajeno,
                            "`detectar_bifurcacion` da el mismo informe para el mismo "
                            "linaje y para uno ajeno: no detecta la bifurcación")
        # `propia` viene de la API y `self.revision()` del CLI, y el CLI añade `ventana`.
        # La afirmación que interesa —detectar una bifurcación NO puede mover el estado—
        # se comprueba sobre las claves durables del §2.3, que es donde vive el estado.
        self.assertEqual(solo_durables(self.revision()), solo_durables(propia),
                         "detectar una bifurcación no puede modificar el estado")


# ===================================================================================
# NEGATIVOS · lo que el motor tiene PROHIBIDO hacer
# ===================================================================================

    def test_19_abrir_y_resolver_una_reconciliacion_por_la_CLI(self):
        """T178 · Defecto que previene: un camino del motor que sólo existe en la API.

        La apertura explícita de una reconciliación no tenía subcomando, de modo que el
        único camino alcanzable desde fuera era el de reintentos agotados — y era
        precisamente el que no se comprobaba contra el diario. Un camino que sólo existe en
        la API no se ejercita, y lo que no se ejercita se rompe sin que nadie lo vea.
        """
        self.inicializar()
        abrir = cli(self.repo, ["abrir-reconciliacion", "--producto", "pesquerapp",
                                "--repositorio", "backend", "--item", "it-9",
                                "--intento", "3", "--causa", "el remoto no responde"])
        self.assertEqual(abrir.returncode, 0, abrir.stderr or abrir.stdout)

        listado = cli(self.repo, ["reconciliacion", "--pendientes", "--json"])
        self.assertEqual(listado.returncode, 0, listado.stderr)
        datos = json.loads(listado.stdout)
        self.assertEqual(datos["pendientes"], ["rec-0001"],
                         f"la apertura por CLI no se dedujo: {datos['pendientes']}")
        registro = datos["pendientes"][0]
        apertura = [l for l in datos["lineas"]
                    if l["tipo"] == "apertura" and l["registro"] == registro][0]
        for campo in ("producto", "repositorio", "item", "intento", "causa", "momento"):
            self.assertIn(campo, apertura,
                          f"`g.9` exige que el registro identifique {campo}")

        resolver = cli(self.repo, ["resolver", registro, "--autoridad", "DSP",
                                   "--motivo", "reintegrado a mano y comprobado"])
        self.assertEqual(resolver.returncode, 0, resolver.stderr or resolver.stdout)

        with self.almacen() as alm:
            self.assertEqual(alm.reconciliacion_pendiente(), [],
                             "la pendencia sigue viva tras resolverla por transición")
            self.assertIn("reconciliacion.resuelta", [ev["tipo"] for ev in alm.diario()],
                          "la resolución no dejó rastro auditable en el diario")
        for orden in (["verificar"], ["auditar"]):
            self.assertEqual(cli(self.repo, orden).returncode, 0,
                             f"`{orden[0]}` no queda en verde tras una resolución legítima")


class Negativos(Caso):

    def test_20_estado_corrupto_al_leer(self):
        """T177 · Defecto que previene: servir como bueno un fichero canónico manipulado.

        `g.5`: toda corrupción se detecta AL LEER y produce fallo cerrado. Se cambia el
        contenido conservando JSON válido, que es el caso difícil: sintácticamente sano,
        pero su `cid` ya no casa con `REVISION.json.raiz`.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        ruta = self.ruta_estado("canonico", "items", "it-1.json")
        escribir_json(ruta, {"esquema": "ads.estado/1", "n": 999})
        with self.almacen(recuperar=False) as alm:
            self.assertFalloCerrado(errores.EstadoCorrupto, alm.leer, "items/it-1.json")

    def test_21_diario_truncado(self):
        """T177 · Defecto que previene: aceptar un diario cortado por la mitad.

        Un corte de luz durante un `append` deja media línea. Leerlo «hasta donde se
        pueda» es exactamente cómo se pierde una transición sin que nadie se entere.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        ruta = self.ruta_estado("diario", "DIARIO.jsonl")
        bruto = bytes_de(ruta)
        with open(ruta, "wb") as fh:
            fh.write(bruto[:-12])                                # media línea final
        self.assertFalloCerrado(errores.DiarioCorrupto, estado.abrir, self.repo,
                                recuperar=False)

    def test_22_diario_con_la_cadena_de_hash_rota(self):
        """T177 · Defecto que previene: reescribir un evento del diario y que cuadre igual.

        Se altera el `motivo` de un evento intermedio dejando el JSON válido: su `huella`
        deja de casar y la cadena se parte. Sin esta comprobación, el diario es un fichero
        de texto editable y `g.13` no vale nada.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        self.transicion_ok("tx-b", "items/it-2.json", {"esquema": "ads.estado/1", "n": 2})
        ruta = self.ruta_estado("diario", "DIARIO.jsonl")
        lineas = lineas_json(ruta)
        lineas[1]["motivo"] = "reescrito a mano"
        with open(ruta, "w", encoding="utf-8") as fh:
            for ev in lineas:
                fh.write(json.dumps(ev, sort_keys=True, ensure_ascii=False,
                                    separators=(",", ":")) + "\n")
        with self.almacen(recuperar=False) as alm:
            self.assertFalloCerrado(errores.DiarioCorrupto, alm.verificar_integridad)

    def test_23_escritura_parcial_termina_en_MARCAR_y_no_en_publicacion(self):
        """T175 · Defecto que previene: COMPLETAR una transición cuyo material ya no está.

        Se cae tras `transicion.preparada` —punto de no retorno— y se BORRA uno de los
        objetos preparados. El §3 es tajante: si falta un objeto preparado o su `cid` no
        casa, se MARCA. Completar «con lo que haya» publicaría una mezcla parcial, que es
        precisamente lo que `g.3` prohíbe.

        EXPECTATIVA: `RecuperacionMarcada`, evento `transicion.marcada`, copia íntegra en
        `reconciliacion/conflictos/<tx>/`, y la revisión SIN avanzar.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        rev_antes = self.revision()
        caida = self.transicion("tx-b", "items/it-2.json",
                                {"esquema": "ads.estado/1", "n": 2},
                                fallo="antes-del-commit-atomico")
        self.assertEqual(caida.returncode, CODIGO_SALIDA_CAIDA)

        zona = self.ruta_estado("operacional", "tx")
        preparados = [os.path.join(d, f) for d, _s, fs in os.walk(zona) for f in fs]
        self.assertTrue(preparados, "no hay zona de preparación tras `preparada`")
        os.remove(preparados[0])

        self.assertFalloCerrado(errores.RecuperacionMarcada, estado.abrir, self.repo)
        self.assertIn("transicion.marcada", self.tipos_del_diario())
        conflictos = self.ruta_estado("reconciliacion", "conflictos")
        self.assertTrue(os.path.isdir(conflictos) and os.listdir(conflictos),
                        "MARCAR sin copia íntegra de lo divergente (§3)")
        self.assertEqual(self.revision()["revision"], rev_antes["revision"],
                         "una transición marcada NO puede haber publicado")

    def test_24_revision_obsoleta(self):
        """T176 · Defecto que previene: la actualización perdida.

        Quien parte de una base que ya no es la vigente tiene que ser rechazado. Si el
        motor acepta la base vieja, la escritura del que llegó antes desaparece sin rastro.
        """
        self.inicializar()
        base_vieja = self.revision()["revision_id"]
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        proceso = self.transicion("tx-b", "items/it-2.json",
                                  {"esquema": "ads.estado/1", "n": 2}, base=base_vieja)
        self.assertEqual(proceso.returncode, 1)
        self.assertEqual(codigo_de_error(proceso), "REVISION_OBSOLETA")
        with self.almacen() as alm:
            self.assertNotIn("items/it-2.json", alm.listar())

    def test_25_identificador_duplicado_con_operaciones_distintas(self):
        """T174 · Defecto que previene: reutilizar un `id` de transacción para otra cosa.

        Mismo `id` y mismas operaciones es idempotencia. Mismo `id` y operaciones
        DISTINTAS es un error del llamador, y tragárselo haría que la idempotencia mintiera.
        """
        self.inicializar()
        with self.almacen() as alm:
            base = alm.revision()["revision_id"]
            alm.aplicar(estado.Transicion(
                tipo="prueba", base=base,
                operaciones=[estado.Escritura("items/it-1.json",
                                              {"esquema": "ads.estado/1", "n": 1})],
                autor="agente-b", motivo="primera", id="tx-a"))
            distinta = estado.Transicion(
                tipo="prueba", base=alm.revision()["revision_id"],
                operaciones=[estado.Escritura("items/it-1.json",
                                              {"esquema": "ads.estado/1", "n": 2})],
                autor="agente-b", motivo="otra cosa", id="tx-a")
            self.assertFalloCerrado(errores.IdentificadorDuplicado, alm.aplicar, distinta)
            self.assertEqual(alm.leer("items/it-1.json")["n"], 1,
                             "el duplicado rechazado alteró el estado")

    def test_26_migracion_desconocida(self):
        """T179 · Defecto que previene: adivinar una migración que nadie registró (`g.11`)."""
        self.inicializar()
        with self.almacen() as alm:
            self.assertFalloCerrado(errores.MigracionDesconocida, alm.migrar, 99)
        self.assertNotIn("migracion.aplicada", self.tipos_del_diario())

    def test_27_version_de_esquema_desconocida(self):
        """T179 · Defecto que previene: leer un almacén futuro «haciendo lo que se pueda».

        `g.10` y `G-A7`: fallo cerrado, no adivinanza. Se marca `REVISION.json` con un
        esquema que este lector no entiende.
        """
        self.inicializar()
        ruta = self.ruta_estado("REVISION.json")
        datos = json.loads(texto_de(ruta))
        datos["esquema"] = "ads.estado/99"
        escribir_json(ruta, datos)
        self.assertFalloCerrado(errores.VersionDesconocida, estado.abrir, self.repo,
                                recuperar=False)

    def test_28_formato_desconocido(self):
        """T179 · Defecto que previene: abrir un almacén cuyo FORMATO no se entiende (§5)."""
        self.inicializar()
        escribir_json(self.ruta_estado("FORMATO.json"),
                      {"formato": "ads.estado", "version_formato": 99})
        self.assertFalloCerrado(errores.FormatoDesconocido, estado.abrir, self.repo,
                                recuperar=False)

    def test_29_almacen_no_inicializado(self):
        """T173 · Defecto que previene: crear el almacén por sorpresa al abrirlo.

        Abrir lo que no existe tiene que fallar, no inicializar en silencio: un `--repo`
        mal escrito crearía un almacén vacío y el estado real parecería haberse perdido.
        """
        vacio = os.path.join(self.tmp, "sin-almacen")
        os.makedirs(vacio)
        self.assertFalloCerrado(errores.AlmacenNoInicializado, estado.abrir, vacio)
        self.assertFalse(os.path.exists(os.path.join(vacio, "estado")),
                         "abrir un almacén inexistente lo creó")

    def test_30_inicializar_dos_veces(self):
        """T173 · Defecto que previene: reinicializar encima de un almacén con estado."""
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        segundo = cli(self.repo, ["inicializar", "--json"])
        self.assertEqual(segundo.returncode, 1)
        self.assertEqual(codigo_de_error(segundo), "ALMACEN_YA_INICIALIZADO")
        with self.almacen() as alm:
            self.assertEqual(alm.leer("items/it-1.json")["n"], 1)

    def test_31_rutas_invalidas(self):
        """T174 · Defecto que previene: escribir fuera del almacén por una ruta compuesta.

        `../`, ruta absoluta y ruta vacía. Es la familia de defectos que convierte un
        motor de estado en una primitiva de escritura arbitraria.

        SE COMPRUEBAN LAS DOS CAPAS, y no una:

          · `Transicion.__init__` valida en el CONSTRUCTOR y levanta `RutaInvalida` antes
            de que la transición llegue a existir. Fallar pronto es lo correcto: una
            transición mal formada no debería poder circular por el programa.

          · `aplicar` vuelve a validar (paso 3 del §3). Se comprueba con una transición
            construida por OTRA VÍA —válida al nacer y alterada después, que es como llega
            un objeto reconstruido desde fuera o manipulado por el llamador—, porque una
            validación que sólo vive en el constructor se puede rodear, y entonces la
            frontera del almacén dependería de la buena educación de quien llama.
        """
        self.inicializar()
        malas = ("../fuera.json", "/etc/ads.json", "items/../../fuera.json", "")

        # capa 1 · el constructor rechaza, y la transición ni siquiera se construye.
        # Se envuelve en un cierre porque `Transicion` recibe `tipo=` como palabra clave y
        # chocaría con el primer parámetro de `assertFalloCerrado`; de paso queda escrito
        # que lo que se comprueba aquí es la CONSTRUCCIÓN.
        def construir(ruta):
            return estado.Transicion(
                tipo="prueba", base="sha256:" + "0" * 64,
                operaciones=[estado.Escritura(ruta, {"esquema": "ads.estado/1"})],
                autor="agente-b", motivo="ruta inválida", id="tx-constructor")

        for mala in malas:
            self.assertFalloCerrado(errores.RutaInvalida, construir, mala)

        # capa 2 · `aplicar` rechaza aunque la transición haya esquivado el constructor
        with self.almacen() as alm:
            base = alm.revision()["revision_id"]
            for numero, mala in enumerate(malas):
                t = estado.Transicion(
                    tipo="prueba", base=base,
                    operaciones=[estado.Escritura("items/it-1.json",
                                                  {"esquema": "ads.estado/1"})],
                    autor="agente-b", motivo="ruta inválida", id=f"tx-{numero}")
                t.operaciones[0].ruta = mala          # alterada DESPUÉS de construirse
                self.assertFalloCerrado(errores.RutaInvalida, alm.aplicar, t)
            self.assertEqual(alm.listar(), [],
                             "una ruta inválida llegó a publicar algo")
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "fuera.json")),
                         "una ruta compuesta escribió fuera del almacén")

    def test_32_transicion_invalida(self):
        """T174 · Defecto que previene: aceptar una transición sin operaciones o con basura.

        Una transición vacía que «tiene éxito» publica una revisión que no explica nada, y
        deja el diario lleno de eventos sin contenido.
        """
        self.inicializar()
        with self.almacen() as alm:
            base = alm.revision()["revision_id"]
            vacia = estado.Transicion(tipo="prueba", base=base, operaciones=[],
                                      autor="agente-b", motivo="vacía", id="tx-vacia")
            self.assertFalloCerrado(errores.TransicionInvalida, alm.aplicar, vacia)
            sin_autor = estado.Transicion(
                tipo="prueba", base=base,
                operaciones=[estado.Escritura("items/it-1.json", {"esquema": "ads.estado/1"})],
                autor="", motivo="", id="tx-sin-autor")
            self.assertFalloCerrado(errores.TransicionInvalida, alm.aplicar, sin_autor)

    def test_33_modificar_el_estado_sin_diario_no_pasa_la_auditoria(self):
        """T177 · Defecto que previene: el estado editado a mano que nadie desmiente.

        Se recalcula `REVISION.json` NO: se edita el fichero canónico y se deja el resto
        como está, que es lo que hace quien «arregla» un item con un editor. `auditar()`
        tiene que fallar cerrado porque ese cambio no lo explica ningún evento.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        escribir_json(self.ruta_estado("canonico", "items", "it-1.json"),
                      {"esquema": "ads.estado/1", "n": 42})
        with self.almacen(recuperar=False) as alm:
            with self.assertRaises(errores.ErrorDeEstado):
                alm.auditar()

    def test_34_borrar_la_reconciliacion_a_mano_es_corrupcion(self):
        """T178 · Defecto que previene: cerrar una pendencia borrando su línea.

        El §9 lo dice con todas las letras: borrar el registro a mano tiene que dar
        `RegistroDeReconciliacionCorrupto`. Si no, cualquiera retira una pendencia sin la
        transición explícita que `g.9` exige.
        """
        self.inicializar()
        with self.almacen() as alm:
            registro = alm.abrir_reconciliacion(producto="p", repositorio="r", item="i",
                                                intento=3, causa="prueba")
            alm.resolver_reconciliacion(registro, autoridad="SIS", motivo="cerrada")
        ruta = self.ruta_estado("reconciliacion", "REGISTRO.jsonl")
        lineas = [l for l in texto_de(ruta).splitlines(keepends=True) if l.strip()]
        self.assertGreaterEqual(len(lineas), 2)
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write(lineas[0])                                  # se borra la resolución
        with self.almacen(recuperar=False) as alm:
            self.assertFalloCerrado(errores.RegistroDeReconciliacionCorrupto,
                                    alm.verificar_integridad)

    def test_35_resolver_una_reconciliacion_inexistente(self):
        """T178 · Defecto que previene: cerrar una pendencia que nunca se abrió."""
        self.inicializar()
        with self.almacen() as alm:
            self.assertFalloCerrado(errores.ReconciliacionDesconocida,
                                    alm.resolver_reconciliacion, "rec-9999",
                                    autoridad="SIS", motivo="no existe")

    @unittest.skipIf(os.geteuid() == 0, "como root todo permiso es concedido")
    def test_36_permisos_insuficientes(self):
        """T174 · Defecto que previene: dejar el almacén a medias cuando el disco dice que no.

        `g.4`: una operación que no puede alcanzar durabilidad FALLA de forma visible y no
        se declara completada. Se retira el permiso de escritura del directorio canónico.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        rev_antes = self.revision()
        canonico = self.ruta_estado("canonico")
        os.chmod(canonico, 0o555)
        try:
            with self.almacen(recuperar=False) as alm:
                base = alm.revision()["revision_id"]
                t = estado.Transicion(
                    tipo="prueba", base=base,
                    operaciones=[estado.Escritura("items/it-2.json",
                                                  {"esquema": "ads.estado/1", "n": 2})],
                    autor="agente-b", motivo="sin permiso", id="tx-b")
                self.assertFalloCerrado(errores.PermisoInsuficiente, alm.aplicar, t)
        finally:
            os.chmod(canonico, 0o755)
        self.assertEqual(self.revision(), rev_antes,
                         "una escritura sin permiso movió la revisión publicada")

    def test_37_uso_incorrecto_del_cli_sale_con_dos(self):
        """T173 · Defecto que previene: confundir «la operación falló» con «me lo pediste mal».

        El §11 separa 1 de 2 a propósito: un guion automatizado tiene que poder distinguir
        un error tipado del motor de una orden mal escrita.
        """
        self.inicializar()
        self.assertEqual(cli(self.repo, ["orden-que-no-existe"]).returncode, 2)
        self.assertEqual(cli(self.repo, ["transicion", "--id", "x"]).returncode, 2)

    def test_38_la_salida_no_lleva_rutas_absolutas_sin_json(self):
        """T173 · Defecto que previene: una evidencia que cambia de máquina a máquina.

        El §11 exige rutas relativas al repo cuando no se pide `--json`. Con rutas
        absolutas dentro, la evidencia publicada deja de ser comparable.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        for orden in (["listar"], ["revision"], ["verificar"]):
            proceso = cli(self.repo, orden)
            self.assertEqual(proceso.returncode, 0, proceso.stderr)
            self.assertNotIn(self.repo, proceso.stdout,
                             f"`{orden[0]}` imprime la ruta absoluta del repo")
            self.assertNotIn(self.tmp, proceso.stdout)


# ===================================================================================
# ATESTACIÓN EXTERNA · `g.15`, interfaz — no despliegue productivo
# ===================================================================================

    def test_39_ningun_error_imprime_una_ruta_absoluta_de_la_maquina(self):
        """T177 · Defecto que previene: una evidencia que cambia de máquina a máquina.

        `test_38` sólo miraba la salida de las órdenes que TERMINAN BIEN, y la auditoría
        independiente encontró la fuga donde no miraba: en los caminos de ERROR. Cuatro
        módulos —bloqueo, diario, reconciliación y atestación— pasaban la ruta cruda,
        mientras el motor sí la relativizaba. Aquí se recorren los errores de tres módulos
        distintos, en texto y en JSON, y se exige que ninguno imprima la ruta absoluta del
        temporal en el que corren. Es lo que hace que la evidencia publicada sea la misma
        en cualquier máquina.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})

        # tres corrupciones que salen por tres módulos distintos
        with open(self.ruta_estado("canonico", "items", "it-1.json"), "w",
                  encoding="utf-8") as fh:
            fh.write('{"esquema": "ads.estado/1", "n": 99}\n')
        ordenes = [["verificar"], ["leer", "items/it-1.json"], ["auditar"],
                   ["reconciliacion", "--pendientes"]]

        raiz_temporal = os.path.realpath(self.tmp)
        for orden in ordenes:
            for extra in ([], ["--json"]):
                proceso = cli(self.repo, orden + extra)
                salida = (proceso.stdout or "") + (proceso.stderr or "")
                self.assertNotIn(raiz_temporal, salida,
                                 f"`{' '.join(orden + extra)}` imprime la ruta absoluta de "
                                 f"la máquina: la evidencia dejaría de ser reproducible")
                self.assertNotIn(self.repo, salida)
                for linea in salida.splitlines():
                    self.assertNotRegex(
                        linea, r"(?<![\w])/(?:tmp|home|Users|var)/",
                        "una ruta absoluta se ha colado en la salida de error")


class Atestacion(Caso):

    def test_40_el_proveedor_efimero_se_declara_solo_para_pruebas(self):
        """T177 · Defecto que previene: que alguien tome el proveedor de pruebas por productivo.

        El §7 obliga a que su docstring lo diga literalmente, y `FD-1` sigue abierta: no
        hay titular ni custodio de clave productiva. Además se USA —firma y verifica— para
        que la comprobación no sea sólo de texto.
        """
        proveedor = atestacion.ProveedorEfimero()
        texto = (atestacion.ProveedorEfimero.__doc__ or "").upper()
        self.assertIn("EXCLUSIVAMENTE PARA PRUEBAS", texto)
        firma = proveedor.firmar(b"contenido")
        self.assertTrue(proveedor.verificar(b"contenido", firma))
        self.assertFalse(proveedor.verificar(b"contenido alterado", firma))
        self.assertTrue(proveedor.identidad())

    def test_41_sin_proveedor_no_hay_atestacion(self):
        """T177 · Defecto que previene: una ruta por defecto que firma con cualquier cosa (§7)."""
        self.inicializar()
        destino = os.path.join(self.tmp, "fuera", "evidencia.json")
        with self.almacen() as alm:
            self.assertFalloCerrado(errores.SinProveedorDeAtestacion,
                                    atestacion.atestar, alm, None, destino)
        self.assertFalse(os.path.exists(destino))

    def test_42_la_evidencia_no_puede_vivir_dentro_del_arbol_verificado(self):
        """T177 · Defecto que previene: verificarse a sí mismo desde dentro (`g.13`, `g.15`).

        Evidencia guardada dentro del árbol que verifica es evidencia que el propio árbol
        puede reescribir.
        """
        self.inicializar()
        dentro = os.path.join(self.repo, "evidencia.json")
        with self.almacen() as alm:
            self.assertFalloCerrado(errores.EvidenciaDentroDelArbol, atestacion.atestar,
                                    alm, atestacion.ProveedorEfimero(), dentro)
        self.assertFalse(os.path.exists(dentro))

    def test_43_evidencia_manipulada_truncada_o_de_otra_identidad(self):
        """T177 · Defecto que previene: un veredicto falseado DESDE DENTRO (`G-A9`).

        Tres ataques sobre la misma evidencia: alterarla, truncarla y presentarla ante
        otra identidad. Los tres tienen que fallar cerrado.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        proveedor = atestacion.ProveedorEfimero()
        destino = os.path.join(self.tmp, "fuera", "evidencia.json")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with self.almacen() as alm:
            atestacion.atestar(alm, proveedor, destino)
        self.assertTrue(atestacion.verificar_atestacion(destino, proveedor))

        bruto = bytes_de(destino)

        with open(destino, "wb") as fh:                           # manipulada
            fh.write(bruto.replace(b"sha256:", b"sha256:0", 1))
        self.assertFalloCerrado(errores.AtestacionInvalida,
                                atestacion.verificar_atestacion, destino, proveedor)

        with open(destino, "wb") as fh:                           # truncada
            fh.write(bruto[: len(bruto) // 2])
        self.assertFalloCerrado(errores.AtestacionInvalida,
                                atestacion.verificar_atestacion, destino, proveedor)

        with open(destino, "wb") as fh:                           # otra identidad
            fh.write(bruto)
        self.assertFalloCerrado(errores.AtestacionInvalida,
                                atestacion.verificar_atestacion, destino,
                                atestacion.ProveedorEfimero())


# ===================================================================================
# FALLO INYECTADO · los NUEVE puntos, con procesos que mueren de verdad
#
# Cada caso declara su EXPECTATIVA antes de mirar nada, porque la única forma de que una
# prueba de recuperación demuestre algo es que sepa de antemano cuál de las dos ramas debe
# tomar. El corte de la ventana es el evento `transicion.preparada`: antes de él, REVERTIR
# —la transición se pierde y NO se publica—; a partir de él, COMPLETAR.
# ===================================================================================

class FalloInyectado(Caso):

    def preparar_con_una_confirmada(self):
        """Deja el almacén con una transición YA confirmada, que ninguna caída puede tocar."""
        self.inicializar()
        self.transicion_ok("tx-previa", "items/it-0.json",
                           {"esquema": "ads.estado/1", "n": 0})
        return self.revision()

    def caer_en(self, punto, *, ident="tx-caida", ruta="items/it-1.json",
                contenido=None):
        contenido = contenido or {"esquema": "ads.estado/1", "n": 1}
        proceso = self.transicion(ident, ruta, contenido, fallo=punto)
        self.assertEqual(
            proceso.returncode, CODIGO_SALIDA_CAIDA,
            f"el punto '{punto}' no terminó el proceso con {CODIGO_SALIDA_CAIDA}: "
            f"código {proceso.returncode}. Un punto que no corta no prueba nada")
        return proceso

    # -- comprobaciones de las dos ramas, escritas una sola vez ---------------------
    def esperar_perdida_y_no_publicada(self, rev_antes, ruta, punto):
        """EXPECTATIVA: la transición se PERDIÓ y NO se publicó.

        Se cayó antes del punto de no retorno. Nada de `canonico/` se tocó: la reversión
        está acotada a lo especulativo local. Tras reiniciar tiene que quedar la revisión
        anterior, la ruta ausente y un `transicion.revertida` que lo explique.
        """
        with self.almacen() as alm:                              # abrir recupera (§3)
            self.assertEqual(alm.estado_de_la_ventana(), "cerrada",
                             f"[{punto}] la ventana sigue abierta tras recuperar")
            self.assertEqual(alm.revision()["revision"], rev_antes["revision"],
                             f"[{punto}] se publicó una transición que debía revertirse")
            self.assertEqual(alm.revision()["revision_id"], rev_antes["revision_id"])
            self.assertNotIn(ruta, alm.listar(),
                             f"[{punto}] la ruta se publicó pese a la reversión")
            self.assertNotIn(ruta, alm.revision()["raiz"])
            alm.verificar_integridad()
            alm.auditar()
        self.assertIn("transicion.revertida", self.tipos_del_diario(),
                      f"[{punto}] se revirtió sin anotarlo: la reversión no es auditable")
        self.assertNotIn("transicion.confirmada", self.tipos_del_diario()[-1:],
                         f"[{punto}] el último evento no puede ser una confirmación")

    def esperar_completada(self, rev_antes, ruta, contenido, punto):
        """EXPECTATIVA: la transición se COMPLETÓ.

        Se cayó a partir de `transicion.preparada`, que es el punto de no retorno. El §3
        obliga a reejecutar los pasos 8, 9 y 10 de forma idempotente: la revisión avanza
        exactamente uno, la ruta queda publicada con su contenido y el diario cierra con
        `transicion.confirmada`.
        """
        with self.almacen() as alm:
            self.assertEqual(alm.estado_de_la_ventana(), "cerrada",
                             f"[{punto}] la ventana sigue abierta tras recuperar")
            self.assertEqual(alm.revision()["revision"], rev_antes["revision"] + 1,
                             f"[{punto}] la transición preparada no se completó")
            self.assertEqual(alm.revision()["padre"], rev_antes["revision_id"],
                             f"[{punto}] la revisión completada perdió su linaje")
            self.assertEqual(alm.leer(ruta), contenido,
                             f"[{punto}] se publicó un contenido distinto del preparado")
            alm.verificar_integridad()
            alm.auditar()
        self.assertIn("transicion.confirmada", self.tipos_del_diario(),
                      f"[{punto}] se completó sin anotar la confirmación")

    # -- los nueve -----------------------------------------------------------------
    def test_50_durante_el_diario(self):
        """T175 · Punto 1/9 · `durante-el-diario` (paso 4 del protocolo).

        EXPECTATIVA: transición PERDIDA y NO publicada. Se cae escribiendo el evento
        `transicion.abierta`, mucho antes del punto de no retorno; puede que el diario ni
        siquiera contenga la apertura. Lo que NO puede ocurrir bajo ningún supuesto es que
        la ruta aparezca publicada: eso sería estado sin diario que lo explique (`g.13`).
        """
        rev = self.preparar_con_una_confirmada()
        self.caer_en("durante-el-diario")
        with self.almacen() as alm:
            self.assertEqual(alm.revision()["revision_id"], rev["revision_id"],
                             "[durante-el-diario] la revisión avanzó pese a caer en el diario")
            self.assertNotIn("items/it-1.json", alm.listar())
            self.assertEqual(alm.estado_de_la_ventana(), "cerrada")
            self.assertEqual(alm.leer("items/it-0.json")["n"], 0,
                             "la caída se llevó por delante una transición YA confirmada")
            alm.verificar_integridad()

    def test_51_antes_de_escribir_temporal(self):
        """T175 · Punto 2/9 · `antes-de-escribir-temporal` (paso 5, antes de tocar nada).

        EXPECTATIVA: transición PERDIDA y NO publicada. El diario tiene `abierta` y no
        `preparada`, así que la rama es REVERTIR.
        """
        rev = self.preparar_con_una_confirmada()
        self.caer_en("antes-de-escribir-temporal")
        self.esperar_perdida_y_no_publicada(rev, "items/it-1.json",
                                            "antes-de-escribir-temporal")

    def test_52_despues_de_escribir_temporal(self):
        """T175 · Punto 3/9 · `despues-de-escribir-temporal` (paso 5, ya en `operacional/tx/`).

        EXPECTATIVA: transición PERDIDA y NO publicada. Hay objetos en la zona de
        preparación, pero son ESPECULATIVOS LOCALES: `g.8` acota ahí la reversión y
        prohíbe publicarlos.
        """
        rev = self.preparar_con_una_confirmada()
        self.caer_en("despues-de-escribir-temporal")
        self.esperar_perdida_y_no_publicada(rev, "items/it-1.json",
                                            "despues-de-escribir-temporal")

    def test_53_despues_de_sincronizar_temporal(self):
        """T175 · Punto 4/9 · `despues-de-sincronizar-temporal` (paso 6, antes de `preparada`).

        EXPECTATIVA: transición PERDIDA y NO publicada. Que los temporales estén ya en
        disco NO adelanta el punto de no retorno: el punto de no retorno es el evento
        `transicion.preparada`, no el `fsync`.
        """
        rev = self.preparar_con_una_confirmada()
        self.caer_en("despues-de-sincronizar-temporal")
        self.esperar_perdida_y_no_publicada(rev, "items/it-1.json",
                                            "despues-de-sincronizar-temporal")

    def test_54_antes_del_commit_atomico(self):
        """T175 · Punto 5/9 · `antes-del-commit-atomico` (paso 8, tras `preparada`).

        EXPECTATIVA: transición COMPLETADA. Es el primer punto pasado el no retorno: la
        recuperación reejecuta 8, 9 y 10, y `canonico/` recibe lo preparado.
        """
        rev = self.preparar_con_una_confirmada()
        contenido = {"esquema": "ads.estado/1", "n": 1}
        self.caer_en("antes-del-commit-atomico", contenido=contenido)
        self.esperar_completada(rev, "items/it-1.json", contenido,
                                "antes-del-commit-atomico")

    def test_55_antes_de_sincronizar_directorio(self):
        """T175 · Punto 6/9 · `antes-de-sincronizar-directorio` (paso 8, entre `replace` y `fsync`).

        EXPECTATIVA: transición COMPLETADA. El objeto puede estar ya en su sitio sin que
        el directorio se haya sincronizado; la recuperación tiene que rehacer el paso de
        forma idempotente, no duplicarlo ni saltárselo.
        """
        rev = self.preparar_con_una_confirmada()
        contenido = {"esquema": "ads.estado/1", "n": 1}
        self.caer_en("antes-de-sincronizar-directorio", contenido=contenido)
        self.esperar_completada(rev, "items/it-1.json", contenido,
                                "antes-de-sincronizar-directorio")

    def test_56_despues_del_commit_atomico(self):
        """T175 · Punto 7/9 · `despues-del-commit-atomico` (paso 9, YA publicado).

        EXPECTATIVA: transición COMPLETADA. `REVISION.json` ya se reemplazó, así que lo
        publicado NO se restaura nunca (`g.8`): la recuperación sólo puede terminar de
        anotar `transicion.confirmada`. Revertir aquí sería deshacer algo publicado, que
        es exactamente lo que la norma prohíbe.
        """
        rev = self.preparar_con_una_confirmada()
        contenido = {"esquema": "ads.estado/1", "n": 1}
        self.caer_en("despues-del-commit-atomico", contenido=contenido)
        self.esperar_completada(rev, "items/it-1.json", contenido,
                                "despues-del-commit-atomico")
        self.assertNotIn("transicion.revertida", self.tipos_del_diario(),
                         "se revirtió una transición YA PUBLICADA (`g.8` lo prohíbe)")

    def test_57_antes_de_devolver_exito(self):
        """T175 · Punto 8/9 · `antes-de-devolver-exito` (paso 11, todo hecho, sin responder).

        EXPECTATIVA: transición COMPLETADA, y `recuperar()` no añade NADA. El llamador se
        quedó sin respuesta, pero el estado está cerrado: la ventana es `cerrada` y el
        único resto posible es la zona de preparación, que es reconstruible y no durable.
        """
        rev = self.preparar_con_una_confirmada()
        contenido = {"esquema": "ads.estado/1", "n": 1}
        self.caer_en("antes-de-devolver-exito", contenido=contenido)
        self.esperar_completada(rev, "items/it-1.json", contenido,
                                "antes-de-devolver-exito")
        tras_recuperar = self.tipos_del_diario()
        with self.almacen(recuperar=False) as alm:
            alm.recuperar()
        self.assertEqual(self.tipos_del_diario(), tras_recuperar,
                         "recuperar añadió eventos sobre una ventana ya cerrada")

    def test_58_durante_el_registro_auxiliar(self):
        """T175 · Punto 9/9 · `durante-el-registro-auxiliar` (la escritura de `g.9`).

        EXPECTATIVA, con las dos únicas salidas admisibles escritas por delante:
          · el ESTADO CANÓNICO queda intacto —revisión y `cid_raiz` idénticos—, porque el
            registro auxiliar no lo toca nunca (`g.9`, `I-g7`); y
          · el registro auxiliar queda o bien con su cadena íntegra, o bien detectado como
            `RegistroDeReconciliacionCorrupto` al verificar.
        Lo que queda PROHIBIDO es la tercera salida: una cadena rota que se lee como buena.
        """
        rev = self.preparar_con_una_confirmada()
        guion = os.path.join(self.tmp, "abrir_reconciliacion.py")
        with open(guion, "w", encoding="utf-8") as fh:
            fh.write(
                "import sys\n"
                f"sys.path.insert(0, {RUNTIME!r})\n"
                "import estado\n"
                "alm = estado.abrir(sys.argv[1], recuperar=False)\n"
                "alm.abrir_reconciliacion(producto='p', repositorio='r', item='i',\n"
                "                         intento=3, causa='caída dirigida')\n"
                "alm.cerrar()\n")
        entorno = dict(ENTORNO, ADS_ESTADO_FALLO="durante-el-registro-auxiliar")
        proceso = subprocess.run([sys.executable, guion, self.repo], capture_output=True,
                                 text=True, env=entorno, timeout=SEGUNDOS_DE_ESPERA,
                                 cwd=tempfile.gettempdir())
        self.assertEqual(proceso.returncode, CODIGO_SALIDA_CAIDA,
                         "el punto `durante-el-registro-auxiliar` no cortó el proceso")

        rev_ahora = self.revision()
        self.assertEqual(rev_ahora["revision_id"], rev["revision_id"],
                         "el registro auxiliar movió el estado canónico")
        self.assertEqual(rev_ahora["cid_raiz"], rev["cid_raiz"])
        with self.almacen() as alm:
            self.assertEqual(alm.leer("items/it-0.json")["n"], 0)
            try:
                alm.verificar_integridad()
            except errores.RegistroDeReconciliacionCorrupto as error:
                self.assertTrue(error.codigo)                     # fallo cerrado: admisible
            else:
                for pendiente in alm.reconciliacion_pendiente():
                    self.assertIn("registro", pendiente)

    def test_59_el_censo_de_puntos_es_el_del_contrato_y_todos_se_alcanzan(self):
        """T175 · Defecto que previene: dar por inyectada una caída que nunca se inyectó.

        Dos mitades, y las dos importan:

          · EL CENSO. `fallos.puntos()` se EJECUTA —no se lee el fichero— y se confronta
            con los nueve del §10; y se comprueba, contra el código del paquete, que
            ninguno queda declarado sin que nadie lo llame. Un punto declarado y no
            llamado es una caída que nadie podrá provocar nunca.

          · LA ERRATA. Un `ADS_ESTADO_FALLO` con el nombre mal escrito tiene que FALLAR
            RUIDOSAMENTE y nombrar el punto pedido. Si se ignorase en silencio, escribir
            `antes-del-commit` en vez de `antes-del-commit-atomico` daría una prueba en
            verde que no ha inyectado nada, y estaríamos publicando como evidencia de
            recuperación una ejecución en la que nunca hubo corte. La expectativa es
            explícita: código de salida 1 —error de la operación, no 70 y no 0—, código
            tipado `PUNTO_DE_FALLO_DESCONOCIDO`, el punto pedido nombrado en la salida, y
            el estado sin tocar.
        """
        self.assertEqual(sorted(fallos.puntos()), sorted(PUNTOS_DEL_CONTRATO))
        fuentes = ""
        paquete = os.path.join(RUNTIME, "estado")
        for dirpath, _d, ficheros in os.walk(paquete):
            for nombre in sorted(ficheros):
                if nombre.endswith(".py") and nombre != "fallos.py":
                    with open(os.path.join(dirpath, nombre), encoding="utf-8") as fuente:
                        fuentes += fuente.read()
        for punto in PUNTOS_DEL_CONTRATO:
            self.assertIn(punto, fuentes,
                          f"el punto '{punto}' está declarado y nadie lo llama")

        self.inicializar()
        rev_antes = self.revision()
        inventado = "antes-del-commit"          # la errata realista: el nombre a medias
        self.assertNotIn(inventado, fallos.puntos())
        proceso = self.transicion("tx-a", "items/it-1.json",
                                  {"esquema": "ads.estado/1", "n": 1},
                                  fallo=inventado)
        self.assertEqual(proceso.returncode, 1,
                         f"un punto de fallo inexistente salió con {proceso.returncode}: "
                         f"ni cortó (70) ni avisó (1), luego se ignoró en silencio")
        self.assertEqual(codigo_de_error(proceso), "PUNTO_DE_FALLO_DESCONOCIDO")
        self.assertIn(inventado, proceso.stdout + proceso.stderr,
                      "el error no nombra el punto que se pidió, que es lo único que "
                      "permite ver la errata")
        self.assertEqual(solo_durables(self.revision()), solo_durables(rev_antes),
                         "la errata en el punto de fallo llegó a mover el estado")

        # y en proceso, para que el módulo quede ejercitado y no sólo leído
        os.environ[fallos.VARIABLE] = inventado
        try:
            error = self.assertFalloCerrado(errores.ErrorDeEstado, fallos.activo)
            self.assertEqual(error.codigo, "PUNTO_DE_FALLO_DESCONOCIDO")
            self.assertIn(inventado, json.dumps(error.a_dict(), ensure_ascii=False),
                          "el error tipado no lleva el punto pedido en su contexto")
        finally:
            del os.environ[fallos.VARIABLE]


# ===================================================================================
# CONCURRENCIA · procesos de verdad, no dos objetos en memoria
# ===================================================================================

# Puerta de salida común: cada escritor espera a que aparezca un fichero y sólo entonces
# ejecuta el CLI. Sin esta puerta, lanzar cuatro `Popen` seguidos no garantiza solape y la
# «prueba de concurrencia» acabaría siendo cuatro escrituras en fila que pasan siempre.
GUION_PUERTA = """\
import os, sys, time
puerta = sys.argv[1]
limite = time.monotonic() + 60
while not os.path.exists(puerta) and time.monotonic() < limite:
    time.sleep(0.002)
os.execv(sys.executable, [sys.executable] + sys.argv[2:])
"""

# Retenedor del bloqueo: toma el `flock` exclusivo del escritor y NO lo suelta hasta que
# aparece el fichero de relevo. Es un proceso real, con el bloqueo real del §4.
GUION_RETENEDOR = """\
import fcntl, os, sys, time
cerrojo, listo, relevo = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(os.path.dirname(cerrojo), exist_ok=True)
fd = os.open(cerrojo, os.O_RDWR | os.O_CREAT, 0o644)
fcntl.flock(fd, fcntl.LOCK_EX)
open(listo, "w").close()
limite = time.monotonic() + 120
while not os.path.exists(relevo) and time.monotonic() < limite:
    time.sleep(0.01)
"""


class Concurrencia(Caso):

    def setUp(self):
        super().setUp()
        self.puerta_py = os.path.join(self.tmp, "puerta.py")
        with open(self.puerta_py, "w", encoding="utf-8") as fh:
            fh.write(GUION_PUERTA)
        self.retenedor_py = os.path.join(self.tmp, "retenedor.py")
        with open(self.retenedor_py, "w", encoding="utf-8") as fh:
            fh.write(GUION_RETENEDOR)
        self.cerrojo = self.ruta_estado("operacional", "escritor.lock")

    def lanzar_escritores(self, cuantos, base):
        """Arranca `cuantos` procesos que salen A LA VEZ, todos desde la MISMA base."""
        puerta = os.path.join(self.tmp, "abrir-la-puerta")
        procesos = []
        for n in range(cuantos):
            carga = os.path.join(self.cargas, f"c{n}.json")
            escribir_json(carga, {"esquema": "ads.estado/1", "escritor": n})
            orden = [sys.executable, self.puerta_py, puerta,
                     CLI, "--repo", self.repo, "transicion",
                     "--id", f"tx-carrera-{n}", "--autor", f"escritor-{n}",
                     "--motivo", "carrera", "--base", base,
                     "--escribir", f"items/it-{n}.json={carga}"]
            procesos.append(subprocess.Popen(orden, stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE, text=True,
                                             env=ENTORNO, cwd=tempfile.gettempdir()))
        time.sleep(0.2)                       # que todos lleguen a la puerta
        open(puerta, "w").close()
        resultados = []
        for p in procesos:
            salida, error = p.communicate(timeout=SEGUNDOS_DE_ESPERA)
            resultados.append((p.returncode, salida, error))
        return resultados

    def test_60_cuatro_escritores_desde_la_misma_base_no_dan_doble_exito(self):
        """T176 · Defecto que previene: dos escritores publicando sobre la MISMA revisión.

        Es LA garantía del §4: «Ningún doble éxito para la misma revisión». Cuatro
        procesos reales salen a la vez desde la misma base. Exactamente uno puede terminar
        con 0; los otros tres tienen que fallar con un código tipado y NO haber publicado
        nada. La revisión final es base+1, no base+4.
        """
        self.inicializar()
        base = self.revision()
        resultados = self.lanzar_escritores(4, base["revision_id"])
        exitos = [r for r in resultados if r[0] == 0]
        self.assertEqual(len(exitos), 1,
                         f"hubo {len(exitos)} éxitos para la misma revisión; sólo cabe uno. "
                         f"Resultados: {[(c, e.strip()[:80]) for c, _s, e in resultados]}")
        admisibles = {"REVISION_OBSOLETA", "ESCRITOR_CONCURRENTE",
                      "BLOQUEO_NO_ADQUIRIDO", "REINTENTOS_AGOTADOS"}
        for codigo, _salida, error in resultados:
            if codigo == 0:
                continue
            self.assertEqual(codigo, 1, "un perdedor no salió con 1 (§11)")
            hallado = re.findall(r"\b[A-Z][A-Z0-9_]{5,}\b", error or "")
            self.assertTrue(set(hallado) & admisibles,
                            f"el perdedor no dice por qué perdió: {error.strip()[:200]}")
        final = self.revision()
        self.assertEqual(final["revision"], base["revision"] + 1,
                         "la revisión avanzó más de una vez: hubo doble publicación")
        with self.almacen() as alm:
            self.assertEqual(len(alm.listar()), 1,
                             "más de un escritor publicó su objeto")
            alm.verificar_integridad()
            alm.auditar()

    def test_61_los_perdedores_pueden_reintentar_sobre_la_base_nueva(self):
        """T176 · Defecto que previene: una serialización que sólo sabe rechazar.

        `g.6` exige SERIALIZAR, no sólo detectar. Tras la carrera, el perdedor que relee
        la base vigente tiene que poder aplicar la suya, y el resultado final contiene las
        dos escrituras y sigue siendo íntegro.
        """
        self.inicializar()
        base = self.revision()
        self.lanzar_escritores(3, base["revision_id"])
        primera = self.revision()
        self.assertEqual(primera["revision"], base["revision"] + 1)
        self.transicion_ok("tx-tarde", "items/tarde.json",
                           {"esquema": "ads.estado/1", "n": 9})
        segunda = self.revision()
        self.assertEqual(segunda["revision"], primera["revision"] + 1)
        self.assertEqual(segunda["padre"], primera["revision_id"])
        with self.almacen() as alm:
            self.assertEqual(len(alm.listar()), 2)
            alm.verificar_integridad()

    def test_62_ocho_escritores_no_rompen_la_integridad(self):
        """T176 · Defecto que previene: la corrupción que sólo aparece con presión.

        Ocho procesos reales a la vez sobre la misma base. Además de la regla del doble
        éxito, se comprueba que el diario sigue encadenado y que `auditar()` explica el
        estado: una carrera que deja el diario con dos eventos de la misma secuencia no
        sería visible mirando sólo los códigos de salida.
        """
        self.inicializar()
        base = self.revision()
        resultados = self.lanzar_escritores(8, base["revision_id"])
        self.assertEqual(len([r for r in resultados if r[0] == 0]), 1,
                         "más de un escritor tuvo éxito sobre la misma revisión")
        self.assertEqual(self.revision()["revision"], base["revision"] + 1)
        with self.almacen(recuperar=False) as alm:
            eventos = alm.diario()
        secuencias = [ev["secuencia"] for ev in eventos]
        self.assertEqual(secuencias, sorted(set(secuencias)),
                         "el diario tiene secuencias repetidas o desordenadas")
        with self.almacen() as alm:
            alm.verificar_integridad()
            alm.auditar()

    def test_63_agotar_reintentos_no_toca_el_estado_y_deja_registro(self):
        """T176 · Defecto que previene: quedarse esperando, o peor, escribir a la fuerza.

        Un proceso real retiene el `flock` del escritor. El escritor agota sus reintentos
        y, según `g.6` y `g.9`, tiene que: salir con error tipado, dejar el estado canónico
        EXACTAMENTE como estaba, y escribir la apertura del registro auxiliar.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        rev_antes = self.revision()

        listo = os.path.join(self.tmp, "cerrojo-tomado")
        relevo = os.path.join(self.tmp, "suelta-el-cerrojo")
        retenedor = subprocess.Popen(
            [sys.executable, self.retenedor_py, self.cerrojo, listo, relevo],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=ENTORNO,
            cwd=tempfile.gettempdir())
        try:
            limite = time.monotonic() + 30
            while not os.path.exists(listo) and time.monotonic() < limite:
                time.sleep(0.01)
            self.assertTrue(os.path.exists(listo), "el retenedor no llegó a tomar el cerrojo")

            proceso = self.transicion("tx-bloqueada", "items/it-2.json",
                                      {"esquema": "ads.estado/1", "n": 2})
            self.assertEqual(proceso.returncode, 1,
                             "el escritor bloqueado no falló: ¿escribió sin el cerrojo?")
            # SE EXIGE `REINTENTOS_AGOTADOS`, y ya no se admite `ESCRITOR_CONCURRENTE`.
            # Admitirlo era el agujero que la auditoría independiente encontró: es
            # justamente el código del camino que NO abre el registro de `g.9`, de modo
            # que la prueba daba por buena la rama no conforme.
            self.assertEqual(codigo_de_error(proceso), "REINTENTOS_AGOTADOS",
                             "agotar los reintentos tiene que decirlo con SU código: "
                             "`ESCRITOR_CONCURRENTE` es el camino que no abre el registro")
        finally:
            open(relevo, "w").close()
            retenedor.communicate(timeout=SEGUNDOS_DE_ESPERA)

        self.assertEqual(self.revision(), rev_antes,
                         "agotar reintentos modificó el estado canónico (`g.6` lo prohíbe)")
        with self.almacen() as alm:
            self.assertNotIn("items/it-2.json", alm.listar())
            pendientes = alm.reconciliacion_pendiente()
        self.assertTrue(pendientes,
                        "se agotaron los reintentos sin escribir el registro de `g.9`")
        self.assertTrue(any(p.get("intento") for p in pendientes),
                        "el registro auxiliar no dice cuántos intentos hubo")

    def test_64_bloqueo_abandonado_se_reclama_solo(self):
        """T176 · Defecto que previene: un almacén bloqueado para siempre por un proceso muerto.

        El §4 dice que el SO libera el `flock` cuando el proceso muere, y que el fichero de
        metadatos del bloqueo es INFORMATIVO y no decide. Se mata al retenedor con SIGKILL
        —sin `finally`, sin limpieza— y el escritor siguiente tiene que poder trabajar.
        """
        self.inicializar()
        listo = os.path.join(self.tmp, "cerrojo-tomado")
        relevo = os.path.join(self.tmp, "nunca")
        retenedor = subprocess.Popen(
            [sys.executable, self.retenedor_py, self.cerrojo, listo, relevo],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=ENTORNO,
            cwd=tempfile.gettempdir())
        limite = time.monotonic() + 30
        while not os.path.exists(listo) and time.monotonic() < limite:
            time.sleep(0.01)
        self.assertTrue(os.path.exists(listo), "el retenedor no llegó a tomar el cerrojo")
        retenedor.send_signal(signal.SIGKILL)
        retenedor.communicate(timeout=SEGUNDOS_DE_ESPERA)

        self.transicion_ok("tx-tras-el-abandono", "items/it-1.json",
                           {"esquema": "ads.estado/1", "n": 1})
        with self.almacen() as alm:
            self.assertEqual(alm.leer("items/it-1.json")["n"], 1)
            alm.verificar_integridad()

    def test_65_dos_caidas_simultaneas_no_publican_dos_veces(self):
        """T176 · Defecto que previene: dos ventanas abiertas a la vez y una recuperación que
        las mezcla.

        Dos procesos reales salen juntos y AMBOS mueren en el punto de no retorno. Sólo
        uno pudo tener el cerrojo, así que sólo uno pudo dejar una `preparada`. Tras
        recuperar, la revisión avanza como mucho UNA vez: si avanzara dos, la recuperación
        habría publicado la ventana de un escritor que nunca llegó a serializarse.
        """
        self.inicializar()
        base = self.revision()
        puerta = os.path.join(self.tmp, "abrir-la-puerta")
        entorno = dict(ENTORNO, ADS_ESTADO_FALLO="antes-del-commit-atomico")
        procesos = []
        for n in range(2):
            carga = os.path.join(self.cargas, f"d{n}.json")
            escribir_json(carga, {"esquema": "ads.estado/1", "escritor": n})
            procesos.append(subprocess.Popen(
                [sys.executable, self.puerta_py, puerta, CLI, "--repo", self.repo,
                 "transicion", "--id", f"tx-doble-{n}", "--autor", f"e{n}",
                 "--motivo", "doble caída", "--base", base["revision_id"],
                 "--escribir", f"items/it-{n}.json={carga}"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                env=entorno, cwd=tempfile.gettempdir()))
        time.sleep(0.2)
        open(puerta, "w").close()
        codigos = [p.wait(timeout=SEGUNDOS_DE_ESPERA) for p in procesos]
        for p in procesos:
            p.stdout.close()
            p.stderr.close()
        self.assertIn(CODIGO_SALIDA_CAIDA, codigos,
                      "ninguno de los dos llegó al punto de no retorno")

        with self.almacen() as alm:                              # abrir recupera
            self.assertEqual(alm.estado_de_la_ventana(), "cerrada")
            avance = alm.revision()["revision"] - base["revision"]
            self.assertIn(avance, (0, 1),
                          f"la recuperación publicó {avance} revisiones: dos ventanas "
                          f"simultáneas se publicaron, y sólo una pudo serializarse")
            self.assertLessEqual(len(alm.listar()), 1)
            alm.verificar_integridad()
            alm.auditar()


    def test_66_recuperar_al_abrir_con_ventana_abierta_agota_y_registra(self):
        """T176 · Defecto que previene: la mitad de `G-A5` que sólo se ve con ventana abierta.

        `g.6` y `G-A5` exigen que agotar los reintentos «produce el registro auxiliar». La
        auditoría independiente demostró que eso sólo se cumplía cuando la ventana estaba
        CERRADA: con otro escritor a mitad de transición —el caso EXACTO del que habla
        `g.6`—, la recuperación del arranque agotaba sus intentos y salía con
        `ESCRITOR_CONCURRENTE` **sin registro `g.9`**. Aquí se monta ese caso a propósito:
        una ventana abierta de verdad, provocada matando un proceso en el punto de no
        retorno, y el cerrojo retenido por otro proceso vivo.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        rev_antes = self.revision()

        # ventana ABIERTA de verdad: el proceso muere tras `preparada` y antes de publicar
        muerto = self.transicion("tx-v", "items/it-2.json",
                                 {"esquema": "ads.estado/1", "n": 2},
                                 fallo="antes-del-commit-atomico")
        self.assertEqual(muerto.returncode, 70, "la caída controlada no ocurrió")
        with self.almacen(recuperar=False) as alm:
            self.assertEqual(alm.estado_de_la_ventana(), "preparada")

        listo = os.path.join(self.tmp, "cerrojo-tomado-2")
        relevo = os.path.join(self.tmp, "suelta-el-cerrojo-2")
        retenedor = subprocess.Popen(
            [sys.executable, self.retenedor_py, self.cerrojo, listo, relevo],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=ENTORNO,
            cwd=tempfile.gettempdir())
        try:
            limite = time.monotonic() + 30
            while not os.path.exists(listo) and time.monotonic() < limite:
                time.sleep(0.01)
            self.assertTrue(os.path.exists(listo), "el retenedor no llegó a tomar el cerrojo")
            error = self.assertFalloCerrado(errores.ReintentosAgotados,
                                            estado.abrir, self.repo, recuperar=True)
            self.assertEqual(error.codigo, "REINTENTOS_AGOTADOS")
        finally:
            open(relevo, "w").close()
            retenedor.communicate(timeout=SEGUNDOS_DE_ESPERA)

        self.assertEqual(solo_durables(self.revision()), solo_durables(rev_antes),
                         "la recuperación que no pudo tomar el cerrojo movió el estado")
        with self.almacen() as alm:
            pendientes = alm.reconciliacion_pendiente()
        self.assertTrue(pendientes,
                        "agotar los reintentos AL RECUPERAR no dejó el registro de `g.9`: "
                        "`G-A5` no dice «al aplicar», dice al agotar los reintentos")
        self.assertTrue(any(p.get("item") for p in pendientes),
                        "el registro auxiliar no dice sobre qué item se agotaron")

    def test_67_la_cola_del_registro_nacido_por_reintentos_no_se_puede_borrar(self):
        """T178 · Defecto que previene: cerrar una pendencia borrando su última línea.

        ES EL DEFECTO QUE BLOQUEABA EL CORTE, y lo encontró la auditoría independiente. El
        contraste del registro contra el diario sólo alcanza a las aperturas que dejaron
        evento allí, y la apertura POR REINTENTOS AGOTADOS **no puede dejarlo**: quien
        agota los reintentos nunca obtuvo el cerrojo del escritor. Como una cadena de
        huellas no detecta que le quiten la COLA —el prefijo sigue encadenado—, borrar esa
        línea cerraba la pendencia en silencio y `verificar` y `auditar` decían `ok`.

        Se prueban CINCO vectores sobre el camino real, y los tres caminos de lectura.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})

        listo = os.path.join(self.tmp, "cerrojo-tomado-3")
        relevo = os.path.join(self.tmp, "suelta-el-cerrojo-3")
        retenedor = subprocess.Popen(
            [sys.executable, self.retenedor_py, self.cerrojo, listo, relevo],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=ENTORNO,
            cwd=tempfile.gettempdir())
        try:
            limite = time.monotonic() + 30
            while not os.path.exists(listo) and time.monotonic() < limite:
                time.sleep(0.01)
            self.assertTrue(os.path.exists(listo), "el retenedor no llegó a tomar el cerrojo")
            self.transicion("tx-b", "items/it-2.json", {"esquema": "ads.estado/1", "n": 2})
        finally:
            open(relevo, "w").close()
            retenedor.communicate(timeout=SEGUNDOS_DE_ESPERA)

        registro = self.ruta_estado("reconciliacion", "REGISTRO.jsonl")
        cabeza = self.ruta_estado("reconciliacion", "CABEZA.json")
        with self.almacen() as alm:
            pendientes = alm.reconciliacion_pendiente()
        self.assertTrue(pendientes, "no nació ninguna pendencia por reintentos agotados")
        self.assertTrue(os.path.exists(cabeza),
                        "el registro no tiene cabeza durable: sin ella, quitarle la cola es "
                        "indetectable, porque el prefijo sigue perfectamente encadenado")

        original = texto_de(registro)
        original_cabeza = bytes_de(cabeza)
        lineas = [l for l in original.splitlines() if l.strip()]

        def _restaurar():
            with open(registro, "w", encoding="utf-8") as fh:
                fh.write(original)
            with open(cabeza, "wb") as fh:
                fh.write(original_cabeza)

        def _escribir_registro(texto):
            with open(registro, "w", encoding="utf-8") as fh:
                fh.write(texto)

        vectores = {
            "borrar la ÚLTIMA línea": lambda: _escribir_registro(
                "".join(l + "\n" for l in lineas[:-1])),
            "borrar TODAS las líneas": lambda: _escribir_registro(""),
            "borrar la CABEZA": lambda: os.remove(cabeza),
            "truncar la CABEZA": lambda: open(cabeza, "wb").close(),
        }
        for nombre, mutar in vectores.items():
            with self.subTest(vector=nombre):
                _restaurar()
                mutar()
                # LOS TRES CAMINOS DE LECTURA, no sólo el que más se mira. Deducir la
                # pendencia de un registro al que le falta la cola NO es deducirla de forma
                # inequívoca, y `g.9` exige que lo sea.
                for orden in (["reconciliacion", "--pendientes"], ["verificar"], ["auditar"]):
                    proceso = cli(self.repo, orden)
                    self.assertEqual(
                        proceso.returncode, 1,
                        f"«{nombre}» no hizo fallar `{orden[0]}`: una pendencia se estaría "
                        f"retirando SIN la transición explícita que `g.9` y `G-A6` exigen")
                    self.assertEqual(codigo_de_error(proceso),
                                     "REGISTRO_DE_RECONCILIACION_CORRUPTO")
        _restaurar()
        with self.almacen() as alm:
            self.assertTrue(alm.reconciliacion_pendiente(),
                            "restaurar el registro íntegro tiene que devolver la pendencia")


# ===================================================================================
# T297 a T301 · `E-08` · EL ORDEN DE LOS PASOS 8 Y 9, PROTEGIDO POR UN TESTIGO DURABLE
# ===================================================================================
class OrdenDeLosPasos8y9(Caso):
    """`E-08`. El §3 dice que el orden «no admite reordenación», y hasta ahora no lo impedía
    nada observable.

    HECHO REPRODUCIDO ANTES DE CORREGIR: se invirtieron los pasos 8 y 9 de TRES formas.
    Dos de ellas —mover los bloques con sus marcadores de fallo tal cual— ponían en rojo
    esta batería. La tercera, la que respeta el SIGNIFICADO de cada punto de fallo, dejaba
    las 66 pruebas y LOS TRES escenarios E2E en VERDE sobre un almacén cuyo `REVISION.json`
    nombraba objetos que no estaban en `canonico/`, es decir, IRRECUPERABLE.

    Lo que estas pruebas ejercitan es el TESTIGO: un fichero durable que el paso 8 escribe
    con el `cid` de lo que acaba de publicar, y que el paso 9 exige encontrar y CASAR con lo
    que la revisión nueva va a declarar. Con eso, el paso 9 no puede adelantarse: cuando
    escribiría el testigo, el disco todavía tendría los `cid` viejos.
    """

    def ruta_del_testigo(self, transaccion):
        return self.ruta_estado("operacional", "tx", transaccion, "PUBLICADOS.json")

    def test_T297_el_paso_9_NO_publica_sin_el_testigo_del_paso_8(self):
        """T297 · Defecto que previene: `E-08`, invertir los pasos 8 y 9 sin que nada lo note.

        Se ejercita la PROPIEDAD por el camino real del motor: se pide publicar la revisión
        con el testigo ausente, que es exactamente el estado del disco cuando el paso 9 se
        adelanta al 8.
        """
        self.inicializar()
        with self.almacen() as alm:
            revision = alm.revision()
            with self.assertRaises(estado.EstadoCorrupto) as capturado:
                alm._publicar_revision(revision, testigo=None)
            self.assertEqual(capturado.exception.codigo, "ESTADO_CORRUPTO")
            # Y el disco no se tocó: la revisión sigue siendo la misma.
            self.assertEqual(alm.revision()["revision_id"], revision["revision_id"])

    def test_T297b_un_testigo_con_los_cid_VIEJOS_no_deja_publicar(self):
        """T297 · Defecto que previene: escribir el testigo ANTES de publicar los objetos.

        Es la inversión más capaz: quien invierte los pasos mueve el testigo con ellos. El
        testigo queda entonces escrito cuando en `canonico/` todavía están los `cid` VIEJOS,
        y el paso 9 lo rechaza porque no anota lo que la revisión nueva declara.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        with self.almacen() as alm:
            plan = [{"ruta": "items/it-1.json", "accion": "escribir",
                     "cid": "0" * 64}]
            # El testigo se escribe con lo que HAY en disco ahora mismo, que es lo viejo.
            os.makedirs(os.path.dirname(self.ruta_del_testigo("tx-inversa")),
                        exist_ok=True)
            alm._escribir_testigo_de_publicacion("tx-inversa", plan, "r-inventada")
            raiz_nueva = {"items/it-1.json": "1" * 64}      # lo que la revisión declararía
            with self.assertRaises(estado.EstadoCorrupto):
                alm._exigir_testigo_de_publicacion(
                    "tx-inversa", plan, "r-inventada", raiz_nueva)

    def test_T298_una_MEZCLA_PARCIAL_no_se_publica(self):
        """T298 · Defecto que previene: publicar la revisión con parte de los objetos fuera.

        El testigo cubre una ruta y el plan tiene dos: el paso 9 se niega. Sin esta
        comprobación, una publicación a medias se convertiría en vigente y el almacén
        quedaría declarando objetos que no existen.
        """
        self.inicializar()
        self.transicion_ok("tx-a", "items/it-1.json", {"esquema": "ads.estado/1", "n": 1})
        with self.almacen() as alm:
            plan_completo = [{"ruta": "items/it-1.json", "accion": "escribir", "cid": "x"},
                             {"ruta": "items/it-2.json", "accion": "escribir", "cid": "y"}]
            plan_parcial = plan_completo[:1]
            os.makedirs(os.path.dirname(self.ruta_del_testigo("tx-parcial")),
                        exist_ok=True)
            alm._escribir_testigo_de_publicacion("tx-parcial", plan_parcial, "r-x")
            with self.assertRaises(estado.EstadoCorrupto) as capturado:
                alm._exigir_testigo_de_publicacion(
                    "tx-parcial", plan_completo, "r-x",
                    {"items/it-1.json": "x", "items/it-2.json": "y"})
            self.assertIn("PARCIAL", str(capturado.exception))

    def test_T299_el_testigo_se_escribe_con_fsync_de_CONTENIDO_y_de_DIRECTORIO(self):
        """T299 · Defecto que previene: un testigo que un corte de corriente se lleva.

        No se lee el fuente: se INTERCEPTAN las primitivas de durabilidad y se comprueba que
        el testigo pasa por las dos —el `fsync` del fichero y el del directorio que lo
        contiene—. Un testigo sin el `fsync` del directorio tendría contenido en disco y no
        tendría nombre, que es la mitad exacta que `g.4` obliga a cerrar.
        """
        self.inicializar()
        from estado import motor as motor_estado
        from estado import rutas as rutas_estado
        ficheros, directorios = [], []
        original_fichero = rutas_estado.escribir_y_sincronizar
        original_directorio = rutas_estado.sincronizar_directorio

        def espia_fichero(ruta, datos):
            ficheros.append(ruta)
            return original_fichero(ruta, datos)

        def espia_directorio(ruta):
            directorios.append(ruta)
            return original_directorio(ruta)

        motor_estado.escribir_y_sincronizar = espia_fichero
        motor_estado.sincronizar_directorio = espia_directorio
        self.addCleanup(setattr, motor_estado, "escribir_y_sincronizar",
                        original_fichero)
        self.addCleanup(setattr, motor_estado, "sincronizar_directorio",
                        original_directorio)
        with self.almacen() as alm:
            plan = [{"ruta": "items/it-1.json", "accion": "escribir", "cid": "z"}]
            os.makedirs(os.path.dirname(self.ruta_del_testigo("tx-fsync")), exist_ok=True)
            alm._escribir_testigo_de_publicacion("tx-fsync", plan, "r-z")
        temporal = self.ruta_del_testigo("tx-fsync") + ".tmp"
        self.assertIn(temporal, ficheros,
                      "el testigo no pasó por `escribir_y_sincronizar`: su CONTENIDO no "
                      "está garantizado en disco")
        self.assertIn(os.path.dirname(self.ruta_del_testigo("tx-fsync")), directorios,
                      "no se sincronizó el DIRECTORIO del testigo: su NOMBRE no está "
                      "garantizado en disco")

    def test_T300_caida_ENTRE_los_pasos_8_y_9_y_RECUPERACION_posterior(self):
        """T300 · Defecto que previene: dar por recuperable lo que nadie ha recuperado.

        Se corta en `entre-el-paso-8-y-el-9`, que es el único punto donde los objetos ya
        están publicados con su testigo y la revisión todavía no. Se comprueba, en ese orden:
        el testigo ESTÁ en disco (el paso 8 terminó) · la revisión NO avanzó (el 9 no llegó)
        · tras recuperar, la transición se COMPLETA · y el almacén queda ÍNTEGRO.
        """
        rev_antes = self.inicializar() and self.revision()
        contenido = {"esquema": "ads.estado/1", "n": 8}
        proceso = self.transicion("tx-entre", "items/it-8.json", contenido,
                                  fallo="entre-el-paso-8-y-el-9")
        self.assertEqual(proceso.returncode, CODIGO_SALIDA_CAIDA,
                         "el corte entre los pasos 8 y 9 no cortó: "
                         + (proceso.stderr or proceso.stdout)[:200])
        # 1 · el paso 8 TERMINÓ: su testigo está en disco.
        self.assertTrue(os.path.isfile(self.ruta_del_testigo("tx-entre")),
                        "el paso 8 no dejó su testigo durable antes de la caída")
        # 2 · el paso 9 NO llegó: la revisión vigente sigue siendo la anterior.
        self.assertEqual(self.revision()["revision_id"], rev_antes["revision_id"],
                         "se publicó la revisión pese a caer antes del paso 9")
        # 3 · RECUPERACIÓN: la rama COMPLETAR reejecuta 8, 9 y 10.
        with self.almacen() as alm:
            self.assertEqual(alm.estado_de_la_ventana(), "cerrada")
            self.assertEqual(alm.revision()["revision"], rev_antes["revision"] + 1)
            self.assertEqual(alm.leer("items/it-8.json"), contenido)
            informe = alm.verificar_integridad()
            self.assertTrue(informe.ok, informe.a_dict())
            alm.auditar()
        self.assertIn("transicion.confirmada", self.tipos_del_diario())

    def test_T301_borrar_el_testigo_impide_completar_a_ciegas(self):
        """T301 · Defecto que previene: que la RECUPERACIÓN se salte la garantía del orden.

        La rama COMPLETAR reejecuta los pasos 8, 9 y 10. Si sólo el camino feliz exigiera el
        testigo, bastaría con caer y recuperar para publicar sin él. Se borra el testigo, se
        recupera, y la recuperación tiene que REESCRIBIRLO —porque reejecuta el paso 8— y
        dejar el almacén íntegro; nunca publicar sin él.
        """
        rev_antes = self.inicializar() and self.revision()
        contenido = {"esquema": "ads.estado/1", "n": 9}
        self.transicion("tx-sin-testigo", "items/it-9.json", contenido,
                        fallo="antes-del-commit-atomico")
        testigo = self.ruta_del_testigo("tx-sin-testigo")
        if os.path.exists(testigo):
            os.remove(testigo)
        with self.almacen() as alm:
            self.assertEqual(alm.estado_de_la_ventana(), "cerrada")
            self.assertEqual(alm.revision()["revision"], rev_antes["revision"] + 1,
                             "la recuperación no completó la transición preparada")
            self.assertEqual(alm.leer("items/it-9.json"), contenido)
            informe = alm.verificar_integridad()
            self.assertTrue(informe.ok, informe.a_dict())


# ===================================================================================
# `g.7` · EL SELLADO DEL DIARIO — T312..T319
# ===================================================================================
#
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-04:
#
#      $ grep -rniE "sellad|sellar|compacta" kernel/operativo/runtime/ --include=*.py --include=*.md
#      kernel/operativo/runtime/estado/serializacion.py:13:    COMPACTA  `separators=…`
#      $ grep -nEi "sellad|compact|umbral" kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md
#      (sin salida)
#
#  Es decir: de los cinco puntos de `g.7`, los tres primeros estaban construidos y probados
#  y los DOS ÚLTIMOS —el sellado con su umbral calibrable, y la retirada de un cuerpo por
#  transición explícita— no existían en ninguna parte. La única coincidencia del `grep` era
#  la forma COMPACTA de serialización, que es otra cosa: la forma de transporte del JSONL.
#  `g.7` estaba en la resta A del derivador de obligaciones y se daba por implementada.
#
#  Cada caso de aquí se puso ROJO reintroduciendo el defecto que comprueba. El CONTROL DEL
#  CONTROL está al final, en `test_T319c`, y no lo afirma: lo ejecuta.

class SelladoDelDiario(Caso):
    """`g.7` · el SELLADO compacta el CUERPO, y jamás el ESLABÓN."""

    UMBRAL = 6                      # cola corta a propósito: con 64 no se sellaría nada

    def ruta_diario(self):
        return self.ruta_estado("diario", "DIARIO.jsonl")

    def poblar(self, cuantas=8, operaciones=4, desde=0):
        """Transiciones MULTIARCHIVO reales, por la API, sobre el mismo control repo.

        Multiarchivo y no de una sola escritura porque lo que el sellado retira es el
        CUERPO, y el cuerpo de un evento de una transición trivial es casi todo eslabón:
        medir la compactación sobre transiciones de un fichero mediría el suelo del formato
        y no el sellado.
        """
        with self.almacen() as alm:
            for numero in range(desde, desde + cuantas):
                operaciones_ = [
                    estado.Escritura(
                        "dominio%d/objeto-%02d-%02d.json" % (numero % 2, numero, indice),
                        {"esquema": "ads.estado/1", "n": indice, "de": numero},
                    )
                    for indice in range(operaciones)
                ]
                alm.aplicar(estado.Transicion(
                    tipo="alta", base=alm.revision()["revision_id"],
                    operaciones=operaciones_, autor="agente-e",
                    motivo="alta multiarchivo numero %d, con un motivo suficientemente "
                           "largo para que el cuerpo pese" % numero,
                    id="tx-%02d" % numero,
                ))

    def sellar(self, *, umbral=None, autor="OWNER", motivo="compactación periódica",
               **kw):
        with self.almacen() as alm:
            return alm.sellar(autor=autor, motivo=motivo,
                              umbral=self.UMBRAL if umbral is None else umbral, **kw)

    # -- T312 · positivo: se compacta de verdad, y se mide -------------------------
    def test_T312_el_sellado_compacta_el_diario_y_se_mide(self):
        """T312 · Defecto que previene: un «sellado» que no retira ni un byte.

        `g.7`: «el SELLADO compacta el diario». Se MIDE el fichero antes y después, sobre
        el disco y no sobre una estructura en memoria, porque compactar es una propiedad
        del fichero. Y se comprueba que lo que se retiró es el CUERPO —`operaciones`,
        `motivo`, `autor`, `base`— y que el ESLABÓN sigue entero.
        """
        self.inicializar()
        self.poblar()
        antes = os.path.getsize(self.ruta_diario())
        eventos_antes = len(self.tipos_del_diario())

        informe = self.sellar()
        despues = os.path.getsize(self.ruta_diario())

        self.assertGreater(informe.sellados, 0,
                           "no se selló ni un evento: el umbral deja cola de sobra")
        self.assertLess(despues, antes,
                        "el diario no encogió: sellar sin compactar no es sellar, y `g.7` "
                        "dice literalmente «compacta el diario»")
        self.assertEqual(informe.bytes_antes, antes)
        self.assertEqual(informe.bytes_despues, despues)
        self.assertEqual(informe.bytes_retirados, antes - despues)

        eventos = lineas_json(self.ruta_diario())
        # NI UNA LÍNEA MENOS: sellar retira cuerpos, no eventos. Una línea de más, la del
        # `diario.sellado` que explica la retirada.
        self.assertEqual(len(eventos), eventos_antes + 1)
        self.assertEqual(eventos[-1]["tipo"], "diario.sellado")
        self.assertEqual(eventos[-1]["sellados"], informe.sellados)
        self.assertEqual(eventos[-1]["umbral"], self.UMBRAL)

        talones = [ev for ev in eventos if "sellado" in ev]
        self.assertEqual(len(talones), informe.sellados)
        for talon in talones:
            for clave in ("esquema", "secuencia", "tipo", "previo", "huella"):
                self.assertIn(clave, talon,
                              "el sellado tocó el ESLABÓN, que es lo único intocable")
            for clave in ("operaciones", "motivo", "autor", "base"):
                self.assertNotIn(clave, talon,
                                 "el cuerpo sigue ahí: no se ha retirado nada")
            self.assertIn("operaciones", talon["sellado"]["retirados"],
                          "un talón tiene que DECIR qué se le retiró")

    def test_T312b_la_cola_del_umbral_queda_intacta_y_lo_no_sellable_tambien(self):
        """T312 · Defecto que previene: sellar la ventana o el punto de no retorno.

        Los últimos `umbral` eventos NO se tocan, y `almacen.inicializado` y
        `transicion.preparada` no se tocan NUNCA, esté donde esté el umbral: la primera es
        donde arranca el linaje de `auditar()` y la segunda es el punto de no retorno cuyo
        plan lee la rama COMPLETAR de `g.8`.
        """
        self.inicializar()
        self.poblar()
        informe = self.sellar()
        eventos = lineas_json(self.ruta_diario())

        sellados = {ev["secuencia"] for ev in eventos if "sellado" in ev}
        self.assertEqual(sorted(sellados), informe.secuencias)
        # la cola: los `umbral` eventos anteriores al propio evento de sellado
        cola = [ev["secuencia"] for ev in eventos[-(self.UMBRAL + 1):-1]]
        self.assertTrue(sellados.isdisjoint(cola),
                        "se selló dentro de la cola que el umbral reserva")
        for evento in eventos:
            if evento["tipo"] in ("almacen.inicializado", "transicion.preparada"):
                self.assertNotIn("sellado", evento,
                                 "se selló `%s`, que la auditoría y la recuperación leen "
                                 "entero" % evento["tipo"])

    # -- T313 · la cadena sigue verificándose --------------------------------------
    def test_T313_la_cadena_de_huellas_y_la_auditoria_sobreviven_al_sellado(self):
        """T313 · Defecto que previene: un sellado que rompe la cadena o la auditoría.

        La restricción que MANDA: sellar no puede romper la verificabilidad del eslabón.
        Se ejercitan las cuatro puertas que leen el diario entero —`eventos()`,
        `exigir_coherente()`, `verificar_integridad()` y `auditar()`— y además
        `detectar_bifurcacion`, que reconstruye el linaje desde el origen.
        """
        self.inicializar()
        self.poblar()
        antes = self.revision()
        self.sellar()

        with self.almacen(recuperar=False) as alm:
            eventos = alm.diario()                    # verifica eslabón a eslabón
            alm._diario.exigir_coherente(antes["diario_secuencia"])
            self.assertTrue(alm.verificar_integridad().ok)
            informe = alm.auditar()
            self.assertTrue(informe.ok, informe.a_dict())
            self.assertEqual(informe.cid_raiz_reproducido, antes["cid_raiz"],
                             "la auditoría ya no reproduce `cid_raiz` desde el diario: el "
                             "sellado se llevó lo que `g.13` necesita")
            self.assertEqual(
                alm.detectar_bifurcacion(antes)["relacion"], "identica",
                "el linaje dejó de reconstruirse tras el sellado")
        # y la cadena de `previo` sigue casando, comprobada aquí y no sólo en el motor
        previo = None
        for evento in eventos:
            self.assertEqual(evento.get("previo"), previo,
                             "la cadena de huellas se rompió en la secuencia %s"
                             % evento["secuencia"])
            previo = evento["huella"]

    def test_T313b_un_almacen_sellado_sigue_admitiendo_transiciones(self):
        """T313 · Defecto que previene: un diario que tras sellarse ya no se puede anexar.

        Anexar toma la huella de la ÚLTIMA línea; si el sellado la hubiera dejado
        inservible, la primera transición posterior fallaría. Se sella DOS veces con
        transiciones en medio, porque el segundo sellado es el que ancla talones nuevos
        junto a los viejos.
        """
        self.inicializar()
        self.poblar(cuantas=6)
        self.sellar()
        self.poblar(cuantas=6, desde=6)
        segundo = self.sellar(motivo="segunda compactación")
        self.assertGreater(segundo.sellados, 0)
        with self.almacen() as alm:
            self.assertTrue(alm.auditar().ok)
            self.assertTrue(alm.verificar_integridad().ok)
        self.poblar(cuantas=1, desde=12)
        with self.almacen() as alm:
            self.assertTrue(alm.auditar().ok)
            self.assertEqual(alm.leer("dominio0/objeto-12-00.json")["de"], 12)

    # -- T314 · la recuperación, en sus DOS ramas ----------------------------------
    def _historia_sellada(self):
        """Un almacén con historia YA SELLADA, listo para que le inyecten una caída."""
        self.inicializar()
        self.poblar()
        informe = self.sellar()
        self.assertGreater(informe.sellados, 0)
        return self.revision()

    def test_T314_la_rama_REVERTIR_funciona_sobre_un_diario_sellado(self):
        """T314 · Defecto que previene: sellar y perder la recuperación de `g.8`.

        Rama REVERTIR: se cae ANTES del punto de no retorno sobre un almacén cuyo diario ya
        está sellado. La transición se pierde, nada se publica, y el diario sellado tiene
        que seguir explicándolo.
        """
        rev = self._historia_sellada()
        proceso = self.transicion("tx-caida", "items/it-9.json",
                                  {"esquema": "ads.estado/1", "n": 9},
                                  fallo="antes-de-escribir-temporal")
        self.assertEqual(proceso.returncode, CODIGO_SALIDA_CAIDA)
        with self.almacen() as alm:                            # abrir recupera
            self.assertEqual(alm.estado_de_la_ventana(), "cerrada")
            self.assertEqual(alm.revision()["revision_id"], rev["revision_id"],
                             "se publicó sobre un diario sellado una transición que debía "
                             "revertirse")
            self.assertNotIn("items/it-9.json", alm.listar())
            self.assertTrue(alm.verificar_integridad().ok)
            self.assertTrue(alm.auditar().ok)
        self.assertIn("transicion.revertida", self.tipos_del_diario())

    def test_T314b_la_rama_COMPLETAR_funciona_sobre_un_diario_sellado(self):
        """T314 · Defecto que previene: sellar y perder la otra mitad de `g.8`.

        Rama COMPLETAR: se cae ENTRE los pasos 8 y 9, pasado el punto de no retorno, sobre
        un almacén sellado. La recuperación tiene que republicar y confirmar leyendo la
        `transicion.preparada`, que es justamente la que el sellado no toca nunca.
        """
        rev = self._historia_sellada()
        contenido = {"esquema": "ads.estado/1", "n": 9}
        proceso = self.transicion("tx-caida", "items/it-9.json", contenido,
                                  fallo="entre-el-paso-8-y-el-9")
        self.assertEqual(proceso.returncode, CODIGO_SALIDA_CAIDA)
        with self.almacen() as alm:
            self.assertEqual(alm.estado_de_la_ventana(), "cerrada")
            self.assertEqual(alm.revision()["revision"], rev["revision"] + 1,
                             "la transición preparada no se completó sobre el diario "
                             "sellado")
            self.assertEqual(alm.leer("items/it-9.json"), contenido)
            self.assertTrue(alm.verificar_integridad().ok)
            self.assertTrue(alm.auditar().ok)
        self.assertIn("transicion.confirmada", self.tipos_del_diario())

    # -- T315 · la ventana no se sella ---------------------------------------------
    def test_T315_una_transaccion_en_su_ventana_no_se_sella(self):
        """T315 · Defecto que previene: compactar la ventana que `g.8` necesita leer.

        Con una transacción abierta y sin cerrar, sellar se NIEGA —`SELLADO_IMPOSIBLE`— y
        no toca ni un byte del diario. Y aunque se sellara, la regla por evento tampoco
        dejaría: se comprueba también sobre `sellables()`, que es quien decide.
        """
        self.inicializar()
        self.poblar()
        proceso = self.transicion("tx-abierta", "items/it-9.json",
                                  {"esquema": "ads.estado/1", "n": 9},
                                  fallo="antes-de-escribir-temporal")
        self.assertEqual(proceso.returncode, CODIGO_SALIDA_CAIDA)

        antes = bytes_de(self.ruta_diario())
        with self.almacen(recuperar=False) as alm:
            self.assertEqual(alm.estado_de_la_ventana(), "abierta")
            error = self.assertFalloCerrado(
                errores.SelladoImposible, alm.sellar,
                autor="OWNER", motivo="compactar con la ventana abierta",
                umbral=self.UMBRAL)
            self.assertEqual(error.codigo, "SELLADO_IMPOSIBLE")
            # y la regla POR EVENTO, que es la que de verdad protege: ninguna secuencia de
            # la transacción sin cerrar entra en la lista de sellables
            eventos = alm._diario.eventos(tolerar_cola=True)
            # `umbral=None` A PROPÓSITO: con la cola del umbral puesta, los eventos de la
            # transacción viva caen dentro de ella y quedarían fuera del sellado por ser
            # RECIENTES, no por estar abiertos. La prueba pasaría igual con la regla de la
            # ventana saboteada —se comprobó— y no probaría lo que dice probar. Sin cola,
            # lo único que los protege es la regla de la ventana.
            sellables = alm._diario.sellables(eventos, umbral=None)
            abiertas = [ev["secuencia"] for ev in eventos
                        if ev.get("transaccion") == "tx-abierta"]
            self.assertTrue(abiertas, "la caída no dejó ninguna ventana que probar")
            self.assertTrue(set(sellables).isdisjoint(abiertas),
                            "se iba a sellar un evento de una transacción sin cerrar: "
                            "`g.8` lee ese cuerpo para revertir")
        self.assertEqual(bytes_de(self.ruta_diario()), antes,
                         "el sellado rechazado tocó el diario igualmente")

    # -- T316 · el umbral, calibrable y con fallo cerrado --------------------------
    def contrato_con(self, cuerpo):
        """Una sede ALTERNATIVA del contrato derivado, para calibrar en la prueba."""
        ruta = os.path.join(self.tmp, "CONTRATO-%d.md" % len(os.listdir(self.tmp)))
        with open(ruta, "w", encoding="utf-8") as fichero:
            fichero.write("# contrato de prueba\n\n" + cuerpo + "\n")
        return ruta

    def test_T316_el_umbral_se_lee_del_contrato_derivado_y_es_calibrable(self):
        """T316 · Defecto que previene: un umbral que es una constante del código.

        `g.7`: «su umbral es parámetro CALIBRABLE del contrato derivado». Calibrable
        significa que cambia SIN TOCAR CÓDIGO: se cambia el número en el contrato y el
        sellado sella otra cosa. Se comprueba con dos sedes que sólo difieren en el número.
        """
        # el contrato que viaja con el aparato declara un umbral utilizable
        self.assertGreaterEqual(diario_mod.umbral_de_sellado(), diario_mod.MINIMO_DE_LA_COLA)

        bloque = '```json\n{\n  "esquema": "ads.estado.calibracion/1",\n' \
                 '  "sellado_umbral_eventos": %d\n}\n```'
        estrecho = self.contrato_con(bloque % 4)
        ancho = self.contrato_con(bloque % 40)
        self.assertEqual(diario_mod.umbral_de_sellado(estrecho), 4)
        self.assertEqual(diario_mod.umbral_de_sellado(ancho), 40)

        self.inicializar()
        self.poblar()
        with self.almacen() as alm:
            informe = alm.sellar(autor="OWNER", motivo="calibrado ancho", contrato=ancho)
            self.assertEqual(informe.umbral, 40)
            anchos = informe.sellados
            informe = alm.sellar(autor="OWNER", motivo="calibrado estrecho",
                                 contrato=estrecho)
            self.assertEqual(informe.umbral, 4)
        self.assertGreater(informe.sellados, 0,
                           "cambiar el umbral en el contrato no cambió lo que se sella: el "
                           "parámetro no es calibrable, es decorado")
        self.assertLess(anchos, anchos + informe.sellados)

    def test_T316b_un_umbral_ausente_ilegible_o_absurdo_es_fallo_cerrado(self):
        """T316 · Defecto que previene: un valor por omisión silencioso.

        Los cuatro casos que el hallazgo nombra, cada uno con su error TIPADO y su código
        estable. Un umbral que no está NO se sustituye por uno de fábrica: si se sustituyera,
        el contrato dejaría de ser la sede y el código volvería a serlo.
        """
        bloque = '```json\n{\n  "esquema": "ads.estado.calibracion/1",\n' \
                 '  "sellado_umbral_eventos": %s\n}\n```'
        sedes = {
            "ausente": self.contrato_con("sin bloque de calibración ninguno"),
            "sin la clave": self.contrato_con(
                '```json\n{\n  "esquema": "ads.estado.calibracion/1"\n}\n```'),
            "cero": self.contrato_con(bloque % "0"),
            "negativo": self.contrato_con(bloque % "-7"),
            "no entero": self.contrato_con(bloque % '"cuatro"'),
            "fraccionario": self.contrato_con(bloque % "4.5"),
            "ilegible": self.contrato_con('```json\n{ esto no es JSON,\n```'),
            "declarado dos veces": self.contrato_con(
                (bloque % "8") + "\n\ntexto entre medias\n\n" + (bloque % "9")),
        }
        for caso, sede in sorted(sedes.items()):
            error = self.assertFalloCerrado(
                errores.UmbralDeSelladoInvalido, diario_mod.umbral_de_sellado, sede)
            self.assertEqual(error.codigo, "UMBRAL_DE_SELLADO_INVALIDO",
                             "el umbral %s no falló con su código propio" % caso)
            self.assertNotIn(self.tmp, str(error),
                             "el error publica la ruta absoluta del temporal")
        # y una sede que NO existe tampoco se rellena con nada
        self.assertFalloCerrado(errores.UmbralDeSelladoInvalido,
                                diario_mod.umbral_de_sellado,
                                os.path.join(self.tmp, "no-existe.md"))

    def test_T316c_el_umbral_absurdo_pasado_a_mano_tampoco_pasa(self):
        """T316 · Defecto que previene: validar la sede y no el valor que se usa.

        El umbral también entra por la llamada —para calibrar una compactación concreta— y
        ahí se valida igual: si sólo se comprobara al leer el contrato, pasar `0` por la
        API sería la puerta de atrás que anula la comprobación.
        """
        self.inicializar()
        self.poblar(cuantas=4)
        with self.almacen() as alm:
            for valor in (0, -1, "cuatro", 4.5, True, 2):
                error = self.assertFalloCerrado(
                    errores.UmbralDeSelladoInvalido, alm.sellar,
                    autor="OWNER", motivo="umbral absurdo", umbral=valor)
                self.assertEqual(error.codigo, "UMBRAL_DE_SELLADO_INVALIDO",
                                 "el umbral %r no falló cerrado" % (valor,))
        proceso = cli(self.repo, ["sellar", "--autor", "OWNER", "--motivo", "m",
                                  "--umbral", "0"])
        self.assertEqual(proceso.returncode, 1,
                         "el punto ejecutable no devolvió el código del fallo tipado")
        self.assertEqual(codigo_de_error(proceso), "UMBRAL_DE_SELLADO_INVALIDO")

    # -- T317 · retirar exige transición -------------------------------------------
    def test_T317_retirar_un_cuerpo_sin_transicion_es_fallo_cerrado(self):
        """T317 · Defecto que previene: un borrado disfrazado de sellado.

        `g.7`: «retirar el cuerpo de un evento sellado exige una transición EXPLÍCITA Y
        AUDITABLE». Sin `autor` y sin `motivo` no hay transición auditable: se sabría qué se
        retiró y no quién lo decidió ni por qué. Es la misma exigencia que `Transicion`
        impone al estado canónico, y por la misma razón.
        """
        self.inicializar()
        self.poblar(cuantas=4)
        antes = bytes_de(self.ruta_diario())
        with self.almacen() as alm:
            for autor, motivo in (("", "m"), ("   ", "m"), (None, "m"),
                                  ("OWNER", ""), ("OWNER", "  "), ("OWNER", None)):
                error = self.assertFalloCerrado(
                    errores.RetiradaSinTransicion, alm.sellar,
                    autor=autor, motivo=motivo, umbral=self.UMBRAL)
                self.assertEqual(error.codigo, "RETIRADA_SIN_TRANSICION")
        self.assertEqual(bytes_de(self.ruta_diario()), antes,
                         "una retirada rechazada tocó el diario")

    def test_T317b_un_cuerpo_vaciado_a_mano_se_caza_al_leer(self):
        """T317 · Defecto que previene: vaciar un cuerpo conservando la huella.

        Es el ataque que la cadena de `previo` NO detecta por sí sola: quitar el cuerpo y
        dejar la huella no rompe ningún eslabón, porque la huella de un talón no se
        recalcula. Lo que lo caza es que no haya ningún `diario.sellado` que lo explique,
        que es exactamente la transición que `g.7` exige.
        """
        self.inicializar()
        self.poblar(cuantas=4)
        eventos = lineas_json(self.ruta_diario())
        indice = next(i for i, ev in enumerate(eventos)
                      if ev["tipo"] == "transicion.confirmada")
        eventos[indice] = {
            "esquema": eventos[indice]["esquema"], "secuencia": eventos[indice]["secuencia"],
            "tipo": eventos[indice]["tipo"], "transaccion": eventos[indice]["transaccion"],
            "resultado": eventos[indice]["resultado"],
            "sellado": {"esquema": 1, "cuerpo": "sha256:" + "0" * 64,
                        "retirados": ["operaciones"]},
            "previo": eventos[indice]["previo"], "huella": eventos[indice]["huella"],
        }
        with open(self.ruta_diario(), "w", encoding="utf-8") as fichero:
            for evento in eventos:
                fichero.write(json.dumps(evento, sort_keys=True, ensure_ascii=False,
                                         separators=(",", ":")) + "\n")
        with self.almacen(recuperar=False) as alm:
            error = self.assertFalloCerrado(errores.DiarioCorrupto, alm.diario)
            self.assertEqual(error.codigo, "DIARIO_CORRUPTO")
            self.assertIn("diario.sellado", error.detalle,
                          "el error no nombra la transición que falta")

    # -- T318 · lo que la recuperación necesita no se retira ------------------------
    def test_T318_retirar_un_cuerpo_que_la_recuperacion_necesita_es_fallo_cerrado(self):
        """T318 · Defecto que previene: una retirada dirigida que se salta las reglas.

        La retirada DIRIGIDA no consulta el umbral —es un acto de autoridad sobre un evento
        concreto—, pero pasa por las MISMAS comprobaciones de conservación. Se prueban las
        tres que importan: la ventana de `g.8`, el punto de no retorno que la rama COMPLETAR
        lee, y el arranque del linaje que `auditar()` necesita.
        """
        self.inicializar()
        self.poblar(cuantas=3)
        proceso = self.transicion("tx-abierta", "items/it-9.json",
                                  {"esquema": "ads.estado/1", "n": 9},
                                  fallo="antes-de-escribir-temporal")
        self.assertEqual(proceso.returncode, CODIGO_SALIDA_CAIDA)

        antes = bytes_de(self.ruta_diario())
        with self.almacen(recuperar=False) as alm:
            eventos = alm._diario.eventos(tolerar_cola=True)
            por_tipo = {}
            for evento in eventos:
                por_tipo.setdefault(evento["tipo"], []).append(evento["secuencia"])
            abierta_viva = [ev["secuencia"] for ev in eventos
                            if ev.get("transaccion") == "tx-abierta"]
            casos = {
                "la ventana de `g.8`": abierta_viva[:1],
                "el punto de no retorno": por_tipo["transicion.preparada"][:1],
                "el arranque del linaje": por_tipo["almacen.inicializado"][:1],
                "un evento que no existe": [999],
            }
            for nombre, secuencias in sorted(casos.items()):
                self.assertTrue(secuencias, "el caso «%s» no tiene evento" % nombre)
                error = self.assertFalloCerrado(
                    errores.RetiradaNoAdmisible, alm._diario.retirar_cuerpo,
                    secuencias, autor="OWNER", motivo="retirada dirigida")
                self.assertEqual(error.codigo, "RETIRADA_NO_ADMISIBLE",
                                 "«%s» no falló con su código propio" % nombre)
        self.assertEqual(bytes_de(self.ruta_diario()), antes,
                         "una retirada no admisible tocó el diario igualmente")

    def test_T318b_la_retirada_con_transicion_deja_rastro_auditable(self):
        """T318 · Defecto que previene: retirar sin dejar quién y por qué.

        La cara positiva de `g.7`: la retirada admisible SÍ ocurre, y deja en el propio
        diario un evento que dice quién la decidió, por qué, qué secuencias se llevó y qué
        ancla las verifica. Se comprueba que el rastro ESTÁ, y que el almacén sigue íntegro.
        """
        self.inicializar()
        self.poblar(cuantas=4)
        with self.almacen() as alm:
            eventos = alm._diario.eventos()
            objetivo = next(ev["secuencia"] for ev in eventos
                            if ev["tipo"] == "transicion.confirmada")
            informe = alm._diario.retirar_cuerpo(
                [objetivo], autor="OWNER",
                motivo="retirada dirigida de un cuerpo ya innecesario")
        self.assertEqual(informe.secuencias, [objetivo])
        self.assertLess(informe.bytes_despues, informe.bytes_antes)

        eventos = lineas_json(self.ruta_diario())
        rastro = [ev for ev in eventos if ev["tipo"] == "diario.sellado"]
        self.assertEqual(len(rastro), 1, "la retirada no dejó rastro en el diario")
        self.assertEqual(rastro[0]["autor"], "OWNER")
        self.assertEqual(rastro[0]["motivo"],
                         "retirada dirigida de un cuerpo ya innecesario")
        self.assertEqual(rastro[0]["desde"], objetivo)
        self.assertEqual(rastro[0]["hasta"], objetivo)
        self.assertEqual(rastro[0]["sellados"], 1)
        self.assertTrue(rastro[0]["cid_sellados"].startswith("sha256:"))
        talon = next(ev for ev in eventos if ev["secuencia"] == objetivo)
        self.assertIn("sellado", talon)
        with self.almacen() as alm:
            self.assertTrue(alm.verificar_integridad().ok)
            self.assertTrue(alm.auditar().ok)

    def test_T318c_el_punto_ejecutable_sella_con_la_misma_disciplina(self):
        """T318 · Defecto que previene: un camino del motor que sólo existe en la API.

        `ads_estado.py` es el punto ejecutable del motor y el sellado se invoca desde ahí,
        con los MISMOS códigos de salida que las otras doce órdenes: 0 el éxito, 1 el fallo
        tipado del kernel, 2 el uso incorrecto.
        """
        self.inicializar()
        self.poblar()
        antes = os.path.getsize(self.ruta_diario())
        proceso = cli(self.repo, ["sellar", "--autor", "OWNER", "--motivo",
                                  "compactación desde el punto ejecutable",
                                  "--umbral", str(self.UMBRAL), "--json"])
        self.assertEqual(proceso.returncode, 0, proceso.stderr)
        informe = json.loads(proceso.stdout)
        self.assertGreater(informe["sellados"], 0)
        self.assertEqual(informe["bytes_antes"], antes)
        self.assertLess(os.path.getsize(self.ruta_diario()), antes)
        self.assertNotIn(self.repo, proceso.stdout + proceso.stderr,
                         "la salida publica la ruta absoluta del control repo")

        # uso incorrecto: sin `--motivo` no hay transición que firmar, y argparse lo para
        proceso = cli(self.repo, ["sellar", "--autor", "OWNER"])
        self.assertEqual(proceso.returncode, 2)
        # retirada dirigida inadmisible: fallo TIPADO, código 1
        proceso = cli(self.repo, ["sellar", "--autor", "OWNER", "--motivo", "m",
                                  "--secuencia", "1"])
        self.assertEqual(proceso.returncode, 1)
        self.assertEqual(codigo_de_error(proceso), "RETIRADA_NO_ADMISIBLE")
        # y las órdenes del resto del motor siguen funcionando sobre el diario sellado
        for orden in (["verificar"], ["auditar"], ["revision"], ["recuperar"]):
            proceso = cli(self.repo, orden)
            self.assertEqual(proceso.returncode, 0,
                             "`%s` falló sobre un diario sellado: %s"
                             % (orden[0], proceso.stderr))

    # -- T319 · alterar un evento sellado se caza ----------------------------------
    def _alterar_talon(self, mutar):
        eventos = lineas_json(self.ruta_diario())
        indice = next(i for i, ev in enumerate(eventos) if "sellado" in ev)
        mutar(eventos[indice])
        with open(self.ruta_diario(), "w", encoding="utf-8") as fichero:
            for evento in eventos:
                fichero.write(json.dumps(evento, sort_keys=True, ensure_ascii=False,
                                         separators=(",", ":")) + "\n")
        return eventos[indice]

    def test_T319_alterar_un_evento_sellado_lo_caza_la_verificacion(self):
        """T319 · Defecto que previene: un talón editable sin que nada lo note.

        La huella de un talón no se recalcula —su contenido es justo lo retirado—, así que
        sin el ancla del `diario.sellado` un talón sería editable a mano con la cadena
        intacta. El ancla es el `cid` de la lista de pares `[secuencia, cid del talón
        entero]`: cualquier byte que cambie en cualquier talón —el resumen del sellado, un
        campo conservado o un campo REPUESTO— cambia el ancla y no casa.
        """
        alteraciones = {
            "el `cuerpo` retirado": lambda ev: ev["sellado"].__setitem__(
                "cuerpo", "sha256:" + "1" * 64),
            "la `huella` conservada": lambda ev: ev.__setitem__(
                "huella", "sha256:" + "2" * 64),
            "el `resultado` conservado": lambda ev: ev.__setitem__(
                "resultado", "sha256:" + "3" * 64),
            "reponer un cuerpo retirado": lambda ev: ev.__setitem__("motivo", "otro"),
        }
        for nombre, mutar in sorted(alteraciones.items()):
            with self.subTest(alteracion=nombre):
                self.setUp()
                self.inicializar()
                self.poblar(cuantas=4)
                self.sellar()
                self._alterar_talon(mutar)
                with self.almacen(recuperar=False) as alm:
                    error = self.assertFalloCerrado(errores.DiarioCorrupto, alm.diario)
                    self.assertEqual(error.codigo, "DIARIO_CORRUPTO")

    def test_T319b_quitar_el_ancla_deja_los_talones_sin_explicacion(self):
        """T319 · Defecto que previene: retirar la transición y quedarse los talones.

        Si alguien borra el evento `diario.sellado` para que nadie sepa quién retiró qué, lo
        que queda es un diario con cuerpos retirados y ninguna transición que los explique.
        Se caza dos veces: por la cadena —falta una línea— y, si se renumerara, porque los
        talones se quedan sin ancla.
        """
        self.inicializar()
        self.poblar(cuantas=4)
        self.sellar()
        eventos = lineas_json(self.ruta_diario())
        self.assertEqual(eventos[-1]["tipo"], "diario.sellado")
        with open(self.ruta_diario(), "w", encoding="utf-8") as fichero:
            for evento in eventos[:-1]:
                fichero.write(json.dumps(evento, sort_keys=True, ensure_ascii=False,
                                         separators=(",", ":")) + "\n")
        with self.almacen(recuperar=False) as alm:
            error = self.assertFalloCerrado(errores.DiarioCorrupto, alm.diario)
            self.assertIn("diario.sellado", error.detalle)

    def test_T319c_control_del_control_del_ancla_del_sellado(self):
        """T319 · CONTROL DEL CONTROL: se retira la comprobación y se mira qué se pone rojo.

        No se afirma que las pruebas de arriba sirvan: se DEMUESTRA. Se sustituye
        `_verificar_sellado` por una que no comprueba nada —que es exactamente el defecto de
        no haber construido el sellado— y se ejecutan los dos casos que dependen de ella. Si
        siguieran pasando, serían decorado.
        """
        self.inicializar()
        self.poblar(cuantas=4)
        self.sellar()
        self._alterar_talon(lambda ev: ev["sellado"].__setitem__(
            "cuerpo", "sha256:" + "1" * 64))

        # con la comprobación PUESTA: rojo, es decir, el motor lo caza
        with self.almacen(recuperar=False) as alm:
            self.assertFalloCerrado(errores.DiarioCorrupto, alm.diario)

        original = estado.diario.Diario._verificar_sellado
        estado.diario.Diario._verificar_sellado = lambda self, eventos: None
        try:
            with self.almacen(recuperar=False) as alm:
                # sin la comprobación, el diario alterado pasa como bueno: eso es lo que
                # había antes de esta corrección, y es el defecto exacto que `g.7` describe
                alm.diario()
        finally:
            estado.diario.Diario._verificar_sellado = original
        with self.almacen(recuperar=False) as alm:
            self.assertFalloCerrado(errores.DiarioCorrupto, alm.diario)


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    La salida de estas pruebas se PUBLICA como evidencia, y la regla del repositorio es
    que los artefactos generados sean deterministas: `git status` tiene que quedar vacío
    tras regenerarlos. «Ran 29 tests in 1.697s» cambia en cada ejecución y ensuciaría el
    árbol en cada comprobación, hasta que alguien dejara de mirarlo.
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
