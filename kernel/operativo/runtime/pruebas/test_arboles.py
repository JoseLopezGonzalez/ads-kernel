#!/usr/bin/env python3
"""test_arboles — batería de `V6-15`, los ÁRBOLES ADVERSARIALES. `T210` a `T213`.

    `T210`  el CONJUNTO se DERIVA de su sede, se valida y detecta duplicados
    `T211`  las VERSIONES HISTÓRICAS vulnerables, con su control del ataque y su control
            del control
    `T212`  la implementación VIGENTE rechaza cada árbol POR LA PROPIEDAD que le toca
    `T213`  la matriz de cuatro columnas, las dos restas de cierre y el punto ejecutable

Todo sobre repositorios Git REALES construidos en temporales, sin red, con el entorno
hermético que fija `gobierno/git.py`, y con la sede documental del propio repositorio.

**NINGÚN CARDINAL DEL CONJUNTO SE ESCRIBE EN ESTA BATERÍA**, y una prueba lo comprueba sobre
el paquete, sobre el punto ejecutable, sobre el contrato derivado y sobre la salida. Es la
regla de `J-07` que §20.5 aplica a esta fila.
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

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

RAIZ_RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ_RUNTIME)

import arboles                                                       # noqa: E402
from arboles import ataques as fixtures                              # noqa: E402
from arboles import derivador, suite, versiones                      # noqa: E402
from gobierno.git import CanalGit                                    # noqa: E402

# La raíz del repositorio: `runtime/` → `operativo/` → `kernel/` → raíz.
RAIZ_REPO = os.path.dirname(os.path.dirname(os.path.dirname(RAIZ_RUNTIME)))
PUNTO_EJECUTABLE = os.path.join(RAIZ_RUNTIME, "ads_arboles.py")


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
#  La suite se EJECUTA UNA VEZ y las pruebas la interrogan
# ===========================================================================
#  Cada fixture funda TRES repositorios Git reales y aplica su ataque; volver a ejecutarla
#  por prueba multiplicaría el coste sin medir nada nuevo. Lo que cada prueba comprueba es
#  una PROPIEDAD DISTINTA del mismo informe, y el informe es determinista.
class SuiteEjecutada(unittest.TestCase):

    informe = None

    @classmethod
    def setUpClass(cls):
        if SuiteEjecutada.informe is None:
            SuiteEjecutada.informe = arboles.ejecutar(RAIZ_REPO)
        cls.informe = SuiteEjecutada.informe


class ArbolTemporalDeSede(unittest.TestCase):
    """Un árbol documental de laboratorio, para los casos que la sede real no puede dar."""

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-sede-")
        self.addCleanup(shutil.rmtree, self.directorio, ignore_errors=True)
        self.evolucion = os.path.join(self.directorio, "docs", "evolucion")
        os.makedirs(self.evolucion)

    def documento(self, nombre, texto):
        destino = os.path.join(self.evolucion, nombre)
        with open(destino, "w", encoding="utf-8") as manejador:
            manejador.write(texto)
        return "docs/evolucion/" + nombre


# ===========================================================================
#  T210 · el CONJUNTO se DERIVA
# ===========================================================================
class ConjuntoDerivado(unittest.TestCase):

    def test_el_conjunto_sale_de_las_cabeceras_y_no_de_una_lista(self):
        """T210 · Defecto que previene: enumerar a mano un conjunto que caduca en silencio."""
        conjunto = arboles.derivar(RAIZ_REPO)
        self.assertTrue(conjunto, "la sede tiene que entregar árboles")
        for arbol in conjunto:
            with self.subTest(arbol=arbol.ordinal):
                self.assertRegex(arbol.cabecera, derivador.PATRON_DE_CABECERA)
                self.assertTrue(arbol.documento.startswith("docs/evolucion/"))
                self.assertFalse(os.path.isabs(arbol.documento))

    def test_cada_entrada_existe_documento_y_cabecera(self):
        """T210 · Defecto que previene: una entrada cuya sede ya no está donde dice."""
        conjunto = arboles.derivar(RAIZ_REPO)
        informe = arboles.exigir_validas(RAIZ_REPO, conjunto)
        self.assertTrue(informe["ok"])
        for fila in informe["entradas"]:
            with self.subTest(arbol=fila["ordinal"]):
                self.assertTrue(fila["documento_presente"])
                self.assertTrue(fila["cabecera_presente"])

    def test_cada_arbol_trae_el_hallazgo_que_lo_cerro(self):
        """T210 · Defecto que previene: un árbol sin el hallazgo que §20.5 exige adjuntarle."""
        for arbol in arboles.derivar(RAIZ_REPO):
            with self.subTest(arbol=arbol.ordinal):
                self.assertTrue(arbol.hallazgos,
                                "§20.5 exige el identificador del hallazgo que lo cerró")
                for hallazgo in arbol.hallazgos:
                    self.assertRegex(hallazgo, r"^[A-Z][A-Z0-9]{0,3}-[0-9]{2}$")

    def test_el_hallazgo_vive_en_el_MISMO_documento(self):
        """T210 · Defecto que previene: adjudicar a un árbol el hallazgo de otro gate."""
        for arbol in arboles.derivar(RAIZ_REPO):
            with open(os.path.join(RAIZ_REPO, arbol.documento),
                      encoding="utf-8") as manejador:
                texto = manejador.read()
            for hallazgo in arbol.hallazgos:
                with self.subTest(arbol=arbol.ordinal, hallazgo=hallazgo):
                    self.assertIn("`" + hallazgo + "`", texto)

    def test_no_se_recoge_la_proposicion_atacada_como_hallazgo(self):
        """T210 · Defecto que previene: confundir la proposición ATACADA con el hallazgo.

        El documento del OCTAVO ÁRBOL titula el ataque del adjudicador «MI ATAQUE A `M-04`
        — ¿HAY UN OCTAVO ÁRBOL?». `M-04` es la proposición general que el árbol ataca, NO un
        hallazgo de ese documento, y el filtro por hallazgos DECLARADOS lo deja fuera.
        """
        por_ordinal = {arbol.ordinal: arbol for arbol in arboles.derivar(RAIZ_REPO)}
        self.assertIn("OCTAVO", por_ordinal)
        self.assertNotIn("M-04", por_ordinal["OCTAVO"].hallazgos)


class DuplicadosYSedeAusente(ArbolTemporalDeSede):

    CABECERA = "## 2 · EL NOVENO ÁRBOL, DE LABORATORIO\n"
    CUERPO = "\n| **`ZZ-01`** | dato | EL NOVENO ÁRBOL, de laboratorio |\n"

    def test_dos_documentos_con_el_mismo_ordinal_son_duplicado(self):
        """T211 · Defecto que previene: reproducir dos veces el mismo árbol creyendo que son dos."""
        self.documento("40-PRIMERO.md", self.CABECERA + self.CUERPO)
        self.documento("41-SEGUNDO.md", self.CABECERA + self.CUERPO)
        conjunto = arboles.derivar(self.directorio)
        self.assertEqual(len(conjunto), 2)
        self.assertTrue(arboles.duplicados(conjunto))
        with self.assertRaises(arboles.ArbolDuplicado):
            arboles.exigir_sin_duplicados(conjunto)

    def test_sin_sede_documental_el_derivador_falla_cerrado(self):
        """T210 · Defecto que previene: devolver el conjunto vacío como si fuera un hecho."""
        vacio = tempfile.mkdtemp(prefix="ads-sin-sede-")
        self.addCleanup(shutil.rmtree, vacio, ignore_errors=True)
        with self.assertRaises(arboles.SedeAusente):
            arboles.derivar(vacio)

    def test_una_cabecera_desplazada_invalida_la_entrada(self):
        """T210 · Defecto que previene: leer una sede distinta de la que se registró."""
        self.documento("40-PRIMERO.md", self.CABECERA + self.CUERPO)
        conjunto = arboles.derivar(self.directorio)
        movido = derivador.Arbol(conjunto[0].ordinal, conjunto[0].documento,
                                 conjunto[0].linea + 5, conjunto[0].cabecera,
                                 conjunto[0].hallazgos)
        with self.assertRaises(arboles.SedeAusente):
            arboles.exigir_validas(self.directorio, [movido])

    def test_un_documento_no_utf8_de_la_sede_se_denuncia(self):
        """T210 · Defecto que previene: interpretar a medias una sede ilegible."""
        destino = os.path.join(self.evolucion, "42-ILEGIBLE.md")
        with open(destino, "wb") as manejador:
            manejador.write(b"## 2 \xff EL NOVENO \xc1RBOL\n")
        with self.assertRaises(arboles.SedeAusente):
            arboles.derivar(self.directorio)


# ===========================================================================
#  T211 · las versiones históricas, con sus dos controles
# ===========================================================================
class VersionesHistoricas(unittest.TestCase):

    def test_cada_version_declara_su_procedencia_documental(self):
        """T211 · Defecto que previene: una «versión histórica» inventada sin sede."""
        for version in versiones.VERSIONES:
            with self.subTest(version=version.identificador):
                procedencia = version.procedencia
                self.assertIn("documento", procedencia)
                self.assertIn("cabecera", procedencia)
                self.assertIn("hallazgo", procedencia)
                self.assertTrue(os.path.isfile(
                    os.path.join(RAIZ_REPO, procedencia["documento"])))
                with open(os.path.join(RAIZ_REPO, procedencia["documento"]),
                          encoding="utf-8") as manejador:
                    texto = manejador.read()
                self.assertIn(procedencia["cabecera"], texto)
                self.assertIn("`" + procedencia["hallazgo"] + "`", texto)
                self.assertTrue(version.ingrediente)

    def test_cada_version_declara_la_propiedad_que_debilita(self):
        """T211 · Defecto que previene: una variante «vulnerable» sin defecto declarado."""
        for version in versiones.VERSIONES:
            with self.subTest(version=version.identificador):
                self.assertGreater(len(version.propiedad_debilitada), 40)

    def test_el_control_del_ataque_falla_si_el_ataque_no_se_aplico(self):
        """T211 · Defecto que previene: una prueba que pasa porque el ataque es un no-op."""
        ataque = fixtures.SegundaSedeNormativaConfirmada()
        directorio = tempfile.mkdtemp(prefix="ads-inerte-")
        self.addCleanup(shutil.rmtree, directorio, ignore_errors=True)
        sano = os.path.join(directorio, "sano")
        atacado = os.path.join(directorio, "atacado")
        ataque.fundar(sano)
        ataque.fundar(atacado)
        with self.assertRaises(arboles.AtaqueInerte):
            ataque.control_del_ataque(sano, atacado,
                                      {"ruta": ataque.RUTA, "porcelain": b""})

    def test_el_control_del_ataque_falla_si_el_ataque_no_se_confirmo(self):
        """T211 · Defecto que previene: presentar un ataque SIN CONFIRMAR como el del gate."""
        ataque = fixtures.SegundaSedeNormativaConfirmada()
        directorio = tempfile.mkdtemp(prefix="ads-sin-commit-")
        self.addCleanup(shutil.rmtree, directorio, ignore_errors=True)
        sano = os.path.join(directorio, "sano")
        atacado = os.path.join(directorio, "atacado")
        ataque.fundar(sano)
        ataque.fundar(atacado)
        datos = ataque.aplicar_control_positivo(atacado, CanalGit(atacado))
        datos["porcelain"] = fixtures._porcelain(atacado)
        self.assertTrue(datos["porcelain"], "sin confirmar, `porcelain` NO está vacío")
        with self.assertRaises(arboles.AtaqueInerte):
            ataque.control_del_ataque(sano, atacado, datos)

    def test_el_control_del_control_esta_en_la_matriz_de_cada_fila(self):
        """T211 · Defecto que previene: una versión vulnerable que diría VERDE a todo."""
        informe = SuiteEjecutada.informe or arboles.ejecutar(RAIZ_REPO)
        SuiteEjecutada.informe = informe
        for fila in informe["matriz"]:
            with self.subTest(fixture=fila["fixture"]):
                control = fila["control_del_control"]
                self.assertEqual(control["veredicto_de_la_version_vulnerable"], "ROJO")
                self.assertTrue(control["ingrediente_retirado"])


# ===========================================================================
#  T212 · la implementación VIGENTE rechaza por la PROPIEDAD correcta
# ===========================================================================
class RechazoPorLaPropiedad(SuiteEjecutada):

    def test_el_arbol_sano_pasa_en_todos_los_fixtures(self):
        """T212 · Defecto que previene: un verificador que diga ROJO a todo pasaría la suite."""
        for fila in self.informe["matriz"]:
            with self.subTest(fixture=fila["fixture"]):
                self.assertTrue(fila["arbol_sano_pasa"])

    def test_el_ataque_existe_en_el_arbol_atacado(self):
        """T212 · Defecto que previene: juzgar un árbol que no lleva el ataque dentro."""
        for fila in self.informe["matriz"]:
            with self.subTest(fixture=fila["fixture"]):
                self.assertIn("diferencia", fila["el_ataque_existe"])
                self.assertTrue(fila["el_ataque_existe"]["diferencia"])

    def test_la_version_vulnerable_acepta_el_arbol_atacado(self):
        """T212 · Defecto que previene: presentar como reproducción algo que nadie aceptó."""
        for fila in self.informe["matriz"]:
            with self.subTest(fixture=fila["fixture"]):
                self.assertEqual(fila["la_version_vulnerable_lo_acepta"]["veredicto"],
                                 "VERDE")

    def test_la_vigente_lo_rechaza_y_la_asercion_nombra_la_propiedad(self):
        """T212 · Defecto que previene: aprobar por un ROJO de otra causa."""
        for fila in self.informe["matriz"]:
            with self.subTest(fixture=fila["fixture"]):
                rechazo = fila["la_vigente_lo_rechaza"]
                self.assertTrue(rechazo["propiedad"])
                self.assertGreater(len(rechazo["propiedad"]), 40)
                self.assertTrue(rechazo["ruta"])
                self.assertTrue(rechazo.get("puntos"))

    def test_la_mutacion_de_un_preexistente_se_rechaza_por_V6_05(self):
        """T212 · Defecto que previene: exención por antigüedad, que es `S1-02` literal."""
        fila = [f for f in self.informe["matriz"]
                if f["fixture"] == "decimo-mutacion-de-preexistente"][0]
        rechazo = fila["la_vigente_lo_rechaza"]
        self.assertIn("preexistente", rechazo["clases"])
        self.assertIn("V6-05", rechazo["puntos"])

    def test_el_borrado_confirmado_se_ve_con_la_letra_D(self):
        """T212 · Defecto que previene: que una sede desaparezca en silencio, que es `T1-02`."""
        fila = [f for f in self.informe["matriz"]
                if f["fixture"] == "undecimo-borrado-confirmado"][0]
        rechazo = fila["la_vigente_lo_rechaza"]
        self.assertIn("D", rechazo["letras"])
        self.assertIn("base", rechazo["referencias"])

    def test_la_ruta_no_ascii_se_lee_identica_byte_a_byte(self):
        """T212 · Defecto que previene: perder una ruta por la citación de `core.quotePath`."""
        fila = [f for f in self.informe["matriz"]
                if f["fixture"] == "decimo-ruta-no-ascii"][0]
        self.assertTrue(fila["la_vigente_lo_rechaza"]["leida_identica"])
        antigua = fila["el_ataque_existe"]["leida_por_la_version_antigua"]
        self.assertNotIn(fila["la_vigente_lo_rechaza"]["ruta"], antigua)

    def test_la_ruta_con_sufijo_de_bytecode_entra_en_el_universo(self):
        """T212 · Defecto que previene: excluir por EXTENSIÓN, que es `DD-01` literal."""
        fila = [f for f in self.informe["matriz"]
                if f["fixture"] == "octavo-sufijo-de-bytecode"][0]
        self.assertTrue(fila["la_vigente_lo_rechaza"]["entro_en_el_universo"])
        self.assertTrue(fila["la_vigente_lo_rechaza"]["ruta"].endswith(".pyc"))

    def test_la_mutacion_confirmada_se_ve_por_la_referencia_base(self):
        """T212 · Defecto que previene: una guarda inerte sobre lo confirmado (`R1-01`)."""
        fila = [f for f in self.informe["matriz"]
                if f["fixture"] == "noveno-segunda-sede-confirmada"][0]
        self.assertIn("base", fila["la_vigente_lo_rechaza"]["referencias"])
        self.assertTrue(fila["la_vigente_lo_rechaza"]["confirmar_no_exime"])

    def test_la_zona_no_cambia_con_el_contenido_del_fichero(self):
        """T212 · Defecto que previene: eximirse del perímetro mutando el propio cuerpo."""
        fila = [f for f in self.informe["matriz"]
                if f["fixture"] == "undecimo-mutacion-fuera-del-perimetro"][0]
        self.assertTrue(fila["la_vigente_lo_rechaza"]["clasificada_por_la_ruta"])
        self.assertTrue(fila["el_ataque_existe"][
            "predicado_de_bytecode_en_el_atacado"])
        self.assertFalse(fila["el_ataque_existe"][
            "predicado_de_bytecode_en_el_sano"])


# ===========================================================================
#  T213 · las dos restas, la matriz y el punto ejecutable
# ===========================================================================
class CierreDeV615(SuiteEjecutada):

    def test_entrada_menos_suite_es_vacio(self):
        """T213 · Defecto que previene: un árbol del conjunto derivado sin fixture."""
        self.assertEqual(self.informe["cruce"]["entrada_menos_suite"], [])

    def test_suite_menos_entrada_es_vacio(self):
        """T213 · Defecto que previene: exigir un árbol que la entrada no entrega."""
        self.assertEqual(self.informe["cruce"]["suite_menos_entrada"], [])

    def test_ningun_fixture_se_adjudica_un_hallazgo_ajeno(self):
        """T213 · Defecto que previene: adjudicarse un árbol por un hallazgo de otro documento."""
        self.assertEqual(self.informe["cruce"]["hallazgos_ajenos"], [])

    def test_una_suite_incompleta_falla_cerrado(self):
        """T213 · Defecto que previene: cerrar `V6-15` con una resta abierta."""
        conjunto = arboles.derivar(RAIZ_REPO)
        recortada = [a for a in fixtures.ATAQUES if a.ordinal != "UNDÉCIMO"]
        with self.assertRaises(arboles.ArbolNoCubierto):
            arboles.exigir_cobertura(conjunto, recortada)

    def test_un_fixture_sin_arbol_falla_cerrado(self):
        """T213 · Defecto que previene: una suite que exige lo que la entrada no entrega."""
        conjunto = [a for a in arboles.derivar(RAIZ_REPO) if a.ordinal != "OCTAVO"]
        with self.assertRaises(arboles.FixtureSinArbol):
            arboles.exigir_cobertura(conjunto)

    def test_cada_fixture_publica_su_documento_y_su_cabecera(self):
        """T213 · Defecto que previene: un fixture sin procedencia, que `V6-15` exige."""
        for fila in self.informe["matriz"]:
            with self.subTest(fixture=fila["fixture"]):
                procedencia = fila["procedencia"]
                self.assertTrue(procedencia["documento"].startswith("docs/evolucion/"))
                self.assertIn("ÁRBOL", procedencia["cabecera"])
                self.assertTrue(procedencia["hallazgo"])

    def test_la_suite_entera_cierra(self):
        """T213 · Defecto que previene: publicar una matriz con una fila en rojo."""
        self.assertTrue(self.informe["ok"])
        for fila in self.informe["matriz"]:
            with self.subTest(fixture=fila["fixture"]):
                self.assertTrue(fila["ok"])

    def test_el_reparto_de_fases_se_conserva(self):
        """T213 · Defecto que previene: mover a `F6` lo que §20.5 asigna a `SIS` en `F4c`."""
        self.assertEqual(self.informe["propietario_de_la_especificacion"], "SIS")
        self.assertEqual(self.informe["fase_de_la_especificacion"], "F4c")
        self.assertEqual(self.informe["fase_de_la_construccion"], "F6")


class PuntoEjecutable(unittest.TestCase):

    def _correr(self, orden, cwd):
        return subprocess.run(
            [sys.executable, PUNTO_EJECUTABLE, "--repo", RAIZ_REPO, orden],
            cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                 "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8", "HOME": cwd},
            check=False,
        )

    def test_el_conjunto_sale_identico_desde_dos_directorios_distintos(self):
        """T213 · Defecto que previene: una evidencia que cambia con el `cwd` de quien la produce."""
        uno = tempfile.mkdtemp(prefix="ads-cwd-a-")
        otro = tempfile.mkdtemp(prefix="ads-cwd-b-")
        self.addCleanup(shutil.rmtree, uno, ignore_errors=True)
        self.addCleanup(shutil.rmtree, otro, ignore_errors=True)
        primera = self._correr("conjunto", uno)
        segunda = self._correr("conjunto", otro)
        self.assertEqual(primera.returncode, 0, primera.stderr.decode())
        self.assertEqual(segunda.returncode, 0, segunda.stderr.decode())
        self.assertEqual(primera.stdout, segunda.stdout)

    def test_la_salida_es_json_con_claves_ordenadas(self):
        """T213 · Defecto que previene: una evidencia cuyo orden depende del diccionario."""
        directorio = tempfile.mkdtemp(prefix="ads-json-")
        self.addCleanup(shutil.rmtree, directorio, ignore_errors=True)
        resultado = self._correr("conjunto", directorio)
        datos = json.loads(resultado.stdout.decode("utf-8"))
        self.assertEqual(datos["punto"], "V6-15")
        vuelto = json.dumps(datos, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
        self.assertEqual(vuelto, resultado.stdout.decode("utf-8"))

    def test_el_cruce_cierra_desde_la_linea_de_ordenes(self):
        """T213 · Defecto que previene: que el instrumento afirme un cierre que no mide."""
        directorio = tempfile.mkdtemp(prefix="ads-cruce-")
        self.addCleanup(shutil.rmtree, directorio, ignore_errors=True)
        resultado = self._correr("cruce", directorio)
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        datos = json.loads(resultado.stdout.decode("utf-8"))
        self.assertEqual(datos["entrada_menos_suite"], [])
        self.assertEqual(datos["suite_menos_entrada"], [])

    def test_ninguna_salida_imprime_una_ruta_absoluta_de_la_maquina(self):
        """T213 · Defecto que previene: publicar el árbol de directorios de quien ejecuta."""
        directorio = tempfile.mkdtemp(prefix="ads-rutas-")
        self.addCleanup(shutil.rmtree, directorio, ignore_errors=True)
        resultado = self._correr("conjunto", directorio)
        texto = resultado.stdout.decode("utf-8")
        self.assertNotIn(RAIZ_REPO, texto)
        self.assertNotIn(directorio, texto)


# ===========================================================================
#  La regla de `J-07`: ni un cardinal del conjunto, en ninguna sede
# ===========================================================================
class SinCardinalesDelConjunto(unittest.TestCase):

    CARDINAL = re.compile(
        r"(?i)\b(dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|"
        r"\d+)\s+(árbol|árboles|arbol|arboles|fixture|fixtures)\b"
    )

    def _sedes(self):
        rutas = [PUNTO_EJECUTABLE]
        paquete = os.path.join(RAIZ_RUNTIME, "arboles")
        for nombre in sorted(os.listdir(paquete)):
            if nombre.endswith(".py"):
                rutas.append(os.path.join(paquete, nombre))
        rutas.append(os.path.join(RAIZ_RUNTIME,
                                  "CONTRATO-ARBOLES-ADVERSARIALES.md"))
        rutas.append(os.path.abspath(__file__))
        return rutas

    def test_ni_el_codigo_ni_el_contrato_escriben_el_cardinal(self):
        """T210 · Defecto que previene: `J-07`, un cardinal al lado de su enumeración."""
        for ruta in self._sedes():
            if not os.path.isfile(ruta):
                continue
            with open(ruta, encoding="utf-8") as manejador:
                for numero, linea in enumerate(manejador, start=1):
                    casado = self.CARDINAL.search(linea)
                    with self.subTest(sede=os.path.basename(ruta), linea=numero):
                        self.assertIsNone(
                            casado,
                            "cardinal escrito: " + (casado.group(0) if casado else ""))

    def test_la_salida_del_instrumento_tampoco_lo_escribe(self):
        """T210 · Defecto que previene: reintroducir el cardinal por la salida."""
        conjunto = arboles.derivar(RAIZ_REPO)
        texto = arboles.serializar({"conjunto": [a.a_dict() for a in conjunto]})
        self.assertIsNone(self.CARDINAL.search(texto))


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
