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
    AnclaNoCoincide,
    AtestacionInvalida,
    EmisorNoCoincide,
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
#  `E-07` · LOS SIETE PASOS, UNA SOLA VEZ, EN UN SOLO SITIO
# ---------------------------------------------------------------------------
#  DECISIÓN · `verificar` y `comprobar` corren EXACTAMENTE la misma secuencia
#      Alternativas: (a) que `verificar` compruebe lo que puede y `comprobar` haga el resto;
#      (b) una sola función que ejecute los siete pasos sobre el SOBRE ya construido, y que
#      las dos órdenes la llamen.
#      Se elige (b). Con (a) hay dos listas de comprobaciones que se creen la misma, y ésa es
#      la forma exacta en que se cuela lo que nadie mira: la auditoría encontró que `verificar`
#      escribía evidencia sin comprobar el vínculo, y `comprobar` sí lo comprobaba, con lo
#      cual el defecto sólo aparecía si alguien acordaba comprobar después. Con (b) EMITIR es
#      VERIFICAR LO EMITIDO, y la evidencia sale por una puerta que exige el testigo completo.
def verificar_en_orden(sobre, *, configuracion, anillo, proveedor, commit, tree):
    """Ejecuta los SIETE pasos EN SU ORDEN y devuelve el testigo. Falla cerrado en el primero.

    Orden, y el orden es la garantía: **firma · clave aceptada · época · commit · tree ·
    política · identidad del emisor**. Comprobar el vínculo antes que la firma sería juzgar
    bytes que nadie ha autenticado; comprobar la época antes que la pertenencia al anillo
    sería preguntar por la ventana de una identidad que no está inscrita.
    """
    secuencia = modulo_de_atestacion.SecuenciaDeVerificacion()
    cuerpo = sobre.atestacion
    modulo_de_atestacion.exigir_forma(cuerpo)

    # 1 · FIRMA. Contra `orden_de_verificacion`, que sólo tiene claves PÚBLICAS.
    if not proveedor.verificar(modulo_de_atestacion.canonizar(cuerpo), sobre.firma):
        raise FirmaNoVerificada(
            "la atestación NO verifica contra los firmantes autorizados: o se ha "
            "manipulado, o la firmó una clave que esta raíz no acepta"
        )
    secuencia.anotar("firma")

    # 2 · CLAVE ACEPTADA. Estar inscrita en el anillo externo, que el árbol no controla.
    firmante = cuerpo.get("identidad")
    try:
        inscrita = anillo.obtener(firmante)
    except ErrorDeIdentidad as error:
        raise IdentidadNoAceptada(
            "la identidad que firma la atestación no la acepta la configuración externa: "
            + error.detalle, identidad=str(firmante)) from error
    secuencia.anotar("clave-aceptada")

    # 3 · ÉPOCA. Tiempo LÓGICO, nunca el reloj de quien verifica (`I-g3`).
    epoca = int(cuerpo.get("epoca", 0))
    try:
        anillo.exigir_valida(firmante, epoca)
    except ErrorDeIdentidad as error:
        raise IdentidadNoAceptada(
            "la identidad que firma la atestación no es válida en la época que la "
            "atestación declara: " + error.detalle,
            identidad=str(firmante), epoca=epoca) from error
    secuencia.anotar("epoca")

    # 4 y 5 · las DOS MITADES del vínculo, por separado y con su propio código.
    modulo_de_atestacion.exigir_commit(cuerpo, commit)
    secuencia.anotar("commit")
    modulo_de_atestacion.exigir_tree(cuerpo, tree)
    secuencia.anotar("tree")

    # 6 · POLÍTICA. La autoridad y el ANCLA bajo las que se calculó el veredicto son las que
    #     declara la configuración EXTERNA, no las que el árbol pudiera proponer.
    declaracion = configuracion.declaracion()
    if not declaracion.ancla:
        raise AnclaNoCoincide(
            "la configuración externa de confianza no declara ancla: sin ancla que venga de "
            "fuera no hay política contra la que juzgar, y `V6-17` prohíbe el verde"
        )
    if cuerpo.get("autoridad") != configuracion.autoridad():
        raise AnclaNoCoincide(
            "la atestación dice haberse emitido bajo la autoridad `"
            + str(cuerpo.get("autoridad")) + "` y esta configuración externa es `"
            + str(configuracion.autoridad()) + "`",
            atestada=str(cuerpo.get("autoridad")),
            declarada=str(configuracion.autoridad()),
        )
    base_atestada = (cuerpo.get("veredicto") or {}).get("base")
    if base_atestada != declaracion.ancla:
        raise AnclaNoCoincide(
            "el veredicto atestado parte de la base " + str(base_atestada)[:12]
            + " y la configuración externa ancla en " + str(declaracion.ancla)[:12]
            + ": un veredicto calculado contra otra base no es el de esta raíz externa",
            atestada=str(base_atestada)[:12], declarada=str(declaracion.ancla)[:12],
        )
    secuencia.anotar("politica")

    # 7 · IDENTIDAD DEL EMISOR. La huella PÚBLICA atestada es la que el anillo inscribe para
    #     ese identificador. Sin este paso, una atestación podría llamarse `raiz-externa-1` y
    #     publicar la huella de otra clave, y la trazabilidad apuntaría a quien no fue.
    if cuerpo.get("huella_publica") != inscrita.huella_publica:
        raise EmisorNoCoincide(
            "la atestación se atribuye a `" + str(firmante) + "` y publica una huella "
            "pública que NO es la que el anillo externo inscribe para esa identidad",
            identidad=str(firmante),
        )
    secuencia.anotar("identidad-del-emisor")

    secuencia.exigir_completa()
    return secuencia


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
    canonico = modulo_de_atestacion.canonizar(cuerpo)
    firma_blindada = proveedor.firmar(canonico)
    sobre = modulo_de_atestacion.Sobre(cuerpo, firma_blindada.hex())

    # 6 bis · SE VERIFICA LO QUE SE ACABA DE FIRMAR, y no es ceremonia.
    #
    # DEFECTO QUE CIERRA, encontrado por la auditoría independiente. `firmar` delega en el
    # anfitrión y devuelve lo que el anfitrión produzca: si la clave que el anfitrión tiene
    # a mano NO es la que el anillo acepta —otra ruta, otro almacén, una variable de entorno
    # apuntando a otro sitio—, la firma sale igualmente, la atestación se escribe con la
    # identidad y la huella que la CONFIGURACIÓN declara, y el punto ejecutable termina con
    # código 0. Es decir: se publicaba una ATRIBUCIÓN FALSA en un artefacto durable firmado,
    # y un `verificar && desplegar` seguía adelante sobre ella.
    #
    # `comprobar` sí lo detectaba, pero detectarlo después no es fallar cerrado: `O25` §2
    # exige que sin proveedor VÁLIDO no se firme, y un proveedor que firma con una clave que
    # el anillo no acepta no es válido. La verificación va contra `orden_de_verificacion`,
    # que sólo tiene claves PÚBLICAS, de modo que este paso no puede firmar nada.
    if not proveedor.verificar(canonico, sobre.firma):
        raise FirmaNoVerificada(
            "la atestación recién firmada NO verifica contra los firmantes autorizados: "
            "el anfitrión ha firmado con una clave que esta raíz externa NO acepta. NO se "
            "emite evidencia, y el fallo es CERRADO: publicarla estamparía la identidad "
            "declarada sobre una firma que no es suya",
            identidad=str(activa.id),
        )

    # 6 ter · `E-07` · LOS SIETE PASOS, sobre el sobre que se acaba de construir y en su
    #         orden. EMITIR ES VERIFICAR LO EMITIDO: la misma secuencia que corre
    #         `comprobar`, en el mismo sitio y con el mismo código.
    secuencia = verificar_en_orden(
        sobre, configuracion=configuracion, anillo=anillo, proveedor=proveedor,
        commit=commit, tree=tree)

    # 7 · la evidencia, FUERA del árbol verificado. La escritura pasa por la ÚNICA puerta
    #     que exige el testigo COMPLETO: sin los siete pasos no hay fichero.
    modulo_de_atestacion.escribir_evidencia(evidencia, sobre, secuencia)

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
        # La secuencia se PUBLICA: quien lee la evidencia ve QUÉ se verificó y en qué orden,
        # y no tiene que creerse que se verificó algo.
        "secuencia_de_verificacion": secuencia.a_dict(),
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

    # 1 a 7 · `E-07` · LA MISMA SECUENCIA que corre la emisión, en el mismo orden: firma ·
    #         clave aceptada · época · commit · tree · política · identidad del emisor.
    firmante = sobre.atestacion.get("identidad")
    epoca = int(sobre.atestacion.get("epoca", 0))
    proveedor = _proveedor(configuracion, firmante)
    commit, tree = _commit_y_arbol(repo, argumentos.revision or "HEAD")
    secuencia = verificar_en_orden(
        sobre, configuracion=configuracion, anillo=anillo, proveedor=proveedor,
        commit=commit, tree=tree)

    # 8 · `G-A9`: la autodeclaración del árbol, contrastada con la atestación externa.
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
        "secuencia_de_verificacion": secuencia.a_dict(),
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
