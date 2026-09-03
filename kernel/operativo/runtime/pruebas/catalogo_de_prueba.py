#!/usr/bin/env python3
"""catalogo_de_prueba — el CATÁLOGO DE MODELOS que un proyecto declararía en su `PROFILE.md`.

NO es un mock: es material del PROYECTO. `C2` sitúa el adaptador entre perfiles y modelos
reales «en el PROFILE del proyecto o en la instalación, NUNCA en el kernel», de modo que un
control repo de prueba tiene que traer el suyo igual que trae su `SOURCES.toml`. Lo que este
módulo escribe es un `PROFILE.md` de verdad, que el runtime lee de verdad, con el analizador
de bloques de verdad. Nada se sustituye ni se simula.

LOS IDENTIFICADORES SON NEUTROS Y EVIDENTEMENTE INVENTADOS —`modelo:alfa`, `modelo:beta`,
`modelo:gamma`, `modelo:delta`, `modelo:epsilon`—, porque `K0.8` prohíbe que un nombre
comercial aparezca en `kernel/` o en `packs/`, y estas pruebas viven en `kernel/`.

Los CINCO están calibrados para que cada motivo de descarte de `C2` tenga un caso vivo:

    modelo:alfa      cumple todo, y su coste está POR ENCIMA de casi todos los techos
    modelo:beta      todo al tope salvo `critica`, que se queda en `alto`  → descarte por EJE
    modelo:gamma     cumple todo menos la herramienta `lectura de imágenes` → descarte por HERRAMIENTA
    modelo:delta     cumple todo pero su contexto es `amplio`              → descarte por CONTEXTO
    modelo:epsilon   cumple todo, y su coste queda dentro de más techos que el de `alfa`

Las herramientas se DERIVAN de los perfiles reales del corpus: si mañana un perfil del
kernel exige una herramienta nueva, el catálogo la trae sin que nadie lo edite, y los
descartes siguen midiendo lo que dicen medir.
"""
from __future__ import annotations

import os

HERRAMIENTA_DE_VISION = "lectura de imágenes"


def herramientas_del_kernel(corpus):
    """La UNIÓN de las herramientas que declaran los perfiles del corpus, ordenada."""
    todas = set()
    for perfil in corpus.de_tipo("perfil-agente"):
        todas.update(str(h) for h in (perfil.get("herramientas") or []))
    return tuple(sorted(todas))


def _tope(politica, eje):
    return politica.tope(eje)


def modelos(politica, corpus):
    """Los cinco modelos del catálogo, con sus siete ejes derivados de la escala real."""
    herramientas = list(herramientas_del_kernel(corpus))
    sin_vision = [h for h in herramientas if h != HERRAMIENTA_DE_VISION]
    todo_al_tope = {eje: _tope(politica, eje) for eje in politica.ejes}
    critica_baja = dict(todo_al_tope)
    # Un escalón por debajo del tope en `critica`: se toma de la escala, no se escribe.
    critica_baja["critica"] = politica.niveles["critica"][-2]
    return [
        {"id": "modelo:alfa", "ofrece": dict(todo_al_tope), "contexto": "maximo",
         "herramientas": herramientas, "coste": "sin-techo"},
        {"id": "modelo:beta", "ofrece": critica_baja, "contexto": "maximo",
         "herramientas": herramientas, "coste": "minimo"},
        {"id": "modelo:gamma", "ofrece": dict(todo_al_tope), "contexto": "maximo",
         "herramientas": sin_vision, "coste": "contenido"},
        {"id": "modelo:delta", "ofrece": dict(todo_al_tope), "contexto": "amplio",
         "herramientas": herramientas, "coste": "contenido"},
        {"id": "modelo:epsilon", "ofrece": dict(todo_al_tope), "contexto": "maximo",
         "herramientas": herramientas, "coste": "alto"},
    ]


