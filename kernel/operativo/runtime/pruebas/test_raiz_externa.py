#!/usr/bin/env python3
"""test_raiz_externa — batería de `V6-16`, la RAÍZ EXTERNA DE CONFIANZA. `T217` a `T220`.

    `T217`  PROCESO e INSTALACIÓN separados, configuración de confianza EXTERNA, y el árbol
            verificado FUERA de la ruta de importación del verificador
    `T218`  FIRMA ASIMÉTRICA real con `ssh-keygen -Y` y Ed25519: firmar · verificar · rotar ·
            solapar · retirar · revocar · rechazar desconocida · rechazar manipulada, con
            FALLO CERRADO sin proveedor y sin clave, y sin un solo secreto en la evidencia
    `T219`  INDEPENDENCIA: la identidad de la raíz externa NO PUEDE ESCRIBIR en el árbol, y
            se demuestra INTENTÁNDOLO —los ocho intentos, con su mensaje real—
    `T220`  `G-A9`: un veredicto falseado DESDE DENTRO del árbol es DESMENTIDO por la
            atestación externa; evidencia FUERA; política no controlable desde el árbol

**LAS CLAVES SON EFÍMERAS, VIVEN FUERA DE TODO REPOSITORIO Y SE DESTRUYEN AL TERMINAR**,
también si la prueba falla: el directorio de claves se retira en un `addClassCleanup`, que
`unittest` ejecuta pase lo que pase. `O25` §5 permite claves efímeras «únicamente en pruebas»
y dice que no constituyen custodia productiva; aquí se dice igual.
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
import stat
import subprocess
import sys
import tempfile
import unittest

RAIZ_RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ_OPERATIVO = os.path.dirname(RAIZ_RUNTIME)
PAQUETE_EXTERNO = os.path.join(RAIZ_OPERATIVO, "raiz-externa")
RAIZ_REPO = os.path.dirname(os.path.dirname(RAIZ_OPERATIVO))

sys.path.insert(0, RAIZ_RUNTIME)
sys.path.insert(0, PAQUETE_EXTERNO)

import admision                                                      # noqa: E402
import aislamiento                                                   # noqa: E402
import atestacion as modulo_de_atestacion                            # noqa: E402
import firma as modulo_de_firma                                      # noqa: E402
import instalar as modulo_de_instalacion                             # noqa: E402
from admision import censo, matriz, perimetro                        # noqa: E402
from errores import (                                                # noqa: E402
    AnclaNoCoincide,
    EmisorNoCoincide,
    EscrituraNoImpedida,
    InstalacionAlterada,
    InstalacionDentroDelArbol,
    ProveedorDeFirmaAusente,
    SecuenciaDeVerificacionIncompleta,
    VinculoDeCommitRoto,
    VinculoDeTreeRoto,
)
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


def escribir_configuracion(ruta, datos):
    """Escribe la configuración externa en el subconjunto de datos que el aparato lee.

    Se escribe a mano y no con una biblioteca de terceros: el kernel es stdlib pura, y el
    lector es `admision/formulas.py`, que declara su propio subconjunto.
    """
    lineas = [
        "version: " + str(datos["version"]),
        "autoridad: " + datos["autoridad"],
        "epoca_vigente: " + str(datos["epoca_vigente"]),
        "orden_de_firma: [" + ", ".join(datos["orden_de_firma"]) + "]",
        "orden_de_verificacion: [" + ", ".join(datos["orden_de_verificacion"]) + "]",
        "identidades:",
    ]
    for entrada in datos["identidades"]:
        lineas.append("  - id: " + entrada["id"])
        lineas.append("    algoritmo: " + entrada["algoritmo"])
        lineas.append("    huella_publica: " + entrada["huella_publica"])
        lineas.append("    estado: " + entrada["estado"])
        lineas.append("    epoca_de_alta: " + str(entrada["epoca_de_alta"]))
        if entrada.get("epoca_de_retirada") is not None:
            lineas.append("    epoca_de_retirada: " + str(entrada["epoca_de_retirada"]))
        if entrada.get("solapamiento") is not None:
            lineas.append("    solapamiento: " + str(entrada["solapamiento"]))
    lineas.append("ancla:")
    lineas.append("  base: " + datos["ancla"]["base"])
    lineas.append("  digest_del_censo: " + datos["ancla"]["digest_del_censo"])
    lineas.append("admitidas: []")
    with open(ruta, "w", encoding="utf-8") as manejador:
        manejador.write("\n".join(lineas) + "\n")
    return ruta


class RaizExternaInstalada(unittest.TestCase):
    """Monta el escenario COMPLETO una vez: árbol, claves efímeras, instalación y config.

    Se hace en `setUpClass` porque instalar copia un árbol de ficheros y generar una clave
    Ed25519 llama a `ssh-keygen`; repetirlo por prueba multiplicaría el coste sin medir nada
    nuevo. Lo que cada prueba comprueba es una propiedad distinta del mismo escenario.
    """

    @classmethod
    def setUpClass(cls):
        cls.taller = tempfile.mkdtemp(prefix="ads-raiz-")
        cls.addClassCleanup(cls._retirar_todo)

        cls.repo = os.path.join(cls.taller, "control")
        os.makedirs(cls.repo)
        cls.canal = CanalGit(cls.repo)
        cls.base = matriz.fundar(cls.repo, cls.canal)
        # La política del gobierno, DENTRO del árbol verificado: es uno de los ocho
        # objetivos de escritura de `T219` y tiene que existir para que el intento mida
        # un permiso y no una ausencia.
        cls._sembrar_politica()

        cls.externo = os.path.join(cls.taller, "externo")
        os.makedirs(cls.externo)
        # LAS CLAVES, FUERA DE TODO REPOSITORIO. `0700` en el directorio y `0600` en la
        # clave, y el directorio entero se destruye en el `addClassCleanup`.
        cls.claves = os.path.join(cls.taller, "claves")
        os.makedirs(cls.claves, mode=0o700)

        cls.privada, cls.publica = modulo_de_firma.generar_par_efimero(
            cls.claves, "raiz-externa-1")
        cls.privada_2, cls.publica_2 = modulo_de_firma.generar_par_efimero(
            cls.claves, "raiz-externa-2")
        cls.privada_ajena, cls.publica_ajena = modulo_de_firma.generar_par_efimero(
            cls.claves, "identidad-desconocida")
        cls.firmantes = modulo_de_firma.escribir_firmantes(
            os.path.join(cls.externo, "allowed_signers"),
            [("raiz-externa-1", cls.publica), ("raiz-externa-2", cls.publica_2)])

        cls.instalacion = modulo_de_instalacion.instalar(
            os.path.join(cls.taller, "instalacion"),
            arbol_verificado=cls.repo, runtime=RAIZ_RUNTIME)
        cls.verificador = cls.instalacion["verificador"]
        cls.firmante = os.path.join(cls.instalacion["destino"], "raiz-externa",
                                    "anfitrion_firmante.py")
        cls.verificante = os.path.join(cls.instalacion["destino"], "raiz-externa",
                                       "anfitrion_verificador.py")

        cls.digest_del_censo = perimetro.digest_del_censo(censo.cargar_zonas(cls.repo))
        cls.configuracion = escribir_configuracion(
            os.path.join(cls.externo, "confianza.yml"), cls._datos_de_configuracion())
        cls.evidencia = os.path.join(cls.externo, "atestacion.json")

        # El cuerpo de la clave privada, para poder BARRER las salidas buscándolo.
        with open(cls.privada, encoding="ascii") as manejador:
            cuerpo = [linea.strip() for linea in manejador.read().splitlines()
                      if linea.strip() and not linea.startswith("-----")]
        cls.marcador_de_clave = max(cuerpo, key=len)

    @classmethod
    def _sembrar_politica(cls):
        origen = os.path.join(RAIZ_RUNTIME, "gobierno", "POLITICA-CONTROL-REPO.yml")
        destino = os.path.join(cls.repo, "kernel", "operativo", "runtime", "gobierno",
                               "POLITICA-CONTROL-REPO.yml")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        shutil.copyfile(origen, destino)
        cls.canal.ejecutar("add", "-A")
        cls.canal.ejecutar("commit", "--quiet", "-m", "politica del gobierno")
        cls.base = cls.canal.resolver("HEAD")

    @classmethod
    def _datos_de_configuracion(cls, identidades=None, epoca=1):
        return {
            "version": 1,
            "autoridad": "raiz-externa-de-la-bateria",
            "epoca_vigente": epoca,
            "orden_de_firma": [cls.firmante],
            "orden_de_verificacion": [cls.verificante, "--firmantes", cls.firmantes],
            "identidades": identidades or [{
                "id": "raiz-externa-1",
                "algoritmo": modulo_de_firma.ALGORITMO,
                "huella_publica": modulo_de_firma.huella_publica(cls.publica),
                "estado": "activa",
                "epoca_de_alta": 1,
            }],
            "ancla": {"base": cls.base, "digest_del_censo": cls.digest_del_censo},
        }

    @classmethod
    def _retirar_todo(cls):
        """Destruye el taller ENTERO, claves incluidas. Se ejecuta pase lo que pase."""
        shutil.rmtree(cls.taller, ignore_errors=True)

    # -- utilidades ---------------------------------------------------------
    def entorno(self, *, con_clave=True, extra=None):
        """Entorno CONSTRUIDO desde cero. La clave se pasa por la variable de `O25` §2."""
        entorno = {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "LC_ALL": "C.UTF-8",
            "LANG": "C.UTF-8",
            "HOME": self.taller,
        }
        if con_clave:
            entorno["ADS_ANFITRION_ALMACEN"] = self.privada
        if extra:
            entorno.update(extra)
        return entorno

    def correr(self, argumentos, *, con_clave=True, extra=None, cwd=None):
        return subprocess.run(
            [sys.executable, self.verificador] + list(argumentos),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.entorno(con_clave=con_clave, extra=extra),
            cwd=cwd or self.taller, check=False,
        )

    def emitir(self, *, evidencia=None, configuracion=None, con_clave=True):
        destino = evidencia or self.evidencia
        return self.correr([
            "verificar", "--repo", self.repo, "--base", self.base,
            "--configuracion", configuracion or self.configuracion,
            "--evidencia", destino,
        ], con_clave=con_clave), destino

    def leer_sobre(self, ruta=None):
        with open(ruta or self.evidencia, encoding="utf-8") as manejador:
            return json.load(manejador)


# ===========================================================================
#  T217 · proceso, paquete e instalación SEPARADOS
# ===========================================================================
class SeparacionDelEjecutor(RaizExternaInstalada):

    def test_el_paquete_vive_fuera_de_runtime(self):
        """T217 · Defecto que previene: un «verificador externo» que es un módulo más del runtime."""
        self.assertTrue(os.path.isdir(PAQUETE_EXTERNO))
        self.assertNotEqual(os.path.dirname(PAQUETE_EXTERNO), RAIZ_RUNTIME)
        self.assertFalse(PAQUETE_EXTERNO.startswith(RAIZ_RUNTIME + os.sep))

    def test_el_verificador_se_ejecuta_como_PROCESO_aparte(self):
        """T217 · Defecto que previene: llamar «externo» a una función del mismo intérprete."""
        resultado = self.correr(["capacidades"])
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        informe = json.loads(resultado.stdout.decode("utf-8"))
        self.assertTrue(informe["disponible"])
        self.assertFalse(informe["simetrica"])
        self.assertTrue(informe["version_de_openssh"].startswith("OpenSSH_"))
        self.assertEqual(informe["algoritmo"], modulo_de_firma.ALGORITMO)

    def test_la_instalacion_esta_fuera_del_arbol_verificado(self):
        """T217 · Defecto que previene: un verificador que vive donde vive lo verificado."""
        destino = os.path.realpath(self.instalacion["destino"])
        arbol = os.path.realpath(self.repo)
        self.assertFalse(destino == arbol or destino.startswith(arbol + os.sep))
        self.assertTrue(os.path.isfile(self.verificador))

    def test_instalar_dentro_del_arbol_falla_cerrado(self):
        """T217 · Defecto que previene: instalar la raíz externa dentro de lo que verifica."""
        with self.assertRaises(InstalacionDentroDelArbol):
            modulo_de_instalacion.instalar(
                os.path.join(self.repo, "raiz-externa"),
                arbol_verificado=self.repo, runtime=RAIZ_RUNTIME)

    def test_el_arbol_verificado_NO_contiene_la_raiz_externa(self):
        """T217 · Defecto que previene: que el árbol pueda editar a quien lo verifica."""
        dentro = []
        for carpeta, subcarpetas, ficheros in os.walk(self.repo):
            if ".git" in subcarpetas:
                subcarpetas.remove(".git")
            for nombre in ficheros:
                if nombre in ("verificador.py", "anfitrion_firmante.py",
                              "anfitrion_verificador.py"):
                    dentro.append(os.path.join(carpeta, nombre))
        self.assertEqual(dentro, [])

    def test_el_manifiesto_de_la_instalacion_se_recalcula_y_casa(self):
        """T217 · Defecto que previene: §11.8, huellas leídas del árbol en vez de recalculadas."""
        informe = modulo_de_instalacion.verificar_instalacion(
            self.instalacion["destino"])
        self.assertTrue(informe["ok"], informe)
        resultado = self.correr(["instalacion", "--instalacion",
                                 self.instalacion["destino"]])
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())

    def test_una_instalacion_alterada_falla_cerrado(self):
        """T217 · Defecto que previene: emitir veredicto desde un verificador manipulado."""
        copia = os.path.join(self.taller, "instalacion-alterada")
        shutil.copytree(self.instalacion["destino"], copia)
        self.addCleanup(shutil.rmtree, copia, ignore_errors=True)
        objetivo = os.path.join(copia, "runtime", "admision", "perimetro.py")
        with open(objetivo, "a", encoding="utf-8") as manejador:
            manejador.write("\n# alteracion del instrumento\n")
        with self.assertRaises(InstalacionAlterada):
            modulo_de_instalacion.exigir_instalacion_intacta(copia)

    def test_el_verificador_NO_importa_el_runtime_del_arbol_verificado(self):
        """T217 · Defecto que previene: que el árbol decida cómo se le verifica."""
        guion = (
            "import json, os, sys\n"
            "sys.argv = ['verificador.py', 'capacidades']\n"
            "ruta = " + repr(self.verificador) + "\n"
            "carpeta = os.path.dirname(ruta)\n"
            "sys.path.insert(0, carpeta)\n"
            "import runpy\n"
            "try:\n"
            "    runpy.run_path(ruta, run_name='no-main')\n"
            "except SystemExit:\n"
            "    pass\n"
            "import admision\n"
            "print(os.path.dirname(os.path.dirname(admision.__file__)))\n"
        )
        resultado = subprocess.run(
            [sys.executable, "-c", guion], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, env=self.entorno(), cwd=self.taller, check=False)
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        procedencia = resultado.stdout.decode("utf-8").strip().splitlines()[-1]
        self.assertTrue(procedencia.startswith(self.instalacion["destino"]),
                        "el verificador importó `admision` desde " + procedencia)
        self.assertFalse(procedencia.startswith(os.path.realpath(self.repo)))

    def test_la_configuracion_de_confianza_vive_fuera_del_arbol(self):
        """T217 · Defecto que previene: `O25` §3, que el árbol decida qué identidad se acepta."""
        import identidad
        configuracion = identidad.cargar(self.configuracion, arbol_verificado=self.repo)
        self.assertEqual(configuracion.autoridad(), "raiz-externa-de-la-bateria")
        dentro = os.path.join(self.repo, "confianza.yml")
        shutil.copyfile(self.configuracion, dentro)
        self.addCleanup(os.remove, dentro)
        with self.assertRaises(identidad.ConfiguracionDentroDelArbol):
            identidad.cargar(dentro, arbol_verificado=self.repo)


# ===========================================================================
#  T218 · la FIRMA ASIMÉTRICA
# ===========================================================================
class FirmaAsimetrica(RaizExternaInstalada):

    def test_la_dependencia_queda_fijada_en_la_evidencia(self):
        """T218 · Defecto que previene: una dependencia externa sin versión registrada."""
        resultado, _ = self.emitir()
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        sobre = self.leer_sobre()
        proveedor = sobre["atestacion"]["proveedor"]
        self.assertEqual(proveedor["herramienta"], "ssh-keygen")
        self.assertTrue(proveedor["version_de_openssh"].startswith("OpenSSH_"))
        self.assertEqual(proveedor["algoritmo"], "ssh-ed25519")
        self.assertFalse(proveedor["simetrica"])

    def test_la_clave_privada_tiene_permisos_0600_y_esta_fuera_de_todo_repositorio(self):
        """T218 · Defecto que previene: `O25` §2, una clave versionada o legible por todos."""
        modo = stat.S_IMODE(os.stat(self.privada).st_mode)
        self.assertEqual(modo, 0o600)
        self.assertFalse(os.path.realpath(self.privada).startswith(
            os.path.realpath(self.repo) + os.sep))
        self.assertFalse(os.path.realpath(self.privada).startswith(
            os.path.realpath(RAIZ_REPO) + os.sep))

    def test_quien_verifica_NO_puede_firmar(self):
        """T218 · Defecto que previene: un HMAC, donde verificar y firmar son el mismo poder."""
        proceso = subprocess.run(
            [sys.executable, self.verificante, "--firmantes", self.firmantes,
             "firmar", "raiz-externa-1"],
            input=b"mensaje", stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.entorno(), check=False)
        self.assertNotEqual(proceso.returncode, 0)
        with open(self.firmantes, encoding="ascii") as manejador:
            firmantes = manejador.read()
        self.assertNotIn("PRIVATE KEY", firmantes)
        self.assertIn("ssh-ed25519", firmantes)

    def test_el_firmante_se_niega_a_verificar(self):
        """T218 · Defecto que previene: juntar los dos poderes en un único programa."""
        proceso = subprocess.run(
            [sys.executable, self.firmante, "verificar", "raiz-externa-1", "00"],
            input=b"mensaje", stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=self.entorno(), check=False)
        self.assertEqual(proceso.returncode, 4)
        self.assertIn(b"SOLO firma", proceso.stderr)

    def test_sin_clave_el_veredicto_favorable_NO_se_emite(self):
        """T218 · Defecto que previene: `O25` §2, seguir adelante sin proveedor válido."""
        destino = os.path.join(self.externo, "sin-clave.json")
        resultado, _ = self.emitir(evidencia=destino, con_clave=False)
        self.assertNotEqual(resultado.returncode, 0)
        self.assertFalse(os.path.exists(destino))

    def test_una_atestacion_manipulada_no_verifica(self):
        """T218 · Defecto que previene: reescribir el veredicto después de firmarlo."""
        resultado, _ = self.emitir()
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        manipulada = os.path.join(self.externo, "manipulada.json")
        sobre = self.leer_sobre()
        sobre["atestacion"]["veredicto"]["color"] = "VERDE"
        sobre["atestacion"]["autoridad"] = "otra-autoridad"
        sobre["firma"]["digest_de_lo_firmado"] = modulo_de_atestacion.digest(
            sobre["atestacion"])
        with open(manipulada, "w", encoding="utf-8") as manejador:
            manejador.write(json.dumps(sobre, sort_keys=True, ensure_ascii=False,
                                       indent=2) + "\n")
        comprobacion = self.correr([
            "comprobar", "--repo", self.repo, "--configuracion", self.configuracion,
            "--evidencia", manipulada])
        self.assertNotEqual(comprobacion.returncode, 0)
        self.assertIn(b"FIRMA_NO_VERIFICADA", comprobacion.stderr)

    def test_cambiar_UN_BYTE_de_la_atestacion_la_invalida(self):
        """T218 · Defecto que previene: una firma que no cubre todo lo que dice cubrir."""
        cuerpo = modulo_de_atestacion.construir(
            autoridad="a", identidad="raiz-externa-1", huella_publica="SHA256:x",
            epoca=1, commit="a" * 40, tree="b" * 40,
            veredicto={"color": "ROJO"}, proveedor={"herramienta": "ssh-keygen"})
        mensaje = modulo_de_atestacion.canonizar(cuerpo)
        blindada = modulo_de_firma.firmar(mensaje, clave_privada=self.privada)
        valida, _ = modulo_de_firma.verificar(
            mensaje, blindada, firmantes=self.firmantes, principal="raiz-externa-1")
        self.assertTrue(valida)
        alterado = bytearray(mensaje)
        alterado[-8] = alterado[-8] ^ 0x01
        invalida, diagnostico = modulo_de_firma.verificar(
            bytes(alterado), blindada, firmantes=self.firmantes,
            principal="raiz-externa-1")
        self.assertFalse(invalida)
        self.assertTrue(diagnostico)

    def test_una_clave_desconocida_se_rechaza(self):
        """T218 · Defecto que previene: aceptar una firma de quien la configuración no acepta."""
        cuerpo = modulo_de_atestacion.construir(
            autoridad="a", identidad="identidad-desconocida", huella_publica="SHA256:x",
            epoca=1, commit="a" * 40, tree="b" * 40,
            veredicto={"color": "VERDE"}, proveedor={"herramienta": "ssh-keygen"})
        mensaje = modulo_de_atestacion.canonizar(cuerpo)
        blindada = modulo_de_firma.firmar(mensaje, clave_privada=self.privada_ajena)
        valida, _ = modulo_de_firma.verificar(
            mensaje, blindada, firmantes=self.firmantes,
            principal="identidad-desconocida")
        self.assertFalse(valida)

    def test_el_punto_ejecutable_VERIFICA_lo_que_acaba_de_firmar(self):
        """T218 · Defecto que previene: publicar una atribución FALSA en un artefacto firmado.

        DEFECTO QUE CIERRA, encontrado por la auditoría independiente y clasificado como
        BLOQUEANTE. `verificar` firmaba delegando en el anfitrión y escribía la evidencia SIN
        comprobar la firma resultante: si el anfitrión tenía a mano una clave que el anillo
        NO acepta —otra ruta, otro almacén, una variable apuntando a otro sitio—, la firma
        salía igual, la atestación se escribía estampando la identidad y la huella de la
        clave LEGÍTIMA, y el punto ejecutable terminaba con CÓDIGO 0. Un `verificar &&
        desplegar` seguía adelante sobre una atestación forjada.

        `comprobar` sí lo detectaba, pero detectarlo después no es fallar cerrado: `O25` §2
        exige que sin proveedor VÁLIDO no se firme, y un proveedor que firma con una clave
        que el anillo no acepta no es un proveedor válido.
        """
        destino = os.path.join(self.taller, "atestacion-forjada.json")
        if os.path.exists(destino):
            os.remove(destino)
        # El anfitrión firma con una clave que NO está en `allowed_signers` ni en el anillo.
        forjado = self.correr([
            "verificar", "--repo", self.repo, "--base", self.base,
            "--configuracion", self.configuracion, "--evidencia", destino,
        ], extra={"ADS_ANFITRION_ALMACEN": self.privada_ajena})
        self.assertNotEqual(forjado.returncode, 0,
                            "una firma de una clave NO aceptada terminó con éxito")
        self.assertIn("FIRMA_NO_VERIFICADA", forjado.stderr.decode("utf-8", "replace"))
        self.assertFalse(os.path.exists(destino),
                         "se escribió evidencia de una atestación que no verifica")
        # CONTROL DEL CONTROL: con la clave LEGÍTIMA, el mismo camino sí emite. Sin él,
        # «no se escribió nada» se explicaría por un verificador que no arranca.
        legitimo, ruta = self.emitir(evidencia=destino)
        self.assertEqual(legitimo.returncode, 0,
                         legitimo.stderr.decode("utf-8", "replace")[:300])
        self.assertTrue(os.path.exists(ruta))
        with open(ruta, encoding="utf-8") as manejador:
            sobre = json.load(manejador)
        self.assertEqual(sobre["atestacion"]["huella_publica"],
                         modulo_de_firma.huella_publica(self.publica))

    def test_rotacion_solapamiento_retirada_y_revocacion(self):
        """T218 · Defecto que previene: `O25` §5, un contrato de identidad sin ciclo de vida."""
        import identidad
        configuracion = identidad.cargar(self.configuracion, arbol_verificado=self.repo)
        anillo = configuracion.anillo()
        entrante = identidad.Identidad(
            identificador="raiz-externa-2", algoritmo=modulo_de_firma.ALGORITMO,
            huella_publica=modulo_de_firma.huella_publica(self.publica_2),
            estado="activa", epoca_de_alta=1)
        acta = anillo.rotar(nueva=entrante, motivo="rotacion programada",
                            solapamiento=2)
        self.assertEqual(acta["saliente"]["estado"], "retirada")
        self.assertEqual(acta["entrante"]["estado"], "activa")
        # SOLAPAMIENTO: la retirada sigue verificando dentro de su ventana...
        self.assertTrue(anillo.exigir_valida("raiz-externa-1", acta["epoca"]))
        # ...y deja de hacerlo fuera de ella.
        with self.assertRaises(identidad.IdentidadFueraDeSolapamiento):
            anillo.exigir_valida("raiz-externa-1",
                                 acta["epoca"] + acta["solapamiento"] + 1)
        # REVOCACIÓN: no verifica NUNCA, ni dentro del solapamiento.
        anillo.revocar("raiz-externa-1", motivo="clave comprometida")
        with self.assertRaises(identidad.IdentidadRevocada):
            anillo.exigir_valida("raiz-externa-1", acta["epoca"])
        # DESCONOCIDA: la configuración externa no la acepta y el árbol no puede añadirla.
        with self.assertRaises(identidad.IdentidadDesconocida):
            anillo.exigir_valida("identidad-desconocida", acta["epoca"])
        # TRAZABILIDAD sin revelación: la traza lleva la huella PÚBLICA y nada más.
        traza = json.dumps(anillo.traza(), sort_keys=True, ensure_ascii=False)
        self.assertIn("rotacion", traza)
        self.assertIn("revocacion", traza)
        self.assertNotIn(self.marcador_de_clave, traza)

    def test_la_identidad_rotada_firma_y_verifica_de_verdad(self):
        """T218 · Defecto que previene: una rotación que sólo cambia un campo de un fichero."""
        configuracion = escribir_configuracion(
            os.path.join(self.externo, "confianza-rotada.yml"),
            self._datos_de_configuracion(identidades=[
                {"id": "raiz-externa-1", "algoritmo": modulo_de_firma.ALGORITMO,
                 "huella_publica": modulo_de_firma.huella_publica(self.publica),
                 "estado": "retirada", "epoca_de_alta": 1, "epoca_de_retirada": 2,
                 "solapamiento": 2},
                {"id": "raiz-externa-2", "algoritmo": modulo_de_firma.ALGORITMO,
                 "huella_publica": modulo_de_firma.huella_publica(self.publica_2),
                 "estado": "activa", "epoca_de_alta": 2},
            ], epoca=2))
        destino = os.path.join(self.externo, "atestacion-rotada.json")
        resultado = self.correr([
            "verificar", "--repo", self.repo, "--base", self.base,
            "--configuracion", configuracion, "--evidencia", destino],
            extra={"ADS_ANFITRION_ALMACEN": self.privada_2})
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        sobre = self.leer_sobre(destino)
        self.assertEqual(sobre["atestacion"]["identidad"], "raiz-externa-2")
        comprobacion = self.correr([
            "comprobar", "--repo", self.repo, "--configuracion", configuracion,
            "--evidencia", destino])
        self.assertEqual(comprobacion.returncode, 0, comprobacion.stderr.decode())

    def test_ninguna_salida_lleva_material_de_clave_privada(self):
        """T218 · Defecto que previene: `O25` §2, un secreto en la evidencia, el log o el error."""
        salidas = []
        resultado, _ = self.emitir()
        salidas.append(resultado.stdout.decode("utf-8", "replace"))
        salidas.append(resultado.stderr.decode("utf-8", "replace"))
        sin_clave, _ = self.emitir(evidencia=os.path.join(self.externo, "x.json"),
                                   con_clave=False)
        salidas.append(sin_clave.stdout.decode("utf-8", "replace"))
        salidas.append(sin_clave.stderr.decode("utf-8", "replace"))
        comprobacion = self.correr([
            "comprobar", "--repo", self.repo, "--configuracion", self.configuracion,
            "--evidencia", self.evidencia])
        salidas.append(comprobacion.stdout.decode("utf-8", "replace"))
        salidas.append(comprobacion.stderr.decode("utf-8", "replace"))
        with open(self.evidencia, encoding="utf-8") as manejador:
            salidas.append(manejador.read())
        import identidad
        configuracion = identidad.cargar(self.configuracion, arbol_verificado=self.repo)
        salidas.append(json.dumps(configuracion.exportar(), sort_keys=True,
                                  ensure_ascii=False))
        for indice, texto in enumerate(salidas):
            with self.subTest(salida=indice):
                self.assertNotIn(self.marcador_de_clave, texto)
        # Y el ÁRBOL VERIFICADO entero: ni un byte de clave dentro del repositorio.
        for carpeta, _, ficheros in os.walk(self.repo):
            for nombre in ficheros:
                with open(os.path.join(carpeta, nombre), "rb") as manejador:
                    self.assertNotIn(self.marcador_de_clave.encode("ascii"),
                                     manejador.read())

    def test_el_marcador_si_esta_en_la_clave_privada(self):
        """T218 · Control del CONTROL: si el marcador no estuviera, el barrido no probaría nada."""
        with open(self.privada, encoding="ascii") as manejador:
            self.assertIn(self.marcador_de_clave, manejador.read())

    def test_sin_ssh_keygen_el_proveedor_falla_cerrado(self):
        """T218 · Defecto que previene: emitir veredicto favorable sin herramienta de firma."""
        vacio = tempfile.mkdtemp(prefix="ads-sin-ssh-")
        self.addCleanup(shutil.rmtree, vacio, ignore_errors=True)
        guion = (
            "import os, sys\n"
            "os.environ['PATH'] = " + repr(vacio) + "\n"
            "sys.path.insert(0, " + repr(PAQUETE_EXTERNO) + ")\n"
            "import firma\n"
            "from errores import ProveedorDeFirmaAusente\n"
            "try:\n"
            "    firma.exigir_proveedor()\n"
            "except ProveedorDeFirmaAusente as error:\n"
            "    print(error.codigo)\n"
            "    raise SystemExit(0)\n"
            "raise SystemExit(9)\n"
        )
        resultado = subprocess.run(
            [sys.executable, "-c", guion], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, env={"PATH": vacio, "LC_ALL": "C", "HOME": vacio},
            check=False)
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        self.assertIn(b"PROVEEDOR_DE_FIRMA_AUSENTE", resultado.stdout)


# ===========================================================================
#  T219 · INDEPENDENCIA: la identidad NO puede escribir en el árbol
# ===========================================================================
class IndependenciaDeLaIdentidad(RaizExternaInstalada):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        resultado = subprocess.run(
            [sys.executable, cls.verificador, "verificar", "--repo", cls.repo,
             "--base", cls.base, "--configuracion", cls.configuracion,
             "--evidencia", cls.evidencia],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LC_ALL": "C.UTF-8",
                 "LANG": "C.UTF-8", "HOME": cls.taller,
                 "ADS_ANFITRION_ALMACEN": cls.privada},
            cwd=cls.taller, check=False)
        cls.emision = resultado
        cls.capacidades_de_aislamiento = aislamiento.capacidades()

    def test_el_usuario_del_sistema_distinto_NO_es_posible_aqui_y_se_registra(self):
        """T219 · Defecto que previene: declarar imposible lo que no se ha comprobado."""
        fila = [f for f in self.capacidades_de_aislamiento["mecanismos"]
                if f["mecanismo"] == "usuario-del-sistema"][0]
        self.assertFalse(fila["disponible"])
        self.assertTrue(fila["motivo"])

    def test_hay_al_menos_un_aislamiento_real_disponible(self):
        """T219 · Defecto que previene: dar por buena la independencia sin poder ejercerla."""
        if self.capacidades_de_aislamiento["elegido"] is None:
            self.skipTest(
                "este anfitrión no ofrece aislamiento: `V6-16` NO se declara completo y el "
                "requisito de infraestructura queda en el informe")
        self.assertIn(self.capacidades_de_aislamiento["elegido"],
                      ("contenedor", "espacio-de-nombres"))

    def test_los_ocho_intentos_de_escritura_son_impedidos(self):
        """T219 · Defecto que previene: llamar «sin escritura» a lo que nadie intentó escribir."""
        if self.capacidades_de_aislamiento["elegido"] is None:
            self.skipTest("no hay aislamiento disponible en este anfitrión")
        informe = aislamiento.ejecutar(
            self.repo, self.externo,
            informe_de_capacidades=self.capacidades_de_aislamiento)
        self.assertEqual(len(informe["intentos"]), len(aislamiento.INTENTOS))
        for entrada in informe["intentos"]:
            with self.subTest(intento=entrada["intento"]):
                self.assertTrue(entrada["impedido"],
                                entrada["intento"] + " NO fue impedido: "
                                + entrada["mensaje"])
                self.assertTrue(entrada["mensaje"],
                                "un intento impedido sin mensaje del sistema no distingue "
                                "un permiso de un fichero ausente")
        self.assertTrue(aislamiento.exigir_sin_escritura(informe))

    def test_el_control_del_control_del_aislamiento(self):
        """T219 · Defecto que previene: que «todo falló» sea porque el intérprete no arrancó."""
        if self.capacidades_de_aislamiento["elegido"] is None:
            self.skipTest("no hay aislamiento disponible en este anfitrión")
        informe = aislamiento.ejecutar(
            self.repo, self.externo,
            informe_de_capacidades=self.capacidades_de_aislamiento)
        self.assertTrue(informe["control_positivo"]["escribio"])
        self.assertTrue(informe["control_de_lectura"]["leyo"])

    def test_la_identidad_del_verificador_es_DISTINTA_de_la_del_runtime(self):
        """T219 · Defecto que previene: `g.15`, compartir la identidad de escritura del runtime."""
        if "contenedor" not in [f["mecanismo"] for f
                                in self.capacidades_de_aislamiento["mecanismos"]
                                if f["disponible"]]:
            self.skipTest("sin contenedor no se puede ejercer una identidad distinta")
        informe = aislamiento.ejecutar(
            self.repo, self.externo, mecanismo="contenedor",
            informe_de_capacidades=self.capacidades_de_aislamiento)
        self.assertTrue(informe["identidad_distinta"])
        self.assertNotEqual(informe["identidad_del_verificador"]["uid"],
                            informe["identidad_del_runtime"]["uid"])

    def test_un_intento_no_impedido_invalida_la_demostracion(self):
        """T219 · Defecto que previene: publicar una independencia con un agujero dentro."""
        informe = {
            "control_de_lectura": {"codigo": 0},
            "control_positivo": {"codigo": 0},
            "intentos": [{"intento": "crear-un-fichero", "impedido": False,
                          "codigo": 0, "mensaje": ""}],
            "no_ejecutados": [],
        }
        with self.assertRaises(EscrituraNoImpedida):
            aislamiento.exigir_sin_escritura(informe)

    def test_el_espacio_de_nombres_declara_su_limite(self):
        """T219 · Defecto que previene: presentar el respaldo como si diera identidad distinta."""
        fila = [f for f in self.capacidades_de_aislamiento["mecanismos"]
                if f["mecanismo"] == "espacio-de-nombres"][0]
        if not fila["disponible"]:
            self.skipTest("no hay espacios de nombres en este anfitrión")
        self.assertFalse(fila["identidad_distinta"])
        self.assertIn("MISMO usuario", fila["motivo"])


# ===========================================================================
#  T220 · `G-A9` y la evidencia FUERA del árbol
# ===========================================================================
class VeredictoDesmentidoYEvidencia(RaizExternaInstalada):

    def test_la_atestacion_se_vincula_al_commit_y_al_tree(self):
        """T220 · Defecto que previene: §11.8, atestar sobre un nombre de rama."""
        resultado, _ = self.emitir()
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        sobre = self.leer_sobre()
        repositorio = sobre["atestacion"]["repositorio"]
        commit = self.canal.resolver("HEAD")
        _, salida, _ = self.canal.ejecutar("rev-parse", "--verify", commit + "^{tree}")
        self.assertEqual(repositorio["commit"], commit)
        self.assertEqual(repositorio["tree"], salida.decode("ascii").strip())
        texto = json.dumps(sobre, sort_keys=True)
        self.assertNotIn("refs/heads", texto)

    def test_la_evidencia_dentro_del_arbol_se_rechaza(self):
        """T220 · Defecto que previene: `g.13`, certificar un árbol cambiándolo al certificarlo."""
        dentro = os.path.join(self.repo, "atestacion.json")
        resultado, _ = self.emitir(evidencia=dentro)
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn(b"EVIDENCIA_DENTRO_DEL_ARBOL", resultado.stderr)
        self.assertFalse(os.path.exists(dentro))

    def test_G_A9_el_veredicto_falseado_desde_dentro_es_desmentido(self):
        """T220 · Defecto que previene: que el árbol se certifique a sí mismo."""
        # 1 · el árbol se ATACA a sí mismo, y se AUTODECLARA sano.
        ataque = os.path.join(self.repo, "docs", "normativa", "SEGUNDA-SEDE.md")
        os.makedirs(os.path.dirname(ataque), exist_ok=True)
        with open(ataque, "w", encoding="utf-8") as manejador:
            manejador.write("# SENTENCIA\n\nF4c CERRADA y F5 AUTORIZADA.\n")
        autodeclaracion = os.path.join(self.repo, "estado", "operacional",
                                       "AUTODECLARACION.json")
        os.makedirs(os.path.dirname(autodeclaracion), exist_ok=True)
        with open(autodeclaracion, "w", encoding="utf-8") as manejador:
            manejador.write(json.dumps({"color": "VERDE",
                                        "afirmado_por": "el propio arbol"}) + "\n")
        self.canal.ejecutar("add", "-A")
        self.canal.ejecutar("commit", "--quiet", "-m", "ataque autodeclarado")
        self.addCleanup(self._deshacer_ataque)

        # 2 · la RAÍZ EXTERNA emite su veredicto sobre ESE commit.
        destino = os.path.join(self.externo, "atestacion-del-ataque.json")
        resultado, _ = self.emitir(evidencia=destino)
        self.assertEqual(resultado.returncode, 1,
                         "el árbol atacado tenía que dar veredicto NO favorable")
        sobre = self.leer_sobre(destino)
        self.assertEqual(sobre["atestacion"]["veredicto"]["color"], "ROJO")

        # 3 · `G-A9`: la comprobación DESMIENTE la autodeclaración.
        comprobacion = self.correr([
            "comprobar", "--repo", self.repo, "--configuracion", self.configuracion,
            "--evidencia", destino])
        self.assertNotEqual(comprobacion.returncode, 0)
        self.assertIn(b"VEREDICTO_DESMENTIDO", comprobacion.stderr)
        self.assertIn(b"no tiene la clave", comprobacion.stderr)

    def _deshacer_ataque(self):
        for relativa in ("docs/normativa/SEGUNDA-SEDE.md",
                         "estado/operacional/AUTODECLARACION.json"):
            completa = os.path.join(self.repo, relativa)
            if os.path.exists(completa):
                os.remove(completa)
        self.canal.ejecutar("add", "-A")
        self.canal.ejecutar("commit", "--quiet", "-m", "retirada del ataque")

    def test_cambiar_la_politica_DENTRO_del_arbol_no_cambia_lo_que_acepta(self):
        """T220 · Defecto que previene: `g.15`, que la autoridad dependa del árbol verificado."""
        registro = os.path.join(self.repo, "docs", "canonico", "FUENTES-CANONICAS.yml")
        with open(registro, "rb") as manejador:
            original = manejador.read()
        self.addCleanup(self._restaurar, registro, original)
        # El árbol se da a sí mismo una zona que lo declara todo NO APLICABLE, y encima
        # mete una segunda sede normativa. Con la política del árbol mandando, pasaría.
        with open(registro, "wb") as manejador:
            manejador.write(original + (
                "  - patron: '^docs/normativa/'\n"
                "    clase: NO_APLICABLE_A_IMPLEMENTACION\n"
                "    motivo: zona que el propio arbol se concede\n"
            ).encode("utf-8"))
        ataque = os.path.join(self.repo, "docs", "normativa", "SEGUNDA-SEDE.md")
        os.makedirs(os.path.dirname(ataque), exist_ok=True)
        with open(ataque, "w", encoding="utf-8") as manejador:
            manejador.write("# SENTENCIA\n\nF4c CERRADA.\n")
        self.addCleanup(self._borrar, ataque)

        destino = os.path.join(self.externo, "atestacion-politica.json")
        resultado, _ = self.emitir(evidencia=destino)
        self.assertNotEqual(resultado.returncode, 0,
                            "el árbol cambió su propia política y la raíz externa lo aceptó")
        sobre = self.leer_sobre(destino)
        self.assertEqual(sobre["atestacion"]["veredicto"]["color"], "ROJO")
        causas = " ".join(hallazgo["causa"] for hallazgo
                          in sobre["atestacion"]["veredicto"]["hallazgos"])
        self.assertIn("quién lo clasifica", causas)

    def _restaurar(self, ruta, contenido):
        with open(ruta, "wb") as manejador:
            manejador.write(contenido)

    def _borrar(self, ruta):
        if os.path.exists(ruta):
            os.remove(ruta)

    def test_la_trazabilidad_publica_identidad_epoca_y_digest(self):
        """T220 · Defecto que previene: una evidencia que no se puede reanclar a nada."""
        resultado, _ = self.emitir()
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        resumen = json.loads(resultado.stdout.decode("utf-8"))
        sobre = self.leer_sobre()
        self.assertEqual(resumen["digest_de_la_atestacion"],
                         modulo_de_atestacion.digest(sobre["atestacion"]))
        self.assertEqual(resumen["identidad"], sobre["atestacion"]["identidad"])
        self.assertEqual(resumen["huella_publica"],
                         sobre["atestacion"]["huella_publica"])
        self.assertEqual(resumen["epoca"], sobre["atestacion"]["epoca"])

    def test_la_atestacion_no_lleva_reloj_ni_numero_de_ejecucion(self):
        """T220 · Defecto que previene: `I-g3`, hora de pared o contador en lo derivado."""
        resultado, _ = self.emitir()
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        texto = json.dumps(self.leer_sobre()["atestacion"], sort_keys=True)
        for prohibido in ("fecha", "timestamp", "duracion", "numero_de_ejecucion", "pid"):
            self.assertNotIn(prohibido, texto)

    def test_dos_emisiones_sobre_el_mismo_commit_atestan_lo_mismo(self):
        """T220 · Defecto que previene: una evidencia que cambia sin que cambie el árbol."""
        primera = os.path.join(self.externo, "atestacion-a.json")
        segunda = os.path.join(self.externo, "atestacion-b.json")
        self.emitir(evidencia=primera)
        self.emitir(evidencia=segunda)
        uno = self.leer_sobre(primera)["atestacion"]
        otro = self.leer_sobre(segunda)["atestacion"]
        self.assertEqual(modulo_de_atestacion.canonizar(uno),
                         modulo_de_atestacion.canonizar(otro))

    def test_una_atestacion_de_otro_commit_no_sirve(self):
        """T220 · Defecto que previene: reutilizar una atestación buena sobre otro árbol."""
        resultado, _ = self.emitir()
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        with open(os.path.join(self.repo, "docs", "canonico", "otro.md"),
                  "w", encoding="utf-8") as manejador:
            manejador.write("# otro\n")
        self.canal.ejecutar("add", "-A")
        self.canal.ejecutar("commit", "--quiet", "-m", "avance")
        self.addCleanup(self._borrar,
                        os.path.join(self.repo, "docs", "canonico", "otro.md"))
        comprobacion = self.correr([
            "comprobar", "--repo", self.repo, "--configuracion", self.configuracion,
            "--evidencia", self.evidencia])
        self.assertNotEqual(comprobacion.returncode, 0)
        # `E-07`: se exige el código de la MITAD que lo detectó, no un genérico. Un commit
        # nuevo cambia el commit Y su árbol, así que la mitad que corta primero es la del
        # commit; con el código genérico esta prueba pasaba igual si el vínculo no se
        # hubiera comprobado en absoluto y algo más hubiera fallado.
        self.assertIn(b"VINCULO_DE_COMMIT_ROTO", comprobacion.stderr)


# ===========================================================================
#  T290 a T295 · `E-07` · EL VÍNCULO COMMIT + TREE, MITAD A MITAD, Y LOS SIETE PASOS
# ===========================================================================
class VinculoCommitYTree(RaizExternaInstalada):
    """`E-07`. Las DOS mitades, cada una con su prueba, y la evidencia después de los siete.

    HECHO REPRODUCIDO ANTES DE CORREGIR, y por eso existe esta clase: neutralizar la mitad
    `tree` de `exigir_vinculo` dejaba la batería en 38/38 VERDE, y neutralizar la mitad
    `commit`, también. La única prueba que tocaba el vínculo —`test_una_atestacion_de_otro_
    commit_no_sirve`— confirma un commit NUEVO, con lo que cambian el commit Y su árbol a la
    vez: cualquiera de las dos mitades bastaba para que pasara.

    Lo que estas pruebas ejercitan es la PROPIEDAD —qué RECHAZA la raíz externa— y no el
    texto de ningún mensaje: cada una fabrica un sobre FIRMADO DE VERDAD con la clave
    legítima, de modo que la firma pasa y lo único que puede cortar es la mitad que se
    quiere medir.
    """

    def sobre_firmado(self, *, commit=None, tree=None, identidad="raiz-externa-1",
                      huella=None, epoca=1, autoridad=None, base=None, clave=None,
                      color="VERDE"):
        """Un sobre con firma VÁLIDA sobre el cuerpo que se le pida. Nada simulado."""
        cuerpo = modulo_de_atestacion.construir(
            autoridad=autoridad or "raiz-externa-de-la-bateria",
            identidad=identidad,
            huella_publica=(huella if huella is not None
                            else modulo_de_firma.huella_publica(self.publica)),
            epoca=epoca,
            commit=commit or self.canal.resolver("HEAD"),
            tree=tree or self.tree_de_head(),
            veredicto={"color": color, "base": base or self.base, "hallazgos": [],
                       "digest_del_censo": self.digest_del_censo},
            proveedor={"herramienta": "ssh-keygen", "algoritmo": modulo_de_firma.ALGORITMO,
                       "version_de_openssh": "OpenSSH_ficticio", "simetrica": False,
                       "espacio_de_nombres": "ads-raiz-externa"},
        )
        blindada = modulo_de_firma.firmar(modulo_de_atestacion.canonizar(cuerpo),
                                          clave_privada=clave or self.privada)
        return modulo_de_atestacion.Sobre(cuerpo, blindada.hex())

    def tree_de_head(self):
        commit = self.canal.resolver("HEAD")
        _, salida, _ = self.canal.ejecutar("rev-parse", "--verify", commit + "^{tree}")
        return salida.decode("ascii").strip()

    def comprobar_sobre(self, sobre, nombre):
        ruta = os.path.join(self.externo, nombre)
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(sobre.serializar())
        self.addCleanup(self._borrar_si_existe, ruta)
        return self.correr(["comprobar", "--repo", self.repo,
                            "--configuracion", self.configuracion, "--evidencia", ruta])

    def _borrar_si_existe(self, ruta):
        if os.path.exists(ruta):
            os.remove(ruta)

    # -- CONTROL POSITIVO: sin él, «todo falla» no probaría nada -------------
    def test_T290_control_positivo_el_sobre_bien_construido_SI_pasa(self):
        """T290 · Control del CONTROL: el mismo camino, con commit y tree correctos, PASA."""
        resultado = self.comprobar_sobre(self.sobre_firmado(), "vinculo-sano.json")
        self.assertEqual(resultado.returncode, 0,
                         resultado.stderr.decode("utf-8", "replace")[:400])
        resumen = json.loads(resultado.stdout.decode("utf-8"))
        self.assertEqual(resumen["secuencia_de_verificacion"]["hechos"],
                         list(modulo_de_atestacion.PASOS_DE_VERIFICACION))

    # -- MITAD `tree`: commit CORRECTO, tree INCORRECTO ----------------------
    def test_T291_commit_correcto_con_tree_incorrecto_se_RECHAZA(self):
        """T291 · Defecto que previene: `E-07`, que la mitad `tree` no tenga cobertura propia.

        SABOTAJE QUE LA PONE ROJA: neutralizar la comprobación del `tree` en
        `atestacion.exigir_tree`. Ninguna otra prueba de la batería cambia.
        """
        sobre = self.sobre_firmado(tree="b" * 40)
        resultado = self.comprobar_sobre(sobre, "vinculo-tree-roto.json")
        self.assertNotEqual(resultado.returncode, 0,
                            "un `tree` que no es el del commit fue aceptado")
        self.assertIn(b"VINCULO_DE_TREE_ROTO", resultado.stderr)
        self.assertNotIn(b"VINCULO_DE_COMMIT_ROTO", resultado.stderr)

    def test_T291b_la_mitad_tree_es_una_funcion_propia_y_falla_sola(self):
        """T291 · La mitad `tree` ejercida DIRECTAMENTE, sin que la del commit intervenga."""
        cuerpo = self.sobre_firmado().atestacion
        self.assertTrue(modulo_de_atestacion.exigir_commit(cuerpo,
                                                           self.canal.resolver("HEAD")))
        with self.assertRaises(VinculoDeTreeRoto):
            modulo_de_atestacion.exigir_tree(cuerpo, "c" * 40)

    # -- MITAD `commit`: tree CORRECTO, commit INCORRECTO --------------------
    def test_T292_tree_correcto_con_commit_incorrecto_se_RECHAZA(self):
        """T292 · Defecto que previene: `E-07`, que la mitad `commit` no tenga cobertura propia.

        SABOTAJE QUE LA PONE ROJA: neutralizar la comprobación del commit en
        `atestacion.exigir_commit`. Ninguna otra prueba de la batería cambia.
        """
        sobre = self.sobre_firmado(commit="a" * 40)
        resultado = self.comprobar_sobre(sobre, "vinculo-commit-roto.json")
        self.assertNotEqual(resultado.returncode, 0,
                            "un commit que no es el comprobado fue aceptado")
        self.assertIn(b"VINCULO_DE_COMMIT_ROTO", resultado.stderr)

    def test_T292b_la_mitad_commit_es_una_funcion_propia_y_falla_sola(self):
        """T292 · La mitad `commit` ejercida DIRECTAMENTE, con el `tree` correcto al lado."""
        cuerpo = self.sobre_firmado().atestacion
        self.assertTrue(modulo_de_atestacion.exigir_tree(cuerpo, self.tree_de_head()))
        with self.assertRaises(VinculoDeCommitRoto):
            modulo_de_atestacion.exigir_commit(cuerpo, "a" * 40)

    def test_T293_las_dos_mitades_incorrectas_se_RECHAZAN(self):
        """T293 · Defecto que previene: una atestación de otro árbol reutilizada entera."""
        sobre = self.sobre_firmado(commit="a" * 40, tree="b" * 40)
        resultado = self.comprobar_sobre(sobre, "vinculo-ambos-rotos.json")
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn(b"VINCULO_DE_", resultado.stderr)

    def test_T293b_una_firma_CORRECTA_de_una_tupla_DISTINTA_no_sirve(self):
        """T293 · Defecto que previene: reusar una firma buena cambiando de qué habla.

        La firma verifica: es del cuerpo que se firmó, byte a byte. Lo que no vale es la
        TUPLA `(commit, tree)` que ese cuerpo declara. Sin esta prueba, «la firma es válida»
        podría confundirse con «la atestación vale para este árbol».
        """
        # Se avanza el árbol, de modo que la tupla firmada deja de ser la vigente.
        ruta = os.path.join(self.repo, "docs", "canonico", "avance-e07.md")
        sobre = self.sobre_firmado()
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write("# avance\n")
        self.canal.ejecutar("add", "-A")
        self.canal.ejecutar("commit", "--quiet", "-m", "avance E-07")
        self.addCleanup(self._deshacer_avance, ruta)
        # La firma sigue siendo válida sobre EXACTAMENTE esos bytes...
        valida, _ = modulo_de_firma.verificar(
            modulo_de_atestacion.canonizar(sobre.atestacion), sobre.firma,
            firmantes=self.firmantes, principal="raiz-externa-1")
        self.assertTrue(valida, "el control positivo de la firma falló")
        # ...y aun así la raíz externa la RECHAZA, porque habla de otra tupla.
        resultado = self.comprobar_sobre(sobre, "vinculo-tupla-distinta.json")
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn(b"VINCULO_DE_COMMIT_ROTO", resultado.stderr)

    def _deshacer_avance(self, ruta):
        if os.path.exists(ruta):
            os.remove(ruta)
        self.canal.ejecutar("add", "-A")
        self.canal.ejecutar("commit", "--quiet", "-m", "retirada del avance E-07")

    def test_T294_una_clave_valida_para_OTRA_EPOCA_se_rechaza(self):
        """T294 · Defecto que previene: una firma buena fuera de la ventana de su identidad.

        La clave es la LEGÍTIMA y la firma verifica. Lo que no vale es la ÉPOCA: la
        configuración declara `raiz-externa-1` RETIRADA con solapamiento 1 desde la época 2,
        y la atestación dice hablar de la época 9. `I-g3`: tiempo lógico, no reloj.
        """
        configuracion = escribir_configuracion(
            os.path.join(self.externo, "confianza-epoca.yml"),
            self._datos_de_configuracion(identidades=[
                {"id": "raiz-externa-1", "algoritmo": modulo_de_firma.ALGORITMO,
                 "huella_publica": modulo_de_firma.huella_publica(self.publica),
                 "estado": "retirada", "epoca_de_alta": 1, "epoca_de_retirada": 2,
                 "solapamiento": 1},
                {"id": "raiz-externa-2", "algoritmo": modulo_de_firma.ALGORITMO,
                 "huella_publica": modulo_de_firma.huella_publica(self.publica_2),
                 "estado": "activa", "epoca_de_alta": 2},
            ], epoca=9))
        sobre = self.sobre_firmado(epoca=9)
        ruta = os.path.join(self.externo, "epoca-fuera-de-ventana.json")
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(sobre.serializar())
        self.addCleanup(self._borrar_si_existe, ruta)
        resultado = self.correr(["comprobar", "--repo", self.repo,
                                 "--configuracion", configuracion, "--evidencia", ruta])
        self.assertNotEqual(resultado.returncode, 0,
                            "una identidad fuera de su solapamiento fue aceptada")
        self.assertIn(b"IDENTIDAD_NO_ACEPTADA", resultado.stderr)

    def test_T294b_la_huella_del_emisor_tiene_que_ser_la_del_anillo(self):
        """T294 · Defecto que previene: atribuir una atestación a quien no la firmó.

        El sobre se firma con la clave LEGÍTIMA de `raiz-externa-1` y publica la huella
        pública de OTRA clave. La firma verifica y el vínculo casa: sólo el paso 7 lo corta.
        """
        sobre = self.sobre_firmado(
            huella=modulo_de_firma.huella_publica(self.publica_ajena))
        resultado = self.comprobar_sobre(sobre, "emisor-con-huella-ajena.json")
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn(b"EMISOR_NO_COINCIDE", resultado.stderr)

    def test_T294c_una_atestacion_bajo_OTRA_politica_se_rechaza(self):
        """T294 · Defecto que previene: colar un veredicto calculado contra otra base."""
        sobre = self.sobre_firmado(base="f" * 40)
        resultado = self.comprobar_sobre(sobre, "ancla-distinta.json")
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn(b"ANCLA_NO_COINCIDE", resultado.stderr)

    def test_T295_modificar_la_atestacion_DESPUES_de_firmarla_la_invalida(self):
        """T295 · Defecto que previene: reescribir la tupla del repositorio tras la firma."""
        sobre = self.sobre_firmado()
        datos = json.loads(sobre.serializar())
        # Se cambia el `tree` DESPUÉS de firmar, y se recalcula el digest publicado para que
        # el sobre no se delate por ahí: lo único que queda es la firma.
        datos["atestacion"]["repositorio"]["tree"] = "d" * 40
        datos["firma"]["digest_de_lo_firmado"] = modulo_de_atestacion.digest(
            datos["atestacion"])
        ruta = os.path.join(self.externo, "modificada-despues-de-firmar.json")
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(json.dumps(datos, sort_keys=True, ensure_ascii=False,
                                       indent=2) + "\n")
        self.addCleanup(self._borrar_si_existe, ruta)
        resultado = self.correr(["comprobar", "--repo", self.repo,
                                 "--configuracion", self.configuracion,
                                 "--evidencia", ruta])
        self.assertNotEqual(resultado.returncode, 0)
        self.assertIn(b"FIRMA_NO_VERIFICADA", resultado.stderr)


# ===========================================================================
#  T296 · `E-07` · LA EVIDENCIA, SÓLO DESPUÉS DE LOS SIETE PASOS
# ===========================================================================
class SecuenciaDeLosSietePasos(RaizExternaInstalada):
    """La evidencia NO se escribe antes de completar firma · clave · época · commit · tree ·
    política · identidad del emisor. Se INTERRUMPE en cada uno de los siete."""

    def test_T296_interrumpir_en_CADA_paso_deja_CERO_ficheros(self):
        """T296 · Defecto que previene: publicar evidencia de lo que no se ha verificado.

        Se ejercita la PUERTA REAL —`atestacion.escribir_evidencia`, la misma que usa el
        punto ejecutable— con el testigo cortado en cada uno de los siete pasos. La
        propiedad medida no es «se levanta una excepción»: es que **no queda fichero**.
        """
        sobre = modulo_de_atestacion.Sobre(
            modulo_de_atestacion.construir(
                autoridad="a", identidad="raiz-externa-1", huella_publica="SHA256:x",
                epoca=1, commit="a" * 40, tree="b" * 40,
                veredicto={"color": "VERDE"}, proveedor={"herramienta": "ssh-keygen"}),
            "00")
        pasos = modulo_de_atestacion.PASOS_DE_VERIFICACION
        for corte in range(len(pasos)):
            with self.subTest(interrumpido_en=pasos[corte]):
                secuencia = modulo_de_atestacion.SecuenciaDeVerificacion()
                for paso in pasos[:corte]:
                    secuencia.anotar(paso)
                destino = os.path.join(self.externo,
                                       "corte-" + str(corte) + ".json")
                with self.assertRaises(SecuenciaDeVerificacionIncompleta):
                    modulo_de_atestacion.escribir_evidencia(destino, sobre, secuencia)
                self.assertFalse(os.path.exists(destino),
                                 "se escribió evidencia con la secuencia cortada en "
                                 + pasos[corte])
        # CONTROL DEL CONTROL: con los SIETE anotados, la misma llamada SÍ escribe.
        completa = modulo_de_atestacion.SecuenciaDeVerificacion()
        for paso in pasos:
            completa.anotar(paso)
        destino = os.path.join(self.externo, "corte-completo.json")
        self.addCleanup(self._borrar, destino)
        modulo_de_atestacion.escribir_evidencia(destino, sobre, completa)
        self.assertTrue(os.path.exists(destino))

    def test_T296b_los_pasos_fuera_de_ORDEN_son_un_fallo(self):
        """T296 · Defecto que previene: que el orden sea una costumbre y no una garantía."""
        secuencia = modulo_de_atestacion.SecuenciaDeVerificacion()
        with self.assertRaises(SecuenciaDeVerificacionIncompleta):
            secuencia.anotar("tree")          # antes que la firma
        secuencia.anotar("firma")
        with self.assertRaises(SecuenciaDeVerificacionIncompleta):
            secuencia.anotar("politica")      # saltándose clave, época, commit y tree

    def test_T296c_sin_testigo_no_se_escribe_evidencia(self):
        """T296 · Defecto que previene: escribir «porque el código llegó hasta aquí»."""
        destino = os.path.join(self.externo, "sin-testigo.json")
        with self.assertRaises(SecuenciaDeVerificacionIncompleta):
            modulo_de_atestacion.escribir_evidencia(destino, object(), None)
        self.assertFalse(os.path.exists(destino))

    def test_T296d_la_emision_publica_los_SIETE_pasos_en_su_orden(self):
        """T296 · Defecto que previene: una emisión que dice verificar y no lo demuestra."""
        resultado, _ = self.emitir()
        self.assertEqual(resultado.returncode, 0, resultado.stderr.decode())
        resumen = json.loads(resultado.stdout.decode("utf-8"))
        self.assertEqual(resumen["secuencia_de_verificacion"]["hechos"],
                         list(modulo_de_atestacion.PASOS_DE_VERIFICACION))
        self.assertTrue(resumen["secuencia_de_verificacion"]["completa"])

    def _borrar(self, ruta):
        if os.path.exists(ruta):
            os.remove(ruta)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
