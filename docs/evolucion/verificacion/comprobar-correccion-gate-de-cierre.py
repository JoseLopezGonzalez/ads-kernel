#!/usr/bin/env python3
"""Bateria mecanica de la correccion del gate de cierre de F4c.

Cada comprobacion DERIVA su resultado del arbol. Ninguna cifra esta escrita a mano:
las que aparecen abajo son las EXIGIDAS, y el fallo se produce cuando lo derivado difiere.
"""
from __future__ import annotations
import io, os, re, subprocess, sys
from collections import Counter

# La raíz se DERIVA de `__file__` y de nada más.
#
# Este fichero vive en `docs/evolucion/verificacion/`, luego la raíz del repositorio está
# TRES niveles por encima. No se usa el cwd —una batería que dependiera de desde dónde se
# invoca no sería auditable—, y no se codifica la ruta de ninguna máquina: la versión
# anterior caía a `/home/jose/ads-kernel` y, en cualquier otro clon o worktree, comprobaba
# el repositorio del autor en vez del que tenía delante. Eso hacía que la batería diera
# verde sobre un árbol que nadie estaba mirando.
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir, os.pardir, os.pardir))

_ESPERADOS = ("docs/evolucion", "docs/rediseno", "kernel/operativo")
_faltan = [d for d in _ESPERADOS if not os.path.isdir(os.path.join(RAIZ, d))]
if _faltan:
    sys.stderr.write(
        f"ESTRUCTURA NO ENCONTRADA bajo la raíz derivada de __file__.\n"
        f"  raíz derivada : {RAIZ}\n"
        f"  script        : {os.path.abspath(__file__)}\n"
        f"  faltan        : {', '.join(_faltan)}\n"
        f"Esta batería espera vivir en `docs/evolucion/verificacion/` dentro del "
        f"repositorio ADS. No se adivina otra raíz ni se recurre al cwd: comprobar un "
        f"árbol que no es el que se pidió comprobar es peor que no comprobar nada.\n")
    sys.exit(2)
D11 = os.path.join(RAIZ, "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md")
DEC = os.path.join(RAIZ, "docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md")
CHK = os.path.join(RAIZ, "docs/evolucion/CHECKPOINT-ADS-NEXT.md")
IDX = os.path.join(RAIZ, "docs/evolucion/00-INDICE.md")

def leer(p): return io.open(p, encoding="utf-8").read()
def lineas(p): return leer(p).split("\n")

# ── lexicón de numerales, compartido por varias comprobaciones ───────────
_PALABRA = {
    "cero": 0, "una": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12,
    "trece": 13, "catorce": 14, "quince": 15, "dieciseis": 16, "diecisiete": 17,
    "dieciocho": 18, "diecinueve": 19, "veinte": 20, "treinta": 30, "cuarenta": 40,
    "cincuenta": 50, "sesenta": 60,
}
_ACENTOS = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")

def _num(txt):
    """Convierte a entero un numeral en dígitos o en letra, con decenas compuestas."""
    t = txt.translate(_ACENTOS).lower().strip()
    if t.isdigit():
        return int(t)
    partes = [w for w in re.split(r"\s+y\s+|\s+", t) if w]
    if len(partes) == 1:
        return _PALABRA.get(partes[0])
    if len(partes) == 2 and partes[0] in _PALABRA and partes[1] in _PALABRA:
        d, u = _PALABRA[partes[0]], _PALABRA[partes[1]]
        if d >= 20 and u < 10:
            return d + u
    return None

RES = []
def check(id_, titulo, ok, detalle=""):
    RES.append((id_, titulo, bool(ok), detalle))

# ── secciones de 11, para localizar cada linea ────────────────────────────
def secciones(ls):
    out = []
    for i, l in enumerate(ls, 1):
        m = re.match(r'^#{1,4} (?:§)?([0-9]+(?:\.[0-9]+)*) ·', l)
        if m: out.append((i, m.group(1)))
    return out
L11 = lineas(D11); S11 = secciones(L11)
def sec_de(n):
    cur = "?"
    for i, name in S11:
        if i <= n: cur = name
        else: break
    return cur

t11 = leer(D11)

# ── G-01 · cero `estado/cuarentena/` VIGENTE ─────────────────────────────
# Una mencion es VIGENTE si su ENTORNO no declara la retirada. La comprobacion es
# por PARRAFO y no por linea, porque el texto se ajusta a 96 columnas y la palabra
# «RETIRADA» cae con frecuencia en la linea siguiente a la de la ruta.
# Las menciones que quedan son la nota de correccion de §2.6.9 y la fila `D87` del
# registro: las dos DECLARAN la retirada, y son texto historico, no norma.
parrafos11 = re.split(r"\n\s*\n", t11)
vig = []
for par in parrafos11:
    if "estado/cuarentena" not in par: continue
    if re.search(r"RETIRADA|se resuelve sin crear una tercera fuente", par, re.I):
        continue
    vig.append(par.strip()[:80])
n_menc = sum(1 for l in L11 if "estado/cuarentena" in l)
check("G-01", "cero `estado/cuarentena/` VIGENTE: toda mencion que queda declara su retirada",
      not vig, f"{n_menc} menciones, en {sum(1 for p_ in parrafos11 if 'estado/cuarentena' in p_)} "
               f"parrafos, y todos declaran la retirada" if not vig
               else f"VIGENTES SIN RETIRAR: {vig}")

# ── G-02 · `.ads/run/quarantine/` clasificado y con ciclo ────────────────
q = "`.ads/run/quarantine/"
faltan = []
if q not in t11: faltan.append("no aparece")
# clasificado en §2.4
s24 = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "2.4")
if "quarantine" not in s24: faltan.append("no clasificado en §2.4")
if "OPERACIONAL" not in s24: faltan.append("§2.4 sin plano operacional")
# listado en §2.3
s23 = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "2.3")
if "quarantine" not in s23: faltan.append("no listado en §2.3")
# ciclo: crea antes de restaurar / verifica por hash / elimina despues del commit
s269 = "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "2.6.9")
for frase, etq in [("ANTES de restaurar", "crear antes de restaurar"),
                   ("POR HASH", "verificar por hash"),
                   ("commit del incidente", "eliminar tras el commit")]:
    if frase not in s269: faltan.append("§2.6.9 sin " + etq)
# no canonica y no fuente de verdad
if "NO CANÓNICA" not in s269 and "no canónica" not in s269.lower(): faltan.append("sin declarar no canonica")
if "NO es fuente de verdad" not in s269: faltan.append("sin declarar que no es fuente de verdad")
if "SEG" not in s269: faltan.append("sin el bloqueo de SEG")
check("G-02", "`.ads/run/quarantine/` clasificado, con ciclo y sin ser fuente de verdad",
      not faltan, "; ".join(faltan) or "plano, arbol, ciclo, hash, SEG y perdida aceptada")

