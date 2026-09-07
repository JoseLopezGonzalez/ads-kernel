from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
import os as _os_g03
import sys as _sys_g03

# LA GUARDA NO DEJA RASTRO EN EL ÁRBOL QUE JUZGA. Medido: al importar la guarda, Python
# escribía `validadores/__pycache__/aislamiento_de_arranque…pyc` en el árbol, y
# `comprobar_arranque.py` empezó a publicar «el proyecto arrastra `__pycache__`» sobre
# proyectos recién creados. Se desactiva la escritura de bytecode DURANTE la guarda y se
# devuelve al estado que tenía: lo que el punto importe después sigue cacheándose como
# siempre, y no se paga rendimiento por una comprobación que corre una vez.
_G03_BYTECODE = _sys_g03.dont_write_bytecode
_sys_g03.dont_write_bytecode = True
_G03_PROPIA = _os_g03.path.dirname(_os_g03.path.realpath(__file__))
_G03_SEDE = ""
_G03_RAIZ = _G03_PROPIA
while not _G03_SEDE:
    for _G03_CANDIDATA in (_G03_PROPIA,
                           _os_g03.path.join(_G03_RAIZ, "kernel", "operativo",
                                             "validadores")):
        if _os_g03.path.isfile(_os_g03.path.join(_G03_CANDIDATA,
                                                 "aislamiento_de_arranque.py")):
            _G03_SEDE = _G03_CANDIDATA
            break
    else:
        _G03_PADRE = _os_g03.path.dirname(_G03_RAIZ)
        if _G03_PADRE == _G03_RAIZ:
            _sys_g03.stderr.write(
                "[PROCEDENCIA_NO_FIABLE] no hay `aislamiento_de_arranque.py` ni junto a "
                "este punto ejecutable ni en el `kernel/operativo/validadores/` de ning\u00fan "
                "ancestro suyo: no se puede decidir si el arranque est\u00e1 aislado, y no se "
                "sigue\n")
            raise SystemExit(5)
        _G03_RAIZ = _G03_PADRE
_sys_g03.path.insert(0, _G03_SEDE)
import aislamiento_de_arranque as _aislamiento_g03                    # noqa: E402

AISLAMIENTO = _aislamiento_g03.exigir(__file__, __name__)
_sys_g03.dont_write_bytecode = _G03_BYTECODE

# `-I` deja FUERA de `sys.path` el directorio del guión —es lo que impide que un homónimo
# vecino se cuele— y los puntos que importan módulos hermanos lo necesitan. Se reintroduce
# por RUTA DERIVADA DE `__file__`, que no la escribe el lanzador.
if _G03_PROPIA not in _sys_g03.path:
    _sys_g03.path.insert(0, _G03_PROPIA)

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  `A2` lo midió sobre este mismo fichero: entró en el inventario de puntos ejecutables
#  SIN la purga y con un mecanismo `G-03` que divergía del de los otros sesenta en dos
#  escapes —`\u00fa` frente a `ú`—, y eso puso `T330` y `T381` en rojo y arrastró SIETE
#  obligaciones a «sin implementar» que no tenían defecto ninguno. Un punto ejecutable
#  lleva el mecanismo ENTERO y COPIADO, no adaptado: es exactamente lo que `T381` mide.

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

RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()
import argparse                                                       # noqa: E402
import io                                                             # noqa: E402
import os                                                             # noqa: E402
import re                                                             # noqa: E402
import subprocess                                                     # noqa: E402
import sys                                                            # noqa: E402
import unicodedata                                                    # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "..", ".."))

TODOS_SATISFECHOS, HAY_INCUMPLIDOS, NO_SE_PUDO_COMPROBAR = 0, 1, 2

# ===========================================================================
#  1 · LA CLASE, Y POR QUÉ NO SE JUZGA CON UNA LISTA DE SUSTANTIVOS
# ===========================================================================
#  `O31` §6 manda juzgar ESTA clase:
#
#      copia manual de estado, cardinal o conjunto variable dentro de una sede viva que
#      debería derivarlo o remitir a su fuente competente.
#
#  EL CONTROL ANTERIOR ERA UN `awk` CON UNA LISTA DE SUSTANTIVOS ESCRITA A MANO
#  —«árboles, hallazgos, gates, bloqueantes, graves, medios, menores, leves, contratos,
#  condiciones»— y alcance POR LÍNEA. Medido sobre la base de `O31`: de seis variantes
#  cazaba DOS. Escapaban el cardinal separado de su sustantivo por un salto de línea y los
#  tres cardinales que este mismo expediente deriva —«los 24 invariantes críticos», «las 58
#  obligaciones internas», «los 57 sabotajes declarados»—, porque sus sustantivos no
#  estaban en la lista. Un control que reconoce el vocabulario que conoce juzga instancias.
#
#  LA INVERSIÓN QUE LO CONVIERTE EN CLASE. No se enumera la clase ABIERTA —los sustantivos,
#  que son infinitos y crecen con el corpus— sino las clases CERRADAS del español, que no
#  crecen: las palabras función (artículos, preposiciones, conjunciones, verbos auxiliares)
#  y los numerales. Un sustantivo DESCONOCIDO cae por descarte, que es exactamente lo que
#  «cardinal introducido después de escribir el control» significa.
#
#  Y UN CRÍTICO ADVERSARIAL ATACÓ ESTE DISEÑO ANTES DE QUE SE ESCRIBIERA. Sus catorce
#  variantes y sus cuatro ataques estructurales están todos aquí, cada uno con el mecanismo
#  que lo caza, y sus siete controles negativos están en las excepciones tipadas.

# LAS PALABRAS FUNCIÓN. Clase CERRADA del español: no crece con el corpus. Se enumera ésta
# —y no los sustantivos— porque enumerar lo cerrado es derivar y enumerar lo abierto es
# envejecer en silencio.
PALABRAS_FUNCION = frozenset("""
el la los las un una unos unas lo al del de a ante bajo cabe con contra desde durante en
entre hacia hasta mediante para por segun sin so sobre tras y e ni o u pero mas sino aunque
porque pues que si como cuando donde quien cual cuyo cuya cuyos cuyas se le les me te nos os
su sus mi mis tu tus este esta estos estas ese esa esos esas aquel aquella aquellos aquellas
es son era eran fue fueron ser sido siendo esta estan estaba estaban estar hay habia haber
ha han he hemos habran seria serian sera seran queda quedan quedaba quedaban quedo quedaron
sigue siguen seguia seguian sigo va van iba iban tiene tienen tenia tenian tener no ni si
tambien tampoco ya aun todavia solo solamente muy mas menos tan tanto asi aqui alli ahi hoy
ayer manana ahora entonces antes despues luego mientras siempre nunca jamas casi apenas
""".split())

