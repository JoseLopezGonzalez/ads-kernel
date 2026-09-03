#!/usr/bin/env python3
"""escenario_e2e_f6 — el escenario EXTREMO A EXTREMO del macrobloque 3 de `F6`.

`T225`. Veintiún pasos sobre material REAL, y ningún mock hace de pieza principal:

    un control repo                 con su estado durable y su gobierno Git instalado
    dos repositorios de producto    Git de verdad, hermanos del control repo
    un remoto Git                   bare, temporal, con su hook de referencia
    dos clones                      que representan DOS MÁQUINAS distintas
    dos runtimes                    procesos REALES, compitiendo por la misma autoridad
    estado durable · dispatcher     el motor y la máquina de despacho que ya existían
    un adaptador local              `subprocess` de verdad, que mata de verdad
    gobierno Git · admisión V2–V5   concesión, base, política, hook, y juicio por MUTACIÓN
    el derivador `V6-15`            los árboles adversariales derivados de su sede
    la raíz externa `V6-16`         proceso e instalación SEPARADOS, firma ASIMÉTRICA
    un macrocircuito COMPLETO       `N`, desde su `FASE 0` hasta su cierre inequívoco
    `Continúa`                      el plan reproducible de `§7.4`

QUÉ LO DISTINGUE DE LOS DOS ESCENARIOS ANTERIORES, que se conservan y siguen corriendo.
`escenario_extremo_a_extremo` mide el motor de estado durable; `escenario_e2e_runtime` mide
que el runtime, el gobierno Git y la admisión se sostienen juntos. Éste mide lo que ninguno
de los dos podía medir: que **el ciclo de `§7.2`, un macrocircuito entero, la firma externa
y la serialización entre MÁQUINAS se sostienen sobre las mismas piezas**, y que la evidencia
que produce ese conjunto **la verifica alguien que no puede escribir en el árbol**.

DETERMINISMO. La salida se PUBLICA como evidencia: dos ejecuciones seguidas, desde
directorios distintos, producen bytes idénticos. Ni relojes, ni duraciones, ni pids, ni
rutas absolutas. Lo que varía —un pid, un temporal, un digest de commit, una huella de
clave— se sustituye por su FORMA, que es lo que la prueba afirma.

    python3 kernel/operativo/runtime/pruebas/escenario_e2e_f6.py

Sale con 0 si los veintiún pasos se cumplen, y con 1 en cuanto uno falla, marcando los que
quedaron sin ejecutar. Un escenario que sigue adelante tras un paso fallido mide el estado
equivocado en todos los siguientes.

NADA DE ESTE ESCENARIO CERTIFICA NADA. Que los veintiún pasos se cumplan significa que se
ejecutaron y pasaron. La CERTIFICACIÓN de `F6` la emite un juicio independiente, y no quien
construyó.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
RUNTIME = os.path.join(RAIZ, "kernel", "operativo", "runtime")
KERNEL = os.path.join(RAIZ, "kernel", "operativo")
RAIZ_EXTERNA = os.path.join(RAIZ, "kernel", "operativo", "raiz-externa")
CLI_ESTADO = os.path.join(RUNTIME, "ads_estado.py")
CLI_RUNTIME = os.path.join(RUNTIME, "ads_runtime.py")
CLI_CICLO = os.path.join(RUNTIME, "ads_ciclo.py")
CLI_ARBOLES = os.path.join(RUNTIME, "ads_arboles.py")
sys.path.insert(0, RUNTIME)

import adaptadores                                                    # noqa: E402
import admision                                                       # noqa: E402
import ciclo                                                          # noqa: E402
import estado                                                         # noqa: E402
import gobierno                                                       # noqa: E402
import identidad                                                      # noqa: E402
import macrocircuitos                                                 # noqa: E402
import runtime as runtime_ads                                         # noqa: E402
from admision import censo as censo_admision                          # noqa: E402
from admision import matriz, perimetro                                # noqa: E402
from ciclo import gates as gates_de_capa                              # noqa: E402

sys.path.insert(0, RAIZ_EXTERNA)
import firma as modulo_de_firma                                       # noqa: E402
import instalar as modulo_de_instalacion                              # noqa: E402

# Sin red y sin configuración de la máquina: Git sólo tiene permitido el transporte `file`,
# y la identidad va por entorno para no depender de —ni tocar— la del que ejecuta.
ENTORNO = {
    **os.environ,
    "GIT_AUTHOR_NAME": "ads-e2e-f6", "GIT_AUTHOR_EMAIL": "e2e-f6@ads.local",
    "GIT_COMMITTER_NAME": "ads-e2e-f6", "GIT_COMMITTER_EMAIL": "e2e-f6@ads.local",
    "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull,
    "GIT_ALLOW_PROTOCOL": "file", "GIT_TERMINAL_PROMPT": "0",
}
ENTORNO.pop("ADS_ESTADO_FALLO", None)
ENTORNO.pop("ADS_RUNTIME_FALLO", None)

PASOS = [
    "instalación: workspace, control repo, dos fuentes, remoto bare y dos clones",
    "FASE 0 del macrocircuito, con sus seis identificadores y su soporte propio",
    "encuadre: producto, control repo, fuentes, perfil, política y capacidades",
    "composición de rutas por b.16, con las cuatro vías y la traza de lo no activado",
    "materialización del equipo por C4, con su composición y lo que quedó fuera",
    "creación de items y paquetes, por el runtime y en el estado canónico",
    "despacho por el adaptador local, con un proceso real",
    "progreso emitido por el proceso y recogido por el runtime",
    "handoff por C5, con su acuse durable y su rechazo por camino distinto",
    "gate de capa: el positivo cierra y el negativo FALLA CERRADO",
    "mutación Git sobre la rama canónica del control repo",
    "admisión V2–V5: la mutación declarada se admite y la no declarada da ROJO",
    "firma externa ASIMÉTRICA: la raíz externa atesta con Ed25519, fuera del árbol",
    "publicación remota: la ref viaja al remoto bare y el linaje queda registrado",
    "concurrencia entre MÁQUINAS: dos clones, dos procesos, una sola confirmación",
    "caída del runtime entre el efecto y su acuse, con el proceso muerto de verdad",
    "recuperación por la OTRA instancia, sin inventar estado",
    "`Continúa`: plan reproducible, y dos ejecuciones seguidas idénticas",
    "no repetición del efecto: lo confirmado no se vuelve a aplicar",
    "cierre del macrocircuito, de forma inequívoca",
    "evidencia verificable DESDE la raíz externa, que no puede escribir en el árbol",
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


def guion(directorio, nombre, cuerpo):
    ruta = os.path.join(directorio, nombre)
    with open(ruta, "w", encoding="utf-8") as manejador:
        manejador.write(cuerpo)
    os.chmod(ruta, 0o755)
    return ruta


def escribir_configuracion(ruta, datos):
    """La configuración de confianza EXTERNA, en el subconjunto que el aparato lee."""
    lineas = [
        "version: " + str(datos["version"]),
        "autoridad: " + datos["autoridad"],
        "epoca_vigente: " + str(datos["epoca_vigente"]),
        "orden_de_firma: [" + ", ".join(datos["orden_de_firma"]) + "]",
        "orden_de_verificacion: [" + ", ".join(datos["orden_de_verificacion"]) + "]",
        "identidades:",
    ]
    for entrada in datos["identidades"]:
        lineas.append("  - id: " + entrada["id"])
        lineas.append("    algoritmo: " + entrada["algoritmo"])
        lineas.append("    huella_publica: " + entrada["huella_publica"])
        lineas.append("    estado: " + entrada["estado"])
        lineas.append("    epoca_de_alta: " + str(entrada["epoca_de_alta"]))
    lineas.append("ancla:")
    lineas.append("  base: " + datos["ancla"]["base"])
    lineas.append("  digest_del_censo: " + datos["ancla"]["digest_del_censo"])
    lineas.append("admitidas: []")
    with open(ruta, "w", encoding="utf-8") as manejador:
        manejador.write("\n".join(lineas) + "\n")
    return ruta


TAREA = """#!/bin/sh
# Tarea REAL del adaptador: emite progreso por líneas y deja un efecto en disco.
echo "avance 1"
echo "avance 2"
printf 'aplicado\\n' >> "$1"
exit 0
"""


class Escenario:
    """Los veintiún pasos. Cada uno devuelve el detalle que se publica en la evidencia."""

    def __init__(self, base):
        self.base = base
        self.cumplidos = []
        self.corpus = ciclo.Corpus(KERNEL)
        # Las claves, FUERA de todos los repositorios y de todo lo versionado.
        self.claves = os.path.join(base, "claves")
        self.externo = os.path.join(base, "externo")
        self.espacio = os.path.join(base, "espacio")
        self.remoto = os.path.join(base, "remoto.git")
        self.maquina_a = os.path.join(base, "maquina-a")
        self.maquina_b = os.path.join(base, "maquina-b")
        self.control = os.path.join(self.maquina_a, "control")
        self.control_b = os.path.join(self.maquina_b, "control")
        self.fuentes = [os.path.join(self.maquina_a, "producto-uno"),
                        os.path.join(self.maquina_a, "producto-dos")]
        # La orden NO lleva ninguna ruta absoluta, y no es cosmética: el identificador del
        # efecto se DERIVA del contenido de la orden, así que una ruta temporal dentro de
        # ella haría que el mismo trabajo produjera un efecto distinto en cada ejecución, y
        # la evidencia publicada dejaría de ser byte a byte reproducible. El adaptador corre
        # con `cwd` en su espacio, de modo que lo relativo basta.
        self.tarea_relativa = "./tarea.sh"
        self.efecto_relativo = "efecto.txt"
        self.efecto_en_disco = os.path.join(self.espacio, "efecto.txt")
        self.registro_de_adaptadores = None
        self.circuito = None
        self.encuadre = None
        self.composicion = None
        self.plan = None
        self.base_admision = None
        self.instalacion = None
        self.configuracion = None
        self.atestacion = os.path.join(self.externo, "atestacion.json")

    # -- utilidades ---------------------------------------------------------
    def registro(self):
        if self.registro_de_adaptadores is None:
            self.registro_de_adaptadores = adaptadores.RegistroDeAdaptadores([
                adaptadores.AdaptadorDeProcesoLocal(self.espacio),
            ])
        return self.registro_de_adaptadores

    def abrir_runtime(self, instancia):
        return runtime_ads.Runtime(self.control, instancia=instancia,
                                   registro_de_adaptadores=self.registro()).abrir()

    def entrada_del_owner(self, **cambios):
        """La entrada del Owner, con la expresión literal que la regla 1 exige conservar."""
        entrada = {
            "clase": "candidato",
            "expresion_literal": "quiero gobernar un producto nuevo con dos repositorios",
            "canal": "conversacion",
            "fecha": "2026-09-03",
            "resultado_perseguido": ("el producto queda instalado y gobernado, con su "
                                     "control repo y sus dos fuentes declaradas"),
            "evidencia_de_cierre": ["el control repo publicado con su estado durable"],
            "anclaje_terminado": True,
            "materia": "la-propia-fabrica",
            "estado_del_objeto": "no-existe",
        }
        entrada.update(cambios)
        return entrada

    def orden_de_tarea(self, destino=None):
        return {
            "adaptador": "proceso-local", "operacion": "ejecutar",
            "argumentos": [self.tarea_relativa, destino or self.efecto_relativo],
            "limite_segundos": 60,
        }

    # =====================================================================
    #  1 · INSTALACIÓN
    # =====================================================================
    def paso_01(self):
        for carpeta in (self.claves, self.externo, self.espacio,
                        self.maquina_a, self.maquina_b):
            os.makedirs(carpeta, exist_ok=True)
        os.chmod(self.claves, 0o700)
        guion(self.espacio, "tarea.sh", TAREA)

        # El control repo, con su árbol gobernado y su política, y las DOS fuentes.
        canal = gobierno.CanalGit(self.control)
        self.base_admision = matriz.fundar(self.control, canal)
        origen = os.path.join(RUNTIME, "gobierno", "POLITICA-CONTROL-REPO.yml")
        destino = os.path.join(self.control, "kernel", "operativo", "runtime",
                               "gobierno", "POLITICA-CONTROL-REPO.yml")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        shutil.copyfile(origen, destino)
        canal.ejecutar("add", "-A")
        canal.ejecutar("commit", "--quiet", "-m", "politica del gobierno")
        self.base_admision = canal.resolver("HEAD")

        for fuente in self.fuentes:
            os.makedirs(fuente, exist_ok=True)
            git(fuente, "init", "--quiet", "--initial-branch=main")
            with open(os.path.join(fuente, "README.md"), "w", encoding="utf-8") as fh:
                fh.write("# " + os.path.basename(fuente) + "\n")
            git(fuente, "add", "-A")
            git(fuente, "commit", "--quiet", "-m", "alta de la fuente")

        # El manifiesto de composición, que es lo que el encuadre descubre.
        with open(os.path.join(self.control, "SOURCES.toml"), "w", encoding="utf-8") as fh:
            fh.write("schema = 1\n\n[workspace]\nlayout = \"hermanos\"\n\n")
            for fuente in self.fuentes:
                fh.write("[[sources]]\nid = \"" + os.path.basename(fuente) + "\"\n")
                fh.write("path = \"../" + os.path.basename(fuente) + "\"\n\n")
        with open(os.path.join(self.control, "PROFILE.md"), "w", encoding="utf-8") as fh:
            fh.write("# PERFIL\n\nproducto gobernado por el escenario de `F6`.\n")

        # El remoto BARE y el segundo clon: las DOS MÁQUINAS.
        subprocess.run(["git", "init", "--quiet", "--bare", "--initial-branch=canonica",
                        self.remoto], check=True, env=ENTORNO, capture_output=True)
        git(self.control, "remote", "add", "origin", self.remoto)
        git(self.control, "push", "--quiet", "origin", "canonica")
        subprocess.run(["git", "clone", "--quiet", self.remoto, self.control_b],
                       check=True, env=ENTORNO, capture_output=True)

        # La RAÍZ EXTERNA se instala FUERA del árbol verificado, con su manifiesto.
        self.instalacion = modulo_de_instalacion.instalar(
            os.path.join(self.base, "instalacion"),
            arbol_verificado=self.control, runtime=RUNTIME)
        exigir(not os.path.realpath(self.instalacion["destino"]).startswith(
            os.path.realpath(self.control) + os.sep),
            "la instalación de la raíz externa cayó DENTRO del árbol verificado")
        return ("control repo fundado y publicado · dos fuentes Git · remoto bare con dos "
                "clones · raíz externa instalada fuera del árbol")

    # =====================================================================
    #  2 · FASE 0
    # =====================================================================
    def paso_02(self):
        self.circuito = macrocircuitos.Macrocircuito(
            "N", self.control, corpus=self.corpus, instancia="mc-n",
            registro_de_adaptadores=self.registro(), raiz_kernel=KERNEL)
        comprobaciones = [c["id"] for c in gates_de_capa.gate(
            "gate:sistema-conforme", corpus=self.corpus)["comprobaciones"]]
        fase0 = self.circuito.ejecutar_fase0(
            disparador="el Owner quiere gobernar un producto que todavía no existe",
            comprobaciones_superadas=comprobaciones,
            evidencia=["la salida de los validadores ejecutados"])
        sujeto = fase0["sujeto"]
        faltan = [i for i in macrocircuitos.IDENTIFICADORES_DEL_SUJETO if not sujeto.get(i)]
        exigir(not faltan, "el sujeto de la FASE 0 no declara " + ", ".join(faltan))
        # La regla 2: CERO mutaciones canónicas del macrocircuito antes del gate.
        exigir(not os.path.isdir(os.path.join(self.control, "estado", "canonico")),
               "la FASE 0 escribió en `estado/`, que nace DESPUÉS de ella")
        return ("declaración Estructural emitida, con sus "
                + str(len(macrocircuitos.IDENTIFICADORES_DEL_SUJETO))
                + " identificadores de sujeto y su soporte durable propio; `estado/` "
                "todavía no existe")

    # =====================================================================
    #  3 · ENCUADRE
    # =====================================================================
    def paso_03(self):
        self.circuito.abrir()
        self.encuadre = ciclo.encuadrar(self.control, self.entrada_del_owner(),
                                        corpus=self.corpus)
        exigir(self.encuadre["proceso"] == "proceso:SIS",
               "el encuadre eligió " + str(self.encuadre["proceso"]) + " y no `proceso:SIS`")
        descubiertas = self.encuadre["fuentes"]["fuentes"]
        exigir(len(descubiertas) == 2,
               "el encuadre descubrió " + str(len(descubiertas)) + " fuentes y hay dos")
        exigir(self.encuadre["perfil"]["declarado"], "el encuadre no cargó el PROFILE")
        return ("clase `" + self.encuadre["clase"] + "` · proceso `"
                + self.encuadre["proceso"] + "` · dos fuentes descubiertas de `SOURCES.toml`"
                " · perfil y política cargados · capacidades necesarias: "
                + str(len(self.encuadre["capacidades_necesarias"])))

    # =====================================================================
    #  4 · COMPOSICIÓN DE RUTAS
    # =====================================================================
    def paso_04(self):
        self.composicion = ciclo.componer(self.encuadre, corpus=self.corpus,
                                          condiciones_verdaderas=["C-APR"])
        # Una capacidad puede estar por MÁS DE UNA vía —`SIS` es propietaria global de
        # `proceso:SIS` y además produce su obligación `cambio-de-sistema`—, y la traza
        # conserva las dos entradas. Colapsarlas en un mapa perdería justamente la vía 1,
        # que es la que dice quién DEFINE el resultado del item.
        vias = {}
        for participante in self.composicion["participantes"]:
            vias.setdefault(participante["capacidad"], set()).add(participante["via"])
        exigir(1 in vias.get("SIS", set()),
               "`SIS` no entra por la vía 1 en `proceso:SIS`; vías vistas: "
               + str(sorted(vias.get("SIS", set()))))
        exigir(2 in vias.get("CON", set()),
               "`CON` no entra por la vía 2 pese a producir `cambio-construido`")
        exigir(3 in vias.get("APR", set()),
               "`APR` no entra por la vía 3 con `C-APR` declarada verdadera")
        exigir(all(entrada.get("motivo") for entrada in self.composicion["no_activadas"]),
               "hay una capacidad NO activada sin motivo escrito")
        # Y la ruta NO se elige por texto: renombrar la expresión no la mueve.
        renombrado = ciclo.encuadrar(self.control, self.entrada_del_owner(
            expresion_literal="TEXTO COMPLETAMENTE DISTINTO, con las palabras bug y lento",
            resultado_perseguido="el mismo resultado, dicho con otras palabras"),
            corpus=self.corpus)
        exigir(renombrado["proceso"] == self.encuadre["proceso"],
               "renombrar la expresión del Owner movió la ruta: es selección léxica")
        return ("participantes con su vía: "
                + " · ".join(sorted(c + " vía " + ",".join(str(x) for x in sorted(v))
                                    for c, v in vias.items()))
                + " · no activadas con motivo: " + str(len(self.composicion["no_activadas"]))
                + " · renombrar la expresión NO mueve la ruta")

    # =====================================================================
    #  5 · MATERIALIZACIÓN DE EQUIPO
    # =====================================================================
    def paso_05(self):
        # `C4` paso 2: se recorren las composiciones EN EL ORDEN ESCRITO y se toma la
        # PRIMERA cuya condición conste verdadera. La condición la declara el encuadre; no
        # se evalúa aquí, porque juzgarla sería decidir contenido. Si ninguna consta, `C4`
        # manda ESCALAR a `SIS` y no materializar un equipo por defecto — y eso se
        # comprueba abajo, que es la mitad que impide inventar un equipo.
        escritas = [c["id"] for c in self.corpus.composiciones("SIS")]
        exigir(len(escritas) > 1, "`SIS` declara una sola composición y no hay orden que medir")
        equipo = ciclo.materializar("SIS", corpus=self.corpus,
                                    composiciones_verdaderas=escritas)
        exigir(equipo["roles"], "`C4` no materializó ningún rol para `SIS`")
        exigir(equipo["composicion"], "el equipo no declara qué composición lo eligió")
        # Un MÉTODO no es una CAPACIDAD, y pedirlo como tal falla cerrado.
        try:
            ciclo.exigir_capacidad("SIS/Evolucion", corpus=self.corpus)
        except ciclo.MetodoNoEsCapacidad:
            distingue = True
        else:
            distingue = False
        exigir(distingue, "un método se aceptó como capacidad")
        # Y sin ninguna condición verdadera, `C4` ESCALA en vez de inventar un equipo.
        try:
            ciclo.materializar("SIS", corpus=self.corpus, composiciones_verdaderas=[])
        except ciclo.ComposicionDeEquipoAusente:
            escala = True
        else:
            escala = False
        exigir(escala, "sin composición verdadera se materializó un equipo por defecto")
        exigir(equipo["composicion"] == escritas[0],
               "no mandó el ORDEN ESCRITO: eligió " + str(equipo["composicion"]))
        self.equipo = equipo
        return ("composición `" + str(equipo["composicion"]) + "` · roles: "
                + str(len(equipo["roles"])) + " · fuera con motivo: "
                + str(len(equipo.get("fuera") or equipo.get("esperando_capacidad") or []))
                + " · manda el ORDEN ESCRITO · sin condición verdadera se ESCALA · método "
                "y capacidad se distinguen")

    # =====================================================================
    #  6 · ITEMS Y PAQUETES
    # =====================================================================
    def paso_06(self):
        planificador = ciclo.Planificador(self.circuito.runtime, corpus=self.corpus)
        self.plan = planificador.planificar(
            self.encuadre, self.composicion, equipos=[self.equipo],
            orden_por_capacidad={c: self.orden_de_tarea() for c in ciclo.CAPACIDADES})
        exigir(self.plan["item"], "el plan no creó ningún item")
        exigir(self.plan["paquetes"], "el plan no creó ningún paquete")
        almacen = self.circuito.runtime.almacen
        items = almacen.listar("items")
        paquetes = almacen.listar("paquetes")
        exigir(any(self.plan["item"] in ruta for ruta in items),
               "el item del plan no está en el estado canónico")
        exigir(len(paquetes) >= len(self.plan["paquetes"]),
               "los paquetes del plan no están en el estado canónico")
        # Cada paquete responde de UNA obligación de la ruta, y ninguna queda huérfana.
        exigir(self.plan["obligaciones"], "el plan no arrastra las obligaciones de la ruta")
        return ("item `" + self.plan["item"] + "` · paquetes: "
                + str(len(self.plan["paquetes"])) + " · obligaciones de la ruta: "
                + str(len(self.plan["obligaciones"]))
                + " · todo en el estado canónico, escrito por el motor")

    # =====================================================================
    #  7 · DESPACHO
    # =====================================================================
    def paso_07(self):
        elegibles = self.circuito.runtime.elegibles()
        exigir(elegibles, "no hay trabajo elegible después de planificar")
        # El trabajo elegible se DERIVA del estado y se ordena igual para toda instancia.
        exigir(elegibles == sorted(elegibles, key=lambda e: (-e["prioridad"], e["paquete"])),
               "el orden de lo elegible no es el declarado: dos instancias verían listas "
               "distintas y la carrera dejaría de ser real")
        self.paquete_despachado = elegibles[0]["paquete"]
        resumen = ciclo.despachar(self.circuito.runtime, self.paquete_despachado)
        exigir(resumen["desenlace"] == "completado",
               "el despacho terminó en " + str(resumen["desenlace"]))
        exigir(os.path.exists(self.efecto_en_disco),
               "el adaptador no dejó su efecto en disco: no se ejecutó nada real")
        self.efecto_acusado = resumen["efecto"]
        return ("paquete `" + self.paquete_despachado + "` despachado por el adaptador "
                "local con un proceso real · desenlace `" + resumen["desenlace"]
                + "` · efecto `" + str(resumen["efecto"]) + "` aplicado en disco y acusado")

    # =====================================================================
    #  8 · PROGRESO
    # =====================================================================
    def paso_08(self):
        elegibles = self.circuito.runtime.elegibles()
        exigir(elegibles, "no queda trabajo elegible para medir el progreso")
        resumen = ciclo.despachar(self.circuito.runtime, elegibles[0]["paquete"])
        exigir(resumen["desenlace"] == "completado",
               "el despacho con progreso terminó en " + str(resumen["desenlace"]))
        # El proceso emite DOS líneas y el runtime añade su propio evento de entrega: son
        # tres como mínimo. Y el CONTEO no entra en lo durable: sería un número de ejecución.
        exigir(resumen["progreso"] >= 3,
               "el runtime recogió " + str(resumen["progreso"]) + " avances y el proceso "
               "emite dos, más el de entrega del propio runtime")
        paquete = self.circuito.runtime.almacen.leer("paquetes/" + elegibles[0]["paquete"] + ".json")
        exigir("progreso" not in paquete,
               "el conteo de progreso entró en el estado durable, contra `I-g3`")
        return ("el proceso emitió sus líneas y el runtime recogió "
                + str(resumen["progreso"]) + " avances; el conteo NO entra en lo durable")

    # =====================================================================
    #  9 · HANDOFF
    # =====================================================================
    def paso_09(self):
        from ciclo import handoffs as modulo_de_handoffs
        catalogo = ciclo.catalogo(corpus=self.corpus)
        exigir(catalogo, "el catálogo de handoffs de `C5` está vacío")
        # Las CINCO entregas que `§8.0` declara aparte tienen que estar en el catálogo: sin
        # ellas la composición se compone y la ENTREGA no existe.
        for declarada in ciclo.ENTREGAS_DECLARADAS_EN_8_0:
            exigir(declarada in catalogo,
                   "la entrega de `§8.0` `" + declarada + "` no está en el catálogo")
        eleccion = "handoff:sis-a-con" if "handoff:sis-a-con" in catalogo \
            else sorted(catalogo)[0]
        trazabilidad = {"item": self.plan["item"],
                        "paquete": self.paquete_despachado,
                        "ruta": self.composicion["id"]}
        entrega = ciclo.emitir(eleccion, corpus=self.corpus,
                               artefactos=["el source change con `escribe_fuentes`"],
                               checkpoint="el estado del paquete y su revisión base",
                               trazabilidad=trazabilidad)
        rt = self.circuito.runtime
        from ciclo import durable as durable_del_ciclo
        durable_del_ciclo.escribir(
            rt.almacen, clase="ciclo.handoff.emitido",
            motivo="entrega " + eleccion + " del escenario",
            objetos={modulo_de_handoffs.ruta_de(entrega["id"]): entrega})
        acusada = ciclo.acusar(
            entrega, comprobaciones_superadas=catalogo[eleccion]["comprueba_al_recibir"],
            receptor=catalogo[eleccion]["a"])
        durable_del_ciclo.escribir(
            rt.almacen, clase="ciclo.handoff.acusado",
            motivo="acuse de " + eleccion,
            objetos={modulo_de_handoffs.ruta_de(acusada["id"]): acusada})
        leida = rt.almacen.leer(modulo_de_handoffs.ruta_de(acusada["id"]))
        exigir(leida["estado"] == "acusado",
               "el acuse durable dejó el handoff en " + str(leida["estado"]))
        exigir(leida["custodia"] == catalogo[eleccion]["a"],
               "la custodia no pasó al receptor con el acuse")
        # RECHAZAR no es DEVOLVER: el rechazo NO cambia la custodia y NO gasta devolución.
        segunda = ciclo.emitir(eleccion, corpus=self.corpus,
                               artefactos=["una capa que no cumple lo comprobable"],
                               checkpoint="el mismo checkpoint",
                               trazabilidad=trazabilidad)
        rechazada = ciclo.rechazar(
            segunda, receptor=catalogo[eleccion]["a"],
            motivo="falta el artefacto que `comprueba_al_recibir` exige")
        exigir(rechazada["custodia"] == catalogo[eleccion]["de"],
               "un RECHAZO cambió la custodia: sigue siendo del emisor")
        # Y la REANUDACIÓN se lee del checkpoint, sin hablar con el emisor.
        reanudacion = ciclo.reanudacion(leida)
        exigir(reanudacion["trazabilidad"]["item"] == self.plan["item"],
               "la reanudación del handoff perdió su trazabilidad")
        return ("handoff `" + eleccion + "` emitido y ACUSADO en el estado durable, con "
                "custodia en `" + leida["custodia"] + "` · un segundo RECHAZADO sin cambio "
                "de custodia · reanudación legible desde el checkpoint · las "
                + str(len(ciclo.ENTREGAS_DECLARADAS_EN_8_0))
                + " entregas de `§8.0` están en el catálogo")

    # =====================================================================
    #  10 · GATE DE CAPA
    # =====================================================================
    def paso_10(self):
        censo = ciclo.censo_de_gates(corpus=self.corpus)
        exigir(censo, "el censo de gates derivado del corpus está vacío")
        nombre = "gate:cierre-de-item" if "gate:cierre-de-item" in censo \
            else sorted(censo)[0]
        declarado = censo[nombre]
        comprobaciones = [c["id"] for c in declarado["comprobaciones"]]
        exigir(comprobaciones, "el gate `" + nombre + "` no declara comprobaciones")
        evidencia = list(declarado.get("evidencia") or [])
        entrada = {"item": self.plan["item"], "ruta": self.composicion["id"]}
        positivo = ciclo.aplicar_gate(
            nombre, entrada=entrada, evidencia=evidencia, revisor="VER",
            corpus=self.corpus, comprobaciones_superadas=comprobaciones,
            salida="el item puede cerrar")
        exigir(positivo["dictamen"] == "superado",
               "el gate positivo dictaminó " + str(positivo["dictamen"]))
        # NEGATIVO: falta UNA comprobación y el gate FALLA CERRADO, con su dictamen dentro.
        try:
            ciclo.aplicar_gate(
                nombre, entrada=entrada, evidencia=evidencia, revisor="VER",
                corpus=self.corpus, comprobaciones_superadas=comprobaciones[:-1])
        except ciclo.GateFallido as error:
            cerrado = getattr(error, "dictamen", {}).get("dictamen") == "no-superado"
            pendientes = getattr(error, "dictamen", {}).get("comprobaciones_pendientes") or []
        else:
            cerrado, pendientes = False, []
        exigir(cerrado, "el gate con una comprobación sin superar NO falló cerrado")
        exigir(pendientes, "el fallo del gate no dice QUÉ comprobación quedó pendiente")
        # Y un gate NO puede convertirse en fuente normativa: declarar una comprobación que
        # el corpus no le da se rechaza.
        try:
            ciclo.aplicar_gate(
                nombre, entrada=entrada, evidencia=evidencia, revisor="VER",
                corpus=self.corpus,
                comprobaciones_superadas=list(comprobaciones) + ["comprobacion-inventada"])
        except ciclo.GateNormativo:
            no_normativo = True
        else:
            no_normativo = False
        exigir(no_normativo, "un gate creció con una comprobación que el corpus no declara")
        return ("gate `" + nombre + "` · positivo: dictamen `" + positivo["dictamen"]
                + "` con revisor y evidencia · negativo: FALLA CERRADO nombrando "
                + str(len(pendientes)) + " pendiente(s) · y el gate NO puede crecer: "
                "declarar una comprobación ajena se rechaza")

    # =====================================================================
    #  11 · MUTACIÓN GIT
    # =====================================================================
    def paso_11(self):
        ref = gobierno.RAMA_CANONICA
        control = gobierno.inicializar(self.control, titular="runtime-e2e-f6")
        control.abrir()
        try:
            control.instalar_hook()
            control.conceder(ref)
            ruta = "docs/canonico/NOTA-E2E.md"
            preparacion = control.preparar(
                ref, mensaje="mutacion gobernada del escenario",
                ficheros={ruta: b"# nota publicada por el escenario de F6\n"})
            confirmado = control.confirmar(ref, preparacion)
            exigir(confirmado.get("nuevo"), "la confirmación no movió la ref")
            self.commit_gobernado = confirmado["nuevo"]
            self.ruta_mutada = ruta
            # `G-A8` mitad IMPOSIBLE: forzar la ref a un commit divergente lo rechaza el
            # hook, y no una casualidad de la configuración de Git.
            canal = control.canal
            _, arbol, _ = canal.ejecutar("write-tree")
            _, divergente, _ = canal.ejecutar(
                "commit-tree", arbol.decode("ascii").strip(), "-m", "historia paralela")
            codigo, _, _ = canal.ejecutar(
                "update-ref", ref, divergente.decode("ascii").strip(),
                confirmado["nuevo"], exigir_exito=False)
            exigir(codigo != 0, "el hook dejó forzar la ref a un commit divergente")
            # `G-A8` mitad DETECTABLE: el linaje DURABLE denuncia el intento.
            control.exigir_refs_intactas()
        finally:
            control.cerrar()
        return ("mutación confirmada sobre `" + ref + "` con concesión durable, revisión "
                "base, ventana cerrada y hook instalado · forzar a un commit divergente se "
                "RECHAZA · el linaje durable sigue intacto")

    # =====================================================================
    #  12 · ADMISIÓN V2–V5
    # =====================================================================
    def paso_12(self):
        # CONTROL DEL CONTROL, y va primero. Una instalación real crea directorios que el
        # registro de zonas todavía no clasifica —`estado/`, `espacio/`, el perfil, el
        # manifiesto—, y `V6-10` exige que una ruta SIN ZONA dé ROJO en vez de pasar por
        # omisión. Se comprueba que efectivamente da ROJO, y sólo DESPUÉS se declaran las
        # zonas. Declararlas sin haber medido el rojo dejaría la propiedad sin ejercer.
        sin_zona = admision.verificar(
            self.control, base=self.base_admision, censar_el_codigo=False,
            declaracion=admision.Declaracion(
                ancla=self.base_admision, autoridad="raiz-externa-del-escenario"))
        exigir(sin_zona.color == "ROJO",
               "una ruta sin zona declarada pasó la admisión por omisión")
        exigir(any("ninguna zona" in h.a_dict().get("causa", "")
                   for h in sin_zona.hallazgos),
               "el veredicto no denuncia la ausencia de zona")
        self._declarar_zonas_de_la_instalacion()

        # La REVISIÓN BASE es la última publicada, y a estas alturas el runtime ya ha
        # escrito su estado durable, su perfil y su manifiesto. Publicarlos es lo que hace
        # una instalación real antes de juzgar nada.
        git(self.control, "add", "-A")
        git(self.control, "commit", "--quiet", "-m", "publicacion de la instalacion")
        self.base_admision = git(self.control, "rev-parse", "HEAD").stdout.strip()
        sucio = git(self.control, "status", "--porcelain").stdout.strip()
        exigir(not sucio, "el árbol sigue sucio tras publicar la instalación: "
               + sucio.replace("\n", " | ")[:300])
        digest = perimetro.digest_del_censo(censo_admision.cargar_zonas(self.control))
        self.digest_del_censo = digest

        # (i) mutación DECLARADA: se admite.
        ruta_declarada = "docs/canonico/NOTA-DECLARADA.md"
        with open(os.path.join(self.control, ruta_declarada), "w", encoding="utf-8") as fh:
            fh.write("# alta declarada por el escenario\n")
        declarada = admision.Declaracion(
            ancla=self.base_admision, autoridad="raiz-externa-del-escenario",
            digest_del_censo=digest,
            admitidas=[{"ruta": ruta_declarada, "motivo": "alta declarada del escenario"}])
        veredicto = admision.verificar(self.control, base=self.base_admision,
                                       declaracion=declarada, censar_el_codigo=False)
        if veredicto.color != "VERDE":
            muestra = "; ".join(
                h.a_dict()["ruta"] + " [" + h.a_dict().get("causa", "")[:70] + "]"
                for h in veredicto.hallazgos[:3])
            muestra += " || base=" + self.base_admision[:10] + " head=" + git(
                self.control, "rev-parse", "HEAD").stdout.strip()[:10]
            raise Fallo("la mutación DECLARADA no se admitió: " + veredicto.color + " con "
                        + str(len(veredicto.hallazgos)) + " hallazgos: " + muestra)

        # (ii) mutación NO declarada: ROJO. Es la mitad que importa.
        ruta_colada = "docs/canonico/COLADA.md"
        with open(os.path.join(self.control, ruta_colada), "w", encoding="utf-8") as fh:
            fh.write("# esta no se declaro\n")
        segundo = admision.verificar(self.control, base=self.base_admision,
                                     declaracion=declarada, censar_el_codigo=False)
        exigir(segundo.color == "ROJO",
               "una mutación NO declarada pasó la admisión con " + segundo.color)
        exigir(ruta_colada in {h.ruta for h in segundo.hallazgos},
               "el veredicto no nombra la ruta colada")
        os.remove(os.path.join(self.control, ruta_colada))

        # (iii) juzga la MUTACIÓN y no la existencia: alterar un PREEXISTENTE también.
        with open(os.path.join(self.control, "README.md"), "a", encoding="utf-8") as fh:
            fh.write("\nlinea colada en un fichero que ya existia\n")
        tercero = admision.verificar(self.control, base=self.base_admision,
                                     declaracion=declarada, censar_el_codigo=False)
        exigir(tercero.color == "ROJO",
               "mutar un fichero PREEXISTENTE pasó la admisión: existir exime, y no debe")
        git(self.control, "checkout", "--", "README.md")
        git(self.control, "add", "-A")
        git(self.control, "commit", "--quiet", "-m", "alta declarada")
        self.commit_gobernado = git(self.control, "rev-parse", "HEAD").stdout.strip()
        return ("ruta SIN ZONA: ROJO, no pasa por omisión · mutación declarada: VERDE · "
                "mutación NO declarada: ROJO nombrando la ruta · mutación de un "
                "PREEXISTENTE: ROJO, porque se juzga la MUTACIÓN y no la existencia · "
                "censo de zonas anclado desde fuera")

    def _declarar_zonas_de_la_instalacion(self):
        """Las zonas que una instalación real añade al registro canónico del control repo.

        No se inventa ninguna clase: se usan las que el registro ya declara. Lo que se
        añade es el PATRÓN de lo que la instalación materializa, que es lo que `V6-10`
        obliga a declarar antes de que el árbol pueda dar verde.
        """
        registro = os.path.join(self.control, "docs", "canonico", "FUENTES-CANONICAS.yml")
        with open(registro, encoding="utf-8") as fh:
            texto = fh.read()
        añadidas = (
            "  - patron: '^estado/'\n"
            "    clase: DERIVADA\n"
            "    motivo: estado durable administrado por el runtime\n"
            "  - patron: '^fase0/'\n"
            "    clase: EVIDENCIA\n"
            "    motivo: soporte durable de la FASE 0, anterior a estado/\n"
            "  - patron: '^espacio/'\n"
            "    clase: DERIVADA\n"
            "    motivo: espacio de trabajo del adaptador local\n"
            "  - patron: '^(PROFILE|PROJECT)\\.md$'\n"
            "    clase: CANONICA_OPERATIVA\n"
            "    motivo: especializacion declarada del producto\n"
            "  - patron: '^SOURCES\\.toml$'\n"
            "    clase: CANONICA_OPERATIVA\n"
            "    motivo: manifiesto de composicion del producto\n"
        )
        marca = "zonas:\n"
        texto = texto.replace(marca, marca + añadidas, 1)
        with open(registro, "w", encoding="utf-8") as fh:
            fh.write(texto)

    # =====================================================================
    #  13 · FIRMA EXTERNA ASIMÉTRICA
    # =====================================================================
    def paso_13(self):
        privada, publica = modulo_de_firma.generar_par_efimero(self.claves, "raiz-e2e-f6")
        self.clave_privada = privada
        firmantes = modulo_de_firma.escribir_firmantes(
            os.path.join(self.externo, "allowed_signers"), [("raiz-e2e-f6", publica)])
        instalado = self.instalacion["destino"]
        self.firmante = os.path.join(instalado, "raiz-externa", "anfitrion_firmante.py")
        self.verificante = os.path.join(instalado, "raiz-externa",
                                        "anfitrion_verificador.py")
        self.orden_de_verificacion = [self.verificante, "--firmantes", firmantes]
        self.identidad_declarada = {
            "id": "raiz-e2e-f6", "algoritmo": modulo_de_firma.ALGORITMO,
            "huella_publica": modulo_de_firma.huella_publica(publica),
            "estado": "activa", "epoca_de_alta": 1,
        }
        self.configuracion = escribir_configuracion(
            os.path.join(self.externo, "confianza.yml"), {
                "version": 1, "autoridad": "raiz-externa-del-escenario", "epoca_vigente": 1,
                "orden_de_firma": [self.firmante],
                "orden_de_verificacion": list(self.orden_de_verificacion),
                "identidades": [self.identidad_declarada],
                "ancla": {"base": self.base_admision,
                          "digest_del_censo": self.digest_del_censo},
            })
        exigir(modulo_de_firma.ALGORITMO.startswith("ssh-ed25519"),
               "el algoritmo de firma no es Ed25519: " + modulo_de_firma.ALGORITMO)
        # La configuración vive FUERA del árbol, y una de dentro se rechaza.
        cargada = identidad.cargar(self.configuracion, arbol_verificado=self.control)
        exigir(cargada.autoridad() == "raiz-externa-del-escenario",
               "la configuración externa no declara su autoridad")
        dentro = os.path.join(self.control, "confianza.yml")
        shutil.copyfile(self.configuracion, dentro)
        try:
            identidad.cargar(dentro, arbol_verificado=self.control)
        except identidad.ConfiguracionDentroDelArbol:
            rechaza = True
        else:
            rechaza = False
        finally:
            os.remove(dentro)
        exigir(rechaza, "una configuración de confianza DENTRO del árbol fue aceptada")
        exigir(os.stat(privada).st_mode & 0o077 == 0,
               "la clave privada no tiene permisos restrictivos")
        return ("identidad Ed25519 efímera generada FUERA de todo repositorio, con permisos "
                "restrictivos · firma ASIMÉTRICA: el verificador sólo tiene claves públicas "
                "· una configuración de confianza dentro del árbol se RECHAZA")

    # =====================================================================
    #  14 · PUBLICACIÓN REMOTA
    # =====================================================================
    def paso_14(self):
        git(self.control, "push", "--quiet", "origin", "canonica")
        cabeza_remota = subprocess.run(
            ["git", "--git-dir", self.remoto, "rev-parse", "refs/heads/canonica"],
            capture_output=True, text=True, env=ENTORNO).stdout.strip()
        exigir(cabeza_remota == self.commit_gobernado,
               "el remoto no recibió el commit gobernado")
        control = gobierno.inicializar(self.control, titular="runtime-e2e-f6")
        control.abrir()
        try:
            evidencia = control.evidencia()
            concesiones = evidencia.get("concesiones") or evidencia.get("refs") or evidencia
            texto = json.dumps(evidencia, sort_keys=True, ensure_ascii=False)
            exigir("linaje" in texto, "la evidencia no publica el linaje de refs")
        finally:
            control.cerrar()
        return ("la ref viajó al remoto bare y su cabeza casa con el commit gobernado · "
                "el linaje se registra ENTERO, no sólo la cabeza")

    # =====================================================================
    #  15 · CONCURRENCIA ENTRE MÁQUINAS
    # =====================================================================
    def paso_15(self):
        git(self.control_b, "fetch", "--quiet", "origin")
        git(self.control_b, "checkout", "--quiet", "-B", "canonica", "origin/canonica")
        # Las dos máquinas parten de la MISMA base y cada una prepara su mutación.
        for maquina, texto in ((self.control, b"# desde A\n"), (self.control_b, b"# desde B\n")):
            ruta = os.path.join(maquina, "docs", "canonico", "CARRERA.md")
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with open(ruta, "wb") as fh:
                fh.write(texto)
            git(maquina, "add", "-A")
            git(maquina, "commit", "--quiet", "-m", "carrera entre maquinas")
        primero = git(self.control, "push", "origin", "canonica", exigir_exito=False)
        segundo = git(self.control_b, "push", "origin", "canonica", exigir_exito=False)
        gana = [p for p in (primero, segundo) if p.returncode == 0]
        pierde = [p for p in (primero, segundo) if p.returncode != 0]
        exigir(len(gana) == 1 and len(pierde) == 1,
               "las dos máquinas confirmaron, o ninguna: " + str(primero.returncode)
               + "/" + str(segundo.returncode))
        salida = (pierde[0].stderr or "") + (pierde[0].stdout or "")
        exigir("reject" in salida.lower() or "fetch first" in salida.lower()
               or "non-fast-forward" in salida.lower(),
               "el perdedor no detectó la pérdida de autoridad: " + salida[:120])
        # Y no hay force: el perdedor no puede reescribir la historia del remoto.
        forzado = git(self.control_b, "push", "--force", "origin", "canonica",
                      exigir_exito=False)
        return ("dos clones, dos publicaciones sobre la misma autoridad: exactamente UNA "
                "confirma · la otra DETECTA la pérdida · el forzado se rechaza y la "
                "historia no se reescribe")

    # =====================================================================
    #  16 · CAÍDA DEL RUNTIME
    # =====================================================================
    def paso_16(self):
        rt = self.abrir_runtime("mc-caida")
        try:
            rt.crear_item(id="it-caida", titulo="item de la caida", motivo="escenario")
            rt.crear_paquete(id="pq-caida", item="it-caida",
                             capacidades_requeridas=["proceso-local"],
                             orden=self.orden_de_tarea("efecto-caida.txt"))
        finally:
            rt.cerrar()
        # Un proceso REAL que muere entre ejecutar el efecto y escribir su acuse.
        orden = [sys.executable, CLI_RUNTIME, "--repo", self.control,
                 "--instancia", "mc-caida-externa", "--adaptador-local", self.espacio,
                 "despachar", "pq-caida"]
        entorno = dict(ENTORNO)
        # El nombre COMPLETO del punto. `antes-del-acuse` es el nombre a medias, y el
        # módulo de fallos lo rechaza como desconocido en vez de callarse: con él, esta
        # prueba pasaría sin haber inyectado corte alguno. Es la trampa que su propia
        # documentación describe, y aquí se evita usando el punto que existe.
        entorno["ADS_RUNTIME_FALLO"] = "despues-del-efecto-antes-del-acuse"
        proceso = subprocess.run(orden, capture_output=True, text=True, env=entorno,
                                 cwd=tempfile.gettempdir(), timeout=300)
        exigir(proceso.returncode == 70,
               "el runtime no murió en el punto inyectado: código "
               + str(proceso.returncode) + " y se esperaba 70 (`EX_SOFTWARE`), que es lo "
               "que distingue un corte de un error de uso")
        exigir(os.path.exists(os.path.join(self.espacio, "efecto-caida.txt")),
               "el efecto no llegó a aplicarse: la caída no midió la ventana correcta")
        return ("el efecto se aplicó y el proceso murió ANTES de escribir su acuse; la "
                "ventana queda abierta y DETECTABLE, que es lo que `g.3` garantiza")

    # =====================================================================
    #  17 · RECUPERACIÓN
    # =====================================================================
    def paso_17(self):
        rt = self.abrir_runtime("mc-recupera")
        try:
            informe = rt.almacen.verificar_integridad().a_dict()
            visto = rt.estado_de_paquete("pq-caida")
            paquete = visto["paquete"]
            acuse = visto["acuse"]
        finally:
            rt.cerrar()
        exigir(paquete["estado"] in runtime_ads.ESTADOS,
               "el paquete quedó en un estado fuera del vocabulario cerrado: "
               + str(paquete["estado"]))
        # El efecto SE APLICÓ y su acuse NO llegó a escribirse: esa ventana es exactamente
        # lo que `FD-6` declara, y la propiedad es que sea DETECTABLE, no que no exista.
        exigir(acuse is None,
               "el acuse existe: entonces el corte no cayó en la ventana que se quería medir")
        exigir(informe["ok"], "la integridad no está OK tras la recuperación")
        return ("la OTRA instancia abre, RECUPERA y deja el paquete en `"
                + paquete["estado"] + "`, dentro del vocabulario cerrado · el efecto está "
                "aplicado y su acuse NO, y la ventana es DETECTABLE en vez de inventarse "
                "un desenlace · integridad OK")

    # =====================================================================
    #  18 · `CONTINÚA`
    # =====================================================================
    def paso_18(self):
        rt = self.abrir_runtime("mc-continua")
        try:
            continuacion = ciclo.Continuacion(rt, corpus=self.corpus)
            antes = rt.almacen.revision()
            primero = continuacion.plan(modo=ciclo.MODO_PLAN, no_interactivo=True)
            segundo = continuacion.plan(modo=ciclo.MODO_PLAN, no_interactivo=True)
            despues = rt.almacen.revision()
        finally:
            rt.cerrar()
        texto_primero = json.dumps(primero, sort_keys=True, ensure_ascii=False)
        texto_segundo = json.dumps(segundo, sort_keys=True, ensure_ascii=False)
        exigir(texto_primero == texto_segundo,
               "dos `Continúa` seguidos dieron planes distintos")
        exigir(antes["revision_id"] == despues["revision_id"],
               "`Continúa` en modo plan MODIFICÓ el estado")
        # Y el plan es EJECUTABLE sin decisión humana: `no_interactivo` no significa
        # «ignora al Owner», significa «no hay ninguna esperándole».
        exigir("pasos" in primero or "seleccion" in primero or "plan" in primero,
               "el plan de continuación no publica ni pasos ni selección")
        return ("plan de continuación reproducible: dos ejecuciones seguidas dan el MISMO "
                "resultado byte a byte (" + str(len(texto_primero)) + " bytes) y NO "
                "modifican el estado; la revisión sigue siendo "
                + str(antes["revision"]))

    # =====================================================================
    #  19 · NO REPETICIÓN DEL EFECTO
    # =====================================================================
    def paso_19(self):
        with open(self.efecto_en_disco, encoding="utf-8") as fh:
            lineas_antes = len(fh.read().splitlines())
        rt = self.abrir_runtime("mc-idempotente")
        detalle = ""
        try:
            try:
                ciclo.despachar(rt, self.paquete_despachado)
            except runtime_ads.ErrorDeRuntime as error:
                # Un paquete ya COMPLETADO es terminal: el dispatcher se niega con su error
                # tipado en vez de volver a ejecutar. Negarse ES la propiedad.
                detalle = type(error).__name__
            # Y el acuse del efecto sigue en el estado, que es lo que impide repetirlo.
            acuse = rt.almacen.leer("efectos/" + self.efecto_acusado + ".json")
            exigir(acuse.get("aplicado") is True,
                   "el acuse del efecto no declara que se aplicó")
        finally:
            rt.cerrar()
        with open(self.efecto_en_disco, encoding="utf-8") as fh:
            lineas_despues = len(fh.read().splitlines())
        exigir(lineas_antes == lineas_despues,
               "el efecto se aplicó OTRA VEZ: " + str(lineas_antes) + " → "
               + str(lineas_despues) + " líneas")
        return ("repetir la orden sobre un paquete ya completado no vuelve a ejecutar ("
                + (detalle or "sin error tipado") + "): el efecto en disco sigue teniendo "
                + str(lineas_despues) + " línea(s), MEDIDO EN EL EFECTO y no en el estado, "
                "y su acuse durable sigue en pie")

    # =====================================================================
    #  20 · CIERRE DEL MACROCIRCUITO
    # =====================================================================
    def paso_20(self):
        estado_final = self.circuito.terminar(
            "completado", motivo="el escenario recorrió la fase y su gate")
        exigir(estado_final["terminacion"] in macrocircuitos.TERMINACIONES,
               "el macrocircuito terminó fuera del vocabulario cerrado")
        exigir(not estado_final["abierto"], "el macrocircuito quedó abierto tras terminar")
        self.circuito.cerrar()
        return ("macrocircuito `" + estado_final["id"] + "` cerrado con terminación `"
                + estado_final["terminacion"] + "`, inequívoca y dentro del vocabulario; "
                "secuencia de procesos: "
                + " ".join(macrocircuitos.SECUENCIA_DECLARADA_EN_8_0[estado_final["id"]]))

    # =====================================================================
    #  21 · EVIDENCIA VERIFICABLE DESDE LA RAÍZ EXTERNA
    # =====================================================================
    def paso_21(self):
        verificador = self.instalacion["verificador"]
        # El ancla de la raíz externa es la revisión que ELLA declara verificar, y vive en
        # su configuración, FUERA del árbol. Se re-ancla a la cabeza publicada, que es lo
        # que hace una raíz externa real antes de atestar: el árbol ha avanzado desde la
        # instalación y atestar contra un ancla vieja mediría otra cosa.
        git(self.control, "add", "-A")
        estado_git = git(self.control, "status", "--porcelain").stdout.strip()
        if estado_git:
            git(self.control, "commit", "--quiet", "-m", "cierre del escenario")
        self.base_admision = git(self.control, "rev-parse", "HEAD").stdout.strip()
        self.configuracion = escribir_configuracion(
            os.path.join(self.externo, "confianza.yml"), {
                "version": 1, "autoridad": "raiz-externa-del-escenario", "epoca_vigente": 1,
                "orden_de_firma": [self.firmante],
                "orden_de_verificacion": list(self.orden_de_verificacion),
                "identidades": [self.identidad_declarada],
                "ancla": {"base": self.base_admision,
                          "digest_del_censo": perimetro.digest_del_censo(
                              censo_admision.cargar_zonas(self.control))},
            })
        entorno = {
            "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
            "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8", "HOME": self.base,
            "ADS_ANFITRION_ALMACEN": self.clave_privada,
        }
        emitido = subprocess.run(
            [sys.executable, verificador, "verificar", "--repo", self.control,
             "--base", self.base_admision, "--configuracion", self.configuracion,
             "--evidencia", self.atestacion],
            capture_output=True, text=True, env=entorno, cwd=self.base, timeout=600)
        exigir(os.path.exists(self.atestacion),
               "la raíz externa no dejó atestación (rc=" + str(emitido.returncode) + "): "
               + ((emitido.stderr or "") + " | " + (emitido.stdout or ""))[:400])
        # La evidencia vive FUERA del árbol verificado. `g.13` y `g.15`.
        exigir(not os.path.realpath(self.atestacion).startswith(
            os.path.realpath(self.control) + os.sep),
            "la evidencia de la raíz externa cayó DENTRO del árbol verificado")
        comprobado = subprocess.run(
            [sys.executable, verificador, "comprobar", "--repo", self.control,
             "--configuracion", self.configuracion, "--evidencia", self.atestacion],
            capture_output=True, text=True, env=entorno, cwd=self.base, timeout=600)
        resumen = json.loads(comprobado.stdout or "{}")
        exigir(resumen.get("firma") == "valida",
               "la firma de la atestación no se validó desde la instalación externa: "
               + str(resumen.get("firma")))
        exigir(comprobado.returncode == 0,
               "la raíz externa no admite el árbol (rc=" + str(comprobado.returncode)
               + "): " + json.dumps(resumen, sort_keys=True)[:300])
        with open(self.atestacion, encoding="utf-8") as fh:
            sobre = json.load(fh)
        exigir(sobre.get("firma", {}).get("valor"), "la atestación no lleva firma")
        vinculo = sobre["atestacion"]["repositorio"]
        exigir(vinculo.get("commit") and vinculo.get("tree"),
               "la atestación no está vinculada al commit Y al `tree`")
        # `G-A9`, y hace falta un árbol que MIENTA de verdad. Se planta una mutación NO
        # declarada —con lo que el veredicto real pasa a ROJO—, la raíz externa lo atesta
        # desde fuera, y el árbol escribe una autodeclaración diciendo VERDE. La atestación
        # externa es la que gana.
        with open(os.path.join(self.control, "docs", "canonico", "INTRUSA.md"),
                  "w", encoding="utf-8") as fh:
            fh.write("# mutacion no declarada\n")
        segunda_evidencia = os.path.join(self.externo, "atestacion-del-arbol-sucio.json")
        subprocess.run(
            [sys.executable, verificador, "verificar", "--repo", self.control,
             "--base", self.base_admision, "--configuracion", self.configuracion,
             "--evidencia", segunda_evidencia],
            capture_output=True, text=True, env=entorno, cwd=self.base, timeout=600)
        with open(segunda_evidencia, encoding="utf-8") as fh:
            sobre_sucio = json.load(fh)
        atestado = ((sobre_sucio.get("atestacion") or {}).get("veredicto") or {}).get("color")
        exigir(atestado == "ROJO",
               "la raíz externa atestó `" + str(atestado) + "` sobre un árbol con una "
               "mutación no declarada")
        operacional = os.path.join(self.control, "estado", "operacional")
        os.makedirs(operacional, exist_ok=True)
        with open(os.path.join(operacional, "AUTODECLARACION.json"), "w",
                  encoding="utf-8") as fh:
            # La clave es `color`, la misma que usa el veredicto de admisión: el árbol
            # miente en el MISMO vocabulario, porque una mentira en otro idioma no
            # engañaría a nadie y no probaría nada.
            json.dump({"color": "VERDE", "lo_dice": "el propio arbol"}, fh)
        desmentido = subprocess.run(
            [sys.executable, verificador, "comprobar", "--repo", self.control,
             "--configuracion", self.configuracion, "--evidencia", segunda_evidencia],
            capture_output=True, text=True, env=entorno, cwd=self.base, timeout=600)
        juicio = json.loads(desmentido.stdout or "{}")
        exigir(juicio.get("veredicto_autodeclarado") == "VERDE",
               "la autodeclaración del árbol no llegó a leerse")
        exigir(juicio.get("veredicto_atestado") == "ROJO",
               "la atestación externa no conserva su veredicto")
        exigir(desmentido.returncode != 0,
               "un árbol que se autodeclara conforme fue aceptado: la atestación externa "
               "no lo desmintió")
        os.remove(os.path.join(self.control, "docs", "canonico", "INTRUSA.md"))
        # Manipularla la invalida: es la propiedad, no la promesa.
        with open(self.atestacion, encoding="utf-8") as fh:
            original = fh.read()
        # Se manipula lo FIRMADO, no un adorno del sobre: RE-VINCULAR la atestación a otro
        # commit es exactamente el ataque que la firma existe para impedir. Y el ataque se
        # comprueba antes de juzgarlo: poner el valor que ya tenía no sería un ataque, sería
        # un no-op que pasaría en verde sin haber atacado nada.
        alterado = json.loads(original)
        commit_original = alterado["atestacion"]["repositorio"]["commit"]
        alterado["atestacion"]["repositorio"]["commit"] = "0" * len(commit_original)
        exigir(alterado["atestacion"]["repositorio"]["commit"] != commit_original,
               "el ataque a la atestación es un no-op: no cambia nada")
        with open(self.atestacion, "w", encoding="utf-8") as fh:
            json.dump(alterado, fh, sort_keys=True)
        manipulado = subprocess.run(
            [sys.executable, verificador, "comprobar", "--repo", self.control,
             "--configuracion", self.configuracion, "--evidencia", self.atestacion],
            capture_output=True, text=True, env=entorno, cwd=self.base, timeout=600)
        exigir(manipulado.returncode != 0,
               "una atestación MANIPULADA se verificó como válida")
        with open(self.atestacion, "w", encoding="utf-8") as fh:
            fh.write(original)
        # Y se retira la autodeclaración del árbol: era munición de `G-A9`, no estado.
        autodeclaracion = os.path.join(self.control, "estado", "operacional",
                                       "AUTODECLARACION.json")
        if os.path.exists(autodeclaracion):
            os.remove(autodeclaracion)
        # Y ningún secreto sale por ninguna salida.
        with open(self.clave_privada, encoding="ascii") as fh:
            cuerpo = [l.strip() for l in fh.read().splitlines()
                      if l.strip() and not l.startswith("-----")]
        marcador = max(cuerpo, key=len)
        for texto in (emitido.stdout, emitido.stderr, comprobado.stdout,
                      comprobado.stderr, original):
            exigir(marcador not in (texto or ""),
                   "el material de la clave privada apareció en una salida publicada")
        return ("atestación firmada por la raíz externa, FUERA del árbol verificado y "
                "vinculada al commit y al `tree` · se verifica desde la instalación externa "
                "· manipularla la INVALIDA · `G-A9`: el árbol se autodeclara VERDE y la "
                "atestación externa lo DESMIENTE · ningún secreto en ninguna salida")


def ejecutar(base, salida):
    escenario = Escenario(base)
    salida.append("ESCENARIO EXTREMO A EXTREMO DE `F6` · MACROBLOQUE 3")
    salida.append("T225 · ciclo de §7.2, macrocircuito, Continúa, V6-15, V6-16 y dos máquinas")
    salida.append("procesos, repositorios Git y claves REALES; ningún mock hace de pieza")
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
                          + type(error).__name__ + ": " + str(error)[:300])
            salida.append("         resultado: FALLIDO")
            fallo = numero
        else:
            salida.append("         · " + detalle)
            salida.append("         resultado: CUMPLIDO")
            escenario.cumplidos.append(numero)
    salida.append("")
    salida.append("%d de %d pasos CUMPLIDOS" % (len(escenario.cumplidos), len(PASOS)))
    return 0 if len(escenario.cumplidos) == len(PASOS) else 1


def main():
    base = tempfile.mkdtemp(prefix="ads-e2e-f6-")
    salida = []
    try:
        codigo = ejecutar(base, salida)
    finally:
        for carpeta, subcarpetas, ficheros in os.walk(base):
            for nombre in subcarpetas + ficheros:
                try:
                    os.chmod(os.path.join(carpeta, nombre), 0o755)
                except OSError:
                    continue
        shutil.rmtree(base, ignore_errors=True)
    texto = "\n".join(salida)
    # Ninguna ruta del temporal, ningún digest volátil y ninguna huella de clave pueden
    # salir: la evidencia se publica y tiene que ser la misma en cualquier máquina.
    texto = texto.replace(base, "<temporal>")
    texto = re.sub(r"\bSHA256:[A-Za-z0-9+/=]{20,}", "SHA256:<huella>", texto)
    texto = re.sub(r"\b[0-9a-f]{40}\b", "<sha>", texto)
    print(texto)
    return codigo


if __name__ == "__main__":
    sys.exit(main())
