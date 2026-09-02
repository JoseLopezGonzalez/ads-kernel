#!/usr/bin/env python3
"""validar-f5 — controles pequenos sobre la matriz de F5 y sus borradores.

QUE COMPRUEBA, y nada mas:

  F1  la matriz es YAML valido y tiene las claves de primer nivel obligatorias
  F2  los siete entregables F5-A...F5-G estan declarados, y ninguno sobra
  F3  los siete criterios A1...A7 estan declarados, y ninguno sobra
  F4  todo identificador de fila es unico
  F5  el estado de cada fila esta en `estados_validos`, y NINGUNA fila usa una categoria
      vaga: el vocabulario es cerrado y se comprueba contra el declarado
  F6  COBERTURA DE PRESIONES: el censo VIGENTE se DERIVA del arbol —del barrido de las
      cabeceras `## `PN-` de la sede unica, excluyendo RETIRADA y FUSIONADA— y toda presion
      derivada tiene fila. Ninguna cifra se escribe a mano
  F7  toda fila con `decision_owner: SI` nombra una `decision_id`, y toda fila con
      `decision_owner: NO` no la nombra
  F8  toda `decision_id` de la matriz existe en el paquete de decisiones, y toda decision
      del paquete esta referenciada por al menos una fila. En los dos sentidos: una
      decision sin fila es una pregunta inventada, y una fila sin decision es una
      obligacion que nadie contesta
  F9  todo `artefacto` declarado existe en el arbol
  F10 TODO fichero de docs/f5/borradores/ lleva la marca `ESTADO-DEL-BORRADOR: NO_APROBADO`
      en sus primeras lineas. Un borrador sin marca podria presentarse como aprobado
  F11 NINGUN fichero de docs/f5/ lleva `ESTADO-DEL-BORRADOR: APROBADO`. Este arbol no
      contiene ninguna aprobacion del Owner, y esta comprobacion lo hace comprobable
  F12 todo marcador `PENDIENTE-DECISION-DEL-OWNER: <id>` de un borrador nombra una decision
      que existe en el paquete
  F22 APPEND-ONLY DE LA SEDE DEL OWNER, comprobado contra el COMMIT DE NACIMIENTO y no
      contra HEAD: el contenido de hoy tiene que EMPEZAR por el de la version que creo el
      fichero. Confirmar una alteracion no la vuelve legitima, y por eso la referencia es
      el nacimiento. A2 lo prometia y ningun control lo ejecutaba

  F14 O23 esta INSCRITA y cubre las QUINCE decisiones: sus doce apartados existen, y cada
      identificador D-01..D-10 y R-01..R-05 tiene fila en la matriz con su acto
  F15 LITERALIDAD DE O23: su texto conserva las frases que fijan cada decision. Alterar una
      palabra de las declaradas hace ROJO
  F16 COBERTURA DE PRESIONES CON ACTO: el censo VIGENTE se deriva del arbol y toda presion
      tiene fila en el acta de disposicion, con disposicion y acto que la cierra
  F17 NINGUNA sede afirma que F5 este CERRADA MIENTRAS EL OWNER NO LO HAYA DECLARADO. El
      control NO se retira cuando la fase se cierra: se ANCLA al acto. Se busca en la SEDE
      CANONICA DEL OWNER una resolucion que declare `F5` CERRADA; si no existe, cualquier
      afirmacion de cierre es ROJA, exactamente como antes. Si existe, la afirmacion es
      legitima y el control publica QUE RESOLUCION la sostiene. Se detectan las DOS formas
      de afirmarlo: la frase con verbo y la FILA DE TABLA de la sede del estado, que la
      version anterior no veia y que habria dejado el control vacio en cuanto la fase
      avanzara
  F18 NINGUN contrato de F6 se presenta como IMPLEMENTADO o EJECUTADO SIN CITAR, EN LA
      MISMA LINEA, un fichero de evidencia publicado que EXISTA; y NINGUNO se presenta como
      CERTIFICADO, en ningun sitio y bajo ninguna condicion. Antes de que F6 empezara, la
      regla podia ser «nada»; ahora que construye, «nada» seria falso y «lo que sea» seria
      peor. La condicion es la evidencia, y se comprueba contra el arbol
  F19 PesquerApp sigue declarada BLOQUEADA en la unica sede del estado de fase
  F20 el ESTADO CANONICO, el DIARIO CANONICO y el REGISTRO AUXILIAR de reconciliacion
      permanecen como TRES materias declaradas y separadas en la seccion (g)
  F21 la apertura automatica por politica NO puede eludir el gate constitucional: la sede
      que la reconoce declara expresamente su subordinacion

  F13 el estado de fase NO se copia. Se comprueban DOS cosas, porque una sola no basta:
      (a) el ROTULO de estado aparece a lo sumo en UNA sede, que es
          docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md. «A lo sumo» y no «exactamente»: cuando
          F5 cambie de estado el rotulo desaparecera, y eso NO es un fallo;
      (b) NINGUN otro documento AFIRMA el estado de F5 con sus propias palabras. Es la
          forma por la que el estado se copia de verdad: no repitiendo el rotulo, sino
          escribiendo la frase al lado de la promesa de no copiarlo.
      EL BARRIDO NO SE LIMITA a docs/canonico/: alcanza tambien el indice de la iniciativa
      y todo docs/f5/, que son las zonas donde este macrobloque escribe.
      EXENCION DECLARADA, Y UNA SOLA: docs/f5/01-ACTO-DE-INICIO-DE-F5.md TRANSCRIBE
      literalmente el acto del Owner, que contiene esa frase. Reescribirla seria reescribir
      la orden, que es la misma razon por la que el corpus exime los documentos en voz del
      Owner. La exencion es POR FICHERO y esta escrita aqui, no en una lista aparte.

QUE NO COMPRUEBA, y se dice: no juzga si una clasificacion es correcta, no lee el contenido
de las sedes superiores, no verifica ninguna enmienda y NO CERTIFICA NADA. Un verde de aqui
no aprueba ninguna decision y no cierra ninguna fila.

LIMITACION HEREDADA, DECLARADA Y NO OCULTADA. Este fichero es codigo ejecutable sin guarda
de integridad: no esta en el manifiesto de validadores del kernel y no entra en la huella.
Es exactamente la limitacion CD-3 que el corpus registra de
docs/canonico/validar-fuentes-canonicas.py. NO se corrige aqui: meterlo en el manifiesto o
en la huella exige tocar kernel/ o tooling/, y CD-3 pertenece al endurecimiento instrumental
de F6. Se declara para que nadie lo cuente como garantia que no da.

Uso:
  python3 docs/f5/validar-f5.py [--raiz DIR] [--json]

Codigos de salida:  0 sin fallos  ·  1 hay fallos  ·  2 no se pudo empezar
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:                                          # pragma: no cover
    print("validar-f5 requiere PyYAML", file=sys.stderr)
    sys.exit(2)

# La raiz se deriva de la ubicacion de este fichero y de nada mas. No se usa el cwd: es la
# leccion que la bateria del corpus aprendio por un defecto real.
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

MATRIZ = "docs/f5/MATRIZ-F5.yml"
PAQUETE = "docs/f5/20-PAQUETE-DE-DECISIONES-DEL-OWNER.md"
BORRADORES = "docs/f5/borradores"
SEDE_DEL_ESTADO = "docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md"
DIR_CANONICO = "docs/canonico"
# Las zonas donde este macrobloque escribe, y por tanto donde puede copiar un estado.
ZONAS_DEL_BARRIDO = ("docs/canonico", "docs/f5")
INDICE_INICIATIVA = "docs/evolucion/00-INDICE.md"
# La UNICA exencion, y su motivo esta en el docstring: transcribe el acto del Owner.
EXENTO_POR_TRANSCRIPCION = "docs/f5/01-ACTO-DE-INICIO-DE-F5.md"
SEDE_PRESIONES = "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md"
SEDE_OWNER = "docs/owner/ADS-OWNER-RESOLUCIONES.md"
ACTA_PRESIONES = "docs/f5/40-DISPOSICION-DE-LAS-PRESIONES.md"
SECCION_G = "docs/rediseno/g-ESTADO-DURABLE-APROBADA.md"
ENMIENDA_ARRANQUE = "docs/rediseno/a-ENMIENDA-E3-ARRANQUE-Y-POLITICA.md"

# Las QUINCE decisiones que O23 resuelve.
DECISIONES_O23 = [f"D-{n:02d}" for n in range(1, 11)] + [f"R-{n:02d}" for n in range(1, 6)]

# Frases de O23 cuya alteracion cambiaria una decision. Se comprueban LITERALES.
LITERAL_O23 = [
    "Se adopta una sección `(g)` normativa breve y un contrato derivado que `F6` deberá implementar.",
    "La norma de la raíz externa de confianza forma parte de `(g)` y tendrá un contrato derivado propio para `F6`.",
    "Al agotarse los reintentos se escribirá un registro operativo auxiliar durable, separado del estado canónico y del diario canónico.",
    "Se conserva el gate constitucional de arranque. El circuito nuevo queda subordinado a él.",
    "Se reconoce una tercera vía de nacimiento del trabajo: apertura automática por una política previamente aprobada.",
    "Verificación es participante condicional y productora del dictamen en la ruta de auditoría.",
    "manda la grafía con tilde de la fuente aprobada",
    "El mapa documental se satisface mediante una derivación mecánica reproducible.",
    "`F5` sólo podrá declararse cerrada mediante un acto posterior y expreso del Owner",
    "Esta resolución no declara `F5` cerrada, no implementa contratos de `F6` y no autoriza el inicio de PesquerApp.",
]

# Afirmaciones de cierre de F5. Las DOS formas: la frase con verbo, y la FILA DE TABLA de
# la sede del estado —«| **`F5`** | **CERRADA**»—, que no lleva verbo y que la version
# anterior no detectaba.
PROHIBIDO_F5_CERRADA = re.compile(
    r"`?F5`?\s+(?:queda|está|esta|ha quedado)\s+\**\s*CERRADA"
    r"|\|\s*\**\s*`?F5`?\s*\**\s*\|\s*\**\s*CERRADA", re.IGNORECASE)
# EL ACTO que las legitima, buscado en la SEDE CANONICA DEL OWNER y en ningun otro sitio.
# Sin acto, toda afirmacion de cierre sigue siendo ROJA.
ACTO_DE_CIERRE_DE_F5 = re.compile(r"^Declaro\s+`?F5`?\s+CERRADA\.", re.M)
PROHIBIDO_F6_IMPLEMENTADO = re.compile(
    r"(?:contrato|verificador|runtime)[^.\n]{0,60}\b(?:ya\s+)?(?:está|esta)\s+\**\s*"
    r"(?:IMPLEMENTAD|EJECUTAD|CERTIFICAD)", re.IGNORECASE)
# CERTIFICADO no admite excusa: la certificacion de F6 la emite un juicio independiente y no
# quien construyo —criterio B6—, y hoy no existe ninguno.
AFIRMA_CERTIFICADO = re.compile(r"CERTIFICAD", re.IGNORECASE)
# La UNICA prueba que legitima «implementado» o «ejecutado»: la linea cita un fichero de
# evidencia publicado, y ese fichero existe en el arbol. Una afirmacion sin evidencia citada
# es exactamente lo que este control existe para impedir.
CITA_DE_EVIDENCIA = re.compile(r"(kernel/operativo/pruebas/evidencia/[A-Za-z0-9._-]+)"
                               r"|(?:evidencia/)([A-Za-z0-9._-]+\.txt)")
# Una NEGACION no es una afirmacion de haberlo construido. Es la diferencia entre «esta
# implementado» y «nada esta implementado», y confundirlas haria inutil el control.
NEGACION = re.compile(r"\b(?:no|ninguno|ninguna|nada|ningún|ningun|sin)\b", re.IGNORECASE)
# Un CRITERIO DE ACEPTACION enuncia lo que habra que demostrar, no lo que ya se demostro.
# «B1 cada contrato esta IMPLEMENTADO» es la vara de F6, no una afirmacion de F5.
CRITERIO = re.compile(r"^\s*[AB]\d+\s")

CLAVES = ("version", "descripcion", "derivacion", "entregables",
          "criterios_de_aceptacion", "estados_validos", "filas")

ENTREGABLES = ("F5-A", "F5-B", "F5-C", "F5-D", "F5-E", "F5-F", "F5-G")
CRITERIOS = ("A1", "A2", "A3", "A4", "A5", "A6", "A7")

MARCA_NO_APROBADO = "ESTADO-DEL-BORRADOR: NO_APROBADO"
MARCA_APROBADO = "ESTADO-DEL-BORRADOR: APROBADO"
RE_PENDIENTE = re.compile(r"PENDIENTE-DECISION-DEL-OWNER:\s*([DR]-[0-9]{2})")
RE_DECISION_PAQUETE = re.compile(r"^#{2,3}\s+`([DR]-[0-9]{2})`", re.M)
# La cabecera de una presion en su sede unica. El censo se DERIVA de aqui.
RE_PRESION = re.compile(r"^## `(PN-[0-9]+)` ·(.*)$", re.M)


class Resultado:
    def __init__(self):
        self.fallos = []
        self.datos = {}

    def fallo(self, control, msg):
        self.fallos.append(f"{control} · {msg}")


def _leer(raiz, rel):
    with open(os.path.join(raiz, rel), encoding="utf-8") as fh:
        return fh.read()


def presiones_vigentes(raiz):
    """El censo VIGENTE, DERIVADO del arbol. Excluye RETIRADA y FUSIONADA."""
    texto = _leer(raiz, SEDE_PRESIONES)
    vivas = []
    for ident, resto in RE_PRESION.findall(texto):
        if "RETIRADA" in resto or "FUSIONADA" in resto:
            continue
        vivas.append(ident)
    return vivas


def validar(raiz):
    r = Resultado()

    # ---- F1 -------------------------------------------------------------
    ruta_matriz = os.path.join(raiz, MATRIZ)
    if not os.path.exists(ruta_matriz):
        print(f"no se encuentra {MATRIZ}", file=sys.stderr)
        sys.exit(2)
    try:
        m = yaml.safe_load(_leer(raiz, MATRIZ))
    except yaml.YAMLError as exc:
        r.fallo("F1", f"la matriz no es YAML valido: {exc}")
        return r
    for clave in CLAVES:
        if clave not in m:
            r.fallo("F1", f"falta la clave de primer nivel `{clave}`")
    if r.fallos:
        return r

    filas = m["filas"]
    validos = set(m["estados_validos"])
    r.datos["filas"] = len(filas)
    reparto = {}
    for f in filas:
        reparto[f.get("estado")] = reparto.get(f.get("estado"), 0) + 1
    r.datos["reparto_por_estado"] = " · ".join(
        f"{k} {v}" for k, v in sorted(reparto.items(), key=lambda kv: -kv[1]))
    r.datos["estados_validos"] = len(validos)

    # ---- F2 · los siete entregables -------------------------------------
    declarados = [e["id"] for e in m["entregables"]]
    if sorted(declarados) != sorted(ENTREGABLES):
        r.fallo("F2", f"los entregables declarados no son F5-A...F5-G: {declarados}")
    r.datos["entregables"] = len(declarados)

    # ---- F3 · los siete criterios ---------------------------------------
    crits = [c["id"] for c in m["criterios_de_aceptacion"]]
    if sorted(crits) != sorted(CRITERIOS):
        r.fallo("F3", f"los criterios declarados no son A1...A7: {crits}")
    r.datos["criterios"] = len(crits)

    # ---- F4 · unicidad ---------------------------------------------------
    ids = [f["id"] for f in filas]
    repes = {i for i in ids if ids.count(i) > 1}
    if repes:
        r.fallo("F4", f"identificadores de fila repetidos: {sorted(repes)}")

    # ---- F5 · vocabulario cerrado de estados -----------------------------
    for f in filas:
        if f.get("estado") not in validos:
            r.fallo("F5", f"{f['id']}: estado `{f.get('estado')}` fuera del vocabulario "
                          f"declarado. Una fila sin ubicacion inequivoca es el defecto")

    # ---- F6 · cobertura de presiones, DERIVADA ---------------------------
    vivas = presiones_vigentes(raiz)
    r.datos["presiones_vigentes_derivadas"] = len(vivas)
    cubiertas = {f["presion"] for f in filas if f.get("presion")}
    sin_fila = [p for p in vivas if p not in cubiertas]
    if sin_fila:
        r.fallo("F6", f"presiones VIGENTES sin fila en la matriz: {sin_fila}. El censo se "
                      f"deriva del arbol, y la matriz tiene que cubrirlo entero")
    sobran = [p for p in sorted(cubiertas) if p not in vivas]
    if sobran:
        r.fallo("F6", f"la matriz cubre presiones que su sede NO declara vigentes: {sobran}")

    # ---- F7 · coherencia decision_owner / decision_id --------------------
    for f in filas:
        tiene = bool(f.get("decision_id"))
        if f.get("decision_owner") == "SI" and not tiene:
            r.fallo("F7", f"{f['id']}: declara decision del Owner y no nombra `decision_id`")
        if f.get("decision_owner") == "NO" and tiene:
            r.fallo("F7", f"{f['id']}: no declara decision del Owner y nombra `decision_id`")

    # ---- F8 · el paquete y la matriz se cubren en los DOS sentidos -------
    ruta_paquete = os.path.join(raiz, PAQUETE)
    if not os.path.exists(ruta_paquete):
        r.fallo("F8", f"no existe el paquete de decisiones {PAQUETE}")
        del_paquete = set()
    else:
        del_paquete = set(RE_DECISION_PAQUETE.findall(_leer(raiz, PAQUETE)))
    de_la_matriz = {f["decision_id"] for f in filas if f.get("decision_id")}
    r.datos["decisiones_en_el_paquete"] = len(del_paquete)
    huerfanas = sorted(de_la_matriz - del_paquete)
    if huerfanas:
        r.fallo("F8", f"la matriz nombra decisiones que el paquete no plantea: {huerfanas}")
    inventadas = sorted(del_paquete - de_la_matriz)
    if inventadas:
        r.fallo("F8", f"el paquete plantea decisiones que ninguna fila necesita: "
                      f"{inventadas}. Una pregunta sin obligacion detras es una pregunta "
                      f"inventada")

    # ---- F9 · los artefactos declarados existen --------------------------
    for f in filas:
        art = f.get("artefacto")
        if art and not os.path.exists(os.path.join(raiz, art)):
            r.fallo("F9", f"{f['id']}: el artefacto declarado no existe: {art}")

    # ---- F10 y F12 · los borradores -------------------------------------
    dir_b = os.path.join(raiz, BORRADORES)
    n_borr = 0
    if os.path.isdir(dir_b):
        for nombre in sorted(os.listdir(dir_b)):
            if not nombre.endswith(".md"):
                continue
            n_borr += 1
            rel = f"{BORRADORES}/{nombre}"
            texto = _leer(raiz, rel)
            if MARCA_NO_APROBADO not in "\n".join(texto.splitlines()[:20]):
                r.fallo("F10", f"{rel}: sin la marca `{MARCA_NO_APROBADO}` en sus primeras "
                               f"veinte lineas. Un borrador sin marca puede presentarse "
                               f"como material aprobado")
            for ident in RE_PENDIENTE.findall(texto):
                if ident not in del_paquete:
                    r.fallo("F12", f"{rel}: el marcador nombra `{ident}`, que el paquete "
                                   f"no plantea")
    r.datos["borradores"] = n_borr

    # ---- F11 · nada esta aprobado en este arbol --------------------------
    for base, _dirs, ficheros in os.walk(os.path.join(raiz, "docs/f5")):
        for nombre in ficheros:
            ruta = os.path.join(base, nombre)
            rel = os.path.relpath(ruta, raiz).replace(os.sep, "/")
            if not nombre.endswith((".md", ".yml")):
                continue
            if MARCA_APROBADO in _leer(raiz, rel):
                r.fallo("F11", f"{rel}: contiene `{MARCA_APROBADO}`. Este arbol no puede "
                               f"contener ninguna aprobacion del Owner")

    # ---- F14 · O23 inscrita y cubriendo las quince -----------------------
    ruta_owner = os.path.join(raiz, SEDE_OWNER)
    o23 = ""
    if not os.path.exists(ruta_owner):
        r.fallo("F14", f"no existe la sede canonica del Owner {SEDE_OWNER}")
    else:
        texto_owner = _leer(raiz, SEDE_OWNER)
        if "# `O23`" not in texto_owner:
            r.fallo("F14", "O23 NO esta inscrita en la sede canonica del Owner")
        else:
            resto = texto_owner[texto_owner.index("# `O23`"):]
            # ACOTADO a la siguiente resolucion. Sin esto, el acto de cierre de F5 —que
            # sera una resolucion posterior— pondria este control en rojo por existir.
            sig = re.search(r"^# `O(?!23`)", resto[1:], re.M)
            o23 = resto[:sig.start() + 1] if sig else resto
            apartados = len(re.findall(r"^## \d+ · ", o23, re.M))
            r.datos["apartados_de_o23"] = apartados
            if apartados != 12:
                r.fallo("F14", f"O23 declara {apartados} apartados y su alcance exige 12")
    sin_fila = [d for d in DECISIONES_O23 if d not in de_la_matriz]
    r.datos["decisiones_de_o23_con_fila"] = len(DECISIONES_O23) - len(sin_fila)
    if sin_fila:
        r.fallo("F14", f"decisiones que O23 resuelve y ninguna fila de la matriz recoge: "
                       f"{sin_fila}. Retirar una decision de O23 deja su obligacion sin acto")

    falsos = [f["id"] for f in filas
              if f.get("estado") == "APLICADO_POR_O23"
              and str(f.get("artefacto") or "").startswith(f"{BORRADORES}/")]
    if falsos:
        r.fallo("F14", f"filas APLICADAS cuyo artefacto es un BORRADOR: {falsos}. Un borrador "
                       f"NO_APROBADO no puede ser el instrumento que aplica una decision")

    # ---- F22 · append-only contra el NACIMIENTO --------------------------
    try:
        nac = subprocess.run(["git", "-C", raiz, "log", "--diff-filter=A", "--format=%H",
                              "--", SEDE_OWNER], capture_output=True, text=True, timeout=30)
        commits = [c for c in nac.stdout.split() if c]
        if not commits:
            r.datos["append_only"] = "sin historia: no comprobado"
        else:
            nacimiento = commits[-1]
            orig = subprocess.run(["git", "-C", raiz, "show", f"{nacimiento}:{SEDE_OWNER}"],
                                  capture_output=True, timeout=30).stdout
            hoy = open(os.path.join(raiz, SEDE_OWNER), "rb").read()
            r.datos["append_only"] = f"contra {nacimiento[:8]}: " + (
                "OK" if hoy.startswith(orig) else "ROTO")
            if not hoy.startswith(orig):
                r.fallo("F22", f"la sede del Owner YA NO EMPIEZA por el contenido del commit "
                               f"que la creo ({nacimiento[:8]}). Es append-only, y confirmar "
                               f"una alteracion no la vuelve legitima")
    except Exception as exc:                                     # pragma: no cover
        r.datos["append_only"] = f"no comprobado: {exc}"

    # ---- F15 · literalidad de O23 ----------------------------------------
    if o23:
        faltan = [f for f in LITERAL_O23 if f not in o23]
        r.datos["frases_literales_de_o23"] = len(LITERAL_O23) - len(faltan)
        if faltan:
            r.fallo("F15", f"O23 ha perdido {len(faltan)} de sus frases decisorias literales. "
                           f"La primera que falta: {faltan[0][:70]!r}")

    # ---- F16 · toda presion vigente con disposicion y acto ---------------
    if not os.path.exists(os.path.join(raiz, ACTA_PRESIONES)):
        r.fallo("F16", f"no existe el acta de disposicion {ACTA_PRESIONES}")
    else:
        acta = _leer(raiz, ACTA_PRESIONES)
        # Se leen TRES columnas: identificador, disposicion y ACTO que la cierra.
        filas_acta = {m[0]: (m[1], m[2]) for m in re.findall(
            r"^\| `(PN-\d+)` \| \*\*([^*]+)\*\* \| ([^|]*)\|", acta, re.M)}
        r.datos["presiones_en_el_acta"] = len(filas_acta)
        sin_acta = [p for p in vivas if p not in filas_acta]
        if sin_acta:
            r.fallo("F16", f"presiones VIGENTES sin fila en el acta de disposicion: {sin_acta}")
        # `startswith` y NO `in`: «NO RESUELTA» contiene «RESUELTA», y aceptarla seria
        # dar por cerrada una presion que el acta declara abierta.
        sin_resolver = [p for p, (d, _a) in filas_acta.items()
                        if not (d.strip().startswith("RESUELTA")
                                or d.strip().startswith("RETIRADA"))]
        if sin_resolver:
            r.fallo("F16", f"presiones sin disposicion inequivoca en el acta: {sin_resolver}")
        sin_acto = [p for p, (_d, a) in filas_acta.items() if not a.strip()]
        if sin_acto:
            r.fallo("F16", f"presiones cuyo ACTO de cierre esta vacio en el acta: {sin_acto}. "
                           f"Una disposicion sin acto es una presion sin cerrar")

    # ---- F17 · nadie declara F5 cerrada SIN ACTO DEL OWNER ---------------
    # El acto se busca en la sede canonica y se atribuye a la resolucion que lo contiene.
    # Que el acto exista NO retira el control: lo ancla. Sin acto, todo sigue en rojo.
    acto, resolucion_del_acto = False, None
    if os.path.exists(ruta_owner):
        texto_owner = _leer(raiz, SEDE_OWNER)
        m_acto = ACTO_DE_CIERRE_DE_F5.search(texto_owner)
        if m_acto:
            acto = True
            cabeceras = re.findall(r"^# `(O\d+)`", texto_owner[:m_acto.start()], re.M)
            resolucion_del_acto = cabeceras[-1] if cabeceras else "sin resolucion"
    r.datos["acto_de_cierre_de_F5"] = (
        f"{resolucion_del_acto} · en {SEDE_OWNER}" if acto else "NO EMITIDO")

    # Se recorre F5, el corpus canonico y el material aprobado nuevo.
    ambito = []
    for zona in ("docs/f5", "docs/canonico", "docs/rediseno"):
        for base, _d, ficheros in os.walk(os.path.join(raiz, zona)):
            for nombre in sorted(ficheros):
                if nombre.endswith(".md"):
                    ambito.append(os.path.relpath(os.path.join(base, nombre),
                                                  raiz).replace(os.sep, "/"))
    r.datos["ficheros_barridos_por_F17"] = len(ambito)
    for rel in ambito:
        texto = _leer(raiz, rel)
        for m in PROHIBIDO_F5_CERRADA.finditer(texto):
            # `F6` exige `F5` CERRADA es una CONDICION, no una declaracion de estado
            ventana = texto[max(0, m.start() - 90):m.start()]
            if "exige" in ventana or "sólo podrá" in ventana or "solo podra" in ventana:
                continue
            if acto:
                # Hay acto competente del Owner: la afirmacion no adelanta nada.
                continue
            r.fallo("F17", f"{rel}: declara `F5` CERRADA y la sede canonica del Owner NO "
                           f"contiene el acto que la cierra. Su cierre exige un acto "
                           f"posterior y expreso del Owner, y ningun artefacto puede "
                           f"adelantarlo")
            break

    # ---- F18 · ningun contrato de F6 presentado como implementado --------
    for rel in ambito:
        texto = _leer(raiz, rel)
        for m in PROHIBIDO_F6_IMPLEMENTADO.finditer(texto):
            # se mira la frase entera: una negacion delante invierte el sentido
            ini = texto.rfind("\n", 0, m.start()) + 1
            linea = texto[ini:texto.find("\n", m.end()) if texto.find("\n", m.end()) > 0 else len(texto)]
            if NEGACION.search(texto[ini:m.end()]) or CRITERIO.match(linea):
                continue
            if AFIRMA_CERTIFICADO.search(m.group(0)):
                r.fallo("F18", f"{rel}: presenta como CERTIFICADO algo que es CONTRATO de "
                               f"F6. La certificacion la emite un juicio independiente y no "
                               f"quien construyo, y hoy no existe ninguno: {m.group(0)[:60]!r}")
                break
            citadas = [g for par in CITA_DE_EVIDENCIA.findall(linea) for g in par if g]
            existentes = [c for c in citadas
                          if os.path.exists(os.path.join(raiz, c))
                          or os.path.exists(os.path.join(
                              raiz, "kernel/operativo/pruebas/evidencia", os.path.basename(c)))]
            if existentes:
                # La afirmacion se sostiene en evidencia PUBLICADA que existe. No se juzga
                # aqui si esa evidencia es suficiente: eso lo hace la bateria del kernel.
                continue
            r.fallo("F18", f"{rel}: presenta como implementado o ejecutado algo que es "
                           f"CONTRATO de F6 SIN citar en la misma linea un fichero de "
                           f"evidencia publicado que exista: {m.group(0)[:60]!r}")
            break

    # ---- F19 · PesquerApp sigue bloqueada --------------------------------
    sede_estado = _leer(raiz, SEDE_DEL_ESTADO)
    if not re.search(r"PesquerApp\*\*\s*\|\s*\*\*BLOQUEADA", sede_estado):
        r.fallo("F19", f"{SEDE_DEL_ESTADO} ya no declara PesquerApp BLOQUEADA en la unica "
                       f"sede del estado de fase")

    # ---- F20 · las tres materias del estado durable, separadas -----------
    if not os.path.exists(os.path.join(raiz, SECCION_G)):
        r.fallo("F20", f"no existe la seccion (g) en {SECCION_G}")
    else:
        g = _leer(raiz, SECCION_G)
        for materia in ("ESTADO CANÓNICO", "DIARIO CANÓNICO", "REGISTRO OPERATIVO"):
            if materia not in g:
                r.fallo("F20", f"la seccion (g) ya no declara la materia {materia!r}")
        if "I-g7" not in g:
            r.fallo("F20", "la seccion (g) ya no declara el invariante que mantiene separados "
                           "el estado canonico, el diario y el registro auxiliar")
        g_plano = " ".join(g.split())
        if "Ninguna implementación puede colapsarlas" not in g_plano:
            r.fallo("F20", "la seccion (g) ya no prohibe colapsar las tres materias en una "
                           "sola estructura")
        if "no es** estado canónico" not in g and "NO es estado canónico" not in g:
            r.fallo("F20", "la seccion (g) ya no declara que el registro auxiliar NO es "
                           "estado canonico: mezclarlos rompe la separacion que O23 exige")

    # ---- F21 · la apertura por politica no elude el gate constitucional --
    if not os.path.exists(os.path.join(raiz, ENMIENDA_ARRANQUE)):
        r.fallo("F21", f"no existe la enmienda de arranque {ENMIENDA_ARRANQUE}")
    else:
        e3 = _leer(raiz, ENMIENDA_ARRANQUE)
        if "NO ELUDE EL GATE CONSTITUCIONAL" not in e3.upper():
            r.fallo("F21", "la enmienda que reconoce la apertura automatica por politica ya "
                           "no declara su subordinacion al gate constitucional")
        # UNA FILA por regla, no una mencion en prosa: la prueba posterior lo exige asi,
        # y una mencion suelta dejaria pasar la declaracion global que la enmienda prohibe.
        faltan_reglas = [f"G{n}" for n in range(20, 24)
                         if not re.search(rf"^\| \*\*`G{n}`\*\*", e3, re.M)]
        if faltan_reglas:
            r.fallo("F21", f"la enmienda no nombra {faltan_reglas}, y su prueba posterior "
                           f"exige UNA FILA POR REGLA, no una declaracion global")
        fuente = _leer(raiz, "docs/rediseno/a-CAPACIDADES-APROBADA.md")
        if "CONSERVADAS, y subordinantes" not in fuente:
            r.fallo("F21", "la fuente aprobada ya no remite a la disposicion de las reglas "
                           "constitucionales: la enmienda quedaria sin marca en su sede")

    # ---- F13 · una sola sede para el estado de fase ----------------------
    rotulo = re.compile(r"INICIADA\s*·\s*EN CURSO|COMPLETADA TÉCNICAMENTE")
    # La forma en que un estado se copia de verdad: afirmandolo con palabras propias.
    afirmacion = re.compile(r"`?F5`?\s+(?:est[aá]|queda|sigue)\s+\**\s*(?:EN CURSO|INICIADA)",
                            re.IGNORECASE)

    candidatos = []
    for zona in ZONAS_DEL_BARRIDO:
        for base, _dirs, ficheros in os.walk(os.path.join(raiz, zona)):
            for nombre in sorted(ficheros):
                if nombre.endswith(".md"):
                    candidatos.append(os.path.relpath(os.path.join(base, nombre),
                                                      raiz).replace(os.sep, "/"))
    if os.path.exists(os.path.join(raiz, INDICE_INICIATIVA)):
        candidatos.append(INDICE_INICIATIVA)

    con_rotulo, con_afirmacion = [], []
    for rel in sorted(set(candidatos)):
        texto = _leer(raiz, rel)
        if rotulo.search(texto):
            con_rotulo.append(rel)
        if rel != EXENTO_POR_TRANSCRIPCION and afirmacion.search(texto):
            con_afirmacion.append(rel)

    r.datos["ficheros_barridos_por_F13"] = len(set(candidatos))
    r.datos["sedes_con_el_rotulo_de_estado"] = len(con_rotulo)
    if [x for x in con_rotulo if x != SEDE_DEL_ESTADO]:
        r.fallo("F13", f"el rotulo de estado de `F5` aparece fuera de su unica sede: "
                       f"{[x for x in con_rotulo if x != SEDE_DEL_ESTADO]}. Su sede es "
                       f"{SEDE_DEL_ESTADO}")
    if [x for x in con_afirmacion if x != SEDE_DEL_ESTADO]:
        r.fallo("F13", f"estos documentos AFIRMAN el estado de `F5` con sus propias "
                       f"palabras: {[x for x in con_afirmacion if x != SEDE_DEL_ESTADO]}. "
                       f"Un estado copiado caduca solo en cuanto la fase avanza")
    return r


def main():
    ap = argparse.ArgumentParser(description="controles de la matriz de F5")
    ap.add_argument("--raiz", default=RAIZ)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    raiz = os.path.abspath(args.raiz)

    r = validar(raiz)

    if args.json:
        print(json.dumps({"fallos": r.fallos, "datos": r.datos}, ensure_ascii=False, indent=2))
    else:
        print("CONTROLES DE LA MATRIZ DE F5")
        for clave, valor in r.datos.items():
            print(f"  {clave:34s}: {valor}")
        print()
        for f in r.fallos:
            print(f"  FALLO  {f}")
        print()
        print(f"{len(r.fallos)} fallos")
    return 1 if r.fallos else 0


if __name__ == "__main__":
    sys.exit(main())
