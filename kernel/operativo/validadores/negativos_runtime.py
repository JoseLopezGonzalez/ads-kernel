#!/usr/bin/env python3
"""negativos_runtime — las infracciones deliberadas que sabotean las BATERÍAS del runtime.

POR QUÉ EXISTE ESTE FICHERO, Y QUÉ AGUJERO CIERRA. El catálogo único de infracciones sólo
sabía sabotear VALIDADORES: `comprobar_negativos.ejecutar` construía
`kernel/operativo/validadores/<validador>.py`, lo llamaba con `--json --raiz` y buscaba una
fila `{"id": "Tnnn", "estado": …}`. Una batería `unittest` del runtime no puede satisfacer
nada de eso. Medido antes de corregir: de las 102 mutaciones con validador literal, **CERO**
apuntaban a `kernel/operativo/runtime/pruebas/`.

La consecuencia no era estética. El derivador del universo obligatorio calcula la resta `B`
—«implementadas SIN PRUEBA CAPAZ DE FALLAR»— como «ninguna `Mutacion` apunta a sus
pruebas». Como las 37 obligaciones de esa resta se verifican con baterías del runtime y el
catálogo no podía alcanzarlas, **36 de sus 37 filas estaban ahí POR CONSTRUCCIÓN**. Con ese
criterio `F6` sería incertificable por construcción, y eso no puede ser lo que `O26` §5.2
quiso decir. No se baja el listón: se sube el ALCANCE DEL INSTRUMENTO, y después se puebla.

QUÉ HAY AQUÍ, Y CON QUÉ EXIGENCIA. Dieciocho infracciones. Diecisiete son de clase
`bateria` —copian el corpus, meten el defecto, ejecutan la batería DECLARADA con el
intérprete en curso sobre la copia y exigen TRES cosas, no una: que la batería termine en
rojo, que ENTRE LOS CASOS CAÍDOS esté el declarado —se sabe por el docstring `Tnnn · …` que
`unittest` imprime debajo del nombre de cada caso con `verbosity=2`— y que ESE caso caiga
POR EL MOTIVO ESPERADO—. Una es de clase `validador`, porque la obligación que desbloquea
—`FD-3`— se verifica con `comprobar_arranque.py` y no con una batería.

CÓMO SE ELIGIÓ CADA UNA, Y POR QUÉ NO SON TREINTA Y SIETE. Las 37 obligaciones no tienen 37
pruebas: se concentran en unas pocas. Lo que hace falta es que ALGUNA mutación apunte a una
prueba que cubra cada obligación, y que cada mutación sabotee una propiedad **real y
distinta**, la que la obligación NOMBRA. Un sabotaje que no corresponda a la propiedad que
la obligación nombra es peor que la ausencia: acredita en falso. Por eso cada entrada de
abajo cita el `falla_si` del escenario que ataca, y rompe exactamente esa cosa.

  obligación(es)                        prueba   propiedad saboteada
  ------------------------------------  -------  --------------------------------------
  `A14`                                 `T172`   la guarda de intérprete se puede RELAJAR
  `g.1` `g.2` `g.16`                    `T173`   el diario lleva el `pid` del que escribe
  `g.3` `g.4` `g.12` `g.16`             `T174`   la zona de preparación entra al versionado
  `g.8` `g.3`                           `T175`   el punto de no retorno se mueve a `abierta`
  `g.6` `g.12`                          `T176`   agotar reintentos no abre el registro
  `g.5` `g.13` `g.15`                   `T177`   el `cid` del canónico deja de contrastarse
  `g.9` `g.2`                           `T178`   la cabeza no ancla el extremo al LEER
  `g.10` `g.11`                         `T179`   una versión de formato desconocida se adivina
  `g.14`                                `T187`   omitir el valor viejo salta la guarda del hook
  `g.15` `FD-1`                         `T192`   la configuración de confianza cabe DENTRO
  `V6-01`…`V6-09`                       `T188`   una salida truncada se devuelve como completa
  `V6-10` `V6-11`                       `T189`   el instrumento se sale de su propio alcance
  `V6-13` `V6-14` `V6-17` `V6-18` `V6-19` `T190` la sede de fórmulas rompe el caso frontera
  `V6-15`                               `T211`   la versión vulnerable deja de aceptar el ataque
  `V6-16`                               `T217`   una instalación ALTERADA emite veredicto
  `FD-5`                                `T216`   el backend débil se presenta como fuerte
  `FD-6`                                `T191`   un recibo ABIERTO se reejecuta, y duplica
  `FD-3`                                `T194`   el motor durable no viaja al proyecto instalado

FORMA SINTÁCTICA, Y POR QUÉ NO SE TOCA. El derivador externo lee los sabotajes con
`Mutacion\\(\\s*"([^"]+)"\\s*,\\s*"[^"]*"\\s*,\\s*"(T\\d+)"`. Esa expresión exige el token
`Mutacion` pegado al paréntesis y el identificador de prueba como TERCER posicional
entrecomillado. Por eso la clase de batería no es una subclase con nombre propio: es un
CAMPO `clase` de `Mutacion`. Una subclase llamada de otro modo dejaría cada entrada de aquí
invisible para la resta `B`, que es lo único que este fichero existe para mover.

COSTE DE CORRIDA, MEDIDO. Cada mutación copia el corpus entero (~14 MB) y ejecuta una
batería COMPLETA: no hay ninguna corrida parcial, y por tanto no hay ninguna que declarar.
Las baterías usadas tardan, sueltas: `test_estado_durable` ~20 s, `test_gobierno_git` ~13 s,
`test_contencion` ~15 s, `test_raiz_externa` ~8 s, `test_admision` ~3 s, `test_arboles`
~1 s, `test_identidad` ~0,2 s; `comprobar_arranque` ~90 s. El total añadido está medido en
el informe de la corrección.
"""
from __future__ import annotations

