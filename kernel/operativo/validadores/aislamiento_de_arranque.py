"""aislamiento_de_arranque — `G-03`: el aislamiento se decide ANTES de arrancar Python.

POR QUÉ EXISTE ESTE FICHERO, Y QUÉ AGUJERO CIERRA. Todo el aparato llevaba desde `E-10` un
prólogo que purgaba `sys.path` en la primera sentencia del módulo. El gate del 2026-09-05 lo
midió y lo tumbó en cuatro órdenes:

    $ cat veneno/sitecustomize.py
      import hashlib; hashlib.sha256 = lambda *a, **k: _Falso()
    $ PYTHONPATH=veneno python3.12 kernel/operativo/validadores/huella.py
      0000000000000000                      ← la huella FORJADA sobre un árbol mutado
    $ PYTHONPATH=veneno python3.12 kernel/operativo/validadores/comprobar_integridad.py
      T150  SUPERADA · EXIT=0               ← VERDE sobre un árbol MUTADO

La causa no es que el prólogo esté mal escrito: es que **llega tarde por construcción**.
`site.py` importa `sitecustomize` durante la inicialización del intérprete, **antes de que la
primera línea de cualquier módulo se ejecute**. Una purga escrita en Python no puede
adelantarse a algo que ocurre mientras Python arranca. Y el control del control que había
—mirar la procedencia de `os`— no ve la sustitución de `hashlib.sha256`, porque el módulo es
el bueno y lo que cambió es un atributo suyo.

    LO QUE NO LO CIERRA, y se dice porque es la tentación barata
    Comprobar más atributos: cierra la instancia y deja la clase. El atacante muta otro. Es
    exactamente el patrón que este expediente lleva cinco gates persiguiendo —se cierra la
    instancia, la clase aguanta— y aquí se rompe de raíz.

    LO QUE SÍ LO CIERRA
    Que el intérprete arranque con `-I -S -E`: sin `site`, sin variables de entorno y sin el
    directorio del script en la ruta. Entonces `sitecustomize` **no se importa nunca**, y no
    hay atributo que mutar porque el gancho no llega a ejecutarse. Medido las dos veces.

DECISIÓN · dos piezas, y ninguna sola basta
    (1) un LANZADOR que reejecuta el punto con el intérprete aislado, y
    (2) una GUARDA que cada punto comprueba al entrar y que FALLA CERRADO si no se cumple.
    Con sólo (1), invocar el script directamente esquiva el lanzador. Con sólo (2), el punto
    sabe que está contaminado pero ya se ha ejecutado `sitecustomize`. Juntas, la ejecución
    directa se reejecuta a sí misma aislada y la que no puede, no corre.

DECISIÓN · el lanzador REEJECUTA en vez de negarse
    Alternativas: (a) fallar y pedir al usuario que invoque con `-I -S -E`; (b) reejecutar.
    Se elige (b). Con (a) el aislamiento depende de que quien invoca se acuerde, que es la
    misma clase de garantía que acaba de fallar. Con (b) la vía correcta es la única vía: se
    reejecuta UNA sola vez —lo marca la opción `-X ads_aislado=1`— y si tras reejecutar sigue
    aislado, se falla cerrado en vez de entrar en bucle.

DECISIÓN · el entorno del hijo se construye, no se hereda
    Se conservan sólo las variables que el aparato necesita y declara. `PYTHONPATH`,
    `PYTHONSTARTUP`, `PYTHONHOME` y las demás de su familia **no pasan**: `-E` ya las
    ignoraría, y además se retiran para que no lleguen a los NIETOS que el punto lance.
"""
from __future__ import annotations

import os as _os
import sys as _sys

CODIGO_DE_PROCEDENCIA = 5

# Lo único que sobrevive del entorno del lanzador. Todo lo demás se retira, y en particular
# la familia `PYTHON*`, que es por donde entra el gancho.
VARIABLES_CONSERVADAS = (
    "PATH", "HOME", "LANG", "LC_ALL", "LC_CTYPE", "TZ", "TMPDIR", "USER", "LOGNAME",
    "XDG_RUNTIME_DIR",
)

