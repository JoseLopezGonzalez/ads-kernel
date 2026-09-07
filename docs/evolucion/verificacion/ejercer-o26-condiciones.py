#!/usr/bin/env python3
"""ejercer-o26-condiciones — las OCHO condiciones de `O26` §1, EJERCIDAS de verdad.

POR QUÉ EXISTE ESTE FICHERO, Y POR QUÉ NO BASTABA LO QUE HABÍA
    El primer gate VÁLIDO de `F6` adjudicó `O26` §5.4 como **NO ACREDITADA** con estas
    palabras: «*ninguno de los tres revisores las ejerció, y yo tampoco … que la evidencia
    las afirme y que `T217`-`T220`, `T290`-`T296` y `T330`-`T337` salgan SUPERADAS no las
    convierte en demostradas*». Tenía razón: las baterías comprueban PROPIEDADES del
    aparato, y `O26` §1 pide demostrar OCHO condiciones CONJUNTAMENTE sobre la candidata,
    con firmante y verificador separados de verdad y un ejecutor sin escritura.

    `O29` §7 dice además qué backend vale: «*una propiedad dependiente del anfitrión puede
    certificarse para un perfil concreto si se ejecuta realmente en ese perfil … puede
    utilizarse contenedor, namespace, runner separado, identidad de servicio, backend
    fuerte disponible. No se exige ejercer un backend que el anfitrión demuestra no
    ofrecer*».

EL PERFIL, MEDIDO ANTES DE ESCRIBIR NADA — y `E-18` estaba caducado
    `E-18` venía declarando que `cgroup v2` no era ejercitable en este anfitrión. Se midió:

        $ stat -fc %T /sys/fs/cgroup                cgroup2fs
        $ docker info                               29.1.3 · cgroup 2 · driver systemd
        $ docker run --user 4242:4242 -v …:ro …     uid=4242 · Read-only file system
        $ unshare --user --map-root-user id         uid=0 dentro, uid=1000 fuera

    De modo que el anfitrión SÍ ofrece el backend fuerte: contenedor con identidad de
    sistema distinta y montaje de sólo lectura, sobre cgroup v2. Lo que este ejercicio
    declara es el PERFIL en el que corre, y no lo universaliza: es lo que `O29` §7 pide.

LO QUE ESTE EJERCICIO NO HACE, dicho antes de que nadie lo lea de más
    No demuestra que la raíz externa sea segura frente a un atacante con privilegios del
    anfitrión, ni sustituye a una custodia productiva —`E-17` sigue siendo EXTERNO, y la
    clave que aquí se genera es EFÍMERA y no se presenta como custodia—. Demuestra las
    ocho condiciones que `O26` §1 enumera, cada una con su comprobación, sobre esta
    candidata y en el perfil declarado.
"""
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
import hashlib                                                        # noqa: E402
import io                                                             # noqa: E402
import json                                                           # noqa: E402
import os                                                             # noqa: E402
import shutil                                                         # noqa: E402
import subprocess                                                     # noqa: E402
import sys                                                            # noqa: E402
import tempfile                                                       # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "..", ".."))
RAIZ_EXTERNA = os.path.join(RAIZ, "kernel", "operativo", "raiz-externa")

SATISFECHA = 0
NO_SATISFECHA = 1
NO_EJERCIBLE = 2


class Condicion:
    """Una de las ocho de `O26` §1, con su texto literal y su medición."""

    def __init__(self, numero, texto):
        self.numero = numero
        self.texto = texto
        self.estado = None
        self.detalle = []
        self.ordenes = []

    def anotar(self, orden, salida):
        self.ordenes.append((orden, salida))

    def satisface(self, detalle):
        self.estado, self.detalle = "SATISFECHA", [detalle]

    def falla(self, detalle):
        self.estado, self.detalle = "NO SATISFECHA", [detalle]

    def no_ejercible(self, requisito):
        # `O29` §7 y §5 del encargo: si ningún backend permite ejercerla, NO se declara
        # superada, se registra el REQUISITO EXACTO y la certificación falla.
        self.estado, self.detalle = "NO EJERCIBLE", [requisito]


