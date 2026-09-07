#!/usr/bin/env python3
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
import os as _os_g03
import sys as _sys_g03

# LA GUARDA NO DEJA RASTRO EN EL ÁRBOL QUE JUZGA. Medido: al importar la guarda, Python
# escribía `validadores/__pycache__/aislamiento_de_arranque…pyc` en el árbol, y
# `comprobar_arranque.py` empezó a publicar «el proyecto arrastra `__pycache__`» sobre
# proyectos recién creados. Se desactiva la escritura de bytecode DURANTE la guarda y se
# devuelve al estado que tenía: lo que el punto importe después sigue cacheándose como
# siempre, y no se paga rendimiento por una comprobación que corre una vez.
_G03_BYTECODE = _sys_g03.dont_write_bytecode
_sys_g03.dont_write_bytecode = True
_G03_PROPIA = _os_g03.path.dirname(_os_g03.path.realpath(__file__))
_G03_SEDE = ""
_G03_RAIZ = _G03_PROPIA
while not _G03_SEDE:
    for _G03_CANDIDATA in (_G03_PROPIA,
                           _os_g03.path.join(_G03_RAIZ, "kernel", "operativo",
                                             "validadores")):
        if _os_g03.path.isfile(_os_g03.path.join(_G03_CANDIDATA,
                                                 "aislamiento_de_arranque.py")):
            _G03_SEDE = _G03_CANDIDATA
            break
    else:
        _G03_PADRE = _os_g03.path.dirname(_G03_RAIZ)
        if _G03_PADRE == _G03_RAIZ:
            _sys_g03.stderr.write(
                "[PROCEDENCIA_NO_FIABLE] no hay `aislamiento_de_arranque.py` ni junto a "
                "este punto ejecutable ni en el `kernel/operativo/validadores/` de ning\u00fan "
                "ancestro suyo: no se puede decidir si el arranque est\u00e1 aislado, y no se "
                "sigue\n")
            raise SystemExit(5)
        _G03_RAIZ = _G03_PADRE
_sys_g03.path.insert(0, _G03_SEDE)
import aislamiento_de_arranque as _aislamiento_g03                    # noqa: E402

AISLAMIENTO = _aislamiento_g03.exigir(__file__, __name__)
_sys_g03.dont_write_bytecode = _G03_BYTECODE

# `-I` deja FUERA de `sys.path` el directorio del guión —es lo que impide que un homónimo
# vecino se cuele— y los puntos que importan módulos hermanos lo necesitan. Se reintroduce
# por RUTA DERIVADA DE `__file__`, que no la escribe el lanzador.
if _G03_PROPIA not in _sys_g03.path:
    _sys_g03.path.insert(0, _G03_PROPIA)

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  `A2` lo midió sobre este mismo fichero: entró en el inventario de puntos ejecutables
#  SIN la purga y con un mecanismo `G-03` que divergía del de los otros sesenta en dos
#  escapes —`\u00fa` frente a `ú`—, y eso puso `T330` y `T381` en rojo y arrastró SIETE
#  obligaciones a «sin implementar» que no tenían defecto ninguno. Un punto ejecutable
#  lleva el mecanismo ENTERO y COPIADO, no adaptado: es exactamente lo que `T381` mide.

import sys as _sys
import os as _os

_RAIZ_DEL_APARATO = _os.path.dirname(_os.path.abspath(__file__))


def _entradas_del_lanzador():
    """Lo que el LANZADOR puede meter en la ruta de importación: `PYTHONPATH` y el `cwd`."""
    sospechosas = set()
    for entrada in (_os.environ.get("PYTHONPATH") or "").split(_os.pathsep):
        if entrada:
            sospechosas.add(_os.path.realpath(entrada))
    try:
        sospechosas.add(_os.path.realpath(_os.getcwd()))
    except OSError:
        # Un `cwd` borrado bajo los pies no es motivo para no purgar el resto.
        pass
    return sospechosas


