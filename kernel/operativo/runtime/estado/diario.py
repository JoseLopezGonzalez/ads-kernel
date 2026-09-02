#!/usr/bin/env python3
"""diario — el DIARIO CANÓNICO: la secuencia de eventos que EXPLICA el estado (`g.7`).

Es uno de los TRES componentes durables de `g.1`, y no es ninguno de los otros dos. Aquí
importa decir en qué se diferencia MATERIALMENTE, porque `I-g7` prohíbe colapsarlos:

    ESTADO CANÓNICO      JSON indentado, un fichero por entidad, SOBRESCRIBIBLE por
                         `os.replace`, sin orden entre entidades, sin cadena de hash.
                         Responde «¿qué es verdad ahora?» y se lee sin reproyectar nada.

    DIARIO CANÓNICO      JSONL append-only, UNA sola secuencia total, encadenado por hash,
                         NUNCA se reescribe una línea. Responde «¿cómo llegó a serlo?».
                         No es sede del estado: borrar el diario no cambia ni un dato del
                         estado canónico, y borrar un objeto canónico no cambia ni una
                         línea del diario. Esa independencia es la prueba de `I-g7`.

    REGISTRO AUXILIAR    otro fichero, otra cadena, otro bloqueo, otro vocabulario
    (reconciliacion.py)  (`apertura`/`resolucion` frente a `transicion.*`) y otra
                         semántica: lo que el runtime NO PUDO hacer.

DECISIÓN · cadena de hash sobre el diario, y no un simple contador
    Alternativas: (a) confiar en `secuencia`; (b) encadenar cada evento con la huella del
    anterior.
    Se elige (b). Con (a), quitar una línea del medio y renumerar deja un diario
    perfectamente coherente, y entonces `g.13` —«todo cambio del estado canónico es
    explicable por el diario»— se puede satisfacer borrando lo inexplicable. Con la cadena,
    retirar, insertar o editar cualquier línea rompe `previo` en la siguiente y el fallo es
    cerrado. Se conserva ADEMÁS `secuencia`, porque el «momento» que `g.9` exige registrar
    es el MOMENTO LÓGICO —el número de secuencia—, y no una hora de pared que `I-g3` veda.

DECISIÓN · el anexado es UN SOLO `os.write` sobre un descriptor `O_APPEND`
    Alternativas: (a) `open(..., "a")` de `io`, con su búfer; (b) descriptor crudo en
    `O_APPEND` y una única llamada al sistema por línea.
    Se elige (b). Con (a), el búfer de `io` puede partir la línea en dos escrituras y un
    corte entre ambas deja media línea y media verdad. Con `O_APPEND` el desplazamiento y
    la escritura son atómicos respecto a otros escritores, y una sola llamada con la línea
    entera hace que el desgarro sólo sea posible por debajo, en el medio físico.

DECISIÓN · una COLA DESGARRADA se repara; un hueco INTERMEDIO es corrupción
    Un corte durante el anexado puede dejar una última línea incompleta. Alternativas:
    (a) declarar corrupto el diario y exigir intervención; (b) tratar la línea incompleta
    como un evento que NUNCA llegó a ser durable, descartarla bajo el bloqueo de escritor y
    seguir.
    Se elige (b), y sólo para la ÚLTIMA línea. Con (a) cualquier corte inyectado por el §10
    dejaría el almacén irrecuperable, y `g.8` exige justo lo contrario: que lo incompleto se
    detecte y se termine o se revierta. Un evento cuyos bytes no llegaron enteros al medio
    no es durable por definición de `g.4`, así que descartarlo no pierde ninguna verdad: la
    transacción que lo iba a explicar queda sin cerrar y la recuperación la ve. En cambio
    una línea rota EN MEDIO, o una huella que no casa, es manipulación o daño del medio, y
    ahí el fallo es CERRADO: `DiarioCorrupto`, sin tocar el estado canónico.
    `verificar_integridad` NO repara: si ve la cola desgarrada, la denuncia.
"""
from __future__ import annotations

import os

from . import fallos
from .errores import DiarioCorrupto
from .rutas import asegurar_directorio, traducir_error_de_sistema
from .serializacion import (
    ESQUEMA,
    cid_de_objeto,
    comprobar_esquema,
    deserializar,
    serializar_compacto,
)

