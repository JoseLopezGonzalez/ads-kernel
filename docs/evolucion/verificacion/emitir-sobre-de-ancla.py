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

Y el quinto defecto, `X-01`, no se cierra aquí sino en la batería: este fichero **no estaba
en ningún inventario de integridad**, y con tres líneas de puerta trasera —sin commitear—
producía un sobre idéntico al honesto sobre un corpus corrupto. `G-34` cubre ahora el
instrumental de `docs/evolucion/verificacion/` entero: publicado, enumerado e **idéntico a
`HEAD`**. Las dos mitades se sostienen juntas: el emisor exige el árbol limpio, y la batería
exige que el emisor sea el publicado.

QUÉ NO ES, Y SE DICE
--------------------
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
si las asignaciones declaradas no cuadran con las derivadas, o si un universo no deriva, sale
con código 2 y diagnóstico. Un sobre incompleto es peor que ningún sobre: promete una
garantía que no da.
"""

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
DERIVADOR = "docs/evolucion/verificacion/derivar-universo-obligatorio.py"


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
    cambiar un digest. Lo que la limpieza garantiza es lo otro: que **el emisor y el
    derivador que están corriendo son los publicados**, y no una copia modificada en el
    árbol de trabajo. Ésa es la puerta que `X-01` abrió con tres líneas sin commitear.
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
        tar = subprocess.run(["git", "-C", RAIZ, "archive", commit],
                             capture_output=True)
        if tar.returncode != 0:
            raise NoEmitible("`git archive %s` falló: %s"
                             % (commit[:7], tar.stderr.decode("utf-8", "replace").strip()))
        ex = subprocess.run(["tar", "-x", "-C", tmp], input=tar.stdout,
                            capture_output=True)
        if ex.returncode != 0:
            raise NoEmitible("no se pudo desplegar el árbol de `%s`: %s"
                             % (commit[:7], ex.stderr.decode("utf-8", "replace").strip()))
        deriv = os.path.join(tmp, DERIVADOR)
        if not os.path.isfile(deriv):
            raise NoEmitible("el commit `%s` no contiene `%s`: sin derivador no hay universo "
                             "que anclar" % (commit[:7], DERIVADOR))
        p = subprocess.run([sys.executable, deriv, "--rutas"], capture_output=True,
                           text=True, cwd=tmp)
        if p.returncode != 0:
            raise NoEmitible("el derivador DEL COMMIT `%s` no completó: código %d · %s"
                             % (commit[:7], p.returncode, p.stderr.strip()))
        rutas = [r for r in p.stdout.split("\n") if r.strip()]
        if not rutas:
            raise NoEmitible("el derivador de `%s` no devolvió ninguna fuente" % commit[:7])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    filas, lineas, huellas = [], 0, {}
    for rel in sorted(rutas):
        crudo = _blob(commit, rel)
        lineas += crudo.count(b"\n") + (0 if crudo.endswith(b"\n") else 1)
        h = hashlib.sha256(crudo).hexdigest()
        huellas[rel] = h
        filas.append("%s %s" % (rel, h))
    digest = hashlib.sha256("\n".join(filas).encode("utf-8")).hexdigest()
    return digest, len(rutas), lineas, huellas


# ── ASIGNACIONES, DERIVADAS del manifiesto ───────────────────────────────────────
#
# `X-05`. Era el único campo del sobre que nada contrastaba, y era el único falso. Se deriva
# de la columna `revisor` del reparto de LECTURA ÍNTEGRA: cada fila aporta tantas
# asignaciones como revisores nombra, `V+X` cuenta dos. La tabla se localiza por su CABECERA
# —la que tiene una celda `revisor`—, no por el número de sección: los manifiestos no
# numeran igual sus secciones, y un número escrito caduca.
_MARCAS = re.compile(r"^[A-Z][0-9]?$")


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
# de ese commit, `git show` para cada byte.
RECETA = """  C=%s
  d=$(mktemp -d) && git archive "$C" | tar -x -C "$d"
  python3 "$d/%s" --rutas | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\\n"}{printf "%%s",$0}' | sha256sum
  rm -rf "$d\""""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidata", required=True)
    ap.add_argument("--gate", required=True)
    ap.add_argument("--manifiesto", required=True)
    ap.add_argument("--asignaciones", type=int, default=None,
                    help="OPCIONAL. Se DERIVA del manifiesto; si se pasa, tiene que "
                         "coincidir con lo derivado o no se emite sobre")
    ap.add_argument("--emisor", default="coordinador del gate")
    a = ap.parse_args()

    try:
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
        dig_c, nf_c, nl_c, hue_c = universo_de(commit_c)
        dig_g, nf_g, nl_g, hue_g = universo_de(commit_g)
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
    W("  ARBOL DE TRABAJO        LIMPIO · `git status --porcelain` vacío al emitir\n")
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
    W(_f % ("FUENTES OBLIGATORIAS", nf_c, nf_g))
    W(_f % ("LINEAS OBLIGATORIAS", nl_c, nl_g))
    W(_f % ("DIGEST DEL UNIVERSO", dig_c, dig_g))
    W("\n")
    if difieren:
        W("  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: %d\n" % len(difieren))
        for r in difieren:
            W("    %s  %s → %s\n" % (r, hue_c.get(r, "AUSENTE")[:12] or "AUSENTE",
                                     hue_g.get(r, "AUSENTE")[:12] or "AUSENTE"))
    else:
        W("  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: NINGUNA. Los dos digest coinciden y\n")
        W("  el gate no ha tocado el universo después de publicar la candidata\n")
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
    W("  4 LAS RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN, listadas arriba, son la superficie\n")
    W("    exacta en que la candidata y el gate no son el mismo objeto. Todo lo que el\n")
    W("    manifiesto afirme sobre ellas tiene que decir DE QUE ARBOL habla.\n")
    W("  5 SI EL ARBOL DE TRABAJO DE QUIEN EMITIO ESTABA SUCIO NO HAY SOBRE: este emisor se\n")
    W("    niega a emitirlo. Un sobre existente es, por construcción, un sobre limpio.\n")
    W("=" * 78 + "\n")
    W("LO QUE ESTE SOBRE **NO** GARANTIZA, y `O18` lo declara:\n")
    W("  compromiso del canal del Owner · compromiso simultaneo del repositorio y del\n")
    W("  coordinador · robo de credenciales · reescritura autorizada de ramas remotas ·\n")
    W("  manipulacion del ejecutor externo · falsificacion de identidad.\n")
    W("  Esos riesgos son del VERIFICADOR EXTERNO que `O18` contrata para `F6`, y que es\n")
    W("  condicion previa a la adopcion permanente de PesquerApp.\n")
    W("  Y NO ANCLA NINGUNA RESOLUCION DEL OWNER: `X-03`. `docs/owner/` no contiene\n")
    W("  `O15`-`O18`, y mientras no exista esa sede el sobre no puede cubrirlas.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
