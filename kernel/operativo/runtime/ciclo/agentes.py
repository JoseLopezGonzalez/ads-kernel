#!/usr/bin/env python3
"""agentes — el PASO 4 de `C4`, ejecutado con la política de `C2` sobre el catálogo REAL.

`C4` paso 4 es una línea: «ASIGNAR AGENTES: por cada rol, aplicar la política de `C2`.
Registrar modelo elegido, descartados y motivo». La política de `C2` son seis pasos —LEER
PERFIL · FILTRAR por ejes · FILTRAR herramientas y contexto · ORDENAR · ASIGNAR ·
DEGRADAR—, y este módulo los ejecuta tal como están escritos, sin añadir ninguno y sin
saltarse ninguno.

DECISIÓN · el VOCABULARIO se DERIVA de `esquemas/perfil-agente.yaml`, y no se copia aquí
    Los siete ejes, sus niveles, el orden del esquema —que es el desempate del eje
    dominante—, los cuatro tamaños de contexto y los cuatro escalones de coste están
    escritos UNA vez, en el esquema. Copiarlos aquí crearía una segunda sede que puede
    desincronizarse en silencio: la primera vez que alguien añadiera un eje, este módulo
    seguiría filtrando por siete y nada lo diría. `Politica` los lee del esquema en cada
    construcción, y por eso `vision: no` —que el YAML entrega como booleano `False`— se
    normaliza en un solo sitio, contra los valores que el propio esquema declara.

DECISIÓN · el CATÁLOGO DE MODELOS vive en el PROFILE del PROYECTO, nunca en el kernel
    `C2` es literal en los cuatro conceptos: «ADAPTADOR — traducción entre un perfil y los
    modelos reales de un proveedor. Vive en el PROFILE del proyecto o en la instalación,
    NUNCA en el kernel», y su regla de portabilidad remata: «ningún fichero de
    `kernel/operativo/` ni de `packs/` nombra un proveedor, un modelo comercial ni una
    herramienta de marca como requisito». Por eso aquí NO hay ni un identificador de
    modelo: el catálogo se LEE del `PROFILE.md` del control repo, que es lo que
    `encuadre.cargar_perfil` ya localiza, y en bloques ```yaml ads:modelo``` que son el
    ESPEJO EXACTO del esquema `perfil-agente` —`exige` pasa a `ofrece`, y caen los dos
    campos que son del perfil y no del modelo—. La forma se DERIVA del esquema; las
    instancias son del proyecto.

DECISIÓN · sin catálogo, FALLO CERRADO: el rol queda BLOQUEADO y no se despacha
    Alternativas: (a) un modelo por defecto cuando el proyecto no declara catálogo; (b)
    dejar el rol sin agente y no despacharlo.
    Se elige (b). (a) es exactamente lo que `C4` prohíbe —«PROHIBIDO materializar un rol
    sin asignarle agente: un rol vacío no es un rol»— disfrazado de comodidad, y además
    nombraría un modelo dentro del kernel, que es lo que `K0.8` prohíbe. Un proyecto sin
    catálogo no tiene agentes: decirlo es correcto, inventarlos no.

DECISIÓN · `coste` ORDENA, y NO filtra
    `C2` coloca el coste en el paso 4 —ORDENAR—, no en los pasos 2 y 3, que son los que
    FILTRAN, y lo dice con todas las letras: «`coste` es un techo, no un criterio de
    diseño. Ordena entre candidatos que ya cumplen; nunca sustituye a un candidato que
    cumple por otro que no». Y el paso 6 dispara la degradación «si NINGÚN modelo cumple»,
    donde cumplir es cumplir el PERFIL, no el precio. De ahí la clave de orden: primero el
    eje dominante, después los que están dentro del techo, después el coste ascendente, y
    el identificador como desempate. Un candidato por encima del techo NO se descarta: se
    ordena detrás, porque descartarlo sí sería sustituir a un candidato que cumple.

DECISIÓN · el EJE DOMINANTE es el NIVEL `maximo` de `C2`, al pie de la letra
    `C2` paso 4 (a) dice «el declarado en `exige` con nivel `maximo`, y si hay varios, el
    primero por orden del esquema», y eso es lo que se ejecuta: se busca el NIVEL `maximo`,
    no «el tope de su eje».

    La distinción no es retórica y una auditoría independiente la midió. Generalizar a «el
    tope de su eje» mete a `vision` en la carrera —su escala es `no` · `util` · `requerida`,
    cuyo tope es `requerida`— y la adelanta por delante de un eje que sí pide `maximo`.
    Diverge en dos de los veintiún perfiles del kernel: `perfil:investigacion-visual`, donde
    `C2` dice `investigacion` y salía `vision`, y `perfil:prototipado`, donde `C2` dice
    `programacion` y salía `vision`. Bajo la letra de `C2`, `vision` NO PUEDE ser nunca el
    eje dominante, porque su escala no contiene ese nivel. El valor se PUBLICA en el
    registro auditable de la asignación, de modo que publicarlo mal es publicar una razón
    falsa, aunque en ambos casos los dos ejes empaten en el filtro y la elección de modelo
    no cambie.

    El caso que `C2` NO contempla —un perfil sin ningún eje en `maximo`, y
    `perfil:interlocucion` es uno— se resuelve con la MISMA regla de desempate que `C2`
    escribe para el caso que sí contempla: el nivel más alto que el perfil pida, y entre los
    que lo empatan el primero por orden del esquema. Sin regla, el criterio (a) se quedaría
    sin contenido y la elección la gobernaría el coste, que es justo lo que `C2` prohíbe. Va
    marcado como `DERIVADO` en el motivo publicado, para que se lea como derivación y no
    como cita.

DECISIÓN · la DEGRADACIÓN nunca se infiere del texto de `degradacion_permitida`
    Ese campo es `{tipo: texto}` en el esquema, y su contenido es prosa castellana dirigida
    a quien decide («ninguna en el eje razonamiento ni en critica», «con vision no
    disponible el rol construye pero NO juzga el resultado»). Derivar de ahí una regla
    ejecutable exigiría reglas léxicas sobre texto libre, que es precisamente lo que la
    regla 2 de este paquete prohíbe. Por tanto: NINGUNA degradación es automática. Si
    ningún modelo cumple, el paquete queda `bloqueado` nombrando qué capacidad de modelo
    falta —`C2` paso 6— y el registro lleva el texto de `degradacion_permitida` VERBATIM
    para quien tenga que decidir. Una degradación puede APLICARSE, pero sólo DECLARADA como
    dato, eje a eje y con su motivo, y entonces queda escrita en el registro con el sello
    `degradado: true`. Inferida jamás; declarada siempre que alguien la firme.
"""
from __future__ import annotations

