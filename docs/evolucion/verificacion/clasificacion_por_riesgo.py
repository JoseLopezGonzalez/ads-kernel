# -*- coding: utf-8 -*-
"""
`O29` §2 · CLASIFICACIÓN POR RIESGO DE LAS PROPIEDADES DEL CORPUS
=================================================================

POR QUÉ EXISTE ESTE FICHERO
---------------------------
`O26-SAB` mide **342 propiedades · 300 PENDIENTES** tomando como unidad **cada cláusula
`falla_si`**. `O29` §1 corrige expresamente esa interpretación:

    «Una cláusula funcional no se convierte automáticamente en una propiedad crítica por
     estar formulada como condición de fallo.»

`O29` no dice «mide menos»: dice **mide con la clase que a cada propiedad le corresponde**.
Este módulo NO elimina ninguna de las 342. Las CLASIFICA en las seis clases del encargo

    CRÍTICA · FUNCIONAL · OBSERVABILIDAD · DOCUMENTAL · EXTERNA · LIMITACIÓN_DE_ANFITRIÓN

y publica, para cada una, **por qué** cayó donde cayó. Una clasificación que no dice su
motivo no se puede auditar, y por tanto no clasifica: reparte.

DE DÓNDE SE DERIVA LA CLASE — Y DE DÓNDE NO
-------------------------------------------
De su EFECTO, que es lo que `O29` §2 enumera. No hay ninguna lista de identificadores
escrita a mano en la clasificación: hay una tabla de **diez efectos peligrosos**, uno por
cada apartado de `O29` §2, y cada efecto se deriva de la cláusula y de su contexto —el
nombre del escenario, sus `entonces`, sus obligaciones y su canal—. Lo que sí hay escrito a
mano es la lista `ANCLAS_CONOCIDAS` de `comprobar-propiedades-saboteadas.py`: escenarios
que el gate válido y sus revisores nombraron y que este clasificador **tiene que** marcar
CRÍTICOS. Ésa no es la fuente de la clasificación; es su CONTROL, vive fuera de las reglas
—para poder vaciarla y comprobar que se nota— y se ejerce en cada corrida.

DÓNDE SE USA
------------
Este fichero es una BIBLIOTECA: no se ejecuta, se importa. Lo importa
`comprobar-propiedades-saboteadas.py`, que es quien deriva el universo y publica:

    …/comprobar-propiedades-saboteadas.py --por-riesgo
    …/comprobar-propiedades-saboteadas.py --autopruebas-riesgo

No lleva línea de intérprete a propósito: `T330` deriva del disco el inventario de puntos
ejecutables y le exige a cada uno la guarda `G-03` y el mecanismo `E-10`; una `#!` en un
fichero que no es invocable lo presentaría como ejecutable sin serlo.

LA ASIMETRÍA, QUE ES LO ÚNICO QUE PROTEGE DE UN BLANQUEO
-------------------------------------------------------
Un clasificador léxico puede REBAJAR una propiedad crítica. Ése es el peor resultado
posible: convertiría el encargo en un blanqueo. La defensa no es afinar el léxico —siempre
se le escapará una— sino la forma de la decisión:

  1. **Subir es barato, bajar es caro.** Basta que UN efecto de `O29` §2 se derive de la
     cláusula O de su contexto para que la propiedad sea CRÍTICA. Para rebajarla hace falta
     que NINGUNO se derive **y además** evidencia positiva de la clase inferior, escrita en
     la propia cláusula.
  2. **El residuo sube.** Una propiedad de la que no se deriva ni efecto peligroso ni
     motivo de rebaja se queda CRÍTICA, no FUNCIONAL. Ante la duda, crítica: que sobre.
  3. **El contexto sólo puede subir.** El nombre del escenario y sus `entonces` se miran
     para AÑADIR criticidad, nunca para quitarla. Una regla que rebajase por contexto sería
     una puerta para blanquear desde un campo que la cláusula no controla.
  4. **`LIMITACIÓN_DE_ANFITRIÓN` y `EXTERNA` no son salidas.** `O29` §7 permite certificar
     una propiedad dependiente del anfitrión para un perfil concreto; no permite dejar de
     considerarla crítica. Por eso una propiedad de la que se deriva un efecto de §2 y que
     además toca el anfitrión sale **CRÍTICA con la marca `anfitrion`**, y no
     `LIMITACIÓN_DE_ANFITRIÓN`. La clase inferior sólo la alcanzan las propiedades de las
     que no se deriva ningún efecto.

LO QUE ESTE CRITERIO **NO** CUBRE — y hay que leerlo antes que los cardinales
----------------------------------------------------------------------------
  · **Es léxico.** Deriva de las palabras de la cláusula y de su contexto, no de la
    semántica del código que la implementa. Una cláusula que describa un efecto peligroso
    con vocabulario que ninguna regla recoge caería al residuo — y el residuo es CRÍTICA,
    que es el lado seguro del error, pero seguiría sin decir CUÁL de los diez efectos es.
  · **No mide la severidad dentro de la clase.** Todas las CRÍTICAS pesan igual aquí.
  · **No juzga si la propiedad está bien escrita.** Una cláusula vaga se clasifica por lo
    que dice, no por lo que quiso decir.
  · **No sustituye a `O26-SAB`.** Dice qué propiedades exigen prueba adversarial; que la
    tengan y que sea capaz lo mide `O26-SAB`, y este módulo no reimplementa ese juicio.
  · **El universo es el que deriva `O26-SAB`**: cláusulas `falla_si` de escenarios que
    cubren una obligación del universo derivado y declaran validador. Las propiedades de
    escenarios que no cubren ninguna obligación de ese universo —`T380`…`T399` del
    aislamiento y `T420`…`T429` de la evidencia contra `HEAD`, que cubren `G-03`, `E-10`,
    `ADJ-B2` y `D-05`— **no entran en las 342 y este módulo tampoco las ve**. Se publica
    como agujero del universo, no se calla.
"""