# LOS NUMERALES. También clase CERRADA. No se escribe una lista de cardinales «hasta
# catorce» —el defecto que el propio corpus registró—: se escriben las PIEZAS y se compone,
# de modo que `treinta y un`, `doscientos`, `mil doscientos` y `novecientos noventa y nueve`
# se reconocen sin figurar en ninguna parte.
UNIDADES = {"cero": 0, "un": 1, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4,
            "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
            "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
            "dieciseis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
            "veinte": 20, "veintiun": 21, "veintiuno": 21, "veintiuna": 21,
            "veintidos": 22, "veintitres": 23, "veinticuatro": 24, "veinticinco": 25,
            "veintiseis": 26, "veintisiete": 27, "veintiocho": 28, "veintinueve": 29}
DECENAS = {"treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
           "ochenta": 80, "noventa": 90}
CENTENAS = {"cien": 100, "ciento": 100, "doscientos": 200, "doscientas": 200,
            "trescientos": 300, "trescientas": 300, "cuatrocientos": 400,
            "cuatrocientas": 400, "quinientos": 500, "quinientas": 500,
            "seiscientos": 600, "seiscientas": 600, "setecientos": 700, "setecientas": 700,
            "ochocientos": 800, "ochocientas": 800, "novecientos": 900,
            "novecientas": 900}
MULTIPLICADORES = {"mil": 1000, "millon": 1000000, "millones": 1000000}
# ORDINALES y COLECTIVOS: `el septimo hallazgo` copia un ordinal de estado, y `una decena
# de hallazgos` copia un cardinal por aproximación. Los dos son la clase.
ORDINALES = frozenset("""primer primero primera segundo segunda tercer tercero tercera
cuarto cuarta quinto quinta sexto sexta septimo septima octavo octava noveno novena decimo
decima undecimo undecima duodecimo duodecima ultimo ultima penultimo penultima""".split())
COLECTIVOS = frozenset("par pareja terna docena decena veintena centenar millar".split())
# FRACCIONES Y PROPORCIONES: `la mitad de los hallazgos` y `el 60% de los hallazgos`
# copian el mismo estado que `siete hallazgos`, y ningún detector de cardinales los ve.
# `cuarto` y `quinto` NO entran: en español son ordinal mucho más a menudo que fracción
# —`el cuarto gate`, `el documento 24 del CUARTO`—, y meterlos convertía cada referencia
# ordinal en un falso positivo. Quedan los inequívocos.
FRACCIONES = frozenset("mitad tercio tercios porciento".split())
# CUANTIFICADORES UNIVERSALES: `todos los gates fueron devueltos` copia un estado SIN
# ninguna cifra, y es la variante que sobrevive a cualquier detector numérico.
# `sendos`/`sendas` NO entran: son DISTRIBUTIVOS, no universales, y un crítico adversarial
# midió que el barrido anterior los enrojecía por contener la subcadena `dos`. Ese falso
# positivo trivial —y con él `los citados hallazgos`, `los mencionados gates`— es lo que
# se evita usando fronteras de palabra reales y no subcadenas.
# Sólo los universales que se predican de un CONJUNTO. `ningun adaptador existe` es una
# afirmación normativa en singular, no un recuento copiado; `todos los gates emitidos
# fueron devueltos` sí lo es, y es la variante que sobrevive a cualquier detector
# numérico porque no lleva ninguna cifra.
UNIVERSALES = frozenset("todos todas ambos ambas totalidad".split())
# Palabras que anuncian que lo enumerado se presenta como EXHAUSTIVO.
EXHAUSTIVOS = frozenset("son quedan restan vivos vivas vigentes abiertos abiertas "
                        "pendientes actuales".split())

ROMANO = re.compile(r"^(?=[MDCLXVI])M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})"
                    r"(IX|IV|V?I{0,3})$")
IDENTIFICADOR = re.compile(r"^(?:[A-ZÁÉÍÓÚÑ]{1,4}[0-9]*(?:[-.][A-Z0-9]+)*[-.]?[0-9]+[a-z]?"
                           r"|[A-ZÁÉÍÓÚÑ]-[A-Z]\.?[0-9]+|F[0-9]+[a-z]?|§[0-9.]+)$")
DIGEST = re.compile(r"^[0-9a-f]{7,64}$")
VERSION = re.compile(r"^v?[0-9]+\.[0-9]+(\.[0-9]+)?$")
FECHA_ISO = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}(T[0-9:.+Z-]+)?$")
FECHA_ROMANA = re.compile(r"^[0-9]{1,2}-[IVXLCDM]{1,7}-[0-9]{4}$")
MESES = frozenset("""enero febrero marzo abril mayo junio julio agosto septiembre setiembre
octubre noviembre diciembre""".split())
# Un comando de derivación. Es lo CONTRARIO de la clase: deriva en vez de copiar.
COMANDO = re.compile(r"\b(grep|awk|sed|git|wc|sort|uniq|comm|cut|head|tail|find|python3?"
                     r"|jq|xargs|diff|ls-tree|rev-parse)\b")
# La marca con la que una sede declara que un cardinal es un LÍMITE CONTRACTUAL CONSTANTE:
# lo cuantificado lo define esa misma sede, y no hay otra fuente competente que lo cuente.
MARCA_CONSTANTE = "[CONSTANTE CONTRACTUAL]"
ROTULOS_HISTORICOS = ("[HISTÓRICO", "[HISTORICO", "[CIFRA DE AQUEL MOMENTO",
                      "[ESTADO ANTERIOR]", "[ESTADO ANTERIOR ")


def _sin_acentos(texto):
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn")


def normalizar(texto):
    """NFKC, marcado retirado y TODO espacio convertido en espacio normal.

    Tres ataques del crítico caen aquí y sólo aquí: `**14** hallazgos` (marcado pegado a la
    cifra), `` `14` hallazgos `` (código en línea) y `14 hallazgos` (espacio duro,
    invisible al revisor). Y `１４` (dígitos fullwidth) se vuelve `14` con NFKC.
    """
    texto = unicodedata.normalize("NFKC", texto)
    texto = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", texto)            # enlaces markdown
    texto = re.sub(r"[*_`~]+", " ", texto)                            # marcado
    texto = "".join(" " if unicodedata.category(c) in ("Zs", "Cc") and c != "\n" else c
                    for c in texto)
    return texto


def valor_numeral(palabras):
    """Compone un numeral escrito con palabras. `None` si no lo es.

    Compone en vez de enumerar: por eso `treinta y un`, `doscientos` y `mil doscientos` se
    reconocen sin estar escritos en ninguna parte. El corpus registró que la lista anterior
    «se cortaba en catorce»; una lista que se corta es el defecto, no su longitud.
    """
    total, parcial, visto = 0, 0, False
    for palabra in palabras:
        p = _sin_acentos(palabra).lower()
        if p in UNIDADES:
            parcial += UNIDADES[p]; visto = True
        elif p in DECENAS:
            parcial += DECENAS[p]; visto = True
        elif p in CENTENAS:
            parcial += CENTENAS[p]; visto = True
        elif p in MULTIPLICADORES:
            parcial = (parcial or 1) * MULTIPLICADORES[p]
            total += parcial; parcial = 0; visto = True
        elif p == "y" and visto:
            continue
        else:
            return None
    return (total + parcial) if visto else None


