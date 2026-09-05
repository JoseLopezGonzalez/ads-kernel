#!/usr/bin/env python3
"""test_macrocircuitos — la batería de los CUATRO y de su `FASE 0` (`F6`, macrobloque 3, A).

Instancia el `§18` —«Los cuatro macrocircuitos, mapeados a los procesos de `b.16`», que es
su SEDE CANÓNICA—, el `§8.0` y el `§9.6` con su tabla adversarial `X-S1`–`X-S11`.

CINCO REGLAS QUE ESTA BATERÍA SE IMPONE, Y POR QUÉ:

  1. LA TABLA DEL DOCUMENTO SE ANALIZA, NO SE CITA. `T206` lee la tabla de `§18` en
     `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, deriva de ella macrocircuito, fase,
     proceso, propietario y gate, y **falla si el conjunto derivado y la tabla dejan de
     coincidir**. Es la única forma de que la proyección del kernel no envejezca en
     silencio.

  2. LA COMPOSICIÓN DE CADA FASE SE COMPRUEBA CONTRA `b.16`. No basta con que la tabla y el
     dato coincidan: se COMPONE la ruta de cada fase con las condiciones que la fila declara
     y se comprueba que los participantes resultantes son exactamente los que la fila
     nombra. Una fila con un participante que su proceso no admite se ve aquí.

  3. LAS ONCE FILAS ADVERSARIALES SE EJECUTAN. Cada `X-S` tiene su prueba, cada prueba
     comprueba el CÓDIGO del error —no su texto— y cada error declara la fila que instancia.

  4. LA EXCLUSIÓN DE AUTORIDAD SE PRUEBA CON DOS PROCESOS REALES. Dos objetos en el mismo
     intérprete comparten memoria y comparten el `flock` del proceso: una prueba así no
     distingue una autoridad durable de una variable compartida.

  5. LOS CUATRO PASAN POR EL MISMO PUNTO. Se instala un observador en el punto único de
     despacho y se comprueba que las cuatro ejecuciones pasan por él y por ninguno otro.

    python3 kernel/operativo/runtime/pruebas/test_macrocircuitos.py

Sale con 0 si todo pasa. Se ejecuta desde cualquier directorio.
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
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
RUNTIME = os.path.join(RAIZ, "kernel", "operativo", "runtime")
KERNEL = os.path.join(RAIZ, "kernel", "operativo")
ARQUITECTURA = os.path.join(RAIZ, "docs", "evolucion", "11-ARQUITECTURA-INTEGRADA.md")
sys.path.insert(0, RUNTIME)

try:
    import adaptadores
    import ciclo
    import macrocircuitos
    import runtime as paquete_runtime
    from ciclo import durable, gates
    from macrocircuitos import definicion, errores as errores_mc, fase0
except ImportError as exc:
    print(f"no se encuentra el paquete `macrocircuitos` bajo {RUNTIME}: {exc}",
          file=sys.stderr)
    raise

ENTORNO = {
    clave: valor for clave, valor in os.environ.items()
    if clave not in ("ADS_RUNTIME_FALLO", "ADS_ESTADO_FALLO")
}

SEGUNDOS_DE_ESPERA = 240

# Los CUATRO, y las ONCE filas adversariales de `§9.6`. Transcritos para CONFRONTAR.
CUATRO = ("A", "M", "N", "U")
ONCE_FILAS = tuple("X-S" + str(numero) for numero in range(1, 12))

# El nombre con el que la primera columna de `§18` nombra cada macrocircuito.
NOMBRE_EN_LA_TABLA = {
    "N": "N · instalación", "A": "A · adopción", "M": "M · migración",
    "U": "U · actualización",
}

GUION_DE_LA_CARRERA = textwrap.dedent(
    """
    import json, os, sys, time
    sys.path.insert(0, {runtime!r})
    import adaptadores, ciclo, macrocircuitos
    corpus = ciclo.Corpus({kernel!r})
    circuito = macrocircuitos.Macrocircuito(
        {identificador!r}, {repo!r}, corpus=corpus, instancia={instancia!r},
        registro_de_adaptadores=adaptadores.RegistroDeAdaptadores([
            adaptadores.AdaptadorDeProcesoLocal({espacio!r}),
        ]),
    )
    circuito.ejecutar_fase0(comprobaciones_superadas={comprobaciones!r},
                            evidencia=["la salida de los validadores ejecutados"])
    with open({listo!r}, "w", encoding="utf-8") as fichero:
        fichero.write("listo")
    limite = 2000
    while limite and not os.path.exists({salida!r}):
        time.sleep(0.005)
        limite -= 1
    try:
        circuito.abrir()
        veredicto = {{"gano": True, "codigo": None,
                      "macrocircuito": circuito.autoridad["macrocircuito"]}}
    except macrocircuitos.AutoridadIncompatible as error:
        veredicto = {{"gano": False, "codigo": error.codigo,
                      "vigente": error.contexto.get("vigente")}}
    finally:
        circuito.cerrar()
    print(json.dumps(veredicto, sort_keys=True))
    """
)


def analizar_tabla_de_18():
    """La tabla de `§18`, ANALIZADA del documento. Es la sede; esto es su lectura."""
    with open(ARQUITECTURA, "r", encoding="utf-8") as fichero:
        lineas = fichero.read().split("\n")
    inicio = None
    for indice, linea in enumerate(lineas):
        if linea.startswith("| macrocircuito | fase | proceso `b.16` |"):
            inicio = indice + 2               # la cabecera y su separador
            break
    if inicio is None:
        raise AssertionError("no se encuentra la tabla de `§18` en 11-ARQUITECTURA")
    filas, actual = [], None
    for linea in lineas[inicio:]:
        if not linea.startswith("|"):
            break
        celdas = [celda.strip() for celda in linea.strip().strip("|").split(" | ")]
        if len(celdas) < 10:
            continue
        cabeza = celdas[0]
        if cabeza:
            for identificador, nombre in NOMBRE_EN_LA_TABLA.items():
                if nombre in cabeza:
                    actual = identificador
                    break
        if actual is None:
            continue
        fase = celdas[1].replace("*", "").replace("`", "").split(" · ")[0].strip()
        proceso = re.search(r"`(proceso:[A-Z]{3})`", celdas[2])
        gate = re.search(r"`(gate:[a-z-]+)`", celdas[8])
        celda_propietario = celdas[3]
        if "DERIVADO" in celda_propietario:
            propietario = None
        else:
            casado = re.search(r"`([A-Z]{3})`", celda_propietario)
            propietario = casado.group(1) if casado else None
        filas.append({
            "macrocircuito": actual,
            "fase": fase,
            "proceso": proceso.group(1) if proceso else None,
            "propietario": propietario,
            "gate": gate.group(1) if gate else None,
        })
    return filas


class BaseDeMacrocircuitos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.corpus = ciclo.Corpus(KERNEL)
        cls.comprobaciones = [
            comprobacion["id"] for comprobacion in
            gates.gate("gate:sistema-conforme", corpus=cls.corpus)["comprobaciones"]
        ]

    def setUp(self):
        self.repo = tempfile.mkdtemp(prefix="ads-mc-")
        self.espacio = os.path.join(self.repo, "espacio")
        os.makedirs(self.espacio, exist_ok=True)
        self.addCleanup(shutil.rmtree, self.repo, True)

    def registro(self):
        return adaptadores.RegistroDeAdaptadores([
            adaptadores.AdaptadorDeProcesoLocal(self.espacio),
        ])

    def circuito(self, identificador, repo=None, instancia=None):
        return macrocircuitos.Macrocircuito(
            identificador, repo or self.repo, corpus=self.corpus,
            instancia=instancia or ("mc-" + identificador.lower()),
            registro_de_adaptadores=self.registro(),
        )

    def orden(self):
        return {
            capacidad: {
                "adaptador": "proceso-local", "operacion": "ejecutar",
                "argumentos": ["/bin/sh", "-c", "exit 0"], "limite_segundos": 60,
            }
            for capacidad in ciclo.CAPACIDADES
        }

    def fase0_superada(self, circuito, **argumentos):
        return circuito.ejecutar_fase0(
            comprobaciones_superadas=self.comprobaciones,
            evidencia=["la salida de los validadores ejecutados"],
            **argumentos,
        )


# =========================================================================
# T206 · la definición DERIVADA y la tabla de `§18`
# =========================================================================
class DefinicionDerivada(BaseDeMacrocircuitos):

    def test_01_son_exactamente_cuatro_y_los_declara_la_tabla(self):
        """T206 · Defecto que previene: un macrocircuito escrito de memoria.

        Los identificadores del paquete y los de la tabla de `§18` coinciden, y son cuatro.
        """
        self.assertEqual(macrocircuitos.IDENTIFICADORES, CUATRO)
        de_la_tabla = sorted({fila["macrocircuito"] for fila in analizar_tabla_de_18()})
        self.assertEqual(tuple(de_la_tabla), CUATRO)

    def test_02_la_tabla_y_el_conjunto_derivado_coinciden_fila_a_fila(self):
        """T206 · Defecto que previene: que la proyección del kernel envejezca en silencio.

        ES LA PRUEBA QUE EL ENCARGO EXIGE: si la tabla de `§18` y el conjunto derivado dejan
        de coincidir —fase, proceso, propietario o gate—, esta prueba falla. La sede sigue
        siendo `§18`; el paquete es su proyección comprobada.
        """
        de_la_tabla = analizar_tabla_de_18()
        derivadas = []
        for identificador in macrocircuitos.IDENTIFICADORES:
            for una in macrocircuitos.macrocircuito(identificador)["fases"]:
                derivadas.append({
                    "macrocircuito": identificador,
                    "fase": una["fase"],
                    "proceso": una["proceso"],
                    "propietario": una.get("propietario_global"),
                    "gate": una.get("gate"),
                })
        clave = lambda fila: (fila["macrocircuito"], fila["fase"])          # noqa: E731
        self.assertEqual(sorted(de_la_tabla, key=clave), sorted(derivadas, key=clave))

    def test_03_la_secuencia_de_procesos_es_la_que_8_0_escribe(self):
        """T206 · Defecto que previene: una racha de `a.7` calculada sobre otra secuencia.

        El FRENO 3 cuenta rachas de items `SIS` CONSECUTIVOS, y `§8.0` escribe la secuencia
        de cada macrocircuito CON la `FASE 0` dentro. Se DERIVA de las fases y se compara.
        """
        for identificador in macrocircuitos.IDENTIFICADORES:
            derivada = macrocircuitos.secuencia_de_procesos(identificador)
            self.assertEqual(derivada,
                             macrocircuitos.SECUENCIA_DECLARADA_EN_8_0[identificador],
                             identificador)
        # `U` es el único cuya racha `SIS` alcanza TRES, y `§8.0` lo dice: es el caso donde
        # el FRENO 3 llega a evaluarse.
        rachas = {}
        for identificador in macrocircuitos.IDENTIFICADORES:
            mayor = actual = 0
            for proceso in macrocircuitos.secuencia_de_procesos(identificador):
                actual = actual + 1 if proceso == "SIS" else 0
                mayor = max(mayor, actual)
            rachas[identificador] = mayor
        self.assertEqual(rachas, {"N": 3, "A": 2, "M": 2, "U": 3})

    def test_04_cada_fase_compone_su_ruta_y_sus_participantes_son_los_de_18(self):
        """T206 · Defecto que previene: un «participante sin vehículo» en un macrocircuito.

        Se COMPONE la ruta de cada fase con las condiciones que su fila declara y se
        comprueba que las capacidades resultantes son exactamente las de la fila. Es la
        comprobación que `§8.0` llama GATE DE COMPOSICIÓN, aplicada a las trece filas.
        """
        for identificador in macrocircuitos.IDENTIFICADORES:
            circuito = self.circuito(identificador)
            for una in macrocircuitos.macrocircuito(identificador)["fases"]:
                if una["fase"] == macrocircuitos.FASE_0:
                    continue
                declarado = None if una.get("propietario_global") else "PRD"
                compuesta = circuito.componer_fase(
                    una["fase"], propietario_declarado=declarado,
                )
                derivadas = sorted({p["capacidad"]
                                    for p in compuesta["ruta"]["participantes"]})
                esperadas = list(definicion.capacidades_de_la_fase(una))
                if declarado:
                    esperadas = sorted(set(esperadas) | {declarado})
                self.assertEqual(derivadas, esperadas,
                                 (identificador, una["fase"]))

    def test_05_ni_DEU_ni_DEP_ni_AUD_aparecen_nunca_como_capacidades(self):
        """T206 · Defecto que previene: confundir el nombre de un proceso con el de una capacidad.

        Es el modo de fallo que `G1` corrigió. Los tres son PROCESOS de `b.16`; las quince
        capacidades no los incluyen, y `comprobar()` lo verifica fila a fila.
        """
        self.assertEqual(macrocircuitos.comprobar(self.corpus), CUATRO)
        for nombre in ("AUD", "DEU", "DEP"):
            self.assertNotIn(nombre, ciclo.CAPACIDADES)
            self.assertIn("proceso:" + nombre, self.corpus.procesos())
        for identificador in macrocircuitos.IDENTIFICADORES:
            for una in macrocircuitos.macrocircuito(identificador)["fases"]:
                for participante in una["participantes"]:
                    self.assertIn(participante["capacidad"], ciclo.CAPACIDADES)

    def test_06_la_fase_0_es_la_MISMA_en_los_cuatro(self):
        """T206 · Defecto que previene: cuatro implementaciones divergentes de la `FASE 0`.

        Regla 6 de `O17`: el MISMO contrato y el MISMO mecanismo compartido. Las cuatro
        filas coinciden campo a campo, y todas invocan `gate:sistema-conforme`.
        """
        filas = [macrocircuitos.macrocircuito(i)["fases"][0]
                 for i in macrocircuitos.IDENTIFICADORES]
        for fila in filas:
            self.assertEqual(fila["fase"], macrocircuitos.FASE_0)
            self.assertEqual(fila["gate"], macrocircuitos.GATE_DE_FASE_0)
            self.assertEqual(json.dumps(fila, sort_keys=True, ensure_ascii=False),
                             json.dumps(filas[0], sort_keys=True, ensure_ascii=False))
        self.assertIn(macrocircuitos.GATE_DE_FASE_0, self.corpus.gates())

    def test_07_ENC_no_participa_y_SEG_conserva_su_bloqueo_sin_via(self):
        """T206 · Defecto que previene: dar vía a quien el contrato deja fuera de la ruta.

        `ENC` produce el encuadre ANTES de que haya ruta; en la `FASE 0`, `SEG` entra SIN
        VÍA y CONSERVA su bloqueo, que es lo único que `O17` le da.
        """
        for identificador in macrocircuitos.IDENTIFICADORES:
            fila = macrocircuitos.macrocircuito(identificador)["fases"][0]
            participantes = {p["capacidad"] for p in fila["participantes"]}
            self.assertEqual(participantes, {"VER"})
            presencias = {p["quien"]: p["forma"] for p in fila["presencias"]}
            self.assertEqual(presencias["SEG"], "autoridad")
            self.assertEqual(presencias["PLT"], "ejecutor")
            self.assertNotIn("ENC", participantes)


# =========================================================================
# T207 · la `FASE 0`, sus SEIS identificadores y su soporte durable
# =========================================================================
class Fase0(BaseDeMacrocircuitos):

    def test_20_los_seis_identificadores_y_el_nº2_se_acuña_por_huella(self):
        """T207 · Defecto que previene: certificar sin saber qué se certifica.

        Los SEIS de la regla 7, y el nº 2 —el de la EJECUCIÓN— se ACUÑA POR HUELLA del
        disparador y de los otros cinco: cambia el disparador, cambia la huella.
        """
        sujeto = fase0.resolver_sujeto(
            self.repo, disparador="el Owner quiere instalar", corpus=self.corpus,
            evidencia=["la salida de los validadores"],
        )
        self.assertEqual(sorted(sujeto), sorted(fase0.IDENTIFICADORES))
        for identificador in fase0.IDENTIFICADORES:
            self.assertTrue(str(sujeto[identificador]).strip(), identificador)
        self.assertTrue(sujeto["ejecucion_del_macrocircuito"].startswith("ejec-"))
        otro = fase0.resolver_sujeto(
            self.repo, disparador="OTRO disparador", corpus=self.corpus,
            evidencia=["la salida de los validadores"],
        )
        self.assertNotEqual(sujeto["ejecucion_del_macrocircuito"],
                            otro["ejecucion_del_macrocircuito"])
        # Y sobre el MISMO disparador, la misma: repetir da lo mismo, no un segundo.
        repetido = fase0.resolver_sujeto(
            self.repo, disparador="el Owner quiere instalar", corpus=self.corpus,
            evidencia=["la salida de los validadores"],
        )
        self.assertEqual(sujeto, repetido)

    def test_21_el_soporte_durable_esta_fuera_de_estado_y_no_lo_crea(self):
        """T207 · Defecto que previene: escribir en `estado/` antes de que exista.

        La `FASE 0` escribe en su soporte propio —la declaración, su dosier y su celda, y
        NADA del macrocircuito— y `estado/` no existe cuando termina.
        """
        circuito = self.circuito("N")
        resultado = self.fase0_superada(circuito)
        self.assertFalse(os.path.isdir(os.path.join(self.repo, "estado")))
        directorio = fase0.directorio_del_soporte(self.repo, resultado["sujeto"])
        self.assertTrue(os.path.isdir(directorio))
        self.assertEqual(sorted(os.listdir(directorio)),
                         ["celda.json", "declaracion.json", "dosier.json"])
        self.assertEqual(fase0.exigir_soporte_fuera_de_estado(
            self.repo, resultado["sujeto"]), os.path.abspath(directorio))
        # NADA del macrocircuito: la celda no nombra fases, ni items, ni paquetes.
        volcado = json.dumps(resultado["celda"], ensure_ascii=False)
        for palabra in ("INS-0", "paquete", "iniciativa"):
            self.assertNotIn(palabra, volcado)

    def test_22_repetirla_sobre_el_mismo_disparador_da_LA_MISMA_declaracion(self):
        """T207 · Defecto que previene: dos declaraciones cuando el chat se agota dentro.

        `§9.6`: la `FASE 0` NO SE REANUDA, se REPITE ENTERA, y repetirla sobre el mismo
        disparador produce **la MISMA** declaración, con lo que la regla 1 se conserva.
        """
        circuito = self.circuito("N")
        primera = self.fase0_superada(circuito)
        segunda = self.fase0_superada(self.circuito("N"))
        self.assertEqual(primera["declaracion"], segunda["declaracion"])
        self.assertEqual(primera["celda"], segunda["celda"])
        self.assertEqual(fase0.exigir_una_sola(self.repo, "N"), 1)

    def test_23_la_incorporacion_no_reemite_y_conserva_la_huella(self):
        """T207 · Defecto que previene: certificar dos veces lo mismo al abrir `estado/`.

        La primera fase que crea `estado/` INCORPORA la declaración a `estado/cobertura/`
        como primer acto, sin reemitirla, y con la MISMA huella.
        """
        circuito = self.circuito("N")
        resultado = self.fase0_superada(circuito)
        circuito.abrir()
        self.addCleanup(circuito.cerrar)
        celda = fase0.exigir_incorporada(circuito.runtime, resultado)
        self.assertEqual(celda["huella_del_sujeto"],
                         resultado["celda"]["huella_del_sujeto"])
        self.assertFalse(celda["reemitida"])
        self.assertEqual(celda["reside_en"], "estado/cobertura")
        self.assertEqual(celda["incorporada_por"], "N")

    def test_24_el_reparto_de_9_6_se_respeta_y_PLT_exige_pero_no_certifica(self):
        """T207 · Defecto que previene: que el propietario del macrocircuito certifique.

        `SIS` productor y propietario · `VER` el dosier sin apropiarse de la decisión · `PLT`
        la maquinaria · `SEG` el bloqueo · `ENC` no participa.
        """
        circuito = self.circuito("U")
        resultado = self.fase0_superada(circuito)
        self.assertEqual(resultado["declaracion"]["productor"], "SIS")
        self.assertEqual(resultado["dosier"]["productor"], "VER")
        self.assertIn("NO certifica", resultado["dosier"]["nota"])
        self.assertEqual(resultado["dictamen"]["revisor"], "VER")
        self.assertEqual(resultado["dictamen"]["autor"], "SIS")
        # `U5b` tiene a `PLT` como propietario global, y `PLT` no certifica: EXIGE.
        u5b = macrocircuitos.fase("U", "U5b")
        self.assertEqual(u5b["propietario_global"], "PLT")
        with self.assertRaises(errores_mc.ProductorIndebido):
            self.circuito("U", repo=tempfile.mkdtemp(prefix="ads-mc-otro-")
                          ).ejecutar_fase0(productor="PLT",
                                           comprobaciones_superadas=self.comprobaciones)

    def test_25_la_reutilizacion_de_evidencia_exige_todas_las_huellas_identicas(self):
        """T207 · Defecto que previene: presumir vigente lo que sólo se parece.

        Reglas 8, 9 y 10 a la vez: reutilizar evidencia y emitir declaración son cosas
        distintas, y una sola huella distinta invalida la reutilización.
        """
        sujeto = fase0.resolver_sujeto(self.repo, disparador="uno", corpus=self.corpus,
                                       evidencia=["a"])
        igual = dict(sujeto)
        self.assertTrue(fase0.reutilizar_evidencia(igual, sujeto)["reutilizable"])
        distinto = dict(sujeto)
        distinto["revision_del_kernel"] = "sha256:" + "1" * 64
        with self.assertRaises(errores_mc.ReutilizacionInvalida) as capturado:
            fase0.reutilizar_evidencia(distinto, sujeto)
        self.assertEqual(capturado.exception.contexto["difieren"], ["revision_del_kernel"])


# =========================================================================
# T208 · las ONCE filas adversariales `X-S1`–`X-S11`
# =========================================================================
class TablaAdversarial(BaseDeMacrocircuitos):

    def test_40_las_once_filas_tienen_su_codigo_propio(self):
        """T208 · Defecto que previene: probar que «algo falló» en vez de qué falló.

        Cada fila `X-S` tiene una clase de error con su código estable, y el censo de filas
        cubiertas se DERIVA de las clases, no se escribe.
        """
        self.assertEqual(errores_mc.FILAS_CUBIERTAS, ONCE_FILAS)
        self.assertEqual(len(errores_mc.CODIGOS), len(set(errores_mc.CODIGOS)))

    def test_41_X_S1_mutar_sin_fase_0_falla_nombrando_el_circuito_y_la_mutacion(self):
        """T208 · `X-S1` · resultado exigido: FALLA, nombrando el macrocircuito y la mutación.

        La certificación Estructural es PRECONDICIÓN, no un paso recomendado: sin ella la
        primera mutación está prohibida (regla 2 de `O17`).
        """
        circuito = self.circuito("A")
        with self.assertRaises(errores_mc.Fase0Omitida) as capturado:
            circuito.abrir()
        error = capturado.exception
        self.assertEqual(error.codigo, "FASE_0_OMITIDA")
        self.assertEqual(error.contexto["macrocircuito"], "A")
        self.assertIn("estado", error.contexto["mutacion"])
        self.assertEqual(error.contexto["fila_adversarial"], "X-S1")
        self.assertFalse(os.path.isdir(os.path.join(self.repo, "estado")))

    def test_42_X_S2_una_certificacion_copiada_no_vale(self):
        """T208 · `X-S2` · resultado exigido: FALLA. La regla 10 prohíbe copiar y presumir.

        Se toma la declaración de una ejecución y se presenta para otra: se exige la
        declaración propia de ESTA ejecución (regla 9).
        """
        propia = self.fase0_superada(self.circuito("N"))
        ajena = fase0.resolver_sujeto(self.repo, disparador="OTRO", corpus=self.corpus,
                                      evidencia=["a"])
        with self.assertRaises(errores_mc.CertificacionCopiada) as capturado:
            fase0.exigir_declaracion_propia(propia["declaracion"], ajena)
        self.assertEqual(capturado.exception.codigo, "CERTIFICACION_COPIADA")
        self.assertEqual(capturado.exception.contexto["fila_adversarial"], "X-S2")
        with self.assertRaises(errores_mc.CertificacionCopiada):
            fase0.exigir_declaracion_propia(None, propia["sujeto"])

    def test_43_X_S3_una_sola_huella_distinta_invalida_la_reutilizacion(self):
        """T208 · `X-S3` · resultado exigido: FALLA, nombrando el identificador que difiere.

        La regla 8 exige que TODAS las entradas y huellas sigan idénticas: una basta.
        """
        sujeto = fase0.resolver_sujeto(self.repo, disparador="uno", corpus=self.corpus,
                                       evidencia=["a"])
        comparables = [i for i in fase0.IDENTIFICADORES
                       if i != "ejecucion_del_macrocircuito"]
        for identificador in comparables:
            anterior = dict(sujeto)
            anterior[identificador] = "sha256:" + "2" * 64
            with self.assertRaises(errores_mc.ReutilizacionInvalida,
                                   msg=identificador) as capturado:
                fase0.reutilizar_evidencia(anterior, sujeto)
            self.assertEqual(capturado.exception.contexto["difieren"], [identificador])
            self.assertEqual(capturado.exception.contexto["fila_adversarial"], "X-S3")

    def test_44_X_S4_no_se_sube_de_nivel_sin_estructural_vigente_de_esa_ejecucion(self):
        """T208 · `X-S4` · resultado exigido: FALLA por la definición de «NIVEL ALCANZADO».

        Un nivel superior ya `verificado` NO vale como prueba de que Estructural siga
        vigente (regla 4), y una huella de sujeto distinta es OTRO sujeto.
        """
        resultado = self.fase0_superada(self.circuito("M"))
        for nivel in ("operativa", "integrada", "completa"):
            self.assertEqual(
                fase0.exigir_estructural_vigente(resultado["declaracion"],
                                                 resultado["sujeto"], nivel=nivel),
                resultado["declaracion"],
            )
        otro = dict(resultado["sujeto"])
        otro["revision_del_kernel"] = "sha256:" + "3" * 64
        with self.assertRaises(errores_mc.NivelNoAlcanzable) as capturado:
            fase0.exigir_estructural_vigente(resultado["declaracion"], otro,
                                             nivel="integrada")
        self.assertEqual(capturado.exception.codigo, "NIVEL_NO_ALCANZABLE")
        with self.assertRaises(errores_mc.NivelNoAlcanzable):
            fase0.exigir_estructural_vigente(resultado["declaracion"],
                                             resultado["sujeto"], nivel="estructural")

    def test_45_X_S5_si_la_fase_0_falla_no_se_abre_la_iniciativa(self):
        """T208 · `X-S5` · resultado exigido: FALLA. Una iniciativa abierta YA es estado.

        La regla 5 exige BLOQUEAR ANTES de mutar, y la frontera es exacta: no «antes de
        tocar las fuentes».
        """
        resultado = self.fase0_superada(self.circuito("N"))
        fallido = dict(resultado)
        fallido["dictamen"] = dict(resultado["dictamen"])
        fallido["dictamen"]["dictamen"] = gates.NO_SUPERADO
        with self.assertRaises(errores_mc.MutacionAntesDelGate) as capturado:
            fase0.exigir_gate_superado(fallido, macrocircuito="N",
                                       mutacion="abrir la iniciativa")
        self.assertEqual(capturado.exception.codigo, "MUTACION_ANTES_DEL_GATE")
        self.assertEqual(capturado.exception.contexto["fila_adversarial"], "X-S5")
        # Y el camino completo: un gate que no se supera no llega a devolver resultado.
        otro = tempfile.mkdtemp(prefix="ads-mc-fallo-")
        self.addCleanup(shutil.rmtree, otro, True)
        with self.assertRaises(ciclo.GateFallido):
            self.circuito("N", repo=otro).ejecutar_fase0(
                comprobaciones_superadas=self.comprobaciones[:1],
            )
        self.assertFalse(os.path.isdir(os.path.join(otro, "estado")))

    def test_46_X_S6_dos_declaraciones_en_una_misma_ejecucion_fallan(self):
        """T208 · `X-S6` · resultado exigido: FALLA. Exactamente una por ejecución.

        Se escribe a mano una declaración DISTINTA en el soporte de la misma ejecución, y el
        soporte lo rechaza: dos son dos verdades sobre el mismo hecho.
        """
        resultado = self.fase0_superada(self.circuito("N"))
        directorio = fase0.directorio_del_soporte(self.repo, resultado["sujeto"])
        otra = dict(resultado["declaracion"])
        otra["id"] = "dec-falsificada"
        with self.assertRaises(errores_mc.DosDeclaraciones) as capturado:
            fase0._publicar(os.path.join(directorio, fase0.DECLARACION), otra)
        self.assertEqual(capturado.exception.codigo, "DOS_DECLARACIONES")
        self.assertEqual(capturado.exception.contexto["fila_adversarial"], "X-S6")

    def test_47_X_S7_el_propietario_ni_sustituye_a_SIS_ni_puede_no_exigirla(self):
        """T208 · `X-S7` · resultado exigido: FALLA en los DOS casos.

        No puede sustituir a `SIS` y DEBE exigirla: son las dos mitades del mismo reparto, y
        satisfacer una no dispensa de la otra.
        """
        with self.assertRaises(errores_mc.ProductorIndebido) as capturado:
            self.circuito("A").ejecutar_fase0(
                productor="ARQ", comprobaciones_superadas=self.comprobaciones,
            )
        self.assertEqual(capturado.exception.codigo, "PRODUCTOR_INDEBIDO")
        self.assertEqual(capturado.exception.contexto["fila_adversarial"], "X-S7")
        with self.assertRaises(errores_mc.ProductorIndebido):
            self.circuito("A").ejecutar_fase0(
                dosier_de="SIS", comprobaciones_superadas=self.comprobaciones,
            )
        # La segunda mitad: continuar SIN exigirla es `X-S1`, y también falla.
        with self.assertRaises(errores_mc.Fase0Omitida):
            self.circuito("A").abrir()

    def test_48_X_S8_el_veto_de_SEG_no_lo_levanta_nadie(self):
        """T208 · `X-S8` · resultado exigido: FALLA. El veto no lo levantan las otras tres.

        Aunque TODAS las comprobaciones del gate estén superadas, el bloqueo de `SEG` para
        la fase antes de que el gate llegue a dictaminar.
        """
        with self.assertRaises(errores_mc.BloqueoDeSeguridad) as capturado:
            self.circuito("U").ejecutar_fase0(
                comprobaciones_superadas=self.comprobaciones,
                bloqueo_de_seg="la estructura expone una superficie sin autenticar",
            )
        self.assertEqual(capturado.exception.codigo, "BLOQUEO_DE_SEGURIDAD")
        self.assertEqual(capturado.exception.contexto["fila_adversarial"], "X-S8")
        self.assertFalse(os.path.isdir(os.path.join(self.repo, "fase0")))

    def test_49_X_S9_falta_un_identificador_del_sujeto_y_se_dice_cual(self):
        """T208 · `X-S9` · resultado exigido: FALLA, nombrando el que falta.

        La regla 7 es un MÍNIMO, y omitir uno es un fallo del gate, no una simplificación.
        """
        completo = fase0.resolver_sujeto(self.repo, disparador="uno", corpus=self.corpus,
                                         evidencia=["a"])
        for identificador in fase0.IDENTIFICADORES:
            mutilado = dict(completo)
            mutilado.pop(identificador)
            with self.assertRaises(errores_mc.SujetoIncompleto,
                                   msg=identificador) as capturado:
                fase0.exigir_sujeto_completo(mutilado)
            self.assertEqual(capturado.exception.contexto["falta"], identificador)
            self.assertEqual(capturado.exception.contexto["fila_adversarial"], "X-S9")

    def test_50_X_S10_la_fase_0_no_abre_iniciativa_ni_consume_contador(self):
        """T208 · `X-S10` · resultado exigido: FALLA, y es la prueba de que el nº 2 no es el de la iniciativa.

        El identificador nº 2 lo ACUÑA la `FASE 0` por HUELLA: sin abrir nada y sin consumir
        contador. Se comprueba sobre el disco: no hay `estado/`, no hay items, no hay
        contador, y el identificador no tiene la forma `<PREFIJO><n>`.
        """
        resultado = self.fase0_superada(self.circuito("M"))
        ejecucion = resultado["sujeto"]["ejecucion_del_macrocircuito"]
        self.assertFalse(os.path.isdir(os.path.join(self.repo, "estado")))
        self.assertEqual(sorted(os.listdir(self.repo)), ["espacio", "fase0"])
        self.assertNotRegex(ejecucion, r"^[A-Z]+-?\d+$")
        self.assertTrue(ejecucion.startswith("ejec-"))
        # Y si alguien creara `estado/` mientras se resuelve el sujeto, se dice.
        self.assertEqual(errores_mc.IniciativaPrematura.FILA, "X-S10")

    def test_51_X_S11_ni_dentro_de_estado_ni_sin_incorporar_ni_con_otra_huella(self):
        """T208 · `X-S11` · resultado exigido: FALLA en los TRES casos.

        `estado/` nace después de la `FASE 0`; no incorporarla deja el nivel sin sede
        canónica; incorporarla con otra huella es OTRO sujeto.
        """
        circuito = self.circuito("N")
        resultado = self.fase0_superada(circuito)
        # 1 · el soporte NO cae dentro de `estado/`.
        directorio = fase0.exigir_soporte_fuera_de_estado(self.repo, resultado["sujeto"])
        self.assertNotIn(os.path.join(self.repo, "estado"), directorio)
        # 2 · abrir `estado/` sin incorporar.
        rt = paquete_runtime.Runtime(self.repo, instancia="mc-sin-incorporar",
                                     registro_de_adaptadores=self.registro()).abrir()
        self.addCleanup(rt.cerrar)
        with self.assertRaises(errores_mc.IncorporacionInvalida) as capturado:
            fase0.exigir_incorporada(rt, resultado)
        self.assertEqual(capturado.exception.codigo, "INCORPORACION_INVALIDA")
        self.assertEqual(capturado.exception.contexto["fila_adversarial"], "X-S11")
        # 3 · incorporarla con OTRA huella.
        impostora = dict(resultado["celda"])
        impostora["huella_del_sujeto"] = "sha256:" + "4" * 64
        durable.escribir(
            rt.almacen, clase="prueba.celda", motivo="celda con otra huella",
            objetos={"cobertura/" + impostora["id"] + ".json": impostora},
        )
        with self.assertRaises(errores_mc.IncorporacionInvalida):
            fase0.incorporar(rt, resultado, macrocircuito="N")


# =========================================================================
# T209 · los cuatro extremo a extremo, el punto único y la autoridad
# =========================================================================
class ExtremoAExtremo(BaseDeMacrocircuitos):

    def _positivo(self, identificador, repo):
        circuito = self.circuito(identificador, repo=repo,
                                 instancia="mc-" + identificador.lower())
        self.fase0_superada(circuito)
        circuito.abrir()
        try:
            definido = macrocircuitos.macrocircuito(identificador)
            primera = [f for f in definido["fases"]
                       if f["fase"] != macrocircuitos.FASE_0][0]
            declarado = None if primera.get("propietario_global") else "PRD"
            resultado = circuito.ejecutar_fase(
                primera["fase"], orden_por_capacidad=self.orden(),
                propietario_declarado=declarado,
            )
            estado_final = circuito.terminar(
                "completado", motivo="la fase " + primera["fase"] + " quedó despachada",
            )
            return circuito, resultado, estado_final
        finally:
            circuito.cerrar()

    def test_60_los_cuatro_recorren_su_primera_fase_extremo_a_extremo(self):
        """T209 · CASO POSITIVO de los cuatro · Defecto que previene: cuatro caminos distintos.

        Cada macrocircuito: `FASE 0` · abrir con autoridad e incorporación · componer ·
        planificar · despachar · terminar de forma INEQUÍVOCA. El MISMO código para los
        cuatro, parametrizado por su definición.
        """
        for identificador in macrocircuitos.IDENTIFICADORES:
            repo = tempfile.mkdtemp(prefix="ads-mc-" + identificador + "-")
            self.addCleanup(shutil.rmtree, repo, True)
            os.makedirs(os.path.join(repo, "espacio"), exist_ok=True)
            circuito, resultado, estado_final = self._positivo(identificador, repo)
            self.assertTrue(resultado["plan"]["paquetes"], identificador)
            self.assertTrue(resultado["despacho"]["atendidos"], identificador)
            self.assertEqual(estado_final["terminacion"], "completado", identificador)
            self.assertFalse(estado_final["abierto"], identificador)
            self.assertEqual(estado_final["id"], identificador)
            self.assertEqual(list(estado_final["secuencia_de_procesos"]),
                             list(macrocircuitos.SECUENCIA_DECLARADA_EN_8_0[identificador]))
            del circuito

    def test_61_el_caso_negativo_de_los_cuatro_bloquea_antes_de_mutar(self):
        """T209 · CASO NEGATIVO de los cuatro · Defecto que previene: abrir con el gate rojo.

        Con `SEG` bloqueando, ninguno de los cuatro emite declaración ni abre `estado/`: el
        soporte de la `FASE 0` ni siquiera se crea, y no hay nada que deshacer.
        """
        for identificador in macrocircuitos.IDENTIFICADORES:
            repo = tempfile.mkdtemp(prefix="ads-mc-neg-" + identificador + "-")
            self.addCleanup(shutil.rmtree, repo, True)
            circuito = macrocircuitos.Macrocircuito(
                identificador, repo, corpus=self.corpus, instancia="mc-neg",
            )
            with self.assertRaises(errores_mc.BloqueoDeSeguridad, msg=identificador):
                circuito.ejecutar_fase0(
                    comprobaciones_superadas=self.comprobaciones,
                    bloqueo_de_seg="secreto detectado en la estructura",
                )
            self.assertFalse(os.path.isdir(os.path.join(repo, "estado")), identificador)
            self.assertFalse(os.path.isdir(os.path.join(repo, "fase0")), identificador)
            with self.assertRaises(errores_mc.Fase0Omitida, msg=identificador):
                circuito.abrir()

    def test_62_las_cuatro_ejecuciones_pasan_por_el_MISMO_punto_de_despacho(self):
        """T209 · Defecto que previene: cuatro runtimes paralelos disfrazados de uno.

        Regla 6 de `O17`: el MISMO mecanismo compartido. Se instala un observador en el
        punto único y se comprueba que las cuatro ejecuciones pasan por él, con su origen, y
        que ninguna pasa por otro punto.
        """
        vistos = []
        retirar = ciclo.observar(vistos.append)
        self.addCleanup(retirar)
        for identificador in macrocircuitos.IDENTIFICADORES:
            repo = tempfile.mkdtemp(prefix="ads-mc-punto-" + identificador + "-")
            self.addCleanup(shutil.rmtree, repo, True)
            os.makedirs(os.path.join(repo, "espacio"), exist_ok=True)
            self._positivo(identificador, repo)
        self.assertTrue(vistos)
        origenes = {suceso["origen"] for suceso in vistos}
        self.assertEqual(
            origenes,
            {"macrocircuito:" + i for i in macrocircuitos.IDENTIFICADORES},
        )
        for suceso in vistos:
            self.assertEqual(suceso["punto"], ciclo.PUNTO_DE_ENTRADA)

    def test_63_pausa_reanudacion_y_continua_sobre_un_macrocircuito(self):
        """T209 · Defecto que previene: un macrocircuito que no se puede retomar.

        Cada uno debe permitir pausa, reanudación y `Continúa`, y `Continúa` es EL MISMO del
        ciclo: no hay una continuación por macrocircuito.
        """
        circuito = self.circuito("A")
        self.fase0_superada(circuito)
        circuito.abrir()
        self.addCleanup(circuito.cerrar)
        circuito.ejecutar_fase("A0–A1", orden_por_capacidad=self.orden(), despachar=False)
        pausado = circuito.pausar(motivo="presupuesto agotado")
        self.assertEqual(pausado["terminacion"], "pausado")
        reanudado = circuito.reanudar(motivo="el Owner lo retoma")
        self.assertIsNone(reanudado["terminacion"])
        primera = circuito.continuar()
        segunda = circuito.continuar()
        self.assertEqual(primera["huella"], segunda["huella"])
        self.assertTrue(primera["4_seleccionar"]["retoma"])
        terminado = circuito.terminar("escalado", motivo="queda una decisión del Owner")
        self.assertEqual(circuito.estado()["terminacion"], "escalado")
        self.assertIn(terminado["terminacion"], macrocircuitos.TERMINACIONES)

    def test_64_dos_macrocircuitos_no_adquieren_autoridad_incompatible(self):
        """T209 · Defecto que previene: instalar y adoptar el mismo producto a la vez.

        CON DOS PROCESOS REALES, no dos objetos en el mismo intérprete: dos hilos comparten
        el `flock` del proceso y comparten memoria, así que no distinguirían una autoridad
        durable de una variable compartida. Exactamente uno gana; el otro recibe
        `AUTORIDAD_INCOMPATIBLE` y no muta nada.
        """
        # El control repo ya existe: lo que se disputa es la AUTORIDAD, no la fundación.
        cimiento = paquete_runtime.Runtime(
            self.repo, instancia="cimiento", registro_de_adaptadores=self.registro(),
        ).abrir()
        cimiento.cerrar()
        salida = os.path.join(self.repo, "salida.flag")
        procesos, listos = [], []
        for identificador in ("N", "A"):
            listo = os.path.join(self.repo, "listo-" + identificador)
            listos.append(listo)
            guion = GUION_DE_LA_CARRERA.format(
                runtime=RUNTIME, kernel=KERNEL, identificador=identificador,
                repo=self.repo, instancia="mc-" + identificador.lower(),
                espacio=self.espacio, comprobaciones=list(self.comprobaciones),
                listo=listo, salida=salida,
            )
            procesos.append(subprocess.Popen(
                [sys.executable, "-c", guion], env=ENTORNO,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            ))
        try:
            limite = 4000
            while limite and not all(os.path.exists(ruta) for ruta in listos):
                time.sleep(0.005)
                limite -= 1
            self.assertTrue(all(os.path.exists(ruta) for ruta in listos),
                            "los dos procesos no llegaron a la salida")
            with open(salida, "w", encoding="utf-8") as fichero:
                fichero.write("ya")
            veredictos = []
            for proceso in procesos:
                fuera, error = proceso.communicate(timeout=SEGUNDOS_DE_ESPERA)
                self.assertEqual(proceso.returncode, 0,
                                 error.decode("utf-8", "replace"))
                veredictos.append(json.loads(fuera.decode("utf-8").strip()))
        finally:
            for proceso in procesos:
                if proceso.poll() is None:
                    proceso.kill()
        ganadores = [v for v in veredictos if v["gano"]]
        perdedores = [v for v in veredictos if not v["gano"]]
        self.assertEqual(len(ganadores), 1, veredictos)
        self.assertEqual(len(perdedores), 1, veredictos)
        self.assertEqual(perdedores[0]["codigo"], "AUTORIDAD_INCOMPATIBLE")
        self.assertEqual(perdedores[0]["vigente"], ganadores[0]["macrocircuito"])
        # Y el estado durable declara UNA sola autoridad, la del ganador.
        comprobador = paquete_runtime.Runtime(
            self.repo, instancia="comprobador", registro_de_adaptadores=self.registro(),
        ).abrir()
        self.addCleanup(comprobador.cerrar)
        autoridades = comprobador.almacen.listar("autoridad")
        self.assertEqual(len(autoridades), 1, autoridades)
        vigente = comprobador.almacen.leer(autoridades[0])
        self.assertEqual(vigente["macrocircuito"], ganadores[0]["macrocircuito"])


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de `test_runtime.py`, no importado: la batería de los macrocircuitos no puede
    depender de otra batería para poder ejecutarse. La salida se PUBLICA como evidencia.
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
