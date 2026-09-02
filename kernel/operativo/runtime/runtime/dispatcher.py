#!/usr/bin/env python3
"""dispatcher — el RUNTIME de ADS: ejecuta contratos existentes, y no es fuente de verdad.

    «NO ES una fuente de verdad. Todo lo que decide queda escrito en el estado canónico
     ANTES de que valga. Si el runtime muere, el estado sigue siendo el estado.»
                                                                    `11-ARQ` §7.1

Ésa es la regla que gobierna cada línea de este módulo. Sus consecuencias, dichas para que
se puedan comprobar y no sólo creer:

  · NO HAY UN SEGUNDO SISTEMA DE ESTADO. No hay cola en memoria que sea la verdad, ni
    fichero de trabajo propio, ni diario paralelo, ni recuperación alternativa. Todo lo
    durable es una `Transicion` sobre el `Almacen` de `estado/`. Este objeto guarda en
    memoria tres cosas y ninguna es estado del trabajo: el almacén abierto, el testigo de
    vida —que vive en el plano operacional, gitignorado— y la configuración inmutable
    recibida en el constructor.
  · EL TRABAJO ELEGIBLE SE DERIVA DEL ESTADO en cada llamada. `elegibles()` no recuerda
    nada entre llamadas: lee `canonico/paquetes/` y ordena. Dos instancias ven la MISMA
    lista, y por eso la carrera por un paquete es real y no accidental.
  · NINGUNA DECISIÓN VALE ANTES DE ESTAR ESCRITA. Se adquiere autoridad escribiendo el
    lease; se abre el intento escribiendo el paquete; se acusa el efecto escribiendo el
    acuse en la MISMA transición que el resultado.

DECISIÓN · toda escritura pasa por `estado_util.aplicar_con_reintento`
    Es la única forma de escribir de este módulo, y la razón está escrita en ese fichero:
    el motor hace comparación e intercambio sobre la revisión base, así que la transición
    se construye como FUNCIÓN de la revisión releída y la guarda se reevalúa en cada
    vuelta. Reaplicar una transición ya construida convertiría el CAS en «el último gana»,
    que es lo que `g.6` prohíbe.

DECISIÓN · `abrir()` recupera EXPLÍCITAMENTE y guarda el informe
    Alternativas: (a) `estado.abrir(recuperar=True)`, que recupera por dentro; (b) abrir
    sin recuperar y llamar a `recuperar()`.
    Se elige (b). El §4.2 exige que si la recuperación vuelve MARCADO el runtime no
    despache nada, y con (a) el informe se pierde dentro de `abrir` y no hay forma de
    saber si hubo marca. Con (b) el informe queda en `self.recuperacion` y `marcado` es un
    dato comprobable. El único matiz: `estado.abrir(recuperar=False)` no tolera una cola
    de diario desgarrada y levanta `DiarioCorrupto`; ese error tipado —y sólo ése— se
    trata volviendo a abrir con `recuperar=True`, que es el camino que el motor reserva
    para repararla. No es tragarse una excepción: es tomar el camino declarado para ella.

DECISIÓN · un fallo de EJECUCIÓN se ESCRIBE primero y se levanta después
    `despachar` escribe el resultado y el acuse, aplica la política y sólo entonces
    levanta `EjecucionFallida`, `EjecucionDefinitiva`, `EjecucionCancelada` o
    `TiempoAgotado`. Levantar antes de escribir dejaría el paquete en `ejecutando` con un
    efecto ya aplicado y sin acuse, que es exactamente el estado que la idempotencia
    quiere evitar. `AutoridadPerdida` es la excepción y va al revés: se levanta SIN
    escribir nada, porque escribir sería pisar al titular vigente.

DECISIÓN · agotar libera la autoridad, y eso NO es «tocar más el estado canónico»
    El §4.2 dice que al agotar el paquete pasa a `agotado` y el estado canónico no se toca
    más. Lo que no se toca es la UNIDAD DE TRABAJO: su salida la decide la autoridad por la
    única vía de `g.9`. El lease es autoridad, no trabajo, y dejarlo tomado convertiría
    cada agotamiento en un lease huérfano que sólo una reclamación por observaciones
    podría retirar. Se libera, en su propia transición, después de abrir la reconciliación.
"""
from __future__ import annotations

import os

import estado
from estado.errores import DiarioCorrupto, RutaInvalida
from estado.rutas import SEGMENTO_VALIDO
from estado.serializacion import cid_de_objeto

from . import fallos, politica, vistas
from .ejecucion import comprobar_adaptador
from .errores import (
    AdaptadorIncompatible,
    AutoridadNoDisponible,
    AutoridadPerdida,
    CapacidadNoSoportada,
    DependenciaNoResuelta,
    EjecucionCancelada,
    EjecucionDefinitiva,
    EjecucionFallida,
    EstadoDePaqueteInvalido,
    PaqueteDesconocido,
    ReclamacionPrematura,
    RuntimeInconsistente,
    TiempoAgotado,
)
from .estado_util import aplicar_con_reintento
from .lease import (
    PACIENCIA_POR_DEFECTO,
    TestigoDeVida,
    comprobar_lease,
    con_latido,
    con_observacion,
    es_titular,
    exigir_titularidad,
    nuevo_lease,
    observaciones_de,
    reclamado_por,
)
from .modelo import (
    DOMINIO_LEASES,
    DOMINIO_PAQUETES,
    ESTADOS_EN_CURSO,
    comprobar_paquete,
    comprobar_transicion,
    con_estado,
    derivar_efecto,
    identificador_de,
    normalizar_orden,
    nuevo_acuse,
    nuevo_item,
    nuevo_paquete,
    ruta_efecto,
    ruta_item,
    ruta_lease,
    ruta_paquete,
)

REPOSITORIO = "control"

# Trabajo que ya no admite despacho: los dos terminales del §3 más `agotado`, cuya salida
# la decide la autoridad por `g.9`. Un lease sobre uno de éstos no gobierna nada.
ESTADOS_CERRADOS = ("completado", "cancelado", "agotado")

# Lecturas del diario que se conceden a una ventana ajena para que se cierre sola antes de
# ir a recuperarla. Se cuenta en LECTURAS y no en segundos: el tiempo lógico de este
# sistema es la revisión, no el reloj, y una espera medida en observaciones es reproducible
# donde una medida en milisegundos depende de la máquina.
OBSERVACIONES_DE_LA_VENTANA = 40

DESENLACE_COMPLETADO = "completado"
DESENLACE_FALLIDO = "fallido"
DESENLACE_AGOTADO = "agotado"
DESENLACE_CANCELADO = "cancelado"
DESENLACE_OMITIDO = "omitido"

# Errores que `ciclo` ANOTA en su informe en vez de propagar: describen el desenlace de un
# paquete concreto, no un defecto del barrido. Se enumeran uno a uno —nunca `Exception`—
# para que añadir una clase nueva a la jerarquía obligue a decidir dónde encaja.
DESENLACES_DE_UN_PAQUETE = (
    AutoridadNoDisponible, AutoridadPerdida, DependenciaNoResuelta,
    CapacidadNoSoportada, AdaptadorIncompatible, EstadoDePaqueteInvalido,
    EjecucionFallida, EjecucionDefinitiva, EjecucionCancelada, TiempoAgotado,
)

