#!/usr/bin/env python3
"""test_gobierno_git — batería del GOBIERNO GIT del control repo. Escenario `T187`.

Demuestra `g.14` y, sobre todo, `G-A8` de `g.16` con sus DOS mitades y con repositorios Git
REALES:

    IMPOSIBLE    con el hook `reference-transaction` puesto, `git update-ref` no
                 fast-forward FALLA, y el borrado de una ref protegida FALLA
    DETECTABLE   quitado el hook y forzada la ref, `verificar_refs()` la DENUNCIA

Todo con repositorios temporales, sin red, con `GIT_CONFIG_GLOBAL=/dev/null`,
`GIT_CONFIG_SYSTEM=/dev/null`, identidad por variables, `GIT_ALLOW_PROTOCOL=file` y
`GIT_TERMINAL_PROMPT=0`. El entorno lo fija `gobierno/git.py` en el propio canal, y una
prueba lo comprueba en vez de confiar en que se pase.
"""
from __future__ import annotations

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

import estado                                                        # noqa: E402
import gobierno                                                      # noqa: E402
from admision.formulas import digest_de_contenido                    # noqa: E402
from gobierno import propiedad                                       # noqa: E402


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de `tooling/tests/test_workspace.py` a propósito, y no importado: esa batería
    vive en `tooling/` y no está en la ruta de importación del runtime. La salida de estas
    pruebas se PUBLICA como evidencia, y la regla del repositorio es que los artefactos
    generados sean deterministas: «Ran 29 tests in 1.697s» cambia en cada ejecución.
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


class BaseDeGobierno(unittest.TestCase):
    """Funda un control repo temporal con gobierno instalado, y lo retira al terminar."""

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-gob-")
        self.repo = os.path.join(self.directorio, "control")
        os.makedirs(self.repo)
        self.gobierno = gobierno.inicializar(self.repo, titular="runtime-A")
        self.addCleanup(self._retirar)

    def _retirar(self):
        try:
            self.gobierno.cerrar()
        except estado.ErrorDeEstado:
            # Varios casos cierran el almacén a propósito antes de terminar; volver a
            # cerrarlo es un error tipado del motor y NO un fallo de la prueba.
            self.gobierno = None
        shutil.rmtree(self.directorio, ignore_errors=True)

    def _confirmar(self, nombre, contenido):
        ref = gobierno.RAMA_CANONICA
        preparacion = self.gobierno.preparar(ref, mensaje=nombre, ficheros={nombre: contenido})
        return self.gobierno.confirmar(ref, preparacion)

    def _commit_divergente(self):
        """Un commit que NO desciende de la cabeza viva. Es la munición del forzado."""
        canal = self.gobierno.canal
        _, arbol, _ = canal.ejecutar("write-tree")
        _, commit, _ = canal.ejecutar("commit-tree", arbol.decode("ascii").strip(),
                                      "-m", "divergente")
        return commit.decode("ascii").strip()


