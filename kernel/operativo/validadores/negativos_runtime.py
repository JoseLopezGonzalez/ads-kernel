#!/usr/bin/env python3
"""negativos_runtime — las infracciones deliberadas que sabotean las BATERÍAS del runtime.

POR QUÉ EXISTE ESTE FICHERO, Y QUÉ AGUJERO CIERRA. El catálogo único de infracciones sólo
sabía sabotear VALIDADORES: `comprobar_negativos.ejecutar` construía
`kernel/operativo/validadores/<validador>.py`, lo llamaba con `--json --raiz` y buscaba una
fila `{"id": "Tnnn", "estado": …}`. Una batería `unittest` del runtime no puede satisfacer
nada de eso. Medido antes de corregir: de las 102 mutaciones con validador literal, **CERO**
apuntaban a `kernel/operativo/runtime/pruebas/`.

La consecuencia no era estética. El derivador del universo obligatorio calcula la resta `B`
—«implementadas SIN PRUEBA CAPAZ DE FALLAR»— como «ninguna `Mutacion` apunta a sus
pruebas». Como las 37 obligaciones de esa resta se verifican con baterías del runtime y el
catálogo no podía alcanzarlas, **36 de sus 37 filas estaban ahí POR CONSTRUCCIÓN**. Con ese
criterio `F6` sería incertificable por construcción, y eso no puede ser lo que `O26` §5.2
quiso decir. No se baja el listón: se sube el ALCANCE DEL INSTRUMENTO, y después se puebla.

QUÉ HAY AQUÍ, Y CON QUÉ EXIGENCIA. Veintidós infracciones —dieciocho, más las CUATRO que
añaden `ADJ-B1` y `ADJ-B2` del gate del 2026-09-04—. Veintiuna son de clase
`bateria` —copian el corpus, meten el defecto, ejecutan la batería DECLARADA con el
intérprete en curso sobre la copia y exigen TRES cosas, no una: que la batería termine en
rojo, que ENTRE LOS CASOS CAÍDOS esté el declarado —se sabe por el docstring `Tnnn · …` que
`unittest` imprime debajo del nombre de cada caso con `verbosity=2`— y que ESE caso caiga
POR EL MOTIVO ESPERADO—. Una es de clase `validador`, porque la obligación que desbloquea
—`FD-3`— se verifica con `comprobar_arranque.py` y no con una batería.

CÓMO SE ELIGIÓ CADA UNA, Y POR QUÉ NO SON TREINTA Y SIETE. Las 37 obligaciones no tienen 37
pruebas: se concentran en unas pocas. Lo que hace falta es que ALGUNA mutación apunte a una
prueba que cubra cada obligación, y que cada mutación sabotee una propiedad **real y
distinta**, la que la obligación NOMBRA. Un sabotaje que no corresponda a la propiedad que
la obligación nombra es peor que la ausencia: acredita en falso. Por eso cada entrada de
abajo cita el `falla_si` del escenario que ataca, y rompe exactamente esa cosa.

  obligación(es)                        prueba   propiedad saboteada
  ------------------------------------  -------  --------------------------------------
  `A14`                                 `T172`   la guarda de intérprete se puede RELAJAR
  `g.1` `g.2` `g.16`                    `T173`   el diario lleva el `pid` del que escribe
  `g.3` `g.4` `g.12` `g.16`             `T174`   la zona de preparación entra al versionado
  `g.8` `g.3`                           `T175`   el punto de no retorno se mueve a `abierta`
  `g.6` `g.12`                          `T176`   agotar reintentos no abre el registro
  `g.5` `g.13` `g.15`                   `T177`   el `cid` del canónico deja de contrastarse
  `g.9` `g.2`                           `T178`   la cabeza no ancla el extremo al LEER
  `g.10` `g.11`                         `T179`   una versión de formato desconocida se adivina
  `g.14`                                `T187`   omitir el valor viejo salta la guarda del hook
  `g.15` `FD-1`                         `T192`   la configuración de confianza cabe DENTRO
  `V6-01`…`V6-09`                       `T188`   una salida truncada se devuelve como completa
  `V6-10` `V6-11`                       `T189`   el instrumento se sale de su propio alcance
  `V6-13` `V6-14` `V6-17` `V6-18` `V6-19` `T190` la sede de fórmulas rompe el caso frontera
  `V6-15`                               `T211`   la versión vulnerable deja de aceptar el ataque
  `V6-16`                               `T217`   una instalación ALTERADA emite veredicto
  `FD-5`                                `T216`   el backend débil se presenta como fuerte
  `FD-6`                                `T191`   un recibo ABIERTO se reejecuta, y duplica
  `FD-3`                                `T194`   el motor durable no viaja al proyecto instalado
  `ADJ-B1`                              `T320`   la migración 0->1 publica la revisión 0 SIN
                                                 el `testigo` que `E-08` hizo obligatorio
  `ADJ-B1`                              `T321`   la guarda de la fundación vuelve a mirar el
                                                 evento del diario y no la revisión que falta
  `ADJ-B2`                              `T330`   el verificador de la raíz externa pierde la
                                                 purga `E-10` de la ruta de importación
  `ADJ-B2`                              `T333`   el instalador vuelve a copiar encima del
                                                 destino, e instala a medias

FORMA SINTÁCTICA, Y POR QUÉ NO SE TOCA. El derivador externo lee los sabotajes con
`Mutacion\\(\\s*"([^"]+)"\\s*,\\s*"[^"]*"\\s*,\\s*"(T\\d+)"`. Esa expresión exige el token
`Mutacion` pegado al paréntesis y el identificador de prueba como TERCER posicional
entrecomillado. Por eso la clase de batería no es una subclase con nombre propio: es un
CAMPO `clase` de `Mutacion`. Una subclase llamada de otro modo dejaría cada entrada de aquí
invisible para la resta `B`, que es lo único que este fichero existe para mover.

COSTE DE CORRIDA, MEDIDO. Cada mutación copia el corpus entero (~14 MB) y ejecuta una
batería COMPLETA: no hay ninguna corrida parcial, y por tanto no hay ninguna que declarar.
Las baterías usadas tardan, sueltas: `test_estado_durable` ~20 s, `test_gobierno_git` ~13 s,
`test_contencion` ~15 s, `test_raiz_externa` ~8 s, `test_admision` ~3 s, `test_arboles`
~1 s, `test_identidad` ~0,2 s; `comprobar_arranque` ~90 s. El total añadido está medido en
el informe de la corrección.
"""
# ---------------------------------------------------------------------------
#  ADVERTENCIA DE FORMA · este módulo NO lleva línea de intérprete, y es deliberado.
#
#  `H-03` de la auditoría independiente del 2026-09-04 obligó a que el inventario de puntos
#  ejecutables se derive del ÁRBOL ENTERO y a que TODO `.py` quede clasificado —el
#  inventario anterior era mecánico DENTRO de dos zonas escritas a mano, y por eso
#  `validadores/` estaba entera fuera del control mientras `H-01` encontraba el defecto
#  `E-10` vivo en `huella.py`—. La equivalencia que `T330` comprueba sobre el disco es:
#
#      lleva `#!`   ⟺   es INVOCABLE   ⟺   lleva el MECANISMO `E-10`
#
#  Este módulo se IMPORTA —`comprobar_negativos.py` lo incorpora por nombre y sin
#  `try/except`— y no se ejecuta: no define `__main__` ni sale desde el nivel superior. No
#  cumple el segundo término, así que tampoco puede llevar el primero: una línea de
#  intérprete presenta un módulo como ejecutable, y a un ejecutable esta equivalencia le
#  exige la purga. Se retira la línea, y con ella la ambigüedad. Es exactamente lo que
#  `ADJ-B2` hizo con `errores.py`, `firma.py`, `atestacion.py` y `aislamiento.py` de la
#  raíz externa.
# ---------------------------------------------------------------------------

