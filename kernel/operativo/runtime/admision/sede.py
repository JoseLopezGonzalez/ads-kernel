#!/usr/bin/env python3
"""sede — APPEND-ONLY POR ENTRADA CERRADA de la sede canónica del Owner. `V6-12` · `O27` §3.

**ÉSTE ES EL MÓDULO QUE CIERRA `ADJ-B3`**, y conviene decir con precisión qué era el
defecto, porque el remedio equivocado —hacer el prefijo «más largo»— no cierra nada.

    LO QUE FALLABA (`docs/f6/03-GATE-DE-CERTIFICACION-FINAL-20260904.md` §4.3)
    `perimetro._juzgar_append_only` decidía con una sola línea:

        if actual.startswith(anterior): return None

    donde `anterior` eran los bytes de la sede EN SU COMMIT DE NACIMIENTO. El contraste
    era un PREFIJO. Medido byte a byte sobre el árbol candidato: nacimiento 14 395 bytes,
    hoy 42 181; el prefijo protegía el 34,1 % del fichero. `O17`, `O18` y `O19` dentro;
    `O20`…`O26` FUERA. El adjudicador borró `O20`–`O26` ENTERAS, las sustituyó por
    «F6 QUEDA CERTIFICADA SIN CONDICIONES», lo confirmó, y el verificador publicó
    `color=INDETERMINADO · hallazgos=0` con la sede perdiendo dos tercios de su contenido.

    LO QUE **NO** LO CIERRA, y por qué no se hace
    (a) Comparar contra `HEAD` en vez de contra el nacimiento: es una tautología, y ya
        está descartado en `perimetro`.
    (b) Anclar un digest del fichero ENTERO en el árbol: entonces AÑADIR una resolución
        —que es el acto legítimo que la sede existe para permitir— daría ROJO, y el
        guardián se retiraría a la primera resolución nueva. Un control que hay que apagar
        para trabajar deja de estar puesto.
    (c) Alargar el prefijo hasta `HEAD~1`: mueve la frontera, no la suprime. Todo lo
        añadido en la última pasada sigue siendo reescribible, y el ataque se hace en dos
        commits en vez de en uno.
    (d) Enumerar `O17`…`O27` en una lista escrita a mano: caduca en la resolución
        siguiente, y `O28` nacería SIN PROTECCIÓN sin que nadie escribiera una línea. Es
        el defecto que el corpus ya documenta tres veces —`Q-04`, `T-03`, `A2`—.

    LO QUE SÍ LO CIERRA, y es `O27` §3 literal
    «La implementación deberá DERIVAR las entradas cerradas de la sede, CONSERVAR cada una
    BYTE A BYTE y permitir ÚNICAMENTE AÑADIR una nueva entrada completa AL FINAL.»
    Aquí se deriva la lista de entradas de la ESTRUCTURA del documento, cada entrada se
    ancla al COMMIT QUE LA INTRODUJO —leyendo la historia de la ruta, no una tabla—, y el
    juicio compara bloque completo contra bloque completo.

DECISIÓN · las entradas se DERIVAN de la estructura, y el LIBRO se deriva de la HISTORIA
    Alternativas: (a) una constante `ENTRADAS = ("O17", …, "O27")`; (b) derivar los
    identificadores del contenido de HOY; (c) derivar los identificadores y sus bytes
    recorriendo la historia de la ruta, entrada por commit.
    Se elige (c), y (b) sería un agujero abierto: si el término de comparación se deriva
    del fichero actual, quien borra `O20`–`O26` borra a la vez la lista de lo que había
    que conservar, y el juicio se aplica sobre lo que el atacante dejó. Con (c) el LIBRO
    —qué entradas existen, con qué bytes y desde qué commit— vive en la historia de Git,
    que el árbol de trabajo no puede reescribir sin reescribir la historia; y reescribir la
    historia lo caza `lectura.procedencia_de_la_historia`, que ya está puesto por `E-09`.

DECISIÓN · el DELIMITADOR entre entradas NO es contenido de ninguna de las dos
    Es `O27` §1 aplicado a la mecánica: «era un delimitador externo del encargo y NO
    formaba parte del texto resolutivo». Y no es una sutileza teórica: MEDIDO sobre la
    historia real de la sede, la última entrada de cada commit gana EXACTAMENTE 6 bytes
    —`\\n---\\n\\n`— cuando la siguiente se inscribe encima.

        1d3b5d41  PREAMBULO,O17,O18,O19        O19 = 3 118 bytes
        7aeed6aa  +O20                         O19 = 3 124 bytes   (+6)
        07a6975e  +O21                         O20 = 5 220 → 5 226 (+6)
        …y así las ocho inscripciones

    Un juicio que tratara el delimitador como contenido daría ROJO sobre la sede REAL,
    intacta, en cuanto se inscribiera la resolución siguiente: un falso rojo garantizado,
    que es la forma más rápida de que un guardián se acabe apagando. El delimitador se
    reconoce, se separa y NO se compara; lo que se compara es el TEXTO RESOLUTIVO.

DECISIÓN · el delimitador se EXIGE, y no se «tolera lo que haya entre dos entradas»
    Alternativas: (a) recortar del final de cada bloque cualquier cosa que se parezca a un
    separador; (b) exigir que entre dos entradas esté EXACTAMENTE el delimitador declarado.
    Se elige (b). Con (a) el hueco entre dos resoluciones se convierte en una zona franca
    donde se puede escribir texto que ningún bloque reclama —y una sede del Owner con
    prosa que nadie firma es exactamente lo que `O19` creó esta sede para impedir—. Con
    (b) cualquier byte insertado ahí pertenece al bloque anterior y produce
    `ENTRADA_ALTERADA`, o rompe la estructura y produce `ESTRUCTURA_ILEGIBLE`.

DECISIÓN · los campos de forma se exigen SÓLO a las entradas NUEVAS
    Es `O27` §2 literal: los campos «son exigibles prospectivamente» y «no se insertarán
    retroactivamente dentro de `O23`, `O24`, `O25` ni `O26`». Una comprobación de forma
    aplicada a las entradas del LIBRO pondría en rojo resoluciones ya emitidas y empujaría
    a editarlas, que es justo lo que `O27` §2 prohíbe. Aquí la forma se exige a lo que se
    AÑADE —donde todavía se puede escribir bien— y jamás a lo ya inscrito.

DECISIÓN · un identificador repetido es un HALLAZGO, no una excepción de lectura
    `derivar_bloques` es estructural y no juzga: devuelve lo que hay, duplicados incluidos.
    Quien juzga es `juzgar`, y por eso un `O27` duplicado sale como `ENTRADA_DUPLICADA`
    con su causa escrita en vez de como una traza. Una excepción aquí obligaría a quien
    llama a decidir si «no he podido leerlo» es «está bien», que es el modo de fallo que
    `V6-03` y `E-09` cierran en los otros dos canales de este mismo paquete.
"""
from __future__ import annotations