def _purgar_la_ruta_de_importacion():
    """Retira de `sys.path` lo que venga del lanzador. Devuelve cuántas entradas retiró."""
    del_lanzador = _entradas_del_lanzador()
    propia = _os.path.realpath(_RAIZ_DEL_APARATO)
    conservadas, retiradas = [], []
    for entrada in _sys.path:
        try:
            real = _os.path.realpath(entrada or _os.getcwd())
        except OSError:
            conservadas.append(entrada)
            continue
        if real != propia and real in del_lanzador:
            retiradas.append(real)
        else:
            conservadas.append(entrada)
    _sys.path[:] = conservadas
    return retiradas


RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()

# CONTROL DEL CONTROL de la purga: `os` se usa para poder purgar, así que si `os` mismo
# viniera del lanzador la purga no probaría nada. No hay forma honesta de seguir: se dice y
# se sale con el código de PROCEDENCIA.
if _os.path.realpath(_os.path.dirname(_os.__file__ or ".")) in _entradas_del_lanzador():
    _sys.stderr.write(
        "[PROCEDENCIA_NO_FIABLE] el módulo `os` procede de la ruta de importación del "
        "lanzador: este punto ejecutable no puede garantizar de dónde salen sus módulos y "
        "NO ejecuta\n")
    raise SystemExit(5)

RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()
import argparse                                                       # noqa: E402
import io                                                             # noqa: E402
import os                                                             # noqa: E402
import subprocess                                                     # noqa: E402
import sys                                                            # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "..", ".."))

sys.path.insert(0, os.path.join(RAIZ, "kernel", "operativo", "validadores"))
import universo_de_instrumentos as universo                           # noqa: E402
import comprobar_evidencia as guardian                                # noqa: E402

TODOS_SATISFECHOS, HAY_INCUMPLIDOS, NO_SE_PUDO_COMPROBAR = 0, 1, 2
DIR_EVIDENCIA = "kernel/operativo/pruebas/evidencia"


class Juicio:
    def __init__(self):
        self.fallos = []
        self.notas = []

    def falla(self, condicion, causa):
        self.fallos.append((condicion, causa))

    def anota(self, texto):
        self.notas.append(texto)

    @property
    def ok(self):
        return not self.fallos


def _blob_de_head(base, rel):
    """Los bytes de `rel` tal y como están CONFIRMADOS en `HEAD`, o `None`."""
    proc = subprocess.run(["git", "-C", base, "show", "HEAD:%s" % rel],
                          capture_output=True)
    return proc.stdout if proc.returncode == 0 else None


def _escenarios_que_citan_evidencia(base):
    """`{fichero de evidencia: nº de `ads:escenario` que lo declaran}`, DERIVADO.

    Es la población de `T350`. No se escribe: se recorre el corpus y se cuenta.
    """
    import re                                                         # noqa: PLC0415
    cuenta = {}
    for ambito in ("kernel/operativo", "packs", "docs"):
        raiz = os.path.join(base, ambito)
        if not os.path.isdir(raiz):
            continue
        for dirpath, dirnames, filenames in os.walk(raiz):
            dirnames[:] = [d for d in dirnames if d not in universo.NO_SE_RECORRE]
            for nombre in sorted(filenames):
                if not nombre.endswith(".md"):
                    continue
                with open(os.path.join(dirpath, nombre), encoding="utf-8",
                          errors="replace") as manejador:
                    texto = manejador.read()
                for bloque in re.findall(r"```(?:yaml )?ads:escenario\n(.*?)```", texto,
                                         re.S):
                    for hallado in re.findall(r"([A-Za-z0-9_.-]+-salida\.txt)", bloque):
                        cuenta[hallado] = cuenta.get(hallado, 0) + 1
    return cuenta


