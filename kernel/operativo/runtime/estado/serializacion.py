#!/usr/bin/env python3
"""serializacion — bytes deterministas e identidad por contenido.

Dos formas, y son DOS a propósito (§2.1):

    CANÓNICA   `sort_keys=True, ensure_ascii=False, indent=2` + salto final.
               Es la forma de los ficheros de `canonico/`, de `REVISION.json` y de
               `FORMATO.json`. Se elige indentada porque `I-g1` exige que el estado
               canónico sea LEGIBLE SIN HERRAMIENTA: se abre el fichero y se sabe el
               estado. Un JSON compacto de una línea cumpliría la letra y traicionaría el
               propósito.

    COMPACTA   `separators=(",", ":")`, una línea. Es la forma de transporte del diario y
               del registro auxiliar, que son JSONL append-only: una línea por evento, y
               el salto de línea es el delimitador de registro. Indentar ahí rompería el
               formato, no lo embellecería.

DECISIÓN · la IDENTIDAD se calcula SIEMPRE sobre la forma canónica
    Alternativas: (a) `cid` de los bytes tal como se transportan —canónicos para el estado,
    compactos para el diario—; (b) `cid` siempre de la forma canónica.
    Se elige (b). Con (a), la huella de un evento dependería de su envoltorio de transporte:
    mover un evento de JSONL a un fichero indentado, o al revés, cambiaría su identidad sin
    cambiar su contenido, y `g.5` dice que la identidad se deriva DEL CONTENIDO y de nada
    más. Con (b) la cadena de hash del diario sigue siendo verificable aunque el formato
    concreto del diario cambie —y `g.17` lo declara CALIBRABLE, así que va a cambiar—.
    Para los ficheros de `canonico/` ambas opciones coinciden, porque allí la forma de
    transporte YA es la canónica: `cid(bytes del fichero) == cid_de_objeto(contenido)`.

DECISIÓN · `ensure_ascii=False` y por tanto UTF-8 explícito en todas partes
    El corpus de ADS está en castellano y lleva tildes y eñes. Con `ensure_ascii=True` el
    estado canónico se llenaría de `\\u00f3` y dejaría de ser legible sin herramienta,
    otra vez contra `I-g1`. El precio es que toda lectura y escritura declara
    `encoding="utf-8"`: nunca se confía en la codificación por defecto del sistema, que en
    otra máquina produciría bytes distintos para el mismo estado y rompería `I-g3`.

Nada de este módulo mira el reloj, el pid ni un contador de ejecución: mismos datos, bytes
idénticos, en cualquier máquina y en cualquier ejecución (`I-g3`).
"""
from __future__ import annotations

import hashlib
import json

from .errores import EstadoCorrupto, VersionDesconocida

VERSION_DE_ESQUEMA = 1
ESQUEMA = "ads.estado/" + str(VERSION_DE_ESQUEMA)
PREFIJO_ESQUEMA = "ads.estado/"
CLAVE_ESQUEMA = "esquema"


def serializar_canonico(objeto):
    """Bytes canónicos: legibles, ordenados, con salto final. Deterministas."""
    texto = json.dumps(objeto, sort_keys=True, ensure_ascii=False, indent=2)
    return (texto + "\n").encode("utf-8")