import os

from estado.serializacion import cid_de_objeto

from .corpus import Corpus, bloques
from .errores import (
    CatalogoDeModelosAusente,
    CatalogoDeModelosInvalido,
    CorpusIncompleto,
    DegradacionInvalida,
    PerfilDesconocido,
)

# La sede del catálogo: el `PROFILE.md` del control repo, que es el mismo fichero que
# `encuadre.PERFIL` localiza. Se declara aquí por su nombre para no importar en círculo.
PERFIL_DEL_PROYECTO = "PROFILE.md"

# El tipo de bloque canónico del catálogo. Es el ESPEJO de `ads:perfil-agente`.
BLOQUE_DE_MODELO = "modelo"

# Los dos campos del esquema `perfil-agente` que son del PERFIL y no del MODELO: un modelo
# no declara qué degradación admite —eso lo exige el rol— ni qué le está prohibido.
CAMPOS_SOLO_DEL_PERFIL = ("degradacion_permitida", "prohibido")

# `exige` en el perfil es `ofrece` en el modelo. Es el único renombrado del espejo.
ESPEJO = {"exige": "ofrece"}

ESTADO_ASIGNADO = "asignado"
ESTADO_BLOQUEADO = "bloqueado"

REGLA_EJES = "`C2` paso 2 · cumplir o superar cada exigencia del perfil"
REGLA_HERRAMIENTAS = "`C2` paso 3 · herramientas declaradas"
REGLA_CONTEXTO = "`C2` paso 3 · tamaño de contexto"


def _texto_de_nivel(valor):
    """`vision: no` llega del YAML como booleano. La escala es de TEXTO en el esquema."""
    if valor is False:
        return "no"
    if valor is True:
        return "si"
    return str(valor)


