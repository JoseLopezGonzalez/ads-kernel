#!/usr/bin/env python3
"""escenario_extremo_a_extremo — los QUINCE pasos del §12.1 del CONTRATO DEL CORTE.

Es la demostración de extremo a extremo del MOTOR DE ESTADO DURABLE: un control repo que
nace, recibe transiciones, SUFRE UNA CAÍDA REAL, se recupera sin perder lo confirmado y sin
publicar lo incompleto, choca con una revisión obsoleta, agota reintentos contra un
bloqueo retenido por otro proceso, produce el registro auxiliar de `g.9`, lo resuelve por
transición explícita y termina íntegro y auditable.

TRES COSAS QUE LO DISTINGUEN DE UNA PRUEBA CORRIENTE:

  · TODO se ejecuta con el CLI en PROCESOS REALES. Ni un solo paso llama a la API en
    memoria. La caída del paso 5 es `os._exit(70)` disparado por `ADS_ESTADO_FALLO`: el
    proceso muere sin `finally` y sin vaciar buffers, que es lo que hace un corte de luz.
    El paso 10 retiene el `flock` del escritor desde otro proceso de verdad.

  · La salida es DETERMINISTA, y esa es una condición del encargo, no un adorno. No se
    imprime ni una hora, ni una duración, ni un pid, ni una ruta absoluta. Dos ejecuciones
    seguidas producen BYTES IDÉNTICOS —compruébese con `diff`—, porque esta salida se
    publica como evidencia y una evidencia que cambia sola deja de mirarse.

  · Cada paso declara QUÉ debe haber pasado antes de mirarlo. Un escenario que acepta «lo
    que salga» no distingue un motor correcto de uno que publica mezclas parciales.

    python3 kernel/operativo/runtime/pruebas/escenario_extremo_a_extremo.py

Sale con 0 sólo si los quince pasos se cumplen. Se ejecuta desde cualquier directorio: la
raíz se deriva de `__file__` y nunca del `cwd`.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
RUNTIME = os.path.join(RAIZ, "kernel", "operativo", "runtime")
CLI = os.path.join(RUNTIME, "ads_estado.py")
sys.path.insert(0, RUNTIME)

# El entorno no hereda `ADS_ESTADO_FALLO`: si alguien lo tuviera puesto, el escenario
# moriría en el paso 3 y el informe culparía al motor de algo que no ha hecho.
ENTORNO = {k: v for k, v in os.environ.items() if k != "ADS_ESTADO_FALLO"}

CODIGO_SALIDA_CAIDA = 70
ESPERA = 120

# Retenedor del bloqueo del paso 10: un proceso real que toma el `flock` exclusivo del
# escritor y no lo suelta hasta que aparece el fichero de relevo.
GUION_RETENEDOR = """\
import fcntl, os, sys, time
cerrojo, listo, relevo = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(os.path.dirname(cerrojo), exist_ok=True)
fd = os.open(cerrojo, os.O_RDWR | os.O_CREAT, 0o644)
fcntl.flock(fd, fcntl.LOCK_EX)
open(listo, "w").close()
limite = time.monotonic() + 120
while not os.path.exists(relevo) and time.monotonic() < limite:
    time.sleep(0.01)
