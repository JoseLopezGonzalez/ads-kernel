#!/usr/bin/env python3
"""composicion_packs — resolución de la precedencia P1 entre packs instalados.

`packs/COMPOSICION.md` fija cuatro reglas de precedencia. La primera —**lo más restrictivo
gana cuando ambos packs hablan de la misma propiedad medible**— no era computable: no había
forma mecánica de saber cuál de dos valores es el más restrictivo, porque eso depende de si
la propiedad es un SUELO o un TECHO, y eso no estaba declarado en ninguna parte.

Aquí se resuelve declarándolo. Cada pack declara sus `propiedades_medibles` con su
`direccion`:

    minimo   el valor es un SUELO exigido   ->  más restrictivo = MAYOR
    maximo   el valor es un TECHO exigido   ->  más restrictivo = MENOR

Y la resolución es una función pura de esas declaraciones: mismo conjunto de packs, mismo
resultado, con independencia del orden en que se pasen.

Uso como biblioteca:
    from composicion_packs import resolver
    resultado = resolver([pack_a, pack_b])          # dicts del bloque ads:pack

Uso desde la línea de órdenes (muestra la resolución de los packs instalados):
    python3 kernel/operativo/validadores/composicion_packs.py [--raiz DIR] [--json]
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-04, sobre `validadores/huella.py` —el
#  instrumento que produce el número que se publica como línea base— y con seis líneas de
#  veneno: un `hashlib.py` homónimo cuyo `sha256()` devuelve siempre el digest esperado.
#
#      $ echo "# CODIGO INYECTADO" >> mutado/kernel/operativo/validadores/ads_lint.py
#      $ cd mutado && python3.12 …/huella.py                     → 8b38fb4f4b07300c
#      $ python3.12 …/comprobar_integridad.py                    → T150 FALLIDA  EXIT=1
#      $ PYTHONPATH=veneno python3.12 …/huella.py                → bc59513f7182130a
#      $ PYTHONPATH=veneno python3.12 …/comprobar_integridad.py  → T150 SUPERADA EXIT=0
#
#  `T150` es la prueba que dice «la huella detecta su edición», y bajo veneno certificaba en
#  VERDE un árbol editado. La causa: la zona `validadores/` estaba ENTERA fuera del
#  inventario de `T306`, de modo que `E-10` —declarado «CERRADO POR INVENTARIO MECÁNICO»—
#  seguía vivo justo en el aparato que produce la evidencia de la certificación.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      Alternativas: (a) importar la purga de un módulo común; (b) copiar el prólogo entero
#      —recital incluido— desde `ads_runtime.py`; (c) copiar el MECANISMO byte a byte y
#      escribir el recital de esta sede.
#      Se elige (c). Con (a) la guardia dependería de un `import`, que es exactamente lo que
#      está protegiendo: una guardia que necesita importar ya ha perdido. Con (b) el recital
#      mentiría, porque el hecho reproducido allí no es el de aquí. Con (c) `T330` exige
#      —y comprueba— que el MECANISMO sea IDÉNTICO byte a byte en todos los puntos
#      ejecutables del árbol (digest `aa219465a6dd6a04`, 1 869 bytes), mientras cada sede
#      dice qué se midió en ella. Lo que protege es el mecanismo; lo que se lee, el recital.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación
#      distinta y convertiría un fallo de entorno en un fallo del aparato. Lo que `E-10`
#      nombra es concreto: `PYTHONPATH` y el `cwd`. Se retiran ésos, se cuenta cuántos, y el
#      recuento queda en `RETIRADAS_DE_LA_RUTA`.
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
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


class ConflictoDeComposicion(Exception):
    """Dos packs hablan de la misma propiedad de forma NO comparable.

    No es un empate que se rompa con una regla: es la condición P4 de
    `packs/COMPOSICION.md`, y su salida legítima es el arbitraje declarado en el PROFILE.
    """


def _mas_restrictivo(direccion, a, b):
    if direccion == "minimo":
        return max(a, b)
    if direccion == "maximo":
        return min(a, b)
    raise ConflictoDeComposicion(f"dirección desconocida: {direccion}")


def resolver(packs):
    """Aplica P1 sobre una lista de bloques ads:pack. Función pura y determinista.

    Devuelve, por propiedad:
      estado    resuelta | unica | pendiente-de-profile
      valor     el que gana, cuando lo hay
      gana      el pack del que procede la restricción vencedora
      motivo    por qué gana, en una frase comprobable
      perdedores  qué valores quedaron descartados y de qué pack venían

    Lanza ConflictoDeComposicion si dos packs declaran la misma propiedad con dirección o
    unidad distintas: no son comparables, y P1 no aplica.
    """
    # orden de entrada irrelevante: se ordena por id de pack antes de nada
    packs = sorted(packs, key=lambda p: p.get("id", ""))

    declaraciones = {}
    for pack in packs:
        for prop in pack.get("propiedades_medibles") or []:
            declaraciones.setdefault(prop["id"], []).append((pack["id"], prop))

    salida = {}
    for pid in sorted(declaraciones):
        entradas = declaraciones[pid]
        direcciones = {p["direccion"] for _, p in entradas}
        unidades = {p["unidad"] for _, p in entradas}
        if len(direcciones) > 1:
            raise ConflictoDeComposicion(
                f"'{pid}': dos packs la declaran con direcciones distintas "
                f"{sorted(direcciones)}. No son comparables: lo arbitra el PROFILE (P4)")
        if len(unidades) > 1:
            raise ConflictoDeComposicion(
                f"'{pid}': dos packs la declaran en unidades distintas {sorted(unidades)}. "
                f"No son comparables: lo arbitra el PROFILE (P4)")

        direccion = entradas[0][1]["direccion"]
        unidad = entradas[0][1]["unidad"]
        con_valor = [(pk, p) for pk, p in entradas if p.get("valor") is not None]

        if not con_valor:
            salida[pid] = {
                "estado": "pendiente-de-profile", "direccion": direccion, "unidad": unidad,
                "declarada_por": sorted(pk for pk, _ in entradas),
                "motivo": "ningún pack puede conocer el umbral: lo fija el PROFILE",
            }
            continue

        ganador_pack, ganador_prop = con_valor[0]
        for pk, p in con_valor[1:]:
            if _mas_restrictivo(direccion, ganador_prop["valor"], p["valor"]) == p["valor"] \
                    and p["valor"] != ganador_prop["valor"]:
                ganador_pack, ganador_prop = pk, p
        perdedores = [{"pack": pk, "valor": p["valor"]}
                      for pk, p in con_valor if pk != ganador_pack]
        comparativo = "el mayor" if direccion == "minimo" else "el menor"
        salida[pid] = {
            "estado": "resuelta" if len(con_valor) > 1 else "unica",
            "direccion": direccion, "unidad": unidad,
            "valor": ganador_prop["valor"], "gana": ganador_pack,
            "motivo": (f"la propiedad es un {'suelo' if direccion == 'minimo' else 'techo'} "
                       f"exigido, luego lo más restrictivo es {comparativo}: "
                       f"{ganador_prop['valor']} {unidad} de {ganador_pack}"),
            "perdedores": sorted(perdedores, key=lambda d: d["pack"]),
        }
    return salida


def cargar_packs(raiz=None):
    from ads_lint import Lint
    base = os.path.abspath(raiz or RAIZ)
    lint = Lint(base, ["packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    return [d for t, d, _, _ in lint.bloques if t == "pack"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    packs = cargar_packs(args.raiz)
    try:
        res = resolver(packs)
    except ConflictoDeComposicion as exc:
        print(f"CONFLICTO: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(f"packs instalados: {', '.join(sorted(p['id'] for p in packs))}\n")
        for pid, d in res.items():
            if d["estado"] == "pendiente-de-profile":
                print(f"{pid:26} PENDIENTE DE PROFILE  ({', '.join(d['declarada_por'])})")
            else:
                perd = " · ".join(f"{x['pack']}={x['valor']}" for x in d["perdedores"]) or "—"
                print(f"{pid:26} {d['valor']} {d['unidad']:8} gana {d['gana']:12} "
                      f"descartados: {perd}")
                print(f"{'':26} {d['motivo']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
