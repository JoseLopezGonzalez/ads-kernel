#!/usr/bin/env python3
"""Una instancia puede declarar sus propias zonas no analizadas. Comprobado.

    python3 kernel/operativo/validadores/pruebas/prueba_exclusiones_de_instancia.py

QUE SE ARREGLO Y POR QUE
------------------------
`exclusiones.yaml` vive dentro de `kernel/`, y `kernel/` entra en la huella que decide
si una instalacion es un FORK. Una instancia que ganaba legitimamente una zona propia
no tenia donde declararla: tocar el fichero del kernel la volvia divergente y ponia en
rojo su propia comprobacion de integridad —justo la alarma que esa huella existe para
dar—. Las dos salidas eran malas, y ninguna era la correcta.

Y ganar una zona propia es el caso NORMAL, no el raro. Un ADS gobierna unas fuentes y
acaba archivando material de esas fuentes: documentos que llegan con enlaces relativos
a SU arbol de origen, apuntando a hermanos que no vinieron. No son corpus —son
evidencia, y la evidencia describe—, pero el validador los leia como corpus y denunciaba
cada enlace. Una instancia real llego asi a 442 errores en material archivado, con su CI
muriendo en el primer paso y sin llegar a ejecutar nada mas.

LO QUE ESTO TIENE QUE SEGUIR IMPIDIENDO
---------------------------------------
Que la sede de instancia sea una puerta trasera. Por eso las cinco comprobaciones no
son «funciona»: tres de ellas exigen que el mecanismo se NIEGUE. Una exclusion sin
motivo es indistinguible de un descuido, y una exclusion huerfana tapa la zona que
ocupe manana ese nombre.
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
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
LINT = os.path.join(RAIZ, "kernel", "operativo", "validadores", "ads_lint.py")

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass


def monta(exclusiones: str | None) -> str:
    """Un arbol minimo con UN documento archivado que enlaza a algo que no vino."""
    raiz = tempfile.mkdtemp(prefix="prueba-exclusiones-")
    # El validador exige los esquemas canonicos para arrancar. Se enlaza `kernel/` del
    # repositorio real en lugar de copiarlo: `os.walk` no sigue enlaces simbolicos por
    # defecto, asi que el laboratorio ve los esquemas —que se abren por ruta— y NO se
    # pone a recorrer el kernel entero buscando enlaces. Lo que se mide aqui es la zona
    # heredada, no el corpus del kernel.
    os.symlink(os.path.join(RAIZ, "kernel"), os.path.join(raiz, "kernel"))
    os.makedirs(os.path.join(raiz, "zona-archivada"))
    with open(os.path.join(raiz, "zona-archivada", "heredado.md"), "w",
              encoding="utf-8") as fh:
        fh.write("# Documento heredado\n\n"
                 "Llego de otro repositorio y enlaza a un hermano que no vino:\n\n"
                 "[el hermano](./no-vino-con-el.md)\n")
    if exclusiones is not None:
        os.makedirs(os.path.join(raiz, "docs", "canonico"))
        with open(os.path.join(raiz, "docs", "canonico",
                               "exclusiones-de-instancia.yaml"), "w",
                  encoding="utf-8") as fh:
            fh.write(exclusiones)
    return raiz


def corre(raiz: str) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, LINT, "--raiz", raiz],
                          capture_output=True, text=True,
                          env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    return proc.returncode, proc.stdout + proc.stderr


FALLOS: list[str] = []
TOTAL = 5


def comprueba(titulo: str, condicion: bool, detalle: str = "") -> None:
    """Publica el veredicto NOMINAL del escenario, en la forma que el registro lee.

    La linea empieza en la columna cero y es `T4xx  SUPERADA|FALLIDA  <titulo>`, que es
    justo lo que `registro_pruebas.derivar_estado` sabe leer. No es decoracion: sin una
    linea de veredicto por escenario, la evidencia sostiene «se ejecuto» y NO «salio bien»,
    y un escenario que declarase `prueba-superada` estaria subiendo de estado por argumento
    —que es la regla dura que el registro existe para hacer cumplir—.
    """
    veredicto = "SUPERADA" if condicion else "FALLIDA"
    ident, _, resto = titulo.partition(" · ")
    print(f"{ident}  {veredicto}  {resto or titulo}")
    if not condicion:
        if detalle:
            print("          " + detalle.replace("\n", "\n          ")[:700])
        FALLOS.append(titulo)


def main() -> int:
    print("ZONAS NO ANALIZADAS DECLARADAS POR LA INSTANCIA")
    print("=" * 74)

    # 1 · SIN declaracion, el enlace roto se denuncia. Es la linea base: si esto no
    #     saliera en rojo, las otras tres no demostrarian nada.
    codigo, salida = corre(monta(None))
    comprueba("T430 · sin sede de instancia, el enlace heredado sale en ROJO",
              codigo != 0 and "enlace-roto" in salida, salida)

    # 2 · CON declaracion, la zona se salta Y SE PUBLICA. Lo segundo importa tanto
    #     como lo primero: una zona excluida que no se ve en cada ejecucion deja de
    #     ser una decision y pasa a ser una costumbre.
    codigo, salida = corre(monta(
        "no_analizados:\n"
        "  - ruta: zona-archivada\n"
        "    motivo: material heredado de una fuente; es evidencia, no corpus\n"))
    comprueba("T431 · con la zona declarada, sale en VERDE", codigo == 0, salida)
    comprueba("T432 · ...y la ejecucion PUBLICA la zona excluida",
              "zona-archivada" in salida and "NO analizadas" in salida, salida)

    # 3 · Sin motivo, se NIEGA. Una exclusion sin motivo no se distingue de un descuido.
    codigo, salida = corre(monta(
        "no_analizados:\n"
        "  - ruta: zona-archivada\n"))
    comprueba("T433 · una exclusion SIN MOTIVO se rechaza",
              codigo != 0 and "motivo" in salida, salida)

    # 4 · Huerfana, se NIEGA. Si no se exigiera, la lista acumularia restos y taparia
    #     en silencio la zona que ocupe manana ese nombre.
    codigo, salida = corre(monta(
        "no_analizados:\n"
        "  - ruta: zona-que-ya-no-existe\n"
        "    motivo: se quedo aqui de una limpieza anterior\n"))
    comprueba("T434 · una exclusion HUERFANA se rechaza",
              codigo != 0 and "ya no existe" in salida, salida)

    print("=" * 74)
    for f in FALLOS:
        print(f"  falla: {f}")
    # EL CIERRE ES EL DEL CONVENIO, NO UNA FRASE PROPIA. `registro_pruebas.derivar_estado`
    # solo reconoce tres formas de decir «esto termino», y una salida que cierra con una
    # frase inventada se lee como TRUNCADA: la evidencia sostendria `prueba-ejecutada` y
    # el escenario que declarase `prueba-superada` estaria subiendo de estado por argumento.
    print(f"{TOTAL - len(FALLOS)} superadas · {len(FALLOS)} fallidas")
    return 1 if FALLOS else 0


if __name__ == "__main__":
    sys.exit(main())
