#!/usr/bin/env python3
"""test_oficina — `T460`–`T486`: el protocolo de trabajadores, la entrega, los niveles, el supervisor, los handoffs de §78 y las fronteras de §77.

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
from unittest.mock import patch

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
from ciclo import agentes, briefs, entregas, gates, oficina, tablero, terminacion  # noqa: E402
from runtime import supervisor as modulo_supervisor                  # noqa: E402
import catalogo_de_prueba                                            # noqa: E402

ENTORNO = {k: v for k, v in os.environ.items()
           if k not in ("ADS_RUNTIME_FALLO", "ADS_ESTADO_FALLO", "ADS_ADAPTADOR_FALLO")}

CIRCUITO_FUNDACION_VISUAL = '''
```yaml ads:circuito-base
id: circuito:fundacion-visual
nombre: Fundación visual (laboratorio de T506)
clase_de_trabajo: fundacion-visual
cuando_aplica: laboratorio para medir el orden entre roles de Diseño que pueden compartir agente
materia: capacidad-ausente
estado_del_objeto: no-existe
condiciones_de_ruta: [C-DIS, C-ENT]
composiciones: [composicion:prd-alcance-rutinario, composicion:dis-feature-visual, composicion:con-implementacion, composicion:ver-dosier, composicion:ent-convergencia]
niveles_obligatorios: [implementado, revisado, integrado, verificado, validado-visual, aceptado]
inaplicabilidad:
  - nivel: integrado
    condicion: fuentes_escritas_cuenta == 0
    quien_lo_declara: la instancia, derivándolo de las fuentes que el item escribe
roles_minimos: [DIS/diseno-visual, DIS/prototipado, CNS/implementacion, VER/dosier, ENT/convergencia]
independencias:
  - rol: CNS/revision-de-construccion
    de: [CNS/implementacion]
gates_de_cierre: [gate:cierre-de-item]
```
'''

CIRCUITO_INTERFAZ = '''
```yaml ads:circuito-base
id: circuito:cambio-con-interfaz
nombre: Cambio con interfaz
clase_de_trabajo: cambio-con-interfaz
cuando_aplica: el item escribe en una fuente con pantalla y el usuario ve algo distinto
materia: capacidad-ausente
estado_del_objeto: no-existe
condiciones_de_ruta: [C-DIS, C-ENT]
composiciones: [composicion:prd-alcance-rutinario, composicion:dis-extension-de-patron, composicion:con-implementacion, composicion:ver-dosier, composicion:ent-convergencia]
niveles_obligatorios: [implementado, revisado, integrado, verificado, validado-visual, aceptado]
inaplicabilidad:
  - nivel: integrado
    condicion: fuentes_escritas_cuenta == 0
    quien_lo_declara: la instancia, derivándolo de las fuentes que el item escribe
roles_minimos: [DIS/diseno-visual, DIS/revision-de-fidelidad, CNS/implementacion, CNS/revision-de-construccion, VER/dosier, ENT/convergencia]
independencias:
  - rol: CNS/revision-de-construccion
    de: [CNS/implementacion]
  - rol: DIS/revision-de-fidelidad
    de: [CNS/implementacion, DIS/diseno-visual]
  - rol: ENT/convergencia
    de: [CNS/implementacion]
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

CIRCUITO_DOMINIO = '''
```yaml ads:circuito-base
id: circuito:cambio-de-dominio
nombre: Cambio de dominio
clase_de_trabajo: cambio-de-dominio
cuando_aplica: el modelo de dominio cambia y hay migración de datos
materia: capacidad-ausente
estado_del_objeto: no-existe
condiciones_de_ruta: [C-DOM]
composiciones: [composicion:prd-alcance-rutinario, composicion:dom-migracion, composicion:con-implementacion, composicion:ver-dosier]
niveles_obligatorios: [implementado, revisado, verificado, aceptado]
inaplicabilidad: []
roles_minimos: [DOM/modelo, DOM/migracion, CNS/implementacion, CNS/revision-de-construccion, VER/dosier]
independencias:
  - rol: CNS/revision-de-construccion
    de: [CNS/implementacion]
  - rol: DOM/migracion
    de: [DOM/modelo]
gates_de_cierre: [gate:cierre-de-item]
```
'''

CIRCUITO_DIRECCION = '''
```yaml ads:circuito-base
id: circuito:cambio-de-direccion
nombre: Cambio de dirección
clase_de_trabajo: cambio-de-direccion
cuando_aplica: el Owner sustituye una dirección ya decidida; no se construye nada
materia: direccion-ya-decidida
estado_del_objeto: existe
condiciones_de_ruta: []
composiciones: [composicion:prd-direccion-nueva, composicion:arq-plan-completo, composicion:ver-decision, composicion:dsp-supervisor]
niveles_obligatorios: [aceptado]
inaplicabilidad: []
roles_minimos: [PRD/definicion, ARQ/encaje, VER/decision, DSP/enrutamiento]
independencias:
  - rol: VER/decision
    de: [ARQ/encaje]
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
        perfil = catalogo_de_prueba.texto(self.politica, self.corpus) + CIRCUITO_BACKEND + CIRCUITO_INTERFAZ + CIRCUITO_DOMINIO + CIRCUITO_DIRECCION + CIRCUITO_FUNDACION_VISUAL
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
                               for t in ("commit", "rama", "pr", "salida-de-orden", "dosier", "medicion",
                                         "documento", "captura")],
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

    def test_03b_un_trabajador_que_entrega_mientras_el_supervisor_observa_no_tumba_el_barrido(self):
        """T461 · Defecto que previene: el supervisor muerto por una carrera, y nadie reofreciendo.

        Medido en el dogfood con workers reales: el lease existía al listar, el trabajador
        entregó antes de observarlo, `observar` levantó RUNTIME_INCONSISTENTE y el
        supervisor murió en su primera pasada; todo quedó esperando a un lease muerto.
        """
        A = self.rt("w-A")
        A.crear_item(id="it-1", titulo="primero", motivo="alta")
        A.crear_paquete(id="pq-1", item="it-1", capacidades_requeridas=["worker"],
                        orden=paquete_runtime.orden_externa())
        A.tomar("pq-1")
        S = self.rt("supervisor")
        original = S.observar

        def carrera(paquete):
            # el trabajador entrega JUSTO antes de que el supervisor observe su lease
            A.entregar("pq-1", {"estado": "completado", "codigo": 0, "salida": "ok", "detalle": "",
                                "reintentable": False})
            return original(paquete)

        S.observar = carrera
        informe = S.ciclo()
        self.assertEqual(S._leer_paquete("pq-1")["estado"], "completado")
        self.assertNotIn("pq-1", informe["reofrecidos"])
        self.assertEqual(informe["atendidos"], [])
        # y sin carrera, el mismo barrido sigue observando y reofreciendo como siempre
        S.observar = original
        A.crear_paquete(id="pq-2", item="it-1", capacidades_requeridas=["worker"],
                        orden=paquete_runtime.orden_externa())
        A.tomar("pq-2")
        reofrecido = None
        for pasada in range(S.paciencia + 1):
            if "pq-2" in S.ciclo()["reofrecidos"]:
                reofrecido = pasada
                break
        self.assertEqual(reofrecido, S.paciencia)

    def test_03c_un_lector_detras_de_un_escritor_no_ve_corrupcion(self):
        """T474 · Defecto que previene: un worker que lee mientras otro publica muere por «estado corrupto».

        Medido con tres workers reales: entre leer REVISION.json y leer el objeto, otro
        proceso publicó los dos; el lector juzgaba el objeto nuevo contra la revisión vieja y
        levantaba ESTADO_CORRUPTO. Se reproduce sirviéndole al lector una revisión rancia.
        """
        A = self.rt("w-A")
        A.crear_item(id="it-1", titulo="primero", motivo="alta")
        A.crear_paquete(id="pq-1", item="it-1", capacidades_requeridas=["worker"],
                        orden=paquete_runtime.orden_externa())
        L = self.rt("lector")
        almacen = L.almacen
        rancia = almacen._leer_revision()
        A.tomar("pq-1")                                    # el escritor publica: el objeto cambia
        original = almacen._leer_revision
        servida = {"veces": 0}

        def primero_rancia():
            servida["veces"] += 1
            return rancia if servida["veces"] == 1 else original()

        almacen._leer_revision = primero_rancia
        objeto = almacen.leer("paquetes/pq-1.json")       # no levanta: la revisión avanzó
        self.assertEqual(objeto["estado"], "ejecutando")
        almacen._leer_revision = original
        # y un objeto de verdad corrupto sigue siendo corrupción: fallo cerrado
        ruta = os.path.join(self.repo, "estado", "canonico", "paquetes", "pq-1.json")
        with open(ruta, "a", encoding="utf-8") as fichero:
            fichero.write(" ")
        with self.assertRaises(Exception) as cm:
            almacen.leer("paquetes/pq-1.json")
        self.assertIn("ESTADO_CORRUPTO", str(cm.exception))

    def test_03d_un_lease_que_otro_libero_entre_dos_lecturas_no_es_corrupcion(self):
        """T474 · Defecto que previene: el supervisor muere por «el fichero no existe» cuando un worker suelta.

        Medido con un supervisor y tres workers como procesos: la revisión leída nombraba el
        lease, el titular lo liberó y publicó, y el lector encontraba el fichero ausente.
        """
        A = self.rt("w-A")
        A.crear_item(id="it-1", titulo="primero", motivo="alta")
        A.crear_paquete(id="pq-1", item="it-1", capacidades_requeridas=["worker"],
                        orden=paquete_runtime.orden_externa())
        A.tomar("pq-1")
        L = self.rt("lector")
        almacen = L.almacen
        rancia = almacen._leer_revision()                  # nombra leases/pq-1.json
        A.soltar("pq-1")                                   # el titular lo retira y publica
        original = almacen._leer_revision
        servida = {"veces": 0}

        def primero_rancia():
            servida["veces"] += 1
            return rancia if servida["veces"] == 1 else original()

        almacen._leer_revision = primero_rancia
        with self.assertRaises(Exception) as cm:
            almacen.leer("leases/pq-1.json")
        self.assertIn("RUTA_INVALIDA", str(cm.exception))   # «no existe», no «corrupto»
        almacen._leer_revision = primero_rancia
        servida["veces"] = 0
        self.assertIsNone(L._leer_lease("pq-1"))            # y el lector opcional lo lee como «sin lease»
        almacen._leer_revision = original
        # un fichero que falta SIN que la revisión avance sigue siendo corrupción
        ruta = os.path.join(self.repo, "estado", "canonico", "paquetes", "pq-1.json")
        os.remove(ruta)
        with self.assertRaises(Exception) as cm:
            almacen.leer("paquetes/pq-1.json")
        self.assertIn("ESTADO_CORRUPTO", str(cm.exception))

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
        self.assertLess(pos["VER/dosier"], pos["ENT/convergencia"])
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

    def test_07b_sin_lease_no_se_escribe_ni_el_primer_paso_de_la_entrega(self):
        """T461 · Defecto que previene: media entrega escrita por quien ya no tiene la autoridad.

        Medido en el sexto dogfood: el supervisor reclamó el lease de un worker vivo pero lento
        (el latido se paró al acabar el ejecutable y la entrega tardó más que la paciencia);
        el worker escribió dictamen, devolución y corrección antes de que la publicación le
        dijera AUTORIDAD_PERDIDA.
        """
        A, plan, impl = self._hasta_impl()
        rev = self.paquete_de(plan, "CNS/revision-de-construccion")
        self.tomar_y_acusar(A, impl)
        self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        B = self.rt("w-B")
        self.tomar_y_acusar(B, rev)
        S = self.rt("supervisor")
        for _ in range(S.paciencia):                      # B no late: el supervisor lo reclama
            S.observar(rev)
        S.reclamar(rev)
        S.soltar(rev)
        self.assertIsNone(S._leer_lease(rev))
        antes = sorted(B.almacen.listar("paquetes")), sorted(B.almacen.listar("dictamenes")), sorted(B.almacen.listar("handoffs"))
        entrega = self.entrega(rev, "CNS/revision-de-construccion", "devuelto")
        entrega["dictamenes"] = [self.dictamen("gate:revision-de-construccion", impl, "no-superado")]
        entrega["devolucion"] = {"que_falta": "la prueba del conflicto no muerde",
                                 "por_que_es_insuficiente": "no protege el cambio",
                                 "que_la_cerraria": "una prueba roja al revertir",
                                 "evidencia": ["tabla de reversión"]}
        from runtime.errores import AutoridadPerdida                   # noqa: PLC0415
        with self.assertRaises(AutoridadPerdida):
            oficina.entregar(B, corpus=self.corpus, paquete=rev, entrega=entrega, circuito=self.circuito)
        despues = sorted(B.almacen.listar("paquetes")), sorted(B.almacen.listar("dictamenes")), sorted(B.almacen.listar("handoffs"))
        self.assertEqual(antes, despues)                  # ni dictamen, ni devolución, ni corrección

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

    def test_09b_quien_corrigio_la_implementacion_tampoco_pasa_la_puerta_del_juez(self):
        """T465 · Defecto que previene: el autor de la CORRECCIÓN toma VER/dosier y su entrega se rechaza después.

        Medido en el quinto dogfood: el handoff a VER venía de la implementación original
        (de otro worker), la puerta sólo miraba handoffs, y quien corrigió consumió un intento.
        """
        C = self.rt("w-C")
        plan = self.planificar(C)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        self.avanzar_prd(C, plan, impl)
        rev = self.paquete_de(plan, "CNS/revision-de-construccion")
        ver = self.paquete_de(plan, "VER/dosier")
        self.tomar_y_acusar(C, impl)
        self.entregar(C, impl, self.entrega(impl, "CNS/implementacion"))
        B = self.rt("w-B")
        self.tomar_y_acusar(B, rev)
        entrega = self.entrega(rev, "CNS/revision-de-construccion", "devuelto")
        entrega["dictamenes"] = [self.dictamen("gate:revision-de-construccion", impl, "no-superado")]
        entrega["devolucion"] = {"que_falta": "la prueba del conflicto no muerde",
                                 "por_que_es_insuficiente": "no protege el cambio",
                                 "que_la_cerraria": "una prueba roja al revertir",
                                 "evidencia": ["tabla de reversión"]}
        res = self.entregar(B, rev, entrega)
        correccion = res["correccion"]["correccion"]
        A = self.rt("w-A")                                  # OTRO worker corrige
        self.tomar_y_acusar(A, correccion)
        self.entregar(A, correccion, self.entrega(correccion, "CNS/implementacion"))
        for juez in (A, C):                                 # ni el que corrigió ni el que construyó
            with self.assertRaises(ciclo.AutocertificacionRechazada):
                oficina.tomar(juez, corpus=self.corpus, paquete=ver, circuito=self.circuito)
            self.assertIsNone(juez._leer_lease(ver))        # y no queda lease detrás
        F = self.rt("w-F")
        with self.assertRaises(Exception) as cm:            # F pasa la puerta: lo que le frena es la dependencia
            oficina.tomar(F, corpus=self.corpus, paquete=ver, circuito=self.circuito)
        self.assertNotIsInstance(cm.exception, ciclo.AutocertificacionRechazada)

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
                              "autoridad": "OWNER", "posturas": ["A: exportar todo", "B: exportar filtrado"],
                              "materia": self.corpus.capacidad("CNS")["autoridad"]["escala"][1]}
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
        # un `no` de verdad en la checklist casa con el `no` del esquema (YAML 1.1 lo lee como False)
        from ciclo import entregas as modulo_entregas, formas as modulo_formas
        esquema = self.corpus.esquema("entrega")
        entrega = {"paquete": "pq-x", "rol": "CNS/implementacion", "veredicto": "entregado",
                   "artefactos": [{"tipo": "commit", "referencia": "abc1234", "descripcion": "el commit"}],
                   "evidencias": [], "diferencias_declaradas": [], "decisiones_asumidas": [], "riesgos": [],
                   "deuda_aceptada": [], "no_hecho": [], "siguiente": "a revisión",
                   "autoevaluacion": {"gate": "gate:implementacion-completa",
                                      "comprobaciones": [{"id": "x", "resultado": "no"}],
                                      "checklist": [{"id": "y", "respuesta": "no-aplica"}, {"id": "z", "respuesta": "no"}]}}
        fallos = modulo_formas.validar(entrega, esquema, corpus=self.corpus, camino="entrega")
        self.assertEqual([f for f in fallos if "respuesta" in f or "resultado" in f], [])
        del modulo_entregas
        # y la plantilla del brief lista los valores cerrados como texto, nunca como booleanos
        brief = oficina.brief_de(self.rt("w-P"), corpus=self.corpus, paquete=self.paquete_de(
            self.planificar(self.rt("w-Q"), item="enc-p")["plan"], "CNS/implementacion"), circuito=self.circuito)
        plantilla = brief["forma_de_la_entrega"]["plantilla"]
        self.assertEqual(plantilla["rol"], "CNS/implementacion")
        self.assertIn("no-aplica", plantilla["autoevaluacion"]["checklist"][0]["respuesta"])
        self.assertNotIn("False", json.dumps(plantilla))
        self.assertTrue(all(a["tipo"] for a in plantilla["artefactos"]))
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


# =========================================================================
# T468 bis · el nivel integrado exige un Integration Set exacto y completo
# =========================================================================
class Integrado(Laboratorio):

    def conjunto(self, item, fuentes, estado="verificado", pendiente=False, con_71=True):
        base = {"id": "IS-001", "item": item, "estado": estado,
                "fuentes": [{"source": f, "commit": "0123456789ab" + str(n), "rama": "ads/" + f}
                            for n, f in enumerate(fuentes)],
                "verificacion": [{"ambito": "regresion", "resultado": "pendiente" if pendiente else "pasa",
                                  "evidencia": "dosier de VER pq-x-1"}],
                "restaura_a": "IS-000, la combinación anterior"}
        if con_71 and len(fuentes) > 1:
            base.update({
                "orden_de_merge": list(fuentes),
                "compatibilidad": [{"entre": list(fuentes),
                                    "condicion": "el frontend tolera la API anterior y la nueva: el backend va antes"}],
                "despliegue": [{"source": f, "orden": n + 1, "como": "PR fusionado y despliegue de " + f}
                               for n, f in enumerate(fuentes)],
                "dependencias": [fuentes[1] + " depende de " + fuentes[0]],
            })
        return base

    def test_22b_con_varias_fuentes_el_conjunto_define_orden_compatibilidad_y_despliegue(self):
        """T497 · Defecto que previene: varias PRs presentadas al Owner como trabajos inconexos (§71)."""
        hechos = {"fuentes_escritas": ["backend", "frontend"]}
        entrega = {"integration_set": self.conjunto("enc-int", ["backend", "frontend"])}
        oficina._exigir_integration_set(self.corpus, entrega, hechos, "pq-conv")     # completo: vale
        uno = {"integration_set": self.conjunto("enc-int", ["backend"], con_71=False)}
        oficina._exigir_integration_set(self.corpus, uno, {"fuentes_escritas": ["backend"]}, "pq-conv")  # una fuente: trivial
        def rechaza(nombre, **cambios):
            conjunto = self.conjunto("enc-int", ["backend", "frontend"])
            for clave, valor in cambios.items():
                if valor is None:
                    conjunto.pop(clave, None)
                else:
                    conjunto[clave] = valor
            with self.assertRaises(ciclo.EntregaInvalida, msg=nombre) as cm:
                oficina._exigir_integration_set(self.corpus, {"integration_set": conjunto}, hechos, "pq-conv")
            return str(cm.exception)
        self.assertIn("orden_de_merge", rechaza("sin orden", orden_de_merge=None))
        self.assertIn("despliegue", rechaza("sin despliegue", despliegue=None))
        self.assertIn("compatibilidad", rechaza("sin compatibilidad", compatibilidad=None))
        self.assertIn("cada una UNA vez", rechaza("orden con una fuente de menos", orden_de_merge=["backend"]))
        self.assertIn("ninguna ajena", rechaza("orden con una fuente ajena", orden_de_merge=["backend", "frontend", "mobile"]))
        self.assertIn("no dice cómo se despliega frontend",
                      rechaza("despliegue incompleto", despliegue=[{"source": "backend", "orden": 1}]))
        self.assertIn("mismo `orden`", rechaza("despliegue sin secuencia",
                                               despliegue=[{"source": "backend", "orden": 1}, {"source": "frontend", "orden": 1}]))
        self.assertIn("fuentes que el conjunto no tiene",
                      rechaza("compatibilidad ajena", compatibilidad=[{"entre": ["backend", "mobile"], "condicion": "tolera la API"}]))
        self.assertIn("integration_set.despliegue", rechaza("despliegue mal formado", despliegue=[{"source": "backend"}]))

    def test_22_integrado_solo_con_un_conjunto_exacto_que_nombra_todas_las_fuentes_escritas(self):
        """T468 · Defecto que previene: «integrado» como palabra, o dos ramas que nadie probó juntas."""
        A = self.rt("w-A")
        B = self.rt("w-B")
        circuito = self.circuitos["cambio-con-interfaz"]
        plan = oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=circuito,
                                  control_repo=self.repo, item="enc-int", titulo="Con pantalla")["plan"]
        filas = self.filas(plan)
        impl = self.paquete_de(plan, "CNS/implementacion")
        conv = self.paquete_de(plan, "ENT/convergencia")
        hechos = {"afecta_superficie": True, "fuentes_escritas": ["backend", "frontend"], "fuentes_escritas_cuenta": 2}
        # hasta que la convergencia sea tomable, entregando cada paquete anterior
        for _ in range(10):
            pendientes, _inv = A._dependencias_pendientes(A._leer_paquete(conv))
            if not pendientes:
                break
            pq = [t["paquete"] for t in A.tomables()["tomables"] if t["paquete"] != conv][0]
            rol = filas[pq]["rol"]
            trabajador = A if rol in ("PRD/definicion", "PRD/criterio-de-exito", "DIS/diseno-visual", "CNS/implementacion") else B
            self.tomar_y_acusar(trabajador, pq)
            entrega = self.entrega(pq, rol)
            if rol == "DIS/revision-de-fidelidad":
                entrega["dictamenes"] = [self.dictamen("gate:excelencia-visual", impl)]
            if rol == "CNS/revision-de-construccion":
                entrega["dictamenes"] = [self.dictamen("gate:implementacion-completa", impl),
                                         self.dictamen("gate:revision-de-construccion", impl)]
            if rol == "VER/dosier":
                entrega["dictamenes"] = [self.dictamen("gate:evidencia-suficiente", impl)]
            oficina.entregar(trabajador, corpus=self.corpus, paquete=pq, entrega=entrega, circuito=circuito, hechos=hechos)
        ev = oficina.evaluar_terminacion(A, corpus=self.corpus, item="enc-int", circuito=circuito, hechos=hechos)
        self.assertIn("integrado", ev["faltan"])
        # el CONSTRUCTOR no puede declarar la convergencia de lo suyo
        with self.assertRaises(ciclo.AutocertificacionRechazada):
            self.tomar_y_acusar(A, conv)
        self.tomar_y_acusar(B, conv)
        base = self.entrega(conv, "ENT/convergencia")
        base["artefactos"].append({"tipo": "integration-set", "referencia": "IS-001", "descripcion": "el conjunto"})
        base["dictamenes"] = [self.dictamen("gate:convergencia-de-fuentes", impl)]
        revision = B.almacen.revision()["revision"]
        # sin conjunto · con una fuente de menos · por rama · pendiente · parcial: cinco rechazos
        for nombre, conjunto in (
            ("sin conjunto", None),
            ("fuente de menos", self.conjunto("enc-int", ["backend"])),
            ("pendiente", self.conjunto("enc-int", ["backend", "frontend"], pendiente=True)),
            ("parcial", self.conjunto("enc-int", ["backend", "frontend"], estado="parcial")),
            ("por rama", dict(self.conjunto("enc-int", ["backend", "frontend"]),
                              fuentes=[{"source": "backend", "commit": "0123456789ab0"},
                                       {"source": "frontend", "commit": "feature/rama"}])),
        ):
            entrega = dict(base)
            if conjunto is not None:
                entrega["integration_set"] = conjunto
            with self.assertRaises(ciclo.EntregaInvalida, msg=nombre):
                oficina.entregar(B, corpus=self.corpus, paquete=conv, entrega=entrega, circuito=circuito, hechos=hechos)
            self.assertEqual(B.almacen.revision()["revision"], revision, nombre)
        entrega = dict(base)
        entrega["integration_set"] = self.conjunto("enc-int", ["backend", "frontend"])
        res = oficina.entregar(B, corpus=self.corpus, paquete=conv, entrega=entrega, circuito=circuito, hechos=hechos)
        self.assertEqual([d["dictamen"] for d in res["dictamenes"]], ["superado"])
        ev = oficina.evaluar_terminacion(A, corpus=self.corpus, item="enc-int", circuito=circuito, hechos=hechos)
        estados = {f["nivel"]: f["estado"] for f in ev["niveles"]}
        self.assertEqual(estados["integrado"], "alcanzado")
        self.assertEqual(ev["faltan"], ["aceptado"])
        # y un item que no escribe fuentes lo declara inaplicable, sólo por su condición
        ev = terminacion.evaluar(circuito, item="enc-int", paquetes_del_item=plan["paquetes"], dictamenes=[],
                                 hechos={"fuentes_escritas_cuenta": 0, "afecta_superficie": True})
        self.assertEqual({f["nivel"]: f["estado"] for f in ev["niveles"]}["integrado"], "inaplicable")


# =========================================================================
# T474 bis · la crónica: la secuencia se deriva del diario, no de un registro aparte
# =========================================================================
class Cronica(Laboratorio):

    def test_23_la_cronica_dice_quien_tomo_que_y_que_entrego_en_el_orden_del_diario(self):
        """T474 · Defecto que previene: una secuencia que sólo existe en la memoria del que la vio."""
        from ciclo import cronica
        A = self.rt("w-A")
        B = self.rt("w-B")
        plan = self.planificar(A)["plan"]
        filas = self.filas(plan)
        primero = A.tomables()["tomables"][0]["paquete"]
        self.tomar_y_acusar(A, primero)
        A.checkpoint(primero, {"paso": 1})
        self.entregar(A, primero, self.entrega(primero, filas[primero]["rol"]))
        segundo = A.tomables()["tomables"][0]["paquete"]
        self.tomar_y_acusar(B, segundo)
        sucesos = cronica.derivar(A.almacen, item="enc-x")
        secuencias = [s["secuencia"] for s in sucesos]
        self.assertEqual(secuencias, sorted(secuencias))
        # una fila por transacción CONFIRMADA: ni la fase abierta ni la preparada cuentan
        self.assertEqual(len(set(s["transaccion"] for s in sucesos)), len(sucesos))
        self.assertEqual([s["clase"] for s in sucesos if s["paquete"] == primero].count("runtime.lease.adquirido"), 1)
        clases_de_a = [s["clase"] for s in sucesos if s["autor"] == "w-A" and s["paquete"] == primero]
        self.assertIn("runtime.lease.adquirido", clases_de_a)
        self.assertTrue(any(c.startswith("ciclo.entrega") for c in clases_de_a))
        self.assertLess(clases_de_a.index("runtime.lease.adquirido"),
                        [i for i, c in enumerate(clases_de_a) if c.startswith("ciclo.entrega")][0])
        por = cronica.por_trabajador(sucesos)
        self.assertIn("w-A", por)
        self.assertIn("w-B", por)
        self.assertTrue(any(s["paquete"] == segundo and s["clase"] == "runtime.lease.adquirido" for s in por["w-B"]))
        # determinista: dos derivaciones, los mismos bytes
        self.assertEqual(json.dumps(sucesos, sort_keys=True), json.dumps(cronica.derivar(A.almacen, item="enc-x"), sort_keys=True))
        texto = cronica.como_texto(sucesos)
        self.assertIn("CRÓNICA DE LA OFICINA", texto)
        self.assertNotIn(self.repo, texto)


# =========================================================================
# T483–T486 · handoffs con los catorce campos de §78, acuse obligatorio, materia del
# escalado y fronteras previas a la construcción (Directiva del Owner de La Pesquerapp)
# =========================================================================
class HandoffsYFronteras(Laboratorio):

    def test_24_entregar_con_un_handoff_recibido_sin_acusar_se_rechaza(self):
        """T483 · Defecto que previene: «seguimos» como transferencia implícita (§78)."""
        from ciclo import handoffs
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        self.avanzar_prd(A, plan, impl)
        # tomar SIN acusar: el brief lista lo recibido, y se entrega sin haberlo acusado
        toma = oficina.tomar(A, corpus=self.corpus, paquete=impl, circuito=self.circuito)
        self.assertTrue(toma["brief"]["recibes"])
        with self.assertRaises(ciclo.EntregaInvalida) as cm:
            self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        self.assertIn("sin acusar", str(cm.exception))
        self.assertEqual(A._leer_paquete(impl)["estado"], "ejecutando")   # no tocó el estado
        for h in toma["brief"]["recibes"]:
            oficina.acusar(A, corpus=self.corpus, handoff=h["id"], comprobaciones_superadas=h["comprueba_al_recibir"])
        res = self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        self.assertEqual(res["veredicto"], "entregado")
        self.assertTrue(all(h["estado"] == handoffs.ACUSADO for h in oficina.handoffs_del_item(A.almacen, "enc-x")
                            if (h.get("trazabilidad") or {}).get("destino") == impl))

    def test_25_el_handoff_emitido_lleva_los_catorce_campos_de_la_directiva(self):
        """T484 · Defecto que previene: un receptor que reconstruye la entrega leyendo un chat."""
        from ciclo import handoffs
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        self.avanzar_prd(A, plan, impl)
        self.tomar_y_acusar(A, impl)
        e = self.entrega(impl, "CNS/implementacion")
        e["riesgos"] = ["la migración toca una tabla caliente"]
        e["decisiones_asumidas"] = ["índice compuesto en vez de dos simples"]
        e["no_hecho"] = ["la exportación a XLSX"]
        res = self.entregar(A, impl, e)
        self.assertTrue(res["handoffs_emitidos"])
        emitido = [h for h in oficina.handoffs_del_item(A.almacen, "enc-x") if h["id"] in res["handoffs_emitidos"]][0]
        contenido = emitido["contenido"]
        self.assertEqual(sorted(contenido), sorted(handoffs.CAMPOS_DE_78))
        self.assertEqual(contenido["paquete"], impl)
        self.assertEqual(contenido["origen"]["rol"], "CNS/implementacion")
        self.assertTrue(contenido["destino"]["paquete"])
        self.assertTrue(contenido["entrada_recibida"])                 # lo que impl acusó de PRD
        self.assertEqual(contenido["riesgos"], ["la migración toca una tabla caliente"])
        self.assertEqual(contenido["decisiones"], ["índice compuesto en vez de dos simples"])
        self.assertIn("la exportación a XLSX", contenido["cuestiones_abiertas"])
        self.assertTrue(contenido["que_puede_devolver_el_receptor"]["rechaza_si"])
        self.assertEqual(len(contenido["entregables"]), len(e["artefactos"]))
        # un contenido a medias no se emite
        with self.assertRaises(ciclo.HandoffIncompleto):
            handoffs.emitir("handoff:con-a-ver", artefactos=["commit:abc"], checkpoint="x",
                            trazabilidad={"item": "i", "paquete": "p", "ruta": "r"}, corpus=self.corpus,
                            contenido={"origen": "x"})

    def test_26_escalar_exige_una_materia_que_la_capacidad_escala_y_no_una_que_decide_sola(self):
        """T485 · Defecto que previene: el Owner arbitrando spacing (Directiva §20, §41, §76)."""
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        crit = self.paquete_de(plan, "PRD/criterio-de-exito")
        defin = self.paquete_de(plan, "PRD/definicion")
        self.tomar_y_acusar(A, defin)
        self.entregar(A, defin, self.entrega(defin, "PRD/definicion"))
        self.tomar_y_acusar(A, crit)
        autoridad = self.corpus.capacidad("PRD")["autoridad"]
        base = {"que_lo_impide": "el criterio exige una decisión de alcance", "que_lo_desbloquearia": "que el Owner elija",
                "autoridad": "OWNER", "posturas": ["A: exportar todo", "B: exportar sólo lo filtrado"]}
        # sin materia: no
        e = self.entrega(crit, "PRD/criterio-de-exito", "escalado"); e["bloqueo"] = dict(base)
        with self.assertRaises(ciclo.EntregaInvalida) as cm:
            self.entregar(A, crit, e)
        self.assertIn("materia", str(cm.exception))
        # una materia que PRD decide sola: no
        e["bloqueo"] = dict(base, materia=autoridad["decide_sola"][0])
        with self.assertRaises(ciclo.EntregaInvalida) as cm:
            self.entregar(A, crit, e)
        self.assertIn("decide sola", str(cm.exception))
        # una materia inventada: no
        e["bloqueo"] = dict(base, materia="el color del botón de exportar")
        with self.assertRaises(ciclo.EntregaInvalida):
            self.entregar(A, crit, e)
        self.assertEqual(A._leer_paquete(crit)["estado"], "ejecutando")   # nada tocó el estado
        # una de las que ESCALA: sí, y el cierre queda escalado con su autoridad
        e["bloqueo"] = dict(base, materia=autoridad["escala"][0])
        res = self.entregar(A, crit, e)
        self.assertEqual(res["cierre"]["salida"], "escalado")
        self.assertEqual(res["cierre"]["autoridad"], "OWNER")

    def test_26b_un_corpus_sin_autoridad_no_autoriza_un_escalado(self):
        """T485 · Defecto que previene: que una ficha ilegible autorice cualquier materia."""
        from ciclo.errores import CorpusIlegible, CorpusIncompleto
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        defin = self.paquete_de(plan, "PRD/definicion")
        self.tomar_y_acusar(A, defin)
        e = self.entrega(defin, "PRD/definicion", "escalado")
        e["bloqueo"] = {"que_lo_impide": "materia inventada", "que_lo_desbloquearia": "decisión del Owner",
                        "autoridad": "OWNER", "posturas": ["A", "B"], "materia": "inventada"}
        revision = A.almacen.revision()["revision"]
        for error in (CorpusIlegible, CorpusIncompleto):
            with self.subTest(error=error.__name__):
                with patch.object(self.corpus, "capacidad", side_effect=error("ficha ausente")):
                    with self.assertRaises(ciclo.EntregaInvalida) as cm:
                        self.entregar(A, defin, e)
                self.assertIn("autoridad", str(cm.exception))
                self.assertEqual(A.almacen.revision()["revision"], revision)
                self.assertEqual(A._leer_paquete(defin)["estado"], "ejecutando")

    def test_27_las_fronteras_previas_a_la_construccion_se_distinguen(self):
        """T486 · Defecto que previene: «cerrado» como sinónimo de «implementado», y un item del
        que nadie sabe si está diseñado (Directiva §77)."""
        A = self.rt("w-A")
        circuito = self.circuitos["cambio-con-interfaz"]
        plan = oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=circuito,
                                  control_repo=self.repo, item="enc-ui", titulo="Diálogo nuevo")["plan"]
        hechos = {"afecta_superficie": True}
        ev = oficina.evaluar_terminacion(A, corpus=self.corpus, item="enc-ui", circuito=circuito, hechos=hechos)
        fr = {f["frontera"]: f["estado"] for f in ev["fronteras"]}
        self.assertEqual(fr["admitida"], "alcanzado")
        self.assertEqual(fr["encuadrada"], "alcanzado")
        self.assertEqual(fr["investigada"], "no-exigido")          # el circuito no trae INV
        self.assertEqual(fr["disenada"], "pendiente")
        self.assertEqual(fr["aprobada"], "sin-mecanismo")          # se dice, no se finge
        # se entrega el diseño visual —el único paquete de la frontera en este circuito—: la
        # frontera diseñada queda alcanzada, sin tocar los niveles
        dis = self.paquete_de(plan, "DIS/diseno-visual")
        filas = self.filas(plan)
        for _ in range(6):
            pendientes, inviables = A._dependencias_pendientes(A._leer_paquete(dis))
            if not pendientes and not inviables:
                break
            pq = [t["paquete"] for t in A.tomables()["tomables"] if t["paquete"] != dis and t["paquete"] in filas][0]
            self.tomar_y_acusar(A, pq)
            self.entregar(A, pq, self.entrega(pq, filas[pq]["rol"]))
        self.tomar_y_acusar(A, dis)
        res = oficina.entregar(A, corpus=self.corpus, paquete=dis, entrega=self.entrega(dis, "DIS/diseno-visual"), circuito=circuito)
        self.assertEqual(res["veredicto"], "entregado")
        ev = oficina.evaluar_terminacion(A, corpus=self.corpus, item="enc-ui", circuito=circuito, hechos=hechos)
        fr = {f["frontera"]: f["estado"] for f in ev["fronteras"]}
        self.assertEqual(fr["disenada"], "alcanzado")
        # y cuando la frontera tiene MAS de un paquete, uno entregado no la alcanza: la frontera
        # nombra lo que espera, y solo con todos entregados queda alcanzada
        from ciclo import terminacion
        plan_dos = {"encuadre": "enc-x", "correspondencia": [
            {"paquete": "pq-visual", "rol": "DIS/diseno-visual"},
            {"paquete": "pq-interaccion", "rol": "DIS/diseno-interaccion"},
            {"paquete": "pq-cns", "rol": "CNS/implementacion"}]}
        fr_dos = {f["frontera"]: f for f in terminacion.evaluar_fronteras(plan_dos, {"pq-visual": "completado"})}
        self.assertEqual(fr_dos["disenada"]["estado"], "pendiente")
        self.assertIn("pq-interaccion", fr_dos["disenada"]["motivo"])
        self.assertNotIn("pq-visual", fr_dos["disenada"]["motivo"])
        fr_dos = {f["frontera"]: f for f in terminacion.evaluar_fronteras(
            plan_dos, {"pq-visual": "completado", "pq-interaccion": "completado"})}
        self.assertEqual(fr_dos["disenada"]["estado"], "alcanzado")
        self.assertIn("implementado", ev["faltan"])                # las fronteras no son niveles


class CatalogoDeClases(Laboratorio):
    """Las clases de trabajo que el catálogo profesional de una instancia declara y que el
    kernel nunca había planificado: participaciones DOBLES de una capacidad (`DOM`, `SEG`) y
    el proceso que deriva su propietario del encargo (`DIR`)."""

    def test_28_una_capacidad_que_participa_dos_veces_acuna_paquetes_distintos(self):
        """T487 · Defecto que previene: ninguna clase con C-DOM o C-SEG se podía planificar
        (`a.5` comparaba un paquete consigo mismo), medido en el catálogo de La Pesquerapp."""
        A = self.rt("w-A")
        circuito = self.circuitos["cambio-de-dominio"]
        plan = oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=circuito,
                                  control_repo=self.repo, item="enc-dom", titulo="Entidad nueva")["plan"]
        filas = plan["correspondencia"]
        ids = [f["paquete"] for f in filas]
        self.assertEqual(len(ids), len(set(ids)), "dos filas del plan comparten paquete")
        dom = [f["paquete"] for f in filas if str(f.get("rol") or "").startswith("DOM/")]
        self.assertEqual(len(dom), 4, "DOM participa dos veces con dos roles: cuatro paquetes")
        orden = {f["paquete"]: i for i, f in enumerate(filas)}
        cns = self.paquete_de(plan, "CNS/implementacion")
        ver = self.paquete_de(plan, "VER/dosier")
        antes = [p for p in dom if orden[p] < orden[cns]]
        despues = [p for p in dom if orden[p] > orden[ver]]
        self.assertEqual(len(antes), 2, "modelo y migración se planifican ANTES de construir")
        self.assertEqual(len(despues), 2, "y la revisión posterior de DOM va DESPUÉS de verificar")
        # la dependencia por independencia se resuelve DENTRO de la misma participación
        modelo_antes = [p for p in antes if self.filas(plan)[p]["rol"] == "DOM/modelo"][0]
        migracion_antes = [p for p in antes if self.filas(plan)[p]["rol"] == "DOM/migracion"][0]
        depende = set(A._leer_paquete(migracion_antes).get("depende_de") or [])
        self.assertIn(modelo_antes, depende)
        self.assertFalse(depende & set(despues), "la migración previa no espera a la revisión posterior")
        # replanificar es idempotente por contenido: mismos identificadores
        plan2 = oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=circuito,
                                   control_repo=self.repo, item="enc-dom", titulo="Entidad nueva")["plan"]
        self.assertEqual(ids, [f["paquete"] for f in plan2["correspondencia"]])

    def test_29_el_cambio_de_direccion_deriva_su_propietario_del_encargo(self):
        """T488 · Defecto que previene: `DIR` no se podía planificar desde la oficina porque el
        propietario que el encargo declara nunca llegaba a la composición (`b.16`)."""
        A = self.rt("w-A")
        circuito = self.circuitos["cambio-de-direccion"]
        with self.assertRaises(ciclo.PropietarioNoDerivable):
            oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=circuito,
                               control_repo=self.repo, item="enc-dir", titulo="Nuevo lenguaje")
        # el propietario que el encargo declara, sin decir quién produce las sustituciones:
        # la obligación con productora DERIVADA sigue sin productora y la fase no abre
        entrada = dict(self.entrada(), propietario_global="PRD")
        with self.assertRaises(ciclo.ComposicionIncompleta):
            oficina.planificar(A, corpus=self.corpus, entrada=entrada, circuito=circuito,
                               control_repo=self.repo, item="enc-dir", titulo="Nuevo lenguaje")
        entrada["productores_declarados"] = {"sustituciones-registradas": "PRD"}
        plan = oficina.planificar(A, corpus=self.corpus, entrada=entrada, circuito=circuito,
                                  control_repo=self.repo, item="enc-dir", titulo="Nuevo lenguaje")["plan"]
        self.assertEqual(plan["propietario_global"], "PRD")
        self.assertEqual(plan["proceso"], "proceso:DIR")
        roles = [f.get("rol") for f in plan["correspondencia"]]
        self.assertIn("ARQ/encaje", roles)
        self.assertIn("VER/decision", roles)
        self.assertNotIn("CNS/implementacion", roles)                # un DIR no construye
        entrada = dict(self.entrada(), propietario_global="ZZZ",
                       productores_declarados={"sustituciones-registradas": "PRD"})
        with self.assertRaises(ciclo.PropietarioNoDerivable):
            oficina.planificar(A, corpus=self.corpus, entrada=entrada, circuito=circuito,
                               control_repo=self.repo, item="enc-dir2", titulo="Nuevo lenguaje")


class EstacionDeImpacto(Laboratorio):
    """Directiva §5: la clasificación inicial no conoce todo el impacto; el trabajo lo revela y
    el circuito reacciona solo (§62), sin esperar a que alguien lo note."""

    def test_30_un_impacto_que_el_circuito_cubre_no_marca_nada(self):
        """T489 · Defecto que previene: tratar toda declaración de impacto como alarma."""
        A = self.rt("w-A")
        circuito = self.circuitos["cambio-con-interfaz"]
        plan = oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=circuito,
                                  control_repo=self.repo, item="enc-ui", titulo="Diálogo nuevo")["plan"]
        defin = self.paquete_de(plan, "PRD/definicion")
        self.tomar_y_acusar(A, defin)
        e = self.entrega(defin, "PRD/definicion")
        e["impacto"] = {"disparadores": ["nuevo-estado-visible", "nueva-accion"], "nota": "un estado y una acción nuevos"}
        res = oficina.entregar(A, corpus=self.corpus, paquete=defin, entrega=e, circuito=circuito)
        self.assertEqual(res["veredicto"], "entregado")
        self.assertEqual(res["impacto"]["condiciones_derivadas"], ["C-DIS"])
        self.assertEqual(res["impacto"]["no_cubiertas"], [])
        self.assertIsNone(oficina.plan_vigente_de_item(A.almacen, "enc-ui").get("impacto"))
        criterio = self.paquete_de(plan, "PRD/criterio-de-exito")
        self.tomar_y_acusar(A, criterio)                          # el item sigue

    def test_31_un_impacto_que_el_circuito_no_cubre_marca_el_plan_y_para_el_item(self):
        """T490 · Defecto que previene: seguir construyendo sobre una clasificación que ya se
        sabe incompleta (§5: «los circuitos no deben asumir…»; §62: reacción automática)."""
        A = self.rt("w-A")
        B = self.rt("w-B")
        plan = self.planificar(A, item="enc-back")["plan"]          # cambio-de-backend: sin C-DIS
        defin = self.paquete_de(plan, "PRD/definicion")
        self.tomar_y_acusar(A, defin)
        e = self.entrega(defin, "PRD/definicion")
        e["impacto"] = {"disparadores": ["nuevo-estado-visible", "nuevo-permiso"]}
        res = oficina.entregar(A, corpus=self.corpus, paquete=defin, entrega=e, circuito=self.circuito)
        self.assertEqual(res["veredicto"], "entregado")             # la entrega vale: lo que vio, cuenta
        self.assertEqual(res["impacto"]["no_cubiertas"], ["C-DIS", "C-SEG"])
        marca = oficina.plan_vigente_de_item(A.almacen, "enc-back")["impacto"]
        self.assertEqual(marca["condiciones_no_cubiertas"], ["C-DIS", "C-SEG"])
        self.assertEqual(marca["rol"], "PRD/definicion")
        self.assertIn("replanificar", marca["que_hacer"])
        criterio = self.paquete_de(plan, "PRD/criterio-de-exito")
        with self.assertRaises(ciclo.ImpactoNoCubierto):
            oficina.tomar(B, corpus=self.corpus, paquete=criterio, circuito=self.circuito)
        self.assertIsNone(B._leer_lease(criterio))                  # no quedó lease colgado
        ev = oficina.evaluar_terminacion(A, corpus=self.corpus, item="enc-back", circuito=self.circuito,
                                         hechos={"afecta_superficie": False})
        self.assertEqual(ev["impacto"]["condiciones_no_cubiertas"], ["C-DIS", "C-SEG"])
        # REPLANIFICAR con un circuito que cubre C-DIS (generación nueva) sustituye al plan marcado
        nuevo = oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(), circuito=self.circuitos["cambio-con-interfaz"],
                                   control_repo=self.repo, item="enc-back", titulo="Exportar CSV", generacion=1)["plan"]
        self.assertEqual(nuevo["sustituye_a"], plan["id"])
        vigente = oficina.plan_vigente_de_item(A.almacen, "enc-back")
        self.assertEqual(vigente["id"], nuevo["id"])
        self.assertIsNone(vigente.get("impacto"))
        definicion2 = self.paquete_de(nuevo, "PRD/definicion")
        self.tomar_y_acusar(B, definicion2)                         # el item vuelve a andar

    def test_32_un_disparador_fuera_de_los_dieciseis_es_una_entrega_invalida(self):
        """T491 · Defecto que previene: «impacto» como prosa libre."""
        A = self.rt("w-A")
        plan = self.planificar(A)["plan"]
        defin = self.paquete_de(plan, "PRD/definicion")
        self.tomar_y_acusar(A, defin)
        e = self.entrega(defin, "PRD/definicion")
        e["impacto"] = {"disparadores": ["cosa-rara"]}
        revision = A.almacen.revision()["revision"]
        with self.assertRaises(ciclo.EntregaInvalida) as cm:
            oficina.entregar(A, corpus=self.corpus, paquete=defin, entrega=e, circuito=self.circuito)
        self.assertIn("dieciséis", str(cm.exception))
        self.assertEqual(A.almacen.revision()["revision"], revision)
        from ciclo import impacto as modulo_impacto
        self.assertEqual(len(modulo_impacto.DISPARADORES), 16)
        self.assertEqual(modulo_impacto.comprobar_vocabulario(), [])


class ParadasTipadas(Laboratorio):
    """Directiva §36: el supervisor para por riesgo extraordinario o barrera externa con NOMBRE,
    porque son las dos condiciones (3 y 4) que necesitan al Owner y que `bloqueado` confundía
    con una dependencia interna."""

    def _bloquear(self, clase, instancia="w-A", item="enc-x"):
        A = self.rt(instancia)
        plan = self.planificar(A, item=item)["plan"]
        defin = self.paquete_de(plan, "PRD/definicion")
        self.tomar_y_acusar(A, defin)
        e = self.entrega(defin, "PRD/definicion", "bloqueado")
        e["bloqueo"] = {"que_lo_impide": "algo que este rol no puede resolver", "que_lo_desbloquearia": "lo que haga falta",
                        "autoridad": "PRD"}
        if clase:
            e["bloqueo"]["clase"] = clase
        res = oficina.entregar(A, corpus=self.corpus, paquete=defin, entrega=e, circuito=self.circuito)
        self.assertEqual(res["veredicto"], "bloqueado")
        return A, defin

    def test_33a_una_barrera_externa_es_una_parada_con_nombre(self):
        """T492 · Defecto que previene: una barrera externa parada como «bloqueado» genérico,
        que TRABAJA trata como algo que un desbloqueador resuelve (§36.4)."""
        A, defin = self._bloquear("barrera-externa")
        self.assertEqual(A._leer_paquete(defin)["clase_de_bloqueo"], "barrera-externa")
        res = modulo_supervisor.Supervisor(A, corpus=self.corpus, reloj=lambda s: None).bucle(pasadas=2)
        self.assertEqual(res["parada"], "barrera-externa")
        self.assertIn(defin, res["motivo"])

    def test_33b_un_riesgo_extraordinario_es_una_parada_con_nombre_y_manda_sobre_los_demas(self):
        """T492 · el riesgo extraordinario (§36.3) se nombra, y con una barrera al lado gana."""
        A, defin = self._bloquear("barrera-externa", item="enc-b")
        B, defin2 = self._bloquear("riesgo-extraordinario", instancia="w-B", item="enc-r")
        self.assertEqual(B._leer_paquete(defin2)["clase_de_bloqueo"], "riesgo-extraordinario")
        res = modulo_supervisor.Supervisor(B, corpus=self.corpus, reloj=lambda s: None).bucle(pasadas=2)
        self.assertEqual(res["parada"], "riesgo-extraordinario")
        self.assertIn(defin2, res["motivo"])
        self.assertNotIn(defin, res["motivo"])

    def test_33c_sin_clase_sigue_siendo_bloqueado_y_una_clase_inventada_no_entra(self):
        """T492 · sin clase, `bloqueado` (dependencia interna o decisión); una clase fuera de las
        tres es una entrega inválida."""
        A, defin = self._bloquear(None)
        self.assertNotIn("clase_de_bloqueo", A._leer_paquete(defin))
        self.assertEqual(modulo_supervisor.Supervisor(A, corpus=self.corpus, reloj=lambda s: None).bucle(pasadas=2)["parada"], "bloqueado")
        B = self.rt("w-B")
        plan = self.planificar(B, item="enc-y")["plan"]
        defin = self.paquete_de(plan, "PRD/definicion")
        self.tomar_y_acusar(B, defin)
        e = self.entrega(defin, "PRD/definicion", "bloqueado")
        e["bloqueo"] = {"que_lo_impide": "algo que este rol no puede resolver", "que_lo_desbloquearia": "lo que haga falta",
                        "autoridad": "PRD", "clase": "pereza"}
        with self.assertRaises(ciclo.EntregaInvalida):
            oficina.entregar(B, corpus=self.corpus, paquete=defin, entrega=e, circuito=self.circuito)


# =========================================================================
# T494–T496 · la base de partida y el mundo que cambia debajo (Directiva §61, §63)
# =========================================================================
class BaseDePartida(Laboratorio):
    """El control repo del laboratorio se convierte en un repositorio Git con `main` y una
    rama de trabajo; `main` avanza desde un worktree aparte, como lo haría otro agente."""

    def _git(self, *args, cwd=None):
        return subprocess.run(["git", "-c", "user.name=lab", "-c", "user.email=lab@ads.invalid",
                               "-c", "commit.gpgsign=false", *args], cwd=cwd or self.repo,
                              capture_output=True, text=True, check=True, env=ENTORNO).stdout.strip()

    def _escribir(self, ruta, texto, cwd=None):
        completa = os.path.join(cwd or self.repo, ruta)
        os.makedirs(os.path.dirname(completa), exist_ok=True)
        with open(completa, "w", encoding="utf-8") as manejador:
            manejador.write(texto)

    def _repo_git(self):
        self._git("init", "-q", "-b", "main")
        self._escribir("src/a.php", "uno\ndos\n")
        self._git("add", "PROFILE.md", "src/a.php")
        self._git("commit", "-q", "-m", "base")
        self._git("checkout", "-q", "-b", "trabajo")
        return self._git("rev-parse", "main")[:12]

    def _avanzar_main(self, ruta, texto):
        """Otro agente avanza `main` desde un worktree aparte; el laboratorio sigue en `trabajo`."""
        aparte = tempfile.mkdtemp(prefix="ads-main-")
        self._git("worktree", "add", "-q", aparte, "main")
        try:
            self._escribir(ruta, texto, cwd=aparte)
            self._git("add", ruta, cwd=aparte)
            self._git("commit", "-q", "-m", "avance de la base", cwd=aparte)
        finally:
            self._git("worktree", "remove", "--force", aparte)
        return self._git("rev-parse", "main")[:12]

    def _commit_mio(self, ruta, texto):
        self._escribir(ruta, texto)
        self._git("add", ruta)
        self._git("commit", "-q", "-m", "mi trabajo")

    @staticmethod
    def _base_del_checkpoint(rt, paquete):
        from runtime.externo import leer_checkpoint                     # noqa: PLC0415
        return (leer_checkpoint(rt, paquete)["contenido"]).get("base")

    def _implementacion_tomada(self, rt):
        plan = self.planificar(rt)["plan"]
        impl = self.paquete_de(plan, "CNS/implementacion")
        self.avanzar_prd(rt, plan, impl)
        return impl, self.tomar_y_acusar(rt, impl)

    def test_34_al_tomar_nace_la_base_y_un_avance_compatible_se_registra(self):
        """T494 · Defecto que previene: un trabajo que no sabe de qué commit nació ni en qué rama está."""
        main0 = self._repo_git()
        A = self.rt("w-A")
        impl, toma = self._implementacion_tomada(A)
        base = toma["base"]
        self.assertEqual(base["veredicto"], "sin-cambio")
        self.assertEqual(base["nacimiento"]["control-repo"]["rama"], "trabajo")
        self.assertEqual(base["nacimiento"]["control-repo"]["nacio_de"], main0)
        self.assertEqual(self._base_del_checkpoint(A, impl)["nacimiento"]["control-repo"]["base_ahora"], main0)
        self._commit_mio("src/a.php", "uno-mio\ndos\n")
        main1 = self._avanzar_main("docs/otro.md", "otra cosa\n")
        cp = oficina.checkpoint(A, paquete=impl, contenido={"paso": 1})
        base = cp["contenido"]["base"]
        self.assertEqual(base["veredicto"], "compatible")
        self.assertEqual(base["registrada"]["control-repo"], main1)
        self.assertEqual(base["nacimiento"]["control-repo"]["nacio_de"], main0)
        self.assertEqual(base["ahora"]["control-repo"]["commits_de_la_base_que_no_tengo"], 1)
        self.assertEqual(base["ahora"]["control-repo"]["rama"], "trabajo")
        self.assertEqual(cp["contenido"]["paso"], 1)
        res = self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        self.assertEqual(res["veredicto"], "entregado")
        self.assertEqual(self._base_del_checkpoint(A, impl)["veredicto"], "compatible")
        self.assertTrue(A.almacen.verificar_integridad().a_dict()["ok"])

    def test_35_un_avance_que_toca_lo_mismo_contradice_y_no_se_entrega_hasta_reconciliar(self):
        """T495 · Defecto que previene: entregar «terminado» sobre una base que ya cambió lo mismo."""
        self._repo_git()
        A = self.rt("w-A")
        impl, _ = self._implementacion_tomada(A)
        self._commit_mio("src/a.php", "uno-mio\ndos\n")
        main1 = self._avanzar_main("src/a.php", "uno\ndos\ntres\n")
        cp = oficina.checkpoint(A, paquete=impl, contenido={"paso": 1})
        base = cp["contenido"]["base"]
        self.assertEqual(base["veredicto"], "contradiccion")
        self.assertEqual(base["conflictos"], [{"repo": "control-repo", "commits_nuevos": 1,
                                               "ficheros": ["src/a.php"]}])
        self.assertNotIn("control-repo", base["registrada"])
        revision = A.almacen.revision()["revision"]
        with self.assertRaises(ciclo.BaseContradicha) as contexto:
            self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        self.assertIn("src/a.php", str(contexto.exception))
        self.assertEqual(A.almacen.revision()["revision"], revision)
        self.assertEqual(A._leer_paquete(impl)["estado"], "ejecutando")
        # el trabajador reconcilia EN SU RAMA (hunks distintos: la fusión es limpia) y vuelve a entregar
        self._git("merge", "-q", "--no-edit", "main")
        cp = oficina.checkpoint(A, paquete=impl, contenido={"paso": 2})
        self.assertEqual(cp["contenido"]["base"]["veredicto"], "sin-cambio")
        self.assertEqual(cp["contenido"]["base"]["registrada"]["control-repo"], main1)
        res = self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        self.assertEqual(res["veredicto"], "entregado")

    def test_36_sin_git_no_se_mide_y_nada_cambia(self):
        """T496 · Defecto que previene: un control repo sin Git frenado por una medida que no existe."""
        A = self.rt("w-A")
        impl, toma = self._implementacion_tomada(A)
        self.assertIsNone(toma["base"])
        from runtime.externo import leer_checkpoint                     # noqa: PLC0415
        self.assertIsNone(leer_checkpoint(A, impl))
        cp = oficina.checkpoint(A, paquete=impl, contenido={"paso": 1})
        self.assertEqual(cp["contenido"], {"paso": 1})
        res = self.entregar(A, impl, self.entrega(impl, "CNS/implementacion"))
        self.assertEqual(res["veredicto"], "entregado")
        self.assertEqual(leer_checkpoint(A, impl)["contenido"], {"paso": 1})


# =========================================================================
# T498 · exclusión segura entre workers por recurso exclusivo (Directiva §68)
# =========================================================================
class ExclusionPorRecurso(Laboratorio):

    def _tres(self, A):
        A.crear_item(id="it-1", titulo="primero", motivo="alta")
        orden = paquete_runtime.orden_externa(argumentos=["CNS", "CNS/implementacion"])
        A.crear_paquete(id="pq-a", item="it-1", capacidades_requeridas=["worker"], orden=orden,
                        acoplamiento={"escribe_ficheros": ["src/a.php"], "afecta_contratos": ["api/v2/pedidos"]})
        A.crear_paquete(id="pq-b", item="it-1", capacidades_requeridas=["worker"], orden=orden,
                        acoplamiento={"escribe_ficheros": ["src/b.php"], "afecta_contratos": ["api/v2/pedidos"]})
        A.crear_paquete(id="pq-c", item="it-1", capacidades_requeridas=["worker"], orden=orden,
                        acoplamiento={"escribe_ficheros": ["src/c.php"], "lee_fuentes": ["backend"]})

    def test_37_un_recurso_exclusivo_en_manos_ajenas_hace_al_paquete_temporalmente_incompatible(self):
        """T498 · Defecto que previene: dos workers sobre el mismo contrato a la vez, y el Owner arbitrando."""
        A = self.rt("w-A")
        self._tres(A)
        self.assertEqual([t["paquete"] for t in A.tomables()["tomables"]], ["pq-a", "pq-b", "pq-c"])
        A.tomar("pq-a")
        tomables = A.tomables()
        self.assertEqual([t["paquete"] for t in tomables["tomables"]], ["pq-a", "pq-c"])
        esperando = {t["paquete"]: t for t in tomables["esperando"]}
        self.assertEqual(esperando["pq-b"]["incompatible_por"],
                         [{"recurso": "contrato:api/v2/pedidos", "lo_posee": "pq-a"}])
        self.assertEqual(esperando["pq-b"]["espera_a"], ["pq-a"])
        self.assertEqual([e["paquete"] for e in A.elegibles()], ["pq-c"])
        self.assertEqual([i["paquete"] for i in A.incompatibles_por_recurso()], ["pq-b"])
        B = self.rt("w-B")
        with self.assertRaises(paquete_runtime.RecursoOcupado) as cm:
            B.tomar("pq-b")
        self.assertIn("api/v2/pedidos", str(cm.exception))
        self.assertIsNone(B._leer_lease("pq-b"))                 # no retiene el lease
        self.assertEqual(B._leer_paquete("pq-b")["estado"], "listo")
        B.tomar("pq-c")                                          # ámbito independiente: en paralelo
        A.entregar("pq-a", {"estado": "completado", "codigo": 0, "salida": "ok", "detalle": "",
                            "reintentable": False})
        self.assertEqual(A.incompatibles_por_recurso(), [])
        self.assertIn("pq-b", [t["paquete"] for t in A.tomables()["tomables"]])
        toma = A.tomar("pq-b")                                   # el recurso quedó libre al entregar
        self.assertEqual(toma["estado"], "ejecutando")
        self.assertTrue(A.almacen.verificar_integridad().a_dict()["ok"])


# =========================================================================
# T500 · el acoplamiento se declara por ROL, o dos paquetes de la misma capacidad
#        no pueden ser paralelos NUNCA (Directiva §62, §68, §81)
# =========================================================================
class AcoplamientoPorRol(Laboratorio):
    """La llave por CAPACIDAD no basta, y esto lo mide ejecutando.

    Las condiciones 2, 3 y 4 de `a.5` se evalúan por INTERSECCIÓN de los conjuntos
    declarados. Con la llave por capacidad, dos paquetes de la misma capacidad reciben una
    declaración IDÉNTICA: la intersección es el propio conjunto, nunca vacía, y la pareja
    queda secuenciada declare la instancia lo que declare.

    HECHO MEDIDO ANTES DE CORREGIR (2026-09-20, instancia de La Pesquerapp): en el plan de
    `ui-2-nueva-superficie`, once de diecisiete paquetes son `DIS`. Con la dirección
    artística escalada al Owner, la organización no continuaba con NADA —de diecisiete
    paquetes, UNO tomable—, y §81 pide exactamente lo contrario: que el trabajo no bloqueado
    siga mientras el Owner decide.
    """

    def _plan_con(self, A, item, **afinado):
        circuito = self.circuitos["cambio-de-dominio"]        # DOM participa DOS veces
        return oficina.planificar(A, corpus=self.corpus, entrada=self.entrada(),
                                  circuito=circuito, control_repo=self.repo,
                                  item=item, titulo="Entidad nueva", **afinado)["plan"]

    def test_38_la_llave_por_capacidad_no_puede_paralelizar_dos_roles_de_la_misma(self):
        """T500 · Defecto que previene: declarar el acoplamiento y que no sirva de nada."""
        A = self.rt("w-A")
        # CONTROL NEGATIVO · por capacidad, los dos roles de DOM reciben lo MISMO
        por_capacidad = {"DOM": {"escribe_ficheros": ["docs/dominio/entidad.md"],
                                 "integra_en": "rama de trabajo del encargo"}}
        plan = self._plan_con(A, "enc-cap", acoplamiento_por_capacidad=por_capacidad)
        filas = {f["paquete"]: f for f in plan["correspondencia"]}
        dom = [p for p, f in filas.items() if str(f.get("rol") or "").startswith("DOM/")]
        modelo = [p for p in dom if filas[p]["rol"] == "DOM/modelo"][0]
        migracion = [p for p in dom if filas[p]["rol"] == "DOM/migracion"][0]
        depende = set(A._leer_paquete(migracion).get("depende_de") or [])
        self.assertIn(modelo, depende,
                      "con la llave por capacidad la pareja NO puede salir paralela: "
                      "escriben el mismo fichero porque la declaración es la misma")

        # CONTROL POSITIVO · por rol, cada uno declara lo que de verdad escribe
        B = self.rt("w-B")
        por_rol = {
            "DOM/modelo": {"escribe_ficheros": ["docs/dominio/modelo.md"],
                           "integra_en": "rama de trabajo del encargo"},
            "DOM/migracion": {"escribe_ficheros": ["docs/dominio/migracion.md"],
                              "integra_en": "rama de trabajo del encargo"},
        }
        plan2 = self._plan_con(B, "enc-rol", acoplamiento_por_capacidad=por_capacidad,
                               acoplamiento_por_rol=por_rol)
        filas2 = {f["paquete"]: f for f in plan2["correspondencia"]}
        dom2 = [p for p, f in filas2.items() if str(f.get("rol") or "").startswith("DOM/")]
        modelo2 = [p for p in dom2 if filas2[p]["rol"] == "DOM/modelo"][0]
        migracion2 = [p for p in dom2 if filas2[p]["rol"] == "DOM/migracion"][0]
        self.assertEqual(B._leer_paquete(modelo2)["acoplamiento"]["escribe_ficheros"],
                         ["docs/dominio/modelo.md"],
                         "el paquete se queda con la declaración de SU rol, no la de la capacidad")
        self.assertEqual(B._leer_paquete(migracion2)["acoplamiento"]["escribe_ficheros"],
                         ["docs/dominio/migracion.md"])

        # y la sexta condición SIGUE mandando: sin `integra_en` se vuelve a secuenciar,
        # porque declarar por rol no afloja `b.11` — sólo permite decir la verdad
        C = self.rt("w-C")
        sin_estrategia = {k: {"escribe_ficheros": v["escribe_ficheros"]}
                          for k, v in por_rol.items()}
        plan3 = self._plan_con(C, "enc-sin", acoplamiento_por_rol=sin_estrategia)
        filas3 = {f["paquete"]: f for f in plan3["correspondencia"]}
        dom3 = [p for p, f in filas3.items() if str(f.get("rol") or "").startswith("DOM/")]
        migracion3 = [p for p in dom3 if filas3[p]["rol"] == "DOM/migracion"][0]
        modelo3 = [p for p in dom3 if filas3[p]["rol"] == "DOM/modelo"][0]
        self.assertIn(modelo3, set(C._leer_paquete(migracion3).get("depende_de") or []),
                      "sin `integra_en` la sexta condición falla y `b.11` secuencia: "
                      "declarar por rol NO es una autorización de paralelismo")


# =========================================================================
# T501 · los roles CONDICIONALES se pueden activar desde la oficina (§5, §81)
# =========================================================================
class CondicionesDeRol(Laboratorio):
    """Nueve roles del corpus son condicionales y NINGUNO podía entrar en un plan.

    `equipos.materializar` acepta `condiciones_de_rol` y deja fuera, con su motivo, al rol
    «condicional cuya condición no consta verdadera». Pero `oficina.planificar` no exponía el
    parámetro: nadie podía declarar ninguna condición, así que los nueve quedaban SIEMPRE
    fuera —`ARQ/encaje`, `ARQ/diagnostico`, `DIS/movimiento`, `DIS/investigacion-visual`,
    `DIS/investigacion-ux`, `DIS/sistema-de-diseno`, `DIS/critica-visual`,
    `DIS/revision-de-fidelidad` y `SIS/evolucion`—.

    HECHO MEDIDO (2026-09-20, instancia de La Pesquerapp). §81 pide que la síntesis diga
    «Investigamos patrones internos y externos», y ese material lo produce
    `DIS/investigacion-visual`. El plan de `ui-2-nueva-superficie` materializaba dieciséis
    roles y ése no estaba, y no porque la composición lo excluya —lo admite con su condición,
    «el material registrado en 02-REFERENCIAS no cubre la materia de esta superficie»— sino
    porque no había forma de declararla. El diagnóstico inicial fue que la composición estaba
    mal y había que hacer el rol obligatorio; leerla a fondo mostró que lo que faltaba era el
    parámetro, y que hacerlo obligatorio habría forzado investigación redundante cuando el
    material ya existe.
    """

    def test_39_un_rol_condicional_entra_solo_si_su_condicion_se_declara(self):
        """T501 · Defecto que previene: un corpus con roles condicionales que no se activan nunca."""
        # El circuito NO se elige a mano: se busca el primero del PROFILE cuya composicion
        # declare un rol condicional. Escribir aqui un nombre concreto ataria la prueba a un
        # catalogo que cada instancia define a su manera.
        comps = {c["id"]: c for c in self.corpus.de_tipo("composicion")}
        candidatos = []
        for nombre, circ in sorted(self.circuitos.items()):
            for cid in (circ.get("composiciones") or []):
                for entrada in ((comps.get(cid) or {}).get("roles") or []):
                    cond = str(entrada.get("condicion") or "").strip()
                    if cond and not entrada.get("obligatorio"):
                        candidatos.append((nombre, circ, entrada["rol"], cond))
        self.assertTrue(candidatos, "ningun circuito del PROFILE declara un rol condicional")

        # Y de los candidatos se usa el primero que de hecho PLANIFIQUE: algunos circuitos
        # —los de cambio de direccion— exigen un propietario global declarado en la entrada,
        # y eso es otra prueba (T488), no esta.
        # Algunos circuitos —los de cambio de direccion— exigen propietario global y
        # productoras declaradas en la ENTRADA (eso lo cubre T488). Se prueba con la entrada
        # simple y, si no compone, con la enriquecida; lo que esta prueba mide es otra cosa.
        def _entradas():
            yield self.entrada()
            yield dict(self.entrada(), propietario_global="PRD",
                       productores_declarados={"sustituciones-registradas": "PRD"})

        elegido = None
        for nombre, circuito, rol, condicion in candidatos:
            for n_entrada, datos in enumerate(_entradas()):
                A = self.rt("w-A-%s-%d" % (nombre[:6], n_entrada))
                try:
                    sin = oficina.planificar(A, corpus=self.corpus, entrada=datos,
                                             circuito=circuito, control_repo=self.repo,
                                             item="enc-sin-%s-%d" % (nombre[:6], n_entrada),
                                             titulo="Sin condicion")["plan"]
                except Exception:                                        # noqa: BLE001
                    continue
                elegido = (nombre, circuito, rol, condicion, sin, datos)
                break
            if elegido:
                break
        self.assertIsNotNone(elegido, "ningun circuito con rol condicional se pudo planificar")
        nombre, circuito, rol, condicion, sin, datos = elegido
        roles_sin = {f.get("rol") for f in sin["correspondencia"]}
        self.assertNotIn(rol, roles_sin,
                         "sin declarar su condicion, un rol condicional NO entra en el plan")

        B = self.rt("w-B")
        con = oficina.planificar(B, corpus=self.corpus, entrada=datos, circuito=circuito,
                                 control_repo=self.repo, item="enc-con-" + nombre[:8],
                                 titulo="Con condicion", condiciones_de_rol=[condicion])["plan"]
        roles_con = {f.get("rol") for f in con["correspondencia"]}
        self.assertIn(rol, roles_con,
                      "declarada su condicion, el rol condicional SI entra: sin esto los nueve "
                      "roles condicionales del corpus eran inalcanzables desde la oficina")
        self.assertTrue(roles_sin < roles_con,
                        "declarar una condicion solo AÑADE: no cambia los roles que ya estaban")


# =========================================================================
# T504 · ninguna capacidad del corpus queda CALLADA en una ruta (§32)
# =========================================================================
class NingunaCapacidadCallada(Laboratorio):
    """«No se permite silencio» (§32), y cuatro capacidades lo guardaban.

    `a.6` exige que lo no activado deje motivo, y eso se cumplía sólo para las capacidades que
    el proceso contempla con una condición: aparecían en `no_activadas` con «la condición
    `C-X` no consta verdadera». Las demás no aparecían de ninguna forma.

    HECHO MEDIDO (2026-09-21, instancia de La Pesquerapp, encargo `ui-2` real): de las QUINCE
    capacidades del corpus, la ruta nombraba TRECE. `ENC` está declarada en `NUNCA_PARTICIPA`
    y por eso su ausencia es una respuesta; `DSP`, `INV`, `PLT` y `SIS` no estaban ni como
    participantes, ni como no activadas, ni como nunca-participa. Cuatro silencios, del tipo
    exacto que §32 prohíbe con esas palabras.

    Lo encontró la prueba que se escribió para PUBLICAR la ruta: el objeto llevaba el dato
    desde siempre y ninguna orden lo sacaba, así que nadie podía ver lo que faltaba.
    """

    def test_40_toda_capacidad_aparece_o_participando_o_con_su_motivo(self):
        """T504 · Defecto que previene: una capacidad que nunca se evalúa y nadie lo nota."""
        # El encuadre se compone como lo compone la oficina, no a mano: si se inventara aquí
        # la prueba mediría su propia invención. `encuadrar` es la misma puerta que usa
        # `oficina.planificar`.
        from ciclo import encuadre as modulo_encuadre, rutas  # noqa: PLC0415
        circuito = self.circuito
        entrada = dict(self.entrada("que ninguna capacidad se quede callada"))
        entrada.setdefault("materia", circuito["materia"])
        entrada.setdefault("estado_del_objeto", circuito["estado_del_objeto"])
        marco = modulo_encuadre.encuadrar(self.repo, entrada, corpus=self.corpus)
        ruta = rutas.componer(
            marco, corpus=self.corpus,
            condiciones_verdaderas=list(circuito.get("condiciones_de_ruta") or []))
        dichas = {p["capacidad"] for p in ruta["participantes"]}
        dichas |= {p["capacidad"] for p in ruta["no_activadas"]}
        calladas = sorted(c for c in rutas.CAPACIDADES
                          if c not in dichas and c not in rutas.NUNCA_PARTICIPA)
        self.assertEqual(calladas, [],
                         "capacidades sin decir nada de ellas: " + ", ".join(calladas)
                         + ". §32 no permite silencio: o participa, o consta fuera con motivo, "
                           "o está declarada en NUNCA_PARTICIPA")
        sin_motivo = [p["capacidad"] for p in ruta["no_activadas"]
                      if not str(p.get("motivo") or "").strip()]
        self.assertEqual(sin_motivo, [],
                         "no activadas sin motivo: " + ", ".join(sin_motivo))


# =========================================================================
# T506 · la ENTRADA OBLIGATORIA ordena, aunque los dos puedan compartir agente
# =========================================================================
class EsperaPorEntradaObligatoria(Laboratorio):
    """Independencia dice QUIÉN; entrada obligatoria dice CUÁNDO. No son lo mismo.

    HECHO MEDIDO (2026-09-21, La Pesquerapp, encargo `ui-2` real con modelo real). El plan
    ofreció `DIS/prototipado` EN PARALELO con `DIS/diseno-visual`, y el modelo lo DEVOLVIÓ
    citando su propio contrato: «hace ejecutable una dirección ya elegida; no decide forma, la
    ejecuta». Tenía razón. El orden se derivaba sólo de `requiere_independencia`, y
    `DIS/prototipado` la declara **false** —puede compartir agente con diseño visual—, así que
    no había arista.

    Dos roles pueden ser la misma persona y aun así uno va después. Eso es lo que `espera_a`
    añade, y por eso se DECLARA: inferirlo del texto de `entradas` produce ciclos inmediatos
    (catorce roles nombran a otro ahí), que es la trampa de `T499`.
    """

    def test_41_quien_declara_espera_va_despues_aunque_no_exija_independencia(self):
        """T506 · Defecto que previene: prototipar antes de que exista lo que se prototipa."""
        rol = self.corpus.rol("DIS/prototipado")
        self.assertFalse((rol.get("independencia") or {}).get("requiere_independencia"),
                         "esta prueba mide el caso en que NO hay independencia; si el corpus "
                         "cambia y empieza a exigirla, el caso deja de ser el medido")
        espera = [str(x) for x in (rol.get("espera_a") or [])]
        self.assertIn("DIS/diseno-visual", espera,
                      "el contrato de prototipado exige la especificación de diseño visual como "
                      "ENTRADA: sin `espera_a` el plan los pone en paralelo")

        rt = self.rt("w-espera")
        entrada = dict(self.entrada("fundar la dirección visual de la superficie"))
        resultado = oficina.planificar(
            rt, corpus=self.corpus, entrada=entrada,
            circuito=self.circuitos["fundacion-visual"],
            control_repo=self.repo, item="enc-espera", titulo="Espera declarada")
        plan = resultado["plan"] if isinstance(resultado, dict) and "plan" in resultado else resultado
        filas = plan.get("correspondencia") or []
        por_rol = {f.get("rol"): f for f in filas}
        if "DIS/prototipado" not in por_rol or "DIS/diseno-visual" not in por_rol:
            self.skipTest("el circuito de laboratorio no materializa los dos roles: "
                          + ", ".join(sorted(str(f.get("rol")) for f in filas)))
        prototipo = por_rol["DIS/prototipado"]
        visual = por_rol["DIS/diseno-visual"]
        paquetes = {p["id"]: p for p in (plan.get("paquetes") or []) if isinstance(p, dict)}
        espera = (paquetes.get(prototipo["paquete"], {}).get("depende_de")
                  or prototipo.get("depende_de") or [])
        self.assertIn(visual["paquete"], espera,
                      "el paquete de prototipado tiene que ESPERAR al de diseño visual: "
                      "declararon que pueden compartir agente, no que puedan ir a la vez")


# =========================================================================
# T508 · el gate de una materia lo dictamina quien tiene esa materia
# =========================================================================
class QuienDictaminaCadaGate(Laboratorio):
    """`02-NIVELES-DE-TERMINACION.md` asigna cada gate de nivel a un rol. Nadie lo aplicaba.

    HECHO MEDIDO (2026-09-21, `OWN-ADS-0081`, §22 «Construcción no certifica Diseño»). Los
    VEINTICUATRO bloques `ads:gate` del corpus carecían de campo que dijera quién los
    dictamina, y `gates.aplicar` comprobaba dos cosas: revisor ≠ autor, y revisor ∈
    capacidades ∪ roles ∪ {OWNER}. Con eso, `CNS/revision-de-construccion` firmaba
    `gate:excelencia-visual` sin que nada se quejara —no es el autor, y es un rol válido—:
    Construcción certificaba a Diseño. La asignación existía, escrita en la prosa de la
    tabla de niveles, y una asignación que sólo vive en la prosa no la aplica nadie.

    La tabla es la SEDE, y por eso esta prueba la LEE en vez de copiarla: si mañana la tabla
    cambia de dictaminador y el bloque `ads:gate` no, la prueba lo dice con los dos nombres
    delante.
    """

    ROL = re.compile(r"^[A-Z]{3}/[a-z0-9-]+$")

    def asignaciones_de_la_tabla(self):
        """gate -> quien lo dictamina, LEÍDO de `recorrido/02-NIVELES-DE-TERMINACION.md`."""
        ruta = os.path.join(KERNEL, "recorrido", "02-NIVELES-DE-TERMINACION.md")
        with open(ruta, encoding="utf-8") as manejador:
            texto = manejador.read()
        asignaciones = {}
        for linea in texto.split("\n"):
            if "gate:" not in linea:
                continue
            piezas = linea.split()
            for indice, pieza in enumerate(piezas):
                if not pieza.startswith("gate:") or indice + 1 >= len(piezas):
                    continue
                siguiente = piezas[indice + 1].rstrip(",.")
                if self.ROL.match(siguiente):
                    asignaciones[pieza] = siguiente
                elif siguiente == gates.REVISOR_OWNER:
                    asignaciones[pieza] = gates.REVISOR_OWNER
        return asignaciones

    def test_42_cada_gate_de_nivel_declara_el_rol_que_la_tabla_le_asigna(self):
        """T508 · Defecto que previene: una asignación que sólo vive en la prosa."""
        asignaciones = self.asignaciones_de_la_tabla()
        self.assertGreaterEqual(
            len(asignaciones), 5,
            "la tabla de niveles dejó de nombrar dictaminadores reconocibles; esta prueba "
            "mide contra ELLA, así que sin filas no mide nada: " + repr(asignaciones))
        censo = gates.censo(self.corpus)
        discrepancias = []
        for identificador, esperado in sorted(asignaciones.items()):
            if identificador not in censo:
                discrepancias.append(identificador + ": la tabla lo nombra y el censo no lo tiene")
                continue
            declarado = str(censo[identificador].get("dictamina") or "")
            if declarado != esperado:
                discrepancias.append(
                    identificador + ": la tabla dice `" + esperado + "` y el bloque declara `"
                    + (declarado or "(nada)") + "`")
        self.assertEqual(discrepancias, [], "; ".join(discrepancias))

    def test_43_construccion_no_puede_firmar_el_gate_visual_de_diseno(self):
        """T508 · Defecto que previene: un revisor competente en OTRA materia certificando ésta."""
        identificador = "gate:excelencia-visual"
        declarado = gates.gate(identificador, corpus=self.corpus)
        self.assertEqual(declarado.get("dictamina"), "DIS/revision-de-fidelidad")
        comun = {
            "corpus": self.corpus,
            "entrada": {"item": "enc-dictamina", "sobre_item": "enc-dictamina"},
            "evidencia": [str(pieza) for pieza in (declarado.get("evidencia") or [])],
            "comprobaciones_superadas": list(gates.comprobaciones_de(identificador,
                                                                     corpus=self.corpus)),
            "salida": "el nivel validado-visual",
        }

        # EL DEFECTO, tal cual pasaba antes: un rol VÁLIDO, que NO es el autor, de otra
        # capacidad. El mecanismo viejo lo daba por bueno.
        with self.assertRaises(gates.GateFallido) as capturado:
            gates.aplicar(identificador, revisor="CNS/revision-de-construccion",
                          autor="DIS/diseno-visual", **comun)
        self.assertIn("DIS/revision-de-fidelidad", str(capturado.exception))

        # Y la capacidad entera TAMPOCO vale por el rol: `DIS` no es `DIS/revision-de-fidelidad`.
        with self.assertRaises(gates.GateFallido):
            gates.aplicar(identificador, revisor="DIS", autor="CNS", **comun)

        # Control POSITIVO: con el rol que la tabla asigna, el gate se supera. Sin esto la
        # prueba pasaría igual con un mecanismo que rechazara a TODO el mundo.
        dictamen = gates.aplicar(identificador, revisor="DIS/revision-de-fidelidad",
                                 autor="DIS/diseno-visual", **comun)
        self.assertEqual(dictamen["dictamen"], gates.SUPERADO)

    def test_44_el_gate_que_no_declara_dictaminador_se_comporta_como_siempre(self):
        """T508 · Defecto que previene: endurecer de tapadillo los gates que nadie asignó."""
        censo = gates.censo(self.corpus)
        sin_declarar = [i for i, g in sorted(censo.items()) if not g.get("dictamina")]
        self.assertTrue(sin_declarar, "si TODOS declaran dictaminador, este caso no existe")
        identificador = sin_declarar[0]
        declarado = censo[identificador]
        dictamen = gates.aplicar(
            identificador, corpus=self.corpus,
            entrada={"item": "enc-sin-dictamina"},
            evidencia=[str(pieza) for pieza in (declarado.get("evidencia") or [])],
            revisor="VER", autor="CNS",
            comprobaciones_superadas=list(gates.comprobaciones_de(identificador,
                                                                  corpus=self.corpus)),
            salida="lo de siempre")
        self.assertEqual(dictamen["dictamen"], gates.SUPERADO,
                         "`" + identificador + "` no declara dictaminador: tiene que seguir "
                         "comportándose EXACTAMENTE como antes de T508")


# =========================================================================
# T509 · lo que el tablero OFRECE, la oficina lo ENTREGA
# =========================================================================
class ElTableroNoOfreceLoQueNoDa(Laboratorio):
    """El tablero publicaba paquetes de un plan SUPERADO, y `tomar` los rechazaba.

    HECHO REPRODUCIDO (2026-09-21, sobre un clon real de la instancia). Se planifica un
    encargo, se REPLANIFICA, y el tablero sigue ofreciendo en `TOMABLES AHORA` el primer
    paquete del plan viejo. Un trabajador que haga lo que el tablero dice —tomar el primero
    de la lista— recibe `CICLO_INCONSISTENTE: el paquete no está en ningún plan vigente: no
    se toma lo que no tiene rol ni gate`.

    No es un adorno de la vista. El tablero es la sede que le dice a una sesión nueva qué
    puede tomar (`§45`), y el relevo se apoya en ella: si miente, el relevo se estrella en la
    primera orden. Y la causa es la de siempre en este sistema: DOS nociones de «tomable» sin
    nadie que las case. `runtime.tomables()` mira el plano operacional —dependencias y
    leases— y no sabe qué es un plan vigente; `oficina.tomar` exige el plan vigente y no sabe
    qué publicó la vista.

    Lo que esta prueba fija es la propiedad, no la implementación: **lo que el tablero ofrece,
    la oficina lo entrega**. Cómo se consiga es asunto del tablero.
    """

    def test_45_todo_lo_que_el_tablero_ofrece_se_puede_tomar(self):
        """T509 · Defecto que previene: una lista de trabajo que revienta al obedecerla."""
        rt = self.rt("w-tablero")
        primera = oficina.planificar(
            rt, corpus=self.corpus, entrada=self.entrada(), circuito=self.circuito,
            control_repo=self.repo, item="enc-replan", titulo="Exportar CSV")["plan"]
        segunda = oficina.planificar(
            rt, corpus=self.corpus, entrada=self.entrada(), circuito=self.circuito,
            control_repo=self.repo, item="enc-replan", titulo="Exportar CSV",
            generacion=1)["plan"]
        viejos = set(primera["paquetes"]) - set(segunda["paquetes"])
        self.assertTrue(viejos, "sin paquetes que la replanificación deje atrás no hay caso")

        vista = tablero.derivar(rt, corpus=self.corpus)
        ofrecidos = list(vista["tomables"])
        self.assertTrue(ofrecidos, "el tablero tiene que ofrecer algo para que esto mida algo")
        self.assertEqual(
            sorted(set(ofrecidos) & viejos), [],
            "el tablero ofrece paquetes de un plan SUPERADO: " + ", ".join(sorted(set(ofrecidos) & viejos)))

        # Y el control que de verdad importa, porque es el que sufre el trabajador: cada
        # paquete ofrecido se toma de hecho. Comprobar sólo la lista dejaría pasar cualquier
        # otra razón por la que `tomar` se niegue.
        for paquete in ofrecidos:
            with self.subTest(paquete=paquete):
                otro = self.rt("w-toma-" + paquete[-4:])
                toma = oficina.tomar(otro, corpus=self.corpus, paquete=paquete,
                                     circuito=self.circuito)
                self.assertEqual(toma["brief"]["paquete"], paquete)

    def test_46_lo_que_el_tablero_retira_lo_dice_con_su_motivo(self):
        """T509 · Defecto que previene: arreglar la mentira callándose."""
        rt = self.rt("w-tablero-motivo")
        oficina.planificar(rt, corpus=self.corpus, entrada=self.entrada(), circuito=self.circuito,
                           control_repo=self.repo, item="enc-motivo", titulo="Exportar CSV")
        oficina.planificar(rt, corpus=self.corpus, entrada=self.entrada(), circuito=self.circuito,
                           control_repo=self.repo, item="enc-motivo", titulo="Exportar CSV",
                           generacion=1)
        vista = tablero.derivar(rt, corpus=self.corpus)
        retirados = vista.get("tomables_de_plan_superado") or []
        self.assertTrue(retirados,
                        "un paquete que deja de ofrecerse no desaparece en silencio: se publica "
                        "con su motivo, como las capacidades no activadas de la ruta")
        sin_motivo = [r["paquete"] for r in retirados if not str(r.get("motivo") or "").strip()]
        self.assertEqual(sin_motivo, [], "retirados sin motivo: " + ", ".join(sin_motivo))
        texto = tablero.como_texto(vista)
        self.assertIn("plan superado", texto.lower(),
                      "y el que lee el tablero en texto tiene que verlo, no sólo el que lee el JSON")


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
