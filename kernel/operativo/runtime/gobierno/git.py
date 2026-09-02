#!/usr/bin/env python3
"""git — CANAL ÚNICO de invocación de Git de todo el aparato de `F6`.

Es la ÚNICA sede que ejecuta `git`. Ni el verificador de admisión, ni el control del
gobierno, ni los adaptadores, ni la identidad abren un proceso de Git por su cuenta: todos
pasan por aquí, y el censo derivado de `admision/censo.py` lo comprueba con `ast`.

LO QUE ESTE CANAL PROHÍBE, y no admite excepción:

  · `--force`, `-f`, `--force-with-lease`, `+<refspec>` en `push`, `--hard` en `reset`
  · `update-ref -d` sobre una ref PROTEGIDA
  · toda actualización de ref que no vaya por COMPARACIÓN E INTERCAMBIO

DECISIÓN · la actualización de ref va SIEMPRE por compare-and-swap, y `--force-with-lease`
           NO es un sustituto
    Alternativas: (a) `git push --force-with-lease`; (b) `git update-ref <ref> <nuevo>
    <viejo-esperado>`.
    Se elige (b). `--force-with-lease` es una cortesía del cliente: comprueba lo que el
    cliente CREE que era el valor viejo, se puede desactivar con un flag más, y sin
    argumento explícito compara contra el remote-tracking local, que un `git fetch`
    inadvertido acaba de actualizar. `update-ref` con tres argumentos es una comparación e
    intercambio del LADO DEL ALMACÉN de refs: o el valor viejo es exactamente el que se
    declaró, o la transacción de refs se aborta entera. `g.14` dice que forzar está
    prohibido «sin que ninguna política pueda autorizarlo», y una comprobación que el
    llamante puede desactivar no es una prohibición.

DECISIÓN · el entorno de Git se fija ENTERO y no se hereda
    Alternativas: (a) heredar el entorno del proceso; (b) construirlo desde cero.
    Se elige (b). Un `GIT_CONFIG_GLOBAL` de la máquina puede definir `core.quotePath`,
    `diff.renames`, `core.autocrlf` o un `include.path` que cambie el resultado de una
    LECTURA de la que depende un veredicto. Un verificador cuyo veredicto dependa de la
    configuración de quien lo ejecuta no verifica nada, y ésa es justamente la propiedad que
    `g.15` exige que no dependa del árbol ni de su entorno.

DECISIÓN · `core.quotePath=false` y `-z` en toda lista
    Con `quotePath` activo Git devuelve `"kernel/.../SENTENCI\\303\\221A.txt"`, entre comillas
    y con octales, y una ruta no ASCII deja de casar consigo misma. Fue exactamente el
    vector de `S1-01`. Se apaga en el canal, no en cada llamada.
"""
from __future__ import annotations

import os
import subprocess

from .errores import (
    DobleEscritor,
    GitFallo,
    GitInvocacionProhibida,
    HistoriaNoLineal,
    RefProtegida,
    RevisionBaseObsoleta,
)

NULO = "0" * 40

# Banderas que este canal NO invoca nunca. La comprobación es sobre los argumentos ya
# construidos, de modo que da igual quién los componga.
BANDERAS_PROHIBIDAS = (
    "--force", "--force-with-lease", "--force-if-includes", "-f",
    "--hard", "--allow-unrelated-histories", "--no-verify",
)

# Órdenes de Git que producen una LISTA de rutas. Todas EXIGEN `-z`, y el censo lo mide.
ORDENES_DE_LISTA = (
    "ls-tree", "ls-files", "diff", "diff-tree", "diff-index", "status", "diff-files",
)