import re

from .errores import SedeIlegible
from .formulas import digest_de_contenido

# ===========================================================================
#  LA FORMA DE LA SEDE. Inicio y final INEQUÍVOCOS de cada entrada.
# ===========================================================================
#  Una entrada EMPIEZA en una línea que, EN COLUMNA CERO, abre un título de nivel 1 con el
#  identificador entre acentos graves y el separador `·`. Es la forma que las once entradas
#  vivas usan sin excepción, y es inequívoca: el `^` en modo multilínea no casa dentro de
#  una línea, y ninguna otra construcción del documento abre nivel 1 después del título.
#
#  Una entrada TERMINA donde empieza la siguiente, MENOS el delimitador estructural. La
#  última termina al final del fichero. No hay marca de cierre que falsificar, y por eso no
#  hay «fin de entrada» que un atacante pueda mover.
CABECERA_DE_ENTRADA = re.compile(rb"(?m)^# `(?P<id>(?P<familia>[A-Z]+)(?P<numero>\d+))` \xc2\xb7 ")

# Los bytes que separan dos entradas. Ni la de arriba ni la de abajo los reclaman.
DELIMITADOR = b"\n---\n\n"

# El bloque anterior a la primera entrada: portada, reglas de la sede y qué NO está en ella.
# Es contenido cerrado como cualquier entrada —se conserva byte a byte— y no lleva número.
PREAMBULO = "PREAMBULO"

