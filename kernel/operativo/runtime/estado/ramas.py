#!/usr/bin/env python3
"""ramas — el estado durable de un control repo, comparado entre DOS referencias Git.

`g.6` fija que una bifurcación se DETECTA y que su resolución no se decide en el motor:
`Almacen.detectar_bifurcacion` compara el linaje de dos ALMACENES vivos y publica la
relación. Lo que ese aparato no cubría —y una instancia real lo sufrió el 2026-09-15— es el
caso más corriente en un repositorio de control gobernado por Git: **dos RAMAS del mismo
repositorio** que, desde un antepasado común, anexan transacciones DISTINTAS al mismo
diario. Ninguna de las dos está corrupta; las dos verifican; cada una es un almacén
perfectamente coherente. Y el primer sitio donde se ve la divergencia es un conflicto de
`git merge` sobre `estado/diario/DIARIO.jsonl` y `estado/REVISION.json`: tarde, sin
vocabulario, y sin decir QUÉ OBJETOS chocan.

Esto lo mide ANTES y sin tocar nada: no abre ningún almacén, no cambia de rama, no escribe
en el árbol de trabajo. Lee `REVISION.json` y el diario de cada referencia como BLOBS de
Git —por el canal único de `gobierno/git.py`—, comprueba que cada diario leído está
encadenado (`previo` y `huella`, §2.4 del contrato), deriva el linaje con LA MISMA REGLA que
el motor (`diario.linaje_de`) y clasifica el par con un vocabulario CERRADO de colisiones:

    SIN INTERFERENCIA     las dos referencias publican la misma revisión
    COMPATIBLE            una es antepasada de la otra: el diario de una es prefijo del de
                          la otra, y Git fusiona sin conflicto de estado
    RIESGO DE CONFLICTO   bifurcadas desde el antepasado común, sin objeto canónico en
                          común: el diario y la revisión chocarán al fusionar aunque los
                          objetos no; hay que RE-APLICAR las transacciones de una sobre la
                          otra, y eso no está automatizado
    CONFLICTO DIRECTO     bifurcadas Y escribieron el mismo objeto canónico: no hay orden de
                          re-aplicación que no pierda una de las dos escrituras sin decidir
    BLOQUEO               no se puede juzgar: una referencia no existe, no hay antepasado
                          común, una referencia no lleva estado durable, su diario no está
                          encadenado, o tiene una ventana de publicación abierta

Igual que `detectar_bifurcacion`, esto **NO RESUELVE**: publica la clase, nombra los objetos
y dice qué habría que hacer. Resolver es autoridad de quien integra, y la instancia lo hace
por su gobierno Git, nunca por un automatismo del motor.

DECISIÓN · se lee del BLOB y no del árbol de trabajo
    Alternativas: (a) `git checkout` de cada referencia en un directorio temporal y abrir
    el almacén con el motor; (b) leer los dos ficheros como blobs y derivar.
    Se elige (b). (a) abriría almacenes ajenos —con su bloqueo de escritor, su recuperación
    automática de `g.8` y su testigo— sobre árboles que no son de nadie, y una recuperación
    disparada por una lectura es exactamente la mutación que una comparación no debe
    causar. (b) no muta nada y no puede: un blob no tiene bloqueo ni ventana que cerrar.

DECISIÓN · la cadena del diario se verifica aunque el almacén de esa rama «verifique»
    Un diario leído como blob no pasa por `Diario.eventos(verificar=True)`. Sin comprobar
    `previo` y `huella` aquí, una rama con un diario manipulado se clasificaría con la
    misma tranquilidad que una sana, y la clase publicada sería falsa. El coste es leer
    los eventos enteros, que es lo que ya hace el motor en cada apertura.

Requisitos que sostiene: OWN-ADS-0226 (§62 de la Directiva aplicado al propio ADS),
OWN-ADS-0223 y OWN-ADS-0224 (colisión clasificada antes de ejecutar).
"""
from __future__ import annotations

import json
import os
import posixpath