from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  Este módulo registra su catálogo de mutaciones con `CATALOGO.extend(...)` en el NIVEL
#  SUPERIOR: hace trabajo al importarse, y por tanto es un punto ejecutable, lo invoque
#  alguien directamente o no. El auditor independiente señaló que de los dos ficheros de
#  esta familia uno llevaba la guarda y el otro no, y que la asimetría no la medía nadie
#  porque los dos quedaban fuera del inventario. Ahora los dos están dentro.

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
#  Este módulo entró en el inventario de puntos ejecutables al invertirse la carga —hace
#  trabajo al importarse: registra su catálogo con `CATALOGO.extend(...)` en el nivel
#  superior—, y a un punto ejecutable se le exige el mecanismo ENTERO y no medio: la guarda
#  de `G-03` de arriba, que decide el aislamiento antes de que el intérprete arranque, y
#  esta purga, que retira de `sys.path` lo que el LANZADOR pudo meter. Se copia byte a byte
#  del resto de puntos, que es lo que `T330` comprueba: un mecanismo «adaptado» es un
#  mecanismo que ya no se sabe si protege.

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

RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()

CATALOGO = []

import os  # noqa: E402

import comprobar_negativos as _cn  # noqa: E402

Mutacion, _sustituir = _cn.Mutacion, _cn._sustituir
BATERIA = _cn.CLASE_BATERIA

PRUEBAS_RUNTIME = "kernel/operativo/runtime/pruebas/"
ESTADO_DURABLE = PRUEBAS_RUNTIME + "test_estado_durable.py"
ADMISION = PRUEBAS_RUNTIME + "test_admision.py"
GOBIERNO_GIT = PRUEBAS_RUNTIME + "test_gobierno_git.py"
IDENTIDAD = PRUEBAS_RUNTIME + "test_identidad.py"
ARBOLES = PRUEBAS_RUNTIME + "test_arboles.py"
CONTENCION = PRUEBAS_RUNTIME + "test_contencion.py"
ADAPTADORES = PRUEBAS_RUNTIME + "test_adaptadores.py"
RAIZ_EXTERNA = PRUEBAS_RUNTIME + "test_raiz_externa.py"
INTEGRIDAD = PRUEBAS_RUNTIME + "test_integridad_y_evidencia.py"


# ===========================================================================
#  `A14` · la guarda de versión del intérprete
# ===========================================================================

def m_a14_la_guarda_se_puede_relajar(raiz):
    """`T172`, `falla_si`: «la guarda se puede relajar por entorno».

    `entorno.py` admite `ADS_ENTORNO_VERSION_MINIMA` para SUBIR la exigencia y NUNCA para
    bajarla, y lo razona: «una guarda que se puede relajar por entorno no es una guarda: es
    un interruptor, y el primero que lo use en CI la apaga para todos». Aquí se le quita la
    pinza y la variable pasa a mandar en los dos sentidos.
    """
    _sustituir(raiz, "kernel/operativo/validadores/entorno.py",
               "    if pedido <= VERSION_MINIMA:\n"
               "        return VERSION_MINIMA, (f\"{VARIABLE_DE_EXIGENCIA}={crudo} no supera la mínima \"",
               "    if False:\n"
               "        return VERSION_MINIMA, (f\"{VARIABLE_DE_EXIGENCIA}={crudo} no supera la mínima \"")


# ===========================================================================
#  `g.1`…`g.16` · el MOTOR DE ESTADO DURABLE
# ===========================================================================

def m_g1_el_diario_lleva_el_pid(raiz):
    """`T173`, `entonces`: «ninguna lectura del estado necesita reproyectar el diario», y el
    §0 prohíbe reloj, duración y `pid` en lo durable (`I-g3`).

    Un campo «inofensivo» en cada evento del diario: el `pid` del proceso que lo escribió.
    Es el defecto clásico —nadie lo pone por maldad— y rompe la reproducibilidad: dos
    almacenes construidos con las MISMAS transiciones dejan de dar los mismos bytes.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/diario.py",
               '        evento = {"esquema": ESQUEMA, "secuencia": len(completas) + 1, "tipo": tipo}',
               '        evento = {"esquema": ESQUEMA, "secuencia": len(completas) + 1, "tipo": tipo,\n'
               '                  "pid": os.getpid()}')


def m_g3_la_zona_de_preparacion_entra_al_versionado(raiz):
    """`T174`, `falla_si`: «la zona de preparación entra en el versionado, y la rama canónica
    pasa a contener estado parcial».

    El motor escribe él mismo el `.gitignore` del almacén «en vez de confiar en que alguien
    se acuerde de hacerlo». Aquí se le quita la única línea que excluye `operacional/`: a
    partir de ahí, un `git add -A` durante la ventana de una transacción sube la zona de
    preparación a la rama canónica, que es exactamente lo que `g.14` prohíbe.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/rutas.py",
               '    + OPERACIONAL + "/\\n"\n)',
               '    "# (la zona de preparación se excluye en otro sitio)\\n"\n)')


def m_g8_el_punto_de_no_retorno_se_adelanta(raiz):
    """`T175`, `falla_si`: «una transición incompleta queda publicada».

    El §3 fija el punto de no retorno en `transicion.preparada`: antes se REVIERTE, después
    se COMPLETA, y no hay tercera rama. Aquí se adelanta a `transicion.abierta`, de modo que
    una caída ANTES de preparar nada se «completa» igualmente y publica una transición que
    nunca llegó a estar preparada.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/motor.py",
               '        if "transicion.preparada" in tipos:\n'
               '            preparada = [e for e in propios if e["tipo"] == "transicion.preparada"][-1]',
               '        if "transicion.abierta" in tipos:\n'
               '            preparada = [e for e in propios if e["tipo"] == "transicion.abierta"][-1]')


def m_g6_agotar_reintentos_no_abre_el_registro(raiz):
    """`T176`, `falla_si`: «agotar reintentos se declara con el código del camino que NO abre
    el registro auxiliar».

    Es el agujero que la auditoría independiente ya encontró una vez, reintroducido: el
    escritor que agota sus reintentos propaga `ESCRITOR_CONCURRENTE` tal cual en vez de
    `REINTENTOS_AGOTADOS`, y por ese camino no se escribe el registro de `g.9`. La pendencia
    deja de existir sin que nadie la haya cerrado.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/motor.py",
               "            registro = self._abrir_reconciliacion_por_reintentos("
               "transicion.id, intentos, exc)\n"
               "            raise ReintentosAgotados(",
               "            raise exc\n"
               "            registro = self._abrir_reconciliacion_por_reintentos("
               "transicion.id, intentos, exc)\n"
               "            raise ReintentosAgotados(")


