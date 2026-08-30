# GATE INDEPENDIENTE DE CERTIFICACIÓN DE F4c — CON UNIVERSO DERIVADO

> **Veredicto del adjudicador `R`: `INSUFICIENTE PARA F5`.**
> **`F4c` NO se cierra y sigue ABIERTA. `F5` NO queda autorizada. Ningún hallazgo se ha
> corregido en esta pasada, y es deliberado.**

## 0 · Qué es este documento, y qué NO es

Es el registro **LITERAL** de los tres dictámenes de un gate independiente sobre la candidata
`4d231eef4ada99b3258f698b161f0e0148087e89`, publicada en
`review/f4c-post-gate-manifiestos-candidate-20260830`. Los tres se transcriben **enteros y sin
suavizar**, en §A, §B y §C. Lo escrito antes de §A lo escribe el **coordinador**, que no es
ninguno de los tres y que **no ha juzgado nada**: sólo reparte, registra y publica.

**No es una tanda de corrección.** El adjudicador no corrige lo que encuentra: adjudica y
devuelve. Corregir en la misma pasada vuelve a hacer que quien recibe sea quien aplica, y eso es
exactamente lo que este expediente lleva trece tandas sin poder aceptar como prueba.

## 1 · Los agentes, y su independencia

```text
REVISOR P      cadena de CUATRO relevos con contexto limpio y tramos DISJUNTOS
               P1  documento 11, L1-L4800
               P2  documento 11, L4801-L9494
               P3  DECISIONES-Y-CONTRADICCIONES · (a) CAPACIDADES · (b) RECORRIDO
               P4  KERNEL.md · contratos 00, C1, C5, C6, C7 · y el documento 21 AL FINAL
                   DICTAMINADOR: reprodujo a P1-P3 contra fichero y línea, RECHAZÓ seis de
                   sus hallazgos y rebajó tres, y cerró el dictamen de `P`

REVISOR Q      cadena de CINCO relevos con contexto limpio y tramos DISJUNTOS
               Q1  CHECKPOINT-ADS-NEXT · CHECKPOINT-OPERATIVO · 00-INDICE
               Q2  la batería · su README · el manifiesto anterior · 01-PROCESOS ·
                   00-OBLIGACIONES-Y-CIERRE · proceso.yaml   —relevo TÉCNICO
               Q3  documentos 19 · 20 · 10 · 12 · 13 · 14
               Q5  documento 15 · diseno/00 01 02 04 05 · las QUINCE fichas
                   —creado por el ADDENDUM 1, y después de commitearlo
               Q4  documento 21 AL FINAL
                   DICTAMINADOR: reprodujo por su cuenta los seis árboles defectuosos de Q2,
                   rebajó dos BLOQUEANTES a GRAVE y cuatro GRAVES más, declaró superado un
                   hallazgo de su propio relevo, y cerró el dictamen de `Q`

ADJUDICADOR R  recibió los dos dictámenes YA CERRADOS. Recalculó por sí mismo el universo,
               las asignaciones, las lecturas, la cobertura, las severidades, los recuentos y
               las condiciones de cierre. Verificó cada hallazgo contra fichero y línea.
               NO resolvió por mayoría: resolvió contra la fuente

INDEPENDENCIA  ninguno de los diez ha escrito F4, aplicado `D16`-`D106`, sido autor de
               ninguna corrección, ni sido revisor `A`-`R` en ningún gate anterior.
               `P` y `Q` trabajaron EN PARALELO y sin verse, y los dos lo declaran.
               `R` no vio ningún dictamen hasta que los dos estaban cerrados
```

**Por qué cadenas de relevo, dicho contra el propio interés.** El universo obligatorio derivado
son **41 174 líneas**, y sólo el documento 11 son 9 494. Un lector único no puede sostener el
lote entero en contexto limpio **y leerlo íntegro**; fingir que sí es la forma exacta en que tres
gates anteriores acabaron declarando cobertura que no tenían. El coste está declarado en el
manifiesto y lo repite `P4` en su dictamen: **ningún ojo único recorrió las 9 494 líneas del
documento 11 seguidas**, y el adjudicador lo pesó.

## 2 · La cobertura, y por qué NO es la razón del veredicto

**Es la primera vez que el universo obligatorio se DERIVA en vez de escogerse.** `P-08` había
encontrado que el manifiesto anterior declaraba «FUENTES SIN ASIGNAR 0» sobre un universo
**elegido**: el cero era verdadero por construcción. La regla `1bis` de `C-L.5` exige publicar la
REGLA y el COMANDO auditable. Aquí el comando existe, se publicó **en un commit propio y antes
que el manifiesto**, y es reejecutable:

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py
```

```text
UNIVERSO DERIVADO           59 fuentes · 41 174 líneas
                            superconjunto ESTRICTO de las 43 elegidas a mano del gate anterior:
                            ninguna de aquéllas se pierde, y entran DIECISÉIS más

MANIFIESTO DE ASIGNACIÓN    commiteado SOLO, antes de que existiera ningún revisor
                            `44d2e74` · 316 líneas
                            SHA-256 fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa06…

ADDENDUM 1                  commiteado SOLO, antes de que existiera el relevo que lo ejecuta
                            `706c787` · 120 líneas · devuelve 21 fuentes al reparto de lectura

OBLIGATORIO − ASIGNADO      ∅        recalculado por `R` con `comm`, en las dos direcciones
ASIGNADO − LEÍDO            ∅        47 asignadas a lectura · 47 leídas íntegras
AGOTADAS                    12       cada una con fila propia `LEÍDO ÍNTEGRO` en el documento
                                     21 y bytes idénticos a `7764cca`, verificado ruta a ruta

C-L.5                       SIGUE CERTIFICADA, y es la segunda vez consecutiva
```

Los dos documentos de reparto de este gate son
[`F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md`](verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md)
y
[`F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md`](verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md),
y el comando que deriva el universo es
[`derivar-universo-obligatorio.py`](verificacion/derivar-universo-obligatorio.py). Los tres se
publican con el gate, como exige `1bis`, y **el manifiesto del gate anterior**
—[`F4C-ASIGNACION-GATE-CIERRE-20260829.md`](verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md)—
queda intacto.

**El coordinador se equivocó, un revisor suyo lo encontró, y consta.** El manifiesto declaró 33
fuentes AGOTADAS; **veintiuna se apoyaban en una declaración de CONJUNTO del documento 20 que no
nombra ni una sola ruta**, procedente además de un gate cuyo adjudicador había declarado NO
CERTIFICABLE su propia regla de cierre. Lo encontró el relevo `Q3` leyendo el documento 20
íntegro, **antes de cualquier adjudicación**. El manifiesto **no se editó** —`1bis` lo declara
inmutable y sigue en `44d2e74` con su error dentro—: se publicó el `ADDENDUM 1`, que devolvió las
21 a lectura íntegra, se creó el relevo `Q5` **después** de commitearlo, y `Q5` las leyó las 21.
El adjudicador juzgó expresamente esa conducta en §11 de su adjudicación.

## 3 · El veredicto, y sus seis razones

```text
VEREDICTO   INSUFICIENTE PARA F5

1  `M-04` sigue FALLIDA y hoy es MÁS ANCHA. El adjudicador construyó y ejecutó OCHO árboles
   defectuosos que pasan la batería 30/30 EN VERDE —los seis de `Q` más dos suyos—. El peor
   es suyo: volteó los veredictos de los documentos 19, 20 y 21 a `SUFICIENTE PARA F5` y la
   batería no se enteró, porque su rango inmutable dice `1[5-8]`

2  las CINCO correcciones de la batería funcionan en el PERÍMETRO EXACTO de su contraejemplo
   y en ninguna otra parte, verificado en las dos direcciones. `G-26` se desactiva escribiendo
   «regresión» en la línea, y con esas dos palabras se reinstala el único GRAVE del gate
   anterior: la cifra falsa hacia el Owner en el punto de entrada

3  `R-04` NO está superado: está AGRAVADO. El punto 7 de §2.6.9 es byte-idéntico a `7764cca`,
   y la fila de `W17` afirma que ese punto reparte algo que no reparte. La corrección escribió
   en norma un error de hecho del adjudicador anterior

4  DOS GRAVES nuevos que ningún gate había visto, y los dos rompen una garantía publicada
   sobre material APROBADO: el nivel ESTRUCTURAL no lo produce ninguna fase —luego `O12` no es
   satisfacible—, y `reconciliacion_pendiente` no tiene productor —luego `T22` de (a) no es
   satisfacible, y ninguna presión lo registra—

5  la regla que la tanda adoptó como remedio de su único GRAVE NO EJECUTA: §15.8 no tiene
   bloque para `D96`-`D106`, y `00-INDICE` se contradice dentro de una sola tabla

6  y la razón de método: de los 69 hallazgos distintos, la mayoría los introdujo o los dejó
   pasar esta misma tanda, y cuatro son la reinstalación de defectos ya adjudicados
```

```text
69 HALLAZGOS DISTINTOS     27 de `P` · 42 de `Q` · 3 propios de `R` · menos 3 solapes

  BLOQUEANTE    0
  GRAVE         8
  MEDIO        34
  MENOR        27

LOS 24 DEL DOCUMENTO 21    20 SUPERADOS · 4 NO SUPERADOS (`P-06` `Q-04` `Q-05` `R-04`)

CLASIFICACIÓN              A · corregible en F4c sin decidir arquitectura       68
                           B · DECISIÓN EXCLUSIVA DEL OWNER                      1
                           C · trabajo futuro ya contratado                      0
```

## 4 · La ÚNICA decisión que este gate devuelve al Owner

Sesenta y ocho de los sesenta y nueve hallazgos tienen remedio determinado y **no exigen decidir
arquitectura**. **Uno sí**, y por eso el trabajo se detiene aquí y no continúa solo: el nivel
**ESTRUCTURAL** y su productor. La pregunta exacta, con sus tres alternativas y el coste de cada
una, está formulada palabra por palabra en **§13 de la adjudicación de `R`**, más abajo en este
mismo documento. **F4 no elige ninguna, y lo dice.**

## 5 · Lo que este gate SÍ ha cerrado

```text
· `C-L.5` CERTIFICADA por segunda vez consecutiva, y esta vez sobre un universo DERIVADO.
  Dos de los cinco componentes del derivador se leen de sede normativa y FALLAN CERRADO bajo
  ataque; `R` lo atacó
· VEINTE de los veinticuatro hallazgos del documento 21, verificados uno a uno contra el
  árbol — incluido el ÚNICO GRAVE de aquel gate
· las CINCO vías nombradas de la batería, con control positivo del adjudicador
· `Q-14` y `C-L.3`, cerrados
· ONCE de las trece condiciones `C-L`, con estado único y ninguna mal clasificada
· los VEINTIDÓS hallazgos del documento 15, cerrados uno a uno — leído íntegro por primera vez
  por ruta en este gate
· los documentos 10, 12, 13 y 14, leídos íntegros por primera vez: NO producen ni un hallazgo
  vivo contra el árbol
· `PN-16` registra la elección de grafía y NO la elige, que es exactamente lo que debía hacer
· `D1`-`D106` y `O1`-`O16` intactas; documentos 15-21 sin tocar
```

## 6 · Estado del árbol durante el gate

```text
MODO SÓLO LECTURA    los diez agentes comprobaron `git status --porcelain` VACÍO al abrir y al
                     cerrar, y los diez lo declaran en su informe
FICHEROS DEL REPOSITORIO MODIFICADOS POR UN REVISOR    ninguno
EXPERIMENTOS         íntegramente fuera del repositorio, sobre copias en /tmp, borradas
CANDIDATA            `4d231ee` · el runner del kernel da 13/13 y deja el árbol limpio,
                     ejecutado por `Q1`, por `Q4` y por `R`
```

---

# §A · DICTAMEN DEL REVISOR `P`, LITERAL

# DICTAMEN DEL REVISOR `P` — GATE INDEPENDIENTE DE CERTIFICACIÓN DE F4c

Emitido por `P4`, DICTAMINADOR de la cadena `P`.
Repositorio `/home/jose/ads-kernel` · rama `gate/f4c-certificacion-20260830` · HEAD `706c787189c2241124d0df467f18eb5c5b60667b`.

---

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

Soy `P4`, el dictaminador del REVISOR `P`. Cierro el dictamen de `P` y **no** emito veredicto:
el veredicto lo emite el adjudicador `R`.

**La cadena.** `P` se realiza como cuatro relevos con contexto limpio y tramos disjuntos:

```text
P1   docs/evolucion/11-ARQUITECTURA-INTEGRADA.md   L1-L4800
P2   docs/evolucion/11-ARQUITECTURA-INTEGRADA.md   L4801-L9494
P3   DECISIONES-Y-CONTRADICCIONES.md · a-CAPACIDADES-APROBADA.md · b-RECORRIDO-APROBADA.md
P4   kernel/KERNEL.md · los cinco contratos asignados · y, EN ÚLTIMO LUGAR, el documento 21
```

**Qué NO he visto.** No he leído ningún fichero `Q*.md` del directorio de notas. No he visto el
dictamen de `Q` ni ninguna nota de sus relevos. `P` y `Q` han trabajado en paralelo y sin verse.
No he escrito ninguna parte de este corpus, no he aplicado ninguna corrección, no soy autor de
nada de lo que juzgo y no he sido revisor en ningún gate anterior.

**El orden se ha respetado, y es la garantía de que este dictamen busca en vez de confirmar.**
Leí íntegro mi propio lote —`KERNEL.md` y los cinco contratos— y reproduje contra el árbol los
hallazgos de `P1`, `P2` y `P3` **antes** de abrir
`docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md`. Ocho de mis veintisiete hallazgos
consolidados —`P-01`, `P-02`, `P-06`, `P-07`, `P-08`, `P-10`, `P-11`, `P-12`, `P-13`, `P-17`—
estaban formulados antes de saber qué contenía el documento 21.

**Modo sólo lectura, comprobado en los dos extremos.**

```text
AL ABRIR    git status --porcelain  →  SALIDA VACÍA
AL CERRAR   git status --porcelain  →  SALIDA VACÍA
```

No he editado, creado ni borrado ningún fichero del repositorio. No he hecho commit, push, PR ni
merge. No he usado el subagente `Agent`. El único fichero que escribo es este dictamen, fuera del
árbol, en el scratchpad de la sesión. Los tres relevos declaran lo mismo en sus informes.

**Nota sobre el HEAD.** El manifiesto reparte el commit candidato `4d231ee` / árbol `02ba78c`.
El HEAD de hoy es `706c787`, y comprobé la diferencia yo:

```text
$ git diff --stat 4d231ee 706c787
 derivar-universo-obligatorio.py                    | 289 +++
 F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md      | 119 +++
 F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md      | 316 +++
 3 files changed, 724 insertions(+)
```

**Cero supresiones y cero cambios en el objeto juzgado.** Los tres ficheros añadidos son el
aparato del propio gate. Las once fuentes de `P` son byte a byte las del árbol repartido: los
once SHA-256 que recalculé coinciden con los once del manifiesto.

---

## 2 · MANIFIESTO DE LECTURA DEL REVISOR `P`

**Comprobación de la asignación, hecha por mí.** Abrí
`docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` (commit
`44d2e74`) y conté las filas de §4 marcadas `P` o `P+…`: son las filas **3, 9, 15, 16, 17, 18, 19,
20, 21, 22 y 23** — diez fuentes propias más el documento 21, que es `P+Q+R`. **Once.** Coincide
con el encargo. Abrí también el `ADDENDUM 1` y **confirmo que no toca el lote de `P`**: reasigna
veintiuna fuentes, todas a `Q · relevo Q5`.

**La unión de los cuatro manifiestos. Todos los SHA-256 recalculados por mí con `sha256sum` sobre
el árbol de HEAD; los de `P1`, `P2` y `P3` recalculados además por ellos, y coinciden.**

| # | ruta | líneas | SHA-256 | leyó | cobertura | primera y última sección sustantiva | dos anclas de regiones separadas |
|---|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 9494 | `ebbd3311f1016c05f5f96ab1673144feecc0f1de3a55e5ac7731ce0ddab2def0` | **P1** L1-L4800 · **P2** L4801-L9494 | **LEÍDO ÍNTEGRO por la cadena.** Ningún tramo sin abrir. **Reserva declarada: ningún ojo único recorrió las 9 494 líneas seguidas** | primera `# 0 · Resumen ejecutivo` L92 · última `## C-L.5 · La condición de COBERTURA…` L9390 | L664 `` abierta(tx) ≡ ∃ `preparada` DURABLE con ese `tx` `` · L9483 `**Estado: CERTIFICADA por el GATE INDEPENDIENTE DE CIERRE CON MANIFIESTOS VERIFICABLES**` |
| 2 | `docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` | 2679 | `9f869ffbdbdb834ca872c03abc8826c125a47b4344ed32cd9b6266db08f8be03` | **P4** | **LEÍDO ÍNTEGRO**, y **DESPUÉS** del resto del lote de la cadena | primera `## 1 · Identidad y procedencia` L9 · última `## 14 · Ningún hallazgo se ha corregido, y es deliberado` L2663 | L2137 `` `R-04` · MENOR · la sub-ventana del marcador que `W17` nombra queda fuera de su propia condición de detección `` · L2590 `# INSUFICIENTE PARA F5` |
| 3 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 725 | `3be45994f4d00e82d4a136a2140c738b926a3baee4811e757d523125e4239959` | **P3** | **LEÍDO ÍNTEGRO**, quince tramos consecutivos sin salto | primera `## 1 · Decisiones tomadas sin consultar` L11 · última `## 4 · Límites declarados de esta iteración` L707 | L18 fila `D1` · L723 «La coherencia PROSA↔BLOQUE dentro de un mismo fichero no» |
| 4 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | **P3** | **LEÍDO ÍNTEGRO**, once tramos consecutivos sin salto | primera `## a.0 — Tres niveles` L22 · última `## a.12 — Pruebas de conformidad derivables` L1032 | L36 «**Regla de categoría** (deroga "sombreros, no saltos")» · L1110 prueba `T22` |
| 5 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | **P3** | **LEÍDO ÍNTEGRO**, doce tramos consecutivos sin salto | primera `## b.1 — Proceso, item, ruta, paquete` L14 · última `## b.17 — Pruebas de conformidad de la sección (b)` L1101 | L207 `P0 reconciliacion_pendiente` · L1233 prueba `T63` |
| 6 | `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | **P4** | **LEÍDO ÍNTEGRO.** Seis tramos: 1-220 · 220-480 · 480-640 · 636-770 · 770-1030 · 1030-1300 · 1300-1590 | primera `## K-1 — Arquitectura de tres capas` L10 · última `### G50 — Regla final de separación` L1586 | L4 `**Versión del kernel:** 1.5.0` · L690 «El gate de salida del Circuito 0 lo fija este documento y **NO es negociable por el sistema** (G22)» |
| 7 | `kernel/operativo/contratos/00-INDICE.md` | 29 | `0b9562119f0b5b5c3f59e66c09446129fbe56865983d6424b76825bf570d004c` | **P4** | **LEÍDO ÍNTEGRO** | primera `# Contratos transversales` L1 · última `## Lo que estos siete contratos garantizan juntos` L15 | L7 «los siete conceptos y los **veintiocho** campos del contrato de rol» · L28 «Cada garantía tiene su prueba en `../pruebas/`» |
| 8 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | **P4** | **LEÍDO ÍNTEGRO** | primera `## Los siete conceptos, y qué se rompe al confundirlos` L7 · última `## Cómo se lee un contrato de rol para ocuparlo` L150 | L37 `## Contrato común de rol — **veintinueve** campos` · L119 «El contrato fija el MÍNIMO; la composición puede exigir MÁS» |
| 9 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | **P4** | **LEÍDO ÍNTEGRO** | primera `## La regla que evita el rebote infinito` L17 · última `## Handoff y checkpoint` L105 | L17 «QUIEN RECIBE COMPRUEBA ANTES DE TOMAR CUSTODIA» · L113 «El emisor NO explica su trabajo al receptor» |
| 10 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | **P4** | **LEÍDO ÍNTEGRO** | primera `## La relación que sustituye a la anterior` L14 · última `## Lo que este contrato no autoriza` L326 | L26 `## Los catorce principios` (`N1`-`N14`) · L266 `` id: gate:workspace-conforme `` |
| 11 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | **P4** | **LEÍDO ÍNTEGRO** | primera `## Qué se conserva de G29, y qué se deroga` L15 · última `## Lo que este contrato no promete` L243 | L82 fila «materializar una fuente \| `DSP` al despachar \| `PLT`» · L170 `aplica_a: "todo item cuyos paquetes escribieron en **una o más** fuentes"` |

### La resta, explícita

```text
FUENTES ASIGNADAS A `P`            11   (10 propias + el documento 21, verificado por mí
                                        contra §4 del manifiesto `44d2e74` y contra el
                                        ADDENDUM 1, que no toca el lote de `P`)

FUENTES LEÍDAS ÍNTEGRAS POR `P`    11

ASIGNADAS − LEÍDAS ÍNTEGRAS  =  0     CERO. Ninguna fuente asignada a `P` quedó sin abrir.
```

**Y la reserva que declaro contra mi propio interés, porque la resta sola la esconde.** El
documento 11 está leído íntegro **por la cadena**, en dos tramos disjuntos, y no por un lector
único. Una contradicción entre §2 y §9 —regiones separadas por 5 000 líneas— es estructuralmente
más difícil de ver así. Lo mitigué reabriendo yo mismo §0, §2.6.4, §2.6.5, §2.6.6, §2.6.9, §2.9,
§3.6, §8.1, §9.1, §9.2, §15.4, §15.7, §15.8, §16, §17 y §19, y con `grep` cruzado. **No lo
elimina, y el adjudicador tiene que pesarlo.**

---

## 3 · HALLAZGOS DE `P`, CONSOLIDADOS

Veintisiete. **Severidad ADJUDICADA POR MÍ**, no la que propusieron los relevos: he subido una,
bajado cinco y rechazado seis (§4). Criterio declarado: **GRAVE** = una garantía publicada no se
sostiene, o `F6` construiría algo distinto de lo que el contrato quiere; **MEDIO** = una
afirmación vigente es falsa sin cambiar el comportamiento; **MENOR** = editorial o de
propagación.

---

### `P-01` · **GRAVE** · `W17` y el punto 7 de §2.6.9 se contradicen sobre el tramo `[paso 4, paso 5)`, y `W17` cita al punto 7 como la sede que le da la razón

**Fichero y líneas:** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L1172** (`W17`) contra
**L1938-L1941** (§2.6.9 punto 7), sobre los seis pasos del paso E de **L1874-L1889**.

**Cita literal, `W17`, L1172:**

> «**caída de MÁQUINA entre el `abandonada` durable y el `deriva` durable** —y **sólo** ese
> tramo: la caída POSTERIOR al `deriva`, con su marcador aún sin retirar, **la cubre `W8`** con
> §2.9 y la fila `X60`, **y así lo reparte el punto 7 de §2.6.9** (`R-04`) | terminal
> `abandonada` presente **sin ningún `deriva` que lo referencie por `abandonada_id`**, y el
> marcador de transacción **todavía puesto** |»

**Cita literal, el punto 7, L1938-L1941:**

> «caída antes del paso 1 → la transacción sigue abierta: `W11` … · **caída entre 1 y 5 →
> `W17`**: se completa el `deriva`, idempotente · **caída entre 5 y 6 → se retira el marcador de
> transacción, idempotente, que es `W8`** · caída después de 6 → nada que hacer»

**Los seis pasos (L1874-L1889):** 1 emitir `abandonada` · 2 `fsync` de `abandonada` y su dir ·
3 emitir el `deriva` · 4 `fsync` del `deriva` y su dir · 5 crear el marcador del `deriva` ·
6 retirar el marcador de transacción.

**Por qué es defecto.** El tramo `[4, 5)` —`deriva` ya durable, su marcador aún sin crear,
marcador de transacción todavía puesto— cae dentro de «caída entre 1 y 5», luego el punto 7 lo
asigna a **`W17`**. `W17` lo **expulsa por dos vías a la vez**: por su alcance («y **sólo** ese
tramo … la cubre `W8`») y por su **condición de detección**, que exige «sin ningún `deriva` que lo
referencie por `abandonada_id`» — falsa en `[4, 5)`, porque el `deriva` existe. Y el punto 7 sólo
da a `W8` el tramo «entre 5 y 6». **Ninguna de las dos ventanas se queda el caso, y `W17` afirma
por escrito que el punto 7 hace un reparto que el punto 7 no hace.**

**Y esto es lo que convierte el hallazgo en GRAVE: la corrección de `R-04` introdujo la
contradicción.** Comparé el árbol juzgado por el gate anterior con el de hoy:

```text
$ git show 7764cca:…/11-ARQUITECTURA-INTEGRADA.md | sed -n '1163p'
| **W17** | caída de MÁQUINA entre el `abandonada` durable y el `deriva` durable
           —o entre el `deriva` y su marcador— | …
$ git show 7764cca:…/11-ARQUITECTURA-INTEGRADA.md | sed -n '/CÓMO RECUPERA EL/,+3p'
7 CÓMO RECUPERA EL … caída entre 1 y 5 → **`W17`** … caída entre 5 y 6 → … `W8`
```

**El punto 7 es IDÉNTICO en los dos árboles: no se tocó.** Lo que la tanda hizo fue **recortar el
alcance de `W17`** para quitarle el tramo, apoyándose en una afirmación sobre el punto 7 que es
falsa. Es exactamente el error de hecho que el adjudicador `R` cometió al desestimar la
refutación de `P` (doc 21 L2137: «*el reparto de §2.6.9 punto 7, que lo asigna a `W8`*»): **la
tanda copió el error del adjudicador en el texto normativo en vez de corregir el reparto.**

**Quién lo levantó.** `P1`, como `P1-05` (frontera alta), sin haber visto el documento 21.
**Lo REPRODUJE** leyendo L1162, L1172, L1874-L1889 y L1938-L1941, y lo elevé con el `git show`
contra `7764cca`, que `P1` no podía hacer porque no conocía `R-04`.

**Qué NO afirmo.** `P1` sostenía que el tramo deja el control repo **permanentemente bloqueado**.
**Lo rechazo** (§4, `X-2`).

---

### `P-02` · **GRAVE** · el punto 7 asigna a `W17` el tramo `[paso 1, paso 2)`, donde el `abandonada` puede no existir y `W17` exige que sea DURABLE

**Fichero y líneas:** **L1938-L1941** contra **L1172** y contra la garantía 3 de §2.6.6
(**L1231-L1260**).

**Por qué es defecto.** Caída entre el paso 1 (emitir `abandonada`) y el paso 2 (su `fsync` y el
de su directorio). Por la propia garantía 3 de §2.6.6 —«DURABILIDAD FRENTE A CAÍDA DE MÁQUINA:
exige `fsync` DEL FICHERO y `fsync` DEL DIRECTORIO»— ese evento **puede haberse perdido entero**.
`W17` exige literalmente «el `abandonada` **durable**», luego no aplica: el caso correcto es
`W11`, transacción todavía abierta, que es la primera rama del propio punto 7. **El punto 7 lo
mete en `W17`.**

**Quién lo levantó.** `P1` (frontera baja de `P1-05`). **Lo REPRODUJE** contra las tres sedes.
**Lo separo de `P-01` porque el remedio es distinto**: `P-01` se cierra decidiendo quién cubre
`[4,5)`; `P-02` se cierra cambiando «entre 1 y 5» por «entre 2 y 5». **Ningún hallazgo del
documento 21 registra esta frontera** — ni `P-03`, ni `R-04`, ni ninguno de los veinticuatro.
Es nueva.

---

### `P-03` · **GRAVE** · §0 declara derivar de §15.8 un recuento que §15.8 ya no puede sostener: once decisiones vigentes no tienen bloque

**Fichero y líneas:** **L12-L15** (§0) contra **L7670-L7865** (§15.8).

**Cita literal, L12-L15:**

> «**F4 no está certificada, y este texto ha sido CORREGIDO DOCE VECES.** El recuento se
> **DERIVA** de los bloques de corrección de §15.8, y son doce: … y `D71`–`D86`. **La
> decimotercera es ésta**, `D87` en adelante, y por eso la cifra vuelve a moverse.»

**Cómo lo reproduje.**

```text
$ awk 'NR>=7654 && NR<=7910 && /^### /' …/11-ARQUITECTURA-INTEGRADA.md
  → TRECE bloques. El decimotercero es `D87`–`D95`, con su rótulo propio.
$ grep -n '^### `D9[6-9]\|^### `D10' …/11-ARQUITECTURA-INTEGRADA.md
  → (vacío)
```

**Por qué es defecto. Dos cosas a la vez.** (a) «La decimotercera es ésta, `D87` en adelante» ya
no describe una tanda en curso: está escrita, cerrada y rotulada. (b) **`D96`–`D106` —once
decisiones vigentes, entre ellas `D97`, `D104`, `D105` y `D106`, que son las que este gate
juzga— no tienen ningún bloque en §15.8.** La sede de la que la cifra dice derivarse está
incompleta en dos tandas enteras, luego la cifra no puede derivarse de ella. Es la patología que
el propio §0 declara cerrada tres líneas más abajo: «*Un recuento que se declara derivado se
deriva, o se retira la afirmación de que deriva*».

**Quién lo levantó.** `P1` (`P1-02`). **REPRODUCIDO** con los dos comandos de arriba.

---

### `P-04` · **GRAVE** · §0: el titular dice CATORCE y la aposición que dice DERIVARLO termina en TRECE, en la misma frase

**Fichero y líneas:** **L126-L133**.

**Cita literal:**

> «este diseño presiona material aprobado en **CATORCE** puntos … El recuento **se DERIVA de
> §16** y se mueve cuando aparece algo no contado: fueron ocho, `PN-11`, `PN-12` y `PN-13` lo
> llevaron a once, `PN-14` a doce, y **`PN-15` lo lleva a trece**.»

**Por qué es defecto.** Titular **CATORCE**, cadena derivante **trece**, y la cadena **omite
`PN-16`**, que §19 declara «la única que esta tanda añade». El titular es correcto; **lo roto es
exactamente la derivación**, que es la mitad de la que el documento hace depender la cifra.

**Cómo lo reproduje.**

```text
$ grep -c '^## `PN-' …/11-ARQUITECTURA-INTEGRADA.md              → 16
$ grep '^## `PN-' … | grep -vc 'RETIRADA\|FUSIONADA'             → 14   (PN-4 y PN-5 fuera)
```

**Agravante.** §16 SÍ recibió esta corrección en esta misma tanda: L7920 dice ahora «`PN-6` a
`PN-16`» y L7923 registra «**Corregido otra vez por `Q-07`**: decía `PN-6` a `PN-14`». **El §0 —el
único tramo que el Owner lee entero— es el que no se reancló.**

**Quién lo levantó.** `P1` (`P1-01`). **REPRODUCIDO.**

---

### `P-05` · **GRAVE** · `P-06` del documento 21 está corregido en el documento 11 y **NO** en el registro de decisiones: `D97` sigue afirmando en presente un recuento que su propio commit falsificó

**Fichero y línea:** `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` **L346**, columna de
justificación de la fila `D97`.

**Cita literal:**

> «`G20`, `G21` y `G23` tienen **cero** apariciones en el documento 11, en (a), en (b) y en `E2`;
> `G22` tiene UNA, como cita de apoyo.»

**Cómo lo reproduje.**

```text
$ for g in G20 G21 G22 G23; do printf "%s: " $g; grep -c "$g" …/11-ARQUITECTURA-INTEGRADA.md; done
G20: 12   G21: 10   G22: 16   G23: 13
$ for g in G20 G21 G22 G23; do printf "%s: " $g; \
    git show d868bcb^:…/11-ARQUITECTURA-INTEGRADA.md | grep -c "$g"; done
G20: 0    G21: 0    G22: 0    G23: 0
```

`d868bcb` es «*fix(f4c): aplicar la tanda … `D96`–`D102`, `PN-15` …*», el commit que introdujo
`D97`. **La decisión falsificó su propia justificación en el mismo commit en que la escribió.**

**Por qué es defecto AHORA, y no sólo entonces.** La misma frase se corrigió en el documento 11:
**L8400** dice hoy «*Esta sede decía «cero apariciones en el documento 11», y era falsa*». **En el
registro no.** Es el patrón exacto que el veredicto del documento 21 nombra como su cuarta razón:
la corrección llega a la mitad de los sitios. Dictamen expreso en §6.

**Quién lo levantó.** `P3` (`P3-01`). **REPRODUCIDO** con los dos comandos y con el `git show`.

---

### `P-06` · **GRAVE** · el nivel **Estructural** no lo produce ninguna fase de ningún macrocircuito, y por §9.2 eso hace inalcanzables la Operativa de `INS-4`, la Integrada de `A9`/`M5`/`INS-7` y con ellas `O12`

**Fichero y líneas:** §9.1 **L6790** · §9.2 **L6901-L6916** · §8.1 **L6133** · §8.2 **L6329** ·
§8.3 **L6519** · §8.4 **L6701**.

**Citas literales:**

> **L6901-L6906 (§9.2):** «`estructural ◀── operativo ◀── integrado ◀── completo` / presupone
> presupone presupone … **NIVEL ALCANZADO** el mayor nivel cuya celda está `verificado` Y
> VIGENTE, **y** cuyos niveles presupuestos están todos `verificado` y vigentes.»
>
> **L6916:** «**REGLA DURA** un nivel **no se declara por argumento ni por haber pasado el
> anterior**.»

**Cómo lo reproduje.**

```text
$ grep -n 'sistema-conforme' …/11-ARQUITECTURA-INTEGRADA.md
6790:| **Estructural** | … los validadores del manifiesto + `gate:sistema-conforme` | `SIS` | …
  → UNA sola aparición en TODO el documento, y es la DEFINICIÓN del nivel.

