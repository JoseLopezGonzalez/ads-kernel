#!/usr/bin/env python3
"""motor — el ejecutor ÚNICO de mutaciones canónicas (`I-g4`) y su protocolo.

Aquí se instancia el §3 del contrato paso a paso, y las dos ramas de `g.8`. Las decisiones
que el contrato dejaba abiertas, con sus alternativas y con la invariante que preservan:

DECISIÓN · `REVISION.json` es el ÚNICO punto de publicación
    Alternativas: (a) considerar publicado cada objeto en cuanto su `os.replace` termina;
    (b) considerar publicado el conjunto sólo cuando `REVISION.json` cambia.
    Se elige (b). Con (a), una transición multiarchivo cortada por la mitad dejaría una
    MEZCLA PARCIAL visible como estado vigente, y `g.3` prohíbe exactamente eso. Con (b) los
    objetos publicados antes del corte son inertes: `leer` los verifica contra `raiz`, y
    `raiz` sigue siendo la de la revisión anterior, así que nadie los ve como verdad. La
    ventana entre el primer `os.replace` y el cambio de `REVISION.json` existe —`g.3` dice
    expresamente que NO se afirma aislamiento de lecturas—, pero no es publicable.

DECISIÓN · el PUNTO DE NO RETORNO es `transicion.preparada`, no el primer `os.replace`
    Alternativas: (a) que la recuperación decida por lo que encuentre en disco; (b) que lo
    decida un evento del diario escrito y sincronizado ANTES de tocar `canonico/`.
    Se elige (b). Con (a), distinguir «iba a escribir» de «escribió y le cortaron» exigiría
    adivinar, y `I-g2` prohíbe inventar estado. Con (b) la regla es mecánica y no depende de
    haber presenciado el fallo, que es lo que `g.3` pide: si hay `preparada` se COMPLETA, si
    sólo hay `abierta` se REVIERTE. El diario sostiene la recuperación, tal como dice `g.7`.

DECISIÓN · la RECUPERACIÓN no inyecta puntos de fallo
    Los nueve puntos del §10 se llaman en `aplicar`, en las fronteras que el §3 marca, y no
    en `recuperar`. Si la recuperación también los disparase, un almacén abierto con
    `ADS_ESTADO_FALLO` exportada moriría al recuperarse, luego al recuperarse otra vez, y
    nunca cerraría la ventana: la variable pensada para demostrar la recuperación la haría
    imposible. El corte se inyecta en la escritura; la recuperación se ejecuta después.

DECISIÓN · `aplicar` se NIEGA a escribir sobre una ventana sin cerrar
    Alternativas: (a) recuperar automáticamente dentro de `aplicar`; (b) rechazar y exigir
    `recuperar()` explícito.
    Se elige (b). `g.8` dice que la salida de un conflicto la decide LA AUTORIDAD y no el
    runtime; encadenar una recuperación dentro de una escritura escondería una decisión de
    autoridad dentro de una operación rutinaria. `abrir(recuperar=True)` sí recupera, porque
    ahí el llamador lo ha pedido explícitamente al abrir.

DECISIÓN · las verificaciones «byte a byte» se hacen por `cid`
    `g.8` exige verificar byte a byte antes de revertir. Comparar el `cid` de los bytes del
    fichero contra el `cid` que la base declara ES esa comparación: SHA-256 cubre todos los
    bytes, y hacerlo así permite comparar contra la base sin conservar una segunda copia del
    contenido anterior, que sería un almacén paralelo y otro sitio donde desincronizarse.

DECISIÓN · `verificar_integridad` y `auditar` FALLAN CERRADO en vez de devolver `ok=False`
    Alternativas: (a) devolver un informe con `ok=False`; (b) levantar el error tipado que
    corresponda, con el informe adjunto en `error.informe`.
    Se elige (b). `g.5` dice «produce fallo CERRADO» y el §9 dice que borrar el registro a
    mano produce `RegistroDeReconciliacionCorrupto` AL VERIFICAR. Un informe con `ok=False`
    que el llamador puede ignorar no es un fallo cerrado: es un aviso. El informe sigue
    disponible, adjunto al error, para que la evidencia describa el daño y no sólo lo nombre.
"""
from __future__ import annotations

import os

from . import fallos, migracion as _migracion
from .bloqueo import BloqueoExclusivo
from .diario import Diario
from .errores import (
    AlmacenNoInicializado,
    AlmacenYaInicializado,
    ErrorDeEstado,
    EscritorConcurrente,
    EstadoCorrupto,
    FormatoDesconocido,
    IdentificadorDuplicado,
    PermisoInsuficiente,
    RecuperacionMarcada,
    RegistroDeReconciliacionCorrupto,
    ReintentosAgotados,
    RevisionObsoleta,
    RutaInvalida,
    TransicionInvalida,
    VersionDesconocida,
)
from .reconciliacion import RegistroAuxiliar, momento_logico
from .rutas import (
    CONTENIDO_GITIGNORE,
    Disposicion,
    asegurar_directorio,
    borrar_arbol,
    borrar_si_existe,
    comprobar_ruta_logica,
    dominio_de,
    escribir_fichero,
    escribir_y_sincronizar,
    leer_bytes,
    publicar,
    recorrer_canonico,
    sincronizar_directorio,
    sincronizar_fichero,
)
from .serializacion import (
    ESQUEMA,
    VERSION_DE_ESQUEMA,
    calcular_cid_raiz,
    calcular_revision_id,
    cid,
    comprobar_esquema,
    deserializar,
    serializar_canonico,
)
from .transaccion import (
    InformeAuditoria,
    InformeIntegridad,
    InformeRecuperacion,
    ResultadoTransicion,
    Transicion,
    componer_revision,
    identificador_derivado,
    proyectar_raiz,
)

VERSION_DE_FORMATO = 1
NOMBRE_FORMATO = "ads.estado"
AUTOR_RUNTIME = "runtime"

CLAVES_REVISION = (
    "esquema", "revision", "revision_id", "padre", "cid_raiz", "raiz",
    "diario_secuencia", "transaccion",
)


# ===========================================================================
#  apertura e inicialización
# ===========================================================================
def _contenido_formato():
    # El §2 fija este objeto EXACTO. No lleva `esquema`: la versión que declara es la del
    # FORMATO del almacén, que es una materia distinta de la versión de esquema de los
    # objetos durables, y confundirlas haría imposible migrar una sin tocar la otra.
    return {"formato": NOMBRE_FORMATO, "version_formato": VERSION_DE_FORMATO}


def _leer_formato(disposicion):
    datos = leer_bytes(disposicion.formato, error=FormatoDesconocido)
    objeto = deserializar(datos, ruta=disposicion.formato, error=FormatoDesconocido)
    if not isinstance(objeto, dict) or objeto.get("formato") != NOMBRE_FORMATO:
        raise FormatoDesconocido(
            "`FORMATO.json` no declara `formato: " + NOMBRE_FORMATO + "`",
            ruta=disposicion.relativa(disposicion.formato),
        )
    version = objeto.get("version_formato")
    if not isinstance(version, int) or version != VERSION_DE_FORMATO:
        raise FormatoDesconocido(
            "versión de formato " + repr(version) + " desconocida; este motor entiende la "
            + str(VERSION_DE_FORMATO) + " y `g.10` le prohíbe adivinar el resto",
            ruta=disposicion.relativa(disposicion.formato),
            encontrada=version,
            soportada=VERSION_DE_FORMATO,
        )
    return version


def _fundar_estructura_sin_formato(disposicion):
    """El esqueleto de directorios y el `.gitignore`, SIN declarar el formato todavía.

    Se separa del paso que escribe `FORMATO.json` porque la migración 0->1 necesita fundar
    el esqueleto y declarar el formato en momentos distintos: el fichero de formato es la
    señal de «este almacén ya es del formato nuevo», y hasta que la migración termina esa
    señal sería mentira.
    """
    asegurar_directorio(disposicion.almacen)
    asegurar_directorio(disposicion.canonico)
    asegurar_directorio(os.path.dirname(disposicion.diario))
    asegurar_directorio(disposicion.reconciliacion)
    asegurar_directorio(disposicion.conflictos)
    asegurar_directorio(os.path.join(disposicion.operacional, "tx"))
    # `g.14`: la rama canónica NUNCA contiene estado parcial. La zona de preparación ES
    # estado parcial, así que el motor la excluye él mismo en vez de confiar en que alguien
    # se acuerde de hacerlo.
    escribir_y_sincronizar(disposicion.gitignore, CONTENIDO_GITIGNORE.encode("utf-8"))
    sincronizar_directorio(disposicion.almacen)


def _fundar_estructura(disposicion):
    """El esqueleto completo, con el formato ya declarado. Es lo que usa `inicializar`."""
    _fundar_estructura_sin_formato(disposicion)
    escribir_y_sincronizar(disposicion.formato, serializar_canonico(_contenido_formato()))
    sincronizar_directorio(disposicion.almacen)


