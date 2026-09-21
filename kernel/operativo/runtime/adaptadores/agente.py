#!/usr/bin/env python3
"""agente — ADAPTADOR DE AGENTE SIN CHAT: lanza un agente con un brief y recoge su entrega.

HECHO MEDIDO ANTES DE CONSTRUIR (La Pesquerapp, 2026-09-14). `CONTRATO-ADAPTADOR.md` §5 lo
decía con todas las letras: «no existe ningún adaptador de proveedor comercial». El único
adaptador real ejecutaba un subproceso, y por eso ningún supervisor podía poner a trabajar a
un agente sin que hubiera una persona en un chat. Este adaptador cierra esa distancia SIN
meter un proveedor en el kernel: lo que lanza lo declara el PROYECTO en su `PROFILE.md`
como bloque `ads:ejecutor` —el `argv` del ejecutable sin chat del proveedor que el proyecto use—
y el kernel sólo sabe sustituir marcadores, esperar, matar y leer la entrega.

DECISIÓN · se COMPONE sobre `AdaptadorDeProcesoLocal`; no se reescribe
    Timeout que mata al grupo, recibo abierto antes y cerrado después, `ambiguo` cuando el
    proceso muere entre ejecutar y cerrar, contención opcional: todo eso está construido y
    medido en `proceso.py`. Este adaptador construye el `argv` y delega la ejecución; lo
    único que añade es LEER LA ENTREGA y decidir el desenlace por ella.

DECISIÓN · sin entrega válida NO hay `completado`, aunque el proceso saliera con 0
    Un agente que termina bien y no deja `entregas/<paquete>-<efecto>.json` con la forma
    del esquema `entrega` no ha entregado nada: el resultado es `fallido` y REINTENTABLE,
    con el detalle de qué faltó. Un `completado` durable sobre una entrega ausente sería
    exactamente el «terminado» que esta campaña vino a impedir.

DECISIÓN · la entrega viaja ENTERA en `salida`, y por eso queda en el estado canónico
    El resultado del §4.4 se escribe en el paquete por el dispatcher. Si `salida` llevara
    sólo la ruta del fichero en el espacio del adaptador —que es operacional— y el
    supervisor muriera antes de registrarla, la entrega se perdería del estado durable. Con
    la entrega dentro de `salida`, registrarla en `entregas/` es derivable e idempotente.
"""
from __future__ import annotations

import json
import os

from .contrato import (
    VERSION_DE_CONTRATO,
    Adaptador,
    FichaDeAdaptador,
    OrdenInvalida,
)
from .proceso import AdaptadorDeProcesoLocal
from . import puntero

CAPACIDAD = "agente"
BLOQUE_DE_EJECUTOR = "ejecutor"
MARCADORES = ("{brief}", "{entrega}", "{espacio}", "{modelo}", "{paquete}", "{repo}")

SUBDIRECTORIO_BRIEFS = "briefs"
SUBDIRECTORIO_ENTREGAS = "entregas"
SUBDIRECTORIO_PROCESOS = "procesos"

CODIGO_SIN_ENTREGA = 65
CODIGO_ENTREGA_ILEGIBLE = 66


# ===========================================================================
#  los ejecutores, leídos del PROFILE del proyecto
# ===========================================================================
def ejecutores_desde_texto(texto, *, corpus, sede="PROFILE.md"):
    """Los bloques `ads:ejecutor` de un texto, validados, por el modelo que ejecutan."""
    from ciclo import formas                                          # noqa: PLC0415
    from ciclo.corpus import bloques                                  # noqa: PLC0415
    esquema = corpus.esquema(BLOQUE_DE_EJECUTOR)
    salida = {}
    for clase, datos, _ruta, linea in bloques(texto, sede):
        if clase != BLOQUE_DE_EJECUTOR:
            continue
        fallos = formas.validar(datos, esquema, corpus=corpus, camino="ejecutor")
        if fallos:
            raise OrdenInvalida(sede + ":" + str(linea) + ": " + "; ".join(fallos))
        if not any(m in " ".join(datos["argv"]) for m in ("{brief}", "{entrega}")):
            raise OrdenInvalida(
                sede + ":" + str(linea) + ": el ejecutor `" + datos["id"] + "` no usa "
                "`{brief}` ni `{entrega}` en su argv: un agente que no recibe el brief ni "
                "sabe dónde entregar no puede ejecutar un paquete",
            )
        if datos["modelo"] in salida:
            raise OrdenInvalida(sede + ": dos ejecutores para el modelo `" + datos["modelo"] + "`")
        salida[datos["modelo"]] = datos
    return salida


