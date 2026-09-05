#!/usr/bin/env python3
"""test_sesion_nueva — PRUEBA DE HUMO EN SESIÓN NUEVA. Pieza 4 de §6.4 y §6.5. `T223`, `T224`.

    `T223`  los diez pasos de la prueba de humo, en una SESIÓN NUEVA de verdad, y repetidos
            desde una SEGUNDA sesión igual de limpia
    `T224`  la sesión abierta SOBRE UNA FUENTE, con sus CUATRO desenlaces exigidos y
            DISTINTOS, y el NIVEL ALCANZADO **derivado** de las celdas de cobertura

QUÉ SIGNIFICA «SESIÓN NUEVA» AQUÍ, y se comprueba cada cosa en vez de suponerla:

    proceso            `subprocess`, no una función ni un hilo
    memoria y módulos  el intérprete arranca de cero; nada importado sobrevive
    entorno            se CONSTRUYE entero con `env={...}`. La sesión comprueba que su
                       propio `os.environ` es EXACTAMENTE el que se le construyó, y falla
                       si le ha llegado una variable de más
    `cwd`              directorio propio de la sesión, creado para ella
    temporales         espacio de trabajo propio, vacío al arrancar. La sesión lo comprueba

**EL NIVEL NO SE PRESUPONE.** §6.5 dice que el nivel alcanzado NO ES UN CAMPO: se DERIVA de
las celdas de cobertura. Aquí se implementa esa derivación y se publica lo que salga, que es
`compatible` y no `soportado`, porque no existe ninguna celda `certificacion/integrado`.
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
sys.path.insert(0, RAIZ_RUNTIME)

from adaptadores import proyeccion                                   # noqa: E402
from adaptadores.contrato import VERSION_DE_CONTRATO                 # noqa: E402
from gobierno.git import CanalGit                                    # noqa: E402

REMOTO_CANONICO = "git@github.com:organizacion/producto-ads.git"
NOMBRE_DEL_PUNTERO = "ADS-PUNTERO.yml"
VERSION_DE_ADS = "F6"


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
#  §6.5 · el NIVEL ALCANZADO, DERIVADO de las celdas. NO es un campo.
# ===========================================================================
#  La tabla es la de §6.5, traducida a código y evaluada EN ORDEN. La primera fila cuyas
#  celdas estén todas presentes gana; si ninguna, `desconocido`.
#
#  DECISIÓN · la derivación se escribe en el ORDEN de la tabla y se recorre, no se anida
#      Un `if/elif` anidado esconde el orden de prioridad dentro del flujo de control y no
#      se puede publicar en la evidencia. Con la tabla como dato, el informe publica QUÉ
#      fila ganó y QUÉ celdas la sostienen, que es lo que hace auditable el nivel.
SUJETO = "adaptador:transversal/proceso-local"

NIVELES = (
    {
        "nivel": "soportado",
        "autoriza": "el entorno ejecuta ADS con sus garantías",
        "exige": (
            {"aspecto": "aspecto:certificacion/operativo", "estado": "verificado",
             "vigente": True, "con_prueba_de_humo": True},
            {"aspecto": "aspecto:certificacion/integrado", "estado": "verificado",
             "vigente": True},
        ),
    },
    {
        "nivel": "compatible",
        "autoriza": "hay proyección y funciona lo esencial",
        "exige": (
            {"aspecto": "aspecto:certificacion/estructural", "estado": "verificado"},
        ),
    },
    {
        "nivel": "generico",
        "autoriza": "recibe el contrato y las instrucciones universales",
        "exige": (),
    },
)

DESCONOCIDO = {"nivel": "desconocido", "autoriza": "nada", "exige": ()}


def _celda_cumple(celda, exigencia):
    if celda.get("aspecto") != exigencia["aspecto"]:
        return False
    if celda.get("estado") != exigencia["estado"]:
        return False
    if exigencia.get("vigente") and celda.get("vigencia") != "vigente":
        return False
    if exigencia.get("con_prueba_de_humo") and not celda.get("prueba_de_humo_ejecutada"):
        return False
    return True


def derivar_nivel(celdas, sujeto=SUJETO):
    """§6.5: el nivel alcanzado SALE de las celdas. No se escribe, no se declara.

    `desconocido` cuando no hay ninguna celda del sujeto, o cuando TODAS son
    `no-auditado`. Es literal de §6.5, y por eso se comprueba antes de recorrer la tabla:
    si no, `generico` —que no exige ninguna celda— ganaría siempre.
    """
    propias = [celda for celda in celdas if celda.get("sujeto") == sujeto]
    if not propias or all(celda.get("estado") == "no-auditado" for celda in propias):
        return {"nivel": DESCONOCIDO["nivel"], "autoriza": DESCONOCIDO["autoriza"],
                "sostenido_por": [], "sujeto": sujeto,
                "motivo": "ninguna celda del sujeto, o todas `no-auditado`"}
    for fila in NIVELES:
        sostienen = []
        for exigencia in fila["exige"]:
            casada = next((celda for celda in propias
                           if _celda_cumple(celda, exigencia)), None)
            if casada is None:
                sostienen = None
                break
            sostienen.append(casada)
        if sostienen is None:
            continue
        return {
            "nivel": fila["nivel"],
            "autoriza": fila["autoriza"],
            "sujeto": sujeto,
            "sostenido_por": [celda["aspecto"] for celda in sostienen],
            "motivo": "",
        }
    return {"nivel": DESCONOCIDO["nivel"], "autoriza": DESCONOCIDO["autoriza"],
            "sostenido_por": [], "sujeto": sujeto,
            "motivo": "ninguna fila de la tabla de §6.5 tiene sus celdas"}


# ===========================================================================
#  EL GUION DE LA SESIÓN · se escribe FUERA del repositorio y se ejecuta aparte
# ===========================================================================
GUION_DE_SESION = r'''#!/usr/bin/env python3
"""Una SESIÓN NUEVA de ADS. Proceso propio, entorno construido, `cwd` propio.

