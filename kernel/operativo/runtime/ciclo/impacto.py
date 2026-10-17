"""La ESTACIÓN DE ANÁLISIS DE IMPACTO (Directiva del Owner §5, §32; OWN-ADS-0030–0033).

«Los circuitos no deben asumir que la clasificación inicial conoce ya todo el impacto.» Un
cambio de backend puede introducir un estado visible; un cambio de interfaz puede exigir un
dato o una semántica de dominio; un fix visual puede revelar un patrón roto. La clase con la
que se abrió el encargo fijó qué condiciones de ruta eran verdaderas; si el trabajo revela
otras, el circuito que se está recorriendo YA NO ES el de este trabajo.

Aquí eso deja de ser una opinión. El primer rol que trabaja —o cualquiera después— declara en
su entrega los DISPARADORES que ha visto, con el vocabulario cerrado de §5; cada disparador
nombra la condición de ruta que dispara; y si una condición derivada no está entre las que el
circuito declaró, el plan queda MARCADO: ningún otro paquete del item se toma hasta que el
encargo se replanifique con un circuito que la cubra (`b.1`: cambiar de proceso cuando el
diagnóstico revela materia nueva). La marca es durable y la reacción, automática (§62): no se
sigue construyendo sobre una clasificación que ya se sabe incompleta.

Un `NO APLICA` deja de ser silencio: el circuito dice qué condiciones NO activó (la ruta lo
registra en `no_activadas`), y la única forma de contradecirlo es un disparador declarado.
"""
from __future__ import annotations

from .corpus import CONDICIONES_DE_B16
from .errores import EntregaInvalida

# Los dieciséis disparadores de §5, cada uno con las condiciones de ruta que dispara.
DISPARADORES = {
    # un cambio en backend puede introducir…
    "nuevo-estado-visible": ("C-DIS",),
    "nueva-restriccion": ("C-DIS",),
    "nueva-accion": ("C-DIS",),
    "nuevo-error": ("C-DIS",),
    "nuevo-permiso": ("C-DIS", "C-SEG"),
    "nuevo-flujo": ("C-DIS", "C-USO"),
    "nueva-forma-de-presentar": ("C-DIS",),
    # un cambio de interfaz puede requerir…
    "nuevo-dato": ("C-DOM",),
    "agregacion": ("C-ARQ",),
    "endpoint": ("C-ARQ",),
    "cambio-de-modelo": ("C-DOM", "C-ARQ"),
    "nueva-semantica-de-dominio": ("C-DOM",),
    # un fix aparentemente visual puede revelar…
    "patron-roto": ("C-DIS",),
    "inconsistencia-entre-pantallas": ("C-DIS",),
    "problema-de-accesibilidad": ("C-DIS",),
    "deuda-del-sistema-de-diseno": ("C-DIS",),
}
GRUPOS = {
    "backend": ("nuevo-estado-visible", "nueva-restriccion", "nueva-accion", "nuevo-error", "nuevo-permiso",
                "nuevo-flujo", "nueva-forma-de-presentar"),
    "interfaz": ("nuevo-dato", "agregacion", "endpoint", "cambio-de-modelo", "nueva-semantica-de-dominio"),
    "fix-visual": ("patron-roto", "inconsistencia-entre-pantallas", "problema-de-accesibilidad",
                   "deuda-del-sistema-de-diseno"),
}


def comprobar_vocabulario():
    """Los dieciséis, en tres grupos, y toda condición derivada es una de `b.16`. Es una
    función y no un `assert` de nivel superior: un módulo que trabaja al importarse es un
    punto ejecutable para el inventario de `T330` (medido con `estado/ramas.py`)."""
    fallos = []
    for d, cs in DISPARADORES.items():
        for c in cs:
            if c not in CONDICIONES_DE_B16:
                fallos.append(d + " dispara " + c + ", que no es una condición de b.16")
    if sum(len(v) for v in GRUPOS.values()) != len(DISPARADORES) or len(DISPARADORES) != 16:
        fallos.append("los grupos no suman los dieciséis disparadores de §5")
    return fallos


def evaluar(circuito, declaracion, *, paquete=None):
    """`{disparadores, condiciones_derivadas, cubiertas, no_cubiertas}` de una declaración de
    impacto contra el circuito. Un disparador fuera del vocabulario es una entrega inválida:
    el vocabulario es cerrado para que «impacto» no sea prosa."""
    disparadores = list((declaracion or {}).get("disparadores") or [])
    desconocidos = sorted(str(d) for d in disparadores if d not in DISPARADORES)
    if desconocidos:
        raise EntregaInvalida(
            "entrega.impacto.disparadores: " + ", ".join(desconocidos) + " no están entre los "
            "dieciséis de §5: " + ", ".join(sorted(DISPARADORES)), paquete=paquete,
        )
    declaradas = {str(c) for c in (circuito or {}).get("condiciones_de_ruta") or []}
    derivadas = sorted({c for d in disparadores for c in DISPARADORES[d]})
    return {
        "disparadores": sorted(set(disparadores)),
        "condiciones_derivadas": derivadas,
        "cubiertas": [c for c in derivadas if c in declaradas],
        "no_cubiertas": [c for c in derivadas if c not in declaradas],
        "circuito": (circuito or {}).get("id"),
    }


def marca_del_plan(evaluacion, *, paquete, rol, entrega):
    """La marca durable que va al plan cuando hay condiciones sin cubrir."""
    return {
        "paquete": paquete, "rol": rol, "entrega": entrega,
        "disparadores": evaluacion["disparadores"],
        "condiciones_no_cubiertas": evaluacion["no_cubiertas"],
        "que_hacer": "replanificar el encargo con un circuito que cubra " + ", ".join(evaluacion["no_cubiertas"])
                     + " (b.1: el diagnóstico reveló materia que la clase no preveía)",
    }


def pendiente(plan):
    """La marca vigente de un plan, o None."""
    marca = (plan or {}).get("impacto")
    if marca and marca.get("condiciones_no_cubiertas"):
        return marca
    return None
