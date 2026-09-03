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
    Ejecutar un proceso no es lo mismo que ejecutar GIT. Este aparato abre procesos SÓLO en
    las sedes que `SEDES_DE_PROCESO` declara, cada una con su motivo, y el censo denuncia
    cualquier otra. **Cuántas son no se escribe aquí**: se leen de la propia tabla, porque
    un cardinal al lado de su enumeración caduca en silencio en cuanto crece —y creció, con
    el puntero de §6.7, con la contención de `FD-5` y con los árboles de `V6-15`—. Una lista
    de sedes es una superficie enumerable; una ausencia de lista es una superficie que nadie
    ha enumerado, que es lo que `S1-01` midió.

DECISIÓN · el aparato se censa ENTERO, y la vía histórica se declara en vez de omitirse
    `arboles/` reproduce a propósito lecturas de Git de la ÉPOCA —sin `-z`— porque ése es
    el defecto que `V6-15` tiene que volver a provocar. Se podía dejar el paquete fuera del
    censo, y sería lo cómodo; entonces una lectura insegura NUEVA escrita ahí no aparecería
    en ninguna parte. Se mete dentro, y la vía histórica se publica acotada por
    `(paquete, módulo)` en `SEDES_DE_REPRODUCCION_HISTORICA`. Lo que no esté en esa tabla
    sigue dando ROJO, también dentro de `arboles/`.

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
#  Las sedes que pueden abrir un proceso, con su motivo. Cualquier otra es un hallazgo.
#  **Su número NO se escribe**: un cardinal al lado de su propia enumeración caduca en
#  silencio en cuanto la enumeración crece, que es la regla de `J-07`. Ya creció una vez.
SEDES_DE_PROCESO = {
    "git.py": "canal ÚNICO de invocación de Git (`gobierno/git.py`)",
    "proceso.py": "adaptador local REAL: lanza la tarea del Owner (`adaptadores/proceso.py`)",
    "proveedor.py": "delegación de firma en el anfitrión (`identidad/proveedor.py`, `O25` §2)",
    "puntero.py": "lectura del remoto canónico para localizar el control repo hermano "
                  "(`adaptadores/puntero.py`, §6.7 regla 4)",
    "deteccion.py": "sondas REALES de las capacidades de contención del anfitrión "
                    "(`contencion/deteccion.py`, `FD-5`)",
    "backends.py": "contenedores de recursos del anfitrión (`contencion/backends.py`, `FD-5`)",
    "ejecutor.py": "lanzamiento de la tarea DENTRO de la contención (`contencion/ejecutor.py`)",
    "versiones.py": "REPRODUCCIÓN HISTÓRICA de las versiones vulnerables de `V6-15` "
                    "(`arboles/versiones.py`); ver `SEDES_DE_REPRODUCCION_HISTORICA`",
    "ataques.py": "materialización de los árboles adversariales en repositorios reales "
                  "(`arboles/ataques.py`, `V6-15` §20.5)",
}

#  LA EXCEPCIÓN HISTÓRICA, ACOTADA Y PUBLICADA · `V6-15`
#
#  DECISIÓN de `F6`, y va contra la comodidad. `arboles/` reproduce los defectos que los
#  gates derribaron, y uno de ellos —`S1-01`— ES una lectura de lista sin `-z`: una versión
#  histórica que pasara por el canal único NO PODRÍA reproducir su propio defecto, y la
#  fila entera de la matriz dejaría de significar nada.
#
#  Alternativas: (a) dejar `arboles/` FUERA de `modulos_del_aparato`, que es lo cómodo;
#  (b) meterlo dentro y declarar la excepción, acotada al MÓDULO y al PAQUETE.
#  Se elige (b). Con (a) el paquete queda sin censar entero, y entonces una lectura insegura
#  NUEVA escrita en cualquier fichero de `arboles/` no aparecería en ningún sitio: sería
#  exactamente la superficie que nadie ha enumerado que `S1-01` midió. Con (b) el paquete se
#  censa, la vía histórica se PUBLICA con su motivo en `reproduccion_historica`, y cualquier
#  lectura insegura fuera de esos módulos declarados sigue dando ROJO.
#
#  La clave es `(paquete, módulo)` y no sólo el nombre del fichero: si fuera el nombre, un
#  `versiones.py` nuevo en `admision/` heredaría la exención, y la excepción se habría
#  convertido en un agujero.
SEDES_DE_REPRODUCCION_HISTORICA = {
    ("arboles", "versiones.py"):
        "las versiones VULNERABLES de `V6-15`: leen Git con la configuración de la ÉPOCA "
        "—sin `-z`, sin `core.quotePath=false`— porque ése ES el defecto que reproducen "
        "(`S1-01`). Pasar por el canal único las volvería incapaces de fallar",
    ("arboles", "ataques.py"):
        "la materialización de los árboles adversariales en repositorios Git reales: "
        "construye el árbol atacado, y construirlo no es verificarlo",
}