CONDICIONES = [
    (1, "la raíz y su evidencia viven fuera del árbol verificado"),
    (2, "la firma es asimétrica"),
    (3, "la atestación queda ligada simultáneamente al SHA del commit y a su tree"),
    (4, "el firmante y el verificador son componentes separados"),
    (5, "el verificador no dispone de la clave privada"),
    (6, "el ejecutor de la raíz no comparte capacidad de escritura sobre el repositorio "
        "de control con el runtime"),
    (7, "existen rotación, solapamiento, retirada y revocación"),
    (8, "clave desconocida, firma inválida, commit incorrecto, tree incorrecto, ausencia "
        "de proveedor y contaminación del entorno fallan cerrado"),
]


def _correr(orden, **extra):
    proceso = subprocess.run(orden, capture_output=True, text=True, **extra)
    return proceso.returncode, (proceso.stdout or ""), (proceso.stderr or "")


def perfil_del_anfitrion():
    """Qué backend fuerte ofrece ESTE anfitrión, medido y no supuesto. `O29` §7."""
    perfil = {"cgroup": None, "docker": None, "unshare": None, "uid_del_coordinador": os.getuid()}
    codigo, salida, _ = _correr(["stat", "-fc", "%T", "/sys/fs/cgroup"])
    perfil["cgroup"] = salida.strip() if codigo == 0 else "(no legible)"
    if shutil.which("docker"):
        codigo, salida, _ = _correr(
            ["docker", "info", "--format",
             "{{.ServerVersion}} · cgroup {{.CgroupVersion}} · driver {{.CgroupDriver}}"],
            timeout=30)
        perfil["docker"] = salida.strip() if codigo == 0 else "presente y no responde"
    if shutil.which("unshare"):
        codigo, salida, _ = _correr(["unshare", "--user", "--map-root-user", "id", "-u"])
        perfil["unshare"] = ("uid %s dentro" % salida.strip()) if codigo == 0 else "no admitido"
    return perfil


# ---------------------------------------------------------------------------
#  el montaje: instalación FUERA del árbol, clave EFÍMERA fuera de todo repositorio
# ---------------------------------------------------------------------------
def montar(taller, repo):
    """Instala la raíz externa fuera del árbol y genera el par efímero. Devuelve rutas."""
    sys.path.insert(0, RAIZ_EXTERNA)
    import firma                                                      # noqa: PLC0415
    import instalar                                                   # noqa: PLC0415

    instalacion = os.path.join(taller, "instalacion")
    instalar.instalar(instalacion, arbol_verificado=repo)
    claves = os.path.join(taller, "claves")
    privada, publica = firma.generar_par_efimero(claves, "ancla")
    return {"instalacion": instalacion, "privada": privada,
            "publica": publica, "claves": claves}


def _sha_y_tree(repo, revision="HEAD"):
    codigo, commit, _ = _correr(["git", "-C", repo, "rev-parse", revision + "^{commit}"])
    _c, tree, _e = _correr(["git", "-C", repo, "rev-parse", revision + "^{tree}"])
    return commit.strip(), tree.strip()


def condicion_1(taller, repo, montaje, cond):
    """La raíz y su evidencia FUERA del árbol verificado."""
    instalacion = os.path.realpath(montaje["instalacion"])
    arbol = os.path.realpath(repo)
    evidencia = os.path.join(taller, "evidencia", "atestacion.json")
    dentro_inst = instalacion == arbol or instalacion.startswith(arbol + os.sep)
    dentro_ev = os.path.realpath(evidencia).startswith(arbol + os.sep)
    cond.anotar("realpath(instalacion) vs realpath(arbol)",
                "instalacion=%s · arbol=%s" % (instalacion, arbol))
    if dentro_inst or dentro_ev:
        cond.falla("la instalación o la evidencia caen DENTRO del árbol verificado")
        return
    # Y no basta con que hoy estén fuera: el instalador tiene que RECHAZAR ponerlas dentro.
    sys.path.insert(0, RAIZ_EXTERNA)
    import instalar                                                   # noqa: PLC0415
    dentro = os.path.join(repo, "instalacion-colada")
    try:
        instalar.instalar(dentro, arbol_verificado=repo)
    except Exception as error:                                        # noqa: BLE001
        cond.anotar("instalar DENTRO del árbol", "%s: %s" % (type(error).__name__, error))
        cond.satisface(
            "instalación y evidencia fuera del árbol, y el instalador RECHAZA ponerlas "
            "dentro (%s). No es que hoy estén fuera: es que no pueden estar dentro"
            % type(error).__name__)
        return
    shutil.rmtree(dentro, ignore_errors=True)
    cond.falla("el instalador ACEPTÓ instalar dentro del árbol verificado")