# ===========================================================================
#  la política de `C2`, DERIVADA del esquema `perfil-agente`
# ===========================================================================
class Politica:
    """Los siete ejes, sus escalas y su ORDEN, leídos del esquema. No se copian aquí."""

    def __init__(self, corpus=None):
        self.corpus = corpus or Corpus()
        esquema = self.corpus.esquema("perfil-agente")
        campos = esquema.get("campos") or {}
        exige = campos.get("exige") or {}
        declarados = exige.get("campos") or {}
        obligatorios = exige.get("obligatorios") or []
        if not declarados or not obligatorios:
            raise CorpusIncompleto(
                "el esquema `perfil-agente` no declara los ejes de `exige`",
                ruta="esquemas/perfil-agente.yaml",
            )
        if sorted(declarados) != sorted(str(c) for c in obligatorios):
            raise CorpusIncompleto(
                "el esquema `perfil-agente` declara unos ejes en `obligatorios` y otros "
                "en `campos`; sin una sola lista no hay orden del esquema que aplicar",
                ruta="esquemas/perfil-agente.yaml",
            )
        # El ORDEN DEL ESQUEMA es el orden en que están escritos los campos, y es lo que
        # `C2` paso 4 (a) usa como desempate del eje dominante.
        self.ejes = tuple(declarados)
        self.niveles = {
            eje: tuple(_texto_de_nivel(v) for v in (declarados[eje].get("valores") or []))
            for eje in self.ejes
        }
        for eje, escala in self.niveles.items():
            if len(escala) < 2:
                raise CorpusIncompleto(
                    "el eje `" + eje + "` no declara una escala de niveles",
                    ruta="esquemas/perfil-agente.yaml",
                )
        self.contextos = tuple(
            _texto_de_nivel(v) for v in ((campos.get("contexto") or {}).get("valores") or []))
        self.costes = tuple(
            _texto_de_nivel(v) for v in ((campos.get("coste") or {}).get("valores") or []))
        if not self.contextos or not self.costes:
            raise CorpusIncompleto(
                "el esquema `perfil-agente` no declara las escalas de `contexto` y `coste`",
                ruta="esquemas/perfil-agente.yaml",
            )
        self.obligatorios_de_perfil = tuple(str(c) for c in (esquema.get("obligatorios") or []))
        self.patron_de_modelo = str(
            ((campos.get("id") or {}).get("patron") or "")).replace("perfil", "modelo")
        self._perfiles = None
        self._roles = None

    # ------------------------------------------------------- espejo del esquema
    @property
    def obligatorios_de_modelo(self):
        """El ESPEJO: los campos del perfil, con `exige` → `ofrece` y sin los dos del rol."""
        return tuple(
            ESPEJO.get(campo, campo) for campo in self.obligatorios_de_perfil
            if campo not in CAMPOS_SOLO_DEL_PERFIL
        )

    # -------------------------------------------------------------- escalas
    def indice(self, eje, valor):
        escala = self.niveles[eje]
        texto = _texto_de_nivel(valor)
        if texto not in escala:
            raise CatalogoDeModelosInvalido(
                "`" + texto + "` no es un nivel del eje `" + eje + "`; la escala es "
                + " < ".join(escala),
                eje=eje, valor=texto,
            )
        return escala.index(texto)

    def indice_de_contexto(self, valor):
        texto = _texto_de_nivel(valor)
        if texto not in self.contextos:
            raise CatalogoDeModelosInvalido(
                "`" + texto + "` no es un tamaño de contexto; la escala es "
                + " < ".join(self.contextos), valor=texto,
            )
        return self.contextos.index(texto)

    def indice_de_coste(self, valor):
        texto = _texto_de_nivel(valor)
        if texto not in self.costes:
            raise CatalogoDeModelosInvalido(
                "`" + texto + "` no es un escalón de coste; la escala es "
                + " < ".join(self.costes), valor=texto,
            )
        return self.costes.index(texto)

    def tope(self, eje):
        """El nivel más alto del eje. Para los seis es `maximo`; para `vision`, `requerida`."""
        return self.niveles[eje][-1]

    # -------------------------------------------------------------- perfiles
    def perfiles(self):
        """Los perfiles DERIVADOS del corpus, validados contra su propio esquema."""
        if self._perfiles is None:
            salida = {}
            for datos in self.corpus.de_tipo("perfil-agente"):
                identificador = datos.get("id")
                if not isinstance(identificador, str):
                    raise CorpusIncompleto("un bloque `ads:perfil-agente` sin `id`")
                if identificador in salida:
                    raise CorpusIncompleto(
                        "dos bloques declaran `" + identificador + "`")
                faltan = [c for c in self.obligatorios_de_perfil if c not in datos]
                if faltan:
                    raise CorpusIncompleto(
                        "el perfil `" + identificador + "` no declara "
                        + ", ".join(faltan), ruta=identificador,
                    )
                salida[identificador] = datos
            if not salida:
                raise CorpusIncompleto("el corpus no declara ningún `ads:perfil-agente`")
            self._perfiles = salida
        return self._perfiles

    def perfil(self, identificador):
        catalogo = self.perfiles()
        if identificador not in catalogo:
            raise PerfilDesconocido(
                "el corpus no declara `" + str(identificador) + "`; declarados: "
                + ", ".join(sorted(catalogo)), perfil=str(identificador),
            )
        return catalogo[identificador]

    # ----------------------------------------------------------------- roles
    def roles(self):
        if self._roles is None:
            salida = {}
            for datos in self.corpus.de_tipo("rol"):
                identificador = datos.get("id")
                if isinstance(identificador, str):
                    salida[identificador] = datos
            self._roles = salida
        return self._roles

    def perfil_de_rol(self, rol):
        """`C2` paso 1: el rol DECLARA su `perfil_agente`. No se adivina por su nombre."""
        catalogo = self.roles()
        if rol not in catalogo:
            raise PerfilDesconocido(
                "el corpus no declara el rol `" + str(rol) + "`, y un rol sin contrato no "
                "tiene perfil que aplicar", rol=str(rol),
            )
        declarado = catalogo[rol].get("perfil_agente")
        if not isinstance(declarado, str) or not declarado.strip():
            raise PerfilDesconocido(
                "el rol `" + str(rol) + "` no declara `perfil_agente`, que el esquema "
                "`rol` exige", rol=str(rol),
            )
        return declarado.strip()

    # ------------------------------------------------------------ exigencias
    def exigencia_de_perfil(self, identificador):
        """La exigencia EJECUTABLE de un perfil: ejes, contexto, herramientas y techo."""
        perfil = self.perfil(identificador)
        exige = perfil.get("exige") or {}
        faltan = [eje for eje in self.ejes if eje not in exige]
        if faltan:
            raise CorpusIncompleto(
                "el perfil `" + identificador + "` no exige " + ", ".join(faltan),
                ruta=identificador,
            )
        ejes = {}
        for eje in self.ejes:
            nivel = _texto_de_nivel(exige[eje])
            self.indice(eje, nivel)
            ejes[eje] = nivel
        contexto = _texto_de_nivel(perfil.get("contexto"))
        self.indice_de_contexto(contexto)
        coste = _texto_de_nivel(perfil.get("coste"))
        self.indice_de_coste(coste)
        herramientas = [str(h) for h in (perfil.get("herramientas") or [])]
        return {
            "perfiles": [identificador],
            "ejes": ejes,
            "contexto": contexto,
            "herramientas": sorted(set(herramientas)),
            "coste": coste,
            "degradacion_permitida": str(perfil.get("degradacion_permitida") or "").strip(),
        }

    def combinar(self, exigencias):
        """La exigencia de un AGENTE que ocupa VARIOS roles: el máximo de cada eje.

        `C2` define el agente como «modelo + instrucciones + herramientas + contexto +
        presupuesto + rol o roles que ocupa»: UN modelo. Si dos roles combinables van a
        compartir agente, el modelo tiene que cumplir los DOS perfiles, y eso es el máximo
        eje a eje, la unión de las herramientas y el mayor contexto. El techo de coste es
        el MENOR de los dos: un techo compartido no puede ser más alto que el más estricto
        de los que comparte.
        """
        exigencias = list(exigencias)
        if not exigencias:
            raise DegradacionInvalida("no hay exigencias que combinar")
        if len(exigencias) == 1:
            return dict(exigencias[0])
        ejes = {}
        for eje in self.ejes:
            ejes[eje] = max((e["ejes"][eje] for e in exigencias),
                            key=lambda nivel, _eje=eje: self.indice(_eje, nivel))
        contexto = max((e["contexto"] for e in exigencias), key=self.indice_de_contexto)
        coste = min((e["coste"] for e in exigencias), key=self.indice_de_coste)
        herramientas = sorted({h for e in exigencias for h in e["herramientas"]})
        perfiles = sorted({p for e in exigencias for p in e["perfiles"]})
        textos = sorted({e["degradacion_permitida"] for e in exigencias
                         if e["degradacion_permitida"]})
        return {
            "perfiles": perfiles,
            "ejes": ejes,
            "contexto": contexto,
            "herramientas": herramientas,
            "coste": coste,
            "degradacion_permitida": "\n\n".join(textos),
        }

    # -------------------------------------------------------- eje dominante
    # `C2` paso 4 (a) nombra un NIVEL, no «el tope del eje»: «el declarado en `exige` con
    # nivel `maximo`». La escala de `vision` —`no` · `util` · `requerida`— no tiene ese
    # nivel, de modo que `vision` NUNCA puede ser el eje dominante bajo la letra de `C2`.
    NIVEL_DOMINANTE = "maximo"

    def eje_dominante(self, exigencia):
        """`C2` paso 4 (a), al pie de la letra. Devuelve `(eje, nivel, por_qué)`.

        DECISIÓN · el criterio es el NIVEL `maximo`, no «el tope de su eje»
            La versión anterior generalizaba a «el primero declarado en el tope de SU eje»,
            y esa generalización NO es `C2`: adelantaba `vision: requerida` por delante de
            un eje que sí pide `maximo`. Diverge en `perfil:investigacion-visual` —donde
            `C2` dice `investigacion` y salía `vision`— y en `perfil:prototipado` —donde
            `C2` dice `programacion` y salía `vision`—. El valor se PUBLICA en el registro
            auditable, así que publicarlo mal es publicar una razón falsa aunque la elección
            de modelo no cambie. Se vuelve a la letra.

        DECISIÓN · el desempate cuando NINGÚN eje pide `maximo` se DECLARA, no se calla
            `C2` no dice qué hacer con un perfil sin ningún `maximo` —`perfil:interlocucion`
            es uno—, y sin regla no habría orden determinista, que es lo único que el paso 4
            existe para garantizar. Se toma el nivel más alto que el perfil pide y, entre
            los que lo empatan, el primero por orden del esquema: es la MISMA regla de
            desempate que `C2` escribe para el caso que sí contempla, aplicada al caso que
            no contempla. Se marca en el motivo para que se lea como derivación y no como
            cita.
        """
        for eje in self.ejes:
            if exigencia["ejes"][eje] == self.NIVEL_DOMINANTE:
                return eje, exigencia["ejes"][eje], (
                    "declarado en `exige` con nivel `" + self.NIVEL_DOMINANTE + "`, y es "
                    "el primero por orden del esquema entre los que lo declaran "
                    "(`C2` paso 4 a)")
        mayor = max(self.indice(eje, exigencia["ejes"][eje]) for eje in self.ejes)
        for eje in self.ejes:
            if self.indice(eje, exigencia["ejes"][eje]) == mayor:
                return eje, exigencia["ejes"][eje], (
                    "DERIVADO: ningún eje se declara con nivel `" + self.NIVEL_DOMINANTE
                    + "`, caso que `C2` no contempla; es el nivel más alto que el perfil "
                    "pide y el primero por orden del esquema entre los que lo empatan")
        raise CorpusIncompleto("un perfil sin ningún eje declarado")  # pragma: no cover