# ===========================================================================
#  G-A8 · mitad IMPOSIBLE
# ===========================================================================
class HookImposible(BaseDeGobierno):

    def test_el_hook_se_instala_y_su_contenido_se_mide(self):
        """T187 · Defecto que previene: un hook «instalado» que nadie comprueba que sigue ahí."""
        informe = self.gobierno.comprobar_hook()
        self.assertEqual(informe["digest"], gobierno.DIGEST_DEL_HOOK)
        destino = self.gobierno.ruta_del_hook()
        self.assertTrue(os.access(destino, os.X_OK))
        with open(destino, "rb") as manejador:
            contenido = manejador.read()
        self.assertEqual(digest_de_contenido(contenido), gobierno.DIGEST_DEL_HOOK)

    def test_hook_retirado_es_hook_ausente(self):
        """T187 · Defecto que previene: dar por instalada una política que ya no está."""
        os.remove(self.gobierno.ruta_del_hook())
        with self.assertRaises(gobierno.HookAusente) as capturado:
            self.gobierno.comprobar_hook()
        self.assertIn("HOOK_AUSENTE", str(capturado.exception))

    def test_hook_editado_es_hook_ausente(self):
        """T187 · Defecto que previene: un hook editado, que es un hook desactivado."""
        destino = self.gobierno.ruta_del_hook()
        with open(destino, "a", encoding="utf-8") as manejador:
            manejador.write("\nexit 0\n")
        with self.assertRaises(gobierno.HookAusente):
            self.gobierno.comprobar_hook()

    def test_forzado_no_fast_forward_es_rechazado_por_el_hook(self):
        """T187 · Defecto que previene: forzar la rama canónica con el hook puesto."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        resultado = self._confirmar("a.txt", b"uno\n")
        divergente = self._commit_divergente()
        codigo, _, error = self.gobierno.canal.ejecutar(
            "update-ref", gobierno.RAMA_CANONICA, divergente, resultado["nuevo"],
            exigir_exito=False,
        )
        self.assertNotEqual(codigo, 0)
        self.assertIn("NO fast-forward", error.decode("utf-8", "replace"))
        _, cabeza = self.gobierno.canal.existe_ref(gobierno.RAMA_CANONICA)
        self.assertEqual(cabeza, resultado["nuevo"])

    def test_borrado_de_ref_protegida_es_rechazado_por_el_hook(self):
        """T187 · Defecto que previene: borrar la rama canónica y rehacerla a gusto."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        resultado = self._confirmar("a.txt", b"uno\n")
        codigo, _, error = self.gobierno.canal.ejecutar(
            "update-ref", "-d", gobierno.RAMA_CANONICA, resultado["nuevo"],
            exigir_exito=False,
        )
        self.assertNotEqual(codigo, 0)
        self.assertIn("BORRADO", error.decode("utf-8", "replace"))

    def test_una_rama_de_trabajo_si_se_retira(self):
        """T187 · Control POSITIVO: la protección no puede consistir en no dejar hacer nada."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        resultado = self._confirmar("a.txt", b"uno\n")
        self.gobierno.canal.actualizar_ref(
            "refs/heads/trabajo", resultado["nuevo"], gobierno.NULO
        )
        informe = self.gobierno.canal.retirar_rama(
            "refs/heads/trabajo", resultado["nuevo"],
            protegidas=self.gobierno.politica.refs_protegidas(),
        )
        self.assertTrue(informe["retirada"])
        existe, _ = self.gobierno.canal.existe_ref("refs/heads/trabajo")
        self.assertFalse(existe)


# ===========================================================================
#  G-A8 · mitad DETECTABLE
# ===========================================================================
class ForzadoDetectable(BaseDeGobierno):

    def test_forzado_con_el_hook_retirado_es_denunciado(self):
        """T187 · Defecto que previene: quitar el hook, forzar, y que nadie se entere."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        primero = self._confirmar("a.txt", b"uno\n")
        segundo = self._confirmar("b.txt", b"dos\n")
        self.assertTrue(self.gobierno.verificar_refs()["ok"])

        os.remove(self.gobierno.ruta_del_hook())
        divergente = self._commit_divergente()
        codigo, _, _ = self.gobierno.canal.ejecutar(
            "update-ref", gobierno.RAMA_CANONICA, divergente, segundo["nuevo"],
            exigir_exito=False,
        )
        self.assertEqual(codigo, 0, "sin hook, Git deja forzar: por eso hace falta detectar")

        informe = self.gobierno.verificar_refs()
        self.assertFalse(informe["ok"])
        self.assertEqual(len(informe["forzados"]), 1)
        huerfanas = informe["forzados"][0]["huerfanas"]
        self.assertIn(primero["nuevo"][:12], huerfanas)
        self.assertIn(segundo["nuevo"][:12], huerfanas)
        with self.assertRaises(gobierno.ForzadoDetectado) as capturado:
            self.gobierno.exigir_refs_intactas()
        self.assertIn("FORZADO DETECTADO", str(capturado.exception))

    def test_la_deteccion_no_depende_del_hook_para_dar_verde(self):
        """T187 · Control POSITIVO: sin hook y sin forzar, la detección NO denuncia nada."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        self._confirmar("a.txt", b"uno\n")
        os.remove(self.gobierno.ruta_del_hook())
        informe = self.gobierno.verificar_refs()
        self.assertTrue(informe["ok"])
        self.assertIsNone(informe["hook"])
        self.assertIn("hook_diagnostico", informe)

    def test_la_desaparicion_de_una_ref_registrada_se_denuncia(self):
        """T187 · Defecto que previene: borrar la ref por debajo y presentar el árbol limpio."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        resultado = self._confirmar("a.txt", b"uno\n")
        os.remove(self.gobierno.ruta_del_hook())
        self.gobierno.canal.ejecutar(
            "update-ref", "-d", gobierno.RAMA_CANONICA, resultado["nuevo"]
        )
        informe = self.gobierno.verificar_refs()
        self.assertFalse(informe["ok"])
        self.assertIn("DESAPARECIDO", informe["forzados"][0]["causa"])