# DECISIÓN · lo del APARATO se conserva POR PREFIJO, y no por lista escrita
#     La primera versión de esta lista enumeraba cuatro `ADS_*`. Se midió al aplicar la
#     guarda a las 21 baterías: `ADS_ADAPTADOR_FALLO` y `ADS_RAIZ_EXTERNA_HOME` no estaban,
#     y las pruebas que los usan habrían pasado a medir un anfitrión sin la variable —verde
#     por la razón equivocada—. Alternativas: (a) alargar la lista con las dos que faltan;
#     (b) conservar el PREFIJO entero del aparato.
#     Se elige (b). Con (a) la lista se queda corta la próxima vez que el aparato declare
#     una variable, que es el mismo modo de fallo que `ADJ-B2` persigue en los inventarios.
#     Con (b) el criterio es derivable y lo que NO pasa sigue siendo lo peligroso: la
#     familia `PYTHON*`, que es por donde entra el gancho, no lleva el prefijo del aparato.
PREFIJO_DEL_APARATO = "ADS_"

# DECISIÓN · la marca de «ya me he reejecutado» va en `-X`, y NO en el entorno
#     Era `ADS_AISLADO=1` en el entorno, y se midió el fallo: cualquiera que ponga esa
#     variable —incluido un abuelo que la heredó— hace que un punto NO aislado crea que ya
#     se reejecutó y falle cerrado sin haberlo intentado. Es una denegación de servicio
#     regalada, y peor: la señal que rompe el bucle la controlaba justo quien ataca.
#     Alternativas: (a) el entorno; (b) un argumento más en `argv`; (c) una opción `-X`.
#     Se elige (c). Con (a) la señal es forjable y hereda. Con (b) se altera el `argv` que
#     el programa lee, que es suyo. Con (c) la señal SÓLO puede venir de la línea de
#     órdenes del propio proceso —`-X` no se lee del entorno, y `-E` lo garantiza—, no la
#     heredan los hijos, y se ve en `sys._xoptions`.
MARCA_DE_REEJECUCION = "ads_aislado"


def ya_se_reejecuto():
    """`True` si ESTE proceso es el resultado de la reejecución aislada, y no otra cosa."""
    return MARCA_DE_REEJECUCION in getattr(_sys, "_xoptions", {})


# `-E` IGNORA LA FAMILIA `PYTHON*`, Y ESO BORRA DECISIONES QUE NO SON DEL ATACANTE
#
#  HECHO REPRODUCIDO al aplicar esta guarda, y es de los caros de ver.
#  `test_agentes.py::T235` sabotea una COPIA del árbol cambiando `min(` por `max(` en
#  `ciclo/agentes.py` —MISMO número de bytes— y exige que la prueba se ponga roja. Se
#  defiende del `.pyc` obsoleto poniendo `PYTHONDONTWRITEBYTECODE=1` en el entorno de sus
#  hijos, porque un `.pyc` cacheado del control positivo con el MISMO tamaño y el MISMO
#  segundo de `mtime` se considera válido y el sabotaje no llega a compilarse.
#  Con `-E` y el entorno construido, esa variable desaparecía dos veces —ni `-E` la lee ni
#  el entorno saneado la pasa—, el hijo cacheaba, y el sabotaje salía VERDE:
#
#      SABOTAJE SIN ROJO · el techo de coste del agente combinado deja de ser el MENOR ·
#      la prueba `LoQueLaAuditoriaEncontro.test_13…` siguió pasando con la regla borrada
#
#  DECISIÓN · lo que `-E` desactiva y tiene equivalente en la línea de órdenes, se TRADUCE
#      Alternativas: (a) conservar `PYTHONDONTWRITEBYTECODE` en el entorno del hijo;
#      (b) añadir `-B` siempre; (c) traducir la variable a su bandera y propagar la
#      intención con una variable del aparato.
#      Se elige (c). Con (a) no serviría —`-E` la ignora igual— y además reabriría la
#      familia `PYTHON*`, que es por donde entra el gancho. Con (b) se paga recompilar en
#      cada corrida de cada punto, y el `.pyc` no es un problema: lo es que una decisión
#      del llamante desaparezca en silencio. Con (c) la intención sobrevive, viaja a los
#      nietos por el prefijo `ADS_` y se ve en la orden publicada.
VARIABLE_SIN_BYTECODE = "ADS_SIN_BYTECODE"