def es_cifra(token):
    """¿Es este token un cardinal escrito con dígitos? Cubre los NO ASCII."""
    limpio = token.replace(".", "").replace(",", "").replace("%", "")
    return bool(limpio) and all(c.isdigit() for c in limpio)


def clasificar_excepcion(token, contexto):
    """Si este token cae en una excepción TIPADA, devuelve su tipo. Si no, `None`.

    Cada excepción tiene nombre y motivo, y se publican. `O31` §6 las enumera: fechas,
    versiones, identificadores normativos, SHA y digests, citas históricas rotuladas,
    límites contractuales realmente constantes, salidas generadas y comandos de derivación.
    """
    if FECHA_ISO.match(token) or FECHA_ROMANA.match(token):
        return "FECHA"
    if VERSION.match(token):
        return "VERSION"
    if DIGEST.match(token) and not token.isdigit():
        return "DIGEST"
    if IDENTIFICADOR.match(token):
        return "IDENTIFICADOR"
    if COMANDO.search(contexto):
        return "COMANDO"
    if MARCA_CONSTANTE in contexto:
        return "CONSTANTE"
    # Una cifra pegada a un nombre de mes, o rodeada de otras dos que forman fecha.
    palabras = [_sin_acentos(p).lower() for p in contexto.split()]
    if any(m in palabras for m in MESES):
        return "FECHA"
    return None


def nucleos_que_otra_sede_deriva(base):
    """Los sustantivos cuyo cardinal ALGUNA otra sede del corpus DERIVA. Se calcula.

    ES LA MITAD QUE FALTABA DE LA CLASE, y la dice `O31` §6 con todas sus letras: la copia
    es de un cardinal «que **debería derivarlo o remitir a su fuente competente**». Sin
    esta mitad, el control enrojece cualquier cardinal en prosa —medido: 637 sobre este
    árbol, casi todos narración— y obligaría a vaciar las sedes en vez de a derivar.

    La fuente NO se escribe: se recorre el corpus y se recogen los sustantivos que
    aparecen junto a una orden de derivación —una línea que cuenta con `wc -l`, `sort -u`,
    `grep -c`— o en la cabecera de un fichero `-generado.md`, que por definición publica lo
    derivado. Un cardinal nuevo que el corpus empiece a derivar entra solo en la clase.
    """
    nucleos = set()
    # LA FUENTE MÁS DIRECTA ES LA EVIDENCIA. Un instrumento que publica «24 invariantes
    # medidos» o «57 sabotajes declarados» ESTÁ DERIVANDO ese cardinal: es literalmente la
    # sede competente que `O31` §6 nombra. Recogerlo de ahí es más fiel que inferirlo de
    # una orden de conteo, y crece solo cuando un instrumento nuevo empieza a contar algo.
    evidencia = os.path.join(base, "kernel", "operativo", "pruebas", "evidencia")
    if os.path.isdir(evidencia):
        for nombre in sorted(os.listdir(evidencia)):
            if not nombre.endswith(".txt"):
                continue
            with open(os.path.join(evidencia, nombre), encoding="utf-8",
                      errors="replace") as manejador:
                for linea in manejador:
                    for m in re.finditer(r"(?<![\w-])\d+\s+([A-Za-zÁÉÍÓÚÑáéíóúñ]{4,})",
                                         linea):
                        pieza = m.group(1)
                        if es_sustantivo(pieza) and _es_plural(pieza):
                            nucleos.add(_sin_acentos(pieza).lower())
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "__pycache__", ".pytest_cache")]
        for nombre in sorted(filenames):
            if not nombre.endswith(".md"):
                continue
            ruta = os.path.join(dirpath, nombre)
            with open(ruta, encoding="utf-8", errors="replace") as manejador:
                texto = manejador.read()
            derivado = nombre.endswith("-generado.md")
            for linea in texto.split("\n"):
                if not (derivado or re.search(r"\b(wc -l|sort -u|grep -c|uniq -c)\b",
                                              linea)):
                    continue
                for token in normalizar(linea).split():
                    limpio = token.strip(".,;:()[]{}«»\"'|`")
                    if es_sustantivo(limpio) and _es_plural(limpio):
                        nucleos.add(_sin_acentos(limpio).lower())
    return nucleos


# NARRACIÓN EN PASADO FRENTE A ESTADO. `C-L.7` habla de copia de ESTADO: «y quedan los 14
# hallazgos abiertos» copia el estado de hoy; «H-09, H-10 y H-16 fueron tres instancias
# suyas» narra lo que pasó. La diferencia es morfológica y de clase cerrada —la conjugación
# del pretérito y del imperfecto del español—, no una lista de frases.
#
# Medido: sin esta distinción el control publica 127 hallazgos sobre este árbol y la mayoría
# son narración dentro de campos vivos. Enrojecerla obligaría a reescribir la historia
# contada en el bloque, que no es lo que `C-L.7` pide y que `O31` §1 prohíbe expresamente.
PASADO = re.compile(
    r"(?<![\w-])(?:fue|fueron|era|eran|iba|iban|hubo|habia|habian|tuvo|tuvieron|"
    r"estuvo|estuvieron|quedo|quedaron|dejo|dejaron|nombro|nombraron|demostro|"
    r"demostraron|caduco|caducaron|tomo|tomaron|escribio|escribieron|encontro|"
    r"encontraron|midio|midieron|publico|publicaron|declaro|declararon|corrigio|"
    r"corrigieron|aplico|aplicaron|retiro|retiraron|paso|pasaron|"
    r"[a-z]{2,}(?:aron|ieron|aba|abas|aban|ia|ian))(?![\w-])")


def _es_narracion(contexto):
    """¿La frase que rodea al cardinal está en PASADO? Entonces narra, no copia estado."""
    return bool(PASADO.search(_sin_acentos(contexto).lower()))


def _derivado(token, derivados):
    """¿Otra sede deriva el cardinal de ESTE núcleo? Se prueba también en plural.

    El conjunto se cosecha en plural —un recuento habla de un conjunto—, de modo que un
    núcleo en SINGULAR, como «queda 1 hallazgo bloqueante», no casaría nunca. Se prueba la
    forma tal cual y sus dos plurales regulares del español.
    """
    p = _sin_acentos(token.strip(".,;:()[]{}«»\"'|")).lower()
    return p in derivados or (p + "s") in derivados or (p + "es") in derivados


def _es_plural(token):
    """¿Es plural? Un recuento copiado habla de un CONJUNTO, y el conjunto va en plural."""
    p = _sin_acentos(token.strip(".,;:()[]{}«»\"'|")).lower()
    return p.endswith(("s", "es"))


