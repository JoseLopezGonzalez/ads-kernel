#!/usr/bin/env python3
"""lease — la AUTORIDAD TEMPORAL sobre un paquete, medida en REVISIONES y no en reloj.

Instancia el §3 del contrato del corte 2 y la materia que `g.6` deja calibrable —«la
bifurcación entre máquinas se DETECTA; su resolución NO se decide en esta sección, y queda
declarada como materia calibrable del contrato derivado»—.

EL TIEMPO LÓGICO ES LA REVISIÓN. `I-g3` prohíbe reloj de pared, duración, número de
ejecución e identidad de proceso en cualquier byte durable, y un lease con caducidad es,
literalmente, un reloj escrito en el estado. Aquí la caducidad se sustituye por
OBSERVACIONES CONTADAS:

    · `latido` es un contador que el TITULAR incrementa en cada transición suya sobre el
      paquete. No mide tiempo: mide progreso.
    · un ASPIRANTE que quiere reclamar escribe OBSERVACIONES. Cada observación es una
      transición durable que anota, bajo su nombre, el `latido` que vio.
    · cuando el aspirante acumula `PACIENCIA` observaciones consecutivas **sin que el
      latido avance**, puede reclamar: sube `epoca`, se pone como `titular`, reinicia
      `latido` y `observado_por`.

DECISIÓN · `observado_por[aspirante]` es un objeto `{latido, observaciones}`, y no un entero
    El §3 dice dos cosas a la vez: que la observación «anota en `observado_por[aspirante]`
    el `latido` visto», y que se reclama tras «`PACIENCIA` observaciones CONSECUTIVAS sin
    que `latido` avance». Con un solo entero sólo se puede guardar una de las dos.
    Alternativas: (a) guardar el latido visto y deducir la consecutividad de que el titular
    limpie `observado_por` cada vez que late; (b) guardar el recuento y perder el latido
    visto; (c) guardar los dos.
    Se elige (c) y se REPORTA la ambigüedad al coordinador. (a) hace que la corrección
    dependa de que el TITULAR haga limpieza, y el titular que estamos midiendo es
    precisamente el que se presume muerto: una garantía que depende del muerto no es una
    garantía. (b) pierde el dato que el §3 nombra explícitamente. Con (c) el aspirante
    detecta por sí mismo que el latido avanzó y REINICIA su cuenta a uno, sin depender de
    nadie; el titular sigue limpiando `observado_por` al latir, y las dos mitades coinciden
    en vez de sustituirse. La forma del ejemplo del §3 —`{"runtime-B": 2}`— queda como
    `{"runtime-B": {"latido": 7, "observaciones": 2}}`, con el mismo significado y el dato
    que faltaba.

DECISIÓN · la vía rápida por `flock` NO sustituye a las observaciones, y sólo vale hacia abajo
    El §3 la describe como atajo de la MISMA máquina: el titular mantiene un `flock` sobre
    `estado/operacional/runtime/<instancia>.vivo`, y si un aspirante consigue ese `flock`,
    el titular está muerto y la reclamación es inmediata. Ese fichero vive en el plano
    OPERACIONAL, que está gitignorado y no es estado durable: ahí sí puede haber reloj y
    pid, y de hecho el núcleo suelta el `flock` solo cuando el proceso muere, que es
    justamente la propiedad que se quiere.
    La vía rápida sólo puede concluir «MUERTO», nunca «VIVO»: si el fichero no existe, la
    respuesta es `None` —no se puede decidir— y NO «está muerto». Entre máquinas el
    fichero de un titular remoto sencillamente no está, y concluir de su ausencia que el
    titular murió sería doble despacho por la puerta de atrás. Manda entonces la regla de
    las observaciones, que es la que `g.6` deja a este contrato.

DECISIÓN · EL TESTIGO DESAPARECE EN LA SALIDA LIMPIA, y esto era un DEFECTO GRAVE
    Corregido tras la integración, y merece contarse porque el error era sutil y tumbaba la
    capacidad 5 del §7 entera. `cerrar()` soltaba el `flock` y dejaba el fichero. Pero
    entonces un proceso que TERMINA BIEN deja exactamente la misma huella que uno que
    MURIÓ —fichero presente, `flock` libre—, y la vía rápida no puede distinguirlos. En el
    modelo de la CLI, que es un proceso por orden, el titular NUNCA está vivo entre dos
    órdenes, así que cualquier segunda instancia leía «muerto» y se llevaba el lease sin
    una sola observación:

        ads_runtime --instancia runtime-A adquirir pq-ok   → titular runtime-A, época 1
        ads_runtime --instancia runtime-B adquirir pq-ok   → titular runtime-B, época 2

    El lease no protegía nada. Ahora `cerrar()` BORRA el fichero, y las tres lecturas
    quedan separadas de verdad:

        no existe                 → salió limpiamente, o es de otra máquina → `None`,
                                    INDECIDIBLE, y manda la regla de las observaciones
        existe y `flock` TOMADO   → `False`, hay un proceso vivo con ese nombre
        existe y `flock` LIBRE    → `True`, MURIÓ sin poder limpiar. SÓLO un final abrupto
                                    —`os._exit`, `SIGKILL`, corte de corriente— deja esa
                                    combinación, porque ninguno de los tres ejecuta
                                    `finally`

    El borrado va ANTES de soltar el `flock`, y no después: entre soltar y borrar habría un
    instante con «existe y libre», que es justo la lectura peligrosa. Y se borra sólo si el
    fichero SIGUE siendo el nuestro —se compara el inodo—, porque otra instancia homónima
    que arrancase mientras cerramos habría creado ya el suyo, y borrarlo la dejaría sin
    testigo estando viva.
"""
from __future__ import annotations

