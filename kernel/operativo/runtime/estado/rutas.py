#!/usr/bin/env python3
"""rutas — la disposición física del almacén y las primitivas de escritura durable.

Dos materias, y viven juntas por una razón: **la durabilidad es una propiedad de la
disposición**, no del contenido. Dónde cae un fichero decide qué hay que sincronizar para
que sobreviva a un corte, y separar «dónde» de «cómo se sincroniza» invitaría a escribir
en un sitio nuevo olvidando el `fsync` del directorio que lo contiene.

Disposición (§2), y qué es durable y qué no (`g.1`):

    estado/FORMATO.json                    durable
    estado/REVISION.json                   durable · ÚNICO punto de publicación atómica
    estado/canonico/<dominio>/<id>.json    durable · ESTADO CANÓNICO
    estado/diario/DIARIO.jsonl             durable · DIARIO CANÓNICO
    estado/reconciliacion/REGISTRO.jsonl   durable · REGISTRO OPERATIVO AUXILIAR
    estado/reconciliacion/conflictos/<tx>/ durable · copia íntegra de lo divergente
    estado/operacional/                    NO durable · reconstruible · ignorado por Git

DECISIÓN · `fsync` sobre el DIRECTORIO, y no sólo sobre el fichero
    Alternativas: (a) `fsync` del fichero y confiar en que la entrada de directorio llegue
    sola; (b) `fsync` del fichero y además del directorio que lo contiene.
    Se elige (b). Un `os.replace` es atómico respecto a los lectores, pero la ENTRADA DE
    DIRECTORIO que ese `replace` crea es metadato del directorio, y en POSIX no hay ninguna
    promesa de que un `fsync` del fichero la arrastre. Con (a), tras un corte de corriente
    el contenido estaría en el disco y el nombre no, y `g.4` —«lo confirmado como durable
    SOBREVIVE a un corte»— quedaría en una afirmación sin respaldo. El directorio se abre
    con `os.open(d, os.O_RDONLY)` porque un directorio no se puede abrir para escritura.

DECISIÓN · validación de ruta lógica por FORMA y además por RESOLUCIÓN REAL
    Alternativas: (a) rechazar `..` textualmente; (b) resolver de verdad el destino y
    comprobar que cae dentro del árbol.
    Se hacen LAS DOS. `..` no es la única forma de salir de un directorio: un enlace
    simbólico en cualquier antecesor lo consigue sin escribir un solo punto. Es la misma
    regla que `tooling/workspace.py` aplica al workspace, y aquí protege algo más grave:
    una ruta lógica que se escapa de `canonico/` escribiría fuera del árbol verificado y
    ese byte no aparecería en `cid_raiz`, es decir, sería un cambio del estado NO explicable
    por el diario, contra `g.13`.

DECISIÓN · el `.gitignore` de `operacional/` se escribe al inicializar, no se documenta
    `g.14` exige que la rama canónica NUNCA contenga estado parcial, y la zona de
    preparación es estado parcial por definición. Un `.gitignore` que hay que acordarse de
    poner a mano es una promesa; uno que el motor escribe al inicializar es un hecho.
"""
from __future__ import annotations

import errno
import os
import re
import shutil

from .errores import ErrorDeEstado, EstadoCorrupto, PermisoInsuficiente, RutaInvalida

RAIZ_ALMACEN = "estado"
FORMATO = "FORMATO.json"
REVISION = "REVISION.json"
SUFIJO_TEMPORAL = ".tmp"
CANONICO = "canonico"
DIARIO = "diario"
FICHERO_DIARIO = "DIARIO.jsonl"
RECONCILIACION = "reconciliacion"
FICHERO_REGISTRO = "REGISTRO.jsonl"
CONFLICTOS = "conflictos"
OPERACIONAL = "operacional"
BLOQUEO_ESCRITOR = "escritor.lock"
BLOQUEO_REGISTRO = "registro.lock"
ZONA_TX = "tx"
OBJETOS_TX = "objetos"
GITIGNORE = ".gitignore"

# Un segmento de ruta lógica es un identificador ESTABLE que aparece en `cid_raiz`, en las
# claves de `REVISION.json` y en la salida que lee una persona. Se acota a lo que no puede
# confundirse con otra cosa: sin espacios, sin saltos de línea que inventen una línea de
# error falsa, y sin `.` ni `..` que parezcan un salto de directorio.
SEGMENTO_VALIDO = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
IDENTIFICADOR_VALIDO = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,95}$")

