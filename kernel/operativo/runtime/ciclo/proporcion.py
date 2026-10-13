"""proporcion — cuánta EVIDENCIA exige un trabajo, y qué hace que una devolución sea material.

No es una taxonomía nueva. Las dos preguntas ya tenían respuesta en el corpus y nadie la
aplicaba a la evidencia:

    · CUÁNTO SE COMPRUEBA. Las composiciones de DIS ya declaran su nivel de novedad
      (`diseno/03-ESCALA-DE-NOVEDAD.md`: «Lo que un nivel bajo elimina es la EXPLORACIÓN,
      nunca la comprobación»), pero la comparación de fidelidad (`05-FIDELIDAD.md`), la
      evidencia `superficie-usable` de CNS y el dosier de VER pedían la MISMA matriz —todos
      los entornos del pack × los cinco estados × movimiento × valores— a una retirada de
      un botón y a una pantalla nueva. Medido (La Pesquerapp, `enc-stk-contencion-reorganizar`,
      2026-10-13): ocultar UNA acción produjo una comparación de 144 capturas principales,
      varios motores y 29,39 USD.

    · QUÉ BLOQUEA. `00-CONTRATOS-BASE` ya prohibía «devolver por preferencia», pero «lo
      exigido» incluía cada campo de cada artefacto. Medido (`enc-ped-def-*`, 2026-09-30 a
      10-12): cinco devoluciones sobre cuatro arreglos cuyo código no cambió nunca después
      del primer commit; una era una anotación `no-aplica` en vez de `no`. Y al revés
      (`enc-stk-a1`, 2026-10-12): una pérdida de coste y de liquidación la vieron cuatro
      capas, y cada una la ANOTÓ como «insuficiencia de la capa de PRD» y la pasó aguas
      abajo con su dictamen superado. Las dos caras son el mismo defecto: la materialidad no
      era un dato.

DECISIÓN · el alcance se DERIVA de la composición de DIS del circuito, no se elige
    Alternativas: (a) un campo nuevo en el encargo que alguien rellena; (b) derivarlo de las
    composiciones que el circuito base ya declara, cada una con su nivel de novedad.
    Se elige (b): «bajar el nivel es la forma más silenciosa de abaratar el diseño» (03),
    y un dato que se rellena se rellena a la baja. Quien revisa puede AMPLIAR el modo con
    motivo; nadie puede reducirlo por debajo del derivado.

DECISIÓN · la reducción es de ALCANCE, nunca de gate ni de rol
    Ningún modo omite un gate, un rol o un nivel del circuito (PROFILE §16.3 de La
    Pesquerapp: no se reduce un circuito por ahorro). El modo `focal` sigue exigiendo la
    comparación de fidelidad —`acabado` y `fidelidad` nunca se reutilizan—; la exige sobre
    lo que el cambio TOCA y lo que puede ALTERAR, no sobre todo lo que la pantalla contiene.
"""
from __future__ import annotations

MODO_SIN_SUPERFICIE = "sin-superficie"
MODO_FOCAL = "focal"
MODO_PERIMETRO = "perimetro-completo"
MODO_MATRIZ = "matriz-completa"
ORDEN_DE_MODOS = (MODO_SIN_SUPERFICIE, MODO_FOCAL, MODO_PERIMETRO, MODO_MATRIZ)