CATALOGO = []

import comprobar_negativos as _cn  # noqa: E402

Mutacion, _sustituir = _cn.Mutacion, _cn._sustituir
BATERIA = _cn.CLASE_BATERIA

PRUEBAS_RUNTIME = "kernel/operativo/runtime/pruebas/"
ESTADO_DURABLE = PRUEBAS_RUNTIME + "test_estado_durable.py"
ADMISION = PRUEBAS_RUNTIME + "test_admision.py"
GOBIERNO_GIT = PRUEBAS_RUNTIME + "test_gobierno_git.py"
IDENTIDAD = PRUEBAS_RUNTIME + "test_identidad.py"
ARBOLES = PRUEBAS_RUNTIME + "test_arboles.py"
CONTENCION = PRUEBAS_RUNTIME + "test_contencion.py"
ADAPTADORES = PRUEBAS_RUNTIME + "test_adaptadores.py"
RAIZ_EXTERNA = PRUEBAS_RUNTIME + "test_raiz_externa.py"


# ===========================================================================
#  `A14` · la guarda de versión del intérprete
# ===========================================================================

def m_a14_la_guarda_se_puede_relajar(raiz):
    """`T172`, `falla_si`: «la guarda se puede relajar por entorno».

    `entorno.py` admite `ADS_ENTORNO_VERSION_MINIMA` para SUBIR la exigencia y NUNCA para
    bajarla, y lo razona: «una guarda que se puede relajar por entorno no es una guarda: es
    un interruptor, y el primero que lo use en CI la apaga para todos». Aquí se le quita la
    pinza y la variable pasa a mandar en los dos sentidos.
    """
    _sustituir(raiz, "kernel/operativo/validadores/entorno.py",
               "    if pedido <= VERSION_MINIMA:\n"
               "        return VERSION_MINIMA, (f\"{VARIABLE_DE_EXIGENCIA}={crudo} no supera la mínima \"",
               "    if False:\n"
               "        return VERSION_MINIMA, (f\"{VARIABLE_DE_EXIGENCIA}={crudo} no supera la mínima \"")


# ===========================================================================
#  `g.1`…`g.16` · el MOTOR DE ESTADO DURABLE
# ===========================================================================

