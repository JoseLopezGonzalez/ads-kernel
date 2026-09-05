#!/usr/bin/env python3
"""negativos_contratos19 — infracciones deliberadas de la corrección del 2026-09-04.

POR QUÉ ESTE FICHERO EXISTE, Y NO UNA LÍNEA MÁS EN `comprobar_negativos.py`. La corrección
de los hallazgos `E-01`…`E-16` se reparte en tres ejes disjuntos que se escriben en
paralelo. Tres ejes escribiendo sobre la MISMA lista producen una integración que nadie
puede revisar por partes, y la lista de sabotajes es justamente lo que no puede quedar sin
revisar. Cada eje escribe el suyo AQUÍ, y `comprobar_negativos.py` los INCORPORA por
nombre, sin descubrimiento y sin `try/except ImportError`: si uno falta, el validador
revienta al importar, que es exactamente lo que tiene que pasar. El catálogo sigue siendo
UNO y la sede de ejecución sigue siendo UNA.

Cada entrada es una `comprobar_negativos.Mutacion`. Se construyen aquí y se comprueban
allí.

QUÉ CUBRE ESTE EJE. Las CUATRO obligaciones de fase `F6` de `11-ARQ` §19, una a una y sin
absorberlas bajo un identificador común:

  CONTRATO 1    `N270`, `N270b`, `N270c`   la cobertura del censo DERIVA
  CONTRATO 1bis `N271`                     los perfiles de agente se cuentan
  CONTRATO 2    `N272`, `N272b`            el alcance de `T152` DERIVA
  `D104`        `N273`…`N273f`, `N275`,    el catálogo de `<CAP>:revision`, su herencia,
                `N276`                     su posición, su conjunto vigilado y sus censos

Cada infracción declara el DIAGNÓSTICO que espera. Sin `espera`, una prueba se daría por
detectada porque falló, sin comprobar que falló POR ESO.
"""
# ---------------------------------------------------------------------------
#  ADVERTENCIA DE FORMA · este módulo NO lleva línea de intérprete, y es deliberado.
#
#  `H-03` de la auditoría independiente del 2026-09-04 obligó a que el inventario de puntos
#  ejecutables se derive del ÁRBOL ENTERO y a que TODO `.py` quede clasificado —el
#  inventario anterior era mecánico DENTRO de dos zonas escritas a mano, y por eso
#  `validadores/` estaba entera fuera del control mientras `H-01` encontraba el defecto
#  `E-10` vivo en `huella.py`—. La equivalencia que `T330` comprueba sobre el disco es:
#
#      lleva `#!`   ⟺   es INVOCABLE   ⟺   lleva el MECANISMO `E-10`
#
#  Este módulo se IMPORTA —`comprobar_negativos.py` lo incorpora por nombre y sin
#  `try/except`— y no se ejecuta: no define `__main__` ni sale desde el nivel superior. No
#  cumple el segundo término, así que tampoco puede llevar el primero: una línea de
#  intérprete presenta un módulo como ejecutable, y a un ejecutable esta equivalencia le
#  exige la purga. Se retira la línea, y con ella la ambigüedad. Es exactamente lo que
#  `ADJ-B2` hizo con `errores.py`, `firma.py`, `atestacion.py` y `aislamiento.py` de la
#  raíz externa.
# ---------------------------------------------------------------------------

from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  Este módulo registra su catálogo de mutaciones con `CATALOGO.extend(...)` en el NIVEL
#  SUPERIOR: hace trabajo al importarse, y por tanto es un punto ejecutable, lo invoque
#  alguien directamente o no. El auditor independiente señaló que de los dos ficheros de
#  esta familia uno llevaba la guarda y el otro no, y que la asimetría no la medía nadie
#  porque los dos quedaban fuera del inventario. Ahora los dos están dentro.

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
#  Este módulo entró en el inventario de puntos ejecutables al invertirse la carga —hace
#  trabajo al importarse: registra su catálogo con `CATALOGO.extend(...)` en el nivel
#  superior—, y a un punto ejecutable se le exige el mecanismo ENTERO y no medio: la guarda
#  de `G-03` de arriba, que decide el aislamiento antes de que el intérprete arranque, y
#  esta purga, que retira de `sys.path` lo que el LANZADOR pudo meter. Se copia byte a byte
#  del resto de puntos, que es lo que `T330` comprueba: un mecanismo «adaptado» es un
#  mecanismo que ya no se sabe si protege.

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

