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

# ── Git, que FALLA CERRADO ────────────────────────────────────────────────
#
# Añadido por la corrección del GATE DE COBERTURA (`M-12`). `G-21`, `G-22` y `G-23`
# llamaban a `subprocess.run(...)` y usaban su `stdout` SIN mirar el `returncode`. Sobre
# una copia sin `.git` —un tarball, un `git archive`, la forma en que este corpus viajaría
# a un revisor externo— `git` fallaba, `stdout` venía vacío, y las tres interpretaban el
# vacío como «nada cambió»: declaraban intacto un árbol con (a) mutilada, el documento 18
# alterado y `C7` modificado.
#
# `_git()` devuelve la salida SÓLO si el comando tuvo éxito. Si falla, si no existe, o si
# el repositorio no responde, devuelve None — y las comprobaciones que dependen de él
# fallan CERRADO, con diagnóstico.
def _git(*args):
    try:
        r = subprocess.run(["git", "-C", RAIZ, *args],
                           capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    return r.stdout if r.returncode == 0 else None

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
_base_raw = _git("show", "7e99388:docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md")
base = _base_raw.split("\n") if _base_raw is not None else []
o = [l for l in base if l.startswith("| D67 |")]
a = [l for l in lineas(DEC) if l.startswith("| D67 |")]
check("G-11", "la fila `D67` es identica BYTE A BYTE a la de `7e99388` (falla CERRADO sin git)",
      _base_raw is not None and len(o) == 1 and len(a) == 1 and o[0] == a[0],
      "identica" if o and a and o[0] == a[0] else "DIFIERE")

# ── G-11b · D1-D86 intactas salvo D67 ────────────────────────────────
#
# FALLA CERRADO desde `Q-01`. Era la ÚNICA comprobación dependiente de Git que no lo hacía:
# sin `.git`, `_base_raw` es `None`, `base` queda vacía, el bucle no encuentra ni una fila
# con la que comparar y `difs` sale vacío — con lo que declaraba «ninguna difiere» sobre
# OCHENTA Y SEIS filas que no había mirado. Es el defecto que `M-12` cerró en `G-21`, `G-22`
# y `G-23`, sobreviviendo en la de mayor alcance de las cuatro.
difs = []
for n in range(1, 87):
    ob = [l for l in base if l.startswith(f"| D{n} |")]
    ac = [l for l in lineas(DEC) if l.startswith(f"| D{n} |")]
    if ob and ac and ob[0] != ac[0]: difs.append(f"D{n}")
if _base_raw is None:
    difs.append("GIT NO RESPONDE: no se puede comparar contra `7e99388`")
elif not base:
    difs.append("la base de `7e99388` viene VACÍA: no hay nada contra lo que comparar")
check("G-11b", "`D1`-`D86` conservan su texto (D67 restaurada al de 7e99388; falla CERRADO sin git)",
      _base_raw is not None and not difs,
      "ninguna difiere" if (_base_raw is not None and not difs) else "DIFIEREN: " + ", ".join(difs))

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
# y el BARRIDO de `PN-15` sobre el material APROBADO, derivado fichero a fichero (`P-06`)
#
# El bloque de evidencia declaraba «cero apariciones de `G20`, `G21` y `G23` en el documento
# 11, en (a), en (b) y en `E2`», y era falso del documento 11 —donde hay decenas, casi todas
# introducidas por el propio bloque que lo negaba: la evidencia se destruía al registrarla—.
# La tesis que sí se sostiene, y la única que la presión necesita, es que **el material
# APROBADO no contiene una derogación válida**. Aquí se deriva ese barrido y se contrasta
# contra las tres cifras publicadas. El documento 11 queda fuera a propósito: sus
# apariciones son documentales y contarlas no probaría nada.
_APROBADO = {"(a)": "docs/rediseno/a-CAPACIDADES-APROBADA.md",
             "(b)": "docs/rediseno/b-RECORRIDO-APROBADA.md",
             "E2":  "docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md"}
_m_bar = re.search(r"\(a\) (\d+) · \(b\) (\d+) · E2 (\d+)", t11)
if not _m_bar:
    _g13.append("el bloque de `PN-15` no publica el barrido «(a) n · (b) n · E2 n»")
else:
    _pub = dict(zip(("(a)", "(b)", "E2"), (int(g) for g in _m_bar.groups())))
    for _k, _ruta in _APROBADO.items():
        _real = sum(1 for l in lineas(os.path.join(RAIZ, _ruta))
                    if re.search(r"\bG2[0-3]\b", l))
        if _pub[_k] != _real:
            _g13.append(f"barrido de `PN-15`: publica {_pub[_k]} en {_k} y el fichero "
                        f"deriva {_real}")

check("G-13", "el censo de presiones es coherente y el barrido de `PN-15` sobre el material APROBADO, derivado",
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
# Reescrita por la corrección del GATE DE COBERTURA (`D104`). La versión anterior derivaba
# de verdad la CIFRA, y aun así el gate la refutó por cuatro caminos: no implementaba la vía
# PROPIETARIA que su criterio nombra en primer lugar (`O-01`), no evaluaba la vía CONDICIONAL
# de `proceso:AUD` (`M-01`), partía estático/dinámico buscando la palabra «DERIVADO» en un
# campo `{tipo: texto}` (`N-02`), y comparaba sólo la PRIMERA proyección del bloque, con lo
# que una segunda contradictoria pasaba en verde (`M-04`, refutación 2).
#
# Ahora deriva las CUATRO vías, parte por pertenencia al conjunto de las quince, deriva el
# ancla de posición, y exige que la proyección publicada sea ÚNICA y coincida.

_DIR_CAPS = os.path.join(RAIZ, "kernel/operativo/capacidades")
_CAPS = frozenset(os.listdir(_DIR_CAPS))
_PROC_MD = os.path.join(RAIZ, "kernel/operativo/recorrido/01-PROCESOS.md")

# El conjunto VIGILADO se DERIVA de las fichas, y no se escribe.
#
# `Q-09`. La versión anterior traía `_VIGILADAS = ("DOM", "SEG")` como literal, que es la
# misma clase de censo escrito a mano que esta batería existe para cazar: si mañana `b.16`
# diera la doble participación a una tercera capacidad, o se la quitara a una de las dos, la
# comprobación seguiría verde sobre un catálogo que ya no es el suyo. La sede canónica es la
# ficha de cada capacidad, que lo declara en su propio atributo — hoy `DOM` y `SEG`, cada una
# en su L51. Aquí se lee esa declaración y el código de la capacidad es el NOMBRE DE SU
# DIRECTORIO, no una cadena buscada dentro del texto.
def _derivar_vigiladas():
    out = []
    for cap in sorted(_CAPS):
        ficha = os.path.join(_DIR_CAPS, cap, "CAPACIDAD.md")
        if not os.path.isfile(ficha):
            continue
        if re.search(r"participa dos veces", leer(ficha)):
            out.append(cap)
    return tuple(out)

_VIGILADAS = _derivar_vigiladas()

def _base(valor):
    """Capacidad BASE: segmento anterior al primer `:` y al primer `/`. Nada más."""
    return valor.strip().strip('"').strip("'").split(":")[0].split("/")[0].strip()

def _limpio(valor):
    return valor.strip().strip('"').strip("'").strip()

def _bloques_proceso(texto):
    return re.findall(r"```yaml ads:proceso\n(.*?)```", texto, re.S)

def _campos(bloque):
    """Los campos REALES del bloque, leyendo INDENTACIÓN y ESCALARES DE BLOQUE.

    Devuelve `(campos, prosa_sospechosa)`. `campos` es [(seccion, clave, valor, sangria)].

    `Q-05`. La versión anterior troceaba el bloque con `find("obligatorias:")` /
    `find("condicionales:")` y sacaba las participaciones con un `re.findall` sobre esos
    SEGMENTOS DE TEXTO. Eso no es leer YAML: es buscar una cadena. Una línea escrita dentro
    del escalar de prosa de un `criterio_de_satisfaccion` —o de `capa_exigida`, `condicion`
    o `autoridad_de_retirada`— entraba en la derivación como si fuera un campo, y `G-15`
    seguía en verde. El contrato de `D104` declara que esos cuatro campos NO se leen, y el
    mecanismo no lo sostenía.

    Aquí una línea sólo es campo si vive al nivel de sangría de su sección y NO está dentro
    de un escalar `>` o `|`. Lo que aparece dentro de un escalar es PROSA, siempre — y si esa
    prosa tiene aspecto de campo de participación, se devuelve en `prosa_sospechosa` para
    poder fallar NOMBRANDO el campo que la contiene, en vez de acusar a la proyección.
    """
    campos, prosa = [], []
    seccion = None
    esc_ind = esc_clave = None
    for linea in bloque.split("\n"):
        if not linea.strip():
            continue
        ind = len(linea) - len(linea.lstrip(" "))
        if esc_ind is not None:
            if ind > esc_ind:
                if re.match(r"\s*(?:capacidad_productora|capacidad)\s*:", linea):
                    prosa.append((seccion, esc_clave, linea.strip()))
                continue
            esc_ind = esc_clave = None
        cuerpo = linea.strip()
        if cuerpo.startswith("- "):
            cuerpo, ind = cuerpo[2:].strip(), ind + 2
        m = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", cuerpo)
        if not m:
            continue
        clave, valor = m.group(1), m.group(2).strip()
        if ind == 0:
            seccion = clave if clave in ("obligatorias", "condicionales") else None
        if valor in (">", "|", ">-", "|-", ">+", "|+"):
            esc_ind, esc_clave = ind, clave
            valor = ""
        campos.append((seccion, clave, valor, ind))
    return campos, prosa

def _analizar(bloque):
    """(pid, propietario, es_estatico, ancla, participaciones, prosa_sospechosa).

    `participaciones` es [(capacidad_base, via, seccion)] con via ∈ {1,2,3,4}:
      1 propietaria · 2 obligatoria desnuda · 3 condicional desnuda · 4 item enlazado tipado
    y `seccion` ∈ {propietaria, obligatorias, condicionales}. **La PROCEDENCIA se conserva**
    (`Q-03`, `Q-10`): una obligatoria se exige SIEMPRE —también tipada por la vía 4— y una
    condicional sólo cuando su condición está activa, luego la vía por sí sola ya no basta
    para saber qué exige un item.

    `capa_exigida`, `condicion`, `criterio_de_satisfaccion` y `autoridad_de_retirada` NO se
    leen, y ahora el mecanismo lo garantiza: sus escalares se saltan como prosa (`_campos`).
    Toda la inferencia sigue siendo UNA prueba de pertenencia a `_CAPS`.
    """
    campos, prosa = _campos(bloque)
    pid = next(_limpio(v) for sec, k, v, i in campos if k == "id" and i == 0).split(":", 1)[1]
    pg = next(_limpio(v) for sec, k, v, i in campos if k == "propietario_global" and i == 0)
    obl = [_limpio(v) for sec, k, v, i in campos
           if sec == "obligatorias" and k == "capacidad_productora"]
    cond = [_limpio(v) for sec, k, v, i in campos
            if sec == "condicionales" and k == "capacidad"]

    # DISCRIMINANTE ESTRUCTURAL: igualdad contra el conjunto de las quince, no subcadena
    estatico = pg in _CAPS

    # ANCLA DE POSICIÓN: la obligatoria de `VER` si existe; si no, la última obligatoria.
    # Se compara sobre la capacidad BASE (`Q-02`): antes se comparaba la cadena CRUDA, y un
    # `capacidad_productora: "VER:dosier"` —referencia tipada LEGÍTIMA por el propio
    # contrato— dejaba de ser `VER`, desplazaba el ancla del proceso en silencio y `G-15`
    # imprimía verde. `D104` declara que normalizar a la capacidad base ES TODA LA
    # INFERENCIA QUE HAY: el ancla no puede ser la excepción.
    obl_base = [_base(v) for v in obl]
    ancla = "VER" if "VER" in obl_base else (obl_base[-1] if obl_base else None)

    part = []
    if estatico and _base(pg) in _VIGILADAS:
        part.append((_base(pg), 1, "propietaria"))     # vía 1 · propietaria
    for v in obl:
        b = _base(v)
        if b in _VIGILADAS:
            part.append((b, 2 if v == b else 4, "obligatorias"))
    for v in cond:
        b = _base(v)
        if b in _VIGILADAS:
            part.append((b, 3 if v == b else 4, "condicionales"))
    return pid, pg, estatico, ancla, part, prosa

def _derivar(texto):
    """(estaticos, dinamicos, anclas, prosa) — estaticos: {(proc,cap): (via, seccion)}."""
    estaticos, dinamicos, anclas, prosa = {}, {}, {}, []
    for b in _bloques_proceso(texto):
        pid, pg, est, ancla, part, pr = _analizar(b)
        anclas[pid] = ancla
        prosa += [(pid, sec, clave, linea) for sec, clave, linea in pr]
        if est:
            for cap, via, sec in part:
                estaticos[(pid, cap)] = (via, sec)
        else:
            dinamicos[pid] = part
    return estaticos, dinamicos, anclas, prosa

def _exige_item(proceso_part, propietario_efectivo, condicionales_activos):
    """REGLA POR ITEM: propietario del item ∪ obligatorias ∪ condicionales ACTIVADAS.

    Manda la PROCEDENCIA, no la vía (`Q-10`). La versión anterior escribía
    `if via in (3, 4)`, con lo que una participación tipada de la sección `obligatorias`
    —vía 4 legítima— se trataba como condicional y dejaba de exigirse cuando su condición
    no estaba activa. Hoy ninguna vía 4 procede de `obligatorias` en el árbol real, así que
    el defecto era LATENTE: se corrige antes de que tenga instancias, y el fixture de abajo
    lo mantiene cerrado.
    """
    out = set()
    b = _base(propietario_efectivo)
    if b in _VIGILADAS:
        out.add(b)
    for cap, via, seccion in proceso_part:
        if seccion == "obligatorias":
            out.add(cap)
        elif seccion == "condicionales" and cap in condicionales_activos:
            out.add(cap)
    return out

_g15 = []
_PROC = leer(_PROC_MD)
_est, _din, _anclas, _prosa = _derivar(_PROC)
_procs_est = sorted({p for p, _ in _est})
_FIXTURES = []          # censo de fixtures EJECUTADOS, derivado y contrastado (`Q-12`)

# 0 · ninguna PROSA se cuela como participación (`Q-05`)
#
# Falla NOMBRANDO el campo que contiene la línea, que es lo que el gate pidió: acusar a la
# proyección publicada de no cuadrar cuando el defecto está en un escalar de prosa mandaría
# a corregir la sede equivocada.
for _pid, _sec, _clave, _linea in _prosa:
    _g15.append(f"prosa con aspecto de campo en `proceso:{_pid}` → `{_clave}` "
                f"(sección {_sec}): «{_linea}». Un escalar de prosa NO declara participación")

# 1 · el contrato tiene que traer sus piezas y nombrar las cuatro vías
i19 = t11.index("### `DOM` y `SEG` participan DOS veces")
b19 = t11[i19:t11.index("**Y dos más, que no son defectos de F4", i19)]
b19p = re.sub(r"[`*]", "", re.sub(r"\s+", " ", b19))
for pieza in ("PROPIETARIA", "OBLIGATORIA", "CONDICIONAL", "ITEM PROPIO",
              "DATOS DE ENTRADA", "ALGORITMO DE", "SALIDA ESPERADA", "CASOS POSITIVOS",
              "CONTRAEJEMPLOS", "composicion-incompleta", "PROPIETARIO", "F6",
              "ANCLA DE", "REGLA POR ITEM"):
    if pieza not in b19:
        _g15.append(f"el contrato no trae «{pieza}»")
if "NO se analizan `capa_exigida` ni `condicion`" not in b19 and \
   "capa_exigida, condicion, criterio_de_satisfaccion y autoridad_de_retirada NO se leen" not in b19p:
    _g15.append("no declara que los campos de prosa NO se leen")
if "pertenencia al conjunto de las QUINCE" not in b19p:
    _g15.append("no declara el discriminante estructural por pertenencia")

# 2 · la proyección publicada tiene que ser ÚNICA y coincidir con lo derivado.
#     Ni el número ni el conteo de proyecciones se escriben aquí: se derivan.
_proys = re.findall(r"([A-ZÁÉÍÓÚa-z]+) procesos . ([A-ZÁÉÍÓÚa-z]+) pares", b19p)
if not _proys:
    _g15.append("la proyección no publica «<n> procesos · <n> pares» de forma legible")
elif len(_proys) > 1:
    _g15.append(f"hay {len(_proys)} proyecciones en el bloque y debe haber UNA: {_proys}")
else:
    _p, _q = _num(_proys[0][0]), _num(_proys[0][1])
    if _p != len(_procs_est):
        _g15.append(f"publica {_proys[0][0]} procesos y el catálogo deriva {len(_procs_est)}")
    if _q != len(_est):
        _g15.append(f"publica {_proys[0][1]} pares y el catálogo deriva {len(_est)}")

# 2bis · el REPARTO EXACTO POR VÍA, no sólo el total (`Q-03`)
#
# Un total de nueve pares admite repartos semánticamente distintos: mover `DOM` y `SEG` de
# `FEA` de la vía 4 a la vía 3 deja el total intacto y cambia lo que el contrato significa.
# La proyección publica el reparto y aquí se contrasta vía a vía.
_reparto_real = Counter(via for via, _ in _est.values())
_reparto_pub = {int(v): int(n) for v, n in re.findall(r"vía (\d) . (\d+) par", b19p)}
if not _reparto_pub:
    _g15.append("la proyección no publica el REPARTO POR VÍA «vía <n> · <n> pares»")
else:
    for _v in (1, 2, 3, 4):
        if _reparto_pub.get(_v, 0) != _reparto_real.get(_v, 0):
            _g15.append(f"reparto por vía {_v}: publica {_reparto_pub.get(_v, 0)} y "
                        f"el catálogo deriva {_reparto_real.get(_v, 0)}")

# 2ter · las ANCLAS publicadas, proceso a proceso, contra las derivadas (`Q-11`)
#
# La sede publicaba «`INV` `AUD` → tras su única obligatoria, `conclusion-fundada` de
# `INV`», y `conclusion-fundada` es la obligatoria de `AUD`: la de `INV` es
# `evidencia-producida`. Una sola frase atribuía el mismo item a dos procesos. Ahora la
# proyección publica el ancla de cada proceso y esto la contrasta.
_m_anclas = re.search(r"ANCLA DERIVADA HOY(.{0,600})", b19p)
_anclas_pub = dict(re.findall(r"\b([A-Z]{3}) → ([A-Z]{3})\b", _m_anclas.group(1))) \
    if _m_anclas else {}
if not _anclas_pub:
    _g15.append("la proyección no publica «ANCLA DERIVADA HOY» con «<PROC> → <CAP>» "
                "proceso a proceso")
else:
    for _pr, _an in sorted(_anclas.items()):
        if _anclas_pub.get(_pr) != _an:
            _g15.append(f"ancla de `{_pr}`: publica {_anclas_pub.get(_pr)} y se deriva {_an}")
    for _pr in sorted(set(_anclas_pub) - set(_anclas)):
        _g15.append(f"la proyección publica un ancla para `{_pr}`, que no es un proceso")

# 3 · las cuatro vías, ejercitadas sobre FIXTURES SINTÉTICOS
#
# Los fixtures se construyen aquí, enteros, y NO mutando el árbol real: un fixture que
# depende de que cierta cadena exista en el corpus se rompe el día que el corpus cambia,
# y entonces la comprobación deja de comprobar en vez de fallar con diagnóstico.
_FX = """```yaml ads:proceso
id: proceso:FX
propietario_global: "%s"
obligatorias:
  - id: uno
    capacidad_productora: "%s"
  - id: dos
    capacidad_productora: "VER"
condicionales:
  - capacidad: "%s"
```"""

# vía 1 · PROPIETARIA — el fixture que `O-01` demostró que la versión anterior no veía
_FIXTURES.append("vía 1 · propietaria")
_e1, _, _, _ = _derivar(_FX % ("DOM", "CON", "APR"))
if _e1.get(("FX", "DOM")) != (1, "propietaria"):
    _g15.append("fixture VÍA 1: un `propietario_global: \"DOM\"` no emite par propietario")

# vía 2 y vía 4 sobre el fixture, con las dos formas del mismo campo
_FIXTURES += ["vía 2 · obligatoria desnuda", "vía 4 · item enlazado tipado"]
_e2, _, _, _ = _derivar(_FX % ("PRD", "SEG", "DOM:condiciones"))
if _e2.get(("FX", "SEG")) != (2, "obligatorias"):
    _g15.append("fixture VÍA 2: `capacidad_productora: \"SEG\"` no emite par obligatorio")
if _e2.get(("FX", "DOM")) != (4, "condicionales"):
    _g15.append("fixture VÍA 4: `DOM:condiciones` no emite par tipado")

# vía 3 sobre el fixture, con la capacidad BASE desnuda
_FIXTURES.append("vía 3 · condicional desnuda")
_e3, _, _, _ = _derivar(_FX % ("PRD", "CON", "SEG"))
if _e3.get(("FX", "SEG")) != (3, "condicionales"):
    _g15.append("fixture VÍA 3: `capacidad: \"SEG\"` desnuda no emite par condicional")

# y el discriminante: un propietario que NO es uno de los quince cae en dinámico
_FIXTURES.append("discriminante estructural")
_, _d4, _, _ = _derivar(_FX % ("la capacidad que decida el encargo", "CON", "APR"))
if "FX" not in _d4:
    _g15.append("el discriminante no clasifica como dinámico un propietario que no es "
                "uno de los quince")

# y sobre el ÁRBOL REAL, las dos vías que hoy tienen instancias
if _est.get(("DEP", "SEG")) != (2, "obligatorias"):
    _g15.append("árbol real: `(DEP, SEG)` no se deriva por la vía obligatoria")
if sum(1 for via, _ in _est.values() if via == 4) == 0:
    _g15.append("árbol real: ninguna participación tipada `<CAP>:condiciones` se deriva")

# vía 3 · CONDICIONAL desnuda — `AUD` declara `DOM` y `SEG` así
_aud = dict((c, v) for c, v, _ in _din.get("AUD", []))
if _aud.get("DOM") != 3 or _aud.get("SEG") != 3:
    _g15.append("fixture VÍA 3: los condicionales desnudos de `AUD` no se derivan")

# 3bis · el ANCLA no se deja desplazar por una referencia TIPADA legítima (`Q-02`)
_FIXTURES.append("ancla ante `VER:dosier`")
_, _, _a5, _ = _derivar(_FX % ("PRD", "CON", "APR"))
_FXVER = _FX.replace('capacidad_productora: "VER"', 'capacidad_productora: "VER:dosier"')
_, _, _a6, _ = _derivar(_FXVER % ("PRD", "CON", "APR"))
if _a5.get("FX") != "VER" or _a6.get("FX") != "VER":
    _g15.append(f"fixture ANCLA TIPADA: `VER` da {_a5.get('FX')} y `VER:dosier` da "
                f"{_a6.get('FX')}; una referencia tipada legítima desplaza el ancla")

# 3ter · una PROSA con aspecto de campo no participa, y se DENUNCIA (`Q-05`)
_FIXTURES.append("prosa con aspecto de campo")
_FXPROSA = """```yaml ads:proceso
id: proceso:FY
propietario_global: "PRD"
obligatorias:
  - id: uno
    capacidad_productora: "CON"
    criterio_de_satisfaccion: >
      el criterio menciona, sin ser un campo,
      capacidad_productora: "DOM"
      y no debe contar como participación
condicionales:
  - capacidad: "APR"
```"""
_ey, _, _, _py = _derivar(_FXPROSA)
if ("FY", "DOM") in _ey:
    _g15.append("fixture PROSA: una línea dentro de un escalar `>` emite participación")
if not _py:
    _g15.append("fixture PROSA: la línea sospechosa no se denuncia con su campo contenedor")

# 3quater · una OBLIGATORIA tipada se exige SIEMPRE, no como condicional (`Q-10`)
_FIXTURES.append("obligatoria tipada de vía 4")
_FXOBL = """```yaml ads:proceso
id: proceso:FZ
propietario_global: "la capacidad que decida el encargo"
obligatorias:
  - id: uno
    capacidad_productora: "SEG:condiciones"
condicionales:
  - capacidad: "DOM"
```"""
_, _dz, _, _ = _derivar(_FXOBL)
if _exige_item(_dz.get("FZ", []), "PRD", set()) != {"SEG"}:
    _g15.append("fixture OBLIGATORIA TIPADA: una `SEG:condiciones` declarada en "
                "`obligatorias` deja de exigirse cuando ninguna condición está activa")
if _exige_item(_dz.get("FZ", []), "PRD", {"DOM"}) != {"SEG", "DOM"}:
    _g15.append("fixture OBLIGATORIA TIPADA: activar la condicional no acumula sobre la "
                "obligatoria")

# 4 · `AUD` dinámico, con sus CUATRO combinaciones por item
_pa = _din.get("AUD", [])
for prop, activos, esperado in (
    ("DOM", set(),               {"DOM"}),
    ("SEG", set(),               {"SEG"}),
    ("PRD", set(),               set()),
    ("PRD", {"DOM", "SEG"},      {"DOM", "SEG"}),
    ("DOM", {"SEG"},             {"DOM", "SEG"}),
):
    _FIXTURES.append(f"AUD · propietario {prop} · activos {sorted(activos) or '∅'}")
    obtenido = _exige_item(_pa, prop, activos)
    if obtenido != esperado:
        _g15.append(f"fixture AUD (propietario {prop}, activos {sorted(activos) or '∅'}): "
                    f"esperado {sorted(esperado) or '∅'}, obtenido {sorted(obtenido) or '∅'}")

# 5 · `DIR` — dinámico por la MISMA regla, sin excepción escrita
_FIXTURES += ["DIR · propietario vigilado", "DIR · propietario ajeno"]
if "DIR" not in _din:
    _g15.append("`DIR` no se clasifica como propietario derivado por item")
if _exige_item(_din.get("DIR", []), "DOM", set()) != {"DOM"}:
    _g15.append("fixture DIR: propietario `DOM` no exige `DOM:revision`")
if _exige_item(_din.get("DIR", []), "ARQ", set()) != set():
    _g15.append("fixture DIR: propietario ajeno exige algo")
if any(p == "DIR" for p, _ in _est):
    _g15.append("`DIR` aparece en el catálogo ESTÁTICO, y su propietario no es uno de los quince")

# 6 · el ANCLA no exige `VER` donde no hay `VER`
_sin_ver = sorted(p for p, a in _anclas.items() if a != "VER")
if "AUD" not in _sin_ver:
    _g15.append("`AUD` recibe ancla `VER` y `AUD` no declara `VER`")
for _p in _sin_ver:
    if _anclas[_p] is None:
        _g15.append(f"`{_p}` no tiene ancla derivable")

# 7 · fixture NEGATIVO · quitar la obligatoria SEG de DEP retira el par
_FIXTURES.append("negativo · retirar la obligatoria de DEP")
_sin_seg = re.sub(r"  - id: condiciones-de-seguridad\n(?:    .*\n|      .*\n)*", "",
                  _PROC[_PROC.index("id: proceso:DEP"):_PROC.index("id: proceso:AUD")])
_ffix = _PROC[:_PROC.index("id: proceso:DEP")] + _sin_seg + _PROC[_PROC.index("id: proceso:AUD"):]
_efix, _, _, _ = _derivar(_ffix)
if ("DEP", "SEG") in _efix or len(_efix) >= len(_est):
    _g15.append("fixture negativo: quitar la obligatoria SEG de DEP no retira el par")

# 7bis · el conjunto VIGILADO se deriva de las fichas, y cambia con ellas (`Q-09`)
_FIXTURES.append("conjunto vigilado derivado de las fichas")
if set(_VIGILADAS) != {c for c in _CAPS
                       if re.search(r"participa dos veces",
                                    leer(os.path.join(_DIR_CAPS, c, "CAPACIDAD.md")))}:
    _g15.append("el conjunto vigilado no coincide con lo que declaran las fichas")
if not _VIGILADAS:
    _g15.append("ninguna ficha declara la doble participación: el conjunto vigilado es vacío")

# 8 · el contrato exige que la prueba prescrita falle HOY nombrando DEP
if not re.search(r"FALLIDA nombrando.{0,80}?proceso:DEP → SEG:revision AUSENTE", b19p):
    _g15.append("su prueba no exige fallar HOY nombrando `proceso:DEP`")

# 9 · el CENSO DE FIXTURES publicado coincide con el EJECUTADO (`Q-12`)
#
# La sede decía «cinco fixtures, uno por vía y uno por proceso dinámico» junto a una
# enumeración de seis grupos, con tres procesos dinámicos. La cifra era manual y no
# describía lo que la batería ejecuta. Ahora el censo se DERIVA de los fixtures realmente
# corridos, y la sede publica ese número.
_censo_pub = re.search(r"CENSO DE FIXTURES[^.]{0,80}?(\d+) fixtures", b19p)
if not _censo_pub:
    _g15.append("la sede no publica el «CENSO DE FIXTURES … <n> fixtures»")
elif int(_censo_pub.group(1)) != len(_FIXTURES):
    _g15.append(f"censo de fixtures: publica {_censo_pub.group(1)} y se ejecutan "
                f"{len(_FIXTURES)}")

check("G-15",
      "`<CAP>:revision` derivado por las CUATRO vías, con procedencia, ancla normalizada, prosa excluida y censos derivados",
      not _g15,
      "; ".join(_g15) or
      f"catálogo {len(_procs_est)} procesos {sorted(_procs_est)} · {len(_est)} pares "
      f"(reparto por vía: {sorted(_reparto_real.items())}) · dinámicos {sorted(_din)} · "
      f"vigiladas {sorted(_VIGILADAS)} · anclas sin VER {_sin_ver} · "
      f"{len(_FIXTURES)} fixtures ejecutados, todos en verde")

# ── G-16 · 43 estados primarios, sin duplicados ─────────────────────
filas = re.findall(r"^\| `([A-Za-z0-9-]+)` \| (BLOQUEANTE|GRAVE|MEDIO|MENOR) \| \*\*`([A-Z_0-9]+)`\*\* \|(.*)$",
                   tchk, re.M)
ids = [f[0] for f in filas]
dup = [k for k, v in Counter(ids).items() if v > 1]
# `comp = [... if " y " in f[2] or "+" in f[2]]` vivía aquí y se RETIRA: el grupo 3 está
# restringido a `[A-Z_0-9]+` y nunca podía contener un espacio ni un `+`, luego la
# comprobación de estados compuestos no podía disparar jamás. Es `M-11`. La sustituye la
# detección sobre la LÍNEA ENTERA, más abajo.
# La MISMA regla, sobre el otro objeto que la necesita: las trece condiciones de cierre
# `C-L.1`–`C-L.13`. Se comprueba AQUÍ, dentro de `G-16`, porque es la misma norma y porque
# la batería no crece: sigue teniendo TREINTA comprobaciones.
#
# Reescrita por la corrección del GATE DE COBERTURA. La versión anterior comprobaba la
# COHERENCIA INTERNA del bloque resumen —que la cifra declarada casara con los ids
# nombrados— y nada más, con lo que mover `C-L.12` de estado ajustando los contadores
# pasaba en verde contradiciendo su propio detalle (`M-04`, refutación 3). Además llevaba
# DOS censos escritos a mano dentro de la comprobación cuyo objeto es esa disciplina
# (`O-02`), y una detección de estados compuestos que no podía disparar jamás (`M-11`).
#
# Ahora contrasta el resumen contra las TRECE FILAS DE DETALLE, deriva los componentes de
# `C-L.13` de esa misma fuente, y deriva su propio mensaje de éxito.
_ESTADOS_CL = ("CORREGIDAS EN F4c", "REGISTRADAS PARA F5", "CONTRATADA PARA F6",
               "MIXTA POR DESGLOSE", "CERTIFICADA POR")

_g16c = []
_asig, _declarado = {}, {}
# La clasificación VIGENTE está delimitada, y su detalle se lee DENTRO de ella (`Q-14`).
#
# Antes, las filas de detalle se buscaban en TODO el checkpoint y se tomaba la primera
# aparición de cada `C-L.n`: una fila de un bloque HISTÓRICO satisfacía el contraste de la
# clasificación vigente. Es la puerta por la que `C-L.3` podía estar descrita a la vez como
# CERRADA por la regla de `D103` —que `M-01` refutó— y como NO CERRADA, sin que nada lo
# viera. Ahora el bloque vigente se abre con «CÓMO QUEDA CADA CONDICIÓN», se cierra con
# «FIN DE LA CLASIFICACIÓN VIGENTE», y **todo lo que se contrasta sale de ahí dentro**.
_i = tchk.find("CÓMO QUEDA CADA CONDICIÓN")
_fin_vig = tchk.find("FIN DE LA CLASIFICACIÓN VIGENTE", _i) if _i >= 0 else -1
if _i < 0:
    _g16c.append("no se encuentra el bloque de clasificación VIGENTE de las condiciones")
elif _fin_vig < 0:
    _g16c.append("el bloque de clasificación vigente no se cierra con «FIN DE LA "
                 "CLASIFICACIÓN VIGENTE»: su alcance no es determinable")
else:
    _vigente = tchk[_i:_fin_vig]
    _fin_blq = tchk.find("= los trece ids distintos", _i)
    _blq = tchk[_i:_fin_blq if 0 < _fin_blq < _fin_vig else _fin_vig]
    for _est in _ESTADOS_CL:
        _m = re.search(rf"^\s*{re.escape(_est)}\s+(\d+)\s+(.*)$", _blq, re.M)
        if not _m:
            _g16c.append(f"falta el estado «{_est}»")
            continue
        _ini = _m.end()
        _sig = [_blq.find(e, _ini) for e in _ESTADOS_CL if _blq.find(e, _ini) > 0]
        _texto = _m.group(2) + " " + _blq[_ini: min(_sig) if _sig else len(_blq)]
        _ids = set(re.findall(r"\bC-L\.\d+\b", _texto))
        _declarado[_est] = int(_m.group(1))
        if _declarado[_est] != len(_ids):
            _g16c.append(f"«{_est}» declara {_m.group(1)} y nombra {len(_ids)} ids")
        for _x in _ids:
            _asig.setdefault(_x, []).append(_est)
        if re.search(r"\b[JKLMNO]-\d+\b", _m.group(2)):
            _g16c.append(f"«{_est}» cuenta un subhallazgo como condición: "
                         f"{re.findall(r'[JKLMNO]-[0-9]+', _m.group(2))}")

    _esperados = {f"C-L.{n}" for n in range(1, 14)}
    _faltan = sorted(_esperados - set(_asig), key=lambda x: int(x[4:]))
    _sobran = sorted(set(_asig) - _esperados)
    _dobles = sorted((k for k, v in _asig.items() if len(v) > 1), key=lambda x: int(x[4:]))
    if _faltan: _g16c.append(f"sin estado primario: {_faltan}")
    if _sobran: _g16c.append(f"ids que no son condiciones: {_sobran}")
    if _dobles: _g16c.append(f"con DOS estados primarios: {_dobles}")
    if sum(_declarado.values()) != len(_esperados):
        _g16c.append(f"la suma de los estados declara {sum(_declarado.values())} "
                     f"y las condiciones son {len(_esperados)}")

    # ── contraste contra la SEDE CANÓNICA: las trece filas de DETALLE ──────────
    # Sin esto, mover `C-L.12` de estado ajustando contadores pasaba en verde.
    _CANON = {
        "CORREGIDAS EN F4c":    ("CERRADA",),
        "REGISTRADAS PARA F5":  ("REGISTRADA PARA F5", "REGISTRADA"),
        "CONTRATADA PARA F6":   ("CONTRATADA PARA F6", "CONTRATADA"),
        "MIXTA POR DESGLOSE":   ("MIXTA",),
        "CERTIFICADA POR":      ("CERTIFICADA",),
    }
    _detalle = {}
    # el estado puede llevar dígitos —«REGISTRADA PARA F5», «CONTRATADA PARA F6»—, y una
    # clase que los excluya deja tres filas sin reconocer
    for _m in re.finditer(r"^\s*(C-L\.\d+)\s+([A-ZÁÉÍÓÚ][A-ZÁÉÍÓÚ0-9 ,]*?)(?:\s+·|\s*$)",
                          _vigente, re.M):
        _detalle.setdefault(_m.group(1), _m.group(2).strip())
    _sin_detalle = sorted(_esperados - set(_detalle), key=lambda x: int(x[4:]))
    if _sin_detalle:
        _g16c.append(f"sin fila de detalle en su sede: {_sin_detalle}")
    for _id, _estados in _asig.items():
        _det = _detalle.get(_id)
        if not _det:
            continue
        _admitidos = _CANON.get(_estados[0], ())
        if not any(_det.startswith(a) for a in _admitidos):
            _g16c.append(f"{_id}: el resumen lo pone en «{_estados[0]}» y su fila de detalle "
                         f"dice «{_det}»")

    # ── `C-L.13`: sus componentes se DERIVAN de la fila de detalle, no de una lista ──
    _m13 = re.search(r"^\s*C-L\.13\s+.*?(?=^\s*C-L\.\d|\Z)", _vigente, re.M | re.S)
    _comp13 = sorted(set(re.findall(r"\b[JKL]-\d+\b", _m13.group(0)))) if _m13 else []
    if _asig.get("C-L.13") != ["MIXTA POR DESGLOSE"]:
        _g16c.append(f"`C-L.13` no está exactamente una vez como MIXTA: {_asig.get('C-L.13')}")
    if len(_comp13) < 2:
        _g16c.append("`C-L.13` no declara sus componentes en su fila de detalle")
    _b13 = _blq[_blq.find("MIXTA POR DESGLOSE"):]
    _falt13 = [c for c in _comp13 if c not in _b13]
    if _falt13:
        _g16c.append(f"el resumen de `C-L.13` omite componentes que su detalle declara: {_falt13}")
    if _comp13 and not re.search(rf"{_comp13[0] if 'J-11' not in _comp13 else 'J-11'}"
                                 r"[^\n]*(?:contratad|NO implementad)", _b13, re.I):
        if "J-11" in _comp13:
            _g16c.append("`J-11` no consta como contratado para F6 y no implementado")
    if _asig.get("C-L.5") != ["CERTIFICADA POR"]:
        _g16c.append(f"`C-L.5` no está CERTIFICADA POR COBERTURA: {_asig.get('C-L.5')}")
    # `C-L.3` tiene que estar descrita por `D104` y NO por la regla que `M-01` refutó
    _m3 = re.search(r"^\s*C-L\.3\s+.*?(?=^\s*C-L\.\d|\Z)", _vigente, re.M | re.S)
    if not _m3 or "D104" not in _m3.group(0):
        _g16c.append("`C-L.3` vigente no nombra `D104`")
    if _m3 and re.search(r"cero o un par, nunca dos", _m3.group(0)):
        _g16c.append("`C-L.3` vigente conserva la regla de `D103` que `M-01` refutó")

_g16 = []
if len(filas) != 43 or len(set(ids)) != 43:
    _g16.append(f"matriz: {len(filas)} filas / {len(set(ids))} ids, se esperan 43 y 43")
if dup:
    _g16.append(f"matriz: ids DUPLICADOS {dup}")
# ESTADO COMPUESTO en la matriz: se detecta sobre la línea ENTERA, no sobre el grupo
# capturado. El grupo está restringido a [A-Z_0-9]+ y nunca podía contener " y " ni "+":
# la comprobación anterior era código muerto y no podía disparar jamás (`M-11`).
_comp = re.findall(r"^\| `([A-Za-z0-9-]+)` \| (?:BLOQUEANTE|GRAVE|MEDIO|MENOR) \| "
                   r"\*\*`[A-Z_0-9]+`(?: y |\s*\+\s*)`?[A-Z_0-9]+", tchk, re.M)
if _comp:
    _g16.append(f"matriz: estados COMPUESTOS {_comp}")
_g16 += [f"condiciones C-L: {x}" for x in _g16c]

# El mensaje de éxito se DERIVA de lo comprobado. La versión anterior llevaba la cadena
# «8+2+1+1+1 = 13» codificada, y la imprimía intacta sobre un bloque que declaraba otra
# distribución (`O-02`).
_resumen = "+".join(str(_declarado[e]) for e in _ESTADOS_CL if e in _declarado) \
           if not _g16c or _declarado else "?"
check("G-16",
      "un estado primario por elemento y ninguno compuesto: los 43 hallazgos, y las 13 condiciones `C-L` contra su detalle",
      not _g16,
      "; ".join(_g16) or
      f"matriz {len(filas)} filas / {len(set(ids))} ids · condiciones "
      f"{sum(_declarado.values())}/{len(_esperados)} con estado único, {_resumen} = "
      f"{sum(_declarado.values())}, cada resumen coincide con su fila de detalle · "
      f"C-L.13 MIXTA con {len(_comp13)} componentes derivados · C-L.5 CERTIFICADA")

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
# y la MATRIZ DE LOS 24 del gate del documento 21, con la misma disciplina: un id por
# fila, cada uno exactamente una vez, la severidad ADJUDICADA, y el recuento DERIVADO de
# las filas —no copiado— coincidiendo con el publicado. Ninguno puede declararse SUPERADO:
# corregido por quien lo recibió no es superado por revisión independiente.
_g17 = []
_m24 = re.findall(r"^\| \d+ \| `([A-Z]-\d+(?:≡[A-Z]-\d+)?)` \| \*\*(BLOQUEANTE|GRAVE|MEDIO|MENOR)\*\* \|(.*)$",
                  tchk, re.M)
if not _m24:
    _g17.append("no se encuentra la matriz de trazabilidad de los 24 hallazgos")
else:
    _ids24 = [a for a, _, _ in _m24]
    _dup24 = sorted(k for k, v in Counter(_ids24).items() if v > 1)
    if _dup24:
        _g17.append(f"matriz de los 24: ids duplicados {_dup24}")
    if len(_ids24) != 24:
        _g17.append(f"matriz de los 24: {len(_ids24)} filas y deben ser 24")
    _sev24 = Counter(b for _, b, _ in _m24)
    _der24 = [_sev24["BLOQUEANTE"], _sev24["GRAVE"], _sev24["MEDIO"], _sev24["MENOR"]]
    _pub24 = re.search(r"BLOQUEANTE\s+(\d+).*?GRAVE\s+(\d+).*?MEDIO\s+(\d+).*?MENOR\s+(\d+)",
                       tchk, re.S)
    if not _pub24:
        _g17.append("la matriz de los 24 no publica su recuento por severidad")
    elif [int(x) for x in _pub24.groups()] != _der24:
        _g17.append(f"matriz de los 24: publica {[int(x) for x in _pub24.groups()]} "
                    f"y las filas derivan {_der24}")
    _superados = [a for a, _, resto in _m24 if "SUPERAD" in resto.upper()]
    if _superados:
        _g17.append(f"matriz de los 24: se declaran SUPERADOS {_superados}, y quien aplica "
                    f"no certifica")
    _sin_estado = [a for a, _, resto in _m24 if "APLICADA, NO CERTIFICADA" not in resto]
    if _sin_estado:
        _g17.append(f"matriz de los 24: sin «APLICADA, NO CERTIFICADA» {_sin_estado}")

check("G-17", "los recuentos publicados coinciden con lo DERIVADO: las 43 filas y los 24 hallazgos del documento 21",
      pubv == derv and sum(derv) == 43 and not _g17,
      "; ".join(_g17) or
      f"derivado {derv} suma {sum(derv)} · publicado {pubv} · matriz de los 24: "
      f"{len(_m24)} ids únicos, severidades {_der24} = {sum(_der24)}")

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
if _base_raw is None:
    difs.append("GIT NO RESPONDE: no se puede comparar contra `7e99388`")
check("G-21", "`O1`-`O16` intactas frente a `7e99388` (y falla CERRADO si git no responde)",
      _base_raw is not None and bool(ob) and not difs and len(set(ac)) >= len(set(ob)),
      "ninguna difiere" if (_base_raw is not None and not difs) else ", ".join(difs))

# ── G-22 · los documentos 15, 16, 17 y 18 intactos ──────────────
# Se compara la BASE contra el ÁRBOL DE TRABAJO, no contra `HEAD`.
#
# Con `05f71b7 HEAD` se comparaban dos commits, y entonces `G-22` y `G-23` no veían nada de
# lo que hubiera sin confirmar: editar un contrato, una capacidad o cualquier otro validador
# dejaba la comprobación en verde. Una comprobación que sólo mira commits no protege el árbol
# que se le pone delante, que es justo lo que se le pide.
_tocados_raw = _git("diff", "--name-only", "05f71b7")
tocados = _tocados_raw.split() if _tocados_raw is not None else []
inmutables = [f for f in tocados if re.search(r"docs/evolucion/1[5-8]-", f)]
check("G-22", "los documentos 15, 16, 17 y 18 NO se han tocado (y falla CERRADO si git no responde)",
      _tocados_raw is not None and not inmutables,
      "intactos" if (_tocados_raw is not None and not inmutables)
      else (", ".join(inmutables) or "GIT NO RESPONDE: no se puede saber qué se tocó"))

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
# ── y la PROSA del checkpoint contrastada contra lo que Git deriva ────────
#
# Añadido por la verificación previa a publicación. El bloque «EXCEPCIÓN EXACTA DEL
# KERNEL» del checkpoint enumeraba la lista A MANO, y envejeció dos veces: primero
# decía «y sólo ésta» sobre TRES ficheros omitiendo `entrada/02-CIRCUITO.md` (`M-06`),
# y su corrección dijo «CUATRO rutas más la evidencia derivada» enumerando cuatro
# entradas de las cuales la cuarta ERA la evidencia — contándola dentro y fuera, y
# llamando «ruta» a una categoría junto a tres ficheros.
#
# Ahora la lista se CONTRASTA contra `git diff -- kernel/`: si el conjunto cambia y la
# prosa no, esto se pone en rojo. No hay ninguna cifra escrita aquí.
_kern = sorted(f for f in tocados if f.startswith("kernel/"))
_kern_ev = [f for f in _kern if "/pruebas/evidencia/" in f]
_kern_dir = [f for f in _kern if f not in _kern_ev]
_i_exc = tchk.find("EXCEPCIÓN EXACTA")
if _i_exc < 0:
    prohibidos.append("el checkpoint no declara la excepción exacta del kernel")
elif _tocados_raw is not None:
    # el bloque llega hasta la SIGUIENTE etiqueta de campo en columna 0, no hasta la
    # primera línea en blanco: el bloque tiene líneas en blanco dentro
    # la etiqueta del campo ocupa DOS líneas —«EXCEPCIÓN EXACTA / DEL KERNEL»—, luego se
    # busca la siguiente a partir de 200 caracteres, y no desde el principio
    _m_fin = re.search(r"^[A-ZÁÉÍÓÚ][A-ZÁÉÍÓÚ ]{4,}\s{2,}\S", tchk[_i_exc + 200:], re.M)
    _blq_exc = tchk[_i_exc: _i_exc + 200 + (_m_fin.start() if _m_fin else 4000)]
    # sólo se consideran RUTAS DE FICHERO: el último segmento tiene extensión. Una
    # mención en prosa a un directorio —«`kernel/operativo/` está intacto»— no es una
    # entrada del recuento y no debe contarse como sobrante.
    _listados = {f for f in re.findall(r"kernel/[A-Za-z0-9_./-]+", _blq_exc)
                 if "." in f.rsplit("/", 1)[-1]}
    _faltan_exc = [f for f in _kern if f not in _listados]
    _sobran_exc = [f for f in _listados if f not in _kern]
    if _faltan_exc:
        prohibidos.append(f"el checkpoint NO enumera ficheros del kernel tocados: {_faltan_exc}")
    if _sobran_exc:
        prohibidos.append(f"el checkpoint enumera ficheros que no se han tocado: {_sobran_exc}")
    # los recuentos publicados, contrastados contra lo derivado
    for _pat, _real, _que in (
        (r"TOTAL (\d+) = (\d+) directos \+ (\d+) de evidencia derivada",
         (len(_kern), len(_kern_dir), len(_kern_ev)), "total/directos/evidencia"),):
        _m = re.search(_pat, _blq_exc)
        if not _m:
            prohibidos.append("el checkpoint no publica el recuento «TOTAL n = n directos + n de evidencia derivada»")
        elif tuple(int(g) for g in _m.groups()) != _real:
            prohibidos.append(f"el checkpoint publica {_m.groups()} y Git deriva {_real} ({_que})")
    # ninguna categoría contada como fichero. Una CITA de la formulación vieja —entre
    # comillas angulares, para decir que era incorrecta— no es una afirmación viva: es la
    # misma distinción que `G-26` hace entre sede vigente y cita histórica.
    for _m_cat in re.finditer(r"(?:CUATRO|CINCO|SEIS|TRES) rutas más la evidencia", _blq_exc):
        _lin_ini = _blq_exc.rfind("\n", 0, _m_cat.start()) + 1
        _lin_fin = _blq_exc.find("\n", _m_cat.end())
        _lin = _blq_exc[_lin_ini: _lin_fin if _lin_fin > 0 else len(_blq_exc)]
        _dentro = any(c.start() <= _m_cat.start() - _lin_ini <= c.end()
                      for c in re.finditer(r"«[^»]*»", _lin))
        if not _dentro:
            prohibidos.append("el checkpoint cuenta la evidencia dentro de las rutas "
                              "Y otra vez fuera")

# ── y la TOPOLOGÍA REAL DEL ÁRBOL, no sólo el rango de Git ────────────────
#
# `Q-04` y la proposición de `M-04`. `git diff --name-only` lista ficheros RASTREADOS y
# MODIFICADOS: un fichero NUEVO SIN RASTREAR no aparece en su salida. Con eso, un árbol con
# una copia íntegra del catálogo de procesos —`01-PROCESOS-BIS.md`— y un contrato que
# declara POR ESCRITO que contradice a `C4` —`C8-SEGUNDA-SEDE.md`— pasaba **30/30 en
# verde**: la comprobación que promete «lo normativo intacto» no cubría la forma más simple
# de romperlo, que es AÑADIR una segunda sede de la misma verdad.
#
# Aquí se compara el CONJUNTO de ficheros del kernel en el ÁRBOL DE TRABAJO contra el
# conjunto en la revisión base, y se exige que las fuentes canónicas sean ÚNICAS. Se deriva
# de Git y del disco; no hay lista escrita a mano, y sin Git falla cerrado.
_CACHE = re.compile(r"(?:^|/)__pycache__/|\.pyc$")
_base_kern_raw = _git("ls-tree", "-r", "--name-only", "05f71b7", "--", "kernel/")
if _base_kern_raw is None:
    prohibidos.append("GIT NO RESPONDE: no se puede derivar el conjunto base del kernel")
else:
    _base_kern = {f for f in _base_kern_raw.split() if not _CACHE.search(f)}
    _disco_kern = set()
    for _r, _d, _f in os.walk(os.path.join(RAIZ, "kernel")):
        for _x in _f:
            _ruta = os.path.relpath(os.path.join(_r, _x), RAIZ).replace(os.sep, "/")
            if not _CACHE.search(_ruta):
                _disco_kern.add(_ruta)
    _nuevos = sorted(_disco_kern - _base_kern - COD_AUTORIZADO - DOC_AUTORIZADO - HUELLA)
    _idos = sorted(_base_kern - _disco_kern)
    if _nuevos:
        prohibidos.append(f"AMPLIACIÓN del kernel fuera de la excepción publicada, "
                          f"rastreada o no: {_nuevos}")
    if _idos:
        prohibidos.append(f"ficheros del kernel DESAPARECIDOS: {_idos}")

# unicidad de las fuentes canónicas: bajo `kernel/` —el espacio donde vive la verdad
# operativa— el catálogo de procesos ocupa UNA sede, y cuáles son se deriva de la revisión
# base, no se escribe. Fuera de `kernel/` un bloque igual es una CITA —el documento 11
# reproduce el formato para explicarlo— y citar no es duplicar la fuente.
_cat_base_raw = _git("grep", "-l", "yaml ads:proceso", "05f71b7", "--", "kernel/")
if _cat_base_raw is None:
    prohibidos.append("GIT NO RESPONDE: no se puede derivar dónde vivía el catálogo de procesos")
else:
    _cat_base = {l.split(":", 1)[1] for l in _cat_base_raw.split("\n") if ":" in l}
    _cat_disco = set()
    for _r, _d, _f in os.walk(os.path.join(RAIZ, "kernel")):
        for _x in _f:
            if not _x.endswith(".md"):
                continue
            _ruta = os.path.relpath(os.path.join(_r, _x), RAIZ).replace(os.sep, "/")
            try:
                if "yaml ads:proceso" in io.open(os.path.join(_r, _x), encoding="utf-8").read():
                    _cat_disco.add(_ruta)
            except (UnicodeDecodeError, OSError):
                continue
    _sedes_nuevas = sorted(_cat_disco - _cat_base)
    if _sedes_nuevas:
        prohibidos.append(f"SEGUNDA SEDE del catálogo de procesos bajo `kernel/`: "
                          f"{_sedes_nuevas}. La fuente única no admite copias")

# ── y el PUNTO DE ENTRADA no reproduce la excepción: REMITE ───────────────
#
# `R-02`. La sección «Siguiente acción exacta» —la que la cabecera del checkpoint designa
# como punto de entrada de un agente sin contexto— llevaba su PROPIA copia de la excepción
# del kernel, con TRES ficheros, mientras la sede derivada enumeraba SEIS. Es `M-06`
# reproducido en la misma tanda que lo declaraba corregido. Una lista copiada envejece sola:
# aquí se exige que esa sección REMITA a la sede derivada en vez de copiarla.
_i_sig = tchk.find("## Siguiente acción exacta")
if _i_sig < 0:
    prohibidos.append("el checkpoint no tiene sección «Siguiente acción exacta»")
else:
    _sig = tchk[_i_sig:]
    _rutas_sig = {f for f in re.findall(r"kernel/[A-Za-z0-9_./-]+", _sig)
                  if "." in f.rsplit("/", 1)[-1]}
    if _rutas_sig:
        prohibidos.append(f"«Siguiente acción exacta» copia rutas del kernel en vez de "
                          f"remitir a la sede derivada: {sorted(_rutas_sig)}")
    if "EXCEPCIÓN EXACTA" not in _sig:
        prohibidos.append("«Siguiente acción exacta» no remite al campo «EXCEPCIÓN EXACTA "
                          "DEL KERNEL», que es la sede derivada")

if _tocados_raw is None:
    prohibidos.append("GIT NO RESPONDE: no se puede saber qué se tocó")
check("G-23", "lo normativo intacto; la TOPOLOGÍA del kernel y la unicidad de las fuentes canónicas, derivadas; y la excepción contrastada contra la prosa (falla CERRADO sin git)",
      _tocados_raw is not None and not prohibidos,
      f"{len(_kern)} ficheros de kernel = {len(_kern_dir)} directos + {len(_kern_ev)} de "
      f"evidencia derivada, todos enumerados en el checkpoint"
      if (_tocados_raw is not None and not prohibidos) else ", ".join(sorted(set(prohibidos))))

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

def _sedes(patron, texto=None, contexto=None, ventana=6, por_bloque=False):
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
        # `§16 · presiones` no afirma «dieciséis presiones»: el numeral es el número de
        # sección. Una referencia a una sede no es un censo.
        if m.start() > ini and texto[m.start() - 1] == "§":
            continue
        if por_bloque:
            # la marca de histórico va en la primera línea de un campo de varias: se busca
            # en el BLOQUE, como hace `G-01` con la cuarentena
            _bi = texto.rfind("\n\n", 0, m.start()) + 2
            if _BLOQUE_HISTORICO.search(texto[_bi: fin if fin > 0 else len(texto)]):
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

# y el MISMO censo sobre el CHECKPOINT, que es el fichero que un agente lee al reanudar.
#
# `P-05`≡`Q-08`. La sección «Siguiente acción exacta» mandaba al Owner DOCE presiones donde
# el derivado daba TRECE, por SEGUNDA vez seguida sobre la misma línea —la corrección
# anterior, `I-28`, estaba escrita dos renglones más abajo—. Estos patrones sólo barrían el
# documento 11: la sede que va al Owner quedaba fuera del control que existe para ella.
for ln, val in _sedes(_NUM + r"\s+(?:presiones|PRESIONES)", tchk,
                      contexto=r"§16|vigente|VIGENTES|Owner", por_bloque=True):
    if val != n_pn:
        _fallos_26.append(f"c1) checkpoint L{ln}: dice {val} presiones y las cabeceras "
                          f"de §16 derivan {n_pn}")

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

# ── 26.e · la fila que BARRE TODAS LAS VENTANAS, contra las filas W ───────
#
# `P-01`≡`Q-13`. `X54` decía «las diecisiete ventanas» mientras §2.6.5 deriva DIECIOCHO de
# sus filas, y ninguna de las 46 filas adversariales nombraba `W17` — la ventana que `D105`
# creó para cerrar `M-03` y `O-03`. La tabla se declara convertible en pruebas de F6 «sin
# traducción»: lo que no tiene fila, no se prueba. Aquí el censo se DERIVA de las filas `W`
# y se contrasta contra el numeral de la fila que dice barrerlas todas.
_ws = re.findall(r"^\| \*{0,2}(W[0-9]+[ab]?)\*{0,2} \|", t11, re.M)
if not _ws:
    _fallos_26.append("e) no se encontró la tabla de ventanas de §2.6.5")
else:
    _x_barre = [l for l in t11.split("\n")
                if re.match(r"^\| `X[0-9]+` \|", l) and "ventanas" in l and "cada una" in l]
    if not _x_barre:
        _fallos_26.append("e) ninguna fila adversarial dice barrer todas las ventanas")
    for _l in _x_barre:
        _m = re.search(_NUM + r"\s+ventanas", _l)
        _v = _num(_m.group(1)) if _m else None
        _id = re.match(r"^\| `(X[0-9]+)`", _l).group(1)
        if _v != len(_ws):
            _fallos_26.append(f"e) `{_id}` dice {_m.group(1) if _m else '?'} ventanas y "
                              f"§2.6.5 deriva {len(_ws)} filas")
        if _ws[-1] not in _l:
            _fallos_26.append(f"e) `{_id}` barre todas las ventanas y no nombra `{_ws[-1]}`, "
                              f"que es la última que la tabla declara")

# ── 26.f · los RANGOS de presiones, no sólo los numerales ─────────────────
#
# `Q-07`. §16 decía «`PN-6` a `PN-14`» cuando ya existía `PN-15`, y omitía precisamente la
# que va al Owner. Es la TERCERA vez que esa frase caduca —`m2` y luego `I-11` la
# corrigieron—, y las dos veces anteriores se corrigió el numeral: un RANGO no es un
# numeral, y por eso `G-13` y `G-26` no lo veían. Aquí se deriva el último vigente de las
# cabeceras y se exige que todo rango VIVO termine en él.
_pn_vig = [int(n) for n, resto in re.findall(r"^## `PN-(\d+)` ·(.*)$", t11, re.M)
           if "RETIRADA" not in resto and "FUSIONADA" not in resto]
_ultimo = max(_pn_vig) if _pn_vig else None
for _txt, _quien in ((t11, "11"), (tchk, "checkpoint")):
    for _m in re.finditer(r"`PN-(\d+)`\s*a\s*`PN-(\d+)`", _txt):
        _ini = _txt.rfind("\n", 0, _m.start()) + 1
        _fin = _txt.find("\n", _m.end())
        _lin = _txt[_ini: _fin if _fin > 0 else len(_txt)]
        # la marca de histórico se busca POR BLOQUE y no por línea: un campo del registro
        # ocupa varias líneas y su etiqueta `[HISTÓRICO]` va en la primera, exactamente
        # como `G-01` hace con la cuarentena
        _bl_ini = _txt.rfind("\n\n", 0, _m.start()) + 2
        _bloque = _txt[_bl_ini:_fin if _fin > 0 else len(_txt)]
        if _es_cita(_lin, _m.start() - _ini, _m.end() - _ini) or \
           _BLOQUE_HISTORICO.search(_bloque):
            continue
        if int(_m.group(2)) != _ultimo:
            _fallos_26.append(
                f"f) {_quien} L{_txt.count(chr(10), 0, _m.start()) + 1}: el rango vivo "
                f"«PN-{_m.group(1)} a PN-{_m.group(2)}» no termina en la última vigente, "
                f"que es PN-{_ultimo}")

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
# `ancho = max(len(t) ...)` vivía aquí y se RETIRA: se calculaba en cada corrida y no lo
# leía nadie —las dos `f-string` de abajo usan anchos fijos—. Es `Q-15`, y es la misma
# clase que `M-11`: código que aparenta gobernar el formato y no gobierna nada.
print("BATERÍA MECÁNICA DE LA CORRECCIÓN DEL GATE DE CIERRE\n")
for id_, t, ok, det in RES:
    print(f"{'OK  ' if ok else 'FALLO'} {id_:7s} {t}")
    if det: print(f"{'':13s}└─ {det}")
verde = sum(1 for _, _, ok, _ in RES if ok)
print(f"\n{verde}/{len(RES)} comprobaciones en verde")
sys.exit(0 if verde == len(RES) else 1)