def cargar_ejecutores(ruta_control_repo, *, corpus):
    sede = os.path.join(ruta_control_repo, "PROFILE.md")
    if not os.path.isfile(sede):
        raise OrdenInvalida("el control repo no trae `PROFILE.md`, donde viven los ejecutores")
    with open(sede, "r", encoding="utf-8") as manejador:
        return ejecutores_desde_texto(manejador.read(), corpus=corpus)


# ===========================================================================
#  el adaptador
# ===========================================================================
class AdaptadorDeAgente(Adaptador):
    """Lanza el ejecutor del modelo con el brief del paquete y devuelve su entrega."""

    identificador = "agente"
    version_de_contrato = VERSION_DE_CONTRATO
    capacidades = (CAPACIDAD,)

    def __init__(self, espacio_de_trabajo, ejecutores, *, repo=None, entorno=None,
                 politica_de_contencion=None):
        self.espacio = os.path.abspath(espacio_de_trabajo)
        self.ejecutores = dict(ejecutores or {})
        self.repo = os.path.abspath(repo) if repo else ""
        if not self.ejecutores:
            raise OrdenInvalida(
                "el adaptador de agente no tiene ejecutores: el PROFILE del proyecto tiene "
                "que declarar al menos un bloque `ads:ejecutor`",
            )
        for nombre in (SUBDIRECTORIO_BRIEFS, SUBDIRECTORIO_ENTREGAS, SUBDIRECTORIO_PROCESOS):
            os.makedirs(os.path.join(self.espacio, nombre), exist_ok=True)
        self._proceso = AdaptadorDeProcesoLocal(
            os.path.join(self.espacio, SUBDIRECTORIO_PROCESOS), entorno=entorno,
            politica_de_contencion=politica_de_contencion,
        )

    # -- ficha -------------------------------------------------------------
    def ficha(self):
        interna = self._proceso.ficha()
        return FichaDeAdaptador(
            identificador=self.identificador,
            version=VERSION_DE_CONTRATO,
            capacidades=list(self.capacidades),
            operaciones=["ejecutar"],
            limites=interna["limites"],
            timeout=interna["timeout"],
            cancelacion=interna["cancelacion"],
            idempotencia="la del proceso interno por `efecto`, más la entrega leída del "
                         "espacio por paquete y efecto: repetir devuelve la misma entrega",
            forma_de_progreso=interna["forma_de_progreso"],
            resultado="{estado, codigo, salida, detalle, reintentable, efecto, repetido}; "
                      "`salida` lleva la ENTREGA del agente como JSON cuando está completado",
            errores=["ORDEN_INVALIDA", "ERROR_DE_ADAPTADOR"],
            evidencia="el brief y la entrega en el espacio del adaptador, y el recibo del "
                      "proceso interno",
            compatibilidad="cualquier ejecutor que el PROFILE declare con argv; declarado, "
                           "no certificado (§6.5)",
            resolucion_del_control_repo=puntero.DESENLACES_DECLARADOS,
        )

    # -- rutas ---------------------------------------------------------------
    def ruta_de_brief(self, paquete):
        return os.path.join(self.espacio, SUBDIRECTORIO_BRIEFS, paquete + ".md")

    def ruta_de_entrega(self, paquete, efecto):
        return os.path.join(self.espacio, SUBDIRECTORIO_ENTREGAS, paquete + "-" + efecto + ".json")

    def escribir_brief(self, paquete, texto, datos=None):
        """El SUPERVISOR escribe el brief ANTES de despachar. Devuelve la ruta."""
        ruta = self.ruta_de_brief(paquete)
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(texto)
        if datos is not None:
            with open(ruta[: -len(".md")] + ".json", "w", encoding="utf-8") as manejador:
                manejador.write(json.dumps(datos, sort_keys=True, ensure_ascii=False, indent=2))
        return ruta

    # -- ejecución ---------------------------------------------------------
    def ejecutar(self, orden, *, efecto, limite_segundos, progreso=None, cancelacion=None):
        if not isinstance(orden, dict):
            raise OrdenInvalida("la orden de un adaptador es un mapa")
        argumentos = list(orden.get("argumentos") or [])
        if len(argumentos) < 2:
            raise OrdenInvalida(
                "la orden de un paquete de agente declara [<modelo>, <paquete>] en sus "
                "argumentos; llegaron " + str(len(argumentos)),
            )
        modelo, paquete = str(argumentos[0]), str(argumentos[1])
        ejecutor = self.ejecutores.get(modelo)
        if ejecutor is None:
            return self._fallo(efecto, CODIGO_SIN_ENTREGA, reintentable=False,
                               detalle="no hay ejecutor declarado para el modelo `" + modelo
                               + "`; declarados: " + ", ".join(sorted(self.ejecutores)))
        brief = self.ruta_de_brief(paquete)
        if not os.path.isfile(brief):
            return self._fallo(efecto, CODIGO_SIN_ENTREGA, reintentable=True,
                               detalle="no hay brief para `" + paquete + "` en el espacio del "
                               "adaptador: el supervisor lo escribe antes de despachar")
        entrega = self.ruta_de_entrega(paquete, efecto)
        sustituciones = {
            "{brief}": brief, "{entrega}": entrega, "{espacio}": self.espacio,
            "{modelo}": modelo, "{paquete}": paquete, "{repo}": self.repo,
        }
        argv = []
        for pieza in ejecutor["argv"]:
            texto = str(pieza)
            for marcador, valor in sustituciones.items():
                texto = texto.replace(marcador, valor)
            argv.append(texto)
        limite = min(float(limite_segundos), float(ejecutor["limite_segundos"]))
        interno = self._proceso.ejecutar(
            {"adaptador": "proceso-local", "operacion": "ejecutar", "argumentos": argv,
             "limite_segundos": limite},
            efecto=efecto, limite_segundos=limite, progreso=progreso, cancelacion=cancelacion,
        )
        if interno["estado"] != "completado":
            # timeout · cancelado · ambiguo · fallido: se devuelve tal cual, con su detalle.
            salida = dict(interno)
            salida["efecto"] = efecto
            salida["salida"] = self._recortar(interno.get("salida") or "")
            return salida
        if not os.path.isfile(entrega):
            return self._fallo(efecto, CODIGO_SIN_ENTREGA, reintentable=True,
                               detalle="el ejecutor terminó con 0 y NO dejó entrega en "
                               + os.path.basename(entrega) + "; sin entrega no hay completado",
                               repetido=bool(interno.get("repetido")))
        try:
            with open(entrega, "r", encoding="utf-8") as manejador:
                datos = json.load(manejador)
        except (OSError, ValueError) as exc:
            return self._fallo(efecto, CODIGO_ENTREGA_ILEGIBLE, reintentable=True,
                               detalle="la entrega no es JSON legible: " + str(exc),
                               repetido=bool(interno.get("repetido")))
        if not isinstance(datos, dict):
            return self._fallo(efecto, CODIGO_ENTREGA_ILEGIBLE, reintentable=True,
                               detalle="la entrega no es un mapa JSON")
        # QUIÉN la produjo viaja CON la entrega, y lo pone quien lanzó el ejecutable, no
        # quien entrega. Un trabajador puede llamarse como quiera; el ejecutor que lo movió
        # es un hecho del despacho, y sin él la afirmación «ejecución real por modelo» no se
        # puede derivar del estado: hay que creerse una línea de terminal.
        datos["ejecutor"] = {"clase": "modelo", "id": modelo,
                             "orden": os.path.basename(str(argv[0])) if argv else ""}
        return {
            "estado": "completado", "codigo": 0,
            "salida": json.dumps(datos, sort_keys=True, ensure_ascii=False),
            "detalle": "entrega leída de " + os.path.basename(entrega),
            "reintentable": False, "efecto": efecto,
            "repetido": bool(interno.get("repetido")),
        }

    @staticmethod
    def _recortar(texto, maximo=4000):
        texto = str(texto)
        return texto if len(texto) <= maximo else texto[-maximo:]

    @staticmethod
    def _fallo(efecto, codigo, *, reintentable, detalle, repetido=False):
        return {"estado": "fallido", "codigo": int(codigo), "salida": "", "detalle": detalle,
                "reintentable": bool(reintentable), "efecto": efecto, "repetido": bool(repetido)}