Ejecuta la PRUEBA DE HUMO de §6.4 —sus diez pasos— y, cuando el modo lo pide, la abre SOBRE
UNA FUENTE: lee el puntero, resuelve el control repo hermano POR IDENTIDAD y opera con él.

LA LÓGICA DE RESOLUCIÓN VIVE AQUÍ, y §6.7 dice que su sitio es el ADAPTADOR, como campo
`resolucion_del_control_repo` de su contrato. Está escrita como la escribiría el adaptador
—estrategia, profundidad, normalización y los cuatro desenlaces— y la petición de integración
del informe lleva el diff exacto para moverla a `adaptadores/`. No se toca `adaptadores/`
desde aquí porque no es zona de escritura de este corte.
"""
import json
import os
import subprocess
import sys

orden = json.loads(sys.argv[1])
sys.path.insert(0, orden["runtime"])

from adaptadores.contrato import VERSION_DE_CONTRATO, Cancelacion
from adaptadores.proceso import AdaptadorDeProcesoLocal
from adaptadores.registro import RegistroDeAdaptadores

informe = {"modo": orden["modo"], "pasos": {}}


def paso(nombre, valor):
    informe["pasos"][nombre] = valor
    return valor


# ---------------------------------------------------------------------------
#  La SESIÓN comprueba que es nueva. No lo supone.
# ---------------------------------------------------------------------------
paso("00-sesion-limpia", {
    "pid_propio": os.getpid() != orden["pid_de_quien_lanza"],
    "cwd": os.getcwd() == os.path.realpath(orden["cwd"]),
    "entorno_exacto": sorted(os.environ) == sorted(orden["entorno_esperado"]),
    "entorno_recibido": sorted(os.environ),
    "espacio_vacio_al_arrancar": sorted(os.listdir(orden["espacio"])) == [],
    "modulos_de_ads_al_arrancar": [n for n in sorted(orden["modulos_al_arrancar"])],
})


# ---------------------------------------------------------------------------
#  LA RESOLUCIÓN DEL CONTROL REPO · §6.7 regla 4
# ---------------------------------------------------------------------------
ENCONTRADO = "LO_ENCUENTRA"
NO_ENCONTRADO = "NO_LO_ENCUENTRA"
NO_SE_PUDO = "NO_SE_PUDO_COMPROBAR"
DOS = "ENCUENTRA_DOS"


def normalizar_remoto(url):
    """Sin credenciales · con y sin `.git` · `ssh` y `https` EQUIVALENTES.

    Sin esta normalización, dos escrituras del MISMO remoto no casan y el descubrimiento
    falla por una diferencia de ortografía, que es lo que §6.7 regla 4 nombra.
    """
    texto = (url or "").strip()
    if not texto:
        return ""
    for prefijo in ("ssh://", "https://", "http://", "git://"):
        if texto.startswith(prefijo):
            texto = texto[len(prefijo):]
            break
    if "@" in texto.split("/", 1)[0]:
        texto = texto.split("@", 1)[1]
    texto = texto.replace(":", "/", 1) if ":" in texto.split("/", 1)[0] else texto
    if texto.endswith(".git"):
        texto = texto[: -len(".git")]
    return texto.rstrip("/").lower()


def leer_puntero(fuente, nombre):
    """El puntero: DATOS y nada más. Si trae conocimiento, se rechaza."""
    ruta = os.path.join(fuente, nombre)
    if not os.path.isfile(ruta):
        return None
    datos = {"componentes": []}
    with open(ruta, encoding="utf-8") as manejador:
        for linea in manejador:
            recorte = linea.strip()
            if not recorte or recorte.startswith("#"):
                continue
            if recorte.startswith("- "):
                datos["componentes"].append(recorte[2:].strip())
                continue
            clave, _, valor = recorte.partition(":")
            clave, valor = clave.strip(), valor.strip()
            if clave == "componentes" and not valor:
                # La cabecera de la lista NO es un escalar vacío: pisarla borraría la
                # lista que las líneas siguientes van a llenar.
                continue
            datos[clave] = valor
    return datos


def _remoto_de(directorio):
    """`(estado, remoto)`. `estado` es `leido`, `no-es-repo` o `impedido`."""
    try:
        entradas = os.listdir(directorio)
    except PermissionError:
        return "impedido", ""
    except OSError:
        return "no-es-repo", ""
    if ".git" not in entradas:
        return "no-es-repo", ""
    proceso = subprocess.run(
        ["git", "-C", directorio, "config", "--get", "remote.origin.url"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LC_ALL": "C",
             "HOME": directorio, "GIT_CONFIG_GLOBAL": os.devnull,
             "GIT_CONFIG_SYSTEM": os.devnull, "GIT_TERMINAL_PROMPT": "0"},
        check=False)
    if proceso.returncode == 128:
        return "impedido", proceso.stderr.decode("utf-8", "replace").strip()
    if proceso.returncode != 0:
        return "no-es-repo", ""
    return "leido", proceso.stdout.decode("utf-8", "replace").strip()


def resolver_control_repo(abierto_en, puntero, *, profundidad_maxima=2):
    """Los CUATRO desenlaces de §6.7, cada uno con su diagnóstico DISTINTO."""
    buscado = normalizar_remoto(puntero.get("remoto_canonico", ""))
    candidatos = []
    impedidos = []
    directorio = os.path.realpath(abierto_en)
    for _ in range(profundidad_maxima):
        padre = os.path.dirname(directorio)
        if padre == directorio:
            break
        try:
            hermanos = sorted(os.listdir(padre))
        except PermissionError as fallo:
            impedidos.append({"directorio": os.path.basename(padre),
                              "causa": fallo.strerror})
            break
        for nombre in hermanos:
            hermano = os.path.join(padre, nombre)
            if not os.path.isdir(hermano) or os.path.realpath(hermano) == directorio:
                continue
            estado, remoto = _remoto_de(hermano)
            if estado == "impedido":
                impedidos.append({"directorio": nombre, "causa": remoto or "sin permiso"})
                continue
            if estado != "leido":
                continue
            if normalizar_remoto(remoto) == buscado and buscado:
                candidatos.append(hermano)
        directorio = padre
    if len(candidatos) > 1:
        return {"desenlace": DOS, "candidatos": [os.path.basename(c) for c in candidatos],
                "diagnostico": ("DOS control repos para el mismo producto: es exactamente "
                                "el defecto que el puntero existe para no crear"),
                "buscado": buscado}
    if len(candidatos) == 1:
        return {"desenlace": ENCONTRADO, "control_repo": candidatos[0],
                "diagnostico": "", "buscado": buscado}
    if impedidos:
        return {"desenlace": NO_SE_PUDO, "impedimentos": impedidos,
                "diagnostico": ("hay directorios que NO SE PUDIERON comprobar: esto no es "
                                "ausencia, es IMPEDIMENTO, y son dos causas distintas"),
                "buscado": buscado}
    return {"desenlace": NO_ENCONTRADO, "diagnostico":
            "no se encontró ningún hermano con el remoto canónico, y NO se adivina",
            "buscado": buscado}


# ---------------------------------------------------------------------------
#  MODO `fuente` · §6.4, la sesión abierta SOBRE UNA FUENTE
# ---------------------------------------------------------------------------
if orden["modo"] == "fuente":
    puntero = leer_puntero(orden["fuente"], orden["nombre_del_puntero"])
    paso("01-puntero", {"leido": puntero is not None,
                        "componentes": (puntero or {}).get("componentes", []),
                        "remoto": (puntero or {}).get("remoto_canonico", "")})
    resolucion = resolver_control_repo(
        orden["fuente"], puntero or {},
        profundidad_maxima=int(orden.get("profundidad_maxima", 2)))
    paso("02-resolucion", {clave: resolucion[clave] for clave in sorted(resolucion)
                           if clave != "control_repo"})
    if resolucion["desenlace"] == ENCONTRADO:
        # OPERA CON ÉL COMO CONTEXTO PRINCIPAL: lo abre y lee su cabeza.
        proceso = subprocess.run(
            ["git", "-C", resolucion["control_repo"], "rev-parse", "--verify", "HEAD"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "LC_ALL": "C",
                 "HOME": resolucion["control_repo"], "GIT_CONFIG_GLOBAL": os.devnull,
                 "GIT_CONFIG_SYSTEM": os.devnull},
            check=False)
        paso("03-contexto-principal", {
            "abierto": proceso.returncode == 0,
            "cabeza": proceso.stdout.decode("ascii", "replace").strip(),
            "nombre": os.path.basename(resolucion["control_repo"]),
        })
    with open(orden["salida"], "w", encoding="utf-8") as manejador:
        manejador.write(json.dumps(informe, sort_keys=True, ensure_ascii=False,
                                   indent=2) + "\n")
    raise SystemExit(0)


# ---------------------------------------------------------------------------
#  MODO `humo` · los DIEZ pasos de §6.4
# ---------------------------------------------------------------------------
# 1 · INSTALAR O DESCUBRIR el adaptador.
registro = RegistroDeAdaptadores()
adaptador = AdaptadorDeProcesoLocal(orden["espacio"])
registro.registrar(adaptador)
elegido = registro.seleccionar(("proceso-local",))
paso("1-descubrimiento", {"identificadores": registro.identificadores(),
                          "elegido": elegido.identificador})

# 2 · CARGAR SU FICHA.
ficha = elegido.ficha().a_dict()
paso("2-ficha", {"campos": sorted(ficha), "identificador": ficha["identificador"]})

# 3 · VERIFICAR VERSIÓN Y CAPACIDADES.
paso("3-version-y-capacidades", {
    "version": ficha["version"],
    "version_esperada": VERSION_DE_CONTRATO,
    "compatible": ficha["version"] == VERSION_DE_CONTRATO,
    "capacidades": sorted(ficha["capacidades"]),
    "cubre_lo_pedido": set(("proceso-local",)).issubset(set(ficha["capacidades"])),
})

# 4 · EJECUTAR UNA OPERACIÓN REAL, y 5 · RECIBIR PROGRESO.
avisos = []
marca = os.path.join(orden["espacio"], "efecto-aplicado.txt")
tarea = {"argumentos": ["sh", "-c",
                        "echo arrancando; echo aplicado >> " + marca + "; echo hecho"]}
resultado = elegido.ejecutar(tarea, efecto=orden["efecto"], limite_segundos=30,
                             progreso=lambda apunte: avisos.append(apunte))
paso("4-operacion-real", {"estado": resultado["estado"], "codigo": resultado["codigo"]})
paso("5-progreso", {"lineas": [apunte["texto"] for apunte in avisos],
                    "numeradas": [apunte["linea"] for apunte in avisos]})

# 6 · OBTENER RESULTADO.
paso("6-resultado", {clave: resultado[clave] for clave in
                     ("estado", "codigo", "salida", "reintentable", "efecto", "repetido")})

# 7 · PRODUCIR RECIBO Y EVIDENCIA.
recibo = elegido.recibo(orden["efecto"])
evidencia = {"adaptador": ficha["identificador"], "ficha": ficha, "recibo": recibo,
             "resultado": paso("6-resultado", informe["pasos"]["6-resultado"])}
with open(orden["evidencia"], "w", encoding="utf-8") as manejador:
    manejador.write(json.dumps(evidencia, sort_keys=True, ensure_ascii=False,
                               indent=2) + "\n")
paso("7-recibo-y-evidencia", {"recibo_cerrado": bool(recibo and recibo.get("cerrado")),
                              "evidencia": os.path.basename(orden["evidencia"]),
                              "evidencia_fuera_del_espacio":
                                  not orden["evidencia"].startswith(orden["espacio"])})

# 8 · COMPROBAR IDEMPOTENCIA. El efecto NO se aplica dos veces.
segunda = elegido.ejecutar(tarea, efecto=orden["efecto"], limite_segundos=30)
with open(marca, encoding="utf-8") as manejador:
    aplicaciones = [linea for linea in manejador.read().splitlines() if linea.strip()]
paso("8-idempotencia", {"repetido": segunda["repetido"],
                        "veces_aplicado": len(aplicaciones),
                        "mismo_estado": segunda["estado"] == resultado["estado"]})

# 9 · CERRAR. El adaptador no deja procesos ni descriptores abiertos.
cancelacion = Cancelacion()
paso("9-cierre", {"cancelacion_disponible": cancelacion.activada() is False,
                  "espacio_al_cerrar": sorted(os.listdir(orden["espacio"]))})

with open(orden["salida"], "w", encoding="utf-8") as manejador:
    manejador.write(json.dumps(informe, sort_keys=True, ensure_ascii=False, indent=2)
                    + "\n")
'''


class BaseDeSesion(unittest.TestCase):
    """Escribe el guion de sesión FUERA del repositorio y sabe lanzar sesiones limpias."""

    def setUp(self):
        self.taller = tempfile.mkdtemp(prefix="ads-sesion-")
        self.addCleanup(self._retirar)
        self.guion = os.path.join(self.taller, "sesion.py")
        with open(self.guion, "w", encoding="utf-8") as manejador:
            manejador.write(GUION_DE_SESION)
        self.contador = 0

    def _retirar(self):
        for carpeta, subcarpetas, ficheros in os.walk(self.taller):
            for nombre in subcarpetas + ficheros:
                try:
                    os.chmod(os.path.join(carpeta, nombre), stat.S_IRWXU)
                except OSError:
                    # Devolver el permiso es best-effort en el desmontaje; `rmtree` con
                    # `ignore_errors` remata, y aquí no hay nada que afirmar.
                    continue
        shutil.rmtree(self.taller, ignore_errors=True)

    def sesion(self, **orden):
        """Abre una SESIÓN NUEVA: proceso, entorno, `cwd` y espacio propios y vacíos."""
        self.contador += 1
        etiqueta = "sesion-" + str(self.contador)
        raiz = os.path.join(self.taller, etiqueta)
        cwd = os.path.join(raiz, "cwd")
        espacio = os.path.join(raiz, "espacio")
        for directorio in (raiz, cwd, espacio):
            os.makedirs(directorio)
        salida = os.path.join(raiz, "informe.json")
        evidencia = os.path.join(raiz, "evidencia.json")
        # EL ENTORNO SE CONSTRUYE ENTERO. Nada de `os.environ`: ni una variable heredada.
        entorno = {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "LC_ALL": "C.UTF-8",
            "LANG": "C.UTF-8",
            "TZ": "UTC",
            "HOME": raiz,
        }
        completa = {
            "runtime": RAIZ_RUNTIME,
            "modo": "humo",
            "espacio": espacio,
            "cwd": cwd,
            "salida": salida,
            "evidencia": evidencia,
            "efecto": "humo-" + etiqueta,
            "pid_de_quien_lanza": os.getpid(),
            "entorno_esperado": sorted(entorno),
            "modulos_al_arrancar": [],
            "nombre_del_puntero": NOMBRE_DEL_PUNTERO,
        }
        completa.update(orden)
        proceso = subprocess.run(
            [sys.executable, self.guion, json.dumps(completa)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=entorno, cwd=cwd, check=False)
        informe = {}
        if os.path.isfile(salida):
            with open(salida, encoding="utf-8") as manejador:
                informe = json.load(manejador)
        return {"proceso": proceso, "informe": informe, "raiz": raiz,
                "espacio": espacio, "cwd": cwd, "evidencia": evidencia,
                "entorno": entorno}


# ===========================================================================
#  T223 · los diez pasos, en una sesión nueva de verdad
# ===========================================================================
class PruebaDeHumo(BaseDeSesion):

    def setUp(self):
        super().setUp()
        self.primera = self.sesion()
        self.assertEqual(self.primera["proceso"].returncode, 0,
                         self.primera["proceso"].stderr.decode())
        self.pasos = self.primera["informe"]["pasos"]

    def test_la_sesion_es_NUEVA_y_lo_comprueba_ella_misma(self):
        """T223 · Defecto que previene: llamar «sesión nueva» a la misma de siempre."""
        limpia = self.pasos["00-sesion-limpia"]
        self.assertTrue(limpia["pid_propio"], "no es un proceso distinto")
        self.assertTrue(limpia["cwd"], "no arrancó en su propio directorio")
        self.assertTrue(limpia["entorno_exacto"],
                        "le llegó una variable de entorno de más: "
                        + str(limpia["entorno_recibido"]))
        self.assertTrue(limpia["espacio_vacio_al_arrancar"],
                        "el espacio de trabajo traía ficheros de otra sesión")

    def test_el_entorno_NO_hereda_nada_de_quien_lanza(self):
        """T223 · Defecto que previene: una variable accidental que cambia el resultado."""
        recibido = set(self.pasos["00-sesion-limpia"]["entorno_recibido"])
        self.assertEqual(recibido, set(self.primera["entorno"]))
        for prohibida in ("PYTHONPATH", "ADS_ADAPTADOR_FALLO", "ADS_ANFITRION_ALMACEN",
                          "GIT_DIR", "VIRTUAL_ENV"):
            self.assertNotIn(prohibida, recibido)

    def test_1_instala_o_descubre_el_adaptador(self):
        """T223 · §6.4 paso 1. Defecto que previene: dar por descubierto lo que nadie buscó."""
        paso = self.pasos["1-descubrimiento"]
        self.assertIn("proceso-local", paso["identificadores"])
        self.assertEqual(paso["elegido"], "proceso-local")

    def test_2_carga_su_ficha(self):
        """T223 · §6.4 paso 2. Defecto que previene: usar un adaptador sin contrato declarado."""
        paso = self.pasos["2-ficha"]
        self.assertEqual(paso["identificador"], "proceso-local")
        for campo in ("capacidades", "idempotencia", "timeout", "cancelacion",
                      "evidencia", "compatibilidad"):
            self.assertIn(campo, paso["campos"])

    def test_3_verifica_version_y_capacidades(self):
        """T223 · §6.4 paso 3. Defecto que previene: hablar con un contrato de otra versión."""
        paso = self.pasos["3-version-y-capacidades"]
        self.assertEqual(paso["version"], VERSION_DE_CONTRATO)
        self.assertTrue(paso["compatible"])
        self.assertTrue(paso["cubre_lo_pedido"])

    def test_4_ejecuta_una_operacion_REAL(self):
        """T223 · §6.4 paso 4. Defecto que previene: un simulacro presentado como ejecución."""
        paso = self.pasos["4-operacion-real"]
        self.assertEqual(paso["estado"], "completado")
        self.assertEqual(paso["codigo"], 0)
        self.assertTrue(os.path.isfile(
            os.path.join(self.primera["espacio"], "efecto-aplicado.txt")))

    def test_5_recibe_progreso(self):
        """T223 · §6.4 paso 5. Defecto que previene: un progreso que sólo existe en la ficha."""
        paso = self.pasos["5-progreso"]
        self.assertIn("arrancando", paso["lineas"])
        self.assertIn("hecho", paso["lineas"])
        self.assertEqual(paso["numeradas"], sorted(paso["numeradas"]))

    def test_6_obtiene_resultado(self):
        """T223 · §6.4 paso 6. Defecto que previene: un resultado sin los campos del contrato."""
        paso = self.pasos["6-resultado"]
        for campo in ("estado", "codigo", "salida", "reintentable", "efecto", "repetido"):
            self.assertIn(campo, paso)
        self.assertFalse(paso["repetido"])

    def test_7_produce_recibo_y_evidencia(self):
        """T223 · §6.4 paso 7. Defecto que previene: una ejecución sin rastro auditable."""
        paso = self.pasos["7-recibo-y-evidencia"]
        self.assertTrue(paso["recibo_cerrado"])
        self.assertTrue(paso["evidencia_fuera_del_espacio"])
        self.assertTrue(os.path.isfile(self.primera["evidencia"]))
        with open(self.primera["evidencia"], encoding="utf-8") as manejador:
            evidencia = json.load(manejador)
        self.assertEqual(evidencia["adaptador"], "proceso-local")
        self.assertTrue(evidencia["recibo"]["cerrado"])

    def test_8_comprueba_idempotencia(self):
        """T223 · §6.4 paso 8. Defecto que previene: aplicar dos veces el mismo efecto."""
        paso = self.pasos["8-idempotencia"]
        self.assertTrue(paso["repetido"])
        self.assertEqual(paso["veces_aplicado"], 1,
                         "el efecto se aplicó más de una vez: la idempotencia no existe")
        self.assertTrue(paso["mismo_estado"])

    def test_9_cierra(self):
        """T223 · §6.4 paso 9. Defecto que previene: cerrar dejando el espacio a medias."""
        paso = self.pasos["9-cierre"]
        self.assertTrue(paso["cancelacion_disponible"])
        self.assertIn("efectos", paso["espacio_al_cerrar"])
        self.assertEqual(self.primera["proceso"].returncode, 0)

    def test_10_se_repite_desde_OTRA_sesion_limpia(self):
        """T223 · §6.4 paso 10. Defecto que previene: un verde que sólo sale la primera vez."""
        segunda = self.sesion()
        self.assertEqual(segunda["proceso"].returncode, 0,
                         segunda["proceso"].stderr.decode())
        pasos = segunda["informe"]["pasos"]
        self.assertNotEqual(segunda["espacio"], self.primera["espacio"])
        self.assertTrue(pasos["00-sesion-limpia"]["espacio_vacio_al_arrancar"])
        self.assertEqual(pasos["4-operacion-real"]["estado"], "completado")
        self.assertTrue(pasos["8-idempotencia"]["repetido"])
        self.assertEqual(pasos["8-idempotencia"]["veces_aplicado"], 1)
        # Y los pasos que NO dependen de la sesión salen idénticos.
        self.assertEqual(pasos["2-ficha"], self.pasos["2-ficha"])
        self.assertEqual(pasos["3-version-y-capacidades"],
                         self.pasos["3-version-y-capacidades"])


# ===========================================================================
#  T224 · la sesión abierta SOBRE UNA FUENTE, y el NIVEL derivado
# ===========================================================================
class SesionSobreUnaFuente(BaseDeSesion):

    def setUp(self):
        super().setUp()
        self.workspace = os.path.join(self.taller, "workspace")
        os.makedirs(self.workspace)
        self.fuente = self._repo("frontend", "https://github.com/organizacion/frontend.git")
        self.control = self._repo("ads", REMOTO_CANONICO)
        self.puntero = self._compilar_puntero(self.fuente)

    def _repo(self, nombre, remoto):
        ruta = os.path.join(self.workspace, nombre)
        os.makedirs(ruta)
        canal = CanalGit(ruta, autor="sesion")
        canal.ejecutar("init", "--quiet", "--initial-branch=canonica")
        with open(os.path.join(ruta, "README.md"), "w", encoding="utf-8") as manejador:
            manejador.write("# " + nombre + "\n")
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "semilla de " + nombre)
        canal.ejecutar("remote", "add", "origin", remoto)
        return ruta

    def _fuentes(self):
        """`SOURCES.toml` del control repo. La lista de componentes se DERIVA de aquí."""
        cuerpo = (
            "schema = 1\n\n"
            "[workspace]\n"
            'layout = "siblings"\n\n'
            "[[sources]]\n"
            'id     = "frontend"\n'
            'remote = "https://github.com/organizacion/frontend.git"\n'
            'path   = "frontend"\n\n'
            "[[components]]\n"
            'id     = "web"\n'
            'source = "frontend"\n'
            'path   = "apps/web"\n\n'
            "[[components]]\n"
            'id     = "api"\n'
            'source = "frontend"\n'
            'path   = "apps/api"\n'
        ).encode("utf-8")
        ruta = os.path.join(self.control, "SOURCES.toml")
        with open(ruta, "wb") as manejador:
            manejador.write(cuerpo)
        return ruta, cuerpo

    def _compilar_puntero(self, fuente):
        """El puntero: GENERADO, con HUELLA, con AVISO, y con la lista DERIVADA."""
        import tomllib
        ruta_de_fuentes, cuerpo_de_fuentes = self._fuentes()
        datos = tomllib.loads(cuerpo_de_fuentes.decode("utf-8"))
        componentes = sorted(entrada["id"] for entrada in datos.get("components", [])
                             if entrada.get("source") == "frontend")
        cuerpo = "\n".join(
            ["remoto_canonico: " + REMOTO_CANONICO,
             "version_del_adaptador: 1",
             "componentes:"]
            + ["  - " + identificador for identificador in componentes])
        texto = proyeccion.compilar(
            adaptador="proceso-local", version_de_ads=VERSION_DE_ADS,
            entradas={"SOURCES.toml": cuerpo_de_fuentes},
            cuerpo=cuerpo,
            origen_canonico="ads/adaptadores/proceso-local/")
        ruta = os.path.join(fuente, NOMBRE_DEL_PUNTERO)
        proyeccion.escribir(ruta, texto)
        canal = CanalGit(fuente, autor="sesion")
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "puntero del adaptador")
        return {"ruta": ruta, "texto": texto, "componentes": componentes,
                "entradas": {"SOURCES.toml": cuerpo_de_fuentes},
                "fuentes": ruta_de_fuentes}

    def abrir_sobre(self, fuente, **extra):
        orden = {"modo": "fuente", "fuente": fuente,
                 "nombre_del_puntero": NOMBRE_DEL_PUNTERO, "profundidad_maxima": 2}
        orden.update(extra)
        return self.sesion(**orden)

    # -- los CUATRO desenlaces, y son DISTINTOS -----------------------------
    def test_desenlace_LO_ENCUENTRA_y_opera_con_el(self):
        """T224 · §6.7 regla 4. Defecto que previene: encontrarlo y no usarlo."""
        sesion = self.abrir_sobre(self.fuente)
        self.assertEqual(sesion["proceso"].returncode, 0,
                         sesion["proceso"].stderr.decode())
        pasos = sesion["informe"]["pasos"]
        self.assertTrue(pasos["01-puntero"]["leido"])
        self.assertEqual(pasos["02-resolucion"]["desenlace"], "LO_ENCUENTRA")
        contexto = pasos["03-contexto-principal"]
        self.assertTrue(contexto["abierto"])
        self.assertEqual(contexto["nombre"], "ads")
        self.assertEqual(len(contexto["cabeza"]), 40)

    def test_desenlace_NO_LO_ENCUENTRA_y_dice_que_buscaba(self):
        """T224 · Defecto que previene: adivinar el control repo cuando no está."""
        shutil.rmtree(self.control)
        sesion = self.abrir_sobre(self.fuente)
        pasos = sesion["informe"]["pasos"]
        self.assertEqual(pasos["02-resolucion"]["desenlace"], "NO_LO_ENCUENTRA")
        self.assertTrue(pasos["02-resolucion"]["buscado"])
        self.assertIn("NO se adivina", pasos["02-resolucion"]["diagnostico"])
        self.assertNotIn("03-contexto-principal", pasos)

    def test_desenlace_NO_SE_PUDO_COMPROBAR_es_DISTINTO_de_la_ausencia(self):
        """T224 · Defecto que previene: `P-08`, dos causas bajo un mismo diagnóstico."""
        # IMPEDIMENTO REAL: el hermano existe y NO se puede inspeccionar.
        opaco = os.path.join(self.workspace, "opaco")
        os.makedirs(os.path.join(opaco, ".git"))
        os.chmod(opaco, 0o000)
        self.addCleanup(os.chmod, opaco, 0o700)
        shutil.rmtree(self.control)
        sesion = self.abrir_sobre(self.fuente)
        resolucion = sesion["informe"]["pasos"]["02-resolucion"]
        self.assertEqual(resolucion["desenlace"], "NO_SE_PUDO_COMPROBAR")
        self.assertTrue(resolucion["impedimentos"])
        self.assertIn("IMPEDIMENTO", resolucion["diagnostico"])

    def test_desenlace_ENCUENTRA_DOS_es_un_error_explicito(self):
        """T224 · Defecto que previene: dos control repos para el mismo producto."""
        gemelo = self._repo("ads-gemelo", REMOTO_CANONICO)
        self.assertTrue(os.path.isdir(gemelo))
        sesion = self.abrir_sobre(self.fuente)
        resolucion = sesion["informe"]["pasos"]["02-resolucion"]
        self.assertEqual(resolucion["desenlace"], "ENCUENTRA_DOS")
        self.assertEqual(len(resolucion["candidatos"]), 2)
        self.assertIn("no crear", resolucion["diagnostico"])

    def test_los_cuatro_desenlaces_son_DISTINTOS_entre_si(self):
        """T224 · Defecto que previene: cuatro nombres para el mismo resultado."""
        desenlaces = []
        desenlaces.append(self.abrir_sobre(self.fuente)["informe"]["pasos"][
            "02-resolucion"]["desenlace"])
        gemelo = self._repo("ads-gemelo", REMOTO_CANONICO)
        desenlaces.append(self.abrir_sobre(self.fuente)["informe"]["pasos"][
            "02-resolucion"]["desenlace"])
        shutil.rmtree(gemelo)
        shutil.rmtree(self.control)
        desenlaces.append(self.abrir_sobre(self.fuente)["informe"]["pasos"][
            "02-resolucion"]["desenlace"])
        opaco = os.path.join(self.workspace, "opaco")
        os.makedirs(os.path.join(opaco, ".git"))
        os.chmod(opaco, 0o000)
        self.addCleanup(os.chmod, opaco, 0o700)
        desenlaces.append(self.abrir_sobre(self.fuente)["informe"]["pasos"][
            "02-resolucion"]["desenlace"])
        self.assertEqual(len(set(desenlaces)), 4, desenlaces)

    # -- el PUNTERO, y lo que NO puede contener -----------------------------
    def test_el_puntero_es_generado_versionado_y_con_huella(self):
        """T224 · §6.7 regla 2. Defecto que previene: un puntero editado a mano."""
        informe = proyeccion.validar_deriva(self.puntero["texto"],
                                            self.puntero["entradas"])
        self.assertEqual(informe["diagnostico"], proyeccion.AL_DIA)
        self.assertIn(proyeccion.AVISO, self.puntero["texto"])
        canal = CanalGit(self.fuente, autor="sesion")
        codigo, salida, _ = canal.ejecutar("ls-tree", "-r", "-z", "--name-only", "HEAD")
        self.assertIn(NOMBRE_DEL_PUNTERO,
                      salida.decode("utf-8").split("\0"))

    def test_un_puntero_editado_a_mano_se_detecta(self):
        """T224 · §6.3. Defecto que previene: fabricar deriva editando la proyección."""
        alterado = self.puntero["texto"].replace(REMOTO_CANONICO, "git@host:otro/repo.git")
        informe = proyeccion.validar_deriva(alterado, self.puntero["entradas"])
        self.assertEqual(informe["diagnostico"], proyeccion.EDITADA_A_MANO)

    def test_el_puntero_no_contiene_conocimiento(self):
        """T224 · §6.7 regla 3. Defecto que previene: copiar el kernel a las fuentes."""
        cuerpo = self.puntero["texto"].lower()
        for prohibido in ("profile", "project", "memoria", "checkpoint", "item",
                          "pack", "prompt", "contrato", "decision"):
            self.assertNotIn(prohibido, cuerpo, "el puntero lleva `" + prohibido + "`")
        self.assertLess(len(self.puntero["texto"].encode("utf-8")), 2048,
                        "el puntero ha crecido: alguien está copiando el kernel otra vez")

    def test_la_lista_de_componentes_se_DERIVA_de_sources(self):
        """T224 · §6.7 regla 3, corregida por `I.1`. Defecto que previene: el campo singular."""
        self.assertEqual(self.puntero["componentes"], ["api", "web"])
        sesion = self.abrir_sobre(self.fuente)
        leidos = sesion["informe"]["pasos"]["01-puntero"]["componentes"]
        self.assertEqual(sorted(leidos), ["api", "web"])
        self.assertGreater(len(leidos), 1,
                           "componente y fuente NO tienen cardinalidad 1:1 obligatoria")

    def test_el_remoto_se_resuelve_por_IDENTIDAD_y_no_por_ruta(self):
        """T224 · §6.7 regla 4. Defecto que previene: dos formas del mismo remoto que no casan."""
        # El control repo declara su remoto en `ssh`; el puntero lo declara igual. Se
        # cambia a la forma `https` SIN `.git` y tiene que seguir casando.
        canal = CanalGit(self.control, autor="sesion")
        canal.ejecutar("remote", "set-url", "origin",
                       "https://usuario:token@github.com/organizacion/producto-ads")
        sesion = self.abrir_sobre(self.fuente)
        resolucion = sesion["informe"]["pasos"]["02-resolucion"]
        self.assertEqual(resolucion["desenlace"], "LO_ENCUENTRA")

    # -- §6.5 · el NIVEL, DERIVADO -----------------------------------------
    def _celdas_medidas(self):
        """Las celdas que ESTE corte puede sostener con evidencia, y ni una más."""
        sesion = self.sesion()
        self.assertEqual(sesion["proceso"].returncode, 0,
                         sesion["proceso"].stderr.decode())
        humo = sesion["informe"]["pasos"]["4-operacion-real"]["estado"] == "completado"
        proyeccion_al_dia = proyeccion.validar_deriva(
            self.puntero["texto"], self.puntero["entradas"])["diagnostico"]
        celdas = [{
            "sujeto": SUJETO,
            "aspecto": "aspecto:certificacion/estructural",
            "estado": "verificado" if proyeccion_al_dia == proyeccion.AL_DIA
                      else "findings-abiertos",
            "vigencia": "vigente",
            "evidencia": "adaptador presente, proyección compilada y huella casada",
        }, {
            "sujeto": SUJETO,
            "aspecto": "aspecto:certificacion/operativo",
            "estado": "verificado" if humo else "findings-abiertos",
            "vigencia": "vigente",
            "prueba_de_humo_ejecutada": humo,
            "evidencia": "prueba de humo en sesión nueva, ejecutada",
        }]
        # NO se emite celda `certificacion/integrado`: exigiría `SOURCES.toml`, CI y
        # permisos certificados, y este corte no los certifica. Inventarla sería
        # exactamente el campo editable que §6.5 retira.
        return celdas, sesion

    def test_el_nivel_se_DERIVA_de_las_celdas_y_no_se_declara(self):
        """T224 · §6.5. Defecto que previene: un adaptador que se declara `soportado`."""
        celdas, _ = self._celdas_medidas()
        derivado = derivar_nivel(celdas)
        self.assertEqual(derivado["nivel"], "compatible")
        self.assertEqual(derivado["sostenido_por"],
                         ["aspecto:certificacion/estructural"])
        self.assertNotEqual(derivado["nivel"], "soportado")

    def test_sin_celda_integrado_NO_se_alcanza_soportado(self):
        """T224 · §6.5. Defecto que previene: llamar `soportado` a lo que no lo es."""
        celdas, _ = self._celdas_medidas()
        aspectos = {celda["aspecto"] for celda in celdas}
        self.assertNotIn("aspecto:certificacion/integrado", aspectos)
        self.assertEqual(derivar_nivel(celdas)["nivel"], "compatible")
        # Y con la celda de `integrado` añadida —que este corte NO tiene— sí saldría
        # `soportado`: la derivación no está atascada, es que le falta la evidencia.
        completas = celdas + [{
            "sujeto": SUJETO, "aspecto": "aspecto:certificacion/integrado",
            "estado": "verificado", "vigencia": "vigente",
            "evidencia": "hipotética, para comprobar que la tabla discrimina",
        }]
        self.assertEqual(derivar_nivel(completas)["nivel"], "soportado")

    def test_una_celda_vencida_BAJA_el_nivel_sola(self):
        """T224 · §6.5 y §9.3. Defecto que previene: un nivel que no caduca."""
        celdas, _ = self._celdas_medidas()
        completas = celdas + [{
            "sujeto": SUJETO, "aspecto": "aspecto:certificacion/integrado",
            "estado": "verificado", "vigencia": "vigente", "evidencia": "hipotética",
        }]
        self.assertEqual(derivar_nivel(completas)["nivel"], "soportado")
        for celda in completas:
            if celda["aspecto"] == "aspecto:certificacion/operativo":
                celda["vigencia"] = "vencido"
        self.assertEqual(derivar_nivel(completas)["nivel"], "compatible")

    def test_sin_ninguna_celda_el_nivel_es_desconocido(self):
        """T224 · §6.5. Defecto que previene: que `generico` gane por no exigir nada."""
        self.assertEqual(derivar_nivel([])["nivel"], "desconocido")
        self.assertEqual(derivar_nivel([
            {"sujeto": SUJETO, "aspecto": "aspecto:certificacion/estructural",
             "estado": "no-auditado"}])["nivel"], "desconocido")

    def test_el_nivel_de_OTRO_sujeto_no_cuenta(self):
        """T224 · §6.5. Defecto que previene: heredar el nivel de otro adaptador."""
        celdas, _ = self._celdas_medidas()
        self.assertEqual(derivar_nivel(celdas, sujeto="adaptador:transversal/otro")["nivel"],
                         "desconocido")


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