class CanalGit:
    """La única puerta por la que este aparato habla con Git."""

    def __init__(self, repositorio, *, autor="verificador", correo="verificador@ads.local"):
        self.repositorio = os.path.abspath(repositorio)
        self._autor = autor
        self._correo = correo

    # -- entorno ----------------------------------------------------------
    def entorno(self):
        """Entorno HERMÉTICO: sin configuración de la máquina, sin red, sin prompt."""
        base = {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "HOME": self.repositorio,
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_SYSTEM": os.devnull,
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_ALLOW_PROTOCOL": "file",
            "GIT_ASKPASS": "/bin/false",
            "GIT_AUTHOR_NAME": self._autor,
            "GIT_AUTHOR_EMAIL": self._correo,
            "GIT_COMMITTER_NAME": self._autor,
            "GIT_COMMITTER_EMAIL": self._correo,
            # `I-g3`: fechas fijas. Sin esto, dos ejecuciones del mismo escenario producen
            # commits con SHA distinto y la evidencia deja de ser byte-idéntica.
            "GIT_AUTHOR_DATE": "1136214245 +0000",
            "GIT_COMMITTER_DATE": "1136214245 +0000",
        }
        return base

    # -- invocación -------------------------------------------------------
    def _comprobar(self, argumentos):
        for argumento in argumentos:
            if argumento in BANDERAS_PROHIBIDAS:
                raise GitInvocacionProhibida(
                    "el canal único no invoca Git con `" + argumento + "`: forzar una "
                    "referencia está prohibido por `g.14` y ninguna política lo autoriza"
                )
            if argumento.startswith("+refs/"):
                raise GitInvocacionProhibida(
                    "refspec forzada `" + argumento + "`: el `+` inicial es un forzado"
                )
        if argumentos and argumentos[0] == "push":
            for argumento in argumentos[1:]:
                if argumento.startswith("+"):
                    raise GitInvocacionProhibida(
                        "refspec forzada en `push`: " + argumento
                    )

    def ejecutar(self, *argumentos, entrada=None, exigir_exito=True, entorno_extra=None):
        """Invoca Git y devuelve `(codigo, salida, error)` con las salidas en BYTES.

        Devuelve bytes a propósito: decodificar aquí obligaría a elegir una política de
        errores para todo el aparato, y `V6-02` exige que la decodificación sea ESTRICTA
        justo donde se interpretan rutas. Quien necesite texto decide, y falla cerrado.
        """
        self._comprobar(argumentos)
        orden = ["git", "-c", "core.quotePath=false", "-c", "core.autocrlf=false",
                 "-c", "advice.detachedHead=false", "-C", self.repositorio]
        orden.extend(argumentos)
        entorno = self.entorno()
        if entorno_extra:
            entorno.update(entorno_extra)
        proceso = subprocess.run(
            orden,
            input=entrada,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=entorno,
            check=False,
        )
        if exigir_exito and proceso.returncode != 0:
            lineas = proceso.stderr.decode("utf-8", "replace").strip().splitlines()
            mensaje = ("`git " + " ".join(argumentos[:3]) + "` devolvió "
                       + str(proceso.returncode))
            if lineas:
                mensaje += ": " + lineas[-1]
            raise GitFallo(mensaje)
        return proceso.returncode, proceso.stdout, proceso.stderr

    # -- lecturas puntuales (NO listas: las listas van por `admision/lectura.py`) ----
    def resolver(self, revision):
        _, salida, _ = self.ejecutar("rev-parse", "--verify", str(revision) + "^{commit}")
        return salida.decode("ascii", "strict").strip()

    def existe_ref(self, ref):
        codigo, salida, _ = self.ejecutar(
            "rev-parse", "--verify", "--quiet", ref, exigir_exito=False
        )
        return (codigo == 0, salida.decode("ascii", "replace").strip())

    def es_antecesor(self, viejo, nuevo):
        """¿`viejo` es antecesor de `nuevo`? Es la definición exacta de fast-forward."""
        codigo, _, _ = self.ejecutar(
            "merge-base", "--is-ancestor", viejo, nuevo, exigir_exito=False
        )
        return codigo == 0

    def contenido_de_blob(self, revision, ruta):
        """Bytes de un fichero en una revisión. Bytes, no texto: el contenido puede no serlo."""
        codigo, salida, _ = self.ejecutar(
            "cat-file", "blob", str(revision) + ":" + ruta, exigir_exito=False
        )
        return salida if codigo == 0 else None

    # -- la ÚNICA vía de mutación de una ref ------------------------------
    def actualizar_ref(self, ref, nuevo, viejo_esperado, *, protegidas=()):
        """Comparación e intercambio. `viejo_esperado` es OBLIGATORIO, y `NULO` crea.

        Comprueba fast-forward en el canal ANTES de invocar a Git, además del hook. Las dos
        capas son deliberadas: el hook cubre a quien no pase por aquí, y esta comprobación
        cubre el caso de que el hook no esté instalado todavía.
        """
        if not isinstance(viejo_esperado, str) or len(viejo_esperado) != 40:
            raise GitInvocacionProhibida(
                "toda actualización de ref exige el valor viejo esperado, de 40 caracteres; "
                "sin él la operación sería un forzado con otro nombre"
            )
        if nuevo == NULO:
            raise RefProtegida(
                "el canal único no borra refs con `update-ref`: usa `retirar_rama`",
                ruta=ref,
            )
        if viejo_esperado != NULO and not self.es_antecesor(viejo_esperado, nuevo):
            raise HistoriaNoLineal(
                "la actualización propuesta no es fast-forward: el valor viejo no es "
                "antecesor del nuevo, y `g.14` prohíbe forzar",
                ruta=ref,
            )
        codigo, _, error = self.ejecutar(
            "update-ref", ref, nuevo, viejo_esperado, exigir_exito=False
        )
        if codigo != 0:
            raise _traducir_rechazo_de_ref(error, ref, viejo_esperado)
        return {"ref": ref, "viejo": viejo_esperado, "nuevo": nuevo,
                "modo": "comparacion-e-intercambio"}

    @staticmethod
    def _traducir(error, ref, viejo_esperado):
        return _traducir_rechazo_de_ref(error, ref, viejo_esperado)

    def retirar_rama(self, ref, viejo_esperado, *, protegidas=()):
        """Retira una rama NO protegida. Sobre una protegida levanta `RefProtegida`."""
        if ref in tuple(protegidas):
            raise RefProtegida(
                "esta ref está protegida y no se retira: `g.14` no admite excepción "
                "automática y ninguna política puede autorizarla",
                ruta=ref,
            )
        codigo, _, error = self.ejecutar(
            "update-ref", "-d", ref, viejo_esperado, exigir_exito=False
        )
        if codigo != 0:
            raise _traducir_rechazo_de_ref(error, ref, viejo_esperado)
        return {"ref": ref, "retirada": True, "viejo": viejo_esperado}


