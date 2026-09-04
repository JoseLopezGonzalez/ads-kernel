#!/usr/bin/env python3
"""anfitrion_verificador — la mitad PÚBLICA de la frontera de firma. `O25` §3 y §4.

    anfitrion_verificador.py --firmantes <fichero> verificar <identidad> <firma-hex>
        < mensaje    >  `valida` | `invalida`

**No tiene clave privada, y no puede tenerla**: lo único que lee es el fichero de FIRMANTES
AUTORIZADOS, que contiene claves PÚBLICAS. Ésa es la asimetría que `V6-16` necesita y que un
HMAC no puede dar: quien verifica NO puede firmar.

DECISIÓN · el fichero de firmantes llega por ARGUMENTO de la configuración externa, no por
           variable de entorno ni por convención
    `O25` §3: «la configuración externa de confianza establece la identidad o huella pública
    aceptada» y «el repositorio verificado no puede cambiar por sí mismo qué identidad acepta
    la raíz externa». Una ruta por convención la puede plantar el árbol; una ruta que viaja en
    el campo `orden_de_verificacion` de la configuración externa, no.

DECISIÓN · la respuesta es `valida` o `invalida`, y nunca un tercer valor
    Es el protocolo que `identidad/proveedor.py` ya define y consume. Cualquier otra salida
    —incluida la vacía— la lee ese módulo como NO válida, que es el sentido correcto del
    fallo por omisión.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `ADJ-B2` · LA PURGA `E-10`, EN LA RAÍZ EXTERNA
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, sobre este mismo paquete. Con un `json.py` HOMÓNIMO
#  en `PYTHONPATH` y desde un `cwd` ajeno:
#
#      verificador.py capacidades            → {}   EXIT=0   (sano: las nueve condiciones)
#      instalar.py --destino … --arbol …     → {}   EXIT=0   manifiesto 3 BYTES (sano: 6734)
#                                                            y 41 ficheros instalados igual
#      … --comprobar sobre esa instalación   → KeyError: 'ficheros'  EXIT=1, cuatro rutas
#                                                            absolutas del anfitrión
#      grep de purga sobre TODO `raiz-externa/`                      CERO líneas
#
#  Es el MISMO defecto que el árbol declaraba cerrado para los cinco `ads_*.py`, vivo en la
#  única pieza que `O26` §1 juzga, e incumpliendo su condición 8 —«contaminación del entorno
#  falla cerrado»—, la única de las ocho que no se cumplía.
#
#  DECISIÓN · el prólogo se COPIA byte a byte, no se importa y no se adapta
#      Alternativas: (a) un módulo `procedencia.py` del paquete que los cuatro importen;
#      (b) una variante «para la raíz externa» del prólogo; (c) el MISMO prólogo, copiado.
#      Se elige (c), por dos razones y las dos se comprueban. (a) es la alternativa que el
#      propio `E-10` ya descartó: una guardia que necesita importar para poder purgar ya ha
#      perdido, porque el `import` es exactamente lo que está protegiendo. (b) produce dos
#      textos que divergen, y la divergencia se descubre el día que uno de los dos se queda
#      corto. Con (c) los NUEVE puntos ejecutables del árbol llevan el mismo texto y una
#      prueba lo comprueba por digest: si alguien toca uno, tiene que tocarlos todos.

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, sobre este mismo punto ejecutable: con
#  `PYTHONPATH=<dir>` apuntando a un directorio que contiene un `json.py` HOMÓNIMO, el
#  proceso IMPORTABA el homónimo. `sys.path[0]` —el directorio del script— protege a
#  `admision`, `estado` y `runtime`, que viven al lado; NO protege a la biblioteca estándar,
#  que va DESPUÉS de `PYTHONPATH`. Medido: `ads_admision.py --repo <dir> verificar --json`
#  publicaba `{}` como veredicto y terminaba con código 0, y los cinco `ads_*.py` importaban
#  el módulo envenenado.
#
#  DECISIÓN · la purga es lo PRIMERO del fichero y sólo usa `sys` y `os`
#      Alternativas: (a) purgar después de los imports normales; (b) purgar en un módulo
#      aparte e importarlo; (c) purgar aquí, con lo único que el intérprete ya ha cargado.
#      Se elige (c). Con (a) la purga llega tarde: el homónimo ya está en `sys.modules`. Con
#      (b) la purga depende de un `import` que es exactamente lo que se está protegiendo —una
#      guardia que necesita importar ya ha perdido—. `sys` es un módulo incorporado y `os` lo
#      carga el arranque del intérprete, así que los dos vienen de `sys.modules` y no de la
#      ruta de importación. Que `os` sea el bueno se COMPRUEBA, no se supone.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación
#      distinta y convertiría un fallo de entorno en un fallo del aparato. Lo que `E-10`
#      nombra es concreto: `PYTHONPATH` y el `cwd`. Se retiran ésos, se cuenta cuántos, y el
#      recuento se PUBLICA en la procedencia.
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
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import firma as modulo_de_firma                                      # noqa: E402
from errores import ErrorDeRaizExterna                               # noqa: E402


# ---------------------------------------------------------------------------
#  `E-10` · la PROCEDENCIA, también en la frontera con el anfitrión
# ---------------------------------------------------------------------------
#  Este programa lo lanza `identidad/proveedor.py` con un entorno construido de cero, pero
#  también lo puede lanzar una persona desde su terminal, y ahí el `PYTHONPATH` es el que
#  sea. Un `firma` homónimo en la ruta de importación decidiría qué se firma o qué se
#  acepta como firmado, que es el poder entero de esta frontera. La purga de arriba impide
#  que entre; esto comprueba que no entró, y sin poder comprobarlo NO se ejecuta.
MODULOS_DEL_APARATO = ("firma", "errores")

CODIGO_DE_PROCEDENCIA = 5


def _origen_de(fichero):
    """Nunca una ruta absoluta del anfitrión: ni en la salida ni en el diagnóstico."""
    if not fichero:
        return "(sin fichero)"
    real = os.path.realpath(fichero)
    propia = os.path.realpath(_RAIZ_DEL_APARATO)
    if real == propia or real.startswith(propia + os.sep):
        return "aparato:" + os.path.relpath(real, propia)
    return "FUERA-DEL-APARATO:" + os.path.basename(real)


def exigir_procedencia_del_aparato():
    """FALLO CERRADO si un módulo del aparato no sale del aparato. `E-10`, `O25`."""
    intrusos = []
    for nombre in MODULOS_DEL_APARATO:
        modulo = sys.modules.get(nombre)
        origen = _origen_de(getattr(modulo, "__file__", None))
        if origen.startswith("FUERA-DEL-APARATO") or origen == "(sin fichero)":
            intrusos.append(nombre)
    if intrusos:
        sys.stderr.write(
            "[PROCEDENCIA_NO_FIABLE] modulos de la raiz externa importados desde fuera del "
            "paquete: " + ", ".join(sorted(intrusos)) + ". NO se ejecuta\n")
        return CODIGO_DE_PROCEDENCIA
    return None


def main(argv=None):
    intruso = exigir_procedencia_del_aparato()
    if intruso is not None:
        return intruso
    argumentos = list(sys.argv[1:] if argv is None else argv)
    firmantes = None
    while argumentos and argumentos[0] == "--firmantes":
        if len(argumentos) < 2:
            sys.stderr.write("uso: --firmantes <fichero>\n")
            return 2
        firmantes = argumentos[1]
        argumentos = argumentos[2:]
    if len(argumentos) < 3 or argumentos[0] != "verificar":
        sys.stderr.write(
            "uso: anfitrion_verificador.py --firmantes <fichero> verificar <identidad> "
            "<firma-hex>\n"
        )
        return 2
    identidad = argumentos[1]
    try:
        blindada = bytes.fromhex(argumentos[2])
    except ValueError:
        sys.stdout.write("invalida")
        return 0
    if not firmantes or not os.path.isfile(firmantes):
        sys.stderr.write(
            "no esta el fichero de firmantes autorizados que la configuracion externa "
            "declara: sin el no se acepta ninguna identidad\n"
        )
        return 3
    mensaje = sys.stdin.buffer.read()
    try:
        valida, _ = modulo_de_firma.verificar(
            mensaje, blindada, firmantes=firmantes, principal=identidad)
    except ErrorDeRaizExterna as error:
        sys.stderr.write(str(error) + "\n")
        return 3
    sys.stdout.write("valida" if valida else "invalida")
    return 0


if __name__ == "__main__":
    sys.exit(main())
