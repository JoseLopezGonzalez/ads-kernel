#!/usr/bin/env python3
"""lectura — CANAL ÚNICO de lectura de listas de rutas. Corte `V2` · `V6-01` a `V6-04`.

Los cuatro puntos de §20.1 que este módulo cierra, con su criterio literal:

  `V6-01`  toda lectura que produzca una LISTA usa una representación INEQUÍVOCA.
           Cierre: **cero** lecturas de lista con separador contenible en una ruta.
  `V6-02`  separación por `NUL` y decodificación ESTRICTA, o tratamiento byte a byte.
           Cierre: **todas** las lecturas con `-z`; ninguna decodificación laxa.
  `V6-03`  fallo CERRADO ante codificación inválida, truncamiento o estructura inesperada.
           Cierre: los **tres** casos producen ROJO y NOMBRAN la causa.
  `V6-04`  inventario DERIVADO de todas las lecturas; ninguna vía paralela oculta.
           Cierre: el censo se DERIVA del código; **cero** lecturas fuera del canal.
           (lo ejecuta `censo.py`, que analiza este paquete con `ast`)

DECISIÓN · el separador es `NUL` y no el salto de línea, y no es una preferencia
    Un nombre de fichero en Linux puede contener cualquier byte salvo `\\0` y `/`. Luego el
    ÚNICO separador que una ruta no puede contener es `\\0`. Leer con `\\n` no es «menos
    seguro»: es incorrecto, y un fichero llamado `a\\nb.txt` parte la lista en dos rutas que
    no existen mientras la que sí existe desaparece. `_exigir_separador_seguro` lo impide en
    ejecución, y el censo con `ast` lo impide en el código.

DECISIÓN · la decodificación es ESTRICTA, y una ruta indecodificable se DENUNCIA
    Alternativas: (a) `errors="replace"`; (b) `errors="surrogateescape"`; (c) estricta.
    Se elige (c). Con (a) dos rutas distintas se convierten en la misma cadena y el conjunto
    de rutas ENCOGE en silencio: una ruta atacante puede colisionar con una legítima y
    desaparecer del universo. Con (b) el veredicto se calcularía sobre cadenas que no se
    pueden volver a escribir en ninguna evidencia publicable. Con (c) el aparato dice
    exactamente qué byte no pudo leer y en qué registro, que es lo que `V6-02` pide con la
    palabra «DENUNCIA».

DECISIÓN · la salida truncada se detecta por el terminador, no por el tamaño
    Una lista `-z` bien formada termina SIEMPRE en `\\0`. Si no termina en `\\0` y no está
    vacía, faltan bytes: la lectura se cortó. No hace falta saber cuántos deberían venir, y
    por eso la comprobación no depende de ninguna cifra escrita a mano.

DECISIÓN · NO se devuelve nunca lista vacía con éxito ante una salida ilegible
    Es la mitad del criterio de `V6-03` que más falsos verdes ha producido en el expediente:
    una salida que no se entiende y un árbol limpio son indistinguibles si las dos devuelven
    `[]`. Aquí una salida ilegible levanta, y quien la reciba emite ROJO.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gobierno.git import ORDENES_DE_LISTA, CanalGit                  # noqa: E402

from .errores import (                                               # noqa: E402
    EstructuraAjena,
    GitNoResponde,
    LecturaInsegura,
    SalidaNoDecodificable,
    SalidaTruncada,
)

# Las seis letras de `V6-06`, más las dos que Git puede emitir y que aquí NO se ignoran.
LETRAS = ("A", "M", "D", "T", "R", "C")
LETRAS_ADICIONALES = ("U", "X", "B")

# Referencias declaradas de `V6-07`. Cada lectura dice contra qué estado juzga.
REFERENCIAS = ("base", "HEAD", "indice", "trabajo")


def _exigir_separador_seguro(argumentos):
    """`V6-01`: una orden que produce lista SIN `-z` no se ejecuta. Ni una."""
    if not argumentos:
        return
    orden = argumentos[0]
    if orden not in ORDENES_DE_LISTA:
        return
    if "-z" not in argumentos:
        raise LecturaInsegura(
            "`git " + orden + "` produce una LISTA de rutas y se ha pedido sin `-z`. El "
            "único separador que una ruta no puede contener es `NUL`, y sin él una ruta con "
            "un salto de línea parte la lista en dos"
        )


def _registros(salida, orden):
    """Trocea una salida `-z` en registros. Detecta el truncamiento por el TERMINADOR."""
    if not salida:
        return []
    if not salida.endswith(b"\0"):
        raise SalidaTruncada(
            "la salida de `git " + orden + "` no termina en `NUL`: faltan bytes y la "
            "lectura se cortó. No se devuelve una lista parcial",
        )
    return salida[:-1].split(b"\0")


def _decodificar(crudo, orden, indice):
    try:
        return crudo.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise SalidaNoDecodificable(
            "la salida de `git " + orden + "` trae una ruta que no es UTF-8 válido en el "
            "registro " + str(indice) + ", byte " + str(exc.start) + ": se DENUNCIA y no "
            "se interpreta a medias"
        ) from exc


class CanalDeLecturaGit:
    """La ÚNICA vía por la que este aparato obtiene una lista de rutas de Git."""

    def __init__(self, repositorio, *, canal=None):
        self.repositorio = os.path.abspath(repositorio)
        self.canal = canal if canal is not None else CanalGit(self.repositorio)

    # -- primitiva ---------------------------------------------------------
    def _leer(self, *argumentos):
        _exigir_separador_seguro(argumentos)
        codigo, salida, error = self.canal.ejecutar(*argumentos, exigir_exito=False)
        if codigo != 0:
            detalle = error.decode("utf-8", "replace").strip().splitlines()
            raise GitNoResponde(
                "`git " + argumentos[0] + "` devolvió " + str(codigo)
                + (": " + detalle[-1] if detalle else "")
                + ". No se sigue con una lista vacía"
            )
        return salida

    # -- lecturas de LISTA, todas con `-z` --------------------------------
    def rutas_del_arbol(self, revision):
        """Rutas versionadas en una revisión. Referencia declarada: la que se pase."""
        salida = self._leer("ls-tree", "-r", "-z", "--name-only", str(revision))
        crudos = _registros(salida, "ls-tree")
        return [_decodificar(crudo, "ls-tree", indice)
                for indice, crudo in enumerate(crudos) if crudo]

    def rutas_sin_rastrear(self):
        """Ficheros sin rastrear del árbol de trabajo. Referencia declarada: `trabajo`."""
        salida = self._leer("ls-files", "-z", "--others", "--exclude-standard")
        crudos = _registros(salida, "ls-files")
        return [_decodificar(crudo, "ls-files", indice)
                for indice, crudo in enumerate(crudos) if crudo]

    def porcelain(self):
        """`git status --porcelain=v1 -z`. Referencia declarada: `trabajo`."""
        salida = self._leer("status", "--porcelain=v1", "-z", "--untracked-files=all")
        crudos = _registros(salida, "status")
        return [_decodificar(crudo, "status", indice)
                for indice, crudo in enumerate(crudos) if crudo]

    def diferencia(self, *seleccion, referencia):
        """`diff --name-status -z -M -C` sobre la selección, con su referencia DECLARADA.

        Devuelve `[{letra, similitud, ruta, origen, referencia}]`. Las dos puntas de `R` y
        `C` viajan en el MISMO registro: `origen` y `ruta`. Quien las juzgue por separado es
        `mutacion.py`, y lo hace por las dos.
        """
        if referencia not in REFERENCIAS:
            raise EstructuraAjena(
                "referencia no declarada: `" + str(referencia) + "`. `V6-07` exige que "
                "cada comprobación declare contra qué estado juzga"
            )
        # `--find-copies-harder` y no sólo `-C`: sin él Git detecta una copia únicamente
        # cuando el ORIGEN aparece modificado en el mismo diff, de modo que la letra `C` no
        # se produce casi nunca y `V6-06` quedaría sin fixture por una limitación de la
        # lectura y no del juicio. El coste es una lectura más cara sobre un control repo,
        # que es un repositorio pequeño por diseño.
        argumentos = ["diff", "--name-status", "-z", "-M", "-C",
                      "--find-copies-harder", "--no-color"]
        argumentos.extend(seleccion)
        salida = self._leer(*argumentos)
        return self.interpretar_name_status(salida, referencia)

    def interpretar_name_status(self, salida, referencia):
        """Desmonta una salida `--name-status -z`. Estructura ajena → ROJO con la causa."""
        crudos = _registros(salida, "diff")
        filas = []
        indice = 0
        while indice < len(crudos):
            estado_crudo = crudos[indice]
            if not estado_crudo:
                indice += 1
                continue
            estado_texto = _decodificar(estado_crudo, "diff", indice)
            letra = estado_texto[0]
            if letra not in LETRAS + LETRAS_ADICIONALES:
                raise EstructuraAjena(
                    "la salida de `git diff --name-status` trae la letra de mutación `"
                    + letra + "`, que no pertenece al vocabulario de Git. Estructura ajena"
                )
            similitud = estado_texto[1:] or None
            if letra in ("R", "C"):
                if indice + 2 >= len(crudos):
                    raise EstructuraAjena(
                        "un registro `" + letra + "` exige DOS rutas —origen y destino— y "
                        "la salida se acaba antes. Estructura ajena, no lista parcial"
                    )
                origen = _decodificar(crudos[indice + 1], "diff", indice + 1)
                destino = _decodificar(crudos[indice + 2], "diff", indice + 2)
                filas.append({"letra": letra, "similitud": similitud, "ruta": destino,
                              "origen": origen, "referencia": referencia})
                indice += 3
                continue
            if indice + 1 >= len(crudos):
                raise EstructuraAjena(
                    "un registro `" + letra + "` exige una ruta y la salida se acaba antes. "
                    "Estructura ajena, no lista parcial"
                )
            ruta = _decodificar(crudos[indice + 1], "diff", indice + 1)
            filas.append({"letra": letra, "similitud": similitud, "ruta": ruta,
                          "origen": None, "referencia": referencia})
            indice += 2
        return filas

    # -- lecturas que NO son listas ---------------------------------------
    def contenido(self, revision, ruta):
        """Bytes de un blob en una revisión, o `None` si no existe allí."""
        return self.canal.contenido_de_blob(revision, ruta)

    def contenido_en_disco(self, ruta):
        """Bytes de un fichero del árbol de trabajo, o `None`. Cierra SIEMPRE el fichero."""
        destino = os.path.join(self.repositorio, ruta)
        if not os.path.isfile(destino) or os.path.islink(destino):
            return None
        with open(destino, "rb") as manejador:
            return manejador.read()

    def resolver(self, revision):
        return self.canal.resolver(revision)

    def procedencia_de_la_historia(self):
        """`E-09` · ¿es esta copia capaz de responder «cuál fue el commit de NACIMIENTO»?

        `git log --diff-filter=A` siempre devuelve algo en un repositorio SUPERFICIAL o
        INJERTADO: devuelve el primer commit que ESTA COPIA alcanza, que en un clon
        `--depth 1` es el corte de la clonación y no el nacimiento. Se midió en este mismo
        anfitrión: sobre un clon superficial la función devolvía un SHA distinto del real y
        con el contenido ya alterado, con lo que el contraste de `V6-12` se hacía contra la
        alteración y salía verde.

        DECISIÓN · se PREGUNTA a Git, y además se mira el disco
            `git rev-parse --is-shallow-repository` es la respuesta autorizada, y el fichero
            `.git/shallow` es la marca que queda cuando la versión de Git no conoce esa
            opción. Se miran las dos: una comprobación que dependa de una opción moderna
            fallaría abierta en un anfitrión antiguo, y fallar abierto es justo lo que
            `E-09` cierra. `info/grafts` y `refs/replace/` se miran por lo mismo: los dos
            reescriben qué historia se alcanza sin tocar ningún commit.
        """
        codigo, salida, _ = self.canal.ejecutar(
            "rev-parse", "--is-shallow-repository", exigir_exito=False)
        if codigo == 0 and salida.decode("ascii", "replace").strip() == "true":
            return {"completa": False,
                    "motivo": "el repositorio es SUPERFICIAL (`--depth`): el primer commit "
                              "que alcanza no es el nacimiento de nada"}
        directorio = os.path.join(self.repositorio, ".git")
        if os.path.isfile(os.path.join(directorio, "shallow")):
            return {"completa": False,
                    "motivo": "hay `.git/shallow`: la historia está truncada"}
        if os.path.isfile(os.path.join(directorio, "info", "grafts")):
            return {"completa": False,
                    "motivo": "hay `.git/info/grafts`: la historia está INJERTADA y el "
                              "nacimiento que Git recorrería no es el real"}
        codigo, salida, _ = self.canal.ejecutar(
            "for-each-ref", "--format=%(refname)", "refs/replace/", exigir_exito=False)
        if codigo == 0 and salida.decode("utf-8", "replace").strip():
            return {"completa": False,
                    "motivo": "hay refs de `replace`: la historia que Git recorre está "
                              "sustituida y el nacimiento derivado no sería el real"}
        return {"completa": True, "motivo": "historia completa y sin injertos"}

    def commits_de_la_ruta(self, ruta):
        """`O27` §3: TODA la historia de una sede, del nacimiento a `HEAD`, en orden.

        Es lo que permite anclar cada entrada cerrada al commit que la introdujo sin
        escribir ninguna tabla. `--reverse` y no un `sorted()` posterior: el orden lo fija
        Git recorriendo la historia, y ordenar por otra cosa —fecha, por ejemplo— haría que
        una fecha falseada moviera el commit de introducción de una resolución.

        No es una lista de RUTAS, así que no lleva `-z` ni lo necesita: un SHA-1 en
        hexadecimal no puede contener un salto de línea. Se decodifica igualmente en
        ESTRICTO, y una salida que no sea ASCII levanta en vez de interpretarse a medias.
        """
        codigo, salida, error = self.canal.ejecutar(
            "log", "--format=%H", "--reverse", "--", ruta, exigir_exito=False,
        )
        if codigo != 0:
            detalle = error.decode("utf-8", "replace").strip().splitlines()
            raise GitNoResponde(
                "no se pudo derivar la historia de una sede APPEND-ONLY: `git log` "
                "devolvió " + str(codigo) + (": " + detalle[-1] if detalle else "")
                + ". No se sigue con una historia parcial"
            )
        try:
            texto = salida.decode("ascii", "strict")
        except UnicodeDecodeError as exc:
            raise SalidaNoDecodificable(
                "`git log --format=%H` devolvió algo que no es ASCII en el byte "
                + str(exc.start) + ": no es una lista de commits y no se interpreta"
            ) from exc
        return texto.split()

    def commit_de_nacimiento(self, ruta):
        """`V6-12`: el commit que CREÓ una sede. No es `HEAD`, y por eso se busca."""
        codigo, salida, _ = self.canal.ejecutar(
            "log", "--diff-filter=A", "--format=%H", "--reverse", "--", ruta,
            exigir_exito=False,
        )
        if codigo != 0:
            raise GitNoResponde(
                "no se pudo derivar el commit de nacimiento de una sede: `git log` "
                "devolvió " + str(codigo)
            )
        lineas = salida.decode("ascii", "strict").split()
        return lineas[0] if lineas else None
