#!/usr/bin/env python3
"""test_multimaquina — SERIALIZACIÓN ENTRE MÁQUINAS y PUBLICACIÓN GIT REMOTA. `T221`, `T222`.

    `T221`  dos máquinas sobre la misma autoridad: sólo una confirma, la otra DETECTA la
            pérdida, sin `force`, sin historia reescrita, con la obsoleta rechazada y la
            legítima posterior aceptada
    `T222`  caída antes del push · caída después del push y antes del acuse · ref protegida
            que no se borra · remoto manipulado · linaje completo · y la prueba de que la
            serialización NO depende de un `flock` compartido

**NADA DE ESTO ES UN SIMULACRO.** Hay un remoto BARE de verdad, dos clones de verdad, dos
PROCESOS INDEPENDIENTES —`subprocess`, no hilos—, dos identidades de commit distintas,
publicación real de refs por `git push`, el hook `reference-transaction` instalado en el
REMOTO, y concesiones durables escritas por el motor de estado.

LO QUE SERIALIZA, Y LO QUE NO. `g.6` y `g.14` no ponen un cerrojo compartido entre máquinas
—no existe tal cosa cuando los dos clones viven en sistemas de ficheros distintos—. Lo que
serializa es:

    · la CONCESIÓN DURABLE, que dice quién tiene la autoridad y contra qué revisión
    · el CONTRASTE DE REVISIÓN BASE, que compara lo declarado con lo vigente
    · el RECHAZO DEL REMOTO, que es una comparación e intercambio del lado del almacén

`T222` lo demuestra: los dos clones tienen ficheros de bloqueo DISTINTOS, cada uno dentro de
su propio clon, uno puede tomar el suyo sin que el otro se entere, y aun así sólo uno publica.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

RAIZ_RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ_RUNTIME)

import estado                                                        # noqa: E402
import gobierno                                                      # noqa: E402
from gobierno.git import (                                           # noqa: E402
    CONTENIDO_DEL_HOOK,
    NOMBRE_DEL_HOOK,
    NULO,
    CanalGit,
)

REF = gobierno.RAMA_CANONICA
LIMITE_DE_BARRERA = 60.0


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
#  LA MÁQUINA · un PROCESO independiente, no un hilo
# ===========================================================================
#  Se escribe a un fichero temporal FUERA del repositorio y se ejecuta con `subprocess`. Un
#  hilo compartiría el intérprete, la memoria y —lo que aquí importa— el mismo `flock` del
#  proceso: `fcntl.flock` es por DESCRIPTOR y por PROCESO, de modo que dos hilos del mismo
#  proceso no se serializarían igual que dos máquinas. Con procesos, lo que se mide es lo que
#  ocurre de verdad.
GUION_DE_MAQUINA = '''#!/usr/bin/env python3
"""Una MÁQUINA del escenario multimáquina. Proceso independiente, identidad propia."""
import json
import os
import sys
import time

orden = json.loads(sys.argv[1])
sys.path.insert(0, orden["runtime"])

import estado
import gobierno
from gobierno.errores import ErrorDeGobierno

REF = gobierno.RAMA_CANONICA
CODIGO_DE_CAIDA = 70


def publicar(informe):
    with open(orden["salida"], "w", encoding="utf-8") as manejador:
        manejador.write(json.dumps(informe, sort_keys=True, ensure_ascii=False,
                                   indent=2) + "\\n")
        manejador.flush()
        os.fsync(manejador.fileno())


def barrera():
    """Espera a que TODAS las máquinas hayan preparado. Sin esto no habría carrera."""
    if not orden.get("barrera"):
        return
    marca = os.path.join(orden["barrera"], orden["titular"])
    with open(marca, "w", encoding="ascii") as manejador:
        manejador.write("listo")
    limite = time.monotonic() + float(orden.get("limite_de_barrera", 60.0))
    esperadas = int(orden.get("maquinas", 2))
    while time.monotonic() < limite:
        if len(os.listdir(orden["barrera"])) >= esperadas:
            return
        time.sleep(0.02)


informe = {"titular": orden["titular"], "etapa": "arranque"}
try:
    gob = gobierno.GobiernoDelControlRepo(orden["clon"], titular=orden["titular"])
    gob.abrir()
    try:
        # Se trae lo publicado y se parte de la cabeza LOCAL, que es la base declarada.
        gob.canal.ejecutar("fetch", "--quiet", "origin",
                           "refs/heads/canonica:refs/remotes/origin/canonica")
        existe, base = gob.canal.existe_ref(REF)
        informe["base"] = base if existe else "0" * 40
        informe["concesion"] = gob.conceder(REF)
        preparacion = gob.preparar(REF, mensaje=orden["mensaje"],
                                   ficheros={orden["fichero"]:
                                             orden["contenido"].encode("utf-8")})
        informe["commit"] = preparacion["commit"]
        informe["etapa"] = "preparado"
        gob.confirmar(REF, preparacion)
        informe["confirmado_localmente"] = True
        informe["etapa"] = "confirmado-localmente"

        barrera()

        if orden.get("caida") == "antes-del-push":
            publicar(informe)
            os._exit(CODIGO_DE_CAIDA)

        codigo, _, error = gob.canal.ejecutar(
            "push", "origin", "refs/heads/canonica:refs/heads/canonica",
            exigir_exito=False)
        informe["push_codigo"] = codigo
        informe["push_error"] = error.decode("utf-8", "replace").strip()
        informe["publicado"] = codigo == 0
        informe["etapa"] = "publicado" if codigo == 0 else "rechazado-por-el-remoto"

        if orden.get("caida") == "despues-del-push":
            publicar(informe)
            os._exit(CODIGO_DE_CAIDA)

        if codigo == 0:
            # EL ACUSE. Es un objeto durable aparte del linaje: el linaje dice qué publicó
            # ESTA máquina en su ref local, y el acuse dice qué quedó en el REMOTO.
            gob.almacen.aplicar(estado.Transicion(
                tipo="gobierno.publicacion",
                base=gob.almacen.revision()["revision_id"],
                operaciones=[estado.Escritura(
                    "publicaciones/canonica.json",
                    {"ref": REF, "cabeza": preparacion["commit"],
                     "titular": orden["titular"]})],
                autor=orden["titular"],
                motivo="acuse de publicacion en el remoto",
                id="tx-acuse-" + orden["titular"] + "-" + preparacion["commit"][:12],
            ))
            informe["acuse"] = True
            informe["etapa"] = "acusado"
        else:
            # PÉRDIDA DE AUTORIDAD: se RELEE lo vigente y se contrasta. No se adivina.
            gob.canal.ejecutar("fetch", "--quiet", "origin",
                               "refs/heads/canonica:refs/remotes/origin/canonica")
            _, remota = gob.canal.existe_ref("refs/remotes/origin/canonica")
            informe["cabeza_remota"] = remota
            try:
                gob.contrastar_revision_base(REF, remota)
                informe["deteccion"] = "NO detectó la pérdida"
            except ErrorDeGobierno as fallo:
                informe["deteccion"] = fallo.codigo
                informe["deteccion_detalle"] = fallo.detalle
    finally:
        gob.cerrar()
except ErrorDeGobierno as fallo:
    informe["error"] = fallo.codigo
    informe["error_detalle"] = fallo.detalle
except estado.ErrorDeEstado as fallo:
    informe["error"] = fallo.codigo
    informe["error_detalle"] = fallo.detalle

publicar(informe)
'''


class Escenario(unittest.TestCase):
    """Un remoto bare, dos clones, dos identidades. Todo real y todo temporal."""

    def setUp(self):
        self.taller = tempfile.mkdtemp(prefix="ads-multi-")
        self.addCleanup(shutil.rmtree, self.taller, ignore_errors=True)
        self.guion = os.path.join(self.taller, "maquina.py")
        with open(self.guion, "w", encoding="utf-8") as manejador:
            manejador.write(GUION_DE_MAQUINA)

        self.remoto = os.path.join(self.taller, "remoto.git")
        os.makedirs(self.remoto)
        canal_remoto = CanalGit(self.remoto, autor="remoto")
        canal_remoto.ejecutar("init", "--bare", "--quiet",
                              "--initial-branch=canonica")
        # Se DESACTIVA la guarda propia de Git —`denyDeleteCurrent`— a propósito. Si se
        # dejara puesta, el borrado de la rama protegida lo rechazaría Git por una razón
        # suya —«es la rama actual»— y la prueba estaría midiendo una casualidad de la
        # configuración en vez del gobierno. Con ella quitada, quien rechaza es el HOOK, y
        # eso es lo que `PG-3` promete.
        canal_remoto.ejecutar("config", "receive.denyDeleteCurrent", "ignore")
        self.instalar_hook(self.remoto)

        # La SEMILLA: el primer commit, publicado por una máquina que después se retira.
        semilla = os.path.join(self.taller, "semilla")
        os.makedirs(semilla)
        canal_semilla = CanalGit(semilla, autor="semilla")
        canal_semilla.ejecutar("init", "--quiet", "--initial-branch=canonica")
        with open(os.path.join(semilla, "README.md"), "w", encoding="utf-8") as manejador:
            manejador.write("# control repo\n")
        canal_semilla.ejecutar("add", "-A")
        canal_semilla.ejecutar("commit", "--quiet", "-m", "semilla")
        canal_semilla.ejecutar("push", "--quiet", self.remoto,
                               "refs/heads/canonica:refs/heads/canonica")
        self.semilla = canal_semilla.resolver("HEAD")

        self.clones = {}
        for titular in ("runtime-A", "runtime-B"):
            self.clones[titular] = self.clonar(titular)

    # -- utilidades ---------------------------------------------------------
    def instalar_hook(self, repositorio):
        """El MISMO hook del gobierno, instalado en el REMOTO. `G-A8`, mitad imposible."""
        directorio = os.path.join(repositorio, "hooks")
        if not os.path.isdir(directorio):
            directorio = os.path.join(repositorio, ".git", "hooks")
        os.makedirs(directorio, exist_ok=True)
        ruta = os.path.join(directorio, NOMBRE_DEL_HOOK)
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(CONTENIDO_DEL_HOOK)
        os.chmod(ruta, 0o755)
        return ruta

    def clonar(self, titular):
        destino = os.path.join(self.taller, titular)
        CanalGit(self.taller, autor=titular).ejecutar(
            "clone", "--quiet", self.remoto, titular)
        gob = gobierno.inicializar(destino, titular=titular)
        gob.cerrar()
        return destino

    def correr_maquina(self, titular, **extra):
        """Lanza UNA máquina como PROCESO independiente y devuelve su informe."""
        salida = os.path.join(self.taller, "informe-" + titular + ".json")
        orden = {
            "runtime": RAIZ_RUNTIME,
            "clon": self.clones[titular],
            "titular": titular,
            "mensaje": "publicacion de " + titular,
            "fichero": "docs/" + titular + ".md",
            "contenido": "# aportacion de " + titular + "\n",
            "salida": salida,
            "limite_de_barrera": LIMITE_DE_BARRERA,
        }
        orden.update(extra)
        proceso = subprocess.run(
            [sys.executable, self.guion, json.dumps(orden)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                 "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8", "HOME": self.taller},
            cwd=self.taller, check=False)
        return proceso, self._leer(salida)

    def lanzar_maquina(self, titular, **extra):
        """Igual, pero SIN esperar: la carrera necesita a las dos a la vez."""
        salida = os.path.join(self.taller, "informe-" + titular + ".json")
        orden = {
            "runtime": RAIZ_RUNTIME,
            "clon": self.clones[titular],
            "titular": titular,
            "mensaje": "publicacion de " + titular,
            "fichero": "docs/" + titular + ".md",
            "contenido": "# aportacion de " + titular + "\n",
            "salida": salida,
            "limite_de_barrera": LIMITE_DE_BARRERA,
        }
        orden.update(extra)
        proceso = subprocess.Popen(
            [sys.executable, self.guion, json.dumps(orden)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                 "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8", "HOME": self.taller},
            cwd=self.taller)
        return proceso, salida

    def _leer(self, ruta):
        if not os.path.isfile(ruta):
            return {}
        with open(ruta, encoding="utf-8") as manejador:
            return json.load(manejador)

    def carrera(self, **extra_por_titular):
        """Las DOS máquinas a la vez, con barrera, sobre la misma base."""
        barrera = os.path.join(self.taller, "barrera")
        os.makedirs(barrera, exist_ok=True)
        lanzadas = []
        for titular in ("runtime-A", "runtime-B"):
            extra = dict(extra_por_titular.get(titular, {}))
            extra.update({"barrera": barrera, "maquinas": 2})
            lanzadas.append((titular,) + self.lanzar_maquina(titular, **extra))
        informes = {}
        for titular, proceso, salida in lanzadas:
            proceso.wait(timeout=LIMITE_DE_BARRERA + 60)
            informes[titular] = self._leer(salida)
            informes[titular]["codigo_del_proceso"] = proceso.returncode
        return informes

    def cabeza_remota(self):
        canal = CanalGit(self.remoto, autor="lector")
        existe, cabeza = canal.existe_ref(REF)
        return cabeza if existe else NULO

    def historia_remota(self):
        """La primera línea de descendencia del remoto: la cadena de cabezas publicadas."""
        canal = CanalGit(self.remoto, autor="lector")
        _, salida, _ = canal.ejecutar("rev-list", "--first-parent", REF)
        return salida.decode("ascii").split()

    def alcanzables_en_el_remoto(self):
        """TODO lo alcanzable desde la cabeza remota, fusiones incluidas.

        `--first-parent` sigue una sola línea y por eso no sirve para medir «no se ha
        reescrito nada»: tras una fusión, el trabajo del otro cuelga del SEGUNDO padre y
        seguiría estando, aunque `--first-parent` no lo enseñe.
        """
        canal = CanalGit(self.remoto, autor="lector")
        _, salida, _ = canal.ejecutar("rev-list", REF)
        return salida.decode("ascii").split()


# ===========================================================================
#  T221 · la carrera por la autoridad
# ===========================================================================
class CarreraPorLaAutoridad(Escenario):

    def setUp(self):
        super().setUp()
        self.informes = self.carrera()
        self.ganadores = [t for t, i in self.informes.items() if i.get("publicado")]
        self.perdedores = [t for t, i in self.informes.items()
                           if i.get("publicado") is False]

    def test_1_dos_maquinas_intentan_publicar_sobre_la_misma_autoridad(self):
        """T221 · Defecto que previene: una «carrera» en la que sólo corre uno."""
        bases = {t: i.get("base") for t, i in self.informes.items()}
        self.assertEqual(len(set(bases.values())), 1,
                         "las dos máquinas tienen que partir de la MISMA base: " + str(bases))
        self.assertEqual(set(bases.values()), {self.semilla})
        for titular, informe in self.informes.items():
            with self.subTest(maquina=titular):
                self.assertTrue(informe.get("confirmado_localmente"))
                self.assertTrue(informe.get("commit"))

    def test_2_solo_una_confirma(self):
        """T221 · Defecto que previene: dos publicaciones sobre la misma ref."""
        self.assertEqual(len(self.ganadores), 1, self.informes)
        self.assertEqual(len(self.perdedores), 1, self.informes)
        ganador = self.informes[self.ganadores[0]]
        self.assertEqual(self.cabeza_remota(), ganador["commit"])
        self.assertTrue(ganador.get("acuse"))

    def test_3_la_otra_detecta_la_perdida_de_autoridad(self):
        """T221 · Defecto que previene: seguir creyéndose el titular tras perder la ref."""
        perdedor = self.informes[self.perdedores[0]]
        self.assertEqual(perdedor.get("deteccion"), "REVISION_BASE_OBSOLETA")
        self.assertIn("ya no es la cabeza", perdedor.get("deteccion_detalle", ""))
        self.assertEqual(perdedor["cabeza_remota"], self.cabeza_remota())
        self.assertNotIn("acuse", perdedor)

    def test_4_no_hay_force_en_ninguna_parte(self):
        """T221 · Defecto que previene: `g.14`, resolver la carrera forzando la ref."""
        for informe in self.informes.values():
            with self.subTest(maquina=informe["titular"]):
                self.assertNotIn("--force", informe.get("push_error", ""))
        canal = CanalGit(self.clones["runtime-A"], autor="runtime-A")
        for prohibida in (["push", "origin", "--force",
                           "refs/heads/canonica:refs/heads/canonica"],
                          ["push", "origin",
                           "+refs/heads/canonica:refs/heads/canonica"]):
            with self.subTest(orden=prohibida[2]):
                with self.assertRaises(gobierno.GitInvocacionProhibida):
                    canal.ejecutar(*prohibida)

    def test_5_no_hay_historia_reescrita(self):
        """T221 · Defecto que previene: que publicar borre lo publicado antes."""
        historia = self.historia_remota()
        self.assertIn(self.semilla, historia,
                      "la semilla dejó de ser alcanzable: la historia se reescribió")
        ganador = self.informes[self.ganadores[0]]
        self.assertEqual(historia[0], ganador["commit"])

    def test_6_una_publicacion_obsoleta_falla(self):
        """T221 · Defecto que previene: publicar contra una base que ya no es la cabeza."""
        perdedor = self.informes[self.perdedores[0]]
        self.assertNotEqual(perdedor["push_codigo"], 0)
        self.assertIn("rejected", perdedor["push_error"].lower())
        self.assertNotEqual(self.cabeza_remota(), perdedor["commit"])

    def test_7_una_publicacion_legitima_posterior_funciona(self):
        """T221 · Defecto que previene: que perder la carrera deje a la máquina bloqueada."""
        perdedor_titular = self.perdedores[0]
        # La máquina que perdió se pone al día y vuelve a publicar.
        #
        # DECISIÓN · se pone al día FUSIONANDO, y no reescribiendo su rama
        #     Alternativas: (a) `reset` de la rama local a la cabeza vigente; (b) una
        #     FUSIÓN.
        #     Se elige (b), y (a) NO ES POSIBLE aquí, que es la mejor demostración de que
        #     el gobierno funciona: la rama local del perdedor apunta a un commit que NO es
        #     antecesor de la cabeza vigente, de modo que `reset` sería una actualización
        #     no fast-forward y **el hook la aborta**. La vía legítima es la que `g.14` deja
        #     abierta: una confirmación NUEVA que conserva las dos historias.
        canal = CanalGit(self.clones[perdedor_titular], autor=perdedor_titular)
        canal.ejecutar("fetch", "--quiet", "origin",
                       "refs/heads/canonica:refs/remotes/origin/canonica")
        with self.assertRaises(gobierno.GitFallo):
            canal.ejecutar("reset", "--quiet", "--soft",
                           "refs/remotes/origin/canonica")
        canal.ejecutar("merge", "--quiet", "--no-edit",
                       "refs/remotes/origin/canonica")
        proceso, informe = self.correr_maquina(
            perdedor_titular, fichero="docs/" + perdedor_titular + "-2.md",
            contenido="# segunda aportacion\n",
            mensaje="segunda publicacion de " + perdedor_titular)
        self.assertEqual(proceso.returncode, 0, proceso.stderr.decode())
        self.assertTrue(informe.get("publicado"), informe)
        self.assertEqual(self.cabeza_remota(), informe["commit"])
        # Y NADA se ha perdido: el commit del ganador anterior y la semilla siguen
        # alcanzables desde la cabeza. La fusión conserva las dos historias.
        alcanzables = self.alcanzables_en_el_remoto()
        self.assertIn(self.informes[self.ganadores[0]]["commit"], alcanzables)
        self.assertIn(self.informes[perdedor_titular]["commit"], alcanzables)
        self.assertIn(self.semilla, alcanzables)

    def test_las_dos_maquinas_publican_con_IDENTIDADES_distintas(self):
        """T221 · Defecto que previene: dos «máquinas» que son la misma identidad."""
        canal = CanalGit(self.remoto, autor="lector")
        autores = set()
        for informe in self.informes.values():
            codigo, salida, _ = canal.ejecutar(
                "log", "-1", "--format=%an", informe["commit"], exigir_exito=False)
            if codigo == 0:
                autores.add(salida.decode("utf-8").strip())
        self.assertGreaterEqual(len(autores), 1)
        canal_a = CanalGit(self.clones["runtime-A"], autor="runtime-A")
        canal_b = CanalGit(self.clones["runtime-B"], autor="runtime-B")
        self.assertNotEqual(canal_a.entorno()["GIT_AUTHOR_NAME"],
                            canal_b.entorno()["GIT_AUTHOR_NAME"])


# ===========================================================================
#  T222 · caídas, ref protegida, remoto manipulado, linaje y el `flock`
# ===========================================================================
class CaidasYLinaje(Escenario):

    def test_8_una_caida_antes_del_push_se_recupera(self):
        """T222 · Defecto que previene: perder lo confirmado localmente por un corte."""
        proceso, informe = self.correr_maquina("runtime-A", caida="antes-del-push")
        self.assertEqual(proceso.returncode, 70,
                         "el corte tiene que ser un corte de verdad, no un `return`")
        self.assertTrue(informe["confirmado_localmente"])
        self.assertNotIn("push_codigo", informe)
        self.assertEqual(self.cabeza_remota(), self.semilla,
                         "el remoto no puede haberse movido: la caída fue ANTES del push")

        # RECUPERACIÓN: se reabre, se recupera el almacén y se comprueba el linaje.
        with gobierno.GobiernoDelControlRepo(self.clones["runtime-A"],
                                             titular="runtime-A") as gob:
            recuperacion = gob.recuperar()
            self.assertTrue(recuperacion["ok"], recuperacion)
            concesion = gob.exigir_concesion(REF)
            self.assertIn(informe["commit"], concesion["linaje"])
            # Lo confirmado localmente sigue ahí y se puede publicar sin forzar nada.
            codigo, _, _ = gob.canal.ejecutar(
                "push", "origin", "refs/heads/canonica:refs/heads/canonica",
                exigir_exito=False)
            self.assertEqual(codigo, 0)
        self.assertEqual(self.cabeza_remota(), informe["commit"])

    def test_9_una_caida_despues_del_push_y_antes_del_acuse_se_reconcilia(self):
        """T222 · Defecto que previene: republicar lo ya publicado, o darlo por perdido."""
        proceso, informe = self.correr_maquina("runtime-B", caida="despues-del-push")
        self.assertEqual(proceso.returncode, 70)
        self.assertTrue(informe["publicado"])
        self.assertNotIn("acuse", informe)
        self.assertEqual(self.cabeza_remota(), informe["commit"])

        with gobierno.GobiernoDelControlRepo(self.clones["runtime-B"],
                                             titular="runtime-B") as gob:
            recuperacion = gob.recuperar()
            self.assertTrue(recuperacion["ok"], recuperacion)
            # RECONCILIACIÓN: no hay acuse, pero el remoto YA tiene la cabeza. Se
            # comprueba contrastando, no republicando: publicar otra vez sería duplicar.
            with self.assertRaises(estado.ErrorDeEstado):
                gob.almacen.leer("publicaciones/canonica.json")
            self.assertEqual(self.cabeza_remota(), informe["commit"])
            gob.almacen.aplicar(estado.Transicion(
                tipo="gobierno.publicacion",
                base=gob.almacen.revision()["revision_id"],
                operaciones=[estado.Escritura(
                    "publicaciones/canonica.json",
                    {"ref": REF, "cabeza": informe["commit"],
                     "titular": "runtime-B", "reconciliado": True})],
                autor="runtime-B",
                motivo="acuse reconstruido tras la caida",
                id="tx-acuse-reconciliado-" + informe["commit"][:12],
            ))
            acuse = gob.almacen.leer("publicaciones/canonica.json")
            self.assertEqual(acuse["cabeza"], informe["commit"])
            self.assertTrue(acuse["reconciliado"])
            # Y la publicación es IDEMPOTENTE: repetir el push no mueve nada.
            codigo, _, salida = gob.canal.ejecutar(
                "push", "origin", "refs/heads/canonica:refs/heads/canonica",
                exigir_exito=False)
            self.assertEqual(codigo, 0)
            self.assertEqual(self.cabeza_remota(), informe["commit"])

    def test_10_una_ref_protegida_no_puede_borrarse(self):
        """T222 · Defecto que previene: `PG-3`, borrar la rama canónica del remoto."""
        canal = CanalGit(self.clones["runtime-A"], autor="runtime-A")
        codigo, _, error = canal.ejecutar(
            "push", "origin", ":refs/heads/canonica", exigir_exito=False)
        self.assertNotEqual(codigo, 0,
                            "el remoto aceptó borrar una ref PROTEGIDA")
        texto = error.decode("utf-8", "replace")
        self.assertIn("BORRADO de una ref protegida", texto)
        self.assertEqual(self.cabeza_remota(), self.semilla)
        # Y por el canal local, la prohibición es del propio canal y no del hook.
        with gobierno.GobiernoDelControlRepo(self.clones["runtime-A"],
                                             titular="runtime-A") as gob:
            with self.assertRaises(gobierno.RefProtegida):
                gob.canal.retirar_rama(REF, self.semilla,
                                       protegidas=gob.politica.refs_protegidas())

    def test_11_un_remoto_manipulado_no_puede_fingir_autoridad(self):
        """T222 · Defecto que previene: cambiar el remoto por otro con otra historia."""
        proceso, informe = self.correr_maquina("runtime-A")
        self.assertTrue(informe.get("publicado"), informe)
        legitimo = informe["commit"]

        # Un remoto FALSO, con otra historia, que dice ser la autoridad.
        falso = os.path.join(self.taller, "remoto-falso.git")
        os.makedirs(falso)
        CanalGit(falso, autor="impostor").ejecutar(
            "init", "--bare", "--quiet", "--initial-branch=canonica")
        forjado = os.path.join(self.taller, "forjado")
        os.makedirs(forjado)
        canal_forjado = CanalGit(forjado, autor="impostor")
        canal_forjado.ejecutar("init", "--quiet", "--initial-branch=canonica")
        with open(os.path.join(forjado, "README.md"), "w", encoding="utf-8") as manejador:
            manejador.write("# historia forjada\n")
        canal_forjado.ejecutar("add", "-A")
        canal_forjado.ejecutar("commit", "--quiet", "-m", "historia forjada")
        canal_forjado.ejecutar("push", "--quiet", falso,
                               "refs/heads/canonica:refs/heads/canonica")
        cabeza_forjada = canal_forjado.resolver("HEAD")

        with gobierno.GobiernoDelControlRepo(self.clones["runtime-A"],
                                             titular="runtime-A") as gob:
            gob.canal.ejecutar("remote", "set-url", "origin", falso)
            # 1 · EL HOOK ABORTA HASTA EL `fetch`. Git actualiza además la ref de
            #     seguimiento por el refspec configurado del remoto, y esa actualización es
            #     no fast-forward: la transacción de refs entera se aborta y el impostor no
            #     llega ni a entrar en el repositorio.
            with self.assertRaises(gobierno.GitFallo) as fallo_de_fetch:
                gob.canal.ejecutar("fetch", "--quiet", "origin",
                                   "refs/heads/canonica:refs/remotes/origin/impostor")
            self.assertIn("aborted by hook", str(fallo_de_fetch.exception))
            # 2 · el canal se NIEGA a mover la ref a una historia ajena: no es fast-forward.
            gob.canal.ejecutar("fetch", "--quiet", "--no-write-fetch-head", falso,
                               "refs/heads/canonica:refs/remotes/impostor/canonica")
            with self.assertRaises(gobierno.HistoriaNoLineal):
                gob.canal.actualizar_ref(REF, cabeza_forjada, legitimo,
                                         protegidas=gob.politica.refs_protegidas())
            # 3 · y si alguien la moviera por debajo —con el hook quitado—, el LINAJE lo
            #     denuncia igual. Es la mitad DETECTABLE de `G-A8`, que no depende del hook.
            os.remove(gob.ruta_del_hook())
            gob.canal.ejecutar("update-ref", "--no-deref", REF, cabeza_forjada)
            with self.assertRaises(gobierno.ForzadoDetectado) as capturado:
                gob.exigir_refs_intactas()
            self.assertIn(legitimo[:12], str(capturado.exception.contexto["huerfanas"]))

    def test_12_el_linaje_completo_detecta_un_forzado_anterior(self):
        """T222 · Defecto que previene: que un commit legítimo posterior tape un forzado."""
        proceso, primero = self.correr_maquina("runtime-A")
        self.assertTrue(primero.get("publicado"), primero)

        with gobierno.GobiernoDelControlRepo(self.clones["runtime-A"],
                                             titular="runtime-A") as gob:
            # Se RETIRA el hook: el forzado ocurre con el guardián quitado, que es
            # exactamente el escenario que la mitad DETECTABLE de `G-A8` cubre.
            os.remove(gob.ruta_del_hook())
            gob.canal.ejecutar("update-ref", "--no-deref", REF, self.semilla)
            # Y ENCIMA se publica un commit LEGÍTIMO sobre la cabeza forzada.
            with open(os.path.join(self.clones["runtime-A"], "docs", "tapadera.md"),
                      "w", encoding="utf-8") as manejador:
                manejador.write("# commit legitimo posterior\n")
            gob.canal.ejecutar("add", "-A")
            gob.canal.ejecutar("commit", "--quiet", "-m", "commit legitimo posterior")
            cabeza = gob.canal.resolver("HEAD")
            gob.canal.ejecutar("update-ref", "--no-deref", REF, cabeza)

            informe = gob.verificar_refs()
            self.assertFalse(informe["ok"],
                             "el linaje no denunció el forzado tapado por un commit nuevo")
            huerfanas = informe["forzados"][0]["huerfanas"]
            self.assertIn(primero["commit"][:12], huerfanas)
            with self.assertRaises(gobierno.ForzadoDetectado):
                gob.exigir_refs_intactas()

    # -- la serialización NO es un `flock` compartido ------------------------
    def test_la_serializacion_no_depende_de_un_flock_compartido(self):
        """T222 · Defecto que previene: creer que dos máquinas comparten un cerrojo.

        Los dos clones tienen ficheros de bloqueo DISTINTOS, cada uno dentro de su propio
        clon. Una máquina puede tener el suyo tomado mientras la otra trabaja sin enterarse.
        Lo que serializa es la concesión durable, el contraste de revisión base y el rechazo
        del remoto, y la carrera lo demuestra con las dos máquinas corriendo a la vez.
        """
        bloqueos = {}
        for titular, clon in self.clones.items():
            bloqueos[titular] = os.path.realpath(
                estado.abrir(clon).disposicion.bloqueo_escritor()
                if hasattr(estado.abrir(clon), "disposicion")
                else os.path.join(clon, "estado", "operacional", "escritor.lock"))
        self.assertEqual(len(set(bloqueos.values())), 2,
                         "los dos clones comparten fichero de bloqueo: " + str(bloqueos))
        for titular, ruta in bloqueos.items():
            with self.subTest(maquina=titular):
                self.assertTrue(ruta.startswith(
                    os.path.realpath(self.clones[titular]) + os.sep))

        # Con el bloqueo de A TOMADO por un proceso vivo, B opera igual: el cerrojo local
        # no serializa nada entre máquinas.
        import fcntl
        ruta_a = bloqueos["runtime-A"]
        os.makedirs(os.path.dirname(ruta_a), exist_ok=True)
        descriptor = open(ruta_a, "a+b")
        self.addCleanup(descriptor.close)
        fcntl.flock(descriptor.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        proceso, informe = self.correr_maquina("runtime-B")
        fcntl.flock(descriptor.fileno(), fcntl.LOCK_UN)
        self.assertEqual(proceso.returncode, 0, proceso.stderr.decode())
        self.assertTrue(informe.get("publicado"), informe)

        # Y AUN ASÍ sólo una publica: se comprueba con la carrera, cuyo perdedor recibe un
        # rechazo DEL REMOTO y no un fallo de cerrojo.
        canal = CanalGit(self.clones["runtime-A"], autor="runtime-A")
        canal.ejecutar("fetch", "--quiet", "origin",
                       "refs/heads/canonica:refs/remotes/origin/canonica")
        canal.ejecutar("merge", "--quiet", "--no-edit",
                       "refs/remotes/origin/canonica")
        informes = self.carrera()
        publicados = [t for t, i in informes.items() if i.get("publicado")]
        rechazados = [t for t, i in informes.items() if i.get("publicado") is False]
        self.assertEqual(len(publicados), 1, informes)
        self.assertEqual(len(rechazados), 1, informes)
        self.assertIn("rejected", informes[rechazados[0]]["push_error"].lower())
        self.assertEqual(informes[rechazados[0]]["deteccion"], "REVISION_BASE_OBSOLETA")


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