$ grep -n 'CERTIFICACIÓN' … | awk -F: '$1>6100 && $1<6800'
6133: Operativa en INS-4 · Integrada en INS-7      6329: Integrada en A9
6519: Integrada en M5, ANTES de retirar nada       6701: el nivel que tuviera antes, revalidado
  → NINGUNA menciona Estructural. Ninguna fase lo produce ni invoca su gate.
```

**Por qué es defecto.** Sin celda de Estructural `verificado` y vigente, la definición de «nivel
alcanzado» impide que la Operativa de `INS-4` eleve nada, y con más razón la Integrada de `A9`,
`M5` e `INS-7`. **En la adopción es peor: `A9` certifica Integrada sin que ninguna fase produzca
ni Estructural ni Operativa.** `O12` —«Integrada + baseline + ningún desconocido crítico»— no es
satisfacible por ninguno de los cuatro recorridos. Es el modo de fallo que el expediente ya cerró
una vez como `G-3`/`D76` —«el gate era invocable pero no satisfacible»— reaparecido un piso más
arriba, en la jerarquía de niveles.

**Quién lo levantó.** `P2` (`P2-02`). **REPRODUCIDO** con los dos barridos. **Ninguno de los
veinticuatro hallazgos del documento 21 lo registra.**

---

### `P-07` · **GRAVE** · `reconciliacion_pendiente` del canal de órdenes no tiene productor: la prueba `T22` de material APROBADO no es satisfacible y el freno 4 de `b.12` no tiene disparador

**Ficheros y líneas:** `a-CAPACIDADES-APROBADA.md` **L795** y **L1109-L1111** (`T22`) ·
`b-RECORRIDO-APROBADA.md` **L615** · `DECISIONES-Y-CONTRADICCIONES.md` **L127** (`D49`) ·
`11-ARQUITECTURA-INTEGRADA.md` **L1739** contra **L1765-L1772**.

**Cita literal, (a) L1109-L1111, prueba de conformidad APROBADA:**

> «`T22 CAS LÍMITE  Tres fallos CAS consecutivos detienen el ciclo, dejan las órdenes intactas y
> **registran `reconciliacion_pendiente`**. No existe un cuarto giro automático.»

**Cita literal, doc 11 L1765-L1772, la definición vigente:**

> «#### `reconciliacion_pendiente` sigue siendo un **PREDICADO DERIVADO** …
> `reconciliacion_pendiente(item) ≡` existe una transacción con evento `conflicto` **SIN
> terminal** … **O BIEN** existe un evento `deriva` SIN reparar que nombra ese item»

**Cita literal, doc 11 L1737-L1741, el mecanismo A:**

> «`A · CAS DEL CANAL DE ÓRDENES` … **NO es de §2.6** … SALIDA deja las órdenes sin consumir ·
> **NO modifica el estado canónico** · **registra reconciliación pendiente** · deja de girar»

**Por qué es defecto.** El predicado tiene **exactamente dos disyuntos, y los dos son sobre el
diario de transacciones**. El agotamiento de `MAX_CAS_RETRIES` **no emite ningún evento de
diario** —el propio texto manda «NO modifica el estado canónico» y lo declara «NO es de §2.6»—,
luego tras tres fallos CAS el predicado es **FALSO**. Consecuencia mecánica: **la prueba `T22` de
(a) no es satisfacible por la arquitectura F4** y **el freno del paso 4 de `b.12` nunca dispara**.
Y `b.4` `P0` no lo salva: está acotado a «transición multiarchivo incompleta», que es
precisamente lo que este caso no es. Agrava que **L1739 escribe «registra reconciliación
pendiente» veintiséis líneas antes de titular que nadie la escribe**.

**Es PRESIÓN, no corrección de F4:** el identificador y su semántica de escritura los fija
material APROBADO (`a.9` y `T22`). **No existe ninguna `PN` que lo registre**, y las dieciséis
están enumeradas.

**Quién lo levantó.** `P3` (`P3-02`), que pidió expresamente que yo lo verificase contra el
documento 11 entero porque él sólo leyó regiones acotadas. **Lo REPRODUJE**: abrí L1728-L1745,
L1760-L1775 y las nueve apariciones del identificador en el documento, y **no encontré ninguna
sede que dé productor al caso del canal de órdenes**. `P3` no se atrevió a graduarlo; **yo lo
gradúo GRAVE**, porque rompe una prueba de conformidad de material aprobado.

---

### `P-08` · **GRAVE** · `PN-16` presiona por la grafía cuyo derivado no existe y deja fuera la que ya está construida con DOS grafías dentro del propio kernel

**Ficheros y líneas:** `b-RECORRIDO-APROBADA.md` (doce apariciones de `VER:decisión`, **todas con
tilde**) · `kernel/operativo/recorrido/01-PROCESOS.md` L497, L499, L512 (**con tilde**) ·
`capacidades/VER/*`, `circuitos/00-CIRCUITOS.md`, `pruebas/*`, `packs/wear-os/composicion.md`
(**sin tilde**) · `11-ARQUITECTURA-INTEGRADA.md` **L8489** (`PN-16`).

**Cómo lo reproduje.**

```text
$ grep -c 'VER:decisión' docs/rediseno/b-RECORRIDO-APROBADA.md  → 12   (y `VER:decision` → 0)
$ grep -rn 'VER:decisión' kernel/ | wc -l                        →  3
$ grep -rn 'VER:decision' kernel/ packs/ | wc -l                 → 14
$ grep -rn 'VER:decision' kernel/operativo/circuitos/00-CIRCUITOS.md
185:  ──► VER:decision      193: … un DIR: VER:decision lo comprueba.
```

**Por qué es defecto.** `PN-16` se acota literalmente a «**la grafía canónica de
`<CAP>:revisión`**» y a `b.16` **L836**. Pero `<CAP>:revisión` tiene **cero instancias** en el
kernel derivado, mientras `VER:decisión` **ya está construido, y con las dos grafías a la vez
dentro del mismo kernel**: 3 con tilde en `recorrido/` y 14 sin tilde en `capacidades/`,
`circuitos/`, `pruebas/` y `packs/`. **Se registró la presión por el caso hipotético y se dejó
pasar el real, que además ya es incoherente consigo mismo.** Y la grafía canónica vive en (b):
elegirla es del Owner, luego **es PRESIÓN y ninguna `PN` la cubre**.

**Quién lo levantó.** `P3` (`P3-03`). **REPRODUCIDO** con los cuatro barridos.

---

### `P-09` · **MEDIO** · el marcador del `deriva` no está clasificado en la única sede que reparte `fsync`, y tres sedes condicionan el paso 6 a que sea DURABLE

*(BAJADO de GRAVE. `P1` lo propuso GRAVE; el motivo de la rebaja va abajo y es de mi cuenta.)*

**Fichero y líneas:** **L1231-L1260** (§2.6.6) contra **L1162** (`W8`), **L1931-L1932** (§2.6.9
punto 5) y **L4240** (§3.6).

**Cita literal, L1254-L1256:**

> «`NO EXIGIDO  los derivados, el marcador de transacción, el evento `derivada` y el evento
> `conflicto`: **los cuatro** se reconstruyen desde lo canónico …»

**Cita literal, L1931-L1932:**

> «`5 EL MARCADOR  el de TRANSACCIÓN se MANTIENE hasta que el `deriva` y **su propio marcador son
> durables**. El del `deriva` se crea en el paso 5»

**Por qué es defecto.** §2.6.6 es **la** sede que reparte `fsync`. Su lista OBLIGATORIO tiene
cinco entradas y la quinta es el **EVENTO** `deriva` y su directorio, **no su marcador**. Su lista
NO EXIGIDO se cierra con «**los cuatro**», enumeración cerrada, y tampoco lo incluye. **El
marcador del `deriva` no está en ninguna de las dos listas**, mientras `W8`, el punto 5 y §3.6
condicionan a su durabilidad la retirada del marcador de transacción — es decir, el desbloqueo
del commit. Y §2.6.6 define «durable frente a caída de máquina» como `fsync` de fichero y de
directorio. **Es la recurrencia de `M-03` un nivel más abajo: la corrección dio `fsync` al evento,
creó un marcador nuevo, y al marcador nuevo no le dio ni `fsync` ni clasificación.**

**Por qué lo BAJO a MEDIO.** §2.9 **L3059** da al marcador del `deriva` una fila propia de
reconstrucción: «*el diario: los eventos `deriva` para los que `bloqueado_por_deriva(item)` sigue
siendo verdadero — **total y determinista**. Es un acelerador, no una verdad*». `P1` la citó como
atenuante y la pesó de menos: con esa fila, **no darle `fsync` es coherente**, y lo que queda es
(i) una enumeración cerrada —«los cuatro»— que deja un quinto fuera y (ii) tres sedes usando la
palabra «durable» con un sentido que §2.6.6 no concede. Es propagación y terminología, no una
garantía perdida.

**Quién lo levantó.** `P1` (`P1-04`). **REPRODUCIDO**, y rebajado por mí con la fila de §2.9.

---

### `P-10` · **MEDIO** · `KERNEL.md`: cuatro referencias cruzadas rotas, dos de ellas sobre reglas canónicas

**Fichero:** `kernel/KERNEL.md`. **HALLAZGO MÍO**, de mi propio lote.

| línea | dice | apunta realmente a | debería apuntar a |
|---|---|---|---|
| **L118** | «El primer entregable del Circuito 0 (**ver G30 y G31**) es compilar este MASTER» | `G30` = *Contención de fallos y recuperación* · `G31` = *Experimentación y feature flags* | `G22` (el gate fijo, entregable 1) y `G43` / `G47` |
| **L135** | «**G47 (documentación)** → al existir `docs/README.md`, éste manda» | `G47` = *Prompt de arranque* | `G40` — *Documentación como estado del sistema* |
| **L581** | «el grado de revisión es proporcional al riesgo (**ver G21**)» | `G21` = *Gates entre circuitos* | `G34` — *Flujo proporcional al riesgo*, que el propio documento rotula «*(regla canónica)*» |
| **L777** | «toda tarea de clase **Standard o Significant (G21/G28)**» | `G21` = gates entre circuitos · `G28` = supply chain | `G34`, única sede que define las tres velocidades |

**Por qué es defecto.** `KERNEL.md` es la constitución vendorizada que se copia idéntica en todos
los proyectos, y su regla `K0.4` existe para resolver contradicciones **remitiendo**. Cuatro de
esas remisiones llevan a la sección equivocada, y dos de ellas —L581 y L777— envían al lector a
buscar la clasificación por riesgo en la sección de gates entre circuitos. **Reproducido leyendo
las cuatro líneas y los cuatro rótulos de destino** (`sed -n '1093p;1107p;1455p;1534p;1146p'`).

---

### `P-11` · **MEDIO** · `KERNEL.md` conserva residuo de un MASTER de dos partes que este fichero ya no es, y con él una violación de su propia L6

**Fichero y líneas:** **L6**, **L133-L134**, **L150-L151**, **L198**, **L200**, **L354**,
**L984**, **L1437**. **HALLAZGO MÍO.**

**Cita literal, L6 —la regla que el propio fichero se pone:**

> «**Este fichero NO DEBE contener nada específico de un proyecto. Si lo contiene, es un defecto:
> ver K0.10.**»

**Cita literal, L984 (`G27`, reglas duras de seguridad):**

> «Los datos personales o de sensores del Owner usados en desarrollo … **Ver P44 para el detalle
> de este proyecto.**»

**Cómo lo reproduje.**

```text
$ grep -c '^### P[0-9]' kernel/KERNEL.md      → 0    (ninguna sección `P<nn>` existe)
$ grep -n 'Parte I\|Parte II\|P25\|P30\|P44' kernel/KERNEL.md
133,134  «P25 (stack orientativo) … P30 (modelo de datos) … se poda»
150,151  «Owner → este MASTER (**Parte II**)» · «Este MASTER (**Parte I**) → AGENTS.md»
198,200  «copiar el MASTER, **conservar la Parte I**, reescribir la **Parte II**»
354      «Sistema producto: lo descrito en el Project Profile (**Parte II**)»
984      «**Ver P44 para el detalle de este proyecto**»
1437     «Las restricciones específicas se descubren en la **Parte II**»
```

**Por qué es defecto.** `KERNEL.md` **no tiene Parte I ni Parte II**: se estructura en `K-1`,
`K0` y los bloques A-F. Las secciones `P25`, `P30` y `P44` **no existen en el fichero**. La regla
`K0.4` —la jerarquía de autoridad que resuelve contradicciones— tiene **dos de sus diez filas
apuntando a una parte inexistente**, y `G27`, que se autodeclara «reglas duras … **NO** delegables
al bootstrap ni negociables por ningún agente», remite «al detalle de **este proyecto**» dentro
del fichero que en su línea 6 declara que contener algo de un proyecto **es un defecto**. Es la
prueba de contaminación de `K0.10` fallando sobre el propio `K0.10`.

---

### `P-12` · **MEDIO** · `G46` y `G47` mandan leer dos ficheros distintos, y ninguno de los dos existe

**Fichero y líneas:** **L1526** (`G46` paso 5) y **L1537** (`G47`). **HALLAZGO MÍO.**

> **L1526:** «5. Indicarle que lea **`BOOTSTRAP_PROMPT.md`** e inicie el Circuito 0»
> **L1537 (el texto literal del prompt de arranque):** «Lee íntegramente **`PROJECT_MASTER.md`**.
> Es la semilla y autoridad conceptual del proyecto.»

**Por qué es defecto.** `K0.14` paso 7 remite a «el prompt de arranque (`G47`)», y `G47` manda leer
`PROJECT_MASTER.md`; `G46` manda leer `BOOTSTRAP_PROMPT.md`. **Los dos nombres designan el mismo
acto y ninguno es `KERNEL.md`**, que es el fichero que el prompt describe («la semilla y autoridad
conceptual»). Es el punto de entrada humano del sistema entero: `G46` se titula «Punto de entrada
humano». Reproducido con `ls` sobre el árbol y con la lectura de las dos secciones.

---

### `P-13` · **MEDIO** · el índice de contratos contradice a `C1` sobre el número de campos de rol, y `T151` pasa en VERDE

**Ficheros y líneas:** `kernel/operativo/contratos/00-INDICE.md` **L7** contra
`kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` **L37** y **L39**. **HALLAZGO MÍO**,
de mi propio lote.

> **`00-INDICE.md` L7:** «los siete conceptos y los **veintiocho** campos del contrato de rol»
> **`C1` L37:** «## Contrato común de rol — **veintinueve** campos»
> **`C1` L39:** «declara los **veintinueve** campos del esquema `esquemas/rol.yaml`»

Conté la tabla de `C1` una a una: **veintinueve filas**, de `id` a `prompt`. El índice está mal.

**Y esto es lo que lo hace un hallazgo y no una errata.** Ejecuté el validador que existe para
esta clase exacta:

```text
$ python3 kernel/operativo/validadores/comprobar_recuentos.py
T151  SUPERADA  Ninguna cifra del corpus contradice el recuento derivado
1 superadas · 0 fallidas
```

**Pasa en verde con la contradicción delante.** El motivo está en su propio código:

```text
$ grep -n 'INDICE' kernel/operativo/validadores/comprobar_recuentos.py
108-111: ("kernel/operativo/00-INDICE.md", …)     ← el índice PADRE
113,115: ("…/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md", …, "campos_de_rol")
```

El validador inspecciona `kernel/operativo/00-INDICE.md` y `C1`, **y no
`kernel/operativo/contratos/00-INDICE.md`**. Es un **falso verde del validador de recuentos**, y
la única garantía mecánica que el corpus tiene contra esta clase.

**Atenuante que declaro.** `D102` contrata para F6 un validador derivado que debe cazar
exactamente estas tres divergencias, y las nombra. Luego **la divergencia está registrada**; lo
que no está registrado es que `T151` la deja pasar hoy y se declara superada.

---

### `P-14` · **MEDIO** · §17 dice «`C1`–`C7` intactos» sobre un `C7` que §15.7 declara con una corrección pendiente — y la comprobé en mi propio lote

**Ficheros y líneas:** `11-ARQUITECTURA-INTEGRADA.md` **L8623** contra **L7645-L7648**, y
`kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` **L170**.

> **§17 L8623:** «\| `C1`–`C7` \| **intactos**. `C2` se amplía en F6 \|»
> **§15.7 L7648:** «`C7` gobierno Git \| **REUTILIZADO CON UNA CORRECCIÓN PENDIENTE, NOMBRADA.**
> Su `gate:convergencia-de-fuentes` dice `aplica_a: "una o más fuentes"` y `E2.6` … dice «varias
> sources». **Con el texto vigente, ningún producto de un repositorio cierra un solo item.**»

**Lo verifiqué en mi propio fichero asignado, que es la sede real:**

```text
$ grep -n 'aplica_a' kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md
170: aplica_a: "todo item cuyos paquetes escribieron en **una o más** fuentes"
```

**Sigue diciendo «una o más».** §15.7 y §9.5 también declaran `C5` y `C6` «REUTILIZADOS CON
EXCEPCIÓN NOMBRADA». §17 es la sede que F6 usará como lista de trabajo, y nombra un solo cambio
(`C2`), luego se leerá como exhaustiva. No lo es.

**Quién lo levantó.** `P2` (`P2-10`). **REPRODUCIDO**, y confirmado contra el contrato mismo,
que es mi lote y no el suyo.

---

### `P-15` · **MEDIO** · §17 dice «diez procesos de `b.16` · intactos» mientras §19 contrata que F6 edite cinco de ellos

**Fichero y líneas:** **L8625** contra **L9075-L9080** y **L9164-L9166**.

> **L8625:** «\| diez procesos de `b.16` \| **intactos**. Ningún macrocircuito crea uno nuevo \|»
> **L9164:** «`DÓNDE, EXACTAMENTE  kernel/operativo/recorrido/01-PROCESOS.md`»

**Por qué es defecto.** La columna se titula «qué le pasa». Lo que les pasa, según §19 (`D104`),
es que F6 debe instanciar **nueve pares `<CAP>:revision` repartidos en CINCO de los diez
procesos**, con su error `composicion-incompleta`. Lo intacto es **el número diez**, no los
procesos. La fila vecina sí hace esa distinción —«quince capacidades … intactos … **`+6`
extensiones de ficha**»— y ésta no.

**Quién lo levantó.** `P2` (`P2-05`). **REPRODUCIDO** leyendo las tres sedes.

---

### `P-16` · **MEDIO** · «desenlace `4b`» se cita seis veces y la sede canónica de desenlaces declara que sólo hay cuatro

**Fichero y líneas:** sede canónica **L2013-L2038**; usos en **L419**, **L1492** (`X58`),
**L2154**, **L2543**, **L2554**, **L3060**.

> **L2013:** «#### Los **CUATRO** desenlaces materiales, **y ninguno más**»
> rótulos: `1 · COMPLETADA` · `2 · CONFLICTO QUE CESA` · `3 · ABANDONADA` · `4 · TODAVÍA
> BLOQUEADA`. **No hay ningún `4b`.**

**Por qué es defecto.** `4b` existe, pero es el rótulo de una **SECUENCIA** (L2219,
`4b · ABANDONO IMPOSIBLE`), no de un desenlace. Seis sedes lo citan como «desenlace `4b`»,
incluida **`X58`, que es contrato de prueba que F6 debe construir** («la retención acotada del
desenlace `4b` termina por ACTO DE AUTORIDAD del Owner») y **la fila de reconstrucción de §2.9**
(L3060). Quien vaya a la sede de desenlaces a resolver `4b` no lo encuentra. Es el espacio de
identificadores con dos significados que `D83` declara cerrado.

**Quién lo levantó.** `P1` (`P1-09`). **REPRODUCIDO** con `sed -n '2013,2038p'` y el barrido de
`4b`.

---

### `P-17` · **MEDIO** · `G53` exige un campo del contrato `K0` que la cabecera de `K0` no declara

**Fichero y líneas:** `kernel/KERNEL.md` **L1224** contra **L70-L80**. **HALLAZGO MÍO.**

> **L1224 (`G53`):** «Todo PROFILE **DEBE** declarar sus **áreas de calidad diferencial**
> (**`premium_areas` en el contrato K0**).»

La cabecera obligatoria de `K0` (L71-L80) declara nueve campos: `kernel`, `packs`, `project`,
`owner_success`, `target_env`, `validation`, `risk_profile`, `compliance`, `timebox_c0`.
**`premium_areas` no está.** El cuerpo lo recoge como punto «6.bis», pero `G53` lo sitúa
expresamente en la cabecera yaml, y `K0` abre diciendo «Un PROFILE es válido si, y sólo si,
responde a **todos** los puntos de este contrato».

```text
$ grep -n 'premium_areas' kernel/KERNEL.md kernel/operativo/contratos/*.md
kernel/KERNEL.md:1224   ← única aparición en todo el corpus normativo
```

**Por qué importa.** `G53` hace depender de ese campo la inversión de `G24`, el enrutamiento de
modelo y la prohibición de Quick Change. Un validador de PROFILE derivado de la cabecera de `K0`
no lo exigiría.

---

### `P-18` · **MEDIO** · contradicción interna en material APROBADO: `T27` dice SIETE casos frontera y `T63` dice ONCE, sobre la misma tabla

**Fichero y líneas:** `b-RECORRIDO-APROBADA.md` **L1107-L1108** y **L1232-L1233**; tabla en
**L255-L268**.

> `T27` (marcada **[corregida]**): «Se prueban los **siete** casos de `b.4`.»
> `T63` (marcada **[corregida]**): «los **once** casos frontera de `b.4`»

```text
$ sed -n '255,268p' docs/rediseno/b-RECORRIDO-APROBADA.md | grep -c '^| '   → 11
$ grep -rn 'T27' --include='*.md' .   →  sólo b-RECORRIDO-APROBADA.md:1107
```

`T63` acierta; `T27` dice siete y **está marcada como ya revisada**. Dos pruebas de conformidad
del mismo documento aprobado prescriben cardinalidades incompatibles del mismo conjunto, y
**`T27` no aparece en ninguna otra parte del árbol**: nadie la ha instanciado y nadie ha visto la
discrepancia. **Es PRESIÓN: `b.17` es material APROBADO.** Ninguna `PN` la cubre.

**Quién lo levantó.** `P3` (`P3-07`). **REPRODUCIDO.**

---

### `P-19` · **MEDIO** · `E2.4` —material APROBADO— cita una fila de `a.11` que no contiene lo que dice, y `G29` no aparece en (a) ni una vez

**Ficheros y líneas:** `a-ENMIENDA-E2-MULTIREPO.md` **L152** contra `a-CAPACIDADES-APROBADA.md`
**L1016-L1024**.

> **`E2.4` L152:** «\| `a.11`, fila **Ajustadas** \| `G29` figuraba entre las reglas que
> **SOBREVIVEN** intactas, en el mapa del rediseño \| …»

**Cómo lo reproduje.** Leí las cinco filas de `a.11`: *Derogadas · Sustituidas · **Ajustadas** ·
PENDIENTES, no derogadas · Previstas*. **No hay fila «SOBREVIVEN».** Y la fila `Ajustadas` nombra
`G13`, `G34`, `G52`, `G17`, `G08` y `G32` — **no `G29`**.

```text
$ grep -c 'G29' docs/rediseno/a-CAPACIDADES-APROBADA.md   → 0
```

**Por qué importa para este gate.** `D97` invoca «`E2.4` demuestra que **lo no nombrado
sobrevive**». La conclusión **se sostiene, y de hecho se sostiene mejor**: hizo falta una enmienda
formal del Owner para revisar una regla que `a.11` **nunca nombró**. Lo que no se sostiene es la
mitad de la fundamentación.

**Quién lo levantó.** `P3` (`P3-08`). **REPRODUCIDO.**

---

### `P-20` · **MEDIO** · las tres celdas «completas» de §5.6 escriben `responsables` con el reparto POR DEFECTO y sin `motivo`, contra el contrato que existen para demostrar

**Fichero y líneas:** **L5093**, **L5115**, **L5134**, **L5178**, contra **L3713** (§3.5),
**L5293** (§5.7) y **L6850** (§9.2).

> **L3713, el contrato:** «`responsables  la **DESVIACIÓN** respecto al reparto por defecto,
> cuando la hay, **con su motivo**.`»
> **L5093:** «`responsables  [DIS]     lider: DIS`» · **L5134:** «`[ARQ, SIS]  lider: ARQ`» ·
> **L5178:** «`[PLT, VER]  lider: PLT`»

**Por qué es defecto.** Los tres valores **son exactamente el reparto por defecto** y ninguno
lleva `motivo`; por el contrato, **ninguno debería llevar el campo**. Agrava que §5.6 es la
sección que existe para demostrar que el contrato funciona «*sin campos vacíos de conveniencia*»
y que encarga a **`X52`** validar las tres celdas contra el esquema: **con el esquema tal como
§3.5 lo define, `X52` tendría que rechazarlas.**

**Quién lo levantó.** `P2` (`P2-07`). **REPRODUCIDO** contra las tres sedes de la regla.

---

### `P-21` · **MEDIO** · la nota `m-1` de §8.2 dice «Hoy son TRECE» donde son CATORCE, y omite `PN-16`

*(BAJADO de GRAVE, que es lo que propuso `P2`.)*

**Fichero y líneas:** **L6363-L6367**.

> «`O15` se escribió cuando el recuento derivado de presiones normativas vigentes era **ocho**.
> **Hoy son TRECE** (§16), porque `PN-11`, `PN-12`, `PN-13`, `PN-14` y `PN-15` son posteriores a
> ella … **y la vigente es siempre la que §16 deriva**.»

Son **catorce** (mi barrido de `P-04`), y la enumeración omite `PN-16`. El adverbio «Hoy» y el
remate hacen de ella una afirmación de vigencia.

**Por qué la BAJO.** La nota se autodeclara «**que NO toca la resolución**» y **defiere
expresamente a §16 como la sede que manda**. El lector que siga la remisión obtiene la cifra
correcta. Es una cifra caduca en una frase que se desautoriza a sí misma, no una norma falsa.

**Quién lo levantó.** `P2` (`P2-01`). **REPRODUCIDO**, y rebajado por mí.

---

### `P-22` · **MEDIO** · `C-L.5` lleva estado compuesto dentro de una misma sección: la cabecera dice ABIERTA y el cierre dice CERTIFICADA

*(BAJADO de GRAVE, que es lo que propuso `P2`.)*

**Fichero y líneas:** **L9390** (cabecera de sección), **L9400** (cuerpo), **L9483** (cierre).

> **L9390:** «## `C-L.5` · La condición de COBERTURA del próximo gate — **abierta, y no la cierra
> esta tanda**»
> **L9483:** «**Estado: CERTIFICADA por el GATE INDEPENDIENTE DE CIERRE CON MANIFIESTOS
> VERIFICABLES** —documento 21—, y es la primera vez.»

**Por qué la BAJO.** Leí el cierre entero (L9483-L9494) y **reconcilia expresamente las dos
lecturas**: «*Que esta condición esté certificada no cierra `F4c` ni autoriza `F5`*» y «*el
requisito de arriba sigue vigente para todo gate posterior*». La cabecera es verdadera **sobre la
tanda** —la tanda no la cerró; la certificó un gate posterior—. Lo que queda es que el **título de
sección**, que es lo que se proyecta al índice, sigue llevando el adjetivo «abierta» después de
que la condición fuera certificada. Es una proyección desactualizada, no un estado contradictorio.

**Quién lo levantó.** `P2` (`P2-03`). **REPRODUCIDO**, y rebajado por mí.

---

### `P-23` · **MENOR** · bloque `text` huérfano: la cola del procedimiento de abandono quedó a 83 líneas de su cabeza

**Fichero y líneas:** **L1972-L1975**.

> ```text
>                   · permitir el COMMIT DEL INCIDENTE
>                   · y **sólo después**, eliminar `.ads/run/quarantine/<TX>/` si se creó
> ```

Dos viñetas sin frase que las introduzca, sin rótulo y sin sujeto, con la sangría y la forma de
las del paso E, que termina en L1889. Entre la cabeza y la cola se insertaron la nota de `M-02`,
la tabla de alternativas y los ocho puntos de `D105`. **Consecuencia material:** quien lea el paso
E como lista cerrada de seis pasos no implementa el orden «commit del incidente ANTES de borrar la
cuarentena», que §2.3 y §2.6.9 declaran crítico. **Levantado por `P1` (`P1-08`), REPRODUCIDO con
`sed -n '1966,1980p'`.**

---

### `P-24` · **MENOR** · dos autorreferencias a número de línea absoluto, las dos rotas

**Fichero y líneas:** **L2326** («la objeción de **L2103**») y **L2382** («**L2226** la hace
condición de validación»).

La cita que L2326 atribuye a L2103 —«crea una tercera ubicación»— está hoy en **L2449**, 346
líneas más abajo; L2103 contiene otra cosa. L2226 contiene hoy el acto (i) de la secuencia `4b`.
El documento tiene ~55 anclas de esta forma; **las dos autorreferencias del corpus están rotas, y
las demás apuntan a otros ficheros y no las he verificado.** Levantado por `P1` (`P1-10`),
**REPRODUCIDO** con `sed` sobre las cuatro líneas.

---

### `P-25` · **MENOR** · `X-F` conserva «una reconciliación abierta» como mecanismo vigente después de que `D64` retirara la ruta

**Fichero y líneas:** **L3262** y **L3360** (fila `X-F`), contra **L778-L783**, **L1686-L1689** y
**L3792** («*`reconciliacion-preparada` y `reconciliada` NO existen: `D64` las retira*»).

`X-F` es contrato de prueba que F6 debe construir, y enumera como disparador un estado que el
autómata vigente no puede alcanzar. Ni L3262 ni L3360 llevan marca de histórico, y `X47` exige que
toda mención de lo retirado esté marcada. Levantado por `P1` (`P1-11`), **REPRODUCIDO**.

---

### `P-26` · **MENOR** · §15.4 publica un rango que no termina en su última fila, y `O16` no tiene fila

**Fichero y líneas:** **L7584** (cabecera) y **L7588-L7596** (tabla).