# ===========================================================================
#  El canal único
# ===========================================================================
class CanalUnico(BaseDeGobierno):

    def test_el_canal_rechaza_las_banderas_de_forzado(self):
        """T187 · Defecto que previene: `--force` colado por cualquier ruta del código."""
        for bandera in ("--force", "--force-with-lease", "-f", "--no-verify"):
            with self.subTest(bandera=bandera):
                with self.assertRaises(gobierno.GitInvocacionProhibida):
                    self.gobierno.canal.ejecutar("push", "origen", bandera)

    def test_el_canal_rechaza_una_refspec_forzada(self):
        """T187 · Defecto que previene: el `+` inicial, que es `--force` con otro nombre."""
        with self.assertRaises(gobierno.GitInvocacionProhibida):
            self.gobierno.canal.ejecutar("push", "origen", "+refs/heads/canonica")

    def test_actualizar_ref_exige_el_valor_viejo_esperado(self):
        """T187 · Defecto que previene: mover una ref sin comparación e intercambio."""
        with self.assertRaises(gobierno.GitInvocacionProhibida) as capturado:
            self.gobierno.canal.actualizar_ref(gobierno.RAMA_CANONICA, "0" * 40, None)
        self.assertIn("valor viejo esperado", str(capturado.exception))

    def test_actualizar_ref_rechaza_la_historia_no_lineal_antes_de_invocar_a_git(self):
        """T187 · Defecto que previene: depender sólo del hook, que se puede quitar."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        resultado = self._confirmar("a.txt", b"uno\n")
        divergente = self._commit_divergente()
        os.remove(self.gobierno.ruta_del_hook())
        with self.assertRaises(gobierno.HistoriaNoLineal):
            self.gobierno.canal.actualizar_ref(
                gobierno.RAMA_CANONICA, divergente, resultado["nuevo"]
            )

    def test_la_comparacion_e_intercambio_falla_si_el_valor_viejo_no_es_el_vigente(self):
        """T187 · Defecto que previene: escribir sobre lo que otro acaba de publicar."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        primero = self._confirmar("a.txt", b"uno\n")
        segundo = self._confirmar("b.txt", b"dos\n")
        tercero = self.gobierno.preparar(
            gobierno.RAMA_CANONICA, mensaje="tres", ficheros={"c.txt": b"tres\n"}
        )
        with self.assertRaises(gobierno.GitFallo):
            # Se declara como viejo el PRIMERO, cuando la ref ya está en el SEGUNDO.
            self.gobierno.canal.actualizar_ref(
                gobierno.RAMA_CANONICA, tercero["commit"], primero["nuevo"]
            )
        _, cabeza = self.gobierno.canal.existe_ref(gobierno.RAMA_CANONICA)
        self.assertEqual(cabeza, segundo["nuevo"])

    def test_el_entorno_de_git_es_hermetico(self):
        """T187 · Defecto que previene: un veredicto que dependa de la config de la máquina."""
        entorno = self.gobierno.canal.entorno()
        self.assertEqual(entorno["GIT_CONFIG_GLOBAL"], os.devnull)
        self.assertEqual(entorno["GIT_CONFIG_SYSTEM"], os.devnull)
        self.assertEqual(entorno["GIT_TERMINAL_PROMPT"], "0")
        self.assertEqual(entorno["GIT_ALLOW_PROTOCOL"], "file")
        self.assertIn("GIT_AUTHOR_NAME", entorno)
        self.assertIn("GIT_COMMITTER_EMAIL", entorno)
        self.assertNotIn("GIT_DIR", entorno)

    def test_retirar_una_ref_protegida_levanta_ref_protegida(self):
        """T187 · Defecto que previene: que la política del canal admita una excepción."""
        with self.assertRaises(gobierno.RefProtegida):
            self.gobierno.canal.retirar_rama(
                gobierno.RAMA_CANONICA, "0" * 40,
                protegidas=self.gobierno.politica.refs_protegidas(),
            )


