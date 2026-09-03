#!/usr/bin/env python3
"""suite — la SUITE DE REGRESIÓN de `V6-15`, con su matriz de cuatro columnas.

El criterio de cierre de `V6-15` es literal y tiene dos mitades que se miden sobre el MISMO
conjunto de ÁRBOLES: `entrada − suite = ∅` **y** `suite − entrada = ∅`, y cada fixture con su
documento y su cabecera de origen. Este módulo las mide, y además ejecuta la reproducción.

LA MATRIZ, con sus CUATRO COLUMNAS, y ninguna sobra:

    1 · ÁRBOL SANO            la implementación VIGENTE le da VERDE. Sin esta columna, un
                              verificador que diga ROJO a todo pasaría la suite entera
    2 · EL ATAQUE EXISTE      el árbol atacado DIFIERE del sano EN LO QUE EL ATAQUE DICE
                              cambiar. Sin esta columna, un fixture roto se lee como remedio
    3 · LA VERSIÓN VULNERABLE la implementación histórica lo ACEPTA. Sin esta columna, no
        LO ACEPTA             consta que el ataque fuera real contra nada
    4 · LA VIGENTE LO RECHAZA y lo rechaza POR LA PROPIEDAD, que la fila NOMBRA. Un ROJO por
        POR SU PROPIEDAD      otra causa es un aprobado por accidente

Y una QUINTA comprobación, que es el CONTROL DEL CONTROL de la tercera columna: retirado el
INGREDIENTE del ataque, la MISMA versión histórica da ROJO. Sin ella, una versión vulnerable
que devolviera VERDE siempre pasaría por reproducción histórica.

DECISIÓN · la suite se ADJUDICA al conjunto derivado, y no al revés
    El conjunto lo entrega el derivador desde la sede inmutable. La suite declara, fixture a
    fixture, a qué ORDINAL y a qué HALLAZGO pertenece, y el cruce se hace contra lo derivado.
    Si un gate futuro publica otro árbol, la resta `entrada − suite` deja de ser vacía y la
    suite falla EN VERDE hasta que se le añada el fixture: exactamente lo que la condición de
    bloqueo de `V6-15` describe. No hay ningún cardinal escrito que haya que actualizar.

DECISIÓN · un repositorio Git por PAPEL, y no uno mutado tres veces
    SANO, ATACADO y CONTROL POSITIVO viven a la vez. El control del ataque compara SANO
    contra ATACADO byte a byte, y compararlos exige que los dos existan.
"""
from __future__ import annotations

import json
import os
import shutil
import tempfile

import admision
from admision import censo as censo_de_admision
from admision.perimetro import Declaracion, Perimetro
from gobierno.git import CanalGit

from . import ataques as fixtures
from . import derivador
from .errores import ArbolNoCubierto, FixtureSinArbol, ReproduccionInvalida

AUTORIDAD = "raiz-externa-de-la-suite-de-arboles"


def _zona_de(raiz, ruta):
    """La clase de zona que el registro canónico del árbol asigna a una ruta."""
    zonas = censo_de_admision.cargar_zonas(raiz)
    zona = Perimetro(zonas).zona_de(ruta)
    return zona.clase if zona is not None else "(sin zona)"


def _verificar_vigente(raiz, base, *, censar_el_codigo=False):
    """La implementación VIGENTE, con su declaración externa y su ancla."""
    declaracion = Declaracion(ancla=base, autoridad=AUTORIDAD, admitidas=[])
    return admision.verificar(raiz, base=base, declaracion=declaracion,
                              censar_el_codigo=censar_el_codigo)