# ── G-03 · `estado/deriva/` con las siete piezas ────────────────────────
piezas = {
  "arbol §2.3":        "deriva/<ID>.abierta" in s23,
  "excepcion §2.4":    "estado/deriva" in s24,
  "ignore en positivo": bool(re.search(r"NADA de `estado/deriva/`", t11)),
  "reconstruccion §2.9": bool(re.search(r"\| el marcador `estado/deriva/<ID>\.abierta` \|", t11)),
  "creacion paso E":   "crear su marcador `estado/deriva/<ID>.abierta`" in t11,
  "retirada":          "se retira\n                   `estado/deriva/<ID>.abierta`" in t11
                        or "**se retira\n" in t11 or "retira\n                   `estado/deriva" in t11
                        or "lo RETIRA la transacción CERRADA" in t11,
  "prueba adversarial": "`X59`" in t11 and "`X60`" in t11,
}
check("G-03", "`estado/deriva/` en arbol, excepcion, ignore, reconstruccion, creacion, retirada y prueba",
      all(piezas.values()), ", ".join(k for k, v in piezas.items() if not v) or "las siete")

# ── G-04 · predicado `abierta(tx)` unico: ninguna sede lo redeclara ──────
redecl = []
for i, l in enumerate(L11, 1):
    if sec_de(i) == "2.6.1": continue
    if re.search(r"durable y SIN `derivada`", l) or re.search(r"`preparada` durable y SIN `derivada`", l):
        redecl.append(i)
citas = sorted({sec_de(i) for i, l in enumerate(L11, 1)
                if "abierta(tx)" in l and sec_de(i) not in ("2.6.1", "15.8")})
check("G-04", "predicado `abierta(tx)` UNICO: ninguna sede vigente lo redeclara",
      not redecl, f"sedes que lo citan y remiten: {citas}" if not redecl else f"redeclaran: {redecl}")

# ── G-05 · cero reglas de intentos/agotado en la capa B ────────────────
i_capaB = t11.index("#### B · Qué comprueba el VALIDADOR SEMÁNTICO DEL DIARIO")
i_capaC = t11.index("#### C · Qué garantizan o DEMUESTRAN el RUNTIME")
capaB = t11[i_capaB:i_capaC]
malas = []
if re.search(r"#observaciones = #intentos", capaB) and "Corregido por el gate" not in capaB:
    malas.append("#observaciones = #intentos")
if re.search(r"exactamente un `derivada` por transacción cerrada", capaB) and "decía «exactamente un" not in capaB:
    malas.append("terminalidad sobre `derivada`")
# ninguna regla VIGENTE (fuera de la nota de correccion) puede llevarlas
vigentes = [l for l in capaB.split("\n")
            if l.startswith("· ") and ("agotado: true" in l or "#intentos" in l)]
check("G-05", "cero reglas de `#intentos` / `agotado` VIGENTES en la capa B",
      not malas and not vigentes, "; ".join(malas + vigentes) or "sólo quedan en la nota de retirada")

# ── G-06 · DOS terminales, en la capa B y en el automata ───────────────
dos = ("`derivada` **o** `abandonada`" in capaB
       or "es `derivada` o\n  `abandonada`" in capaB
       or re.search(r"exactamente UN terminal, y es `derivada`", capaB))
check("G-06", "la capa B declara DOS terminales, no uno", bool(dos),
      "terminalidad reescrita sobre los dos" if dos else "no encontrado")

# ── G-07 · cero atribuciones «PLT para cada source change» ─────────────
mal = []
for i, l in enumerate(L11, 1):
    if re.search(r"`PLT`[^|\n]{0,80}cada source change", l) and "Corregido" not in l and not l.lstrip().startswith(">"):
        mal.append(i)
check("G-07", "cero atribuciones «`PLT` para cada source change» vigentes",
      not mal, "" if not mal else f"lineas {mal}")

# ── G-08 · las cinco sedes usan C7 correctamente ──────────────────────
sedes = {"§8.0": None, "§8.1": None, "§8.2": None, "§8.4": None, "§18": None}
bloques = {
 "§8.0": "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "8.0"),
 "§8.1": "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "8.1"),
 "§8.2": "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "8.2"),
 "§8.3": "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "8.3"),
 "§8.4": "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "8.4"),
 "§18":  "\n".join(l for i, l in enumerate(L11, 1) if sec_de(i) == "18"),
}
faltan = []
for nombre, b in bloques.items():
    if "C7:82" not in b: faltan.append(f"{nombre} sin `C7:82` (PLT materializa)")
    if nombre != "§18" and "C7:83" not in b: faltan.append(f"{nombre} sin `C7:83`-`C7:86` (custodia)")
    if "C7:88" not in b: faltan.append(f"{nombre} sin `C7:88`-`C7:89` (ENT convergencia)")
check("G-08", "las SEIS sedes de §8 y §18 citan `C7` operacion a operacion",
      not faltan, "; ".join(faltan) or "§8.0 §8.1 §8.2 §8.3 §8.4 §18")

# ── G-09 · INS-5 completo en §18 ──────────────────────────────────────
s18 = bloques["§18"]
need = ["INS-5` BASELINE APROBADO POR EL OWNER", "CLASIFICACIÓN DE DESCONOCIDOS CRÍTICOS",
        "BASELINE de producto, dominio y diseño de `INS-5`", "TRES condiciones y el productor de cada una"]
falta = [x for x in need if x not in s18]
check("G-09", "§18 lleva el gate de `INS-5`, su salida y los tres productores de `O12`",
      not falta, "; ".join(falta) or "gate, salida y productores")

# ── G-10 · SEIS extensiones de ficha, en las tres sedes ───────────────
seis = {
  "§5.2": "**Son\n                          SEIS**" in t11 or "**Son SEIS**" in t11 or "Son\n                          SEIS" in t11,
  "§16":  "las **SEIS**\n> extensiones de ficha" in t11 or "**SEIS**\n> extensiones" in t11,
  "§17":  "**`+6` extensiones de ficha**" in t11,
}
caps = ["ENT", "ARQ", "PLT", "SEG", "DSP", "ENC"]
i17 = t11.index("`+6` extensiones de ficha")
fila17 = t11[i17:t11.index("\n", i17)]
falta = [k for k, v in seis.items() if not v] + [c for c in caps if f"`{c}`" not in fila17]
check("G-10", "SEIS extensiones de ficha —ENT ARQ PLT SEG DSP ENC— en §5.2, §16 y §17",
      not falta, "; ".join(falta) or "las seis, en las tres sedes")

