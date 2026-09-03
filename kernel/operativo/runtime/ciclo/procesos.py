#!/usr/bin/env python3
"""procesos — `b.16` DERIVADO del corpus, y la correspondencia MATERIA → PROCESO.

    «El proceso lo determina el RESULTADO PERSEGUIDO por el item, no las capacidades que
     se usan para obtenerlo» — `b.1`, primera línea de `recorrido/01-PROCESOS.md`

Este módulo no guarda una copia de los diez procesos: los lee de los bloques
`ads:proceso` con `corpus.Corpus`. Lo único que vive aquí como DATO es lo que el corpus no
puede dar por sí solo: **cómo se decide cuál de los diez le toca a un encuadre**.

DECISIÓN · la selección es por MATERIA y ESTADO DECLARADOS, y NUNCA por texto libre
    Alternativas: (a) buscar palabras en el título o en la expresión del Owner —«bug»,
    «lento», «no existe»— y elegir el proceso que más case; (b) exigir que el ENCUADRE
    declare una MATERIA de un vocabulario CERRADO y un ESTADO del objeto, y aplicar una
    tabla declarada.
    Se elige (b), y (a) queda PROHIBIDA. Con (a) renombrar un item cambia su proceso, un
    sinónimo activa una ruta que nadie pidió, y dos encuadres idénticos en sustancia caen
    en procesos distintos según cómo se redactaron. `b.1` dice que el proceso lo determina
    el RESULTADO PERSEGUIDO: el resultado perseguido es una declaración del encuadre, no
    una propiedad estadística de su prosa. `test_ciclo.py` lo prueba por los dos lados:
    renombrar el título no mueve la ruta, y un sinónimo en la expresión literal no activa
    ninguna.

DECISIÓN · la tabla es `(materia, estado)` y no sólo `materia`
    `§7.2` dice «determina el PROCESO por el resultado perseguido (b.1)», y `b.1` distingue
    `FEA` de `GAP` exactamente por el ESTADO del objeto: en `FEA` **no existe todavía**, en
    `GAP` **existe y no llega**. Con una tabla de una sola columna esas dos rutas serían
    indistinguibles y habría que desempatar leyendo prosa, que es lo que (a) hacía.

DECISIÓN · la MATERIA se valida contra el corpus, no contra esta tabla
    Cada fila declara el `id` del proceso, y `exigir_coherente()` comprueba contra los
    procesos DERIVADOS que (i) todo proceso de la tabla existe en `b.16` y (ii) todo
    proceso de `b.16` es alcanzable por alguna materia. Un proceso inalcanzable es una ruta
    que el corpus declara y el runtime nunca podría componer, y eso no se descubre solo.
"""
from __future__ import annotations

from .corpus import CONDICIONES_DE_B16, Corpus
from .errores import (
    CicloInconsistente,
    CondicionVaga,
    EstadoDeMateriaInvalido,
    MateriaSinProceso,
    ObligacionSinProductora,
    ProcesoDesconocido,
)

# Los TRES estados del objeto sobre el que se trabaja. Cerrado.
NO_EXISTE = "no-existe"
EXISTE = "existe"
EN_USO_REAL = "en-uso-real"
ESTADOS_DEL_OBJETO = (NO_EXISTE, EXISTE, EN_USO_REAL)

# La CORRESPONDENCIA DECLARADA. Cada fila: materia → (proceso, estados admisibles, por qué).
# El «por qué» cita la `intencion` o la `condicion_de_entrada` del proceso, que es lo que
# la fila instancia; `exigir_coherente()` comprueba que el `id` existe de verdad.
CORRESPONDENCIA = {
    "capacidad-ausente": {
        "proceso": "proceso:FEA",
        "estados": (NO_EXISTE,),
        "motivo": "introducir una capacidad o un comportamiento que el producto NO tenía",
    },
    "expectativa-no-alcanzada": {
        "proceso": "proceso:GAP",
        "estados": (EXISTE, EN_USO_REAL),
        "motivo": "existe algo, y no llega a lo que se esperaba de ello",
    },
    "comportamiento-especificado-roto": {
        "proceso": "proceso:DEF",
        "estados": (EXISTE, EN_USO_REAL),
        "motivo": "algo especificado no hace lo que su especificación dice",
    },
    "incidente-en-uso-real": {
        "proceso": "proceso:INC",
        "estados": (EN_USO_REAL,),
        "motivo": "algo falla en uso real, con impacto observable",
    },
    "conocimiento-ausente": {
        "proceso": "proceso:INV",
        "estados": (NO_EXISTE, EXISTE, EN_USO_REAL),
        "motivo": "existe una decisión que no puede tomarse porque falta evidencia",
    },
    "forma-interna-costosa": {
        "proceso": "proceso:DEU",
        "estados": (EXISTE, EN_USO_REAL),
        "motivo": "algo funciona y su forma interna encarece o arriesga lo que venga",
    },
    "dependencia-externa": {
        "proceso": "proceso:DEP",
        "estados": (NO_EXISTE, EXISTE, EN_USO_REAL),
        "motivo": "una dependencia externa entra, cambia de versión o sale",
    },
    "conclusion-sobre-lo-existente": {
        "proceso": "proceso:AUD",
        "estados": (EXISTE, EN_USO_REAL),
        "motivo": "hace falta saber en qué estado está algo que ya existe",
    },
    "direccion-ya-decidida": {
        "proceso": "proceso:DIR",
        "estados": (EXISTE, EN_USO_REAL),
        "motivo": "el Owner quiere sustituir una dirección ya decidida",
    },
    "la-propia-fabrica": {
        "proceso": "proceso:SIS",
        "estados": (NO_EXISTE, EXISTE, EN_USO_REAL),
        "motivo": "cambiar la propia fábrica: memoria, plantillas, catálogo o runtime",
    },
}

