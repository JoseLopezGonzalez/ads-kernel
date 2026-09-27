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
        pasa, _, motivo = H.decidir(1, DIVERGENTE, "claude/directiva-oficina-profesional-r19", None)
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