# ===========================================================================
#  el CATÁLOGO del proyecto
# ===========================================================================
class Catalogo:
    """Los modelos que el PROYECTO declara. Inmutable, ordenado y con huella propia."""

    def __init__(self, modelos, *, sede):
        self.modelos = tuple(sorted(modelos, key=lambda m: m["id"]))
        self.sede = sede
        self.huella = cid_de_objeto({"sede": sede, "modelos": list(self.modelos)})

    def __len__(self):
        return len(self.modelos)

    @property
    def ids(self):
        return tuple(m["id"] for m in self.modelos)

    def a_dict(self):
        return {"sede": self.sede, "huella": self.huella, "modelos": list(self.modelos)}


def _validar_modelo(datos, politica, *, sede, numero):
    faltan = [c for c in politica.obligatorios_de_modelo if c not in datos]
    if faltan:
        raise CatalogoDeModelosInvalido(
            "el modelo nº " + str(numero) + " del catálogo no declara " + ", ".join(faltan)
            + "; la forma del catálogo es el ESPEJO del esquema `perfil-agente`",
            ruta=sede, faltan=sorted(faltan),
        )
    identificador = datos["id"]
    if not isinstance(identificador, str) or not identificador.startswith("modelo:"):
        raise CatalogoDeModelosInvalido(
            "el identificador de un modelo casa `" + politica.patron_de_modelo + "`; se "
            "declaró " + repr(identificador), ruta=sede,
        )
    ofrece = datos.get("ofrece") or {}
    faltan_ejes = [eje for eje in politica.ejes if eje not in ofrece]
    if faltan_ejes:
        raise CatalogoDeModelosInvalido(
            "el modelo `" + identificador + "` no declara los ejes "
            + ", ".join(faltan_ejes) + "; son los mismos SIETE del esquema",
            ruta=sede, modelo=identificador,
        )
    sobran = [eje for eje in ofrece if eje not in politica.ejes]
    if sobran:
        raise CatalogoDeModelosInvalido(
            "el modelo `" + identificador + "` declara ejes que el esquema no tiene: "
            + ", ".join(sorted(sobran)), ruta=sede, modelo=identificador,
        )
    ejes = {}
    for eje in politica.ejes:
        nivel = _texto_de_nivel(ofrece[eje])
        politica.indice(eje, nivel)
        ejes[eje] = nivel
    contexto = _texto_de_nivel(datos.get("contexto"))
    politica.indice_de_contexto(contexto)
    coste = _texto_de_nivel(datos.get("coste"))
    politica.indice_de_coste(coste)
    herramientas = datos.get("herramientas")
    if not isinstance(herramientas, list) or not herramientas:
        raise CatalogoDeModelosInvalido(
            "el modelo `" + identificador + "` no declara ninguna herramienta",
            ruta=sede, modelo=identificador,
        )
    return {
        "id": identificador,
        "ofrece": ejes,
        "contexto": contexto,
        "herramientas": sorted({str(h) for h in herramientas}),
        "coste": coste,
    }


