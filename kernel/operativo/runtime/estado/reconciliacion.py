#!/usr/bin/env python3
"""reconciliacion — el REGISTRO OPERATIVO AUXILIAR de `g.9`.

Es el TERCER componente durable de `g.1`, y `g.9` lo dice sin margen: **no es estado
canónico y no es diario canónico**. Colapsarlo en cualquiera de los dos rompe `I-g7`.
Este módulo mantiene esa separación de forma MATERIAL, no nominal:

    otro FICHERO          `reconciliacion/REGISTRO.jsonl`, en su propio directorio
    otro BLOQUEO          `operacional/registro.lock`, distinto del de escritor
    otro VOCABULARIO      `apertura` / `resolucion`, no `transicion.*`
    otro CONTENIDO        PRODUCTO, REPOSITORIO, ITEM, INTENTO, CAUSA y MOMENTO —campos que
                          el diario no tiene y que el estado canónico no tiene—
    otra CADENA de hash   independiente de la del diario: romper una no rompe la otra
    otra SEMÁNTICA        registra lo que el runtime NO PUDO hacer. El diario registra lo
                          que SÍ hizo. Ninguno se deriva del otro: de una apertura no se
                          puede reconstruir ningún estado, y de ninguna secuencia de
                          eventos del diario se puede reconstruir una apertura

DECISIÓN · bloqueo propio, y por qué es OBLIGATORIO que sea propio
    El registro se escribe justamente cuando se han AGOTADO los reintentos de tomar el
    bloqueo de escritor. Con un único bloqueo, ese camino —el único que `g.6` obliga a
    recorrer— sería inalcanzable: no se podría dejar constancia precisamente del fallo que
    hay que dejar constancia. Con bloqueo propio, el escritor derrotado escribe su apertura
    mientras el ganador sigue mutando el estado canónico, y ninguno de los dos espera al
    otro. Es también la razón por la que este fichero NO puede vivir dentro del diario.

DECISIÓN · `reconciliacion_pendiente` se DEDUCE, no se almacena
    Alternativas: (a) un campo `estado: abierta|resuelta` que se reescribe; (b) deducirlo
    de «hay apertura y no hay resolución».
    Se elige (b). (a) exigiría REESCRIBIR una línea ya escrita, y `g.9` manda append-only.
    Además un campo mutable puede quedar desincronizado con los hechos, y entonces la
    deducción dejaría de ser INEQUÍVOCA, que es la palabra que usa `g.9`. Con (b) el
    fichero es la única fuente y no hay estado derivado que mantener.

DECISIÓN · el MOMENTO es lógico, nunca reloj
    `g.9` exige identificar el MOMENTO. `I-g3` prohíbe la hora de pared en un artefacto
    durable, y esto es durable. El momento se registra como `{diario_secuencia, revision}`:
    dos coordenadas del propio sistema, reproducibles, que sitúan la apertura en la
    historia con más precisión que un reloj y sin destruir el determinismo.

DECISIÓN · CABEZA DURABLE, porque una cadena de hash no protege su propia cola
    El defecto que cierra, y era real: la cadena detecta que se retire, se inserte o se
    edite cualquier línea que NO sea la última, porque rompe el `previo` de la siguiente.
    Borrar la ÚLTIMA deja un prefijo perfectamente encadenado y **indistinguible de un
    registro que nunca tuvo esa línea**. Con eso, una reconciliación pendiente se retiraba
    borrando un renglón, sin la transición explícita que `g.9` exige y sin que `verificar`
    ni `auditar` protestaran: `G-A6` incumplido.

    El contraste con el diario NO bastaba, y conviene decir por qué se creyó que sí. Sólo
    funciona para las aperturas que tienen contraparte en el diario, y la apertura por
    REINTENTOS AGOTADOS —la única que produce el camino real de `g.6`— no la tiene ni puede
    tenerla: quien agota los reintentos no obtuvo el cerrojo del escritor, y anotar en el
    diario sería tocar estado canónico, que `g.6` le prohíbe expresamente. Es decir: el
    contraste cubría justo el caso que no importaba.

    Alternativas consideradas:
      (a) anotar toda apertura en el diario · descartada: rompe `g.6`, que prohíbe tocar el
          estado canónico en ese camino, y rompe `I-g7` metiendo el registro en el diario.
      (b) anclar la huella del registro en `REVISION.json` · descartada: haría que el estado
          canónico dependiera del registro auxiliar, que es exactamente el colapso que
          `I-g7` prohíbe, y además exigiría el cerrojo del escritor que no se tiene.
      (c) CABEZA DURABLE separada del propio log · ELEGIDA.

    `reconciliacion/CABEZA.json` guarda la última secuencia y su huella, se escribe de forma
    ATÓMICA tras cada anexado y bajo el bloqueo PROPIO del registro. Borrar una línea deja
    entonces una cabeza que afirma más líneas de las que hay, y eso es detectable SIEMPRE,
    sin el diario y sin el cerrojo del escritor. La cabeza vive en la materia del registro,
    la administra el runtime, no toca el estado canónico ni el diario, y no la deriva nadie
    de nada: `I-g7` intacto. El log sigue siendo APPEND-ONLY; la cabeza no es el log, es un
    puntero monótono a su extremo, que es la «semántica equivalente auditable» que `g.9`
    admite.

    RESIDUO, dicho contra el propio interés: entre el `fsync` de una línea y el reemplazo
    atómico de la cabeza hay una ventana de un anexado. Un corte justo ahí deja la cabeza
    UNA línea por detrás, y esa holgura de una sola línea hay que tolerarla o cualquier
    corte dejaría el registro inservible. Quien borrase la última línea EXACTAMENTE en esa
    ventana no sería detectado. Se cierra en cuanto el registro vuelve a anexar o el
    almacén se recupera, porque las dos cosas reescriben la cabeza. Y falsificar a la vez
    el log y su cabeza sigue sin ser detectable desde dentro, que es literalmente lo que
    `g.5` advierte —«ningún resumen calculado por el propio árbol basta como prueba de la
    integridad de ese árbol»— y lo que `g.15` reserva a la raíz externa.

DECISIÓN · una apertura NO exige evento en el diario; una resolución SÍ
    Una apertura por reintentos agotados NO PUEDE anotar en el diario: no tiene el bloqueo
    de escritor, y anotarlo sería modificar estado canónico, que `g.6` prohíbe expresamente
    en ese camino. Una resolución, en cambio, `g.9` la exige «mediante una transición
    explícita y auditable», así que se escribe DENTRO de la transacción que la explica y
    tiene su `reconciliacion.resuelta` en el diario. `auditar()` comprueba esa
    correspondencia en las dos direcciones para las resoluciones.
"""
from __future__ import annotations

