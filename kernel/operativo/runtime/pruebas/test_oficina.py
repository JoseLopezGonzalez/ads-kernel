#!/usr/bin/env python3
"""test_oficina — `T460`–`T475`: el protocolo de trabajadores, la entrega, los niveles y el supervisor.

Contrato: `CONTRATO-OFICINA.md`. Todo esto EJECUTA sobre control repos reales en directorios
temporales, con trabajadores que son PROCESOS reales cuando la propiedad lo exige —una
muerte con lease, una carrera por el mismo paquete— y con un agente sin chat que es un
ejecutable de verdad lanzado por el adaptador de agente.

Ninguna prueba certifica nada: `prueba-superada` significa que se ejecutó y pasó.

    python3 kernel/operativo/runtime/pruebas/test_oficina.py

Sale con 0 si todo pasa. Se ejecuta desde cualquier directorio: la raíz se deriva de
`__file__` y NUNCA del `cwd`.
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
#  ESTA SEDE nace el 2026-09-14 con el prólogo puesto: `T330` exige que toda batería lo
#  lleve, y su salida se PUBLICA como evidencia de los escenarios `T460`-`T475`. Un `json.py`
#  homónimo en el `PYTHONPATH` de quien la corre decidiría qué dice esa evidencia, y en esta
#  batería la evidencia es lo que sostiene que el protocolo de trabajadores funciona.
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

import contextlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
RUNTIME = os.path.join(RAIZ, "kernel", "operativo", "runtime")
KERNEL = os.path.join(RAIZ, "kernel", "operativo")
CLI = os.path.join(RUNTIME, "ads_ciclo.py")
sys.path.insert(0, RUNTIME)
sys.path.insert(0, AQUI)

import adaptadores                                                   # noqa: E402
import ciclo                                                         # noqa: E402
import runtime as paquete_runtime                                    # noqa: E402
from ciclo import agentes, briefs, entregas, oficina, tablero, terminacion  # noqa: E402
from runtime import supervisor as modulo_supervisor                  # noqa: E402
import catalogo_de_prueba                                            # noqa: E402

ENTORNO = {k: v for k, v in os.environ.items()
           if k not in ("ADS_RUNTIME_FALLO", "ADS_ESTADO_FALLO", "ADS_ADAPTADOR_FALLO")}

CIRCUITO_INTERFAZ = '''
```yaml ads:circuito-base
id: circuito:cambio-con-interfaz
nombre: Cambio con interfaz
clase_de_trabajo: cambio-con-interfaz
cuando_aplica: el item escribe en una fuente con pantalla y el usuario ve algo distinto
materia: capacidad-ausente
estado_del_objeto: no-existe
condiciones_de_ruta: [C-DIS]
composiciones: [composicion:prd-alcance-rutinario, composicion:dis-extension-de-patron, composicion:con-implementacion, composicion:ver-dosier]
niveles_obligatorios: [implementado, revisado, verificado, validado-visual, aceptado]
inaplicabilidad: []
roles_minimos: [DIS/diseno-visual, DIS/revision-de-fidelidad, CNS/implementacion, CNS/revision-de-construccion, VER/dosier]
independencias:
  - rol: CNS/revision-de-construccion
    de: [CNS/implementacion]
  - rol: DIS/revision-de-fidelidad
    de: [CNS/implementacion, DIS/diseno-visual]
gates_de_cierre: [gate:cierre-de-item]
```
'''

CIRCUITO_BACKEND = '''
```yaml ads:circuito-base
id: circuito:cambio-de-backend
nombre: Cambio de backend
clase_de_trabajo: cambio-de-backend
cuando_aplica: el item escribe solo en el backend y no toca ninguna pantalla
materia: capacidad-ausente
estado_del_objeto: no-existe
condiciones_de_ruta: []
composiciones: [composicion:prd-alcance-rutinario, composicion:con-implementacion, composicion:ver-dosier]
niveles_obligatorios: [implementado, revisado, verificado, validado-visual, aceptado]
inaplicabilidad:
  - nivel: validado-visual
    condicion: afecta_superficie es-falso
    quien_lo_declara: DSP al planificar, sobre escribe_fuentes
roles_minimos: [CNS/implementacion, CNS/revision-de-construccion, VER/dosier]
independencias:
  - rol: CNS/revision-de-construccion
    de: [CNS/implementacion]
gates_de_cierre: [gate:cierre-de-item]
```
'''

# El AGENTE SIN CHAT de estas pruebas: un ejecutable real que lee el brief JSON y escribe
# una entrega válida. Es un `python -c` para no añadir un punto ejecutable al inventario.
AGENTE_STUB = r'''
import json, sys
brief = json.load(open(sys.argv[1][:-3] + ".json", encoding="utf-8"))
forma = brief["forma_de_la_entrega"]
rol = brief["rol"]["id"]
entrega = {
  "paquete": brief["paquete"], "rol": rol, "veredicto": "entregado",
  "artefactos": [{"tipo": t, "referencia": "ref-" + t, "descripcion": "artefacto " + t}
                 for t in ["commit", "rama", "salida-de-orden", "dosier", "medicion", "documento"]],
  "evidencias": [], "diferencias_declaradas": [], "decisiones_asumidas": [], "riesgos": [],
  "deuda_aceptada": [], "no_hecho": [], "siguiente": "al siguiente rol",
  "autoevaluacion": {"gate": brief["gate"]["id"],
                     "comprobaciones": [{"id": c, "resultado": "si"} for c in forma["comprobaciones_del_gate"]],
                     "checklist": [{"id": c, "respuesta": "si"} for c in forma["checklist"]]},
}
if brief["entregas_previas"] and rol in ("CNS/revision-de-construccion", "VER/dosier"):
    juzgado = [e for e in brief["entregas_previas"] if e["rol"] == "CNS/implementacion"]
    if juzgado:
        gates = ["gate:implementacion-completa", "gate:revision-de-construccion"] if rol.startswith("CNS") else ["gate:evidencia-suficiente"]
        entrega["dictamenes"] = [{"gate": g, "sobre_paquete": juzgado[-1]["id"].rsplit("-", 1)[0],
                                  "comprobaciones_superadas": brief.get("_comprobaciones", {}).get(g, []),
                                  "evidencia": brief.get("_evidencia", {}).get(g, []), "dictamen": "superado"} for g in gates]
json.dump(entrega, open(sys.argv[2], "w", encoding="utf-8"))
'''


def _ejecutor(modelo):
    return ("```yaml ads:ejecutor\nid: ejecutor:" + modelo.split(":")[1] + "\nmodelo: " + modelo
            + "\nargv:\n  - " + sys.executable + "\n  - -c\n  - " + json.dumps(AGENTE_STUB)
            + "\n  - \"{brief}\"\n  - \"{entrega}\"\nlimite_segundos: 60\n```\n")


class Laboratorio(unittest.TestCase):
    """Un control repo real con PROFILE (catálogo, circuito base y ejecutores)."""

    @classmethod
    def setUpClass(cls):
        cls.corpus = ciclo.Corpus(KERNEL)
        cls.politica = agentes.Politica(cls.corpus)

    def setUp(self):
        self.repo = tempfile.mkdtemp(prefix="ads-oficina-")
        self.addCleanup(shutil.rmtree, self.repo, True)
        perfil = catalogo_de_prueba.texto(self.politica, self.corpus) + CIRCUITO_BACKEND + CIRCUITO_INTERFAZ
        for modelo in ("modelo:alfa", "modelo:beta", "modelo:gamma", "modelo:delta", "modelo:epsilon"):
            perfil += _ejecutor(modelo)
        with open(os.path.join(self.repo, "PROFILE.md"), "w", encoding="utf-8") as manejador:
            manejador.write(perfil)
        self.circuitos = terminacion.cargar_circuitos_base(self.repo, corpus=self.corpus)
        self.circuito = self.circuitos["cambio-de-backend"]
        self.abiertos = []

    def tearDown(self):
        for rt in self.abiertos:
            try:
                rt.cerrar()
            except Exception:                                        # noqa: BLE001
                pass

    def rt(self, instancia, registro=None):
        rt = paquete_runtime.Runtime(self.repo, instancia=instancia,
                                     registro_de_adaptadores=registro).abrir()
        self.abiertos.append(rt)
        return rt

    def entrada(self, texto="exportar la tabla a CSV"):
        return {"clase": "item", "expresion_literal": texto, "canal": "chat",
                "fecha": "2026-09-14", "resultado_perseguido": "el usuario descarga la tabla completa en CSV",
                "evidencia_de_cierre": ["un CSV con las mismas filas"], "anclaje_terminado": True}

    def planificar(self, rt, item="enc-x", ordenes=None):
        return oficina.planificar(rt, corpus=self.corpus, entrada=self.entrada(), circuito=self.circuito,
                                  control_repo=self.repo, item=item, titulo="Exportar CSV", ordenes=ordenes)

    @staticmethod
    def filas(plan):
        return {f["paquete"]: f for f in plan["correspondencia"]}

    def paquete_de(self, plan, rol):
        return [p for p, f in self.filas(plan).items() if f.get("rol") == rol][0]

    def autoevaluacion(self, gate, rol):
        contrato = self.corpus.contrato_operativo_de(rol) or {}
        return {"gate": gate,
                "comprobaciones": [{"id": c["id"], "resultado": "si"}
                                   for c in self.corpus.gates()[gate]["comprobaciones"]],
                "checklist": [{"id": c["id"], "respuesta": "si"} for c in contrato.get("checklist", [])]}

    def entrega(self, paquete, rol, veredicto="entregado"):
        gate = self.corpus.rol(rol)["gate"]
        return {"paquete": paquete, "rol": rol, "veredicto": veredicto,
                "artefactos": [{"tipo": t, "referencia": "ref-" + t, "descripcion": "artefacto " + t}
                               for t in ("commit", "rama", "salida-de-orden", "dosier", "medicion", "documento")],
                "evidencias": [], "autoevaluacion": self.autoevaluacion(gate, rol),
                "diferencias_declaradas": [], "decisiones_asumidas": [], "riesgos": [],
                "deuda_aceptada": [], "no_hecho": [], "siguiente": "al siguiente rol"}

    def dictamen(self, gate, sobre, dictamen="superado"):
        declarado = self.corpus.gates()[gate]
        return {"gate": gate, "sobre_paquete": sobre,
                "comprobaciones_superadas": [c["id"] for c in declarado["comprobaciones"]]
                if dictamen == "superado" else [declarado["comprobaciones"][0]["id"]],
                "evidencia": list(declarado["evidencia"]), "dictamen": dictamen}

    def tomar_y_acusar(self, rt, paquete):
        toma = oficina.tomar(rt, corpus=self.corpus, paquete=paquete, circuito=self.circuito)
        for h in toma["brief"]["recibes"]:
            oficina.acusar(rt, corpus=self.corpus, handoff=h["id"],
                           comprobaciones_superadas=h["comprueba_al_recibir"])
        return toma

    def entregar(self, rt, paquete, entrega):
        return oficina.entregar(rt, corpus=self.corpus, paquete=paquete, entrega=entrega,
                                circuito=self.circuito)

    def avanzar_prd(self, rt, plan, impl):
        """Entrega los paquetes de PRD hasta que la implementación no espere a nadie."""
        filas = self.filas(plan)
        for _ in range(6):
            pendientes, inviables = rt._dependencias_pendientes(rt._leer_paquete(impl))
            if not pendientes and not inviables:
                return
            tomables = [t["paquete"] for t in rt.tomables()["tomables"]
                        if t["paquete"] != impl and t["paquete"] in filas]
            pq = tomables[0]
            self.tomar_y_acusar(rt, pq)
            self.entregar(rt, pq, self.entrega(pq, filas[pq]["rol"]))
        self.fail("la implementación nunca fue tomable")

    def cli(self, *argumentos, instancia="cli-A"):
        return subprocess.run([sys.executable, CLI, "--repo", self.repo, "--instancia", instancia,
                               "--json"] + list(argumentos), capture_output=True, text=True,
                              env=ENTORNO, cwd=self.repo)


# =========================================================================
# T460 · tomar, checkpoint, entregar, reintento entre dos trabajadores
# =========================================================================
class ProtocoloDeTrabajadores(Laboratorio):

    def test_01_tomar_checkpoint_entregar_y_reintento_entre_dos_trabajadores(self):
        """T460 · Defecto que previene: una ejecución que sólo existe en un chat."""
        A = self.rt("w-A")
        A.crear_item(id="it-1", titulo="primero", motivo="alta")
        A.crear_paquete(id="pq-1", item="it-1", capacidades_requeridas=["worker"],
                        orden=paquete_runtime.orden_externa(argumentos=["CNS", "CNS/implementacion"]))
        self.assertEqual([t["paquete"] for t in A.tomables()["tomables"]], ["pq-1"])
        toma = A.tomar("pq-1")
        self.assertEqual(toma["estado"], "ejecutando")
        self.assertEqual(toma["intento"], 1)
        self.assertTrue(toma["efecto"].startswith("ef-"))
        cp = A.checkpoint("pq-1", {"paso": 2})
        self.assertEqual(cp["contenido"], {"paso": 2})
        self.assertEqual(A._leer_lease("pq-1")["latido"], 3)
        B = self.rt("w-B")
        with self.assertRaises(paquete_runtime.AutoridadNoDisponible):
            B.tomar("pq-1")
        res = A.entregar("pq-1", {"estado": "fallido", "codigo": 1, "salida": "", "detalle": "x",
                                  "reintentable": True})
        self.assertEqual(res["desenlace"], "fallido")
        self.assertEqual(A._leer_paquete("pq-1")["estado"], "listo")
        toma = B.tomar("pq-1")
        self.assertEqual(toma["intento"], 2)
        self.assertEqual(toma["checkpoint"]["contenido"], {"paso": 2})
        res = B.entregar("pq-1", {"estado": "completado", "codigo": 0, "salida": "ok", "detalle": "",
                                  "reintentable": False})
        self.assertEqual(res["desenlace"], "completado")
        self.assertTrue(A.almacen.verificar_integridad().a_dict()["ok"])

    def test_02_un_paquete_no_externo_no_se_toma_y_una_entrega_mal_formada_no_toca_el_estado(self):
        """T460 · Defecto que previene: entregar lo que el dispatcher ejecuta, o entregar basura."""
        A = self.rt("w-A")
        A.crear_item(id="it-1", titulo="primero", motivo="alta")
        A.crear_paquete(id="pq-p", item="it-1", capacidades_requeridas=["proceso-local"],
                        orden={"adaptador": "proceso-local", "operacion": "ejecutar",
                               "argumentos": ["/bin/true"], "limite_segundos": 5})
        with self.assertRaises(paquete_runtime.EstadoDePaqueteInvalido):
            A.tomar("pq-p")
        A.crear_paquete(id="pq-e", item="it-1", capacidades_requeridas=["worker"],
                        orden=paquete_runtime.orden_externa())
        A.tomar("pq-e")
        revision = A.almacen.revision()["revision"]
        with self.assertRaises(paquete_runtime.RuntimeInconsistente):
            A.entregar("pq-e", {"estado": "terminado", "codigo": 0})
        self.assertEqual(A.almacen.revision()["revision"], revision)


# =========================================================================
# T461 · muerte con lease, reoferta y reanudación desde el checkpoint
# =========================================================================
class MuerteDelTrabajador(Laboratorio):

    def test_03_un_trabajador_que_muere_con_el_lease_es_reofrecido_tras_paciencia(self):
        """T461 · Defecto que previene: un paquete secuestrado por un trabajador muerto."""
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        primero = A.tomables()["tomables"][0]["paquete"]
        A.cerrar()
        # Un PROCESO real toma el paquete, deja checkpoint y MUERE sin entregar: su lease
        # queda sin latido. Es la muerte que hay que sobrevivir.
        proceso = self.cli("tomar", "--paquete", primero, "--clase-de-trabajo", "cambio-de-backend",
                           instancia="w-muerto")
        self.assertEqual(proceso.returncode, 0, proceso.stderr)
        proceso = self.cli("checkpoint", "--paquete", primero, "--nota", "a mitad", instancia="w-muerto")
        self.assertEqual(proceso.returncode, 0, proceso.stderr)
        S = self.rt("supervisor")
        reofrecido = None
        for pasada in range(S.paciencia + 1):
            informe = S.ciclo()
            self.assertEqual(informe["atendidos"], [])
            if primero in informe["reofrecidos"]:
                reofrecido = pasada
                break
        self.assertIsNotNone(reofrecido, "nunca se reofreció")
        self.assertEqual(reofrecido, S.paciencia)          # ni antes, ni por vía rápida
        self.assertIsNone(S._leer_lease(primero))
        self.assertEqual(S._leer_paquete(primero)["estado"], "ejecutando")
        B = self.rt("w-B")
        toma = B.tomar(primero)
        self.assertEqual(toma["intento"], 1)                # MISMO intento, MISMO efecto
        self.assertEqual(toma["checkpoint"]["contenido"], {"nota": "a mitad"})
        self.assertEqual(toma["checkpoint"]["titular"], "w-muerto")

    def test_04_dos_procesos_compiten_por_el_mismo_paquete_y_exactamente_uno_lo_toma(self):
        """T462 · Defecto que previene: doble despacho entre dos sesiones."""
        A = self.rt("w-A")
        self.planificar(A)
        primero = A.tomables()["tomables"][0]["paquete"]
        A.cerrar()
        procesos = [subprocess.Popen(
            [sys.executable, CLI, "--repo", self.repo, "--instancia", "w-" + n, "--json",
             "tomar", "--paquete", primero, "--clase-de-trabajo", "cambio-de-backend"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, env=ENTORNO, cwd=self.repo) for n in ("uno", "dos")]
        salidas = [p.communicate(timeout=120) for p in procesos]
        codigos = sorted(p.returncode for p in procesos)
        self.assertEqual(codigos, [0, 1], salidas)
        perdedor = [s for p, s in zip(procesos, salidas) if p.returncode == 1][0]
        self.assertIn("AUTORIDAD_NO_DISPONIBLE", perdedor[1])
        S = self.rt("lector")
        self.assertEqual(S._leer_paquete(primero)["intentos"], 1)
        self.assertEqual(S._leer_lease(primero)["titular"], "w-" + [n for n, p in zip(
            ("uno", "dos"), procesos) if p.returncode == 0][0])
        # y un paquete que NO está en ningún plan no se toma por la puerta de la oficina, y
        # no deja lease detrás
        S.crear_item(id="it-suelto", titulo="suelto", motivo="alta")
        S.crear_paquete(id="pq-suelto", item="it-suelto", capacidades_requeridas=["worker"],
                        orden=paquete_runtime.orden_externa())
        with self.assertRaises(ciclo.CicloInconsistente):
            oficina.tomar(S, corpus=self.corpus, paquete="pq-suelto", circuito=self.circuito)
        self.assertIsNone(S._leer_lease("pq-suelto"))
        self.assertEqual(S._leer_paquete("pq-suelto")["estado"], "listo")


# =========================================================================
# T463 · planificación por rol
# =========================================================================
class PlanificacionPorRol(Laboratorio):

    def test_05_un_paquete_por_rol_y_la_revision_espera_a_la_implementacion(self):
        """T463 · Defecto que previene: un equipo materializado sin trabajo por rol."""
        A = self.rt("dsp")
        res = self.planificar(A)
        plan = res["plan"]
        filas = self.filas(plan)
        roles = [f["rol"] for f in plan["correspondencia"]]
        self.assertIn("CNS/implementacion", roles)
        self.assertIn("CNS/revision-de-construccion", roles)
        self.assertIn("VER/dosier", roles)
        impl = self.paquete_de(plan, "CNS/implementacion")
        rev = self.paquete_de(plan, "CNS/revision-de-construccion")
        ver = self.paquete_de(plan, "VER/dosier")
        self.assertIn(impl, filas[rev]["depende_de"])
        self.assertIn(rev, filas[ver]["depende_de"])
        # PRD va ANTES que CNS: el orden lo manda la obligación del proceso, no el alfabeto
        orden = [f["capacidad"] for f in plan["correspondencia"]]
        self.assertLess(orden.index("PRD"), orden.index("CNS"))
        # y la propietaria global cierra con la integración semántica, que espera a todos
        integracion = [f for f in plan["correspondencia"] if f.get("integracion_semantica")]
        self.assertEqual(len(integracion), 1)
        self.assertEqual(set(integracion[0]["depende_de"]),
                         set(plan["paquetes"]) - {integracion[0]["paquete"]})
        self.assertEqual(filas[rev]["gate"], "gate:revision-de-construccion")
        self.assertEqual(filas[rev]["metodo"], "CNS/RevisionDeConstruccion")
        # todos externos: el barrido no los despacha ni los posterga
        informe = A.ciclo()
        self.assertEqual(informe["atendidos"], [])
        self.assertEqual(informe["postergados"], [])
        # sin catálogo en el PROFILE no se planifica: fallo cerrado, sin agente por defecto
        with open(os.path.join(self.repo, "PROFILE.md"), "w", encoding="utf-8") as manejador:
            manejador.write(CIRCUITO_BACKEND)
        with self.assertRaises(ciclo.RolSinAgente):
            self.planificar(A, item="enc-y")

    def test_05b_una_revision_de_diseno_va_despues_de_construir_y_replanificar_es_otra_generacion(self):
        """T463 · Defecto que previene: diseñar después de verificar, o un ciclo silencioso al replanificar.

        Medido en La Pesquerapp con `cambio-con-interfaz`: `DIS` es condicional (`C-DIS`) y las
        obligatorias iban todas antes que cualquier condicional, así que el diseño quedaba
        detrás de `VER`; y al corregir el orden y replanificar, los paquetes viejos —mismo id—
        se reutilizaron con sus dependencias viejas, con un ciclo dentro.
        """
        A = self.rt("dsp")
        circuito = self.circuitos["cambio-con-interfaz"]
        plan = oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=circuito,
                                  control_repo=self.repo, item="enc-ui", titulo="Con pantalla")["plan"]
        filas = self.filas(plan)
        rol_de = {f["paquete"]: f.get("rol") for f in plan["correspondencia"]}
        pos = {f.get("rol"): n for n, f in enumerate(plan["correspondencia"])}
        self.assertLess(pos["PRD/criterio-de-exito"], pos["DIS/diseno-visual"])
        self.assertLess(pos["DIS/diseno-visual"], pos["CNS/implementacion"])
        self.assertLess(pos["CNS/implementacion"], pos["DIS/revision-de-fidelidad"])
        self.assertLess(pos["DIS/revision-de-fidelidad"], pos["VER/dosier"])
        impl = self.paquete_de(plan, "CNS/implementacion")
        rev_dis = self.paquete_de(plan, "DIS/revision-de-fidelidad")
        self.assertIn(impl, filas[rev_dis]["depende_de"])
        self.assertNotIn(rev_dis, filas[impl]["depende_de"])
        self.assertEqual(tablero.derivar(A, corpus=self.corpus)["dependencias_circulares"], [])
        del rol_de
        # planificar OTRA VEZ el mismo item con el mismo circuito es idempotente (mismos ids)
        segundo = oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=circuito,
                                     control_repo=self.repo, item="enc-ui", titulo="Con pantalla")["plan"]
        self.assertEqual(sorted(segundo["paquetes"]), sorted(plan["paquetes"]))
        # un paquete que ya existe con OTRAS dependencias no se reutiliza en silencio
        from ciclo import durable
        objeto = A._leer_paquete(impl)
        objeto["depende_de"] = sorted(set(objeto["depende_de"]) | {rev_dis})
        durable.escribir(A.almacen, clase="prueba.deps", motivo="dependencias viejas a propósito",
                         objetos={"paquetes/" + impl + ".json": objeto})
        with self.assertRaises(ciclo.PlanificacionInvalida):
            oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=circuito,
                               control_repo=self.repo, item="enc-ui", titulo="Con pantalla")
        # y una generación nueva nace con identidades propias, conservando la anterior
        tercero = oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=circuito,
                                     control_repo=self.repo, item="enc-ui", titulo="Con pantalla",
                                     generacion=1)["plan"]
        self.assertFalse(set(tercero["paquetes"]) & set(plan["paquetes"]))
        self.assertIsNotNone(A._leer_paquete(impl))

    def test_06_el_brief_se_deriva_y_dice_lo_que_el_rol_tiene_que_hacer(self):
        """T463 · Defecto que previene: un agente que trabaja con criterio general."""
        A = self.rt("dsp")
        plan = self.planificar(A)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        brief = oficina.brief_de(A, corpus=self.corpus, paquete=impl, circuito=self.circuito)
        texto = briefs.como_markdown(brief)
        for esperado in ("## 2 · Tu rol", "## 3 · Contrato operativo", "## 4 · Método", "## 5 · Gate",
                         "## 8 · Cómo entregas", "## 9 · Prohibiciones", "## 11 · Prompt operativo",
                         "gate:implementacion-completa", "comprobaciones previas", "checklist",
                         "NO escribes en la rama principal"):
            self.assertIn(esperado, texto)
        self.assertNotIn(self.repo, texto)
        otra = oficina.brief_de(A, corpus=self.corpus, paquete=impl, circuito=self.circuito)
        self.assertEqual(brief["huella"], otra["huella"])


# =========================================================================
# T464–T466 · entregas, autocertificación, devolución y freno
# =========================================================================
class Entregas(Laboratorio):

    def _hasta_impl(self):
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        self.avanzar_prd(A, plan, impl)
        return A, plan, impl

    def test_07_una_entrega_incompleta_se_rechaza_y_no_toca_el_estado(self):
        """T464 · Defecto que previene: «PR #14 sin fusionar» como evidencia de cierre."""
        A, plan, impl = self._hasta_impl()
        self.tomar_y_acusar(A, impl)
        revision = A.almacen.revision()["revision"]
        buena = self.entrega(impl, "CNS/implementacion")
        casos = {
            "gate incompleto": {"autoevaluacion": {"gate": "gate:implementacion-completa",
                                                    "comprobaciones": [{"id": "tests-propios", "resultado": "si"}]}},
            "artefacto obligatorio ausente": {"artefactos": [{"tipo": "pr", "referencia": "#1",
                                                              "descripcion": "sólo la PR"}]},
            "checklist sin contestar": {"autoevaluacion": {"gate": "gate:implementacion-completa",
                                                           "comprobaciones": buena["autoevaluacion"]["comprobaciones"]}},
            "devolución sin los cuatro campos": {"veredicto": "devuelto"},
            "rol equivocado": {"rol": "VER/dosier"},
            "campo desconocido": {"opinion": "me parece bien"},
            "gate de otro rol": {"autoevaluacion": dict(buena["autoevaluacion"], gate="gate:evidencia-suficiente")},
        }
        for nombre, mutacion in casos.items():
            entrega = dict(buena)
            entrega.update(mutacion)
            with self.assertRaises(ciclo.EntregaInvalida, msg=nombre):
                self.entregar(A, impl, entrega)
            self.assertEqual(A.almacen.revision()["revision"], revision, nombre)
        self.assertEqual(A._leer_paquete(impl)["estado"], "ejecutando")

    def test_08_la_autocertificacion_se_rechaza_por_trabajador_y_por_rol(self):
        """T465 · Defecto que previene: el implementador como único verificador de su trabajo."""
        A, plan, impl = self._hasta_impl()
        rev = self.paquete_de(plan, "CNS/revision-de-construccion")
        self.tomar_y_acusar(A, impl)
        self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        # G13 en la PUERTA: quien construyó no llega ni a tomar la revisión, y no deja lease
        with self.assertRaises(ciclo.AutocertificacionRechazada):
            self.tomar_y_acusar(A, rev)
        self.assertIsNone(A._leer_lease(rev))
        self.assertEqual(A._leer_paquete(rev)["estado"], "listo")
        # y aunque tomara por la vía cruda del runtime, la entrega con dictamen se rechaza
        A.tomar(rev)
        for h in oficina.handoffs_pendientes_para(A.almacen, rev):
            oficina.acusar(A, corpus=self.corpus, handoff=h["id"],
                           comprobaciones_superadas=h["comprueba_al_recibir"])
        entrega = self.entrega(rev, "CNS/revision-de-construccion")
        entrega["dictamenes"] = [self.dictamen("gate:implementacion-completa", impl),
                                 self.dictamen("gate:revision-de-construccion", impl)]
        with self.assertRaises(ciclo.AutocertificacionRechazada):
            self.entregar(A, rev, entrega)
        # y un dictamen sobre uno mismo tampoco: lo para el contrato (no_autocertifica) ANTES
        # de que el mecanismo de titulares tenga que intervenir
        entrega["dictamenes"] = [self.dictamen("gate:revision-de-construccion", rev)]
        with self.assertRaises(ciclo.EntregaInvalida):
            self.entregar(A, rev, entrega)
        A.soltar(rev)
        B = self.rt("w-B")
        self.tomar_y_acusar(B, rev)
        entrega["dictamenes"] = [self.dictamen("gate:implementacion-completa", impl),
                                 self.dictamen("gate:revision-de-construccion", impl)]
        res = self.entregar(B, rev, entrega)
        self.assertEqual([d["dictamen"] for d in res["dictamenes"]], ["superado", "superado"])
        ev = oficina.evaluar_terminacion(B, corpus=self.corpus, item="enc-x", circuito=self.circuito,
                                         hechos={"afecta_superficie": False})
        estados = {f["nivel"]: f["estado"] for f in ev["niveles"]}
        self.assertEqual(estados["implementado"], "alcanzado")
        self.assertEqual(estados["revisado"], "alcanzado")
        self.assertEqual(estados["verificado"], "pendiente")
        self.assertEqual(estados["validado-visual"], "inaplicable")
        # un dictamen firmado por el MISMO titular que entregó se publica como RECHAZADO
        forjado = dict(self.corpus.gates()["gate:evidencia-suficiente"], dictamen="superado",
                       gate="gate:evidencia-suficiente", id="dic-forjado", revisor="VER",
                       entrada={"item": "enc-x", "sobre_paquete": impl, "autor_titular": "w-A",
                                "revisor_titular": "w-A"})
        ev = terminacion.evaluar(self.circuito, item="enc-x", paquetes_del_item=plan["paquetes"],
                                 dictamenes=[forjado], hechos={})
        self.assertEqual({f["nivel"]: f["estado"] for f in ev["niveles"]}["verificado"], "rechazado")

    def test_09_devolucion_corrige_reapunta_y_a_la_tercera_frena(self):
        """T466 · Defecto que previene: una capa devuelta que sigue adelante, o un rebote sin fin."""
        A, plan, impl = self._hasta_impl()
        rev = self.paquete_de(plan, "CNS/revision-de-construccion")
        ver = self.paquete_de(plan, "VER/dosier")
        B = self.rt("w-B")
        vueltas = []
        actual_impl, actual_rev = impl, rev
        for vuelta in range(1, 4):
            self.tomar_y_acusar(A, actual_impl)
            self.entregar(A, actual_impl, self.entrega(actual_impl, "CNS/implementacion"))
            self.tomar_y_acusar(B, actual_rev)
            entrega = self.entrega(actual_rev, "CNS/revision-de-construccion", "devuelto")
            entrega["dictamenes"] = [self.dictamen("gate:revision-de-construccion", actual_impl, "no-superado")]
            entrega["devolucion"] = {"que_falta": "la prueba del conflicto no muerde",
                                     "por_que_es_insuficiente": "no protege el cambio",
                                     "que_la_cerraria": "una prueba roja al revertir",
                                     "evidencia": ["tabla de reversión"]}
            try:
                res = self.entregar(B, actual_rev, entrega)
            except ciclo.FrenoDisparado as freno:
                vueltas.append(("freno", freno.contexto.get("devoluciones")))
                break
            # ANTES de cerrar la revisión, VER ya espera al nuevo receptor
            correccion, nuevo = res["correccion"]["correccion"], res["correccion"]["receptor"]
            self.assertIn(nuevo, B._leer_paquete(ver)["depende_de"])
            self.assertNotIn(actual_rev, B._leer_paquete(ver)["depende_de"])
            self.assertEqual(B._leer_paquete(actual_rev)["estado"], "completado")
            self.assertEqual([t["paquete"] for t in A.tomables()["tomables"]], [correccion])
            vueltas.append(("devuelto", vuelta))
            actual_impl, actual_rev = correccion, nuevo
        self.assertEqual([v[0] for v in vueltas], ["devuelto", "devuelto", "freno"])
        escalados = [c for c in oficina.cierres_de_item(A.almacen, "enc-x") if c["salida"] == "escalado"]
        self.assertEqual(len(escalados), 1)
        self.assertEqual(escalados[0]["autoridad"], "OWNER")
        self.assertEqual(len(escalados[0]["posturas"]), 2)
        vista = tablero.derivar(A, corpus=self.corpus)
        self.assertEqual(len(vista["devoluciones"]), 3)       # la tercera se registra, y frena
        self.assertEqual(len(vista["escalados"]), 1)

    def test_10_un_rechazo_al_recibir_no_cuenta_para_el_freno_y_cancela_el_receptor(self):
        """T466 · Defecto que previene: aceptar por cortesía y devolver después."""
        A, plan, impl = self._hasta_impl()
        rev = self.paquete_de(plan, "CNS/revision-de-construccion")
        self.tomar_y_acusar(A, impl)
        self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        B = self.rt("w-B")
        toma = oficina.tomar(B, corpus=self.corpus, paquete=rev, circuito=self.circuito)
        handoff = toma["brief"]["recibes"][0]
        res = oficina.rechazar(B, corpus=self.corpus, handoff=handoff["id"],
                               motivo="el commit nombrado no existe", paquete_receptor=rev)
        self.assertEqual(res["handoff"]["estado"], "rechazado")
        self.assertFalse(res["handoff"]["cuenta_para_el_freno"])
        self.assertEqual(B._leer_paquete(rev)["estado"], "cancelado")
        self.assertEqual([t["paquete"] for t in A.tomables()["tomables"]], [res["correccion"]])
        with self.assertRaises(ciclo.HandoffRechazado):
            oficina.acusar(B, corpus=self.corpus, handoff=handoff["id"], comprobaciones_superadas=[])