CONTENIDO_GITIGNORE = (
    "# Lo OPERACIONAL no es estado durable (`g.1`): bloqueos y zona de preparación son\n"
    "# reconstruibles, y su desaparición no pierde ninguna verdad. Que no entren en la\n"
    "# rama canónica es lo que impide que ésta contenga estado parcial (`g.14`).\n"
    + OPERACIONAL + "/\n"
)


# --------------------------------------------------------------- rutas lógicas
def comprobar_identificador(valor, que="identificador"):
    """Un `id` de transacción o de registro que no se pueda confundir con una ruta."""
    if not isinstance(valor, str) or not IDENTIFICADOR_VALIDO.match(valor):
        raise RutaInvalida(
            "el " + que + " debe casar con " + IDENTIFICADOR_VALIDO.pattern
            + " y no puede llevar espacios, saltos de línea ni separadores de ruta",
            ruta=valor if isinstance(valor, str) else None,
        )
    return valor


def comprobar_ruta_logica(ruta):
    """Valida `<dominio>/<id>.json` por FORMA. La resolución real la hace `ruta_canonica`.

    Se exigen exactamente dos segmentos porque el §2 fija `canonico/<dominio>/<id>.json`:
    admitir profundidad arbitraria sería mecanismo nuevo que nadie ha decidido, y las
    claves de `raiz` dejarían de tener una forma comprobable.
    """
    if not isinstance(ruta, str) or not ruta:
        raise RutaInvalida("la ruta lógica debe ser una cadena no vacía")
    if "\\" in ruta or "\n" in ruta or "\r" in ruta or "\0" in ruta:
        raise RutaInvalida("la ruta lógica lleva un carácter prohibido", ruta=ruta)
    if ruta.startswith("/") or os.path.isabs(ruta):
        raise RutaInvalida("la ruta lógica es relativa a `canonico/`, nunca absoluta", ruta=ruta)
    partes = ruta.split("/")
    if len(partes) != 2:
        raise RutaInvalida(
            "la ruta lógica es `<dominio>/<id>.json`, con exactamente dos segmentos",
            ruta=ruta,
        )
    dominio, hoja = partes
    if not SEGMENTO_VALIDO.match(dominio):
        raise RutaInvalida(
            "dominio inválido: debe casar con " + SEGMENTO_VALIDO.pattern, ruta=ruta
        )
    if not hoja.endswith(".json"):
        raise RutaInvalida("el objeto canónico se nombra `<id>.json`", ruta=ruta)
    if not SEGMENTO_VALIDO.match(hoja[: -len(".json")]):
        raise RutaInvalida(
            "identificador inválido: debe casar con " + SEGMENTO_VALIDO.pattern, ruta=ruta
        )
    return ruta


def dominio_de(ruta):
    return ruta.split("/", 1)[0]