CATALOGO = []

import os  # noqa: E402

import comprobar_negativos as _cn  # noqa: E402

Mutacion, _sustituir, _escribir = _cn.Mutacion, _cn._sustituir, _cn._escribir


# ===========================================================================
#  CONTRATO 1 · la cobertura de sedes se DESCUBRE
# ===========================================================================

def m_c1_sede_nueva_con_cifra_falsa(raiz):
    """La prueba negativa que el CONTRATO 1 pide con esas palabras.

    Un fichero NUEVO —«que ninguna lista podría contener»— con una afirmación falsa sobre
    un objeto censable. Si `T151` lo detecta sin que nadie haya tocado el validador, la
    cobertura deriva; si no lo detecta, sigue enumerándose.
    """
    _escribir(raiz, "kernel/operativo/capacidades/NOTA-DE-COBERTURA.md",
              "# Nota de cobertura\n\nEl sistema declara hoy las once capacidades del "
              "árbol, cada una con su ficha.\n")


def m_c1_sede_nueva_en_otro_arbol(raiz):
    """La misma prueba, en una rama del corpus que ninguna regla nombra.

    La primera sede nueva cuelga de `capacidades/`, que las reglas del censo mencionan por
    otros motivos. Ésta cuelga de `plantillas/`, que ninguna regla nombra: si sólo se
    detectara la primera, la cobertura estaría derivando a medias.
    """
    _escribir(raiz, "kernel/operativo/plantillas/APUNTE-SUELTO.md",
              "# Apunte\n\nEste apunte recuerda que los cuatro contratos transversales "
              "gobiernan el corpus.\n")


def m_c1_cobertura_vuelve_a_enumerarse(raiz):
    """La condición de cierre, atacada de frente: la lista literal vuelve.

    Se sustituye el BARRIDO por una lista de rutas escrita a mano. `T151` seguiría en verde
    —las sedes de la lista siguen siendo correctas—, y es exactamente por eso que hace
    falta `T270`: la que ejerce la propiedad.
    """
    _sustituir(raiz, "kernel/operativo/validadores/comprobar_recuentos.py",
               "def sedes_vivas(base):",
               "def sedes_vivas(base):\n"
               "    for _rel in ('kernel/operativo/00-INDICE.md',):\n"
               "        _r = os.path.join(base, _rel)\n"
               "        if os.path.exists(_r):\n"
               "            yield _rel, _r\n"
               "    return\n"
               "def _sedes_vivas_original(base):")


# ===========================================================================
#  CONTRATO 1bis · el censo de perfiles de agente
# ===========================================================================

def m_c1bis_perfil_nuevo_en_c2(raiz):
    """«Introducir un perfil nuevo en `C2` y comprobar que el recuento se mueve solo.»

    Es la prueba que el contrato prescribe, literal. El perfil entra en `C2`, la derivación
    pasa a contar uno más, y la tabla publicada deja de coincidir. Si el recuento NO se
    moviera, la cifra seguiría viviendo sólo en prosa, que es `N-04`.
    """
    import os
    import re
    ruta = os.path.join(raiz, "kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    inicio = texto.index("```yaml ads:perfil-agente")
    fin = texto.index("```", texto.index("\n", inicio)) + 3
    clon = re.sub(r"^id: perfil:[\w:-]+", "id: perfil:censo-de-sabotaje",
                  texto[inicio:fin], flags=re.M)
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto[:fin] + "\n\n" + clon + texto[fin:])


# ===========================================================================
#  CONTRATO 2 · el alcance de `T152`
# ===========================================================================

def m_c2_sede_nueva_con_version_falsa(raiz):
    """«Crear una sede nueva con una versión falsa y comprobar que la detecta sin
    modificar el validador.» Es la prueba negativa del CONTRATO 2, literal."""
    _escribir(raiz, "kernel/operativo/entrada/NOTA-DE-VERSION.md",
              "# Nota\n\nEste circuito está escrito contra `kernel/KERNEL.md` 1.2.0 y su "
              "vocabulario.\n")


