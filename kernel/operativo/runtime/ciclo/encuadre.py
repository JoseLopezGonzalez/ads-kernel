#!/usr/bin/env python3
"""encuadre — la etapa 1 del ciclo de `§7.2`: qué producto, qué fuentes, qué entrada.

Lo que esta etapa hace, y en este orden, es lo que `§7.2` escribe en su primera fila:
identificar el PRODUCTO · identificar el CONTROL REPO · descubrir los REPOSITORIOS FUENTE ·
cargar el PERFIL y la POLÍTICA · validar las PRECONDICIONES · determinar las CAPACIDADES
NECESARIAS. Y, encima de todo eso, **clasificar la entrada del Owner** en una de las NUEVE
clases de `entrada/01-TAXONOMIA.md`, de las cuales **sólo tres crean trabajo**.

DECISIÓN · la CLASE la DECLARA quien encuadra; el ciclo la VALIDA y aplica la prueba escrita
    Alternativas: (a) deducir la clase del texto del Owner con reglas léxicas; (b) exigir
    que la entrada declare su clase y comprobar, para la única frontera que la taxonomía
    escribe como PRUEBA, que la declaración se sostiene.
    Se elige (b). (a) es la misma patología que `procesos.py` rechaza un piso más abajo:
    con reglas léxicas, «esto ya no se usa» y «esto ya no se utiliza» caerían en clases
    distintas. Lo que sí se aplica —porque el corpus lo escribe como prueba con tres
    casillas, no como impresión— es la FRONTERA entre `idea-inmadura` y `candidato`: si una
    de las tres falla, la clase resultante es `idea-inmadura` **y lo que falla es
    exactamente lo que hay que madurar**, que es lo que dice la taxonomía. No es
    clasificación por texto: es la comprobación estructural de tres campos declarados.

DECISIÓN · las TRES clases que crean trabajo se DERIVAN del corpus
    `crea_item != "nunca"`. No se escriben aquí. La regla 2 de la taxonomía dice «salvo las
    tres que lo declaran explícitamente abajo», y «lo declaran» es literal: está en el
    campo `crea_item` de cada bloque `ads:entrada`. Una prueba comprueba que son tres.

DECISIÓN · el encuadre NO guarda el `remote` de ninguna fuente
    `SOURCES.toml` declara identidad Git y `C6` prohíbe que lleve credenciales, pero una
    credencial puesta por error no puede además acabar en el estado canónico, que se
    publica, se versiona y se firma. El encuadre guarda `id` y `path` —lo único que hace
    falta para saber qué hay que materializar— y un booleano que dice si el remoto está
    declarado. Es la misma línea que `tooling/workspace.py` traza con `redactar()`, movida
    un paso antes: lo que no se copia no se puede filtrar.

DECISIÓN · el encuadre es DURABLE y se escribe por el motor, en su propio dominio
    `canonico/encuadres/<id>.json`. No hay fichero propio, no hay caché y no hay segunda
    sede: `§7.1` dice que lo que el runtime decide vale cuando está escrito. El
    identificador se DERIVA del contenido (`cid_de_objeto`), sin reloj y sin contador, de
    modo que encuadrar dos veces la misma entrada produce el MISMO encuadre y no un
    segundo.
"""
from __future__ import annotations

import os

from estado.serializacion import cid_de_objeto

from .corpus import CAPACIDADES, Corpus
from .errores import (
    EncuadreIncompleto,
    EntradaNoClasificable,
    EntradaSinTrabajo,
    PrecondicionIncumplida,
)
from .procesos import (
    ESTADOS_DEL_OBJETO,
    MATERIAS,
    capacidad_de,
    proceso_de,
    productora_de,
)

try:                                                     # pragma: no cover - 3.11+
    import tomllib
except ModuleNotFoundError:                              # pragma: no cover - 3.10 y antes
    tomllib = None

DOMINIO = "encuadres"
MANIFIESTO = "SOURCES.toml"
PERFIL = "PROFILE.md"
PROYECTO = "PROJECT.md"
ESQUEMA = "ads.estado/1"

# Los campos que un encuadre DEBE traer para que se pueda componer una ruta con él. Es la
# lista de `handoff:enc-a-dsp`: sin ellos DSP devuelve a ENC, y ésa es la razón de que la
# comprobación viva aquí y no en `rutas.py`.
CAMPOS_DE_ENTRADA = ("clase", "expresion_literal", "canal")

# Las tres casillas de la PRUEBA ESCRITA de la frontera `idea-inmadura` / `candidato`, en
# `entrada/01-TAXONOMIA.md`. Se instancian literalmente.
VERBOS_INSUFICIENTES = ("mejorar", "optimizar", "revisar")