def inicializar(ruta_control_repo):
    """Funda un almacén vacío en `<control_repo>/estado/` y devuelve el `Almacen` abierto."""
    disposicion = Disposicion(ruta_control_repo)
    if os.path.exists(disposicion.formato) or os.path.exists(disposicion.revision):
        raise AlmacenYaInicializado(
            "ya hay un almacén de estado en este control repo; inicializar de nuevo "
            "destruiría el diario, y `g.13` no lo permite",
            ruta=disposicion.relativa(disposicion.almacen),
        )
    if not os.path.isdir(disposicion.repo):
        raise RutaInvalida("el control repo no existe como directorio", ruta=ruta_control_repo)

    _fundar_estructura(disposicion)
    almacen = Almacen(disposicion)
    almacen._diario.crear()
    almacen._registro.crear()

    transaccion = identificador_derivado(0, {"tipo": "almacen.inicializado", "revision": 0})
    # La revisión 0 se compone ANTES de anexar el evento, porque el evento declara su
    # `resultado`: sin él, `detectar_bifurcacion` no podría reconstruir el linaje desde el
    # origen y `auditar` no tendría con qué comparar la primera revisión.
    revision = componer_revision(0, None, {}, transaccion, diario_secuencia=1)
    almacen._diario.anexar(
        "almacen.inicializado",
        transaccion=transaccion,
        base=None,
        resultado=revision["revision_id"],
        operaciones=[],
        autor=AUTOR_RUNTIME,
        motivo="inicialización del almacén de estado durable",
    )
    almacen._publicar_revision(revision)
    return almacen


def abrir(ruta_control_repo, *, recuperar=True):
    """Abre un almacén existente. Con `recuperar=True` cierra la ventana si la hay (§3)."""
    disposicion = Disposicion(ruta_control_repo)
    if not os.path.isdir(disposicion.almacen):
        raise AlmacenNoInicializado(
            "no hay `estado/` en este control repo", ruta=disposicion.relativa(disposicion.almacen)
        )
    if not os.path.exists(disposicion.formato):
        # Almacén HEREDADO (formato 0): existe estado pero no declara formato. No se
        # adivina y no se migra al leer (`g.11`); se devuelve un almacén que sólo admite
        # `migrar()`, para que la compatibilidad sea DEMOSTRABLE y no una promesa.
        if os.path.isdir(disposicion.canonico) or os.path.exists(disposicion.revision):
            return Almacen(disposicion, heredado=True)
        raise AlmacenNoInicializado(
            "`estado/` existe pero no contiene ni `FORMATO.json` ni `canonico/`",
            ruta=disposicion.relativa(disposicion.almacen),
        )
    _leer_formato(disposicion)
    if not os.path.exists(disposicion.revision):
        raise AlmacenNoInicializado(
            "falta `REVISION.json`: el almacén declara formato pero no tiene revisión",
            ruta=disposicion.relativa(disposicion.revision),
        )
    almacen = Almacen(disposicion)
    # `g.5`: toda corrupción o truncamiento se DETECTA AL LEER, y abrir es leer. Las dos
    # comprobaciones se hacen aquí y no al primer uso porque un almacén que se abre sin
    # protestar y falla tres llamadas más tarde ya ha dejado creer que estaba sano.
    #  · `_leer_revision` valida el esquema declarado: una versión que este lector no
    #    entiende produce `VersionDesconocida` y no una lectura «a lo que se pueda» (`g.10`).
    #  · `exigir_coherente` comprueba que el diario llega hasta el evento que la revisión
    #    publicada dice que la explica, y con la cadena de huellas intacta.
    revision = almacen._leer_revision()
    almacen._diario.exigir_coherente(revision["diario_secuencia"], tolerar_cola=recuperar)
    if recuperar and almacen._hay_ventana_que_cerrar():
        almacen.recuperar()
    return almacen