def m_c2_alcance_vuelve_a_ser_una_lista(raiz):
    """El alcance vuelve a ser los dos ficheros escritos a mano que `T152` recorría."""
    _sustituir(raiz, "kernel/operativo/validadores/comprobar_versiones.py",
               'AMBITO_F6 = [r"^README\\.md$", r"^START_HERE\\.md$", r"^kernel/", r"^packs/"]',
               'AMBITO_F6 = [r"^README\\.md$", r"^START_HERE\\.md$"]')


# ===========================================================================
#  `D104` · el catálogo de `<CAP>:revision`
# ===========================================================================

def m_d104_dep_sin_revision(raiz):
    """EL CONTRAEJEMPLO PRESCRITO, conservado como sabotaje.

    `D104` exige que la comprobación devuelva FALLIDA nombrando `proceso:DEP` →
    `SEG:revision` AUSENTE. Eso describía el árbol ANTES de que F6 materializara. Retirar
    la instancia de `DEP` —y SÓLO la de `DEP`, dejando intactas las de los otros cuatro
    procesos del catálogo— tiene que volver a producir exactamente ese diagnóstico. Es la
    mitad que `D104` subraya: «tiene que seguir fallando si alguien añade `SEG:revision` a
    los otros cuatro procesos del catálogo y no a `DEP`».
    """
    _sustituir(raiz, "kernel/operativo/recorrido/01-PROCESOS.md",
               '''  - id: revision-de-seguridad
    capa_exigida: >
      la revisión posterior de SEG sobre la dependencia ya incorporada, con lo comprobado y lo NO comprobado
    capacidad_productora: "SEG:revision"''',
               '''  - id: revision-de-seguridad
    capa_exigida: >
      la revisión posterior de SEG sobre la dependencia ya incorporada, con lo comprobado y lo NO comprobado
    capacidad_productora: "APR"''')


def m_d104_revision_retirable_en_dep(raiz):
    """«Un proceso con `SEG:revision` RETIRABLE en `DEP` → FALLA.»

    La instancia sigue estando; lo que se rompe es la HERENCIA. Su origen —la condición de
    seguridad anterior a construir— es irretirable por `G28`, y el paso 8 del algoritmo
    manda heredar la obligatoriedad.
    """
    _sustituir(raiz, "kernel/operativo/recorrido/01-PROCESOS.md",
               "      nadie: la participación de SEG en DEP es doble por b.16",
               "      PLT, que posee la maquinaria; la participación de SEG en DEP es doble por b.16")


def m_d104_revision_antes_del_ancla(raiz):
    """«Un proceso con `<CAP>:revision` colocado ANTES de su ancla → FALLA.»

    La revisión de `DEP` se mueve delante del dosier de `VER`. Sigue declarada, sigue
    heredando, y está en el sitio equivocado: revisar antes de que exista lo que hay que
    revisar no es la mitad posterior de la participación doble.
    """
    import os
    ruta = os.path.join(raiz, "kernel/operativo/recorrido/01-PROCESOS.md")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    inicio = texto.index("  - id: revision-de-seguridad")
    fin = texto.index("condicionales:", inicio)
    bloque = texto[inicio:fin]
    texto = texto[:inicio] + texto[fin:]
    ancla = texto.index("  - id: evidencia-suficiente\n    capa_exigida: >\n      el dosier de VER sobre el cambio")
    texto = texto[:ancla] + bloque + texto[ancla:]
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto)


def m_d104_revision_no_hereda_la_activacion(raiz):
    """La revisión condicional se activa con una condición distinta de la de su origen.

    `FEA` declara `SEG:condiciones` bajo `C-SEG`; su revisión pasa a activarse con `C-DOM`.
    El par sigue instanciado y la participación queda desacoplada de lo que la exige: se
    revisaría cuando manda el dominio y no cuando manda la seguridad.
    """
    _sustituir(raiz, "kernel/operativo/recorrido/01-PROCESOS.md",
               '''  - capacidad: "SEG:revision"
    condicion: "C-SEG"''',
               '''  - capacidad: "SEG:revision"
    condicion: "C-DOM"''')