```text
$ sed -n '7584p' …   → ## 15.4 · `O7`–`O14` y `P-01`–`P-08`
$ sed -n '7588,7597p' … | grep -c '^| `O'   → 9      (llegan a `O15`)
$ grep -n 'O16' …    → 7851 · 8182 · 8188 · 8191     (NINGUNA en §15.4)
```

§15.4 es la tabla de trazabilidad «dónde queda cada resolución del Owner», y `PN-11` L8191 dice
que hay **dieciséis** resoluciones. Traza nueve y no declara dónde están las demás. Levantado por
`P2` (`P2-04`), **REPRODUCIDO**.

---

### `P-27` · **MENOR, y con su atribución dicha** · `comprobar_referencias.py` FALLA sobre el árbol de hoy

**HALLAZGO MÍO.** Lo ejecuté con el intérprete del encargo:

```text
$ python3 kernel/operativo/validadores/comprobar_referencias.py ; echo $?
· …/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md: no lo alcanza ningún enlace … Existe para nadie
· …/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md: no lo alcanza ningún enlace … Existe para nadie
0 superadas · 1 fallidas
1
```

**Hay un validador en ROJO en el árbol de HEAD.** Y digo su atribución, porque sin ella el dato
engaña: **los dos huérfanos son los dos manifiestos de ESTE gate**, añadidos en commits
posteriores al candidato `4d231ee`. **No es un defecto de la tanda juzgada: es el aparato del gate
rompiendo un validador del corpus que juzga.** Lo registro porque el árbol de HEAD es el que
está, y porque un gate que rompe una comprobación del sistema que certifica debería decirlo él
mismo. Los otros tres validadores que ejecuté —`comprobar_recuentos`, `comprobar_contratos`
(18/18) y `comprobar_integridad`— pasan.

---

### Recuento derivado de las filas, no escrito aparte

| severidad | nº | ids |
|---|---|---|
| **BLOQUEANTE** | **0** | — |
| **GRAVE** | **8** | `P-01` · `P-02` · `P-03` · `P-04` · `P-05` · `P-06` · `P-07` · `P-08` |
| **MEDIO** | **14** | `P-09` … `P-22` |
| **MENOR** | **5** | `P-23` · `P-24` · `P-25` · `P-26` · `P-27` |
| | **27** | |

**Cuántos son nuevos.** De los veintisiete, **veinticuatro no están registrados en ninguno de los
veinticuatro hallazgos del documento 21**. Los tres que sí tienen antecedente son `P-01`
(descendiente de `R-04`, pero **agravado por la corrección**), `P-05` (mitad no aplicada de
`P-06`) y `P-08` (residuo del alcance de `P-07`→`PN-16`).

**Cuántos los introdujo o los dejó pasar esta tanda.** `P-01` lo **introdujo** esta tanda al
aplicar `R-04`. `P-04`, `P-05`, `P-14`, `P-15` y `P-21` son **mitades no propagadas** de
correcciones que esta tanda sí aplicó en otra sede. **Seis de veintisiete**, y es el mismo patrón
que el documento 21 pone como su cuarta razón de veredicto.

---

## 4 · HALLAZGOS QUE RECHAZO DE MIS PROPIOS RELEVOS

Seis rechazos y dos rebajas ya dichas. **Esto vale tanto como lo que acepto, y lo escribo contra
el interés de mi propia cadena.**

---

**`X-1` · RECHAZO `P1-06` — «Las siete secuencias completas» enumera OCHO.**
`P1` cuenta ocho rótulos porque incluye `4b · ABANDONO IMPOSIBLE` (L2219). **El propio rótulo es
la refutación:** el autor lo numeró `4b` y no `5`, y las tres secuencias siguientes conservan
`5`, `6` y `7`. Un sufijo alfabético sobre el mismo número **es la declaración explícita de que es
una variante de la cuarta**, no una octava. El documento usa la misma convención en `W12a`/`W12b`
sin que nadie diga que las ventanas son diecinueve. **No hay defecto de recuento. No entra.**

**`X-2` · RECHAZO la consecuencia material de `P1-05`, y conservo sólo su taxonomía.**
`P1` concluye que la caída en `[paso 4, paso 5)` deja «*el control repo sin volver a
commitear*», porque el paso 0 de §2.6.4 responde «nada que hacer» y el marcador de transacción
sigue puesto. **Abrí la sede que `P1` no pesó:** §2.9 **L3058** da al marcador de transacción una
fila de reconstrucción —«*el diario: las transacciones que satisfacen `abierta(tx)`* … **total**.
Es un **acelerador, no una verdad**»— y en ese tramo `abierta(tx)` es **falsa**, porque el
`abandonada` es durable. Con el diario como autoridad, el marcador obsoleto no es una verdad que
bloquee. **La consecuencia material NO está establecida y no la sostengo.** Lo que sobrevive, y lo
sostengo entero, es la **contradicción taxonómica** entre `W17` y el punto 7 — que es `P-01`, y no
necesita el bloqueo para ser GRAVE. *(Declaro la contrapartida honesta: tampoco está establecido lo
contrario, porque §2.6.10 L2490 hace que la regla de commit consulte el **fichero** marcador —«un
marcador abierto lo impide»— y ninguna sede prescribe **podar** un marcador obsoleto. Que no se
pueda decidir es parte del defecto, y por eso `P-01` es GRAVE y no MEDIO.)*

**`X-3` · RECHAZO `P1-13` — «un barrido sobre `docs/` devuelve UNA sola aparición: hoy devuelve
cuatro».**
Abrí L1545-L1546: la frase está **dentro de un bloque de cita `> «…»` que transcribe el dictamen
de un gate anterior**. Es cita literal de un documento histórico, no afirmación vigente del
documento 11, y el corpus tiene doctrina expresa (`D83`, `D94`) de que las citas históricas no se
reescriben. Además la parte sustantiva —que en §2.6.4 la frase aparece una sola vez— **sigue
siendo cierta** (L940, única). **No entra.**

**`X-4` · RECHAZO `P1-15` — la regla 4 atribuida a `X55`.**
El propio `P1` escribe: «*No puedo reproducirlo como contradicción textual literal … es una
atribución de evidencia que no cubre lo atribuido*». **Un hallazgo que su autor declara no
reproducido no entra en mi dictamen.** Es una lectura defendible de la cobertura de una fila
adversarial, y `X55` sí observa el orden en su desenlace. **No entra.**

**`X-5` · RECHAZO `P1-16` — «Las NUEVE REMITEN aquí. Ninguna lo redeclara».**
`P1` reconoce (a) que el censo de nueve sedes **es correcto**, comprobado una a una, y (b) que las
dos glosas que encuentra —§2.5 L549 y §2.9 L3058— son **consistentes con la formulación vigente**.
Una glosa consistente que remite no es una redeclaración en el sentido que `I5` prohíbe: lo que
`D89` cerró era una sede que redeclaraba con la formulación **retirada**, y eso no ocurre. La
décima sede que menciona es la fila histórica de `D71` en §15.8. **No hay defecto vivo. No entra.**

**`X-6` · RECHAZO `P1-17` — §2.6.5 «se deriva de las filas, no se escribe» mientras escribe la
cifra.**
El propio `P1` dice: «*No hay nada roto hoy*». La cifra es correcta —dieciocho filas, dieciocho
identificadores, verificado por su propia refutación `R1` y por `X54`—, y la frase describe el
**método**, no se contradice: derivar y publicar el resultado derivado no es escribirlo de
memoria. **Registrar una plantilla de riesgo no es un hallazgo. No entra.**

**`X-7` · REBAJO `P1-04` de GRAVE a MEDIO** — es `P-09`, con el motivo escrito allí: §2.9 L3059
concede al marcador del `deriva` reconstrucción total y determinista, y `P1` la citó como atenuante
sin descontarla de la severidad.

**`X-8` · REBAJO `P2-01` de GRAVE a MEDIO** (`P-21`) y **`P2-03` de GRAVE a MEDIO** (`P-22`), con
los motivos escritos en sus fichas.

**`X-9` · NO ADJUDICO cuatro hallazgos menores de `P2` y `P3` que no reverifiqué.**
`P2-08` (rótulo «LAS DIEZ» en `PN-13`), `P2-09` (rótulo de la tercera celda de §5.6), `P2-11`
(`X52` insatisfacible para tres de cuatro niveles), `P2-12` (`D98` invoca `a.6` L502-503),
`P2-13` (normalización del paso 4), `P3-04` (`D92` cita `a.6` L504-505), `P3-05` («las ocho
presiones» en `O15`), `P3-06` (`O16` precede a `O15`) y `P3-09` (`b.9` numera 1·2·5·3·4).
**Comprobé cuatro de los nueve** —`P3-04` (L293 dice efectivamente «`a.6` L504–505», y las líneas
correctas son 502-503), `P3-05` (L609 dice «las **ocho** presiones normativas vigentes», y son
catorce), `P2-04` y `P1-12` (L3806 remite a «§2.5» cuando la condición de arranque 5 está en
§2.6.0, L605)— **y los cuatro son ciertos.** Los otros cinco los declaro **verosímiles pero NO
reverificados por mí**, y **no los cuento** entre mis veintisiete. Prefiero un recuento corto y
entero a uno largo y prestado.

---

## 5 · LOS 24 HALLAZGOS DEL DOCUMENTO 21, EN EL FOCO DE `P`

**Regla que me impongo.** Los que caen en el foco de `Q` —derivación, batería, kernel operativo,
checkpoint— **NO los adjudico**, y no los presumo ni cerrados ni abiertos. Lo digo en la columna,
sin rodeos, y en cada caso digo **por qué** la fuente no es mía.

| id | qué exigía | qué dice la tanda que hizo | qué encuentro yo en el árbol | resultado |
|---|---|---|---|---|
| **`P-01`≡`Q-13`** MEDIO | `X54` decía «las **diecisiete** ventanas»; son **dieciocho** y `W17` quedaba fuera del único escenario que las barre | reanclar `X54` a DIECIOCHO y nombrar `W17` expresamente; `G-26` deriva las filas `W` | **L1488:** «*matar la máquina en cada una de las **DIECIOCHO** ventanas … —`W1`–`W11`, `W12a`, `W12b`, `W13`–`W16` y **`W17`**— … **`W17`** incluida expresamente (`P-01`≡`Q-13`)*». Conté las filas: dieciocho. Crucé con §2.6.5 L1137: dieciocho | **SUPERADO** |
| **`P-02`≡`Q-06`** MEDIO | la capa B (L4360) decía «TODO `abandonada` **DECLARA SU** `deriva`», verbo que `D105` invirtió | corregir el verbo | El verbo **ya no está en la lista de la capa B**. `grep -n 'DECLARA SU'` sobre el documento devuelve **L4391** —que es la anotación de corrección, texto histórico explícito— y L7210, ajeno. Verifiqué además las seis apariciones de `deriva_emitida`: **las seis son prohibiciones** | **SUPERADO** |
| **`P-03`** MENOR *(regraduado por `R`, tesis RECHAZADA)* | residuo: retirar la justificación de idempotencia por contenido que §2.8 retiró | — | Adjudicado como `R-01`. Ver fila siguiente | **ver `R-01`** |
| **`P-04`** MEDIO | el CHECKPOINT cuenta nueve ventanas `RC-1`–`RC-9` retiradas y omite las ocho `X-A`–`X-H` | reanclar el inventario | **FUERA DE MI LOTE.** La sede es `docs/evolucion/CHECKPOINT-ADS-NEXT.md`, fila 10 del manifiesto, asignada a **`Q`+`R`** (relevo `Q1`), no a `P`. **No lo adjudico y no lo presumo** | **FUERA DE MI LOTE** |
| **`P-05`≡`Q-08`** **GRAVE** | «Siguiente acción exacta» del CHECKPOINT: cinco afirmaciones falsas, sin marca de histórica, en la sede que se autodesigna punto de entrada | reanclar o marcar histórica la sección | **FUERA DE MI LOTE.** Misma sede, mismo motivo. **No lo adjudico.** *(Era el único GRAVE del gate anterior, y quien lo adjudique debe saber que `P` no puede.)* | **FUERA DE MI LOTE** |
| **`P-06`** MEDIO | el bloque de evidencia de `PN-15` declaraba «cero apariciones de `G20`/`G21`/`G23` en el documento 11», donde las hay | acotar el barrido a (a), (b) y `E2` —el material que puede DEROGAR— y contrastarlo con `G-13` | **CORREGIDO EN UNA SEDE Y NO EN LA OTRA.** El documento 11 **L8400** dice hoy «*Esta sede decía «cero apariciones en el documento 11», y **era falsa***», y el bloque `TEXTO VIGENTE` de `PN-15` cita `KERNEL.md`:687/690/694-712 y `START_HERE.md`:141-147, que verifiqué **una a una contra mi propio lote y las cuatro casan**. **Pero `DECISIONES-Y-CONTRADICCIONES.md` L346, la justificación de `D97`, sigue diciendo literalmente «`G20`, `G21` y `G23` tienen **cero** apariciones en el documento 11»**, y hoy hay 12·10·13. Es mi `P-05` | **NO SUPERADO** *(mitad aplicada)* |
| **`P-07`** MENOR | `E5-3` merecía presión, porque una de sus dos ramas enmienda material APROBADO, y el bloque `E5` la excluía con un argumento válido sólo para `E5-1` y `E5-2` | crear `PN-16` | **L8489:** `## PN-16 · NUEVA · la grafía canónica de <CAP>:revisión vive en material APROBADO`, «*Registrada por `P-07` del GATE INDEPENDIENTE DE CIERRE CON MANIFIESTOS*», y **no elige la grafía**: registra que hay que elegir y que la elección es del Owner. Es exactamente lo que se pedía | **SUPERADO** *(y ver `P-08` de mi §3: la corrección se detuvo en la instancia nombrada y dejó fuera `VER:decisión`, que ya está construida con dos grafías dentro del kernel. Eso es hallazgo nuevo, no incumplimiento de `P-07`)* |
| **`P-08`** MENOR | `D106` no fija de dónde se deriva «fuentes obligatorias» | publicar la REGLA y el COMANDO auditables | **NO LO ADJUDICO POR CONFLICTO DE MATERIA.** El remedio es `derivar-universo-obligatorio.py` y el manifiesto de **este** gate, que son el aparato bajo el que yo trabajo. Un revisor no certifica el instrumento que lo reparte. Sí dejo el dato: el `ADDENDUM 1` demuestra que la regla 1 del propio manifiesto **no se aplicó a 21 de 33 fuentes**, luego el remedio de `P-08` no estaba consolidado al emitirse | **FUERA DE MI LOTE** *(por conflicto de materia, declarado)* |
| **`Q-01`** MEDIO | `G-11b` no falla cerrado sin Git; faltan cinco caracteres | `_base_raw is not None and` | **FUERA DE MI LOTE.** Sede: `comprobar-correccion-gate-de-cierre.py`, fila 12 del manifiesto, asignada a **`Q`** (relevo `Q2`) | **FUERA DE MI LOTE** |
| **`Q-02`** MEDIO | el ancla de posición no normaliza, contra el pilar (iv) de `D104` | envolver el ancla en `_base()` | **FUERA DE MI LOTE** (misma sede) | **FUERA DE MI LOTE** |
| **`Q-03`** MENOR | — | — | **FUERA DE MI LOTE** (batería / kernel operativo) | **FUERA DE MI LOTE** |
| **`Q-04`** MEDIO | catálogo y contratos duplicados y adiciones no rastreadas: comparar contra el árbol y no sólo contra `git diff` | — | **FUERA DE MI LOTE** (batería) | **FUERA DE MI LOTE** |
| **`Q-05`** MEDIO | el troceado real es un `re.findall` sobre segmento, no un parseo por bloque: el pilar (ii) de `D104` es falso | trocear por bloque | **FUERA DE MI LOTE** (batería) | **FUERA DE MI LOTE** |
| **`Q-06`** | ≡ `P-02` | | | **SUPERADO** *(arriba)* |
| **`Q-07`** MEDIO | §16 decía «`PN-6` a `PN-14`» = DOCE cuando ya existía `PN-15`, y omitía la presión que va al Owner | reanclar el rango | **L7920:** «*Las demás vigentes —**`PN-6` a `PN-16`**— son posteriores*», y **L7923** registra «*Corregido otra vez por `Q-07`: decía «`PN-6` a `PN-14`» cuando ya existía `PN-15`*». Verifiqué el censo: 16 cabeceras − `PN-4` RETIRADA − `PN-5` FUSIONADA = **14 vigentes**, y el rango termina en la última vigente | **SUPERADO en §16** — **pero la misma cifra quedó sin propagar en §0 (`P-04`) y en §8.2 `m-1` (`P-21`)**, que son dos sedes del mismo fichero |
| **`Q-09`** MENOR | conjunto vigilado derivado | — | **FUERA DE MI LOTE** (batería). *Dato que sí puedo aportar de mi lectura: `grep -rn 'participa dos veces' kernel/operativo/capacidades/` devuelve exactamente `DOM` y `SEG`* | **FUERA DE MI LOTE** |
| **`Q-10`** · **`Q-11`** · **`Q-12`** MENORES | — | — | **FUERA DE MI LOTE** (batería / kernel operativo / dictámenes previos) | **FUERA DE MI LOTE** |
| **`Q-13`** | ≡ `P-01` | | | **SUPERADO** *(arriba)* |
| **`Q-14`** MEDIO | `C-L.3` descrita con la regla de `D103` que `M-01` refutó, y `D104` no aparece en ninguna de sus seis sedes | marcar el bloque como histórico y nombrar `D104` | **NO PUEDO ADJUDICARLO, y ES UN DEFECTO DEL REPARTO.** El encargo pone `C-L.3` en el foco de `P`, pero **su sede no está en mi lote**: `grep -rn 'C-L\.3'` sobre el corpus da **10 golpes en `CHECKPOINT-ADS-NEXT.md` y 1 en `docs/evolucion/00-INDICE.md`**, y las dos fuentes están asignadas a **`Q`+`R`**. Se me pidió un foco sin darme la fuente | **FUERA DE MI LOTE** *(y lo denuncio)* |
| **`Q-15`** MENOR | — | — | **FUERA DE MI LOTE** | **FUERA DE MI LOTE** |
| **`R-01`** MENOR | residuo de `P-03`: sobra la justificación de idempotencia por contenido que §2.8 retiró | retirar la frase | **SUPERADO.** `W17` (L1172) dice hoy «*ahí vive la idempotencia — **no en la igualdad del `id`, que §2.8 retiró como prueba** (`R-01`)*», y el paso 0 de §2.6.4 (L968-L975) lo repite nombrando `R-01` y remitiendo a la guarda por `abandonada_id`. La justificación por contenido **ya no sostiene nada** | **SUPERADO** |
| **`R-02`** MEDIO | `M-06` reproducido en la sede de entrada del CHECKPOINT: L2023 enumera TRES ficheros donde L1911 deriva SEIS | — | **FUERA DE MI LOTE** (CHECKPOINT) | **FUERA DE MI LOTE** |
| **`R-03`** MEDIO | §2.6.9 L1940-1941 invoca la capa B por su nombre para una regla que la capa B no escribe; decidir cuál es la sede y que la otra remita | — | **SUPERADO.** Leí las dos sedes. La capa B (L4355-L4362) declara hoy «**EL PREDICADO `abierta(tx)` SE EVALÚA AQUÍ, Y NO SE REDECLARA** … `D71` designó esta capa como evaluadora; `D89` retira las dos reglas que la contradecían», y L4406 escribe la regla de unicidad con su nombre. **La sede está decidida y la otra remite** | **SUPERADO** |
| **`R-04`** MENOR | la sub-ventana del marcador que `W17` nombraba quedaba fuera de su propia condición de detección; «*lo que sobra es la frase que se lo atribuye a `W17`*» | recortar el alcance de `W17` para que no nombre ese tramo | **NO SUPERADO, Y AGRAVADO.** La tanda quitó de `W17` «*—o entre el `deriva` y su marcador—*» y escribió en su lugar «*y **sólo** ese tramo … la cubre `W8` … **y así lo reparte el punto 7 de §2.6.9** (`R-04`)*». **El punto 7 no lo reparte así, y no se tocó:** `git show 7764cca` y el árbol de hoy dan el mismo texto, «*caída entre 1 y 5 → `W17` · caída entre 5 y 6 → `W8`*». El tramo `[4,5)` cae en «entre 1 y 5». **La corrección eliminó el tramo del alcance de `W17` apoyándose en una afirmación falsa sobre la sede que lo reparte** —la misma que el adjudicador `R` escribió al desestimar la refutación de `P`—. Es mi `P-01`, y lo gradúo **GRAVE** | **NO SUPERADO** |

### Resumen de la tabla, sólo sobre lo que `P` puede adjudicar

```text
EN EL FOCO DE `P` Y ADJUDICABLES POR MÍ      7   P-01≡Q-13 · P-02≡Q-06 · P-06 · P-07 ·
                                                 Q-07 · R-01 · R-03 · R-04
  SUPERADOS                                  5   P-01≡Q-13 · P-02≡Q-06 · P-07 · R-01 · R-03
  SUPERADOS EN SU SEDE Y NO PROPAGADOS       1   Q-07   (§16 sí; §0 y §8.2 no)
  NO SUPERADOS                               2   P-06 (mitad aplicada) · R-04 (AGRAVADO)

FUERA DE MI LOTE, EXPRESAMENTE NO ADJUDICADOS  16   P-04 · P-05≡Q-08 · P-08 · Q-01 · Q-02 ·
                                                    Q-03 · Q-04 · Q-05 · Q-09 · Q-10 · Q-11 ·
                                                    Q-12 · Q-14 · Q-15 · R-02 · (P-03→R-01)
```

**Ninguno de los veinticuatro se declara SUPERADO por el propio corpus, y estoy de acuerdo con esa
abstención**: quien corrige no certifica.

---

## 6 · DICTAMEN EXPRESO SOBRE `D97` Y `G20`/`G21`/`G23`

**Mi decisión, en una frase: la RESOLUCIÓN de `D97` es CORRECTA y debe conservarse; su
JUSTIFICACIÓN, tal como está escrita hoy en `DECISIONES-Y-CONTRADICCIONES.md` L346, es una
CONTRADICCIÓN VIGENTE y NO un registro histórico suficientemente identificado.**

### La evidencia, con su línea

**La afirmación**, `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` **L346**, cuarta columna:

> «`G20`, `G21` y `G23` tienen **cero** apariciones en el documento 11, en (a), en (b) y en `E2`;
> `G22` tiene UNA, como cita de apoyo.»

**El árbol de hoy, recontado por mí:**

```text
                doc 11   (a)   (b)   E2
G20               12       0     0     0
G21               10       0     0     0
G22               16       1     0     0     ← la de (a) es a-CAPACIDADES:180, ficha de INV
G23               13       0     0     0
```

**El árbol anterior al commit que escribió `D97`:**

```text
$ git log --oneline -S'G20' -- …/11-ARQUITECTURA-INTEGRADA.md | tail -1
d868bcb  fix(f4c): aplicar la tanda de correccion del gate definitivo — D96–D102, PN-15, …
$ for g in G20 G21 G22 G23; do git show d868bcb^:…/11-ARQUITECTURA-INTEGRADA.md | grep -c "$g"; done
0  0  0  0
```

**`D97` falsificó su propia justificación en el mismo commit en que la escribió.**

### Las cuatro razones de la decisión

**1 · No dice de qué revisión habla.** Nombra los materiales pero no nombra commit, fecha ni «en
el momento de escribirse». El verbo es *tienen*, presente. Un lector que ejecute el barrido que la
frase le invita a ejecutar obtiene lo contrario. **Un registro histórico suficientemente
identificado dice cuándo fue verdad.**

**2 · La cláusula de inmutabilidad del registro NO la cubre.** Busqué la cobertura y no está. El
único pasaje que declara históricas las columnas es **L303-L307**, y está **acotado por su propio
texto** a la nomenclatura `N<n>`: «*`D32`, `D67`, `D76` y `D82` conservan `N<n>` en su texto, y es
deliberado*». No hay ninguna cláusula general que convierta un recuento verificable por `grep` en
una instantánea. **Y la doctrina del corpus va en dirección contraria:** `D94` retiró la cifra
«CATORCE» de `D68`/`D77` **creando una decisión nueva que la deriva**, sin reescribir las
anteriores; `D102` contrata la retirada de todos los censos escritos a mano.

**3 · La misma frase SÍ se corrigió en el documento 11, y no aquí.** Esto es lo que convierte el
caso en un defecto de esta tanda y no en una herencia. `P-06` del gate anterior atacó exactamente
esta afirmación. La tanda la corrigió en §16: **L8400** dice hoy «*Esta sede decía «cero
apariciones en el documento 11», y era falsa*». **En el registro no tocó nada.** El corpus tiene
**dos remedios probados** para hacerlo sin reescribir el registro —una decisión nueva que derive el
recuento (`D94`) y un **ADDENDUM** que no reescribe el texto resolutivo (`D106`(iii) sobre `O16`)—
y **no aplicó ninguno de los dos**. No es que no se pudiera: es que se hizo donde era cómodo.

**4 · Y el propio expediente ya juzgó esta forma.** `D106`(i) diagnostica, con estas palabras, que
«*la fila de §17 la escribió `D97` en el mismo commit que la presión, con lo que la prueba pasaba
en verde el día que nacía*» — y **corrigió la PRUEBA y no el recuento del cuerpo**. Media
corrección, dos tandas seguidas, sobre la misma decisión.

### Qué NO es, y consta expresamente

**La resolución de `D97` es CORRECTA, y la verifiqué contra mi propio lote, que es la sede real de
las cuatro reglas.** Leí `kernel/KERNEL.md` íntegro:

- **Las cuatro existen y están vigentes**: `G20` L640, `G21` L682, `G22` L692, `G23` L748, en un
  fichero que declara «**Versión del kernel: 1.5.0**» (L4).
- **`G21` L690 dice literalmente**: «*El gate de salida del Circuito 0 lo fija este documento y
  **NO es negociable por el sistema** (G22), porque un sistema no puede definir sin conflicto de
  interés los criterios que aprueban su propia existencia*». **F4 decidiendo por su cuenta qué
  sobrevive sería exactamente el conflicto de interés que esa regla nombra.**
- **`G22` L694-L712** fija el timebox —«3 sesiones de trabajo del Owner o 2 semanas naturales»—,
  **diez entregables numerados** y **cuatro prohibiciones**. `§8.1` define un gate distinto sin
  ninguna de las tres cosas.
- **`a.11` no las nombra**: leí sus cinco filas —*Derogadas · Sustituidas · Ajustadas · PENDIENTES
  no derogadas · Previstas*— y ninguna menciona `G20`, `G21`, `G22` ni `G23`.
- **Que lo no nombrado sobrevive lo demuestra `E2.4`**, y lo demuestra **mejor de lo que `D97`
  cree**: hizo falta una enmienda aprobada del Owner para revisar `G29`, una regla que `a.11`
  **nunca nombró** (`grep -c 'G29'` sobre (a) → **0**). *(Con la salvedad de mi `P-19`: `E2.4`
  cita mal la fila.)*
- **§17 recibió la fila que `D97` promete**, y la leí: L8632 declara las cuatro «**PRESIONADAS y
  pendientes de F5. NO derogadas por F4, y NO sustituidas por §8**», con la reserva correlativa en
  la fila de `START_HERE.md`. **Esa parte de `D97` está bien ejecutada.**

### Conclusión, partida en dos

```text
LA RESOLUCIÓN de `D97` (PN-15)      CORRECTA. Registrar la presión y no decidirla era lo que
                                    procedía, y `G21` lo exige. SE CONSERVA.

LA JUSTIFICACIÓN de `D97` (L346)    CONTRADICCIÓN VIGENTE en su cláusula «cero apariciones en
                                    el documento 11». Es mi `P-05`, GRAVE, y hace que `P-06`
                                    del documento 21 NO esté superado.

LA VÍA DE CORRECCIÓN                NO es reescribir `D97` —eso es `I-16` y el corpus lo
                                    prohíbe—. Es una `D107` que derive el recuento, como `D94`,
                                    o un ADDENDUM, como `D106`(iii). El remedio está probado
                                    dos veces en este mismo fichero y no se ha aplicado aquí.
```

---

## 7 · REFUTACIONES QUE INTENTÉ Y NO CAYERON

Siete. Las escribo con el mismo detalle que los hallazgos, porque valen lo mismo.

**`RF-1` · Intenté que `P-01` cayera por la vía de que §2.9 rescata el tramo, y no cayó del todo —
pero SÍ tumbó la mitad de la tesis de mi propio relevo.**
Abrí §2.9 L3058-L3059 buscando que la reconstrucción del marcador de transacción desde el diario
hiciera inocuo el tramo `[4,5)`. **La encontré**, y por eso rechazo la consecuencia material de
`P1-05` (§4, `X-2`). Pero seguí: §2.6.10 **L2490** dice que el commit lo impide «*un marcador
abierto*» —el **fichero**, no el predicado— y **ninguna sede prescribe podar un marcador
obsoleto**. §7.4 paso 2 sólo pregunta «*¿hay transacciones con `abierta(tx)`?*», que en ese tramo
es falsa, luego no entra en ninguna rama. **La contradicción taxonómica sobrevive entera y la
ambigüedad material es parte del defecto.** Es la refutación que más trabajo me costó y la que más
cambió mi dictamen.

**`RF-2` · Intenté tumbar el recuento de CATORCE presiones del titular de §0, y aguantó.**
Sospeché que el titular fuera el error y la cadena la verdad. Lo deriv é yo: `grep -c '^## \`PN-'`
→ **16**; menos `PN-4` RETIRADA y `PN-5` FUSIONADA → **14**. Crucé con §16 L7920 («`PN-6` a
`PN-16`»: 3 + 11 = 14) y con §19 L8800 («CATORCE PRESIONES NORMATIVAS VIGENTES»). **El titular es
correcto en tres sedes independientes.** Lo roto es sólo la derivación, y por eso `P-04` es sobre
la aposición y no sobre la cifra.

**`RF-3` · Intenté demostrar que `P-01`≡`Q-13` no estaba realmente cerrado, y no cayó.**
No me bastó con que `X54` dijera «DIECIOCHO»: extraje los identificadores de la tabla de §2.6.5
mecánicamente y salieron `W1`…`W11`, `W12a`, `W12b`, `W13`…`W17` = **dieciocho filas, dieciocho
identificadores**, y `X54` los **enumera uno a uno** en vez de dar sólo la cifra, y añade que
`G-26` deriva las filas `W` para que «*el número no vuelva a caducar solo*». **El remedio va más
allá de lo pedido. No cae.**

**`RF-4` · Intenté que la dirección de la referencia `abandonada`↔`deriva` conservara el sentido
antiguo en alguna sede, y no cayó en ninguna de las seis.**
Barrí `deriva_emitida` en el documento 11: **seis apariciones, y las seis son prohibiciones**
—L1877 («*queda PROHIBIDO en esta fase*»), L1892, L1916, L4240 («*PROHIBIDO desde `D105`*»),
L4327, L4387—. Ninguna sede conserva el puntero invertido. Y verifiqué que la lista de la capa B
lleva el verbo nuevo. **`D105` está propagada limpiamente en la dirección de la referencia, y lo
digo aunque `P-01` y `P-09` toquen la misma maquinaria.**

**`RF-5` · Intenté falsar la cita que `PN-15` hace de MI PROPIO LOTE, y las cuatro casan.**
`PN-15` cita `KERNEL.md`:687, :690 y :694-712. Yo tengo ese fichero leído íntegro y las comprobé
una a una: L687 es el diagrama `C0 →[gate fijo, ver G22]→ C1 →…→ C3 →[baseline, ver G23]→ C4`;
L690 es la frase «no es negociable por el sistema»; L694-L712 es `G22` con su timebox de 3
sesiones o 2 semanas, sus **diez** entregables numerados y sus **cuatro** prohibiciones. **Conté
los entregables: diez. Conté las prohibiciones: cuatro.** La evidencia de `PN-15` sobre material
que no puede tocar es **exacta**. Lo digo porque `P-05` ataca la otra mitad de la misma decisión y
la asimetría importa.

> ⁱ **ÚNICA INTERVENCIÓN DE TRANSCRIPCIÓN DE TODO ESTE DOCUMENTO, y se declara aquí.**
> El dictamen de `P` reproducía **literal**, entre comillas, la formulación retirada `R4`.
> `T161` prohibe reproducirla fuera de sus dos sedes declaradas —`C7` y `KERNEL.md`—, y la
> prohibe con razón: es la equivalencia que `E2.4` derogó, y un gate que la reimprime la
> reinstala en el corpus. Se sustituye por su IDENTIFICADOR, que la nombra sin reproducirla.
> **No se ha tocado ni una palabra más de ninguno de los tres dictámenes**, y el juicio de
> `RF-6` —que `C7` y `G29` no se contradicen— queda intacto.

**`RF-6` · Intenté encontrar en `C7` una contradicción con `G29` de `KERNEL.md`, y no la hay.**
Los leí los dos íntegros y crucé cláusula a cláusula. `G29` L1015-L1021 se autodeclara «REVISADA
por la enmienda `E2.4`», conserva por fuente exactamente lo que `C7` L17-L28 dice conservar, deroga
exactamente lo que `C7` deroga —la relación universal que `T161` registra como
`R4-item-una-rama-un-pr`, retirada por `E2.4`—ⁱ y remite a `C7` por su ruta. La tabla
de propiedad de `C7` L80-L92 no contradice ninguna cláusula de `G29`. **La articulación
`KERNEL`↔contrato está limpia**, y es lo mejor construido de mi lote. *(Lo que sí falta —el control
repo fuera de la tabla de propiedad de `C7`— ya está registrado por el corpus en §15.7, y por eso
no lo levanto como hallazgo.)*

**`RF-7` · Intenté que los contratos `C5`, `C6` y `C7` tuvieran segundas sedes de lo mismo, y no
las tienen.**
Era el encargo expreso: «contratos DUPLICADOS o segundas sedes de lo mismo». `C5` **declara la
FORMA y remite las INSTANCIAS a `circuitos/`** («*C5 define la forma, no las instancias*», L36-38).
`C6` declara `SOURCES.toml` como fuente única y **prohíbe copiar su contenido semántico**
nombrando `I5`. `C7` remite la forma copiable del Integration Set a `plantillas/` y su plantilla
vacía la marca como tal. `C6` y `C7` se tocan en workspace y Git y **no se solapan**: `C6` fija
qué es una fuente, `C7` quién ejecuta cada operación sobre ella. **La disciplina de sede única está
bien aplicada entre los cinco contratos que leí**, y el único censo que discrepa es el del índice
(`P-13`), que no es duplicación sino desactualización.

---

## 8 · LO QUE NO HE CUBIERTO, SIN ADORNO

1. **Ningún fichero del lote de `Q`.** No he abierto `CHECKPOINT-ADS-NEXT.md`,
   `comprobar-correccion-gate-de-cierre.py`, `docs/evolucion/00-INDICE.md`, los documentos 10,
   12-14, 19, 20, `verificacion/README.md`, `esquemas/proceso.yaml`, ni
   `recorrido/00-OBLIGACIONES-Y-CIERRE.md`. Consecuencia dura: **`C-L.1`-`C-L.13` quedan sin
   juicio por mi parte**, incluida `C-L.3`, que el encargo puso en mi foco **sin darme su sede**.
   Ocho de los veinticuatro hallazgos del documento 21 los declaro FUERA DE MI LOTE por esto.
2. **No he ejecutado la batería `comprobar-correccion-gate-de-cierre.py`**, ni reproducido `R1`-`R4`,
   ni verificado los tres falsos verdes `Q-01`/`Q-04`/`Q-05`. Sí ejecuté cuatro validadores del
   kernel, y de ahí sale `P-13` y `P-27`.
3. **No he verificado el aparato de `D104`** —las cuatro vías, los nueve pares, los diez anclas—
   contra `01-PROCESOS.md`. `P2` y `P3` lo rederivaron por separado y coincidieron; **yo no lo
   reejecuté**, y no lo cuento entre mis hallazgos ni entre mis refutaciones.
4. **Ningún ojo único recorrió las 9 494 líneas del documento 11.** Ya declarado en §2. Reabrí
   dieciséis regiones, y aun así una contradicción entre §2 y §9 puede habérsenos escapado a los
   tres.
5. **No puedo falsar nada sobre disco real.** `estado/`, `estado/tx/`, `estado/deriva/` y
   `.ads/run/` **no existen en este árbol**: es la distribución, no un producto instalado. `P-01`,
   `P-02` y `P-09` son análisis de **texto contra texto**, y lo digo porque el propio documento
   insiste en la distinción.
6. **Las ~55 anclas `L<nnn>` a OTROS ficheros no están verificadas.** Sólo las dos autorreferencias
   (`P-24`), y las dos están rotas. Es un riesgo sistemático que dejo señalado y sin medir.
7. **`P2-08`, `P2-09`, `P2-11`, `P2-12` y `P2-13` no los reverifiqué** y no los cuento (§4, `X-9`).
8. **No he verificado ninguna cita que el documento 11 hace de los documentos 12-20** —«33
   hallazgos», «43 distintos», «28 consolidados»—. Sólo las del documento 21, que sí leí.
9. **No he juzgado el manifiesto ni el derivador de este gate**, por conflicto de materia, y lo
   declaro en la fila `P-08` de §5 en vez de esconderlo.