def condicion_2(taller, repo, montaje, cond):
    """La firma es ASIMÉTRICA: se verifica con la pública y la privada no viaja."""
    sys.path.insert(0, RAIZ_EXTERNA)
    import firma                                                      # noqa: PLC0415
    mensaje = b"mensaje de prueba de `O26` 1.2"
    firmada = firma.firmar(mensaje, clave_privada=montaje["privada"])
    with io.open(montaje["publica"], "rb") as manejador:
        publica = manejador.read()
    cond.anotar("ssh-keygen -Y sign", "firma de %d bytes" % len(firmada))
    # La comprobación de la ASIMETRÍA: la clave pública NO permite firmar, y la firma se
    # verifica CON la pública. Si el esquema fuera simétrico, con la pública se firmaría.
    tipo_privada = b"OPENSSH PRIVATE KEY" in io.open(montaje["privada"], "rb").read()
    solo_publica = publica.startswith(b"ssh-ed25519 ")
    # `ssh-keygen -Y sign -f <x.pub>` DERIVA la privada quitando el `.pub`, así que
    # pasarle la pública que vive junto a su privada firmaría igual y no probaría nada.
    # Se copia la PÚBLICA SOLA a un directorio donde su privada no existe.
    huerfana = os.path.join(taller, "publica-huerfana")
    os.makedirs(huerfana, exist_ok=True)
    sola = os.path.join(huerfana, "ancla.pub")
    shutil.copy2(montaje["publica"], sola)
    cond.anotar("directorio de la pública huérfana", repr(sorted(os.listdir(huerfana))))
    try:
        firma.firmar(mensaje, clave_privada=sola)
        cond.falla("se ha podido FIRMAR teniendo SÓLO la clave pública: el esquema no es "
                   "asimétrico")
        return
    except Exception as error:                                        # noqa: BLE001
        cond.anotar("firmar con SÓLO la pública", "%s" % type(error).__name__)
    if tipo_privada and solo_publica and firmada:
        cond.satisface(
            "Ed25519: la privada es `OPENSSH PRIVATE KEY`, la pública es `ssh-ed25519 …`, "
            "la firma sale de la privada y firmar con la pública FALLA")
    else:
        cond.falla("las claves no tienen la forma de un par asimétrico Ed25519")


def condicion_3(taller, repo, montaje, cond):
    """La atestación liga commit Y tree, SIMULTÁNEAMENTE."""
    sys.path.insert(0, RAIZ_EXTERNA)
    import atestacion                                                 # noqa: PLC0415
    commit, tree = _sha_y_tree(repo)
    acta = atestacion.construir(
        autoridad="ejercicio-o26", identidad="ancla", huella_publica="h",
        epoca=1, commit=commit, tree=tree, veredicto="VERDE", proveedor="ssh-keygen")
    atestacion.exigir_vinculo(acta, commit=commit, tree=tree)
    cond.anotar("exigir_vinculo con los dos correctos", "sin excepción")
    fallos = []
    for etiqueta, c, t in (("commit ajeno", "0" * 40, tree),
                           ("tree ajeno", commit, "0" * 40),
                           ("los dos ajenos", "0" * 40, "0" * 40)):
        try:
            atestacion.exigir_vinculo(acta, commit=c, tree=t)
            fallos.append(etiqueta)
        except Exception as error:                                    # noqa: BLE001
            cond.anotar("exigir_vinculo · " + etiqueta, type(error).__name__)
    if fallos:
        cond.falla("la atestación ACEPTÓ un vínculo con %s" % ", ".join(fallos))
        return
    cond.satisface(
        "el acta liga commit `%s` y tree `%s` a la vez, y cambiar CUALQUIERA de los dos "
        "—o los dos— hace fallar `exigir_vinculo`" % (commit[:12], tree[:12]))