def bloque(modelo):
    """Un bloque ```yaml ads:modelo```: el ESPEJO del esquema `perfil-agente`."""
    lineas = ["```yaml ads:modelo", "id: " + modelo["id"], "ofrece:"]
    for eje in sorted(modelo["ofrece"]):
        lineas.append("  " + eje + ": " + str(modelo["ofrece"][eje]))
    lineas.append("contexto: " + modelo["contexto"])
    lineas.append("herramientas:")
    for herramienta in modelo["herramientas"]:
        lineas.append("  - " + herramienta)
    lineas.append("coste: " + modelo["coste"])
    lineas.append("```")
    return "\n".join(lineas)


def texto(politica, corpus, *, seleccion=None, quitar_bloques=False):
    """El `PROFILE.md` completo del proyecto, con su catálogo. Bytes deterministas."""
    cabecera = (
        "# PERFIL\n\n"
        "Producto gobernado por el aparato de `F6`.\n\n"
        "## Catálogo de modelos\n\n"
        "El ADAPTADOR de `C2`: la traducción entre los perfiles del kernel y los modelos\n"
        "que este proyecto tiene instalados. Vive aquí y NUNCA en el kernel.\n\n"
    )
    if quitar_bloques:
        return cabecera + "(este proyecto todavía no ha declarado su catálogo)\n"
    elegidos = modelos(politica, corpus)
    if seleccion is not None:
        permitidos = set(seleccion)
        elegidos = [m for m in elegidos if m["id"] in permitidos]
    return cabecera + "\n\n".join(bloque(m) for m in elegidos) + "\n"


def escribir(ruta_control_repo, politica, corpus, **opciones):
    """Escribe el `PROFILE.md` del control repo y devuelve su ruta."""
    destino = os.path.join(ruta_control_repo, "PROFILE.md")
    with open(destino, "w", encoding="utf-8") as manejador:
        manejador.write(texto(politica, corpus, **opciones))
    return destino


def a_medida(politica, exigencias):
    """Un catálogo HOSTIL: un modelo POR PERFIL, a la medida EXACTA de ese perfil y de nadie más.

    Sirve para ejercer la ruptura de una combinación: si cada modelo cumple exactamente uno
    de los dos perfiles y ninguno cumple los dos, `C4` paso 5 tiene que separar el par —la
    combinación es una LICENCIA, no una obligación— y el equipo escrito tiene que quedar
    coherente. Sigue sin ser un mock: son bloques `ads:modelo` reales que el runtime lee con
    su analizador real.

    `a medida EXACTA` importa: si un modelo ofreciera de más, cumpliría también el otro
    perfil, el grupo no se rompería y la prueba mediría otra cosa sin decirlo.
    """
    salida = []
    for nombre, exigencia in sorted(exigencias.items()):
        salida.append({
            "id": "modelo:" + nombre.split("/")[-1].replace("_", "-"),
            "ofrece": {eje: exigencia["ejes"][eje] for eje in politica.ejes},
            "contexto": exigencia["contexto"],
            "herramientas": list(exigencia["herramientas"]),
            "coste": exigencia["coste"],
        })
    return salida


def escribir_a_medida(ruta_control_repo, politica, exigencias):
    """Escribe un `PROFILE.md` con el catálogo hostil de `a_medida`. Devuelve su ruta."""
    cabecera = (
        "# PERFIL\n\n"
        "Producto gobernado por el aparato de `F6`.\n\n"
        "## Catálogo de modelos\n\n"
        "Catálogo A MEDIDA: un modelo por perfil, y ninguno que cumpla dos a la vez.\n\n"
    )
    destino = os.path.join(ruta_control_repo, "PROFILE.md")
    cuerpo = "\n\n".join(bloque(m) for m in a_medida(politica, exigencias))
    with open(destino, "w", encoding="utf-8") as manejador:
        manejador.write(cabecera + cuerpo + "\n")
    return destino
