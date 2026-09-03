#!/usr/bin/env python3
"""admision — VERIFICADOR DE ADMISIÓN del control repo. Cortes `V2`, `V3`, `V4` y `V5`.

Sede de sus puntos: `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` §20.1, filas `V6-01` a
`V6-19`. Reparto por corte, según `docs/canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md` §4:

    V2 · lectura Git segura      `V6-01` `V6-02` `V6-03` `V6-04`   → `lectura.py`, `censo.py`
    V3 · admisión por MUTACIÓN   `V6-05` … `V6-09`                 → `mutacion.py`
    V4 · auto-inclusión          `V6-10` `V6-11` `V6-12`           → `perimetro.py`, `censo.py`
    V5 · matriz adversarial      `V6-13` `V6-14` `V6-17` `V6-18` `V6-19`
                                                                  → `matriz.py`, `formulas.py`

**LOS DOS QUE FALTABAN, Y DÓNDE VIVEN AHORA.** El macrobloque 3 los construyó, y este
paquete deja de declararlos fuera de alcance:

    `V6-15`  el DERIVADOR de los árboles adversariales de §20.5, con su suite de regresión,
             su matriz de cuatro columnas y su control del control, en `arboles/`. El
             conjunto se DERIVA de las cabeceras que los gates publicaron; no se enumera.
    `V6-16`  la RAÍZ EXTERNA, en el PAQUETE SEPARADO `kernel/operativo/raiz-externa/`, que
             se instala FUERA del árbol verificado, corre como proceso propio con identidad
             sin permiso de escritura, y firma con `ssh-keygen -Y` y Ed25519.

**Ninguno de los dos está CERTIFICADO**: implementado y probado no es certificado, y la
certificación de `F6` la emite un juicio independiente.

Uso mínimo:

    import admision
    declaracion = admision.Declaracion(ancla="<sha de la base>", autoridad="raiz-externa",
                                       admitidas=[{"ruta": "docs/canonico/x.md",
                                                   "motivo": "alta declarada"}])
    veredicto = admision.verificar("/ruta/al/repo", base="<sha>", declaracion=declaracion)
    veredicto.color        # VERDE · ROJO · INDETERMINADO
"""
from __future__ import annotations

import os

from . import censo, formulas, lectura, mutacion, perimetro
from .errores import (
    CensoDeFormulasSucio,
    CensoDeLecturasSucio,
    DatoIlegible,
    ErrorDeAdmision,
    EstructuraAjena,
    GitNoResponde,
    InstrumentoAlterado,
    LecturaInsegura,
    MutacionNoDeclarada,
    SalidaNoDecodificable,
    SalidaTruncada,
    SedeDeFormulaAusente,
    SedeDelOwnerAlterada,
    SinAnclaExterna,
    ZonaSinCondicion,
)
from .lectura import CanalDeLecturaGit
from .perimetro import (
    SEDE_DEL_OWNER,
    Declaracion,
    Hallazgo,
    Perimetro,
    Veredicto,
    Zona,
)

RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Prefijos del INSTRUMENTO. Se leen de la política del gobierno —que es DATO y entra en la
# huella— y no se escriben aquí: dos sedes para la misma lista serían dos verdades.
def prefijos_de_instrumento(politica=None):
    if politica is None:
        from gobierno import propiedad
        politica = propiedad.cargar()
    return politica.prefijos_de_autoinclusion()


def _contenidos_para_append_only(canal, base, rutas):
    """`(bytes en el NACIMIENTO, bytes ahora)` de las sedes append-only que hayan mutado."""
    salida = {}
    for ruta in rutas:
        nacimiento = canal.commit_de_nacimiento(ruta)
        anterior = canal.contenido(nacimiento, ruta) if nacimiento else None
        if anterior is None:
            anterior = canal.contenido(base, ruta)
        actual = canal.contenido("HEAD", ruta)
        if actual is None:
            actual = canal.contenido_en_disco(ruta)
        salida[ruta] = (anterior, actual)
    return salida