import errno
import fcntl
import os

from estado.rutas import asegurar_directorio, traducir_error_de_sistema

from .errores import AutoridadPerdida, RuntimeInconsistente
from .modelo import ESQUEMA

PACIENCIA_POR_DEFECTO = 3

# Subdirectorio del plano OPERACIONAL donde vive el testigo de vida de cada instancia.
# `estado/.gitignore` excluye `operacional/` entero, de modo que nada de esto entra en la
# rama canónica y `g.14` sigue siendo cierto.
SUBDIRECTORIO_VIVOS = "runtime"
SUFIJO_VIVO = ".vivo"

CLAVES_DE_LEASE = ("paquete", "titular", "epoca", "revision_adquirida", "latido",
                   "observado_por")


# ------------------------------------------------------------------- objeto durable
def nuevo_lease(*, paquete, titular, revision_adquirida, epoca=1):
    return {
        "esquema": ESQUEMA,
        "paquete": paquete,
        "titular": titular,
        "epoca": int(epoca),
        "revision_adquirida": revision_adquirida,
        "latido": 0,
        "observado_por": {},
    }


def comprobar_lease(objeto, ruta):
    """FALLO CERRADO ante un lease que ninguna regla sabe interpretar."""
    if not isinstance(objeto, dict):
        raise RuntimeInconsistente("el lease no es un mapa JSON", ruta=ruta)
    faltan = [clave for clave in CLAVES_DE_LEASE if clave not in objeto]
    if faltan:
        raise RuntimeInconsistente("el lease no declara " + ", ".join(faltan), ruta=ruta)
    if not isinstance(objeto["titular"], str) or not objeto["titular"].strip():
        raise RuntimeInconsistente("`titular` es una cadena no vacía", ruta=ruta)
    for nombre in ("epoca", "latido"):
        if not isinstance(objeto[nombre], int) or isinstance(objeto[nombre], bool):
            raise RuntimeInconsistente("`" + nombre + "` es un entero", ruta=ruta)
    if objeto["epoca"] < 1 or objeto["latido"] < 0:
        raise RuntimeInconsistente(
            "`epoca` empieza en 1 y `latido` no puede ser negativo", ruta=ruta)
    observado = objeto["observado_por"]
    if not isinstance(observado, dict):
        raise RuntimeInconsistente("`observado_por` es un mapa", ruta=ruta)
    for aspirante, anotacion in observado.items():
        if not isinstance(anotacion, dict) or "latido" not in anotacion \
                or "observaciones" not in anotacion:
            raise RuntimeInconsistente(
                "la observación de `" + str(aspirante) + "` no declara `latido` y "
                "`observaciones`", ruta=ruta,
            )
    return objeto


def es_titular(lease, instancia):
    return bool(lease) and lease.get("titular") == instancia


