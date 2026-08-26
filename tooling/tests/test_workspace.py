#!/usr/bin/env python3
"""Pruebas de tooling/workspace.py — sin red, sin GitHub, sin dependencias.

Cada caso construye su propio workspace en un directorio temporal, con repositorios Git
locales `--bare` haciendo de remotos. Nada de lo que aquí se ejecuta sale de la máquina.

    python3 tooling/tests/test_workspace.py

Cubre los veinte casos que exige el mandato multi-repo, más el arranque de extremo a
extremo de `new-project.sh` y el fixture de adopción.
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

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WORKSPACE_PY = os.path.join(RAIZ, "tooling", "workspace.py")
NEW_PROJECT = os.path.join(RAIZ, "tooling", "new-project.sh")

# Identidad de Git para los commits de prueba. Se pasa por entorno para no depender de la
# configuración global de quien ejecute las pruebas, ni modificarla.
ENTORNO = {
    **os.environ,
    "GIT_AUTHOR_NAME": "ads-tests", "GIT_AUTHOR_EMAIL": "tests@ads.local",
    "GIT_COMMITTER_NAME": "ads-tests", "GIT_COMMITTER_EMAIL": "tests@ads.local",
    "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull,
}


def git(args, cwd):
    return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True,
                          env=ENTORNO)


def workspace(args, cwd):
    return subprocess.run([sys.executable, WORKSPACE_PY] + args, cwd=cwd,
                          capture_output=True, text=True, env=ENTORNO)


def workspace_json(args, cwd):
    p = workspace(args + ["--json"], cwd)
    return p.returncode, json.loads(p.stdout)


def crear_remoto_bare(base, nombre, fichero="README.md"):
    """Un repositorio `--bare` local que hace de remoto, con un commit dentro."""
    semilla = os.path.join(base, f".semilla-{nombre}")
    os.makedirs(semilla)
    git(["init", "-q", "-b", "main"], semilla)
    with open(os.path.join(semilla, fichero), "w", encoding="utf-8") as fh:
        fh.write(f"# {nombre}\n")
    git(["add", "-A"], semilla)
    git(["commit", "-qm", "semilla"], semilla)
    bare = os.path.join(base, f"{nombre}.git")
    git(["clone", "-q", "--bare", semilla, bare], base)
    shutil.rmtree(semilla)
    return bare


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ads-ws-")
        self.ws = os.path.join(self.tmp, "producto")
        self.ads = os.path.join(self.ws, "ads")
        os.makedirs(self.ads)
        git(["init", "-q", "-b", "main"], self.ads)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def manifiesto(self, texto):
        with open(os.path.join(self.ads, "SOURCES.toml"), "w", encoding="utf-8") as fh:
            fh.write(texto)

    def base_valida(self):
        return 'schema = 1\n\n[workspace]\nlayout = "siblings"\n'


class TestManifiesto(Base):
    def test_01_manifiesto_vacio_es_valido(self):
        """Un producto nuevo todavía no tiene código. Eso NO es un error."""
        self.manifiesto(self.base_valida())
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 0)
        self.assertTrue(d["ok"])
        self.assertEqual(d["sources"], [])

    def test_02_una_source_valida(self):
        bare = crear_remoto_bare(self.tmp, "frontend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "frontend"\nremote = "{bare}"\npath = "frontend"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 0)
        self.assertEqual(len(d["sources"]), 1)
        self.assertFalse(d["sources"][0]["present"])

    def test_03_varias_sources_validas(self):
        f = crear_remoto_bare(self.tmp, "frontend")
        b = crear_remoto_bare(self.tmp, "backend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "frontend"\nremote = "{f}"\npath = "frontend"\n'
                        f'\n[[sources]]\nid = "backend"\nremote = "{b}"\npath = "backend"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 0)
        self.assertEqual(len(d["sources"]), 2)

    def test_06_path_duplicado(self):
        f = crear_remoto_bare(self.tmp, "frontend")
        b = crear_remoto_bare(self.tmp, "backend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "a"\nremote = "{f}"\npath = "misma"\n'
                        f'\n[[sources]]\nid = "b"\nremote = "{b}"\npath = "misma"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("colisiona" in h["mensaje"] for h in d["hallazgos"]))

    def test_07_id_duplicado(self):
        f = crear_remoto_bare(self.tmp, "frontend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "x"\nremote = "{f}"\npath = "uno"\n'
                        f'\n[[sources]]\nid = "x"\nremote = "{f}"\npath = "dos"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("duplicado" in h["mensaje"] for h in d["hallazgos"]))

    def test_08_escape_con_dos_puntos(self):
        self.manifiesto(self.base_valida() +
                        '\n[[sources]]\nid = "fuga"\nremote = "https://ej.com/r.git"\n'
                        'path = "../../otro-proyecto"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("escapa" in h["mensaje"] for h in d["hallazgos"]))

    def test_09_ruta_absoluta(self):
        self.manifiesto(self.base_valida() +
                        '\n[[sources]]\nid = "abs"\nremote = "https://ej.com/r.git"\n'
                        'path = "/etc"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("absoluta" in h["mensaje"] for h in d["hallazgos"]))

    def test_10_ruta_ads_reservada(self):
        self.manifiesto(self.base_valida() +
                        '\n[[sources]]\nid = "otro"\nremote = "https://ej.com/r.git"\n'
                        'path = "ads"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("reservado" in h["mensaje"] for h in d["hallazgos"]))

    def test_credenciales_en_remoto(self):
        self.manifiesto(self.base_valida() +
                        '\n[[sources]]\nid = "s"\n'
                        'remote = "https://usuario:token@github.com/org/r.git"\npath = "s"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("credenciales" in h["mensaje"] for h in d["hallazgos"]))

    def test_schema_no_soportado(self):
        self.manifiesto('schema = 99\n\n[workspace]\nlayout = "siblings"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("schema" in h["ambito"] for h in d["hallazgos"]))

    def test_layout_no_soportado(self):
        self.manifiesto('schema = 1\n\n[workspace]\nlayout = "nested"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)

    def test_15_componente_con_source_inexistente(self):
        self.manifiesto(self.base_valida() +
                        '\n[[components]]\nid = "web"\nsource = "no-existe"\npath = "."\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("no está declarada" in h["mensaje"] for h in d["hallazgos"]))

    def test_16_component_path_fuera_de_source(self):
        f = crear_remoto_bare(self.tmp, "frontend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "front"\nremote = "{f}"\npath = "front"\n'
                        '\n[[components]]\nid = "web"\nsource = "front"\npath = "../fuera"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("escapa" in h["mensaje"] for h in d["hallazgos"]))

    def test_dos_componentes_misma_source(self):
        """CA-8: dos componentes pueden apuntar a la misma fuente. Monorepo."""
        a = crear_remoto_bare(self.tmp, "app")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "app"\nremote = "{a}"\npath = "app"\n'
                        '\n[[components]]\nid = "web"\nsource = "app"\npath = "apps/web"\n'
                        '\n[[components]]\nid = "api"\nsource = "app"\npath = "apps/api"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 0)
        self.assertEqual(len(d["components"]), 2)
        self.assertEqual({c["source"] for c in d["components"]}, {"app"})


class TestMaterializacion(Base):
    def test_04_clone_de_source_ausente(self):
        bare = crear_remoto_bare(self.tmp, "backend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "backend"\nremote = "{bare}"\npath = "backend"\n')
        cod, d = workspace_json(["init", "backend"], self.ads)
        self.assertEqual(cod, 0)
        self.assertEqual(d["sources"][0]["accion"], "clonada")
        self.assertTrue(os.path.isdir(os.path.join(self.ws, "backend", ".git")))

    def test_05_reutilizacion_de_source_existente(self):
        bare = crear_remoto_bare(self.tmp, "frontend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "frontend"\nremote = "{bare}"\npath = "frontend"\n')
        workspace(["init"], self.ads)
        marca = os.path.join(self.ws, "frontend", "MARCA-LOCAL.txt")
        with open(marca, "w", encoding="utf-8") as fh:
            fh.write("trabajo local\n")
        cod, d = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 0)
        self.assertEqual(d["sources"][0]["accion"], "reutilizada")
        self.assertTrue(os.path.exists(marca), "reutilizar no puede perder trabajo local")

    def test_11_remote_equivocado(self):
        bueno = crear_remoto_bare(self.tmp, "bueno")
        malo = crear_remoto_bare(self.tmp, "malo")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "s"\nremote = "{bueno}"\npath = "s"\n')
        git(["clone", "-q", malo, os.path.join(self.ws, "s")], self.ws)
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("identidad remota distinta" in h["mensaje"] for h in d["hallazgos"]))
        cod, d = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 1)
        self.assertEqual(d["sources"][0]["accion"], "error-otra-identidad")
        self.assertTrue(os.path.isdir(os.path.join(self.ws, "s", ".git")),
                        "el repositorio equivocado NO se destruye")

    def test_12_directorio_no_git(self):
        bare = crear_remoto_bare(self.tmp, "x")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "x"\nremote = "{bare}"\npath = "x"\n')
        ocupado = os.path.join(self.ws, "x")
        os.makedirs(ocupado)
        with open(os.path.join(ocupado, "algo.txt"), "w", encoding="utf-8") as fh:
            fh.write("contenido de alguien\n")
        cod, d = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 1)
        self.assertEqual(d["sources"][0]["accion"], "error-no-git")
        self.assertTrue(os.path.exists(os.path.join(ocupado, "algo.txt")),
                        "un directorio ocupado NO se borra")

    def test_13_repo_dirty_no_se_destruye(self):
        bare = crear_remoto_bare(self.tmp, "d")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "d"\nremote = "{bare}"\npath = "d"\n')
        workspace(["init"], self.ads)
        sucio = os.path.join(self.ws, "d", "README.md")
        with open(sucio, "a", encoding="utf-8") as fh:
            fh.write("cambio sin confirmar\n")
        cod, d = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 0, "estar sucio no es un error")
        with open(sucio, encoding="utf-8") as fh:
            self.assertIn("cambio sin confirmar", fh.read())
        cod, d = workspace_json(["status"], self.ads)
        self.assertTrue(d["sources"][0]["dirty"])
        self.assertTrue(any(h["nivel"] == "WARN" for h in d["hallazgos"]))

    def test_14_remoto_inexistente(self):
        falso = os.path.join(self.tmp, "no-existe.git")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "f"\nremote = "{falso}"\npath = "f"\n')
        cod, d = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 1)
        self.assertEqual(d["sources"][0]["accion"], "error-clone")

    def test_19_seleccion_de_source_en_init(self):
        f = crear_remoto_bare(self.tmp, "frontend")
        b = crear_remoto_bare(self.tmp, "backend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "frontend"\nremote = "{f}"\npath = "frontend"\n'
                        f'\n[[sources]]\nid = "backend"\nremote = "{b}"\npath = "backend"\n')
        cod, d = workspace_json(["init", "frontend"], self.ads)
        self.assertEqual(cod, 0)
        self.assertTrue(os.path.isdir(os.path.join(self.ws, "frontend")))
        self.assertFalse(os.path.exists(os.path.join(self.ws, "backend")),
                         "init selectivo no materializa lo que no se pidió")

    def test_init_de_source_desconocida(self):
        self.manifiesto(self.base_valida())
        cod, d = workspace_json(["init", "fantasma"], self.ads)
        self.assertEqual(cod, 1)
        self.assertTrue(any("no está declarada" in h["mensaje"] for h in d["hallazgos"]))

    def test_source_ausente_no_bloquea_a_las_demas(self):
        """§63: un trabajo de frontend puro continúa aunque falte el backend."""
        f = crear_remoto_bare(self.tmp, "frontend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "frontend"\nremote = "{f}"\npath = "frontend"\n'
                        '\n[[sources]]\nid = "backend"\nremote = "https://ej.com/b.git"\n'
                        'path = "backend"\n')
        workspace(["init", "frontend"], self.ads)
        cod, d = workspace_json(["status"], self.ads)
        self.assertEqual(cod, 0, "una fuente no materializada es INFO, no ERROR")
        por_id = {s["id"]: s for s in d["sources"]}
        self.assertTrue(por_id["frontend"]["present"])
        self.assertFalse(por_id["backend"]["present"])


class TestNormalizacionYSalida(Base):
    def test_17_normalizacion_https_ssh(self):
        sys.path.insert(0, os.path.join(RAIZ, "tooling"))
        from workspace import normalizar_remoto  # noqa: E402
        formas = ["https://github.com/org/repo.git",
                  "git@github.com:org/repo.git",
                  "ssh://git@github.com/org/repo.git",
                  "https://github.com/org/repo"]
        normal = {normalizar_remoto(f) for f in formas}
        self.assertEqual(len(normal), 1, f"deberían ser la misma identidad: {normal}")
        self.assertNotEqual(normalizar_remoto("https://github.com/org/repo.git"),
                            normalizar_remoto("https://github.com/org/otro.git"))

    def test_18_status_json(self):
        f = crear_remoto_bare(self.tmp, "frontend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "frontend"\nremote = "{f}"\npath = "frontend"\n')
        workspace(["init"], self.ads)
        cod, d = workspace_json(["status"], self.ads)
        self.assertEqual(cod, 0)
        s = d["sources"][0]
        for campo in ("id", "path", "present", "branch", "head", "dirty", "remote_ok"):
            self.assertIn(campo, s)
        self.assertEqual(d["ads_root"], self.ads)
        self.assertEqual(d["workspace_root"], self.ws)

    def test_20_ejecucion_desde_subdirectorio(self):
        f = crear_remoto_bare(self.tmp, "frontend")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "frontend"\nremote = "{f}"\npath = "frontend"\n')
        sub = os.path.join(self.ads, "docs", "profundo")
        os.makedirs(sub)
        cod, d = workspace_json(["check"], sub)
        self.assertEqual(cod, 0)
        self.assertEqual(d["ads_root"], self.ads)

    def test_sin_manifiesto_falla_con_codigo_2(self):
        p = workspace(["check"], self.ads)
        self.assertEqual(p.returncode, 2)


class TestBootstrapYAdopcion(unittest.TestCase):
    """Extremo a extremo: new-project.sh y el fixture de adopción."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ads-boot-")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    @unittest.skipUnless(os.path.exists(NEW_PROJECT), "falta new-project.sh")
    def test_bootstrap_crea_workspace_con_ads_dentro(self):
        p = subprocess.run(["bash", NEW_PROJECT, "demo", "--en", self.tmp],
                           capture_output=True, text=True, env=ENTORNO)
        self.assertEqual(p.returncode, 0, p.stderr)
        ws = os.path.join(self.tmp, "demo")
        ads = os.path.join(ws, "ads")
        self.assertTrue(os.path.isdir(ads), "el control repo vive en <workspace>/ads")
        self.assertTrue(os.path.isdir(os.path.join(ads, ".git")))
        self.assertFalse(os.path.exists(os.path.join(ws, ".git")),
                         "el workspace NO es un repositorio Git")
        for esperado in ("SOURCES.toml", "PROJECT.md", "PROFILE.md", "kernel", "tooling"):
            self.assertTrue(os.path.exists(os.path.join(ads, esperado)),
                            f"falta {esperado} en el control repo")
        cod, d = workspace_json(["check"], ads)
        self.assertEqual(cod, 0, f"el proyecto recién creado no valida: {d}")
        self.assertEqual(d["sources"], [], "un proyecto nuevo arranca sin fuentes")

    @unittest.skipUnless(os.path.exists(NEW_PROJECT), "falta new-project.sh")
    def test_adopcion_de_dos_repos_existentes(self):
        """§87: ads + frontend + backend independientes, reconocidos sin volver a clonar."""
        p = subprocess.run(["bash", NEW_PROJECT, "prod", "--en", self.tmp],
                           capture_output=True, text=True, env=ENTORNO)
        self.assertEqual(p.returncode, 0, p.stderr)
        ws, ads = os.path.join(self.tmp, "prod"), os.path.join(self.tmp, "prod", "ads")

        remotos = {n: crear_remoto_bare(self.tmp, n) for n in ("frontend", "backend")}
        for n, bare in remotos.items():
            git(["clone", "-q", bare, os.path.join(ws, n)], ws)

        with open(os.path.join(ads, "SOURCES.toml"), "a", encoding="utf-8") as fh:
            for n, bare in remotos.items():
                fh.write(f'\n[[sources]]\nid = "{n}"\nremote = "{bare}"\npath = "{n}"\n')
            fh.write('\n[[components]]\nid = "web"\nsource = "frontend"\npath = "."\n'
                     'kind = "frontend"\n')

        # una marca local en cada repo: si `init` volviera a clonar, desaparecería
        marcas = {n: os.path.join(ws, n, "MARCA-LOCAL.txt") for n in remotos}
        for m in marcas.values():
            with open(m, "w", encoding="utf-8") as fh:
                fh.write("trabajo previo del equipo\n")

        cod, d = workspace_json(["check"], ads)
        self.assertEqual(cod, 0, d)
        self.assertTrue(all(s["present"] and s["remote_ok"] for s in d["sources"]))

        cod, d = workspace_json(["init"], ads)
        self.assertEqual(cod, 0)
        self.assertTrue(all(s["accion"] == "reutilizada" for s in d["sources"]),
                        "los repos ya clonados se reutilizan, no se vuelven a clonar")
        for n, m in marcas.items():
            self.assertTrue(os.path.exists(m), f"{n}: init destruyó trabajo local")


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