---

## 9 · MI RECOMENDACIÓN DE VEREDICTO, Y SUS RAZONES

> **Yo RECOMIENDO. El veredicto lo emite el adjudicador `R`, que no soy yo.** `R` recalcula por su
> cuenta universo, asignaciones, lecturas, cobertura, severidades y recuentos, y puede revocar
> cualquiera de mis veintisiete adjudicaciones, mis seis rechazos y mis tres rebajas.

# INSUFICIENTE PARA F5

### Las razones, numeradas

**1 · Una corrección de este gate anterior no sólo no está superada: está AGRAVADA, y en el punto
exacto que `D105` existe para cerrar.** `R-04` pedía retirar de `W17` la frase que le atribuía un
tramo que su propia condición de detección excluye. La tanda la retiró **afirmando que el punto 7
de §2.6.9 reparte ese tramo a `W8`** — y el punto 7 **no lo reparte así y no se tocó**, cosa que
comprobé con `git show 7764cca` contra el árbol de hoy. El resultado es que **`W17` y el punto 7 se
contradicen sobre `[paso 4, paso 5)` mientras `W17` cita al punto 7 como su aval**, y que el tramo
`[paso 1, paso 2)` sigue asignado a una ventana que exige durable un evento que ahí puede no
existir. Es `P-01` y `P-02`, los dos GRAVES, y **el segundo no lo había visto nadie**.

**2 · La afirmación que este gate me mandó dictaminar expresamente sigue viva, y su corrección se
aplicó a media.** `P-06` del documento 21 atacó «cero apariciones de `G20`/`G21`/`G23` en el
documento 11». La tanda lo corrigió en §16 —donde escribió «*y era falsa*»— y **dejó intacta la
misma frase en `D97` L346**, donde hoy hay 12·10·13 apariciones. El corpus tiene **dos remedios
probados** para hacerlo sin reescribir el registro, `D94` y `D106`(iii), y **no aplicó ninguno**.
Es `P-05`, y el §6 lo dictamina entero.

**3 · Tres hallazgos GRAVES nuevos, ninguno registrado por ninguna `PN` ni por ninguno de los
veinticuatro, tocan cosas que ningún recorrido puede satisfacer.** `P-06`: **ninguna fase de
ningún macrocircuito produce el nivel Estructural** —`gate:sistema-conforme` aparece **una sola
vez en todo el documento, y es su definición**—, luego por la regla de §9.2 ni `INS-4`, ni `A9`,
ni `M5`, ni `INS-7` alcanzan el nivel que certifican, y `O12` no es satisfacible. `P-07`: el
predicado `reconciliacion_pendiente` **no tiene productor** para el canal de órdenes, luego la
prueba `T22` de material **APROBADO** no es satisfacible y el freno 4 de `b.12` no dispara.
`P-08`: `PN-16` presiona por la grafía cuyo derivado **no existe** y deja fuera `VER:decisión`,
que **ya está construida con dos grafías dentro del propio kernel**.

**4 · El §0 —el único tramo que el Owner lee entero— es el que no se propagó, y lo demuestra dos
veces en la misma página.** `P-04`: titular CATORCE y cadena derivante que muere en «`PN-15` lo
lleva a trece», omitiendo la única presión que esta tanda añade. `P-03`: un recuento que se
declara derivado de §15.8 cuando **once decisiones vigentes —`D96` a `D106`, las que este gate
juzga— no tienen bloque en §15.8**. La misma página diagnostica la patología en su línea 16 y la
comete en su línea 128.

**5 · La única garantía mecánica del corpus contra esta clase de defecto pasa en VERDE con la
contradicción delante.** Ejecuté `comprobar_recuentos.py`: `T151 SUPERADA · 1 superadas · 0
fallidas`, mientras `contratos/00-INDICE.md` L7 dice «veintiocho campos» y `C1` L37 dice
«veintinueve» sobre una tabla de veintinueve filas. El validador inspecciona el índice **padre** y
no el de contratos. Es `P-13`, y es un falso verde de la comprobación que existe para esto.

**6 · Y el fichero que dice de sí mismo que contenerlo es un defecto lo contiene.**
`kernel/KERNEL.md` L6: «*Este fichero **NO DEBE** contener nada específico de un proyecto. Si lo
contiene, es un defecto*». `G27`, en sus reglas duras no negociables, dice «*Ver **P44** para el
detalle de **este proyecto***», y no existe ninguna sección `P<nn>` en el fichero. Con ella
sobreviven «Parte I», «Parte II», `P25` y `P30` en la jerarquía de autoridad y en la regla de
sunset, y cuatro referencias cruzadas llevan a la sección equivocada, dos de ellas sobre reglas
canónicas. Es `P-10`, `P-11`, `P-12` y `P-17`: **cuatro hallazgos MEDIOS en la constitución
vendorizada que se copia idéntica en todos los proyectos**, y **ninguno de los veinticuatro
hallazgos anteriores tocó este fichero**, porque hasta este gate nadie lo tenía asignado.

### Y lo que expresamente NO fundamenta mi recomendación

- **NO recomiendo por cobertura.** `asignadas − leídas = 0` en `P`. Las once fuentes están leídas
  íntegras y los once SHA-256 casan con el manifiesto.
- **NO recomiendo por `D105`.** La ataqué por cuatro caminos (`RF-1`, `RF-4`) y su núcleo
  —invertir la referencia, prohibir `deriva_emitida`, dar `fsync` al evento `deriva` con su
  directorio, completar en vez de prohibir— **aguanta entero**. Lo que falla es el reparto de
  ventanas que la recupera, no la decisión.
- **NO recomiendo por la resolución de `D97`.** Es correcta, y la verifiqué contra `KERNEL.md`
  íntegro. Falla su justificación.
- **NO recomiendo porque quede arquitectura por inventar.** Ninguno de mis veintisiete hallazgos
  exige decidir diseño. `P-01` es reescribir una frase del punto 7. `P-04`, una cadena. `P-05`,
  una `D107` o un addendum. `P-10` a `P-13` y `P-17`, ediciones de referencia. Los tres que
  cuestan —`P-06`, `P-07`, `P-08`— son **registrar una presión o nombrar un productor**, y las dos
  cosas el corpus sabe hacerlas.
- **NO recomiendo por el validador en rojo.** `P-27` lo causa el aparato de este gate, no la tanda.

### Lo que consta a favor, y no es cortesía

La aritmética de este documento es **notablemente sólida**: entre los cuatro relevos atacamos las
dieciocho ventanas, las cuarenta y seis filas adversariales con sus dieciséis huecos, el
`34·20·54` de §3.6, los `19+4+2=25` de §3.8 **contra el árbol real**, el censo de nueve sedes de
`abierta(tx)`, el catálogo derivado de `D104` **rederivado dos veces por separado y coincidente**,
y los seis censos «cero / ninguna / un barrido devuelve» de §5 y §6. **Ninguno cayó.** `D105` es
la mejor pieza del expediente y sobrevivió al ataque más duro que supe hacerle. `Q-07`, `R-01`,
`R-03`, `P-01`≡`Q-13`, `P-02`≡`Q-06` y `P-07` están **cerrados con mecanismo**, no con prosa: `X54`
ahora enumera las dieciocho en vez de contarlas, y `G-26` las deriva. La articulación
`G29`↔`C7` está limpia y la disciplina de sede única entre los cinco contratos está bien aplicada.

**Y aun así no recomiendo cerrar, por la razón que este expediente lleva doce tandas persiguiendo
y que esta vez tengo documentada con `git show`: una corrección que se aplica afirmando algo falso
sobre la sede que debía corregirse no es una corrección, es una segunda contradicción firmada con
el identificador de la primera.**

---

**`git status --porcelain` al cerrar: SALIDA VACÍA.** El árbol queda exactamente como lo
encontré, en `706c787`. No he corregido nada, y es deliberado: quien corrige no certifica.

---

# §B · DICTAMEN DEL REVISOR `Q`, LITERAL

# DICTAMEN DEL REVISOR `Q` — GATE INDEPENDIENTE DE CERTIFICACIÓN DE F4c
## Emitido por `Q4`, DICTAMINADOR de la cadena `Q`

```text
REPOSITORIO        /home/jose/ads-kernel
RAMA               gate/f4c-certificacion-20260830
HEAD               706c787189c2241124d0df467f18eb5c5b60667b
FECHA              2026-08-30
INTÉRPRETE         Python 3.12.14 (shim del scratchpad). El python3 del sistema es 3.10.
LABORATORIO        /tmp/lab-Q4, copia completa con .git, BORRADA al cerrar.
RECOMENDACIÓN      INSUFICIENTE PARA F5   (el veredicto lo emite `R`, no yo)
```

---

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

Soy `Q4`. Cierro el dictamen del **REVISOR `Q`**, que se realiza como cadena de relevos con
contexto limpio y tramos disjuntos: **`Q1` · `Q2` · `Q3` · `Q5` · `Q4`**. `Q5` es el relevo que
el `ADDENDUM 1` creó para leer las veintiuna fuentes que ese addendum devolvió al reparto.

**Qué NO soy.** No escribí `F4`, `F4b` ni `F4c`. No apliqué ninguna decisión `D16`–`D106`. No
soy autor de ninguna corrección de ninguna tanda. No fui revisor `A`–`R` de ningún gate
anterior. **No he visto ningún fichero del REVISOR `P`**: no he abierto `P1.md`, `P2.md`,
`P3.md` ni ningún `DICTAMEN-P.md`; el directorio de notas los contiene y no los toqué. No he
usado el subagente `Agent`.

**Orden de trabajo, cumplido.** Leí primero las cuatro notas de mis relevos, después mi propio
lote (el documento 21), y sólo después construí los experimentos. El documento 21 no se abrió
antes que las fuentes, que es la regla del §3bis del manifiesto.

**Modo, y las dos comprobaciones que el encargo exige:**

```text
git status --porcelain  AL ABRIR    → (salida vacía)   VERIFICADO como primer comando
git status --porcelain  AL CERRAR   → (salida vacía)   VERIFICADO como último comando
HEAD al abrir y al cerrar           → 706c787189c2241124d0df467f18eb5c5b60667b, idéntico
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · MERGE              ninguno
```

**Todos mis experimentos se ejecutaron sobre `/tmp/lab-Q4`**, copia completa obtenida con
`cp -a /home/jose/ads-kernel /tmp/lab-Q4`, fuera del repositorio. **El laboratorio quedó limpio
(`git status --porcelain` vacío dentro de la copia) y después se borró con `rm -rf`.** El
repositorio no recibió una sola escritura, ni siquiera la del runner del kernel: la ejecución
de `registrar_evidencia.py` —que muta dos ficheros de evidencia derivada— la hice **en la copia
y no en el árbol**, precisamente para no repetir la mutación que `Q1` tuvo que revertir.

**No corrijo nada.** Ninguno de los hallazgos de abajo está corregido, y es deliberado:
corregirlos aquí volvería a hacer que quien recibe sea quien aplica.

---

## 2 · MANIFIESTO DE LECTURA DEL REVISOR `Q`

Es la **UNIÓN** de los manifiestos de `Q1`, `Q2`, `Q3`, `Q5` y el mío. **Todos los SHA-256 de
esta tabla los he recalculado YO** con `sha256sum` sobre el árbol de `706c787`, y todos los
recuentos de línea con `wc -l`, incluidos los de las fuentes que leyeron otros relevos.

### 2.1 · Qué se le asignó a `Q`, derivado por mí y no copiado

Las fuentes de `Q` son las que le atribuyen los dos manifiestos. **Lo comprobé
mecánicamente**, no de palabra:

```text
$ sed -n '135,160p' .../F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md \
    | awk -F'|' '{gsub(/[ *]/,"",$7); print $7}' | sort | uniq -c
     10 P          ← lote de P
      1 P+Q+R      ← el documento 21
     13 Q
      2 Q+R        ← 00-INDICE y CHECKPOINT-ADS-NEXT

  filas de §4 que contienen «Q» = 16
  filas del ADDENDUM 1 §2       = 21
  ASIGNADAS A `Q`               = 16 + 21 = 37
```

### 2.2 · Las TREINTA Y SIETE fuentes, una fila cada una

| # | ruta | líneas | SHA-256 recalculado por mí sobre `706c787` | quién la leyó | cobertura |
|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 113 | `56d1cdb133108c77f87fe70d096ca2547c04cc733fe84694846b72a5cc873307` | `Q1` | **LEÍDO ÍNTEGRO** |
| 2 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 2382 | `3b6e1f776cc0f89e3068ee3ff9a89c88f6436b68114c3e77d637402d31cef613` | `Q1` | **LEÍDO ÍNTEGRO** |
| 3 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 160 | `5f19d517ec4812e28b003202ffddbfc38885c544febf81e9456af82c7c7b51ff` | `Q1` | **LEÍDO ÍNTEGRO** |
| 4 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 1568 | `d245651397790f64fae51392ede29327ee23b2f28777531aaa88905d1b4c5bff` | `Q2` | **LEÍDO ÍNTEGRO** |
| 5 | `docs/evolucion/verificacion/README.md` | 124 | `3f8741613a060312494f2de2d70043e70c6fea78456a61b00b2fb78f7e9f9fcb` | `Q2` | **LEÍDO ÍNTEGRO** |
| 6 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` | 140 | `c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` | `Q2` | **LEÍDO ÍNTEGRO** |
| 7 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | `Q2` | **LEÍDO ÍNTEGRO** |
| 8 | `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | 130 | `f56e8fe4872e46b5ccc8bd2b9531cdc9e53247aaec1e36ebcae131efbe3674ac` | `Q2` | **LEÍDO ÍNTEGRO** |
| 9 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | `Q2` | **LEÍDO ÍNTEGRO** |
| 10 | `docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md` | 1152 | `48baaa1a8e69c6ef3401eb7a0088dcf06849bd66fa3f238bf3e7b8c8fd14392d` | `Q3` | **LEÍDO ÍNTEGRO** |
| 11 | `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` | 801 | `d7d2e4fa3f878e0c010d979e89affdb63462cc6fdd6628ed885d3a760bde09d1` | `Q3` | **LEÍDO ÍNTEGRO** |
| 12 | `docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md` | 336 | `202ac1af8df5ca6e032cb06f6566c63cf2656fb1a54d65a8c9a0f5d0ef5d41d9` | `Q3` | **LEÍDO ÍNTEGRO** |
| 13 | `docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md` | 764 | `c50e0aa6c1b9827c166171efee1737b2e091cc5518d78bad8c469c709c0dd56f` | `Q3` | **LEÍDO ÍNTEGRO** |
| 14 | `docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` | 797 | `6804d134dfb66b5304ec9c539750559e578a2d5855785b5803189baac2da931f` | `Q3` | **LEÍDO ÍNTEGRO** |
| 15 | `docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md` | 325 | `7f94e236f3cfb11e78762a301d9a3e94939ab47df34658710d1b8686ed7050fb` | `Q3` | **LEÍDO ÍNTEGRO** |
| 16 | `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | 651 | `b0e015c118ceb916e58fc8191b2a5e40cf28c44dd426618fdd49d10e3ea495d6` | `Q5` | **LEÍDO ÍNTEGRO** |
| 17 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | `Q5` | **LEÍDO ÍNTEGRO** |
| 18 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | `Q5` | **LEÍDO ÍNTEGRO** |
| 19 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | `Q5` | **LEÍDO ÍNTEGRO** |
| 20 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | `Q5` | **LEÍDO ÍNTEGRO** |
| 21 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | `Q5` | **LEÍDO ÍNTEGRO** |
| 22 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | `Q5` | **LEÍDO ÍNTEGRO** |
| 23 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | `Q5` | **LEÍDO ÍNTEGRO** |
| 24 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | `Q5` | **LEÍDO ÍNTEGRO** |
| 25 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | `Q5` | **LEÍDO ÍNTEGRO** |
| 26 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | `Q5` | **LEÍDO ÍNTEGRO** |
| 27 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | `Q5` | **LEÍDO ÍNTEGRO** |
| 28 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | `Q5` | **LEÍDO ÍNTEGRO** |
| 29 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | `Q5` | **LEÍDO ÍNTEGRO** |
| 30 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | `Q5` | **LEÍDO ÍNTEGRO** |
| 31 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | `Q5` | **LEÍDO ÍNTEGRO** |
| 32 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` | `Q5` | **LEÍDO ÍNTEGRO** |
| 33 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` | `Q5` | **LEÍDO ÍNTEGRO** |
| 34 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` | `Q5` | **LEÍDO ÍNTEGRO** |
| 35 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` | `Q5` | **LEÍDO ÍNTEGRO** |
| 36 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` | `Q5` | **LEÍDO ÍNTEGRO** |
| 37 | `docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` | 2679 | `9f869ffbdbdb834ca872c03abc8826c125a47b4344ed32cd9b6266db08f8be03` | **`Q4` (yo)** | **LEÍDO ÍNTEGRO** |

**Los 37 SHA-256 los recalculé yo hoy, y los 37 coinciden con los que publican el manifiesto de
asignación y su ADDENDUM 1.** Ninguna divergencia.

### 2.3 · Primera y última sección sustantiva, y DOS anclas de regiones separadas

Publico las mías íntegras y una muestra por relevo; las demás están en las cuatro notas y las
he cotejado contra el árbol.

**`21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` (mi lote, 2679 líneas)**
- Primera sección sustantiva: **L9** `## 1 · Identidad y procedencia`.
- Última: **L2663** `## 14 · Ningún hallazgo se ha corregido, y es deliberado`, cerrada en L2679.
- **Ancla A (L4)**: `> # INSUFICIENTE PARA F5`
- **Ancla B (L1132, a 1128 líneas de la anterior)**: «vigilado por la batería **es derivable del
  corpus** y está escrito a mano. Es `Q-09`.»
- **Tramos**: `1–190`, `190–430`, `425–445`, `440–560`, `560–690`, `690–830`, `830–970`,
  `970–1110`, `1110–1250`, `1250–1400`, `1400–1560`, `1560–1720`, `1720–1880`, `1880–2040`,
  `2040–2200`, `2200–2400`, `2400–2679`. **Unión = [1, 2679]. Ningún tramo sin abrir.**

| relevo | fuente muestreada | 1.ª / última sección | ancla A | ancla B |
|---|---|---|---|---|
| `Q1` | `CHECKPOINT-ADS-NEXT.md` | L1 `# CHECKPOINT — ADS NEXT` / L2293 `## Siguiente acción exacta` | L6 «**Basta decir «Continúa»**» | L1171 «pregunta_pendiente: ninguna. Las TRECE presiones…» |
| `Q2` | `comprobar-correccion-gate-de-cierre.py` | L20 derivación de `RAIZ` / L1560–1568 informe y `sys.exit` | L46 lexicón de numerales | L744 `_efix, _, _, _ = _derivar(_ffix)` |
| `Q3` | `20-GATE-INDEPENDIENTE-…F4C.md` | L8 `## 1 · Identidad y procedencia` / L779 `## 11 · Ningún hallazgo se ha corregido` | L62 «BLOQUE C (§13–§17)…» | L745 «**Seis razones, cada una suficiente por sí sola:**» |
| `Q5` | `diseno/04-CICLO-DE-CALIDAD.md` | L49 `## Los retornos` / L107 `## Qué estaciones se ejecutan…` | L4 «Trece estaciones… **seis de ellas** pueden devolver» | L109 «**Esta tabla no es una fuente: se deriva.**» |

### 2.4 · LA RESTA, explícita

```text
ASIGNADAS A `Q`                    37   16 del manifiesto §4 + 21 del ADDENDUM 1
LEÍDAS ÍNTEGRAS POR LA CADENA      37   Q1 3 · Q2 6 · Q3 6 · Q5 21 · Q4 1
PARCIALES                           0
NO ABIERTAS                         0

ASIGNADAS − LEÍDAS ÍNTEGRAS  =  ∅   (conjunto VACÍO)
```

**Cautela que declaro y que NO debilita la resta.** `Q1`, `Q2` y `Q3` trabajaron sobre `HEAD =
44d2e74`; `Q5` y yo sobre `706c787`. Comprobé que la diferencia es un solo fichero:

```text
$ git diff --name-only 44d2e74..HEAD
docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md
```

y **recalculé hoy los quince SHA-256 de las fuentes de `Q1`, `Q2` y `Q3`: los quince coinciden
con los que ellos declararon.** Sus lecturas describen los bytes de mi árbol.

**Por tanto: NO procede la recomendación `INSUFICIENTE PARA F5 POR COBERTURA`.** Mi
recomendación se emite sobre el fondo, y lo digo aquí, antes del veredicto, como el encargo
manda.

---

## 3 · LA REPRODUCCIÓN DE `M-04`, EXPERIMENTO A EXPERIMENTO

`Q2` afirma haber construido **seis árboles defectuosos distintos que pasan la batería 30/30 en
verde**, dos de ellos BLOQUEANTES. Es la afirmación más fuerte de todo el gate y **la he
reproducido yo, las seis**, sobre `/tmp/lab-Q4`, con `.git` incluido.

```bash
cp -a /home/jose/ads-kernel /tmp/lab-Q4 && cd /tmp/lab-Q4
export PATH=".../scratchpad/toolchain/shim:$PATH"     # Python 3.12.14
python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py
```

**BASELINE sobre la copia limpia:**
```text
OK   G-27    la regla 1 de §2.6.10 usa «los cinco CAMPOS», no «los cinco conceptos»
30/30 comprobaciones en verde
```

### `A` · el BLOQUEANTE de `Q2-01` — segunda sede normativa, sin rastrear, FUERA de `kernel/`

```bash
cat > docs/rediseno/C8-SEGUNDA-SEDE.md   # «CONTRADICE deliberadamente a C4-MATERIALIZACION
                                         #  y a C7-GOBIERNO… Esta sede es NORMATIVA y VIGENTE
                                         #  y prevalece sobre las dos anteriores»
cp docs/rediseno/a-CAPACIDADES-APROBADA.md    docs/rediseno/a-CAPACIDADES-APROBADA-BIS.md
cp docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md docs/rediseno/DECISIONES-Y-CONTRADICCIONES-BIS.md
```
```text
?? docs/rediseno/C8-SEGUNDA-SEDE.md
?? docs/rediseno/DECISIONES-Y-CONTRADICCIONES-BIS.md
?? docs/rediseno/a-CAPACIDADES-APROBADA-BIS.md

30/30 comprobaciones en verde
```
**REPRODUCIDO.** Y con el control complementario que lo hace concluyente: **el mismo ataque
DENTRO de `kernel/`** (`01-PROCESOS-BIS.md` + `C8-SEGUNDA-SEDE.md`) da **29/30 y `G-23` lo
caza**. La corrección de `Q-04` se aplicó al perímetro del contraejemplo, no al principio.

### `B` · el BLOQUEANTE de `Q2-02` — la proyección «ÚNICA» que admite una segunda

Inserté en el bloque de `SALIDA ESPERADA` de `D104` (`11-ARQ` tras L9079):

```text
**PROYECCIÓN SEGUNDA, Y ES LA VIGENTE**: el catálogo
estático tiene SEIS procesos y emite DIEZ pares, y
`(DEP, SEG)` NO se deriva por la vía 2 sino por la vía 4.
```
```text
30/30 comprobaciones en verde
```
**Y el CONTROL, que es lo que lo convierte en prueba.** La misma contradicción escrita con la
redacción literal —`**SEIS procesos y DIEZ pares**, y es la vigente.`— sí cae:
```text
FALLO G-15    `<CAP>:revision` derivado por las CUATRO vías…
29/30 comprobaciones en verde
```
**REPRODUCIDO.** El contrato de `D104` promete literalmente que «una segunda proyección en el
mismo bloque es el contraejemplo de `M-04`, **y la comprobación la suspende**». No la suspende:
basta interponer dos palabras entre «procesos» y el numeral. El patrón es
`([A-ZÁÉÍÓÚa-z]+) procesos . ([A-ZÁÉÍÓÚa-z]+) pares` (L555) y exige **exactamente un carácter**
entre los dos.

### `C` · `Q2-06` — la excepción del kernel es por RUTA, no por CONTENIDO

```bash
echo 'import sys; sys.exit(0)' > kernel/operativo/validadores/comprobar_negativos.py
echo 'TODO EN VERDE. 0 fallos. (falsificado)' > kernel/operativo/pruebas/evidencia/negativos-salida.txt
echo 'huella falsificada' > kernel/.upstream-hash
```
```text
 M kernel/.upstream-hash
 M kernel/operativo/pruebas/evidencia/negativos-salida.txt
 M kernel/operativo/validadores/comprobar_negativos.py

30/30 comprobaciones en verde
```
**REPRODUCIDO.** El comentario que precede a `COD_AUTORIZADO` (L1085) promete «Excepciones
AUTORIZADAS, una a una. **No hay comodines sobre directorios de código**» y a continuación
exime `kernel/operativo/pruebas/evidencia/` entero y tres rutas cuyo CONTENIDO no se fija de
ninguna manera — incluida `.upstream-hash`, que es la única evidencia que cubriría la
mutilación del validador.

### `D` · `Q2-05` — el contraste de `G-16` contra la sede canónica es por PREFIJO

Reescribí la fila de detalle VIGENTE de `C-L.1` en el checkpoint:
```text
C-L.1  CERRADA SOLO EN PARTE, SIGUE ABIERTA Y BLOQUEA F5 · D96 no cierra nada
```
```text
30/30 comprobaciones en verde
```
**REPRODUCIDO.** `G-16` usa `if not any(_det.startswith(a) for a in _admitidos)` (L881). La
sede canónica declara la condición **abierta y bloqueante** mientras el resumen la cuenta entre
las CORREGIDAS, y el contraste que la refutación 3 de `M-04` obligó a añadir no lo ve porque la
cadena sigue empezando por «CERRADA».

### `E` · `Q2-04` — `G-26` se desactiva escribiendo «regresión» en la línea

Sobre `CHECKPOINT-ADS-NEXT.md` **L2339**, la línea `5  QUÉ LLEVAR AL OWNER`:

```text
E-a   «CATORCE» → «ONCE», a secas
      FALLO G-26 · 29/30                      ← la comprobación FUNCIONA

E-b   la MISMA cifra falsa + « (sin regresión)» al final de la MISMA línea
      5  QUÉ LLEVAR AL OWNER  las **ONCE** presiones de §16 …  (sin regresión)
      30/30 comprobaciones en verde           ← la comprobación DESAPARECE
```
**REPRODUCIDO, y es el más grave de los seis.** Es `P-05`≡`Q-08` —el **único GRAVE** que `R`
adjudicó en el gate anterior, la cifra falsa hacia el Owner en la sede que la cabecera designa
como punto de entrada— **reinstalable con dos palabras**. La causa está en L1347:
`_BLOQUE_HISTORICO = re.compile(r"\[HISTÓRICO|\bHISTÓRICO\b|\bcaducad|\bregresión\b")`, evaluada
sobre **la LÍNEA ENTERA**, al contrario que las otras dos ramas de `_es_cita`, que se evalúan
sobre la OCURRENCIA. Y «regresión» es vocabulario corriente del corpus.

### `F` · `Q2-03` — `G-01` se desactiva escribiendo «RETIRADA»

Inserté en §16 un párrafo que **ANULA** la retirada:
```text
NORMA VIGENTE REINSTAURADA: el estado en cuarentena vive en `estado/cuarentena/<ID>/`
y esa ruta es CANONICA y fuente de verdad para todo el sistema. La nota que hablaba de
una RETIRADA queda SIN EFECTO y no se aplica.
```
```text
OK   G-01    cero `estado/cuarentena/` VIGENTE: toda mencion que queda declara su retirada
30/30 comprobaciones en verde
```
**REPRODUCIDO.** `G-01` (L117) exime el párrafo entero si contiene `RETIRADA` en cualquier
posición, `re.I`, sin polaridad. El párrafo que **deroga** la retirada satisface el exento.

### VEREDICTO DE §3

> ## `M-04` SIGUE VIVA, y más ancha que cuando `R` la declaró FALLIDA.
>
> **Seis árboles defectuosos distintos, construidos por mí y ejecutados por mí, pasan la
> batería 30/30 en verde.** Dos de ellos (`A`, `E`) son contraejemplos ya adjudicados por el
> gate anterior —`Q-04` y `P-05`≡`Q-08`— reinstalados con **un cambio de directorio** y **dos
> palabras**. Confirmo la afirmación de `Q2` sin reservas y sin rebajarla: la reproduje entera,
> en mi copia, con mis manos.

**Y confirmo también lo contrario, porque es la mitad honesta.** La tanda **cerró de verdad**
las tres vías concretas que se le encargaron, y lo verifiqué con controles positivos propios:

```text
Q-01  sin .git → 25/30, y G-11b FALLA CERRADO           («falla CERRADO sin git» en su título)
Q-02  capacidad_productora: "VER:dosier" en INC → el ancla NO se mueve: anclas sin VER
      siguen siendo ['AUD','INV']. `obl_base = [_base(v) for v in obl]`. CERRADA
Q-03  DOM/SEG desnudos en FEA → FALLA G-15: «reparto por vía 3: publica 0 y deriva 2;
      vía 4: publica 8 y deriva 6». CERRADA
Q-04  el mismo ataque DENTRO de kernel/ → 29/30, G-23 lo caza. CERRADA en su perímetro
Q-05  capacidad_productora inyectada en un escalar `>` → FALLA G-15 y NOMBRA el campo:
      «prosa con aspecto de campo en `proceso:FEA` → `criterio_de_satisfaccion`
       (sección obligatorias)… Un escalar de prosa NO declara participación». CERRADA
      para escalares de bloque
```

Las cinco correcciones funcionan **en el perímetro exacto del contraejemplo que las motivó**, y
en ninguna otra parte. Ése es el hallazgo de método, y los seis árboles son sus instancias.

---

## 4 · HALLAZGOS DE `Q`, CONSOLIDADOS

Severidad **adjudicada por mí**, con el criterio que declaro y que es el que `R` usó en el gate
anterior: **BLOQUEANTE = obliga a decidir arquitectura nueva · GRAVE = una garantía publicada no
se sostiene, o `F6` construiría algo distinto de lo que el contrato quiere · MEDIO = una
afirmación vigente es falsa sin cambiar el comportamiento · MENOR = editorial.**

```text
BLOQUEANTE   0
GRAVE        8
MEDIO       12
MENOR       21
            ──
            41
```

### GRAVES

---
**`Q-01` · GRAVE · `M-04` sigue viva: seis árboles defectuosos distintos pasan 30/30 en verde.**
**Fichero.** `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py`, íntegro.
**Por qué es defecto.** La condición 7 del gate anterior («la batería no ofrece falsos verdes»)
se declaró CUMPLIDA sobre `R1`–`R4`, y `R` dejó escrito que fuera de ellas había **tres** falsos
verdes. Hoy hay **seis**, dos de ellos los contraejemplos ya adjudicados, meramente desplazados.
**Quién lo levantó.** `Q2` (§2, seis experimentos). **Reproducido por mí:** los seis, §3.
**Rebajo la severidad que `Q2` propuso** (BLOQUEANTE) porque ninguno obliga a decidir
arquitectura: todos se cierran con material que el corpus ya tiene escrito.

---
**`Q-02` · GRAVE · La corrección de `Q-04` se aplicó bajo `kernel/` y el mismo ataque un
directorio afuera pasa 30/30.**
**Fichero y línea.** batería **L1171** y **L1100**.
**Cita literal (L1171).** `_base_kern_raw = _git("ls-tree", "-r", "--name-only", "05f71b7", "--", "kernel/")`
**Cita literal (L1100).** `prohibidos += [f for f in tocados if re.search(NORMATIVO, f)]`
**Por qué es defecto.** `NORMATIVO` (L1073–1076) nombra `a-CAPACIDADES-APROBADA`,
`b-RECORRIDO-APROBADA`, `a-ENMIENDA-E1`, `a-ENMIENDA-E2`, `C4-MATERIALIZACION` y `C7-GOBIERNO`
—material que vive fuera de `kernel/`— y sólo lo confronta contra `tocados`, que son ficheros
**rastreados y modificados**. La comparación de CONJUNTOS, la única que ve las adiciones sin
rastrear, existe **sólo para `kernel/`**. El título publicado de `G-23` dice «lo normativo
**intacto**» sin matiz. **Quién.** `Q2-01`. **Reproducido por mí:** experimento `A` + control.

---
**`Q-03` · GRAVE · La unicidad de proyección que el contrato de `D104` promete no existe: se
derrota reformulando.**
**Fichero y línea.** batería **L555**.
**Cita literal.** `_proys = re.findall(r"([A-ZÁÉÍÓÚa-z]+) procesos . ([A-ZÁÉÍÓÚa-z]+) pares", b19p)`
**Por qué es defecto.** El contrato promete que «una segunda proyección en el mismo bloque es el
contraejemplo de `M-04`, y la comprobación **la suspende**». El patrón exige exactamente **un
carácter** entre «procesos» y el numeral siguiente; con dos palabras intermedias el bloque
publica dos cifras incompatibles del mismo objeto **en verde**. Es la refutación 2 de `M-04`
reabierta. **Quién.** `Q2-02`. **Reproducido por mí:** experimento `B`, con su control literal.

---
**`Q-04` · GRAVE · `G-26` se desactiva escribiendo «regresión» en la línea, y con ello se
reinstala el único GRAVE del gate anterior.**
**Fichero y línea.** batería **L1347** y **L1350–1351**.
**Cita literal.** `_BLOQUE_HISTORICO = re.compile(r"\[HISTÓRICO|\bHISTÓRICO\b|\bcaducad|\bregresión\b")`
**Por qué es defecto.** Esta rama de `_es_cita` se evalúa sobre la **LÍNEA ENTERA**, al contrario
que las otras dos, que se evalúan sobre la **OCURRENCIA** — y el propio corpus fijó esa
disciplina por escrito para `G-26` («sobre LA OCURRENCIA CONCRETA del numeral, no sobre la línea
entera», L1338–1341). «regresión» es vocabulario corriente: aparece como sustantivo técnico en
`01-PROCESOS.md` L166, L169, L185, L233. Cualquier sede viva que mencione una regresión queda
fuera del control de recuentos, **incluida la línea que lleva la cifra al Owner**.
**Quién.** `Q2-04`. **Reproducido por mí:** experimento `E`, con control negativo y positivo.

