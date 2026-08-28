# GATE FINAL INDEPENDIENTE DE F4C

> **Nota de transcripción — la escribe el agente principal, NO los revisores ni el adjudicador.**
>
> ```text
> QUIÉN JUZGA             TRES agentes con CONTEXTO LIMPIO, encargados para esta pasada:
>                           REVISOR A      arquitectura, estado, protocolo transaccional,
>                                          concurrencia y Git
>                           REVISOR B      integración con kernel, capacidades, procesos,
>                                          macrocircuitos, documentación, adopción y
>                                          operabilidad
>                           ADJUDICADOR C  recibe los DOS dictámenes ya cerrados, verifica
>                                          cada hallazgo contra su fichero y su línea, y
>                                          emite el ÚNICO veredicto
>                         Ninguno escribió F4. Ninguno aplicó ninguna de sus correcciones.
>                         Ninguno participó en `D16`–`D70` ni en `O1`–`O16`.
>
> CÓMO SE PROTEGIÓ LA     A y B trabajaron EN PARALELO y NO vieron el dictamen del otro
> INDEPENDENCIA           hasta terminar. C recibió los dos DESPUÉS de que ambos cerraran.
>                         **C no resolvió por mayoría**: coincidir no hace cierto un
>                         hallazgo, y C rechazó piezas de cinco de ellos.
>
> QUIÉN TRANSCRIBE        el agente principal, que SÍ escribió las correcciones de F4 y por
>                         tanto NO PUEDE CERTIFICAR SU PROPIO TRABAJO. Su papel aquí es
>                         copiar los tres textos LITERALMENTE. **No ha suavizado,
>                         reinterpretado ni corregido ningún hallazgo**, y NO ha tocado
>                         `11-ARQUITECTURA-INTEGRADA.md` en esta pasada.
>
> QUÉ SE HA RETIRADO      de los tres textos recibidos, sólo el sufijo técnico del arnés de
>                         ejecución. Ni una palabra de los juicios se ha alterado.
>
> SOBRE QUÉ ÁRBOL         HEAD `a713590a9a1d2d0f6d0a3c5942f81a8052630ed5`, rama
>                         `redesign/kernel-2.0`, árbol limpio, ONCE commits locales sin
>                         publicar. El remoto seguía en `8e08a48`.
>
> VEREDICTO               **INSUFICIENTE PARA F5.** Por tanto **`F4c` NO se cierra**: sigue
>                         ABIERTA, y F5 NO queda autorizada.
>
> QUÉ NO SE HA HECHO      NINGÚN hallazgo se ha corregido en esta pasada. Corregirlos aquí
>                         sería volver a que quien recibe sea quien aplica, que es el
>                         defecto que estas revisiones encadenadas existen para no repetir.
> ```

---

## Corpus obligatorio: inventario y cobertura

El encargo exige que **entre A y B** se cubra íntegro el corpus obligatorio. El inventario
previo dio **121 ficheros** obligatorios, todos presentes en el árbol:

```text
docs/evolucion obligatorios        8     capacidades (CAPACIDAD.md)      15
docs/rediseno + owner + KERNEL     8     recorrido (10 procesos)          2
contratos C1–C7                    7     circuitos                        3
entrada                            6     diseno                           6
packs                              5     esquemas · manifiestos · plantillas  30
validadores                       16     pruebas                         10
tooling                            5     ─────────────────────────────  TOTAL 121
```

**La cobertura resultó INCOMPLETA**, y el adjudicador la derivó cruzando las dos secciones
«corpus realmente leído». **Dieciocho fuentes obligatorias quedaron sin abrir por ninguno de
los dos.** El detalle, y por qué basta para bloquear con independencia de los hallazgos, está
en la sección 7 de la adjudicación.

---

## DICTAMEN DEL REVISOR A

### 1 · Identidad y procedencia

Soy el **REVISOR A** del gate final independiente de `F4c`. Reviso el eje **arquitectura, estado, protocolo transaccional, concurrencia y Git**.

```text
REPOSITORIO      /home/jose/ads-kernel
RAMA             redesign/kernel-2.0
HEAD             a713590a9a1d2d0f6d0a3c5942f81a8052630ed5   (verificado con git rev-parse)
ÁRBOL            limpio (git status --short vacío)
MODO             SÓLO LECTURA. No he modificado ningún fichero, no he hecho commits
                 ni he ejecutado ninguna escritura de git
```

**Qué NO soy.** No escribí F4 ni ninguna de sus correcciones. No apliqué `D16`–`D70`. No soy el adjudicador: no emito el veredicto, lo recomiendo. No he consultado al REVISOR B ni supongo nada de lo que diga.

**Qué he tratado como objeto y no como fuente.** Los documentos `12`, `13`, `14`, `15`, `DECISIONES-Y-CONTRADICCIONES.md`, los mensajes de commit y las cabeceras de corrección del propio entregable. Cada cita que aparece abajo la he abierto en su fichero original con `grep`/`sed`. Cada recuento lo he derivado con un script, no copiado.

---

### 2 · Corpus realmente leído

| fichero | cobertura | qué he cubierto |
|---|---|---|
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | **íntegro en mi eje; parcial fuera de él** | §0, §1 completo, **§2 completo (L259–2858)**, §3.6 completo, §3.8, §6.7, §7.4, §9.5, §10, §15.7, §15.8, §16 (cabecera + PN-1, PN-7, resumen), §19, cabecera L1–62. **NO leído en detalle:** §4, §5 (salvo §5.7), §8, §11, §12, §13, §14, §17, §18 — quedan al REVISOR B |
| `docs/rediseno/a-CAPACIDADES-APROBADA.md` | **parcial, tramos nombrados** | `a.9` L627–760 (los cinco conceptos, autoridad frente a escritor, tablero, atomicidad), TOC completo |
| `docs/rediseno/b-RECORRIDO-APROBADA.md` | **parcial, tramos nombrados** | `b.14` L698–726 íntegra, TOC completo |
| `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | **parcial** | L186–239 (`D60`–`D70`), L290–310 (`O16`/`C8`) |
| `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | **parcial** | TOC, `G1`, `G2`, `B1` (L180–225), §9 condiciones C1–C13 |
| `docs/evolucion/12`, `13`, `14` | **consulta dirigida** | sólo para verificar citas del entregable (`abortada`, `reconciliada`, `D38`, hallazgo `N-9`) |
| `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | **íntegro en lo relevante** | L1–100 + `grep` dirigido sobre `aplica_a` y los gates |
| `kernel/operativo/contratos/C6`, `C4` | **estructural** | TOC + `grep` sobre control repo, `estado/`, topología |
| `kernel/operativo/esquemas/` | **inventario completo** | 19 `.yaml` listados y contados; `integration-set.yaml` leído en sus campos citados |
| `kernel/operativo/validadores/` | **ejecutados**, no leídos línea a línea | 7 validadores ejecutados; `comprobar_fuentes.py` y `workspace.py` leídos en su dependencia TOML |
| `kernel/operativo/plantillas/SOURCES.toml` | **íntegro** (cabecera normativa L1–60) | |
| `tooling/workspace.py` | **estructural** | mapa de funciones + tramo `tomllib` |
| `tooling/tests/test_workspace.py`, `tooling/new-project.sh` | **NO leídos** | pytest no está instalado; ver §7 |

**Lo que NO he cubierto y digo para que conste:** §4, §5, §8, §11–§14, §17–§18 del entregable; `C1`, `C2`, `C3`, `C5` completos; los `.py` de validadores línea a línea; `test_workspace.py`.

---

### 3 · Método y comandos

```bash
git rev-parse HEAD; git status --short                    # anclar HEAD y modo lectura
grep -n '^#\{1,3\} ' docs/evolucion/11-*.md               # TOC derivado, no el índice declarado
sed -n '<a>,<b>p' docs/evolucion/11-*.md                  # lectura por tramos, 17 tramos

# recuento de la tabla adversarial — derivado, no copiado
awk 'NR>=1244 && NR<=1350' docs/evolucion/11-*.md \
  | grep -cE '^\| \*?\*?`X[0-9A-Za-z]+`'                  # → 42 filas
awk '...' | grep -oE '`X[0-9A-Za-z]+`' | sort -u | wc -l  # → 42 ids únicos

# barridos de consistencia sobre predicados y enums
grep -n 'sin `derivada`\|sin evento `derivada`\|único terminal' docs/evolucion/11-*.md
grep -n 'abandono-de-transaccion\|posterior-al-cierre\|sin-transaccion' docs/evolucion/11-*.md
grep -n 'seis fases\|CINCO fases\|cinco conceptos' docs/evolucion/11-*.md
grep -n '^## `PN-' docs/evolucion/11-*.md                 # → 12 bloques, 10 vigentes
grep -n '| `D6[4-8]` |' docs/evolucion/11-*.md            # → VACÍO

# verificación de citas contra la fuente aprobada
sed -n '656,700p' docs/rediseno/a-CAPACIDADES-APROBADA.md  # los cinco conceptos, literal
sed -n '698,726p' docs/rediseno/b-RECORRIDO-APROBADA.md    # b.14, rama «revertir»
grep -n 'aplica_a' kernel/operativo/contratos/C7-*.md      # → «una o más fuentes»

# ejecución real
for v in comprobar_{fuentes,contratos,referencias,recuentos,arranque,negativos,evidencia}; do
  python3 kernel/operativo/validadores/$v.py; done