def _sin_bytecode():
    return bool(_os.environ.get("PYTHONDONTWRITEBYTECODE")
                or _os.environ.get(VARIABLE_SIN_BYTECODE))


def entorno_saneado(extra=None):
    """El entorno MÍNIMO con el que se arranca el intérprete aislado.

    `extra` lo usa el RUNNER que lanza hijos —`registrar_evidencia.py`— para añadir lo que
    el hijo necesite sin heredar nada más. Devolver un diccionario NUEVO cada vez es
    deliberado: un llamante que mutara el resultado no puede contaminar al siguiente.
    """
    limpio = {clave: valor for clave, valor in _os.environ.items()
              if clave in VARIABLES_CONSERVADAS or clave.startswith(PREFIJO_DEL_APARATO)}
    if _sin_bytecode():
        limpio[VARIABLE_SIN_BYTECODE] = "1"
    if extra:
        limpio.update(extra)
    return limpio


# Las banderas con las que se arranca el intérprete aislado, en UN solo sitio: el lanzador
# de `exigir` y el runner de la evidencia tienen que pedir lo MISMO, y dos listas separadas
# derivan —y la que miente es siempre la que nadie mira—.
BANDERAS_DE_AISLAMIENTO = ("-I", "-S", "-E")


def orden_aislada(guion, argumentos=()):
    """La orden con la que se invoca un punto ejecutable por la vía oficial."""
    banderas = list(BANDERAS_DE_AISLAMIENTO)
    if _sin_bytecode():
        banderas.append("-B")
    return [_sys.executable] + banderas \
        + ["-X", MARCA_DE_REEJECUCION + "=1", guion] + [str(a) for a in argumentos]


def flags_de_aislamiento():
    """Lo que el intérprete dice de sí mismo. `safe_path` sólo existe desde 3.11."""
    return {
        "isolated": bool(_sys.flags.isolated),
        "no_site": bool(_sys.flags.no_site),
        "ignore_environment": bool(_sys.flags.ignore_environment),
        "safe_path": bool(getattr(_sys.flags, "safe_path", False)),
    }


def esta_aislado():
    """Las CUATRO banderas, y `safe_path` sólo se exige donde el intérprete la tiene.

    DECISIÓN · `safe_path` se exige CUANDO EXISTE, y no se da por implicada
        `-I` implica `-P` desde 3.11, de modo que comprobarla parece redundante. No lo es:
        lo que se comprueba es lo que el intérprete DICE de sí mismo, y si un día `-I`
        dejara de implicarla —o alguien arrancara con `-S -E` sin `-I`— el directorio del
        guion volvería a `sys.path[0]` y el homónimo entraría por ahí. Donde el atributo no
        existe (3.10 y anteriores) no se puede exigir lo que no se puede medir, y por eso
        `informe()` publica `safe_path_medible` para que la ausencia se vea.
    """
    banderas = flags_de_aislamiento()
    if not (banderas["isolated"] and banderas["no_site"]
            and banderas["ignore_environment"]):
        return False
    if hasattr(_sys.flags, "safe_path"):
        return banderas["safe_path"]
    return True


def _primitivas_intactas():
    """CONTROL DE LA PRIMITIVA · el vector conocido que caza el gancho en sitio.

    `-I -S -E` impide que `sitecustomize` llegue a ejecutarse, y con eso basta para el ataque
    medido. Esta comprobación es la SEGUNDA línea, y existe por una razón concreta: cubre la
    mutación que ocurra por cualquier otra vía —un `.pth`, una instalación alterada, un
    módulo del propio árbol manipulado—. Se comprueba lo que el aparato USA para decidir:
    el digest con el que se firma la huella y la evidencia.
    """
    import hashlib                                                   # noqa: PLC0415
    esperado = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    return hashlib.sha256(b"hello").hexdigest() == esperado