# ===========================================================================
#  Las once capacidades
# ===========================================================================
class OnceCapacidades(BaseDeGobierno):

    def test_1_representar_propiedad_y_autoridad(self):
        """T187 · Defecto que previene: una autoridad que no se puede consultar."""
        informe = self.gobierno.autoridad("runtime", "confirmar")
        self.assertTrue(informe["puede"])
        self.assertTrue(informe["serializa"])
        self.assertTrue(informe["exige_revision_base"])
        self.assertFalse(self.gobierno.autoridad("agente", "confirmar")["puede"])
        self.assertFalse(self.gobierno.autoridad("verificador-externo", "confirmar")["puede"])

    def test_2_y_8_conceder_y_rechazar_doble_escritor(self):
        """T187 · Defecto que previene: dos titulares con autoridad sobre la misma ref."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        otro = gobierno.GobiernoDelControlRepo(
            self.repo, titular="runtime-B", almacen=self.gobierno.almacen
        )
        with self.assertRaises(gobierno.DobleEscritor):
            otro.conceder(gobierno.RAMA_CANONICA)

    def test_3_contrastar_la_revision_base(self):
        """T187 · Defecto que previene: preparar contra una base que ya no es la vigente."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        self._confirmar("a.txt", b"uno\n")
        with self.assertRaises(gobierno.RevisionBaseObsoleta):
            self.gobierno.contrastar_revision_base(gobierno.RAMA_CANONICA, "0" * 40)

    def test_4_preparar_no_mueve_ninguna_ref(self):
        """T187 · Defecto que previene: preparar y publicar en el mismo acto irrechazable."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        preparacion = self.gobierno.preparar(
            gobierno.RAMA_CANONICA, mensaje="uno", ficheros={"a.txt": b"uno\n"}
        )
        existe, _ = self.gobierno.canal.existe_ref(gobierno.RAMA_CANONICA)
        self.assertFalse(existe, "preparar NO publica")
        self.assertEqual(preparacion["base"], gobierno.NULO)

    def test_5_validar_la_politica_rechaza_al_actor_sin_autoridad(self):
        """T187 · Defecto que previene: confirmar sin que la política lo autorice."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        preparacion = self.gobierno.preparar(
            gobierno.RAMA_CANONICA, mensaje="uno", ficheros={"a.txt": b"uno\n"}
        )
        with self.assertRaises(gobierno.PoliticaViolada):
            self.gobierno.confirmar(gobierno.RAMA_CANONICA, preparacion, actor="agente")

    def test_6_confirmar_publica_y_registra_el_linaje(self):
        """T187 · Defecto que previene: confirmar sin dejar linaje que denuncie un forzado."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        primero = self._confirmar("a.txt", b"uno\n")
        segundo = self._confirmar("b.txt", b"dos\n")
        self.assertEqual(primero["linaje"], 1)
        self.assertEqual(segundo["linaje"], 2)
        self.assertEqual(segundo["latido"], 2)
        self.assertEqual(segundo["modo"], "comparacion-e-intercambio")

    def test_7_detectar_perdida_de_autoridad(self):
        """T187 · Defecto que previene: escribir con una autoridad que ya no se tiene."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        # Otro titular releva la concesión por la vía durable, sin avisar a éste.
        logica = "refs/refs.heads.canonica.json"
        cuerpo = dict(self.gobierno.almacen.leer(logica))
        cuerpo["titular"] = "runtime-B"
        cuerpo["epoca"] = cuerpo["epoca"] + 1
        self.gobierno.almacen.aplicar(estado.Transicion(
            tipo="gobierno.relevo",
            base=self.gobierno.almacen.revision()["revision_id"],
            operaciones=[estado.Escritura(logica, cuerpo)],
            autor="runtime-B", motivo="relevo", id="tx-relevo-1",
        ))
        with self.assertRaises(gobierno.AutoridadDeRefNoConcedida) as capturado:
            self.gobierno.exigir_concesion(gobierno.RAMA_CANONICA)
        self.assertIn("bajo los pies", str(capturado.exception))

    def test_confirmar_sin_concesion_no_publica(self):
        """T187 · Defecto que previene: publicar sin haber pedido autoridad nunca."""
        preparacion = self.gobierno.preparar(
            gobierno.RAMA_CANONICA, mensaje="uno", ficheros={"a.txt": b"uno\n"}
        )
        with self.assertRaises(gobierno.AutoridadDeRefNoConcedida):
            self.gobierno.confirmar(gobierno.RAMA_CANONICA, preparacion)
        existe, _ = self.gobierno.canal.existe_ref(gobierno.RAMA_CANONICA)
        self.assertFalse(existe)

    def test_11_la_evidencia_es_determinista_y_sin_rutas_absolutas(self):
        """T187 · Defecto que previene: publicar evidencia con el árbol de la máquina dentro."""
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        self._confirmar("a.txt", b"uno\n")
        evidencia = self.gobierno.evidencia()
        texto = json.dumps(evidencia, sort_keys=True, ensure_ascii=False)
        self.assertNotIn(self.directorio, texto)
        self.assertNotIn(os.path.expanduser("~"), texto)
        self.assertEqual(evidencia["politica"]["ruta"], propiedad.RUTA_EN_EL_ARBOL)
        # Determinismo: dos lecturas seguidas producen los mismos bytes.
        self.assertEqual(texto,
                         json.dumps(self.gobierno.evidencia(), sort_keys=True,
                                    ensure_ascii=False))