---
**`Q-05` · GRAVE · La excepción del kernel se concede por RUTA y no por CONTENIDO: validador
mutilado, evidencia falsificada y huella sobrescrita dan 30/30.**
**Fichero y línea.** batería **L1085–L1096**.
**Cita literal.**
```python
COD_AUTORIZADO = {"kernel/operativo/validadores/comprobar_negativos.py"}
DOC_AUTORIZADO = {"kernel/operativo/entrada/02-CIRCUITO.md"}
HUELLA         = {"kernel/.upstream-hash"}
...
    if f.startswith("kernel/operativo/pruebas/evidencia/"):
        return False
```
**Por qué es defecto.** El comentario inmediatamente anterior promete «No hay comodines sobre
directorios de código» y a continuación exime uno entero. La autorización de
`comprobar_negativos.py` era para **un arreglo nombrado** (`N158g`); nada fija su contenido. Y
`.upstream-hash` —la huella que según el propio comentario «cubre el código de los
validadores»— está en el conjunto libre, de modo que la única evidencia que detectaría la
mutilación se puede reescribir en la misma tanda. **Quién.** `Q2-06`. **Reproducido:** exp. `C`.

---
**`Q-06` · GRAVE · El contraste de `G-16` contra la sede canónica es por PREFIJO: una `C-L`
declarada ABIERTA Y BLOQUEANTE en su detalle se cuenta entre las CORREGIDAS.**
**Fichero y línea.** batería **L878–L884**.
**Cita literal.** `if not any(_det.startswith(a) for a in _admitidos):`
**Por qué es defecto.** Este contraste se añadió exactamente para cerrar la refutación 3 de
`M-04`. Un `startswith` deja pasar cualquier calificación posterior que invierta el sentido.
**Quién.** `Q2-05`. **Reproducido por mí:** experimento `D`.

---
**`Q-07` · GRAVE · `G-01` se desactiva escribiendo la palabra «RETIRADA» en el párrafo.**
**Fichero y línea.** batería **L117**.
**Cita literal.** `if re.search(r"RETIRADA|se resuelve sin crear una tercera fuente", par, re.I): continue`
**Por qué es defecto.** El discriminante entre norma viva y texto histórico es la **mera
presencia** de una palabra, sin polaridad ni posición. La comprobación titulada «cero
`estado/cuarentena/` VIGENTE» no puede distinguir una retirada de su derogación.
**Quién.** `Q2-03`. **Reproducido por mí:** experimento `F`.

---
**`Q-08` · GRAVE · La batería canónica del kernel NO da 13/13 sobre el árbol que se certifica, y
el árbol NO queda limpio después. Y es PEOR que cuando `Q1` lo midió.**
**Fichero y línea.** `docs/rediseno/CHECKPOINT-OPERATIVO.md` **L79–L82**;
`docs/evolucion/CHECKPOINT-ADS-NEXT.md` **L2151–L2157**.
**Cita literal (`CHECKPOINT-OPERATIVO` L80–L81).**
```bash
python3 kernel/operativo/validadores/registrar_evidencia.py
git status --short          # tiene que quedar vacío: los generados son deterministas
```
**Por qué es defecto.** Sobre `706c787` el runner devuelve **12/13**, el validador `referencias`
falla, y `git status --porcelain` **no queda vacío**: dos ficheros de evidencia derivada quedan
modificados. Las dos sedes que publican la orden de comprobación afirman lo contrario, en su
sección «Cómo se comprueba que esto sigue en pie», sin marca de histórico.
**Reproducido por mí, en `/tmp/lab-Q4` y NO en el repositorio:**
```text
12/13 validadores en verde · 12 evidencias publicadas · 1 problemas
 M kernel/operativo/pruebas/evidencia/fuentes-salida.txt
 M kernel/operativo/pruebas/evidencia/negativos-salida.txt

T147  FALLIDA   Todo documento es alcanzable por ruta, y ninguna referencia es ambigua
   · …/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md: no lo alcanza ningún enlace por ruta…
   · …/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md: no lo alcanza ningún enlace por ruta…
```
**AGRAVO el hallazgo de `Q1`.** `Q1` midió **un** fichero denunciado por `T147`; en mi HEAD son
**DOS**: el ADDENDUM 1 añade el segundo. La laguna es estructural y no accidental:
`exclusiones.yaml` no contempla `docs/evolucion/verificacion/manifiestos/`, de modo que **todo
gate futuro que publique su manifiesto —y `C-L.5` OBLIGA a publicarlo— romperá `T147` igual, y
un manifiesto más cada vez**. **Quién.** `Q1-01`, ampliado por mí.
**Y digo la atenuante entera, contra mi propio interés:** la rotura la introducen los dos
commits que **este mismo gate** añadió sobre la candidata `4d231ee`; sobre la candidata la
batería casi con certeza daba 13/13. Hay dos lecturas legítimas —defecto del procedimiento del
gate, o incumplimiento del árbol que se juzga— y **no la resuelvo yo**. Lo que sí es defecto del
corpus con independencia de eso es la laguna de `exclusiones.yaml`.

### MEDIOS

| id | qué es | fichero y línea | quién | ¿reproducido por mí? |
|---|---|---|---|---|
| `Q-09` | `Q-05` cerrada sólo para ESCALARES: la INDENTACIÓN que su propia docstring promete no se aplica | batería **L407** (promesa) contra **L410–437** | `Q2-11` | **SÍ**, con fixture propio. Un `capacidad_productora: "DOM"` anidado dos niveles bajo una clave inventada da `[('DOM', 2, 'obligatorias'), ('SEG', 4, 'condicionales')]`, `prosa_sospechosa = []` **y además desplaza el ancla a `DOM`**. Peor de lo que `Q2` describió |
| `Q-10` | El conjunto vigilado se deriva con `re.search` sobre PROSA, y el fixture «7bis» que lo respalda es una TAUTOLOGÍA que no puede fallar, contada entre los «17 fixtures en verde» | batería **L372–382** y **L748–753** | `Q2-09`·`Q2-12`·`Q5-05` | **SÍ**, por lectura de código: `_VIGILADAS = _derivar_vigiladas()` **es** la misma comprensión de conjunto sobre los mismos ficheros. La condición no puede ser verdadera nunca |
| `Q-11` | Censos ESCRITOS A MANO dentro de la batería, uno de ellos MUERTO | batería **L944** (`esperado`, nunca leído después) y **L997** | `Q2-13` | **SÍ**: `awk 'NR>944 && /\besperado\b/'` no devuelve ninguna lectura. `G-17` compara `pubv == derv` |
| `Q-12` | `CHECKPOINT-ADS-NEXT` publica **TRECE** presiones donde el árbol deriva **CATORCE**, y una de las dos sedes lo hace bajo el rótulo «CIFRAS VIGENTES, DERIVADAS» | **L1171–1173** y **L1835/L1843–1845** | `Q1-02`·`Q1-03` | **SÍ**: `grep -c '^## \`PN-'` doc 11 = **16**; `PN-4` RETIRADA (L7994), `PN-5` FUSIONADA (L8022) → **14**. La sección de entrada lo dice bien; estas dos no |
| `Q-13` | `00-INDICE` L58 atribuye al documento 11 «**DOCE** presiones vigentes» y «CORREGIDA DOCE VECES»; **L83 de la misma tabla dice CATORCE** | `00-INDICE.md` **L58** vs **L83** | `Q1-06` | **SÍ**. Doc 11 publica CATORCE en L126, L8559 y L8601. El índice se contradice dentro de una sola tabla |
| `Q-14` | `00-INDICE` L74 declara, en presente y sin marca, «**13/13**», «`T161` = **293**» y «**el gate independiente TODAVÍA NO SE HA INICIADO**» | `00-INDICE.md` **L74** | `Q1-07` | **SÍ**: los tres son falsos hoy; se han ejecutado los gates de los documentos 19, 20 y 21 y éste es el cuarto |
| `Q-15` | `CHECKPOINT-OPERATIVO` L84 dice «los **once** validadores» donde son **trece**, en el documento cuya L6 promete que ninguna cifra se escribe a mano | `CHECKPOINT-OPERATIVO.md` **L84** | `Q1-08` | **SÍ**: `grep -c 'tipo: validador' validadores.yaml` = **13** |
| `Q-16` | «Estado de las fases» —la proyección canónica, **sin marca de histórico**— omite las dos últimas pasadas y declara `C-L.5` abierta contra la clasificación que el mismo fichero rotula VIGENTE | `CHECKPOINT-ADS-NEXT.md` **L1446–1487** | `Q1-04` | **SÍ** |
| `Q-17` | La regla de derivación del ordinal de la tanda **no ejecuta**: §15.8 del doc 11 da TRECE bloques y su último es `D87`–`D95`; `00-INDICE` da CATORCE | `CHECKPOINT-ADS-NEXT.md` **L2333–2337** | `Q1-05` | **SÍ**: §15.8 = L7654–7909, último `### D87–D95` en L7865; cabecera del doc 11 L12–15 sigue diciendo «CORREGIDO DOCE VECES … la decimotercera es ésta, `D87`» |
| `Q-18` | El documento 20 **afirma tener** manifiestos de lectura fichero a fichero con SHA-256 y **no tiene ninguno**; su adjudicador declara la regla de cierre NO CERTIFICABLE y `C-L.5` ABIERTA a trece líneas de la cita que se le atribuye | doc 20 **L127–129** contra **L638 / L651 / L656 / L801** | `Q3-01`·`Q3-02` | **SÍ**: `sed -n '152,533p' | grep -cE '[0-9a-f]{64}'` → **0**; `grep -c 'LEÍDO ÍNTEGRO'` → **0**. Ver §7: **REMEDIADO procedimentalmente dentro de este gate** |
| `Q-19` | `04-CICLO-DE-CALIDAD` L4 dice «**seis** de ellas pueden devolver hacia atrás» y su propia tabla, 47 líneas más abajo, lista **SIETE** | `diseno/04-CICLO-DE-CALIDAD.md` **L4** vs **L53–64** | `Q5-01` | **SÍ**: columna `desde` = {4, 5, 6, 8, 9, 11, 12}. **Rebajo de GRAVE a MEDIO** (ver §5) |
| `Q-20` | `04-CICLO` L61 prescribe un retorno «9 validación visual → 10 construcción, rechazo por **fidelidad**» que `02-RUBRICAS` hace imposible, y la corrección de `A-21` («los NUEVE ejes tienen destino», L70) se apoya en esa fila | `04-CICLO` **L61** vs `02-RUBRICAS` **L215**, **L272–285** | `Q5-02` | **SÍ**: `02-RUBRICAS` L280 marca `fidelidad` como `pendiente-de-construccion` en la estación 9 y L281 dice que un rechazo ahí «vuelve a exploración, convergencia o prototipo». **Rebajo de GRAVE a MEDIO** |

Y un doce que es de `Q5` y lo mantengo en MEDIO:
**`Q-21` · MEDIO ·** `00-SISTEMA-DE-EXCELENCIA` L59 y `02-RUBRICAS` L119 dicen «los **diez**
motivos … cada uno tiene su eje» y los ejes derivados son **NUEVE** (verificado: `awk 'NR>=121
&& NR<=200' 02-RUBRICAS.md | grep -c "^  - id:"` → 9). Dos colisiones y un eje huérfano
(`acabado`). Levantado por `Q5-03`, reproducido por mí.

### MENORES (21)

| id | qué es | sede | quién | ¿lo reproduje? |
|---|---|---|---|---|
| `Q-22` | La guarda de base VACÍA de `G-11b` es CÓDIGO MUERTO: `"".split("\n") == ['']`, que es verdadero | batería L266–271 | `Q2-08` | **SÍ** (código + `python3 -c`). **Rebajo de MEDIO a MENOR**: `G-11b` **sí** falla cerrado hoy por `_base_raw is not None`; el hueco exige un `git` que salga 0 con stdout vacío |
| `Q-23` | `G-22` cubre sólo modificaciones RASTREADAS: una copia sin rastrear del documento 16 pasaría | batería L1050–1056 | `Q2-07` | NO reproducido por mí; el mecanismo es el mismo de `Q-02`, ya reproducido |
| `Q-24` | La batería ABORTA con traceback y sin informe ante un fichero del kernel ausente o no-UTF-8, antes de que `G-24` pueda diagnosticarlo | batería L39, alcanzado desde L378 y L523 | `Q2-10` | NO reproducido; confirmado por lectura de orden de ejecución |
| `Q-25` | El README publica de `G-20`, `G-23` y del «lector estructurado» promesas por encima del código | `verificacion/README.md` L55, L60, L62–63 | `Q2-14`·`Q2-15` | **SÍ** para `G-20`: el código deriva el tope y hoy da `D1-D106`; el README dice «`D1`–`D95`» |
| `Q-26` | Los documentos **19, 20 y 21** no están fijados por ningún rango inmutable (`docs/evolucion/1[5-8]-`) | batería L1056 | `Q2-16` | Confirmado por lectura del patrón |
| `Q-27` | `_CAPS` incluye FICHEROS y no sólo directorios, mientras `G-24` filtra por `isdir`: dos comprobaciones que dicen derivar el mismo conjunto | batería L360 vs L1288–1289 | `Q2-17` | Confirmado por lectura |
| `Q-28` | La PROCEDENCIA se conserva y **no se contrasta contra nada publicado**: el reparto obligatorias/condicionales (1 / 8) no aparece en ninguna sede | batería L546, L568–576 | `Q2-18` | Confirmado: `G-15` publica el reparto por VÍA, no por PROCEDENCIA |
| `Q-29` | **MÍO.** El `ADDENDUM 1` afirma que las DOCE agotadas restantes tienen en el doc 21 «su ruta, sus líneas y **su SHA-256**». Tres de ellas —`entrada/00`, `02`, `04`, citadas en doc 21 **L1056–L1058**— publican **sólo los 16 primeros hexadecimales** | ADDENDUM 1 L77–79 vs doc 21 L1056–1058 | **yo** | **SÍ**. Verifiqué además que los doce SHA-256 completos **coinciden byte a byte con el árbol de hoy**, de modo que la regla 2 se cumple; lo que falla es la descripción |
| `Q-30` | La aritmética con que `O` retira la quinta razón de veredicto de un revisor —«su total declarado sólo cuadra incluyéndolo»— es **falsa por 19 líneas** | doc 20 L628 vs L76–85 | `Q3-03` | **SÍ**: 9058+1152+1898+677+1132+1288+1590+862+8735 = **26 392**, declarado **26 411**. El total de `N` sí cuadra (5 799 + 8 735 = 14 534) |
| `Q-31` | Doc 19 L310 y L898–899 definen el BLOQUE C de `ADS-PENDIENTES` como **§13–§15**; es **§13–§17** | doc 19 vs doc 20 L62 | `Q3-05` | **SÍ**: `## 17. Decisiones pendientes` en L1120, `# BLOQUE D` en L1137. Doc 20 acierta; el defecto es de un dictamen inmutable |
| `Q-32` | El manifiesto repite 21 veces la conflación commit/árbol que `O` corrigió por escrito (`c3d6465` es un commit; su árbol es `db26b4d`) | manifiesto §5 | `Q3-06` | Confirmado |
| `Q-33` | Doc 13 fija «ERRATA CONFIRMADA · DIEZ» sobre una cifra que doc 12 hoy contradice (ONCE), sin marca de que su verificación quedó superada | doc 13 L42, L618 vs doc 12 L620–621 | `Q3-07` | Confirmado |
| `Q-34` | La cita falsa de `a.6` L504–505 sobrevive en `D92` sin la nota al pie que el corpus sí puso a `O15`, `O16` y `D38` | `DECISIONES` L293 | `Q3-08` | Confirmado |
| `Q-35` | `rama_de_trabajo` nombra rama y base de dos tandas atrás, dentro del bloque `freshness: vigente` | `CHECKPOINT` L438–442 | `Q1-10` | Confirmado |
| `Q-36` | «Siguiente acción exacta» puntos 0 y 7 describen como pendiente lo que el propio árbol ya ejecutó | `CHECKPOINT` L2296–2304, L2358–2365 | `Q1-11` | Confirmado, con la atenuante de que el fichero es idéntico al de la candidata |
| `Q-37` | La sede canónica de `C-L.5` conserva cabecera y primer párrafo diciendo «abierta, y no la cierra esta tanda», sesenta líneas antes de declararse CERTIFICADA | doc 11 L9390, L9400 vs L9483 | `Q1-12` | **SÍ**, verificado línea a línea |
| `Q-38` | Tercer bloque de estado histórico sin la marca `[ESTADO ANTERIOR]` que llevan los dos anteriores | `CHECKPOINT` L334 vs L69, L200 | `Q1-09` | **SÍ**: `grep -n 'ESTADO ANTERIOR'` → sólo 69 y 200 |
| `Q-39` | Ninguna de las quince fichas declara sus `prompts`: los 36 ficheros cuelgan de un enlace a directorio | las quince `CAPACIDAD.md` | `Q5-06` | Confirmado |
| `Q-40` | `00-SISTEMA` L37 dice «ambos [gates] son obligatorios» y la ficha `DIS` declara un solo `gate:` escalar | `00-SISTEMA` L37 vs `DIS/CAPACIDAD.md` L41 | `Q5-07` | Confirmado |
| `Q-41` | El índice de `00-SISTEMA` L138 rotula el directorio de **seis** métodos como «los tres procedimientos», tres líneas antes de decir «sus seis métodos» | `00-SISTEMA` L138 vs L140 | `Q5-08` | Confirmado |
| `Q-42` | `04-CICLO` L101–105 declara exhaustivamente «las únicas comprobaciones de hardware» y omite dos de los tres gates de `mobile-app` | `04-CICLO` L101–105 | `Q5-04` | Confirmado |

*(Numeración corrida `Q-01`…`Q-42`; el censo de arriba dice 41 porque `Q-21` se contabiliza en
MEDIO y no en MENOR. **Total de hallazgos distintos: 42** — 8 GRAVES, 13 MEDIOS, 21 MENORES.
Rectifico aquí el recuento derivándolo de las filas y no del borrador, que es lo que el corpus
exige de sí mismo.)*

---

## 5 · HALLAZGOS QUE RECHAZO O REBAJO DE MIS PROPIOS RELEVOS

1. **RECHAZO la severidad BLOQUEANTE de `Q2-01` y `Q2-02`.** Los hechos son ciertos y los
   reproduje; la severidad no. Un BLOQUEANTE, en la escala que el propio expediente usa, obliga
   a **decidir arquitectura nueva**. Ninguno de los dos lo hace: `Q2-01` se cierra comparando el
   conjunto del árbol también fuera de `kernel/` —el mecanismo ya existe, escrito, para
   `kernel/`—, y `Q2-02` se cierra troceando el bloque por proyecciones en vez de por un patrón
   de línea. **Los adjudico GRAVES.** Y digo lo que esto NO cambia: mi recomendación es la
   misma con GRAVE que con BLOQUEANTE.

2. **REBAJO `Q2-08` de MEDIO a MENOR.** `Q2` lo presenta como «el modo de fallo de `Q-01`, un
   escalón más adentro». Lo comprobé: **`G-11b` HOY FALLA CERRADO**. Su predicado es
   `_base_raw is not None and not difs`, y sin `.git` la batería da 25/30 con `G-11b` en rojo,
   que reproduje. Lo que sobrevive es que la rama `elif not base:` es inalcanzable —cierto,
   `"".split("\n") == ['']`—, es decir **código muerto**, no una vía de falso verde. El
   escenario que `Q2` construye (`E1c`) exige un `git` que devuelva código 0 con stdout vacío,
   que no es el modo de fallo de `Q-01`.

3. **REBAJO `Q5-01` y `Q5-02` de GRAVE a MEDIO.** El propio `Q5` invita a ello y tiene razón en
   invitarlo: son contradicciones documentales dentro de un sistema de diseño **que no está
   construido**, sin garantía publicada que se caiga ni consecuencia para `F6` distinta de leer
   la sede correcta. En la escala que `R` aplicó a los 24, eso es MEDIO.

4. **DECLARO SUPERADO `Q3-04`** («el recuento de entradas de `N` no deriva, y de ese número
   cuelgan 21 agotamientos»). Es correcto en el hecho, y **ha dejado de tener consecuencia**:
   el `ADDENDUM 1` retiró esas 21 fuentes del agotamiento y las devolvió al reparto de lectura,
   donde `Q5` las leyó íntegras. El hallazgo ya no cuelga de nada.

5. **NO ADJUDICO NADA DEL FOCO DE `P`, y lo digo expresamente.** El protocolo transaccional,
   `D105`, `abandonada`→`deriva` y la dirección de la referencia, las DIECIOCHO ventanas y
   `W17`, `W8` frente a `W17`, `fsync`, marcador y durabilidad, `PN-15`/`PN-16`, los contratos
   `C1`–`C7`, `KERNEL.md`, `(a)`, `(b)`, `E1`, `E2`, y la afirmación conservada en `D97` sobre
   `G20`/`G21`/`G23`: **no los presumo cerrados ni abiertos.** No he leído esas fuentes; están
   en el lote de `P`, y sustituir una lectura ausente por una inferencia es el defecto que este
   expediente lleva cuatro gates persiguiendo. Donde una sede de mi lote los roza —`Q-37`, la
   cabecera de `C-L.5`— juzgo sólo la coherencia interna de la sede, que es lo mío.

---

## 6 · LOS 24 HALLAZGOS DEL DOCUMENTO 21, EN EL FOCO DE `Q`

Verificados **uno a uno contra el árbol de hoy**, no contra lo que la tanda dice de sí misma.
«SUPERADO» significa: la corrección está hecha **y es suficiente**.

| # | id | qué exigía | qué dice la tanda que hizo | qué encuentro YO | veredicto |
|---|---|---|---|---|---|
| 1 | `P-01`≡`Q-13` | `X54` decía «diecisiete» y §2.6.5 deriva DIECIOCHO | reescribió `X54` nombrando `W17`; `G-26` deriva las filas `W` | L1488: «cada una de las **DIECIOCHO** ventanas … **`W17` incluida expresamente**». `grep` sobre las 54 filas `X`: **1** menciona `W17` (antes 0) | **SUPERADO** |
| 2 | `P-02`≡`Q-06` | la capa B conservaba «DECLARA SU `deriva`» | corrigió el verbo | **FUERA DE MI LOTE** — es materia de `P`. No lo presumo | **FUERA DE MI LOTE** |
| 3 | `P-03` | tesis RECHAZADA por `R` | no altera `D105` | **FUERA DE MI LOTE** | **FUERA DE MI LOTE** |
| 4 | `P-04` | el checkpoint contaba 9 ventanas `RC-*` retiradas | corrigió el inventario | **FUERA DE MI LOTE** (`P`) | **FUERA DE MI LOTE** |
| 5 | `P-05`≡`Q-08` | **GRAVE**: cinco afirmaciones falsas en la sede de entrada | reancló la sección; hoy dice CATORCE y deriva | `Q1` verificó sus ocho afirmaciones factuales una a una: la sección dice hoy la verdad. **PERO** reproduje que la MISMA línea vuelve a pasar en verde con la cifra falsa y la palabra «regresión» (`Q-04`), y quedan residuos en el punto 0 y el 7 (`Q-36`) | **SUPERADO en el texto, NO en la comprobación que debía impedir su regreso** |
| 6 | `P-06` | `PN-15` declaraba «cero apariciones» de `G20`–`G23` en doc 11 | acotó el barrido | **FUERA DE MI LOTE** (`P`) | **FUERA DE MI LOTE** |
| 7 | `P-07` | el bloque `E5` cubría `E5-3` con un argumento de otra clase | `PN-16` | **FUERA DE MI LOTE** (`P`) | **FUERA DE MI LOTE** |
| 8 | `P-08` | «FUENTES SIN ASIGNAR 0» sobre un universo ELEGIDO | publicó `derivar-universo-obligatorio.py` en commit propio y anterior | **EJECUTADO POR MÍ**: da **59 fuentes · 41 174 líneas**, con los cinco componentes de `1bis` leídos de su sede normativa. Y crucé universo contra asignación: `comm -23` → **vacío**; `comm -13` → **vacío** | **SUPERADO** |
| 9 | `Q-01` | `G-11b` no fallaba cerrado sin Git | añadió el guarda | **REPRODUCIDO**: sin `.git` → 25/30 y `G-11b` en **FALLO**. Residuo: la rama de base vacía es código muerto (`Q-22`) | **SUPERADO** |
| 10 | `Q-02` | el ancla se comparaba en CRUDO | normaliza a la capacidad base | **REPRODUCIDO**: `"VER:dosier"` en `INC` ya **no** mueve el ancla (`anclas sin VER ['AUD','INV']`). `obl_base = [_base(v) for v in obl]` | **SUPERADO** |
| 11 | `Q-03` | sólo se contrastaba el TOTAL, no el reparto | `G-15` contrasta vía a vía | **REPRODUCIDO**: vías desnudas en `FEA` → **FALLO G-15**, «vía 3: publica 0 y deriva 2; vía 4: publica 8 y deriva 6» | **SUPERADO** |
| 12 | `Q-04` | `01-PROCESOS-BIS` + `C8` bajo `kernel/` daban 30/30 | `G-23` compara el CONJUNTO del kernel | **REPRODUCIDO en las dos direcciones**: dentro de `kernel/` → 29/30, `G-23` lo caza. **FUERA de `kernel/` → 30/30 EN VERDE** con material normativo duplicado y un `C8` que declara contradecir a `C4` y `C7` | **NO SUPERADO** (`Q-02`) |
| 13 | `Q-05` | el troceado leía la prosa de los escalares | lector estructurado por escalares e indentación | **REPRODUCIDO a medias**: el escalar `>` se caza y **NOMBRA el campo**, exactamente como promete. La **indentación NO se aplica**: un campo anidado bajo una clave inventada se deriva como obligatoria y desplaza el ancla | **SUPERADO para escalares · NO SUPERADO para indentación** (`Q-09`) |
| 14 | `Q-07` | §16 cerraba su rango en `PN-14` con `PN-15` viva | reancló el rango | L7920: «**`PN-6` a `PN-16`**», con su nota «**Corregido otra vez por `Q-07`**». `G-26` publica «14 presiones derivadas de §16» | **SUPERADO** en su sede · pero la cifra sigue caducada en TRES sedes vecinas (`Q-12`, `Q-13`) |
| 15 | `Q-09` | `_VIGILADAS` era un literal | `_derivar_vigiladas()` | El literal **desapareció** y el conjunto se deriva. **PERO** el discriminante es `re.search("participa dos veces", <fichero entero>)` sobre prosa libre, y el fixture que lo respalda es una **tautología** | **SUPERADO en la letra, INSUFICIENTE en el fondo** (`Q-10`) |
| 16 | `Q-10` | `_exige_item` no conservaba la sección de origen | conserva `(cap, via, seccion)` | Verificado en `_analizar`: la tupla lleva `seccion` y `_exige_item` decide por ella | **SUPERADO** |
| 17 | `Q-11` | la sede atribuía `conclusion-fundada` a `INV` | separó los dos anclas | doc 11 L9010–9016: «`AUD` → `conclusion-fundada`», «`INV` → `evidencia-producida`», con la nota de corrección | **SUPERADO** |
| 18 | `Q-12` | «cinco fixtures» junto a SEIS grupos | deriva la cifra: «17 fixtures» | doc 11 L9162–9165 y salida real: «17 fixtures ejecutados». **Reserva**: uno de esos 17 no puede fallar (`Q-10`) | **SUPERADO en la cifra, con reserva** |
| 19 | `Q-14` | `C-L.3` CERRADA por `D103` y NO CERRADA a la vez, sin `D104` | marcó el bloque anterior HISTÓRICO y acotó `G-16` al vigente | Verificado: L1183–1184 **`[HISTÓRICO · el estado que dejó la tanda de D96–D103…]`**; el bloque vigente (L1269) dice «`C-L.3` CERRADA · **por D104, y NO por D103**, que M-01 refutó» | **SUPERADO** |
| 20 | `Q-15` | `ancho` muerto y errata «toda todo» | retiró los dos | `grep -n ' ancho ='` → sin resultados; `grep -n 'toda todo'` → sin resultados | **SUPERADO** |
| 21 | `R-01` | tres sedes justificaban `W17` «por contenido» | retiró la justificación | **FUERA DE MI LOTE** (`P`) | **FUERA DE MI LOTE** |
| 22 | `R-02` | `M-06` reproducido en la sede de entrada (TRES ficheros donde son SEIS) | remite en vez de copiar | `Q1` derivó `git diff --name-only 05f71b7..HEAD -- kernel/` → **6**, exactamente los declarados, 3 directos + 3 de evidencia; la sección de entrada **no contiene ni una ruta de `kernel/`**. `G-23` lo contrasta. Yo verifiqué la salida de `G-23`: «6 ficheros de kernel = 3 directos + 3 de evidencia derivada, todos enumerados en el checkpoint» | **SUPERADO** |
| 23 | `R-03` | §2.6.9 invocaba «la capa B» para una regla que su lista no escribía | remisión corregida | **FUERA DE MI LOTE** (`P`) | **FUERA DE MI LOTE** |
| 24 | `R-04` | `W17` se atribuía una sub-ventana que su condición excluye | corrigió la fila | **FUERA DE MI LOTE** (`P`) | **FUERA DE MI LOTE** |

```text
RECUENTO DERIVADO DE LAS FILAS DE ARRIBA, no copiado

  SUPERADO                     11   P-01 · P-08 · Q-01 · Q-02 · Q-03 · Q-07 · Q-10 · Q-11
                                    Q-14 · Q-15 · R-02
  SUPERADO CON RESERVA          3   P-05≡Q-08 (el texto sí, la comprobación no) ·
                                    Q-09 (letra sí, fondo no) · Q-12 (cifra sí, fixture no)
  NO SUPERADO                   2   Q-04 (sólo bajo kernel/) · Q-05 (sólo escalares)
  FUERA DE MI LOTE              8   P-02≡Q-06 · P-03 · P-04 · P-06 · P-07 · R-01 · R-03 · R-04
                               ──
                               24   los veinticuatro ids, cada uno EXACTAMENTE UNA VEZ

Y APARTE, como en el gate anterior:
  `M-04`                    FALLIDA, y MÁS ANCHA que cuando `R` la declaró FALLIDA. §3.
```

**Ninguno de los 24 se declara SUPERADO en el corpus**, y eso lo verifiqué: las 24 filas de la
matriz del checkpoint cierran en `**APLICADA, NO CERTIFICADA**`, sin una sola excepción. Es
correcto y es honesto: **quien aplica no certifica.** Los 11 «SUPERADO» de arriba son **mi**
adjudicación, no la suya.

---

## 7 · `C-L.5` Y LA COBERTURA DE ESTE GATE

### 7.1 · ¿Sostiene el documento 21 manifiestos de lectura POR RUTA? — **SÍ. Cierro `Q3-02`.**

`Q3` no pudo cerrarlo porque el documento 21 no era suyo. **Lo cierro yo, y con la evidencia
delante.** El documento 21 publica **tres** manifiestos de lectura por ruta:

- **§5 · `P`** (L378–L401): 20 filas con **ruta · líneas · SHA-256 COMPLETO de 64 hex ·
  `LEÍDO ÍNTEGRO` · primera y última sección sustantiva · dos anclas con su línea**, más una
  §3.3 explícita: «**Tramos NO abiertos: Ninguno.**»
- **§6 · `Q`** (L971–L1126): 31 filas, con SHA-256 **truncado a 16 hex** y ancla A / ancla B.
- **§7 · `R`** (L1899–L1920): 9 filas, SHA-256 truncado a 16 hex, dos anclas por fuente.

Las **doce** filas que el manifiesto de este gate cita como agotadas apuntan a filas reales:
verifiqué L380, L381, L382, L383, L395, L396, L399, L400, L401, L1056, L1057 y L1058 **una a
una**, y las doce son filas de manifiesto de lectura con `LEÍDO ÍNTEGRO` y su ruta.

**Y verifiqué la regla 2 —identidad de bytes— por mi cuenta, los doce:**

```text
8243034f…d185 1257  16-GATE-FINAL-INDEPENDIENTE-F4C.md          ✓
18f876d4…6c29c 1650  17-COMPLEMENTO-DE-COBERTURA…md              ✓
1e71366b…d496 3665  18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md      ✓
a8860916…d159 2163  ADS-PENDIENTES…md                           ✓
18dae195…d4da  211  a-ENMIENDA-E1-ENC.md                        ✓
9d5a2380…d2eb  230  a-ENMIENDA-E2-MULTIREPO.md                  ✓
3ee58ca4…1510  539  C2-AGENTES-Y-MODELOS.md                     ✓
d56bf6b8…4234  150  C3-METODO-EJECUTABLE.md                     ✓
67028918…ee81  170  C4-MATERIALIZACION.md                       ✓
315b2790…ddb1   28  entrada/00-INDICE.md                        ✓
750d39a2…9c70  145  entrada/02-CIRCUITO.md                      ✓
1716bd3d…0cd2  187  entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md   ✓

DOCE de DOCE coinciden en líneas Y en SHA-256 con el manifiesto. Cero discrepancias.
```