# =========================================================================
# T467–T468 · bloqueo sin intento, niveles y cierre
# =========================================================================
class BloqueoYCierre(Laboratorio):

    def test_11_un_bloqueo_no_consume_intento_y_deja_el_desbloqueador_nombrado(self):
        """T467 · Defecto que previene: un bloqueo que acaba en `agotado` y en g.9."""
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        self.avanzar_prd(A, plan, impl)
        self.tomar_y_acusar(A, impl)
        entrega = self.entrega(impl, "CNS/implementacion", "bloqueado")
        entrega["bloqueo"] = {"que_lo_impide": "no hay acceso a la fuente backend",
                              "que_lo_desbloquearia": "materializar la fuente en el workspace",
                              "autoridad": "PLT"}
        res = self.entregar(A, impl, entrega)
        paquete = A._leer_paquete(impl)
        self.assertEqual(paquete["estado"], "bloqueado")
        self.assertEqual(paquete["intentos"], 1)
        self.assertIsNone(A._leer_lease(impl))
        self.assertEqual(res["cierre"]["salida"], "bloqueado")
        self.assertIn("materializar", res["cierre"]["trabajo_de_reemplazo"])
        self.assertEqual(A.almacen.reconciliacion_pendiente(), [])
        vista = tablero.derivar(A, corpus=self.corpus)
        self.assertTrue(any(e["paquete"] == impl and e["por_que"].startswith("bloqueado")
                            for e in vista["esperando"]))
        self.assertIn("bloqueado", vista["que_hara_el_sistema_si_nadie_dice_nada"])
        # se desbloquea con la autoridad, y se vuelve a tomar reanudando el checkpoint
        A.reanudar(impl, motivo="fuente materializada", autoridad="PLT")
        toma = A.tomar(impl)
        self.assertEqual(toma["intento"], 2)
        self.assertEqual(toma["checkpoint"]["contenido"]["bloqueo"]["autoridad"], "PLT")

    def test_12_el_item_no_cierra_como_producto_hasta_alcanzar_los_niveles_exigidos(self):
        """T468 · Defecto que previene: «cerrado» mientras nadie abrió la pantalla."""
        A = self.rt("w-A")
        B = self.rt("w-B")
        C = self.rt("w-C")
        plan = self.planificar(A)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        rev = self.paquete_de(plan, "CNS/revision-de-construccion")
        ver = self.paquete_de(plan, "VER/dosier")
        self.avanzar_prd(A, plan, impl)
        self.tomar_y_acusar(A, impl)
        self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        self.tomar_y_acusar(B, rev)
        e = self.entrega(rev, "CNS/revision-de-construccion")
        e["dictamenes"] = [self.dictamen("gate:implementacion-completa", impl),
                           self.dictamen("gate:revision-de-construccion", impl)]
        self.entregar(B, rev, e)
        hechos = {"afecta_superficie": False}
        with self.assertRaises(ciclo.CircuitoBaseIncumplido) as cm:
            oficina.cerrar_item(A, corpus=self.corpus, item="enc-x", circuito=self.circuito, hechos=hechos,
                                integracion={"propietario_global": "PRD", "declaracion": "x"},
                                aprendizaje="none")
        self.assertIn("verificado", cm.exception.contexto["faltan"])
        self.assertIn("aceptado", cm.exception.contexto["faltan"])
        self.tomar_y_acusar(C, ver)
        e = self.entrega(ver, "VER/dosier")
        e["dictamenes"] = [self.dictamen("gate:evidencia-suficiente", impl)]
        self.entregar(C, ver, e)
        # el resto del plan (la integración semántica de PRD) lo entrega A
        for _ in range(4):
            tomables = [t["paquete"] for t in A.tomables()["tomables"]]
            if not tomables:
                break
            pq = tomables[0]
            self.tomar_y_acusar(A, pq)
            self.entregar(A, pq, self.entrega(pq, self.filas(plan)[pq]["rol"]))
        with self.assertRaises(ciclo.CircuitoBaseIncumplido) as cm:
            oficina.cerrar_item(A, corpus=self.corpus, item="enc-x", circuito=self.circuito, hechos=hechos,
                                integracion={"propietario_global": "PRD", "declaracion": "x"},
                                aprendizaje="none")
        self.assertEqual(cm.exception.contexto["faltan"], ["aceptado"])
        # el Owner acepta: el gate lo firma OWNER y nadie más
        gate = self.corpus.gates()["gate:aceptacion-del-owner"]
        dictamen = oficina.aceptar(A, corpus=self.corpus, item="enc-x",
                                   comprobaciones_superadas=[c["id"] for c in gate["comprobaciones"]],
                                   evidencia=list(gate["evidencia"]))
        self.assertEqual(dictamen["dictamen"], "superado")
        self.assertEqual(dictamen["revisor"], "OWNER")
        res = oficina.cerrar_item(A, corpus=self.corpus, item="enc-x", circuito=self.circuito, hechos=hechos,
                                  integracion={"propietario_global": "PRD", "declaracion": "integrado"},
                                  aprendizaje="none")
        self.assertEqual(res["cierre"]["salida"], "completado")
        self.assertEqual(res["cierre"]["informe"]["huerfanas"], [])
        ev = oficina.evaluar_terminacion(A, corpus=self.corpus, item="enc-x", circuito=self.circuito, hechos=hechos)
        self.assertEqual({f["nivel"]: f["estado"] for f in ev["niveles"]}["cerrado"], "alcanzado")
        # sin el hecho, validado-visual NO es inaplicable y el cierre se habría negado
        ev = oficina.evaluar_terminacion(A, corpus=self.corpus, item="enc-x", circuito=self.circuito, hechos={})
        self.assertIn("validado-visual", ev["faltan"])