def m_d104_conjunto_vigilado_deja_de_derivarse(raiz):
    """`Q-09` · el conjunto vigilado se deriva de las FICHAS, no de una lista.

    Se retira de la ficha de `SEG` la declaración de doble participación de `b.16`. El
    catálogo tiene que moverse solo: los pares de `SEG` dejan de exigirse, y las instancias
    que el árbol conserva quedan sin ninguna participación que las derive. Una lista
    escrita en el validador seguiría en verde sobre un catálogo que ya no es el suyo.
    """
    _sustituir(raiz, "kernel/operativo/capacidades/SEG/CAPACIDAD.md",
               '  - "b.16 · SEG participa dos veces y es obligatoria antes de construir en DEP"',
               '  - "b.16 · SEG es obligatoria antes de construir en DEP"')


def m_d104_via_propietaria_sin_par(raiz):
    """`O-01` · una participación PROPIETARIA de una vigilada que no emite par.

    `proceso:SIS` pasa a tener `propietario_global: "DOM"`. Por la vía 1 eso exige
    `DOM:revision`, y el fixture de la vía propietaria existe justamente porque `D103`
    pasaba este caso en verde sin emitir par.
    """
    _sustituir(raiz, "kernel/operativo/recorrido/01-PROCESOS.md",
               'id: proceso:SIS\nnombre: Evolución del sistema',
               'id: proceso:SIS\nnombre: Evolución del sistema')
    _sustituir(raiz, "kernel/operativo/recorrido/01-PROCESOS.md",
               'Una fricción real, un incidente del sistema o una capacidad de producto bloqueada lo exigen.\npropietario_global: "SIS"',
               'Una fricción real, un incidente del sistema o una capacidad de producto bloqueada lo exigen.\npropietario_global: "SEG"')


def m_d104_censo_de_fixtures_caducado(raiz):
    """El censo de fixtures de §19 deja de ser el que la batería corre.

    `D104` lo dice así: «`G-15` cuenta los fixtures que ejecuta y falla si esta cifra no es
    la suya, nombrando sede, responsable y remedio. La única forma de que envejezca es en
    ROJO». Se mueve la cifra publicada y la comprobación tiene que ponerse roja.
    """
    _sustituir(raiz, "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md",
               "escrito a mano: 20 fixtures**", "escrito a mano: 17 fixtures**")


def m_d104_reparto_por_via_caducado(raiz):
    """`Q-03` · la proyección del reparto por vía deja de ser la derivada.

    «Un total de nueve admite repartos que significan cosas distintas —mover los
    condicionales de `FEA` de la forma tipada a la desnuda deja el nueve intacto y cambia
    el contrato—, luego publicar sólo el total no basta.»
    """
    _sustituir(raiz, "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md",
               "**vía 1 · 0 pares · vía 2 · 1 par · vía 3 · 0 pares · vía 4 ·\n"
               "                           8 pares**",
               "**vía 1 · 0 pares · vía 2 · 2 pares · vía 3 · 0 pares · vía 4 ·\n"
               "                           7 pares**")