def m_g1_el_diario_lleva_el_pid(raiz):
    """`T173`, `entonces`: «ninguna lectura del estado necesita reproyectar el diario», y el
    §0 prohíbe reloj, duración y `pid` en lo durable (`I-g3`).

    Un campo «inofensivo» en cada evento del diario: el `pid` del proceso que lo escribió.
    Es el defecto clásico —nadie lo pone por maldad— y rompe la reproducibilidad: dos
    almacenes construidos con las MISMAS transiciones dejan de dar los mismos bytes.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/diario.py",
               '        evento = {"esquema": ESQUEMA, "secuencia": len(completas) + 1, "tipo": tipo}',
               '        evento = {"esquema": ESQUEMA, "secuencia": len(completas) + 1, "tipo": tipo,\n'
               '                  "pid": os.getpid()}')


def m_g3_la_zona_de_preparacion_entra_al_versionado(raiz):
    """`T174`, `falla_si`: «la zona de preparación entra en el versionado, y la rama canónica
    pasa a contener estado parcial».

    El motor escribe él mismo el `.gitignore` del almacén «en vez de confiar en que alguien
    se acuerde de hacerlo». Aquí se le quita la única línea que excluye `operacional/`: a
    partir de ahí, un `git add -A` durante la ventana de una transacción sube la zona de
    preparación a la rama canónica, que es exactamente lo que `g.14` prohíbe.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/rutas.py",
               '    + OPERACIONAL + "/\\n"\n)',
               '    "# (la zona de preparación se excluye en otro sitio)\\n"\n)')


def m_g8_el_punto_de_no_retorno_se_adelanta(raiz):
    """`T175`, `falla_si`: «una transición incompleta queda publicada».

    El §3 fija el punto de no retorno en `transicion.preparada`: antes se REVIERTE, después
    se COMPLETA, y no hay tercera rama. Aquí se adelanta a `transicion.abierta`, de modo que
    una caída ANTES de preparar nada se «completa» igualmente y publica una transición que
    nunca llegó a estar preparada.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/motor.py",
               '        if "transicion.preparada" in tipos:\n'
               '            preparada = [e for e in propios if e["tipo"] == "transicion.preparada"][-1]',
               '        if "transicion.abierta" in tipos:\n'
               '            preparada = [e for e in propios if e["tipo"] == "transicion.abierta"][-1]')


def m_g6_agotar_reintentos_no_abre_el_registro(raiz):
    """`T176`, `falla_si`: «agotar reintentos se declara con el código del camino que NO abre
    el registro auxiliar».

    Es el agujero que la auditoría independiente ya encontró una vez, reintroducido: el
    escritor que agota sus reintentos propaga `ESCRITOR_CONCURRENTE` tal cual en vez de
    `REINTENTOS_AGOTADOS`, y por ese camino no se escribe el registro de `g.9`. La pendencia
    deja de existir sin que nadie la haya cerrado.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/motor.py",
               "            registro = self._abrir_reconciliacion_por_reintentos("
               "transicion.id, intentos, exc)\n"
               "            raise ReintentosAgotados(",
               "            raise exc\n"
               "            registro = self._abrir_reconciliacion_por_reintentos("
               "transicion.id, intentos, exc)\n"
               "            raise ReintentosAgotados(")


def m_g5_el_cid_deja_de_contrastarse(raiz):
    """`T177`, `falla_si`: «una corrupción se lee como estado válido».

    `leer` compara el `cid` del fichero en disco con el que `REVISION.json` declara y falla
    CERRADO cuando no casan: «un lector que recibe datos que no casan con la revisión
    propaga la corrupción». Aquí se sirve el contenido sin contrastarlo, que es servir como
    bueno un fichero canónico manipulado a mano.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/motor.py",
               "            if encontrado == esperado:\n"
               "                objeto = deserializar(datos, ruta=ruta)",
               "            if True:\n"
               "                objeto = deserializar(datos, ruta=ruta)")


def m_g9_la_cabeza_no_ancla_en_el_camino_de_lectura(raiz):
    """`T178`, `falla_si`: «la comprobación vive sólo en la verificación y no en el camino de
    lectura que deduce la pendencia».

    Una cadena de huellas NO detecta que le quiten la COLA: el prefijo sigue encadenado. Por
    eso el registro auxiliar tiene una CABEZA que ancla su extremo, y por eso se contrasta
    en el camino de LECTURA y no sólo al verificar. Aquí se retira de la lectura: borrar la
    última línea vuelve a cerrar una pendencia en silencio.
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/reconciliacion.py",
               "        if verificar:\n"
               "            # En el camino de LECTURA, y no sólo en `verificar_integridad`: `g.9` exige que\n"
               "            # la pendencia se deduzca de forma INEQUÍVOCA, y deducirla de un log al que le\n"
               "            # falta la cola no es deducirla, es creerse lo que quedó.\n"
               "            self._exigir_cabeza(salida)\n",
               "")