import os

from . import fallos
from .errores import RegistroDeReconciliacionCorrupto, ReconciliacionDesconocida
from .rutas import (
    asegurar_directorio,
    escribir_y_sincronizar,
    leer_bytes,
    publicar,
    sincronizar_directorio,
    traducir_error_de_sistema,
)
from .serializacion import (
    ESQUEMA,
    cid_de_objeto,
    comprobar_esquema,
    deserializar,
    serializar_canonico,
    serializar_compacto,
)

TIPOS = ("apertura", "resolucion")
CLAVE_HUELLA = "huella"
CLAVE_PREVIO = "previo"
PREFIJO_REGISTRO = "rec-"
FICHERO_CABEZA = "CABEZA.json"

# Campos que `g.9` declara obligatorios en una apertura. El censo se usa para validar, y
# así una apertura incompleta se rechaza al escribirla y no al auditarla seis meses después.
CAMPOS_APERTURA = ("producto", "repositorio", "item", "intento", "causa", "momento")
CAMPOS_RESOLUCION = ("transaccion", "autoridad", "motivo", "momento")


def _huella(linea):
    """Huella de una línea del registro: `cid` de su forma canónica SIN `huella`.

    Se calcula aquí y no se importa de `diario.py`, aunque la regla sea la misma. Compartir
    la función acoplaría las dos estructuras que `I-g7` manda mantener separadas, y bastaría
    un cambio en el diario para alterar en silencio la identidad de este registro.
    """
    cuerpo = {clave: linea[clave] for clave in linea if clave != CLAVE_HUELLA}
    return cid_de_objeto(cuerpo)


def momento_logico(diario_secuencia, revision):
    """El MOMENTO de `g.9`, en coordenadas del sistema y no del reloj (`I-g3`)."""
    return {"diario_secuencia": int(diario_secuencia), "revision": int(revision)}


