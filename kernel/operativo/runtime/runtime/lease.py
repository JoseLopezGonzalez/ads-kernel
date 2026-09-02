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

RETIRADA · LA VÍA RÁPIDA POR `flock` YA NO EXISTE, y no se puede reponer
    Hubo aquí un atajo que el §3 contempla: el titular sostenía un `flock` sobre
    `estado/operacional/runtime/<instancia>.vivo`, y un aspirante que consiguiera ese
    `flock` concluía que el titular había MUERTO y reclamaba en el acto. Se retira entero
    tras la auditoría independiente, y conviene dejar escrito el ataque para que nadie lo
    reponga por comodidad dentro de seis meses.

    EL ATAQUE, ejecutado con `runtime-A` VIVO y trabajando:

        A vivo? pid 1719412 · poll = None    testigo de A presente: True
        >>> testigo de runtime-A SUSTITUIDO. A sigue vivo: True
        reclamar de B  exit= 0   → {"titular": "runtime-B", "epoca": 2}
        >>> B despacha pq-ok con A todavía ejecutándolo → "completado"
        integridad del estado: VERDE

    No hizo falta matar a nadie: bastó **BORRAR el fichero y crear otro en su sitio**. El
    testigo nuevo existe y su `flock` está libre, que es exactamente la huella que el
    atajo leía como muerte. La afirmación «sólo un final abrupto deja esa combinación» era
    FALSA.

    POR QUÉ NO SE ARREGLA AUTENTICANDO EL TESTIGO. El plano operacional es, por definición
    de `g.1`, **reconstruible y no durable**: está fuera de la huella, fuera de la admisión
    y fuera del versionado. Nada de lo que vive ahí está protegido contra ser sustituido, y
    no hay forma de autenticarlo DESDE DENTRO: cualquier secreto que el lease pudiera
    comparar contra el testigo tendría que estar escrito en el estado canónico, que es
    legible, y por tanto sería falsificable por quien fabrica el testigo. **Una credencial
    que cualquiera puede fabricar no puede decidir autoridad.**

    Y es peor que tocar el estado: editar el lease a mano da `ESTADO_CORRUPTO` y se ve.
    Esto dejaba la integridad VERDE y un `runtime.lease.reclamado` de aspecto legítimo en
    el diario, es decir, un robo con papeles en regla.

    LO QUE QUEDA, y es una sola puerta: `PACIENCIA` observaciones consecutivas sin que el
    latido avance. Cada observación es una transición DURABLE, escrita por el aspirante,
    auditable y sujeta a la misma integridad que todo lo demás; falsificarla exige
    falsificar el estado canónico, que es justamente lo que sí se detecta. El precio es que
    recuperarse de una caída real es más lento —hay que observar `PACIENCIA` veces en vez
    de reclamar al instante—, y es el precio correcto: la alternativa era un lease que no
    protege nada.

    `diagnostico_del_testigo()` sobrevive con otro nombre y SÓLO como diagnóstico. Ninguna
    ruta de decisión lo consulta, y una prueba lo comprueba contra el árbol sintáctico.
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


# ------------------------------------------------- testigo de vida (SÓLO diagnóstico)
class TestigoDeVida:
    """`flock` sobre `estado/operacional/runtime/<instancia>.vivo`. NO es estado durable.

    Hace HOY dos cosas, y ninguna es decidir autoridad:

      1 · IMPIDE DOS PROCESOS HOMÓNIMOS. `abrir()` falla si otro proceso vivo ya usa este
          nombre de instancia. Eso sí es una garantía real, porque se apoya en un `flock`
          que este proceso sostiene mientras vive: nadie puede hacer que un bloqueo tomado
          parezca libre. Importa porque `titular` es quien firma cada observación y cada
          latido, y dos runtimes homónimos lo volverían ambiguo.
      2 · DA DIAGNÓSTICO. `diagnostico_del_testigo()` describe lo que hay en el plano
          operacional, y se publica nombrándolo como pista NO AUTENTICADA.

    Lo que YA NO hace es decidir que un titular murió. Ese atajo se retiró tras la
    auditoría: el fichero es sustituible por cualquiera y con él se robaba el lease de un
    titular VIVO. El encabezado del módulo guarda el ataque.

    Nótese la asimetría, que es la que hace legítimo (1) e ilegítimo lo retirado: un
    bloqueo TOMADO prueba que hay alguien: nadie puede falsificar la presencia. Un bloqueo
    LIBRE no prueba nada: cualquiera puede fabricar la ausencia.
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
                # del lease dejaría de identificar a uno solo, y `titular` es lo que
                # nombra al autor de cada observación y de cada latido.
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
        y ésa era exactamente la huella que la vía rápida —hoy retirada— leía como
        MUERTE. El borrado sigue yendo primero: `diagnostico_del_testigo` la publica, y una
        pista de diagnóstico que miente confunde igual aunque no decida nada.
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

    def diagnostico_del_testigo(self, titular):
        """DIAGNÓSTICO, y NADA MÁS. No decide nada y ninguna ruta de decisión lo llama.

        Devuelve `propio` · `ausente` · `tomado` · `libre` · `indeterminado`, que describen
        lo que hay en el plano operacional y no lo que le ocurre al titular. La diferencia
        importa: `libre` NO significa «murió». Significa «hay un fichero con ese nombre y
        nadie lo tiene bloqueado», y eso lo produce igual una muerte que **un tercero que
        borra el fichero y crea otro en su sitio**, que es el ataque que retiró la vía
        rápida (ver el encabezado de este módulo).

        Sirve para que un operador vea qué hay, y para que la CLI lo publique nombrándolo
        por lo que es: una pista NO AUTENTICADA. Quien lo lea no puede concluir autoridad.
        """
        if titular == self.instancia:
            return "propio"
        ruta = os.path.join(self.directorio, titular + SUFIJO_VIVO)
        if not os.path.exists(ruta):
            return "ausente"
        try:
            descriptor = os.open(ruta, os.O_RDWR)
        except OSError:
            return "indeterminado"
        try:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError as exc:
                if exc.errno in (errno.EACCES, errno.EAGAIN, errno.EWOULDBLOCK):
                    return "tomado"
                return "indeterminado"
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            except OSError:
                # El `finally` cierra el descriptor y con él se suelta el bloqueo. El
                # desbloqueo explícito es cortesía, no requisito.
                pass
            return "libre"
        finally:
            os.close(descriptor)

    def __enter__(self):
        return self.abrir()

    def __exit__(self, tipo, valor, traza):
        self.cerrar()
        return False
