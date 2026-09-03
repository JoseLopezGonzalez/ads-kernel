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
from admision import censo, formulas, matriz, mutacion, perimetro    # noqa: E402
from admision.perimetro import Declaracion                           # noqa: E402
from gobierno.git import CanalGit                                    # noqa: E402


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
        """T190 · Control POSITIVO: hoy no hay ninguna segunda definición."""
        modulos = censo.modulos_del_aparato(RAIZ_RUNTIME)
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


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
