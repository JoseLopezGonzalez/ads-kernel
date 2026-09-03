#!/usr/bin/env python3
"""cierre — la etapa 8: completar · bloquear · pausar · escalar · continuar · DERIVAR.

`gate:cierre-de-item` tiene siete comprobaciones y `00-OBLIGACIONES-Y-CIERRE.md` tres
reglas duras. Las tres reglas son las que gobiernan este módulo, y se citan porque cada una
tiene aquí un mecanismo:

    1  CANCELAR UN PAQUETE NO RETIRA SU OBLIGACIÓN. Deja la obligación HUÉRFANA mientras
       nadie con autoridad la retire. Cerrar todos los paquetes no resuelve nada por sí
       mismo.
    2  DSP NO RETIRA. Retirar es autoridad semántica. DSP SOLICITA la retirada a quien la
       posee y la registra cuando llega autorizada.
    3  UNA RETIRADA QUE CAMBIA MATERIALMENTE EL RESULTADO activa `b.1`: cambio de proceso o
       item nuevo. Recomponer no puede ser la vía silenciosa para reducir el alcance.

DECISIÓN · el cierre se COMPRUEBA aquí y se DECLARA fuera
    `00-OBLIGACIONES`: «DSP verifica; no declara: la integración la declara el propietario
    global, y la retirada pertenece a la recomposición aprobada». Por eso `cerrar()` exige
    recibir la declaración de integración FIRMADA por el propietario global de la ruta, y no
    la produce. Un cierre que se declarase a sí mismo convertiría a DSP en autoridad
    semántica, que es exactamente lo que `b.5` y `b.9` le niegan.

DECISIÓN · SATISFECHA y RETIRADA se cuentan POR SEPARADO y nunca se suman
    Es la última comprobación del gate —`informe-separa`— y la razón está escrita: «Un
    informe que sume satisfechas y retiradas y lo presente como entregado es un defecto de
    conformidad, no un redondeo». El informe de cierre lleva dos cifras y no lleva total.

DECISIÓN · el TRABAJO DERIVADO nace ENLAZADO, y el enlace es durable y comprobable
    Alternativas: (a) crear el item nuevo y anotar la relación en un texto; (b) crear el
    item nuevo con un objeto `derivacion` durable que nombre origen y destino, y escribirlo
    en la MISMA transición que el plan del item nuevo.
    Se elige (b). Con (a) la relación se pierde en cuanto alguien reescribe el texto, y el
    item derivado queda huérfano de su causa: es el modo de fallo que `DIR` intenta impedir
    con `items-derivados`, cuyo criterio de satisfacción es literalmente «cada consecuencia
    ejecutable está cubierta por un item derivado que enlaza a `DIR` y a la decisión
    concreta que ejecuta». Con (b) el enlace es estado canónico y una prueba lo recorre.
"""
from __future__ import annotations

from estado.serializacion import cid_de_objeto

from . import durable, planificacion
from .errores import (
    CierreBloqueado,
    ObligacionHuerfana,
    RetiradaSinAutoridad,
)

DOMINIO = "cierres"
DOMINIO_DERIVACIONES = "derivaciones"
ESQUEMA = "ads.estado/1"

SATISFECHA = "satisfecha"
RETIRADA = "retirada"
HUERFANA = "huerfana"
ESTADOS_DE_OBLIGACION = (SATISFECHA, RETIRADA, HUERFANA)

# Las salidas del `§7.2`, y ninguna otra palabra vale.
COMPLETADO = "completado"
BLOQUEADO = "bloqueado"
PAUSADO = "pausado"
ESCALADO = "escalado"
CONTINUA = "continua"
SALIDAS = (COMPLETADO, BLOQUEADO, PAUSADO, ESCALADO, CONTINUA)

# `00-OBLIGACIONES`, regla dura 2: DSP no retira, y por eso su nombre no vale como autoridad.
NO_PUEDE_RETIRAR = ("DSP",)