```

---

### 4 · Comprobaciones independientes: derivado frente a declarado

| # | qué | declarado | **derivado por mí** | veredicto |
|---|---|---|---|---|
| 1 | fases transaccionales | 5 (§3.6 L3574) / **6** (L513, L3327, L3639) | **5** — `preparada`·`confirmada`·`conflicto`·`abandonada`·`derivada` | **NO CUADRA**: tres sedes declaran 6 |
| 2 | terminales | **2** (§2.6.1 L547) / **1** (L449, L986, L2514) | **2** | **NO CUADRA** |
| 3 | transiciones admitidas | 6 (`D64`) | 6 filas (1 inicial + 5 reales) | CUADRA |
| 4 | estados no terminales sin sucesor **en el grafo** | 0 | 0 — `preparada`→2, `conflicto`→2, `confirmada`→1 | CUADRA |
| 5 | filas del contrato condicional fase a fase | **8** (L3639) | **7** (5 fases + `deriva` + `fallo`) | **NO CUADRA** |
| 6 | valores de `evento.tipo` | 9 | 9 | CUADRA |
| 7 | estados del campo `fase` | 6 (L3574) / **7** (L3328) | **6** (5 + ausencia) | **NO CUADRA** |
| 8 | espacio bruto `tipo`×`fase` | 54 | 9×6 = **54** | CUADRA |
| 9 | combinaciones válidas | 34 | 25+6+1+1+1 = **34** | CUADRA |
| 10 | combinaciones prohibidas | 20 | 5+0+5+5+5 = **20** | CUADRA (34+20=54, partición cierra) |
| 11 | valores de `deriva.causa` | **2** (§3.6 L3659) / **3** (§2.6.11 L2203) | **3** son necesarios | **NO CUADRA** |
| 12 | ventanas de caída | 17 | W1–W11 + W12a/W12b + W13–W16 = **17** | CUADRA |
| 13 | filas adversariales `X<nn>` | 42 filas / 42 ids | **42 / 42**; huecos `X24`, `X29`–`X36`, `X40`–`X46` | CUADRA |
| 14 | ventanas `R1`–`R9` | retiradas (L968) / **vigentes** (L2816, L7060) | retiradas | **NO CUADRA** |
| 15 | esquemas vigentes | 19 | **19** `.yaml` en `esquemas/` | CUADRA |
| 16 | recuento total de tipos | 19+4+2 = 25 | **25** | CUADRA |
| 17 | presiones normativas vigentes | **10** (§16 L6871, §19 L7073) / **8** (§0 L100) | **10** (PN-1,2,3,6–12) | **NO CUADRA** |
| 18 | decisiones registradas en §15.8 | `D16`–`D70` implícito | **`D16`–`D63` + `D69`–`D70`; faltan `D64`–`D68`** | **NO CUADRA** |
| 19 | los cinco conceptos de `a.9` | correcto en §3.6 / **incorrecto en §2.6.10 L1917** | `a.9` L673–679, verificado literal | **NO CUADRA** |
| 20 | `C7.aplica_a` | «una o más fuentes» | **literal en C7 L170** | CUADRA — la denuncia de §9.5 es exacta |
| 21 | `integration-set.yaml` `restaura_a` obligatorio, `resultado: no-aplica` | sí | **verificado L5, L35, L40** | CUADRA |

---

### 5 · Hallazgos

#### BLOQUEANTES

---

**`A1` · El contrato de `evento` no puede representar el segundo terminal: `abandonada` es inemitible como está escrito — BLOQUEANTE**

`D64` cierra `B1` dando a `conflicto` una segunda salida, `abandonada`, cuyo bloqueo pasa a un evento `deriva`. §3.6 —**la sede del contrato del que F6 deriva el esquema**— no puede representar ese `deriva`. Tres afirmaciones dentro de §3.6 se contradicen entre sí:

> `11-ARQUITECTURA-INTEGRADA.md` **L3659** (tabla del contrato condicional, fila `deriva`):
> «`causa` ∈ {`posterior-al-cierre`,`sin-transaccion`} · … · `tx_afectada` **sólo si `causa: posterior-al-cierre`**»

> `11-ARQUITECTURA-INTEGRADA.md` **L3622** (combinaciones prohibidas):
> «`tx_afectada` sin `causa: posterior-al-cierre`   ESQUEMA ESTRUCTURAL»

> `11-ARQUITECTURA-INTEGRADA.md` **L3745** (lo que el esquema estructural comprueba):
> «que en `deriva` el `tx_afectada` sólo aparezca con `causa: posterior-al-cierre` **o `abandono-de-transaccion`**»

Y §2.6.11, la prosa del protocolo, declara **tres** valores:

> **L2203–2211**: «`causa` · `posterior-al-cierre` … · `sin-transaccion` … · `abandono-de-transaccion` **añadida por `D64`** … es lo que conserva el bloqueo cuando el marcador se retira»

**Por qué es defecto.** La fila `abandonada` de la misma tabla (**L3657**) declara `deriva_emitida` **obligatorio**: «`deriva_emitida` = `id` del `deriva` que conserva el bloqueo». Ese `deriva` es, por §2.6.4 paso 0 (**L814**) y por `X55` (**L1293**), un `deriva` con `causa: abandono-de-transaccion` que **referencia la transacción abandonada**. Contra el enum de L3659 su `causa` está fuera de dominio; contra la regla de L3622 su `tx_afectada` es rechazado por el esquema estructural. Un esquema derivado literalmente de §3.6 **rechaza el único registro que hace emitible `abandonada`**, y con ello el segundo terminal —la corrección entera de `D64`— deja de existir en el contrato. No es una errata: hay **dos sedes editables** para el mismo enum (§2.6.11 y §3.6) que dicen cosas distintas, lo que viola además `I5` y la regla de fuente única de §1.3.

**Qué exigiría cerrarlo.** Que §3.6 L3659 declare el enum de tres valores, que L3622 admita `tx_afectada` con `abandono-de-transaccion`, y que la sede del enum sea **una sola** —§3.6— con §2.6.11 remitiendo a ella en vez de redeclararla.

---

**`A2` · El predicado de «transacción abierta» sigue siendo «sin `derivada`» en las dos reglas operativas, y eso reinstaura el bloqueo global que `D64` dice haber eliminado en su raíz — BLOQUEANTE**

`D64` introduce un segundo terminal. El predicado que decide si una transacción sigue abierta **no se propagó**. Sigue formulado como «sin evento `derivada`» en siete sitios vigentes, de los cuales **dos son operativos**:

> `11-ARQUITECTURA-INTEGRADA.md` **L2514** (§2.9, tabla de reconstrucción):
> «| el marcador `estado/tx/<TX>.abierta` | el diario: una transacción **sin evento `derivada`** | total. … Con `derivada` como **único terminal** (§2.6.1), **la condición es UNA** |»

> `11-ARQUITECTURA-INTEGRADA.md` **L5018** (§7.4, `Continúa` paso 2):
> «· ¿hay transacciones **sin evento `derivada`**?  → completar, o marcar conflicto»

Y en los otros cinco: **L449** (§2.5, «sin evento `derivada`, que es el único terminal»), **L819** (§2.6.4 paso 1), **L1144/L1160** (§2.6.6, partición binaria ABIERTA/CERRADA sobre `derivada`), **L1405** (§2.6.8), **L2185** (§2.6.11). Más **L986**:

> **L986** (`W8`): «se borra el marcador. Idempotente. **`derivada` es el único terminal**, luego «cerrada» y «terminal» vuelven a coincidir (§2.6.1)»

**Por qué es defecto.** Una transacción cerrada por `abandonada` **no tiene `derivada`**. Por tanto:

1. **§2.9 L2514 reconstruye su marcador.** El marcador que `abandonada` acaba de retirar (§2.6.9, paso E) vuelve a nacer en el siguiente arranque, y como la transacción nunca tendrá `derivada`, **nunca se vuelve a retirar**. Por la regla de commit de §2.6.6 —«ADS nunca hace commit de un árbol con una transacción abierta»— el control repo **deja de commitear para todo el producto, indefinidamente**. Es exactamente el modo de fallo que `B1` clasificó como bloqueante y que `D64` afirma eliminar «en su raíz» (**L1043–1046**).
2. **§7.4 L5018 dirige `Continúa` a «completar, o marcar conflicto»** sobre una transacción que ya tiene terminal, lo que §2.6.1 prohíbe con todas las letras: «**NINGUNA transición sale de un terminal**» (**L549**) y `X57` exige que no exista ningún evento con `fase` cuyo `tx` ya cerró (**L1295**).

§2.6.4 se salva **sólo** porque su paso 0 (L811–817) comprueba «un terminal durable —`derivada` o `abandonada`—» **antes** que el paso 1 defectuoso. §2.9 y §7.4 no tienen esa guarda.

**Qué exigiría cerrarlo.** Un predicado **único y nombrado** —`abierta(tx) ≡ existe `preparada` durable ∧ no existe terminal ∈ {`derivada`,`abandonada`}`— declarado una sola vez y referenciado desde los siete sitios; retirar «único terminal» de L449, L986 y L2514; y corregir §7.4 L5018.

---

#### GRAVES

---

**`A3` · §7.4 `Continúa` declara en voz normativa un diseño que `D69` retiró — GRAVE**

> `11-ARQUITECTURA-INTEGRADA.md` **L5008–5013**: «Donde (b) escribe *«completar o REVERTIR (a.9)»*, esta arquitectura escribe *«completar o marcar conflicto»*, y **§2.6 elimina el ramal de reversión por completo**. … La decisión de *roll-forward only* es buena y está argumentada en §2.6.2 … La desviación queda registrada como presión normativa `PN-7` en §16, y **no se resuelve aquí**.»

Contra §2.6.9, que dice lo contrario:

> **L1601** (título de la Salida 2): «**LA AUTORIDAD ABANDONA — y abandonar es RESTAURAR**, no «cerrar dejando lo aplicado»»
> **L1643**: «**Y por eso `abandonada` ES la rama «revertir» de `b.14`**, no un tercer desenlace … y `PN-7` **se reformula** en consecuencia (§16)»
> **L1648–1653**: «QUÉ SE RETIRA DE «ROLL-FORWARD ONLY»: la afirmación … **como absoluto** … el estado ESPECULATIVO **sí se revierte**»

Y contra el propio `PN-7` reformulado (**L6717–6722**): «**REFORMULADO por `D69`.** §2.6 tenía sólo ROLL-FORWARD … Ahora tiene **LAS DOS RAMAS**».

Además el resumen de §16 repite la formulación retirada:

> **L6876**: «PN-7   b.14 paso 2 dice «completar o revertir», y **§2.6 sólo completa**        NUEVA»

**Por qué es defecto.** §7.4 es la sección que implementa `b.14`, el punto de entrada operativo del runtime. Declara retirado un ramal que §2.6.9 exige, su paso 2 omite la salida de abandono/restauración, y su nota de desviación describe una presión normativa que ya no está vigente en esa forma. Un lector de §7.4 construiría un `Continúa` sin capacidad de abandonar.

**Qué exigiría cerrarlo.** Reescribir §7.4 contra `D69`: paso 2 con las dos ramas y el predicado correcto de `A2`, retirada de «§2.6 elimina el ramal de reversión por completo» y de «roll-forward only es buena» como absolutos, y alineación de L6876 con el cuerpo de `PN-7`.

---

**`A4` · El aparato de trazabilidad del entregable va un ciclo por detrás de su cuerpo normativo: `D64`–`D68` no están registradas, y la tercera revisión independiente no consta — GRAVE**

Derivado con `grep -n '| \`D6[4-8]\` |' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` → **salida vacía**. §15.8 pasa del bloque `D63` (L6521–6528) directamente a `D69`–`D70` (L6530).

> **L6530–6533**: «### `D69`–`D70` · las decisiones de la corrección previa al gate — Comprobación adversarial de sólo lectura **sobre la tanda anterior**. Sus seis defectos eran **todos propios de esa tanda** … **`D16`–`D68` conservan su texto**.»

«La tanda anterior» y `D64`–`D68` **no se introducen en ninguna parte de §15.8**, y las columnas «qué revisa» de `D69` y `D70` citan `D64` y `D65` (**L6538–6539**) como referencias colgantes. `D64` se invoca **26 veces** en el cuerpo del documento y es la decisión sobre la que descansa todo §2.6.

La cabecera arrastra el mismo desfase:

> **L12**: «**F4 no está certificada, y este texto ha sido CORREGIDO DOS VECES.**»
> **L59–62**: «Es el SÉPTIMO encadenamiento consecutivo … `F4c` sigue **ABIERTA**, **pendiente de una tercera revisión independiente**.»

La tabla de la cabecera (L14–48) **no registra** ni la tercera revisión independiente (`15-TERCERA-REVISION-INDEPENDIENTE-F4C.md`, que produjo `D64`–`D68`) ni la comprobación adversarial previa al gate (`D69`–`D70`). §19 lo repite:

> **L7079–7082**: «DOS críticas independientes y UNA devolución técnica la han devuelto … `F4c` sigue ABIERTA, **pendiente de una TERCERA REVISIÓN INDEPENDIENTE**»

— y se contradice cuatro líneas antes consigo mismo: **L7073** dice «tras DOS devoluciones independientes **y la TERCERA REVISIÓN**».

**Por qué es defecto.** §15 existe para que cada decisión de la fase sea verificable. Un adjudicador que lea la cabecera, §15.8 y §19 concluiría que la tercera revisión no ha ocurrido y que `D64`–`D68` no existen — precisamente la tanda que un gate necesita auditar. La información no se ha perdido (está en `DECISIONES-Y-CONTRADICCIONES.md` L222–238, verificado), pero §15.8 se declara su espejo y está incompleto. El último commit (`d3bf543`, «cabecera, §19 y el índice reanclados») no cerró esto.

**Qué exigiría cerrarlo.** Bloque `D64`–`D68` en §15.8; dos filas nuevas en la tabla de la cabecera; corregir «CORREGIDO DOS VECES»; y retirar de L62 y L7081 la afirmación de que la tercera revisión está pendiente.

---

**`A5` · El commit del incidente se declara a la vez con y sin los hashes esperados — GRAVE**

> `11-ARQUITECTURA-INTEGRADA.md` **L1632–1640** (§2.6.9, «Qué contiene exactamente el commit del incidente»):
> ```
> LLEVA    · el estado canónico RESTAURADO A LA BASE …
>          · el evento `preparada`
>          · los eventos `conflicto` …
>          · el evento `abandonada` …
>          · el evento `deriva`
>
> NO LLEVA **ningún `hash_posterior_esperado`**. Ni uno. El conjunto publicable es la BASE
>          CONSISTENTE MÁS EL INCIDENTE, nunca la mezcla parcial.
> ```

Y §3.6 hace ese campo **obligatorio** dentro de `preparada`:

> **L3654**: «| `preparada` | … | `afecta[]` con `ruta`·`hash_previo`·**`hash_posterior_esperado`**·`orden`· … | campos OBLIGATORIOS |»

**Por qué es defecto.** Las dos líneas del mismo bloque se contradicen: el commit lleva `preparada`, y `preparada` contiene por contrato al menos un `hash_posterior_esperado`. Leído literalmente, «ni uno» obligaría a **despojar el evento `preparada` de sus hashes esperados antes de commitear**, lo que rompe tres cosas a la vez: (i) §2.3 L—«`<EV-ID>.md` **SE EMITEN, NO SE EDITAN**. Con UNA excepción física autorizada: la lápida de `retirada-de-cuerpo`»; (ii) la identidad `id = EV-H(evento MENOS id)` de §2.8 punto 4, que dejaría de reproducir el `id`; y (iii) la propia verificación de `abandonada`, que se audita comparando lo restaurado contra `revision_base` **y contra la intención declarada**. Es la degradación de trazabilidad exacta: `preparada` debe conservar sus `hash_posterior_esperado` **como registro de la INTENCIÓN**, y «el commit no lleva estado posterior parcial» es una afirmación sobre los **ficheros canónicos**, no sobre los **campos del evento**. El texto afirma las dos cosas a la vez y no distingue los dos sujetos.

**Qué exigiría cerrarlo.** Reformular L1639 sobre el sujeto correcto: «**ningún fichero canónico en su `hash_posterior_esperado`**. El evento `preparada` **sí conserva** los suyos, como registro de la intención que no se alcanzó».

---

#### MEDIOS

---

**`A6` · Tres sedes vigentes declaran seis fases y ocho filas donde el recuento derivado da cinco y siete — MEDIO**

> **L513** (título de §2.6.1): «### 2.6.1 · El autómata de fases — **seis fases, dos rutas, un solo cierre**»
> **L3327–3328**: «**Las fases son SEIS**; los estados del campo, **SIETE** contando su ausencia; y `orden` es **condicional**. `D57` conserva su texto.»
> **L3637–3640**: «Sus **seis primeras filas son las seis FASES** … **La tabla tiene ocho filas y el eje `fase` tiene seis valores**»

Contra el recuento derivado de la propia tabla:

> **L3568–3574**: «FASES TRANSACCIONALES **5** … ESTADOS DEL CAMPO `fase` **6** — las CINCO fases, más la AUSENCIA»

Mi conteo de la tabla de L3654–3660: **7 filas** (`preparada`, `confirmada`, `conflicto`, `abandonada`, `derivada`, `deriva`, `fallo`), de las cuales **5** son fases.

**Por qué es defecto.** El título de §2.6.1 miente en sus dos mitades («seis fases» y «un solo cierre»), y el preámbulo normativo del contrato condicional describe mal la tabla que introduce. §3.8 declara explícitamente que el recuento se **deriva** y «no se conserva ninguno por arrastre» (L3583) — aquí sí se arrastran tres.

**Qué exigiría cerrarlo.** L513 → «cinco fases, dos rutas, dos cierres»; L3327–3328 y L3637–3640 → 5 fases, 6 estados del campo, 7 filas.

---

**`A7` · `D66` corrige los cinco conceptos de `a.9` en §3.6 y no los corrige en §2.6.10, que es una de las dos sedes que la tercera revisión nombró — MEDIO**

Verificado literal contra la fuente aprobada:

> `docs/rediseno/a-CAPACIDADES-APROBADA.md` **L673–679**: «Cinco conceptos que **NO DEBEN** confundirse …: **PROPIETARIO DEL CAMPO · AUTORIDAD · ORDENANTE · ESCRITOR DEL COMANDO · EJECUTOR DE MUTACIÓN**»

§3.6 lo resuelve bien y con motivo declarado (L3268–3298: cinco **conceptos**, cuatro persistidos, `propietario del campo` **derivado** de §1.3, `actor_atribuido` **aparte**). Pero:

> `11-ARQUITECTURA-INTEGRADA.md` **L1916–1918** (§2.6.10, regla 1): «EL COMMIT LOCAL SE HACE, y emite su evento con los **CINCO conceptos de `a.9`**: ordenante · autoridad · escritor_del_comando · ejecutor · **actor_atribuido**. La ausencia de cualquiera de los cinco es un FALLO DEL VALIDADOR, no un silencio.»

Es la formulación exacta que `G1` condenó, y la tercera revisión nombró **«`X39` y la regla 1 de §2.6.10»** como los dos sitios que la convierten en condición de validación. Uno se corrigió; el otro no.

**Qué exigiría cerrarlo.** Alinear L1917 con §3.6: «los cinco **campos** de procedencia (§3.6)», no «los cinco conceptos de `a.9`».

---

**`A8` · La única justificación del marcador queda anulada por la regla 2bis de la misma sección — MEDIO (proporcionalidad)**

El marcador `estado/tx/<TX>.abierta` es, por declaración propia, «**un acelerador, no una verdad**» (L2514) y reconstruible desde el diario. Su única razón de existir es evitar reproyectar el diario:

> **L1394–1400** (§2.6.8): «F4c obligaba a recorrer `estado/eventos/` para saber QUÉ ficheros estaban en vuelo — es decir, a **REPROYECTAR EL DIARIO** … que es exactamente el coste con el que §2.2 descarta la alternativa C. **F4 pagaba el coste de C sin haber elegido C**.»

Pero la regla de lectura, en la misma sección, obliga ahora a hacer exactamente eso:

> **L1372–1373**: «1  ANTES DE LEER EL ESTADO CANÓNICO, se comprueban **DOS cosas**: los marcadores de `estado/tx/` y **los eventos `deriva` SIN REPARAR del diario**.»

**Por qué es defecto.** Determinar «`deriva` sin reparar» exige, por el predicado de L1690–1693, cruzar **todos** los `deriva` contra **todas** las `derivada` que llevan `resuelve_deriva` — una proyección completa del diario, estrictamente **más cara** que el barrido de marcadores que el marcador existía para evitar. La regla está dirigida a «TODO lector —humano, agente o herramienta, sea o no el runtime» y el índice SQLite está declarado no canónico y operacional, luego no puede invocarse como atajo. El marcador conserva valor (acota qué rutas mirar), pero **el argumento escrito que lo justifica ya no se sostiene**, y §2.2 usa ese mismo coste para descartar la alternativa C.

**Qué exigiría cerrarlo.** O un artefacto derivado equivalente para los `deriva` sin reparar, legible sin herramienta y sujeto a la misma disciplina que el marcador; o rehacer la justificación del marcador sobre lo que de verdad compra (acotar el alcance), retirando el argumento de «no reproyectar el diario».

---

**`A9` · El desenlace `4b` no tiene salida material garantizada y su radio de daño es global; `X58` exige un resultado más fuerte del que el análisis material sostiene — MEDIO**

> **L1862–1866** (desenlace 4b): «no puede completar, y **no puede preservar la divergencia o restaurar la base** … PERMANECE ABIERTA · marcador VIVO · **NO HAY COMMIT** · exige intervención EN LA MISMA MÁQUINA. **No es un estado sin salida**: sus salidas son las tres de arriba, y lo que falta es una condición material, no una transición»
> **L1774–1778**: «SI LO DIVERGENTE NO ES PUBLICABLE — **`SEG` bloquea su publicación** … la transacción **NO puede declararse abandonada hasta que exista una forma autorizada de preservar lo necesario**. Sin preservación autorizada, el desenlace es el cuarto: sigue abierta.»
> **L1296** (`X58`): «**no existe ninguno** … **Ninguna transacción puede quedar reteniéndolo para siempre**»

**Por qué es defecto.** En el grafo la afirmación es cierta y la verifiqué (§4, fila 4). Materialmente no lo es: **ambas** salidas de `conflicto` están condicionadas a hechos fuera del control del sistema —que el mundo revierta la divergencia, o que `SEG` autorice preservarla—, y ninguna autoridad está facultada para desempatar. Mientras 4b dura, el marcador vive y por §2.6.6 el control repo **no commitea para todo el producto**, que es el radio de daño global que `B1` clasificó como bloqueante y que la sección de CONTENCIÓN (L1707–1712) dice haber acotado. La tabla de proporcionalidad lo afirma sin la condición:

> **L1457**: «| el bloqueo persiste hasta que se repara | **sí, y mejor acotado** | pasa del marcador —que bloqueaba el commit de TODO el producto— al `deriva`, que bloquea los items que nombra |»

El traspaso al `deriva` sólo ocurre **después** de `abandonada`. Mientras hay un `conflicto` abierto —o mientras dura 4b— el bloqueo del commit sigue siendo global y sin tope declarado (`observacion` es explícitamente «SIN TOPE», L1553).

**Qué exigiría cerrarlo.** O una autoridad nombrada que pueda cerrar 4b (p. ej. el Owner autorizando el abandono con preservación degradada y evidencia de la degradación), o reformular `X58` y L1457 para que digan lo que el diseño sostiene: el bloqueo está acotado **por acto de autoridad**, no por construcción.

---

**`A10` · El resumen ejecutivo subestima en dos las aprobaciones que el Owner debe conceder — MEDIO**

> **L100** (§0, «Para el Owner, sin vocabulario interno»): «LAS ENMIENDAS   este diseño presiona material aprobado en **OCHO puntos**, tras **dos devoluciones independientes**.»

Derivado con `grep -n '^## \`PN-'`: 12 bloques, `PN-4` RETIRADA y `PN-5` FUSIONADA → **10 vigentes**. Coincide con las otras dos sedes:

> **L6871** (§16): «VIGENTES · **DIEZ**»
> **L7073** (§19): «**DIEZ** PRESIONES NORMATIVAS VIGENTES … tras DOS devoluciones independientes **y la TERCERA REVISIÓN**»

**Por qué es defecto.** §0 es la única sección escrita para el Owner, y `PN-1` bloquea todo el estado durable. Un recuento bajo en la sección de decisión es peor que en la técnica.

**Qué exigiría cerrarlo.** L100 → «DIEZ puntos, tras dos devoluciones independientes, una devolución técnica y una tercera revisión independiente».

---

#### MENORES

---

**`A11` · Dos sedes vigentes citan las nueve ventanas `R1`–`R9` como contrato de prueba existente — MENOR**

> **L2816**: «**Ninguna se ha ejecutado**, como las cuarenta y dos de §2.6.7 y **las nueve `R1`–`R9`**.»
> **L7060** (§19): «las CUARENTA Y DOS filas de la tabla adversarial de §2.6.7, **las NUEVE ventanas `R1`–`R9` de §2.6.9**»

Contra su retirada declarada dos veces:

> **L968**: «**las nueve `R1`–`R9` de la reconciliación se retiran** con la ruta larga (`D64`)»
> **L1348**: «**Las nueve ventanas `R1`–`R9` se retiran** con la ruta de reconciliación (`D64`)»

§19 es la sección que inventaría lo escrito y no probado; inflarla con nueve contratos inexistentes la hace inservible como base del gate.

---

**`A12` · «Un único escritor» se ofrece como protección de una rama compartida, y el propio documento declara que es local a la máquina — MENOR**

> **L2041–2043** (§2.6.10): «Lo que SÍ la protege es otra cosa: **un único escritor** (`R5`), **commits sólo entre transacciones** (§2.6.6) y **push bajo autoridad**.» (idéntico en **L1929**)

Contra §2.7:

> **L2277–2280**: «`.ads/run/lock` … **Vive en el plano operacional a propósito: un lock versionado en Git sería un lock que viaja a otra máquina**»
> **L2312–2313**: «no depende de un lock que sólo existe en una máquina, y **`R5` es un requisito del runtime local, no del producto**»

**Respuesta a la pregunta del encargo:** «único escritor» es una regla **comprobable sólo por worktree** —lock con identidad de proceso y latido, con reclamación registrada—, y **no es comprobable entre máquinas**. El documento lo dice honestamente en la regla 5 de §2.6.10 (L1936–1942: «dos máquinas sobre el mismo control repo son un caso **POSIBLE y no gobernado**»). Lo que realmente serializa `main` es el **CAS de Git** (rechazo non-fast-forward), que sí figura aparte. El defecto es sólo que L2041 lo lista entre las protecciones de la rama canónica, que es una propiedad entre máquinas que el lock no da.

---

**`A13` · La fila `preparada` de §3.6 sigue etiquetando su lista obligatoria como «los cinco de `a.9`» — MENOR**

> **L3654**: «| `preparada` | … | `afecta[]` … · **los cinco de `a.9`** · `base` |»

`D66` acaba de establecer (L3296–3298) que el evento lleva **cinco CAMPOS** —`ordenante`, `autoridad`, `escritor_del_comando`, `ejecutor`, `actor_atribuido`— que **no son** los cinco conceptos de `a.9`, porque `propietario del campo` se deriva y `actor_atribuido` pertenece a otra lista. La etiqueta de L3654 es la que `D66` acaba de declarar engañosa.

---

**`A14` · La versión mínima de Python está declarada sólo en una cadena de documentación, y sin ella dos pruebas de certificación fallan con un mensaje que parece un defecto del producto — MENOR**

Ejecutado en este entorno (Python **3.10.12**):

```
comprobar_fuentes.py   → T159  FALLIDA
  · kernel/operativo/plantillas/SOURCES.toml: se requiere Python 3.11 o superior para leer TOML
