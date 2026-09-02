#!/usr/bin/env python3
"""bloqueo — serialización de escritores dentro de una máquina (`g.6`).

`I-g4` dice que hay UN SOLO ejecutor de mutaciones canónicas. En una máquina eso se
consigue con un bloqueo exclusivo, y aquí es `fcntl.flock` sobre `operacional/escritor.lock`.

DECISIÓN · `flock` y no un fichero-centinela con el pid dentro
    Alternativas: (a) crear `escritor.lock` con `O_EXCL` y borrarlo al terminar; (b) escribir
    un centinela con el pid y comprobar si ese pid vive; (c) `fcntl.flock`.
    Se elige (c). (a) y (b) comparten el defecto que arruina cualquier bloqueo casero: si el
    proceso MUERE —y el §10 existe precisamente para matarlo— el centinela queda ahí para
    siempre y el almacén se vuelve inescribible hasta que una persona lo borra a mano. Peor
    aún, la reclamación por «ese pid ya no vive» es insegura: los pid se reciclan, y el
    reciclado autorizaría a dos escritores a la vez, rompiendo `I-g4` justo en el caso más
    difícil de reproducir. Con `flock` el bloqueo lo mantiene el NÚCLEO asociado al
    descriptor abierto: cuando el proceso muere, por la causa que sea, el núcleo lo suelta.
    Un bloqueo abandonado se reclama SOLO, sin intervención y sin heurística.

DECISIÓN · el fichero de metadatos es INFORMATIVO y NO decide
    Se escribe `escritor.lock.meta` con el pid del tenedor, y se borra al liberar. No se
    consulta jamás para decidir si se puede entrar: quien decide es `flock`. Existe sólo
    para que una persona que mira el directorio sepa a quién preguntar. Que lleve un pid no
    viola `I-g3` porque vive en `operacional/`, que `g.1` declara NO DURABLE y que el
    `.gitignore` del almacén excluye: nunca entra en `cid_raiz` ni en la rama canónica.

DECISIÓN · `LOCK_NB` + reintentos explícitos, y no `flock` bloqueante
    Un `flock` bloqueante esperaría indefinidamente, y `g.6` pide lo contrario: que el
    conflicto se DETECTE y que agotar los reintentos deje las órdenes intactas y produzca el
    registro de `g.9`. Con `LOCK_NB` el conflicto es un valor de retorno, contable y
    convertible en `ReintentosAgotados`. La espera entre intentos es FIJA y corta: un
    retroceso exponencial con aleatoriedad haría la evidencia no reproducible, contra `I-g3`.

DECISIÓN · dos bloqueos, no uno
    `escritor.lock` serializa las mutaciones CANÓNICAS. `registro.lock` serializa el
    registro operativo auxiliar. Tienen que ser dos: el registro auxiliar se escribe
    justamente cuando NO se ha podido tomar el bloqueo de escritor, y con un único bloqueo
    ese camino sería imposible de recorrer. Además son estructuras separadas por `I-g7`, y
    darles el mismo bloqueo las volvería a acoplar por la puerta de atrás.
"""
from __future__ import annotations

import errno
import fcntl
import os
import time

from .errores import BloqueoNoAdquirido, EscritorConcurrente
from .rutas import asegurar_directorio, traducir_error_de_sistema

ESPERA_ENTRE_INTENTOS = 0.05