CATALOGO.extend([
    Mutacion("N270", "§19 CONTRATO 1", "T151", "comprobar_recuentos",
             "una sede NUEVA publica una cifra falsa sobre un objeto censable",
             m_c1_sede_nueva_con_cifra_falsa,
             espera="NOTA-DE-COBERTURA.md"),
    Mutacion("N270b", "§19 CONTRATO 1", "T151", "comprobar_recuentos",
             "la sede nueva cuelga de una rama que ninguna regla nombra",
             m_c1_sede_nueva_en_otro_arbol,
             espera="APUNTE-SUELTO.md"),
    Mutacion("N270c", "§19 CONTRATO 1", "T270", "comprobar_recuentos",
             "la cobertura de sedes vuelve a ser una lista literal de rutas",
             m_c1_cobertura_vuelve_a_enumerarse,
             espera="la cobertura sigue enumerándose"),
    Mutacion("N271", "§19 CONTRATO 1bis", "T271", "comprobar_recuentos",
             "entra un perfil de agente nuevo en C2 y el censo tiene que moverse solo",
             m_c1bis_perfil_nuevo_en_c2,
             espera="perfiles_de_agente = 22"),
    Mutacion("N272", "§19 CONTRATO 2", "T152", "comprobar_versiones",
             "una sede NUEVA publica una versión del kernel que no es la vigente",
             m_c2_sede_nueva_con_version_falsa,
             espera="NOTA-DE-VERSION.md"),
    Mutacion("N272b", "§19 CONTRATO 2", "T272", "comprobar_versiones",
             "el alcance de T152 vuelve a ser los dos ficheros escritos a mano",
             m_c2_alcance_vuelve_a_ser_una_lista,
             espera="el alcance sigue enumerándose"),
    Mutacion("N273", "§19 D104", "T273", "comprobar_composicion_procesos",
             "DEP se queda sin SEG:revision, con las otras cuatro intactas",
             m_d104_dep_sin_revision,
             espera="proceso:DEP → `SEG:revision` AUSENTE"),
    Mutacion("N273b", "§19 D104", "T273", "comprobar_composicion_procesos",
             "la SEG:revision de DEP se vuelve RETIRABLE y deja de heredar de su origen",
             m_d104_revision_retirable_en_dep,
             espera="no hereda la autoridad de retirada"),
    Mutacion("N273c", "§19 D104", "T273", "comprobar_composicion_procesos",
             "la revisión de DEP se coloca ANTES de su ancla",
             m_d104_revision_antes_del_ancla,
             espera="está ANTES de su ancla"),
    Mutacion("N273d", "§19 D104", "T273", "comprobar_composicion_procesos",
             "una revisión condicional deja de heredar la activación de su origen",
             m_d104_revision_no_hereda_la_activacion,
             espera="no hereda la activación"),
    Mutacion("N273e", "§19 D104", "T273", "comprobar_composicion_procesos",
             "la ficha de SEG deja de declarar la doble participación de b.16",
             m_d104_conjunto_vigilado_deja_de_derivarse,
             espera="NINGUNA participación del catálogo la exige"),
    Mutacion("N273f", "§19 D104", "T273", "comprobar_composicion_procesos",
             "una participación PROPIETARIA de una capacidad vigilada no emite par",
             m_d104_via_propietaria_sin_par,
             espera="vía 1"),
    Mutacion("N275", "§19 D104", "T275", "comprobar_composicion_procesos",
             "el censo de fixtures publicado deja de ser el que la batería ejecuta",
             m_d104_censo_de_fixtures_caducado,
             espera="el censo de fixtures publicado es 17"),
    Mutacion("N276", "§19 D104", "T276", "comprobar_composicion_procesos",
             "el reparto por vía publicado deja de ser el derivado del árbol",
             m_d104_reparto_por_via_caducado,
             espera="pares por la vía 2 y el árbol deriva"),
])


# ===========================================================================
#  `ADJ-B3` y `ADJ-G2` · LOS SABOTAJES DE LA PASADA DEL 2026-09-04
# ===========================================================================
#  QUÉ SE AÑADE AQUÍ, Y POR QUÉ AQUÍ. `ADJ-B3` midió que `V6-12` figuraba con `B=0` —o sea
#  «tiene sabotaje declarado»— mientras la propiedad que el adjudicador derribó **no tenía
#  ninguno**: los tres imputados eran `N189`, `N242` y `N242b`, y `N189` está declarado
#  contra `V6-11`. Y `ADJ-G2` midió que el `estado:` de un escenario no lo contrastaba
#  nadie. Cada corrección de esta pasada trae aquí su infracción deliberada, que es lo que
#  impide que la corrección se pueda deshacer en silencio.
#
#  Se escriben en ESTE fichero y no en `comprobar_negativos.py` por la misma razón por la
#  que existe el fichero: tres ejes en paralelo sobre la misma lista producen una
#  integración que nadie puede revisar por partes. El catálogo sigue siendo UNO, y lo sigue
#  componiendo `comprobar_negativos.py` por nombre.

