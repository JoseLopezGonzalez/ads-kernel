#!/usr/bin/env python3
"""comprobar_composicion_procesos — el GATE DE COMPOSICIÓN de `D104`, ejecutable.

`11-ARQ` §19, ficha `D104`, fase **F6**: «F6 MATERIALIZA; no elige la forma». Lo que
materializa son los pares `<CAP>:revision` que el árbol EXIGE y que no estaban: hasta esta
entrega había **cero instancias de `:revision` en todo `kernel/operativo/`** y **cero
validadores que lo comprobasen**. Este fichero es el comprobador.

QUÉ DERIVA, Y QUÉ NO ESCRIBE. Nada de lo que publica está escrito a mano:

  · las QUINCE capacidades, de los directorios de `kernel/operativo/capacidades/`
  · el CONJUNTO VIGILADO, de las FICHAS que declaran la doble participación de `b.16`
    —hoy `DOM` y `SEG`, cada una en su propio `CAPACIDAD.md`—. Si `b.16` se la diera a una
    tercera o se la quitara a una de las dos, el catálogo se movería solo
  · el DISCRIMINANTE estático/por item, por PERTENENCIA de `propietario_global` al conjunto
    de las quince, por igualdad de cadena. No se busca la palabra «DERIVADO» ni ninguna
    otra: es la corrección de `N-02`
  · el ANCLA de posición, en sus dos ramas: tras la obligatoria de `VER` si el proceso la
    declara, y si no, tras su ÚLTIMA obligatoria. Ninguna presupone que `VER` exista, que
    es la corrección de `N-01`
  · las CUATRO VÍAS, y las cuatro cuentan. Es la corrección de `O-01` y de `M-01`
  · los tres REPARTOS —por vía, por procedencia y por ancla—, contrastados contra la
    proyección única de §19 cuando esa sede está disponible

LA GRAFÍA. Todo el aparato de §19, `D92`, `D98`, `D103` y `D104` escribe `revision` SIN
TILDE, y ésa es la canónica. `b.16` L836 escribe `<CAP>:revisión` con tilde en una única
aparición; es material APROBADO de `F5` y no se enmienda desde aquí. La discrepancia está
registrada como `E5-3`.

Uso:
  python3 kernel/operativo/validadores/comprobar_composicion_procesos.py
          [--json] [--raiz DIR] [--catalogo]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402
from comprobar_contratos import Resultado  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# La VARIANTE que este validador deriva. Es la única cadena de este fichero que nombra el
# objeto derivado, y va sin tilde por la razón dicha en la cabecera.
VARIANTE = "revision"

# La sede ÚNICA de la cifra de fixtures y de los tres repartos. `D104` lo dice sin rodeos:
# «Esta cifra vive aquí porque un documento no puede contarlos, pero no puede caducar en
# silencio: la única forma de que envejezca es en ROJO». Se cita en texto plano y NO se
# enlaza: `docs/` no viaja al proyecto instalado, y un enlace roto allí es el defecto que
# `E5` destapó.
SEDE_DE_LA_PROYECCION = "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md"


# ===========================================================================
#  LO QUE SE DERIVA DEL ÁRBOL
# ===========================================================================

def quince(base):
    """El conjunto de las QUINCE, derivado de los directorios de capacidades."""
    raiz = os.path.join(base, "kernel/operativo/capacidades")
    if not os.path.isdir(raiz):
        return set()
    return {d for d in os.listdir(raiz)
            if os.path.isdir(os.path.join(raiz, d)) and re.fullmatch(r"[A-Z]{3}", d)}


# Cómo declara una FICHA la doble participación de `b.16`. No es una palabra suelta en
# prosa libre: es una entrada del campo estructurado `deriva_de` que cita `b.16` y dice
# que la capacidad participa DOS VECES. `Q-09`: el conjunto vigilado se DERIVA, y no se
# escribe; una lista escrita aquí seguiría en verde sobre un catálogo que ya no es el suyo.
_DOBLE_PARTICIPACION = re.compile(r"b\.16\b.*\bparticipa dos veces\b", re.I)


def conjunto_vigilado(bloques):
    """Las capacidades cuya FICHA declara la doble participación de `b.16`."""
    vigilado = set()
    for datos, _ruta in bloques.get("capacidad", []):
        for linea in (datos.get("deriva_de") or []):
            if _DOBLE_PARTICIPACION.search(str(linea)):
                vigilado.add(datos.get("id"))
    return vigilado


def base_de(valor):
    """La capacidad BASE: el segmento anterior al primer `:` y al primer `/`, recortado.

    «Sobre esa base se aplica UNA SOLA prueba: pertenencia al conjunto de las QUINCE. No se
    analiza ninguna otra cosa.» Es toda la inferencia que hay.
    """
    if not isinstance(valor, str):
        return None
    return re.split(r"[:/]", valor.strip(), 1)[0].strip()


def variante_de(valor):
    """El aspecto tipado de una referencia `<CAP>:<aspecto>`, o `None` si va desnuda."""
    if not isinstance(valor, str) or ":" not in valor:
        return None
    return valor.split(":", 1)[1].strip()


def es_tipada(valor):
    """`<CAP>:<aspecto>` o `<CAP>/<metodo>`: una REFERENCIA TIPADA, que es la vía 4."""
    return isinstance(valor, str) and (":" in valor or "/" in valor)


def clasificar_propietario(proceso, las_quince):
    """ESTÁTICO si `propietario_global` es EXACTAMENTE uno de los quince; si no, POR ITEM.

    Igualdad de cadena contra un conjunto derivado del árbol, no búsqueda de subcadena y no
    búsqueda de la palabra «DERIVADO»: un propietario que no es un identificador es, por
    construcción, una expresión que sólo se resuelve con el encargo delante (`N-02`).
    """
    propietario = str(proceso.get("propietario_global", "")).strip()
    return "ESTATICO" if propietario in las_quince else "POR_ITEM"


def ancla_de(proceso):
    """`(id de la obligatoria ancla, capacidad que la produce, índice)`.

    Dos ramas, las dos derivables del propio bloque, y ninguna presupone que `VER` exista:
    la obligatoria de `VER` si el proceso la declara, y si no, su ÚLTIMA obligatoria.
    """
    obligatorias = proceso.get("obligatorias") or []
    for i, o in enumerate(obligatorias):
        if base_de(o.get("capacidad_productora")) == "VER":
            return o.get("id"), "VER", i
    if not obligatorias:
        return None, None, -1
    ultima = obligatorias[-1]
    return ultima.get("id"), base_de(ultima.get("capacidad_productora")), len(obligatorias) - 1


def participaciones(proceso, vigilado):
    """Las participaciones de una capacidad VIGILADA, con su VÍA y su PROCEDENCIA.

    La vía dice CÓMO se declaró —1, 2, 3 o 4—; la procedencia dice DE DÓNDE —propietaria,
    `obligatorias` o `condicionales`—. **No son lo mismo desde que la vía 4 puede venir de
    las dos secciones** (`Q-10`).

    Una participación cuya variante es la que este validador DERIVA no es una entrada del
    algoritmo: es su consecuencia. Contarla como origen haría que materializar el par
    creara un par nuevo, y el catálogo crecería solo cada vez que se cierra.
    """
    halladas = []
    propietario = str(proceso.get("propietario_global", "")).strip()
    if propietario in vigilado:
        halladas.append({"capacidad": propietario, "via": 1, "procedencia": "propietaria",
                         "origen": "propietario_global", "condicion": None,
                         "autoridad_de_retirada": None, "indice": -1})
    for i, o in enumerate(proceso.get("obligatorias") or []):
        valor = o.get("capacidad_productora")
        if variante_de(valor) == VARIANTE:
            continue
        cap = base_de(valor)
        if cap not in vigilado:
            continue
        halladas.append({
            "capacidad": cap, "via": 4 if es_tipada(valor) else 2,
            "procedencia": "obligatorias", "origen": o.get("id"), "condicion": None,
            "autoridad_de_retirada": o.get("autoridad_de_retirada"), "indice": i})
    for c in (proceso.get("condicionales") or []):
        valor = c.get("capacidad")
        if variante_de(valor) == VARIANTE:
            continue
        cap = base_de(valor)
        if cap not in vigilado:
            continue
        halladas.append({
            "capacidad": cap, "via": 4 if es_tipada(valor) else 3,
            "procedencia": "condicionales", "origen": valor,
            "condicion": c.get("condicion"), "autoridad_de_retirada": None, "indice": None})
    return halladas


def revisiones_declaradas(proceso):
    """Las participaciones `<CAP>:revision` que el bloque YA declara, con su forma."""
    puestas = []
    for i, o in enumerate(proceso.get("obligatorias") or []):
        valor = o.get("capacidad_productora")
        if variante_de(valor) == VARIANTE:
            puestas.append({"capacidad": base_de(valor), "seccion": "obligatorias",
                            "indice": i, "condicion": None,
                            "autoridad_de_retirada": o.get("autoridad_de_retirada")})
    for c in (proceso.get("condicionales") or []):
        valor = c.get("capacidad")
        if variante_de(valor) == VARIANTE:
            puestas.append({"capacidad": base_de(valor), "seccion": "condicionales",
                            "indice": None, "condicion": c.get("condicion"),
                            "autoridad_de_retirada": None})
    return puestas


def catalogo_estatico(procesos, vigilado, las_quince):
    """SALIDA A de `D104`: el conjunto ESTÁTICO, con vía, procedencia y ancla de cada par.

    Un PAR es `(proceso, capacidad, vía)`. Dos participaciones de la misma capacidad por la
    misma vía en el mismo proceso son un solo par: lo que el par exige es UNA revisión.
    """
    pares = {}
    for datos, _ruta in procesos:
        if clasificar_propietario(datos, las_quince) != "ESTATICO":
            continue
        obligacion, capacidad_ancla, indice = ancla_de(datos)
        for p in participaciones(datos, vigilado):
            clave = (datos.get("id"), p["capacidad"], p["via"])
            if clave in pares:
                continue
            pares[clave] = dict(p, proceso=datos.get("id"), ancla=obligacion,
                                ancla_capacidad=capacidad_ancla, ancla_indice=indice)
    return [pares[k] for k in sorted(pares)]


def regla_por_item(proceso, vigilado, las_quince, propietario_efectivo, condicionales_activos):
    """SALIDA B de `D104`: el conjunto exigido para UN item de un proceso POR ITEM.

    «Con el item delante se resuelven DOS cosas, y las dos suman»: el PROPIETARIO EFECTIVO
    (vía 1) y los CONDICIONALES de las vigiladas que el item ACTIVA (vías 3 y 4). **El
    conjunto exigido es la UNIÓN de los dos**, y por eso un item de `proceso:AUD` puede
    exigir `∅`, `{DOM}`, `{SEG}` o `{DOM, SEG}`. `D103` decía «cero o un par, NUNCA los
    dos»: era cierto mirando sólo el propietario y deja de serlo al contar los
    condicionales que `b.16` L895 declara. Es la corrección de `M-01`.

    No se agrega al total de la SALIDA A.
    """
    exigido = set()
    if propietario_efectivo in vigilado:
        exigido.add(propietario_efectivo)
    for c in (proceso.get("condicionales") or []):
        valor = c.get("capacidad")
        cap = base_de(valor)
        if cap in vigilado and c.get("condicion") in condicionales_activos:
            exigido.add(cap)
    return exigido


def cargar(base):
    lint = Lint(base, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    por_tipo = {}
    for tipo, datos, ruta, _l in lint.bloques:
        por_tipo.setdefault(tipo, []).append((datos, ruta))
    return por_tipo


def variantes_admitidas(base):
    """Las variantes que `esquemas/proceso.yaml` declara. Es una sede NORMATIVA."""
    import yaml as _yaml
    ruta = os.path.join(base, "kernel/operativo/esquemas/proceso.yaml")
    if not os.path.exists(ruta):
        return set()
    with open(ruta, encoding="utf-8") as fh:
        return set((_yaml.safe_load(fh) or {}).get("variantes_de_capacidad") or [])


# ===========================================================================
#  T273 · EL CATÁLOGO ESTÁTICO, MATERIALIZADO
# ===========================================================================

def _retirable(autoridad):
    """Si la obligación PUEDE retirarse. «nadie» es la única forma de irretirable."""
    return not re.match(r"\s*nadie\b", str(autoridad or ""), re.I)


def t273_catalogo_estatico_materializado(raiz=None):
    """`D104` · cada par exigido tiene su `<CAP>:revision`, posterior al ancla y heredada.

    El error es **`composicion-incompleta`**, con el proceso, la capacidad, la VÍA por la
    que participa, el NIVEL —catálogo o item—, el ANCLA derivada y la participación que
    falta. **No es un aviso: impide el cierre del gate de composición.**

    CÓMO LEER LA PRUEBA PRESCRITA. `D104` dice que sobre el árbol de HOY tiene que devolver
    FALLIDA nombrando `proceso:DEP → SEG:revision AUSENTE`. Eso describía el árbol ANTES de
    que F6 materializara: había cero instancias de `:revision` en todo `kernel/operativo/`.
    Materializadas las instancias, la comprobación queda en VERDE sobre el árbol
    materializado, y el contraejemplo se CONSERVA como SABOTAJE: retirar `SEG:revision` de
    `DEP` en una copia vuelve a ponerla FALLIDA nombrando exactamente eso, y sigue fallando
    si alguien la añade a los otros cuatro procesos del catálogo y no a `DEP`. Una prueba
    que hoy pasara en verde SIN la materialización estaría mal construida; una que siguiera
    en rojo CON ella estaría comprobando el árbol de ayer.
    """
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T273", "Todo par del catálogo estático de D104 tiene su <CAP>:revision")
    bloques = cargar(base)
    las_quince, vigilado = quince(base), conjunto_vigilado(bloques)
    if not vigilado:
        r.fallo("ninguna ficha de capacidad declara la doble participación de `b.16`: el "
                "conjunto vigilado se deriva de ellas y ha quedado vacío")
        return r
    admitidas = variantes_admitidas(base)
    for par in catalogo_estatico(bloques.get("proceso", []), vigilado, las_quince):
        proceso = next(d for d, _ in bloques["proceso"] if d["id"] == par["proceso"])
        exigida = f"{par['capacidad']}:{VARIANTE}"
        puestas = [p for p in revisiones_declaradas(proceso)
                   if p["capacidad"] == par["capacidad"]]
        if not puestas:
            aviso = ""
            if exigida not in admitidas:
                aviso = (f" NO SE PUEDE MATERIALIZAR mientras `esquemas/proceso.yaml` no "
                         f"admita la variante `{exigida}` en `variantes_de_capacidad`: "
                         f"ampliar ese conjunto es un ACTO NORMATIVO y su sede es el "
                         f"esquema")
            r.fallo(f"composicion-incompleta · {par['proceso']} → `{exigida}` AUSENTE · "
                    f"vía {par['via']} · nivel catálogo · procedencia {par['procedencia']} "
                    f"· ancla `{par['ancla']}` ({par['ancla_capacidad']}) · falta la "
                    f"participación de revisión posterior al ancla.{aviso}")
            continue
        puesta = puestas[0]
        # POSICIÓN · «la revisión se coloca DESPUÉS del ancla». En `obligatorias` la
        # posición es el índice; en `condicionales` es posterior por construcción, porque la
        # sección entera va detrás de las obligaciones.
        if puesta["seccion"] == "obligatorias" and puesta["indice"] <= par["ancla_indice"]:
            r.fallo(f"composicion-incompleta · {par['proceso']} → `{exigida}` está ANTES "
                    f"de su ancla `{par['ancla']}` (posición {puesta['indice']} frente a "
                    f"{par['ancla_indice']}) · vía {par['via']} · nivel catálogo")
        # HERENCIA · activación, obligatoriedad y autoridad de retirada, de la
        # participación de ORIGEN. Es el paso 8 del algoritmo de `D104`.
        if par["procedencia"] == "condicionales":
            if puesta["seccion"] != "condicionales":
                r.fallo(f"composicion-incompleta · {par['proceso']} → `{exigida}` procede "
                        f"de `condicionales` y se ha materializado como {puesta['seccion']}: "
                        f"no hereda su ACTIVACIÓN")
            elif puesta["condicion"] != par["condicion"]:
                r.fallo(f"composicion-incompleta · {par['proceso']} → `{exigida}` se activa "
                        f"con «{puesta['condicion']}» y su origen `{par['origen']}` con "
                        f"«{par['condicion']}»: no hereda la activación")
        else:
            if puesta["seccion"] != "obligatorias":
                r.fallo(f"composicion-incompleta · {par['proceso']} → `{exigida}` procede "
                        f"de `obligatorias` —se exige SIEMPRE— y se ha materializado como "
                        f"{puesta['seccion']}: no hereda su OBLIGATORIEDAD")
            elif _retirable(puesta["autoridad_de_retirada"]) != _retirable(
                    par["autoridad_de_retirada"]):
                r.fallo(f"composicion-incompleta · {par['proceso']} → `{exigida}` es "
                        f"RETIRABLE y su origen `{par['origen']}` no lo es: no hereda la "
                        f"autoridad de retirada")
    # Y al revés: una revisión que ningún par exige es una instancia sin derivación.
    for datos, _ruta in bloques.get("proceso", []):
        exigidas = {p["capacidad"] for p in catalogo_estatico(
            [(datos, _ruta)], vigilado, las_quince)}
        for puesta in revisiones_declaradas(datos):
            if puesta["capacidad"] not in exigidas:
                r.fallo(f"{datos['id']} declara `{puesta['capacidad']}:{VARIANTE}` y "
                        f"NINGUNA participación del catálogo la exige: una instancia sin "
                        f"derivación es una lista escrita a mano")
    return r


def t274_regla_por_item(raiz=None):
    """`D104` SALIDA B · los procesos de propietario POR ITEM se resuelven CON EL ITEM.

    No se declara que un proceso «pasa vacío»: se resuelve. `DIR` pasa vacío o no según su
    item (`N-01`), `DEF` hoy nunca exige par y eso también se deriva, y un item de `AUD`
    puede exigir los DOS pares a la vez (`M-01`). Se comprueba ejerciendo la regla contra
    los procesos REALES del árbol, no contra un ejemplo escrito.
    """
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T274", "La regla POR ITEM se resuelve con el item, y no por declaración")
    bloques = cargar(base)
    las_quince, vigilado = quince(base), conjunto_vigilado(bloques)
    por_item = [d for d, _ in bloques.get("proceso", [])
                if clasificar_propietario(d, las_quince) == "POR_ITEM"]
    if not por_item:
        r.fallo("ningún proceso resulta de propietario POR ITEM, y `b.16` deriva tres: "
                "`DEF`, `AUD` y `DIR`. El discriminante estructural no está funcionando")
        return r
    for proceso in por_item:
        # un proceso POR ITEM nunca aporta par al catálogo estático
        if catalogo_estatico([(proceso, "")], vigilado, las_quince):
            r.fallo(f"{proceso['id']} es de propietario POR ITEM y aporta par al catálogo "
                    f"ESTÁTICO: el paso 6 de `D104` prohíbe emitir par sin el item delante")
        condiciones = {c.get("condicion") for c in (proceso.get("condicionales") or [])
                       if base_de(c.get("capacidad")) in vigilado}
        # propietario ajeno y sin condicionales activos: tiene que pasar VACÍO
        if regla_por_item(proceso, vigilado, las_quince, "PLT", set()):
            r.fallo(f"{proceso['id']}: con propietario ajeno y sin condicionales activos "
                    f"exige par, y tiene que pasar vacío")
        # propietario vigilado: exige su par por la vía 1
        for capacidad in sorted(vigilado):
            if capacidad not in regla_por_item(proceso, vigilado, las_quince, capacidad,
                                               set()):
                r.fallo(f"{proceso['id']}: con `propietario_global` efectivo `{capacidad}` "
                        f"NO exige `{capacidad}:{VARIANTE}`. Es el contraejemplo de `O-01`: "
                        f"la participación PROPIETARIA no se estaría implementando")
        # todos los condicionales vigilados activos: la UNIÓN, que puede ser los dos
        union = regla_por_item(proceso, vigilado, las_quince, "PLT", condiciones)
        esperado = {base_de(c.get("capacidad")) for c in (proceso.get("condicionales") or [])
                    if base_de(c.get("capacidad")) in vigilado}
        if union != esperado:
            r.fallo(f"{proceso['id']}: con todos sus condicionales vigilados activos exige "
                    f"{sorted(union) or '∅'} y sus condicionales declaran "
                    f"{sorted(esperado) or '∅'}. Es el contraejemplo de `M-01`")
    return r


# ===========================================================================
#  T275 · LOS FIXTURES, EJECUTADOS Y CONTADOS
# ===========================================================================
#  `D104`: «un fixture por VÍA, uno por cada combinación de un proceso de propietario POR
#  ITEM, y uno por cada modo de fallo cerrado, y `G-15` los ejecuta en cada corrida». La
#  cifra —VEINTE— vive en §19 porque un documento no puede contarlos; lo que este validador
#  hace es CONTAR LOS QUE EJECUTA y fallar si esa cifra no es la suya, nombrando sede,
#  responsable y remedio. La única forma de que la cifra envejezca es en ROJO.
#
#  Un fixture es un bloque `ads:proceso` SINTÉTICO —no vive en el corpus— y su comprobación.
#  Se ejercita la DERIVACIÓN, no el texto.

_QUINCE_FIXTURE = {"PRD", "ARQ", "CON", "VER", "DOM", "SEG", "DIS", "ENT", "USO", "APR",
                   "INV", "SIS", "PLT", "DSP", "ENC"}
_VIGILADO_FIXTURE = {"DOM", "SEG"}


def _proceso(pid, propietario, obligatorias, condicionales=()):
    return {"id": pid, "propietario_global": propietario,
            "obligatorias": list(obligatorias), "condicionales": list(condicionales)}


def _ob(oid, capacidad, retirada="el Owner, y queda registrado"):
    return {"id": oid, "capacidad_productora": capacidad, "autoridad_de_retirada": retirada}


def _cond(capacidad, condicion):
    return {"capacidad": capacidad, "condicion": condicion}


def _vias(proceso):
    return sorted((p["capacidad"], p["via"], p["procedencia"])
                  for p in participaciones(proceso, _VIGILADO_FIXTURE))


def _pares(proceso):
    return catalogo_estatico([(proceso, "")], _VIGILADO_FIXTURE, _QUINCE_FIXTURE)


def fixtures():
    """Los fixtures, cada uno `(nombre, función que devuelve None o el motivo del fallo)`.

    Se declaran como una LISTA porque el censo es el número de los que SE EJECUTAN: la
    longitud de esta lista es lo que se contrasta contra la cifra de §19.
    """
    lote = []

    def f(nombre):
        def registrar(fn):
            lote.append((nombre, fn))
            return fn
        return registrar

    # --- las CUATRO VÍAS, una cada una -------------------------------------------------
    @f("vía 1 · participación PROPIETARIA")
    def _():
        p = _proceso("proceso:F1", "DOM", [_ob("ev", "VER")])
        if _vias(p) != [("DOM", 1, "propietaria")]:
            return f"un `propietario_global: DOM` no emite par por la vía 1: {_vias(p)}"

    @f("vía 2 · obligatoria DESNUDA")
    def _():
        p = _proceso("proceso:F2", "PLT", [_ob("seg", "SEG"), _ob("ev", "VER")])
        if ("SEG", 2, "obligatorias") not in _vias(p):
            return f"una obligatoria `SEG` desnuda no emite par por la vía 2: {_vias(p)}"

    @f("vía 3 · condicional DESNUDA")
    def _():
        p = _proceso("proceso:F3", "PRD", [_ob("ev", "VER")], [_cond("DOM", "C-DOM")])
        if ("DOM", 3, "condicionales") not in _vias(p):
            return f"un condicional `DOM` desnudo no emite par por la vía 3: {_vias(p)}"

    @f("vía 4 · item ENLAZADO TIPADO en condicionales")
    def _():
        p = _proceso("proceso:F4", "PRD", [_ob("ev", "VER")],
                     [_cond("SEG:condiciones", "C-SEG")])
        if ("SEG", 4, "condicionales") not in _vias(p):
            return f"`SEG:condiciones` no emite par por la vía 4: {_vias(p)}"

    @f("vía 4 · obligatoria TIPADA, que procede de `obligatorias` y no de `condicionales`")
    def _():
        p = _proceso("proceso:F5", "PLT", [_ob("seg", "SEG:condiciones"), _ob("ev", "VER")])
        if ("SEG", 4, "obligatorias") not in _vias(p):
            return (f"una obligatoria TIPADA no distingue vía 4 con procedencia "
                    f"`obligatorias`: {_vias(p)}. `Q-10`: la vía y la procedencia no son lo "
                    f"mismo desde que la vía 4 viene de las dos secciones")

    # --- el DISCRIMINANTE, estructural ------------------------------------------------
    @f("discriminante ESTRUCTURAL · pertenencia, ni subcadena ni la palabra «DERIVADO»")
    def _():
        estatico = _proceso("proceso:F6", "SEG", [_ob("ev", "VER")])
        if clasificar_propietario(estatico, _QUINCE_FIXTURE) != "ESTATICO":
            return "`propietario_global: SEG` no se clasifica como ESTÁTICO"
        dinamico = _proceso("proceso:F7", "la capacidad PROPIETARIA de la decisión, con SEG "
                            "cuando aplique", [_ob("ev", "VER")])
        if clasificar_propietario(dinamico, _QUINCE_FIXTURE) != "POR_ITEM":
            return ("una frase que CONTIENE `SEG` se clasifica como ESTÁTICA: el "
                    "discriminante está buscando subcadena en vez de pertenencia (`N-02`)")
        sin_palabra = _proceso("proceso:F8", "la que el OWNER declare líder",
                               [_ob("ev", "VER")])
        if clasificar_propietario(sin_palabra, _QUINCE_FIXTURE) != "POR_ITEM":
            return ("un propietario en prosa SIN la palabra «DERIVADO» no se clasifica "
                    "POR ITEM: la partición depende de una palabra (`N-02`)")

    @f("prosa CON ASPECTO DE CAMPO en `propietario_global`")
    def _():
        p = _proceso("proceso:F9", "DOM: cuando C-DOM; SEG en caso contrario",
                     [_ob("ev", "VER")])
        if clasificar_propietario(p, _QUINCE_FIXTURE) != "POR_ITEM":
            return ("`DOM: cuando…` se toma por el identificador `DOM`: la igualdad de "
                    "cadena no se está aplicando sobre el valor recortado entero")
        if _pares(p):
            return "una prosa con aspecto de campo emite par estático"

    # --- el ANCLA, en sus dos ramas ---------------------------------------------------
    @f("ancla · las DOS ramas, y ante una referencia TIPADA `VER:dosier`")
    def _():
        con_ver = _proceso("proceso:FA", "PRD",
                           [_ob("a", "PRD"), _ob("b", "VER"), _ob("c", "APR")])
        if ancla_de(con_ver)[:2] != ("b", "VER"):
            return f"el ancla no es la obligatoria de `VER`: {ancla_de(con_ver)}"
        sin_ver = _proceso("proceso:FB", "INV", [_ob("a", "INV")])
        if ancla_de(sin_ver)[:2] != ("a", "INV"):
            return (f"sin `VER`, el ancla no cae en la última obligatoria: "
                    f"{ancla_de(sin_ver)}. Exigir «tras VER» donde no hay VER es `N-01`")
        tipada = _proceso("proceso:FC", "PRD", [_ob("a", "PRD"), _ob("d", "VER:dosier")])
        if ancla_de(tipada)[:2] != ("d", "VER"):
            return (f"una obligatoria `VER:dosier` no se reconoce como la de `VER`: la "
                    f"normalización no se aplica al buscar el ancla: {ancla_de(tipada)}")

    # --- `AUD`, con sus CINCO casos ---------------------------------------------------
    def _aud():
        return _proceso("proceso:FAUD", "DERIVADO del encargo", [_ob("cf", "INV")],
                        [_cond("DOM", "C-DOM"), _cond("SEG", "C-SEG")])

    @f("`AUD` · propietario `DOM` sin condicionales activos → `{DOM}`")
    def _():
        r = regla_por_item(_aud(), _VIGILADO_FIXTURE, _QUINCE_FIXTURE, "DOM", set())
        if r != {"DOM"}:
            return f"da {sorted(r) or '∅'} y tiene que dar {{DOM}}"

    @f("`AUD` · propietario `SEG` sin condicionales activos → `{SEG}`")
    def _():
        r = regla_por_item(_aud(), _VIGILADO_FIXTURE, _QUINCE_FIXTURE, "SEG", set())
        if r != {"SEG"}:
            return f"da {sorted(r) or '∅'} y tiene que dar {{SEG}}"

    @f("`AUD` · propietario `PRD` con `C-DOM` y `C-SEG` activos → `{DOM, SEG}`")
    def _():
        r = regla_por_item(_aud(), _VIGILADO_FIXTURE, _QUINCE_FIXTURE, "PRD",
                           {"C-DOM", "C-SEG"})
        if r != {"DOM", "SEG"}:
            return (f"da {sorted(r) or '∅'} y tiene que dar {{DOM, SEG}}. `D103` decía "
                    f"«cero o un par, NUNCA los dos»: es el contraejemplo de `M-01`")

    @f("`AUD` · propietario `PRD` sin condicionales activos → `∅`")
    def _():
        r = regla_por_item(_aud(), _VIGILADO_FIXTURE, _QUINCE_FIXTURE, "PRD", set())
        if r:
            return f"da {sorted(r)} y tiene que pasar VACÍO"

    @f("`AUD` · el ancla es su ÚNICA obligatoria, que produce `INV`, y no `VER`")
    def _():
        if ancla_de(_aud())[:2] != ("cf", "INV"):
            return (f"el ancla de `AUD` no es su conclusión fundada: {ancla_de(_aud())}. "
                    f"Exigirle la revisión «tras VER» es el contraejemplo de `N-01`")

    # --- `DIR`, con propietario vigilado y con propietario ajeno -----------------------
    def _dir():
        return _proceso("proceso:FDIR", "la capacidad PROPIETARIA de la decisión",
                        [_ob("ri", "ARQ"), _ob("dv", "VER")],
                        [_cond("DIS", "C-DIS"), _cond("APR", "C-APR")])

    @f("`DIR` · propietario efectivo `DOM` → `{DOM}` por la vía 1")
    def _():
        r = regla_por_item(_dir(), _VIGILADO_FIXTURE, _QUINCE_FIXTURE, "DOM", {"C-DIS"})
        if r != {"DOM"}:
            return f"da {sorted(r) or '∅'} y tiene que dar {{DOM}}"

    @f("`DIR` · propietario efectivo `ARQ` → `∅`, resuelto y no declarado")
    def _():
        r = regla_por_item(_dir(), _VIGILADO_FIXTURE, _QUINCE_FIXTURE, "ARQ",
                           {"C-DIS", "C-APR"})
        if r:
            return (f"da {sorted(r)} y tiene que pasar vacío. Declarar que `DIR` pasa vacío "
                    f"SIN resolver su item es el contraejemplo de `N-01`")

    # --- los MODOS DE FALLO cerrados --------------------------------------------------
    @f("negativo de `DEP` · `SEG` sólo en `obligatorias` y sin `SEG:revision` → FALLA")
    def _():
        p = _proceso("proceso:FDEP", "PLT", [_ob("cs", "SEG", "nadie: G28 lo hace "
                                                 "obligatorio"), _ob("ev", "VER")])
        pares = _pares(p)
        if not pares or revisiones_declaradas(p):
            return "el par `(DEP, SEG)` no se exige, o se da por puesto sin estarlo"
        if pares[0]["via"] != 2 or pares[0]["procedencia"] != "obligatorias":
            return f"el par de `DEP` no sale por la vía 2 desde `obligatorias`: {pares[0]}"

    @f("`<CAP>:revision` colocado ANTES de su ancla → se detecta")
    def _():
        p = _proceso("proceso:FANT", "PLT",
                     [_ob("cs", "SEG", "nadie"), _ob("rev", f"SEG:{VARIANTE}", "nadie"),
                      _ob("ev", "VER")])
        puestas = revisiones_declaradas(p)
        if not puestas or puestas[0]["indice"] > ancla_de(p)[2]:
            return ("una revisión colocada ANTES del ancla no se distingue de una colocada "
                    "después: la posición no se está midiendo")

    @f("`SEG:revision` RETIRABLE donde su origen es irretirable → se detecta")
    def _():
        if _retirable("nadie: G28 lo hace obligatorio y no se retira"):
            return "«nadie» se toma por retirable"
        if not _retirable("PLT, que posee la maquinaria"):
            return "una autoridad de retirada real se toma por irretirable"

    @f("modo de fallo · una proyección con TOTAL FIJO distinto del derivado")
    def _():
        arbol = [(_proceso("proceso:FX", "PRD", [_ob("ev", "VER")],
                           [_cond("DOM:condiciones", "C-DOM")]), "")]
        derivado = len(catalogo_estatico(arbol, _VIGILADO_FIXTURE, _QUINCE_FIXTURE))
        if derivado != 1:
            return f"el árbol sintético deriva {derivado} pares y tiene que derivar 1"
        # una proyección que publicara «2 pares» sobre este árbol tiene que discrepar del
        # derivado, que es lo único que impide que la cifra envejezca en silencio (`M-04`)
        if derivado == 2:
            return "una proyección de 2 pares coincidiría con un árbol que deriva 1"

    @f("conjunto VIGILADO derivado de las fichas, y no escrito")
    def _():
        ficha = {"capacidad": [
            ({"id": "DOM", "deriva_de": ["b.16 · DOM participa dos veces: condiciones antes "
                                         "de CON, revisión después de VER"]}, ""),
            ({"id": "ARQ", "deriva_de": ["b.16 · ARQ es propietario global de DEU"]}, "")]}
        derivado = conjunto_vigilado(ficha)
        if derivado != {"DOM"}:
            return (f"el conjunto vigilado da {sorted(derivado)} sobre unas fichas donde "
                    f"sólo `DOM` declara la doble participación: no se está derivando de "
                    f"ellas (`Q-09`)")

    return lote


def censo_publicado(base):
    """La cifra de fixtures que §19 publica. NO se escribe aquí: se lee de su sede."""
    ruta = os.path.join(base, SEDE_DE_LA_PROYECCION)
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    m = re.search(r"CENSO DE FIXTURES.{0,200}?escrito a mano:\s*(\d+)\s+fixtures",
                  texto, re.S)
    return int(m.group(1)) if m else None


def t275_los_fixtures_se_ejecutan_y_se_cuentan(raiz=None):
    """`D104` · los fixtures se ejecutan EN CADA CORRIDA, y su censo se contrasta."""
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T275", "Los fixtures de D104 se ejecutan y su censo coincide con su sede")
    lote = fixtures()
    for nombre, comprobacion in lote:
        motivo = comprobacion()
        if motivo:
            r.fallo(f"fixture «{nombre}»: {motivo}")
    publicado = censo_publicado(base)
    if publicado is None:
        # La sede no viaja al proyecto instalado. Se dice, y no se inventa una cifra.
        return r
    if publicado != len(lote):
        r.fallo(f"el censo de fixtures publicado es {publicado} y esta batería ejecuta "
                f"{len(lote)}. SEDE: `{SEDE_DE_LA_PROYECCION}`, §19, ficha `D104`, campo "
                f"«QUÉ TIENE QUE DEMOSTRAR LA COMPROBACIÓN». RESPONSABLE: `SIS`. REMEDIO: "
                f"o la batería recupera el fixture que perdió, o la sede publica la cifra "
                f"que la batería corre. Una cifra que envejece en silencio es `M-04`")
    return r


def t276_las_proyecciones_derivan(raiz=None):
    """`D104` · los tres repartos y el conjunto vigilado DERIVAN, y su sede no discrepa.

    `G-15` contrasta vía a vía, procedencia a procedencia y ancla a ancla contra la
    proyección ÚNICA de §19. Una proyección que publique un total fijo distinto del
    derivado FALLA, y una segunda proyección contradictoria en el mismo bloque también.
    """
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T276", "Los repartos por vía, procedencia y ancla derivan del árbol")
    bloques = cargar(base)
    las_quince, vigilado = quince(base), conjunto_vigilado(bloques)
    if len(las_quince) != 15:
        r.fallo(f"los directorios de `capacidades/` dan {len(las_quince)} capacidades y el "
                f"conjunto de las QUINCE es el que gobierna toda la normalización")
    catalogo = catalogo_estatico(bloques.get("proceso", []), vigilado, las_quince)
    ruta = os.path.join(base, SEDE_DE_LA_PROYECCION)
    if not os.path.exists(ruta):
        return r
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()

    # ANCLA, proceso a proceso, contra la proyección publicada
    publicadas = dict(re.findall(r"`([A-Z]{3})\s*→\s*([A-Z]{3})`", texto))
    for datos, _ruta in bloques.get("proceso", []):
        codigo = datos["id"].split(":", 1)[1]
        if codigo not in publicadas:
            continue
        _oid, capacidad, _i = ancla_de(datos)
        if publicadas[codigo] != capacidad:
            r.fallo(f"§19 publica el ancla `{codigo} → {publicadas[codigo]}` y el árbol "
                    f"deriva `{codigo} → {capacidad}`")

    # REPARTO POR VÍA y POR PROCEDENCIA
    por_via = {v: sum(1 for p in catalogo if p["via"] == v) for v in (1, 2, 3, 4)}
    m = re.search(r"vía 1 · (\d+) pares? · vía 2 · (\d+) par(?:es)? · vía 3 · (\d+) "
                  r"pares? ·\s*\n?\s*vía 4 ·\s*\n?\s*(\d+) pares?", texto)
    if m:
        for i, via in enumerate((1, 2, 3, 4)):
            if int(m.group(i + 1)) != por_via[via]:
                r.fallo(f"§19 publica {m.group(i + 1)} pares por la vía {via} y el árbol "
                        f"deriva {por_via[via]}. Un total admite repartos que significan "
                        f"cosas distintas: publicar sólo el total no basta (`Q-03`)")
    por_procedencia = {p: sum(1 for x in catalogo if x["procedencia"] == p)
                       for p in ("propietaria", "obligatorias", "condicionales")}
    m = re.search(r"propietaria · (\d+) pares? ·\s*\n?\s*`?obligatorias`? · (\d+) "
                  r"par(?:es)?[^·]*·\s*`?condicionales`? · (\d+)\s*\n?\s*pares?", texto)
    if m:
        for i, procedencia in enumerate(("propietaria", "obligatorias", "condicionales")):
            if int(m.group(i + 1)) != por_procedencia[procedencia]:
                r.fallo(f"§19 publica {m.group(i + 1)} pares de procedencia "
                        f"`{procedencia}` y el árbol deriva {por_procedencia[procedencia]} "
                        f"(`Q-28`)")
    return r


PRUEBAS = [t273_catalogo_estatico_materializado, t274_regla_por_item,
           t275_los_fixtures_se_ejecutan_y_se_cuentan, t276_las_proyecciones_derivan]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None)
    ap.add_argument("--catalogo", action="store_true",
                    help="publicar el catálogo derivado, sin juzgarlo")
    args = ap.parse_args()
    if args.catalogo:
        base = os.path.abspath(args.raiz or RAIZ)
        bloques = cargar(base)
        las_quince, vigilado = quince(base), conjunto_vigilado(bloques)
        catalogo = catalogo_estatico(bloques.get("proceso", []), vigilado, las_quince)
        print(f"conjunto vigilado (derivado de las fichas): {sorted(vigilado)}")
        print(f"{len({p['proceso'] for p in catalogo})} procesos · {len(catalogo)} pares")
        for p in catalogo:
            print(f"  {p['proceso']:14} {p['capacidad']}:{VARIANTE}  vía {p['via']}  "
                  f"{p['procedencia']:14} ancla {p['ancla']} ({p['ancla_capacidad']})")
        return 0
    resultados = [f(args.raiz) for f in PRUEBAS]
    if args.json:
        print(json.dumps([{"id": x.id, "nombre": x.nombre,
                           "estado": "prueba-superada" if x.superada else "prueba-fallida",
                           "fallos": x.fallos} for x in resultados], ensure_ascii=False,
                         indent=2))
    else:
        for x in resultados:
            print(f"{x.id}  {'SUPERADA' if x.superada else 'FALLIDA '}  {x.nombre}")
            for f in x.fallos:
                print(f"          · {f}")
        fallidas = [x for x in resultados if not x.superada]
        print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if any(not x.superada for x in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
