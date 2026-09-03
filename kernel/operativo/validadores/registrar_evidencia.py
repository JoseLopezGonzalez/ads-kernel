#!/usr/bin/env python3
"""registrar_evidencia — ejecuta los validadores y publica su evidencia, con seguridad.

POR QUÉ EXISTE. La evidencia de la entrega anterior se archivó con un bucle de shell que
construía el nombre del script SIN la extensión `.py`, redirigía el error del intérprete
DENTRO del fichero con `2>&1`, y publicaba sin mirar el código de salida. Ocho de diez
ficheros quedaron con «python3: can't open file», sobrescribiendo evidencia que era válida,
mientras el informe seguía afirmando «todos EXIT 0». El defecto no fue el fallo: fue que
publicar y comprobar eran el mismo gesto, y ninguno de los dos comprobaba nada.

CÓMO EVITA QUE VUELVA A OCURRIR:

  1. la lista de validadores se DESCUBRE del manifiesto canónico `validadores.yaml`,
     no se escribe en el comando
  2. cada script se invoca por su ruta completa TERMINADA EN `.py`, y se verifica que el
     fichero existe ANTES de intentar ejecutarlo
  3. stdout, stderr y código de salida se capturan POR SEPARADO — nunca se mezclan
  4. se escribe primero en un temporal, y se publica con `os.replace`, que es atómico
  5. una ejecución con código distinto de cero NO se publica: la evidencia anterior
     sobrevive intacta
  6. el proceso termina con código distinto de cero si cualquier validación falla

Uso:
  python3 kernel/operativo/validadores/registrar_evidencia.py [--raiz DIR] [--json]
                                                             [--sin-generadores]
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import entorno  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DIR_VALIDADORES = "kernel/operativo/validadores"
DIR_EVIDENCIA = "kernel/operativo/pruebas/evidencia"


def _sin_rutas_del_anfitrion(texto, base):
    """La ruta ABSOLUTA del checkout se sustituye por `<raiz>` antes de publicar.

    POR QUÉ. La evidencia se PUBLICA y se versiona, y su promesa es que dos ejecuciones de
    lo mismo dan lo mismo. No la cumplía: tres ficheros —`adaptadores`, `contencion` y
    `multimaquina`— empotraban la ruta absoluta del anfitrión, porque un `ResourceWarning`
    de Python cita el fichero por su ruta completa. Reproducir la suite en OTRO checkout
    daba un `diff` que no señalaba ningún cambio de comportamiento: sólo decía dónde estaba
    el árbol. Una auditoría independiente lo midió y lo llamó por su nombre —dependencia de
    anfitrión no declarada—, porque el determinismo que se afirmaba era «en esta máquina y
    en esta ruta», no el que la evidencia promete.

    Se normaliza AQUÍ, en el único punto por el que pasa toda la evidencia, y no en cada
    instrumento: un instrumento que lo olvidara volvería a publicar la ruta sin que nada lo
    dijera. Lo que se sustituye es EXACTAMENTE la raíz del checkout, de la más larga a la
    más corta, de modo que nada del contenido real se pierde ni se enmascara.
    """
    for ruta in sorted({os.path.abspath(base), os.path.realpath(base)}, key=len, reverse=True):
        texto = texto.replace(ruta, "<raiz>")
    return texto


class Ejecucion:
    def __init__(self, comp):
        self.id = comp["id"]
        self.script = comp["script"]
        # `dir` permite registrar un ejecutable que NO vive en validadores/ —las pruebas
        # de workspace viven en tooling/tests/ porque prueban tooling, no el corpus— sin
        # que quede fuera de la evidencia por estar en otro sitio.
        self.dir = comp.get("dir") or DIR_VALIDADORES
        self.args = comp.get("args") or []
        self.tipo = comp["tipo"]
        self.evidencia = comp.get("evidencia")
        self.codigo = None
        self.publicada = False
        self.motivo = ""

    @property
    def orden(self):
        return " ".join([f"{self.dir}/{self.script}"] + self.args)


def cargar_manifiesto(base):
    ruta = os.path.join(base, DIR_VALIDADORES, "validadores.yaml")
    with open(ruta, encoding="utf-8") as fh:
        return (yaml.safe_load(fh) or {}).get("componentes") or []


def comprobar_manifiesto(base, componentes, problemas):
    """Todo `.py` del directorio está en el manifiesto, y todo lo del manifiesto existe.

    Sin esto, añadir un validador nuevo y olvidarse de registrarlo lo dejaría fuera de la
    evidencia sin que nada lo dijera — que es la forma silenciosa del mismo defecto.
    """
    declarados = set()
    for comp in componentes:
        script = comp.get("script", "")
        if not script.endswith(".py"):
            problemas.append(f"manifiesto: '{comp.get('id')}' declara el script '{script}', "
                             f"que no termina en .py")
            continue
        directorio = comp.get("dir") or DIR_VALIDADORES
        if directorio == DIR_VALIDADORES:
            declarados.add(script)
        if not os.path.isfile(os.path.join(base, directorio, script)):
            problemas.append(f"manifiesto: '{comp['id']}' declara {directorio}/{script}, "
                             f"que no existe")
    en_disco = {f for f in os.listdir(os.path.join(base, DIR_VALIDADORES))
                if f.endswith(".py")}
    for f in sorted(en_disco - declarados):
        problemas.append(f"{f} existe en validadores/ y el manifiesto no lo declara: "
                         f"quedaría fuera de la evidencia sin que nada lo dijera")


def ejecutar(base, ej, publicar=True):
    script = os.path.join(base, ej.dir, ej.script)
    if not os.path.isfile(script):
        ej.codigo = -1
        ej.motivo = f"el script no existe: {script}"
        return
    proc = subprocess.run([sys.executable, script, *ej.args],
                          cwd=base, capture_output=True, text=True)
    ej.codigo = proc.returncode
    if ej.codigo != 0:
        ej.motivo = (f"terminó con código {ej.codigo}; la evidencia anterior NO se ha "
                     f"tocado. stderr: {proc.stderr.strip()[:200] or '(vacío)'}")
        return
    if not publicar or not ej.evidencia:
        ej.motivo = "ejecutado" if not ej.evidencia else "no se pidió publicar"
        return

    # La evidencia lleva SU PROPIA cabecera: qué se ejecutó y con qué código. Sin ella,
    # un fichero de salida no dice de quién es ni si tuvo éxito.
    cabecera = (f"# evidencia de: {ej.id}\n"
                f"# orden:        python3 {ej.orden}\n"
                f"# codigo:       {ej.codigo}\n"
                f"# ---------------------------------------------------------------\n")
    cuerpo = proc.stdout
    if proc.stderr.strip():
        # stderr se conserva IDENTIFICADO, nunca mezclado con la salida.
        cuerpo += f"\n# --- stderr (código {ej.codigo}) ---\n{proc.stderr}"
    cuerpo = _sin_rutas_del_anfitrion(cuerpo, base)

    destino = os.path.join(base, DIR_EVIDENCIA, ej.evidencia)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(destino), prefix=".ev-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(cabecera + cuerpo)
        os.replace(tmp, destino)          # atómico: no hay estado intermedio publicado
        ej.publicada = True
        ej.motivo = "publicada"
    except Exception:                                          # noqa: BLE001
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--sin-generadores", action="store_true")
    args = ap.parse_args()

    # LA GUARDA, ANTES DE CORRER NADA (A14). El defecto que cierra es concreto y ya ocurrió:
    # bajo un intérprete insuficiente algunos validadores fallan por el ENTORNO, este runner
    # —correctamente— no republica su evidencia, y la cobertura publicada queda describiendo
    # un corpus anterior mientras el comprobador de evidencia sigue en verde. Publicar a
    # medias es peor que no publicar: aquí no se empieza.
    entorno.exigir()

    base = os.path.abspath(args.raiz or RAIZ)

    problemas = []
    componentes = cargar_manifiesto(base)
    comprobar_manifiesto(base, componentes, problemas)

    # Los generadores van primero: la evidencia de los validadores tiene que reflejar el
    # estado YA regenerado, no el anterior.
    generadores = [Ejecucion(c) for c in componentes if c["tipo"] == "generador"]
    validadores = [Ejecucion(c) for c in componentes if c["tipo"] == "validador"]

    if not args.sin_generadores:
        for ej in generadores:
            ejecutar(base, ej, publicar=False)
            if ej.codigo != 0:
                problemas.append(f"generador {ej.id}: {ej.motivo}")

    for ej in validadores:
        ejecutar(base, ej)
        if ej.codigo != 0:
            problemas.append(f"validador {ej.id}: {ej.motivo}")

    todas = generadores + validadores
    if args.json:
        print(json.dumps({
            "problemas": problemas,
            "ejecuciones": [{"id": e.id, "orden": e.orden, "tipo": e.tipo,
                             "codigo": e.codigo, "publicada": e.publicada,
                             "motivo": e.motivo} for e in todas]},
            ensure_ascii=False, indent=2))
    else:
        print("EJECUCIÓN Y PUBLICACIÓN DE EVIDENCIA\n")
        for e in todas:
            marca = "OK " if e.codigo == 0 else "FALLO"
            pub = "publicada" if e.publicada else ("—" if e.tipo == "generador" else "NO publicada")
            print(f"{marca}  {e.id:22} código {str(e.codigo):>3}  {pub:14} {e.orden}")
            if e.codigo != 0:
                print(f"       └─ {e.motivo}")
        if problemas:
            print("\nPROBLEMAS")
            for p in problemas:
                print(f"  · {p}")
        n_ok = sum(1 for e in validadores if e.codigo == 0)
        print(f"\n{n_ok}/{len(validadores)} validadores en verde · "
              f"{sum(1 for e in todas if e.publicada)} evidencias publicadas · "
              f"{len(problemas)} problemas")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