# Lo ÚNICO que queda fuera del censo del aparato, con su motivo. No es una lista de lo que
# entra —eso se deriva del disco—: es la lista de lo que se excluye, que es mucho más corta
# y mucho más difícil de estirar sin que se note.
PAQUETES_EXCLUIDOS = {
    "pruebas": "las baterías EJERCEN el aparato y abren procesos a propósito —matan, lanzan "
               "contenedores, provocan caídas—; censarlas denunciaría el instrumento de "
               "medida en vez del aparato",
    "__pycache__": "artefactos de ejecución, no código fuente",
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


def _envoltorios_de_proceso(arbol):
    """Las funciones del MÓDULO que, directa o transitivamente, abren un proceso.

    DECISIÓN de `F6`, y cierra un FALSO NEGATIVO medido. `INVOCADORES` es una lista de
    nombres, y una lista de nombres se esquiva escribiendo otro nombre: basta envolver
    `subprocess.run` en un `_git_historico()` local para que una lectura de lista sin `-z`
    deje de aparecer en el censo. Ocurrió de verdad —`arboles/versiones.py` lo hace, y el
    censo no la veía— y es exactamente el modo de fallo de `S1-01`: la superficie que nadie
    ha enumerado.

    Alternativas: (a) añadir esos dos nombres a `INVOCADORES`, que es jugar al topo; (b)
    retirar `INVOCADORES` y censar toda llamada con una orden de lista entre sus literales,
    que produce FALSOS ROJOS sobre menciones —`_registros(salida, "diff")`— y un censo con
    falsos rojos se acaba desactivando; (c) DERIVAR, por módulo, qué funciones alcanzan un
    proceso, y tratarlas como invocadoras.
    Se elige (c): no depende de que nadie mantenga una lista, distingue la mención de la
    invocación igual que antes, y el envoltorio deja de ser un escondite.
    """
    cuerpo_de = {}
    for nodo in ast.walk(arbol):
        if isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef)):
            cuerpo_de[nodo.name] = nodo

    directas = set()
    llamadas_de = {}
    for nombre, definicion in cuerpo_de.items():
        llamadas_de[nombre] = set()
        for hijo in ast.walk(definicion):
            if not isinstance(hijo, ast.Call):
                continue
            llamado = _nombre_llamado(hijo.func)
            if llamado in LLAMADAS_DE_PROCESO:
                directas.add(nombre)
            if isinstance(hijo.func, ast.Name):
                llamadas_de[nombre].add(hijo.func.id)

    # Cierre transitivo: quien llama a un envoltorio también lo es. Sin él, un segundo nivel
    # de envoltura —`_rutas_por_split` sobre `_git_historico`— volvería a esconder la lectura.
    alcanzan = set(directas)
    creciendo = True
    while creciendo:
        creciendo = False
        for nombre, llamadas in llamadas_de.items():
            if nombre in alcanzan:
                continue
            if llamadas & alcanzan:
                alcanzan.add(nombre)
                creciendo = True
    return alcanzan


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
        paquete = os.path.basename(os.path.dirname(ruta))
        historica = SEDES_DE_REPRODUCCION_HISTORICA.get((paquete, modulo))
        arbol = _arbol_de(ruta)
        vocabulario = _nodos_de_vocabulario(arbol)
        invocadores = INVOCADORES | _envoltorios_de_proceso(arbol)
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
                if invocable not in invocadores:
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
                    "paquete": paquete,
                    "linea": nodo.lineno,
                    "orden": orden,
                    "separador_seguro": "-z" in palabras,
                    "es_el_canal": modulo == "lectura.py",
                    # Publicada, no escondida: la vía histórica aparece en el censo con su
                    # motivo, y sólo por eso deja de contar como hallazgo.
                    "reproduccion_historica": historica or "",
                })
                break

    fuera = [entrada for entrada in procesos if not entrada["sede_declarada"]]
    historicas = [entrada for entrada in lecturas if entrada["reproduccion_historica"]]
    juzgables = [entrada for entrada in lecturas if not entrada["reproduccion_historica"]]
    sin_z = [entrada for entrada in juzgables if not entrada["separador_seguro"]]
    lista_fuera = [entrada for entrada in juzgables if not entrada["es_el_canal"]]
    return {
        "sedes_declaradas": {nombre: SEDES_DE_PROCESO[nombre]
                             for nombre in sorted(SEDES_DE_PROCESO)},
        "reproduccion_historica": sorted(
            ({"paquete": clave[0], "modulo": clave[1], "motivo": motivo}
             for clave, motivo in SEDES_DE_REPRODUCCION_HISTORICA.items()),
            key=lambda e: (e["paquete"], e["modulo"]),
        ),
        "lecturas_historicas": sorted(historicas,
                                      key=lambda e: (e["paquete"], e["modulo"], e["linea"])),
        "procesos": sorted(procesos, key=lambda e: (e["modulo"], e["linea"])),
        "lecturas": sorted(lecturas, key=lambda e: (e["modulo"], e["linea"])),
        "fuera_del_canal": sorted(fuera, key=lambda e: (e["modulo"], e["linea"])),
        "listas_fuera_del_canal": sorted(lista_fuera,
                                         key=lambda e: (e["modulo"], e["linea"])),
        "sin_separador_seguro": sorted(sin_z, key=lambda e: (e["modulo"], e["linea"])),
        "ok": not fuera and not sin_z and not lista_fuera,
    }