def exigir_titularidad(lease, instancia, epoca_esperada, *, paquete):
    """La comprobación del §3 antes de escribir cualquier resultado. NO escribe nada.

    Se llama RELEYENDO el lease del estado canónico, nunca sobre la copia que el llamador
    tenía en la mano: comprobar contra la copia vieja es no comprobar.
    """
    if lease is None:
        raise AutoridadPerdida(
            "el lease del paquete ya no existe: otro lo liberó o lo reclamó",
            ruta=paquete,
        )
    if lease["titular"] != instancia:
        raise AutoridadPerdida(
            "el lease cambió de titular bajo los pies: ahora lo tiene `"
            + lease["titular"] + "`",
            ruta=paquete, titular=lease["titular"], epoca=lease["epoca"],
        )
    if epoca_esperada is not None and lease["epoca"] != epoca_esperada:
        raise AutoridadPerdida(
            "la época del lease subió bajo los pies: se adquirió en la "
            + str(epoca_esperada) + " y ahora es la " + str(lease["epoca"]),
            ruta=paquete, epoca=lease["epoca"], esperada=epoca_esperada,
        )
    return lease


def con_latido(lease):
    """Sube el `latido` y limpia las observaciones: el titular ha demostrado progreso."""
    nuevo = dict(lease)
    nuevo["latido"] = int(lease["latido"]) + 1
    nuevo["observado_por"] = {}
    return nuevo


def con_observacion(lease, aspirante):
    """Anota una observación del aspirante y devuelve el lease resultante.

    La cuenta se reinicia a uno en cuanto el `latido` anotado difiere del vigente: el
    titular ha avanzado, luego las observaciones anteriores dejaron de ser consecutivas.
    Esa comprobación la hace el ASPIRANTE sobre lo que él mismo anotó, y por eso no
    depende de que el titular limpie nada.
    """
    if es_titular(lease, aspirante):
        raise RuntimeInconsistente(
            "el titular no se observa a sí mismo: para renovar su autoridad usa `renovar`",
            ruta=lease["paquete"], titular=aspirante,
        )
    latido = int(lease["latido"])
    previa = lease["observado_por"].get(aspirante)
    if isinstance(previa, dict) and previa.get("latido") == latido:
        observaciones = int(previa.get("observaciones", 0)) + 1
    else:
        observaciones = 1
    nuevo = dict(lease)
    nuevo["observado_por"] = dict(lease["observado_por"])
    nuevo["observado_por"][aspirante] = {
        "latido": latido, "observaciones": observaciones,
    }
    return nuevo


def observaciones_de(lease, aspirante):
    """Observaciones CONSECUTIVAS del aspirante sobre el latido VIGENTE. Cero si no casan."""
    anotacion = lease["observado_por"].get(aspirante)
    if not isinstance(anotacion, dict):
        return 0
    if anotacion.get("latido") != int(lease["latido"]):
        # El titular latió después de la anotación: la racha se rompió y hay que empezar.
        return 0
    return int(anotacion.get("observaciones", 0))


def reclamado_por(lease, aspirante, revision_adquirida):
    """Sube la época, cambia el titular y reinicia `latido` y `observado_por` (§3)."""
    return {
        "esquema": ESQUEMA,
        "paquete": lease["paquete"],
        "titular": aspirante,
        "epoca": int(lease["epoca"]) + 1,
        "revision_adquirida": revision_adquirida,
        "latido": 0,
        "observado_por": {},
    }