# ------------------------------------------------------------------ disposición
class Disposicion:
    """Las rutas físicas de un almacén concreto. Sólo compone; no toca el disco."""

    def __init__(self, ruta_control_repo):
        if not isinstance(ruta_control_repo, str) or not ruta_control_repo:
            raise RutaInvalida("la ruta del control repo debe ser una cadena no vacía")
        # `abspath` y no `realpath`: el control repo puede ser legítimamente un enlace
        # (un workspace montado), y resolverlo cambiaría las rutas relativas que la CLI
        # imprime, que el §11 exige deterministas. La defensa contra enlaces se aplica
        # DENTRO del árbol, en `ruta_canonica`, que es donde importa.
        self.repo = os.path.abspath(ruta_control_repo)
        self.almacen = os.path.join(self.repo, RAIZ_ALMACEN)

    @property
    def formato(self):
        return os.path.join(self.almacen, FORMATO)

    @property
    def revision(self):
        return os.path.join(self.almacen, REVISION)

    @property
    def revision_temporal(self):
        return self.revision + SUFIJO_TEMPORAL

    @property
    def canonico(self):
        return os.path.join(self.almacen, CANONICO)

    @property
    def diario(self):
        return os.path.join(self.almacen, DIARIO, FICHERO_DIARIO)

    @property
    def reconciliacion(self):
        return os.path.join(self.almacen, RECONCILIACION)

    @property
    def registro(self):
        return os.path.join(self.reconciliacion, FICHERO_REGISTRO)

    @property
    def conflictos(self):
        return os.path.join(self.reconciliacion, CONFLICTOS)

    @property
    def operacional(self):
        return os.path.join(self.almacen, OPERACIONAL)

    @property
    def bloqueo_escritor(self):
        return os.path.join(self.operacional, BLOQUEO_ESCRITOR)

    @property
    def bloqueo_registro(self):
        return os.path.join(self.operacional, BLOQUEO_REGISTRO)

    @property
    def gitignore(self):
        return os.path.join(self.almacen, GITIGNORE)

    def zona_tx(self, transaccion):
        comprobar_identificador(transaccion, "identificador de transacción")
        return os.path.join(self.operacional, ZONA_TX, transaccion)

    def objeto_preparado(self, transaccion, ruta_logica):
        comprobar_ruta_logica(ruta_logica)
        return os.path.join(self.zona_tx(transaccion), OBJETOS_TX, *ruta_logica.split("/"))

    def conflicto(self, transaccion):
        comprobar_identificador(transaccion, "identificador de transacción")
        return os.path.join(self.conflictos, transaccion)

    def ruta_canonica(self, ruta_logica):
        """Ruta física de un objeto canónico, verificada de VERDAD contra la evasión.

        La comprobación no es textual: se resuelve el antecesor existente más próximo y se
        exige que caiga dentro de `canonico/`. Un enlace simbólico plantado en un dominio
        sacaría la escritura fuera del árbol sin escribir un solo `..`, y ese byte no
        entraría en `cid_raiz`: sería un cambio del estado canónico no explicable por el
        diario, que es justo lo que `g.13` prohíbe.
        """
        comprobar_ruta_logica(ruta_logica)
        destino = os.path.join(self.canonico, *ruta_logica.split("/"))
        base = os.path.realpath(self.canonico) if os.path.exists(self.canonico) else \
            os.path.abspath(self.canonico)
        sonda = destino
        while not os.path.exists(sonda) and os.path.dirname(sonda) != sonda:
            sonda = os.path.dirname(sonda)
        resuelto = os.path.realpath(sonda)
        if resuelto != base and not resuelto.startswith(base + os.sep):
            raise RutaInvalida(
                "la ruta lógica se resuelve FUERA de `canonico/`; hay un enlace simbólico "
                "en el camino y por ahí se escribiría estado que `cid_raiz` no vería",
                ruta=ruta_logica,
            )
        return destino

    def relativa(self, ruta_fisica):
        """Ruta relativa al control repo, para que la salida no publique rutas de máquina."""
        try:
            return os.path.relpath(ruta_fisica, self.repo).replace(os.sep, "/")
        except ValueError:
            # En otro volumen no hay relativa posible; se devuelve el nombre a secas antes
            # que una ruta absoluta, que el §11 prohíbe imprimir sin `--json`.
            return os.path.basename(ruta_fisica)


# ------------------------------------------------- primitivas durables de disco
def traducir_error_de_sistema(exc, ruta=None, accion=""):
    """Convierte un `OSError` en un error TIPADO del §8. Nunca se deja escapar crudo."""
    if exc.errno in (errno.EACCES, errno.EPERM, errno.EROFS):
        return PermisoInsuficiente(
            "permiso insuficiente" + (" al " + accion if accion else "") + ": " + exc.strerror,
            ruta=ruta,
        )
    return ErrorDeEstado(
        "fallo de sistema de ficheros" + (" al " + accion if accion else "") + ": "
        + (exc.strerror or str(exc)),
        ruta=ruta,
        codigo="FALLO_DE_SISTEMA_DE_FICHEROS",
        errno=errno.errorcode.get(exc.errno, exc.errno),
    )


def asegurar_directorio(ruta):
    try:
        os.makedirs(ruta, exist_ok=True)
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "crear el directorio") from exc
    return ruta


def sincronizar_directorio(ruta):
    """`fsync` sobre el DIRECTORIO: es lo que hace durable el NOMBRE, no el contenido."""
    try:
        descriptor = os.open(ruta, os.O_RDONLY)
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "abrir el directorio para sincronizar") from exc
    try:
        os.fsync(descriptor)
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "sincronizar el directorio") from exc
    finally:
        os.close(descriptor)