MATERIAS = tuple(sorted(CORRESPONDENCIA))

# Formulaciones que `b.16` PROHÍBE en la condición de una capacidad condicional. Se
# comparan en minúsculas y sin acentos por la vía del propio texto, que ya está en
# castellano normalizado en el corpus. La lista se lee del validador de vocabulario, que es
# su sede: aquí sólo se instancia para la vía 3, que es donde el ciclo la aplica.
FORMULAS_VAGAS = (
    "si aplica", "si procede", "cuando corresponda", "cuando proceda",
    "segun el contexto", "según el contexto", "segun convenga", "según convenga",
    "si fuera necesario", "en su caso", "en la medida de lo posible",
    "a criterio del agente", "a juicio del agente", "lo que sea razonable",
)

LONGITUD_MINIMA_DE_CONDICION = 5


def proceso_de(materia, estado_del_objeto, *, corpus=None):
    """El `id` de proceso de `b.16` para una materia y un estado DECLARADOS."""
    if materia not in CORRESPONDENCIA:
        raise MateriaSinProceso(
            "materia fuera del vocabulario cerrado: " + repr(materia) + "; declaradas: "
            + ", ".join(MATERIAS),
            materia=str(materia),
        )
    if estado_del_objeto not in ESTADOS_DEL_OBJETO:
        raise EstadoDeMateriaInvalido(
            "estado del objeto fuera del vocabulario cerrado: " + repr(estado_del_objeto)
            + "; válidos: " + ", ".join(ESTADOS_DEL_OBJETO),
        )
    fila = CORRESPONDENCIA[materia]
    if estado_del_objeto not in fila["estados"]:
        raise EstadoDeMateriaInvalido(
            "la materia `" + materia + "` no admite el estado `" + estado_del_objeto
            + "`; admite: " + ", ".join(fila["estados"]) + ". " + fila["motivo"],
            materia=materia, estado=estado_del_objeto,
        )
    identificador = fila["proceso"]
    if corpus is not None:
        # Se comprueba contra el corpus, no contra esta tabla: la tabla dice cuál toca, el
        # corpus dice cuáles hay, y una tabla que nombra un proceso inexistente es un
        # defecto que tiene que salir aquí y no tres llamadas más tarde.
        corpus.proceso(identificador)
    return identificador


def exigir_coherente(corpus=None):
    """La tabla y `b.16` dicen lo mismo: sin filas huérfanas y sin procesos inalcanzables."""
    corpus = corpus or Corpus()
    declarados = set(corpus.procesos())
    en_tabla = {fila["proceso"] for fila in CORRESPONDENCIA.values()}
    huerfanos = sorted(en_tabla - declarados)
    if huerfanos:
        raise ProcesoDesconocido(
            "la correspondencia nombra procesos que `b.16` no declara: "
            + ", ".join(huerfanos),
        )
    inalcanzables = sorted(declarados - en_tabla)
    if inalcanzables:
        raise CicloInconsistente(
            "hay procesos de `b.16` que ninguna materia puede alcanzar: "
            + ", ".join(inalcanzables) + "; una ruta declarada que el runtime nunca "
            "compondría es una ruta muerta",
            inalcanzables=inalcanzables,
        )
    return tuple(sorted(declarados))


