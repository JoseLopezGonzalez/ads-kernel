#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EMISOR DEL SOBRE DE ANCLA DE UN GATE DE F4c
===========================================

Materializa el mecanismo que `O18` adopta —la alternativa (b)— y que `D108` propaga: una
**raíz documental EXTERNA al árbol auditado**.

POR QUÉ EXISTE
--------------
Tres gates consecutivos fallaron por la misma causa, y el segundo la identificó: la batería
vive DENTRO del repositorio que audita y decide si algo está «intacto» comparándolo contra
referencias que TAMBIÉN viven ahí —`HEAD`, la revisión base, `kernel/.upstream-hash` y su
propio README—. **Quien puede escribir el repositorio puede escribir la referencia.** El
propio corpus lo había declarado en §11.4 del documento 11 y lo había dejado abierto.

`O18` no lo cierra con otra comprobación interna —eso «sólo movería la circularidad de
sitio»—: lo cierra **cambiando la raíz de confianza**. El coordinador emite este sobre y lo
entrega **a cada revisor dentro de su encargo**, por un canal que el repositorio no reescribe
y **antes de que el revisor empiece a leer**. El revisor verifica el árbol **contra lo que
recibió**, no contra el árbol.

QUÉ CORRIGIÓ EL TERCER GATE, Y POR QUÉ ESTABA ROTO
--------------------------------------------------
El adjudicador `X` del documento 24 midió cuatro defectos en el sobre que este fichero
emitía, y los tres primeros son del fichero:

  1  `_universo()` leía cada fuente con `io.open(RAIZ/ruta)` — **el directorio de trabajo de
     quien ejecuta**. El digest publicado no correspondía a ningún commit: bastaba un
     fichero sucio para publicarlo distinto, y nadie lo notaba. Ahora **cada byte se lee del
     COMMIT** con `git show <commit>:<ruta>`, y el emisor **se niega a emitir con el árbol
     de trabajo sucio** — un sobre sucio no se emite.
  2  El sobre **yuxtaponía dos árboles**: publicaba el `tree` de la candidata y, a su lado,
     el SHA del derivador, las fuentes, las líneas y el digest del árbol DEL GATE. `X` lo
     midió: candidato 65 fuentes / 53 354 líneas / `9490d6a3…`; gate 67 / 53 772 /
     `19ac2551…`. **Mutuamente insatisfacibles: ningún árbol cumplía los dos.** La causa no
     es un descuido: **el derivador es fila de su propio universo**, y el commit del
     manifiesto lo toca. Ahora el sobre **publica los DOS árboles**, cada uno con su
     derivador, sus fuentes, sus líneas y su digest **derivados de SU commit con SU
     derivador**, y publica además **en qué rutas difieren**. Ningún campo mezcla sedes.
  3  La receta publicada canalizaba `echo … | sha256sum`, que añade un `\\n` final que el
     digest no lleva. Daba `6e2f90f2…` sobre el árbol del que salía `19ac2551…`: **fallaba
     sobre todo árbol, sano o corrupto**. Una regla de parada alimentada por un falso
     positivo universal no es una garantía. La receta de abajo **reproduce el digest byte a
     byte**, y se comprobó ejecutándola.
  4  `ASIGNACIONES` se recibía por CLI y **no se contrastaba contra nada**; era el único
     campo sin contrastar y era el único falso (18 publicado, 17 real). Ahora **se DERIVA**
     de la columna `revisor` del reparto de lectura del manifiesto, leído del commit del
     gate; si además se pasa `--asignaciones`, tiene que coincidir o no hay sobre.

QUÉ AÑADIÓ `O19`, Y POR QUÉ UN SOBRE SIN ELLO NO SE EMITE
---------------------------------------------------------
El adjudicador `X` midió un sexto defecto, `X-03`: **el sobre no anclaba NINGUNA resolución
del Owner**. Anclaba el árbol, el manifiesto y el derivador —el continente— y nada del
contenido normativo que el gate juzga. El Owner lo resolvió en `O19`: ratificó el texto
amplio de `O18`, **trasladó la autoridad canónica de la paráfrasis del coordinador a
`docs/owner/`** —«la omisión está en la transcripción del coordinador, no en mi resolución
original»— y ordenó que el sobre publique la ruta de esa sede, **su SHA-256 leído DEL COMMIT
AUDITADO**, los identificadores, **el digest del texto canónico de cada resolución**, la
relación «`O19` revisa la proyección incompleta de `O18`» y una declaración externa de que
ésa es la resolución ratificada.

El bloque de cada resolución se **DERIVA** de la sede —desde su encabezado `# `Onn`` hasta
el encabezado de nivel 1 siguiente— y se publica con la receta que lo reproduce byte a byte,
igual que los digest de árbol. Ninguna lista de resoluciones se escribe aquí: se publican
**todas** las que la sede contenga, y se EXIGEN al menos `O17`, `O18` y `O19`, que son las
que `O19` nombra. **Si la sede no está en el commit auditado, si falta un identificador
exigido o si un digest no se puede derivar, NO HAY SOBRE.**

Y el quinto defecto, `X-01`, no se cierra aquí sino en la batería: este fichero **no estaba
en ningún inventario de integridad**, y con tres líneas de puerta trasera —sin commitear—
producía un sobre idéntico al honesto sobre un corpus corrupto. `G-34` cubre ahora el
instrumental de `docs/evolucion/verificacion/` entero: publicado, enumerado e **idéntico a
`HEAD`**. Las dos mitades se sostienen juntas: el emisor exige el árbol limpio, y la batería
exige que el emisor sea el publicado.

QUÉ NO ES, Y SE DICE
--------------------
**ANCLAR UNA RAMA EJECUTA CÓDIGO DE ESA RAMA** (`Z-16`): el derivador es fila de su propio
universo, de modo que `universo_de()` ejecuta **el derivador del commit que se ancla** en la
máquina de quien emite. Es necesario y no se puede evitar sin dejar de anclar lo que se
ancla; se declara aquí porque no estaba declarado.

No es un verificador externo. No protege frente al compromiso del canal del Owner, al
compromiso simultáneo del repositorio y del coordinador, al robo de credenciales, a la
reescritura autorizada de ramas remotas, a la manipulación del ejecutor externo ni a la
falsificación de identidad. **Esos riesgos son del verificador externo que `O18` contrata
para `F6`**, y que es condición previa a la adopción permanente de PesquerApp.

Es una garantía **transitoria y explícitamente limitada**, y así la declara `O18`.

USO
---
    python3 docs/evolucion/verificacion/emitir-sobre-de-ancla.py \\
        --candidata <ref-remota> --gate <ref-remota> --manifiesto <ruta>

