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
import subprocess
import sys
import tempfile

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import entorno  # noqa: E402
# El mismo módulo que la guarda de arriba, con el nombre con el que se usa abajo. Se pide de
# aquí —y no se reescriben las banderas ni la lista de variables— para que el runner y la
# guarda pidan LO MISMO: dos listas separadas derivan, y la que miente es la que nadie mira.
import aislamiento_de_arranque as aisl  # noqa: E402

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
        # `D-01` · con qué aislamiento se lanzó el hijo. Se rellena al ejecutar y se PUBLICA
        # en la cabecera: una garantía que no se publica no la puede comprobar nadie.
        self.aislamiento = ""

    @property
    def orden(self):
        """La orden PUBLICABLE: la misma que se ejecuta, con la ruta relativa al árbol.

        Las banderas no se escriben aquí: se derivan de la orden real que
        `aislamiento_de_arranque` construye, para que la cabecera no pueda decir una cosa y
        el proceso hacer otra —que es la clase entera de `HALLAZGO 3`—.
        """
        real = aisl.orden_aislada(f"{self.dir}/{self.script}", self.args)
        return " ".join(aisl.banderas_de(real) + [f"{self.dir}/{self.script}"] + self.args)


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
    # `D-01` · EL RUNNER SANEA EL ENTORNO DE SUS HIJOS, Y LO PUBLICA
    #
    #  HECHO REPRODUCIDO ANTES DE CORREGIR — `HALLAZGO 3` del revisor 3, gate del
    #  2026-09-05. Esta línea era:
    #
    #      proc = subprocess.run([sys.executable, script, *ej.args],
    #                            cwd=base, capture_output=True, text=True)
    #
    #  SIN `env=`, de modo que `subprocess` copia el entorno del padre entero y el veneno
    #  del lanzador —`PYTHONPATH`, y con él `sitecustomize`— llegaba intacto a CADA una de
    #  las veintiuna baterías que este runner ejecuta. Este es el canal que PRODUCE la
    #  evidencia: contaminarlo es contaminar todo lo que la evidencia afirma.
    #
    #  DECISIÓN · se hacen las DOS cosas que el revisor adjudicó, y no una
    #      Alternativas: (a) meter el prólogo en las 21 baterías; (b) sanear aquí el entorno
    #      de los hijos y publicarlo; (c) las dos.
    #      Se elige (c). El revisor lo escribió así: «lo segundo cierra las 21 de una vez y
    #      es más barato; lo primero cierra también la ejecución suelta». Una batería se
    #      ejecuta a mano mientras se escribe, y ésa no pasa por aquí; y un runner limpio que
    #      lanzara una batería sin guarda dependería de que nadie la invocara de otro modo.
    #      Con las dos, ni el canal ni la pieza dependen de quien las llama.
    #
    #  DECISIÓN · el hijo se lanza AISLADO, y no sólo con el entorno limpio
    #      Un `env=` sin `PYTHONPATH` no impide que `site.py` importe un `sitecustomize`
    #      INSTALADO en `site-packages`. Las banderas `-I -S -E` sí, y son las mismas que
    #      `aislamiento_de_arranque` exige: se piden desde ahí para que no haya dos listas.
    orden = aisl.orden_aislada(script, ej.args)
    entorno = aisl.entorno_saneado()
    ej.aislamiento = aisl.linea_de_aislamiento_del_hijo(orden, entorno)
    proc = subprocess.run(orden, cwd=base, capture_output=True, text=True, env=entorno)
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
    #  Y la GARANTÍA se publica: la línea `aislamiento` dice con qué banderas y con qué
    #  entorno se lanzó el hijo que produjo esta salida. Sin ella, quien lee la evidencia no
    #  puede distinguir una corrida saneada de una heredada, que es la diferencia que
    #  `HALLAZGO 3` midió. `comprobar_evidencia.py` la exige y la comprueba.
    cabecera = (f"# evidencia de: {ej.id}\n"
                f"# orden:        python3 {ej.orden}\n"
                f"# aislamiento:  {ej.aislamiento}\n"
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