# La familia de identificadores de esta sede. Una familia NUEVA no se admite en silencio:
# `juzgar` la denuncia, porque un `P1` colado entre `O27` y `O28` no tiene ni orden ni
# cliquet de numeración que lo gobierne.
FAMILIA_CANONICA = "O"

# `O27` §2 · los campos exigibles PROSPECTIVAMENTE a una entrada NUEVA. Dos, y no seis: son
# los dos que se pueden comprobar mecánicamente sin interpretar el texto. Los otros cuatro
# —procedencia, texto, alcance, relaciones de revisión— no tienen marca sintáctica estable
# en las once entradas vivas, y una comprobación que hay que adivinar produce rojos que
# nadie sabe reparar. Se declara lo que se mide.
CAMPOS_DE_ENTRADA_NUEVA = (
    (rb"(?m)^\*\*Fecha:\*\*", "**Fecha:**"),
    (rb"(?m)^\*\*Autoridad:\*\*", "**Autoridad:**"),
)

# Códigos de infracción. Estables, publicables y distintos entre sí: «la sede cambió» no es
# un diagnóstico, y quien reciba el veredicto tiene que poder decir QUÉ pasó.
ALTERADA = "ENTRADA_ALTERADA"
BORRADA = "ENTRADA_BORRADA"
REORDENADAS = "ENTRADAS_REORDENADAS"
DUPLICADA = "ENTRADA_DUPLICADA"
INSERCION = "INSERCION_NO_AL_FINAL"
SALTO = "SALTO_DE_NUMERACION"
INCOMPLETA = "ENTRADA_INCOMPLETA"
FAMILIA_AJENA = "FAMILIA_DESCONOCIDA"
ESTRUCTURA = "ESTRUCTURA_ILEGIBLE"
HISTORIA = "HISTORIA_INCOHERENTE"


class BloqueCerrado:
    """Una entrada cerrada de la sede: su identificador, sus límites y sus bytes."""

    __slots__ = ("identificador", "familia", "numero", "orden", "inicio", "fin", "contenido")

    def __init__(self, identificador, familia, numero, orden, inicio, fin, contenido):
        self.identificador = identificador
        self.familia = familia
        self.numero = numero
        self.orden = orden
        self.inicio = inicio
        self.fin = fin
        self.contenido = contenido

    @property
    def digest(self):
        return digest_de_contenido(self.contenido)

    def a_dict(self):
        return {
            "identificador": self.identificador,
            "familia": self.familia,
            "numero": self.numero,
            "orden": self.orden,
            "inicio": self.inicio,
            "fin": self.fin,
            "bytes": len(self.contenido),
            "digest": self.digest,
        }

    def __repr__(self):
        return "BloqueCerrado(" + self.identificador + ", " + str(len(self.contenido)) + "B)"