# ── LA PROCEDENCIA DEL CÓDIGO Y LA INSTALACIÓN AUTORIZADA ────────────────────────────
#
#  `G-03` no pide sólo las cuatro banderas: pide que el punto compruebe al entrar «la
#  procedencia del código» y «el repositorio o instalación autorizados». Las banderas dicen
#  cómo arrancó el intérprete; no dicen de QUÉ ÁRBOL salió lo que se está ejecutando.
#
#  DECISIÓN · la instalación autorizada la define la SEDE DE LA GUARDA, no una ruta escrita
#      Alternativas: (a) una constante con la raíz del repositorio; (b) una variable de
#      entorno que la declare; (c) derivarla de la ubicación de ESTE fichero.
#      Se elige (c). Con (a) el árbol no se puede materializar en otro sitio —y
#      `tooling/workspace.py` existe justamente para eso—. Con (b) el atacante que controla
#      el entorno controla también la autorización, que es el agujero que se está cerrando.
#      Con (c) la relación es la única que no se puede falsificar sin tocar el disco: el
#      punto se autoriza contra el árbol QUE LE DIO LA GUARDA. Un punto de otro árbol que se
#      lance con esta guarda cae; y un árbol B lanzado desde un árbol A usa la guarda de B,
#      porque el prólogo la busca subiendo desde `__file__` y no desde el `cwd`.
#
#  DECISIÓN · la raíz se deriva de DÓNDE VIVE ESTE FICHERO, y admite las dos formas
#      Este módulo vive en dos sitios por construcción: en el árbol, bajo
#      `kernel/operativo/validadores/`; y DENTRO de una instalación de la raíz externa, que
#      `instalar.py` deja fuera del árbol y que no tiene ese camino. Medido: sin esta
#      distinción, la raíz externa instalada calculaba una raíz dos niveles por encima del
#      destino —el abuelo del directorio de instalación— y la comprobación dejaba de decir
#      nada. Alternativas: (a) una sola forma y que la instalación se apañe; (b) las dos
#      formas, cada una derivada del propio camino del fichero.
#      Se elige (b): en el árbol, la raíz es la del repositorio; en una instalación, es el
#      directorio que CONTIENE el paquete —`raiz-externa/` y `runtime/` cuelgan de él—.
_SEDE_EN_EL_ARBOL = _os.path.join("kernel", "operativo", "validadores")
_AQUI = _os.path.dirname(_os.path.realpath(__file__))
if _AQUI.endswith(_os.sep + _SEDE_EN_EL_ARBOL):
    RAIZ_AUTORIZADA = _AQUI[:-len(_os.sep + _SEDE_EN_EL_ARBOL)]
else:
    RAIZ_AUTORIZADA = _os.path.dirname(_AQUI)

#  La ruta de importación TAL Y COMO LA DEJÓ EL INTÉRPRETE. Se captura al importar este
#  módulo, que en un punto aislado es lo primero que se importa después de la biblioteca
#  estándar: bajo `-I -S -E` nada de fuera ha podido tocarla todavía. Es la referencia
#  contra la que se juzga la procedencia de todo lo demás.
RUTA_DE_ARRANQUE = tuple(sorted({_os.path.realpath(entrada)
                                 for entrada in _sys.path if entrada}))


def _dentro_de(camino, raiz):
    return camino == raiz or camino.startswith(raiz + _os.sep)


def _interprete_verificado():
    """El intérprete que corre, comprobado contra sí mismo. Devuelve `(bool, motivo)`.

    Cierra el ataque del `PATH` con un intérprete falso. Lo que se puede comprobar sin
    creerse nada del entorno: que `sys.executable` es un fichero REAL, que vive dentro del
    prefijo que él mismo declara, que la biblioteca estándar sale de ese mismo prefijo, y
    que la implementación es la que el aparato declara soportar.

    LO QUE ESTA COMPROBACIÓN NO HACE, y se escribe para que nadie lo suponga: no distingue
    un CPython 3.12 legítimo de OTRO CPython 3.12 legítimo puesto antes en el `PATH`. Eso lo
    cierra la vía oficial, que invoca por RUTA ABSOLUTA, y lo caza `_primitivas_intactas`
    si el intérprete sustituido miente sobre el digest.
    """
    ejecutable = _sys.executable
    if not ejecutable or not _os.path.isfile(ejecutable):
        return False, "`sys.executable` no resuelve a un fichero: %r" % (ejecutable,)
    base = _os.path.realpath(_sys.base_prefix)
    if not _dentro_de(_os.path.realpath(ejecutable), base):
        return False, ("el intérprete %r no vive dentro del prefijo que declara (%r)"
                       % (_os.path.realpath(ejecutable), base))
    origen_de_os = _os.path.realpath(_os.__file__ or "")
    if not _dentro_de(origen_de_os, base):
        return False, ("la biblioteca estándar (%r) no sale del prefijo del intérprete (%r)"
                       % (origen_de_os, base))
    if _sys.implementation.name != "cpython":
        return False, "la implementación es %r y el aparato declara CPython" \
            % (_sys.implementation.name,)
    return True, ""


