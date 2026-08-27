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


def cargar_manifiesto(base):
    ruta = os.path.join(base, "kernel/operativo/validadores/validadores.yaml")
    with open(ruta, encoding="utf-8") as fh:
        return (yaml.safe_load(fh) or {}).get("componentes") or []


def t158_evidencia(raiz=None):
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T158", "La evidencia publicada demuestra lo que el informe afirma")
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


def _vigencia(base, componentes, r):
    for comp in componentes:
        if comp.get("tipo") != "validador":
            continue
        entradas = comp.get("vigencia") or []
        if not entradas:
            continue

        # Sin circularidad: quien está exento de su propia comprobación no puede además
        # declarar vigencia, porque T158 estaría comprobando su propia evidencia contra sí
        # mismo y aceptándose.
        if comp.get("se_excluye_de_su_propia_comprobacion"):
            r.fallo(f"manifiesto: '{comp['id']}' declara `vigencia` y está exento de su "
                    f"propia comprobación. Comprobaría su evidencia contra sí mismo")
            continue

        rel = os.path.join(DIR_EVIDENCIA, comp["evidencia"])
        ruta = os.path.join(base, rel)
        if not os.path.isfile(ruta):
            continue                       # su ausencia ya se ha reportado más arriba
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()

        for e in entradas:
            eid = e.get("id") or "(sin id)"
            if not e.get("motivo"):
                r.fallo(f"manifiesto: la vigencia '{eid}' de '{comp['id']}' no escribe su "
                        f"motivo. Una comprobación sin motivo no se puede revisar")
            calcular = RECUENTOS_DE_VIGENCIA.get(e.get("recuento"))
            if calcular is None:
                r.fallo(f"manifiesto: la vigencia '{eid}' de '{comp['id']}' declara el "
                        f"recuento '{e.get('recuento')}', que no está registrado en "
                        f"RECUENTOS_DE_VIGENCIA. Sin implementación no se comprueba nada, "
                        f"y una comprobación que no existe no puede darse por superada")
                continue
            m = re.search(e["patron"], texto)
            if not m:
                r.fallo(f"{rel}: la vigencia '{eid}' no encuentra su cifra (/{e['patron']}/). "
                        f"La evidencia dejó de publicar el valor que se comprueba")
                continue
            publicado = int(m.group(1))
            actual = calcular(base)
            if publicado != actual:
                r.fallo(f"{rel}: la vigencia '{eid}' publica {publicado} y el corpus vigente "
                        f"da {actual}. La evidencia está CADUCADA: describe un corpus que ya "
                        f"no existe. Regenérala con registrar_evidencia.py — no la edites")


PRUEBAS = [t158_evidencia]


def main():
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