class RegistroAuxiliar:
    """El registro operativo auxiliar durable. Append-only y encadenado."""

    def __init__(self, ruta, bloqueo=None):
        self.ruta = ruta
        self.cabeza = os.path.join(os.path.dirname(ruta), FICHERO_CABEZA)
        # El bloqueo se inyecta para que el motor decida su ruta y para que las pruebas
        # puedan observar la serialización sin duplicar la disposición física aquí.
        self.bloqueo = bloqueo

    # ------------------------------------------------------------------ lectura
    def existe(self):
        return os.path.exists(self.ruta)

    def crear(self):
        asegurar_directorio(os.path.dirname(self.ruta))
        if not os.path.exists(self.ruta):
            try:
                descriptor = os.open(self.ruta, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
            except FileExistsError:
                return
            except OSError as exc:
                raise traducir_error_de_sistema(exc, self.ruta, "crear el registro") from exc
            os.fsync(descriptor)
            os.close(descriptor)
        # La cabeza nace con el log: un registro vacío SIN cabeza y uno al que le han
        # borrado todas las líneas son indistinguibles, y fundarla aquí evita que el
        # segundo pueda hacerse pasar por el primero en un almacén recién creado.
        if not os.path.exists(self.cabeza):
            self._publicar_cabeza(0, None)

    # ------------------------------------------------------------------- cabeza
    def _publicar_cabeza(self, secuencia, huella):
        """Escribe la cabeza de forma ATÓMICA: temporal, `fsync`, `os.replace`, `fsync` dir.

        Atómica y no «escribir encima»: una cabeza escrita a medias por un corte sería una
        cabeza corrupta, y entonces el mecanismo que existe para detectar manipulaciones
        sería él mismo la primera fuente de falsos positivos. Con `os.replace` la cabeza
        anterior sigue entera hasta que la nueva está completa en el medio.
        """
        contenido = {"esquema": ESQUEMA, "secuencia": int(secuencia), "huella": huella}
        temporal = self.cabeza + ".tmp"
        asegurar_directorio(os.path.dirname(self.cabeza))
        escribir_y_sincronizar(temporal, serializar_canonico(contenido))
        publicar(temporal, self.cabeza)
        sincronizar_directorio(os.path.dirname(self.cabeza))
        return contenido

    def _leer_cabeza(self):
        """La cabeza publicada, o `None` si no hay ninguna. Falla cerrado si está rota."""
        if not os.path.exists(self.cabeza):
            return None
        datos = leer_bytes(self.cabeza, error=RegistroDeReconciliacionCorrupto)
        cabeza = deserializar(datos, ruta=self.cabeza,
                              error=RegistroDeReconciliacionCorrupto)
        if not isinstance(cabeza, dict):
            raise RegistroDeReconciliacionCorrupto(
                "la cabeza del registro no es un objeto JSON", ruta=self.cabeza)
        comprobar_esquema(cabeza, ruta=self.cabeza,
                          error=RegistroDeReconciliacionCorrupto)
        secuencia = cabeza.get("secuencia")
        if not isinstance(secuencia, int) or isinstance(secuencia, bool) or secuencia < 0:
            raise RegistroDeReconciliacionCorrupto(
                "la cabeza del registro no declara una `secuencia` válida",
                ruta=self.cabeza)
        return cabeza

    def _exigir_cabeza(self, lineas):
        """Contrasta el log contra su cabeza. Es lo que hace detectable borrar la cola."""
        cabeza = self._leer_cabeza()
        if cabeza is None:
            if not lineas:
                return                      # registro virgen: nada que anclar todavía
            raise RegistroDeReconciliacionCorrupto(
                "el registro tiene " + str(len(lineas)) + " línea(s) y no tiene cabeza: "
                "falta `" + FICHERO_CABEZA + "`, que es lo que ancla su extremo",
                ruta=self.cabeza)
        declarada = cabeza["secuencia"]
        if declarada > len(lineas):
            # LA DETECCIÓN. La cabeza afirma un extremo que el log ya no alcanza: se han
            # retirado líneas del final, y `g.9` sólo admite retirarlas mediante una
            # transición explícita y auditable.
            raise RegistroDeReconciliacionCorrupto(
                "la cabeza del registro declara " + str(declarada) + " línea(s) y sólo "
                "hay " + str(len(lineas)) + ": se retiró la cola del registro sin la "
                "transición explícita que `g.9` exige",
                ruta=self.ruta, declarada=declarada, encontradas=len(lineas))
        if declarada < len(lineas) - 1:
            # Se toleran como mucho UNA línea por delante de la cabeza, que es la ventana
            # de un corte entre el anexado y la publicación de la cabeza. Más que eso son
            # líneas añadidas a mano, que es la manipulación simétrica de la anterior.
            raise RegistroDeReconciliacionCorrupto(
                "el registro tiene " + str(len(lineas)) + " línea(s) y su cabeza sólo "
                "llega a " + str(declarada) + ": se añadieron líneas sin pasar por el "
                "runtime",
                ruta=self.ruta, declarada=declarada, encontradas=len(lineas))
        esperada = lineas[declarada - 1][CLAVE_HUELLA] if declarada >= 1 else None
        if cabeza.get(CLAVE_HUELLA) != esperada:
            raise RegistroDeReconciliacionCorrupto(
                "la huella que declara la cabeza no es la de la línea " + str(declarada)
                + ": el registro o su cabeza fueron editados",
                ruta=self.cabeza)

    def _particion(self):
        if not os.path.exists(self.ruta):
            return [], b""
        try:
            with open(self.ruta, "rb") as fichero:
                datos = fichero.read()
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "leer el registro") from exc
        if not datos:
            return [], b""
        corte = datos.rfind(b"\n")
        if corte == -1:
            return [], datos
        return datos[: corte + 1].split(b"\n")[:-1], datos[corte + 1:]

    def cola_desgarrada(self):
        return bool(self._particion()[1])

    def lineas(self, verificar=True, tolerar_cola=False):
        """Las líneas del registro, con la cadena verificada de principio a fin.

        Borrar una línea a mano —lo que el §9 nombra explícitamente— rompe `previo` en la
        siguiente y produce `RegistroDeReconciliacionCorrupto`. Es el mecanismo que hace que
        «desaparece ÚNICAMENTE mediante una transición explícita» sea comprobable y no una
        buena intención.
        """
        completas, cola = self._particion()
        if cola and not tolerar_cola:
            raise RegistroDeReconciliacionCorrupto(
                "el registro auxiliar termina en una línea incompleta de " + str(len(cola))
                + " byte(s)",
                ruta=self.ruta,
                bytes_sueltos=len(cola),
            )
        salida = []
        anterior = None
        for indice, cruda in enumerate(completas):
            linea = deserializar(cruda, ruta=self.ruta, error=RegistroDeReconciliacionCorrupto)
            if not isinstance(linea, dict):
                raise RegistroDeReconciliacionCorrupto(
                    "la línea " + str(indice + 1) + " no es un objeto JSON", ruta=self.ruta
                )
            comprobar_esquema(linea, ruta=self.ruta, error=RegistroDeReconciliacionCorrupto)
            if verificar:
                self._verificar_eslabon(linea, anterior, indice)
            salida.append(linea)
            anterior = linea
        if verificar:
            # En el camino de LECTURA, y no sólo en `verificar_integridad`: `g.9` exige que
            # la pendencia se deduzca de forma INEQUÍVOCA, y deducirla de un log al que le
            # falta la cola no es deducirla, es creerse lo que quedó.
            self._exigir_cabeza(salida)
        return salida

    def _verificar_eslabon(self, linea, anterior, indice):
        esperada = indice + 1
        if linea.get("secuencia") != esperada:
            raise RegistroDeReconciliacionCorrupto(
                "la secuencia del registro salta: se esperaba " + str(esperada)
                + " y se lee " + str(linea.get("secuencia")),
                ruta=self.ruta,
                posicion=esperada,
            )
        if linea.get("tipo") not in TIPOS:
            raise RegistroDeReconciliacionCorrupto(
                "tipo no declarado en el §2.5: " + repr(linea.get("tipo")),
                ruta=self.ruta,
                posicion=esperada,
            )
        obligatorios = CAMPOS_APERTURA if linea["tipo"] == "apertura" else CAMPOS_RESOLUCION
        faltan = [campo for campo in obligatorios if campo not in linea]
        if faltan or "registro" not in linea:
            raise RegistroDeReconciliacionCorrupto(
                "faltan campos obligatorios de `g.9`: " + ", ".join(sorted(faltan) or ["registro"]),
                ruta=self.ruta,
                posicion=esperada,
            )
        previo_esperado = anterior[CLAVE_HUELLA] if anterior is not None else None
        if linea.get(CLAVE_PREVIO) != previo_esperado:
            raise RegistroDeReconciliacionCorrupto(
                "la cadena de hash se rompe en la línea " + str(esperada)
                + ": falta una línea, se insertó una, o se editó el registro a mano",
                ruta=self.ruta,
                posicion=esperada,
            )
        calculada = _huella(linea)
        if linea.get(CLAVE_HUELLA) != calculada:
            raise RegistroDeReconciliacionCorrupto(
                "la huella de la línea " + str(esperada) + " no casa con su contenido",
                ruta=self.ruta,
                posicion=esperada,
                esperada=calculada,
                encontrada=linea.get(CLAVE_HUELLA),
            )

    # -------------------------------------------------------------- deducciones
    # Todas las deducciones aceptan una instantánea del llamador. El registro también es
    # APPEND-ONLY y también lo escriben otros procesos —el escritor derrotado abre su
    # apertura sin el bloqueo de escritor—, así que dos lecturas seguidas devuelven
    # legítimamente dos contenidos. Quien vaya a cruzar dos deducciones pasa `lineas` y
    # cruza sobre el MISMO corte; quien sólo quiera una, deja que se lea aquí.
    def aperturas(self, lineas=None):
        lineas = self.lineas() if lineas is None else lineas
        return [linea for linea in lineas if linea["tipo"] == "apertura"]

    def resoluciones(self, lineas=None):
        lineas = self.lineas() if lineas is None else lineas
        return [linea for linea in lineas if linea["tipo"] == "resolucion"]

    def pendientes(self, lineas=None):
        """`reconciliacion_pendiente` (`g.9`): apertura SIN resolución, deducido, no guardado."""
        lineas = self.lineas() if lineas is None else lineas
        resueltos = {l["registro"] for l in lineas if l["tipo"] == "resolucion"}
        return [l for l in lineas if l["tipo"] == "apertura" and l["registro"] not in resueltos]

    def tiene_resolucion(self, registro, lineas=None):
        lineas = self.lineas() if lineas is None else lineas
        return any(
            l["tipo"] == "resolucion" and l["registro"] == registro for l in lineas
        )

    def apertura_de(self, registro, lineas=None):
        lineas = self.lineas() if lineas is None else lineas
        for linea in lineas:
            if linea["tipo"] == "apertura" and linea["registro"] == registro:
                return linea
        raise ReconciliacionDesconocida(
            "no hay ninguna apertura con ese identificador en el registro auxiliar",
            ruta=registro,
        )

    def siguiente_identificador(self):
        """`rec-0001`, `rec-0002`… Deriva del recuento de aperturas: sin contador guardado."""
        return PREFIJO_REGISTRO + str(len(self.aperturas()) + 1).zfill(4)

    # ----------------------------------------------------------------- escritura
    def sincronizar_cabeza(self):
        """Vuelve a anclar la cabeza al extremo real del log. Cierra la holgura de un corte.

        Sólo se llama desde la recuperación, que tiene los cerrojos. NO repara un borrado:
        si la cabeza afirmara más líneas de las que hay, `_exigir_cabeza` falla cerrado
        antes de llegar aquí, y así tiene que ser: reparar eso sería borrar la prueba.
        """
        lineas = self.lineas()
        if not lineas:
            if self._leer_cabeza() is None:
                self._publicar_cabeza(0, None)
            return 0
        ultima = lineas[-1]
        cabeza = self._leer_cabeza()
        if cabeza is not None and cabeza["secuencia"] == ultima["secuencia"]:
            return 0
        self._publicar_cabeza(ultima["secuencia"], ultima[CLAVE_HUELLA])
        return ultima["secuencia"]

    def reparar_cola(self):
        completas, cola = self._particion()
        if not cola:
            return 0
        longitud = sum(len(linea) + 1 for linea in completas)
        try:
            descriptor = os.open(self.ruta, os.O_WRONLY)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "reparar el registro") from exc
        try:
            os.ftruncate(descriptor, longitud)
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        return len(cola)

    def _anexar(self, linea):
        completas, cola = self._particion()
        if cola:
            raise RegistroDeReconciliacionCorrupto(
                "no se anexa sobre un registro con la cola desgarrada", ruta=self.ruta
            )
        # UNA sola lectura del log —la de `_particion`— alimenta las dos deducciones: el
        # contraste con la cabeza y el `previo` de la nueva línea. Releer para cada una
        # sería el mismo patrón de lecturas cruzadas que ya costó un `KeyError` en el diario.
        interpretadas = [
            deserializar(cruda, ruta=self.ruta, error=RegistroDeReconciliacionCorrupto)
            for cruda in completas
        ]
        # Se verifica ANTES de anexar: encadenar sobre un log manipulado convertiría la
        # manipulación en historia legítima a partir de la línea siguiente.
        self._exigir_cabeza(interpretadas)
        previo = interpretadas[-1].get(CLAVE_HUELLA) if interpretadas else None
        linea = dict(linea)
        linea["esquema"] = ESQUEMA
        linea["secuencia"] = len(completas) + 1
        linea[CLAVE_PREVIO] = previo
        linea[CLAVE_HUELLA] = _huella(linea)

        datos = serializar_compacto(linea) + b"\n"
        asegurar_directorio(os.path.dirname(self.ruta))
        try:
            descriptor = os.open(self.ruta, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "abrir el registro") from exc
        try:
            escritos = os.write(descriptor, datos)
            if escritos != len(datos):
                raise RegistroDeReconciliacionCorrupto(
                    "el anexado al registro quedó corto", ruta=self.ruta
                )
            fallos.punto("durante-el-registro-auxiliar")
            os.fsync(descriptor)
        except OSError as exc:
            raise traducir_error_de_sistema(exc, self.ruta, "anexar al registro") from exc
        finally:
            os.close(descriptor)
        # La cabeza DESPUÉS del `fsync` de la línea, nunca antes: si se publicara primero,
        # un corte entre ambas dejaría una cabeza que afirma una línea inexistente, y eso
        # es indistinguible de un borrado. Al revés, el corte deja la cabeza una línea por
        # detrás, que es la holgura tolerada y se repara en el siguiente anexado.
        self._publicar_cabeza(linea["secuencia"], linea[CLAVE_HUELLA])
        return linea

    def anexar_apertura(self, *, registro, producto, repositorio, item, intento, causa,
                        momento):
        """Abre un registro auxiliar. NO toca el estado canónico: ése es todo su sentido."""
        for nombre, valor in (("producto", producto), ("repositorio", repositorio),
                              ("item", item), ("causa", causa)):
            if not isinstance(valor, str) or not valor.strip():
                raise RegistroDeReconciliacionCorrupto(
                    "`g.9` exige identificar " + nombre.upper() + " y no admite vacío",
                    ruta=self.ruta,
                )
        if not isinstance(intento, int) or intento < 1:
            raise RegistroDeReconciliacionCorrupto(
                "`intento` es el número de intento realizado y es un entero >= 1",
                ruta=self.ruta,
            )
        return self._escribir_con_bloqueo({
            "tipo": "apertura",
            "registro": registro,
            "producto": producto,
            "repositorio": repositorio,
            "item": item,
            "intento": intento,
            "causa": causa,
            "momento": momento,
        })

    def anexar_resolucion(self, *, registro, transaccion, autoridad, motivo, momento):
        """Cierra un registro. Sólo la llama el motor DENTRO de la transacción que la explica."""
        for nombre, valor in (("autoridad", autoridad), ("motivo", motivo)):
            if not isinstance(valor, str) or not valor.strip():
                raise RegistroDeReconciliacionCorrupto(
                    "una resolución sin " + nombre + " no es auditable", ruta=self.ruta
                )
        return self._escribir_con_bloqueo({
            "tipo": "resolucion",
            "registro": registro,
            "transaccion": transaccion,
            "autoridad": autoridad,
            "motivo": motivo,
            "momento": momento,
        })

    def _escribir_con_bloqueo(self, linea):
        if self.bloqueo is None:
            return self._anexar(linea)
        # Reentrante a propósito: el motor puede tener ya tomado el bloqueo del registro
        # para leer y escribir de forma consistente dentro de una misma transacción.
        if self.bloqueo.tomado():
            return self._anexar(linea)
        self.bloqueo.adquirir(intentos=20)
        try:
            return self._anexar(linea)
        finally:
            self.bloqueo.liberar()