# ── G-11 · D67 identica byte a byte a la de 7e99388 ───────────────────
base = subprocess.run(["git", "-C", RAIZ, "show",
        "7e99388:docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md"],
        capture_output=True, text=True).stdout.split("\n")
o = [l for l in base if l.startswith("| D67 |")]
a = [l for l in lineas(DEC) if l.startswith("| D67 |")]
check("G-11", "la fila `D67` es identica BYTE A BYTE a la de `7e99388`",
      len(o) == 1 and len(a) == 1 and o[0] == a[0],
      "identica" if o and a and o[0] == a[0] else "DIFIERE")

# ── G-11b · D1-D86 intactas salvo D67 ────────────────────────────────
difs = []
for n in range(1, 87):
    ob = [l for l in base if l.startswith(f"| D{n} |")]
    ac = [l for l in lineas(DEC) if l.startswith(f"| D{n} |")]
    if ob and ac and ob[0] != ac[0]: difs.append(f"D{n}")
check("G-11b", "`D1`-`D86` conservan su texto (D67 restaurada al de 7e99388)",
      not difs, "ninguna difiere" if not difs else "DIFIEREN: " + ", ".join(difs))

# ── G-12 · PN-14 presente y SIN enmienda redactada ───────────────────
tiene = "## `PN-14`" in t11
i = t11.index("## `PN-14`") if tiene else -1
cuerpo = t11[i:t11.index("**Resumen para el Owner", i)] if tiene else ""
sin_enmienda = tiene and "no se redacta ninguna enmienda" in cuerpo.lower()
campos = ["QUÉ PRESIONA", "TEXTO VIGENTE", "MATERIA MÍNIMA", "ALCANCE", "BLOQUEA",
          "CONDICIÓN DE", "ORIGEN"]
falta = [c for c in campos if c not in cuerpo]
check("G-12", "`PN-14` presente, con sus campos, y SIN enmienda redactada",
      tiene and sin_enmienda and not falta,
      "; ".join(falta) if falta else ("presente y sin redactar" if sin_enmienda else "falta la declaracion"))

# ── G-13 · el censo de presiones es COHERENTE, y su tope se DERIVA ───
#
# La versión anterior exigía literalmente 14 cabeceras y 12 vigentes: dos cifras escritas
# a mano en la comprobación que existe para que las cifras no se escriban a mano. Fallaba
# en rojo el día que nacía `PN-15`, que es exactamente lo que §16 existe para permitir.
# Lo comprobable es la COHERENCIA: la serie es continua, las excluidas están marcadas una
# a una, y el resumen de §16 declara lo mismo que derivan las cabeceras.
cab = re.findall(r"^## `PN-(\d+)` ·(.*)$", t11, re.M)
_nums = sorted(int(n) for n, _ in cab)
vigentes = [n for n, resto in cab if "RETIRADA" not in resto and "FUSIONADA" not in resto]
_excluidas = [f"PN-{n}" for n, resto in cab if "RETIRADA" in resto or "FUSIONADA" in resto]
_g13 = []
if _nums != list(range(1, (_nums[-1] if _nums else 0) + 1)):
    _g13.append(f"la serie PN no es continua: {_nums}")
if len(_nums) != len(set(_nums)):
    _g13.append("hay cabeceras PN repetidas")
# el resumen de §16 tiene que declarar lo MISMO que derivan las cabeceras
_m = re.search(r"^VIGENTES · ([A-ZÁÉÍÓÚa-z]+)$", t11, re.M)
if not _m:
    _g13.append("el resumen de §16 no declara «VIGENTES · <n>»")
elif _num(_m.group(1)) != len(vigentes):
    _g13.append(f"el resumen dice {_m.group(1)} y las cabeceras derivan {len(vigentes)}")
check("G-13", "el censo de presiones es coherente: serie continua, excluidas marcadas, resumen = derivado",
      not _g13,
      "; ".join(_g13) or
      f"{len(cab)} cabeceras - {len(_excluidas)} marcadas ({', '.join(_excluidas)}) "
      f"= {len(vigentes)} vigentes, y el resumen de §16 dice lo mismo")

# ── G-14 · F-01 reclasificado ────────────────────────────────────────
tchk = leer(CHK)
m = re.search(r"^\| `F-01` \| (\w+) \| \*\*`([A-Z_0-9]+)`\*\* \|(.*)$", tchk, re.M)
cols = [c.strip() for c in m.group(3).split(" | ")] if m else []
ok = (m and m.group(2) == "PRESION_LISTA_PARA_F5"
      and cols[2] != "no" and cols[3] != "no")
check("G-14", "`F-01` reclasificado a `PRESION_LISTA_PARA_F5`, con requiere_f5 y requiere_f6",
      ok, f"estado={m.group(2) if m else '?'} f5={cols[2] if cols else '?'} f6={'sí' if cols and cols[3]!='no' else '?'}")

# ── G-15 · el contrato de `<CAP>:revision`, DERIVADO Y EJECUTADO ─────
#
# Reescrita por la corrección técnica posterior (`D103`). La versión anterior comprobaba
# que el DOCUMENTO contuviera ciertas palabras y que `SEG` fuera obligatoria en `DEP`.
# **No ejecutaba la derivación**, y por eso pasaba en verde mientras el documento publicaba
# «seis procesos, diez pares exigidos» — cuando el catálogo da CINCO procesos y NUEVE
# pares, y `AUD` no aporta un par fijo sino cero o uno POR ITEM.
#
# Ahora comprueba COMPORTAMIENTO: parsea los bloques `ads:proceso`, normaliza `DOM`/`SEG`
# desde campos ESTRUCTURADOS, deriva el conjunto estático y lo compara con la proyección
# publicada. **El nueve no está escrito aquí**: se deriva y se contrasta con la cifra que
# el documento publica. Si el catálogo cambia, esta comprobación se mueve sola.

_PROC = leer(os.path.join(RAIZ, "kernel/operativo/recorrido/01-PROCESOS.md"))
_BASE_VIGILADAS = ("DOM", "SEG")

def _base(valor):
    """Capacidad BASE de una participación, desde el campo estructurado y nada más.

    `SEG`, `SEG:condiciones` y `capacidad_productora: "SEG"` normalizan todas a `SEG`;
    `DIS/Reconstruccion` normaliza a `DIS`. No se mira `capa_exigida` ni `condicion`:
    inferir por texto libre es lo que `D103` retira.
    """
    return valor.strip().strip('"').strip("'").split(":")[0].split("/")[0].strip()

def _bloques_proceso(texto):
    return re.findall(r"```yaml ads:proceso\n(.*?)```", texto, re.S)