# ===========================================================================
#  el almacén
# ===========================================================================
class Almacen:
    """El almacén de estado durable de un control repo. Único ejecutor de mutaciones."""

    def __init__(self, disposicion, heredado=False):
        self._d = disposicion
        self.ruta = disposicion.repo
        self.ruta_almacen = disposicion.almacen
        self.heredado = heredado
        self._cerrado = False
        self._diario = Diario(disposicion.diario)
        self._bloqueo_registro = BloqueoExclusivo(disposicion.bloqueo_registro, "registro")
        self._registro = RegistroAuxiliar(disposicion.registro, self._bloqueo_registro)

    # ------------------------------------------------------------- salvaguardas
    def _exigir_operable(self):
        if self._cerrado:
            raise ErrorDeEstado(
                "el almacén está cerrado", codigo="ALMACEN_CERRADO",
                ruta=self._d.relativa(self._d.almacen),
            )
        if self.heredado:
            raise FormatoDesconocido(
                "el almacén está en formato heredado (0) y no declara `FORMATO.json`; "
                "`g.11` prohíbe migrar al leer: llame a `migrar()` explícitamente",
                ruta=self._d.relativa(self._d.almacen),
            )

    def _exigir_abierto(self):
        if self._cerrado:
            raise ErrorDeEstado(
                "el almacén está cerrado", codigo="ALMACEN_CERRADO",
                ruta=self._d.relativa(self._d.almacen),
            )

    # ------------------------------------------------------------------ lectura
    def _leer_revision(self):
        datos = leer_bytes(self._d.revision, error=EstadoCorrupto)
        revision = deserializar(datos, ruta=self._d.relativa(self._d.revision))
        if not isinstance(revision, dict):
            raise EstadoCorrupto("`REVISION.json` no es un objeto JSON",
                                 ruta=self._d.relativa(self._d.revision))
        comprobar_esquema(revision, ruta=self._d.relativa(self._d.revision))
        faltan = [clave for clave in CLAVES_REVISION if clave not in revision]
        if faltan:
            raise EstadoCorrupto(
                "`REVISION.json` no lleva " + ", ".join(faltan),
                ruta=self._d.relativa(self._d.revision),
            )
        if not isinstance(revision["raiz"], dict):
            raise EstadoCorrupto("`raiz` debe ser un mapa `ruta -> cid`",
                                 ruta=self._d.relativa(self._d.revision))
        return revision

    def revision(self):
        """Copia de `REVISION.json`. Copia, para que nadie mute el estado por referencia."""
        self._exigir_operable()
        revision = self._leer_revision()
        revision["raiz"] = dict(revision["raiz"])
        return revision

    def _cid_en_disco(self, ruta_logica):
        """`cid` del fichero canónico, o `None` si no está. Lee TODOS sus bytes."""
        destino = self._d.ruta_canonica(ruta_logica)
        if not os.path.exists(destino):
            return None
        return cid(leer_bytes(destino, error=EstadoCorrupto))

    def leer(self, ruta):
        """El estado canónico de una ruta lógica, verificado contra `REVISION.json.raiz`."""
        self._exigir_operable()
        comprobar_ruta_logica(ruta)
        revision = self._leer_revision()
        esperado = revision["raiz"].get(ruta)
        if esperado is None:
            raise RutaInvalida(
                "la ruta no existe en la revisión vigente " + str(revision["revision"]),
                ruta=ruta,
            )
        destino = self._d.ruta_canonica(ruta)
        datos = leer_bytes(destino, error=EstadoCorrupto)
        encontrado = cid(datos)
        if encontrado != esperado:
            # Fallo CERRADO (`g.5`): no se devuelve el contenido «por si acaso sirve». Un
            # lector que recibe datos que no casan con la revisión propaga la corrupción.
            raise EstadoCorrupto(
                "el `cid` del objeto no casa con el declarado en `REVISION.json`: el "
                "fichero fue modificado fuera del diario, o está truncado",
                ruta=ruta, esperado=esperado, encontrado=encontrado,
            )
        objeto = deserializar(datos, ruta=ruta)
        comprobar_esquema(objeto, ruta=ruta)
        return objeto

    def listar(self, dominio=""):
        """Rutas lógicas de la revisión vigente, ordenadas. Filtra por dominio si se da."""
        self._exigir_operable()
        revision = self._leer_revision()
        rutas = sorted(revision["raiz"])
        if dominio:
            rutas = [ruta for ruta in rutas if dominio_de(ruta) == dominio]
        return rutas

    def diario(self, desde=0):
        self._exigir_operable()
        return self._diario.eventos(desde=desde)

    # ------------------------------------------------------------- publicación
    def _publicar_revision(self, revision):
        """Paso 9 del §3: el ÚNICO punto de publicación atómica. Deja todo durable."""
        datos = serializar_canonico(revision)
        escribir_y_sincronizar(self._d.revision_temporal, datos)
        publicar(self._d.revision_temporal, self._d.revision)
        sincronizar_directorio(self._d.almacen)

    # ------------------------------------------------------------------ ventana
    def _hay_ventana_que_cerrar(self):
        """¿Queda algo que recuperar? UNA lectura del diario responde a las dos preguntas.

        Antes eran dos lecturas —`cola_desgarrada()` y luego `transaccion_sin_cerrar()`— y
        con varios escritores anexando en paralelo las dos veían diarios distintos. Ahora
        la cola desgarrada y la transacción sin cerrar se deducen del mismo corte.
        """
        eventos, cola = self._diario.instantanea(tolerar_cola=True)
        if cola:
            return True
        return self._diario.transaccion_sin_cerrar(eventos) is not None

    def estado_de_la_ventana(self):
        """`abierta` | `preparada` | `cerrada` (§3). No necesita haber presenciado el fallo."""
        self._exigir_operable()
        eventos, _ = self._diario.instantanea(tolerar_cola=True)
        return self._ventana_de(eventos)

    def _ventana_de(self, eventos):
        """La ventana deducida de una instantánea YA leída, para no releer el diario."""
        sin_cerrar = self._diario.transaccion_sin_cerrar(eventos)
        if sin_cerrar is None:
            return "cerrada"
        tipos = {evento["tipo"] for evento in sin_cerrar[1]}
        return "preparada" if "transicion.preparada" in tipos else "abierta"

    # =====================================================================
    #  protocolo transaccional (§3)
    # =====================================================================
    def aplicar(self, transicion, *, intentos=3):
        self._exigir_operable()
        if not isinstance(transicion, Transicion):
            raise TransicionInvalida(
                "se esperaba una `Transicion`; se recibió " + type(transicion).__name__
            )
        return self._aplicar_con_anexos(transicion, intentos=intentos, anexos=None)

    def _aplicar_con_anexos(self, transicion, *, intentos, anexos):
        transicion.validar(exige_cambio=not anexos)
        bloqueo = BloqueoExclusivo(self._d.bloqueo_escritor, "escritor")
        try:
            bloqueo.adquirir(intentos=max(1, int(intentos)))
        except EscritorConcurrente as exc:
            # `g.6`: agotar los reintentos NO modifica el estado canónico. Lo único que se
            # escribe es el registro auxiliar, que por eso tiene bloqueo propio.
            registro = self._abrir_reconciliacion_por_reintentos(transicion.id, intentos, exc)
            raise ReintentosAgotados(
                "no se pudo serializar con el escritor concurrente tras " + str(intentos)
                + " intento(s); el estado canónico queda intacto y se abrió el registro "
                "auxiliar " + registro,
                ruta=self._d.relativa(self._d.bloqueo_escritor),
                registro=registro, intentos=intentos,
            ) from exc
        try:
            return self._aplicar_bajo_bloqueo(transicion, anexos or {})
        finally:
            bloqueo.liberar()

    def _aplicar_bajo_bloqueo(self, transicion, anexos):
        diario = self._diario

        # Paso 2 · leer la revisión y comprobar la base. Antes, la ventana: escribir sobre
        # una transacción sin cerrar publicaría una revisión cuyo padre nadie ha establecido.
        if self._hay_ventana_que_cerrar():
            raise ErrorDeEstado(
                "hay una transacción sin cerrar; `g.8` reserva su salida a la autoridad, "
                "así que `aplicar` no la resuelve por su cuenta: llame a `recuperar()`",
                codigo="VENTANA_SIN_CERRAR",
                ruta=self._d.relativa(self._d.diario),
            )
        base = self._leer_revision()
        eventos = diario.eventos()

        repetida = self._resultado_si_repetida(transicion, eventos)
        if repetida is not None:
            return repetida

        if transicion.base is not None and transicion.base != base["revision_id"]:
            raise RevisionObsoleta(
                "la transición parte de una revisión que ya no es la vigente: otro "
                "escritor publicó antes. El ciclo se detiene y las órdenes quedan intactas",
                ruta=self._d.relativa(self._d.revision),
                esperada=transicion.base, vigente=base["revision_id"],
                revision=base["revision"],
            )

        # Paso 3 · validar. La forma ya se comprobó al construir la `Transicion`; aquí se
        # repite ENTERA —el §3 sitúa la validación en este paso— y se añade lo que sólo se
        # puede comprobar contra el estado real: que las rutas se resuelvan dentro del
        # árbol y que el medio admita de verdad la escritura.
        transicion.validar(exige_cambio=not anexos)
        plan = transicion.operaciones_a_dict()
        for operacion in plan:
            self._d.ruta_canonica(operacion["ruta"])
        self._exigir_medio_escribible(plan)
        for operacion in plan:
            if operacion["accion"] == "borrar" and operacion["ruta"] not in base["raiz"]:
                raise TransicionInvalida(
                    "no se puede borrar una ruta que la revisión vigente no contiene; "
                    "hacerlo silenciosamente convertiría un error en un no-cambio",
                    ruta=operacion["ruta"],
                )

        raiz_nueva = proyectar_raiz(base["raiz"], plan)
        numero = base["revision"] + 1
        padre = base["revision_id"]
        resultado = calcular_revision_id(
            numero, padre, calcular_cid_raiz(raiz_nueva), transicion.id
        )
        comunes = {
            "transaccion": transicion.id,
            "clase": transicion.tipo,
            "base": padre,
            "resultado": resultado,
            "operaciones": plan,
            "autor": transicion.autor,
            "motivo": transicion.motivo,
        }
        if anexos:
            comunes["anexos"] = anexos

        # Paso 4 · DIARIO ← transicion.abierta (+fsync). A partir de aquí hay ventana.
        diario.anexar("transicion.abierta", **comunes)

        try:
            zona = self._d.zona_tx(transicion.id)
            # Zona de preparación limpia: un resto de una transacción homónima anterior
            # haría que el paso 8 publicase bytes que esta transición nunca preparó.
            borrar_arbol(zona)
            asegurar_directorio(os.path.join(zona, "objetos"))

            # Paso 5 · escribir los objetos en la zona de preparación.
            fallos.punto("antes-de-escribir-temporal")
            preparados = []
            for operacion in transicion.escrituras():
                temporal = self._d.objeto_preparado(transicion.id, operacion.ruta)
                escribir_fichero(temporal, serializar_canonico(operacion.normalizada()))
                preparados.append((operacion, temporal))
            fallos.punto("despues-de-escribir-temporal")

            # Paso 6 · sincronizar cada temporal y el directorio de la zona.
            for _, temporal in preparados:
                sincronizar_fichero(temporal)
            for directorio in sorted({os.path.dirname(t) for _, t in preparados}):
                sincronizar_directorio(directorio)
            sincronizar_directorio(zona)
            fallos.punto("despues-de-sincronizar-temporal")
        except BaseException:
            # Antes del punto de no retorno todo es ESPECULATIVO LOCAL (`g.8`): se revierte
            # aquí mismo, se verifica contra la base y la ventana se cierra. No se deja para
            # `recuperar()` lo que este proceso todavía puede cerrar con certeza.
            self._revertir_especulativo(transicion.id, padre, plan, base)
            raise

        # Paso 7 · DIARIO ← transicion.preparada. PUNTO DE NO RETORNO.
        preparada = diario.anexar("transicion.preparada", **comunes)

        # Paso 8 · publicar cada objeto y sincronizar los directorios afectados.
        fallos.punto("antes-del-commit-atomico")
        self._publicar_objetos(transicion.id, plan, base["raiz"])
        fallos.punto("antes-de-sincronizar-directorio")
        self._sincronizar_dominios(plan)

        # Paso 9 · publicar la revisión. Aquí, y sólo aquí, el cambio pasa a ser vigente.
        revision = componer_revision(
            numero, padre, raiz_nueva, transicion.id, preparada["secuencia"]
        )
        if revision["revision_id"] != resultado:
            raise EstadoCorrupto(
                "la revisión recompuesta no reproduce el `resultado` anotado en el diario",
                ruta=self._d.relativa(self._d.revision),
                esperado=resultado, encontrado=revision["revision_id"],
            )
        self._publicar_revision(revision)
        fallos.punto("despues-del-commit-atomico")

        # Paso 9.5 · anexos que la transacción explica (registro auxiliar y migración).
        # Van ANTES de `transicion.confirmada` a propósito: `confirmada` es lo último que se
        # escribe, y por tanto la única marca de «esto está entero». Si fueran después, un
        # corte entre medias dejaría una transacción cerrada con su anexo sin escribir, y
        # la recuperación no tendría por dónde verlo.
        eventos_anexos = self._escribir_anexos(anexos, revision, transicion.id)

        # Paso 10 · DIARIO ← transicion.confirmada.
        diario.anexar("transicion.confirmada", **comunes)

        # Paso 11 · limpiar la zona de preparación (operacional, no durable).
        borrar_arbol(self._d.zona_tx(transicion.id))
        fallos.punto("antes-de-devolver-exito")

        del eventos_anexos          # sólo interesaba su efecto durable, no su valor
        return ResultadoTransicion(
            transaccion=transicion.id,
            revision=revision["revision"],
            revision_id=revision["revision_id"],
            padre=revision["padre"],
            cid_raiz=revision["cid_raiz"],
            diario_secuencia=revision["diario_secuencia"],
            operaciones=plan,
        )

    # ------------------------------------------------------- piezas del protocolo
    def _exigir_medio_escribible(self, plan):
        """`g.4`: lo que no puede alcanzar durabilidad FALLA de forma VISIBLE, y pronto.

        Se comprueba ANTES del paso 4, es decir antes de anexar `transicion.abierta`. La
        alternativa era dejar que el `OSError` apareciera donde apareciese: cada primitiva
        lo traduce ya a `PermisoInsuficiente`, así que el error saldría igual de tipado.
        Pero saldría TARDE. Con `canonico/` en sólo lectura, el primer sitio donde se nota
        es el `os.replace` del paso 8, que está DESPUÉS del punto de no retorno: la
        transacción quedaría abierta, con su ventana, esperando una recuperación que
        tampoco podría escribir. Comprobarlo aquí convierte un almacén atascado en un
        error limpio con el estado canónico intacto, que es lo que `g.6` promete cuando un
        ciclo se detiene: «dejando las órdenes intactas».

        `os.access` puede quedarse obsoleto entre la comprobación y el uso, y por eso NO
        sustituye a la traducción del `OSError`: es una red por delante, no en lugar de.
        """
        directorios = {self._d.almacen, self._d.canonico, os.path.dirname(self._d.diario)}
        for operacion in plan:
            padre = os.path.dirname(self._d.ruta_canonica(operacion["ruta"]))
            if os.path.isdir(padre):
                directorios.add(padre)
        for directorio in sorted(directorios):
            if not os.path.isdir(directorio):
                continue
            if not os.access(directorio, os.W_OK | os.X_OK):
                raise PermisoInsuficiente(
                    "no hay permiso de escritura sobre un directorio del almacén, así que "
                    "esta transición no puede alcanzar durabilidad; no se declara "
                    "completada y el estado canónico queda intacto",
                    ruta=self._d.relativa(directorio),
                )

    def _publicar_objetos(self, transaccion, plan, raiz_base):
        """Paso 8, IDEMPOTENTE: lo que ya está publicado con su `cid` no se vuelve a tocar."""
        for operacion in plan:
            ruta = operacion["ruta"]
            destino = self._d.ruta_canonica(ruta)
            if operacion["accion"] == "escribir":
                if self._cid_en_disco(ruta) == operacion["cid"]:
                    continue          # ya publicado: repetir el `replace` sería inútil
                temporal = self._d.objeto_preparado(transaccion, ruta)
                if not os.path.exists(temporal):
                    raise EstadoCorrupto(
                        "falta el objeto preparado de la transacción", ruta=ruta,
                        transaccion=transaccion,
                    )
                encontrado = cid(leer_bytes(temporal, error=EstadoCorrupto))
                if encontrado != operacion["cid"]:
                    raise EstadoCorrupto(
                        "el objeto preparado no casa con el `cid` que el diario declara",
                        ruta=ruta, esperado=operacion["cid"], encontrado=encontrado,
                    )
                asegurar_directorio(os.path.dirname(destino))
                publicar(temporal, destino)
            else:
                presente = self._cid_en_disco(ruta)
                if presente is None:
                    continue          # ya borrado
                if presente != raiz_base.get(ruta):
                    raise EstadoCorrupto(
                        "el objeto a borrar no es el que la base declara: borrarlo "
                        "destruiría algo que el diario no explica",
                        ruta=ruta, esperado=raiz_base.get(ruta), encontrado=presente,
                    )
                borrar_si_existe(destino)

    def _sincronizar_dominios(self, plan):
        directorios = {os.path.dirname(self._d.ruta_canonica(op["ruta"])) for op in plan}
        for directorio in sorted(directorios):
            if os.path.isdir(directorio):
                sincronizar_directorio(directorio)
        sincronizar_directorio(self._d.canonico)

    def _revertir_especulativo(self, transaccion, base_id, plan, base):
        """Cierra la ventana de una transición que falló ANTES del punto de no retorno."""
        try:
            revision = self._leer_revision()
            if revision["revision_id"] != base_id:
                return                # alguien publicó: no es especulativo, lo ve `recuperar`
            for operacion in plan:
                if self._cid_en_disco(operacion["ruta"]) != base["raiz"].get(operacion["ruta"]):
                    return            # divergencia: la decide la autoridad, no este `except`
            borrar_arbol(self._d.zona_tx(transaccion))
            self._diario.anexar(
                "transicion.revertida",
                transaccion=transaccion, base=base_id, resultado=None,
                operaciones=plan, autor=AUTOR_RUNTIME,
                motivo="la preparación falló antes del punto de no retorno",
            )
        except ErrorDeEstado:
            # Si ni siquiera se puede revertir, la ventana queda abierta y `recuperar()` la
            # verá: es exactamente el caso para el que existe. No se enmascara el error
            # original del llamador, que es el que explica por qué se llegó hasta aquí.
            return

    def _escribir_anexos(self, anexos, revision, transaccion):
        """Registro auxiliar y evento de migración, ambos IDEMPOTENTES (recuperación)."""
        escritos = []
        if not anexos:
            return escritos
        momento = momento_logico(revision["diario_secuencia"], revision["revision"])
        # Una instantánea de cada fichero para TODAS las comprobaciones de este método. Se
        # ejecuta con el bloqueo de escritor tomado, así que nadie más añade eventos; aun
        # así se lee una vez y no cuatro, porque la regla vale igual cuando el que cambia
        # el fichero es uno mismo: las comprobaciones son de tipos distintos y ninguna se
        # invalida por lo que escriba la otra.
        eventos = self._diario.eventos()
        lineas = self._registro.lineas()
        datos = anexos.get("reconciliacion")
        if datos:
            if not self._registro.tiene_resolucion(datos["registro"], lineas):
                self._registro.anexar_resolucion(
                    registro=datos["registro"], transaccion=transaccion,
                    autoridad=datos["autoridad"], motivo=datos["motivo"], momento=momento,
                )
                escritos.append("registro:resolucion")
            if not self._hay_evento(transaccion, "reconciliacion.resuelta", eventos):
                self._diario.anexar(
                    "reconciliacion.resuelta",
                    transaccion=transaccion, registro=datos["registro"],
                    autoridad=datos["autoridad"], motivo=datos["motivo"], momento=momento,
                )
                escritos.append("diario:reconciliacion.resuelta")
        datos = anexos.get("migracion")
        if datos and not self._hay_evento(transaccion, "migracion.aplicada", eventos):
            self._diario.anexar(
                "migracion.aplicada",
                transaccion=transaccion, desde=datos["desde"], hasta=datos["hasta"],
                autor=AUTOR_RUNTIME, motivo=datos.get("motivo", "migración registrada"),
            )
            escritos.append("diario:migracion.aplicada")
        return escritos

    def _hay_evento(self, transaccion, tipo, eventos=None):
        for evento in (self._diario.eventos() if eventos is None else eventos):
            if evento.get("transaccion") == transaccion and evento.get("tipo") == tipo:
                return True
        return False

    def _resultado_si_repetida(self, transicion, eventos):
        """Semántica de idempotencia del §9: mismo `id` confirmado → no se vuelve a aplicar."""
        propios = [e for e in eventos if e.get("transaccion") == transicion.id]
        if not propios:
            return None
        tipos = {evento["tipo"] for evento in propios}
        plan = transicion.operaciones_a_dict()
        declarado = None
        for evento in propios:
            if evento["tipo"] in ("transicion.abierta", "transicion.preparada"):
                declarado = evento.get("operaciones")
                break
        if declarado is not None and declarado != plan:
            raise IdentificadorDuplicado(
                "ya existe una transacción con este identificador y con OTRAS operaciones; "
                "reutilizar el identificador haría que el diario explicase dos cambios "
                "distintos con la misma entrada",
                ruta=transicion.id,
            )
        if "transicion.confirmada" not in tipos:
            if tipos & {"transicion.revertida", "transicion.marcada"}:
                raise IdentificadorDuplicado(
                    "este identificador pertenece a una transacción ya cerrada sin "
                    "confirmar; reutilizarlo confundiría dos historias distintas",
                    ruta=transicion.id,
                )
            return None
        preparadas = [e for e in propios if e["tipo"] == "transicion.preparada"]
        if not preparadas:
            raise IdentificadorDuplicado(
                "hay una `transicion.confirmada` sin su `transicion.preparada`: el diario "
                "no explica de dónde salió esa revisión",
                ruta=transicion.id,
            )
        confirmada = preparadas[-1]
        revision_actual = self._leer_revision()
        numero = self._numero_de_revision(confirmada["resultado"], eventos)
        return ResultadoTransicion(
            transaccion=transicion.id,
            revision=numero if numero is not None else revision_actual["revision"],
            revision_id=confirmada["resultado"],
            padre=confirmada["base"],
            cid_raiz=self._cid_raiz_de(confirmada["resultado"], revision_actual, eventos),
            diario_secuencia=confirmada["secuencia"],
            operaciones=confirmada["operaciones"],
            repetida=True,
        )

    def _linaje(self, eventos=None):
        """La sucesión de `revision_id`, de la revisión 0 a la vigente, según el diario."""
        eventos = self._diario.eventos() if eventos is None else eventos
        agrupados = self._diario.por_transaccion(eventos)
        linaje = []
        for evento in eventos:
            if evento["tipo"] == "almacen.inicializado":
                linaje.append(evento["resultado"])
            elif evento["tipo"] == "transicion.preparada":
                tipos = {e["tipo"] for e in agrupados.get(evento["transaccion"], ())}
                if "transicion.confirmada" in tipos:
                    linaje.append(evento["resultado"])
        return linaje

    def _numero_de_revision(self, revision_id, eventos=None):
        linaje = self._linaje(eventos)
        return linaje.index(revision_id) if revision_id in linaje else None

    def _cid_raiz_de(self, revision_id, revision_actual, eventos=None):
        if revision_actual["revision_id"] == revision_id:
            return revision_actual["cid_raiz"]
        # Para una revisión que ya no es la vigente el `cid_raiz` se reproduce del diario;
        # no se guarda una copia, porque un segundo sitio donde vive el mismo dato es un
        # segundo sitio donde puede desincronizarse.
        raiz = {}
        for evento in (self._diario.eventos() if eventos is None else eventos):
            if evento["tipo"] == "almacen.inicializado":
                raiz = {}
            elif evento["tipo"] == "transicion.preparada":
                raiz = proyectar_raiz(raiz, evento["operaciones"])
            if evento.get("resultado") == revision_id:
                return calcular_cid_raiz(raiz)
        return calcular_cid_raiz(raiz)

    # =====================================================================
    #  recuperación (`g.8`)
    # =====================================================================
    def recuperar(self):
        """Cierra la ventana con COMPLETAR o REVERTIR, o MARCA. Idempotente (§3)."""
        self._exigir_operable()
        bloqueo = BloqueoExclusivo(self._d.bloqueo_escritor, "escritor")
        # Más intentos que una escritura normal: recuperar no compite por publicar, sólo
        # espera a que el escritor vivo termine. Si de verdad hay otro escritor, es él quien
        # está cerrando la ventana y no hace falta que la cerremos nosotros.
        intentos = 10
        try:
            bloqueo.adquirir(intentos=intentos)
        except EscritorConcurrente as exc:
            # `G-A5` y `g.6` no distinguen qué operación agotó los reintentos: exigen que
            # agotarlos deje las órdenes intactas Y produzca el registro auxiliar. Esta
            # rama faltaba, y era la que más se recorre: `abrir(recuperar=True)` llama aquí
            # en cada arranque, así que con otro escritor a mitad de transición —el caso
            # EXACTO del que habla `g.6`— se levantaba `EscritorConcurrente` a secas y la
            # pendencia no quedaba registrada en ninguna parte.
            registro = self._abrir_reconciliacion_por_reintentos(
                self._item_de_la_ventana(), intentos, exc
            )
            raise ReintentosAgotados(
                "no se pudo tomar el bloqueo de escritor para recuperar tras "
                + str(intentos) + " intento(s); la ventana sigue abierta, el estado "
                "canónico queda intacto y se abrió el registro auxiliar " + registro,
                ruta=self._d.relativa(self._d.bloqueo_escritor),
                registro=registro, intentos=intentos,
            ) from exc
        try:
            return self._recuperar_bajo_bloqueo()
        finally:
            bloqueo.liberar()

    def _item_de_la_ventana(self):
        """El identificador de la transacción sin cerrar, para el `item` de `g.9`.

        Se lee SIN el bloqueo —no lo tenemos, por eso estamos aquí— y por eso puede fallar
        o quedar desfasado. Un registro auxiliar sin `item` no es admisible por `g.9`, así
        que cuando no se puede averiguar se dice lo que se sabe, `recuperacion`, en vez de
        inventar un identificador que no correspondería a ninguna transacción.
        """
        try:
            sin_cerrar = self._diario.transaccion_sin_cerrar()
        except ErrorDeEstado:
            return "recuperacion"
        return sin_cerrar[0] if sin_cerrar else "recuperacion"

    def _recuperar_bajo_bloqueo(self):
        descartados = self._diario.reparar_cola()
        self._registro.reparar_cola()
        # Vuelve a anclar la cabeza del registro auxiliar al extremo real de su log. Cierra
        # la holgura de una línea que deja un corte entre el anexado y la publicación de la
        # cabeza, y con ella la única ventana en que borrar la cola no sería detectable.
        self._registro.sincronizar_cabeza()
        eventos = self._diario.eventos()
        marcadas = sorted({
            evento["transaccion"] for evento in eventos
            if evento["tipo"] == "transicion.marcada"
        })
        sin_cerrar = self._diario.transaccion_sin_cerrar(eventos)
        if sin_cerrar is None:
            self._limpiar_zonas_cerradas(eventos)
            return InformeRecuperacion(
                rama="ninguna", ventana_previa="cerrada", marcadas=marcadas,
                revision_id=self._leer_revision()["revision_id"],
                cola_del_diario_descartada=descartados,
            )
        transaccion, propios = sin_cerrar
        tipos = {evento["tipo"] for evento in propios}
        if "transicion.preparada" in tipos:
            preparada = [e for e in propios if e["tipo"] == "transicion.preparada"][-1]
            return self._completar(transaccion, preparada, descartados, marcadas)
        abierta = [e for e in propios if e["tipo"] == "transicion.abierta"][-1]
        return self._revertir(transaccion, abierta, descartados, marcadas)

    def _limpiar_zonas_cerradas(self, eventos):
        """Las zonas de preparación de transacciones ya cerradas son basura reconstruible."""
        raiz_tx = os.path.join(self._d.operacional, "tx")
        if not os.path.isdir(raiz_tx):
            return
        vivas = {
            evento["transaccion"] for evento in eventos
            if evento["tipo"] in ("transicion.abierta", "transicion.preparada")
        } - {
            evento["transaccion"] for evento in eventos
            if evento["tipo"] in ("transicion.confirmada", "transicion.revertida",
                                  "transicion.marcada")
        }
        for nombre in sorted(os.listdir(raiz_tx)):
            if nombre not in vivas:
                borrar_arbol(os.path.join(raiz_tx, nombre))

    def _revertir(self, transaccion, abierta, descartados, marcadas):
        """Rama REVERTIR: sólo `abierta`. Nada de `canonico/` se tocó; se verifica y se anota."""
        revision = self._leer_revision()
        divergencias = []
        if revision["revision_id"] != abierta["base"]:
            divergencias.append({
                "ruta": "REVISION.json", "donde": "revision",
                "esperado": abierta["base"], "encontrado": revision["revision_id"],
            })
        else:
            for operacion in abierta["operaciones"]:
                ruta = operacion["ruta"]
                esperado = revision["raiz"].get(ruta)
                # «Byte a byte»: el `cid` cubre todos los bytes del fichero. Si casa con la
                # base, el objeto no se tocó y revertir no destruye nada publicado.
                encontrado = self._cid_en_disco(ruta)
                if encontrado != esperado:
                    divergencias.append({
                        "ruta": ruta, "donde": "canonico",
                        "esperado": esperado, "encontrado": encontrado,
                    })
        if divergencias:
            return self._marcar(transaccion, abierta, divergencias, descartados, marcadas)

        borrar_arbol(self._d.zona_tx(transaccion))
        self._diario.anexar(
            "transicion.revertida",
            transaccion=transaccion, base=abierta["base"], resultado=None,
            operaciones=abierta["operaciones"], autor=AUTOR_RUNTIME,
            motivo="transacción abierta sin preparar: reversión de lo especulativo local",
        )
        return InformeRecuperacion(
            rama="revertir", ventana_previa="abierta", transaccion=transaccion,
            acciones=["verificada la base byte a byte", "descartada la zona de preparación"],
            eventos_anexados=["transicion.revertida"],
            revision_id=revision["revision_id"], marcadas=marcadas,
            cola_del_diario_descartada=descartados,
        )

    def _completar(self, transaccion, preparada, descartados, marcadas):
        """Rama COMPLETAR: se reejecutan los pasos 8, 9 y 10 de forma idempotente."""
        revision = self._leer_revision()
        plan = preparada["operaciones"]
        acciones = []
        divergencias = []

        if revision["revision_id"] == preparada["resultado"]:
            # El corte cayó DESPUÉS del punto de publicación: la revisión ya es la nueva.
            # Nada que republicar; sólo se comprueba que el árbol casa con lo publicado.
            for operacion in plan:
                ruta = operacion["ruta"]
                esperado = revision["raiz"].get(ruta)
                encontrado = self._cid_en_disco(ruta)
                if encontrado != esperado:
                    divergencias.append({
                        "ruta": ruta, "donde": "canonico",
                        "esperado": esperado, "encontrado": encontrado,
                    })
            acciones.append("la revisión ya estaba publicada: sólo se verifica")
        elif revision["revision_id"] == preparada["base"]:
            objetivo = proyectar_raiz(revision["raiz"], plan)
            faltan = self._comprobar_preparados(transaccion, plan, revision["raiz"])
            if faltan:
                divergencias.extend(faltan)
            else:
                self._publicar_objetos(transaccion, plan, revision["raiz"])
                self._sincronizar_dominios(plan)
                nueva = componer_revision(
                    revision["revision"] + 1, revision["revision_id"], objetivo,
                    transaccion, preparada["secuencia"],
                )
                if nueva["revision_id"] != preparada["resultado"]:
                    divergencias.append({
                        "ruta": "REVISION.json", "donde": "resultado",
                        "esperado": preparada["resultado"],
                        "encontrado": nueva["revision_id"],
                    })
                else:
                    self._publicar_revision(nueva)
                    revision = nueva
                    acciones.append("republicados los objetos preparados y la revisión")
        else:
            divergencias.append({
                "ruta": "REVISION.json", "donde": "revision",
                "esperado": preparada["base"], "encontrado": revision["revision_id"],
            })

        if divergencias:
            return self._marcar(transaccion, preparada, divergencias, descartados, marcadas)

        anexados = self._escribir_anexos(preparada.get("anexos"), revision, transaccion)
        self._diario.anexar(
            "transicion.confirmada",
            transaccion=transaccion, clase=preparada.get("clase", "transicion"),
            base=preparada["base"], resultado=preparada["resultado"],
            operaciones=plan, autor=preparada["autor"], motivo=preparada["motivo"],
            **({"anexos": preparada["anexos"]} if preparada.get("anexos") else {})
        )
        borrar_arbol(self._d.zona_tx(transaccion))
        return InformeRecuperacion(
            rama="completar", ventana_previa="preparada", transaccion=transaccion,
            acciones=acciones, eventos_anexados=anexados + ["transicion.confirmada"],
            revision_id=revision["revision_id"], marcadas=marcadas,
            cola_del_diario_descartada=descartados,
        )

    def _comprobar_preparados(self, transaccion, plan, raiz_base):
        """¿Está todo lo preparado, y casa con su `cid`? Si no, la rama es MARCAR."""
        problemas = []
        for operacion in plan:
            ruta = operacion["ruta"]
            if operacion["accion"] == "escribir":
                if self._cid_en_disco(ruta) == operacion["cid"]:
                    continue          # ya publicado antes del corte
                temporal = self._d.objeto_preparado(transaccion, ruta)
                if not os.path.exists(temporal):
                    problemas.append({
                        "ruta": ruta, "donde": "preparado",
                        "esperado": operacion["cid"], "encontrado": None,
                    })
                    continue
                encontrado = cid(leer_bytes(temporal, error=EstadoCorrupto))
                if encontrado != operacion["cid"]:
                    problemas.append({
                        "ruta": ruta, "donde": "preparado",
                        "esperado": operacion["cid"], "encontrado": encontrado,
                    })
            else:
                presente = self._cid_en_disco(ruta)
                if presente is not None and presente != raiz_base.get(ruta):
                    problemas.append({
                        "ruta": ruta, "donde": "canonico",
                        "esperado": raiz_base.get(ruta), "encontrado": presente,
                    })
        return problemas

    def _marcar(self, transaccion, evento, divergencias, descartados, marcadas):
        """Rama MARCAR: copia íntegra de lo divergente y `transicion.marcada`. NO decide."""
        destino = self._d.conflicto(transaccion)
        asegurar_directorio(destino)
        copiadas = []
        zona_objetos = os.path.join(self._d.zona_tx(transaccion), "objetos")
        if os.path.isdir(zona_objetos):
            for ruta_relativa in sorted(recorrer_canonico(zona_objetos)):
                origen = os.path.join(zona_objetos, *ruta_relativa.split("/"))
                copia = os.path.join(destino, "preparado", *ruta_relativa.split("/"))
                escribir_y_sincronizar(copia, leer_bytes(origen, error=EstadoCorrupto))
                copiadas.append("preparado/" + ruta_relativa)
        for operacion in evento.get("operaciones", []):
            ruta = operacion["ruta"]
            actual = self._d.ruta_canonica(ruta)
            if os.path.exists(actual):
                copia = os.path.join(destino, "canonico", *ruta.split("/"))
                escribir_y_sincronizar(copia, leer_bytes(actual, error=EstadoCorrupto))
                copiadas.append("canonico/" + ruta)
        if os.path.exists(self._d.revision):
            copia = os.path.join(destino, "REVISION.json")
            escribir_y_sincronizar(copia, leer_bytes(self._d.revision, error=EstadoCorrupto))
            copiadas.append("REVISION.json")

        divergencia = {
            "esquema": ESQUEMA,
            "transaccion": transaccion,
            "base": evento.get("base"),
            "resultado": evento.get("resultado"),
            "operaciones": evento.get("operaciones", []),
            "divergencias": divergencias,
            "copiado": sorted(copiadas),
        }
        escribir_y_sincronizar(
            os.path.join(destino, "DIVERGENCIA.json"), serializar_canonico(divergencia)
        )
        sincronizar_directorio(destino)
        sincronizar_directorio(self._d.conflictos)

        self._diario.anexar(
            "transicion.marcada",
            transaccion=transaccion, base=evento.get("base"),
            resultado=evento.get("resultado"), operaciones=evento.get("operaciones", []),
            autor=AUTOR_RUNTIME,
            motivo="lo encontrado no casa ni con la base ni con el resultado",
            divergencias=divergencias,
        )
        informe = InformeRecuperacion(
            rama="marcar",
            ventana_previa="preparada" if evento["tipo"] == "transicion.preparada" else "abierta",
            transaccion=transaccion,
            acciones=["copiado íntegro lo divergente"],
            eventos_anexados=["transicion.marcada"],
            revision_id=self._leer_revision()["revision_id"],
            conflicto=self._d.relativa(destino),
            marcadas=sorted(set(marcadas) | {transaccion}),
            cola_del_diario_descartada=descartados,
        )
        # `g.8`: la salida la decide LA AUTORIDAD. El runtime no elige, levanta y se aparta.
        error = RecuperacionMarcada(
            "la transacción " + transaccion + " diverge y se ha MARCADO; la copia íntegra "
            "está en " + informe.conflicto + " y la salida la decide la autoridad",
            ruta=informe.conflicto, transaccion=transaccion, divergencias=len(divergencias),
        )
        error.informe = informe
        raise error

    # =====================================================================
    #  integridad y auditoría (`g.5`, `g.13`)
    # =====================================================================
    def verificar_integridad(self):
        self._exigir_operable()
        hallazgos = []
        revision = self._leer_revision()
        raiz = revision["raiz"]

        en_disco = recorrer_canonico(self._d.canonico)
        for ruta in en_disco:
            if ruta not in raiz:
                hallazgos.append({
                    "codigo": "OBJETO_HUERFANO", "ruta": ruta,
                    "detalle": "hay un fichero en `canonico/` que la revisión no declara: "
                               "un cambio del estado que el diario no explica",
                })
        verificados = 0
        for ruta in sorted(raiz):
            encontrado = self._cid_en_disco(ruta)
            if encontrado is None:
                hallazgos.append({
                    "codigo": "OBJETO_AUSENTE", "ruta": ruta,
                    "detalle": "la revisión declara el objeto y el fichero no está",
                })
            elif encontrado != raiz[ruta]:
                hallazgos.append({
                    "codigo": "CID_NO_CASA", "ruta": ruta,
                    "detalle": "esperado " + raiz[ruta] + ", encontrado " + encontrado,
                })
            else:
                verificados += 1

        cid_raiz = calcular_cid_raiz(raiz)
        if cid_raiz != revision["cid_raiz"]:
            hallazgos.append({
                "codigo": "CID_RAIZ_NO_CASA", "ruta": "REVISION.json",
                "detalle": "esperado " + cid_raiz + ", declarado " + revision["cid_raiz"],
            })
        revision_id = calcular_revision_id(
            revision["revision"], revision["padre"], revision["cid_raiz"],
            revision["transaccion"],
        )
        if revision_id != revision["revision_id"]:
            hallazgos.append({
                "codigo": "REVISION_ID_NO_CASA", "ruta": "REVISION.json",
                "detalle": "esperado " + revision_id + ", declarado " + revision["revision_id"],
            })

        informe = InformeIntegridad(
            ok=False, revision=revision["revision"], revision_id=revision["revision_id"],
            cid_raiz=revision["cid_raiz"], objetos_verificados=verificados,
            eventos_del_diario=0, lineas_del_registro=0,
            reconciliaciones_pendientes=0, ventana="desconocida", hallazgos=hallazgos,
        )
        # El diario y el registro fallan cerrado por su cuenta; se les adjunta el informe
        # parcial para que la evidencia describa el daño y no sólo lo nombre.
        try:
            eventos, _ = self._diario.instantanea(tolerar_cola=True)
            lineas = self._registro.lineas()
            pendientes = self._registro.pendientes(lineas)
        except ErrorDeEstado as exc:
            exc.informe = informe
            raise
        informe.eventos_del_diario = len(eventos)
        informe.lineas_del_registro = len(lineas)
        informe.reconciliaciones_pendientes = len(pendientes)
        # De la instantánea ya leída, no de una lectura nueva: el informe describe UN
        # estado del almacén, y un campo tomado un instante después describiría otro.
        informe.ventana = self._ventana_de(eventos)

        # La cadena de hash no basta para el registro auxiliar: borrar la ÚLTIMA línea deja
        # un prefijo perfectamente encadenado. Lo que la delata es el CONTRASTE con el
        # diario, que anota por su cuenta cada apertura explícita y cada resolución. Es la
        # comprobación que hace cierto lo que el §9 promete: borrar el registro a mano
        # produce `RegistroDeReconciliacionCorrupto` al verificar.
        del_registro = []
        self._auditar_reconciliacion(eventos, del_registro, lineas)
        informe.hallazgos = hallazgos + del_registro
        if hallazgos:
            error = EstadoCorrupto(
                "la verificación de integridad encontró " + str(len(informe.hallazgos))
                + " hallazgo(s); el estado canónico NO se ha tocado",
                ruta=self._d.relativa(self._d.almacen), hallazgos=len(informe.hallazgos),
            )
            error.informe = informe
            raise error
        if del_registro:
            error = RegistroDeReconciliacionCorrupto(
                "el registro auxiliar no casa con el diario en " + str(len(del_registro))
                + " punto(s): se retiró una línea sin la transición explícita que `g.9` "
                "exige",
                ruta=self._d.relativa(self._d.registro),
            )
            error.informe = informe
            raise error
        informe.ok = True
        return informe

    def auditar(self):
        """Reproduce `cid_raiz` aplicando el diario desde el principio (§6)."""
        self._exigir_operable()
        revision = self._leer_revision()
        eventos = self._diario.eventos()
        agrupados = self._diario.por_transaccion(eventos)
        hallazgos = []

        raiz = {}
        numero = -1
        padre = None
        vigente = None
        confirmadas = 0
        for evento in eventos:
            if evento["tipo"] == "almacen.inicializado":
                raiz, numero, padre = {}, 0, None
                vigente = evento["resultado"]
            elif evento["tipo"] == "transicion.preparada":
                tipos = {e["tipo"] for e in agrupados.get(evento["transaccion"], ())}
                if "transicion.confirmada" not in tipos:
                    continue
                raiz = proyectar_raiz(raiz, evento["operaciones"])
                padre, numero = vigente, numero + 1
                reproducido = calcular_revision_id(
                    numero, padre, calcular_cid_raiz(raiz), evento["transaccion"]
                )
                if reproducido != evento["resultado"]:
                    hallazgos.append({
                        "codigo": "REVISION_NO_REPRODUCIBLE",
                        "ruta": evento["transaccion"],
                        "detalle": "el diario declara " + str(evento["resultado"])
                                   + " y reproduce " + reproducido,
                    })
                vigente = evento["resultado"]
                confirmadas += 1

        cid_raiz = calcular_cid_raiz(raiz)
        if numero < 0:
            hallazgos.append({
                "codigo": "SIN_INICIALIZACION", "ruta": "diario/DIARIO.jsonl",
                "detalle": "el diario no contiene `almacen.inicializado`: la historia del "
                           "estado no arranca en ninguna parte",
            })
        if cid_raiz != revision["cid_raiz"]:
            hallazgos.append({
                "codigo": "ESTADO_NO_EXPLICABLE", "ruta": "REVISION.json",
                "detalle": "el diario reproduce " + cid_raiz + " y la revisión declara "
                           + revision["cid_raiz"] + ": hay un cambio del estado canónico "
                           "que ningún evento explica",
            })
        if vigente is not None and vigente != revision["revision_id"]:
            hallazgos.append({
                "codigo": "LINAJE_NO_CASA", "ruta": "REVISION.json",
                "detalle": "el diario termina en " + str(vigente) + " y la revisión "
                           "vigente es " + revision["revision_id"],
            })
        for ruta in sorted(raiz):
            encontrado = self._cid_en_disco(ruta)
            if encontrado != raiz[ruta]:
                hallazgos.append({
                    "codigo": "OBJETO_NO_EXPLICABLE", "ruta": ruta,
                    "detalle": "el diario reproduce " + str(raiz[ruta]) + " y en disco hay "
                               + str(encontrado),
                })
        for ruta in recorrer_canonico(self._d.canonico):
            if ruta not in raiz:
                hallazgos.append({
                    "codigo": "OBJETO_NO_EXPLICABLE", "ruta": ruta,
                    "detalle": "hay un objeto en disco que el diario nunca escribió",
                })

        casadas = self._auditar_reconciliacion(eventos, hallazgos, self._registro.lineas())
        informe = InformeAuditoria(
            ok=not hallazgos, revision=revision["revision"],
            revision_id=revision["revision_id"], cid_raiz=revision["cid_raiz"],
            cid_raiz_reproducido=cid_raiz, transacciones_confirmadas=confirmadas,
            eventos=len(eventos), resoluciones_casadas=casadas, hallazgos=hallazgos,
        )
        if hallazgos:
            error = EstadoCorrupto(
                "la auditoría encontró " + str(len(hallazgos)) + " hallazgo(s): hay estado "
                "que el diario no explica",
                ruta=self._d.relativa(self._d.almacen),
            )
            error.informe = informe
            raise error
        return informe

    def _auditar_reconciliacion(self, eventos, hallazgos, lineas=None):
        """La correspondencia entre el diario y el registro auxiliar, en ambos sentidos.

        Contrasta DOS instantáneas, y el llamador debe pasar las mismas que usa para el
        resto de su informe: contrastar un diario de hace un instante con un registro de
        ahora inventa discrepancias que nunca existieron a la vez.
        """
        lineas = self._registro.lineas() if lineas is None else lineas
        aperturas = {l["registro"] for l in lineas if l["tipo"] == "apertura"}
        resoluciones = {(l["registro"], l["transaccion"]) for l in lineas
                        if l["tipo"] == "resolucion"}
        del_diario = {(e["registro"], e["transaccion"]) for e in eventos
                      if e["tipo"] == "reconciliacion.resuelta"}
        abiertas_diario = {e["registro"] for e in eventos
                           if e["tipo"] == "reconciliacion.abierta"}
        for registro in sorted(abiertas_diario - aperturas):
            hallazgos.append({
                "codigo": "APERTURA_SIN_REGISTRO", "ruta": registro,
                "detalle": "el diario anota la apertura y el registro auxiliar no la "
                           "contiene: se borró una línea del registro",
            })
        for registro, transaccion in sorted(del_diario - resoluciones):
            hallazgos.append({
                "codigo": "RESOLUCION_SIN_REGISTRO", "ruta": registro,
                "detalle": "la transacción " + transaccion + " resolvió la reconciliación "
                           "en el diario y el registro auxiliar no lo refleja",
            })
        for registro, transaccion in sorted(resoluciones - del_diario):
            hallazgos.append({
                "codigo": "RESOLUCION_SIN_TRANSICION", "ruta": registro,
                "detalle": "el registro auxiliar declara resuelta la reconciliación por la "
                           "transacción " + transaccion + " y el diario no la explica; "
                           "`g.9` sólo admite retirarla mediante transición explícita",
            })
        return len(resoluciones & del_diario)

    # =====================================================================
    #  reconciliación (`g.9`)
    # =====================================================================
    def reconciliacion_pendiente(self):
        """Aperturas sin resolución. Se DEDUCE del registro auxiliar; no se almacena.

        La deducción se hace sobre un registro COMPROBADO, no sobre lo que quede en el
        fichero. `g.9` exige que la pendencia se deduzca de forma INEQUÍVOCA y que sólo
        desaparezca por una transición explícita: si alguien retira la línea de resolución
        a mano, el registro vuelve a «deducir» una pendencia que ya se cerró, y si retira
        la apertura, cierra una pendencia sin transición. Las dos cosas son el mismo
        defecto, y las dos se denuncian aquí antes de responder.
        """
        self._exigir_operable()
        # Una instantánea de cada fichero, y las dos deducciones —comprobar la coherencia
        # y deducir las pendencias— salen de ellas. Con dos lecturas del registro, una
        # resolución anexada entre medias haría pasar la comprobación sobre un contenido y
        # responder sobre otro, y `g.9` exige que la deducción sea INEQUÍVOCA.
        lineas = self._registro.lineas()
        self._exigir_registro_coherente(lineas=lineas)
        return self._registro.pendientes(lineas)

    def _exigir_registro_coherente(self, eventos=None, lineas=None):
        """Contrasta el registro auxiliar con el diario. Fallo CERRADO si no casan.

        La cadena de huellas del registro detecta que se edite, se inserte o se retire
        cualquier línea que no sea la última; retirar la ÚLTIMA deja un prefijo
        perfectamente encadenado y hace falta esta segunda comprobación. Los dos ficheros
        siguen SEPARADOS (`I-g7`): no se derivan el uno del otro, se contrastan.
        """
        hallazgos = []
        if eventos is None:
            eventos, _ = self._diario.instantanea(tolerar_cola=True)
        self._auditar_reconciliacion(eventos, hallazgos, lineas)
        if hallazgos:
            error = RegistroDeReconciliacionCorrupto(
                "el registro auxiliar no casa con el diario en " + str(len(hallazgos))
                + " punto(s): " + hallazgos[0]["detalle"],
                ruta=self._d.relativa(self._d.registro),
            )
            error.hallazgos = hallazgos
            raise error

    def _abrir_reconciliacion_por_reintentos(self, item, intentos, causa):
        """Registro auxiliar tras agotar los reintentos. NO toca el estado canónico.

        No anota nada en el diario, y no puede: no tiene el bloqueo de escritor, y el diario
        es estado canónico. `g.6` exige justamente que este camino deje el estado intacto.

        `item` es una cadena y no una `Transicion` porque hay DOS operaciones que pueden
        agotar los reintentos y las dos deben producir este registro: la transición, cuyo
        `item` es su identificador, y la recuperación al arrancar, cuyo `item` es la
        transacción que iba a cerrar. `G-A5` no dice «al aplicar»: dice que agotar los
        reintentos deja las órdenes intactas Y produce el registro auxiliar.
        """
        self._bloqueo_registro.adquirir(intentos=20)
        try:
            revision = self._leer_revision()
            registro = self._registro.siguiente_identificador()
            self._registro.anexar_apertura(
                registro=registro,
                producto=os.path.basename(self._d.repo) or "control-repo",
                repositorio="control",
                item=item,
                intento=int(intentos),
                causa=causa.codigo + ": " + causa.detalle,
                momento=momento_logico(
                    self._diario.siguiente_secuencia(), revision["revision"]
                ),
            )
            return registro
        finally:
            self._bloqueo_registro.liberar()

    def abrir_reconciliacion(self, *, producto, repositorio, item, intento, causa):
        """Abre un registro auxiliar explícitamente, y lo anota también en el diario."""
        self._exigir_operable()
        bloqueo = BloqueoExclusivo(self._d.bloqueo_escritor, "escritor")
        bloqueo.adquirir(intentos=3)
        try:
            self._bloqueo_registro.adquirir(intentos=20)
            try:
                revision = self._leer_revision()
                registro = self._registro.siguiente_identificador()
                # El registro PRIMERO y el diario después: si un corte cae en medio queda
                # una apertura sin evento, que es la forma normal del camino por reintentos
                # agotados y no rompe nada. Al revés quedaría un evento sin registro, y eso
                # sí es un hallazgo de auditoría.
                self._registro.anexar_apertura(
                    registro=registro, producto=producto, repositorio=repositorio,
                    item=item, intento=intento, causa=causa,
                    momento=momento_logico(
                        self._diario.siguiente_secuencia(), revision["revision"]
                    ),
                )
                self._diario.anexar(
                    "reconciliacion.abierta",
                    registro=registro, producto=producto, repositorio=repositorio,
                    item=item, intento=intento, causa=causa, autor=AUTOR_RUNTIME,
                    motivo="apertura explícita de reconciliación",
                )
                return registro
            finally:
                self._bloqueo_registro.liberar()
        finally:
            bloqueo.liberar()

    def resolver_reconciliacion(self, registro, *, autoridad, motivo, operaciones=()):
        """ÚNICA vía de retirar `reconciliacion_pendiente` (§9): una transición explícita."""
        self._exigir_operable()
        # Las dos comprobaciones previas, sobre el MISMO corte del registro. Son un filtro
        # temprano para dar un error claro; la comprobación que MANDA es la de
        # `_escribir_anexos`, que corre con el bloqueo de escritor tomado y es la que
        # impide de verdad una segunda resolución.
        lineas = self._registro.lineas()
        apertura = self._registro.apertura_de(registro, lineas)
        if self._registro.tiene_resolucion(registro, lineas):
            raise ErrorDeEstado(
                "esa reconciliación ya está resuelta; el registro es append-only y una "
                "segunda resolución falsearía la deducción de `g.9`",
                codigo="RECONCILIACION_YA_RESUELTA", ruta=registro,
            )
        base = self._leer_revision()
        transaccion = identificador_derivado(base["revision"] + 1, {
            "tipo": "reconciliacion", "registro": registro, "autoridad": autoridad,
            "motivo": motivo, "item": apertura["item"],
            "operaciones": [op.a_dict() for op in operaciones],
        })
        transicion = Transicion(
            tipo="reconciliacion", base=base["revision_id"], operaciones=list(operaciones),
            autor=autoridad, motivo=motivo, id=transaccion,
        )
        return self._aplicar_con_anexos(transicion, intentos=3, anexos={
            "reconciliacion": {
                "registro": registro, "autoridad": autoridad, "motivo": motivo,
            }
        })

    # =====================================================================
    #  versionado, migración y bifurcación
    # =====================================================================
    def version_de_formato(self):
        """0 si el almacén es heredado; si no, la que declara `FORMATO.json`."""
        self._exigir_abierto()
        if self.heredado:
            return 0
        return _leer_formato(self._d)

    def migrar(self, a_version=VERSION_DE_FORMATO):
        """Aplica las migraciones REGISTRADAS y explícitas, cada una como transacción (§5)."""
        self._exigir_abierto()
        return _migracion.migrar(self, a_version)

    def detectar_bifurcacion(self, revision_ajena):
        """Compara linaje por `revision_id`/`padre`. NO resuelve: `g.6` no lo decide aquí."""
        self._exigir_operable()
        if not isinstance(revision_ajena, dict):
            raise TransicionInvalida("`revision_ajena` debe ser un `REVISION.json` leído")
        comprobar_esquema(revision_ajena, ruta="revision_ajena", error=VersionDesconocida)
        for clave in ("revision", "revision_id", "padre", "cid_raiz"):
            if clave not in revision_ajena:
                raise EstadoCorrupto(
                    "la revisión ajena no lleva `" + clave + "`", ruta="revision_ajena"
                )
        # La revisión PRIMERO y el diario después, y no al revés. El diario crece antes
        # que la revisión que lo cita —`preparada` se anexa antes de publicar
        # `REVISION.json`—, así que leer en este orden garantiza que el diario leído es al
        # menos tan nuevo como la revisión leída. Al revés se podría comparar una revisión
        # nueva contra un linaje viejo que todavía no la contiene.
        local = self._leer_revision()
        linaje = self._linaje()
        ajena_id = revision_ajena["revision_id"]
        ajena_padre = revision_ajena["padre"]

        if ajena_id == local["revision_id"]:
            relacion, comun = "identica", ajena_id
        elif ajena_id in linaje:
            relacion, comun = "ancestro-de-la-local", ajena_id
        elif ajena_padre == local["revision_id"]:
            relacion, comun = "descendiente-de-la-local", local["revision_id"]
        elif ajena_padre in linaje:
            relacion, comun = "bifurcada", ajena_padre
        else:
            relacion, comun = "sin-relacion-detectable", None
        return {
            "relacion": relacion,
            "bifurcada": relacion in ("bifurcada", "sin-relacion-detectable"),
            "antepasado_comun": comun,
            "local": {
                "revision": local["revision"], "revision_id": local["revision_id"],
                "cid_raiz": local["cid_raiz"],
            },
            "ajena": {
                "revision": revision_ajena["revision"], "revision_id": ajena_id,
                "cid_raiz": revision_ajena["cid_raiz"],
            },
            # `g.6` lo dice expresamente: la bifurcación se DETECTA, y su resolución no se
            # decide en la norma. Tampoco aquí. Este campo existe para que nadie construya
            # encima un automatismo creyendo que el motor ya eligió.
            "resolucion": "no-se-decide-aqui",
        }

    # ------------------------------------------------------------------- cierre
    def cerrar(self):
        self._bloqueo_registro.liberar()
        self._cerrado = True

    def __enter__(self):
        return self

    def __exit__(self, tipo, valor, traza):
        self.cerrar()
        return False