"""

TITULOS = [
    "inicializar el estado de un control repo temporal",
    "leer la revisión inicial",
    "aplicar una transición válida",
    "escribir estado y diario de forma durable",
    "simular una interrupción en un punto controlado",
    "reiniciar el proceso",
    "recuperar sin perder una transición confirmada",
    "comprobar que una transición incompleta no se publicó",
    "detectar un escritor concurrente o una revisión obsoleta",
    "agotar reintentos en un escenario dirigido",
    "comprobar que se creó el registro auxiliar de reconciliación",
    "deducir reconciliacion-pendiente",
    "resolverla mediante una transición explícita",
    "conservar evidencia auditable",
    "terminar con un estado íntegro y reproducible",
]


class FalloDelPaso(Exception):
    """Un paso no cumplió lo que había declarado. Corta el escenario."""


# Lecturas que CIERRAN. Un `open(...).read()` suelto deja el descriptor a merced del
# recolector y CPython avisa con un `ResourceWarning` que lleva dentro la ruta del
# temporal: una ruta absoluta y aleatoria en una salida que tiene que ser determinista.
def texto_de(ruta, **kw):
    with open(ruta, encoding="utf-8", **kw) as fh:
        return fh.read()


def bytes_de(ruta):
    with open(ruta, "rb") as fh:
        return fh.read()


def lineas_json(ruta):
    """Los eventos de un JSONL, ya decodificados. Es la lectura más repetida de aquí."""
    return [json.loads(linea) for linea in texto_de(ruta).splitlines() if linea.strip()]


def contiene(datos, aguja):
    """¿Aparece `aguja` en cualquier lugar de una estructura JSON?

    Se busca por VALOR y no por nombre de campo a propósito: el §11 fija las órdenes del
    CLI, no la forma exacta de su JSON, y el escenario no debe romperse porque el motor
    llame `registro` a lo que aquí se llamaría de otro modo.
    """
    if isinstance(datos, dict):
        return any(contiene(v, aguja) for v in datos.values())
    if isinstance(datos, list):
        return any(contiene(v, aguja) for v in datos)
    return aguja in datos if isinstance(datos, str) else False


class Escenario:

    def __init__(self):
        self.tmp = tempfile.mkdtemp(prefix="ads-e2e-")
        self.repo = os.path.join(self.tmp, "control")
        os.makedirs(self.repo)
        self.cargas = os.path.join(self.tmp, "cargas")
        os.makedirs(self.cargas)
        self.retenedor_py = os.path.join(self.tmp, "retenedor.py")
        with open(self.retenedor_py, "w", encoding="utf-8") as fh:
            fh.write(GUION_RETENEDOR)
        self.lineas = []
        self.estado_de_los_pasos = ["NO EJECUTADO"] * 15
        self.paso_actual = 0

    # -- salida ---------------------------------------------------------------------
    def emitir(self, texto=""):
        self.lineas.append(texto)

    def hecho(self, texto):
        self.emitir(f"         · {texto}")

    def exigir(self, condicion, explicacion):
        if not condicion:
            raise FalloDelPaso(explicacion)

    # -- ejecución de órdenes -------------------------------------------------------
    def cli(self, argumentos, *, fallo=None):
        entorno = dict(ENTORNO)
        if fallo:
            entorno["ADS_ESTADO_FALLO"] = fallo
        return subprocess.run(
            [sys.executable, CLI, "--repo", self.repo] + [str(a) for a in argumentos],
            capture_output=True, text=True, env=entorno, timeout=ESPERA,
            cwd=tempfile.gettempdir())

    def json_de(self, argumentos):
        proceso = self.cli(list(argumentos) + ["--json"])
        self.exigir(proceso.returncode == 0,
                    f"`{argumentos[0]}` salió con {proceso.returncode}")
        try:
            return json.loads(proceso.stdout)
        except json.JSONDecodeError as exc:
            raise FalloDelPaso(f"`{argumentos[0]} --json` no devolvió JSON: {exc}")

    def revision(self):
        return self.json_de(["revision"])

    def carga(self, nombre, datos):
        ruta = os.path.join(self.cargas, nombre + ".json")
        with open(ruta, "w", encoding="utf-8") as fh:
            json.dump(datos, fh, ensure_ascii=False, sort_keys=True, indent=2)
            fh.write("\n")
        return ruta

    def transicion(self, ident, ruta, datos, *, base, fallo=None, motivo="escenario e2e"):
        return self.cli(["transicion", "--id", ident, "--autor", "escenario-e2e",
                         "--motivo", motivo, "--base", base,
                         "--escribir", f"{ruta}={self.carga(ident, datos)}"], fallo=fallo)

    @staticmethod
    def codigo_de_error(proceso):
        hallados = re.findall(r"\b[A-Z][A-Z0-9_]{5,}\b", proceso.stderr or "")
        return hallados[0] if hallados else "(sin código)"

    # ================================================================== los 15 pasos
    def ejecutar(self):
        self.emitir("ESCENARIO EXTREMO A EXTREMO · MOTOR DE ESTADO DURABLE")
        self.emitir("T180 · F6 · corte vertical 1 · quince pasos del §12.1 del contrato")
        self.emitir("todo con el CLI en procesos reales; la caída es os._exit(70)")
        self.emitir()

        pasos = [self.paso_01, self.paso_02, self.paso_03, self.paso_04, self.paso_05,
                 self.paso_06, self.paso_07, self.paso_08, self.paso_09, self.paso_10,
                 self.paso_11, self.paso_12, self.paso_13, self.paso_14, self.paso_15]
        for indice, funcion in enumerate(pasos):
            self.paso_actual = indice
            self.emitir(f"paso {indice + 1:02d}  {TITULOS[indice]}")
            try:
                funcion()
            except FalloDelPaso as fallo:
                self.estado_de_los_pasos[indice] = "FALLIDO"
                self.hecho(f"FALLO: {fallo}")
                self.emitir("         resultado: FALLIDO")
                break
            except (subprocess.TimeoutExpired, OSError, ValueError, KeyError) as error:
                self.estado_de_los_pasos[indice] = "FALLIDO"
                self.hecho(f"FALLO inesperado: {type(error).__name__}")
                self.emitir("         resultado: FALLIDO")
                break
            self.estado_de_los_pasos[indice] = "CUMPLIDO"
            self.emitir("         resultado: CUMPLIDO")
        self.resumen()

    # -- 1 --------------------------------------------------------------------------
    def paso_01(self):
        """DEBE: crear el almacén, publicar la revisión 0 y excluir lo operacional."""
        proceso = self.cli(["inicializar", "--json"])
        self.exigir(proceso.returncode == 0,
                    f"`inicializar` salió con {proceso.returncode}")
        self.exigir(os.path.isfile(os.path.join(self.repo, "estado", "FORMATO.json")),
                    "no se escribió FORMATO.json")
        ignorar = os.path.join(self.repo, "estado", ".gitignore")
        self.exigir(os.path.isfile(ignorar), "falta estado/.gitignore (`g.14`)")
        with open(ignorar, encoding="utf-8") as fh:
            self.exigir("operacional" in fh.read(),
                        "estado/.gitignore no excluye operacional/: la rama canónica "
                        "podría contener estado parcial")
        self.hecho("almacén creado, con lo operacional excluido de la rama canónica")

    # -- 2 --------------------------------------------------------------------------
    def paso_02(self):
        """DEBE: la revisión 0 existe, no tiene padre y está explicada por el diario."""
        rev = self.revision()
        self.exigir(rev["revision"] == 0, f"la revisión inicial es {rev['revision']}")
        self.exigir(rev["padre"] is None, "la revisión 0 tiene padre")
        self.exigir(rev["esquema"] == "ads.estado/1", "esquema inesperado")
        self.exigir(rev["revision_id"].startswith("sha256:"),
                    "`revision_id` no es una identidad por contenido (`g.5`)")
        self.base_inicial = rev["revision_id"]
        self.hecho("revisión 0, sin padre, con identidad por contenido")

    # -- 3 --------------------------------------------------------------------------
    def paso_03(self):
        """DEBE: una transición válida se confirma y la revisión pasa a 1."""
        self.contenido_confirmado = {"esquema": "ads.estado/1", "item": "it-1", "n": 1}
        proceso = self.transicion("tx-0001", "items/it-1.json", self.contenido_confirmado,
                                  base=self.base_inicial)
        self.exigir(proceso.returncode == 0,
                    f"la transición válida salió con {proceso.returncode} "
                    f"({self.codigo_de_error(proceso)})")
        rev = self.revision()
        self.exigir(rev["revision"] == 1, f"la revisión es {rev['revision']}, se esperaba 1")
        self.exigir(rev["padre"] == self.base_inicial, "la revisión 1 perdió su linaje")
        self.revision_confirmada = rev
        self.hecho("revisión 1 publicada, con la revisión 0 como padre")

    # -- 4 --------------------------------------------------------------------------
    def paso_04(self):
        """DEBE: el estado se lee sin reproyectar, y el diario lo explica entero."""
        leido = self.json_de(["leer", "items/it-1.json"])
        self.exigir(contiene(leido, "it-1"),
                    "`leer` no devuelve el estado escrito: `I-g1` exige leerlo directo")
        ruta = os.path.join(self.repo, "estado", "canonico", "items", "it-1.json")
        self.exigir(os.path.isfile(ruta), "el objeto canónico no está en disco")
        diario = os.path.join(self.repo, "estado", "diario", "DIARIO.jsonl")
        eventos = lineas_json(diario)
        tipos = [e["tipo"] for e in eventos if e.get("transaccion", "").startswith("tx-0001")]
        for obligatorio in ("transicion.abierta", "transicion.preparada",
                            "transicion.confirmada"):
            self.exigir(obligatorio in tipos,
                        f"el diario no contiene {obligatorio} para la transición")
        for anterior, siguiente in zip(eventos, eventos[1:]):
            self.exigir(siguiente["previo"] == anterior["huella"],
                        "la cadena de hash del diario está rota")
        self.eventos_tras_confirmar = len(eventos)
        self.hecho(f"diario encadenado con {len(eventos)} eventos; abierta, preparada y "
                   f"confirmada presentes")

    # -- 5 --------------------------------------------------------------------------
    def paso_05(self):
        """DEBE: el proceso MUERE en el punto pedido, con 70, antes del no retorno.

        Se elige `despues-de-escribir-temporal`: hay objetos ya escritos en la zona de
        preparación pero todavía NO hay `transicion.preparada`, de modo que la ventana
        cae del lado de REVERTIR y el paso 8 puede exigir que no se publicara nada.
        """
        proceso = self.transicion("tx-0002", "items/it-2.json",
                                  {"esquema": "ads.estado/1", "item": "it-2", "n": 2},
                                  base=self.revision_confirmada["revision_id"],
                                  fallo="despues-de-escribir-temporal")
        self.exigir(proceso.returncode == CODIGO_SALIDA_CAIDA,
                    f"el punto de fallo no cortó el proceso: salió con "
                    f"{proceso.returncode}, se esperaba {CODIGO_SALIDA_CAIDA}")
        self.hecho("proceso terminado por os._exit(70) en despues-de-escribir-temporal")

    # -- 6 --------------------------------------------------------------------------
    def paso_06(self):
        """DEBE: un proceso NUEVO detecta la ventana sin haber presenciado la caída, y
        recuperar de nuevo NO vuelve a tocar nada.

        QUÉ SE MIDE, Y POR QUÉ NO EL INFORME. La idempotencia que el §3 exige es «invocada
        N veces produce el mismo ESTADO y no añade EVENTOS después de la primera pasada que
        resolvió la ventana». No exige que el informe sea igual, y no debe: la primera
        pasada tiene que poder decir que revirtió una ventana y las siguientes que no había
        nada que hacer. Un motor cuyas tres pasadas informasen de lo mismo estaría mintiendo
        en dos de las tres. Así que se compara lo DURABLE —los bytes del diario y los de
        `REVISION.json`— antes y después de las pasadas de más, que es donde vive la
        propiedad, y de paso se comprueba que el estado estacionario sí es estable.
        """
        proceso = self.cli(["recuperar", "--json"])
        self.exigir(proceso.returncode == 0,
                    f"`recuperar` salió con {proceso.returncode} "
                    f"({self.codigo_de_error(proceso)})")

        diario = os.path.join(self.repo, "estado", "diario", "DIARIO.jsonl")
        revision = os.path.join(self.repo, "estado", "REVISION.json")
        diario_tras_la_primera = bytes_de(diario)
        revision_tras_la_primera = bytes_de(revision)

        segunda = self.cli(["recuperar", "--json"])
        self.exigir(segunda.returncode == 0, "la segunda recuperación falló")
        tercera = self.cli(["recuperar", "--json"])
        self.exigir(tercera.returncode == 0, "la tercera recuperación falló")

        self.exigir(bytes_de(diario) == diario_tras_la_primera,
                    "recuperar de nuevo anexó eventos al diario: la pasada que cerró la "
                    "ventana ya la había resuelto, y el §3 prohíbe añadir nada después")
        self.exigir(bytes_de(revision) == revision_tras_la_primera,
                    "recuperar de nuevo movió la revisión publicada")
        self.exigir(tercera.stdout == segunda.stdout,
                    "dos recuperaciones sobre una ventana ya cerrada informan distinto: "
                    "el estado estacionario no es estable")
        self.hecho("proceso nuevo; dos pasadas de más no anexan al diario ni mueven la "
                   "revisión")

    # -- 7 --------------------------------------------------------------------------
    def paso_07(self):
        """DEBE: la transición YA CONFIRMADA del paso 3 sigue intacta tras la caída."""
        leido = self.json_de(["leer", "items/it-1.json"])
        self.exigir(contiene(leido, "it-1"),
                    "la recuperación se llevó por delante una transición confirmada")
        rev = self.revision()
        self.exigir(rev["revision"] >= self.revision_confirmada["revision"],
                    "la revisión retrocedió: se restauró algo ya publicado (`g.8`)")
        self.hecho("la transición confirmada antes de la caída sigue publicada y legible")

    # -- 8 --------------------------------------------------------------------------
    def paso_08(self):
        """DEBE: la transición interrumpida NO se publicó, y el diario lo explica."""
        rev = self.revision()
        self.exigir(rev["revision"] == self.revision_confirmada["revision"],
                    f"la revisión avanzó a {rev['revision']}: se publicó una transición "
                    f"que se interrumpió antes del punto de no retorno")
        self.exigir("items/it-2.json" not in rev["raiz"],
                    "la ruta interrumpida aparece en la raíz publicada")
        listado = self.json_de(["listar"])
        self.exigir(not contiene(listado, "it-2.json"),
                    "`listar` enumera un objeto que nunca se confirmó")
        diario = os.path.join(self.repo, "estado", "diario", "DIARIO.jsonl")
        tipos = [evento["tipo"] for evento in lineas_json(diario)]
        self.exigir("transicion.revertida" in tipos,
                    "se revirtió sin anotarlo: la reversión no es auditable (`g.13`)")
        self.exigir("transicion.marcada" not in tipos,
                    "se MARCÓ una ventana que sólo estaba abierta: `g.8` manda REVERTIR")
        self.hecho("mezcla parcial no publicada; reversión anotada en el diario")

    # -- 9 --------------------------------------------------------------------------
    def paso_09(self):
        """DEBE: una base obsoleta se rechaza con código tipado y sin tocar el estado."""
        rev_antes = self.revision()
        proceso = self.transicion("tx-0003", "items/it-3.json",
                                  {"esquema": "ads.estado/1", "item": "it-3", "n": 3},
                                  base=self.base_inicial)
        self.exigir(proceso.returncode == 1,
                    f"una base obsoleta salió con {proceso.returncode}, se esperaba 1")
        codigo = self.codigo_de_error(proceso)
        self.exigir(codigo == "REVISION_OBSOLETA",
                    f"el código de error es «{codigo}», se esperaba REVISION_OBSOLETA")
        self.exigir(self.revision() == rev_antes,
                    "el rechazo por base obsoleta modificó el estado")
        self.hecho("rechazo con REVISION_OBSOLETA y estado canónico intacto")

    # -- 10 -------------------------------------------------------------------------
    def paso_10(self):
        """DEBE: con el cerrojo retenido por OTRO proceso, se agotan los reintentos.

        Y agotarlos NO puede modificar el estado canónico (`g.6`).
        """
        rev_antes = self.revision()
        cerrojo = os.path.join(self.repo, "estado", "operacional", "escritor.lock")
        listo = os.path.join(self.tmp, "cerrojo-tomado")
        relevo = os.path.join(self.tmp, "suelta-el-cerrojo")
        retenedor = subprocess.Popen(
            [sys.executable, self.retenedor_py, cerrojo, listo, relevo],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=ENTORNO,
            cwd=tempfile.gettempdir())
        try:
            limite = time.monotonic() + 30
            while not os.path.exists(listo) and time.monotonic() < limite:
                time.sleep(0.01)
            self.exigir(os.path.exists(listo), "el retenedor no llegó a tomar el cerrojo")
            proceso = self.transicion("tx-0004", "items/it-4.json",
                                      {"esquema": "ads.estado/1", "item": "it-4", "n": 4},
                                      base=rev_antes["revision_id"])
            self.exigir(proceso.returncode == 1,
                        f"el escritor bloqueado salió con {proceso.returncode}: "
                        f"¿escribió sin tener el cerrojo?")
            codigo = self.codigo_de_error(proceso)
            self.exigir(codigo in ("REINTENTOS_AGOTADOS", "BLOQUEO_NO_ADQUIRIDO",
                                   "ESCRITOR_CONCURRENTE"),
                        f"el código de error es «{codigo}» y no describe el bloqueo")
        finally:
            open(relevo, "w").close()
            retenedor.communicate(timeout=ESPERA)
        self.exigir(self.revision() == rev_antes,
                    "agotar reintentos modificó el estado canónico (`g.6` lo prohíbe)")
        self.hecho(f"escritor serializado y detenido con {codigo}; órdenes intactas")

    # -- 11 -------------------------------------------------------------------------
    def paso_11(self):
        """DEBE: al agotar los reintentos existe la APERTURA del registro auxiliar."""
        ruta = os.path.join(self.repo, "estado", "reconciliacion", "REGISTRO.jsonl")
        self.exigir(os.path.isfile(ruta),
                    "no se escribió el registro operativo auxiliar que `g.9` exige")
        lineas = lineas_json(ruta)
        aperturas = [l for l in lineas if l.get("tipo") == "apertura"]
        self.exigir(aperturas, "el registro auxiliar no contiene ninguna apertura")
        apertura = aperturas[0]
        for campo in ("producto", "repositorio", "item", "intento", "causa", "momento"):
            self.exigir(campo in apertura,
                        f"la apertura no identifica «{campo}», y `g.9` lo exige")
        self.exigir(sorted(apertura["momento"]) == ["diario_secuencia", "revision"],
                    "el «momento» no es lógico: `I-g3` prohíbe el reloj de pared")
        self.exigir(apertura["previo"] is None, "la cadena del registro no arranca en nulo")
        self.registro = apertura["registro"]
        self.hecho(f"apertura {self.registro} con producto, repositorio, item, intento, "
                   f"causa y momento lógico")

    # -- 12 -------------------------------------------------------------------------
    def paso_12(self):
        """DEBE: la pendencia se DEDUCE del registro, sin campo que la declare."""
        pendientes = self.json_de(["reconciliacion", "--pendientes"])
        self.exigir(contiene(pendientes, self.registro),
                    f"`reconciliacion --pendientes` no deduce {self.registro}")
        rev = self.revision()
        self.exigir("reconciliacion" not in json.dumps(rev["raiz"]),
                    "la pendencia vive en el estado canónico: `I-g7` los separa")
        self.hecho(f"{self.registro} deducida como pendiente, fuera del estado canónico")

    # -- 13 -------------------------------------------------------------------------
    def paso_13(self):
        """DEBE: sólo una transición explícita retira la pendencia, y mueve la revisión."""
        rev_antes = self.revision()
        proceso = self.cli(["resolver", self.registro, "--autoridad", "SIS",
                            "--motivo", "resuelta por la autoridad", "--json"])
        self.exigir(proceso.returncode == 0,
                    f"`resolver` salió con {proceso.returncode} "
                    f"({self.codigo_de_error(proceso)})")
        pendientes = self.json_de(["reconciliacion", "--pendientes"])
        self.exigir(not contiene(pendientes, self.registro),
                    "la resolución no retiró la pendencia")
        rev = self.revision()
        self.exigir(rev["revision"] > rev_antes["revision"],
                    "resolver no movió la revisión: no fue una transición")
        self.exigir(rev["padre"] == rev_antes["revision_id"],
                    "la revisión de la resolución perdió su linaje")
        self.revision_final = rev
        self.hecho(f"resuelta por transición explícita; revisión {rev['revision']}")

    # -- 14 -------------------------------------------------------------------------
    def paso_14(self):
        """DEBE: la auditoría explica el estado entero, y las dos sedes guardan su parte.

        POR QUÉ AQUÍ NO SE EXIGE `reconciliacion.abierta` EN EL DIARIO, y no es una
        rebaja. En este escenario la apertura NO nació de una llamada explícita: nació en
        el paso 10, del camino de REINTENTOS AGOTADOS. Ese camino es, por definición, aquel
        en el que el escritor nunca consiguió el cerrojo —es lo que significa agotarlos—, y
        sin cerrojo no se puede anexar al diario. Exigir el evento aquí sería exigir que el
        motor escribiese en el diario justamente cuando ha demostrado que no podía, o que
        lo hiciera sin serializarse, que es peor. Lo que `g.9` sí exige, y se comprueba: la
        apertura vive en el REGISTRO AUXILIAR (paso 11), y su retirada exige una transición
        explícita, que sí queda en el diario como `reconciliacion.resuelta`.

        La otra mitad de `g.9` —una apertura pedida explícitamente sí se anota en el
        diario— la cubre la batería, que la abre con el cerrojo disponible.
        """
        auditoria = self.json_de(["auditar"])
        self.exigir(isinstance(auditoria, (dict, list)),
                    "`auditar --json` no devuelve un informe")
        diario = os.path.join(self.repo, "estado", "diario", "DIARIO.jsonl")
        tipos = [evento["tipo"] for evento in lineas_json(diario)]
        for obligatorio in ("almacen.inicializado", "transicion.abierta",
                            "transicion.preparada", "transicion.confirmada",
                            "transicion.revertida", "reconciliacion.resuelta"):
            self.exigir(obligatorio in tipos,
                        f"el diario no conserva evidencia de {obligatorio}")
        registro = os.path.join(self.repo, "estado", "reconciliacion", "REGISTRO.jsonl")
        lineas = lineas_json(registro)
        self.exigir(any(l.get("tipo") == "apertura" for l in lineas),
                    "el registro auxiliar no conserva la apertura: es append-only")
        self.exigir(any(l.get("tipo") == "resolucion" for l in lineas),
                    "el registro auxiliar no conserva la resolución: es append-only")
        for anterior, siguiente in zip(lineas, lineas[1:]):
            self.exigir(siguiente["previo"] == anterior["huella"],
                        "la cadena del registro auxiliar está rota")
        self.hecho(f"diario con {len(tipos)} eventos; registro auxiliar encadenado con "
                   f"apertura y resolución conservadas")

    # -- 15 -------------------------------------------------------------------------
    def paso_15(self):
        """DEBE: integridad completa, y ni un reloj ni un pid en lo durable."""
        proceso = self.cli(["verificar", "--json"])
        self.exigir(proceso.returncode == 0,
                    f"`verificar` salió con {proceso.returncode} "
                    f"({self.codigo_de_error(proceso)})")
        sospechosos = [re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}"),
                       re.compile(r"\b1[6-9]\d{8}\b"),
                       re.compile(r"\bpid\b", re.IGNORECASE)]
        for sub in ("canonico", "diario", "reconciliacion"):
            base = os.path.join(self.repo, "estado", sub)
            for dirpath, _d, ficheros in os.walk(base):
                for nombre in sorted(ficheros):
                    texto = texto_de(os.path.join(dirpath, nombre),
                                     errors="replace")
                    for patron in sospechosos:
                        self.exigir(patron.search(texto) is None,
                                    f"un artefacto durable contiene «{patron.pattern}»: "
                                    f"`I-g3` lo prohíbe")
        rev = self.revision()
        self.exigir(rev["cid_raiz"].startswith("sha256:"), "`cid_raiz` no es un cid")
        self.hecho(f"estado íntegro en la revisión {rev['revision']}, sin reloj ni pid "
                   f"en ningún artefacto durable")

    # -- resumen --------------------------------------------------------------------
    def resumen(self):
        cumplidos = self.estado_de_los_pasos.count("CUMPLIDO")
        self.emitir()
        self.emitir(f"{cumplidos} de 15 pasos CUMPLIDOS")
        if cumplidos != 15:
            self.emitir("pasos no cumplidos:")
            for indice, estado_paso in enumerate(self.estado_de_los_pasos):
                if estado_paso != "CUMPLIDO":
                    self.emitir(f"  {indice + 1:02d}  {estado_paso}  {TITULOS[indice]}")

    def codigo_de_salida(self):
        return 0 if self.estado_de_los_pasos.count("CUMPLIDO") == 15 else 1

    def limpiar(self):
        for base, dirs, _f in os.walk(self.tmp):
            for d in dirs:
                try:
                    os.chmod(os.path.join(base, d), 0o755)
                except OSError:
                    pass
        shutil.rmtree(self.tmp, ignore_errors=True)


# ---------------------------------------------------------------------------
#  `ADJ-M3` · EL ALMACÉN CORTADO ENTRE LOS PASOS 8 Y 9, QUE HAY QUE RECUPERAR
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR. `CONTRATO-ESTADO-DURABLE.md` §3 afirma que los tres
#  escenarios extremo a extremo «ya no pueden seguir verdes sobre un almacén irrecuperable»,
#  y `entre-el-paso-8-y-el-9` es el ÚNICO punto del protocolo que deja el disco en ese
#  estado —objetos publicados con su testigo, revisión todavía sin publicar—. Medido sobre
#  los tres ficheros: `grep -c 'entre-el-paso-8-y-el-9'` daba **0 en los tres**. La
#  comprobación de recuperabilidad recorría almacenes que ningún corte había dejado a
#  medias: podía fallar en teoría y no había visto nunca el estado que dice cazar.
#
#  DECISIÓN · se SIEMBRA un almacén cortado ahí, en un control repo APARTE
#      Alternativas: (a) cortar uno de los almacenes que el escenario ya usa; (b) crear uno
#      propio para el corte; (c) dejarlo y pedir que el contrato retire la afirmación.
#      Se elige (b). Con (a) los pasos numerados dejarían de medir lo que declaran —un corte
#      en medio cambia todo lo que viene después— y la salida dejaría de ser comparable con
#      la evidencia publicada. Con (c) se perdería una propiedad que el motor SÍ tiene y que
#      sólo faltaba ejercer desde aquí. Con (b) los pasos quedan intactos y el barrido de
#      recuperabilidad —que descubre los almacenes por su marca en disco, no por una lista—
#      encuentra uno más y tiene que RECUPERARLO por la rama COMPLETAR.
#
#  DECISIÓN · la siembra COMPRUEBA que cortó, y no se conforma con haberlo intentado
#      Se exige código 70 —el corte real, `os._exit` sin `finally` y sin vaciar búferes—, el
#      TESTIGO del paso 8 en disco y la revisión SIN avanzar. Sin esas tres, sembrar podría
#      dejar un almacén sano y la comprobación volvería a ser vacua, que es justo el defecto
#      que se cierra. Y por eso la siembra puede poner el escenario en ROJO ella sola.
PUNTO_DE_CORTE = "entre-el-paso-8-y-el-9"
ALMACEN_CORTADO = "almacen-cortado-8-9"
TX_CORTADA = "tx-corte-8-9"
CODIGO_DE_CORTE = 70


def sembrar_almacen_cortado(base, cli_estado, entorno):
    """Deja bajo `base` un almacén cortado ENTRE los pasos 8 y 9. Devuelve `(ok, lineas)`."""
    repo = os.path.join(base, ALMACEN_CORTADO)
    os.makedirs(repo, exist_ok=True)
    carga = os.path.join(base, "carga-corte-8-9.json")
    with open(carga, "w", encoding="utf-8") as manejador:
        json.dump({"esquema": "ads.estado/1", "n": 89}, manejador, sort_keys=True)
    orden = [sys.executable, cli_estado, "--repo", repo]
    limpio = {clave: valor for clave, valor in entorno.items()
              if clave != "ADS_ESTADO_FALLO"}
    arranque = subprocess.run(orden + ["inicializar"], capture_output=True, text=True,
                              env=limpio)
    if arranque.returncode != 0:
        return False, ["T362 · corte 8-9: `inicializar` salió con "
                       + str(arranque.returncode) + ", así que no hay almacén que cortar"]
    cortado = dict(limpio)
    cortado["ADS_ESTADO_FALLO"] = PUNTO_DE_CORTE
    caida = subprocess.run(
        orden + ["transicion", "--id", TX_CORTADA, "--autor", "escenario-e2e",
                 "--motivo", "corte deliberado entre los pasos 8 y 9",
                 "--escribir", "items/it-corte.json=" + carga],
        capture_output=True, text=True, env=cortado)
    lineas, ok = [], True
    if caida.returncode != CODIGO_DE_CORTE:
        ok = False
        lineas.append("T362 · corte 8-9: el corte NO cortó (código "
                      + str(caida.returncode) + "). Sin corte no queda nada a medias y la "
                      "comprobación de recuperabilidad no mediría nada")
    testigo = os.path.join(repo, "estado", "operacional", "tx", TX_CORTADA,
                           "PUBLICADOS.json")
    if not os.path.isfile(testigo):
        ok = False
        lineas.append("T362 · corte 8-9: el paso 8 no dejó su testigo durable, luego el "
                      "corte no cayó entre los pasos 8 y 9")
    try:
        with open(os.path.join(repo, "estado", "REVISION.json"), encoding="utf-8") as m:
            revision = json.load(m)["revision"]
    except (OSError, ValueError, KeyError, TypeError):
        revision = None
    if revision != 0:
        ok = False
        lineas.append("T362 · corte 8-9: la revisión vigente es " + str(revision)
                      + " y tenía que seguir siendo 0. El paso 9 llegó a publicar, y "
                      "entonces el almacén no queda a medias")
    if ok:
        lineas.append("T362 · corte 8-9: almacén cortado en `" + PUNTO_DE_CORTE
                      + "` — testigo del paso 8 en disco y revisión SIN publicar. La "
                      "comprobación de recuperabilidad tiene que encontrarlo y COMPLETARLO")
    # El VEREDICTO, en la forma que `registro_pruebas.veredictos_publicados` sabe leer. Sin
    # él la evidencia registra la ejecución y NO sostiene el `estado:` que el escenario
    # declara, y «no he podido contrastarlo» acabaría leyéndose como «está bien».
    lineas = [linea + " ... " + ("ok" if ok else "FAIL") for linea in lineas]
    return ok, lineas


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
    escenario = Escenario()
    recuperable = True
    try:
        escenario.ejecutar()
        # `ADJ-M3` · antes de comprobar la recuperabilidad se SIEMBRA el único estado que la
        # hace significar algo: un almacén cortado entre los pasos 8 y 9.
        sembrado, lineas_del_corte = sembrar_almacen_cortado(
            escenario.tmp, CLI, ENTORNO)
        escenario.lineas.append("")
        escenario.lineas.extend(lineas_del_corte)
        # `E-08` · el escenario no termina en verde sobre un almacén que no se puede volver
        # a abrir. Se comprueba ANTES de borrar el temporal.
        recuperable, lineas_de_recuperabilidad = comprobar_recuperabilidad(escenario.tmp)
        recuperable = recuperable and sembrado
        escenario.lineas.append("")
        escenario.lineas.extend(lineas_de_recuperabilidad)
    finally:
        escenario.limpiar()
    # Se imprime AL FINAL y de una vez: así el informe no se entrelaza con nada que
    # escriban los subprocesos, y los bytes son los mismos en cada ejecución.
    print("\n".join(escenario.lineas))
    return escenario.codigo_de_salida() or (0 if recuperable else 1)


if __name__ == "__main__":
    sys.exit(main())