def m_g5_el_cid_deja_de_contrastarse(raiz):
    """`T177`, `falla_si`: «una corrupción se lee como estado válido».

    `leer` compara el `cid` del fichero en disco con el que `REVISION.json` declara y falla
    CERRADO cuando no casan: «un lector que recibe datos que no casan con la revisión
    propaga la corrupción». Aquí se sirve el contenido sin contrastarlo, que es servir como
    bueno un fichero canónico manipulado a mano.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/motor.py",
               "            if encontrado == esperado:\n"
               "                objeto = deserializar(datos, ruta=ruta)",
               "            if True:\n"
               "                objeto = deserializar(datos, ruta=ruta)")


def m_g9_la_cabeza_no_ancla_en_el_camino_de_lectura(raiz):
    """`T178`, `falla_si`: «la comprobación vive sólo en la verificación y no en el camino de
    lectura que deduce la pendencia».

    Una cadena de huellas NO detecta que le quiten la COLA: el prefijo sigue encadenado. Por
    eso el registro auxiliar tiene una CABEZA que ancla su extremo, y por eso se contrasta
    en el camino de LECTURA y no sólo al verificar. Aquí se retira de la lectura: borrar la
    última línea vuelve a cerrar una pendencia en silencio.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/reconciliacion.py",
               "        if verificar:\n"
               "            # En el camino de LECTURA, y no sólo en `verificar_integridad`: `g.9` exige que\n"
               "            # la pendencia se deduzca de forma INEQUÍVOCA, y deducirla de un log al que le\n"
               "            # falta la cola no es deducirla, es creerse lo que quedó.\n"
               "            self._exigir_cabeza(salida)\n",
               "")


