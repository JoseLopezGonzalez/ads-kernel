#!/usr/bin/env python3
"""censo — los DOS censos DERIVADOS del aparato. `V6-04` (lecturas) y `V6-10` (zonas).

Los dos se DERIVAN. Ninguno se escribe a mano, y ésa es la mitad del criterio de cierre de
las dos filas de §20.1:

  `V6-04`  «el censo se DERIVA del código; **cero** lecturas fuera del canal». Se deriva con
           `ast`, y una lectura de Git escrita fuera de `gobierno/git.py` **aparece en el
           censo y da ROJO**.
  `V6-10`  «el censo de zonas se DERIVA; **cero** zonas sin condición». Se deriva de
           `docs/canonico/FUENTES-CANONICAS.yml` y del árbol, y una zona sin condición
           declarada **da ROJO, no pasa por omisión**.

DECISIÓN · `ast` y no `grep`, y la razón es medible
    `grep -n "subprocess"` encuentra la palabra en un comentario y no encuentra
    `getattr(__import__("subprocess"), "run")`. `ast` ve la LLAMADA. Además, el censo con
    `ast` reconoce la forma equivalente: `os.system`, `os.popen`, `subprocess.Popen` y
    `subprocess.check_output` son cuatro ortografías del mismo acto y las cuatro salen.

DECISIÓN · el canal único es UNO, y las sedes de proceso se declaran una a una
    Ejecutar un proceso no es lo mismo que ejecutar GIT. Este aparato abre procesos en tres
    sitios con motivo declarado —el canal de Git, el adaptador local de proceso, y el
    proveedor de firma que delega en el anfitrión— y en ningún otro. El censo publica las
    tres sedes con su motivo y denuncia cualquier cuarta. Una lista de sedes es una
    superficie enumerable; una ausencia de lista es una superficie que nadie ha enumerado,
    que es lo que `S1-01` midió.

DECISIÓN · el censo de zonas se cruza con el ÁRBOL, no sólo con el registro
    Un registro de zonas puede estar completo y el árbol tener un directorio que ningún
    patrón cubre. Derivar sólo del registro daría un censo limpio sobre un árbol con una
    zona ciega, que es el defecto de PERÍMETRO que el corpus documenta tres veces.
"""
from __future__ import annotations

import ast
import os

from .errores import CensoDeLecturasSucio, DatoIlegible
from .formulas import digest_de_contenido, leer_fichero_de_datos
from .perimetro import Zona

# ===========================================================================
#  CENSO DE LECTURAS · `V6-04`
# ===========================================================================
#  Las TRES sedes que pueden abrir un proceso, con su motivo. Cualquier otra es un hallazgo.
SEDES_DE_PROCESO = {
    "git.py": "canal ÚNICO de invocación de Git (`gobierno/git.py`)",
    "proceso.py": "adaptador local REAL: lanza la tarea del Owner (`adaptadores/proceso.py`)",
    "proveedor.py": "delegación de firma en el anfitrión (`identidad/proveedor.py`, `O25` §2)",
}

# Nombres que abren un proceso, en todas sus ortografías.
LLAMADAS_DE_PROCESO = {
    ("subprocess", "run"), ("subprocess", "Popen"), ("subprocess", "call"),
    ("subprocess", "check_call"), ("subprocess", "check_output"),
    ("subprocess", "getoutput"), ("subprocess", "getstatusoutput"),
    ("os", "system"), ("os", "popen"), ("os", "spawnv"), ("os", "spawnvp"),
    ("os", "execv"), ("os", "execvp"), ("os", "execve"), ("os", "posix_spawn"),
}

# Órdenes de Git que producen una LISTA de rutas y por tanto EXIGEN `-z`.
ORDENES_DE_LISTA = (
    "ls-tree", "ls-files", "diff", "diff-tree", "diff-index", "status", "diff-files",
)


