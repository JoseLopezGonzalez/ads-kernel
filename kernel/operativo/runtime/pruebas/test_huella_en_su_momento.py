#!/usr/bin/env python3
"""T519 · La batería de macOS comprueba portabilidad, y la huella se juzga en su momento del ciclo.

Defecto que cierra (medido en r13, r15, r18 y r19): el job ejecutaba `kernel-status.sh` con
`set -e` antes del sello, salía rojo por una divergencia que es normal hasta que el job de
release sella, y no llegaba a ejecutar la comprobación de `execve` en POSIX. Dos mitades:

  · la DECISIÓN (`tooling/huella_en_su_momento.py`): pasa la divergencia previa al sello y
    sólo ésa; `main`, una divergencia sin cambios desde el sello y un kernel-status que no
    responde siguen siendo rojo.
  · la FORMA del job (`.github/workflows/kernel.yml`): cada propiedad en su paso, los dos
    últimos corren aunque falle el anterior, y ningún paso exige LIMPIO a pelo antes del sello.
    Esta mitad se salta con su motivo donde el workflow no viaja (una instancia vendorizada).
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
import sys
import unittest

AQUI = os.path.dirname(os.path.abspath(__file__))
KERNEL = os.path.dirname(os.path.dirname(AQUI))                       # kernel/operativo
REPO = os.path.dirname(os.path.dirname(KERNEL))                       # raíz del repositorio
sys.path.insert(0, os.path.join(REPO, "tooling"))
import huella_en_su_momento as H  # noqa: E402

LIMPIO = "kernel version : x\nhuella local   : abc\nestado         : LIMPIO (coincide con el release)\n"
DIVERGENTE = "kernel version : x\nhuella local   : abc\nestado         : DIVERGENTE — el kernel ha sido editado localmente.\n"
WORKFLOW = os.path.join(REPO, ".github", "workflows", "kernel.yml")


class Decision(unittest.TestCase):

    def test_01_la_divergencia_previa_al_sello_no_es_un_fallo_de_macos(self):
        pasa, _, motivo = H.decidir(1, DIVERGENTE, "oficina/directiva-profesional", 3)
        self.assertTrue(pasa, motivo)
        pasa, _, motivo = H.decidir(1, DIVERGENTE, "release/corte-r19", None)
        self.assertTrue(pasa, motivo)

    def test_02_limpio_pasa(self):
        self.assertTrue(H.decidir(0, LIMPIO, "main", 0)[0])

    def test_03_en_main_la_huella_tiene_que_estar_sellada(self):
        pasa, _, motivo = H.decidir(1, DIVERGENTE, "main", 5)
        self.assertFalse(pasa)
        self.assertIn("sellados", motivo)

    def test_04_divergir_sin_haber_cambiado_nada_desde_el_sello_es_rojo(self):
        pasa, _, motivo = H.decidir(1, DIVERGENTE, "oficina/x", 0)
        self.assertFalse(pasa)
        self.assertIn("sello roto", motivo)

    def test_05_un_kernel_status_que_no_responde_es_un_fallo_de_portabilidad(self):
        for codigo, salida in ((127, ""), (1, "Traceback (most recent call last):\n"), (2, "estado : NO COMPROBABLE"),
                               (0, DIVERGENTE), (1, LIMPIO)):
            pasa, _, motivo = H.decidir(codigo, salida, "oficina/x", 3)
            self.assertFalse(pasa, (codigo, salida, motivo))
            self.assertIn("portabilidad", motivo)


@unittest.skipUnless(os.path.isfile(WORKFLOW), "el workflow del kernel no viaja en una copia vendorizada")
class FormaDelJob(unittest.TestCase):

    def _pasos_de_macos(self):
        import yaml  # noqa: PLC0415
        with open(WORKFLOW, encoding="utf-8") as fichero:
            flujo = yaml.safe_load(fichero)
        return flujo["jobs"]["macos"]["steps"]

    def test_06_ningun_paso_exige_limpio_a_pelo_antes_del_sello(self):
        for paso in self._pasos_de_macos():
            orden = str(paso.get("run") or "")
            lineas = [l.strip() for l in orden.splitlines()]
            self.assertNotIn("./tooling/kernel-status.sh", lineas,
                             "%s ejecuta kernel-status.sh a pelo: con set -e, la divergencia previa al "
                             "sello tumba el job y tapa lo que viene después" % paso.get("name"))

    def test_07_las_propiedades_posix_y_la_huella_corren_aunque_falle_lo_anterior(self):
        pasos = {str(p.get("name")): p for p in self._pasos_de_macos()}
        execve = [p for n, p in pasos.items() if "execve" in n]
        huella = [p for p in pasos.values() if "huella_en_su_momento.py" in str(p.get("run") or "")]
        self.assertTrue(execve and huella, sorted(pasos))
        for paso in execve + huella:
            self.assertIn("failure()", str(paso.get("if") or ""), paso.get("name"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
