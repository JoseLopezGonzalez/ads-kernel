#!/usr/bin/env python3
"""comprobar_recuentos — ninguna cifra del corpus se escribe a mano.

Hallazgo A-24: once recuentos incorrectos, repartidos por cuatro de los cinco contratos
transversales, el índice, la nota de versión y el registro de pruebas. «Diecisiete
esquemas» cuando eran dieciséis, «35 métodos» cuando eran treinta y cuatro, «veintiocho
campos» sobre una tabla de veintinueve filas, «trece estaciones» sobre un diagrama de
catorce. Ninguno rompía la ejecución; en conjunto invalidaban la lectura del corpus como
fuente fiable, y aparecían en la propia nota que resumía el trabajo.

La fuente canónica de cada cifra es **el corpus**. Este validador la deriva, publica
`pruebas/RECUENTOS-generado.md` y comprueba que ningún documento afirme otra cosa.

CONTRATO 1 de `11-ARQ` §19 · la COBERTURA DE SEDES ya no se enumera: se DESCUBRE barriendo
el corpus vivo, en dígitos y en letra. Ver el bloque `REGLAS`.
CONTRATO 1bis de `11-ARQ` §19 · los `ads:perfil-agente` de `C2` se cuentan como los demás
bloques tipados, y la cifra deja de vivir sólo en prosa.

Uso:
  python3 kernel/operativo/validadores/comprobar_recuentos.py [--json] [--raiz DIR]
                                                             [--generar]
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

# Los cardinales castellanos, CONSTRUIDOS y no escritos a mano. El censo tiene que leer
# «veintiocho» y «DOCE» igual que lee `28` y `12`: el hallazgo `A-24` y los ocho casos de
# regresión de §19 están escritos en letra, no en dígitos, y una tabla parcial de cardinales
# es otra lista literal que envejece. Se generan las unidades, la decena irregular, las
# veintenas y las decenas con su «y», que es todo el rango en que un corpus publica censos.
_UNIDADES = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho",
             "nueve"]
_DIEZ_A_VEINTINUEVE = [
    "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
    "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés",
    "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho",
    "veintinueve"]
_DECENAS = {30: "treinta", 40: "cuarenta", 50: "cincuenta", 60: "sesenta", 70: "setenta",
            80: "ochenta", 90: "noventa"}


def _construir_cardinales():
    tabla = {i: p for i, p in enumerate(_UNIDADES)}
    tabla.update({i + 10: p for i, p in enumerate(_DIEZ_A_VEINTINUEVE)})
    for decena, nombre in _DECENAS.items():
        tabla[decena] = nombre
        for u in range(1, 10):
            tabla[decena + u] = f"{nombre} y {_UNIDADES[u]}"
    tabla[100] = "cien"
    return tabla


CARDINALES = _construir_cardinales()

# Las variantes de género y apócope que el castellano usa delante de un sustantivo. No son
# cifras nuevas: son la MISMA cifra escrita como se escribe cuando lleva nombre detrás.
_VARIANTES = {"un": 1, "una": 1, "veintiún": 21, "veintiuna": 21, "veintiuna": 21,
              "treinta y un": 31, "treinta y una": 31, "cuarenta y un": 41,
              "cuarenta y una": 41, "cincuenta y un": 51, "cincuenta y una": 51}


# Cómo se llama en castellano cada tipo canónico cuando se publica su censo. NO es la lista
# de lo que se cuenta —eso lo deriva `derivar` de los esquemas del árbol—: es sólo la
# traducción de los que ya tenían nombre. Un tipo que falte aquí se publica igual.
NOMBRE_DEL_TIPO = {
    "capacidad": "capacidades", "rol": "roles", "metodo": "metodos", "gate": "gates",
    "composicion": "composiciones", "escenario": "escenarios", "pack": "packs",
    "veto": "vetos", "rubrica": "rubricas", "handoff": "handoffs", "proceso": "procesos",
    "nivel-novedad": "niveles_de_novedad", "forma-conversacion": "formas_de_conversacion",
    "entrada": "clases_de_entrada", "memoria": "secciones_de_memoria",
    "perfil-agente": "perfiles_de_agente", "encuadre": "encuadres",
    "integration-set": "integration_sets", "esquema": "bloques_de_esquema",
}


def derivar(base=None):
    """Todas las cifras, calculadas desde el corpus. Es la única fuente."""
    base = os.path.abspath(base or RAIZ)
    lint = Lint(base, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    por_tipo = {}
    for tipo, datos, ruta, _l in lint.bloques:
        por_tipo.setdefault(tipo, []).append((datos, ruta))

    def n(tipo):
        return len(por_tipo.get(tipo, []))

    def ficheros(patron, raiz_rel):
        origen = os.path.join(base, raiz_rel)
        salida = []
        for dirpath, dirnames, filenames in os.walk(origen):
            dirnames[:] = [d for d in dirnames
                           if d != "__pycache__" and not d.startswith("legacy-")]
            for f in filenames:
                if re.search(patron, os.path.join(dirpath, f)):
                    salida.append(os.path.join(dirpath, f))
        return salida

    import yaml as _yaml
    def campos_obligatorios(esquema):
        ruta = os.path.join(base, f"kernel/operativo/esquemas/{esquema}.yaml")
        with open(ruta, encoding="utf-8") as fh:
            return len(_yaml.safe_load(fh).get("obligatorios") or [])

    # ===================================================================================
    #  CONTRATO 1bis de `11-ARQ` §19 (`N-04`) · NINGÚN TIPO CANÓNICO SE QUEDA SIN CENSO
    # ===================================================================================
    #  `C2` declara VEINTIÚN bloques `ads:perfil-agente`, y esta tabla contaba roles,
    #  métodos, prompts, composiciones, gates, rúbricas, vetos, formas, niveles de novedad
    #  y clases de entrada —todos tipados exactamente igual que éste— y NO los contaba. Por
    #  eso ninguna comprobación mecánica pudo cazar que el documento 17 publicase 22 y 21
    #  para el mismo objeto, ni que su adjudicador diera el requisito `0.1` por satisfecho.
    #
    #  El remedio NO es añadir una línea para `perfil-agente`: eso deja la siguiente
    #  omisión esperando. El conjunto de tipos se DERIVA de los esquemas del árbol, y cada
    #  uno recibe censo por existir. Un tipo canónico nuevo queda contado el día que nace.
    #  `NOMBRE_DEL_TIPO` sólo traduce al castellano los que ya tenían nombre publicado; un
    #  tipo sin traducción se publica igual, con su nombre técnico, y nunca en silencio.
    cuenta = {}
    for tipo in sorted(lint.esquemas):
        cuenta[NOMBRE_DEL_TIPO.get(tipo, "bloques_" + tipo.replace("-", "_"))] = n(tipo)
    cuenta.update({
        "esquemas": len(ficheros(r"/esquemas/.+\.yaml$", "kernel/operativo")),
        "validadores": len(ficheros(r"/validadores/.+\.py$", "kernel/operativo")),
        "prompts": len(ficheros(r"/prompts/.+\.md$", "kernel/operativo")),
        "campos_de_rol": campos_obligatorios("rol"),
        "campos_de_metodo": campos_obligatorios("metodo"),
        "campos_de_capacidad": campos_obligatorios("capacidad"),
        "campos_de_pack": campos_obligatorios("pack"),
        "contratos_transversales": len(ficheros(r"/contratos/C\d.*\.md$", "kernel/operativo")),
    })
    # Las estaciones del circuito de entrada se cuentan del PROPIO DIAGRAMA, que es su
    # sede. Vivía fuera de `derivar`, en el cuerpo de `T151`, y por eso ninguna otra prueba
    # podía usarla: una derivación que sólo existe dentro de una prueba no es una fuente.
    ruta_circuito = os.path.join(base, "kernel/operativo/entrada/02-CIRCUITO.md")
    if os.path.exists(ruta_circuito):
        with open(ruta_circuito, encoding="utf-8") as fh:
            cuenta["estaciones_de_entrada"] = len(
                set(re.findall(r"│\s*(\d{1,2})\s{2}[A-ZÁÉÍÓÚÑ]", fh.read())))
    cuenta["composiciones_de_dis"] = len(
        [1 for d, ruta in por_tipo.get("composicion", []) if "/DIS/" in ruta])
    cuenta["roles_de_dis"] = len(
        [1 for d, _ in por_tipo.get("rol", []) if d.get("capacidad") == "DIS" and ":" not in d["id"]])
    cuenta["metodos_de_dis"] = len(
        [1 for d, _ in por_tipo.get("metodo", []) if d.get("capacidad") == "DIS"])
    return cuenta


# ===========================================================================
#  CONTRATO 1 de `11-ARQ` §19 · LA COBERTURA DE SEDES SE DESCUBRE, NO SE ENUMERA
# ===========================================================================
#  Aquí vivía `AFIRMACIONES`: una lista literal de `(ruta, patrón, clave)`. Su defecto no
#  era estar mal escrita: era estar ESCRITA. Cubría `C1` y no cubría
#  `contratos/00-INDICE.md`:7 ni `pruebas/T086-T092-contratos.md`:14 —«veintiocho campos»
#  sobre un esquema de veintinueve—, y `T151` salía SUPERADA con dos sedes vigentes
#  afirmando lo que el corpus desmiente. La condición de cierre del contrato es literal:
#  «que `AFIRMACIONES` deje de existir como lista literal y que la cobertura del validador
#  sea derivada. Mientras exista la lista, la condición NO está cerrada, aunque `T151` salga
#  verde».
#
#  Lo que la sustituye es lo que el contrato prescribe con esas palabras: «para cada cifra
#  publicada, la FUENTE de la que deriva declarada como una regla `(patrón de sede,
#  derivación)` — no una lista de rutas». La RUTA deja de enumerarse. Cada regla declara un
#  PATRÓN de sede, y **una sede nueva queda cubierta el día que nace**, sin tocar este
#  fichero: es exactamente lo que la prueba negativa del contrato exige demostrar.
#
#  Lo que sí sigue declarándose, porque el contrato lo pide así, es CÓMO se publica cada
#  cifra —el patrón de la afirmación— y DE DÓNDE sale su valor verdadero —la derivación—.
#  Eso no es una lista de sedes: es el diccionario de lo censable.


class Regla:
    """Una regla `(patrón de sede, derivación)` del CONTRATO 1.

    `sede`      expresión regular sobre la RUTA RELATIVA. Por defecto, cualquier documento
                del corpus vivo: la cobertura no se enumera.
    `objeto`    cómo se nombra el objeto censable cuando alguien publica su cardinal. El
                patrón completo se construye con la MARCA DE TOTALIDAD delante —«las quince
                capacidades»—, que es lo que distingue la afirmación del TOTAL de la de un
                subconjunto: «dos capacidades con veto» no lleva ninguna y no es un censo.

                DECISIÓN · la marca era SÓLO el artículo, y se le añade el VERBO DE
                DECLARACIÓN. La auditoría midió que «El corpus declara veintiocho
                capacidades» —sin artículo delante del cardinal— no se detectaba. El
                razonamiento gramatical de origen sigue en pie: hace falta una marca, y
                admitir cualquier cardinal suelto denunciaría verdades hasta que alguien
                apagara el validador. Pero «declara N objetos» es tan afirmación del total
                como «los N objetos»: el verbo de censo hace el mismo trabajo que el
                artículo. Se admite ese verbo, y NADA MÁS: se midió que sobre el corpus de
                hoy no produce ni un falso positivo (cero divergencias nuevas en 500+
                ficheros). Verbos como «contiene» o «incluye» NO se admiten, porque
                admiten legítimamente un subconjunto —«contiene tres bloques de esto»— y
                ahí la marca no dice nada.
    `salvo`     lo que, escrito INMEDIATAMENTE DETRÁS del objeto, restringe el conjunto y
                convierte la afirmación en otra cosa: «los dos gates **de Diseño**» no
                afirma cuántos gates hay. Sin esto la regla denunciaría verdades.
    `extra`     formulaciones que no siguen la forma artículo+cardinal+objeto y que el
                corpus usa igual: «las clases de expresión son nueve», «Contiene catorce
                bloques». Llevan su propio grupo de captura.
    """

    def __init__(self, clave, objeto, *, sede=r"\.md$", salvo=None, marca=None,
                 extra=None, articulo=r"(?:l[oa]s|sus|declaran?)"):
        self.clave, self.objeto, self.sede_re = clave, objeto, re.compile(sede)
        self.salvo = re.compile(salvo, re.I) if salvo else None
        cola = r"\s+(?:" + marca + r")\b" if marca else r"\b"
        self.patrones = [re.compile(
            articulo + r"\s+(?:\*\*)?(" + _NUMERAL + r")(?:\*\*)?\s+(?:\*\*)?(?:" + objeto
            + r")" + cola, re.I)]
        for p in (extra or []):
            self.patrones.append(re.compile(p.replace("<N>", "(" + _NUMERAL + ")"), re.I))


# El NUMERAL, en dígitos o en letra. Se construye del diccionario de cardinales para que no
# haya dos sedes de lo mismo: si el diccionario crece, el barrido lee más, sin tocar nada.
def _alternativa_numeral():
    palabras = set(CARDINALES.values()) | set(_VARIANTES)
    # sin tildes también: el corpus las escribe de las dos maneras
    palabras |= {p.translate(str.maketrans("áéíóú", "aeiou")) for p in palabras}
    return "|".join(sorted(palabras, key=len, reverse=True))


_NUMERAL = r"\d{1,3}|" + _alternativa_numeral()

# El corpus VIVO: dónde una cifra obsoleta es un defecto que hay que corregir. Es un
# conjunto de PATRONES, no una lista de ficheros, y por eso una sede nueva entra sola.
AMBITO_VIVO = [r"^README\.md$", r"^START_HERE\.md$", r"^kernel/", r"^packs/",
               r"^docs/canonico/", r"^docs/f6/"]

# Y lo que queda FUERA, cada patrón con su motivo escrito. Un corpus histórico no se
# corrige: se cita. Excluirlo sin decir por qué sería la lista literal por la puerta de
# atrás, y por eso `T151` comprueba que cada motivo esté escrito.
FUERA_DEL_AMBITO = [
    (r"^kernel/KERNEL_CHANGELOG\.md$",
     "registro histórico: cita las cifras que eran ciertas en cada versión anterior"),
    (r"^kernel/operativo/pruebas/evidencia/",
     "salidas CAPTURADAS de ejecuciones pasadas: se regeneran, no se editan"),
    (r"^kernel/operativo/pruebas/RECUENTOS-generado\.md$",
     "es el DERIVADO que este validador publica: compararlo consigo mismo no dice nada"),
    (r"^kernel/operativo/validadores/",
     "es el código, y contiene las infracciones DELIBERADAS de `comprobar_negativos.py`"),
    (r"^packs/legacy-", "packs retirados: se conservan sólo para trazabilidad"),
    (r"^docs/f6/\d\d-GATE-.*-\d{8}\.md$",
     "acta de un gate FECHADO: describe el árbol de ese día y no se reescribe"),
]


def _vivo(rel):
    if not any(re.search(p, rel) for p in AMBITO_VIVO):
        return False
    return not any(re.search(p, rel) for p, _m in FUERA_DEL_AMBITO)


def sedes_vivas(base):
    """Todo documento del corpus VIVO, DESCUBIERTO por barrido. Nunca una lista."""
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "__pycache__", ".pytest_cache")]
        for nombre in sorted(filenames):
            if not nombre.endswith(".md"):
                continue
            ruta = os.path.join(dirpath, nombre)
            rel = os.path.relpath(ruta, base).replace(os.sep, "/")
            if _vivo(rel):
                yield rel, ruta


# El diccionario de lo CENSABLE: qué objetos publica el corpus con cardinal, y de qué
# derivación sale el valor verdadero de cada uno. **Ninguna entrada nombra una ruta.**
#
# Por qué unas reglas llevan `salvo` y otras `marca`. El castellano marca el TOTAL con el
# artículo —«las quince capacidades»— y el SUBCONJUNTO con un restrictivo detrás —«los dos
# gates de Diseño», «las dos capacidades QUE pueden actuar solas»—. Donde el sustantivo sólo
# nombra el catálogo entero, basta con excluir los restrictivos que el corpus usa (`salvo`).
# Donde el sustantivo nombra también agrupaciones internas —`gates`, `roles`, `métodos`,
# `composiciones` viven en subconjuntos con nombre propio—, la regla exige la MARCA de
# totalidad (`marca`): sin ella, la regla denunciaría verdades, que es el modo de fallo que
# convierte un validador en ruido y termina apagándolo.
#
# `validadores` NO tiene regla, y se dice por qué: el corpus llama «validadores» tanto a los
# ficheros de `validadores/` como a las validaciones registradas del manifiesto, y las dos
# cifras son legítimamente distintas. Un objeto cuyo nombre no identifica un conjunto no es
# censable en prosa; su cifra se publica igual en `RECUENTOS-generado.md`, y `T154` exige
# que llegue allí.
REGLAS = [
    Regla("capacidades", r"capacidades|c[oó]digos est[aá]n reservados",
          salvo=r"\s*(?:ejecutables|con veto|del pack|que\b)"),
    Regla("contratos_transversales", r"contratos transversales"),
    Regla("procesos", r"procesos",
          salvo=r"\s*(?:reales|independientes|concurrentes|intentan|usen|compit)"),
    Regla("esquemas", r"tipos can[oó]nicos|esquemas",
          extra=[r"el lenguaje canónico y los (?:\*\*)?<N>(?:\*\*)? tipos"]),
    Regla("prompts", r"prompts can[oó]nicos|prompts operativos"),
    Regla("roles", r"roles", marca=r"del corpus|declarados|can[oó]nicos|del cat[aá]logo"),
    Regla("metodos", r"m[eé]todos",
          marca=r"del corpus|declarados|can[oó]nicos|del cat[aá]logo"),
    Regla("gates", r"gates", marca=r"del corpus|declarados|can[oó]nicos|del cat[aá]logo"),
    Regla("composiciones", r"composiciones",
          marca=r"del corpus|declaradas|can[oó]nicas|del cat[aá]logo"),
    Regla("handoffs", r"handoffs|entregas tipadas", salvo=r"\s*(?:de|del|que)\b"),
    Regla("vetos", r"vetos", salvo=r"\s*(?:de|del|que|levantables|duros)\b"),
    Regla("rubricas", r"r[uú]bricas", salvo=r"\s*(?:de|del|que)\b"),
    Regla("packs", r"packs", salvo=r"\s*(?:de|del|que|distintos|aportan|dicen|no pueden)\b"),
    Regla("niveles_de_novedad", r"niveles de novedad"),
    Regla("secciones_de_memoria", r"secciones del corpus|secciones de memoria"),
    Regla("formas_de_conversacion", r"formas de conversaci[oó]n",
          extra=[r"Contiene (?:\*\*)?<N>(?:\*\*)? bloques"]),
    Regla("clases_de_entrada", r"clases de (?:expresi[oó]n|entrada)",
          extra=[r"las clases de expresi[oó]n son (?:\*\*)?<N>(?:\*\*)?"]),
    Regla("estaciones_de_entrada", r"estaciones", sede=r"^kernel/operativo/entrada/",
          extra=[r"(?m)^(?:\*\*)?<N>(?:\*\*)? estaciones\."]),
    Regla("campos_de_rol", r"campos del contrato de rol",
          extra=[r"Contrato común de rol — (?:\*\*)?<N>(?:\*\*)? campos",
                 r"\brol\b[^.\n]{0,60}?\bsus (?:\*\*)?<N>(?:\*\*)? campos",
                 r"(?m)^(?![^\n]*m[eé]todo)[^\n]*declara los (?:\*\*)?<N>(?:\*\*)? campos del esquema"]),
    Regla("campos_de_metodo", r"campos del contrato de m[eé]todo",
          extra=[r"(?m)^[^\n]*m[eé]todo[^\n]*declara los (?:\*\*)?<N>(?:\*\*)? campos del esquema"]),
    # CONTRATO 1bis · el censo que nadie hacía (`N-04`). Ver `perfiles_de_agente` en
    # `derivar`: son los bloques `ads:perfil-agente` de `C2`, contados por barrido.
    Regla("perfiles_de_agente", r"perfiles de agente|bloques `?ads:perfil-agente`?",
          salvo=r"\s*(?:distintos|del pack|que)\b"),
    Regla("roles_de_dis", r"contratos|instrucciones operativas",
          sede=r"^kernel/operativo/capacidades/DIS/", articulo=r"—"),
    Regla("metodos_de_dis", r"procedimientos",
          sede=r"^kernel/operativo/capacidades/DIS/", articulo=r"—"),
    Regla("composiciones_de_dis", r"matrices de composici[oó]n",
          sede=r"^kernel/operativo/capacidades/DIS/", articulo=r"—"),
    Regla("roles_de_dis", r"(?!)", sede=r"^kernel/operativo/diseno/",
          extra=[r"con sus (?:\*\*)?<N>(?:\*\*)? roles"]),
    Regla("metodos_de_dis", r"(?!)", sede=r"^kernel/operativo/diseno/",
          extra=[r"sus (?:\*\*)?<N>(?:\*\*)? m[eé]todos"]),
]


def _palabra_a_numero(txt):
    txt = txt.strip().lower().strip(".,;:*_`«»—-")
    if txt.isdigit():
        return int(txt)
    sin_tilde = txt.translate(str.maketrans("áéíóú", "aeiou"))
    for tabla in (_VARIANTES,):
        if txt in tabla:
            return tabla[txt]
    for valor, palabra in CARDINALES.items():
        if txt in (palabra, palabra.translate(str.maketrans("áéíóú", "aeiou"))):
            return valor
    for palabra, valor in _VARIANTES.items():
        if sin_tilde == palabra.translate(str.maketrans("áéíóú", "aeiou")):
            return valor
    return None


# ---------------------------------------------------------------------------
#  DESHACER EL REFLUJO ANTES DE MIRAR
# ---------------------------------------------------------------------------
#  DECISIÓN · el barrido se aplica DOS VECES: al texto tal cual, y al texto con el
#  reflujo deshecho.
#
#  El defecto medido: `Los DOCE contratos transversales` se detectaba, y
#  `Los DOCE contratos\ntransversales` NO. El corpus entero está ajustado a noventa
#  columnas, luego una afirmación de cardinal partida por el ajuste de línea no es el caso
#  raro: es el caso NORMAL. Un control que sólo ve las afirmaciones que caben en una línea
#  deja fuera, por construcción, a la mayoría de las que hay, y el que quisiera colar una
#  cifra falsa sólo tendría que escribirla larga.
#
#  Por qué DOS PASADAS y no una sola sobre el texto colapsado. Tres patrones `extra` del
#  diccionario están anclados a la LÍNEA —`(?m)^…`, `[^\n]*`— para distinguir «la línea que
#  habla de método» de «la que no». Colapsar los saltos de línea los rompería, y arreglar
#  el defecto rompiendo tres detecciones vigentes sería cambiar un agujero por otro. Con
#  dos pasadas no se pierde ni una detección de las de hoy: sólo se añaden las que el
#  reflujo escondía. Las divergencias se deduplican por `(sede, línea, clave, cifra)`.
#
#  Y por qué se CONSERVA el corte de párrafo. Colapsar también los renglones en blanco
#  pegaría el final de un párrafo con el principio del siguiente y fabricaría frases que
#  nadie escribió —«… los doce» + «Contratos transversales …»—, que es denunciar una
#  verdad: el modo de fallo que convierte un validador en ruido. Una afirmación no cruza
#  un párrafo.

def _sin_reflujo(texto):
    """`(plano, origen)` — el texto con el reflujo deshecho, y el mapa al original.

    `plano[i]` procede de `texto[origen[i]]`, de modo que el NÚMERO DE LÍNEA que se publica
    sigue siendo el del fichero real y no el de un texto que no existe en disco. Sin ese
    mapa, el diagnóstico apuntaría a una línea inventada y quien lo leyera no encontraría
    nada allí.
    """
    plano, origen, i, n = [], [], 0, len(texto)
    while i < n:
        if not texto[i].isspace():
            plano.append(texto[i])
            origen.append(i)
            i += 1
            continue
        j = i
        while j < n and texto[j].isspace():
            j += 1
        racha = texto[i:j]
        # dos o más saltos de línea son un CORTE DE PÁRRAFO, y se conserva como tal
        pieza = "\n\n" if racha.count("\n") >= 2 else " "
        for c in pieza:
            plano.append(c)
            origen.append(i)
        i = j
    origen.append(n)
    return "".join(plano), origen


def barrer_afirmaciones(base, cuenta):
    """El barrido del CONTRATO 1: `(ruta, línea, cifra escrita, cifra derivada)`.

    No recibe ninguna ruta. Recorre las sedes VIVAS que encuentra y aplica a cada una las
    reglas cuyo PATRÓN DE SEDE la alcanza, sobre el texto literal Y sobre el texto sin
    reflujo. Devuelve sólo las divergencias, sin repetir.
    """
    divergencias, vistas = [], set()
    for rel, ruta in sedes_vivas(base):
        aplicables = [g for g in REGLAS if g.sede_re.search(rel)]
        if not aplicables:
            continue
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        plano, origen = _sin_reflujo(texto)
        for regla in aplicables:
            derivado = cuenta.get(regla.clave)
            if derivado is None:
                continue
            for patron in regla.patrones:
                # el literal PRIMERO: su cita es la que el corpus escribió, y es la que se
                # publica cuando la misma afirmación aparece en las dos pasadas
                for cuerpo, mapa in ((texto, None), (plano, origen)):
                    for m in patron.finditer(cuerpo):
                        cola = re.sub(r"[\s>]+", " ", cuerpo[m.end():m.end() + 60])
                        if regla.salvo and regla.salvo.match(cola):
                            continue
                        escrito = _palabra_a_numero(m.group(1))
                        if escrito is None or escrito == derivado:
                            continue
                        inicio = m.start() if mapa is None else mapa[m.start()]
                        linea = texto[:inicio].count("\n") + 1
                        firma = (rel, linea, regla.clave, escrito)
                        if firma in vistas:
                            continue
                        vistas.add(firma)
                        divergencias.append((rel, linea, m.group(0).strip(), escrito,
                                             regla.clave, derivado))
    return divergencias


def t151_recuentos_derivados(raiz=None):
    """CONTRATO 1 · ninguna sede viva publica un cardinal que el corpus desmienta."""
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T151", "Ninguna cifra del corpus contradice el recuento derivado")
    cuenta = derivar(base)
    # Cada exclusión del ámbito tiene que decir POR QUÉ. Una exclusión sin motivo es la
    # lista literal volviendo por la puerta de atrás.
    for patron, motivo in FUERA_DEL_AMBITO:
        if not (motivo or "").strip():
            r.fallo(f"la exclusión «{patron}» no dice por qué queda fuera del ámbito vivo")
    for rel, linea, cita, escrito, clave, derivado in barrer_afirmaciones(base, cuenta):
        r.fallo(f"{rel}:{linea}: «{cita}» — escrito {escrito} · derivado {derivado} "
                f"({clave}). La sede no se enumeró: la encontró el barrido "
                f"(`11-ARQ` §19, CONTRATO 1)")
    return r


def t270_la_cobertura_de_sedes_se_descubre(raiz=None):
    """CONTRATO 1, condición de cierre · la cobertura DERIVA, y se demuestra ejerciéndola.

    No inspecciona el texto de este fichero buscando la palabra `AFIRMACIONES`: eso sería
    una prueba de redacción. Ejerce la PROPIEDAD que la lista literal no tenía. Fabrica en
    un directorio temporal una sede que **no existe en ningún sitio** —nombre nuevo, ruta
    nueva, contenido nuevo— con una afirmación falsa sobre un objeto censable, y exige que
    el mismo barrido que corre `T151` la denuncie sin haber tocado ninguna declaración.

    Y comprueba lo contrario, que es la mitad que se olvida: la misma sede con la cifra
    VERDADERA no puede producir ningún fallo. Un barrido que denuncia siempre no verifica
    nada.
    """
    import tempfile
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T270", "La cobertura de sedes se descubre barriendo, y no se enumera")
    cuenta = derivar(base)
    verdad = cuenta.get("capacidades")
    if not verdad:
        r.fallo("no se deriva el número de capacidades: sin derivación no hay contra qué "
                "comparar")
        return r
    with tempfile.TemporaryDirectory(prefix="ads-cobertura-") as tmp:
        # una sede que ninguna lista podría contener: no existe en el corpus
        nueva = os.path.join(tmp, "kernel", "operativo", "SEDE-QUE-NADIE-ENUMERO.md")
        os.makedirs(os.path.dirname(nueva), exist_ok=True)
        falsa = CARDINALES[verdad + 1].upper()
        with open(nueva, "w", encoding="utf-8") as fh:
            fh.write(f"# sede nueva\n\nEl sistema tiene las {falsa} capacidades "
                     f"declaradas.\n")
        hallado = barrer_afirmaciones(tmp, cuenta)
        if not any(h[0].endswith("SEDE-QUE-NADIE-ENUMERO.md") for h in hallado):
            r.fallo("una sede NUEVA con la afirmación falsa «las {} capacidades» NO fue "
                    "detectada: la cobertura sigue enumerándose en vez de derivarse "
                    "(`11-ARQ` §19, CONTRATO 1, prueba negativa)".format(falsa))
        with open(nueva, "w", encoding="utf-8") as fh:
            fh.write(f"# sede nueva\n\nEl sistema tiene las {CARDINALES[verdad]} "
                     f"capacidades declaradas.\n")
        if barrer_afirmaciones(tmp, cuenta):
            r.fallo("la MISMA sede con la cifra verdadera también se denuncia: un barrido "
                    "que falla siempre no distingue nada")
    return r


def t271_todo_recuento_derivado_se_publica(raiz=None):
    """CONTRATO 1bis · ninguna cifra derivada se queda sin publicar, y `N-04` en concreto.

    `RECUENTOS-generado.md` contaba roles, métodos, prompts, composiciones, gates,
    rúbricas, vetos, formas, niveles de novedad y clases de entrada —todos bloques tipados
    como los `ads:perfil-agente` de `C2`— y NO contaba los perfiles de agente. Por eso
    ninguna comprobación mecánica podía cazar que el documento 17 publicase DOS cifras
    distintas para el mismo objeto. La condición de cierre es que la cifra deje de existir
    sólo en prosa.

    Se comprueba por PROPIEDAD y en los dos sentidos: todo tipo canónico que el corpus
    declara con bloques tiene que tener recuento derivado, y todo recuento derivado tiene
    que estar publicado en la tabla.
    """
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T271", "Todo bloque tipado del corpus tiene recuento derivado y publicado")
    cuenta = derivar(base)
    if "perfiles_de_agente" not in cuenta:
        r.fallo("no se deriva `perfiles_de_agente`: el censo de `N-04` volvería a la prosa "
                "(`11-ARQ` §19, CONTRATO 1bis)")
    # Todo tipo canónico DECLARADO POR UN ESQUEMA del árbol tiene que tener censo. El
    # conjunto de tipos se descubre; no se enumera aquí ni en `derivar`.
    lint = Lint(base, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    for tipo in sorted(lint.esquemas):
        clave = NOMBRE_DEL_TIPO.get(tipo, "bloques_" + tipo.replace("-", "_"))
        esperado = len([1 for tt, _d, _r, _l in lint.bloques if tt == tipo])
        if clave not in cuenta:
            r.fallo(f"el esquema declara el tipo `ads:{tipo}` y ninguna cifra derivada lo "
                    f"cuenta: un tipo tipado sin censo es `N-04` otra vez")
        elif cuenta[clave] != esperado:
            r.fallo(f"`{clave}` deriva {cuenta[clave]} y el corpus tiene {esperado} "
                    f"bloques `ads:{tipo}`")
    tabla = os.path.join(base, "kernel/operativo/pruebas/RECUENTOS-generado.md")
    if not os.path.exists(tabla):
        r.fallo("no existe `pruebas/RECUENTOS-generado.md`: la cifra viviría sólo en prosa")
        return r
    with open(tabla, encoding="utf-8") as fh:
        publicado = fh.read()
    for clave, valor in sorted(cuenta.items()):
        fila = f"| {clave.replace('_', ' ')} | **{valor}** |"
        if fila not in publicado:
            r.fallo(f"`RECUENTOS-generado.md` no publica «{clave} = {valor}»: la cifra "
                    f"derivada no llega a ninguna sede legible. Regenera con "
                    f"`comprobar_recuentos.py --generar`")
    return r


# ===========================================================================
#  LAS DOS CABECERAS QUE AFIRMABAN UN RECUENTO FALSO — `F-10` y `F-11`
# ===========================================================================
#  `06-DEUDA` §7 las resume así: los hallazgos externos con propietario y fase alcanzan
#  «a dos cabeceras que afirman recuentos falsos». Aquí se cierran por PROPIEDAD y no por
#  redacción: la primera deriva los dos cardinales y prohíbe la biyección MIENTRAS
#  difieran; la segunda deriva del propio fichero qué pruebas contiene y exige que la
#  cabecera nombre ésas y no otras.

# Formulaciones de la BIYECCIÓN entre formas de conversación y clases de expresión. Se
# declaran una a una y con su motivo: la aposición «uno por clase de expresión» era falsa
# por catorce contra nueve (`11-ARQ` §19, `F-10`).
# El salto de línea y la marca de cita del Markdown se toleran: una aposición no deja de
# afirmarse porque el párrafo se envuelva.
_HUECO = r"[\s>]+"
BIYECCIONES_PROHIBIDAS = [
    r"uno" + _HUECO + r"por" + _HUECO + r"clase" + _HUECO + r"de" + _HUECO + r"expresi[oó]n",
    r"una" + _HUECO + r"por" + _HUECO + r"clase" + _HUECO + r"de" + _HUECO + r"expresi[oó]n",
    r"uno" + _HUECO + r"por" + _HUECO + r"cada" + _HUECO + r"clase" + _HUECO + r"de" + _HUECO + r"expresi[oó]n",
    r"una" + _HUECO + r"por" + _HUECO + r"cada" + _HUECO + r"clase" + _HUECO + r"de" + _HUECO + r"expresi[oó]n",
]
DONDE_SE_AFIRMABA = [
    "kernel/operativo/entrada/03-FORMAS.md",
    "kernel/operativo/entrada/00-INDICE.md",
    "kernel/operativo/entrada/01-TAXONOMIA.md",
    "kernel/operativo/00-INDICE.md",
]


def t245_ninguna_cabecera_afirma_una_biyeccion_falsa(raiz=None):
    """`F-10`. La aposición sólo es falsa cuando se predica de las FORMAS.

    `01-TAXONOMIA.md` dice «uno por clase de expresión» de los bloques `ads:entrada`, y
    ahí es CIERTO: hay una clase de entrada por clase de expresión. Lo que era falso es
    predicarlo de las catorce formas de conversación. La regla mira la frase que contiene
    la aposición, no el fichero entero: prohibir la formulación en abstracto habría
    borrado una verdad para tapar una mentira.
    """
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T245", "Ninguna cabecera afirma una correspondencia uno a uno entre formas y clases")
    cuenta = derivar(base)
    formas, clases = cuenta.get("formas_de_conversacion"), cuenta.get("clases_de_entrada")
    if formas is None or clases is None:
        r.fallo("no se derivan las formas de conversación o las clases de expresión")
        return r
    if formas == clases:
        # La regla se APAGA sola si algún día los dos cardinales coinciden: entonces la
        # aposición dejaría de ser falsa y prohibirla sería censurar una verdad.
        return r
    for rel in DONDE_SE_AFIRMABA:
        ruta = os.path.join(base, rel)
        if not os.path.exists(ruta):
            continue
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        for patron in BIYECCIONES_PROHIBIDAS:
            for m in re.finditer(patron, texto, re.I):
                linea = texto[:m.start()].count("\n") + 1
                # La FRASE que contiene la aposición, acotada por su puntuación. Ampliar la
                # ventana a un número fijo de caracteres metía dentro la frase siguiente, y
                # con ella su negación: la regla se apagaba sola sobre la infracción.
                abre = max(texto.rfind(".", 0, m.start()),
                           texto.rfind("\n\n", 0, m.start())) + 1
                cierra = texto.find(".", m.end())
                frase = texto[abre:(cierra + 1) if cierra != -1 else m.end() + 80]
                if not re.search(r"forma-conversacion|formas de conversaci[oó]n", frase, re.I):
                    continue          # se predica de otra cosa, y de otra cosa puede ser cierto
                if re.search(r"\bNo hay\b|era falsa|deja de afirmar", frase, re.I):
                    continue          # la cita que DESMIENTE la aposición, no la afirma
                r.fallo(f"{rel}:{linea}: afirma «{m.group(0)}» de las formas de "
                        f"conversación, y hay {formas} formas frente a {clases} clases de "
                        f"expresión. La aposición es falsa (`11-ARQ` §19, `F-10`)")
    return r


def _rangos(texto):
    """Los identificadores `Tnn` que un texto cita, con los rangos EXPANDIDOS.

    `T75`–`T80` cita seis pruebas y escribe dos. Comparar sólo los extremos daría por
    enumerada una cabecera que se salta lo de en medio.
    """
    limpio = re.sub(r"\]\([^)]*\)", "]", texto)          # fuera los destinos de enlace
    citados, consumidos = set(), []
    for m in re.finditer(r"T(\d{2,3})\s*[`*]*\s*[–—-]\s*[`*]*\s*T(\d{2,3})", limpio):
        a, b = int(m.group(1)), int(m.group(2))
        if a <= b:
            citados |= set(range(a, b + 1))
        consumidos.append(m.span())
    for m in re.finditer(r"T(\d{2,3})", limpio):
        if any(ini <= m.start() < fin for ini, fin in consumidos):
            continue
        citados.add(int(m.group(1)))
    return citados


def t246_la_cabecera_enumera_las_pruebas_que_contiene(raiz=None):
    """`F-11`."""
    base = os.path.abspath(raiz or RAIZ)
    r = Resultado("T246", "La cabecera de los escenarios enumera las pruebas que el fichero contiene")
    rel = "kernel/operativo/entrada/05-ESCENARIOS.md"
    ruta = os.path.join(base, rel)
    if not os.path.exists(ruta):
        r.fallo(f"{rel}: no existe, y es donde vive la cabecera que `F-11` corrige")
        return r
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    contenidas = {int(x) for x in re.findall(r"^id:\s*T(\d{2,3})\s*$", texto, re.M)}
    if not contenidas:
        r.fallo(f"{rel}: no contiene ningún bloque con `id: T…`")
        return r
    cabecera = texto.split("\n---\n", 1)[0]
    # Lo que la cabecera declara EXPRESAMENTE que vive en OTRO fichero no se cuenta como
    # citado, y además se comprueba: si está aquí, la cabecera miente por el otro lado.
    fuera = set()
    for m in re.finditer(r"([^.\n]*NO están aquí)", cabecera):
        fuera |= _rangos(m.group(1))
    citadas = _rangos(cabecera) - fuera
    for ident in sorted(citadas - contenidas):
        r.fallo(f"{rel}: la cabecera nombra T{ident} y el fichero NO lo contiene "
                f"(`11-ARQ` §19, `F-11`)")
    for ident in sorted(contenidas - citadas):
        r.fallo(f"{rel}: el fichero contiene T{ident} y la cabecera no lo enumera "
                f"(`11-ARQ` §19, `F-11`)")
    for ident in sorted(fuera & contenidas):
        r.fallo(f"{rel}: la cabecera declara que T{ident} NO está aquí, y sí está")
    return r


# Las pruebas de este validador, en UNA sede. `registro_pruebas.py` y `registrar_evidencia`
# leen de aquí: una prueba nueva entra en la corrida por existir en esta lista, y no por que
# alguien se acuerde de añadirla al `main`.
PRUEBAS = [t151_recuentos_derivados,
           t270_la_cobertura_de_sedes_se_descubre,
           t271_todo_recuento_derivado_se_publica,
           t245_ninguna_cabecera_afirma_una_biyeccion_falsa,
           t246_la_cabecera_enumera_las_pruebas_que_contiene]


CABECERA = """# RECUENTOS — generado

