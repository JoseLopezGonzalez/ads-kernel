#!/usr/bin/env python3
"""paralelismo — la CONDICIÓN COMPUESTA de `a.5`, y el freno de `a.7`. Etapa 5 del `§7.2`.

    «Dos paquetes se despachan en paralelo sólo si se cumplen LAS SEIS» — `a.5`
    «`escribe` disjunto NUNCA basta por sí solo» — `§7.2`, etapa 5

DEFECTO QUE CIERRA, encontrado por la auditoría independiente. El `§7.2` declara una etapa
—«DSP comprueba la condición COMPUESTA de paralelismo (a.5, seis condiciones); si falla
cualquiera, secuencia»— que NO estaba implementada. Lo que había era un booleano
`secuencial` que encadenaba todos los paquetes con `depende_de`, y encadenar siempre no es
comprobar: da el resultado seguro por el camino de no mirar. Con él, la prohibición central
de `a.5` —que el aislamiento físico por sí solo NUNCA autoriza— no estaba en ninguna parte
del código, porque no había ninguna otra condición que pudiera contradecirla.

DECISIÓN · las seis se evalúan TODAS, y el resultado dice cuáles fallaron
    Alternativas: (a) cortar en la primera que falle; (b) evaluarlas las seis y devolver la
    lista de las incumplidas.
    Se elige (b). `b.12` paso 7 exige EXPLICAR qué se excluyó y por qué, y con (a) el motivo
    publicado dependería del orden en que están escritas: dos paquetes que violan cuatro
    condiciones reportarían sólo una, y quien intentara arreglarlo descubriría las otras tres
    de una en una.

DECISIÓN · el FALLBACK es SECUENCIAR, y una declaración ausente NO se lee como «no toca nada»
    `b.11` lo escribe: «FALLBACK SEGURO = 1 si el runtime NO PUEDE DEMOSTRAR que dos
    paquetes son compatibles». Por eso `integra_en` vacío hace fallar la sexta: no hay
    estrategia de integración DECLARADA, y suponerla sería exactamente lo que ese fallback
    prohíbe. La declaración de acoplamiento escribe listas vacías EXPLÍCITAS, de modo que
    «no toca ningún contrato» sigue siendo distinguible de «nadie lo ha dicho».

DECISIÓN · el aislamiento físico se comprueba en `escribe_ficheros` Y en `escribe_fuentes`
    `E2.2` instrumenta esa componente sin sustituirla: dos paquetes cuyas `escribe_fuentes`
    son disjuntas satisfacen la parte física «sin más análisis», y **las demás componentes
    siguen exigiéndose igual**. Dos paquetes que escriben en sources distintas y tocan el
    mismo contrato NO son paralelizables, y la prueba lo ejerce.
"""
from __future__ import annotations

from .errores import PlanificacionInvalida

# Las SEIS de `a.5`, en el orden en que su fuente las escribe. Su número no se escribe en
# ninguna frase: quien lo necesite mide la tupla.
CONDICIONES = (
    "sin-dependencia-de-salida",
    "escrituras-fisicas-disjuntas-o-aisladas",
    "sin-autoridad-concurrente-sobre-la-misma-decision",
    "sin-contratos-compartidos-incompatibles",
    "versiones-de-entrada-compatibles",
    "estrategia-de-integracion-explicita",
)

# El freno 2 de `a.7`: dos devoluciones por item, y a la tercera se para y se escala.
DEVOLUCIONES_MAXIMAS = 2


def _conjunto(paquete, campo):
    return set((paquete.get("acoplamiento") or {}).get(campo) or [])


def _depende(uno, otro):
    return otro["id"] in set(uno.get("depende_de") or [])