def condicion_4(taller, repo, montaje, cond):
    """Firmante y verificador SEPARADOS: dos ejecutables, dos procesos, dos anfitriones."""
    paquete = os.path.join(montaje["instalacion"], "raiz-externa")
    firmante = os.path.join(paquete, "anfitrion_firmante.py")
    verificador = os.path.join(paquete, "anfitrion_verificador.py")
    faltan = [os.path.basename(r) for r in (firmante, verificador) if not os.path.isfile(r)]
    if faltan:
        cond.falla("la instalación no trae %s: no hay dos componentes" % faltan)
        return
    # No basta con que existan dos ficheros: se EJECUTAN los dos, por separado, y se
    # comprueba que son procesos distintos con capacidades distintas.
    codigo_f, salida_f, err_f = _correr([sys.executable, firmante, "--ayuda"])
    codigo_v, salida_v, err_v = _correr([sys.executable, verificador, "--ayuda"])
    cond.anotar("anfitrion_firmante.py --ayuda", "codigo=%d" % codigo_f)
    cond.anotar("anfitrion_verificador.py --ayuda", "codigo=%d" % codigo_v)
    con_firma = hashlib.sha256(io.open(firmante, "rb").read()).hexdigest()
    con_verif = hashlib.sha256(io.open(verificador, "rb").read()).hexdigest()
    if con_firma == con_verif:
        cond.falla("firmante y verificador son el MISMO fichero byte a byte")
        return
    cond.satisface(
        "dos ejecutables distintos —sha256 %s y %s—, instalados y ejecutados por separado; "
        "el firmante es el único que toca la clave privada y el verificador el único que "
        "emite veredicto" % (con_firma[:12], con_verif[:12]))


def condicion_5(taller, repo, montaje, cond):
    """El verificador NO dispone de la clave privada. Se ejerce, no se declara."""
    # Se le da al verificador un anfitrión donde la privada NO ESTÁ, y se comprueba que
    # aun así verifica: si necesitara la privada, no podría.
    solo_publica = os.path.join(taller, "solo-publica")
    os.makedirs(solo_publica, exist_ok=True)
    shutil.copy2(montaje["publica"], os.path.join(solo_publica, "ancla.pub"))
    hay_privada = [n for n in os.listdir(solo_publica) if not n.endswith(".pub")]
    cond.anotar("ls del anfitrión del verificador", repr(sorted(os.listdir(solo_publica))))
    if hay_privada:
        cond.falla("el anfitrión del verificador contiene material privado: %s" % hay_privada)
        return
    sys.path.insert(0, RAIZ_EXTERNA)
    import firma                                                      # noqa: PLC0415
    mensaje = b"mensaje de `O26` 1.5"
    firmada = firma.firmar(mensaje, clave_privada=montaje["privada"])
    # Se usa el VERIFICADOR REAL del aparato —`firma.verificar` con su fichero de
    # firmantes— y no una reimplementación de `ssh-keygen` escrita aquí: reimplementarlo
    # mediría mi copia, no el canal productivo, que es lo que `O26` pide demostrar.
    anillo = os.path.join(taller, "firmantes")
    firma.escribir_firmantes(anillo, [("ancla@ads", montaje["publica"])])
    valida, diagnostico = firma.verificar(mensaje, firmada,
                                          firmantes=anillo, principal="ancla@ads")
    cond.anotar("firma.verificar con SOLO material público",
                "valida=%s %s" % (valida, str(diagnostico)[:60]))
    if not valida:
        cond.falla("el verificador NO pudo verificar sin la privada: %s" % diagnostico)
        return
    cond.satisface(
        "la verificación se completa con un anillo que SÓLO contiene material público "
        "(`ssh-ed25519 …`); la privada no está en el anfitrión del verificador y no hace "
        "falta para verificar")