def catalogo_desde_texto(texto, *, politica, sede):
    """El catálogo de un documento con bloques ```yaml ads:modelo```. Falla cerrado si no hay."""
    encontrados = [datos for tipo, datos, _r, _l in bloques(texto, sede)
                   if tipo == BLOQUE_DE_MODELO]
    if not encontrados:
        raise CatalogoDeModelosAusente(
            "`" + sede + "` no declara ningún bloque `ads:" + BLOQUE_DE_MODELO + "`: el "
            "proyecto no tiene catálogo de modelos, y sin catálogo no hay agente que "
            "asignar. `C2` sitúa el adaptador en el PROFILE del proyecto, NUNCA en el "
            "kernel, y el kernel no inventa uno por defecto",
            ruta=sede,
        )
    modelos, vistos = [], set()
    for numero, datos in enumerate(encontrados, 1):
        modelo = _validar_modelo(datos, politica, sede=sede, numero=numero)
        if modelo["id"] in vistos:
            raise CatalogoDeModelosInvalido(
                "el catálogo declara dos veces `" + modelo["id"] + "`", ruta=sede,
                modelo=modelo["id"],
            )
        vistos.add(modelo["id"])
        modelos.append(modelo)
    return Catalogo(modelos, sede=sede)


def cargar_catalogo(ruta_control_repo, *, politica=None, corpus=None):
    """El catálogo del PROYECTO, leído de su `PROFILE.md`. Sin PROFILE no hay catálogo."""
    politica = politica or Politica(corpus)
    if not ruta_control_repo:
        raise CatalogoDeModelosAusente(
            "no se ha declarado control repo del que leer el `" + PERFIL_DEL_PROYECTO
            + "`: el catálogo de modelos es material del PROYECTO",
        )
    sede = os.path.join(ruta_control_repo, PERFIL_DEL_PROYECTO)
    if not os.path.isfile(sede):
        raise CatalogoDeModelosAusente(
            "el control repo no trae `" + PERFIL_DEL_PROYECTO + "`, que es donde `C2` "
            "sitúa el adaptador entre perfiles y modelos reales",
            ruta=sede,
        )
    with open(sede, "r", encoding="utf-8") as manejador:
        texto = manejador.read()
    return catalogo_desde_texto(texto, politica=politica, sede=PERFIL_DEL_PROYECTO)