comprobar_arranque.py  → T148  FALLIDA (4 proyectos: workspace check exit 1, "schema": null)
```

La exigencia sólo consta aquí:

> `tooling/workspace.py` **L21–22**: «`SOURCES.toml` se lee con `tomllib`, que es estándar desde Python 3.11: leer el manifiesto NO introduce ninguna dependencia.»

No hay comprobación previa de versión en `tooling/new-project.sh` ni en los validadores, y ningún fichero declara `python_requires`. `workspace.py` degrada limpiamente (L47–49, L433–435), lo que es correcto — pero el resultado sube a la capa de certificación como **prueba fallida**, indistinguible de un defecto real.

---

### 6 · Hallazgos que intenté y NO pude reproducir

Esta lista es parte del entregable. Ninguno de los siguientes es un hallazgo.

| # | qué busqué | resultado | motivo |
|---|---|---|---|
| 1 | Alguna frase **vigente** que prometa recuperación distribuida exacta del estado abierto | **NO EXISTE** | §2.6.6 L1808–1812 dice «**NO EXISTE REANUDACIÓN EXACTA** … esto es **REINICIO SEGURO, no reanudación**, y no se llama de otra manera»; §2.6.10 L2000 «SE SACRIFICA la **REANUDACIÓN EXACTA DISTRIBUIDA**». `D70` la retiró y la retirada está completa. **Las tres garantías A/B/C de la comprobación 5 están demostradas** (L1791–1812) |
| 2 | Segunda sede editable para prioridad y aparcado | **NO EXISTE** | §1.3 L200–216 lo cierra con tres reglas correctas: la orden es canal de comandos, `02-control.md` es el campo canónico, el runtime es el único ejecutor. Verificado contra `a.9` L692–697, que dice lo mismo |
| 3 | Autorización de `--force` en alguna ruta | **NO EXISTE** | L2115–2118: «**PROHIBIDO.** Sin excepción automática … Ninguna recuperación, ningún reintento y ninguna política lo autorizan». Coherente en L1930–1932 y en el ramal de `fallo` de `W15` |
| 4 | `X32`–`X34` y `X42` citados sin existir (hallazgo `M2`) | **NO REPRODUCIDO** | Reasignados a `X51` (L4917) y la nota de huecos (L1323–1326) declara los huecos correctamente. **Mi conteo independiente confirma 42 filas / 42 ids** con huecos `X24`, `X29`–`X36`, `X40`–`X46` |
| 5 | Dos filas `X28` idénticas / «Un fichero que no existe» duplicado | **NO REPRODUCIDO** | Confirmado por conteo propio, coincide con lo que L1332–1341 declara |
| 6 | Que `C7` haya sido modificado en esta pasada pese a declararse intocado | **NO OCURRIÓ** | `C7` L170 conserva literalmente `aplica_a: "todo item cuyos paquetes escribieron en una o más fuentes"`. La denuncia de §9.5 es **exacta** y la abstención de tocarlo es **coherente** |
| 7 | Doble sede `C7`/`C8` para el gobierno Git del control repo | **NO EXISTE** | `O16` (DECISIONES L290–310) y §16 `PN-11` (L6823–6828) separan limpiamente autoridad normativa `(g)` y contrato derivado `C8` en F6; `C7` queda acotado a las sources |
| 8 | Que `estado/tx/` o `.ads/run/` estuvieran provisionados en `tooling/` o `kernel/` contra lo declarado | **NADA PROVISIONADO** | Consistente con «NADA ESTÁ CONSTRUIDO» (§19). No es defecto en una fase de diseño |
| 9 | Ejecutar `tooling/tests/test_workspace.py` | **NO PUDE** | `pytest` no está instalado en este entorno. No he leído el fichero ni puedo afirmar nada sobre su cobertura |
| 10 | Que `A1` (enum de `causa`) falle en algún validador o esquema real | **NO PUDE DEMOSTRARLO EN EJECUCIÓN** | **No existe `esquemas/evento.yaml`** ni ningún validador del diario: `grep` sobre `esquemas/` y `validadores/` no devuelve una sola referencia a `preparada`/`confirmada`/`abandonada`. La contradicción es **textual y verificable**, pero por diseño de la fase no es ejecutable |

---

### 7 · Limitaciones de mi revisión

```text
1  NO he leído §4, §5 (salvo §5.7), §8, §11, §12, §13, §14, §17 ni §18 del entregable.
   Quedan fuera de mi eje y no afirmo nada sobre ellos.

2  NO he leído `C1`, `C2`, `C3`, `C5` completos, ni `test_workspace.py`, ni los
   validadores línea a línea. Los ejecuté; no los audité.

3  NADA de lo que revisé está implementado. No hay esquema de `evento`, ni validador del
   diario, ni runtime. Todos mis hallazgos sobre el protocolo son sobre TEXTO, y ninguno
   pude confirmarlo ni desmentirlo con una ejecución. Un contrato contradictorio no es lo
   mismo que un sistema roto: es un sistema que no se puede construir sin decidir cuál de
   las dos frases vale.

4  Dos pruebas del corpus (T148, T159) no pudieron evaluarse por la versión de Python de
   este entorno. NO afirmo que pasarían en 3.11; afirmo que su fallo aquí no es
   atribuible al entregable.

5  Verifiqué `a.9` y `b.14` en los tramos citados por el entregable, no íntegros. Una cita
   correcta de un tramo no garantiza que otro tramo no diga lo contrario.

6  NO he consultado al REVISOR B ni conozco su eje ni sus hallazgos.

7  He derivado todos los recuentos que declaro (§4). Donde escribo CUADRA, lo conté.
   Donde escribo NO CUADRA, lo conté y difiere.
```

---

### 8 · Nota sobre lo que sí está bien, porque un dictamen que sólo lista defectos no es una medida

Lo digo porque afecta a la recomendación. **`D69` y `D70` son correcciones sustantivas y bien hechas**: la separación estable/especulativo (§2.6.0), el procedimiento de cinco pasos de `abandonada` con verificación **byte a byte** contra `revision_base` (§2.6.9 A–E), y las tres garantías de recuperación (§2.6.6 A/B/C) responden **completamente** a las comprobaciones 3 y 5 del encargo. **`D63` responde completamente a la comprobación 8**: identidad normal, excepción tipada, tres niveles, fuente de recuperación comprobada antes de retirar, referencia estructural frente a dependencia semántica, y el reconocimiento explícito de que el diario físico no es append-only. **`D65` responde a la comprobación 6** en trece de sus catorce puntos. Y la **matriz de §3.6 cuadra exactamente** en su aritmética (34 · 20 · 54), derivada por mí sin fiarme del titular.

El patrón de todos mis hallazgos bloqueantes y graves es **el mismo y es uno solo**: `D64` y `D69` son correcciones profundas cuya propagación al resto del documento quedó incompleta. No encontré ninguna decisión mal tomada; encontré decisiones bien tomadas y **aplicadas a la mitad de los sitios que las invocan**.

---

### 9 · Recomendación de veredicto

**INSUFICIENTE PARA F5** — por `A1` y `A2`, que dejan el segundo terminal irrepresentable en el contrato de `evento` y reinstauran en §2.9 y §7.4 el bloqueo global del control repo que `D64` declara eliminado en su raíz; y por `A4`, que deja `D64`–`D68` y la tercera revisión fuera del aparato de trazabilidad del propio entregable.

*No soy quien emite este veredicto.* Lo emite el adjudicador C, que verificará cada cita de arriba contra su fichero y su línea. Señalo que los catorce hallazgos son **de propagación, no de concepción**: ninguno exige una decisión arquitectónica nueva, y los dos bloqueantes se cierran alineando enums y un predicado que el propio documento ya define correctamente en §2.6.11 y en el paso 0 de §2.6.4.

---

## DICTAMEN DEL REVISOR B

### 1 · Identidad y procedencia

Soy el **REVISOR B** del gate final independiente de `F4c`. Trabajo sobre `/home/jose/ads-kernel`, rama `redesign/kernel-2.0`, **HEAD `a713590a9a1d2d0f6d0a3c5942f81a8052630ed5`**, árbol limpio (`git status` sin cambios).

**Qué NO soy.** No escribí `F4`, ni `F4b`, ni `F4c`. No apliqué ninguna de sus correcciones ni de sus siete comprobaciones técnicas encadenadas. No participé en `D16`–`D70` ni en la redacción de `O7`–`O16`. No soy el REVISOR A: **no he auditado el autómata transaccional en detalle**, y donde un hallazgo mío roza §2.6 lo marco como posible solapamiento. **No soy el adjudicador**: no emito el veredicto, lo recomiendo.

**Modo.** Sólo lectura. No he modificado ningún fichero, no he hecho commits ni ninguna escritura de git. Mi única entrada ha sido el árbol del repositorio en ese HEAD.

**Regla que he aplicado sin excepción.** Ningún informe, checkpoint, changelog, mensaje de commit ni revisión anterior ha sido fuente. `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` y `CHECKPOINT-ADS-NEXT.md` los he tratado como **objeto**, no como verdad: no cito ni uno solo de sus veredictos como apoyo de un hallazgo mío. Toda cita de este dictamen está abierta en su fichero original y verificada por línea.

---

### 2 · Corpus realmente leído

#### Íntegro

| fichero | qué cubre |
|---|---|
| `kernel/operativo/capacidades/{APR,ARQ,CON,DIS,DOM,DSP,ENC,ENT,INV,PLT,PRD,SEG,SIS,USO,VER}/CAPACIDAD.md` | **LAS QUINCE, completas.** Ninguna omitida |
| `kernel/operativo/recorrido/01-PROCESOS.md` (564 l.) | **LOS DIEZ procesos, completos** |
| `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` (130 l.) | seis conceptos, matriz de autoridad, `gate:cierre-de-item` |
| `kernel/operativo/circuitos/00-CIRCUITOS.md` (240 l.) | los diez circuitos y los dos que (b) no numera |
| `kernel/operativo/plantillas/CIERRE.md` | íntegro |
| `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` §1 y §2 (L1–380) | `D1`–`D70` y `O1`–`O16`, completos |
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` §1.3 · §2.1–2.2 · §3.1–3.3.1 · §3.5 · §3.7–3.8 · §4.1–4.3 · **§5 entero** · **§6 entero** · **§8 entero** · **§9 entero** · §12 · §13 · §15.1–15.3 · **§16 entero** · §17 · §18 · §19 | mi eje completo |
| `docs/evolucion/ADS-PENDIENTES…` §5.18 · §20.3 · §20.14–20.15 · §26.7 · §26.9–26.10 | los contrastes literales que el gate exige |
| `kernel/operativo/pruebas/RECUENTOS-generado.md` · `REGISTRO.md` · `REGISTRO-generado.md` | recuentos y estado real de pruebas |
| `kernel/KERNEL.md` `G27` y `G28` | verificación literal de las dos reglas duras que F4 invoca |

#### Parcial, y lo digo

`11-ARQUITECTURA-INTEGRADA.md` §2.3–§2.11 (protocolo transaccional — **eje del REVISOR A**, leído sólo §2.1, §2.2, §2.6.5 y §2.6.9 por sus consecuencias de integración), §3.4, §3.6, §7, §10, §11, §14, §15.4–§15.8. · `ADS-NEXT-OWNER-BRIEF.md` (índice íntegro + §6.1–6.3). · `KERNEL.md` (localización de `G03`, `G05`, `G13`, `G22`, `G24`, `G26`, `G29`, `G33`, `G36`, `G52`, `K0.2`, `K0.8`, `K0.10`–`K0.13`; lectura íntegra sólo de `G27` y `G28`). · `entrada/01-TAXONOMIA.md` (cabecera, reglas duras y tabla de nueve clases; dos bloques `ads:entrada` leídos de nueve). · `contratos/C4` (algoritmo) y `C7` (`gate:convergencia-de-fuentes`). · `packs/00-QUE-ES-UN-PACK.md`, `packs/COMPOSICION.md`, `packs/web-app/PACK.md` (cabeceras). · `plantillas/CHECKPOINT.md` e `INTEGRATION-SET.md` (cabeceras). · `DIS/composicion.md` y `DSP/metodos/Supervision.md` (parciales).

#### **Lo que NO cubrí, declarado sin adorno**

- Los **`roles/`, `metodos/`, `prompts/` y `composicion.md`** de las quince capacidades: **no leídos** (salvo los parciales de arriba). Son ~150 ficheros. **Cubrí las quince fichas `CAPACIDAD.md` íntegras, que es lo que el gate exige, pero no su desarrollo operativo.**
- `circuitos/DIS-handoffs.md` y `circuitos/handoffs-generales.md`: **no leídos**. Mi cobertura de «todos los circuitos y handoffs» es por tanto **parcial**.
- `entrada/02-CIRCUITO.md` a `05-ESCENARIOS.md`, `diseno/00-` a `05-`, contratos `C1`, `C2`, `C3`, `C5`, `C6` completos, `docs/owner/`: **no leídos**.
- `ADS-PENDIENTES` fuera de los apartados citados, y `docs/rediseno/(a)`, `(b)`, `E1`, `E2` completos: leídos sólo por `grep` dirigido (`a.7` FRENO 3, `E2.6`).

**Consecuencia para el gate: mi cobertura de las quince capacidades y de los diez procesos es COMPLETA a nivel de ficha y de proceso canónico; mi cobertura de circuitos, handoffs, entrada, diseño y packs es PARCIAL, y el adjudicador debe descontarla.**

---

### 3 · Método y comandos

Todo recuento es **derivado por mí**, nunca copiado.

```bash
# identidad del árbol
git rev-parse HEAD && git status --short

# las quince capacidades: existencia y lectura completa
ls -1 kernel/operativo/capacidades/ | wc -l
for f in kernel/operativo/capacidades/*/CAPACIDAD.md; do cat -n "$f"; done

# los diez procesos, derivados del corpus y no del texto
grep -c '^id: proceso:' kernel/operativo/recorrido/01-PROCESOS.md

# D y O: identificadores realmente definidos en tabla
grep -o '^| D[0-9]\+ ' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md | sort -V
grep -o '^| O[0-9]\+ ' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md | sort -V

# PN: cabeceras reales, no el resumen
grep -n '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md

# recuentos del corpus, derivados por el propio generador y comprobados a mano
cat kernel/operativo/pruebas/RECUENTOS-generado.md
ls -1 kernel/operativo/esquemas/*.yaml | wc -l
grep -c 'tipo: validador' kernel/operativo/validadores/validadores.yaml

# contraste literal de citas contra su fichero original
grep -n 'convergencia-de-fuentes' -A 6 kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md
grep -n 'varias sources' docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md
sed -n '771,795p' docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md   # §5.18
sed -n "$(grep -n '^### G28' kernel/KERNEL.md | cut -d: -f1),+12p" kernel/KERNEL.md

# recuento de las áreas condicionales, por parsing y a mano
python3 -c "...split de la lista de §4.3 y de §5.18..."
```

---

### 4 · Comprobaciones independientes: derivado frente a declarado