# =========================================================================
# T469–T470 · tablero, agente sin chat y supervisor
# =========================================================================
class TableroYSupervisor(Laboratorio):

    def test_13_el_tablero_es_determinista_y_dice_que_hara_el_sistema(self):
        """T469 · Defecto que previene: reconstruir la organización leyendo veinte JSON."""
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        primera = tablero.derivar(A, corpus=self.corpus)
        segunda = tablero.derivar(A, corpus=self.corpus)
        self.assertEqual(json.dumps(primera, sort_keys=True), json.dumps(segunda, sort_keys=True))
        self.assertEqual(len(primera["items"]), 1)
        self.assertEqual(primera["items"][0]["proceso"], "proceso:FEA")
        self.assertEqual(len(primera["tomables"]), 1)
        self.assertIn("tomar y trabajar", primera["que_hara_el_sistema_si_nadie_dice_nada"])
        self.assertTrue(all(e["por_que"].startswith("espera a") for e in primera["esperando"]))
        texto = tablero.como_texto(primera)
        self.assertIn("SI NADIE DICE NADA", texto)
        self.assertNotIn(self.repo, texto)
        A.cerrar()
        proceso = self.cli("tablero")
        self.assertEqual(proceso.returncode, 0, proceso.stderr)
        self.assertEqual(json.loads(proceso.stdout)["tomables"], primera["tomables"])

    def test_14_un_agente_sin_chat_ejecuta_un_paquete_con_su_brief_y_el_supervisor_cierra_la_oficina(self):
        """T470 · Defecto que previene: «no existe ningún adaptador de proveedor»."""
        espacio = os.path.join(self.repo, "espacio-agente")
        registro = adaptadores.RegistroDeAdaptadores([adaptadores.AdaptadorDeAgente(
            espacio, adaptadores.cargar_ejecutores(self.repo, corpus=self.corpus), repo=self.repo)])
        S = self.rt("supervisor", registro)

        def ordenes(capacidad, rol):
            if rol == "CNS/implementacion":
                return {"adaptador": "agente", "operacion": "ejecutar",
                        "argumentos": ["modelo:alfa", "<paquete>"], "limite_segundos": 60}
            return paquete_runtime.orden_externa(argumentos=[capacidad, rol or ""])

        plan = self.planificar(S, ordenes=ordenes)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        # la orden del agente nombra su paquete: se reescribe con el id real
        objeto = S._leer_paquete(impl)
        objeto["orden"]["argumentos"][1] = impl
        from ciclo import durable
        durable.escribir(S.almacen, clase="prueba.orden", motivo="nombrar el paquete en su orden",
                         objetos={"paquetes/" + impl + ".json": objeto})
        self.avanzar_prd(S, plan, impl)

        def brief_de(paquete):
            brief = oficina.brief_de(S, corpus=self.corpus, paquete=paquete, circuito=self.circuito)
            return brief, briefs.como_markdown(brief)

        def tras(paquete):
            return oficina.registrar_entrega_de_agente(S, corpus=self.corpus, paquete=paquete,
                                                       circuito=self.circuito)

        sup = modulo_supervisor.Supervisor(S, corpus=self.corpus, adaptador_de_agente=registro.seleccionar(["agente"]),
                                           brief_de=brief_de, tras_completar=tras, reloj=lambda s: None)
        resultado = sup.bucle(pasadas=3)
        atendidos = [a for p in resultado["pasadas"] for a in p["atendidos"]]
        self.assertEqual([(a["paquete"], a["desenlace"]) for a in atendidos], [(impl, "completado")])
        self.assertTrue(os.path.isfile(os.path.join(espacio, "briefs", impl + ".md")))
        registrada = entregas.ultima(S.almacen, impl)
        self.assertEqual(registrada["veredicto"], "entregado")
        self.assertEqual(registrada["rol"], "CNS/implementacion")
        self.assertIn("CNS/implementacion", json.loads(S._leer_paquete(impl)["resultado"]["salida"])["rol"])
        # la oficina emitió el handoff a la revisión, que es externa y ahora es tomable
        rev = self.paquete_de(plan, "CNS/revision-de-construccion")
        self.assertEqual([t["paquete"] for t in S.tomables()["tomables"]], [rev])
        self.assertTrue(oficina.handoffs_pendientes_para(S.almacen, rev))
        # con la revisión en manos externas el supervisor sigue observando hasta agotar las
        # pasadas: `todo-en-manos-ajenas` no es una parada legítima, es una espera
        self.assertEqual(resultado["parada"], "pasadas-agotadas")
        self.assertEqual(resultado["pasadas"][-1]["parada"], "todo-en-manos-ajenas")
        # repetir la pasada NO vuelve a ejecutar ni a registrar
        segunda = sup.pasada()
        self.assertEqual(segunda["atendidos"], [])
        self.assertEqual(entregas.ultima(S.almacen, impl)["id"], registrada["id"])

    def test_15_sin_entrega_valida_el_agente_no_completa_y_sin_ejecutor_falla_cerrado(self):
        """T470 · Defecto que previene: un `completado` durable sobre una entrega que no existe."""
        espacio = os.path.join(self.repo, "espacio-agente")
        ejecutores = adaptadores.cargar_ejecutores(self.repo, corpus=self.corpus)
        roto = dict(ejecutores["modelo:beta"])
        roto["argv"] = [sys.executable, "-c", "import sys; sys.exit(0)", "{brief}", "{entrega}"]
        adaptador = adaptadores.AdaptadorDeAgente(espacio, {"modelo:beta": roto}, repo=self.repo)
        adaptador.escribir_brief("pq-z", "# brief\n", {"paquete": "pq-z"})
        resultado = adaptador.ejecutar({"adaptador": "agente", "operacion": "ejecutar",
                                        "argumentos": ["modelo:beta", "pq-z"], "limite_segundos": 30},
                                       efecto="ef-000000000001", limite_segundos=30)
        self.assertEqual(resultado["estado"], "fallido")
        self.assertTrue(resultado["reintentable"])
        self.assertIn("NO dejó entrega", resultado["detalle"])
        resultado = adaptador.ejecutar({"adaptador": "agente", "operacion": "ejecutar",
                                        "argumentos": ["modelo:inexistente", "pq-z"], "limite_segundos": 30},
                                       efecto="ef-000000000002", limite_segundos=30)
        self.assertEqual(resultado["estado"], "fallido")
        self.assertFalse(resultado["reintentable"])
        with self.assertRaises(adaptadores.OrdenInvalida):
            adaptadores.AdaptadorDeAgente(espacio, {}, repo=self.repo)
        with self.assertRaises(adaptadores.OrdenInvalida):
            adaptadores.ejecutores_desde_texto("```yaml ads:ejecutor\nid: ejecutor:x\nmodelo: modelo:alfa\n"
                                               "argv: [echo]\nlimite_segundos: 5\n```\n", corpus=self.corpus)