# --------------------------------------------------------------- vía rápida local
class TestigoDeVida:
    """`flock` sobre `estado/operacional/runtime/<instancia>.vivo`. NO es estado durable.

    Se toma al abrir el runtime y lo suelta el NÚCLEO cuando el proceso muere, sin
    `finally`, sin `atexit` y sin cooperación del proceso muerto. Un centinela con pid no
    tendría esa propiedad: quedaría a medio escribir y alguien acabaría borrándolo a mano.
    """

    def __init__(self, raiz_operacional, instancia):
        self.directorio = os.path.join(raiz_operacional, SUBDIRECTORIO_VIVOS)
        self.instancia = instancia
        self.ruta = os.path.join(self.directorio, instancia + SUFIJO_VIVO)
        self.descriptor = None

    def abrir(self):
        """Declara viva a esta instancia. Idempotente."""
        if self.descriptor is not None:
            return self
        asegurar_directorio(self.directorio)
        try:
            descriptor = os.open(self.ruta, os.O_RDWR | os.O_CREAT, 0o644)
        except OSError as exc:
            raise traducir_error_de_sistema(
                exc, self.ruta, "abrir el testigo de vida") from exc
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            os.close(descriptor)
            if exc.errno in (errno.EACCES, errno.EAGAIN, errno.EWOULDBLOCK):
                # Otro proceso VIVO ya usa este nombre de instancia. Dejarlo pasar
                # permitiría que dos procesos se llamasen igual, y entonces el `titular`
                # del lease dejaría de identificar a uno solo: la vía rápida daría
                # «muerto» sobre un titular vivo.
                raise RuntimeInconsistente(
                    "ya hay un proceso vivo con el nombre de instancia `"
                    + self.instancia + "`; dos runtimes homónimos harían que `titular` "
                    "dejase de identificar a uno solo",
                    ruta=self.ruta, instancia=self.instancia,
                ) from exc
            raise traducir_error_de_sistema(
                exc, self.ruta, "bloquear el testigo de vida") from exc
        self.descriptor = descriptor
        return self

    def cerrar(self):
        """Retira el testigo. Idempotente: se llama desde `cerrar()` y desde `__exit__`.

        El ORDEN es parte del contrato: primero se BORRA el fichero y después se suelta el
        `flock`. Al revés habría un instante en que el testigo existe con el bloqueo libre,
        y ésa es exactamente la huella que `titular_muerto` lee como MUERTE.
        """
        if self.descriptor is None:
            return
        self._retirar_fichero()
        try:
            fcntl.flock(self.descriptor, fcntl.LOCK_UN)
        except OSError:
            # El núcleo suelta el `flock` igualmente al cerrar el descriptor; que el
            # desbloqueo explícito falle no deja el testigo tomado.
            pass
        try:
            os.close(self.descriptor)
        except OSError:
            # Un descriptor ya cerrado por otra vía no deja el testigo tomado: el núcleo
            # libera el `flock` con el último cierre, y aquí sólo se está apuntando la
            # contabilidad local. Fallar por esto convertiría un cierre limpio en un error.
            pass
        self.descriptor = None

    def _retirar_fichero(self):
        """Borra el testigo SÓLO si sigue siendo el nuestro, comparando el INODO.

        Una instancia homónima que arrancase mientras cerramos habría creado ya su propio
        fichero en la misma ruta. Borrar por nombre le quitaría el testigo estando viva, y
        entonces un tercero la leería como INDECIDIBLE cuando en realidad está trabajando.
        Comparar el inodo del descriptor que sostenemos con el que hoy tiene el nombre
        convierte «borro mi testigo» en algo que no puede alcanzar al de nadie más.
        """
        try:
            mio = os.fstat(self.descriptor).st_ino
            en_disco = os.stat(self.ruta).st_ino
        except OSError:
            # El fichero ya no está, o no se puede consultar. No hay nada que retirar, y la
            # ausencia es precisamente el estado al que se quería llegar.
            return
        if mio != en_disco:
            return
        try:
            os.remove(self.ruta)
        except OSError:
            # Otro proceso lo retiró entre el `stat` y el `remove`. El resultado es el
            # mismo —no queda testigo— y forzar un error aquí convertiría una carrera
            # benigna en un fallo de cierre.
            return

    def titular_muerto(self, titular):
        """`True` muerto · `False` vivo · `None` no se puede decidir desde esta máquina.

        Las tres lecturas, y sólo son válidas porque `cerrar()` retira el fichero:

            no existe                 → salió limpiamente, o es de otra máquina → `None`
            existe y `flock` TOMADO   → `False`, hay un proceso vivo con ese nombre
            existe y `flock` LIBRE    → `True`, MURIÓ sin poder limpiar

        `None` es una respuesta correcta y no un fallo: un titular de OTRA máquina no deja
        testigo aquí, y su ausencia no prueba nada. El §3 reserva ese caso a la regla de
        las observaciones, y quien recibe `None` NO puede robar el lease.
        """
        if titular == self.instancia:
            return False
        ruta = os.path.join(self.directorio, titular + SUFIJO_VIVO)
        if not os.path.exists(ruta):
            return None
        try:
            descriptor = os.open(ruta, os.O_RDWR)
        except OSError:
            return None
        try:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError as exc:
                if exc.errno in (errno.EACCES, errno.EAGAIN, errno.EWOULDBLOCK):
                    return False        # alguien lo sostiene: el titular está VIVO
                return None
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            except OSError:
                # El `finally` cierra el descriptor y con él se suelta el bloqueo. El
                # desbloqueo explícito es cortesía, no requisito: el veredicto ya está
                # tomado y no depende de él.
                pass
            return True                 # nadie lo sostiene: el titular está MUERTO
        finally:
            os.close(descriptor)

    def __enter__(self):
        return self.abrir()

    def __exit__(self, tipo, valor, traza):
        self.cerrar()
        return False