def _participaciones(bloque):
    """{capacidad_base: via} de DOM/SEG en un bloque, SÓLO desde campos estructurados."""
    out = {}
    ic = bloque.find("condicionales:")
    io_ = bloque.find("obligatorias:")
    fin_obl = ic if ic > io_ >= 0 else len(bloque)
    for v in re.findall(r"^\s*capacidad_productora:\s*(.+)$",
                        bloque[io_:fin_obl] if io_ >= 0 else "", re.M):
        b = _base(v)
        if b in _BASE_VIGILADAS:
            out[b] = "obligatoria"
    for v in re.findall(r"^\s*-\s*capacidad:\s*(.+)$",
                        bloque[ic:] if ic >= 0 else "", re.M):
        b = _base(v)
        if b in _BASE_VIGILADAS:
            out.setdefault(b, "condicional")
    return out

def _derivar_catalogo(texto):
    """NIVEL A · pares estáticos. Excluye los procesos de propietario DERIVADO."""
    estaticos, dinamicos = set(), set()
    for b in _bloques_proceso(texto):
        m = re.search(r"^id:\s*proceso:(\w+)", b, re.M)
        pg = re.search(r"^propietario_global:\s*(.*)$", b, re.M)
        if not m or not pg:
            continue
        pid = m.group(1)
        if "DERIVADO" in pg.group(1).upper():
            dinamicos.add(pid)                     # NIVEL B: cardinalidad por item
            continue
        for cap in _participaciones(b):
            estaticos.add((pid, cap))
    return estaticos, dinamicos

def _exige_por_item(propietario):
    """NIVEL B · qué exige UN item cuyo propietario efectivo es `propietario`.

    Cero o UN par. Nunca los dos: un item tiene un propietario, no dos.
    """
    b = _base(propietario)
    return {b} if b in _BASE_VIGILADAS else set()

_g15 = []
_est, _din = _derivar_catalogo(_PROC)
_procs_est = sorted({p for p, _ in _est})
_n_est = len(_est)

# 1 · el contrato tiene que traer sus piezas, y nombrar los DOS niveles
i19 = t11.index("### `DOM` y `SEG` participan DOS veces")
b19 = t11[i19:t11.index("**Y dos más, que no son defectos de F4", i19)]
b19n = re.sub(r"\s+", " ", b19)
# Y una variante SIN marcas de énfasis ni comillas de código: en este corpus una misma
# frase aparece con `**` y con backticks en posiciones distintas según dónde caiga el
# salto de línea, y un patrón que los presuponga falla sobre texto que SÍ está. Es la
# cuarta vez que esta batería tropieza con lo mismo; se normaliza de una vez.
b19p = re.sub(r"[`*]", "", b19n)
for pieza in ("DATOS DE ENTRADA", "ALGORITMO DE", "SALIDA ESPERADA", "CASOS POSITIVOS",
              "CONTRAEJEMPLOS", "composicion-incompleta", "PROPIETARIO", "F6",
              "DERIVACIÓN", "POR ITEM"):
    if pieza not in b19:
        _g15.append(f"el contrato no trae «{pieza}»")
if not ("F4 **no edita `01-PROCESOS.md`**" in b19 or "F4 no toca `01-PROCESOS.md`" in b19):
    _g15.append("no declara que F4 NO edita 01-PROCESOS.md")

# 2 · los DOS barridos léxicos, retirados: el del criterio y el del algoritmo
if not re.search(r"barrido léxico[^.]{0,120}RETIRADO", b19p):
    _g15.append("no declara RETIRADO el barrido léxico de `:condiciones`")
if "NO se analizan capa_exigida ni condicion buscando palabras" not in b19p:
    _g15.append("no declara que `capa_exigida` y `condicion` NO se analizan por palabras")

# 3 · la proyección publicada tiene que COINCIDIR con lo derivado. El número NO se
#     escribe aquí: se deriva y se compara con la cifra que el documento publica.
_m_proc = re.search(r"([A-ZÁÉÍÓÚa-z]+) procesos · ([A-ZÁÉÍÓÚa-z]+) pares", b19p)
if not _m_proc:
    _g15.append("la proyección no publica «<n> procesos · <n> pares» de forma legible")
else:
    _p, _q = _num(_m_proc.group(1)), _num(_m_proc.group(2))
    if _p != len(_procs_est):
        _g15.append(f"publica {_m_proc.group(1)} procesos y el catálogo deriva {len(_procs_est)}")
    if _q != _n_est:
        _g15.append(f"publica {_m_proc.group(2)} pares y el catálogo deriva {_n_est}")

# 4 · `(DEP, SEG)` presente, y por la vía OBLIGATORIA
if ("DEP", "SEG") not in _est:
    _g15.append("el par (DEP, SEG) NO se deriva del catálogo")
else:
    _bd = next((b for b in _bloques_proceso(_PROC) if "id: proceso:DEP" in b), "")
    if _participaciones(_bd).get("SEG") != "obligatoria":
        _g15.append("(DEP, SEG) no procede de la vía OBLIGATORIA")

# 5 · `AUD` es regla DINÁMICA por item, y NO entra en ningún total estático
if "AUD" not in _din:
    _g15.append("`AUD` no se detecta como proceso de propietario DERIVADO")
if any(p == "AUD" for p, _ in _est):
    _g15.append("`AUD` está contado dentro del conjunto ESTÁTICO, y no debe estarlo")
if "proceso:AUD NO tiene cardinalidad estática" not in b19p:
    _g15.append("el contrato no declara que `AUD` carece de cardinalidad estática")
if "no un total simultáneo ni un décimo par fijo" not in b19p:
    _g15.append("el contrato no declara que {DOM, SEG} NO es un total simultáneo")

# 6 · TRES FIXTURES mínimos del nivel B
for prop, esperado in (("DOM", {"DOM"}), ("SEG", {"SEG"}), ("PRD", set())):
    obtenido = _exige_por_item(prop)
    if obtenido != esperado:
        _g15.append(f"fixture AUD propietario {prop}: esperado {esperado or '∅'}, "
                    f"obtenido {obtenido or '∅'}")
# y un item NUNCA exige las dos a la vez
if any(len(_exige_por_item(x)) > 1 for x in ("DOM", "SEG", "PRD", "ARQ")):
    _g15.append("un item AUD llega a exigir DOM y SEG simultáneamente")

# 7 · FIXTURE NEGATIVO · si el catálogo deja de declarar la obligatoria SEG de DEP,
#     el par tiene que DESAPARECER, y una proyección que aún lo publique tiene que fallar
_sin_seg = re.sub(
    r"  - id: condiciones-de-seguridad\n(?:    .*\n|      .*\n)*", "",
    _PROC[_PROC.index("id: proceso:DEP"):_PROC.index("id: proceso:AUD")])
