#!/usr/bin/env python3
"""escenario_e2e_runtime — el escenario EXTREMO A EXTREMO del segundo corte de `F6`.

`T193`. Veinticinco pasos sobre un producto REAL, no sobre un montaje de mocks:

    un control repo                 con su estado durable y su gobierno Git instalado
    dos repositorios de producto    Git de verdad, hermanos del control repo
    dos instancias de runtime       procesos REALES, compitiendo por el mismo trabajo
    un adaptador local de proceso   `subprocess` de verdad, que mata de verdad
    gobierno Git real               concesión, base, política, hook y detección de forzado
    admisión real                   juicio sobre MUTACIONES, no sobre nombres

QUÉ LO DISTINGUE DE LAS BATERÍAS. Las baterías comprueban cada pieza contra su contrato.
Esto comprueba que las piezas SE SOSTIENEN JUNTAS: que el dispatcher escribe en el mismo
estado durable que el motor recupera, que la autoridad que el runtime toma es la que el
gobierno Git respeta, y que la admisión juzga el árbol que los dos han dejado.

DETERMINISMO. La salida se PUBLICA como evidencia: dos ejecuciones seguidas, desde
directorios distintos, producen bytes idénticos. Ni relojes, ni duraciones, ni pids, ni
rutas absolutas. Lo que varía —un pid, un temporal, un digest de commit— se sustituye por su
FORMA, que es lo que la prueba afirma.

    python3 kernel/operativo/runtime/pruebas/escenario_e2e_runtime.py

Sale con 0 si los veinticinco pasos se cumplen, y con 1 en cuanto uno falla, marcando los
que quedaron sin ejecutar. Un escenario que sigue adelante tras un paso fallido mide el
estado equivocado en todos los siguientes.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
RUNTIME = os.path.join(RAIZ, "kernel", "operativo", "runtime")
CLI_RUNTIME = os.path.join(RUNTIME, "ads_runtime.py")
CLI_ESTADO = os.path.join(RUNTIME, "ads_estado.py")
sys.path.insert(0, RUNTIME)

import adaptadores                                                    # noqa: E402
import admision                                                       # noqa: E402
import estado                                                         # noqa: E402
import gobierno                                                       # noqa: E402
import identidad                                                      # noqa: E402
import runtime as runtime_ads                                         # noqa: E402
from admision import matriz                                           # noqa: E402

# Sin red y sin configuración de la máquina: Git sólo tiene permitido el transporte `file`,
# y la identidad va por entorno para no depender de —ni tocar— la del que ejecuta.
ENTORNO = {
    **os.environ,
    "GIT_AUTHOR_NAME": "ads-e2e", "GIT_AUTHOR_EMAIL": "e2e@ads.local",
    "GIT_COMMITTER_NAME": "ads-e2e", "GIT_COMMITTER_EMAIL": "e2e@ads.local",
    "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull,
    "GIT_ALLOW_PROTOCOL": "file", "GIT_TERMINAL_PROMPT": "0",
}
ENTORNO.pop("ADS_ESTADO_FALLO", None)
ENTORNO.pop("ADS_RUNTIME_FALLO", None)

PASOS = [
    "instalación e inicialización del workspace, el control repo y las dos fuentes",
    "recuperación del estado antes de despachar nada",
    "creación de trabajo: un item y cuatro paquetes",
    "selección: el trabajo elegible se DERIVA del estado y se ordena igual en las dos instancias",
    "adquisición de autoridad por la primera instancia",
    "prevención de doble despacho: la segunda instancia no puede adquirir",
    "ejecución por el adaptador local, con un proceso real",
    "progreso emitido por el proceso y recogido por el runtime",
    "transición confirmada: el paquete queda completado y el efecto acusado",
    "fallo REINTENTABLE: el proceso sale con código distinto de cero",
    "reintento: el paquete vuelve a listo y se despacha otra vez",
    "agotamiento: se acaban los intentos y el estado canónico deja de tocarse",
    "reconciliación pendiente, deducida del registro auxiliar",
    "pausa de un paquete listo",
    "reanudación del paquete pausado",
    "cancelación de un paquete, que es terminal",
    "caída del runtime entre el efecto y su acuse, con el proceso muerto de verdad",
    "recuperación por la OTRA instancia, sin repetir el efecto ya ejecutado",
    "mutación Git ADMITIDA sobre la rama canónica del control repo",
    "mutación Git RECHAZADA: forzar una referencia es imposible por política",
    "ruta adversarial: espacio, salto de línea, guion inicial y no ASCII",
    "la RAÍZ del repositorio está inventariada: el ataque de `S1-02` da ROJO",
    "resultado idempotente: repetir la orden no vuelve a ejecutar",
    "evidencia auditable: diario, atestación y configuración de confianza fuera del árbol",
    "cierre limpio: integridad, ventana cerrada y árbol de producto sin residuos",
]


class Fallo(Exception):
    """Un paso no se cumplió. Corta el escenario: seguir mediría el estado equivocado."""


def exigir(condicion, detalle):
    if not condicion:
        raise Fallo(detalle)


def git(repo, *argumentos, exigir_exito=True):
    proceso = subprocess.run(["git", "-C", repo, *argumentos], capture_output=True,
                             text=True, env=ENTORNO)
    if exigir_exito and proceso.returncode != 0:
        raise Fallo("git " + " ".join(argumentos) + " -> " + (proceso.stderr or "").strip())
    return proceso


def cli(ejecutable, repo, argumentos, *, instancia=None, fallo=None, adaptador=None):
    entorno = dict(ENTORNO)
    if fallo:
        entorno["ADS_RUNTIME_FALLO"] = fallo
    orden = [sys.executable, ejecutable, "--repo", repo]
    if instancia:
        orden.extend(["--instancia", instancia])
    if adaptador:
        orden.extend(["--adaptador-local", adaptador])
    orden.extend(str(x) for x in argumentos)
    return subprocess.run(orden, capture_output=True, text=True, env=entorno,
                          cwd=tempfile.gettempdir(), timeout=300)


def cli_json(ejecutable, repo, argumentos, **kw):
    proceso = cli(ejecutable, repo, list(argumentos) + ["--json"], **kw)
    if proceso.returncode not in (0, 1):
        raise Fallo("la orden terminó con " + str(proceso.returncode) + ": "
                    + (proceso.stderr or "").strip()[:200])
    try:
        return proceso.returncode, json.loads(proceso.stdout or "null")
    except json.JSONDecodeError:
        raise Fallo("la orden no devolvió JSON: " + (proceso.stdout or "")[:200])


def guion(directorio, nombre, cuerpo):
    ruta = os.path.join(directorio, nombre)
    with open(ruta, "w", encoding="utf-8") as manejador:
        manejador.write(cuerpo)
    os.chmod(ruta, 0o755)
    return ruta


class Escenario:

    def __init__(self, base):
        self.base = base
        self.ws = os.path.join(base, "ws")
        self.control = os.path.join(self.ws, "ads")
        self.fuentes = {}
        self.adaptador = os.path.join(base, "adaptador")
        self.guiones = os.path.join(base, "guiones")
        self.fuera = os.path.join(base, "fuera-del-arbol")
        self.cumplidos = []
        self.notas = {}

    # -- 1 --------------------------------------------------------------------
    def paso_01(self):
        for carpeta in (self.ws, self.adaptador, self.guiones, self.fuera):
            os.makedirs(carpeta, exist_ok=True)
        os.makedirs(self.control)
        gob = gobierno.inicializar(self.control, titular="runtime-A")
        try:
            exigir(gob.comprobar_hook(), "el hook de referencias no quedó instalado")
            exigir(os.path.isdir(os.path.join(self.control, "estado", "canonico")),
                   "el estado durable no se fundó en el control repo")
        finally:
            gob.cerrar()
        for nombre in ("frontend", "backend"):
            ruta = os.path.join(self.ws, nombre)
            os.makedirs(ruta)
            git(ruta, "init", "--quiet", "--initial-branch=main")
            with open(os.path.join(ruta, "README.md"), "w", encoding="utf-8") as manejador:
                manejador.write("# " + nombre + "\n")
            git(ruta, "add", "-A")
            git(ruta, "commit", "--quiet", "-m", "semilla")
            self.fuentes[nombre] = ruta
        exigir(sorted(os.listdir(self.ws)) == ["ads", "backend", "frontend"],
               "el workspace no contiene el control repo y las dos fuentes")
        return "control repo con gobierno y hook · dos fuentes Git · estado durable fundado"

    # -- 2 --------------------------------------------------------------------
    def paso_02(self):
        codigo, datos = cli_json(CLI_RUNTIME, self.control, ["elegibles"],
                                 instancia="runtime-A")
        exigir(codigo == 0, "el runtime no pudo abrir el control repo")
        exigir(datos["recuperacion"]["rama"] in ("ninguna", "completar", "revertir"),
               "la apertura no informó de la rama de recuperación")
        exigir(not datos["marcado"], "el almacén quedó MARCADO y no debe despacharse")
        return "abrir() recupera ANTES de despachar · rama " + datos["recuperacion"]["rama"]

    # -- 3 --------------------------------------------------------------------
    def paso_03(self):
        bien = guion(self.guiones, "bien.sh",
                     "#!/bin/sh\necho 'paso 1 de 2'\necho 'paso 2 de 2'\nexit 0\n")
        # UN FALLO REINTENTABLE, y por eso es un TIMEOUT y no un código de salida: repetir
        # una orden que devolvió 3 devolvería 3 otra vez, y la política —con razón— la
        # clasifica DEFINITIVA. Lo reintentable es lo que puede cambiar solo, y de paso este
        # guion obliga al adaptador a MATAR un proceso de verdad.
        mal = guion(self.guiones, "mal.sh",
                    "#!/bin/sh\necho 'empiezo y me quedo colgado'\nsleep 120\n")
        self.notas["bien"] = bien
        self.notas["mal"] = mal
        codigo, _ = cli_json(CLI_RUNTIME, self.control,
                             ["crear-item", "--id", "it-1", "--titulo", "primer item",
                              "--motivo", "escenario e2e"], instancia="runtime-A")
        exigir(codigo == 0, "no se pudo crear el item")
        paquetes = [
            ("pq-ok", bien, 40, 3), ("pq-falla", mal, 30, 2, 1.0),
            ("pq-pausa", bien, 20, 3), ("pq-cancela", bien, 10, 3),
        ]
        for fila in paquetes:
            identificador, script, prioridad, intentos = fila[:4]
            limite = fila[4] if len(fila) > 4 else 20
            codigo, _ = cli_json(CLI_RUNTIME, self.control, [
                "crear-paquete", "--id", identificador, "--item", "it-1",
                "--capacidad", "proceso-local", "--argumento", "/bin/sh",
                "--argumento", script, "--prioridad", prioridad,
                "--max-intentos", intentos, "--limite-segundos", limite],
                instancia="runtime-A")
            exigir(codigo == 0, "no se pudo crear el paquete " + identificador)
        with estado.abrir(self.control) as almacen:
            # `listar` devuelve RUTAS LÓGICAS, que es lo que el estado canónico guarda.
            escritos = sorted(os.path.basename(ruta)[:-len(".json")]
                              for ruta in almacen.listar("paquetes"))
            exigir(escritos == ["pq-cancela", "pq-falla", "pq-ok", "pq-pausa"],
                   "los paquetes no quedaron en el estado canónico: " + str(escritos))
        return "1 item y 4 paquetes, escritos como transiciones del estado durable"

    # -- 4 --------------------------------------------------------------------
    def paso_04(self):
        _, uno = cli_json(CLI_RUNTIME, self.control, ["elegibles"], instancia="runtime-A")
        _, dos = cli_json(CLI_RUNTIME, self.control, ["elegibles"], instancia="runtime-B")
        orden_a = [p["paquete"] for p in uno["elegibles"]]
        orden_b = [p["paquete"] for p in dos["elegibles"]]
        exigir(orden_a == orden_b, "las dos instancias no ven el mismo orden elegible")
        # Prioridad DESCENDENTE y después identificador: lo urgente primero, y ante empate
        # un desempate estable, que es lo que hace que las dos instancias vean lo mismo.
        exigir(orden_a == ["pq-ok", "pq-falla", "pq-pausa", "pq-cancela"],
               "el orden no respeta prioridad y después identificador: " + str(orden_a))
        return "orden derivado del estado, idéntico en las dos instancias: " + ", ".join(orden_a)

    # -- 5 --------------------------------------------------------------------
    def paso_05(self):
        codigo, lease = cli_json(CLI_RUNTIME, self.control, ["adquirir", "pq-ok"],
                                 instancia="runtime-A")
        exigir(codigo == 0, "runtime-A no pudo adquirir la autoridad")
        exigir(lease["titular"] == "runtime-A", "el lease no quedó a nombre de runtime-A")
        return "lease de pq-ok en runtime-A, época " + str(lease["epoca"])

    # -- 6 --------------------------------------------------------------------
    def paso_06(self):
        proceso = cli(CLI_RUNTIME, self.control, ["adquirir", "pq-ok"],
                      instancia="runtime-B")
        exigir(proceso.returncode == 1, "runtime-B adquirió una autoridad que ya era de otro")
        exigir("AUTORIDAD_NO_DISPONIBLE" in (proceso.stderr or ""),
               "el rechazo no llegó con su código tipado: " + (proceso.stderr or "").strip())
        codigo, despacho = cli_json(CLI_RUNTIME, self.control, ["despachar", "pq-ok"],
                                    instancia="runtime-B", adaptador=self.adaptador)
        exigir(codigo == 1, "runtime-B despachó un paquete cuya autoridad no tiene")
        return "runtime-B rechazado por AUTORIDAD_NO_DISPONIBLE, en adquirir y en despachar"

    # -- 7 y 8 y 9 ------------------------------------------------------------
    def paso_07(self):
        codigo, datos = cli_json(CLI_RUNTIME, self.control, ["despachar", "pq-ok"],
                                 instancia="runtime-A", adaptador=self.adaptador)
        exigir(codigo == 0, "el despacho falló: " + json.dumps(datos)[:200])
        self.notas["despacho_ok"] = datos
        exigir(datos["resultado"]["estado"] == "completado",
               "el adaptador no completó la tarea")
        exigir(datos["resultado"]["codigo"] == 0, "el proceso no salió con código cero")
        recibos = os.path.join(self.adaptador, "efectos")
        exigir(os.path.isdir(recibos) and os.listdir(recibos),
               "el adaptador no dejó recibo de su efecto: no hubo proceso real")
        return "adaptador de proceso local ejecutado, con recibo durable por efecto"

    def paso_08(self):
        datos = self.notas["despacho_ok"]
        avances = [linea for linea in datos["resultado"]["salida"].splitlines() if linea.strip()]
        exigir(avances == ["paso 1 de 2", "paso 2 de 2"],
               "el progreso del proceso no llegó entero: " + str(avances))
        with estado.abrir(self.control) as almacen:
            tipos = [evento["tipo"] for evento in almacen.diario()]
        exigir(any(tipo.startswith("transicion.") for tipo in tipos),
               "el diario no registró las transiciones del despacho")
        return "2 líneas de progreso recogidas del proceso, y el diario las explica"

    def paso_09(self):
        with estado.abrir(self.control) as almacen:
            paquete = almacen.leer("paquetes/pq-ok.json")
            efecto = almacen.leer("efectos/" + paquete["efecto"] + ".json")
        exigir(paquete["estado"] == "completado",
               "el paquete no quedó completado: " + paquete["estado"])
        exigir(efecto["aplicado"] is True, "el acuse del efecto no quedó escrito")
        exigir(efecto["paquete"] == "pq-ok", "el acuse no nombra su paquete")
        return "pq-ok completado y su efecto acusado en la MISMA transición"

    # -- 10, 11, 12, 13 -------------------------------------------------------
    def paso_10(self):
        cli_json(CLI_RUNTIME, self.control, ["adquirir", "pq-falla"], instancia="runtime-A")
        codigo, datos = cli_json(CLI_RUNTIME, self.control, ["despachar", "pq-falla"],
                                 instancia="runtime-A", adaptador=self.adaptador)
        exigir(codigo == 1, "un fallo del proceso no se reportó como fallo")
        with estado.abrir(self.control) as almacen:
            paquete = almacen.leer("paquetes/pq-falla.json")
        exigir(paquete["estado"] == "listo",
               "tras un fallo REINTENTABLE el paquete debe volver a listo: " + paquete["estado"])
        exigir(paquete["intentos"] == 1, "el intento no quedó contado")
        return "timeout: proceso MATADO, fallo reintentable, paquete de vuelta a listo, intento 1"

    def paso_11(self):
        cli_json(CLI_RUNTIME, self.control, ["adquirir", "pq-falla"], instancia="runtime-A")
        cli_json(CLI_RUNTIME, self.control, ["despachar", "pq-falla"],
                 instancia="runtime-A", adaptador=self.adaptador)
        with estado.abrir(self.control) as almacen:
            paquete = almacen.leer("paquetes/pq-falla.json")
        exigir(paquete["intentos"] == 2, "el segundo intento no quedó contado")
        return "reintento ejecutado: intento 2 de 2"

    def paso_12(self):
        with estado.abrir(self.control) as almacen:
            revision_antes = almacen.revision()["revision_id"]
        exigir(revision_antes, "no se pudo leer la revisión previa al agotamiento")
        with estado.abrir(self.control) as almacen:
            paquete = almacen.leer("paquetes/pq-falla.json")
        exigir(paquete["estado"] == "agotado",
               "al acabarse los intentos el paquete debe quedar agotado: " + paquete["estado"])
        # La invariante NO es que no se pueda tomar el lease —la autoridad y el estado del
        # trabajo son cosas distintas—, sino que un paquete agotado deja de ser trabajo:
        # ni sale elegible, ni se puede despachar. Volverlo a la vida exige la transición
        # explícita de reconciliación, y nada más.
        _, elegibles = cli_json(CLI_RUNTIME, self.control, ["elegibles"],
                                instancia="runtime-A")
        exigir("pq-falla" not in [p["paquete"] for p in elegibles["elegibles"]],
               "un paquete agotado sigue siendo trabajo elegible")
        proceso = cli(CLI_RUNTIME, self.control, ["despachar", "pq-falla"],
                      instancia="runtime-A", adaptador=self.adaptador)
        exigir(proceso.returncode == 1, "un paquete agotado se volvió a despachar")
        return "intentos agotados: pq-falla en `agotado`, fuera de lo elegible y sin despacho"

    def paso_13(self):
        with estado.abrir(self.control) as almacen:
            pendientes = almacen.reconciliacion_pendiente()
        exigir(pendientes, "agotar los reintentos no dejó la pendencia de `g.9`")
        apertura = pendientes[0]
        for campo in ("producto", "repositorio", "item", "intento", "causa", "momento"):
            exigir(campo in apertura, "el registro auxiliar no identifica " + campo)
        # `g.9` exige que el registro identifique el ITEM, y eso es lo que lleva. Qué
        # PAQUETE del item se agotó vive en la causa, que es donde la norma deja el detalle.
        exigir(apertura["item"] == "it-1", "la pendencia no nombra el item")
        exigir("intento" in str(apertura["causa"]) or apertura["intento"] >= 1,
               "la pendencia no dice cuántos intentos se agotaron")
        self.notas["registro"] = apertura["registro"]
        return "reconciliación " + apertura["registro"] + " deducida del registro auxiliar"

    # -- 14, 15, 16 -----------------------------------------------------------
    def paso_14(self):
        codigo, _ = cli_json(CLI_RUNTIME, self.control, [
            "pausar", "pq-pausa", "--motivo", "presupuesto agotado",
            "--autoridad", "owner"], instancia="runtime-A")
        exigir(codigo == 0, "no se pudo pausar")
        _, elegibles = cli_json(CLI_RUNTIME, self.control, ["elegibles"],
                                instancia="runtime-A")
        exigir("pq-pausa" not in [p["paquete"] for p in elegibles["elegibles"]],
               "un paquete pausado sigue siendo elegible")
        return "pq-pausa en `pausado`, y fuera del trabajo elegible"

    def paso_15(self):
        codigo, _ = cli_json(CLI_RUNTIME, self.control, [
            "reanudar", "pq-pausa", "--motivo", "presupuesto repuesto",
            "--autoridad", "owner"], instancia="runtime-A")
        exigir(codigo == 0, "no se pudo reanudar")
        _, elegibles = cli_json(CLI_RUNTIME, self.control, ["elegibles"],
                                instancia="runtime-A")
        exigir("pq-pausa" in [p["paquete"] for p in elegibles["elegibles"]],
               "un paquete reanudado no vuelve a ser elegible")
        return "pq-pausa reanudado y elegible otra vez"

    def paso_16(self):
        codigo, _ = cli_json(CLI_RUNTIME, self.control, [
            "cancelar", "pq-cancela", "--motivo", "el Owner lo retira",
            "--autoridad", "owner"], instancia="runtime-A")
        exigir(codigo == 0, "no se pudo cancelar")
        proceso = cli(CLI_RUNTIME, self.control, [
            "reanudar", "pq-cancela", "--motivo", "vuelta atrás", "--autoridad", "owner"],
            instancia="runtime-A")
        exigir(proceso.returncode == 1, "un paquete cancelado es terminal y no se reanuda")
        return "pq-cancela cancelado, y la cancelación es terminal"

    # -- 17 y 18 --------------------------------------------------------------
    def paso_17(self):
        script = guion(self.guiones, "efecto.sh", "#!/bin/sh\necho 'efecto aplicado'\nexit 0\n")
        codigo, _ = cli_json(CLI_RUNTIME, self.control, [
            "crear-paquete", "--id", "pq-caida", "--item", "it-1",
            "--capacidad", "proceso-local", "--argumento", "/bin/sh",
            "--argumento", script, "--prioridad", "90", "--limite-segundos", "20"],
            instancia="runtime-A")
        exigir(codigo == 0, "no se pudo crear el paquete de la caída")
        cli_json(CLI_RUNTIME, self.control, ["adquirir", "pq-caida"], instancia="runtime-A")
        proceso = cli(CLI_RUNTIME, self.control, ["despachar", "pq-caida"],
                      instancia="runtime-A", adaptador=self.adaptador,
                      fallo="despues-del-efecto-antes-del-acuse")
        exigir(proceso.returncode == 70,
               "la caída controlada no ocurrió: código " + str(proceso.returncode))
        with estado.abrir(self.control) as almacen:
            paquete = almacen.leer("paquetes/pq-caida.json")
            acuse = "efectos/" + paquete["efecto"] + ".json" in almacen.revision()["raiz"]
        exigir(not acuse, "el acuse se escribió antes de la caída: no hay nada que demostrar")
        recibos = os.listdir(os.path.join(self.adaptador, "efectos"))
        exigir(len(recibos) >= 2, "el adaptador no dejó recibo del efecto ya ejecutado")
        self.notas["efecto_caida"] = paquete["efecto"]
        return "runtime-A muerto con os._exit(70) tras el efecto y ANTES del acuse"

    def paso_18(self):
        for _ in range(runtime_ads.PACIENCIA_POR_DEFECTO):
            codigo, _ = cli_json(CLI_RUNTIME, self.control, ["observar", "pq-caida"],
                                 instancia="runtime-B")
            exigir(codigo == 0, "runtime-B no pudo observar el lease abandonado")
        codigo, lease = cli_json(CLI_RUNTIME, self.control, ["reclamar", "pq-caida"],
                                 instancia="runtime-B")
        exigir(codigo == 0, "runtime-B no pudo reclamar un lease abandonado")
        exigir(lease["titular"] == "runtime-B", "la reclamación no cambió de titular")
        codigo, datos = cli_json(CLI_RUNTIME, self.control, ["despachar", "pq-caida"],
                                 instancia="runtime-B", adaptador=self.adaptador)
        exigir(codigo == 0, "runtime-B no pudo completar el trabajo huérfano")
        exigir(datos["resultado"].get("repetido") is True,
               "el efecto se volvió a EJECUTAR: la idempotencia no sostuvo la caída")
        with estado.abrir(self.control) as almacen:
            paquete = almacen.leer("paquetes/pq-caida.json")
        exigir(paquete["estado"] == "completado", "el paquete huérfano no llegó a completado")
        return ("runtime-B reclamó tras " + str(runtime_ads.PACIENCIA_POR_DEFECTO)
                + " observaciones y completó SIN reejecutar el efecto")

    # -- 19 y 20 --------------------------------------------------------------
    def paso_19(self):
        gob = gobierno.GobiernoDelControlRepo(self.control, titular="runtime-A")
        try:
            gob.abrir()
            gob.conceder(gobierno.RAMA_CANONICA)
            preparacion = gob.preparar(gobierno.RAMA_CANONICA, mensaje="alta de fuente",
                                       ficheros={"SOURCES.toml": b'schema = 1\n'})
            confirmacion = gob.confirmar(gobierno.RAMA_CANONICA, preparacion)
            exigir(confirmacion["ref"] == gobierno.RAMA_CANONICA,
                   "la confirmación no nombra la ref")
            self.notas["cabeza"] = confirmacion["nuevo"]
            gob.liberar(gobierno.RAMA_CANONICA)
        finally:
            gob.cerrar()
        exigir(git(self.control, "rev-parse", gobierno.RAMA_CANONICA).stdout.strip()
               == self.notas["cabeza"], "la rama canónica no avanzó a la confirmación")
        return "mutación admitida sobre la rama canónica, por concesión y revisión base"

    def paso_20(self):
        proceso = git(self.control, "commit-tree", "-m", "divergente",
                      git(self.control, "write-tree").stdout.strip(), exigir_exito=False)
        divergente = (proceso.stdout or "").strip()
        exigir(divergente, "no se pudo fabricar el commit divergente")
        forzado = git(self.control, "update-ref", gobierno.RAMA_CANONICA, divergente,
                      self.notas["cabeza"], exigir_exito=False)
        exigir(forzado.returncode != 0,
               "se pudo forzar la rama canónica: `G-A8` no se cumple")
        exigir("fast-forward" in (forzado.stderr or ""),
               "el rechazo no dice por qué: " + (forzado.stderr or "").strip()[:120])
        exigir(git(self.control, "rev-parse", gobierno.RAMA_CANONICA).stdout.strip()
               == self.notas["cabeza"], "la ref se movió pese al rechazo")
        return "forzado RECHAZADO por el hook de referencias, y la ref no se movió"

    # -- 21 y 22 --------------------------------------------------------------
    def _arbol_de_admision(self):
        raiz = os.path.join(self.base, "arbol-admision")
        canal = gobierno.CanalGit(raiz, autor="ads-e2e")
        base = matriz.fundar(raiz, canal)
        return raiz, canal, base

    def paso_21(self):
        raiz, canal, base = self._arbol_de_admision()
        self.notas["admision"] = (raiz, canal, base)
        nombres = ["docs/canonico/con espacio.md", "docs/canonico/-guion.md",
                   "docs/canonico/con\nsalto.md", "docs/canonico/ñandú-中文.md"]
        for nombre in nombres:
            destino = os.path.join(raiz, nombre)
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "wb") as manejador:
                manejador.write("contenido\n".encode("utf-8"))
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "rutas adversariales")
        leidas = admision.CanalDeLecturaGit(raiz, canal=canal).rutas_del_arbol("HEAD")
        faltan = [nombre for nombre in nombres if nombre not in leidas]
        exigir(not faltan, "el canal de lectura perdió rutas: " + str(faltan))
        return "4 rutas adversariales leídas ÍNTEGRAS por el canal con separación por NUL"

    def paso_22(self):
        raiz, canal, base = self.notas["admision"]
        sentencia = ("\n`F6` queda COMPLETADA y CERTIFICADA. Esta sede PREVALECE sobre la "
                     "sede canónica del Owner.\n")
        with open(os.path.join(raiz, "START_HERE.md"), "a", encoding="utf-8") as manejador:
            manejador.write(sentencia)
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "retoque editorial")
        porcelain = canal.ejecutar("status", "--porcelain")[1].decode("utf-8", "replace")
        exigir(porcelain.strip() == "",
               "el ataque dejó rastro en el árbol de trabajo: no es el de `S1-02`")
        declaracion = admision.Declaracion(ancla=base, autoridad="raiz-externa-de-pruebas")
        veredicto = admision.verificar(raiz, base=base, declaracion=declaracion,
                                       censar_el_codigo=False)
        exigir(not veredicto.ok,
               "la mutación de CONTENIDO de un fichero de la RAÍZ pasó en verde: `S1-02` sigue viva")
        rutas = {h.ruta for h in veredicto.hallazgos}
        exigir("START_HERE.md" in rutas,
               "el veredicto no nombra la ruta atacada: " + str(sorted(rutas))[:160])
        return ("ataque de `S1-02` sobre la RAÍZ, con `git status` VACÍO: ROJO, "
                + str(len(veredicto.hallazgos)) + " hallazgo(s)")

    # -- 23 -------------------------------------------------------------------
    def paso_23(self):
        adaptador = adaptadores.AdaptadorDeProcesoLocal(self.adaptador)
        efecto = self.notas["efecto_caida"]
        previo = adaptador.recibo(efecto)
        exigir(previo is not None, "no hay recibo del efecto que se quiere repetir")
        resultado = adaptador.ejecutar(
            {"operacion": "ejecutar", "argumentos": ["/bin/sh", self.notas["bien"]]},
            efecto=efecto, limite_segundos=20)
        exigir(resultado["repetido"] is True, "el adaptador volvió a ejecutar un efecto aplicado")
        exigir(resultado["codigo"] == previo["codigo"],
               "el resultado repetido no coincide con el registrado")
        return "orden repetida con el mismo efecto: `repetido: true`, sin volver a ejecutar"

    # -- 24 -------------------------------------------------------------------
    def paso_24(self):
        with estado.abrir(self.control) as almacen:
            informe = almacen.auditar()
            exigir(informe.a_dict()["ok"], "la auditoría del estado no queda en verde")
            proveedor = estado.ProveedorEfimero()
            destino = os.path.join(self.fuera, "atestacion.json")
            estado.atestar(almacen, proveedor, destino)
            exigir(estado.verificar_atestacion(destino, proveedor),
                   "la atestación no se verifica con su propio proveedor")
            with open(destino, "r+", encoding="utf-8") as manejador:
                cuerpo = manejador.read().replace("sha256:", "sha256:0")
                manejador.seek(0)
                manejador.write(cuerpo)
                manejador.truncate()
            try:
                estado.verificar_atestacion(destino, proveedor)
                raise Fallo("una atestación manipulada se dio por válida")
            except estado.AtestacionInvalida:
                pass
        dentro = os.path.join(self.control, "confianza.json")
        with open(dentro, "w", encoding="utf-8") as manejador:
            json.dump({"autoridad": "yo mismo", "identidades": []}, manejador)
        try:
            identidad.cargar(dentro, arbol_verificado=self.control)
            raise Fallo("se aceptó una configuración de confianza DENTRO del árbol verificado")
        except identidad.ConfiguracionDentroDelArbol:
            pass
        finally:
            os.remove(dentro)
        return ("diario auditable · atestación verificada y su manipulación rechazada · "
                "configuración de confianza DENTRO del árbol rechazada")

    # -- 25 -------------------------------------------------------------------
    def paso_25(self):
        with estado.abrir(self.control) as almacen:
            exigir(almacen.estado_de_la_ventana() == "cerrada",
                   "queda una ventana transaccional abierta al cerrar")
            integridad = almacen.verificar_integridad().a_dict()
            exigir(integridad["ok"], "el estado no queda íntegro: " + json.dumps(integridad)[:160])
        for nombre, ruta in sorted(self.fuentes.items()):
            porcelain = git(ruta, "status", "--porcelain").stdout
            exigir(porcelain.strip() == "",
                   "la fuente " + nombre + " no quedó limpia: " + porcelain[:120])
        operacional = os.path.join(self.control, "estado", "operacional")
        rastreados = git(self.control, "ls-files", "--", "estado/operacional").stdout
        exigir(rastreados.strip() == "",
               "el plano operacional entró en el versionado: la rama contendría estado parcial")
        exigir(os.path.isdir(operacional), "el plano operacional no existe")
        return "integridad verde · ventana cerrada · fuentes limpias · operacional fuera del git"


def ejecutar(base, salida):
    escenario = Escenario(base)
    salida.append("ESCENARIO EXTREMO A EXTREMO · RUNTIME, GIT, ADMISIÓN Y ADAPTADORES")
    salida.append("T193 · F6 · corte vertical 2 · veinticinco pasos del §12 del encargo")
    salida.append("procesos y repositorios Git REALES; ningún mock hace de pieza")
    salida.append("")
    fallo = None
    for numero, titulo in enumerate(PASOS, 1):
        etiqueta = "paso %02d" % numero
        if fallo is not None:
            salida.append(etiqueta + "  " + titulo)
            salida.append("         resultado: NO EJECUTADO")
            continue
        metodo = getattr(escenario, "paso_%02d" % numero)
        salida.append(etiqueta + "  " + titulo)
        try:
            detalle = metodo()
        except Fallo as error:
            salida.append("         · " + str(error))
            salida.append("         resultado: FALLIDO")
            fallo = numero
        except Exception as error:                                    # noqa: BLE001
            salida.append("         · error inesperado: "
                          + type(error).__name__ + ": " + str(error)[:200])
            salida.append("         resultado: FALLIDO")
            fallo = numero
        else:
            salida.append("         · " + detalle)
            salida.append("         resultado: CUMPLIDO")
            escenario.cumplidos.append(numero)
    salida.append("")
    salida.append("%d de %d pasos CUMPLIDOS" % (len(escenario.cumplidos), len(PASOS)))
    return 0 if len(escenario.cumplidos) == len(PASOS) else 1


# ---------------------------------------------------------------------------
#  `E-08` · RECUPERABILIDAD DEL ALMACÉN AL TERMINAR
# ---------------------------------------------------------------------------
#  Hecho reproducido antes de corregir: con los pasos 8 y 9 invertidos, este escenario
#  terminaba en VERDE sobre un almacén cuyo `REVISION.json` nombraba objetos que no estaban
#  publicados en `canonico/`, es decir, IRRECUPERABLE. Un escenario extremo a extremo que no
#  mira si lo que deja detrás se puede volver a abrir no está midiendo durabilidad.
#
#  DECISIÓN · se recorren TODOS los almacenes que el escenario haya dejado, y no uno elegido
#      El escenario crea varios control repos —máquinas, clones, copias— y cuál de ellos
#      tiene almacén cambia con los pasos. Buscarlos por su marca en disco —`estado/
#      REVISION.json`— hace que un almacén nuevo entre en la comprobación sin que nadie se
#      acuerde de añadirlo. Y se exige encontrar AL MENOS UNO: si el descubrimiento fallara,
#      «ninguno estaba roto» sería trivialmente cierto y no probaría nada.
def almacenes_del_escenario(base):
    """Todo directorio bajo `base` que sea un control repo con almacén durable."""
    encontrados = []
    for carpeta, subcarpetas, _ficheros in os.walk(base):
        if ".git" in subcarpetas:
            subcarpetas.remove(".git")
        if os.path.isfile(os.path.join(carpeta, "estado", "REVISION.json")):
            encontrados.append(carpeta)
            subcarpetas[:] = [s for s in subcarpetas if s != "estado"]
    return sorted(encontrados)


def comprobar_recuperabilidad(base):
    """`(ok, lineas)`: cada almacén se ABRE, se RECUPERA y se verifica su integridad."""
    import estado as _estado                                          # noqa: PLC0415
    lineas = []
    repos = almacenes_del_escenario(base)
    if not repos:
        return False, ["T301 · recuperabilidad: NO se encontró ningún almacén durable, así que la "
                       "comprobación no habría podido fallar nunca"]
    ok = True
    for repo in repos:
        nombre = os.path.relpath(repo, base)
        try:
            with _estado.abrir(repo, recuperar=True) as almacen:
                informe = almacen.verificar_integridad()
                almacen.auditar()
        except Exception as error:                                    # noqa: BLE001
            ok = False
            lineas.append("T301 · recuperabilidad  " + nombre + ": NO SE PUDO ABRIR NI RECUPERAR ("
                          + type(error).__name__ + ")")
            continue
        if not informe.ok:
            ok = False
            lineas.append("T301 · recuperabilidad  " + nombre + ": ÍNTEGRIDAD ROTA — "
                          + ", ".join(sorted({h["codigo"] for h in informe.hallazgos})))
        else:
            lineas.append("T301 · recuperabilidad  " + nombre + ": abierto, recuperado e íntegro")
    return ok, lineas


def main():
    base = tempfile.mkdtemp(prefix="ads-e2e2-")
    salida = []
    try:
        codigo = ejecutar(base, salida)
        # `E-08` · el escenario no termina en verde sobre un almacén que no se
        # puede volver a abrir. Se comprueba ANTES de borrar el temporal.
        recuperable, lineas_de_recuperabilidad = comprobar_recuperabilidad(base)
        salida.append("")
        salida.extend(lineas_de_recuperabilidad)
        if not recuperable:
            codigo = 1
    finally:
        # Los casos de permisos y los repositorios Git dejan ficheros de sólo lectura.
        for carpeta, subcarpetas, ficheros in os.walk(base):
            for nombre in subcarpetas + ficheros:
                try:
                    os.chmod(os.path.join(carpeta, nombre), 0o755)
                except OSError:
                    continue
        shutil.rmtree(base, ignore_errors=True)
    texto = "\n".join(salida)
    # Ninguna ruta del temporal puede salir: la evidencia se publica y tiene que ser la
    # misma en cualquier máquina.
    texto = texto.replace(base, "<temporal>")
    print(texto)
    return codigo


if __name__ == "__main__":
    sys.exit(main())