PRUEBAS_RUNTIME = "kernel/operativo/runtime/pruebas/"
ADMISION = PRUEBAS_RUNTIME + "test_admision.py"
BATERIA = _cn.CLASE_BATERIA
SEDE_ADMISION = "kernel/operativo/runtime/admision/"


def m_b3_el_append_only_vuelve_al_prefijo(raiz):
    """`ADJ-B3` · el régimen de ENTRADAS CERRADAS se retira y vuelve el prefijo.

    Es el defecto EXACTO que el adjudicador explotó: `actual.startswith(anterior)` contra el
    commit de nacimiento, que protegía 14 395 de 42 181 bytes de la sede del Owner.
    """
    ruta = os.path.join(raiz, SEDE_ADMISION + "perimetro.py")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    inicio = texto.index("        # `ADJ-B3` · `O27` §3 · el régimen FUERTE")
    fin = texto.index("        # Régimen de PREFIJO, para documentos continuos")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto[:inicio] + texto[fin:])


def m_b3_el_delimitador_vuelve_a_ser_contenido(raiz):
    """`ADJ-B3` · el delimitador estructural vuelve a contarse como texto de la entrada.

    `O27` §1 dice que un delimitador externo NO es contenido. Contarlo pone en ROJO una
    sede INTACTA en cuanto se inscribe la resolución siguiente —medido: seis bytes por
    inscripción— y un guardián que da rojos falsos acaba apagado.
    """
    _sustituir(raiz, SEDE_ADMISION + "sede.py",
               "        if bruto.endswith(DELIMITADOR):\n"
               "            return bruto[: -len(DELIMITADOR)]",
               "        if bruto.endswith(DELIMITADOR):\n"
               "            return bruto")


def m_b3_la_conservacion_byte_a_byte_se_retira(raiz):
    """`ADJ-B3` · el canal ESTRUCTURAL deja de comparar cada entrada byte a byte."""
    _sustituir(raiz, SEDE_ADMISION + "sede.py",
               '        if bloque.contenido != registrada["contenido"]:',
               '        if False:')


def m_b3_el_canal_de_presencia_literal_se_retira(raiz):
    """`ADJ-B3` · se retira el canal que sigue hablando con la estructura rota."""
    _sustituir(raiz, SEDE_ADMISION + "sede.py",
               '    literales = []\n'
               '    for identificador in libro["orden"]:\n'
               '        if libro["entradas"][identificador]["contenido"] not in contenido:\n'
               '            literales.append(identificador)',
               '    literales = []')


def m_b3_el_canal_de_la_historia_se_retira(raiz):
    """`ADJ-B3` · una alteración confirmada y luego revertida deja de constar."""
    _sustituir(raiz, SEDE_ADMISION + "sede.py",
               '    for incidencia in libro["incidencias"]:',
               '    for incidencia in []:')


def m_b3_el_regimen_se_decide_por_el_fichero_de_hoy(raiz):
    """`ADJ-B3` · el régimen deja de derivarse de la HISTORIA.

    Con esto, borrar las cabeceras `# ``Onn`` ·` haría que el documento «dejara de tener
    entradas» y cayera al contraste débil: apagar el guardián quitándole la estructura.
    """
    _sustituir(raiz, SEDE_ADMISION + "sede.py",
               '    return any(identificador != PREAMBULO for identificador in libro["orden"])',
               '    return False')


def m_g2_la_sede_de_la_derivacion_desaparece(raiz):
    """`ADJ-G2` · `registro_pruebas` deja de publicar la fórmula del estado.

    `T350` NO reimplementa la derivación: la importa de su sede única, que es la regla que
    `V6-19` impone en el paquete de admisión y por la misma razón. Si la sede deja de
    ofrecerla, la prueba tiene que DEJAR DE EMITIR en vez de calcular una suya equivalente,
    que es la degradación silenciosa que `E-09` cerró en el verificador.
    """
    _sustituir(raiz, "kernel/operativo/validadores/registro_pruebas.py",
               "def contraste_de_estados(escenarios, raiz):",
               "def contraste_de_estados_RETIRADA(escenarios, raiz):")