Imprime el sobre. El coordinador lo COPIA al encargo de cada revisor. **No se publica como
fichero del árbol para que el revisor lo lea de ahí**: si el revisor lo leyera del árbol, el
sobre dejaría de ser externo y no valdría para nada.

FALLA CERRADO
-------------
Si el árbol de trabajo está sucio, si una referencia no resuelve, si el commit no existe, si
el manifiesto no está en el commit que se declara, si el reparto de lectura no se puede leer,
si las asignaciones declaradas no cuadran con las derivadas, si un universo no deriva, **si
la SEDE CANÓNICA del Owner no está en el commit auditado, si un identificador exigido no
aparece en ella o si un digest de resolución no se puede derivar**, sale con código 2 y
diagnóstico. Un sobre incompleto es peor que ningún sobre: promete una
garantía que no da.
"""


# `E-10` · LA PROCEDENCIA DE LOS MÓDULOS, PURGADA ANTES DE NINGÚN `import` PROPIO
#
#  POR QUÉ ESTÁ AQUÍ, Y NO SÓLO EN `kernel/operativo/runtime/`. `H-01` de la auditoría del
#  2026-09-04 midió que `validadores/huella.py` no llevaba este prólogo y que, con un
#  `hashlib` homónimo en `PYTHONPATH`, **un árbol MUTADO producía la huella esperada y
#  `T150` publicaba SUPERADA con `EXIT=0`**. El mismo defecto vive en cualquier ejecutable
#  que decida algo y no purgue: éstos deciden qué universo obligatorio existe y si un gate
#  puede adjudicar, que es tanto o más que una huella.
#
#  DECISIÓN · se purga ANTES de importar nada propio, con lo único que el intérprete ya cargó
#      Purgar después de los `import` normales llega tarde —el homónimo ya está en
#      `sys.modules`— y purgar desde un módulo aparte depende de un `import`, que es
#      exactamente lo que se está protegiendo. `sys` es incorporado y `os` lo carga el
#      arranque, así que los dos vienen de `sys.modules` y no de la ruta. Que `os` sea el
#      bueno se COMPRUEBA, no se supone.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación y
#      convertiría un fallo de entorno en un fallo del aparato. `E-10` nombra dos cosas
#      concretas: `PYTHONPATH` y el `cwd`. Se retiran ésas y el recuento se publica.
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
import datetime
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir, os.pardir, os.pardir))
# `S1-08` · LA FÓRMULA DE LÍNEAS TIENE UNA SOLA SEDE, Y ES EL DERIVADOR.
# Se IMPORTA, no se copia. Si la importación falla, este emisor no puede publicar cifras
# de líneas con una fórmula propia y **no emite**: un sobre cuyas métricas no salgan de la
# sede canónica no vale para lo que el sobre existe.
import importlib.util as _ilu
_spec_der = _ilu.spec_from_file_location(
    "_ads_derivador",
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 "derivar-universo-obligatorio.py"))
_DERIVADOR_MOD = _ilu.module_from_spec(_spec_der)
_spec_der.loader.exec_module(_DERIVADOR_MOD)

DERIVADOR = "docs/evolucion/verificacion/derivar-universo-obligatorio.py"
EMISOR = "docs/evolucion/verificacion/emitir-sobre-de-ancla.py"
# `O19`. La SEDE CANÓNICA de las resoluciones del Owner, y las que `O19` NOMBRA como
# exigidas. No es un censo: es el mínimo que el Owner ordenó anclar. Lo que el sobre
# PUBLICA son todas las que la sede contenga, derivadas de ella.
SEDE_OWNER = "docs/owner/ADS-OWNER-RESOLUCIONES.md"
RESOLUCIONES_EXIGIDAS = ("O17", "O18", "O19")


class NoEmitible(Exception):
    """No se puede emitir un sobre honesto. Mejor ninguno que uno incompleto."""


def _git(*args):
    p = subprocess.run(["git", "-C", RAIZ] + list(args), capture_output=True, text=True)
    if p.returncode != 0:
        raise NoEmitible("`git %s` falló: %s" % (" ".join(args), p.stderr.strip()))
    return p.stdout.strip()


def _arbol_limpio():
    """`X` punto 1: UN SOBRE SUCIO NO SE EMITE.

    Todo lo que el sobre publica se lee de commits, de modo que un fichero sucio ya no puede
    cambiar un digest.

    `Z2-01`≡`Z-11`. AQUÍ DECÍA que la limpieza garantiza «que **el emisor y el derivador que
    están corriendo son los publicados**», y **eso es falso**, por dos motivos que se dicen
    enteros porque los midió un revisor:

      · `git status --porcelain` compara contra el `HEAD` **LOCAL**, que este emisor no
        contrasta contra `commit_c` ni contra `commit_g`: un `HEAD` local distinto del
        commit del gate deja el árbol «limpio» sobre otro código;
      · `git update-index --skip-worktree` vacía la salida con el fichero **modificado en
        disco**, y el emisor imprime «ARBOL DE TRABAJO LIMPIO» junto a su propia cadena
        falsificada.

    Lo que esta guarda garantiza, y es todo lo que garantiza: **que no hay modificaciones
    VISIBLES para `git status` en el momento de emitir**. Lo que sí permite comprobar el
    contraste es el campo que el sobre publica hoy y antes no publicaba: el **SHA-256 del
    EMISOR en los dos commits y el del fichero que ha corrido**. El ataque del
    `--skip-worktree` es de clase `C` —exige control del índice de Git de quien emite— y
    `O18` lo contrata para `F6`; lo que NO era de clase `C` era esta afirmación, y se retira.
    """
    sucio = subprocess.run(["git", "-C", RAIZ, "status", "--porcelain"],
                           capture_output=True, text=True)
    if sucio.returncode != 0:
        raise NoEmitible("`git status --porcelain` no responde (%s): sin saber si el árbol "
                         "está limpio no se puede afirmar que el emisor que corre sea el "
                         "publicado" % sucio.stderr.strip())
    lineas = [l for l in sucio.stdout.split("\n") if l.strip()]
    if lineas:
        raise NoEmitible(
            "EL ÁRBOL DE TRABAJO ESTÁ SUCIO y un sobre sucio NO SE EMITE. `git status "
            "--porcelain` devuelve %d entrada(s): %s. Con el árbol sucio no se puede "
            "afirmar que el emisor ni el derivador que están corriendo sean los que el "
            "commit publica, que es exactamente la puerta que `X-01` abrió con tres líneas "
            "sin commitear. Confírmese o reviértase el árbol, y vuélvase a emitir"
            % (len(lineas), "; ".join(lineas[:10]) + (" …" if len(lineas) > 10 else "")))


def _remota(ref):
    salida = _git("ls-remote", "origin", "refs/heads/" + ref)
    if not salida:
        raise NoEmitible("la referencia remota `%s` NO EXISTE en origin. Un sobre que la "
                         "nombre sería falso" % ref)
    return salida.split("\t")[0]


def _blob(commit, ruta):
    p = subprocess.run(["git", "-C", RAIZ, "show", "%s:%s" % (commit, ruta)],
                       capture_output=True)
    if p.returncode != 0:
        raise NoEmitible("`%s` no existe en el commit `%s`. El sobre no puede declarar la "
                         "huella de algo que no está donde dice" % (ruta, commit[:7]))
    return p.stdout


def _sha256_en(commit, ruta):
    crudo = _blob(commit, ruta)
    return hashlib.sha256(crudo).hexdigest(), crudo.count(b"\n")


# ── el ÁRBOL DE UN COMMIT, materializado SIN atributos ───────────────────────────
#
# `Z2-03`≡`Z-04`. Esto era `git archive <commit> | tar -x`, y **`git archive` HONRA
# `export-ignore`**: un `.gitattributes` confirmado en el propio commit retiraba un dictamen
# nuevo del árbol desplegado, el derivador daba una fuente menos, el sobre publicaba ese
# universo encogido con `rc=0` **y, como la RECETA publicada usaba el mismo camino, el
# digest que el revisor recalculaba COINCIDÍA**. Nada delataba la pérdida. Medido: 72 rutas
# derivando del árbol del commit, 71 pasando por el archive.
#
# El remedio es de RESTA: se deja de usar el camino que lee atributos. `git read-tree` sobre
# un índice temporal FUERA del repositorio y `git checkout-index -a --prefix` materializan
# el árbol del commit **sin honrar `export-ignore`**, no tocan el índice ni el árbol de
# trabajo de quien emite, y la RECETA publicada usa exactamente los mismos dos comandos. No
# hay guarda nueva que añadir: se ha quitado el paso que mentía.
#
# `EE-15`. Aquí se decía además que esos dos comandos «**no consultan `.gitattributes`**», y
# **eso es falso y está medido**: `checkout-index` sí lee atributos —los de conversión,
# `text`/`eol`/`filter`—, y lo que NO honra es `export-ignore`, que es lo único que este
# remedio necesitaba. Se conserva la parte cierta y se retira la generalización.
#
# **Y con ella queda declarada la divergencia estructural que la sostiene:** lo que el
# DERIVADOR ve es el árbol MATERIALIZADO —sujeto a esos filtros de conversión— y lo que el
# DIGEST mide es el BLOB leído con `git show`, que no pasa por ninguno. En este corpus las
# dos cosas coinciden porque no hay ningún atributo de conversión declarado; un
# `.gitattributes` que declarara uno las separaría, y el sobre lo publicaría sin decirlo.
# Queda dicho aquí en vez de presumirse imposible.
def _lineas_de(crudo):
    """Líneas de un blob. **Importada del DERIVADOR**, que es su única sede (`S1-08`)."""
    return _DERIVADOR_MOD.lineas_de_blob(crudo)


def _desplegar(commit, destino):
    """Materializa el árbol de `commit` bajo `destino`, sin honrar `export-ignore`."""
    idx = os.path.join(destino, ".indice-temporal")
    entorno = dict(os.environ, GIT_INDEX_FILE=idx)
    for orden in (["read-tree", commit],
                  ["checkout-index", "-a", "--prefix=%s/" % os.path.join(destino, "t")]):
        p = subprocess.run(["git", "-C", RAIZ] + orden, capture_output=True, env=entorno)
        if p.returncode != 0:
            raise NoEmitible(
                "no se pudo materializar el árbol de `%s` con `git %s`: %s. El despliegue "
                "NO usa `git archive` a propósito: honra `export-ignore` y un "
                "`.gitattributes` del propio commit retiraba fuentes del universo con el "
                "digest cuadrando (`Z-04`)"
                % (commit[:7], orden[0], p.stderr.decode("utf-8", "replace").strip()))
    os.remove(idx)
    return os.path.join(destino, "t")


# ── el universo, DERIVADO DE UN COMMIT y de nada más ─────────────────────────────
#
# `X` punto 1. El árbol se materializa con `git archive` fuera del repositorio, el derivador
# que se ejecuta es **el de ESE commit** —porque el derivador es fila de su propio universo—
# y cada byte del digest se lee con `git show <commit>:<ruta>`. Ni una lectura del directorio
# de trabajo. El resultado depende del commit y de nada más, y por eso es reproducible por
# cualquiera que tenga el commit.
def universo_de(commit):
    """(digest, n_fuentes, n_lineas, {ruta: sha256}) del universo obligatorio de `commit`."""
    tmp = tempfile.mkdtemp(prefix="sobre-de-ancla-")
    try:
        arbol = _desplegar(commit, tmp)
        deriv = os.path.join(arbol, DERIVADOR)
        if not os.path.isfile(deriv):
            raise NoEmitible("el commit `%s` no contiene `%s`: sin derivador no hay universo "
                             "que anclar" % (commit[:7], DERIVADOR))
        p = subprocess.run([sys.executable, deriv, "--rutas"], capture_output=True,
                           text=True, cwd=arbol)
        if p.returncode != 0:
            raise NoEmitible("el derivador DEL COMMIT `%s` no completó: código %d · %s"
                             % (commit[:7], p.returncode, p.stderr.strip()))
        rutas = [r for r in p.stdout.split("\n") if r.strip()]
        if not rutas:
            raise NoEmitible("el derivador de `%s` no devolvió ninguna fuente" % commit[:7])
        # lo que el componente (iv) DEJA FUERA viaja en el sobre. El derivador lo publica
        # hoy también por `--rutas`, que es el camino que se audita: un universo que encoge
        # lo dice, y el revisor lo lee en el ancla y no en una tabla que nadie ejecuta.
        excluidos = [l.rstrip() for l in p.stderr.split("\n") if l.strip()]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # `EE-16`. Esta suma escribía su propia fórmula —`count("\n") + (0 if endswith("\n")
    # else 1)`— y el derivador escribía la suya, con una divergencia REAL en el único caso
    # en que difieren: un fichero VACÍO daba **1** aquí y **0** allí.
    #
    # `S1-08`. El remedio de `EE-16` **escribió una TERCERA copia de la fórmula y dijo «se
    # usa UNA»**: la divergencia quedó cerrada y la afirmación no. Hoy la sede es UNA de
    # verdad — `metricas_de_lineas()` se IMPORTA del derivador, que es quien publica las
    # métricas del universo—, y si esa importación falla el sobre **NO SE EMITE**: un
    # emisor que no puede usar la fórmula canónica no publica cifras con una suya.
    filas, lineas, huellas = [], 0, {}
    for rel in sorted(rutas):
        crudo = _blob(commit, rel)
        lineas += _lineas_de(crudo)
        h = hashlib.sha256(crudo).hexdigest()
        huellas[rel] = h
        filas.append("%s %s" % (rel, h))
    digest = hashlib.sha256("\n".join(filas).encode("utf-8")).hexdigest()
    return digest, len(rutas), lineas, huellas, excluidos


# ── la SEDE CANÓNICA DEL OWNER, DERIVADA DEL COMMIT AUDITADO ─────────────────────
#
# `X-03`, resuelto por `O19`. El bloque canónico de cada resolución va **desde su
# encabezado `# `Onn`` hasta el encabezado de nivel 1 siguiente**, sin recortar ni
# normalizar nada: los bytes tal cual están en el commit. Esa definición es la que reproduce
# el `awk` de la receta, y por eso el revisor puede recalcular cada digest sin ejecutar este
# emisor. La lista de resoluciones **no se escribe**: sale de la sede.
_ENCABEZADO_RES = re.compile(rb"^# `(O\d+)`")


def sede_del_owner(commit, papel):
    """(sha256 del fichero, [(id, digest, líneas)]) de la SEDE CANÓNICA en `commit`."""
    crudo = _blob(commit, SEDE_OWNER)          # falla CERRADO si no está en el commit
    if not crudo.endswith(b"\n"):
        raise NoEmitible(
            "la SEDE CANÓNICA `%s` del %s (`%s`) no termina en salto de línea, y entonces la "
            "receta publicada NO reproduciría el último digest byte a byte: es exactamente "
            "`W-12`, y un sobre cuya receta falla sobre todo árbol no es una garantía"
            % (SEDE_OWNER, papel, commit[:7]))
    lineas = crudo.splitlines(keepends=True)
    cortes = [i for i, l in enumerate(lineas) if l.startswith(b"# ")]
    bloques, orden = {}, []
    for n, i in enumerate(cortes):
        m = _ENCABEZADO_RES.match(lineas[i])
        if not m:
            continue
        ident = m.group(1).decode("ascii")
        fin = cortes[n + 1] if n + 1 < len(cortes) else len(lineas)
        cuerpo = b"".join(lineas[i:fin])
        if ident in bloques:
            raise NoEmitible(
                "la SEDE CANÓNICA del %s (`%s`) declara `%s` DOS VECES: dos bloques con el "
                "mismo identificador son dos textos canónicos, y el sobre no puede publicar "
                "el digest de un texto que no es único" % (papel, commit[:7], ident))
        bloques[ident] = cuerpo
        orden.append(ident)
    if not orden:
        raise NoEmitible(
            "de la SEDE CANÓNICA `%s` del %s (`%s`) NO SE DERIVA NI UN BLOQUE `# `Onn``: sin "
            "texto canónico no hay digest que anclar, y un sobre que anunciara la sede sin "
            "publicar su contenido prometería una garantía que no da"
            % (SEDE_OWNER, papel, commit[:7]))
    faltan = [i for i in RESOLUCIONES_EXIGIDAS if i not in bloques]
    if faltan:
        raise NoEmitible(
            "la SEDE CANÓNICA del %s (`%s`) NO CONTIENE %s. `O19` ordena que el sobre ancle "
            "%s, y un sobre que callara la que falta anclaría un corpus del que el Owner no "
            "responde" % (papel, commit[:7], " ni ".join("`%s`" % f for f in faltan),
                          " · ".join("`%s`" % r for r in RESOLUCIONES_EXIGIDAS)))
    filas = []
    for ident in orden:
        cuerpo = bloques[ident]
        filas.append((ident, hashlib.sha256(cuerpo).hexdigest(), cuerpo.count(b"\n")))
    # `C-20`. La tercera salida son los CUERPOS, y no es un extra: `O19` obliga a que el
    # revisor reciba **el texto de la ratificacion**, no solo su digest. Un digest deja al
    # receptor con la sola opcion de ir a leerlo AL ARBOL QUE SE AUDITA, que es exactamente
    # lo que el sobre existe para no tener que hacer. Se devuelven los bytes del commit.
    return hashlib.sha256(crudo).hexdigest(), filas, bloques


# ── ASIGNACIONES, DERIVADAS del manifiesto ───────────────────────────────────────
#
# `X-05`. Era el único campo del sobre que nada contrastaba, y era el único falso. Se deriva
# de la columna `revisor` del reparto de LECTURA ÍNTEGRA: cada fila aporta tantas
# asignaciones como revisores nombra, `V+X` cuenta dos. La tabla se localiza por su CABECERA
# —la que tiene una celda `revisor`—, no por el número de sección: los manifiestos no
# numeran igual sus secciones, y un número escrito caduca.
#
# La marca admite UNA o DOS letras porque **el alfabeto de una letra se agotó**: los gates de
# `F4c` han consumido de `A` a `Z` entre revisores y adjudicadores, y el adjudicador del
# cuarto gate es `AA`. Aceptar dos letras NO ablanda nada —sigue exigiendo mayúsculas, sigue
# rechazando minúsculas, dígito inicial, espacios y texto libre, y sigue haciendo que el
# emisor se niegue a adivinar a quién se asignó una fuente—: sólo reconoce la continuación
# natural de una serie que se quedó sin símbolos.
_MARCAS = re.compile(r"^[A-Z]{1,2}[0-9]?$")


def _celdas(linea):
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def _limpia(celda):
    return re.sub(r"[`*]", "", celda).strip()


def asignaciones_de(texto_manifiesto, ruta):
    """Nº de asignaciones de lectura DERIVADO del manifiesto. Falla cerrado si no se lee."""
    ls = texto_manifiesto.split("\n")
    cabeceras = [i for i, l in enumerate(ls)
                 if l.startswith("|") and "revisor" in [_limpia(c).lower()
                                                        for c in _celdas(l)]]
    if len(cabeceras) != 1:
        raise NoEmitible(
            "el manifiesto `%s` no tiene EXACTAMENTE UNA tabla con columna `revisor` (tiene "
            "%d): sin ella las ASIGNACIONES no se derivan de nada, y el campo sin contrastar "
            "del sobre fue el único falso del gate anterior (`X-05`)" % (ruta, len(cabeceras)))
    i = cabeceras[0]
    col = [_limpia(c).lower() for c in _celdas(ls[i])].index("revisor")
    total, filas = 0, 0
    for linea in ls[i + 2:]:
        if not linea.startswith("|"):
            break
        celdas = _celdas(linea)
        if len(celdas) <= col:
            raise NoEmitible("el reparto de `%s` trae una fila con menos columnas que su "
                             "cabecera: %r" % (ruta, linea.strip()))
        marcas = [m.strip() for m in _limpia(celdas[col]).split("+") if m.strip()]
        if not marcas:
            raise NoEmitible("el reparto de `%s` trae una fila SIN revisor: %r. Una fuente "
                             "asignada a nadie no la lee nadie" % (ruta, linea.strip()))
        malas = [m for m in marcas if not _MARCAS.match(m)]
        if malas:
            raise NoEmitible("el reparto de `%s` trae marcas de revisor que no lo son: %r. "
                             "El emisor no adivina a quién se asignó una fuente"
                             % (ruta, malas))
        total += len(marcas)
        filas += 1
    if not filas:
        raise NoEmitible("el reparto de `%s` no tiene ni una fila bajo su cabecera: un "
                         "reparto vacío daría ASIGNACIONES 0 y ningún sobre honesto lo dice"
                         % ruta)
    return total, filas


# ── la RECETA, que reproduce el digest byte a byte ──────────────────────────────
#
# `X` punto 3, y `W-12`. La receta anterior canalizaba `echo … | sha256sum`: el `echo` de la
# última fila añade un `\n` que el digest —`"\n".join(filas)`— no lleva. El `awk` de abajo
# emite el separador ANTES de cada fila menos la primera, de modo que la corriente termina
# sin salto, igual que el `join`. `LC_ALL=C` fija la colación de `sort` a la del `sorted()`
# de Python. Y todo se lee del COMMIT: `git archive` para derivar las rutas con el derivador
# de ese commit, `git show` para cada byte. Y el árbol se materializa con `read-tree` +
# `checkout-index` y NO con `git archive`: `git archive` honra `export-ignore` y un
# `.gitattributes` del propio commit retiraba fuentes del universo **con este digest
# cuadrando** (`Z-04`). Los dos comandos son los mismos que ejecuta el emisor.
RECETA = """  C=%s
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/%s" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\\n"}{printf "%%s",$0}' | sha256sum
  rm -rf "$d\""""


