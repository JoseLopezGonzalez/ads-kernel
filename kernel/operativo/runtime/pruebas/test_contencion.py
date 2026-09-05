#!/usr/bin/env python3
"""test_contencion — batería de `FD-5`, el AISLAMIENTO DE PROCESOS. `T214` a `T216`, `T410`-`T414`.

    `T214`  DETECCIÓN de las capacidades del anfitrión, sonda a sonda y con su motivo
    `T215`  CONTENCIÓN FUERTE: hijo, nieto y bisnieto, los tres haciendo `setsid`, y
            NINGUNO sobrevive a la cancelación ni al timeout
    `T216`  el backend SIMPLE, con su nivel INFERIOR declarado, el bisnieto que SÍ escapa, y
            el FALLO CERRADO cuando la política exige contención fuerte y no la hay
    `T410`  el PROTOCOLO DE PREPARACIÓN: las cuatro generaciones confirman que existen
            ANTES de que se mate nada, y el `killpg` no ocurre hasta entonces
    `T411`  «nunca creado» y «muerto por contención» son veredictos DISTINTOS
    `T412`  la preparación no es una espera: es una condición OBSERVADA
    `T413`  repetición BAJO CARGA, sin intermitencia, con el débil y con el fuerte
    `T414`  `setsid` conservado y MEDIDO: cada generación en su propia sesión

**LA PAREJA `T215`/`T216` ES LA PRUEBA QUE IMPIDE PRESENTAR EL DÉBIL COMO FUERTE.** Con el
backend fuerte no sobrevive nadie; con el simple sobrevive quien se salió del grupo. Si las
dos dieran lo mismo, una de las dos estaría mal escrita.

Todo con procesos REALES: se localizan por su marca en `/proc/<pid>/cmdline` —que es la única
forma de verlos desde fuera de un espacio de nombres de PID— y se comprueban uno a uno con
`os.kill(pid, 0)`.

`G-08` · POR QUÉ LA TAREA YA NO ESPERA, SINO QUE CONFIRMA
--------------------------------------------------------
HECHO REPRODUCIDO ANTES DE CORREGIR. La tarea generacional decía `sleep 0.6` y después
`echo listo`, y la captura de las cuatro generaciones ocurría en ese instante. `T216` exige
que el bisnieto SOBREVIVA al `killpg` del backend débil, y para exigirlo necesita haberlo
CAPTURADO: si a los 0,6 s el bisnieto todavía no existe, la captura sale vacía y la prueba
cae en `assertTrue(capturadas.get("bisnieto"))`. Cae al lado seguro —rojo, no verde—, pero
NO es determinista, y la línea base de `F6` declara «determinismo byte a byte». El revisor 3
lo midió en el gate: su primera corrida dio `35/36` con `contencion` en rojo, y la misma
batería aislada dio `Ran 20 tests · OK`.

Medido aquí antes de tocar nada, con un banco que sólo sustituye esa constante y deja el
resto del código intacto, sobre este mismo anfitrión de veinte núcleos y con carga real
—sesenta quemadores de CPU más sesenta tormentas de `fork`, `loadavg` 98—:

    sleep=0.6   ·  4/15 capturas INCOMPLETAS · {raiz:0, hijo:0, nieto:3, bisnieto:4}

En reposo, las mismas quince salen 0/15. El veredicto de `T216` era función de una
constante, no de un hecho.

EL REMEDIO NO ES UNA ESPERA MÁS LARGA. Una constante mayor mueve la frontera y no la
quita: sigue habiendo una carga a partir de la cual el bisnieto llega tarde. Lo que se pone
en su lugar es un PROTOCOLO DE PREPARACIÓN OBSERVABLE, y tiene dos canales porque las dos
preguntas son distintas:

    canal de EXISTENCIA   cada generación, nada más arrancar, escribe por `stdout` la
                          línea `preparado <generación>`. `stdout` es el descriptor que
                          `setsid` NO cierra y que el ejecutor ya lee línea a línea, de modo
                          que el anuncio llega DESDE DENTRO de cualquier backend —también
                          desde dentro de un contenedor, donde el sistema de ficheros del
                          anfitrión no se ve—. Esa línea es la prueba de que la generación
                          LLEGÓ A EXISTIR, y sobrevive a su muerte: es lo que permite
                          distinguir «muerto por contención» de «nunca creado»
    canal de CONSENSO     cada generación deja además su testigo en un directorio que las
                          cuatro comparten, y la RAÍZ no anuncia `listo` hasta haber
                          observado los tres testigos de sus descendientes. `listo` deja de
                          ser «ha pasado el tiempo que supuse» y pasa a ser «he comprobado
                          que están los tres»

La raíz sondea ese directorio hasta `SONDEOS_DE_PREPARACION` veces y ni una más. El tope no
es una espera: es lo que convierte un NO-SUCESO en un veredicto explícito. Si se agota, la
raíz publica `sin-preparar` con la lista de los testigos que sí encontró, y la prueba falla
diciendo QUIÉN no llegó a existir — que es un fallo distinto, con otro texto y otra causa,
de «sobrevivió a la contención».

DECISIÓN · el número de repeticiones NO sustituye al protocolo
    `T413` repite bajo carga, y repetir es útil: demuestra que la intermitencia medida ya no
    aparece. Pero si el protocolo no estuviera, mil repeticiones verdes seguirían siendo
    compatibles con la carga mil uno. La repetición MIDE; lo que GARANTIZA es que el
    `killpg` no puede ocurrir antes de que las cuatro generaciones hayan confirmado.
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
import re
import shlex
import shutil
import signal
import subprocess
import sys
import tempfile
import unittest

RAIZ_RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ_RUNTIME)

import contencion                                                    # noqa: E402
from adaptadores.contrato import Cancelacion                         # noqa: E402
from contencion import backends, deteccion, politica as modulo_politica  # noqa: E402

SEGUNDOS_DE_LA_TAREA = 90

# --------------------------------------------------------------------------------------
#  El PROTOCOLO DE PREPARACIÓN de `G-08`, declarado como DATO
# --------------------------------------------------------------------------------------
#  Las cuatro generaciones, en el orden en que nacen. La raíz existe por construcción —es el
#  proceso que el ejecutor lanzó—; las otras tres son las que había que esperar y que ahora
#  se CONFIRMAN.
GENERACIONES = ("raiz", "hijo", "nieto", "bisnieto")
DESCENDIENTES = GENERACIONES[1:]

# El vocabulario del canal de `stdout`. Son tres palabras y ninguna es decorativa: la prueba
# decide por ellas, así que se declaran aquí y no se escriben sueltas en cada sitio.
ANUNCIO = "preparado"          # `preparado <generación>` · esta generación EXISTE
LISTO = "listo"                # la raíz OBSERVÓ los tres testigos: se puede matar
SIN_PREPARAR = "sin-preparar"  # la raíz agotó sus sondeos: alguien NO llegó a existir

# Sondeos de la raíz sobre el directorio de testigos, a `INTERVALO_DE_PREPARACION` cada uno.
# Seiscientos por cinco centésimas son treinta segundos de techo. NO es la espera: la espera
# termina en cuanto están los tres testigos, y esto es sólo el punto en el que un no-suceso
# deja de esperarse y se convierte en el veredicto `sin-preparar`. Treinta segundos, y no
# uno, porque el fallo que este tope tiene que distinguir es «no se creó NUNCA», no «tardó»:
# un tope corto volvería a meter la carga del anfitrión en el veredicto, que es justo el
# defecto que `G-08` cierra.
SONDEOS_DE_PREPARACION = 600
INTERVALO_DE_PREPARACION = "0.05"

# Límite del modo `timeout`. Antes eran 2,5 s y el timeout podía vencer ANTES de que las
# generaciones existieran, con lo que la prueba del timeout heredaba la misma intermitencia.
# Ahora es holgado y la prueba comprueba, además, que la preparación se observó ANTES de que
# venciera: si no fue así lo dice con esas palabras y no lo confunde con un fallo de
# contención. Un timeout es, por definición, un plazo; lo que se ha quitado es que el plazo
# decida si la tarea llegó a engendrar lo que la prueba mide.
LIMITE_DEL_TIMEOUT = 12.0

# `T413`, la repetición bajo carga. Ocho pasadas por backend y dos quemadores por núcleo: lo
# bastante para que la intermitencia medida —4 de cada 15— apareciera si siguiera ahí, y lo
# bastante corto para que la batería siga siendo ejecutable en el gate.
REPETICIONES_BAJO_CARGA = 8
QUEMADORES_POR_NUCLEO = 2


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
#  La TAREA GENERACIONAL: hijo, nieto y bisnieto, los tres con `setsid`
# ===========================================================================
#  Cada generación lleva su propia MARCA en la línea de órdenes, y las marcas ANIDAN: la del
#  bisnieto está también en el cuerpo del nieto, del hijo y de la raíz, porque cada capa
#  contiene el texto de la siguiente. Por eso una generación se identifica RESTANDO: los
#  procesos que llevan la marca del nieto y NO la del hijo son los nietos.
#
#  Y cada generación PARTICIPA EN EL PROTOCOLO de `G-08`: nada más arrancar se anuncia por
#  `stdout` y deja su testigo en el directorio compartido, ANTES de engendrar a la siguiente.
#  El orden importa y es éste a propósito: si el anuncio fuera después del engendramiento, un
#  fallo al engendrar dejaría a la generación viva y muda, y el protocolo no sabría si la que
#  falta es ella o su descendiente.
def _capa(marca, interior, segundos, generacion, antes=""):
    cuerpo = (": " + marca + "\n"
              + antes
              + "echo " + ANUNCIO + " " + generacion + "\n"
              + ": > \"$ADS_PREPARACION/" + generacion + "\"\n"
              + interior
              + "sleep " + str(segundos) + "\n")
    return "setsid sh -c " + shlex.quote(cuerpo) + " &\n"


def _espera_observada(sondeos=None):
    """El bucle de la RAÍZ: sondea la condición y para cuando la ve. No es una espera fija.

    Se escribe en `sh` porque tiene que correr DENTRO de la contención, que es donde están
    las generaciones. `condicion` es la conjunción de los tres testigos; el contador existe
    sólo para que un no-suceso termine en `sin-preparar` en vez de colgarse, y `T412`
    comprueba que ese contador no es lo que decide en el camino normal.
    """
    condicion = " && ".join('[ -f "$ADS_PREPARACION/' + g + '" ]' for g in DESCENDIENTES)
    tope = SONDEOS_DE_PREPARACION if sondeos is None else int(sondeos)
    return (
        "preparadas=no\n"
        "sondeo=0\n"
        "while [ \"$sondeo\" -lt " + str(tope) + " ]; do\n"
        "  if " + condicion + "; then preparadas=si; break; fi\n"
        "  sondeo=$((sondeo+1))\n"
        "  sleep " + INTERVALO_DE_PREPARACION + "\n"
        "done\n"
        "if [ \"$preparadas\" = si ]; then\n"
        "  echo " + LISTO + " " + " ".join(DESCENDIENTES) + " sondeos=$sondeo\n"
        "else\n"
        "  echo " + SIN_PREPARAR + " testigos=$(ls \"$ADS_PREPARACION\" 2>/dev/null "
        "| tr '\\n' ',') sondeos=$sondeo\n"
        "fi\n"
    )


def directorio_de_preparacion(prefijo):
    """Dónde dejan su testigo las cuatro generaciones, VISTO DESDE DENTRO de la contención.

    `${TMPDIR:-/tmp}` y no el espacio de trabajo: el backend de contenedor no monta el
    espacio del anfitrión, y el `cwd` que `Popen` fija es el del cliente `docker`, no el de
    dentro. `/tmp` existe y es escribible en las cuatro contenciones, y el protocolo tiene
    que funcionar en las cuatro o no es el protocolo.
    """
    return "${TMPDIR:-/tmp}/" + prefijo + ".preparacion"


def tarea_generacional(prefijo, segundos=SEGUNDOS_DE_LA_TAREA):
    """`sh` que engendra hijo, nieto y bisnieto y anuncia `listo` CUANDO los ha confirmado.

    Ya no hay ninguna espera temporal aquí. `T412` lo comprueba sobre el texto de la propia
    tarea, que es donde estaba el defecto.
    """
    bisnieto = _capa(prefijo + "-BISNIETO", "", segundos, "bisnieto")
    nieto = _capa(prefijo + "-NIETO", bisnieto, segundos, "nieto")
    hijo = _capa(prefijo + "-HIJO", nieto, segundos, "hijo")
    guion = (": " + prefijo + "-RAIZ\n"
             + "ADS_PREPARACION=\"" + directorio_de_preparacion(prefijo) + "\"\n"
             + "export ADS_PREPARACION\n"
             + "mkdir -p \"$ADS_PREPARACION\" || { echo " + SIN_PREPARAR
             + " testigos= sondeos=0; exit 97; }\n"
             + "echo " + ANUNCIO + " raiz\n"
             + ": > \"$ADS_PREPARACION/raiz\"\n"
             + hijo
             + _espera_observada()
             + "sleep " + str(segundos) + "\n")
    return ["sh", "-c", guion]


def tarea_sin_una_generacion(prefijo, ausente, segundos=SEGUNDOS_DE_LA_TAREA,
                             sondeos=None):
    """La misma tarea con UNA generación amputada. Es el control sano de `T411`.

    Sin ella, «el protocolo detecta al que no llegó a existir» sería una afirmación sobre un
    caso que nunca ocurre. Aquí ocurre a propósito: la capa `ausente` no se engendra, su
    anuncio nunca sale y su testigo nunca aparece, de modo que la raíz agota sus sondeos y
    publica `sin-preparar`.
    """
    if ausente not in DESCENDIENTES:
        raise ValueError("`ausente` es una de " + str(DESCENDIENTES))
    interior = ""
    for generacion in ("bisnieto", "nieto", "hijo"):
        if generacion == ausente:
            # Se amputa ESTA capa y todo lo que colgaba de ella: un nieto sin hijo que lo
            # engendre tampoco nace, y el protocolo tiene que nombrar a los dos.
            interior = ""
            continue
        interior = _capa(prefijo + "-" + generacion.upper(), interior, segundos,
                         generacion)
    guion = (": " + prefijo + "-RAIZ\n"
             + "ADS_PREPARACION=\"" + directorio_de_preparacion(prefijo) + "\"\n"
             + "export ADS_PREPARACION\n"
             + "mkdir -p \"$ADS_PREPARACION\"\n"
             + "echo " + ANUNCIO + " raiz\n"
             + ": > \"$ADS_PREPARACION/raiz\"\n"
             + interior
             + _espera_observada(sondeos=sondeos)
             + "sleep " + str(segundos) + "\n")
    return ["sh", "-c", guion]


def tarea_con_generacion_lenta(prefijo, lenta, retardo, segundos=SEGUNDOS_DE_LA_TAREA):
    """La misma tarea, con UNA generación que tarda `retardo` segundos en anunciarse.

    Es el control positivo de `T412` y la demostración de que la espera murió: con
    `retardo` MUY por encima de los 0,6 s que la tarea esperaba antes, la raíz sigue sin
    anunciar `listo` hasta que la generación lenta deja su testigo. Con la constante
    anterior, esta misma tarea habría capturado una generación vacía.
    """
    if lenta not in DESCENDIENTES:
        raise ValueError("`lenta` es una de " + str(DESCENDIENTES))
    interior = ""
    for generacion in ("bisnieto", "nieto", "hijo"):
        espera = ("sleep " + str(retardo) + "\n") if generacion == lenta else ""
        interior = _capa(prefijo + "-" + generacion.upper(), interior, segundos,
                         generacion, antes=espera)
    guion = (": " + prefijo + "-RAIZ\n"
             + "ADS_PREPARACION=\"" + directorio_de_preparacion(prefijo) + "\"\n"
             + "export ADS_PREPARACION\n"
             + "mkdir -p \"$ADS_PREPARACION\"\n"
             + "echo " + ANUNCIO + " raiz\n"
             + ": > \"$ADS_PREPARACION/raiz\"\n"
             + interior
             + _espera_observada()
             + "sleep " + str(segundos) + "\n")
    return ["sh", "-c", guion]


def generaciones(prefijo):
    """`{raiz, hijo, nieto, bisnieto}` con los PID del ANFITRIÓN de cada generación."""
    raiz = set(contencion.pids_con_marca(prefijo + "-RAIZ"))
    con_hijo = set(contencion.pids_con_marca(prefijo + "-HIJO"))
    con_nieto = set(contencion.pids_con_marca(prefijo + "-NIETO"))
    con_bisnieto = set(contencion.pids_con_marca(prefijo + "-BISNIETO"))
    return {
        "raiz": sorted(raiz),
        "hijo": sorted(con_hijo - raiz),
        "nieto": sorted(con_nieto - con_hijo),
        "bisnieto": sorted(con_bisnieto - con_nieto),
    }


def sesion_de(pid):
    """El identificador de SESIÓN de un PID del anfitrión, leído de `/proc/<pid>/stat`.

    Es lo que `setsid` cambia, y por eso es lo que hay que mirar para no CREER que las
    generaciones se salieron del grupo: el campo 6 de `stat`, contando desde 1, después del
    nombre entre paréntesis —que puede llevar espacios, y por eso se corta por el último
    `)` y no por el primer espacio—.
    """
    try:
        with open("/proc/" + str(int(pid)) + "/stat", encoding="ascii") as manejador:
            crudo = manejador.read()
    except OSError:
        return None
    cola = crudo.rsplit(")", 1)[-1].split()
    # `cola[0]` es el estado; el `pgid` es `cola[2]` y la sesión `cola[3]`.
    if len(cola) < 4:
        return None
    return cola[3]


class BaseDeContencion(unittest.TestCase):
    """Espacio de trabajo temporal, marca única por prueba y remate de supervivientes."""

    def setUp(self):
        self.espacio = tempfile.mkdtemp(prefix="ads-cont-")
        self.addCleanup(shutil.rmtree, self.espacio, ignore_errors=True)
        self.prefijo = "ADSFD5" + os.urandom(6).hex().upper()
        self.addCleanup(self._rematar)
        self.addCleanup(self._retirar_testigos)
        self.capacidades = contencion.capacidades()
        # Lo que el PROTOCOLO de `G-08` deja por escrito de la corrida en curso. Se reinicia
        # aquí y no en `_correr` porque `T413` corre varias veces dentro de una prueba y
        # necesita el acumulado de la última.
        self.anunciadas = set()
        self.linea_de_preparacion = None
        self.salida_de_la_tarea = []
        self.sesiones = {}

    def _rematar(self):
        """Ningún superviviente de una prueba sobrevive a la batería. Ni uno."""
        for pid in contencion.pids_con_marca(self.prefijo):
            try:
                os.kill(pid, signal.SIGKILL)
            except OSError:
                # Ya no está, o no es nuestro. En los dos casos no hay nada que rematar.
                continue

    def _retirar_testigos(self):
        """El directorio de testigos vive fuera del espacio de trabajo: se retira aparte.

        Vive fuera porque tiene que ser visible desde DENTRO de cualquier backend, y el
        espacio del anfitrión no lo es dentro de un contenedor. Lo que se limpia aquí es el
        del anfitrión; el que quede dentro de un contenedor muere con él.
        """
        raiz = os.environ.get("TMPDIR") or "/tmp"
        shutil.rmtree(os.path.join(raiz, self.prefijo + ".preparacion"),
                      ignore_errors=True)

    # ------------------------------------------------------ el PROTOCOLO, del lado de fuera
    def _progreso_del_protocolo(self, capturadas, cancelacion, modo):
        """El lector del canal de `stdout`. Es la mitad del protocolo que vive aquí.

        Tres líneas y ninguna más: `preparado <generación>` acumula EXISTENCIA, `listo`
        dispara la captura y la muerte, y `sin-preparar` se guarda para que el veredicto
        pueda decir QUIÉN no llegó a existir.
        """

        def progreso(apunte):
            texto = apunte["texto"].strip()
            self.salida_de_la_tarea.append(texto)
            if texto.startswith(ANUNCIO + " "):
                self.anunciadas.add(texto.split(None, 1)[1].strip())
                return
            if texto.startswith(SIN_PREPARAR):
                self.linea_de_preparacion = texto
                return
            if not texto.startswith(LISTO) or capturadas:
                return
            self.linea_de_preparacion = texto
            # AQUÍ, y sólo aquí, consta que las cuatro generaciones existen: la raíz ha
            # OBSERVADO los tres testigos antes de escribir esta línea. La captura y la
            # muerte van después, en este mismo instante lógico.
            capturadas.update(generaciones(self.prefijo))
            # Y la SESIÓN de cada una se lee AQUÍ y no después: después de matar no hay
            # `/proc/<pid>/stat` que leer, y el resultado de `setsid` —que es lo que
            # distingue este montaje de uno que no probara nada— se habría perdido.
            self.sesiones = {
                generacion: sorted({sesion_de(pid) for pid in pids} - {None})
                for generacion, pids in capturadas.items()
            }
            if modo == "cancelacion":
                cancelacion.activar()

        return progreso

    def exigir_preparacion(self, capturadas):
        """El veredicto del protocolo, ANTES de juzgar la contención. `G-08`.

        Separa las dos preguntas que la prueba anterior mezclaba en un solo `assertTrue`:

            ¿LLEGARON A EXISTIR?   lo dice el canal de anuncios, que sobrevive a la muerte
            ¿SE LAS VIO A TIEMPO?  lo dice la captura por `/proc`, en el instante de `listo`

        Un fallo aquí NUNCA es «sobrevivió a la contención»: es el protocolo diciendo que la
        tarea no engendró lo que la prueba dice medir, y lo dice con esas palabras.
        """
        if self.linea_de_preparacion is None:
            self.fail("la tarea no llegó a publicar ni `" + LISTO + "` ni `" + SIN_PREPARAR
                      + "`: el protocolo de preparación no llegó a cerrarse. Anunciaron su "
                        "existencia: " + str(sorted(self.anunciadas)) + ". Salida de la "
                        "tarea: " + str(self.salida_de_la_tarea))
        if self.linea_de_preparacion.startswith(SIN_PREPARAR):
            nunca = [g for g in GENERACIONES if g not in self.anunciadas]
            self.fail("NUNCA CREADO(S): " + str(nunca) + ". La raíz agotó sus sondeos sin "
                      "ver los tres testigos y publicó «" + self.linea_de_preparacion
                      + "». Esto NO es «muerto por contención»: es que la tarea no engendró "
                        "lo que esta prueba dice medir")
        self.assertEqual(sorted(self.anunciadas), sorted(GENERACIONES),
                         "el canal de anuncios no vio a las cuatro generaciones y la raíz "
                         "sin embargo dijo `" + LISTO + "`: los dos canales del protocolo "
                         "discrepan, y eso es un defecto del protocolo, no de la contención")
        for generacion in GENERACIONES:
            self.assertTrue(
                capturadas.get(generacion),
                "el " + generacion + " ANUNCIÓ que existía y no se le capturó ningún PID "
                "del anfitrión en el instante de `" + LISTO + "`: no es contención, es que "
                "la observación por `/proc` no le vio")

    def _correr(self, backend, nivel, *, modo, limite=25.0, tarea=None):
        """Lanza la tarea generacional y devuelve `(resultado, generaciones capturadas)`.

        `modo` es `cancelacion` o `timeout`. En los dos casos las generaciones se capturan
        DESDE DENTRO del progreso, cuando la tarea anuncia `listo` — que ya no es «tras
        `sleep 0.6`» sino «tras haber observado los tres testigos», que es la corrección de
        `G-08`.
        """
        cancelacion = Cancelacion()
        capturadas = {}
        self.anunciadas = set()
        self.linea_de_preparacion = None
        self.salida_de_la_tarea = []
        self.sesiones = {}

        resultado = contencion.ejecutar(
            tarea if tarea is not None else tarea_generacional(self.prefijo),
            espacio=self.espacio,
            limite_segundos=limite if modo == "cancelacion" else LIMITE_DEL_TIMEOUT,
            politica=contencion.Politica(nivel, backend=backend),
            marca=self.prefijo,
            progreso=self._progreso_del_protocolo(capturadas, cancelacion, modo),
            cancelacion=cancelacion if modo == "cancelacion" else None,
            capacidades=self.capacidades,
        )
        return resultado, capturadas


# ===========================================================================
#  T214 · DETECCIÓN de capacidades del anfitrión
# ===========================================================================
class DeteccionDeCapacidades(BaseDeContencion):

    def test_se_sondean_todos_los_backends_del_orden_declarado(self):
        """T214 · Defecto que previene: elegir un backend sin haber mirado los demás."""
        sondeados = [fila["backend"] for fila in self.capacidades["backends"]]
        self.assertEqual(sondeados, list(deteccion.ORDEN_DE_PREFERENCIA))

    def test_cada_sonda_publica_su_motivo(self):
        """T214 · Defecto que previene: un «no disponible» sin causa, que nadie puede corregir."""
        for fila in self.capacidades["backends"]:
            with self.subTest(backend=fila["backend"]):
                self.assertTrue(fila["motivo"])
                self.assertIn(fila["nivel"], deteccion.NIVELES)

    def test_el_nivel_de_cada_backend_es_del_vocabulario_cerrado(self):
        """T214 · Defecto que previene: inventar un nivel intermedio que no significa nada."""
        for identificador, clase in backends.CLASES.items():
            with self.subTest(backend=identificador):
                self.assertIn(clase.nivel, deteccion.NIVELES)
                self.assertEqual(clase.nivel,
                                 deteccion.NIVEL_POR_BACKEND[identificador])

    def test_la_sonda_de_cgroup_ejerce_el_mismo_envoltorio_que_el_backend(self):
        """T214 · Defecto que previene: sondear una vía distinta de la que después se usa."""
        instancia = None
        if deteccion.raiz_delegada() is not None:
            instancia = backends.CgroupV2(espacio=self.espacio)
            envoltura = instancia.envolver(["sh", "-c", "true"])
            self.assertIn(deteccion.GUION_DE_MIGRACION, envoltura)
            instancia.limpiar()
        else:
            self.skipTest("este anfitrión no delega ningún subárbol de `cgroup2`")

    def test_la_deteccion_no_descarga_imagenes_de_contenedor(self):
        """T214 · Defecto que previene: que la disponibilidad dependa de la red."""
        fila = [f for f in self.capacidades["backends"]
                if f["backend"] == "contenedor"][0]
        if fila["disponible"]:
            self.assertIn(fila["evidencia"]["imagen"], deteccion.IMAGENES_ACEPTADAS)
        else:
            self.assertTrue(fila["motivo"])

    def test_el_backend_simple_siempre_esta_disponible_y_con_nivel_inferior(self):
        """T214 · Defecto que previene: quedarse sin vía cuando no hay contención fuerte."""
        fila = [f for f in self.capacidades["backends"] if f["backend"] == "simple"][0]
        self.assertTrue(fila["disponible"])
        self.assertEqual(fila["nivel"], deteccion.GRUPO_DE_PROCESOS)
        self.assertIn("setsid", fila["motivo"])


# ===========================================================================
#  T215 · CONTENCIÓN FUERTE
# ===========================================================================
class ContencionFuerte(BaseDeContencion):

    def _comprobar_generacional(self, backend, modo):
        resultado, capturadas = self._correr(
            backend, deteccion.ARBOL_DE_PROCESOS, modo=modo)
        self.assertEqual(resultado.nivel_de_aislamiento, deteccion.ARBOL_DE_PROCESOS)
        self.assertEqual(resultado.backend, backend)
        self.assertEqual(resultado.estado,
                         "cancelado" if modo == "cancelacion" else "timeout")
        # PRIMERO el protocolo, DESPUÉS la contención. En ese orden y no en el otro: si la
        # descendencia no llegó a existir, cualquier cosa que se diga después sobre si murió
        # es una afirmación sobre un conjunto vacío. `G-08`.
        self.exigir_preparacion(capturadas)
        todos = (capturadas["raiz"] + capturadas["hijo"]
                 + capturadas["nieto"] + capturadas["bisnieto"])
        vivos = contencion.esperar_a_que_mueran(todos)
        self.assertEqual(vivos, [],
                         "sobrevivió descendencia al backend `" + backend + "`: "
                         + str(vivos))
        return resultado, capturadas

    def test_el_bisnieto_con_setsid_no_escapa_al_backend_elegido(self):
        """T215 · Defecto que previene: llamar contención a un `killpg` que `setsid` esquiva."""
        if not self.capacidades["fuertes_disponibles"]:
            self.skipTest("no hay contención fuerte en este anfitrión; el fallo cerrado "
                          "lo cubre `T216`")
        elegido, _ = modulo_politica.elegir(
            contencion.Politica(deteccion.ARBOL_DE_PROCESOS), self.capacidades)
        self._comprobar_generacional(elegido, "cancelacion")

    def test_cada_backend_fuerte_disponible_contiene_las_tres_generaciones(self):
        """T215 · Defecto que previene: probar sólo el backend cómodo y declarar la clase."""
        disponibles = self.capacidades["fuertes_disponibles"]
        if not disponibles:
            self.skipTest("no hay contención fuerte en este anfitrión")
        for backend in disponibles:
            with self.subTest(backend=backend):
                self.setUp()
                self._comprobar_generacional(backend, "cancelacion")

    def test_el_timeout_tambien_limpia_la_descendencia(self):
        """T215 · Defecto que previene: un timeout que termina el informe y no la tarea."""
        if not self.capacidades["fuertes_disponibles"]:
            self.skipTest("no hay contención fuerte en este anfitrión")
        elegido, _ = modulo_politica.elegir(
            contencion.Politica(deteccion.ARBOL_DE_PROCESOS), self.capacidades)
        resultado, _ = self._comprobar_generacional(elegido, "timeout")
        self.assertEqual(resultado.estado, "timeout")

    def test_la_contencion_sobrevive_al_cambio_de_grupo_de_procesos(self):
        """T215 · Defecto que previene: contener por grupo, que es lo que `setsid` rompe."""
        if not self.capacidades["fuertes_disponibles"]:
            self.skipTest("no hay contención fuerte en este anfitrión")
        elegido, _ = modulo_politica.elegir(
            contencion.Politica(deteccion.ARBOL_DE_PROCESOS), self.capacidades)
        _, capturadas = self._comprobar_generacional(elegido, "cancelacion")
        # El control del control: si las generaciones NO hubieran cambiado de grupo, la
        # prueba no distinguiría el backend fuerte del simple. Se comprueba que la tarea
        # engendró tres generaciones distintas y separadas.
        self.assertNotEqual(capturadas["hijo"], capturadas["nieto"])
        self.assertNotEqual(capturadas["nieto"], capturadas["bisnieto"])

    def test_el_resultado_publicable_no_lleva_pid_ni_duracion(self):
        """T215 · Defecto que previene: `I-g3`, un pid o una duración en lo derivado."""
        resultado = contencion.ejecutar(
            ["sh", "-c", "echo hecho"], espacio=self.espacio, limite_segundos=20,
            politica=contencion.Politica(deteccion.GRUPO_DE_PROCESOS, backend="simple"),
            marca=self.prefijo, capacidades=self.capacidades)
        publicable = resultado.a_dict()
        self.assertEqual(resultado.estado, "completado")
        self.assertNotIn("pid", publicable)
        for clave in publicable:
            self.assertNotIn("duracion", clave)
            self.assertNotIn("ejecucion", clave)


# ===========================================================================
#  T216 · el backend SIMPLE y el FALLO CERRADO
# ===========================================================================
class BackendSimpleYFalloCerrado(BaseDeContencion):

    def test_con_el_backend_simple_el_bisnieto_SI_escapa(self):
        """T216 · Defecto que previene: presentar el nivel débil como si fuera el fuerte.

        Es la mitad negativa de `T215`. `adaptadores/proceso.py` declara este límite —«un
        descendiente que hace `setsid` ESCAPA, y esto está MEDIDO»— y aquí se vuelve a medir
        en vez de creerlo.
        """
        resultado, capturadas = self._correr(
            "simple", deteccion.GRUPO_DE_PROCESOS, modo="cancelacion")
        self.assertEqual(resultado.nivel_de_aislamiento, deteccion.GRUPO_DE_PROCESOS)
        # `G-08`. Aquí estaba el defecto: `assertTrue(capturadas.get("bisnieto"))` era la
        # única red, y bajo carga caía porque el bisnieto todavía no existía a los 0,6 s.
        # Ahora el protocolo responde ANTES, y responde a la pregunta correcta: si el
        # bisnieto no llegó a existir, lo dice con esas palabras; sólo si existió se pasa a
        # juzgar si sobrevivió.
        self.exigir_preparacion(capturadas)
        vivos = [pid for pid in capturadas["bisnieto"] if contencion.sigue_vivo(pid)]
        self.assertEqual(vivos, capturadas["bisnieto"],
                         "el bisnieto NO sobrevivió al backend simple: o la tarea no hizo "
                         "`setsid`, o esta prueba dejó de distinguir los dos niveles")

    def test_el_backend_simple_declara_su_alcance_en_el_resultado(self):
        """T216 · Defecto que previene: degradar sin dejar rastro en la evidencia."""
        resultado, _ = self._correr("simple", deteccion.GRUPO_DE_PROCESOS,
                                    modo="cancelacion")
        self.assertIn("setsid", resultado.ficha_del_backend["detalle"]["alcance"])
        self.assertEqual(resultado.a_dict()["nivel_de_aislamiento"],
                         deteccion.GRUPO_DE_PROCESOS)

    def test_pedir_el_simple_con_politica_fuerte_falla_cerrado(self):
        """T216 · Defecto que previene: cumplir una política fuerte con un backend débil."""
        with self.assertRaises(contencion.ContencionFuerteNoDisponible):
            modulo_politica.elegir(
                contencion.Politica(deteccion.ARBOL_DE_PROCESOS, backend="simple"),
                self.capacidades)

    def test_sin_ningun_backend_fuerte_la_politica_fuerte_falla_cerrado(self):
        """T216 · Defecto que previene: degradar en silencio a `killpg`."""
        fabricadas = {
            "orden_de_preferencia": list(deteccion.ORDEN_DE_PREFERENCIA),
            "niveles": list(deteccion.NIVELES),
            "backends": [
                {"backend": fila["backend"], "nivel": fila["nivel"],
                 "disponible": fila["nivel"] == deteccion.GRUPO_DE_PROCESOS,
                 "motivo": "anfitrión sin contenedores de recursos", "evidencia": {}}
                for fila in self.capacidades["backends"]
            ],
            "fuertes_disponibles": [],
            "hay_contencion_fuerte": False,
            "mejor_disponible": "simple",
        }
        with self.assertRaises(contencion.ContencionFuerteNoDisponible) as capturado:
            modulo_politica.elegir(
                contencion.Politica(deteccion.ARBOL_DE_PROCESOS), fabricadas)
        self.assertIn("NO se degrada", str(capturado.exception))
        # Y la ejecución tampoco ocurre: no hay resultado degradado que nadie pueda leer.
        with self.assertRaises(contencion.ContencionFuerteNoDisponible):
            contencion.ejecutar(["sh", "-c", "echo no deberia correr"],
                                espacio=self.espacio, limite_segundos=5,
                                politica=contencion.Politica(deteccion.ARBOL_DE_PROCESOS),
                                capacidades=fabricadas)

    def test_la_eleccion_nunca_devuelve_el_simple_cuando_se_exige_lo_fuerte(self):
        """T216 · Defecto que previene: una degradación por el camino del `for`."""
        if not self.capacidades["fuertes_disponibles"]:
            self.skipTest("no hay contención fuerte en este anfitrión")
        elegido, _ = modulo_politica.elegir(
            contencion.Politica(deteccion.ARBOL_DE_PROCESOS), self.capacidades)
        self.assertNotEqual(elegido, "simple")
        self.assertEqual(deteccion.NIVEL_POR_BACKEND[elegido],
                         deteccion.ARBOL_DE_PROCESOS)

    def test_pedir_el_simple_explicitamente_es_legitimo_y_queda_registrado(self):
        """T216 · Defecto que previene: retirar el backend débil en vez de declararlo."""
        elegido, _ = modulo_politica.elegir(
            contencion.Politica(deteccion.GRUPO_DE_PROCESOS, backend="simple"),
            self.capacidades)
        self.assertEqual(elegido, "simple")

    def test_un_nivel_fuera_del_vocabulario_falla_cerrado(self):
        """T216 · Defecto que previene: una política con un nivel que nadie implementa."""
        with self.assertRaises(contencion.NivelDesconocido):
            contencion.Politica("aislamiento-total")

    def test_un_backend_desconocido_falla_cerrado(self):
        """T216 · Defecto que previene: pedir un mecanismo que no existe y seguir."""
        with self.assertRaises(contencion.BackendNoDisponible):
            modulo_politica.elegir(
                contencion.Politica(deteccion.ARBOL_DE_PROCESOS, backend="jaula"),
                self.capacidades)

    def test_una_orden_vacia_falla_cerrado(self):
        """T216 · Defecto que previene: lanzar una contención alrededor de nada."""
        with self.assertRaises(contencion.TareaInvalida):
            contencion.ejecutar([], espacio=self.espacio, limite_segundos=5,
                                capacidades=self.capacidades)


# ===========================================================================
#  T410 - T414 · el PROTOCOLO DE PREPARACIÓN de `G-08`, probado como tal
# ===========================================================================
#  Estas cinco no prueban la contención: prueban el APARATO con el que la contención se
#  mide. Es la lección de `G-08`: una batería que falla al lado seguro por una carrera
#  sigue siendo una batería que no dice la verdad, y la línea de base de `F6` declara
#  determinismo byte a byte.
class ProtocoloDePreparacion(BaseDeContencion):

    def test_410_las_cuatro_generaciones_CONFIRMAN_antes_de_que_se_mate_nada(self):
        """T410 · Defecto que previene: matar antes de saber qué había que matar.

        La captura ocurría tras un `sleep 0.6`. Ahora ocurre tras una CONFIRMACIÓN, y esta
        prueba lo comprueba por el ORDEN de la salida: los cuatro `preparado` salen ANTES
        del `listo`, y el `listo` es lo que dispara la cancelación.
        """
        _, capturadas = self._correr("simple", deteccion.GRUPO_DE_PROCESOS,
                                     modo="cancelacion")
        self.exigir_preparacion(capturadas)
        self.assertTrue(self.linea_de_preparacion.startswith(LISTO),
                        self.linea_de_preparacion)
        posicion_listo = [i for i, t in enumerate(self.salida_de_la_tarea)
                          if t.startswith(LISTO)]
        self.assertTrue(posicion_listo, "la tarea no publicó `" + LISTO + "`")
        for generacion in GENERACIONES:
            anuncio = ANUNCIO + " " + generacion
            posicion = [i for i, t in enumerate(self.salida_de_la_tarea)
                        if t.startswith(anuncio)]
            self.assertTrue(posicion, "no se anunció el " + generacion)
            self.assertLess(
                posicion[0], posicion_listo[0],
                "el " + generacion + " se anunció DESPUÉS de `" + LISTO + "`: la raíz dijo "
                "que estaban los tres sin que estuvieran, y la captura vuelve a ser una "
                "carrera")

    def test_411_nunca_creado_y_muerto_por_contencion_son_veredictos_DISTINTOS(self):
        """T411 · Defecto que previene: leer «no existe» como «lo mató la contención».

        Es la mitad que faltaba. Con una generación AMPUTADA, la raíz agota sus sondeos y el
        protocolo dice `NUNCA CREADO(S)`. Con la tarea entera, las cuatro se anuncian y la
        raíz —que sí está en el grupo— muere por `killpg`: mismo aparato, dos veredictos, y
        ninguno se puede confundir con el otro.
        """
        # (1) NUNCA CREADO. Veinte sondeos —un segundo— bastan: lo que se mide aquí no es
        #     cuánto tarda, es que no llega nunca.
        _, capturadas = self._correr(
            "simple", deteccion.GRUPO_DE_PROCESOS, modo="cancelacion", limite=12.0,
            tarea=tarea_sin_una_generacion(self.prefijo, "bisnieto", segundos=20,
                                           sondeos=20))
        self.assertTrue(self.linea_de_preparacion.startswith(SIN_PREPARAR),
                        "la raíz dijo `" + str(self.linea_de_preparacion) + "` con el "
                        "bisnieto amputado: el protocolo no detecta al que no nació")
        self.assertNotIn("bisnieto", self.anunciadas)
        self.assertIn("hijo", self.anunciadas)
        with self.assertRaises(self.failureException) as capturado:
            self.exigir_preparacion(capturadas)
        self.assertIn("NUNCA CREADO", str(capturado.exception))
        self.assertIn("bisnieto", str(capturado.exception))
        self.assertNotIn("sobrevivió", str(capturado.exception))

        # (2) MUERTO POR CONTENCIÓN. Otra corrida, tarea entera: la raíz se anuncia, se la
        #     captura viva y `killpg` se la lleva. El protocolo NO se queja de nadie.
        self.setUp()
        _, enteras = self._correr("simple", deteccion.GRUPO_DE_PROCESOS,
                                  modo="cancelacion")
        self.exigir_preparacion(enteras)
        self.assertIn("raiz", self.anunciadas)
        self.assertEqual(contencion.esperar_a_que_mueran(enteras["raiz"]), [],
                         "la raíz sobrevivió a `killpg` estando en el grupo: entonces esta "
                         "prueba no distingue nada")

    def test_412_la_preparacion_es_una_condicion_OBSERVADA_y_no_una_espera(self):
        """T412 · Defecto que previene: cambiar una constante por otra constante mayor.

        Dos mitades. La primera mira el TEXTO de la tarea —ahí vivía el defecto— y exige que
        la vieja espera no esté y que la conjunción de los tres testigos sí. La segunda es la
        que de verdad decide: una generación que tarda CINCO segundos en anunciarse —ocho
        veces la constante que había— no rompe nada, porque la raíz espera a que aparezca en
        vez de suponer que ya apareció.
        """
        texto = tarea_generacional(self.prefijo)[-1]
        self.assertNotIn("sleep 0.6", texto,
                         "la espera arbitraria sigue en la tarea")
        for generacion in DESCENDIENTES:
            self.assertIn('[ -f "$ADS_PREPARACION/' + generacion + '" ]', texto,
                          "la raíz no observa el testigo del " + generacion)
        self.assertIn("echo " + LISTO, texto)

        retardo = 5
        _, capturadas = self._correr(
            "simple", deteccion.GRUPO_DE_PROCESOS, modo="cancelacion", limite=60.0,
            tarea=tarea_con_generacion_lenta(self.prefijo, "bisnieto", retardo,
                                             segundos=40))
        self.exigir_preparacion(capturadas)
        self.assertTrue(self.linea_de_preparacion.startswith(LISTO),
                        self.linea_de_preparacion)
        # El número de sondeos lo publica la propia raíz: con cinco segundos de retardo y
        # cinco centésimas por sondeo, tiene que haber sondeado de verdad. Si saliera 0, la
        # condición no se estaría observando.
        sondeos = int(self.linea_de_preparacion.rsplit("sondeos=", 1)[-1])
        self.assertGreater(sondeos, 1,
                           "la raíz dijo `" + LISTO + "` sin haber sondeado: la condición "
                           "no se está observando")

    def test_413_repeticion_BAJO_CARGA_sin_intermitencia_debil_y_fuerte(self):
        """T413 · Defecto que previene: declarar determinismo midiendo en reposo.

        La intermitencia de `G-08` se midió BAJO CARGA —4 capturas incompletas de cada 15— y
        en reposo daba 0 de 15. Repetir en reposo no habría demostrado nada. Aquí la carga se
        genera a propósito, y se repite con el backend DÉBIL y con el FUERTE, porque el
        protocolo tiene que valer para los dos o no vale.

        LA REPETICIÓN NO SUSTITUYE AL PROTOCOLO: sin él, N pasadas verdes sólo dicen que la
        carga N+1 no se probó. Lo que garantiza es `T410`.
        """
        quemadores = self._encender_carga()
        self.addCleanup(self._apagar_carga, quemadores)
        planes = [("simple", deteccion.GRUPO_DE_PROCESOS)]
        if self.capacidades["fuertes_disponibles"]:
            elegido, _ = modulo_politica.elegir(
                contencion.Politica(deteccion.ARBOL_DE_PROCESOS), self.capacidades)
            planes.append((elegido, deteccion.ARBOL_DE_PROCESOS))
        for backend, nivel in planes:
            for pasada in range(REPETICIONES_BAJO_CARGA):
                with self.subTest(backend=backend, pasada=pasada):
                    self.setUp()
                    _, capturadas = self._correr(backend, nivel, modo="cancelacion",
                                                 limite=60.0)
                    self.exigir_preparacion(capturadas)

    def test_414_setsid_conservado_y_MEDIDO_generacion_a_generacion(self):
        """T414 · Defecto que previene: que el montaje deje de probar lo que dice probar.

        `T215` y `T216` sólo significan algo si las generaciones SE SALEN del grupo: si un
        día la tarea dejara de hacer `setsid`, las dos seguirían pasando y ya no distinguirían
        el nivel fuerte del débil. Antes esto se aproximaba comparando listas de PID; aquí se
        mide lo que `setsid` de verdad cambia, el identificador de SESIÓN de
        `/proc/<pid>/stat`, leído en el instante de la captura.
        """
        _, capturadas = self._correr("simple", deteccion.GRUPO_DE_PROCESOS,
                                     modo="cancelacion")
        self.exigir_preparacion(capturadas)
        vistas = {}
        for generacion in GENERACIONES:
            sesiones = self.sesiones.get(generacion) or []
            self.assertTrue(sesiones,
                            "no se pudo leer la sesión del " + generacion)
            for sesion in sesiones:
                self.assertNotIn(
                    sesion, vistas,
                    "el " + generacion + " comparte sesión con el " + str(vistas.get(sesion))
                    + ": no hizo `setsid`, y entonces `T215`/`T216` no distinguen los dos "
                      "niveles de aislamiento")
                vistas[sesion] = generacion
        self.assertEqual(len(vistas), len(GENERACIONES))

    # -------------------------------------------------------------- carga, encendida aquí
    def _encender_carga(self):
        """Quemadores de CPU reales. La carga que hizo aparecer la intermitencia medida."""
        cuantos = max(2, (os.cpu_count() or 2) * QUEMADORES_POR_NUCLEO)
        guion = "i=0\nwhile [ 1 ]; do i=$((i+1)); done\n"
        procesos = []
        for _ in range(cuantos):
            procesos.append(subprocess.Popen(
                ["sh", "-c", guion], stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                start_new_session=True))
        return procesos

    def _apagar_carga(self, procesos):
        for proceso in procesos:
            try:
                os.killpg(os.getpgid(proceso.pid), signal.SIGKILL)
            except OSError:
                # Ya murió, o el grupo se fue. En los dos casos no queda nada que apagar.
                pass
            try:
                proceso.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proceso.kill()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