# ===========================================================================
#  los seis pasos de `C2`
# ===========================================================================
def _motivo_por_ejes(exigencia, modelo, politica):
    fallos = []
    for eje in politica.ejes:
        exigido, ofrecido = exigencia["ejes"][eje], modelo["ofrece"][eje]
        if politica.indice(eje, ofrecido) < politica.indice(eje, exigido):
            fallos.append("el eje `" + eje + "` exige `" + exigido + "` y el modelo ofrece `"
                          + ofrecido + "`")
    return fallos


def _motivo_por_herramientas(exigencia, modelo):
    ofrecidas = set(modelo["herramientas"])
    faltan = [h for h in exigencia["herramientas"] if h not in ofrecidas]
    return ["no ofrece la herramienta declarada `" + h + "`" for h in faltan]


def _motivo_por_contexto(exigencia, modelo, politica):
    if politica.indice_de_contexto(modelo["contexto"]) < politica.indice_de_contexto(
            exigencia["contexto"]):
        return ["el contexto exige `" + exigencia["contexto"] + "` y el modelo ofrece `"
                + modelo["contexto"] + "`"]
    return []


def _exigencia_degradada(exigencia, degradacion, politica):
    """Aplica una degradación DECLARADA, eje a eje. Nunca inferida de la prosa del perfil."""
    if not degradacion:
        return exigencia, None
    ejes = degradacion.get("ejes") or {}
    motivo = str(degradacion.get("motivo") or "").strip()
    autoriza = str(degradacion.get("autoriza") or "").strip()
    if not ejes or not motivo or not autoriza:
        raise DegradacionInvalida(
            "una degradación se DECLARA con `ejes`, `motivo` y `autoriza`; sin las tres no "
            "se distingue de rebajar el perfil en silencio, que es lo que `C4` prohíbe",
        )
    sobran = sorted(e for e in ejes if e not in politica.ejes)
    if sobran:
        raise DegradacionInvalida(
            "la degradación nombra ejes que el esquema no tiene: " + ", ".join(sobran),
        )
    rebajado = {clave: valor for clave, valor in exigencia.items()}
    rebajado["ejes"] = dict(exigencia["ejes"])
    aplicados = []
    for eje in politica.ejes:
        if eje not in ejes:
            continue
        nivel = _texto_de_nivel(ejes[eje])
        if politica.indice(eje, nivel) >= politica.indice(eje, exigencia["ejes"][eje]):
            raise DegradacionInvalida(
                "la degradación del eje `" + eje + "` no rebaja nada: el perfil exige `"
                + exigencia["ejes"][eje] + "` y se declara `" + nivel + "`", eje=eje,
            )
        rebajado["ejes"][eje] = nivel
        aplicados.append({"eje": eje, "de": exigencia["ejes"][eje], "a": nivel})
    if not aplicados:
        raise DegradacionInvalida("la degradación declarada no rebaja ningún eje")
    return rebajado, {"ejes": aplicados, "motivo": motivo, "autoriza": autoriza}