def evaluar(uno, otro):
    """`(paralelizable, [condiciones incumplidas con su motivo])`. Se evalúan LAS SEIS."""
    if uno["id"] == otro["id"]:
        raise PlanificacionInvalida(
            "la condición compuesta de `a.5` se evalúa entre paquetes DISTINTOS; se ha "
            "pedido comparar `" + str(uno["id"]) + "` consigo mismo",
        )
    incumplidas = []

    # 1 · no existe dependencia de salida entre ellos
    if _depende(uno, otro) or _depende(otro, uno):
        incumplidas.append({
            "condicion": CONDICIONES[0],
            "motivo": "uno declara al otro en `depende_de`: hay dependencia de salida",
        })

    # 2 · sus escrituras físicas son disjuntas, o están aisladas
    ficheros = _conjunto(uno, "escribe_ficheros") & _conjunto(otro, "escribe_ficheros")
    fuentes = _conjunto(uno, "escribe_fuentes") & _conjunto(otro, "escribe_fuentes")
    if ficheros or fuentes:
        incumplidas.append({
            "condicion": CONDICIONES[1],
            "motivo": "escriben lo mismo: "
                      + ", ".join(sorted(ficheros | fuentes)),
        })

    # 3 · no poseen autoridad concurrente sobre la misma decisión
    decisiones = _conjunto(uno, "afecta_decisiones") & _conjunto(otro, "afecta_decisiones")
    if decisiones:
        incumplidas.append({
            "condicion": CONDICIONES[2],
            "motivo": "ejercen autoridad sobre la MISMA decisión: "
                      + ", ".join(sorted(decisiones)),
        })

    # 4 · no modifican contratos compartidos de forma incompatible
    #
    # Compartir un contrato NO es compatible por defecto: `a.5` corrige expresamente la
    # lectura contraria, y `E2.2` insiste en que dos paquetes que escriben en sources
    # distintas y tocan el mismo contrato NO son paralelizables. Demostrar compatibilidad
    # es juzgar CONTENIDO, y eso no le toca a DSP: secuencia y lo dice.
    contratos = _conjunto(uno, "afecta_contratos") & _conjunto(otro, "afecta_contratos")
    if contratos:
        incumplidas.append({
            "condicion": CONDICIONES[3],
            "motivo": "tocan contratos COMPARTIDOS y nadie ha demostrado que sea "
                      "compatible: " + ", ".join(sorted(contratos)),
        })

    # 5 · sus versiones de entrada (`based_on`) son compatibles
    #
    # Incompatible es partir de DOS versiones distintas de la MISMA fuente. Partir de la
    # misma versión, o de fuentes distintas, es compatible.
    versiones_uno = {v.split("@", 1)[0]: v for v in _conjunto(uno, "based_on")}
    versiones_otro = {v.split("@", 1)[0]: v for v in _conjunto(otro, "based_on")}
    chocan = sorted(
        fuente for fuente in set(versiones_uno) & set(versiones_otro)
        if versiones_uno[fuente] != versiones_otro[fuente]
    )
    if chocan:
        incumplidas.append({
            "condicion": CONDICIONES[4],
            "motivo": "parten de versiones DISTINTAS de la misma fuente: "
                      + ", ".join(chocan),
        })

    # 6 · existe una estrategia explícita de integración
    sin_estrategia = [p["id"] for p in (uno, otro)
                      if not str((p.get("acoplamiento") or {}).get("integra_en") or "").strip()]
    if sin_estrategia:
        incumplidas.append({
            "condicion": CONDICIONES[5],
            "motivo": "no declaran `integra_en`: " + ", ".join(sin_estrategia)
                      + ". `b.11` fija el FALLBACK SEGURO cuando no se puede DEMOSTRAR "
                        "compatibilidad, y suponer la estrategia sería saltárselo",
        })

    return (not incumplidas), incumplidas


def solo_lo_fisico_no_basta(uno, otro):
    """`True` si las escrituras son disjuntas y AUN ASÍ alguna condición falla.

    Existe para que la prohibición central de `a.5` sea COMPROBABLE y no sólo escrita: «el
    aislamiento físico es una condición NECESARIA, nunca un criterio completo. En ningún
    punto del kernel puede volver a usarse por sí solo para autorizar paralelismo».
    """
    _, incumplidas = evaluar(uno, otro)
    fisicas = [i for i in incumplidas if i["condicion"] == CONDICIONES[1]]
    return not fisicas and bool(incumplidas)


def secuenciar(paquetes):
    """Devuelve `{id: [ids de los que debe esperar]}` aplicando la condición compuesta.

    Un paquete espera a TODO paquete anterior con el que no sea paralelizable. El orden de
    entrada decide quién espera a quién, y por eso `planificacion` lo pasa ya ordenado de
    forma determinista: sin un orden estable, dos ejecuciones producirían grafos distintos.
    """
    espera = {}
    traza = []
    for indice, paquete in enumerate(paquetes):
        anteriores = []
        for previo in paquetes[:indice]:
            paralelizable, incumplidas = evaluar(paquete, previo)
            if not paralelizable:
                anteriores.append(previo["id"])
                traza.append({
                    "paquete": paquete["id"],
                    "espera_a": previo["id"],
                    "incumplidas": [i["condicion"] for i in incumplidas],
                    "motivos": [i["motivo"] for i in incumplidas],
                })
        espera[paquete["id"]] = anteriores
    return espera, traza


# ===========================================================================
#  FRENO 2 de `a.7` · las devoluciones se ACUMULAN
# ===========================================================================
def devoluciones_por_item(almacen):
    """Cuenta las devoluciones que `C5` marcó `cuenta_para_el_freno`, POR ITEM.

    DEFECTO QUE CIERRA: `handoffs.py` escribía `cuenta_para_el_freno` en cada entrega y
    NADIE lo sumaba ni aplicaba el tope. Un contador que nadie lee no es un freno.
    """
    from .handoffs import DOMINIO as DOMINIO_HANDOFFS

    cuenta = {}
    for ruta in sorted(almacen.listar(DOMINIO_HANDOFFS)):
        entrega = almacen.leer(ruta)
        if not entrega.get("cuenta_para_el_freno"):
            continue
        item = str((entrega.get("trazabilidad") or {}).get("item") or "")
        if item:
            cuenta[item] = cuenta.get(item, 0) + 1
    return cuenta


def freno_de_devoluciones(almacen, item):
    """`(frenado, cuenta, motivo)`. Al tercer intento se PARA y se escala; no se recompone."""
    cuenta = devoluciones_por_item(almacen).get(str(item), 0)
    if cuenta < DEVOLUCIONES_MAXIMAS:
        return False, cuenta, ""
    return True, cuenta, (
        "el item `" + str(item) + "` acumula " + str(cuenta) + " devoluciones y el freno "
        "de `a.7` fija el tope en " + str(DEVOLUCIONES_MAXIMAS) + ": no se recompone otra "
        "vez, se PARA y se escala. Un reintento sin tope es un livelock"
    )