# =========================================================================
# T471–T475 · adversarial: circularidad, handoff incompleto, Owner ausente, reinicio, documentos
# =========================================================================
class Adversarial(Laboratorio):

    def test_16_una_dependencia_circular_no_se_toma_y_el_tablero_la_nombra(self):
        """T471 · Defecto que previene: dos paquetes esperándose para siempre en silencio."""
        A = self.rt("w-A")
        A.crear_item(id="it-1", titulo="primero", motivo="alta")
        A.crear_paquete(id="pq-a", item="it-1", capacidades_requeridas=["worker"],
                        orden=paquete_runtime.orden_externa(), depende_de=[])
        A.crear_paquete(id="pq-b", item="it-1", capacidades_requeridas=["worker"],
                        orden=paquete_runtime.orden_externa(), depende_de=["pq-a"])
        from ciclo import durable
        objeto = A._leer_paquete("pq-a")
        objeto["depende_de"] = ["pq-b"]
        durable.escribir(A.almacen, clase="prueba.ciclo", motivo="cerrar el ciclo a propósito",
                         objetos={"paquetes/pq-a.json": objeto})
        self.assertEqual(A.tomables()["tomables"], [])
        vista = tablero.derivar(A, corpus=self.corpus)
        self.assertEqual(sorted(vista["dependencias_circulares"]), ["pq-a", "pq-b"])
        self.assertIn("circular", vista["que_hara_el_sistema_si_nadie_dice_nada"])
        S = modulo_supervisor.Supervisor(A, corpus=self.corpus, reloj=lambda s: None)
        self.assertEqual(S.bucle(pasadas=2)["parada"], "bloqueado")

    def test_17_un_handoff_incompleto_no_se_emite_y_un_acuse_a_medias_no_toma_custodia(self):
        """T472 · Defecto que previene: «el trabajo hecho» como entrega."""
        from ciclo import handoffs
        with self.assertRaises(ciclo.HandoffIncompleto):
            handoffs.emitir("handoff:con-a-ver", artefactos=[], checkpoint="x",
                            trazabilidad={"item": "i", "paquete": "p", "ruta": "r"}, corpus=self.corpus)
        with self.assertRaises(ciclo.HandoffIncompleto):
            handoffs.emitir("handoff:con-a-ver", artefactos=["commit:abc"], checkpoint="x",
                            trazabilidad={"item": "i", "paquete": "p"}, corpus=self.corpus)
        entrega = handoffs.emitir("handoff:con-a-ver", artefactos=["commit:abc"], checkpoint="x",
                                  trazabilidad={"item": "i", "paquete": "p", "ruta": "r"}, corpus=self.corpus)
        with self.assertRaises(ciclo.HandoffRechazado):
            handoffs.acusar(entrega, comprobaciones_superadas=entrega["comprueba_al_recibir"][:1],
                            receptor="VER")
        with self.assertRaises(ciclo.HandoffRechazado):
            handoffs.acusar(entrega, comprobaciones_superadas=entrega["comprueba_al_recibir"],
                            receptor="CNS")
        generica = handoffs.generica("PRD", "CNS", corpus=self.corpus)
        self.assertEqual(generica["de"], "PRD")
        self.assertTrue(generica["comprueba_al_recibir"])

    def test_18_con_el_owner_ausente_el_trabajo_independiente_continua(self):
        """T473 · Defecto que previene: parar la oficina entera por una decisión pendiente."""
        A = self.rt("w-A")
        plan_x = self.planificar(A, item="enc-x")["plan"]
        plan_y = self.planificar(A, item="enc-y")["plan"]
        # el item X queda ESCALADO al Owner; el Y sigue
        impl_x = self.paquete_de(plan_x, "CNS/implementacion")
        self.avanzar_prd(A, plan_x, impl_x)
        self.tomar_y_acusar(A, impl_x)
        entrega = self.entrega(impl_x, "CNS/implementacion", "escalado")
        entrega["bloqueo"] = {"que_lo_impide": "el criterio de éxito exige una decisión de alcance",
                              "que_lo_desbloquearia": "que el Owner elija entre las dos opciones",
                              "autoridad": "OWNER", "posturas": ["A: exportar todo", "B: exportar filtrado"]}
        self.entregar(A, impl_x, entrega)
        vista = tablero.derivar(A, corpus=self.corpus)
        self.assertEqual([e["item"] for e in vista["escalados"]], ["enc-x"])
        tomables = [t["paquete"] for t in A.tomables()["tomables"]]
        self.assertTrue(tomables)
        self.assertTrue(all(A._leer_paquete(p)["item"] == "enc-y" for p in tomables))
        self.assertIn("tomar y trabajar", vista["que_hara_el_sistema_si_nadie_dice_nada"])

    def test_19_un_reinicio_completo_reconstruye_exactamente_lo_mismo(self):
        """T474 · Defecto que previene: continuidad que vive en la conversación."""
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        self.avanzar_prd(A, plan, impl)
        self.tomar_y_acusar(A, impl)
        A.checkpoint(impl, {"paso": 3, "ficheros": ["a.php"]})
        antes = tablero.derivar(A, corpus=self.corpus)
        from ciclo import cli_oficina
        brief_antes = oficina.brief_de(A, corpus=self.corpus, paquete=impl, circuito=self.circuito,
                                       ordenes=cli_oficina._ordenes_del_brief(None))
        A.cerrar()
        # OTRO proceso, sin memoria de éste: la CLI abre el mismo control repo desde cero
        proceso = self.cli("tablero", instancia="w-A")
        self.assertEqual(proceso.returncode, 0, proceso.stderr)
        despues = json.loads(proceso.stdout)
        for clave in ("items", "paquetes", "por_estado", "tomables", "esperando", "equipos",
                      "handoffs_pendientes_de_acuse", "que_hara_el_sistema_si_nadie_dice_nada"):
            self.assertEqual(json.dumps(antes[clave], sort_keys=True), json.dumps(despues[clave], sort_keys=True), clave)
        proceso = self.cli("brief", "--paquete", impl, "--clase-de-trabajo", "cambio-de-backend",
                           instancia="lector-nuevo")
        self.assertEqual(proceso.returncode, 0, proceso.stderr)
        self.assertEqual(json.loads(proceso.stdout)["huella"], brief_antes["huella"])
        self.assertEqual(json.loads(proceso.stdout)["checkpoint"]["contenido"]["paso"], 3)
        # el trabajador vuelve con su MISMA instancia y sigue siendo el titular
        A2 = self.rt("w-A")
        toma = A2.tomar(impl)
        self.assertEqual(toma["intento"], 1)
        self.assertEqual(toma["checkpoint"]["contenido"]["paso"], 3)

    def test_20_los_documentos_inconsistentes_se_rechazan_con_su_nombre(self):
        """T475 · Defecto que previene: un circuito, una entrega o un PROFILE que dicen dos cosas."""
        with self.assertRaises(ciclo.CircuitoBaseIlegible):
            terminacion.circuitos_base_desde_texto(CIRCUITO_BACKEND.replace(
                "niveles_obligatorios: [implementado, revisado, verificado, validado-visual, aceptado]",
                "niveles_obligatorios: [implementado]"), corpus=self.corpus)
        with self.assertRaises(ciclo.CircuitoBaseIlegible):
            terminacion.circuitos_base_desde_texto(CIRCUITO_BACKEND.replace(
                "condicion: afecta_superficie es-falso", "condicion: si no hace falta"), corpus=self.corpus)
        with self.assertRaises(ciclo.CircuitoBaseIlegible):
            terminacion.circuitos_base_desde_texto(CIRCUITO_BACKEND.replace(
                "roles_minimos: [CNS/implementacion, CNS/revision-de-construccion, VER/dosier]",
                "roles_minimos: [CNS/inventado]"), corpus=self.corpus)
        vacio = tempfile.mkdtemp(prefix="ads-sin-perfil-")
        self.addCleanup(shutil.rmtree, vacio, True)
        with self.assertRaises(ciclo.CircuitoBaseIlegible):
            terminacion.cargar_circuitos_base(vacio, corpus=self.corpus)
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        rev = self.paquete_de(plan, "CNS/revision-de-construccion")
        self.avanzar_prd(A, plan, impl)
        self.tomar_y_acusar(A, impl)
        self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        B = self.rt("w-B")
        self.tomar_y_acusar(B, rev)
        # dice «entregado» y su dictamen es no-superado: las dos cosas no pueden ser ciertas
        entrega = self.entrega(rev, "CNS/revision-de-construccion")
        entrega["dictamenes"] = [self.dictamen("gate:revision-de-construccion", impl, "no-superado")]
        with self.assertRaises(ciclo.EntregaInvalida):
            self.entregar(B, rev, entrega)
        # declara superado y el gate recorrido dice lo contrario
        entrega["dictamenes"] = [dict(self.dictamen("gate:revision-de-construccion", impl, "no-superado"),
                                      dictamen="superado")]
        with self.assertRaises(ciclo.EntregaInvalida):
            self.entregar(B, rev, entrega)
        self.assertEqual(B._leer_paquete(rev)["estado"], "ejecutando")