def es_sustantivo(token):
    """¿Este token puede ser el NÚCLEO de lo cuantificado? Por DESCARTE, no por lista.

    Es el corazón de la inversión: no se pregunta «¿está en la lista de sustantivos?» —lista
    abierta que envejece— sino «¿NO es una palabra función, ni un numeral, ni un
    identificador?». Un sustantivo que nadie ha visto nunca cae aquí por descarte, y por eso
    un cardinal escrito después de este control no lo esquiva.
    """
    limpio = token.strip(".,;:()[]{}«»\"'¿?¡!").strip()
    if len(limpio) < 4:
        return False
    p = _sin_acentos(limpio).lower()
    if not p.isalpha():
        return False
    if p in PALABRAS_FUNCION or p in UNIDADES or p in DECENAS or p in CENTENAS:
        return False
    if p in MULTIPLICADORES or p in ORDINALES or p in UNIVERSALES:
        return False
    return True


# ===========================================================================
#  2 · LA POBLACIÓN · las SEDES VIVAS, derivadas y no enumeradas
# ===========================================================================
#  Una SEDE VIVA es un bloque que se declara a sí mismo estado reanudable. Se reconoce por
#  su propia declaración —`regla_de_reanclaje:`—, de modo que un bloque nuevo del mismo
#  género entra en la población sin que nadie lo apunte.
#
#  Y SE CUENTAN LOS CAMPOS, PORQUE UN CRÍTICO ADVERSARIAL MIDIÓ DOS FORMAS DE VACIAR LA
#  POBLACIÓN SIN TOCAR EL TEXTO SUCIO:
#
#    · una valla ``` a columna 0 dentro del bloque TRUNCA el barrido, y el censo bajaba de
#      catorce campos a seis sin que la salvaguarda —«compruébese que devuelve campos»— se
#      enterara, porque seis no es cero. La salvaguarda protegía del conjunto VACÍO, no del
#      TRUNCADO. Aquí el censo se contrasta contra el de `HEAD` y encoger es rojo;
#    · un campo con un nombre que el patrón no reconoce —`ESTADO_F6:`, `estado-f6:`— no
#      reiniciaba el rótulo histórico y HEREDABA la exención del campo anterior. Aquí,
#      cualquier línea a columna 0 con forma de campo que no encaje es roja.
DECLARACION_DE_SEDE_VIVA = "regla_de_reanclaje:"
CAMPO = re.compile(r"^([A-Za-zÁÉÍÓÚÑáéíóúñ_][A-Za-z0-9ÁÉÍÓÚÑáéíóúñ_]*):(.*)$")
PARECE_CAMPO = re.compile(r"^([^\s:#|>-][^:\n]{0,60}):(\s|$)")


def sedes_vivas(base):
    """`[(ruta, [(nombre_de_campo, texto, vigente)])]`, derivado del corpus."""
    halladas = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "__pycache__", ".pytest_cache")]
        for nombre in sorted(filenames):
            if not nombre.endswith(".md"):
                continue
            ruta = os.path.join(dirpath, nombre)
            with open(ruta, encoding="utf-8", errors="replace") as manejador:
                texto = manejador.read()
            if DECLARACION_DE_SEDE_VIVA not in texto:
                continue
            # UNA SEDE VIVA TIENE LAS DOS COSAS: la regla Y su fecha de reanclaje. Un gate
            # HISTÓRICO que CITA la regla no es una sede viva, y juzgarlo sería a la vez
            # inútil y prohibido —`O31` §11 protege los gates históricos—. Se exige, por
            # eso, que el bloque declare también `actualizado:`, que es lo que convierte un
            # bloque en estado reanudable y no en una cita.
            if "\nactualizado:" not in texto:
                continue
            rel = os.path.relpath(ruta, base).replace(os.sep, "/")
            halladas.append((rel, _campos_del_bloque(texto)))
    return halladas


def _campos_del_bloque(texto):
    """Los campos de la sede viva, con su texto COMPLETO y si están vigentes.

    El texto de un campo son TODAS sus líneas hasta el campo siguiente, unidas. Por eso un
    cardinal separado de su sustantivo por un salto de línea NO escapa: dentro del campo no
    hay saltos que valgan. El barrido anterior era por línea y ése era su tercer escape.
    """
    # EL BLOQUE ES LA VALLA QUE LO CONTIENE, NI MÁS NI MENOS.
    #
    #     Medido mientras se escribía esto: anclar en la declaración y leer hasta la
    #     siguiente valla daba SESENTA Y NUEVE campos —el bloque tiene los que caben entre
    #     su valla de apertura y la de cierre— y arrastraba prosa que no es estado
    #     reanudable. Un control que juzga más de lo que debe enrojece la narración entera
    #     y obliga a vaciarla, que es la regresión que `O31` §6 previene.
    lineas = texto.split("\n")
    try:
        declara = next(i for i, l in enumerate(lineas)
                       if l.strip().startswith(DECLARACION_DE_SEDE_VIVA))
    except StopIteration:
        return []
    aperturas = [i for i, l in enumerate(lineas) if l.startswith("```") and i < declara]
    if not aperturas:
        return []
    inicio = aperturas[-1] + 1
    cierres = [i for i, l in enumerate(lineas) if l.startswith("```") and i > declara]
    fin = cierres[0] if cierres else len(lineas)
    lineas = lineas[inicio:fin]
    inicio = 0
    campos, actual, cuerpo, sospechosas = [], None, [], []
    for linea in lineas[inicio:]:
        m = CAMPO.match(linea)
        if m:
            if actual is not None:
                campos.append((actual, "\n".join(cuerpo), _vigente(actual, cuerpo)))
            actual, cuerpo = m.group(1), [m.group(2)]
            continue
        if linea and not linea[0].isspace() and not m:
            # Línea a columna 0 que NO es campo. Si parece un campo con otro formato, es el
            # ataque del campo no reconocido; si es una valla, el bloque acaba de verdad.
            if linea.startswith("```"):
                break
            if PARECE_CAMPO.match(linea):
                sospechosas.append(linea.strip()[:70])
                continue
        cuerpo.append(linea)
    if actual is not None:
        campos.append((actual, "\n".join(cuerpo), _vigente(actual, cuerpo)))
    for sospechosa in sospechosas:
        campos.append(("__CAMPO_NO_RECONOCIDO__", sospechosa, True))
    return campos