_fix = _PROC[:_PROC.index("id: proceso:DEP")] + _sin_seg + _PROC[_PROC.index("id: proceso:AUD"):]
_est_fix, _ = _derivar_catalogo(_fix)
if ("DEP", "SEG") in _est_fix:
    _g15.append("fixture negativo: quitar la obligatoria SEG de DEP NO retira el par (DEP, SEG)")
if len(_est_fix) >= _n_est:
    _g15.append("fixture negativo: el conjunto derivado no decrece al quitar la participación")

# 8 · FIXTURE NEGATIVO · una proyección que publique un total FIJO de diez tiene que fallar
_proy_falsa = b19p.replace(f"{_m_proc.group(1)} procesos · {_m_proc.group(2)} pares",
                           "SEIS procesos · DIEZ pares") if _m_proc else ""
_m_falsa = re.search(r"([A-ZÁÉÍÓÚa-z]+) procesos · ([A-ZÁÉÍÓÚa-z]+) pares", _proy_falsa)
if not (_m_falsa and (_num(_m_falsa.group(1)) != len(_procs_est)
                      or _num(_m_falsa.group(2)) != _n_est)):
    _g15.append("la comprobación NO detectaría una proyección con el total fijo de diez")

# 9 · el contrato exige que la prueba prescrita falle HOY nombrando DEP
if not re.search(r"FALLIDA nombrando.{0,80}?proceso:DEP → SEG:revision AUSENTE", b19p):
    _g15.append("su prueba no exige fallar HOY nombrando `proceso:DEP`")

check("G-15",
      "el contrato de `<CAP>:revision` se DERIVA de campos estructurados: catálogo estático = proyección, `AUD` dinámico por item",
      not _g15,
      "; ".join(_g15) or
      f"catálogo derivado {len(_procs_est)} procesos {sorted(_procs_est)} · {_n_est} pares · "
      f"(DEP,SEG) por obligatoria · AUD dinámico ({sorted(_din)}) · "
      f"fixtures DOM→{{DOM}} SEG→{{SEG}} PRD→∅ · negativos detectados")

# ── G-16 · 43 estados primarios, sin duplicados ─────────────────────
filas = re.findall(r"^\| `([A-Za-z0-9-]+)` \| (BLOQUEANTE|GRAVE|MEDIO|MENOR) \| \*\*`([A-Z_0-9]+)`\*\* \|(.*)$",
                   tchk, re.M)
ids = [f[0] for f in filas]
dup = [k for k, v in Counter(ids).items() if v > 1]
comp = [f[0] for f in filas if " y " in f[2] or "+" in f[2]]
check("G-16", "43 filas, 43 ids DISTINTOS, un estado primario por id y ninguno compuesto",
      len(filas) == 43 and len(set(ids)) == 43 and not dup and not comp,
      f"{len(filas)} filas / {len(set(ids))} ids" + (f" DUPLICADOS {dup}" if dup else ""))

# ── G-16b · A11 absorbido, A14 excluido ────────────────────────────
check("G-16b", "`A11` absorbido en `M-8` y `A14` excluido: ninguno es fila de la matriz",
      "A11" not in ids and "A14" not in ids,
      "ninguno aparece como fila")

# ── G-17 · recuentos DERIVADOS coinciden con lo publicado ──────────
est = Counter(f[2] for f in filas)
esperado = {"CORREGIDO_EN_F4": 31, "PRESION_LISTA_PARA_F5": 2,
            "CONTRATO_COMPLETO_PARA_F6": 2, "EXTERNO_CON_PROPIETARIO": 7,
            "HISTORICO_NO_APLICABLE": 1}
pub = re.search(r"CORREGIDO_EN_F4\s+(\d+).*?PRESION_LISTA_PARA_F5\s+(\d+).*?"
                r"CONTRATO_COMPLETO_PARA_F6\s+(\d+).*?EXTERNO_CON_PROPIETARIO\s+(\d+).*?"
                r"HISTORICO_NO_APLICABLE\s+(\d+)", tchk, re.S)
pubv = [int(x) for x in pub.groups()] if pub else []
derv = [est["CORREGIDO_EN_F4"], est["PRESION_LISTA_PARA_F5"],
        est["CONTRATO_COMPLETO_PARA_F6"], est["EXTERNO_CON_PROPIETARIO"],
        est["HISTORICO_NO_APLICABLE"]]
check("G-17", "el recuento publicado coincide con el DERIVADO de las filas",
      pubv == derv and sum(derv) == 43,
      f"derivado {derv} suma {sum(derv)} · publicado {pubv}")

# ── G-17b · atributos secundarios derivados ───────────────────────
f5 = [f[0] for f in filas if [c.strip() for c in f[3].split(" | ")][2] != "no"]
f6 = [f[0] for f in filas if [c.strip() for c in f[3].split(" | ")][3] != "no"]
check("G-17b", "requiere_f5 sube por `PN-14` y requiere_f6 conserva `F-01`",
      len(f5) == 3 and "F-01" in f5 and "F-01" in f6 and len(f6) == 11,
      f"F5={len(f5)} {f5} · F6={len(f6)}")

# ── G-18 · vallas Markdown balanceadas ────────────────────────────
desb = []
for p in (D11, DEC, CHK, IDX):
    n = sum(1 for l in lineas(p) if l.strip().startswith("```"))
    if n % 2: desb.append(f"{os.path.basename(p)}={n}")
check("G-18", "vallas Markdown balanceadas en los cuatro ficheros tocados",
      not desb, "; ".join(desb) or "todas pares")

# ── G-19 · cero parrafos duplicados introducidos ─────────────────
def dup_parrafos(p):
    txt = leer(p)
    trozos = [t.strip() for t in re.split(r"\n\s*\n", txt) if len(t.strip()) > 220]
    c = Counter(trozos)
    return [t[:70] for t, n in c.items() if n > 1]
dups = {os.path.basename(p): dup_parrafos(p) for p in (D11, DEC, CHK, IDX)}
malos = {k: v for k, v in dups.items() if v}
check("G-19", "cero parrafos largos duplicados en los cuatro ficheros",
      not malos, "; ".join(f"{k}: {v}" for k, v in malos.items()) or "ninguno")

# ── G-20 · el registro D sin hueco y sin repetir ─────────────────
#
# El tope se DERIVA de la última fila del registro, no se escribe: la versión anterior
# exigía literalmente `D1`-`D95` y fallaba en rojo el día que nacía `D96`, que es
# precisamente lo que el registro existe para permitir. Lo que hay que comprobar es que
# la serie sea CONTINUA y SIN REPETIR, no que se detenga en un número concreto.
ns = sorted(int(x) for x in re.findall(r"^\| D(\d+) ", leer(DEC), re.M))
_huecos = [i for i in range(1, ns[-1] + 1) if i not in ns] if ns else []
_reps = sorted(k for k, v in Counter(
    int(x) for x in re.findall(r"^\| D(\d+) ", leer(DEC), re.M)).items() if v > 1)
