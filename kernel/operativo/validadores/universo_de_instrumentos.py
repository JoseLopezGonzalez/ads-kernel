#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`O31` §3 y §5 · EL UNIVERSO DE INSTRUMENTOS, DERIVADO DEL ÁRBOL Y NO DEL MANIFIESTO.

QUÉ DEFECTO CIERRA, Y POR QUÉ ERA DE CLASE
------------------------------------------------------------------------------
El verificador independiente de `O30` registró dos GRAVES que son la misma cosa vista
desde dos sitios:

  `V-G1`  la comprobación de completitud del manifiesto enumeraba SÓLO
          `kernel/operativo/validadores/*.py`, y el manifiesto reparte sus filas en
          CUATRO directorios. Lo que vivía fuera del glob no existía para el control.
  `M-04`  el universo esperado se leía del MANIFIESTO cuya completitud se estaba
          juzgando. Quien edita el manifiesto edita a la vez el hecho y su medida.

Medido sobre `4d99a5e` antes de esta corrección: retirar la fila `invariantes-criticos`
—el instrumento que mide `K01`–`K24`— y borrar su evidencia dejaba
`comprobar_evidencia.py` en `2 superadas · 0 fallidas`, `rc=0`; y regenerando huella y
sello, la batería ENTERA del corpus daba verde. Es el «duodécimo árbol».

CÓMO SE DERIVA, Y POR QUÉ ASÍ
------------------------------------------------------------------------------
No se enumera ningún directorio. Un PUNTO EJECUTABLE es cualquier `.py` del árbol cuyo
árbol sintáctico contenga la guarda `if __name__ == "__main__":`. Es una propiedad del
FICHERO, no de su ruta: moverlo, renombrarlo o crear un directorio nuevo no lo saca del
universo, y ésa es exactamente la diferencia entre juzgar la clase y juzgar la instancia.

Se usa `ast` y no `grep`: la cadena `__main__` dentro de un comentario, de una cadena de
texto o de un mensaje de diagnóstico NO cuenta. Lo que cuenta es la guarda real.

Medido el 2026-09-07 sobre este árbol: 59 puntos ejecutables en NUEVE directorios, y
**cero** puntos con `__main__` que no lleven además la guarda de aislamiento `G-03`. El
marcador estructural es, por tanto, completo sobre este corpus.

LO QUE NO ES UN VALIDADOR, Y CÓMO SE DECLARA
------------------------------------------------------------------------------
Hay puntos ejecutables que legítimamente no son filas del manifiesto de validadores: la
línea de órdenes del producto, el paquete SEPARADO de la raíz externa, el instalador de
proyectos. Su exclusión NO se escribe aquí como lista de rutas —eso sería el mismo
defecto de clase con otro disfraz, y `O31` §3 lo prohíbe con esas palabras—: se declara
DENTRO DEL PROPIO FICHERO, con su motivo, en la constante

    FUERA_DEL_MANIFIESTO_DE_VALIDADORES = "motivo por el que este punto no es un validador"