| qué | declarado | **derivado por mí** | fuente de la derivación | ¿cuadra? |
|---|---|---|---|---|
| capacidades | quince | **15** (`APR ARQ CON DIS DOM DSP ENC ENT INV PLT PRD SEG SIS USO VER`) | `ls capacidades/` + 15 bloques `ads:capacidad` | **sí** |
| procesos de `b.16` | diez | **10** (`FEA GAP DEF INC INV DEU DEP AUD DIR SIS`) | `grep '^id: proceso:'` | **sí** |
| esquemas vigentes | 19 (§3.8, §17) | **19** | `ls esquemas/*.yaml` | **sí** |
| total de esquemas tras F4 | 25 = 19+4+2 | **25**, aritmética correcta | §3.8 | **sí** |
| validadores | trece (§17) | **13** con `tipo: validador` (+2 generadores, +3 bibliotecas; 16 ficheros `.py`) | `validadores.yaml` | **sí** |
| contratos transversales | siete | **7** (`C1`–`C7`) | `ls contratos/C*.md` | **sí** |
| vetos | cuatro | **4** (`DIS`, `DOM`, `SEG`, `VER`) | bloques `ads:veto` | **sí** |
| decisiones `D` | `D16`–`D68` existen | **`D1`–`D70`**, sin huecos | tabla de `DECISIONES` | **sí, y hay dos más** |
| decisiones `O` | `O1`–`O16` existen | **`O1`–`O16`**, sin huecos | tabla de `DECISIONES` | **sí** |
| PN vigentes | DIEZ (§16 L6871, §19 L7073) | **10** = 12 identificadores − `PN-4` retirada − `PN-5` fusionada | `grep '^## \`PN-'` | **sí** |
| `PN-4` | RETIRADA | **retirada**, con motivo escrito | L6633, L6657 | **sí** |
| `PN-5` | FUSIONADA en `PN-3` | **fusionada**, y `PN-3` la absorbe explícitamente (L6623, L6628) | L6661–6676 | **sí** |
| `PN-7` | «completar o revertir» | **refleja las dos ramas**: `confirmada→derivada` y `abandonada` (`D69`) | L6718–6728 | **sí** |
| `PN-11` | sede `(g)` + `C8` futuro | **`O16`** le da sede: autoridad en `(g)`, `C8` derivado en F6, `C7` intacto | L6821–6828 · `DECISIONES` L282–312 | **sí** |
| `PN-12` | coincide con `O8` | **coincide**: `O8` dice «las doce áreas semánticas del §5.18»; `PN-12` restituye esas doce literalmente | L6844 vs `DECISIONES` O8 | **sí** |
| `O15` vs `O16` | no se contradicen | **no se contradicen**: distinto sujeto (permanencia de la adopción vs. sede del gobierno Git). `PN-11` declara una *dependencia* de `O15`, no un choque | L6829–6831 | **sí** |
| **áreas documentales obligatorias** | doce, literales de `§5.18` | **12, e idénticas una a una** a `§5.18` L775–786 | comparación literal | **sí** |
| **áreas documentales condicionales** | **CATORCE** (§4.3 L4174 y tabla L4191) | **TRECE** en la enumeración de §4.3, y **TRECE** en `§5.18` | parsing y recuento manual | **NO** |
| `O15` no autoriza el inicio | punto 9 | **confirmado tres veces**: `DECISIONES` L121–124, §8.2 L5253, §19 L7068 | lectura literal | **sí** |
| defecto de `C7` que §9.5 denuncia | `aplica_a` «una o más» contra `E2.6` «varias» | **confirmado**: `C7` L170 dice literalmente «una o más fuentes»; `E2.6` L197 dice «varias sources» | ambos ficheros | **sí** |
| escenarios del corpus | — | **95**: 56 `contrato-definido`, 39 `prueba-superada`, 0 ejecutadas pendientes | `REGISTRO-generado.md` | — |
| **presiones vigentes citadas por `O15`** | «las **ocho** presiones normativas vigentes» | **DIEZ** | `DECISIONES` L366 vs §16 L6871 | **NO** |

---

### 5 · Hallazgos por severidad

---

## BLOQUEANTE

### `B-1` · §8.2 y §18 asignan **dos procesos incompatibles** a las mismas fases de la adopción, y la elección determina qué condicionales existen