def derivar_bloques(contenido):
    """Deriva las entradas cerradas de unos bytes de sede. ESTRUCTURAL: no juzga.

    Devuelve la lista en el orden en que aparecen, con el `PREAMBULO` primero cuando lo
    hay. Levanta `SedeIlegible` SÓLO cuando la estructura no se puede leer sin adivinar:
    entre dos entradas falta el delimitador declarado. No devolver nunca «lista vacía con
    éxito» ante algo ilegible es la misma regla que `lectura` aplica a las listas de rutas.
    """
    if contenido is None:
        raise SedeIlegible(
            "no hay bytes de sede que derivar. Sin contenido no hay entradas cerradas que "
            "conservar, y una lista vacía no se confunde con una sede intacta",
        )
    cabeceras = list(CABECERA_DE_ENTRADA.finditer(contenido))
    if not cabeceras:
        # Un documento sin ninguna cabecera de entrada es UN solo bloque cerrado. No es un
        # error: es el régimen que corresponde a un texto que no está dividido en entradas,
        # y quien juzgue verá que ese bloque tiene que conservarse entero.
        return [BloqueCerrado(PREAMBULO, None, None, 0, 0, len(contenido), contenido)]

    limites = [m.start() for m in cabeceras] + [len(contenido)]
    bloques = []

    def recortar(bruto, es_ultimo, identificador):
        if bruto.endswith(DELIMITADOR):
            return bruto[: -len(DELIMITADOR)]
        if es_ultimo:
            return bruto
        raise SedeIlegible(
            "entre el final de `" + identificador + "` y la entrada siguiente no está el "
            "delimitador estructural declarado " + repr(DELIMITADOR) + ". Un hueco que no "
            "es el delimitador es texto que ninguna entrada reclama, y no se interpreta a "
            "medias",
        )

    if limites[0] > 0:
        bloques.append(BloqueCerrado(
            PREAMBULO, None, None, 0, 0, limites[0],
            recortar(contenido[: limites[0]], False, PREAMBULO),
        ))
    for indice, cabecera in enumerate(cabeceras):
        inicio = limites[indice]
        fin = limites[indice + 1]
        es_ultimo = indice == len(cabeceras) - 1
        identificador = cabecera.group("id").decode("ascii")
        bloques.append(BloqueCerrado(
            identificador,
            cabecera.group("familia").decode("ascii"),
            int(cabecera.group("numero")),
            len(bloques),
            inicio,
            fin,
            recortar(contenido[inicio:fin], es_ultimo, identificador),
        ))
    return bloques


def derivar_libro(canal, ruta, commits=None, base=None):
    """El LIBRO de entradas cerradas: qué entrada nació en qué commit, y con qué bytes.

    Se recorre la historia de la ruta en orden ASCENDENTE y cada entrada se ancla al PRIMER
    commit en que aparece. Ése es su commit de introducción, y sus bytes de allí son el
    término de comparación de `O27` §3.

    Si una entrada YA publicada aparece con bytes distintos en un commit posterior, eso es
    una alteración INSCRITA EN LA HISTORIA: se registra en `incidencias` y quien juzgue la
    convierte en hallazgo. Confirmar no exime, y confirmar dos veces tampoco.
    """
    if commits is None:
        commits = canal.commits_de_la_ruta(ruta)

    # `V6-07` · qué entradas estaban CERRADAS en la revisión BASE, y por tanto cuáles son
    # las que ESTA pasada añade. La conservación byte a byte NO depende de la base —su
    # término es el commit que introdujo cada entrada, y por eso la elección de la base no
    # puede blanquear nada—; lo que sí depende de la base es la pregunta «qué se ha añadido
    # aquí», que es literalmente relativa a un punto de partida y se declara como tal.
    en_la_base = None
    base_ilegible = None
    if base:
        contenido_base = canal.contenido(base, ruta)
        if contenido_base is not None:
            try:
                en_la_base = {b.identificador for b in derivar_bloques(contenido_base)}
            except SedeIlegible as error:
                base_ilegible = str(error)
    entradas = {}
    orden = []
    incidencias = []
    ilegibles = []
    for commit in commits:
        contenido = canal.contenido(commit, ruta)
        if contenido is None:
            continue
        try:
            bloques = derivar_bloques(contenido)
        except SedeIlegible as error:
            # Un commit histórico ilegible no se salta en silencio: se publica. Saltarlo
            # sería derivar el libro de una historia recortada a conveniencia.
            ilegibles.append({"commit": commit, "detalle": str(error)})
            continue
        for bloque in bloques:
            conocida = entradas.get(bloque.identificador)
            if conocida is None:
                entradas[bloque.identificador] = {
                    "commit": commit,
                    "contenido": bloque.contenido,
                    "numero": bloque.numero,
                    "familia": bloque.familia,
                }
                orden.append(bloque.identificador)
            elif conocida["contenido"] != bloque.contenido:
                incidencias.append({
                    "identificador": bloque.identificador,
                    "introducida_en": conocida["commit"],
                    "alterada_en": commit,
                    "bytes_originales": len(conocida["contenido"]),
                    "bytes_ahora": len(bloque.contenido),
                })
    # Si la base no se pudo leer, se considera cerrado todo lo que el LIBRO ya conoce. Es
    # fallo seguro y no fallo abierto: se pierde la exigencia de FORMA sobre entradas
    # antiguas —que `O27` §2 prohíbe exigir de todas formas— y no se pierde ni una sola de
    # las comprobaciones de conservación, orden, numeración y no duplicación.
    if en_la_base is None:
        en_la_base = set(entradas)
    return {
        "ruta": ruta,
        "commits": list(commits),
        "orden": orden,
        "entradas": entradas,
        "en_la_base": en_la_base,
        "base_ilegible": base_ilegible,
        "incidencias": incidencias,
        "commits_ilegibles": ilegibles,
    }


