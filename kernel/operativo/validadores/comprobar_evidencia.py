#!/usr/bin/env python3
"""comprobar_evidencia — la evidencia publicada demuestra lo que el informe afirma.

Ocho de diez ficheros de evidencia de la entrega anterior contenían «python3: can't open
file» mientras el informe afirmaba «todos EXIT 0» y «27 pruebas superadas». Nadie lo vio
porque **nada comprobaba la evidencia**: se escribía con una redirección y se daba por
buena. Editar los `.txt` a mano no habría arreglado eso; habría escondido la causa.

T158 falla si:

    · falta un fichero de evidencia requerido por el manifiesto
    · el fichero contiene un error de INVOCACIÓN del intérprete o una traza
    · no contiene el identificador o el resumen que su validador debe producir
    · afirma éxito sin una salida compatible con ese éxito
    · la evidencia corresponde a OTRO validador que el que dice
    · la ejecución que la produjo terminó con código distinto de cero
    · una cifra que el manifiesto declara DERIVABLE del corpus ya no lo describe

La última llegó tarde, y por una ejecución, no por una lectura. Bajo un intérprete sin
`tomllib` el validador `fuentes` falla, el runner —correctamente— NO sobrescribe su
evidencia, y la cobertura publicada se quedó describiendo un corpus anterior. Cabecera de
procedencia, código 0, firma de éxito y `debe_contener` seguían siendo válidos: T158 pasó.
Es la misma familia del defecto que creó T158, por otra vía — allí la evidencia estaba
CORRUPTA, aquí está intacta y CADUCADA.

ALCANCE DECLARADO: la vigencia está garantizada para lo que el manifiesto declara en
`vigencia`, hoy sólo la cobertura de T161. Los demás validadores pueden publicar cifras que
envejezcan igual, y nada lo detecta. Registrado como P-08; su solución general es materia
de F4 porque exige declarar las ENTRADAS de cada validador.

Uso:
  python3 kernel/operativo/validadores/comprobar_evidencia.py [--json] [--raiz DIR]
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-05, sobre esta zona. Con seis líneas de
#  veneno en un `sitecustomize.py` alcanzable desde `PYTHONPATH`:
#
#      $ cat veneno/sitecustomize.py
#        import hashlib; hashlib.sha256 = lambda *a, **k: _Falso()   # digest 0000…
#      $ PYTHONPATH=veneno python3.12 kernel/operativo/validadores/huella.py
#        0000000000000000                     ← la huella FORJADA sobre un árbol mutado
#      $ PYTHONPATH=veneno python3.12 kernel/operativo/validadores/comprobar_integridad.py
#        T150  SUPERADA · EXIT=0              ← VERDE sobre un árbol MUTADO
#
#  El prólogo `E-10` de abajo purga `sys.path` en su primera sentencia, y eso llega TARDE:
#  `site.py` importa `sitecustomize` mientras el intérprete arranca, antes de que la primera
#  línea de este módulo exista. Lo que cambia no es un módulo —`hashlib` es el bueno— sino
#  un atributo suyo, y el control del control de `E-10`, que mira la procedencia de `os`, no
#  lo ve. Con la guarda, este punto se reejecuta con `-I -S -E` y `sitecustomize` no llega a
#  importarse: medido en la tabla de los doce ataques de `T380`-`T399`.
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
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-04, sobre `validadores/huella.py` —el
#  instrumento que produce el número que se publica como línea base— y con seis líneas de
#  veneno: un `hashlib.py` homónimo cuyo `sha256()` devuelve siempre el digest esperado.
#
#      $ echo "# CODIGO INYECTADO" >> mutado/kernel/operativo/validadores/ads_lint.py
#      $ cd mutado && python3.12 …/huella.py                     → 8b38fb4f4b07300c
#      $ python3.12 …/comprobar_integridad.py                    → T150 FALLIDA  EXIT=1
#      $ PYTHONPATH=veneno python3.12 …/huella.py                → bc59513f7182130a
#      $ PYTHONPATH=veneno python3.12 …/comprobar_integridad.py  → T150 SUPERADA EXIT=0
#
#  `T150` es la prueba que dice «la huella detecta su edición», y bajo veneno certificaba en
#  VERDE un árbol editado. La causa: la zona `validadores/` estaba ENTERA fuera del
#  inventario de `T306`, de modo que `E-10` —declarado «CERRADO POR INVENTARIO MECÁNICO»—
#  seguía vivo justo en el aparato que produce la evidencia de la certificación.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      Alternativas: (a) importar la purga de un módulo común; (b) copiar el prólogo entero
#      —recital incluido— desde `ads_runtime.py`; (c) copiar el MECANISMO byte a byte y
#      escribir el recital de esta sede.
#      Se elige (c). Con (a) la guardia dependería de un `import`, que es exactamente lo que
#      está protegiendo: una guardia que necesita importar ya ha perdido. Con (b) el recital
#      mentiría, porque el hecho reproducido allí no es el de aquí. Con (c) `T330` exige
#      —y comprueba— que el MECANISMO sea IDÉNTICO byte a byte en todos los puntos
#      ejecutables del árbol (digest `aa219465a6dd6a04`, 1 869 bytes), mientras cada sede
#      dice qué se midió en ella. Lo que protege es el mecanismo; lo que se lee, el recital.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación
#      distinta y convertiría un fallo de entorno en un fallo del aparato. Lo que `E-10`
#      nombra es concreto: `PYTHONPATH` y el `cwd`. Se retiran ésos, se cuenta cuántos, y el
#      recuento queda en `RETIRADAS_DE_LA_RUTA`.
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


import argparse
import json
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(__file__))
import entorno  # noqa: E402
from ads_lint import Lint  # noqa: E402
from comprobar_contratos import Resultado  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DIR_EVIDENCIA = "kernel/operativo/pruebas/evidencia"

# Las banderas que la cabecera de una evidencia tiene que nombrar. No se escriben aquí por
# duplicado: se piden al módulo que las define, que es el mismo que la guarda `G-03` usa
# para reejecutar y el que el runner usa para lanzar. Tres sedes con la misma lista escrita
# tres veces es cómo se derivan las listas.
BANDERAS_EXIGIDAS_EN_LA_CABECERA = tuple(_aislamiento_g03.BANDERAS_DE_AISLAMIENTO)

# Señales de que un fichero de evidencia NO es la salida de una ejecución correcta.
# `FALLIDA` y `NO detectada` sólo se admiten donde el manifiesto declara que la salida
# contiene el resultado interno de un fixture negativo.
ERRORES_DE_INVOCACION = [
    (r"can't open file", "error de invocación del intérprete"),
    (r"No such file or directory", "fichero no encontrado al invocar"),
    (r"ModuleNotFoundError", "importación rota"),
    (r"Traceback \(most recent call last\)", "traza de excepción"),
    (r"SyntaxError", "error de sintaxis"),
]
SENALES_DE_FALLO = [
    (r"\bFALLIDA\b", "una prueba fallida"),
    (r"\bNO detectada\b", "una infracción no detectada"),
]


# ---------------------------------------------------------------------------
# VIGENCIA · recuentos que se RECALCULAN sobre el corpus vigente
#
# Cada entrada `vigencia` del manifiesto nombra uno de éstos. El nombre se resuelve aquí y
# NO por importación dinámica de una cadena arbitraria: un manifiesto no ejecuta código que
# este fichero no haya declarado. Un nombre que no esté en el registro es un FALLO —el
# mecanismo falla cerrado—, porque dar por buena una evidencia que no se sabe comprobar es
# exactamente lo que se está corrigiendo.
#
# La función NO reimplementa el recorrido: lo importa de quien lo define. Dos
# implementaciones del mismo recuento derivan, y la que miente es siempre la que nadie mira.
# ---------------------------------------------------------------------------

def _fuentes_ficheros_recorridos(base):
    import comprobar_fuentes                                    # noqa: PLC0415
    return comprobar_fuentes.ficheros_recorridos(base)


RECUENTOS_DE_VIGENCIA = {
    "fuentes.ficheros_recorridos": _fuentes_ficheros_recorridos,
}



# ---------------------------------------------------------------------------
#  `E-14` · EL RESULTADO EXACTO DE UNA BATERÍA, Y NO UNA SUBCADENA
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR: dieciséis componentes del manifiesto declaran
#  `firma_de_exito: 'OK'`, y esa firma se comprueba con `re.search`, que casa igual con la
#  salida `OK` de `unittest` y con `OK (skipped=3)`. Medido: `re.search('OK', 'OK
#  (skipped=17)')` devuelve un objeto, no `None`. Y hay 17 llamadas a `skipTest` repartidas
#  por seis baterías del runtime, ninguna contada y ninguna publicada. Una batería que se
#  saltara sus 17 casos pasaría el validador sin que nada lo dijera.
#
#  DECISIÓN · el resultado se DERIVA de la salida y se compara ENTERO
#      Alternativas: (a) endurecer cada `firma_de_exito` del manifiesto a `^OK$`; (b) derivar
#      el resultado —casos corridos, fallos, errores, saltos— de la propia salida y exigirlo
#      completo.
#      Se hacen las dos, y ésta es la que no depende de que el manifiesto esté bien escrito.
#      Con sólo (a), el día que alguien añada un componente con `firma_de_exito: 'OK'` vuelve
#      el agujero entero, y nada avisa. Con (b) el agujero no depende de una cadena: la
#      comprobación mira el resultado de `unittest` tal cual lo imprime.
#
#  DECISIÓN · el número de casos se RECUENTA sobre la salida, no se cree
#      `Ran 38 tests` es una cifra que la propia evidencia declara. Si la evidencia se edita
#      a mano —o se recorta—, esa cifra sigue diciendo lo que decía. La salida es VERBOSA:
#      cada caso imprime su desenlace (`... ok`, `... skipped ...`, `... FAIL`, `... ERROR`).
#      Se cuentan esos desenlaces y se exige que casen con la cifra declarada. Manipular el
#      contador deja de ser gratis: invalida la evidencia.
#
#  DECISIÓN · CERO saltos, salvo que el manifiesto los DECLARE uno a uno
#      `E-14` literal: si el contrato exige cero skips, cualquier skip es ROJO; si los
#      permite, debe declarar CUÁLES y POR QUÉ. `skips_permitidos` es una lista de mapas con
#      `id` y `motivo`; el recuento tiene que casar EXACTAMENTE, y cada `id` declarado tiene
#      que aparecer en la salida. Un salto no declarado es ROJO, y un salto declarado que ya
#      no ocurre también: los dos significan que la evidencia y el contrato han divergido.
LINEA_DE_RECUENTO = re.compile(r"^Ran (\d+) tests?\b", re.M)
LINEA_DE_RESULTADO = re.compile(r"^(OK|FAILED)(?:\s*\((.*)\))?\s*$", re.M)
DESENLACE_DE_CASO = re.compile(
    r"\.\.\. (ok|skipped|FAIL|ERROR|expected failure|unexpected success)\b")
CONTADORES_DEL_RESULTADO = re.compile(r"(failures|errors|skipped|expected failures|"
                                      r"unexpected successes)=(\d+)")


def _resultado_de_unittest(texto):
    """`(recuento_declarado, veredicto, contadores)` o `None` si no es salida de `unittest`."""
    recuentos = LINEA_DE_RECUENTO.findall(texto)
    resultados = LINEA_DE_RESULTADO.findall(texto)
    if not recuentos and not resultados:
        return None
    contadores = {}
    detalle = resultados[-1][1] if resultados else ""
    for nombre, valor in CONTADORES_DEL_RESULTADO.findall(detalle or ""):
        contadores[nombre] = int(valor)
    return {
        "recuentos_declarados": [int(n) for n in recuentos],
        "veredictos": [veredicto for veredicto, _detalle in resultados],
        "detalle": detalle or "",
        "contadores": contadores,
        "desenlaces_contados": len(DESENLACE_DE_CASO.findall(texto)),
    }


def _skips_declarados(comp, r):
    """La lista `skips_permitidos` del manifiesto, validada ANTES de usarse."""
    entradas = comp.get("skips_permitidos")
    if entradas is None:
        return []
    cid = comp.get("id")
    if not isinstance(entradas, list):
        r.fallo(f"manifiesto: `skips_permitidos` de '{cid}' es "
                f"{type(entradas).__name__} y tiene que ser una lista de mapas con `id` y "
                f"`motivo`")
        return []
    utilizables = []
    for pos, entrada in enumerate(entradas):
        donde = f"`skips_permitidos`[{pos}] de '{cid}'"
        if not isinstance(entrada, dict):
            r.fallo(f"manifiesto: {donde} es {type(entrada).__name__} y tiene que ser un "
                    f"mapa con `id` y `motivo`")
            continue
        faltan = [c for c in ("id", "motivo")
                  if not isinstance(entrada.get(c), str) or not entrada[c].strip()]
        if faltan:
            r.fallo(f"manifiesto: {donde} no declara {', '.join(faltan)}. Un salto "
                    f"permitido sin decir CUÁL y POR QUÉ es un salto silencioso con "
                    f"permiso escrito")
            continue
        utilizables.append(entrada)
    return utilizables


def _comprobar_aislamiento_publicado(rel, texto, r):
    """`D-01` · La cabecera de una evidencia declara con qué AISLAMIENTO se produjo.

    Se separa en una función porque la prueba `T395` la ejerce con cabeceras fabricadas: una
    comprobación que sólo se puede ejecutar corriendo el validador entero sobre el árbol
    real no se puede sabotear a propósito, y una comprobación que no se puede poner en rojo
    a propósito no se sabe si mide algo.
    """
    # 4 bis · `D-01` · LA GARANTÍA DE AISLAMIENTO VA PUBLICADA Y SE COMPRUEBA
    #
    #  HECHO REPRODUCIDO — `HALLAZGO 3` del revisor 3, gate del 2026-09-05:
    #  `registrar_evidencia.py` L212 lanzaba a sus hijos con `subprocess.run` SIN `env=`,
    #  de modo que el veneno del padre —`PYTHONPATH`, y con él `sitecustomize`— llegaba
    #  entero a cada batería. El remedio adjudicado incluye, con estas palabras, «y lo
    #  publica en la cabecera de cada evidencia»: sin la línea, quien lee no puede
    #  distinguir una corrida saneada de una heredada.
    #
    #  DECISIÓN · se exige la LÍNEA y se exige que diga las banderas, no sólo que exista
    #      Alternativas: (a) exigir que la línea esté; (b) exigir además que nombre las
    #      banderas con las que se aisló el hijo.
    #      Se elige (b). Con (a) la cabecera pasaría diciendo «aislamiento: ninguno», que
    #      es peor que no decir nada porque parece una garantía. Con (b), el día que
    #      alguien retire el `env=` o las banderas, la línea cambia y esto enrojece.
    #
    #  EL ALCANCE DE ESTA GARANTÍA, MEDIDO POR EL AUDITOR INDEPENDIENTE (hallazgo 9)
    #      Esta línea la escribe el PADRE sobre el proceso que lanzó, y esta comprobación la
    #      lee como texto. Contra una REGRESIÓN —alguien retira el `env=`, alguien quita una
    #      bandera— funciona: la línea cambia sola y esto enrojece, que es para lo que se
    #      hizo. Contra un EDITOR DELIBERADO no funciona: reescribir la línea a mano en una
    #      evidencia ya confirmada no cambia ningún veredicto, así que `T350` pasa, y aquí
    #      sólo se comprueba que la línea diga lo que debe decir. El auditor lo demostró
    #      además con una cifra del cuerpo —`sed -i 's/\b518\b/519/g'` sobre
    #      `fuentes-salida.txt`— y los dos validadores siguieron en verde.
    #
    #      NO SE FINGE QUE ESTO LO CIERRA. Lo que un fichero editable declara sobre sí mismo
    #      no puede demostrar su propia procedencia, y la prueba de procedencia de verdad
    #      —un digest que calcule el HIJO y que no pase por las manos del padre— es otro
    #      aparato: cambiaría los bytes de las 38 evidencias y toca el contrato de
    #      aislamiento, que es de otro propietario. Queda como PETICIÓN, escrita aquí, que
    #      es donde la encuentra quien lee esta comprobación y podría creerse más de lo que
    #      hay. Quien SÍ juzga que la zona `EVIDENCIA` no mute es `V6-10` en el verificador
    #      de admisión, y ahí la condición es INMUTABLE.
    m_aisl = re.search(r"^# aislamiento:\s*(.+)$", texto, re.M)
    if not m_aisl:
        r.fallo(f"{rel}: su cabecera no publica con qué AISLAMIENTO se lanzó el proceso "
                f"que la produjo. Es la garantía que `HALLAZGO 3` pidió publicar, y una "
                f"garantía que no se publica no la puede comprobar nadie. Regenérala "
                f"con registrar_evidencia.py")
    else:
        declarado = m_aisl.group(1)
        faltan = [b for b in BANDERAS_EXIGIDAS_EN_LA_CABECERA if b not in declarado]
        if faltan:
            r.fallo(f"{rel}: su cabecera declara el aislamiento «{declarado.strip()}» y "
                    f"no nombra {' '.join(faltan)}. El hijo que produjo esta evidencia "
                    f"no se lanzó aislado, o el runner dejó de aislarlo")
        # Y la familia `PYTHON*` no puede estar entre las variables ENTREGADAS. Es la
        # que trae el gancho: `PYTHONPATH` lleva al `sitecustomize`, `PYTHONSTARTUP`
        # ejecuta código antes que nadie y `PYTHONHOME` mueve la biblioteca estándar.
        entregadas = re.search(r"entorno CONSTRUIDO con \d+ variables \(([^)]*)\)",
                               declarado)
        coladas = [v for v in (entregadas.group(1).split() if entregadas else [])
                   if v.startswith("PYTHON")]
        if coladas:
            r.fallo(f"{rel}: su cabecera declara que al hijo se le entregaron "
                    f"{' '.join(coladas)}. La familia `PYTHON*` es por donde entra el "
                    f"gancho, y el entorno del hijo se construye sin ella")


def _comprobar_resultado_exacto(rel, comp, texto, r):
    """`E-14` · el resultado EXACTO: casos corridos, fallos, errores y saltos."""
    resultado = _resultado_de_unittest(texto)
    if resultado is None:
        return                      # no es una batería de `unittest`: nada que exigir aquí

    if len(resultado["recuentos_declarados"]) != 1 or len(resultado["veredictos"]) != 1:
        r.fallo(f"{rel}: la salida no tiene EXACTAMENTE un `Ran N tests` y un resultado "
                f"final ({len(resultado['recuentos_declarados'])} recuentos, "
                f"{len(resultado['veredictos'])} resultados). Dos corridas pegadas en un "
                f"fichero permiten publicar la buena y esconder la mala")
        return

    declarado = resultado["recuentos_declarados"][0]
    contados = resultado["desenlaces_contados"]
    if contados != declarado:
        r.fallo(f"{rel}: declara `Ran {declarado} tests` y su salida contiene {contados} "
                f"desenlaces de caso. La cifra publicada no describe la corrida que la "
                f"acompaña: manipular el contador INVALIDA la evidencia")

    if resultado["veredictos"][0] != "OK":
        r.fallo(f"{rel}: la batería NO terminó en OK ({resultado['veredictos'][0]} "
                f"{resultado['detalle']})")
        return

    contadores = resultado["contadores"]
    for prohibido in ("failures", "errors", "expected failures", "unexpected successes"):
        if contadores.get(prohibido):
            r.fallo(f"{rel}: el resultado declara `{prohibido}={contadores[prohibido]}` y "
                    f"aun así dice OK. Un éxito con {prohibido} no es un éxito")

    saltados = contadores.get("skipped", 0)
    permitidos = _skips_declarados(comp, r)
    if saltados and not permitidos:
        r.fallo(f"{rel}: la corrida SALTÓ {saltados} caso(s) y el manifiesto no declara "
                f"ninguno. `OK (skipped={saltados})` no es `OK`: los casos saltados no "
                f"demuestran nada y su ausencia no se publica")
    elif permitidos and saltados != len(permitidos):
        r.fallo(f"{rel}: el manifiesto declara {len(permitidos)} salto(s) permitido(s) y la "
                f"corrida saltó {saltados}. Un salto de más no está declarado; uno de menos "
                f"significa que el contrato describe una corrida que ya no ocurre")
    for entrada in permitidos:
        if entrada["id"] not in texto:
            r.fallo(f"{rel}: el manifiesto permite el salto '{entrada['id']}' y la salida "
                    f"no lo menciona. Un salto declarado que no aparece no se puede "
                    f"contrastar con nada")

def cargar_manifiesto(base):
    ruta = os.path.join(base, "kernel/operativo/validadores/validadores.yaml")
    with open(ruta, encoding="utf-8") as fh:
        return (yaml.safe_load(fh) or {}).get("componentes") or []


# ---------------------------------------------------------------------------
#  `11-ARQ` §19, CONTRATO 3 · LA GUARDIA DE ENTORNO, EJERCIDA
# ---------------------------------------------------------------------------
#  El contrato dice dónde va la guardia: «el punto de entrada del runner … y el mismo
#  prólogo en los tres validadores que importan `tomllib`, PARA QUE EJECUTARLOS SUELTOS NO
#  ELUDA LA GUARDIA». Ponerla es la mitad; la otra mitad es que quitarla se note.
#
#  HECHO REPRODUCIDO ANTES DE CORREGIR, con el Python 3.10.12 del PATH:
#      $ python3 kernel/operativo/validadores/comprobar_evidencia.py
#      T158  SUPERADA  La evidencia publicada demuestra lo que el informe afirma
#      1 superadas · 0 fallidas          → rc=0
#  Verde, código 0, sobre una evidencia que en ese entorno NADIE puede regenerar.
#
#  CÓMO SE EJERCE SIN DESINSTALAR PYTHON. `entorno.py` admite `ADS_ENTORNO_VERSION_MINIMA`
#  para SUBIR la exigencia —nunca para bajarla—, y dice que ése es su único uso legítimo:
#  probar la rama de fallo. Se lanza cada validador con la exigencia por encima de
#  cualquier intérprete y se exige que termine con el código propio de «no se pudo
#  ejecutar». Si alguien quita el prólogo, el validador corre normalmente, sale con 0 y
#  esta comprobación se pone ROJA. Es el control que el hallazgo pide.
#
#  El marcador `ADS_ENTORNO_SONDA` impide la recursión: con el prólogo puesto, el hijo
#  muere antes de leerlo; sin el prólogo, el hijo llega hasta aquí, ve el marcador y no
#  lanza otra sonda. Sin él, un validador sin guardia se llamaría a sí mismo sin fin.

MARCADOR_DE_SONDA = "ADS_ENTORNO_SONDA"

# Los validadores que dependen de `tomllib`, DIRECTA o TRANSITIVAMENTE, y su cadena. No es
# una lista de comodidad: cada uno se ejerce, y la cadena está escrita para que nadie tenga
# que deducirla del `import`, que es donde una dependencia transitiva se esconde.
CON_GUARDIA_DE_ENTORNO = [
    ("comprobar_fuentes.py",
     "lee `SOURCES.toml` con `tooling/workspace.py`, que usa `tomllib`"),
    ("comprobar_evidencia.py",
     "recalcula la vigencia llamando a `comprobar_fuentes`, que lo usa"),
    ("comprobar_arranque.py",
     "invoca `workspace.py check` en el proyecto creado, que usa `tomllib`"),
]

# `SIN_GUARDIA_TODAVIA` queda VACÍA y NO se borra, por la misma razón por la que
# `admision` conserva su `fuera_de_alcance` vacío: su ausencia haría indistinguible «no
# falta ninguno» de «ya nadie lo publica», que son cosas muy distintas. Los TRES validadores
# que `CONTRATO 3` nombra llevan su prólogo, y el tercero —`comprobar_arranque.py`— lo ganó
# en la pasada de corrección del 2026-09-04: bajo 3.10 publicaba `T148 FALLIDA … workspace
# check falla (exit 78)` con código 1, o sea el entorno insuficiente disfrazado de defecto
# del producto.
SIN_GUARDIA_TODAVIA = []


def _sonda_de_entorno(script):
    """Ejecuta `script` con la exigencia subida por encima de cualquier intérprete."""
    import subprocess                                            # noqa: PLC0415
    ambiente = dict(os.environ)
    ambiente["ADS_ENTORNO_VERSION_MINIMA"] = "99.0"
    ambiente[MARCADOR_DE_SONDA] = "1"
    return subprocess.run([sys.executable, script, "--json"],
                          capture_output=True, text=True, env=ambiente)


def _comprobar_la_guardia_de_entorno(base, r):
    if os.environ.get(MARCADOR_DE_SONDA):
        return                                   # se está EJECUTANDO como sonda: no anidar
    for nombre, cadena in CON_GUARDIA_DE_ENTORNO:
        script = os.path.join(base, "kernel/operativo/validadores", nombre)
        if not os.path.isfile(script):
            r.fallo(f"{nombre}: no existe, y el CONTRATO 3 exige su prólogo de entorno")
            continue
        proc = _sonda_de_entorno(script)
        if proc.returncode != entorno.CODIGO_ENTORNO_INSUFICIENTE:
            r.fallo(
                f"{nombre}: con la exigencia de intérprete por encima de la disponible "
                f"terminó con código {proc.returncode} y no con "
                f"{entorno.CODIGO_ENTORNO_INSUFICIENTE}. Le falta el prólogo "
                f"`entorno.exigir()`, y {cadena}: ejecutarlo suelto ELUDE la guardia "
                f"(`11-ARQ` §19, CONTRATO 3)")
        elif "ENTORNO INSUFICIENTE" not in proc.stderr:
            r.fallo(f"{nombre}: sale con el código de entorno insuficiente pero sin decir "
                    f"por qué. Un código sin mensaje no distingue un entorno de un fallo")


def t158_evidencia(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T158", "La evidencia publicada demuestra lo que el informe afirma")
    # La guardia PRIMERO: una evidencia intacta bajo un intérprete que no pudo regenerarla
    # es exactamente la evidencia CADUCADA que este validador existe para no dar por buena.
    _comprobar_la_guardia_de_entorno(base, r)
    componentes = cargar_manifiesto(base)
    esperados = {}

    for comp in componentes:
        if comp.get("tipo") != "validador" or not comp.get("evidencia"):
            continue
        esperados[comp["evidencia"]] = comp
        if comp.get("se_excluye_de_su_propia_comprobacion"):
            continue
        rel = os.path.join(DIR_EVIDENCIA, comp["evidencia"])
        ruta = os.path.join(base, rel)

        # 1 · existe
        if not os.path.isfile(ruta):
            r.fallo(f"{rel}: falta la evidencia de '{comp['id']}', que el manifiesto exige")
            continue
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        if not texto.strip():
            r.fallo(f"{rel}: está vacío. Un fichero vacío no es evidencia de nada")
            continue

        # 2 · errores de invocación: la causa exacta del defecto anterior
        for patron, que in ERRORES_DE_INVOCACION:
            if re.search(patron, texto):
                r.fallo(f"{rel}: contiene {que}. No es la salida de una ejecución "
                        f"correcta: es el mensaje de que la ejecución no ocurrió")

        # 3 · la cabecera dice de QUIÉN es y con qué código terminó
        m_id = re.search(r"^# evidencia de:\s*(\S+)", texto, re.M)
        m_orden = re.search(r"^# orden:\s*(.+)$", texto, re.M)
        m_cod = re.search(r"^# codigo:\s*(-?\d+)", texto, re.M)
        if not (m_id and m_orden and m_cod):
            r.fallo(f"{rel}: sin cabecera de procedencia. Una evidencia que no dice qué "
                    f"orden la produjo ni con qué código no se puede auditar")
            continue

        # 4 · corresponde a SU validador, no a otro
        if m_id.group(1) != comp["id"]:
            r.fallo(f"{rel}: dice ser evidencia de '{m_id.group(1)}' y ocupa el fichero de "
                    f"'{comp['id']}'")
        script = comp["script"]
        if script not in m_orden.group(1):
            r.fallo(f"{rel}: su orden «{m_orden.group(1).strip()}» no invoca {script}")
        if not re.search(r"\.py(\s|$)", m_orden.group(1)):
            r.fallo(f"{rel}: su orden no invoca un script terminado en .py — es exactamente "
                    f"el defecto que corrompió la evidencia anterior")

        _comprobar_aislamiento_publicado(rel, texto, r)

        # 5 · el código registrado es cero
        if m_cod.group(1) != "0":
            r.fallo(f"{rel}: registra código {m_cod.group(1)}. Una ejecución que no terminó "
                    f"bien no se publica como evidencia")

        # 6 · afirma éxito con una salida compatible con ese éxito
        firma = comp.get("firma_de_exito")
        if firma and not re.search(firma, texto):
            r.fallo(f"{rel}: no contiene el resumen de éxito que su validador produce "
                    f"(/{firma}/). Afirma un éxito que su salida no respalda")
        for marca in comp.get("debe_contener") or []:
            if marca not in texto:
                r.fallo(f"{rel}: no menciona '{marca}', que su validador debe producir")

        # 6 bis · `E-14` · el RESULTADO EXACTO de una batería de `unittest`, y no una
        #         subcadena. `OK` no puede seguir equivaliendo a `OK (skipped=N)`.
        _comprobar_resultado_exacto(rel, comp, texto, r)

        # 7 · señales de fallo, salvo donde el manifiesto declara que son de un fixture
        if not comp.get("contiene_salida_de_fixture"):
            for patron, que in SENALES_DE_FALLO:
                if re.search(patron, texto):
                    r.fallo(f"{rel}: contiene {que}, y su manifiesto no declara que su "
                            f"salida incluya el resultado interno de un fixture negativo")

    # 8 · el manifiesto está completo: todo `.py` de validadores/ está declarado.
    #     Un validador nuevo sin registrar quedaría fuera de la evidencia en silencio,
    #     que es la forma callada del mismo defecto.
    dir_val = os.path.join(base, "kernel/operativo/validadores")
    # `dir` permite declarar un ejecutable que vive fuera de validadores/ —las pruebas de
    # workspace prueban tooling, no el corpus—. Sólo los que SÍ viven aquí cuentan para la
    # comprobación de «nada sobra en el directorio».
    declarados = {c.get("script") for c in componentes
                  if not c.get("dir") or c.get("dir") == "kernel/operativo/validadores"}
    for f in sorted(os.listdir(dir_val)):
        if f.endswith(".py") and f not in declarados:
            r.fallo(f"validadores/{f}: existe y el manifiesto no lo declara. Quedaría "
                    f"fuera de la evidencia sin que nada lo dijera")
    for c in componentes:
        script = c.get("script", "")
        if not script.endswith(".py"):
            r.fallo(f"manifiesto: '{c.get('id')}' declara '{script}', que no termina en .py")
        else:
            directorio = c.get("dir") or "kernel/operativo/validadores"
            if not os.path.isfile(os.path.join(base, directorio, script)):
                r.fallo(f"manifiesto: '{c.get('id')}' declara {directorio}/{script}, "
                        f"que no existe")

    # 9 · nada sobra en el directorio: una evidencia huérfana es una que nadie regenera
    dir_ev = os.path.join(base, DIR_EVIDENCIA)
    if os.path.isdir(dir_ev):
        for f in sorted(os.listdir(dir_ev)):
            if f.endswith(".txt") and f not in esperados:
                r.fallo(f"{DIR_EVIDENCIA}/{f}: no lo declara ningún validador del "
                        f"manifiesto. Nadie lo regenera y nadie responde de él")

    # 10 · VIGENCIA · la evidencia describe el corpus que hay, no el que había.
    #
    # Va LA ÚLTIMA a propósito. `comprobar_negativos` publica el PRIMER fallo de cada
    # mutación como su detalle: si esta comprobación se adelantara, una mutación que además
    # cambie el tamaño del corpus se registraría con el motivo equivocado.
    _vigencia(base, componentes, r)
    return r


def _entradas_de_vigencia(comp, r):
    """Valida el contrato `vigencia` ANTES de usarlo, y devuelve las entradas utilizables.

    Un manifiesto mal escrito es un defecto de conformidad, y se dice con un fallo
    explicativo. Lo que NO puede hacer es reventar: un traceback no dice qué corregir, tumba
    las comprobaciones que venían detrás, y deja la evidencia sin comprobar sin que nadie
    declare que quedó sin comprobar. Ocurrió con `patron` ausente y un `KeyError`.

    Cada condición se comprueba por separado y con su mensaje. No hay `except Exception`:
    convertir un defecto en silencio es el mismo error con otra forma.
    """
    entradas = comp.get("vigencia")
    if entradas is None:
        return []
    cid = comp.get("id")

    if not isinstance(entradas, list):
        r.fallo(f"manifiesto: `vigencia` de '{cid}' es {type(entradas).__name__} y tiene que "
                f"ser una lista de entradas. Una sola entrada suelta no se lee como lista")
        return []

    # Quien está exento de su propia comprobación no puede declarar vigencia: estaría
    # comprobando su evidencia contra sí mismo y aceptándose.
    if comp.get("se_excluye_de_su_propia_comprobacion"):
        r.fallo(f"manifiesto: '{cid}' declara `vigencia` y está exento de su propia "
                f"comprobación. Comprobaría su evidencia contra sí mismo")
        return []

    if not comp.get("evidencia"):
        r.fallo(f"manifiesto: '{cid}' declara `vigencia` y no declara fichero de evidencia. "
                f"No hay dónde leer la cifra que dice comprobar")
        return []

    utilizables, vistos = [], set()
    for pos, e in enumerate(entradas):
        donde = f"`vigencia`[{pos}] de '{cid}'"
        if not isinstance(e, dict):
            r.fallo(f"manifiesto: {donde} es {type(e).__name__} y tiene que ser un mapa con "
                    f"`id`, `patron`, `recuento` y `motivo`")
            continue

        # campos obligatorios: existen, son texto y no están vacíos
        faltan = False
        for campo in ("id", "patron", "recuento", "motivo"):
            valor = e.get(campo)
            if valor is None:
                r.fallo(f"manifiesto: {donde} no declara `{campo}`. Los cuatro campos son "
                        f"obligatorios: sin ellos no se sabe qué se comprueba ni por qué")
                faltan = True
            elif not isinstance(valor, str):
                r.fallo(f"manifiesto: {donde} declara `{campo}` como "
                        f"{type(valor).__name__} y tiene que ser texto")
                faltan = True
            elif not valor.strip():
                r.fallo(f"manifiesto: {donde} declara `{campo}` vacío")
                faltan = True
        if faltan:
            continue

        eid = e["id"].strip()
        if eid in vistos:
            r.fallo(f"manifiesto: la vigencia '{eid}' está declarada dos veces en '{cid}'. "
                    f"Dos comprobaciones con el mismo identificador no se distinguen en el "
                    f"informe, y una tapa a la otra")
            continue
        vistos.add(eid)

        # el patrón compila, y ofrece el grupo de captura del que sale la cifra
        try:
            patron = re.compile(e["patron"])
        except re.error as exc:
            r.fallo(f"manifiesto: la vigencia '{eid}' de '{cid}' no es una expresión regular "
                    f"válida ({exc}). Nunca casaría, y su comprobación pasaría siempre")
            continue
        if patron.groups < 1:
            r.fallo(f"manifiesto: la vigencia '{eid}' de '{cid}' no declara ningún grupo de "
                    f"captura. Sin grupo no hay cifra que extraer, y comprobar la presencia "
                    f"del texto es lo que `debe_contener` ya hace")
            continue

        calcular = RECUENTOS_DE_VIGENCIA.get(e["recuento"])
        if calcular is None:
            r.fallo(f"manifiesto: la vigencia '{eid}' de '{cid}' declara el recuento "
                    f"'{e['recuento']}', que no está registrado en RECUENTOS_DE_VIGENCIA. Sin "
                    f"implementación no se comprueba nada, y una comprobación que no existe "
                    f"no puede darse por superada")
            continue

        utilizables.append((eid, patron, calcular))
    return utilizables


def _vigencia(base, componentes, r):
    for comp in componentes:
        if comp.get("tipo") != "validador":
            continue
        if comp.get("vigencia") is None:
            continue

        entradas = _entradas_de_vigencia(comp, r)
        if not entradas:
            continue

        rel = os.path.join(DIR_EVIDENCIA, comp["evidencia"])
        ruta = os.path.join(base, rel)
        if not os.path.isfile(ruta):
            continue                       # su ausencia ya se ha reportado más arriba
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()

        for eid, patron, calcular in entradas:
            m = patron.search(texto)
            if not m:
                r.fallo(f"{rel}: la vigencia '{eid}' no encuentra su cifra "
                        f"(/{patron.pattern}/). La evidencia dejó de publicar el valor que se "
                        f"comprueba")
                continue
            crudo = m.group(1)
            if crudo is None or not crudo.strip().lstrip("-").isdigit():
                r.fallo(f"{rel}: la vigencia '{eid}' captura «{crudo}», que no es un entero. "
                        f"Una vigencia compara recuentos: su grupo tiene que capturar la cifra")
                continue
            publicado = int(crudo)
            actual = calcular(base)
            if publicado != actual:
                r.fallo(f"{rel}: la vigencia '{eid}' publica {publicado} y el corpus vigente "
                        f"da {actual}. La evidencia está CADUCADA: describe un corpus que ya "
                        f"no existe. Regenérala con registrar_evidencia.py — no la edites")
# ===========================================================================
#  `T350` · `ADJ-G2` · EL `estado` DE UNA PRUEBA NO ES UN CAMPO A MANO
# ===========================================================================
#  HECHO REPRODUCIDO, y no hizo falta mutar nada porque el árbol ya lo publicaba:
#
#      $ awk '/^id: T273$/,/^```$/' pruebas/T270-T289-contratos-19-y-composicion.md
#        estado: prueba-fallida
#      $ sed -n '220p' pruebas/REGISTRO-generado.md
#        | [T273] | … | **PRUEBA FALLIDA** | evidencia/composicion-procesos-salida.txt |
#      $ head -9 pruebas/evidencia/composicion-procesos-salida.txt
#        # codigo:  0
#        T273  SUPERADA  Todo par del catálogo estático de D104 tiene su <CAP>:revision
#        4 superadas · 0 fallidas
#
#  Tres sedes decían VERDE, la cuarta publicaba `PRUEBA FALLIDA`, y los 34 validadores
#  estaban en verde porque NINGUNO contrastaba ese campo contra nada. `REGISTRO.md` escribe
#  «ninguna prueba sube de estado por argumento»; esta prueba es esa regla, mecanizada.
#
#  DECISIÓN · la fórmula NO se reescribe aquí: se IMPORTA de `registro_pruebas`
#      Alternativas: (a) una copia de la derivación en este validador; (b) importarla de la
#      sede que la publica.
#      Se elige (b), y es la misma regla que `V6-19` impone en el paquete de admisión: dos
#      definiciones de «qué estado tiene esta prueba» son dos verdades, y la divergencia
#      entre ellas aparece el día en que una se toca y la otra no. Si la sede no se puede
#      importar, esta prueba NO EMITE un verde: falla con su motivo.
def t350_estado_derivado_de_la_evidencia(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T350", "El estado declarado de cada escenario lo sostiene su evidencia")
    try:
        import registro_pruebas                                       # noqa: PLC0415
    except Exception as error:                                        # noqa: BLE001
        r.fallo("no se puede importar `registro_pruebas`, que es la SEDE de la derivación "
                f"del estado ({type(error).__name__}: {error}). Sin ella no se calcula una "
                f"equivalente: no se emite")
        return r
    for nombre in ("derivar_estado", "contraste_de_estados", "veredictos_publicados"):
        if not hasattr(registro_pruebas, nombre):
            r.fallo(f"`registro_pruebas` no ofrece `{nombre}`: la sede de la derivación del "
                    f"estado ha dejado de publicarla, y este validador no la reimplementa")
            return r

    lint = Lint(base, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    escenarios = [d for t, d, _f, _l in lint.bloques if t == "escenario"]
    if not escenarios:
        r.fallo("no se ha cargado ni un bloque `ads:escenario`: sin escenarios este "
                "contraste no dice nada, y una lista vacía no es un corpus limpio")
        return r

    divergencias, contrastados, sin_contraste = registro_pruebas.contraste_de_estados(
        escenarios, base)
    for d in divergencias:
        motivo = " · ".join(d["motivos"]) or "los veredictos publicados dicen otra cosa"
        r.fallo(f"{d['id']}: declara `estado: {d['declarado']}` y su evidencia sostiene "
                f"`{d['derivado']}` — {motivo}. Ninguna prueba sube ni baja de estado por "
                f"argumento (`pruebas/REGISTRO.md`)")

    # 2 · el estado por encima de `validador-implementado` EXIGE evidencia declarada.
    for datos in escenarios:
        estado = datos.get("estado")
        if estado in ("prueba-ejecutada", "prueba-superada", "prueba-fallida") \
                and not (datos.get("evidencia") or "").strip():
            r.fallo(f"{datos.get('id')}: declara `{estado}` y no declara `evidencia`. Un "
                    f"estado que afirma una ejecución sin salida registrada es exactamente "
                    f"lo que la regla dura de `REGISTRO.md` prohíbe")

    # 3 · la evidencia que un escenario cita tiene que ser una que ALGUIEN REGENERE. Una
    #     evidencia fuera del manifiesto no la publica el runner y nadie responde de ella:
    #     es la forma en que `T277` acabó citando un fichero que no ha existido nunca.
    declaradas = {c["evidencia"] for c in cargar_manifiesto(base) if c.get("evidencia")}
    for datos in escenarios:
        evidencia = (datos.get("evidencia") or "").strip()
        if evidencia and os.path.basename(evidencia) not in declaradas:
            r.fallo(f"{datos.get('id')}: cita la evidencia `{evidencia}`, que el manifiesto "
                    f"canónico no declara. Nadie la regenera y nadie responde de ella")

    # 4 · LA EVIDENCIA ES LA CONFIRMADA, y no una editada encima. Se contrasta contra el
    #     blob de `HEAD`. Donde no hay repositorio —la copia que `comprobar_negativos`
    #     fabrica no lleva `.git`— el canal NO SE HACE, y se DICE: una comprobación omitida
    #     en silencio es indistinguible de una comprobación que pasa.
    r.nota = _contrastar_contra_head(base, escenarios, r)
    # `H-08` · LA CIFRA DEL CONTRASTE SE PUBLICA, PORQUE SI NO, NO EXISTE
    #
    #     HECHO REPRODUCIDO POR LA AUDITORÍA INDEPENDIENTE DEL 2026-09-04: la línea base
    #     afirmaba «160 escenarios contrastados · 107 no contrastables»; el árbol producía
    #     `193 contrastados · 74 no contrastables`, y `grep -rn "160 contrastados\|107 no
    #     contrastables"` sobre el árbol entero devolvía VACÍO. `r.nota_cobertura` se
    #     CALCULABA aquí y no la imprimía nadie: la cifra que encabezaba la línea base no
    #     era reproducible desde ninguna evidencia, y la que el árbol produce era otra.
    #
    #     DECISIÓN · se publica la COBERTURA y NO se publica `r.nota` ENTERA
    #         `nota_cobertura` se deriva del corpus y de la evidencia: mismo árbol, mismos
    #         bytes. `r.nota` cuenta cuántas evidencias difieren del blob de `HEAD` y cuáles
    #         no están confirmadas todavía, y eso cambia entre el minuto anterior y el
    #         posterior a un `git commit`. Meterla en una salida que se publica como
    #         evidencia rompería el determinismo byte a byte que `T158` exige, y una
    #         evidencia que cambia sola no vale como evidencia.
    #
    #     CORRECCIÓN · SE PUBLICA SI EL CANAL CORRIÓ, QUE ES LA PARTE QUE NO CAMBIA SOLA
    #         HALLADO POR EL AUDITOR INDEPENDIENTE. La decisión de arriba era correcta en su
    #         motivo y demasiado ancha en su consecuencia: descartaba la nota ENTERA, y con
    #         ella la única frase que el propio canal escribe para no ser mudo —«el contraste
    #         NO se ha hecho, y no se da por hecho»—. Efecto medido: sobre el corpus que
    #         `comprobar_negativos` copia sin `.git`, el canal no corre y la evidencia
    #         publicada es BYTE A BYTE indistinguible de una corrida donde sí corrió. Es
    #         exactamente el hecho que `D-05` existe para cerrar, y `T427` y `T428` asertaban
    #         sobre una cadena que en producción se tiraba a la basura.
    #         Así que se parte en dos: si el canal se EJERCIÓ o no —que depende del árbol y
    #         no del reloj, y por tanto es determinista— se publica siempre; el detalle
    #         volátil —cuántas difieren hoy, cuáles están sin confirmar— sigue fuera.
    r.nota_cobertura = (f"contrastados {len(contrastados)} · no contrastables "
                        f"{len(sin_contraste)} · divergencias {len(divergencias)}")
    r.nota_cobertura += (" · contraste contra el blob de HEAD: "
                         + ("EJERCIDO" if os.path.isdir(os.path.join(base, ".git"))
                            else "NO SE HA HECHO — no hay repositorio Git en la raíz, y no "
                                 "se da por hecho"))
    # `H-02` · y el DESGLOSE de los no contrastables por el estado que DECLARAN. La cifra
    # agregada mezclaba a los que no afirman ninguna ejecución con los catorce que
    # afirmaban `prueba-superada` sobre una evidencia que no los nombra, y esa mezcla es
    # exactamente lo que los mantuvo invisibles.
    reparto = registro_pruebas.no_contrastables_por_estado(escenarios, base)
    r.nota_cobertura += (" · no contrastables por estado declarado: "
                         + " ".join(f"{e}={n}" for e, n in sorted(reparto.items())))
    return r


# `ADJ-G2` · LA EVIDENCIA DE OTRO COMMIT, Y DÓNDE ESTÁ EL LÍMITE DE ESTA COMPROBACIÓN
#
#     DECISIÓN · falla el VEREDICTO QUE CAMBIA, no el fichero que difiere
#         La primera versión de esta comprobación exigía que la evidencia del árbol de
#         trabajo fuera BYTE A BYTE la confirmada en `HEAD`, y se midió lo que eso hace en
#         una pasada de verdad: en cuanto el runner regenera una evidencia y todavía no se
#         ha confirmado, `T350` se pone roja. Ocurrió el mismo día, con
#         `recuentos-salida.txt` regenerada y sin confirmar. Un guardián que da rojo cada
#         vez que alguien trabaja se apaga, y apagado no protege de nada.
#         Lo que este hallazgo tiene que impedir es que una evidencia se EDITE para que
#         diga otra cosa. Eso se mide exactamente: se derivan los veredictos de la versión
#         de `HEAD` y los de la del disco, y si para un mismo escenario NO COINCIDEN, la
#         evidencia ha cambiado de dictamen y eso es ROJO. Una regeneración legítima cambia
#         cifras y no cambia dictámenes.
#         Y la mitad que esta comprobación NO cubre se DICE en vez de suponerse: que el
#         contenido de `kernel/operativo/pruebas/evidencia/` no mute sin declararlo lo juzga
#         el verificador de admisión, cuya zona `EVIDENCIA` tiene condición INMUTABLE
#         (`V6-10`), y ninguna declaración de admisión la levanta.
def _contrastar_contra_head(base, escenarios, r):
    """¿Ha cambiado de DICTAMEN alguna evidencia entre `HEAD` y el árbol de trabajo?"""
    import subprocess                                                 # noqa: PLC0415
    import registro_pruebas                                           # noqa: PLC0415
    if not os.path.isdir(os.path.join(base, ".git")):
        return ("sin repositorio Git en la raíz: el contraste de la evidencia contra el "
                "blob de HEAD NO se ha hecho, y no se da por hecho")
    por_evidencia = {}
    for datos in escenarios:
        evidencia = (datos.get("evidencia") or "").strip()
        if evidencia:
            por_evidencia.setdefault(os.path.basename(evidencia), []).append(datos)
    hechas, sin_confirmar, regeneradas, borradas = 0, [], [], []
    for nombre in sorted(por_evidencia):
        rel = os.path.join(DIR_EVIDENCIA, nombre)
        ruta = os.path.join(base, rel)
        if not os.path.isfile(ruta):
            # `D-05`, ATAQUE 9, HALLADO POR EL AUDITOR INDEPENDIENTE. Esto era `continue`, y
            # con él BORRAR el fichero pasaba en verde mientras VACIARLO era rojo: dos
            # gestos con el mismo efecto —el dictamen deja de existir— y veredictos
            # opuestos. Un fichero que `HEAD` tiene y el árbol de trabajo no es un dictamen
            # retirado, exactamente igual que uno vaciado, y se juzga igual.
            proceso = subprocess.run(["git", "-C", base, "cat-file", "-e", "HEAD:" + rel],
                                     capture_output=True)
            if proceso.returncode == 0:
                borradas.append(rel)
                r.fallo(f"{rel}: `HEAD` tiene esta evidencia confirmada y en el árbol de "
                        f"trabajo NO EXISTE. Borrar una evidencia retira todos los "
                        f"dictámenes que sostenía, igual que vaciarla, y no hay ninguna "
                        f"ejecución que respalde esa retirada")
            continue
        proc = subprocess.run(["git", "-C", base, "show", "HEAD:" + rel],
                              capture_output=True)
        if proc.returncode != 0:
            sin_confirmar.append(rel)
            continue
        with open(ruta, "rb") as manejador:
            en_disco = manejador.read()
        hechas += 1
        if proc.stdout == en_disco:
            continue
        regeneradas.append(rel)
        confirmada = proc.stdout.decode("utf-8", "replace")
        ahora = en_disco.decode("utf-8", "replace")
        for datos in por_evidencia[nombre]:
            identificador = datos.get("id", "")
            antes = registro_pruebas.veredictos_publicados(confirmada, identificador)
            despues = registro_pruebas.veredictos_publicados(ahora, identificador)
            # `D-05` · HECHO REPRODUCIDO POR `T425`, MECANIZANDO EL ATAQUE. Esta guarda
            # era `if not (antes and despues): continue`, y con ella el ataque MÁS FUERTE
            # de todos —vaciar la evidencia, o reescribirla para que deje de nombrar al
            # escenario— pasaba en VERDE: sin veredictos «después» no había nada que
            # comparar, y no comparar se trataba como no haber encontrado nada raro. Al
            # revés: que `HEAD` juzgara este escenario y el árbol de trabajo ya no lo
            # juzgue es la forma más limpia de borrar un dictamen incómodo.
            if antes and not despues:
                r.fallo(f"{rel}: la versión confirmada en `HEAD` publica {sorted(antes)} "
                        f"para `{identificador}` y la del árbol de trabajo NO PUBLICA "
                        f"NINGUNO. Un escenario que deja de estar juzgado por su propia "
                        f"evidencia no es un escenario sin novedad: es un dictamen "
                        f"retirado sin una ejecución que lo respalde")
                continue
            if not (antes and despues):
                # `HEAD` no lo juzgaba: no hay dictamen anterior del que apartarse. Que un
                # escenario cite una evidencia que no lo nombra lo juzga el contraste de
                # esta misma prueba, que lo cuenta como NO CONTRASTABLE con su estado.
                continue
            # `H-08` bis · QUÉ ES «CAMBIAR DE DICTAMEN», MEDIDO EN VEZ DE SUPUESTO
            #
            #     HECHO REPRODUCIDO EN ESTA MISMA PASADA. La comparación era
            #     `sorted(antes) != sorted(despues)`, es decir el MULTICONJUNTO de
            #     veredictos. Al añadir a la batería de integridad un caso nuevo que PASA
            #     —`T307g`, el control de `H-08`—, la evidencia regenerada pasó de seis
            #     `ok` a siete para `T307`, y esta comprobación dio ROJO:
            #
            #         integridad-evidencia-salida.txt: para `T307` la versión confirmada en
            #         `HEAD` publica ['ok'×6] y la del árbol de trabajo publica ['ok'×7].
            #         La evidencia ha cambiado de DICTAMEN sin una ejecución que lo respalde
            #
            #     Es un ROJO FALSO, y del peor tipo: castiga REFORZAR una batería. El
            #     comentario de arriba ya dice qué se quiere medir —«una regeneración
            #     legítima cambia cifras y no cambia dictámenes»—; el código medía cifras.
            #
            #     DECISIÓN · se compara el DICTAMEN y se pone un CLIQUET a la cobertura
            #         Tres condiciones, y cada una tapa una vía distinta:
            #           1 · el CONJUNTO de veredictos distintos tiene que ser el mismo. Un
            #               `ok` que se vuelve `FAIL` lo cambia; añadir otro `ok`, no.
            #           2 · el número de veredictos MALOS no puede cambiar. Esconder un
            #               fallo entre casos nuevos no cuela.
            #           3 · el número de veredictos BUENOS no puede BAJAR. Añadir casos es
            #               legítimo; que la evidencia adelgace en silencio, no. Es un
            #               cliquet, no una igualdad, y por eso admite lo primero y no lo
            #               segundo.
            #         Alternativa descartada: comparar sólo el conjunto. Habría dejado pasar
            #         que una batería encogiera de seis casos a uno sin decir nada.
            buenos_antes = [v for v in antes if registro_pruebas.veredicto_es_bueno(v)]
            buenos_despues = [v for v in despues if registro_pruebas.veredicto_es_bueno(v)]
            malos_antes = [v for v in antes if not registro_pruebas.veredicto_es_bueno(v)]
            malos_despues = [v for v in despues
                             if not registro_pruebas.veredicto_es_bueno(v)]
            if set(antes) != set(despues) or len(malos_antes) != len(malos_despues):
                r.fallo(f"{rel}: para `{identificador}` la versión confirmada en `HEAD` "
                        f"publica {sorted(antes)} y la del árbol de trabajo publica "
                        f"{sorted(despues)}. La evidencia ha cambiado de DICTAMEN sin una "
                        f"ejecución que lo respalde")
            elif len(buenos_despues) < len(buenos_antes):
                r.fallo(f"{rel}: para `{identificador}` la evidencia ha ENCOGIDO: `HEAD` "
                        f"publica {len(buenos_antes)} veredictos buenos y el árbol de "
                        f"trabajo {len(buenos_despues)}. Añadir casos es legítimo; que la "
                        f"cobertura adelgace sin decirlo, no")
    partes = [f"evidencia contrastada contra el blob de HEAD: {hechas}"]
    if borradas:
        partes.append(f"confirmadas en HEAD y AUSENTES del árbol de trabajo: "
                      f"{len(borradas)} ({', '.join(os.path.basename(x) for x in borradas)})")
    if regeneradas:
        partes.append(f"difieren de HEAD sin cambiar ningún dictamen (regeneración en "
                      f"curso): {len(regeneradas)}")
    if sin_confirmar:
        partes.append(f"citadas y todavía NO confirmadas en HEAD: {len(sin_confirmar)} "
                      f"({', '.join(os.path.basename(x) for x in sin_confirmar)})")
    partes.append("que el contenido de la zona EVIDENCIA no mute sin declararlo lo juzga "
                  "`V6-10` en el verificador de admisión, no esta prueba")
    return " · ".join(partes)


PRUEBAS = [t158_evidencia, t350_estado_derivado_de_la_evidencia]


def main():
    # `11-ARQ` §19, CONTRATO 3 · EL MISMO PRÓLOGO. Este validador recalcula la VIGENCIA
    # llamando a `comprobar_fuentes`, que lee `SOURCES.toml` con `tomllib`: la dependencia
    # es transitiva, y una dependencia transitiva no deja de serlo por no verse en el
    # `import`. Bajo Python 3.10 se medía esto: `python3 comprobar_evidencia.py` salía
    # `T158 SUPERADA` con CÓDIGO 0 sobre una evidencia que en ese entorno NADIE puede
    # regenerar. Es literalmente lo que la prueba negativa del contrato prohíbe: «`T158`
    # NO puede salir SUPERADA sobre evidencia que no se ha regenerado en esta corrida».
    entorno.exigir()
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None)
    args = ap.parse_args()
    resultados = [f(args.raiz) for f in PRUEBAS]
    if args.json:
        print(json.dumps([{"id": x.id, "nombre": x.nombre,
                           "estado": "prueba-superada" if x.superada else "prueba-fallida",
                           "fallos": x.fallos,
                           "cobertura_del_contraste": getattr(x, "nota_cobertura", None)}
                          for x in resultados], ensure_ascii=False, indent=2))
    else:
        for x in resultados:
            print(f"{x.id}  {'SUPERADA' if x.superada else 'FALLIDA '}  {x.nombre}")
            for f in x.fallos:
                print(f"          · {f}")
            # `H-08` · la cobertura del contraste, PUBLICADA. Se imprime pase o falle: una
            # cifra que sólo sale cuando todo va bien no sirve para ver cuándo empeora.
            if getattr(x, "nota_cobertura", None):
                print(f"          cobertura del contraste: {x.nota_cobertura}")
        fallidas = [x for x in resultados if not x.superada]
        print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if any(not x.superada for x in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