def escribir_fichero(ruta, datos):
    """Escribe el fichero ENTERO. NO sincroniza: los bytes quedan en la caché de página.

    Escribir y sincronizar son dos pasos separados porque el §3 los separa —paso 5 escribe,
    paso 6 sincroniza— y entre ambos hay un punto de fallo declarado. Fundirlos en una sola
    llamada haría inalcanzable `despues-de-escribir-temporal`, y con él el escenario en que
    un corte encuentra los bytes escritos pero no durables, que es el caso que `g.4` obliga
    a demostrar.
    """
    asegurar_directorio(os.path.dirname(ruta))
    try:
        descriptor = os.open(ruta, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "abrir para escribir") from exc
    try:
        pendiente = memoryview(datos)
        while pendiente:
            escritos = os.write(descriptor, pendiente)
            # `os.write` puede escribir MENOS de lo pedido y no es un error: un bucle es la
            # única forma correcta de escribir un búfer grande sobre un descriptor crudo.
            pendiente = pendiente[escritos:]
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "escribir") from exc
    finally:
        os.close(descriptor)


def sincronizar_fichero(ruta):
    """Lleva al medio los bytes ya escritos. Es lo que convierte «escrito» en «durable»."""
    try:
        descriptor = os.open(ruta, os.O_RDONLY)
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "abrir para sincronizar") from exc
    try:
        os.fsync(descriptor)
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "sincronizar") from exc
    finally:
        os.close(descriptor)


def escribir_y_sincronizar(ruta, datos):
    """Escribe y sincroniza en un solo gesto, para las fronteras que no separan ambos pasos."""
    escribir_fichero(ruta, datos)
    sincronizar_fichero(ruta)


def publicar(origen, destino):
    """`os.replace`: el intercambio de nombre atómico. NO sincroniza el directorio.

    Se deja fuera el `fsync` del directorio a propósito: el protocolo del §3 publica varios
    objetos y luego sincroniza, y hacerlo aquí escondería un punto de fallo que el §10
    nombra (`antes-de-sincronizar-directorio`) donde nadie podría inyectarlo.
    """
    try:
        os.replace(origen, destino)
    except OSError as exc:
        raise traducir_error_de_sistema(exc, destino, "publicar") from exc


def leer_bytes(ruta, error=EstadoCorrupto):
    try:
        with open(ruta, "rb") as fichero:
            return fichero.read()
    except FileNotFoundError as exc:
        raise error("el fichero no existe", ruta=ruta) from exc
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "leer") from exc


def borrar_si_existe(ruta):
    try:
        os.remove(ruta)
        return True
    except FileNotFoundError:
        # No existe: el efecto pedido ya está conseguido. Es lo que hace idempotente al
        # borrado durante la recuperación, que puede repetir el paso 8 varias veces.
        return False
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "borrar") from exc


def borrar_arbol(ruta):
    """Borra la zona de preparación. Sólo se usa sobre `operacional/`, nunca sobre durable."""
    try:
        shutil.rmtree(ruta)
        return True
    except FileNotFoundError:
        return False
    except OSError as exc:
        raise traducir_error_de_sistema(exc, ruta, "borrar el árbol") from exc


def recorrer_canonico(raiz_canonico):
    """Todas las rutas lógicas presentes EN DISCO bajo `canonico/`, ordenadas.

    Recorre el disco y no `REVISION.json` a propósito: la diferencia entre lo que hay y lo
    que la revisión dice que hay es exactamente lo que delata una modificación a mano, y
    `g.13` exige detectarla. Un recorrido que partiera de la revisión nunca vería un
    fichero huérfano.
    """
    encontradas = []
    if not os.path.isdir(raiz_canonico):
        return encontradas
    for dominio in sorted(os.listdir(raiz_canonico)):
        directorio = os.path.join(raiz_canonico, dominio)
        if not os.path.isdir(directorio):
            raise EstadoCorrupto(
                "`canonico/` sólo contiene directorios de dominio; hay un fichero suelto",
                ruta=dominio,
            )
        for hoja in sorted(os.listdir(directorio)):
            if os.path.isdir(os.path.join(directorio, hoja)):
                raise EstadoCorrupto(
                    "`canonico/<dominio>/` sólo contiene objetos `<id>.json`; hay un "
                    "subdirectorio, y su contenido no entraría en `cid_raiz`",
                    ruta=dominio + "/" + hoja,
                )
            encontradas.append(dominio + "/" + hoja)
    return encontradas