def tiene_entradas_cerradas(libro):
    """¿Gobierna a esta ruta el régimen de ENTRADAS CERRADAS, o el de prefijo?

    Se responde desde el LIBRO —o sea, desde la HISTORIA— y NUNCA desde los bytes de hoy.
    La diferencia es el ataque: si el régimen se decidiera mirando el fichero actual,
    bastaría con borrar las cabeceras `# \\`Onn\\`` para que el documento «dejara de tener
    entradas» y cayera al régimen más débil. Derivado de la historia, un atacante tendría
    que reescribir los ocho commits de inscripción, y eso ya lo caza `E-09`.

    `PREAMBULO` no cuenta: un documento sin ninguna entrada es un texto continuo —`KERNEL.md`
    o una especificación aprobada—, y a ése le corresponde el contrato que `V6-12` le venía
    aplicando, no un régimen de entradas que no tiene.
    """
    return any(identificador != PREAMBULO for identificador in libro["orden"])


def _umbral_de_forma(libro):
    """Desde qué número son exigibles los campos de forma. DERIVADO, no escrito.

    `O27` §2 dice que los campos «son exigibles prospectivamente DESDE LA RESOLUCIÓN QUE
    ESTABLECIÓ ESA FORMA». Aquí esa resolución no se escribe a mano: se busca cuál es la
    primera entrada del LIBRO que ya los trae, y desde ahí se exigen. Medido sobre la sede
    real, el umbral sale `O23` —`O17`…`O22` no los llevan y `O23`…`O27` sí—, que es
    exactamente lo que `O27` §2 describe.

    Escribir `23` como constante habría dado el mismo resultado HOY y habría caducado en
    cuanto la forma volviera a cambiar; y peor: habría puesto en rojo a `O17`…`O22`, que es
    justo lo que `O27` §2 prohíbe.
    """
    con_forma = [d["numero"] for d in libro["entradas"].values()
                 if d["numero"] is not None
                 and all(re.search(patron, d["contenido"])
                         for patron, _ in CAMPOS_DE_ENTRADA_NUEVA)]
    return min(con_forma) if con_forma else None