def verificar(raiz, *, base, declaracion, registro=censo.REGISTRO_DE_ZONAS,
              politica=None, censar_el_codigo=True):
    """Emite el veredicto de admisión del árbol `raiz` respecto de la revisión `base`.

    Orden de las comprobaciones, y el orden importa:

      0 · `exigir_sede()`. Si la sede de fórmulas compartidas no está, **NO SE EMITE**
          (`V6-19`, criterio de cierre literal). No se calcula con una fórmula propia.
      1 · censo de ZONAS derivado. Una zona sin condición, o una ruta sin zona, es ROJO.
      2 · mutaciones por las CUATRO referencias declaradas (`V6-05` … `V6-09`).
      3 · juicio por la condición de CONTENIDO de la zona de cada ruta (`V6-10`).
      4 · auto-inclusión del instrumento (`V6-11`), que va ANTES que cualquier exención.
      5 · sede del Owner contra el commit de NACIMIENTO (`V6-12`).
      6 · censo de LECTURAS y censo de FÓRMULAS, derivados del código (`V6-04`, `V6-19`).
      7 · ancla EXTERNA (`V6-17`). Sin ella el veredicto es INDETERMINADO, nunca VERDE.
    """
    formulas.exigir_sede()

    raiz = os.path.abspath(raiz)
    canal = CanalDeLecturaGit(raiz)
    zonas = censo.cargar_zonas(raiz, registro)
    instrumento = prefijos_de_instrumento(politica)
    metro = Perimetro(zonas, prefijos_de_instrumento=instrumento)

    base_resuelta = canal.resolver(base)
    rutas = set(canal.rutas_del_arbol("HEAD")) | set(canal.rutas_sin_rastrear())
    censo_de_zonas = metro.censo(rutas)

    hallazgos = []
    for patron in censo_de_zonas["sin_condicion"]:
        hallazgos.append(Hallazgo(
            "V6-10", ZonaSinCondicion.CODIGO, patron, "(clase sin condición)",
            "la zona está declarada en el registro canónico pero su clase no declara "
            "condición de CONTENIDO. Una zona sin condición da ROJO, no pasa por omisión",
        ))
    for ruta in censo_de_zonas["sin_zona"]:
        hallazgos.append(Hallazgo(
            "V6-10", ZonaSinCondicion.CODIGO, ruta, "(sin zona)",
            "ninguna zona del censo derivado clasifica esta ruta",
        ))

    mutaciones = mutacion.derivar(canal, base_resuelta)
    base_conocida = mutacion.preexistentes(canal, base_resuelta)

    append_only = sorted({
        m.ruta for m in mutaciones
        if (metro.zona_de(m.ruta) is not None
            and metro.zona_de(m.ruta).condicion == perimetro.APPEND_ONLY)
        or m.ruta == SEDE_DEL_OWNER
    })
    contenidos = _contenidos_para_append_only(canal, base_resuelta, append_only)
    nacimiento = None
    if SEDE_DEL_OWNER in contenidos:
        nacimiento = contenidos[SEDE_DEL_OWNER][0]

    hallazgos.extend(metro.juzgar(mutaciones, declaracion, contenidos=contenidos,
                                  nacimiento=nacimiento))

    censo_de_lecturas = None
    censo_de_formulas = None
    if censar_el_codigo:
        modulos = censo.modulos_del_aparato(RUNTIME)
        censo_de_lecturas = censo.censar_lecturas(modulos)
        if not censo_de_lecturas["ok"]:
            for entrada in (censo_de_lecturas["fuera_del_canal"]
                            + censo_de_lecturas["listas_fuera_del_canal"]
                            + censo_de_lecturas["sin_separador_seguro"]):
                hallazgos.append(Hallazgo(
                    "V6-04", CensoDeLecturasSucio.CODIGO,
                    entrada["modulo"] + ":" + str(entrada["linea"]),
                    "(censo de lecturas)",
                    "invocación de Git o de proceso fuera del canal único, o lista sin "
                    "`-z`. El censo se deriva del código y no admite vía paralela",
                ))
        censo_de_formulas = formulas.censar_formulas(modulos)
        if not censo_de_formulas["ok"]:
            for entrada in censo_de_formulas["segundas_definiciones"]:
                hallazgos.append(Hallazgo(
                    "V6-19", CensoDeFormulasSucio.CODIGO,
                    entrada["modulo"] + ":" + str(entrada["linea"]),
                    "(censo de fórmulas)",
                    "SEGUNDA definición de la fórmula compartida `" + entrada["formula"]
                    + "` fuera de su sede única, aunque hoy coincida con ella",
                ))

    # `V6-17` · el ancla llega de FUERA. Un digest del propio árbol no prueba nada.
    digest_interno = perimetro.digest_del_censo(zonas)
    indeterminado = False
    try:
        casa = perimetro.exigir_ancla_externa(declaracion, base_resuelta)
        if not casa:
            hallazgos.append(Hallazgo(
                "V6-17", SinAnclaExterna.CODIGO, "(ancla)", "(externa)",
                "el ancla externa declara la revisión " + str(declaracion.ancla)[:12]
                + " y el árbol dice partir de " + base_resuelta[:12]
                + ". El árbol no decide contra qué se le compara",
            ))
    except SinAnclaExterna:
        indeterminado = True

    if declaracion.digest_del_censo and declaracion.digest_del_censo != digest_interno:
        hallazgos.append(Hallazgo(
            "V6-17", SinAnclaExterna.CODIGO, registro, "(censo de zonas)",
            "el censo de zonas del árbol no casa con el que la configuración externa "
            "ancla: el repositorio ha intentado cambiar quién lo clasifica",
        ))

    informe = {
        "base": base_resuelta,
        "mutaciones": [entrada for entrada in mutacion.clasificar(mutaciones, base_conocida)],
        "cobertura_de_letras": mutacion.cobertura_de_letras(mutaciones),
        "censo_de_zonas": censo_de_zonas,
        "censo_de_lecturas": censo_de_lecturas,
        "censo_de_formulas": censo_de_formulas,
        "declaracion": declaracion.a_dict(),
        "digest_del_censo": digest_interno,
        "referencias_declaradas": list(mutacion.LECTURAS_DECLARADAS),
        "instrumento": list(instrumento),
        # Ya no queda ningún punto de §20.1 fuera de alcance. Lo que se publica ahora no es
        # una ausencia sino la PROCEDENCIA de los dos que faltaban, para que un lector pueda
        # ir a ejecutarla en vez de creerse esta línea. `fuera_de_alcance` se conserva —vacío
        # y no borrado— porque su ausencia haría indistinguible «no queda nada fuera» de «ya
        # nadie lo publica», que son cosas muy distintas.
        "fuera_de_alcance": {},
        "procedencia_de_los_puntos": {
            "V6-15": "kernel/operativo/runtime/arboles/ · suite.ejecutar() · punto "
                     "ejecutable ads_arboles.py",
            "V6-16": "kernel/operativo/raiz-externa/verificador.py, PAQUETE SEPARADO que "
                     "se instala FUERA del árbol verificado",
        },
    }
    if hallazgos:
        color = "ROJO"
    elif indeterminado:
        color = "INDETERMINADO"
    else:
        color = "VERDE"
    return Veredicto(color, hallazgos, informe)


__all__ = [
    "verificar", "Declaracion", "Veredicto", "Hallazgo", "Perimetro", "Zona",
    "CanalDeLecturaGit", "SEDE_DEL_OWNER", "prefijos_de_instrumento",
    "censo", "formulas", "lectura", "mutacion", "perimetro",
    "ErrorDeAdmision", "LecturaInsegura", "SalidaTruncada", "SalidaNoDecodificable",
    "EstructuraAjena", "GitNoResponde", "CensoDeLecturasSucio", "ZonaSinCondicion",
    "MutacionNoDeclarada", "SedeDelOwnerAlterada", "InstrumentoAlterado",
    "SinAnclaExterna", "SedeDeFormulaAusente", "CensoDeFormulasSucio", "DatoIlegible",
]