def juzgar(base):
    """Las ocho condiciones `U-01`…`U-08`. Todas fallan cerrado."""
    j = Juicio()
    componentes = guardian.cargar_manifiesto(base)
    resta = universo.universo_contra_manifiesto(base, componentes)

    # `U-01` · ANTITAUTOLOGÍA. Un universo vacío haría que todo lo demás pasara solo.
    #     Y no basta con que no esté vacío: tiene que abarcar MÁS DE UN DIRECTORIO, que es
    #     exactamente lo que el universo anterior no hacía y lo que `V-G1` era.
    if len(resta["puntos"]) < 2:
        j.falla("U-01", "el universo derivado tiene %d puntos ejecutables: un universo "
                        "vacío o de uno hace que todo lo demás pase por construcción"
                        % len(resta["puntos"]))
    if len(resta["directorios"]) < 2:
        j.falla("U-01", "el universo derivado vive en %d directorio(s): si sólo cubriera "
                        "uno sería el mismo glob que `V-G1` con otro nombre"
                        % len(resta["directorios"]))

    # `U-02` · TODO PUNTO EJECUTABLE es fila del manifiesto o declara su exclusión EN EL
    #     FICHERO. Es la condición que pone rojo el duodécimo árbol de `M-04`: el
    #     instrumento sigue en el árbol aunque su fila desaparezca.
    for ruta in resta["sin_fila"]:
        j.falla("U-02", "`%s` es un punto ejecutable del árbol y NO es fila del manifiesto "
                        "ni declara `%s` con su motivo. O se declara, o se registra: en "
                        "silencio no se queda" % (ruta, universo.MARCA_DE_EXCLUSION))

    # `U-02 bis` · LA MARCA DE EXCLUSION EXPLICA, NO RETIRA. Sin esto, el duodecimo arbol
    #     de `M-04` se rehace en dos lineas: marcar el instrumento y quitarle la fila.
    for ruta, causa in resta["exclusiones_ilegitimas"]:
        j.falla("U-02", "`%s` reclama `%s` y no puede: %s"
                        % (ruta, universo.MARCA_DE_EXCLUSION, causa))

    # `U-02 ter` · ENLACES A DIRECTORIO dentro del ambito. `os.walk` no los sigue, de modo
    #     que un directorio de instrumentos colgado detras de un enlace seria invisible.
    for enlace in universo.enlaces_a_directorio(base):
        j.falla("U-02", "`%s` es un ENLACE A DIRECTORIO dentro del corpus: el recorrido no "
                        "lo sigue, de modo que lo que cuelgue de el quedaria fuera del "
                        "universo sin que nada lo dijera" % enlace)

    # `U-03` · toda fila apunta a un fichero que existe DONDE dice.
    for cid, ruta in resta["filas_sin_fichero"]:
        j.falla("U-03", "la fila '%s' declara `%s`, que no existe" % (cid, ruta))

    # `U-04` · toda fila `tipo: validador` es un punto ejecutable de verdad.
    for cid, ruta in resta["validador_sin_main"]:
        j.falla("U-04", "la fila '%s' se declara `tipo: validador` y `%s` no tiene guarda "
                        "`if __name__ == \"__main__\"`: nadie puede ejecutarla"
                        % (cid, ruta))

    # `U-05` · LOS OCHO CONTRASTES de `O31` §3, fila a fila.
    ids = [c.get("id") for c in componentes]
    repetidos = sorted({i for i in ids if ids.count(i) > 1})
    if repetidos:
        j.falla("U-05", "identificadores repetidos en el manifiesto: %s. Un identificador "
                        "que nombra a dos filas no identifica nada" % ", ".join(repetidos))
    for comp in componentes:
        cid = comp.get("id")
        if not cid:
            j.falla("U-05", "hay una fila sin `id`")
            continue
        if not comp.get("script"):
            j.falla("U-05", "la fila '%s' no declara `script`" % cid)
        if comp.get("tipo") not in ("validador", "biblioteca", "generador"):
            j.falla("U-05", "la fila '%s' declara `tipo: %r`, que no es ninguno de los "
                            "tres del manifiesto" % (cid, comp.get("tipo")))
        if comp.get("tipo") != "validador":
            continue
        if not comp.get("evidencia"):
            j.falla("U-05", "la fila '%s' es `tipo: validador` y no declara `evidencia`: "
                            "un validador sin evidencia no publica nada que contrastar"
                            % cid)
        if not (comp.get("firma_de_exito") or comp.get("debe_contener")
                or comp.get("evidencia_reflexiva")):
            j.falla("U-05", "la fila '%s' no declara condición de éxito —ni "
                            "`firma_de_exito`, ni `debe_contener`—: su verde no significa "
                            "nada" % cid)

    # `U-06` · EL RUNNER los ejecuta TODOS. Se deriva del propio runner, no se supone.
    en_runner = set()
    try:
        sys.path.insert(0, os.path.join(base, "kernel", "operativo", "validadores"))
        import registrar_evidencia                                    # noqa: PLC0415
        en_runner = {c.get("id") for c in
                     registrar_evidencia.cargar_manifiesto(base)}
    except Exception as error:                                        # noqa: BLE001
        j.anota("el runner no se pudo interrogar (%s: %s); `U-06` queda SIN COMPROBAR y "
                "eso NO cuenta como superada" % (type(error).__name__, error))
        j.falla("U-06", "no se pudo derivar del runner qué filas ejecuta")
    else:
        fuera = sorted({c.get("id") for c in componentes} - en_runner)
        if fuera:
            j.falla("U-06", "el runner NO ejecuta estas filas del manifiesto: %s"
                            % ", ".join(fuera))

    # `U-07` · TODO VALIDADOR CON EVIDENCIA TIENE GUARDIÁN. `O31` §3 lo exige con esas
    #     palabras: `T350` o un guardián MECÁNICAMENTE EQUIVALENTE. `T350` sólo alcanza a
    #     la evidencia que algún `ads:escenario` declara —13 de 45 no lo tenían, y entre
    #     ellas las cinco que miden las condiciones de `O30`—, así que el equivalente se
    #     ejerce AQUÍ: los bytes del árbol de trabajo contra el blob de `HEAD`.
    citas = _escenarios_que_citan_evidencia(base)
    sin_guardian, por_t350, por_equivalente = [], [], []
    for comp in componentes:
        if comp.get("tipo") != "validador" or not comp.get("evidencia"):
            continue
        nombre = comp["evidencia"]
        rel = os.path.join(DIR_EVIDENCIA, nombre)
        if citas.get(nombre, 0) > 0:
            por_t350.append(comp["id"])
            continue
        # GUARDIÁN EQUIVALENTE. Si la evidencia no existe y la fila tiene dispensa
        # reflexiva, su ausencia ya la juzga `T158`: aquí no se duplica ese juicio.
        # QUÉ ES «MECÁNICAMENTE EQUIVALENTE A `T350`», Y QUÉ NO PUEDE SER.
        #
        #     La primera redacción de esta condición comparaba los BYTES del árbol de
        #     trabajo con el blob de `HEAD`. Es un ancla que se mueve: el runner REGENERA
        #     la evidencia y después la juzga, de modo que en su propia pasada la evidencia
        #     recién escrita siempre difiere de `HEAD` y el control salía rojo por su
        #     construcción, no por un defecto. `O31` §6 lo dice con todas sus letras: «no
        #     exijas que una evidencia confirmada contenga el hash del mismo commit que la
        #     contiene… no conviertas esa autorreferencia imposible en otro bloqueo».
        #
        #     Lo que `T350` da y aquí se replica sin esa trampa son DOS cosas: que la
        #     evidencia esté ANCLADA en la historia —existe como blob en `HEAD`, de modo
        #     que aparecer o desaparecer deja rastro— y que su CONTENIDO esté JUZGADO —la
        #     fila declara condición de éxito, y `T158` la contrasta contra la salida—. Una
        #     evidencia anclada y juzgada no se puede alterar en silencio, que es lo que el
        #     guardián existe para impedir.
        # ESTE INSTRUMENTO NO SE JUZGA A SÍ MISMO EN ESTA CONDICIÓN, Y SE DICE POR QUÉ.
        #
        #     El runner publica la evidencia SÓLO cuando el instrumento sale con 0. Si esta
        #     condición se aplicara al propio juez, su primera evidencia no existiría nunca:
        #     saldría rojo por no estar anclada, el runner no la publicaría por salir rojo,
        #     y no se anclaría por no publicarse. Es la autorreferencia imposible que `O31`
        #     §6 manda no convertir en bloqueo.
        #
        #     Y NO QUEDA SIN GUARDIÁN: su contenido lo juzgan `T158` —contra su
        #     `firma_de_exito`, que exige los dos cardinales de antitautología— y `T350`, y
        #     su ausencia del manifiesto la caza `U-02`. Lo único que no hace es
        #     certificarse a sí mismo el anclaje.
        if os.path.basename(comp.get("script") or "") == os.path.basename(__file__):
            por_equivalente.append(comp["id"] + " (no se juzga a sí mismo el anclaje)")
            continue
        confirmado = _blob_de_head(base, rel)
        if confirmado is None:
            if comp.get("evidencia_reflexiva"):
                por_equivalente.append(comp["id"] + " (dispensada)")
                continue
            sin_guardian.append((comp["id"],
                                 "su evidencia NO está confirmada en `HEAD`: aparecer o "
                                 "desaparecer no dejaría rastro"))
            continue
        if not (comp.get("firma_de_exito") or comp.get("debe_contener")):
            sin_guardian.append((comp["id"],
                                 "su evidencia está anclada pero NADIE juzga su contenido: "
                                 "la fila no declara condición de éxito"))
            continue
        por_equivalente.append(comp["id"])
    for cid, causa in sin_guardian:
        j.falla("U-07", "'%s' sostiene su veredicto sobre una evidencia SIN GUARDIÁN: %s. "
                        "Ni `T350` la alcanza —ningún `ads:escenario` la declara— ni el "
                        "equivalente la sostiene" % (cid, causa))
    j.anota("guardián: %d por `T350` · %d por el equivalente de `O31` §3 · %d sin guardián"
            % (len(por_t350), len(por_equivalente), len(sin_guardian)))

    # `U-09` · LA SEGUNDA FUENTE INDEPENDIENTE · lo que la HISTORIA ya confirmó.
    #     La primera fuente contrasta por RUTA, y una ruta respalda varias filas:
    #     `comprobar-invariantes-criticos.py` respalda la fila que mide `K01`-`K24` y la
    #     de sus autopruebas. Medido durante esta corrección: retirar la primera dejando
    #     la segunda mantiene la ruta declarada y el contraste por ruta NO lo ve. Por eso
    #     se pregunta a `git` qué evidencias EXISTEN CONFIRMADAS, que no es el manifiesto
    #     ni el árbol de trabajo. Vaciar el universo exigiría reescribir la historia.
    huerfanas, motivo = universo.evidencias_huerfanas_de_la_historia(base, componentes)
    if motivo:
        j.falla("U-09", motivo + ", y eso NO cuenta como superada")
    for nombre in huerfanas:
        j.falla("U-09", "`%s` está CONFIRMADA en `HEAD` y ninguna fila viva la declara: "
                        "alguien retiró del manifiesto el instrumento que la produce sin "
                        "retirarla de la historia. Una retirada deliberada se hace en el "
                        "mismo commit que la evidencia, y entonces `HEAD` ya no la tiene"
                        % nombre)

    # `U-08` · nada sobra en el directorio de evidencia. Una evidencia huérfana es una que
    #     nadie regenera y de la que nadie responde.
    esperadas = {c["evidencia"] for c in componentes
                 if c.get("tipo") == "validador" and c.get("evidencia")}
    dir_ev = os.path.join(base, DIR_EVIDENCIA)
    if os.path.isdir(dir_ev):
        for nombre in sorted(os.listdir(dir_ev)):
            if nombre.endswith(".txt") and nombre not in esperadas:
                j.falla("U-08", "`%s/%s` no lo declara ninguna fila: nadie lo regenera y "
                                "nadie responde de él" % (DIR_EVIDENCIA, nombre))
    return j, resta, citas