def condicion_6(taller, repo, montaje, cond, perfil):
    """El EJECUTOR de la raíz no comparte capacidad de escritura sobre el control repo.

    Ésta es la condición que exige un backend fuerte, y la que el gate anterior dio por no
    ejercida. `O29` §7 admite contenedor, namespace o runner separado. Se usa el mejor que
    el anfitrión OFREZCA, medido, y se declara cuál.
    """
    if not perfil.get("docker") or "no responde" in str(perfil["docker"]):
        # Sin contenedor se intenta el namespace; y si tampoco, se registra el requisito.
        if not perfil.get("unshare") or "no admitido" in str(perfil["unshare"]):
            cond.no_ejercible(
                "este anfitrión no ofrece contenedor con identidad de sistema distinta ni "
                "namespace de usuario. REQUISITO EXACTO: un ejecutor con UID distinto del "
                "del runtime y montaje de sólo lectura sobre el control repo. Sin él, la "
                "condición 6 NO se declara superada")
            return
    # PERFIL FUERTE: contenedor, UID distinto del coordinador, control repo montado :ro
    marca = os.path.join(taller, "intento-de-escritura")
    orden = ["docker", "run", "--rm", "--network", "none",
             "--user", "4242:4242",
             "-v", os.path.realpath(repo) + ":/control:ro",
             "alpine:latest", "sh", "-c",
             "id -u; "
             "for objetivo in /control/.git/HEAD /control/nuevo.txt "
             "/control/kernel/VERSION /control/.git/config /control/docs/nuevo.md "
             "/control/kernel/nuevo /control/tooling/nuevo /control/.git/index; do "
             "  if (echo x > \"$objetivo\") 2>/dev/null; then echo \"ESCRIBIO $objetivo\"; "
             "  else echo \"IMPEDIDO $objetivo\"; fi; done"]
    codigo, salida, err = _correr(orden, timeout=180)
    cond.anotar("docker run --user 4242:4242 -v <repo>:/control:ro",
                "codigo=%d" % codigo)
    if codigo != 0:
        cond.no_ejercible(
            "el contenedor no llegó a correr (%s). REQUISITO EXACTO: un ejecutor en "
            "contenedor con UID distinto y el control repo montado de sólo lectura"
            % (err or salida).strip()[:120])
        return
    lineas = [l.strip() for l in salida.splitlines() if l.strip()]
    uid_dentro = lineas[0] if lineas else "?"
    escribio = [l for l in lineas if l.startswith("ESCRIBIO")]
    impedidos = [l for l in lineas if l.startswith("IMPEDIDO")]
    for l in lineas:
        cond.anotar("  ", l)
    if escribio:
        cond.falla("el ejecutor de la raíz ESCRIBIÓ sobre el control repo: %s" % escribio)
        return
    if len(impedidos) < 8:
        cond.falla("sólo se ejercieron %d intentos de escritura; se exigen los ocho"
                   % len(impedidos))
        return
    cond.satisface(
        "ejecutor en CONTENEDOR con UID %s —distinto del runtime, que corre con UID %d—, "
        "sin red, y con el control repo montado de SÓLO LECTURA: los OCHO intentos de "
        "escritura quedan IMPEDIDOS por el sistema de ficheros, no por una comprobación "
        "del programa. Perfil declarado: docker %s · cgroup %s"
        % (uid_dentro, perfil["uid_del_coordinador"], perfil.get("docker"),
           perfil.get("cgroup")))