def modulos_de_procedencia_ajena(terceros=None):
    """Los módulos YA CARGADOS que no salen ni del intérprete ni del árbol autorizado.

    Cierra el ataque del «import previo a la purga»: cualquier cosa que se haya colado en
    `sys.modules` antes de que este punto tomara la palabra —`sitecustomize`,
    `usercustomize`, un homónimo del `PYTHONPATH`, un `.pth`— tiene un `__file__` que NO
    cae en ninguna de las procedencias admitidas, y aquí se ve por su nombre y su ruta.
    """
    admitidas = [_os.path.realpath(_sys.base_prefix), _os.path.realpath(_sys.prefix),
                 RAIZ_AUTORIZADA]
    admitidas.extend(RUTA_DE_ARRANQUE)
    if terceros:
        admitidas.append(terceros)
    ajenos = []
    for nombre, modulo in sorted(_sys.modules.items()):
        origen = getattr(modulo, "__file__", None)
        if not origen:
            continue                     # incorporado o congelado: no tiene procedencia
        real = _os.path.realpath(origen)
        if not any(_dentro_de(real, raiz) for raiz in admitidas):
            ajenos.append((nombre, real))
    return ajenos


def _salir(nombre_del_punto, causa):
    _sys.stderr.write("[PROCEDENCIA_NO_FIABLE] %s. `%s` NO ejecuta\n"
                      % (causa, nombre_del_punto))
    raise SystemExit(CODIGO_DE_PROCEDENCIA)