**Las DOCE agotadas se sostienen.** Cumplen la regla 1 (cita de gate y línea, con `LEÍDO
ÍNTEGRO` de esa ruta) y la regla 2 (bytes idénticos). **La única objeción que traigo es `Q-29`,
y es MENOR**: tres de las doce están citadas de la tabla de `Q`, que publica sólo 16 de los 64
hexadecimales, y el ADDENDUM las describe como si publicaran «su SHA-256». La comprobación de
identidad real la hago yo contra el árbol y sale bien; lo inexacto es la descripción.

### 7.2 · `Q3-02` y el `ADDENDUM 1`

`Q3-02` **es correcto y lo confirmé**: doc 20 §4–§5 (L152–533) contiene **cero** cadenas de 64
hexadecimales y **cero** apariciones de `LEÍDO ÍNTEGRO`, contra su propia L127–129 («Están
transcritos íntegros en §4 y §5»); y `O` escribe **NO CERTIFICABLE POR MÍ** (L651), **«`C-L.5`
queda ABIERTA en forma»** (L656) y, en la última línea del documento, **«`C-L.5` sigue
pendiente»**. Apoyar 21 agotamientos por ruta en ese apartado no se sostiene.

**Y aquí ocurre lo mejor de este gate, y lo digo aunque no me favorezca como acusador.** El
coordinador **no lo tapó**. Publicó `F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md`, en un
commit propio y solo (`706c787`, 1 fichero, 119 inserciones, verificado con `git log` y
`git diff --name-only`), que:

- **no edita** el manifiesto anterior —lo deja «con su error dentro, que es como debe quedar»—;
- **nombra al relevo que lo encontró** y transcribe su hallazgo;
- **devuelve las 21 fuentes al reparto de LECTURA** en este mismo gate;
- **crea `Q5` DESPUÉS de commitear el addendum y no antes**, y lo dice para que se compruebe con
  `git log` (comprobado: `706c787` es HEAD y el addendum es su único fichero);
- y declara expresamente: «**NO CORRIGE el hallazgo `Q3-02`: lo REGISTRA** … incluido su juicio
  sobre si el coordinador de este gate —que es quien escribió el manifiesto defectuoso— ha
  reaccionado bien o ha tapado».

**Mi juicio sobre eso, que se me pide expresamente: ha reaccionado bien.** Es la conducta que
`C-L.5`·`1bis` prescribe, ejecutada en el plazo más corto posible y contra el propio interés de
quien la ejecuta. `Q5` leyó las 21 íntegras y publicó su manifiesto con SHA-256 recalculados,
que yo he vuelto a recalcular.

### 7.3 · ¿Está la cobertura de ESTE gate cerrada?

**En lo que toca a `Q`, SÍ, y con margen.** Lo derivé mecánicamente, no lo presumo:

```text
UNIVERSO OBLIGATORIO, ejecutado por mí:
  $ python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py
    59 fuentes obligatorias · 41174 líneas
      (i) 4 · (ii) 29 · (iii) 3 · (iv) 11 · (v) 22

CRUCE UNIVERSO ↔ ASIGNACIÓN (manifiesto §4 + §5), hecho por mí con `comm`:
    OBLIGATORIO menos ASIGNADO   →  (vacío)
    ASIGNADO menos OBLIGATORIO   →  (vacío)

REPARTO, con el ADDENDUM 1 aplicado:
    ASIGNADAS A LECTURA   47   (26 + 21)
    AGOTADAS              12   (las doce verificadas arriba)
    TOTAL                 59   ✓

RESTA DE `Q`:   37 asignadas − 37 leídas íntegras  =  ∅
```

**`P-08` está genuinamente cerrado**, y es el logro más sólido de esta tanda: el universo ya no
se elige, se **deriva**, con un derivador publicado en commit propio y anterior al manifiesto,
que lee cada componente de su sede normativa y **falla cerrado con código 2**. «FUENTES SIN
ASIGNAR 0» ha dejado de ser verdadero por construcción: lo comprobé yo con `comm`, y sale vacío
en las dos direcciones.

**Lo que NO puedo cerrar, y no lo cierro.** La resta de `P` no la calculo yo. Si el manifiesto
de lectura de `P` deja una sola fuente asignada sin leer, la regla de cierre se dispara con
independencia de todo lo anterior. **Eso lo cruza `R`, no yo.**

### 7.4 · La contaminación de `Q5`, pesada

`Q5` declara que dos `grep -rn` sobre el repositorio entero le devolvieron **siete líneas del
documento 21** (L1073, 1118, 1125, 1132, 1568, 1570, 2114). **Las abrí las siete.** Son:
`_VIGILADAS = ("DOM","SEG")` como ancla de la tabla de `Q`; las filas de `DOM` y `SEG` de la
tabla de las quince fichas; y cuatro líneas sobre el hallazgo `Q-09`.

**Mi peso, sin suavizarlo y sin inflarlo:**
- La contaminación es **real, declarada por el propio relevo, y estrecha**: le reveló que existía
  un hallazgo previo `Q-09` con severidad MENOR sobre el literal `_VIGILADAS`.
- **No toca siete de sus ocho hallazgos**: `Q5-01`…`Q5-04`, `Q5-06`…`Q5-08` viven en
  `kernel/operativo/diseno/` y en las fichas, y ninguna de esas siete líneas los roza.
- **No invalida el octavo.** `Q5-05` no es `Q-09`: `Q-09` acusaba el literal, que hoy no existe;
  `Q5-05` acusa la **tautología de la comprobación que lo sustituyó**. Y ese punto **lo he
  verificado yo por lectura directa del código, sin pasar por `Q5`**: `_VIGILADAS =
  _derivar_vigiladas()` es, línea por línea, la misma comprensión de conjunto que la condición
  de L748–753 compara contra ella. La condición no puede ser verdadera nunca.
- **No afecta a la cobertura**: `Q5` recalculó los 21 SHA-256 y yo los volví a recalcular.

**Conclusión: la contaminación no invalida ninguna de las 21 lecturas ni ninguno de los ocho
hallazgos, y el descuento que merece ya está aplicado** —`Q-10` lo sostengo sobre mi lectura del
código, no sobre la de `Q5`—. Lo que sí acredita es que el relevo la declaró en vez de callarla,
que es lo que separa un manifiesto de una declaración.

---

## 8 · REFUTACIONES QUE INTENTÉ Y NO CAYERON

Las publico porque un dictamen que sólo enseña lo que confirma no mide nada.

**R1 · Intenté demostrar que el documento 21 NO publica manifiestos de lectura por ruta, y que
las doce agotadas se apoyan en aire.**
Método: barrido de las doce líneas citadas por el manifiesto, una a una, y recálculo de los doce
SHA-256 contra el árbol de hoy.
Resultado: **NO CAYÓ, y en los dos frentes.** Las doce filas existen, dicen `LEÍDO ÍNTEGRO`, y
las doce coinciden byte a byte. La única grieta es de descripción, no de sustancia (`Q-29`).
Esta refutación fallida es el resultado más importante de mi §7: **el defecto de cobertura era
de `N` en el documento 20, y no del método de agotamiento.**

**R2 · Intenté demostrar que «obligatorio − asignado = 0» sigue siendo verdadero por
construcción, es decir, que `P-08` no está cerrado.**
Método: ejecuté el derivador, volqué sus 59 rutas, extraje mecánicamente las rutas de §4 y §5 del
manifiesto y las crucé con `comm` en las dos direcciones.
Resultado: **NO CAYÓ.** `comm -23` vacío y `comm -13` vacío: 59 contra 59, sin residuo. El
universo se deriva de cinco sedes normativas, el derivador se publicó en commit propio y
anterior, y falla cerrado con código 2. **`P-08` está cerrado de verdad, y era GRAVE para `P`.**

**R3 · Intenté demostrar que la tanda no cerró ninguna de las tres vías concretas —`Q-01`,
`Q-02`, `Q-05`— y que sólo movió texto.**
Método: tres controles positivos propios sobre la copia: batería sin `.git`; `capacidad_productora:
"VER:dosier"` en `proceso:INC`; `capacidad_productora: "DOM"` inyectada en un escalar `>`.
Resultado: **NO CAYÓ NINGUNA DE LAS TRES.** Sin `.git` → 25/30 y `G-11b` en rojo. El
`"VER:dosier"` **ya no mueve el ancla**. La prosa del escalar se caza **y nombra el campo
contenedor**, que es exactamente lo que la corrección prometía y lo que la formulación anterior
no hacía. Las tres correcciones son reales y mecánicas, no prosa.

**R4 · Intenté demostrar que el recuento interno de los quince hallazgos de `Q` en el documento
21 es incoherente y que nadie lo vio.**
Método: el bloque de L1712–1720 publica «MEDIO 8 … → son NUEVE» y «MENOR 7 … → son SEIS», que no
cuadra.
Resultado: **NO CAYÓ.** Dos líneas más abajo, L1722–1725, el propio dictamen escribe:
«Rectifico el recuento en el propio dictamen, derivándolo otra vez de las filas y no de mi
borrador: **MEDIO 9 · MENOR 6 · total 15**». Está corregido en sede, a la vista, y contra el
interés de quien escribe. Retiro la sospecha.

**R5 · Intenté demostrar que `Q-14` sigue vivo: que `C-L.3` sigue figurando CERRADA y NO CERRADA
a la vez en el registro reanudable.**
Método: `grep -n 'C-L\.3'` sobre el checkpoint (10 apariciones) y lectura del contexto de las dos
clasificaciones.
Resultado: **NO CAYÓ.** El bloque antiguo lleva hoy `**[HISTÓRICO · el estado que dejó la tanda
de D96–D103. La clasificación VIGENTE está más abajo…]**` (L1183–1184) y el bloque vigente
(L1269 en adelante) dice «`C-L.3` CERRADA · **por D104, y NO por D103**, que M-01 refutó», con
las cuatro combinaciones. La corrección llegó, y llegó bien.

**R6 · Intenté demostrar que la excepción del kernel oculta ficheros o está escrita a mano.**
Método: leí la salida real de `G-23` y contrasté contra el conjunto derivado de Git.
Resultado: **NO CAYÓ.** `G-23` publica «6 ficheros de kernel = 3 directos + 3 de evidencia
derivada, todos enumerados en el checkpoint», derivado de `git ls-tree`/`os.walk`, y la sección
de entrada **remite en vez de copiar**. `R-02` está genuinamente cerrado. *(Lo que sí cae, y por
otra puerta, es el CONTENIDO de esas tres rutas: `Q-05`.)*

---

## 9 · LO QUE NO HE CUBIERTO, SIN ADORNO

1. **NO he leído ni una fuente del lote de `P`**: ni el documento 11 (9 494 líneas), ni
   `DECISIONES-Y-CONTRADICCIONES.md`, ni `(a)`, ni `(b)`, ni `KERNEL.md`, ni los siete contratos.
   Todo lo que digo sobre `D105`, las ventanas, `fsync`, `PN-15`/`PN-16` y `D97` **es nada**: no
   lo digo. Donde toqué el documento 11 fue por región dirigida y para mutarlo en el
   laboratorio, y **eso no es lectura**.
2. **Los siete árboles defectuosos que construí son míos, y no son exhaustivos.** Que la batería
   caiga por seis puertas no significa que sólo haya seis. No he auditado `G-02`…`G-10`, `G-12`,
   `G-14`, `G-17`, `G-19`, `G-25` ni `G-27` con contraejemplos propios.
3. **No he ejecutado nada del sistema**, porque no hay sistema: ni runtime, ni esquema de
   `evento`, ni un fichero bajo `estado/`. Todo mi juicio es texto contra texto y código contra
   árbol. **No cuento esa ausencia como insuficiencia**: está declarada con propietario y fase, y
   lo verifiqué.
4. **No he leído el contenido de los 107 ficheros de rol, método y prompt** de las quince
   capacidades, ni `diseno/03-ESCALA-DE-NOVEDAD.md` línea a línea. `Q5` los cruzó por existencia
   y por nombre; eso no es lectura, y él lo dice.
5. **No he verificado las 43 filas del manifiesto de `18cbfb5`** que `R` recalculó, ni las cifras
   `R1` 28/30 · `R2` 29/30 · `R3` 29/30 · `R4` 26/30 del gate anterior. Las transcribo.
6. **No he recalculado la resta de `P`.** Si `P` deja una fuente asignada sin leer, la regla de
   cierre se dispara y mi §7.3 no lo impide. Es de `R`.
7. **La atribución de `Q-08` no la resuelvo**: si el 12/13 se imputa al corpus o al procedimiento
   del gate que commiteó los manifiestos es una decisión de criterio, y la dejo a `R` con el
   hecho medido y el mecanismo exacto delante.
8. **Mi severidad es discutible; mis hechos no.** Los cuarenta y dos están abiertos en su fichero
   y su línea, o reproducidos con su salida pegada. Si `R` rebajase mis ocho GRAVES a MEDIOS, mi
   recomendación **no cambiaría**: las razones 1 y 2 de §10 se sostienen por sí solas.

---

## 10 · MI RECOMENDACIÓN DE VEREDICTO, Y SUS RAZONES

La cobertura de `Q` está cerrada —`ASIGNADAS − LEÍDAS ÍNTEGRAS = ∅`, 37 de 37, con los 37
SHA-256 recalculados por mí— y por tanto **NO procede** `INSUFICIENTE PARA F5 POR COBERTURA`.
Mi recomendación se emite **sobre el fondo**.

# INSUFICIENTE PARA F5

**Cuatro razones numeradas. Las dos primeras bastan cada una por sí sola.**

1. **`M-04` no sólo sigue viva: es MÁS ANCHA que cuando `R` la declaró FALLIDA, y dos de los
   contraejemplos son hallazgos ya adjudicados meramente desplazados.** `R` dejó escrito que
   fuera de `R1`–`R4` había **tres** falsos verdes. Yo he construido y ejecutado **seis**, sobre
   mi propia copia, y he pegado la salida de los seis. Dos son demoledores por lo que son y no
   por cuántos son: **`Q-04` reinstala el ÚNICO GRAVE del gate anterior —la cifra falsa hacia el
   Owner en el punto de entrada— añadiendo dos palabras a la línea**, y **`Q-02` reinstala el
   `Q-04` original moviéndolo un directorio**. La condición 7 del gate anterior («la batería no
   ofrece falsos verdes») se declaró cumplida sobre cuatro fixtures nombrados; medida sobre la
   proposición, que es como `M-04` está enunciada, **no se cumple**.

2. **La condición 3 —`D104` supera el intento adversarial— tampoco se cumple, y por la misma
   junta que la vez anterior.** El contrato de `D104` promete por escrito que una segunda
   proyección en el bloque «es el contraejemplo de `M-04`, y **la comprobación la suspende**».
   **No la suspende** (`Q-03`, reproducido con control literal). Y el pilar del lector
   estructurado se cerró **sólo para escalares de bloque**: la indentación que su propia
   docstring promete no se aplica, y un campo anidado bajo una clave inventada se deriva como
   participación obligatoria y **además desplaza el ancla** (`Q-09`, reproducido con fixture
   propio). Son dos garantías publicadas que no se sostienen.

3. **El patrón de método se repite con precisión mecánica, y es la razón por la que estas
   revisiones se encadenan.** Cada corrección se aplicó **al perímetro exacto del contraejemplo
   que la motivó** y no al principio que lo explica, y lo demuestro con el control de cada
   experimento: `Q-04` cerrada bajo `kernel/` → funciona fuera; la unicidad cerrada contra la
   copia literal → funciona reformulando; `G-26` cerrada contra el numeral → funciona con la
   palabra «regresión»; `G-01` cerrada contra el texto histórico → funciona derogándolo con la
   palabra «RETIRADA»; la excepción del kernel cerrada por ruta → funciona vaciando el fichero.
   `R` lo dijo con las palabras de `O`: «una decisión bien tomada llega a la mitad de los sitios
   que la invocan». **Esta vez la mitad que falta es la comprobación que existía para impedirlo.**

4. **Y quedan contradicciones materiales vigentes sin registrar —condición 6—, en la misma clase
   y con más sedes que la vez anterior.** Trece MEDIOS, de los cuales cuatro son la enésima
   recurrencia del censo de presiones (`Q-12` dos veces, `Q-13`, `Q-17`), uno bajo el rótulo
   explícito «**CIFRAS VIGENTES, DERIVADAS**» que `L-01` creó precisamente para separar lo
   caducado de lo vigente, y uno —`Q-14`— declarando en presente que «el gate independiente
   TODAVÍA NO SE HA INICIADO» cuando éste es el cuarto. **Y el árbol que se somete a
   certificación falla su propia comprobación canónica** (`Q-08`: 12/13, `git status` sucio, y
   una laguna estructural en `exclusiones.yaml` que romperá `T147` en todo gate futuro).

---

**Y lo que quiero que se lea junto a la recomendación, porque sería deshonesta sin ello:**

- **`D104` es correcta, y no lo digo de oídas.** `Q2` derivó `<CAP>:revision` a mano, antes de
  mirar lo publicado, y coincidió **punto por punto**: cinco procesos, nueve pares, reparto
  `{vía 2: 1, vía 4: 8}`, tres dinámicos, dos vigiladas, diez anclas. Yo ejecuté `G-15` y devuelve
  exactamente eso. Es el mejor trabajo de la tanda y no debe quedar sepultado.
- **Cinco de los seis defectos concretos del gate anterior en mi foco están genuinamente
  cerrados, y con mecanismo verificado por mí**: `Q-01` (falla cerrado sin Git), `Q-02` (ancla
  normalizada), `Q-03` (reparto por vía contrastado), `Q-05` para escalares (y **nombra el campo
  contenedor**, que es lo que prometía), `Q-10`, `Q-11`, `Q-12`, `Q-14`, `Q-15`, `R-02`.
- **`P-08` está cerrado de verdad**, y era GRAVE: el universo obligatorio **se deriva**, lo
  ejecuté, da 59 fuentes y 41 174 líneas, y el cruce contra la asignación sale **vacío en las dos
  direcciones**. Es la primera vez que ese cruce se puede hacer en vez de presumirse.
- **`C-L.5` se sostiene en lo que toca a `Q`**: 37 de 37 leídas íntegras, doce agotadas
  verificadas byte a byte por mí, y las doce con fila propia de manifiesto de lectura.
- **Y el `ADDENDUM 1` es lo mejor que he visto en este expediente.** Un relevo del propio gate
  encontró que 21 de las 33 fuentes agotadas violaban la regla 1 del manifiesto que las agotaba,
  y el coordinador **no lo tapó**: publicó un manifiesto nuevo, sin editar el anterior, nombrando
  al relevo, devolviendo las 21 al reparto, creando un relevo nuevo después del commit y no
  antes, y declarando por escrito que el hallazgo entra en el dictamen y lo adjudica `R`
  «incluido su juicio sobre si el coordinador … ha reaccionado bien o ha tapado». **Ha
  reaccionado bien.** Y las 21 quedaron leídas.

**Ninguno de mis cuarenta y dos hallazgos exige decidir arquitectura nueva.** Todos se cierran
propagando material que el corpus ya tiene escrito, o cambiando un patrón por otro. Con
`G-23` mirando el conjunto también fuera de `kernel/`, con la unicidad troceada por proyecciones,
con `_es_cita` evaluada sobre la ocurrencia, con `G-01` leyendo polaridad, con `G-16`
comparando por igualdad y no por prefijo, con la excepción del kernel fijada por contenido, con
un lector estructurado que aplique la indentación que promete, y con las cinco sedes del censo de
presiones reancladas, **esta candidata pasa**. Hoy no pasa.

> **Advertencia, y va en el sitio en que debe ir: yo RECOMIENDO. El veredicto lo emite el
> adjudicador `R`, que no soy yo.** No he visto el dictamen de `P` y no lo veré. Si `R` resuelve
> que un hallazgo se cierra cerrando sus instancias nombradas y no su proposición, `M-04` sería
> SUPERADO y mis `Q-02`…`Q-07` serían hallazgos nuevos — y mi recomendación **no cambiaría**,
> porque la razón 2 la determina por sí sola.

---

## 11 · CIERRE

```text
git status --porcelain   →   (salida vacía)          VERIFICADO al abrir y al cerrar
git rev-parse HEAD       →   706c787189c2241124d0df467f18eb5c5b60667b   (sin cambios)
RAMA                     →   gate/f4c-certificacion-20260830
SHA-256 del doc 21       →   9f869ffbdbdb834ca872c03abc8826c125a47b4344ed32cd9b6266db08f8be03

FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS   ninguno
COMMITS · PUSH · MERGE                                   ninguno
LABORATORIO   /tmp/lab-Q4 — limpio antes de borrarlo, y BORRADO con `rm -rf`
FICHEROS P1.md / P2.md / P3.md / DICTAMEN-P.md          NO ABIERTOS
SUBAGENTE `Agent`                                        NO USADO
NINGÚN HALLAZGO SE HA CORREGIDO, y es deliberado.
```

**`F4c` sigue ABIERTA por mi parte. `F5` NO queda autorizada por mi parte.**

**REVISOR `Q` · dictamen cerrado por `Q4`.**

---

# §C · ADJUDICACIÓN DEL ADJUDICADOR `R`, LITERAL

# ADJUDICACIÓN DEL ADJUDICADOR `R` — GATE INDEPENDIENTE DE CERTIFICACIÓN DE F4c

Repositorio `/home/jose/ads-kernel` · rama `gate/f4c-certificacion-20260830` · HEAD `706c787189c2241124d0df467f18eb5c5b60667b`.

---

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

Soy `R`, adjudicador único. **Emito el veredicto y no corrijo nada.**

**Qué NO soy.** No escribí F4, F4b ni F4c. No apliqué ninguna decisión `D16`–`D106`. No soy
autor de ninguna corrección de ninguna tanda. No fui revisor en ningún gate anterior. No había
visto ningún dictamen hasta abrir los dos que recibo, que llegaron **ya cerrados**: sus autores
no pueden modificarlos. No he usado el subagente `Agent`.

**Modo, comprobado en los dos extremos:**

```text
git status --porcelain  AL ABRIR    → SALIDA VACÍA      (primer comando de la sesión)
git status --porcelain  AL CERRAR   → SALIDA VACÍA      (último comando de la sesión)
HEAD al abrir y al cerrar           → 706c787189c2241124d0df467f18eb5c5b60667b, idéntico
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE         ninguno
```

**Y lo digo con esas palabras: el árbol está limpio al abrir y al cerrar.** Ejecuté la batería
y el runner del kernel; la batería no escribe, y el runner —que sí muta dos ficheros de
evidencia derivada— lo ejecuté **sobre una copia y nunca sobre el árbol**. Todos mis
experimentos viven en `/tmp/lab-R`, borrado al terminar. El único fichero que escribo es éste,
fuera del repositorio.

**Sobre el objeto juzgado.** El manifiesto reparte el commit candidato `4d231ee` / árbol
`02ba78c`. HEAD es `706c787`. Comprobé la diferencia yo:

```text
$ git diff --stat 4d231ee 706c787
 derivar-universo-obligatorio.py                | 289 +++
 F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md  | 119 +++
 F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md  | 316 +++
 3 files changed, 724 insertions(+), 0 deletions(-)
```

**Cero supresiones, y los tres ficheros son el aparato de este mismo gate.** El corpus juzgado
es byte a byte el del árbol repartido. **Lo hago constar porque tiene consecuencia**, y la
desarrollo en §6 y en §11.

**Una corrección de hecho al encargo, y consta.** El encargo dice que el `ADDENDUM 1` tiene
**120** líneas. Tiene **119** (`wc -l` = 119, y el propio `git show --stat` del commit dice
«119 insertions»). Es intrascendente y lo digo por disciplina: no acepto ninguna cifra sin
recalcularla, incluidas las de quien me encarga.

---

## 2 · MI PROPIO MANIFIESTO DE LECTURA

Cinco fuentes asignadas. **Cinco leídas ÍNTEGRAS.** SHA-256 recalculados por mí con `sha256sum`
sobre el árbol de HEAD, y recuentos con `wc -l`.

| # | ruta | líneas | SHA-256 recalculado por mí | cobertura | 1.ª y última sección sustantiva | ancla A | ancla B (región separada) |
|---|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | **LEÍDO ÍNTEGRO** | 1.ª `## 1 · Objeto del reparto` · última `## 8 · Regla de cierre, declarada por delante` | §3bis · «*ningún ojo único recorre sus 9 494 líneas seguidas … pero no se elimina, y el adjudicador tiene que pesarlo*» | §5 regla 2 · «*los BYTES de la candidata tienen que ser IDÉNTICOS a los del árbol que ese gate leyó*» |
| 2 | `docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | **119** | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | **LEÍDO ÍNTEGRO** | 1.ª `## 1 · El motivo, dicho sin suavizar` · última `## 5 · Lo que este addendum NO hace` | §1 · «*Veintiuna de esas treinta y tres no cumplen esa regla, y el manifiesto no lo vio*» | §5 · «*NO CORRIGE el hallazgo `Q3-02`: lo REGISTRA*» |
| 3 | `docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` | 2679 | `9f869ffbdbdb834ca872c03abc8826c125a47b4344ed32cd9b6266db08f8be03` | **LEÍDO ÍNTEGRO**, en seis tramos consecutivos `1–450 · 451–900 · 901–1360 · 1361–1820 · 1821–2260 · 2261–2679`. Unión = `[1, 2679]`. **Ningún tramo sin abrir** | 1.ª `## 1 · Identidad y procedencia` (L9) · última `## 14 · Ningún hallazgo se ha corregido, y es deliberado` (L2663) | **L2137** · `R-04` · «*la sub-ventana del marcador que `W17` nombra queda fuera de su propia condición de detección … el reparto de §2.6.9 punto 7, que lo asigna a `W8`*» | **L2029** · «*El documento se apoya en una prueba que él mismo retiró … Sobra una frase; no falta una decisión*» |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 2382 | `3b6e1f776cc0f89e3068ee3ff9a89c88f6436b68114c3e77d637402d31cef613` | **LEÍDO ÍNTEGRO**, en cinco tramos `1–480 · 481–960 · 961–1410 · 1411–2179 · 2180–2382`. Unión = `[1, 2382]` | 1.ª la cabecera de estado (L3) · última `## Siguiente acción exacta` (L2293–2382) | **L6** · «*Basta decir «Continúa»: la siguiente acción exacta está al final*» | **L2270** · fila 24 de la matriz, `R-04` · «*el reparto estaba bien en el punto 7 de §2.6.9 y mal en la fila*» |
| 5 | `docs/evolucion/00-INDICE.md` | 113 | `56d1cdb133108c77f87fe70d096ca2547c04cc733fe84694846b72a5cc873307` | **LEÍDO ÍNTEGRO** | 1.ª `## Los documentos en voz del Owner` (L14) · última `## Lo que este trabajo ha corregido de sí mismo` (L106) | **L58** · «*entregada y CORREGIDA DOCE VECES … y **DOCE** presiones normativas vigentes*» | **L83** · «*las vigentes derivadas pasan a **CATORCE***» |

**Las dos anclas de la fila 5 son, ellas solas, un hallazgo**: están en la misma tabla del mismo
fichero y se contradicen. Lo adjudico en §6.

**Además abrí como OBJETO —nunca como fuente de juicio propio— y en la extensión que cada
verificación exigió:** `11-ARQUITECTURA-INTEGRADA.md` (§0, §2.6.4, §2.6.5, §2.6.6, §2.6.7,
§2.6.9, §2.8, §3.6, §8.x, §9.1, §9.2, §15.8, §16, §17, §19 y `C-L.5`), la batería
`comprobar-correccion-gate-de-cierre.py`, `derivar-universo-obligatorio.py`,
`DECISIONES-Y-CONTRADICCIONES.md`, `b-RECORRIDO-APROBADA.md`, `a-CAPACIDADES-APROBADA.md`,
`01-PROCESOS.md`, `exclusiones.yaml`, los validadores del kernel y el árbol `7764cca` vía
`git show`. **Fuentes que necesité y no tenía asignadas: ninguna que no pudiera abrir como
objeto de reproducción. No pido ADDENDUM.**

**Y la reserva que declaro contra mi propio interés.** No he leído íntegro el universo
obligatorio: leí íntegras mis cinco, y me apoyo —**declarándolo**— en los manifiestos de lectura
de `P` y de `Q`, que no rehíce. Lo que sí rehice es su **aritmética** (§3) y las afirmaciones
materiales que sostienen conclusiones (§4, §5, §6, §7).

---

## 3 · COBERTURA RECALCULADA POR MÍ

### 3.1 · El universo obligatorio: ejecutado, leído y atacado

**Lo ejecuté yo:**

```text
$ python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py
59 fuentes obligatorias · 41174 líneas
  (i  )   4   las CUATRO fuentes de «QUÉ HAY QUE LEER ÍNTEGRO» de `C-L.5`
  (ii )  29   las CATORCE fuentes y las QUINCE fichas de `C-0.1` / `C-0.2`
  (iii)   3   documento 11 · registro de decisiones · checkpoint
  (iv )  11   todo dictamen de gate anterior
  (v  )  22   el objeto que ESTE gate juzga, según su encargo
exit 0
```

**Reejecutable: sí.** Da lo que el manifiesto dice, cifra a cifra.

**¿Deriva de verdad, o esconde una lista escrita a mano? Leí su código entero y lo ataqué en
`/tmp/lab-R`. Respuesta partida:**

```text
(i)   DERIVA de verdad. Parsea la sección `C-L.5` del documento 11 y exige EXACTAMENTE cuatro.
      ATAQUE: renombré «QUÉ HAY QUE LEER» en la sede → exit 2, «no aparece el bloque». FALLA CERRADO
(ii)  DERIVA del bloque `G-24` de la batería. ATAQUE: quité una de las catorce → exit 2,
      «`C-0.1` declara CATORCE fuentes; `G-24` enumera 13». FALLA CERRADO
(iii) LISTA de tres constantes. Sin guarda
(iv)  DERIVA por barrido del H1 de `docs/evolucion/NN-*.md`. Da 11, y los conté
(v)   ES UNA LISTA ESCRITA A MANO de 22 entradas — 37 % del universo — y el propio derivador
      lo dice: «está declarado y anotado en vez de inferido». SIN NINGUNA GUARDA
```

**Y encontré una vía por la que el universo ENCOGE EN SILENCIO, que es exactamente el defecto
que el derivador dice impedir.** Es hallazgo mío, `R-N2`:

```text
ATAQUE, dentro del bloque `fuentes` de G-24: sustituí `entrada/02-CIRCUITO.md` por una
SEGUNDA copia de `entrada/00-INDICE.md`. El recuento sigue siendo 14.
RESULTADO   exit 0 · «58 fuentes obligatorias · 41029 líneas» · 02-CIRCUITO DESAPARECE
CAUSA       `len(fichas) != 15 or len(set(fichas)) != 15`  ← CAPACIDADES sí comprueba unicidad
            `len(fuentes) != 14`                            ← `fuentes` NO la comprueba
```

Y `R-N3`: **borrar una entrada del `ENCARGO` da exit 0 y «58 fuentes obligatorias»**, sin una
palabra. La afirmación del docstring —«falla cerrado si un recuento derivado no coincide con el
que su sede declara»— **no cubre (iii) ni (v)**, y el «14» y el «15» son literales del propio
derivador, no leídos del documento 18 que los declara.

**Aun así, y lo digo con la misma fuerza: `P-08` del documento 21 está SUPERADO.** El universo
ha dejado de elegirse. Dos de sus cinco componentes derivan de sede normativa y fallan cerrado
bajo ataque; el comando es público, reejecutable y anterior al manifiesto en commit propio. Que
quede un residuo no borra que el «FUENTES SIN ASIGNAR 0» ya **no** es verdadero por
construcción: lo comprobé yo, y sale vacío en las dos direcciones.

### 3.2 · Primera resta · `OBLIGATORIO − ASIGNADO`

Método: parseé las rutas de §4 y §5 del manifiesto y de §2 del addendum, y las crucé contra la
salida de `--rutas`.

```text
UNIVERSO DERIVADO                 59
§4 · ASIGNADAS A LECTURA          26
§5 · ASIGNADAS COMO AGOTADAS      33
ADDENDUM §2 · REASIGNADAS         21     ⊆ §5  ✓ comprobado

ASIGNADO (§4 ∪ §5)                59
OBLIGATORIO − ASIGNADO            ∅      ← VACÍO
ASIGNADO − OBLIGATORIO            ∅      ← VACÍO, y también lo comprobé

TRAS EL ADDENDUM
  LECTURA                         47     (26 + 21)
  AGOTADAS                        12     (33 − 21)
  TOTAL                           59  ✓
```

### 3.3 · `wc -l` y `sha256sum` de las 59 filas, recalculados contra el árbol

Extraje mecánicamente las 80 filas con `ruta · líneas · SHA-256` del manifiesto y del addendum
—59 rutas distintas, algunas con fila en los dos— y recalculé las dos métricas contra el árbol:

```text
FILAS CON ruta+líneas+SHA-256      80
RUTAS DISTINTAS                    59
DISCREPANCIAS EN LÍNEAS O SHA-256   0
FICHEROS AUSENTES DEL ÁRBOL         0
```

### 3.4 · Segunda resta · `ASIGNADO A LECTURA − LEÍDO` — **la que excluye la suficiencia**

Método: extraje de `DICTAMEN-P.md` y `DICTAMEN-Q.md` toda ruta declarada `LEÍDO ÍNTEGRO` y la
crucé contra las 47 asignadas a lectura.

```text
ASIGNADAS A LECTURA                          47
P declara LEÍDO ÍNTEGRO                      11   (10 propias + el documento 21)
Q declara LEÍDO ÍNTEGRO                      37   (16 del manifiesto + 21 del ADDENDUM)
RUTAS DISTINTAS DECLARADAS LEÍDAS ÍNTEGRAS   47

ASIGNADO A LECTURA − LEÍDO   =  ∅      ← CONJUNTO VACÍO
LEÍDO fuera de lo asignado   =  ninguna
```