<!-- GENERADO por validadores/comprobar_recuentos.py. No editar a mano. -->

La fuente canónica de estas cifras **es el corpus**, no este fichero ni ningún otro texto.
Cualquier documento que afirme una distinta hace fallar la prueba T151.

| qué | cuántos |
|---|---|
"""


def generar(base=None):
    base = os.path.abspath(base or RAIZ)
    cuenta = derivar(base)
    filas = "".join(f"| {k.replace('_', ' ')} | **{v}** |\n" for k, v in sorted(cuenta.items()))
    destino = os.path.join(base, "kernel/operativo/pruebas/RECUENTOS-generado.md")
    with open(destino, "w", encoding="utf-8") as fh:
        fh.write(CABECERA + filas)
    return destino, len(cuenta)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=None)
    ap.add_argument("--generar", action="store_true")
    args = ap.parse_args()
    if args.generar:
        destino, n = generar(args.raiz)
        print(f"{n} recuentos · {destino}")
        return 0
    resultados = [f(args.raiz) for f in PRUEBAS]
    if args.json:
        print(json.dumps([{"id": x.id, "nombre": x.nombre,
                           "estado": "prueba-superada" if x.superada else "prueba-fallida",
                           "fallos": x.fallos} for x in resultados], ensure_ascii=False, indent=2))
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