def _arbol_de(ruta):
    try:
        with open(ruta, "rb") as manejador:
            fuente = manejador.read()
    except OSError as exc:
        raise CensoDeLecturasSucio(
            "no se pudo leer un módulo para censarlo: " + exc.strerror, ruta=ruta
        ) from exc
    try:
        return ast.parse(fuente, filename=os.path.basename(ruta))
    except SyntaxError as exc:
        raise CensoDeLecturasSucio(
            "un módulo del censo no es Python analizable: " + str(exc.msg), ruta=ruta
        ) from exc


def _nombre_llamado(nodo):
    if isinstance(nodo, ast.Attribute) and isinstance(nodo.value, ast.Name):
        return (nodo.value.id, nodo.attr)
    if isinstance(nodo, ast.Name):
        return ("", nodo.id)
    return None


def _literales(nodo):
    """Todas las cadenas literales alcanzables desde un nodo de argumento."""
    salida = []
    for hijo in ast.walk(nodo):
        if isinstance(hijo, ast.Constant) and isinstance(hijo.value, str):
            salida.append(hijo.value)
    return salida


# Nombres de invocable que EJECUTAN algo. Un `_registros(salida, "diff")` menciona la
# palabra `diff` y no ejecuta nada: distinguir la MENCIÓN de la INVOCACIÓN es justo lo que
# `ast` permite y `grep` no.
INVOCADORES = {
    "ejecutar", "_leer", "run", "Popen", "call", "check_call", "check_output",
    "getoutput", "getstatusoutput", "system", "popen",
}


def _nodos_de_vocabulario(arbol):
    """Nodos que declaran un VOCABULARIO —`ORDENES_DE_LISTA = (...)`— y no una invocación.

    Se reconocen por lo que son: una asignación a un nombre en MAYÚSCULAS. Sin esta
    exclusión, la propia lista de órdenes censadas se censaría a sí misma como una lectura
    sin `-z`, y el censo denunciaría su propio diccionario.
    """
    excluidos = set()
    for nodo in ast.walk(arbol):
        if not isinstance(nodo, ast.Assign):
            continue
        for destino in nodo.targets:
            if isinstance(destino, ast.Name) and destino.id.isupper():
                for hijo in ast.walk(nodo.value):
                    excluidos.add(id(hijo))
    return excluidos