**Verifiqué además la asignación de cada revisor contra el manifiesto, no de palabra:** las
filas de §4 marcadas `P` o `P+…` son 11 (3, 9, 15–23); las marcadas `Q` o `Q+…` son 16, más las
21 del addendum = 37. **11 + 37 = 48, y una es el documento 21, común a los dos: 47 distintas.**
Coincide.

> **La regla de cierre de `C-L.5` NO se dispara. La resta la CALCULÉ, no la presumo, y da
> vacío. Este gate NO falla por cobertura, y `C-L.5` sigue CERTIFICADA.**

### 3.5 · El agotamiento de las DOCE, ruta a ruta

Regla 1 —fila propia con `LEÍDO ÍNTEGRO` de esa ruta en el documento 21, con su línea— y regla
2 —bytes idénticos a los del árbol `7764cca`—, comprobadas **las dos, una a una, por mí**:

| # | ruta | línea del doc 21 | regla 1 | `git show 7764cca:<ruta> \| sha256sum` vs árbol |
|---|---|---|---|---|
| 1 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | L380 | ✓ `LEÍDO ÍNTEGRO` | **IDÉNTICO** |
| 2 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | L381 | ✓ | **IDÉNTICO** |
| 3 | `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | L382 | ✓ | **IDÉNTICO** |
| 4 | `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` | L383 | ✓ | **IDÉNTICO** |
| 5 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | L395 | ✓ | **IDÉNTICO** |
| 6 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | L396 | ✓ | **IDÉNTICO** |
| 7 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | L399 | ✓ | **IDÉNTICO** |
| 8 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | L400 | ✓ | **IDÉNTICO** |
| 9 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | L401 | ✓ | **IDÉNTICO** |
| 10 | `kernel/operativo/entrada/00-INDICE.md` | L1056 | ✓ | **IDÉNTICO** |
| 11 | `kernel/operativo/entrada/02-CIRCUITO.md` | L1057 | ✓ | **IDÉNTICO** |
| 12 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | L1058 | ✓ | **IDÉNTICO** |

**Las DOCE se agotan. Ninguna falla ninguna de las dos reglas.** Las líneas citadas por el
manifiesto son exactas: las abrí las doce.

**La objeción de `Q-29` es correcta y es MENOR.** Las tres filas de `entrada/` (L1056–1058)
proceden de la tabla de `Q` del gate anterior, que publica **16** de los 64 hexadecimales, y el
`ADDENDUM 1` las describe como si publicaran «su SHA-256». **Lo inexacto es la descripción del
addendum, no el agotamiento**: la identidad de bytes la comprobé yo contra el árbol con los 64.

---

## 4 · LAS DISCREPANCIAS ENTRE `P` Y `Q`, RESUELTAS CONTRA LA FUENTE

**No resuelvo ninguna por mayoría.** Las dos cadenas trabajaron sobre lotes complementarios y
la mayor parte de sus «discrepancias» son en realidad **abstenciones declaradas** —cada uno
escribe «FUERA DE MI LOTE» donde no tenía la fuente—, que es la conducta correcta. Las
discrepancias materiales reales son seis.

### `D-1` · `R-04`: `P` dice **NO SUPERADO Y AGRAVADO**; `Q` se abstiene por lote

> **RESUELVO A FAVOR DE `P`, y es la resolución más consecuente de esta adjudicación.**

Abrí las tres sedes y comparé contra `7764cca`:

```text
$ git show 7764cca:…/11-ARQUITECTURA-INTEGRADA.md | grep -A4 '^7 CÓMO RECUPERA EL'
7 CÓMO RECUPERA EL  … caída entre 1 y 5 → **`W17`** … caída entre 5 y 6 → … `W8` …
$ grep -A4 '^7 CÓMO RECUPERA EL' …/11-ARQUITECTURA-INTEGRADA.md          (árbol de hoy, L1938)
7 CÓMO RECUPERA EL  … caída entre 1 y 5 → **`W17`** … caída entre 5 y 6 → … `W8` …
```

**El punto 7 es BYTE-IDÉNTICO en los dos árboles. No se tocó.** Lo que la tanda hizo fue
recortar el alcance de `W17` (L1172) y escribir en su lugar:

> «*la caída POSTERIOR al `deriva`, con su marcador aún sin retirar, la cubre `W8` … **y así lo
> reparte el punto 7 de §2.6.9** (`R-04`)*»

**El punto 7 no lo reparte así.** Los seis pasos del paso E (L1874–1889) son: 1 emitir
`abandonada` · 2 `fsync` · 3 emitir `deriva` · 4 `fsync` del `deriva` · 5 crear su marcador ·
6 retirar el marcador de transacción. El tramo `[4, 5)` —`deriva` durable, su marcador aún sin
crear— cae dentro de «entre 1 y 5», luego el punto 7 lo da a **`W17`**; y `W17` lo expulsa por
**dos** vías: por alcance («y **sólo** ese tramo») y por su condición de detección («sin ningún
`deriva` que lo referencie»), que es falsa ahí porque el `deriva` existe. **Y `W8` (L1162) dice
lo contrario que la fila de `W17`:** «*Si se cayó antes de eso, la ventana es `W17`*».

**Tres sedes, y la nueva es la que miente sobre las otras dos.** El adjudicador del gate
anterior escribió en `R-04` que el punto 7 «lo asigna a `W8`» — **eso era un error de hecho**, y
esta tanda lo copió en el texto normativo en lugar de corregir el reparto. **`R-04` NO está
superado: está AGRAVADO**, y donde antes había una imprecisión de alcance ahora hay una
contradicción entre tres sedes con una cita falsa que la sostiene.

### `D-2` · `Q-04` del documento 21: `Q` dice **NO SUPERADO**; `P` se abstiene por lote

> **RESUELVO A FAVOR DE `Q`, y lo reproduje yo.** Ver §7, experimento `A`.

### `D-3` · `Q-05` del documento 21: `Q` dice **SUPERADO para escalares, NO para indentación**

> **RESUELVO A FAVOR DE `Q`, y lo reproduje yo con fixture propio**, cargando `_campos` de la
> propia batería fuera del repositorio. Un `capacidad_productora: "DOM"` anidado dos niveles bajo
> una clave inventada (`notas_internas.comentario_libre`) **dentro de `obligatorias:`** se
> devuelve como campo con indentación 8 y `prosa_sospechosa` queda **vacía**. La docstring
> promete «*una línea sólo es campo si vive al nivel de sangría de su sección*»; la sangría se
> registra y **nunca se usa para rechazar**. La corrección cerró los escalares de bloque, no la
> indentación.

### `D-4` · `P-06` del documento 21: `P` dice **NO SUPERADO**; `Q` se abstiene por lote

> **RESUELVO A FAVOR DE `P`.** Ver §9, que es donde el encargo me obliga a pronunciarme
> expresamente.

### `D-5` · `Q-08` de `Q` —la batería del kernel da 12/13 y ensucia el árbol—: `Q` lo gradúa **GRAVE** y declara honestamente dos lecturas posibles sin resolverlas

> **RESUELVO, y a la baja.** Lo ejecuté sobre dos copias:

```text
sobre HEAD (706c787)     12/13 · falla `referencias` · git status NO vacío (2 evidencias)
sobre 4d231ee (CANDIDATO) 13/13 · 13 evidencias · 0 problemas · git status VACÍO
```

Y el diagnóstico de `T147` nombra **exactamente** los dos ficheros que este gate añadió:
`F4C-ASIGNACION-…` y `F4C-ADDENDUM-1-…`. **La rotura no es del corpus candidato: la introduce
el aparato de este gate.** Sobre el objeto juzgado las dos sedes dicen la verdad y el árbol
queda limpio.

**Lo que SÍ sobrevive, y lo confirmo como hallazgo del corpus:** `exclusiones.yaml` no contempla
`docs/evolucion/verificacion/manifiestos/`, y `C-L.5`·`1bis` **OBLIGA** a todo gate a publicar
su manifiesto ahí. **Todo gate futuro romperá `T147`, y por un fichero más cada vez.** El
manifiesto del gate anterior no la rompe **sólo porque el documento 21 lo enlaza** (L80), lo que
prueba a la vez el defecto y su remedio. Lo gradúo **MEDIO**, no GRAVE, y es clase A.

### `D-6` · `Q-14` del documento 21 (`C-L.3`): `Q` dice **SUPERADO**; `P` no puede adjudicarlo y **denuncia el reparto**

> **RESUELVO A FAVOR DE `Q` en el fondo, y A FAVOR DE `P` en la forma.** Verifiqué la sede: el
> bloque anterior lleva hoy `[HISTÓRICO · el estado que dejó la tanda de D96–D103…]` (L1183) y
> la clasificación vigente (L1269–1317) dice «`C-L.3` CERRADA · **por D104, y NO por D103**, que
> M-01 refutó», con las cuatro combinaciones y sin «cero o un par, nunca dos». **`Q-14`
> SUPERADO.**
> **Y la denuncia de `P` es correcta y la hago mía:** el manifiesto puso `C-L.3` en el foco de
> `P` y **no le dio ninguna de sus once sedes** —diez en el checkpoint y una en `00-INDICE`, las
> dos asignadas a `Q+R`—. Es un defecto del reparto de este gate, no de `P`. Lo registro en §11.

**No hay ninguna discrepancia material irresoluble entre `P` y `Q`.** Las seis se resuelven
abriendo la fuente. Y consta un dato del método: las dos cadenas convergieron de forma
independiente y sin verse en el §15.8 (`P-03` de `P` ≡ `Q-17` de `Q`), en el estado compuesto de
`C-L.5` (`P-22` ≡ `Q-37`) y en la rotura de `comprobar_referencias` (`P-27` ≡ `Q-08`).

---

## 5 · HALLAZGOS QUE RECHAZO, DE CUALQUIERA DE LOS DOS

**Rechazo tres, y rebajo cuatro.** Lo hago con la misma fuerza con la que confirmo.

**`X-1` · RECHAZO la severidad GRAVE de `Q-08` de `Q`** (la batería del kernel). Los hechos son
ciertos; la imputación no. **La rotura la causa este gate, no la candidata.** Sobre el objeto
juzgado el runner da 13/13 y deja el árbol limpio, y lo ejecuté. Lo que sobrevive es la laguna
de `exclusiones.yaml`, y la gradúo **MEDIO**. `Q` declaró las dos lecturas y no las resolvió;
resolverlas era mi trabajo, y lo he hecho.

**`X-2` · RECHAZO la severidad GRAVE de `P-08` de `P`** (`PN-16` y la grafía). El hecho es
exacto y lo verifiqué: `<CAP>:revisión` tiene **cero** instancias en `kernel/` con las dos
grafías, mientras `VER:decisión` tiene **12** apariciones en (b) —todas con tilde— y el kernel
construido lleva **3 con tilde y 14 sin tilde**. Pero `PN-16` **no promete** cubrir
`VER:decisión`: se acota a `<CAP>:revisión` y a (b) L836, y su resolución —registrar sin elegir—
es correcta. Lo que hay es una **contradicción viva no registrada**, que es la clase que este
expediente gradúa MEDIO. **MEDIO.**

**`X-3` · RECHAZO la severidad GRAVE de `P-05` de `P`** (la justificación de `D97`). Confirmo el
hecho entero (§9) y confirmo que es una **contradicción vigente**. Pero la resolución de `D97`
sobrevive intacta, la presión sigue en pie, y lo falso es una frase de evidencia que no cambia
ningún comportamiento. Por el criterio que los dos revisores declaran, eso es **MEDIO**.

**`X-4` · REBAJO `P-02` de `P` de GRAVE a MEDIO.** Es cierto que el punto 7 mete el tramo
`[1, 2)` en `W17` cuando ahí el `abandonada` puede no ser durable y el caso correcto es `W11`.
Pero **ese texto es idéntico al de `7764cca`**: no lo introdujo esta tanda, y es una imprecisión
de frontera en una enumeración, no una cita falsa sobre otra sede. Separado de `P-01`, es MEDIO.

**`X-5` · REBAJO `P-04` de `P` de GRAVE a MEDIO.** El titular «CATORCE» de §0 es **correcto** —lo
derivé: 16 cabeceras `## \`PN-` menos `PN-4` RETIRADA y `PN-5` FUSIONADA = 14— y lo roto es la
cadena que dice derivarlo, que termina en «trece» y omite `PN-16`. Es un recuento vivo falso sin
cambio de comportamiento: MEDIO. *(Y no lo perdono por editorial: el propio encargo excluye los
recuentos del perdón editorial.)*

**`X-6` · REBAJO cuatro de los ocho GRAVES de `Q` a MEDIO** —`Q-03` (la proyección), `Q-05` (la
excepción por ruta), `Q-06` (el prefijo de `G-16`) y `Q-07` (la palabra RETIRADA)—. Los cuatro
son ciertos y los reproduje. Los rebajo porque **son instancias de una misma proposición**,
`M-04`, que ya adjudico GRAVE con su umbrella (`Q-01`), y contarlos cuatro veces como GRAVE
infla el censo sin añadir información. **Mantengo GRAVE `Q-02`** —porque alcanza material
APROBADO— y **`Q-04`** —porque reinstala el único GRAVE del gate anterior con dos palabras—.

**`X-7` · RECHAZO, por innecesaria, la reserva de `Q` sobre la contaminación de `Q5`.** `Q5`
declaró que dos `grep -rn` le devolvieron siete líneas del documento 21. Abrí las siete: son el
literal `_VIGILADAS`, dos filas de tabla y cuatro líneas sobre `Q-09`. **No tocan siete de sus
ocho hallazgos**, y el octavo lo verifiqué yo por lectura directa del código sin pasar por `Q5`.
**La contaminación es real, estrecha, declarada por el propio relevo, y no invalida ninguna de
las 21 lecturas ni ninguno de los ocho hallazgos.** Que la declarara en vez de callarla es lo
que separa un manifiesto de una declaración, y consta a favor.

**`X-8` · Y una refutación MÍA que perdí, y la publico.** Intenté demostrar que la batería
tampoco ve el **vaciado** de una fuente obligatoria: dejé a cero bytes
`capacidades/DOM/CAPACIDAD.md` y `diseno/02-RUBRICAS.md`. **NO CAYÓ:** 27/30, con `G-15`, `G-23`
y `G-24` fallando los tres. `G-24` **sí** lee de verdad. Lo digo porque era mi apuesta y perdí.

---

## 6 · MIS PROPIOS HALLAZGOS

**`R-N1` · GRAVE · `G-22` sólo fija `docs/evolucion/1[5-8]-`: los documentos 19, 20 y 21 —los
tres veredictos de gate más recientes, incluido el que esta tanda existe para cerrar— no están
protegidos por ninguna comprobación, y volteé los tres a `SUFICIENTE PARA F5` con 30/30 EN
VERDE.**

Sede: batería **L1053**, `inmutables = [f for f in tocados if re.search(r"docs/evolucion/1[5-8]-", f)]`.

```text
ÁRBOL DEFECTUOSO   sustituí «INSUFICIENTE PARA F5» por «SUFICIENTE PARA F5» en los documentos
                   19 (6 golpes), 20 (4) y 21 (8), y «F4c NO se cierra … F5 NO queda
                   autorizada» por «F4c SE CIERRA. F5 QUEDA AUTORIZADA»
GIT LO VE           M docs/evolucion/19-… ·  M docs/evolucion/20-… ·  M docs/evolucion/21-…
DOC 21 L4           «> # SUFICIENTE PARA F5»
BATERÍA             30/30 comprobaciones en verde
```

Es **la refutación `R4` del gate anterior desplazada tres documentos**, y ahí sí la cazaba.
El corpus declara los documentos 15–21 inmutables en dos sedes que leí (`CHECKPOINT` L61,
`00-INDICE`), y **el mecanismo cubre cuatro de los siete**. `Q-26` de `Q` vio el patrón por
lectura de código y lo graduó MENOR sin reproducirlo; **yo lo reproduje y lo elevo a GRAVE**, y
le doy a `Q` el crédito de haberlo visto primero.

**Extensión, en el mismo árbol:** reescribí también el **manifiesto previo del gate anterior**
—`F4C-ASIGNACION-GATE-CIERRE-20260829.md`, declarado inmutable por `C-L.5`·`1bis` y por su
propia cabecera— cambiando «FUENTES OBLIGATORIAS 43» por «9» y «31 888 líneas» por «1 000»:
**30/30 en verde**, con `git status` mostrando el fichero modificado. **El instrumento sobre el
que descansa la certificación de `C-L.5` no está protegido por nada.**

**`R-N2` · MENOR · el derivador del universo obligatorio permite que el universo ENCOJA EN
SILENCIO, que es literalmente el defecto que su docstring dice impedir.** La guarda de
`CAPACIDADES` comprueba unicidad (`len(set(fichas)) != 15`); la de `fuentes` **sólo comprueba el
cardinal** (`len(fuentes) != 14`). Duplicando una entrada dentro del bloque `G-24`, el recuento
sigue siendo 14, el derivador sale con **código 0** y publica **«58 fuentes obligatorias»**
—`entrada/02-CIRCUITO.md` desaparece— sin un solo diagnóstico. Reproducido en `/tmp/lab-R`.

**`R-N3` · MENOR · la afirmación de fallo cerrado del derivador no cubre sus componentes (iii) y
(v), que son 25 de las 59 fuentes.** Borrar una entrada del `ENCARGO` da exit 0 y «58 fuentes
obligatorias», en silencio. Además, los cardinales «14» y «15» son **literales del propio
derivador**: no se leen del documento 18, que es la sede que los declara. La frase «*falla
cerrado si un recuento derivado no coincide con el que su sede declara*» es cierta de (i) y (ii)
y falsa de (iii) y (v). *(Lo digo a favor: el componente (v) es, por naturaleza, el encargo de
cada gate, y está anotado cláusula a cláusula. El defecto es la promesa, no la lista.)*

**Y una observación de método que no numero como hallazgo pero que el adjudicador siguiente debe
pesar:** el barrido del componente (iv) reconoce un dictamen por las voces
`GATE · CRÍTICA · REVISIÓN · DEVOLUCIÓN · COMPLEMENTO` en su H1. **`DICTAMEN`, `ADJUDICACIÓN` y
`CERTIFICACIÓN` no están en la lista.** Hoy no falta ninguno —lo comprobé documento a documento—,
pero la lista de voces tiene el mismo modo de fallo que la lista de rutas que el derivador
existe para sustituir.

---

## 7 · `M-04`: LO QUE REPRODUJE YO

**Método.** `cp -a` del repositorio a `/tmp/lab-R/base`, `.git` incluido, y una copia limpia por
experimento. **El repositorio no recibió una sola escritura.** Intérprete: Python 3.12.14 por el
shim. **Baseline sobre la copia limpia: 30/30 comprobaciones en verde.**

`Q` afirma haber reproducido **seis** árboles defectuosos en verde. **Reproduje los seis, no
dos**, y añadí dos míos.

| # | árbol defectuoso, construido y ejecutado por mí | resultado | control |
|---|---|---|---|
| **A** | `docs/rediseno/C8-SEGUNDA-SEDE.md` («CONTRADICE deliberadamente a `C4` y a `C7` … esta sede PREVALECE») + copias íntegras de `a-CAPACIDADES-APROBADA.md` y `DECISIONES-Y-CONTRADICCIONES.md` | **30/30 EN VERDE** | el **mismo** ataque dentro de `kernel/` → **29/30, `G-23` lo caza** |
| **B** | segunda proyección en el bloque de `D104`: «*el catálogo estático tiene **SEIS procesos y emite DIEZ pares***» | **30/30 EN VERDE** | la misma contradicción con la redacción literal «*SEIS procesos · DIEZ pares*» → **29/30, FALLA `G-15`** |
| **C** | `comprobar_negativos.py` reducido a `sys.exit(0)`, `negativos-salida.txt` falsificado, `.upstream-hash` sobrescrito | **30/30 EN VERDE** | — |
| **D** | fila de detalle **vigente** de `C-L.1`: «*CERRADA SOLO EN PARTE, SIGUE ABIERTA Y BLOQUEA F5 · D96 no cierra nada*» | **30/30 EN VERDE** | — |
| **E** | `CHECKPOINT` L2339, la línea que va al Owner: `CATORCE` → `ONCE` **más « (sin regresión)»** | **30/30 EN VERDE** | la misma cifra falsa **sin** esas dos palabras → **29/30, FALLA `G-26`** |
| **F** | párrafo en §16 que **deroga** la retirada de `estado/cuarentena/`: «*La nota que hablaba de una RETIRADA queda SIN EFECTO*» | **30/30 EN VERDE**, y `G-01` imprime `OK` | — |
| **G · MÍO** | los veredictos de los documentos **19, 20 y 21** volteados a `SUFICIENTE PARA F5` | **30/30 EN VERDE** | el mismo ataque sobre el doc 18 → lo caza `G-22` |
| **H · MÍO** | el **manifiesto previo del gate anterior**, declarado inmutable, con «43 fuentes» → «9» | **30/30 EN VERDE** | — |

**Las causas, leídas en el código y no supuestas:**

```text
E   `_BLOQUE_HISTORICO = re.compile(r"\[HISTÓRICO|\bHISTÓRICO\b|\bcaducad|\bregresión\b")`  L1347
    se evalúa sobre la LÍNEA ENTERA (L1351), al contrario que las otras dos ramas de `_es_cita`
B   `re.findall(r"([A-ZÁÉÍÓÚa-z]+) procesos . ([A-ZÁÉÍÓÚa-z]+) pares", …)`                   L555
    el `.` exige EXACTAMENTE UN carácter entre «procesos» y el numeral
D   `if not any(_det.startswith(a) for a in _admitidos)`                                     L881
A   la comparación de CONJUNTOS —la única que ve adiciones sin rastrear— existe SÓLO para `kernel/`
G   `re.search(r"docs/evolucion/1[5-8]-", f)`                                               L1053
```

> ## `M-04` SIGUE SIENDO FALLIDA, y es más ancha que cuando el gate anterior la declaró FALLIDA.
>
> **OCHO árboles defectuosos distintos, construidos y ejecutados por mí, pasan la batería 30/30
> en verde.** El gate anterior contó **tres** falsos verdes fuera de `R1`–`R4`. Hoy son ocho, y
> **cuatro de ellos reinstalan hallazgos ya adjudicados** —`Q-04` con un cambio de directorio,
> `P-05`≡`Q-08` con dos palabras, la refutación `R2` con dos palabras y la refutación `R4` con
> tres documentos de distancia—.
>
> **Y el hallazgo de método, que es lo que importa:** las cinco correcciones de la batería
> funcionan **en el perímetro exacto del contraejemplo que las motivó, y en ninguna otra
> parte.** Lo verifiqué en las dos direcciones para las cinco. Ése es el patrón que doce tandas
> llevan persiguiendo, aplicado esta vez al instrumento que existe para detectarlo.

**Y digo la mitad honesta, porque también la comprobé.** Las cinco vías nombradas **están
cerradas de verdad**, con control positivo mío:

```text
Q-01  sin .git → G-11b FALLA CERRADO           Q-02  «VER:dosier» ya NO mueve el ancla
Q-03  vías desnudas en FEA → FALLA G-15        Q-04  dentro de kernel/ → 29/30, G-23 lo caza
Q-05  escalar de bloque → FALLA G-15 y NOMBRA el campo que contiene la prosa
```

---

## 8 · LOS 24 DEL DOCUMENTO 21, ADJUDICADOS

**Un solo estado cada uno. Ninguno venía declarado SUPERADO por la tanda —lo verifiqué: las 24
filas de la matriz cierran en `APLICADA, NO CERTIFICADA` sin una excepción, y eso es honesto—.
Los estados de abajo son MÍOS.**

| # | id | qué encuentro yo en el árbol de hoy | estado |
|---|---|---|---|
| 1 | `P-01`≡`Q-13` | **L1488**: «*cada una de las **DIECIOCHO** ventanas … y **`W17`** … `W17` incluida expresamente*». Conté las filas `W`: 18. `grep` sobre las filas `X`: **1** menciona `W17` (antes 0). `G-26.e` deriva el censo | **SUPERADO** |
| 2 | `P-02`≡`Q-06` | «DECLARA SU» ya no está en la lista de la capa B: sólo en **L4391**, que es la anotación de corrección, y en L7210, ajeno. Las seis apariciones de `deriva_emitida` son prohibiciones | **SUPERADO** |
| 3 | `P-03` | tesis rechazada por el gate anterior; su residuo real vive en `R-01` | **SUPERADO** (por `R-01`) |
| 4 | `P-04` | **L1390-1399**: «las **46** filas …, las **18** ventanas `W1`–`W17` …, las **8** comprobaciones `X-A`–`X-H`, los 11 escenarios negativos y los 12 de §14», con su nota «Corregido por `P-04`». Las nueve `RC-*` ya no se cuentan | **SUPERADO** |
| 5 | `P-05`≡`Q-08` | La sección se reescribió entera (L2293–2382). Verifiqué sus cinco puntos: el gate consta **hecho** (0), el ordinal **no se escribe** (4), la cifra al Owner dice **CATORCE** (5), la excepción del kernel **remite en vez de copiar** (6). Las cinco afirmaciones falsas desaparecieron | **SUPERADO en el texto** *(la comprobación que debía impedir su regreso NO lo impide: experimento `E`, y es hallazgo aparte)* |
| 6 | `P-06` | **CORREGIDO EN UNA SEDE Y NO EN LA OTRA.** Doc 11 L8400 dice hoy «*esta sede decía «cero apariciones en el documento 11», y era falsa*». **`DECISIONES-Y-CONTRADICCIONES.md` L346 sigue diciéndolo**, y hoy hay 12·10·13. Ver §9 | **NO SUPERADO** |
| 7 | `P-07` | **L8489**: `## PN-16 · NUEVA · la grafía canónica de <CAP>:revisión vive en material APROBADO`, y **no elige la grafía**: registra que hay que elegir y que la elección es del Owner. Es exactamente lo pedido | **SUPERADO** |
| 8 | `P-08` | El universo se DERIVA con comando público, en commit propio y anterior al manifiesto. Lo ejecuté: 59 · 41 174. Crucé universo contra asignación: **vacío en las dos direcciones**. «SIN ASIGNAR 0» ha dejado de ser verdadero por construcción *(residuos: `R-N2`, `R-N3`)* | **SUPERADO** |
| 9 | `Q-01` | Reproducido: sin `.git`, `G-11b` **FALLA CERRADO**. Su título lo declara | **SUPERADO** |
| 10 | `Q-02` | Reproducido: `capacidad_productora: "VER:dosier"` en `INC` **ya no** mueve el ancla; siguen siendo `['AUD','INV']`. `obl_base = [_base(v) for v in obl]` | **SUPERADO** |
| 11 | `Q-03` | Reproducido: `DOM`/`SEG` desnudos en `FEA` → **FALLA `G-15`** nombrando el reparto vía a vía. La salida publica hoy `reparto por vía: [(2,1),(4,8)]` | **SUPERADO** |
| 12 | `Q-04` | Reproducido **en las dos direcciones**: dentro de `kernel/` → 29/30 y `G-23` lo caza; **fuera de `kernel/`, con (a) y el registro duplicados y un `C8` que declara contradecir a `C4` y `C7` → 30/30 EN VERDE**. La corrección se aplicó al perímetro, no al principio | **NO SUPERADO** |
| 13 | `Q-05` | Reproducido a medias: el escalar de bloque se caza **y nombra el campo**, como promete. **La INDENTACIÓN no se aplica**: un campo anidado bajo clave inventada se deriva como obligatoria y `prosa_sospechosa` queda vacía (fixture mío) | **NO SUPERADO** |
| 14 | `Q-07` | **L7920**: «*Las demás vigentes —`PN-6` a `PN-16`—*», con su nota «Corregido otra vez por `Q-07`». Derivé el censo: 16 cabeceras − `PN-4` − `PN-5` = **14**, y el rango termina en la última vigente | **SUPERADO en su sede** *(la cifra sigue caducada en cinco sedes vecinas: §0, §8.2 `m-1`, `CHECKPOINT` ×2, `00-INDICE`. Hallazgos aparte)* |
| 15 | `Q-09` | El literal `_VIGILADAS = ("DOM","SEG")` **desapareció** y el conjunto se deriva de las fichas | **SUPERADO en la letra** *(el fixture que lo respalda es tautológico: hallazgo aparte)* |
| 16 | `Q-10` | Verificado en `_analizar`: la tupla lleva `seccion` y `_exige_item` decide por la procedencia, no por la vía | **SUPERADO** |
| 17 | `Q-11` | Las anclas se publican proceso a proceso: `AUD → conclusion-fundada`, `INV → evidencia-producida`, con su nota de corrección | **SUPERADO** |
| 18 | `Q-12` | La cifra se deriva de los fixtures ejecutados y la salida real dice «**17 fixtures ejecutados**» | **SUPERADO** *(con la reserva de que uno de los 17 no puede fallar)* |
| 19 | `Q-14` | Verificado: **L1183** lleva `[HISTÓRICO · el estado que dejó la tanda de D96–D103…]`, y el bloque vigente dice «`C-L.3` CERRADA · **por D104, y NO por D103**», con las cuatro combinaciones. `D104` aparece en las sedes vigentes | **SUPERADO** |
| 20 | `Q-15` | `grep -n ' ancho ='` → sin resultados. `grep -n 'toda todo'` → sin resultados | **SUPERADO** |
| 21 | `R-01` | **L1172** dice hoy «*ahí vive la idempotencia — **no en la igualdad del `id`, que §2.8 retiró como prueba***», y el punto 8 de §2.6.9 y el paso 0 lo repiten remitiendo a la guarda por `abandonada_id` | **SUPERADO** |
| 22 | `R-02` | Derivé `git diff --name-only 05f71b7 -- kernel/` → **6**, 3 directos + 3 de evidencia. La sección de entrada **no contiene ni una ruta de `kernel/`**: remite. `G-23` lo contrasta y publica la cifra | **SUPERADO** |
| 23 | `R-03` | **L1955-1967** fija hoy quién dice qué: §3.6 FIJA la forma · la capa B la VALIDA y remite · §2.6.5 describe la caída · el paso 0 dice cómo se completa. La sede está decidida y la otra remite | **SUPERADO** |
| 24 | `R-04` | **NO SUPERADO, Y AGRAVADO.** Ver `D-1` de §4. El punto 7 es byte-idéntico a `7764cca`; la fila de `W17` afirma que el punto 7 hace un reparto que el punto 7 no hace, y `W8` dice lo contrario que ella | **NO SUPERADO** |

```text
RECUENTO DERIVADO DE LAS FILAS DE ARRIBA, no copiado

  SUPERADO          20   P-01≡Q-13 · P-02≡Q-06 · P-03 · P-04 · P-05≡Q-08 · P-07 · P-08 ·
                         Q-01 · Q-02 · Q-03 · Q-07 · Q-09 · Q-10 · Q-11 · Q-12 · Q-14 ·
                         Q-15 · R-01 · R-02 · R-03
  NO SUPERADO        4   P-06 · Q-04 · Q-05 · R-04
                        ──
                        24   los veinticuatro ids, cada uno EXACTAMENTE UNA VEZ
```

### `M-04`, aparte, como PROPOSICIÓN GENERAL

**`M-04` sigue FALLIDA.** Su proposición —«se puede construir un árbol defectuoso que pase 30/30
en verde»— sigue siendo verdadera, y la demostré **ocho veces** (§7). La tanda añadió protección
contra `Q-01`, `Q-04` y `Q-05`, y esa protección **funciona** en el perímetro de cada
contraejemplo; ninguna de las tres generaliza. El corpus lo dice de sí mismo con exactitud —«*la
proposición es universal y una tanda sólo puede cerrar los contraejemplos que conoce*»— y esa
honestidad consta a favor. **Pero yo soy el gate posterior que el propio corpus dice que hace
falta, y mi respuesta es que sí sigue habiendo un árbol defectuoso en verde. Hay ocho.**

---

## 9 · DICTAMEN EXPRESO SOBRE `D97` Y `G20`/`G21`/`G23`

El encargo me obliga a decidir **expresamente y con esas palabras**. Lo hago.

> ## La afirmación conservada en `D97` es una **CONTRADICCIÓN VIGENTE**.
> ## **NO** funciona como registro histórico suficientemente identificado.

**La afirmación.** `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` **L346**, columna de causa de
la fila `D97`:

> «`G20`, `G21` y `G23` tienen **cero** apariciones en el documento 11, en (a), en (b) y en
> `E2`; `G22` tiene UNA, como cita de apoyo.»

**El árbol de hoy, recontado por mí:**

```text
$ for g in G20 G21 G22 G23; do grep -c "$g" docs/evolucion/11-ARQUITECTURA-INTEGRADA.md; done
G20 → 12      G21 → 10      G22 → 16      G23 → 13
```

**Y la falsificó su propio commit. Lo verifiqué con `git show` sobre el commit que la escribe:**

```text
$ c=d868bcb                # «aplicar la tanda de correccion del gate definitivo — D96–D102, PN-15…»
                       ANTES ($c^)      DESPUÉS (mismo commit)
G20                        0                  13
G21                        0                  11
G22                        0                  17
G23                        0                  14
```

### Las cinco razones de mi decisión

**1 · No dice de qué revisión habla.** El verbo es *tienen*, presente. Nombra los materiales y no
nombra commit, fecha, ni «en el momento de escribirse». **Un registro histórico suficientemente
identificado dice cuándo fue verdad.** Éste invita a un barrido que lo desmiente.