def m_g10_una_version_desconocida_se_adivina(raiz):
    """`T179`, `falla_si`: «un lector adivina el significado de una versión que no conoce».

    `g.10` dice que un lector que encuentra una versión que no entiende FALLA CERRADO. Aquí
    se conserva la comprobación de TIPO —que sea un entero— y se retira la de VALOR, que es
    la que importa: cualquier versión de formato futura se abre «haciendo lo que se pueda».
    """
    _sustituir(raiz, "kernel/operativo/runtime/estado/motor.py",
               "    if not isinstance(version, int) or version != VERSION_DE_FORMATO:",
               "    if not isinstance(version, int):")


# ===========================================================================
#  `g.14` · gobierno Git del REPOSITORIO DE CONTROL
# ===========================================================================

def m_g14_omitir_el_valor_viejo_salta_la_guarda(raiz):
    """`T187`, `falla_si`: «omitir el valor viejo —que Git hace opcional— salta la guarda».

    El `OID` nulo en `viejo` NO significa «creación»: Git lo pasa también cuando el llamador
    no declara valor viejo, que es el caso POR DEFECTO de `git update-ref <ref> <nuevo>`. El
    hook lo sabe y RESUELVE la ref por su cuenta. Aquí vuelve a tratarse como creación, y la
    mitad IMPOSIBLE de `G-A8` se salta escribiendo tres palabras en vez de cuatro.
    """
    _sustituir(raiz, "kernel/operativo/runtime/gobierno/git.py",
               '    actual="$viejo"\n'
               '    if [ "$viejo" = "$nulo" ]; then\n'
               '        actual=$(git rev-parse --verify --quiet "$ref^{commit}" 2>/dev/null || echo "$nulo")\n'
               '    fi',
               '    actual="$viejo"\n'
               '    if [ "$viejo" = "$nulo" ]; then\n'
               '        continue\n'
               '    fi')


# ===========================================================================
#  `g.15` · frontera con la RAÍZ EXTERNA DE CONFIANZA
# ===========================================================================

def m_g15_la_configuracion_cabe_dentro_del_arbol(raiz):
    """`T192`, `falla_si`: «el repositorio verificado puede cambiar qué identidad se acepta».

    `O25` §3 prohíbe que la configuración externa de confianza viva dentro de lo que
    gobierna. La comprobación es un `startswith` sobre la ruta resuelta; aquí se degrada a
    una igualdad exacta, de modo que sólo se rechaza la raíz del árbol y CUALQUIER
    subdirectorio suyo pasa. Es la forma en que estas guardas se rompen de verdad: nadie
    borra la comprobación, la debilita.
    """
    _sustituir(raiz, "kernel/operativo/runtime/identidad/configuracion.py",
               "def _dentro(candidata, arbol):\n"
               "    return candidata == arbol or candidata.startswith(arbol + os.sep)",
               "def _dentro(candidata, arbol):\n"
               "    return candidata == arbol")


# ===========================================================================
#  `V6-01`…`V6-19` · el VERIFICADOR DE ADMISIÓN
# ===========================================================================

def m_v6_salida_truncada_pasa_por_completa(raiz):
    """`T188`, `falla_si`: «una salida truncada devuelve lista vacía con éxito».

    Una lista `-z` bien formada termina SIEMPRE en `NUL`, y ése es el ÚNICO indicio de que
    la lectura llegó entera. Aquí se retira la denuncia del truncamiento y se devuelve lo
    que hubiera llegado: una lista parcial presentada como completa, que es como un fichero
    tocado desaparece del inventario sin que nada lo diga.
    """
    _sustituir(raiz, "kernel/operativo/runtime/admision/lectura.py",
               '    if not salida.endswith(b"\\0"):\n'
               '        raise SalidaTruncada(',
               '    if not salida.endswith(b"\\0"):\n'
               '        return salida.split(b"\\0")\n'
               '    if False:\n'
               '        raise SalidaTruncada(')


