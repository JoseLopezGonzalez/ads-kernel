#!/usr/bin/env python3
"""test_estado_entre_ramas — el estado durable de DOS ramas del mismo control repo, clasificado.

Mide `estado/ramas.py` y `ads_estado.py divergencia` (`CONTRATO-ESTADO-DURABLE` §6 bis)
EJECUTANDO: repositorios Git reales, almacenes reales inicializados por el motor,
transacciones aplicadas por el motor sobre ramas distintas, un diario manipulado en un
commit y una ventana de publicación abierta producida matando de verdad al escritor con
`ADS_ESTADO_FALLO`. Ninguna prueba se limita a mirar.

    T480  cinco clases de colisión de estado entre ramas, una por caso construido
    T481  la CLI publica la clase y no resuelve; un diario manipulado y una ventana abierta son BLOQUEO
    T482  sin `canonico/` en disco se escribe; con un enlace simbólico debajo, no (defecto reproducido)

Requisitos de la Directiva del Owner de La Pesquerapp que sostiene: OWN-ADS-0226, 0223, 0224.

    python3 kernel/operativo/runtime/pruebas/test_estado_entre_ramas.py

Sale con 0 si todo pasa. La raíz se deriva de `__file__`, nunca del `cwd`.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE y `E-10` · PROCEDENCIA — el MECANISMO se copia byte a
#  byte de las demás baterías (`T330`, `T380` exigen que sea idéntico); el recital, no.
#  Esta sede nace el 2026-09-15 y su salida se publica como evidencia de `T480`-`T481`.
# ---------------------------------------------------------------------------
import os as _os_g03
import sys as _sys_g03

# LA GUARDA NO DEJA RASTRO EN EL ÁRBOL QUE JUZGA. Medido: al importar la guarda, Python
# escribía `validadores/__pycache__/aislamiento_de_arranque…pyc` en el árbol, y
# `comprobar_arranque.py` empezó a publicar «el proyecto arrastra `__pycache__`» sobre
# proyectos recién creados. Se desactiva la escritura de bytecode DURANTE la guarda y se
# devuelve al estado que tenía: lo que el punto importe después sigue cacheándose como
# siempre, y no se paga rendimiento por una comprobación que corre una vez.
_G03_BYTECODE = _sys_g03.dont_write_bytecode
_sys_g03.dont_write_bytecode = True
_G03_PROPIA = _os_g03.path.dirname(_os_g03.path.realpath(__file__))
_G03_SEDE = ""
_G03_RAIZ = _G03_PROPIA
while not _G03_SEDE:
    for _G03_CANDIDATA in (_G03_PROPIA,
                           _os_g03.path.join(_G03_RAIZ, "kernel", "operativo",
                                             "validadores")):
        if _os_g03.path.isfile(_os_g03.path.join(_G03_CANDIDATA,
                                                 "aislamiento_de_arranque.py")):
            _G03_SEDE = _G03_CANDIDATA
            break
    else:
        _G03_PADRE = _os_g03.path.dirname(_G03_RAIZ)
        if _G03_PADRE == _G03_RAIZ:
            _sys_g03.stderr.write(
                "[PROCEDENCIA_NO_FIABLE] no hay `aislamiento_de_arranque.py` ni junto a "
                "este punto ejecutable ni en el `kernel/operativo/validadores/` de ning\u00fan "
                "ancestro suyo: no se puede decidir si el arranque est\u00e1 aislado, y no se "
                "sigue\n")
            raise SystemExit(5)
        _G03_RAIZ = _G03_PADRE
_sys_g03.path.insert(0, _G03_SEDE)
import aislamiento_de_arranque as _aislamiento_g03                    # noqa: E402

AISLAMIENTO = _aislamiento_g03.exigir(__file__, __name__)
_sys_g03.dont_write_bytecode = _G03_BYTECODE

# `-I` deja FUERA de `sys.path` el directorio del guión —es lo que impide que un homónimo
# vecino se cuele— y los puntos que importan módulos hermanos lo necesitan. Se reintroduce
# por RUTA DERIVADA DE `__file__`, que no la escribe el lanzador.
if _G03_PROPIA not in _sys_g03.path:
    _sys_g03.path.insert(0, _G03_PROPIA)

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  ESTA SEDE nace el 2026-09-14 con el prólogo puesto: `T330` exige que toda batería lo
#  lleve, y su salida se PUBLICA como evidencia de los escenarios `T460`-`T475`. Un `json.py`
#  homónimo en el `PYTHONPATH` de quien la corre decidiría qué dice esa evidencia, y en esta
#  batería la evidencia es lo que sostiene que el protocolo de trabajadores funciona.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      Es la decisión de `ADJ-B2`, sin cambio: `T330` exige que el mecanismo sea IDÉNTICO en
#      todos los puntos ejecutables, y cada sede escribe qué se midió en ella.
import sys as _sys
import os as _os

_RAIZ_DEL_APARATO = _os.path.dirname(_os.path.abspath(__file__))


def _entradas_del_lanzador():
    """Lo que el LANZADOR puede meter en la ruta de importación: `PYTHONPATH` y el `cwd`."""
    sospechosas = set()
    for entrada in (_os.environ.get("PYTHONPATH") or "").split(_os.pathsep):
        if entrada:
            sospechosas.add(_os.path.realpath(entrada))
    try:
        sospechosas.add(_os.path.realpath(_os.getcwd()))
    except OSError:
        # Un `cwd` borrado bajo los pies no es motivo para no purgar el resto.
        pass
    return sospechosas


def _purgar_la_ruta_de_importacion():
    """Retira de `sys.path` lo que venga del lanzador. Devuelve cuántas entradas retiró."""
    del_lanzador = _entradas_del_lanzador()
    propia = _os.path.realpath(_RAIZ_DEL_APARATO)
    conservadas, retiradas = [], []
    for entrada in _sys.path:
        try:
            real = _os.path.realpath(entrada or _os.getcwd())
        except OSError:
            conservadas.append(entrada)
            continue
        if real != propia and real in del_lanzador:
            retiradas.append(real)
        else:
            conservadas.append(entrada)
    _sys.path[:] = conservadas
    return retiradas


RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()

# CONTROL DEL CONTROL de la purga: `os` se usa para poder purgar, así que si `os` mismo
# viniera del lanzador la purga no probaría nada. No hay forma honesta de seguir: se dice y
# se sale con el código de PROCEDENCIA.
if _os.path.realpath(_os.path.dirname(_os.__file__ or ".")) in _entradas_del_lanzador():
    _sys.stderr.write(
        "[PROCEDENCIA_NO_FIABLE] el módulo `os` procede de la ruta de importación del "
        "lanzador: este punto ejecutable no puede garantizar de dónde salen sus módulos y "
        "NO ejecuta\n")
    raise SystemExit(5)

# ---------------------------------------------------------------------------
#  la batería
# ---------------------------------------------------------------------------
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RUNTIME)

import estado  # noqa: E402
from estado import ramas  # noqa: E402
from gobierno.git import CanalGit  # noqa: E402

CLI = os.path.join(RUNTIME, "ads_estado.py")
SEGUNDOS_DE_ESPERA = 120

# Entorno HERMÉTICO para los procesos hijos: sin el entorno de quien ejecuta.
ENTORNO = {
    "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
    "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8", "TZ": "UTC",
    "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0",
}


def cli(repo, argumentos, *, fallo=None):
    """La CLI del estado en un PROCESO REAL, desde el temporal del sistema."""
    entorno = dict(ENTORNO)
    entorno["HOME"] = tempfile.gettempdir()
    if fallo:
        entorno["ADS_ESTADO_FALLO"] = fallo
    return subprocess.run(
        [sys.executable, CLI, "--repo", repo] + [str(a) for a in argumentos],
        capture_output=True, text=True, env=entorno, timeout=SEGUNDOS_DE_ESPERA,
        cwd=tempfile.gettempdir())


class Laboratorio:
    """Un control repo Git REAL con un almacén REAL, y ramas sobre las que el motor escribe."""

    def __init__(self):
        self.tmp = tempfile.mkdtemp(prefix="ads-ramas-")
        self.repo = os.path.join(self.tmp, "control")
        os.makedirs(self.repo)
        self.canal = CanalGit(self.repo)
        self.canal.ejecutar("init", "-q", "-b", "main")
        with open(os.path.join(self.repo, ".gitignore"), "w", encoding="utf-8") as f:
            f.write("estado/operacional/\n")
        estado.inicializar(self.repo)
        self.confirmar("almacen inicializado")

    def limpiar(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    # -- git ----------------------------------------------------------------
    def confirmar(self, mensaje):
        self.canal.ejecutar("add", "-A")
        self.canal.ejecutar("commit", "-q", "--allow-empty", "-m", mensaje)
        return self.canal.resolver("HEAD")

    def rama(self, nombre, desde="HEAD"):
        self.canal.ejecutar("branch", nombre, desde)

    def ir_a(self, nombre):
        # `operacional/` no está versionado: se retira antes de cambiar de rama para que
        # un bloqueo huérfano de una rama no viaje a la otra.
        shutil.rmtree(os.path.join(self.repo, "estado", "operacional"), ignore_errors=True)
        self.canal.ejecutar("checkout", "-q", nombre)

    def rama_activa(self):
        _, salida, _ = self.canal.ejecutar("rev-parse", "--abbrev-ref", "HEAD")
        return salida.decode("ascii").strip()

    # -- estado -------------------------------------------------------------
    def revision_id(self):
        with estado.abrir(self.repo) as almacen:
            return almacen.revision()["revision_id"]

    def escribir(self, ident, ruta, datos, *, motivo="prueba"):
        """Una transición REAL por el motor, y su commit en la rama activa."""
        with estado.abrir(self.repo) as almacen:
            base = almacen.revision()["revision_id"]
            almacen.aplicar(estado.Transicion(
                tipo="prueba", base=base, autor="agente-lab", motivo=motivo, id=ident,
                operaciones=[estado.Escritura(ruta, {"esquema": "ads.estado/1", "v": datos})]))
        return self.confirmar(ident)

    def escribir_y_morir(self, ident, ruta, punto):
        """La CLI muere en `punto` a mitad de publicar: deja la ventana ABIERTA, y se confirma así."""
        carga = os.path.join(self.tmp, ident + ".json")
        with open(carga, "w", encoding="utf-8") as f:
            json.dump({"esquema": "ads.estado/1", "v": ident}, f)
        proceso = cli(self.repo, ["transicion", "--tipo", "prueba", "--id", ident,
                                  "--autor", "agente-lab", "--motivo", "muere",
                                  "--base", self.revision_id(),
                                  "--escribir", ruta + "=" + carga], fallo=punto)
        assert proceso.returncode == 70, "el escritor no murió en " + punto + ": " + proceso.stderr
        return self.confirmar(ident + " (ventana abierta)")


class Caso(unittest.TestCase):
    def setUp(self):
        self.lab = Laboratorio()
        self.addCleanup(self.lab.limpiar)


class T480(Caso):
    """T480 · las cinco clases, una por caso construido, sin mutar nada."""

    def test_01_sin_interferencia_y_compatible(self):
        """T480 · Defecto que previene: descubrir en el merge que dos ramas comparten estado."""
        lab = self.lab
        lab.rama("quieta")
        lab.escribir("tx-a1", "items/a.json", 1)
        r = ramas.comparar(lab.repo, "main", "quieta")
        self.assertEqual(r["clase"], ramas.COMPATIBLE, r)
        self.assertEqual(r["relacion"], "a-avanza-sobre-b")
        self.assertEqual(r["objetos"]["a"], ["items/a.json"])
        self.assertEqual(r["objetos"]["b"], [])
        r = ramas.comparar(lab.repo, "quieta", "main")
        self.assertEqual(r["clase"], ramas.COMPATIBLE)
        self.assertEqual(r["relacion"], "b-avanza-sobre-a")
        lab.rama("gemela")
        r = ramas.comparar(lab.repo, "main", "gemela")
        self.assertEqual(r["clase"], ramas.SIN_INTERFERENCIA)
        self.assertEqual(r["relacion"], "identica")
        self.assertEqual(r["resolucion"], ramas.RESOLUCION)

    def test_02_riesgo_de_conflicto_y_conflicto_directo(self):
        """T480 · Defecto que previene: dos diarios con las mismas secuencias y distinto contenido."""
        lab = self.lab
        lab.rama("otra")
        lab.escribir("tx-main", "items/a.json", 1)
        lab.ir_a("otra")
        lab.escribir("tx-otra", "items/b.json", 2)
        rev_antes = lab.revision_id()
        r = ramas.comparar(lab.repo, "main", "otra")
        self.assertEqual(r["clase"], ramas.RIESGO_DE_CONFLICTO, r)
        self.assertEqual(r["relacion"], "bifurcada")
        self.assertEqual(r["objetos"], {"a": ["items/a.json"], "b": ["items/b.json"], "comunes": []})
        self.assertIn("RE-APLICAR", r["que_hacer"])
        # ahora `otra` escribe TAMBIÉN el objeto que `main` escribió
        lab.escribir("tx-otra-2", "items/a.json", 3)
        r = ramas.comparar(lab.repo, "main", "otra")
        self.assertEqual(r["clase"], ramas.CONFLICTO_DIRECTO, r)
        self.assertEqual(r["objetos"]["comunes"], ["items/a.json"])
        # y la comparación es simétrica en la clase
        self.assertEqual(ramas.comparar(lab.repo, "otra", "main")["clase"], ramas.CONFLICTO_DIRECTO)
        # nada se movió: ni la rama activa ni la revisión del almacén de la rama activa
        self.assertEqual(lab.rama_activa(), "otra")
        self.assertNotEqual(lab.revision_id(), rev_antes)   # movió la ESCRITURA tx-otra-2, no comparar
        rev_tras = lab.revision_id()
        ramas.comparar(lab.repo, "main", "otra")
        self.assertEqual(lab.revision_id(), rev_tras)

    def test_03_bloqueo_por_referencia_o_estado_ausentes(self):
        """T480 · Defecto que previene: adivinar una relación donde no hay estado que comparar."""
        lab = self.lab
        r = ramas.comparar(lab.repo, "main", "no-existe")
        self.assertEqual(r["clase"], ramas.BLOQUEO)
        self.assertIn("no existe", r["motivo"])
        # una rama SIN estado durable (nació antes del almacén)
        lab.canal.ejecutar("checkout", "-q", "--orphan", "vacia")
        lab.canal.ejecutar("rm", "-rq", "--cached", ".")
        shutil.rmtree(os.path.join(lab.repo, "estado"), ignore_errors=True)
        os.remove(os.path.join(lab.repo, ".gitignore"))
        with open(os.path.join(lab.repo, "README"), "w", encoding="utf-8") as f:
            f.write("sin estado\n")
        lab.confirmar("rama sin estado")
        r = ramas.comparar(lab.repo, "main", "vacia")
        self.assertEqual(r["clase"], ramas.BLOQUEO, r)
        self.assertIn("antepasado", r["motivo"])


class T481(Caso):
    """T481 · la CLI publica y no resuelve; diario manipulado y ventana abierta son BLOQUEO."""

    def test_04_la_cli_publica_la_clase_en_texto_y_en_json(self):
        """T481 · Defecto que previene: una comparación que sólo existe como API."""
        lab = self.lab
        lab.rama("otra")
        lab.escribir("tx-main", "items/a.json", 1)
        lab.ir_a("otra")
        lab.escribir("tx-otra", "items/a.json", 2)
        rev_antes = lab.revision_id()
        texto = cli(lab.repo, ["divergencia", "--ref-a", "main", "--ref-b", "otra"])
        self.assertEqual(texto.returncode, 0, texto.stderr)
        self.assertIn("clase        CONFLICTO DIRECTO", texto.stdout)
        self.assertIn("comunes      1  items/a.json", texto.stdout)
        self.assertIn("resolucion   no-se-decide-aqui", texto.stdout)
        self.assertNotIn(lab.repo, texto.stdout, "la salida no publica rutas del anfitrión")
        como_json = cli(lab.repo, ["divergencia", "--ref-a", "main", "--ref-b", "otra", "--json"])
        self.assertEqual(como_json.returncode, 0, como_json.stderr)
        datos = json.loads(como_json.stdout)
        self.assertEqual(datos["clase"], ramas.CONFLICTO_DIRECTO)
        self.assertEqual(datos["objetos"]["comunes"], ["items/a.json"])
        self.assertEqual(lab.revision_id(), rev_antes, "la CLI movió el estado al comparar")
        self.assertEqual(lab.rama_activa(), "otra")

    def test_05_un_diario_manipulado_es_bloqueo(self):
        """T481 · Defecto que previene: clasificar con tranquilidad un diario que alguien editó."""
        lab = self.lab
        lab.escribir("tx-1", "items/a.json", 1)
        lab.rama("sana")
        lab.rama("manipulada")
        lab.ir_a("manipulada")
        diario = os.path.join(lab.repo, "estado", "diario", "DIARIO.jsonl")
        with open(diario, encoding="utf-8") as f:
            lineas = f.read().splitlines()
        evento = json.loads(lineas[-1])
        evento["motivo"] = "otro motivo, misma huella"
        lineas[-1] = json.dumps(evento, ensure_ascii=False, sort_keys=True)
        with open(diario, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas) + "\n")
        lab.canal.ejecutar("add", "-A")
        lab.canal.ejecutar("commit", "-q", "-m", "diario editado a mano")
        r = ramas.comparar(lab.repo, "sana", "manipulada")
        self.assertEqual(r["clase"], ramas.BLOQUEO, r)
        self.assertIn("huella", r["motivo"])
        self.assertIn("secuencia", r["motivo"])
        # el diario sano contra sí mismo sigue siendo juzgable
        self.assertEqual(ramas.comparar(lab.repo, "sana", "main")["clase"], ramas.SIN_INTERFERENCIA)

    def test_06_una_ventana_abierta_es_bloqueo(self):
        """T481 · Defecto que previene: comparar un estado a medio publicar como si estuviera cerrado."""
        lab = self.lab
        lab.rama("cerrada")
        lab.rama("abierta")
        lab.ir_a("abierta")
        lab.escribir_y_morir("tx-muere", "items/z.json", "entre-el-paso-8-y-el-9")
        r = ramas.comparar(lab.repo, "cerrada", "abierta")
        self.assertEqual(r["clase"], ramas.BLOQUEO, r)
        self.assertIn("ventana", r["motivo"])
        self.assertIn("tx-muere", r["motivo"])
        self.assertEqual(r["ventana"], {"b": ["tx-muere"]})


class T482(Caso):
    """T482 · sin `canonico/` en disco se escribe; con un enlace debajo, no."""

    def test_07_escribir_tras_un_checkout_que_dejo_canonico_sin_directorio(self):
        """T482 · Defecto que previene (reproducido): «hay un enlace simbólico» donde no lo hay."""
        lab = self.lab
        lab.rama("vieja")
        lab.escribir("tx-1", "items/a.json", 1)
        lab.ir_a("vieja")
        canonico = os.path.join(lab.repo, "estado", "canonico")
        self.assertFalse(os.path.exists(canonico), "el laboratorio no reproduce el hecho: canonico/ sigue en disco")
        lab.escribir("tx-2", "items/b.json", 2)          # antes: RutaInvalida
        with estado.abrir(lab.repo) as almacen:
            self.assertIn("items/b.json", almacen.revision()["raiz"])

    def test_08_un_enlace_simbolico_bajo_canonico_sigue_siendo_ruta_invalida(self):
        """T482 · Control del control: la guarda que la corrección conserva."""
        lab = self.lab
        fuera = os.path.join(lab.tmp, "fuera")
        os.makedirs(fuera)
        os.symlink(fuera, os.path.join(lab.repo, "estado", "canonico", "fuga"))
        with self.assertRaises(estado.RutaInvalida):
            lab.escribir("tx-fuga", "fuga/x.json", 1)
        self.assertEqual(os.listdir(fuera), [], "se escribió fuera de canonico/ a través del enlace")


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen (salida publicada)."""

    def run(self, test):
        buffer = io.StringIO()
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
