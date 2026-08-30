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
    python3 docs/evolucion/verificacion/emitir-sobre-de-ancla.py \
        --candidata <ref-remota> --gate <ref-remota> --manifiesto <ruta>

Imprime el sobre. El coordinador lo COPIA al encargo de cada revisor. **No se publica como
fichero del árbol para que el revisor lo lea de ahí**: si el revisor lo leyera del árbol, el
sobre dejaría de ser externo y no valdría para nada.

FALLA CERRADO
-------------
Si una referencia no resuelve, si el commit no existe, si el manifiesto no está en el commit
que se declara, o si el universo no deriva, sale con código 2 y diagnóstico. Un sobre
incompleto es peor que ningún sobre: promete una garantía que no da.
"""

import argparse
import datetime
import hashlib
import io
import os
import subprocess
import sys

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


def _remota(ref):
    salida = _git("ls-remote", "origin", "refs/heads/" + ref)
    if not salida:
        raise NoEmitible("la referencia remota `%s` NO EXISTE en origin. Un sobre que la "
                         "nombre sería falso" % ref)
    return salida.split("\t")[0]


def _sha256_en(commit, ruta):
    p = subprocess.run(["git", "-C", RAIZ, "show", "%s:%s" % (commit, ruta)],
                       capture_output=True)
    if p.returncode != 0:
        raise NoEmitible("`%s` no existe en el commit `%s`. El sobre no puede declarar la "
                         "huella de algo que no está donde dice" % (ruta, commit[:7]))
    return hashlib.sha256(p.stdout).hexdigest(), p.stdout.count(b"\n")


def _universo():
    """Deriva el universo y devuelve su DIGEST, el número de fuentes y el de líneas.

    El digest se calcula sobre la lista ORDENADA de `ruta SHA-256`, de modo que dos
    universos son el mismo si y sólo si tienen las mismas rutas con el mismo contenido.
    Un revisor lo recalcula ejecutando el derivador y comparándolo contra el sobre.
    """
    p = subprocess.run([sys.executable, os.path.join(RAIZ, DERIVADOR), "--rutas"],
                       capture_output=True, text=True)
    if p.returncode != 0:
        raise NoEmitible("el derivador no completó: código %d · %s"
                         % (p.returncode, p.stderr.strip()))
    rutas = [r for r in p.stdout.split("\n") if r.strip()]
    if not rutas:
        raise NoEmitible("el derivador no devolvió ninguna fuente")
    filas, lineas = [], 0
    for rel in sorted(rutas):
        with io.open(os.path.join(RAIZ, rel), "rb") as fh:
            crudo = fh.read()
        lineas += crudo.count(b"\n") + (0 if crudo.endswith(b"\n") else 1)
        filas.append("%s %s" % (rel, hashlib.sha256(crudo).hexdigest()))
    digest = hashlib.sha256("\n".join(filas).encode("utf-8")).hexdigest()
    return digest, len(rutas), lineas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidata", required=True)
    ap.add_argument("--gate", required=True)
    ap.add_argument("--manifiesto", required=True)
    ap.add_argument("--asignaciones", type=int, required=True)
    ap.add_argument("--emisor", default="coordinador del gate")
    a = ap.parse_args()

    try:
        commit_c = _remota(a.candidata)
        arbol_c = _git("rev-parse", commit_c + "^{tree}")
        commit_g = _remota(a.gate)
        sha_man, lin_man = _sha256_en(commit_g, a.manifiesto)
        sha_der, _ = _sha256_en(commit_g, DERIVADOR)
        digest, n_fuentes, n_lineas = _universo()
    except NoEmitible as e:
        sys.stderr.write("NO EMITIBLE · %s\n" % e)
        return 2

    ahora = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    W = sys.stdout.write
    W("SOBRE DE ANCLA · emitido por el coordinador ANTES de crear a ningún revisor\n")
    W("=" * 78 + "\n")
    W("  REPOSITORIO             %s\n" % _git("remote", "get-url", "origin"))
    W("  REF REMOTA CANDIDATA    refs/heads/%s\n" % a.candidata)
    W("  COMMIT CANDIDATO        %s\n" % commit_c)
    W("  ARBOL (tree SHA)        %s\n" % arbol_c)
    W("  REF REMOTA DEL GATE     refs/heads/%s\n" % a.gate)
    W("  COMMIT DEL MANIFIESTO   %s\n" % commit_g)
    W("  RUTA DEL MANIFIESTO     %s\n" % a.manifiesto)
    W("  SHA-256 DEL MANIFIESTO  %s\n" % sha_man)
    W("  SHA-256 DEL DERIVADOR   %s\n" % sha_der)
    W("  DIGEST DEL UNIVERSO     %s\n" % digest)
    W("  FUENTES OBLIGATORIAS    %d\n" % n_fuentes)
    W("  LINEAS OBLIGATORIAS     %d\n" % n_lineas)
    W("  ASIGNACIONES            %d\n" % a.asignaciones)
    W("  EMITIDO                 %s\n" % ahora)
    W("  EMISOR                  %s\n" % a.emisor)
    W("  DECISION QUE LO EXIGE   O18 · alternativa (b) · propagada por D108\n")
    W("  ENTREGA                 este sobre se entrega a cada revisor DENTRO de su encargo\n")
    W("                          y ANTES de que empiece a leer. NO se obtiene leyendo el\n")
    W("                          repositorio que se audita\n")
    W("=" * 78 + "\n")
    W("COMO SE RECALCULA EL DIGEST DEL UNIVERSO, para que el revisor no tenga que fiarse:\n")
    W("  python3 %s --rutas | sort | while read r; do\n" % DERIVADOR)
    W("      echo \"$r $(sha256sum \"$r\" | cut -d' ' -f1)\"; done | sha256sum\n")
    W("=" * 78 + "\n")
    W("LO QUE ESTE SOBRE **NO** GARANTIZA, y `O18` lo declara:\n")
    W("  compromiso del canal del Owner · compromiso simultaneo del repositorio y del\n")
    W("  coordinador · robo de credenciales · reescritura autorizada de ramas remotas ·\n")
    W("  manipulacion del ejecutor externo · falsificacion de identidad.\n")
    W("  Esos riesgos son del VERIFICADOR EXTERNO que `O18` contrata para `F6`, y que es\n")
    W("  condicion previa a la adopcion permanente de PesquerApp.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