check("G-20", "el registro `D` es una serie CONTINUA desde `D1`, sin huecos y sin repetir",
      bool(ns) and not _huecos and not _reps,
      f"D1-D{ns[-1] if ns else '?'}, {len(ns)} filas, huecos {_huecos}, repetidas {_reps}")

# ── G-21 · O1-O16 intactas ───────────────────────────────────────
ob = re.findall(r"^\| O(\d+) \|", "\n".join(base), re.M)
ac = re.findall(r"^\| O(\d+) \|", leer(DEC), re.M)
difs = []
for n in set(ob):
    x = [l for l in base if l.startswith(f"| O{n} |")]
    y = [l for l in lineas(DEC) if l.startswith(f"| O{n} |")]
    if x and y and x[0] != y[0]: difs.append(f"O{n}")
check("G-21", "`O1`-`O16` intactas frente a `7e99388`",
      not difs and len(set(ac)) >= len(set(ob)), "ninguna difiere" if not difs else ", ".join(difs))

# ── G-22 · los documentos 15, 16, 17 y 18 intactos ──────────────
# Se compara la BASE contra el ÁRBOL DE TRABAJO, no contra `HEAD`.
#
# Con `05f71b7 HEAD` se comparaban dos commits, y entonces `G-22` y `G-23` no veían nada de
# lo que hubiera sin confirmar: editar un contrato, una capacidad o cualquier otro validador
# dejaba la comprobación en verde. Una comprobación que sólo mira commits no protege el árbol
# que se le pone delante, que es justo lo que se le pide.
tocados = subprocess.run(["git", "-C", RAIZ, "diff", "--name-only", "05f71b7"],
                          capture_output=True, text=True).stdout.split()
inmutables = [f for f in tocados if re.search(r"docs/evolucion/1[5-8]-", f)]
check("G-22", "los documentos 15, 16, 17 y 18 NO se han tocado",
      not inmutables, "intactos" if not inmutables else ", ".join(inmutables))

# ── G-23 · lo normativo intacto, y el kernel con su EXCEPCIÓN NOMBRADA ──
#
# La versión anterior afirmaba «`kernel/operativo/` intacto» y excluía en bloque todo
# `pruebas/evidencia/`. Dejó de ser cierta en `1b588ac`, que corrigió `comprobar_negativos.py`
# para hacer `N158g` independiente del orden del runner, y reancló `.upstream-hash` porque la
# huella cubre el código de los validadores.
#
# Se sustituye la afirmación falsa por la comprobación EXACTA: lo normativo sigue intacto, el
# kernel operativo SUSTANTIVO sigue intacto, y la única excepción de código es la que se
# nombra. Una exclusión amplia volvería a dejar pasar cualquier otro cambio del kernel, que es
# justo lo que esta comprobación existe para impedir.
NORMATIVO = (r"a-CAPACIDADES-APROBADA|b-RECORRIDO-APROBADA|"
             r"a-ENMIENDA-E1|a-ENMIENDA-E2|"
             r"kernel/operativo/contratos/C4-MATERIALIZACION|"
             r"kernel/operativo/contratos/C7-GOBIERNO")

# Excepciones AUTORIZADAS, una a una. No hay comodines sobre directorios de código.
#
# `entrada/02-CIRCUITO.md` entra por la corrección del gate definitivo (`K-09`, MENOR):
# su L54 citaba `04-CONFIRMACION.md`, que NO existe — el fichero es
# `04-INCERTIDUMBRE-Y-CONFIRMACION.md`. Es un enlace colgante y su remedio es de una línea.
# Se nombra AQUÍ, fichero a fichero, y no se abre ningún comodín sobre `entrada/`: la
# comprobación tiene que seguir cazando cualquier otro cambio del kernel.
COD_AUTORIZADO = {"kernel/operativo/validadores/comprobar_negativos.py"}
DOC_AUTORIZADO = {"kernel/operativo/entrada/02-CIRCUITO.md"}
HUELLA         = {"kernel/.upstream-hash"}

def _kernel_no_autorizado(f):
    if not f.startswith("kernel/"):
        return False
    if f in COD_AUTORIZADO or f in DOC_AUTORIZADO or f in HUELLA:
        return False
    # la evidencia derivada SÍ puede cambiar: la publica el runner, no una mano
    if f.startswith("kernel/operativo/pruebas/evidencia/"):
        return False
    return True

prohibidos = [f for f in tocados if _kernel_no_autorizado(f)]
prohibidos += [f for f in tocados if re.search(NORMATIVO, f)]
check("G-23", "lo normativo intacto; del kernel sólo cambia la excepción NOMBRADA",
      not prohibidos,
      "intacto salvo comprobar_negativos.py, entrada/02-CIRCUITO.md (K-09), "
      ".upstream-hash y evidencia derivada"
      if not prohibidos else ", ".join(sorted(set(prohibidos))))

# ── G-24 · las catorce fuentes y las quince fichas existen ──────
fuentes = """kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md
kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md
kernel/operativo/diseno/02-RUBRICAS.md
kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md
kernel/operativo/diseno/05-FIDELIDAD.md
kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md
kernel/operativo/contratos/C3-METODO-EJECUTABLE.md
kernel/operativo/contratos/C4-MATERIALIZACION.md
kernel/operativo/entrada/00-INDICE.md
kernel/operativo/entrada/02-CIRCUITO.md
kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md
docs/rediseno/a-ENMIENDA-E1-ENC.md
docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md
docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md""".split("\n")
# «legibles» tiene que significar LEÍDAS, y «quince fichas» tiene que significar ESTAS
# quince. La versión anterior comprobaba `os.path.exists` y `len(fichas) == 15`: con eso,
# una ficha sustituida por otra, renombrada o ilegible pasaba en verde, y quince
# directorios cualesquiera contaban como el catálogo. Aquí se comparan los NOMBRES exactos
# y se ABRE cada fichero en UTF-8.
CAPACIDADES = ["APR", "ARQ", "CON", "DIS", "DOM", "DSP", "ENC", "ENT",
               "INV", "PLT", "PRD", "SEG", "SIS", "USO", "VER"]