def exigir(nombre_del_punto, nombre_del_modulo="__main__"):
    """Se llama al ENTRAR en un punto ejecutable. Reejecuta aislado, o falla cerrado.

    Devuelve el informe de procedencia cuando todo está en regla. No devuelve nunca sobre un
    intérprete contaminado: o reejecuta, o sale.
    """
    punto = _os.path.realpath(nombre_del_punto)

    # UN MÓDULO IMPORTADO NO ES UN PUNTO DE EJECUCIÓN, y no se reejecuta.
    #
    # DECISIÓN · la guarda distingue «me han ejecutado» de «me han importado»
    #     Medido: `test_integridad_y_evidencia.py` importa `comprobar_evidencia` y
    #     `comprobar_contratos`, y `kernel-status.sh` importa `huella`. Si la guarda
    #     reejecutara al importar, un `import` inocente sustituiría el proceso del
    #     importador por otro con SUS argumentos, que es un daño peor que el que cierra.
    #     Alternativas: (a) reejecutar siempre; (b) no hacer nada al importar; (c) no
    #     reejecutar, pero seguir comprobando lo que sí es comprobable.
    #     Se elige (c). Con (a) se rompe el aparato. Con (b) un módulo importado desde un
    #     proceso envenenado no diría nada. Con (c) el importador —que es a su vez un punto
    #     ejecutable inventariado, y por tanto lleva esta misma guarda— ya está aislado, y
    #     si NO lo está, la primitiva y la procedencia se comprueban igual y fallan cerrado.
    if nombre_del_modulo != "__main__":
        if not _primitivas_intactas():
            _salir(nombre_del_punto,
                   "`hashlib.sha256` no produce el digest conocido de un vector fijo: la "
                   "primitiva con la que este aparato firma su evidencia está sustituida")
        return {"aislado": esta_aislado(), "importado": True,
                "flags": flags_de_aislamiento(), "interprete": _sys.executable,
                "biblioteca_de_terceros": None, "punto": punto}

    if esta_aislado():
        if not _primitivas_intactas():
            _salir(nombre_del_punto,
                   "`hashlib.sha256` no produce el digest conocido de un vector fijo: la "
                   "primitiva con la que este aparato firma su evidencia está sustituida")
        correcto, motivo = _interprete_verificado()
        if not correcto:
            _salir(nombre_del_punto, "el INTÉRPRETE no se verifica contra sí mismo: " + motivo)
        # EL REPOSITORIO O INSTALACIÓN AUTORIZADOS: el punto tiene que pertenecer al árbol
        # que le dio la guarda. Un punto de otro árbol, o una instalación a medio copiar en
        # la que el punto y la guarda ya no son del mismo sitio, cae aquí.
        if not _dentro_de(punto, RAIZ_AUTORIZADA):
            _salir(nombre_del_punto,
                   "el punto ejecutable %r no pertenece a la instalación que le da la "
                   "guarda (%r): son dos árboles distintos" % (punto, RAIZ_AUTORIZADA))
        # LA MARCA NO VIAJA A LOS NIETOS, y por eso vive en `-X` y no en el entorno.
        # Medido al aplicar la guarda a las baterías: con la marca en el entorno, una
        # batería aislada lanzaba `ads_estado.py` con una copia de su propio entorno, el
        # nieto heredaba la marca sin estar aislado, creía haberse reejecutado ya y fallaba
        # cerrado —98 fallos en `test_estado_durable.py`—.
        reejecutado = ya_se_reejecuto()
        terceros = habilitar_biblioteca_de_terceros()
        ajenos = modulos_de_procedencia_ajena(terceros)
        if ajenos:
            _salir(nombre_del_punto,
                   "hay módulos cargados de procedencia ajena al intérprete y al árbol "
                   "autorizado: " + ", ".join("%s <- %s" % par for par in ajenos))
        return {"aislado": True, "importado": False,
                "reejecutado": reejecutado,
                "flags": flags_de_aislamiento(),
                "interprete": _sys.executable,
                "raiz_autorizada": RAIZ_AUTORIZADA,
                "biblioteca_de_terceros": terceros,
                "punto": punto}

    # No está aislado. Si YA se reejecutó, algo impide el aislamiento y no se sigue: entrar
    # en bucle sería peor que parar, y seguir contaminado es lo que este fichero existe para
    # impedir.
    if ya_se_reejecuto():
        _salir(nombre_del_punto,
               "se reejecutó con `%s` y el intérprete sigue sin declarar aislamiento (%r)"
               % (" ".join(BANDERAS_DE_AISLAMIENTO), flags_de_aislamiento()))

    guion = _os.path.realpath(_sys.argv[0] or nombre_del_punto)
    if not _os.path.isfile(guion):
        _salir(nombre_del_punto,
               "no se puede resolver por ruta absoluta el punto ejecutable, luego no se "
               "puede reejecutar aislado")

    # SE REEJECUTA EL FICHERO DEL PUNTO, no lo que diga `argv[0]`, cuando los dos no son el
    # mismo fichero. `argv[0]` lo escribe quien lanza; `__file__` lo resuelve el importador
    # a partir de dónde está el módulo de verdad.
    if guion != punto and _os.path.isfile(punto):
        guion = punto
    orden = orden_aislada(guion, _sys.argv[1:])
    _os.execve(orden[0], orden, entorno_saneado())      # no vuelve


# ── LA BIBLIOTECA DE TERCEROS, BAJO AISLAMIENTO ──────────────────────────────────────
#
#  `-S` desactiva `site`, y con él desaparece `site-packages`: PyYAML deja de importarse y
#  media docena de validadores no arrancan. La tentación es retirar `-S` y quedarse con
#  `-I -E`, que ya ignora `PYTHONPATH`; pero entonces un `sitecustomize` INSTALADO en
#  `site-packages` seguiría ejecutándose, y el agujero quedaría abierto por el otro lado.
#
#  DECISIÓN · se conserva `-S` y se reintroduce `site-packages` por RUTA ABSOLUTA, DESPUÉS
#      Alternativas: (a) retirar `-S`; (b) vendorizar PyYAML; (c) añadir el directorio a
#      mano tras el arranque.
#      Se elige (c). Con (a) el aislamiento tiene una puerta declarada. Con (b) el árbol
#      carga una copia de una biblioteca mantenida, que `O25` §5 desaconseja para la
#      criptografía y que aquí sería peor: dos PyYAML derivando. Con (c) `site.py` NO corre
#      —luego `sitecustomize` y `usercustomize` no se importan NUNCA— y el paquete se resuelve
#      por una ruta que se comprueba: tiene que existir, ser directorio, y estar DENTRO del
#      prefijo del intérprete que está ejecutando. Un `site-packages` de otra instalación no
#      entra.
def habilitar_biblioteca_de_terceros():
    """Añade el `site-packages` del intérprete EN CURSO, comprobado. Devuelve la ruta o `None`."""
    if not _sys.flags.no_site:
        return None                     # `site` ya corrió: no hay nada que reintroducir
    prefijo = _os.path.realpath(_sys.prefix)
    version = "python%d.%d" % _sys.version_info[:2]
    for relativa in (("lib", version, "site-packages"),
                     ("lib", "site-packages"),
                     ("Lib", "site-packages")):
        candidata = _os.path.realpath(_os.path.join(prefijo, *relativa))
        if not _os.path.isdir(candidata):
            continue
        # La ruta tiene que caer DENTRO del prefijo del intérprete en curso. Un
        # `site-packages` ajeno es exactamente el vector que `-S` acaba de cerrar.
        if _os.path.commonpath([prefijo, candidata]) != prefijo:
            continue
        if candidata not in _sys.path:
            _sys.path.append(candidata)
        return candidata
    return None