La declaración viaja con el fichero. Moverlo la conserva; borrarla lo devuelve al
universo y lo pone rojo; y un instrumento NUEVO que nadie declare aparece rojo por su
ausencia material, no por una lista que alguien tenga que acordarse de actualizar.
"""
from __future__ import annotations

import ast
import os

# El nombre de la constante con la que un punto ejecutable declara que NO es un validador
# del manifiesto. Se lee del propio fichero: es una declaración, no una lista.
MARCA_DE_EXCLUSION = "FUERA_DEL_MANIFIESTO_DE_VALIDADORES"

# Directorios que no son corpus. No es la lista de instrumentos —ésa se deriva—: es lo
# que no se recorre porque no es del árbol.
NO_SE_RECORRE = (".git", "__pycache__", ".pytest_cache", "node_modules", ".venv")

DIR_VALIDADORES_POR_DEFECTO = "kernel/operativo/validadores"
DIR_EVIDENCIA = "kernel/operativo/pruebas/evidencia"

# Los enlaces a directorio que el último recorrido encontró. No es estado oculto:
# `enlaces_a_directorio()` los devuelve y el instrumento los PUBLICA.
_ENLACES_VISTOS = {}


def enlaces_a_directorio(base):
    """Los enlaces a directorio hallados dentro del ámbito, recorriendo si hace falta."""
    clave = os.path.abspath(base)
    if clave not in _ENLACES_VISTOS:
        puntos_ejecutables(base)
    return _ENLACES_VISTOS.get(clave, [])


def _es_punto_ejecutable(arbol):
    """¿Es esto un punto ejecutable? Tres señales, y basta UNA.

    LA PRIMERA VERSIÓN DE ESTA FUNCIÓN ERA DERROTABLE, Y LO DIJO UN CRÍTICO ADVERSARIAL
    ANTES DE QUE SE PUBLICARA. Miraba SÓLO `arbol.body` y exigía que la constante
    `"__main__"` estuviera literalmente en el test. Escapaban, sin dejar rastro:

        MAIN = "__main__"
        if __name__ == MAIN: ...          # la constante no está en el test

        try:                              # el `If` no está en `arbol.body`
            if __name__ == "__main__": ...
        except KeyboardInterrupt: ...

        sys.exit(main())                  # línea de órdenes sin guarda ninguna

    Los tres sacaban el fichero del universo ENTERO —ni fila, ni exclusión, ni ruido—, que
    es el vaciado más limpio posible. Ahora:

      1 · cualquier `If` del árbol ENTERO cuyo test mencione `__name__`, con constante o
          sin ella. Un fichero que consulta `__name__` para decidir si arranca ES un punto
          ejecutable, y qué constante compare da igual;
      2 · una llamada a `sys.exit(...)` o `main()` a nivel de módulo;
      3 · lo dice quien lo lee: un `#!` de intérprete en la primera línea, que se comprueba
          fuera de esta función, sobre los bytes.
    """
    for nodo in ast.walk(arbol):
        if isinstance(nodo, ast.If):
            for hijo in ast.walk(nodo.test):
                if isinstance(hijo, ast.Name) and hijo.id == "__name__":
                    return True
    for nodo in arbol.body:
        if not isinstance(nodo, ast.Expr) or not isinstance(nodo.value, ast.Call):
            continue
        llamada = nodo.value.func
        nombre = (llamada.attr if isinstance(llamada, ast.Attribute)
                  else llamada.id if isinstance(llamada, ast.Name) else "")
        if nombre in ("exit", "main"):
            return True
    return False


def _motivo_de_exclusion(arbol):
    """El motivo declarado DENTRO del fichero, o `None` si no lo declara."""
    for nodo in arbol.body:
        if not isinstance(nodo, ast.Assign):
            continue
        for destino in nodo.targets:
            if isinstance(destino, ast.Name) and destino.id == MARCA_DE_EXCLUSION:
                if isinstance(nodo.value, ast.Constant) and isinstance(nodo.value.value, str):
                    return nodo.value.value.strip() or None
    return None


def normalizar_ruta(base, directorio, script):
    """La ruta CANÓNICA de una invocación, relativa a la raíz y con separador `/`.

    `O31` §4.6 exige que «una ruta equivalente pero no idéntica a la declarada» falle. Lo
    que hace equivalentes a `docs/x.py`, `./docs/x.py`, `docs/./x.py` y `docs/a/../x.py`
    es que `normpath` las lleva a la misma cadena; lo que las hace distintas de la
    declarada es que la comparación se hace sobre ESA cadena y no sobre el basename.
    """
    bruta = os.path.join(directorio or DIR_VALIDADORES_POR_DEFECTO, script or "")
    ruta = os.path.normpath(bruta).replace(os.sep, "/")
    # Una ruta que se sale de la raíz no es del corpus, y se devuelve tal cual para que
    # quien la juzgue la vea salirse en vez de recibirla ya saneada.
    if os.path.isabs(ruta):
        try:
            ruta = os.path.relpath(ruta, base).replace(os.sep, "/")
        except ValueError:
            pass
    return ruta


def puntos_ejecutables(base):
    """`{ruta relativa: motivo_de_exclusion o None}` para todo punto ejecutable del árbol.

    Recorre el árbol ENTERO. No conoce ningún directorio de instrumentos, y por eso un
    directorio nuevo no lo deja fuera.
    """
    encontrados, enlaces = {}, []
    for dirpath, dirnames, filenames in os.walk(base):
        # ENLACES A DIRECTORIO · `os.walk` NO los sigue, y un crítico adversarial midió
        # que colgar un directorio de instrumentos detrás de un enlace los hace
        # INVISIBLES al recorrido. No se siguen —seguirlos abre ciclos— : se REGISTRAN,
        # y quien juzgue tendrá que decir algo de ellos. Un enlace a directorio dentro
        # del corpus no es una situación normal; en silencio no se queda.
        for d in list(dirnames):
            if os.path.islink(os.path.join(dirpath, d)):
                enlaces.append(os.path.relpath(os.path.join(dirpath, d), base)
                               .replace(os.sep, "/"))
        dirnames[:] = [d for d in dirnames if d not in NO_SE_RECORRE]
        for nombre in sorted(filenames):
            ruta_abs = os.path.join(dirpath, nombre)
            rel = os.path.relpath(ruta_abs, base).replace(os.sep, "/")
            # LA EXTENSIÓN NO DEFINE UN INSTRUMENTO, Y ÉSA FUE OTRA MEDIDA DEL CRÍTICO:
            # `.pyw`, `.py3` y un ejecutable con `#!` y sin extensión escapaban de un
            # censo por sufijo. Entra todo lo que sea `.py*` O lleve un `#!` de python.
            if not nombre.endswith((".py", ".pyw", ".py3")):
                try:
                    with open(ruta_abs, "rb") as manejador:
                        primera = manejador.readline(200)
                except OSError:
                    continue
                if not (primera.startswith(b"#!") and b"python" in primera):
                    continue
            try:
                with open(ruta_abs, encoding="utf-8") as manejador:
                    fuente = manejador.read()
                arbol = ast.parse(fuente, filename=rel)
            except (OSError, SyntaxError, UnicodeDecodeError):
                # Un fichero que no se puede leer o no compila NO se descarta en silencio:
                # entra en el universo sin motivo de exclusión, y quien lo juzgue tendrá
                # que decir algo de él. Descartarlo aquí sería la puerta de atrás.
                encontrados[rel] = None
                continue
            # EL `#!` POR SÍ SOLO NO BASTA, y esto se midió: en este corpus TODOS los
            # módulos de biblioteca del runtime llevan `#!/usr/bin/env python3` y ninguno
            # es un punto de entrada. Lo que separa a un punto ejecutable de un módulo es
            # que ALGUIEN lo pueda arrancar: `#!` MÁS bit de ejecución. Un fichero que
            # lleva las dos cosas está declarando que se invoca directamente.
            arrancable = fuente.startswith("#!") and os.access(ruta_abs, os.X_OK)
            if _es_punto_ejecutable(arbol) or arrancable:
                encontrados[rel] = _motivo_de_exclusion(arbol)
    _ENLACES_VISTOS[os.path.abspath(base)] = sorted(enlaces)
    return encontrados


def tiene_main(base, rel):
    """¿Este fichero concreto es un punto ejecutable? Para contrastar una fila suelta."""
    ruta = os.path.join(base, rel)
    if not os.path.isfile(ruta):
        return False
    try:
        with open(ruta, encoding="utf-8") as manejador:
            return _es_punto_ejecutable(ast.parse(manejador.read(), filename=rel))
    except (OSError, SyntaxError, UnicodeDecodeError):
        return False


def rutas_del_manifiesto(base, componentes):
    """`{ruta normalizada: [ids de las filas que la declaran]}`."""
    reparto = {}
    for comp in componentes:
        ruta = normalizar_ruta(base, comp.get("dir"), comp.get("script"))
        reparto.setdefault(ruta, []).append(comp.get("id"))
    return reparto


def universo_contra_manifiesto(base, componentes):
    """La resta en LOS DOS SENTIDOS, que es lo que `O31` §3 y §5 mandan contrastar.

    Devuelve un mapa con:
      `puntos`              todo punto ejecutable del árbol, con su motivo de exclusión
      `sin_fila`            puntos que NO son fila del manifiesto NI declaran su exclusión
      `excluidos`           puntos que declaran su exclusión, con el motivo
      `filas_sin_fichero`   filas cuyo ejecutable no existe donde dicen
      `validador_sin_main`  filas `tipo: validador` cuyo fichero no es punto ejecutable
      `biblioteca_con_main` filas `tipo: biblioteca` que sí lo son
    """
    puntos = puntos_ejecutables(base)
    reparto = rutas_del_manifiesto(base, componentes)

    # LA MARCA DE EXCLUSIÓN NO PUEDE RETIRAR NADA DEL APARATO, Y ÉSA ES SU ÚNICA LIMITACIÓN
    # SERIA.
    #
    #     UN CRÍTICO ADVERSARIAL LO VIO ANTES DE QUE ESTO SE PUBLICARA, y tenía razón: si
    #     bastara con escribir `FUERA_DEL_MANIFIESTO_DE_VALIDADORES` dentro del fichero,
    #     el duodécimo árbol de `M-04` se rehacía en dos líneas —añadir la marca al
    #     instrumento que mide `K01`–`K24` y retirar su fila—, y la misma mano seguiría
    #     moviendo el hecho y su medida. El defecto habría pasado de un glob a una
    #     constante que viaja DENTRO del objeto medido.
    #
    #     LO QUE LO CIERRA es que la marca sólo puede EXPLICAR lo que nunca estuvo en el
    #     aparato, nunca RETIRAR lo que sí estaba. La frontera no la decide quien escribe
    #     la marca: la decide la HISTORIA. Si `HEAD` declaraba esa ruta como fila del
    #     manifiesto y ahora el fichero reclama exclusión, es el gesto del vaciado y se
    #     falla cerrado. Añadir la marca a un fichero nuevo sigue siendo legítimo y sigue
    #     publicándose con su motivo en la evidencia, que es donde alguien lo audita.
    declaradas_en_head = rutas_declaradas_en_head(base)

    sin_fila, excluidos, exclusiones_ilegitimas = [], {}, []
    for ruta, motivo in sorted(puntos.items()):
        if ruta in reparto:
            if motivo:
                exclusiones_ilegitimas.append(
                    (ruta, "es fila VIVA del manifiesto y a la vez declara `%s`: una cosa "
                           "o la otra" % MARCA_DE_EXCLUSION))
            continue
        if motivo:
            if declaradas_en_head is not None and ruta in declaradas_en_head:
                exclusiones_ilegitimas.append(
                    (ruta, "`HEAD` la declara como fila del manifiesto y este árbol la "
                           "retira reclamando exclusión. La marca EXPLICA lo que nunca "
                           "estuvo en el aparato; no RETIRA lo que sí estaba"))
            else:
                excluidos[ruta] = motivo
        else:
            sin_fila.append(ruta)

    filas_sin_fichero, validador_sin_main, biblioteca_con_main = [], [], []
    for comp in componentes:
        ruta = normalizar_ruta(base, comp.get("dir"), comp.get("script"))
        existe = os.path.isfile(os.path.join(base, ruta))
        if not existe:
            filas_sin_fichero.append((comp.get("id"), ruta))
            continue
        es_punto = ruta in puntos
        if comp.get("tipo") == "validador" and not es_punto:
            validador_sin_main.append((comp.get("id"), ruta))
        if comp.get("tipo") == "biblioteca" and es_punto:
            biblioteca_con_main.append((comp.get("id"), ruta))

    return {
        "puntos": puntos,
        "sin_fila": sin_fila,
        "excluidos": excluidos,
        "exclusiones_ilegitimas": exclusiones_ilegitimas,
        "filas_sin_fichero": filas_sin_fichero,
        "validador_sin_main": validador_sin_main,
        "biblioteca_con_main": biblioteca_con_main,
        "directorios": sorted({os.path.dirname(p) for p in puntos}),
    }


# ---------------------------------------------------------------------------
#  `O31` §4 · LA IDENTIDAD CANÓNICA DE UNA INVOCACIÓN
# ---------------------------------------------------------------------------
#  QUÉ DEFECTO CIERRA. `V-G2`: la dispensa reflexiva se concedía al SCRIPT, sondeado con
#  argumentos FIJOS, y nunca miraba los `args:` ni el `dir:` declarados de la FILA. Medido:
#  una fila con el script legítimo y `args: ['--help']` obtenía la dispensa y dejaba el
#  guardián en `2 superadas · 0 fallidas`.
#
#  La identidad reúne los SIETE elementos que `O31` §4 enumera. Dos filas que difieran en
#  cualquiera de ellos tienen identidades distintas, y una dispensa pertenece a UNA.
def _normalizar_argumentos(args):
    """Los argumentos en forma canónica, SIN reordenarlos.

    NO se ordenan: `--solo A --hasta B` y `--hasta B --solo A` son invocaciones distintas
    para cualquier `argparse` con posicionales, y tratarlas como iguales sería volver a
    conceder por parecido. Sí se unifica `--opcion=valor` con `--opcion valor`, porque
    ésas SÍ son la misma invocación y distinguirlas dejaría pasar la fila legítima escrita
    de la otra manera.
    """
    import unicodedata                                                # noqa: PLC0415
    partidos = []
    for bruto in (args or ()):
        # NFC Y ESPACIOS REALES. Un crítico adversarial midió que un espacio duro U+00A0 o
        # unos acentos en NFD producen una cadena que `.strip()` no toca, que no casa con
        # ninguna clave del corpus y que además contamina cualquier nombre derivado de
        # ella. Se normaliza ANTES de comparar nada.
        texto = unicodedata.normalize("NFC", str(bruto))
        texto = "".join(" " if unicodedata.category(c) == "Zs" else c for c in texto)
        if texto.startswith("--") and "=" in texto:
            opcion, valor = texto.split("=", 1)
            partidos.extend([opcion, valor])
        else:
            partidos.append(texto)
    # BANDERAS REPETIDAS. `--sin-ejecutar --sin-ejecutar` es, para `argparse`, la misma
    # invocación que `--sin-ejecutar`: el crítico la usó para fabricar una invocación
    # «distinta» que en realidad era la misma. Se colapsa la repetición CONSECUTIVA e
    # inmediata de una bandera larga sin valor, que es el único caso en que la
    # equivalencia es segura; no se reordena nada, porque reordenar rompería posicionales.
    limpios = []
    for pieza in partidos:
        if (pieza.startswith("--") and limpios and limpios[-1] == pieza):
            continue
        limpios.append(pieza)
    return tuple(limpios)


def invocacion_ejecutada(base, comp):
    """LO QUE DE VERDAD SE EJECUTA: ruta REAL, digest del CONTENIDO, cwd real y argumentos.

    ES DISTINTA DE LA IDENTIDAD, Y SEPARARLAS ES LO QUE UN CRÍTICO ADVERSARIAL EXIGIÓ.
    La identidad de `O31` §4 incluye el `id` de la fila y su evidencia, y los `id` son
    únicos por construcción: si la detección de FILAS GEMELAS se hiciera con ella, no
    podría dispararse nunca y la condición que HOY sí funciona quedaría convertida en un
    adorno. Así que se parten en dos:

      · esta función responde «¿es la misma ejecución?» y sirve para cazar gemelas;
      · `identidad_de_invocacion` responde «¿a quién pertenece esta dispensa?».

    Y responde a la primera con el CONTENIDO, no con el nombre. El mismo crítico midió el
    ataque: copiar el instrumento legítimo byte a byte a otro nombre, colgarlo de un
    ENLACE de directorio y escribir argumentos `argparse`-equivalentes obtenía la dispensa.
    Contra eso, `realpath` resuelve el enlace y el digest resuelve la copia: dos rutas
    distintas con el mismo contenido son la misma ejecución.
    """
    import hashlib                                                    # noqa: PLC0415
    rel = normalizar_ruta(base, comp.get("dir"), comp.get("script"))
    absoluta = os.path.realpath(os.path.join(base, rel))
    try:
        with open(absoluta, "rb") as manejador:
            digest = hashlib.sha256(manejador.read()).hexdigest()
    except OSError:
        digest = "NO-SE-PUDO-LEER"
    cwd = os.path.realpath(os.path.join(base, comp.get("dir")
                                        or DIR_VALIDADORES_POR_DEFECTO))
    return (digest, cwd, _normalizar_argumentos(comp.get("args")))


def argumentos_bien_formados(comp):
    """`(sí_o_no, motivo)`. Un `args:` que no sea lista de cadenas FALLA CERRADO.

    Medido por el crítico: `args: --autopruebas` escrito como ESCALAR de YAML hace que
    `for bruto in args` recorra CARACTERES, con lo que la invocación normalizada sale
    `('-','-','a','u',…)` y no coincide jamás con ninguna otra. La detección de gemelas se
    derrota con un par de corchetes de menos, y en silencio. Y el runner, que concatena
    `[ruta] + args`, revienta con `TypeError` fuera del `except` de la sonda.
    """
    args = comp.get("args")
    if args is None:
        return True, ""
    if not isinstance(args, (list, tuple)):
        return False, ("`args` es %s y tiene que ser una LISTA de cadenas. Un escalar se "
                       "recorre carácter a carácter y produce una invocación que no "
                       "coincide con ninguna" % type(args).__name__)
    for bruto in args:
        if not isinstance(bruto, str):
            return False, ("`args` contiene %r, que es %s y no una cadena. El runner lo "
                           "pasa tal cual a `subprocess` y revienta"
                           % (bruto, type(bruto).__name__))
    return True, ""


def identidad_de_invocacion(base, comp, obligacion):
    """Los SIETE elementos de `O31` §4, en una tupla comparable y publicable.

    Se devuelve la TUPLA y no un hash: un hash esconde en qué difieren dos invocaciones, y
    el diagnóstico de un rechazo tiene que poder decirlo. El hash se calcula aparte, para
    publicarlo, en `huella_de_identidad`.
    """
    return (
        ("obligacion", (obligacion or "").strip()),
        ("id", (comp.get("id") or "").strip()),
        ("script", normalizar_ruta(base, comp.get("dir"), comp.get("script"))),
        ("cwd", os.path.normpath(comp.get("dir") or DIR_VALIDADORES_POR_DEFECTO)
                  .replace(os.sep, "/")),
        ("args", _normalizar_argumentos(comp.get("args"))),
        ("evidencia", (comp.get("evidencia") or "").strip()),
        ("cierre", (comp.get("firma_de_exito") or "").strip()),
    )


def huella_de_identidad(identidad):
    """El digest de la identidad, para publicarlo en la evidencia sin volcar la tupla."""
    import hashlib                                                    # noqa: PLC0415
    texto = "\n".join("%s=%r" % (clave, valor) for clave, valor in identidad)
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def diferencias(una, otra):
    """En qué elementos difieren dos identidades. Es lo que publica un rechazo."""
    izquierda, derecha = dict(una), dict(otra)
    return sorted(c for c in izquierda if izquierda[c] != derecha.get(c))


# ---------------------------------------------------------------------------
#  `O31` §5 · LA SEGUNDA FUENTE INDEPENDIENTE: LO QUE LA HISTORIA YA CONFIRMÓ
# ---------------------------------------------------------------------------
#  POR QUÉ HACE FALTA UNA SEGUNDA. La primera fuente —los puntos ejecutables del árbol—
#  contrasta por RUTA, y una ruta puede respaldar VARIAS filas: `comprobar-invariantes-
#  criticos.py` respalda `invariantes-criticos` y `invariantes-criticos-autopruebas`.
#  Medido durante esta misma corrección: retirar la fila que mide `K01`–`K24` dejando la
#  de autopruebas mantiene la ruta declarada, y el contraste por ruta NO lo ve. El
#  duodécimo árbol de `M-04` seguía en pie.
#
#  LA SEGUNDA FUENTE NO ES EL MANIFIESTO NI EL ÁRBOL DE TRABAJO: es la HISTORIA. Toda
#  evidencia que `HEAD` tiene confirmada fue producida por una fila, y su desaparición del
#  manifiesto es exactamente el gesto que `M-04` describe. Quien quiera vaciar el universo
#  tendría que reescribir la historia, que está prohibido y es detectable.
#
#  Y NO SE MUERDE LA COLA: no se pregunta al manifiesto qué evidencias espera, sino a
#  `git` qué evidencias EXISTEN CONFIRMADAS. Un instrumento retirado deliberadamente se
#  declara —su evidencia se retira del árbol Y del manifiesto en el mismo commit, y a
#  partir del siguiente `HEAD` ya no está—, de modo que la regla no impide retirar: impide
#  retirar EN SILENCIO dentro del árbol que se está juzgando.
def evidencias_confirmadas(base, subdirectorio=DIR_EVIDENCIA):
    """Los `*-salida.txt` que `HEAD` tiene confirmados. `None` si no hay historia."""
    import subprocess                                                 # noqa: PLC0415
    proc = subprocess.run(["git", "-C", base, "ls-tree", "--name-only", "HEAD",
                           subdirectorio + "/"], capture_output=True, text=True)
    if proc.returncode != 0:
        return None
    nombres = set()
    for linea in proc.stdout.splitlines():
        nombre = os.path.basename(linea.strip())
        if nombre.endswith(".txt"):
            nombres.add(nombre)
    return nombres


def evidencias_huerfanas_de_la_historia(base, componentes):
    """Evidencias confirmadas en `HEAD` que NINGUNA fila viva declara.

    Devuelve `(lista, motivo_de_no_poder_comprobarlo)`. Falla cerrado: si no hay historia
    se dice, y quien lo juzgue NO puede contarlo como superado.
    """
    confirmadas = evidencias_confirmadas(base)
    if confirmadas is None:
        return [], ("no hay historia `git` en este árbol, de modo que la segunda fuente "
                    "independiente NO se pudo interrogar")
    declaradas = {c.get("evidencia") for c in componentes if c.get("evidencia")}
    return sorted(confirmadas - declaradas), None


def rutas_declaradas_en_head(base):
    """Las rutas que el manifiesto CONFIRMADO en `HEAD` declara. `None` si no hay historia.

    Es la tercera fuente independiente, y existe sólo para una cosa: impedir que la marca
    de exclusión se use para RETIRAR del aparato lo que ya estaba dentro.
    """
    import subprocess                                                 # noqa: PLC0415
    proc = subprocess.run(
        ["git", "-C", base, "show", "HEAD:kernel/operativo/validadores/validadores.yaml"],
        capture_output=True, text=True)
    if proc.returncode != 0:
        return None
    # No se importa el cargador del manifiesto para no depender de él: se leen los tres
    # campos que hacen falta con una lectura literal, que es lo que un juez debe hacer con
    # la versión confirmada de un fichero que quizá el árbol de trabajo ya cambió.
    import re                                                         # noqa: PLC0415
    rutas, script, directorio = set(), None, None
    for linea in proc.stdout.split("\n"):
        if re.match(r"^\s*- id:", linea):
            if script:
                rutas.add(normalizar_ruta(base, directorio, script))
            script, directorio = None, None
            continue
        m = re.match(r"^\s*script:\s*(\S+)", linea)
        if m:
            script = m.group(1)
        m = re.match(r"^\s*dir:\s*(\S+)", linea)
        if m:
            directorio = m.group(1)
    if script:
        rutas.add(normalizar_ruta(base, directorio, script))
    return rutas