def _redactar(texto):
    """Nunca sale de aquí, pero existe: un remoto se resume, no se transcribe."""
    return "declarado" if texto else "sin declarar"


def clases(corpus=None):
    """Las NUEVE clases de la taxonomía, DERIVADAS del corpus."""
    return (corpus or Corpus()).entradas()


def clases_que_crean_trabajo(corpus=None):
    """Las que declaran `crea_item != nunca`. Regla 2 de la taxonomía, derivada."""
    catalogo = clases(corpus)
    return tuple(sorted(
        identificador for identificador, datos in catalogo.items()
        if str(datos.get("crea_item", "nunca")).strip() != "nunca"
    ))


def clasificar(entrada, *, corpus=None):
    """La clase de la entrada, VALIDADA contra las nueve, con la frontera escrita aplicada.

    Devuelve `(clase, motivo, crea_trabajo, lo_que_falta)`. `lo_que_falta` sólo se llena
    cuando una entrada declarada `candidato` no supera la prueba de tres casillas: entonces
    la clase resultante es `idea-inmadura`, que es lo que la taxonomía manda.
    """
    corpus = corpus or Corpus()
    catalogo = clases(corpus)
    declarada = entrada.get("clase")
    if not isinstance(declarada, str) or not declarada.strip():
        raise EntradaNoClasificable(
            "la entrada no declara su clase; las nueve son: " + ", ".join(sorted(catalogo)),
        )
    identificador = declarada if declarada.startswith("entrada:") else "entrada:" + declarada
    if identificador not in catalogo:
        raise EntradaNoClasificable(
            "clase fuera de la taxonomía: " + repr(declarada) + "; las nueve son: "
            + ", ".join(sorted(catalogo)),
            clase=str(declarada),
        )
    faltan = []
    if identificador == "entrada:candidato":
        faltan = _lo_que_falta_para_ser_candidato(entrada)
        if faltan:
            return (
                "entrada:idea-inmadura",
                "declarada `candidato` y no supera la prueba escrita de la frontera: "
                + ", ".join(faltan),
                False,
                faltan,
            )
    crea = identificador in clases_que_crean_trabajo(corpus)
    return identificador, str(catalogo[identificador].get("que_es", "")).strip(), crea, []


def _lo_que_falta_para_ser_candidato(entrada):
    """Las tres casillas de `01-TAXONOMIA.md`, tal como están escritas."""
    faltan = []
    resultado = str(entrada.get("resultado_perseguido") or "").strip()
    if not resultado:
        faltan.append("el RESULTADO PERSEGUIDO no está escrito en una frase")
    else:
        palabras = [p.strip(".,;:").lower() for p in resultado.split()]
        verbos = [p for p in palabras if p in VERBOS_INSUFICIENTES]
        # La taxonomía prohíbe esos verbos como ÚNICO verbo, no como palabra: se comprueba
        # que haya algún otro verbo, aproximado por «alguna palabra de cuatro letras o más
        # que no sea uno de los tres y no sea la primera». Es la lectura conservadora: ante
        # la duda, IDEA INMADURA, que es la salida que no fabrica trabajo.
        otras = [p for p in palabras if len(p) >= 4 and p not in VERBOS_INSUFICIENTES]
        if verbos and len(otras) < 2:
            faltan.append(
                "el resultado perseguido usa `" + verbos[0] + "` como único verbo"
            )
    evidencias = entrada.get("evidencia_de_cierre")
    if not isinstance(evidencias, list) or not [e for e in evidencias if str(e).strip()]:
        faltan.append("no hay ninguna EVIDENCIA DE CIERRE comprobable escrita")
    if entrada.get("anclaje_terminado") is not True:
        faltan.append("el ANCLAJE no ha terminado: falta saber qué existe y si duplica algo")
    return faltan