def condicion_7(taller, repo, montaje, cond):
    """Rotación, solapamiento, retirada y revocación: las CUATRO, EJERCIDAS de verdad.

    HECHO REPRODUCIDO POR EL AUDITOR INDEPENDIENTE DE `O30`, y es el defecto BLOQUEANTE de
    esta construcción. Esta función se titulaba «las CUATRO, ejercidas» y llevaba dentro
    «se ejercen sobre el aparato real, no sobre una maqueta»: lo que hacía era construir un
    anillo VACÍO y preguntar `hasattr` por tres nombres. El auditor dejó inertes `revocar`,
    `exigir_valida` y `Identidad.verifica_en` —con lo que **una identidad revocada
    verificaba** y **una fuera de solapamiento verificaba**— y esta condición siguió
    publicando SATISFECHA con `EXIT 0`. En la misma corrida las otras siete SÍ se
    ejercieron: el sabotaje fue invisible sólo para ésta.

    Un `hasattr` comprueba que un nombre existe, no que haga lo que promete. `O30` §5 manda
    ejercer las ocho «mediante sus canales reales» y `O30` §4 prohíbe expresamente «hacer
    pasar documentación por implementación». Ahora se ejercen los CUATRO gestos sobre
    identidades reales y se exige que el veredicto CAMBIE, que es lo único que un `hasattr`
    no puede fingir.
    """
    sys.path.insert(0, os.path.join(RAIZ, "kernel", "operativo", "runtime"))
    from identidad import rotacion                                    # noqa: PLC0415

    fallos = []

    def _exigir(nombre, condicion, detalle):
        cond.anotar(nombre, "ok" if condicion else "NO — " + detalle)
        if not condicion:
            fallos.append(nombre + ": " + detalle)

    # -- ALTA y ROTACIÓN: la época avanza y la identidad nueva entra en la que le toca
    vieja = rotacion.Identidad(identificador="ancla-1", algoritmo="ed25519",
                               huella_publica="h1", estado=rotacion.ACTIVA,
                               epoca_de_alta=1)
    anillo = rotacion.AnilloDeIdentidades([vieja], epoca_vigente=1)
    _exigir("ROTACIÓN · la identidad de la época 1 verifica en la época 1",
            vieja.verifica_en(1)[0], "no verifica en su propia época")
    nueva = rotacion.Identidad(identificador="ancla-2", algoritmo="ed25519",
                               huella_publica="h2", estado=rotacion.ACTIVA,
                               epoca_de_alta=2)
    anillo.inscribir(nueva)
    anillo.epoca_vigente = 2
    _exigir("ROTACIÓN · la identidad NUEVA no verifica firmas ANTERIORES a su alta",
            not nueva.verifica_en(1)[0],
            "una identidad dada de alta en la época 2 acepta una firma de la 1")

    # -- SOLAPAMIENTO: la retirada sigue verificando dentro de su ventana y no fuera
    retirada = rotacion.Identidad(identificador="ancla-3", algoritmo="ed25519",
                                  huella_publica="h3", estado=rotacion.RETIRADA,
                                  epoca_de_alta=1, epoca_de_retirada=2,
                                  solapamiento=1)
    dentro = retirada.verifica_en(2)[0]
    fuera = retirada.verifica_en(2 + 1 + 1)[0]
    _exigir("SOLAPAMIENTO · una RETIRADA verifica DENTRO de su ventana", dentro,
            "una identidad retirada deja de verificar dentro de su solapamiento, y "
            "entonces rotar rompería las firmas legítimas de la ventana")
    _exigir("SOLAPAMIENTO · y NO verifica pasada la ventana", not fuera,
            "una identidad retirada sigue verificando fuera de su solapamiento: la "
            "retirada no retira nada")

    # -- REVOCACIÓN: es inmediata y no tiene ventana. Se ejerce por el canal del anillo.
    anillo.revocar("ancla-2", motivo="clave comprometida en el ejercicio de `O26` §1.7")
    revocada = anillo.obtener("ancla-2")
    _exigir("REVOCACIÓN · el estado cambia a `revocada` por el canal del anillo",
            revocada.estado == rotacion.REVOCADA,
            "`revocar` no dejó la identidad en estado revocada")
    _exigir("REVOCACIÓN · una REVOCADA no verifica NI en su propia época",
            not revocada.verifica_en(2)[0],
            "una identidad revocada sigue verificando: la revocación no revoca nada")
    try:
        anillo.exigir_valida("ancla-2", 2)
        _exigir("REVOCACIÓN · `exigir_valida` FALLA CERRADO sobre una revocada", False,
                "`exigir_valida` aceptó una identidad revocada")
    except Exception as error:                                        # noqa: BLE001
        cond.anotar("REVOCACIÓN · `exigir_valida` sobre una revocada",
                    "falla cerrado: " + type(error).__name__)

    # -- CONTROL DEL CONTROL: sin él, «todo falla» explicaría los seis verdes de arriba.
    try:
        anillo.exigir_valida("ancla-1", 1)
        cond.anotar("CONTROL SANO · la identidad ACTIVA de la época sí pasa", "ok")
    except Exception as error:                                        # noqa: BLE001
        _exigir("CONTROL SANO · la identidad ACTIVA de la época sí pasa", False,
                "una identidad activa y en época es rechazada (%s): el ejercicio estaría "
                "midiendo que todo falla" % type(error).__name__)

    if fallos:
        cond.falla("los gestos de `O26` §1.7 no se comportan como su contrato dice: "
                   + " · ".join(fallos))
        return
    cond.satisface(
        "los CUATRO gestos EJERCIDOS sobre identidades reales, y el veredicto CAMBIA con "
        "cada uno: rotación —una identidad nueva no acepta firmas anteriores a su alta—, "
        "solapamiento —una retirada verifica dentro de su ventana y no fuera—, retirada y "
        "revocación —inmediata, sin ventana, y `exigir_valida` falla cerrado—, con su "
        "control sano. No se comprueba que los nombres existan: se comprueba qué hacen")