def m_v6_el_instrumento_se_sale_de_su_alcance(raiz):
    """`T189`, `falla_si` de `V6-11`: el verificador y su política no pueden salirse de su
    propio alcance.

    Los prefijos de autoinclusión son lo que mete al propio verificador —y a su política—
    dentro del perímetro que juzga. Vaciándolos, cambiar la regla y aprobarse con la regla
    nueva vuelve a ser gratis, y la mutación del instrumento deja de dar ROJO.
    """
    _sustituir(raiz, "kernel/operativo/runtime/admision/__init__.py",
               "    return politica.prefijos_de_autoinclusion()",
               "    return ()")


def m_v6_la_sede_de_formulas_rompe_su_frontera(raiz):
    """`T190`, `falla_si`: «un control adversarial no puede ponerse rojo», y `V6-19`: una
    sola definición de cada fórmula compartida.

    El recuento de líneas de un blob tiene DOS casos frontera declarados por su nombre: el
    fichero VACÍO da 0, y el que no termina en salto de línea cuenta igual. Aquí se sustituye
    por `splitlines()` con un mínimo de 1 —la reimplementación «equivalente» que siempre
    aparece—, y los dos instrumentos que cuentan líneas pasan a contradecirse justo ahí.
    """
    _sustituir(raiz, "kernel/operativo/runtime/admision/formulas.py",
               '    datos = bytes(datos)\n'
               '    if not datos:\n'
               '        return 0\n'
               '    completas = datos.count(b"\\n")\n'
               '    return completas if datos.endswith(b"\\n") else completas + 1',
               '    datos = bytes(datos)\n'
               '    return len(datos.splitlines()) or 1')


def m_v6_la_version_vulnerable_deja_de_reproducir(raiz):
    """`T211`, `falla_si`: «la versión vulnerable y la vigente no se distinguen sobre el mismo
    árbol».

    Las versiones históricas existen para ACEPTAR el árbol atacado: si dijeran ROJO a todo,
    la suite mediría dos instrumentos idénticos y no demostraría que la corrección corrigió
    nada. Aquí la versión vulnerable de `S1-01` pasa a denunciar siempre, «por si acaso», y
    la reproducción del defecto original deja de producirse.
    """
    _sustituir(raiz, "kernel/operativo/runtime/arboles/versiones.py",
               "    # Publica su recuento, y ése es el recuento FALSO que `S1-01` midió.\n"
               '    return _veredicto("VERDE", del_kernel=sorted(del_kernel),',
               '    return _veredicto("ROJO", del_kernel=sorted(del_kernel),\n'
               "                      enumerados=len(del_kernel), leidos=sorted(tocados),\n"
               '                      causa="por si acaso")\n'
               '    return _veredicto("VERDE", del_kernel=sorted(del_kernel),')


def m_v6_una_instalacion_alterada_emite_veredicto(raiz):
    """`T217`, `falla_si`: «un cambio dentro del árbol altera la política que la raíz externa
    aplica», y §11.8: los digests se RECALCULAN.

    La raíz externa recalcula el digest de cada fichero de su instalación y no emite si algo
    no casa. Aquí se retira `alteradas` de la condición: siguen contando la ausencia y el
    sobrante, pero un fichero MODIFICADO —el caso que importa, porque es el que un atacante
    provoca— deja de invalidar la instalación y el verificador manipulado emite veredicto.
    """
    _sustituir(raiz, "kernel/operativo/raiz-externa/instalar.py",
               '        "ok": not alteradas and not ausentes and not sobrantes,',
               '        "ok": not ausentes and not sobrantes,')


# ===========================================================================
#  `FD-5` · contención de procesos
# ===========================================================================

def m_fd5_el_backend_debil_se_presenta_como_fuerte(raiz):
    """`T216`, `falla_si` de `T214`: «una sonda declara disponible un mecanismo que no puede
    contener nada».

    El backend `simple` mata el GRUPO de procesos y su nivel declarado es INFERIOR: un
    descendiente que hace `setsid` se le escapa, y eso está escrito en `FD-5`. Aquí se le
    sube el nivel a `arbol-de-procesos`, con lo que una política que exige contención FUERTE
    se cumpliría con el backend que no la da. Es presentar el débil como fuerte, que es la
    forma exacta en que esta deuda se cerraría en falso.
    """
    _sustituir(raiz, "kernel/operativo/runtime/contencion/deteccion.py",
               '    "simple": GRUPO_DE_PROCESOS,\n}',
               '    "simple": ARBOL_DE_PROCESOS,\n}')