def modulos_del_aparato(raiz_runtime):
    """TODOS los `.py` del runtime, DERIVADOS del disco. Ni los paquetes se enumeran.

    DEFECTO QUE CIERRA, encontrado por la auditoría independiente. Esta función enumeraba
    los paquetes A MANO, y la lista envejeció exactamente como su propio docstring advertía
    que envejecen las listas a mano: el macrobloque que creó `ciclo/` y `macrocircuitos/`
    **no los añadió**, de modo que el censo de `V6-04` dejaba fuera 45 de los 82 módulos del
    runtime —el 55 %—, incluidos los dos que ese mismo corte acababa de escribir. Una
    lectura insegura de Git escrita en `ciclo/`, `macrocircuitos/`, `estado/` o `runtime/`
    era INVISIBLE para el censo que promete «cero lecturas fuera del canal».

    Ahora el criterio no es una lista: es una PROPIEDAD del disco —ser un paquete Python
    dentro del runtime—, y un paquete nuevo entra solo el día que se crea. `PAQUETES_EXCLUIDOS`
    dice, uno a uno y con su motivo, qué queda fuera y por qué; cualquier otra cosa entra.
    """
    salida = []
    for entrada in sorted(os.listdir(raiz_runtime)):
        directorio = os.path.join(raiz_runtime, entrada)
        if entrada in PAQUETES_EXCLUIDOS or not os.path.isdir(directorio):
            continue
        if not os.path.isfile(os.path.join(directorio, "__init__.py")):
            continue
        for nombre in sorted(os.listdir(directorio)):
            if nombre.endswith(".py"):
                salida.append(os.path.join(directorio, nombre))
    for nombre in sorted(os.listdir(raiz_runtime)):
        if nombre.startswith("ads_") and nombre.endswith(".py"):
            salida.append(os.path.join(raiz_runtime, nombre))
    return salida


# Los paquetes del APARATO DE VERIFICACIÓN, que es el sujeto que `V6-19` declara: «el
# conjunto de instrumentos del aparato de verificación y las fórmulas que más de uno
# necesita». NO es el mismo sujeto que el del censo de LECTURAS, y mezclarlos sería un error
# con consecuencias.
#
# POR QUÉ SON DOS ÁMBITOS Y NO UNO, dicho porque la tentación de unificarlos es fuerte:
#
#   `V6-04` · LECTURAS  el riesgo es que CUALQUIER módulo abra Git por una vía paralela, así
#                       que su ámbito tiene que ser TODO el runtime. Un módulo fuera del
#                       censo es una superficie que nadie ha enumerado.
#   `V6-19` · FÓRMULAS  el riesgo es que dos INSTRUMENTOS DE VERIFICACIÓN calculen lo mismo
#                       de dos maneras y diverjan. Su ámbito es el aparato de verificación.
#
# Aplicar el ámbito de `V6-04` al censo de fórmulas obligaría al MOTOR de estado durable a
# importar su direccionamiento por contenido desde el verificador de admisión: la flecha de
# dependencia al revés, y el motor dejando de poder existir sin el verificador. `cid_de_objeto`
# del motor y `digest_de_contenido` del verificador coinciden en usar SHA-256 y NO son la
# misma fórmula: una identifica objetos durables y la otra resume ficheros para anclarlos.
PAQUETES_DEL_VERIFICADOR = ("admision", "gobierno", "adaptadores", "identidad", "arboles")


def modulos_del_verificador(raiz_runtime):
    """Los `.py` del aparato de VERIFICACIÓN. Sujeto de `V6-19`, no de `V6-04`."""
    salida = []
    for paquete in PAQUETES_DEL_VERIFICADOR:
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
