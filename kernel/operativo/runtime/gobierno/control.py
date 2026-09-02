#!/usr/bin/env python3
"""control — las once capacidades ejecutables del gobierno Git del control repo (`g.14`).

    1 · representar propiedad y autoridad        7 · detectar pérdida de autoridad
    2 · obtener una concesión (lease de ref)     8 · rechazar doble escritor
    3 · contrastar la revisión base              9 · serializar entre dos procesos
    4 · preparar la mutación                    10 · recuperar tras caída
    5 · validar la política                     11 · dejar evidencia auditable
    6 · confirmar

Y `G-A8` con sus DOS mitades, que es lo que `g.16` exige demostrar:

    IMPOSIBLE    el hook `reference-transaction`, instalado al inicializar el gobierno,
                 rechaza toda actualización no fast-forward y todo borrado de ref protegida.
                 `comprobar_hook()` mide que sigue instalado y con el contenido esperado.
    DETECTABLE   `verificar_refs()` contrasta el LINAJE DURABLE registrado en el almacén
                 contra las refs vivas y DENUNCIA un forzado aunque el hook se hubiera
                 quitado. No depende del hook para nada.

DECISIÓN · la concesión de ref es DURABLE, y no un fichero de bloqueo
    Alternativas: (a) un `flock` sobre un fichero del plano operacional; (b) un objeto del
    estado canónico.
    Se elige (b), con (a) como vía rápida y no como sustituto. Un `flock` muere con el
    proceso y no sobrevive a una caída, de modo que «recuperar tras caída» no se podría
    demostrar: al arrancar no habría rastro de quién tenía la autoridad ni contra qué
    revisión. La concesión vive en `canonico/refs/<ref>.json`, es una `Transicion` del motor
    que ya existe, y por tanto la escribe el mismo mecanismo que serializa a dos escritores.
    NO se construye un segundo sistema de estado.

DECISIÓN · el LINAJE se registra en cada confirmación, y por eso el forzado se ve
    Alternativas: (a) guardar sólo la cabeza; (b) guardar la cadena de cabezas publicadas.
    Se elige (b). Con (a), un forzado a un commit que no descienda de la cabeza registrada
    se detecta, pero un forzado seguido de una confirmación legítima borraría la evidencia:
    la cabeza nueva descendería de la falsa y todo cuadraría. Con la cadena, la
    comprobación es que CADA cabeza registrada sigue siendo alcanzable desde la actual, y
    un forzado deja huérfana una cabeza de la cadena para siempre.

DECISIÓN · `epoca` y `latido` en lugar de reloj
    `I-g3` prohíbe el reloj de pared en lo durable. El tiempo lógico de una concesión es su
    ÉPOCA, que sube cuando cambia el titular, y su LATIDO, que sube en cada transición del
    titular. Es el mismo mecanismo que el §3 del contrato fija para los leases de paquete.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import estado                                                        # noqa: E402
from admision.formulas import digest_de_contenido                    # noqa: E402

from . import propiedad                                              # noqa: E402
from .errores import (                                               # noqa: E402
    AutoridadDeRefNoConcedida,
    DobleEscritor,
    EstadoParcialEnLaRama,
    ForzadoDetectado,
    HookAusente,
    PoliticaViolada,
    RefProtegida,
    RevisionBaseObsoleta,
)
from .git import CONTENIDO_DEL_HOOK, NOMBRE_DEL_HOOK, NULO, CanalGit  # noqa: E402

DOMINIO = "refs"
RAMA_CANONICA = "refs/heads/canonica"

# El digest del hook se DERIVA de su contenido, no se escribe. Escribirlo a mano habría
# creado una segunda verdad que se desincroniza en cuanto alguien toque una línea del hook.
DIGEST_DEL_HOOK = digest_de_contenido(CONTENIDO_DEL_HOOK)


def _identificador_de_ref(ref):
    """`refs/heads/canonica` → `refs.heads.canonica`, que el motor admite como id."""
    return ref.replace("/", ".")


class GobiernoDelControlRepo:
    """Gobierna las referencias de UN control repo. No abre ninguno por su cuenta."""

    def __init__(self, ruta_control_repo, *, titular, politica=None, almacen=None):
        self.ruta = os.path.abspath(ruta_control_repo)
        self.titular = titular
        self.politica = politica if politica is not None else propiedad.cargar()
        self.canal = CanalGit(self.ruta, autor=titular)
        self._almacen = almacen
        self._propio = almacen is None

    # =====================================================================
    #  apertura y cierre
    # =====================================================================
    def abrir(self):
        if self._almacen is None:
            self._almacen = estado.abrir(self.ruta)
        return self

    def cerrar(self):
        if self._almacen is not None and self._propio:
            self._almacen.cerrar()
            self._almacen = None

    def __enter__(self):
        return self.abrir()

    def __exit__(self, tipo, valor, traza):
        self.cerrar()
        return False

    @property
    def almacen(self):
        if self._almacen is None:
            raise AutoridadDeRefNoConcedida(
                "el gobierno no está abierto: `abrir()` recupera el almacén antes de nada"
            )
        return self._almacen

    # =====================================================================
    #  1 · representar propiedad y autoridad
    # =====================================================================
    def autoridad(self, actor, operacion):
        """¿Puede este actor esta operación? Lo dice la política, no el código."""
        return {
            "actor": actor,
            "operacion": operacion,
            "puede": self.politica.puede(actor, operacion),
            "serializa": self.politica.serializa(operacion),
            "exige_revision_base": self.politica.exige_revision_base(operacion),
        }

    # =====================================================================
    #  5 · validar la política  ·  G-A8 mitad IMPOSIBLE
    # =====================================================================
    def ruta_del_hook(self):
        codigo, salida, _ = self.canal.ejecutar(
            "rev-parse", "--git-path", "hooks", exigir_exito=False
        )
        if codigo != 0:
            raise HookAusente("el repositorio no declara directorio de hooks")
        relativa = salida.decode("utf-8", "strict").strip()
        if not os.path.isabs(relativa):
            relativa = os.path.join(self.ruta, relativa)
        return os.path.join(relativa, NOMBRE_DEL_HOOK)

    def instalar_hook(self):
        """Instala el hook `reference-transaction`. Es la mitad IMPOSIBLE de `G-A8`."""
        destino = self.ruta_del_hook()
        directorio = os.path.dirname(destino)
        if not os.path.isdir(directorio):
            os.makedirs(directorio, exist_ok=True)
        with open(destino, "w", encoding="utf-8", newline="\n") as manejador:
            manejador.write(CONTENIDO_DEL_HOOK)
        os.chmod(destino, 0o755)
        return {"hook": NOMBRE_DEL_HOOK, "digest": DIGEST_DEL_HOOK, "instalado": True}

    def comprobar_hook(self):
        """¿Sigue instalado, ejecutable y con el contenido esperado? Falla cerrado."""
        destino = self.ruta_del_hook()
        if not os.path.exists(destino):
            raise HookAusente(
                "el hook `" + NOMBRE_DEL_HOOK + "` no está instalado: sin él, forzar una "
                "referencia deja de ser imposible y sólo queda ser detectable",
                ruta=NOMBRE_DEL_HOOK,
            )
        with open(destino, "rb") as manejador:
            contenido = manejador.read()
        digest = digest_de_contenido(contenido)
        if digest != DIGEST_DEL_HOOK:
            raise HookAusente(
                "el hook `" + NOMBRE_DEL_HOOK + "` está instalado pero su contenido NO es "
                "el esperado: un hook editado es un hook desactivado con otro nombre",
                ruta=NOMBRE_DEL_HOOK,
            )
        if not os.access(destino, os.X_OK):
            raise HookAusente(
                "el hook `" + NOMBRE_DEL_HOOK + "` no es ejecutable, y Git no lo invoca",
                ruta=NOMBRE_DEL_HOOK,
            )
        return {"hook": NOMBRE_DEL_HOOK, "digest": digest, "instalado": True}

    # =====================================================================
    #  2 · obtener una concesión (lease de ref)   ·   8 · rechazar doble escritor
    # =====================================================================
    def _leer_concesion(self, ref):
        logica = DOMINIO + "/" + _identificador_de_ref(ref) + ".json"
        try:
            return self.almacen.leer(logica)
        except estado.ErrorDeEstado:
            return None

    def conceder(self, ref, *, actor=None):
        """Concede la autoridad sobre una ref. `DobleEscritor` si otro la tiene viva."""
        actor = actor or "runtime"
        if ref in self.politica.refs_protegidas():
            permitidos = self.politica.mueve(ref)
            if permitidos and actor not in permitidos:
                raise RefProtegida(
                    "la política no autoriza a `" + actor + "` a mover esta ref",
                    ruta=ref,
                )
        # La revisión se lee ANTES que la concesión y se usa como base de la escritura. Así
        # la concesión se publica por COMPARACIÓN E INTERCAMBIO sobre el estado que se leyó:
        # si otro proceso publicó entre la lectura y la escritura, ésta se rechaza en vez de
        # pisarla. Sin esto, dos aspirantes que leen `None` a la vez se conceden los dos.
        revision = self.almacen.revision()["revision_id"]
        concesion = self._leer_concesion(ref)
        if concesion is not None and concesion["titular"] != self.titular:
            raise DobleEscritor(
                "la ref ya está concedida a otro titular en la época "
                + str(concesion["epoca"]) + "; la autoridad no se comparte",
                ruta=ref,
            )
        existe, cabeza = self.canal.existe_ref(ref)
        # Reconceder al MISMO titular no sube la época: la época es el contador del CAMBIO
        # de titular, y subirla en cada apertura haría indistinguible una reapertura de un
        # relevo. Un titular distinto no llega aquí: lo para `DobleEscritor`.
        epoca = 1 if concesion is None else concesion["epoca"]
        # `esquema` NO se pone aquí: lo pone el motor en `Escritura.normalizada()`. Ponerlo
        # a mano sería una segunda sede del número de versión.
        cuerpo = {
            "ref": ref,
            "titular": self.titular,
            "actor": actor,
            "epoca": epoca,
            "latido": 0 if concesion is None else concesion["latido"],
            "cabeza": cabeza if existe else NULO,
            "linaje": list(concesion["linaje"]) if concesion is not None else (
                [cabeza] if existe else []
            ),
        }
        self._escribir_concesion(ref, cuerpo, "gobierno.concesion", "concesión de ref",
                                 base=revision, intentos=1)
        return cuerpo

    def _escribir_concesion(self, ref, cuerpo, tipo, motivo, base=None, intentos=3):
        logica = DOMINIO + "/" + _identificador_de_ref(ref) + ".json"
        # El `id` incluye el TITULAR. Dos titulares distintos que compiten por la misma
        # concesión producían el mismo identificador, y el motor rechazaba al segundo por
        # `IDENTIFICADOR_DUPLICADO`: la serialización funcionaba por accidente y por el
        # mecanismo equivocado. Con el titular dentro, quien serializa es la comparación e
        # intercambio sobre la revisión base, que es lo que `g.6` manda.
        self.almacen.aplicar(estado.Transicion(
            tipo=tipo,
            base=base if base is not None else self.almacen.revision()["revision_id"],
            operaciones=[estado.Escritura(logica, cuerpo)],
            autor=self.titular,
            motivo=motivo + " " + ref,
            id="tx-" + tipo.replace(".", "-") + "-" + _identificador_de_ref(ref)
               + "-" + self.titular
               + "-e" + str(cuerpo["epoca"]) + "-l" + str(cuerpo["latido"]),
        ), intentos=intentos)

    def exigir_concesion(self, ref):
        """7 · detectar PÉRDIDA de autoridad. Se RELEE, no se recuerda."""
        concesion = self._leer_concesion(ref)
        if concesion is None:
            raise AutoridadDeRefNoConcedida(
                "no hay concesión viva sobre esta ref", ruta=ref
            )
        if concesion["titular"] != self.titular:
            raise AutoridadDeRefNoConcedida(
                "la concesión es de `" + str(concesion["titular"]) + "` y no de `"
                + self.titular + "`: la autoridad se perdió bajo los pies",
                ruta=ref,
            )
        return concesion

    def liberar(self, ref):
        concesion = self.exigir_concesion(ref)
        logica = DOMINIO + "/" + _identificador_de_ref(ref) + ".json"
        cuerpo = dict(concesion)
        cuerpo["titular"] = ""
        cuerpo["latido"] = concesion["latido"] + 1
        self.almacen.aplicar(estado.Transicion(
            tipo="gobierno.liberacion",
            base=self.almacen.revision()["revision_id"],
            operaciones=[estado.Escritura(logica, cuerpo)],
            autor=self.titular,
            motivo="liberación de la concesión de " + ref,
            id="tx-gobierno-liberacion-" + _identificador_de_ref(ref)
               + "-l" + str(cuerpo["latido"]),
        ))
        return cuerpo

    # =====================================================================
    #  3 · contrastar la revisión base
    # =====================================================================
    def contrastar_revision_base(self, ref, revision_base):
        """La cabeza viva tiene que ser EXACTAMENTE la declarada. Si no, obsoleta."""
        existe, cabeza = self.canal.existe_ref(ref)
        vigente = cabeza if existe else NULO
        if revision_base != vigente:
            raise RevisionBaseObsoleta(
                "la revisión base declarada ya no es la cabeza de la ref: se declaró "
                + revision_base[:12] + " y la ref está en " + vigente[:12],
                ruta=ref,
            )
        return vigente

    # =====================================================================
    #  4 · preparar la mutación
    # =====================================================================
    def preparar(self, ref, *, mensaje, ficheros):
        """Prepara la mutación SIN publicarla: índice y árbol, nunca la ref.

        `ficheros` es `{ruta relativa: bytes}`. Se escriben, se añaden al índice y se
        construye un commit con `commit-tree`, que NO mueve ninguna ref. Mover la ref es un
        acto aparte, con comparación e intercambio, y por eso se puede rechazar.
        """
        for relativa, contenido in sorted(ficheros.items()):
            destino = os.path.join(self.ruta, relativa)
            os.makedirs(os.path.dirname(destino) or self.ruta, exist_ok=True)
            with open(destino, "wb") as manejador:
                manejador.write(contenido)
            self.canal.ejecutar("add", "--", relativa)
        _, arbol, _ = self.canal.ejecutar("write-tree")
        arbol = arbol.decode("ascii", "strict").strip()
        existe, cabeza = self.canal.existe_ref(ref)
        argumentos = ["commit-tree", arbol]
        if existe:
            argumentos.extend(["-p", cabeza])
        argumentos.extend(["-m", mensaje])
        _, commit, _ = self.canal.ejecutar(*argumentos)
        return {
            "arbol": arbol,
            "commit": commit.decode("ascii", "strict").strip(),
            "base": cabeza if existe else NULO,
            "ficheros": sorted(ficheros),
        }

    # =====================================================================
    #  6 · confirmar   ·   9 · serializar entre dos procesos
    # =====================================================================
    def confirmar(self, ref, preparacion, *, actor="runtime"):
        """Publica la mutación en la ref por COMPARACIÓN E INTERCAMBIO.

        Exige, en este orden y todo antes de tocar la ref:
          · autoridad viva sobre la ref (`AutoridadDeRefNoConcedida` si se perdió)
          · política que autorice a este actor la operación `confirmar`
          · hook instalado y con el contenido esperado (`HookAusente`)
          · ventana del almacén CERRADA (`EstadoParcialEnLaRama`)
          · la revisión base declarada, todavía vigente (`RevisionBaseObsoleta`)
        """
        concesion = self.exigir_concesion(ref)
        if not self.politica.puede(actor, "confirmar"):
            raise PoliticaViolada(
                "la política no autoriza a `" + actor + "` a confirmar en la rama canónica"
            )
        self.comprobar_hook()
        ventana = self.almacen.estado_de_la_ventana()
        if ventana != "cerrada":
            raise EstadoParcialEnLaRama(
                "la ventana del almacén está `" + ventana + "`: la rama canónica NUNCA "
                "contiene estado parcial (`g.14`), y confirmar ahora la publicaría",
                ruta=ref,
            )
        self.contrastar_revision_base(ref, preparacion["base"])
        resultado = self.canal.actualizar_ref(
            ref, preparacion["commit"], preparacion["base"],
            protegidas=self.politica.refs_protegidas(),
        )
        # 11 · EVIDENCIA AUDITABLE: el linaje crece en la MISMA transición que sube el
        # latido. O se ven los dos, o no se ve ninguno.
        cuerpo = dict(concesion)
        cuerpo["latido"] = concesion["latido"] + 1
        cuerpo["cabeza"] = preparacion["commit"]
        cuerpo["linaje"] = list(concesion["linaje"]) + [preparacion["commit"]]
        self._escribir_concesion(ref, cuerpo, "gobierno.confirmacion",
                                 "confirmación sobre")
        resultado["latido"] = cuerpo["latido"]
        resultado["linaje"] = len(cuerpo["linaje"])
        return resultado

    # =====================================================================
    #  G-A8 mitad DETECTABLE   ·   10 · recuperar tras caída
    # =====================================================================
    def verificar_refs(self):
        """Denuncia un forzado contrastando el LINAJE DURABLE contra las refs vivas.

        No consulta el hook, no consulta el reflog y no confía en ninguna bandera: si una
        cabeza que este gobierno publicó ha dejado de ser alcanzable desde la cabeza actual,
        alguien movió la ref fuera de su linaje. Eso es cierto tanto si el hook estaba
        puesto como si lo quitaron para poder forzar.
        """
        informe = {"refs": [], "forzados": [], "hook": None}
        try:
            informe["hook"] = self.comprobar_hook()["digest"]
        except HookAusente as fallo:
            informe["hook"] = None
            informe["hook_diagnostico"] = fallo.detalle
        for logica in sorted(self.almacen.listar(DOMINIO)):
            concesion = self.almacen.leer(logica)
            # FALLO CERRADO ante un objeto del dominio que no es una concesión. Un
            # `KeyError` aquí sería una traza cruda al usuario, y seguir adelante ignorando
            # el objeto convertiría un estado inconsistente en un verde.
            faltan = [clave for clave in ("ref", "cabeza", "linaje")
                      if clave not in concesion]
            if faltan:
                raise PoliticaViolada(
                    "hay un objeto en el dominio `" + DOMINIO + "` que no es una concesión "
                    "de ref: le faltan " + ", ".join(faltan),
                    ruta=logica,
                )
            ref = concesion["ref"]
            existe, cabeza = self.canal.existe_ref(ref)
            fila = {
                "ref": ref,
                "registrada": concesion["cabeza"],
                "viva": cabeza if existe else NULO,
                "linaje": len(concesion["linaje"]),
                "coherente": True,
            }
            if not existe:
                if concesion["linaje"]:
                    fila["coherente"] = False
                    informe["forzados"].append(
                        {"ref": ref, "causa": "la ref registrada ha DESAPARECIDO"}
                    )
                informe["refs"].append(fila)
                continue
            huerfanas = [
                publicada for publicada in concesion["linaje"]
                if not self.canal.es_antecesor(publicada, cabeza) and publicada != cabeza
            ]
            if huerfanas:
                fila["coherente"] = False
                fila["huerfanas"] = [valor[:12] for valor in huerfanas]
                informe["forzados"].append({
                    "ref": ref,
                    "causa": "cabezas publicadas ya NO alcanzables desde la cabeza viva",
                    "huerfanas": [valor[:12] for valor in huerfanas],
                    "viva": cabeza[:12],
                })
            informe["refs"].append(fila)
        informe["ok"] = not informe["forzados"]
        return informe

    def exigir_refs_intactas(self):
        """`verificar_refs()` con fallo cerrado: es la forma que usa una comprobación."""
        informe = self.verificar_refs()
        if not informe["ok"]:
            primero = informe["forzados"][0]
            raise ForzadoDetectado(
                "FORZADO DETECTADO sobre `" + primero["ref"] + "`: " + primero["causa"]
                + ". El linaje registrado en el estado durable no lo respalda",
                ruta=primero["ref"],
                huerfanas=primero.get("huerfanas", []),
            )
        return informe

    def recuperar(self):
        """10 · recuperar tras caída: el almacén cierra su ventana y las refs se contrastan."""
        informe_estado = self.almacen.recuperar().a_dict()
        informe_refs = self.verificar_refs()
        return {
            "estado": {
                "rama": informe_estado["rama"],
                "ventana_previa": informe_estado["ventana_previa"],
                "marcadas": informe_estado["marcadas"],
            },
            "refs": informe_refs,
            "ok": informe_refs["ok"] and not informe_estado["marcadas"],
        }

    # =====================================================================
    #  11 · evidencia auditable
    # =====================================================================
    def evidencia(self):
        """Forma determinista y publicable del gobierno. Sin rutas absolutas, sin secretos."""
        revision = self.almacen.revision()
        return {
            "politica": self.politica.a_dict(),
            "titular": self.titular,
            "revision": revision["revision"],
            "revision_id": revision["revision_id"],
            "ventana": self.almacen.estado_de_la_ventana(),
            "refs": self.verificar_refs(),
            "hook_esperado": DIGEST_DEL_HOOK,
        }


def inicializar(ruta_control_repo, *, titular, politica=None):
    """Funda el gobierno sobre un control repo: almacén, hook y concesión de la canónica."""
    ruta = os.path.abspath(ruta_control_repo)
    canal = CanalGit(ruta, autor=titular)
    codigo, _, _ = canal.ejecutar("rev-parse", "--git-dir", exigir_exito=False)
    if codigo != 0:
        canal.ejecutar("init", "--quiet", "--initial-branch=canonica")
    try:
        almacen = estado.abrir(ruta)
    except estado.AlmacenNoInicializado:
        almacen = estado.inicializar(ruta)
    gobierno = GobiernoDelControlRepo(ruta, titular=titular, politica=politica,
                                      almacen=almacen)
    gobierno._propio = True
    gobierno.instalar_hook()
    return gobierno