def publicar(destino, base, j, resta, citas):
    destino.write("`O31` §3 y §5 · EL UNIVERSO DE INSTRUMENTOS, DERIVADO DEL ÁRBOL\n")
    destino.write("=" * 78 + "\n\n")
    proc = subprocess.run(["git", "-C", base, "rev-parse", "HEAD"], capture_output=True,
                          text=True)
    tree = subprocess.run(["git", "-C", base, "rev-parse", "HEAD^{tree}"],
                          capture_output=True, text=True)
    destino.write("  ANCLA   commit %s · tree %s\n\n"
                  % (proc.stdout.strip() or "?", tree.stdout.strip() or "?"))

    destino.write("CÓMO SE DERIVA, Y POR QUÉ NO ES UNA LISTA\n")
    destino.write("-" * 78 + "\n")
    destino.write(
        "  Un PUNTO EJECUTABLE es cualquier `.py` del árbol cuyo árbol sintáctico\n"
        "  contenga la guarda `if __name__ == \"__main__\"`. Se usa `ast` y no `grep`:\n"
        "  la cadena dentro de un comentario o de un mensaje NO cuenta. No se enumera\n"
        "  ningún directorio, de modo que mover un instrumento, renombrarlo o crear un\n"
        "  directorio nuevo NO lo saca del universo. `O31` §3: rojo por ausencia\n"
        "  material, no por una lista manual de rutas.\n\n")

    destino.write("EL UNIVERSO\n")
    destino.write("-" * 78 + "\n")
    destino.write("  puntos ejecutables en el árbol ....... %d\n" % len(resta["puntos"]))
    destino.write("  directorios que ocupan ............... %d\n"
                  % len(resta["directorios"]))
    for d in resta["directorios"]:
        destino.write("      %s\n" % (d or "(raíz)"))
    destino.write("  filas del manifiesto ................. %d\n"
                  % len(guardian.cargar_manifiesto(base)))
    destino.write("  puntos SIN fila ni exclusión ......... %d\n" % len(resta["sin_fila"]))
    destino.write("  exclusiones DECLARADAS en el fichero . %d\n\n"
                  % len(resta["excluidos"]))

    destino.write("LO QUE NO ES UN VALIDADOR, Y LO DICE ÉL MISMO\n")
    destino.write("-" * 78 + "\n")
    for ruta, motivo in sorted(resta["excluidos"].items()):
        destino.write("  %s\n      %s\n" % (ruta, motivo))
    if not resta["excluidos"]:
        destino.write("  ninguno\n")
    destino.write("\n")

    destino.write("EL GUARDIÁN DE CADA EVIDENCIA\n")
    destino.write("-" * 78 + "\n")
    destino.write("  `T350` alcanza a la evidencia que algún `ads:escenario` declara. Las\n"
                  "  demás las sostiene el equivalente de `O31` §3, ejercido aquí: los\n"
                  "  bytes del árbol de trabajo contra el blob de `HEAD`.\n")
    for comp in guardian.cargar_manifiesto(base):
        if comp.get("tipo") != "validador" or not comp.get("evidencia"):
            continue
        n = citas.get(comp["evidencia"], 0)
        destino.write("  %-34s %-44s %s\n"
                      % (comp["id"], comp["evidencia"],
                         "T350 (%d escenarios)" % n if n else "equivalente `O31` §3"))
    destino.write("\n")

    if j.notas:
        destino.write("OBSERVACIONES\n")
        destino.write("-" * 78 + "\n")
        for nota in j.notas:
            destino.write("  · %s\n" % nota)
        destino.write("\n")

    destino.write("LOS INCUMPLIMIENTOS, UNO A UNO\n")
    destino.write("-" * 78 + "\n")
    if not j.fallos:
        destino.write("  ninguno\n")
    for condicion, causa in j.fallos:
        destino.write("  [%s] %s\n" % (condicion, causa))
    destino.write("\n")

    destino.write("LO QUE ESTE VEREDICTO NO DEMUESTRA\n")
    destino.write("-" * 78 + "\n")
    destino.write(
        "  · no demuestra que cada instrumento MIDA BIEN lo suyo: demuestra que está\n"
        "    en el universo, que tiene fila, evidencia, condición de éxito y guardián;\n"
        "  · no cierra `M-04` ni `V-G1`: `O31` §5 y §7 reservan eso al verificador\n"
        "    independiente, y exigen que reproduzca el ataque él mismo;\n"
        "  · no juzga el contenido de la evidencia: eso es `T158` y `T350`.\n\n")

    destino.write("%d puntos ejecutables · %d directorios · %d sin fila ni exclusión · "
                  "%d exclusiones declaradas · %d incumplimientos\n"
                  % (len(resta["puntos"]), len(resta["directorios"]),
                     len(resta["sin_fila"]), len(resta["excluidos"]), len(j.fallos)))
    return TODOS_SATISFECHOS if j.ok else HAY_INCUMPLIDOS


