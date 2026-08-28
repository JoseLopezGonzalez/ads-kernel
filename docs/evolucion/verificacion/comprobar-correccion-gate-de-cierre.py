#!/usr/bin/env python3
"""Bateria mecanica de la correccion del gate de cierre de F4c.

Cada comprobacion DERIVA su resultado del arbol. Ninguna cifra esta escrita a mano:
las que aparecen abajo son las EXIGIDAS, y el fallo se produce cuando lo derivado difiere.
"""
from __future__ import annotations
import io, os, re, subprocess, sys
from collections import Counter

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if not os.path.exists(os.path.join(RAIZ, "docs")):
    RAIZ = "/home/jose/ads-kernel"
D11 = os.path.join(RAIZ, "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md")
DEC = os.path.join(RAIZ, "docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md")
CHK = os.path.join(RAIZ, "docs/evolucion/CHECKPOINT-ADS-NEXT.md")
IDX = os.path.join(RAIZ, "docs/evolucion/00-INDICE.md")

def leer(p): return io.open(p, encoding="utf-8").read()
def lineas(p): return leer(p).split("\n")

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

# ── G-13 · doce presiones vigentes, DERIVADAS ────────────────────────
cab = re.findall(r"^## `PN-(\d+)` ·(.*)$", t11, re.M)
vigentes = [n for n, resto in cab if "RETIRADA" not in resto and "FUSIONADA" not in resto]
check("G-13", "DOCE presiones normativas vigentes, derivadas de sus cabeceras",
      len(cab) == 14 and len(vigentes) == 12,
      f"{len(cab)} cabeceras - 2 marcadas = {len(vigentes)} vigentes")

# ── G-14 · F-01 reclasificado ────────────────────────────────────────
tchk = leer(CHK)
m = re.search(r"^\| `F-01` \| (\w+) \| \*\*`([A-Z_0-9]+)`\*\* \|(.*)$", tchk, re.M)
cols = [c.strip() for c in m.group(3).split(" | ")] if m else []
ok = (m and m.group(2) == "PRESION_LISTA_PARA_F5"
      and cols[2] != "no" and cols[3] != "no")
check("G-14", "`F-01` reclasificado a `PRESION_LISTA_PARA_F5`, con requiere_f5 y requiere_f6",
      ok, f"estado={m.group(2) if m else '?'} f5={cols[2] if cols else '?'} f6={'sí' if cols and cols[3]!='no' else '?'}")

# ── G-15 · DOM/SEG condiciones + revision declarados para F6 ─────────
need = ["`<CAP>:revision`", "DESPUÉS de `VER`", "no sólo en `DEU` y `DEP`",
        "01-PROCESOS.md", "SU PRUEBA", "PROPIETARIO", "F6"]
i19 = t11.index("### `DOM` y `SEG` participan DOS veces")
b19 = t11[i19:t11.index("**Y dos más, que no son defectos de F4", i19)]
falta = [x for x in need if x not in b19 and x.replace("`","") not in b19]
noeditado = "F4 **no edita `01-PROCESOS.md`**" in b19 or "F4 no toca `01-PROCESOS.md`" in b19
check("G-15", "`<CAP>:revision` declarado para F6 con edicion, propietario y prueba, sin tocar el kernel",
      not falta and noeditado, "; ".join(falta) or "edicion, propietario, fase y prueba; kernel intacto")

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

# ── G-20 · D1-D95 sin hueco ──────────────────────────────────────
ns = sorted(int(x) for x in re.findall(r"^\| D(\d+) ", leer(DEC), re.M))
check("G-20", "`D1`-`D95` sin hueco y sin repetir",
      ns == list(range(1, 96)), f"D1-D{ns[-1]}, {len(ns)} filas, huecos {[i for i in range(1,ns[-1]+1) if i not in ns]}")

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
tocados = subprocess.run(["git", "-C", RAIZ, "diff", "--name-only", "05f71b7", "HEAD"],
                          capture_output=True, text=True).stdout.split()
inmutables = [f for f in tocados if re.search(r"docs/evolucion/1[5-8]-", f)]
check("G-22", "los documentos 15, 16, 17 y 18 NO se han tocado",
      not inmutables, "intactos" if not inmutables else ", ".join(inmutables))

# ── G-23 · (a) (b) E1 E2 K-1 C4 C7 y el kernel intactos ─────────
prohibidos = [f for f in tocados if f.startswith("kernel/operativo/")
              and not f.startswith("kernel/operativo/pruebas/evidencia/")]
prohibidos += [f for f in tocados if re.search(
  r"a-CAPACIDADES-APROBADA|b-RECORRIDO-APROBADA|a-ENMIENDA-E1|a-ENMIENDA-E2", f)]
check("G-23", "(a), (b), `E1`, `E2`, `C4`, `C7` y `kernel/operativo/` intactos",
      not prohibidos, "intactos" if not prohibidos else ", ".join(prohibidos))

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
faltan = [f for f in fuentes if not os.path.exists(os.path.join(RAIZ, f))]
fichas = sorted(os.listdir(os.path.join(RAIZ, "kernel/operativo/capacidades")))
check("G-24", "las CATORCE fuentes y las QUINCE fichas existen y son legibles",
      not faltan and len(fichas) == 15,
      f"14 fuentes ok, {len(fichas)} fichas" if not faltan else ", ".join(faltan))

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

# ── G-26 · tabla adversarial: filas = ids distintos ────────────
xs = re.findall(r"^\| \*{0,2}`(X[0-9]+)`\*{0,2} \|", t11, re.M)
check("G-26", "la tabla adversarial tiene tantas filas como ids distintos",
      len(xs) == len(set(xs)) and len(xs) == 45,
      f"{len(xs)} filas / {len(set(xs))} ids")

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