# --------------------------------------------------------------- obligaciones
def productora_de(entrada):
    """QUIÉN produce la capa: una CAPACIDAD, o la AUTORIDAD declarada en su campo propio.

    `F-02` punto 5 es literal: «`OWNER` NO es una capacidad: se separa como AUTORIDAD, en su
    propio campo, porque las quince no lo incluyen», y su remedio dice **MOVER** `OWNER` a
    autoridad, no duplicarlo. Una obligación producida por el Owner declara
    `autoridad_productora` y NO declara `capacidad_productora`: dejar el token viejo en el
    campo de capacidad habría conservado exactamente lo que `F-02` existe para retirar.

    Éste es el ÚNICO punto que resuelve la pareja. Los consumidores preguntan por la
    productora y no tienen que conocer las dos claves, que es lo que hacía que el token
    viejo fuese imposible de quitar sin romperlos.
    """
    capacidad = entrada.get("capacidad_productora")
    if capacidad is not None and str(capacidad).strip():
        return str(capacidad)
    autoridad = entrada.get("autoridad_productora")
    if autoridad is not None and str(autoridad).strip():
        return str(autoridad)
    raise ObligacionSinProductora(
        "la obligación `" + str(entrada.get("id")) + "` no declara ni "
        "`capacidad_productora` ni `autoridad_productora`; el esquema exige exactamente "
        "una de las dos y sin ninguna no se sabe quién produce la capa",
        obligacion=str(entrada.get("id")),
    )


def obligaciones_de(proceso):
    """Las obligaciones del proceso, DERIVADAS de sus `obligatorias` (`00-OBLIGACIONES`)."""
    salida = []
    for entrada in proceso.get("obligatorias") or []:
        salida.append({
            "id": entrada["id"],
            "capa_exigida": entrada["capa_exigida"],
            # Las DOS claves viajan tal como el corpus las declara —una de ellas ausente—,
            # y `productora` resuelve cuál manda. Nada las mezcla en un solo campo.
            "capacidad_productora": entrada.get("capacidad_productora"),
            "autoridad_productora": entrada.get("autoridad_productora"),
            "productora": productora_de(entrada),
            "criterio_de_satisfaccion": entrada["criterio_de_satisfaccion"],
            "autoridad_de_retirada": entrada["autoridad_de_retirada"],
            "estado": "huerfana",
        })
    return salida


def condicionales_de(proceso):
    """Las capacidades condicionales del proceso, con su condición TAL COMO está escrita."""
    return [
        {"capacidad": entrada["capacidad"], "condicion": entrada["condicion"]}
        for entrada in (proceso.get("condicionales") or [])
    ]


def comprobar_condicion(condicion, *, capacidad):
    """La condición de la vía 3: del vocabulario de `b.16`, o propia y REDACTADA."""
    if not isinstance(condicion, str) or not condicion.strip():
        raise CondicionVaga(
            "la capacidad condicional `" + str(capacidad) + "` no declara condición",
            capacidad=str(capacidad),
        )
    limpia = condicion.strip()
    if limpia in CONDICIONES_DE_B16:
        return limpia
    minuscula = limpia.lower()
    for formula in FORMULAS_VAGAS:
        if formula in minuscula:
            raise CondicionVaga(
                "la condición de `" + str(capacidad) + "` usa una fórmula vaga que `b.16` "
                "prohíbe; escribe la condición comprobable",
                capacidad=str(capacidad), formula=formula,
            )
    if len(limpia) < LONGITUD_MINIMA_DE_CONDICION:
        raise CondicionVaga(
            "la condición propia de `" + str(capacidad) + "` es demasiado corta para ser "
            "comprobable por alguien que no la escribió",
            capacidad=str(capacidad),
        )
    return limpia


# ------------------------------------------------------ capacidad y método
def capacidad_de(participante):
    """`DOM:condiciones` → `DOM`; `DIS/Reconstruccion` → `DIS`; `CON` → `CON`.

    El corpus escribe los participantes condicionales como `CAPACIDAD:metodo` o
    `CAPACIDAD/Metodo` cuando la condición activa un método concreto. Lo que entra en la
    ruta —y lo que `C4` materializa— es la CAPACIDAD; el método es CÓMO trabaja, y `C1` los
    separa. Confundirlos es el modo de fallo que `metodo_de` documenta.
    """
    if not isinstance(participante, str) or not participante.strip():
        raise CicloInconsistente("un participante sin nombre no es un participante")
    texto = participante.strip()
    for separador in (":", "/"):
        if separador in texto:
            texto = texto.split(separador, 1)[0]
    return texto.strip()


def metodo_de(participante):
    """El MÉTODO que el participante nombra, o `None`. NUNCA se usa como capacidad."""
    if not isinstance(participante, str):
        return None
    for separador in (":", "/"):
        if separador in participante:
            return participante.split(separador, 1)[1].strip() or None
    return None