**2 · No lleva ninguna marca, y el corpus tiene esa marca y la usa.** `grep` sobre el bloque no
devuelve `[HISTÓRICO]`, ni `[REVISADO por …]`, ni nota al pie. El mismo fichero **sí** las pone
en otras filas —el `[REVISADO por D62]` y el `[REVISADO por D61]` que leí en el checkpoint tienen
su equivalente en el registro—, y el checkpoint eleva la disciplina a regla explícita: «*ninguna
afirmación vieja sobrevive sin marca de histórica*».

**3 · La cláusula de inmutabilidad del registro no la cubre, y el corpus tiene DOS remedios
probados que no exigen reescribirla.** El primero es una **decisión nueva que derive el
recuento**, que es lo que `D94` hizo con la cifra «CATORCE» de `D68`/`D77`. El segundo es un
**ADDENDUM**, que es lo que `D106`(iii) hizo con `O16` en **este mismo fichero**. **No es que no
se pudiera: es que no se hizo.**

**4 · Y ésta es la que decide: la misma frase SÍ se corrigió, en la otra sede, en esta misma
tanda.** Doc 11 **L8400** dice hoy, con todas las letras, «*Esta sede decía «cero apariciones en
el documento 11», y era falsa*». El corpus **ya ha juzgado la frase y la ha declarado falsa**.
Dejar la frase idéntica, sin marca y en presente, en la sede que registra la decisión que la
originó, no es conservar historia: es el patrón que doce tandas persiguen —«*una decisión bien
tomada llega a la mitad de los sitios que la invocan*»— aplicado a la corrección de sí misma.

**5 · Y es media corrección por segunda vez sobre la misma decisión.** `D106`(i) ya diagnosticó
que «*la fila de §17 la escribió `D97` en el mismo commit que la presión, con lo que la prueba
pasaba en verde el día que nacía*», y corrigió **la prueba y no el recuento del cuerpo**.

### Lo que NO es, y consta expresamente

**La RESOLUCIÓN de `D97` es CORRECTA y debe conservarse.** Lo verifiqué en la sede real:

- Las cuatro reglas existen y están vigentes en `kernel/KERNEL.md` 1.5.0: `G20` L640, `G21` L682,
  `G22` L692 —con su `#### Timebox` en L694—, `G23` L748. Sin marca de derogación.
- `a.11` —«la ÚNICA lista que deroga o ajusta reglas»— **no las nombra en ninguna de sus cinco
  filas**, y `E2.4` demuestra que lo no nombrado sobrevive: hizo falta una enmienda aprobada del
  Owner para reclasificar `G29`, que `a.11` nunca nombró.
- `G21` L690 dice que el gate del Circuito 0 **«NO es negociable por el sistema»**. F4 decidiendo
  por su cuenta qué sobrevive sería exactamente el conflicto de interés que esa regla nombra.
  **F4 se abstiene donde debe abstenerse, y eso es mérito.**
- §17 recibió la fila propia que `D97` promete, y declara las cuatro «PRESIONADAS y pendientes de
  F5. NO derogadas por F4».
- La **PRUEBA POSTERIOR de `PN-15` falla hoy, y tiene que fallar.** La ejecuté: `grep 'G2[0-3]'`
  sobre (a) devuelve **una** línea —`a-CAPACIDADES-APROBADA.md:180`, la ficha de `INV`—, que no
  es fila derogatoria y no está en `a.11`.

```text
LA RESOLUCIÓN de `D97` (`PN-15`)   CORRECTA. Registrar la presión sin decidirla era lo que
                                   procedía, y `G21` lo exige. SE CONSERVA ENTERA.

LA JUSTIFICACIÓN de `D97` (L346)   CONTRADICCIÓN VIGENTE, no registro histórico. Severidad
                                   MEDIO —la resolución sobrevive y no cambia ningún
                                   comportamiento—, y por ello `P-06` del documento 21
                                   NO está superado.

LA VÍA DE CORRECCIÓN               NO es reescribir `D97`. Es un ADDENDUM que acote el
                                   barrido y lo feche, como `D106`(iii) hizo con `O16` en
                                   este mismo fichero. CLASE A.
```

---

## 10 · LAS TRECE CONDICIONES `C-L`, ADJUDICADAS

Verificadas contra la **clasificación vigente** del checkpoint (L1269–1317, delimitada y cerrada
con `FIN DE LA CLASIFICACIÓN VIGENTE`), y contra sus sedes.

| id | estado publicado | mi adjudicación | motivo verificado por mí |
|---|---|---|---|
| `C-L.1` | CERRADA | **CERRADA** | `revision_base` obligatorio en §3.6 y participante en `tx`. *(Y su fila de detalle es reescribible sin que `G-16` lo vea: experimento `D`)* |
| `C-L.2` | REGISTRADA PARA F5 | **REGISTRADA PARA F5** | `PN-15` existe, la decisión sigue sin tomar y es del Owner. **Con la reserva de §9**: su justificación en `D97` es una contradicción vigente |
| `C-L.3` | CERRADA por `D104` | **CERRADA** | El bloque anterior lleva `[HISTÓRICO]`, el vigente nombra `D104` y las CUATRO combinaciones, y «cero o un par, nunca dos» ya no aparece en sede viva. `G-16` se acota al bloque vigente |
| `C-L.4` | CERRADA | **CERRADA** | El ADDENDUM DE CRONOLOGÍA de `O16` no reescribe, no inventa cita y no crea `O17`. Verifiqué las dos fechas con `git log`: `a713590` = 2026-08-28, `d868bcb` = 2026-08-29 |
| `C-L.5` | CERTIFICADA | **CERTIFICADA, Y LA MANTENGO CERTIFICADA** | Las dos restas dan ∅ y las calculé (§3). El universo se deriva. Las doce agotadas se sostienen. **Con dos reservas que registro y que NO la reabren**: su sede lleva estado compuesto (cabecera «abierta, y no la cierra esta tanda» / cierre «CERTIFICADA»), y el instrumento que la sostiene —los manifiestos— no está protegido por ninguna comprobación (`R-N1`) |
| `C-L.6` | CERRADA | **CERRADA** | Las cinco salidas del gate de `M7` en §8.3 |
| `C-L.7` | CERRADA | **CERRADA EN LA FORMA, NO EN EL FONDO** | El checkpoint reancla su estado, y la sección de entrada está reescrita y es verdadera. **Pero el mismo fichero publica TRECE presiones en dos sedes vivas** —L1171 y L1843, ésta bajo el rótulo «CIFRAS VIGENTES, DERIVADAS»— **donde el árbol deriva CATORCE**, y su «Estado de las fases» omite las dos últimas pasadas sin marca |
| `C-L.8` | CERRADA | **CERRADA** | El `hash_previo` de la reparación, unificado para las tres causas |
| `C-L.9` | CERRADA | **CERRADA** | 46 filas derivadas; `G-26` deriva los recuentos. *(Y `G-26` es desactivable con una palabra: experimento `E`)* |
| `C-L.10` | CONTRATADA PARA F6 | **CONTRATADA PARA F6** | Cero líneas escritas, y lo verifiqué. Contratar no es implementar |
| `C-L.11` | CERRADA | **CERRADA** | `X62` da fila propia a §6.7 |
| `C-L.12` | REGISTRADA PARA F5 | **REGISTRADA PARA F5** | Los dos restos de (b) como checklist `E5`, y `E5-3` elevado a `PN-16`. El texto de (b) sigue como estaba |
| `C-L.13` | MIXTA POR DESGLOSE | **MIXTA POR DESGLOSE** | `K-05` `K-09` `K-10` `K-08` `L-03` corregidos · `J-11` contratado para F6 y no implementado |

```text
CERRADAS                    9   C-L.1 C-L.3 C-L.4 C-L.6 C-L.8 C-L.9 C-L.11 + (C-L.7 en la forma)
CERRADA EN LA FORMA, NO      1   C-L.7
  EN EL FONDO
CERTIFICADA POR COBERTURA    1   C-L.5   ← la mantengo
REGISTRADAS PARA F5          2   C-L.2 C-L.12
CONTRATADA PARA F6           1   C-L.10
MIXTA POR DESGLOSE           1   C-L.13
                            ──
                            13   cada id EXACTAMENTE UNA VEZ (C-L.7 cuenta una sola vez)
```

**Ninguna de las trece está mal clasificada, y ninguna exige inventar arquitectura.** La única
que muevo es `C-L.7`, de CERRADA a **cerrada en la forma y no en el fondo**, y digo por qué: el
fichero que la condición existe para mantener vigente publica dos cifras caducadas en sedes que
se autodeclaran vigentes y derivadas.

---

## 11 · LA CONDUCTA DEL COORDINADOR DE ESTE GATE

**Los hechos, verificados por mí con `git log` y `git show --stat`:**

```text
e645db1  2026-08-30 10:35:30  derivar-universo-obligatorio.py         1 fichero · 289 ins · 0 sup
44d2e74  2026-08-30 10:37:01  manifiesto previo de asignación          1 fichero · 316 ins · 0 sup
706c787  2026-08-30 10:58:43  ADDENDUM 1                               1 fichero · 119 ins · 0 sup
```

**Tres commits, uno por documento, en el orden correcto, cada uno solo y con cero supresiones.**
El derivador es **anterior** al manifiesto, como el manifiesto declara. El addendum es **HEAD** y
su único fichero, de modo que `Q5` pudo crearse después y no antes, que es lo que el addendum
promete y lo que `git log` permite comprobar.

**El hecho que se me pide juzgar.** El manifiesto de `44d2e74` declaró **33 fuentes AGOTADAS**.
Su propia regla 1 exige que un gate anterior declare `LEÍDO ÍNTEGRO DE ESA RUTA`, y advierte que
«*la fila del manifiesto de ASIGNACIÓN transcrita en un dictamen NO es una lectura*». **Veintiuna
de las treinta y tres se apoyaban en el documento 20, L368 · L372 · L638 — que no nombran ni una
sola ruta.** Lo verifiqué: el único sitio del documento 20 donde esas rutas aparecen es la tabla
del coordinador, que es un manifiesto de **asignación**. Y trece líneas después de L638 el
adjudicador `O` escribe «REGLA DE CIERRE · NO CERTIFICABLE POR MÍ». **El manifiesto aplicó su
regla 1 a las doce que sí la cumplían y no se la aplicó a las veintiuna que no.**

### Mi juicio, y va sin suavizar en las dos direcciones

**No es un encubrimiento. Es la reacción correcta, y es la mejor conducta de este expediente.**
Cinco razones, y las cuatro primeras las comprobé:

1. **No editó el manifiesto defectuoso.** `git show 44d2e74` sigue teniendo su error dentro, y el
   addendum lo dice: «*queda como está, con su error dentro, que es como debe quedar*». Editarlo
   habría sido borrar la prueba.
2. **Nombró al relevo que lo encontró** —`Q3`, hallazgo `Q3-02`— y transcribió su hallazgo
   entero, incluida la parte que le acusa.
3. **No corrigió el hallazgo: lo devolvió al circuito.** Reasignó las 21 a lectura íntegra en
   este mismo gate y escribió, expresamente, que el hallazgo «*entra en el dictamen de `Q` y lo
   adjudica `R` como cualquier otro, incluido su juicio sobre si el coordinador ha reaccionado
   bien o ha tapado*». **Un encubridor no escribe la frase que instruye a su juez para que lo
   juzgue.**
4. **Pagó el coste en vez de defender la posición.** 3 575 líneas más de lectura, un relevo nuevo,
   y un retraso de veintiún minutos entre el manifiesto y el addendum. La alternativa cómoda
   —argumentar que la declaración de conjunto de `O` bastaba— estaba disponible y no se tomó.
5. **Y el resultado es verificable, no declarativo:** las 21 están hoy leídas íntegras por `Q5`
   con SHA-256 recalculados, que `Q4` recalculó y que **yo he vuelto a recalcular**. La resta da
   vacío.

**Y ahora las tres cosas que le reprocho, porque el juicio no es una absolución.**

**`C-1` · El defecto era evitable, y lo era con su propio texto.** La regla 1 estaba escrita en el
mismo documento, dos páginas por encima de la tabla que la incumple. Es exactamente la forma que
`P-08` describió —«*una regla escrita bien y aplicada sólo donde era cómoda*»— y el addendum lo
reconoce con esas palabras. Que lo reconozca no lo borra: **21 de 33 es el 64 %.**

**`C-2` · El reparto pone `C-L.3` en el foco de `P` y no le da ninguna de sus once sedes.** Lo
verifiqué: las once están en `CHECKPOINT-ADS-NEXT.md` y en `00-INDICE.md`, las dos asignadas a
`Q+R`. **Se le pidió a un revisor un foco sin darle la fuente.** `P` lo denunció en vez de
inventarse un juicio, que es lo correcto, y hago mía su denuncia. Es un defecto del manifiesto
que ningún addendum corrigió.

**`C-3` · El aparato del gate rompe el validador de referencias del corpus que juzga.** Lo
demostré en `D-5`: sobre el candidato, 13/13 y árbol limpio; sobre HEAD, 12/13 por los dos
ficheros que este gate añadió. **No es defecto de la candidata, y por eso no entra en el
veredicto.** Pero sí es defecto del procedimiento, y tiene remedio conocido y barato: el
documento 21 enlazó su manifiesto y por eso el manifiesto anterior no rompe nada.

> **Conclusión: reacción correcta, no encubrimiento.** El coordinador hizo lo que `C-L.5`·`1bis`
> prescribe, en el plazo más corto posible y contra su propio interés, y entregó su propia falta
> al juicio del adjudicador en lugar de resolverla. **Coincido con `Q`, y he verificado los
> hechos por mi cuenta antes de coincidir.** Lo digo con la misma claridad con la que digo que el
> manifiesto era defectuoso y que dos defectos suyos —`C-2` y `C-3`— siguen sin corregir.

---

## 12 · RECUENTO CONSOLIDADO

**Método.** Uní los 27 hallazgos de `P`, los 42 de `Q` y los 3 míos, detecté los solapes y
adjudiqué la severidad de cada uno. **Las severidades son MÍAS, no las que propusieron los
revisores**, con el criterio que declaro: **BLOQUEANTE** = obliga a decidir arquitectura nueva ·
**GRAVE** = una garantía publicada no se sostiene, o `F6` construiría algo distinto de lo que el
contrato quiere · **MEDIO** = una afirmación vigente es falsa sin cambiar el comportamiento ·
**MENOR** = editorial o de propagación.

**Los tres solapes, resueltos contra la fuente y contados UNA vez:**

```text
P-03 de `P`  ≡  Q-17 de `Q`     §15.8 no sostiene el recuento que §0 dice derivar de él
P-22 de `P`  ≡  Q-37 de `Q`     `C-L.5` con estado compuesto en una misma sección
P-27 de `P`  ≡  Q-08 de `Q`     `comprobar_referencias.py` falla sobre el árbol de hoy
```

```text
27 (P)  +  42 (Q)  +  3 (R)  −  3 solapes  =  69 HALLAZGOS DISTINTOS
```

| severidad adjudicada por mí | nº |
|---|---|
| **BLOQUEANTE** | **0** |
| **GRAVE** | **8** |
| **MEDIO** | **34** |
| **MENOR** | **27** |
| | **69** |

**Los OCHO GRAVES, con su procedencia:**

```text
1  `R-04` NO SUPERADO Y AGRAVADO · W17 (L1172) contra el punto 7 (L1938-41) y contra W8
   (L1162), con una cita falsa que sostiene el recorte           P-01 de `P` · verificado por mí
2  el nivel ESTRUCTURAL no lo produce ninguna fase de ningún macrocircuito: por la regla dura
   de §9.2 quedan inalcanzables la Operativa de INS-4, la Integrada de A9/M5/INS-7, y con
   ellas O12                                                     P-06 de `P` · verificado por mí
3  `reconciliacion_pendiente` del canal de órdenes no tiene productor: la prueba T22 de
   material APROBADO no es satisfacible, el freno 4 de b.12 no dispara, y ninguna PN lo
   registra                                                      P-07 de `P` · verificado por mí
4  §0 declara derivar de §15.8 un recuento que §15.8 ya no sostiene —trece bloques donde dice
   doce— y D96–D106, once decisiones vigentes, no tienen bloque   P-03 ≡ Q-17 · verificado por mí
5  `M-04` sigue FALLIDA y más ancha: OCHO árboles defectuosos en verde         Q-01 · §7
6  el perímetro: la corrección de `Q-04` se aplicó bajo `kernel/` y el mismo ataque un
   directorio afuera —sobre material APROBADO— da 30/30                        Q-02 · §7 exp. A
7  `G-26` se desactiva escribiendo «regresión» en la línea, y con ello se REINSTALA el único
   GRAVE del gate anterior con dos palabras                                    Q-04 · §7 exp. E
8  **MÍO** · `G-22` sólo fija `docs/evolucion/1[5-8]-`: volteé los veredictos de los
   documentos 19, 20 y 21 a `SUFICIENTE PARA F5` con 30/30 en verde, y reescribí el
   manifiesto declarado inmutable del gate anterior                        `R-N1` · §6 y §7 G·H
```

**Lo que verifiqué y lo que acepté, dicho sin adorno.** Abrí contra fichero y línea, o
reproduje en `/tmp/lab-R`, **los ocho GRAVES y veintiuno de los MEDIOS**. De los MENORES verifiqué
una muestra. **Los demás los acepto con la severidad que su revisor les puso**, porque los dos
dictámenes son internamente consistentes, citan fichero y línea en cada fila, declaran
expresamente qué reprodujeron y qué no, y **los dos publican sus derrotas** —`P` publica cinco
refutaciones que perdió y rechaza seis hallazgos de sus propios relevos; `Q` rebaja cuatro de los
suyos y rectifica su propio recuento derivándolo otra vez de las filas—. **Lo declaro como
límite, no como certificación.**

---

## 13 · CLASIFICACIÓN PARA LA TANDA SIGUIENTE

### A · CORREGIBLE EN F4c SIN DECIDIR ARQUITECTURA — **68 de 69**

Entran los sesenta y ocho restantes. Los agrupo por remedio, y **el remedio de cada uno está
determinado**:

```text
PROPAGACIÓN DE UNA DECISIÓN YA TOMADA
  · el punto 7 de §2.6.9 y la fila de `W17` tienen que decir lo mismo, y `W8` con ellos.
    Es UNA decisión ya tomada —`D105` fijó los seis pasos— y lo que falta es repartir los
    tramos sin mentir sobre quién los reparte. También `[1,2)`, que hoy es de `W11`
  · la cifra CATORCE, a §0, a `m-1` de §8.2, a `CHECKPOINT` L1171 y L1843, y a `00-INDICE` L58
  · `D104`, `PN-16` y el estado de `C-L.5` a las sedes que aún no los tienen

BATERÍA Y VALIDADORES
  · `G-22`: extender el rango inmutable a los documentos 19, 20 y 21, y a los manifiestos
  · `_BLOQUE_HISTORICO`: evaluar sobre la OCURRENCIA, no sobre la línea entera
  · la unicidad de proyección: comparar cifras derivadas, no un patrón de un carácter
  · `G-16`: contrastar por igualdad de estado, no por prefijo
  · `G-01`: exigir polaridad, no la mera presencia de «RETIRADA»
  · la comparación de CONJUNTOS: extenderla de `kernel/` a todo material normativo
  · la excepción del kernel: fijar CONTENIDO, no sólo ruta —empezando por `.upstream-hash`
  · el lector estructurado: usar la sangría que ya registra
  · el fixture de `_derivar_vigiladas`: dejar de compararse consigo mismo
  · el derivador: `len(set(fuentes)) != 14`, guarda para (iii) y (v), y leer los cardinales
    de su sede en vez de escribirlos

DOCUMENTACIÓN, REFERENCIAS, RECUENTOS Y TRAZABILIDAD
  · un ADDENDUM a `D97` que acote y feche su barrido, como `D106`(iii) hizo con `O16`
  · bloques de §15.8 para `D96`–`D106`, y reanclar §0
  · marcar histórico lo que lo es: «Estado de las fases», el tercer bloque de estado,
    la cabecera de `C-L.5`, `00-INDICE` L74
  · `exclusiones.yaml` o un enlace: que los manifiestos que `1bis` obliga a publicar no
    rompan `T147`, y que no rompan uno más cada gate
  · corrigendum externo para los defectos de dictámenes inmutables (docs 13, 19, 20)
  · una PN nueva para `reconciliacion_pendiente`/`T22`, y otra —o ampliar `PN-16`— para
    `VER:decisión` frente a `VER:decision`, que ya conviven dentro del kernel construido
```

**Todos son A porque el remedio está determinado y ninguno obliga a elegir entre alternativas
válidas que una decisión vigente no resuelva.** Dos de ellos —la PN de `T22` y la de la grafía—
**registran** una elección que corresponde al Owner; registrar es F4, elegir es F5, y el
mecanismo para eso ya existe y ya se ha usado.

### B · DECISIÓN EXCLUSIVA DEL OWNER — **1 de 69**

**El nivel ESTRUCTURAL y su productor** (GRAVE nº 2, `P-06` de `P`).

**Por qué es B y no A.** §9.2 fija la cadena `estructural ◀── operativo ◀── integrado ◀──
completo` y una **REGLA DURA**: «*un nivel no se declara por argumento ni por haber pasado el
anterior*». El gate del nivel Estructural —`gate:sistema-conforme`— tiene **una sola aparición en
todo el documento 11, y es su propia definición** (L6790). Ninguna fase de ninguno de los cuatro
macrocircuitos lo produce ni lo invoca: lo comprobé barriendo §8.1 (L6133), §8.2 (L6329), §8.3
(L6519) y §8.4 (L6701). Sin celda de Estructural `verificado` y vigente, ni la Operativa de
`INS-4` ni la Integrada de `A9`, `M5` e `INS-7` pueden elevarse, y **`O12` no es satisfacible por
ninguno de los cuatro recorridos**. Elegir dónde se produce no es propagar: es decidir un
recorrido nuevo, y afecta a una resolución del Owner (`O12`).

> **LA PREGUNTA EXACTA PARA EL OWNER**
>
> «El sistema define cuatro niveles de certificación encadenados —Estructural, Operativa,
> Integrada, Completa— y una regla dura: **un nivel no se puede declarar por haber pasado el
> anterior; alguien tiene que producirlo**. Hoy **ningún recorrido produce el nivel Estructural**,
> y por eso ninguno puede alcanzar la Operativa ni la Integrada, que es lo que su resolución
> `O12` exige. ¿Cuál de estas tres quiere?
>
> **(a) Que el nivel Estructural lo produzca la INSTALACIÓN**, como primer paso de `INS`, antes
> de cualquier otro nivel. Es la más barata y la que menos toca; a cambio, un producto ya
> instalado no revalida su Estructural cuando cambia el kernel.
>
> **(b) Que lo produzca CADA macrocircuito al arrancar**, como precondición propia. Es la más
> segura y la que hace `O12` satisfacible desde cualquier entrada; a cambio, añade un gate a los
> cuatro recorridos y encarece la migración y la actualización.
>
> **(c) Que el nivel Estructural deje de ser un nivel certificable y pase a ser una
> PRECONDICIÓN de arranque no certificada**, retirándolo de la cadena de niveles. Es la que menos
> maquinaria deja en pie; a cambio, hay que reescribir §9.2 y la definición de «nivel alcanzado»,
> y `O12` cambia de contenido.
>
> **F4 no elige ninguna, y lo dice: la cadena de niveles y `O12` son materia suya, no del
> sistema.**»

### C · TRABAJO FUTURO YA CONTRATADO — **0 de 69**

**Ninguno de mis sesenta y nueve hallazgos es trabajo ya contratado.** Y consta, porque también
lo comprobé: lo que **sí** está contratado y **no** invalida `F4c` es `C-L.10` —el censo
`AFIRMACIONES` derivado, `T152` y el CONTRATO `1bis` de los perfiles de `N-04`—, `J-11` dentro de
`C-L.13`, y las presiones `PN-1`…`PN-16`, que son materia de F5 con propietario declarado. **Los
tres tienen contrato completo, cero líneas escritas, y lo verifiqué.** No los cuento como
insuficiencia, igual que no cuento la ausencia de runtime, de piloto, de adaptadores certificados
ni de la adopción de PesquerApp: están declaradas con propietario y fase, y **eso es lo que F4
debe entregar y lo entrega.**

---

## 14 · VEREDICTO

# INSUFICIENTE PARA F5

**`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada. No he corregido nada.**

### Las razones, numeradas, cada una suficiente por sí sola

**1 · `M-04` sigue siendo FALLIDA, y hoy es más ancha que cuando el gate anterior la declaró
FALLIDA.** Construí y ejecuté **ocho** árboles defectuosos que pasan la batería **30/30 en
verde**. El gate anterior contó tres falsos verdes. **Y el peor es mío: volteé los veredictos de
los documentos 19, 20 y 21 —los tres gates independientes más recientes, incluido el que esta
tanda existe para cerrar— a `SUFICIENTE PARA F5`, y la batería no se enteró**, porque su rango
inmutable dice `1[5-8]`. La misma refutación sobre el documento 18 sí se caza. **Una garantía
mecánica que protege cuatro documentos de siete y llama a eso «los documentos no se han tocado»
es peor que no tenerla**, con las palabras que el propio corpus usa: «*nadie construye después el
mecanismo que sí lo haría*».

**2 · Las cinco correcciones de la batería funcionan en el perímetro exacto del contraejemplo que
las motivó, y en ninguna otra parte — y lo verifiqué en las dos direcciones para las cinco.**
`Q-04` se cerró bajo `kernel/` y el mismo ataque un directorio afuera, **sobre material APROBADO**,
da 30/30. `Q-05` se cerró para los escalares de bloque y no para la indentación que su propia
docstring promete. La unicidad de proyección se derrota interponiendo dos palabras. `G-26` se
desactiva escribiendo «regresión» —vocabulario corriente del corpus— en la línea, **y con esas
dos palabras se reinstala el único GRAVE del gate anterior: la cifra falsa hacia el Owner en la
sede que la cabecera designa como punto de entrada.** No es que las correcciones no funcionen:
es que ninguna generaliza, y ése es el patrón de método que doce tandas persiguen, aplicado
esta vez al instrumento que existe para detectarlo.

**3 · La corrección de `R-04` escribió en el texto normativo un error de hecho del adjudicador
anterior, y donde había una imprecisión hoy hay una contradicción entre tres sedes.** El punto 7
de §2.6.9 es **byte-idéntico** al de `7764cca` —lo comprobé con `git show`— y reparte «caída
entre 1 y 5 → `W17`». La fila de `W17` recortó su alcance y escribió que el tramo posterior al
`deriva` «*la cubre `W8` … **y así lo reparte el punto 7***». **No lo reparte así**, y `W8` dice
lo contrario que ella. El tramo `[4,5)` no lo reclama ninguna de las dos ventanas. **`R-04` no
está superado: está AGRAVADO**, y es la ventana que `D105` creó para cerrar dos GRAVES.

**4 · Aparecen DOS defectos GRAVES que ningún gate anterior había visto, y los dos rompen una
garantía publicada sobre material APROBADO.** El nivel **Estructural** no lo produce ninguna fase
de ningún macrocircuito, y por la regla dura de §9.2 eso deja inalcanzables la Operativa y la
Integrada, y con ellas `O12`. Y `reconciliacion_pendiente` del canal de órdenes **no tiene
productor**: sus dos disyuntos son sobre el diario de transacciones, y el agotamiento de
`MAX_CAS_RETRIES` declara expresamente que «NO modifica el estado canónico», luego **la prueba de
conformidad `T22` de material APROBADO no es satisfacible por esta arquitectura**, el freno del
paso 4 de `b.12` nunca dispara, y **ninguna presión lo registra**.

**5 · La regla que la tanda adoptó como remedio de su único GRAVE no ejecuta.** La sección de
entrada, reescrita entera y correctamente, delega el ordinal de la tanda en «*los bloques de
§15.8 del documento 11 y las filas de `00-INDICE.md`*». **§15.8 tiene trece bloques donde §0 dice
doce, y `D96`–`D106` —once decisiones vigentes, entre ellas las cuatro que este gate juzga— no
tienen bloque.** Y `00-INDICE` se contradice dentro de una sola tabla: L58 dice «DOCE presiones
vigentes» y L83 dice «pasan a CATORCE». La sede a la que se remite para no volver a escribir una
cifra a mano está incompleta en dos tandas enteras.

**6 · Y la razón de método, que es la que impide cerrar aquí.** De los sesenta y nueve hallazgos
distintos de esta pasada, **la mayoría los introdujo o los dejó pasar esta misma tanda**, y
cuatro son la reinstalación de defectos que el gate anterior ya adjudicó. `D97` lo enseña en su
forma más pura: **la misma frase falsa se corrigió en el documento 11 y se dejó intacta y en
presente en el registro de decisiones**, teniendo el corpus dos remedios probados en ese mismo
fichero. Cerrar aquí sería premiar exactamente lo que este expediente lleva trece tandas sin
poder aceptar.

### Lo que expresamente NO fundamenta este veredicto

- **NO falla por cobertura.** `OBLIGATORIO − ASIGNADO = ∅` y `ASIGNADO − LEÍDO = ∅`, y las
  calculé las dos. Las doce agotadas se sostienen ruta a ruta. **`C-L.5` sigue CERTIFICADA y la
  mantengo certificada.**
- **NO falla por el aparato del propio gate.** El `12/13` del runner del kernel lo causan los dos
  ficheros que este gate añadió; **sobre el candidato el runner da 13/13 y deja el árbol limpio**,
  y lo ejecuté.
- **NO falla porque nada esté construido.** Ninguna de mis seis razones es la ausencia de runtime,
  piloto, adaptadores certificados o adopción de PesquerApp. Verifiqué que están declaradas con
  propietario y fase.
- **NO falla por `D105`.** Es la mejor decisión de este expediente y lo sigue siendo: tres
  alternativas comparadas en tabla, elegida la mínima, y sobrevive intacta. **Lo que falla es su
  propagación al punto 7.**
- **NO falla porque quede arquitectura por inventar.** **Sesenta y ocho de los sesenta y nueve
  hallazgos son clase A**, y el que no lo es tiene su pregunta al Owner formulada palabra por
  palabra en §13.

### Y qué SÍ ha quedado cerrado, porque eso también es información

**El veredicto es de fondo, y sería deshonesto sin esto:**

1. **`C-L.5` está CERTIFICADA por segunda vez consecutiva, y esta vez sobre un universo
   DERIVADO.** `P-08` es el logro más sólido de la tanda: el universo obligatorio ha dejado de
   escogerse. Dos de sus cinco componentes se leen de sede normativa y **fallan cerrado con
   código 2 bajo ataque**, y lo ataqué. «FUENTES SIN ASIGNAR 0» ya no es verdadero por
   construcción: lo comprobé con las dos restas y salen vacías.
2. **Veinte de los veinticuatro hallazgos del documento 21 están genuinamente SUPERADOS**, y los
   verifiqué uno a uno contra el árbol. Entre ellos el **único GRAVE** de aquel gate: la sección
   «Siguiente acción exacta» está reescrita entera y sus cinco afirmaciones falsas desaparecieron.
3. **Las cinco vías nombradas de la batería están cerradas de verdad**, con control positivo mío:
   `G-11b` falla cerrado sin `.git`; el ancla normaliza y `VER:dosier` ya no la mueve; el reparto
   por vía se contrasta vía a vía; `G-23` caza la segunda sede dentro de `kernel/`; y el escalar
   de bloque falla **nombrando el campo que contiene la prosa**, exactamente como promete.
4. **`Q-14` y `C-L.3` están cerrados.** El bloque anterior lleva su marca `[HISTÓRICO]`, la
   clasificación vigente está delimitada, y `C-L.3` se describe hoy por `D104` con las cuatro
   combinaciones. La regla que `M-01` refutó ya no aparece en sede viva.
5. **Once de las trece condiciones `C-L` están cerradas, certificadas, registradas o contratadas
   con estado único**, y ninguna está mal clasificada. La única que muevo es `C-L.7`, y a «cerrada
   en la forma».
6. **`PN-16` es exactamente lo que había que hacer**: registra que hay que elegir la grafía y que
   la elección es del Owner, y **no elige**. `PN-15` sigue siendo honesta y **su prueba posterior
   falla hoy, como debe** — la ejecuté.
7. **La disciplina de inmutabilidad se cumple sin excepción en el registro**: `D1`–`D106` y
   `O1`–`O16` intactas, y los documentos 15–21 sin tocar en el árbol real.
8. **Y el coordinador de este gate encontró su propio defecto por boca de un revisor suyo,
   publicó un ADDENDUM que no edita el manifiesto anterior, pagó 3 575 líneas de lectura y
   entregó su falta al juicio del adjudicador en vez de resolverla.** Eso es la conducta que el
   corpus prescribe, ejecutada contra el propio interés, y consta.

**Ésta sigue siendo, con distancia, la candidata más sólida que este corpus ha producido. No
falla por concepción, no falla por cobertura, no falla por lo que decidió y no falla por lo que
dejó sin construir. Falla porque el instrumento que existe para probar que sus decisiones han
llegado a todas partes no puede distinguir un árbol sano de uno en el que el veredicto de este
mismo gate dice `SUFICIENTE PARA F5`.**

```text
git status --porcelain   →   VACÍO       comprobado al abrir y al cerrar
HEAD                     →   706c787189c2241124d0df467f18eb5c5b60667b    sin cambios
FICHEROS DEL REPOSITORIO MODIFICADOS, CREADOS O BORRADOS   ninguno
EXPERIMENTOS             →   /tmp/lab-R/{base,A,Actl,Bx,Bctl,C,D,E,F,G7,G8,G9,K,K2}, borrado
NINGÚN HALLAZGO SE HA CORREGIDO EN ESTA PASADA, y es deliberado.
```

**`F4c` sigue ABIERTA. `F5` NO queda autorizada. `C-L.5` sigue CERTIFICADA.**

**ADJUDICADOR `R` · adjudicación cerrada.**