def resolver_obligaciones(plan, *, satisfechas=(), retiradas=()):
    """El estado de cada obligación del proceso: SATISFECHA, RETIRADA o HUÉRFANA."""
    por_satisfacer = {str(s) for s in satisfechas}
    retiros = {}
    for retiro in retiradas:
        identificador = str(retiro.get("obligacion") or "")
        autoridad = str(retiro.get("autoridad") or "").strip()
        if not autoridad:
            raise RetiradaSinAutoridad(
                "la retirada de `" + identificador + "` no identifica quién tuvo autoridad; "
                "`gate:cierre-de-item` lo comprueba en `retirada-con-autoridad`",
                obligacion=identificador,
            )
        if autoridad in NO_PUEDE_RETIRAR:
            raise RetiradaSinAutoridad(
                "`" + autoridad + "` NO retira: retirar es autoridad semántica y DSP no la "
                "tiene (`b.5`, `b.9`). DSP SOLICITA la retirada y la registra cuando llega "
                "autorizada",
                obligacion=identificador, autoridad=autoridad,
            )
        if not str(retiro.get("como_afecta") or "").strip():
            raise RetiradaSinAutoridad(
                "la retirada de `" + identificador + "` no explica CÓMO AFECTA al resultado "
                "perseguido, y el gate lo exige",
                obligacion=identificador,
            )
        retiros[identificador] = {
            "obligacion": identificador,
            "autoridad": autoridad,
            "como_afecta": str(retiro["como_afecta"]),
            "cambia_el_resultado": bool(retiro.get("cambia_el_resultado")),
        }

    resueltas = []
    for obligacion in plan["obligaciones"]:
        identificador = obligacion["id"]
        if identificador in retiros and identificador in por_satisfacer:
            raise CierreBloqueado(
                "la obligación `" + identificador + "` se declara satisfecha Y retirada; "
                "son resultados DISTINTOS y llamarlos igual permite informar de que se "
                "entregó algo que en realidad se eliminó",
                obligacion=identificador,
            )
        if identificador in por_satisfacer:
            estado = SATISFECHA
        elif identificador in retiros:
            estado = RETIRADA
        else:
            estado = HUERFANA
        resueltas.append({
            "obligacion": identificador,
            "capacidad_productora": obligacion["capacidad_productora"],
            "criterio_de_satisfaccion": obligacion["criterio_de_satisfaccion"],
            "autoridad_de_retirada": obligacion["autoridad_de_retirada"],
            "estado": estado,
            "retirada": retiros.get(identificador),
        })
    return resueltas


def informe(plan, resueltas, *, paquetes):
    """Las DOS cifras, por separado y sin sumarlas (`informe-separa`)."""
    satisfechas = [r["obligacion"] for r in resueltas if r["estado"] == SATISFECHA]
    retiradas = [r["obligacion"] for r in resueltas if r["estado"] == RETIRADA]
    huerfanas = [r["obligacion"] for r in resueltas if r["estado"] == HUERFANA]
    abiertos = sorted(
        identificador for identificador, estado in paquetes.items()
        if estado not in ("completado", "cancelado")
    )
    return {
        "item": plan["item"],
        "proceso": plan["proceso"],
        "satisfechas": sorted(satisfechas),
        "retiradas": sorted(retiradas),
        "huerfanas": sorted(huerfanas),
        "paquetes_abiertos": abiertos,
        "cuantas_satisfechas": len(satisfechas),
        "cuantas_retiradas": len(retiradas),
        # No hay `total`, y es a propósito: sumar satisfechas y retiradas y presentarlo como
        # entregado es el defecto de conformidad que `00-OBLIGACIONES` nombra.
    }