def m_g2_una_prueba_fallida_se_declara_superada(raiz):
    """`ADJ-G2` · la divergencia VIVA que el adjudicador midió, reintroducida al revés.

    `T273` vuelve a declarar `prueba-fallida` mientras su evidencia publica
    `T273  SUPERADA` y `# codigo: 0`. Es el estado exacto del árbol candidato del gate.
    """
    _sustituir(raiz, "kernel/operativo/pruebas/T270-T289-contratos-19-y-composicion.md",
               'validador: "kernel/operativo/validadores/comprobar_composicion_procesos.py"'
               '\nestado: prueba-superada',
               'validador: "kernel/operativo/validadores/comprobar_composicion_procesos.py"'
               '\nestado: prueba-fallida')


def m_g2_un_escenario_cita_una_evidencia_que_no_existe(raiz):
    """`ADJ-G2` · un escenario declara `prueba-superada` con evidencia inexistente.

    Es la forma exacta de la segunda divergencia viva que esta pasada encontró: `T277`
    declaraba `prueba-ejecutada` citando un fichero que no ha existido en ningún commit.
    """
    _sustituir(raiz, "kernel/operativo/pruebas/T182-T194-runtime-y-admision.md",
               "evidencia: evidencia/admision-salida.txt",
               "evidencia: evidencia/no-existe-esta-salida.txt")


def m_g2_la_evidencia_se_edita_a_mano(raiz):
    """`ADJ-G2` · la evidencia publicada se edita para que diga otra cosa.

    Sin canal que la contraste, un `SUPERADA` escrito a mano vale lo mismo que uno
    ejecutado. Aquí se cambia el veredicto de `T273` a `FALLIDA` en la evidencia y se deja
    el escenario declarando `prueba-superada`: el contraste tiene que verlo POR LA
    EVIDENCIA, y no por el campo.

    ALCANCE, DICHO: el OTRO canal de este mismo hallazgo —que la evidencia en disco sea la
    que `HEAD` tiene confirmada— NO se puede sabotear desde aquí, porque `copiar_corpus`
    fabrica la copia SIN `.git` y ese canal se declara no ejecutado sobre ella. Se dice en
    vez de fingir que está probado.
    """
    _sustituir(raiz, "kernel/operativo/pruebas/evidencia/composicion-procesos-salida.txt",
               "T273  SUPERADA", "T273  FALLIDA ")


def m_h02_un_escenario_sube_de_estado_sin_contraste(raiz):
    """`H-02` · la grieta que la auditoría independiente del 2026-09-04 destapó.

    Un escenario vuelve a declarar `prueba-superada` sobre una evidencia que **NO LO
    NOMBRA**. Es la forma que `ADJ-G2` dejaba abierta: la divergencia se CALCULABA, se
    escribía el motivo —«la ejecución consta, el resultado DE ESTE escenario no»— y se
    DESCARTABA por marcar `contrastado=False`, de modo que catorce escenarios subían de
    estado por argumento con `T350` en verde.

    ESTE SABOTAJE SE REESCRIBIÓ AL CERRARSE `D-02`, y se dice por qué. `T162` era uno de
    esos catorce: declaraba `prueba-ejecutada` porque `evidencia/workspace-salida.txt` no
    lo nombraba —`grep -c "T162"` devolvía `0`—, y la mutación consistía en devolverle el
    `prueba-superada` que tuvo. Cerrada `D-02`, su ejecutor publica el veredicto nominal y
    `T162` declara `prueba-superada` con todo el derecho: ya no hay ningún escenario en el
    estado que este sabotaje reintroducía, y por eso dejó de encajar.

    La CLASE es la misma y se reproduce por el otro lado: en vez de subir el estado
    declarado hasta una evidencia que no lo nombra, se le quita a la evidencia el veredicto
    que lo nombra y se deja el estado declarado donde está. El resultado es idéntico —un
    `prueba-superada` que su evidencia no sostiene— y la distingue de `N350b` y `N350c` lo
    mismo que antes: allí la evidencia CONTRADICE o no existe; aquí existe, la ejecución
    consta, y lo que falta es el veredicto de ESTE escenario.
    """
    _sustituir(raiz, "kernel/operativo/pruebas/evidencia/workspace-salida.txt",
               "T162 · una fuente ya clonada se reutiliza y no se vuelve a clonar. ... ok",
               "una fuente ya clonada se reutiliza y no se vuelve a clonar. ... ok")


