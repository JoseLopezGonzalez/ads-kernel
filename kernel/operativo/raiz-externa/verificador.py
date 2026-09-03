#!/usr/bin/env python3
"""verificador — PUNTO EJECUTABLE de la RAÍZ EXTERNA DE CONFIANZA. `V6-16` · `g.15` · `O25`.

    python3 verificador.py capacidades
    python3 verificador.py verificar  --repo <dir> --base <rev> --configuracion <fuera>
                                      --evidencia <fichero FUERA del árbol>
    python3 verificador.py comprobar  --repo <dir> --configuracion <fuera>
                                      --evidencia <fichero>
    python3 verificador.py instalacion --instalacion <dir>

Códigos de salida: 0 éxito · 1 veredicto no favorable o error tipado · 2 uso incorrecto.

QUÉ HACE QUE ESTO SEA UNA RAÍZ EXTERNA, y no un script del repositorio, punto por punto de
`g.15`:

    se EJECUTA FUERA           es un PROCESO propio y un PAQUETE aparte —fuera de
                               `runtime/`—, que `instalar.py` copia a una instalación fuera
                               del árbol verificado, con manifiesto de digests
    identidad SIN ESCRITURA    la identidad que firma no es la del runtime, y `aislamiento.py`
                               DEMUESTRA que no puede escribir en el árbol: lo intenta
    configuración DESDE FUERA  `identidad/configuracion.py` rechaza una configuración que
                               viva dentro del árbol, por los dos caminos de resolución
    entradas VERIFICADAS       el commit y el `tree` se resuelven con Git, y la atestación
                               queda vinculada a los dos
    evidencia FUERA            `--evidencia` se rechaza si cae dentro del árbol verificado
    FALLA CERRADO              sin `ssh-keygen`, sin clave, sin configuración, sin ancla o
                               con una firma que no verifica, NO se emite veredicto favorable
    condiciones DECLARADAS     `capacidades` las publica, con la versión de OpenSSH

DECISIÓN · el `sys.path` apunta a la instalación, NUNCA al árbol verificado
    Es la línea que separa una raíz externa de un script interno. Si este proceso importara
    `admision` desde el árbol que verifica, quien pueda escribir ese árbol decidiría cómo se
    le verifica. El `runtime` se busca como HERMANO de este paquete, que es donde
    `instalar.py` lo deja, y una prueba comprueba que el árbol verificado NO está en la ruta
    de importación.

DECISIÓN · `comprobar` desmiente al árbol, y ése es `G-A9`
    El árbol puede declararse sano: es sólo un fichero suyo. La comprobación contrasta esa
    declaración con la ATESTACIÓN FIRMADA, y cuando discrepan gana la atestación, porque el
    árbol no tiene la clave. `VeredictoDesmentido` es el resultado, y es la demostración de
    `G-A9` sin ninguna pieza simulada.

DECISIÓN · el veredicto INDETERMINADO sale con código 1
    Mismo criterio que `ads_admision.py`: «no he podido afirmar que esté bien» NO es un
    éxito, y darle 0 haría que un `&&` de un guion lo tratara como aprobación.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
INSTALACION = os.path.dirname(AQUI)
RUNTIME_INSTALADO = os.path.join(INSTALACION, "runtime")

sys.path.insert(0, AQUI)
# El runtime de la INSTALACIÓN, jamás el del árbol verificado.
if os.path.isdir(RUNTIME_INSTALADO):
    sys.path.insert(0, RUNTIME_INSTALADO)

import atestacion as modulo_de_atestacion                            # noqa: E402
import firma as modulo_de_firma                                      # noqa: E402
import instalar as modulo_de_instalacion                             # noqa: E402
from errores import (                                                # noqa: E402
    AtestacionInvalida,
    ErrorDeRaizExterna,
    EvidenciaDentroDelArbol,
    FirmaNoVerificada,
    IdentidadNoAceptada,
    VeredictoDesmentido,
)

import admision                                                      # noqa: E402
import identidad                                                     # noqa: E402
from admision.errores import ErrorDeAdmision                         # noqa: E402
from gobierno.errores import ErrorDeGobierno                         # noqa: E402
from gobierno.git import CanalGit                                    # noqa: E402
from identidad.errores import ErrorDeIdentidad                       # noqa: E402

EXITO, FALLO, USO = 0, 1, 2

# El fichero con el que un árbol se declara sano A SÍ MISMO. No tiene ninguna autoridad: es
# la parte FALSEABLE de `G-A9`, y existe para poder desmentirla.
AUTODECLARACION = "estado/operacional/AUTODECLARACION.json"


def _volcar(objeto):
    return json.dumps(objeto, sort_keys=True, ensure_ascii=False, indent=2)


def _uso(mensaje):
    sys.stderr.write("uso: " + mensaje + "\n")
    return USO


def _dentro(candidata, arbol):
    return candidata == arbol or candidata.startswith(arbol + os.sep)


def exigir_evidencia_fuera(ruta, arbol_verificado):
    """`g.13` y `g.15`: la evidencia NO vive dentro del árbol verificado. Dos caminos."""
    arbol = os.path.realpath(arbol_verificado)
    absoluta = os.path.abspath(ruta)
    directorio = os.path.dirname(absoluta) or "."
    por_directorio = os.path.join(os.path.realpath(directorio),
                                  os.path.basename(absoluta))
    del_fichero = os.path.realpath(absoluta)
    for candidata, causa in (
        (por_directorio, "la ruta declarada apunta dentro del árbol"),
        (del_fichero, "la ruta parece externa y se resuelve DENTRO del árbol"),
    ):
        if _dentro(candidata, arbol):
            raise EvidenciaDentroDelArbol(
                "la evidencia de la raíz externa no puede escribirse dentro del árbol que "
                "verifica: " + causa + ". Un resultado escrito dentro vuelve a estar al "
                "alcance de quien puede escribir el árbol",
                ruta=os.path.basename(candidata),
            )
    return absoluta


def _commit_y_arbol(repo, revision):
    """El SHA del commit y el SHA de su `tree`. La atestación se ata a los DOS."""
    canal = CanalGit(repo)
    commit = canal.resolver(revision)
    _, salida, _ = canal.ejecutar("rev-parse", "--verify", commit + "^{tree}")
    return commit, salida.decode("ascii", "strict").strip()


def _proveedor(configuracion, identificador=None):
    return identidad.ProveedorProductivo(configuracion, identidad=identificador)


def _identidad_activa(configuracion):
    anillo = configuracion.anillo()
    activa = anillo.activa()
    return anillo, activa


# ---------------------------------------------------------------------------
#  capacidades
# ---------------------------------------------------------------------------
def _orden_capacidades(argumentos):
    informe = modulo_de_firma.capacidades()
    informe["condiciones_de_certificacion"] = [
        "proceso ejecutor SEPARADO del runtime verificado",
        "paquete e instalación FUERA del árbol verificado, con manifiesto de digests",
        "configuración de confianza EXTERNA al árbol",
        "identidad distinta de la del runtime y SIN permiso de escritura",
        "firma ASIMÉTRICA con criptografía estándar del anfitrión",
        "clave privada FUERA de todos los repositorios",
        "atestación vinculada al SHA del commit y al `tree` SHA",
        "evidencia FUERA del árbol verificado",
        "FALLO CERRADO sin proveedor, sin clave, sin ancla o con firma inválida",
    ]
    sys.stdout.write(_volcar(informe) + "\n")
    return EXITO if informe["disponible"] else FALLO


# ---------------------------------------------------------------------------
#  verificar
# ---------------------------------------------------------------------------
def _orden_verificar(argumentos):
    # 1 · FALLO CERRADO antes de nada: sin proveedor de firma no se emite.
    proveedor_de_firma = modulo_de_firma.exigir_proveedor()

    # 2 · la propia instalación, recalculada AQUÍ y no leída del árbol.
    estado_de_la_instalacion = None
    if os.path.isfile(os.path.join(INSTALACION, modulo_de_instalacion.MANIFIESTO)):
        estado_de_la_instalacion = modulo_de_instalacion.exigir_instalacion_intacta(
            INSTALACION)

    repo = os.path.abspath(argumentos.repo)
    evidencia = exigir_evidencia_fuera(argumentos.evidencia, repo)

    # 3 · la configuración de confianza, que `identidad/` rechaza si vive dentro del árbol.
    configuracion = identidad.cargar(argumentos.configuracion, arbol_verificado=repo)
    anillo, activa = _identidad_activa(configuracion)

    # 4 · el veredicto de admisión, calculado por ESTE proceso con SU copia del verificador.
    veredicto = admision.verificar(repo, base=argumentos.base,
                                   declaracion=configuracion.declaracion(),
                                   censar_el_codigo=argumentos.censar_el_codigo)

    # 5 · el vínculo con el commit y con el árbol.
    commit, tree = _commit_y_arbol(repo, argumentos.revision or "HEAD")

    cuerpo = modulo_de_atestacion.construir(
        autoridad=configuracion.autoridad(),
        identidad=activa.id,
        huella_publica=activa.huella_publica,
        epoca=anillo.epoca_vigente,
        commit=commit,
        tree=tree,
        veredicto={
            "color": veredicto.color,
            "base": veredicto.informe["base"],
            "hallazgos": [hallazgo.a_dict() for hallazgo in veredicto.hallazgos],
            "digest_del_censo": veredicto.informe["digest_del_censo"],
        },
        proveedor={
            "herramienta": proveedor_de_firma["herramienta"],
            "version_de_openssh": proveedor_de_firma["version_de_openssh"],
            "algoritmo": proveedor_de_firma["algoritmo"],
            "espacio_de_nombres": proveedor_de_firma["espacio_de_nombres"],
            "simetrica": proveedor_de_firma["simetrica"],
        },
        alcance={
            "ejecutor": "raiz-externa",
            "instalacion_verificada": bool(estado_de_la_instalacion),
            "runtime_importado": ("instalacion" if os.path.isdir(RUNTIME_INSTALADO)
                                  else "arbol-de-origen"),
        },
    )

    # 6 · la FIRMA, delegada en el anfitrión. La clave privada no cruza esta frontera.
    proveedor = _proveedor(configuracion, activa.id)
    firma_blindada = proveedor.firmar(modulo_de_atestacion.canonizar(cuerpo))
    sobre = modulo_de_atestacion.Sobre(cuerpo, firma_blindada.hex())

    # 7 · la evidencia, FUERA del árbol verificado.
    os.makedirs(os.path.dirname(evidencia) or ".", exist_ok=True)
    with open(evidencia, "w", encoding="utf-8") as manejador:
        manejador.write(sobre.serializar())

    resumen = {
        "color": veredicto.color,
        "commit": commit,
        "tree": tree,
        "identidad": activa.id,
        "huella_publica": activa.huella_publica,
        "epoca": anillo.epoca_vigente,
        "digest_de_la_atestacion": modulo_de_atestacion.digest(cuerpo),
        "evidencia": os.path.basename(evidencia),
        "instalacion": (estado_de_la_instalacion["ok"]
                        if estado_de_la_instalacion else None),
    }
    sys.stdout.write(_volcar(resumen) + "\n")
    return EXITO if veredicto.color == "VERDE" else FALLO


# ---------------------------------------------------------------------------
#  comprobar  ·  `G-A9`
# ---------------------------------------------------------------------------
def _leer_autodeclaracion(repo):
    """Lo que el ÁRBOL dice de sí mismo. No tiene autoridad; existe para desmentirlo."""
    ruta = os.path.join(repo, AUTODECLARACION)
    if not os.path.isfile(ruta):
        return None
    with open(ruta, encoding="utf-8") as manejador:
        try:
            return json.load(manejador)
        except ValueError:
            # Un árbol que ni siquiera sabe escribir su propia declaración no la tiene.
            return None


def _orden_comprobar(argumentos):
    modulo_de_firma.exigir_proveedor()
    repo = os.path.abspath(argumentos.repo)
    with open(argumentos.evidencia, encoding="utf-8") as manejador:
        sobre = modulo_de_atestacion.Sobre.desde_texto(manejador.read())

    configuracion = identidad.cargar(argumentos.configuracion, arbol_verificado=repo)
    anillo = configuracion.anillo()

    # 1 · la identidad que firma tiene que estar ACEPTADA y verificar en su época.
    firmante = sobre.atestacion.get("identidad")
    epoca = int(sobre.atestacion.get("epoca", 0))
    try:
        anillo.exigir_valida(firmante, epoca)
    except ErrorDeIdentidad as error:
        raise IdentidadNoAceptada(
            "la identidad que firma la atestación no la acepta la configuración externa: "
            + error.detalle, identidad=str(firmante)) from error

    # 2 · la FIRMA, verificada por el anfitrión que sólo tiene claves PÚBLICAS.
    proveedor = _proveedor(configuracion, firmante)
    if not proveedor.verificar(modulo_de_atestacion.canonizar(sobre.atestacion),
                               sobre.firma):
        raise FirmaNoVerificada(
            "la atestación NO verifica contra los firmantes autorizados: o se ha "
            "manipulado, o la firmó una clave que esta raíz no acepta"
        )

    # 3 · el VÍNCULO con el commit y el árbol que se están comprobando.
    commit, tree = _commit_y_arbol(repo, argumentos.revision or "HEAD")
    modulo_de_atestacion.exigir_vinculo(sobre.atestacion, commit=commit, tree=tree)

    # 4 · `G-A9`: la autodeclaración del árbol, contrastada con la atestación externa.
    autodeclarado = _leer_autodeclaracion(repo)
    atestado = sobre.atestacion["veredicto"]["color"]
    resumen = {
        "firma": "valida",
        "identidad": firmante,
        "epoca": epoca,
        "commit": commit,
        "tree": tree,
        "veredicto_atestado": atestado,
        "veredicto_autodeclarado": (autodeclarado or {}).get("color"),
        "digest_de_la_atestacion": modulo_de_atestacion.digest(sobre.atestacion),
    }
    if autodeclarado and autodeclarado.get("color") != atestado:
        sys.stdout.write(_volcar(resumen) + "\n")
        raise VeredictoDesmentido(
            "el árbol se declara `" + str(autodeclarado.get("color")) + "` y la atestación "
            "externa dice `" + atestado + "` sobre el MISMO commit y el MISMO árbol. Gana "
            "la atestación: el árbol no tiene la clave con que se firma",
            autodeclarado=str(autodeclarado.get("color")), atestado=atestado,
        )
    sys.stdout.write(_volcar(resumen) + "\n")
    return EXITO if atestado == "VERDE" else FALLO


# ---------------------------------------------------------------------------
#  instalacion
# ---------------------------------------------------------------------------
def _orden_instalacion(argumentos):
    destino = argumentos.instalacion or INSTALACION
    informe = modulo_de_instalacion.exigir_instalacion_intacta(destino)
    sys.stdout.write(_volcar(informe) + "\n")
    return EXITO


ORDENES = {
    "capacidades": _orden_capacidades,
    "verificar": _orden_verificar,
    "comprobar": _orden_comprobar,
    "instalacion": _orden_instalacion,
}


def construir_analizador():
    analizador = argparse.ArgumentParser(
        prog="verificador",
        description="raíz externa de confianza del control repo (`V6-16`, `g.15`)")
    ordenes = analizador.add_subparsers(dest="orden", required=True)

    ordenes.add_parser("capacidades")

    verificar = ordenes.add_parser("verificar")
    verificar.add_argument("--repo", required=True)
    verificar.add_argument("--base", required=True)
    verificar.add_argument("--configuracion", required=True)
    verificar.add_argument("--evidencia", required=True)
    verificar.add_argument("--revision", default=None)
    verificar.add_argument("--censar-el-codigo", dest="censar_el_codigo",
                           action="store_true", default=False)

    comprobar = ordenes.add_parser("comprobar")
    comprobar.add_argument("--repo", required=True)
    comprobar.add_argument("--configuracion", required=True)
    comprobar.add_argument("--evidencia", required=True)
    comprobar.add_argument("--revision", default=None)

    instalacion = ordenes.add_parser("instalacion")
    instalacion.add_argument("--instalacion", default=None)
    return analizador


def main(argv=None):
    analizador = construir_analizador()
    argumentos = analizador.parse_args(argv)
    ejecutar = ORDENES.get(argumentos.orden)
    if ejecutar is None:
        return _uso("orden desconocida: " + str(argumentos.orden))
    try:
        return ejecutar(argumentos)
    except (ErrorDeRaizExterna, ErrorDeAdmision, ErrorDeGobierno,
            ErrorDeIdentidad) as error:
        sys.stderr.write(str(error) + "\n")
        return FALLO


if __name__ == "__main__":
    sys.exit(main())