# ===========================================================================
#  AUTOPRUEBAS · se sabotea el propio juez y se le exige que sepa decir que NO
# ===========================================================================
#  La lección `G-05`: un instrumento cuyo autotest pasa y cuyo producto no corre está roto
#  y sale verde. Aquí se ejerce la mitad contraria, sobre árboles sintéticos.
def autopruebas(destino):
    import shutil                                                     # noqa: PLC0415
    import tempfile                                                   # noqa: PLC0415

    controles = []

    def control(nombre, condicion, preparar):
        taller = tempfile.mkdtemp(prefix="ads-o31-universo-")
        try:
            copia = os.path.join(taller, "arbol")
            shutil.copytree(RAIZ, copia, symlinks=True,
                            ignore=shutil.ignore_patterns(*universo.NO_SE_RECORRE))
            preparar(copia)
            j, _resta, _citas = juzgar(copia)
            obtenidas = sorted({c for c, _ in j.fallos})
            controles.append({"nombre": nombre, "espera": condicion,
                              "obtenidas": obtenidas,
                              "detectado": condicion in obtenidas})
        finally:
            shutil.rmtree(taller, ignore_errors=True)

    def _quitar_fila(copia, cid):
        ruta = os.path.join(copia, "kernel/operativo/validadores/validadores.yaml")
        texto = io.open(ruta, encoding="utf-8").read()
        i = texto.index("  - id: %s\n" % cid)
        j2 = texto.index("\n  - id: ", i + 5) + 1
        io.open(ruta, "w", encoding="utf-8").write(texto[:i] + texto[j2:])

    # SE ESPERA `U-09` Y NO `U-02`, Y ES LA LECCIÓN DE ESTE CICLO: el script sigue
    # declarado por la fila de autopruebas, de modo que el contraste POR RUTA no ve la
    # retirada. Quien la ve es la segunda fuente independiente, la historia.
    control("un instrumento retirado del manifiesto sigue en el árbol", "U-09",
            lambda c: _quitar_fila(c, "invariantes-criticos"))

    def _mover(copia):
        origen = os.path.join(copia, "docs/evolucion/verificacion",
                              "comprobar-invariantes-criticos.py")
        destino_nuevo = os.path.join(copia, "docs/evolucion", "movido.py")
        shutil.move(origen, destino_nuevo)
    control("un instrumento MOVIDO de ruta", "U-02", _mover)

    def _nuevo(copia):
        nuevo = os.path.join(copia, "docs", "instrumento-nuevo.py")
        io.open(nuevo, "w", encoding="utf-8").write(
            'import sys\nif __name__ == "__main__":\n    sys.exit(0)\n')
    control("un instrumento NUEVO en un directorio que no existía", "U-02", _nuevo)

    def _borrar_marca(copia):
        ruta = os.path.join(copia, "kernel/operativo/runtime/ads_ciclo.py")
        texto = io.open(ruta, encoding="utf-8").read()
        i = texto.index(universo.MARCA_DE_EXCLUSION)
        fin = texto.index(")\n", i) + 2
        io.open(ruta, "w", encoding="utf-8").write(texto[:i - 1] + texto[fin:])
    control("se BORRA la declaración de exclusión de un punto", "U-02", _borrar_marca)

    def _fila_sin_fichero(copia):
        ruta = os.path.join(copia, "kernel/operativo/validadores/validadores.yaml")
        texto = io.open(ruta, encoding="utf-8").read()
        io.open(ruta, "w", encoding="utf-8").write(
            texto.replace("    script: comprobar-invariantes-criticos.py\n",
                          "    script: comprobar-invariantes-criticos-que-no-existe.py\n", 1))
    control("una fila apunta a un fichero que no existe", "U-03", _fila_sin_fichero)

    def _sin_condicion(copia):
        ruta = os.path.join(copia, "kernel/operativo/validadores/validadores.yaml")
        texto = io.open(ruta, encoding="utf-8").read()
        i = texto.index("  - id: lint\n")
        j2 = texto.index("\n  - id: ", i + 5) + 1
        bloque = texto[i:j2]
        limpio = "\n".join(l for l in bloque.split("\n")
                           if not l.strip().startswith(("firma_de_exito:", "debe_contener:",
                                                        "#", "'", '"'))
                           and l.strip() != "") + "\n"
        io.open(ruta, "w", encoding="utf-8").write(texto[:i] + limpio + texto[j2:])
    control("un validador sin condición de éxito", "U-05", _sin_condicion)

    def _evidencia_huerfana(copia):
        io.open(os.path.join(copia, DIR_EVIDENCIA, "huerfana-salida.txt"), "w",
                encoding="utf-8").write("nadie me regenera\n")
    control("una evidencia que ninguna fila declara", "U-08", _evidencia_huerfana)

    destino.write("`O31` · AUTOPRUEBAS DEL JUEZ DEL UNIVERSO\n")
    destino.write("=" * 78 + "\n\n")
    for fila in controles:
        destino.write("%-5s %-6s %s\n"
                      % ("OK" if fila["detectado"] else "FALLO", fila["espera"],
                         fila["nombre"]))
        if not fila["detectado"]:
            destino.write("        obtenidas: %s\n"
                          % (", ".join(fila["obtenidas"]) or "ninguna"))
    sin = [f for f in controles if not f["detectado"]]
    destino.write("\n%d controles · %d sin detectar\n" % (len(controles), len(sin)))
    return HAY_INCUMPLIDOS if sin else TODOS_SATISFECHOS


def main(argv=None):
    analizador = argparse.ArgumentParser(
        description="`O31` §3 y §5 · el universo de instrumentos, derivado del árbol")
    analizador.add_argument("--raiz", default=None)
    analizador.add_argument("--autopruebas", action="store_true")
    argumentos = analizador.parse_args(argv)
    base = os.path.abspath(argumentos.raiz) if argumentos.raiz else RAIZ
    if argumentos.autopruebas:
        return autopruebas(sys.stdout)
    j, resta, citas = juzgar(base)
    return publicar(sys.stdout, base, j, resta, citas)


if __name__ == "__main__":
    sys.exit(main())
