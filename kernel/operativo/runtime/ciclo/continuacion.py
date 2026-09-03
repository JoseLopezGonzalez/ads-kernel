#!/usr/bin/env python3
"""continuacion — `Continúa` de `§7.4`: los SIETE pasos de `b.14`, ejecutados de verdad.

    **`Continúa` no significa «haz todo lo pendiente»**                          `§7.4`

Ésa es la frase que gobierna el módulo entero, y de ella salen sus dos modos:

    PLAN        pasos 1 a 6. Determinista, sin Owner, y **no toca el estado**. Es el modo
                por defecto, y el que se puede ejecutar dos veces seguidas obteniendo los
                MISMOS bytes y la MISMA revisión.
    EJECUCIÓN   añade el paso 7, y sólo cuando no queda ninguna decisión humana pendiente.
                Con una decisión pendiente levanta `DecisionDelOwnerPendiente` en vez de
                elegir por el Owner.

DECISIÓN · el paso 2 VERIFICA y REPORTA; no repara lo que `g.9` reserva a la AUTORIDAD
    Alternativas: (a) que `Continúa` resuelva sola todo lo que encuentre; (b) que repare lo
    que es suyo y ESCALE lo que no.
    Se elige (b), y la frontera no la traza este módulo: la traza `g.9`, que reserva la
    salida de una reconciliación a una transición explícita de la autoridad, y `§7.3`, que
    manda parar y escalar ante una inconsistencia irresoluble sin decidir. Lo que `Continúa`
    SÍ hace por su cuenta: convertir en bloqueo una espera que dejó de ser viable (`b.8` lo
    ordena), regenerar derivados divergentes y recompilar proyecciones con huella rota
    (`I5`: se recompilan, no se sincronizan). Lo que NO: resolver reconciliaciones, decidir
    la salida de una transacción marcada, y tocar nada cuando hay deriva no transaccional.

DECISIÓN · las DOS ramas del paso 2 se REPORTAN, y quien las ejecuta es el motor
    `§7.4` fija COMPLETAR o MARCAR conflicto, y la reversión acotada a lo especulativo
    local. Las dos ramas están implementadas en `Almacen.recuperar()` y las ejecuta
    `Runtime.abrir()` ANTES de despachar. `Continúa` no las reimplementa: LEE el informe
    (`runtime.recuperacion`) y dice qué rama se tomó, qué transacción y si quedó MARCADA.
    Reimplementarlas aquí sería una segunda recuperación, y la primera regla del corte 2 es
    que no hay un segundo sistema de estado.

DECISIÓN · «vencida» se decide por HUELLA y nunca por reloj
    Una celda de cobertura vence cuando cambia alguno de los identificadores de su sujeto
    (`§9.6`, VIGENCIA), no cuando pasa un plazo. Es la única definición compatible con
    `I-g3`: un plazo exige leer el reloj, y un artefacto derivado que lea el reloj deja de
    dar bytes idénticos entre dos ejecuciones. Y se REPORTA, sin abrir trabajo, que es lo
    que `§7.4` manda con todas las letras.

DECISIÓN · el plan de continuación es DETERMINISTA y no lleva instancia
    El informe no incluye el nombre de la instancia del runtime, ni el `cwd`, ni ninguna
    ruta absoluta. Dos runtimes distintos, en dos directorios distintos, sobre el MISMO
    estado, producen el MISMO plan byte a byte. Si llevara la instancia, la propiedad
    central de `test_continua.py` sería falsa por construcción y habría que debilitarla.
"""
from __future__ import annotations

import json
import os

from estado.errores import ErrorDeEstado, EstadoCorrupto
from estado.serializacion import cid_de_objeto

from . import durable
from .corpus import Corpus
from .errores import DecisionDelOwnerPendiente, DerivaNoTransaccional, TrabajoAmbiguo

DOMINIO_ORDENES = "ordenes"
DOMINIO_DERIVADOS = "derivados"
DOMINIO_COBERTURA = "cobertura"
DOMINIO_PROYECCIONES = "proyecciones"

MODO_PLAN = "plan"
MODO_EJECUCION = "ejecucion"

# Los siete pasos de `b.14`, escritos como DATO para que el informe los recorra en orden y
# ninguno se pueda quedar sin ejecutar en silencio.
PASOS = (
    "1-reconstruir", "2-verificar", "3-consumir", "4-seleccionar",
    "5-reportar", "6-cargar", "7-trabajar",
)