# =========================================================================
# T476 · el contrato efectivo de un rol sin contrato completo
# =========================================================================
class ContratosEfectivos(Laboratorio):

    def test_21_un_rol_sin_contrato_completo_tiene_contrato_efectivo_que_manda_en_el_brief(self):
        """T476 · Defecto que previene: treinta roles trabajando con prosa y criterio propio."""
        from ciclo import contratos
        clases = contratos.clasificar(self.corpus)
        self.assertEqual({c for c in clases.values()} - {"materializable", "consultivo", "conceptual"}, set())
        for rol, clase in clases.items():
            if clase != "conceptual":
                self.assertEqual(contratos.fallos_del_contrato(self.corpus, rol), [], rol)
        # ARQ/diagnostico no tiene contrato completo: el efectivo es base + derivación
        contrato = self.corpus.contrato_operativo_de("ARQ/diagnostico")
        self.assertEqual(contrato["rol"], "ARQ/diagnostico")
        self.assertIn("gate:plan-tecnico", contrato["no_autocertifica"])
        self.assertEqual(contrato["metodos"], ["ARQ/Diagnostico"])
        self.assertTrue(any(c["id"] == "acuse-antes" for c in contrato["checklist"]))
        self.assertTrue(any(c["id"] == "entradas-localizables" for c in contrato["comprobaciones_previas"]))
        self.assertEqual(contrato["secuencia"][0]["n"], 1)
        self.assertIn("Acusar o rechazar", contrato["secuencia"][0]["hace"])
        self.assertEqual(contrato["entrega_a"], ["segun-el-plan"])
        self.assertTrue(contrato["decisiones_propias"])
        # el mismo rol con contrato completo devuelve el completo, no la fusión
        completo = self.corpus.contrato_operativo_de("CNS/implementacion")
        self.assertEqual(completo["id"], "contrato:con-implementacion")
        # y ningún rol conceptual se inventa un contrato
        self.assertIsNone(self.corpus.contrato_operativo_de("ENC/interlocutor"))
        # no_autocertifica MUERDE en la entrega: un dictamen del gate propio sobre el propio paquete
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        self.avanzar_prd(A, plan, impl)
        self.tomar_y_acusar(A, impl)
        entrega = self.entrega(impl, "CNS/implementacion")
        entrega["dictamenes"] = [self.dictamen("gate:implementacion-completa", impl)]
        with self.assertRaises(ciclo.EntregaInvalida) as cm:
            self.entregar(A, impl, entrega)
        self.assertIn("no_autocertifica", str(cm.exception))


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen (salida publicada)."""

    def run(self, test):
        buffer = io.StringIO()
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