def seleccionar(exigencia, catalogo, *, politica, degradacion=None):
    """Los pasos 2 a 6 de `C2`. Devuelve el REGISTRO completo, elegido o bloqueado."""
    efectiva, aplicada = _exigencia_degradada(exigencia, degradacion, politica)
    eje, nivel, por_que = politica.eje_dominante(efectiva)
    descartados, admitidos = [], []
    for modelo in (catalogo.modelos if catalogo is not None else ()):
        motivos = _motivo_por_ejes(efectiva, modelo, politica)
        regla = REGLA_EJES
        if not motivos:
            motivos = _motivo_por_herramientas(efectiva, modelo)
            regla = REGLA_HERRAMIENTAS
        if not motivos:
            motivos = _motivo_por_contexto(efectiva, modelo, politica)
            regla = REGLA_CONTEXTO
        if motivos:
            descartados.append({
                "modelo": modelo["id"], "regla": regla, "motivo": "; ".join(motivos),
            })
            continue
        admitidos.append(modelo)

    dentro = {m["id"]: politica.indice_de_coste(m["coste"])
              <= politica.indice_de_coste(efectiva["coste"]) for m in admitidos}
    ordenados = sorted(admitidos, key=lambda m: (
        -politica.indice(eje, m["ofrece"][eje]),
        0 if dentro[m["id"]] else 1,
        politica.indice_de_coste(m["coste"]),
        m["id"],
    ))
    orden = [{
        "modelo": m["id"],
        "clave": [politica.indice(eje, m["ofrece"][eje]),
                  0 if dentro[m["id"]] else 1,
                  politica.indice_de_coste(m["coste"]), m["id"]],
    } for m in ordenados]

    registro = {
        "perfiles": list(efectiva["perfiles"]),
        "exigencia": {"ejes": dict(efectiva["ejes"]), "contexto": efectiva["contexto"],
                      "herramientas": list(efectiva["herramientas"]),
                      "coste": efectiva["coste"]},
        "eje_dominante": {"eje": eje, "nivel": nivel, "por_que": por_que},
        "catalogo": (catalogo.huella if catalogo is not None else None),
        "candidatos": list(catalogo.ids) if catalogo is not None else [],
        "descartados": sorted(descartados, key=lambda d: d["modelo"]),
        "orden": orden,
        "degradado": bool(aplicada),
        "degradacion": aplicada,
        "degradacion_permitida": efectiva["degradacion_permitida"],
    }
    if not ordenados:
        registro["estado"] = ESTADO_BLOQUEADO
        registro["modelo"] = None
        registro["coste"] = None
        registro["dentro_del_techo"] = None
        registro["falta"] = _lo_que_falta(efectiva, catalogo, politica)
        return registro
    elegido = ordenados[0]
    registro["estado"] = ESTADO_ASIGNADO
    registro["modelo"] = elegido["id"]
    registro["coste"] = elegido["coste"]
    registro["dentro_del_techo"] = bool(dentro[elegido["id"]])
    registro["falta"] = []
    return registro