# ===========================================================================
#  `FD-6` · la ventana entre EJECUTAR y escribir el recibo, que se hace DETECTABLE
# ===========================================================================
#  `06-DEUDA` §10 bis lo escribe así: la ventana «**no se cierra: se hace DETECTABLE** — el
#  recibo se abre antes de ejecutar y una segunda invocación que lo encuentre sin cerrar
#  devuelve `ambiguo`, y la autoridad decide». No tiene cierre por diseño: con un proceso
#  externo cualquiera no existe «exactamente una vez». Lo que SÍ se exige, y es lo que este
#  sabotaje ataca, es que la ambigüedad **se detecte en vez de duplicarse en silencio**.
def m_fd6_el_recibo_abierto_se_reejecuta(raiz):
    """`T191`, `falla_si`: «una caída entre ejecutar y cerrar el recibo duplica el efecto EN
    SILENCIO».

    Se cambia la rama del recibo ABIERTO para que, en vez de devolver `ambiguo`, siga de
    largo y vuelva a lanzar la orden. Es exactamente la duplicación que `FD-6` declara no
    poder cerrar y sí poder detectar: si esta mutación no pusiera nada rojo, la mitad
    DETECTABLE de la deuda estaría escrita y no ejercida, que es la forma en que una deuda
    se cierra en falso.
    """
    _sustituir(raiz, "kernel/operativo/runtime/adaptadores/proceso.py",
               '            return comprobar_resultado({\n                "estado": AMBIGUO,',
               '            pass\n        if False:\n            return comprobar_resultado({\n                "estado": AMBIGUO,')


# ===========================================================================
#  `FD-3` · la especificación normativa que VIAJA al proyecto instalado
# ===========================================================================
#  Ésta es la única de clase `validador`, y se dice por qué: `FD-3` se verifica con `T181` y
#  `T194`, y las dos declaran `comprobar_arranque.py` como su validador. `T181` no tiene hoy
#  implementación en ese validador —el fichero publica `T148`, `T171` y `T194`—, así que la
#  única prueba de `FD-3` que puede ponerse roja es `T194`, y a ella se apunta. Queda dicho
#  en el informe como PETICIÓN, no como omisión.

def m_fd3_el_motor_durable_no_viaja(raiz):
    """`T194`: «el runtime del estado durable viaja con el kernel al proyecto instalado».

    El arranque copia `kernel/operativo` entero. Aquí se le quita el runtime justo después,
    que es la forma en que esto se rompe de verdad: no borrando la copia, sino podándola
    «porque el proyecto no lo necesita». Un proyecto instalado sin motor no puede sostener
    el estado durable que la sección `(g)` le exige, y `T194` lo dice con esas palabras.
    """
    _sustituir(raiz, "tooling/new-project.sh",
               'cp -r "$SRC/kernel/operativo" "$ADS/kernel/"\n',
               'cp -r "$SRC/kernel/operativo" "$ADS/kernel/"\n'
               'rm -rf "$ADS/kernel/operativo/runtime"\n')