# ===========================================================================
#  Estado parcial, recuperación y serialización entre PROCESOS
# ===========================================================================
_GUION_ESCRITOR = """
import os, sys
sys.path.insert(0, {runtime!r})
import gobierno
g = gobierno.GobiernoDelControlRepo({repo!r}, titular={titular!r})
g.abrir()
try:
    g.conceder(gobierno.RAMA_CANONICA)
    p = g.preparar(gobierno.RAMA_CANONICA, mensaje={titular!r},
                   ficheros={{{titular!r} + ".txt": b"x"}})
    r = g.confirmar(gobierno.RAMA_CANONICA, p)
    sys.stdout.write("OK " + r["nuevo"] + "\\n")
except gobierno.ErrorDeGobierno as error:
    sys.stdout.write("NO " + error.codigo + "\\n")
except Exception as error:
    # Se captura ancho A PROPOSITO y SOLO en este guion de prueba: lo que se mide es que
    # el segundo escritor NO publica, y el codigo concreto con que se le niega la
    # autoridad puede venir del motor de estado o del gobierno.
    sys.stdout.write("NO " + getattr(error, "codigo", type(error).__name__) + "\\n")
finally:
    g.cerrar()
"""

_GUION_CAIDA = """
import os, sys
sys.path.insert(0, {runtime!r})
import estado
os.environ["ADS_ESTADO_FALLO"] = "antes-del-commit-atomico"
alm = estado.abrir({repo!r}, recuperar=False)
alm.aplicar(estado.Transicion(
    tipo="gobierno.prueba", base=alm.revision()["revision_id"],
    operaciones=[estado.Escritura("pruebas/interrumpida.json", {{"x": 1}})],
    autor="runtime-A", motivo="caida provocada", id="tx-caida-1"))
sys.stdout.write("NO DEBERIA LLEGAR\\n")
"""