# El nivel de novedad que cada composición de DIS declara en `capacidades/DIS/composicion.md`,
# y el modo de evidencia que le corresponde. N0 aplica un patrón vigente; N1 extiende uno;
# N2 o más decide forma nueva y exige la matriz entera de 05-FIDELIDAD.
MODO_POR_COMPOSICION = {
    "composicion:dis-bug-visual": MODO_FOCAL,              # N0 · desviación de un patrón vigente
    "composicion:dis-revision-implementacion": MODO_FOCAL,  # N0 · comprobar lo construido
    "composicion:dis-extension-de-patron": MODO_FOCAL,      # N0
    "composicion:dis-gap-de-diseno": MODO_PERIMETRO,        # N1 · falta una decisión puntual
    "composicion:dis-caso-nuevo": MODO_PERIMETRO,           # N1
    "composicion:dis-nueva-interaccion": MODO_MATRIZ,       # N2
    "composicion:dis-animacion": MODO_MATRIZ,               # N2 · movimiento nuevo
    "composicion:dis-feature-visual": MODO_MATRIZ,          # N2
    "composicion:dis-reconstruccion": MODO_MATRIZ,          # N3
    "composicion:dis-proyecto-nuevo": MODO_MATRIZ,          # N4
}

EXIGE = {
    MODO_SIN_SUPERFICIE: (
        "ninguna evidencia visual: el encargo no cambia lo que el usuario ve",
    ),
    MODO_FOCAL: (
        "la comparación de fidelidad cubre los ELEMENTOS QUE EL DIFF TOCA y los estados cuyo "
        "render depende del código cambiado; los demás estados de la pantalla no se recapturan",
        "dos tamaños: el más estrecho y el más amplio de la matriz, en el motor principal; un "
        "segundo motor sólo si el diff toca composición, CSS o tokens",
        "la evidencia de usabilidad (`superficie-usable`) se produce sólo para los estados y "
        "medios de entrada que el cambio altera; el resto se enlaza a la del patrón vigente",
        "la regresión automática de la fuente se ejecuta ENTERA: es barata y no se recorta",
    ),
    MODO_PERIMETRO: (
        "la comparación cubre los COMPONENTES tocados con TODOS sus estados (los cinco y los "
        "propios), en los tamaños extremos y en todos los motores de la matriz",
        "la evidencia de usabilidad cubre los componentes tocados entera",
        "la regresión automática de la fuente se ejecuta ENTERA",
    ),
    MODO_MATRIZ: (
        "la comparación entera de 05-FIDELIDAD: cada entorno de la matriz, los cinco estados, "
        "movimiento, dispositivo real cuando el pack lo exige y extracción de valores",
        "la evidencia de usabilidad entera de gate:usabilidad",
        "la regresión automática de la fuente se ejecuta ENTERA",
    ),
}

# Lo que obliga a SUBIR el modo aunque la composición diga otro. Lo declara quien revisa; la
# regla es que el modo derivado es un SUELO, nunca un techo.
AMPLIAN = (
    "el diff toca composición de página, contenedores de layout, puntos de adaptación o CSS global",
    "el diff cambia tokens del sistema de diseño o un componente compartido de `ui/` o `Shared/`",
    "el cambio introduce una interacción, un estado o un movimiento que la superficie no tenía",
    "lo construido no coincide con el perímetro que la entrega de CNS declaró",
)


def modo_de_circuito(circuito):
    """El modo de evidencia que el circuito base exige, y de qué composición sale.

    Con varias composiciones de DIS manda la más exigente. Sin ninguna, el circuito no tiene
    Diseño y no hay evidencia visual que pedir (la regresión de la fuente sigue).
    """
    composiciones = [str(c) for c in ((circuito or {}).get("composiciones") or [])]
    candidatas = [(MODO_POR_COMPOSICION[c], c) for c in composiciones if c in MODO_POR_COMPOSICION]
    if not candidatas:
        return MODO_SIN_SUPERFICIE, None
    modo, origen = max(candidatas, key=lambda par: ORDEN_DE_MODOS.index(par[0]))
    return modo, origen


def alcance_de_la_evidencia(circuito):
    """El alcance de la evidencia que un paquete de este circuito debe producir o juzgar."""
    modo, origen = modo_de_circuito(circuito)
    return {
        "modo": modo,
        "derivado_de": origen or "el circuito no declara ninguna composición de DIS",
        "exige": list(EXIGE[modo]),
        "amplian": list(AMPLIAN) if modo != MODO_MATRIZ else [],
        "regla": ("el modo derivado es un SUELO: quien revisa puede ampliarlo con motivo (uno de "
                  "`amplian`), y nadie puede reducirlo. Reducir el alcance no omite ningún gate, "
                  "ningún rol ni ningún nivel del circuito"),
    }