def _ilegible(ruta):
    """Devuelve el motivo si no se puede leer como UTF-8 con contenido; si no, None."""
    try:
        with io.open(ruta, encoding="utf-8") as fh:
            if not fh.read().strip():
                return "vacío"
    except FileNotFoundError:
        return "no existe"
    except UnicodeDecodeError:
        return "no es UTF-8"
    except OSError as e:
        return f"no se puede abrir: {e.strerror}"
    return None

problemas = []
for f in fuentes:
    motivo = _ilegible(os.path.join(RAIZ, f))
    if motivo:
        problemas.append(f"{f}: {motivo}")

_dir_cap = os.path.join(RAIZ, "kernel/operativo/capacidades")
presentes = sorted(d for d in os.listdir(_dir_cap)
                   if os.path.isdir(os.path.join(_dir_cap, d)))
sobran = [d for d in presentes if d not in CAPACIDADES]
ausentes = [c for c in CAPACIDADES if c not in presentes]
if ausentes:
    problemas.append("faltan capacidades: " + ", ".join(ausentes))
if sobran:
    problemas.append("capacidades no declaradas: " + ", ".join(sobran))

for c in CAPACIDADES:
    if c in presentes:
        motivo = _ilegible(os.path.join(_dir_cap, c, "CAPACIDAD.md"))
        if motivo:
            problemas.append(f"{c}/CAPACIDAD.md: {motivo}")

check("G-24", "las CATORCE fuentes y las QUINCE fichas se LEEN, y son EXACTAMENTE ésas",
      not problemas,
      f"{len(fuentes)} fuentes leídas · {len(CAPACIDADES)} fichas leídas, "
      f"nombre a nombre" if not problemas else "; ".join(problemas))

# ── G-25 · CATORCE campos en los cuatro macrocircuitos ─────────
campos = ["DISPARADOR","PRECONDICIONES","PROCESO","PARTICIPANTES","LEE","ESCRIBE","ESTADO",
          "HANDOFFS","EVIDENCIA","GATES","ROLLBACK","REANUDACIÓN","CERTIFICACIÓN","CIERRE"]
falt = []
for k in ("8.1","8.2","8.3","8.4"):
    b = bloques["§"+k]
    f = [c for c in campos if not re.search(r"^"+c+r"(\s|$)", b, re.M)]
    if f: falt.append(f"§{k}: {f}")
check("G-25", "los cuatro macrocircuitos declaran sus CATORCE campos, handoffs incluidos",
      not falt, "; ".join(falt) or "14/14 en los cuatro")

# ── G-26 · recuentos DERIVADOS, en cuatro planos ───────────────
#
# Ampliada por la corrección del gate definitivo (`J-07` + `K-04`; `C-L.9`). La versión
# anterior comparaba filas contra ids Y contra un 45 ESCRITO A MANO — que es exactamente
# el defecto que esta comprobación existe para cazar, y por eso no vio que cuatro sedes
# de prosa decían «cuarenta y dos» mientras la tabla tenía cuarenta y cinco filas.
#
# **Aquí no hay ni una cifra constante.** Todo se deriva del árbol: la tabla se cuenta, la
# prosa se lee, y se comparan. Si mañana nace una fila nueva, esta comprobación se mueve
# sola; si nace una sede de prosa nueva con la cifra vieja, la caza sin tocar el validador.
#
# Y distingue SEDE VIGENTE de CITA HISTÓRICA, que es la misma disciplina que `X47` aplica
# al enum de `fase`: la proyección normativa vigente es UNA y las citas históricas son
# MUCHAS y están marcadas. Una cifra entre comillas angulares, o en una línea que la
# corrige, o en un bloque marcado HISTÓRICO, es una cita — no una afirmación viva.

# numeral: dígitos, o una/dos palabras unidas por «y», con negritas opcionales
_NUM = r"\*{0,2}((?:[0-9]{1,3})|(?:[A-Za-zÁÉÍÓÚáéíóú]+(?:\s+y\s+[A-Za-zÁÉÍÓÚáéíóú]+)?))\*{0,2}"

# Una cifra es CITA HISTÓRICA, y no afirmación viva, en tres casos y sólo en tres.
# La distinción se hace sobre LA OCURRENCIA CONCRETA del numeral, no sobre la línea
# entera: si bastara que la línea contuviera «corregido», la propia prosa que corrige
# una cifra desactivaría la comprobación de la cifra que acaba de escribir — que es el
# modo de fallo exacto que esta batería existe para no repetir.
_CITA_ENTRE_COMILLAS = re.compile(r"«[^»]*»")
_VERBO_DE_CITA = re.compile(
    r"(?:decía|decían|dijo|habiendo|frente a|en vez de|se escribió cuando"
    r"|NO REPRODUCIDO|reanclad[ao]|conteo a)\s*$", re.I)
_BLOQUE_HISTORICO = re.compile(r"\[HISTÓRICO|\bHISTÓRICO\b|\bcaducad|\bregresión\b")

def _es_cita(linea, ini_rel, fin_rel):
    """¿La ocurrencia [ini_rel:fin_rel] de esta línea es una cita y no una afirmación?"""
    if _BLOQUE_HISTORICO.search(linea):
        return True
    for c in _CITA_ENTRE_COMILLAS.finditer(linea):
        if c.start() <= ini_rel and fin_rel <= c.end():
            return True                     # el numeral está DENTRO de «…»
    return bool(_VERBO_DE_CITA.search(linea[:ini_rel]))

def _sedes(patron, texto=None, contexto=None, ventana=6):
    """[(línea, valor)] de cada sede VIVA que afirma una cifra.

    `contexto` es un patrón que debe aparecer en la VENTANA de líneas alrededor para
    que la afirmación se considere sobre ESE objeto: sin él, «la tabla tiene siete
    filas» de §3.6 se compararía con la tabla adversarial, que es otra tabla. La
    ventana existe porque una afirmación y el nombre de su objeto rara vez caben en
    la misma línea de un bloque de texto justificado.
    """
    texto = t11 if texto is None else texto
    ls = texto.split("\n")
    out = []
    for m in re.finditer(patron, texto, re.I):
        n = _num(m.group(1))
        if n is None:
            continue
        ini = texto.rfind("\n", 0, m.start()) + 1
        fin = texto.find("\n", m.end())
        linea = texto[ini: fin if fin > 0 else len(texto)]
        if _es_cita(linea, m.start() - ini, m.end() - ini):
            continue
        if contexto:
            nl = texto.count("\n", 0, m.start())
            bloque = "\n".join(ls[max(0, nl - ventana): nl + ventana + 1])
            if not re.search(contexto, bloque, re.I):
                continue
        out.append((texto.count("\n", 0, m.start()) + 1, n))
    return out

_fallos_26 = []