class SerializacionYRecuperacion(BaseDeGobierno):

    def _correr(self, guion):
        ruta = os.path.join(self.directorio, "guion.py")
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(guion)
        proceso = subprocess.run(
            [sys.executable, ruta], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            check=False,
        )
        return proceso

    def test_9_dos_procesos_reales_se_serializan_y_uno_solo_publica(self):
        """T187 · Defecto que previene: dos escritores publicando a la vez en la canónica."""
        self.gobierno.cerrar()
        guiones = []
        for titular in ("runtime-A", "runtime-B"):
            ruta = os.path.join(self.directorio, "e-" + titular + ".py")
            with open(ruta, "w", encoding="utf-8") as manejador:
                manejador.write(_GUION_ESCRITOR.format(
                    runtime=RAIZ_RUNTIME, repo=self.repo, titular=titular))
            guiones.append(ruta)
        procesos = [subprocess.Popen([sys.executable, ruta], stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
                    for ruta in guiones]
        salidas = []
        for proceso in procesos:
            salida, _ = proceso.communicate(timeout=120)
            salidas.append(salida.decode("utf-8", "replace").strip())
        exitos = [linea for linea in salidas if linea.startswith("OK")]
        self.assertEqual(len(exitos), 1,
                         "exactamente UNO publica; el otro no comparte la autoridad")
        fallos = [linea for linea in salidas if linea.startswith("NO")]
        self.assertEqual(len(fallos), 1)
        self.assertIn(fallos[0].split()[1],
                      ("DOBLE_ESCRITOR", "REVISION_OBSOLETA", "ESCRITOR_CONCURRENTE",
                       "REINTENTOS_AGOTADOS", "REVISION_BASE_OBSOLETA", "GIT_FALLO",
                       "AUTORIDAD_DE_REF_NO_CONCEDIDA"))
        self.gobierno = gobierno.GobiernoDelControlRepo(self.repo, titular="runtime-C")
        self.gobierno.abrir()
        self.assertTrue(self.gobierno.verificar_refs()["ok"])

    def test_10_recuperar_tras_una_caida_real(self):
        """T187 · Defecto que previene: arrancar sobre una ventana abierta y publicar mezcla."""
        # La concesión se obtiene ANTES del corte: el motor no admite `aplicar` con la
        # ventana abierta, así que pedirla después mediría otra cosa.
        self.gobierno.conceder(gobierno.RAMA_CANONICA)
        self.gobierno.cerrar()
        ruta = os.path.join(self.directorio, "caida.py")
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(_GUION_CAIDA.format(runtime=RAIZ_RUNTIME, repo=self.repo))
        proceso = subprocess.run([sys.executable, ruta], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, check=False)
        self.assertEqual(proceso.returncode, 70, "el corte tiene que ser real")

        almacen = estado.abrir(self.repo, recuperar=False)
        self.addCleanup(almacen.cerrar)
        self.assertNotEqual(almacen.estado_de_la_ventana(), "cerrada")
        parcial = gobierno.GobiernoDelControlRepo(
            self.repo, titular="runtime-A", almacen=almacen
        )
        preparacion = parcial.preparar(
            gobierno.RAMA_CANONICA, mensaje="uno", ficheros={"a.txt": b"uno\n"}
        )
        with self.assertRaises(gobierno.EstadoParcialEnLaRama) as capturado:
            parcial.confirmar(gobierno.RAMA_CANONICA, preparacion)
        self.assertIn("NUNCA contiene estado parcial", str(capturado.exception))
        existe, _ = parcial.canal.existe_ref(gobierno.RAMA_CANONICA)
        self.assertFalse(existe, "la rama canónica no recibió el estado parcial")

        informe = parcial.recuperar()
        self.assertEqual(almacen.estado_de_la_ventana(), "cerrada")
        self.assertTrue(informe["refs"]["ok"])


# ===========================================================================
#  La política como DATO, y su auto-inclusión
# ===========================================================================
class PoliticaComoDato(unittest.TestCase):

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-pol-")
        self.addCleanup(shutil.rmtree, self.directorio, True)

    def test_la_politica_declara_las_ocho_operaciones_de_g14(self):
        """T187 · Defecto que previene: una tabla de propiedad con huecos."""
        politica = propiedad.cargar()
        for operacion in propiedad.OPERACIONES_EXIGIDAS:
            with self.subTest(operacion=operacion):
                self.assertIn(operacion, politica.operaciones())

    def test_la_publicacion_por_defecto_es_esperando_owner(self):
        """T187 · Defecto que previene: que la ausencia de política signifique «publica»."""
        politica = propiedad.cargar()
        self.assertEqual(politica.publicacion_por_defecto(), "esperando-owner")

    def test_la_raiz_externa_no_escribe_nada(self):
        """T187 · Defecto que previene: `g.12` incumplido por una lista ausente."""
        politica = propiedad.cargar()
        self.assertEqual(politica.escribe("verificador-externo"), ())
        self.assertFalse(politica.puede_escribir("verificador-externo", "estado/canonico/x"))

    def test_la_politica_no_puede_eximirse_a_si_misma(self):
        """T187 · Defecto que previene: una política que se saca del alcance del verificador."""
        with open(propiedad.ruta_por_defecto(), "r", encoding="utf-8") as manejador:
            texto = manejador.read()
        mutada = texto.replace(
            "    - kernel/operativo/runtime/gobierno/\n", ""
        )
        self.assertNotEqual(texto, mutada, "la política tiene que declarar su propio prefijo")
        ruta = os.path.join(self.directorio, "POLITICA-CONTROL-REPO.yml")
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(mutada)
        with self.assertRaises(gobierno.PoliticaViolada) as capturado:
            propiedad.cargar(ruta)
        self.assertIn("no se incluye a sí misma", str(capturado.exception))

    def test_una_politica_que_autoriza_el_borrado_protegido_se_rechaza(self):
        """T187 · Defecto que previene: `g.14` dice que NINGUNA política puede autorizarlo."""
        with open(propiedad.ruta_por_defecto(), "r", encoding="utf-8") as manejador:
            texto = manejador.read()
        mutada = texto.replace("  borrado_permitido: []",
                               "  borrado_permitido: [refs/heads/canonica]")
        ruta = os.path.join(self.directorio, "POLITICA-CONTROL-REPO.yml")
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(mutada)
        with self.assertRaises(gobierno.PoliticaViolada) as capturado:
            propiedad.cargar(ruta)
        self.assertIn("ninguna política", str(capturado.exception))

    def test_una_politica_sin_clave_obligatoria_no_se_completa_sola(self):
        """T187 · Defecto que previene: que una clave ausente signifique «sin restricción»."""
        ruta = os.path.join(self.directorio, "POLITICA-CONTROL-REPO.yml")
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write("version: 1\nactores:\n  - id: owner\n    descripcion: x\n")
        with self.assertRaises(gobierno.PoliticaViolada) as capturado:
            propiedad.cargar(ruta)
        self.assertIn("NUNCA significa", str(capturado.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