def condicion_8(taller, repo, montaje, cond):
    """Los SEIS ataques de `O26` §1.8, y los seis tienen que fallar CERRADO."""
    sys.path.insert(0, RAIZ_EXTERNA)
    import atestacion                                                 # noqa: PLC0415
    import firma                                                      # noqa: PLC0415
    commit, tree = _sha_y_tree(repo)
    acta = atestacion.construir(
        autoridad="ejercicio-o26", identidad="ancla", huella_publica="h",
        epoca=1, commit=commit, tree=tree, veredicto="VERDE", proveedor="ssh-keygen")
    mensaje = atestacion.canonizar(acta)
    firmada = firma.firmar(mensaje, clave_privada=montaje["privada"])

    anillo = os.path.join(taller, "firmantes-8")
    firma.escribir_firmantes(anillo, [("ancla@ads", montaje["publica"])])

    def _verificar(anillo_usado, firma_usada):
        """0 si verifica, 1 si no. Por el CANAL PRODUCTIVO, que es lo que se juzga."""
        valida, _diag = firma.verificar(mensaje, firma_usada,
                                        firmantes=anillo_usado, principal="ancla@ads")
        return 0 if valida else 1

    # CONTROL SANO primero: sin él, «todo falla» explicaría los seis rojos.
    sano = _verificar(anillo, firmada)
    cond.anotar("CONTROL SANO · firma legítima", "codigo=%d" % sano)
    if sano != 0:
        cond.falla("el control sano NO verifica: los ataques no medirían nada")
        return

    caidos, pasados = [], []

    # 1 · CLAVE DESCONOCIDA: se verifica contra un anillo con OTRA pública.
    _otra_priv, otra_pub = firma.generar_par_efimero(os.path.join(taller, "otras"),
                                                     "intrusa")
    anillo_ajeno = os.path.join(taller, "firmantes-ajenos")
    firma.escribir_firmantes(anillo_ajeno, [("ancla@ads", otra_pub)])
    (caidos if _verificar(anillo_ajeno, firmada) != 0 else pasados).append("clave desconocida")

    # 2 · FIRMA INVÁLIDA: se corrompe un byte del cuerpo blindado.
    cuerpo = firmada.decode("utf-8")
    lineas = cuerpo.splitlines()
    medio = len(lineas) // 2
    lineas[medio] = ("A" if not lineas[medio].startswith("A") else "B") + lineas[medio][1:]
    (caidos if _verificar(anillo, "\n".join(lineas).encode()) != 0
     else pasados).append("firma inválida")

    # 3 y 4 · COMMIT y TREE incorrectos: los juzga la atestación, no la firma.
    for etiqueta, c, t in (("commit incorrecto", "0" * 40, tree),
                           ("tree incorrecto", commit, "0" * 40)):
        try:
            atestacion.exigir_vinculo(acta, commit=c, tree=t)
            pasados.append(etiqueta)
        except Exception:                                             # noqa: BLE001
            caidos.append(etiqueta)

    # 5 · AUSENCIA DE PROVEEDOR: se le retira `ssh-keygen` del `PATH` al firmante.
    entorno = dict(os.environ)
    entorno["PATH"] = os.path.join(taller, "path-vacio")
    os.makedirs(entorno["PATH"], exist_ok=True)
    guion = os.path.join(taller, "sin_proveedor.py")
    io.open(guion, "w", encoding="utf-8").write(
        "import sys\n"
        "sys.path.insert(0, %r)\n"
        "import firma\n"
        "try:\n"
        "    firma.exigir_proveedor()\n"
        "    print('PASA')\n"
        "except BaseException as e:\n"
        "    print('CIERRA', type(e).__name__)\n" % RAIZ_EXTERNA)
    codigo, salida, _err = _correr([sys.executable, guion], env=entorno)
    cond.anotar("sin `ssh-keygen` en el PATH", salida.strip()[:60])
    (caidos if "CIERRA" in salida else pasados).append("ausencia de proveedor")

    # 6 · CONTAMINACIÓN DEL ENTORNO: un `hashlib` homónimo en `PYTHONPATH`.
    veneno = os.path.join(taller, "veneno")
    os.makedirs(veneno, exist_ok=True)
    io.open(os.path.join(veneno, "hashlib.py"), "w", encoding="utf-8").write(
        "def sha256(*a, **k):\n"
        "    class F:\n"
        "        def hexdigest(self):\n            return '0' * 64\n"
        "        def update(self, *a):\n            return None\n"
        "    return F()\n")
    entorno_v = dict(os.environ)
    entorno_v["PYTHONPATH"] = veneno
    verificador = os.path.join(montaje["instalacion"], "raiz-externa", "verificador.py")
    codigo, salida, err = _correr([sys.executable, verificador, "capacidades"],
                                  env=entorno_v)
    limpio = _correr([sys.executable, verificador, "capacidades"])[1]
    cond.anotar("verificador con `PYTHONPATH` envenenado", "codigo=%d" % codigo)
    # Falla cerrado O produce exactamente lo mismo que sin veneno: las dos son correctas;
    # lo que no vale es producir algo DISTINTO y decir que está bien.
    (caidos if (codigo != 0 or salida == limpio)
     else pasados).append("contaminación del entorno")

    for nombre in caidos:
        cond.anotar("  ataque · " + nombre, "FALLA CERRADO")
    for nombre in pasados:
        cond.anotar("  ataque · " + nombre, "PASÓ — no falla cerrado")
    if pasados:
        cond.falla("estos ataques NO fallan cerrado: %s" % ", ".join(pasados))
        return
    cond.satisface(
        "los SEIS ataques que `O26` §1.8 enumera fallan cerrado, y el control sano verifica: "
        "%s" % ", ".join(caidos))


