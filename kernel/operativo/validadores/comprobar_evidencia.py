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
    declarados = {c.get("script") for c in componentes}
    for f in sorted(os.listdir(dir_val)):
        if f.endswith(".py") and f not in declarados:
            r.fallo(f"validadores/{f}: existe y el manifiesto no lo declara. Quedaría "
                    f"fuera de la evidencia sin que nada lo dijera")
    for c in componentes:
        script = c.get("script", "")
        if not script.endswith(".py"):
            r.fallo(f"manifiesto: '{c.get('id')}' declara '{script}', que no termina en .py")
        elif not os.path.isfile(os.path.join(dir_val, script)):
            r.fallo(f"manifiesto: '{c.get('id')}' declara {script}, que no existe")

    # 9 · nada sobra en el directorio: una evidencia huérfana es una que nadie regenera
    dir_ev = os.path.join(base, DIR_EVIDENCIA)
    if os.path.isdir(dir_ev):
        for f in sorted(os.listdir(dir_ev)):
            if f.endswith(".txt") and f not in esperados:
                r.fallo(f"{DIR_EVIDENCIA}/{f}: no lo declara ningún validador del "
                        f"manifiesto. Nadie lo regenera y nadie responde de él")
    return r


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