# Lo que Git dice cuando OTRO escritor tiene tomada la ref, en sus dos redacciones.
# Es CONTENCIÓN, no avería del disco, y por eso no puede salir como fallo de sistema de
# ficheros: quien lea el error iría a mirar el disco en vez de reintentar.
_CONTENCION = ("cannot lock ref", "unable to lock", "unable to create",
               "reference already exists", "lock file", "ref is at")
_DESAJUSTE = ("but expected", "is at", "cannot lock ref")


def _traducir_rechazo_de_ref(error, ref, viejo_esperado):
    """Traduce el rechazo de Git al error TIPADO que corresponde.

    DECISIÓN · perder la carrera por una ref NO puede aparecer como avería de disco
        Git dice `cannot lock ref 'refs/heads/canonica': Unable to create
        '.../canonica.lock': File exists`, y ese texto, propagado tal cual, se lee como un
        fallo del sistema de ficheros. Falla cerrado igual, pero engaña a quien lo lee y le
        manda a diagnosticar el disco en vez de a reintentar. Se distinguen tres cosas:

          · el valor viejo declarado ya NO es el vigente   → `RevisionBaseObsoleta`
          · otro escritor tiene la ref tomada              → `DobleEscritor`
          · cualquier otra cosa                            → `GitFallo`, sin adivinar

        El texto original de Git se conserva en el `contexto`, para que el diagnóstico no
        pierda información al ganar precisión.
    """
    detalle = error.decode("utf-8", "replace").strip()
    plano = detalle.lower()
    if "but expected" in plano or "is at" in plano:
        return RevisionBaseObsoleta(
            "la comparación e intercambio sobre la ref falló: el valor viejo declarado ya "
            "no es el vigente, luego otro escritor publicó primero",
            ruta=ref, esperado=viejo_esperado[:12], git=detalle,
        )
    if any(marca in plano for marca in _CONTENCION):
        return DobleEscritor(
            "otro escritor tiene tomada esta ref: la operación se serializa y NO se pisa. "
            "Es contención, no una avería del sistema de ficheros",
            ruta=ref, git=detalle,
        )
    return GitFallo(
        "la operación sobre la ref fue rechazada: " + detalle, ruta=ref
    )