def _juzgar_numeracion(bloques):
    """Familia, orden y CONSECUTIVIDAD de los números, sobre el documento entero.

    Va sobre TODOS los bloques y no sólo sobre los añadidos en esta pasada, porque un
    `O99` colado en un commit que después se declara como base no sería «nuevo» para nadie
    y seguiría siendo un hueco de setenta números que nadie puede auditar. Esto es
    estructura, no forma: exigirlo de las entradas históricas no las obliga a cambiar ni un
    byte, y por eso no choca con `O27` §2.
    """
    fallos = []
    anterior = None
    for bloque in bloques:
        if bloque.identificador == PREAMBULO:
            if bloque.orden != 0:
                fallos.append((ESTRUCTURA, PREAMBULO,
                               "el preámbulo de la sede aparece en la posición "
                               + str(bloque.orden) + " y no la primera"))
            continue
        if bloque.familia != FAMILIA_CANONICA:
            fallos.append((FAMILIA_AJENA, bloque.identificador,
                           "la entrada `" + bloque.identificador + "` pertenece a la "
                           "familia `" + str(bloque.familia) + "`, que esta sede no "
                           "gobierna. Una familia nueva no hereda ni el orden ni el "
                           "cliquet de numeración de la que dice suceder"))
            continue
        if anterior is not None and bloque.numero != anterior + 1:
            fallos.append((SALTO, bloque.identificador,
                           "después de `" + FAMILIA_CANONICA + str(anterior) + "` la sede "
                           "publica `" + bloque.identificador + "`. Un salto de numeración "
                           "deja un hueco que nadie puede auditar: o falta una resolución, "
                           "o se ha renumerado una que ya estaba"))
        anterior = bloque.numero
    return fallos


def _juzgar_forma(bloque, umbral):
    """`O27` §2 y §3: lo que se AÑADE se añade COMPLETO, o no se añade."""
    fallos = []
    cuerpo = (bloque.contenido[bloque.contenido.find(b"\n") + 1:]
              if b"\n" in bloque.contenido else b"")
    if not cuerpo.strip():
        fallos.append((INCOMPLETA,
                       "la entrada añadida `" + bloque.identificador + "` no tiene cuerpo: "
                       "es un título sin resolución. `O27` §3 admite añadir una entrada "
                       "COMPLETA, y un titular no lo es"))
        return fallos
    if umbral is None or bloque.numero is None or bloque.numero < umbral:
        return fallos
    for patron, nombre in CAMPOS_DE_ENTRADA_NUEVA:
        if not re.search(patron, bloque.contenido):
            fallos.append((INCOMPLETA,
                           "la entrada añadida `" + bloque.identificador + "` no declara `"
                           + nombre + "`, y la forma quedó establecida en `"
                           + FAMILIA_CANONICA + str(umbral) + "`. `O27` §2 hace estos "
                           "campos exigibles PROSPECTIVAMENTE: no se insertan en las "
                           "históricas, y no se omiten en las nuevas"))
    return fallos


