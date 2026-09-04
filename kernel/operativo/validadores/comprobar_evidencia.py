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
    r.nota_cobertura = (f"contrastados {len(contrastados)} · no contrastables "
                        f"{len(sin_contraste)} · divergencias {len(divergencias)}")
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
    hechas, sin_confirmar, regeneradas = 0, [], []
    for nombre in sorted(por_evidencia):
        rel = os.path.join(DIR_EVIDENCIA, nombre)
        ruta = os.path.join(base, rel)
        if not os.path.isfile(ruta):
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
            if antes and despues and sorted(antes) != sorted(despues):
                r.fallo(f"{rel}: para `{identificador}` la versión confirmada en `HEAD` "
                        f"publica {sorted(antes)} y la del árbol de trabajo publica "
                        f"{sorted(despues)}. La evidencia ha cambiado de DICTAMEN sin una "
                        f"ejecución que lo respalde")
    partes = [f"evidencia contrastada contra el blob de HEAD: {hechas}"]
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
                           "fallos": x.fallos} for x in resultados], ensure_ascii=False, indent=2))
    else:
        for x in resultados:
            print(f"{x.id}  {'SUPERADA' if x.superada else 'FALLIDA '}  {x.nombre}")
            for f in x.fallos:
                print(f"          · {f}")
        fallidas = [x for x in resultados if not x.superada]
        print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if any(not x.superada for x in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