# ===========================================================================
#  El HOOK `reference-transaction` · la mitad IMPOSIBLE de `G-A8`
# ===========================================================================
#  Git ejecuta este hook con la fase (`prepared` / `committed` / `aborted`) como argumento
#  y con las líneas `<viejo> <nuevo> <ref>` por la entrada estándar. Si el hook sale con
#  código distinto de cero en la fase `prepared`, Git ABORTA LA TRANSACCIÓN DE REFS ENTERA.
#  Ahí es donde vive la imposibilidad: no depende de qué flags use el cliente, ni de si
#  pasa por el canal de este módulo, ni de si viene por `push` o por `update-ref`.
#
#  Se escribe en `sh` y no en Python a propósito: el hook tiene que funcionar aunque quien
#  mueva la ref no sea este aparato, y `sh` y `git` es lo único que se puede dar por
#  presente en el repositorio.

CONTENIDO_DEL_HOOK = """#!/bin/sh
# reference-transaction — gobierno Git del control repo (`g.14`, `G-A8`).
# GENERADO por `gobierno/git.py`. No se edita a mano: `comprobar_hook()` mide su digest.
#
# Rechaza, en la fase `prepared` y por tanto ABORTANDO la transaccion entera:
#   · el borrado de una ref protegida, se declare o no el valor viejo
#   · toda actualizacion que no sea fast-forward, SE DECLARE O NO EL VALOR VIEJO
set -eu
fase="${1:-}"
[ "$fase" = "prepared" ] || exit 0
nulo="0000000000000000000000000000000000000000"
while read -r viejo nuevo ref; do
    case "$ref" in
        refs/heads/canonica|refs/heads/main|refs/heads/master)
            protegida="si" ;;
        *)
            protegida="no" ;;
    esac
    if [ "$nuevo" = "$nulo" ]; then
        if [ "$protegida" = "si" ]; then
            echo "gobierno: BORRADO de una ref protegida rechazado: $ref" >&2
            exit 1
        fi
        continue
    fi
    # EL OID NULO EN `viejo` NO SIGNIFICA «CREACION».
    # Git lo pasa tambien cuando el llamador NO DECLARA valor viejo, que es el caso POR
    # DEFECTO de `git update-ref <ref> <nuevo>` y de `git update-ref --stdin`. Tratarlo
    # como creacion dejaba pasar CUALQUIER forzado con solo omitir un argumento: la mitad
    # IMPOSIBLE de `G-A8` se saltaba escribiendo tres palabras en vez de cuatro.
    # Aqui se RESUELVE la ref y se juzga contra su valor REAL. Si la ref no existe, es una
    # creacion de verdad y pasa; si existe, se juzga como cualquier otra actualizacion.
    actual="$viejo"
    if [ "$viejo" = "$nulo" ]; then
        actual=$(git rev-parse --verify --quiet "$ref^{commit}" 2>/dev/null || echo "$nulo")
    fi
    [ "$actual" = "$nulo" ] && continue
    if ! git merge-base --is-ancestor "$actual" "$nuevo" 2>/dev/null; then
        echo "gobierno: actualizacion NO fast-forward rechazada: $ref" >&2
        echo "gobierno: forzar una referencia del control repo esta prohibido" >&2
        exit 1
    fi
done
exit 0
"""

NOMBRE_DEL_HOOK = "reference-transaction"