def juzgar(libro, contenido):
    """Contrasta los bytes ACTUALES contra el libro. Devuelve la lista de infracciones.

    Cada infracción es `{"codigo", "identificador", "causa"}`. Lista vacía significa que
    toda entrada cerrada se conserva byte a byte, en su orden, sin duplicados, y que lo
    único que ha cambiado es una entrada nueva y completa al final.
    """
    infracciones = []

    if contenido is None:
        # La sede NO ESTÁ. No es «no ha cambiado»: es que no hay bytes que conservar, y
        # cada entrada cerrada del libro se ha perdido entera. Se dice así, y no se cae con
        # una traza —que es lo que hacía este camino antes de esta guarda— porque una traza
        # no es un veredicto.
        return [{"codigo": BORRADA, "identificador": i,
                 "causa": "la sede APPEND-ONLY no tiene contenido, y la entrada `" + i
                          + "`, introducida en el commit "
                          + libro["entradas"][i]["commit"][:12] + ", se ha perdido con ella"}
                for i in libro["orden"]]

    nombradas = set()

    def anotar(codigo, identificador, causa):
        infracciones.append({"codigo": codigo, "identificador": identificador,
                             "causa": causa})
        nombradas.add(identificador)

    # ── CANAL 1 · PRESENCIA LITERAL ──────────────────────────────────────────
    # Los bytes de cada entrada cerrada tienen que SEGUIR ESTANDO, tal cual, en algún
    # sitio del documento. Es una comprobación tosca a propósito: no necesita que la
    # estructura se pueda leer, y por eso sigue hablando cuando el canal estructural se
    # ha quedado mudo —que es exactamente lo que pasa cuando el ataque corta el fichero
    # por la mitad de un delimitador—. Necesaria pero NO suficiente: no ve reordenaciones
    # ni duplicados, y de ésos responde el canal 2.
    literales = []
    for identificador in libro["orden"]:
        if libro["entradas"][identificador]["contenido"] not in contenido:
            literales.append(identificador)

    # ── CANAL 2 · ESTRUCTURAL ────────────────────────────────────────────────
    try:
        bloques = derivar_bloques(contenido)
    except SedeIlegible as error:
        anotar(ESTRUCTURA, "(sede)", str(error))
        for identificador in literales:
            anotar(BORRADA, identificador,
                   "los bytes de la entrada `" + identificador + "`, introducida en el "
                   "commit " + libro["entradas"][identificador]["commit"][:12]
                   + " y cerrada desde entonces, YA NO APARECEN en la sede. No se conserva "
                   "byte a byte, y la estructura tampoco se puede leer para decir más")
        _anotar_historia(libro, anotar)
        return infracciones

    vistos = {}
    for bloque in bloques:
        if bloque.identificador in vistos:
            anotar(DUPLICADA, bloque.identificador,
                   "la sede publica DOS entradas con el identificador `"
                   + bloque.identificador + "` (posiciones " + str(vistos[bloque.identificador])
                   + " y " + str(bloque.orden) + "). Con dos textos bajo el mismo nombre, "
                   "cuál rige deja de ser una pregunta con respuesta")
        else:
            vistos[bloque.identificador] = bloque.orden

    presentes = {b.identificador: b for b in bloques}
    for identificador in libro["orden"]:
        registrada = libro["entradas"][identificador]
        bloque = presentes.get(identificador)
        if bloque is None:
            anotar(BORRADA, identificador,
                   "la entrada `" + identificador + "`, introducida en el commit "
                   + registrada["commit"][:12] + " y cerrada desde entonces, ya no está en "
                   "la sede. Una entrada cerrada no se borra: una resolución posterior la "
                   "REVISA sin borrarla")
            continue
        if bloque.contenido != registrada["contenido"]:
            anotar(ALTERADA, identificador,
                   "la entrada `" + identificador + "` no coincide BYTE A BYTE con la que "
                   "se introdujo en el commit " + registrada["commit"][:12] + " ("
                   + str(len(registrada["contenido"])) + " bytes → "
                   + str(len(bloque.contenido)) + " bytes). Da igual si el cambio es una "
                   "condición, una fecha o un espacio: lo publicado se conserva")

    # El ORDEN. Las entradas del libro tienen que aparecer en la misma secuencia, y todas
    # ANTES de cualquier añadido: `O27` §3 permite añadir AL FINAL, no intercalar.
    secuencia = [b.identificador for b in bloques if b.identificador in libro["entradas"]]
    esperada = [i for i in libro["orden"] if i in presentes]
    if secuencia != esperada and len(secuencia) == len(set(secuencia)):
        anotar(REORDENADAS, "(sede)",
               "las entradas cerradas aparecen en el orden " + " ".join(secuencia)
               + " y el libro las introdujo en el orden " + " ".join(esperada)
               + ". Reordenar no pierde bytes y cambia qué revisa a qué: es una "
               "alteración de la sede aunque cada entrada siga entera")

    # La NUMERACIÓN, sobre el documento entero. Estructura, no forma.
    for codigo, identificador, causa in _juzgar_numeracion(bloques):
        anotar(codigo, identificador, causa)

    # Lo que ESTA pasada añade: tiene que ir al FINAL y estar COMPLETO. `en_la_base`
    # declara contra qué estado se juzga «añadido», que es `V6-07` aplicado aquí.
    en_la_base = libro.get("en_la_base") or set(libro["entradas"])
    posicion_de_la_ultima_cerrada = -1
    for bloque in bloques:
        if bloque.identificador in en_la_base:
            posicion_de_la_ultima_cerrada = bloque.orden

    umbral = _umbral_de_forma(libro)
    for bloque in bloques:
        if bloque.identificador in en_la_base:
            continue
        if bloque.orden < posicion_de_la_ultima_cerrada:
            anotar(INSERCION, bloque.identificador,
                   "la entrada `" + bloque.identificador + "` es nueva y NO está al final: "
                   "ocupa la posición " + str(bloque.orden) + " y por debajo de ella "
                   "quedan entradas ya cerradas. `O27` §3 admite AÑADIR al final, no "
                   "intercalar")
        for codigo, causa in _juzgar_forma(bloque, umbral):
            anotar(codigo, bloque.identificador, causa)

    for identificador in literales:
        if identificador in nombradas:
            continue
        anotar(BORRADA, identificador,
               "los bytes de la entrada `" + identificador + "` ya no aparecen literalmente "
               "en la sede, y el canal estructural no lo ha señalado. Los dos canales tienen "
               "que decir lo mismo; que no lo digan es en sí un hallazgo")
    _anotar_historia(libro, anotar)
    return infracciones