# Fallos que ocurren ANTES de que nada se haya ejecutado. Al propagarlos hay que soltar la
# autoridad: retenerla dejaría el paquete inalcanzable para cualquier otra instancia hasta
# que alguien acumulase `PACIENCIA` observaciones. Se enumeran uno a uno, nunca `Exception`.
FALLOS_ANTES_DE_EJECUTAR = (
    DependenciaNoResuelta, CapacidadNoSoportada, AdaptadorIncompatible,
    EstadoDePaqueteInvalido, RuntimeInconsistente, PaqueteDesconocido,
)


class Cancelacion:
    """`.activada()` LEE el estado canónico. No hay bandera en memoria que pueda mentir."""

    def __init__(self, runtime, paquete):
        self._runtime = runtime
        self._paquete = paquete

    def activada(self):
        actual = self._runtime._leer_paquete_opcional(self._paquete)
        if actual is None:
            # El paquete desapareció mientras corría: no hay a quién entregarle el
            # resultado, así que la ejecución debe pararse igual que si se cancelara.
            return True
        return actual["estado"] == "cancelado"


class Runtime:
    """El runtime y el dispatcher del §7 de `11-ARQ`, sobre el motor de estado durable."""

    def __init__(self, ruta_control_repo, *, instancia,
                 paciencia=PACIENCIA_POR_DEFECTO, registro_de_adaptadores=None):
        if not isinstance(instancia, str) or not SEGMENTO_VALIDO.match(instancia):
            raise RuntimeInconsistente(
                "el nombre de instancia debe casar con " + SEGMENTO_VALIDO.pattern
                + ": nombra el `titular` de un lease durable y el testigo de vida",
                instancia=str(instancia),
            )
        if not isinstance(paciencia, int) or isinstance(paciencia, bool) or paciencia < 1:
            raise RuntimeInconsistente(
                "`paciencia` es el número de observaciones consecutivas sin latido que "
                "exige una reclamación, y es un entero >= 1",
            )
        self.ruta = ruta_control_repo
        self.instancia = instancia
        self.paciencia = paciencia
        self.registro = registro_de_adaptadores
        self.recuperacion = None
        self.marcado = False
        self._almacen = None
        self._testigo = None

    # =====================================================================
    #  1 · abrir, 19 · cerrar
    # =====================================================================
    def abrir(self):
        """Abre el control repo, RECUPERA antes de despachar y declara viva la instancia."""
        if self._almacen is not None:
            return self
        disposicion_estado = os.path.join(self.ruta, "estado")
        if not os.path.isdir(disposicion_estado):
            # Fundar el almacén es parte de «abrir un control repo» (§4.2, capacidad 1).
            # `estado.inicializar` exige que el directorio del repo exista, de modo que una
            # ruta equivocada sigue dando un error tipado en vez de crear un árbol nuevo.
            almacen = estado.inicializar(self.ruta)
        else:
            try:
                almacen = estado.abrir(self.ruta, recuperar=False)
            except DiarioCorrupto:
                # Camino DECLARADO para una cola de diario desgarrada: el motor la repara
                # al abrir con recuperación. No se trata ningún otro error de esta forma.
                almacen = estado.abrir(self.ruta, recuperar=True)
        try:
            informe = self._recuperar_si_hace_falta(almacen)
            testigo = TestigoDeVida(
                os.path.join(almacen.ruta_almacen, "operacional"), self.instancia
            ).abrir()
        except BaseException:
            # NO se traga nada: se cierra el almacén y se RELANZA. `BaseException` y no
            # `Exception` porque un `KeyboardInterrupt` entre el `abrir` y el testigo
            # dejaría igual de abierto el `flock` de escritor del motor, y quien reabra
            # después esperaría cuatro segundos por un proceso que ya no existe.
            almacen.cerrar()
            raise
        self._almacen = almacen
        self._testigo = testigo
        self.recuperacion = informe
        # MARCADO: `g.8` reserva la salida de un conflicto a la AUTORIDAD, no al runtime.
        # Mientras haya una transacción marcada, este runtime no despacha NADA.
        self.marcado = bool(informe["marcadas"]) or informe["rama"] == "marcar"
        return self

    def _recuperar_si_hace_falta(self, almacen):
        """RECUPERA ANTES DE DESPACHAR, y sólo si de verdad hay una ventana que cerrar.

        DECISIÓN · la ventana se OBSERVA antes de recuperar, y las observaciones se CUENTAN
            `Almacen.recuperar()` toma el bloqueo EXCLUSIVO de escritor. Llamarlo en cada
            apertura —aunque no hubiera nada que cerrar— hacía que dos runtimes que
            arrancan a la vez compitieran por ese bloqueo sin motivo, y agotar sus
            reintentos abre un registro de reconciliación de `g.9` que no describe ningún
            trabajo fallido, sino contención. `g.9` se llenaba de pendencias vacías.
            Alternativas: (a) recuperar siempre; (b) recuperar sólo si la ventana está
            abierta; (c) además, esperar a que se cierre sola antes de intentarlo.
            Se eligen (b) y (c) juntas. (b) sola no basta: en plena carrera la ventana casi
            siempre está abierta, porque el OTRO proceso está a mitad de una transición
            perfectamente sana, y recuperarla es exactamente lo que no hay que hacer.
            (c) espera, y la espera se mide en OBSERVACIONES CONTADAS del diario y no en
            segundos, por la misma razón que la expiración de un lease: el reloj no es el
            tiempo lógico de este sistema. Una ventana que sigue abierta tras
            `OBSERVACIONES_DE_LA_VENTANA` lecturas es una ventana que nadie está cerrando,
            y ésa sí se recupera.

        Cuando no hay ventana, el informe se compone LEYENDO el diario, que es lo que
        `recuperar()` habría hecho igualmente para calcular `marcadas`: sin él no se podría
        saber si `g.8` dejó algo MARCADO, y el §4.2 exige no despachar en ese caso.
        """
        ventana = almacen.estado_de_la_ventana()
        observaciones = 0
        while ventana != "cerrada" and observaciones < OBSERVACIONES_DE_LA_VENTANA:
            observaciones += 1
            ventana = almacen.estado_de_la_ventana()
        if ventana != "cerrada":
            return almacen.recuperar().a_dict()
        marcadas = sorted({
            evento["transaccion"] for evento in almacen.diario()
            if evento["tipo"] == "transicion.marcada"
        })
        return {
            "rama": "ninguna", "ventana_previa": "cerrada", "transaccion": None,
            "acciones": [], "eventos_anexados": [],
            "revision_id": almacen.revision()["revision_id"], "conflicto": None,
            "marcadas": marcadas, "cola_del_diario_descartada": 0,
            "observaciones_de_la_ventana": observaciones,
        }

    def cerrar(self):
        """Cierre limpio (§4.2, capacidad 19). Idempotente: se llama también desde `__exit__`."""
        if self._testigo is not None:
            self._testigo.cerrar()
            self._testigo = None
        if self._almacen is not None:
            self._almacen.cerrar()
            self._almacen = None

    def __enter__(self):
        return self.abrir()

    def __exit__(self, tipo, valor, traza):
        self.cerrar()
        return False

    # ------------------------------------------------------------- salvaguardas
    def _exigir_operable(self):
        if self._almacen is None:
            raise RuntimeInconsistente(
                "el runtime no está abierto; `abrir()` recupera el estado ANTES de "
                "despachar y ese orden no se puede saltar",
            )

    def _exigir_no_marcado(self):
        if self.marcado:
            raise RuntimeInconsistente(
                "la recuperación dejó transacciones MARCADAS: `g.8` reserva su salida a "
                "la autoridad y este runtime no despacha nada hasta que se resuelvan",
                marcadas=list((self.recuperacion or {}).get("marcadas") or []),
            )

    @property
    def almacen(self):
        """El `Almacen` abierto. Se expone porque la verdad vive ahí y no aquí."""
        self._exigir_operable()
        return self._almacen

    # =====================================================================
    #  lectura — todo se lee del estado canónico, nunca de memoria
    # =====================================================================
    def _leer_opcional(self, ruta):
        try:
            return self._almacen.leer(ruta)
        except RutaInvalida:
            return None

    def _leer_paquete(self, paquete):
        ruta = ruta_paquete(paquete)
        objeto = self._leer_opcional(ruta)
        if objeto is None:
            raise PaqueteDesconocido(
                "no hay paquete con ese identificador en la revisión vigente",
                ruta=paquete,
            )
        return comprobar_paquete(objeto, ruta)

    def _leer_paquete_opcional(self, paquete):
        objeto = self._leer_opcional(ruta_paquete(paquete))
        if objeto is None:
            return None
        return comprobar_paquete(objeto, ruta_paquete(paquete))

    def _leer_lease(self, paquete):
        ruta = ruta_lease(paquete)
        objeto = self._leer_opcional(ruta)
        if objeto is None:
            return None
        lease = comprobar_lease(objeto, ruta)
        if lease["paquete"] != paquete:
            raise RuntimeInconsistente(
                "el lease dice gobernar el paquete `" + str(lease["paquete"])
                + "` y está escrito en la ruta de `" + paquete + "`",
                ruta=ruta,
            )
        return lease

    def _leer_acuse(self, efecto, *, paquete):
        if not efecto:
            return None
        ruta = ruta_efecto(efecto)
        acuse = self._leer_opcional(ruta)
        if acuse is None:
            return None
        if acuse.get("paquete") != paquete or acuse.get("efecto") != efecto:
            raise RuntimeInconsistente(
                "el acuse `" + efecto + "` dice acusar el paquete `"
                + str(acuse.get("paquete")) + "`",
                ruta=ruta,
            )
        if acuse.get("aplicado") is not True:
            raise RuntimeInconsistente(
                "hay un acuse de efecto que no declara `aplicado: true`; un acuse sólo se "
                "escribe cuando el efecto ya se aplicó",
                ruta=ruta,
            )
        return acuse

    def _todos_los_paquetes(self):
        salida = []
        for ruta in self._almacen.listar(DOMINIO_PAQUETES):
            salida.append(comprobar_paquete(self._almacen.leer(ruta), ruta))
        salida.sort(key=lambda p: p["id"])
        return salida

    # =====================================================================
    #  escritura — una sola puerta
    # =====================================================================
    def _identificador(self, clase, semilla, revision):
        """`tx-rt-<16 hex>` derivado del CONTENIDO. Sin reloj, sin pid, sin uuid (`I-g3`).

        La revisión base entra en la semilla a propósito: sin ella, dos vueltas del
        reintento por revisión obsoleta producirían el mismo identificador y el motor
        devolvería la primera como `repetida` en vez de aplicar la segunda, que es la que
        se construyó sobre el estado nuevo. La instancia también entra: dos runtimes que
        compiten por el mismo lease deben producir DOS transacciones distintas, o el
        segundo creería haber adquirido lo que adquirió el primero.
        """
        digest = cid_de_objeto({
            "clase": clase,
            "instancia": self.instancia,
            "revision": revision["revision_id"],
            "semilla": semilla,
        })
        return "tx-rt-" + digest.split(":", 1)[-1][:16]

    def _aplicar(self, clase, construir, *, descripcion):
        return aplicar_con_reintento(
            self._almacen, construir, descripcion=descripcion,
        )

    def _transicion(self, clase, revision, operaciones, motivo, semilla):
        return estado.Transicion(
            tipo=clase, base=revision["revision_id"], operaciones=operaciones,
            autor=self.instancia, motivo=motivo,
            id=self._identificador(clase, semilla, revision),
        )

    # =====================================================================
    #  4 · adquirir autoridad · 5 · impedir doble despacho · 17 · expirarla
    # =====================================================================
    def adquirir(self, paquete):
        """Toma el lease del paquete. **`adquirir` NUNCA ROBA.**

        Sólo hace dos cosas: crear el lease cuando no hay ninguno, y renovar el PROPIO. Si
        el lease es de otro —esté vivo, muerto o sea indecidible— la respuesta es
        `AutoridadNoDisponible`, y punto.

        DECISIÓN · quitarle un lease a otro es una DECISIÓN, no un efecto colateral de pedirlo
            Corregido tras la integración. `adquirir` tenía dentro la vía rápida: si el
            titular parecía muerto, reclamaba en el acto. Dos cosas iban mal a la vez. La
            primera era que «parecía muerto» incluía a todo el que hubiera terminado bien,
            y eso se arregla en `lease.TestigoDeVida.cerrar`. La segunda es de diseño y es
            la que se arregla aquí: mientras robar sea una rama de `adquirir`, cualquier
            camino que pida autoridad puede acabar quitándosela a otro sin que en el código
            aparezca la palabra. Ahora robar tiene un solo nombre, `reclamar`, y sus dos
            únicas puertas siguen siendo las del §3: `PACIENCIA` observaciones consecutivas
            sin latido, o muerte PROBADA. Quien despacha llama a `reclamar` de forma
            explícita —`_reclamar_si_murio`— y el robo se lee en la traza del diario.
            Alternativa descartada: dejar la vía rápida en `adquirir` sólo para la muerte
            probada. Es correcta hoy y sigue siendo indistinguible de un robo mañana, en
            cuanto alguien toque la definición de «probada».
        """
        self._exigir_operable()
        self._leer_paquete(paquete)
        escrito = {}

        def construir(revision):
            lease = self._leer_lease(paquete)
            if lease is None:
                nuevo = nuevo_lease(paquete=paquete, titular=self.instancia,
                                    revision_adquirida=revision["revision_id"])
                motivo = "adquisición inicial de autoridad sobre " + paquete
            elif es_titular(lease, self.instancia):
                nuevo = con_latido(lease)
                motivo = "renovación de la autoridad propia sobre " + paquete
            else:
                # El lease es de OTRO. No se mira si está vivo para decidir si robar: no se
                # roba. Se mira sólo para explicar en el error cuál es la vía abierta.
                muerto = self._testigo.titular_muerto(lease["titular"])
                if muerto is True:
                    salida = ("su testigo de vida quedó libre, luego murió: la vía es "
                              "`reclamar`, que sube la época y deja el robo escrito")
                elif muerto is False:
                    salida = "su testigo de vida sigue tomado: está VIVO"
                else:
                    salida = ("no hay testigo suyo en esta máquina, así que su estado es "
                              "INDECIDIBLE: la vía es observar y luego `reclamar`")
                raise AutoridadNoDisponible(
                    "el lease lo tiene `" + lease["titular"] + "` en la época "
                    + str(lease["epoca"]) + "; " + salida,
                    ruta=paquete, titular=lease["titular"], epoca=lease["epoca"],
                )
            escrito["lease"] = nuevo
            return self._transicion(
                "runtime.lease.adquirido", revision,
                [estado.Escritura(ruta_lease(paquete), nuevo)], motivo,
                {"paquete": paquete, "epoca": nuevo["epoca"], "latido": nuevo["latido"]},
            )

        self._aplicar("runtime.lease.adquirido", construir,
                      descripcion="adquisición del lease de " + paquete)
        return escrito["lease"]

    def _reclamar_si_murio(self, paquete):
        """Reclama SÓLO ante muerte PROBADA del titular. Devuelve si hubo reclamación.

        Es la única puerta por la que el barrido del dispatcher se hace con la autoridad de
        otro, y pasa por `reclamar`, no por `adquirir`: así el robo queda escrito en el
        diario como `runtime.lease.reclamado`, con la época que sube, y se puede auditar.
        Muerte PROBADA es la tercera lectura de `titular_muerto`: el testigo existe y su
        `flock` está libre, que es lo que deja un final abrupto y sólo un final abrupto.
        """
        lease = self._leer_lease(paquete)
        if lease is None or es_titular(lease, self.instancia):
            return False
        if self._testigo.titular_muerto(lease["titular"]) is not True:
            return False
        self.reclamar(paquete)
        return True

    def renovar(self, paquete):
        """Sube el `latido`: el titular demuestra progreso. `AutoridadPerdida` si ya no lo es."""
        self._exigir_operable()
        self._leer_paquete(paquete)
        escrito = {}

        def construir(revision):
            lease = exigir_titularidad(self._leer_lease(paquete), self.instancia, None,
                                       paquete=paquete)
            nuevo = con_latido(lease)
            escrito["lease"] = nuevo
            return self._transicion(
                "runtime.lease.renovado", revision,
                [estado.Escritura(ruta_lease(paquete), nuevo)],
                "renovación de autoridad sobre " + paquete,
                {"paquete": paquete, "latido": nuevo["latido"]},
            )

        self._aplicar("runtime.lease.renovado", construir,
                      descripcion="renovación del lease de " + paquete)
        return escrito["lease"]

    def observar(self, paquete):
        """Anota una observación de aspirante: el `latido` visto, y cuántas van seguidas."""
        self._exigir_operable()
        self._leer_paquete(paquete)
        escrito = {}

        def construir(revision):
            lease = self._leer_lease(paquete)
            if lease is None:
                raise RuntimeInconsistente(
                    "no hay lease sobre este paquete: no hay autoridad que observar. "
                    "Para tomarla se usa `adquirir`",
                    ruta=paquete,
                )
            nuevo = con_observacion(lease, self.instancia)
            escrito["lease"] = nuevo
            anotacion = nuevo["observado_por"][self.instancia]
            return self._transicion(
                "runtime.lease.observado", revision,
                [estado.Escritura(ruta_lease(paquete), nuevo)],
                "observación " + str(anotacion["observaciones"]) + " de `"
                + self.instancia + "` sobre el latido " + str(anotacion["latido"]),
                {"paquete": paquete, "latido": anotacion["latido"],
                 "observaciones": anotacion["observaciones"]},
            )

        self._aplicar("runtime.lease.observado", construir,
                      descripcion="observación del lease de " + paquete)
        return escrito["lease"]

    def reclamar(self, paquete):
        """Reclama un lease abandonado. `ReclamacionPrematura` si aún no toca."""
        self._exigir_operable()
        self._leer_paquete(paquete)
        escrito = {}

        def construir(revision):
            lease = self._leer_lease(paquete)
            if lease is None:
                raise RuntimeInconsistente(
                    "no hay lease que reclamar sobre este paquete; para tomarlo se usa "
                    "`adquirir`", ruta=paquete,
                )
            if es_titular(lease, self.instancia):
                escrito["lease"] = lease
                return None
            muerto = self._testigo.titular_muerto(lease["titular"])
            if muerto is not True:
                vistas_seguidas = observaciones_de(lease, self.instancia)
                if vistas_seguidas < self.paciencia:
                    raise ReclamacionPrematura(
                        "hacen falta " + str(self.paciencia) + " observaciones "
                        "consecutivas sin que el latido avance y hay "
                        + str(vistas_seguidas) + "; el latido vigente es "
                        + str(lease["latido"]),
                        ruta=paquete, observaciones=vistas_seguidas,
                        paciencia=self.paciencia, latido=lease["latido"],
                    )
            nuevo = reclamado_por(lease, self.instancia, revision["revision_id"])
            escrito["lease"] = nuevo
            return self._transicion(
                "runtime.lease.reclamado", revision,
                [estado.Escritura(ruta_lease(paquete), nuevo)],
                "reclamación del lease abandonado por `" + lease["titular"]
                + "`; época " + str(lease["epoca"]) + " → " + str(nuevo["epoca"]),
                {"paquete": paquete, "epoca": nuevo["epoca"]},
            )

        self._aplicar("runtime.lease.reclamado", construir,
                      descripcion="reclamación del lease de " + paquete)
        return escrito["lease"]

    def liberar(self, paquete):
        """Suelta la autoridad. Un paquete `despachado` sin empezar vuelve a `listo`."""
        self._exigir_operable()

        def construir(revision):
            lease = self._leer_lease(paquete)
            if lease is None:
                return None                    # ya estaba liberado: nada que escribir
            exigir_titularidad(lease, self.instancia, None, paquete=paquete)
            operaciones = [estado.Borrado(ruta_lease(paquete))]
            actual = self._leer_paquete_opcional(paquete)
            if actual is not None and actual["estado"] == "despachado":
                # `despachado` → `listo` está en la tabla del §4.2, y es lo correcto: se
                # abrió un intento que nadie llegó a ejecutar. Un paquete en `ejecutando`
                # NO se toca: la tabla no permite volver de ahí, y su reanudación la
                # resuelve el siguiente despacho reutilizando el mismo efecto.
                operaciones.append(estado.Escritura(
                    ruta_paquete(paquete), con_estado(actual, "listo")))
            return self._transicion(
                "runtime.lease.liberado", revision, operaciones,
                "liberación de la autoridad sobre " + paquete,
                {"paquete": paquete, "epoca": lease["epoca"]},
            )

        self._aplicar("runtime.lease.liberado", construir,
                      descripcion="liberación del lease de " + paquete)
        return None

    # =====================================================================
    #  3 · derivar trabajo elegible DEL ESTADO
    # =====================================================================
    def _dependencias_pendientes(self, paquete):
        """`(pendientes, inviables)` — las dos listas que `b.8` distingue."""
        pendientes, inviables = [], []
        for dependencia in paquete["depende_de"]:
            otro = self._leer_paquete_opcional(dependencia)
            if otro is None:
                raise RuntimeInconsistente(
                    "el paquete depende de `" + str(dependencia) + "`, que no existe en "
                    "la revisión vigente: ninguna regla dice cómo esperar a algo que no "
                    "está", ruta=paquete["id"],
                )
            if otro["estado"] == "completado":
                continue
            if otro["estado"] in ("cancelado", "agotado"):
                # `b.8`: una espera que deja de ser viable DEBE convertirse en bloqueo. No
                # puede quedarse muerta esperando a algo que ya no va a completarse.
                inviables.append(dependencia)
            else:
                pendientes.append(dependencia)
        return pendientes, inviables

    def elegibles(self):
        """El trabajo elegible, DERIVADO del estado y ordenado igual para toda instancia.

        Se ordena por prioridad descendente y después por identificador. Que dos instancias
        vean exactamente la misma lista es lo que hace que la carrera por un paquete sea
        real, y no un accidente del orden en que cada una leyó el directorio.
        """
        self._exigir_operable()
        salida = []
        for paquete in self._todos_los_paquetes():
            if paquete["estado"] == "esperando-dependencia":
                pendientes, inviables = self._dependencias_pendientes(paquete)
                if pendientes and not inviables:
                    continue
            elif paquete["estado"] != "listo":
                continue
            lease = self._leer_lease(paquete["id"])
            salida.append({
                "paquete": paquete["id"],
                "item": paquete["item"],
                "estado": paquete["estado"],
                "prioridad": paquete["prioridad"],
                "capacidades_requeridas": list(paquete["capacidades_requeridas"]),
                "intentos": paquete["intentos"],
                "max_intentos": paquete["max_intentos"],
                "depende_de": list(paquete["depende_de"]),
                "titular": lease["titular"] if lease else None,
            })
        salida.sort(key=lambda e: (-e["prioridad"], e["paquete"]))
        return salida

    # =====================================================================
    #  6 · seleccionar adaptador · 7 · ejecutar · 8 · registrar · 15 · no repetir
    # =====================================================================
    def _seleccionar(self, paquete):
        if self.registro is None:
            raise CapacidadNoSoportada(
                "este runtime no tiene registro de adaptadores: se inyecta en el "
                "constructor (`registro_de_adaptadores=`)",
                ruta=paquete["id"],
                requeridas=sorted(paquete["capacidades_requeridas"]),
            )
        adaptador = self.registro.seleccionar(list(paquete["capacidades_requeridas"]))
        return comprobar_adaptador(adaptador, list(paquete["capacidades_requeridas"]))

    def _abrir_intento(self, paquete, lease):
        """`listo` → `despachado`: consume un intento y FIJA el efecto de ese intento."""
        escrito = {}

        def construir(revision):
            actual = self._leer_paquete(paquete)
            vigente = exigir_titularidad(self._leer_lease(paquete), self.instancia,
                                         lease["epoca"], paquete=paquete)
            if actual["estado"] != "listo":
                raise EstadoDePaqueteInvalido(
                    "el paquete dejó de estar `listo` mientras se abría el intento: "
                    "ahora está `" + actual["estado"] + "`", ruta=paquete,
                )
            intento = int(actual["intentos"]) + 1
            nuevo = con_estado(
                actual, "despachado",
                intentos=intento,
                efecto=derivar_efecto(actual["orden"], paquete, intento),
                resultado=None,
            )
            escrito["paquete"] = nuevo
            return self._transicion(
                "runtime.paquete.despachado", revision,
                [estado.Escritura(ruta_paquete(paquete), nuevo),
                 estado.Escritura(ruta_lease(paquete), con_latido(vigente))],
                "apertura del intento " + str(intento) + " de " + str(nuevo["max_intentos"]),
                {"paquete": paquete, "intento": intento, "efecto": nuevo["efecto"]},
            )

        self._aplicar("runtime.paquete.despachado", construir,
                      descripcion="apertura de intento de " + paquete)
        return escrito["paquete"]

    def _marcar_ejecutando(self, paquete, lease):
        escrito = {}

        def construir(revision):
            actual = self._leer_paquete(paquete)
            vigente = exigir_titularidad(self._leer_lease(paquete), self.instancia,
                                         lease["epoca"], paquete=paquete)
            if actual["estado"] == "ejecutando":
                escrito["paquete"] = actual
                return None
            nuevo = con_estado(actual, "ejecutando")
            escrito["paquete"] = nuevo
            return self._transicion(
                "runtime.paquete.ejecutando", revision,
                [estado.Escritura(ruta_paquete(paquete), nuevo),
                 estado.Escritura(ruta_lease(paquete), con_latido(vigente))],
                "inicio de la ejecución del intento " + str(nuevo["intentos"]),
                {"paquete": paquete, "intento": nuevo["intentos"]},
            )

        self._aplicar("runtime.paquete.ejecutando", construir,
                      descripcion="inicio de ejecución de " + paquete)
        return escrito["paquete"]

    def _publicar_resultado(self, paquete, lease, efecto, resultado, estado_final):
        """UNA transición escribe resultado, ACUSE y latido: o se ven los tres, o ninguno.

        Ésta es la pieza que hace que un efecto confirmado no se aplique dos veces. El
        acuse `efectos/<efecto>.json` y el `paquetes/<id>.json` con su resultado viajan en
        la misma `Transicion`, y el §3 del contrato del motor garantiza que una transacción
        multiarchivo se observa entera o no se observa.
        """
        escrito = {}

        def construir(revision):
            # GUARDA, reevaluada en cada vuelta y en este orden:
            #  1 · ¿sigo siendo el titular de la misma época?   → si no, AutoridadPerdida
            #  2 · ¿el acuse del efecto ya existe?              → si sí, no se escribe nada
            #  3 · ¿el paquete sigue donde lo dejé?             → si no, error tipado
            vigente = exigir_titularidad(self._leer_lease(paquete), self.instancia,
                                         lease["epoca"], paquete=paquete)
            acuse_previo = self._leer_acuse(efecto, paquete=paquete)
            if acuse_previo is not None:
                escrito["acuse"] = acuse_previo
                escrito["paquete"] = self._leer_paquete(paquete)
                return None
            actual = self._leer_paquete(paquete)
            if actual["estado"] != "ejecutando":
                raise EstadoDePaqueteInvalido(
                    "el paquete debía estar `ejecutando` para acusar su efecto y está `"
                    + actual["estado"] + "`", ruta=paquete,
                )
            if actual["efecto"] != efecto:
                raise RuntimeInconsistente(
                    "el paquete cambió de efecto mientras se ejecutaba: se ejecutó `"
                    + efecto + "` y ahora declara `" + str(actual["efecto"]) + "`",
                    ruta=paquete,
                )
            nuevo = con_estado(actual, estado_final, resultado=dict(resultado))
            acuse = nuevo_acuse(efecto=efecto, paquete=paquete,
                                intento=actual["intentos"], resultado=dict(resultado))
            escrito["paquete"] = nuevo
            escrito["acuse"] = acuse
            return self._transicion(
                "runtime.efecto.acusado", revision,
                [estado.Escritura(ruta_paquete(paquete), nuevo),
                 estado.Escritura(ruta_efecto(efecto), acuse),
                 estado.Escritura(ruta_lease(paquete), con_latido(vigente))],
                "resultado `" + estado_final + "` del intento " + str(actual["intentos"])
                + " y acuse durable del efecto " + efecto,
                {"paquete": paquete, "efecto": efecto, "estado": estado_final},
            )

        self._aplicar("runtime.efecto.acusado", construir,
                      descripcion="acuse del efecto " + efecto)
        return escrito["paquete"], escrito["acuse"]

    def _soltar_si_es_mio(self, paquete):
        """Suelta la autoridad si todavía es nuestra. `AutoridadPerdida` ya no hay qué soltar."""
        try:
            self.liberar(paquete)
        except AutoridadPerdida:
            # Otro la reclamó mientras fallábamos. No hay nada que soltar, y volver a
            # escribir sería pisar al titular vigente.
            return None
        return None

    def despachar(self, paquete):
        """Selecciona adaptador y EJECUTA, bajo autoridad y sin repetir un efecto acusado."""
        self._exigir_operable()
        self._exigir_no_marcado()

        fallos.punto("antes-de-adquirir")
        lease = self.adquirir(paquete)
        fallos.punto("despues-de-adquirir")
        try:
            return self._despachar_con_autoridad(paquete, lease)
        except AutoridadPerdida:
            # NO se escribe NADA, ni siquiera para soltar el lease: ya es de otro.
            raise
        except FALLOS_ANTES_DE_EJECUTAR:
            # Nada se ha ejecutado todavía. Retener la autoridad dejaría el paquete
            # inalcanzable para otra instancia hasta acumular `PACIENCIA` observaciones.
            self._soltar_si_es_mio(paquete)
            raise

    def _despachar_con_autoridad(self, paquete, lease):
        """El ciclo de despacho propiamente dicho, ya con el lease en la mano."""
        actual = self._leer_paquete(paquete)
        actual = self._resolver_dependencias(paquete, actual, lease)
        adaptador = self._seleccionar(actual)

        if actual["estado"] == "listo":
            actual = self._abrir_intento(paquete, lease)
        elif actual["estado"] not in ESTADOS_EN_CURSO:
            raise EstadoDePaqueteInvalido(
                "un paquete en `" + actual["estado"] + "` no se despacha; la tabla del "
                "§4.2 no lleva de ahí a `despachado`", ruta=paquete,
            )

        efecto = actual["efecto"]
        acuse = self._leer_acuse(efecto, paquete=paquete)
        if acuse is not None:
            # 15 · NO REPETIR UN EFECTO CONFIRMADO, y 20 · FALLO CERRADO. Llegar aquí con
            # acuse significa ver un acuse durable mientras el paquete sigue `despachado` o
            # `ejecutando`, y eso NO puede haber ocurrido: el acuse y el resultado viajan
            # en la MISMA transición y el §3 del contrato del motor garantiza que una
            # transacción multiarchivo se observa entera o no se observa. Un estado que
            # ninguna regla explica no se despacha «por si acaso»: se denuncia.
            raise RuntimeInconsistente(
                "hay acuse durable del efecto `" + efecto + "` y el paquete sigue en `"
                + actual["estado"] + "`; acuse y resultado se escriben en la misma "
                "transición y no pueden verse por separado",
                ruta=paquete, efecto=efecto, estado=actual["estado"],
            )

        if actual["estado"] == "despachado":
            actual = self._marcar_ejecutando(paquete, lease)

        registro_de_progreso = []

        def progreso(dato):
            fallos.punto("durante-la-ejecucion")
            registro_de_progreso.append(dict(dato))

        fallos.punto("antes-de-ejecutar")
        # El runtime emite su PROPIO evento de progreso al entregar el control. Sin él,
        # `durante-la-ejecucion` sólo sería alcanzable con adaptadores que emitan progreso,
        # y un punto de fallo que depende del adaptador no es un punto del runtime.
        progreso({"fase": "entrega", "adaptador": adaptador.identificador})
        resultado = adaptador.ejecutar(
            actual["orden"], efecto=efecto,
            limite_segundos=actual["orden"]["limite_segundos"],
            progreso=progreso, cancelacion=Cancelacion(self, paquete),
        )
        fallos.punto("despues-del-efecto-antes-del-acuse")

        politica.comprobar_resultado(resultado, efecto=efecto, paquete=paquete)
        clase, error = politica.clasificar(resultado)
        estado_final = politica.estado_de_paquete(clase)
        registro = dict(resultado)
        registro["progreso"] = len(registro_de_progreso)
        actual, _acuse = self._publicar_resultado(
            paquete, lease, efecto, registro, estado_final)
        fallos.punto("despues-del-acuse-antes-de-liberar")

        resumen = self._cerrar(paquete, actual, lease, efecto, registro,
                               repetido=bool(resultado["repetido"]), error=error,
                               clase=clase)
        if error is not None:
            error.contexto.update({
                "paquete": paquete, "intento": resumen["intento"],
                "desenlace": resumen["desenlace"],
            })
            raise error
        return resumen

    # =====================================================================
    #  9 · reintentos · 10 · reconciliación al agotar
    # =====================================================================
    def _cerrar(self, paquete, actual, lease, efecto, resultado, *, repetido,
                error=None, clase=None):
        """Aplica la política al paquete YA cerrado y suelta la autoridad."""
        if clase is None:
            clase = {
                "completado": politica.CLASE_COMPLETADO,
                "cancelado": politica.CLASE_CANCELACION,
                "fallido": (politica.CLASE_REINTENTABLE
                            if (resultado or {}).get("reintentable") else
                            politica.CLASE_DEFINITIVO),
            }.get(actual["estado"])
            if clase is None:
                raise RuntimeInconsistente(
                    "no se puede clasificar un paquete cerrado en `" + actual["estado"]
                    + "`", ruta=paquete,
                )
        decision = politica.decidir(clase, actual)
        reconciliacion = None
        if decision == politica.DECISION_REINTENTAR:
            fallos.punto("antes-de-reintentar")
            actual = self._reintentar(paquete, lease)
            desenlace = DESENLACE_FALLIDO
        elif decision == politica.DECISION_AGOTAR:
            fallos.punto("antes-de-agotar")
            actual, reconciliacion = self._agotar(paquete, lease, clase, error)
            desenlace = DESENLACE_AGOTADO
        else:
            desenlace = (DESENLACE_CANCELADO if actual["estado"] == "cancelado"
                         else DESENLACE_COMPLETADO)

        fallos.punto("antes-de-liberar")
        self.liberar(paquete)
        return {
            "paquete": paquete,
            "instancia": self.instancia,
            "epoca": lease["epoca"],
            "intento": actual["intentos"],
            "max_intentos": actual["max_intentos"],
            "efecto": efecto,
            "estado": actual["estado"],
            "desenlace": desenlace,
            "clase": clase,
            "decision": decision,
            "repetido": bool(repetido),
            "reconciliacion": reconciliacion,
            "resultado": dict(resultado) if isinstance(resultado, dict) else None,
        }

    def _reintentar(self, paquete, lease):
        escrito = {}

        def construir(revision):
            actual = self._leer_paquete(paquete)
            vigente = exigir_titularidad(self._leer_lease(paquete), self.instancia,
                                         lease["epoca"], paquete=paquete)
            if actual["estado"] != "fallido":
                escrito["paquete"] = actual
                return None
            nuevo = con_estado(actual, "listo")
            escrito["paquete"] = nuevo
            return self._transicion(
                "runtime.paquete.reintentado", revision,
                [estado.Escritura(ruta_paquete(paquete), nuevo),
                 estado.Escritura(ruta_lease(paquete), con_latido(vigente))],
                "reintento: intento " + str(actual["intentos"]) + " de "
                + str(actual["max_intentos"]) + " consumido y el fallo es reintentable",
                {"paquete": paquete, "intento": actual["intentos"]},
            )

        self._aplicar("runtime.paquete.reintentado", construir,
                      descripcion="reintento de " + paquete)
        return escrito["paquete"]

    def _agotar(self, paquete, lease, clase, error):
        """`fallido` → `agotado` y, en la MISMA pasada, el registro de `g.9`."""
        escrito = {}

        def construir(revision):
            actual = self._leer_paquete(paquete)
            vigente = exigir_titularidad(self._leer_lease(paquete), self.instancia,
                                         lease["epoca"], paquete=paquete)
            if actual["estado"] == "agotado":
                escrito["paquete"] = actual
                return None
            nuevo = con_estado(actual, "agotado")
            escrito["paquete"] = nuevo
            return self._transicion(
                "runtime.paquete.agotado", revision,
                [estado.Escritura(ruta_paquete(paquete), nuevo),
                 estado.Escritura(ruta_lease(paquete), con_latido(vigente))],
                "agotamiento: " + clase + " tras " + str(actual["intentos"]) + " de "
                + str(actual["max_intentos"]) + " intento(s)",
                {"paquete": paquete, "intento": actual["intentos"], "clase": clase},
            )

        self._aplicar("runtime.paquete.agotado", construir,
                      descripcion="agotamiento de " + paquete)
        actual = escrito["paquete"]
        # A partir de aquí el estado canónico de la UNIDAD DE TRABAJO no se toca más: su
        # salida la decide la autoridad por `resolver_reconciliacion`, y sólo entonces
        # `agotado` → `listo`.
        registro = self._almacen.abrir_reconciliacion(
            producto=os.path.basename(os.path.abspath(self.ruta)) or "control-repo",
            repositorio=REPOSITORIO,
            item=actual["item"],
            intento=int(actual["intentos"]),
            causa=politica.causa_de_reconciliacion(clase, error, actual),
        )
        return actual, registro

    # =====================================================================
    #  11 · pausar · 12 · cancelar · 13 · reanudar
    # =====================================================================
    def _mover(self, paquete, destino, *, motivo, autoridad, clase):
        if not isinstance(motivo, str) or not motivo.strip():
            raise RuntimeInconsistente("una decisión de autoridad sin `motivo` no es auditable")
        if not isinstance(autoridad, str) or not autoridad.strip():
            raise RuntimeInconsistente("una decisión sin `autoridad` no es atribuible")
        self._exigir_operable()
        escrito = {}

        def construir(revision):
            actual = self._leer_paquete(paquete)
            comprobar_transicion(actual["estado"], destino, paquete=paquete)
            nuevo = con_estado(actual, destino)
            escrito["paquete"] = nuevo
            return estado.Transicion(
                tipo=clase, base=revision["revision_id"],
                operaciones=[estado.Escritura(ruta_paquete(paquete), nuevo)],
                autor=autoridad, motivo=motivo,
                id=self._identificador(clase, {"paquete": paquete, "destino": destino,
                                               "autoridad": autoridad, "motivo": motivo},
                                       revision),
            )

        self._aplicar(clase, construir, descripcion=clase + " de " + paquete)
        return escrito["paquete"]

    def pausar(self, paquete, *, motivo, autoridad):
        return self._mover(paquete, "pausado", motivo=motivo, autoridad=autoridad,
                           clase="runtime.paquete.pausado")

    def reanudar(self, paquete, *, motivo, autoridad):
        return self._mover(paquete, "listo", motivo=motivo, autoridad=autoridad,
                           clase="runtime.paquete.reanudado")

    def cancelar(self, paquete, *, motivo, autoridad):
        return self._mover(paquete, "cancelado", motivo=motivo, autoridad=autoridad,
                           clase="runtime.paquete.cancelado")

    # =====================================================================
    #  alta de trabajo
    # =====================================================================
    def crear_item(self, *, id, titulo, motivo):
        self._exigir_operable()
        identificador = id
        escrito = {}

        def construir(revision):
            if self._leer_opcional(ruta_item(identificador)) is not None:
                raise RuntimeInconsistente(
                    "ya existe un item con ese identificador; sobrescribirlo borraría su "
                    "historia sin dejar constancia", ruta=identificador,
                )
            objeto = nuevo_item(identificador=identificador, titulo=titulo)
            escrito["item"] = objeto
            return self._transicion(
                "runtime.item.creado", revision,
                [estado.Escritura(ruta_item(identificador), objeto)], motivo,
                {"item": identificador},
            )

        self._aplicar("runtime.item.creado", construir,
                      descripcion="alta del item " + identificador)
        return escrito["item"]

    def crear_paquete(self, *, id, item, capacidades_requeridas, orden,
                      prioridad=50, max_intentos=politica.MAX_INTENTOS_POR_DEFECTO,
                      depende_de=()):
        self._exigir_operable()
        identificador = id
        escrito = {}

        def construir(revision):
            if self._leer_opcional(ruta_paquete(identificador)) is not None:
                raise RuntimeInconsistente(
                    "ya existe un paquete con ese identificador", ruta=identificador,
                )
            if self._leer_opcional(ruta_item(item)) is None:
                raise RuntimeInconsistente(
                    "el paquete dice pertenecer al item `" + str(item) + "`, que no "
                    "existe en la revisión vigente", ruta=identificador,
                )
            objeto = nuevo_paquete(
                identificador=identificador, item=item,
                capacidades_requeridas=capacidades_requeridas,
                orden=normalizar_orden(orden), prioridad=prioridad,
                max_intentos=max_intentos, depende_de=depende_de,
            )
            comprobar_paquete(objeto, ruta_paquete(identificador))
            escrito["paquete"] = objeto
            return self._transicion(
                "runtime.paquete.creado", revision,
                [estado.Escritura(ruta_paquete(identificador), objeto)],
                "alta del paquete " + identificador + " del item " + str(item),
                {"paquete": identificador, "item": item},
            )

        self._aplicar("runtime.paquete.creado", construir,
                      descripcion="alta del paquete " + identificador)
        return escrito["paquete"]

    # =====================================================================
    #  dependencias (`b.8`)
    # =====================================================================
    def _resolver_dependencias(self, paquete, actual, lease):
        """Aparca, bloquea o deja pasar. Devuelve el paquete tal como queda escrito."""
        if actual["estado"] not in ("listo", "esperando-dependencia"):
            return actual
        pendientes, inviables = self._dependencias_pendientes(actual)
        if inviables:
            destino, clase = "bloqueado", "runtime.paquete.bloqueado"
            motivo = ("la espera dejó de ser viable: " + ", ".join(sorted(inviables))
                      + " no va(n) a completarse")
        elif pendientes:
            if actual["estado"] == "esperando-dependencia":
                raise DependenciaNoResuelta(
                    "sigue esperando a " + ", ".join(sorted(pendientes)), ruta=paquete,
                    pendientes=sorted(pendientes),
                )
            destino, clase = "esperando-dependencia", "runtime.paquete.espera"
            motivo = "espera a " + ", ".join(sorted(pendientes))
        elif actual["estado"] == "esperando-dependencia":
            destino, clase = "listo", "runtime.paquete.desbloqueado"
            motivo = "todas las dependencias están completadas"
        else:
            return actual

        escrito = {}

        def construir(revision):
            vigente_paquete = self._leer_paquete(paquete)
            vigente_lease = exigir_titularidad(self._leer_lease(paquete), self.instancia,
                                               lease["epoca"], paquete=paquete)
            if vigente_paquete["estado"] == destino:
                escrito["paquete"] = vigente_paquete
                return None
            nuevo = con_estado(vigente_paquete, destino)
            escrito["paquete"] = nuevo
            return self._transicion(
                clase, revision,
                [estado.Escritura(ruta_paquete(paquete), nuevo),
                 estado.Escritura(ruta_lease(paquete), con_latido(vigente_lease))],
                motivo, {"paquete": paquete, "destino": destino},
            )

        self._aplicar(clase, construir, descripcion=clase + " de " + paquete)
        resultante = escrito["paquete"]
        if destino == "bloqueado":
            raise DependenciaNoResuelta(
                "el paquete quedó BLOQUEADO: " + motivo, ruta=paquete,
                inviables=sorted(inviables),
            )
        if destino == "esperando-dependencia":
            raise DependenciaNoResuelta(
                "el paquete quedó en `esperando-dependencia`: " + motivo, ruta=paquete,
                pendientes=sorted(pendientes),
            )
        return resultante

    # =====================================================================
    #  14 · recuperarse tras morir · un barrido completo
    # =====================================================================
    def ciclo(self, *, maximo=0):
        """Un barrido del dispatcher: sanea lo que quedó a medias y despacha lo elegible."""
        self._exigir_operable()
        self._exigir_no_marcado()
        informe = {
            "instancia": self.instancia,
            "revision_inicial": self._almacen.revision()["revision"],
            "ventana": self._almacen.estado_de_la_ventana(),
            "recuperacion": dict(self.recuperacion or {}),
            "reanudados": [],
            "elegibles": [],
            "atendidos": [],
            "reconciliaciones_pendientes": [],
        }

        # 0 · Autoridad abandonada sobre trabajo ya cerrado (capacidad 17). Un lease
        # nuestro sobre un paquete terminal o `agotado` no gobierna nada: lo dejó ahí una
        # caída entre el acuse y la liberación. Se suelta antes de nada, porque mientras
        # esté puesto ninguna otra instancia puede tomarlo sin observar tres veces.
        informe["liberados"] = []
        for ruta in self._almacen.listar(DOMINIO_LEASES):
            identificador = identificador_de(ruta)
            lease = self._leer_lease(identificador)
            if lease is None or not es_titular(lease, self.instancia):
                continue
            actual = self._leer_paquete_opcional(identificador)
            if actual is None or actual["estado"] in ESTADOS_CERRADOS:
                self._soltar_si_es_mio(identificador)
                informe["liberados"].append(identificador)

        # 1 · Paquetes en `fallido`: la política quedó sin aplicar porque el proceso murió
        # entre el acuse y la decisión. Se aplica ahora, con la autoridad que corresponda.
        for paquete in self._todos_los_paquetes():
            if paquete["estado"] != "fallido":
                continue
            atencion = self._atender_fallido(paquete["id"])
            if atencion is not None:
                informe["atendidos"].append(atencion)

        # 2 · Paquetes en curso cuyo titular somos nosotros o MURIÓ de verdad: se REANUDAN,
        # y la reanudación reutiliza el MISMO efecto, de modo que el acuse —o el recibo del
        # adaptador— impide repetir lo ya aplicado. Cuando el titular murió, la autoridad se
        # toma con `reclamar` y NO con `adquirir`: quitarle el lease a otro es una decisión
        # que tiene que quedar escrita en el diario, con su época subida, y no un efecto
        # colateral de pedir autoridad.
        reanudables = []
        informe["reclamados"] = []
        for paquete in self._todos_los_paquetes():
            if paquete["estado"] not in ESTADOS_EN_CURSO:
                continue
            lease = self._leer_lease(paquete["id"])
            if lease is None or es_titular(lease, self.instancia):
                reanudables.append(paquete["id"])
            elif self._reclamar_si_murio(paquete["id"]):
                reanudables.append(paquete["id"])
                informe["reclamados"].append(paquete["id"])
        informe["reanudados"] = list(reanudables)

        elegibles = [entrada["paquete"] for entrada in self.elegibles()]
        informe["elegibles"] = list(elegibles)

        orden = reanudables + [p for p in elegibles if p not in reanudables]
        if maximo:
            orden = orden[:int(maximo)]
        for identificador in orden:
            informe["atendidos"].append(self._despachar_anotando(identificador))

        informe["revision_final"] = self._almacen.revision()["revision"]
        informe["reconciliaciones_pendientes"] = [
            linea["registro"] for linea in self._almacen.reconciliacion_pendiente()
        ]
        return informe

    def _despachar_anotando(self, paquete):
        """Despacha y ANOTA el desenlace. Sólo se anotan errores de UN paquete concreto."""
        try:
            return self.despachar(paquete)
        except DESENLACES_DE_UN_PAQUETE as error:
            return {
                "paquete": paquete,
                "instancia": self.instancia,
                "desenlace": DESENLACE_OMITIDO,
                "codigo": error.codigo,
                "detalle": error.detalle,
            }

    def _atender_fallido(self, paquete):
        """Un `fallido` sin política aplicada. Exige autoridad: no se toca lo de otro.

        Si el titular MURIÓ de verdad, se le reclama explícitamente antes de pedir la
        autoridad; si sigue vivo o su estado es indecidible, no se atiende y se deja para
        quien corresponda. `adquirir` no roba, así que sin el `reclamar` previo el paquete
        de un titular muerto se quedaría en `fallido` para siempre.
        """
        self._reclamar_si_murio(paquete)
        try:
            lease = self.adquirir(paquete)
        except AutoridadNoDisponible:
            return None
        actual = self._leer_paquete(paquete)
        if actual["estado"] != "fallido":
            self.liberar(paquete)
            return None
        resultado = actual["resultado"] if isinstance(actual["resultado"], dict) else {}
        return self._cerrar(paquete, actual, lease, actual["efecto"], resultado,
                            repetido=True)

    # =====================================================================
    #  18 · vistas DERIVADAS
    # =====================================================================
    def vistas(self, *, eventos_recientes=vistas.EVENTOS_RECIENTES_POR_DEFECTO):
        """Se calculan del estado canónico en cada llamada. NO se persisten (§7.5)."""
        self._exigir_operable()
        derivadas = vistas.derivar(self._almacen, eventos_recientes=eventos_recientes)
        derivadas["instancia"] = self.instancia
        derivadas["marcado"] = self.marcado
        return derivadas

    def estado_de_paquete(self, paquete):
        """El paquete y su lease, leídos del estado canónico. Sin caché y sin adornos."""
        self._exigir_operable()
        actual = self._leer_paquete(paquete)
        lease = self._leer_lease(paquete)
        return {
            "paquete": actual,
            "lease": lease,
            "acuse": self._leer_acuse(actual["efecto"], paquete=paquete),
            "revision": self._almacen.revision()["revision"],
        }