# La receta de un bloque de la sede. `awk` enciende la impresión en el encabezado del
# bloque pedido y la apaga en el encabezado de nivel 1 siguiente, que es EXACTAMENTE el
# corte que `sede_del_owner()` aplica sobre los mismos bytes del mismo commit.
RECETA_SEDE = """  git show %s:%s |
    awk '/^# /{p = ($0 ~ /^# `%s`/)} p' | sha256sum"""


# ── el campo 14 · LA IDENTIDAD, que es el ancla de `O18(b)` ──────────────────────
#
# `AA-05`. `O18` dice sin adorno que no hay forma mecánica de comprobar esta identidad, y
# eso sigue siendo verdad: lo único que se puede hacer mecánicamente es **negarse a emitir
# sin ella y negarse a aceptar un ROL en su lugar**, que es lo que el sobre emitido hacía.
# No se comprueba quién es: se comprueba que se haya NOMBRADO a alguien.
_ROLES = ("coordinador", "orquestador", "revisor", "adjudicador", "dictaminador",
          "relevo", "agente", "owner", "ejecutor", "gate")


def _identidad(emisor):
    txt = (emisor or "").strip()
    if not txt:
        raise NoEmitible(
            "el campo 14 —IDENTIDAD DEL EMISOR— viene VACÍO. §11.6 lo declara obligatorio y "
            "dice que **el ancla de `O18(b)` ES ESA IDENTIDAD** mientras no exista `(c)`: un "
            "sobre sin ella no ancla nada")
    plano = re.sub(r"[^a-záéíóúñ ]", " ", txt.lower())
    palabras = [w for w in plano.split() if w]
    if not palabras:
        raise NoEmitible("el campo 14 no contiene ni una palabra: %r" % txt)
    if all(w in _ROLES or len(w) <= 3 or w.isdigit() for w in palabras):
        raise NoEmitible(
            "el campo 14 declara un ROL y no una IDENTIDAD: %r. §11.6 pide «quién lo emite, "
            "NOMBRADO», y «coordinador del gate» no nombra a nadie. El sobre del cuarto gate "
            "publicó `coordinador orquestador del gate 4 de F4c` y `AA` lo midió como el "
            "campo 14 fallando **en el sobre EMITIDO**. Nómbrese a quien lo emite" % txt)
    return txt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidata", required=True)
    ap.add_argument("--gate", required=True)
    ap.add_argument("--manifiesto", required=True)
    ap.add_argument("--asignaciones", type=int, default=None,
                    help="OPCIONAL. Se DERIVA del manifiesto; si se pasa, tiene que "
                         "coincidir con lo derivado o no se emite sobre")
    # `AA-05`. Esto era `default="coordinador del gate"`: texto libre, NO `required`, sin
    # validación **y con un ROL como valor por defecto**. §11.6 campo 14 pide «quién lo
    # emite, NOMBRADO» y dice que «el ancla de (b) ES ESA IDENTIDAD» mientras no exista
    # `(c)`. El sobre emitido publicaba `EMISOR  coordinador orquestador del gate 4 de F4c`
    # —un rol— y **el campo 14 fallaba en el sobre EMITIDO, no sólo en el entregado**.
    # Ahora es OBLIGATORIO, no tiene valor por defecto, y se rechaza lo que es un ROL y no
    # un nombre. Un sobre sin identidad no se emite.
    ap.add_argument("--emisor", required=True,
                    help="OBLIGATORIO. La IDENTIDAD NOMBRADA de quien emite (§11.6, campo "
                         "14). Un ROL no es una identidad y se rechaza")
    a = ap.parse_args()

    try:
        _identidad(a.emisor)
        _arbol_limpio()
        commit_c = _remota(a.candidata)
        arbol_c = _git("rev-parse", commit_c + "^{tree}")
        commit_g = _remota(a.gate)
        arbol_g = _git("rev-parse", commit_g + "^{tree}")
        man_crudo = _blob(commit_g, a.manifiesto)
        sha_man = hashlib.sha256(man_crudo).hexdigest()
        asig, filas_reparto = asignaciones_de(man_crudo.decode("utf-8", "replace"),
                                              a.manifiesto)
        if a.asignaciones is not None and a.asignaciones != asig:
            raise NoEmitible(
                "ASIGNACIONES declaradas %d y DERIVADAS del manifiesto %d (%d filas de "
                "reparto). El sobre no publica un número que su manifiesto no sostenga: "
                "ése fue `X-05`" % (a.asignaciones, asig, filas_reparto))
        sha_der_c, _ = _sha256_en(commit_c, DERIVADOR)
        sha_der_g, _ = _sha256_en(commit_g, DERIVADOR)
        # `Z2-01`≡`Z-11`. El sobre publicaba el SHA del DERIVADOR dos veces y **nunca el
        # suyo propio**, que es lo único con lo que el revisor puede contrastar que el
        # emisor que corrió es el publicado. Se publica, de los DOS commits, y con la orden
        # de contrastarlo contra el fichero que corre.
        sha_emi_c, _ = _sha256_en(commit_c, EMISOR)
        sha_emi_g, _ = _sha256_en(commit_g, EMISOR)
        with open(os.path.abspath(__file__), "rb") as _fh:
            sha_emi_corriendo = hashlib.sha256(_fh.read()).hexdigest()
        dig_c, nf_c, nl_c, hue_c, exc_c = universo_de(commit_c)
        dig_g, nf_g, nl_g, hue_g, exc_g = universo_de(commit_g)
        sede_c, res_c, cuerpos_c = sede_del_owner(commit_c, "COMMIT AUDITADO (candidata)")
        sede_g, res_g, _cuerpos_g = sede_del_owner(commit_g, "commit del gate")
    except NoEmitible as e:
        sys.stderr.write("NO EMITIBLE · %s\n" % e)
        return 2

    difieren = sorted(set(hue_c) ^ set(hue_g)) + \
        sorted(r for r in set(hue_c) & set(hue_g) if hue_c[r] != hue_g[r])
    ahora = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    W = sys.stdout.write
    W("SOBRE DE ANCLA · emitido por el coordinador ANTES de crear a ningún revisor\n")
    W("=" * 78 + "\n")
    W("  REPOSITORIO             %s\n" % _git("remote", "get-url", "origin"))
    W("  ARBOL DE TRABAJO        `git status --porcelain` VACÍO al emitir, y eso es todo lo\n")
    W("                          que prueba: no había modificaciones VISIBLES para `git\n")
    W("                          status`. Ver la obligación 5 y los SHA-256 del emisor\n")
    W("  TODO LO DE ABAJO SE LEE DE COMMITS con `git show <commit>:<ruta>`. Ni un byte\n")
    W("  del directorio de trabajo de quien emite\n")
    W("-" * 78 + "\n")
    W("  REF REMOTA CANDIDATA    refs/heads/%s\n" % a.candidata)
    W("  COMMIT CANDIDATO        %s\n" % commit_c)
    W("  ARBOL CANDIDATO         %s\n" % arbol_c)
    W("  REF REMOTA DEL GATE     refs/heads/%s\n" % a.gate)
    W("  COMMIT DEL GATE         %s\n" % commit_g)
    W("  ARBOL DEL GATE          %s\n" % arbol_g)
    W("  RUTA DEL MANIFIESTO     %s\n" % a.manifiesto)
    W("  SHA-256 DEL MANIFIESTO  %s   (en el commit del gate)\n" % sha_man)
    W("  ASIGNACIONES            %d   DERIVADAS de las %d filas de reparto del manifiesto,\n"
      % (asig, filas_reparto))
    W("                          no recibidas por parámetro\n")
    W("-" * 78 + "\n")
    W("LOS DOS ARBOLES, CADA UNO DERIVADO DE SU PROPIO COMMIT CON SU PROPIO DERIVADOR.\n")
    W("El derivador es FILA DE SU PROPIO UNIVERSO y el commit del gate lo toca: por eso el\n")
    W("sobre publica LOS DOS y no mezcla ni un campo. El gate anterior yuxtapuso el árbol\n")
    W("de la candidata con las cifras del árbol del gate, y eran insatisfacibles.\n")
    W("\n")
    _f = "  %-22s  %-64s  %s\n"
    W(_f % ("", "CANDIDATA", "GATE"))
    W(_f % ("COMMIT", commit_c, commit_g))
    W(_f % ("SHA-256 DEL DERIVADOR", sha_der_c, sha_der_g))
    W(_f % ("SHA-256 DEL EMISOR", sha_emi_c, sha_emi_g))
    W(_f % ("FUENTES OBLIGATORIAS", nf_c, nf_g))
    W(_f % ("LINEAS OBLIGATORIAS", nl_c, nl_g))
    W(_f % ("DIGEST DEL UNIVERSO", dig_c, dig_g))
    W("\n")
    W("\n")
    W("  SHA-256 DEL EMISOR QUE HA CORRIDO ESTE SOBRE: %s\n" % sha_emi_corriendo)
    if sha_emi_corriendo == sha_emi_g:
        W("  COINCIDE con el del commit del gate. El revisor puede rehacer este contraste:\n")
    else:
        W("  **NO COINCIDE** con el del commit del gate (%s). El fichero que ha emitido este\n"
          % sha_emi_g)
        W("  sobre NO es el que el commit del gate publica, y eso se dice aquí en vez de\n")
        W("  callarse. El revisor rehace el contraste:\n")
    W("    git show %s:%s | sha256sum\n" % (commit_g, EMISOR))
    W("\n")
    if difieren:
        W("  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: %d\n" % len(difieren))
        for r in difieren:
            W("    %s  %s → %s\n" % (r, hue_c.get(r, "AUSENTE")[:12] or "AUSENTE",
                                     hue_g.get(r, "AUSENTE")[:12] or "AUSENTE"))
    else:
        W("  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: NINGUNA. Los dos digest coinciden y\n")
        W("  el gate no ha tocado el universo después de publicar la candidata\n")
    W("\n")
    W("LO QUE EL COMPONENTE (iv) DEL DERIVADOR DEJA FUERA DEL UNIVERSO, con su H1, tal como\n")
    W("el derivador de cada commit lo publica. Un universo que encoge lo dice, y lo dice\n")
    W("aqui: un dictamen nuevo cuyo H1 lleve una voz de NO-DICTAMEN sale del universo con\n")
    W("`rc=0`, y el revisor tiene que poder verlo sin ejecutar nada (`Z-08`, `Z-13`).\n")
    for _papel, _exc in (("CANDIDATA", exc_c), ("GATE", exc_g)):
        W("\n  ── %s\n" % _papel)
        for _l in _exc:
            W("  %s\n" % _l)
    W("=" * 78 + "\n")
    W("LA SEDE CANONICA DE LAS RESOLUCIONES DEL OWNER, QUE `O19` ORDENA ANCLAR AQUI.\n")
    W("`O19` traslada la AUTORIDAD CANONICA de la parafrasis del coordinador a esta sede:\n")
    W("el registro de decisiones pasa a ser una PROYECCION DERIVADA de ella. Todo lo de\n")
    W("abajo se lee DEL COMMIT, no del arbol de trabajo de quien emite.\n")
    W("\n")
    W("  RUTA DE LA SEDE         %s\n" % SEDE_OWNER)
    W("  RESOLUCIONES ANCLADAS   %d, DERIVADAS de la sede y no escritas: %s\n"
      % (len(res_c), " · ".join("%s (%d lineas)" % (i, n) for i, _, n in res_c)))
    W("  EXIGIDAS POR `O19`      %s   sin una sola de ellas NO HAY SOBRE\n"
      % " · ".join(RESOLUCIONES_EXIGIDAS))
    W("\n")
    W(_f % ("", "CANDIDATA (COMMIT AUDITADO)", "GATE"))
    W(_f % ("SHA-256 DE LA SEDE", sede_c, sede_g))
    _dig_g = {i: d for i, d, _ in res_g}
    for ident, dig, _nl in res_c:
        W(_f % ("DIGEST DE `%s`" % ident, dig,
                _dig_g.get(ident, "AUSENTE EN EL COMMIT DEL GATE")))
    for ident, dig, _n in res_g:
        if ident not in {i for i, _, _ in res_c}:
            W(_f % ("DIGEST DE `%s`" % ident, "AUSENTE EN EL COMMIT AUDITADO", dig))
    W("\n")
    if sede_c == sede_g:
        W("  LOS DOS COMMITS PUBLICAN LA MISMA SEDE, byte a byte.\n")
    else:
        W("  ATENCION: LA SEDE DIFIERE ENTRE LOS DOS COMMITS. El texto canonico que la\n")
        W("  candidata publica NO es el que publica el arbol del gate, y el revisor tiene\n")
        W("  que decir DE CUAL habla antes de afirmar nada sobre una resolucion del Owner.\n")
    W("\n")
    W("  RELACION ENTRE RESOLUCIONES, dicha por el Owner y no derivada por el emisor:\n")
    W("    `O19` REVISA LA PROYECCION INCOMPLETA DE `O18`. NO revisa su contenido ni su\n")
    W("    diseño: `O18` NO vuelve a someterse a eleccion. La entrada corta de `O18` en el\n")
    W("    registro de decisiones se conserva como REGISTRO HISTORICO de una transcripcion\n")
    W("    incompleta, y la proyeccion ENLAZA a la sede.\n")
    W("\n")
    W("  DECLARACION EXTERNA, que es la razon de que esto viaje en el sobre y no se lea\n")
    W("  del arbol: EL TEXTO ANCLADO ARRIBA ES LA RESOLUCION RATIFICADA POR EL OWNER.\n")
    W("  `O19` ratifica el texto AMPLIO de `O18` —sus tres condiciones obligatorias y su\n")
    W("  reparto— y declara que «la omision esta en la transcripcion del coordinador, no en\n")
    W("  mi resolucion original». A partir de `O19`, lo que una sede derivada rotule como\n")
    W("  literal lo es DE LA SEDE CANONICA, no de la parafrasis.\n")
    W("\n")
    W("  COMO SE RECALCULA CADA DIGEST DE RESOLUCION, sobre el COMMIT AUDITADO:\n")
    for ident, dig, _n in res_c:
        W("\n  ── `%s` → %s\n" % (ident, dig))
        W(RECETA_SEDE % (commit_c, SEDE_OWNER, ident) + "\n")
    W("\n  ── LA SEDE ENTERA → %s\n" % sede_c)
    W("  git show %s:%s | sha256sum\n" % (commit_c, SEDE_OWNER))
    # ── `C-20`, cerrado AQUI y no en `F6` ────────────────────────────────────────
    #
    # `O19` enumera SEIS cosas que cada revisor debe recibir externamente, y la PRIMERA
    # es **el texto de esta ratificacion**. El sobre llevaba las otras cinco —los cinco
    # SHA— y de la primera llevaba un separador y una palabra suelta: 2 de 62 lineas
    # sustantivas, medido por `HH` sobre su propio sobre. Un digest NO es el texto: con
    # solo el digest, el unico camino que le queda al revisor para saber QUE dice `O19`
    # es abrir el arbol que esta auditando, y el sobre existe precisamente para que la
    # raiz de confianza no salga de ahi.
    #
    # Por que aqui y no en `V6-16`/`V6-17`: ninguno de los dos menciona el CONTENIDO del
    # sobre —uno contrata que la prueba corra desde una raiz EXTERNA, el otro que ningun
    # digest calculado por el propio arbol baste—, de modo que `F6` podia cerrarlos los
    # dos en verde con el defecto intacto. Y §11.6 ya le habia puesto fase al emisor:
    # propietario `PLT`, fase «ya, para el PROXIMO gate de `F4c`».
    #
    # La rama alternativa —que `O19` dejara de exigir el texto— NO estaba disponible: esa
    # lista vive dentro de una sede APPEND-ONLY y retirarla es una decision del Owner.
    W("=" * 78 + "\n")
    W("EL TEXTO INTEGRO DE LA RATIFICACION `O19`, TRANSPORTADO MATERIALMENTE EN EL SOBRE.\n")
    W("`O19` exige que cada revisor reciba EXTERNAMENTE seis cosas, y la primera es EL\n")
    W("TEXTO DE LA RATIFICACION. Los cinco SHA van arriba; el texto va aqui, entero y sin\n")
    W("resumir. No es cortesia: con solo el digest, el unico modo de saber que dice `O19`\n")
    W("seria abrir el arbol AUDITADO, que es lo que este sobre existe para no tener que\n")
    W("hacer. Son los bytes del COMMIT AUDITADO `%s`, no los del arbol de trabajo.\n"
      % commit_c[:7])
    W("\n")
    _o19 = cuerpos_c.get(b"O19".decode("ascii"))
    if _o19 is None:                       # inalcanzable: `sede_del_owner` ya lo exige
        W("  ATENCION: `O19` NO ESTA EN LA SEDE DEL COMMIT AUDITADO.\n")
    else:
        _dig_o19 = hashlib.sha256(_o19).hexdigest()
        _txt_o19 = _o19.decode("utf-8")
        W("  DIGEST DEL TEXTO QUE SIGUE   %s\n" % _dig_o19)
        W("  LINEAS TRANSPORTADAS         %d\n" % _o19.count(b"\n"))
        W("  COMO COMPROBAR QUE EL TEXTO ENTREGADO ES EL DE LA SEDE ANCLADA: recorte el\n")
        W("  bloque de abajo entre las dos lineas de guiones, sin la sangria de dos\n")
        W("  espacios que este sobre le añade, y pasele `sha256sum`. Debe dar el digest de\n")
        W("  esta misma linea, que es el mismo `DIGEST DE `O19`` publicado arriba y el que\n")
        W("  reproduce la receta:\n")
        W(RECETA_SEDE % (commit_c, SEDE_OWNER, "O19") + "\n")
        W("  Si el digest del texto entregado NO coincide con el anclado, el sobre miente\n")
        W("  sobre su propia raiz y el gate es INVALIDO: se dice, y no se sigue leyendo.\n")
        W("\n  " + "-" * 76 + "\n")
        for _l in _txt_o19.splitlines():
            W("  %s\n" % _l)
        W("  " + "-" * 76 + "\n")
    W("=" * 78 + "\n")
    W("  EMITIDO                 %s\n" % ahora)
    W("  EMISOR                  %s\n" % a.emisor)
    W("  DECISION QUE LO EXIGE   O18 · alternativa (b) · propagada por D108\n")
    W("  ENTREGA                 este sobre se entrega a cada revisor DENTRO de su encargo\n")
    W("                          y ANTES de que empiece a leer. NO se obtiene leyendo el\n")
    W("                          repositorio que se audita\n")
    W("=" * 78 + "\n")
    W("COMO SE RECALCULA CADA DIGEST, para que el revisor no tenga que fiarse. Reproduce el\n")
    W("digest BYTE A BYTE; si no lo reproduce, el sobre o el árbol están mal, y en ese orden:\n")
    W("\n  ── ARBOL CANDIDATO → %s\n" % dig_c)
    W(RECETA % (commit_c, DERIVADOR) + "\n")
    W("\n  ── ARBOL DEL GATE  → %s\n" % dig_g)
    W(RECETA % (commit_g, DERIVADOR) + "\n")
    W("=" * 78 + "\n")
    W("OBLIGACIONES DEL REVISOR, que son parte del sobre y no cortesía:\n")
    W("  1 RECALCULE LOS DOS DIGEST con la receta de arriba, antes de leer nada. Si uno solo\n")
    W("    no reproduce, el gate es INVALIDO y se dice, sin seguir leyendo.\n")
    W("  2 LEA EL MANIFIESTO EN EL COMMIT DEL GATE, no en el árbol de trabajo, y compruebe\n")
    W("    su SHA-256 contra el de arriba.\n")
    W("  3 CADA FILA DEL MANIFIESTO DECLARA UN ARBOL. Contrástela contra ESE árbol y contra\n")
    W("    ningún otro. La fila del propio derivador es la que el gate anterior falseó dos\n")
    W("    gates seguidos (`U-02`, y su reincidencia `X-06`): mírela primero.\n")
    # `EE-19`. Decía «son la SUPERFICIE EXACTA en que la candidata y el gate no son el
    # mismo objeto», y las rutas listadas son las del UNIVERSO OBLIGATORIO, que es un
    # SUBCONJUNTO PROPIO del árbol: dos commits pueden diferir además en ficheros que el
    # universo no contiene —la evidencia derivada, por ejemplo— y esta lista no los nombra.
    # Prometer «exacta» sobre un subconjunto propio es la sexta condición de `O18` aplicada
    # al propio sobre. Se dice lo que la lista ES, y se publica el comando que da la otra.
    W("  4 LAS RUTAS EN QUE LOS DOS UNIVERSOS OBLIGATORIOS DIFIEREN, listadas arriba, son\n")
    W("    la superficie en que difieren los UNIVERSOS, y NO la superficie en que difieren\n")
    W("    los ARBOLES: los dos commits pueden diferir ademas en ficheros que el universo\n")
    W("    obligatorio no contiene, y esta lista NO los nombra. La otra la da\n")
    W("      git diff --name-only <commit-candidato> <commit-del-gate>\n")
    W("    Todo lo que el manifiesto afirme sobre ellas tiene que decir DE QUE ARBOL habla.\n")
    W("  5 ESTE EMISOR SE NIEGA A EMITIR SI `git status --porcelain` NO VIENE VACIO, y eso\n")
    W("    es TODO lo que esa negativa prueba: que no habia modificaciones VISIBLES para\n")
    W("    `git status` al emitir. NO prueba que el emisor y el derivador que corrieron sean\n")
    W("    los publicados —`git status` compara contra el HEAD LOCAL, y\n")
    W("    `git update-index --skip-worktree` lo vacia con el fichero modificado en disco—.\n")
    W("    LO QUE SI PUEDE COMPROBAR USTED es el SHA-256 DEL EMISOR y el DEL DERIVADOR que\n")
    W("    este sobre publica de los DOS commits: recalculelos con `git show <commit>:<ruta>`\n")
    W("    y contrastelos. `Z-11` midio que la frase anterior —«un sobre existente es, por\n")
    W("    construccion, un sobre limpio»— era falsa, y se retira.\n")
    W("  6 RECALCULE LOS DIGEST DE LA SEDE CANONICA DEL OWNER y contrastelos con toda sede\n")
    W("    derivada que cite una resolucion suya. La AUTORIDAD es la sede; el registro de\n")
    W("    decisiones es una PROYECCION. Una parafrasis que AMPLIE el texto canonico es un\n")
    W("    hallazgo, y `O19` nacio exactamente de uno.\n")
    W("  7 EL TEXTO INTEGRO DE `O19` VIAJA EN ESTE SOBRE, y no es un adorno: `O19` lo pone\n")
    W("    el PRIMERO de las seis cosas que usted debe recibir externamente. Pasele\n")
    W("    `sha256sum` al bloque entregado y contrastelo con el digest publicado a su lado.\n")
    W("    Si no coincide, o si lo que recibio es un resumen en vez del texto, el sobre no\n")
    W("    cumple `O19` y el gate es INVALIDO. Y no lo dé por bueno leyendolo del arbol\n")
    W("    auditado: hacerlo devuelve la raiz de confianza al objeto que usted juzga.\n")
    W("=" * 78 + "\n")
    W("LO QUE ESTE SOBRE **NO** GARANTIZA, y `O18` lo declara:\n")
    W("  compromiso del canal del Owner · compromiso simultaneo del repositorio y del\n")
    W("  coordinador · robo de credenciales · reescritura autorizada de ramas remotas ·\n")
    W("  manipulacion del ejecutor externo · falsificacion de identidad.\n")
    W("  Esos riesgos son del VERIFICADOR EXTERNO que `O18` contrata para `F6`, y que es\n")
    W("  condicion previa a la adopcion permanente de PesquerApp.\n")
    W("  Y LA SEDE CANONICA DEL OWNER NO ES MECANICAMENTE VERIFICABLE CONTRA UNA FUENTE\n")
    W("  EXTERNA AL SISTEMA, y lo declara el propio Owner. `O19` TRASLADA LA AUTORIDAD de\n")
    W("  la parafrasis del coordinador a `docs/owner/` y este sobre publica su huella, pero\n")
    W("  quien pueda escribir el repositorio puede escribir la sede: lo que el sobre prueba\n")
    W("  es que el texto no ha cambiado entre el commit auditado y lo que el revisor\n")
    W("  recibio FUERA del arbol, NO que sea el que el Owner emitio. Es la limitacion que\n")
    W("  `O18` declara de si misma —garantia TRANSITORIA y LIMITADA— y SIGUE VIGENTE hasta\n")
    W("  el verificador externo real de `F6`.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