# Los verbos de orden de `b.13` que este módulo sabe consumir. Vocabulario cerrado: una
# orden con otro verbo se REPORTA como no consumible, no se interpreta.
VERBOS = ("pausar", "reanudar", "cancelar")


class Continuacion:
    """`Continúa` sobre un producto existente. Reconstruye, verifica, selecciona y reporta."""

    def __init__(self, runtime, *, corpus=None):
        self.runtime = runtime
        self.corpus = corpus or Corpus()

    @property
    def almacen(self):
        return self.runtime.almacen

    # =====================================================================
    #  paso 1 · RECONSTRUIR
    # =====================================================================
    def reconstruir(self):
        """Lee el estado canónico completo. NO lee el kernel entero, NO lee conversación."""
        almacen = self.almacen
        revision = almacen.revision()
        dominios = {}
        for ruta in almacen.listar():
            dominio = ruta.split("/", 1)[0]
            dominios.setdefault(dominio, []).append(ruta)
        # RECONSTRUIR es LEER, y leer un árbol adulterado tiene que poder terminar: un
        # objeto que la revisión declara y que en disco no está —o que no casa con su
        # `cid`— es DERIVA, y quien la reporta es el paso 2. Si el paso 1 se rompiera al
        # encontrarla, `Continúa` no llegaría nunca a decir qué pasa, que es justo lo que
        # `b.14.3` pide: parar y ESCALAR, no morir.
        ilegibles = []

        def _leer(ruta):
            try:
                return almacen.leer(ruta)
            except ErrorDeEstado as exc:
                ilegibles.append({"ruta": ruta, "codigo": exc.codigo,
                                  "detalle": exc.detalle})
                return None

        paquetes = [p for p in (_leer(r) for r in sorted(dominios.get("paquetes", [])))
                    if p is not None]
        planes = [p for p in (_leer(r) for r in sorted(dominios.get("planes", [])))
                  if p is not None]
        return {
            "revision": revision["revision"],
            "revision_id": revision["revision_id"],
            "cid_raiz": revision["cid_raiz"],
            "dominios": {d: len(rutas) for d, rutas in sorted(dominios.items())},
            "paquetes": {p["id"]: p for p in paquetes},
            "planes": planes,
            "ilegibles": sorted(ilegibles, key=lambda i: i["ruta"]),
            "rutas_por_dominio": {d: sorted(r) for d, r in sorted(dominios.items())},
        }

    # =====================================================================
    #  paso 2 · VERIFICAR
    # =====================================================================
    def verificar(self, reconstruido, *, reparar=False):
        """Las OCHO comprobaciones del paso 2, una a una y ejecutando."""
        hallazgos = []
        acciones = []

        # · ¿hay deriva NO transaccional respecto a HEAD? Se comprueba LO PRIMERO: si el
        #   árbol no casa con su revisión, leer objetos de él propagaría la corrupción.
        deriva = self._deriva_no_transaccional()
        if deriva["hay_deriva"]:
            hallazgos.append({
                "comprobacion": "deriva-no-transaccional",
                "gravedad": "bloqueante",
                "detalle": deriva["detalle"],
                "escala_a": "la autoridad del control repo",
            })

        # · objetos que la revisión declara y el paso 1 no pudo leer. No se traga: es la
        #   misma deriva, vista desde la lectura en vez de desde la verificación.
        for ilegible in reconstruido.get("ilegibles") or []:
            hallazgos.append({
                "comprobacion": "deriva-no-transaccional",
                "gravedad": "bloqueante",
                "detalle": "la revisión declara `" + ilegible["ruta"] + "` y no se puede "
                           "leer (" + ilegible["codigo"] + "): " + ilegible["detalle"],
                "escala_a": "la autoridad del control repo",
            })

        # · ¿existen los artefactos que los paquetes dicen haber producido?
        artefactos = self._artefactos_declarados(reconstruido)
        hallazgos.extend(artefactos["hallazgos"])

        # · efectos ABIERTOS sin acuse: un paquete en curso cuyo intento tiene efecto y
        #   todavía no tiene acuse durable. No es un defecto —es la ventana que el §3 del
        #   contrato del corte 2 declara— y por eso se REPORTA sin escalar; pero se reporta,
        #   porque es exactamente lo que queda tras una muerte a mitad del despacho.
        sin_acuse = self._efectos_sin_acuse(reconstruido)
        if sin_acuse:
            hallazgos.append({
                "comprobacion": "efectos-sin-acuse",
                "gravedad": "informativo",
                "detalle": "paquetes en curso con efecto abierto y sin acuse durable: "
                           + ", ".join(sin_acuse) + ". El acuse del adaptador impide que "
                           "se repita lo ya aplicado",
                "escala_a": None,
            })

        # · handoffs EMITIDOS y sin acusar: hay una entrega esperando a que su receptor
        #   compruebe y tome custodia (`C5`). No bloquea; se dice.
        pendientes_de_acuse = self._handoffs_pendientes()
        if pendientes_de_acuse:
            hallazgos.append({
                "comprobacion": "handoffs-pendientes",
                "gravedad": "informativo",
                "detalle": "entregas emitidas y sin acusar: "
                           + ", ".join(pendientes_de_acuse),
                "escala_a": None,
            })

        # · ¿hay transacciones abiertas? → LAS DOS RAMAS, y no hay una tercera
        ventana = self.almacen.estado_de_la_ventana()
        recuperacion = dict(self.runtime.recuperacion or {})
        rama = recuperacion.get("rama") or "ninguna"
        marcadas = sorted(recuperacion.get("marcadas") or [])
        if rama in ("completar", "revertir", "marcar"):
            acciones.append({
                "comprobacion": "transacciones-abiertas",
                "rama": rama,
                "transaccion": recuperacion.get("transaccion"),
                "detalle": "la recuperación del motor tomó la rama `" + rama + "` ANTES de "
                           "despachar; `Continúa` no la reimplementa, la lee",
            })
        if marcadas:
            hallazgos.append({
                "comprobacion": "transacciones-abiertas",
                "gravedad": "bloqueante",
                "detalle": "hay transacciones MARCADAS: " + ", ".join(marcadas)
                           + ". `g.8` reserva su salida a la AUTORIDAD y no se despacha nada",
                "escala_a": "la autoridad del control repo",
            })

        # · ¿hay `reconciliacion_pendiente`? → resolverla antes de nada
        pendientes = [linea["registro"] for linea in self.almacen.reconciliacion_pendiente()]
        if pendientes:
            hallazgos.append({
                "comprobacion": "reconciliacion-pendiente",
                "gravedad": "bloqueante",
                "detalle": "hay reconciliaciones abiertas y se resuelven ANTES de nada: "
                           + ", ".join(pendientes) + ". `g.9` reserva su salida a una "
                           "transición explícita de la autoridad",
                "escala_a": "la autoridad que `g.9` nombra",
            })

        # · ¿hay derivados divergentes de su `source_revision`? → regenerar
        derivados = self._derivados_divergentes()
        if derivados and reparar:
            acciones.append(self._regenerar_derivados(derivados))
        elif derivados:
            hallazgos.append({
                "comprobacion": "derivados-divergentes",
                "gravedad": "reparable",
                "detalle": "hay derivados cuya fuente cambió: "
                           + ", ".join(d["derivado"] for d in derivados)
                           + ". Se REGENERAN, no se sincronizan (`I5`)",
                "escala_a": None,
            })

        # · ¿hay proyecciones con huella rota? → recompilar
        proyecciones = self._proyecciones_rotas()
        if proyecciones:
            hallazgos.append({
                "comprobacion": "proyecciones-con-huella-rota",
                "gravedad": "reparable",
                "detalle": "; ".join(
                    p["proyeccion"] + ": " + p["diagnostico"] for p in proyecciones
                ) + ". Se RECOMPILAN (`§6.3`)",
                "escala_a": None,
            })

        # · ¿siguen viables todas las `esperando-dependencia`? (`b.8`)
        inviables = self._esperas_inviables(reconstruido)
        if inviables and reparar:
            acciones.append(self._convertir_en_bloqueo(inviables))
        elif inviables:
            hallazgos.append({
                "comprobacion": "esperas-no-viables",
                "gravedad": "reparable",
                "detalle": "esperas que dejaron de ser viables y `b.8` obliga a convertir "
                           "en BLOQUEO: " + ", ".join(sorted(inviables)),
                "escala_a": None,
            })

        # · ¿hay celdas de cobertura vencidas? → SÓLO REPORTAR, no abrir
        vencidas = self._cobertura_vencida()
        if vencidas:
            hallazgos.append({
                "comprobacion": "cobertura-vencida",
                "gravedad": "informativo",
                "detalle": "celdas vencidas por cambio de huella del sujeto: "
                           + ", ".join(vencidas) + ". SÓLO SE REPORTA: no se abre trabajo",
                "escala_a": None,
            })

        return {
            "ventana": ventana,
            "rama_de_recuperacion": rama,
            "transacciones_marcadas": marcadas,
            "artefactos_ausentes": artefactos["ausentes"],
            "efectos_sin_acuse": sin_acuse,
            "handoffs_pendientes": pendientes_de_acuse,
            "reconciliaciones_pendientes": pendientes,
            "derivados_divergentes": [d["derivado"] for d in derivados],
            "proyecciones_rotas": [p["proyeccion"] for p in proyecciones],
            "esperas_no_viables": sorted(inviables),
            "cobertura_vencida": vencidas,
            "hallazgos": sorted(hallazgos, key=lambda h: (h["comprobacion"], h["detalle"])),
            "acciones": acciones,
            "bloqueante": any(h["gravedad"] == "bloqueante" for h in hallazgos),
        }

    def _artefactos_declarados(self, reconstruido):
        """Un paquete `completado` dice haber producido un efecto: su acuse debe estar."""
        ausentes, hallazgos = [], []
        for identificador, paquete in sorted(reconstruido["paquetes"].items()):
            if paquete["estado"] != "completado":
                continue
            efecto = paquete.get("efecto")
            if not efecto:
                hallazgos.append({
                    "comprobacion": "artefactos-declarados",
                    "gravedad": "bloqueante",
                    "detalle": "el paquete `" + identificador + "` está `completado` y no "
                               "declara efecto: no hay forma de saber qué produjo",
                    "escala_a": "la autoridad del control repo",
                })
                ausentes.append(identificador)
                continue
            if self._acuse_ausente(efecto):
                hallazgos.append({
                    "comprobacion": "artefactos-declarados",
                    "gravedad": "bloqueante",
                    "detalle": "el paquete `" + identificador + "` dice haber aplicado el "
                               "efecto `" + efecto + "` y su acuse no está en el estado "
                               "canónico",
                    "escala_a": "la autoridad del control repo",
                })
                ausentes.append(identificador)
        return {"ausentes": sorted(ausentes), "hallazgos": hallazgos}

    def _acuse_ausente(self, efecto):
        """¿Falta el acuse? Un acuse ILEGIBLE cuenta como ausente y no se traga en silencio."""
        try:
            return durable.leer(self.almacen, "efectos/" + efecto + ".json") is None
        except EstadoCorrupto:
            return True

    def _efectos_sin_acuse(self, reconstruido):
        salida = []
        for identificador, paquete in sorted(reconstruido["paquetes"].items()):
            if paquete["estado"] not in ("despachado", "ejecutando"):
                continue
            if paquete.get("efecto") and self._acuse_ausente(paquete["efecto"]):
                salida.append(identificador)
        return salida

    def _handoffs_pendientes(self):
        from .handoffs import DOMINIO as DOMINIO_HANDOFFS, EMITIDO
        salida = []
        for ruta in sorted(self.almacen.listar(DOMINIO_HANDOFFS)):
            entrega = self.almacen.leer(ruta)
            if entrega.get("estado") == EMITIDO:
                salida.append(entrega["instancia"])
        return sorted(set(salida))

    def _deriva_no_transaccional(self):
        """Cambios en el árbol que el diario no explica, y bifurcación respecto a `HEAD`."""
        try:
            self.almacen.verificar_integridad()
        except EstadoCorrupto as exc:
            return {"hay_deriva": True,
                    "detalle": "la verificación de integridad encontró cambios que el "
                               "diario no explica: " + exc.detalle}
        except ErrorDeEstado as exc:
            return {"hay_deriva": True,
                    "detalle": "el estado no se puede verificar: " + exc.detalle}
        ajena = self._revision_en_head()
        if ajena is None:
            return {"hay_deriva": False, "detalle": ""}
        comparacion = self.almacen.detectar_bifurcacion(ajena)
        if comparacion["bifurcada"]:
            return {"hay_deriva": True,
                    "detalle": "la revisión publicada en `HEAD` y la local han BIFURCADO ("
                               + comparacion["relacion"] + "); `g.6` detecta y no decide"}
        return {"hay_deriva": False, "detalle": ""}

    def _revision_en_head(self):
        """`REVISION.json` tal como está en `HEAD`, o `None` si no hay Git o no está.

        DEFECTO QUE CIERRA, encontrado por la auditoría independiente: esto abría su propio
        `subprocess` con `git show`, es decir, una vía de invocación de Git PARALELA al
        canal único de `gobierno/git.py`. Era invisible para el censo de `V6-04` sólo porque
        el censo no barría este paquete; en cuanto lo barrió, apareció. Se corrige donde
        había que corregirlo —usando el canal—, y no declarando una sede de proceso más:
        una excepción por cada sitio que quiera abrir Git acaba con el canal único.
        """
        from gobierno.git import CanalGit
        repo = self.runtime.ruta
        if not os.path.isdir(os.path.join(repo, ".git")):
            return None
        crudo = CanalGit(repo).contenido_de_blob("HEAD", "estado/REVISION.json")
        if not crudo:
            return None
        try:
            return json.loads(crudo.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            # Un `REVISION.json` ilegible en `HEAD` es deriva, y se dice: no se ignora.
            raise DerivaNoTransaccional(
                "el `REVISION.json` publicado en `HEAD` no es JSON legible",
                ruta="estado/REVISION.json",
            )

    def _derivados_divergentes(self):
        divergentes = []
        for ruta in sorted(self.almacen.listar(DOMINIO_DERIVADOS)):
            derivado = self.almacen.leer(ruta)
            fuente = derivado.get("fuente")
            declarada = derivado.get("source_revision")
            if not fuente or not declarada:
                continue
            actual = self.almacen.revision()["raiz"].get(fuente)
            if actual != declarada:
                divergentes.append({
                    "derivado": derivado["id"], "ruta": ruta, "fuente": fuente,
                    "source_revision": declarada, "vigente": actual,
                })
        return divergentes

    def _regenerar_derivados(self, divergentes):
        objetos = {}
        for entrada in divergentes:
            derivado = self.almacen.leer(entrada["ruta"])
            fuente = durable.leer(self.almacen, entrada["fuente"])
            nuevo = dict(derivado)
            nuevo["source_revision"] = entrada["vigente"]
            nuevo["contenido"] = cid_de_objeto(fuente) if fuente is not None else None
            objetos[entrada["ruta"]] = nuevo
        durable.escribir(
            self.almacen, clase="ciclo.derivados.regenerados",
            motivo="regeneración de " + str(len(objetos)) + " derivado(s) divergentes",
            objetos=objetos, semilla=sorted(objetos),
        )
        return {"comprobacion": "derivados-divergentes", "accion": "regenerados",
                "derivados": sorted(e["derivado"] for e in divergentes)}

    def _proyecciones_rotas(self):
        """Proyecciones declaradas en el estado, contrastadas con `adaptadores.proyeccion`."""
        import adaptadores
        rotas = []
        for ruta in sorted(self.almacen.listar(DOMINIO_PROYECCIONES)):
            declarada = self.almacen.leer(ruta)
            fichero = declarada.get("fichero")
            entradas = declarada.get("entradas") or {}
            if not fichero:
                continue
            absoluta = os.path.join(self.runtime.ruta, fichero)
            if not os.path.isfile(absoluta):
                rotas.append({"proyeccion": declarada["id"],
                              "diagnostico": "AUSENTE", "remedio": "recompilar"})
                continue
            with open(absoluta, "r", encoding="utf-8") as manejador:
                texto = manejador.read()
            diagnostico = adaptadores.validar_deriva(texto, entradas)
            if diagnostico["diagnostico"] != adaptadores.AL_DIA:
                rotas.append({"proyeccion": declarada["id"],
                              "diagnostico": diagnostico["diagnostico"],
                              "remedio": diagnostico["remedio"]})
        return rotas

    def _esperas_inviables(self, reconstruido):
        inviables = set()
        paquetes = reconstruido["paquetes"]
        for identificador, paquete in paquetes.items():
            if paquete["estado"] != "esperando-dependencia":
                continue
            for dependencia in paquete["depende_de"]:
                otro = paquetes.get(dependencia)
                if otro is None or otro["estado"] in ("cancelado", "agotado"):
                    inviables.add(identificador)
        return inviables

    def _convertir_en_bloqueo(self, inviables):
        # `_mover` es del `Runtime` y es privado: hoy no hay `bloquear()` público, y
        # escribir aquí la transición sería una SEGUNDA máquina de estados del paquete. Se
        # reutiliza la del runtime —que valida contra la tabla del §4.2— y queda una
        # PETICIÓN DE INTEGRACIÓN para exponerla, que es un cambio fuera de esta zona.
        convertidos = []
        for identificador in sorted(inviables):
            actual = durable.leer(self.almacen, "paquetes/" + identificador + ".json")
            if actual is None or actual["estado"] != "esperando-dependencia":
                continue
            self.runtime._mover(
                identificador, "bloqueado",
                motivo="`b.8`: la espera dejó de ser viable y DEBE convertirse en bloqueo",
                autoridad="DSP", clase="runtime.paquete.bloqueado",
            )
            convertidos.append(identificador)
        return {"comprobacion": "esperas-no-viables", "accion": "convertidas-en-bloqueo",
                "paquetes": convertidos}

    def _cobertura_vencida(self):
        """Vencida = cambió la huella de su sujeto. Sin reloj, por `I-g3`."""
        vencidas = []
        vigente = self.corpus.huella()
        for ruta in sorted(self.almacen.listar(DOMINIO_COBERTURA)):
            celda = self.almacen.leer(ruta)
            declarada = (celda.get("sujeto") or {}).get("revision_de_esquemas_y_contratos")
            if declarada and declarada != vigente:
                vencidas.append(celda["id"])
        return sorted(vencidas)

    # =====================================================================
    #  paso 3 · CONSUMIR
    # =====================================================================
    def consumir(self, *, aplicar=False):
        """Las órdenes pendientes, con su BASE contrastada. Una orden caduca no se aplica."""
        aplicadas, caducas, desconocidas, pendientes = [], [], [], []
        for ruta in sorted(self.almacen.listar(DOMINIO_ORDENES)):
            orden = self.almacen.leer(ruta)
            if orden.get("consumida"):
                continue
            verbo = orden.get("verbo")
            paquete = orden.get("paquete")
            if verbo not in VERBOS:
                desconocidas.append(orden["id"])
                continue
            actual = durable.leer(self.almacen, "paquetes/" + str(paquete) + ".json")
            if actual is None:
                caducas.append(orden["id"])
                continue
            base = orden.get("base")
            vigente = self.almacen.revision()["raiz"].get("paquetes/" + str(paquete) + ".json")
            if base and base != vigente:
                # `entrada:orden` conserva «la base sobre la que se emitió, para detectar
                # que dejó de ser vigente». Una orden emitida sobre otro estado NO se
                # aplica a ciegas: se reporta y espera.
                caducas.append(orden["id"])
                continue
            pendientes.append({"orden": orden["id"], "verbo": verbo, "paquete": paquete})
            if not aplicar:
                continue
            destino = {"pausar": "pausado", "reanudar": "listo", "cancelar": "cancelado"}[verbo]
            if actual["estado"] != destino:
                getattr(self.runtime, verbo)(
                    paquete, motivo=str(orden.get("motivo") or "orden del Owner"),
                    autoridad=str(orden.get("autoridad") or "OWNER"),
                )
            consumida = dict(orden)
            consumida["consumida"] = True
            durable.escribir(
                self.almacen, clase="ciclo.orden.consumida",
                motivo="orden " + orden["id"] + ": " + verbo + " " + str(paquete),
                objetos={ruta: consumida}, semilla={"orden": orden["id"]},
            )
            aplicadas.append(orden["id"])
        return {
            "pendientes": sorted(pendientes, key=lambda o: o["orden"]),
            "aplicadas": sorted(aplicadas),
            "caducas": sorted(caducas),
            "verbo_desconocido": sorted(desconocidas),
        }

    # =====================================================================
    #  paso 4 · SELECCIONAR
    # =====================================================================
    def seleccionar(self, reconstruido, verificacion, *, frente=1):
        """El FRENTE, no todo lo pendiente. Determinista: prioridad y luego identificador."""
        if verificacion["bloqueante"]:
            return {"retoma": [], "motivo": "hay hallazgos bloqueantes en el paso 2 y "
                                            "`b.14.3` manda parar y escalar",
                    "descartados": [], "ambiguo": False}
        elegibles = self.runtime.elegibles()
        if not elegibles:
            return {"retoma": [], "motivo": "no hay trabajo elegible: «no hay trabajo "
                                            "listo» es una respuesta correcta y completa "
                                            "(`b.15`, punto 8)",
                    "descartados": [], "ambiguo": False}
        cabeza = elegibles[: max(1, int(frente))]
        resto = elegibles[max(1, int(frente)):]
        # AMBIGÜEDAD: dos candidatos con la MISMA prioridad y sin dependencia entre ellos no
        # son ambiguos —el identificador desempata y el desempate está en el contrato—. Lo
        # ambiguo es un paquete elegible cuyo plan no lo reconoce: dos lecturas del estado
        # igual de defendibles, y `b.14.3` manda parar.
        conocidos = set()
        for plan in reconstruido["planes"]:
            conocidos.update(plan["paquetes"])
        huerfanos = [e["paquete"] for e in cabeza
                     if conocidos and e["paquete"] not in conocidos]
        return {
            "retoma": [
                {"paquete": e["paquete"], "item": e["item"], "prioridad": e["prioridad"]}
                for e in cabeza
            ],
            "motivo": "prioridad descendente y desempate por identificador, que es lo que "
                      "`gate:despacho-coherente` exige como determinismo",
            "descartados": [
                {"paquete": e["paquete"], "prioridad": e["prioridad"],
                 "motivo": "queda por detrás del frente en el orden determinista"}
                for e in resto
            ],
            "ambiguo": bool(huerfanos),
            "huerfanos": sorted(huerfanos),
        }

    # =====================================================================
    #  paso 5 · REPORTAR   ·   paso 6 · CARGAR
    # =====================================================================
    def reportar(self, reconstruido, verificacion, seleccion, consumo):
        """UNA vez, en pocas líneas. No se pide permiso (`b.14`, nota 2)."""
        vistas = self.runtime.vistas()
        aparcados = [p["paquete"] for p in vistas["que_esta_bloqueado"]
                     if p["estado"] == "pausado"]
        espera_owner = [p["paquete"] for p in vistas["que_espera_decision_del_owner"]]
        inanicion = [
            {"paquete": e["paquete"], "prioridad": e["prioridad"]}
            for e in seleccion["descartados"]
        ]
        return {
            "que_se_esta_construyendo": sorted(
                p["paquete"] for p in vistas["que_se_esta_construyendo"]
            ),
            "que_retoma": [r["paquete"] for r in seleccion["retoma"]],
            "por_que_ese_y_no_otro": seleccion["motivo"],
            "que_espera_decision_del_owner": sorted(espera_owner),
            "que_esta_aparcado": sorted(aparcados),
            "que_esta_en_inanicion": inanicion,
            "ordenes_pendientes": [o["orden"] for o in consumo["pendientes"]],
            "hallazgos": [h["comprobacion"] for h in verificacion["hallazgos"]],
            "recuento": vistas["recuento"],
        }

    def cargar(self, reconstruido, seleccion):
        """Entrega el control a la capacidad con custodia, con su checkpoint (`a.10`)."""
        cargas = []
        for entrada in seleccion["retoma"]:
            plan = None
            for candidato in reconstruido["planes"]:
                if entrada["paquete"] in candidato["paquetes"]:
                    plan = candidato
                    break
            correspondencia = None
            if plan is not None:
                for fila in plan["correspondencia"]:
                    if fila["paquete"] == entrada["paquete"]:
                        correspondencia = fila
                        break
            cargas.append({
                "paquete": entrada["paquete"],
                "item": entrada["item"],
                "capacidad": (correspondencia or {}).get("capacidad"),
                "metodo": (correspondencia or {}).get("metodo"),
                "gate": (correspondencia or {}).get("gate"),
                "obligacion": (correspondencia or {}).get("obligacion"),
                "plan": (plan or {}).get("id"),
                "checkpoint": self._checkpoint(entrada["paquete"]),
            })
        return cargas

    def _checkpoint(self, paquete):
        """El checkpoint del paquete, LEÍDO del estado. No se reconstruye de memoria."""
        actual = durable.leer(self.almacen, "paquetes/" + paquete + ".json")
        if actual is None:
            return None
        return {
            "estado": actual["estado"],
            "intentos": actual["intentos"],
            "max_intentos": actual["max_intentos"],
            "efecto": actual["efecto"],
            "depende_de": list(actual["depende_de"]),
            "based_on": self.almacen.revision()["raiz"].get("paquetes/" + paquete + ".json"),
        }

    # =====================================================================
    #  el plan completo
    # =====================================================================
    def plan(self, *, modo=MODO_PLAN, frente=1, reparar=False, no_interactivo=True):
        """Los siete pasos, en orden. Determinista, y sin tocar el estado en modo PLAN."""
        if modo not in (MODO_PLAN, MODO_EJECUCION):
            raise TrabajoAmbiguo("modo de continuación desconocido: " + repr(modo))
        reconstruido = self.reconstruir()
        verificacion = self.verificar(reconstruido, reparar=reparar and modo == MODO_EJECUCION)
        consumo = self.consumir(aplicar=(modo == MODO_EJECUCION))
        if consumo["aplicadas"] or (verificacion["acciones"] and modo == MODO_EJECUCION):
            # El estado cambió al consumir u ordenar: se RECONSTRUYE, porque seleccionar
            # sobre la lectura vieja elegiría con bytes caducados.
            reconstruido = self.reconstruir()
        seleccion = self.seleccionar(reconstruido, verificacion, frente=frente)
        if seleccion["ambiguo"]:
            raise TrabajoAmbiguo(
                "hay trabajo elegible que ningún plan reconoce: " + ", ".join(seleccion["huerfanos"])
                + "; `b.14.3` manda parar y escalar, y NUNCA inventar estado",
                paquetes=seleccion["huerfanos"],
            )
        reporte = self.reportar(reconstruido, verificacion, seleccion, consumo)
        cargas = self.cargar(reconstruido, seleccion)

        plan = {
            "pasos": list(PASOS),
            "modo": modo,
            "1_reconstruir": {
                "revision": reconstruido["revision"],
                "dominios": reconstruido["dominios"],
                "ilegibles": reconstruido.get("ilegibles") or [],
            },
            "2_verificar": {clave: verificacion[clave] for clave in sorted(verificacion)},
            "3_consumir": consumo,
            "4_seleccionar": seleccion,
            "5_reportar": reporte,
            "6_cargar": cargas,
            "7_trabajar": {"ejecutado": False, "atendidos": []},
            "requiere_decision_del_owner": bool(
                reporte["que_espera_decision_del_owner"] or verificacion["bloqueante"]
            ),
            "no_significa_hacer_todo_lo_pendiente": True,
        }
        if modo == MODO_EJECUCION:
            if plan["requiere_decision_del_owner"] and no_interactivo:
                raise DecisionDelOwnerPendiente(
                    "queda una decisión del Owner y la ejecución es NO INTERACTIVA: "
                    + ", ".join(reporte["que_espera_decision_del_owner"] or
                                [h["comprobacion"] for h in verificacion["hallazgos"]])
                    + ". `Continúa` no elige por el Owner",
                    espera=reporte["que_espera_decision_del_owner"],
                )
            atendidos = []
            from . import despacho
            for carga in cargas:
                atendidos.append(despacho.despachar(
                    self.runtime, carga["paquete"], origen="continua",
                ))
            plan["7_trabajar"] = {
                "ejecutado": True,
                "atendidos": [
                    {"paquete": a.get("paquete"), "desenlace": a.get("desenlace")}
                    for a in atendidos
                ],
            }
        # La huella se calcula SOBRE EL PLAN YA COMPLETO y sin la instancia: dos runtimes
        # distintos sobre el mismo estado dan la misma huella, y por eso comparar dos
        # ejecuciones seguidas es comparar una cadena y no dos informes a ojo.
        plan["huella"] = cid_de_objeto(plan)
        return plan


def como_texto(plan):
    """El reporte del paso 5, en pocas líneas. Determinista y sin rutas de la máquina."""
    reporte = plan["5_reportar"]
    lineas = [
        "construyendo  " + (", ".join(reporte["que_se_esta_construyendo"]) or "(nada)"),
        "retoma        " + (", ".join(reporte["que_retoma"]) or "(nada)"),
        "por que       " + reporte["por_que_ese_y_no_otro"],
        "espera owner  " + (", ".join(reporte["que_espera_decision_del_owner"]) or "(nadie)"),
        "aparcado      " + (", ".join(reporte["que_esta_aparcado"]) or "(nada)"),
        "inanicion     " + (", ".join(
            i["paquete"] for i in reporte["que_esta_en_inanicion"]) or "(nada)"),
        "hallazgos     " + (", ".join(reporte["hallazgos"]) or "(ninguno)"),
    ]
    return lineas
