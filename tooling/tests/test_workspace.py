#!/usr/bin/env python3
"""Pruebas de tooling/workspace.py — sin red, sin GitHub, sin dependencias.

Cada caso construye su propio workspace en un directorio temporal, con repositorios Git
locales `--bare` haciendo de remotos. Nada de lo que aquí se ejecuta sale de la máquina.

    python3 tooling/tests/test_workspace.py

Cubre los veinte casos que exige el mandato multi-repo, el arranque de extremo a extremo
de `new-project.sh`, el fixture de adopción, la RECONSTRUCCIÓN de un producto de cuatro
fuentes, y la batería ADVERSARIAL: lo que una revisión externa consiguió hacerle a la
herramienta y la batería anterior no veía.

La batería adversarial no comprueba que la herramienta funcione. Comprueba que NO hace lo
que no debe: no escribe fuera del workspace por un enlace simbólico, no clona con un
manifiesto roto, no imprime un secreto, no iguala dos repositorios distintos y no revienta
con un tipo que no esperaba.
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
    # SIN RED, y no por costumbre: Git sólo tiene permitido el transporte `file`. Un
    # `clone` por https o por ssh muere con «transport not allowed» antes de resolver un
    # nombre. «Estas pruebas no salen de la máquina» deja de ser una promesa del comentario
    # y pasa a ser una condición que la prueba 44 comprueba.
    "GIT_ALLOW_PROTOCOL": "file",
    "GIT_TERMINAL_PROMPT": "0",
}


# Marcador que NO puede aparecer en ninguna salida. Si sale, hay una fuga: no se busca
# «token» ni «password», se busca ESTE literal, que sólo existe en la entrada de la prueba.
MARCADOR = "ZZ-marcador-secreto-de-prueba-9f3a1c"


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
    def test_bootstrap_nace_en_la_rama_que_documenta(self):
        """El script documenta `git push -u origin main` y creaba `master`.

        `git init` sin `-b` toma la rama de `init.defaultBranch`. ENTORNO apunta
        GIT_CONFIG_GLOBAL y GIT_CONFIG_SYSTEM a /dev/null, así que esto se ejecuta con la
        configuración global VACÍA, que es donde el defecto aparece.
        """
        p = subprocess.run(["bash", NEW_PROJECT, "rama", "--en", self.tmp],
                           capture_output=True, text=True, env=ENTORNO)
        self.assertEqual(p.returncode, 0, p.stderr)
        ads = os.path.join(self.tmp, "rama", "ads")
        rama = git(["rev-parse", "--abbrev-ref", "HEAD"], ads).stdout.strip()
        self.assertEqual(rama, "main", "el control repo no nació en la rama documentada")
        # y el comando que el propio script imprime nombra ESA rama, no otra
        documentado = re.search(r"git push -u origin (\S+)", p.stdout)
        self.assertIsNotNone(documentado, p.stdout)
        self.assertEqual(documentado.group(1), rama,
                         "el comando documentado y la rama creada no son la misma")

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


# ===========================================================================
# BATERÍA ADVERSARIAL
#
# Cada prueba de aquí abajo REPRODUCE un defecto que una revisión externa consiguió
# provocar sobre la implementación anterior, y que las veintinueve pruebas de arriba no
# detectaban. Todas fallan contra aquel código y pasan contra éste.
# ===========================================================================
class TestEscapeDeRaiz(Base):
    """Ninguna fuente ni componente sale de su raíz autorizada. Ni por texto, ni por enlace."""

    def test_21_escape_por_enlace_simbolico_en_source(self):
        """`normpath` es textual y no ve un symlink: la ruta parece relativa y no lo es."""
        fuera = os.path.join(self.tmp, "FUERA-DEL-WORKSPACE")
        os.makedirs(fuera)
        os.symlink(fuera, os.path.join(self.ws, "puente"))
        bare = crear_remoto_bare(self.tmp, "x")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "x"\nremote = "{bare}"\npath = "puente/dentro"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1, f"un enlace simbólico no puede sacar una fuente: {d}")
        self.assertTrue(any("enlaces simbólicos" in h["mensaje"] for h in d["hallazgos"]), d)
        cod, _ = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 1)
        self.assertFalse(os.path.exists(os.path.join(fuera, "dentro")),
                         "init escribió FUERA del workspace")

    def test_22_escape_por_enlace_simbolico_en_componente(self):
        """La misma comprobación, con la fuente como raíz autorizada del componente."""
        bare = crear_remoto_bare(self.tmp, "app")
        os.makedirs(os.path.join(self.ws, "app"))
        fuera = os.path.join(self.tmp, "OTRO-REPO")
        os.makedirs(fuera)
        os.symlink(fuera, os.path.join(self.ws, "app", "enlace"))
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "app"\nremote = "{bare}"\npath = "app"\n'
                        '\n[[components]]\nid = "web"\nsource = "app"\npath = "enlace/web"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 1, d)
        self.assertTrue(any("enlaces simbólicos" in h["mensaje"] for h in d["hallazgos"]), d)

    def test_23_source_dentro_del_control_repo(self):
        """C6: prohibido clonar las fuentes DENTRO del control repo.

        Rechazar exactamente `path = "ads"` no basta: `ads/frontend`, `./ads/sub` y
        `ads/../ads/z` son la misma prohibición escrita de otra manera.
        """
        bare = crear_remoto_bare(self.tmp, "y")
        for ruta in ("ads/frontend", "./ads/sub", "ads/../ads/z", "ads/"):
            with self.subTest(ruta=ruta):
                self.manifiesto(self.base_valida() +
                                f'\n[[sources]]\nid = "y"\nremote = "{bare}"\npath = "{ruta}"\n')
                cod, d = workspace_json(["check"], self.ads)
                self.assertEqual(cod, 1, f"'{ruta}' cae dentro del control repo: {d}")

    def test_24_source_en_la_raiz_del_workspace(self):
        """`path = "."` haría del workspace un repositorio Git, que es lo que C6 prohíbe."""
        bare = crear_remoto_bare(self.tmp, "z")
        for ruta in (".", "./", "app/.."):
            with self.subTest(ruta=ruta):
                self.manifiesto(self.base_valida() +
                                f'\n[[sources]]\nid = "z"\nremote = "{bare}"\npath = "{ruta}"\n')
                cod, d = workspace_json(["check"], self.ads)
                self.assertEqual(cod, 1, f"'{ruta}' resuelve a la raíz del workspace: {d}")
                self.assertTrue(any("raíz" in h["mensaje"] for h in d["hallazgos"]), d)

    def test_25_colision_jerarquica_entre_sources(self):
        """Dos rutas distintas pueden seguir anidando un repositorio Git dentro de otro."""
        a = crear_remoto_bare(self.tmp, "a")
        b = crear_remoto_bare(self.tmp, "b")
        for p1, p2 in (("app", "app/interno"), ("app/interno", "app"), ("a/b/c", "a/b")):
            with self.subTest(p1=p1, p2=p2):
                self.manifiesto(self.base_valida() +
                                f'\n[[sources]]\nid = "uno"\nremote = "{a}"\npath = "{p1}"\n'
                                f'\n[[sources]]\nid = "dos"\nremote = "{b}"\npath = "{p2}"\n')
                cod, d = workspace_json(["check"], self.ads)
                self.assertEqual(cod, 1, f"'{p1}' y '{p2}' anidan repositorios: {d}")
                self.assertTrue(any("colisiona" in h["mensaje"] for h in d["hallazgos"]), d)

    def test_25b_rutas_hermanas_con_prefijo_comun_son_validas(self):
        """`app` y `app-movil` comparten prefijo y NO anidan. Comparar por prefijo de
        cadena las rechazaría, y sería un falso positivo."""
        a = crear_remoto_bare(self.tmp, "a")
        b = crear_remoto_bare(self.tmp, "b")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "uno"\nremote = "{a}"\npath = "app"\n'
                        f'\n[[sources]]\nid = "dos"\nremote = "{b}"\npath = "app-movil"\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 0, d)


class TestInitAtomico(Base):
    """`init` es la única orden que MUTA. Con el manifiesto roto, no toca el disco."""

    MANIFIESTOS_ROTOS = {
        "layout no soportado": 'layout = "nested"',
        "layout ausente": None,
    }

    def _con_fuente_valida(self, cabecera, bare):
        return cabecera + f'\n[[sources]]\nid = "buena"\nremote = "{bare}"\npath = "buena"\n'

    def test_26_manifiesto_invalido_no_clona_ni_crea_directorios(self):
        bare = crear_remoto_bare(self.tmp, "buena")
        casos = {
            "layout no soportado": 'schema = 1\n\n[workspace]\nlayout = "nested"\n',
            "schema no soportado": 'schema = 99\n\n[workspace]\nlayout = "siblings"\n',
            "schema ausente": '[workspace]\nlayout = "siblings"\n',
            "workspace ausente": 'schema = 1\n',
            "otra fuente con credenciales": (
                'schema = 1\n\n[workspace]\nlayout = "siblings"\n'
                f'\n[[sources]]\nid = "mala"\nremote = "https://u:{MARCADOR}@ej.invalid/r.git"\n'
                'path = "mala"\n'),
            "otra fuente con id inválido": (
                'schema = 1\n\n[workspace]\nlayout = "siblings"\n'
                '\n[[sources]]\nid = "../fuga"\nremote = "https://ej.invalid/r.git"\n'
                'path = "mala"\n'),
            "componente con tipo inválido": (
                'schema = 1\n\n[workspace]\nlayout = "siblings"\n'
                '\n[[components]]\nid = "web"\nsource = "buena"\nkind = 7\n'),
        }
        for nombre, cabecera in casos.items():
            with self.subTest(caso=nombre):
                for sobrante in os.listdir(self.ws):
                    if sobrante != "ads":
                        shutil.rmtree(os.path.join(self.ws, sobrante), ignore_errors=True)
                self.manifiesto(self._con_fuente_valida(cabecera, bare))
                cod, d = workspace_json(["init"], self.ads)
                self.assertEqual(cod, 1, d)
                self.assertEqual(d["sources"], [],
                                 "init registró acciones con el manifiesto roto")
                self.assertTrue(any("NO ha ejecutado ninguna acción" in h["mensaje"]
                                    for h in d["hallazgos"]), d)
                self.assertEqual(sorted(os.listdir(self.ws)), ["ads"],
                                 f"[{nombre}] init creó algo en el workspace")

    def test_26b_el_mismo_manifiesto_corregido_si_materializa(self):
        """La contraparte: sin el error, la fuente válida se clona. Si no, la prueba de
        arriba pasaría por no hacer nada nunca."""
        bare = crear_remoto_bare(self.tmp, "buena")
        self.manifiesto(self._con_fuente_valida(self.base_valida(), bare))
        cod, d = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 0, d)
        self.assertEqual(d["sources"][0]["accion"], "clonada")
        self.assertTrue(os.path.isdir(os.path.join(self.ws, "buena", ".git")))


class TestSecretos(Base):
    """Ningún secreto sale por texto, por JSON, por un error de identidad ni por stderr."""

    def _sin_marcador(self, *procesos):
        for p in procesos:
            self.assertNotIn(MARCADOR, p.stdout, "fuga por stdout")
            self.assertNotIn(MARCADOR, p.stderr, "fuga por stderr")

    def test_27_secreto_del_manifiesto_no_sale_por_ninguna_salida(self):
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "s"\n'
                        f'remote = "https://usuario:{MARCADOR}@ej.invalid/org/r.git"\n'
                        'path = "s"\n')
        for orden in (["check"], ["status"], ["init"]):
            with self.subTest(orden=orden[0]):
                self._sin_marcador(workspace(orden, self.ads),
                                   workspace(orden + ["--json"], self.ads))

    def test_28_secreto_en_el_origen_de_disco_no_sale_por_el_error_de_identidad(self):
        """El manifiesto puede estar limpio y el repositorio de disco no estarlo.

        Es el caso peor: el error de identidad imprime AMBOS remotos, y el de disco no ha
        pasado por ninguna validación.
        """
        bueno = crear_remoto_bare(self.tmp, "bueno")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "s"\nremote = "{bueno}"\npath = "s"\n')
        destino = os.path.join(self.ws, "s")
        git(["clone", "-q", bueno, destino], self.ws)
        git(["remote", "set-url", "origin",
             f"https://usuario:{MARCADOR}@ej.invalid/org/otro.git"], destino)
        p = workspace(["check"], self.ads)
        self.assertEqual(p.returncode, 1)
        self.assertIn("identidad remota distinta", p.stdout + p.stderr)
        self._sin_marcador(p, workspace(["check", "--json"], self.ads),
                           workspace(["status"], self.ads),
                           workspace(["status", "--json"], self.ads),
                           workspace(["init"], self.ads))

    def test_29_el_error_de_clone_nunca_reproduce_una_credencial(self):
        """`git clone` cita la URL en su stderr, y esa URL puede llevar el secreto.

        Aquí se comprueban las dos mitades de la defensa:

          1. con credenciales en el manifiesto NO SE LLEGA a clonar. Es un error estático y
             `init` es todo o nada: el camino que filtraba ni siquiera se recorre;
          2. y si aun así se recorriera —un remoto de disco, otra orden futura—, el stderr
             de Git pasa por `redactar` antes de salir.
        """
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "f"\n'
                        f'remote = "https://usuario:{MARCADOR}@ej.invalid/no/existe.git"\n'
                        'path = "f"\n')
        p = workspace(["init"], self.ads)
        self.assertEqual(p.returncode, 1)
        self.assertIn("NO ha ejecutado ninguna acción", p.stdout + p.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.ws, "f")),
                         "no se intentó ningún clone, luego no se creó nada")
        self._sin_marcador(p, workspace(["init", "--json"], self.ads))

        sys.path.insert(0, os.path.join(RAIZ, "tooling"))
        from workspace import redactar  # noqa: E402
        stderr_de_git = (f"fatal: unable to access "
                         f"'https://usuario:{MARCADOR}@ej.invalid/no/existe.git/': "
                         f"Could not resolve host: ej.invalid")
        self.assertNotIn(MARCADOR, redactar(stderr_de_git))
        self.assertIn("usuario:***@", redactar(stderr_de_git))

    def test_30_redactar_no_toca_un_usuario_ssh_normal(self):
        """Redactar de más haría el mensaje inútil: `git@` no es un secreto."""
        sys.path.insert(0, os.path.join(RAIZ, "tooling"))
        from workspace import redactar  # noqa: E402
        self.assertEqual(redactar("ssh://git@github.com/org/repo.git"),
                         "ssh://git@github.com/org/repo.git")
        self.assertEqual(redactar("git@github.com:org/repo.git"), "git@github.com:org/repo.git")
        self.assertEqual(redactar("https://usuario:tok@h/r.git"), "https://usuario:***@h/r.git")
        self.assertEqual(redactar("https://tok@h/r.git"), "https://***@h/r.git")
        self.assertEqual(redactar("ssh://git:tok@h/r.git"), "ssh://git:***@h/r.git")


class TestSSHFrenteACredenciales(Base):
    def test_31_ssh_explicita_es_una_url_valida(self):
        """§39 la admite. Confundirla con un token rompe la forma canónica de SSH."""
        for url in ("ssh://git@github.com/org/repo.git",
                    "ssh://git@gitlab.ej:2222/org/repo.git",
                    "git@github.com:org/repo.git"):
            with self.subTest(url=url):
                self.manifiesto(self.base_valida() +
                                f'\n[[sources]]\nid = "s"\nremote = "{url}"\npath = "s"\n')
                cod, d = workspace_json(["check"], self.ads)
                self.assertEqual(cod, 0, d)
                self.assertFalse(any("credenciales" in h["mensaje"] for h in d["hallazgos"]), d)

    def test_32_credenciales_http_siguen_siendo_error(self):
        for url in ("https://usuario:tok@github.com/org/r.git",
                    "https://ghp_token@github.com/org/r.git",
                    "http://u:p@ej.invalid/r.git",
                    "ssh://git:tok@github.com/org/r.git"):
            with self.subTest(url=url):
                self.manifiesto(self.base_valida() +
                                f'\n[[sources]]\nid = "s"\nremote = "{url}"\npath = "s"\n')
                cod, d = workspace_json(["check"], self.ads)
                self.assertEqual(cod, 1, d)
                self.assertTrue(any("credenciales" in h["mensaje"] for h in d["hallazgos"]), d)


class TestNormalizacionConservadora(unittest.TestCase):
    """Igualar de menos avisa de más. Igualar de más acepta el repositorio equivocado."""

    def setUp(self):
        sys.path.insert(0, os.path.join(RAIZ, "tooling"))
        from workspace import normalizar_remoto  # noqa: E402
        self.n = normalizar_remoto

    def test_33_equivalencia_documentada_de_github(self):
        """Lo que §39 SÍ declara equivalente tiene que seguir siéndolo."""
        formas = ["https://github.com/org/repo.git",
                  "git@github.com:org/repo.git",
                  "ssh://git@github.com/org/repo.git",
                  "https://github.com/org/repo",
                  "https://GitHub.com/org/repo.git",
                  "https://github.com/org/repo.git/"]
        self.assertEqual(len({self.n(f) for f in formas}), 1,
                         f"deberían ser la misma identidad: {[self.n(f) for f in formas]}")

    def test_34_no_iguala_puertos_distintos(self):
        pares = [("https://h.ej/o/r.git", "https://h.ej:8443/o/r.git"),
                 ("ssh://git@h.ej:22/o/r.git", "ssh://git@h.ej:2222/o/r.git"),
                 ("ssh://git@h.ej/o/r.git", "ssh://git@h.ej:22/o/r.git")]
        for a, b in pares:
            with self.subTest(a=a, b=b):
                self.assertNotEqual(self.n(a), self.n(b), "dos puertos son dos servidores")

    def test_35_no_pliega_la_capitalizacion_de_la_ruta(self):
        self.assertNotEqual(self.n("https://gitlab.ej/Org/Repo.git"),
                            self.n("https://gitlab.ej/org/repo.git"))
        # el HOST sí se pliega: el DNS no distingue mayúsculas
        self.assertEqual(self.n("https://GitLab.EJ/org/repo.git"),
                         self.n("https://gitlab.ej/org/repo.git"))

    def test_36_no_iguala_rutas_locales_distintas(self):
        self.assertNotEqual(self.n("/srv/git/Foo.git"), self.n("/srv/git/foo.git"))
        self.assertNotEqual(self.n("/srv/git/foo.git"), self.n("/srv/git/foo"))
        self.assertEqual(self.n("/srv/git/foo.git"), self.n("/srv/git/./foo.git"))

    def test_37_lo_ambiguo_solo_es_igual_a_si_mismo(self):
        raros = ["esquema-raro://h/o/r.git", "no es una url", "://vacio", "h.ej:", "@"]
        for u in raros:
            with self.subTest(u=u):
                self.assertEqual(self.n(u), self.n(u))
                self.assertNotEqual(self.n(u), self.n(u + "x"))
        self.assertNotEqual(self.n("esquema-raro://github.com/org/repo.git"),
                            self.n("https://github.com/org/repo.git"))

    def test_38_repositorios_distintos_siguen_siendo_distintos(self):
        self.assertNotEqual(self.n("https://github.com/org/repo.git"),
                            self.n("https://github.com/org/otro.git"))
        self.assertNotEqual(self.n("https://github.com/org/repo.git"),
                            self.n("https://gitlab.com/org/repo.git"))


class TestTomlRobusto(Base):
    """Ningún tipo incorrecto produce un traceback, y ninguno pasa por válido."""

    CASOS = {
        "workspace escalar": 'schema = 1\nworkspace = "siblings"\n',
        "workspace lista": 'schema = 1\nworkspace = ["siblings"]\n',
        "sources no es lista": 'schema = 1\nsources = "frontend"\n[workspace]\nlayout = "siblings"\n',
        "sources con entradas escalares": 'schema = 1\nsources = [1, "x"]\n[workspace]\nlayout = "siblings"\n',
        "components no es lista": 'schema = 1\ncomponents = 3\n[workspace]\nlayout = "siblings"\n',
        "components con entradas escalares": 'schema = 1\ncomponents = ["web"]\n[workspace]\nlayout = "siblings"\n',
        "schema booleano": 'schema = true\n[workspace]\nlayout = "siblings"\n',
        "schema texto": 'schema = "1"\n[workspace]\nlayout = "siblings"\n',
        "layout no es texto": 'schema = 1\n[workspace]\nlayout = 3\n',
        "id ausente": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                       '[[sources]]\nremote = "https://e.ej/r.git"\npath = "p"\n'),
        "id vacío": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                     '[[sources]]\nid = "  "\nremote = "https://e.ej/r.git"\npath = "p"\n'),
        "id peligroso": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                         '[[sources]]\nid = "../fuga"\nremote = "https://e.ej/r.git"\npath = "p"\n'),
        "id con salto de línea": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                                  '[[sources]]\nid = "a\\nERROR  falso"\n'
                                  'remote = "https://e.ej/r.git"\npath = "p"\n'),
        "id numérico": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                        '[[sources]]\nid = 7\nremote = "https://e.ej/r.git"\npath = "p"\n'),
        "remote ausente": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                           '[[sources]]\nid = "s"\npath = "p"\n'),
        "remote no es texto": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                               '[[sources]]\nid = "s"\nremote = 5\npath = "p"\n'),
        "path ausente": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                         '[[sources]]\nid = "s"\nremote = "https://e.ej/r.git"\n'),
        "path no es texto": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                             '[[sources]]\nid = "s"\nremote = "https://e.ej/r.git"\npath = 2\n'),
        "component sin source": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                                 '[[components]]\nid = "web"\npath = "."\n'),
        "component con source no textual": ('schema = 1\n[workspace]\nlayout = "siblings"\n'
                                            '[[components]]\nid = "web"\nsource = 3\n'),
        "component con kind no textual": (
            'schema = 1\n[workspace]\nlayout = "siblings"\n'
            '[[sources]]\nid = "s"\nremote = "https://e.ej/r.git"\npath = "p"\n'
            '[[components]]\nid = "web"\nsource = "s"\npath = "."\nkind = 7\n'),
        "TOML sintácticamente inválido": 'schema = = 1\n',
    }

    def test_39_ningun_tipo_incorrecto_pasa_ni_revienta(self):
        for nombre, texto in self.CASOS.items():
            with self.subTest(caso=nombre):
                self.manifiesto(texto)
                for orden in (["check"], ["status"], ["init"]):
                    p = workspace(orden + ["--json"], self.ads)
                    self.assertNotIn("Traceback", p.stderr,
                                     f"[{nombre}] {orden[0]} lanzó una excepción")
                    self.assertEqual(p.returncode, 1,
                                     f"[{nombre}] {orden[0]} no devolvió código 1")
                    d = json.loads(p.stdout)      # la salida sigue siendo JSON válido
                    self.assertFalse(d["ok"], f"[{nombre}] se aceptó como válido")
                    self.assertTrue([h for h in d["hallazgos"] if h["nivel"] == "ERROR"],
                                    f"[{nombre}] falló sin un hallazgo estructurado")

    def test_40_kind_es_opcional_porque_el_modelo_aprobado_lo_declara_descriptivo(self):
        """`plantillas/SOURCES.toml` dice: «`kind` es descriptivo y abierto».

        No se inventa una obligación que el modelo aprobado no impone. Lo que sí se
        rechaza es declararlo mal, y eso lo cubre el caso «component con kind no textual».
        """
        bare = crear_remoto_bare(self.tmp, "app")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "app"\nremote = "{bare}"\npath = "app"\n'
                        '\n[[components]]\nid = "web"\nsource = "app"\npath = "."\n')
        cod, d = workspace_json(["check"], self.ads)
        self.assertEqual(cod, 0, d)
        self.assertIsNone(d["components"][0]["kind"])

    def test_41_ids_validos_siguen_siendo_validos(self):
        """La regla de ids no puede rechazar lo que el corpus usa de verdad."""
        bare = crear_remoto_bare(self.tmp, "app")
        for sid in ("frontend", "api-v2", "app_movil", "web.2", "a", "X9"):
            with self.subTest(id=sid):
                self.manifiesto(self.base_valida() +
                                f'\n[[sources]]\nid = "{sid}"\nremote = "{bare}"\npath = "p"\n')
                cod, d = workspace_json(["check"], self.ads)
                self.assertEqual(cod, 0, d)


class TestSinRed(Base):
    """CA-16 · «sin red» es una condición comprobada, no una intención del comentario."""

    def test_44_git_no_puede_salir_de_la_maquina_en_estas_pruebas(self):
        destino = os.path.join(self.tmp, "no-deberia-existir")
        for url in ("https://github.com/git/git.git",
                    "ssh://git@github.com/git/git.git",
                    "git://github.com/git/git.git"):
            with self.subTest(url=url):
                p = git(["clone", "-q", url, destino], self.tmp)
                self.assertNotEqual(p.returncode, 0)
                self.assertIn("not allowed", p.stderr,
                              f"el transporte de '{url}' no está bloqueado: estas pruebas "
                              f"PODRÍAN salir a la red")
                self.assertFalse(os.path.exists(destino))

    def test_45_y_aun_asi_un_remoto_local_se_clona(self):
        """La contraparte: si el bloqueo dejara fuera también al transporte local, las
        pruebas pasarían sin ejercitar nada."""
        bare = crear_remoto_bare(self.tmp, "local")
        self.manifiesto(self.base_valida() +
                        f'\n[[sources]]\nid = "local"\nremote = "{bare}"\npath = "local"\n')
        cod, d = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 0, d)
        self.assertEqual(d["sources"][0]["accion"], "clonada")


class TestReconstruccion(Base):
    """CA-3 · el caso que el checkpoint afirmaba como «test mental», ejecutado de verdad.

    Cuatro repositorios Git locales, sin red. Se materializan, se BORRAN los cuatro, y el
    workspace se reconstruye desde el repositorio ADS de control y su manifiesto.
    """

    FUENTES = ("frontend", "backend", "movil", "infra")

    def test_42_producto_de_cuatro_fuentes_se_reconstruye_tras_borrarlas(self):
        bares = {n: crear_remoto_bare(self.tmp, n, fichero=f"{n}.md") for n in self.FUENTES}
        texto = self.base_valida()
        for n, bare in bares.items():
            texto += f'\n[[sources]]\nid = "{n}"\nremote = "{bare}"\npath = "{n}"\n'
        texto += ('\n[[components]]\nid = "web"\nsource = "frontend"\npath = "."\nkind = "frontend"\n'
                  '\n[[components]]\nid = "api"\nsource = "backend"\npath = "."\nkind = "backend"\n'
                  '\n[[components]]\nid = "app"\nsource = "movil"\npath = "."\nkind = "mobile"\n'
                  '\n[[components]]\nid = "despliegue"\nsource = "infra"\npath = "deploy"\n')
        self.manifiesto(texto)

        cod, d = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 0, d)
        self.assertEqual({s["accion"] for s in d["sources"]}, {"clonada"})

        cod, d = workspace_json(["status"], self.ads)
        self.assertEqual(cod, 0, d)
        antes = {s["id"]: s["head"] for s in d["sources"]}
        self.assertEqual(set(antes), set(self.FUENTES))
        self.assertTrue(all(antes.values()), antes)

        # se pierde el workspace entero salvo el repositorio de control
        for n in self.FUENTES:
            shutil.rmtree(os.path.join(self.ws, n))
        self.assertEqual(sorted(os.listdir(self.ws)), ["ads"])
        cod, d = workspace_json(["status"], self.ads)
        self.assertEqual(cod, 0, "cuatro fuentes ausentes son INFO, no ERROR")
        self.assertFalse(any(s["present"] for s in d["sources"]))

        # ... y se reconstruye desde el control repo y su manifiesto, sin más entrada
        cod, d = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 0, d)
        self.assertEqual({s["accion"] for s in d["sources"]}, {"clonada"})
        cod, d = workspace_json(["status"], self.ads)
        self.assertEqual(cod, 0, d)
        despues = {s["id"]: s["head"] for s in d["sources"]}
        self.assertEqual(antes, despues, "la reconstrucción no devolvió las mismas revisiones")
        self.assertTrue(all(s["present"] and s["is_git"] and s["remote_ok"]
                            for s in d["sources"]), d)
        for n in self.FUENTES:
            self.assertTrue(os.path.isfile(os.path.join(self.ws, n, f"{n}.md")),
                            f"{n}: el contenido no volvió")
        self.assertEqual(len(d["components"]), 4)

    def test_43_reconstruccion_parcial_solo_toca_lo_que_falta(self):
        """Borrar una de las cuatro no vuelve a clonar las otras tres."""
        bares = {n: crear_remoto_bare(self.tmp, n, fichero=f"{n}.md") for n in self.FUENTES}
        texto = self.base_valida()
        for n, bare in bares.items():
            texto += f'\n[[sources]]\nid = "{n}"\nremote = "{bare}"\npath = "{n}"\n'
        self.manifiesto(texto)
        workspace(["init"], self.ads)
        marcas = {n: os.path.join(self.ws, n, "MARCA-LOCAL.txt") for n in self.FUENTES}
        for m in marcas.values():
            with open(m, "w", encoding="utf-8") as fh:
                fh.write("trabajo local\n")
        shutil.rmtree(os.path.join(self.ws, "movil"))

        cod, d = workspace_json(["init"], self.ads)
        self.assertEqual(cod, 0, d)
        acciones = {s["id"]: s["accion"] for s in d["sources"]}
        self.assertEqual(acciones["movil"], "clonada")
        for n in ("frontend", "backend", "infra"):
            self.assertEqual(acciones[n], "reutilizada")
            self.assertTrue(os.path.exists(marcas[n]), f"{n}: init destruyó trabajo local")


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
