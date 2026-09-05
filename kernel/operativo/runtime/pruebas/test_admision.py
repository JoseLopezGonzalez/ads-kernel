#!/usr/bin/env python3
"""test_admision — batería del VERIFICADOR DE ADMISIÓN. Escenarios `T188`, `T189` y `T190`.

    `T188`  lectura Git segura y admisión por MUTACIÓN     `V6-01` … `V6-09`
    `T189`  perímetro, censo de zonas y la deuda `S1-02`   `V6-10` `V6-11` `V6-12`
    `T190`  matriz adversarial y fórmulas compartidas      `V6-13` `V6-14` `V6-17` `V6-18`
                                                          `V6-19`

**FUERA DE ALCANCE, declarado y no fingido:** `V6-15` (los árboles adversariales derivados de
un documento inmutable) y `V6-16` (la raíz externa productiva). De `V6-16` se demuestra la
PROPIEDAD —ejecución desde fuera del árbol, con una identidad que no puede escribir en él— y
no el despliegue.

Todo sobre repositorios Git temporales REALES, sin red, con el entorno hermético que fija
`gobierno/git.py`.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, `HALLAZGO 3` del revisor 3 en el gate del
#  2026-09-05: veintiuna baterías de `runtime/pruebas/` y `tooling/tests/` no llevaban el
#  prólogo `E-10`, y el inventario de `T330` las eximía POR SU ZONA con `motivo: "bateria"`
#  —que es la lista escrita a mano que `ADJ-B2` prohibió, sólo que escrita por directorios—.
#  Y el canal que PRODUCE la evidencia, `registrar_evidencia.py` L212, lanzaba a sus hijos
#  con `subprocess.run` SIN `env=`: el veneno del padre llegaba entero a cada batería.
#
#  Lo que esto significa aquí: la salida de esta batería se PUBLICA como evidencia y
#  sostiene el estado de escenarios. Un `hashlib` o un `json` sustituidos por quien la corre
#  deciden qué dice esa evidencia. Se aplica el remedio ENTERO que el revisor adjudicó: el
#  prólogo entra en la batería —lo que cierra también la ejecución suelta— y el runner
#  sanea el entorno de sus hijos y lo publica en la cabecera de cada evidencia.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      La misma disciplina que `E-10` sigue debajo y que `T330` comprueba: lo que protege
#      está fijado y es idéntico en todos los puntos —`T380` lo exige con su digest—, y lo
#      que se lee dice qué se midió en ESTA sede. Un recital común mentiría en la mitad de
#      las sedes; un mecanismo por sede derivaría, y el que derive de menos es el que nadie
#      mira.
#
#  DECISIÓN · la guarda va ANTES del prólogo `E-10`, y no lo sustituye
#      Alternativas: (a) sustituir `E-10` por la guarda; (b) dejar `E-10` y añadir la
#      guarda encima.
#      Se elige (b). Cierran cosas distintas: `E-10` retira del `sys.path` lo que mete el
#      lanzador —y sigue haciendo falta cuando el punto se IMPORTA, donde la guarda no
#      reejecuta—; `G-03` impide que `sitecustomize` llegue siquiera a ejecutarse. Quitar
#      `E-10` reabriría la contaminación de la ruta en el caso importado.
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
#  HECHO REPRODUCIDO ANTES DE CORREGIR, `HALLAZGO 3` del gate del 2026-09-05: esta batería
#  no llevaba el prólogo, y el inventario de `T330` la eximía por vivir en una zona de
#  pruebas. Su salida se PUBLICA como evidencia; un `json.py` o un `hashlib.py` homónimos en
#  el `PYTHONPATH` de quien la corre deciden qué dice esa evidencia, que es exactamente el
#  daño que `H-01` midió sobre `huella.py`. La deuda ya no es de zona: la exclusión
#  `motivo: "bateria"` se ha RETIRADO del inventario y esta batería es un punto ejecutable
#  como cualquier otro.
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

import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest

RAIZ_RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ_RUNTIME)

import admision                                                      # noqa: E402
from admision import censo, formulas, matriz, mutacion, perimetro, sede  # noqa: E402
from admision.perimetro import Declaracion                           # noqa: E402
from gobierno.git import CanalGit                                    # noqa: E402

# El SHA del ÁRBOL VACÍO de Git. Es una constante del formato de objetos, la misma en
# todos los repositorios, y `E-09` la usa para construir un commit REAL que no
# contiene ninguna ruta.
ARBOL_VACIO_DE_GIT = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"


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
#  REPRODUCCIÓN DE LA REGLA ANTERIOR  —  la que `S1-02` derribó
# ===========================================================================
#  NO se edita el script antiguo: `docs/evolucion/verificacion/comprobar-correccion-gate-de-
#  cierre.py` es evidencia de proceso y es inmutable. Se REPRODUCE su regla, que es lo que
#  permite comparar REGLAS y no scripts.
#
#  PROCEDENCIA EXACTA, para que se pueda contrastar:
#      · `comprobar-correccion-gate-de-cierre.py`, líneas 3110-3128: `_disco`,
#        `_publicado`, `_base_gobernada`, `_ampliaciones` y `_idos`
#      · `docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md` §3.2, que cita la fórmula
#        literal: `_ampliaciones = (_disco ∪ _publicado) − _base_gobernada`
#
#  LO QUE LA REGLA MIRA, y es todo lo que mira: la TOPOLOGÍA. Qué ficheros APARECEN y qué
#  ficheros DESAPARECEN respecto de la revisión base. El CONTENIDO de un fichero que ya
#  existía en la base no lo mira NADIE, y la RAÍZ del repositorio no está en ningún
#  inventario de contenido.
#
#  NO se le añade ninguna mejora, y eso es deliberado: si se le añadiera, la comparación
#  mediría un aparato que nunca existió.

def universo_gobernado_regla_anterior(raiz, canal, base):
    """`(ampliaciones, idos)` según la regla SÓLO-TOPOLOGÍA del aparato anterior."""
    disco = set()
    for carpeta, subcarpetas, ficheros in os.walk(raiz):
        if ".git" in subcarpetas:
            subcarpetas.remove(".git")
        for nombre in ficheros:
            completa = os.path.join(carpeta, nombre)
            disco.add(os.path.relpath(completa, raiz).replace(os.sep, "/"))
    publicado = set(canal.rutas_del_arbol("HEAD"))
    base_gobernada = set(canal.rutas_del_arbol(base))
    ampliaciones = (disco | publicado) - base_gobernada
    idos = base_gobernada - (disco | publicado)
    return ampliaciones, idos


def veredicto_regla_anterior(raiz, canal, base, admitidas=()):
    """VERDE si no hay ampliación sin clasificar ni desaparición. El CONTENIDO no se mira."""
    ampliaciones, idos = universo_gobernado_regla_anterior(raiz, canal, base)
    sin_clasificar = sorted(ampliaciones - set(admitidas))
    if sin_clasificar or idos:
        return "ROJO", {"ampliaciones": sin_clasificar, "idos": sorted(idos)}
    return "VERDE", {"ampliaciones": [], "idos": []}


# ===========================================================================
#  Cimientos comunes
# ===========================================================================
class ArbolTemporal(unittest.TestCase):
    """Un árbol Git real con la forma del corpus: raíz, canónico, owner, evidencia, packs."""

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-adm-")
        self.addCleanup(self._retirar)
        self.repo = os.path.join(self.directorio, "arbol")
        os.makedirs(self.repo)
        self.canal_git = CanalGit(self.repo)
        self.base = matriz.fundar(self.repo, self.canal_git)
        self.canal = admision.CanalDeLecturaGit(self.repo, canal=self.canal_git)

    def _retirar(self):
        for carpeta, subcarpetas, ficheros in os.walk(self.directorio):
            for nombre in subcarpetas + ficheros:
                try:
                    os.chmod(os.path.join(carpeta, nombre), stat.S_IRWXU)
                except OSError:
                    # Devolver el permiso es best-effort en el desmontaje: `rmtree` con
                    # `ignore_errors` es quien remata, y aquí no hay nada que afirmar.
                    continue
        shutil.rmtree(self.directorio, ignore_errors=True)

    def escribir(self, relativa, contenido):
        destino = os.path.join(self.repo, relativa)
        os.makedirs(os.path.dirname(destino) or self.repo, exist_ok=True)
        with open(destino, "wb") as manejador:
            manejador.write(contenido)
        return relativa

    def confirmar(self, mensaje="cambio"):
        self.canal_git.ejecutar("add", "-A")
        self.canal_git.ejecutar("commit", "--quiet", "-m", mensaje)

    def verificar(self, *, admitidas=(), ancla=None):
        declaracion = Declaracion(
            ancla=self.base if ancla is None else ancla,
            autoridad="raiz-externa-de-pruebas",
            admitidas=[{"ruta": ruta, "motivo": "declarada"} for ruta in admitidas],
        )
        return admision.verificar(self.repo, base=self.base, declaracion=declaracion,
                                  censar_el_codigo=False)


# ===========================================================================
#  T188 · lectura Git segura   ·   `V6-01` a `V6-04`
# ===========================================================================
class LecturaSegura(ArbolTemporal):

    def test_toda_lista_exige_separador_seguro(self):
        """T188 · Defecto que previene: leer una lista con un separador que cabe en una ruta."""
        with self.assertRaises(admision.LecturaInsegura) as capturado:
            self.canal._leer("ls-tree", "-r", "--name-only", "HEAD")
        self.assertIn("NUL", str(capturado.exception))

    def test_una_ruta_con_salto_de_linea_se_lee_entera(self):
        """T188 · Defecto que previene: partir en dos una ruta que lleva un salto de línea."""
        nombre = "docs/canonico/con\nsalto.md"
        self.escribir(nombre, b"contenido\n")
        self.confirmar("salto")
        rutas = self.canal.rutas_del_arbol("HEAD")
        self.assertIn(nombre, rutas)

    def test_las_seis_formas_de_nombre_se_leen_identicas(self):
        """T188 · Defecto que previene: perder una ruta por su ortografía."""
        nombres = ["docs/canonico/con espacio.md", "docs/canonico/-guion.md",
                   "docs/canonico/ñandú-中文.md", "docs/canonico/con\nsalto.md",
                   "docs/canonico/normal.md", "docs/canonico/con\ttab.md"]
        for nombre in nombres:
            self.escribir(nombre, b"x\n")
        self.confirmar("formas")
        rutas = set(self.canal.rutas_del_arbol("HEAD"))
        for nombre in nombres:
            with self.subTest(nombre=nombre.encode("unicode_escape").decode("ascii")):
                self.assertIn(nombre, rutas)

    def test_salida_truncada_es_rojo_con_diagnostico(self):
        """T188 · Defecto que previene: devolver una lista parcial como si fuera completa."""
        with self.assertRaises(admision.SalidaTruncada) as capturado:
            admision.lectura._registros(b"docs/a.md\0docs/b.md", "ls-tree")
        self.assertIn("no termina en `NUL`", str(capturado.exception))
        self.assertIn("SALIDA_TRUNCADA", str(capturado.exception))

    def test_salida_no_decodificable_se_denuncia_y_no_se_interpreta_a_medias(self):
        """T188 · Defecto que previene: `errors=replace`, que hace desaparecer rutas."""
        with self.assertRaises(admision.SalidaNoDecodificable) as capturado:
            admision.lectura._decodificar(b"docs/\xff\xfe.md", "ls-tree", 3)
        self.assertIn("registro 3", str(capturado.exception))
        self.assertIn("DENUNCIA", str(capturado.exception))

    def test_estructura_ajena_es_rojo_con_diagnostico(self):
        """T188 · Defecto que previene: leer una salida con otra forma y seguir tan tranquilo."""
        with self.assertRaises(admision.EstructuraAjena) as capturado:
            self.canal.interpretar_name_status(b"R100\0solo-una-punta\0", "base")
        self.assertIn("DOS rutas", str(capturado.exception))
        with self.assertRaises(admision.EstructuraAjena):
            self.canal.interpretar_name_status(b"Z\0ruta\0", "base")

    def test_los_tres_casos_nunca_devuelven_lista_vacia_con_exito(self):
        """T188 · Defecto que previene: confundir «no entiendo» con «no hay nada»."""
        casos = (
            (b"a\0b", admision.SalidaTruncada),
            (b"\xff\xfe\0", admision.SalidaNoDecodificable),
            (b"R100\0uno\0", admision.EstructuraAjena),
        )
        for salida, esperado in casos:
            with self.subTest(esperado=esperado.CODIGO):
                with self.assertRaises(esperado):
                    self.canal.interpretar_name_status(salida, "base")

    def test_una_ruta_no_decodificable_del_arbol_real_se_denuncia(self):
        """T188 · Defecto que previene: una ruta Latin-1 en el árbol que nadie vuelve a ver."""
        crudo = os.path.join(self.repo.encode("utf-8"), b"docs/canonico/lat\xedn1.md")
        with open(crudo, "wb") as manejador:
            manejador.write(b"x\n")
        self.confirmar("latin1")
        with self.assertRaises(admision.SalidaNoDecodificable):
            self.canal.rutas_del_arbol("HEAD")

    def test_git_que_no_responde_no_produce_lista_vacia(self):
        """T188 · Defecto que previene: tratar un fallo de Git como un árbol limpio."""
        with self.assertRaises(admision.GitNoResponde):
            self.canal.rutas_del_arbol("revision-que-no-existe")


class CensoDeLecturas(unittest.TestCase):
    """`V6-04`: el censo se DERIVA del código con `ast`, no con `grep` ni a mano."""

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-censo-")
        self.addCleanup(shutil.rmtree, self.directorio, True)

    def test_el_censo_del_aparato_real_esta_limpio(self):
        """T188 · Control POSITIVO: hoy no hay ni una lectura fuera del canal único."""
        modulos = censo.modulos_del_aparato(RAIZ_RUNTIME)
        self.assertGreater(len(modulos), 10)
        informe = censo.censar_lecturas(modulos)
        self.assertTrue(informe["ok"], informe["fuera_del_canal"]
                        + informe["sin_separador_seguro"])
        self.assertEqual(informe["fuera_del_canal"], [])
        self.assertEqual(informe["listas_fuera_del_canal"], [])
        self.assertGreater(len(informe["lecturas"]), 0)

    def test_una_lectura_escrita_fuera_del_canal_aparece_en_el_censo(self):
        """T188 · Defecto que previene: una vía paralela de invocación de Git, oculta."""
        modulo = os.path.join(self.directorio, "atajo.py")
        with open(modulo, "w", encoding="utf-8") as manejador:
            manejador.write(
                "import subprocess\n"
                "def leer():\n"
                "    return subprocess.run(['git', 'ls-files'], capture_output=True)\n"
            )
        informe = censo.censar_lecturas([modulo])
        self.assertFalse(informe["ok"])
        self.assertEqual(len(informe["fuera_del_canal"]), 1)
        self.assertEqual(informe["fuera_del_canal"][0]["modulo"], "atajo.py")
        self.assertEqual(len(informe["sin_separador_seguro"]), 1)

    def test_una_lista_sin_separador_seguro_aparece_en_el_censo(self):
        """T188 · Defecto que previene: una lectura de lista escrita sin `-z`."""
        modulo = os.path.join(self.directorio, "lectura.py")
        with open(modulo, "w", encoding="utf-8") as manejador:
            manejador.write(
                "def leer(canal):\n"
                "    return canal.ejecutar('ls-tree', '-r', '--name-only', 'HEAD')\n"
            )
        informe = censo.censar_lecturas([modulo])
        self.assertFalse(informe["ok"])
        self.assertEqual(informe["sin_separador_seguro"][0]["orden"], "ls-tree")

    def test_el_censo_no_se_denuncia_a_si_mismo_por_su_vocabulario(self):
        """T188 · Control POSITIVO: distinguir la MENCIÓN de la INVOCACIÓN, que es lo que da `ast`."""
        modulo = os.path.join(self.directorio, "vocabulario.py")
        with open(modulo, "w", encoding="utf-8") as manejador:
            manejador.write(
                "ORDENES_DE_LISTA = ('ls-tree', 'ls-files', 'diff')\n"
                "def diagnosticar(salida):\n"
                "    return _registros(salida, 'diff')\n"
                "def _registros(salida, orden):\n"
                "    return []\n"
            )
        informe = censo.censar_lecturas([modulo])
        self.assertTrue(informe["ok"])
        self.assertEqual(informe["lecturas"], [])

    def test_un_envoltorio_local_no_esconde_la_lectura(self):
        """T188 · Defecto que previene: esquivar el censo poniéndole otro nombre.

        `INVOCADORES` es una lista de NOMBRES, y una lista de nombres se esquiva escribiendo
        otro. Envolver `subprocess.run` en un `_mi_git()` local, y ése en un segundo
        envoltorio, hacía desaparecer del censo una lectura de lista sin `-z`. Es el modo de
        fallo de `S1-01` —la superficie que nadie ha enumerado— y ocurrió de verdad en
        `arboles/versiones.py`. Ahora los envoltorios se DERIVAN por cierre transitivo.
        """
        modulo = os.path.join(self.directorio, "envuelto.py")
        with open(modulo, "w", encoding="utf-8") as manejador:
            manejador.write(
                "import subprocess\n"
                "def _mi_git(raiz, *argumentos):\n"
                "    return subprocess.run(['git', '-C', raiz] + list(argumentos))\n"
                "def _rutas(raiz, *argumentos):\n"
                "    return _mi_git(raiz, *argumentos).stdout.split()\n"
                "def leer(raiz, base):\n"
                "    return _rutas(raiz, 'diff', '--name-only', base, 'HEAD')\n"
            )
        informe = censo.censar_lecturas([modulo])
        self.assertFalse(informe["ok"])
        self.assertEqual(informe["sin_separador_seguro"][0]["orden"], "diff")

    def test_la_via_historica_esta_ACOTADA_al_paquete_y_al_modulo(self):
        """T188 · Defecto que previene: que la excepción de `V6-15` sea un agujero.

        `arboles/versiones.py` puede leer Git como en su época porque ése ES el defecto que
        reproduce. La exención está acotada por `(paquete, módulo)`: el MISMO fichero en otro
        paquete NO la hereda, y otro fichero del MISMO paquete tampoco.
        """
        cuerpo = (
            "import subprocess\n"
            "def _mi_git(raiz, *argumentos):\n"
            "    return subprocess.run(['git', '-C', raiz] + list(argumentos))\n"
            "def leer(raiz, base):\n"
            "    return _mi_git(raiz, 'diff', '--name-only', base).stdout.split()\n"
        )
        # (i) el nombre exento, pero en OTRO paquete: NO hereda la exención.
        ajeno = os.path.join(self.directorio, "admision")
        os.makedirs(ajeno, exist_ok=True)
        impostor = os.path.join(ajeno, "versiones.py")
        with open(impostor, "w", encoding="utf-8") as manejador:
            manejador.write(cuerpo)
        informe = censo.censar_lecturas([impostor])
        self.assertFalse(informe["ok"], "un `versiones.py` de otro paquete NO puede heredar "
                                        "la exención histórica")
        # (ii) el paquete exento, pero OTRO fichero: tampoco.
        propio = os.path.join(self.directorio, "arboles")
        os.makedirs(propio, exist_ok=True)
        otro = os.path.join(propio, "colado.py")
        with open(otro, "w", encoding="utf-8") as manejador:
            manejador.write(cuerpo)
        informe = censo.censar_lecturas([otro])
        self.assertFalse(informe["ok"], "sólo los módulos DECLARADOS de `arboles/` están "
                                        "exentos, no el paquete entero")

    def test_la_via_historica_declarada_se_PUBLICA_en_vez_de_omitirse(self):
        """T188 · Control POSITIVO: la exención no esconde, publica.

        La lectura sin `-z` de `arboles/versiones.py` tiene que APARECER en el censo, con su
        paquete, su módulo y su motivo. Una exención que borrase la entrada sería
        indistinguible de no haber censado el paquete.
        """
        modulos = censo.modulos_del_aparato(RAIZ_RUNTIME)
        informe = censo.censar_lecturas(modulos)
        historicas = informe["lecturas_historicas"]
        self.assertTrue(historicas, "la vía histórica tiene que estar censada y publicada")
        paquetes = {entrada["paquete"] for entrada in historicas}
        self.assertEqual(paquetes, {"arboles"})
        inseguras = [e for e in historicas if not e["separador_seguro"]]
        self.assertTrue(inseguras, "la reproducción de `S1-01` es una lectura SIN `-z`, y "
                                   "el censo tiene que verla, no perderla")
        for entrada in historicas:
            self.assertIn((entrada["paquete"], entrada["modulo"]),
                          censo.SEDES_DE_REPRODUCCION_HISTORICA)


# ===========================================================================
#  T188 · admisión por MUTACIÓN   ·   `V6-05` a `V6-09`
# ===========================================================================
class AdmisionPorMutacion(ArbolTemporal):

    def test_las_cuatro_referencias_estan_declaradas(self):
        """T188 · Defecto que previene: una comprobación que declara una y usa otra."""
        declaradas = {fila["referencia"] for fila in mutacion.LECTURAS_DECLARADAS}
        self.assertEqual(declaradas, set(admision.lectura.REFERENCIAS))

    def test_una_mutacion_solo_en_el_indice_se_ve(self):
        """T188 · Defecto que previene: `git add` sin commit, invisible para la guarda."""
        self.escribir("docs/canonico/00-EMPEZAR-AQUI.md", b"# empezar\nmutado\n")
        self.canal_git.ejecutar("add", "-A")
        mutaciones = mutacion.derivar(self.canal, self.base)
        indices = [m for m in mutaciones if m.referencia == "HEAD"]
        self.assertEqual(len(indices), 1)
        self.assertEqual(indices[0].ruta, "docs/canonico/00-EMPEZAR-AQUI.md")

    def test_un_fichero_sin_rastrear_se_ve(self):
        """T188 · Defecto que previene: dejar fuera lo que no rastrea nadie."""
        self.escribir("docs/canonico/nueva.md", b"# nueva\n")
        mutaciones = mutacion.derivar(self.canal, self.base)
        trabajo = [m for m in mutaciones if m.referencia == "trabajo"]
        self.assertEqual([m.ruta for m in trabajo], ["docs/canonico/nueva.md"])

    def test_existir_en_la_base_no_exime(self):
        """T188 · Defecto que previene: `S1-02`, la preexistencia como exención (`V6-05`)."""
        self.escribir("docs/canonico/00-EMPEZAR-AQUI.md", b"# empezar\nreescrito entero\n")
        self.confirmar("mutacion de un preexistente")
        veredicto = self.verificar()
        self.assertEqual(veredicto.color, "ROJO")
        rutas = {hallazgo.ruta for hallazgo in veredicto.hallazgos}
        self.assertIn("docs/canonico/00-EMPEZAR-AQUI.md", rutas)
        clases = {fila["clase"] for fila in veredicto.informe["mutaciones"]
                  if fila["ruta"] == "docs/canonico/00-EMPEZAR-AQUI.md"}
        self.assertEqual(clases, {"preexistente"})

    def test_confirmar_no_exime(self):
        """T188 · Defecto que previene: `V6-08`, que el commit convierta un rojo en verde."""
        self.escribir("docs/canonico/nueva.md", b"# sentencia falsa\n")
        sin_confirmar = self.verificar()
        self.assertEqual(sin_confirmar.color, "ROJO")
        self.confirmar("ataque confirmado")
        confirmado = self.verificar()
        self.assertEqual(confirmado.color, "ROJO")
        codigo, salida, _ = self.canal_git.ejecutar("status", "--porcelain")
        self.assertEqual(salida.strip(), b"", "el árbol queda LIMPIO y aun así es ROJO")

    def test_un_renombrado_con_origen_no_admitido_da_rojo(self):
        """T188 · Defecto que previene: `V6-06`, juzgar `R` por una sola punta."""
        origen = os.path.join(self.repo, "docs/canonico/00-EMPEZAR-AQUI.md")
        with open(origen, "rb") as manejador:
            cuerpo = manejador.read()
        os.remove(origen)
        self.escribir("docs/canonico/00-RENOMBRADA.md", cuerpo)
        self.confirmar("renombrado")
        veredicto = self.verificar(admitidas=["docs/canonico/00-RENOMBRADA.md"])
        self.assertEqual(veredicto.color, "ROJO")
        hallazgo = veredicto.hallazgos[0]
        self.assertEqual(hallazgo.ruta, "docs/canonico/00-EMPEZAR-AQUI.md")
        self.assertIn("punta origen", hallazgo.causa)
        # Y con LAS DOS puntas declaradas, verde: la regla no es «todo rojo».
        completo = self.verificar(admitidas=["docs/canonico/00-RENOMBRADA.md",
                                             "docs/canonico/00-EMPEZAR-AQUI.md"])
        self.assertEqual(completo.color, "VERDE")

    def test_las_dos_clases_tienen_guarda(self):
        """T188 · Defecto que previene: `V6-09`, que una clase quede sin guarda."""
        self.escribir("docs/canonico/nueva.md", b"# nueva\n")
        self.escribir("docs/canonico/00-EMPEZAR-AQUI.md", b"# mutada\n")
        self.confirmar("las dos clases")
        veredicto = self.verificar()
        clases = {fila["clase"] for fila in veredicto.informe["mutaciones"]}
        self.assertEqual(clases, {"nueva", "preexistente"})
        rutas = {hallazgo.ruta for hallazgo in veredicto.hallazgos}
        self.assertEqual(rutas, {"docs/canonico/nueva.md",
                                 "docs/canonico/00-EMPEZAR-AQUI.md"})

    def test_un_arbol_sano_da_verde(self):
        """T188 · Control POSITIVO: sin mutaciones, VERDE. Un control que no puede aprobar no sirve."""
        veredicto = self.verificar()
        self.assertEqual(veredicto.color, "VERDE")
        self.assertEqual(veredicto.hallazgos, [])


# ===========================================================================
#  T189 · censo de ZONAS, auto-inclusión y sede del Owner
# ===========================================================================
class CensoDeZonas(ArbolTemporal):

    def test_el_censo_de_zonas_se_deriva_y_todas_tienen_condicion(self):
        """T189 · Defecto que previene: `V6-10`, una zona sin condición que pasa por omisión."""
        veredicto = self.verificar()
        informe = veredicto.informe["censo_de_zonas"]
        self.assertGreater(len(informe["zonas"]), 0)
        self.assertEqual(informe["sin_condicion"], [])
        self.assertEqual(informe["sin_zona"], [])
        for fila in informe["zonas"]:
            with self.subTest(patron=fila["patron"]):
                self.assertTrue(fila["declarada"])
                self.assertIsNotNone(fila["condicion"])

    def test_el_censo_del_registro_canonico_real_esta_completo(self):
        """T189 · Defecto que previene: que el registro VIVO tenga una clase sin condición."""
        raiz_repo = os.path.dirname(os.path.dirname(os.path.dirname(RAIZ_RUNTIME)))
        zonas = censo.cargar_zonas(raiz_repo)
        self.assertGreaterEqual(len(zonas), 25)
        sin_condicion = [zona.patron for zona in zonas if zona.condicion is None]
        self.assertEqual(sin_condicion, [],
                         "toda clase del registro canónico declara condición de CONTENIDO")

    def test_una_zona_sin_condicion_da_rojo(self):
        """T189 · Defecto que previene: añadir una clase nueva y que herede el verde."""
        self.escribir("docs/canonico/FUENTES-CANONICAS.yml",
                      matriz.plantilla_de_registro()
                      + b"  - patron: '^inventado/'\n"
                        b"    clase: CLASE_QUE_NADIE_HA_DECLARADO\n"
                        b"    motivo: zona nueva sin condicion\n")
        self.confirmar("zona sin condicion")
        veredicto = self.verificar(admitidas=["docs/canonico/FUENTES-CANONICAS.yml"])
        self.assertEqual(veredicto.color, "ROJO")
        puntos = {hallazgo.punto for hallazgo in veredicto.hallazgos}
        self.assertIn("V6-10", puntos)
        codigos = {hallazgo.codigo for hallazgo in veredicto.hallazgos}
        self.assertIn(admision.ZonaSinCondicion.CODIGO, codigos)

    def test_una_ruta_que_ninguna_zona_clasifica_da_rojo(self):
        """T189 · Defecto que previene: el defecto de PERÍMETRO, por tercera vez."""
        self.escribir("inventado/SENTENCIA.md", b"# fuera de toda zona\n")
        self.confirmar("zona ciega")
        veredicto = self.verificar(admitidas=["inventado/SENTENCIA.md"])
        self.assertEqual(veredicto.color, "ROJO")
        rutas = {hallazgo.ruta for hallazgo in veredicto.hallazgos}
        self.assertIn("inventado/SENTENCIA.md", rutas)


class AutoInclusion(ArbolTemporal):
    """`V6-11`: ni el verificador ni su política pueden salirse de su propio alcance."""

    def _preparar_instrumento(self):
        """Coloca el instrumento DENTRO del árbol de pruebas, con su ruta real."""
        self.escribir("kernel/operativo/runtime/admision/perimetro.py",
                      b"# el verificador\n")
        self.escribir("kernel/operativo/runtime/gobierno/POLITICA-CONTROL-REPO.yml",
                      b"version: 1\n")
        self.confirmar("instrumento en el arbol")
        self.base = self.canal.resolver("HEAD")

    def test_una_mutacion_del_verificador_da_rojo(self):
        """T189 · Defecto que previene: cambiar la regla y aprobarse con la regla nueva."""
        self._preparar_instrumento()
        self.escribir("kernel/operativo/runtime/admision/perimetro.py",
                      b"# el verificador, con una exencion nueva\n")
        self.confirmar("mutacion del instrumento")
        veredicto = self.verificar(
            admitidas=["kernel/operativo/runtime/admision/perimetro.py"]
        )
        self.assertEqual(veredicto.color, "ROJO")
        hallazgo = veredicto.hallazgos[0]
        self.assertEqual(hallazgo.punto, "V6-11")
        self.assertEqual(hallazgo.codigo, admision.InstrumentoAlterado.CODIGO)

    def test_una_mutacion_de_la_politica_da_rojo(self):
        """T189 · Defecto que previene: reescribir la política y certificarse con ella."""
        self._preparar_instrumento()
        self.escribir("kernel/operativo/runtime/gobierno/POLITICA-CONTROL-REPO.yml",
                      b"version: 1\nexento: todo\n")
        self.confirmar("mutacion de la politica")
        veredicto = self.verificar(
            admitidas=["kernel/operativo/runtime/gobierno/POLITICA-CONTROL-REPO.yml"]
        )
        self.assertEqual(veredicto.color, "ROJO")
        self.assertEqual(veredicto.hallazgos[0].punto, "V6-11")

    def test_declarar_la_mutacion_del_instrumento_no_la_exime(self):
        """T189 · Defecto que previene: salirse del alcance por la puerta de la declaración."""
        self._preparar_instrumento()
        self.escribir("kernel/operativo/runtime/admision/perimetro.py", b"# cambiado\n")
        self.confirmar("mutacion declarada")
        for admitidas in ([], ["kernel/operativo/runtime/admision/perimetro.py"]):
            with self.subTest(declarada=bool(admitidas)):
                self.assertEqual(self.verificar(admitidas=admitidas).color, "ROJO")

    def test_cero_rutas_del_instrumento_exentas(self):
        """T189 · Defecto que previene: que un prefijo del instrumento quede fuera."""
        prefijos = admision.prefijos_de_instrumento()
        for ruta in ("kernel/operativo/runtime/admision/perimetro.py",
                     "kernel/operativo/runtime/admision/formulas.py",
                     "kernel/operativo/runtime/gobierno/POLITICA-CONTROL-REPO.yml",
                     "kernel/operativo/runtime/identidad/proveedor.py",
                     "kernel/operativo/runtime/adaptadores/proceso.py",
                     "kernel/operativo/runtime/ads_admision.py"):
            with self.subTest(ruta=ruta):
                self.assertTrue(any(ruta.startswith(prefijo) for prefijo in prefijos))


class SedeDelOwner(ArbolTemporal):
    """`V6-12`: APPEND-ONLY, contrastado contra el COMMIT DE NACIMIENTO y no contra `HEAD`."""

    def test_anadir_una_resolucion_es_legitimo(self):
        """T189 · Control POSITIVO: la sede del Owner CRECE, y crecer no es alterar."""
        with open(os.path.join(self.repo, perimetro.SEDE_DEL_OWNER), "rb") as manejador:
            cuerpo = manejador.read()
        self.escribir(perimetro.SEDE_DEL_OWNER, cuerpo + b"\n## O2\n\notra resolucion\n")
        self.confirmar("nueva resolucion")
        self.assertEqual(self.verificar().color, "VERDE")

    def test_alterar_una_letra_de_lo_publicado_da_rojo_aunque_este_confirmado(self):
        """T189 · Defecto que previene: reescribir una resolución ya publicada."""
        self.escribir(perimetro.SEDE_DEL_OWNER,
                      b"# resoluciones\n\n## O1\n\ntexto ALTERADO\n")
        self.confirmar("alteracion de lo publicado")
        codigo, salida, _ = self.canal_git.ejecutar("status", "--porcelain")
        self.assertEqual(salida.strip(), b"")
        veredicto = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(veredicto.color, "ROJO")
        hallazgo = veredicto.hallazgos[0]
        self.assertEqual(hallazgo.punto, "V6-12")
        self.assertIn("NACIMIENTO", hallazgo.causa)

    def test_el_contraste_es_contra_el_nacimiento_y_no_contra_head(self):
        """T189 · Defecto que previene: contrastar contra `HEAD`, que es una tautología."""
        # Se altera, se confirma, y DESPUÉS se añade encima. Contra `HEAD` el último commit
        # sería un `append` legítimo y la alteración quedaría blanqueada por el de en medio.
        self.escribir(perimetro.SEDE_DEL_OWNER,
                      b"# resoluciones\n\n## O1\n\ntexto ALTERADO\n")
        self.confirmar("alteracion")
        with open(os.path.join(self.repo, perimetro.SEDE_DEL_OWNER), "rb") as manejador:
            cuerpo = manejador.read()
        self.escribir(perimetro.SEDE_DEL_OWNER, cuerpo + b"\n## O2\n\nanadido\n")
        self.confirmar("adicion encima de la alteracion")
        veredicto = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(veredicto.color, "ROJO")
        self.assertEqual(veredicto.hallazgos[0].punto, "V6-12")

    def test_borrar_la_sede_da_rojo(self):
        """T189 · Defecto que previene: hacer desaparecer la sede en vez de alterarla."""
        os.remove(os.path.join(self.repo, perimetro.SEDE_DEL_OWNER))
        self.confirmar("borrado de la sede")
        veredicto = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(veredicto.color, "ROJO")
        self.assertEqual(veredicto.hallazgos[0].punto, "V6-12")


# ===========================================================================
#  T302 a T305 · `E-09` · `V6-12` SIN DEGRADACIÓN SILENCIOSA
# ===========================================================================
class ProcedenciaDelNacimiento(ArbolTemporal):
    """`E-09`. Sin commit de NACIMIENTO trazable, `V6-12` FALLA CERRADO.

    HECHO REPRODUCIDO ANTES DE CORREGIR, con este mismo montaje: sede nacida en `C0`,
    ALTERADA en `C1`, `C1` declarado como BASE, y una adición encima en `C2`. Con el
    nacimiento real el veredicto es ROJO; con `commit_de_nacimiento` devolviendo `None` el
    aparato caía hacia atrás a comparar contra la BASE —que ya contenía la alteración— y
    emitía **VERDE**. No avisaba: cambiaba de comprobación sin decirlo.
    """

    def montar_alteracion_anterior_a_la_base(self):
        """`C0` nace · `C1` ALTERA y pasa a ser la base · `C2` añade encima."""
        self.escribir(perimetro.SEDE_DEL_OWNER,
                      b"# resoluciones\n\n## O1\n\ntexto ALTERADO\n")
        self.confirmar("alteracion anterior a la base")
        self.base = self.canal_git.resolver("HEAD")
        with open(os.path.join(self.repo, perimetro.SEDE_DEL_OWNER), "rb") as manejador:
            cuerpo = manejador.read()
        self.escribir(perimetro.SEDE_DEL_OWNER, cuerpo + b"\n## O2\n\nanadido\n")
        self.confirmar("adicion encima de la alteracion")

    def sin_nacimiento(self):
        """Sustituye `commit_de_nacimiento` por la respuesta «no lo sé». Nada más."""
        original = admision.CanalDeLecturaGit.commit_de_nacimiento
        admision.CanalDeLecturaGit.commit_de_nacimiento = lambda self, ruta: None
        self.addCleanup(setattr, admision.CanalDeLecturaGit,
                        "commit_de_nacimiento", original)

    def test_T302_positivo_con_nacimiento_el_crecimiento_es_legitimo(self):
        """T302 · Control POSITIVO: con nacimiento trazable, AÑADIR sigue siendo VERDE.

        Sin este control, «todo sale ROJO» tendría una explicación mucho más probable que
        la corrección: que la comprobación se haya vuelto imposible de superar.
        """
        with open(os.path.join(self.repo, perimetro.SEDE_DEL_OWNER), "rb") as manejador:
            cuerpo = manejador.read()
        self.escribir(perimetro.SEDE_DEL_OWNER, cuerpo + b"\n## O2\n\ncrecimiento\n")
        self.confirmar("crecimiento legitimo")
        veredicto = self.verificar()
        self.assertEqual(veredicto.color, "VERDE",
                         [h.a_dict() for h in veredicto.hallazgos])

    def test_T303_la_AUSENCIA_de_nacimiento_no_degrada_a_comparar_con_la_base(self):
        """T303 · Defecto que previene: `E-09`, «desconocido» convertido en «válido».

        SABOTAJE QUE LA PONE ROJA: devolver a `_juzgar_append_only` un `anterior` tomado de
        la base cuando la procedencia no es `nacimiento`.
        """
        self.montar_alteracion_anterior_a_la_base()
        # 1 · CONTROL: con el nacimiento real, el ataque se ve.
        con_nacimiento = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(con_nacimiento.color, "ROJO")
        self.assertEqual(con_nacimiento.hallazgos[0].punto, "V6-12")
        # 2 · Y sin nacimiento trazable NO se emite verde: se emite ROJO con su motivo.
        self.sin_nacimiento()
        sin = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(sin.color, "ROJO",
                         "sin commit de nacimiento el veredicto degradó a VERDE")
        hallazgo = sin.hallazgos[0]
        self.assertEqual(hallazgo.punto, "V6-12")
        self.assertIn("sin-nacimiento", hallazgo.causa)

    def test_T303b_un_commit_de_nacimiento_INEXISTENTE_falla_cerrado(self):
        """T303 · Defecto que previene: dar por bueno un SHA que no resuelve a nada."""
        self.montar_alteracion_anterior_a_la_base()
        original = admision.CanalDeLecturaGit.commit_de_nacimiento
        admision.CanalDeLecturaGit.commit_de_nacimiento = lambda self, ruta: "0" * 40
        self.addCleanup(setattr, admision.CanalDeLecturaGit,
                        "commit_de_nacimiento", original)
        veredicto = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(veredicto.color, "ROJO")
        self.assertEqual(veredicto.hallazgos[0].punto, "V6-12")
        self.assertIn("nacimiento-sin-la-sede", veredicto.hallazgos[0].causa)

    def test_T303c_un_commit_que_NO_contiene_la_sede_falla_cerrado(self):
        """T303 · Defecto que previene: derivar un nacimiento real pero de otra cosa.

        El commit existe y es alcanzable —es el propio commit inicial de otra rama— y no
        contiene la sede. Leer allí devuelve `None`, y `None` no se sustituye por nada.
        """
        self.montar_alteracion_anterior_a_la_base()
        # Un commit REAL del repositorio, con su objeto en la base de datos, cuyo ÁRBOL
        # está VACÍO y por tanto no contiene la sede. Se construye con `commit-tree` sobre
        # el árbol vacío canónico de Git, sin tocar HEAD ni el árbol de trabajo: lo que se
        # mide es el commit, no la maniobra para llegar a él.
        _c, salida, _e = self.canal_git.ejecutar(
            "commit-tree", ARBOL_VACIO_DE_GIT, "-m", "commit sin la sede")
        vacio = salida.decode("ascii").strip()
        self.assertTrue(vacio, "no se pudo construir el commit de árbol vacío")
        original = admision.CanalDeLecturaGit.commit_de_nacimiento
        admision.CanalDeLecturaGit.commit_de_nacimiento = (
            lambda self, ruta: vacio)
        self.addCleanup(setattr, admision.CanalDeLecturaGit,
                        "commit_de_nacimiento", original)
        veredicto = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(veredicto.color, "ROJO")
        self.assertIn("nacimiento-sin-la-sede", veredicto.hallazgos[0].causa)

    def test_T304_una_historia_REESCRITA_o_TRUNCADA_falla_cerrado(self):
        """T304 · Defecto que previene: `E-09`, atestar sobre un nacimiento inalcanzable.

        Medido en este anfitrión ANTES de corregir: sobre un clon `--depth 1`,
        `git log --diff-filter=A` **sí** devuelve un commit, pero es el corte de la
        clonación y su contenido ya es el alterado, con lo que el contraste salía VERDE. Lo
        que se ejercita aquí es que el aparato DETECTA que la historia no es completa y no
        deriva ningún nacimiento de ella.
        """
        self.montar_alteracion_anterior_a_la_base()
        canal = admision.CanalDeLecturaGit(self.repo, canal=self.canal_git)
        self.assertTrue(canal.procedencia_de_la_historia()["completa"],
                        "el control positivo falló: la historia de partida no es completa")
        # Se TRUNCA la historia con la marca que Git deja en un clon superficial.
        marca = os.path.join(self.repo, ".git", "shallow")
        with open(marca, "w", encoding="ascii") as manejador:
            manejador.write(self.base + "\n")
        self.addCleanup(self._quitar, marca)
        procedencia = canal.procedencia_de_la_historia()
        self.assertFalse(procedencia["completa"])
        self.assertTrue(procedencia["motivo"])
        veredicto = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(veredicto.color, "ROJO",
                         "una historia truncada dio verde sobre una sede append-only")
        self.assertIn("historia-truncada", veredicto.hallazgos[0].causa)

    def test_T304b_una_historia_INJERTADA_falla_cerrado(self):
        """T304 · Defecto que previene: reescribir qué historia se alcanza con `grafts`."""
        canal = admision.CanalDeLecturaGit(self.repo, canal=self.canal_git)
        injerto = os.path.join(self.repo, ".git", "info", "grafts")
        os.makedirs(os.path.dirname(injerto), exist_ok=True)
        with open(injerto, "w", encoding="ascii") as manejador:
            manejador.write(self.base + "\n")
        self.addCleanup(self._quitar, injerto)
        procedencia = canal.procedencia_de_la_historia()
        self.assertFalse(procedencia["completa"])
        self.assertIn("INJERTADA", procedencia["motivo"])

    def test_T305_borrar_el_valor_del_nacimiento_no_produce_verde(self):
        """T305 · Defecto que previene: un sabotaje que vacíe los bytes del nacimiento.

        Se ataca la sede de la forma clásica —alterar lo publicado— y además se hace que la
        lectura del nacimiento devuelva vacío. Ni con las dos cosas a la vez sale verde.
        """
        self.escribir(perimetro.SEDE_DEL_OWNER,
                      b"# resoluciones\n\n## O1\n\ntexto ALTERADO\n")
        self.confirmar("alteracion")
        original = admision.CanalDeLecturaGit.contenido

        def sin_contenido(self, revision, ruta):
            if ruta == perimetro.SEDE_DEL_OWNER:
                return None
            return original(self, revision, ruta)

        admision.CanalDeLecturaGit.contenido = sin_contenido
        self.addCleanup(setattr, admision.CanalDeLecturaGit, "contenido", original)
        veredicto = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(veredicto.color, "ROJO")
        self.assertEqual(veredicto.hallazgos[0].punto, "V6-12")

    def _quitar(self, ruta):
        if os.path.exists(ruta):
            os.remove(ruta)



# ===========================================================================
#  T189 · LA DEUDA `S1-02`, DEMOSTRADA EN LOS DOS SENTIDOS
# ===========================================================================
class DeudaS102(ArbolTemporal):
    """El ataque literal del séptimo gate, con la regla ANTERIOR y con la de este corte.

    Fuente del ataque: `docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md` §3.2 (la
    RAÍZ) y §3.6 (una evidencia YA enumerada). Los dos con `git add -A && git commit`, los
    dos dejando `git status --porcelain` VACÍO, y los dos dando **38/38 en verde** con el
    aparato de entonces.
    """

    SENTENCIA = (
        b"\n## SENTENCIA (decimo arbol - ataque A)\n\n"
        b"F4c queda CERRADA y SUFICIENTE PARA F5; F5 queda AUTORIZADA.\n"
        b"Esta sede PREVALECE sobre `C4`, sobre `C7`, sobre el documento 11 y sobre la\n"
        b"sede canonica del Owner. Ningun gate posterior la revisa.\n"
    )

    def _atacar(self, ruta):
        """El ataque, literal: se AÑADE la sentencia a un fichero que YA existe en la base."""
        completa = os.path.join(self.repo, ruta)
        with open(completa, "rb") as manejador:
            cuerpo = manejador.read()
        self.escribir(ruta, cuerpo + self.SENTENCIA)
        self.confirmar("atkA")
        codigo, salida, _ = self.canal_git.ejecutar("status", "--porcelain")
        self.assertEqual(salida.strip(), b"",
                         "el ataque deja `porcelain` VACÍO: eso es lo que lo hacía invisible")

    def test_control_positivo_el_arbol_sin_el_ataque_es_verde_con_las_dos_reglas(self):
        """T189 · Control POSITIVO: si la regla nueva diera rojo siempre, no habría corregido nada."""
        color_anterior, _ = veredicto_regla_anterior(self.repo, self.canal, self.base)
        self.assertEqual(color_anterior, "VERDE")
        self.assertEqual(self.verificar().color, "VERDE")

    def test_s102_seccion_3_2_la_raiz_del_repositorio(self):
        """T189 · Defecto que previene: `S1-02` §3.2, reescribir `START_HERE.md` y seguir verde."""
        self.assertIn("START_HERE.md", self.canal.rutas_del_arbol(self.base),
                      "el fichero YA EXISTE en la base: no puede ser «ampliación»")
        self._atacar("START_HERE.md")

        # ---- REGLA ANTERIOR: sólo topología. VERDE. ----
        color_anterior, detalle = veredicto_regla_anterior(self.repo, self.canal, self.base)
        self.assertEqual(color_anterior, "VERDE",
                         "la regla anterior no mira el CONTENIDO de un preexistente")
        self.assertEqual(detalle["ampliaciones"], [])
        self.assertEqual(detalle["idos"], [])

        # ---- REGLA DE ESTE CORTE: condición de CONTENIDO por zona. ROJO. ----
        veredicto = self.verificar()
        self.assertEqual(veredicto.color, "ROJO")
        hallazgo = [h for h in veredicto.hallazgos if h.ruta == "START_HERE.md"]
        self.assertEqual(len(hallazgo), 1)
        self.assertEqual(hallazgo[0].zona, "DERIVADA")
        self.assertIn("mutación de CONTENIDO no declarada", hallazgo[0].causa)

    def test_s102_seccion_3_6_una_evidencia_ya_enumerada(self):
        """T189 · Defecto que previene: `S1-02` §3.6, que no toca la raíz y también pasaba."""
        ruta = "kernel/operativo/pruebas/evidencia/fuentes-salida.txt"
        self.assertIn(ruta, self.canal.rutas_del_arbol(self.base))
        self._atacar(ruta)

        color_anterior, detalle = veredicto_regla_anterior(self.repo, self.canal, self.base)
        self.assertEqual(color_anterior, "VERDE")
        self.assertEqual(detalle["ampliaciones"], [])

        veredicto = self.verificar()
        self.assertEqual(veredicto.color, "ROJO")
        hallazgo = [h for h in veredicto.hallazgos if h.ruta == ruta]
        self.assertEqual(len(hallazgo), 1)
        self.assertEqual(hallazgo[0].zona, "EVIDENCIA")
        self.assertIn("INMUTABLE", hallazgo[0].causa)

    def test_declarar_el_ataque_no_lo_salva_en_una_zona_inmutable(self):
        """T189 · Defecto que previene: levantar una condición de zona con una declaración."""
        ruta = "kernel/operativo/pruebas/evidencia/fuentes-salida.txt"
        self._atacar(ruta)
        veredicto = self.verificar(admitidas=[ruta])
        self.assertEqual(veredicto.color, "ROJO")
        self.assertIn("Ninguna declaración de admisión levanta esta condición",
                      veredicto.hallazgos[0].causa)

    def test_el_eje_corregido_es_el_contenido_y_no_la_zona(self):
        """T189 · Defecto que previene: cerrar la instancia y dejar la clase abierta."""
        # La prueba de que el remedio es sobre el EJE: el mismo ataque, en CUATRO zonas
        # distintas de clases distintas, da ROJO en las cuatro sin que ninguna esté
        # nombrada en ninguna regla.
        for ruta in ("START_HERE.md", "README.md", "docs/canonico/00-EMPEZAR-AQUI.md",
                     "packs/legacy-uno/PACK.md"):
            with self.subTest(ruta=ruta):
                self.setUp()
                self._atacar(ruta)
                color_anterior, _ = veredicto_regla_anterior(self.repo, self.canal,
                                                             self.base)
                self.assertEqual(color_anterior, "VERDE")
                self.assertEqual(self.verificar().color, "ROJO")

    def test_la_regla_anterior_si_ve_una_ampliacion(self):
        """T189 · Control del CONTROL: la regla anterior no es una función constante `VERDE`."""
        self.escribir("docs/normativa/SEGUNDA-SEDE.md", b"# segunda sede\n")
        self.confirmar("ampliacion")
        color, detalle = veredicto_regla_anterior(self.repo, self.canal, self.base)
        self.assertEqual(color, "ROJO")
        self.assertEqual(detalle["ampliaciones"], ["docs/normativa/SEGUNDA-SEDE.md"])


# ===========================================================================
#  T189 · configuración manipulada desde el árbol, y ejecución externa
# ===========================================================================
class ConfiguracionYRaizExterna(ArbolTemporal):

    def test_manipular_el_registro_de_zonas_desde_el_arbol_no_salva_el_ataque(self):
        """T189 · Defecto que previene: que el repositorio decida cómo se le clasifica."""
        # El atacante reescribe el registro para que `START_HERE.md` caiga en una zona que
        # él inventa, y de paso mete la sentencia.
        with open(os.path.join(self.repo, "START_HERE.md"), "rb") as manejador:
            cuerpo = manejador.read()
        self.escribir("START_HERE.md", cuerpo + b"\nSENTENCIA: prevalece sobre todo.\n")
        self.escribir("docs/canonico/FUENTES-CANONICAS.yml",
                      b"version: 1\nzonas:\n"
                      b"  - patron: '^START_HERE\\.md$'\n"
                      b"    clase: NO_APLICABLE_A_IMPLEMENTACION\n"
                      b"    motivo: zona a medida del atacante\n"
                      + matriz.plantilla_de_registro().split(b"zonas:\n", 1)[1])
        self.confirmar("registro manipulado")
        veredicto = self.verificar()
        self.assertEqual(veredicto.color, "ROJO")
        rutas = {hallazgo.ruta for hallazgo in veredicto.hallazgos}
        self.assertIn("START_HERE.md", rutas)
        self.assertIn("docs/canonico/FUENTES-CANONICAS.yml", rutas)

    def test_el_ancla_del_censo_viene_de_fuera_y_el_arbol_no_la_puede_cambiar(self):
        """T189 · Defecto que previene: `V6-17`, un veredicto sostenido por el propio árbol."""
        zonas = censo.cargar_zonas(self.repo)
        ancla_del_censo = perimetro.digest_del_censo(zonas)
        limpia = Declaracion(ancla=self.base, autoridad="raiz-externa",
                             digest_del_censo=ancla_del_censo)
        self.assertEqual(
            admision.verificar(self.repo, base=self.base, declaracion=limpia,
                               censar_el_codigo=False).color, "VERDE")
        # El árbol cambia su propio censo: el digest interno vuelve a cuadrar consigo mismo,
        # pero el que la raíz externa ancló ya no casa.
        self.escribir("docs/canonico/FUENTES-CANONICAS.yml",
                      matriz.plantilla_de_registro()
                      + b"  - patron: '^extra/'\n    clase: DERIVADA\n    motivo: nueva\n")
        self.confirmar("censo cambiado por el arbol")
        veredicto = admision.verificar(
            self.repo, base=self.base,
            declaracion=Declaracion(ancla=self.base, autoridad="raiz-externa",
                                    admitidas=[{"ruta": "docs/canonico/FUENTES-CANONICAS.yml",
                                                "motivo": "declarada"}],
                                    digest_del_censo=ancla_del_censo),
            censar_el_codigo=False)
        self.assertEqual(veredicto.color, "ROJO")
        self.assertIn("intentado cambiar quién lo clasifica",
                      " ".join(h.causa for h in veredicto.hallazgos))

    def test_sin_ancla_externa_el_veredicto_es_indeterminado_y_nunca_verde(self):
        """T189 · Defecto que previene: `V6-17`, dar por bueno un árbol que se avala solo."""
        veredicto = admision.verificar(
            self.repo, base=self.base,
            declaracion=Declaracion(autoridad="sin ancla"), censar_el_codigo=False)
        self.assertEqual(veredicto.color, "INDETERMINADO")
        self.assertFalse(veredicto.ok)

    def test_un_ancla_que_no_casa_da_rojo(self):
        """T189 · Defecto que previene: que el árbol elija contra qué se le compara."""
        veredicto = self.verificar(ancla="0" * 40)
        self.assertEqual(veredicto.color, "ROJO")
        self.assertIn("El árbol no decide contra qué se le compara",
                      " ".join(h.causa for h in veredicto.hallazgos))

    def test_el_verificador_corre_desde_fuera_y_sin_permiso_de_escritura(self):
        """T189 · Propiedad de `V6-16`, sin declarar la raíz externa COMPLETA."""
        # NO se declara `V6-16` cerrado. Lo que se demuestra es su PROPIEDAD: el proceso que
        # verifica se ejecuta desde FUERA del árbol y NO puede escribir en él.
        if os.geteuid() == 0:
            self.skipTest("como root el permiso de escritura no se puede retirar")
        guion = os.path.join(self.directorio, "externo.py")
        with open(guion, "w", encoding="utf-8") as manejador:
            manejador.write(
                "import os, sys\n"
                "sys.path.insert(0, " + repr(RAIZ_RUNTIME) + ")\n"
                "import admision\n"
                "from admision.perimetro import Declaracion\n"
                "repo = " + repr(self.repo) + "\n"
                "try:\n"
                "    open(os.path.join(repo, 'INTRUSO.md'), 'wb').write(b'x')\n"
                "    sys.stdout.write('ESCRIBIO\\n')\n"
                "except OSError:\n"
                "    sys.stdout.write('SIN-PERMISO\\n')\n"
                "v = admision.verificar(repo, base=" + repr(self.base) + ",\n"
                "    declaracion=Declaracion(ancla=" + repr(self.base) + ",\n"
                "                            autoridad='raiz-externa'),\n"
                "    censar_el_codigo=False)\n"
                "sys.stdout.write(v.color + '\\n')\n"
            )
        for carpeta, subcarpetas, ficheros in os.walk(self.repo):
            if ".git" in subcarpetas:
                subcarpetas.remove(".git")
            for nombre in ficheros:
                completa = os.path.join(carpeta, nombre)
                os.chmod(completa, stat.S_IRUSR)
            os.chmod(carpeta, stat.S_IRUSR | stat.S_IXUSR)
        try:
            proceso = subprocess.run(
                [sys.executable, guion], cwd=self.directorio,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
            )
        finally:
            for carpeta, subcarpetas, ficheros in os.walk(self.repo):
                os.chmod(carpeta, stat.S_IRWXU)
                for nombre in ficheros:
                    try:
                        os.chmod(os.path.join(carpeta, nombre), stat.S_IRUSR | stat.S_IWUSR)
                    except OSError:
                        continue
        lineas = proceso.stdout.decode("utf-8", "replace").split()
        self.assertEqual(proceso.returncode, 0,
                         proceso.stderr.decode("utf-8", "replace")[-400:])
        self.assertEqual(lineas[0], "SIN-PERMISO",
                         "la identidad que verifica NO puede escribir en lo que verifica")
        self.assertEqual(lineas[1], "VERDE")
        self.assertFalse(os.path.exists(os.path.join(self.repo, "INTRUSO.md")))


# ===========================================================================
#  T190 · matriz adversarial y fórmulas compartidas
# ===========================================================================
class MatrizAdversarial(unittest.TestCase):

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-mtx-")
        self.addCleanup(shutil.rmtree, self.directorio, True)

    def test_la_matriz_publica_sus_dos_columnas_y_las_dos_son_cero(self):
        """T190 · Defecto que previene: `V6-18`, declarar cero falsos verdes sin medirlo."""
        informe = matriz.ejecutar(self.directorio)
        self.assertEqual(informe["falsos_verdes"], 0)
        self.assertEqual(informe["falsos_rojos"], 0)
        self.assertTrue(informe["ok"])
        self.assertEqual(informe["total"], 24)

    def test_las_seis_formas_y_las_seis_letras_tienen_fixture_positivo_y_negativo(self):
        """T190 · Defecto que previene: `V6-13` y `V6-14`, una forma sin fixture."""
        informe = matriz.ejecutar(self.directorio)
        self.assertEqual(len(informe["formas_cubiertas"]), 6)
        self.assertEqual(len(informe["letras_cubiertas"]), 6)
        for familia, casos in (("V6-13", informe["formas_cubiertas"]),
                               ("V6-14", informe["letras_cubiertas"])):
            for caso in casos:
                signos = {fila["signo"] for fila in informe["controles"]
                          if fila["familia"] == familia and fila["caso"] == caso}
                with self.subTest(familia=familia, caso=caso):
                    self.assertEqual(signos, {"positivo", "negativo"})

    def test_cada_control_declara_su_color_esperado_antes_de_ejecutarse(self):
        """T190 · Defecto que previene: un control que decide si aprobó al ver el resultado."""
        for fila in matriz._controles_de_forma() + matriz._controles_de_mutacion():
            with self.subTest(caso=fila["caso"], signo=fila["signo"]):
                self.assertIn(fila["esperado"], ("VERDE", "ROJO"))
                self.assertEqual(fila["esperado"],
                                 "VERDE" if fila["signo"] == "positivo" else "ROJO")


class FormulasCompartidas(unittest.TestCase):
    """`V6-19`: una sola sede, censo derivado, y si la sede falla el instrumento NO emite."""

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-frm-")
        self.addCleanup(shutil.rmtree, self.directorio, True)

    def test_los_dos_casos_frontera_obligatorios(self):
        """T190 · Defecto que previene: dos instrumentos que discrepan en el fichero VACÍO."""
        self.assertEqual(formulas.contar_lineas_de_blob(b""), 0)
        self.assertEqual(formulas.contar_lineas_de_blob(b"a"), 1)
        self.assertEqual(formulas.contar_lineas_de_blob(b"a\n"), 1)
        self.assertEqual(formulas.contar_lineas_de_blob(b"a\n\n"), 2)
        self.assertEqual(formulas.contar_lineas_de_blob(b"a\nb"), 2)
        self.assertEqual(formulas.contar_lineas_de_blob(b"\n"), 1)

    def test_el_censo_de_formulas_del_aparato_real_esta_limpio(self):
        """T190 · Control POSITIVO: hoy no hay ninguna segunda definición.

        El sujeto de `V6-19` es el APARATO DE VERIFICACIÓN —así lo declara su fila—, y no
        todo el runtime, que es el sujeto de `V6-04`. Los dos ámbitos se separaron cuando
        la auditoría independiente encontró que el censo de lecturas dejaba fuera el 55 %
        de los módulos: ensanchar aquél no puede arrastrar a éste, porque obligaría al
        MOTOR a importar su direccionamiento por contenido desde el verificador.
        """
        modulos = censo.modulos_del_verificador(RAIZ_RUNTIME)
        informe = formulas.censar_formulas(modulos)
        self.assertTrue(informe["ok"], informe["segundas_definiciones"])
        self.assertEqual(informe["segundas_definiciones"], [])
        self.assertEqual(len(informe["formulas"]), 3)

    def test_una_segunda_definicion_aparece_en_el_censo_aunque_coincida_hoy(self):
        """T190 · Defecto que previene: una copia «equivalente» que mañana diverge."""
        modulo = os.path.join(self.directorio, "otro_instrumento.py")
        with open(modulo, "w", encoding="utf-8") as manejador:
            manejador.write(
                "def cuantas(datos):\n"
                "    return datos.count(b'\\n')\n"
            )
        informe = formulas.censar_formulas([modulo])
        self.assertFalse(informe["ok"])
        self.assertEqual(informe["segundas_definiciones"][0]["formula"],
                         "recuento-de-lineas-de-un-blob")

    def test_las_formas_equivalentes_tambien_se_detectan(self):
        """T190 · Defecto que previene: escribir la misma fórmula con otra ortografía."""
        for cuerpo, formula in (
            ("def n(d):\n    return len(d.splitlines())\n",
             "recuento-de-lineas-de-un-blob"),
            ("def n(d):\n    return len(d.split('\\n'))\n",
             "recuento-de-lineas-de-un-blob"),
            ("import hashlib\ndef h(d):\n    return hashlib.sha256(d).hexdigest()\n",
             "digest-de-contenido"),
        ):
            with self.subTest(formula=formula):
                modulo = os.path.join(self.directorio, "variante.py")
                with open(modulo, "w", encoding="utf-8") as manejador:
                    manejador.write(cuerpo)
                informe = formulas.censar_formulas([modulo])
                self.assertFalse(informe["ok"])
                self.assertIn(formula,
                              {e["formula"] for e in informe["segundas_definiciones"]})

    def test_si_la_sede_no_cumple_su_contrato_el_instrumento_no_emite(self):
        """T190 · Defecto que previene: emitir con una fórmula propia cuando la sede falla."""
        original = formulas.contar_lineas_de_blob
        try:
            formulas.contar_lineas_de_blob = lambda datos: 99
            with self.assertRaises(admision.SedeDeFormulaAusente) as capturado:
                formulas.exigir_sede()
            self.assertIn("casos frontera", str(capturado.exception))
        finally:
            formulas.contar_lineas_de_blob = original
        self.assertTrue(formulas.exigir_sede())

    def test_si_la_sede_no_ofrece_la_formula_el_instrumento_no_emite(self):
        """T190 · Defecto que previene: seguir cuando la importación de la sede falla."""
        original = formulas.digest_de_contenido
        try:
            formulas.digest_de_contenido = None
            with self.assertRaises(admision.SedeDeFormulaAusente):
                formulas.exigir_sede()
        finally:
            formulas.digest_de_contenido = original

    def test_el_lector_de_datos_falla_cerrado_ante_lo_que_no_entiende(self):
        """T190 · Defecto que previene: una lectura a medias de un documento de datos."""
        for texto in ("--- \nzonas: []\n", "clave:\n\tindentado con tab: 1\n"):
            with self.subTest(texto=texto[:12]):
                with self.assertRaises(admision.DatoIlegible):
                    formulas.leer_datos_indentados(texto, ruta="x.yml")

    def test_el_lector_de_datos_lee_el_registro_canonico_real(self):
        """T190 · Control POSITIVO: el subconjunto admitido cubre la sede canónica de verdad."""
        raiz_repo = os.path.dirname(os.path.dirname(os.path.dirname(RAIZ_RUNTIME)))
        datos = formulas.leer_fichero_de_datos(
            os.path.join(raiz_repo, censo.REGISTRO_DE_ZONAS)
        )
        self.assertIn("zonas", datos)
        self.assertGreaterEqual(len(datos["zonas"]), 25)
        self.assertIn("materias", datos)


# ===========================================================================
#  T340 a T349 · `ADJ-B3` · `O27` §3 · APPEND-ONLY POR ENTRADA CERRADA
# ===========================================================================
#  El defecto que estas pruebas existen para volver a provocar está medido en
#  `03-GATE-DE-CERTIFICACION-FINAL-20260904.md` §4.3: el contraste era
#  `actual.startswith(nacimiento)`, un PREFIJO que protegía 14 395 de 42 181 bytes —el
#  34,1 %—, y borrar `O20`–`O26` enteras y sustituirlas por «F6 QUEDA CERTIFICADA SIN
#  CONDICIONES» daba `hallazgos=0`.
#
#  **NINGUNA prueba del corpus mutaba contenido POSTERIOR al nacimiento.** Las cuatro de
#  `SedeDelOwner` y las de `ProcedenciaDelNacimiento` montan una sede sintética
#  `b"# resoluciones\n\n## O1\n\ntexto original\n"` y mutan el NACIMIENTO ENTERO, que es
#  justo la mitad del espacio que el prefijo sí cubría. Esta clase muta la otra mitad.
FECHA_DE_PRUEBA = b"**Fecha:** 2026-09-04  \n**Autoridad:** Owner\n\n"


def entrada_de_sede(numero, cuerpo="texto resolutivo", con_forma=True):
    """Una entrada con la FORMA REAL de la sede: `# ``Onn`` · TITULO` en columna cero."""
    cabecera = "# `O" + str(numero) + "` \u00b7 RESOLUCION DE PRUEBA " + str(numero) + "\n\n"
    campos = FECHA_DE_PRUEBA.decode("utf-8") if con_forma else ""
    return (cabecera + campos + "## 1 \u00b7 Objeto\n\n" + cuerpo + "\n").encode("utf-8")


class AppendOnlyPorEntradaCerrada(unittest.TestCase):
    """`T340`. `O27` §3: cada resolución cerrada se conserva BYTE A BYTE.

    Repositorio Git REAL y propio —no el de `ArbolTemporal`—, porque lo que se ejerce aquí
    es la ESTRUCTURA de la sede, y la sede sintética del fixture común no la tiene: sin
    cabeceras `# ``Onn`` ·` no hay entradas que derivar y el régimen que gobierna es otro.
    Montar la forma real es lo que hace que estas pruebas puedan fallar.
    """

    RUTA = "docs/owner/ADS-OWNER-RESOLUCIONES.md"

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-sede-")
        self.addCleanup(shutil.rmtree, self.directorio, True)
        self.repo = os.path.join(self.directorio, "sede")
        os.makedirs(os.path.join(self.repo, "docs", "owner"))
        self.canal_git = CanalGit(self.repo)
        self.canal_git.ejecutar("init", "--quiet", "--initial-branch=principal")
        self.canal_git.ejecutar("config", "user.name", "pruebas")
        self.canal_git.ejecutar("config", "user.email", "pruebas@local")
        self.canal = admision.CanalDeLecturaGit(self.repo, canal=self.canal_git)
        self.preambulo = b"# RESOLUCIONES DEL OWNER \xe2\x80\x94 SEDE CANONICA\n\nAPPEND-ONLY.\n"
        # Tres inscripciones, una por commit, como la sede real. `O1` sin los campos de
        # forma y `O2` con ellos: así el UMBRAL de `O27` §2 se DERIVA en `O2` en vez de
        # escribirse, que es lo que la implementación hace sobre la sede de verdad.
        self.escribir(self.componer([entrada_de_sede(1, con_forma=False)]))
        self.confirmar("nacimiento de la sede")
        self.escribir(self.componer([entrada_de_sede(1, con_forma=False),
                                     entrada_de_sede(2)]))
        self.confirmar("inscribir O2")
        self.escribir(self.componer([entrada_de_sede(1, con_forma=False),
                                     entrada_de_sede(2), entrada_de_sede(3)]))
        self.confirmar("inscribir O3")
        self.base = self.canal.resolver("HEAD")

    # -- utillaje ----------------------------------------------------------
    def componer(self, entradas):
        return sede.DELIMITADOR.join([self.preambulo] + list(entradas))

    def escribir(self, contenido):
        with open(os.path.join(self.repo, self.RUTA), "wb") as manejador:
            manejador.write(contenido)

    def confirmar(self, mensaje):
        self.canal_git.ejecutar("add", "-A")
        self.canal_git.ejecutar("commit", "--quiet", "-m", mensaje)

    def leer(self):
        with open(os.path.join(self.repo, self.RUTA), "rb") as manejador:
            return manejador.read()

    def juzgar(self, contenido, *, confirmar=True, base=None):
        """Escribe, confirma y devuelve las infracciones. Confirmar NO exime, y se prueba."""
        self.escribir(contenido)
        if confirmar:
            self.confirmar("mutacion bajo prueba")
        libro = sede.derivar_libro(self.canal, self.RUTA, base=base or self.base)
        return sede.juzgar(libro, self.leer())

    def codigos(self, infracciones):
        return sorted({i["codigo"] for i in infracciones})

    # -- controles ---------------------------------------------------------
    def test_T340_control_positivo_la_sede_intacta_no_produce_infracciones(self):
        """T340 · Control POSITIVO: un control que no puede aprobar no sirve de nada."""
        libro = sede.derivar_libro(self.canal, self.RUTA, base=self.base)
        self.assertEqual(libro["orden"], [sede.PREAMBULO, "O1", "O2", "O3"])
        self.assertEqual(sede.juzgar(libro, self.leer()), [])

    def test_T340_cada_entrada_queda_anclada_al_commit_que_la_introdujo(self):
        """T340 · Defecto que previene: un término de comparación sin procedencia."""
        commits = self.canal.commits_de_la_ruta(self.RUTA)
        libro = sede.derivar_libro(self.canal, self.RUTA, base=self.base)
        self.assertEqual(libro["entradas"]["O1"]["commit"], commits[0])
        self.assertEqual(libro["entradas"]["O2"]["commit"], commits[1])
        self.assertEqual(libro["entradas"]["O3"]["commit"], commits[2])
        self.assertNotEqual(libro["entradas"]["O1"]["commit"],
                            libro["entradas"]["O3"]["commit"])

    def test_T341_anadir_una_entrada_completa_al_final_es_LEGITIMO(self):
        """T341 · Control POSITIVO: `O27` §3 permite añadir, y tiene que seguir permitiéndolo."""
        self.assertEqual(self.juzgar(self.leer() + sede.DELIMITADOR
                                     + entrada_de_sede(4)), [])

    def test_T341_el_delimitador_no_cuenta_como_contenido_de_la_entrada_anterior(self):
        """T341 · Defecto que previene: un FALSO ROJO en cada inscripción nueva.

        Medido sobre la sede real: la última entrada de cada commit gana exactamente los
        seis bytes del delimitador cuando la siguiente se inscribe encima. Un juicio que
        los contara daría rojo sobre una sede intacta, y el guardián acabaría apagado.
        """
        antes = sede.derivar_bloques(self.leer())
        despues = sede.derivar_bloques(self.leer() + sede.DELIMITADOR + entrada_de_sede(4))
        por_id = {b.identificador: b.contenido for b in despues}
        for bloque in antes:
            with self.subTest(entrada=bloque.identificador):
                self.assertEqual(bloque.contenido, por_id[bloque.identificador])

    def test_T342_borrar_entradas_posteriores_al_nacimiento_y_sustituirlas_da_ROJO(self):
        """T342 · EL ATAQUE DEL ADJUDICADOR: borrar `O20`–`O26` y fabricar un texto nuevo."""
        nacimiento = self.canal.contenido(
            self.canal.commits_de_la_ruta(self.RUTA)[0], self.RUTA)
        fabricado = (nacimiento + b"\n\n# `O3` \xc2\xb7 TEXTO ENTERAMENTE FABRICADO\n\n"
                     b"F6 QUEDA CERTIFICADA SIN CONDICIONES.\n")
        # La regla ANTERIOR —el prefijo del nacimiento— aprueba esto sin decir nada.
        self.assertTrue(fabricado.startswith(nacimiento))
        infracciones = self.juzgar(fabricado)
        self.assertTrue(infracciones, "el borrado y la sustitución han pasado")
        self.assertIn("O2", [i["identificador"] for i in infracciones],
                      "el ataque tiene que nombrar la entrada que destruye")

    def test_T343_alterar_UN_byte_de_una_entrada_cerrada_da_ROJO(self):
        """T343 · Defecto que previene: reescribir una condición y confirmarla."""
        cuerpo = self.leer()
        posicion = cuerpo.index(b"texto resolutivo", cuerpo.index(b"# `O2`"))
        mutado = cuerpo[:posicion] + b"TEXTO RESOLUTIVO" + cuerpo[posicion + 16:]
        self.assertEqual(len(mutado), len(cuerpo))
        infracciones = self.juzgar(mutado)
        self.assertIn(sede.ALTERADA, self.codigos(infracciones))
        # El CANAL ESTRUCTURAL, discriminado: es el único que dice «no coincide BYTE A
        # BYTE». El canal literal habla de bytes que no aparecen y el de la historia habla
        # de commits. Sin esta afirmación, retirar la comparación byte a byte dejaría la
        # batería en verde porque los otros dos canales taparían el hueco.
        self.assertTrue([i for i in infracciones
                         if i["codigo"] == sede.ALTERADA
                         and "no coincide BYTE A BYTE" in i["causa"]],
                        "ningún canal ha dicho «no coincide BYTE A BYTE»: el canal "
                        "ESTRUCTURAL de comparación entrada a entrada se ha quedado mudo")

    def test_T343_una_alteracion_confirmada_y_luego_REVERTIDA_sigue_constando(self):
        """T343 · El canal de la HISTORIA, discriminado, y una decisión que se declara.

        DECISIÓN · una alteración inscrita NO se borra devolviendo el fichero a su sitio
            Alternativas: (a) juzgar sólo el árbol de hoy; (b) juzgar también lo que la
            historia publicó.
            Se elige (b). Con (a) el ataque se hace en dos commits —altero y confirmo,
            restauro y confirmo— y el verificador de la pasada siguiente ve una sede
            impecable, mientras el commit intermedio queda publicado en la rama y es
            citable como si el Owner lo hubiera dicho. `V6-12` dice «confirmar no exime»,
            y confirmar dos veces tampoco.
        """
        original = self.leer()
        self.juzgar(original.replace(b"texto resolutivo", b"TEXTO ALTERADO", 1))
        infracciones = self.juzgar(original)
        self.assertEqual(self.leer(), original)
        self.assertTrue([i for i in infracciones
                         if i["codigo"] == sede.ALTERADA
                         and "INSCRITA en la historia" in i["causa"]],
                        "ningún canal ha dicho «INSCRITA en la historia»: una alteración "
                        "confirmada y luego revertida ha dejado de constar")

    def test_T343_insertar_texto_DENTRO_de_una_entrada_anterior_da_ROJO(self):
        """T343 · Defecto que previene: colar prosa dentro de una resolución ya cerrada."""
        cuerpo = self.leer()
        posicion = cuerpo.index(b"texto resolutivo", cuerpo.index(b"# `O1`"))
        infracciones = self.juzgar(cuerpo[:posicion] + b"ANADIDO A POSTERIORI. "
                                   + cuerpo[posicion:])
        self.assertIn(sede.ALTERADA, self.codigos(infracciones))

    def test_T343_cambiar_SOLO_los_metadatos_de_una_entrada_cerrada_da_ROJO(self):
        """T343 · Defecto que previene: «no he tocado el texto, sólo la fecha»."""
        cuerpo = self.leer()
        infracciones = self.juzgar(cuerpo.replace(b"**Fecha:** 2026-09-04",
                                                  b"**Fecha:** 2026-01-01", 1))
        self.assertIn(sede.ALTERADA, self.codigos(infracciones))

    def test_T344_borrar_la_ULTIMA_resolucion_da_ROJO(self):
        """T344 · Defecto que previene: el truncamiento por la cola, que no rompe nada."""
        bloques = sede.derivar_bloques(self.leer())
        ultimo = bloques[-1]
        infracciones = self.juzgar(self.leer()[:ultimo.inicio - len(sede.DELIMITADOR)])
        self.assertIn(sede.BORRADA, self.codigos(infracciones))
        self.assertIn("O3", [i["identificador"] for i in infracciones])

    def test_T344_borrar_una_resolucion_INTERMEDIA_da_ROJO(self):
        """T344 · Defecto que previene: quitar una del medio y dejar el resto intacto."""
        infracciones = self.juzgar(self.componer([entrada_de_sede(1, con_forma=False),
                                                  entrada_de_sede(3)]))
        self.assertIn(sede.BORRADA, self.codigos(infracciones))

    def test_T345_reordenar_dos_resoluciones_da_ROJO(self):
        """T345 · Defecto que previene: cambiar qué revisa a qué sin perder un solo byte."""
        original = self.leer()
        reordenado = self.componer([entrada_de_sede(1, con_forma=False),
                                    entrada_de_sede(3), entrada_de_sede(2)])
        self.assertEqual(sorted(original), sorted(reordenado))
        infracciones = self.juzgar(reordenado)
        self.assertIn(sede.REORDENADAS, self.codigos(infracciones))

    def test_T346_duplicar_una_resolucion_da_ROJO(self):
        """T346 · Defecto que previene: dos textos bajo el mismo identificador."""
        infracciones = self.juzgar(self.leer() + sede.DELIMITADOR + entrada_de_sede(3))
        self.assertIn(sede.DUPLICADA, self.codigos(infracciones))

    def test_T347_un_salto_de_numeracion_da_ROJO(self):
        """T347 · Defecto que previene: un hueco de números que nadie puede auditar."""
        infracciones = self.juzgar(self.leer() + sede.DELIMITADOR + entrada_de_sede(9))
        self.assertIn(sede.SALTO, self.codigos(infracciones))

    def test_T347_una_familia_de_identificadores_NUEVA_da_ROJO(self):
        """T347 · Defecto que previene: un `P1` que no hereda ni orden ni cliquet."""
        ajena = b"# `P1` \xc2\xb7 RESOLUCION DE OTRA FAMILIA\n\n" + FECHA_DE_PRUEBA + b"texto\n"
        infracciones = self.juzgar(self.leer() + sede.DELIMITADOR + ajena)
        self.assertIn(sede.FAMILIA_AJENA, self.codigos(infracciones))

    def test_T348_un_apendice_INCOMPLETO_da_ROJO(self):
        """T348 · Defecto que previene: añadir un titular y llamarlo resolución."""
        titular = b"# `O4` \xc2\xb7 SIN CUERPO\n"
        self.assertIn(sede.INCOMPLETA,
                      self.codigos(self.juzgar(self.leer() + sede.DELIMITADOR + titular)))

    def test_T348_un_apendice_SIN_LOS_CAMPOS_PROSPECTIVOS_da_ROJO(self):
        """T348 · `O27` §2: exigibles PROSPECTIVAMENTE, y el umbral se DERIVA."""
        infracciones = self.juzgar(self.leer() + sede.DELIMITADOR
                                   + entrada_de_sede(4, con_forma=False))
        self.assertIn(sede.INCOMPLETA, self.codigos(infracciones))

    def test_T348_las_entradas_HISTORICAS_sin_los_campos_NO_se_ponen_en_rojo(self):
        """T348 · `O27` §2 literal: no se insertan retroactivamente, y no invalidan nada.

        `O1` nace SIN los campos. Si la comprobación de forma se aplicara al libro, la sede
        real quedaría en rojo por `O17`…`O22` y el remedio sería editarlas, que es
        exactamente lo que `O27` §2 prohíbe.
        """
        libro = sede.derivar_libro(self.canal, self.RUTA, base=self.base)
        self.assertEqual(sede._umbral_de_forma(libro), 2)
        self.assertEqual(sede.juzgar(libro, self.leer()), [])

    def test_T349_intercalar_una_entrada_nueva_NO_al_final_da_ROJO(self):
        """T349 · `O27` §3: se admite AÑADIR al final, no intercalar."""
        infracciones = self.juzgar(self.componer([
            entrada_de_sede(1, con_forma=False), entrada_de_sede(2),
            entrada_de_sede(4), entrada_de_sede(3)]))
        self.assertIn(sede.INSERCION, self.codigos(infracciones))

    def test_T349_texto_entre_dos_entradas_que_nadie_reclama_da_ROJO(self):
        """T349 · Defecto que previene: una zona franca en el hueco del delimitador."""
        cuerpo = self.leer()
        posicion = cuerpo.index(b"# `O2`")
        infracciones = self.juzgar(cuerpo[:posicion] + b"PROSA QUE NADIE FIRMA\n\n"
                                   + cuerpo[posicion:])
        self.assertTrue(infracciones)

    def test_T349_borrar_las_cabeceras_NO_degrada_el_regimen_a_prefijo(self):
        """T349 · Defecto que previene: apagar el guardián quitándole la estructura.

        Si el régimen se decidiera mirando el fichero de hoy, borrar las cabeceras haría
        que el documento «dejara de tener entradas» y cayera al contraste débil. Se decide
        desde la HISTORIA, así que no hay dónde caer.
        """
        libro = sede.derivar_libro(self.canal, self.RUTA, base=self.base)
        self.assertTrue(sede.tiene_entradas_cerradas(libro),
                        "el régimen entradas-cerradas ya no se deriva de la historia")
        sin_cabeceras = self.leer().replace(b"# `O", b"## O")
        libro_despues = sede.derivar_libro(self.canal, self.RUTA, base=self.base)
        self.escribir(sin_cabeceras)
        self.confirmar("borrar las cabeceras")
        self.assertTrue(sede.tiene_entradas_cerradas(libro_despues),
                        "el régimen entradas-cerradas se ha caído al quitar las cabeceras")
        self.assertTrue(sede.juzgar(libro_despues, sin_cabeceras))

    def test_T349_confirmar_no_exime_y_dos_commits_tampoco(self):
        """T349 · Defecto que previene: blanquear una alteración con un commit encima."""
        cuerpo = self.leer()
        self.juzgar(cuerpo.replace(b"texto resolutivo", b"TEXTO ALTERADO", 1))
        infracciones = self.juzgar(self.leer() + sede.DELIMITADOR + entrada_de_sede(4))
        self.assertIn(sede.ALTERADA, self.codigos(infracciones))


class ElVeredictoAplicaLasEntradasCerradas(ArbolTemporal):
    """`T340`. El régimen de `O27` §3 llega hasta el VEREDICTO, y no se queda en el módulo.

    Sin esta clase, `sede.py` podría estar perfecto y `perimetro._juzgar_append_only` seguir
    decidiendo con `actual.startswith(anterior)`: las pruebas de `sede` pasarían y el
    ataque volvería a dar `hallazgos=0`. Aquí se ejerce `admision.verificar` ENTERO.

    El preámbulo del fixture se conserva TAL CUAL lo escribió `matriz.fundar` —es el bloque
    cerrado anterior a la primera entrada, y cambiarlo sería alterar la sede— y las
    entradas se inscriben encima, que es exactamente lo que la sede real hizo ocho veces.
    """

    PREAMBULO_DEL_FIXTURE = b"# resoluciones\n\n## O1\n\ntexto publicado\n"

    def setUp(self):
        super().setUp()
        self.inscribir([entrada_de_sede(1, con_forma=False)], "inscribir O1")
        self.inscribir([entrada_de_sede(1, con_forma=False), entrada_de_sede(2)],
                       "inscribir O2")

    def inscribir(self, entradas, mensaje):
        cuerpo = sede.DELIMITADOR.join([self.PREAMBULO_DEL_FIXTURE] + list(entradas))
        self.escribir(perimetro.SEDE_DEL_OWNER, cuerpo)
        self.confirmar(mensaje)
        return cuerpo

    def test_T340_el_veredicto_declara_el_REGIMEN_que_ha_aplicado(self):
        """T340 · Defecto que previene: un verde del que nadie puede decir qué significa."""
        veredicto = self.verificar()
        publicado = veredicto.informe["append_only"][perimetro.SEDE_DEL_OWNER]
        self.assertEqual(publicado["regimen"], "entradas-cerradas")
        self.assertEqual([e["identificador"] for e in publicado["entradas_cerradas"]],
                         [sede.PREAMBULO, "O1", "O2"])
        self.assertTrue(publicado["ok"])
        self.assertEqual(veredicto.color, "VERDE")

    def test_T341_anadir_una_resolucion_completa_sigue_siendo_VERDE(self):
        """T341 · Control POSITIVO: el guardián no impide el acto que existe para permitir."""
        self.inscribir([entrada_de_sede(1, con_forma=False), entrada_de_sede(2),
                        entrada_de_sede(3)], "inscribir O3")
        self.assertEqual(self.verificar().color, "VERDE")

    def test_T342_borrar_una_entrada_POSTERIOR_al_nacimiento_da_ROJO_en_el_veredicto(self):
        """T342 · `ADJ-B3` literal: lo que el prefijo del nacimiento dejaba pasar."""
        nacimiento = self.canal.contenido(
            self.canal.commits_de_la_ruta(perimetro.SEDE_DEL_OWNER)[0],
            perimetro.SEDE_DEL_OWNER)
        fabricada = (nacimiento + b"\n\n# `O2` \xc2\xb7 TEXTO FABRICADO\n\n"
                     b"F6 QUEDA CERTIFICADA SIN CONDICIONES.\n")
        self.assertTrue(fabricada.startswith(nacimiento))
        self.escribir(perimetro.SEDE_DEL_OWNER, fabricada)
        self.confirmar("borrado y sustitucion")
        veredicto = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(veredicto.color, "ROJO",
                         "el borrado de una entrada cerrada posterior al nacimiento ha "
                         "pasado: el veredicto no ha dado ROJO")
        hallazgo = [h for h in veredicto.hallazgos
                    if h.ruta == perimetro.SEDE_DEL_OWNER][0]
        self.assertEqual(hallazgo.punto, "V6-12")
        self.assertIn("ALTERACIÓN DE ENTRADAS CERRADAS", hallazgo.causa)

    def test_T344_borrar_la_sede_ENTERA_nombra_todas_las_entradas_perdidas(self):
        """T344 · Defecto que previene: una TRAZA donde tenía que haber un veredicto.

        Sin bytes que juzgar, el canal de presencia literal hacía `x not in None` y el
        proceso moría con `TypeError`. Una traza no es un veredicto, y `V6-03` lo dice para
        el canal de lectura por la misma razón por la que aquí hace falta decirlo.
        """
        os.remove(os.path.join(self.repo, perimetro.SEDE_DEL_OWNER))
        self.confirmar("borrado de la sede entera")
        veredicto = self.verificar(admitidas=[perimetro.SEDE_DEL_OWNER])
        self.assertEqual(veredicto.color, "ROJO")
        publicado = veredicto.informe["append_only"][perimetro.SEDE_DEL_OWNER]
        perdidas = {i["identificador"] for i in publicado["infracciones"]
                    if i["codigo"] == sede.BORRADA}
        self.assertEqual(perdidas, {sede.PREAMBULO, "O1", "O2"})

    def test_T342_una_alteracion_ANTERIOR_a_la_base_no_se_blanquea_por_no_mutar(self):
        """T342 · Defecto que previene: elegir como base el commit del ataque.

        Si el juicio sólo alcanzara a las rutas que el diff contra la base señala, bastaría
        con confirmar la alteración y declarar ESE commit como base: la sede dejaría de
        aparecer como mutación y nadie la miraría.
        """
        cuerpo = self.inscribir([entrada_de_sede(1, con_forma=False),
                                 entrada_de_sede(2, cuerpo="TEXTO ALTERADO")],
                                "alteracion confirmada")
        self.base = self.canal.resolver("HEAD")
        codigo, salida, _ = self.canal_git.ejecutar("status", "--porcelain")
        self.assertEqual(salida.strip(), b"")
        veredicto = self.verificar()
        self.assertEqual(veredicto.color, "ROJO")
        self.assertTrue([h for h in veredicto.hallazgos
                         if h.ruta == perimetro.SEDE_DEL_OWNER])
        self.assertIn(b"TEXTO ALTERADO", cuerpo)


class LaSedeRealDelOwner(unittest.TestCase):
    """`T340`. La propiedad, medida sobre la SEDE DE VERDAD y no sobre un fixture.

    Un fixture demuestra que el mecanismo funciona; esta clase demuestra que funciona
    SOBRE EL DOCUMENTO QUE `O26` §5 convierte en criterio de certificación. Es de sólo
    lectura: no escribe nada en el árbol, y el ataque se aplica en memoria.
    """

    RUTA = "docs/owner/ADS-OWNER-RESOLUCIONES.md"

    @classmethod
    def setUpClass(cls):
        cls.raiz = os.path.dirname(os.path.dirname(os.path.dirname(RAIZ_RUNTIME)))
        with open(os.path.join(cls.raiz, cls.RUTA), "rb") as manejador:
            cls.cuerpo = manejador.read()

    @staticmethod
    def libro_de_la_instantanea(contenido):
        """El libro DERIVADO DE LOS BYTES DE HOY, sin preguntarle nada a Git.

        DECISIÓN · esta clase no depende de que haya `.git`, y se dice por qué
            El anclaje de cada entrada a su commit de introducción lo ejerce
            `AppendOnlyPorEntradaCerrada` sobre repositorios Git reales. Aquí lo que se
            ejerce es OTRA COSA: que la derivación y el juicio funcionen sobre LOS BYTES
            DE LA SEDE DE VERDAD, 44 KB y once entradas, y no sobre un fixture de tres.
            Hacerla depender de Git la volvería inejecutable donde el corpus se copia sin
            historia —que es exactamente como `comprobar_negativos` fabrica sus copias—, y
            un sabotaje que no puede correr no prueba nada.
        """
        return {
            "ruta": LaSedeRealDelOwner.RUTA,
            "commits": ["(instantánea)"],
            "orden": [b.identificador for b in sede.derivar_bloques(contenido)],
            "entradas": {b.identificador: {"commit": "(instantánea)",
                                           "contenido": b.contenido,
                                           "numero": b.numero,
                                           "familia": b.familia}
                         for b in sede.derivar_bloques(contenido)},
            "en_la_base": {b.identificador
                           for b in sede.derivar_bloques(contenido)},
            "base_ilegible": None,
            "incidencias": [],
            "commits_ilegibles": [],
        }

    def test_T340_las_entradas_de_la_sede_real_se_DERIVAN_de_su_estructura(self):
        """T340 · Control POSITIVO: la forma declarada describe la sede que existe."""
        bloques = sede.derivar_bloques(self.cuerpo)
        self.assertEqual(bloques[0].identificador, sede.PREAMBULO)
        numeros = [b.numero for b in bloques[1:]]
        self.assertGreaterEqual(len(numeros), 11)
        self.assertEqual(numeros, list(range(numeros[0], numeros[0] + len(numeros))))
        self.assertTrue(all(b.familia == sede.FAMILIA_CANONICA for b in bloques[1:]))

    def test_T342_el_ataque_de_borrado_sobre_la_sede_REAL_se_detecta(self):
        """T342 · EL ATAQUE, sobre los bytes reales: `hallazgos=0` no se puede repetir."""
        libro = self.libro_de_la_instantanea(self.cuerpo)
        self.assertEqual(sede.juzgar(libro, self.cuerpo), [],
                         "la sede real, intacta, no puede producir infracciones")
        bloques = sede.derivar_bloques(self.cuerpo)
        # El corte del adjudicador: se conservan el preámbulo y las TRES primeras entradas
        # —lo que el prefijo del nacimiento protegía— y se sustituye todo lo demás.
        # Se corta ANTES del delimitador, que es exactamente como lo hizo el adjudicador:
        # el fichero queda con la estructura ROTA, el canal estructural no puede decir qué
        # falta, y quien tiene que hablar es el canal de PRESENCIA LITERAL.
        corte = bloques[4].inicio - len(sede.DELIMITADOR)
        fabricada = (self.cuerpo[:corte] + b"\n\n"
                     + b"# `O26` \xc2\xb7 TEXTO ENTERAMENTE FABRICADO POR EL ADJUDICADOR"
                     b"\n\nF6 QUEDA CERTIFICADA SIN CONDICIONES.\n")
        # La regla ANTERIOR aprobaba esto: lo conservado sigue siendo un prefijo exacto.
        self.assertTrue(self.cuerpo.startswith(self.cuerpo[:corte]))
        infracciones = sede.juzgar(libro, fabricada)
        borradas = {i["identificador"] for i in infracciones if i["codigo"] == sede.BORRADA}
        self.assertTrue(borradas, "el ataque tiene que nombrar las entradas que destruye")
        self.assertGreaterEqual(len(borradas), 6)
        self.assertLess(len(fabricada), len(self.cuerpo))


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