import re
import unicodedata

# ---------------------------------------------------------------------------
#  las seis clases del encargo
# ---------------------------------------------------------------------------

CRITICA = "CRÍTICA"
FUNCIONAL = "FUNCIONAL"
OBSERVABILIDAD = "OBSERVABILIDAD"
DOCUMENTAL = "DOCUMENTAL"
EXTERNA = "EXTERNA"
ANFITRION = "LIMITACIÓN_DE_ANFITRIÓN"

CLASES = (CRITICA, FUNCIONAL, OBSERVABILIDAD, DOCUMENTAL, EXTERNA, ANFITRION)


def normalizar(texto):
    """Minúsculas, sin acentos y con los espacios colapsados. Nada más."""
    plano = unicodedata.normalize("NFD", (texto or "").lower())
    plano = "".join(c for c in plano if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", plano)


# ---------------------------------------------------------------------------
#  los DIEZ efectos de `O29` §2 — uno por apartado, con su número
# ---------------------------------------------------------------------------

class Efecto:
    """Un apartado de `O29` §2 y los rastros por los que se deriva de un texto."""

    def __init__(self, numero, titulo, patrones):
        self.numero = numero
        self.titulo = titulo
        self.patron = re.compile("|".join("(?:%s)" % p for p in patrones))

    def rastro(self, texto):
        """El fragmento LITERAL por el que se deriva, o `None`. Publicar el fragmento es
        lo que hace auditable la derivación: sin él, la clase es una afirmación."""
        m = self.patron.search(texto)
        return m.group(0) if m else None


EFECTOS = (
    Efecto(1, "pérdida o corrupción silenciosa de estado", (
        r"se pierde", r"\bperdida\b", r"corrupcion", r"corrupto", r"corromp",
        r"estado canonico tocado", r"mezcla parcial", r"estado parcial",
        r"inventa un estado", r"se lee como estado valido", r"parte el linaje",
        r"inmigrable", r"trunca", r"vaciar un cuerpo", r"retira(?:r)? un cuerpo",
        r"se lleva el cuerpo", r"se llevo lo que", r"borrad", r"\bborra\b", r"\bborre\b",
        r"pisa el perfil", r"reescribe los objetos", r"queda con parte de los ficheros",
        r"deja el almacen", r"almacen (?:roto|heredado|sano)", r"se come la corrupcion",
        r"sellar retira", r"sella el punto de no retorno", r"sin dejar rastro",
        r"desaparece sin", r"deja de poder cerrarse", r"un fichero roto",
        r"\bcarrera\b", r"deja pasar una escritura", r"bytes caducados",
        r"cola reordenada", r"haciendo parecer cerrada", r"difiere del",
        r"pierde grado", r"desaparece una de las", r"modifica por si mismo",
        r"pasa a ser fuente de verdad", r"se persiste",
    )),
    Efecto(2, "publicación parcial o inválida", (
        r"publicacion a medias", r"queda publicada", r"se convierte en vigente",
        r"revision.json", r"manifiesto truncado", r"nombra objetos que",
        r"publica(?:r)? (?:la |una )?(?:revision|transicion|evidencia|objetos)",
        r"sin el testigo", r"\btestigo\b", r"transicion incompleta",
        r"se publica una ejecucion", r"instalacion que no se puede comprobar",
        r"un manifiesto que no cubre nada", r"publicar\b", r"publicando",
        r"la revision avanza",
    )),
    Efecto(3, "doble efecto o doble confirmación", (
        r"dos veces", r"duplica el efecto", r"los dos confirman", r"dos escritores",
        r"segundo escritor", r"doble (?:efecto|confirmacion|participacion)",
        r"segunda migracion", r"anexa eventos", r"dos autoridades",
        r"cuatro implementaciones divergentes", r"idempot", r"dos veredictos",
        r"gasta una devolucion", r"dos materializaciones",
    )),
    Efecto(4, "evasión de autoridad, permisos o gates", (
        r"salta la guarda", r"se salta", r"eximirse", r"por su cuenta",
        r"decide la autoridad", r"sustituir a la raiz externa", r"autoridad interna",
        r"sin autoridad declarada", r"pasa por omision", r"acto de autoridad",
        r"decide con que codigo", r"roba un lease", r"pasa el gate",
        r"\bsin dictamen\b", r"apaga el guardian", r"blanquea", r"impide el acto",
        r"puerta de atras", r"se puede editar a mano", r"quien pueda escribir",
        r"resuelve una reconciliacion", r"despacha todo lo pendiente",
        r"\bautoridad\b", r"\bpermiso", r"\bgate\b", r"nadie exige",
        r"la conversacion bajo el grado",
        r"decide qu[ei] identidad", r"cambiar qu[ei] identidad", r"puede cambiar qu",
    )),
    Efecto(5, "falsificación de evidencia, identidad, commit o tree", (
        r"evidencia", r"atestacion", r"\bfirma\b", r"firmad", r"\bfirmo\b", r"\bdigest\b",
        r"\bhuella\b", r"\bcommit\b", r"\btree\b", r"nacimiento", r"historia reescrita",
        r"cifra falsa", r"\bidentidad\b(?! de proceso)", r"que su salida no respalda",
        r"caducada pasa por valida", r"atribuirse a quien no", r"fabricar", r"se fabrica",
        r"puede fabricar", r"reutilizar una atestacion", r"\blinaje\b", r"\btalon\b",
        r"\beslabon\b", r"cadena de huellas", r"cifra publicada", r"cifra verdadera",
        r"contraste", r"contrastar", r"contrastarla", r"sin contrastar",
        r"se presenta como", r"pasa por (?:valida|bueno|buena)", r"\bsecreto\b",
        r"clave (?:privada|efimera)", r"criptografia propia", r"primitiva criptografica",
    )),
    Efecto(6, "ejecución de código no autorizado", (
        r"sys\.path", r"pythonpath", r"\bcwd\b", r"procedencia", r"homonimo",
        r"sustituyen a un modulo", r"modulos cuya procedencia", r"\bla purga\b",
        r"sin la purga", r"se contaminan", r"directorio de trabajo",
        r"con que codigo se le verifica", r"punto ejecutable nuevo",
    )),
    Efecto(7, "degradación silenciosa de un mecanismo de seguridad", (
        r"en silencio", r"silencios", r"desapercibid", r"sin que nada lo",
        r"sin que nadie lo", r"sin que nada .{0,40}(?:diga|note)", r"parpadee",
        r"decorativ", r"decorado", r"no puede ponerse rojo", r"dice verde a todo",
        r"da rojo siempre", r"backend (?:debil|simple)", r"nivel inferior",
        r"aviso en vez de", r"se oculta", r"por omision", r"se degrada", r"degradacion",
        r"custodia productiva", r"tolerancia de la ventana", r"interruptor",
        r"relajar", r"no se recalcula", r"escrit[oa]s? a mano", r"escribe a mano",
        r"escribirse a mano", r"a mano en vez de", r"lista literal",
        r"una constante en vez de", r"deja de (?:comprobarse|tipar|derivarse)",
        r"se retira y", r"se retira los", r"con la comprobacion retirada",
        r"vuelve a ser (?:un|una|los|las)", r"vuelve a mirar", r"vuelve a casar",
        r"tapan el hueco", r"deja de detectarse", r"sin criterio",
        r"no se comprueba", r"se omite", r"se hace sobre el conjunto",
        r"queda de decorado", r"solo existe en la api", r"solo (?:se |)mira",
        r"cae en un valor por omision", r"cubre lo que viene del lanzador",
        r"lista parcial en vez de", r"excepcion de lectura en vez de",
        r"sin aviso", r"no se mueve", r"censa(?:r)? un conjunto distinto",
        r"entra en el universo", r"queda fuera del universo",
        r"\binvisible\b", r"queda sin censo", r"no llega a la tabla",
        r"sale de cualquiera de los dos censos",
    )),
    Efecto(8, "incumplimiento de aislamiento", (
        r"aislamiento", r"mismo proceso", r"dentro del arbol", r"descendiente",
        r"huerfano", r"nieto", r"setsid", r"\bsesion\b", r"contencion", r"contener",
        r"killpg", r"comparten? (?:agente|slot|sesion|identificador|codigo de error)",
        r"comparten? codigo de salida", r"rol productor y el rol que critica",
        r"dos repositorios distintos", r"cerrojos locales", r"paralelos al motor",
        r"sigue vivo", r"sobrevive", r"\bgeneracion(?:es)? \b", r"dos agentes",
        r"un rol acaba en dos", r"dos roles", r"la raiz externa se ejecuta",
        r"cambio dentro del arbol", r"segundo escritor", r"escribe en el estado canonico",
    )),
    Efecto(9, "recuperación no idempotente", (
        r"recuperacion", r"recuperad", r"recuperar", r"reanud", r"migracion",
        r"migrar", r"migrable", r"reintent", r"recompone", r"recompuesta",
        r"punto de corte", r"puntos de corte", r"rama completar",
    )),
    Efecto(10, "declaración de éxito sobre una operación no ejecutada", (
        r"se simula", r"\bmock\b", r"se da por", r"\bverde\b", r"falso verde",
        r"exit 0", r"exit=0", r"codigo cero", r"codigo de salida", r"\bcodigo 0\b",
        r"se cuenta como ejercido", r"se rotula como ejecutado", r"no llego a aplicarse",
        r"se acredita solo por", r"declara disponible", r"no mediria nada",
        r"no demuestra nada", r"no distinguiria nada", r"imposible de superar",
        r"insensible al defecto", r"no habria podido fallar", r"sin ser detectado",
        r"pasa sin", r"pasa en verde", r"sale con codigo", r"sale verde",
        r"termina en verde", r"sigue en verde", r"queda en verde", r"sigue siendo correct",
        r"se declara(?:n)? (?:cerrada|superada|con el codigo)", r"se da por superada",
        r"declara(?:n)? (?:cerrada|ejecutado|ejercido)", r"no los nombra",
        r"medir(?:ia|a)? (?:el estado equivocado|en reposo)", r"mide en reposo",
        r"la prueba lo da por", r"la medicion lo desmiente", r"y no por el aislamiento",
        r"no se distinguen sobre el mismo arbol", r"sin (?:su |)control del",
        r"se publica como cero", r"se cuenta como contrastado",
    )),
)


# ---------------------------------------------------------------------------
#  las rebajas · SÓLO con evidencia positiva, y sólo si no se derivó ningún efecto
# ---------------------------------------------------------------------------

class Rebaja:
    """Una clase inferior y la evidencia positiva que hay que encontrar para bajar a ella.

    `exige` tiene que casar en la CLÁUSULA —no en el contexto—: bajar por un campo que la
    cláusula no controla es exactamente cómo se blanquea una propiedad.
    `veta` deshace la rebaja: si algo de esto aparece, la propiedad no baja por esta regla.
    """

    def __init__(self, clase, titulo, exige, veta=()):
        self.clase = clase
        self.titulo = titulo
        self.exige = re.compile("|".join("(?:%s)" % p for p in exige))
        self.veta = re.compile("|".join("(?:%s)" % p for p in veta)) if veta else None

    # LA POLARIDAD DE «X EN VEZ DE Y» · hallazgo del AUDITOR INDEPENDIENTE, dirección 1
    #
    #     HECHO REPRODUCIDO. `T226/f1` —«el eje agente se declara EN PROSA EN VEZ DE
    #     asignarse y registrarse»— se rebajaba a DOCUMENTAL porque la regla encontró
    #     «prosa». Pero en esa cláusula «en prosa» es **la alternativa PROHIBIDA**, no el
    #     sujeto del fallo: el sujeto es *asignar y registrar*, que es el canal operativo
    #     de `C4` paso 4. La regla casaba con X cuando el contrato dice que debe ocurrir Y.
    #
    #     El auditor midió el alcance: **26 cláusulas del universo** llevan esa
    #     construcción, y las demás se salvaron por los `veta` o por casualidad, no por
    #     diseño. Es la dirección peligrosa —rebajar una propiedad crítica— y por eso se
    #     cierra aquí y no se deja como observación.
    #
    # DECISIÓN · en «X EN VEZ DE Y», el sujeto del fallo es **Y**, no X
    #     `X` es lo que ocurre MAL —la alternativa prohibida— e `Y` es lo que el contrato
    #     dice que debe ocurrir. La propiedad en juego es `Y`, así que la evidencia
    #     positiva de la rebaja se busca en `Y` y se DESCARTA `X`. En `T226/f1` eso deja
    #     fuera «en prosa» —que es lo prohibido— y deja dentro «asignarse y registrarse»,
    #     que no casa con ninguna rebaja documental: la propiedad no baja.
    #
    #     La primera versión de esta corrección cortaba al revés —se quedaba con `X`— y no
    #     cambiaba nada: `T226/f1` seguía saliendo DOCUMENTAL. Se dice porque el corte
    #     correcto no es obvio y equivocarse de lado no da error, da el mismo resultado de
    #     antes con un comentario nuevo, que es la peor forma de no arreglar algo.
    _ALTERNATIVA_PROHIBIDA = re.compile(r"\b(?:en vez de|en lugar de)\b")

    def rastro(self, clausula):
        if self.veta and self.veta.search(clausula):
            return None
        corte = self._ALTERNATIVA_PROHIBIDA.search(clausula)
        sujeto = clausula[corte.end():] if corte else clausula
        m = self.exige.search(sujeto)
        return m.group(0) if m else None


REBAJAS = (
    Rebaja(ANFITRION, "el mecanismo lo provee el anfitrión y el corpus declara su límite",
           exige=(r"cgroup", r"\bnamespace", r"anfitrion", r"backend fuerte",
                  r"identidad de sistema", r"proveedor de firma"),
           veta=(r"\bverde\b", r"se da por", r"en silencio")),
    Rebaja(EXTERNA, "el sujeto del fallo vive fuera del kernel juzgado",
           exige=(r"custodia (?:productiva |)externa", r"\bowner\b(?! pasa)",
                  r"coordinador", r"raiz externa custodia"),
           veta=(r"\bverde\b", r"se da por")),
    Rebaja(DOCUMENTAL, "el sujeto del fallo es un documento, una cabecera o una cifra "
                       "publicada, sin canal operativo detrás",
           exige=(r"cabecera", r"\brotulo\b", r"\bprosa\b", r"redaccion",
                  r"\bdocumento\b", r"\bcita\b", r"\bcitad", r"vuelve a decir",
                  r"\benumera\b", r"no la enumera", r"\bafirma\b"),
           veta=(r"\bverde\b", r"se da por", r"a mano", r"derivar", r"derivad")),
    Rebaja(OBSERVABILIDAD, "el fallo es que algo deja de DECIRSE; el mecanismo sigue "
                           "haciendo lo que hace",
           exige=(r"no dice", r"sin decir", r"no nombra", r"no publica",
                  r"deja de publicar", r"el diagnostico no",
                  r"no lista", r"deja de ser reproducible", r"no es demostrable",
                  r"traza en vez de", r"como traza", r"\bexplicativo\b",
                  r"reloj, duracion", r"ruta absoluta", r"arbol de directorios",
                  r"no se puede leer", r"sin identificar"),
           veta=(r"\bverde\b", r"se da por")),
    Rebaja(FUNCIONAL, "obligación de forma o de contrato cuyo incumplimiento no produce "
                      "ninguno de los diez efectos de `O29` §2",
           exige=(r"esquema", r"texto libre", r"\bcampo\b", r"\bformato\b",
                  r"\btipar\b", r"\bvariante\b", r"\bcardinal\b", r"\bperfil\b",
                  r"\bcriterio\b", r"\bfixture\b", r"deja de pasar", r"\bfamilia\b",
                  r"hueco de numeracion", r"\bordene?\b", r"\borden\b"),
           veta=(r"\bverde\b", r"se da por", r"a mano")),
)


# ---------------------------------------------------------------------------
#  el veredicto
# ---------------------------------------------------------------------------

class Veredicto:
    """La clase de una propiedad, con POR QUÉ, y no sólo con qué."""

    def __init__(self, clase, motivo, efectos=(), marcas=(), regla=""):
        self.clase = clase
        self.motivo = motivo
        self.efectos = tuple(efectos)          # [(numero, titulo, rastro, campo)]
        self.marcas = tuple(marcas)
        self.regla = regla

    @property
    def por_residuo(self):
        return self.clase == CRITICA and not self.efectos

    def efectos_dichos(self):
        return ", ".join("§2.%d %s" % (n, t) for n, t, _r, _c in self.efectos)


# Los campos del contexto que pueden SUBIR una propiedad a crítica. El contexto no rebaja
# nunca: por eso esta tabla no tiene equivalente en las rebajas.
CAMPOS_DE_CONTEXTO = ("nombre", "entonces")

# Marcas · no cambian la clase, la anotan. `O29` §7 permite certificar una propiedad
# dependiente del anfitrión para un perfil; no permite dejar de considerarla crítica.
MARCAS = (
    ("anfitrion", re.compile(r"cgroup|\bnamespace|anfitrion|backend fuerte|"
                             r"identidad de sistema|setsid|proveedor de firma")),
    ("externa", re.compile(r"raiz externa|custodia|\bowner\b|coordinador")),
)


# ---------------------------------------------------------------------------
#  LOS CUATRO EJES POR LOS QUE ESTE CLASIFICADOR SE PUEDE CONVERTIR EN UN BLANQUEO
# ---------------------------------------------------------------------------
#  No son parámetros de configuración: son las cuatro decisiones que hacen que la
#  clasificación proteja o no proteja, escritas donde se puedan ATACAR. Las autopruebas de
#  `--autopruebas-riesgo` cambian cada una de ellas en una copia del árbol y exigen que el
#  control de las ANCLAS lo cace. Una decisión que no se puede sabotear no se puede
#  auditar, y un clasificador cuyo autotest no puede fallar no clasifica: reparte.
ORDEN = ("efecto", "rebaja")           # subir primero. Al revés, una rebaja léxica gana
CLASE_DEL_RESIDUO = CRITICA            # lo no derivado sube. Bajarlo es blanquear por
                                       # ignorancia del clasificador
REBAJA_MIRA_EL_CONTEXTO = False        # el contexto sólo puede SUBIR; si además rebajase,
                                       # un campo que la cláusula no controla la degradaría
LA_MARCA_DECIDE_LA_CLASE = False       # `O29` §7 permite certificar por perfil, no dejar
                                       # de considerar crítica. Si la marca decidiese,
                                       # toda propiedad del anfitrión saldría del riesgo


def clasificar(clausula, contexto=None):
    """`Veredicto` de una cláusula `falla_si`, derivado de su efecto y de su contexto."""
    contexto = contexto or {}
    texto = normalizar(clausula)

    piezas = [("clausula", texto)]
    for campo in CAMPOS_DE_CONTEXTO:
        valor = contexto.get(campo)
        if isinstance(valor, (list, tuple)):
            valor = " · ".join(valor)
        if valor:
            piezas.append((campo, normalizar(valor)))

    marcas = tuple(nombre for nombre, patron in MARCAS
                   if any(patron.search(t) for _c, t in piezas))

    if LA_MARCA_DECIDE_LA_CLASE and marcas:
        clase = ANFITRION if "anfitrion" in marcas else EXTERNA
        return Veredicto(clase, "la marca `%s` decide la clase" % marcas[0],
                         marcas=marcas, regla="marca")

    def por_efecto():
        derivados = []
        for efecto in EFECTOS:
            for campo, trozo in piezas:
                rastro = efecto.rastro(trozo)
                if rastro:
                    derivados.append((efecto.numero, efecto.titulo, rastro, campo))
                    break
        if not derivados:
            return None
        return Veredicto(
            CRITICA,
            "se derivan %d efectos de `O29` §2: %s" % (
                len(derivados),
                "; ".join("§2.%d «%s» (en %s)" % (n, r, c) for n, _t, r, c in derivados)),
            efectos=derivados, marcas=marcas, regla="efecto")

    def por_rebaja():
        mirables = piezas if REBAJA_MIRA_EL_CONTEXTO else piezas[:1]
        for rebaja in REBAJAS:
            for campo, trozo in mirables:
                rastro = rebaja.rastro(trozo)
                if rastro:
                    return Veredicto(
                        rebaja.clase,
                        "no se deriva ningún efecto de `O29` §2 y %s da evidencia positiva "
                        "de la clase: %s — «%s»" % (
                            "la cláusula" if campo == "clausula" else "el campo `%s`" % campo,
                            rebaja.titulo, rastro),
                        marcas=marcas, regla="rebaja:%s" % rebaja.clase)
        return None

    intentos = {"efecto": por_efecto, "rebaja": por_rebaja}
    for paso in ORDEN:
        veredicto = intentos[paso]()
        if veredicto is not None:
            return veredicto

    return Veredicto(
        CLASE_DEL_RESIDUO,
        "RESIDUO · no se deriva ningún efecto de `O29` §2 y tampoco hay evidencia "
        "positiva de ninguna clase inferior. Ante la duda, CRÍTICA: rebajarla sin "
        "motivo escrito sería blanquearla",
        marcas=marcas, regla="residuo")