# ---------------------------------------------------------------------------------------------
#  MATERIALIDAD — qué puede bloquear, y qué no puede pasar aguas abajo
# ---------------------------------------------------------------------------------------------
# Una devolución detiene el trabajo y abre un paquete de corrección y otro de revisión. Sólo
# lo justifica una de estas causas. Vocabulario CERRADO, como el de los disparadores de §5:
# para que «material» no sea prosa.
MATERIALIDADES = {
    "criterio-incumplido": "un criterio de éxito o una obligación funcional del encargo no se cumple, con evidencia",
    "prueba-relevante-fallida": "una prueba que protege comportamiento del encargo falla, o un cambio protegido no tiene ninguna prueba que muerda",
    "riesgo-de-seguridad": "una incertidumbre de seguridad, de permisos o de aislamiento entre tenants",
    "perdida-de-datos-o-trazabilidad": "el cambio pierde, corrompe o desvincula datos, costes, trazabilidad o liquidaciones",
    "decision-ajena-cambiada": "lo construido cambia una decisión de PRD, DIS, ARQ o DOM sin haberla devuelto",
    "alcance-excedido": "lo construido toca lo que el encargo no autoriza, sin declararlo",
    "evidencia-imposible-de-juzgar": "falta la evidencia que el alcance EXIGE para juzgar un criterio material, no un campo de forma",
}
# Lo que NO bloquea. Se registra como observación del dictamen y no abre corrección.
NO_MATERIALES = {
    "editorial": "redacción, formato, numeración o una anotación de forma sin efecto en el producto",
    "preferencia": "otra forma igualmente válida de cumplir lo exigido",
    "evidencia-redundante": "evidencia que repite otra vigente sobre la misma revisión, o que el alcance no exige",
    "perfeccionamiento": "una mejora deseable que ningún criterio exige",
}


def materialidad_valida(valor):
    return str(valor or "") in MATERIALIDADES


def es_no_material(valor):
    return str(valor or "") in NO_MATERIALES


# ---------------------------------------------------------------------------------------------
#  RE-REVISIÓN DIFERENCIAL — qué vuelve a juzgar el receptor nuevo tras una corrección
# ---------------------------------------------------------------------------------------------
def revision_diferencial(fila_del_plan):
    """Lo que el brief dice al revisor que sustituye a otro tras una devolución, o None.

    Medido (`enc-ped-def-importes`): las mismas 21 pruebas se revirtieron en cuatro tablas, y
    cada revisión nueva rehízo la anterior entera, porque el brief del receptor nuevo no
    decía que era una RE-revisión ni qué se había devuelto.
    """
    if not (fila_del_plan or {}).get("reemplaza_a"):
        return None
    return {
        "reemplaza_a": fila_del_plan["reemplaza_a"],
        "vuelta": fila_del_plan.get("vuelta"),
        "motivo_devuelto": fila_del_plan.get("motivo_devuelto") or "",
        "correccion": (fila_del_plan.get("depende_de") or [None])[0],
        "que_rejuzgas": (
            "el hallazgo devuelto, y todo lo que el diff de la corrección toca o puede alterar"),
        "que_reutilizas": (
            "el resto del dictamen y de la evidencia de `" + str(fila_del_plan["reemplaza_a"]) + "`, "
            "citándolos, SIEMPRE que se refieran a ficheros que la corrección no cambió; lo "
            "compruebas con git diff entre la revisión juzgada y la corregida"),
        "no_puedes": (
            "abrir hallazgos nuevos bloqueantes sobre lo que la corrección no tocó salvo que "
            "sean materiales y nuevos; si los hay, dilo: el revisor anterior los pasó por alto"),
    }