from gobierno.git import CanalGit, GitFallo
from .diario import (
    CLAVE_HUELLA, CLAVE_PREVIO, TIPO_INICIALIZADO, TIPOS_QUE_CIERRAN, TIPO_PREPARADA,
    calcular_huella, linaje_de,
)

RUTA_ESTADO = "estado"
FICHERO_REVISION = "REVISION.json"
FICHERO_DIARIO = posixpath.join("diario", "DIARIO.jsonl")

# El vocabulario CERRADO. Ninguna otra palabra vale, y la CLI lo publica tal cual.
SIN_INTERFERENCIA = "SIN INTERFERENCIA"
COMPATIBLE = "COMPATIBLE"
RIESGO_DE_CONFLICTO = "RIESGO DE CONFLICTO"
CONFLICTO_DIRECTO = "CONFLICTO DIRECTO"
BLOQUEO = "BLOQUEO"
CLASES = (SIN_INTERFERENCIA, COMPATIBLE, RIESGO_DE_CONFLICTO, CONFLICTO_DIRECTO, BLOQUEO)

RESOLUCION = "no-se-decide-aqui"


class RamaSinEstado(Exception):
    """Una referencia no lleva estado durable legible: se clasifica BLOQUEO, no se adivina."""


# ---------------------------------------------------------------- lecturas por blob
def _ruta(ruta_estado, fichero):
    return posixpath.join(ruta_estado, fichero)