def m_g10_una_version_desconocida_se_adivina(raiz):
    """`T179`, `falla_si`: «un lector adivina el significado de una versión que no conoce».

    `g.10` dice que un lector que encuentra una versión que no entiende FALLA CERRADO. Aquí
    se conserva la comprobación de TIPO —que sea un entero— y se retira la de VALOR, que es
    la que importa: cualquier versión de formato futura se abre «haciendo lo que se pueda».
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/motor.py",
               "    if not isinstance(version, int) or version != VERSION_DE_FORMATO:",
               "    if not isinstance(version, int):")


# ===========================================================================
#  `g.14` · gobierno Git del REPOSITORIO DE CONTROL
# ===========================================================================

def m_g14_omitir_el_valor_viejo_salta_la_guarda(raiz):
    """`T187`, `falla_si`: «omitir el valor viejo —que Git hace opcional— salta la guarda».

    El `OID` nulo en `viejo` NO significa «creación»: Git lo pasa también cuando el llamador
    no declara valor viejo, que es el caso POR DEFECTO de `git update-ref <ref> <nuevo>`. El
    hook lo sabe y RESUELVE la ref por su cuenta. Aquí vuelve a tratarse como creación, y la
    mitad IMPOSIBLE de `G-A8` se salta escribiendo tres palabras en vez de cuatro.
    """
    _sustituir(raiz, "kernel/operativo/runtime/gobierno/git.py",
               '    actual="$viejo"\n'
               '    if [ "$viejo" = "$nulo" ]; then\n'
               '        actual=$(git rev-parse --verify --quiet "$ref^{commit}" 2>/dev/null || echo "$nulo")\n'
               '    fi',
               '    actual="$viejo"\n'
               '    if [ "$viejo" = "$nulo" ]; then\n'
               '        continue\n'
               '    fi')


# ===========================================================================
#  `g.15` · frontera con la RAÍZ EXTERNA DE CONFIANZA
# ===========================================================================

def m_g15_la_configuracion_cabe_dentro_del_arbol(raiz):
    """`T192`, `falla_si`: «el repositorio verificado puede cambiar qué identidad se acepta».

    `O25` §3 prohíbe que la configuración externa de confianza viva dentro de lo que
    gobierna. La comprobación es un `startswith` sobre la ruta resuelta; aquí se degrada a
    una igualdad exacta, de modo que sólo se rechaza la raíz del árbol y CUALQUIER
    subdirectorio suyo pasa. Es la forma en que estas guardas se rompen de verdad: nadie
    borra la comprobación, la debilita.
    """
    _sustituir(raiz, "kernel/operativo/runtime/identidad/configuracion.py",
               "def _dentro(candidata, arbol):\n"
               "    return candidata == arbol or candidata.startswith(arbol + os.sep)",
               "def _dentro(candidata, arbol):\n"
               "    return candidata == arbol")


# ===========================================================================
#  `V6-01`…`V6-19` · el VERIFICADOR DE ADMISIÓN
# ===========================================================================

def m_v6_salida_truncada_pasa_por_completa(raiz):
    """`T188`, `falla_si`: «una salida truncada devuelve lista vacía con éxito».

    Una lista `-z` bien formada termina SIEMPRE en `NUL`, y ése es el ÚNICO indicio de que
    la lectura llegó entera. Aquí se retira la denuncia del truncamiento y se devuelve lo
    que hubiera llegado: una lista parcial presentada como completa, que es como un fichero
    tocado desaparece del inventario sin que nada lo diga.
    """
    _sustituir(raiz, "kernel/operativo/runtime/admision/lectura.py",
               '    if not salida.endswith(b"\\0"):\n'
               '        raise SalidaTruncada(',
               '    if not salida.endswith(b"\\0"):\n'
               '        return salida.split(b"\\0")\n'
               '    if False:\n'
               '        raise SalidaTruncada(')


def m_v6_el_instrumento_se_sale_de_su_alcance(raiz):
    """`T189`, `falla_si` de `V6-11`: el verificador y su política no pueden salirse de su
    propio alcance.

    Los prefijos de autoinclusión son lo que mete al propio verificador —y a su política—
    dentro del perímetro que juzga. Vaciándolos, cambiar la regla y aprobarse con la regla
    nueva vuelve a ser gratis, y la mutación del instrumento deja de dar ROJO.
    """
    _sustituir(raiz, "kernel/operativo/runtime/admision/__init__.py",
               "    return politica.prefijos_de_autoinclusion()",
               "    return ()")


def m_v6_la_sede_de_formulas_rompe_su_frontera(raiz):
    """`T190`, `falla_si`: «un control adversarial no puede ponerse rojo», y `V6-19`: una
    sola definición de cada fórmula compartida.

    El recuento de líneas de un blob tiene DOS casos frontera declarados por su nombre: el
    fichero VACÍO da 0, y el que no termina en salto de línea cuenta igual. Aquí se sustituye
    por `splitlines()` con un mínimo de 1 —la reimplementación «equivalente» que siempre
    aparece—, y los dos instrumentos que cuentan líneas pasan a contradecirse justo ahí.
    """
    _sustituir(raiz, "kernel/operativo/runtime/admision/formulas.py",
               '    datos = bytes(datos)\n'
               '    if not datos:\n'
               '        return 0\n'
               '    completas = datos.count(b"\\n")\n'
               '    return completas if datos.endswith(b"\\n") else completas + 1',
               '    datos = bytes(datos)\n'
               '    return len(datos.splitlines()) or 1')


def m_v6_la_version_vulnerable_deja_de_reproducir(raiz):
    """`T211`, `falla_si`: «la versión vulnerable y la vigente no se distinguen sobre el mismo
    árbol».

    Las versiones históricas existen para ACEPTAR el árbol atacado: si dijeran ROJO a todo,
    la suite mediría dos instrumentos idénticos y no demostraría que la corrección corrigió
    nada. Aquí la versión vulnerable de `S1-01` pasa a denunciar siempre, «por si acaso», y
    la reproducción del defecto original deja de producirse.
    """
    _sustituir(raiz, "kernel/operativo/runtime/arboles/versiones.py",
               "    # Publica su recuento, y ése es el recuento FALSO que `S1-01` midió.\n"
               '    return _veredicto("VERDE", del_kernel=sorted(del_kernel),',
               '    return _veredicto("ROJO", del_kernel=sorted(del_kernel),\n'
               "                      enumerados=len(del_kernel), leidos=sorted(tocados),\n"
               '                      causa="por si acaso")\n'
               '    return _veredicto("VERDE", del_kernel=sorted(del_kernel),')


def m_v6_una_instalacion_alterada_emite_veredicto(raiz):
    """`T217`, `falla_si`: «un cambio dentro del árbol altera la política que la raíz externa
    aplica», y §11.8: los digests se RECALCULAN.

    La raíz externa recalcula el digest de cada fichero de su instalación y no emite si algo
    no casa. Aquí se retira `alteradas` de la condición: siguen contando la ausencia y el
    sobrante, pero un fichero MODIFICADO —el caso que importa, porque es el que un atacante
    provoca— deja de invalidar la instalación y el verificador manipulado emite veredicto.
    """
    _sustituir(raiz, "kernel/operativo/raiz-externa/instalar.py",
               '        "ok": not alteradas and not ausentes and not sobrantes,',
               '        "ok": not ausentes and not sobrantes,')


# ===========================================================================
#  `FD-5` · contención de procesos
# ===========================================================================

def m_fd5_el_backend_debil_se_presenta_como_fuerte(raiz):
    """`T216`, `falla_si` de `T214`: «una sonda declara disponible un mecanismo que no puede
    contener nada».

    El backend `simple` mata el GRUPO de procesos y su nivel declarado es INFERIOR: un
    descendiente que hace `setsid` se le escapa, y eso está escrito en `FD-5`. Aquí se le
    sube el nivel a `arbol-de-procesos`, con lo que una política que exige contención FUERTE
    se cumpliría con el backend que no la da. Es presentar el débil como fuerte, que es la
    forma exacta en que esta deuda se cerraría en falso.
    """
    _sustituir(raiz, "kernel/operativo/runtime/contencion/deteccion.py",
               '    "simple": GRUPO_DE_PROCESOS,\n}',
               '    "simple": ARBOL_DE_PROCESOS,\n}')


# ===========================================================================
#  `FD-6` · la ventana entre EJECUTAR y escribir el recibo, que se hace DETECTABLE
# ===========================================================================
#  `06-DEUDA` §10 bis lo escribe así: la ventana «**no se cierra: se hace DETECTABLE** — el
#  recibo se abre antes de ejecutar y una segunda invocación que lo encuentre sin cerrar
#  devuelve `ambiguo`, y la autoridad decide». No tiene cierre por diseño: con un proceso
#  externo cualquiera no existe «exactamente una vez». Lo que SÍ se exige, y es lo que este
#  sabotaje ataca, es que la ambigüedad **se detecte en vez de duplicarse en silencio**.
def m_fd6_el_recibo_abierto_se_reejecuta(raiz):
    """`T191`, `falla_si`: «una caída entre ejecutar y cerrar el recibo duplica el efecto EN
    SILENCIO».

    Se cambia la rama del recibo ABIERTO para que, en vez de devolver `ambiguo`, siga de
    largo y vuelva a lanzar la orden. Es exactamente la duplicación que `FD-6` declara no
    poder cerrar y sí poder detectar: si esta mutación no pusiera nada rojo, la mitad
    DETECTABLE de la deuda estaría escrita y no ejercida, que es la forma en que una deuda
    se cierra en falso.
    """
    _sustituir(raiz, "kernel/operativo/runtime/adaptadores/proceso.py",
               '            return comprobar_resultado({\n                "estado": AMBIGUO,',
               '            pass\n        if False:\n            return comprobar_resultado({\n                "estado": AMBIGUO,')


# ===========================================================================
#  `FD-3` · la especificación normativa que VIAJA al proyecto instalado
# ===========================================================================
#  Ésta es la única de clase `validador`, y se dice por qué: `FD-3` se verifica con `T181` y
#  `T194`, y las dos declaran `comprobar_arranque.py` como su validador. `T181` no tiene hoy
#  implementación en ese validador —el fichero publica `T148`, `T171` y `T194`—, así que la
#  única prueba de `FD-3` que puede ponerse roja es `T194`, y a ella se apunta. Queda dicho
#  en el informe como PETICIÓN, no como omisión.

def m_fd3_el_motor_durable_no_viaja(raiz):
    """`T194`: «el runtime del estado durable viaja con el kernel al proyecto instalado».

    El arranque copia `kernel/operativo` entero. Aquí se le quita el runtime justo después,
    que es la forma en que esto se rompe de verdad: no borrando la copia, sino podándola
    «porque el proyecto no lo necesita». Un proyecto instalado sin motor no puede sostener
    el estado durable que la sección `(g)` le exige, y `T194` lo dice con esas palabras.
    """
    _sustituir(raiz, "tooling/new-project.sh",
               'cp -r "$SRC/kernel/operativo" "$ADS/kernel/"\n',
               'cp -r "$SRC/kernel/operativo" "$ADS/kernel/"\n'
               'rm -rf "$ADS/kernel/operativo/runtime"\n')


# ===========================================================================
#  `ADJ-B1` · la MIGRACIÓN 0->1 sobre un almacén heredado REAL
# ===========================================================================

def m_adjb1_la_migracion_vuelve_a_omitir_el_testigo(raiz):
    """`T320`, `falla_si`: «la migración 0->1 publica la revisión 0 SIN el `testigo` que
    `E-08` hizo obligatorio».

    Es el defecto de `ADJ-B1` reintroducido tal cual: de las cinco llamadas a
    `_publicar_revision` del árbol, la de la migración vuelve a quedarse sin el argumento de
    sólo palabra clave. Lo medido antes de corregir era `TypeError` NO tipada, `EXIT=1`,
    `stdout` vacío y siete rutas absolutas del anfitrión en la traza.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/migracion.py",
               "    almacen._publicar_revision(revision_cero, "
               "testigo=motor.TESTIGO_DE_FUNDACION)",
               "    almacen._publicar_revision(revision_cero)")