def parrafos_vigentes(texto):
    """Los párrafos del campo que NO están bajo un rótulo histórico, según la regla 8.

    LA REGLA 8 DEL PROPIO BLOQUE, aplicada literalmente y no interpretada: «un
    `[HISTÓRICO …]` escrito DENTRO de una viñeta o de un párrafo alcanza hasta el final de
    esa viñeta o de ese párrafo, y no alcanza a la siguiente… Un `[HISTÓRICO …]` escrito EN
    LA LÍNEA DE APERTURA DEL CAMPO alcanza el campo entero. No hay una tercera forma».

    El segundo caso lo resuelve `_vigente`. Éste resuelve el primero, y hace falta: sin él
    el control reprocha lo que el bloque ya rotuló como historia —el defecto sería suyo, no
    del bloque—, y además pisaría `JA-01`, que es deuda registrada de otro propietario.

    Un PÁRRAFO aquí es un tramo separado por línea en blanco o por el comienzo de una
    viñeta —`·`, `-`, `*`, `•`—, que es el ancla que la regla 8 nombra.
    """
    parrafos, actual = [], []
    for linea in texto.split("\n"):
        desnuda = linea.strip()
        abre_vineta = desnuda.startswith(("·", "-", "*", "•"))
        if not desnuda or abre_vineta:
            if actual:
                parrafos.append(actual)
            actual = [linea] if abre_vineta else []
            continue
        actual.append(linea)
    if actual:
        parrafos.append(actual)
    vivos = []
    for parrafo in parrafos:
        crudo = "\n".join(parrafo)
        if any(r in crudo for r in ROTULOS_HISTORICOS):
            continue
        vivos.append(crudo)
    return vivos


def _es_campo_de_registro(nombre):
    """¿El NOMBRE del campo dice que registra algo YA HECHO, en vez de estado vigente?

    LA MORFOLOGÍA, NO UNA LISTA. Un campo llamado `resuelto_en_la_CUARTA_COMPROBACION`,
    `cerrado_en_el_NIVEL_0_DEL_GATE` o `devuelto_por_el_GATE_FINAL` no publica el estado de
    hoy: registra lo que una tanda pasada hizo. Se reconoce porque su primera palabra es un
    PARTICIPIO —`-ado`, `-ido`, `-uelto`, `-echo`, `-ito`, `-ento`—, que es clase cerrada
    del español y no crece con el corpus.

    POR QUÉ IMPORTA, MEDIDO. Sin esta distinción el control publica 367 hallazgos sobre
    este árbol y casi todos caen en campos de registro, que son historia sin rótulo: eso es
    `JA-01` —«el alcance del rótulo histórico es el del CAMPO, no el de la viñeta»—, deuda
    REGISTRADA con propietario y fase, y no la clase que `C-L.7` define. Meterla aquí sería
    ensanchar el universo por preferencia documental, que `O31` §9 prohíbe con esas
    palabras.
    """
    primera = _sin_acentos(nombre.split("_")[0]).lower()
    return primera.endswith(("ado", "ada", "ido", "ida", "uelto", "uelta", "echo", "echa"))


def _vigente(nombre, cuerpo):
    """Un campo es VIGENTE salvo que sea `_anterior`, de REGISTRO, o abra con rótulo.

    EL RÓTULO TIENE QUE ABRIR, y esto lo midió el crítico: bastaba MENCIONAR el literal en
    cualquier sitio —incluso negándolo: «este campo NO lleva rotulo [HISTORICO ...]»— para
    que el barrido eximiera todo lo que viniera detrás. Citar la regla dentro de un campo
    vigente eximía al campo. Ahora sólo cuenta en posición de apertura: primera línea del
    campo, o principio de una viñeta.
    """
    if nombre.endswith("_anterior") or _es_campo_de_registro(nombre):
        return False
    for linea in cuerpo:
        limpia = linea.strip().lstrip("·-*• ").strip()
        if limpia.startswith(ROTULOS_HISTORICOS):
            return False
        if limpia:
            break
    return True