# ── 26.a · filas FÍSICAS frente a IDS ÚNICOS ──────────────────────────────
xs = re.findall(r"^\| \*{0,2}`(X[0-9]+)`\*{0,2} \|", t11, re.M)
n_x = len(xs)
if n_x == 0:
    _fallos_26.append("a) la tabla adversarial no se encontró: el patrón de fila no casa")
elif n_x != len(set(xs)):
    dup = sorted(k for k, v in Counter(xs).items() if v > 1)
    _fallos_26.append(f"a) {n_x} filas frente a {len(set(xs))} ids únicos; duplicados: {dup}")

# ── 26.b · PROSA VIGENTE frente al valor DERIVADO ─────────────────────────
# Sólo sedes que hablan de LA TABLA ADVERSARIAL: la línea tiene que nombrarla.
_CTX_X = r"adversarial|§2\.6\.7|\bX[0-9]{2}\b"
for pat, que in (
    (_NUM + r"\s+filas\s+(?:físicas|de datos|escritas)", "filas"),
    (_NUM + r"\s+identificadores", "ids"),
    (r"(?:las|como las)\s+" + _NUM + r"\s+de\s+§2\.6\.7", "filas"),
    (_NUM + r"\s+filas\s+de\s+la\s+tabla\s+adversarial", "filas"),
):
    for ln, val in _sedes(pat, contexto=_CTX_X):
        if val != n_x:
            _fallos_26.append(f"b) L{ln}: la prosa dice {val} {que} y el conteo da {n_x}")

# ── 26.c · AGREGADOS frente a sus MIEMBROS ────────────────────────────────
# c1 · presiones normativas: cabeceras de §16 menos RETIRADA y FUSIONADA
_pn = re.findall(r"^## `(PN-[0-9]+)`([^\n]*)$", t11, re.M)
n_pn = sum(1 for _, resto in _pn if "RETIRADA" not in resto and "FUSIONADA" not in resto)
if not _pn:
    _fallos_26.append("c1) no se encontró ninguna cabecera `## `PN-` en §16")
# El contexto exigido distingue una AFIRMACIÓN DE CENSO —«N presiones vigentes»— de un
# uso incidental del sustantivo, como «presentar al Owner dos presiones donde hay una
# enmienda», que no cuenta nada. Las dos formas específicas de abajo no necesitan
# contexto: ya son inequívocas por sí mismas.
_CTX_PN = r"vigente|VIGENTES|§16"
for pat, ctx in (
    (_NUM + r"\s+(?:presiones|PRESIONES|puntos de presión)", _CTX_PN),
    (r"VIGENTES\s*·\s*" + _NUM, None),
    (r"presiona material aprobado en\s+" + _NUM + r"\s+puntos", None),
):
    for ln, val in _sedes(pat, contexto=ctx):
        if val != n_pn:
            _fallos_26.append(f"c1) L{ln}: dice {val} y las cabeceras de §16 derivan {n_pn}")

# c2 · externos de §19: la tabla frente a la prosa que la reconcilia
_i19 = t11.find("## Lo que esta fase NO puede corregir")
if _i19 < 0:
    _fallos_26.append("c2) no se encontró la sección de externos de §19")
else:
    _seg = t11[_i19:_i19 + 12000]
    _off = t11.count("\n", 0, _i19)
    _filas_f = re.findall(r"^\| `(F-[0-9]+)`", _seg, re.M)
    # miembros que la propia reconciliación declara NO externos
    _no_ext = set(re.findall(
        r"`(F-[0-9]+)`[^\n]{0,120}?(?:deja de ser externo|NO es externo|nunca lo fue)", _seg))
    n_ext = len(_filas_f) - len(_no_ext)
    for pat, que in ((r"los externos son\s+" + _NUM, "externos"),
                     (_NUM + r"\s+de los cuarenta y tres hallazgos", "externos")):
        for ln, val in _sedes(pat, _seg, contexto=r"externo"):
            if val != n_ext:
                _fallos_26.append(
                    f"c2) L{_off+ln}: «{val} externos» y la tabla deriva {n_ext} "
                    f"({len(_filas_f)} filas − {len(_no_ext)} declaradas no externas)")
    for ln, val in _sedes(r"La tabla tiene\s+" + _NUM + r"\s+filas", _seg, contexto=r"externo"):
        if val != len(_filas_f):
            _fallos_26.append(f"c2) L{_off+ln}: «la tabla tiene {val} filas» y tiene {len(_filas_f)}")

# ── 26.d · TOTALES INCOMPATIBLES entre sedes VIVAS ────────────────────────
# Dos sedes vivas que afirmen cifras distintas del MISMO objeto es un fallo aunque
# ninguna difiera del derivado por el patrón que la caza.
for etiqueta, sedes in (
    ("filas adversariales",
     _sedes(_NUM + r"\s+filas\s+(?:físicas|de datos|escritas)", contexto=_CTX_X)),
    ("presiones vigentes",
     _sedes(_NUM + r"\s+(?:presiones|PRESIONES)", contexto=_CTX_PN)),
):
    vals = sorted({v for _, v in sedes})
    if len(vals) > 1:
        _fallos_26.append(f"d) sedes vivas incompatibles para «{etiqueta}»: {vals}")

check("G-26",
      "recuentos DERIVADOS: filas/ids · prosa/derivado · agregados/miembros · sin totales incompatibles",
      not _fallos_26,
      "; ".join(_fallos_26) or
      f"{n_x} filas = {len(set(xs))} ids · {n_pn} presiones derivadas de §16 · "
      f"prosa viva y agregados coinciden")

# ── G-27 · A7 · los cinco CAMPOS en la regla 1 de §2.6.10 ─────
r1 = re.search(r"1  EL COMMIT LOCAL SE HACE[^\n]*\n(?:[^\n]*\n){0,3}", t11)
ok = r1 and "CAMPOS DE PROCEDENCIA" in r1.group(0)
mal = re.search(r"con los CINCO conceptos de `a\.9`:", t11)
check("G-27", "la regla 1 de §2.6.10 usa «los cinco CAMPOS», no «los cinco conceptos»",
      bool(ok) and not mal, "corregida" if ok and not mal else "sigue diciendo conceptos")

# ── informe ──────────────────────────────────────────────────
ancho = max(len(t) for _, t, _, _ in RES)
print("BATERÍA MECÁNICA DE LA CORRECCIÓN DEL GATE DE CIERRE\n")
for id_, t, ok, det in RES:
    print(f"{'OK  ' if ok else 'FALLO'} {id_:7s} {t}")
    if det: print(f"{'':13s}└─ {det}")
verde = sum(1 for _, _, ok, _ in RES if ok)
print(f"\n{verde}/{len(RES)} comprobaciones en verde")
sys.exit(0 if verde == len(RES) else 1)