def cruzar(arboles, ataques=fixtures.ATAQUES):
    """Las DOS restas de `V6-15`, sobre el mismo conjunto de ÁRBOLES."""
    de_la_entrada = {}
    for arbol in arboles:
        de_la_entrada[arbol.ordinal] = arbol
    de_la_suite = {}
    for ataque in ataques:
        de_la_suite.setdefault(ataque.ordinal, []).append(ataque)

    entrada_menos_suite = sorted(set(de_la_entrada) - set(de_la_suite))
    suite_menos_entrada = sorted(set(de_la_suite) - set(de_la_entrada))

    # Segundo cruce, más fino: el HALLAZGO que cada fixture dice cerrar tiene que ser uno de
    # los que el documento del árbol publica. Sin esto, un fixture podría adjudicarse a un
    # árbol correcto por un hallazgo que ese documento no declara.
    hallazgos_ajenos = []
    for ordinal in sorted(set(de_la_suite) & set(de_la_entrada)):
        publicados = set(de_la_entrada[ordinal].hallazgos)
        for ataque in de_la_suite[ordinal]:
            if ataque.hallazgo not in publicados:
                hallazgos_ajenos.append({
                    "fixture": ataque.identificador,
                    "ordinal": ordinal,
                    "hallazgo_declarado": ataque.hallazgo,
                    "hallazgos_publicados": sorted(publicados),
                })

    return {
        "entrada": [arbol.a_dict() for arbol in arboles],
        "suite": [
            {
                "fixture": ataque.identificador,
                "ordinal": ataque.ordinal,
                "hallazgo": ataque.hallazgo,
                "propiedad": ataque.propiedad,
                "punto": ataque.punto,
            }
            for ataque in sorted(ataques, key=lambda a: a.identificador)
        ],
        "entrada_menos_suite": entrada_menos_suite,
        "suite_menos_entrada": suite_menos_entrada,
        "hallazgos_ajenos": hallazgos_ajenos,
        "ok": (not entrada_menos_suite and not suite_menos_entrada
               and not hallazgos_ajenos),
    }


def exigir_cobertura(arboles, ataques=fixtures.ATAQUES):
    """Fallo CERRADO en las dos direcciones. Es el criterio literal de cierre de `V6-15`."""
    cruce = cruzar(arboles, ataques)
    if cruce["entrada_menos_suite"]:
        raise ArbolNoCubierto(
            "la ENTRADA entrega árboles que la suite no reproduce: "
            + ", ".join(cruce["entrada_menos_suite"])
            + ". `entrada − suite` tiene que ser vacío",
            faltan=cruce["entrada_menos_suite"],
        )
    if cruce["suite_menos_entrada"]:
        raise FixtureSinArbol(
            "la SUITE exige árboles que la entrada no entrega: "
            + ", ".join(cruce["suite_menos_entrada"])
            + ". `suite − entrada` tiene que ser vacío",
            sobran=cruce["suite_menos_entrada"],
        )
    if cruce["hallazgos_ajenos"]:
        primero = cruce["hallazgos_ajenos"][0]
        raise FixtureSinArbol(
            "el fixture `" + primero["fixture"] + "` se adjudica el hallazgo `"
            + primero["hallazgo_declarado"] + "`, que el documento del árbol `"
            + primero["ordinal"] + "` no publica",
        )
    return cruce