class Cierre:
    """Comprueba `gate:cierre-de-item` y escribe la salida. No declara la integración."""

    def __init__(self, runtime, *, corpus=None):
        self.runtime = runtime
        self.corpus = corpus

    @property
    def almacen(self):
        return self.runtime.almacen

    def _paquetes_de(self, plan):
        salida = {}
        for identificador in plan["paquetes"]:
            objeto = durable.leer(self.almacen, "paquetes/" + identificador + ".json")
            salida[identificador] = objeto["estado"] if objeto else "desconocido"
        return salida

    def comprobar(self, plan, *, satisfechas=(), retiradas=(), integracion=None,
                  aprendizaje=None):
        """Las siete comprobaciones de `gate:cierre-de-item`, sobre el estado real."""
        resueltas = resolver_obligaciones(plan, satisfechas=satisfechas,
                                          retiradas=retiradas)
        paquetes = self._paquetes_de(plan)
        resumen = informe(plan, resueltas, paquetes=paquetes)
        fallos = []
        if resumen["paquetes_abiertos"]:
            fallos.append("terminacion: siguen abiertos "
                          + ", ".join(resumen["paquetes_abiertos"]))
        if resumen["huerfanas"]:
            fallos.append("obligaciones-resueltas: huérfanas "
                          + ", ".join(resumen["huerfanas"]))
        firmante = str((integracion or {}).get("propietario_global") or "")
        if firmante != plan["propietario_global"]:
            fallos.append(
                "integracion: la declara el PROPIETARIO GLOBAL `"
                + plan["propietario_global"] + "` y firma `" + (firmante or "(nadie)") + "`"
            )
        elif not str((integracion or {}).get("declaracion") or "").strip():
            fallos.append("integracion: la declaración está vacía")
        if aprendizaje is None or not str(aprendizaje).strip():
            fallos.append("aprendizaje: `learning_candidate` sin resolver; vale `none` o un "
                          "enlace, pero no la ausencia")
        return {"informe": resumen, "obligaciones": resueltas, "fallos": fallos,
                "puede_cerrar": not fallos}

    def cerrar(self, plan, *, satisfechas=(), retiradas=(), integracion=None,
               aprendizaje=None):
        """Cierra el item si el gate lo permite. Si no, FALLA CERRADO y no escribe nada."""
        veredicto = self.comprobar(plan, satisfechas=satisfechas, retiradas=retiradas,
                                   integracion=integracion, aprendizaje=aprendizaje)
        if not veredicto["puede_cerrar"]:
            if veredicto["informe"]["huerfanas"]:
                raise ObligacionHuerfana(
                    "el item NO cierra: obligaciones huérfanas "
                    + ", ".join(veredicto["informe"]["huerfanas"])
                    + ". Un item con todos sus paquetes cancelados y ninguna retirada "
                    "aprobada no puede cerrar nunca",
                    item=plan["item"], huerfanas=veredicto["informe"]["huerfanas"],
                )
            raise CierreBloqueado(
                "el item NO cierra: " + "; ".join(veredicto["fallos"]),
                item=plan["item"], fallos=veredicto["fallos"],
            )
        return self._escribir(plan, veredicto, COMPLETADO,
                              motivo="cierre del item " + plan["item"],
                              integracion=integracion, aprendizaje=aprendizaje)

    def bloquear(self, plan, *, motivo, trabajo_de_reemplazo=None):
        """`b.4 P10`: bloqueado si el trabajo de reemplazo es identificable."""
        veredicto = {"informe": informe(plan, [], paquetes=self._paquetes_de(plan)),
                     "obligaciones": [], "fallos": [str(motivo)], "puede_cerrar": False}
        return self._escribir(plan, veredicto, BLOQUEADO, motivo=str(motivo),
                              trabajo_de_reemplazo=trabajo_de_reemplazo)

    def pausar(self, plan, *, motivo, siguiente_accion):
        """`§12`: completar unidad segura · verificar · persistir · dejar la siguiente acción."""
        if not str(siguiente_accion or "").strip():
            raise CierreBloqueado(
                "una pausa sin la SIGUIENTE ACCIÓN EXACTA escrita no es una pausa: quien "
                "retome tendría que reconstruirla, y `§12` lo prohíbe",
                item=plan["item"],
            )
        veredicto = {"informe": informe(plan, [], paquetes=self._paquetes_de(plan)),
                     "obligaciones": [], "fallos": [], "puede_cerrar": False}
        return self._escribir(plan, veredicto, PAUSADO, motivo=str(motivo),
                              siguiente_accion=str(siguiente_accion))

    def escalar(self, plan, *, motivo, autoridad, posturas=()):
        """`b.14.3`: DSP para y escala. NUNCA inventa estado."""
        if not str(autoridad or "").strip():
            raise CierreBloqueado(
                "escalar exige nombrar la AUTORIDAD a la que se escala", item=plan["item"],
            )
        veredicto = {"informe": informe(plan, [], paquetes=self._paquetes_de(plan)),
                     "obligaciones": [], "fallos": [str(motivo)], "puede_cerrar": False}
        return self._escribir(plan, veredicto, ESCALADO, motivo=str(motivo),
                              autoridad=str(autoridad),
                              posturas=[str(p) for p in posturas])

    def continuar(self, plan, *, motivo):
        """El item sigue vivo: ni cierra, ni bloquea, ni pausa. Se declara para que conste."""
        veredicto = {"informe": informe(plan, [], paquetes=self._paquetes_de(plan)),
                     "obligaciones": [], "fallos": [], "puede_cerrar": False}
        return self._escribir(plan, veredicto, CONTINUA, motivo=str(motivo))

    # ------------------------------------------------------ trabajo derivado
    def derivar(self, plan, *, encuadre_derivado, ruta_derivada, planificador,
                orden_por_capacidad, motivo, equipos=()):
        """Abre TRABAJO DERIVADO sin perder la relación con el item de origen.

        El plan nuevo y la `derivacion` se escriben, y la derivación nombra los dos extremos.
        `enlace_de_derivacion` los recorre, y una prueba comprueba que desde el item nuevo se
        llega al de origen sin leer ningún texto.
        """
        nuevo = planificador.planificar(
            encuadre_derivado, ruta_derivada, equipos=equipos,
            orden_por_capacidad=orden_por_capacidad,
        )
        derivacion = {
            "esquema": ESQUEMA,
            "origen": plan["item"],
            "origen_plan": plan["id"],
            "derivado": nuevo["item"],
            "derivado_plan": nuevo["id"],
            "motivo": str(motivo),
        }
        derivacion["id"] = "dv-" + cid_de_objeto(derivacion).split(":", 1)[-1][:16]
        marcado = dict(nuevo)
        marcado["derivado_de"] = {"item": plan["item"], "plan": plan["id"],
                                  "derivacion": derivacion["id"]}
        marcado["id"] = planificacion._identificador(marcado)
        durable.escribir(
            self.almacen, clase="ciclo.trabajo.derivado",
            motivo="trabajo derivado de " + plan["item"] + ": " + str(motivo),
            objetos={
                DOMINIO_DERIVACIONES + "/" + derivacion["id"] + ".json": derivacion,
                planificacion.ruta_de(marcado["id"]): marcado,
            },
            semilla={"derivacion": derivacion["id"]},
        )
        return {"derivacion": derivacion, "plan": marcado}

    def enlace_de_derivacion(self, item):
        """Desde un item derivado, el item de ORIGEN. Recorre estado, no texto."""
        for ruta in sorted(self.almacen.listar(DOMINIO_DERIVACIONES)):
            derivacion = self.almacen.leer(ruta)
            if derivacion["derivado"] == item:
                return derivacion
        return None

    # ------------------------------------------------------------ escritura
    def _escribir(self, plan, veredicto, salida, *, motivo, **extra):
        if salida not in SALIDAS:
            raise CierreBloqueado("salida fuera del vocabulario cerrado: " + repr(salida))
        cuerpo = {
            "esquema": ESQUEMA,
            "item": plan["item"],
            "plan": plan["id"],
            "proceso": plan["proceso"],
            "propietario_global": plan["propietario_global"],
            "salida": salida,
            "motivo": str(motivo),
            "informe": veredicto["informe"],
            "obligaciones": veredicto["obligaciones"],
            "fallos": veredicto["fallos"],
        }
        for clave in sorted(extra):
            cuerpo[clave] = extra[clave]
        cuerpo["id"] = "ci-" + cid_de_objeto(cuerpo).split(":", 1)[-1][:16]
        durable.escribir(
            self.almacen, clase="ciclo.item." + salida,
            motivo=motivo,
            objetos={DOMINIO + "/" + cuerpo["id"] + ".json": cuerpo},
            semilla={"cierre": cuerpo["id"]},
        )
        return cuerpo