# ===========================================================================
#  3 · LA DETECCIÓN · tres formas de la clase, ninguna por lista de sustantivos
# ===========================================================================
def hallazgos_en_campo(texto, derivados=None):
    """`[(forma, fragmento, motivo)]` de la clase dentro del texto de un campo vigente.

    `derivados` es el conjunto de núcleos que OTRA sede deriva. Si se pasa, sólo se
    reprocha el cardinal que recae sobre uno de ellos; si no —autopruebas—, se reprocha
    cualquiera, que es lo que las autopruebas necesitan para ejercer la forma.
    """
    hallazgos = []
    plano = normalizar(texto)
    # LA MARCA DE CONSTANTE EXIME SU LÍNEA, NI MÁS NI MENOS. Eximir el campo entero
    # convertiría la marca en una puerta de atrás; eximir una ventana de nueve palabras la
    # dejaba fuera de alcance cuando el cardinal iba al final de la frase.
    lineas_exentas = {i for i, l in enumerate(plano.split("\n")) if MARCA_CONSTANTE in l}
    if lineas_exentas:
        plano = "\n".join(l for i, l in enumerate(plano.split("\n"))
                           if i not in lineas_exentas)
    tokens = plano.split()
    minus = [_sin_acentos(t).lower().strip(".,;:()[]{}«»\"'") for t in tokens]

    def contexto(i, radio=9):
        return " ".join(tokens[max(0, i - radio):i + radio + 1])

    for i, token in enumerate(tokens):
        limpio = token.strip(".,;:()[]{}«»\"'¿?¡!")
        if not limpio:
            continue
        ctx = contexto(i)
        # UN NUMERAL DETRÁS DE `=` ES EL RESULTADO DE UNA FÓRMULA, NO UN RECUENTO COPIADO.
        # `OBLIGATORIO − ASIGNADO = 0` publica una resta DERIVADA: es lo contrario de la
        # clase, que es copiar lo que otra sede deriva.
        if i and tokens[i - 1].strip() in ("=", "==", "→", "⇒"):
            continue
        # 3.1 · CARDINAL, en cualquiera de sus formas, cuantificando un sustantivo.
        cardinal, forma = None, None
        if es_cifra(limpio):
            cardinal, forma = limpio, "cifra"
        elif minus[i] in COLECTIVOS:
            cardinal, forma = limpio, "colectivo"
        elif minus[i] in FRACCIONES or "%" in limpio:
            cardinal, forma = limpio, "fracción o proporción"
        elif minus[i] in ORDINALES and _es_plural(tokens[i + 1] if i + 1 < len(tokens)
                                                   else ""):
            # UN ORDINAL SOBRE UN SINGULAR NOMBRA UNA POSICIÓN, NO CUENTA UN CONJUNTO.
            # `el ÚLTIMO GATE`, `el TERCER GATE`, `un tercer agente`, `la primera adopción`
            # y `primera y última sección` señalan una pieza; sólo `los primeros tres
            # hallazgos` cuenta. `O31` §6 enumera lo que el control debe reconocer —cifras
            # con dígitos, cifras con palabras, caja, singular y plural, puntuación,
            # sustantivos desconocidos y cardinales posteriores— y el ordinal referencial
            # no está en esa lista. Medido: sin este acotamiento el control publicaba
            # veinticuatro hallazgos sobre este árbol y TODOS eran referencias.
            cardinal, forma = limpio, "ordinal"
        elif ROMANO.match(limpio) and len(limpio) > 1 and limpio.isupper():
            cardinal, forma = limpio, "romano"
        else:
            for largo in (4, 3, 2, 1):
                if valor_numeral(tokens[i:i + largo]) is not None:
                    if i > 0 and valor_numeral(tokens[i - 1:i + largo]) is not None:
                        break            # ya lo cubre el token anterior: no se duplica
                    cardinal = " ".join(tokens[i:i + largo])
                    forma = "numeral en palabras"
                    break
        if cardinal is not None:
            tipo = clasificar_excepcion(limpio, ctx)
            if tipo:
                continue
            # LA CLASE ES UN CARDINAL SOBRE UN CONJUNTO, Y ESO ACOTA DOS COSAS.
            #
            #     `un`, `una` y `uno` NO disparan por sí solos: en español son el artículo
            #     indefinido mucho más a menudo que el numeral, y `un producto real` o `un
            #     MVP` es prosa, no un recuento copiado. Siguen COMPONIENDO —`treinta y
            #     un hallazgos` cae entero— porque ahí el numeral es el compuesto.
            #
            #     Y el núcleo tiene que ser PLURAL cuando el cardinal es mayor que uno: un
            #     recuento copiado habla de un conjunto. Medido: sin estas dos reglas el
            #     control publicaba MIL CIENTO SETENTA Y SEIS hallazgos sobre este mismo
            #     árbol, casi todos prosa corriente, y un control que enrojece la prosa
            #     entera obliga a vaciar las sedes en vez de a derivar sus cardinales —que
            #     es la regresión que `O31` §6 previene al pedir que los comandos de
            #     derivación NO se enrojezcan—.
            valor = (int(cardinal.replace(".", "").replace(",", "").replace("%", ""))
                     if es_cifra(cardinal) else valor_numeral(cardinal.split()))
            if forma == "numeral en palabras" and valor == 1:
                continue
            plural_exigido = forma in ("cifra", "numeral en palabras") and (valor or 0) > 1
            # EL NÚCLEO PUEDE ESTAR A VARIAS PALABRAS, y puede ir DELANTE. `los 14 nuevos
            # hallazgos` mete un adjetivo por medio; `hallazgos abiertos: 14` y
            # `| hallazgos | 14 |` invierten el orden. El crítico midió las tres.
            # UN NUMERAL DETRÁS DE UN SUSTANTIVO SINGULAR ES UNA REFERENCIA, NO UN
            # RECUENTO. `documento 22`, `sección 2`, `regla 7`, `nivel 0` y `nodo 9`
            # NOMBRAN una pieza; `22 documentos` la CUENTA. La diferencia es morfológica y
            # de clase cerrada —posición del numeral y número gramatical del núcleo—, no
            # una lista de sustantivos referenciales, que volvería a envejecer.
            #
            # Medido: sin esta regla el control retiraba el `22` de «el documento 22» y el
            # `2` de «la sección 2», y una retirada mecánica dejaba el texto diciendo «el
            # documento» y «la sección». Un control que obliga a romper la prosa para
            # ponerse verde no cierra la clase: la traslada.
            anterior = tokens[i - 1].strip(".,;:()[]{}«»\"'|") if i else ""
            if es_sustantivo(anterior) and not _es_plural(anterior):
                continue
            # UNA LISTA DE NUMERALES DETRÁS DE UN PLURAL TAMBIÉN NOMBRA: `los documentos
            # 16, 17 y 18` enumera tres piezas por su número, no cuenta dieciséis de nada.
            # Se distingue del recuento invertido —`hallazgos abiertos: 14`— porque ahí el
            # numeral va SOLO. La señal es la lista, no el vocabulario.
            # La lista tiene que ser CONTIGUA: `documentos 16, 17 y 18` encadena numerales
            # sin nada entre ellos. `hallazgos abiertos: 14, bloqueantes: 2` NO es una
            # lista de numerales: hay un sustantivo por medio, y son dos recuentos.
            pegados = [tokens[j].strip(".,;:()[]{}«»\"'|")
                       for j in (i - 1, i + 1) if 0 <= j < len(tokens)]
            if es_cifra(limpio) and any(es_cifra(x) for x in pegados):
                if any(tokens[j].endswith(",") for j in (i - 1, i) if 0 <= j < len(tokens)):
                    continue
            if derivados is not None and _es_narracion(ctx):
                continue

            # EL NÚCLEO VA DELANTE A LO SUMO DOS PALABRAS Y DETRÁS HASTA CUATRO. Delante
            # sólo cabe el recuento invertido —`hallazgos abiertos: 14`—, que es corto;
            # detrás cabe el adjetivo intercalado —`los 14 nuevos hallazgos`—. Sin este
            # acotamiento el control elegía como núcleo una palabra a cuatro de distancia y
            # publicaba «cardinal PRIMERA cuantificando además», que no dice nada.
            ventana = [t for t in tokens[max(0, i - 2):i] + tokens[i + 1:i + 5]]
            nucleos = [t for t in ventana if es_sustantivo(t)
                       and (not plural_exigido or _es_plural(t))
                       and (derivados is None or _derivado(t, derivados))]
            if nucleos:
                hallazgos.append((forma, ctx.strip()[:150],
                                  "cardinal `%s` cuantificando `%s`"
                                  % (cardinal, nucleos[0].strip(".,;:()[]|"))))
                continue
        # 3.2 · CUANTIFICADOR UNIVERSAL sobre un conjunto que otra sede publica. No hay
        #       cifra ninguna, y por eso ningún detector numérico lo vio nunca.
        if minus[i] in UNIVERSALES:
            if clasificar_excepcion(limpio, ctx):
                continue
            if derivados is not None and _es_narracion(ctx):
                continue
            nucleos = [t for t in tokens[i + 1:i + 5]
                       if es_sustantivo(t) and _es_plural(t)
                       and (derivados is None or _derivado(t, derivados))]
            if nucleos:
                hallazgos.append(("universal", ctx.strip()[:150],
                                  "`%s` sobre `%s`: cuantifica por extensión un conjunto "
                                  "que otra sede publica"
                                  % (limpio, nucleos[0].strip(".,;:()[]|"))))
                continue

    # 3.3 · ENUMERACIÓN EXHAUSTIVA de identificadores del corpus. Enumerar es contar por
    #       extensión, y no deja ninguna cifra que buscar.
    # UNA ENUMERACIÓN ES UNA LISTA, NO IDENTIFICADORES DISPERSOS. `O23` §11 … `O24` … `F6`
    # citados a lo largo de un párrafo NOMBRAN piezas; `H-09, H-10, H-16 y X-04` las
    # ENUMERA. La señal es la contigüidad: en una lista los identificadores van separados
    # por coma o por `y`, no por frases enteras.
    identificadores, corrida, mejor = [], [], []
    for j, bruto in enumerate(tokens):
        pieza = bruto.strip(".,;:()[]{}«»\"'")
        if IDENTIFICADOR.match(pieza):
            corrida.append(pieza)
        elif _sin_acentos(pieza).lower() in ("y", "e", "o", "u", "·") or not pieza:
            continue
        else:
            if len(corrida) > len(mejor):
                mejor = corrida
            corrida = []
    if len(corrida) > len(mejor):
        mejor = corrida
    identificadores = mejor
    if len(identificadores) >= 3 and any(p in minus for p in EXHAUSTIVOS):
        if not COMANDO.search(plano) and MARCA_CONSTANTE not in plano:
            hallazgos.append(("enumeración", " ".join(identificadores[:8]),
                              "%d identificadores enumerados junto a una palabra que los "
                              "presenta como el conjunto vigente: es un conjunto variable "
                              "copiado" % len(identificadores)))
    return hallazgos