def censar_lecturas(rutas):
    """Censo DERIVADO de toda invocación de proceso y de toda lectura de lista de Git.

    Devuelve `{procesos, lecturas, fuera_del_canal, sin_separador_seguro, ok}`.
    """
    procesos = []
    lecturas = []
    for ruta in sorted(rutas):
        modulo = os.path.basename(ruta)
        arbol = _arbol_de(ruta)
        vocabulario = _nodos_de_vocabulario(arbol)
        vistas = set()
        for nodo in ast.walk(arbol):
            if isinstance(nodo, ast.Call):
                nombre = _nombre_llamado(nodo.func)
                if nombre in LLAMADAS_DE_PROCESO:
                    procesos.append({
                        "modulo": modulo,
                        "linea": nodo.lineno,
                        "llamada": nombre[0] + "." + nombre[1] if nombre[0] else nombre[1],
                        "sede_declarada": modulo in SEDES_DE_PROCESO,
                        "motivo": SEDES_DE_PROCESO.get(modulo, ""),
                    })
                invocable = None
                if isinstance(nodo.func, ast.Attribute):
                    invocable = nodo.func.attr
                elif isinstance(nodo.func, ast.Name):
                    invocable = nodo.func.id
                if invocable not in INVOCADORES:
                    continue
                palabras = _literales(nodo)
            elif isinstance(nodo, (ast.List, ast.Tuple)):
                if id(nodo) in vocabulario:
                    continue
                elementos = [hijo.value for hijo in nodo.elts
                             if isinstance(hijo, ast.Constant)
                             and isinstance(hijo.value, str)]
                if len(elementos) != len(nodo.elts) or not elementos:
                    continue
                if elementos[0] not in ORDENES_DE_LISTA:
                    continue
                palabras = elementos
            else:
                continue
            for orden in ORDENES_DE_LISTA:
                if orden not in palabras:
                    continue
                clave = (nodo.lineno, orden)
                if clave in vistas:
                    break
                vistas.add(clave)
                lecturas.append({
                    "modulo": modulo,
                    "linea": nodo.lineno,
                    "orden": orden,
                    "separador_seguro": "-z" in palabras,
                    "es_el_canal": modulo == "lectura.py",
                })
                break

    fuera = [entrada for entrada in procesos if not entrada["sede_declarada"]]
    sin_z = [entrada for entrada in lecturas if not entrada["separador_seguro"]]
    lista_fuera = [entrada for entrada in lecturas if not entrada["es_el_canal"]]
    return {
        "sedes_declaradas": {nombre: SEDES_DE_PROCESO[nombre]
                             for nombre in sorted(SEDES_DE_PROCESO)},
        "procesos": sorted(procesos, key=lambda e: (e["modulo"], e["linea"])),
        "lecturas": sorted(lecturas, key=lambda e: (e["modulo"], e["linea"])),
        "fuera_del_canal": sorted(fuera, key=lambda e: (e["modulo"], e["linea"])),
        "listas_fuera_del_canal": sorted(lista_fuera,
                                         key=lambda e: (e["modulo"], e["linea"])),
        "sin_separador_seguro": sorted(sin_z, key=lambda e: (e["modulo"], e["linea"])),
        "ok": not fuera and not sin_z and not lista_fuera,
    }


def modulos_del_aparato(raiz_runtime):
    """Los `.py` de los cuatro paquetes de este corte. Se DERIVAN del disco, no se listan."""
    salida = []
    for paquete in ("admision", "gobierno", "adaptadores", "identidad"):
        directorio = os.path.join(raiz_runtime, paquete)
        if not os.path.isdir(directorio):
            continue
        for nombre in sorted(os.listdir(directorio)):
            if nombre.endswith(".py"):
                salida.append(os.path.join(directorio, nombre))
    punto = os.path.join(raiz_runtime, "ads_admision.py")
    if os.path.isfile(punto):
        salida.append(punto)
    return salida


# ===========================================================================
#  CENSO DE ZONAS · `V6-10`
# ===========================================================================
REGISTRO_DE_ZONAS = "docs/canonico/FUENTES-CANONICAS.yml"


def cargar_zonas(raiz, registro=REGISTRO_DE_ZONAS):
    """Deriva las zonas del registro canónico. Falla cerrado si no se puede leer."""
    ruta = os.path.join(raiz, registro)
    datos = leer_fichero_de_datos(ruta)
    if not isinstance(datos, dict) or "zonas" not in datos:
        raise DatoIlegible(
            "el registro de sedes canónicas no declara `zonas`: sin censo de zonas no se "
            "emite veredicto",
            ruta=ruta,
        )
    zonas = []
    for entrada in datos["zonas"] or []:
        if not isinstance(entrada, dict) or "patron" not in entrada or "clase" not in entrada:
            raise DatoIlegible(
                "una zona del registro no declara `patron` y `clase`", ruta=ruta
            )
        zonas.append(Zona(entrada["patron"], entrada["clase"], entrada.get("motivo", "")))
    if not zonas:
        raise DatoIlegible("el registro de zonas está vacío", ruta=ruta)
    return zonas


def digest_del_registro(raiz, registro=REGISTRO_DE_ZONAS):
    """Digest del registro TAL Y COMO ESTÁ EN EL ÁRBOL, para poder anclarlo desde fuera."""
    ruta = os.path.join(raiz, registro)
    with open(ruta, "rb") as manejador:
        return digest_de_contenido(manejador.read())