def _anotar_historia(libro, anotar):
    """El tercer canal: lo que la HISTORIA de la ruta ya publica como alterado.

    Va el último a propósito. Un ataque confirmado aparece a la vez en el árbol de hoy y en
    la historia, y el motivo que un operador necesita leer primero es el del árbol que
    tiene delante; el de la historia explica CUÁNDO entró, que es la segunda pregunta.
    """
    for incidencia in libro["incidencias"]:
        anotar(ALTERADA, incidencia["identificador"],
               "la entrada `" + incidencia["identificador"] + "`, introducida en "
               + incidencia["introducida_en"][:12] + ", aparece con otros bytes en el "
               "commit " + incidencia["alterada_en"][:12] + " ("
               + str(incidencia["bytes_originales"]) + " → "
               + str(incidencia["bytes_ahora"]) + "). La alteración está INSCRITA en la "
               "historia, y confirmar no exime")
    for ilegible in libro["commits_ilegibles"]:
        anotar(ESTRUCTURA, "(historia)",
               "el commit " + ilegible["commit"][:12] + " publica una sede cuya estructura "
               "no se puede derivar: " + ilegible["detalle"])


def informe(libro, contenido, infracciones=None):
    """La PROCEDENCIA del juicio, publicable: qué entradas, desde qué commit, con qué bytes.

    Se publica en el veredicto haya o no hallazgos. Un guardián que sólo habla cuando algo
    va mal es indistinguible de un guardián apagado, y ése es el modo de fallo que este
    módulo existe para cerrar.
    """
    if infracciones is None:
        infracciones = juzgar(libro, contenido)
    try:
        bloques = [b.a_dict() for b in derivar_bloques(contenido)]
    except SedeIlegible:
        bloques = None
    return {
        "regimen": "entradas-cerradas",
        "ruta": libro["ruta"],
        "commits_de_la_historia": len(libro["commits"]),
        "entradas_cerradas": [
            {"identificador": i,
             "introducida_en": libro["entradas"][i]["commit"],
             "bytes": len(libro["entradas"][i]["contenido"]),
             "digest": digest_de_contenido(libro["entradas"][i]["contenido"])}
            for i in libro["orden"]
        ],
        "bloques_actuales": bloques,
        "infracciones": list(infracciones),
        "ok": not infracciones,
    }