CATALOGO.extend([
    Mutacion("N172", "A14", "T172", ESTADO_DURABLE,
             "la guarda de intérprete pasa a poder RELAJARSE por variable de entorno",
             m_a14_la_guarda_se_puede_relajar, clase=BATERIA,
             espera="no supera la mínima declarada"),
    Mutacion("N173", "g.1", "T173", ESTADO_DURABLE,
             "cada evento del diario lleva el `pid` del proceso que lo escribió",
             m_g1_el_diario_lleva_el_pid, clase=BATERIA,
             espera="contiene «\\bpid\\b»"),
    Mutacion("N174", "g.3", "T174", ESTADO_DURABLE,
             "el `.gitignore` del almacén deja de excluir la zona de preparación",
             m_g3_la_zona_de_preparacion_entra_al_versionado, clase=BATERIA,
             espera="'operacional' not found in"),
    Mutacion("N175", "g.8", "T175", ESTADO_DURABLE,
             "el punto de no retorno se adelanta de `preparada` a `abierta`",
             m_g8_el_punto_de_no_retorno_se_adelanta, clase=BATERIA,
             espera="se publicó una transición que debía revertirse"),
    Mutacion("N176", "g.6", "T176", ESTADO_DURABLE,
             "agotar los reintentos se declara por el camino que NO abre el registro",
             m_g6_agotar_reintentos_no_abre_el_registro, clase=BATERIA,
             espera="`ESCRITOR_CONCURRENTE` es el camino que no abre el registro"),
    Mutacion("N177", "g.5", "T177", ESTADO_DURABLE,
             "el `cid` del objeto canónico deja de contrastarse contra `REVISION.json`",
             m_g5_el_cid_deja_de_contrastarse, clase=BATERIA,
             espera="EstadoCorrupto not raised"),
    Mutacion("N178", "g.9", "T178", ESTADO_DURABLE,
             "la cabeza del registro auxiliar deja de anclar su extremo AL LEER",
             m_g9_la_cabeza_no_ancla_en_el_camino_de_lectura, clase=BATERIA,
             espera="no hizo fallar `reconciliacion`: una pendencia se estaría retirando"),
    Mutacion("N179", "g.10", "T179", ESTADO_DURABLE,
             "una versión de formato desconocida se abre en vez de fallar cerrado",
             m_g10_una_version_desconocida_se_adivina, clase=BATERIA,
             espera="FormatoDesconocido not raised"),
    Mutacion("N187", "g.14", "T187", GOBIERNO_GIT,
             "el hook vuelve a tomar el `OID` nulo por «creación» y deja pasar el forzado",
             m_g14_omitir_el_valor_viejo_salta_la_guarda, clase=BATERIA,
             espera="tres argumentos NO pueden ser una vía de forzado"),
    Mutacion("N192", "g.15", "T192", IDENTIDAD,
             "la configuración de confianza puede vivir en un subdirectorio del árbol",
             m_g15_la_configuracion_cabe_dentro_del_arbol, clase=BATERIA,
             espera="ConfiguracionDentroDelArbol not raised"),
    Mutacion("N188", "V6-02", "T188", ADMISION,
             "una salida `-z` truncada se devuelve como si fuera la lista completa",
             m_v6_salida_truncada_pasa_por_completa, clase=BATERIA,
             espera="SalidaTruncada not raised"),
    Mutacion("N189", "V6-11", "T189", ADMISION,
             "el verificador y su política se quedan fuera de su propio alcance",
             m_v6_el_instrumento_se_sale_de_su_alcance, clase=BATERIA,
             espera="any(ruta.startswith(prefijo) for prefijo in prefijos)"),
    Mutacion("N190", "V6-19", "T190", ADMISION,
             "la sede única de fórmulas rompe el caso frontera del fichero VACÍO",
             m_v6_la_sede_de_formulas_rompe_su_frontera, clase=BATERIA,
             espera="la sede de fórmulas no respeta los casos frontera del fichero VACÍO"),
    Mutacion("N211", "V6-15", "T211", ARBOLES,
             "la versión histórica vulnerable deja de aceptar el árbol atacado",
             m_v6_la_version_vulnerable_deja_de_reproducir, clase=BATERIA,
             espera="NO acepta el árbol atacado"),
    Mutacion("N217", "V6-16", "T217", RAIZ_EXTERNA,
             "una instalación de la raíz externa con un fichero ALTERADO emite veredicto",
             m_v6_una_instalacion_alterada_emite_veredicto, clase=BATERIA,
             espera="InstalacionAlterada not raised"),
    Mutacion("N216", "FD-5", "T216", CONTENCION,
             "el backend `simple` se declara con nivel de árbol de procesos",
             m_fd5_el_backend_debil_se_presenta_como_fuerte, clase=BATERIA,
             espera="ContencionFuerteNoDisponible not raised"),
    Mutacion("N191", "FD-6", "T191", ADAPTADORES,
             "un recibo ABIERTO deja de dar `ambiguo` y el efecto se vuelve a ejecutar",
             m_fd6_el_recibo_abierto_se_reejecuta, clase=BATERIA,
             espera="ambiguo"),
    Mutacion("N194", "FD-3", "T194", "comprobar_arranque",
             "el motor de estado durable deja de viajar al proyecto instalado",
             m_fd3_el_motor_durable_no_viaja,
             espera="no lleva el motor de estado durable"),
])