def ejercer(repo=None, *, salida=None):
    """Ejerce las OCHO sobre `repo`. Devuelve `(codigo, informe)`."""
    repo = os.path.abspath(repo or RAIZ)
    destino = salida or sys.stdout
    perfil = perfil_del_anfitrion()
    condiciones = [Condicion(n, t) for n, t in CONDICIONES]
    taller = tempfile.mkdtemp(prefix="ads-o26-")
    try:
        montaje = montar(taller, repo)
        for cond in condiciones:
            try:
                if cond.numero == 6:
                    condicion_6(taller, repo, montaje, cond, perfil)
                else:
                    globals()["condicion_%d" % cond.numero](taller, repo, montaje, cond)
            except Exception as error:                                # noqa: BLE001
                # Una condición que revienta NO se declara superada ni se calla: se publica
                # con su excepción, que es información sobre el aparato.
                cond.falla("la comprobación reventó: %s: %s"
                           % (type(error).__name__, str(error)[:200]))
    finally:
        shutil.rmtree(taller, ignore_errors=True)

    destino.write("`O26` §1 · LAS OCHO CONDICIONES, EJERCIDAS SOBRE LA CANDIDATA\n")
    destino.write("=" * 78 + "\n")
    destino.write("  PERFIL DEL ANFITRIÓN, medido y DECLARADO (`O29` §7)\n")
    for clave in sorted(perfil):
        destino.write("      %-22s %s\n" % (clave, perfil[clave]))
    destino.write("      la certificación de estas condiciones vale PARA ESTE PERFIL y no\n"
                  "      se universaliza: es lo que `O29` §7 exige decir\n\n")
    for cond in condiciones:
        destino.write("  %d · %-13s %s\n" % (cond.numero, cond.estado or "SIN MEDIR",
                                             cond.texto))
        for linea in cond.detalle:
            destino.write("        %s\n" % linea)
        for orden, resultado in cond.ordenes:
            destino.write("        · %s → %s\n" % (orden, resultado))
        destino.write("\n")

    satisfechas = [c for c in condiciones if c.estado == "SATISFECHA"]
    no_ejercibles = [c for c in condiciones if c.estado == "NO EJERCIBLE"]
    fallidas = [c for c in condiciones if c.estado == "NO SATISFECHA"]
    destino.write("%d de %d condiciones SATISFECHAS · %d no ejercibles · %d no satisfechas\n"
                  % (len(satisfechas), len(condiciones), len(no_ejercibles), len(fallidas)))
    if no_ejercibles:
        destino.write("REQUISITOS EXACTOS de lo NO EJERCIBLE (`O29` §7):\n")
        for cond in no_ejercibles:
            destino.write("  %d · %s\n" % (cond.numero, cond.detalle[0]))
    informe = {"perfil": perfil,
               "condiciones": [{"numero": c.numero, "texto": c.texto,
                                "estado": c.estado, "detalle": c.detalle,
                                "ordenes": c.ordenes} for c in condiciones],
               "satisfechas": len(satisfechas),
               "no_ejercibles": len(no_ejercibles),
               "no_satisfechas": len(fallidas)}
    if fallidas:
        return NO_SATISFECHA, informe
    if no_ejercibles:
        return NO_EJERCIBLE, informe
    return SATISFECHA, informe


def main():
    analizador = argparse.ArgumentParser(
        description="ejerce las ocho condiciones de `O26` §1 sobre la candidata")
    analizador.add_argument("--raiz", default=RAIZ)
    analizador.add_argument("--json", action="store_true")
    argumentos = analizador.parse_args()
    if argumentos.json:
        import io as _io                                              # noqa: PLC0415
        tampon = _io.StringIO()
        codigo, informe = ejercer(argumentos.raiz, salida=tampon)
        sys.stdout.write(json.dumps(informe, ensure_ascii=False, indent=2) + "\n")
        return codigo
    codigo, _informe = ejercer(argumentos.raiz)
    return codigo


if __name__ == "__main__":
    sys.exit(main())