def revision_en(canal, ref, *, ruta_estado=RUTA_ESTADO):
    """`REVISION.json` de una referencia, o `None` si esa referencia no lo lleva."""
    crudo = canal.contenido_de_blob(ref, _ruta(ruta_estado, FICHERO_REVISION))
    if crudo is None:
        return None
    try:
        revision = json.loads(crudo.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        raise RamaSinEstado("REVISION.json ilegible en `%s`: %s" % (ref, exc))
    for clave in ("revision", "revision_id", "padre", "cid_raiz", "raiz", "diario_secuencia"):
        if clave not in revision:
            raise RamaSinEstado("REVISION.json de `%s` no lleva `%s`" % (ref, clave))
    return revision


def diario_en(canal, ref, *, ruta_estado=RUTA_ESTADO):
    """Los eventos del diario de una referencia, VERIFICADOS en su cadena, o `None`."""
    crudo = canal.contenido_de_blob(ref, _ruta(ruta_estado, FICHERO_DIARIO))
    if crudo is None:
        return None
    eventos = []
    for numero, linea in enumerate(crudo.decode("utf-8").splitlines(), start=1):
        if not linea.strip():
            continue
        try:
            evento = json.loads(linea)
        except ValueError as exc:
            raise RamaSinEstado("diario de `%s`: línea %d ilegible: %s" % (ref, numero, exc))
        if not isinstance(evento, dict):
            raise RamaSinEstado("diario de `%s`: línea %d no es un evento" % (ref, numero))
        eventos.append(evento)
    exigir_encadenado(eventos, ref)
    return eventos


def exigir_encadenado(eventos, ref):
    """`previo` de cada evento es la `huella` del anterior, y cada `huella` es la de su cuerpo.

    Es la comprobación de §2.4 del contrato, hecha sobre eventos leídos de un blob. Un
    diario que no la pasa no clasifica nada: es BLOQUEO con su línea."""
    anterior = None
    for evento in eventos:
        huella = evento.get(CLAVE_HUELLA)
        if huella != calcular_huella(evento):
            raise RamaSinEstado("diario de `%s`: la huella de la secuencia %s no es la de su "
                                "cuerpo" % (ref, evento.get("secuencia")))
        if anterior is not None and evento.get(CLAVE_PREVIO) != anterior.get(CLAVE_HUELLA):
            raise RamaSinEstado("diario de `%s`: la secuencia %s no encadena con la %s"
                                % (ref, evento.get("secuencia"), anterior.get("secuencia")))
        anterior = evento


def ventana_abierta(eventos):
    """Las transacciones con `preparada` y sin cierre, en orden. Vacío = ventana cerrada."""
    por_transaccion = {}
    for evento in eventos:
        transaccion = evento.get("transaccion")
        if transaccion is not None:
            por_transaccion.setdefault(transaccion, []).append(evento)
    abiertas = []
    for transaccion, propios in por_transaccion.items():
        tipos = {e.get("tipo") for e in propios}
        if TIPO_PREPARADA in tipos and not (tipos & set(TIPOS_QUE_CIERRAN)):
            abiertas.append(transaccion)
    return abiertas


def objetos_distintos(raiz_base, raiz):
    """Las rutas canónicas cuyo `cid` difiere entre dos raíces, incluidas altas y bajas."""
    rutas = set(raiz_base) | set(raiz)
    return sorted(r for r in rutas if raiz_base.get(r) != raiz.get(r))


# ---------------------------------------------------------------- la comparación
def _resumen(revision):
    return {
        "revision": revision["revision"],
        "revision_id": revision["revision_id"],
        "cid_raiz": revision["cid_raiz"],
        "diario_secuencia": revision["diario_secuencia"],
    }


def _bloqueo(ref_a, ref_b, motivo, **extra):
    resultado = {
        "ref_a": ref_a, "ref_b": ref_b, "clase": BLOQUEO, "relacion": "no-juzgable",
        "motivo": motivo, "que_hacer": "resolver el motivo antes de comparar; no se fusiona "
                                        "un estado que no se puede juzgar",
        "resolucion": RESOLUCION,
    }
    resultado.update(extra)
    return resultado


def comparar(ruta_control_repo, ref_a, ref_b, *, ruta_estado=RUTA_ESTADO):
    """Clasifica el estado durable de `ref_a` frente al de `ref_b`. No muta nada."""
    canal = CanalGit(ruta_control_repo)
    commits = {}
    for nombre, ref in (("a", ref_a), ("b", ref_b)):
        existe, sha = canal.existe_ref(ref)
        if not existe:
            return _bloqueo(ref_a, ref_b, "la referencia `%s` no existe" % ref)
        commits[nombre] = canal.resolver(ref)
    codigo, salida, _ = canal.ejecutar("merge-base", commits["a"], commits["b"], exigir_exito=False)
    if codigo != 0:
        return _bloqueo(ref_a, ref_b, "sin antepasado común entre `%s` y `%s`" % (ref_a, ref_b),
                        commits=commits)
    commits["base"] = salida.decode("ascii", "strict").strip()

    try:
        revisiones = {}
        diarios = {}
        for nombre in ("a", "b", "base"):
            revisiones[nombre] = revision_en(canal, commits[nombre], ruta_estado=ruta_estado)
            diarios[nombre] = diario_en(canal, commits[nombre], ruta_estado=ruta_estado)
    except (RamaSinEstado, GitFallo) as exc:
        return _bloqueo(ref_a, ref_b, str(exc), commits=commits)

    for nombre, ref in (("a", ref_a), ("b", ref_b)):
        if revisiones[nombre] is None or diarios[nombre] is None:
            return _bloqueo(ref_a, ref_b, "`%s` no lleva estado durable (%s)" % (ref, nombre),
                            commits=commits)
        abiertas = ventana_abierta(diarios[nombre])
        if abiertas:
            return _bloqueo(ref_a, ref_b, "`%s` tiene una ventana de publicación abierta "
                            "(transacción %s): recuperar antes de comparar" % (ref, abiertas[0]),
                            commits=commits, ventana={nombre: abiertas})

    rev_a, rev_b = revisiones["a"], revisiones["b"]
    linaje_a, linaje_b = linaje_de(diarios["a"]), linaje_de(diarios["b"])
    raiz_base = revisiones["base"]["raiz"] if revisiones["base"] is not None else {}
    tocados_a = objetos_distintos(raiz_base, rev_a["raiz"])
    tocados_b = objetos_distintos(raiz_base, rev_b["raiz"])
    comunes = sorted(set(tocados_a) & set(tocados_b))

    if rev_a["revision_id"] == rev_b["revision_id"]:
        clase, relacion = SIN_INTERFERENCIA, "identica"
        que_hacer = "nada: las dos referencias publican la misma revisión del estado"
    elif rev_a["revision_id"] in linaje_b:
        clase, relacion = COMPATIBLE, "b-avanza-sobre-a"
        que_hacer = ("`%s` contiene todo el estado de `%s` y más: fusionar `%s` sobre `%s` no "
                     "toca el diario; al revés, el diario de `%s` es un prefijo" % (ref_b, ref_a, ref_a, ref_b, ref_a))
    elif rev_b["revision_id"] in linaje_a:
        clase, relacion = COMPATIBLE, "a-avanza-sobre-b"
        que_hacer = ("`%s` contiene todo el estado de `%s` y más: fusionar `%s` sobre `%s` no "
                     "toca el diario; al revés, el diario de `%s` es un prefijo" % (ref_a, ref_b, ref_b, ref_a, ref_b))
    elif comunes:
        clase, relacion = CONFLICTO_DIRECTO, "bifurcada"
        que_hacer = ("las dos ramas escribieron %d objeto(s) canónico(s) en común desde el "
                     "antepasado común: decidir cuál prevalece y RE-APLICAR las transacciones "
                     "de una rama sobre la otra por el motor, nunca fusionar el diario a mano"
                     % len(comunes))
    else:
        clase, relacion = RIESGO_DE_CONFLICTO, "bifurcada"
        que_hacer = ("las dos ramas anexaron transacciones distintas desde la secuencia %d sin "
                     "tocar los mismos objetos: `git merge` chocará en el diario y en "
                     "REVISION.json igualmente; RE-APLICAR las transacciones de una rama sobre "
                     "la otra por el motor (no automatizado), y no fusionar el diario a mano"
                     % (revisiones["base"]["diario_secuencia"] if revisiones["base"] else 0))

    return {
        "ref_a": ref_a, "ref_b": ref_b, "commits": commits,
        "clase": clase, "relacion": relacion,
        "estado": {
            "a": _resumen(rev_a), "b": _resumen(rev_b),
            "base": _resumen(revisiones["base"]) if revisiones["base"] is not None else None,
        },
        "objetos": {"a": tocados_a, "b": tocados_b, "comunes": comunes},
        "que_hacer": que_hacer,
        "resolucion": RESOLUCION,
    }


def como_lineas(resultado):
    """La proyección de texto de la CLI: determinista y sin rutas del anfitrión."""
    lineas = [
        "clase        " + resultado["clase"],
        "relacion     " + resultado["relacion"],
        "ref_a        " + resultado["ref_a"],
        "ref_b        " + resultado["ref_b"],
    ]
    if resultado["clase"] == BLOQUEO:
        lineas.append("motivo       " + resultado["motivo"])
    else:
        for nombre in ("a", "b", "base"):
            r = resultado["estado"][nombre]
            lineas.append("%-12s %s" % (nombre, "sin estado" if r is None else
                                         "revision %d · secuencia %d · %s" % (
                                             r["revision"], r["diario_secuencia"], r["revision_id"][:23])))
        lineas.append("objetos_a    %d" % len(resultado["objetos"]["a"]))
        lineas.append("objetos_b    %d" % len(resultado["objetos"]["b"]))
        lineas.append("comunes      %d%s" % (len(resultado["objetos"]["comunes"]),
                                             ("  " + " ".join(resultado["objetos"]["comunes"][:6]))
                                             if resultado["objetos"]["comunes"] else ""))
    lineas.append("que_hacer    " + resultado["que_hacer"])
    lineas.append("resolucion   " + resultado["resolucion"])
    return lineas


__all__ = [
    "CLASES", "SIN_INTERFERENCIA", "COMPATIBLE", "RIESGO_DE_CONFLICTO", "CONFLICTO_DIRECTO",
    "BLOQUEO", "RESOLUCION", "RamaSinEstado", "comparar", "como_lineas", "revision_en",
    "diario_en", "exigir_encadenado", "ventana_abierta", "objetos_distintos",
]

# Este módulo NO es un punto ejecutable: lo invoca `ads_estado.py divergencia`. Un `assert`
# de nivel superior lo convertía en uno para el inventario de `T330` (trabaja al importarse)
# y ponía en rojo T306, T308, T330 y T380 en la CI del kernel (run 35060285337).