**Cita 1** — `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L5208–5210** (§8.2, `PARTICIPANTES`):

> `PARTICIPANTES   A2/A3 `AUD` con INV produciendo la capa · A6 activa DOM, SEG,`
> `                DIS/Reconstruccion y PRD, que son LOS CONDICIONALES QUE `proceso:AUD` YA`
> `                DECLARA · A7 ENC · A8 DEU con PLT · A9 SIS+PLT+VER, y SEG si hay superficie`

**Cita 2** — mismo fichero, **L6993** (§18, tabla de `D67`):

> `| | `A2`–`A7` | `proceso:INV` | **`INV`** | `AUD` con `DOM`, `SEG`, `DIS`, `ARQ`, `PRD`, `ENC` | … |`

**Cita 3** — `kernel/operativo/recorrido/01-PROCESOS.md` **L285–293** (`proceso:INV`, `condicionales`):

> `condicionales:`
> `  - capacidad: "CON:experimental"` … `  - capacidad: "PRD"` … `  - capacidad: "ARQ"` … `  - capacidad: "APR"`

**Cita 4** — mismo fichero, **L429–439** (`proceso:AUD`, `condicionales`): `DOM` · `SEG` · `DIS/Reconstruccion` · `PRD` · `APR`.

**Por qué es defecto.** §8.2 justifica la activación de `DOM`, `SEG` y `DIS/Reconstruccion` en `A6` diciendo que **son los condicionales que `proceso:AUD` ya declara**. §18 asigna esas mismas fases a **`proceso:INV`**, cuyos condicionales **no incluyen `DOM`, `SEG` ni `DIS/Reconstruccion`**. Bajo el mapeo de §18, la justificación de §8.2 es falsa y esas tres capacidades **no tienen vehículo normativo** para entrar en la ruta: `b.16` no las declara para `INV`. `proceso:AUD` no aparece **ni una vez** en la tabla de §18, pese a que su `intencion` —«Producir una CONCLUSIÓN sobre un objeto ya existente»— y su `condicion_de_entrada` —«necesita saber en qué estado está algo que ya existe»— describen `A2`/`A3` literalmente, mejor que la de `INV` («producir CONOCIMIENTO que permita decidir algo que hoy no puede decidirse»).

Agrava el hallazgo que §18 declare, **L7002**, que los propietarios globales están *«verificados uno a uno contra `01-PROCESOS.md`»*: la verificación no alcanzó a comprobar que los **condicionales** del proceso elegido cubrieran los participantes que el propio §8.2 declara.

**Y el segundo defecto, dentro del mismo texto.** Tanto §8.2 L5208/L5210 como §18 L6993 listan **`AUD`** y **`DEU`** en la columna de **participantes**, es decir, como capacidades. La nota inmediatamente inferior a la tabla, **L7003–7005**, prohíbe exactamente eso:

> *«`DEU` y `DEP` son **procesos**, no capacidades: las quince son `APR ARQ CON DIS DOM DSP ENC ENT INV PLT PRD SEG SIS USO VER`, y confundir el nombre de un proceso con el de una capacidad es el mismo modo de fallo que `G1` corrigió con `a.9`.»*

La tabla comete en su propia columna el error que su nota al pie declara prohibido.

**Qué exigiría cerrarlo.** (a) Elegir **un** proceso para `A2`–`A7` y hacerlo coherente en las dos sedes; si es `AUD`, resolver además su `propietario_global`, que `01-PROCESOS.md` L419 declara **«DERIVADO del encargo … NUNCA se asigna a mano»** y §18 fija a mano en `INV`. (b) Si se conserva `INV`, declarar por qué vía entran `DOM`, `SEG` y `DIS/Reconstruccion`, y retirar la frase de L5209 que los apoya en `AUD`. (c) Sustituir `AUD` y `DEU` por capacidades reales en las columnas de participantes.

---

### `B-2` · Los participantes declarados de los cuatro macrocircuitos **no tienen vehículo** en los condicionales del proceso que `D67` les asigna

**Cita 1** — §8.1, **L5090–5091**:

> `PARTICIPANTES   Owner · PLT (N0,N2,N6) · ENC+PRD (N1,N5) · SIS (N3) · VER (N4,N7) ·`
> `                ARQ DOM DIS SEG según discovery`

**Cita 2** — §18, **L6990**: `N0`–`N5` → **`proceso:SIS`**, propietario global **`SIS`**.

**Cita 3** — `01-PROCESOS.md` **L553–557**, `proceso:SIS`, sección completa de condicionales:

> `condicionales:`
> `  - capacidad: "ENT"`
> `    condicion: "el cambio modifica el runtime: activación segura y reversible"`
> `  - capacidad: "APR"`
> `    condicion: "C-APR"`

**Por qué es defecto.** `proceso:SIS` declara **exactamente dos** condicionales: `ENT` y `APR`. §8.1 declara como participantes de `N1` y `N5` a `ENC`, `PRD`, y «según discovery» a `ARQ`, `DOM`, `DIS` y `SEG`. **Ninguna de las seis puede entrar en la ruta de un item `proceso:SIS`**: no son obligatorias, no son condicionales, y tampoco caben por la vía de consulta, porque sus propias fichas acotan de quién aceptan consultas y **`SIS` no figura en ninguna**:

- `DIS/CAPACIDAD.md` **L33**: `- "una consulta en modo consulta desde ENC, PRD, ARQ o USO"`
- `PRD/CAPACIDAD.md` **L20**: `- "una consulta en modo consulta desde DIS, ARQ o ENC"`
- `ARQ/CAPACIDAD.md` **L20**: `- "una consulta en modo consulta desde PRD, DIS o ENC"`

El mismo patrón se repite en `A5` y `A9` (§8.2 L5201, L5210) y en `M0`–`M5` (§8.3 L5295).

`D67` existe precisamente para cerrar esto. Su motivo, `DECISIONES-Y-CONTRADICCIONES.md` L101, dice: *«la ruta, las obligaciones, el propietario global y los gates se DERIVAN del proceso — F6 habría tenido que elegirlo, y eso es una decisión arquitectónica»*. La corrección **asignó el proceso y no comprobó que sus condicionales admitieran los participantes declarados**, con lo que F6 sigue teniendo que tomar una decisión arquitectónica nueva: **cómo activa un item `proceso:SIS` a `DIS`, `DOM`, `SEG`, `PRD` o `ENC`**. Las salidas posibles —añadir condicionales a `proceso:SIS` (enmienda de `b.16`), partir cada macrocircuito en más items de procesos distintos, o dejar que esas capacidades actúen fuera de la ruta— tienen consecuencias normativas **opuestas**, y ninguna está escrita.

**Consecuencia material.** O el discovery de `N5` y la reconstrucción de `A6` **no ocurren dentro de la ruta** —y entonces son trabajo sin traza, sin gate y sin capa, contra `b.16`—, o la ruta activa capacidades que su proceso no declara —y entonces `gate:despacho-coherente`, comprobación `traza-de-ruta` (`DSP/CAPACIDAD.md` L78–81), no puede escribirlas ni como activadas ni como no activadas con motivo derivado del proceso.

**Qué exigiría cerrarlo.** Declarar, macrocircuito por macrocircuito y fase por fase, **por qué mecanismo entra cada participante**; y si el mecanismo no existe en `b.16`, registrarlo como presión normativa, que es exactamente lo que §16 hizo con `PN-2` para un caso análogo y no hizo aquí.

---

## GRAVE

### `G-1` · `U5b` se asigna a `proceso:DEP` sin `SEG` ni `CON`, y `proceso:DEP` genera una obligación que **nadie puede retirar**

**Cita 1** — §18 **L6999**:

> `| | `U5`–`U6` | `proceso:SIS` · `proceso:DEP` en `U5b` | **`SIS`** · **`PLT`** en `U5b` | `ENT`, `VER` | … |`

**Cita 2** — §8.4 **L5440**: `PARTICIPANTES   SIS · PLT · VER · Owner si hay incompatibilidad o retirada`

**Cita 3** — `01-PROCESOS.md` **L370–377**, `proceso:DEP`, primera obligatoria:

> `  - id: condiciones-de-seguridad`
> `    capacidad_productora: "SEG"`
> `    autoridad_de_retirada: >`
> `      nadie: G28 lo hace obligatorio en este proceso y no se retira`

**Cita 4** — mismo fichero **L378–385**: segunda obligatoria `cambio-construido`, `capacidad_productora: "CON"`.

**Por qué es defecto.** `SEG` **no aparece** entre los participantes de `U5b` ni en §8.4 ni en §18; `CON` tampoco. Un item de `proceso:DEP` genera las tres obligaciones —`condiciones-de-seguridad`, `cambio-construido`, `evidencia-suficiente`— y `gate:cierre-de-item` (`00-OBLIGACIONES-Y-CIERRE.md` L83) exige **«cero obligaciones huérfanas»**. La primera de ellas tiene `autoridad_de_retirada: nadie`. Sin `SEG`, la obligación queda **huérfana de forma permanente e irremediable**, y el `fallo` del gate (L111–116) es terminante: *«Un item con todos sus paquetes cancelados y ninguna retirada aprobada no puede cerrar nunca»*. **El `CIERRE` que §8.4 L5476 declara —`U6` superado— es inalcanzable tal como está escrito.**

Agrava que **F4 conoce esta regla y la cita ella misma**: §5.2 **L4275** dice *«`b.16` ya declara `SEG:condiciones ⊳ CON` OBLIGATORIO en `DEP` por `G28`»*. Y `G28` existe literalmente en `kernel/KERNEL.md` L986 («Supply chain de dependencias»), con procedencia declarada «obligatorio, no delegable».

**Qué exigiría cerrarlo.** Añadir `SEG` y `CON` a los participantes de `U5b` en §8.4 y en §18 —lo cual está **completamente determinado** por `G28`, no es una decisión nueva—, o justificar por qué propagar un fichero puntero no es «incorporar o actualizar una dependencia externa» y reasignar el proceso.

---

### `G-2` · `A8` y `M6`–`M7` se asignan a `proceso:DEU` con propietario global `ARQ`, y `ARQ` no está entre los participantes; `CON` no aparece en ninguna de las dos filas

**Cita 1** — §18 **L6994** y **L6997**: ambas filas, `proceso:DEU`, propietario global **`ARQ`**, participantes «`PLT` ejecuta bajo `C7`» y «`PLT` ejecuta bajo `C7` · `VER` verifica».

**Cita 2** — §8.3 **L5295**: `PARTICIPANTES   PLT · SIS · VER · Owner en M6` — **`ARQ` ausente**.

**Cita 3** — `01-PROCESOS.md` **L322–329**, `proceso:DEU`, obligatoria `cambio-construido`, `capacidad_productora: "CON"`.

**Por qué es defecto.** (a) §18 hace a `ARQ` propietario global de `M6`–`M7` y §8.3 no lo lista como participante: el propietario global es quien **declara la integración semántica** (`00-OBLIGACIONES-Y-CIERRE.md` L50) y sin él el item no cierra. (b) `proceso:DEU` exige una capa de `CON`, y ninguna de las dos filas declara a `CON`; `PLT` no es `CON`, y su propia ficha (`PLT/CAPACIDAD.md` L4) dice que **«no toma custodia de paquetes de producto»**. Queda sin decidir quién deposita esa capa obligatoria en la única operación destructiva de todo el sistema.

**Qué exigiría cerrarlo.** Reconciliar §8.3 `PARTICIPANTES` con §18, y nombrar a la capacidad productora de `cambio-construido` en `A8`, `M6` y `M7`.

---

### `G-3` · §8.1 declara `N7 = O12` sin declarar productor de dos de las tres condiciones de `O12`

**Cita 1** — §8.1 **L5097**: `GATES           N4 certificación Operativa · N7 = O12`

**Cita 2** — `DECISIONES-Y-CONTRADICCIONES.md` **L36** (`O12`): *«**Integrada + baseline aprobado + ningún desconocido crítico sin clasificar.**»* — y §9.4 **L5685–5686** lo repite: *«Las tres, no dos.»*

**Cita 3** — §8.1 `FASES` **L5081–5089**: `N0` … `N7`. **No hay fase de baseline**, ni gate de baseline, ni paso de clasificación de desconocidos críticos. `EVIDENCIA` (L5096) es *«`workspace check` · prueba de humo por adaptador · checkpoint recuperado»*.

**Por qué es defecto.** La adopción sí lo tiene: §8.2 L5199 declara `A3 BASELINE con evidencia` y L5219 lo eleva a gate *«`A3` baseline aprobado por el Owner»*. La instalación invoca el mismo `O12` en `N7` y no produce dos de sus tres términos. O `O12` se satisface con menos de tres en instalación —y entonces `O12` está reinterpretado sin registrarlo, que es exactamente la vara que `PN-6`, `PN-10` y `PN-12` fijan para las resoluciones del Owner— o `N7` no puede superarse.

**Qué exigiría cerrarlo.** Declarar qué fase de `N` produce el baseline y la clasificación de desconocidos críticos, o registrar la reinterpretación de `O12` como presión normativa con la simetría que §16 se impone a sí misma.

---

### `G-4` · Las doce áreas de `O8` no tienen identificador declarado, y el único ejemplo que existe usa la mitad partida que `D68` retira

**Cita 1** — §4.3 **L4125**: *«Cada una es un `aspecto:documental/<area>` con su namespace propio»*; **L4134**: *«cada área es un `contrato-de-aspecto:documental/<area>`»*.

**Cita 2** — §4.3 **L4139–4148**: las doce áreas se enumeran **sólo en prosa castellana** («mapa documental», «identidad y dirección de producto», «arquitectura actual y dirección arquitectónica ← UNA área, no dos»…). **No hay ni un identificador.**

**Cita 3** — §5.6 **L4430** y **L4433**:

> `aspecto       aspecto:documental/arquitectura-actual       una de las doce áreas de O8`
> `criterio      contrato-de-aspecto:documental/arquitectura-actual        §5.7`

y **L4456**: `memoria.contiene [arquitectura-actual, dominio-y-glosario]   DOS áreas, §4.3`; y §5.7 **L4613** repite `aspecto:documental/arquitectura-actual`.

**Por qué es defecto.** `D68` (§4.3 L4128–4136) corrige que F4 *«partía "arquitectura actual y dirección arquitectónica" en dos»* y restituye **una** área. El identificador `arquitectura-actual` **es el nombre de la mitad retirada**, y sobrevive en cuatro sitios como el único ejemplo trabajado del namespace documental. Con doce áreas sin identificador declarado y el único ejemplo usando un identificador retirado, **F6 tiene que inventar los doce**, y el ejemplo que tiene delante lo induce a repetir la partición que `D68` acaba de deshacer.

**Qué exigiría cerrarlo.** Declarar los doce identificadores `documental/<area>` junto a las doce materias, y corregir §5.6 y §5.7 para que su ejemplo use el identificador del área unificada.

---

## MEDIO

### `M-1` · Recuento de las áreas documentales condicionales: se declara **CATORCE**, la enumeración da **TRECE**

**Cita** — §4.3 **L4174–4178**:

> `CONDICIONALES    las CATORCE que `§5.18` enumera, y son las suyas: UX e investigación,`
> `                 dirección visual, sistema de diseño, arquitectura de datos detallada,`
> `                 integraciones, cumplimiento regulatorio, modelo de amenazas avanzado,`
> `                 observabilidad, continuidad, analítica, dispositivos,`
> `                 internacionalización, gobierno de IA. Se activan por aplicabilidad.`

y **L4191**: `| **condicionales** | 14, las de `§5.18` | … |`

**Derivación.** La lista de §4.3 tiene **13** entradas. La fuente, `ADS-PENDIENTES…` **§5.18 L789–791**, tiene las **mismas 13**: *«UX e investigación, dirección visual, sistema de diseño, arquitectura de datos detallada, integraciones, cumplimiento regulatorio, modelo de amenazas avanzado, observabilidad, continuidad, analítica, dispositivos, internacionalización o gobierno de IA.»*

**Por qué es defecto.** `D68` existe para corregir un recuento documental que conservaba el número y no el conjunto —*«El número doce se conservaba; el conjunto no»*, L4133—. La corrección arregló las obligatorias y **reprodujo el mismo modo de fallo en las condicionales**: cifra declarada distinta del conjunto enumerado, en el mismo apartado y en la tabla que lo resume. Cada condicional es un `contrato-de-aspecto` que F6 construirá.

**Qué exigiría cerrarlo.** Corregir «CATORCE» → «TRECE» en L4174 y «14» → «13» en L4191, o declarar cuál es la decimocuarta.

---

### `M-2` · §4.3 y `PN-12` invocan «su fila en §1.3» para el mapa documental, y §1.3 no tiene esa fila

**Cita 1** — §4.3 **L4156–4157**: *«luego su fila en §1.3 tiene autoridad «nadie: se regenera».»*
**Cita 2** — §16 `PN-12` **L6862–6863**: *«el área 1 pasa a tener responsable y caducidad propios, y su fila en §1.3 deja de tener autoridad «nadie».»*
**Cita 3** — §1.3 **L184–205**, matriz completa. Las tres filas con autoridad «nadie» son: *zona `COLA` de un tablero, dosieres, vistas, índices* · *estado de una iniciativa* · *nivel alcanzado por un adaptador*. **No existe fila para el mapa documental.**

**Por qué es defecto.** Dos sedes —una de diseño y una presión normativa que va al Owner— afirman una fila que la matriz de fuentes de verdad no contiene, en el único apartado que el documento declara aplicación de `I5` a la arquitectura entera. La condición de reversión de `PN-12` es inejecutable como está escrita.

**Qué exigiría cerrarlo.** Añadir la fila a §1.3, o reformular ambas referencias.

---

### `M-3` · §18 fija `U6 = O12`; §8.4 fija para `U` la revalidación del nivel previo. Son cosas distintas

**Cita 1** — §18 **L6999**, columna gate: `` `U6` = `O12` ``.
**Cita 2** — §8.4 **L5464**: `GATES           U3 aprobado antes de U4 · U6 certificación`; y **L5465–5466**: `CERTIFICACIÓN   el nivel que tuviera antes, revalidado. Una actualización que baja el nivel alcanzado es un fallo, no un resultado`.

**Por qué es defecto.** `O12` es **Integrada + baseline + ningún desconocido crítico**. §8.4 dice que `U` revalida **el nivel que el producto tuviera**, que puede ser Estructural u Operativa. Bajo §18, una actualización rutinaria de un producto certificado sólo en Operativa **no podría cerrar** hasta alcanzar Integrada y un baseline aprobado, que es precisamente el aparato de migración que §8.4 L5525–5528 declara que `U` **no** debe cargar.

**Qué exigiría cerrarlo.** Elegir uno de los dos gates para `U6` y hacerlo coherente en ambas sedes.

---

### `M-4` · `D67` resume el mapeo de forma que la tabla de §18 desmiente

**Cita 1** — `DECISIONES-Y-CONTRADICCIONES.md` **L101** (`D67`): *«instalar, migrar y actualizar son `proceso:SIS`; inventariar y reconstruir, `proceso:INV`; retirar lo heredado, `proceso:DEU`; **propagar y certificar, `proceso:DEP`**.»*
**Cita 2** — §18 **L7018–7020**: *«y `proceso:DEP` … **aparece sólo donde de verdad hay una**: `U5b`»*. En la tabla, **toda** certificación (`N4`, `N7`, `A9`–`A10`, `M5`, `U6`) es `proceso:SIS`.

**Por qué es defecto.** El registro de decisiones —que es lo que viaja a un proyecto instalado, según su propia nota L38–39— dice que certificar es `DEP`, y la arquitectura dice lo contrario. Un lector del registro construiría el mapeo mal.

**Qué exigiría cerrarlo.** Corregir el resumen de `D67`, sin reescribir la decisión: basta que diga «propagar a las fuentes, `proceso:DEP`».

---

### `M-5` · El ciclo de auditoría de §5.3 deja `APERTURA` y `CAMPAÑA` sin actor, y `DSP` no aparece en todo §5

**Cita 1** — §5.3 **L4327–4340**:

> `APERTURA            crea un item AUD. SÓLO dentro de la política O7. Si no hay política`
> `                    vigente, el sistema PROPONE y espera`
> …
> `CAMPAÑA             una `iniciativa` con su gate`

Ambos pasos nombran «el sistema» y ningún actor. Todos los demás pasos nombran capacidad: `ENC`, `CON`, `VER`, `APR`.

**Cita 2** — `ADS-PENDIENTES…` **§20.14 L1475**: `| DSP | Planificación, recurrencia, campañas, dependencias y trabajo huérfano |`

**Por qué es defecto.** El reparto del Owner asigna a `DSP` exactamente los dos pasos que quedan sin actor, y `DSP` no aparece en §5. `PN-2` registra la mitad normativa —que la política de recurrencia es una tercera vía de crear trabajo que `b.15.1` no contempla— y **no la mitad de autoría**: quién ejecuta la apertura. `DSP/CAPACIDAD.md` L51 sólo le autoriza *«crear y despachar desbloqueadores dentro del alcance ya autorizado (b.15.1)»*, y L54 le obliga a escalar *«todo lo que exceda el alcance ya autorizado»*.

**Qué exigiría cerrarlo.** Nombrar el actor de `APERTURA` y de `CAMPAÑA`, y declarar si esa apertura cabe o no en la autoridad de `DSP` tal como su ficha la escribe.

---

### `M-6` · `ENC` clasifica findings en toda la arquitectura, y su extensión de ficha no se registra, a diferencia de las otras cuatro

**Cita 1** — §5.3 **L4335**: `CLASIFICACIÓN       `ENC`, con las nueve clases de entrada y los diez procesos de b.16`
**Cita 2** — §8.3 **L5410–5411**: `LA DEPENDENCIA OCULTA TIENE PROCESO … Pasa por `ENC` y por las nueve clases de entrada, como cualquier finding (§5.3)`
**Cita 3** — `ENC/CAPACIDAD.md` **L35–39**, lista completa de `entrada`: expresión del Owner · pregunta del Owner sobre el estado · item existente sobre el que el Owner comenta · aprendizaje o candidato que `APR` devuelve **al Owner** para confirmar. **Un finding de un `AUD` no está.**
**Cita 4** — `entrada/01-TAXONOMIA.md` **L5–6**: *«Entre lo que dice [el Owner] y lo que el sistema fabrica hay nueve cosas distintas»* — las nueve clases están definidas **sobre la expresión del Owner**.
**Cita 5** — §17 **L6915**: *«`+4` extensiones de ficha: `ENT`, `ARQ`, `PLT` y `SEG`»*.

**Por qué es defecto.** F4 registra escrupulosamente cuatro extensiones de ficha en §5.2 L4296–4305, *fichero a fichero*, y omite la quinta, que es la que sostiene dos apartados suyos. El reparto del Owner (`§20.14 L1477`) sí la exige: *«ENC | Clasificación y anclaje de findings»*. La asimetría es el defecto: se aplicó la disciplina a cuatro capacidades y no a la quinta.

**Qué exigiría cerrarlo.** Añadir `capacidades/ENC/` a la lista de extensiones de ficha de §5.2 y a §17, con la entrada «finding clasificable» y la nota de que las nueve clases se aplican a un sujeto que no es el Owner.

---

### `M-7` · El freno de racha `SIS` no se evalúa contra macrocircuitos que son enteramente `proceso:SIS`

**Cita 1** — `docs/rediseno/a-CAPACIDADES-APROBADA.md` **L549–563** (`a.7`, FRENO 3):

> `No se despachan más de 2 items de tipo SIS completados consecutivamente`
> `SI existe al menos un item de producto listo para avanzar.`
> `EXCEPCIONES: · instrucción explícita del Owner · incidente del propio sistema · trabajo SIS que desbloquea directamente el item de producto listo`
> `NO APLICA mientras el objetivo explícito del proyecto sea construir o migrar el propio kernel/runtime.`

**Cita 2** — `DSP/CAPACIDAD.md` **L110–113**: `gate:despacho-coherente`, comprobación `frenos-evaluados`: *«antes de despachar se han evaluado los cuatro frenos … racha SIS … un despacho sin ellos no es conforme»*.

**Cita 3** — §18 **L6998–6999**: `U0`–`U4` y `U5`–`U6` son `proceso:SIS`.

**Derivación.** `grep -n 'racha' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` devuelve **una sola línea**, L6197, y es una mención de pasada en §13.2 («el freno de racha SIS» entre lo que el circuito de aprendizaje conserva). **§8 no lo menciona ni una vez.**

**Por qué es defecto.** La excepción «NO APLICA mientras el objetivo explícito del proyecto sea construir o migrar el kernel» cubre `N` y `M`. **No cubre `U`**: actualizar ADS en un producto vivo no es el objetivo explícito de ese proyecto, y ese producto sí tiene items listos para avanzar. Con `U0`–`U6` como items `proceso:SIS`, el tercero se detiene por `a.7` a mitad de una actualización que §8.4 L5461 declara **bloqueante para cualquier otra**. Ninguna de las tres excepciones aplica de forma evidente.

**Qué exigiría cerrarlo.** Declarar en §8 cómo interactúa cada macrocircuito con el FRENO 3 —excepción aplicable, agrupación en menos items, o registro de la presión.

---

### `M-8` · §19 y §2.9 siguen contando artefactos que `D64` retiró, y `R1`–`R9` colisiona con `R1`–`R8`

> **Solapa parcialmente con el eje del REVISOR A. Lo registro por su efecto sobre §19, que es la declaración de límites del gate.**

**Cita 1** — §2.6.9 **L1439–1440**: *«Lo que había aquí —`reconciliacion-preparada`, `reconciliada`, tres contadores y **nueve ventanas `R1`–`R9`**— **se retira**.»*
**Cita 2** — §2.6.5 **L968–969**: *«las nueve `R1`–`R9` de la reconciliación **se retiran** con la ruta larga (`D64`)»*.
**Cita 3** — §19 **L7059–7062**: *«los doce escenarios de §14, las CUARENTA Y DOS filas … **las NUEVE ventanas `R1`–`R9` de §2.6.9** y los ONCE escenarios negativos … están ESCRITOS. Ninguno se ha ejecutado.»*
**Cita 4** — §2.9 **L2816**: *«Ninguna se ha ejecutado, como las cuarenta y dos de §2.6.7 y **las nueve `R1`–`R9`**.»*
**Cita 5** — §2.1 **L269–283**: `R1` … `R8` son los **ocho requisitos** del estado durable, y `R1` se cita como tal veinte veces más (L300, L302, L311, L1356, L1365, L1979, L1982, L2007, L2047, L6539).

**Por qué es defecto.** (a) §19 es donde el gate lee qué existe y qué no; declara como escritas nueve ventanas que dos apartados anteriores declaran retiradas. (b) `R1`–`R9` significa dos cosas distintas en el mismo documento, y la colisión sobrevive a la retirada de una de ellas.

**Qué exigiría cerrarlo.** Retirar la mención de `R1`–`R9` de §19 L7060 y de §2.9 L2816, y renombrar el conjunto retirado si se conserva su registro histórico.

---

### `M-9` · El contenido del BASELINE de `A3` no está declarado, y `§15.2` traza el apartado 6 de la directiva en bloque

**Cita 1** — §8.2 **L5199**: `A3  BASELINE con evidencia` — y **L5219**: `GATES           A3 baseline aprobado por el Owner`. No hay más.
**Cita 2** — `ADS-NEXT-OWNER-BRIEF.md` **§6.2 L433–451**: catorce preguntas que el baseline **debe** responder con evidencia razonable — *«qué está roto»*, *«qué decisiones están implementadas pero nunca se documentaron»*, *«qué elementos se contradicen»*, entre otras.
**Cita 3** — §15.2 **L6289**: `| 6 | adopción | §8.2 | NUEVA |` — el apartado 6 entero se traza a §8.2, sin desglosar 6.1 ni 6.2.

**Por qué es defecto.** `A3` es un gate que el Owner aprueba, y **qué se le pone delante para aprobarlo no está escrito en ninguna parte de F4**. F6 tendría que derivar el contenido del baseline de la directiva por su cuenta. Lo mismo ocurre con §6.1: `tests`, `tags y releases`, `decisiones inferibles a partir de la implementación`, `convenciones de hecho` y `funcionalidades abandonadas` no aparecen ni en el `LEE` (L5211–5212) ni en el `INVENTARIO` (L5258–5261) de §8.2.

**Qué exigiría cerrarlo.** Declarar las preguntas que `A3` debe responder, o remitir explícitamente a §6.2 de la directiva como su contrato.

---

## MENOR

### `m-1` · `O15` cita «ocho presiones normativas vigentes»; el recuento derivado es **diez**

**Cita** — `DECISIONES-Y-CONTRADICCIONES.md` **L366** (`O15`, punto 9): *«no levanta ninguna de las condiciones que `O14` escribió ni **ninguna de las ocho presiones normativas vigentes**.»*
**Contra** — §16 **L6871**: `VIGENTES · DIEZ`; §19 **L7073**: `DIEZ PRESIONES NORMATIVAS VIGENTES`.

Ocho era correcto cuando se escribió `O15`; `PN-11` y `PN-12` entraron después. El texto de `O15` no se reescribe por norma, y el número es una cifra **derivada** que ahora es falsa. **Qué exigiría cerrarlo:** una nota al pie de `O15` que reancle la cifra sin tocar la resolución.

### `m-2` · La nota de procedencia de `O7`–`O14` quedó separada de su tabla por la inserción de `O16`

**Cita** — `DECISIONES-Y-CONTRADICCIONES.md`: tabla `O7`–`O14` en L271–280; sección `O16` en L282–312; **L313**: *«**Procedencia:** las ocho llegan de la revisión independiente de F3…»*, que se refiere a `O7`–`O14` y ahora sigue a `O16`. Un lector la atribuye a `O16`, que es del 2026-08-27 pero de origen distinto. Editorial, sin consecuencia normativa.

### `m-3` · `calidad/observabilidad` se asigna sólo a `ENT`, y la misión de `PLT` nombra expresamente la observabilidad

**Cita 1** — §5.2 **L4269**: `| `calidad/ci-cd` · `calidad/despliegue` · `calidad/observabilidad` | `ENT` | `ENT` | entrega observada |`
**Cita 2** — `PLT/CAPACIDAD.md` **L12–13**: *«Que exista y funcione la maquinaria … integración continua, **observabilidad** y aislamiento entre agentes.»*
**Cita 3** — `ENT/CAPACIDAD.md` **L4**: *«Opera la maquinaria que PLT construye; **no la construye**.»*

§5.2 creó filas de doble responsable con líder precisamente para `rendimiento`, `resiliencia` y `dependencias` (L4273–4275) por esta misma razón. Dejar `observabilidad` con responsable único es defendible —quien opera juzga— pero es una asimetría no argumentada en el apartado que argumenta las otras tres.

### `m-4` · §18 rotula la fila `U5`–`U6` sin nombrar `U5a`

§8.4 **L5435–5438** parte `U5` en `U5a` y `U5b` por decisión de §6.7 regla 3; §18 **L6999** rotula `` `U5`–`U6` `` y sólo menciona `U5b`. `U5a` no tiene proceso asignado por lectura literal de la tabla.

---

### 6 · Hallazgos que intenté y **no** pude reproducir

| lo que sospeché | por qué lo sospeché | qué encontré | veredicto |
|---|---|---|---|
| «trece validadores» (§17 L6919) sería una cifra obsoleta | `ls kernel/operativo/validadores/*.py` da **16**, y `RECUENTOS-generado.md` declara `validadores: 16` | `grep -c 'tipo: validador' validadores.yaml` → **13**, más 2 `generador` y 3 `biblioteca`. La cifra de §17 cuenta validadores, no ficheros | **NO REPRODUCIDO.** §17 es correcto |
| `O15` habría autorizado o programado la adopción | el volumen de texto de `O15` y su presencia en §18 como «paso 8» | Punto 9 lo niega literalmente (`DECISIONES` L121–124); §8.2 L5253 lo repite —*«Esto no autoriza iniciar la adopción»*—; §19 L7068 lo repite por tercera vez | **NO REPRODUCIDO.** `O15` es fiel y no autoriza |
| faltarían decisiones `D16`–`D68` o resoluciones `O1`–`O16` | siete tandas de corrección encadenadas | Derivados: `D1`–`D70` **sin huecos**, `O1`–`O16` **sin huecos** | **NO REPRODUCIDO** |
| el recuento de PN vigentes sería incorrecto | los identificadores no se renumeran y hay retiradas y fusiones | 12 identificadores − `PN-4` − `PN-5` = **10**, y §16 y §19 declaran diez | **NO REPRODUCIDO** |
| el defecto de `C7` que §9.5 denuncia sería una lectura errónea | F4 acusa a un contrato aprobado | `C7` L170 dice literalmente *«una o más fuentes»*; `E2.6` L197 dice *«varias sources»*. La denuncia es exacta y la prescripción de §9.5 L5818 es correcta | **NO REPRODUCIDO.** F4 tiene razón |
| las citas de `G27` y `G28` estarían infladas | son el fundamento del veto duro y de `SEG` en `DEP` | `KERNEL.md` L956 y L986: `G27` «reglas duras, no delegables ni negociables»; `G28` «Procedencia (obligatorio, no delegable)». Coinciden con lo que `SEG/CAPACIDAD.md` y §5.2 afirman | **NO REPRODUCIDO** |
| las doce áreas obligatorias no coincidirían con `§5.18` | es el hallazgo que `D68` dice haber corregido | Comparación literal una a una: **coinciden exactamente**, incluido «mapa documental» como área 1 y «arquitectura actual y dirección arquitectónica» como **una** | **NO REPRODUCIDO.** `D68` está bien aplicado en las obligatorias (el defecto sobrevive en las **condicionales**: `M-1`) |
| «superconfiguración» y «número de modelos» estarían mal tratados en §12 | el gate me pide evaluarlos | **Ninguno de los dos términos existe en el repositorio.** `grep -ri 'superconfig'` → 0 resultados en todo el árbol. `§26.9` del documento de pendientes cubre *enrutamiento de modelos por juicio y riesgo*, y §12.3 L6134 lo recoge como mecanismo con su límite declarado | **NO EVALUABLE.** No hay fuente contra la que contrastar |
| «técnicas de compresión sin reducir calidad» estarían omitidas de §12 | §12 no las menciona | `§26.7 L1741` las lista como **una familia candidata** entre doce, y §13.3 L6221 difiere la adopción: *«CUÁLES SE ADOPTAN LO DECIDE INVESTIGACIÓN, no esta fase. Un `INV` con su banco de pruebas»*, con los nueve campos de declaración exigidos | **NO ES DEFECTO.** Diferimiento declarado con destino y método |
| F4 confundiría procesos con capacidades en el listado de las quince | es el modo de fallo que la propia §18 nombra | Las quince derivadas por mí coinciden con §18 L7004. `DEU`, `DEP`, `AUD` son procesos y §18 lo dice bien | **NO REPRODUCIDO como error de listado.** Sí reproducido como error de **columna** en §8.2 y §18: ver `B-1` |

---

### 7 · Los diez ejes, resueltos

| # | eje | resultado |
|---|---|---|
| 1 | **Quince capacidades** | Las quince leídas íntegras. Fichas internamente coherentes: cada una declara misión, capa de valor, entradas, salidas, gate, memoria, tablero, métodos, roles, autoridad tripartita, nivel de Owner, materialización y retirada. Los cuatro vetos (`DIS`, `DOM`, `SEG`, `VER`) tienen los seis campos de `a.5` y sus reglas de colisión son mutuamente consistentes, con la excepción única de `G27` declarada en las cuatro. **Hallazgos: `M-6` (extensión de ficha de `ENC` no registrada), `m-3` (observabilidad).** Las cuatro extensiones que F4 sí registra (`ENT`, `ARQ`, `PLT`, `SEG`) están correctamente argumentadas y no son presión normativa |
| 2 | **Diez procesos** | Los diez leídos íntegros. La semántica **NO cabe** en varios de los procesos asignados: `B-1`, `B-2`, `G-1`, `G-2`. No basta que el identificador `proceso:` exista |
| 3 | **Cuatro macrocircuitos** | `N` y `A` declaran las catorce dimensiones; `M` y `U` las ganaron por `D67`. Las operaciones destructivas están **bien gobernadas en `M6`**: cuatro condiciones acumulativas, autorización del Owner **por fuente nombrada**, evidencia de que lo retirado vive en la historia, rollback por fuente, `INTEGRACIÓN PARCIAL`, y la condición de reintento que cierra el bucle `M6→M7→M6`. `U5b` está bien gobernado como escritura pero **mal asignado como proceso** (`G-1`). El reparto local/remoto del rollback de instalación —ninguna eliminación remota automática— es sólido |
| 4 | **Adopción permanente de PesquerApp** | **Cubierta.** Repositorio definitivo (`O15.2`), no MVP (`O15.4`, §18 L7042), no desechable (`O15.3`), inventario completo de repos, código, agentes, skills, prompts, reglas, workflows, documentación, UI/UX de facto, entornos y despliegue (§8.2 L5258–5261), tareas/ideas/gaps (`A7`), retirada controlada con `RETIRADA SEGURA` (L5272–5274), continuidad entre agentes (`estado/` desde `A0`, reanudación por dosier + checkpoint), gate «puede empezar a programarse» (`A10` = `O12`). **`O15` sigue sin autorizar el inicio**, verificado en tres sedes. Residuo: `M-9` (contenido del baseline) |
| 5 | **Documentación y `O8`** | Taxonomía única en tres clases, mapa documental restituido como área 1 y declarado derivado, doce obligatorias **literalmente idénticas** a `§5.18`, compactación sin perder cobertura vía `memoria.contiene`, «no aplicable» con motivo registrado, y las doce materias cubren diseño, producto, arquitectura, seguridad, despliegue, entornos, tecnologías, operación, decisiones y evolución. **Auditorías y trazabilidad** quedan cubiertas por `cobertura` y por el área 11 «decisiones», no por un área propia. **Hallazgos: `G-4`, `M-1`, `M-2`** |
| 6 | **Auditoría autónoma** | **La mejor parte del diseño.** Cobertura por par `(sujeto, aspecto)` con namespace tipado —lo que hace que accesibilidad y responsive de la misma pantalla sean celdas distintas—, `evaluacion_de_pruebas` prueba a prueba, diez estados con `corregido` ≠ `verificado`, `auditor` separado de `verificador_de_correccion`, caducidad y triggers, recurrencia bajo `O7` con revocación, causas raíz por campo común, campañas como iniciativa, corrección escalonada por riesgo sin levantar ningún gate. **Carga mecánica sobre el Owner: ausente** — inventario, cobertura y detección son automáticos y **no crean trabajo**; el Owner sólo aparece en la política, en las excepciones y en `G36` por lotes. **Hallazgo: `M-5`** (falta el actor de apertura y campaña) |
| 7 | **Adaptadores y entornos** | **Correcto y sin reservas.** Cuatro piezas separadas, fuente canónica única editable a mano, proyecciones compiladas no editables, huella y validador de deriva, prueba de humo en sesión nueva con sus cuatro desenlaces, nivel alcanzado **derivado** de celdas y nunca escrito, retirada de proyección tan gobernada como su propagación, descubrimiento por identidad remota y no por ruta, lógica de resolución como **campo del contrato** y no como prosa, y el puntero declarado excepción nombrada a la frontera de `C6`. **Claude Code y Codex son OBJETIVO y no certificado**, dicho tres veces: §6.5 L4737 (`NO CERTIFICADOS`), L4740–4741 (*«NINGÚN ADAPTADOR EXISTE HOY … el nivel alcanzado de todos es `desconocido`»*), §19 L7070. Ningún conocimiento duplicado: el puntero prohíbe expresamente reglas, memoria, estado, decisiones, contratos y prompts |
| 8 | **Coste y tokens** | **Sin sacrificio de calidad, y sin coste sin contrapartida.** §12.1 fija el suelo —*«El presupuesto alarga el calendario; NO rebaja el gate»*— y lo ancla en cuatro artefactos que ya existen. Cada uno de los ocho mecanismos declara **qué NO puede hacer**, y las prohibiciones son las correctas: la caché no sobrevive a un cambio de entorno, la selección de modelo no puede usar uno insuficiente para cumplir presupuesto, el presupuesto no puede recortar diseño, pruebas ni documentación. La unidad de coste es **recursos hasta un resultado aceptado, integrado y verificado**, incluyendo retrabajo y la intervención exigida al Owner, y añade la medición que nadie hace: **el coste de reanudar**. Paralelismo: acotado a un ejecutor por worktree (`D70`), con el paralelismo real declarado capacidad futura. **Lo que falta es de profundidad, no de dirección**: §12.2 admite que la mitad del contexto mínimo —qué métodos, documentos y decisiones se cargan dentro del control repo— **no está** y es trabajo de F6. No lo cuento como defecto: está declarado. Compresión de contexto y skills de terceros van a un `INV` con banco de pruebas y nueve campos obligatorios de declaración |
| 9 | **PN y decisiones** | **Todas las comprobaciones cuadran** salvo `m-1` y `M-4`. Ver tabla §4 |
| 10 | **Implementabilidad** | Cinco componentes exigen a F6 una **decisión arquitectónica nueva**: la activación de participantes fuera de los condicionales del proceso (`B-2`), el proceso de `A2`–`A7` (`B-1`), los identificadores de las doce áreas documentales (`G-4`), el productor del baseline de `N7` (`G-3`) y el actor de la apertura de auditorías (`M-5`). Los demás componentes —adaptadores, certificación, cobertura, iniciativa, contrato documental, gobierno de `M6`— **sí son implementables sin decidir nada nuevo**, y `PN-1` bloquea el resto por diseño |

---

### 8 · Limitaciones de mi revisión

1. **No audité el protocolo transaccional.** §2.3–§2.11 quedan fuera por reparto. `M-8` es lo único que toco de esa zona, y sólo por su efecto sobre §19.
2. **No leí los `roles/`, `metodos/`, `prompts/` ni `composicion.md`** de las quince capacidades. Un hallazgo mío sobre la ficha podría estar resuelto en su desarrollo operativo, y no lo he podido descartar. Esto afecta sobre todo a `M-6`.
3. **No leí `DIS-handoffs.md` ni `handoffs-generales.md`.** Mi cobertura de handoffs es nula. No puedo afirmar que los circuitos entre capacidades sean coherentes con §8.
4. **No leí `entrada/02-` a `05-`, `diseno/00-` a `05-`, `C1`, `C2`, `C3`, `C5`, `C6` completos, `docs/owner/`, ni los packs completos.** Mi lectura de `(a)`, `(b)`, `E1` y `E2` fue por `grep` dirigido.
5. **No ejecuté ningún validador.** Podría haberlo hecho, pero ejecutar `registrar_evidencia.py` escribe evidencia, y mi modo es sólo lectura. Derivé los recuentos leyendo el corpus y el generado, y comprobé la lógica de `comprobar_recuentos.py` por lectura, sin ejecutarla.
6. **No verifiqué los recuentos de escenarios adversariales** (42 filas de §2.6.7, 11 negativos de §11.5, 8 comprobaciones de §2.9, 12 escenarios de §14): pertenecen al eje de A.
7. **`m-3` es un juicio, no un hecho.** Que `observabilidad` deba tener doble responsable es una lectura; que `PLT` la nombre en su misión es un hecho. Separo las dos cosas y dejo el juicio al adjudicador.
8. **No sé lo que dice el REVISOR A.** No lo he consultado. Donde coincidamos, la coincidencia es independiente; donde discrepemos, no he tenido ocasión de reconciliar.

---

### 9 · Recomendación de veredicto

**INSUFICIENTE PARA F5** — dos hallazgos BLOQUEANTES (`B-1` y `B-2`) dejan a los cuatro macrocircuitos sin vía normativa para activar los participantes que ellos mismos declaran, que es justo el hueco que `D67` existía para cerrar; y `G-1` hace mecánicamente incerrable la fase `U5b` por una obligación que nadie tiene autoridad para retirar.

*No soy quien lo emite: lo emite el adjudicador C, que verificará cada cita de este dictamen contra su fichero original.*

---

## ADJUDICACIÓN DEL ADJUDICADOR C

### 1 · Identidad y procedencia

Soy el **ADJUDICADOR C** del gate final independiente de `F4c`. **Yo y sólo yo emito el veredicto**; A y B lo recomiendan.

```text
REPOSITORIO   /home/jose/ads-kernel
RAMA          redesign/kernel-2.0
HEAD          a713590a9a1d2d0f6d0a3c5942f81a8052630ed5   (git rev-parse, verificado)
ÁRBOL         limpio (git status --short vacío)
MODO          SÓLO LECTURA. No he modificado ningún fichero del repositorio, no he
              hecho commits ni ninguna escritura de git
```

**Qué NO soy.** No escribí F4 ni ninguna de sus correcciones. No apliqué `D16`–`D70`. No soy revisor: no aporto un eje propio de revisión, adjudico los dos que se me entregan. **No resuelvo por mayoría**: que A y B coincidan no hace cierto ningún hallazgo.

**Qué he tratado como objeto y no como fuente.** Los dictámenes A y B, los documentos `12`–`15`, `DECISIONES-Y-CONTRADICCIONES.md`, las cabeceras de corrección del entregable y todo mensaje de commit. **Ninguna cita de A ni de B ha sido aceptada sin abrirla en su fichero original.**

---

### 2 · Qué recibí y qué leí

**Recibido:** `dictamen-A.md` (435 líneas, hallazgos `A1`–`A14`, recomienda INSUFICIENTE) y `dictamen-B.md` (477 líneas, hallazgos `B-1`, `B-2`, `G-1`–`G-4`, `M-1`–`M-9`, `m-1`–`m-4`, recomienda INSUFICIENTE). **33 hallazgos en total.**

**Ficheros del repositorio que abrí yo para verificar:**

| fichero | tramos abiertos |
|---|---|
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | L1–64, L90–105, L180–210, L269–284, L505–560, L963–970, L1294–1298, L1345–1350, L1368–1402, L1428–1460, L1596–1660, L1681–1715, L1768–1782, L1855–1890, L1912–1922, L1934–1944, L2038–2046, L2195–2215, L2275–2282, L2308–2316, L2508–2520, L2813–2818, L3288–3300, L3320–3335, L3560–3600, L3610–3670, L3738–3752, L4120–4200, L4265–4277, L4292–4310, L4320–4345, L5004–5022, L5078–5106, L5200–5222, L5288–5300, L5406–5414, L5430–5470, L5680–5690, L6286–6292, L6515–6545, L6712–6730, L6856–6884, L6910–6920, L6985–7025, L7055–7087; más TOC completo de secciones |
| `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | L95–115, L176–239, L269–316, L364–368 |
| `kernel/operativo/recorrido/01-PROCESOS.md` | mapa estructural completo de los diez procesos (`id`, `propietario_global`, `obligatorias`, `capacidad_productora`, `autoridad_de_retirada`, `condicionales`), y L369–378 íntegro |
| `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | L75–120 (`gate:cierre-de-item` completo) |
| `kernel/operativo/capacidades/{ENC,DIS,PRD,ARQ,DOM,SEG,DSP}/CAPACIDAD.md` | tramos de `entrada`, `consulta` y `gate:despacho-coherente` |
| `docs/rediseno/a-CAPACIDADES-APROBADA.md` | `a.7` FRENO 3 (L545–566), `a.9` cinco conceptos (L668–682) |
| `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | L197 |
| `docs/evolucion/ADS-PENDIENTES-…md` | §5.18 (L770–795) |
| `docs/evolucion/ADS-NEXT-OWNER-BRIEF.md` | §6.2 (L428–455) |
| `kernel/operativo/contratos/C7-…md` | L170 |
| `kernel/KERNEL.md` | `K-1` L10 |
| `tooling/workspace.py` | L18–24, L48, L435 |
| inventarios | `esquemas/` (19 `.yaml`), `contratos/` (7), `circuitos/` (3), `entrada/` (6), `diseno/` (6), `docs/owner/` (2), `plantillas/` (7), `packs/` |
| ejecución | `comprobar_fuentes.py`, `comprobar_arranque.py` (Python 3.10.12) |

---

### 3 · Método de verificación

1. Anclar HEAD y modo lectura.
2. Por cada hallazgo BLOQUEANTE, GRAVE y MEDIO: abrir el fichero, ir a la línea, comprobar que **la cita es literal** y que **la inferencia se sigue**. Donde la línea no coincidía, buscar el texto por `grep` y anotar la desviación.
3. Recuentos derivados por mí, nunca copiados: filas de la tabla de contrato condicional (`awk` + `grep -c`), condicionales de cada proceso (`grep` estructural sobre `01-PROCESOS.md`), áreas condicionales de `§5.18`, esquemas `.yaml`.
4. MENORES por muestreo: verifiqué `A11`, `A12`, `A13`, `A14`, `m-1`, `m-2`, `m-3`, `m-4` — **los ocho**, porque eran pocos. Lo digo para que conste que aquí no hubo muestreo real sino cobertura total.
5. Clasificación de categoría por hallazgo confirmado, con la prueba explícita de si obliga a **decidir arquitectura durante F6**.
6. Cruce de las dos secciones «corpus realmente leído» contra el inventario real de directorios para derivar la cobertura.

---

### 4 · Tabla de adjudicación — los 33 hallazgos

| id | severidad del revisor | **mi veredicto** | **categoría** | mi evidencia |
|---|---|---|---|---|
| `A1` | BLOQUEANTE | **CONFIRMADO** | arquitectura (contrato) | L3659 declara `causa` ∈ {2 valores} y `tx_afectada` sólo con `posterior-al-cierre`; L3622 lo hace error de esquema estructural; L3745 lo admite con `abandono-de-transaccion`; L2203–2212 declara **tres** valores. L3657 hace `deriva_emitida` obligatorio en `abandonada`, y L2199–2200 dice que ese `deriva` lleva `tx_afectada`. Tres sedes, dos incompatibles |
| `A2` | BLOQUEANTE | **CONFIRMADO** | arquitectura (protocolo) | L2514 literal: «una transacción **sin evento `derivada`** … Con `derivada` como **único terminal** (§2.6.1), la condición es UNA». §2.6.1 L544–546 declara «**DOS cierres terminales**». L5018 literal: «¿hay transacciones sin evento `derivada`? → completar, o marcar conflicto» sobre una fase que L546 declara terminal |
| `A3` | GRAVE | **CONFIRMADO** | arquitectura | L5008–5013 literal: «§2.6 **elimina el ramal de reversión por completo**» y «*roll-forward only* es buena». Contra L1643 «`abandonada` **ES la rama «revertir»** de `b.14`» y `PN-7` L6717–6722 «**REFORMULADO por `D69`** … Ahora tiene **LAS DOS RAMAS**». Resumen §16 L6876 repite la formulación retirada |
| `A4` | GRAVE | **CONFIRMADO** | arquitectura (trazabilidad) | `grep '\| \`D6[4-8]\` \|'` sobre el entregable → **vacío**. §15.8 salta de `D63` (L6521) a `D69`–`D70` (L6530), cuyas columnas citan `D64`/`D65` como referencias colgantes. Cabecera L12 «CORREGIDO DOS VECES» y L59–62 «pendiente de una **tercera revisión independiente**», contra L7073 «tras DOS devoluciones **y la TERCERA REVISIÓN**» y L7079–7082 que vuelve a decir «pendiente». `D64`–`D68` sí están en `DECISIONES` L222–238 |
| `A5` | GRAVE | **CONFIRMADO CON MATIZ** | arquitectura | L1632–1640 literal: LLEVA «el evento `preparada`» y NO LLEVA «**ningún `hash_posterior_esperado`**. Ni uno». L3654 lo hace obligatorio dentro de `preparada`. **Matiz:** el sujeto correcto es deducible de §2.6.0 y de L345 («SE EMITEN, NO SE EDITAN»), luego es ambigüedad de sujeto, no conflicto de diseño. **Rebajo a MEDIO** |
| `A6` | MEDIO | **CONFIRMADO** | arquitectura (recuento) | L513 «**seis fases, dos rutas, un solo cierre**» contra su propio cuerpo L544–551 («DOS cierres terminales» · «Las **CINCO** fases»). L3327–3328 «SEIS/SIETE» y L3637–3640 «ocho filas / seis valores» contra L3568–3574 (5 fases, 6 estados) y mi recuento derivado: **7 filas** |
| `A7` | MEDIO | **CONFIRMADO** | arquitectura → contrato derivado | L1915–1917 literal: «los **CINCO conceptos de `a.9`**: ordenante · autoridad · escritor_del_comando · ejecutor · actor_atribuido. La ausencia de cualquiera de los cinco es un **FALLO DEL VALIDADOR**». L3290–3294 dice que llamar `actor_atribuido` «uno de los cinco» **era la cita falsa que `G1` señaló**. `a.9` L673–679 verificado literal |
| `A8` | MEDIO | **CONFIRMADO CON MATIZ** | arquitectura (justificación) | L1372–1373 y L1394–1400 literales. El predicado de L1690–1693 exige cruzar todos los `deriva` contra todas las `derivada` con `resuelve_deriva`. **Matiz:** el marcador conserva valor real (acota rutas); lo que cae es el argumento escrito, no la pieza |
| `A9` | MEDIO | **CONFIRMADO CON MATIZ** | arquitectura | Sustancia confirmada: 4b «PERMANECE ABIERTA · marcador VIVO · NO HAY COMMIT» (L1856–1858); condición `SEG` (L1771–1776); `X58` «Ninguna transacción puede quedar reteniéndolo para siempre» (L1296); L1457 sin condición. **Matiz de cita: la línea que A da (L1862–1866) es incorrecta**; el texto citado está en **L1681–1682** y **L1878–1880** |
| `A10` | MEDIO | **CONFIRMADO** | arquitectura (resumen al Owner) | L100 literal «**OCHO puntos**, tras dos devoluciones independientes» contra L6871 «VIGENTES · **DIEZ**» y L7073 «**DIEZ** PRESIONES … y la TERCERA REVISIÓN» |
| `A11` | MENOR | **CONFIRMADO** | prueba escrita (inventario del gate) | L2816 y L7060 cuentan «las nueve `R1`–`R9`» como contratos escritos; L968, L1348 y L1439 las declaran **retiradas** por `D64`. Converge con `M-8` |
| `A12` | MENOR | **CONFIRMADO** | arquitectura | L2041–2043 ofrece «un único escritor (`R5`)» como protección de la rama canónica; L2277–2279 dice que el lock «vive en el plano operacional a propósito» y L2312 que «`R5` es un requisito del runtime local, **no del producto**»; L1936–1942 admite dos máquinas como caso «POSIBLE y no gobernado» |
| `A13` | MENOR | **CONFIRMADO CON MATIZ** | contrato derivado | L3654 literal: fila `preparada` · «**los cinco de `a.9`**». Es el mismo error de `A7` **dentro de la tabla de la que F6 deriva el esquema**. **Severidad subestimada: es MEDIO, no menor** |
| `A14` | MENOR | **CONFIRMADO** | prueba ejecutada / tooling | Reproducido: `comprobar_fuentes.py` → `T159 FALLIDA · se requiere Python 3.11 o superior`; `comprobar_arranque.py` → 1 fallida. Python del entorno: **3.10.12**. La exigencia sólo consta en `tooling/workspace.py` L22; no hay `python_requires` en ninguna parte. **No es defecto de F4** |
| `B-1` | BLOQUEANTE | **CONFIRMADO** | arquitectura | §8.2 L5208–5210 literal: «A6 activa DOM, SEG, DIS/Reconstruccion y PRD, que son **LOS CONDICIONALES QUE `proceso:AUD` YA DECLARA**». §18 L6993 asigna `A2`–`A7` a **`proceso:INV`**, cuyos condicionales son (`01-PROCESOS.md` L285–292) **`CON:experimental`, `PRD`, `ARQ`, `APR`** — sin `DOM`, `SEG` ni `DIS`. Los de `AUD` (L429–437) sí son exactamente esos cuatro. Y `AUD` L419: propietario «**DERIVADO … NUNCA se asigna a mano**». Segundo defecto confirmado: L5210 y L6993 listan `AUD` y `DEU` en la columna de **participantes**, y L7003–7005 prohíbe eso literalmente |
| `B-2` | BLOQUEANTE | **CONFIRMADO CON MATIZ** | arquitectura | `proceso:SIS` (L521–556) declara **exactamente dos** condicionales: `ENT` y `APR`. §8.1 L5090–5091 declara participantes `PLT`, `ENC`, `PRD`, y `ARQ DOM DIS SEG`. **Matiz:** verifiqué la vía de consulta capacidad a capacidad — `DIS` L33, `PRD` L20, `ARQ` L20 acotan el origen y `SIS` no figura, y `ENC` L35–38 tampoco lo admite; **pero `DOM` L17 y `SEG` L53 NO acotan el origen**, luego para esas dos existe vehículo plausible. El hueco queda confirmado para `ENC`, `PRD`, `ARQ` y `DIS`, y basta para el bloqueante |
| `G-1` | GRAVE | **CONFIRMADO** | arquitectura | `proceso:DEP` L369–377 literal: obligatoria `condiciones-de-seguridad`, `capacidad_productora: "SEG"`, `autoridad_de_retirada: > nadie: G28 lo hace obligatorio en este proceso y no se retira`; segunda obligatoria `cambio-construido` → `CON`. §18 L6999 da a `U5b` participantes «`ENT`, `VER`»; §8.4 L5440 «SIS · PLT · VER · Owner». **Ni `SEG` ni `CON`.** `gate:cierre-de-item` exige «cero obligaciones huérfanas» y su `fallo` es terminante. `U6` es inalcanzable como está escrito |
| `G-2` | GRAVE | **CONFIRMADO** | arquitectura | §18 L6994/L6997: `A8` y `M6`–`M7` a `proceso:DEU`, propietario global **`ARQ`**, participantes «`PLT` ejecuta bajo `C7`» / «`PLT` … · `VER` verifica». §8.3 L5295 literal: «PARTICIPANTES PLT · SIS · VER · Owner en M6» — **`ARQ` ausente**, y es quien declara la integración semántica (`00-OBLIGACIONES` L~50, comprobación `integracion`). `proceso:DEU` L322–325 exige capa de `CON`, que no figura en ninguna de las dos filas |
| `G-3` | GRAVE | **CONFIRMADO CON MATIZ** | arquitectura | §8.1 L5097 «`N7` = `O12`». `O12` (`DECISIONES` L278) = «Integrada + baseline aprobado + ningún desconocido crítico sin clasificar»; §9.4 L5685–5686 «**Las tres, no dos**». §8.1 FASES L5081–5089: `N0`–`N7`, **sin fase de baseline ni de clasificación**; EVIDENCIA L5096 no la produce. §8.2 sí tiene `A3 BASELINE`. **Matiz:** en producto greenfield el baseline podría satisfacerse trivialmente por `N1`/`N5`, pero **eso no está escrito en ninguna parte**, y esa es exactamente la decisión que queda para F6 |
| `G-4` | GRAVE | **CONFIRMADO CON MATIZ** | arquitectura → contrato derivado | L4124–4125 y L4134 literales: cada área es un `aspecto:documental/<area>` y un `contrato-de-aspecto:documental/<area>`. Las doce de L4139–4148 están **sólo en prosa, sin un solo identificador**. `arquitectura-actual` aparece en **L4428, L4429, L4430, L4433, L4456 y L4613** como único ejemplo trabajado. **Matiz:** que ese identificador sea «la mitad retirada» es inferencia razonable —`§5.18` punto 5 nombra el área como «arquitectura actual **y dirección arquitectónica**»— pero admite lectura como slug abreviado. El defecto duro —**doce contratos sin identificador declarado**— queda confirmado sin matiz |
| `M-1` | MEDIO | **CONFIRMADO** | arquitectura (recuento) | L4174 dice «las **CATORCE**» y enumera trece: UX e investigación · dirección visual · sistema de diseño · arquitectura de datos detallada · integraciones · cumplimiento regulatorio · modelo de amenazas avanzado · observabilidad · continuidad · analítica · dispositivos · internacionalización · gobierno de IA. `§5.18` L789–791 tiene **las mismas trece**. Tabla L4191 declara «14» |
| `M-2` | MEDIO | **CONFIRMADO** | arquitectura | §1.3 L183–205 leída íntegra: las tres filas con autoridad «nadie» son *zona COLA/dosieres/vistas/índices*, *estado de una iniciativa*, *nivel alcanzado por un adaptador*. **No existe fila para el mapa documental.** L4156 y `PN-12` L6862–6863 la invocan las dos |
| `M-3` | MEDIO | **CONFIRMADO** | arquitectura | §18 L6999 columna gate: `U6` = `O12`. §8.4 L5464 «`U6` certificación» y L5465–5466 «**el nivel que tuviera antes, revalidado**». `O12` exige Integrada; un producto certificado sólo en Operativa no podría cerrar `U6` |
| `M-4` | MEDIO | **CONFIRMADO** | arquitectura vs registro de decisiones | `DECISIONES` L236 (`D67`) literal: «**propagar y certificar, `proceso:DEP`**». §18 L7012 literal: «instalar, migrar, actualizar **y certificar** son `proceso:SIS`», y L7018–7020: `DEP` «aparece **sólo** donde de verdad hay una: `U5b`». En la tabla, toda certificación es `SIS` |
| `M-5` | MEDIO | **CONFIRMADO** | arquitectura | §5.3 L4327–4340: `APERTURA` («crea un item AUD … **el sistema** PROPONE y espera») y `CAMPAÑA` («una `iniciativa` con su gate») son los **únicos dos pasos sin capacidad nombrada**; los demás nombran `ENC`, `CON`, `VER`, `APR`. Derivado por mí: **`DSP` no aparece ni una vez en todo §5** (L4205–4622) |
| `M-6` | MEDIO | **CONFIRMADO CON MATIZ** | arquitectura | `ENC/CAPACIDAD.md` L35–38: cuatro entradas, todas ancladas al Owner; **un finding de un `AUD` no está**. §5.3 L4335 y §8.3 L5410–5411 le encargan clasificar findings. §5.2 L4296–4305 registra cuatro extensiones de ficha (`ENT`, `ARQ`, `PLT`, `SEG`) fichero a fichero y §17 L6915 dice «+4». **Matiz:** B no leyó `ENC/roles|metodos`; la omisión que confirmo es la del **registro** en §5.2 y §17, que es verificable en sí misma |
| `M-7` | MEDIO | **CONFIRMADO CON MATIZ** | arquitectura | `a.7` FRENO 3 verificado literal (L549–563), incluida la excepción «NO APLICA mientras el objetivo explícito del proyecto sea construir o migrar el propio kernel/runtime». `DSP` `gate:despacho-coherente` · `frenos-evaluados` exige los cuatro. Derivado por mí: **`racha` aparece una sola vez en todo el entregable, L6197, en §13.2; §8 no lo menciona jamás**. **Matiz: rechazo el mecanismo concreto** —«el tercero se detiene»— porque el número de items de `U` no está declarado en ninguna parte (§8.1 sí declara `SIS-001` como item único para `N0`–`N5`; §8.4 no declara nada). Lo que confirmo es que **la interacción entre los macrocircuitos y el FRENO 3 no está escrita**, y `DSP` la exige |
| `M-8` | MEDIO | **CONFIRMADO** | arquitectura + prueba escrita | Las cinco citas verificadas. Además derivé §2.1 L269–283: `R1`–`R8` son los ocho requisitos del estado durable. La colisión de espacio de nombres es real y sobrevive a la retirada. Converge con `A11` |
| `M-9` | MEDIO | **CONFIRMADO** | arquitectura | §8.2 L5199 «`A3` BASELINE con evidencia» y L5219 el gate; **no hay más**. `ADS-NEXT-OWNER-BRIEF.md` §6.2 L435–451: **catorce preguntas** que el baseline debe responder con evidencia razonable. §15.2 L6289 traza el apartado 6 entero a §8.2 en bloque |
| `m-1` | MENOR | **CONFIRMADO** | arquitectura (cifra derivada) | `DECISIONES` L366 literal: «ni ninguna de las **ocho** presiones normativas vigentes». §16 L6871 y §19 L7073: **DIEZ** |
| `m-2` | MENOR | **CONFIRMADO** | editorial | Tabla `O7`–`O14` en L271–280; sección `O16` en L282–312; L313 «**Procedencia:** las ocho llegan de la revisión independiente de F3…» queda tras `O16`. Sin consecuencia normativa |
| `m-3` | MENOR | **CONFIRMADO como hecho; el juicio, no asumido** | arquitectura (asimetría) | §5.2 L4269 asigna `calidad/observabilidad` sólo a `ENT`; `PLT/CAPACIDAD.md` L12–13 nombra observabilidad en su misión; L4273–4275 crea doble responsable para las otras tres por ese mismo motivo. Que **deba** tener doble responsable es lectura, y B lo declara. No lo confirmo como defecto |
| `m-4` | MENOR | **CONFIRMADO CON MATIZ (inferencia rechazada)** | editorial | El hecho es cierto: §8.4 L5435–5438 parte `U5a`/`U5b`; §18 L6999 rotula `U5`–`U6` y sólo nombra `U5b`. **Rechazo la inferencia**: la celda dice «`proceso:SIS` · `proceso:DEP` **en `U5b`**», que asigna `SIS` a todo lo demás, `U5a` incluido. No hay fase sin proceso |

**Recuento adjudicado:** **3 BLOQUEANTES confirmados** (`A1`, `A2`, `B-1`) **+ 1 confirmado con matiz que sigue siendo bloqueante** (`B-2`) · **6 GRAVES confirmados** (`A3`, `A4`, `G-1`, `G-2`, `G-3` con matiz, `G-4` con matiz) · **13 MEDIOS confirmados** (contando `A5` y `A13` reclasificados a MEDIO por mí) · **6 MENORES confirmados**, de los cuales uno con inferencia rechazada y uno declarado juicio.

---

### 5 · Discrepancias y solapamientos entre A y B, resueltos uno a uno

**(a) Donde dicen lo mismo por caminos distintos — refuerzo, verificado por mí:**

1. **`A11` ≡ `M-8` · las nueve ventanas `R1`–`R9`.** A llegó por §19 y §2.9; B por §2.6.9 y §2.6.5, y añadió la colisión con `R1`–`R8`. **Resuelto: ambos ciertos, y el hallazgo unificado es el de B**, que es estrictamente más completo. Verifiqué las seis sedes y §2.1 L269–283.
2. **`A10` ≡ `m-1` · la cifra «ocho presiones».** Sedes distintas —§0 L100 y `O15` L366— con la misma raíz: dos cifras derivadas que no se reancoraron cuando entraron `PN-11` y `PN-12`. **Resuelto: dos instancias del mismo defecto, ambas confirmadas.**
3. **`C7.aplica_a`.** A (su no-reproducido nº6) y B (su §4 y su no-reproducido nº5) coinciden en que la denuncia de §9.5 es exacta. Lo verifiqué de forma independiente: `C7` L170 «una o más fuentes», `E2.6` L197 «varias sources». **Resuelto: no es defecto de F4; F4 tiene razón, y la abstención de tocar `C7` es coherente.**
4. **`O15` no autoriza la adopción.** A no lo tocó; B lo verificó en tres sedes. Lo comprobé en L7068 y en `DECISIONES`. **Resuelto: fiel.**

**(b) Donde uno afirma algo que el otro contradice:**

5. **`PN-7`.** B (§4, fila `PN-7`) declara que **cuadra**: refleja las dos ramas, L6718–6728. `A3` sostiene que §16 repite la formulación retirada. **Resuelto por lectura directa: los dos tienen razón sobre sedes distintas.** El **cuerpo** de `PN-7` (L6717–6722) está reformulado y es correcto; el **resumen para el Owner** (L6876) dice «§2.6 sólo completa», que es la formulación que `D69` retiró. **Consecuencia: la afirmación de B en su eje 9 —«todas las comprobaciones cuadran salvo `m-1` y `M-4`»— es demasiado generosa, y la corrijo.** No es discrepancia material: es cobertura desigual dentro de §16.
6. **Implementabilidad.** B (eje 10) afirma que «los demás componentes **sí son implementables sin decidir nada nuevo**». `A1` y `A2` demuestran que el protocolo transaccional **no** lo es. **Resuelto sin conflicto:** B excluyó §2.3–§2.11 de su eje por reparto y lo declara en su limitación 1. La afirmación de B **no cubre** la zona de A. Prevalece A donde A leyó.
7. **`m-4` frente al resto de §18.** B lee la celda `U5`–`U6` como si dejara `U5a` sin proceso. La misma celda que B cita en `G-1` y `M-3` la lee correctamente. **Resuelto contra B en este punto**: la inferencia de `m-4` no se sigue de su propia cita.

**(c) Donde uno da por bueno lo que el otro clasificaría como defecto:**

8. **§8 entero.** B lo leyó y A no. Ningún hallazgo de A lo contradice. **Sin conflicto.**
9. **§2.6 entero.** A lo leyó y B no, salvo `M-8`. Ningún hallazgo de B lo contradice. **Sin conflicto.**
10. **Recuentos de `D` y `PN`.** B derivó `D1`–`D70` sin huecos en `DECISIONES` y lo dio por bueno; `A4` denuncia que **el entregable** no los registra. **Resuelto: no se contradicen** — B miró el registro de decisiones, A miró §15.8 del entregable. Ambos ciertos, y verifiqué los dos.

**No he encontrado ninguna discrepancia MATERIAL irresoluble entre A y B.** Todas las aparentes se resuelven demostrando que los dos revisores miraban sedes distintas. La cláusula del encargo que haría INSUFICIENTE por discrepancia irresoluble **no se dispara**; el veredicto no se apoya en ella.

**(d) Un defecto que ninguno de los dos registró y que confirmo yo, como corroboración de `A3`:**

> **L1458**, tabla de proporcionalidad de §2.6.9: «| roll-forward only, sin deshacer | **sí** | **ninguna de las dos rutas revierte nada** |»

Es una tercera sede vigente que contradice a `D69` (`abandonada` restaura el estado especulativo y lo verifica byte a byte, §2.6.9 C–D). No lo cuento como hallazgo nuevo con severidad propia: **refuerza `A3` y confirma que el patrón de propagación incompleta de `D69` alcanza al menos a §7.4 L5008–5013, §16 L6876 y §2.6.9 L1458.**

---

### 6 · Hallazgos rechazados, con motivo

**Ninguno rechazado en bloque.** Lo digo sin adorno porque es un dato del gate: los 33 hallazgos tienen cita localizable y ninguno resultó inventado. Lo que sí rechazo son **piezas** de tres de ellos:

| pieza rechazada | de | motivo |
|---|---|---|
| «`U5a` no tiene proceso asignado por lectura literal de la tabla» | `m-4` | **La inferencia no se sigue de la propia cita.** §18 L6999 dice «`proceso:SIS` · `proceso:DEP` **en `U5b`**», forma que asigna `SIS` por defecto a todo lo demás. El hecho editorial —el rótulo omite `U5a`— sí lo confirmo |
| «el tercer item `U` se detiene por `a.7` a mitad de una actualización» | `M-7` | **No demostrado.** El número de items de un macrocircuito `U` no está declarado en ninguna parte del entregable. §8.1 sí declara item único (`SIS-001`) para `N0`–`N5`; §8.4 no declara nada. Sin ese dato la mecánica no se sigue. El defecto de fondo —§8 nunca reconcilia los macrocircuitos con el FRENO 3 que `DSP` exige evaluar— **sí lo confirmo** |
| «`SIS` no figura en ninguna» de las fichas de consulta | `B-2` | **Parcialmente falso.** `DOM/CAPACIDAD.md` L17 y `SEG/CAPACIDAD.md` L53 declaran modo consulta **sin acotar el origen**. La afirmación se sostiene sólo para `DIS`, `PRD`, `ARQ` y `ENC` — que bastan, pero la generalización es incorrecta |
| la referencia de línea `L1862–1866` | `A9` | **La cita no está ahí.** El texto existe, en **L1681–1682** y **L1878–1880**. Corrijo la referencia y confirmo la sustancia |
| «`m-3` es un defecto» | `m-3` | **No lo asumo como defecto.** B mismo lo declara juicio y no hecho. Los dos hechos que lo sostienen son ciertos; la conclusión es una preferencia de diseño defendible en ambos sentidos |

Añado dos advertencias de categoría, porque el paso 4 del encargo las exige:

- **`A14` no es defecto de F4.** Es **prueba ejecutada** en un entorno con Python 3.10.12 contra un tooling que exige 3.11. No puede sostener nada, ni siquiera un menor contra el entregable. Lo que sí es real y ajeno a F4 es que la exigencia de versión sólo viva en una cadena de documentación.
- **Ningún hallazgo confirmado es «implementación ausente» ni «limitación ya declarada».** Lo comprobé uno a uno: que nada esté construido está declarado en §19 y no lo cuento; que `PN-1` bloquee el estado durable está declarado y no lo cuento; que el contexto mínimo de §12.2 sea trabajo de F6 está declarado y no lo cuento. **Los cuatro bloqueantes y los seis graves son todos defectos del texto normativo vigente**, no ausencias de código.

---

### 7 · Cobertura del corpus

Derivada por mí cruzando las dos secciones «corpus realmente leído» contra el inventario real de directorios en este HEAD. **Lo que sigue no lo cubrió ninguno de los dos:**

| fuente obligatoria | estado | quién debía |
|---|---|---|
| `kernel/operativo/circuitos/DIS-handoffs.md` | **NO LEÍDO por ninguno** | B lo declara explícitamente en su limitación 3 |
| `kernel/operativo/circuitos/handoffs-generales.md` | **NO LEÍDO por ninguno** | ídem — «Mi cobertura de handoffs es **nula**» |
| `kernel/operativo/entrada/00-INDICE, 02-CIRCUITO, 03-FORMAS, 04-INCERTIDUMBRE, 05-ESCENARIOS` | **NO LEÍDOS** (de `01-TAXONOMIA`, dos bloques de nueve) | B, parcial declarado |
| `kernel/operativo/diseno/00-` a `05-` (**seis ficheros**) | **NO LEÍDO NI UNO** | ninguno de los dos lo abrió |
| `kernel/operativo/contratos/C1`, `C2`, `C3`, `C5` | **NO LEÍDOS por ninguno** | A los declara fuera; B también |
| `C4`, `C6` | **parciales** (A estructural, B algoritmo) | — |
| `docs/owner/` (2 ficheros) | **NO LEÍDO NI UNO** | ninguno |
| `packs/` más allá de cabeceras (11 ficheros `.md`) | **cabeceras únicamente** | B |
| esquemas: 18 de los 19 `.yaml` | **inventariados, no leídos** | sólo `integration-set.yaml` se leyó |
| `(a)`, `(b)`, `E1`, `E2` completos | **tramos y `grep` dirigido** | A leyó `a.9` y `b.14`; B `a.7` y `E2.6`; yo añadí `a.7` FRENO 3 y `E2` L197 |
| `K-1` | **localizado, no leído** (`KERNEL.md` L10) | B declara «intacta» citando §17, que es el objeto, no la fuente |
| `tooling/tests/test_workspace.py` | **NO LEÍDO ni ejecutado** | `pytest` no instalado |
| validadores `.py` línea a línea | **ejecutados, no auditados** | A ejecutó 7; B no ejecutó ninguno |
| `11-ARQUITECTURA-INTEGRADA.md` §11 y §14 | **NO LEÍDOS en detalle por ninguno** | A los excluye; B los declara parciales |

**El encargo exige que entre A y B se cubra íntegro el corpus obligatorio.** No se cubrió. Faltan, sin ambigüedad y por nombre: **los dos ficheros de handoffs, los seis de `diseno/`, cuatro de los siete contratos transversales, los dos de `docs/owner/`, y cuatro de los seis de `entrada/`.** Son dieciocho fuentes obligatorias intactas.

**Esto basta para bloquear por sí solo, por regla del encargo**, y lo separo de los hallazgos deliberadamente: aunque cada uno de los treinta y tres se hubiera rechazado, el gate seguiría sin poder declarar suficiencia sobre un corpus con dieciocho fuentes obligatorias sin abrir. El riesgo no es teórico: `B-2` depende de cómo entra una capacidad en una ruta, y **`C5-HANDOFF.md` y `handoffs-generales.md` son precisamente donde podría vivir el vehículo que B no encontró.** Nadie miró ahí.

---

### 8 · Limitaciones de mi adjudicación

```text
1  Verifiqué los 33 hallazgos contra su fichero y su línea. NO rehice la revisión: no
   busqué hallazgos que ninguno de los dos propusiera, salvo el de §6(d), que apareció
   al comprobar A3.

2  Mi verificación de A1 es TEXTUAL. No existe `esquemas/evento.yaml` ni validador del
   diario, luego la contradicción no es ejecutable en este HEAD. Lo confirmo como
   contradicción de contrato, no como fallo observado.

3  Heredo la laguna de cobertura del §7. NO he leído las dieciocho fuentes que faltan, y
   por tanto NO puedo afirmar que un hallazgo confirmado no esté resuelto en alguna de
   ellas. Esto afecta sobre todo a B-2, M-6 y G-4.

4  T148 y T159 fallan aquí por Python 3.10.12. NO afirmo que pasen en 3.11: afirmo que su
   fallo en este entorno no es atribuible al entregable.

5  NO ejecuté `registrar_evidencia.py` ni ningún validador con efecto de escritura, por
   modo sólo lectura.

6  Los MENORES los verifiqué todos, no por muestreo. Donde el encargo me permitía muestrear,
   no muestreé.

7  Comprobé la coherencia INTERNA de los procesos y de las fichas citadas. NO audité los
   diez procesos ni las quince fichas íntegros: para eso me apoyo en la lectura declarada
   de B, que es la única cobertura completa que existe de ese tramo, y la descuento en
   consecuencia.
```

---

### 9 · VEREDICTO

## **INSUFICIENTE PARA F5**

---

### 10 · Condición exacta para F5, hallazgo a hallazgo, ordenada por lo que desbloquea

**NIVEL 0 — sin esto ningún gate posterior puede ni empezar**

| # | qué tiene que ocurrir | cierra |
|---|---|---|
| 0.1 | **Cubrir las dieciocho fuentes obligatorias no leídas**: `circuitos/DIS-handoffs.md`, `circuitos/handoffs-generales.md`, los seis de `diseno/`, `C1`, `C2`, `C3`, `C5`, los dos de `docs/owner/`, y `entrada/00`, `02`, `03`, `04`, `05`. Con `C5-HANDOFF.md` leído **antes** de cerrar `B-2`, porque puede contener su vehículo | la regla de cobertura del encargo |

**NIVEL 1 — los cuatro bloqueantes: sin ellos el contrato no es derivable ni la ruta transitable**

| # | qué tiene que ocurrir | cierra |
|---|---|---|
| 1.1 | §3.6 L3659 declara el enum de **tres** valores de `deriva.causa`; L3622 admite `tx_afectada` con `abandono-de-transaccion`; **la sede del enum pasa a ser una sola** —§3.6— y §2.6.11 remite a ella en vez de redeclararla | `A1` |
| 1.2 | Un predicado **único y nombrado** de transacción abierta —`abierta(tx) ≡ preparada durable ∧ ¬∃ terminal ∈ {derivada, abandonada}`—, declarado una vez y referenciado desde los siete sitios; retirar «único terminal» de L449, L986 y L2514; corregir §7.4 L5018 | `A2` |
| 1.3 | Elegir **un** proceso para `A2`–`A7` y hacerlo coherente en §8.2 y §18. Si es `AUD`, resolver su `propietario_global` derivado (L419 prohíbe asignarlo a mano). Si se conserva `INV`, declarar por qué vía entran `DOM`, `SEG` y `DIS/Reconstruccion` y retirar la frase de L5209. **Y sustituir `AUD` y `DEU` por capacidades reales en las columnas de participantes** | `B-1` |
| 1.4 | Declarar, macrocircuito por macrocircuito y fase por fase, **por qué mecanismo entra cada participante** que el proceso asignado no declara como obligatorio ni condicional. Si el mecanismo no existe en `b.16`, registrarlo como presión normativa | `B-2` |

**NIVEL 2 — los graves: sin ellos hay fases inalcanzables y contratos sin autor**

| # | qué tiene que ocurrir | cierra |
|---|---|---|
| 2.1 | Añadir `SEG` y `CON` a los participantes de `U5b` en §8.4 y en §18 —determinado por `G28`, no es decisión nueva—, o justificar que propagar un puntero no es incorporar una dependencia externa y reasignar el proceso | `G-1` |
| 2.2 | Reconciliar §8.3 `PARTICIPANTES` con §18 incluyendo `ARQ`, y nombrar la capacidad productora de `cambio-construido` en `A8`, `M6` y `M7` | `G-2` |
| 2.3 | Reescribir §7.4 contra `D69`: paso 2 con las dos ramas y el predicado de 1.2; retirar «§2.6 elimina el ramal de reversión por completo»; alinear el resumen §16 **L6876** con el cuerpo de `PN-7`; **y corregir L1458**, que aún afirma «ninguna de las dos rutas revierte nada» | `A3` + §6(d) |
| 2.4 | Bloque `D64`–`D68` en §15.8; dos filas nuevas en la tabla de la cabecera; corregir «CORREGIDO DOS VECES»; retirar de L62 y de L7081 la afirmación de que la tercera revisión sigue pendiente, que L7073 ya desmiente | `A4` |
| 2.5 | Declarar los **doce identificadores** `documental/<area>` junto a las doce materias, y corregir §5.6 y §5.7 para que su ejemplo use el identificador del área unificada | `G-4` |
| 2.6 | Declarar qué fase de `N` produce el baseline y la clasificación de desconocidos críticos, o registrar la reinterpretación de `O12` en instalación como presión normativa | `G-3` |

**NIVEL 3 — los medios que obligarían a F6 a decidir arquitectura**

| # | qué tiene que ocurrir | cierra |
|---|---|---|
| 3.1 | Alinear §2.6.10 L1917 con §3.6: «los cinco **campos** de procedencia», no «los cinco conceptos de `a.9`» — es condición de validación declarada | `A7` |
| 3.2 | Corregir la fila `preparada` de §3.6 **L3654**, que es la tabla de la que F6 deriva el esquema | `A13` (reclasificado a MEDIO) |
| 3.3 | Elegir un solo gate para `U6` y hacerlo coherente en §18 y §8.4 | `M-3` |
| 3.4 | Añadir la fila del mapa documental a §1.3, o reformular §4.3 L4156 y `PN-12` L6862 | `M-2` |
| 3.5 | Nombrar el actor de `APERTURA` y de `CAMPAÑA` en §5.3, y declarar si esa apertura cabe en la autoridad que `DSP/CAPACIDAD.md` L51–54 le escribe | `M-5` |
| 3.6 | Declarar las preguntas que `A3` debe responder, o remitir explícitamente al §6.2 de la directiva como su contrato; desglosar §15.2 fila 6 | `M-9` |
| 3.7 | Declarar en §8 cómo interactúa cada macrocircuito con el FRENO 3 —excepción aplicable, agrupación en menos items, o presión registrada—, **y declarar de paso cuántos items compone cada macrocircuito**, que hoy sólo consta para `N0`–`N5` | `M-7` |
| 3.8 | O un artefacto derivado equivalente para los `deriva` sin reparar, legible sin herramienta como `R1` exige; o rehacer la justificación del marcador sobre lo que de verdad compra | `A8` |
| 3.9 | O una autoridad nombrada que pueda cerrar el desenlace `4b`, o reformular `X58` y L1457 para que digan lo que el diseño sostiene: bloqueo acotado **por acto de autoridad**, no por construcción | `A9` |
| 3.10 | Reformular L1639 sobre el sujeto correcto: ningún **fichero canónico** en su `hash_posterior_esperado`; el evento `preparada` **sí conserva** los suyos | `A5` (reclasificado a MEDIO) |
| 3.11 | Añadir `capacidades/ENC/` a las extensiones de ficha de §5.2 y §17, con la entrada «finding clasificable» | `M-6` |

**NIVEL 4 — recuentos y citas: no cambian el diseño, pero hacen inservible el inventario del gate**

| # | qué tiene que ocurrir | cierra |
|---|---|---|
| 4.1 | «CATORCE» → «TRECE» en L4174 y «14» → «13» en L4191, o declarar cuál es la decimocuarta | `M-1` |
| 4.2 | Retirar `R1`–`R9` de §19 L7060 y de §2.9 L2816, y renombrar el conjunto retirado para deshacer la colisión con `R1`–`R8` de §2.1 | `M-8` ≡ `A11` |
| 4.3 | L513 → «cinco fases, dos rutas, dos cierres»; L3327–3328 y L3637–3640 → 5 fases, 6 estados del campo, 7 filas | `A6` |
| 4.4 | L100 → «DIEZ puntos», y nota al pie de `O15` que reancle su cifra sin tocar la resolución | `A10` + `m-1` |
| 4.5 | Corregir el resumen de `D67` en el registro: «propagar a las fuentes, `proceso:DEP`» | `M-4` |
| 4.6 | Retirar «un único escritor» de la lista de protecciones de la rama canónica en L2041 y L1929; lo que serializa `main` entre máquinas es el CAS de Git | `A12` |
| 4.7 | Mover la nota de procedencia de `O7`–`O14` delante de la sección de `O16`; rotular `U5a` en §18 | `m-2`, `m-4` |
| 4.8 | Declarar `python_requires ≥ 3.11` en el tooling y comprobarlo antes de correr, para que `T148`/`T159` no suban a la capa de certificación como defecto del producto | `A14` (fuera de F4) |

**Nota final para quien reciba esto.** El patrón que A describe —«decisiones bien tomadas y aplicadas a la mitad de los sitios que las invocan»— lo confirmo, **y lo extiendo al eje de B**: `D67` asignó procesos sin comprobar que sus condicionales admitieran los participantes ya declarados, y `D68` corrigió el recuento documental obligatorio y reprodujo el mismo modo de fallo en el condicional. **Ninguno de los diez hallazgos de nivel 1 y 2 exige una decisión arquitectónica nueva del Owner**: todos se cierran propagando decisiones que el propio corpus ya tomó correctamente en otra sede. Eso es lo mejor que puedo decir de este entregable, y no cambia el veredicto.