# ------------------------------------------------------------------- fuentes
def descubrir_fuentes(ruta_control_repo):
    """Las fuentes de `SOURCES.toml`, sin sus remotos. Lista vacía si no hay manifiesto."""
    manifiesto = os.path.join(ruta_control_repo, MANIFIESTO)
    if not os.path.isfile(manifiesto):
        return {"declarado": False, "fuentes": [], "componentes": [], "motivo":
                "no hay `" + MANIFIESTO + "` en el control repo: un proyecto puede no "
                "tener todavía ninguna fuente, y `C6` lo declara válido"}
    if tomllib is None:
        raise PrecondicionIncumplida(
            "este intérprete no trae `tomllib`, que es estándar desde 3.11, y "
            "`" + MANIFIESTO + "` no se puede leer sin él",
            ruta=MANIFIESTO,
        )
    try:
        with open(manifiesto, "rb") as manejador:
            datos = tomllib.load(manejador)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise PrecondicionIncumplida(
            "`" + MANIFIESTO + "` no se puede leer: " + str(exc).split("\n", 1)[0],
            ruta=MANIFIESTO,
        ) from exc
    fuentes = []
    for entrada in datos.get("sources") or []:
        if not isinstance(entrada, dict) or not entrada.get("id"):
            raise PrecondicionIncumplida(
                "hay una fuente sin `id` en el manifiesto", ruta=MANIFIESTO,
            )
        fuentes.append({
            "id": str(entrada["id"]),
            "path": str(entrada.get("path") or ""),
            "remoto": _redactar(entrada.get("remote")),
        })
    componentes = []
    for entrada in datos.get("components") or []:
        if not isinstance(entrada, dict) or not entrada.get("id"):
            raise PrecondicionIncumplida(
                "hay un componente sin `id` en el manifiesto", ruta=MANIFIESTO,
            )
        componentes.append({
            "id": str(entrada["id"]),
            "source": str(entrada.get("source") or ""),
            "path": str(entrada.get("path") or ""),
        })
    return {
        "declarado": True,
        "schema": int(datos.get("schema") or 0),
        "layout": str((datos.get("workspace") or {}).get("layout") or ""),
        "fuentes": sorted(fuentes, key=lambda f: f["id"]),
        "componentes": sorted(componentes, key=lambda c: c["id"]),
        "motivo": "",
    }


def identificar_producto(ruta_control_repo):
    """El nombre del producto. Del `PROJECT.md` si lo declara; si no, el del control repo.

    Nunca una ruta absoluta: el nombre del directorio es un dato del proyecto, y es lo
    mismo que el motor ya usa para `producto` en el registro de reconciliación.
    """
    proyecto = os.path.join(ruta_control_repo, PROYECTO)
    if os.path.isfile(proyecto):
        with open(proyecto, "r", encoding="utf-8") as manejador:
            for linea in manejador:
                if linea.startswith("# "):
                    nombre = linea[2:].strip()
                    if nombre and "<" not in nombre:
                        return nombre
    return os.path.basename(os.path.abspath(ruta_control_repo)) or "control-repo"


def cargar_perfil(ruta_control_repo):
    """El `PROFILE`, por su presencia y su huella. NO se interpreta su contenido aquí."""
    perfil = os.path.join(ruta_control_repo, PERFIL)
    if not os.path.isfile(perfil):
        return {"declarado": False, "huella": None,
                "motivo": "no hay `" + PERFIL + "`: el saber hacer no está declarado y "
                          "toda capacidad trabaja con el kernel a secas"}
    with open(perfil, "rb") as manejador:
        contenido = manejador.read()
    return {
        "declarado": True,
        "huella": cid_de_objeto({"fichero": PERFIL,
                                 "bytes": contenido.decode("utf-8", "replace")}),
        "motivo": "",
    }


def cargar_politica():
    """La tabla de propiedad de `g.14`, ya validada por `gobierno.propiedad`."""
    import gobierno
    politica = gobierno.cargar_politica()
    return {
        "operaciones": list(politica.operaciones()),
        "publicacion_por_defecto": "esperando-owner",
        "digest": politica.digest,
    }


# ---------------------------------------------------------------- capacidades
def capacidades_necesarias(proceso):
    """Las capacidades que el proceso puede necesitar: obligatorias más condicionales.

    Se DERIVAN del bloque `ads:proceso`, y se devuelven como CAPACIDADES —`DOM`, no
    `DOM:condiciones`—, porque lo que se materializa por `C4` es una capacidad y no un
    método. La lista es el universo de lo POSIBLE; cuáles se activan lo decide `rutas.py`.
    """
    salida = set()
    for obligacion in proceso.get("obligatorias") or []:
        productora = capacidad_de(productora_de(obligacion))
        if productora in CAPACIDADES:
            salida.add(productora)
    for condicional in proceso.get("condicionales") or []:
        capacidad = capacidad_de(condicional["capacidad"])
        if capacidad in CAPACIDADES:
            salida.add(capacidad)
    propietario = capacidad_de(str(proceso.get("propietario_global") or "").split(",")[0])
    if propietario in CAPACIDADES:
        salida.add(propietario)
    return tuple(sorted(salida))