def m_adjb1_la_fundacion_vuelve_a_mirar_el_diario(raiz):
    """`T321`, `falla_si`: «una primera migración fallida deja el almacén inmigrable».

    El AGRAVANTE de `ADJ-B1`, reintroducido: la guarda de la rama de fundación vuelve a
    mirar el EVENTO del diario en vez de la revisión que falta. Con el diario ya fundado y
    sin `REVISION.json`, la rama no se vuelve a entrar y el almacén queda inmigrable
    incluso con el `testigo` puesto. Es la mitad que la corrección de la línea no repara.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/migracion.py",
               "    hay_revision = os.path.exists(disposicion.revision)\n"
               "    fundacion = _fundacion_en(eventos)",
               "    fundacion = _fundacion_en(eventos)\n"
               "    hay_revision = fundacion is not None")


# ===========================================================================
#  `ADJ-B2` · la PURGA `E-10` en TODA la raíz externa
# ===========================================================================

def m_adjb2_la_raiz_externa_pierde_la_purga(raiz):
    """`T330`, `falla_si`: «un punto ejecutable del inventario no lleva el prólogo `E-10`».

    El defecto de `ADJ-B2` reintroducido en el punto que `O26` §1 juzga: `verificador.py`
    deja de purgar la ruta de importación. Lo medido antes de corregir era `capacidades`
    publicando `{}` con código 0 bajo un `json.py` homónimo, y CERO líneas de purga en todo
    el paquete.
    """
    _sustituir(raiz, "kernel/operativo/raiz-externa/verificador.py",
               "def _purgar_la_ruta_de_importacion():",
               "def _purga_desactivada():")
    _sustituir(raiz, "kernel/operativo/raiz-externa/verificador.py",
               "RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()",
               "RETIRADAS_DE_LA_RUTA = []")


def m_adjb2_el_instalador_vuelve_a_copiar_encima(raiz):
    """`T333`, `falla_si`: «una instalación interrumpida deja el destino a medias».

    El instalador vuelve a borrar el destino y copiar encima, en vez de construir aparte y
    publicar por renombrado. Una dependencia que falte deja entonces en el destino un árbol
    con parte de los ficheros y SIN manifiesto: una instalación que no se puede comprobar y
    que está ahí para que alguien la ejecute.
    """
    _sustituir(raiz, "kernel/operativo/raiz-externa/instalar.py",
               "    try:\n"
               "        _construir(en_curso, runtime=runtime)\n"
               "    except BaseException:",
               "    if os.path.exists(destino):\n"
               "        shutil.rmtree(destino)\n"
               "    _construir(destino, runtime=runtime)\n"
               "    return {\"destino\": destino,\n"
               "            \"manifiesto\": os.path.join(destino, MANIFIESTO),\n"
               "            \"verificador\": os.path.join(destino, NOMBRE_DEL_PAQUETE,\n"
               "                                        \"verificador.py\")}\n"
               "    try:\n"
               "        _construir(en_curso, runtime=runtime)\n"
               "    except BaseException:")


# ===========================================================================
#  `H-01` · `H-03` · `H-08` · los tres hallazgos de la auditoría independiente del
#  2026-09-04 que viven en el aparato de la evidencia
# ===========================================================================

def m_h01_la_huella_pierde_la_purga(raiz):
    """`T330`, `falla_si`: «un punto ejecutable del inventario no lleva el prólogo `E-10`».

    El defecto BLOQUEANTE `H-01`, reintroducido en su sede exacta. `validadores/huella.py`
    deja de purgar la ruta de importación, y entonces vuelve a ser cierto lo que el auditor
    midió: con un `hashlib.py` homónimo en `PYTHONPATH` cuyo `sha256()` devuelve el digest
    esperado, un árbol MUTADO produce la huella ESPERADA y `comprobar_integridad.py` publica
    `T150 SUPERADA · EXIT=0`.

    Va contra `T330` y no contra `T150` a propósito: `T150` compara dos números y no puede
    saber de dónde salió el `hashlib` que los calculó; quien lo sabe es el inventario. Es la
    misma razón por la que `N330` va contra `T330` y no contra el `capacidades` del
    verificador.
    """
    _sustituir(raiz, "kernel/operativo/validadores/huella.py",
               "RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()",
               "RETIRADAS_DE_LA_RUTA = []")


def m_h03_el_inventario_vuelve_a_una_zona_escrita(raiz):
    """`T330`, `falla_si`: «el inventario deja de alcanzar alguna zona del árbol».

    `H-03`, reintroducido por su CLASE y no por su instancia. El recorrido vuelve a acotarse
    a una zona escrita a mano —`kernel/operativo/runtime/`—, que es exactamente la forma del
    defecto: la tupla de ficheros escrita a mano dejó fuera a la raíz externa, y la tupla de
    ZONAS que la sustituyó dejó fuera a `validadores/`, `tooling/` y `docs/`, que es donde
    `H-01` encontró el defecto vivo. El sabotaje no quita ninguna purga: sólo deja de MIRAR,
    que es la manera en que este defecto ha vuelto dos veces.
    """
    _sustituir(raiz, "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py",
               "    base = os.path.realpath(raiz or RAIZ_REPO)\n"
               "    puntos, excluidos = {}, {}",
               "    base = os.path.join(os.path.realpath(raiz or RAIZ_REPO),\n"
               "                        \"kernel\", \"operativo\", \"runtime\")\n"
               "    puntos, excluidos = {}, {}")


def m_g03_un_punto_pierde_la_guarda_de_aislamiento(raiz):
    """`T380`, `falla_si`: «un punto ejecutable nuevo entra sin la guarda».

    `G-03` —`H-1` del revisor 2—, reintroducido en la sede donde se midió. `huella.py` deja
    de exigir el aislamiento al entrar, y entonces vuelve a ser cierto lo que el gate del
    2026-09-05 publicó: con un `sitecustomize` alcanzable desde `PYTHONPATH` que sustituye
    `hashlib.sha256`, la huella de un árbol MUTADO sale con el valor fabricado y `T150` da
    `SUPERADA · EXIT=0`.

    Va contra `T380` y no contra `T382` a propósito, y por la misma razón por la que `NH01`
    va contra `T330`: `T382` mide una CORRIDA de `huella.py` y una corrida sin guarda bajo un
    veneno que la mutación no instala no tiene por qué salir mal. Quien sabe que falta la
    guarda es el inventario.
    """
    _sustituir(raiz, "kernel/operativo/validadores/huella.py",
               "AISLAMIENTO = _aislamiento_g03.exigir(__file__, __name__)",
               "AISLAMIENTO = {}")


def m_d01_el_runner_vuelve_a_heredar_el_entorno_de_sus_hijos(raiz):
    """`T394`, `falla_si`: «se quita el `env=` de la llamada».

    `D-01` —`HALLAZGO 3` del revisor 3—, reintroducido en su línea exacta:
    `registrar_evidencia.py` vuelve a lanzar a sus hijos con `subprocess.run` SIN `env=` y
    sin banderas, de modo que el `PYTHONPATH` del padre —y con él el `sitecustomize`— llega
    entero a cada una de las veintiuna baterías que producen la evidencia.

    La mutación NO toca la cabecera: la sigue escribiendo, y con eso se comprueba lo otro que
    el revisor pidió —que la garantía publicada corresponda a lo que de verdad ocurrió—.
    """
    _sustituir(raiz, "kernel/operativo/validadores/registrar_evidencia.py",
               "proc = subprocess.run(orden, cwd=base, capture_output=True, text=True, "
               "env=entorno)",
               "proc = subprocess.run([sys.executable, script, *ej.args], cwd=base, "
               "capture_output=True, text=True)")


def m_h08_la_cobertura_del_contraste_deja_de_publicarse(raiz):
    """`T307`, `falla_si`: «la corrida no publica la cobertura del contraste».

    `H-08`, reintroducido en su sede exacta: `comprobar_evidencia` vuelve a CALCULAR
    `r.nota_cobertura` y a no imprimirla. Lo que el auditor midió es la consecuencia: la
    línea base afirmaba «160 contrastados · 107 no contrastables», el árbol producía
    `193 · 74`, y ninguna de las dos parejas aparecía en ningún fichero del repositorio.
    Una cifra que no se publica no se puede contradecir.

    El sabotaje toca el `print` y NADA MÁS —ni la evidencia publicada, ni el cálculo—,
    porque `T307g` juzga una CORRIDA y no un fichero: así la mutación se detecta en el acto
    y no en la regeneración siguiente.
    """
    _sustituir(raiz, "kernel/operativo/validadores/comprobar_evidencia.py",
               '            if getattr(x, "nota_cobertura", None):',
               '            if False:')


CATALOGO.extend([
    Mutacion("N172", "A14", "T172", ESTADO_DURABLE,
             "la guarda de intérprete pasa a poder RELAJARSE por variable de entorno",
             m_a14_la_guarda_se_puede_relajar, clase=BATERIA,
             espera="no supera la mínima declarada"),
    Mutacion("N173", "g.1", "T173", ESTADO_DURABLE,
             "cada evento del diario lleva el `pid` del proceso que lo escribió",
             m_g1_el_diario_lleva_el_pid, clase=BATERIA,
             espera="contiene «\\bpid\\b»"),
    Mutacion("N174", "g.3", "T174", ESTADO_DURABLE,
             "el `.gitignore` del almacén deja de excluir la zona de preparación",
             m_g3_la_zona_de_preparacion_entra_al_versionado, clase=BATERIA,
             espera="'operacional' not found in"),
    Mutacion("N175", "g.8", "T175", ESTADO_DURABLE,
             "el punto de no retorno se adelanta de `preparada` a `abierta`",
             m_g8_el_punto_de_no_retorno_se_adelanta, clase=BATERIA,
             espera="se publicó una transición que debía revertirse"),
    Mutacion("N176", "g.6", "T176", ESTADO_DURABLE,
             "agotar los reintentos se declara por el camino que NO abre el registro",
             m_g6_agotar_reintentos_no_abre_el_registro, clase=BATERIA,
             espera="`ESCRITOR_CONCURRENTE` es el camino que no abre el registro"),
    Mutacion("N177", "g.5", "T177", ESTADO_DURABLE,
             "el `cid` del objeto canónico deja de contrastarse contra `REVISION.json`",
             m_g5_el_cid_deja_de_contrastarse, clase=BATERIA,
             espera="EstadoCorrupto not raised"),
    Mutacion("N178", "g.9", "T178", ESTADO_DURABLE,
             "la cabeza del registro auxiliar deja de anclar su extremo AL LEER",
             m_g9_la_cabeza_no_ancla_en_el_camino_de_lectura, clase=BATERIA,
             espera="no hizo fallar `reconciliacion`: una pendencia se estaría retirando"),
    Mutacion("N179", "g.10", "T179", ESTADO_DURABLE,
             "una versión de formato desconocida se abre en vez de fallar cerrado",
             m_g10_una_version_desconocida_se_adivina, clase=BATERIA,
             espera="FormatoDesconocido not raised"),
    Mutacion("N187", "g.14", "T187", GOBIERNO_GIT,
             "el hook vuelve a tomar el `OID` nulo por «creación» y deja pasar el forzado",
             m_g14_omitir_el_valor_viejo_salta_la_guarda, clase=BATERIA,
             espera="tres argumentos NO pueden ser una vía de forzado"),
    Mutacion("N192", "g.15", "T192", IDENTIDAD,
             "la configuración de confianza puede vivir en un subdirectorio del árbol",
             m_g15_la_configuracion_cabe_dentro_del_arbol, clase=BATERIA,
             espera="ConfiguracionDentroDelArbol not raised"),
    Mutacion("N188", "V6-02", "T188", ADMISION,
             "una salida `-z` truncada se devuelve como si fuera la lista completa",
             m_v6_salida_truncada_pasa_por_completa, clase=BATERIA,
             espera="SalidaTruncada not raised"),
    Mutacion("N189", "V6-11", "T189", ADMISION,
             "el verificador y su política se quedan fuera de su propio alcance",
             m_v6_el_instrumento_se_sale_de_su_alcance, clase=BATERIA,
             espera="any(ruta.startswith(prefijo) for prefijo in prefijos)"),
    Mutacion("N190", "V6-19", "T190", ADMISION,
             "la sede única de fórmulas rompe el caso frontera del fichero VACÍO",
             m_v6_la_sede_de_formulas_rompe_su_frontera, clase=BATERIA,
             espera="la sede de fórmulas no respeta los casos frontera del fichero VACÍO"),
    Mutacion("N211", "V6-15", "T211", ARBOLES,
             "la versión histórica vulnerable deja de aceptar el árbol atacado",
             m_v6_la_version_vulnerable_deja_de_reproducir, clase=BATERIA,
             espera="NO acepta el árbol atacado"),
    Mutacion("N217", "V6-16", "T217", RAIZ_EXTERNA,
             "una instalación de la raíz externa con un fichero ALTERADO emite veredicto",
             m_v6_una_instalacion_alterada_emite_veredicto, clase=BATERIA,
             espera="InstalacionAlterada not raised"),
    Mutacion("N216", "FD-5", "T216", CONTENCION,
             "el backend `simple` se declara con nivel de árbol de procesos",
             m_fd5_el_backend_debil_se_presenta_como_fuerte, clase=BATERIA,
             espera="ContencionFuerteNoDisponible not raised"),
    Mutacion("N191", "FD-6", "T191", ADAPTADORES,
             "un recibo ABIERTO deja de dar `ambiguo` y el efecto se vuelve a ejecutar",
             m_fd6_el_recibo_abierto_se_reejecuta, clase=BATERIA,
             espera="ambiguo"),
    Mutacion("N320", "ADJ-B1", "T320", ESTADO_DURABLE,
             "la migración 0->1 vuelve a publicar la revisión 0 sin el `testigo` de `E-08`",
             m_adjb1_la_migracion_vuelve_a_omitir_el_testigo, clase=BATERIA,
             espera="un almacén heredado REAL no migró",
             casos=["MigracionHeredadaReal."
                    "test_T320_un_heredado_REAL_migra_y_publica_la_revision_esperada"]),
    Mutacion("N321", "ADJ-B1", "T321", ESTADO_DURABLE,
             "la guarda de la fundación vuelve a mirar el evento del diario y no la revisión",
             m_adjb1_la_fundacion_vuelve_a_mirar_el_diario, clase=BATERIA,
             espera="el almacén quedó inmigrable tras un corte",
             casos=["MigracionHeredadaReal."
                    "test_T321_el_almacen_que_el_defecto_dejo_roto_vuelve_a_ser_migrable"]),
    Mutacion("N330", "ADJ-B2", "T330", INTEGRIDAD,
             "el verificador de la raíz externa pierde la purga `E-10` de `sys.path`",
             m_adjb2_la_raiz_externa_pierde_la_purga, clase=BATERIA,
             espera="es un punto ejecutable SIN la purga",
             casos=["PurgaEnLaRaizExterna."
                    "test_T330_el_inventario_se_DERIVA_del_arbol_ENTERO_y_es_coherente"]),
    Mutacion("N333", "ADJ-B2", "T333", INTEGRIDAD,
             "el instalador vuelve a borrar el destino y copiar encima, e instala a medias",
             m_adjb2_el_instalador_vuelve_a_copiar_encima, clase=BATERIA,
             espera="quedó una instalación a medias en el destino",
             casos=["PurgaEnLaRaizExterna.test_T333_no_se_instala_a_medias"]),
    Mutacion("NH01", "H-01", "T330", INTEGRIDAD,
             "`validadores/huella.py` pierde la purga `E-10` y la huella vuelve a ser "
             "falsificable desde el `PYTHONPATH`",
             m_h01_la_huella_pierde_la_purga, clase=BATERIA,
             espera="es un punto ejecutable SIN la purga",
             casos=["PurgaEnLaRaizExterna."
                    "test_T330_el_inventario_se_DERIVA_del_arbol_ENTERO_y_es_coherente"]),
    Mutacion("NH03", "H-03", "T330", INTEGRIDAD,
             "el inventario vuelve a acotarse a una zona escrita a mano y deja de ver el "
             "resto del árbol",
             m_h03_el_inventario_vuelve_a_una_zona_escrita, clase=BATERIA,
             espera="el inventario no clasifica",
             casos=["PurgaEnLaRaizExterna."
                    "test_T330_el_inventario_se_DERIVA_del_arbol_ENTERO_y_es_coherente"]),
    Mutacion("NG03", "G-03", "T380", INTEGRIDAD,
             "un punto ejecutable pierde la guarda de aislamiento y el `sitecustomize` "
             "vuelve a decidir con qué primitiva se firma",
             m_g03_un_punto_pierde_la_guarda_de_aislamiento, clase=BATERIA,
             espera="sin la guarda `G-03`",
             casos=["AislamientoDeArranque."
                    "test_T380_la_guarda_alcanza_a_TODO_punto_del_inventario_derivado"]),
    Mutacion("ND01", "D-01", "T394", INTEGRIDAD,
             "el runner de la evidencia vuelve a lanzar a sus hijos SIN `env=` y el veneno "
             "del padre llega a cada batería",
             m_d01_el_runner_vuelve_a_heredar_el_entorno_de_sus_hijos, clase=BATERIA,
             espera="el entorno del padre llegó al hijo",
             casos=["AislamientoDeArranque."
                    "test_T394_el_runner_SANEA_el_entorno_de_sus_hijos_y_lo_PUBLICA"]),
    Mutacion("NH08", "H-08", "T307", INTEGRIDAD,
             "la cobertura del contraste vuelve a calcularse y a no publicarse",
             m_h08_la_cobertura_del_contraste_deja_de_publicarse, clase=BATERIA,
             espera="no publica la cobertura del contraste",
             casos=["ResultadoExactoDeLaEvidencia."
                    "test_T307g_la_COBERTURA_DEL_CONTRASTE_va_publicada_en_la_evidencia"]),
    Mutacion("N194", "FD-3", "T194", "comprobar_arranque",
             "el motor de estado durable deja de viajar al proyecto instalado",
             m_fd3_el_motor_durable_no_viaja,
             espera="no lleva el motor de estado durable"),
])


# ===========================================================================
#  `G-04` · la PROHIBICIÓN de `b.12` sobre la prioridad, y `G-08` · el protocolo
#  de preparación · `D-02` · el censo de escenarios atados
# ===========================================================================
#  Se añaden al final, sin tocar ninguna mutación anterior: el catálogo es acumulativo y una
#  mutación que se reescribe deja de demostrar lo que demostró el día que se escribió.
SELECCION = PRUEBAS_RUNTIME + "test_cardinalidad_y_seleccion.py"
RUNTIME_Y_DISPATCHER = PRUEBAS_RUNTIME + "test_runtime.py"


def m_g04_dsp_vuelve_a_subir_la_prioridad_al_postergar(raiz):
    """`T400`, `falla_si`: «la transición de postergación mueve la prioridad».

    ES EL SABOTAJE EXACTO que el revisor 1 reprodujo en el gate del 2026-09-05 y que pasaba
    DOCE baterías con `EXIT=0`, con la línea ejecutándose dieciséis veces y mutando el estado
    durable `50 → 60 → 70`. Se mecaniza aquí, y no sólo en `T269`, porque el catálogo de
    negativos es lo que se ejecuta sobre una COPIA del repositorio en cada corrida del gate:
    `T269` demuestra que la propiedad NO es decorativa, y esto demuestra que la detección
    sigue viva el día que nadie mire.

    Tiene que caer por la PROHIBICIÓN SEMÁNTICA —`PRIORIDAD_INMUTABLE`— y no por la huella
    del kernel, que saltaría con cualquier edición legítima.
    """
    _sustituir(raiz, "kernel/operativo/runtime/runtime/dispatcher.py",
               '                nuevo = dict(actual)\n'
               '                nuevo["seleccion"] = normalizar_seleccion(',
               '                nuevo = dict(actual)\n'
               '                nuevo["prioridad"] = int(actual["prioridad"]) + 10\n'
               '                nuevo["seleccion"] = normalizar_seleccion(')


def m_g04_la_invariante_deja_de_cubrir_la_prioridad(raiz):
    """`T419`, `falla_si`: «la constante que ejecuta la norma deja de coincidir con la citada».

    La otra mitad del mismo eje, y la que una prueba de comportamiento no vería: la
    invariante sigue instalada en la puerta, sigue recorriendo su lista de campos inmutables
    y esa lista deja de contener `prioridad`. Nada falla al escribir, nada falla al leer, y
    la prohibición de `b.12` se ha desactivado sin que ninguna línea diga que se desactivó.
    """
    _sustituir(raiz, "kernel/operativo/runtime/runtime/estado_util.py",
               'CAMPOS_INMUTABLES_DEL_PAQUETE = ("prioridad",)',
               'CAMPOS_INMUTABLES_DEL_PAQUETE = ("prioridad_declarada",)')


def m_g08_vuelve_la_espera_arbitraria_antes_del_killpg(raiz):
    """`T412`, `falla_si`: «la espera fija sigue en la tarea».

    `G-08` en su sede exacta: la raíz vuelve a esperar un plazo en vez de OBSERVAR los tres
    testigos, y `listo` vuelve a significar «ha pasado el tiempo que supuse». Bajo carga eso
    es lo que hacía que `T216` cayera 4 de cada 15 veces. La mutación no toca el resto del
    protocolo —los anuncios siguen saliendo— para que el rojo venga de la espera y no de que
    la batería se quede sin canal.
    """
    _sustituir(raiz, "kernel/operativo/runtime/pruebas/test_contencion.py",
               "             + _espera_observada()\n"
               '             + "sleep " + str(segundos) + "\\n")\n'
               '    return ["sh", "-c", guion]\n'
               "\n"
               "\n"
               "def tarea_sin_una_generacion(",
               '             + "sleep 0.6\\n"\n'
               '             + "echo " + LISTO + " sondeos=0\\n"\n'
               '             + "sleep " + str(segundos) + "\\n")\n'
               '    return ["sh", "-c", guion]\n'
               "\n"
               "\n"
               "def tarea_sin_una_generacion(")


def m_d02_el_censo_de_escenarios_atados_esconde_uno(raiz):
    """`T415`, `falla_si`: «un escenario nuevo entra en la clase y nadie se entera».

    ESTE SABOTAJE SE REESCRIBIÓ AL CERRARSE `D-02`, y se dice por qué. Atacaba el censo
    quitándole una entrada —`"T225": …`—, que es como se ataca un cliquet mientras tiene
    dientes. Cerrada la deuda, `CENSO_D02` está VACÍO: no hay entrada que quitar, y el
    sabotaje dejó de encajar. Mantenerlo así habría dejado el cliquet sin control negativo
    justo cuando pasa a medir su otra mitad.

    Ahora se ataca por donde el censo vacío puede ser atacado, que es además la vía por la
    que la clase volvería de verdad: se le RETIRA a un ejecutor el veredicto nominal que
    aprendió a publicar. `T162` deja de estar nombrado por `test_workspace.py`, vuelve a
    estar atado a que alguien reescriba una batería ajena, y `T415` tiene que decir que la
    clase de `D-02` ha vuelto a crecer.

    SE TOCAN LAS DOS COSAS, Y NO ES UNA CONCESIÓN. `atados_a_una_bateria_ajena` descarta a
    un escenario en cuanto su EVIDENCIA lo nombra, sin llegar a mirar la fuente: tocar sólo
    el ejecutor reproduciría el estado «lo publicará en la próxima pasada», que la propia
    prueba clasifica —bien— como retraso del registrador y no como deuda. El estado que hay
    que reproducir es aquel del que se venía: un ejecutor que NO sabe publicarlo y una
    evidencia que NO lo nombra. Eso son las dos ediciones, y las dos son la misma cosa.
    """
    _sustituir(raiz, "tooling/tests/test_workspace.py",
               '"""T162 · una fuente ya clonada se reutiliza y no se vuelve a clonar."""',
               '"""una fuente ya clonada se reutiliza y no se vuelve a clonar."""')
    _sustituir(raiz, "kernel/operativo/pruebas/evidencia/workspace-salida.txt",
               "T162 · una fuente ya clonada se reutiliza y no se vuelve a clonar. ... ok",
               "una fuente ya clonada se reutiliza y no se vuelve a clonar. ... ok")


CATALOGO.extend([
    Mutacion("NG04", "G-04", "T400", SELECCION,
             "DSP vuelve a subir la prioridad al postergar, que es el sabotaje exacto de "
             "`R1-H02` y pasaba doce baterías en verde",
             m_g04_dsp_vuelve_a_subir_la_prioridad_al_postergar, clase=BATERIA,
             espera="PRIORIDAD_INMUTABLE",
             casos=["PrioridadInmutableDeB12."
                    "test_400_la_prioridad_declarada_sobrevive_a_una_postergacion"]),
    Mutacion("NG04b", "G-04", "T419", SELECCION,
             "la lista de campos inmutables deja de contener `prioridad` y la prohibición "
             "de `b.12` se desactiva sin que ninguna línea lo diga",
             m_g04_la_invariante_deja_de_cubrir_la_prioridad, clase=BATERIA,
             espera="'prioridad' not found in",
             casos=["PrioridadInmutableDeB12."
                    "test_419_la_norma_se_cita_IGUAL_en_las_cuatro_sedes_y_una_de_ellas_la_EJECUTA"]),
    Mutacion("NG08", "G-08", "T412", CONTENCION,
             "la raíz vuelve a esperar un plazo fijo en vez de observar los tres testigos, "
             "y `listo` vuelve a ser una suposición",
             m_g08_vuelve_la_espera_arbitraria_antes_del_killpg, clase=BATERIA,
             espera="la espera arbitraria sigue en la tarea",
             casos=["ProtocoloDePreparacion."
                    "test_412_la_preparacion_es_una_condicion_OBSERVADA_y_no_una_espera"]),
    Mutacion("ND02", "D-02", "T415", RUNTIME_Y_DISPATCHER,
             "a un ejecutor se le RETIRA el veredicto nominal que aprendió a publicar, y "
             "la clase de `D-02` vuelve a crecer con el censo ya cerrado",
             m_d02_el_censo_de_escenarios_atados_esconde_uno, clase=BATERIA,
             espera="La clase de `D-02` ha vuelto a crecer",
             casos=["EscenariosAtadosAUnaBateriaAjena."
                    "test_415_ningun_escenario_NUEVO_queda_atado_a_una_bateria_ajena"]),
])