# ===========================================================================
#  4 · EL JUICIO · seis condiciones, todas fallan cerrado
# ===========================================================================
def _censo_en_head(base, rel):
    """Cuántos campos tenía esa sede en `HEAD`. `None` si no hay historia."""
    proc = subprocess.run(["git", "-C", base, "show", "HEAD:%s" % rel],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        return None
    return len([c for c in _campos_del_bloque(proc.stdout)
                if c[0] != "__CAMPO_NO_RECONOCIDO__"])


def juzgar(base):
    """`(fallos, censo, derivados)`. Cada fallo es `(condicion, sede, campo, forma, motivo, texto)`."""
    fallos, censo = [], []
    sedes = sedes_vivas(base)
    derivados = nucleos_que_otra_sede_deriva(base)
    if len(derivados) < 5:
        fallos.append(("L-05", "-", "-", "-",
                       "sólo se han derivado %d núcleos que otra sede cuenta: con un "
                       "conjunto tan pequeño la condición `L-04` pasaría por construcción, "
                       "y eso no es un verde" % len(derivados), ""))

    # `L-01` · ANTITAUTOLOGÍA. Sin sedes o sin campos, todo lo demás pasa por construcción.
    if not sedes:
        fallos.append(("L-01", "-", "-", "-",
                       "no se ha hallado NINGUNA sede viva: un control que no mira nada "
                       "sale verde siempre y no es un control", ""))
    for rel, campos in sedes:
        vivos = [c for c in campos if c[0] != "__CAMPO_NO_RECONOCIDO__"]
        vigentes = [c for c in vivos if c[2]]
        antes = _censo_en_head(base, rel)
        censo.append((rel, len(vivos), len(vigentes), antes))
        if not vivos:
            fallos.append(("L-01", rel, "-", "-",
                           "la sede no publica ni un campo: el bloque no se está leyendo",
                           ""))
        # `L-02` · EL CENSO NO PUEDE ENCOGER. Truncar el bloque con una valla bajaba el
        #     censo sin vaciarlo, y la salvaguarda anterior sólo protegía del cero.
        if antes is not None and len(vivos) < antes:
            fallos.append(("L-02", rel, "-", "-",
                           "el censo de campos ha ENCOGIDO: `HEAD` tenía %d y este árbol "
                           "publica %d. Truncar el bloque deja el control mirando menos de "
                           "lo que debe, y un censo menor no es un censo vacío: la "
                           "salvaguarda del cero no lo veía" % (antes, len(vivos)), ""))
        # `L-03` · NINGUNA LÍNEA A COLUMNA 0 CON FORMA DE CAMPO SE QUEDA SIN RECONOCER.
        for nombre, texto, _v in campos:
            if nombre == "__CAMPO_NO_RECONOCIDO__":
                fallos.append(("L-03", rel, texto, "-",
                               "línea a columna 0 con forma de campo que el censo no "
                               "reconoce. Un campo con otro formato no reinicia el rótulo "
                               "histórico y HEREDA la exención del campo anterior", texto))
        # `L-04` · LA CLASE, dentro de los campos VIGENTES.
        for nombre, texto, _v in vigentes:
            for forma, fragmento, motivo in hallazgos_en_campo(
                    "\n".join(parrafos_vigentes(texto)), derivados):
                fallos.append(("L-04", rel, nombre, forma, motivo, fragmento))
    return fallos, censo, derivados


# ===========================================================================
#  5 · LO QUE SE PUBLICA
# ===========================================================================
def publicar(destino, base, fallos, censo, derivados):
    destino.write("`O31` §6 · `C-L.7` · COPIA MANUAL DE ESTADO EN SEDE VIVA, POR CLASE\n")
    destino.write("=" * 78 + "\n\n")
    commit = subprocess.run(["git", "-C", base, "rev-parse", "HEAD"], capture_output=True,
                            text=True).stdout.strip()
    tree = subprocess.run(["git", "-C", base, "rev-parse", "HEAD^{tree}"],
                          capture_output=True, text=True).stdout.strip()
    destino.write("  ANCLA   commit %s · tree %s\n\n" % (commit or "?", tree or "?"))

    destino.write("LA CLASE QUE SE JUZGA\n")
    destino.write("-" * 78 + "\n")
    destino.write("  copia manual de estado, cardinal o conjunto variable dentro de una\n"
                  "  sede viva que debería derivarlo o remitir a su fuente competente.\n\n"
                  "  NO se enumeran los sustantivos —clase ABIERTA que crece con el\n"
                  "  corpus—: se enumeran las clases CERRADAS del español, palabras\n"
                  "  función y numerales, y el núcleo cuantificado cae por DESCARTE. Un\n"
                  "  sustantivo que este control no ha visto nunca no lo esquiva.\n\n")

    destino.write("LA POBLACIÓN, DERIVADA\n")
    destino.write("-" * 78 + "\n")
    destino.write("  %-56s %6s %8s %6s\n" % ("sede viva", "campos", "vigentes", "HEAD"))
    for rel, vivos, vigentes, antes in censo:
        destino.write("  %-56s %6d %8d %6s\n"
                      % (rel, vivos, vigentes, "-" if antes is None else antes))
    destino.write("\n")

    destino.write("LAS EXCEPCIONES, TIPADAS Y JUSTIFICADAS\n")
    destino.write("-" * 78 + "\n")
    for tipo, motivo in (
            ("FECHA", "una fecha no cuantifica nada que otra sede cuente"),
            ("VERSION", "una versión es identidad, no recuento"),
            ("IDENTIFICADOR", "`O31`, `T158`, `V6-18` o `§6` nombran, no cuentan"),
            ("DIGEST", "un SHA o un digest es identidad del objeto"),
            ("COMANDO", "una orden que DERIVA el valor es lo contrario de copiarlo"),
            ("CONSTANTE", "un límite que define esta misma sede y que ninguna otra "
                          "cuenta, declarado con `%s`" % MARCA_CONSTANTE),
            ("HISTÓRICO", "campo `_anterior`, o rótulo histórico EN POSICIÓN DE APERTURA "
                          "—mencionarlo en medio de una frase ya no exime")):
        destino.write("  %-14s %s\n" % (tipo, motivo))
    destino.write("\n")

    destino.write("LO HALLADO\n")
    destino.write("-" * 78 + "\n")
    if not fallos:
        destino.write("  ninguno\n")
    for condicion, sede, campo, forma, motivo, texto in fallos:
        destino.write("  [%s] %s · campo `%s` · %s\n      %s\n"
                      % (condicion, sede, campo, forma, motivo))
        if texto:
            destino.write("      «%s»\n" % texto.strip()[:140])
    destino.write("\n")

    destino.write("LO QUE ESTE VEREDICTO NO DEMUESTRA\n")
    destino.write("-" * 78 + "\n")
    destino.write(
        "  · no demuestra que ninguna sede del corpus copie estado: juzga las SEDES\n"
        "    VIVAS, que son las que se declaran estado reanudable;\n"
        "  · no cierra `C-L.7`: `O31` §6 lo reserva al verificador independiente, y le\n"
        "    exige demostrarlo con variantes que el implementador no usó;\n"
        "  · no juzga si un cardinal es CIERTO: juzga si está COPIADO donde debería\n"
        "    derivarse o remitirse.\n\n")

    destino.write("%d sedes vivas · %d campos · %d vigentes · %d núcleos derivados por "
                  "otra sede · %d hallazgos de la clase\n"
                  % (len(censo), sum(c[1] for c in censo), sum(c[2] for c in censo),
                     len(derivados), len(fallos)))
    return TODOS_SATISFECHOS if not fallos else HAY_INCUMPLIDOS


# ===========================================================================
#  6 · AUTOPRUEBAS · las variantes conocidas, las del crítico y los negativos
# ===========================================================================
#  Las positivas tienen que salir ROJAS y las negativas LIMPIAS. Un control que caza todo
#  no es un control: es un `grep` de dígitos, y haría que las sedes retiraran sus comandos
#  de derivación, que es la regresión exacta que `O31` §6 previene.
POSITIVAS = [
    ("dígitos", "y quedan los 14 hallazgos abiertos"),
    ("letras", "y quedan los catorce hallazgos abiertos"),
    ("VERSALES", "Y QUEDAN LOS CATORCE HALLAZGOS ABIERTOS"),
    ("singular", "queda 1 hallazgo bloqueante"),
    ("sustantivo desconocido", "y quedan los 24 invariantes criticos"),
    ("sustantivo desconocido 2", "y quedan las 58 obligaciones internas"),
    ("puntuación alterada", "hallazgos abiertos: 14, bloqueantes: 2"),
    ("cardinal posterior al control", "y quedan los 57 sabotajes declarados"),
    ("salto de línea", "y quedan los catorce\n  hallazgos abiertos"),
    ("adjetivo intercalado", "los 14 nuevos hallazgos siguen abiertos"),
    ("marcado markdown", "quedan **14** hallazgos abiertos"),
    ("código en línea", "quedan `14` hallazgos abiertos"),
    ("espacio duro", "quedan 14 hallazgos abiertos"),
    ("orden invertido", "hallazgos abiertos: 14"),
    ("tabla", "| hallazgos | 14 |"),
    ("enumeración sin cardinal",
     "los hallazgos vivos son H-09, H-10, H-16, X-04 y JA-01"),
    ("estado sin cifra", "todos los gates emitidos fueron devueltos"),
    ("numeral compuesto", "treinta y un hallazgos siguen abiertos"),
    ("numeral fuera de lista", "doscientos contratos tecnicos declarados"),
    ("fracción", "la mitad de los hallazgos sigue abierta"),
    ("dígitos fullwidth", "quedan １４ hallazgos abiertos"),
    ("romano", "XIV hallazgos siguen abiertos"),
    ("colectivo", "una decena larga de hallazgos sigue abierta"),
]
NEGATIVAS = [
    ("fecha rara", "reanclado el 02-IX-2026, y antes el 2026-08-30T14:05:00Z"),
    ("versión", "exige Python 3.12; con 3.10 el arbol no arranca"),
    ("identificadores normativos", "lo manda `O31` §6, lo recogen `T158` y `T350`"),
    ("SHA cortos", "la candidata se congelo en `4d99a5e`, y antes en `57fc58e`"),
    ("ordinal referencial", "el septimo hallazgo bloqueante sigue sin cerrar"),
    ("cita histórica rotulada",
     "[HISTÓRICO · CIFRA DE AQUEL MOMENTO] eran 14 hallazgos y 2 bloqueantes"),
    ("comando de derivación",
     "grep -oE '^# `O[0-9]+`' docs/owner/ADS-OWNER-RESOLUCIONES.md | wc -l"),
    ("límite contractual constante",
     "%s un rotulo historico tiene exactamente dos anclas y no hay una tercera"
     % MARCA_CONSTANTE),
    ("participio en -dos", "los citados hallazgos y los mencionados gates"),
    ("sendos", "sendos hallazgos quedaron abiertos"),
]


def autopruebas(destino):
    destino.write("`O31` §6 · AUTOPRUEBAS DEL CONTROL DE CLASE DE `C-L.7`\n")
    destino.write("=" * 78 + "\n\n")
    fallidos = []
    destino.write("POSITIVAS · tienen que salir ROJAS\n")
    destino.write("-" * 78 + "\n")
    for nombre, texto in POSITIVAS:
        hallado = hallazgos_en_campo(texto)
        ok = bool(hallado)
        if not ok:
            fallidos.append(("positiva", nombre, texto))
        destino.write("%-5s %-30s %s\n"
                      % ("OK" if ok else "FALLO", nombre,
                         (hallado[0][2][:70] if hallado else "NO DETECTADA")))
    destino.write("\nNEGATIVAS · tienen que salir LIMPIAS\n")
    destino.write("-" * 78 + "\n")
    for nombre, texto in NEGATIVAS:
        if nombre == "cita histórica rotulada":
            limpio = not _vigente("campo", texto.split("\n"))
        else:
            limpio = not hallazgos_en_campo(texto)
        if not limpio:
            fallidos.append(("negativa", nombre, texto))
        destino.write("%-5s %-30s %s\n"
                      % ("OK" if limpio else "FALLO", nombre,
                         "limpia" if limpio else
                         hallazgos_en_campo(texto)[0][2][:70]))
    destino.write("\n%d controles · %d sin detectar\n"
                  % (len(POSITIVAS) + len(NEGATIVAS), len(fallidos)))
    return HAY_INCUMPLIDOS if fallidos else TODOS_SATISFECHOS


def main(argv=None):
    analizador = argparse.ArgumentParser(
        description="`O31` §6 · `C-L.7` juzgado por CLASE y no por lista de sustantivos")
    analizador.add_argument("--raiz", default=None)
    analizador.add_argument("--autopruebas", action="store_true")
    argumentos = analizador.parse_args(argv)
    base = os.path.abspath(argumentos.raiz) if argumentos.raiz else RAIZ
    if argumentos.autopruebas:
        return autopruebas(sys.stdout)
    fallos, censo, derivados = juzgar(base)
    return publicar(sys.stdout, base, fallos, censo, derivados)


if __name__ == "__main__":
    sys.exit(main())