# ------------------------------------------------------------------ encuadrar
def encuadrar(ruta_control_repo, entrada, *, corpus=None, precondiciones=()):
    """El objeto `encuadre` DURABLE de `§7.2`. No escribe: lo escribe `planificacion.py`."""
    corpus = corpus or Corpus()
    if not isinstance(entrada, dict):
        raise EncuadreIncompleto("la entrada del Owner es un mapa de campos declarados")
    faltan = [campo for campo in CAMPOS_DE_ENTRADA if not str(entrada.get(campo) or "").strip()]
    if faltan:
        raise EncuadreIncompleto(
            "la entrada no declara " + ", ".join(faltan) + "; la regla 1 de la taxonomía "
            "exige conservar la expresión literal con su fecha y su canal",
        )
    if not os.path.isdir(ruta_control_repo):
        raise PrecondicionIncumplida(
            "el control repo no existe como directorio", ruta=ruta_control_repo,
        )

    clase, que_es, crea_trabajo, lo_que_falta = clasificar(entrada, corpus=corpus)
    fuentes = descubrir_fuentes(ruta_control_repo)
    perfil = cargar_perfil(ruta_control_repo)
    politica = cargar_politica()

    incumplidas = [str(p) for p in precondiciones if not _precondicion_cumplida(p, entrada)]
    if incumplidas:
        raise PrecondicionIncumplida(
            "precondiciones declaradas que no se cumplen: " + ", ".join(sorted(incumplidas)),
            precondiciones=sorted(incumplidas),
        )

    proceso_id = None
    capacidades = ()
    if crea_trabajo:
        materia = entrada.get("materia")
        estado_del_objeto = entrada.get("estado_del_objeto")
        if materia is None or estado_del_objeto is None:
            raise EncuadreIncompleto(
                "una entrada que crea trabajo declara su MATERIA y el ESTADO del objeto; "
                "materias: " + ", ".join(MATERIAS) + "; estados: "
                + ", ".join(ESTADOS_DEL_OBJETO),
            )
        proceso_id = proceso_de(materia, estado_del_objeto, corpus=corpus)
        capacidades = capacidades_necesarias(corpus.proceso(proceso_id))

    cuerpo = {
        "esquema": ESQUEMA,
        "producto": identificar_producto(ruta_control_repo),
        "control_repo": "control",
        "clase": clase,
        "que_es": que_es,
        "crea_trabajo": bool(crea_trabajo),
        "lo_que_falta_para_madurar": list(lo_que_falta),
        "expresion_literal": str(entrada["expresion_literal"]),
        "canal": str(entrada["canal"]),
        "fecha_declarada": str(entrada.get("fecha") or ""),
        "interpretacion": str(entrada.get("interpretacion") or ""),
        "resultado_perseguido": str(entrada.get("resultado_perseguido") or ""),
        "evidencia_de_cierre": [str(e) for e in (entrada.get("evidencia_de_cierre") or [])],
        "anclaje_terminado": bool(entrada.get("anclaje_terminado")),
        "materia": str(entrada.get("materia") or ""),
        "estado_del_objeto": str(entrada.get("estado_del_objeto") or ""),
        "proceso": proceso_id,
        "capacidades_necesarias": list(capacidades),
        "fuentes": fuentes,
        "perfil": perfil,
        "politica": politica,
        "precondiciones_comprobadas": sorted(str(p) for p in precondiciones),
        "huella_del_corpus": corpus.huella(),
    }
    cuerpo["id"] = identificador(cuerpo)
    return cuerpo


def _precondicion_cumplida(precondicion, entrada):
    """Una precondición es el nombre de un hecho que la entrada DECLARA cumplido."""
    declarados = entrada.get("precondiciones_cumplidas") or []
    return str(precondicion) in [str(d) for d in declarados]


def identificador(cuerpo):
    """`enc-<16 hex>` derivado del CONTENIDO. Sin reloj, sin contador, sin pid (`I-g3`)."""
    sin_id = {clave: valor for clave, valor in cuerpo.items() if clave != "id"}
    digest = cid_de_objeto(sin_id)
    return "enc-" + digest.split(":", 1)[-1][:16]


def ruta_de(identificador_de_encuadre):
    return DOMINIO + "/" + identificador_de_encuadre + ".json"


def exigir_que_crea_trabajo(encuadre):
    """Seis de las nueve clases se registran y esperan. Componer con una de ellas es error."""
    if not encuadre.get("crea_trabajo"):
        raise EntradaSinTrabajo(
            "la clase `" + str(encuadre.get("clase")) + "` NO crea trabajo por sí misma "
            "(regla 2 de la taxonomía): se registra, se ancla y espera",
            clase=str(encuadre.get("clase")),
        )
    return encuadre