# Los tipos que el §2.4 declara obligatorios. La tupla es el censo: `anexar` rechaza
# cualquier otro, para que no aparezca un vocabulario paralelo por descuido.
TIPOS = (
    "almacen.inicializado",
    "transicion.abierta",
    "transicion.preparada",
    "transicion.confirmada",
    "transicion.revertida",
    "transicion.marcada",
    "reconciliacion.abierta",
    "reconciliacion.resuelta",
    "migracion.aplicada",
)

TERMINALES = ("transicion.confirmada", "transicion.revertida", "transicion.marcada")

CLAVE_HUELLA = "huella"
CLAVE_PREVIO = "previo"


def calcular_huella(evento):
    """`huella` = `cid` de la forma canónica del evento SIN el campo `huella` (§2.4)."""
    cuerpo = {clave: evento[clave] for clave in evento if clave != CLAVE_HUELLA}
    return cid_de_objeto(cuerpo)


class Diario:
    """El diario canónico de un almacén. Append-only y verificable de principio a fin."""

    def __init__(self, ruta):
        self.ruta = ruta

    # ------------------------------------------------------------------ lectura
    def existe(self):
        return os.path.exists(self.ruta)

    def crear(self):
        """Crea el fichero vacío y sincroniza su directorio: el NOMBRE debe ser durable."""
        asegurar_directorio(os.path.dirname(self.ruta))
        if not os.path.exists(self.ruta):
            try:
                descriptor = os.open(self.ruta, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
            except FileExistsError:
                return
            except OSError as exc:
                raise traducir_error_de_sistema(exc, self.ruta, "crear el diario") from exc
            os.fsync(descriptor)
            os.close(descriptor)

    def _bytes(self):
        if not os.path.exists(self.ruta):
            return b""
        try:
            with open(self.ruta, "rb") as fichero:
                return fichero.read()
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "leer el diario") from exc

    def _lineas(self):
        """Devuelve `(lineas_completas, bytes_de_cola_desgarrada)`.

        Una línea es completa cuando termina en `\\n`. Lo que quede detrás del último salto
        es, por construcción, un anexado que no llegó a terminar.
        """
        datos = self._bytes()
        if not datos:
            return [], b""
        corte = datos.rfind(b"\n")
        if corte == -1:
            return [], datos
        completas = datos[: corte + 1].split(b"\n")[:-1]
        return completas, datos[corte + 1:]

    def cola_desgarrada(self):
        return bool(self._lineas()[1])

    def instantanea(self, *, verificar=True, tolerar_cola=False):
        """UNA sola lectura del diario. Todo lo que se deduzca sale de ELLA y de nada más.

        Defecto que previene, y no es teórico: el diario es APPEND-ONLY y otro proceso
        puede estar anexando justo ahora. Dos llamadas seguidas a `eventos()` devuelven,
        legítimamente, dos listas distintas. Cruzar los resultados de las dos —recorrer una
        y buscar en la otra— produce una conclusión que no corresponde a ningún estado que
        el diario haya tenido nunca, y en el mejor de los casos revienta con un `KeyError`
        crudo; en el peor, decide que no hay ventana cuando la hay.

        La regla es: quien vaya a deducir algo del diario pide UNA instantánea y trabaja
        sobre ella. Un `read()` del fichero entero es un corte coherente por construcción:
        lo que llegue después de ese `read()` no aparece a medias, aparece en la siguiente
        instantánea. Que la conclusión sea de hace un instante es aceptable —`g.3` dice
        expresamente que NO se afirma aislamiento de lecturas—; que sea de dos instantes a
        la vez, no lo es.

        Devuelve `(eventos, bytes_de_cola_desgarrada)`.
        """
        completas, cola = self._lineas()
        if cola and not tolerar_cola:
            raise DiarioCorrupto(
                "el diario termina en una línea incompleta de " + str(len(cola))
                + " byte(s): un anexado quedó a medias. `recuperar()` la descarta bajo el "
                "bloqueo de escritor; leer no la descarta nunca",
                ruta=self.ruta,
                bytes_sueltos=len(cola),
            )
        return self._interpretar(completas, verificar), cola

    def _interpretar(self, completas, verificar):
        """Líneas crudas → eventos, con la cadena comprobada eslabón a eslabón."""
        eventos = []
        anterior = None
        for indice, linea in enumerate(completas):
            evento = deserializar(linea, ruta=self.ruta, error=DiarioCorrupto)
            if not isinstance(evento, dict):
                raise DiarioCorrupto(
                    "la línea " + str(indice + 1) + " del diario no es un objeto JSON",
                    ruta=self.ruta,
                )
            comprobar_esquema(evento, ruta=self.ruta, error=DiarioCorrupto)
            if verificar:
                self._verificar_eslabon(evento, anterior, indice)
            eventos.append(evento)
            anterior = evento
        return eventos

    def eventos(self, desde=0, verificar=True, tolerar_cola=False):
        """Los eventos del diario, verificados de principio a fin.

        Es `instantanea()` para quien sólo quiere la lista. Quien vaya a CRUZAR dos
        deducciones sobre el diario debe pedir la instantánea y pasarla, no llamar aquí
        dos veces.

        `verificar=False` sólo lo usa la propia verificación de integridad para poder
        describir el daño en vez de detenerse en el primer síntoma.
        """
        eventos, _ = self.instantanea(verificar=verificar, tolerar_cola=tolerar_cola)
        if desde:
            eventos = [evento for evento in eventos if evento.get("secuencia", 0) >= desde]
        return eventos

    def _verificar_eslabon(self, evento, anterior, indice):
        esperada = indice + 1
        if evento.get("secuencia") != esperada:
            raise DiarioCorrupto(
                "la secuencia del diario salta: se esperaba " + str(esperada)
                + " y se lee " + str(evento.get("secuencia")),
                ruta=self.ruta,
                posicion=esperada,
            )
        if evento.get("tipo") not in TIPOS:
            raise DiarioCorrupto(
                "tipo de evento no declarado en el §2.4: " + repr(evento.get("tipo")),
                ruta=self.ruta,
                posicion=esperada,
            )
        previo_esperado = anterior[CLAVE_HUELLA] if anterior is not None else None
        if evento.get(CLAVE_PREVIO) != previo_esperado:
            raise DiarioCorrupto(
                "la cadena de hash se rompe en la secuencia " + str(esperada)
                + ": `previo` no es la huella del evento anterior. Falta una línea, se "
                "insertó una, o se editó el diario a mano",
                ruta=self.ruta,
                posicion=esperada,
            )
        huella = calcular_huella(evento)
        if evento.get(CLAVE_HUELLA) != huella:
            raise DiarioCorrupto(
                "la huella del evento " + str(esperada) + " no casa con su contenido: el "
                "evento fue editado después de escribirse",
                ruta=self.ruta,
                posicion=esperada,
                esperada=huella,
                encontrada=evento.get(CLAVE_HUELLA),
            )

    def exigir_coherente(self, hasta_secuencia=None, *, tolerar_cola=False):
        """Fallo CERRADO al LEER si el diario está truncado o roto (`g.5`).

        Distingue DOS daños que se parecen en el fichero y no se parecen en nada más:

          ÚLTIMA LÍNEA TORCIDA · un corte a mitad de `append` deja bytes sin su `\\n`. El
            evento no llegó entero al medio, así que por `g.4` nunca fue durable, y la
            transacción que iba a explicar queda sin cerrar. Es una VENTANA RECUPERABLE:
            `recuperar()`, que tiene el bloqueo de escritor, descarta la cola y cierra la
            ventana. Por eso se tolera cuando se abre con `recuperar=True`.
            Con `recuperar=False` NO se tolera, y la razón es que un lector que no puede
            reparar tampoco puede DISTINGUIR el corte de una truncación deliberada: dar
            por buena la parte legible es exactamente cómo se pierde una transición sin
            que nadie se entere.

          DIARIO QUE NO ALCANZA LA REVISIÓN PUBLICADA · `REVISION.json` declara el
            `diario_secuencia` del evento que la explica. Si el diario ya no llega hasta
            ahí, se han perdido eventos COMPLETOS: hay estado publicado sin diario que lo
            explique, contra `g.13`, y ninguna recuperación puede reconstruirlo sin
            inventar, que es lo que `I-g2` prohíbe. Eso es corrupción SIEMPRE, se abra
            como se abra, y no hay rama de `g.8` que lo arregle.
        """
        completas, cola = self._lineas()
        if cola and not tolerar_cola:
            raise DiarioCorrupto(
                "el diario termina en una línea incompleta de " + str(len(cola))
                + " byte(s); abrir con `recuperar=True` cierra esa ventana, leer no la "
                "cierra nunca",
                ruta=self.ruta, bytes_sueltos=len(cola),
            )
        # Aquí NO se verifica la cadena de huellas, y es deliberado. Esta comprobación es
        # ESTRUCTURAL —¿está el fichero entero?— y se paga en cada apertura, incluidas las
        # de sólo lectura. La cadena responde a otra pregunta —¿lo escribió el motor o lo
        # editó alguien?— y la contestan quienes de verdad leen los eventos: `eventos()`,
        # `verificar_integridad()`, `auditar()`, `recuperar()` y `aplicar()`. Separarlas
        # evita que abrir para mirar la revisión tenga que reconstruir el diario entero, y
        # ninguna corrupción se escapa: nadie usa un evento sin haberlo verificado antes.
        if hasta_secuencia is not None and len(completas) < hasta_secuencia:
            raise DiarioCorrupto(
                "la revisión publicada se explica por el evento " + str(hasta_secuencia)
                + " y el diario sólo llega al " + str(len(completas)) + ": se han perdido "
                "eventos completos, y hay estado publicado que ya nada explica",
                ruta=self.ruta,
                declarada=hasta_secuencia, encontrada=len(completas),
            )
        return len(completas)

    def ultimo(self):
        eventos = self.eventos(tolerar_cola=True)
        return eventos[-1] if eventos else None

    def siguiente_secuencia(self):
        """La secuencia que llevará el próximo evento. Empieza en 1, como el §2.5."""
        completas, _ = self._lineas()
        return len(completas) + 1

    # ----------------------------------------------------------------- escritura
    def reparar_cola(self):
        """Descarta un anexado desgarrado. Sólo se llama con el bloqueo de escritor tomado.

        Devuelve los bytes descartados. Es idempotente: sin cola desgarrada no hace nada y
        no toca el fichero, que es lo que `recuperar()` necesita para poder invocarse N
        veces sin efectos.
        """
        completas, cola = self._lineas()
        if not cola:
            return 0
        longitud = sum(len(linea) + 1 for linea in completas)
        try:
            descriptor = os.open(self.ruta, os.O_WRONLY)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "reparar la cola del diario") from exc
        try:
            os.ftruncate(descriptor, longitud)
            os.fsync(descriptor)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "truncar el diario") from exc
        finally:
            os.close(descriptor)
        return len(cola)

    def anexar(self, tipo, **campos):
        """Añade un evento encadenado y lo hace DURABLE antes de devolver.

        El punto `durante-el-diario` cae entre la escritura y el `fsync`: es la ventana en
        la que el evento está en la caché de página y no en el medio. Un corte ahí es el
        caso interesante, porque produce exactamente la cola desgarrada que `reparar_cola`
        tiene que saber descartar.
        """
        if tipo not in TIPOS:
            raise DiarioCorrupto(
                "tipo de evento no declarado en el §2.4: " + repr(tipo), ruta=self.ruta
            )
        completas, cola = self._lineas()
        if cola:
            raise DiarioCorrupto(
                "no se anexa sobre un diario con la cola desgarrada: primero `recuperar()`",
                ruta=self.ruta,
            )
        previo = None
        if completas:
            ultimo = deserializar(completas[-1], ruta=self.ruta, error=DiarioCorrupto)
            previo = ultimo.get(CLAVE_HUELLA)

        evento = {"esquema": ESQUEMA, "secuencia": len(completas) + 1, "tipo": tipo}
        evento.update(campos)
        evento[CLAVE_PREVIO] = previo
        evento[CLAVE_HUELLA] = calcular_huella(evento)

        linea = serializar_compacto(evento) + b"\n"
        asegurar_directorio(os.path.dirname(self.ruta))
        try:
            descriptor = os.open(self.ruta, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "abrir el diario") from exc
        try:
            escritos = os.write(descriptor, linea)
            if escritos != len(linea):
                # Con `O_APPEND` una escritura corta de un búfer pequeño es anómala. No se
                # completa el resto en un segundo `write`: eso mezclaría la línea con la de
                # otro escritor. Se denuncia, y la cola desgarrada la limpia `recuperar()`.
                raise DiarioCorrupto(
                    "el anexado al diario quedó corto: " + str(escritos) + " de "
                    + str(len(linea)) + " bytes",
                    ruta=self.ruta,
                )
            fallos.punto("durante-el-diario")
            os.fsync(descriptor)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "anexar al diario") from exc
        finally:
            os.close(descriptor)
        return evento

    # -------------------------------------------------------------- agregaciones
    def por_transaccion(self, eventos=None):
        """Mapa `transaccion -> [eventos]`, en orden. Base de la detección de la ventana.

        Sin `eventos` lee el diario una vez. Si el llamador va a usar el mapa JUNTO a otro
        recorrido, tiene que pasar su propia instantánea: dos lecturas producen dos mapas y
        cruzarlos es el defecto que `instantanea()` existe para impedir.
        """
        if eventos is None:
            eventos, _ = self.instantanea(tolerar_cola=True)
        agrupados = {}
        for evento in eventos:
            transaccion = evento.get("transaccion")
            if transaccion is None:
                continue
            agrupados.setdefault(transaccion, []).append(evento)
        return agrupados

    def transaccion_sin_cerrar(self, eventos=None):
        """La última transacción abierta o preparada SIN evento terminal, o `None`.

        Se recorre de atrás hacia delante porque el §3 habla de «la última». Como el
        protocolo sólo permite una transacción viva a la vez —el bloqueo de escritor lo
        garantiza—, en la práctica hay como mucho una; recorrer entero y quedarse con la
        última hace que un almacén con historia anómala se comporte igual de bien.

        UNA sola lectura, y las dos deducciones —la agrupación y el recorrido— salen de
        ella. Antes eran dos: se agrupaba sobre una lectura y se recorría sobre otra, y con
        varios escritores anexando en paralelo la transacción elegida en el recorrido podía
        no existir en la agrupación. Eso reventaba con un `KeyError` CRUDO, sin código
        estable, en la ruta de recuperación al abrir —la que más falta hace que aguante— y
        volcando además un traceback con rutas absolutas de la máquina. El §0 no admite
        ninguna de las tres cosas.
        """
        if eventos is None:
            # `tolerar_cola=True` a propósito: un anexado a medias ES una ventana, y
            # preguntar si la hay tiene que poder responderse justo cuando la hay.
            eventos, _ = self.instantanea(tolerar_cola=True)
        agrupados = self.por_transaccion(eventos)
        candidata = None
        for evento in eventos:
            transaccion = evento.get("transaccion")
            if transaccion is None or evento.get("tipo") not in (
                "transicion.abierta", "transicion.preparada"
            ):
                continue
            tipos = {suceso.get("tipo") for suceso in agrupados.get(transaccion, ())}
            if tipos.isdisjoint(TERMINALES):
                candidata = transaccion
        if candidata is None:
            return None
        propios = agrupados.get(candidata)
        if not propios:
            # Imposible con una instantánea coherente: `candidata` sale del mismo recorrido
            # que alimentó la agrupación. Sólo se llega aquí si el llamador pasó una lista
            # que no es una lectura coherente del diario. Se falla CERRADO y TIPADO, con
            # código estable, en vez de dejar escapar el `KeyError` que el §0 prohíbe.
            raise DiarioCorrupto(
                "la transacción " + str(candidata) + " aparece al recorrer el diario y no "
                "al agruparlo: la lista de eventos recibida no es una lectura coherente. "
                "Pida una `instantanea()` y trabaje sobre ella",
                ruta=self.ruta, transaccion=candidata,
            )
        return candidata, propios