def serializar_compacto(objeto):
    """Bytes de una sola línea, para JSONL. SIN salto final: lo pone el anexador."""
    texto = json.dumps(objeto, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return texto.encode("utf-8")


def deserializar(datos, ruta=None, error=EstadoCorrupto):
    """Bytes → objeto, con fallo CERRADO ante JSON roto, truncado o mal codificado.

    `g.5` exige que toda corrupción o truncamiento se DETECTE al leer. `json.loads` sobre
    un fichero cortado por la mitad levanta `JSONDecodeError`, y sobre bytes que no son
    UTF-8 levanta `UnicodeDecodeError`; ninguna de las dos se deja escapar como excepción
    ajena, porque el llamador tiene que poder distinguir «estado corrupto» de «error de
    programación» sin mirar el traceback.
    """
    try:
        texto = datos.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise error("los bytes no son UTF-8 válido: " + str(exc), ruta=ruta) from exc
    try:
        return json.loads(texto)
    except json.JSONDecodeError as exc:
        raise error(
            "JSON ilegible en la posición " + str(exc.pos) + ": " + exc.msg, ruta=ruta
        ) from exc


def cid(datos):
    """`cid(bytes) = "sha256:" + sha256(bytes).hexdigest()` (§2.2).

    Se documenta aquí, y no sólo en el contrato, lo que `g.5` obliga a decir: este digest
    identifica contenido, y **no prueba la integridad del árbol frente a terceros**. Esa
    prueba pertenece a la raíz externa de `g.15`, porque quien puede reescribir el fichero
    puede reescribir también el digest que él mismo calculó.
    """
    return "sha256:" + hashlib.sha256(datos).hexdigest()


def cid_de_objeto(objeto):
    """Identidad de un objeto durable: el `cid` de su forma CANÓNICA."""
    return cid(serializar_canonico(objeto))


def cid_corto(valor):
    """Los ocho primeros hex de un `cid`, para componer identificadores legibles.

    Ocho hex son 32 bits. NO se usa como identidad —la identidad es el `cid` entero— sino
    como sufijo humano de un identificador de transacción que ya lleva el número de
    revisión delante, y ese par sí es único dentro de un almacén.
    """
    return valor.split(":", 1)[-1][:8]


def calcular_cid_raiz(raiz):
    """`cid_raiz` = `cid` de la lista ORDENADA de pares `[ruta_logica, cid]` (§2.2).

    Ordenada, y por eso reproducible: dos almacenes con el mismo contenido dan el mismo
    `cid_raiz` aunque hayan llegado a él por caminos distintos y en otro orden de escritura.
    Un diccionario JSON también se ordena con `sort_keys`, pero una LISTA DE PARES deja el
    orden explícito en los propios bytes en vez de confiarlo a una opción del serializador.
    """
    pares = [[ruta, raiz[ruta]] for ruta in sorted(raiz)]
    return cid(serializar_canonico(pares))


def calcular_revision_id(revision, padre, cid_raiz, transaccion):
    """`revision_id` = `cid` de `{revision, padre, cid_raiz, transaccion}` (§2.3).

    NO incluye `raiz` completa porque `cid_raiz` ya la resume, ni `diario_secuencia` porque
    ése es un dato de posición y `g.5` prohíbe que la identidad dependa de una posición.
    Incluye `padre`, y eso es lo que convierte la sucesión de revisiones en una CADENA: sin
    él, dos linajes distintos con el mismo árbol tendrían el mismo identificador y
    `detectar_bifurcacion` no podría distinguirlos.
    """
    return cid_de_objeto({
        "revision": revision,
        "padre": padre,
        "cid_raiz": cid_raiz,
        "transaccion": transaccion,
    })


def version_de_esquema(objeto, ruta=None, error=EstadoCorrupto):
    """Extrae el entero `<n>` de `"esquema": "ads.estado/<n>"`. Fallo cerrado si falta."""
    if not isinstance(objeto, dict):
        raise error("el objeto durable no es un mapa JSON", ruta=ruta)
    declarado = objeto.get(CLAVE_ESQUEMA)
    if not isinstance(declarado, str) or not declarado.startswith(PREFIJO_ESQUEMA):
        raise error(
            "el objeto durable no declara `esquema: ads.estado/<n>`; `g.10` no permite "
            "adivinar la versión de un objeto que no la declara",
            ruta=ruta,
        )
    sufijo = declarado[len(PREFIJO_ESQUEMA):]
    if not sufijo.isdigit():
        raise VersionDesconocida(
            "versión de esquema no numérica: " + declarado, ruta=ruta, esquema=declarado
        )
    return int(sufijo)


def comprobar_esquema(objeto, ruta=None, error=EstadoCorrupto):
    """`g.10`: un lector que encuentra una versión que no entiende FALLA CERRADO.

    No hay migración implícita al leer (`g.11`). Aquí no se traduce, no se rellena y no se
    supone: se levanta `VersionDesconocida` y el estado canónico no se toca.
    """
    version = version_de_esquema(objeto, ruta=ruta, error=error)
    if version != VERSION_DE_ESQUEMA:
        raise VersionDesconocida(
            "versión de esquema " + str(version) + " desconocida; este motor entiende la "
            + str(VERSION_DE_ESQUEMA) + " y no adivina el resto",
            ruta=ruta,
            encontrada=version,
            soportada=VERSION_DE_ESQUEMA,
        )
    return version


def con_esquema(contenido):
    """Devuelve una COPIA del contenido con `esquema` puesto, sin mutar el original.

    Se copia porque el llamador conserva su diccionario y volvería a usarlo: mutarlo haría
    que aplicar dos veces la misma `Escritura` partiese de entradas distintas, y la
    idempotencia del §9 dejaría de ser comprobable.
    """
    if not isinstance(contenido, dict):
        raise EstadoCorrupto("el contenido de un objeto canónico debe ser un mapa JSON")
    copia = dict(contenido)
    declarado = copia.get(CLAVE_ESQUEMA)
    if declarado is None:
        copia[CLAVE_ESQUEMA] = ESQUEMA
        return copia
    comprobar_esquema(copia)
    return copia
