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
    from estado import atestacion, errores, fallos
except ImportError as exc:  # el motor todavía no está: que se vea por qué
    print(f"no se encuentra el paquete `estado` bajo {RUNTIME}: {exc}", file=sys.stderr)
    raise

# El entorno de las pruebas NO hereda `ADS_ESTADO_FALLO`. Si alguien lo tuviera puesto en
# su terminal, la mitad de esta batería moriría por una causa que no es la que se está
# probando, y el informe culparía al motor.
ENTORNO = {k: v for k, v in os.environ.items() if k != "ADS_ESTADO_FALLO"}

# Los nueve puntos del §10 del contrato, escritos aquí SÓLO para poder comprobar que el
# censo que el motor declara coincide con el que la norma exige. El motor los deriva; esta
# lista existe para confrontarlos, no para sustituirlos.
PUNTOS_DEL_CONTRATO = [
    "antes-de-escribir-temporal",
    "despues-de-escribir-temporal",
    "despues-de-sincronizar-temporal",
    "antes-del-commit-atomico",
    "despues-del-commit-atomico",
    "antes-de-sincronizar-directorio",
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