def informe(nombre_del_punto):
    """La procedencia, para publicarla. No decide nada: `exigir` ya decidió."""
    correcto, motivo = _interprete_verificado()
    datos = flags_de_aislamiento()
    datos.update({"interprete": _sys.executable,
                  "interprete_verificado": correcto,
                  "interprete_motivo": motivo,
                  "safe_path_medible": hasattr(_sys.flags, "safe_path"),
                  "punto": _os.path.realpath(nombre_del_punto),
                  "raiz_autorizada": RAIZ_AUTORIZADA,
                  "primitiva_intacta": _primitivas_intactas(),
                  "modulos_ajenos": [nombre for nombre, _ in modulos_de_procedencia_ajena()],
                  "reejecutado": ya_se_reejecuto()})
    return datos


# ── LA GARANTÍA SE PUBLICA · `D-01` ──────────────────────────────────────────────────
#
#  El revisor 3 lo escribió con estas palabras: «o el prólogo entra en las baterías, o el
#  runner sanea el entorno de sus hijos **y lo publica en la cabecera de cada evidencia**».
#  Una garantía que no se publica no la puede comprobar nadie: quien lee una evidencia no
#  puede saber si el hijo que la produjo corrió con el entorno del anfitrión o con uno
#  construido, y esa diferencia es exactamente la que `HALLAZGO 3` midió.
#
#  DECISIÓN · la línea la escribe el LANZADOR y dice lo que hizo, no lo que quería hacer
#      Alternativas: (a) una línea fija «entorno saneado»; (b) derivarla de lo que se pasó
#      de verdad al hijo.
#      Se elige (b). Con (a) la cabecera seguiría diciendo «saneado» el día que alguien
#      quitara el `env=`, que es precisamente el defecto. Con (b) la línea enumera las
#      banderas y las variables REALMENTE entregadas: si el saneamiento desaparece, la
#      cabecera cambia y `comprobar_evidencia` lo ve.
def banderas_de(orden):
    """Lo que va entre el intérprete y el guion: las banderas con las que se arrancó.

    Se corta en el primer `.py` y no se filtra por el guion inicial: `-X ads_aislado=1` es
    DOS elementos y el segundo no empieza por guion, de modo que quedarse con «los que
    empiezan por `-`» publicaría un `-X` suelto y sin valor. La cabecera tiene que decir la
    orden que se ejecutó, no una versión suya.
    """
    banderas = []
    for elemento in orden[1:]:
        if elemento.endswith(".py"):
            break
        banderas.append(elemento)
    return banderas


def linea_de_aislamiento_del_hijo(orden, entorno):
    """La línea de cabecera que declara con qué aislamiento se lanzó un hijo."""
    banderas = banderas_de(orden)
    retiradas = sorted(clave for clave in _os.environ
                       if clave not in entorno and clave.startswith("PYTHON"))
    return ("banderas %s · entorno CONSTRUIDO con %d variables (%s) · retiradas del "
            "lanzador: %s" % (" ".join(banderas) or "(ninguna)", len(entorno),
                              " ".join(sorted(entorno)),
                              " ".join(retiradas) or "ninguna de la familia PYTHON*"))