CATALOGO.extend([
    Mutacion("N340", "ADJ-B3 · O27 §3", "T342", ADMISION,
             "el append-only de la sede del Owner vuelve al PREFIJO del nacimiento",
             m_b3_el_append_only_vuelve_al_prefijo, clase=BATERIA,
             casos=["ElVeredictoAplicaLasEntradasCerradas"],
             espera="el borrado de una entrada cerrada posterior al nacimiento ha pasado"),
    Mutacion("N341", "ADJ-B3 · O27 §1", "T341", ADMISION,
             "el delimitador estructural vuelve a contar como contenido de la entrada",
             m_b3_el_delimitador_vuelve_a_ser_contenido, clase=BATERIA,
             casos=["AppendOnlyPorEntradaCerrada"],
             espera="!= []"),
    Mutacion("N343", "ADJ-B3 · O27 §3", "T343", ADMISION,
             "el canal ESTRUCTURAL deja de comparar cada entrada byte a byte",
             m_b3_la_conservacion_byte_a_byte_se_retira, clase=BATERIA,
             casos=["AppendOnlyPorEntradaCerrada"],
             espera="el canal ESTRUCTURAL de comparación entrada a entrada se ha quedado"),
    Mutacion("N342", "ADJ-B3 · O27 §3", "T342", ADMISION,
             "se retira el canal de PRESENCIA LITERAL de las entradas cerradas",
             m_b3_el_canal_de_presencia_literal_se_retira, clase=BATERIA,
             casos=["AppendOnlyPorEntradaCerrada", "LaSedeRealDelOwner"],
             espera="el ataque tiene que nombrar las entradas que destruye"),
    Mutacion("N343b", "ADJ-B3 · V6-12", "T343", ADMISION,
             "una alteración confirmada y luego revertida deja de constar",
             m_b3_el_canal_de_la_historia_se_retira, clase=BATERIA,
             casos=["AppendOnlyPorEntradaCerrada"],
             espera="confirmada y luego revertida ha dejado de constar"),
    Mutacion("N349", "ADJ-B3 · O27 §3", "T349", ADMISION,
             "el régimen de entradas cerradas se decide por el fichero de HOY y no por la "
             "historia",
             m_b3_el_regimen_se_decide_por_el_fichero_de_hoy, clase=BATERIA,
             casos=["AppendOnlyPorEntradaCerrada",
                    "ElVeredictoAplicaLasEntradasCerradas"],
             espera="el régimen entradas-cerradas"),
    Mutacion("N350", "ADJ-G2", "T350", "comprobar_evidencia",
             "la SEDE de la derivación del estado deja de publicar la fórmula",
             m_g2_la_sede_de_la_derivacion_desaparece,
             espera="ha dejado de publicarla"),
    Mutacion("N350b", "ADJ-G2", "T350", "comprobar_evidencia",
             "`T273` vuelve a declarar prueba-fallida con la evidencia diciendo SUPERADA",
             m_g2_una_prueba_fallida_se_declara_superada,
             espera="T273: declara `estado: prueba-fallida`"),
    Mutacion("N350c", "ADJ-G2", "T350", "comprobar_evidencia",
             "un escenario declara superada citando una evidencia que no existe",
             m_g2_un_escenario_cita_una_evidencia_que_no_existe,
             espera="NO EXISTE en el árbol"),
    Mutacion("NH02", "H-02", "T350", "comprobar_evidencia",
             "un escenario vuelve a declarar `prueba-superada` sobre una evidencia que NO "
             "LO NOMBRA, que es la divergencia que el aparato calculaba y descartaba",
             m_h02_un_escenario_sube_de_estado_sin_contraste,
             espera="subir de estado por argumento"),
    Mutacion("N350d", "ADJ-G2", "T350", "comprobar_evidencia",
             "la evidencia publicada se edita a mano para que diga otra cosa",
             m_g2_la_evidencia_se_edita_a_mano,
             espera="su evidencia sostiene `prueba-fallida`"),
])