def _lo_que_falta(exigencia, catalogo, politica):
    """`C2` paso 6: qué CAPACIDAD DE MODELO falta. No «no hay modelo», sino cuál falta."""
    if catalogo is None:
        return ["no hay catálogo de modelos declarado en el `" + PERFIL_DEL_PROYECTO
                + "` del proyecto"]
    if not catalogo.modelos:
        return ["el catálogo del proyecto está vacío"]
    falta = []
    for eje in politica.ejes:
        exigido = exigencia["ejes"][eje]
        if all(politica.indice(eje, m["ofrece"][eje]) < politica.indice(eje, exigido)
               for m in catalogo.modelos):
            falta.append("eje `" + eje + "` al nivel `" + exigido + "`")
    for herramienta in exigencia["herramientas"]:
        if all(herramienta not in m["herramientas"] for m in catalogo.modelos):
            falta.append("herramienta `" + herramienta + "`")
    if all(politica.indice_de_contexto(m["contexto"])
           < politica.indice_de_contexto(exigencia["contexto"]) for m in catalogo.modelos):
        falta.append("contexto `" + exigencia["contexto"] + "`")
    if not falta:
        falta.append(
            "ningún modelo cumple la exigencia COMPLETA, aunque cada parte por separado "
            "esté cubierta por algún modelo del catálogo")
    return falta


# ===========================================================================
#  `C4` paso 4: por cada rol, la política de `C2`
# ===========================================================================
def asignar_rol(rol, *, politica, catalogo, degradaciones=None):
    """El registro de asignación de UN rol: rol · perfil · modelo · descartados · motivo."""
    perfil = politica.perfil_de_rol(rol)
    exigencia = politica.exigencia_de_perfil(perfil)
    degradacion = (degradaciones or {}).get(rol) or (degradaciones or {}).get(perfil)
    registro = seleccionar(exigencia, catalogo, politica=politica, degradacion=degradacion)
    registro["rol"] = rol
    registro["perfil"] = perfil
    return registro


def asignar(roles, *, politica, catalogo, degradaciones=None):
    """`C4` paso 4 sobre una lista de roles. Ordenado por rol: mismo equipo, mismo registro."""
    return [asignar_rol(rol, politica=politica, catalogo=catalogo,
                        degradaciones=degradaciones)
            for rol in sorted({str(r) for r in roles})]


def identificador_de_agente(modelo, roles, reparto=None):
    """`ag-<12 hex>` DERIVADO del contenido: mismo modelo y mismos roles, mismo agente.

    `reparto` distingue a los agentes de un rol REPARTIDO por `C4`: tres agentes sobre
    `DIS/diseno-visual`, uno por dirección explorada, son tres agentes distintos y no pueden
    compartir identificador —si lo compartieran, `exigir_slots_coherentes` los vería como uno
    y el corte por `execution_slots` volvería a contar uno donde hay tres—. Cuando no hay
    reparto no entra en la semilla, de modo que el identificador de un rol de un solo agente
    es EXACTAMENTE el de siempre y ningún equipo ya escrito cambia de identidad.
    """
    semilla = {"modelo": modelo, "roles": sorted(str(r) for r in roles)}
    if reparto:
        semilla["reparto"] = str(reparto)
    digest = cid_de_objeto(semilla)
    return "ag-" + digest.split(":", 1)[-1][:12]