def _ejecutar_fixture(ataque, directorio, *, censar_el_codigo=False):
    """Las cuatro columnas de un fixture, más el control del control. Repositorios reales."""
    sano = os.path.join(directorio, "sano")
    atacado = os.path.join(directorio, "atacado")
    control = os.path.join(directorio, "control-positivo")

    base_sano = ataque.fundar(sano)
    base_atacado = ataque.fundar(atacado)
    base_control = ataque.fundar(control)

    # COLUMNA 1 · el árbol SANO pasa.
    veredicto_sano = _verificar_vigente(sano, base_sano,
                                        censar_el_codigo=censar_el_codigo)
    if veredicto_sano.color != "VERDE":
        raise ReproduccionInvalida(
            "el árbol SANO del fixture `" + ataque.identificador + "` no da VERDE con la "
            "implementación vigente: la suite estaría midiendo un falso rojo",
            fixture=ataque.identificador,
            hallazgos=[h.a_dict() for h in veredicto_sano.hallazgos],
        )

    canal_atacado = CanalGit(atacado)
    datos = ataque.aplicar(atacado, canal_atacado)
    datos["zona_en_el_sano"] = _zona_de(sano, datos["ruta"])

    # COLUMNA 2 · el ataque EXISTE en el árbol atacado.
    control_del_ataque = ataque.control_del_ataque(sano, atacado, datos)

    # COLUMNA 3 · la versión VULNERABLE lo ACEPTA.
    historico = ataque.version.juzgar(atacado, base_atacado)
    if historico["color"] != "VERDE":
        raise ReproduccionInvalida(
            "la versión histórica `" + ataque.version.identificador + "` NO acepta el "
            "árbol atacado: la reproducción del defecto original no se está produciendo",
            fixture=ataque.identificador, veredicto_historico=historico,
        )

    # CONTROL DEL CONTROL · retirado el ingrediente, la MISMA versión da ROJO.
    canal_control = CanalGit(control)
    datos_control = ataque.aplicar_control_positivo(control, canal_control)
    historico_control = ataque.version.juzgar(control, base_control)
    if historico_control["color"] != "ROJO":
        raise ReproduccionInvalida(
            "la versión histórica `" + ataque.version.identificador + "` da VERDE también "
            "SIN el ingrediente del ataque (" + ataque.version.ingrediente + "): no "
            "distingue el control del mutante, luego no prueba nada",
            fixture=ataque.identificador, veredicto_historico=historico_control,
        )

    # COLUMNA 4 · la VIGENTE lo RECHAZA, y por la propiedad correcta.
    veredicto_atacado = _verificar_vigente(atacado, base_atacado,
                                           censar_el_codigo=censar_el_codigo)
    if veredicto_atacado.color != "ROJO":
        raise ReproduccionInvalida(
            "la implementación vigente NO rechaza el árbol atacado del fixture `"
            + ataque.identificador + "`: es un FALSO VERDE",
            fixture=ataque.identificador, color=veredicto_atacado.color,
        )
    propiedad = ataque.comprobar_propiedad(veredicto_atacado, datos)

    return {
        "fixture": ataque.identificador,
        "ordinal": ataque.ordinal,
        "hallazgo": ataque.hallazgo,
        "punto": ataque.punto,
        "procedencia": {clave: ataque.version.procedencia[clave]
                        for clave in sorted(ataque.version.procedencia)},
        "arbol_sano_pasa": True,
        "el_ataque_existe": {clave: control_del_ataque[clave]
                             for clave in sorted(control_del_ataque)},
        "la_version_vulnerable_lo_acepta": {
            "version": ataque.version.identificador,
            "propiedad_debilitada": ataque.version.propiedad_debilitada,
            "veredicto": historico["color"],
        },
        "control_del_control": {
            "ingrediente_retirado": ataque.version.ingrediente,
            "ruta": datos_control["ruta"],
            "veredicto_de_la_version_vulnerable": historico_control["color"],
        },
        "la_vigente_lo_rechaza": {clave: propiedad[clave] for clave in sorted(propiedad)},
        "ok": True,
    }


def ejecutar(raiz, *, ataques=fixtures.ATAQUES, censar_el_codigo=False, directorio=None):
    """La suite entera: deriva el conjunto, cruza las dos restas y ejecuta la matriz."""
    arboles = derivador.exigir_sin_duplicados(derivador.derivar(raiz))
    validacion = derivador.exigir_validas(raiz, arboles)
    cruce = exigir_cobertura(arboles, ataques)

    propio = directorio is None
    base_temporal = directorio or tempfile.mkdtemp(prefix="ads-arboles-")
    filas = []
    try:
        for ataque in ataques:
            carpeta = os.path.join(base_temporal, ataque.identificador)
            os.makedirs(carpeta, exist_ok=True)
            filas.append(_ejecutar_fixture(ataque, carpeta,
                                           censar_el_codigo=censar_el_codigo))
    finally:
        if propio:
            shutil.rmtree(base_temporal, ignore_errors=True)

    return {
        "esquema": 1,
        "punto": "V6-15",
        "propietario_de_la_especificacion": "SIS",
        "fase_de_la_especificacion": "F4c",
        "fase_de_la_construccion": "F6",
        "sede_del_conjunto": (
            "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md §20.5 · las cabeceras publicadas "
            "por cada gate en su documento inmutable"
        ),
        "validacion_de_la_entrada": validacion,
        "cruce": cruce,
        "matriz": filas,
        "ok": (validacion["ok"] and cruce["ok"]
               and all(fila["ok"] for fila in filas)),
    }


def serializar(informe):
    """La forma PUBLICABLE: JSON con claves ordenadas y sin una sola ruta absoluta."""
    return json.dumps(informe, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