class BloqueoExclusivo:
    """Un `flock` exclusivo sobre un fichero de `operacional/`.

    Se usa como gestor de contexto. `liberar()` es idempotente porque el mismo objeto puede
    liberarse desde el `finally` del protocolo y desde `Almacen.cerrar()`.
    """

    def __init__(self, ruta, etiqueta="escritor"):
        self.ruta = ruta
        self.etiqueta = etiqueta
        self.descriptor = None
        self.intentos_realizados = 0

    # -------------------------------------------------------------- adquisición
    def adquirir(self, intentos=1, espera=ESPERA_ENTRE_INTENTOS):
        """Toma el bloqueo, con `intentos` pasadas no bloqueantes. Nunca espera indefinido."""
        if self.descriptor is not None:
            return self
        if intentos < 1:
            raise BloqueoNoAdquirido(
                "el número de intentos debe ser al menos 1", ruta=self.ruta
            )
        asegurar_directorio(os.path.dirname(self.ruta))
        try:
            descriptor = os.open(self.ruta, os.O_RDWR | os.O_CREAT, 0o644)
        except OSError as exc:
            # Un almacén de sólo lectura o sin permiso sobre `operacional/` no es un
            # conflicto de escritores: es `PermisoInsuficiente`, y el llamador no debe
            # reintentar ni abrir un registro de reconciliación por ello.
            raise traducir_error_de_sistema(exc, self.ruta, "abrir el fichero de bloqueo") from exc

        ultimo = None
        for numero in range(1, intentos + 1):
            self.intentos_realizados = numero
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError as exc:
                if exc.errno not in (errno.EACCES, errno.EAGAIN, errno.EWOULDBLOCK):
                    os.close(descriptor)
                    raise traducir_error_de_sistema(exc, self.ruta, "bloquear") from exc
                ultimo = exc
                if numero < intentos:
                    # Espera FIJA: reproducible. No hay retroceso exponencial ni jitter,
                    # porque la evidencia de concurrencia tiene que dar los mismos bytes.
                    time.sleep(espera)
                continue
            self.descriptor = descriptor
            self._anotar_metadatos()
            return self

        os.close(descriptor)
        raise EscritorConcurrente(
            "otro escritor mantiene el bloqueo exclusivo tras " + str(intentos)
            + " intento(s); el estado canónico NO se ha tocado",
            ruta=self.ruta,
            intentos=intentos,
            motivo=errno.errorcode.get(ultimo.errno, "EWOULDBLOCK") if ultimo else "EWOULDBLOCK",
        )

    # ---------------------------------------------------------------- metadatos
    def _anotar_metadatos(self):
        """Deja constancia legible de quién tiene el bloqueo. NO decide nada."""
        try:
            with open(self.ruta + ".meta", "w", encoding="utf-8") as fichero:
                fichero.write('{"etiqueta":"' + self.etiqueta + '","pid":' + str(os.getpid()) + "}\n")
        except OSError:
            # Que no se pueda anotar el metadato NO invalida el bloqueo: el bloqueo lo
            # mantiene el núcleo. Fallar aquí convertiría un adorno en un requisito, y un
            # almacén con `operacional/` casi lleno dejaría de poder escribir por nada.
            pass

    def _limpiar_metadatos(self):
        try:
            os.remove(self.ruta + ".meta")
        except FileNotFoundError:
            pass
        except OSError:
            pass

    # ---------------------------------------------------------------- liberación
    def liberar(self):
        if self.descriptor is None:
            return
        descriptor, self.descriptor = self.descriptor, None
        self._limpiar_metadatos()
        try:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        except OSError:
            # Cerrar el descriptor libera el `flock` igualmente. No se enmascara nada
            # relevante: el desbloqueo explícito es una cortesía, el cierre es la garantía.
            pass
        finally:
            os.close(descriptor)

    def tomado(self):
        return self.descriptor is not None

    def __enter__(self):
        if self.descriptor is None:
            self.adquirir()
        return self

    def __exit__(self, tipo, valor, traza):
        self.liberar()
        return False


def bloqueo_abandonado_reclamable(ruta):
    """¿Está libre un bloqueo cuyo tenedor murió? Se comprueba INTENTÁNDOLO.

    No se mira el `.meta` ni se pregunta por el pid: la única respuesta fiable es la del
    núcleo. Esta función existe para que una prueba pueda afirmar «el bloqueo abandonado se
    reclama solo» sin inventarse una heurística que el motor no usa.
    """
    prueba = BloqueoExclusivo(ruta, etiqueta="sonda")
    try:
        prueba.adquirir(intentos=1)
    except EscritorConcurrente:
        return False
    prueba.liberar()
    return True
